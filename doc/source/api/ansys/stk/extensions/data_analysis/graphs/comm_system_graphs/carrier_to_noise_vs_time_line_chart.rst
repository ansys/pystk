carrier_to_noise_vs_time_line_chart
===================================

.. image:: /graph_images_temp/test_carrier_to_noise_vs_time_line_chart_commsystem.png
  :width: 600
  :alt: image of output from carrier_to_noise_vs_time_line_chart

.. py:function:: carrier_to_noise_vs_time_line_chart(stk_object: ~CommSystem, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, step: ~float = 60, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.comm_system_graphs.carrier_to_noise_vs_time_line_chart

    Graph the carrier-to-noise ratio and the carrier-to-noise-plus-interference ratio as a function of time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CommSystem\\Carrier to Noise vs Time.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.CommSystem`
        The STK CommSystem object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation (the default is None, which implies using the scenario start time).

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation (the default is None, which implies using the scenario stop time).

        **step_time** : :obj:`~float`
        The step time for the calculation (the default is 60 seconds).

        **colormap** : :obj:`~matplotlib.colors.Colormap`
        The colormap with which to color the data (the default is None).

        **time_unit_abbreviation** : :obj:`~str`
        The time unit for formatting (the default is "UTCG").

        **formatter** : :obj:`~collections.abc.Callable` [[:obj:`~float`, :obj:`~float`], :obj:`~str`]
        The formatter for time axes (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: carrier_to_noise_vs_time_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.comm_system_graphs import carrier_to_noise_vs_time_line_chart


