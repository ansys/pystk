IMissionControlSequenceUpdate
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate

   object
   
   Properties for an Update segment.

.. py:currentmodule:: IMissionControlSequenceUpdate

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.set_action_and_value`
              - Set an action and the new value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.get_action`
              - Get the action type for a parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.get_value`
              - Get the value type for a parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.set_action`
              - Set the update action type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.set_value`
              - Set the update value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.control_parameters_available`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.user_variables`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceUpdate


Property detail
---------------

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.user_variables
    :type: IUserVariableUpdateCollection

    Interface used to modify user variables for the update segment.


Method detail
-------------

.. py:method:: set_action_and_value(self, parameterType: UPDATE_PARAM, actionType: UPDATE_ACTION, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.set_action_and_value

    Set an action and the new value.

    :Parameters:

    **parameterType** : :obj:`~UPDATE_PARAM`
    **actionType** : :obj:`~UPDATE_ACTION`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: get_action(self, parameterType: UPDATE_PARAM) -> UPDATE_ACTION
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.get_action

    Get the action type for a parameter.

    :Parameters:

    **parameterType** : :obj:`~UPDATE_PARAM`

    :Returns:

        :obj:`~UPDATE_ACTION`

.. py:method:: get_value(self, parameterType: UPDATE_PARAM) -> float
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.get_value

    Get the value type for a parameter.

    :Parameters:

    **parameterType** : :obj:`~UPDATE_PARAM`

    :Returns:

        :obj:`~float`

.. py:method:: set_action(self, parameterName: UPDATE_PARAM, actionType: UPDATE_ACTION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.set_action

    Set the update action type.

    :Parameters:

    **parameterName** : :obj:`~UPDATE_PARAM`
    **actionType** : :obj:`~UPDATE_ACTION`

    :Returns:

        :obj:`~None`

.. py:method:: set_value(self, parameterName: UPDATE_PARAM, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.set_value

    Set the update value.

    :Parameters:

    **parameterName** : :obj:`~UPDATE_PARAM`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_UPDATE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_UPDATE`

    :Returns:

        :obj:`~None`

.. py:method:: enable_control_parameter(self, param: CONTROL_UPDATE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_UPDATE`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_UPDATE) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_UPDATE`

    :Returns:

        :obj:`~bool`



