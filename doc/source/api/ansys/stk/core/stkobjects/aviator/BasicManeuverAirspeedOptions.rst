BasicManeuverAirspeedOptions
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions

   Class defining the airspeed options for basic maneuver strategies.

.. py:currentmodule:: BasicManeuverAirspeedOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.airspeed_mode`
              - Get or set the active airspeed mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.min_speed_limits`
              - Get or set the minimum speed limit type to enforce.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.max_speed_limits`
              - Get or set the maximum speed limit type to enforce.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.maintain_airspeed_type`
              - Get or set the airspeed type option in the Maintain Current Airspeed mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.specified_airspeed_type`
              - Get or set the airspeed type option in the Maintain Specified Airspeed mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.specified_acceleration_deceleration_mode`
              - Get or set the accel/decel mode for the Maintain Specified Airspeed mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.specified_airspeed`
              - Get or set the airspeed for the Maintain Specified Airspeed mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.specified_acceleration_deceleration_g`
              - Get or set the accel/decel G for the Maintain Specified Airspeed mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.acceleration_g`
              - Get or set the accel G for the Accelerate at mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.deceleration_g`
              - Get or set the decel G for the Decelerate at mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.acceleration_mode`
              - Get or set the accel mode for the Accelerate at mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.deceleration_mode`
              - Get or set the accel mode for the Decelerate at mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.throttle`
              - Get or set the throttle setting for the Accel/Decel using Aero/Propulsion at mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.interpolate_init_g`
              - Get or set the initial G for the Interpolate Accel/Decel over Interval mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.interpolate_end_g`
              - Get or set the end G for the Interpolate Accel/Decel over Interval mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.interpolate_end_time`
              - Get or set the end time for the Interpolate Accel/Decel over Interval mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.interpolate_stop_at_end_time`
              - Get or set the option to stop at the end time for the Interpolate Accel/Decel over Interval mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.thrust`
              - Get the thrust options for the Specify Thrust mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverAirspeedOptions


Property detail
---------------

.. py:property:: airspeed_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.airspeed_mode
    :type: BasicManeuverAirspeedMode

    Get or set the active airspeed mode.

.. py:property:: min_speed_limits
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.min_speed_limits
    :type: BasicManeuverStrategyAirspeedPerformanceLimits

    Get or set the minimum speed limit type to enforce.

.. py:property:: max_speed_limits
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.max_speed_limits
    :type: BasicManeuverStrategyAirspeedPerformanceLimits

    Get or set the maximum speed limit type to enforce.

.. py:property:: maintain_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.maintain_airspeed_type
    :type: AirspeedType

    Get or set the airspeed type option in the Maintain Current Airspeed mode.

.. py:property:: specified_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.specified_airspeed_type
    :type: AirspeedType

    Get or set the airspeed type option in the Maintain Specified Airspeed mode.

.. py:property:: specified_acceleration_deceleration_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.specified_acceleration_deceleration_mode
    :type: PerformanceModelOverride

    Get or set the accel/decel mode for the Maintain Specified Airspeed mode.

.. py:property:: specified_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.specified_airspeed
    :type: float

    Get or set the airspeed for the Maintain Specified Airspeed mode.

.. py:property:: specified_acceleration_deceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.specified_acceleration_deceleration_g
    :type: float

    Get or set the accel/decel G for the Maintain Specified Airspeed mode.

.. py:property:: acceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.acceleration_g
    :type: float

    Get or set the accel G for the Accelerate at mode.

.. py:property:: deceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.deceleration_g
    :type: float

    Get or set the decel G for the Decelerate at mode.

.. py:property:: acceleration_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.acceleration_mode
    :type: PerformanceModelOverride

    Get or set the accel mode for the Accelerate at mode.

.. py:property:: deceleration_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.deceleration_mode
    :type: PerformanceModelOverride

    Get or set the accel mode for the Decelerate at mode.

.. py:property:: throttle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.throttle
    :type: float

    Get or set the throttle setting for the Accel/Decel using Aero/Propulsion at mode.

.. py:property:: interpolate_init_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.interpolate_init_g
    :type: float

    Get or set the initial G for the Interpolate Accel/Decel over Interval mode.

.. py:property:: interpolate_end_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.interpolate_end_g
    :type: float

    Get or set the end G for the Interpolate Accel/Decel over Interval mode.

.. py:property:: interpolate_end_time
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.interpolate_end_time
    :type: float

    Get or set the end time for the Interpolate Accel/Decel over Interval mode.

.. py:property:: interpolate_stop_at_end_time
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.interpolate_stop_at_end_time
    :type: bool

    Get or set the option to stop at the end time for the Interpolate Accel/Decel over Interval mode.

.. py:property:: thrust
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions.thrust
    :type: PropulsionThrust

    Get the thrust options for the Specify Thrust mode.


