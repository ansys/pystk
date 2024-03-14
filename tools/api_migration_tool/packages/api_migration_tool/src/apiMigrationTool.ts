import cluster, { Worker } from "cluster";

import { StandardConsole } from "pyright-internal/common/console";
import { CodeEdit, CodeEditor } from "./codeEditor";
import { CodeScanner } from "./codeScanner";
import { CommandLineOptions, CommandLineStatus, processArgs } from "./options";

interface IWorkerMessage {
  cmd: string;
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
      codeScanner.prepareScan();
      let codeEdits: CodeEdit[] = codeScanner.scan();

      output.info("Creating code edits...");

      const codeEditor = new CodeEditor(output);
      codeEditor.recordEdits(codeEdits);

      output.info(`Applying ${codeEditor.getNumberOfEdits()} migrations`);

      codeEditor.applyEdits();
    } else {
      // Run in parallel

      let codeScanner: CodeScanner = new CodeScanner(
        args.commandLineOptions,
        output
      );

      const codeEditor = new CodeEditor(output);

      let numChunksPerWorker = 128;
      if (args.commandLineOptions.numberOfChunksPerWorker > 0) {
        numChunksPerWorker = args.commandLineOptions.numberOfChunksPerWorker;
      }
      output.info(`Using ${numChunksPerWorker} chunks per worker`);
      const numFilesToScan = codeScanner.getFilesToScan().length;
      const chunkSize = Math.max(
        Math.floor(numFilesToScan / numJobs / numChunksPerWorker),
        1
      );

      let index = 0;

      function endReached(): boolean {
        return index >= numFilesToScan;
      }

      function getNextChunk(): [number, number] {
        const begin = index;
        let end = Math.min(index + chunkSize, numFilesToScan);
        const result: [number, number] = [begin, end];
        index = end;
        return result;
      }

      let workers: Worker[] = [];
      for (let i = 0; i < numJobs; i++) {
        let [begin, end] = getNextChunk();

        const newWorker = cluster.fork();
        workers.push(newWorker);

        newWorker.send({
          cmd: "init",
          commandLineOptions: args.commandLineOptions,
        });

        newWorker.send({
          cmd: "scan",
          begin,
          end,
        });

        if (endReached()) {
          break;
        }
      }

      cluster.on("message", (worker: Worker, msg: IWorkerResult) => {
        output.log(`Worker ${worker.process.pid} chunk done`);
        codeEditor.recordEdits(msg.codeEdits!);

        if (!endReached()) {
          let [begin, end] = getNextChunk();
          worker.send({
            cmd: "scan",
            begin,
            end,
          });
        } else {
          worker.send({
            cmd: "terminate",
          });
        }
      });

      cluster.on("exit", (worker, code) => {
        if (code != 0) {
          output.error(
            `Worker ${worker.process.pid} exited (exit code: ${code})`
          );
        } else {
          output.log(
            `Worker ${worker.process.pid} exited (exit code: ${code})`
          );
        }
      });

      cluster.on("fork", (worker) => {
        output.log(`Worker ${worker.process.pid} forked`);
      });

      const timerPeriod = 1000;
      const timerCallback = () => {
        const stillAlive = workers.some((worker) => {
          return !worker.isDead();
        });

        if (!stillAlive) {
          clearInterval(interval);
          output.info(`Applying ${codeEditor.getNumberOfEdits()} migrations`);

          codeEditor.applyEdits();
        }
      };

      const interval = setInterval(timerCallback, timerPeriod);
    }
  } else {
    // worker process
    let output: StandardConsole | undefined;
    let codeScanner: CodeScanner | undefined;
    process.on("message", (msg: IWorkerMessage) => {
      if (msg.cmd === "init") {
        output = new StandardConsole(msg.commandLineOptions!.logLevel);
        output.log(`Worker ${process.pid} started`);
        codeScanner = new CodeScanner(msg.commandLineOptions!, output!, true);
        codeScanner!.prepareScan();
      } else if (msg.cmd === "scan") {
        let codeEdits: CodeEdit[] = codeScanner!.scan(msg.begin!, msg.end);
        process.send!({ codeEdits: codeEdits });
      } else if (msg.cmd === "terminate") {
        output!.log(`Worker ${process.pid} exiting`);
        process.exit();
      }
    });
  }
}

// Necessary to allow the fallback typeshed directory to be located
// when running dist\api_migration_tool.js from the command line.
(global as any).__rootDirectory = __dirname;

main();
