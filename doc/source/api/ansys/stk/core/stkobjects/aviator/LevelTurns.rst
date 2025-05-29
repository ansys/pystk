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



Examples
--------

Configure the basic acceleration performance model of an aircraft

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the acceleration type
    acceleration = aviatorAircraft.acceleration
    # Get the build in performance model
    basicAccModel = acceleration.get_built_in_model()

    # Get the level turns options
    levelTurns = basicAccModel.level_turns
    # Set a max bank angle of 25
    levelTurns.set_level_turn(TurnMode.TURN_MODE_BANK_ANGLE, 25)
    # Get the climb and descent transition options
    climbAndDescent = basicAccModel.climb_and_descent_transitions
    # Set the max pull up G to 1
    climbAndDescent.max_pull_up_g = 1.2
    # Get the attitude transition options
    attitudeTransitions = basicAccModel.attitude_transitions
    # Set the max roll rate to 25
    attitudeTransitions.roll_rate = 25

    # Get the aerodynamics
    aero = basicAccModel.aerodynamics
    # Use simple aerodynamics
    aero.aerodynamic_strategy = AircraftAerodynamicStrategy.AIRCRAFT_AERODYNAMIC_SIMPLE
    # Get the options for the simple aerodynamics and set some parameters
    simpleAero = aero.mode_as_simple
    simpleAero.s_reference = 5
    simpleAero.cl_max = 3.1
    simpleAero.cd = 0.05

    # Get the propulsion
    prop = basicAccModel.propulsion
    # Use simple propulsion
    prop.propulsion_strategy = AircraftPropulsionStrategy.AIRCRAFT_PROPULSION_SIMPLE
    # Get the simple propulsion options and set some parameters
    simpleProp = prop.mode_as_simple
    simpleProp.max_thrust_acceleration = 0.6
    simpleProp.min_thrust_deceleration = 0.4
    simpleProp.set_density_scaling(True, 0.02)

    # Save the changes to the catalog
    aviatorAircraft.save()


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




