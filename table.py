import pathlib
import xml.etree.ElementTree as ET

tree = ET.parse(pathlib.Path(__file__).parent / "doc" / "source" / "_static" / "migration-tables" / "agi.stk12.graphics.xml")
root = tree.getroot()

print("Enumeration Types")
print("^^^^^^^^^^^^^^^^^")
print()

enum_types = root.findall('./Mapping[@Category="enum_type"]')
print(enum_types)
old_name_max_length = max([len(mapping.get("OldName")) for mapping in enum_types])
new_name_max_length = max([len(mapping.get("NewName")) for mapping in enum_types])

header = "=" * old_name_max_length + " " + "=" * new_name_max_length

print(header)
print("Old Name".ljust(old_name_max_length) + " " + "New Name".ljust(new_name_max_length))
print(header)
for mapping in enum_types:
    print(mapping.get("OldName").ljust(old_name_max_length) + " " + mapping.get("NewName").ljust(new_name_max_length))
print(header)
print()

print("Enumeration Values")
print("^^^^^^^^^^^^^^^^^^")
print()

enum_values = root.findall('./Mapping[@Category="enum_value"]')
old_name_max_length = max([len(mapping.get("OldName")) for mapping in enum_values])
new_name_max_length = max([len(mapping.get("NewName")) for mapping in enum_values])
parent_scope_max_length = max([len(mapping.get("ParentScope")) for mapping in enum_values])

header = "=" * parent_scope_max_length + " " + "=" * old_name_max_length + " " + "=" * new_name_max_length

print(header)
print("Enumeration Type".ljust(parent_scope_max_length) + " " + "Old Name".ljust(old_name_max_length) + " " + "New Name".ljust(new_name_max_length))
print(header)
for mapping in enum_values:
    print(mapping.get("ParentScope").ljust(parent_scope_max_length) + " " + mapping.get("OldName").ljust(old_name_max_length) + " " + mapping.get("NewName").ljust(new_name_max_length))
print(header)
print()

print("Classes")
print("^^^^^^^")
print()

classes = root.findall('./Mapping[@Category="class"]')
old_name_max_length = max([len(mapping.get("OldName")) for mapping in classes])
new_name_max_length = max([len(mapping.get("NewName")) for mapping in classes])

header = "=" * old_name_max_length + " " + "=" * new_name_max_length

print(header)
print("Old Name".ljust(old_name_max_length) + " " + "New Name".ljust(new_name_max_length))
print(header)
for mapping in classes:
    print(mapping.get("OldName").ljust(old_name_max_length) + " " + mapping.get("NewName").ljust(new_name_max_length))
print(header)
print()

print("Interfaces")
print("^^^^^^^^^^")
print()

interfaces = root.findall('./Mapping[@Category="interface"]')
old_name_max_length = max([len(mapping.get("OldName")) for mapping in interfaces])
new_name_max_length = max([len(mapping.get("NewName")) for mapping in interfaces])

header = "=" * old_name_max_length + " " + "=" * new_name_max_length

print(header)
print("Old Name".ljust(old_name_max_length) + " " + "New Name".ljust(new_name_max_length))
print(header)
for mapping in interfaces:
    print(mapping.get("OldName").ljust(old_name_max_length) + " " + mapping.get("NewName").ljust(new_name_max_length))
print(header)
print()

print("Properties & Methods")
print("^^^^^^^^^^^^^^^^^^^^")
print()

methods = root.findall('./Mapping[@Category="method"]')
old_name_max_length = max([len(mapping.get("OldName")) for mapping in methods])
new_name_max_length = max([len(mapping.get("NewName")) for mapping in methods])
parent_scope_max_length = max([len(mapping.get("ParentScope")) for mapping in methods])

header = "=" * parent_scope_max_length + " " + "=" * old_name_max_length + " " + "=" * new_name_max_length

print(header)
print("Enumeration Type".ljust(parent_scope_max_length) + " " + "Old Name".ljust(old_name_max_length) + " " + "New Name".ljust(new_name_max_length))
print(header)
for mapping in methods:
    print(mapping.get("ParentScope").ljust(parent_scope_max_length) + " " + mapping.get("OldName").ljust(old_name_max_length) + " " + mapping.get("NewName").ljust(new_name_max_length))
print(header)
print()
