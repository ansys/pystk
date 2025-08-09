PropagatorRealtimeUTMPoints
===========================

.. py:class:: ansys.stk.core.stkobjects.PropagatorRealtimeUTMPoints

   Add one ephemeris point.

.. py:currentmodule:: PropagatorRealtimeUTMPoints

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimeUTMPoints.add_position`
              - Add an ephemeris point using position only. Valid values for <ZoneStr> are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in Distance.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtimeUTMPoints.add`
              - Add an ephemeris point. Valid values for <ZoneStr> are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in Distance. LonRate and LatRate are entered in degrees/second. AltRate is entered in Distance/second.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorRealtimeUTMPoints



Method detail
-------------

.. py:method:: add_position(self, time: typing.Any, zone_str: str, easting: float, northing: float, alt: float) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimeUTMPoints.add_position

    Add an ephemeris point using position only. Valid values for <ZoneStr> are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in Distance.

    :Parameters:

        **time** : :obj:`~typing.Any`

        **zone_str** : :obj:`~str`

        **easting** : :obj:`~float`

        **northing** : :obj:`~float`

        **alt** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: add(self, time: typing.Any, zone_str: str, easting: float, northing: float, alt: float, lon_rate: float, lat_rate: float, alt_rate: float) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtimeUTMPoints.add

    Add an ephemeris point. Valid values for <ZoneStr> are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in Distance. LonRate and LatRate are entered in degrees/second. AltRate is entered in Distance/second.

    :Parameters:

        **time** : :obj:`~typing.Any`

        **zone_str** : :obj:`~str`

        **easting** : :obj:`~float`

        **northing** : :obj:`~float`

        **alt** : :obj:`~float`

        **lon_rate** : :obj:`~float`

        **lat_rate** : :obj:`~float`

        **alt_rate** : :obj:`~float`


    :Returns:

        :obj:`~None`

