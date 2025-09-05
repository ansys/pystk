AircraftPropulsion
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftPropulsion

   Class defining the propulsion options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.drag_factor`
              - Get or set the scalar value applied to the drag for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.lift_factor`
              - Get or set the scalar value applied to the lift for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_basic_fixed_wing`
              - Get the interface for a basic fixed wing propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_external`
              - Get the interface for an external file propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_ramjet`
              - Get the interface for a Ramjet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_rocket`
              - Get the interface for a Rocket propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_simple`
              - Get the interface for a simple propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_turbojet`
              - Get the interface for a Turbojet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.propulsion_strategy`
              - Get or set the propulsion strategy type.



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

    from ansys.stk.core.stkobjects.aviator import AircraftPropulsion


Property detail
---------------

.. py:property:: drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.drag_factor
    :type: float

    Get or set the scalar value applied to the drag for parametric analysis.

.. py:property:: lift_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.lift_factor
    :type: float

    Get or set the scalar value applied to the lift for parametric analysis.

.. py:property:: mode_as_basic_fixed_wing
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_basic_fixed_wing
    :type: AircraftBasicFixedWingPropulsion

    Get the interface for a basic fixed wing propulsion strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_external
    :type: AircraftExternalPropulsion

    Get the interface for an external file propulsion strategy.

.. py:property:: mode_as_ramjet
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_ramjet
    :type: MissileRamjetPropulsion

    Get the interface for a Ramjet propulsion strategy.

.. py:property:: mode_as_rocket
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_rocket
    :type: MissileRocketPropulsion

    Get the interface for a Rocket propulsion strategy.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_simple
    :type: AircraftSimplePropulsion

    Get the interface for a simple propulsion strategy.

.. py:property:: mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_turbojet
    :type: MissileTurbojetPropulsion

    Get the interface for a Turbojet propulsion strategy.

.. py:property:: propulsion_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.propulsion_strategy
    :type: AircraftPropulsionStrategy

    Get or set the propulsion strategy type.


