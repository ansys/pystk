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

"""Provides graphs for Sensor objects."""
import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import Sensor
from ansys.stk.extensions.data_analysis.graphs._common_graphs import _azimuth_elevation_line_chart
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import line_chart


def azimuth_elevation_line_chart(stk_object :Sensor, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the direction of the sensor's boresight over time, expressed as azimuth and elevation in body-fixed axes of the sensor's parent.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Sensor\\Azimuth-Elevation.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Sensor
        The STK Sensor object.
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
    return _azimuth_elevation_line_chart(stk_object, start_time, stop_time, step, colormap, time_unit_abbreviation, formatter)

def footprint_area_line_chart(stk_object :Sensor, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the area on the ground inside the sensor footprint over time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Sensor\\Footprint Area.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Sensor
        The STK Sensor object.
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
    df = stk_object.data_providers.item('Footprint Area').execute_elements(start_time, stop_time, step, ['Time', 'Area']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Area', 'lines': [
            {'y_name':'area', 'label':'Area', 'use_unit':True, 'unit_squared': None, 'dimension': 'Area'}]}]
    return line_chart([df], root, ['area'], ['time'], axes, 'time', 'Time', 'Footprint Area', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

def obscuration_line_chart(stk_object :Sensor, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create a plot of the percentage that the sensor's field of view is obstructed over time, as generated by Sensor Obscuration tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Sensor\\Obscuration.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.Sensor
        The STK Sensor object.
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
    df = stk_object.data_providers.item('Obscuration').execute_elements(start_time, stop_time, step, ['Time', 'Percent Obscured']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : False, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Percent', 'lines': [
            {'y_name':'percent obscured', 'label':'Percent Obscured', 'use_unit':False, 'unit_squared': None, 'dimension': 'Percent'}]}]
    return line_chart([df], root, ['percent obscured'], ['time'], axes, 'time', 'Time', 'Percent Obscured', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

