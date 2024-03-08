import Path from "path";
import { ConsoleInterface } from "pyright-internal/common/console";
import { FileSystem } from "pyright-internal/common/fileSystem";
import { Uri } from "pyright-internal/common/uri/uri";
import xml2js from "xml2js";

export function findFiles(
  fs: FileSystem,
  directory: string,
  extension: string,
  output: ConsoleInterface
): Uri[] {
  output.log(
    `Scanning ${getPathRelativeToRoot(
      directory
    )} for files with "${extension}" extension`
  );
  let result: Uri[] = [];
  fs.readdirSync(Uri.file(directory)).forEach((entry) => {
    const absolutePath = Path.join(directory, entry);
    output.log(getPathRelativeToRoot(absolutePath));
    if (fs.statSync(Uri.file(absolutePath)).isDirectory()) {
      result.push(...findFiles(fs, absolutePath, extension, output));
    } else if (Path.extname(absolutePath) == extension) {
      result.push(Uri.file(absolutePath));
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
  const xmlMappingFileList: Uri[] = findFiles(
    fs,
    xmlMappingsDir,
    ".xml",
    output
  );

  for (const xmlMappingFile of xmlMappingFileList) {
    output.info(`Processing ${xmlMappingFile.fileName}`);
    const xml = fs.readFileSync(xmlMappingFile);
    xml2js.parseString(xml.toString(), (err, result) => {
      const xmlMappings = result["Mappings"]["Mapping"];

      if (xmlMappings) {
        const pythonFilePath =
          Path.join(
            rootDirectory,
            Path.basename(xmlMappingFile.getFilePath(), ".xml")
              .split(".")
              .join(Path.sep)
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
  let result = Uri.file(rootDirectory).getRelativePath(Uri.file(path));
  if (result === undefined) {
    if (Uri.file(rootDirectory) === Uri.file(path)) {
      result = ".";
    } else {
      result = path;
    }
  }
  return result;
}
