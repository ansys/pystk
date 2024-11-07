ConstraintCollection
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ConstraintCollection

   The Constraint component folder.

.. py:currentmodule:: ConstraintCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.add`
              - Add a constraint to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.item`
              - Iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.remove`
              - Remove a specified constraint from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.cut`
              - Copy the constraint into the clipboard and removes the constraint from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.paste`
              - Pastes the constraint from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.insert_copy`
              - Copy the constraint and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.get_item_by_index`
              - Retrieve a constraint from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.get_item_by_name`
              - Retrieve a constraint from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection._NewEnum`
              - A property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ConstraintCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection._NewEnum
    :type: EnumeratorProxy

    A property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: add(self, result_name: str) -> AsTriggerCondition
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.add

    Add a constraint to the collection.

    :Parameters:

    **result_name** : :obj:`~str`

    :Returns:

        :obj:`~AsTriggerCondition`

.. py:method:: item(self, index_or_name: typing.Any) -> AsTriggerCondition
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.item

    Iterate through the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~AsTriggerCondition`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.remove

    Remove a specified constraint from the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.cut

    Copy the constraint into the clipboard and removes the constraint from the list.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> AsTriggerCondition
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.paste

    Pastes the constraint from the clipboard and inserts into the list.

    :Returns:

        :obj:`~AsTriggerCondition`

.. py:method:: insert_copy(self, cond: AsTriggerCondition) -> AsTriggerCondition
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.insert_copy

    Copy the constraint and inserts the copy into the list.

    :Parameters:

    **cond** : :obj:`~AsTriggerCondition`

    :Returns:

        :obj:`~AsTriggerCondition`

.. py:method:: get_item_by_index(self, index: int) -> AsTriggerCondition
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.get_item_by_index

    Retrieve a constraint from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AsTriggerCondition`

.. py:method:: get_item_by_name(self, name: str) -> AsTriggerCondition
    :canonical: ansys.stk.core.stkobjects.astrogator.ConstraintCollection.get_item_by_name

    Retrieve a constraint from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AsTriggerCondition`

