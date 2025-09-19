AircraftAerodynamic
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic

   Class defining the aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.aerodynamic_strategy`
              - Get or set the aerodynamic strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.drag_factor`
              - Get or set the scalar value applied to the drag for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.lift_factor`
              - Get or set the scalar value applied to the lift for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_advanced_missile`
              - Get the interface for an advanced missile aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_basic_fixed_wing`
              - Get the interface for a basic fixed wing aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_external`
              - Get the interface for an external file aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_four_point`
              - Get the interface for a four point aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_simple`
              - Get the interface for a simple aerodynamics strategy.



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

    from ansys.stk.core.stkobjects.aviator import AircraftAerodynamic


Property detail
---------------

.. py:property:: aerodynamic_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.aerodynamic_strategy
    :type: AircraftAerodynamicStrategy

    Get or set the aerodynamic strategy type.

.. py:property:: drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.drag_factor
    :type: float

    Get or set the scalar value applied to the drag for parametric analysis.

.. py:property:: lift_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.lift_factor
    :type: float

    Get or set the scalar value applied to the lift for parametric analysis.

.. py:property:: mode_as_advanced_missile
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_advanced_missile
    :type: MissileAdvancedAerodynamic

    Get the interface for an advanced missile aerodynamics strategy.

.. py:property:: mode_as_basic_fixed_wing
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_basic_fixed_wing
    :type: AircraftBasicFixedWingAerodynamic

    Get the interface for a basic fixed wing aerodynamics strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_external
    :type: AircraftExternalAerodynamic

    Get the interface for an external file aerodynamics strategy.

.. py:property:: mode_as_four_point
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_four_point
    :type: FourPointAerodynamic

    Get the interface for a four point aerodynamics strategy.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_simple
    :type: AircraftSimpleAerodynamic

    Get the interface for a simple aerodynamics strategy.


