BasicManeuverStrategyRelativeSpeedAltitude
==========================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Relative Speed/Altitude strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyRelativeSpeedAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.set_airspeed_offset`
              - Set the airspeed offset value and type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.set_min_airspeed`
              - Set the minimum airspeed value and type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.set_max_airspeed`
              - Set the maximum airspeed value and type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.cancel_target_position_vel`
              - Cancel the position velocity strategies for Rel Speed Alt.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.target_name`
              - Get or set the target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.valid_target_names`
              - Return the valid target names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.target_resolution`
              - Get or set the target position/velocity sampling resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.relative_altitude_mode`
              - Get or set the mode to define the hold objective for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.elevation_angle`
              - Get or set the goal elevation angle from the target to the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.altitude_offset`
              - Get or set the goal altitude offset from the target to the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.airspeed_offset_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.airspeed_offset`
              - Get the airspeed offset from the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.use_target_aspect_for_airspeed`
              - Get or set the option to use the target aspect to compute the enforced airspeed difference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.use_performance_model_limits`
              - Get or set the option to use the performance model limits for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.range_for_equal_speed`
              - Get or set the range at which the aircraft will achieve the same airspeed as the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.range_to_transition_speed`
              - Get or set the range at which the aircraft will begin to slow down to match the speed of the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.min_altitude`
              - Get or set the minimum altitude boundary for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.max_altitude`
              - Get or set the maximum altitude boundary for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.min_airspeed`
              - Get the minimum airspeed limit for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.min_airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.max_airspeed`
              - Get the maximum airspeed limit for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.max_airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.stop_condition`
              - Get or set the stopping condition for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.position_vel_strategies`
              - Get the position velocity strategies for Rel Speed Alt.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyRelativeSpeedAltitude


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.target_name
    :type: str

    Get or set the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.valid_target_names
    :type: list

    Return the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.target_resolution
    :type: float

    Get or set the target position/velocity sampling resolution.

.. py:property:: relative_altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.relative_altitude_mode
    :type: RelativeAltitudeMode

    Get or set the mode to define the hold objective for the maneuver.

.. py:property:: elevation_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.elevation_angle
    :type: typing.Any

    Get or set the goal elevation angle from the target to the aircraft.

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.altitude_offset
    :type: float

    Get or set the goal altitude offset from the target to the aircraft.

.. py:property:: airspeed_offset_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.airspeed_offset_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: airspeed_offset
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.airspeed_offset
    :type: float

    Get the airspeed offset from the target.

.. py:property:: use_target_aspect_for_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.use_target_aspect_for_airspeed
    :type: bool

    Get or set the option to use the target aspect to compute the enforced airspeed difference.

.. py:property:: use_performance_model_limits
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.use_performance_model_limits
    :type: bool

    Get or set the option to use the performance model limits for the aircraft.

.. py:property:: range_for_equal_speed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.range_for_equal_speed
    :type: float

    Get or set the range at which the aircraft will achieve the same airspeed as the target.

.. py:property:: range_to_transition_speed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.range_to_transition_speed
    :type: float

    Get or set the range at which the aircraft will begin to slow down to match the speed of the target.

.. py:property:: min_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.min_altitude
    :type: float

    Get or set the minimum altitude boundary for the maneuver.

.. py:property:: max_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.max_altitude
    :type: float

    Get or set the maximum altitude boundary for the maneuver.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.min_airspeed
    :type: float

    Get the minimum airspeed limit for the maneuver.

.. py:property:: min_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.min_airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.max_airspeed
    :type: float

    Get the maximum airspeed limit for the maneuver.

.. py:property:: max_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.max_airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.stop_condition
    :type: RelativeSpeedAltitudeStopCondition

    Get or set the stopping condition for the maneuver.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.position_vel_strategies
    :type: BasicManeuverTargetPositionVel

    Get the position velocity strategies for Rel Speed Alt.


Method detail
-------------














.. py:method:: set_airspeed_offset(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.set_airspeed_offset

    Set the airspeed offset value and type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`















.. py:method:: set_min_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.set_min_airspeed

    Set the minimum airspeed value and type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.set_max_airspeed

    Set the maximum airspeed value and type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`






.. py:method:: cancel_target_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude.cancel_target_position_vel

    Cancel the position velocity strategies for Rel Speed Alt.

    :Returns:

        :obj:`~None`

