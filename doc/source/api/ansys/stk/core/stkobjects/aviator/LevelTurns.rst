LevelTurns
==========

.. py:class:: ansys.stk.core.stkobjects.aviator.LevelTurns

   Class defining the level turns options for an acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: LevelTurns

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.set_level_turn`
              - Set the level turn mode and corresponding value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.turn_mode`
              - Get the turn mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.turn_g`
              - Get the TurnG.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.bank_angle`
              - Get the bank angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.turn_acceleration`
              - Get the turn acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.turn_radius`
              - Get the turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.turn_rate`
              - Get the turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.maneuver_mode`
              - Get or set the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.LevelTurns.maneuver_mode_helper`
              - Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import LevelTurns


Property detail
---------------

.. py:property:: turn_mode
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.turn_mode
    :type: TurnMode

    Get the turn mode.

.. py:property:: turn_g
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.turn_g
    :type: float

    Get the TurnG.

.. py:property:: bank_angle
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.bank_angle
    :type: typing.Any

    Get the bank angle.

.. py:property:: turn_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.turn_acceleration
    :type: float

    Get the turn acceleration.

.. py:property:: turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.turn_radius
    :type: float

    Get the turn radius.

.. py:property:: turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.turn_rate
    :type: float

    Get the turn rate.

.. py:property:: maneuver_mode
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.maneuver_mode
    :type: AccelerationManeuverMode

    Get or set the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.

.. py:property:: maneuver_mode_helper
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.maneuver_mode_helper
    :type: AerodynamicPropulsionManeuverModeHelper

    Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.


Method detail
-------------







.. py:method:: set_level_turn(self, turn_mode: TurnMode, turn_value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.LevelTurns.set_level_turn

    Set the level turn mode and corresponding value.

    :Parameters:

    **turn_mode** : :obj:`~TurnMode`
    **turn_value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`




