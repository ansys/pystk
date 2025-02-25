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


class MissileSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(MissileSnippets, self).__init__(*args, **kwargs)

    m_Object: "Missile" = None
    m_DefaultName: str = "missile1"

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
        MissileSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.MISSILE, MissileSnippets.m_DefaultName
            ),
            Missile,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.MISSILE, MissileSnippets.m_DefaultName
        )
        MissileSnippets.m_Object = None

    # endregion

    # region DefineMissileTrajectory
    def test_DefineMissileTrajectory(self):
        initialTimeUnit: str = CodeSnippetsTestBase.m_Root.units_preferences.get_current_unit_abbrv("TimeUnit")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("TimeUnit", "sec")

        self.DefineMissileTrajectory(MissileSnippets.m_Object)

        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("TimeUnit", initialTimeUnit)

    def DefineMissileTrajectory(self, missile: "Missile"):
        # Set missile trajectory type
        missile.set_trajectory_type(PropagatorType.BALLISTIC)

        # Retrieve the Propagator interface
        trajectory: "PropagatorBallistic" = clr.CastAs(missile.trajectory, PropagatorBallistic)

        # Set propagator settings if they should be other than defaults
        trajectory.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        trajectory.step = 60.0

        # Set flight parameters
        trajectory.set_launch_type(VehicleLaunch.DETIC)
        launch: "LaunchVehicleLocationDetic" = clr.CastAs(trajectory.launch, LaunchVehicleLocationDetic)
        launch.latitude = 0.0
        launch.longitude = 0.0
        launch.altitude = 0.0

        # Set impact location type
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)

        # Retrieve the impact point interface
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(
            trajectory.impact_location, VehicleImpactLocationPoint
        )
        impactLocation.set_launch_control_type(VehicleLaunchControl.FIXED_TIME_OF_FLIGHT)

        # Retrieve the launch flight interface
        launchControl: "LaunchVehicleControlFixedTimeOfFlight" = clr.CastAs(
            impactLocation.launch_control, LaunchVehicleControlFixedTimeOfFlight
        )
        launchControl.time_of_flight = 9000.0

        # Configure missile Impact parameters
        impactLocation.set_impact_type(VehicleImpact.IMPACT_LOCATION_DETIC)
        impact: "VehicleImpactLocationDetic" = clr.CastAs(impactLocation.impact, VehicleImpactLocationDetic)
        impact.latitude = -20.0
        impact.longitude = -20.0
        impact.altitude = 0.0

        # Propagate Missile
        trajectory.propagate()

    # endregion
