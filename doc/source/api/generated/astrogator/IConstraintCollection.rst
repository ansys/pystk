IConstraintCollection
=====================

.. py:class:: IConstraintCollection

   object
   
   The list of constraints assigned to a stopping condition.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add a constraint to the collection.
            * - :py:meth:`~item`
              - Iterate through the collection.
            * - :py:meth:`~remove`
              - Remove a specified constraint from the collection.
            * - :py:meth:`~cut`
              - Copy the constraint into the clipboard and removes the constraint from the list.
            * - :py:meth:`~paste`
              - Pastes the constraint from the clipboard and inserts into the list.
            * - :py:meth:`~insert_copy`
              - Copy the constraint and inserts the copy into the list.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a constraint from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a constraint from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IConstraintCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IConstraintCollection._NewEnum
    :type: EnumeratorProxy

    A property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IConstraintCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: add(self, resultName:str) -> "IAsTriggerCondition"

    Add a constraint to the collection.

    :Parameters:

    **resultName** : :obj:`~str`

    :Returns:

        :obj:`~"IAsTriggerCondition"`

.. py:method:: item(self, indexOrName:typing.Any) -> "IAsTriggerCondition"

    Iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IAsTriggerCondition"`

.. py:method:: remove(self, indexOrName:typing.Any) -> None

    Remove a specified constraint from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName:typing.Any) -> None

    Copy the constraint into the clipboard and removes the constraint from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> "IAsTriggerCondition"

    Pastes the constraint from the clipboard and inserts into the list.

    :Returns:

        :obj:`~"IAsTriggerCondition"`

.. py:method:: insert_copy(self, cond:"IAsTriggerCondition") -> "IAsTriggerCondition"

    Copy the constraint and inserts the copy into the list.

    :Parameters:

    **cond** : :obj:`~"IAsTriggerCondition"`

    :Returns:

        :obj:`~"IAsTriggerCondition"`

.. py:method:: get_item_by_index(self, index:int) -> "IAsTriggerCondition"

    Retrieve a constraint from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IAsTriggerCondition"`

.. py:method:: get_item_by_name(self, name:str) -> "IAsTriggerCondition"

    Retrieve a constraint from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IAsTriggerCondition"`

