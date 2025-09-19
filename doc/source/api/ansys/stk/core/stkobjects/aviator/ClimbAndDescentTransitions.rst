ClimbAndDescentTransitions
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions

   Class defining the climb and descent transition options for an Acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: ClimbAndDescentTransitions

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.ignore_flight_path_angle`
              - Opt whether to ignore the flight path angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.maneuver_mode`
              - Get or set the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.maneuver_mode_helper`
              - Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.max_pull_up_g`
              - Get or set the force normal to the velocity vector used to transition into a climb or to a transition out of a dive into the next flight segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.max_push_over_g`
              - Get or set the force normal to the velocity vector used to transition into a descent or to a transition from a climb into the next flight segment.



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

    from ansys.stk.core.stkobjects.aviator import ClimbAndDescentTransitions


Property detail
---------------

.. py:property:: ignore_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.ignore_flight_path_angle
    :type: bool

    Opt whether to ignore the flight path angle.

.. py:property:: maneuver_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.maneuver_mode
    :type: AccelerationManeuverMode

    Get or set the mode that the aircraft will adhere to the specified acceleration parameters. Scale by atmospheric density will cause the aircraft to consider dynamic pressure when calculating turn radius.

.. py:property:: maneuver_mode_helper
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.maneuver_mode_helper
    :type: AerodynamicPropulsionManeuverModeHelper

    Get the interface for the Aero/Prop Maneuver Mode helper. The maneuver mode must be set to Aero/Prop to access this interface.

.. py:property:: max_pull_up_g
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.max_pull_up_g
    :type: float

    Get or set the force normal to the velocity vector used to transition into a climb or to a transition out of a dive into the next flight segment.

.. py:property:: max_push_over_g
    :canonical: ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions.max_push_over_g
    :type: float

    Get or set the force normal to the velocity vector used to transition into a descent or to a transition from a climb into the next flight segment.


