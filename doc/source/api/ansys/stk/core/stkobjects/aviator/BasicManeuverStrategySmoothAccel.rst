BasicManeuverStrategySmoothAccel
================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the smooth accel strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategySmoothAccel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.turn_direction`
              - Gets or sets the roll turn direction for a Smooth Accel basic maneuver strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.roll_rate_mode`
              - Gets or sets the roll rate mode for a Smooth Accel basic maneuver strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.override_roll_rate`
              - Gets or sets the roll rate override value for the Smooth Accel basic maneuver strategy. The roll rate mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.roll_rate_dot`
              - Gets or sets the rate of change of the roll rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.control_roll_angle`
              - Gets or sets the option to define a goal value for the aircraft's roll angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.roll_angle`
              - Gets or sets the goal value for the roll angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.load_factor_mode`
              - Gets or sets the load factor mode for the Smooth Accel basic maneuver strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.override_load_factor`
              - Gets or sets the load factor override value for the smooth accel. The load factor mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.load_factor_dot`
              - Gets or sets the rate of change of the load factor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.control_pitch_angle`
              - Gets or sets the option to define a goal value for the aircraft's pitch angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.pitch_angle`
              - Gets or sets the goal value for the pitch angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.stop_conditions`
              - Gets or sets the stop condition for the Smooth Accel basic maneuver strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.stop_on_roll_angle`
              - Gets or sets the option to stop the maneuver if the specified roll angle is achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.stop_on_pitch_angle`
              - Gets or sets the option to stop the maneuver if the specified pitch angle is achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.airspeed_options`
              - Get the airspeed options.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategySmoothAccel


Property detail
---------------

.. py:property:: turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.turn_direction
    :type: SMOOTH_ACCEL_LEFT_RIGHT

    Gets or sets the roll turn direction for a Smooth Accel basic maneuver strategy.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.roll_rate_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the roll rate mode for a Smooth Accel basic maneuver strategy.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.override_roll_rate
    :type: typing.Any

    Gets or sets the roll rate override value for the Smooth Accel basic maneuver strategy. The roll rate mode must be set to override to access this property.

.. py:property:: roll_rate_dot
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.roll_rate_dot
    :type: typing.Any

    Gets or sets the rate of change of the roll rate.

.. py:property:: control_roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.control_roll_angle
    :type: bool

    Gets or sets the option to define a goal value for the aircraft's roll angle.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.roll_angle
    :type: typing.Any

    Gets or sets the goal value for the roll angle.

.. py:property:: load_factor_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.load_factor_mode
    :type: PERF_MODEL_OVERRIDE

    Gets or sets the load factor mode for the Smooth Accel basic maneuver strategy.

.. py:property:: override_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.override_load_factor
    :type: float

    Gets or sets the load factor override value for the smooth accel. The load factor mode must be set to override to access this property.

.. py:property:: load_factor_dot
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.load_factor_dot
    :type: float

    Gets or sets the rate of change of the load factor.

.. py:property:: control_pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.control_pitch_angle
    :type: bool

    Gets or sets the option to define a goal value for the aircraft's pitch angle.

.. py:property:: pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.pitch_angle
    :type: typing.Any

    Gets or sets the goal value for the pitch angle.

.. py:property:: stop_conditions
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.stop_conditions
    :type: SMOOTH_ACCEL_STOP_CONDITIONS

    Gets or sets the stop condition for the Smooth Accel basic maneuver strategy.

.. py:property:: stop_on_roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.stop_on_roll_angle
    :type: bool

    Gets or sets the option to stop the maneuver if the specified roll angle is achieved.

.. py:property:: stop_on_pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.stop_on_pitch_angle
    :type: bool

    Gets or sets the option to stop the maneuver if the specified pitch angle is achieved.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel.airspeed_options
    :type: IBasicManeuverAirspeedOptions

    Get the airspeed options.


