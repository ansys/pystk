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

from ansys.stk.core.stkdesktop import STKDesktop
from ansys.stk.core.stkobjects import AnimationEndTimeMode, AnimationOptionType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, Scenario, TestBase, category


class ScenarioManagementSnippets(CodeSnippetsTestBase):
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

    def reset_to_default_scenario(self):
        # See CodeSnippetsTestBase.Initialize()
        if TestBase.Application.current_scenario != None:
            TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("CodeSnippetScenario")
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        scenario.set_time_period("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")

    def test_OpenVdfSTKSnippet(self):
        try:
            root = self.get_root()
            root.close_scenario()
            self.OpenVdfSTKSnippet(root)
        finally:
            self.reset_to_default_scenario()

    @code_snippet(
        name="OpenVdfSTK",
        description="Open a Viewer Data File",
        category="Scenario | Scenario Management",
        eid="stkobjects~StkObjectRoot | stkobjects~StkObjectRoot~load_vdf",
    )
    def OpenVdfSTKSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        root.load_vdf(os.path.join(installPath, "Data", "ExampleScenarios", "Intro_STK_Space_Systems.vdf"), "")

    def test_CloseScenarioSnippet(self):
        try:
            root = self.get_root()
            root.close_scenario()
            self.CloseScenarioSnippet(root)
        finally:
            self.reset_to_default_scenario()

    @code_snippet(
        name="CloseScenario",
        description="Close an open Scenario",
        category="Scenario | Scenario Management",
        eid="stkobjects~StkObjectRoot | stkobjects~StkObjectRoot~close_scenario",
    )
    def CloseScenarioSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        root.close_scenario()

    def test_STKEngineEventsSnippet(self):
        try:
            root = self.get_root()
            root.close_scenario()
            self.STKEngineEventsSnippet(self.get_root())
        finally:
            self.reset_to_default_scenario()

    @code_snippet(
        name="STKEngineEvents",
        description="Manage STK Engine events",
        category="Scenario | Scenario Management",
        eid="stkobjects~StkObjectRoot",
    )
    def STKEngineEventsSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        def on_scenario_new_custom_callback(path: str):
            print(f'Scenario {path} has been created.')

        skt_object_root_events = root.subscribe()
        skt_object_root_events.on_scenario_new += on_scenario_new_custom_callback
        
        root.new_scenario('ExampleScenario')
        # callback should be executed now

        # remove the callback from the handler
        skt_object_root_events.on_scenario_new -= on_scenario_new_custom_callback

        # all finished with events, unsubscribe
        skt_object_root_events.unsubscribe()

    @pytest.mark.skip(reason="User interface interaction required to prevent application from hanging")
    @category("ExcludeOnLinux")
    def test_STKDesktopEventsSnippet(self):
        self.STKDesktopEventsSnippet()

    @code_snippet(
        name="STKDesktopEvents",
        description="Manage STK Desktop events",
        category="Scenario | Scenario Management",
        eid="stkobjects~StkObjectRoot",
    )
    def STKDesktopEventsSnippet(self):
        from ansys.stk.core.stkdesktop import STKDesktop
        from ansys.stk.core.stkobjects import STKObjectType

        def on_stk_object_added_custom_callback(path:str):
            print(f'{path} has been added.')

        stk = STKDesktop.start_application(visible=True)
        root = stk.root
        root.new_scenario('ExampleScenario')
        skt_object_root_events = root.subscribe()
        skt_object_root_events.on_stk_object_added += on_stk_object_added_custom_callback
        scenario = root.current_scenario

        # on_stk_object_added_custom_callback is successfully called when the next line is executed
        facility = scenario.children.new(STKObjectType.FACILITY, 'Exton')

        # Now switch control to the desktop application and create another facility.
        # The user interface becomes unresponsive.

        # Now open a tkinter window that processing Windows messages.
        from tkinter import Tk

        window = Tk()
        window.mainloop()
        # Switch control to the desktop application and create another facility.
        # The user interface is responsive and the event callback is successful.

    @category("ExcludeOnLinux")
    def test_CloseSTKSnippet(self):
        try:
            uiApplication = STKDesktop.start_application(visible=True)
            self.CloseSTKSnippet(uiApplication)
        finally:
            uiApplication.shutdown()

    @code_snippet(
        name="CloseSTK",
        description="Close STK",
        category="Scenario | Scenario Management",
        eid="uiapplication~UiApplication",
    )
    def CloseSTKSnippet(self, uiApplication):
        # AgUiApplication uiApplication: STK Application
        uiApplication.shutdown()

    def test_CreateScenarioSnippet(self):
        try:
            root = self.get_root()
            root.close_scenario()
            self.CreateScenarioSnippet(root)
        finally:
            self.reset_to_default_scenario()

    @code_snippet(
        name="CreateScenario",
        description="Create a new Scenario",
        category="Scenario | Scenario Management",
        eid="stkobjects~StkObjectRoot | stkobjects~StkObjectRoot~new_scenario",
    )
    def CreateScenarioSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        root.new_scenario("Example_Scenario")

    def test_SetUnitPreferencesSnippet(self):
        self.SetUnitPreferencesSnippet(self.get_root())

    @code_snippet(
        name="SetUnitPreferences",
        description="Set unit preferences for Object Model",
        category="Scenario | Scenario Management",
        eid="stkobjects~StkObjectRoot | stkobjects~StkObjectRoot~units_preferences",
    )
    def SetUnitPreferencesSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        root.units_preferences.item("DateFormat").set_current_unit("UTCG")
        root.units_preferences.item("Distance").set_current_unit("km")

    def test_SetScenarioTimePeriodSnippet(self):
        root = self.get_root()
        self.SetScenarioTimePeriodSnippet(root)

    @code_snippet(
        name="SetScenarioTimePeriod",
        description="Set the current scenario's time period",
        category="Scenario | Scenario Management",
        eid="stkobjects~Scenario | stkobjects~Scenario~set_time_period",
    )
    def SetScenarioTimePeriodSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        scenario = root.current_scenario
        scenario.set_time_period(
            start_time="1 Jan 2012 12:00:00.000", 
            stop_time="2 Jan 2012 12:00:00.000"
        )

    @category("Graphics Tests")
    def test_ScenarioAnimationModeSnippet(self):
        self.ScenarioAnimationModeSnippet(self.get_root())

    @code_snippet(
        name="ScenarioAnimationMode",
        description="Change animation mode",
        category="Scenario | Scenario Management",
        eid="stkobjects~IAnimation",
    )
    def ScenarioAnimationModeSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        scenario = root.current_scenario
        root.animation_options = AnimationOptionType.STOP
        root.mode = AnimationEndTimeMode.X_REAL_TIME
        scenario.animation_settings.animation_step_value = 1  # second
        scenario.animation_settings.refresh_delta = 0.03  # second

    @category("Graphics Tests")
    def test_ScenarioResetSnippet(self):
        self.ScenarioResetSnippet(self.get_root())

    @code_snippet(
        name="ScenarioReset",
        description="Reset the scenario time",
        category="Scenario | Scenario Management",
        eid="stkobjects~IAnimation",
    )
    def ScenarioResetSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        root.rewind()

    @category("Graphics Tests")
    def test_ScenarioFontSnippet(self):
        self.ScenarioFontSnippet(self.get_root())

    @code_snippet(
        name="ScenarioFont",
        description="Change scenario font",
        category="Scenario | Scenario Management",
        eid="stkobjects~ScenarioGraphics3D",
    )
    def ScenarioFontSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        scenario = root.current_scenario
        scenario.graphics_3d.medium_font.name = "Arial"
        scenario.graphics_3d.medium_font.point_size = 18
        scenario.graphics_3d.medium_font.bold = True
        scenario.graphics_3d.medium_font.italic = False
