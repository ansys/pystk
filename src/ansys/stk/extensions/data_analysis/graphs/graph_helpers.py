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

from typing import List

import matplotlib
import matplotlib.pyplot
import numpy as np
import pandas

from ansys.stk.core.stkobjects import STKObjectRoot


def pie_chart(
    root: STKObjectRoot,
    df: pandas.DataFrame,
    numerical_columns: List[str],
    time_columns: List[str],
    column: str,
    title: str,
    dimension: str,
    label_column: str = None,
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
    df = _convert_columns(df, numerical_columns, time_columns)
    df.dropna(axis=0, inplace=True)

    # create colormap with one color for each slice of pie
    num_colors_needed = len(df[column].value_counts())
    colors = matplotlib.pyplot.cm.rainbow(np.linspace(0, 1, num_colors_needed))

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
    numerical_columns: List[str],
    time_columns: List[str],
    start_column: str,
    stop_column: str,
    start_time: str,
    stop_time: str,
    title: str,
    dimension: str,
    cumulative: bool = False,
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

    Returns
    -------
    matplotlib.figure.Figure
        The newly created figure.
    matplotlib.axes.Axes
        The newly created axes.
    """
    # data conversions
    df = _convert_columns(df, numerical_columns, time_columns)

    # create duration column using stop and start columns
    df["graph duration"] = df[stop_column] - df[start_column]

    # create gap column with times in between durations
    df["graph gap"] = df[start_column].shift(-1) - df[stop_column]

    # last gap is from end of last duration to stop time
    df.at[df.index[-1], "graph gap"] = pandas.to_datetime(stop_time) - df.iloc[-1]["stop time"]

    # convert duration and graph columns to time delta objects in seconds
    df["graph duration"] = df["graph duration"] / np.timedelta64(1, "s")
    df["graph gap"] = df["graph gap"] / np.timedelta64(1, "s")

    # get unit preferences
    units_preferences = root.units_preferences
    unit = units_preferences.get_current_unit_abbrv(dimension)

    # create plot
    fig, ax = matplotlib.pyplot.subplots()
    if cumulative:
        # if plot is cumulative, sum durations
        duration_sum = df["graph duration"].sum()
        # then gap is equivalent to whole length of time - sum of durations
        gap_sum = (
            (pandas.to_datetime(stop_time) - pandas.to_datetime(start_time)) / np.timedelta64(1, "s")
        ) - duration_sum
        # plot duration and gap sums
        matplotlib.pyplot.pie(
            [duration_sum, gap_sum],
            labels=[
                f"Cumulative Duration: {duration_sum:.2f} ({unit})",
                f"Cumulative Gap: {gap_sum:.2f} ({unit})",
            ],
            colors=["deepskyblue", "slategray"],
            autopct="%1.3f%%",
            labeldistance=None,
            pctdistance=1.2,
        )
        # create legend
        ax.legend(shadow=True, loc="lower center")
    else:
        # create zipped list with each duration and gap paired
        zip_list = list(zip(df["graph duration"], df["graph gap"]))
        flat_list = []
        label_list = []
        count = 2
        # flatten list while maintaining order and create list of labels
        for item in zip_list:
            flat_list.append(item[0])
            if not np.isnan(item[0]):
                label_list.append(f"duration {count -1}: {item[0]:.2f}({unit})")
            flat_list.append(item[1])
            if not np.isnan(item[1]):
                label_list.append(f"gap {count}: {item[1]:.2f}({unit})")
            count += 1
        # remove any nan values
        cleaned_list = [x for x in flat_list if not np.isnan(x)]
        # get gap before start of first interval, add to data and label lists
        first_gap = (pandas.to_datetime(df["start time"][0]) - pandas.to_datetime(start_time)) / np.timedelta64(1, "s")
        cleaned_list.insert(0, first_gap)
        label_list.insert(0, f"gap 1: {first_gap:.2f}({unit})")
        # plot intervals
        matplotlib.pyplot.pie(
            cleaned_list,
            colors=["slategray", "deepskyblue"],
            autopct="%1.3f%%",
            pctdistance=1.15,
            wedgeprops={"edgecolor": "black", "linewidth": 1, "antialiased": True},
        )
        # set size
        fig.set_size_inches(8, 8)
        # create legend
        ax.legend(
            labels=label_list,
            ncol=len(cleaned_list) / 4,
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
    dataframe: pandas.DataFrame, numerical_column_list: List[str], date_column_list: List[str]
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

    Returns
    -------
    pandas.DataFrame
        The dataframe with converted columns.
    """
    dataframe[numerical_column_list] = dataframe[numerical_column_list].astype(float)
    dataframe[date_column_list] = dataframe[date_column_list].astype("datetime64[ns]")
    return dataframe
