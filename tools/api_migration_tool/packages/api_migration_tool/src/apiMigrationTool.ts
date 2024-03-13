/* eslint-disable */
/* eslint-enable */

import { StandardConsole } from "pyright-internal/common/console";
import { CodeEdit, CodeEditor } from "./codeEditor";
import { CodeScanner } from "./codeScanner";
import { CommandLineStatus, processArgs } from "./options";

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

  const output = new StandardConsole(args.commandLineOptions.logLevel);

  let codeScanner: CodeScanner = new CodeScanner(
    args.commandLineOptions,
    output
  );
  let codeEdits: CodeEdit[] = codeScanner.scan();

  output.info("Creating code edits...");

  const codeEditor = new CodeEditor(output);
  codeEditor.recordEdits(codeEdits);

  output.info("Applying migrations");

  codeEditor.applyEdits();
}

// Necessary to allow the fallback typeshed directory to be located
// when running dist\api_migration_tool.js from the command line.
(global as any).__rootDirectory = __dirname;

main();
