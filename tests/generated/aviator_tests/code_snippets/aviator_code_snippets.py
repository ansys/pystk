import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.aviator import *


class AviatorCodeSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(AviatorCodeSnippets, self).__init__(*args, **kwargs)

    # region Static DataMembers
    AG_Scenario = None
    AG_AC = None
    AG_AvtrProp = None
    AG_AvtrCatalog = None
    AG_AvtrAircraftModels = None
    AG_Mission = None
    AG_Phases = None
    AG_Procedures = None
    AG_AvtrAircraft = None
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
        scenario = clr.CastAs(TestBase.Application.CurrentScenario, IStkObject)
        AviatorCodeSnippets.AG_Scenario = scenario
        AviatorCodeSnippets.AG_AC = clr.Convert(
            (scenario.Children.New(AgESTKObjectType.eAircraft, "AviatorAC")), IAircraft
        )
        # Set to Propagator to Aviator
        AviatorCodeSnippets.AG_AC.SetRouteType(AgEVePropagatorType.ePropagatorAviator)
        # Get the aircrafts route (still on the STKObjects side)
        aircraftRoute = clr.CastAs(AviatorCodeSnippets.AG_AC.Route, IVehiclePropagatorAviator)
        # Get the Aviator propagator
        AviatorCodeSnippets.AG_AvtrProp = clr.CastAs(aircraftRoute.AvtrPropagator, IAviatorPropagator)
        # Get the Aviator mission
        AviatorCodeSnippets.AG_Mission = AviatorCodeSnippets.AG_AvtrProp.AvtrMission
        # Get the phases
        AviatorCodeSnippets.AG_Phases = AviatorCodeSnippets.AG_Mission.Phases
        # Get the procedures
        AviatorCodeSnippets.AG_Procedures = AviatorCodeSnippets.AG_Phases[0].Procedures
        # Get the Aviator Catalog
        AviatorCodeSnippets.AG_AvtrCatalog = AviatorCodeSnippets.AG_AvtrProp.AvtrCatalog
        # Get the User Aircraft Models
        AviatorCodeSnippets.AG_AvtrAircraftModels = AviatorCodeSnippets.AG_AvtrCatalog.AircraftCategory.AircraftModels
        # Duplicate the basic airliner
        AviatorCodeSnippets.AG_AvtrAircraft = clr.CastAs(
            AviatorCodeSnippets.AG_AvtrAircraftModels.GetAircraft("Basic Airliner").GetAsCatalogItem().Duplicate(),
            IAircraftModel,
        )
        # Use the aircraft in the misison
        AviatorCodeSnippets.AG_Mission.Vehicle = clr.CastAs(AviatorCodeSnippets.AG_AvtrAircraft, IAviatorVehicle)

    # endregion

    # region TestTearDown
    def tearDown(self):
        (clr.Convert(AviatorCodeSnippets.AG_AC, IStkObject)).Unload()
        AviatorCodeSnippets.AG_AC = None
        AviatorCodeSnippets.AG_AvtrAircraft.GetAsCatalogItem().Remove()

    # endregion

    # region ConfigureAviatorPropagator
    def test_ConfigureAviatorPropagator(self):
        self.ConfigureAviatorPropagator(AviatorCodeSnippets.AG_AC)

    def ConfigureAviatorPropagator(self, aircraft):
        # Set to Propagator to Aviator
        aircraft.SetRouteType(AgEVePropagatorType.ePropagatorAviator)
        # Get the aircraft's route
        aircraftRoute = clr.CastAs(aircraft.Route, IVehiclePropagatorAviator)
        # Get the Aviator propagator
        propagator = clr.CastAs(aircraftRoute.AvtrPropagator, IAviatorPropagator)
        # Get the Aviator mission
        mission = propagator.AvtrMission
        # Get the list of phases from the mission
        phases = mission.Phases
        # Get the list of procedures from the first phase
        procedures = phases[0].Procedures
        # Propagate the route
        propagator.Propagate()

    # endregion

    # region SetTheConfiguration
    def test_SetTheConfiguration(self):
        self.SetTheConfiguration(AviatorCodeSnippets.AG_Mission)

    def SetTheConfiguration(self, mission):
        # Get the configuration used for the mission
        configuration = mission.Configuration
        # Set the max landing weight
        configuration.MaxLandingWeight = 300000
        # Set the empty weight
        configuration.EmptyWeight = 210000
        # Update the center of gravity of the aircraft when empty
        configuration.SetEmptyCG(2, 0, 1)

        # Get the stations
        stations = configuration.GetStations()
        # Check if there is an internal fuel station
        hasInternalFuel = stations.ContainsStation("Internal Fuel")
        if hasInternalFuel:
            # Get the fuel tank
            fuelTank = stations.GetInternalFuelTankByName("Internal Fuel")
            # Set the capacity of the fuel tank
            fuelTank.Capacity = 175000
            # Set the initial state of the fuel tank
            fuelTank.InitialFuelState = 125000

        # Add a new payload station
        newPayload = stations.AddPayloadStation()
        # Set the position of the payload station
        newPayload.SetPosition(0, 2, 0)
        # Add an external fuel tank
        externalTank = newPayload.AddExternalFuelTank()
        # Set the empty weight of the tank
        externalTank.EmptyWeight = 2000

    # endregion

    # region ConfigureWeatherAtmosphere
    def test_ConfigureWeatherAtmosphere(self):
        self.ConfigureWeatherAtmosphere(AviatorCodeSnippets.AG_Mission)

    def ConfigureWeatherAtmosphere(self, mission):
        # Get the wind model used for the mission
        windModel = mission.WindModel
        # Let's use the mission model
        windModel.WindModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        # Let's use constant wind
        windModel.WindModelType = AgEAvtrWindModelType.eConstantWind
        # Get the constant wind model options
        constantWind = windModel.ModeAsConstant
        # Set the wind bearing
        constantWind.WindBearing = 30
        # Set the wind speed
        constantWind.WindSpeed = 5

        # Get the atmosphere model used for the mission
        atmosphere = mission.AtmosphereModel
        # Let's use the mission model
        atmosphere.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        # Get the basic atmosphere options
        basicAtmosphere = atmosphere.ModeAsBasic
        # Use standard 1976 atmosphere
        basicAtmosphere.BasicModelType = AgEAvtrAtmosphereModel.eStandard1976
        # Opt to override the values
        basicAtmosphere.UseNonStandardAtmosphere = True
        # Override the temperature
        basicAtmosphere.Temperature = 290

    # endregion

    # region SetAviatorVehicle
    def test_SetAviatorVehicle(self):
        self.SetAviatorVehicle(AviatorCodeSnippets.AG_AvtrProp)
        AviatorCodeSnippets.AG_Mission.Vehicle = clr.CastAs(AviatorCodeSnippets.AG_AvtrAircraft, IAviatorVehicle)

    def SetAviatorVehicle(self, propagator):
        # Get the Aviator catalog
        catalog = propagator.AvtrCatalog
        # Get the aircraft category
        category = catalog.AircraftCategory
        # Get the user aircraft models
        aircraftModels = category.AircraftModels
        # Get the basic fighter
        fighter = aircraftModels.GetAircraft("Basic Fighter")
        # Get the mission
        mission = propagator.AvtrMission
        # Set the vehicle used for the mission
        mission.Vehicle = clr.CastAs(fighter, IAviatorVehicle)

    # endregion

    # region SetupAdvancedFixedWingTool
    def test_SetupAdvancedFixedWingTool(self):
        self.SetupAdvancedFixedWingTool(AviatorCodeSnippets.AG_AvtrAircraft)

    def SetupAdvancedFixedWingTool(self, aviatorAircraft):
        # Get the advanced fixed wing tool
        advFixedWingTool = aviatorAircraft.AdvFixedWingTool
        # Set the basic geometry
        advFixedWingTool.WingArea = 300
        advFixedWingTool.FlapsArea = 50
        advFixedWingTool.SpeedbrakesArea = 10
        # Set the structural and human factor limits
        advFixedWingTool.MaxAltitude = 65000
        advFixedWingTool.MaxMach = 0.98
        advFixedWingTool.MaxEAS = 460
        advFixedWingTool.MinLoadFactor = -2.5
        advFixedWingTool.MaxLoadFactor = 4.5

        # Opt to enforce the max temperature limit
        advFixedWingTool.UseMaxTemperatureLimit = True
        advFixedWingTool.MaxTemperature = 900

        # Use a subsonic aerodynamic strategy
        advFixedWingTool.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero
        # Cache the aerodynamic data to improve calculation speed
        advFixedWingTool.CacheAeroData = True
        # Use a high bypass turbofan
        advFixedWingTool.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanHighBypass
        # Cache the fuel flow data to improve calculation speed
        advFixedWingTool.CacheFuelFlow = True

        # Create the corresponding performance models that reference the advanced fixed wing tool
        # Specify the name, whether to override any existing models with the same name, and whether to set the new models as the default performance models
        advFixedWingTool.CreateAllPerfModels("AdvancedModels", True, True)

        # Save the changes in the catalog
        aviatorAircraft.GetAsCatalogItem().Save()

    # endregion

    # region ConfigurePhasePerformanceModels
    def test_ConfigurePhasePerformanceModels(self):
        self.ConfigurePhasePerformanceModels(AviatorCodeSnippets.AG_Phases[0])

    def ConfigurePhasePerformanceModels(self, phase):
        # Get the acceleration performance model used for the current phase
        acceleration = phase.GetPerformanceModelByType("Acceleration")
        # Check if it is linked to the catalog
        isLinkedToCatalog = acceleration.IsLinkedToCatalog
        # Use the performance model in the catalog named "Built-In Model"
        acceleration.LinkToCatalog("Built-In Model")

        # Get the VTOL performance model
        vtol = phase.GetPerformanceModelByType("VTOL")
        # Create a new vtol model of type AGI VTOL Model. Note that this new model does not exist in the catalog and only exists in the phase.
        vtol.CreateNew("AGI VTOL Model")
        # Rename the performance model
        vtol.Rename("Temporary VTOL Model")

    # endregion

    # region AddPhase
    def test_AddPhase(self):
        self.AddPhase(AviatorCodeSnippets.AG_Phases)

    def AddPhase(self, phases):
        # Add a new phase at the end of the mission
        newPhase = phases.Add()
        # Rename the phase
        newPhase.Name = "New Phase"
        # Copy the performance models from the first phase and paste it to the new phase
        phases[0].CopyPerformanceModels()
        newPhase.PastePerformanceModels()

    # endregion

    # region AddAndRemoveProcedures
    def test_AddAndRemoveProcedures(self):
        self.AddAndRemoveProcedures(AviatorCodeSnippets.AG_Procedures, AviatorCodeSnippets.AG_AvtrProp)

    def AddAndRemoveProcedures(self, procedures, propagator):
        # Add a takeoff procedure with a runway as a site. This will add the procedure
        takeoff = procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        # Add a procedure at a given index (starting from 0)
        enroute = procedures.AddAtIndex(1, AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute)

        # Make sure to propagate the mission to calculate the route
        propagator.Propagate()
        # Get the mission
        mission = propagator.AvtrMission
        # Check to see if the mission is valid (must first be propagated)
        isValid = mission.IsValid

        # Get the number of procedures
        procedureCount = procedures.Count
        # Remove the procedure at the given index
        procedures.RemoveAtIndex(1)
        # Remove the given procedure
        procedures.Remove(takeoff)

        # Propagate the mission
        propagator.Propagate()

    # endregion

    # region ConfigureProcedure
    def test_ConfigureProcedure(self):
        procedure = AviatorCodeSnippets.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        self.ConfigureProcedure(procedure)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)

    def ConfigureProcedure(self, procedure):
        # Rename the procedure
        procedure.Name = "New Procedure"
        # Get the site corresponding to the procedure
        site = procedure.Site
        # Rename the site
        site.Name = "New Site"

    # endregion

    # region ConfigureProcedureWindAtmos
    def test_ConfigureProcedureWindAtmos(self):
        procedure = AviatorCodeSnippets.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        self.ConfigureProcedureWindAtmos(procedure)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)

    def ConfigureProcedureWindAtmos(self, procedure):
        # Get the wind model for the procedure
        windModel = procedure.WindModel
        # Use the procedure model
        windModel.WindModelSource = AgEAvtrWindAtmosModelSource.eProcedureModel
        # Let's use constant wind
        windModel.WindModelType = AgEAvtrWindModelType.eConstantWind
        # Get the constant wind model options
        constantWind = windModel.ModeAsConstant
        # Set the wind bearing
        constantWind.WindBearing = 30
        # Set the wind speed
        constantWind.WindSpeed = 5

        # Get the atmosphere model used for the procedure
        atmosphere = procedure.AtmosphereModel
        # Let's use the procedure model
        atmosphere.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eProcedureModel
        # Get the basic atmosphere options
        basicAtmosphere = atmosphere.ModeAsBasic
        # Use standard 1976 atmosphere
        basicAtmosphere.BasicModelType = AgEAvtrAtmosphereModel.eStandard1976

    # endregion

    # region CreatePerformanceModel
    def test_CreatePerformanceModel(self):
        self.CreatePerformanceModel(AviatorCodeSnippets.AG_AvtrAircraft)

    def CreatePerformanceModel(self, aircraft):
        # Get the acceleration type
        acceleration = aircraft.Acceleration
        # Get it as a catalog item
        accAsCatalogItem = acceleration.GetAsCatalogItem()
        # Get the names of the current acceleration models
        modelNames = accAsCatalogItem.ChildNames
        # Check how many models there are
        modelCount = Array.Length(modelNames)
        # Get the child types (for example AGI Basic Acceleration Model, Advanced Acceleration Model)
        modelTypes = accAsCatalogItem.ChildTypes
        # Create a new performance model of type "Advanced Acceleration Model"
        newPerformanceModel = accAsCatalogItem.AddChildOfType("Advanced Acceleration Model", "Model Name")
        # Save the changes to the catalog
        aircraft.GetAsCatalogItem().Save()

    # endregion

    # region ConfigureBasicAccelerationPerfModel
    def test_ConfigureBasicAccelerationPerfModel(self):
        self.ConfigureBasicAccelerationPerfModel(AviatorCodeSnippets.AG_AvtrAircraft)

    def ConfigureBasicAccelerationPerfModel(self, aircraft):
        # Get the acceleration type
        acceleration = aircraft.Acceleration
        # Get the build in performance model
        basicAccModel = acceleration.GetBuiltInModel()

        # Get the level turns options
        levelTurns = basicAccModel.LevelTurns
        # Set a max bank angle of 25
        levelTurns.SetLevelTurn(AgEAvtrTurnMode.eTurnModeBankAngle, 25)
        # Get the climb and descent transition options
        climbAndDescent = basicAccModel.ClimbAndDescentTransitions
        # Set the max pull up G to 1
        climbAndDescent.MaxPullUpG = 1.2
        # Get the attitude transition options
        attitudeTransitions = basicAccModel.AttitudeTransitions
        # Set the max roll rate to 25
        attitudeTransitions.RollRate = 25

        # Get the aerodynamics
        aero = basicAccModel.Aerodynamics
        # Use simple aerodynamics
        aero.AeroStrategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroSimple
        # Get the options for the simple aerodynamics and set some parameters
        simpleAero = aero.ModeAsSimple
        simpleAero.SRef = 5
        simpleAero.ClMax = 3.1
        simpleAero.Cd = 0.05

        # Get the propulsion
        prop = basicAccModel.Propulsion
        # Use simple propulsion
        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropSimple
        # Get the simple propulsion options and set some parameters
        simpleProp = prop.ModeAsSimple
        simpleProp.MaxThrustAccel = 0.6
        simpleProp.MinThrustDecel = 0.4
        simpleProp.SetDensityScaling(True, 0.02)

        # Save the changes to the catalog
        aircraft.GetAsCatalogItem().Save()

    # endregion

    # region ConfigureBasicCruisePerfModel
    def test_ConfigureBasicCruisePerfModel(self):
        self.ConfigureBasicCruisePerfModel(AviatorCodeSnippets.AG_AvtrAircraft)

    def ConfigureBasicCruisePerfModel(self, aircraft):
        # Get the cruise type
        cruise = aircraft.Cruise
        # Get the build in performance model
        basicCruiseModel = cruise.GetBuiltInModel()

        # Set the ceiling altitude
        basicCruiseModel.CeilingAltitude = 50000
        # Set the default cruise altitude
        basicCruiseModel.DefaultCruiseAltitude = 10000
        # Set the airspeed type
        basicCruiseModel.AirspeedType = AgEAvtrAirspeedType.eTAS
        # Opt to not use the fuel flow calculated by the aero/prop model and instead specify the values
        basicCruiseModel.UseAeroPropFuel = False

        # Set the various airspeeds and fuel flows
        basicCruiseModel.MinAirspeed = 110
        basicCruiseModel.MinAirspeedFuelFlow = 10000

        basicCruiseModel.MaxEnduranceAirspeed = 135
        basicCruiseModel.MaxEnduranceFuelFlow = 8000

        basicCruiseModel.MaxAirspeed = 570
        basicCruiseModel.MaxAirspeedFuelFlow = 30000

        basicCruiseModel.MaxRangeAirspeed = 140
        basicCruiseModel.MaxRangeFuelFlow = 9000

        basicCruiseModel.MaxPerfAirspeed = 150
        basicCruiseModel.MaxPerfAirspeedFuelFlow = 12000

        # Save the changes to the catalog
        aircraft.GetAsCatalogItem().Save()

    # endregion

    # region ConfigureProcedureTimeOptions
    def test_ConfigureProcedureTimeOptions(self):
        procedure = AviatorCodeSnippets.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        self.ConfigureProcedureTimeOptions(procedure)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)

    def ConfigureProcedureTimeOptions(self, procedure):
        # Get the time in epoch seconds
        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        # Get the time options
        timeOptions = procedure.TimeOptions
        # Get the start time
        startTime = timeOptions.StartTime
        # Set the procedure to interrupt after 15 seconds
        timeOptions.SetInterruptTime(15)

    # endregion

    # region AddTakeoffProcedure
    def test_AddTakeoffProcedure(self):
        self.AddTakeoffProcedure(AviatorCodeSnippets.AG_Procedures)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)

    def AddTakeoffProcedure(self, procedures):
        # Add a takeoff procedure with a runway as a site
        takeoff = clr.CastAs(
            procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff), IProcedureTakeoff
        )

        # Get the runway heading options
        headingOptions = takeoff.RunwayHeadingOptions
        # Opt to use the headwind runway
        headingOptions.RunwayMode = AgEAvtrRunwayHighLowEnd.eHeadwind

        # Set the takeoff mode and get that interface
        takeoff.TakeoffMode = AgEAvtrTakeoffMode.eTakeoffNormal
        takeoffNormal = takeoff.ModeAsNormal

        # Set the takeoff climb angle
        takeoffNormal.TakeoffClimbAngle = 5
        # Set the departure altitude above the runway
        takeoffNormal.DepartureAltitude = 600
        # Set the altitude offset for the runway
        takeoffNormal.RunwayAltitudeOffset = 10
        # Use terrain for the runway's altitude
        takeoffNormal.UseRunwayTerrain = True

    # endregion

    # region AddEnrouteProcedure
    def test_AddEnrouteProcedure(self):
        procedure = AviatorCodeSnippets.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        self.AddEnrouteProcedure(AviatorCodeSnippets.AG_Procedures)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)

    def AddEnrouteProcedure(self, procedures):
        # Add an enroute procedure with a site type of End of Previous Procedure
        enroute = clr.CastAs(
            procedures.Add(AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute),
            IProcedureEnroute,
        )
        # Get the altitude options
        altitudeOptions = enroute.AltitudeMSLOptions
        # To specify an altitude, turn off the option to use the default cruise altitude
        altitudeOptions.UseDefaultCruiseAltitude = False
        # Set the altitude
        altitudeOptions.MSLAltitude = 10000

        # Get the navigation options
        navigationOptions = enroute.NavigationOptions
        # Set the route to arrive on a specified course
        navigationOptions.NavMode = AgEAvtrPointToPointMode.eArriveOnCourse
        # Set the course
        navigationOptions.ArriveOnCourse = 30
        # Use a magnetic heading
        navigationOptions.UseMagneticHeading = True

        # Get the navigation options
        airspeedOptions = enroute.EnrouteCruiseAirspeedOptions
        # Fly at max speed
        airspeedOptions.CruiseSpeedType = AgEAvtrCruiseSpeed.eMaxAirspeed
        # To specify an airspeed to fly at, set the speed type to other airspeed
        airspeedOptions.CruiseSpeedType = AgEAvtrCruiseSpeed.eOtherAirspeed
        # Then set the airspeed and airspeed type
        airspeedOptions.SetOtherAirspeed(AgEAvtrAirspeedType.eTAS, 200)

    # endregion

    # region AddBasicManeuverProcedure
    def test_AddBasicManeuverProcedure(self):
        procedure = AviatorCodeSnippets.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        self.AddBasicManeuverProcedure(AviatorCodeSnippets.AG_Procedures)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)

    def AddBasicManeuverProcedure(self, procedures):
        # Add a basic maneuver procedure
        basicManeuver = clr.CastAs(
            procedures.Add(AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver),
            IProcedureBasicManeuver,
        )

        # Set the navigation to use a Straight Ahead strategy
        basicManeuver.NavigationStrategyType = "Straight Ahead"
        # Get the options for the straight ahead strategy
        straightAhead = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyStraightAhead)
        # Opt to maintain course (as opposed to maintain heading)
        straightAhead.ReferenceFrame = AgEAvtrStraightAheadRefFrame.eMaintainCourse

        # Set the profile to use a Autopilot - Vertical Plane strategy
        basicManeuver.ProfileStrategyType = "Autopilot - Vertical Plane"
        # Get the options for the profile strategy
        autopilot = clr.CastAs(basicManeuver.Profile, IBasicManeuverStrategyAutopilotProf)
        # Opt to maintain the initial altitude
        autopilot.AltitudeMode = AgEAvtrAutopilotAltitudeMode.eAutopilotHoldInitAltitude
        airspeedOptions = autopilot.AirspeedOptions
        # Opt to maintain a specified airspeed
        airspeedOptions.AirspeedMode = AgEAvtrBasicManeuverAirspeedMode.eMaintainSpecifiedAirspeed
        # Specify the airspeed
        airspeedOptions.SpecifiedAirspeed = 250

        # Configure the options on the Attitude / Performance / Fuel page
        basicManeuver.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseCruise
        # Override the fuel flow
        basicManeuver.FuelFlowType = AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowOverride
        basicManeuver.OverrideFuelFlowValue = 1000

        # Set the basic stopping conditions
        basicManeuver.UseMaxDownrange = True
        basicManeuver.MaxDownrange = 10
        basicManeuver.UseStopFuelState = False
        basicManeuver.UseMaxTimeOfFlight = False

    # endregion

    # region AddLandingProcedure
    def test_AddLandingProcedure(self):
        procedure = AviatorCodeSnippets.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        self.AddLandingProcedure(AviatorCodeSnippets.AG_Procedures)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)

    def AddLandingProcedure(self, procedures):
        # Add a landing procedure
        landing = clr.CastAs(
            procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcLanding), IProcedureLanding
        )

        # Get the runway heading options
        headingOptions = landing.RunwayHeadingOptions
        # Land from the low end
        headingOptions.RunwayMode = AgEAvtrRunwayHighLowEnd.eLowEnd

        # Use a standard instrument approach
        landing.ApproachMode = AgEAvtrApproachMode.eStandardInstrumentApproach
        # Get the options for a standard instrument approach
        sia = landing.ModeAsStandardInstrumentApproach
        # Change the approach altitude
        sia.ApproachAltitude = 1000
        # Change the glideslope
        sia.Glideslope = 4
        # Offset the runway altitude
        sia.RunwayAltitudeOffset = 10
        # Use the terrain as an altitude reference for the runway
        sia.UseRunwayTerrain = True

    # endregion

    # region ConfigureRunwaySite
    def test_ConfigureRunwaySite(self):
        userRunways = AviatorCodeSnippets.AG_AvtrCatalog.RunwayCategory.UserRunways.GetAsCatalogSource()
        if userRunways.Contains("New User Runway"):
            userRunways.RemoveChild("New User Runway")

        takeoff = AviatorCodeSnippets.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        self.ConfigureRunwaySite(clr.CastAs(takeoff.Site, ISiteRunway))
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)
        if userRunways.Contains("New User Runway"):
            userRunways.RemoveChild("New User Runway")

    def ConfigureRunwaySite(self, runway):
        # Set the latitude, longitude, and altitude
        runway.Latitude = 41
        runway.Longitude = 77
        runway.Altitude = 5

        # Set the altitude reference
        runway.AltitudeRef = AgEAvtrAGLMSL.eAltMSL

        # Set the heading
        runway.HighEndHeading = 195
        # Opt to use true heading
        runway.IsMagnetic = False

        # Set the length of the runway
        runway.Length = 5

        # Rename the runway
        runway.GetAsSite().Name = "New User Runway"
        # Add the runway to the catalog to use it for next time
        runway.AddToCatalog(True)

    # endregion

    # region ConfigureRunwayFromCatalog
    def test_ConfigureRunwayFromCatalog(self):
        userRunways = AviatorCodeSnippets.AG_AvtrCatalog.RunwayCategory.UserRunways
        if not (userRunways.GetAsCatalogSource().Contains("New User Runway")):
            userRunways.AddUserRunway("New User Runway")

        takeoff = AviatorCodeSnippets.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        self.ConfigureRunwayFromCatalog(clr.CastAs(takeoff.Site, ISiteRunway), AviatorCodeSnippets.AG_AvtrCatalog)
        AviatorCodeSnippets.AG_Procedures.RemoveAtIndex(0)
        if userRunways.GetAsCatalogSource().Contains("New User Runway"):
            userRunways.GetAsCatalogSource().RemoveChild("New User Runway")

    def ConfigureRunwayFromCatalog(self, runway, catalog):
        # Get the source of user runways
        userRunways = catalog.RunwayCategory.UserRunways
        if userRunways.GetAsCatalogSource().Contains("New User Runway"):
            # If so, get the user runway with the given name
            runwayFromCatalog = userRunways.GetUserRunway("New User Runway")
            # Copy the parameters of that runway
            runway.CopyFromCatalog(clr.CastAs(runwayFromCatalog, ICatalogRunway))

    # endregion
