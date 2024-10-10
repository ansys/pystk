import * as fs from "fs";

import { ConsoleInterface } from "pyright-internal/common/console";
import { Uri } from "pyright-internal/common/uri/uri";

import { ServiceProvider } from "pyright-internal/common/serviceProvider";
import { getPathRelativeToRoot } from "./fileUtilities";

export class CodeEdit {
  constructor(
    readonly filepath: string,
    readonly line: number,
    readonly startPosition: number,
    readonly endPosition: number,
    readonly newText: string
  ) {}
}

export class CodeEditor {
  replacements: { [file: string]: CodeEdit[] } = {};
  numberOfEdits: number = 0;

  constructor(
    private readonly serviceProvider: ServiceProvider,
    private output: ConsoleInterface
  ) {}

  recordEdits(edits: CodeEdit[]) {
    for (const edit of edits) {
      this.recordEdit(edit);
    }
  }

  recordEdit(edit: CodeEdit) {
    ++this.numberOfEdits;

    if (!(edit.filepath in this.replacements)) {
      this.replacements[edit.filepath] = [];
    }

    this.replacements[edit.filepath].push(edit);
  }

  public getNumberOfEdits() {
    return this.numberOfEdits;
  }

  public applyEdits() {
    for (const filePath in this.replacements) {
      const textEditList: CodeEdit[] = this.replacements[filePath]
        .sort((a: CodeEdit, b: CodeEdit) => {
          if (a.line === b.line) {
            return a.startPosition - b.startPosition;
          } else {
            return a.line - b.line;
          }
        })
        .filter((a: CodeEdit, index: number, arr: CodeEdit[]) => {
          return (
            arr.findIndex(
              (b: CodeEdit) =>
                a.filepath === b.filepath &&
                a.line === b.line &&
                a.startPosition === b.startPosition &&
                a.endPosition === b.endPosition
            ) === index
          );
        })
        .reverse();

      const content: string = fs.readFileSync(filePath).toString();
      const lines: string[] = content.split(/\r?\n/).flat();

      for (const textEdit of textEditList) {
        const lineno = textEdit.line;
        const line = lines[lineno];
        this.output.log(
          `${getPathRelativeToRoot(Uri.file(filePath, this.serviceProvider))}:${
            textEdit.line + 1
          } Replacing "${line.substring(
            textEdit.startPosition,
            textEdit.endPosition
          )}" by "${textEdit.newText}"`
        );
        lines[lineno] =
          line.substring(0, textEdit.startPosition) +
          textEdit.newText +
          line.substring(textEdit.endPosition);
      }

      fs.writeFileSync(filePath, lines.join("\n"), "utf-8");
    }
  }
}
