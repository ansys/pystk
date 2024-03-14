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
import { Reference, ReferenceLocator } from "./referenceLocator";
import { SymbolRenameRecord } from "./symbolRenameRecord";

export class CodeScanner {
  private fs: FileSystem;
  private rootDirectory: string;
  private pythonFileList: string[];
  private filesToScan: string[];
  private cancellationTokenSource: CancellationTokenSource;
  private program: Program | undefined;
  private symbolsToRename: SymbolRenameRecord[] = [];

  constructor(
    private options: CommandLineOptions,
    private output: ConsoleInterface,
    private silent: boolean = false
  ) {
    if (!silent) {
      this.output.info(
        `Global root directory: ${(global as any).__rootDirectory}`
      );
    }

    this.rootDirectory = this.options.rootDirectory!;

    setRootDirectory(this.rootDirectory);

    if (!silent) {
      this.output.info(`Root directory: ${this.rootDirectory}`);
    }

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

    // Sort the files by size so the largest files are
    // processed first
    // This helps with load balancing when splitting
    // work across multiple worker processes
    this.filesToScan.sort((a, b) => {
      return this.fs.statSync(b).size - this.fs.statSync(a).size;
    });

    if (!silent) {
      this.output.info(
        `Found ${this.pythonFileList.length} ` +
          `source ${this.pythonFileList.length === 1 ? "file" : "files"}, ${
            this.filesToScan.length
          } ${this.filesToScan.length === 1 ? "file" : "files"} to migrate`
      );
    }

    this.cancellationTokenSource = new CancellationTokenSource();
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

  public prepareScan() {
    const xmlMappingsDir = this.options.xmlMappingsDirectory!;

    const xmlMappingFileList: string[] = findFiles(
      this.fs,
      xmlMappingsDir,
      ".xml",
      this.output
    );

    if (!this.silent) {
      this.output.info(
        `Found ${xmlMappingFileList.length} ` +
          `mapping ${xmlMappingFileList.length === 1 ? "file" : "files"}`
      );
    }

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

    this.program = new Program(importResolver, configOptions, this.output);
    this.program.setTrackedFiles(this.pythonFileList);

    if (!this.silent) {
      this.output.info(
        "Processing XML input files and finding declarations..."
      );
    }

    readMappingFileDirectory(
      xmlMappingsDir,
      this.fs,
      this.rootDirectory,
      this.output,
      (pythonFilePath: string, mappings: any) => {
        let declarationLocator = new DeclarationLocator(
          pythonFilePath,
          this.program!,
          this.cancellationTokenSource
        );

        for (const mapping of mappings) {
          let declaration = declarationLocator.findDeclaration(
            mapping.oldName,
            mapping.parentScope,
            mapping.category
          );

          if (declaration) {
            this.output.log(`${mapping.oldName} -> ${mapping.newName}`);
            this.symbolsToRename.push(
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
  }

  public scan(
    begin: number | undefined = undefined,
    end: number | undefined = undefined
  ): CodeEdit[] {
    let result: CodeEdit[] = [];

    if (this.program === undefined) {
      throw new Error("prepareScan() must be called first");
    }

    if (!this.silent) {
      this.output.info("Finding references...");
    }

    let referenceLocator = new ReferenceLocator(
      this.program,
      this.cancellationTokenSource,
      this.output
    );

    const allSymbolReferences: Reference[] = [];
    const sliceToScan = this.filesToScan.slice(begin, end);
    for (const currentSourceFilePath of sliceToScan) {
      this.output.info(
        `Processing ${getPathRelativeToRoot(currentSourceFilePath)}`
      );

      allSymbolReferences.push(
        ...referenceLocator.getReferences(
          this.symbolsToRename,
          this.program.getSourceFileInfo(currentSourceFilePath)!
        )
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

    for (const symbolReference of allSymbolReferences) {
      for (const symbolOccurence of symbolReference.occurences) {
        result.push(
          new CodeEdit(
            symbolOccurence.path,
            symbolOccurence.range.start.line,
            symbolOccurence.range.start.character,
            symbolOccurence.range.end.character,
            symbolReference.newName
          )
        );
      }
    }

    return result;
  }
}
