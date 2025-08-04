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
import matplotlib
from stk_environment import stk_root
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_pie_chart, line_chart, interval_plot, polar_chart

@pytest.mark.mpl_image_compare
def test_interval_pie_chart_leap_second(stk_root):
    start_times = ["30 Jun 2015 23:59:55.000", "30 Jun 2015 23:59:59.000"]
    stop_times = ["30 Jun 2015 23:59:56.000", "1 Jul 2015 00:00:00.000"]
    df = pd.DataFrame({"Start": start_times, "Stop": stop_times})
    fig, _ = interval_pie_chart(stk_root, df, [], ["Start", "Stop"], "Start", "Stop", "30 Jun 2015 23:59:52.000", "1 Jul 2015 00:00:04.000", "", "Time")
    return fig

@pytest.mark.mpl_image_compare
def test_interval_pie_chart_cumulative_leap_second(stk_root):
    start_times = ["30 Jun 2015 23:59:55.000", "30 Jun 2015 23:59:59.000"]
    stop_times = ["30 Jun 2015 23:59:56.000", "1 Jul 2015 00:00:00.000"]
    df = pd.DataFrame({"Start": start_times, "Stop": stop_times})
    fig, _ = interval_pie_chart(stk_root, df, [], ["Start", "Stop"], "Start", "Stop", "30 Jun 2015 23:59:52.000", "1 Jul 2015 00:00:04.000", "", "Time", cumulative=True)
    return fig

@pytest.mark.mpl_image_compare
def test_interval_pie_chart_gmt(stk_root):
    stk_root.units_preferences.set_current_unit("Date", "GMT")
    start_times = ["156/00000 2022", "156/00003 2022"]
    stop_times = ["156/00002 2022", "156/00004 2022"]
    df = pd.DataFrame({"Start": start_times, "Stop": stop_times})
    fig, _ = interval_pie_chart(stk_root, df, [], ["Start", "Stop"], "Start", "Stop", "156/00000 2022", "156/00005 2022", "", "Time")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_leap_second(stk_root):
    times = ["30 Jun 2015 23:59:58.000", "30 Jun 2015 23:59:59.000", "30 Jun 2015 23:59:60.000", "1 Jul 2015 00:00:00.000", "1 Jul 2015 00:00:01.000"]
    values = [1, 2, 3, 4, 5]
    df = pd.DataFrame({"Time": times, "Value": values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Value", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_no_leap_second(stk_root):
    times = ["29 Jun 2015 23:59:57.000", "29 Jun 2015 23:59:58.000", "29 Jun 2015 23:59:59.000", "30 Jun 2015 00:00:00.000", "30 Jun 2015 00:00:01.000"]
    values = [1, 2, 3, 4, 5]
    df = pd.DataFrame({"Time": times, "Value": values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Value", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_interval_less_than_one_second(stk_root):
    times = ["1 Jan 2025 00:00:01.000", "1 Jan 2025 00:00:01.002", "1 Jan 2025 00:00:01.004", "1 Jan 2025 00:00:01.006", "1 Jan 2025 00:00:01.008"]
    values = [1, 2, 3, 4, 5]
    df = pd.DataFrame({"Time": times, "Value": values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Value", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_interval_less_than_two_days(stk_root):
    times = ["1 Jan 2025 00:00:00.000", "1 Jan 2025 12:00:00.000", "2 Jan 2025 00:00:00.000", "2 Jan 2025 12:00:00.000"]
    values = [1, 2, 3, 4]
    df = pd.DataFrame({"Time": times, "Value": values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Value", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_interval_less_than_sixty_days(stk_root):
    times = ["1 Jan 2025 00:00:00.000", "20 Jan 2025 00:00:00.000", "31 Jan 2025 00:00:00.000", "15 Feb 2025 00:00:00.000"]
    values = [1, 2, 3, 4]
    df = pd.DataFrame({"Time": times, "Value": values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Value", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_interval_over_sixty_days(stk_root):
    times = ["1 Jan 2025 00:00:00.000", "1 Mar 2025 00:00:00.000", "1 Jun 2025 00:00:00.000", "1 Oct 2025 00:00:00.000"]
    values = [1, 2, 3, 4]
    df = pd.DataFrame({"Time": times, "Value": values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Value", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_log10_axis(stk_root):
    x_values = [1, 2, 3, 4]
    y_values = [1, 10, 100, 1000]
    df = pd.DataFrame({"X": x_values, "Y": y_values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": True, "y2log10": False, "label": "", "lines": [
            {"y_name":"Y", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_log2_axis(stk_root):
    x_values = [1, 2, 3, 4]
    y_values = [1, 2, 4, 8]
    df = pd.DataFrame({"X": x_values, "Y": y_values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": True, "label": "", "lines": [
            {"y_name":"Y", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_two_lines_same_axis(stk_root):
    x_values = [1, 2, 3, 4]
    y_values1 = [1, 2, 3, 4]
    y_values2 = [10, 11, 12, 13]
    df = pd.DataFrame({"X": x_values, "Y1": y_values1, "Y2": y_values2})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Y1", "label":"Value1", "use_unit":None, "unit_squared": None, "dimension": None},
            {"y_name":"Y2", "label":"Value2", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y1", "Y2"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_two_lines_different_axes(stk_root):
    x_values = [1, 2, 3, 4]
    y_values1 = [1, 2, 3, 4]
    y_values2 = [10, 20, 21, 22]
    df = pd.DataFrame({"X": x_values, "Y1": y_values1, "Y2": y_values2})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "Axis1", "lines": [
            {"y_name":"Y1", "label":"Value1", "use_unit":None, "unit_squared": None, "dimension": None}]},
            {"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "Axis2", "lines": [
            {"y_name":"Y2", "label":"Value2", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y1", "Y2"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_with_unit_squared(stk_root):
    x_values = [1, 2, 3, 4]
    y_values1 = [1, 2, 3, 4]
    y_values2 = [10, 20, 21, 22]
    df = pd.DataFrame({"X": x_values, "Y1": y_values1, "Y2": y_values2})
    axes_info = [{"use_unit" : True, "unit_squared": True, "ylog10": False, "y2log10": False, "label": "Axis1", "lines": [
            {"y_name":"Y1", "label":"Value1", "use_unit":True, "unit_squared": True, "dimension": None}]},
            {"use_unit" : True, "unit_squared": False, "ylog10": False, "y2log10": False, "label": "Axis2", "lines": [
            {"y_name":"Y2", "label":"Value2", "use_unit":True, "unit_squared": False, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y1", "Y2"], [], axes_info, "X", "", "")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_pass_colormap(stk_root):
    x_values = [1, 2, 3, 4]
    y_values1 = [1, 2, 3, 4]
    y_values2 = [10, 11, 12, 13]
    y_values3 = [5, 6, 7, 13]
    df = pd.DataFrame({"X": x_values, "Y1": y_values1, "Y2": y_values2, "Y3": y_values3})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Y1", "label":"Value1", "use_unit":None, "unit_squared": None, "dimension": None},
            {"y_name":"Y2", "label":"Value2", "use_unit":None, "unit_squared": None, "dimension": None},
            {"y_name":"Y3", "label":"Value3", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["X", "Y1", "Y2"], [], axes_info, "X", "", "", colormap=matplotlib.cm.plasma)
    return fig

@pytest.mark.mpl_image_compare
def test_interval_chart(stk_root):
    start_times = ["1 Jan 2025 00:00:01.000", "1 Jan 2025 00:00:05.000", "1 Jan 2025 00:00:20.000"]
    stop_times = ["1 Jan 2025 00:00:03.000", "1 Jan 2025 00:00:10.000", "1 Jan 2025 00:00:22.000"]
    df = pd.DataFrame({"start time": start_times, "stop time": stop_times})
    elements=[(("start time", "None"),("stop time", "None"))]
    fig, _ = interval_plot([df], stk_root, elements, [], ["start time","stop time"], "Time", "")
    return fig

@pytest.mark.mpl_image_compare
def test_interval_chart_multiple_bars(stk_root):
    start_times1 = ["1 Jan 2025 00:00:01.000", "1 Jan 2025 00:00:05.000", "1 Jan 2025 00:00:20.000"]
    stop_times1 = ["1 Jan 2025 00:00:03.000", "1 Jan 2025 00:00:10.000", "1 Jan 2025 00:00:22.000"]
    start_times2 = ["1 Jan 2025 00:00:02.000", "1 Jan 2025 00:00:05.000", "1 Jan 2025 00:00:15.000", "1 Jan 2025 00:00:20.000"]
    stop_times2 = ["1 Jan 2025 00:00:04.000", "1 Jan 2025 00:00:11.000", "1 Jan 2025 00:00:17.000", "1 Jan 2025 00:00:27.000"]
    df1 = pd.DataFrame({"start time": start_times1, "stop time": stop_times1})
    df2 = pd.DataFrame({"start time": start_times2, "stop time": stop_times2})
    elements=[(("start time", "1"),("stop time", "1")), (("start time", "2"),("stop time", " "))]
    fig, _ = interval_plot([df1, df2], stk_root, elements, [], ["start time","stop time"], "Time", "")
    return fig

@pytest.mark.mpl_image_compare
def test_interval_chart_during_leap_second(stk_root):
    start_times = ["30 Jun 2015 23:59:56.000",  "30 Jun 2015 23:59:59.000", "1 Jul 2015 00:00:02.000"]
    stop_times = [ "30 Jun 2015 23:59:58.000", "1 Jul 2015 00:00:00.000", "1 Jul 2015 00:00:03.000"]
    df = pd.DataFrame({"start time": start_times, "stop time": stop_times})
    elements=[(("start time", "None"),("stop time", "None"))]
    fig, _ = interval_plot([df], stk_root, elements, [], ["start time","stop time"], "Time", "")
    return fig

@pytest.mark.mpl_image_compare
def test_interval_chart_multiple_bars_pass_colormap(stk_root):
    start_times1 = ["1 Jan 2025 00:00:01.000", "1 Jan 2025 00:00:05.000", "1 Jan 2025 00:00:20.000"]
    stop_times1 = ["1 Jan 2025 00:00:03.000", "1 Jan 2025 00:00:10.000", "1 Jan 2025 00:00:22.000"]
    start_times2 = ["1 Jan 2025 00:00:02.000", "1 Jan 2025 00:00:05.000", "1 Jan 2025 00:00:15.000", "1 Jan 2025 00:00:20.000"]
    stop_times2 = ["1 Jan 2025 00:00:04.000", "1 Jan 2025 00:00:11.000", "1 Jan 2025 00:00:17.000", "1 Jan 2025 00:00:27.000"]
    df1 = pd.DataFrame({"start time": start_times1, "stop time": stop_times1})
    df2 = pd.DataFrame({"start time": start_times2, "stop time": stop_times2})
    elements=[(("start time", "1"),("stop time", "1")), (("start time", "2"),("stop time", " "))]
    fig, _ = interval_plot([df1, df2], stk_root, elements, [], ["start time","stop time"], "Time", "", colormap=matplotlib.cm.plasma)
    return fig

@pytest.mark.mpl_image_compare
def test_polar_chart(stk_root):
    theta_values = [0, 90, 180, 270]
    r_values = [1, 2, 3, 4]
    df = pd.DataFrame({"Angle": theta_values, "Radius": r_values})
    axis={"use_unit" : False, "label": "Angle", "lines": [
        {"y_name":"Radius","x_name":"Angle", "label":"", "use_unit":False, "dimension": None}
        ]}
    fig, _ = polar_chart([df], stk_root, ["Angle","Radius"], axis, "", convert_negative_r = False, origin_0 = False)
    return fig

@pytest.mark.mpl_image_compare
def test_polar_chart_convert_negative_r(stk_root):
    theta_values = [0, 90, 180, 270]
    r_values = [-1, -2, -3, -4]
    df = pd.DataFrame({"Angle": theta_values, "Radius": r_values})
    axis={"use_unit" : False, "label": "Angle", "lines": [
        {"y_name":"Radius","x_name":"Angle", "label":"", "use_unit":False, "dimension": None}
        ]}
    fig, _ = polar_chart([df], stk_root, ["Angle","Radius"], axis, "", convert_negative_r = True, origin_0 = False)
    return fig

@pytest.mark.mpl_image_compare
def test_polar_chart_pass_colormap(stk_root):
    theta_values = [0, 90, 180, 270]
    r_values1 = [1, 2, 3, 4]
    r_values2 = [2, 4, 6, 8]
    df1 = pd.DataFrame({"Angle": theta_values, "Radius": r_values1})
    df2 = pd.DataFrame({"Angle": theta_values, "Radius": r_values2})
    axis={"use_unit" : False, "label": "Angle", "lines": [
        {"y_name":"Radius","x_name":"Angle", "label":"", "use_unit":False, "dimension": None}
        ]}
    fig, _ = polar_chart([df1, df2], stk_root, ["Angle","Radius"], axis, "", convert_negative_r = False, origin_0 = False, colormap=matplotlib.cm.plasma)
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_EarthEpTU_unit(stk_root):
    times = ["1 Jan 2025 00:00:00.000", "1 Jan 2025 12:00:00.000", "2 Jan 2025 00:00:00.000", "2 Jan 2025 12:00:00.000"]
    values = [1, 2, 3, 4]
    df = pd.DataFrame({"Time": times, "Value": values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Value", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "", time_unit_abbreviation="EarthEpTU")
    return fig

@pytest.mark.mpl_image_compare
def test_interval_chart_SunEpTU_unit(stk_root):
    start_times = ["1 Jan 2025 00:00:00.000", "2 Jan 2025 12:00:00.000", "3 Jan 2025 12:00:00.000"]
    stop_times = ["2 Jan 2025 00:00:00.000", "3 Jan 2025 00:00:00.000", "4 Jan 2025 00:00:00.000"]
    df = pd.DataFrame({"start time": start_times, "stop time": stop_times})
    elements=[(("start time", "None"),("stop time", "None"))]
    fig, _ = interval_plot([df], stk_root, elements, [], ["start time","stop time"], "Time", "", time_unit_abbreviation="SunEpTU")
    return fig

@pytest.mark.mpl_image_compare
def test_line_chart_custom_formatter(stk_root):
    times = ["1 Jan 2025 00:00:00.000", "1 Jan 2025 12:00:00.000", "2 Jan 2025 00:00:00.000", "2 Jan 2025 12:00:00.000"]
    values = [1, 2, 3, 4]
    df = pd.DataFrame({"Time": times, "Value": values})
    axes_info = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "", "lines": [
            {"y_name":"Value", "label":"Value", "use_unit":None, "unit_squared": None, "dimension": None}]}]
    def custom_formatter(x : float, pos: float):
        return "Const. Format"
    fig, _ = line_chart([df], stk_root, ["Value"], ["Time"], axes_info, "Time", "", "", formatter=custom_formatter)
    return fig