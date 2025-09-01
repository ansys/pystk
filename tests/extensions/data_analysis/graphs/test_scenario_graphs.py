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

import pytest
from ansys.stk.extensions.data_analysis.graphs.scenario_graphs import greenwich_hour_angle_line_chart, polewanderx_line_chart, polewandery_line_chart, ut1_utc_line_chart
from stk_environment import stk_root

@pytest.fixture()
def scenario(stk_root):
    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    yield scenario

@pytest.mark.mpl_image_compare
def test_greenwich_hour_angle_line_chart_scenario(scenario):
    fig, _ = greenwich_hour_angle_line_chart(scenario)
    return fig

@pytest.mark.mpl_image_compare
def test_polewanderx_line_chart_scenario(scenario):
    fig, _ = polewanderx_line_chart(scenario)
    return fig

@pytest.mark.mpl_image_compare
def test_polewandery_line_chart_scenario(scenario):
    fig, _ = polewandery_line_chart(scenario)
    return fig

@pytest.mark.mpl_image_compare
def test_ut1_utc_line_chart_scenario(scenario):
    fig, _ = ut1_utc_line_chart(scenario)
    return fig

