polar_chart
===========

.. py:function:: polar_chart(data: list[~pandas.DataFrame], root: ~STKObjectRoot, numerical_columns: list[~str], axis: ~dict, title: ~str, origin_0: ~bool = False, convert_negative_r: ~bool = False, colormap: ~matplotlib.colors.Colormap = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.graph_helpers.polar_chart

    Create a polar chart from the provided dataframe and axis information.



    :Parameters:

        **data** : :obj:`~list` of :obj:`~pandas.DataFrame`
        The list of DataFrames containing the data.

        **root** : :obj:`~ansys.stk.core.stkobjects.STKObjectRoot`
        The STK object root.

        **numerical_columns** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with numerical values.

        **axis** : :obj:`~dict`
        The dictionary containing information about the data to plot.

        **title** : :obj:`~str`
        The title of the chart.

        **origin_0** : :obj:`~bool`
        Whether to set the theta 0 point to the top of the graph.

        **convert_negative_r** : :obj:`~bool`
        Whether to convert negative radius values by using opposite angle values.

        **colormap** : :obj:`~matplotlib.colors.Colormap`
        The colormap with which to color the lines (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: polar_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.graph_helpers import polar_chart


