aer_line_chart
==============

.. image:: /graph_images_temp/test_aer_line_chart.png
  :width: 600
  :alt: image of output from aer_line_chart

.. py:function:: aer_line_chart(stk_object: ~Access, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, step: ~float = 60, colormap: ~matplotlib.colors.Colormap = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.access_graphs.aer_line_chart

    Create a plot of the azimuth, elevation, and range values for the relative position vector between the base object and the target object, during access intervals.

    The relative position includes the effects of light time delay and aberration as set by the computational settings of the access. Az-El values are computed with respect to the default AER frame of the selected object of the Access Tool.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\AER.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Access`
        The STK Access object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation.

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation.

        **step_time** : :obj:`~float`
        The step time for the calculation (the default is 60 seconds).

        **colormap** : :obj:`~matplotlib.colors.Colormap`
        The colormap with which to color the data (the default is None).



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: aer_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.access_graphs import aer_line_chart


