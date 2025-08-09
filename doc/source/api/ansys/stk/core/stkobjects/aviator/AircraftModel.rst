AircraftModel
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IAviatorVehicle`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining an aircraft in Aviator.

.. py:currentmodule:: AircraftModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.acceleration`
              - Get the acceleration interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.advanced_fixed_wing_tool`
              - Get the Advanced Fixed Wing Tool for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.climb`
              - Get the climb interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.cruise`
              - Get the cruise interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.default_configuration`
              - Get the aircraft's default configuration as saved in the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.descent`
              - Get the descent interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.landing`
              - Get the landing interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.performance_model_types`
              - Get the types of performance models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.takeoff`
              - Get the takeoff interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.terrain_follow`
              - Get the TerrainFollow interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.vtol`
              - Get the VTOL interface.



Examples
--------

Configure the Advanced Fixed Wing Tool and set the aircraft to use the resulting performance models

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the advanced fixed wing tool
    advFixedWingTool = aviatorAircraft.advanced_fixed_wing_tool
    # Set the basic geometry
    advFixedWingTool.wing_area = 300
    advFixedWingTool.flaps_area = 50
    advFixedWingTool.speedbrakes_area = 10
    # Set the structural and human factor limits
    advFixedWingTool.max_altitude = 65000
    advFixedWingTool.max_mach = 0.98
    advFixedWingTool.max_eas = 460
    advFixedWingTool.min_load_factor = -2.5
    advFixedWingTool.max_load_factor = 4.5

    # Opt to enforce the max temperature limit
    advFixedWingTool.use_max_temperature_limit = True
    advFixedWingTool.max_temperature = 900

    # Use a subsonic aerodynamic strategy
    advFixedWingTool.aerodynamic_strategy = AdvancedFixedWingAerodynamicStrategy.SUBSONIC_AERODYNAMIC
    # Cache the aerodynamic data to improve calculation speed
    advFixedWingTool.cache_aerodynamic_data = True
    # Use a high bypass turbofan
    advFixedWingTool.powerplant_strategy = AdvancedFixedWingPowerplantStrategy.TURBOFAN_HIGH_BYPASS
    # Cache the fuel flow data to improve calculation speed
    advFixedWingTool.cache_fuel_flow = True

    # Create the corresponding performance models that reference the advanced fixed wing tool
    # Specify the name, whether to override any existing models with the same name, and whether to set the new models as the default performance models
    advFixedWingTool.create_all_performance_models("AdvancedModels", True, True)

    # Save the changes in the catalog
    aviatorAircraft.save()


Set the aircraft used for the mission to an aircraft found in the Aviator catalog

.. code-block:: python

    # AviatorPropagator propagator: Aviator Propagator object
    # Get the Aviator catalog
    catalog = propagator.aviator_catalog
    # Get the aircraft category
    category = catalog.aircraft_category
    # Get the user aircraft models
    aircraftModels = category.aircraft_models
    # Get the basic fighter
    fighter = aircraftModels.get_aircraft("Basic Fighter")
    # Get the mission
    mission = propagator.aviator_mission
    # Set the vehicle used for the mission
    mission.vehicle = fighter


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


Configure the basic cruise performance model of an aircraft

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the cruise type
    cruise = aviatorAircraft.cruise
    # Get the build in performance model
    basicCruiseModel = cruise.get_built_in_model()

    # Set the ceiling altitude
    basicCruiseModel.ceiling_altitude = 50000
    # Set the default cruise altitude
    basicCruiseModel.default_cruise_altitude = 10000
    # Set the airspeed type
    basicCruiseModel.airspeed_type = AirspeedType.TAS
    # Opt to not use the fuel flow calculated by the aero/prop model and instead specify the values
    basicCruiseModel.use_aerodynamic_propulsion_fuel = False

    # Set the various airspeeds and fuel flows
    basicCruiseModel.min_airspeed = 110
    basicCruiseModel.min_airspeed_fuel_flow = 10000

    basicCruiseModel.max_endurance_airspeed = 135
    basicCruiseModel.max_endurance_fuel_flow = 8000

    basicCruiseModel.max_airspeed = 570
    basicCruiseModel.max_airspeed_fuel_flow = 30000

    basicCruiseModel.max_range_airspeed = 140
    basicCruiseModel.max_range_fuel_flow = 9000

    basicCruiseModel.max_performance_airspeed = 150
    basicCruiseModel.max_performance_airspeed_fuel_flow = 12000

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

    from ansys.stk.core.stkobjects.aviator import AircraftModel


Property detail
---------------

.. py:property:: acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.acceleration
    :type: AircraftAcceleration

    Get the acceleration interface.

.. py:property:: advanced_fixed_wing_tool
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.advanced_fixed_wing_tool
    :type: AdvancedFixedWingTool

    Get the Advanced Fixed Wing Tool for the aircraft.

.. py:property:: climb
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.climb
    :type: AircraftClimb

    Get the climb interface.

.. py:property:: cruise
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.cruise
    :type: AircraftCruise

    Get the cruise interface.

.. py:property:: default_configuration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.default_configuration
    :type: Configuration

    Get the aircraft's default configuration as saved in the catalog.

.. py:property:: descent
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.descent
    :type: AircraftDescent

    Get the descent interface.

.. py:property:: landing
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.landing
    :type: AircraftLanding

    Get the landing interface.

.. py:property:: performance_model_types
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.performance_model_types
    :type: list

    Get the types of performance models.

.. py:property:: takeoff
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.takeoff
    :type: AircraftTakeoff

    Get the takeoff interface.

.. py:property:: terrain_follow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.terrain_follow
    :type: AircraftTerrainFollow

    Get the TerrainFollow interface.

.. py:property:: vtol
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.vtol
    :type: AircraftVTOL

    Get the VTOL interface.


Method detail
-------------







.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`






