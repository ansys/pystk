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
    PropagatorType,
    VehicleWaypointComputationMethod,
    VehicleWaypointInterpolationMethod,
)

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class GroundVehicleSnippets(CodeSnippetsTestBase):
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

    def test_CreateVehicleSnippet(self):
        self.CreateVehicleSnippet(self.get_scenario())

    @code_snippet(
        name="CreateVehicle",
        description="Create a New Ground Vehicle (on the current scenario central body)",
        category="STK Objects | Ground Vehicle",
        eid="STKObjects~IAgGroundVehicle",
    )
    def CreateVehicleSnippet(self, scenario):
        # Scenario scenario: Scenario object
        grndVehicle = scenario.children.new(STKObjectType.GROUND_VEHICLE, "MyVehicle")
        grndVehicle.set_route_type(PropagatorType.GREAT_ARC)

    def test_AddGroundVehiclePointsSnippet(self):
        try:
            grndVehicle = self.get_scenario().children.new(STKObjectType.GROUND_VEHICLE, "grndVehicle")

            self.AddGroundVehiclePointsSnippet(grndVehicle)
        finally:
            grndVehicle.unload()

    @code_snippet(
        name="AddGroundVehiclePoints",
        description="Set Great Arc Propagator and Add Individual Waypoints to Ground Vehicle",
        category="STK Objects | Ground Vehicle",
        eid="STKObjects~IAgGroundVehicle",
    )
    def AddGroundVehiclePointsSnippet(self, groundVehicle):
        # GroundVehicle grndVehicle: Ground Vehicle object
        # Set route to great arc, method and altitude reference
        groundVehicle.set_route_type(PropagatorType.GREAT_ARC)
        route = groundVehicle.route
        route.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY
        route.set_altitude_reference_type(VehicleAltitudeReference.WGS84)
        # Add first point
        waypoint = route.waypoints.add()
        waypoint.latitude = 56.18
        waypoint.longitude = 40.91
        waypoint.altitude = 0  # km
        waypoint.speed = 0.026  # km/sec
        # Add second point
        waypoint2 = route.waypoints.add()
        waypoint2.latitude = 50.22
        waypoint2.longitude = 11.05
        waypoint2.altitude = 0  # km
        waypoint2.speed = 0.026  # km/sec
        # Propagate the route
        route.propagate()

    def test_AddGroundVehicleArrayPointsSnippet(self):
        try:
            grndVehicle = self.get_scenario().children.new(STKObjectType.GROUND_VEHICLE, "grndVehicle")

            self.AddGroundVehicleArrayPointsSnippet(grndVehicle)
        finally:
            grndVehicle.unload()

    @code_snippet(
        name="AddGroundVehicleArrayPoints",
        description="Add Array of Waypoints to Ground Vehicle and Interpolate over Terrain",
        category="STK Objects | Ground Vehicle",
        eid="STKObjects~IAgGroundVehicle",
    )
    def AddGroundVehicleArrayPointsSnippet(self, grndVehicle):
        # GroundVehicle grndVehicle: Ground Vehicle object
        route = grndVehicle.route
        ptsArray = [
            [41.97766217, 21.44863761, 0, 0.026, 0.5],
            [41.97422351, 21.39956154, 0, 0.026, 0.5],
            [41.99173299, 21.40796942, 0, 0.026, 0.5],
        ]
        route.set_points_smooth_rate_and_propagate(ptsArray)
        route.set_altitude_reference_type(VehicleAltitudeReference.TERRAIN)
        route.altitude_reference.granularity = 0.001
        route.altitude_reference.interpolation_method = VehicleWaypointInterpolationMethod.TERRAIN_HEIGHT
        # Propagate the route
        route.propagate()
