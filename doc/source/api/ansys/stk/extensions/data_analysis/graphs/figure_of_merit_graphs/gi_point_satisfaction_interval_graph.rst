gi_point_satisfaction_interval_graph
====================================

.. image:: /graph_images_temp/test_gi_point_satisfaction_interval_graph_figureofmerit.png
  :width: 600
  :alt: image of output from gi_point_satisfaction_interval_graph

.. py:function:: ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.gi_point_satisfaction_interval_graph(stk_object: ~FigureOfMerit, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs.gi_point_satisfaction_interval_graph

    Create an interval graph of the satisfaction intervals for the point currently selected via the figure of merit grid inspector.

    Satisfaction intervals are defined as periods when a grid point achieves the defined satisfaction criteria associated with the FOM.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\FigureOfMerit\\GI Point Satisfaction.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.FigureOfMerit`
        The STK FigureOfMerit object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation (the default is None, which implies using the scenario start time).

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation (the default is None, which implies using the scenario stop time).

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


.. py:currentmodule:: gi_point_satisfaction_interval_graph


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs import gi_point_satisfaction_interval_graph


