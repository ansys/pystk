import { Program } from "pyright-internal/analyzer/program";
import { ConsoleInterface } from "pyright-internal/common/console";
import { SourceFileInfo } from "pyright-internal/common/extensibility";
import { ServiceProvider } from "pyright-internal/common/serviceProvider";
import { Uri } from "pyright-internal/common/uri/uri";
import {
  FindReferencesTreeWalker,
  LocationWithNode,
} from "pyright-internal/languageService/referencesProvider";
import { CancellationTokenSource } from "vscode-jsonrpc";

import { SymbolRenameRecord } from "./symbolRenameRecord";

export class Reference {
  constructor(
    readonly oldName: string,
    readonly newName: string,
    readonly occurrences: LocationWithNode[]
  ) {}
}

export class ReferenceLocator {
  constructor(
    private program: Program,
    private cancellationTokenSource: CancellationTokenSource,
    private output: ConsoleInterface,
    private readonly serviceProvider: ServiceProvider
  ) {}

  public getReferences(
    symbolRenameRecords: SymbolRenameRecord[],
    sourceFileInfo: SourceFileInfo
  ): Reference[] {
    const result: Reference[] = [];

    const content = sourceFileInfo.sourceFile.getFileContent() ?? "";

    //this.program.setFileOpened(sourceFileInfo!.sourceFile.getUri(), 1, content);

    for (const symbol of symbolRenameRecords) {
      // Make sure searching symbol name exists in the file.
      if (content.indexOf(symbol.oldName) < 0) {
        continue;
      }

      const refTreeWalker = new FindReferencesTreeWalker(
        this.program,
        Uri.file(
          sourceFileInfo.sourceFile.getUri().getFilePath(),
          this.serviceProvider
        ),
        symbol.referencesResult,
        /* includeDeclaration */ true,
        this.cancellationTokenSource.token
      );

      let references = refTreeWalker.findReferences();
      result.push(new Reference(symbol.oldName, symbol.newName, references));

      this.output.log(
        `Found ${references.length} references to ${symbol.oldName}`
      );
    }

    //this.program.setFileClosed(sourceFileInfo!.sourceFile.getUri());
    return result;
  }
}
