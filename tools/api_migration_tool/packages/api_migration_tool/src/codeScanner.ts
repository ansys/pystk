import { ImportResolver } from "pyright-internal/analyzer/importResolver";
import { Program } from "pyright-internal/analyzer/program";
import { ConfigOptions } from "pyright-internal/common/configOptions";
import { ConsoleInterface } from "pyright-internal/common/console";
import { FileSystem } from "pyright-internal/common/fileSystem";
import { FullAccessHost } from "pyright-internal/common/fullAccessHost";
import { getHeapStatistics } from "pyright-internal/common/memUtils";
import {
  RealTempFile,
  createFromRealFileSystem,
} from "pyright-internal/common/realFileSystem";
import { ServiceProvider } from "pyright-internal/common/serviceProvider";

import { CancellationTokenSource } from "vscode-jsonrpc";

import { Uri } from "pyright-internal/common/uri/uri";
import { CodeEdit } from "./codeEditor";
import { DeclarationLocator } from "./declarationLocator";
import {
  findFiles,
  getPathRelativeToRoot,
  readMappingFileDirectory,
  setRootDirectory,
} from "./fileUtilities";
import { CommandLineOptions } from "./options";
import { Reference, ReferenceLocator } from "./referenceLocator";
import { SymbolRenameRecord } from "./symbolRenameRecord";

export class CodeScanner {
  private rootDirectory: Uri;
  private pythonFileList: Uri[];
  private filesToScan: Uri[];
  private cancellationTokenSource: CancellationTokenSource;
  private program: Program | undefined;
  private symbolsToRename: SymbolRenameRecord[] = [];

  constructor(
    private options: CommandLineOptions,
    private output: ConsoleInterface,
    private readonly serviceProvider: ServiceProvider,
    private readonly fs: FileSystem,
    private silent: boolean = false
  ) {
    if (!silent) {
      this.output.info(
        `Global root directory: ${(global as any).__rootDirectory}`
      );
    }

    this.rootDirectory = Uri.file(this.options.rootDirectory!, serviceProvider);

    setRootDirectory(this.rootDirectory);

    if (!silent) {
      this.output.info(`Root directory: ${this.rootDirectory.getFilePath()}`);
    }

    const tempFile = new RealTempFile();
    this.fs = createFromRealFileSystem(tempFile, this.output);

    this.pythonFileList = findFiles(
      this.fs,
      this.rootDirectory!,
      ".py",
      this.output,
      this.serviceProvider
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

  public getFilesToScan(): Uri[] {
    return this.filesToScan;
  }

  private isFileExcluded(filePath: Uri): boolean {
    const isExcluded = this.options.skipDirectories.some(
      (element) =>
        filePath.isChild(Uri.file(element, this.serviceProvider)) ||
        !filePath.isChild(this.rootDirectory)
    );

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
      !filePath.hasExtension(".py") ||
      (regex !== undefined && !regex.test(filePath.getFilePath()))
    ) {
      return true;
    }

    return false;
  }

  public prepareScan() {
    const jsonMappingsDir = Uri.file(
      this.options.jsonMappingsDirectory!,
      this.serviceProvider
    );

    const jsonMappingFileList: Uri[] = findFiles(
      this.fs,
      jsonMappingsDir,
      ".json",
      this.output,
      this.serviceProvider
    );

    if (!this.silent) {
      this.output.info(
        `Found ${jsonMappingFileList.length} ` +
          `mapping ${jsonMappingFileList.length === 1 ? "file" : "files"}`
      );
    }

    const configOptions = new ConfigOptions(this.rootDirectory!);

    if (this.options.strict) {
      configOptions.initializeTypeCheckingMode("strict");
    }

    configOptions.defaultPythonPlatform = this.options.pythonPlatform;

    const importResolver = new ImportResolver(
      this.serviceProvider,
      configOptions,
      new FullAccessHost(this.serviceProvider)
    );

    this.program = new Program(
      importResolver,
      configOptions,
      this.serviceProvider
    );
    this.program.setTrackedFiles(this.pythonFileList);
    this.program
      .getSourceFileInfoList()
      .forEach((fileInfo) =>
        this.program!.setFileOpened(
          fileInfo.sourceFile.getUri(),
          1,
          fileInfo.sourceFile.getFileContent()!
        )
      );

    if (!this.silent) {
      this.output.info(
        "Processing JSON input files and finding declarations..."
      );
    }

    readMappingFileDirectory(
      jsonMappingsDir,
      this.fs,
      this.rootDirectory,
      this.output,
      this.serviceProvider,
      (pythonFilePath: string, mappings: any) => {
        let declarationLocator = new DeclarationLocator(
          pythonFilePath,
          this.program!,
          this.serviceProvider,
          this.cancellationTokenSource
        );

        for (const mapping of mappings) {
          let declaration = declarationLocator.findDeclaration(
            mapping.oldName,
            mapping.parentScope,
            mapping.category,
            this.serviceProvider
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
      this.output,
      this.serviceProvider
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
      for (const symbolOccurence of symbolReference.occurrences) {
        result.push(
          new CodeEdit(
            symbolOccurence.location.uri.getFilePath(),
            symbolOccurence.location.range.start.line,
            symbolOccurence.location.range.start.character,
            symbolOccurence.location.range.end.character,
            symbolReference.newName
          )
        );
      }
    }

    return result;
  }
}
