StateCalcOrbitStateValue
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   OrbitStateValue Calc objects.

.. py:currentmodule:: StateCalcOrbitStateValue

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.calc_object_name`
              - Gets or sets the calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.input_coord_system_name`
              - Gets or sets the coordinate system of the input state.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.x`
              - Gets or sets the x position component. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.y`
              - Gets or sets the y position component. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.z`
              - Gets or sets the z position component. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.vx`
              - Gets or sets the x velocity component. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.vy`
              - Gets or sets the y velocity component. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.vz`
              - Gets or sets the z velocity component. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.control_parameters_available`
              - Returns whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcOrbitStateValue


Property detail
---------------

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.calc_object_name
    :type: str

    Gets or sets the calculation object.

.. py:property:: input_coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.input_coord_system_name
    :type: str

    Gets or sets the coordinate system of the input state.

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.x
    :type: typing.Any

    Gets or sets the x position component. Uses Distance Dimension.

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.y
    :type: typing.Any

    Gets or sets the y position component. Uses Distance Dimension.

.. py:property:: z
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.z
    :type: typing.Any

    Gets or sets the z position component. Uses Distance Dimension.

.. py:property:: vx
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.vx
    :type: typing.Any

    Gets or sets the x velocity component. Uses Rate Dimension.

.. py:property:: vy
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.vy
    :type: typing.Any

    Gets or sets the y velocity component. Uses Rate Dimension.

.. py:property:: vz
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.vz
    :type: typing.Any

    Gets or sets the z velocity component. Uses Rate Dimension.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------

















.. py:method:: enable_control_parameter(self, param: CONTROL_ORBIT_STATE_VALUE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ORBIT_STATE_VALUE`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ORBIT_STATE_VALUE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ORBIT_STATE_VALUE`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ORBIT_STATE_VALUE) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ORBIT_STATE_VALUE`

    :Returns:

        :obj:`~bool`


