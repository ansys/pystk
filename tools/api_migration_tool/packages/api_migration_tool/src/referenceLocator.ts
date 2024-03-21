import { ConsoleInterface } from "pyright-internal/common/console";
import {
  ProgramView,
  SourceFileInfo,
} from "pyright-internal/common/extensibility";
import { DocumentRange } from "pyright-internal/common/textRange";
import { FindReferencesTreeWalker } from "pyright-internal/languageService/referencesProvider";
import { CancellationTokenSource } from "vscode-jsonrpc";

import { SymbolRenameRecord } from "./symbolRenameRecord";

export class Reference {
  constructor(
    readonly oldName: string,
    readonly newName: string,
    readonly occurrences: DocumentRange[]
  ) {}
}

export class ReferenceLocator {
  constructor(
    private program: ProgramView,
    private cancellationTokenSource: CancellationTokenSource,
    private output: ConsoleInterface
  ) {}

  public getReferences(
    symbolRenameRecords: SymbolRenameRecord[],
    sourceFileInfo: SourceFileInfo
  ): Reference[] {
    const result: Reference[] = [];

    const content = sourceFileInfo.sourceFile.getFileContent() ?? "";

    for (const symbol of symbolRenameRecords) {
      // Make sure searching symbol name exists in the file.
      if (content.indexOf(symbol.oldName) < 0) {
        continue;
      }

      const refTreeWalker = new FindReferencesTreeWalker(
        this.program,
        sourceFileInfo.sourceFile.getFilePath(),
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

    return result;
  }
}
