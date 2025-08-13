yaw_pitch_roll_line_chart
=========================

.. image:: /graph_images_temp/test_yaw_pitch_roll_line_chart_satellite.png
  :width: 600
  :alt: image of output from yaw_pitch_roll_line_chart

.. py:function:: yaw_pitch_roll_line_chart(stk_object: ~Satellite, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, step: ~float = 60, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.satellite_graphs.yaw_pitch_roll_line_chart

    Create a plot of the attitude of the vehicle (i.e., the rotation between the vehicle's body axes and the vehicle' central body's inertial frame), expressed using 321 YPR angles, as a function of time.

    YPR angles use a sequence of three rotations starting from a reference coordinate frame. Unlike Euler angles, the rotations are not made about axes defined by an earlier rotation: each rotation is made about the reference system's axes. The 321 sequence uses Z, then Y, and then finally the X axis.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Satellite\\Yaw Pitch Roll.rsg`.

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


.. py:currentmodule:: yaw_pitch_roll_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.satellite_graphs import yaw_pitch_roll_line_chart


