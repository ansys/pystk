BasicManeuverStrategyAutopilotProf
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the autopiloc - vertical plane strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyAutopilotProf

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.altitude_mode`
              - Get or set the altitude mode of the autopilot - vertical plane strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.absolute_altitude`
              - Get or set the absolute altitude for the specify altitude mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.relative_altitude_change`
              - Get or set the relative altitude change for the specify altitude change mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.altitude_rate`
              - Get or set the altitude rate for the specify altitude rate mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.flight_path_angle`
              - Get or set the flight path angle for the specify wind frame flight path angle mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.altitude_control_mode`
              - Get or set the altitude control mode for the hold initial altitude, specify altitude, and specify altitude change modes.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.control_altitude_rate_value`
              - Get or set the altitude rate control value for the hold initial altitude, specify altitude, and specify altitude change modes.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.control_flight_path_angle_value`
              - Get or set the control flight path angle value for the hold initial altitude, specify altitude, and specify altitude change modes.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.control_limit_mode`
              - Get or set the control limits mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.max_pitch_rate`
              - Get or set the max pitch rate for the control limits.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.fly_ballistic`
              - Get or set the option to fly a ballistic trajectory when the performance is insufficient.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.damping_ratio`
              - Get or set the damping ratio of the control law.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.stop_when_conditions_met`
              - Stop when conditions are met.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyAutopilotProf


Property detail
---------------

.. py:property:: altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.altitude_mode
    :type: AutopilotAltitudeMode

    Get or set the altitude mode of the autopilot - vertical plane strategy.

.. py:property:: absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.absolute_altitude
    :type: float

    Get or set the absolute altitude for the specify altitude mode.

.. py:property:: relative_altitude_change
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.relative_altitude_change
    :type: float

    Get or set the relative altitude change for the specify altitude change mode.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.altitude_rate
    :type: float

    Get or set the altitude rate for the specify altitude rate mode.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.flight_path_angle
    :type: typing.Any

    Get or set the flight path angle for the specify wind frame flight path angle mode.

.. py:property:: altitude_control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.altitude_control_mode
    :type: AutopilotAltitudeControlMode

    Get or set the altitude control mode for the hold initial altitude, specify altitude, and specify altitude change modes.

.. py:property:: control_altitude_rate_value
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.control_altitude_rate_value
    :type: float

    Get or set the altitude rate control value for the hold initial altitude, specify altitude, and specify altitude change modes.

.. py:property:: control_flight_path_angle_value
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.control_flight_path_angle_value
    :type: typing.Any

    Get or set the control flight path angle value for the hold initial altitude, specify altitude, and specify altitude change modes.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.control_limit_mode
    :type: PerformanceModelOverride

    Get or set the control limits mode.

.. py:property:: max_pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.max_pitch_rate
    :type: typing.Any

    Get or set the max pitch rate for the control limits.

.. py:property:: fly_ballistic
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.fly_ballistic
    :type: bool

    Get or set the option to fly a ballistic trajectory when the performance is insufficient.

.. py:property:: damping_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.damping_ratio
    :type: float

    Get or set the damping ratio of the control law.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: stop_when_conditions_met
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf.stop_when_conditions_met
    :type: bool

    Stop when conditions are met.


