ITerrainOverlayCollection
=========================

.. py:class:: ITerrainOverlayCollection

   object
   
   A collection of terrain overlay objects.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the terrain overlay at the specified index.
            * - :py:meth:`~contains`
              - Check the presence of a terrain overlay in the collection.
            * - :py:meth:`~contains_uri_string`
              - Check the presence of a terrain overlay with the specified Uri in the collection.
            * - :py:meth:`~remove`
              - Remove a terrain overlay from the collection.
            * - :py:meth:`~clear`
              - Remove all terrain overlay objects from the collection.
            * - :py:meth:`~add`
              - Add terrainOverlay to the collection.
            * - :py:meth:`~add_async`
              - Add terrainOverlay to the collection asynchronously.
            * - :py:meth:`~index_of`
              - Get the index of the specified terrain overlay.
            * - :py:meth:`~index_of_uri_string`
              - Get the index of the terrain overlay with the specified Uri.
            * - :py:meth:`~add_uri_string`
              - Create a terrain overlay from the uri, which represents a uri, and adds it to the collection.
            * - :py:meth:`~add_async_uri_string`
              - Create a terrain overlay from the uri, which represents a uri, and adds it to the collection asynchronously.
            * - :py:meth:`~swap`
              - Swap the position of two terrain overlay objects.
            * - :py:meth:`~swap_by_index`
              - Swap the position of two terrain overlay objects at the specified indices.
            * - :py:meth:`~move`
              - Move the terrain overlay to the specified position.
            * - :py:meth:`~move_by_index`
              - Move the terrain overlay at the specified index to the specified position.
            * - :py:meth:`~bring_to_front`
              - Brings the terrain overlay to the front of the collection so it is rendered first or on the bottom.
            * - :py:meth:`~send_to_back`
              - Send the terrain overlay to the back of the collection so it is rendered last or on the top.
            * - :py:meth:`~Subscribe`
              - """Return an ITerrainOverlayCollectionEventHandler that is subscribed to handle events associated with this instance of ITerrainOverlayCollection."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~is_read_only`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITerrainOverlayCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ITerrainOverlayCollection.count
    :type: int

    Gets the number of terrain overlay objects in the collection.

.. py:property:: is_read_only
    :canonical: ansys.stk.core.graphics.ITerrainOverlayCollection.is_read_only
    :type: bool

    Gets whether or not the collection is read only.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.ITerrainOverlayCollection._NewEnum
    :type: EnumeratorProxy

    Constructs an iterator that can be used to iterate the collection.


Method detail
-------------



.. py:method:: item(self, index:int) -> "ITerrainOverlay"

    Get the terrain overlay at the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"ITerrainOverlay"`


.. py:method:: contains(self, terrainOverlay:"ITerrainOverlay") -> bool

    Check the presence of a terrain overlay in the collection.

    :Parameters:

    **terrainOverlay** : :obj:`~"ITerrainOverlay"`

    :Returns:

        :obj:`~bool`

.. py:method:: contains_uri_string(self, stringUri:str) -> bool

    Check the presence of a terrain overlay with the specified Uri in the collection.

    :Parameters:

    **stringUri** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, terrainOverlay:"ITerrainOverlay") -> bool

    Remove a terrain overlay from the collection.

    :Parameters:

    **terrainOverlay** : :obj:`~"ITerrainOverlay"`

    :Returns:

        :obj:`~bool`

.. py:method:: clear(self) -> None

    Remove all terrain overlay objects from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, terrainOverlay:"ITerrainOverlay") -> None

    Add terrainOverlay to the collection.

    :Parameters:

    **terrainOverlay** : :obj:`~"ITerrainOverlay"`

    :Returns:

        :obj:`~None`

.. py:method:: add_async(self, terrainOverlay:"ITerrainOverlay") -> None

    Add terrainOverlay to the collection asynchronously.

    :Parameters:

    **terrainOverlay** : :obj:`~"ITerrainOverlay"`

    :Returns:

        :obj:`~None`

.. py:method:: index_of(self, terrainOverlay:"ITerrainOverlay") -> int

    Get the index of the specified terrain overlay.

    :Parameters:

    **terrainOverlay** : :obj:`~"ITerrainOverlay"`

    :Returns:

        :obj:`~int`

.. py:method:: index_of_uri_string(self, stringUri:str) -> int

    Get the index of the terrain overlay with the specified Uri.

    :Parameters:

    **stringUri** : :obj:`~str`

    :Returns:

        :obj:`~int`

.. py:method:: add_uri_string(self, uri:str) -> "ITerrainOverlay"

    Create a terrain overlay from the uri, which represents a uri, and adds it to the collection.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~"ITerrainOverlay"`

.. py:method:: add_async_uri_string(self, uri:str) -> "ITerrainOverlay"

    Create a terrain overlay from the uri, which represents a uri, and adds it to the collection asynchronously.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~"ITerrainOverlay"`

.. py:method:: swap(self, terrainOverlay1:"ITerrainOverlay", terrainOverlay2:"ITerrainOverlay") -> None

    Swap the position of two terrain overlay objects.

    :Parameters:

    **terrainOverlay1** : :obj:`~"ITerrainOverlay"`
    **terrainOverlay2** : :obj:`~"ITerrainOverlay"`

    :Returns:

        :obj:`~None`

.. py:method:: swap_by_index(self, index1:int, index2:int) -> None

    Swap the position of two terrain overlay objects at the specified indices.

    :Parameters:

    **index1** : :obj:`~int`
    **index2** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: move(self, terrainOverlay:"ITerrainOverlay", newPosition:int) -> None

    Move the terrain overlay to the specified position.

    :Parameters:

    **terrainOverlay** : :obj:`~"ITerrainOverlay"`
    **newPosition** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: move_by_index(self, index:int, newPosition:int) -> None

    Move the terrain overlay at the specified index to the specified position.

    :Parameters:

    **index** : :obj:`~int`
    **newPosition** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: bring_to_front(self, terrainOverlay:"ITerrainOverlay") -> None

    Brings the terrain overlay to the front of the collection so it is rendered first or on the bottom.

    :Parameters:

    **terrainOverlay** : :obj:`~"ITerrainOverlay"`

    :Returns:

        :obj:`~None`

.. py:method:: send_to_back(self, terrainOverlay:"ITerrainOverlay") -> None

    Send the terrain overlay to the back of the collection so it is rendered last or on the top.

    :Parameters:

    **terrainOverlay** : :obj:`~"ITerrainOverlay"`

    :Returns:

        :obj:`~None`

