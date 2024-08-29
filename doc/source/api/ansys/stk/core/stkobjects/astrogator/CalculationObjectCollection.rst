CalculationObjectCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection

   The Calculation Object component folder.

.. py:currentmodule:: CalculationObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.add`
              - Add a calc object to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.item`
              - Return a calc object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.remove`
              - Remove a calc object from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.cut`
              - Copy a calc object to the clipboard and removes the calc object from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.paste`
              - Pastes a calc object from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.insert_copy`
              - Copy a calc object and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.get_item_by_index`
              - Retrieve a calc object found by the index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.get_item_by_name`
              - Retrieve a calc object found by the name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CalculationObjectCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: add(self, name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.add

    Add a calc object to the collection.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: item(self, indexOrName: typing.Any) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.item

    Return a calc object.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.remove

    Remove a calc object from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.cut

    Copy a calc object to the clipboard and removes the calc object from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.paste

    Pastes a calc object from the clipboard into the list.

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: insert_copy(self, calcObj: IComponentInfo) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.insert_copy

    Copy a calc object and inserts the copy into the list.

    :Parameters:

    **calcObj** : :obj:`~IComponentInfo`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_index(self, index: int) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.get_item_by_index

    Retrieve a calc object found by the index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_name(self, name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection.get_item_by_name

    Retrieve a calc object found by the name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

