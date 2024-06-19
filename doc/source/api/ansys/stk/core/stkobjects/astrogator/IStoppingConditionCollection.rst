IStoppingConditionCollection
============================

.. py:class:: IStoppingConditionCollection

   object
   
   The list of Stopping Conditions.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Allow you to iterate through the collection.
            * - :py:meth:`~add`
              - Add a stopping condition.
            * - :py:meth:`~remove`
              - Remove a stopping condition.
            * - :py:meth:`~cut`
              - Copy the stopping condition into the clipboard and removes the stopping condition from the list.
            * - :py:meth:`~paste`
              - Pastes the stopping condition from the clipboard and inserts into the list.
            * - :py:meth:`~insert_copy`
              - Copy the stopping condition and inserts the copy into the list.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a stopping condition in the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a stopping condition in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStoppingConditionCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IStoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IStoppingConditionElement`

.. py:method:: add(self, conditionName: str) -> IStoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.add

    Add a stopping condition.

    :Parameters:

    **conditionName** : :obj:`~str`

    :Returns:

        :obj:`~IStoppingConditionElement`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.remove

    Remove a stopping condition.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.cut

    Copy the stopping condition into the clipboard and removes the stopping condition from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IStoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.paste

    Pastes the stopping condition from the clipboard and inserts into the list.

    :Returns:

        :obj:`~IStoppingConditionElement`

.. py:method:: insert_copy(self, stopCond: IStoppingConditionElement) -> IStoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.insert_copy

    Copy the stopping condition and inserts the copy into the list.

    :Parameters:

    **stopCond** : :obj:`~IStoppingConditionElement`

    :Returns:

        :obj:`~IStoppingConditionElement`

.. py:method:: get_item_by_index(self, index: int) -> IStoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.get_item_by_index

    Retrieve a stopping condition in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IStoppingConditionElement`

.. py:method:: get_item_by_name(self, name: str) -> IStoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection.get_item_by_name

    Retrieve a stopping condition in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IStoppingConditionElement`

