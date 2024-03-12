import { ProgramView } from "pyright-internal/common/extensibility";
import { Position } from "pyright-internal/common/textRange";
import { DocumentSymbolCollectorUseCase } from "pyright-internal/languageService/documentSymbolCollector";
import { DocumentSymbolProvider } from "pyright-internal/languageService/documentSymbolProvider";
import {
  ReferencesProvider,
  ReferencesResult,
} from "pyright-internal/languageService/referencesProvider";
import { CancellationTokenSource } from "vscode-jsonrpc";
import { DocumentSymbol, SymbolKind } from "vscode-languageserver";

class FlatDocumentSymbol {
  readonly name: string;
  containerName: string | undefined;
  readonly kind: SymbolKind;
  readonly location: Position;

  constructor(documentSymbol: DocumentSymbol) {
    this.name = documentSymbol.name;
    this.kind = documentSymbol.kind;
    this.location = documentSymbol.selectionRange.start;
  }
}

export class DeclarationLocator {
  private flatDocumentSymbols: FlatDocumentSymbol[];

  constructor(
    private filePath: string,
    private program: ProgramView,
    private cancellationTokenSource: CancellationTokenSource
  ) {
    const documentSymbolProvider = new DocumentSymbolProvider(
      program,
      filePath,
      true, // hasHierarchicalDocumentSymbolCapability
      cancellationTokenSource.token
    );

    const documentSymbols =
      documentSymbolProvider.getSymbols() as DocumentSymbol[];

    this.flatDocumentSymbols =
      DeclarationLocator.flattenDocumentSymbols(documentSymbols);
  }

  public findDeclaration(
    symbolName: string,
    parentScope: string,
    category: string
  ): ReferencesResult | undefined {
    const symbol = DeclarationLocator.findSymbol(
      this.flatDocumentSymbols,
      symbolName,
      parentScope,
      category
    );

    if (symbol) {
      const referencesResult = ReferencesProvider.getDeclarationForPosition(
        this.program,
        this.filePath,
        symbol.location,
        /* reporter */ undefined,
        DocumentSymbolCollectorUseCase.Rename,
        this.cancellationTokenSource.token
      );

      return referencesResult;
    }

    return undefined;
  }

  private static compareCategory(category: string, kind: SymbolKind): boolean {
    return (
      (category == "class" && kind == SymbolKind.Class) ||
      (category == "interface" && kind == SymbolKind.Class) || // pyright uses SymbolKind.Class for interfaces
      (category == "enum_type" && kind == SymbolKind.Class) || // pyright uses SymbolKind.Class for enumeration types
      (category == "method" && kind == SymbolKind.Method) ||
      (category == "enum_value" && kind == SymbolKind.Variable) // pyright uses SymbolKind.Variable for enumeration values
    );
  }

  private static findSymbol(
    flatDocumentSymbols: FlatDocumentSymbol[],
    name: string,
    parentScope: string,
    category: string
  ): FlatDocumentSymbol | undefined {
    for (const symbol of flatDocumentSymbols) {
      if (
        symbol.name == name &&
        ((!parentScope && !symbol.containerName) ||
          parentScope == symbol.containerName) &&
        DeclarationLocator.compareCategory(category, symbol.kind)
      ) {
        return symbol;
      }
    }

    return undefined;
  }

  private static flattenDocumentSymbols(symbolList: DocumentSymbol[]) {
    const flatSymbols: FlatDocumentSymbol[] = [];
    for (const symbol of symbolList) {
      DeclarationLocator.flattenDocumentSymbolsRecursive(flatSymbols, symbol);
    }
    return flatSymbols;
  }

  private static flattenDocumentSymbolsRecursive(
    symbolList: FlatDocumentSymbol[],
    symbol: DocumentSymbol,
    path?: string
  ) {
    const flatSymbol: FlatDocumentSymbol = new FlatDocumentSymbol(symbol);

    if (path) {
      flatSymbol.containerName = path;
    }

    symbolList.push(flatSymbol);

    if (symbol.children) {
      const currentPath = path ? path + "." + symbol.name : symbol.name;
      for (const child of symbol.children) {
        DeclarationLocator.flattenDocumentSymbolsRecursive(
          symbolList,
          child,
          currentPath
        );
      }
    }
  }
}
