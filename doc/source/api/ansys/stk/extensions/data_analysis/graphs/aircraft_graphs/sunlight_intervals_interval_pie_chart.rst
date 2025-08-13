sunlight_intervals_interval_pie_chart
=====================================

.. image:: /graph_images_temp/test_sunlight_intervals_interval_pie_chart_aircraft.png
  :width: 600
  :alt: image of output from sunlight_intervals_interval_pie_chart

.. py:function:: sunlight_intervals_interval_pie_chart(stk_object: ~Aircraft, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, color_list: list[~typing.Any] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.aircraft_graphs.sunlight_intervals_interval_pie_chart

    Create a pie chart showing each interval of full sunlight within the graph's requested time interval, separated by gaps indicating the intervals of penumbra/umbra lighting condition before and after each sunlight interval.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Aircraft\\Sunlight Intervals.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Aircraft`
        The STK Aircraft object.

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


.. py:currentmodule:: sunlight_intervals_interval_pie_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.aircraft_graphs import sunlight_intervals_interval_pie_chart


