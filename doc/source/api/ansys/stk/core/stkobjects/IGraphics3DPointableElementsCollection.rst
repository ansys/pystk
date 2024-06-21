IGraphics3DPointableElementsCollection
======================================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection

   object
   
   List of Pointable Elements.

.. py:currentmodule:: IGraphics3DPointableElementsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.sort`
              - Re-orders pointable elements.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DPointableElementsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IGraphics3DPointableElementsElement
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IGraphics3DPointableElementsElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self) -> IGraphics3DPointableElementsElement
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~IGraphics3DPointableElementsElement`

.. py:method:: sort(self) -> None
    :canonical: ansys.stk.core.stkobjects.IGraphics3DPointableElementsCollection.sort

    Re-orders pointable elements.

    :Returns:

        :obj:`~None`

