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

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class ConstellationSnippets(CodeSnippetsTestBase):
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

    def test_CreateConstellationSnippet(self):
        try:
            scenario = self.get_scenario()
            satellite = scenario.children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()
            MyFacility = scenario.children.new(STKObjectType.FACILITY, "MyFacility")

            self.CreateConstellationSnippet(self.get_root(), satellite)
        finally:
            satellite.unload()
            MyFacility.unload()

    @code_snippet(
        name="CreateConstellation",
        description="Define a constellation",
        category="STK Objects | Constellation",
        eid="STKObjects~IAgConstellation",
    )
    def CreateConstellationSnippet(self, root, satellite):
        # StkObjectRoot root: STK Object Model Root
        # Satellite satellite: Satellite object
        constellation = root.current_scenario.children.new(STKObjectType.CONSTELLATION, "MyConstellation")
        constellation.objects.add_object(satellite)
        constellation.objects.add("*/Facility/MyFacility")
