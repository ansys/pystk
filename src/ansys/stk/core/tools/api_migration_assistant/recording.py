"""Recording of API calls."""

import logging
import sys

import xml.etree.ElementTree as ElementTree

from pathlib import Path

from .call_record import CallRecord


class Recording:
    """Group of calls recorded during one or multiple sessions of the recorder."""

    def __init__(self, root_directory_path):
        self.call_records = list()
        self.root_directory_path = root_directory_path

    def add(
        self,
        filename,
        type_name,
        member_name,
        lineno,
        end_lineno,
        col_offset,
        end_col_offset,
    ):
        """Add a new call record to this recording."""
        relative_filename = str(Path(filename).relative_to(self.root_directory_path))
        self.call_records.append(
            CallRecord(
                relative_filename,
                type_name,
                member_name,
                lineno,
                end_lineno,
                col_offset,
                end_col_offset,
            )
        )

    def sort_call_records(self):
        """Sort the call recorded previously added."""
        self.call_records = sorted(self.call_records)

    def save_to_xml(self, xml_file_name, description=None):
        """Save this recording to an XML file."""
        from xml.sax.saxutils import escape

        sorted_call_records = sorted(self.call_records)
        with Path.open(xml_file_name, mode="wt") as f:
            if description is not None:
                f.write(f"<!-- {escape(description).replace("--", "\\-\\-")} -->\n")
            f.write(f'<recording root_directory="{self.root_directory_path}">\n')
            for record in sorted_call_records:
                call = f'<call filename="{record.filename}"'
                call += f' lineno="{record.lineno}"'
                call += f' end_lineno="{record.end_lineno}"'
                call += f' col_offset="{record.col_offset}"'
                call += f' end_col_offset="{record.end_col_offset}"'
                call += f' type_name="{record.type_name}"'
                call += f' member_name="{record.member_name}"'
                call += "/>\n"
                f.write(call)
            f.write("</recording>\n")

    @staticmethod
    def load_from_xml_recordings_in_directory(recordings_directory):
        """Load a new recording from the XML files in the specified directory."""
        xml_files = Path(recordings_directory).glob("*.xml")

        recording = Recording("")
        root_directory = None

        for xml_file in xml_files:
            tree = ElementTree.parse(xml_file)
            root = tree.getroot()

            logging.debug(f"Processing {xml_file}")

            current_file_root_directory = root.attrib["root_directory"]
            if root_directory is None:
                root_directory = current_file_root_directory
            elif root_directory != current_file_root_directory:
                logging.error("Inconsistent XML files based on different root directories!")
                sys.exit(-3)

            records = root.findall("./call")
            for record in records:
                recording.add(
                    record.get("filename"),
                    record.get("type_name"),
                    record.get("member_name"),
                    int(record.get("lineno")),
                    int(record.get("end_lineno")),
                    int(record.get("col_offset")),
                    int(record.get("end_col_offset")),
                )

        recording.root_directory_path = Path(root_directory).resolve()
        recording.sort_call_records()
        return recording

    def get_files_to_edit(self):
        """Get the files that must be edited based on this recording."""
        files_to_edit = set(
            [str((self.root_directory_path / record.filename).resolve()) for record in self.call_records]
        )
        return files_to_edit

    def get_changes_for_file(self, filename):
        """Get the changes for the specified file based on this recording."""
        relative_filename = str(Path(filename).relative_to(self.root_directory_path))
        changes = set([record for record in self.call_records if record.filename == relative_filename])
        return sorted(changes)

    def get_change_for_file_region(self, filename, member_name, lineno, end_lineno, col_offset, end_col_offset):
        """Find the change corresponding to the specified region."""
        relative_filename = str(Path(filename).relative_to(self.root_directory_path))
        changes = [
            record
            for record in self.call_records
            if record.filename == relative_filename
            and record.member_name == member_name
            and record.lineno <= lineno
            and record.end_lineno >= end_lineno
            and record.col_offset <= col_offset
            and record.end_col_offset >= end_col_offset
        ]

        if len(changes) >= 1:
            return changes[0]
        else:
            return None
