ISTKObjectElementCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.ISTKObjectElementCollection

   Represents a collection of STK objects.

.. py:currentmodule:: ISTKObjectElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISTKObjectElementCollection.item`
              - Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISTKObjectElementCollection.contains`
              - Check whether an object with the given name exists.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISTKObjectElementCollection.get_item_by_index`
              - Retrieve an Stk object element from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISTKObjectElementCollection.get_item_by_name`
              - Retrieve an Stk object element from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISTKObjectElementCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISTKObjectElementCollection._new_enum`
              - Return an enumerator that can iterate through the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISTKObjectElementCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ISTKObjectElementCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.ISTKObjectElementCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index_or_name: typing.Any) -> ISTKObject
    :canonical: ansys.stk.core.stkobjects.ISTKObjectElementCollection.item

    Given an index, returns an element in the collection. If the index is an integer, then the method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ISTKObject`


.. py:method:: contains(self, inst_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.ISTKObjectElementCollection.contains

    Check whether an object with the given name exists.

    :Parameters:

        **inst_name** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: get_item_by_index(self, index: int) -> ISTKObject
    :canonical: ansys.stk.core.stkobjects.ISTKObjectElementCollection.get_item_by_index

    Retrieve an Stk object element from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ISTKObject`

.. py:method:: get_item_by_name(self, name: str) -> ISTKObject
    :canonical: ansys.stk.core.stkobjects.ISTKObjectElementCollection.get_item_by_name

    Retrieve an Stk object element from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ISTKObject`

