IEOIRShapeCollection
====================

.. py:class:: IEOIRShapeCollection

   object
   
   IAgEOIRShapeCollection Interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:meth:`~add`
              - Add an element at the end of the collection.
            * - :py:meth:`~remove_at`
              - Remove an element at the given index in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


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

.. py:method:: item(self, index:int) -> "IEOIRShape"

    Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IEOIRShape"`

.. py:method:: add(self) -> "IEOIRShape"

    Add an element at the end of the collection.

    :Returns:

        :obj:`~"IEOIRShape"`

.. py:method:: remove_at(self, index:int) -> None

    Remove an element at the given index in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`



