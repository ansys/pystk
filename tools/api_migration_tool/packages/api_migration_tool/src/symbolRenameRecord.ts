import { ReferencesResult } from 'pyright-internal/languageService/referencesProvider';

export class SymbolRenameRecord {
    readonly oldName: string;
    readonly newName: string;
    readonly referencesResult: ReferencesResult;

    constructor(oldName: string, newName: string, referencesResult: ReferencesResult) {
        this.oldName = oldName;
        this.newName = newName;
        this.referencesResult = referencesResult;
    }
}

