CalculationToolConditionCombined
================================

.. py:class:: ansys.stk.core.vgt.CalculationToolConditionCombined

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolCondition`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Define a condition which combines multiple conditions.

.. py:currentmodule:: CalculationToolConditionCombined

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionCombined.get_all_conditions`
              - Get all conditions that are being combined.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionCombined.set_all_conditions`
              - Set all conditions to be combined.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionCombined.get_condition`
              - Get the condition at the position specified.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionCombined.set_condition`
              - Set the condition at the position specified.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionCombined.remove_condition`
              - Remove the condition at the position specified.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionCombined.add_condition`
              - Add a condition at the end of the list.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionCombined.boolean_operation`
              - Get the operation from the condition that determines how the conditions are combined. The operation can be set to AND, OR, XOR, MINUS.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionCombined.count`
              - Get the number of conditions in the combined condition.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolConditionCombined


Property detail
---------------

.. py:property:: boolean_operation
    :canonical: ansys.stk.core.vgt.CalculationToolConditionCombined.boolean_operation
    :type: ConditionCombinedOperationType

    Get the operation from the condition that determines how the conditions are combined. The operation can be set to AND, OR, XOR, MINUS.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.CalculationToolConditionCombined.count
    :type: int

    Get the number of conditions in the combined condition.


Method detail
-------------




.. py:method:: get_all_conditions(self) -> list
    :canonical: ansys.stk.core.vgt.CalculationToolConditionCombined.get_all_conditions

    Get all conditions that are being combined.

    :Returns:

        :obj:`~list`

.. py:method:: set_all_conditions(self, conditions: list) -> None
    :canonical: ansys.stk.core.vgt.CalculationToolConditionCombined.set_all_conditions

    Set all conditions to be combined.

    :Parameters:

    **conditions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: get_condition(self, pos: int) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.CalculationToolConditionCombined.get_condition

    Get the condition at the position specified.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: set_condition(self, ref: ICalculationToolCondition, pos: int) -> None
    :canonical: ansys.stk.core.vgt.CalculationToolConditionCombined.set_condition

    Set the condition at the position specified.

    :Parameters:

    **ref** : :obj:`~ICalculationToolCondition`
    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_condition(self, pos: int) -> None
    :canonical: ansys.stk.core.vgt.CalculationToolConditionCombined.remove_condition

    Remove the condition at the position specified.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add_condition(self, ref: ICalculationToolCondition) -> None
    :canonical: ansys.stk.core.vgt.CalculationToolConditionCombined.add_condition

    Add a condition at the end of the list.

    :Parameters:

    **ref** : :obj:`~ICalculationToolCondition`

    :Returns:

        :obj:`~None`

