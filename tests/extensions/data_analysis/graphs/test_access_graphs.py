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
#

# """Test the `access_graphs` module."""

import pytest

import matplotlib

from ansys.stk.extensions.data_analysis.graphs.access_graphs import access_duration_pie_chart, bit_error_rate_line_chart, carrier_to_noise_ratio_line_chart, cumulative_dwell_cumulative_pie_chart, ebno_line_chart, radar_sar_azimuth_resolution_line_chart, radar_sar_time_resolution_line_chart, revisit_diagram_interval_pie_chart, aer_line_chart, access_interval_graph, az_el_polar_center_90_graph, angular_rates_line_chart, elevation_angle_line_chart, gaps_interval_graph, probability_of_detection_line_chart, radar_antenna_gain_line_chart, radar_propagation_loss_line_chart, radar_searchtrack_integration_line_chart, radar_searchtrack_snr_line_chart, radar_system_noise_line_chart, signal_to_noise_ratio_line_chart, sun_rfi_line_chart
from stk_environment import stk_root

@pytest.fixture()
def basic_access(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType, ConstraintLighting, AccessConstraintType

    stk_root.new_scenario("GraphTest")
    stk_root.execute_command("Terrain * TerrainServer UseTerrainForAnalysis No")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    facility = scenario.children.new(STKObjectType.FACILITY, "Facility")
    facility.position.assign_planetodetic(39.95, -75.16, 0)

    satellite = scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.common_tasks.add_segments_from_online_source("25544")
    propagator.propagate()

    lighting_constraint = satellite.access_constraints.add_constraint(
        AccessConstraintType.LIGHTING
    )
    lighting_constraint.condition = ConstraintLighting.DIRECT_SUN

    access = facility.get_access_to_object(satellite)
    access.compute_access()

    yield access

@pytest.fixture()
def leap_second_access(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    stk_root.execute_command("Terrain * TerrainServer UseTerrainForAnalysis No")
    scenario = stk_root.current_scenario
    scenario.set_time_period("30 Jun 2015 16:00:00.000", "1 Jul 2015 16:00:00.000")

    place = scenario.children.new(STKObjectType.PLACE, "Place")
    place.position.assign_planetodetic(-43.0076, -11.2231, 0)

    satellite = scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.common_tasks.add_segments_from_online_source("25544")
    propagator.propagate()

    access = place.get_access_to_object(satellite)
    access.compute_access()

    yield access

@pytest.fixture()
def basic_radar_access(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType

    stk_root.new_scenario("GraphTest")
    stk_root.execute_command("Terrain * TerrainServer UseTerrainForAnalysis No")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    aircraft = stk_root.current_scenario.children.new(STKObjectType.AIRCRAFT, "TargetAircraft")
    waypoint1 = aircraft.route.waypoints.add()
    waypoint1.latitude = 37
    waypoint1.longitude = 139.7
    waypoint1.altitude = 7.62
    waypoint1.speed = 330
    waypoint2 = aircraft.route.waypoints.add()
    waypoint2.latitude = 34
    waypoint2.longitude = 139.1
    waypoint2.altitude = 7.62
    waypoint2.speed = 330
    aircraft.route.propagate()

    radar_site = stk_root.current_scenario.children.new(STKObjectType.PLACE, "RadarSite")
    radar_site.position.assign_geodetic(35.75174, 139.35621, 0.01524)

    sensor = radar_site.children.new(STKObjectType.SENSOR, "Sensor")
    radar = sensor.children.new(STKObjectType.RADAR, "Radar")

    access = radar.get_access_to_object(aircraft)
    access.compute_access()

    yield access

@pytest.fixture()
def communications_access(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    satellite = stk_root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.common_tasks.add_segments_from_online_source("25544")
    propagator.propagate()

    facility = stk_root.current_scenario.children.new(STKObjectType.FACILITY, "Facility")
    receiver = satellite.children.new(STKObjectType.RECEIVER, "Receiver")
    transmitter = facility.children.new(STKObjectType.TRANSMITTER, "Transmitter")
    access = receiver.get_access_to_object(transmitter)

    access.compute_access()

    yield access

@pytest.fixture()
def sar_radar_access(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    satellite = stk_root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.common_tasks.add_segments_from_online_source("25544")
    propagator.propagate()

    facility = stk_root.current_scenario.children.new(STKObjectType.FACILITY, "Facility")
    radar = satellite.children.new(STKObjectType.RADAR, "Radar")
    radar.model_component_linking.component.mode_component_linking.set_component("SAR")
    access = radar.get_access_to_object(facility)

    access.compute_access()

    yield access

@pytest.mark.mpl_image_compare
def test_access_duration_pie_chart_access(basic_access):
    fig, _ = access_duration_pie_chart(basic_access)
    return fig

@pytest.mark.mpl_image_compare
def test_access_duration_pie_chart_during_leap_second(leap_second_access):
    fig, _ = access_duration_pie_chart(leap_second_access)
    return fig

@pytest.mark.mpl_image_compare
def test_access_duration_pie_chart_during_leap_second(leap_second_access):
    access = leap_second_access
    fig, _ = access_duration_pie_chart(access)
    return fig

@pytest.mark.mpl_image_compare
def test_access_duration_pie_chart_pass_colormap(basic_access):
    fig, _ = access_duration_pie_chart(basic_access, colormap=matplotlib.cm.plasma)
    return fig

@pytest.mark.mpl_image_compare
def test_access_duration_pie_chart_non_default_start_stop(basic_access):
    fig, _ = access_duration_pie_chart(basic_access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_chart_access(basic_access):
    fig, _ = cumulative_dwell_cumulative_pie_chart(basic_access)
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_chart_during_leap_second(leap_second_access):
    fig, _ = cumulative_dwell_cumulative_pie_chart(leap_second_access)
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_chart_during_leap_second(leap_second_access):
    access = leap_second_access
    fig, _ = cumulative_dwell_cumulative_pie_chart(access)
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_chart_pass_colors(basic_access):
    fig, _ = cumulative_dwell_cumulative_pie_chart(basic_access, color_list=["cornflowerblue", "orchid"])
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_chart_non_default_start_stop(basic_access):
    fig, _ = cumulative_dwell_cumulative_pie_chart(basic_access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig

@pytest.mark.mpl_image_compare
def test_revisit_diagram_interval_pie_chart_access(basic_access):
    fig, _ = revisit_diagram_interval_pie_chart(basic_access)
    return fig

@pytest.mark.mpl_image_compare
def test_revisit_diagram_interval_pie_chart_during_leap_second(leap_second_access):
    fig, _ = revisit_diagram_interval_pie_chart(leap_second_access)
    return fig

@pytest.mark.mpl_image_compare
def test_revisit_diagram_interval_pie_chart_non_default_start_stop(basic_access):
    fig, _ = revisit_diagram_interval_pie_chart(basic_access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig

def test_revisit_diagram_interval_pie_chart_raises_error_with_wrong_colors_length(basic_access):
    with pytest.raises(ValueError) as excinfo:
        revisit_diagram_interval_pie_chart(basic_access, color_list=["cornflowerblue"])
    assert "If provided, 'color_list' argument must contain at least 2 colors." in str(excinfo.value)

@pytest.mark.mpl_image_compare
def test_access_duration_pie_chart_gmt(basic_access):
    basic_access.base.root.units_preferences.set_current_unit("Date", "GMT")
    fig, _ = access_duration_pie_chart(basic_access, start_time= "156/00000 2022", stop_time = "156/43200 2022")
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_chart_gps(basic_access):
    basic_access.base.root.units_preferences.set_current_unit("Date", "GPS")
    fig, _ = cumulative_dwell_cumulative_pie_chart(basic_access, start_time= "2213:18.000", stop_time = "2213:43218.000")
    return fig

@pytest.mark.mpl_image_compare
def test_revisit_diagram_interval_pie_chart_taig(basic_access):
    basic_access.base.root.units_preferences.set_current_unit("Date", "TAIG")
    fig, _ = revisit_diagram_interval_pie_chart(basic_access, start_time= "5 Jun 2022 00:00:37.000", stop_time = "5 Jun 2022 12:00:37.000")
    return fig

@pytest.mark.mpl_image_compare
def test_aer_line_chart_access(basic_access):
    fig, _ = aer_line_chart(basic_access)
    return fig

def test_aer_line_chart_invalid_interval(basic_access):
    with pytest.raises(ValueError) as excinfo:
        _, _ = aer_line_chart(basic_access, start_time="4 Jun 2022 09:00:00.000", stop_time="4 Jun 2022 12:00:00.000")
    assert "No access data to plot- check provided start and stop times." in str(excinfo.value)

@pytest.mark.mpl_image_compare
def test_aer_line_chart_start_stop_contained_within_interval(basic_access):
    fig, _ = aer_line_chart(basic_access, start_time="5 Jun 2022 00:26:00.000", stop_time="5 Jun 2022 00:34:00.000")
    return fig

@pytest.mark.mpl_image_compare
def test_aer_line_chart_during_leap_second(leap_second_access):
    fig, _ = aer_line_chart(leap_second_access, start_time="30 Jun 2015 23:59:30.000", stop_time="1 Jul 2015 00:00:15.000")
    return fig

@pytest.mark.mpl_image_compare
def test_access_interval_graph_access(basic_access):
    fig, _ = access_interval_graph(basic_access)
    return fig

@pytest.mark.mpl_image_compare
def test_az_el_polar_center_90_graph_access(basic_access):
    fig, _ = az_el_polar_center_90_graph(basic_access)
    return fig

@pytest.mark.mpl_image_compare
def test_angular_rates_line_chart_access(basic_access):
    fig, _ = angular_rates_line_chart(basic_access)
    return fig

@pytest.mark.mpl_image_compare
def test_elevation_angle_line_chart_access(basic_access):
    fig, _ = elevation_angle_line_chart(basic_access)
    return fig

@pytest.mark.mpl_image_compare
def test_gaps_interval_graph_access(basic_access):
    fig, _ = gaps_interval_graph(basic_access)
    return fig

@pytest.mark.mpl_image_compare
def test_probability_of_detection_line_chart_access(basic_radar_access):
    fig, _ = probability_of_detection_line_chart(basic_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_radar_antenna_gain_line_chart_access(basic_radar_access):
    fig, _ = radar_antenna_gain_line_chart(basic_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_radar_propagation_loss_line_char_accesst(basic_radar_access):
    fig, _ = radar_propagation_loss_line_chart(basic_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_radar_searchtrack_integration_line_chart_access(basic_radar_access):
    fig, _ = radar_searchtrack_integration_line_chart(basic_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_radar_searchtrack_snr_line_chart_access(basic_radar_access):
    fig, _ = radar_searchtrack_snr_line_chart(basic_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_radar_system_noise_line_chart_access(basic_radar_access):
    fig, _ = radar_system_noise_line_chart(basic_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_signal_to_noise_ratio_line_chart_access(basic_radar_access):
    fig, _ = signal_to_noise_ratio_line_chart(basic_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_bit_error_rate_line_chart_access(communications_access):
    fig, _ = bit_error_rate_line_chart(communications_access)
    return fig

@pytest.mark.mpl_image_compare
def test_carrier_to_noise_ratio_line_chart_access(communications_access):
    fig, _ = carrier_to_noise_ratio_line_chart(communications_access)
    return fig

@pytest.mark.mpl_image_compare
def test_ebno_line_chart_access(communications_access):
    fig, _ = ebno_line_chart(communications_access)
    return fig

@pytest.mark.mpl_image_compare
def test_radar_sar_azimuth_resolution_line_chart_access(sar_radar_access):
    fig, _ = radar_sar_azimuth_resolution_line_chart(sar_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_radar_sar_time_resolution_line_chart_access(sar_radar_access):
    fig, _ = radar_sar_time_resolution_line_chart(sar_radar_access)
    return fig

@pytest.mark.mpl_image_compare
def test_sun_rfi_line_chart_access(communications_access):
    fig, _ = sun_rfi_line_chart(communications_access)
    return fig