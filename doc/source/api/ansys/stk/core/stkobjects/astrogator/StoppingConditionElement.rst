StoppingConditionElement
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StoppingConditionElement

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   A stopping condition.

.. py:currentmodule:: StoppingConditionElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.enable_control_parameter`
              - Enable or disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.active`
              - If true, the stopping condition is active.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.control_parameters_available`
              - Returns whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.properties`
              - Get the properties available to the stopping condition.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StoppingConditionElement


Property detail
---------------

.. py:property:: active
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.active
    :type: bool

    If true, the stopping condition is active.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.properties
    :type: IStoppingConditionComponent

    Get the properties available to the stopping condition.


Method detail
-------------



.. py:method:: enable_control_parameter(self, param: ControlStoppingCondition) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.enable_control_parameter

    Enable or disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~ControlStoppingCondition`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlStoppingCondition) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~ControlStoppingCondition`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlStoppingCondition) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.StoppingConditionElement.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~ControlStoppingCondition`

    :Returns:

        :obj:`~bool`



