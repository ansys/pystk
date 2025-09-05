BasicManeuverStrategyAileronRoll
================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the aileron roll strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyAileronRoll

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_angle`
              - Get or set the roll angle for the active roll mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_mode`
              - Get or set the aileron roll mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_turn_direction`
              - Get or set the roll turn direction for the active roll mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.flight_path_option`
              - Get or set the flight path option.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.override_roll_rate`
              - Get or set the roll rate override value for the aileron roll turn. The roll rate mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.roll_orientation`
              - Get or set the orientation to roll to for the roll to orientation mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.roll_rate_mode`
              - Get or set the roll rate mode for the aileron roll.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyAileronRoll


Property detail
---------------

.. py:property:: active_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_angle
    :type: typing.Any

    Get or set the roll angle for the active roll mode.

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_mode
    :type: AileronRollMode

    Get or set the aileron roll mode.

.. py:property:: active_turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_turn_direction
    :type: RollLeftRight

    Get or set the roll turn direction for the active roll mode.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: flight_path_option
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.flight_path_option
    :type: AileronRollFlightPath

    Get or set the flight path option.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.override_roll_rate
    :type: typing.Any

    Get or set the roll rate override value for the aileron roll turn. The roll rate mode must be set to override to access this property.

.. py:property:: roll_orientation
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.roll_orientation
    :type: RollUprightInverted

    Get or set the orientation to roll to for the roll to orientation mode.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.roll_rate_mode
    :type: PerformanceModelOverride

    Get or set the roll rate mode for the aileron roll.


