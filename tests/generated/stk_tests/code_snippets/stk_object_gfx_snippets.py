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


class StkObjectGfxSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkObjectGfxSnippets, self).__init__(*args, **kwargs)

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

    # region SetUp
    def setUp(self):
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region SetScenarioDisplayToHideShowObjects
    @category("Graphics Tests")
    def test_SetScenarioDisplayToHideShowObjects(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "facility1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "facility2")

        self.SetScenarioDisplayToHideShowObjects((clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario, Scenario)))

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "facility2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "facility1")

    def SetScenarioDisplayToHideShowObjects(self, scenario: "Scenario"):
        gfx: "ScenarioGraphics" = scenario.graphics

        # Individually
        gfx.hide_object("Facility/facility1", "all")
        gfx.show_object("Facility/facility1", "1")

        # In Batches
        # HideObjects and ShowObjects expects as the first parameter a one dimensional array of object paths
        objects = ["Facility/facility1", "Facility/facility2"]
        gfx.hide_objects(objects, "1")
        gfx.show_objects(objects, "all")

    # endregion
