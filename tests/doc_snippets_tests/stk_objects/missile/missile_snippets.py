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

from ansys.stk.core.stkobjects import STKObjectType, VehicleLaunchControl, PropagatorType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class MissileSnippets(CodeSnippetsTestBase):
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

    def test_CreateMissileSnippet(self):
        self.CreateMissileSnippet(self.get_root(), self.get_scenario())

    @code_snippet(
        name="CreateMissile",
        description="Create a New Missile (on the current scenario central body)",
        category="STK Objects | Missile",
        eid="STKObjects~IAgMissile",
    )
    def CreateMissileSnippet(self, root, scenario):
        # Scenario scenario: Scenario object
        missile = scenario.children.new(STKObjectType.MISSILE, "MyMissile")
        missile.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = missile.trajectory
        root.units_preferences.set_current_unit("DateFormat", "EpSec")
        trajectory.ephemeris_interval.set_explicit_interval(0, 0)  # stop time later computed based on propagation
        trajectory.launch.latitude = 29
        trajectory.launch.longitude = -81
        trajectory.impact_location.impact.latitude = 27
        trajectory.impact_location.impact.longitude = -43
        trajectory.impact_location.set_launch_control_type(VehicleLaunchControl.FIXED_APOGEE_ALTITUDE)
        trajectory.impact_location.launch_control.apogee_altitude = 1200  # km
        trajectory.propagate()
