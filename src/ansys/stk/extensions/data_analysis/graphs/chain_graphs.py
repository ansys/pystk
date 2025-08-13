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

"""Provides graphs for Chain objects."""
import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import Chain
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_plot, line_chart


def angle_between_line_chart(stk_object :Chain, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the angle and ranges for each three object sub-strand of a Chain, as a function of time, for each strand access interval that overlaps with the requested report time intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Chain\\Angle Between.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Chain
        The STK Chain object.
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
    df = stk_object.data_providers.item('Angle Between').group.item("Granularity Determined").execute_elements(start_time, stop_time, step, ['Time', 'Range 1', 'Range 2', 'Angle']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'angle', 'label':'Angle', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Distance', 'lines': [
            {'y_name':'range 1', 'label':'Range 1', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'},
            {'y_name':'range 2', 'label':'Range 2', 'use_unit':True, 'unit_squared': None, 'dimension': 'Distance'}]}]
    return line_chart([df], root, ['angle','range 1','range 2'], ['time'], axes, 'time', 'Time', 'Angle Between Data', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def bentpipe_link_cno_line_chart(stk_object :Chain, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the carrier-to-noise density ratio for uplink, downlink, and composite link as a function of time for a bent pipe communications system.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Chain\\BentPipe Link - CNo.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Chain
        The STK Chain object.
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
    df = stk_object.data_providers.item('Link Information').execute_elements(start_time, stop_time, step, ['Time', 'C/No1', 'C/No Tot.2']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Spectral Density', 'lines': [
            {'y_name':'c/no1', 'label':'C/No1', 'use_unit':True, 'unit_squared': None, 'dimension': 'SpectralDensity'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Spectral Density', 'lines': [
            {'y_name':'c/no tot.2', 'label':'C/No Tot.2', 'use_unit':True, 'unit_squared': None, 'dimension': 'SpectralDensity'}]}]
    return line_chart([df], root, ['c/no1','c/no tot.2'], ['time'], axes, 'time', 'Time', 'Bent Pipe C/No Link Analysis', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def complete_chain_access_interval_graph(stk_object :Chain, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval plot of the time intervals for which the chain is completed.

    These intervals are computed by overlapping all the strand accesses.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Chain\\Complete Chain Access.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Chain
        The STK Chain object.
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
    df = stk_object.data_providers.item('Complete Access').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], root, elements, [], ['start time','stop time'], 'Time', 'Complete Chain Access Times', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def individual_object_access_interval_graph(stk_object :Chain, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the time intervals for each object in a Chain for which the object participates in a strand that completes the chain.

    Each object's intervals are graphed on a separate line.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Chain\\Individual Object Access.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Chain
        The STK Chain object.
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
    df = stk_object.data_providers.item('Object Access').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], root, elements, [], ['start time','stop time'], 'Time', 'Object Access', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def individual_strand_access_interval_graph(stk_object :Chain, start_time: typing.Any = None, stop_time : typing.Any = None, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create an interval graph of the time intervals for each strand in a Chain that completes the chain.

    Each strand's intervals are graphed on a separate line.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Chain\\Individual Strand Access.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Chain
        The STK Chain object.
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
    df = stk_object.data_providers.item('Strand Access').execute_elements(start_time, stop_time, ['Start Time', 'Stop Time']).data_sets.to_pandas_dataframe()
    elements=[(('start time', 'None'),('stop time', 'None'))]
    return interval_plot([df], root, elements, [], ['start time','stop time'], 'Time', 'Strand Access Times', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def number_of_accesses_line_chart(stk_object :Chain, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the number of objects participating in a strand that completes the chain at the given time, as a function of time.

    The report is only valid for Chains consisting of two objects.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Chain\\Number Of Accesses.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Chain
        The STK Chain object.
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
    df = stk_object.data_providers.item('Base Object Data').execute_elements(start_time, stop_time, step, ['Time', 'Number Of Accesses']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Value', 'lines': [
            {'y_name':'number of accesses', 'label':'Number Of Accesses', 'use_unit':False, 'unit_squared': None, 'dimension': 'None'}]}]
    return line_chart([df], root, ['number of accesses'], ['time'], axes, 'time', 'Time', 'Number Of Accesses', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

