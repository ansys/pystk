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

"""Provides graphs for Access objects."""

import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import Access
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import (
    _get_access_data,
    interval_pie_chart,
    interval_plot,
    line_chart,
    pie_chart,
    polar_chart,
)


def access_duration_pie_chart(
    stk_object: Access, start_time: typing.Any = None, stop_time: typing.Any = None, colormap: matplotlib.colors.Colormap = None
) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create pie chart of the durations of the access intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Access Duration.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item("Access Data").execute_elements(start_time, stop_time, ["Access Number", "Duration"]).data_sets.to_pandas_dataframe()
    return pie_chart(root, df, ["duration"], [], "duration", "Access Duration", "Time", "access number", colormap = colormap)


def cumulative_dwell_cumulative_pie_chart(
    stk_object: Access, start_time: typing.Any = None, stop_time: typing.Any = None, color_list: list[typing.Any] = None
) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create graph showing access interval durations as a cumulative pie chart.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Cumulative Dwell.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation.
    stop_time : typing.Any
        The stop time of the calculation.
    color_list : list of typing.Any
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item("Access Data").execute_elements(start_time, stop_time, ["Access Number", "Start Time", "Stop Time", "Duration"]).data_sets.to_pandas_dataframe()
    return interval_pie_chart(
        root,
        df,
        ["duration"],
        ["start time", "stop time"],
        "start time",
        "stop time",
        start_time,
        stop_time,
        "Cumulative Dwell",
        "Time",
        True,
        color_list = color_list
    )


def revisit_diagram_interval_pie_chart(
    stk_object: Access, start_time: typing.Any = None, stop_time: typing.Any = None, color_list: list[typing.Any] = None
) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create pie chart showing the durations of access intervals and access gap intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Revisit Diagram.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation.
    stop_time : typing.Any
        The stop time of the calculation.
    color_list : list of typing.Any
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item("Access Data").execute_elements(start_time, stop_time, ["Access Number", "Start Time", "Stop Time", "Duration"]).data_sets.to_pandas_dataframe()
    return interval_pie_chart(
        root,
        df,
        ["duration"],
        ["start time", "stop time"],
        "start time",
        "stop time",
        start_time,
        stop_time,
        "Revisit Diagram",
        "Time",
        color_list = color_list
    )

def aer_line_chart(stk_object :Access, start_time: typing.Any = None, stop_time: typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = "UTCG", formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the azimuth, elevation, and range values for the relative position vector between the base object and the target object, during access intervals.

    The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\AER.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation.
    stop_time : typing.Any
        The stop time of the calculation.
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, "AER Data", True, "Default", ["Azimuth", "Elevation", "Range", "Time"], start_time, stop_time, step)

    axes = [{"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "Longitude/Angle", "lines": [
            {"y_name":"azimuth", "label":"Azimuth", "use_unit":None, "unit_squared": None, "dimension": "Longitude"},
            {"y_name":"elevation", "label":"Elevation", "use_unit":None, "unit_squared": None, "dimension": "Angle"}]},
            {"use_unit" : None, "unit_squared": None, "ylog10": False, "y2log10": False, "label": "Distance", "lines": [
            {"y_name":"range", "label":"Range", "use_unit":None, "unit_squared": None, "dimension": "Distance"}]}]
    return line_chart(data, root, ["azimuth","elevation","range"], ["time"], axes, "time", "Time", "AER", colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def access_interval_graph(stk_object :Access, start_time: typing.Any = None, stop_time: typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = "UTCG", formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the access intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Access.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation.
    stop_time : typing.Any
        The stop time of the calculation.
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item("Access Data").execute_elements(start_time, stop_time, ["Start Time", "Stop Time"]).data_sets.to_pandas_dataframe()
    elements=[(("start time", "None"),("stop time", "None"))]
    return interval_plot([df], root, elements, [], ["start time","stop time"], "Time", "Access Times", colormap=colormap, time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def az_el_polar_center_90_graph(stk_object :Access, start_time : typing.Any = None, stop_time : typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a polar plot with elevation as radius and azimuth as angle theta over time, during access intervals.

    The azimuth and elevation describe the relative position vector between the base object and the target object. The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Az El Polar.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation.
    stop_time : typing.Any
        The stop time of the calculation.
    step_time : float
        The step time for the calculation (the default is 60 seconds).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_object.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    data = _get_access_data(stk_object, "AER Data", True, "Default", ["Azimuth", "Elevation"], start_time, stop_time, step)
    axis={"use_unit" : True, "unit_squared": False, "label": "Angle", "lines": [
        {"y_name":"elevation","x_name":"azimuth", "label":"Azimuth", "use_unit":True, "unit_squared": False, "dimension": "Angle"}
        ]}
    return polar_chart(data, root, ["elevation","azimuth"], axis, "Az El Polar", convert_negative_r = False, origin_0 = True, colormap=colormap)