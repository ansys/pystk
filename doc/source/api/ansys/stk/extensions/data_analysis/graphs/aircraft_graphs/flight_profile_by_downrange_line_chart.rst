flight_profile_by_downrange_line_chart
======================================

.. py:function:: flight_profile_by_downrange_line_chart(stk_object: ~Aircraft, colormap: ~matplotlib.colors.Colormap = None, time_unit_abbreviation: ~str = 'UTCG', formatter: collections.abc.Callable[[float, float], str] = None) -> ~matplotlib.figure.Figure, ~matplotlib.axes.Axes
    :canonical: ansys.stk.extensions.data_analysis.graphs.aircraft_graphs.flight_profile_by_downrange_line_chart

    Create a plot of altitude and true air speed as a function of downrange distance.

    This graph wrapper was generated from `AGI\\STK12\\STKData\\Styles\\Aircraft\\Flight Profile by DownRange.rsg`.

    :Parameters:

        **stk_object** : :obj:`~ansys.stk.core.stkobjects.Aircraft`
        The STK Aircraft object.

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


.. py:currentmodule:: flight_profile_by_downrange_line_chart


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.aircraft_graphs import flight_profile_by_downrange_line_chart


