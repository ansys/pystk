IVehicleRealtimeUTMPoints
=========================

.. py:class:: IVehicleRealtimeUTMPoints

   object
   
   Add one ephemeris point.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add_position`
              - Add an ephemeris point using position only. Valid values for <ZoneStr> are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in Distance.
            * - :py:meth:`~add`
              - Add an ephemeris point. Valid values for <ZoneStr> are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in Distance. LonRate and LatRate are entered in degrees/second. AltRate is entered in Distance/second.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleRealtimeUTMPoints



Method detail
-------------

.. py:method:: add_position(self, time:typing.Any, zoneStr:str, easting:float, northing:float, alt:float) -> None

    Add an ephemeris point using position only. Valid values for <ZoneStr> are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in Distance.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **zoneStr** : :obj:`~str`
    **easting** : :obj:`~float`
    **northing** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, time:typing.Any, zoneStr:str, easting:float, northing:float, alt:float, lonRate:float, latRate:float, altRate:float) -> None

    Add an ephemeris point. Valid values for <ZoneStr> are A, B, Y, Z or ddc, where 00<dd<61 and c is C-X. Easting, Northing and Alt are entered in Distance. LonRate and LatRate are entered in degrees/second. AltRate is entered in Distance/second.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **zoneStr** : :obj:`~str`
    **easting** : :obj:`~float`
    **northing** : :obj:`~float`
    **alt** : :obj:`~float`
    **lonRate** : :obj:`~float`
    **latRate** : :obj:`~float`
    **altRate** : :obj:`~float`

    :Returns:

        :obj:`~None`

