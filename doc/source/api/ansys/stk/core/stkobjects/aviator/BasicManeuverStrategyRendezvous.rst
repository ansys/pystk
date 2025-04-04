BasicManeuverStrategyRendezvous
===============================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Rendezvous/Formation strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyRendezvous

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.set_cpa`
              - Set whether to enable collision avoidance and the corresponding minimum distance between this aircraft and the target aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.set_airspeed_factor`
              - Set whether to enable the option to control how fine the control is and the corresponding dimensionless factor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.cancel_target_position_velocity`
              - Cancel the position velocity strategies for Rendezvous.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.target_name`
              - Get or set the target name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.valid_target_names`
              - Return the valid target names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.target_resolution`
              - Get or set the target position/velocity sampling resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.use_counter_turn_logic`
              - Get or set the option to improve performance when flying with a target on a straight and level flight path.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.enable_collision_avoidance`
              - Get the option to enable collision avoidance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.cpa`
              - Get the minimum distance between this aircraft and the target aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.relative_bearing`
              - Get or set the bearing relative to the target the aircraft will achieve and maintain.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.relative_range`
              - Get or set the range to the target the aircraft will achieve and maintain.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.altitude_split`
              - Get or set the altitude difference between the aircraft and target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.maneuver_factor`
              - Get or set the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.use_performance_model_limits`
              - Get or set the option to derive the control limits of the aircraft from the applicable performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.altitude_rate_control`
              - Get or set the rate at which the aircraft will change altitude to achieve or maintain the ALtitude Split.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.min_load_factor_g`
              - Get or set the minimum load factor the aircraft can bear while maneuvering in formation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.max_load_factor_g`
              - Get or set the maximum load factor the aircraft can bear while maneuvering in formation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.max_speed_advantage`
              - Get or set the limit to the airspeed difference between the aircraft and target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.airspeed_control_mode`
              - Get or set the method to define the aircraft's acceleration performance in formation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.acceleration_deceleration_g`
              - Get or set the aircraft's specified acceleration rate for an airspeed control mode set to override.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.use_separate_airspeed_control`
              - Get the option to control how fine the control is over the airspeed adjustments in formation flight.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.airspeed_factor`
              - Get the maneuver factor, a dimensionless factor defining how fine the control is over airspeed adjustments in formation flight.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.stop_condition`
              - Get or set the stopping condition for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.position_velocity_strategies`
              - Get the position velocity strategies for Rendezvous.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyRendezvous


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.target_name
    :type: str

    Get or set the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.valid_target_names
    :type: list

    Return the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.target_resolution
    :type: float

    Get or set the target position/velocity sampling resolution.

.. py:property:: use_counter_turn_logic
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.use_counter_turn_logic
    :type: bool

    Get or set the option to improve performance when flying with a target on a straight and level flight path.

.. py:property:: enable_collision_avoidance
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.enable_collision_avoidance
    :type: bool

    Get the option to enable collision avoidance.

.. py:property:: cpa
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.cpa
    :type: float

    Get the minimum distance between this aircraft and the target aircraft.

.. py:property:: relative_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.relative_bearing
    :type: typing.Any

    Get or set the bearing relative to the target the aircraft will achieve and maintain.

.. py:property:: relative_range
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.relative_range
    :type: float

    Get or set the range to the target the aircraft will achieve and maintain.

.. py:property:: altitude_split
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.altitude_split
    :type: float

    Get or set the altitude difference between the aircraft and target.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.maneuver_factor
    :type: float

    Get or set the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: use_performance_model_limits
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.use_performance_model_limits
    :type: bool

    Get or set the option to derive the control limits of the aircraft from the applicable performance model.

.. py:property:: altitude_rate_control
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.altitude_rate_control
    :type: float

    Get or set the rate at which the aircraft will change altitude to achieve or maintain the ALtitude Split.

.. py:property:: min_load_factor_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.min_load_factor_g
    :type: float

    Get or set the minimum load factor the aircraft can bear while maneuvering in formation.

.. py:property:: max_load_factor_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.max_load_factor_g
    :type: float

    Get or set the maximum load factor the aircraft can bear while maneuvering in formation.

.. py:property:: max_speed_advantage
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.max_speed_advantage
    :type: float

    Get or set the limit to the airspeed difference between the aircraft and target.

.. py:property:: airspeed_control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.airspeed_control_mode
    :type: AccelerationPerformanceModelOverride

    Get or set the method to define the aircraft's acceleration performance in formation.

.. py:property:: acceleration_deceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.acceleration_deceleration_g
    :type: float

    Get or set the aircraft's specified acceleration rate for an airspeed control mode set to override.

.. py:property:: use_separate_airspeed_control
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.use_separate_airspeed_control
    :type: bool

    Get the option to control how fine the control is over the airspeed adjustments in formation flight.

.. py:property:: airspeed_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.airspeed_factor
    :type: float

    Get the maneuver factor, a dimensionless factor defining how fine the control is over airspeed adjustments in formation flight.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.stop_condition
    :type: RendezvousStopCondition

    Get or set the stopping condition for the maneuver.

.. py:property:: position_velocity_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.position_velocity_strategies
    :type: BasicManeuverTargetPositionVelocity

    Get the position velocity strategies for Rendezvous.


Method detail
-------------










.. py:method:: set_cpa(self, enable: bool, collision_avoidance: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.set_cpa

    Set whether to enable collision avoidance and the corresponding minimum distance between this aircraft and the target aircraft.

    :Parameters:

    **enable** : :obj:`~bool`
    **collision_avoidance** : :obj:`~float`

    :Returns:

        :obj:`~None`

























.. py:method:: set_airspeed_factor(self, enable: bool, airspeed_factor: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.set_airspeed_factor

    Set whether to enable the option to control how fine the control is and the corresponding dimensionless factor.

    :Parameters:

    **enable** : :obj:`~bool`
    **airspeed_factor** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: cancel_target_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous.cancel_target_position_velocity

    Cancel the position velocity strategies for Rendezvous.

    :Returns:

        :obj:`~None`

