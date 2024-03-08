/* eslint-disable */
/* eslint-enable */

import { CacheManager } from "pyright-internal/analyzer/cacheManager";
import { ImportResolver } from "pyright-internal/analyzer/importResolver";
import { Program } from "pyright-internal/analyzer/program";
import { ConfigOptions } from "pyright-internal/common/configOptions";
import { StandardConsole } from "pyright-internal/common/console";
import { FullAccessHost } from "pyright-internal/common/fullAccessHost";
import { getHeapStatistics } from "pyright-internal/common/memUtils";
import { createFromRealFileSystem } from "pyright-internal/common/realFileSystem";
import { createServiceProvider } from "pyright-internal/common/serviceProviderExtensions";

import { CancellationTokenSource } from "vscode-jsonrpc";

import { Uri } from "pyright-internal/common/uri/uri";

import Path from "path";

import { CodeEditor } from "./codeEditor";
import { DeclarationLocator } from "./declarationLocator";
import {
  findFiles,
  getPathRelativeToRoot,
  readMappingFileDirectory,
  setRootDirectory,
} from "./fileUtilities";
import { CommandLineStatus, processArgs } from "./options";
import { ReferenceLocator } from "./referenceLocator";
import { SymbolRenameRecord } from "./symbolRenameRecord";

// Increase the default stack trace limit from 16 to 64 to help diagnose
// crashes with deep stack traces.
Error.stackTraceLimit = 64;

export function main() {
  if (process.env.NODE_ENV === "production") {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    require("source-map-support").install();
  }

  const args = processArgs();

  if (
    args.exitStatus != CommandLineStatus.Continue ||
    args.commandLineOptions === undefined
  ) {
    return;
  }

  const commandLineOptions = args.commandLineOptions;

  if (
    commandLineOptions.rootDirectory === undefined ||
    commandLineOptions.xmlMappingsDirectory === undefined
  ) {
    return;
  }

  console.log(`Global root directory: ${(global as any).__rootDirectory}`);

  const rootDirectory = commandLineOptions.rootDirectory;
  const xmlMappingsDir = commandLineOptions.xmlMappingsDirectory;

  setRootDirectory(rootDirectory);

  const output = new StandardConsole(commandLineOptions.logLevel);

  output.info(`Root directory: ${rootDirectory}`);

  const fs = createFromRealFileSystem(output);

  const pythonFileList: Uri[] = findFiles(fs, rootDirectory, ".py", output);

  output.info(
    `Found ${pythonFileList.length} ` +
      `source ${pythonFileList.length === 1 ? "file" : "files"}`
  );

  const xmlMappingFileList: Uri[] = findFiles(
    fs,
    xmlMappingsDir,
    ".xml",
    output
  );

  output.info(
    `Found ${xmlMappingFileList.length} ` +
      `mapping ${xmlMappingFileList.length === 1 ? "file" : "files"}`
  );

  const cacheManager = new CacheManager();
  const serviceProvider = createServiceProvider(fs, output, cacheManager);
  const configOptions = new ConfigOptions(
    Uri.file(rootDirectory),
    commandLineOptions.strict ? "strict" : undefined
  );

  configOptions.defaultPythonPlatform = commandLineOptions.pythonPlatform;

  const importResolver = new ImportResolver(
    serviceProvider,
    configOptions,
    new FullAccessHost(serviceProvider)
  );

  const cancellationTokenSource = new CancellationTokenSource();

  const program = new Program(importResolver, configOptions, serviceProvider);
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
    const currentSourceFilePath = curSourceFileInfo.sourceFile
      .getUri()
      .getFilePath();
    const isExcluded = commandLineOptions.skipDirectories.some((element) =>
      Uri.file(currentSourceFilePath).isChild(Uri.file(element))
    );
    if (isExcluded || Path.extname(currentSourceFilePath) !== ".py") {
      continue;
    }

    output.info(
      `Processing ${getPathRelativeToRoot(
        curSourceFileInfo.sourceFile.getUri().getFilePath()
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

  output.info("Creating code edits...");

  const codeEditor = new CodeEditor(output);

  for (const symbolToRename of symbolsToRename) {
    symbolToRename.referencesResult.locations.forEach((loc) => {
      codeEditor.recordEdit(
        loc.uri.getFilePath(),
        loc.range,
        symbolToRename.newName
      );
    });
  }

  output.info("Applying migrations");

  codeEditor.applyEdits();
}

// Necessary to allow the fallback typeshed directory to be located
// when running dist\api_migration_tool.js from the command line.
(global as any).__rootDirectory = __dirname;

main();
