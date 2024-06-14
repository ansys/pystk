IImageCollection
================

.. py:class:: IImageCollection

   object
   
   A collection of globe image overlay objects.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the globe image overlay at the specified index.
            * - :py:meth:`~contains`
              - Check the presence of a globe image overlay in the collection.
            * - :py:meth:`~contains_uri_string`
              - Check the presence of a globe image overlay with the specified Uri in the collection.
            * - :py:meth:`~remove`
              - Remove a globe image overlay from the collection.
            * - :py:meth:`~clear`
              - Remove all globe image overlay objects from the collection.
            * - :py:meth:`~add`
              - Add imageryOverlay to the collection.
            * - :py:meth:`~add_async`
              - Add imageryOverlay to the collection asynchronously.
            * - :py:meth:`~index_of`
              - Get the index of the specified globe image overlay.
            * - :py:meth:`~index_of_uri_string`
              - Get the index of the globe image overlay with the specified Uri.
            * - :py:meth:`~add_uri_string`
              - Create a globe overlay from the uri, which represents a uri, and adds it to the collection.
            * - :py:meth:`~add_async_uri_string`
              - Create a globe image overlay from the uri, which represents a uri, and adds it to the collection asynchronously.
            * - :py:meth:`~swap`
              - Swap the position of two globe image overlay objects.
            * - :py:meth:`~swap_by_index`
              - Swap the position of two globe image overlay objects at the specified indices.
            * - :py:meth:`~move`
              - Move the globe image overlay to the specified position.
            * - :py:meth:`~move_by_index`
              - Move the globe image overlay at the specified index to the specified position.
            * - :py:meth:`~bring_to_front`
              - Brings the globe image overlay to the front of the collection so it is rendered first or on the bottom.
            * - :py:meth:`~send_to_back`
              - Send the globe image overlay to the back of the collection so it is rendered last or on the top.
            * - :py:meth:`~Subscribe`
              - """Return an IImageCollectionEventHandler that is subscribed to handle events associated with this instance of IImageCollection."""

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

    from ansys.stk.core.graphics import IImageCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IImageCollection.count
    :type: int

    Gets the number of globe overlay objects in the collection.

.. py:property:: is_read_only
    :canonical: ansys.stk.core.graphics.IImageCollection.is_read_only
    :type: bool

    Gets whether or not the collection is read only.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IImageCollection._NewEnum
    :type: EnumeratorProxy

    Constructs an iterator that can be used to iterate the collection.


Method detail
-------------



.. py:method:: item(self, index:int) -> "IGlobeImageOverlay"

    Get the globe image overlay at the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IGlobeImageOverlay"`


.. py:method:: contains(self, imageryOverlay:"IGlobeImageOverlay") -> bool

    Check the presence of a globe image overlay in the collection.

    :Parameters:

    **imageryOverlay** : :obj:`~"IGlobeImageOverlay"`

    :Returns:

        :obj:`~bool`

.. py:method:: contains_uri_string(self, stringUri:str) -> bool

    Check the presence of a globe image overlay with the specified Uri in the collection.

    :Parameters:

    **stringUri** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, globeOverlay:"IGlobeImageOverlay") -> bool

    Remove a globe image overlay from the collection.

    :Parameters:

    **globeOverlay** : :obj:`~"IGlobeImageOverlay"`

    :Returns:

        :obj:`~bool`

.. py:method:: clear(self) -> None

    Remove all globe image overlay objects from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, imageryOverlay:"IGlobeImageOverlay") -> None

    Add imageryOverlay to the collection.

    :Parameters:

    **imageryOverlay** : :obj:`~"IGlobeImageOverlay"`

    :Returns:

        :obj:`~None`

.. py:method:: add_async(self, imageryOverlay:"IGlobeImageOverlay") -> None

    Add imageryOverlay to the collection asynchronously.

    :Parameters:

    **imageryOverlay** : :obj:`~"IGlobeImageOverlay"`

    :Returns:

        :obj:`~None`

.. py:method:: index_of(self, imageryOverlay:"IGlobeImageOverlay") -> int

    Get the index of the specified globe image overlay.

    :Parameters:

    **imageryOverlay** : :obj:`~"IGlobeImageOverlay"`

    :Returns:

        :obj:`~int`

.. py:method:: index_of_uri_string(self, stringUri:str) -> int

    Get the index of the globe image overlay with the specified Uri.

    :Parameters:

    **stringUri** : :obj:`~str`

    :Returns:

        :obj:`~int`

.. py:method:: add_uri_string(self, uri:str) -> "IGlobeImageOverlay"

    Create a globe overlay from the uri, which represents a uri, and adds it to the collection.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~"IGlobeImageOverlay"`

.. py:method:: add_async_uri_string(self, uri:str) -> "IGlobeImageOverlay"

    Create a globe image overlay from the uri, which represents a uri, and adds it to the collection asynchronously.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~"IGlobeImageOverlay"`

.. py:method:: swap(self, imageryOverlay1:"IGlobeImageOverlay", imageryOverlay2:"IGlobeImageOverlay") -> None

    Swap the position of two globe image overlay objects.

    :Parameters:

    **imageryOverlay1** : :obj:`~"IGlobeImageOverlay"`
    **imageryOverlay2** : :obj:`~"IGlobeImageOverlay"`

    :Returns:

        :obj:`~None`

.. py:method:: swap_by_index(self, index1:int, index2:int) -> None

    Swap the position of two globe image overlay objects at the specified indices.

    :Parameters:

    **index1** : :obj:`~int`
    **index2** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: move(self, imageryOverlay:"IGlobeImageOverlay", newPosition:int) -> None

    Move the globe image overlay to the specified position.

    :Parameters:

    **imageryOverlay** : :obj:`~"IGlobeImageOverlay"`
    **newPosition** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: move_by_index(self, index:int, newPosition:int) -> None

    Move the globe image overlay at the specified index to the specified position.

    :Parameters:

    **index** : :obj:`~int`
    **newPosition** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: bring_to_front(self, imageryOverlay:"IGlobeImageOverlay") -> None

    Brings the globe image overlay to the front of the collection so it is rendered first or on the bottom.

    :Parameters:

    **imageryOverlay** : :obj:`~"IGlobeImageOverlay"`

    :Returns:

        :obj:`~None`

.. py:method:: send_to_back(self, imageryOverlay:"IGlobeImageOverlay") -> None

    Send the globe image overlay to the back of the collection so it is rendered last or on the top.

    :Parameters:

    **imageryOverlay** : :obj:`~"IGlobeImageOverlay"`

    :Returns:

        :obj:`~None`

