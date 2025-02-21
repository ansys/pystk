# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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

import os
import pytest
import shutil
import subprocess
import sys
import tempfile
import textwrap

from pathlib import Path

from ansys.stk.core.tools.api_migration_assistant import api_migration_assistant


class Runner:
    def __init__(self, api, api_mappings, input, api_root=None, in_process=True, extra_args=None, run_pytest=False):
        self.temp_directory = Path(tempfile.TemporaryDirectory().name)
        self.api = api
        self.api_mappings = api_mappings
        self.input = input
        if api_root is not None:
            self.api_root = Path("api") / Path(*api_root)
        else:
            self.api_root = Path("api")
        self.in_process = in_process
        self.input_files = []
        self.result_files = []
        self.entry_points = []
        self.keep_test_files = False
        self.extra_args = extra_args
        self.run_pytest = run_pytest

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.keep_test_files:
            shutil.rmtree(self.temp_directory, True)

    def _setup_api(self):
        api_file = self.temp_directory / self.api_root / "api.py"
        api_file.parent.mkdir(parents=True, exist_ok=True)
        api_file.write_text(textwrap.dedent(self.api), encoding="utf-8")

    def _setup_api_mappings(self):
        api_mapping_dir = self.temp_directory / "api_mappings"
        api_mapping_dir.mkdir(parents=True, exist_ok=True)
        if isinstance(self.api_mappings, list):
            for index, api_mappings_entry in enumerate(self.api_mappings):
                api_mappings_file = api_mapping_dir / f"api_mappings{index}.xml"
                api_mappings_file.write_text(api_mappings_entry, encoding="utf-8")
        else:
            api_mappings_file = api_mapping_dir / "api_mappings.xml"
            api_mappings_file.write_text(self.api_mappings, encoding="utf-8")

    def _setup_input(self):
        test_directory = self.temp_directory / "test"
        test_directory.mkdir(parents=True, exist_ok=True)
        if isinstance(self.input, list):
            for input_entry in self.input:
                input_file = test_directory / input_entry["filename"]
                input_file.write_text(textwrap.dedent(input_entry["code"]), encoding="utf-8")
                self.input_files.append(str(input_file.resolve()))
                self.entry_points.append(input_entry.get("entry_point", None))
        else:
            input_file = test_directory / "input.py"
            input_file.write_text(textwrap.dedent(self.input), encoding="utf-8")
            self.input_files.append(str(input_file.resolve()))
            self.entry_points.append("main")

    def _invoke_migration_assistant_record(
        self,
        pythonpath,
        mappings_directory,
        root_directory,
        recordings_directory,
    ):
        if self.in_process:

            if self.run_pytest:
                raise RuntimeError("Running through pytest is only supported out of process")

            before_modules = list(sys.modules.keys())
            with pytest.MonkeyPatch.context() as m:
                m.syspath_prepend(pythonpath)

                for index, input_file in enumerate(self.input_files):
                    print(f"input: {input_file} -> self.entry_points[index]={self.entry_points[index]}")
                    if self.entry_points[index] is not None:
                        api_migration_assistant.record(
                            mappings_directory,
                            root_directory,
                            recordings_directory,
                            input_file,
                            self.entry_points[index],
                            False,
                            self.extra_args,
                        )

            after_modules = list(sys.modules.keys())
            for m in after_modules:
                if m not in before_modules:
                    del sys.modules[m]

        else:
            api_migration_assistant_module = api_migration_assistant.__name__
            env = os.environ.copy()
            env["PYTHONPATH"] = pythonpath
            for index, input_file in enumerate(self.input_files):
                print(f"input: {input_file} -> self.entry_points[index]={self.entry_points[index]}")
                if self.entry_points[index] is not None:
                    record_command = [
                        sys.executable,
                        "-m",
                        api_migration_assistant_module,
                        "record",
                        "--mappings-directory",
                        mappings_directory,
                        "--root-directory",
                        root_directory,
                        "--recordings-directory",
                        recordings_directory,
                    ]
                    if self.run_pytest:
                        pytest_rootdir = str(Path(input_file).parent.resolve())
                        record_command += [
                            "-m",
                            "pytest",
                            input_file,
                            f"--rootdir={pytest_rootdir}",
                            "--capture=no",
                        ]
                    else:
                        record_command += [
                            "--entry-point",
                            self.entry_points[index],
                            input_file,
                        ]
                    if self.extra_args is not None:
                        record_command += self.extra_args
                    print(" ".join(record_command))
                    record_output = subprocess.call(
                        record_command,
                        env=env,
                    )
                    if record_output != 0:
                        raise RuntimeError("api-migration-assistant record failed")

    def _invoke_migration_assistant_apply(self, mappings_directory, recordings_directory):

        if self.in_process:
            api_migration_assistant.apply(mappings_directory, recordings_directory)
        else:
            api_migration_assistant_module = api_migration_assistant.__name__

            env = os.environ.copy()

            apply_command = [
                sys.executable,
                "-m",
                api_migration_assistant_module,
                "apply",
                "--mappings-directory",
                str((self.temp_directory / "api_mappings").absolute().resolve()),
                "--recordings-directory",
                str((self.temp_directory / "recordings").absolute().resolve()),
            ]

            print(" ".join(apply_command))

            apply_output = subprocess.call(
                apply_command,
                env=env,
            )
            if apply_output != 0:
                raise RuntimeError("api-migration-assistant apply failed")

    def _run_migration_assistant(self):

        mappings_directory = str((self.temp_directory / "api_mappings").absolute().resolve())
        recordings_directory = str((self.temp_directory / "recordings").absolute().resolve())

        self._invoke_migration_assistant_record(
            pythonpath=str((self.temp_directory / "api").absolute().resolve()),
            mappings_directory=mappings_directory,
            root_directory=str((self.temp_directory / "test").absolute().resolve()),
            recordings_directory=recordings_directory,
        )

        self._invoke_migration_assistant_apply(
            mappings_directory=mappings_directory,
            recordings_directory=recordings_directory,
        )

    def _assert_outputs(self, expected_outputs):

        for index, input_file in enumerate(self.input_files):
            output_file = Path(input_file).with_suffix(".py-migrated")
            output = output_file.read_text()
            expected_output = textwrap.dedent(expected_outputs[index])
            self.keep_test_files = output != expected_output  # keep the test files when failed
            indented_expected_output = textwrap.indent(expected_output, "  ")
            indented_actual_output = textwrap.indent(output, "  ")
            assert (
                output == expected_output
            ), f"Expected: {indented_expected_output}but got: {indented_actual_output}(see {self.temp_directory})"


def run(api, api_mappings, input, expected_output, api_root=None, in_process=True, extra_args=None, run_pytest=False):
    print(api_migration_assistant.__file__)
    with Runner(api, api_mappings, input, api_root, in_process, extra_args, run_pytest) as runner:
        runner._setup_api(),
        runner._setup_api_mappings(),
        runner._setup_input(),
        runner._run_migration_assistant()
        runner._assert_outputs(expected_output if isinstance(expected_output, list) else [expected_output])
