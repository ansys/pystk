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

"""Provides graphs for Scenario objects."""
import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import Scenario
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import line_chart


def greenwich_hour_angle_line_chart(stk_object :Scenario, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the Mean Greenwich Hour angle (Mean GHA) over time.

    Mean GHA is sidereal Greenwich Hour Angle (GHA) that does not include equation of the equinox.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Scenario\\Greenwich Hour Angle.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Scenario
        The STK Scenario object.
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
    df = stk_object.data_providers.item('J2000 Angles').execute_elements(start_time, stop_time, step, ['Mean GHA', 'Time']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'mean gha', 'label':'Mean GHA', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['mean gha'], ['time'], axes, 'time', 'Time', 'Greenwich Hour Angle', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def polewanderx_line_chart(stk_object :Scenario, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the X component of pole wander over time.

    Pole wander describes the unmodeled part of the Earth's pole location.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Scenario\\PoleWanderX.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Scenario
        The STK Scenario object.
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
    df = stk_object.data_providers.item('J2000 Angles').execute_elements(start_time, stop_time, step, ['Pole Wander X', 'Time']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Angle', 'lines': [
            {'y_name':'pole wander x', 'label':'Pole Wander X', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['pole wander x'], ['time'], axes, 'time', 'Time', 'PoleWanderX', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def polewandery_line_chart(stk_object :Scenario, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the Y component of pole wander over time.

    Pole wander describes the unmodeled part of the Earth's pole location.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Scenario\\PoleWanderY.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Scenario
        The STK Scenario object.
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
    df = stk_object.data_providers.item('J2000 Angles').execute_elements(start_time, stop_time, step, ['Pole Wander Y', 'Time']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': True, 'label': 'Angle', 'lines': [
            {'y_name':'pole wander y', 'label':'Pole Wander Y', 'use_unit':True, 'unit_squared': None, 'dimension': 'Angle'}]}]
    return line_chart([df], root, ['pole wander y'], ['time'], axes, 'time', 'Time', 'PoleWanderY', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def ut1_utc_line_chart(stk_object :Scenario, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the difference between the UT1 and UTC time scales over time.

    Civil time is tied to UTC while UT1 represents time using the actual rotation of the Earth, which varies due to gravitational effects of the Moon, the Sun, and other planets.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Scenario\\UT1-UTC.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Scenario
        The STK Scenario object.
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
    df = stk_object.data_providers.item('J2000 Angles').execute_elements(start_time, stop_time, step, ['Time', 'UT1-UTC']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Time', 'lines': [
            {'y_name':'ut1-utc', 'label':'UT1-UTC', 'use_unit':True, 'unit_squared': None, 'dimension': 'Time'}]}]
    return line_chart([df], root, ['ut1-utc'], ['time'], axes, 'time', 'Time', 'UT1-UTC', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)