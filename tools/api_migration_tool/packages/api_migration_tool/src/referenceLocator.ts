import { ConsoleInterface } from "pyright-internal/common/console";
import {
  ProgramView,
  SourceFileInfo,
} from "pyright-internal/common/extensibility";
import { ReferencesProvider } from "pyright-internal/languageService/referencesProvider";
import { CancellationTokenSource } from "vscode-jsonrpc";

import { SymbolRenameRecord } from "./symbolRenameRecord";

export class ReferenceLocator {
  private referenceProvider: ReferencesProvider;

  constructor(
    private program: ProgramView,
    private cancellationTokenSource: CancellationTokenSource,
    private output: ConsoleInterface
  ) {
    this.referenceProvider = new ReferencesProvider(
      program,
      cancellationTokenSource.token
    );
  }

  public populateReferences(
    symbolRenameRecords: SymbolRenameRecord[],
    sourceFileInfo: SourceFileInfo
  ): void {
    const content = sourceFileInfo.sourceFile.getFileContent() ?? "";

    for (const symbol of symbolRenameRecords) {
      // Make sure searching symbol name exists in the file.
      if (content.indexOf(symbol.oldName) < 0) {
        continue;
      }

      let initialCount = symbol.referencesResult.locations.length;

      this.referenceProvider.addReferencesToResult(
        sourceFileInfo.sourceFile.getFilePath(),
        /* includeDeclaration */ false,
        symbol.referencesResult
      );

      this.output.log(
        `Found ${
          symbol.referencesResult.locations.length - initialCount
        } references to ${symbol.oldName}`
      );
    }
  }
}
