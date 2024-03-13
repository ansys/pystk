import { ImportResolver } from "pyright-internal/analyzer/importResolver";
import { Program } from "pyright-internal/analyzer/program";
import { ConfigOptions } from "pyright-internal/common/configOptions";
import {
  ConsoleInterface,
  StandardConsole,
} from "pyright-internal/common/console";
import { FullAccessHost } from "pyright-internal/common/fullAccessHost";
import { getHeapStatistics } from "pyright-internal/common/memUtils";
import { createFromRealFileSystem } from "pyright-internal/common/realFileSystem";

import { CancellationTokenSource } from "vscode-jsonrpc";

import Path from "path";
import { CodeEdit } from "./codeEditor";
import { DeclarationLocator } from "./declarationLocator";
import {
  findFiles,
  getPathRelativeToRoot,
  pathIsChild,
  readMappingFileDirectory,
  setRootDirectory,
} from "./fileUtilities";
import { CommandLineOptions } from "./options";
import { ReferenceLocator } from "./referenceLocator";
import { SymbolRenameRecord } from "./symbolRenameRecord";

export class CodeScanner {
  constructor(
    private options: CommandLineOptions,
    private output: ConsoleInterface
  ) {}

  public scan(): CodeEdit[] {
    let result: CodeEdit[] = [];

    if (
      this.options.rootDirectory === undefined ||
      this.options.xmlMappingsDirectory === undefined
    ) {
      return result;
    }

    console.log(`Global root directory: ${(global as any).__rootDirectory}`);

    const rootDirectory = this.options.rootDirectory;
    const xmlMappingsDir = this.options.xmlMappingsDirectory;

    setRootDirectory(rootDirectory);

    const output = new StandardConsole(this.options.logLevel);

    output.info(`Root directory: ${rootDirectory}`);

    const fs = createFromRealFileSystem(output);

    const pythonFileList: string[] = findFiles(
      fs,
      rootDirectory,
      ".py",
      output
    );

    output.info(
      `Found ${pythonFileList.length} ` +
        `source ${pythonFileList.length === 1 ? "file" : "files"}`
    );

    const xmlMappingFileList: string[] = findFiles(
      fs,
      xmlMappingsDir,
      ".xml",
      output
    );

    output.info(
      `Found ${xmlMappingFileList.length} ` +
        `mapping ${xmlMappingFileList.length === 1 ? "file" : "files"}`
    );

    const configOptions = new ConfigOptions(
      rootDirectory,
      this.options.strict ? "strict" : undefined
    );

    configOptions.defaultPythonPlatform = this.options.pythonPlatform;

    const importResolver = new ImportResolver(
      fs,
      configOptions,
      new FullAccessHost(fs)
    );

    const cancellationTokenSource = new CancellationTokenSource();

    const program = new Program(importResolver, configOptions, output);
    program.setTrackedFiles(pythonFileList);

    const symbolsToRename: SymbolRenameRecord[] = [];

    output.info("Processing XML input files and finding declarations...");

    readMappingFileDirectory(
      xmlMappingsDir,
      fs,
      rootDirectory,
      output,
      (pythonFilePath: string, mappings: any) => {
        let declarationLocator = new DeclarationLocator(
          pythonFilePath,
          program,
          cancellationTokenSource
        );

        for (const mapping of mappings) {
          let declaration = declarationLocator.findDeclaration(
            mapping.oldName,
            mapping.parentScope,
            mapping.category
          );

          if (declaration) {
            output.log(`${mapping.oldName} -> ${mapping.newName}`);
            symbolsToRename.push(
              new SymbolRenameRecord(
                mapping.oldName,
                mapping.newName,
                declaration
              )
            );
          }
        }
      }
    );

    output.info("Finding references...");

    let referenceLocator = new ReferenceLocator(
      program,
      cancellationTokenSource,
      output
    );

    for (const curSourceFileInfo of program.getSourceFileInfoList()) {
      const currentSourceFilePath = curSourceFileInfo.sourceFile.getFilePath();
      const isExcluded =
        this.options.skipDirectories.some((element) =>
          pathIsChild(currentSourceFilePath, element)
        ) || !pathIsChild(currentSourceFilePath, this.options.rootDirectory);

      let regex = undefined;
      if (this.options.fileFilter !== undefined) {
        let filter = this.options.fileFilter;
        if (filter.startsWith('"') && filter.endsWith('"')) {
          filter = filter.slice(1, -1);
        }
        regex = new RegExp(filter);
      }

      if (
        isExcluded ||
        Path.extname(currentSourceFilePath) !== ".py" ||
        (regex !== undefined && !regex.test(currentSourceFilePath))
      ) {
        continue;
      }

      output.info(
        `Processing ${getPathRelativeToRoot(
          curSourceFileInfo.sourceFile.getFilePath()
        )}`
      );

      referenceLocator.populateReferences(symbolsToRename, curSourceFileInfo);

      // This operation can consume significant memory, so check
      // for situations where we need to discard the type cache.
      //program.handleMemoryHighUsage();

      if (global.gc) {
        const heapStats = getHeapStatistics();
        if (heapStats.malloced_memory > 4192 * 1024 * 1024) {
          global.gc();
        }
      }
    }

    for (const symbolToRename of symbolsToRename) {
      symbolToRename.referencesResult.locations.forEach((loc) => {
        result.push(
          new CodeEdit(
            loc.path,
            loc.range.start.line,
            loc.range.start.character,
            loc.range.end.character,
            symbolToRename.newName
          )
        );
      });
    }

    return result;
  }
}
