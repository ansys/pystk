import xml.etree.ElementTree as ET
import pathlib

STATIC_PATH = pathlib.Path(__file__).parent / "doc" / "source" / "_static"
MIGRATION_TABLES = STATIC_PATH / "migration-tables"

def migration_table_to_dict(migration_table):
    """Convert an XML migration table to a dictionary."""

    table = {
        "module": migration_table.name[:-4],
        "interfaces": {},
        "classes": {},
        "enums": {},
    }

    root = ET.parse(migration_table).getroot()

    # Interfaces
    for interface in root.findall('./Mapping[@Category="interface"]'):
        table["interfaces"][interface.get("OldName")] = {
            "new_name": interface.get("NewName"),
            "methods": {},
            "properties": {},
        }

    # Classes
    for klass in root.findall('./Mapping[@Category="class"]'):
        table["classes"][klass.get("OldName")] = {
            "new_name": klass.get("NewName"),
            "methods": {},
            "properties": {},
        }

    # Methods and properties
    for method in root.findall('./Mapping[@Category="method"]'):
        is_interface_method = method.get("ParentScope") in table["interfaces"]
        category = "interfaces" if is_interface_method else "classes"
        parent = method.get("ParentScope")

        table[category][parent]["methods"][method.get("OldName")] = method.get("NewName")

    # Enums
    for enum in root.findall('./Mapping[@Category="enum_type"]'):
        table["enums"][enum.get("OldName")] = {
            "new_name": enum.get("NewName"),
            "values": {},
        }

    # Enum values
    for enum_value in root.findall('./Mapping[@Category="enum_value"]'):
        parent = enum_value.get("ParentScope")
        table["enums"][parent]["values"][enum_value.get("OldName")] = enum_value.get("NewName")

    return table
    

def main():

    for migration_table in MIGRATION_TABLES.glob("*.xml"):
        table = migration_table_to_dict(migration_table)
        print(table["enums"])

if __name__ == "__main__":
    main()
