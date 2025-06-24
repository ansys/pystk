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

from ansys.stk.extensions.data_analysis.graphs.access_graphs import access_duration_pie_chart, cumulative_dwell_cumulative_pie_chart, revisit_diagram_interval_pie_chart

from stk_environment import stk_root

@pytest.fixture()
def set_up_basic_access_scenario(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType, ConstraintLighting, AccessConstraintType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    facility = scenario.children.new(STKObjectType.FACILITY, "Facility")
    facility.use_terrain = False
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

@pytest.mark.mpl_image_compare
def test_access_duration_pie_chart(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = access_duration_pie_chart(access)
    return fig

@pytest.mark.mpl_image_compare
def test_access_duration_pie_chart_non_default_start_stop(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = access_duration_pie_chart(access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_chart(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = cumulative_dwell_cumulative_pie_chart(access)
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_chart_non_default_start_stop(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = cumulative_dwell_cumulative_pie_chart(access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig

@pytest.mark.mpl_image_compare
def test_revisit_diagram_interval_pie_chart(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = revisit_diagram_interval_pie_chart(access)
    return fig

@pytest.mark.mpl_image_compare
def test_revisit_diagram_interval_pie_chart_non_default_start_stop(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = revisit_diagram_interval_pie_chart(access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig