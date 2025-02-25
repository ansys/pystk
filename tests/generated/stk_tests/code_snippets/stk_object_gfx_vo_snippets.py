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

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


@category("Graphics Tests")
class StkObjectGfxVOSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkObjectGfxVOSnippets, self).__init__(*args, **kwargs)

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

    # region SetStkOjbectDisplayToAlwaysOn
    def test_SetStkOjbectDisplayToAlwaysOn(self):
        facility: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            STKObjectType.FACILITY, "facility1"
        )

        self.SetStkOjbectDisplayToAlwaysOn(facility)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "facility1")

    def SetStkOjbectDisplayToAlwaysOn(self, stkObject: "IStkObject"):
        display: "IDisplayTime" = clr.CastAs(stkObject, IDisplayTime)
        display.set_display_status_type(DisplayTimesType.ALWAYS_ON)

    # endregion

    # region SetStkObjectDisplayToUseIntervalsMode
    def test_SetStkObjectDisplayToUseIntervalsMode(self):
        facility: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            STKObjectType.FACILITY, "facility1"
        )

        self.SetStkObjectDisplayToUseIntervalsMode(facility)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "facility1")

    def SetStkObjectDisplayToUseIntervalsMode(self, stkObject: "IStkObject"):
        # Attempt to cast STK Object to the IDisplayTime interface
        display: "IDisplayTime" = clr.CastAs(stkObject, IDisplayTime)
        if display != None:
            if display.is_display_status_type_supported(DisplayTimesType.INTERVALS):
                display.set_display_status_type(DisplayTimesType.INTERVALS)

                # Get TimeIntervalCollection interface
                intervalCollection: "TimeIntervalCollection" = clr.CastAs(
                    display.display_times_data, TimeIntervalCollection
                )
                intervalCollection.remove_all()

                # Add subsequent intervals
                intervalCollection.add("1 Jan 2012 12:00:00.00", "1 Jan 2012 13:00:00.000")

    # endregion

    # region SetStkObjectDisplayToUseDuringAccessMode
    def test_SetStkObjectDisplayToUseDuringAccessMode(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.STAR, "star1")
        facility: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            STKObjectType.FACILITY, "facility1"
        )

        self.SetStkObjectDisplayToUseDuringAccessMode(facility)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "facility1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.STAR, "star1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "satellite1")

    def SetStkObjectDisplayToUseDuringAccessMode(self, stkObject: "IStkObject"):
        # Attempt to cast STK Object to the IDisplayTime interface
        display: "IDisplayTime" = clr.CastAs(stkObject, IDisplayTime)
        if display != None:
            if display.is_display_status_type_supported(DisplayTimesType.DURING_ACCESS):
                display.set_display_status_type(DisplayTimesType.DURING_ACCESS)

                duringAccess: "DisplayTimesDuringAccess" = clr.CastAs(
                    display.display_times_data, DisplayTimesDuringAccess
                )

                # Add subsequent existing stk objects to access display
                duringAccess.access_objects.add("Satellite/satellite1")
                duringAccess.access_objects.add("Star/star1")

    # endregion
