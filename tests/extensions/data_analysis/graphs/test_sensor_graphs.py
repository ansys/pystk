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

"""Test the `sensor_graphs` module."""
import pytest
from stk_environment import stk_root
from ansys.stk.extensions.data_analysis.graphs.sensor_graphs import azimuth_elevation_line_chart, footprint_area_line_chart

@pytest.fixture()
def sensor(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType

    stk_root.new_scenario("GraphTest")
    stk_root.execute_command("Terrain * TerrainServer UseTerrainForAnalysis No")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    place = scenario.children.new(STKObjectType.PLACE, "Place")
    place.position.assign_planetodetic(39.95, -75.16, 0)

    sensor = place.children.new(STKObjectType.SENSOR, "Sensor")

    yield sensor

@pytest.fixture()
def sensor_from_satellite(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    satellite = stk_root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.common_tasks.add_segments_from_online_source("25544")
    propagator.propagate()

    sensor = satellite.children.new(STKObjectType.SENSOR, "Sensor")

    yield sensor

@pytest.mark.mpl_image_compare
def test_azimuth_elevation_line_chart_sensor(sensor):
    fig, _ = azimuth_elevation_line_chart(sensor)
    return fig

@pytest.mark.mpl_image_compare
def test_footprint_area_line_chart_sensor(sensor_from_satellite):
    fig, _ = footprint_area_line_chart(sensor_from_satellite)
    return fig