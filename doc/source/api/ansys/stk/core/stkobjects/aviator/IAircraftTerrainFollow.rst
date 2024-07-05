IAircraftTerrainFollow
======================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollow

   object
   
   Interface used to access the TerrainFollow options for an aircraft in the Aviator catalog.

.. py:currentmodule:: IAircraftTerrainFollow

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollow.get_terrain_follow_by_name`
              - Get the TerrainFollow model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollow.get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftTerrainFollow



Method detail
-------------

.. py:method:: get_terrain_follow_by_name(self, name: str) -> IAircraftTerrainFollowModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollow.get_terrain_follow_by_name

    Get the TerrainFollow model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftTerrainFollowModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollow.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

