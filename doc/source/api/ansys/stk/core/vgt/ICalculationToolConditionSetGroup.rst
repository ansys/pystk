ICalculationToolConditionSetGroup
=================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolConditionSetGroup

   object
   
   Allow accessing and creating condition set components.

.. py:currentmodule:: ICalculationToolConditionSetGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup.get_item_by_index`
              - Retrieve a condition set from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup.get_item_by_name`
              - Retrieve a condition set from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup.context`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup.count`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup.factory`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetGroup._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionSetGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup.context
    :type: IAnalysisWorkbenchContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup.factory
    :type: ICalculationToolConditionSetFactory

    Returns a factory object used to create condition set components.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, eventName: str) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup.remove

    Remove a specified element.

    :Parameters:

    **eventName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ICalculationToolConditionSet`


.. py:method:: get_item_by_index(self, index: int) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup.get_item_by_index

    Retrieve a condition set from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICalculationToolConditionSet`

.. py:method:: get_item_by_name(self, name: str) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetGroup.get_item_by_name

    Retrieve a condition set from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolConditionSet`

