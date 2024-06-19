ITerrainCollection
==================

.. py:class:: ITerrainCollection

   object
   
   IAgTerrainCollection lists all the terrain data files available in this scenario for visualization and analysis.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an IAgTerrain interface.
            * - :py:meth:`~add`
              - Add a terrain item to the collection.
            * - :py:meth:`~remove`
              - Remove a given index from the collection.
            * - :py:meth:`~remove_all`
              - Remove all items from the collections.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITerrainCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ITerrainCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ITerrainCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> ITerrain
    :canonical: ansys.stk.core.stkobjects.ITerrainCollection.item

    Given an index, returns an IAgTerrain interface.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ITerrain`

.. py:method:: add(self, location: str, terrainFileType: TERRAIN_FILE_TYPE) -> ITerrain
    :canonical: ansys.stk.core.stkobjects.ITerrainCollection.add

    Add a terrain item to the collection.

    :Parameters:

    **location** : :obj:`~str`
    **terrainFileType** : :obj:`~TERRAIN_FILE_TYPE`

    :Returns:

        :obj:`~ITerrain`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ITerrainCollection.remove

    Remove a given index from the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.ITerrainCollection.remove_all

    Remove all items from the collections.

    :Returns:

        :obj:`~None`

