import commandLineArgs, {
  OptionDefinition,
  CommandLineOptions as RawCommandLineOptions,
} from "command-line-args";
import { cpus, freemem } from "os";
import {
  ConsoleInterface,
  LogLevel,
  convertLogLevel,
} from "pyright-internal/common/console";
import { combinePaths, normalizePath } from "pyright-internal/common/pathUtils";
import {
  PythonVersion,
  versionFromString,
} from "pyright-internal/common/pythonVersion";

const toolName = "api_migration_tool";

export enum CommandLineStatus {
  NoErrors = 0,
  ErrorsReported = 1,
  FatalError = 2,
  ConfigFileParseError = 3,
  ParameterError = 4,
  Continue = 5,
}

export class CommandLineOptions {
  rootDirectory?: string | undefined;
  skipDirectories: string[] = [];
  xmlMappingsDirectory?: string | undefined;
  fileFilter: string | undefined;
  numberOfJobs: number = 0;
  log: string | undefined;
  help: string | undefined;
  pythonPath: string | undefined;
  pythonPlatform: string = "Windows";
  pythonVersion: PythonVersion | undefined;
  strict: boolean = true;
  typeshedPath: string | undefined;
  verboseOutput: boolean | undefined;
  version: string | undefined;
  logLevel: LogLevel = LogLevel.Info;
}

export class Args {
  constructor(
    readonly exitStatus: CommandLineStatus,
    readonly commandLineOptions: CommandLineOptions | undefined = undefined
  ) {}
}

export function processArgs(): Args {
  const optionDefinitions: OptionDefinition[] = [
    { name: "root-dir", type: String },
    { name: "xml-mappings-dir", type: String },
    { name: "skip-dir", type: String, multiple: true },
    { name: "file-filter", type: String },
    { name: "jobs", alias: "j", type: Number },
    { name: "log", type: String },
    { name: "help", alias: "h", type: Boolean },
    { name: "level", type: String },
    { name: "pythonpath", type: String },
    { name: "pythonlatform", type: String },
    { name: "pythonversion", type: String },
    { name: "strict", type: Boolean, defaultValue: true },
    { name: "no-strict", type: Boolean },
    { name: "typeshed-path", type: String },
    { name: "typeshedpath", alias: "t", type: String },
    { name: "verbose", type: Boolean },
    { name: "version", type: Boolean },
  ];

  let args: RawCommandLineOptions;

  try {
    args = commandLineArgs(optionDefinitions);
  } catch (e: any) {
    const argErr: { name: string; optionName: string } = e;
    if (argErr && argErr.optionName) {
      console.error(
        `Unexpected option ${argErr.optionName}.\n${toolName} --help for usage`
      );
      return new Args(CommandLineStatus.ParameterError);
    }

    console.error(`Unexpected error\n${toolName} --help for usage`);
    return new Args(CommandLineStatus.ParameterError);
  }

  if (args.help !== undefined) {
    printUsage();
    return new Args(CommandLineStatus.NoErrors);
  }

  if (args.version !== undefined) {
    printVersion(console);
    return new Args(CommandLineStatus.NoErrors);
  }

  for (const [arg, value] of Object.entries(args)) {
    if (value === null && arg != "jobs") {
      console.error(`'${arg}' option requires a value`);
      return new Args(CommandLineStatus.ParameterError);
    }
  }

  const options = new CommandLineOptions();

  if (args["root-dir"] !== undefined) {
    options.rootDirectory = args["root-dir"];
  } else {
    console.error("--root-dir command line option is required");
    return new Args(CommandLineStatus.ParameterError);
  }

  if (args["xml-mappings-dir"] !== undefined) {
    options.xmlMappingsDirectory = args["xml-mappings-dir"];
  } else {
    console.error("--xml-mappings-dir command line option is required");
    return new Args(CommandLineStatus.ParameterError);
  }

  if (args["skip-dir"] !== undefined) {
    options.skipDirectories = args["skip-dir"];
  }

  if (args["file-filter"] !== undefined) {
    options.fileFilter = args["file-filter"];
  }

  options.strict = args.strict && !args["no-strict"];

  if (args.jobs === null) {
    // -j passed without an explicit value, use num cpus -1 or RAM/4GB
    const fourGb = 4096 * 1024 * 1024; // assume each process requires 4GB
    options.numberOfJobs = Math.floor(
      Math.min(cpus().length - 1, freemem() / fourGb)
    );
  } else if (args.jobs !== undefined) {
    // -j count, use specified count
    options.numberOfJobs = args.jobs;
  }

  if (args.pythonplatform) {
    if (
      args.pythonplatform === "Darwin" ||
      args.pythonplatform === "Linux" ||
      args.pythonplatform === "Windows"
    ) {
      options.pythonPlatform = args.pythonplatform;
    } else {
      console.error(
        `'${args.pythonplatform}' is not a supported Python platform; specify Darwin, Linux, or Windows`
      );
      return new Args(CommandLineStatus.ParameterError);
    }
  }

  if (args.pythonversion) {
    const version = versionFromString(args.pythonversion);
    if (version) {
      options.pythonVersion = version;
    } else {
      console.error(
        `'${args.pythonversion}' is not a supported Python version; specify 3.3, 3.4, etc.`
      );
      return new Args(CommandLineStatus.ParameterError);
    }
  }

  if (args.pythonpath !== undefined) {
    options.pythonPath = combinePaths(
      process.cwd(),
      normalizePath(args["pythonpath"])
    );
  }

  if (args["typeshed-path"]) {
    console.warn(
      `'typeshed-path' option is deprecated; use 'typeshedpath' instead`
    );
    options.typeshedPath = combinePaths(
      process.cwd(),
      normalizePath(args["typeshed-path"])
    );
  }

  if (args["typeshedpath"]) {
    options.typeshedPath = combinePaths(
      process.cwd(),
      normalizePath(args["typeshedpath"])
    );
  }

  if (args.verbose) {
    options.verboseOutput = true;
  }

  if (args.level && typeof args.level === "string") {
    let levelValue = args.level.toLowerCase();
    if (
      levelValue === "error" ||
      levelValue === "warning" ||
      levelValue === "trace" ||
      levelValue === "info"
    ) {
      options.logLevel = convertLogLevel(levelValue);
    } else {
      console.error(
        `'${args.level}' is not a valid value for --level; specify error, warn, info or trace.`
      );
      return new Args(CommandLineStatus.ParameterError);
    }
  }

  if (args.verbose) {
    options.logLevel = LogLevel.Log;
  }

  return new Args(CommandLineStatus.Continue, options);
}

function printUsage() {
  console.info(
    "Usage: " +
      toolName +
      " options...\n" +
      "  Options:\n" +
      "  -h,--help                          Show this help message\n" +
      "  --root-dir <DIRECTORY>             Required: directory containing the files to migrate\n" +
      "  --xml-mappings-dir <DIRECTORY>     Required: directory containing the XML mapping files to apply\n" +
      "  --skip-dir <DIRECTORY>             Directory containing files that should not be migrated\n" +
      "  --file-filter <REGEX>              Only process the file names that match the regular expression\n" +
      "  -j,--jobs [NUMBER]                 Number of parallel processes to spawn\n" +
      "  --level <LEVEL>                    Minimum diagnostic level (error, warn, info or trace)\n" +
      "  --pythonplatform <PLATFORM>        Analyze for a specific platform (Darwin, Linux, Windows)\n" +
      "  --pythonpath <FILE>                Path to the Python interpreter\n" +
      "  --pythonversion <VERSION>          Analyze for a specific version (3.3, 3.4, etc.)\n" +
      "  -t,--typeshedpath <DIRECTORY>      Use typeshed type stubs at this location\n" +
      "  --[no-]strict                      Type checking mode (strict by default)\n" +
      "  --verbose                          Emit verbose diagnostics\n" +
      "  --version                          Print version and exit\n"
  );
}

function getVersionString() {
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const version = require("../package.json").version;
  return version.toString();
}

function printVersion(console: ConsoleInterface) {
  console.info(`${toolName} ${getVersionString()}`);
}
