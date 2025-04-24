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

"""Manipulates the code to apply migrations."""

import logging

from libcst import (
    Annotation,
    Arg,
    Attribute,
    Call,
    CSTTransformer,
    Import,
    ImportAlias,
    ImportFrom,
    ImportStar,
    Name,
    SimpleString,
    ensure_type,
    metadata,
)
from libcst.helpers import get_full_name_for_node


class MigrationTransformer(CSTTransformer):
    """Manipulates the libcst CST to perform code migrations."""

    METADATA_DEPENDENCIES = (metadata.PositionProvider,)

    def __init__(self, filename, recording, mappings):
        """Construct a new transformer."""
        self.filename = filename
        self.recording = recording
        self.mappings = mappings
        self.call_stack = []

    def leave_Arg(self, original_node: Arg, updated_node: Arg) -> Arg:  # noqa: N802, D102
        # The keyword of Arg is neither an Assignment nor an Access and we explicitly don't visit it.
        if updated_node.keyword is not None:
            function_call = self.call_stack[-1]
            member_name = function_call.split(".")[-1]
            named_argument_name = updated_node.keyword.value
            logging.debug(f"Leaving argument: {function_call}({named_argument_name})")

            pos = self.get_metadata(metadata.PositionProvider, original_node)

            change = self.recording.get_change_for_file_region(
                self.filename,
                member_name,
                pos.start.line,
                pos.end.line,
                pos.start.column,
                pos.end.column,
            )

            if change is not None:
                if (
                    new_named_argument_name := self.mappings.get_mapping_for_named_argument(
                        change.type_name + "." + member_name,
                        named_argument_name,
                    )
                ) and new_named_argument_name is not None:
                    updated_node = updated_node.with_changes(keyword=Name(new_named_argument_name))

        return updated_node

    def visit_Call(self, node: Call) -> None:  # noqa: N802, D102
        full_name = get_full_name_for_node(node)
        self.call_stack.append(full_name)

    def leave_Call(self, original_node: Call, updated_node: Call) -> Call:  # noqa: N802, D102

        self.call_stack.pop()

        # Intercept constructor calls
        full_name = get_full_name_for_node(updated_node)

        if full_name is None:
            return updated_node

        full_name_parts = full_name.split(".")
        qualifier = ".".join(full_name_parts[:-1])
        name = full_name_parts[-1]

        if self.mappings.has_mapping_for_type(name):
            pos = self.get_metadata(metadata.PositionProvider, original_node)

            change = self.recording.get_change_for_file_region(
                self.filename,
                "__init__",
                pos.start.line,
                pos.end.line,
                pos.start.column,
                pos.end.column,
            )

            if change is not None:
                new_name = self.mappings.get_replacement_for_type(None, name)
                new_qualifier = self.mappings.get_replacement_for_namespace(qualifier)
                updated_node = updated_node.with_deep_changes(
                    updated_node,
                    func=self._assemble_names([x for x in new_qualifier.split(".") if x] + [new_name]),
                )
                return updated_node

        return updated_node

    def leave_Name(self, original_node, updated_node):  # noqa: N802, D102
        name = original_node.value

        if name is not None and self.mappings.is_member_name_of_interest(name):
            pos = self.get_metadata(metadata.PositionProvider, original_node)

            change = self.recording.get_change_for_file_region(
                self.filename,
                name,
                pos.start.line,
                pos.end.line,
                pos.start.column,
                pos.end.column,
            )

            if change is not None:
                new_name = self.mappings.get_replacement_for_member(change.type_name, change.member_name)
                logging.debug(f"Leaving name: {name}: {change is not None} - {pos} -> {new_name}")
                updated_node = updated_node.with_changes(value=new_name)
            else:
                logging.debug(f"Leaving name: {name}: {change is not None} - {pos} -> not found")

        return updated_node

    def leave_Attribute(self, original_node, updated_node):  # noqa: N802, D102

        attr_node = ensure_type(updated_node, Attribute)
        if isinstance(attr_node.value, Name) and isinstance(attr_node.attr, Name):
            lhs_name = attr_node.value.value
            rhs_name = attr_node.attr.value
            (new_enum_type, new_enum_value) = self.mappings.get_replacement_for_enum(lhs_name, rhs_name)
            logging.debug(f"Leaving attribute: {lhs_name}.{rhs_name} -> {new_enum_type}.{new_enum_value}")
            updated_node = updated_node.with_changes(value=Name(new_enum_type), attr=Name(new_enum_value))

        return updated_node

    def _assemble_names(self, names):
        if len(names) == 1:
            return Name(value=names[0])
        else:
            return Attribute(
                value=self._assemble_names(names[:-1]),
                attr=Name(value=names[-1]),
            )

    def leave_Import(self, original_node: Import, updated_node: Import) -> None:  # noqa: N802, D102

        module_name = updated_node.names

        new_names = []
        for n in module_name:
            old_imported_module = get_full_name_for_node(n.name)
            new_imported_module = self.mappings.get_replacement_for_namespace(old_imported_module)
            new_names.append(
                ImportAlias(
                    name=self._assemble_names(new_imported_module.split(".")),
                    asname=n.asname,
                )
            )

        updated_node = updated_node.with_changes(names=new_names)

        return updated_node

    def leave_Annotation(self, original_node: Annotation, updated_node: Annotation) -> None:  # noqa: N802, D102

        if isinstance(updated_node.annotation, SimpleString):
            was_quoted = True
            annotation_full_name = updated_node.annotation.value[1:-1]  # remove quotes
        else:
            was_quoted = False
            annotation_full_name = get_full_name_for_node(updated_node.annotation)

        logging.debug(f"Type hint found: {annotation_full_name}")

        full_name_parts = annotation_full_name.split(".")
        qualifier = ".".join(full_name_parts[:-1])
        name = full_name_parts[-1]
        new_type_name = self.mappings.get_replacement_for_type(qualifier, name)

        new_qualifier = self.mappings.get_replacement_for_namespace(qualifier)

        if was_quoted:
            updated_node = updated_node.with_changes(
                annotation=SimpleString(
                    '"' + ".".join([x for x in new_qualifier.split(".") if x] + [new_type_name]) + '"'
                )
            )
        else:
            updated_node = updated_node.with_changes(
                annotation=self._assemble_names([x for x in new_qualifier.split(".") if x] + [new_type_name])
            )

        return updated_node

    def leave_ImportFrom(self, original_node: ImportFrom, updated_node: ImportFrom) -> None:  # noqa: N802, D102

        module_name = updated_node.module
        old_imported_module = get_full_name_for_node(module_name)

        new_imported_module = self.mappings.get_replacement_for_namespace(old_imported_module)

        old_names = updated_node.names
        new_names = []
        if not isinstance(old_names, ImportStar):
            for old_name in old_names:
                old_imported_name = old_name.name.value
                new_names.append(
                    ImportAlias(
                        name=Name(self.mappings.get_replacement_for_type(old_imported_module, old_imported_name)),
                        asname=old_name.asname,
                    )
                )

        updated_node = updated_node.with_deep_changes(
            updated_node,
            module=self._assemble_names(new_imported_module.split(".")),
        )

        if len(new_names) > 0:
            updated_node = updated_node.with_deep_changes(
                updated_node,
                names=new_names,
            )

        return updated_node
