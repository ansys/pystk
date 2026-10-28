# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Test the `line_target_graphs` module."""
from ansys.stk.extensions.data_analysis.graphs.line_target_graphs import anchor_point_solar_az_el_line_chart
import pytest
from stk_environment import stk_root

@pytest.fixture()
def line_target(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("30 Jun 2015 16:00:00.000", "1 Jul 2015 16:00:00.000")

    line_target = scenario.children.new(STKObjectType.LINE_TARGET, "LineTarget")
    line_target.points.add(53.76, -21.35)
    line_target.points.add(0, 0)

    yield line_target

@pytest.mark.mpl_image_compare
def test_anchor_point_solar_az_el_line_chart_linetarget(line_target):
    fig, _ = anchor_point_solar_az_el_line_chart(line_target)
    return fig