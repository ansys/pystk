IScreenOverlayCollectionBase
============================

.. py:class:: ansys.stk.core.graphics.IScreenOverlayCollectionBase

   object
   
   The common base class for collections of overlays held by screen overlay and by screen overlay manager.

.. py:currentmodule:: IScreenOverlayCollectionBase

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase.item`
              - Get the overlay at the specified index.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase.contains`
              - Determine whether the collection contains a specific overlay.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase.remove`
              - Remove the first occurrence of a specific overlay from the collection.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase.clear`
              - Remove all overlays from the collection.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase.add`
              - Add an overlay to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase.count`
              - Gets the number of screen overlays in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase.is_read_only`
              - Gets a value indicating whether the collection is read-only.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase._NewEnum`
              - Returns an enumerator that iterates through the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IScreenOverlayCollectionBase


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IScreenOverlayCollectionBase.count
    :type: int

    Gets the number of screen overlays in the collection.

.. py:property:: is_read_only
    :canonical: ansys.stk.core.graphics.IScreenOverlayCollectionBase.is_read_only
    :type: bool

    Gets a value indicating whether the collection is read-only.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IScreenOverlayCollectionBase._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that iterates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> IScreenOverlay
    :canonical: ansys.stk.core.graphics.IScreenOverlayCollectionBase.item

    Get the overlay at the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScreenOverlay`


.. py:method:: contains(self, item: IScreenOverlay) -> bool
    :canonical: ansys.stk.core.graphics.IScreenOverlayCollectionBase.contains

    Determine whether the collection contains a specific overlay.

    :Parameters:

    **item** : :obj:`~IScreenOverlay`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, item: IScreenOverlay) -> bool
    :canonical: ansys.stk.core.graphics.IScreenOverlayCollectionBase.remove

    Remove the first occurrence of a specific overlay from the collection.

    :Parameters:

    **item** : :obj:`~IScreenOverlay`

    :Returns:

        :obj:`~bool`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.IScreenOverlayCollectionBase.clear

    Remove all overlays from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, item: IScreenOverlay) -> None
    :canonical: ansys.stk.core.graphics.IScreenOverlayCollectionBase.add

    Add an overlay to the collection.

    :Parameters:

    **item** : :obj:`~IScreenOverlay`

    :Returns:

        :obj:`~None`

