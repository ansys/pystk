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

"""Make code edits."""

import logging
from pathlib import Path

from libcst import MetadataWrapper, parse_module

from .migration_transformer import MigrationTransformer


class CodeEditor:
    """Edit the code to apply the API migrations identified through both static and dynamic analysis."""

    def __init__(self, recording, mappings):
        """Construct a new editor configured to apply the specified recording and mappings"""
        self.recording = recording
        self.mappings = mappings

    def apply_changes(self):
        """Apply the code migrations."""
        files_to_edit = self.recording.get_files_to_edit()
        for file_to_edit in files_to_edit:
            source_code = Path(file_to_edit).read_text(encoding="utf-8")
            tree = MetadataWrapper(parse_module(source_code))

            transformer = MigrationTransformer(file_to_edit, self.recording, self.mappings)

            modified_tree = tree.visit(transformer)

            migrated_filename = file_to_edit + "-migrated"
            logging.info(f"Writing {migrated_filename}")
            Path(migrated_filename).write_text(modified_tree.code, encoding="utf-8")
