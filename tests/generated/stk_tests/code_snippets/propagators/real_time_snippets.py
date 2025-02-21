# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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


class RealTimeSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(RealTimeSnippets, self).__init__(*args, **kwargs)

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
        RealTimeSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.LAUNCH_VEHICLE, RealTimeSnippets.m_DefaultName
            ),
            LaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.LAUNCH_VEHICLE, RealTimeSnippets.m_DefaultName
        )
        RealTimeSnippets.m_Object = None

    # endregion

    # region ConfigureRealtimePropagator
    def test_ConfigureRealtimePropagator(self):
        scenarioObject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario
        scenario: "Scenario" = clr.CastAs(scenarioObject, Scenario)

        scenAnim: "ScenarioAnimation" = None
        anim: "IAnimation" = None
        holdTimeStepType: "ScenarioTimeStepType" = ScenarioTimeStepType.REAL_TIME
        if not TestBase.NoGraphicsMode:
            scenAnim = scenario.animation_settings
            holdTimeStepType = scenAnim.animation_step_type
            scenAnim.animation_step_type = ScenarioTimeStepType.REAL_TIME
            anim = clr.CastAs(CodeSnippetsTestBase.m_Root, IAnimation)
            anim.play_forward()

        RealTimeSnippets.m_Object.set_trajectory_type(PropagatorType.REAL_TIME)
        prop: "IPropagator" = RealTimeSnippets.m_Object.trajectory
        propRealtime: "PropagatorRealtime" = clr.CastAs(prop, PropagatorRealtime)

        self.ConfigureRealtimePropagator(CodeSnippetsTestBase.m_Root, propRealtime)
        if not TestBase.NoGraphicsMode:
            anim.pause()

            # Cleanup
            scenAnim.animation_step_type = holdTimeStepType

    def ConfigureRealtimePropagator(self, root: "StkObjectRoot", propagator: "PropagatorRealtime"):
        # Set Realtime Propagator settings if they should be other than
        # the defaults.
        propagator.interpolation_order = 1
        propagator.timeout_gap = 30.0
        propagator.time_step = 60.0
        if propagator.is_look_ahead_propagator_supported(LookAheadPropagator.TWO_BODY):
            # Set the look ahead type
            propagator.look_ahead_propagator = LookAheadPropagator.TWO_BODY

            # Set the duration time to look ahead and look behind
            duration: "VehicleDuration" = propagator.duration
            duration.look_ahead = 3600.0
            duration.look_behind = 3600.0

            # Apply the Realtime Propagator settings
            propagator.propagate()

    # endregion

    # region AddRealtimeLLAPositions
    def test_AddRealtimeLLAPositions(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        gv.set_route_type(PropagatorType.REAL_TIME)
        (PropagatorRealtime(gv.route)).propagate()
        realtime: "PropagatorRealtime" = clr.CastAs(gv.route, PropagatorRealtime)
        self.AddRealtimeLLAPositions(realtime)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.GROUND_VEHICLE, "gv1")

    def AddRealtimeLLAPositions(self, propagator: "PropagatorRealtime"):
        points: "PropagatorRealtimeDeticPoints" = propagator.point_builder.ephemeris_in_latitude_longituide_altitude
        points.add("1 Jan 2012 12:00:00.000", 39.693, -76.399, 0.039, 0.03458, 0.01223, 0.05402)

    # endregion

    # region AddRealtimeLLAPositionsInBatches
    def test_AddRealtimeLLAPositionsInBatches(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        gv.set_route_type(PropagatorType.REAL_TIME)
        (PropagatorRealtime(gv.route)).propagate()
        realtime: "PropagatorRealtime" = clr.CastAs(gv.route, PropagatorRealtime)
        self.AddRealtimeLLAPositionsInBatches(realtime)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.GROUND_VEHICLE, "gv1")

    def AddRealtimeLLAPositionsInBatches(self, propagator: "PropagatorRealtime"):
        # Add realtime LLA points in batches
        times = ["1 Jan 2012 12:00:00.000", "1 Jan 2012 12:01:00.000", "1 Jan 2012 12:02:00.000"]
        lat = [39.693, 41.061, 39.925]
        lon = [-76.399, -74.266, -78.578]
        alt = [0.039, 0.042, 0.281]
        latrate = [0.03458, 0.03215, 0.03188]
        lonrate = [0.01223, 0.01148, 0.01075]
        altrate = [0.05402, 0.0521, 0.05075]

        points: "PropagatorRealtimeDeticPoints" = propagator.point_builder.ephemeris_in_latitude_longituide_altitude

        # AddBatch expects each parameter to be a one dimensional array and all of the same length
        points.add_batch(times, lat, lon, alt, latrate, lonrate, altrate)

    # endregion
