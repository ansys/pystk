AircraftSimpleAerodynamic
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic

   Class defining the simple aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftSimpleAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.cd`
              - Get or set the coefficient of drag.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.cl_max`
              - Get or set the max coefficient of lift.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.operating_mode`
              - Get or set the mode option to treat the aircraft as a helicopter or a fixed wing aircraft when calculating the aircraft's attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.s_reference`
              - Get or set the reference surface area of the aircraft.



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

    from ansys.stk.core.stkobjects.aviator import AircraftSimpleAerodynamic


Property detail
---------------

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.cd
    :type: float

    Get or set the coefficient of drag.

.. py:property:: cl_max
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.cl_max
    :type: float

    Get or set the max coefficient of lift.

.. py:property:: operating_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.operating_mode
    :type: AerodynamicPropulsionSimpleMode

    Get or set the mode option to treat the aircraft as a helicopter or a fixed wing aircraft when calculating the aircraft's attitude.

.. py:property:: s_reference
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic.s_reference
    :type: float

    Get or set the reference surface area of the aircraft.


