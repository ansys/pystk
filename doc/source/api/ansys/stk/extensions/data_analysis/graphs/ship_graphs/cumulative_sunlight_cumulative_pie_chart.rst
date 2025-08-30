cumulative_sunlight_cumulative_pie_chart
========================================

.. image:: /graph_images_temp/test_cumulative_sunlight_cumulative_pie_chart_ship.png
  :width: 600
  :alt: image of output from cumulative_sunlight_cumulative_pie_chart

.. py:function:: ansys.stk.extensions.data_analysis.graphs.ship_graphs.cumulative_sunlight_cumulative_pie_chart(stk_object: ~Ship, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, color_list: list[~typing.Any] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.ship_graphs.cumulative_sunlight_cumulative_pie_chart

    Create a pie chart showing the total duration of full sunlight within the graph's requested time interval.

    Gaps in the chart indicate the total duration of penumbra and umbra durations.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Ship\\Cumulative Sunlight.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Ship`
        The STK Ship object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation (the default is None, which implies using the scenario start time).

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation (the default is None, which implies using the scenario stop time).

        **color_list** : :obj:`~list` of :obj:`~typing.Any`
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: cumulative_sunlight_cumulative_pie_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.ship_graphs import cumulative_sunlight_cumulative_pie_chart


