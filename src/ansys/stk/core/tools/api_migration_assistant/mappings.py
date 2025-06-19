# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Specify API mappings from old names to new names."""

import json
import logging
from pathlib import Path


class Mappings:
    """Mappings read from the XML mapping files."""

    def __init__(
        self,
        member_mappings,
        interface_mappings,
        class_mappings,
        enum_type_mappings,
        enum_value_mappings,
        namespace_mappings,
        named_argument_mappings,
    ):
        """Construct a new mapping based on the list of mapping for each category."""
        self.member_mappings = member_mappings
        self.interface_mappings = interface_mappings
        self.class_mappings = class_mappings
        self.enum_type_mappings = enum_type_mappings
        self.enum_value_mappings = enum_value_mappings
        self.namespace_mappings = namespace_mappings
        self.named_argument_mappings = named_argument_mappings

        self.old_member_names_of_interest = set([entry["old_member_name"] for entry in self.member_mappings])

        for argument_mapping in self.named_argument_mappings:
            member_name = argument_mapping["old_type_name"].split(".")[-1]
            self.old_member_names_of_interest.add(member_name)

        all_types = self.interface_mappings + self.class_mappings + self.enum_type_mappings

        self.old_type_names = set([entry["old_type_name"] for entry in all_types])

    @staticmethod
    def load_from(mappings_directory):
        """Load mappings from the specified directory."""
        json_files = Path(mappings_directory).glob("*.json")

        member_mappings = []
        interface_mappings = []
        class_mappings = []
        enum_type_mappings = []
        enum_value_mappings = []
        namespace_mappings = {}
        named_argument_mappings = []

        for json_file in json_files:
            with Path(json_file).open(mode="r") as f:
                mappings = json.load(f)

            logging.debug(f"Processing {json_file}")

            if "RootMapping" in mappings and "OldRootScope" in mappings["RootMapping"] and "NewRootScope" in mappings["RootMapping"]:
                old_root = mappings["RootMapping"]["OldRootScope"]
                new_root = mappings["RootMapping"]["NewRootScope"]
                namespace_mappings[old_root] = new_root
            else:
                old_root = ""
                new_root = ""

            method_entries = mappings.get("MemberMappings", [])

            for method_entry in method_entries:
                old_type_name = method_entry.get("ParentScope")
                old_member_name = method_entry.get("OldName")
                new_member_name = method_entry.get("NewName")

                member_mappings.append(
                    {
                        "old_root": old_root,
                        "old_type_name": old_type_name,
                        "old_member_name": old_member_name,
                        "new_member_name": new_member_name,
                    }
                )

            named_argument_entries = mappings.get("NamedArgumentMappings", [])

            for named_argument_entry in named_argument_entries:
                old_argument_name = named_argument_entry.get("OldName")
                new_argument_name = named_argument_entry.get("NewName")
                old_type_name = named_argument_entry.get("ParentScope")

                named_argument_mappings.append(
                    {
                        "old_root": old_root,
                        "old_type_name": old_type_name,
                        "old_argument_name": old_argument_name,
                        "new_argument_name": new_argument_name,
                    }
                )

            enum_type_entries = mappings.get("EnumTypeMappings", [])

            for enum_type_entry in enum_type_entries:
                old_enum_type_name = enum_type_entry.get("OldName")
                new_enum_type_name = enum_type_entry.get("NewName")

                enum_type_mappings.append(
                    {
                        "old_root": old_root,
                        "old_type_name": old_enum_type_name,
                        "new_type_name": new_enum_type_name,
                    }
                )

            enum_value_entries = mappings.get("EnumValueMappings", [])

            for enum_value_entry in enum_value_entries:
                old_enum_type_name = enum_value_entry.get("ParentScope")
                old_enum_value_name = enum_value_entry.get("OldName")
                new_enum_value_name = enum_value_entry.get("NewName")

                enum_value_mappings.append(
                    {
                        "old_root": old_root,
                        "old_type_name": old_enum_type_name,
                        "old_enum_value_name": old_enum_value_name,
                        "new_enum_value_name": new_enum_value_name,
                    }
                )

            interface_entries = mappings.get("InterfaceMappings", [])

            for interface_entry in interface_entries:
                old_interface_name = interface_entry.get("OldName")
                new_interface_type_name = interface_entry.get("NewName")

                interface_mappings.append(
                    {
                        "old_root": old_root,
                        "old_type_name": old_interface_name,
                        "new_type_name": new_interface_type_name,
                    }
                )

            class_entries = mappings.get("ClassMappings", [])

            for class_entry in class_entries:
                old_class_name = class_entry.get("OldName")
                new_class_name = class_entry.get("NewName")

                class_mappings.append(
                    {
                        "old_root": old_root,
                        "old_type_name": old_class_name,
                        "new_type_name": new_class_name,
                    }
                )

        return Mappings(
            member_mappings,
            interface_mappings,
            class_mappings,
            enum_type_mappings,
            enum_value_mappings,
            namespace_mappings,
            named_argument_mappings,
        )

    def is_member_name_of_interest(self, member_name):
        """Indicate if the specified member name could be of interest or not."""
        return member_name in self.old_member_names_of_interest or member_name == "__init__"

    def has_mapping_for_type(self, type_name):
        """Is there a mapping for the specified type?"""
        return type_name in self.old_type_names

    def get_mapping_for_named_argument(self, qualified_member_name, named_argument):
        """Get the mapping for the specified named argument."""
        matches = [
            entry
            for entry in self.named_argument_mappings
            if entry["old_type_name"] == qualified_member_name and entry["old_argument_name"] == named_argument
        ]
        if len(matches) == 1:
            return matches[0]["new_argument_name"]

        return None

    def get_replacement_for_member(self, type_name, member_name):
        """
        Get the new name for the specified type and member.

        If there is no mapping for this type and member, return the same name.
        """
        matches = [
            entry
            for entry in self.member_mappings
            if entry["old_type_name"] == type_name and entry["old_member_name"] == member_name
        ]
        if len(matches) == 1:
            return matches[0]["new_member_name"]
        elif len(matches) > 1:
            raise RuntimeError(f"Multiple mappings found for {type_name}.{member_name}")
        else:
            return member_name  # not renamed

    def get_replacement_for_enum(self, old_enum_type_name, old_enum_value_name):
        """
        Get the new name for the specified enumeration type and value.

        If there is no mapping for the specified enumeration type and value, return the same names.
        """
        enum_type_matches = [entry for entry in self.enum_type_mappings if entry["old_type_name"] == old_enum_type_name]
        new_enum_type_name = (
            enum_type_matches[0]["new_type_name"]
            if len(enum_type_matches) > 0  # pick the first one
            else old_enum_type_name
        )
        enum_value_matches = [
            entry
            for entry in self.enum_value_mappings
            if entry["old_type_name"] == old_enum_type_name and entry["old_enum_value_name"] == old_enum_value_name
        ]
        new_enum_value_name = (
            enum_value_matches[0]["new_enum_value_name"]
            if len(enum_value_matches) > 0  # pick the first one
            else old_enum_value_name
        )
        return (new_enum_type_name, new_enum_value_name)

    def get_replacement_for_type(self, root, type_name):
        """
        Get the new name for the specified type.

        If there is no mapping for the specified type, return the same name.
        """
        all_types = self.interface_mappings + self.class_mappings + self.enum_type_mappings
        matches = [
            entry
            for entry in all_types
            if entry["old_type_name"] == type_name and (root is None or len(root) == 0 or entry["old_root"] == root)
        ]
        if len(matches) == 1:
            return matches[0]["new_type_name"]
        elif len(matches) > 1:
            raise RuntimeError(f"Multiple mappings found for {root}.{type_name}")
        else:
            return type_name  # not renamed

    def get_replacement_for_namespace(self, namespace):
        """Get the new name for the specified namespace."""
        return self.namespace_mappings.get(namespace, namespace)
