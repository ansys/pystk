CentralBodyTerrainCollectionElement
===================================

.. py:class:: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement

   Element of collection of terrain associated with central body.

.. py:currentmodule:: CentralBodyTerrainCollectionElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitude`
              - Return the altitude at the specified position relative to the input reference surface. If the specified position is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is returned.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitude_batch`
              - Return the altitudes at the specified position array relative to the input reference surface. If a specified position is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is used.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitudes_between_points_at_resolution`
              - Return the terrain profile at the specified resolution relative to the input reference surface. If a position along the profile is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is used.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_extent_maximum_resolution`
              - Return the highest resolution for any terrain that overlaps the specified rectangle.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.central_body`
              - Name of central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.terrain_collection`
              - Terrain collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CentralBodyTerrainCollectionElement


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.central_body
    :type: str

    Name of central body.

.. py:property:: terrain_collection
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.terrain_collection
    :type: TerrainCollection

    Terrain collection.


Method detail
-------------


.. py:method:: get_altitude(self, lat: typing.Any, lon: typing.Any, alt_ref: AltitudeReferenceType) -> float
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitude

    Return the altitude at the specified position relative to the input reference surface. If the specified position is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is returned.

    :Parameters:

        **lat** : :obj:`~typing.Any`

        **lon** : :obj:`~typing.Any`

        **alt_ref** : :obj:`~AltitudeReferenceType`


    :Returns:

        :obj:`~float`

.. py:method:: get_altitude_batch(self, lat_lons: list, alt_ref: AltitudeReferenceType) -> list
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitude_batch

    Return the altitudes at the specified position array relative to the input reference surface. If a specified position is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is used.

    :Parameters:

        **lat_lons** : :obj:`~list`

        **alt_ref** : :obj:`~AltitudeReferenceType`


    :Returns:

        :obj:`~list`

.. py:method:: get_altitudes_between_points_at_resolution(self, southwest_latitude: typing.Any, southwest_longitude: typing.Any, northeast_latitude: typing.Any, northeast_longitude: typing.Any, step_size: typing.Any, distance_type: DistanceOnSphere, alt_ref: AltitudeReferenceType) -> list
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitudes_between_points_at_resolution

    Return the terrain profile at the specified resolution relative to the input reference surface. If a position along the profile is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is used.

    :Parameters:

        **southwest_latitude** : :obj:`~typing.Any`

        **southwest_longitude** : :obj:`~typing.Any`

        **northeast_latitude** : :obj:`~typing.Any`

        **northeast_longitude** : :obj:`~typing.Any`

        **step_size** : :obj:`~typing.Any`

        **distance_type** : :obj:`~DistanceOnSphere`

        **alt_ref** : :obj:`~AltitudeReferenceType`


    :Returns:

        :obj:`~list`

.. py:method:: get_extent_maximum_resolution(self, southwest_latitude: typing.Any, southwest_longitude: typing.Any, northeast_latitude: typing.Any, northeast_longitude: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_extent_maximum_resolution

    Return the highest resolution for any terrain that overlaps the specified rectangle.

    :Parameters:

        **southwest_latitude** : :obj:`~typing.Any`

        **southwest_longitude** : :obj:`~typing.Any`

        **northeast_latitude** : :obj:`~typing.Any`

        **northeast_longitude** : :obj:`~typing.Any`


    :Returns:

        :obj:`~float`


