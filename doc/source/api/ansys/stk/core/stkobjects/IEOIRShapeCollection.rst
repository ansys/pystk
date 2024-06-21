IEOIRShapeCollection
====================

.. py:class:: ansys.stk.core.stkobjects.IEOIRShapeCollection

   object
   
   IAgEOIRShapeCollection Interface.

.. py:currentmodule:: IEOIRShapeCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IEOIRShapeCollection.item`
              - Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IEOIRShapeCollection.add`
              - Add an element at the end of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IEOIRShapeCollection.remove_at`
              - Remove an element at the given index in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IEOIRShapeCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IEOIRShapeCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IEOIRShapeCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IEOIRShapeCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IEOIRShapeCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IEOIRShape
    :canonical: ansys.stk.core.stkobjects.IEOIRShapeCollection.item

    Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IEOIRShape`

.. py:method:: add(self) -> IEOIRShape
    :canonical: ansys.stk.core.stkobjects.IEOIRShapeCollection.add

    Add an element at the end of the collection.

    :Returns:

        :obj:`~IEOIRShape`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IEOIRShapeCollection.remove_at

    Remove an element at the given index in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`



