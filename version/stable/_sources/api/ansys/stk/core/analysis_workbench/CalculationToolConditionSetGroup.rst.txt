CalculationToolConditionSetGroup
================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup

   Allow accessing and creating condition set components.

.. py:currentmodule:: CalculationToolConditionSetGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.get_item_by_index`
              - Retrieve a condition set from the collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.get_item_by_name`
              - Retrieve a condition set from the collection by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.factory`
              - Return a factory object used to create condition set components.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolConditionSetGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.factory
    :type: CalculationToolConditionSetFactory

    Return a factory object used to create condition set components.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, event_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.remove

    Remove a specified element.

    :Parameters:

        **event_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.item

    Return an element by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ICalculationToolConditionSet`


.. py:method:: get_item_by_index(self, index: int) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.get_item_by_index

    Retrieve a condition set from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ICalculationToolConditionSet`

.. py:method:: get_item_by_name(self, name: str) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup.get_item_by_name

    Retrieve a condition set from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolConditionSet`

