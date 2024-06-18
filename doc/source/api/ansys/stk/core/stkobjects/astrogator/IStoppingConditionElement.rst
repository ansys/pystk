IStoppingConditionElement
=========================

.. py:class:: IStoppingConditionElement

   object
   
   The status of a stopping condition.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_control_parameter`
              - Enable or disables the specified control parameter.
            * - :py:meth:`~disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:meth:`~is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~active`
            * - :py:meth:`~control_parameters_available`
            * - :py:meth:`~properties`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStoppingConditionElement


Property detail
---------------

.. py:property:: active
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionElement.active
    :type: bool

    If true, the stopping condition is active.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionElement.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.astrogator.IStoppingConditionElement.properties
    :type: "IAgVAStoppingConditionComponent"

    Get the properties available to the stopping condition.


Method detail
-------------



.. py:method:: enable_control_parameter(self, param:"CONTROL_STOPPING_CONDITION") -> None

    Enable or disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_STOPPING_CONDITION"`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param:"CONTROL_STOPPING_CONDITION") -> None

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_STOPPING_CONDITION"`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param:"CONTROL_STOPPING_CONDITION") -> bool

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~"CONTROL_STOPPING_CONDITION"`

    :Returns:

        :obj:`~bool`



