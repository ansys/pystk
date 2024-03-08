import * as fs from "fs";

import { ConsoleInterface } from "pyright-internal/common/console";
import { Range } from "pyright-internal/common/textRange";

import { TextEdit } from "vscode-languageserver";

import { getPathRelativeToRoot } from "./fileUtilities";

export class CodeEditor {
  replacements: { [file: string]: TextEdit[] } = {};

  constructor(private output: ConsoleInterface) {}

  recordEdit(fileName: string, range: Range, newText: string) {
    if (!(fileName in this.replacements)) {
      this.replacements[fileName] = [];
    }

    this.replacements[fileName].push({
      range: range,
      newText: newText,
    });
  }

  public applyEdits() {
    for (const filePath in this.replacements) {
      const textEditList: TextEdit[] = this.replacements[filePath]
        .sort((a: TextEdit, b: TextEdit) => {
          if (a.range.start.line === b.range.start.line) {
            return a.range.start.character - b.range.start.character;
          } else {
            return a.range.start.line - b.range.start.line;
          }
        })
        .reverse();

      const content: string = fs.readFileSync(filePath).toString();
      const lines: string[] = content.split(/\r?\n/).flat();

      for (const textEdit of textEditList) {
        const lineno = textEdit.range.start.line;
        const line = lines[lineno];
        this.output.log(
          `${getPathRelativeToRoot(filePath)}:${
            textEdit.range.start.line + 1
          } Replacing "${line.substring(
            textEdit.range.start.character,
            textEdit.range.end.character
          )}" by "${textEdit.newText}"`
        );
        lines[lineno] =
          line.substring(0, textEdit.range.start.character) +
          textEdit.newText +
          line.substring(textEdit.range.end.character);
      }

      fs.writeFileSync(filePath, lines.join("\n"), "utf-8");
    }
  }
}
