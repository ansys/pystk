cumulative_dwell_cumulative_pie_chart
=====================================

.. image:: /graph_images_temp/test_cumulative_dwell_cumulative_pie_chart.png
  :width: 600
  :alt: image of output from cumulative_dwell_cumulative_pie_chart

.. py:function:: cumulative_dwell_cumulative_pie_chart(stk_object: ~Access, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, color_list: list[~typing.Any] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.access_graphs.cumulative_dwell_cumulative_pie_chart

    Create graph showing access interval durations as a cumulative pie chart.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Cumulative Dwell.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Access`
        The STK Access object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation.

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation.

        **color_list** : :obj:`~list` of :obj:`~typing.Any`
        The colors with which to color the pie chart slices (the default is None). Must have length >= 2.



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: cumulative_dwell_cumulative_pie_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.access_graphs import cumulative_dwell_cumulative_pie_chart


