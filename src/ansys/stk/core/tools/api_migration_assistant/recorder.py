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

"""Records calls to an API."""

import inspect
import logging
from pathlib import Path
import re
import sys

from .recording import Recording


class Recorder:
    """
    Records the calls of interest.

    Uses :func:`sys.setprofile` to intercept calls.
    """

    def __init__(
        self, program, entry_point, root_directory, is_member_name_of_interest_func, run_as_module, program_args=None
    ):
        """Construct a new recorder."""
        self.program = program
        self.entry_point = entry_point
        self.root_directory_path = Path(root_directory).resolve()
        self.root_directory = root_directory
        self.is_member_name_of_interest_func = is_member_name_of_interest_func
        self.recording = Recording(self.root_directory_path)
        self.run_as_module = run_as_module
        self.program_args = program_args

    def record(self):
        """Record the execution of the specified program."""
        program_args_str = " ".join(self.program_args) if self.program_args else ""
        if not self.run_as_module:
            logging.info(f"Recording {self.program} {program_args_str}")
            script_filepath = Path(self.program)
            script_dirpath = str(script_filepath.parent.resolve())
            sys_path_append_cmd = f"sys.path.append('{script_dirpath}')".replace("\\", "\\\\\\\\")
            module_to_import = script_filepath.stem
        else:
            logging.info(f"Recording -m {self.program} {program_args_str}")
            sys_path_append_cmd = ""
            module_to_import = self.program

        # Temporarily modify sys.argv to pass arguments to the recordee
        prev_sys_argv = sys.argv
        new_sys_argv = [module_to_import]
        if self.program_args is not None:
            new_sys_argv += self.program_args
        sys.argv = new_sys_argv

        if sys.version_info >= (3, 11):
            exec_entry_point = "\n".join([
                f"import {module_to_import} as this_module",
                f"this_module.{self.entry_point}()"
            ])
        else:
            exec_entry_point = "\n".join([
                f"import {module_to_import}",
                f"{module_to_import}.{self.entry_point}()"
            ])

        bootstrap = [
            "exec('import sys')",
            f'exec("{sys_path_append_cmd}")',
            f'exec("""{exec_entry_point}""")',
            f"exec('del sys.modules[\"{module_to_import}\"]')",
        ]

        sys.setprofile(self._trace_call)

        [eval(cmd) for cmd in bootstrap] # nosec: B307

        sys.setprofile(None)

        # Restore initial arguments
        sys.argv = prev_sys_argv

        return self.recording

    def _get_client_frame_of_interest(self, frame):
        """Find the client frame calling the API of interest."""
        client_frame = frame.f_back
        client_filename = client_frame.f_code.co_filename
        client_filename_path = Path(client_filename).resolve()
        is_under_root_directory = (
            self.root_directory_path in client_filename_path.parents
        ) and client_filename_path.exists()
        logging.debug(
            f"Checking frame: name={frame.f_code.co_name}, root directory={self.root_directory_path}, client filename={Path(client_filename).resolve()}"
        )
        if is_under_root_directory:
            return client_frame

        lookup_frame = client_frame
        while lookup_frame is not None:
            if lookup_frame.f_code.co_name == "__setattr__":
                break
            lookup_frame = lookup_frame.f_back

        if (
            lookup_frame
            and "self" in frame.f_locals
            and "self" in lookup_frame.f_locals
            and id(frame.f_locals["self"]) == id(lookup_frame.f_locals["self"])
        ):
            client_frame = lookup_frame.f_back
            arg_info = inspect.getargvalues(lookup_frame)
            if len(arg_info.args) > 1 and arg_info.locals[arg_info.args[1]] == frame.f_code.co_name:
                client_filename = client_frame.f_code.co_filename
                client_filename_path = Path(client_filename).resolve()
                is_under_root_directory = (
                    self.root_directory_path in client_filename_path.parents
                ) and client_filename_path.exists()
                if is_under_root_directory:
                    return client_frame

        return None

    def _get_qualified_name(self, frame):
        """Get the qualified name for the function in the specified frame."""
        if hasattr(frame.f_code, "co_qualname"):
            # co_qualname was added in Python 3.11
            return frame.f_code.co_qualname
        else:
            # for previous versions, find the function object
            # in the garbage collector and get the qualified
            # name from it
            import gc
            import inspect

            for o in gc.get_objects():
                if inspect.isfunction(o) and id(o.__code__) == id(frame.f_code):
                    return o.__qualname__
        return None

    def _get_classname(self, frame, member):
        """Get the class name of the specified member in the specified frame."""
        if "self" in frame.f_locals:
            class_type = type(frame.f_locals["self"])
            if class_type is not None:
                types = list(class_type.__mro__)
                for t in types:
                    if member in t.__dict__:
                        return t.__name__
        else:
            qualified_name = self._get_qualified_name(frame)
            match = re.search("(?:.*\\.)?(.*)\\..*", qualified_name)
            if match:
                return match.group(1)
        return None

    def _trace_call(self, frame, event, arg):
        """Call back from :func:`sys.setprofile` to intercept all calls."""
        if event != "call":
            return

        is_call_of_interest = self.is_member_name_of_interest_func(frame.f_code.co_name)

        if not is_call_of_interest:
            return

        client_frame = self._get_client_frame_of_interest(frame)
        if client_frame:

            member = frame.f_code.co_name

            type_name = self._get_classname(frame, member)

            if type_name is not None:

                import inspect

                frameinfo = inspect.getframeinfo(client_frame)

                if sys.version_info >= (3, 11):
                    lineno = frameinfo.positions.lineno
                    end_lineno = frameinfo.positions.end_lineno
                    col_offset = frameinfo.positions.col_offset
                    end_col_offset = frameinfo.positions.end_col_offset
                else:
                    # Traceback in Python < 3.11 does not provide
                    # end line nor column information
                    lineno = frameinfo.lineno
                    end_lineno = lineno
                    col_offset = 0
                    end_col_offset = sys.maxsize

                self.recording.add(
                    client_frame.f_code.co_filename,
                    type_name,
                    member,
                    lineno,
                    end_lineno,
                    col_offset,
                    end_col_offset,
                )
