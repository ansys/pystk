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


class LaunchVehicleSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LaunchVehicleSnippets, self).__init__(*args, **kwargs)

    m_Object: "LaunchVehicle" = None
    m_DefaultName: str = "MyLaunchVehicle"

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
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()
        LaunchVehicleSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.LAUNCH_VEHICLE, LaunchVehicleSnippets.m_DefaultName
            ),
            LaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.LAUNCH_VEHICLE, LaunchVehicleSnippets.m_DefaultName
        )
        LaunchVehicleSnippets.m_Object = None

    # endregion

    # region CreateLaunchVehicleOnCurrentScenarioCentralBody
    def test_CreateLaunchVehicleOnCurrentScenarioCentralBody(self):
        (IStkObject(LaunchVehicleSnippets.m_Object)).unload()
        self.CreateLaunchVehicleOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateLaunchVehicleOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Launch vehicle
        launchVehicle: "LaunchVehicle" = clr.CastAs(
            root.current_scenario.children.new(STKObjectType.LAUNCH_VEHICLE, "MyLaunchVehicle"), LaunchVehicle
        )

    # endregion

    # region DetermineIfTrajectoryIsSupported
    def test_DetermineIfTrajectoryIsSupported(self):
        self.DetermineIfTrajectoryIsSupported(LaunchVehicleSnippets.m_Object)

    def DetermineIfTrajectoryIsSupported(self, launchVehicle: "LaunchVehicle"):
        supported: bool = launchVehicle.is_trajectory_type_supported(PropagatorType.REAL_TIME)

    # endregion
