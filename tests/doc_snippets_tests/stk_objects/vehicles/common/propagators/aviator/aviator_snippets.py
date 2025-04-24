# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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

import os
import sys

from ansys.stk.core.stkobjects import STKObjectType, PropagatorType
from ansys.stk.core.stkobjects.aviator import (
    AdvancedFixedWingAerodynamicStrategy,
    AdvancedFixedWingPowerplantStrategy,
    AGLMSL,
    AircraftAerodynamicStrategy,
    AircraftPropulsionStrategy,
    AirspeedType,
    ApproachMode,
    AtmosphereModelType,
    AutopilotAltitudeMode,
    BasicManeuverAirspeedMode,
    BasicManeuverFuelFlowType,
    CruiseSpeed,
    PhaseOfFlight,
    PointToPointMode,
    ProcedureType,
    RunwayHighLowEnd,
    SiteType,
    StraightAheadReferenceFrame,
    TakeoffMode,
    TurnMode,
    WindAtmosphereModelSource,
    WindModelType,
)

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class AviatorSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_root(self):
        return CodeSnippetsTestBase.m_Root

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.CurrentScenario

    def get_aviator_aircraft(self):
        aircraft = self.get_root().current_scenario.children.new(STKObjectType.AIRCRAFT, "Boing737")
        aircraft.set_route_type(PropagatorType.AVIATOR)
        aircraftRoute = aircraft.route
        propagator = aircraftRoute.aviator_propagator
        mission = propagator.aviator_mission
        phases = mission.phases
        procedures = phases[0].procedures
        propagator.propagate()
        catalog = propagator.aviator_catalog
        aviatorAircraft = (
            catalog.aircraft_category.aircraft_models.get_aircraft("Basic Airliner").get_as_catalog_item().duplicate()
        )
        return aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft

    def test_AddAndRemoveProceduresSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.AddAndRemoveProceduresSnippet(propagator, procedures)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AddAndRemoveProcedures",
        description="Add and remove procedures",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~ProcedureCollection | stkobjects.aviator~Mission",
    )
    def AddAndRemoveProceduresSnippet(self, propagator, procedures):
        # IProcedureCollection procedures: Procedure Collection object
        # AviatorPropagator propagator: Aviator Propagator object
        # Add a takeoff procedure with a runway as a site. This will add the procedure
        takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
        # Add a procedure at a given index (starting from 0)
        enroute = procedures.add_at_index(1, SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE)

        # Make sure to propagate the mission to calculate the route
        propagator.propagate()
        # Get the mission
        mission = propagator.aviator_mission
        # Check to see if the mission is valid (must first be propagated)
        isValid = mission.is_valid

        # Get the number of procedures
        procedureCount = procedures.count
        # Remove the procedure at the given index
        procedures.remove_at_index(1)
        # Remove the given procedure
        procedures.remove(takeoff)

        # Propagate the mission
        propagator.propagate()

    def test_AddBasicManeuverProcedureSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
            self.AddBasicManeuverProcedureSnippet(procedures)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AddBasicManeuverProcedure",
        description="Add and configure a basic maneuver procedure",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~ProcedureCollection | stkobjects.aviator~ProcedureBasicManeuver | stkobjects.aviator~BasicManeuverStrategyStraightAhead | stkobjects.aviator~BasicManeuverStrategyAutopilotProf | stkobjects.aviator~BasicManeuverAirspeedOptions",
    )
    def AddBasicManeuverProcedureSnippet(self, procedures):
        # IProcedureCollection procedures: Procedure Collection object
        # Add a basic maneuver procedure
        basicManeuver = procedures.add(SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_BASIC_MANEUVER)

        # Set the navigation to use a Straight Ahead strategy
        basicManeuver.navigation_strategy_type = "Straight Ahead"
        # Get the options for the straight ahead strategy
        straightAhead = basicManeuver.navigation
        # Opt to maintain course (as opposed to maintain heading)
        straightAhead.reference_frame = StraightAheadReferenceFrame.MAINTAIN_COURSE

        # Set the profile to use a Autopilot - Vertical Plane strategy
        basicManeuver.profile_strategy_type = "Autopilot - Vertical Plane"
        # Get the options for the profile strategy
        autopilot = basicManeuver.profile
        # Opt to maintain the initial altitude
        autopilot.altitude_mode = AutopilotAltitudeMode.AUTOPILOT_HOLD_INIT_ALTITUDE
        airspeedOptions = autopilot.airspeed_options
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

    def test_AddEnrouteProcedureSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
            self.AddEnrouteProcedureSnippet(procedures)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AddEnrouteProcedure",
        description="Add and configure an en-route procedure",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~ProcedureCollection | stkobjects.aviator~ProcedureEnroute | stkobjects.aviator~AltitudeMSLAndLevelOffOptions | stkobjects.aviator~NavigationOptions | stkobjects.aviator~CruiseAirspeedOptions",
    )
    def AddEnrouteProcedureSnippet(self, procedures):
        # IProcedureCollection procedures: Procedure Collection object
        # Add an enroute procedure with a site type of End of Previous Procedure
        enroute = procedures.add_at_index(1, SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE)
        # Get the altitude options
        altitudeOptions = enroute.altitude_msl_options
        # To specify an altitude, turn off the option to use the default cruise altitude
        altitudeOptions.use_default_cruise_altitude = False
        # Set the altitude
        altitudeOptions.msl_altitude = 10000

        # Get the navigation options
        navigationOptions = enroute.navigation_options
        # Set the route to arrive on a specified course
        navigationOptions.navigation_mode = PointToPointMode.ARRIVE_ON_COURSE
        # Set the course
        navigationOptions.arrive_on_course = 30
        # Use a magnetic heading
        navigationOptions.use_magnetic_heading = True

        # Get the navigation options
        airspeedOptions = enroute.enroute_cruise_airspeed_options
        # Fly at max speed
        airspeedOptions.cruise_speed_type = CruiseSpeed.MAX_AIRSPEED
        # To specify an airspeed to fly at, set the speed type to other airspeed
        airspeedOptions.cruise_speed_type = CruiseSpeed.OTHER_AIRSPEED
        # Then set the airspeed and airspeed type
        airspeedOptions.set_other_airspeed(AirspeedType.TAS, 200)

    def test_AddLandingProcedureSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
            enroute = procedures.add(SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE)
            self.AddLandingProcedureSnippet(procedures)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AddLandingProcedure",
        description="Add and configure a landing procedure",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~ProcedureCollection | stkobjects.aviator~ProcedureLanding | stkobjects.aviator~RunwayHeadingOptions | stkobjects.aviator~LandingStandardInstrumentApproach",
    )
    def AddLandingProcedureSnippet(self, procedures):
        # IProcedureCollection procedures: Procedure Collection object
        # Add a landing procedure
        landing = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_LANDING)

        # Get the runway heading options
        headingOptions = landing.runway_heading_options
        # Land from the low end
        headingOptions.runway_mode = RunwayHighLowEnd.LOW_END

        # Use a standard instrument approach
        landing.approach_mode = ApproachMode.STANDARD_INSTRUMENT_APPROACH
        # Get the options for a standard instrument approach
        sia = landing.mode_as_standard_instrument_approach
        # Change the approach altitude
        sia.approach_altitude = 1000
        # Change the glideslope
        sia.glideslope = 4
        # Offset the runway altitude
        sia.runway_altitude_offset = 10
        # Use the terrain as an altitude reference for the runway
        sia.use_runway_terrain = True

    def test_AddPhaseSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.AddPhaseSnippet(phases)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AddPhase",
        description="Add a new phase and use the same performance models as the first phase",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~PhaseCollection | stkobjects.aviator~Phase",
    )
    def AddPhaseSnippet(self, phases):
        # PhaseCollection phases: Phase Collection object
        # Add a new phase at the end of the mission
        newPhase = phases.add()
        # Rename the phase
        newPhase.name = "New Phase"
        # Copy the performance models from the first phase and paste it to the new phase
        phases[0].copy_performance_models()
        newPhase.paste_performance_models()

    def test_AddTakeoffProcedureSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.AddTakeoffProcedureSnippet(procedures)
        finally:
            aircraft.unload()

    @code_snippet(
        name="AddTakeoffProcedure",
        description="Add a takeoff procedure from a runway",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~ProcedureCollection | stkobjects.aviator~ProcedureTakeoff | stkobjects.aviator~RunwayHeadingOptions | stkobjects.aviator~TakeoffNormal",
    )
    def AddTakeoffProcedureSnippet(self, procedures):
        # IProcedureCollection procedures: Procedure Collection object
        # Add a takeoff procedure with a runway as a site
        takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)

        # Get the runway heading options
        headingOptions = takeoff.runway_heading_options
        # Opt to use the headwind runway
        headingOptions.runway_mode = RunwayHighLowEnd.HEADWIND

        # Set the takeoff mode and get that interface
        takeoff.takeoff_mode = TakeoffMode.TAKEOFF_NORMAL
        takeoffNormal = takeoff.mode_as_normal

        # Set the takeoff climb angle
        takeoffNormal.takeoff_climb_angle = 5
        # Set the departure altitude above the runway
        takeoffNormal.departure_altitude = 600
        # Set the altitude offset for the runway
        takeoffNormal.runway_altitude_offset = 10
        # Use terrain for the runway's altitude
        takeoffNormal.use_runway_terrain = True

    def test_ConfigureAviatorPropagatorSnippet(self):
        try:
            root = self.get_root()
            aircraft = root.current_scenario.children.new(STKObjectType.AIRCRAFT, "Boing737")
            self.ConfigureAviatorPropagatorSnippet(aircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigureAviatorPropagator",
        description="Configure the Aviator propagator",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~AviatorPropagator",
    )
    def ConfigureAviatorPropagatorSnippet(self, aircraft):
        # Aircraft aircraft: Aircraft object
        # Set to Propagator to Aviator
        aircraft.set_route_type(PropagatorType.AVIATOR)
        # Get the aircraft's route
        aircraftRoute = aircraft.route
        # Get the Aviator propagator
        propagator = aircraftRoute.aviator_propagator
        # Get the Aviator mission
        mission = propagator.aviator_mission
        # Get the list of phases from the mission
        phases = mission.phases
        # Get the list of procedures from the first phase
        procedures = phases[0].procedures
        # Propagate the route
        propagator.propagate()

    def test_ConfigureBasicAccelerationPerfModelSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.ConfigureBasicAccelerationPerfModelSnippet(aviatorAircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigureBasicAccelerationPerfModel",
        description="Configure the basic acceleration performance model of an aircraft",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~AircraftModel | stkobjects.aviator~AircraftAcceleration | stkobjects.aviator~AircraftBasicAccelerationModel | stkobjects.aviator~LevelTurns | stkobjects.aviator~ClimbAndDescentTransitions | stkobjects.aviator~AttitudeTransitions | stkobjects.aviator~AircraftAerodynamic | stkobjects.aviator~AircraftSimpleAerodynamic | stkobjects.aviator~AircraftPropulsion | stkobjects.aviator~AircraftSimplePropulsion",
    )
    def ConfigureBasicAccelerationPerfModelSnippet(self, aviatorAircraft):
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

    def test_ConfigureBasicCruisePerfModelSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.ConfigureBasicCruisePerfModelSnippet(aviatorAircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigureBasicCruisePerfModel",
        description="Configure the basic cruise performance model of an aircraft",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~AircraftModel | stkobjects.aviator~AircraftCruise | stkobjects.aviator~AircraftBasicCruiseModel",
    )
    def ConfigureBasicCruisePerfModelSnippet(self, aviatorAircraft):
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

    def test_ConfigurePhasePerformanceModelsSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.ConfigurePhasePerformanceModelsSnippet(phases[0])
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigurePhasePerformanceModels",
        description="Configure the performance models to be used in the phase",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~Phase | stkobjects.aviator~PerformanceModelOptions",
    )
    def ConfigurePhasePerformanceModelsSnippet(self, phase):
        # Phase phase: Phase object
        # Get the acceleration performance model used for the current phase
        acceleration = phase.get_performance_model_by_type("Acceleration")
        # Check if it is linked to the catalog
        isLinkedToCatalog = acceleration.is_linked_to_catalog
        # Use the performance model in the catalog named "Built-In Model"
        acceleration.link_to_catalog("Built-In Model")

        # Get the VTOL performance model
        vtol = phase.get_performance_model_by_type("VTOL")
        # Create a new vtol model of type AGI VTOL Model. Note that this new model does not exist in the catalog and only exists in the phase.
        vtol.create_new("AGI VTOL Model")
        # Rename the performance model
        vtol.rename("Temporary VTOL Model")

    def test_ConfigureProcedureSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            procedure = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
            self.ConfigureProcedureSnippet(procedure)
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigureProcedure",
        description="Rename a procedure and its site",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~IProcedure | stkobjects.aviator~ISite",
    )
    def ConfigureProcedureSnippet(self, procedure):
        # IProcedure procedure: Procedure object
        # Rename the procedure
        procedure.name = "New Procedure"
        # Get the site corresponding to the procedure
        site = procedure.site
        # Rename the site
        site.name = "New Site"

    def test_ConfigureProcedureTimeOptionsSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            procedure = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
            self.ConfigureProcedureTimeOptionsSnippet(self.get_root(), procedure)
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigureProcedureTimeOptions",
        description="Configure a procedure time options",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~IProcedure | stkobjects.aviator~ProcedureTimeOptions",
    )
    def ConfigureProcedureTimeOptionsSnippet(self, root, procedure):
        # IProcedure procedure: Procedure object
        # Get the time in epoch seconds
        root.units_preferences.set_current_unit("DateFormat", "EpSec")
        # Get the time options
        timeOptions = procedure.time_options
        # Get the start time
        startTime = timeOptions.start_time
        # Set the procedure to interrupt after 15 seconds
        timeOptions.set_interrupt_time(15)

    def test_ConfigureProcedureWindAtmosSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            procedure = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
            self.ConfigureProcedureWindAtmosSnippet(procedure)
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigureProcedureWindAtmos",
        description="Configure the wind and atmosphere for a procedure",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~IProcedure | stkobjects.aviator~WindModel | stkobjects.aviator~WindModelConstant | stkobjects.aviator~AtmosphereModel | stkobjects.aviator~AtmosphereModelBasic",
    )
    def ConfigureProcedureWindAtmosSnippet(self, procedure):
        # IProcedure procedure: Procedure object
        # Get the wind model for the procedure
        windModel = procedure.wind_model
        # Use the procedure model
        windModel.wind_model_source = WindAtmosphereModelSource.PROCEDURE_MODEL
        # Let's use constant wind
        windModel.wind_model_type = WindModelType.CONSTANT_WIND
        # Get the constant wind model options
        constantWind = windModel.mode_as_constant
        # Set the wind bearing
        constantWind.wind_bearing = 30
        # Set the wind speed
        constantWind.wind_speed = 5

        # Get the atmosphere model used for the procedure
        atmosphere = procedure.atmosphere_model
        # Let's use the procedure model
        atmosphere.atmosphere_model_source = WindAtmosphereModelSource.PROCEDURE_MODEL
        # Get the basic atmosphere options
        basicAtmosphere = atmosphere.mode_as_basic
        # Use standard 1976 atmosphere
        basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976

    def test_ConfigureRunwayFromCatalogSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
            self.ConfigureRunwayFromCatalogSnippet(catalog, takeoff.site)
        finally:
            if catalog.runway_category.user_runways.get_as_catalog_source().contains("New User Runway"):
                catalog.runway_category.user_runways.get_as_catalog_source().remove_child("New User Runway")
            aircraft.unload()

    @code_snippet(
        name="ConfigureRunwayFromCatalog",
        description="Configure a runway site from a runway in the Aviator catalog",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~SiteRunway | stkobjects.aviator~Catalog | stkobjects.aviator~UserRunwaySource",
    )
    def ConfigureRunwayFromCatalogSnippet(self, catalog, runway):
        # SiteRunway runway: Runway object
        # Catalog catalog: Aviator catalog object
        # Get the source of user runways
        userRunways = catalog.runway_category.user_runways
        # Check that the runway exists in the catalog
        if userRunways.contains("New User Runway") is True:
            # If so, get the user runway with the given name
            runwayFromCatalog = userRunways.get_user_runway("New User Runway")
            # Copy the parameters of that runway
            runway.copy_from_catalog(runwayFromCatalog)

    def test_ConfigureRunwaySiteSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
            self.ConfigureRunwaySiteSnippet(takeoff.site)
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigureRunwaySite",
        description="Configure a runway site",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~SiteRunway",
    )
    def ConfigureRunwaySiteSnippet(self, runway):
        # SiteRunway runway: Runway object
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
        runway.name = "New User Runway"
        # Add the runway to the catalog to use it for next time
        runway.add_to_catalog(1)

    def test_ConfigureWeatherAtmosphereSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.ConfigureWeatherAtmosphereSnippet(mission)
        finally:
            aircraft.unload()

    @code_snippet(
        name="ConfigureWeatherAtmosphere",
        description="Configure the weather and atmosphere of the Mission",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~Mission | stkobjects.aviator~WindModel | stkobjects.aviator~WindModelConstant | stkobjects.aviator~AtmosphereModel | stkobjects.aviator~AtmosphereModelBasic",
    )
    def ConfigureWeatherAtmosphereSnippet(self, mission):
        # Mission mission: Aviator Mission object
        # Get the wind model used for the mission
        windModel = mission.wind_model
        # Let's use the mission model
        windModel.wind_model_source = WindAtmosphereModelSource.MISSION_MODEL
        # Let's use constant wind
        windModel.wind_model_type = WindModelType.CONSTANT_WIND
        # Get the constant wind model options
        constantWind = windModel.mode_as_constant
        # Set the wind bearing
        constantWind.wind_bearing = 30
        # Set the wind speed
        constantWind.wind_speed = 5

        # Get the atmosphere model used for the mission
        atmosphere = mission.atmosphere_model
        # Let's use the mission model
        atmosphere.atmosphere_model_source = WindAtmosphereModelSource.MISSION_MODEL
        # Get the basic atmosphere options
        basicAtmosphere = atmosphere.mode_as_basic
        # Use standard 1976 atmosphere
        basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976
        # Opt to override the values
        basicAtmosphere.use_non_standard_atmosphere = True
        # Override the temperature
        basicAtmosphere.temperature = 290

    def test_CreatePerformanceModelSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.CreatePerformanceModelSnippet(aviatorAircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="CreatePerformanceModel",
        description="Create a new performance model for an aircraft",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~AircraftModel | stkobjects.aviator~AircraftAcceleration | stkobjects.aviator~ICatalogItem | stkobjects.aviator~IPerformanceModel",
    )
    def CreatePerformanceModelSnippet(self, aviatorAircraft):
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

    def test_SetAviatorVehicleSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.SetAviatorVehicleSnippet(propagator)
        finally:
            aircraft.unload()

    @code_snippet(
        name="SetAviatorVehicle",
        description="Set the aircraft used for the mission to an aircraft found in the Aviator catalog",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~Mission | stkobjects.aviator~Catalog | stkobjects.aviator~AircraftCategory | stkobjects.aviator~AircraftModels | stkobjects.aviator~AircraftModel",
    )
    def SetAviatorVehicleSnippet(self, propagator):
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

    def test_SetTheConfigurationSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.SetTheConfigurationSnippet(mission)
        finally:
            aircraft.unload()

    @code_snippet(
        name="SetTheConfiguration",
        description="Set the Configuration used for the Mission",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~Mission | stkobjects.aviator~Configuration | stkobjects.aviator~StationCollection | stkobjects.aviator~PayloadStation | stkobjects.aviator~FuelTankExternal",
    )
    def SetTheConfigurationSnippet(self, mission):
        # Mission mission: Aviator Mission object
        # Get the configuration used for the mission
        configuration = mission.configuration
        # Set the max landing weight
        configuration.max_landing_weight = 300000
        # Set the empty weight
        configuration.empty_weight = 210000
        # Update the center of gravity of the aircraft when empty
        configuration.set_empty_cg(2, 0, 1)

        # Get the stations
        stations = configuration.get_stations()
        # Check if there is an internal fuel station
        if stations.contains_station("Internal Fuel") is True:
            # Get the fuel tank
            fuelTank = stations.get_internal_fuel_tank_by_name("Internal Fuel")
            # Set the capacity of the fuel tank
            fuelTank.capacity = 175000
            # Set the initial state of the fuel tank
            fuelTank.initial_fuel_state = 125000

        # Add a new payload station
        newPayload = stations.add_payload_station()
        # Set the position of the payload station
        newPayload.set_position(0, 2, 0)
        # Add an external fuel tank
        externalTank = newPayload.add_external_fuel_tank()
        # Set the empty weight of the tank
        externalTank.empty_weight = 2000

    def test_SetupAdvancedFixedWingToolSnippet(self):
        try:
            aircraft, propagator, mission, phases, procedures, catalog, aviatorAircraft = self.get_aviator_aircraft()
            self.SetupAdvancedFixedWingToolSnippet(aviatorAircraft)
        finally:
            aircraft.unload()

    @code_snippet(
        name="SetupAdvancedFixedWingTool",
        description="Configure the Advanced Fixed Wing Tool and set the aircraft to use the resulting performance models",
        category="STK Objects | Vehicles | Common | Propagators | Aviator",
        eid="stkobjects.aviator~AircraftModel | stkobjects.aviator~AdvancedFixedWingTool",
    )
    def SetupAdvancedFixedWingToolSnippet(self, aviatorAircraft):
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
