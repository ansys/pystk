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

import typing

import matplotlib

from ansys.stk.core.stkobjects import Access
from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_pie_chart, pie_chart


def access_duration_pie_graph(
    stk_obj: Access, start_time: typing.Any = None, stop_time: typing.Any = None
) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create pie chart of the durations of the access intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Access Duration.rsg`.

    Parameters
    ----------
    stk_obj : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation (the default is None, which implies using the scenario start time).
    stop_time : typing.Any
        The stop time of the calculation (the default is None, which implies using the scenario stop time).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_obj.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_obj.data_providers.item("Access Data").execute(start_time, stop_time).data_sets.to_pandas_dataframe()
    return pie_chart(root, df, ["duration"], [], "duration", "Access Duration", "Time", "access number")


def cumulative_dwell_cumulative_pie_graph(
    stk_obj: Access, start_time: typing.Any = None, stop_time: typing.Any = None
) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create graph showing access interval durations as a cumulative pie chart.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Cumulative Dwell.rsg`.

    Parameters
    ----------
    stk_obj : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation.
    stop_time : typing.Any
        The stop time of the calculation.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_obj.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_obj.data_providers.item("Access Data").execute(start_time, stop_time).data_sets.to_pandas_dataframe()
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
    )


def revisit_diagram_interval_pie_graph(
    stk_obj: Access, start_time: typing.Any = None, stop_time: typing.Any = None
) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    r"""Create pie chart showing the durations of access intervals and access gap intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Revisit Diagram.rsg`.

    Parameters
    ----------
    stk_obj : ansys.stk.core.stkobjects.Access
        The STK Access object.
    start_time : typing.Any
        The start time of the calculation.
    stop_time : typing.Any
        The stop time of the calculation.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    root = stk_obj.base.root
    start_time = start_time or root.current_scenario.start_time
    stop_time = stop_time or root.current_scenario.stop_time
    df = stk_obj.data_providers.item("Access Data").execute(start_time, stop_time).data_sets.to_pandas_dataframe()
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
    )
