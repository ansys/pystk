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

"""Test the `coverage_definition_graphs` module."""

from ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs import coverage_by_latitude_line_chart, gap_duration_line_chart, gi_point_coverage_interval_graph, gi_point_prob_of_coverage_line_chart, gi_region_coverage_line_chart, gi_region_time_to_cover_line_chart, percent_coverage_line_chart, gi_region_full_coverage_interval_graph
import pytest
from pathlib import Path
from stk_environment import stk_root

@pytest.fixture()
def coverage_definition(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    coverage = scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "Coverage")
    satellite = stk_root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    tle_file = Path(__file__).parent / "data" / "iss_5Jun2022.tle"
    propagator.common_tasks.add_segments_from_file("25544", str(tle_file.resolve()))
    propagator.propagate()

    coverage.asset_list.add("Satellite/Satellite")
    coverage.compute_accesses()

    coverage.grid_inspector.select_point(-6,4)

    yield coverage

@pytest.fixture()
def coverage_definition_selected_region(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType, CoverageBounds

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    boundary = [[48, -128], [48.5, -128.5], [47.5, -128], [48, -128.7]]
    area_target = scenario.children.new(STKObjectType.AREA_TARGET, "AreaTarget")
    area_target.common_tasks.set_area_type_pattern(boundary)

    coverage = scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "Coverage")
    satellite = stk_root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    tle_file = Path(__file__).parent / "data" / "iss_5Jun2022.tle"
    propagator.common_tasks.add_segments_from_file("25544", str(tle_file.resolve()))
    propagator.propagate()

    coverage.grid.bounds_type = CoverageBounds.CUSTOM_REGIONS
    coverage.grid.bounds.area_targets.add("AreaTarget/AreaTarget")

    coverage.asset_list.add("Satellite/Satellite")
    coverage.compute_accesses()

    coverage.grid_inspector.select_region("AreaTarget")

    yield coverage

@pytest.mark.mpl_image_compare
def test_coverage_by_latitude_line_chart_coveragedefinition(coverage_definition):
    fig, _ = coverage_by_latitude_line_chart(coverage_definition)
    return fig

@pytest.mark.mpl_image_compare
def test_gap_duration_line_chart_coveragedefinition(coverage_definition):
    fig, _ = gap_duration_line_chart(coverage_definition)
    return fig

@pytest.mark.mpl_image_compare
def test_percent_coverage_line_chart_coveragedefinition(coverage_definition):
    fig, _ = percent_coverage_line_chart(coverage_definition)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_point_coverage_interval_graph_coveragedefinition(coverage_definition):
    fig, _ = gi_point_coverage_interval_graph(coverage_definition)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_point_prob_of_coverage_line_chart_coveragedefinition(coverage_definition):
    fig, _ = gi_point_prob_of_coverage_line_chart(coverage_definition)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_region_coverage_line_chart_coveragedefinition(coverage_definition_selected_region):
    fig, _ = gi_region_coverage_line_chart(coverage_definition_selected_region)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_region_time_to_cover_line_chart_coveragedefinition(coverage_definition_selected_region):
    fig, _ = gi_region_time_to_cover_line_chart(coverage_definition_selected_region)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_region_full_coverage_interval_graph_coveragedefinition(coverage_definition_selected_region):
    fig, _ = gi_region_full_coverage_interval_graph(coverage_definition_selected_region)
    return fig
