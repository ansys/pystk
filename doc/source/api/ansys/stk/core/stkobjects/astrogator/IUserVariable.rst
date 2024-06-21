IUserVariable
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.IUserVariable

   object
   
   The properties for a User Variable initial value.

.. py:currentmodule:: IUserVariable

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariable.enable_control_parameter`
              - Enable or disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariable.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariable.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariable.unit_dimension`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariable.variable_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariable.variable_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariable.control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IUserVariable


Property detail
---------------

.. py:property:: unit_dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariable.unit_dimension
    :type: str

    Get the dimension of the user variable.

.. py:property:: variable_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariable.variable_name
    :type: str

    Set the name of the user variable.

.. py:property:: variable_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariable.variable_value
    :type: typing.Any

    Gets or sets the initial value of the user variable.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariable.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------





.. py:method:: enable_control_parameter(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariable.enable_control_parameter

    Enable or disables the specified control parameter.

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariable.disable_control_parameter

    Disables the specified control parameter.

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariable.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Returns:

        :obj:`~bool`


