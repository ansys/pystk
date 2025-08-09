interval_pie_chart
==================

.. py:function:: interval_pie_chart(root: ~STKObjectRoot, df: ~pandas.DataFrame, numerical_columns: list[~str], time_columns: list[~str], start_column: ~str, stop_column: ~str, start_time: ~str, stop_time: ~str, title: ~str, dimension: ~str, cumulative: ~bool = False, color_list: list[~typing.Any] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.graph_helpers.interval_pie_chart

    Create an interval pie chart from the provided dataframe.



    :Parameters:

        **root** : :obj:`~ansys.stk.core.stkobjects.STKObjectRoot`
        The STK object root.

        **df** : :obj:`~pandas.DataFrame`
        The dataframe containing the data.

        **numerical_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with numerical values.

        **time_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with time values.

        **start_column** : :obj:`~str`
        The column containing the start times of the intervals.

        **stop_column** : :obj:`~str`
        The column containing the stop times of the intervals.

        **start_time** : :obj:`~str`
        The start time of the calculation.

        **stop_time** : :obj:`~str`
        The stop time of the calculation.

        **title** : :obj:`~str`
        The title of the chart.

        **dimension** : :obj:`~str`
        The dimension of the chart data.

        **cumulative** : :obj:`~bool`
        Whether the intervals should be summed into durations and gaps (the default is False).

        **color_list** : :obj:`~list` of :obj:`~typing.Any`
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.

    :Raises:

        :obj:`~ValueError`
        If the length of color_list is less than 2.

.. py:currentmodule:: interval_pie_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_pie_chart


