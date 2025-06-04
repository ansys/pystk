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

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class ConnectSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ConnectSnippets, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region ExecuteConnectCommand
    def test_ExecuteConnectCommand(self):
        self.ExecuteConnectCommand(CodeSnippetsTestBase.m_Root)

    def ExecuteConnectCommand(self, root: "STKObjectRoot"):
        result: "ExecuteCommandResult" = root.execute_command("New / */Satellite JeffSAT")

    # endregion

    # region ExecuteMultipleConnectCommands
    @category("Graphics Tests")
    def test_ExecuteMultipleConnectCommands(self):
        self.ExecuteMultipleConnectCommands(CodeSnippetsTestBase.m_Root)

    def ExecuteMultipleConnectCommands(self, root: "STKObjectRoot"):
        connectCommands = ["New / */Satellite MySatellite", "Graphics */Satellite/MySatellite SetColor red"]

        # ExecuteMultipleCommands expect a one dimensional array of Connect commands
        result: "ExecuteMultipleCommandsResult" = root.execute_multiple_commands(
            connectCommands, ExecuteMultipleCommandsMode.EXCEPTION_ON_ERROR
        )

    # endregion

    # region ExtractDataFromExecConnectResult
    def test_ExtractDataFromExecConnectResult(self):
        result: "ExecuteCommandResult" = CodeSnippetsTestBase.m_Root.execute_command("GetSTKVersion /")
        self.ExtractDataFromExecConnectResult(result)

    def ExtractDataFromExecConnectResult(self, result: "ExecuteCommandResult"):
        if result.is_succeeded:
            i: int = 0
            while i < result.count:
                Console.WriteLine(result[i])

                i += 1

    # endregion

    # region ExtractDataFromMultiExecConnectResult
    def test_ExtractDataFromMultiExecConnectResult(self):
        obj = ["GetSTKVersion /"]

        result: "ExecuteMultipleCommandsResult" = CodeSnippetsTestBase.m_Root.execute_multiple_commands(
            obj, ExecuteMultipleCommandsMode.CONTINUE_ON_ERROR
        )
        self.ExtractDataFromMultiExecConnectResult(result)

    def ExtractDataFromMultiExecConnectResult(self, result: "ExecuteMultipleCommandsResult"):
        i: int = 0
        while i < result.count:
            if result[i].is_succeeded:
                j: int = 0
                while j < result[i].count:
                    Console.WriteLine(result[j])

                    j += 1

            i += 1

    # endregion
