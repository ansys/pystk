gap_duration_line_chart
=======================

.. image:: /graph_images_temp/test_gap_duration_line_chart_coveragedefinition.png
  :width: 600
  :alt: image of output from gap_duration_line_chart

.. py:function:: ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gap_duration_line_chart(stk_object: ~CoverageDefinition, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gap_duration_line_chart

    Create a plot of the cumulative distribution of the access duration gaps of all grid points.

    For each grid point, access intervals to each assigned asset are combined to determine the time intervals over which at least one asset has access to the grid point. The durations of the gaps between these intervals, for all grid points, are then sorted from smallest to largest and the percentages are then plotted.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\Gap Duration.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.CoverageDefinition`
        The STK CoverageDefinition object.

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


.. py:currentmodule:: gap_duration_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs import gap_duration_line_chart


