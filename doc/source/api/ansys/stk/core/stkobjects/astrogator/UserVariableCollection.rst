UserVariableCollection
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.UserVariableCollection

   User Variable Initial Value Collection.

.. py:currentmodule:: UserVariableCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableCollection.get_item_by_index`
              - Retrieve a user variable in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableCollection.get_item_by_name`
              - Retrieve a user variable in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableCollection._new_enum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import UserVariableCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableCollection._new_enum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> UserVariable
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~UserVariable`



.. py:method:: get_item_by_index(self, index: int) -> UserVariable
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableCollection.get_item_by_index

    Retrieve a user variable in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~UserVariable`

.. py:method:: get_item_by_name(self, name: str) -> UserVariable
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableCollection.get_item_by_name

    Retrieve a user variable in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~UserVariable`

