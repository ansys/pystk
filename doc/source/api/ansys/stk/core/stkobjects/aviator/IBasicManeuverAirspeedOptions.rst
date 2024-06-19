IBasicManeuverAirspeedOptions
=============================

.. py:class:: IBasicManeuverAirspeedOptions

   object
   
   Interface used to access airspeed options for basic maneuver strategies.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~airspeed_mode`
            * - :py:meth:`~min_speed_limits`
            * - :py:meth:`~max_speed_limits`
            * - :py:meth:`~maintain_airspeed_type`
            * - :py:meth:`~specified_airspeed_type`
            * - :py:meth:`~specified_accel_decel_mode`
            * - :py:meth:`~specified_airspeed`
            * - :py:meth:`~specified_accel_decel_g`
            * - :py:meth:`~accel_g`
            * - :py:meth:`~decel_g`
            * - :py:meth:`~accel_mode`
            * - :py:meth:`~decel_mode`
            * - :py:meth:`~throttle`
            * - :py:meth:`~interpolate_init_g`
            * - :py:meth:`~interpolate_end_g`
            * - :py:meth:`~interpolate_end_time`
            * - :py:meth:`~interpolate_stop_at_end_time`
            * - :py:meth:`~thrust`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverAirspeedOptions


Property detail
---------------

.. py:property:: airspeed_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.airspeed_mode
    :type: BASIC_MANEUVER_AIRSPEED_MODE

    Gets or sets the active airspeed mode.

.. py:property:: min_speed_limits
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.min_speed_limits
    :type: BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS

    Gets or sets the minimum speed limit type to enforce.

.. py:property:: max_speed_limits
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.max_speed_limits
    :type: BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS

    Gets or sets the maximum speed limit type to enforce.

.. py:property:: maintain_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.maintain_airspeed_type
    :type: AIRSPEED_TYPE

    Gets or sets the airspeed type option in the Maintain Current Airspeed mode.

.. py:property:: specified_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.specified_airspeed_type
    :type: AIRSPEED_TYPE

    Gets or sets the airspeed type option in the Maintain Specified Airspeed mode.

.. py:property:: specified_accel_decel_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.specified_accel_decel_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the accel/decel mode for the Maintain Specified Airspeed mode.

.. py:property:: specified_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.specified_airspeed
    :type: float

    Gets or sets the airspeed for the Maintain Specified Airspeed mode.

.. py:property:: specified_accel_decel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.specified_accel_decel_g
    :type: float

    Gets or sets the accel/decel G for the Maintain Specified Airspeed mode.

.. py:property:: accel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.accel_g
    :type: float

    Gets or sets the accel G for the Accelerate at mode.

.. py:property:: decel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.decel_g
    :type: float

    Gets or sets the decel G for the Decelerate at mode.

.. py:property:: accel_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.accel_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the accel mode for the Accelerate at mode.

.. py:property:: decel_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.decel_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the accel mode for the Decelerate at mode.

.. py:property:: throttle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.throttle
    :type: float

    Gets or sets the throttle setting for the Accel/Decel using Aero/Propulsion at mode.

.. py:property:: interpolate_init_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.interpolate_init_g
    :type: float

    Gets or sets the initial G for the Interpolate Accel/Decel over Interval mode.

.. py:property:: interpolate_end_g
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.interpolate_end_g
    :type: float

    Gets or sets the end G for the Interpolate Accel/Decel over Interval mode.

.. py:property:: interpolate_end_time
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.interpolate_end_time
    :type: float

    Gets or sets the end time for the Interpolate Accel/Decel over Interval mode.

.. py:property:: interpolate_stop_at_end_time
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.interpolate_stop_at_end_time
    :type: bool

    Gets or sets the option to stop at the end time for the Interpolate Accel/Decel over Interval mode.

.. py:property:: thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverAirspeedOptions.thrust
    :type: IAgAvtrPropulsionThrust

    Get the thrust options for the Specify Thrust mode.


