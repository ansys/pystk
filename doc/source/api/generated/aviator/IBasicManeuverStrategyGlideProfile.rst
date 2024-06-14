IBasicManeuverStrategyGlideProfile
==================================

.. py:class:: IBasicManeuverStrategyGlideProfile

   object
   
   Interface used to access options for a Glide Profile Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_airspeed`
              - Set the airspeed and airspeed type that the aircraft will attempt to achieve and maintain if the hold initial airspeed option is not enabled.
            * - :py:meth:`~set_glide_speed_control_mode`
              - Set the glide speed control mode and altitude.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~hold_initial_airspeed`
            * - :py:meth:`~airspeed`
            * - :py:meth:`~airspeed_type`
            * - :py:meth:`~min_g`
            * - :py:meth:`~max_g`
            * - :py:meth:`~max_speed_limits`
            * - :py:meth:`~compensate_for_coriolis_accel`
            * - :py:meth:`~powered_cruise_mode`
            * - :py:meth:`~powered_cruise_throttle`
            * - :py:meth:`~powered_cruise_thrust_model`
            * - :py:meth:`~glide_speed_control_mode`
            * - :py:meth:`~glide_speed_control_altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyGlideProfile


Property detail
---------------

.. py:property:: hold_initial_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.hold_initial_airspeed
    :type: bool

    Select whether to maintain the airspeed of the aircraft at the beginning of the procedure throughout the maneuver.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.airspeed
    :type: float

    Get the airspeed the aircraft will attempt to achieve and maintain if the hold initial airspeed option is not enabled.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed type.

.. py:property:: min_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.min_g
    :type: float

    Gets or sets the minimum load factor the aircraft can withstand.

.. py:property:: max_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.max_g
    :type: float

    Gets or sets the maximum load factor the aircraft can withstand.

.. py:property:: max_speed_limits
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.max_speed_limits
    :type: "BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS"

    Gets or sets the options of what the procedure will do if the aircraft has exceeded the maximum speed limits.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: powered_cruise_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.powered_cruise_mode
    :type: "BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE"

    Gets or sets the powered cruise mode.

.. py:property:: powered_cruise_throttle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.powered_cruise_throttle
    :type: float

    Gets or sets the powered cruise throttle.

.. py:property:: powered_cruise_thrust_model
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.powered_cruise_thrust_model
    :type: "IAgAvtrPropulsionThrust"

    Get the powered cruise thrust model.

.. py:property:: glide_speed_control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.glide_speed_control_mode
    :type: "BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE"

    Get the glide speed control mode.

.. py:property:: glide_speed_control_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyGlideProfile.glide_speed_control_altitude
    :type: float

    Get the glide speed altitude when using the altitude control mode.


Method detail
-------------











.. py:method:: set_airspeed(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the airspeed and airspeed type that the aircraft will attempt to achieve and maintain if the hold initial airspeed option is not enabled.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`










.. py:method:: set_glide_speed_control_mode(self, eGSMode:"BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE", dControlAlt:float) -> None

    Set the glide speed control mode and altitude.

    :Parameters:

    **eGSMode** : :obj:`~"BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE"`
    **dControlAlt** : :obj:`~float`

    :Returns:

        :obj:`~None`

