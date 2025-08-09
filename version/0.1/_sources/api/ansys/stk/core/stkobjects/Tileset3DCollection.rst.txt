Tileset3DCollection
===================

.. py:class:: ansys.stk.core.stkobjects.Tileset3DCollection

   Collection of 3DTilesets available in the Scenario for analysis.

.. py:currentmodule:: Tileset3DCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Tileset3DCollection.item`
              - Given an index, returns an Tileset3D interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.Tileset3DCollection.add`
              - Add a 3DTileset item to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Tileset3DCollection.remove`
              - Remove a given index from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Tileset3DCollection.remove_all`
              - Remove all items from the collections.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Tileset3DCollection.count`
              - Get the number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Tileset3DCollection._new_enum`
              - Enumerates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Tileset3DCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.Tileset3DCollection.count
    :type: int

    Get the number of items in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.Tileset3DCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> Tileset3D
    :canonical: ansys.stk.core.stkobjects.Tileset3DCollection.item

    Given an index, returns an Tileset3D interface.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Tileset3D`

.. py:method:: add(self, name: str, uri: str, source_type: Tileset3DSourceType, reference_frame: str) -> Tileset3D
    :canonical: ansys.stk.core.stkobjects.Tileset3DCollection.add

    Add a 3DTileset item to the collection.

    :Parameters:

        **name** : :obj:`~str`

        **uri** : :obj:`~str`

        **source_type** : :obj:`~Tileset3DSourceType`

        **reference_frame** : :obj:`~str`


    :Returns:

        :obj:`~Tileset3D`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.Tileset3DCollection.remove

    Remove a given index from the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.Tileset3DCollection.remove_all

    Remove all items from the collections.

    :Returns:

        :obj:`~None`

