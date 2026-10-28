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

"""Test the `launch_vehicle_graphs` module."""

import pytest
from ansys.stk.extensions.data_analysis.graphs.launch_vehicle_graphs import altitude_line_chart, beta_angle_line_chart, cumulative_sunlight_cumulative_pie_chart, eclipse_times_interval_graph, euler_angles_line_chart, fixed_position_velocity_line_chart, j2000_position_velocity_line_chart, lighting_times_interval_graph, lla_position_line_chart, solar_aer_line_chart, solar_az_el_polar_center_0_graph, solar_intensity_line_chart, sun_vector_fixed_line_chart, yaw_pitch_roll_line_chart
from stk_environment import stk_root

@pytest.fixture()
def launch_vehicle(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    launch_vehicle = stk_root.current_scenario.children.new(STKObjectType.LAUNCH_VEHICLE, "LaunchVehicle")
    launch_vehicle.set_trajectory_type(PropagatorType.SIMPLE_ASCENT)
    trajectory = launch_vehicle.trajectory
    trajectory.propagate()

    yield launch_vehicle

@pytest.mark.mpl_image_compare
def test_altitude_line_chart_launchvehicle(launch_vehicle):
    fig, _ = altitude_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_beta_angle_line_chart_launchvehicle(launch_vehicle):
    fig, _ = beta_angle_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_sunlight_cumulative_pie_chart_launchvehicle(launch_vehicle):
    fig, _ = cumulative_sunlight_cumulative_pie_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_eclipse_times_interval_graph_launchvehicle(launch_vehicle):
    fig, _ = eclipse_times_interval_graph(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_euler_angles_line_chart_launchvehicle(launch_vehicle):
    fig, _ = euler_angles_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_fixed_position_velocity_line_chart_launchvehicle(launch_vehicle):
    fig, _ = fixed_position_velocity_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_j2000_position_velocity_line_chart_launchvehicle(launch_vehicle):
    fig, _ = j2000_position_velocity_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_lighting_times_interval_graph_launchvehicle(launch_vehicle):
    fig, _ = lighting_times_interval_graph(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_lla_position_line_chart_launchvehicle(launch_vehicle):
    fig, _ = lla_position_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_aer_line_chart_launchvehicle(launch_vehicle):
    fig, _ = solar_aer_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_az_el_polar_center_0_graph_launchvehicle(launch_vehicle):
    fig, _ = solar_az_el_polar_center_0_graph(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_intensity_line_chart_launchvehicle(launch_vehicle):
    fig, _ = solar_intensity_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_sun_vector_fixed_line_chart_launchvehicle(launch_vehicle):
    fig, _ = sun_vector_fixed_line_chart(launch_vehicle)
    return fig

@pytest.mark.mpl_image_compare
def test_yaw_pitch_roll_line_chart_launchvehicle(launch_vehicle):
    fig, _ = yaw_pitch_roll_line_chart(launch_vehicle)
    return fig

