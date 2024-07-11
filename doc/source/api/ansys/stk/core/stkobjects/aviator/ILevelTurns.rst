ILevelTurns
===========

.. py:class:: ansys.stk.core.stkobjects.aviator.ILevelTurns

   object
   
   Interface used to access the Level Turns Transitions options found in the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: ILevelTurns

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.set_level_turn`
              - Set the level turn mode and corresponding value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_mode`
              - Get the turn mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_g`
              - Get the TurnG.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.bank_angle`
              - Get the bank angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_acceleration`
              - Get the turn acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_radius`
              - Get the turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_rate`
              - Get the turn rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.maneuver_mode`
              - Gets or sets the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ILevelTurns.maneuver_mode_helper`
              - Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ILevelTurns


Property detail
---------------

.. py:property:: turn_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_mode
    :type: TURN_MODE

    Get the turn mode.

.. py:property:: turn_g
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_g
    :type: float

    Get the TurnG.

.. py:property:: bank_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.bank_angle
    :type: typing.Any

    Get the bank angle.

.. py:property:: turn_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_acceleration
    :type: float

    Get the turn acceleration.

.. py:property:: turn_radius
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_radius
    :type: float

    Get the turn radius.

.. py:property:: turn_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.turn_rate
    :type: float

    Get the turn rate.

.. py:property:: maneuver_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.maneuver_mode
    :type: ACCEL_MANEUVER_MODE

    Gets or sets the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.

.. py:property:: maneuver_mode_helper
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.maneuver_mode_helper
    :type: IAeroPropManeuverModeHelper

    Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.


Method detail
-------------







.. py:method:: set_level_turn(self, turnMode: TURN_MODE, turnValue: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ILevelTurns.set_level_turn

    Set the level turn mode and corresponding value.

    :Parameters:

    **turnMode** : :obj:`~TURN_MODE`
    **turnValue** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`




