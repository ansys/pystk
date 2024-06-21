ICalculationToolConditionCombined
=================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolConditionCombined

   object
   
   Define a condition which combines multiple conditions.

.. py:currentmodule:: ICalculationToolConditionCombined

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionCombined.get_all_conditions`
              - Get all conditions that are being combined.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionCombined.set_all_conditions`
              - Set all conditions to be combined.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionCombined.get_condition`
              - Get the condition at the position specified.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionCombined.set_condition`
              - Set the condition at the position specified.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionCombined.remove_condition`
              - Remove the condition at the position specified.
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionCombined.add_condition`
              - Add a condition at the end of the list.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionCombined.combine_operation`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionCombined.condition_count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionCombined


Property detail
---------------

.. py:property:: combine_operation
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionCombined.combine_operation
    :type: CRDN_CONDITION_COMBINED_OPERATION_TYPE

    Get the operation from the condition that determines how the conditions are combined. The operation can be set to AND, OR, XOR, MINUS.

.. py:property:: condition_count
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionCombined.condition_count
    :type: int

    Gets the number of conditions in the combined condition.


Method detail
-------------




.. py:method:: get_all_conditions(self) -> list
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionCombined.get_all_conditions

    Get all conditions that are being combined.

    :Returns:

        :obj:`~list`

.. py:method:: set_all_conditions(self, conditions: list) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionCombined.set_all_conditions

    Set all conditions to be combined.

    :Parameters:

    **conditions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: get_condition(self, pos: int) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionCombined.get_condition

    Get the condition at the position specified.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: set_condition(self, ref: ICalculationToolCondition, pos: int) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionCombined.set_condition

    Set the condition at the position specified.

    :Parameters:

    **ref** : :obj:`~ICalculationToolCondition`
    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_condition(self, pos: int) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionCombined.remove_condition

    Remove the condition at the position specified.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add_condition(self, ref: ICalculationToolCondition) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionCombined.add_condition

    Add a condition at the end of the list.

    :Parameters:

    **ref** : :obj:`~ICalculationToolCondition`

    :Returns:

        :obj:`~None`

