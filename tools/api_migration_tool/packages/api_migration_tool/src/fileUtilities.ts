import Path from "path";
import { ConsoleInterface } from "pyright-internal/common/console";
import { ServiceProvider } from "pyright-internal/common/extensibility";
import { FileSystem } from "pyright-internal/common/fileSystem";
import { Uri } from "pyright-internal/common/uri/uri";
import xml2js from "xml2js";

export function findFiles(
  fs: FileSystem,
  directory: Uri,
  extension: string,
  output: ConsoleInterface,
  serviceProvider: ServiceProvider
): Uri[] {
  output.log(
    `Scanning ${getPathRelativeToRoot(
      directory
    )} for files with "${extension}" extension`
  );
  let result: Uri[] = [];
  fs.readdirSync(directory).forEach((entry) => {
    const absolutePath = directory.combinePaths(entry);
    output.log(getPathRelativeToRoot(absolutePath));
    if (fs.statSync(absolutePath).isDirectory()) {
      result.push(
        ...findFiles(fs, absolutePath, extension, output, serviceProvider)
      );
    } else if (absolutePath.hasExtension(extension)) {
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
  xmlMappingsDir: Uri,
  fs: FileSystem,
  rootDirectory: Uri,
  output: ConsoleInterface,
  serviceProvider: ServiceProvider,
  callback: (pythonFilePath: string, mappings: any) => void
) {
  const xmlMappingFileList: Uri[] = findFiles(
    fs,
    xmlMappingsDir,
    ".xml",
    output,
    serviceProvider
  );

  for (const xmlMappingFile of xmlMappingFileList) {
    output.info(`Processing ${xmlMappingFile.fileName}`);
    const xml = fs.readFileSync(xmlMappingFile);
    xml2js.parseString(xml.toString(), (err, result) => {
      const xmlMappings = result["Mappings"]["Mapping"];

      if (xmlMappings) {
        const pythonFilePath =
          Path.join(
            rootDirectory.getFilePath(),
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

let rootDirectory: Uri;

export function setRootDirectory(path: Uri) {
  rootDirectory = path;
}

export function getPathRelativeToRoot(path: Uri): string {
  let result: string | undefined = rootDirectory.getRelativePath(path);
  if (result === undefined) {
    if (rootDirectory === path) {
      result = ".";
    } else {
      result = path.getFilePath();
    }
  }
  return result;
}
