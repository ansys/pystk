StoppingConditionCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The stopping conditions collection.

.. py:currentmodule:: StoppingConditionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.add`
              - Add a stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.remove`
              - Remove a stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.cut`
              - Copy the stopping condition into the clipboard and removes the stopping condition from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.paste`
              - Pastes the stopping condition from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.insert_copy`
              - Copy the stopping condition and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.get_item_by_index`
              - Retrieve a stopping condition in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.get_item_by_name`
              - Retrieve a stopping condition in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StoppingConditionCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> StoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~StoppingConditionElement`

.. py:method:: add(self, conditionName: str) -> StoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.add

    Add a stopping condition.

    :Parameters:

    **conditionName** : :obj:`~str`

    :Returns:

        :obj:`~StoppingConditionElement`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.remove

    Remove a stopping condition.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.cut

    Copy the stopping condition into the clipboard and removes the stopping condition from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> StoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.paste

    Pastes the stopping condition from the clipboard and inserts into the list.

    :Returns:

        :obj:`~StoppingConditionElement`

.. py:method:: insert_copy(self, stopCond: StoppingConditionElement) -> StoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.insert_copy

    Copy the stopping condition and inserts the copy into the list.

    :Parameters:

    **stopCond** : :obj:`~StoppingConditionElement`

    :Returns:

        :obj:`~StoppingConditionElement`

.. py:method:: get_item_by_index(self, index: int) -> StoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.get_item_by_index

    Retrieve a stopping condition in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StoppingConditionElement`

.. py:method:: get_item_by_name(self, name: str) -> StoppingConditionElement
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection.get_item_by_name

    Retrieve a stopping condition in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~StoppingConditionElement`

