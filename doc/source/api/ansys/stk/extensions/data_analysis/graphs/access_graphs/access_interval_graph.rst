access_interval_graph
=====================

.. image:: /graph_images_temp/test_access_interval_graph.png
  :width: 600
  :alt: image of output from access_interval_graph

.. py:function:: access_interval_graph(stk_object: ~Access, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, colormap: ~matplotlib.colors.Colormap = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.access_graphs.access_interval_graph

    Create an interval graph of the access intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Access.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Access`
        The STK Access object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation.

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation.

        **colormap** : :obj:`~matplotlib.colors.Colormap`
        The colormap with which to color the data (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: access_interval_graph


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.access_graphs import access_interval_graph


