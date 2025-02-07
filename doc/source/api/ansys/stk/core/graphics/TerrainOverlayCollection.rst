TerrainOverlayCollection
========================

.. py:class:: ansys.stk.core.graphics.TerrainOverlayCollection

   A collection of terrain overlay objects.

.. py:currentmodule:: TerrainOverlayCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.item`
              - Get the terrain overlay at the specified index.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.contains`
              - Check the presence of a terrain overlay in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.contains_uri_string`
              - Check the presence of a terrain overlay with the specified Uri in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.remove`
              - Remove a terrain overlay from the collection.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.clear`
              - Remove all terrain overlay objects from the collection.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.add`
              - Add terrainOverlay to the collection.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.add_async`
              - Add terrainOverlay to the collection asynchronously.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.index_of`
              - Get the index of the specified terrain overlay.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.index_of_uri_string`
              - Get the index of the terrain overlay with the specified Uri.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.add_uri_string`
              - Create a terrain overlay from the uri, which represents a uri, and adds it to the collection.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.add_async_uri_string`
              - Create a terrain overlay from the uri, which represents a uri, and adds it to the collection asynchronously.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.swap`
              - Swap the position of two terrain overlay objects.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.swap_by_index`
              - Swap the position of two terrain overlay objects at the specified indices.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.move`
              - Move the terrain overlay to the specified position.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.move_by_index`
              - Move the terrain overlay at the specified index to the specified position.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.bring_to_front`
              - Brings the terrain overlay to the front of the collection so it is rendered first or on the bottom.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.send_to_back`
              - Send the terrain overlay to the back of the collection so it is rendered last or on the top.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.subscribe`
              - """Return an ITerrainOverlayCollectionEventHandler that is subscribed to handle events associated with this instance of TerrainOverlayCollection."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.count`
              - Get the number of terrain overlay objects in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection.is_read_only`
              - Get whether or not the collection is read only.
            * - :py:attr:`~ansys.stk.core.graphics.TerrainOverlayCollection._new_enum`
              - Construct an iterator that can be used to iterate the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TerrainOverlayCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.count
    :type: int

    Get the number of terrain overlay objects in the collection.

.. py:property:: is_read_only
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.is_read_only
    :type: bool

    Get whether or not the collection is read only.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection._new_enum
    :type: EnumeratorProxy

    Construct an iterator that can be used to iterate the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> ITerrainOverlay
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.item

    Get the terrain overlay at the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ITerrainOverlay`


.. py:method:: contains(self, terrain_overlay: ITerrainOverlay) -> bool
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.contains

    Check the presence of a terrain overlay in the collection.

    :Parameters:

    **terrain_overlay** : :obj:`~ITerrainOverlay`

    :Returns:

        :obj:`~bool`

.. py:method:: contains_uri_string(self, string_uri: str) -> bool
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.contains_uri_string

    Check the presence of a terrain overlay with the specified Uri in the collection.

    :Parameters:

    **string_uri** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, terrain_overlay: ITerrainOverlay) -> bool
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.remove

    Remove a terrain overlay from the collection.

    :Parameters:

    **terrain_overlay** : :obj:`~ITerrainOverlay`

    :Returns:

        :obj:`~bool`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.clear

    Remove all terrain overlay objects from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, terrain_overlay: ITerrainOverlay) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.add

    Add terrainOverlay to the collection.

    :Parameters:

    **terrain_overlay** : :obj:`~ITerrainOverlay`

    :Returns:

        :obj:`~None`

.. py:method:: add_async(self, terrain_overlay: ITerrainOverlay) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.add_async

    Add terrainOverlay to the collection asynchronously.

    :Parameters:

    **terrain_overlay** : :obj:`~ITerrainOverlay`

    :Returns:

        :obj:`~None`

.. py:method:: index_of(self, terrain_overlay: ITerrainOverlay) -> int
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.index_of

    Get the index of the specified terrain overlay.

    :Parameters:

    **terrain_overlay** : :obj:`~ITerrainOverlay`

    :Returns:

        :obj:`~int`

.. py:method:: index_of_uri_string(self, string_uri: str) -> int
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.index_of_uri_string

    Get the index of the terrain overlay with the specified Uri.

    :Parameters:

    **string_uri** : :obj:`~str`

    :Returns:

        :obj:`~int`

.. py:method:: add_uri_string(self, uri: str) -> ITerrainOverlay
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.add_uri_string

    Create a terrain overlay from the uri, which represents a uri, and adds it to the collection.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~ITerrainOverlay`

.. py:method:: add_async_uri_string(self, uri: str) -> ITerrainOverlay
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.add_async_uri_string

    Create a terrain overlay from the uri, which represents a uri, and adds it to the collection asynchronously.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~ITerrainOverlay`

.. py:method:: swap(self, terrain_overlay1: ITerrainOverlay, terrain_overlay2: ITerrainOverlay) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.swap

    Swap the position of two terrain overlay objects.

    :Parameters:

    **terrain_overlay1** : :obj:`~ITerrainOverlay`
    **terrain_overlay2** : :obj:`~ITerrainOverlay`

    :Returns:

        :obj:`~None`

.. py:method:: swap_by_index(self, index1: int, index2: int) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.swap_by_index

    Swap the position of two terrain overlay objects at the specified indices.

    :Parameters:

    **index1** : :obj:`~int`
    **index2** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: move(self, terrain_overlay: ITerrainOverlay, new_position: int) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.move

    Move the terrain overlay to the specified position.

    :Parameters:

    **terrain_overlay** : :obj:`~ITerrainOverlay`
    **new_position** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: move_by_index(self, index: int, new_position: int) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.move_by_index

    Move the terrain overlay at the specified index to the specified position.

    :Parameters:

    **index** : :obj:`~int`
    **new_position** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: bring_to_front(self, terrain_overlay: ITerrainOverlay) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.bring_to_front

    Brings the terrain overlay to the front of the collection so it is rendered first or on the bottom.

    :Parameters:

    **terrain_overlay** : :obj:`~ITerrainOverlay`

    :Returns:

        :obj:`~None`

.. py:method:: send_to_back(self, terrain_overlay: ITerrainOverlay) -> None
    :canonical: ansys.stk.core.graphics.TerrainOverlayCollection.send_to_back

    Send the terrain overlay to the back of the collection so it is rendered last or on the top.

    :Parameters:

    **terrain_overlay** : :obj:`~ITerrainOverlay`

    :Returns:

        :obj:`~None`

