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
