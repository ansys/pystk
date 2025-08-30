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
"""Provides graphs for Place objects."""
import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import Place
from ansys.stk.extensions.data_analysis.graphs._common_graphs import (
    _cumulative_sunlight_cumulative_pie_chart,
    _eclipse_times_interval_graph,
    _lighting_times_interval_graph,
    _model_area_line_chart,
    _solar_aer_line_chart_stationary,
    _solar_az_el_polar_center_0_graph_stationary,
    _sunlight_intervals_interval_pie_chart,
)


def cumulative_sunlight_cumulative_pie_chart(stk_object :Place, start_time: typing.Any = None, stop_time : typing.Any = None, color_list: list[typing.Any] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a pie chart showing the total duration of full sunlight within the graph's requested time interval.

    Gaps in the chart indicate the total duration of penumbra and umbra durations.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Place\\Cumulative Sunlight.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Place
        The STK Place object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    color_list : list of typing.Any
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    return _cumulative_sunlight_cumulative_pie_chart(stk_object, start_time, stop_time, color_list)

def eclipse_times_interval_graph(stk_object :Place, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the penumbra (partial lighting) and umbra (zero lighting) intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Place\\Eclipse Times.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Place
        The STK Place object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
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
    return _eclipse_times_interval_graph(stk_object, start_time, stop_time, colormap, time_unit_abbreviation, formatter)

def lighting_times_interval_graph(stk_object :Place, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the sunlight (full lighting) intervals, penumbra (partial lighting) intervals and umbra (zero lighting) intervals.

    Each lighting condition's intervals are plotted on separate lines.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Place\\Lighting Times.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Place
        The STK Place object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
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
    return _lighting_times_interval_graph(stk_object, start_time, stop_time, colormap, time_unit_abbreviation, formatter)

def model_area_line_chart(stk_object :Place, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the area of the object's 3D graphics model over time, as viewed from a given view direction, as computed by the Area Tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Place\\Model Area.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Place
        The STK Place object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
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
    return _model_area_line_chart(stk_object, start_time, stop_time, step, colormap, time_unit_abbreviation, formatter)

def solar_aer_line_chart(stk_object :Place, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the azimuth, elevation, and range over time, describing the apparent relative position vector of the Sun with respect to the local horizontal plane.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Place\\Solar AER.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Place
        The STK Place object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
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
    return _solar_aer_line_chart_stationary(stk_object, start_time, stop_time, step, colormap, time_unit_abbreviation, formatter)

def solar_az_el_polar_center_0_graph(stk_object :Place, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to the local horizontal plane.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Place\\Solar Az-El.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Place
        The STK Place object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    step_time : float
        The step time for the calculation (the default is 60 seconds).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the data (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    return _solar_az_el_polar_center_0_graph_stationary(stk_object, start_time, stop_time, step, colormap)

def sunlight_intervals_interval_pie_chart(stk_object :Place, start_time: typing.Any = None, stop_time : typing.Any = None, color_list: list[typing.Any] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Place\\Sunlight Intervals.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Place
        The STK Place object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).
    color_list : list of typing.Any
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    return _sunlight_intervals_interval_pie_chart(stk_object, start_time, stop_time, color_list)

