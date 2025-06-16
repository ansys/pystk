import Path from "path";
import { ConsoleInterface } from "pyright-internal/common/console";
import { FileSystem } from "pyright-internal/common/fileSystem";
import { ServiceProvider } from "pyright-internal/common/serviceProvider";
import { Uri } from "pyright-internal/common/uri/uri";

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
  jsonMappingsDir: Uri,
  fs: FileSystem,
  rootDirectory: Uri,
  output: ConsoleInterface,
  serviceProvider: ServiceProvider,
  callback: (pythonFilePath: string, mappings: any) => void
) {
  const jsonMappingFileList: Uri[] = findFiles(
    fs,
    jsonMappingsDir,
    ".json",
    output,
    serviceProvider
  );

  for (const jsonMappingFile of jsonMappingFileList) {
    output.info(`Processing ${jsonMappingFile.fileName}`);
    let json = JSON.parse(fs.readFileSync(jsonMappingFile).toString());
    json = categorizeMappings(json);
    const jsonMappings = json.MemberMappings.concat(json.InterfaceMappings, json.ClassMappings, json.EnumTypeMappings, json.EnumValueMappings);
    if (jsonMappings) {
      const pythonFilePath =
        Path.join(
          rootDirectory.getFilePath(),
          Path.basename(jsonMappingFile.getFilePath(), ".json")
            .split(".")
            .join(Path.sep)
        ) + ".py";

      let mappings: Mapping[] = [];
      for (const jsonMapping of jsonMappings) {
        const newName = jsonMapping.NewName;
        const oldName = jsonMapping.OldName;
        const parentScope = jsonMapping.ParentScope;
        const category = jsonMapping.Category;

        mappings.push(new Mapping(newName, oldName, parentScope, category));
      }

      if (mappings) {
        callback(pythonFilePath, mappings);
      }
    }
  }
}

function categorizeMappings(json: any) {
  for (let i = 0; i < json.MemberMappings.length; i++) {
      json.MemberMappings[i].Category = "method";
  }
  for (let i = 0; i < json.InterfaceMappings.length; i++) {
      json.InterfaceMappings[i].Category = "interface";
  }
  for (let i = 0; i < json.ClassMappings.length; i++) {
      json.ClassMappings[i].Category = "class";
  }
  for (let i = 0; i < json.EnumTypeMappings.length; i++) {
      json.EnumTypeMappings[i].Category = "enum_type";
  }
  for (let i = 0; i < json.EnumValueMappings.length; i++) {
      json.EnumValueMappings[i].Category = "enum_value";
  }
  return json;
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
