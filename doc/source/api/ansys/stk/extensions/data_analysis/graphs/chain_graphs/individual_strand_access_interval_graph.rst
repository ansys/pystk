individual_strand_access_interval_graph
=======================================

.. image:: /graph_images_temp/test_individual_strand_access_interval_graph_chain.png
  :width: 600
  :alt: image of output from individual_strand_access_interval_graph

.. py:function:: ansys.stk.extensions.data_analysis.graphs.chain_graphs.individual_strand_access_interval_graph(stk_object: ~Chain, start_time: ~typing.Any = None, stop_time: ~typing.Any = None, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.chain_graphs.individual_strand_access_interval_graph

    Create an interval graph of the time intervals for each strand in a Chain that completes the chain.

    Each strand's intervals are graphed on a separate line.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Chain\\Individual Strand Access.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Chain`
        The STK Chain object.

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


.. py:currentmodule:: individual_strand_access_interval_graph


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.chain_graphs import individual_strand_access_interval_graph


