IStateCalcOrbitStateValue
=========================

.. py:class:: IStateCalcOrbitStateValue

   object
   
   Properties for an Orbit State Value calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:meth:`~disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:meth:`~is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~calc_object_name`
            * - :py:meth:`~input_coord_system_name`
            * - :py:meth:`~x`
            * - :py:meth:`~y`
            * - :py:meth:`~z`
            * - :py:meth:`~vx`
            * - :py:meth:`~vy`
            * - :py:meth:`~vz`
            * - :py:meth:`~control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcOrbitStateValue


Property detail
---------------

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.calc_object_name
    :type: str

    Gets or sets the calculation object.

.. py:property:: input_coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.input_coord_system_name
    :type: str

    Gets or sets the coordinate system of the input state.

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.x
    :type: typing.Any

    Gets or sets the x position component. Uses Distance Dimension.

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.y
    :type: typing.Any

    Gets or sets the y position component. Uses Distance Dimension.

.. py:property:: z
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.z
    :type: typing.Any

    Gets or sets the z position component. Uses Distance Dimension.

.. py:property:: vx
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.vx
    :type: typing.Any

    Gets or sets the x velocity component. Uses Rate Dimension.

.. py:property:: vy
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.vy
    :type: typing.Any

    Gets or sets the y velocity component. Uses Rate Dimension.

.. py:property:: vz
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.vz
    :type: typing.Any

    Gets or sets the z velocity component. Uses Rate Dimension.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------

















.. py:method:: enable_control_parameter(self, param: CONTROL_ORBIT_STATE_VALUE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ORBIT_STATE_VALUE`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ORBIT_STATE_VALUE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ORBIT_STATE_VALUE`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ORBIT_STATE_VALUE) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ORBIT_STATE_VALUE`

    :Returns:

        :obj:`~bool`


