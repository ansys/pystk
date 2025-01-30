BasicManeuverStrategyGlideProfile
=================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Glide profile strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyGlideProfile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.set_airspeed`
              - Set the airspeed and airspeed type that the aircraft will attempt to achieve and maintain if the hold initial airspeed option is not enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.set_glide_speed_control_mode`
              - Set the glide speed control mode and altitude.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.hold_initial_airspeed`
              - Select whether to maintain the airspeed of the aircraft at the beginning of the procedure throughout the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.airspeed`
              - Get the airspeed the aircraft will attempt to achieve and maintain if the hold initial airspeed option is not enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.min_g`
              - Gets or sets the minimum load factor the aircraft can withstand.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.max_g`
              - Gets or sets the maximum load factor the aircraft can withstand.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.max_speed_limits`
              - Gets or sets the options of what the procedure will do if the aircraft has exceeded the maximum speed limits.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.compensate_for_coriolis_acceleration`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.powered_cruise_mode`
              - Gets or sets the powered cruise mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.powered_cruise_throttle`
              - Gets or sets the powered cruise throttle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.powered_cruise_thrust_model`
              - Get the powered cruise thrust model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.glide_speed_control_mode`
              - Get the glide speed control mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.glide_speed_control_altitude`
              - Get the glide speed altitude when using the altitude control mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyGlideProfile


Property detail
---------------

.. py:property:: hold_initial_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.hold_initial_airspeed
    :type: bool

    Select whether to maintain the airspeed of the aircraft at the beginning of the procedure throughout the maneuver.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.airspeed
    :type: float

    Get the airspeed the aircraft will attempt to achieve and maintain if the hold initial airspeed option is not enabled.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: min_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.min_g
    :type: float

    Gets or sets the minimum load factor the aircraft can withstand.

.. py:property:: max_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.max_g
    :type: float

    Gets or sets the maximum load factor the aircraft can withstand.

.. py:property:: max_speed_limits
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.max_speed_limits
    :type: BasicManeuverStrategyAirspeedPerformanceLimits

    Gets or sets the options of what the procedure will do if the aircraft has exceeded the maximum speed limits.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.compensate_for_coriolis_acceleration
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.

.. py:property:: powered_cruise_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.powered_cruise_mode
    :type: BasicManeuverStrategyPoweredCruiseMode

    Gets or sets the powered cruise mode.

.. py:property:: powered_cruise_throttle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.powered_cruise_throttle
    :type: float

    Gets or sets the powered cruise throttle.

.. py:property:: powered_cruise_thrust_model
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.powered_cruise_thrust_model
    :type: PropulsionThrust

    Get the powered cruise thrust model.

.. py:property:: glide_speed_control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.glide_speed_control_mode
    :type: BasicManeuverGlideSpeedControlMode

    Get the glide speed control mode.

.. py:property:: glide_speed_control_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.glide_speed_control_altitude
    :type: float

    Get the glide speed altitude when using the altitude control mode.


Method detail
-------------











.. py:method:: set_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.set_airspeed

    Set the airspeed and airspeed type that the aircraft will attempt to achieve and maintain if the hold initial airspeed option is not enabled.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`










.. py:method:: set_glide_speed_control_mode(self, glide_speed_mode: BasicManeuverGlideSpeedControlMode, control_altitude: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile.set_glide_speed_control_mode

    Set the glide speed control mode and altitude.

    :Parameters:

    **glide_speed_mode** : :obj:`~BasicManeuverGlideSpeedControlMode`
    **control_altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`

