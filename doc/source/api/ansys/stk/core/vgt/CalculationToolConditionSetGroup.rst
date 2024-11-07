CalculationToolConditionSetGroup
================================

.. py:class:: ansys.stk.core.vgt.CalculationToolConditionSetGroup

   Allow accessing and creating condition set components.

.. py:currentmodule:: CalculationToolConditionSetGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup.get_item_by_index`
              - Retrieve a condition set from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup.get_item_by_name`
              - Retrieve a condition set from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup.context`
              - Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup.count`
              - Returns a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup.factory`
              - Returns a factory object used to create condition set components.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup._NewEnum`
              - Returns a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolConditionSetGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup.factory
    :type: CalculationToolConditionSetFactory

    Returns a factory object used to create condition set components.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, event_name: str) -> None
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup.remove

    Remove a specified element.

    :Parameters:

    **event_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ICalculationToolConditionSet`


.. py:method:: get_item_by_index(self, index: int) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup.get_item_by_index

    Retrieve a condition set from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICalculationToolConditionSet`

.. py:method:: get_item_by_name(self, name: str) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetGroup.get_item_by_name

    Retrieve a condition set from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolConditionSet`

