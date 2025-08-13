gi_region_full_coverage_interval_graph
======================================

.. image:: /graph_images_temp/test_gi_region_full_coverage_interval_graph_coveragedefinition.png
  :width: 600
  :alt: image of output from gi_region_full_coverage_interval_graph

.. py:function:: gi_region_full_coverage_interval_graph(stk_object: ~CoverageDefinition, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gi_region_full_coverage_interval_graph

    Create an interval graph of the intervals of time when the region selected by the grid inspector is completely covered.

    The region is considered to be completely covered when all points within the region are covered. A point is covered when it has access to some asset.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\GI Region Full Coverage.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.CoverageDefinition`
        The STK CoverageDefinition object.

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


.. py:currentmodule:: gi_region_full_coverage_interval_graph


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs import gi_region_full_coverage_interval_graph


