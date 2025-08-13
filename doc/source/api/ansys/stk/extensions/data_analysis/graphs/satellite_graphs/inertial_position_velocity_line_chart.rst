inertial_position_velocity_line_chart
=====================================

.. image:: /graph_images_temp/test_inertial_position_velocity_line_chart_satellite.png
  :width: 600
  :alt: image of output from inertial_position_velocity_line_chart

.. py:function:: inertial_position_velocity_line_chart(stk_object: ~Satellite, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, step: ~float = 60, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.satellite_graphs.inertial_position_velocity_line_chart

    Plot the position and velocity of the object with respect to the object's central body, as observed from its central body's inertial coordinate system, expressed in Cartesian components as a function of time.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Satellite\\Inertial Position Velocity.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Satellite`
        The STK Satellite object.

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


.. py:currentmodule:: inertial_position_velocity_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.satellite_graphs import inertial_position_velocity_line_chart


