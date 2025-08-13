gi_region_time_to_cover_line_chart
==================================

.. image:: /graph_images_temp/test_gi_region_time_to_cover_line_chart_coveragedefinition.png
  :width: 600
  :alt: image of output from gi_region_time_to_cover_line_chart

.. py:function:: gi_region_time_to_cover_line_chart(stk_object: ~CoverageDefinition, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, step: ~float = 60, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gi_region_time_to_cover_line_chart

    Create a plot of the amount of wait time required, starting from the reported time, before complete coverage of the region selected in the grid inspector occurs.

    The average wait time, compute as the mean of samples, is also plotted. A region is considered to be completely covered if all points within the region have had access to at least one of the assigned assets.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\GI Region Time to Cover.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.CoverageDefinition`
        The STK CoverageDefinition object.

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


.. py:currentmodule:: gi_region_time_to_cover_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs import gi_region_time_to_cover_line_chart


