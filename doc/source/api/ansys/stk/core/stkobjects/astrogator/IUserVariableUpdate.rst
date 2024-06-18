IUserVariableUpdate
===================

.. py:class:: IUserVariableUpdate

   object
   
   Properties for a User Variable update.

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

            * - :py:meth:`~unit_dimension`
            * - :py:meth:`~variable_name`
            * - :py:meth:`~variable_value`
            * - :py:meth:`~variable_action`
            * - :py:meth:`~control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IUserVariableUpdate


Property detail
---------------

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdate.unit_dimension
    :type: str

    Get the dimension of the user variable.

.. py:property:: variable_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdate.variable_name
    :type: str

    Get the name of the user variable.

.. py:property:: variable_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdate.variable_value
    :type: typing.Any

    Update value of the user variable.

.. py:property:: variable_action
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdate.variable_action
    :type: "UPDATE_ACTION"

    Action to be performed using the value.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdate.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------







.. py:method:: enable_control_parameter(self) -> None

    Enable or disables the specified control parameter.

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self) -> None

    Disables the specified control parameter.

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self) -> bool

    Sees if the specified control is enabled.

    :Returns:

        :obj:`~bool`


