import { ImportResolver } from "pyright-internal/analyzer/importResolver";
import { Program } from "pyright-internal/analyzer/program";
import { ConfigOptions } from "pyright-internal/common/configOptions";
import { ConsoleInterface } from "pyright-internal/common/console";
import { FileSystem } from "pyright-internal/common/fileSystem";
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
  private fs: FileSystem;
  private rootDirectory: string;
  private pythonFileList: string[];
  private filesToScan: string[];

  constructor(
    private options: CommandLineOptions,
    private output: ConsoleInterface
  ) {
    this.output.info(
      `Global root directory: ${(global as any).__rootDirectory}`
    );

    this.rootDirectory = this.options.rootDirectory!;

    setRootDirectory(this.rootDirectory);

    this.output.info(`Root directory: ${this.rootDirectory}`);

    this.fs = createFromRealFileSystem(this.output);

    this.pythonFileList = findFiles(
      this.fs,
      this.rootDirectory!,
      ".py",
      this.output
    );

    this.filesToScan = this.pythonFileList.filter(
      (path) => !this.isFileExcluded(path)
    );

    this.output.info(
      `Found ${this.pythonFileList.length} ` +
        `source ${this.pythonFileList.length === 1 ? "file" : "files"}, ${
          this.filesToScan.length
        } ${this.filesToScan.length === 1 ? "file" : "files"} to migrate`
    );
  }

  public getFilesToScan(): string[] {
    return this.filesToScan;
  }

  private isFileExcluded(filePath: string): boolean {
    const isExcluded =
      this.options.skipDirectories.some((element) =>
        pathIsChild(filePath, element)
      ) || !pathIsChild(filePath, this.rootDirectory);

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
      Path.extname(filePath) !== ".py" ||
      (regex !== undefined && !regex.test(filePath))
    ) {
      return true;
    }

    return false;
  }

  public scan(
    begin: number | undefined = undefined,
    end: number | undefined = undefined
  ): CodeEdit[] {
    let result: CodeEdit[] = [];

    const xmlMappingsDir = this.options.xmlMappingsDirectory!;

    const xmlMappingFileList: string[] = findFiles(
      this.fs,
      xmlMappingsDir,
      ".xml",
      this.output
    );

    this.output.info(
      `Found ${xmlMappingFileList.length} ` +
        `mapping ${xmlMappingFileList.length === 1 ? "file" : "files"}`
    );

    const configOptions = new ConfigOptions(
      this.rootDirectory!,
      this.options.strict ? "strict" : undefined
    );

    configOptions.defaultPythonPlatform = this.options.pythonPlatform;

    const importResolver = new ImportResolver(
      this.fs,
      configOptions,
      new FullAccessHost(this.fs)
    );

    const cancellationTokenSource = new CancellationTokenSource();

    const program = new Program(importResolver, configOptions, this.output);
    program.setTrackedFiles(this.pythonFileList);

    const symbolsToRename: SymbolRenameRecord[] = [];

    this.output.info("Processing XML input files and finding declarations...");

    readMappingFileDirectory(
      xmlMappingsDir,
      this.fs,
      this.rootDirectory,
      this.output,
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
            this.output.log(`${mapping.oldName} -> ${mapping.newName}`);
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

    this.output.info("Finding references...");

    let referenceLocator = new ReferenceLocator(
      program,
      cancellationTokenSource,
      this.output
    );

    const sliceToScan = this.filesToScan.slice(begin, end);
    for (const currentSourceFilePath of sliceToScan) {
      this.output.info(
        `Processing ${getPathRelativeToRoot(currentSourceFilePath)}`
      );

      referenceLocator.populateReferences(
        symbolsToRename,
        program.getSourceFileInfo(currentSourceFilePath)!
      );

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
