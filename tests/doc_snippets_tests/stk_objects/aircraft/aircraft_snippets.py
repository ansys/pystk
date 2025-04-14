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

from ansys.stk.core.stkobjects import (
    STKObjectType,
    VehicleAltitudeReference,
    AttitudeProfile,
    PropagatorType,
    VehicleWaypointComputationMethod,
)

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class AircraftSnippets(CodeSnippetsTestBase):
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

    def test_CreateAircraftSnippet(self):
        self.CreateAircraftSnippet(self.get_root())

    @code_snippet(
        name="CreateAircraft",
        description="Create a New Aircraft (on the current scenario central body)",
        category="STK Objects | Aircraft",
        eid="stkobjects~Aircraft",
    )
    def CreateAircraftSnippet(self, root):
        # StkObjectRoot root: STK Object Model root
        aircraft = root.current_scenario.children.new(STKObjectType.AIRCRAFT, "MyAircraft")

    def test_AddAircraftPointsSnippet(self):
        try:
            aircraft = self.get_scenario().children.new(STKObjectType.AIRCRAFT, "aircraft")

            self.AddAircraftPointsSnippet(aircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AddAircraftPoints",
        description="Set the Great Arc Propagator and Add Individual Waypoints to an Aircraft",
        category="STK Objects | Aircraft",
        eid="stkobjects~Aircraft",
    )
    def AddAircraftPointsSnippet(self, aircraft):
        # Aircraft aircraft: Aircraft object
        # Set route to great arc, method and altitude reference
        aircraft.set_route_type(PropagatorType.GREAT_ARC)
        route = aircraft.route
        route.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY
        route.set_altitude_reference_type(VehicleAltitudeReference.MEAN_SEA_LEVEL)
        # Add first point
        waypoint = route.waypoints.add()
        waypoint.latitude = 37.5378
        waypoint.longitude = 14.2207
        waypoint.altitude = 5  # km
        waypoint.speed = 0.1  # km/sec
        # Add second point
        waypoint2 = route.waypoints.add()
        waypoint2.latitude = 47.2602
        waypoint2.longitude = 30.5517
        waypoint2.altitude = 5  # km
        waypoint2.speed = 0.1  # km/sec
        # Propagate the route
        route.propagate()

    def test_AddAircraftArrayPointsSnippet(self):
        try:
            aircraft = self.get_scenario().children.new(STKObjectType.AIRCRAFT, "aircraft")

            self.AddAircraftArrayPointsSnippet(aircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AddAircraftArrayPoints",
        description="Add Array of Waypoints to Aircraft",
        category="STK Objects | Aircraft",
        eid="stkobjects~Aircraft",
    )
    def AddAircraftArrayPointsSnippet(self, aircraft):
        # Aircraft aircraft: Aircraft object
        route = aircraft.route
        ptsArray = [[37.5378, 14.2207, 3.0480, 0.0772, 2], [47.2602, 30.5517, 3.0480, 0.0772, 2]]
        route.set_points_smooth_rate_and_propagate(ptsArray)
        # Propagate the route
        route.propagate()

    def test_AircraftAttitudeSnippet(self):
        try:
            aircraft = self.get_scenario().children.new(STKObjectType.AIRCRAFT, "aircraft")
            self.AircraftAttitudeSnippet(aircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AircraftAttitude",
        description="Set the Attitude of the Aircraft",
        category="STK Objects | Aircraft",
        eid="stkobjects~Aircraft",
    )
    def AircraftAttitudeSnippet(self, aircraft):
        # Aircraft aircraft: Aircraft object
        aircraft.attitude.basic.set_profile_type(AttitudeProfile.COORDINATED_TURN)
