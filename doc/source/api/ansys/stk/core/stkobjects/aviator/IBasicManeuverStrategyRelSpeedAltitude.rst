IBasicManeuverStrategyRelSpeedAltitude
======================================

.. py:class:: IBasicManeuverStrategyRelSpeedAltitude

   object
   
   Interface used to access options for a Relative Speed/Altitude Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_airspeed_offset`
              - Set the airspeed offset value and type.
            * - :py:meth:`~set_min_airspeed`
              - Set the minimum airspeed value and type.
            * - :py:meth:`~set_max_airspeed`
              - Set the maximum airspeed value and type.
            * - :py:meth:`~cancel_tgt_position_vel`
              - Cancel the position velocity strategies for Rel Speed Alt.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~target_name`
            * - :py:meth:`~valid_target_names`
            * - :py:meth:`~target_resolution`
            * - :py:meth:`~relative_altitude_mode`
            * - :py:meth:`~elevation_angle`
            * - :py:meth:`~altitude_offset`
            * - :py:meth:`~airspeed_offset_type`
            * - :py:meth:`~airspeed_offset`
            * - :py:meth:`~use_tgt_aspect_for_airspeed`
            * - :py:meth:`~use_perf_model_limits`
            * - :py:meth:`~range_for_equal_speed`
            * - :py:meth:`~range_to_transition_speed`
            * - :py:meth:`~min_altitude`
            * - :py:meth:`~max_altitude`
            * - :py:meth:`~min_airspeed`
            * - :py:meth:`~min_airspeed_type`
            * - :py:meth:`~max_airspeed`
            * - :py:meth:`~max_airspeed_type`
            * - :py:meth:`~stop_condition`
            * - :py:meth:`~compensate_for_coriolis_accel`
            * - :py:meth:`~position_vel_strategies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyRelSpeedAltitude


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: relative_altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.relative_altitude_mode
    :type: "RELATIVE_ALTITUDE_MODE"

    Gets or sets the mode to define the hold objective for the maneuver.

.. py:property:: elevation_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.elevation_angle
    :type: typing.Any

    Gets or sets the goal elevation angle from the target to the aircraft.

.. py:property:: altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.altitude_offset
    :type: float

    Gets or sets the goal altitude offset from the target to the aircraft.

.. py:property:: airspeed_offset_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.airspeed_offset_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed type.

.. py:property:: airspeed_offset
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.airspeed_offset
    :type: float

    Get the airspeed offset from the target.

.. py:property:: use_tgt_aspect_for_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.use_tgt_aspect_for_airspeed
    :type: bool

    Gets or sets the option to use the target aspect to compute the enforced airspeed difference.

.. py:property:: use_perf_model_limits
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.use_perf_model_limits
    :type: bool

    Gets or sets the option to use the performance model limits for the aircraft.

.. py:property:: range_for_equal_speed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.range_for_equal_speed
    :type: float

    Gets or sets the range at which the aircraft will achieve the same airspeed as the target.

.. py:property:: range_to_transition_speed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.range_to_transition_speed
    :type: float

    Gets or sets the range at which the aircraft will begin to slow down to match the speed of the target.

.. py:property:: min_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.min_altitude
    :type: float

    Gets or sets the minimum altitude boundary for the maneuver.

.. py:property:: max_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.max_altitude
    :type: float

    Gets or sets the maximum altitude boundary for the maneuver.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.min_airspeed
    :type: float

    Get the minimum airspeed limit for the maneuver.

.. py:property:: min_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.min_airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed type.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.max_airspeed
    :type: float

    Get the maximum airspeed limit for the maneuver.

.. py:property:: max_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.max_airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed type.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.stop_condition
    :type: "REL_SPEED_ALTITUDE_STOP_CONDITION"

    Gets or sets the stopping condition for the maneuver.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelSpeedAltitude.position_vel_strategies
    :type: "IAgAvtrBasicManeuverTargetPosVel"

    Get the position velocity strategies for Rel Speed Alt.


Method detail
-------------














.. py:method:: set_airspeed_offset(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the airspeed offset value and type.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`















.. py:method:: set_min_airspeed(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the minimum airspeed value and type.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_airspeed(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the maximum airspeed value and type.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`






.. py:method:: cancel_tgt_position_vel(self) -> None

    Cancel the position velocity strategies for Rel Speed Alt.

    :Returns:

        :obj:`~None`

