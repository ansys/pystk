# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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
import sys

from ansys.stk.core.stkobjects import STKObjectType
from ansys.stk.core.stkutil import ExecuteMultipleCommandsMode

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class ConnectSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_root(self):
        return CodeSnippetsTestBase.m_Root

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.current_scenario

    def test_ConnectCommandSnippet(self):
        try:
            self.ConnectCommandSnippet(self.get_root())
        finally:
            self.get_root().get_object_from_path("*/Target/MyTarget").unload()

    @code_snippet(
        name="ConnectCommand",
        description="Execute Connect command",
        category="Connect",
        eid="stkobjects~StkObjectRoot",
    )
    def ConnectCommandSnippet(self, root):
        root.execute_command("New / */Target MyTarget")

    def test_ConnectCommandMultipleSnippet(self):
        try:
            self.ConnectCommandMultipleSnippet(self.get_root())
        finally:
            self.get_root().get_object_from_path("*/Place/MyPlace").unload()

    @code_snippet(
        name="ConnectCommandMultiple",
        description="Execute multiple Connect commands",
        category="Connect",
        eid="stkobjects~StkObjectRoot",
    )
    def ConnectCommandMultipleSnippet(self, root):
        commandList = [["New / */Place MyPlace"], ["SetPosition */Place/MyPlace Geodetic 37.9 -75.5 0.0"]]
        root.execute_multiple_commands(commandList, ExecuteMultipleCommandsMode.EXCEPTION_ON_ERROR)

    def test_ResultsConnectCommandSnippet(self):
        try:
            MyPlace = self.get_scenario().children.new(STKObjectType.PLACE, "MyPlace")
            self.ResultsConnectCommandSnippet(self.get_root())
        finally:
            MyPlace.unload()

    @code_snippet(
        name="ResultsConnectCommand",
        description="Extract data from Connect result",
        category="Connect",
        eid="stkobjects~StkObjectRoot",
    )
    def ResultsConnectCommandSnippet(self, root):
        result = root.execute_command('Report_RM */Place/MyPlace Style "Cartesian Position"')

        for i in range(0, result.count):
            cmdRes = result.item(i)
            print(cmdRes)
