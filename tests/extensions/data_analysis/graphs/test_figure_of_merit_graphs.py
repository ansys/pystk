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

"""Test the `figure_of_merit_graphs` module."""

from ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs import gi_region_fom_line_chart, gi_region_satisfaction_interval_graph, grid_stats_over_time_line_chart, satisfied_by_time_line_chart, value_by_latitude_line_chart, value_by_longitude_line_chart, gi_point_fom_line_chart, gi_point_satisfaction_interval_graph, gi_all_dop_line_chart
import pytest
from pathlib import Path
from stk_environment import stk_root

@pytest.fixture()
def fom(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType, FigureOfMeritSatisfactionType, FigureOfMeritDefinitionType, FigureOfMeritCompute

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
    coverage.grid_inspector.select_point(-6,4)
    coverage.compute_accesses()

    fom = coverage.children.new(STKObjectType.FIGURE_OF_MERIT, "FigureOfMerit")
    fom.set_definition_type(FigureOfMeritDefinitionType.ACCESS_DURATION)
    fom.definition.set_compute_type(FigureOfMeritCompute.AVERAGE)
    fom.definition.satisfaction.enable_satisfaction = True
    fom.definition.satisfaction.satisfaction_type = FigureOfMeritSatisfactionType.GREATER_THAN
    fom.definition.satisfaction.satisfaction_threshold = 5

    yield fom

@pytest.fixture()
def fom_dop(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType, FigureOfMeritSatisfactionType, FigureOfMeritDefinitionType, FigureOfMeritCompute

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
    coverage.grid_inspector.select_point(-6,4)
    coverage.compute_accesses()

    fom = coverage.children.new(STKObjectType.FIGURE_OF_MERIT, "FigureOfMerit")
    fom.set_definition_type(FigureOfMeritDefinitionType.DILUTION_OF_PRECISION)
    fom.definition.set_compute_type(FigureOfMeritCompute.AVERAGE)
    fom.definition.satisfaction.enable_satisfaction = True
    fom.definition.satisfaction.satisfaction_type = FigureOfMeritSatisfactionType.GREATER_THAN
    fom.definition.satisfaction.satisfaction_threshold = 5

    yield fom

@pytest.fixture()
def fom_selected_region(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType, CoverageBounds, FigureOfMeritDefinitionType, FigureOfMeritCompute, FigureOfMeritSatisfactionType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    boundary = [[29, -12], [29, 34], [6, 34], [6, -12]]
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

    fom = coverage.children.new(STKObjectType.FIGURE_OF_MERIT, "FigureOfMerit")
    fom.set_definition_type(FigureOfMeritDefinitionType.ACCESS_DURATION)
    fom.definition.set_compute_type(FigureOfMeritCompute.AVERAGE)
    fom.definition.satisfaction.enable_satisfaction = True
    fom.definition.satisfaction.satisfaction_type = FigureOfMeritSatisfactionType.GREATER_THAN
    fom.definition.satisfaction.satisfaction_threshold = 5

    yield fom

@pytest.mark.mpl_image_compare
def test_grid_stats_over_time_line_chart_figureofmerit(fom):
    fig, _ = grid_stats_over_time_line_chart(fom)
    return fig

@pytest.mark.mpl_image_compare
def test_satisfied_by_time_line_chart_figureofmerit(fom):
    fig, _ = satisfied_by_time_line_chart(fom)
    return fig

@pytest.mark.mpl_image_compare
def test_value_by_latitude_line_chart_figureofmerit(fom):
    fig, _ = value_by_latitude_line_chart(fom)
    return fig

@pytest.mark.mpl_image_compare
def test_value_by_longitude_line_chart_figureofmerit(fom):
    fig, _ = value_by_longitude_line_chart(fom)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_point_fom_line_chart_figureofmerit(fom):
    fig, _ = gi_point_fom_line_chart(fom)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_point_satisfaction_interval_graph_figureofmerit(fom):
    fig, _ = gi_point_satisfaction_interval_graph(fom)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_region_fom_line_chart_figureofmerit(fom_selected_region):
    fig, _ = gi_region_fom_line_chart(fom_selected_region)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_region_satisfaction_interval_graph_figureofmerit(fom_selected_region):
    fig, _ = gi_region_satisfaction_interval_graph(fom_selected_region)
    return fig

@pytest.mark.mpl_image_compare
def test_gi_all_dop_line_chart_figureofmerit(fom_dop):
    fig, _ = gi_all_dop_line_chart(fom_dop)
    return fig