pie_chart
=========

.. py:function:: pie_chart(root: ~STKObjectRoot, df: ~pandas.DataFrame, numerical_columns: list[~str], time_columns: list[~str], column: ~str, title: ~str, dimension: ~str, label_column: ~str = None, colormap: ~matplotlib.colors.Colormap = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.graph_helpers.pie_chart

    Create a pie chart from the provided dataframe and information.



    :Parameters:

        **root** : :obj:`~ansys.stk.core.stkobjects.STKObjectRoot`
        The STK object root.

        **df** : :obj:`~pandas.DataFrame`
        The dataframe containing the data.

        **numerical_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with numerical values.

        **time_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with time values.

        **column** : :obj:`~str`
        The dataframe column to plot in the pie chart.

        **title** : :obj:`~str`
        The title of the chart.

        **dimension** : :obj:`~str`
        The dimension of the chart data.

        **label_column** : :obj:`~str`
        The dataframe column corresponding to the chart labels (the default is None).

        **colormap** : :obj:`~matplotlib.color.Colormap`
        The colormap with which to color the pie chart slices (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: pie_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.graph_helpers import pie_chart


