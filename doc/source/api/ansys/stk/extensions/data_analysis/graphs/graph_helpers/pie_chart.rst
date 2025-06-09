pie_chart
=========

.. py:function:: pie_chart(root: ~STKObjectRoot, df: ~pandas.DataFrame, numerical_columns: ~list, time_columns: ~list, column: ~str, title: ~str, unit_pref: ~str, label_col: ~str = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.graph_helpers.pie_chart

    Create a pie chart from the provided dataframe and information.



    :Parameters:

        **root** : :obj:`~ansys.stk.core.stkobjects.STKObjectRoot`
        The STK object root.

        **df** : :obj:`~pandas.DataFrame`
        The dataframe containing the data.

        **numerical_columns** : :obj:`~list`
        The list of dataframe columns with numerical values.

        **time_columns** : :obj:`~list`
        The list of dataframe columns with time values.

        **column** : :obj:`~str`
        The dataframe column to plot in the pie chart.

        **title** : :obj:`~str`
        The title of the chart.

        **unit_pref** : :obj:`~str`
        The unit type of the chart data.

        **label_col** : :obj:`~str`
        The dataframe column corresponding to the chart labels (the default is None).



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


