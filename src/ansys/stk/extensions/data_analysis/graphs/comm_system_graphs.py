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

"""Provides graphs for CommSystem objects."""
import collections.abc
import typing

import matplotlib

from ansys.stk.core.stkobjects import CommSystem
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import line_chart


def carrier_to_noise_vs_time_line_chart(stk_object :CommSystem, start_time : typing.Any = None, stop_time :typing.Any = None, step : float = 60, colormap: matplotlib.colors.Colormap = None,  time_unit_abbreviation: str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Graph the carrier-to-noise ratio and the carrier-to-noise-plus-interference ratio as a function of time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CommSystem\\Carrier to Noise vs Time.rsg`.

    Parameters
    ----------
    stk_object : ansys.stk.core.stkobjects.CommSystem
        The STK CommSystem object.
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
    df = stk_object.data_providers.item('Link Information').execute_elements(start_time, stop_time, step, ['C/N', 'Time', 'C/(N+I)']).data_sets.to_pandas_dataframe()
    axes = [{'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'c/n', 'label':'C/N', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]},
            {'use_unit' : True, 'unit_squared': None, 'ylog10': False, 'y2log10': False, 'label': 'Ratio', 'lines': [
            {'y_name':'c/(n+i)', 'label':'C/(N+I)', 'use_unit':True, 'unit_squared': None, 'dimension': 'Ratio'}]}]
    return line_chart([df], root, ['c/n','c/(n+i)'], ['time'], axes, 'time', 'Time', 'Carrier to Noise vs Time', colormap=colormap,  time_unit_abbreviation= time_unit_abbreviation, formatter= formatter)

