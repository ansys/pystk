# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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


"""Test the `aircraft_graphs` module."""

import pytest

from ansys.stk.extensions.data_analysis.graphs.aircraft_graphs import cumulative_sunlight_cumulative_pie_chart, eclipse_times_interval_graph, lighting_times_interval_graph, lla_position_line_chart, solar_aer_line_chart, solar_az_el_polar_center_0_graph, solar_intensity_line_chart, sun_vector_ecf_line_chart, sunlight_intervals_interval_pie_chart
from stk_environment import stk_root

@pytest.fixture()
def basic_aircraft(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    aircraft = stk_root.current_scenario.children.new(STKObjectType.AIRCRAFT, "Aircraft")
    waypoint1 = aircraft.route.waypoints.add()
    waypoint1.latitude = 73
    waypoint1.longitude = 6.3
    waypoint1.altitude = 7.62
    waypoint1.speed = 330
    waypoint2 = aircraft.route.waypoints.add()
    waypoint2.latitude = 35
    waypoint2.longitude = 51.1
    waypoint2.altitude = 7.62
    waypoint2.speed = 330
    waypoint3 = aircraft.route.waypoints.add()
    waypoint3.latitude = 49.4
    waypoint3.longitude = 109.6
    waypoint3.altitude = 7.62
    waypoint3.speed = 330
    aircraft.route.propagate()

    yield aircraft

@pytest.mark.mpl_image_compare
def test_cumulative_sunlight_cumulative_pie_chart_aircraft(basic_aircraft):
    fig, _ = cumulative_sunlight_cumulative_pie_chart(basic_aircraft)
    return fig

@pytest.mark.mpl_image_compare
def test_eclipse_times_interval_graph_aircraft(basic_aircraft):
    fig, _ = eclipse_times_interval_graph(basic_aircraft)
    return fig

@pytest.mark.mpl_image_compare
def test_lighting_times_interval_graph_aircraft(basic_aircraft):
    fig, _ = lighting_times_interval_graph(basic_aircraft)
    return fig

@pytest.mark.mpl_image_compare
def test_lla_position_line_chart_aircraft(basic_aircraft):
    fig, _ = lla_position_line_chart(basic_aircraft, step=1)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_aer_line_chart_aircraft(basic_aircraft):
    fig, _ = solar_aer_line_chart(basic_aircraft, step=1)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_az_el_polar_center_0_graph_aircraft(basic_aircraft):
    fig, _ = solar_az_el_polar_center_0_graph(basic_aircraft, step=1)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_intensity_line_chart_aircraft(basic_aircraft):
    fig, _ = solar_intensity_line_chart(basic_aircraft, step=1)
    return fig

@pytest.mark.mpl_image_compare
def test_sun_vector_ecf_line_chart_aircraft(basic_aircraft):
    fig, _ = sun_vector_ecf_line_chart(basic_aircraft, step=1)
    return fig

@pytest.mark.mpl_image_compare
def test_sunlight_intervals_interval_pie_chart_aircraft(basic_aircraft):
    fig, _ = sunlight_intervals_interval_pie_chart(basic_aircraft)
    return fig