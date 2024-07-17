AircraftTerrainFollow
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollow

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the TerrainFollow category of an Aviator aircraft.

.. py:currentmodule:: AircraftTerrainFollow

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollow.get_terrain_follow_by_name`
              - Get the TerrainFollow model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollow.get_as_catalog_item`
              - Get the catalog item interface for this object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftTerrainFollow



Method detail
-------------

.. py:method:: get_terrain_follow_by_name(self, name: str) -> AircraftTerrainFollowModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollow.get_terrain_follow_by_name

    Get the TerrainFollow model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftTerrainFollowModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollow.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

