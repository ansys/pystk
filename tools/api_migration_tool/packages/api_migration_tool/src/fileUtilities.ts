import Path from "path";
import { ConsoleInterface } from "pyright-internal/common/console";
import { FileSystem } from "pyright-internal/common/fileSystem";
import xml2js from "xml2js";

export function findFiles(
  fs: FileSystem,
  directory: string,
  extension: string,
  output: ConsoleInterface
): string[] {
  output.log(
    `Scanning ${getPathRelativeToRoot(
      directory
    )} for files with "${extension}" extension`
  );
  let result: string[] = [];
  fs.readdirSync(directory).forEach((entry) => {
    const absolutePath = Path.join(directory, entry);
    output.log(getPathRelativeToRoot(absolutePath));
    if (fs.statSync(absolutePath).isDirectory()) {
      result.push(...findFiles(fs, absolutePath, extension, output));
    } else if (Path.extname(absolutePath) == extension) {
      result.push(absolutePath);
    }
  });
  return result;
}

class Mapping {
  constructor(
    readonly newName: string,
    readonly oldName: string,
    readonly parentScope: string,
    readonly category: string
  ) {}
}

export function readMappingFileDirectory(
  xmlMappingsDir: string,
  fs: FileSystem,
  rootDirectory: string,
  output: ConsoleInterface,
  callback: (pythonFilePath: string, mappings: any) => void
) {
  const xmlMappingFileList: string[] = findFiles(
    fs,
    xmlMappingsDir,
    ".xml",
    output
  );

  for (const xmlMappingFile of xmlMappingFileList) {
    output.info(`Processing ${xmlMappingFile}`);
    const xml = fs.readFileSync(xmlMappingFile);
    xml2js.parseString(xml.toString(), (err, result) => {
      const xmlMappings = result["Mappings"]["Mapping"];

      if (xmlMappings) {
        const pythonFilePath =
          Path.join(
            rootDirectory,
            Path.basename(xmlMappingFile, ".xml").split(".").join(Path.sep)
          ) + ".py";

        let mappings: Mapping[] = [];
        for (const xmlMapping of xmlMappings) {
          const newName = xmlMapping["$"]["NewName"];
          const oldName = xmlMapping["$"]["OldName"];
          const parentScope = xmlMapping["$"]["ParentScope"];
          const category = xmlMapping["$"]["Category"];

          mappings.push(new Mapping(newName, oldName, parentScope, category));
        }

        if (mappings) {
          callback(pythonFilePath, mappings);
        }
      }
    });
  }
}

let rootDirectory: string;

export function setRootDirectory(path: string) {
  rootDirectory = path;
}

export function getPathRelativeToRoot(path: string): string {
  let result = Path.relative(rootDirectory, path);
  if (result === undefined) {
    if (Path.normalize(rootDirectory) === Path.normalize(path)) {
      result = ".";
    } else {
      result = path;
    }
  }
  return result;
}

export function pathIsChild(childPath: string, parentPath: string): boolean {
  const relative = Path.relative(parentPath, childPath);
  return (
    relative !== undefined &&
    !relative.startsWith("..") &&
    !Path.isAbsolute(relative)
  );
}
