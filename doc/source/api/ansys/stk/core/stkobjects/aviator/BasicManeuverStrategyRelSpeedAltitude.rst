BasicManeuverStrategyRelSpeedAltitude
=====================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Relative Speed/Altitude strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyRelSpeedAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.set_airspeed_offset`
              - Set the airspeed offset value and type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.set_min_airspeed`
              - Set the minimum airspeed value and type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.set_max_airspeed`
              - Set the maximum airspeed value and type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.cancel_tgt_position_vel`
              - Cancel the position velocity strategies for Rel Speed Alt.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.target_name`
              - Gets or sets the target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.valid_target_names`
              - Returns the valid target names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.target_resolution`
              - Gets or sets the target position/velocity sampling resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.relative_altitude_mode`
              - Gets or sets the mode to define the hold objective for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.elevation_angle`
              - Gets or sets the goal elevation angle from the target to the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.altitude_offset`
              - Gets or sets the goal altitude offset from the target to the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.airspeed_offset_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.airspeed_offset`
              - Get the airspeed offset from the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.use_tgt_aspect_for_airspeed`
              - Gets or sets the option to use the target aspect to compute the enforced airspeed difference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.use_perf_model_limits`
              - Gets or sets the option to use the performance model limits for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.range_for_equal_speed`
              - Gets or sets the range at which the aircraft will achieve the same airspeed as the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.range_to_transition_speed`
              - Gets or sets the range at which the aircraft will begin to slow down to match the speed of the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.min_altitude`
              - Gets or sets the minimum altitude boundary for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.max_altitude`
              - Gets or sets the maximum altitude boundary for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.min_airspeed`
              - Get the minimum airspeed limit for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.min_airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.max_airspeed`
              - Get the maximum airspeed limit for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.max_airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.stop_condition`
              - Gets or sets the stopping condition for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.compensate_for_coriolis_accel`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.position_vel_strategies`
              - Get the position velocity strategies for Rel Speed Alt.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyRelSpeedAltitude


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: relative_altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.relative_altitude_mode
    :type: RELATIVE_ALTITUDE_MODE

    Gets or sets the mode to define the hold objective for the maneuver.

.. py:property:: elevation_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.elevation_angle
    :type: typing.Any

    Gets or sets the goal elevation angle from the target to the aircraft.

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.altitude_offset
    :type: float

    Gets or sets the goal altitude offset from the target to the aircraft.

.. py:property:: airspeed_offset_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.airspeed_offset_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: airspeed_offset
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.airspeed_offset
    :type: float

    Get the airspeed offset from the target.

.. py:property:: use_tgt_aspect_for_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.use_tgt_aspect_for_airspeed
    :type: bool

    Gets or sets the option to use the target aspect to compute the enforced airspeed difference.

.. py:property:: use_perf_model_limits
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.use_perf_model_limits
    :type: bool

    Gets or sets the option to use the performance model limits for the aircraft.

.. py:property:: range_for_equal_speed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.range_for_equal_speed
    :type: float

    Gets or sets the range at which the aircraft will achieve the same airspeed as the target.

.. py:property:: range_to_transition_speed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.range_to_transition_speed
    :type: float

    Gets or sets the range at which the aircraft will begin to slow down to match the speed of the target.

.. py:property:: min_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.min_altitude
    :type: float

    Gets or sets the minimum altitude boundary for the maneuver.

.. py:property:: max_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.max_altitude
    :type: float

    Gets or sets the maximum altitude boundary for the maneuver.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.min_airspeed
    :type: float

    Get the minimum airspeed limit for the maneuver.

.. py:property:: min_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.min_airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.max_airspeed
    :type: float

    Get the maximum airspeed limit for the maneuver.

.. py:property:: max_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.max_airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.stop_condition
    :type: REL_SPEED_ALTITUDE_STOP_CONDITION

    Gets or sets the stopping condition for the maneuver.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.position_vel_strategies
    :type: IBasicManeuverTargetPositionVel

    Get the position velocity strategies for Rel Speed Alt.


Method detail
-------------














.. py:method:: set_airspeed_offset(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.set_airspeed_offset

    Set the airspeed offset value and type.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`















.. py:method:: set_min_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.set_min_airspeed

    Set the minimum airspeed value and type.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.set_max_airspeed

    Set the maximum airspeed value and type.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`






.. py:method:: cancel_tgt_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude.cancel_tgt_position_vel

    Cancel the position velocity strategies for Rel Speed Alt.

    :Returns:

        :obj:`~None`

