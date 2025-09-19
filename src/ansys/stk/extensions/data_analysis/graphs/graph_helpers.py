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

"""PySTK Graphing Utilities.

A set of helper functions for graphing basic STK desktop graph types.
"""

import collections.abc
from math import ceil, radians
import typing

import matplotlib
import matplotlib.axes
import matplotlib.figure
import matplotlib.pyplot
import numpy as np
import pandas

from ansys.stk.core.stkobjects import Access, STKObjectRoot
from ansys.stk.core.stkutil import UnitPreferencesDimensionCollection
from ansys.stk.extensions.data_analysis._dates import _STKDate, _STKDateConverter


def polar_chart(data : list[pandas.DataFrame], root : STKObjectRoot, numerical_columns : list[str], axis : dict, title : str, origin_0 : bool = False, convert_negative_r : bool = False, colormap: matplotlib.colors.Colormap = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    """Create a polar chart from the provided dataframe and axis information.

    Parameters
    ----------
    data : list of pandas.DataFrame
        The list of DataFrames containing the data.
    root : ansys.stk.core.stkobjects.STKObjectRoot
        The STK object root.
    numerical_columns : list of str
        The list of dataframe columns with numerical values.
    axis : dict
        The dictionary containing information about the data to plot.
    title : str
        The title of the chart.
    origin_0 : bool
        Whether to set the theta 0 point to the top of the graph.
    convert_negative_r : bool
        Whether to convert negative radius values by using opposite angle values.
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the lines (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    # create plot
    fig, ax = matplotlib.pyplot.subplots(subplot_kw={"projection": "polar"})

    # get unit preferences from root
    units_preferences = root.units_preferences
    unit = None

    # use one color per line
    colors = colormap(np.linspace(0, 1, len(data))) if colormap else matplotlib.pyplot.cm.rainbow(np.linspace(0,1,len(data)))

    for i, df in enumerate(data):
        # data conversions
        df = _convert_columns(df, numerical_columns, [], units_preferences)
        df.dropna(axis=0, inplace=True)

        # matplotlib works in radians, so get x (theta) column and convert
        x_column = axis["lines"][0]["x_name"]
        df[x_column] = df[x_column].apply(lambda x : radians(x))

        # get line information
        line = axis["lines"][0]
        # get y (r) variable
        y_var = line["y_name"]

        # matplotlib doesn"t support negative r values in polar graphs, so convert for stk graphs
        # that show negative r values with negative angle
        if convert_negative_r:
            _eliminate_negative_r_polar_vals(df, y_var, x_column)

        # if line uses unit, get current unit
        label = ""
        if line["use_unit"]:
            unit = units_preferences.get_current_unit_abbrv(line["dimension"])
            label = line["label"] + f"({unit})"

        # plot x and y data
        x_data = df[x_column]
        y_data = df[y_var]
        ax.plot(x_data, y_data, label=label, color=colors[i])

    # set x label
    ax.set_xlabel(f"{axis['label']} ({unit})") if unit else ax.set_xlabel(f"{axis['label']}")
    # set styling
    ax.set_facecolor("whitesmoke")
    ax.grid(visible=True, axis="both", which="both", linestyle="--")
    # set title
    ax.set_title(title, y=1.05)
    # set theta direction to match stk
    ax.set_theta_direction(-1)

    # styling for y axis with negative values to match stk styling
    if not convert_negative_r:
        ax.invert_yaxis()

    # configure origin location to match stk
    if origin_0:
        ax.set_theta_zero_location("N")

    # return figure and axis
    return fig, ax

def interval_plot(data : list[pandas.DataFrame], root : STKObjectRoot, element_pairs : list, numerical_columns : list[str], time_columns : list[str], x_label : str, title : str, colormap: matplotlib.colors.Colormap = None, time_unit_abbreviation: str = "UTCG", formatter: collections.abc.Callable[[float, float], str] = None) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    """Create an interval plot from the provided list of dataframes.

    Parameters
    ----------
    data : list of pandas.DataFrame
        The list of DataFrames containing the data.
    root : ansys.stk.core.stkobjects.STKObjectRoot
        The STK object root.
    numerical_columns : list of str
        The list of dataframe columns with numerical values.
    time_columns : list of str
        The list of dataframe columns with time values.
    x_label : str
        The label for the x-axis.
    title : str
        The title of the chart.
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the lines (the default is None).
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
    # create plot
    fig, ax = matplotlib.pyplot.subplots()

    # count number of bars
    bar_num = 0

    # create color map with one color for each bar
    colors = colormap(np.linspace(0, 1, len(element_pairs))) if colormap else matplotlib.pyplot.cm.rainbow(np.linspace(0, 1, len(element_pairs)))

    # collect bars
    bars = []

    # collect y tick locations
    tick_locs = []

    # get unit preferences from root
    units_preferences = root.units_preferences

     # data conversions
    for df in data:
        df = _convert_columns(df, numerical_columns, time_columns, units_preferences, root=root)
        df.dropna(axis=0, inplace=True)

    # format time axis
    all_times = (pandas.concat([df[time_columns] for df in data])).stack().reset_index(drop=True).sort_values()
    time_difference = all_times.iloc[-1] - all_times.iloc[0]
    matplotlib.units.registry[_STKDate] = _STKDateConverter(root, time_difference, time_unit_abbreviation, formatter)

    # iterate through pairs of elements
    for i in range(len(element_pairs)):
        element_pair = element_pairs[i]
        first_elem = element_pair[0]
        second_elem = element_pair[1]
        # get corresponding dataframe
        df = data[i]
        # add column to dataframe with difference between end and start times
        df["graph duration"] = df[second_elem[0]] - df[first_elem[0]]
        # create bar starting at start times with length corresponding to duration
        # label if label provided, otherwise leave blank
        bars.append(ax.broken_barh(list(zip(df[first_elem[0]], df["graph duration"])), (bar_num*10 + 10, 9), zorder=1, facecolors=colors[bar_num], label=first_elem[1] if first_elem[1] else ""))
        # append tick location
        tick_locs.append(bar_num*10 + 14.5)
        bar_num += 1

    # set x label
    ax.set_xlabel(f"{x_label}")

    # create legend if more than one bar
    if len(element_pairs) > 1:
        ax.legend(bars, [b.get_label() for b in bars])

    # set title
    ax.set_title(title)

    # set styling
    ax.set_facecolor("whitesmoke")
    ax.grid(visible=True, axis="both", which="both", linestyle="--")
    ax.set_axisbelow(True)

    # label y-axis using tick locations
    ax.set_yticks(tick_locs, labels = [b.get_label() for b in bars])

    # hide y-axis
    ax.get_yaxis().set_visible(False)

    # set size
    fig.set_size_inches(18.5, 7)

    _format_time_x_axis(fig, ax, all_times.iloc[0], all_times.iloc[-1], root, time_unit_abbreviation)

    # return figure and axis
    return fig, ax

def line_chart(data : list[pandas.DataFrame], root : STKObjectRoot, numerical_columns : list[str], time_columns: list[str], axes : list[dict], x_column : str, x_label : str, title : str, colormap: matplotlib.colors.Colormap = None, time_unit_abbreviation: str = "UTCG", formatter: collections.abc.Callable[[float, float], str] = None, multiple_data_providers: bool = False) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    """Create a line chart from the provided dataframe and axes information.

    Parameters
    ----------
    data : list of pandas.DataFrame
        The list of DataFrames containing the data.
    root : ansys.stk.core.stkobjects.STKObjectRoot
        The STK object root.
    numerical_columns : list of str
        The list of dataframe columns with numerical values.
    time_columns : list of str
        The list of dataframe columns with time values.
    axes : list of dict
        The list of dictionaries containing information about the data to plot.
    x_column : str
        The column corresponding to the x-axis data.
    x_label : str
        The label for the x-axis.
    title : str
        The title of the chart.
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the lines (the default is None).
    time_unit_abbreviation : str
        The time unit for formatting (the default is "UTCG").
    formatter : collections.abc.Callable[[float, float], str]
        The formatter for time axes (the default is None).
    multiple_data_providers: bool
        Whether each dataframe provided corresponds to a different data provider and axis (the default is False).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    # count number of lines
    num_lines = 0
    for axis in axes:
        num_lines += len(axis["lines"])

    # get unit preferences from root
    units_preferences = root.units_preferences

    # create plot
    fig, ax = matplotlib.pyplot.subplots()
    # add matplotlib axis to list
    axes_list = [ax]

    # data conversions
    for i, df in enumerate(data):
        df.dropna(inplace=True, subset=[x_column])
        if multiple_data_providers:
            numerical_columns_to_convert = numerical_columns[i]
        else:
            numerical_columns_to_convert = numerical_columns
        if time_columns:
            df = _convert_columns(df, numerical_columns_to_convert, time_columns, units_preferences, root=root)
        elif numerical_columns:
            df = _convert_columns(df, numerical_columns_to_convert, time_columns, units_preferences)
        df.sort_values(x_column, inplace=True)
    if x_column in time_columns:
        all_times = (pandas.concat([df[x_column] for df in data])).sort_values()
        time_difference = all_times.iloc[-1] - all_times.iloc[0]
        matplotlib.units.registry[_STKDate] = _STKDateConverter(root, time_difference, time_unit_abbreviation, formatter)

    # used to count line number to subset color map
    line_count = 0
    # line collection for legend
    mpl_lines = []
    for i in range(len(data)):
        df = data[i]

        # create color map with correct length
        colors = colormap(np.linspace(0, 1, num_lines)) if colormap else matplotlib.pyplot.cm.rainbow(np.linspace(0, 1, num_lines))

        # used to count line number to subset color map
        if not multiple_data_providers:
            line_count = 0
            # line collection for legend
            mpl_lines = []

        # get x data from dataframe
        x_data = df[x_column]

        # iterate through axes information parameter
        for j in range(len(axes)):
            axis = axes[j]
            # if additional axes needed, duplicated matplotlib axis
            if j != 0 and i==0:
                ax = ax.twinx()
                axes_list.append(ax)
            ax = axes_list[j]
            # iterate through lines under axis
            for k in range(len(axis["lines"])):
                if (not multiple_data_providers) or (multiple_data_providers and i == j):
                    line = axis["lines"][k]
                    # get y data
                    y_data = df[line["y_name"]]
                    # get line label
                    label = line["label"]
                    # if line uses unit, get current unit
                    if line["use_unit"]:
                        unit = units_preferences.get_current_unit_abbrv(line["dimension"])
                        # check if unit should be squared in label
                        if line["unit_squared"]:
                            label = label + f"({unit}^2)"
                        else:
                            label = label + f"({unit})"

                    mpl_lines.extend(ax.plot(x_data, y_data, label=label, color=colors[line_count], linewidth=1.5))
                    line_count += 1

            if i == 0:
                # if axis uses unit, set unit in label
                if axis["use_unit"]:
                    if axis["unit_squared"]:
                        ax.set_ylabel(axis["label"] + f" ({unit}^2)")
                    else:
                        ax.set_ylabel(axis["label"] + f" ({unit})")
                else:
                    ax.set_ylabel(axis["label"])

                # set x-label
                ax.set_xlabel(x_label)

                # set styling (must be done for each axis)
                ax.set_facecolor("whitesmoke")

                if len(axes) == 1:
                    ax.grid(visible=True, axis="both", which="both", linestyle="--")
                # if multiple axes, only plot x gridlines
                else:
                    ax.grid(visible=True, axis="x", which="both", linestyle="--")

                # set axis scales
                if axis["ylog10"]:
                    ax.set_yscale("log")
                elif axis["y2log10"]:
                    ax.set_yscale("log", base=2)

    # format time x-axis if needed
    if x_column in time_columns:
        _format_time_x_axis(fig, ax, all_times.iloc[0], all_times.iloc[-1], root, time_unit_abbreviation)

    # if multiple lines, create legend
    if num_lines > 1:
        legend = ax.legend(mpl_lines, [line.get_label() for line in mpl_lines], loc="upper center", fontsize=10)
        for legend_object in legend.legend_handles:
            legend_object.set_linewidth(2.0)

    # set title and size
    ax.set_title(title)
    fig.set_size_inches(12, 6)
    # return figure and axis
    return fig, ax

def pie_chart(
    root: STKObjectRoot,
    df: pandas.DataFrame,
    numerical_columns: list[str],
    time_columns: list[str],
    column: str,
    title: str,
    dimension: str,
    label_column: str = None,
    colormap: matplotlib.colors.Colormap = None
) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    """Create a pie chart from the provided dataframe and information.

    Parameters
    ----------
    root : ansys.stk.core.stkobjects.STKObjectRoot
        The STK object root.
    df : pandas.DataFrame
        The dataframe containing the data.
    numerical_columns : list of str
        The list of dataframe columns with numerical values.
    time_columns : list of str
        The list of dataframe columns with time values.
    column : str
        The dataframe column to plot in the pie chart.
    title : str
        The title of the chart.
    dimension : str
        The dimension of the chart data.
    label_column : str
        The dataframe column corresponding to the chart labels (the default is None).
    colormap : matplotlib.colors.Colormap
        The colormap with which to color the pie chart slices (the default is None).

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.

    """
    # create plot
    fig, ax = matplotlib.pyplot.subplots()

    # get units
    units_preferences = root.units_preferences
    unit = units_preferences.get_current_unit_abbrv(dimension)

    # data conversions
    df = _convert_columns(df, numerical_columns, time_columns, units_preferences, root= root)
    df.dropna(axis=0, inplace=True)

    # create colormap with one color for each slice of pie
    num_colors_needed = len(df[column].value_counts())
    colors = colormap(np.linspace(0, 1, num_colors_needed)) if colormap else matplotlib.pyplot.cm.rainbow(np.linspace(0, 1, num_colors_needed))

    # if plot is labeled with a different column, get and configure labels
    labels = []
    if label_column:
        for i in range(len(df[label_column])):
            labels.append(f"{label_column} {df[label_column][i]:.0f}: {df[column][i]:.3f}({unit})")

    # create pie chart
    ax.pie(df[column], autopct="%1.1f%%", labels=labels, colors=colors, textprops={"fontsize": 8}, counterclock=False)

    # set title
    ax.set_title(title)

    # return figure and axis
    return fig, ax


def interval_pie_chart(
    root: STKObjectRoot,
    df: pandas.DataFrame,
    numerical_columns: list[str],
    time_columns: list[str],
    start_column: str,
    stop_column: str,
    start_time: str,
    stop_time: str,
    title: str,
    dimension: str,
    cumulative: bool = False,
    color_list: list[typing.Any] = None
) -> tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]:
    """Create an interval pie chart from the provided dataframe.

    Parameters
    ----------
    root : ansys.stk.core.stkobjects.STKObjectRoot
        The STK object root.
    df : pandas.DataFrame
        The dataframe containing the data.
    numerical_columns : list of str
        The list of dataframe columns with numerical values.
    time_columns : list of str
        The list of dataframe columns with time values.
    start_column : str
        The column containing the start times of the intervals.
    stop_column : str
        The column containing the stop times of the intervals.
    start_time : str
        The start time of the calculation.
    stop_time : str
        The stop time of the calculation.
    title : str
        The title of the chart.
    dimension : str
        The dimension of the chart data.
    cumulative : bool
        Whether the intervals should be summed into durations and gaps (the default is False).
    color_list : list of typing.Any
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.

    Raises
    ------
    ValueError
        If the length of color_list is less than 2.
    """
    # get unit preferences
    units_preferences = root.units_preferences
    unit = units_preferences.get_current_unit_abbrv(dimension)
    date_unit = units_preferences.get_current_unit_abbrv("Date")

    # data conversions
    df = _convert_columns(df, numerical_columns, time_columns, units_preferences, root=root)

    # create duration column using stop and start columns
    df["graph duration"] = df[stop_column] - df[start_column]

    # create gap column with times in between durations
    df["graph gap"] = df[start_column].shift(-1) - df[stop_column]

    # last gap is from end of last duration to stop time
    last_gap = _STKDate.from_value_and_format(root, stop_time, unit=date_unit) - df.iloc[-1][stop_column]
    #if last_gap != 0:
    df.at[df.index[-1], "graph gap"] = last_gap
    # first gap is from analysis start time to start of first duration
    first_gap = df[start_column][0] - _STKDate.from_value_and_format(root, start_time, unit=date_unit)

    # create plot
    fig, ax = matplotlib.pyplot.subplots()
    if color_list and len(color_list) < 2:
        raise ValueError("If provided, 'color_list' argument must contain at least 2 colors.")

    if cumulative:
        # if plot is cumulative, sum durations
        duration_sum = df["graph duration"].sum()
        # then gap is equivalent to sum of gaps + first gap
        gap_sum = df["graph gap"].sum() + first_gap

        colors = color_list if color_list else ["deepskyblue", "slategray"]

        # plot duration and gap sums
        matplotlib.pyplot.pie(
            [duration_sum, gap_sum],
            labels=[
                f"Cumulative Duration: {duration_sum:.2f} ({unit})",
                f"Cumulative Gap: {gap_sum:.2f} ({unit})",
            ],
            colors=colors,
            autopct="%1.3f%%",
            labeldistance=None,
            pctdistance=1.2,
        )
        # create legend
        ax.legend(shadow=True, loc="lower center")
    else:
        colors = color_list if color_list else ["slategray", "deepskyblue"]

        # create zipped list with each duration and gap paired
        zip_list = list(zip(df["graph duration"], df["graph gap"]))
        flat_list = []
        label_list = []
        count = 2

        # flatten list while maintaining order and create list of labels
        for duration, gap in zip_list:
            flat_list.extend([duration, gap])

            if not np.isnan(duration) and duration != 0:
                label_list.append(f"duration {count -1}: {duration:.2f}({unit})")

            if not np.isnan(gap) and gap !=0:
                label_list.append(f"gap {count}: {gap:.2f}({unit})")

            count += 1

        # remove any nan or 0 values
        cleaned_list = [x for x in flat_list if not np.isnan(x) and x!=0]
        # get gap before start of first interval, add to data and label lists
        if first_gap != 0:
            cleaned_list.insert(0, first_gap)
            label_list.insert(0, f"gap 1: {first_gap:.2f}({unit})")
        # if no first gap, reverse color order to maintain blue for durations and gray for gaps
        else:
            colors.reverse()
        # plot intervals
        matplotlib.pyplot.pie(
            cleaned_list,
            colors=colors,
            autopct="%1.3f%%",
            pctdistance=1.15,
            wedgeprops={"edgecolor": "black", "linewidth": 1, "antialiased": True},
        )
        # set size
        fig.set_size_inches(8, 8)
        # create legend
        ax.legend(
            labels=label_list,
            ncol=ceil(len(cleaned_list) / 4),
            loc="lower center",
            bbox_to_anchor=(0.5, -0.15),
            shadow=True,
            fontsize="x-small",
        )

    # set title
    ax.set_title(title)

    # return figure and axis
    return fig, ax

def _convert_columns(
    df: pandas.DataFrame, numerical_column_list: list[str], date_column_list: list[str], unit_preferences: UnitPreferencesDimensionCollection, root: STKObjectRoot = None
) -> pandas.DataFrame:
    """Convert numerical and time columns in a pandas dataframe.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataframe containing the data.
    numerical_column_list : list of str
        The list of dataframe columns with numerical values.
    date_column_list : list of str
        The list of dataframe columns with time values.
    unit_preferences : UnitPreferencesDimensionCollection
        The collection of scenario-wide unit preferences.
    root : STKObjectRoot
        The STK object root.

    Returns
    -------
    pandas.DataFrame
        The dataframe with converted columns.
    """
    df[numerical_column_list] = df[numerical_column_list].astype(float)
    if date_column_list:
        for col in date_column_list:
            if col in df:
                df[col] = df[col].apply(lambda x: _STKDate.from_value_and_format(root, x, unit_preferences.get_current_unit_abbrv("Date")))
    return df

def _format_time_x_axis(fig : matplotlib.figure.Figure, ax : matplotlib.axes.Axes, first_time : _STKDate, last_time : _STKDate, root : STKObjectRoot, time_unit_abbreviation : str):
    """Convert numerical and time columns in a pandas dataframe.

    Parameters
    ----------
    matplotlib.figure.Figure
        The figure.
    matplotlib.axes.Axes
        The axes.
    first_time : _STKDate
        The earliest time in the data.
    last_time : _STKDate
        The latest time in the data.
    root : STKObjectRoot
        The STK object root.
    """

    def get_d_m_y_utcg(date : _STKDate):
        return date.get_utcg().rsplit(" ", maxsplit=1)[0]

    if time_unit_abbreviation == "UTCG":
        if last_time - first_time < 604800:
            fig.text(0.05, 0.01, get_d_m_y_utcg(first_time),
                horizontalalignment="left", verticalalignment="bottom",
                fontsize=10)
            if get_d_m_y_utcg(first_time) != get_d_m_y_utcg(last_time):
                fig.text(0.95, 0.01, get_d_m_y_utcg(last_time),
                horizontalalignment="right", verticalalignment="bottom",
                fontsize=10)

    # add vertical lines showing day changes
    if last_time - first_time < 2592000:
        start_date = _STKDate.from_value_and_format(root, get_d_m_y_utcg(first_time) + " 00:00:00.000").add_duration(1, "day")
        while start_date < last_time:
            ax.axvline(x=start_date.get_epsec(), color="black", linestyle="-", linewidth=1.5)
            ax.annotate(start_date.format(time_unit_abbreviation), xy =(start_date.get_epsec(),ax.get_ylim()[0]), xytext=(0, 7), rotation = 270, fontsize=9, textcoords="offset points")
            start_date = start_date.add_duration(1, "day")

def _get_access_data(access :Access, item : str, group : bool, group_name : str, elements: list[str], start_time: typing.Any, stop_time: typing.Any, step : float) -> list[pandas.DataFrame]:
    """Get list of data for access object, grouping by access interval while respecting start and stop times.

    Parameters
    ----------
    access : ansys.stk.core.stkobjects.Access
        The STK Access object.
    item : str
        The data provider.
    group : bool
        If the data provider is grouped.
    group_name : str
        The group.
    elements : list of str
        The list of data provider elements to execute.
    start_time : typing.Any
        The start time of the calculation.
    stop_time : typing.Any
        The stop time of the calculation.
    step_time : float
        The step time for the calculation.

    Returns
    -------
    list of pandas.DataFrame
        The list of data.

    Raises
    ------
    ValueError
        If none of the access intervals are contained within the provided start and stop times.
    """
    data=[]
    root = access.base.root
    start_time = _STKDate.from_value_and_format(root, start_time)
    stop_time = _STKDate.from_value_and_format(root, stop_time)
    access_intervals = access.computed_access_interval_times
    for i in range(0, access_intervals.count):
        times = access_intervals.get_interval(i)
        interval_start = _STKDate.from_value_and_format(root, times[0])
        interval_end = _STKDate.from_value_and_format(root, times[1])
        computation_start = None
        computation_stop = None
        # interval fully outside of desired calculation period, so skip
        if (interval_start < start_time and interval_end < start_time) or (interval_start > stop_time and interval_end > stop_time):
            continue
        # interval fully contained within desired calculation period, so include entire interval
        if interval_start >= start_time and interval_end <= stop_time:
            computation_start = interval_start.get_utcg()
            computation_stop = interval_end.get_utcg()
        else:
            # starts before desired calculation period, so start calculation at desired start time
            if interval_start < start_time:
                computation_start = start_time.get_utcg()
            # ends after desired calculation period, so end calculation at desired end time
            if interval_end > stop_time:
                computation_stop = stop_time.get_utcg()
        if group:
            data.append(access.data_providers.item(item).group.item(group_name).execute_elements(computation_start, computation_stop, step, elements).data_sets.to_pandas_dataframe())
        else:
            data.append(access.data_providers.item(item).execute_elements(computation_start, computation_stop, step, elements).data_sets.to_pandas_dataframe())
    if len(data) == 0:
        raise ValueError("No access data to plot- check provided start and stop times.")
    return data

def _eliminate_negative_r_polar_vals(df : pandas.DataFrame, r_var : str, theta_var : str):
    """Convert negative r values in a dataframe that has r and theta values.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe containing the data.
    r_var : str
        The column corresponding to the radius variable.
    theta_var : str
        The column corresponding to the angle variable.
    """
    df[theta_var]= np.where(df[r_var] >= 0, df[theta_var], df[theta_var] + np.pi)
    df[r_var] = df[r_var].apply(lambda x: abs(x))
