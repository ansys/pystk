interval_plot
=============

.. py:function:: interval_plot(data: list[~pandas.DataFrame], root: ~STKObjectRoot, element_pairs: ~list, numerical_columns: list[~str], time_columns: list[~str], x_label: ~str, title: ~str, colormap: ~matplotlib.colors.Colormap = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.graph_helpers.interval_plot

    Create an interval plot from the provided list of dataframes.



    :Parameters:

        **data** : :obj:`~list` of :obj:`~pandas.DataFrame`
        The list of DataFrames containing the data.

        **root** : :obj:`~ansys.stk.core.stkobjects.STKObjectRoot`
        The STK object root.

        **numerical_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with numerical values.

        **time_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with time values.

        **x_label** : :obj:`~str`
        The label for the x-axis.

        **title** : :obj:`~str`
        The title of the chart.

        **colormap** : :obj:`~matplotlib.colors.Colormap`
        The colormap with which to color the lines (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: interval_plot


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.graph_helpers import interval_plot


