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
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
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
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
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
    if start_time is None:
        start_time = root.current_scenario.start_time
    if stop_time is None:
        stop_time = root.current_scenario.stop_time
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
