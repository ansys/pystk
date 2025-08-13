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

"""Test the `satellite_graphs` module."""

from ansys.stk.extensions.data_analysis.graphs.satellite_graphs import beta_angle_line_chart, classical_orbit_elements_line_chart, euler_angles_line_chart, fixed_position_velocity_line_chart, inertial_position_velocity_line_chart, j2000_position_velocity_line_chart, solar_elevation_body_fixed_line_chart, solar_intensity_line_chart, sun_vector_fixed_line_chart, yaw_pitch_roll_line_chart, sunlight_intervals_interval_pie_chart, cumulative_sunlight_cumulative_pie_chart, eclipse_times_interval_graph, lighting_times_interval_graph, solar_az_el_polar_center_0_graph, solar_aer_line_chart, lla_position_line_chart
import pytest
from stk_environment import stk_root

@pytest.fixture()
def satellite(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    satellite = stk_root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.common_tasks.add_segments_from_online_source("25544")
    propagator.propagate()

    yield satellite

@pytest.mark.mpl_image_compare
def test_beta_angle_line_chart_satellite(satellite):
    fig, _ = beta_angle_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_classical_orbit_elements_line_chart_satellite(satellite):
    fig, _ = classical_orbit_elements_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_sunlight_cumulative_pie_chart_satellite(satellite):
    fig, _ = cumulative_sunlight_cumulative_pie_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_eclipse_times_interval_graph_satellite(satellite):
    fig, _ = eclipse_times_interval_graph(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_euler_angles_line_chart_satellite(satellite):
    fig, _ = euler_angles_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_fixed_position_velocity_line_chart_satellite(satellite):
    fig, _ = fixed_position_velocity_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_inertial_position_velocity_line_chart_satellite(satellite):
    fig, _ = inertial_position_velocity_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_j2000_position_velocity_line_chart_satellite(satellite):
    fig, _ = j2000_position_velocity_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_lighting_times_interval_graph_satellite(satellite):
    fig, _ = lighting_times_interval_graph(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_lla_position_line_chart_satellite(satellite):
    fig, _ = lla_position_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_aer_line_chart_satellite(satellite):
    fig, _ = solar_aer_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_az_el_polar_center_0_graph_satellite(satellite):
    fig, _ = solar_az_el_polar_center_0_graph(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_elevation_body_fixed_line_chart_satellite(satellite):
    fig, _ = solar_elevation_body_fixed_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_intensity_line_chart_satellite(satellite):
    fig, _ = solar_intensity_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_sun_vector_fixed_line_chart_satellite(satellite):
    fig, _ = sun_vector_fixed_line_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_sunlight_intervals_interval_pie_chart_satellite(satellite):
    fig, _ = sunlight_intervals_interval_pie_chart(satellite)
    return fig

@pytest.mark.mpl_image_compare
def test_yaw_pitch_roll_line_chart_satellite(satellite):
    fig, _ = yaw_pitch_roll_line_chart(satellite)
    return fig

