TerrainCollection
=================

.. py:class:: ansys.stk.core.stkobjects.TerrainCollection

   Bases: 

   Collection of terrain data files available in the Scenario for visualization and analysis.

.. py:currentmodule:: TerrainCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TerrainCollection.item`
              - Given an index, returns an IAgTerrain interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.TerrainCollection.add`
              - Add a terrain item to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TerrainCollection.remove`
              - Remove a given index from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TerrainCollection.remove_all`
              - Remove all items from the collections.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TerrainCollection.count`
              - The number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TerrainCollection._NewEnum`
              - Enumerates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TerrainCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.TerrainCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.TerrainCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> Terrain
    :canonical: ansys.stk.core.stkobjects.TerrainCollection.item

    Given an index, returns an IAgTerrain interface.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~Terrain`

.. py:method:: add(self, location: str, terrainFileType: TERRAIN_FILE_TYPE) -> Terrain
    :canonical: ansys.stk.core.stkobjects.TerrainCollection.add

    Add a terrain item to the collection.

    :Parameters:

    **location** : :obj:`~str`
    **terrainFileType** : :obj:`~TERRAIN_FILE_TYPE`

    :Returns:

        :obj:`~Terrain`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.TerrainCollection.remove

    Remove a given index from the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.TerrainCollection.remove_all

    Remove all items from the collections.

    :Returns:

        :obj:`~None`

