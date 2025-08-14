centroid_solar_az_el_line_chart
===============================

.. image:: /graph_images_temp/test_centroid_solar_az_el_line_chart_areatarget.png
  :width: 600
  :alt: image of output from centroid_solar_az_el_line_chart

.. py:function:: ansys.stk.extensions.data_analysis.graphs.area_target_graphs.centroid_solar_az_el_line_chart(stk_object: ~AreaTarget, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, step: ~float = 60, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.area_target_graphs.centroid_solar_az_el_line_chart

    Create a plot of the elevation and azimuth over time, describing the relative position vector of the apparent Sun to the area target centroid, with respect to the local horizontal plane.

    This frame has the Z axis aligned with the inward surface normal direction (minus Z is up) and the X axis constrained toward the local north direction.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\AreaTarget\\Centroid Solar Az-El.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.AreaTarget`
        The STK AreaTarget object.

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


.. py:currentmodule:: centroid_solar_az_el_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.area_target_graphs import centroid_solar_az_el_line_chart


