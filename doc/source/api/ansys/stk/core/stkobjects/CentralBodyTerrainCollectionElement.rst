CentralBodyTerrainCollectionElement
===================================

.. py:class:: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement

   Bases: 

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
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_extent_max_resolution`
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
    :type: ITerrainCollection

    Terrain collection.


Method detail
-------------



.. py:method:: get_altitude(self, lat: typing.Any, lon: typing.Any, altRef: ALTITUDE_REFERENCE_TYPE) -> float
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitude

    Return the altitude at the specified position relative to the input reference surface. If the specified position is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is returned.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`
    **altRef** : :obj:`~ALTITUDE_REFERENCE_TYPE`

    :Returns:

        :obj:`~float`

.. py:method:: get_altitude_batch(self, latLons: list, altRef: ALTITUDE_REFERENCE_TYPE) -> list
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitude_batch

    Return the altitudes at the specified position array relative to the input reference surface. If a specified position is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is used.

    :Parameters:

    **latLons** : :obj:`~list`
    **altRef** : :obj:`~ALTITUDE_REFERENCE_TYPE`

    :Returns:

        :obj:`~list`

.. py:method:: get_altitudes_between_points_at_resolution(self, sWLatitude: typing.Any, sWLongitude: typing.Any, nELatitude: typing.Any, nELongitude: typing.Any, stepSize: typing.Any, distanceType: DISTANCE_ON_SPHERE, altRef: ALTITUDE_REFERENCE_TYPE) -> list
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_altitudes_between_points_at_resolution

    Return the terrain profile at the specified resolution relative to the input reference surface. If a position along the profile is outside terrain sources, the altitude of 0.0 relative to the default reference ellipsoid (WGS84 for Earth) is used.

    :Parameters:

    **sWLatitude** : :obj:`~typing.Any`
    **sWLongitude** : :obj:`~typing.Any`
    **nELatitude** : :obj:`~typing.Any`
    **nELongitude** : :obj:`~typing.Any`
    **stepSize** : :obj:`~typing.Any`
    **distanceType** : :obj:`~DISTANCE_ON_SPHERE`
    **altRef** : :obj:`~ALTITUDE_REFERENCE_TYPE`

    :Returns:

        :obj:`~list`

.. py:method:: get_extent_max_resolution(self, sWLatitude: typing.Any, sWLongitude: typing.Any, nELatitude: typing.Any, nELongitude: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement.get_extent_max_resolution

    Return the highest resolution for any terrain that overlaps the specified rectangle.

    :Parameters:

    **sWLatitude** : :obj:`~typing.Any`
    **sWLongitude** : :obj:`~typing.Any`
    **nELatitude** : :obj:`~typing.Any`
    **nELongitude** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

