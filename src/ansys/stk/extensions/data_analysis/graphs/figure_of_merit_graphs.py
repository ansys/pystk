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

"""Provides graphs for FigureOfMerit objects."""
import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import FigureOfMerit
from ansys.stk.extensions.data_analysis.graphs._common_graphs import (
    _grid_stats_over_time_line_chart,
    _value_by_latitude_xy_graph,
    _value_by_longitude_xy_graph,
)
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_plot, line_chart


def gi_all_dop_line_chart(stk_object :FigureOfMerit, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of all DOP values, over time, for the point currently selected via the figure of merit grid inspector.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\GI All DOP.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Selected Point All DOPs').execute_elements(start_time, stop_time, step, ['VDOP', 'Time', 'TDOP', 'PDOP', 'GDOP', 'EDOP', 'HDOP', 'NDOP']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'gdop', 'label':'GDOP', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'},
            {'y_name':'pdop', 'label':'PDOP', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'},
            {'y_name':'hdop', 'label':'HDOP', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'},
            {'y_name':'vdop', 'label':'VDOP', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'},
            {'y_name':'edop', 'label':'EDOP', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'},
            {'y_name':'ndop', 'label':'NDOP', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'},
            {'y_name':'tdop', 'label':'TDOP', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart([df], root, ['gdop','pdop','hdop','vdop','edop','ndop','tdop'], ['time'], axes, 'time', 'Time', 'All Dilutions of Precision', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gi_point_fom_line_chart(stk_object :FigureOfMerit, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the figure of merit values over time, for the point currently selected via the figure of merit grid inspector.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\GI Point FOM.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Selected Point FOM').execute_elements(start_time, stop_time, step, ['Time', 'FOM Value']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'fom value', 'label':'FOM Value', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart([df], root, ['fom value'], ['time'], axes, 'time', 'Time', 'Point FOM Value', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gi_point_satisfaction_interval_graph(stk_object :FigureOfMerit, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the satisfaction intervals for the point currently selected via the figure of merit grid inspector.

    Satisfaction intervals are defined as periods when a grid point achieves the defined satisfaction criteria associated with the FOM.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\GI Point Satisfaction.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Selected Point Satisfaction').execute_elements(start_time, stop_time, ['Interval Start', 'Interval End']).data_sets.to_pandas_dataframe()
    elements=[(('interval start', 'None'),('interval end', 'None'))]
    return interval_plot([df], root, elements, [], ['interval start','interval end'], 'Time', 'Point Satisfaction Intervals', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gi_region_fom_line_chart(stk_object :FigureOfMerit, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the minimum, maximum, and average figure of merit value, sampled over all grid points within the region currently selected in the figure of merit grid inspector, over time.

    Grid points for which a value cannot be computed are not included in the reported statistics.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\GI Region FOM.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Selected Region FOM').execute_elements(start_time, stop_time, step, ['Time', 'Minimum', 'Maximum', 'Average']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'minimum', 'label':'Minimum', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'},
            {'y_name':'maximum', 'label':'Maximum', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'},
            {'y_name':'average', 'label':'Average', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart([df], root, ['minimum','maximum','average'], ['time'], axes, 'time', 'Time', 'Regional FOM Values', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gi_region_satisfaction_interval_graph(stk_object :FigureOfMerit, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the intervals of time when the region selected by the grid inspector is partially covered.

    A region is considered to be covered if at least one point within the region has access to one or more of the assigned assets.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\GI Region Satisfaction.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Selected Region Partial Satisfaction').execute_elements(start_time, stop_time, ['Interval Start', 'Interval End']).data_sets.to_pandas_dataframe()
    elements=[(('interval start', 'None'),('interval end', 'None'))]
    return interval_plot([df], root, elements, [], ['interval start','interval end'], 'Time', 'Periods of Partial Regional Satisfaction', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def grid_stats_over_time_line_chart(stk_object :FigureOfMerit, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the minimum, maximum, and average figure of merit values, sampled over all grid points, over time.

    Grid points for which a value cannot be computed are not included in the reported statistics.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\Grid Stats Over Time.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    return _grid_stats_over_time_line_chart(stk_object, start_time, stop_time, step, colormap, time_unit_abbreviation, formatter)

def satisfied_by_time_line_chart(stk_object :FigureOfMerit, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the percentage of the grid which satisfies the satisfaction criteria defined in the figure of merit, as a function of time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\Satisfied By Time.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    root = stk_object.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_object.data_providers.item('Satisfied by Time').execute_elements(start_time, stop_time, step, ['Time', 'Percent Satisfied']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percent satisfied', 'label':'% Satisfied', 'use_unit':False, 'unit_squared': None, 'dimension': 'Percent'}]}]
    return line_chart([df], root, ['percent satisfied'], ['time'], axes, 'time', 'Time', 'Satisfied By Time', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def value_by_latitude_line_chart(stk_object : FigureOfMerit, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the minimum, maximum, and average figure of merit value, sampled over all grid points at the same latitude, as a function of latitude.

    Statistics are generated by sampling values from all grid points with latitude values within one half degree of the reported latitude value. Values are computed for every one degree of latitude. For example, statistics reported for the latitude value of 30 degrees will represent figure of merit values for all points with latitudes between 29.5 and 30.5 degrees. Grid points for which a value cannot be computed are not included in the reported statistics. Latitudes which do not have any reported grid points within one half degree are not included in the reported values.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\Value By Latitude.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    return _value_by_latitude_xy_graph(stk_object, colormap, time_unit_abbreviation, formatter)

def value_by_longitude_line_chart(stk_object : FigureOfMerit, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the minimum, maximum, and average figure of merit value, sampled over all grid points at the same longitude, as a function of longitude.

    Statistics are generated by sampling values from all grid points with longitude values within one half degree of the reported longitude value. Values are computed for every one degree of longitude. For example, statistics reported for the longitude value of 30 degrees will represent figure of merit values for all points with longitudes between 29.5 and 30.5 degrees. Grid points for which a value cannot be computed are not included in the reported statistics. Longitudes which do not have any reported grid points within one half degree are not included in the reported values.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\Value By Longitude.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.FigureOfMerit
        The STK FigureOfMerit object.
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
    return _value_by_longitude_xy_graph(stk_object, colormap, time_unit_abbreviation, formatter)

