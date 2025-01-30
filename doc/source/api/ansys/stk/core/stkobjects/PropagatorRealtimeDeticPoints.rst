PropagatorRealtimeDeticPoints
=============================

.. py:class:: ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints

   Add one ephemeris point using latitude/longitude/altitude coordinate system.

.. py:currentmodule:: PropagatorRealtimeDeticPoints

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints.add_position`
              - Add an ephemeris point without velocity. Epoch uses DateFormat dimension. Lat uses Latitude dimension. Lon uses Longitude dimension. Alt uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints.add`
              - Add an ephemeris point using position and velocity. Epoch uses DateFormat dimension. Lat uses Latitude dimension. Lon uses Longitude dimension. Alt uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints.add_position_batch`
              - Add data points without velocity information.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints.add_batch`
              - Add data points with velocity information.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorRealtimeDeticPoints



Method detail
-------------

.. py:method:: add_position(self, time: typing.Any, lat: float, lon: float, alt: float) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints.add_position

    Add an ephemeris point without velocity. Epoch uses DateFormat dimension. Lat uses Latitude dimension. Lon uses Longitude dimension. Alt uses Distance dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, time: typing.Any, lat: float, lon: float, alt: float, lat_rate: float, lon_rate: float, alt_rate: float) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints.add

    Add an ephemeris point using position and velocity. Epoch uses DateFormat dimension. Lat uses Latitude dimension. Lon uses Longitude dimension. Alt uses Distance dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`
    **lat_rate** : :obj:`~float`
    **lon_rate** : :obj:`~float`
    **alt_rate** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: add_position_batch(self, times: list, lats: list, lons: list, alts: list) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints.add_position_batch

    Add data points without velocity information.

    :Parameters:

    **times** : :obj:`~list`
    **lats** : :obj:`~list`
    **lons** : :obj:`~list`
    **alts** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: add_batch(self, times: list, lats: list, lons: list, alts: list, lat_rates: list, lon_rates: list, alt_rates: list) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints.add_batch

    Add data points with velocity information.

    :Parameters:

    **times** : :obj:`~list`
    **lats** : :obj:`~list`
    **lons** : :obj:`~list`
    **alts** : :obj:`~list`
    **lat_rates** : :obj:`~list`
    **lon_rates** : :obj:`~list`
    **alt_rates** : :obj:`~list`

    :Returns:

        :obj:`~None`

