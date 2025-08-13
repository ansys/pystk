gi_point_prob_of_coverage_line_chart
====================================

.. image:: /graph_images_temp/test_gi_point_prob_of_coverage_line_chart_coveragedefinition.png
  :width: 600
  :alt: image of output from gi_point_prob_of_coverage_line_chart

.. py:function:: gi_point_prob_of_coverage_line_chart(stk_object: ~CoverageDefinition, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs.gi_point_prob_of_coverage_line_chart

    Create a plot of the probability of coverage being achieved for the point selected in the grid inspector, as a function of the time past a request for coverage.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\CoverageDefinition\\GI Point Prob Of Coverage.rsg`.

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


.. py:currentmodule:: gi_point_prob_of_coverage_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.coverage_definition_graphs import gi_point_prob_of_coverage_line_chart


