UserVariableUpdate
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate

   User Variable Update.

.. py:currentmodule:: UserVariableUpdate

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.enable_control_parameter`
              - Enable or disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.unit_dimension`
              - Get the dimension of the user variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.variable_name`
              - Get the name of the user variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.variable_value`
              - Update value of the user variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.variable_action`
              - Action to be performed using the value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.control_parameters_available`
              - Return whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import UserVariableUpdate


Property detail
---------------

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.unit_dimension
    :type: str

    Get the dimension of the user variable.

.. py:property:: variable_name
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.variable_name
    :type: str

    Get the name of the user variable.

.. py:property:: variable_value
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.variable_value
    :type: typing.Any

    Update value of the user variable.

.. py:property:: variable_action
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.variable_action
    :type: UpdateAction

    Action to be performed using the value.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.


Method detail
-------------







.. py:method:: enable_control_parameter(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.enable_control_parameter

    Enable or disables the specified control parameter.

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.disable_control_parameter

    Disables the specified control parameter.

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableUpdate.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Returns:

        :obj:`~bool`


