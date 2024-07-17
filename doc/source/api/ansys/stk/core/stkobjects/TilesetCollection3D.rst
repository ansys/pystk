TilesetCollection3D
===================

.. py:class:: ansys.stk.core.stkobjects.TilesetCollection3D

   Bases: 

   Collection of 3DTilesets available in the Scenario for analysis.

.. py:currentmodule:: TilesetCollection3D

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TilesetCollection3D.item`
              - Given an index, returns an IAg3DTileset interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.TilesetCollection3D.add`
              - Add a 3DTileset item to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TilesetCollection3D.remove`
              - Remove a given index from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TilesetCollection3D.remove_all`
              - Remove all items from the collections.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TilesetCollection3D.count`
              - Get the number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TilesetCollection3D._NewEnum`
              - Enumerates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TilesetCollection3D


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.TilesetCollection3D.count
    :type: int

    Get the number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.TilesetCollection3D._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> Tileset3D
    :canonical: ansys.stk.core.stkobjects.TilesetCollection3D.item

    Given an index, returns an IAg3DTileset interface.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~Tileset3D`

.. py:method:: add(self, name: str, uRI: str, sourceType: TILESET_3D_SOURCE_TYPE, referenceFrame: str) -> Tileset3D
    :canonical: ansys.stk.core.stkobjects.TilesetCollection3D.add

    Add a 3DTileset item to the collection.

    :Parameters:

    **name** : :obj:`~str`
    **uRI** : :obj:`~str`
    **sourceType** : :obj:`~TILESET_3D_SOURCE_TYPE`
    **referenceFrame** : :obj:`~str`

    :Returns:

        :obj:`~Tileset3D`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.TilesetCollection3D.remove

    Remove a given index from the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.TilesetCollection3D.remove_all

    Remove all items from the collections.

    :Returns:

        :obj:`~None`

