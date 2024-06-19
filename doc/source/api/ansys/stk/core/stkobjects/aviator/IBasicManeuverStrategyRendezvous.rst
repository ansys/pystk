IBasicManeuverStrategyRendezvous
================================

.. py:class:: IBasicManeuverStrategyRendezvous

   object
   
   Interface used to access options for a Rendezvous Formation Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_cpa`
              - Set whether to enable collision avoidance and the corresponding minimum distance between this aircraft and the target aircraft.
            * - :py:meth:`~set_airspeed_factor`
              - Set whether to enable the option to control how fine the control is and the corresponding dimensionless factor.
            * - :py:meth:`~cancel_tgt_position_vel`
              - Cancel the position velocity strategies for Rendezvous.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~target_name`
            * - :py:meth:`~valid_target_names`
            * - :py:meth:`~target_resolution`
            * - :py:meth:`~use_counter_turn_logic`
            * - :py:meth:`~enable_collision_avoidance`
            * - :py:meth:`~cpa`
            * - :py:meth:`~relative_bearing`
            * - :py:meth:`~relative_range`
            * - :py:meth:`~altitude_split`
            * - :py:meth:`~maneuver_factor`
            * - :py:meth:`~use_perf_model_limits`
            * - :py:meth:`~altitude_rate_control`
            * - :py:meth:`~min_load_factor_g`
            * - :py:meth:`~max_load_factor_g`
            * - :py:meth:`~max_speed_advantage`
            * - :py:meth:`~airspeed_control_mode`
            * - :py:meth:`~accel_decel_g`
            * - :py:meth:`~use_separate_airspeed_control`
            * - :py:meth:`~airspeed_factor`
            * - :py:meth:`~stop_condition`
            * - :py:meth:`~position_vel_strategies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyRendezvous


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: use_counter_turn_logic
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.use_counter_turn_logic
    :type: bool

    Gets or sets the option to improve performance when flying with a target on a straight and level flight path.

.. py:property:: enable_collision_avoidance
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.enable_collision_avoidance
    :type: bool

    Get the option to enable collision avoidance.

.. py:property:: cpa
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.cpa
    :type: float

    Get the minimum distance between this aircraft and the target aircraft.

.. py:property:: relative_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.relative_bearing
    :type: typing.Any

    Gets or sets the bearing relative to the target the aircraft will achieve and maintain.

.. py:property:: relative_range
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.relative_range
    :type: float

    Gets or sets the range to the target the aircraft will achieve and maintain.

.. py:property:: altitude_split
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.altitude_split
    :type: float

    Gets or sets the altitude difference between the aircraft and target.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.maneuver_factor
    :type: float

    Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: use_perf_model_limits
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.use_perf_model_limits
    :type: bool

    Gets or sets the option to derive the control limits of the aircraft from the applicable performance model.

.. py:property:: altitude_rate_control
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.altitude_rate_control
    :type: float

    Gets or sets the rate at which the aircraft will change altitude to achieve or maintain the ALtitude Split.

.. py:property:: min_load_factor_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.min_load_factor_g
    :type: float

    Gets or sets the minimum load factor the aircraft can bear while maneuvering in formation.

.. py:property:: max_load_factor_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.max_load_factor_g
    :type: float

    Gets or sets the maximum load factor the aircraft can bear while maneuvering in formation.

.. py:property:: max_speed_advantage
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.max_speed_advantage
    :type: float

    Gets or sets the limit to the airspeed difference between the aircraft and target.

.. py:property:: airspeed_control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.airspeed_control_mode
    :type: ACCEL_PERF_MODEL_OVERRIDE

    Gets or sets the method to define the aircraft's acceleration performance in formation.

.. py:property:: accel_decel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.accel_decel_g
    :type: float

    Gets or sets the aircraft's specified acceleration rate for an airspeed control mode set to override.

.. py:property:: use_separate_airspeed_control
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.use_separate_airspeed_control
    :type: bool

    Get the option to control how fine the control is over the airspeed adjustments in formation flight.

.. py:property:: airspeed_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.airspeed_factor
    :type: float

    Get the maneuver factor, a dimensionless factor defining how fine the control is over airspeed adjustments in formation flight.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.stop_condition
    :type: RENDEZVOUS_STOP_CONDITION

    Gets or sets the stopping condition for the maneuver.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.position_vel_strategies
    :type: IAgAvtrBasicManeuverTargetPosVel

    Get the position velocity strategies for Rendezvous.


Method detail
-------------










.. py:method:: set_cpa(self, enable: bool, cPA: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.set_cpa

    Set whether to enable collision avoidance and the corresponding minimum distance between this aircraft and the target aircraft.

    :Parameters:

    **enable** : :obj:`~bool`
    **cPA** : :obj:`~float`

    :Returns:

        :obj:`~None`

























.. py:method:: set_airspeed_factor(self, enable: bool, airspeedFactor: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.set_airspeed_factor

    Set whether to enable the option to control how fine the control is and the corresponding dimensionless factor.

    :Parameters:

    **enable** : :obj:`~bool`
    **airspeedFactor** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: cancel_tgt_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRendezvous.cancel_tgt_position_vel

    Cancel the position velocity strategies for Rendezvous.

    :Returns:

        :obj:`~None`

