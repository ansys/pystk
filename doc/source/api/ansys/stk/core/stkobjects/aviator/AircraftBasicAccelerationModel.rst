AircraftBasicAccelerationModel
==============================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the basic acceleration performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftBasicAccelerationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.level_turns`
              - Get the level turns interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.attitude_transitions`
              - Get the attitude transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.climb_and_descent_transitions`
              - Get the climb and descent transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.aerodynamics`
              - Get the aerodynamics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.propulsion`
              - Get the propulsion interface.



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

    from ansys.stk.core.stkobjects.aviator import AircraftBasicAccelerationModel


Property detail
---------------

.. py:property:: level_turns
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.level_turns
    :type: LevelTurns

    Get the level turns interface.

.. py:property:: attitude_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.attitude_transitions
    :type: AttitudeTransitions

    Get the attitude transitions interface.

.. py:property:: climb_and_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.climb_and_descent_transitions
    :type: ClimbAndDescentTransitions

    Get the climb and descent transitions interface.

.. py:property:: aerodynamics
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.aerodynamics
    :type: AircraftAerodynamic

    Get the aerodynamics interface.

.. py:property:: propulsion
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.propulsion
    :type: AircraftPropulsion

    Get the propulsion interface.


Method detail
-------------






.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

