MCSUpdate
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSUpdate

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Update segment.

.. py:currentmodule:: MCSUpdate

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.set_action_and_value`
              - Set an action and the new value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.get_action`
              - Get the action type for a parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.get_value`
              - Get the value type for a parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.set_action`
              - Set the update action type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.set_value`
              - Set the update value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate.user_variables`
              - Interface used to modify user variables for the update segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSUpdate


Property detail
---------------

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.user_variables
    :type: UserVariableUpdateCollection

    Interface used to modify user variables for the update segment.


Method detail
-------------

.. py:method:: set_action_and_value(self, parameter_type: UpdateParam, action_type: UpdateAction, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.set_action_and_value

    Set an action and the new value.

    :Parameters:

        **parameter_type** : :obj:`~UpdateParam`

        **action_type** : :obj:`~UpdateAction`

        **value** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: get_action(self, parameter_type: UpdateParam) -> UpdateAction
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.get_action

    Get the action type for a parameter.

    :Parameters:

        **parameter_type** : :obj:`~UpdateParam`


    :Returns:

        :obj:`~UpdateAction`

.. py:method:: get_value(self, parameter_type: UpdateParam) -> float
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.get_value

    Get the value type for a parameter.

    :Parameters:

        **parameter_type** : :obj:`~UpdateParam`


    :Returns:

        :obj:`~float`

.. py:method:: set_action(self, parameter_name: UpdateParam, action_type: UpdateAction) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.set_action

    Set the update action type.

    :Parameters:

        **parameter_name** : :obj:`~UpdateParam`

        **action_type** : :obj:`~UpdateAction`


    :Returns:

        :obj:`~None`

.. py:method:: set_value(self, parameter_name: UpdateParam, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.set_value

    Set the update value.

    :Parameters:

        **parameter_name** : :obj:`~UpdateParam`

        **value** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlUpdate) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlUpdate`


    :Returns:

        :obj:`~None`

.. py:method:: enable_control_parameter(self, param: ControlUpdate) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlUpdate`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlUpdate) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSUpdate.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlUpdate`


    :Returns:

        :obj:`~bool`



