UserVariable
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.UserVariable

   User Variable.

.. py:currentmodule:: UserVariable

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariable.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariable.enable_control_parameter`
              - Enable or disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariable.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariable.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariable.unit_dimension`
              - Get the dimension of the user variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariable.variable_name`
              - Set the name of the user variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariable.variable_value`
              - Get or set the initial value of the user variable.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import UserVariable


Property detail
---------------

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariable.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariable.unit_dimension
    :type: str

    Get the dimension of the user variable.

.. py:property:: variable_name
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariable.variable_name
    :type: str

    Set the name of the user variable.

.. py:property:: variable_value
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariable.variable_value
    :type: typing.Any

    Get or set the initial value of the user variable.


Method detail
-------------


.. py:method:: disable_control_parameter(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariable.disable_control_parameter

    Disables the specified control parameter.

    :Returns:

        :obj:`~None`

.. py:method:: enable_control_parameter(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariable.enable_control_parameter

    Enable or disables the specified control parameter.

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariable.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Returns:

        :obj:`~bool`





