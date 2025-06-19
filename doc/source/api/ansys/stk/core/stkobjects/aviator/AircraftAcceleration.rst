AircraftAcceleration
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAcceleration

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the aircraft acceleration category of an Aviator aircraft.

.. py:currentmodule:: AircraftAcceleration

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_built_in_model`
              - Get the built-in model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_basic_acceleration_by_name`
              - Get the basic acceleration model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_advanced_acceleration_by_name`
              - Get the advanced acceleration model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_as_catalog_item`
              - Get the catalog item interface for this object.


Examples
--------

Create a new performance model for an aircraft

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the acceleration type
    acceleration = aviatorAircraft.acceleration
    # Get the names of the current acceleration models
    modelNames = acceleration.child_names
    # Check how many models there are
    modelCount = len(modelNames)
    # Get the child types (for example AGI Basic Acceleration Model, Advanced Acceleration Model)
    modelTypes = acceleration.child_types
    # Create a new performance model of type "Advanced Acceleration Model"
    newPerformanceModel = acceleration.add_child_of_type("Advanced Acceleration Model", "Model Name")
    # Save the changes to the catalog
    aviatorAircraft.save()


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

    from ansys.stk.core.stkobjects.aviator import AircraftAcceleration



Method detail
-------------

.. py:method:: get_built_in_model(self) -> AircraftBasicAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~AircraftBasicAccelerationModel`

.. py:method:: get_basic_acceleration_by_name(self, name: str) -> AircraftBasicAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_basic_acceleration_by_name

    Get the basic acceleration model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftBasicAccelerationModel`

.. py:method:: get_advanced_acceleration_by_name(self, name: str) -> AircraftAdvancedAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_advanced_acceleration_by_name

    Get the advanced acceleration model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftAdvancedAccelerationModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

