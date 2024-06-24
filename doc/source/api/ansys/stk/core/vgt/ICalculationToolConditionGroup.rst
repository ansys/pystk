ICalculationToolConditionGroup
==============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolConditionGroup

   object
   
   Access or create VGT conditions associated with an object or a central body.

.. py:currentmodule:: ICalculationToolConditionGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup.get_item_by_index`
              - Retrieve a condition from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup.get_item_by_name`
              - Retrieve a condition from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup.context`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup.count`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup.factory`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionGroup._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup.context
    :type: IAnalysisWorkbenchContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup.factory
    :type: ICalculationToolConditionFactory

    Returns a factory object used to create calc scalar components.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, eventName: str) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup.remove

    Remove a specified element.

    :Parameters:

    **eventName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ICalculationToolCondition`


.. py:method:: get_item_by_index(self, index: int) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup.get_item_by_index

    Retrieve a condition from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: get_item_by_name(self, name: str) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionGroup.get_item_by_name

    Retrieve a condition from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolCondition`

