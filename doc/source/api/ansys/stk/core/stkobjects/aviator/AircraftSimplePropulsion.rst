AircraftSimplePropulsion
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion

   Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftSimplePropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.set_density_scaling`
              - Set the option to use density scaling and set the density ratio exponent.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.max_thrust_acceleration`
              - Get or set the rate at which the aircraft speeds up at max throttle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.min_thrust_deceleration`
              - Get or set the rate at which the aircraft slows down at minimum throttle setting.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.use_density_scaling`
              - Opt whether to scale the accel/decel performance by the density ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.density_ratio_exponent`
              - Get the relative impace of atmospheric density on the aircraft's performance.



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

    from ansys.stk.core.stkobjects.aviator import AircraftSimplePropulsion


Property detail
---------------

.. py:property:: max_thrust_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.max_thrust_acceleration
    :type: float

    Get or set the rate at which the aircraft speeds up at max throttle.

.. py:property:: min_thrust_deceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.min_thrust_deceleration
    :type: float

    Get or set the rate at which the aircraft slows down at minimum throttle setting.

.. py:property:: use_density_scaling
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.use_density_scaling
    :type: bool

    Opt whether to scale the accel/decel performance by the density ratio.

.. py:property:: density_ratio_exponent
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.density_ratio_exponent
    :type: float

    Get the relative impace of atmospheric density on the aircraft's performance.


Method detail
-------------







.. py:method:: set_density_scaling(self, use_scaling: bool, exponent: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion.set_density_scaling

    Set the option to use density scaling and set the density ratio exponent.

    :Parameters:

        **use_scaling** : :obj:`~bool`

        **exponent** : :obj:`~float`


    :Returns:

        :obj:`~None`

