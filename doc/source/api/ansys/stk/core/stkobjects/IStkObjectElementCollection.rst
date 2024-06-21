IStkObjectElementCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.IStkObjectElementCollection

   object
   
   Represents a collection of STK objects.

.. py:currentmodule:: IStkObjectElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectElementCollection.item`
              - Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectElementCollection.contains`
              - Check whether an object with the given name exists.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectElementCollection.get_item_by_index`
              - Retrieve an Stk object element from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectElementCollection.get_item_by_name`
              - Retrieve an Stk object element from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectElementCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectElementCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObjectElementCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IStkObjectElementCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IStkObjectElementCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, indexOrName: typing.Any) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectElementCollection.item

    Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IStkObject`


.. py:method:: contains(self, instName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IStkObjectElementCollection.contains

    Check whether an object with the given name exists.

    :Parameters:

    **instName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: get_item_by_index(self, index: int) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectElementCollection.get_item_by_index

    Retrieve an Stk object element from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: get_item_by_name(self, name: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectElementCollection.get_item_by_name

    Retrieve an Stk object element from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

