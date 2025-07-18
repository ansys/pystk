az_el_polar_center_90_graph
===========================

.. image:: /graph_images_temp/test_az_el_polar_center_90_graph.png
  :width: 600
  :alt: image of output from az_el_polar_center_90_graph

.. py:function:: az_el_polar_center_90_graph(stk_object: ~Access, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, step: ~float = 60, colormap: ~matplotlib.colors.Colormap = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.access_graphs.az_el_polar_center_90_graph

    Create a polar plot with elevation as radius and azimuth as angle theta over time, during access intervals.

    The azimuth and elevation describe the relative position vector between the base object and the target object. The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Az El Polar.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Access`
        The STK Access object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation.

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation.

        **step_time** : :obj:`~float`
        The step time for the calculation (the default is 60 seconds).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: az_el_polar_center_90_graph


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.access_graphs import az_el_polar_center_90_graph


