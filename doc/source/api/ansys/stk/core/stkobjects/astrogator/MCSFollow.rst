MCSFollow
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSFollow

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Follow segment.

.. py:currentmodule:: MCSFollow

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.leader`
              - Get the leader object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.x_offset`
              - Get or set the distance that the spacecraft will be offset from the leader's body frame along the X axis. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.y_offset`
              - Get or set the distance that the spacecraft will be offset from the leader's body frame along the Y axis. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.z_offset`
              - Get or set the distance that the spacecraft will be offset from the leader's body frame along the Z axis. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.separation_conditions`
              - If separation conditions are specified, the list of separation conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.spacecraft_parameters`
              - Get the spacecraft's physical properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.fuel_tank`
              - Get the spacecraft's fuel tank properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.joining_type`
              - Get or set the joining type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.separation_type`
              - Get or set the separation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.spacecraft_and_fuel_tank_type`
              - Get or set the spacecraft snd fuel tank configuration type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.joining_conditions`
              - If joining conditions are specified, the list of joining conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.control_parameters_available`
              - Return whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSFollow.user_variables`
              - Interface used to modify user variables for the follow segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSFollow


Property detail
---------------

.. py:property:: leader
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.leader
    :type: ILinkToObject

    Get the leader object.

.. py:property:: x_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.x_offset
    :type: float

    Get or set the distance that the spacecraft will be offset from the leader's body frame along the X axis. Uses Distance Dimension.

.. py:property:: y_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.y_offset
    :type: float

    Get or set the distance that the spacecraft will be offset from the leader's body frame along the Y axis. Uses Distance Dimension.

.. py:property:: z_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.z_offset
    :type: float

    Get or set the distance that the spacecraft will be offset from the leader's body frame along the Z axis. Uses Distance Dimension.

.. py:property:: separation_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.separation_conditions
    :type: StoppingConditionCollection

    If separation conditions are specified, the list of separation conditions.

.. py:property:: spacecraft_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.spacecraft_parameters
    :type: SpacecraftParameters

    Get the spacecraft's physical properties.

.. py:property:: fuel_tank
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.fuel_tank
    :type: FuelTank

    Get the spacecraft's fuel tank properties.

.. py:property:: joining_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.joining_type
    :type: FollowJoin

    Get or set the joining type.

.. py:property:: separation_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.separation_type
    :type: FollowSeparation

    Get or set the separation type.

.. py:property:: spacecraft_and_fuel_tank_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.spacecraft_and_fuel_tank_type
    :type: FollowSpacecraftAndFuelTank

    Get or set the spacecraft snd fuel tank configuration type.

.. py:property:: joining_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.joining_conditions
    :type: StoppingConditionCollection

    If joining conditions are specified, the list of joining conditions.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.user_variables
    :type: UserVariableCollection

    Interface used to modify user variables for the follow segment.


Method detail
-------------


















.. py:method:: enable_control_parameter(self, param: ControlFollow) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlFollow`


    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlFollow) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlFollow`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlFollow) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSFollow.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlFollow`


    :Returns:

        :obj:`~bool`



