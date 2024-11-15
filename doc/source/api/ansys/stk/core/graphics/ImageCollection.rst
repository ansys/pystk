ImageCollection
===============

.. py:class:: ansys.stk.core.graphics.ImageCollection

   A collection of globe image overlay objects.

.. py:currentmodule:: ImageCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.item`
              - Get the globe image overlay at the specified index.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.contains`
              - Check the presence of a globe image overlay in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.contains_uri_string`
              - Check the presence of a globe image overlay with the specified Uri in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.remove`
              - Remove a globe image overlay from the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.clear`
              - Remove all globe image overlay objects from the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.add`
              - Add imageryOverlay to the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.add_async`
              - Add imageryOverlay to the collection asynchronously.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.index_of`
              - Get the index of the specified globe image overlay.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.index_of_uri_string`
              - Get the index of the globe image overlay with the specified Uri.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.add_uri_string`
              - Create a globe overlay from the uri, which represents a uri, and adds it to the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.add_async_uri_string`
              - Create a globe image overlay from the uri, which represents a uri, and adds it to the collection asynchronously.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.swap`
              - Swap the position of two globe image overlay objects.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.swap_by_index`
              - Swap the position of two globe image overlay objects at the specified indices.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.move`
              - Move the globe image overlay to the specified position.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.move_by_index`
              - Move the globe image overlay at the specified index to the specified position.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.bring_to_front`
              - Brings the globe image overlay to the front of the collection so it is rendered first or on the bottom.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.send_to_back`
              - Send the globe image overlay to the back of the collection so it is rendered last or on the top.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.subscribe`
              - """Return an IImageCollectionEventHandler that is subscribed to handle events associated with this instance of ImageCollection."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.count`
              - Gets the number of globe overlay objects in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection.is_read_only`
              - Gets whether or not the collection is read only.
            * - :py:attr:`~ansys.stk.core.graphics.ImageCollection._new_enum`
              - Constructs an iterator that can be used to iterate the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ImageCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ImageCollection.count
    :type: int

    Gets the number of globe overlay objects in the collection.

.. py:property:: is_read_only
    :canonical: ansys.stk.core.graphics.ImageCollection.is_read_only
    :type: bool

    Gets whether or not the collection is read only.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.ImageCollection._new_enum
    :type: EnumeratorProxy

    Constructs an iterator that can be used to iterate the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> IGlobeImageOverlay
    :canonical: ansys.stk.core.graphics.ImageCollection.item

    Get the globe image overlay at the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IGlobeImageOverlay`


.. py:method:: contains(self, imagery_overlay: IGlobeImageOverlay) -> bool
    :canonical: ansys.stk.core.graphics.ImageCollection.contains

    Check the presence of a globe image overlay in the collection.

    :Parameters:

    **imagery_overlay** : :obj:`~IGlobeImageOverlay`

    :Returns:

        :obj:`~bool`

.. py:method:: contains_uri_string(self, string_uri: str) -> bool
    :canonical: ansys.stk.core.graphics.ImageCollection.contains_uri_string

    Check the presence of a globe image overlay with the specified Uri in the collection.

    :Parameters:

    **string_uri** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, globe_overlay: IGlobeImageOverlay) -> bool
    :canonical: ansys.stk.core.graphics.ImageCollection.remove

    Remove a globe image overlay from the collection.

    :Parameters:

    **globe_overlay** : :obj:`~IGlobeImageOverlay`

    :Returns:

        :obj:`~bool`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.clear

    Remove all globe image overlay objects from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, imagery_overlay: IGlobeImageOverlay) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.add

    Add imageryOverlay to the collection.

    :Parameters:

    **imagery_overlay** : :obj:`~IGlobeImageOverlay`

    :Returns:

        :obj:`~None`

.. py:method:: add_async(self, imagery_overlay: IGlobeImageOverlay) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.add_async

    Add imageryOverlay to the collection asynchronously.

    :Parameters:

    **imagery_overlay** : :obj:`~IGlobeImageOverlay`

    :Returns:

        :obj:`~None`

.. py:method:: index_of(self, imagery_overlay: IGlobeImageOverlay) -> int
    :canonical: ansys.stk.core.graphics.ImageCollection.index_of

    Get the index of the specified globe image overlay.

    :Parameters:

    **imagery_overlay** : :obj:`~IGlobeImageOverlay`

    :Returns:

        :obj:`~int`

.. py:method:: index_of_uri_string(self, string_uri: str) -> int
    :canonical: ansys.stk.core.graphics.ImageCollection.index_of_uri_string

    Get the index of the globe image overlay with the specified Uri.

    :Parameters:

    **string_uri** : :obj:`~str`

    :Returns:

        :obj:`~int`

.. py:method:: add_uri_string(self, uri: str) -> IGlobeImageOverlay
    :canonical: ansys.stk.core.graphics.ImageCollection.add_uri_string

    Create a globe overlay from the uri, which represents a uri, and adds it to the collection.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~IGlobeImageOverlay`

.. py:method:: add_async_uri_string(self, uri: str) -> IGlobeImageOverlay
    :canonical: ansys.stk.core.graphics.ImageCollection.add_async_uri_string

    Create a globe image overlay from the uri, which represents a uri, and adds it to the collection asynchronously.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~IGlobeImageOverlay`

.. py:method:: swap(self, imagery_overlay1: IGlobeImageOverlay, imagery_overlay2: IGlobeImageOverlay) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.swap

    Swap the position of two globe image overlay objects.

    :Parameters:

    **imagery_overlay1** : :obj:`~IGlobeImageOverlay`
    **imagery_overlay2** : :obj:`~IGlobeImageOverlay`

    :Returns:

        :obj:`~None`

.. py:method:: swap_by_index(self, index1: int, index2: int) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.swap_by_index

    Swap the position of two globe image overlay objects at the specified indices.

    :Parameters:

    **index1** : :obj:`~int`
    **index2** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: move(self, imagery_overlay: IGlobeImageOverlay, new_position: int) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.move

    Move the globe image overlay to the specified position.

    :Parameters:

    **imagery_overlay** : :obj:`~IGlobeImageOverlay`
    **new_position** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: move_by_index(self, index: int, new_position: int) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.move_by_index

    Move the globe image overlay at the specified index to the specified position.

    :Parameters:

    **index** : :obj:`~int`
    **new_position** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: bring_to_front(self, imagery_overlay: IGlobeImageOverlay) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.bring_to_front

    Brings the globe image overlay to the front of the collection so it is rendered first or on the bottom.

    :Parameters:

    **imagery_overlay** : :obj:`~IGlobeImageOverlay`

    :Returns:

        :obj:`~None`

.. py:method:: send_to_back(self, imagery_overlay: IGlobeImageOverlay) -> None
    :canonical: ansys.stk.core.graphics.ImageCollection.send_to_back

    Send the globe image overlay to the back of the collection so it is rendered last or on the top.

    :Parameters:

    **imagery_overlay** : :obj:`~IGlobeImageOverlay`

    :Returns:

        :obj:`~None`

