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

"""Test the `chain_graphs` module."""

import pytest
from pathlib import Path
from ansys.stk.extensions.data_analysis.graphs.chain_graphs import complete_chain_access_interval_graph, individual_object_access_interval_graph, individual_strand_access_interval_graph, number_of_accesses_line_chart
from stk_environment import stk_root

@pytest.fixture()
def chain(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    facility = scenario.children.new(STKObjectType.FACILITY, "Facility")
    satellite = stk_root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    tle_file = Path(__file__).parent / "data" / "iss_5Jun2022.tle"
    propagator.common_tasks.add_segments_from_file("25544", str(tle_file.resolve()))
    propagator.propagate()

    chain = scenario.children.new(STKObjectType.CHAIN, "Chain")
    chain.start_object = facility
    chain.end_object = satellite
    chain.connections.add(facility, satellite, 0, 10)
    chain.optimal_strand_opts.compute = True
    chain.compute_access()

    yield chain

@pytest.mark.mpl_image_compare
def test_complete_chain_access_interval_graph_chain(chain):
    fig, _ = complete_chain_access_interval_graph(chain)
    return fig

@pytest.mark.mpl_image_compare
def test_individual_object_access_interval_graph_chain(chain):
    fig, _ = individual_object_access_interval_graph(chain)
    return fig

@pytest.mark.mpl_image_compare
def test_individual_strand_access_interval_graph_chain(chain):
    fig, _ = individual_strand_access_interval_graph(chain)
    return fig

@pytest.mark.mpl_image_compare
def test_number_of_accesses_line_chart_chain(chain):
    fig, _ = number_of_accesses_line_chart(chain)
    return fig

