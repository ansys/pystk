access_duration_pie_chart
=========================

.. image:: /graph_images_temp/test_access_duration_pie_chart.png
  :width: 600
  :alt: image of output from access_duration_pie_chart

.. py:function:: access_duration_pie_chart(stk_object: ~Access, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, colormap: ~matplotlib.colors.Colormap = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.access_graphs.access_duration_pie_chart

    Create pie chart of the durations of the access intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Access Duration.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Access`
        The STK Access object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation (the default is None, which implies using the scenario start time).

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation (the default is None, which implies using the scenario stop time).

        **colormap** : :obj:`~matplotlib.colors.Colormap`
        The colormap with which to color the data (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: access_duration_pie_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.access_graphs import access_duration_pie_chart


