receiver_filter_line_chart
==========================

.. image:: /graph_images_temp/test_receiver_filter_line_chart_receiver.png
  :width: 600
  :alt: image of output from receiver_filter_line_chart

.. py:function:: receiver_filter_line_chart(stk_object: ~Receiver, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.receiver_graphs.receiver_filter_line_chart

    Show the receiver RF filter magnitude data as a function of receiver bandwidth frequency.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Receiver\\Receiver Filter.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Receiver`
        The STK Receiver object.

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


.. py:currentmodule:: receiver_filter_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.receiver_graphs import receiver_filter_line_chart


