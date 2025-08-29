transmitter_spectrum_and_filter_line_chart
==========================================

.. image:: /graph_images_temp/test_transmitter_spectrum_and_filter_line_chart_transmitter.png
  :width: 600
  :alt: image of output from transmitter_spectrum_and_filter_line_chart

.. py:function:: ansys.stk.extensions.data_analysis.graphs.transmitter_graphs.transmitter_spectrum_and_filter_line_chart(stk_object: ~Transmitter, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.transmitter_graphs.transmitter_spectrum_and_filter_line_chart

    Show the spectrum of a modulated RF signal as a function of the frequency across the RF bandwidth of a transmitter.

    It also lists the profile of the transmitter filter magnitude and the profile of the filtered spectrum as modified by the filter.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Transmitter\\Transmitter Spectrum and Filter.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Transmitter`
        The STK Transmitter object.

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


.. py:currentmodule:: transmitter_spectrum_and_filter_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.transmitter_graphs import transmitter_spectrum_and_filter_line_chart


