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

"""Test the `place_graphs` module."""
from ansys.stk.extensions.data_analysis.graphs.place_graphs import cumulative_sunlight_cumulative_pie_chart, eclipse_times_interval_graph, lighting_times_interval_graph, solar_aer_line_chart, solar_az_el_polar_center_0_graph, sunlight_intervals_interval_pie_chart
import pytest
from stk_environment import stk_root

@pytest.fixture()
def place(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType

    stk_root.new_scenario("GraphTest")
    stk_root.execute_command("Terrain * TerrainServer UseTerrainForAnalysis No")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    place = scenario.children.new(STKObjectType.PLACE, "Place")
    place.position.assign_planetodetic(39.95, -75.16, 0)

    yield place

@pytest.mark.mpl_image_compare
def test_cumulative_sunlight_cumulative_pie_chart_place(place):
    fig, _ = cumulative_sunlight_cumulative_pie_chart(place)
    return fig

@pytest.mark.mpl_image_compare
def test_eclipse_times_interval_graph_place(place):
    fig, _ = eclipse_times_interval_graph(place)
    return fig

@pytest.mark.mpl_image_compare
def test_lighting_times_interval_graph_place(place):
    fig, _ = lighting_times_interval_graph(place)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_aer_line_chart_place(place):
    fig, _ = solar_aer_line_chart(place)
    return fig

@pytest.mark.mpl_image_compare
def test_solar_az_el_polar_center_0_graph_place(place):
    fig, _ = solar_az_el_polar_center_0_graph(place)
    return fig

@pytest.mark.mpl_image_compare
def test_sunlight_intervals_interval_pie_chart_place(place):
    fig, _ = sunlight_intervals_interval_pie_chart(place)
    return fig

