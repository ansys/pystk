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

"""Provides graphs for CoverageDefinition objects."""
import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import CoverageDefinition
from ansys.stk.extensions.data_analysis.graphs._common_graphs import (
    _coverage_by_latitude_xy_graph,
    _gap_duration_xy_graph,
)
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_plot, line_chart


def coverage_by_latitude_line_chart(stk_object : CoverageDefinition, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the percent time covered vs latitude.

    A point is considered to be covered if it has access to one or more of the assigned assets. The reported values for each latitude are the average value for all grid points at that latitude.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\Coverage By Latitude.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CoverageDefinition
        The STK CoverageDefinition object.
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
    return _coverage_by_latitude_xy_graph(stk_object, colormap, time_unit_abbreviation, formatter)

def gap_duration_line_chart(stk_object : CoverageDefinition, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the cumulative distribution of the access duration gaps of all grid points.

    For each grid point, access intervals to each assigned asset are combined to determine the time intervals over which at least one asset has access to the grid point. The durations of the gaps between these intervals, for all grid points, are then sorted from smallest to largest and the percentages are then plotted.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\Gap Duration.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CoverageDefinition
        The STK CoverageDefinition object.
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
    return _gap_duration_xy_graph(stk_object, colormap, time_unit_abbreviation, formatter)

def gi_point_coverage_interval_graph(stk_object :CoverageDefinition, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the access intervals for the point currently selected by the grid inspector.

    The intervals represent the union of times that the grid point has access to any of the assets.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\GI Point Coverage.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CoverageDefinition
        The STK CoverageDefinition object.
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
    df = stk_object.data_providers.item('Selected Point Coverage').execute_elements(start_time, stop_time, ['Access Start', 'Access End']).data_sets.to_pandas_dataframe()
    elements=[(('access start', 'None'),('access end', 'None'))]
    return interval_plot([df], root, elements, [], ['access start','access end'], 'Time', 'Point Coverage Intervals', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gi_point_prob_of_coverage_line_chart(stk_object : CoverageDefinition, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the probability of coverage being achieved for the point selected in the grid inspector, as a function of the time past a request for coverage.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\GI Point Prob Of Coverage.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CoverageDefinition
        The STK CoverageDefinition object.
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
    df = stk_object.data_providers.item('Selected Point Probability of Coverage').execute_elements(['Time From Request', 'Probability of Collection']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'probability of collection', 'label':'Probability of Collection', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart([df], root, ['probability of collection', 'time from request'], [], axes, 'time from request','Time From Request', 'Probability of Coverage', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gi_region_coverage_line_chart(stk_object :CoverageDefinition, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the percentage of coverage over time of the region selected by the grid inspector.

    A region is considered to be covered if at least one point within the region has access to one or more of the assigned assets.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\GI Region Coverage.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CoverageDefinition
        The STK CoverageDefinition object.
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
    df = stk_object.data_providers.item('Selected Region Coverage').execute_elements(start_time, stop_time, step, ['Time', 'Percent Coverage']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percent coverage', 'label':'% Coverage', 'use_unit':False, 'unit_squared': None, 'dimension': 'Percent'}]}]
    return line_chart([df], root, ['percent coverage'], ['time'], axes, 'time', 'Time', 'Percentage of Region Covered', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gi_region_full_coverage_interval_graph(stk_object :CoverageDefinition, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the intervals of time when the region selected by the grid inspector is completely covered.

    The region is considered to be completely covered when all points within the region are covered. A point is covered when it has access to some asset.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\GI Region Full Coverage.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CoverageDefinition
        The STK CoverageDefinition object.
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
    df = stk_object.data_providers.item('Selected Region Full Coverage').execute_elements(start_time, stop_time, ['Coverage Start', 'Coverage End']).data_sets.to_pandas_dataframe()
    elements=[(('coverage start', 'None'),('coverage end', 'None'))]
    return interval_plot([df], root, elements, [], ['coverage start','coverage end'], 'Time', 'Intervals of Full Regional Coverage', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def gi_region_time_to_cover_line_chart(stk_object :CoverageDefinition, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the amount of wait time required, starting from the reported time, before complete coverage of the region selected in the grid inspector occurs.

    The average wait time, compute as the mean of samples, is also plotted. A region is considered to be completely covered if all points within the region have had access to at least one of the assigned assets.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\GI Region Time to Cover.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CoverageDefinition
        The STK CoverageDefinition object.
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
    df = stk_object.data_providers.item('Selected Region Time To Cover').execute_elements(start_time, stop_time, step, ['Wait for Total Cov', 'Time', 'Average Sampled Wait']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Time', 'lines': [
            {'y_name':'wait for total cov', 'label':'Wait for Total Cov', 'use_unit':True, 'unit_squared': None, 'dimension': 'Time'},
            {'y_name':'average sampled wait', 'label':'Average Sampled Wait', 'use_unit':True, 'unit_squared': None, 'dimension': 'Time'}]}]
    return line_chart([df], root, ['wait for total cov','average sampled wait'], ['time'], axes, 'time', 'Time', 'GI Region Time to Cover', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def percent_coverage_line_chart(stk_object :CoverageDefinition, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the percentage of the area of the total coverage grid which is covered at the reported time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\Percent Coverage.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CoverageDefinition
        The STK CoverageDefinition object.
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
    df = stk_object.data_providers.item('Percent Coverage').execute_elements(start_time, stop_time, step, ['Percent Accum Coverage', 'Time', 'Percent Coverage']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percent coverage', 'label':'% Coverage', 'use_unit':False, 'unit_squared': None, 'dimension': 'Percent'},
            {'y_name':'percent accum coverage', 'label':'% Accum Coverage', 'use_unit':False, 'unit_squared': None, 'dimension': 'Percent'}]}]
    return line_chart([df], root, ['percent coverage','percent accum coverage'], ['time'], axes, 'time', 'Time', 'Current and Accumulated Coverage', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

