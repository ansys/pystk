import cluster, { Worker } from "cluster";

import { StandardConsole } from "pyright-internal/common/console";
import { CodeEdit, CodeEditor } from "./codeEditor";
import { CodeScanner } from "./codeScanner";
import { CommandLineOptions, CommandLineStatus, processArgs } from "./options";

interface IWorkerMessage {
  commandLineOptions: CommandLineOptions | undefined;
  begin: number | undefined;
  end: number | undefined;
}

interface IWorkerResult {
  codeEdits: CodeEdit[] | undefined;
}

// Increase the default stack trace limit from 16 to 64 to help diagnose
// crashes with deep stack traces.
Error.stackTraceLimit = 64;

export function main() {
  if (process.env.NODE_ENV === "production") {
    // eslint-disable-next-line @typescript-eslint/no-var-requires
    require("source-map-support").install();
  }

  if (cluster.isPrimary) {
    const args = processArgs();

    if (
      args.exitStatus != CommandLineStatus.Continue ||
      args.commandLineOptions === undefined
    ) {
      return;
    }

    const output = new StandardConsole(args.commandLineOptions.logLevel);

    const numJobs = args.commandLineOptions.numberOfJobs;
    if (numJobs != 0) {
      output.info(`Using ${numJobs} jobs`);
    }

    if (numJobs < 2) {
      // Run directly in current process
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
    } else {
      // Run in parallel

      let codeScanner: CodeScanner = new CodeScanner(
        args.commandLineOptions,
        output
      );

      let workers: Worker[] = [];
      for (let i = 0; i < numJobs; i++) {
        workers.push(cluster.fork());
      }

      const numFilesToScan = codeScanner.getFilesToScan().length;
      let sliceCount = Math.floor(numFilesToScan / numJobs);

      const codeEditor = new CodeEditor(output);

      for (let i = 0; i < numJobs; i++) {
        const begin = i * sliceCount;
        let end = (i + 1) * sliceCount;
        if (i == numJobs - 1) {
          // Adjust last slice
          end = numFilesToScan;
        }
        workers[i].send({
          cmd: "slice",
          begin,
          end,
          commandLineOptions: args.commandLineOptions,
        });
      }

      cluster.on("message", (worker: Worker, msg: IWorkerResult) => {
        output.log(`Worker ${worker.process.pid} done`);
        codeEditor.recordEdits(msg.codeEdits!);
      });

      cluster.on("exit", (worker, code) => {
        output.error(
          `Worker ${worker.process.pid} exited (exit code: ${code})`
        );
      });

      cluster.on("fork", (worker) => {
        output.log(`Worker ${worker.process.pid} forked`);
      });

      const timerPeriod = 1000;
      const timerCallback = () => {
        const stillAlive = workers.some((worker) => {
          //console.log(worker);
          //console.log(worker.isDead());
          return !worker.isDead();
        });

        if (!stillAlive) {
          clearInterval(interval);
          output.info("Applying migrations");

          codeEditor.applyEdits();
        }
      };

      const interval = setInterval(timerCallback, timerPeriod);
    }
  } else {
    // worker process
    console.log(`Worker ${process.pid} started`);
    process.on("message", (msg: IWorkerMessage) => {
      const output = new StandardConsole(msg.commandLineOptions!.logLevel);

      let codeScanner: CodeScanner = new CodeScanner(
        msg.commandLineOptions!,
        output
      );
      let codeEdits: CodeEdit[] = codeScanner.scan(msg.begin!, msg.end);

      process.send!({ codeEdits: codeEdits });
      console.log(`Worker ${process.pid} exiting`);
      process.exit();
    });
  }
}

// Necessary to allow the fallback typeshed directory to be located
// when running dist\api_migration_tool.js from the command line.
(global as any).__rootDirectory = __dirname;

main();
