# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Test the `ground_vehicle_graphs` module."""

import pytest
from stk_environment import stk_root

from ansys.stk.extensions.data_analysis.graphs.ground_vehicle_graphs import cumulative_sunlight_cumulative_pie_chart, eclipse_times_interval_graph, lighting_times_interval_graph, solar_aer_line_chart, solar_az_el_polar_center_0_graph, sunlight_intervals_interval_pie_chart, lat_lon_position_line_chart, sun_vector_ecf_line_chart

@pytest.fixture()
def basic_ground_vehicle(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, VehicleWaypointComputationMethod, VehicleAltitudeReference, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    ground_vehicle = stk_root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "GroundVehicle")
    ground_vehicle.set_route_type(PropagatorType.GREAT_ARC)
    route = ground_vehicle.route
    route.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY
    route.set_altitude_reference_type(VehicleAltitudeReference.WGS84)
    waypoint = route.waypoints.add()
    waypoint.latitude = 56.18
    waypoint.longitude = 40.91
    waypoint.altitude = 0
    waypoint.speed = 1
    waypoint2 = route.waypoints.add()
    waypoint2.latitude = 50.22
    waypoint2.longitude = 11.05
    waypoint2.altitude = 0
    waypoint2.speed = 1
    waypoint3 = route.waypoints.add()
    waypoint3.latitude = 49
    waypoint3.longitude = 58
    waypoint3.altitude = 0
    waypoint3.speed = 1
    waypoint4 = route.waypoints.add()
    waypoint4.latitude = 43
    waypoint4.longitude = 7
    waypoint4.altitude = 0
    waypoint4.speed = 0.026
    waypoint5 = route.waypoints.add()
    waypoint5.latitude = 42
    waypoint5.longitude = 13
    waypoint5.altitude = 0
    waypoint5.speed = 0.026
    route.propagate()

    yield ground_vehicle

@pytest.mark.mpl_image_compare
def test_cumulative_sunlight_cumulative_pie_chart_groundvehicle(basic_ground_vehicle):
    fig, _ = cumulative_sunlight_cumulative_pie_chart(basic_ground_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_eclipse_times_interval_graph_groundvehicle(basic_ground_vehicle):
    fig, _ = eclipse_times_interval_graph(basic_ground_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_lat_lon_position_line_chart_groundvehicle(basic_ground_vehicle):
    fig, _ = lat_lon_position_line_chart(basic_ground_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_lighting_times_interval_graph_groundvehicle(basic_ground_vehicle):
    fig, _ = lighting_times_interval_graph(basic_ground_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_aer_line_chart_groundvehicle(basic_ground_vehicle):
    fig, _ = solar_aer_line_chart(basic_ground_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_az_el_polar_center_0_graph_groundvehicle(basic_ground_vehicle):
    fig, _ = solar_az_el_polar_center_0_graph(basic_ground_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_sun_vector_ecf_line_chart_groundvehicle(basic_ground_vehicle):
    fig, _ = sun_vector_ecf_line_chart(basic_ground_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_sunlight_intervals_interval_pie_chart_groundvehicle(basic_ground_vehicle):
    fig, _ = sunlight_intervals_interval_pie_chart(basic_ground_vehicle)
    return fig

