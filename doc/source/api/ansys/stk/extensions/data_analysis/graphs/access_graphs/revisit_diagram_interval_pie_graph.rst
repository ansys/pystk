revisit_diagram_interval_pie_graph
==================================

.. py:function:: revisit_diagram_interval_pie_graph(stk_obj: ~Access, start_time: ~typing.Any = None, stop_time: ~typing.Any = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.access_graphs.revisit_diagram_interval_pie_graph

    Create pie chart showing the durations of access intervals and access gap intervals.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Access\\Revisit Diagram.rsg`.

    :Parameters:

        **stk_obj** : :obj:`~ansys.stk.core.stkobjects.Access`
        The STK Access object.

        **start_time** : :obj:`~typing.Any`
        The start time of the calculation.

        **stop_time** : :obj:`~typing.Any`
        The stop time of the calculation.



    :Returns:

        :obj:`~matplotlib.figure.Figure`
        The newly created figure.

        :obj:`~matplotlib.axes.Axes`
        The newly created axes.


.. py:currentmodule:: revisit_diagram_interval_pie_graph


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.access_graphs import revisit_diagram_interval_pie_graph


