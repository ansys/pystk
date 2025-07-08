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

# """Test the `graph_helpers` module."""

import pytest
import pandas as pd
from stk_environment import stk_root
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_pie_chart

@pytest.mark.mpl_image_compare
def test_interval_pie_chart_leap_second(stk_root):
    start_times = ["30 Jun 2015 23:59:55.000", "30 Jun 2015 23:59:59.000"]
    stop_times = ["30 Jun 2015 23:59:56.000", "1 Jul 2015 00:00:00.000"]
    df = pd.DataFrame({'Start': start_times, 'Stop': stop_times})
    fig, _ = interval_pie_chart(stk_root, df, [], ["Start", "Stop"], "Start", "Stop", "30 Jun 2015 23:59:52.000", "1 Jul 2015 00:00:04.000", "", "Time")
    return fig

@pytest.mark.mpl_image_compare
def test_interval_pie_chart_cumulative_leap_second(stk_root):
    start_times = ["30 Jun 2015 23:59:55.000", "30 Jun 2015 23:59:59.000"]
    stop_times = ["30 Jun 2015 23:59:56.000", "1 Jul 2015 00:00:00.000"]
    df = pd.DataFrame({'Start': start_times, 'Stop': stop_times})
    fig, _ = interval_pie_chart(stk_root, df, [], ["Start", "Stop"], "Start", "Stop", "30 Jun 2015 23:59:52.000", "1 Jul 2015 00:00:04.000", "", "Time", cumulative=True)
    return fig

@pytest.mark.mpl_image_compare
def test_interval_pie_chart_gmt(stk_root):
    stk_root.units_preferences.set_current_unit("Date", "GMT")
    start_times = ["156/00000 2022", "156/00003 2022"]
    stop_times = ["156/00002 2022", "156/00004 2022"]
    df = pd.DataFrame({'Start': start_times, 'Stop': stop_times})
    fig, _ = interval_pie_chart(stk_root, df, [], ["Start", "Stop"], "Start", "Stop", "156/00000 2022", "156/00005 2022", "", "Time")
    return fig