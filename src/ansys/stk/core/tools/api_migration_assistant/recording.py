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

"""Recording of API calls."""

import json
import logging
from pathlib import Path
import sys
from typing import Any

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
        try:
            relative_filename = str(Path(filename).relative_to(self.root_directory_path))
        except ValueError:
            logging.warning(f"{filename} is not under {self.root_directory_path}")
        else:
            new_record = CallRecord(
                relative_filename,
                type_name,
                member_name,
                lineno,
                end_lineno,
                col_offset,
                end_col_offset,
            )
            if new_record not in self.call_records:
                self.call_records.append(new_record)

    def sort_call_records(self):
        """Sort the call recorded previously added."""
        self.call_records = sorted(list(set(self.call_records)))

    def save(self, file_name, description=None):
        """Save this recording to the specified file."""
        sorted_call_records = sorted(self.call_records)

        class CallRecordEncoder(json.JSONEncoder):
            def default(self, o: Any):
                if isinstance(o, CallRecord):
                    return {
                        "filename": o.filename,
                        "lineno": o.lineno,
                        "end_lineno": o.end_lineno,
                        "col_offset": o.col_offset,
                        "end_col_offset": o.end_col_offset,
                        "type_name": o.type_name,
                        "member_name": o.member_name,
                        }
                return super(CallRecordEncoder, self).default(o)

        recording = {
            "root_directory": str(self.root_directory_path.resolve()),
            "calls": sorted_call_records,
        }
        if description is not None:
            recording["command"] = description

        with Path(file_name).open(mode="w") as f:
            json.dump(recording, f, cls=CallRecordEncoder, indent=4)

    @staticmethod
    def load_from_recordings_in_directory(recordings_directory):
        """Load a new recording from the files in the specified directory."""
        recording_files = Path(recordings_directory).glob("*.json")

        recording = Recording("")
        root_directory = None

        for recording_file in recording_files:
            logging.debug(f"Processing {recording_file}")

            print(recording_file)

            with Path(recording_file).open(mode="r") as f:
                single_recording = json.load(f)

                current_file_root_directory = single_recording["root_directory"]
                if root_directory is None:
                    root_directory = current_file_root_directory
                elif root_directory != current_file_root_directory:
                    logging.error("Inconsistent recording files based on different root directories!")
                    sys.exit(-3)

                for call in single_recording["calls"]:
                    recording.add(
                        call.get("filename"),
                        call.get("type_name"),
                        call.get("member_name"),
                        int(call.get("lineno")),
                        int(call.get("end_lineno")),
                        int(call.get("col_offset")),
                        int(call.get("end_col_offset")),
                    )

        if root_directory is not None:
            recording.root_directory_path = Path(root_directory).resolve()
        recording.sort_call_records()
        return recording

    def get_files_to_edit(self):
        """Get the files that must be edited based on this recording."""
        files_to_edit = set(
            [str((self.root_directory_path / record.filename).resolve()) for record in self.call_records]
        )
        return files_to_edit

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
