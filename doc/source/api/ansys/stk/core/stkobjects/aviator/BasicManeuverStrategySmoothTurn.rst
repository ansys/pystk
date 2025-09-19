BasicManeuverStrategySmoothTurn
===============================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the smooth turn strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategySmoothTurn

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.flight_path_angle_mode`
              - Get or set the flight path angle mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.heading_change`
              - Get or set the heading change for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.load_factor_mode`
              - Get or set the load factor mode for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.max_load_factor_rate`
              - Get or set the max load factor rate for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.override_load_factor`
              - Get or set the max load factor override value for the smooth turn. The load factor mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.override_roll_rate`
              - Get or set the max roll rate override value for the smooth turn. The roll rate mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.roll_angle`
              - Get or set the roll angle for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.roll_rate_mode`
              - Get or set the roll rate mode for the smooth turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.turn_mode`
              - Get or set the turn mode for the smooth turn.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategySmoothTurn


Property detail
---------------

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: flight_path_angle_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.flight_path_angle_mode
    :type: SmoothTurnFlightPathAngleMode

    Get or set the flight path angle mode.

.. py:property:: heading_change
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.heading_change
    :type: typing.Any

    Get or set the heading change for the smooth turn.

.. py:property:: load_factor_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.load_factor_mode
    :type: PerformanceModelOverride

    Get or set the load factor mode for the smooth turn.

.. py:property:: max_load_factor_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.max_load_factor_rate
    :type: float

    Get or set the max load factor rate for the smooth turn.

.. py:property:: override_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.override_load_factor
    :type: float

    Get or set the max load factor override value for the smooth turn. The load factor mode must be set to override to access this property.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.override_roll_rate
    :type: typing.Any

    Get or set the max roll rate override value for the smooth turn. The roll rate mode must be set to override to access this property.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.roll_angle
    :type: typing.Any

    Get or set the roll angle for the smooth turn.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.roll_rate_mode
    :type: PerformanceModelOverride

    Get or set the roll rate mode for the smooth turn.

.. py:property:: turn_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn.turn_mode
    :type: SmoothTurnMode

    Get or set the turn mode for the smooth turn.


