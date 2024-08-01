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

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.flight_path_option`
              - Gets or sets the flight path option.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_mode`
              - Gets or sets the aileron roll mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_turn_direction`
              - Gets or sets the roll turn direction for the active roll mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_angle`
              - Gets or sets the roll angle for the active roll mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.roll_orientation`
              - Gets or sets the orientation to roll to for the roll to orientation mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.roll_rate_mode`
              - Gets or sets the roll rate mode for the aileron roll.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.override_roll_rate`
              - Gets or sets the roll rate override value for the aileron roll turn. The roll rate mode must be set to override to access this property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.airspeed_options`
              - Get the airspeed options.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyAileronRoll


Property detail
---------------

.. py:property:: flight_path_option
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.flight_path_option
    :type: AILERON_ROLL_FLIGHT_PATH

    Gets or sets the flight path option.

.. py:property:: active_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_mode
    :type: AILERON_ROLL_MODE

    Gets or sets the aileron roll mode.

.. py:property:: active_turn_direction
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_turn_direction
    :type: ROLL_LEFT_RIGHT

    Gets or sets the roll turn direction for the active roll mode.

.. py:property:: active_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.active_angle
    :type: typing.Any

    Gets or sets the roll angle for the active roll mode.

.. py:property:: roll_orientation
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.roll_orientation
    :type: ROLL_UPRIGHT_INVERTED

    Gets or sets the orientation to roll to for the roll to orientation mode.

.. py:property:: roll_rate_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.roll_rate_mode
    :type: PERFORMANCE_MODEL_OVERRIDE

    Gets or sets the roll rate mode for the aileron roll.

.. py:property:: override_roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.override_roll_rate
    :type: typing.Any

    Gets or sets the roll rate override value for the aileron roll turn. The roll rate mode must be set to override to access this property.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll.airspeed_options
    :type: IBasicManeuverAirspeedOptions

    Get the airspeed options.


