line_chart
==========

.. py:function:: line_chart(data: list[~pandas.DataFrame], root: ~STKObjectRoot, numerical_columns: list[~str], time_columns: list[~str], axes: list[~dict], x_column: ~str, x_label: ~str, title: ~str, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.graph_helpers.line_chart

    Create a line chart from the provided dataframe and axes information.



    :Parameters:

        **data** : :obj:`~list` of :obj:`~pandas.DataFrame`
        The list of DataFrames containing the data.

        **root** : :obj:`~ansys.stk.core.stkobjects.STKObjectRoot`
        The STK object root.

        **numerical_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with numerical values.

        **time_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with time values.

        **axes** : :obj:`~list` of :obj:`~dict`
        The list of dictionaries containing information about the data to plot.

        **x_column** : :obj:`~str`
        The column corresponding to the x-axis data.

        **x_label** : :obj:`~str`
        The label for the x-axis.

        **title** : :obj:`~str`
        The title of the chart.

        **colormap** : :obj:`~matplotlib.colors.Colormap`
        The colormap with which to color the lines (the default is None).

        **time_unit_abbreviation** : :obj:`~str`
        The time unit for formatting (the default is "UTCG").

        **formatter** : :obj:`~collections.abc.Callable` [[:obj:`~float`, :obj:`~float`], :obj:`~str`]
        The formatter for time axes (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.graph_helpers import line_chart


