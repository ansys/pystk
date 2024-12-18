import pathlib
import xml.etree.ElementTree as ET

from pathlib import Path

STATIC_PATH = pathlib.Path(__file__).parent / "doc" / "source" / "_static"
MIGRATION_TABLES = STATIC_PATH / "migration-tables"

xml_files = MIGRATION_TABLES.glob("*.xml")



for xml_file in xml_files:
    tree = ET.parse(xml_file)
    root = tree.getroot()

    print(f"Processing {xml_file}")

    rst_file = Path(xml_file).with_suffix('.rst')

    # Read XML input data into dictionary
    # Dictionary structure: 
    # { <old_type_name>: 
    #       { 
    #           'new_name': <new_type_name>, 
    #           'members': 
    #           {
    #               <old__name>: <new__name>
    #           }
    #       }
    # }
    mappings = {}
    type_categories = ["enum_type", "class", "interface"]
    for type_category in  type_categories:
        type_mappings = root.findall(f'./Mapping[@Category="{type_category}"]')
        for type_mapping in type_mappings:
            type_old_name = type_mapping.get("OldName")
            type_new_name = type_mapping.get("NewName")
            mappings[type_old_name] = { 'new_name': type_new_name, 'members': {}}
            member_mappings = root.findall(f'./Mapping[@ParentScope="{type_old_name}"]')
            for member_mapping in member_mappings:
                member_old_name = member_mapping.get("OldName")
                member_new_name = member_mapping.get("NewName")
                mappings[type_old_name]['members'][member_old_name] = member_new_name

    # Compute maximum column sizes
    max_length_column1 = 0
    max_length_column2 = 0
    member_indent = 3 # " - "
    type_bold = 4 # **...**
    for mapping in sorted(mappings.keys()):
        max_length_column1 = max(len(mapping) + type_bold, max_length_column1)
        max_length_column2 = max(len(mappings[mapping]['new_name']) + type_bold, max_length_column2)
        members = mappings[mapping]['members']
        for member in sorted(members.keys()):
            max_length_column1 = max(len(member) + member_indent, max_length_column1)
            max_length_column2 = max(len(members[member]) + member_indent, max_length_column2)

    # Generate output
    output_lines = []
    line_separator = "=" * max_length_column1 + " " + "=" * max_length_column2
    output_lines.append(line_separator)
    output_lines.append("Old Name".ljust(max_length_column1) + " " + "New Name".ljust(max_length_column2))
    output_lines.append(line_separator)
    for mapping in sorted(mappings.keys()):
        output_lines.append(f"{('**' + mapping + '**').ljust(max_length_column1)} {'**' + mappings[mapping]['new_name'] + '**'}")
        members = mappings[mapping]['members']
        for member in sorted(members.keys()):
            output_lines.append(f" - {member.ljust(max_length_column1)} - {members[member]}")
    output_lines.append(line_separator)

    with open(rst_file, "w") as f:
        f.writelines('\n'.join(output_lines))
