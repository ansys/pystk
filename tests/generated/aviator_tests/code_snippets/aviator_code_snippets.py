# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.aviator import *


class AviatorCodeSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(AviatorCodeSnippets, self).__init__(*args, **kwargs)

    # region Static DataMembers
    AG_Scenario: "IStkObject" = None
    AG_AC: "Aircraft" = None
    AG_AvtrProp: "AviatorPropagator" = None
    AG_AvtrCatalog: "Catalog" = None
    AG_AvtrAircraftModels: "AircraftModels" = None
    AG_Mission: "Mission" = None
    AG_Phases: "PhaseCollection" = None
    AG_Procedures: "ProcedureCollection" = None
    AG_AvtrAircraft: "AircraftModel" = None
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        scenario: "IStkObject" = clr.CastAs(TestBase.Application.current_scenario, IStkObject)
        AviatorCodeSnippets.AG_Scenario = scenario
        AviatorCodeSnippets.AG_AC = Aircraft((scenario.children.new(STKObjectType.AIRCRAFT, "AviatorAC")))
        # Set to Propagator to Aviator
        AviatorCodeSnippets.AG_AC.set_route_type(PropagatorType.AVIATOR)
        # Get the aircrafts route (still on the STKObjects side)
        aircraftRoute: "PropagatorAviator" = clr.CastAs(AviatorCodeSnippets.AG_AC.route, PropagatorAviator)
        # Get the Aviator propagator
        AviatorCodeSnippets.AG_AvtrProp = clr.CastAs(aircraftRoute.aviator_propagator, AviatorPropagator)
        # Get the Aviator mission
        AviatorCodeSnippets.AG_Mission = AviatorCodeSnippets.AG_AvtrProp.aviator_mission
        # Get the phases
        AviatorCodeSnippets.AG_Phases = AviatorCodeSnippets.AG_Mission.phases
        # Get the procedures
        AviatorCodeSnippets.AG_Procedures = AviatorCodeSnippets.AG_Phases[0].procedures
        # Get the Aviator Catalog
        AviatorCodeSnippets.AG_AvtrCatalog = AviatorCodeSnippets.AG_AvtrProp.aviator_catalog
        # Get the User Aircraft Models
        AviatorCodeSnippets.AG_AvtrAircraftModels = AviatorCodeSnippets.AG_AvtrCatalog.aircraft_category.aircraft_models
        # Duplicate the basic airliner
        AviatorCodeSnippets.AG_AvtrAircraft = clr.CastAs(
            AviatorCodeSnippets.AG_AvtrAircraftModels.get_aircraft("Basic Airliner").get_as_catalog_item().duplicate(),
            AircraftModel,
        )
        # Use the aircraft in the misison
        AviatorCodeSnippets.AG_Mission.vehicle = clr.CastAs(AviatorCodeSnippets.AG_AvtrAircraft, IAviatorVehicle)

    # endregion

    # region TestTearDown
    def tearDown(self):
        (IStkObject(AviatorCodeSnippets.AG_AC)).unload()
        AviatorCodeSnippets.AG_AC = None
        AviatorCodeSnippets.AG_AvtrAircraft.get_as_catalog_item().remove()

    # endregion

    # region ConfigureAviatorPropagator
    def test_ConfigureAviatorPropagator(self):
        self.ConfigureAviatorPropagator(AviatorCodeSnippets.AG_AC)

    def ConfigureAviatorPropagator(self, aircraft: "Aircraft"):
        # Set to Propagator to Aviator
        aircraft.set_route_type(PropagatorType.AVIATOR)
        # Get the aircraft's route
        aircraftRoute: "PropagatorAviator" = clr.CastAs(aircraft.route, PropagatorAviator)
        # Get the Aviator propagator
        propagator: "AviatorPropagator" = clr.CastAs(aircraftRoute.aviator_propagator, AviatorPropagator)
        # Get the Aviator mission
        mission: "Mission" = propagator.aviator_mission
        # Get the list of phases from the mission
        phases: "PhaseCollection" = mission.phases
        # Get the list of procedures from the first phase
        procedures: "ProcedureCollection" = phases[0].procedures
        # Propagate the route
        propagator.propagate()

    # endregion

    # region SetTheConfiguration
    def test_SetTheConfiguration(self):
        self.SetTheConfiguration(AviatorCodeSnippets.AG_Mission)

    def SetTheConfiguration(self, mission: "Mission"):
        # Get the configuration used for the mission
        configuration: "Configuration" = mission.configuration
        # Set the max landing weight
        configuration.max_landing_weight = 300000
        # Set the empty weight
        configuration.empty_weight = 210000
        # Update the center of gravity of the aircraft when empty
        configuration.set_empty_cg(2, 0, 1)

        # Get the stations
        stations: "StationCollection" = configuration.get_stations()
        # Check if there is an internal fuel station
        hasInternalFuel: bool = stations.contains_station("Internal Fuel")
        if hasInternalFuel:
            # Get the fuel tank
            fuelTank: "FuelTankInternal" = stations.get_internal_fuel_tank_by_name("Internal Fuel")
            # Set the capacity of the fuel tank
            fuelTank.capacity = 175000
            # Set the initial state of the fuel tank
            fuelTank.initial_fuel_state = 125000

        # Add a new payload station
        newPayload: "PayloadStation" = stations.add_payload_station()
        # Set the position of the payload station
        newPayload.set_position(0, 2, 0)
        # Add an external fuel tank
        externalTank: "FuelTankExternal" = newPayload.add_external_fuel_tank()
        # Set the empty weight of the tank
        externalTank.empty_weight = 2000

    # endregion

    # region ConfigureWeatherAtmosphere
    def test_ConfigureWeatherAtmosphere(self):
        self.ConfigureWeatherAtmosphere(AviatorCodeSnippets.AG_Mission)

    def ConfigureWeatherAtmosphere(self, mission: "Mission"):
        # Get the wind model used for the mission
        windModel: "WindModel" = mission.wind_model
        # Let's use the mission model
        windModel.wind_model_source = WindAtmosphereModelSource.MISSION_MODEL
        # Let's use constant wind
        windModel.wind_model_type = WindModelType.CONSTANT_WIND
        # Get the constant wind model options
        constantWind: "WindModelConstant" = windModel.mode_as_constant
        # Set the wind bearing
        constantWind.wind_bearing = 30
        # Set the wind speed
        constantWind.wind_speed = 5

        # Get the atmosphere model used for the mission
        atmosphere: "AtmosphereModel" = mission.atmosphere_model
        # Let's use the mission model
        atmosphere.atmosphere_model_source = WindAtmosphereModelSource.MISSION_MODEL
        # Get the basic atmosphere options
        basicAtmosphere: "AtmosphereModelBasic" = atmosphere.mode_as_basic
        # Use standard 1976 atmosphere
        basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976
        # Opt to override the values
        basicAtmosphere.use_non_standard_atmosphere = True
        # Override the temperature
        basicAtmosphere.temperature = 290

    # endregion

    # region SetAviatorVehicle
    def test_SetAviatorVehicle(self):
        self.SetAviatorVehicle(AviatorCodeSnippets.AG_AvtrProp)
        AviatorCodeSnippets.AG_Mission.vehicle = clr.CastAs(AviatorCodeSnippets.AG_AvtrAircraft, IAviatorVehicle)

    def SetAviatorVehicle(self, propagator: "AviatorPropagator"):
        # Get the Aviator catalog
        catalog: "Catalog" = propagator.aviator_catalog
        # Get the aircraft category
        category: "AircraftCategory" = catalog.aircraft_category
        # Get the user aircraft models
        aircraftModels: "AircraftModels" = category.aircraft_models
        # Get the basic fighter
        fighter: "AircraftModel" = aircraftModels.get_aircraft("Basic Fighter")
        # Get the mission
        mission: "Mission" = propagator.aviator_mission
        # Set the vehicle used for the mission
        mission.vehicle = clr.CastAs(fighter, IAviatorVehicle)

    # endregion

    # region SetupAdvancedFixedWingTool
    def test_SetupAdvancedFixedWingTool(self):
        self.SetupAdvancedFixedWingTool(AviatorCodeSnippets.AG_AvtrAircraft)

    def SetupAdvancedFixedWingTool(self, aviatorAircraft: "AircraftModel"):
        # Get the advanced fixed wing tool
        advFixedWingTool: "AdvancedFixedWingTool" = aviatorAircraft.advanced_fixed_wing_tool
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
        aviatorAircraft.get_as_catalog_item().save()

    # endregion

    # region ConfigurePhasePerformanceModels
    def test_ConfigurePhasePerformanceModels(self):
        self.ConfigurePhasePerformanceModels(AviatorCodeSnippets.AG_Phases[0])

    def ConfigurePhasePerformanceModels(self, phase: "Phase"):
        # Get the acceleration performance model used for the current phase
        acceleration: "PerformanceModelOptions" = phase.get_performance_model_by_type("Acceleration")
        # Check if it is linked to the catalog
        isLinkedToCatalog: bool = acceleration.is_linked_to_catalog
        # Use the performance model in the catalog named "Built-In Model"
        acceleration.link_to_catalog("Built-In Model")

        # Get the VTOL performance model
        vtol: "PerformanceModelOptions" = phase.get_performance_model_by_type("VTOL")
        # Create a new vtol model of type AGI VTOL Model. Note that this new model does not exist in the catalog and only exists in the phase.
        vtol.create_new("AGI VTOL Model")
        # Rename the performance model
        vtol.rename("Temporary VTOL Model")

    # endregion

    # region AddPhase
    def test_AddPhase(self):
        self.AddPhase(AviatorCodeSnippets.AG_Phases)

    def AddPhase(self, phases: "PhaseCollection"):
        # Add a new phase at the end of the mission
        newPhase: "Phase" = phases.add()
        # Rename the phase
        newPhase.name = "New Phase"
        # Copy the performance models from the first phase and paste it to the new phase
        phases[0].copy_performance_models()
        newPhase.paste_performance_models()

    # endregion

    # region AddAndRemoveProcedures
    def test_AddAndRemoveProcedures(self):
        self.AddAndRemoveProcedures(AviatorCodeSnippets.AG_Procedures, AviatorCodeSnippets.AG_AvtrProp)

    def AddAndRemoveProcedures(self, procedures: "ProcedureCollection", propagator: "AviatorPropagator"):
        # Add a takeoff procedure with a runway as a site. This will add the procedure
        takeoff: "IProcedure" = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
        # Add a procedure at a given index (starting from 0)
        enroute: "IProcedure" = procedures.add_at_index(
            1, SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE
        )

        # Make sure to propagate the mission to calculate the route
        propagator.propagate()
        # Get the mission
        mission: "Mission" = propagator.aviator_mission
        # Check to see if the mission is valid (must first be propagated)
        isValid: bool = mission.is_valid

        # Get the number of procedures
        procedureCount: int = procedures.count
        # Remove the procedure at the given index
        procedures.remove_at_index(1)
        # Remove the given procedure
        procedures.remove(takeoff)

        # Propagate the mission
        propagator.propagate()

    # endregion

    # region ConfigureProcedure
    def test_ConfigureProcedure(self):
        procedure: "IProcedure" = AviatorCodeSnippets.AG_Procedures.add(
            SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF
        )
        self.ConfigureProcedure(procedure)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)

    def ConfigureProcedure(self, procedure: "IProcedure"):
        # Rename the procedure
        procedure.name = "New Procedure"
        # Get the site corresponding to the procedure
        site: "ISite" = procedure.site
        # Rename the site
        site.name = "New Site"

    # endregion

    # region ConfigureProcedureWindAtmos
    def test_ConfigureProcedureWindAtmos(self):
        procedure: "IProcedure" = AviatorCodeSnippets.AG_Procedures.add(
            SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF
        )
        self.ConfigureProcedureWindAtmos(procedure)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)

    def ConfigureProcedureWindAtmos(self, procedure: "IProcedure"):
        # Get the wind model for the procedure
        windModel: "WindModel" = procedure.wind_model
        # Use the procedure model
        windModel.wind_model_source = WindAtmosphereModelSource.PROCEDURE_MODEL
        # Let's use constant wind
        windModel.wind_model_type = WindModelType.CONSTANT_WIND
        # Get the constant wind model options
        constantWind: "WindModelConstant" = windModel.mode_as_constant
        # Set the wind bearing
        constantWind.wind_bearing = 30
        # Set the wind speed
        constantWind.wind_speed = 5

        # Get the atmosphere model used for the procedure
        atmosphere: "AtmosphereModel" = procedure.atmosphere_model
        # Let's use the procedure model
        atmosphere.atmosphere_model_source = WindAtmosphereModelSource.PROCEDURE_MODEL
        # Get the basic atmosphere options
        basicAtmosphere: "AtmosphereModelBasic" = atmosphere.mode_as_basic
        # Use standard 1976 atmosphere
        basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976

    # endregion

    # region CreatePerformanceModel
    def test_CreatePerformanceModel(self):
        self.CreatePerformanceModel(AviatorCodeSnippets.AG_AvtrAircraft)

    def CreatePerformanceModel(self, aircraft: "AircraftModel"):
        # Get the acceleration type
        acceleration: "AircraftAcceleration" = aircraft.acceleration
        # Get it as a catalog item
        accAsCatalogItem: "ICatalogItem" = acceleration.get_as_catalog_item()
        # Get the names of the current acceleration models
        modelNames = accAsCatalogItem.child_names
        # Check how many models there are
        modelCount: int = Array.Length(modelNames)
        # Get the child types (for example AGI Basic Acceleration Model, Advanced Acceleration Model)
        modelTypes = accAsCatalogItem.child_types
        # Create a new performance model of type "Advanced Acceleration Model"
        newPerformanceModel: "ICatalogItem" = accAsCatalogItem.add_child_of_type(
            "Advanced Acceleration Model", "Model Name"
        )
        # Save the changes to the catalog
        aircraft.get_as_catalog_item().save()

    # endregion

    # region ConfigureBasicAccelerationPerfModel
    def test_ConfigureBasicAccelerationPerfModel(self):
        self.ConfigureBasicAccelerationPerfModel(AviatorCodeSnippets.AG_AvtrAircraft)

    def ConfigureBasicAccelerationPerfModel(self, aircraft: "AircraftModel"):
        # Get the acceleration type
        acceleration: "AircraftAcceleration" = aircraft.acceleration
        # Get the build in performance model
        basicAccModel: "AircraftBasicAccelerationModel" = acceleration.get_built_in_model()

        # Get the level turns options
        levelTurns: "LevelTurns" = basicAccModel.level_turns
        # Set a max bank angle of 25
        levelTurns.set_level_turn(TurnMode.TURN_MODE_BANK_ANGLE, 25)
        # Get the climb and descent transition options
        climbAndDescent: "ClimbAndDescentTransitions" = basicAccModel.climb_and_descent_transitions
        # Set the max pull up G to 1
        climbAndDescent.max_pull_up_g = 1.2
        # Get the attitude transition options
        attitudeTransitions: "AttitudeTransitions" = basicAccModel.attitude_transitions
        # Set the max roll rate to 25
        attitudeTransitions.roll_rate = 25

        # Get the aerodynamics
        aero: "AircraftAerodynamic" = basicAccModel.aerodynamics
        # Use simple aerodynamics
        aero.aerodynamic_strategy = AircraftAerodynamicStrategy.AIRCRAFT_AERODYNAMIC_SIMPLE
        # Get the options for the simple aerodynamics and set some parameters
        simpleAero: "AircraftSimpleAerodynamic" = aero.mode_as_simple
        simpleAero.s_reference = 5
        simpleAero.cl_max = 3.1
        simpleAero.cd = 0.05

        # Get the propulsion
        prop: "AircraftPropulsion" = basicAccModel.propulsion
        # Use simple propulsion
        prop.propulsion_strategy = AircraftPropulsionStrategy.AIRCRAFT_PROPULSION_SIMPLE
        # Get the simple propulsion options and set some parameters
        simpleProp: "AircraftSimplePropulsion" = prop.mode_as_simple
        simpleProp.max_thrust_acceleration = 0.6
        simpleProp.min_thrust_deceleration = 0.4
        simpleProp.set_density_scaling(True, 0.02)

        # Save the changes to the catalog
        aircraft.get_as_catalog_item().save()

    # endregion

    # region ConfigureBasicCruisePerfModel
    def test_ConfigureBasicCruisePerfModel(self):
        self.ConfigureBasicCruisePerfModel(AviatorCodeSnippets.AG_AvtrAircraft)

    def ConfigureBasicCruisePerfModel(self, aircraft: "AircraftModel"):
        # Get the cruise type
        cruise: "AircraftCruise" = aircraft.cruise
        # Get the build in performance model
        basicCruiseModel: "AircraftBasicCruiseModel" = cruise.get_built_in_model()

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
        aircraft.get_as_catalog_item().save()

    # endregion

    # region ConfigureProcedureTimeOptions
    def test_ConfigureProcedureTimeOptions(self):
        procedure: "IProcedure" = AviatorCodeSnippets.AG_Procedures.add(
            SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF
        )
        self.ConfigureProcedureTimeOptions(procedure)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)

    def ConfigureProcedureTimeOptions(self, procedure: "IProcedure"):
        # Get the time in epoch seconds
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        # Get the time options
        timeOptions: "ProcedureTimeOptions" = procedure.time_options
        # Get the start time
        startTime: typing.Any = timeOptions.start_time
        # Set the procedure to interrupt after 15 seconds
        timeOptions.set_interrupt_time(15)

    # endregion

    # region AddTakeoffProcedure
    def test_AddTakeoffProcedure(self):
        self.AddTakeoffProcedure(AviatorCodeSnippets.AG_Procedures)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)

    def AddTakeoffProcedure(self, procedures: "ProcedureCollection"):
        # Add a takeoff procedure with a runway as a site
        takeoff: "ProcedureTakeoff" = clr.CastAs(
            procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF), ProcedureTakeoff
        )

        # Get the runway heading options
        headingOptions: "RunwayHeadingOptions" = takeoff.runway_heading_options
        # Opt to use the headwind runway
        headingOptions.runway_mode = RunwayHighLowEnd.HEADWIND

        # Set the takeoff mode and get that interface
        takeoff.takeoff_mode = TakeoffMode.TAKEOFF_NORMAL
        takeoffNormal: "TakeoffNormal" = takeoff.mode_as_normal

        # Set the takeoff climb angle
        takeoffNormal.takeoff_climb_angle = 5
        # Set the departure altitude above the runway
        takeoffNormal.departure_altitude = 600
        # Set the altitude offset for the runway
        takeoffNormal.runway_altitude_offset = 10
        # Use terrain for the runway's altitude
        takeoffNormal.use_runway_terrain = True

    # endregion

    # region AddEnrouteProcedure
    def test_AddEnrouteProcedure(self):
        procedure: "IProcedure" = AviatorCodeSnippets.AG_Procedures.add(
            SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF
        )
        self.AddEnrouteProcedure(AviatorCodeSnippets.AG_Procedures)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)

    def AddEnrouteProcedure(self, procedures: "ProcedureCollection"):
        # Add an enroute procedure with a site type of End of Previous Procedure
        enroute: "ProcedureEnroute" = clr.CastAs(
            procedures.add(SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE), ProcedureEnroute
        )
        # Get the altitude options
        altitudeOptions: "AltitudeMSLAndLevelOffOptions" = enroute.altitude_msl_options
        # To specify an altitude, turn off the option to use the default cruise altitude
        altitudeOptions.use_default_cruise_altitude = False
        # Set the altitude
        altitudeOptions.msl_altitude = 10000

        # Get the navigation options
        navigationOptions: "NavigationOptions" = enroute.navigation_options
        # Set the route to arrive on a specified course
        navigationOptions.navigation_mode = PointToPointMode.ARRIVE_ON_COURSE
        # Set the course
        navigationOptions.arrive_on_course = 30
        # Use a magnetic heading
        navigationOptions.use_magnetic_heading = True

        # Get the navigation options
        airspeedOptions: "CruiseAirspeedOptions" = enroute.enroute_cruise_airspeed_options
        # Fly at max speed
        airspeedOptions.cruise_speed_type = CruiseSpeed.MAX_AIRSPEED
        # To specify an airspeed to fly at, set the speed type to other airspeed
        airspeedOptions.cruise_speed_type = CruiseSpeed.OTHER_AIRSPEED
        # Then set the airspeed and airspeed type
        airspeedOptions.set_other_airspeed(AirspeedType.TAS, 200)

    # endregion

    # region AddBasicManeuverProcedure
    def test_AddBasicManeuverProcedure(self):
        procedure: "IProcedure" = AviatorCodeSnippets.AG_Procedures.add(
            SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF
        )
        self.AddBasicManeuverProcedure(AviatorCodeSnippets.AG_Procedures)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)

    def AddBasicManeuverProcedure(self, procedures: "ProcedureCollection"):
        # Add a basic maneuver procedure
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            procedures.add(SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        # Set the navigation to use a Straight Ahead strategy
        basicManeuver.navigation_strategy_type = "Straight Ahead"
        # Get the options for the straight ahead strategy
        straightAhead: "BasicManeuverStrategyStraightAhead" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyStraightAhead
        )
        # Opt to maintain course (as opposed to maintain heading)
        straightAhead.reference_frame = StraightAheadReferenceFrame.MAINTAIN_COURSE

        # Set the profile to use a Autopilot - Vertical Plane strategy
        basicManeuver.profile_strategy_type = "Autopilot - Vertical Plane"
        # Get the options for the profile strategy
        autopilot: "BasicManeuverStrategyAutopilotProf" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyAutopilotProf
        )
        # Opt to maintain the initial altitude
        autopilot.altitude_mode = AutopilotAltitudeMode.AUTOPILOT_HOLD_INIT_ALTITUDE
        airspeedOptions: "BasicManeuverAirspeedOptions" = autopilot.airspeed_options
        # Opt to maintain a specified airspeed
        airspeedOptions.airspeed_mode = BasicManeuverAirspeedMode.MAINTAIN_SPECIFIED_AIRSPEED
        # Specify the airspeed
        airspeedOptions.specified_airspeed = 250

        # Configure the options on the Attitude / Performance / Fuel page
        basicManeuver.flight_mode = PhaseOfFlight.FLIGHT_PHASE_CRUISE
        # Override the fuel flow
        basicManeuver.fuel_flow_type = BasicManeuverFuelFlowType.BASIC_MANEUVER_FUEL_FLOW_OVERRIDE
        basicManeuver.override_fuel_flow_value = 1000

        # Set the basic stopping conditions
        basicManeuver.use_max_downrange = True
        basicManeuver.max_downrange = 10
        basicManeuver.use_stop_fuel_state = False
        basicManeuver.use_max_time_of_flight = False

    # endregion

    # region AddLandingProcedure
    def test_AddLandingProcedure(self):
        procedure: "IProcedure" = AviatorCodeSnippets.AG_Procedures.add(
            SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF
        )
        self.AddLandingProcedure(AviatorCodeSnippets.AG_Procedures)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)

    def AddLandingProcedure(self, procedures: "ProcedureCollection"):
        # Add a landing procedure
        landing: "ProcedureLanding" = clr.CastAs(
            procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_LANDING), ProcedureLanding
        )

        # Get the runway heading options
        headingOptions: "RunwayHeadingOptions" = landing.runway_heading_options
        # Land from the low end
        headingOptions.runway_mode = RunwayHighLowEnd.LOW_END

        # Use a standard instrument approach
        landing.approach_mode = ApproachMode.STANDARD_INSTRUMENT_APPROACH
        # Get the options for a standard instrument approach
        sia: "LandingStandardInstrumentApproach" = landing.mode_as_standard_instrument_approach
        # Change the approach altitude
        sia.approach_altitude = 1000
        # Change the glideslope
        sia.glideslope = 4
        # Offset the runway altitude
        sia.runway_altitude_offset = 10
        # Use the terrain as an altitude reference for the runway
        sia.use_runway_terrain = True

    # endregion

    # region ConfigureRunwaySite
    def test_ConfigureRunwaySite(self):
        userRunways: "ICatalogSource" = (
            AviatorCodeSnippets.AG_AvtrCatalog.runway_category.user_runways.get_as_catalog_source()
        )
        if userRunways.contains("New User Runway"):
            userRunways.remove_child("New User Runway")

        takeoff: "IProcedure" = AviatorCodeSnippets.AG_Procedures.add(
            SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF
        )
        self.ConfigureRunwaySite(clr.CastAs(takeoff.site, SiteRunway))
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)
        if userRunways.contains("New User Runway"):
            userRunways.remove_child("New User Runway")

    def ConfigureRunwaySite(self, runway: "SiteRunway"):
        # Set the latitude, longitude, and altitude
        runway.latitude = 41
        runway.longitude = 77
        runway.altitude = 5

        # Set the altitude reference
        runway.altitude_reference = AGLMSL.ALTITUDE_MSL

        # Set the heading
        runway.high_end_heading = 195
        # Opt to use true heading
        runway.is_magnetic = False

        # Set the length of the runway
        runway.length = 5

        # Rename the runway
        runway.get_as_site().name = "New User Runway"
        # Add the runway to the catalog to use it for next time
        runway.add_to_catalog(True)

    # endregion

    # region ConfigureRunwayFromCatalog
    def test_ConfigureRunwayFromCatalog(self):
        userRunways: "UserRunwaySource" = AviatorCodeSnippets.AG_AvtrCatalog.runway_category.user_runways
        if not (userRunways.get_as_catalog_source().contains("New User Runway")):
            userRunways.add_user_runway("New User Runway")

        takeoff: "IProcedure" = AviatorCodeSnippets.AG_Procedures.add(
            SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF
        )
        self.ConfigureRunwayFromCatalog(clr.CastAs(takeoff.site, SiteRunway), AviatorCodeSnippets.AG_AvtrCatalog)
        AviatorCodeSnippets.AG_Procedures.remove_at_index(0)
        if userRunways.get_as_catalog_source().contains("New User Runway"):
            userRunways.get_as_catalog_source().remove_child("New User Runway")

    def ConfigureRunwayFromCatalog(self, runway: "SiteRunway", catalog: "Catalog"):
        # Get the source of user runways
        userRunways: "UserRunwaySource" = catalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("New User Runway"):
            # If so, get the user runway with the given name
            runwayFromCatalog: "UserRunway" = userRunways.get_user_runway("New User Runway")
            # Copy the parameters of that runway
            runway.copy_from_catalog(clr.CastAs(runwayFromCatalog, ICatalogRunway))

    # endregion
