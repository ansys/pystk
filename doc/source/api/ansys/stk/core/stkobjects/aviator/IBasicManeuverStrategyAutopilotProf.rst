IBasicManeuverStrategyAutopilotProf
===================================

.. py:class:: IBasicManeuverStrategyAutopilotProf

   object
   
   Interface used to access options for the Autopilot - Vertical Plane Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_mode`
            * - :py:meth:`~absolute_altitude`
            * - :py:meth:`~relative_altitude_change`
            * - :py:meth:`~altitude_rate`
            * - :py:meth:`~fpa`
            * - :py:meth:`~altitude_control_mode`
            * - :py:meth:`~control_altitude_rate_value`
            * - :py:meth:`~control_fpa_value`
            * - :py:meth:`~control_limit_mode`
            * - :py:meth:`~max_pitch_rate`
            * - :py:meth:`~fly_ballistic`
            * - :py:meth:`~damping_ratio`
            * - :py:meth:`~airspeed_options`
            * - :py:meth:`~compensate_for_coriolis_accel`
            * - :py:meth:`~stop_when_conditions_met`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyAutopilotProf


Property detail
---------------

.. py:property:: altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.altitude_mode
    :type: "AUTOPILOT_ALTITUDE_MODE"

    Gets or sets the altitude mode of the autopilot - vertical plane strategy.

.. py:property:: absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.absolute_altitude
    :type: float

    Gets or sets the absolute altitude for the specify altitude mode.

.. py:property:: relative_altitude_change
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.relative_altitude_change
    :type: float

    Gets or sets the relative altitude change for the specify altitude change mode.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.altitude_rate
    :type: float

    Gets or sets the altitude rate for the specify altitude rate mode.

.. py:property:: fpa
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.fpa
    :type: typing.Any

    Gets or sets the flight path angle for the specify wind frame flight path angle mode.

.. py:property:: altitude_control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.altitude_control_mode
    :type: "AUTOPILOT_ALTITUDE_CONTROL_MODE"

    Gets or sets the altitude control mode for the hold initial altitude, specify altitude, and specify altitude change modes.

.. py:property:: control_altitude_rate_value
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.control_altitude_rate_value
    :type: float

    Gets or sets the altitude rate control value for the hold initial altitude, specify altitude, and specify altitude change modes.

.. py:property:: control_fpa_value
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.control_fpa_value
    :type: typing.Any

    Gets or sets the control flight path angle value for the hold initial altitude, specify altitude, and specify altitude change modes.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.control_limit_mode
    :type: "PERF_MODEL_OVERRIDE"

    Gets or sets the control limits mode.

.. py:property:: max_pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.max_pitch_rate
    :type: typing.Any

    Gets or sets the max pitch rate for the control limits.

.. py:property:: fly_ballistic
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.fly_ballistic
    :type: bool

    Gets or sets the option to fly a ballistic trajectory when the performance is insufficient.

.. py:property:: damping_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.damping_ratio
    :type: float

    Gets or sets the damping ratio of the control law.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.airspeed_options
    :type: "IAgAvtrBasicManeuverAirspeedOptions"

    Get the airspeed options.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: stop_when_conditions_met
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyAutopilotProf.stop_when_conditions_met
    :type: bool

    Stop when conditions are met.


