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
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_pie_chart, line_chart

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

@pytest.mark.mpl_image_compare
def test_line_chart_leap_second(stk_root):
    times = ["30 Jun 2015 23:59:58.000", "30 Jun 2015 23:59:59.000", "30 Jun 2015 23:59:60.000", "1 Jul 2015 00:00:00.000", "1 Jul 2015 00:00:01.000"]
    values = [1, 2, 3, 4, 5]
    df = pd.DataFrame({'Time': times, 'Value': values})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': '', 'lines': [
            {'y_name':'Value', 'label':'Value', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_no_leap_second(stk_root):
    times = ["29 Jun 2015 23:59:57.000", "29 Jun 2015 23:59:58.000", "29 Jun 2015 23:59:59.000", "30 Jun 2015 00:00:00.000", "30 Jun 2015 00:00:01.000"]
    values = [1, 2, 3, 4, 5]
    df = pd.DataFrame({'Time': times, 'Value': values})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': '', 'lines': [
            {'y_name':'Value', 'label':'Value', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_interval_less_than_one_second(stk_root):
    times = ["1 Jan 2025 00:00:01.000", "1 Jan 2025 00:00:01.002", "1 Jan 2025 00:00:01.004", "1 Jan 2025 00:00:01.006", "1 Jan 2025 00:00:01.008"]
    values = [1, 2, 3, 4, 5]
    df = pd.DataFrame({'Time': times, 'Value': values})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': '', 'lines': [
            {'y_name':'Value', 'label':'Value', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_interval_less_than_two_days(stk_root):
    times = ["1 Jan 2025 00:00:00.000", "1 Jan 2025 12:00:00.000", "2 Jan 2025 00:00:00.000", "2 Jan 2025 12:00:00.000"]
    values = [1, 2, 3, 4]
    df = pd.DataFrame({'Time': times, 'Value': values})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': '', 'lines': [
            {'y_name':'Value', 'label':'Value', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_interval_less_than_sixty_days(stk_root):
    times = ["1 Jan 2025 00:00:00.000", "20 Jan 2025 00:00:00.000", "31 Jan 2025 00:00:00.000", "15 Feb 2025 00:00:00.000"]
    values = [1, 2, 3, 4]
    df = pd.DataFrame({'Time': times, 'Value': values})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': '', 'lines': [
            {'y_name':'Value', 'label':'Value', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_interval_over_sixty_days(stk_root):
    times = ["1 Jan 2025 00:00:00.000", "1 Mar 2025 00:00:00.000", "1 Jun 2025 00:00:00.000", "1 Oct 2025 00:00:00.000"]
    values = [1, 2, 3, 4]
    df = pd.DataFrame({'Time': times, 'Value': values})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': '', 'lines': [
            {'y_name':'Value', 'label':'Value', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_log10_axis(stk_root):
    x_values = [1, 2, 3, 4]
    y_values = [1, 10, 100, 1000]
    df = pd.DataFrame({'X': x_values, 'Y': y_values})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': True, 'y2log10': False, 'label': '', 'lines': [
            {'y_name':'Y', 'label':'Value', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_log2_axis(stk_root):
    x_values = [1, 2, 3, 4]
    y_values = [1, 2, 4, 8]
    df = pd.DataFrame({'X': x_values, 'Y': y_values})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': True, 'label': '', 'lines': [
            {'y_name':'Y', 'label':'Value', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_two_lines_same_axis(stk_root):
    x_values = [1, 2, 3, 4]
    y_values1 = [1, 2, 3, 4]
    y_values2 = [10, 11, 12, 13]
    df = pd.DataFrame({'X': x_values, 'Y1': y_values1, 'Y2': y_values2})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': '', 'lines': [
            {'y_name':'Y1', 'label':'Value1', 'use_unit':None, 'unit_squared': None, 'dimension': None},
            {'y_name':'Y2', 'label':'Value2', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y1", "Y2"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_two_lines_different_axes(stk_root):
    x_values = [1, 2, 3, 4]
    y_values1 = [1, 2, 3, 4]
    y_values2 = [10, 20, 21, 22]
    df = pd.DataFrame({'X': x_values, 'Y1': y_values1, 'Y2': y_values2})
    axes_info = [{'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Axis1', 'lines': [
            {'y_name':'Y1', 'label':'Value1', 'use_unit':None, 'unit_squared': None, 'dimension': None}]},
            {'use_unit' : None, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Axis2', 'lines': [
            {'y_name':'Y2', 'label':'Value2', 'use_unit':None, 'unit_squared': None, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y1", "Y2"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_with_unit_squared(stk_root):
    x_values = [1, 2, 3, 4]
    y_values1 = [1, 2, 3, 4]
    y_values2 = [10, 20, 21, 22]
    df = pd.DataFrame({'X': x_values, 'Y1': y_values1, 'Y2': y_values2})
    axes_info = [{'use_unit' : True, 'unit_squared': True, 'ylog10': False, 'y2log10': False, 'label': 'Axis1', 'lines': [
            {'y_name':'Y1', 'label':'Value1', 'use_unit':True, 'unit_squared': True, 'dimension': None}]},
            {'use_unit' : True, 'unit_squared': False, 'ylog10': False, 'y2log10': False, 'label': 'Axis2', 'lines': [
            {'y_name':'Y2', 'label':'Value2', 'use_unit':True, 'unit_squared': False, 'dimension': None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y1", "Y2"], [], axes_info, "X", "", "")
    return fig