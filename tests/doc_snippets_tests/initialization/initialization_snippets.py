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
import pytest
import sys


# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class InitializationSnippets(CodeSnippetsTestBase):
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
        return CodeSnippetsTestBase.m_Root.CurrentScenario

    @pytest.mark.skip(reason="Only one STKEngine instance is allowed per process")
    def test_StartSTKEngineSnippet(self):
        self.StartSTKEngineSnippet(self.get_root())

    @code_snippet(
        name="StartSTKEngine",
        description="Start STK Engine and get a reference to StkObjectRoot",
        category="Initialization",
        eid="STKObjects~IAgStkObjectRoot",
    )
    def StartSTKEngineSnippet(self, root):
        # Start new instance of STK Engine
        from ansys.stk.core.stkengine import STKEngine

        stk = STKEngine.StartApplication(no_graphics=False)  # optionally, no_graphics = True

        # Get the IAgStkObjectRoot interface
        root = stk.new_object_root()

    @pytest.mark.skip(reason="Require STK Desktop to be already running")
    @category("ExcludeOnLinux")
    def test_AttachSTKSnippet(self):
        self.AttachSTKSnippet(self.get_root())

    @code_snippet(
        name="AttachSTK",
        description="Get a reference to StkObjectRoot using a running STK instance",
        category="Initialization",
        eid="STKObjects~IAgStkObjectRoot",
    )
    def AttachSTKSnippet(self, root):
        # Get reference to running STK instance
        from ansys.stk.core.stkdesktop import STKDesktop

        stk = STKDesktop.attach_to_application()

        # Get the IAgStkObjectRoot interface
        root = stk.root

    @category("ExcludeOnLinux")
    def test_CreateSTKNewSnippet(self):
        self.CreateSTKNewSnippet(self.get_root())

    @code_snippet(
        name="CreateSTKNew",
        description="Start STK and get a reference to StkObjectRoot",
        category="Initialization",
        eid="STKObjects~IAgStkObjectRoot",
    )
    def CreateSTKNewSnippet(self, root):
        # Start new instance of STK
        from ansys.stk.core.stkdesktop import STKDesktop

        stk = STKDesktop.start_application(visible=True)  # using optional visible argument

        # Get the IAgStkObjectRoot interface
        root = stk.root

        # ...

        # Clean-up when done
        stk.shutdown()
