UserVariableUpdateCollection
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection

   User Variable Update Collection.

.. py:currentmodule:: UserVariableUpdateCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection.get_item_by_index`
              - Retrieve a user variable update in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection.get_item_by_name`
              - Retrieve a user variable update in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import UserVariableUpdateCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> UserVariableUpdate
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~UserVariableUpdate`



.. py:method:: get_item_by_index(self, index: int) -> UserVariableUpdate
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection.get_item_by_index

    Retrieve a user variable update in the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~UserVariableUpdate`

.. py:method:: get_item_by_name(self, name: str) -> UserVariableUpdate
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection.get_item_by_name

    Retrieve a user variable update in the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UserVariableUpdate`

