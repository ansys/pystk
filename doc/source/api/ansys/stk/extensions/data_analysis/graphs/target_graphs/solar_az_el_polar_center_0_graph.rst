solar_az_el_polar_center_0_graph
================================

.. image:: /graph_images_temp/test_solar_az_el_polar_center_0_graph_target.png
  :width: 600
  :alt: image of output from solar_az_el_polar_center_0_graph

.. py:function:: solar_az_el_polar_center_0_graph(stk_object: ~Target, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, step: ~float = 60, colormap: ~matplotlib.colors.Colormap = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.target_graphs.solar_az_el_polar_center_0_graph

    Create a polar plot with elevation as radius and azimuth as angle theta over time, describing the apparent relative position vector of the Sun with respect to the local horizontal plane.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Target\\Solar Az-El.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Target`
        The STK Target object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation (the default is None, which implies using the scenario start time).

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation (the default is None, which implies using the scenario stop time).

        **step_time** : :obj:`~float`
        The step time for the calculation (the default is 60 seconds).

        **colormap** : :obj:`~matplotlib.colors.Colormap`
        The colormap with which to color the data (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: solar_az_el_polar_center_0_graph


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.target_graphs import solar_az_el_polar_center_0_graph


