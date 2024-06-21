IBasicManeuverStrategySmoothAccel
=================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel

   object
   
   Interface used to access options for a Smooth Accel Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: IBasicManeuverStrategySmoothAccel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.turn_direction`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.roll_rate_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.override_roll_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.roll_rate_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.control_roll_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.roll_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.load_factor_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.override_load_factor`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.load_factor_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.control_pitch_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.pitch_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.stop_conditions`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.stop_on_roll_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.stop_on_pitch_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.airspeed_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategySmoothAccel


Property detail
---------------

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.turn_direction
    :type: SMOOTH_ACCEL_LEFT_RIGHT

    Gets or sets the roll turn direction for a Smooth Accel basic maneuver strategy.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.roll_rate_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the roll rate mode for a Smooth Accel basic maneuver strategy.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.override_roll_rate
    :type: typing.Any

    Gets or sets the roll rate override value for the Smooth Accel basic maneuver strategy. The roll rate mode must be set to override to access this property.

.. py:property:: roll_rate_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.roll_rate_dot
    :type: typing.Any

    Gets or sets the rate of change of the roll rate.

.. py:property:: control_roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.control_roll_angle
    :type: bool

    Gets or sets the option to define a goal value for the aircraft's roll angle.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.roll_angle
    :type: typing.Any

    Gets or sets the goal value for the roll angle.

.. py:property:: load_factor_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.load_factor_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the load factor mode for the Smooth Accel basic maneuver strategy.

.. py:property:: override_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.override_load_factor
    :type: float

    Gets or sets the load factor override value for the smooth accel. The load factor mode must be set to override to access this property.

.. py:property:: load_factor_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.load_factor_dot
    :type: float

    Gets or sets the rate of change of the load factor.

.. py:property:: control_pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.control_pitch_angle
    :type: bool

    Gets or sets the option to define a goal value for the aircraft's pitch angle.

.. py:property:: pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.pitch_angle
    :type: typing.Any

    Gets or sets the goal value for the pitch angle.

.. py:property:: stop_conditions
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.stop_conditions
    :type: SMOOTH_ACCEL_STOP_CONDITIONS

    Gets or sets the stop condition for the Smooth Accel basic maneuver strategy.

.. py:property:: stop_on_roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.stop_on_roll_angle
    :type: bool

    Gets or sets the option to stop the maneuver if the specified roll angle is achieved.

.. py:property:: stop_on_pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.stop_on_pitch_angle
    :type: bool

    Gets or sets the option to stop the maneuver if the specified pitch angle is achieved.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySmoothAccel.airspeed_options
    :type: IBasicManeuverAirspeedOptions

    Get the airspeed options.


