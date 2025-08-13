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

"""Test the `comm_system_graphs` module."""

import pytest
from ansys.stk.extensions.data_analysis.graphs.comm_system_graphs import carrier_to_noise_vs_time_line_chart
from stk_environment import stk_root

@pytest.fixture()
def comm_system(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    facility = scenario.children.new(STKObjectType.FACILITY, "Facility")
    satellite = stk_root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.common_tasks.add_segments_from_online_source("25544")
    propagator.propagate()

    comm_system =  scenario.children.new(STKObjectType.COMM_SYSTEM, "CommSystem")
    receiver =  facility.children.new(STKObjectType.RECEIVER, "Receiver")
    transmitter =  facility.children.new(STKObjectType.TRANSMITTER, "Transmitter")
    receiver_constellation =  scenario.children.new(STKObjectType.CONSTELLATION, "ReceiverConstellation")       
    receiver_constellation.objects.add_object(receiver)
    transmitter_constellation =  scenario.children.new(STKObjectType.CONSTELLATION, "TransmitterConstellation")
    transmitter_constellation.objects.add_object(transmitter)
    comm_system.transmitters.add("Constellation/TransmitterConstellation")
    comm_system.receivers.add("Constellation/ReceiverConstellation")
    comm_system.compute()

    yield comm_system

@pytest.mark.mpl_image_compare
def test_carrier_to_noise_vs_time_line_chart_commsystem(comm_system):
    fig, _ = carrier_to_noise_vs_time_line_chart(comm_system)
    return fig
