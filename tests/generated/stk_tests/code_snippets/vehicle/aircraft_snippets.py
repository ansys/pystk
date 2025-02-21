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
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class AircraftSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(AircraftSnippets, self).__init__(*args, **kwargs)

    m_Object: "Aircraft" = None
    m_DefaultName: str = "aircraft1"

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
        AircraftSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.AIRCRAFT, AircraftSnippets.m_DefaultName
            ),
            Aircraft,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.AIRCRAFT, AircraftSnippets.m_DefaultName
        )
        AircraftSnippets.m_Object = None

    # endregion

    # region SetAircraftToUseGreatArcPropagator
    def test_SetAircraftToUseGreatArcPropagator(self):
        self.SetAircraftToUseGreatArcPropagator(AircraftSnippets.m_Object)

    def SetAircraftToUseGreatArcPropagator(self, aircraft: "Aircraft"):
        # Set ship route to great arc
        aircraft.set_route_type(PropagatorType.GREAT_ARC)

        # Retrieve propagator interface
        propagator: "PropagatorGreatArc" = clr.CastAs(aircraft.route, PropagatorGreatArc)

    # endregion

    # region ConfigureAircraftRouteUsingGreatArcPropagator
    def test_ConfigureAircraftRouteUsingGreatArcPropagator(self):
        self.ConfigureAircraftRouteUsingGreatArcPropagator(AircraftSnippets.m_Object)

    def ConfigureAircraftRouteUsingGreatArcPropagator(self, aircraft: "Aircraft"):
        # Set ship route to great arc
        aircraft.set_route_type(PropagatorType.GREAT_ARC)

        # Retrieve propagator interface
        propagator: "PropagatorGreatArc" = clr.CastAs(aircraft.route, PropagatorGreatArc)
        propagator.arc_granularity = 51.333

        # Set Ref type to WayPtAltRefTerrain and retreive VehicleWaypointAltitudeReferenceTerrain interface
        propagator.set_altitude_reference_type(VehicleAltitudeReference.TERRAIN)
        altRef: "VehicleWaypointAltitudeReferenceTerrain" = clr.CastAs(
            propagator.altitude_reference, VehicleWaypointAltitudeReferenceTerrain
        )
        altRef.granularity = 51.33
        altRef.interpolation_method = VehicleWaypointInterpolationMethod.ELLIPSOID_HEIGHT

        propagator.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY

        # Add waypoints
        point1: "VehicleWaypointsElement" = propagator.waypoints.add()
        point1.latitude = 39.7674
        point1.longitude = -79.7292
        point1.altitude = 3.0
        point1.speed = 0.0772

        point2: "VehicleWaypointsElement" = propagator.waypoints.add()
        point2.latitude = 38.3721
        point2.longitude = -120.116
        point2.altitude = 3.0
        point2.speed = 0.0772

        # Propagate
        propagator.propagate()

    # endregion
