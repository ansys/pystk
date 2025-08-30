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

"""Provides graphs for Ship objects."""
import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import Ship
from ansys.stk.extensions.data_analysis.graphs._common_graphs import (
    _cumulative_sunlight_cumulative_pie_chart,
    _eclipse_times_interval_graph,
    _lat_lon_position_line_chart,
    _lighting_times_interval_graph,
    _lla_position_line_chart,
    _model_area_line_chart,
    _solar_aer_line_chart_vehicle,
    _solar_az_el_polar_center_0_graph_vehicle,
    _sun_vector_ecf_line_chart,
    _sunlight_intervals_interval_pie_chart,
)


def cumulative_sunlight_cumulative_pie_chart(stk_object :Ship, start_time: typing.Any = None, stop_time : typing.Any = None, color_list: list[typing.Any] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a pie chart showing the total duration of full sunlight within the graph's requested time interval.

    Gaps in the chart indicate the total duration of penumbra and umbra durations.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Cumulative Sunlight.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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

def eclipse_times_interval_graph(stk_object :Ship, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the penumbra (partial lighting) and umbra (zero lighting) intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Eclipse Times.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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

def lat_lon_position_line_chart(stk_object :Ship, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Plot the latitude and longitude of the location of the object, computed with respect to the object's central body shape, as a function of time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Lat-Lon Position.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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
    return _lat_lon_position_line_chart(stk_object, start_time, stop_time, step, colormap, time_unit_abbreviation, formatter)

def lighting_times_interval_graph(stk_object :Ship, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the sunlight (full lighting) intervals, penumbra (partial lighting) intervals and umbra (zero lighting) intervals.

    Each lighting condition's intervals are plotted on separate lines.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Lighting Times.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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

def lla_position_line_chart(stk_object :Ship, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Plot the position of the object, expressed in LLA elements, as a function of time.

    The coordinate system is the Fixed frame of the object's central body.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\LLA Position.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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
    return _lla_position_line_chart(stk_object, start_time, stop_time, step, colormap, time_unit_abbreviation, formatter)

def model_area_line_chart(stk_object :Ship, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the area of the object's 3D graphics model over time, as viewed from a given view direction, as computed by the Area Tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Model Area.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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

def solar_aer_line_chart(stk_object :Ship, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the azimuth, elevation, and range over time, describing the apparent relative position vector of the Sun with respect to Fixed VVLH axes (ECFVVLH).

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Solar AER.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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
    return _solar_aer_line_chart_vehicle(stk_object, start_time, stop_time, step, colormap, time_unit_abbreviation, formatter)

def solar_az_el_polar_center_0_graph(stk_object :Ship, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to Fixed VVLH axes (ECFVVLH).

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Solar Az-El.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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
    return _solar_az_el_polar_center_0_graph_vehicle(stk_object, start_time, stop_time, step, colormap)

def sun_vector_ecf_line_chart(stk_object :Ship, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the apparent relative position of the Sun to the object, expressed in Cartesian components, using the object's central body's Fixed coordinate system, as a function of time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Sun Vector ECF.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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
    return _sun_vector_ecf_line_chart(stk_object, start_time, stop_time, step, colormap, time_unit_abbreviation, formatter)

def sunlight_intervals_interval_pie_chart(stk_object :Ship, start_time: typing.Any = None, stop_time : typing.Any = None, color_list: list[typing.Any] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a Pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Sunlight Intervals.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Ship
        The STK Ship object.
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

