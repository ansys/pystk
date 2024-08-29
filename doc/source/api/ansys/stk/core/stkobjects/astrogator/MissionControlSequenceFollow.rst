MissionControlSequenceFollow
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Follow segment.

.. py:currentmodule:: MissionControlSequenceFollow

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.leader`
              - Get the leader object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.x_offset`
              - Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the X axis. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.y_offset`
              - Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the Y axis. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.z_offset`
              - Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the Z axis. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.separation_conditions`
              - If separation conditions are specified, the list of separation conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.spacecraft_parameters`
              - Get the spacecraft's physical properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.fuel_tank`
              - Get the spacecraft's fuel tank properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.joining_type`
              - Gets or sets the joining type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.separation_type`
              - Gets or sets the separation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.spacecraft_and_fuel_tank_type`
              - Gets or sets the spacecraft snd fuel tank configuration type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.joining_conditions`
              - If joining conditions are specified, the list of joining conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.control_parameters_available`
              - Returns whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.user_variables`
              - Interface used to modify user variables for the follow segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MissionControlSequenceFollow


Property detail
---------------

.. py:property:: leader
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.leader
    :type: ILinkToObject

    Get the leader object.

.. py:property:: x_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.x_offset
    :type: float

    Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the X axis. Uses Distance Dimension.

.. py:property:: y_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.y_offset
    :type: float

    Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the Y axis. Uses Distance Dimension.

.. py:property:: z_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.z_offset
    :type: float

    Gets or sets the distance that the spacecraft will be offset from the leader's body frame along the Z axis. Uses Distance Dimension.

.. py:property:: separation_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.separation_conditions
    :type: StoppingConditionCollection

    If separation conditions are specified, the list of separation conditions.

.. py:property:: spacecraft_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.spacecraft_parameters
    :type: SpacecraftParameters

    Get the spacecraft's physical properties.

.. py:property:: fuel_tank
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.fuel_tank
    :type: FuelTank

    Get the spacecraft's fuel tank properties.

.. py:property:: joining_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.joining_type
    :type: FOLLOW_JOIN

    Gets or sets the joining type.

.. py:property:: separation_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.separation_type
    :type: FOLLOW_SEPARATION

    Gets or sets the separation type.

.. py:property:: spacecraft_and_fuel_tank_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.spacecraft_and_fuel_tank_type
    :type: FOLLOW_SPACECRAFT_AND_FUEL_TANK

    Gets or sets the spacecraft snd fuel tank configuration type.

.. py:property:: joining_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.joining_conditions
    :type: StoppingConditionCollection

    If joining conditions are specified, the list of joining conditions.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.user_variables
    :type: UserVariableCollection

    Interface used to modify user variables for the follow segment.


Method detail
-------------


















.. py:method:: enable_control_parameter(self, param: CONTROL_FOLLOW) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_FOLLOW`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_FOLLOW) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_FOLLOW`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_FOLLOW) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_FOLLOW`

    :Returns:

        :obj:`~bool`



