import pytest
from test_util import *
from assertion_harness import *

from ansys.stk.core.stkobjects.aviator import *
from ansys.stk.core.stkobjects import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        EarlyBoundTests.InitHelper()

    @staticmethod
    def InitHelper():
        TestBase.LoadTestScenario(Path.Combine("AviatorTests", "AviatorTests.sc"))

        scenario: "IStkObject" = clr.CastAs(TestBase.Application.current_scenario, IStkObject)
        EarlyBoundTests.AG_Scenario = TestBase.Application.current_scenario
        EarlyBoundTests.AG_AC = clr.Convert(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "AviatorAC")), Aircraft
        )
        # Set to Propagator to Aviator
        EarlyBoundTests.AG_AC.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_AVIATOR)
        # Get the aircrafts route (still on the STKObjects side)
        aircraftRoute: "VehiclePropagatorAviator" = clr.CastAs(EarlyBoundTests.AG_AC.route, VehiclePropagatorAviator)
        # Get the Aviator propagator
        EarlyBoundTests.AG_AvtrProp = clr.CastAs(aircraftRoute.avtr_propagator, AviatorPropagator)
        # Get the Aviator mission
        EarlyBoundTests.AG_Mission = EarlyBoundTests.AG_AvtrProp.avtr_mission
        # Get the phases
        EarlyBoundTests.AG_Phases = EarlyBoundTests.AG_Mission.phases
        # Get the procedures
        EarlyBoundTests.AG_Procedures = EarlyBoundTests.AG_Phases[0].procedures
        # Get the Aviator Catalog
        EarlyBoundTests.AG_AvtrCatalog = EarlyBoundTests.AG_AvtrProp.avtr_catalog
        # Get the User Aircraft Models
        EarlyBoundTests.AG_AvtrAircraftModels = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.aircraft_models
        # Get the Aviator Aircraft
        EarlyBoundTests.AG_AvtrAircraft = clr.CastAs(EarlyBoundTests.AG_Mission.vehicle, AircraftModel)
        # Create a target object
        EarlyBoundTests.AG_Target = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.TARGET, "Target")

        acModelsAsCatalogSource: "ICatalogSource" = EarlyBoundTests.AG_AvtrAircraftModels.get_as_catalog_source()
        EarlyBoundTests.AG_AvtrAircraft = EarlyBoundTests.AG_AvtrAircraftModels.get_aircraft("NUNIT CSharp Test")
        # Assign the aircraft
        EarlyBoundTests.AG_Mission.vehicle = clr.CastAs(EarlyBoundTests.AG_AvtrAircraft, IAviatorVehicle)

        # Setting up Aviator Catalog databases
        arincPath: str = TestBase.GetScenarioFile("FAANFD18_SlimForTestOnly")
        EarlyBoundTests.AG_AvtrCatalog.runway_category.arinc424_runways.master_data_filepath = arincPath
        EarlyBoundTests.AG_AvtrCatalog.runway_category.arinc424_runways.get_as_catalog_source().save()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_AC = None
        TestBase.Uninitialize()

    # endregion

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
    AG_Target: "IStkObject" = None
    # endregion

    # region Mission
    @category("Mission Tests")
    def test_Mission(self):
        Assert.assertEqual("NUNIT CSharp Test", EarlyBoundTests.AG_Mission.vehicle.get_as_catalog_item().name)

    # endregion

    # region Configuration
    @category("Configuration Tests")
    def test_Configuration(self):
        acCopy: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        defConfig: "Configuration" = acCopy.default_configuration

        defConfig.base_drag_index = 1
        Assert.assertEqual(1, defConfig.base_drag_index)

        defConfig.set_empty_cg(1, 2, 3)
        Assert.assertEqual(1, defConfig.empty_cgx)
        Assert.assertEqual(2, defConfig.empty_cgy)
        Assert.assertEqual(3, defConfig.empty_cgz)

        defConfig2: "Configuration" = EarlyBoundTests.AG_AvtrAircraft.default_configuration
        Assert.assertEqual(0, defConfig2.empty_cgx)
        Assert.assertEqual(0, defConfig2.empty_cgy)
        Assert.assertEqual(0, defConfig2.empty_cgz)

        defConfig.paste_configuration(defConfig2)
        Assert.assertEqual(0, defConfig.empty_cgx)
        Assert.assertEqual(0, defConfig.empty_cgy)
        Assert.assertEqual(0, defConfig.empty_cgz)

        acCopy.get_as_catalog_item().remove()

    # endregion

    # region Stations
    @category("Configuration Tests")
    def test_Stations(self):
        acCopy: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        defConfig: "Configuration" = acCopy.default_configuration

        stations: "StationCollection" = defConfig.get_stations()
        stationCount: int = Array.Length(stations.station_names)

        totalCapacity: float = defConfig.total_capacity
        initialState: float = defConfig.initial_fuel_state

        internalTank: "FuelTankInternal" = stations.add_internal_fuel_tank()
        stationCount += 1
        internalTank.name = "Tank Name Test"
        Assert.assertTrue(stations.contains_station("Tank Name Test"))
        Assert.assertEqual("Tank Name Test", stations.station_names[(stationCount - 1)])
        Assert.assertEqual(stationCount, stations.count)

        internalTankSize: float = 2000
        internalTank.capacity = internalTankSize
        internalTank.initial_fuel_state = internalTankSize
        Assert.assertEqual((totalCapacity + internalTankSize), defConfig.total_capacity)
        Assert.assertEqual((initialState + internalTankSize), defConfig.initial_fuel_state)

        stations.remove_station_by_name("Tank Name Test")
        stationCount -= 1
        Assert.assertEqual(stationCount, stations.count)
        Assert.assertEqual(totalCapacity, defConfig.total_capacity)
        Assert.assertEqual(initialState, defConfig.initial_fuel_state)

        payloadStation: "PayloadStation" = stations.add_payload_station()
        stationCount += 1
        payloadStation.name = "Payload Station Name Test"
        Assert.assertTrue(stations.contains_station("Payload Station Name Test"))
        Assert.assertEqual("Payload Station Name Test", stations.station_names[(stationCount - 1)])
        Assert.assertEqual(stationCount, stations.count)

        externalTank: "FuelTankExternal" = payloadStation.add_external_fuel_tank()
        externalTankSize: float = 3000
        externalTank.capacity = externalTankSize
        externalTank.initial_fuel_state = externalTankSize
        # Need to save the aircraft to update these values.
        # Assert.AreEqual(totalCapacity + externalTankSize, defConfig.TotalCapacity);
        # Assert.AreEqual(initialState + externalTankSize, defConfig.InitialFuelState);

        payloadStation.remove_sub_item()
        Assert.assertEqual(totalCapacity, defConfig.total_capacity)
        Assert.assertEqual(initialState, defConfig.initial_fuel_state)

        # Check that the stations are always returned in alphabetical order
        stations.remove_station_by_name("Payload Station Name Test")
        Assert.assertEqual(0, stations.count)

        currentTank: "FuelTankInternal" = stations.add_internal_fuel_tank()
        currentTank.name = "4"
        currentTank = stations.add_internal_fuel_tank()
        currentTank.name = "1"
        currentPayloadStation: "PayloadStation" = stations.add_payload_station()
        currentPayloadStation.name = "3"
        currentPayloadStation = stations.add_payload_station()
        currentPayloadStation.name = "2"
        currentPayloadStation = stations.add_payload_station()
        currentPayloadStation.name = "1.5"
        currentPayloadStation = stations.add_payload_station()
        currentPayloadStation.name = "Station 1"
        currentPayloadStation = stations.add_payload_station()
        currentPayloadStation.name = "Station 2"

        Assert.assertEqual(7, stations.count)

        Assert.assertEqual("1", stations.station_names[0])
        Assert.assertEqual("1.5", stations.station_names[1])
        Assert.assertEqual("2", stations.station_names[2])
        Assert.assertEqual("3", stations.station_names[3])
        Assert.assertEqual("4", stations.station_names[4])
        Assert.assertEqual("Station 1", stations.station_names[5])
        Assert.assertEqual("Station 2", stations.station_names[6])

        tank: "FuelTankInternal" = clr.CastAs(stations[0], FuelTankInternal)
        Assert.assertEqual("1", tank.name)
        station3: "PayloadStation" = clr.CastAs(stations[3], PayloadStation)
        Assert.assertEqual("3", station3.name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            testVal: "IStation" = stations[-1]
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            testVal: "IStation" = stations[stations.count]

        stations.remove_at_index(3)
        Assert.assertEqual(6, stations.count)
        Assert.assertEqual("2", stations.station_names[2])
        Assert.assertEqual("4", stations.station_names[3])

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            stations.remove_at_index(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            stations.remove_at_index(stations.count)

        acCopy.get_as_catalog_item().remove()

    # endregion

    # region Wind
    @category("Weather Tests")
    @category("ExcludeOnLinux")
    def test_Wind(self):
        tolerance: float = 1e-09

        wind: "WindModel" = EarlyBoundTests.AG_Mission.wind_model
        with pytest.raises(Exception, match=RegexSubstringMatch("procedure model")):
            wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.PROCEDURE_MODEL

        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        wind.wind_model_type = WIND_MODEL_TYPE.CONSTANT_WIND
        addsWind: "WindModelADDS" = None
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            addsWind = wind.mode_as_adds

        constWind: "WindModelConstant" = wind.mode_as_constant
        constWind.wind_speed = 1
        Assert.assertAlmostEqual(1, constWind.wind_speed, delta=tolerance)
        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.SCENARIO_MODEL
        wind.wind_model_type = WIND_MODEL_TYPE.CONSTANT_WIND
        wind.copy()
        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        wind.paste()

        Assert.assertAlmostEqual(0, constWind.wind_speed, delta=tolerance)

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        procWind: "WindModel" = proc1.wind_model
        procWind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        procConstWind: "WindModelConstant" = procWind.mode_as_constant

        Assert.assertAlmostEqual(0, procConstWind.wind_speed, delta=tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("cannot be edited from the procedure")):
            procWind.wind_model_type = WIND_MODEL_TYPE.CONSTANT_WIND

        procWind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.PROCEDURE_MODEL
        procWind.wind_model_type = WIND_MODEL_TYPE.CONSTANT_WIND
        procConstWind.wind_speed = 1
        Assert.assertAlmostEqual(1, procConstWind.wind_speed, delta=tolerance)

        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.SCENARIO_MODEL
        wind.copy()
        procWind.paste()
        Assert.assertAlmostEqual(0, procConstWind.wind_speed, delta=tolerance)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region WindModelConstant
    @category("Weather Tests")
    def test_WindModelConstant(self):
        tolerance: float = 1e-09

        wind: "WindModel" = EarlyBoundTests.AG_Mission.wind_model
        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        wind.wind_model_type = WIND_MODEL_TYPE.CONSTANT_WIND
        constWind: "WindModelConstant" = wind.mode_as_constant

        constWind.name = "Constant Name Test"
        Assert.assertEqual("Constant Name Test", constWind.name)
        constWind.wind_speed = 1
        Assert.assertAlmostEqual(1, constWind.wind_speed, delta=tolerance)

        wind.wind_model_type = WIND_MODEL_TYPE.DISABLED
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            constWind.wind_speed = 1

        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.SCENARIO_MODEL
        wind.copy()
        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        wind.paste()

    # endregion

    # region WindModelADDS
    @category("Weather Tests")
    @category("ExcludeOnLinux")
    def test_WindModelADDS(self):
        wind: "WindModel" = EarlyBoundTests.AG_Mission.wind_model
        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        wind.wind_model_type = WIND_MODEL_TYPE.ADDS
        ADDSWind: "WindModelADDS" = wind.mode_as_adds

        ADDSWind.name = "ADDS Name Test"
        Assert.assertEqual("ADDS Name Test", ADDSWind.name)

        ADDSWind.interp_blend_time = 1
        Assert.assertEqual(1, ADDSWind.interp_blend_time)

        wind.wind_model_type = WIND_MODEL_TYPE.DISABLED
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            ADDSWind.interp_blend_time = 1

        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.SCENARIO_MODEL
        wind.copy()
        wind.wind_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        wind.paste()

    # endregion

    # region Atmosphere
    @category("Weather Tests")
    def test_Atmosphere(self):
        atmos: "AtmosphereModel" = EarlyBoundTests.AG_Mission.atmosphere_model
        with pytest.raises(Exception, match=RegexSubstringMatch("procedure model")):
            atmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.PROCEDURE_MODEL

        atmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        basicAtmos: "AtmosphereModelBasic" = atmos.mode_as_basic
        basicAtmos.basic_model_type = ATMOSPHERE_MODEL.STANDARD1976

        basicAtmos.use_non_standard_atmosphere = True
        basicAtmos.temperature = 300
        Assert.assertEqual(300, basicAtmos.temperature)

        atmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.SCENARIO_MODEL
        atmos.copy()
        atmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        atmos.paste()

        Assert.assertEqual(288.15, basicAtmos.temperature)

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        procAtmos: "AtmosphereModel" = proc1.atmosphere_model
        procAtmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        procAtmosBasic: "AtmosphereModelBasic" = procAtmos.mode_as_basic

        with pytest.raises(Exception, match=RegexSubstringMatch("cannot be edited from the procedure")):
            procAtmosBasic.use_non_standard_atmosphere = True

        procAtmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.PROCEDURE_MODEL
        procAtmosBasic.use_non_standard_atmosphere = True
        Assert.assertTrue(procAtmosBasic.use_non_standard_atmosphere)

        atmos.copy()
        procAtmos.paste()
        Assert.assertFalse(procAtmosBasic.use_non_standard_atmosphere)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region BasicAtmosphereModel
    @category("Weather Tests")
    def test_BasicAtmosphereModel(self):
        atmos: "AtmosphereModel" = EarlyBoundTests.AG_Mission.atmosphere_model
        atmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        basicAtmos: "AtmosphereModelBasic" = atmos.mode_as_basic
        basicAtmos.basic_model_type = ATMOSPHERE_MODEL.STANDARD1976

        Assert.assertEqual(288.15, basicAtmos.temperature)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicAtmos.temperature = 290
        basicAtmos.use_non_standard_atmosphere = True
        basicAtmos.temperature = 290
        Assert.assertEqual(290, basicAtmos.temperature)

        atmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.SCENARIO_MODEL
        atmos.copy()
        atmos.atmosphere_model_source = WIND_ATMOS_MODEL_SOURCE.MISSION_MODEL
        atmos.paste()

    # endregion

    # region PhaseCollection
    @category("Mission Tests")
    def test_PhaseCollection(self):
        Assert.assertEqual(1, EarlyBoundTests.AG_Phases.count)
        Assert.assertEqual("Phase 1", EarlyBoundTests.AG_Phases[0].name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            testVal: "Phase" = EarlyBoundTests.AG_Phases[-1]
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            testVal: "Phase" = EarlyBoundTests.AG_Phases[EarlyBoundTests.AG_Phases.count]

        phase2: "Phase" = EarlyBoundTests.AG_Phases.add()
        Assert.assertEqual(2, EarlyBoundTests.AG_Phases.count)
        Assert.assertEqual("Phase 2", phase2.name)

        phase0: "Phase" = EarlyBoundTests.AG_Phases.add_at_index(0)
        phase0.name = "Phase 0"
        Assert.assertEqual("Phase 0", EarlyBoundTests.AG_Phases[0].name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            EarlyBoundTests.AG_Phases.add_at_index(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            EarlyBoundTests.AG_Phases.add_at_index((EarlyBoundTests.AG_Phases.count + 1))

        countMinusOne: float = EarlyBoundTests.AG_Phases.count - 1
        EarlyBoundTests.AG_Phases.remove(phase0)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Phases.count)
        Assert.assertEqual("Phase 1", EarlyBoundTests.AG_Phases[0].name)

        with pytest.raises(Exception):
            EarlyBoundTests.AG_Phases.remove(phase0)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            EarlyBoundTests.AG_Phases.remove_at_index(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            EarlyBoundTests.AG_Phases.remove_at_index(EarlyBoundTests.AG_Phases.count)

        EarlyBoundTests.AG_Phases.remove_at_index(1)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be at least one phase")):
            EarlyBoundTests.AG_Phases.remove_at_index(0)
        with pytest.raises(Exception):
            EarlyBoundTests.AG_Phases.remove(phase0)

        Assert.assertEqual(1, EarlyBoundTests.AG_Phases.count)

    # endregion

    # region Phase
    @category("Mission Tests")
    def test_Phase(self):
        currentPhase: "Phase" = EarlyBoundTests.AG_Phases[0]

        currentPhase.name = "My First Phase"
        Assert.assertEqual("My First Phase", EarlyBoundTests.AG_Phases[0].name)
        currentPhase.name = "Phase 1"

        with pytest.raises(Exception, match=RegexSubstringMatch("does not contain")):
            testPerfModel: "PerformanceModelOptions" = currentPhase.get_performance_model_by_type("Test")

        acc: "PerformanceModelOptions" = currentPhase.get_performance_model_by_type("Acceleration")

        Assert.assertEqual("Built-In Model", acc.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("cannot be renamed")):
            acc.rename("Test")
        with pytest.raises(Exception, match=RegexSubstringMatch("cannot be deleted")):
            acc.delete()
        Assert.assertTrue(acc.is_linked_to_catalog)

        acc.link_to_catalog("Built-In Model")
        Assert.assertEqual("Built-In Model", acc.name)
        Assert.assertTrue(acc.is_linked_to_catalog)
        basicAcc: "AircraftBasicAccelerationModel" = clr.CastAs(acc.properties, AircraftBasicAccelerationModel)

        acc.copy_from_catalog("Built-In Model")
        Assert.assertEqual("Built-In Model", acc.name)
        Assert.assertEqual(False, acc.is_linked_to_catalog)

        acc.create_new("Advanced Acceleration Model")
        name: str = acc.name
        Assert.assertTrue(("Advanced Acceleration Model" in name))
        Assert.assertEqual(False, acc.is_linked_to_catalog)
        advAcc: "AircraftAdvancedAccelerationModel" = clr.CastAs(acc.properties, AircraftAdvancedAccelerationModel)

        acc.rename("Test Rename")
        Assert.assertEqual("Test Rename", acc.name)

        vtol: "PerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")

        vtol.delete()
        with pytest.raises(Exception, match=RegexSubstringMatch("no performance model")):
            vtol.rename("Test")
        with pytest.raises(Exception, match=RegexSubstringMatch("no performance model")):
            vtol.delete()
        with pytest.raises(Exception, match=RegexSubstringMatch("no performance model")):
            perfModel: "IPerformanceModel" = vtol.properties
        with pytest.raises(Exception, match=RegexSubstringMatch("no performance model")):
            isLinked: bool = vtol.is_linked_to_catalog

        vtol.link_to_catalog("AGI VTOL Model")
        Assert.assertTrue(vtol.is_linked_to_catalog)
        unknownModel: "IPerformanceModel" = vtol.properties

        currentPhase.set_default_perf_models()
        Assert.assertEqual("Built-In Model", acc.name)

        with pytest.raises(Exception, match=RegexSubstringMatch("No copy")):
            currentPhase.paste_performance_models()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        phase2: "Phase" = EarlyBoundTests.AG_Phases.add()
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ENROUTE
        )

        acc.create_new("Advanced Acceleration Model")
        acc.rename("Testing Copy Paste")
        Assert.assertEqual("Testing Copy Paste", acc.name)
        currentPhase.copy_performance_models()
        phase2.paste_performance_models()
        acc2: "PerformanceModelOptions" = phase2.get_performance_model_by_type("Acceleration")
        Assert.assertEqual("Testing Copy Paste", acc2.name)

        EarlyBoundTests.AG_Phases.remove(phase2)
        currentPhase.procedures.remove(proc2)
        currentPhase.procedures.remove(proc1)

        missileTest: "MissileModel" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models.add_missile(
            "Missile Perf Model Test"
        )
        EarlyBoundTests.AG_Mission.vehicle = clr.CastAs(missileTest, IAviatorVehicle)
        acc = currentPhase.get_performance_model_by_type("Acceleration")
        with pytest.raises(Exception):
            perfModel: "IPerformanceModel" = acc.properties

        rotorcraftTest: "RotorcraftModel" = (
            EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models.add_rotorcraft(
                "Rotorcraft Perf Model Test"
            )
        )
        EarlyBoundTests.AG_Mission.vehicle = clr.CastAs(rotorcraftTest, IAviatorVehicle)
        acc = currentPhase.get_performance_model_by_type("Acceleration")
        with pytest.raises(Exception):
            perfModel: "IPerformanceModel" = acc.properties

        EarlyBoundTests.AG_Mission.vehicle = clr.CastAs(EarlyBoundTests.AG_AvtrAircraft, IAviatorVehicle)
        EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models.get_as_catalog_source().remove_child(
            "Missile Perf Model Test"
        )
        EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models.get_as_catalog_source().remove_child(
            "Rotorcraft Perf Model Test"
        )
        Assert.assertEqual(0, currentPhase.procedures.count)
        currentPhase.set_default_perf_models()

    # endregion

    # region ProcedureCollection
    @category("Mission Tests")
    def test_ProcedureCollection(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        proc1.name = "Procedure 1"
        Assert.assertEqual(1, EarlyBoundTests.AG_Procedures.count)

        proc3: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ENROUTE
        )
        proc3.name = "Procedure 3"

        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add_at_index(
            1, SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ENROUTE
        )
        proc2.name = "Procedure 2"

        Assert.assertEqual("Procedure 2", EarlyBoundTests.AG_Procedures[1].name)

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            testVal: "IProcedure" = EarlyBoundTests.AG_Procedures[-1]
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            testVal: "IProcedure" = EarlyBoundTests.AG_Procedures[EarlyBoundTests.AG_Procedures.count]

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            EarlyBoundTests.AG_Procedures.add_at_index(
                -1, SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ENROUTE
            )
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            EarlyBoundTests.AG_Procedures.add_at_index(
                (EarlyBoundTests.AG_Procedures.count + 1),
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE,
                PROCEDURE_TYPE.PROC_ENROUTE,
            )

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            EarlyBoundTests.AG_Procedures.remove_at_index(-1)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid index")):
            EarlyBoundTests.AG_Procedures.remove_at_index(EarlyBoundTests.AG_Procedures.count)

        countMinusOne: float = EarlyBoundTests.AG_Procedures.count - 1
        EarlyBoundTests.AG_Procedures.remove_at_index(1)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Procedures.count)
        Assert.assertEqual("Procedure 3", EarlyBoundTests.AG_Procedures[1].name)

        countMinusOne = EarlyBoundTests.AG_Procedures.count - 1
        EarlyBoundTests.AG_Procedures.remove(proc3)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Procedures.count)

        with pytest.raises(Exception):
            EarlyBoundTests.AG_Procedures.remove(proc3)

        EarlyBoundTests.AG_Procedures.remove_at_index(0)
        self.EmptyProcedures()

    # endregion

    # region ProcedureTimeOptions
    @category("Mission Tests")
    def test_ProcedureTimeOptions(self):
        tolerance: float = 1e-06

        self.EmptyProcedures()

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ENROUTE
        )
        proc3: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_POINT_TO_POINT
        )
        proc4: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_LANDING)

        # //////// TESTING TAKEOFF TIME OPTIONS /////////////
        timeOpts: "ProcedureTimeOptions" = proc1.time_options
        Assert.assertTrue(timeOpts.start_time_enabled)
        Assert.assertTrue(timeOpts.interrupt_time_enabled)
        Assert.assertEqual(False, timeOpts.stop_time_enabled)

        timeOpts.set_start_time(0)
        start: float = float(timeOpts.start_time)
        Assert.assertEqual(0, start)
        timeOpts.set_start_time((start + 1))
        start = float(timeOpts.start_time)
        Assert.assertEqual(1, start)
        Assert.assertTrue(timeOpts.use_start_time)
        timeOpts.use_start_time = False
        Assert.assertEqual(False, timeOpts.use_start_time)
        start = float(timeOpts.start_time)
        Assert.assertEqual(0, start)

        oldTime: float = float(timeOpts.interrupt_time)
        timeOpts.set_interrupt_time((oldTime - 1))
        newTime: float = float(timeOpts.interrupt_time)
        Assert.assertEqual((oldTime - 1), newTime)
        Assert.assertTrue(timeOpts.use_interrupt_time)
        timeOpts.use_interrupt_time = False
        Assert.assertEqual(False, timeOpts.use_interrupt_time)
        newTime = float(timeOpts.interrupt_time)
        Assert.assertEqual(oldTime, newTime)

        Assert.assertEqual(False, timeOpts.use_stop_time)
        with pytest.raises(Exception, match=RegexSubstringMatch("not enabled")):
            timeOpts.use_stop_time = True
        with pytest.raises(Exception, match=RegexSubstringMatch("not enabled")):
            timeOpts.set_stop_time(timeOpts.stop_time)

        # //////// TESTING ENROUTE TIME OPTIONS /////////////

        timeOpts2: "ProcedureTimeOptions" = proc2.time_options
        Assert.assertEqual(False, timeOpts2.start_time_enabled)
        Assert.assertTrue(timeOpts2.interrupt_time_enabled)
        Assert.assertTrue(timeOpts2.stop_time_enabled)

        Assert.assertEqual(False, timeOpts2.use_start_time)
        with pytest.raises(Exception, match=RegexSubstringMatch("not enabled")):
            timeOpts2.use_start_time = True
        with pytest.raises(Exception, match=RegexSubstringMatch("not enabled")):
            timeOpts2.set_start_time(timeOpts2.start_time)

        oldTime = float(timeOpts2.interrupt_time)
        timeOpts2.set_interrupt_time((float(oldTime) - 1))
        newTime = float(timeOpts2.interrupt_time)
        Assert.assertEqual((float(oldTime) - 1), float(newTime))
        Assert.assertTrue(timeOpts2.use_interrupt_time)
        timeOpts2.use_interrupt_time = False
        Assert.assertEqual(False, timeOpts2.use_interrupt_time)
        newTime = float(timeOpts2.interrupt_time)
        Assert.assertEqual(float(oldTime), float(newTime))

        oldstopTime: float = float(timeOpts2.stop_time)
        timeOpts2.set_stop_time((oldstopTime - 1))
        newStopTime: float = float(timeOpts2.stop_time)
        Assert.assertEqual((oldstopTime - 1), newStopTime)
        Assert.assertTrue(timeOpts2.use_stop_time)
        timeOpts2.use_stop_time = False
        Assert.assertEqual(False, timeOpts2.use_stop_time)
        newStopTime = float(timeOpts2.stop_time)
        # The stop time doesn't go back to the original time until
        # the start time of the first procedure is rest
        Assert.assertAlmostEqual((oldstopTime - 1), newStopTime, delta=tolerance)
        timeOpts.set_start_time(0)
        timeOpts.use_start_time = False
        newStopTime = float(timeOpts2.stop_time)
        Assert.assertAlmostEqual(oldstopTime, newStopTime, delta=tolerance)

        # //////// TESTING BASIC POINT TO POINT TIME OPTIONS /////////////

        timeOpts3: "ProcedureTimeOptions" = proc3.time_options
        Assert.assertEqual(False, timeOpts3.start_time_enabled)
        Assert.assertTrue(timeOpts3.interrupt_time_enabled)
        Assert.assertTrue(timeOpts3.stop_time_enabled)

        # //////// TESTING LANDING TIME OPTIONS /////////////

        timeOpts4: "ProcedureTimeOptions" = proc4.time_options
        Assert.assertEqual(False, timeOpts4.start_time_enabled)
        Assert.assertTrue(timeOpts4.interrupt_time_enabled)
        Assert.assertTrue(timeOpts4.stop_time_enabled)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc1, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc3, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc4, IProcedure))
        TestBase.Application.unit_preferences.reset_units()

    # endregion

    # region CalculationOptions
    @category("Mission Tests")
    def test_CalculationOptions(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)

        calcOpts: "CalculationOptions" = proc1.calculation_options

        calcOpts.max_rel_motion_factor = 1.1
        Assert.assertEqual(1.1, calcOpts.max_rel_motion_factor)
        calcOpts.state_cache_time_interval = 0.002
        Assert.assertEqual(0.002, calcOpts.state_cache_time_interval)

        calcOpts.time_resolution = 0.003
        Assert.assertEqual(0.003, calcOpts.time_resolution)
        calcOpts.max_iterations = 54
        Assert.assertEqual(54, calcOpts.max_iterations)
        calcOpts.max_bad_steps = 5
        Assert.assertEqual(5, calcOpts.max_bad_steps)

        calcOpts.integrator_type = NUMERICAL_INTEGRATOR.RUNGE_KUTTA4
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA4, calcOpts.integrator_type)
        Assert.assertEqual("RK4", calcOpts.integrator_type_string)

        calcOpts.integrator_type_string = "RK45"
        Assert.assertEqual(NUMERICAL_INTEGRATOR.RUNGE_KUTTA45, calcOpts.integrator_type)
        Assert.assertEqual("RK45", calcOpts.integrator_type_string)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc1, IProcedure))

    # endregion

    # region RefuelDump
    @category("Mission Tests")
    def test_RefuelDump(self):
        self.EmptyProcedures()

        # Procedure where Refuel/Dump is not supported

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        Assert.assertFalse(proc1.refuel_dump_is_supported)
        rdp: "RefuelDumpProperties" = proc1.refuel_dump_properties

        with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
            rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.REFUEL_DUMP_DISABLED, 0.0)
        with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
            o: typing.Any = rdp.refuel_dump_mode
        with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
            o: typing.Any = rdp.refuel_dump_mode_value
        with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
            o: typing.Any = rdp.refuel_dump_rate
        with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
            o: typing.Any = rdp.refuel_dump_time_offset
        with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
            o: typing.Any = rdp.can_use_end_of_enroute_segment_as_epoch
        with pytest.raises(Exception, match=RegexSubstringMatch("is not supported")):
            o: typing.Any = rdp.use_end_of_enroute_segment_as_epoch

        # Procedure where Refuel/Dump is supported

        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_ARC_ENROUTE)
        Assert.assertTrue(proc2.refuel_dump_is_supported)
        rdp = proc2.refuel_dump_properties

        rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.REFUEL_DUMP_DISABLED, 1.0)
        Assert.assertEqual(REFUEL_DUMP_MODE.REFUEL_DUMP_DISABLED, rdp.refuel_dump_mode)
        Assert.assertEqual(1.0, rdp.refuel_dump_mode_value)  # "not applicable" in GUI

        rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.REFUEL_TOP_OFF, 2.0)
        Assert.assertEqual(REFUEL_DUMP_MODE.REFUEL_TOP_OFF, rdp.refuel_dump_mode)
        Assert.assertEqual(2.0, rdp.refuel_dump_mode_value)  # "not applicable" in GUI

        rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.REFUEL_TO_FUEL_STATE, 3.0)
        Assert.assertEqual(REFUEL_DUMP_MODE.REFUEL_TO_FUEL_STATE, rdp.refuel_dump_mode)
        Assert.assertEqual(3.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.REFUEL_TO_WEIGHT, 4.0)
        Assert.assertEqual(REFUEL_DUMP_MODE.REFUEL_TO_WEIGHT, rdp.refuel_dump_mode)
        Assert.assertEqual(4.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.REFUEL_QUANTITY, 5.0)
        Assert.assertEqual(REFUEL_DUMP_MODE.REFUEL_QUANTITY, rdp.refuel_dump_mode)
        Assert.assertEqual(5.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.DUMP_TO_FUEL_STATE, 6.0)
        Assert.assertEqual(REFUEL_DUMP_MODE.DUMP_TO_FUEL_STATE, rdp.refuel_dump_mode)
        Assert.assertEqual(6.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.DUMP_TO_WEIGHT, 7.0)
        Assert.assertEqual(REFUEL_DUMP_MODE.DUMP_TO_WEIGHT, rdp.refuel_dump_mode)
        Assert.assertEqual(7.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(REFUEL_DUMP_MODE.DUMP_QUANTITY, 8.0)
        Assert.assertEqual(REFUEL_DUMP_MODE.DUMP_QUANTITY, rdp.refuel_dump_mode)
        Assert.assertEqual(8.0, rdp.refuel_dump_mode_value)

        rdp.refuel_dump_rate = 10
        Assert.assertEqual(10, rdp.refuel_dump_rate)
        rdp.refuel_dump_rate = -11
        Assert.assertEqual(11, rdp.refuel_dump_rate)  # When set to negative number, sets to absolute val. Same as GUI.

        rdp.refuel_dump_time_offset = 20
        Assert.assertEqual(20, rdp.refuel_dump_time_offset)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            rdp.refuel_dump_time_offset = -22

        Assert.assertFalse(rdp.can_use_end_of_enroute_segment_as_epoch)

        rdp.use_end_of_enroute_segment_as_epoch = False
        Assert.assertFalse(rdp.use_end_of_enroute_segment_as_epoch)
        rdp.use_end_of_enroute_segment_as_epoch = True
        Assert.assertTrue(rdp.use_end_of_enroute_segment_as_epoch)

        # Procedure where CanUseEndOfEnrouteSegmentAsEpoch

        proc3: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_HOLDING_CIRCULAR
        )
        Assert.assertTrue(proc3.refuel_dump_is_supported)
        rdp = proc3.refuel_dump_properties

        Assert.assertTrue(rdp.can_use_end_of_enroute_segment_as_epoch)

        rdp.use_end_of_enroute_segment_as_epoch = False
        Assert.assertFalse(rdp.use_end_of_enroute_segment_as_epoch)
        rdp.use_end_of_enroute_segment_as_epoch = True
        Assert.assertTrue(rdp.use_end_of_enroute_segment_as_epoch)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(proc2)
        EarlyBoundTests.AG_Procedures.remove(proc3)

    # endregion

    # region ArcEnroute
    @category("Procedure Tests")
    def test_ArcEnroute(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        arcProc: "ProcedureArcEnroute" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ARC_ENROUTE),
            ProcedureArcEnroute,
        )

        alt: "ArcAltitudeAndDelayOptions" = arcProc.altitude_options
        self.ArcAltitudeAndDelayOptions(alt)

        arc: "ArcOptions" = arcProc.arc_options
        self.ArcOptions(arc)

        arcAirspeed: "CruiseAirspeedOptions" = arcProc.arc_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(arcAirspeed)

        enroute: "IEnrouteAndDelayOptions" = arcProc.enroute_options
        self.EnrouteAndDelayOptions(enroute)

        airspeed: "CruiseAirspeedOptions" = arcProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        turnOpts: "EnrouteTurnDirectionOptions" = arcProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(arcProc, IProcedure))

    # endregion

    # region ArcPointToPoint
    @category("Procedure Tests")
    def test_ArcPointToPoint(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        arcProc: "ProcedureArcPointToPoint" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ARC_POINT_TO_POINT
            ),
            ProcedureArcPointToPoint,
        )

        alt: "ArcAltitudeOptions" = arcProc.altitude_options
        self.ArcAltitudeOptions(alt)

        arc: "ArcOptions" = arcProc.arc_options
        self.ArcOptions(arc)

        arcAirspeed: "CruiseAirspeedOptions" = arcProc.arc_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(arcAirspeed)

        enroute: "EnrouteOptions" = arcProc.enroute_options
        self.EnrouteOptions(enroute)

        airspeed: "CruiseAirspeedOptions" = arcProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        turnOpts: "EnrouteTurnDirectionOptions" = arcProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        arcProc.fly_cruise_airspeed_profile = False
        Assert.assertEqual(False, arcProc.fly_cruise_airspeed_profile)

        vertOpts: "ArcVerticalPlaneOptions" = arcProc.vertical_plane_options
        self.ArcVerticalPlane(vertOpts)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(arcProc, IProcedure))

    # endregion

    # region AreaTargetSearch
    @category("Procedure Tests")
    def test_AreaTargetSearch(self):
        self.EmptyProcedures()

        areaTargetObj: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(
            STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget"
        )
        areaTargetProc: "ProcedureAreaTargetSearch" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_STK_AREA_TARGET, PROCEDURE_TYPE.PROC_AREA_TARGET_SEARCH),
            ProcedureAreaTargetSearch,
        )

        self.TestProcedureName(areaTargetProc.get_as_procedure(), "AreaTargetSearch")
        self.AltitudeOptions(areaTargetProc.altitude_options)
        self.EnrouteOptions(areaTargetProc.enroute_options)
        self.EnrouteCruiseAirspeed(areaTargetProc.enroute_cruise_airspeed_options)

        areaTargetProc.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_BASIC_POINT_TO_POINT
        Assert.assertEqual(FLIGHT_LINE_PROC_TYPE.PROC_TYPE_BASIC_POINT_TO_POINT, areaTargetProc.procedure_type)
        areaTargetProc.max_separation = 0.2
        Assert.assertEqual(0.2, areaTargetProc.max_separation)
        areaTargetProc.course_mode = SEARCH_PATTERN_COURSE_MODE.COURSE_MODE_LOW
        Assert.assertEqual(SEARCH_PATTERN_COURSE_MODE.COURSE_MODE_LOW, areaTargetProc.course_mode)
        areaTargetProc.first_leg_retrograde = True
        Assert.assertTrue(areaTargetProc.first_leg_retrograde)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            areaTargetProc.centroid_true_course = 5
        areaTargetProc.course_mode = SEARCH_PATTERN_COURSE_MODE.COURSE_MODE_OVERRIDE
        areaTargetProc.centroid_true_course = 5
        course: typing.Any = areaTargetProc.centroid_true_course
        Assert.assertEqual(5, float(course))

        areaTargetProc.fly_cruise_airspeed_profile = False
        Assert.assertEqual(False, areaTargetProc.fly_cruise_airspeed_profile)
        areaTargetProc.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_ENROUTE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            areaTargetProc.fly_cruise_airspeed_profile = False

        areaTargetProc.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_BASIC_POINT_TO_POINT
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            areaTargetProc.must_level_off = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            areaTargetProc.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_AUTOMATIC_MANEUVER
        areaTargetProc.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_ENROUTE
        areaTargetProc.must_level_off = True
        Assert.assertTrue(areaTargetProc.must_level_off)
        areaTargetProc.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER
        Assert.assertEqual(
            ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER, areaTargetProc.level_off_mode
        )

        takeoffProc: "IProcedure" = EarlyBoundTests.AG_Procedures.add_at_index(
            0, SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF
        )
        areaTargetProc.course_mode = SEARCH_PATTERN_COURSE_MODE.COURSE_MODE_HIGH
        EarlyBoundTests.AG_AvtrProp.propagate()
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            areaTargetProc.first_leg_retrograde = True

        areaTargetObj.unload()
        EarlyBoundTests.AG_Procedures.remove(takeoffProc)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(areaTargetProc, IProcedure))

    # endregion

    # region BasicPointToPoint
    @category("Procedure Tests")
    def test_BasicPointToPoint(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        p2p: "ProcedureBasicPointToPoint" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_POINT_TO_POINT
            ),
            ProcedureBasicPointToPoint,
        )

        alt: "AltitudeOptions" = p2p.altitude_options
        self.AltitudeOptions(alt)

        nav: "NavigationOptions" = p2p.navigation_options
        self.NavigationOptions(nav)

        enroute: "EnrouteOptions" = p2p.enroute_options
        self.EnrouteOptions(enroute)

        airspeed: "ICruiseAirspeedAndProfileOptions" = p2p.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeedAndProfile(airspeed)

        vert: "VerticalPlaneAndFlightPathOptions" = p2p.vertical_plane_options
        self.VerticalPlaneAndFlightPathOptions(vert)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(p2p, IProcedure))

    # endregion

    # region Delay
    @category("Procedure Tests")
    def test_Delay(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        delay: "ProcedureDelay" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_DELAY),
            ProcedureDelay,
        )

        delay.altitude_mode = DELAY_ALTITUDE_MODE.DELAY_DEFAULT_CRUISE_ALTITUDE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            delay.altitude = 5000

        delay.altitude_mode = DELAY_ALTITUDE_MODE.DELAY_OVERRIDE
        delay.altitude = 5000
        Assert.assertEqual(5000, delay.altitude)

        airspeedOpts: "CruiseAirspeedOptions" = delay.cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeedOpts)

        delay.turn_direction = NAVIGATOR_TURN_DIRECTION.NAVIGATOR_TURN_RIGHT
        Assert.assertEqual(NAVIGATOR_TURN_DIRECTION.NAVIGATOR_TURN_RIGHT, delay.turn_direction)
        delay.turn_radius_factor = 3
        Assert.assertEqual(3, delay.turn_radius_factor)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(delay, IProcedure))

    # endregion

    # region Enroute
    @category("Procedure Tests")
    def test_Enroute(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        enroute: "ProcedureEnroute" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ENROUTE),
            ProcedureEnroute,
        )

        alt: "AltitudeMSLAndLevelOffOptions" = enroute.altitude_msl_options
        self.AltitudeMSLAndLevelOffOptions(alt)

        nav: "NavigationOptions" = enroute.navigation_options
        self.NavigationOptions(nav)

        enrouteOpts: "IEnrouteAndDelayOptions" = enroute.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        airspeed: "CruiseAirspeedOptions" = enroute.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(enroute, IProcedure))

    # endregion

    # region ExternalEphemeris
    @category("Procedure Tests")
    def test_ExternalEphemeris(self):
        self.EmptyProcedures()

        extEphem: "ProcedureExtEphem" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_REFERENCE_STATE, PROCEDURE_TYPE.PROC_EXT_EPHEM),
            ProcedureExtEphem,
        )

        proc: "IProcedure" = extEphem.get_as_procedure()
        Assert.assertEqual("ExtEphem", proc.name)
        proc.name = "ExtEphemTest"
        Assert.assertEqual("ExtEphemTest", proc.name)

        with pytest.raises(Exception, match=RegexSubstringMatch("No ephemeris file set")):
            d: float = extEphem.ephemeris_file_duration

        extEphem.ephemeris_file = TestBase.GetScenarioFile("ExternalTestBFW.e")
        Assert.assertTrue(("ExternalTestBFW.e" in extEphem.ephemeris_file))
        Assert.assertAlmostEqual(799.26, extEphem.ephemeris_file_duration, delta=0.01)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            extEphem.ephemeris_file = TestBase.GetScenarioFile("bogus.e")
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            extEphem.ephemeris_file = TestBase.GetScenarioFile("Aircraft1.ac")

        # System.Windows.Forms.MessageBox.Show("after set ephem file");

        extEphem.flight_mode = EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_FORWARD_FLIGHT_CLIMB
        Assert.assertEqual(EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_FORWARD_FLIGHT_CLIMB, extEphem.flight_mode)
        extEphem.flight_mode = EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_FORWARD_FLIGHT_CRUISE
        Assert.assertEqual(EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_FORWARD_FLIGHT_CRUISE, extEphem.flight_mode)
        extEphem.flight_mode = EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_FORWARD_FLIGHT_DESCEND
        Assert.assertEqual(EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_FORWARD_FLIGHT_DESCEND, extEphem.flight_mode)
        extEphem.flight_mode = EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_LANDING
        Assert.assertEqual(EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_LANDING, extEphem.flight_mode)
        extEphem.flight_mode = EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_LANDING_WOW
        Assert.assertEqual(EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_LANDING_WOW, extEphem.flight_mode)
        extEphem.flight_mode = EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_TAKEOFF
        Assert.assertEqual(EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_TAKEOFF, extEphem.flight_mode)
        extEphem.flight_mode = EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_TAKEOFF_WOW
        Assert.assertEqual(EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_TAKEOFF_WOW, extEphem.flight_mode)
        extEphem.flight_mode = EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_VTOL_HOVER
        Assert.assertEqual(EXT_EPHEM_FLIGHT_MODE.EXT_EPHEM_FLIGHT_MODE_VTOL_HOVER, extEphem.flight_mode)

        extEphem.use_start_duration = False
        Assert.assertFalse(extEphem.use_start_duration)

        with pytest.raises(Exception, match=RegexSubstringMatch("not writeable")):
            extEphem.start_time = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("not writeable")):
            extEphem.duration = 200

        extEphem.use_start_duration = True
        Assert.assertTrue(extEphem.use_start_duration)

        extEphem.start_time = 100
        Assert.assertAlmostEqual(100, extEphem.start_time, delta=extEphem.start_time)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be non-negative")):
            extEphem.start_time = -100

        extEphem.duration = 200
        Assert.assertAlmostEqual(200, extEphem.duration, delta=extEphem.duration)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be non-negative")):
            extEphem.duration = -200

        extEphem.use_shift_rotate = False
        Assert.assertFalse(extEphem.use_shift_rotate)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            extEphem.shift_time = 10
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            extEphem.latitude = 20
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            extEphem.longitude = 30
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            extEphem.altitude = 40
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            extEphem.course = 50
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            extEphem.altitude_mode = EPHEM_SHIFT_ROTATE_ALTITUDE_MODE.ALTITUDE_MODE_MSL
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            extEphem.course_mode = EPHEM_SHIFT_ROTATE_COURSE_MODE.COURSE_MODE_TRUE
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            extEphem.shift_rotate_set(22)

        extEphem.use_shift_rotate = True
        Assert.assertTrue(extEphem.use_shift_rotate)

        extEphem.shift_time = 10

        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "rad")
        TestBase.Application.unit_preferences.set_current_unit("LatitudeUnit", "rad")
        extEphem.latitude = 20  # TODO - verify properties use UnitPreferences - AIR-10324

        extEphem.longitude = 30
        extEphem.altitude = 40
        extEphem.course = 50

        extEphem.altitude_mode = EPHEM_SHIFT_ROTATE_ALTITUDE_MODE.ALTITUDE_MODE_MSL
        Assert.assertEqual(EPHEM_SHIFT_ROTATE_ALTITUDE_MODE.ALTITUDE_MODE_MSL, extEphem.altitude_mode)
        extEphem.altitude_mode = EPHEM_SHIFT_ROTATE_ALTITUDE_MODE.ALTITUDE_MODE_WGS
        Assert.assertEqual(EPHEM_SHIFT_ROTATE_ALTITUDE_MODE.ALTITUDE_MODE_WGS, extEphem.altitude_mode)
        extEphem.altitude_mode = EPHEM_SHIFT_ROTATE_ALTITUDE_MODE.ALTITUDE_MODE_REL
        Assert.assertEqual(EPHEM_SHIFT_ROTATE_ALTITUDE_MODE.ALTITUDE_MODE_REL, extEphem.altitude_mode)

        extEphem.course_mode = EPHEM_SHIFT_ROTATE_COURSE_MODE.COURSE_MODE_TRUE
        Assert.assertEqual(EPHEM_SHIFT_ROTATE_COURSE_MODE.COURSE_MODE_TRUE, extEphem.course_mode)
        extEphem.course_mode = EPHEM_SHIFT_ROTATE_COURSE_MODE.COURSE_MODE_MAGNITUDE
        Assert.assertEqual(EPHEM_SHIFT_ROTATE_COURSE_MODE.COURSE_MODE_MAGNITUDE, extEphem.course_mode)
        extEphem.course_mode = EPHEM_SHIFT_ROTATE_COURSE_MODE.COURSE_MODE_REL
        Assert.assertEqual(EPHEM_SHIFT_ROTATE_COURSE_MODE.COURSE_MODE_REL, extEphem.course_mode)

        extEphem.shift_rotate_set(10)

        # TODO - verify values - AIR-10323

        extEphem.shift_rotate_set(30)

        # TODO - verify values - AIR-10323

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(extEphem, IProcedure))

    # endregion

    # region FlightLine
    @category("Procedure Tests")
    def test_FlightLine(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        flightLine: "ProcedureFlightLine" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_FLIGHT_LINE),
            ProcedureFlightLine,
        )

        alt: "AltitudeOptions" = flightLine.altitude_options
        self.AltitudeOptions(alt)

        flightAirspeed: "CruiseAirspeedOptions" = flightLine.flight_line_airspeed_options
        self.EnrouteCruiseAirspeed(flightAirspeed)

        enroute: "EnrouteOptions" = flightLine.enroute_options
        self.EnrouteOptions(enroute)

        turnOpts: "EnrouteTurnDirectionOptions" = flightLine.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "CruiseAirspeedOptions" = flightLine.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        flightLine.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_TERRAIN_FOLLOW
        flightLine.outbound_course = 5
        course: typing.Any = flightLine.outbound_course
        Assert.assertEqual(5, float(course))
        flightLine.use_magnetic_heading = True
        Assert.assertTrue(flightLine.use_magnetic_heading)
        flightLine.leg_length = 11
        Assert.assertEqual(11, flightLine.leg_length)

        flightLine.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_TERRAIN_FOLLOW
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flightLine.fly_cruise_airspeed_profile = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flightLine.must_level_off = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flightLine.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_AUTOMATIC_MANEUVER

        flightLine.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_BASIC_POINT_TO_POINT
        flightLine.fly_cruise_airspeed_profile = False
        Assert.assertEqual(False, flightLine.fly_cruise_airspeed_profile)

        flightLine.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_ENROUTE
        flightLine.must_level_off = True
        Assert.assertTrue(flightLine.must_level_off)
        flightLine.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER
        Assert.assertEqual(ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER, flightLine.level_off_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(flightLine, IProcedure))

    # endregion

    # region FormationFlyer
    @category("Procedure Tests")
    def test_FormationFlyer(self):
        TestBase.LoadTestScenario(TestBase.PathCombine("AviatorTests", "Formation_Flyer", "Scenario1.sc"))
        EarlyBoundTests.AG_Scenario = TestBase.Application.current_scenario
        EarlyBoundTests.AG_AC = clr.Convert(
            (EarlyBoundTests.AG_Scenario.children.get_item_by_name("Wingman")), Aircraft
        )
        aircraftRoute: "VehiclePropagatorAviator" = clr.CastAs(EarlyBoundTests.AG_AC.route, VehiclePropagatorAviator)
        EarlyBoundTests.AG_AvtrProp = clr.CastAs(aircraftRoute.avtr_propagator, AviatorPropagator)
        EarlyBoundTests.AG_Mission = EarlyBoundTests.AG_AvtrProp.avtr_mission
        EarlyBoundTests.AG_Phases = EarlyBoundTests.AG_Mission.phases
        EarlyBoundTests.AG_Procedures = EarlyBoundTests.AG_Phases[0].procedures

        EarlyBoundTests.AG_Procedures.remove_at_index(2)  # Remove existing Formation Flyer procedure.

        formationFlyer: "ProcedureFormationFlyer" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_FORMATION_FLYER
            ),
            ProcedureFormationFlyer,
        )

        formationFlyer.cross_range_close_rate = 10
        Assert.assertEqual(10, formationFlyer.cross_range_close_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):  # Can be set. Should be invalid.
            formationFlyer.cross_range_close_rate = -10

        formationFlyer.initial_close_max_speed_advantage = 20
        Assert.assertEqual(20, formationFlyer.initial_close_max_speed_advantage)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of bounds")):  # Can be set. Should be invalid.
            formationFlyer.initial_close_max_speed_advantage = -20

        formationFlyer.max_time_step = 2
        Assert.assertEqual(2, formationFlyer.max_time_step)
        formationFlyer.max_time_step = 1
        Assert.assertEqual(1, formationFlyer.max_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of bounds")):  # Can be set. Should be invalid.
            formationFlyer.max_time_step = 0

        formationFlyer.min_time_step = 0.2
        Assert.assertEqual(0.2, formationFlyer.min_time_step)
        formationFlyer.min_time_step = 0.1
        Assert.assertEqual(0.1, formationFlyer.min_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("out of bounds")):
            formationFlyer.min_time_step = 0

        stopCond: "FORMATION_FLYER_STOP_CONDITION"

        for stopCond in Enum.GetValues(clr.TypeOf(FORMATION_FLYER_STOP_CONDITION)):
            formationFlyer.stop_condition = stopCond
            Assert.assertEqual(stopCond, formationFlyer.stop_condition)
            if FORMATION_FLYER_STOP_CONDITION.FORMATION_FLYER_STOP_AFTER_TIME == stopCond:
                formationFlyer.stop_time = 30
                Assert.assertEqual(30, formationFlyer.stop_time)
                with pytest.raises(Exception, match=RegexSubstringMatch("out of bounds")):
                    formationFlyer.stop_time = -30

                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_down_range = 40
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_fuel_state = 50

            elif FORMATION_FLYER_STOP_CONDITION.FORMATION_FLYER_STOP_AFTER_DOWN_RANGE == stopCond:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_time = 30

                formationFlyer.stop_down_range = 40
                Assert.assertEqual(40, formationFlyer.stop_down_range)
                with pytest.raises(Exception, match=RegexSubstringMatch("out of bounds")):
                    formationFlyer.stop_down_range = -40

                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_fuel_state = 50

            elif FORMATION_FLYER_STOP_CONDITION.FORMATION_FLYER_STOP_AFTER_FUEL_STATE == stopCond:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_time = 30
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_down_range = 40

                formationFlyer.stop_fuel_state = 50
                Assert.assertEqual(50, formationFlyer.stop_fuel_state)
                with pytest.raises(Exception, match=RegexSubstringMatch("out of bounds")):
                    formationFlyer.stop_fuel_state = -50

            else:
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_time = 30
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_down_range = 40
                with pytest.raises(Exception, match=RegexSubstringMatch("Cannot set")):
                    formationFlyer.stop_fuel_state = 50

        formationFlyer.stop_on_hover = False
        Assert.assertFalse(formationFlyer.stop_on_hover)
        formationFlyer.stop_on_hover = True
        Assert.assertTrue(formationFlyer.stop_on_hover)

        EarlyBoundTests.InitHelper()

    # endregion

    # region FormationRecover
    @category("Procedure Tests")
    def test_FormationRecover(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        EarlyBoundTests.AG_AvtrProp.propagate()

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj: "IStkObject" = acObj.copy_object("AC2")
        ac2: "Aircraft" = clr.CastAs(ac2Obj, Aircraft)
        route2: "VehiclePropagatorAviator" = clr.CastAs(ac2.route, VehiclePropagatorAviator)
        prop2: "AviatorPropagator" = clr.CastAs(route2.avtr_propagator, AviatorPropagator)
        mission2: "Mission" = prop2.avtr_mission
        phases2: "PhaseCollection" = mission2.phases
        procedures2: "ProcedureCollection" = phases2[0].procedures

        proc2: "IProcedure" = procedures2.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_HOLDING_CIRCULAR
        )
        prop2.propagate()

        formRecov: "ProcedureFormationRecover" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_STK_VEHICLE, PROCEDURE_TYPE.PROC_FORMATION_RECOVER),
            ProcedureFormationRecover,
        )

        self.TestProcedureName(formRecov.get_as_procedure(), "Formation/Recover")

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.unit_preferences.set_current_unit("Duration", "Sec")
        formRecov.start_time = 2
        startTime: typing.Any = formRecov.start_time
        Assert.assertEqual(2, float(startTime))

        minTime: typing.Any = formRecov.get_minimum_time(False)
        maxTime: typing.Any = formRecov.maximum_time
        Assert.assertEqual(0, float(minTime))
        firstStartTime: typing.Any = formRecov.find_first_valid_start_time(minTime, maxTime, 30)
        startTime = formRecov.start_time
        Assert.assertEqual(float(startTime), float(firstStartTime))

        Assert.assertTrue(("Center" == str(formRecov.formation_point)))
        formRecov.formation_point = "Missile SubPoint(Detic)"
        Assert.assertTrue(("Missile SubPoint(Detic)" == str(formRecov.formation_point)))
        formRecov.interpolate_point_position_vel = True
        Assert.assertTrue(formRecov.interpolate_point_position_vel)

        formRecov.altitude_offset = 5
        Assert.assertEqual(5, formRecov.altitude_offset)
        formRecov.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_TAKEOFF
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            formRecov.override_fuel_flow_value = 123
        formRecov.consider_accel_for_fuel_flow = True
        Assert.assertTrue(formRecov.consider_accel_for_fuel_flow)

        formRecov.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE
        formRecov.override_fuel_flow_value = 123
        Assert.assertAlmostEqual(123, formRecov.override_fuel_flow_value, delta=tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            formRecov.consider_accel_for_fuel_flow = True

        formRecov.first_pause = 1
        Assert.assertEqual(1, formRecov.first_pause)
        formRecov.transition_time = 2
        Assert.assertEqual(2, formRecov.transition_time)
        formRecov.second_pause = 3
        Assert.assertEqual(3, formRecov.second_pause)
        formRecov.display_step_time = 4
        Assert.assertEqual(4, formRecov.display_step_time)

        formRecov.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_TAKEOFF
        Assert.assertEqual(PHASE_OF_FLIGHT.FLIGHT_PHASE_TAKEOFF, formRecov.flight_mode)

        formRecov.flight_path_angle = 5
        angle: typing.Any = formRecov.flight_path_angle
        Assert.assertEqual(5, float(angle))
        formRecov.radius_factor = 2
        Assert.assertEqual(2, formRecov.radius_factor)

        formRecov.use_delay = True
        Assert.assertTrue(formRecov.use_delay)
        formRecov.delay_turn_direction = DELAY_TURN_DIRECTION.DELAY_TURN_LEFT
        Assert.assertEqual(DELAY_TURN_DIRECTION.DELAY_TURN_LEFT, formRecov.delay_turn_direction)
        formRecov.use_delay = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            formRecov.delay_turn_direction = DELAY_TURN_DIRECTION.DELAY_TURN_LEFT

        formRecov.use_delay = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            airspeed: "CruiseAirspeedOptions" = formRecov.delay_cruise_airspeed_options
        formRecov.use_delay = True
        self.EnrouteCruiseAirspeed(formRecov.delay_cruise_airspeed_options)

        self.EnrouteOptions(formRecov.enroute_options)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_AvtrProp.propagate()
        with pytest.raises(Exception, match=RegexSubstringMatch("first procedure")):
            formRecov.find_first_valid_start_time(minTime, maxTime, 30)
        with pytest.raises(Exception, match=RegexSubstringMatch("first procedure")):
            formRecov.flight_path_angle = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("first procedure")):
            formRecov.radius_factor = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("first procedure")):
            formRecov.use_delay = True
        with pytest.raises(Exception, match=RegexSubstringMatch("first procedure")):
            formRecov.delay_turn_direction = DELAY_TURN_DIRECTION.DELAY_TURN_AUTO
        with pytest.raises(Exception, match=RegexSubstringMatch("first procedure")):
            enrouteOpts: "EnrouteOptions" = formRecov.enroute_options
        with pytest.raises(Exception, match=RegexSubstringMatch("first procedure")):
            airspeed: "CruiseAirspeedOptions" = formRecov.delay_cruise_airspeed_options

        formRecov.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL
        Assert.assertEqual(formRecov.flight_mode, PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL)
        formRecov.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL
        Assert.assertEqual(formRecov.fuel_flow_type, FUEL_FLOW_TYPE.FUEL_FLOW_VTOL)
        currentPhase: "Phase" = EarlyBoundTests.AG_Phases[0]
        vtol: "PerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            formRecov.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            formRecov.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL

        currentPhase.set_default_perf_models()
        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(formRecov, IProcedure))
        ac2Obj.unload()

    # endregion

    # region HoldingCircular
    @category("Procedure Tests")
    def test_HoldingCircular(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        holdingProc: "ProcedureHoldingCircular" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_HOLDING_CIRCULAR
            ),
            ProcedureHoldingCircular,
        )

        alt: "AltitudeMSLOptions" = holdingProc.altitude_options
        self.AltitudeMSLOptions(alt)

        holdAirspeed: "CruiseAirspeedOptions" = holdingProc.hold_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts: "IEnrouteAndDelayOptions" = holdingProc.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts: "EnrouteTurnDirectionOptions" = holdingProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "CruiseAirspeedOptions" = holdingProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.profile_mode = HOLDING_PROFILE_MODE.STK8_COMPATIBLE
        Assert.assertEqual(HOLDING_PROFILE_MODE.STK8_COMPATIBLE, holdingProc.profile_mode)

        holdingProc.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER
        Assert.assertEqual(ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER, holdingProc.level_off_mode)

        holdingProc.bearing = 5
        angle: typing.Any = holdingProc.bearing
        Assert.assertEqual(5, float(angle))
        holdingProc.use_magnetic_heading = False
        Assert.assertEqual(False, holdingProc.use_magnetic_heading)

        holdingProc.range = 11
        Assert.assertEqual(11, holdingProc.range)
        holdingProc.diameter = 15
        Assert.assertEqual(15, holdingProc.diameter)

        with pytest.raises(Exception, match=RegexSubstringMatch("minimum diameter")):
            holdingProc.diameter = 0.01

        holdingProc.use_alternate_entry_points = True
        Assert.assertTrue(holdingProc.use_alternate_entry_points)
        holdingProc.turn_direction = HOLDING_DIRECTION.OUTBOUND_RIGHT_TURN
        Assert.assertEqual(HOLDING_DIRECTION.OUTBOUND_RIGHT_TURN, holdingProc.turn_direction)
        holdingProc.turns = 3
        Assert.assertEqual(3, holdingProc.turns)
        holdingProc.refuel_dump_mode = HOLD_REFUEL_DUMP_MODE.IMMEDIATE_EXIT
        Assert.assertEqual(HOLD_REFUEL_DUMP_MODE.IMMEDIATE_EXIT, holdingProc.refuel_dump_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region HoldingFigure8
    @category("Procedure Tests")
    def test_HoldingFigure8(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        holdingProc: "ProcedureHoldingFigure8" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_HOLDING_FIGURE8
            ),
            ProcedureHoldingFigure8,
        )

        Assert.assertTrue((clr.Is(holdingProc, IProcedure)))

        alt: "AltitudeMSLOptions" = holdingProc.altitude_options
        self.AltitudeMSLOptions(alt)

        holdAirspeed: "CruiseAirspeedOptions" = holdingProc.hold_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts: "IEnrouteAndDelayOptions" = holdingProc.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts: "EnrouteTurnDirectionOptions" = holdingProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "CruiseAirspeedOptions" = holdingProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.profile_mode = HOLDING_PROFILE_MODE.STK8_COMPATIBLE
        Assert.assertEqual(HOLDING_PROFILE_MODE.STK8_COMPATIBLE, holdingProc.profile_mode)

        holdingProc.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER
        Assert.assertEqual(ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER, holdingProc.level_off_mode)

        holdingProc.bearing = 5
        angle: typing.Any = holdingProc.bearing
        Assert.assertEqual(5, float(angle))
        holdingProc.use_magnetic_heading = False
        Assert.assertEqual(False, holdingProc.use_magnetic_heading)

        holdingProc.range = 11
        Assert.assertEqual(11, holdingProc.range)
        holdingProc.width = 14
        Assert.assertEqual(14, holdingProc.width)
        holdingProc.length = 15
        Assert.assertEqual(15, holdingProc.length)

        with pytest.raises(Exception, match=RegexSubstringMatch("minimum diameter")):
            holdingProc.width = 0.01
        with pytest.raises(Exception, match=RegexSubstringMatch("minimum diameter")):
            holdingProc.length = 0.01
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            holdingProc.length = 13

        holdingProc.use_alternate_entry_points = True
        Assert.assertTrue(holdingProc.use_alternate_entry_points)
        holdingProc.turns = 3
        Assert.assertEqual(3, holdingProc.turns)
        holdingProc.refuel_dump_mode = HOLD_REFUEL_DUMP_MODE.IMMEDIATE_EXIT
        Assert.assertEqual(HOLD_REFUEL_DUMP_MODE.IMMEDIATE_EXIT, holdingProc.refuel_dump_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region HoldingRacetrack
    @category("Procedure Tests")
    def test_HoldingRacetrack(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        holdingProc: "ProcedureHoldingRacetrack" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_HOLDING_RACETRACK
            ),
            ProcedureHoldingRacetrack,
        )

        alt: "AltitudeMSLOptions" = holdingProc.altitude_options
        self.AltitudeMSLOptions(alt)

        holdAirspeed: "CruiseAirspeedOptions" = holdingProc.hold_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts: "IEnrouteAndDelayOptions" = holdingProc.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts: "EnrouteTurnDirectionOptions" = holdingProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "CruiseAirspeedOptions" = holdingProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.profile_mode = HOLDING_PROFILE_MODE.STK8_COMPATIBLE
        Assert.assertEqual(HOLDING_PROFILE_MODE.STK8_COMPATIBLE, holdingProc.profile_mode)

        holdingProc.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER
        Assert.assertEqual(ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER, holdingProc.level_off_mode)

        holdingProc.bearing = 5
        angle: typing.Any = holdingProc.bearing
        Assert.assertEqual(5, float(angle))
        holdingProc.use_magnetic_heading = False
        Assert.assertEqual(False, holdingProc.use_magnetic_heading)

        holdingProc.range = 11
        Assert.assertEqual(11, holdingProc.range)
        holdingProc.width = 14
        Assert.assertEqual(14, holdingProc.width)
        holdingProc.length = 15
        Assert.assertEqual(15, holdingProc.length)

        with pytest.raises(Exception, match=RegexSubstringMatch("minimum diameter")):
            holdingProc.width = 0.01

        holdingProc.entry_maneuver = HOLDING_ENTRY_MANEUVER.USE_ALTERNATE_ENTRY_POINTS
        Assert.assertEqual(HOLDING_ENTRY_MANEUVER.USE_ALTERNATE_ENTRY_POINTS, holdingProc.entry_maneuver)
        holdingProc.turns = 3
        Assert.assertEqual(3, holdingProc.turns)
        holdingProc.refuel_dump_mode = HOLD_REFUEL_DUMP_MODE.IMMEDIATE_EXIT
        Assert.assertEqual(HOLD_REFUEL_DUMP_MODE.IMMEDIATE_EXIT, holdingProc.refuel_dump_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region Hover
    @category("Procedure Tests")
    def test_Hover(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_TRANSITION_TO_HOVER
        )
        hoverProc: "ProcedureHover" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_HOVER),
            ProcedureHover,
        )

        alt: "HoverAltitudeOptions" = hoverProc.altitude_options
        self.HoverAltitudeOptions(alt)

        hoverProc.hover_mode = HOVER_MODE.HOVER_MODE_FIXED_TIME
        Assert.assertEqual(HOVER_MODE.HOVER_MODE_FIXED_TIME, hoverProc.hover_mode)
        hoverProc.fixed_time = "00:00:20.000"
        fixedtime: typing.Any = hoverProc.fixed_time
        Assert.assertTrue(("00:00:20.000" == str(fixedtime)))

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.heading_mode = VTOL_HEADING_MODE.HEADING_ALIGN_TRANSLATION_COURSE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_absolute_course(5, False)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_relative_course(4)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_final_translation_course()
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.final_heading_rate = VTOL_RATE_MODE.ALWAYS_STOP
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.translation_mode = VTOL_TRANSLATION_MODE.COME_TO_STOP
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.bearing = 6
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.use_magnetic_bearing = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.range = 7
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.final_course_mode = VTOL_TRANSLATION_FINAL_COURSE_MODE.ANTICIPATE_NEXT_TRANSLATION
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.smooth_translation_mode = VTOL_RATE_MODE.ALWAYS_STOP
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.radius_factor = 3

        hoverProc.hover_mode = HOVER_MODE.HOVER_MODE_MANEUVER
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.fixed_time = 15

        hoverProc.heading_mode = VTOL_HEADING_MODE.HEADING_INTO_WIND
        Assert.assertEqual(VTOL_HEADING_MODE.HEADING_INTO_WIND, hoverProc.heading_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_absolute_course(5, False)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_relative_course(4)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_final_translation_course()
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.final_heading_rate = VTOL_RATE_MODE.ALWAYS_STOP

        hoverProc.heading_mode = VTOL_HEADING_MODE.HEADING_INDEPENDENT
        Assert.assertEqual(VTOL_HEADING_MODE.HEADING_INDEPENDENT, hoverProc.heading_mode)
        hoverProc.set_absolute_course(5, False)
        Assert.assertEqual(VTOL_FINAL_HEADING_MODE.FINAL_HEADING_ABSOLUTE, hoverProc.final_heading_mode)
        absCourse: typing.Any = hoverProc.absolute_course
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertEqual(False, hoverProc.use_magnetic_heading)

        hoverProc.set_relative_course(4)
        Assert.assertEqual(VTOL_FINAL_HEADING_MODE.FINAL_HEADING_RELATIVE, hoverProc.final_heading_mode)
        relCourse: typing.Any = hoverProc.relative_course
        Assert.assertEqual(4, float(relCourse))

        hoverProc.set_final_translation_course()
        Assert.assertEqual(VTOL_FINAL_HEADING_MODE.FINAL_HEADING_TRANSLATION_COURSE, hoverProc.final_heading_mode)

        hoverProc.final_heading_rate = VTOL_RATE_MODE.ALWAYS_STOP
        Assert.assertEqual(VTOL_RATE_MODE.ALWAYS_STOP, hoverProc.final_heading_rate)

        hoverProc.translation_mode = VTOL_TRANSLATION_MODE.COME_TO_STOP
        Assert.assertEqual(VTOL_TRANSLATION_MODE.COME_TO_STOP, hoverProc.translation_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.bearing = 6
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.use_magnetic_bearing = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.range = 7
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.final_course_mode = VTOL_TRANSLATION_FINAL_COURSE_MODE.ANTICIPATE_NEXT_TRANSLATION
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.smooth_translation_mode = VTOL_RATE_MODE.ALWAYS_STOP
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.radius_factor = 3

        hoverProc.translation_mode = VTOL_TRANSLATION_MODE.SET_BEARING_AND_RANGE
        hoverProc.bearing = 6
        bearing: typing.Any = hoverProc.bearing
        Assert.assertEqual(6, float(bearing))

        hoverProc.use_magnetic_bearing = True
        Assert.assertTrue(hoverProc.use_magnetic_bearing)

        hoverProc.range = 7
        Assert.assertEqual(7, hoverProc.range)

        hoverProc.final_course_mode = VTOL_TRANSLATION_FINAL_COURSE_MODE.ANTICIPATE_NEXT_TRANSLATION
        Assert.assertEqual(VTOL_TRANSLATION_FINAL_COURSE_MODE.ANTICIPATE_NEXT_TRANSLATION, hoverProc.final_course_mode)

        hoverProc.smooth_translation_mode = VTOL_RATE_MODE.ALWAYS_STOP
        Assert.assertEqual(VTOL_RATE_MODE.ALWAYS_STOP, hoverProc.smooth_translation_mode)

        hoverProc.radius_factor = 3
        Assert.assertEqual(3, hoverProc.radius_factor)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc1, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(hoverProc, IProcedure))

    # endregion

    # region HoverTranslate
    @category("Procedure Tests")
    def test_HoverTranslate(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_TRANSITION_TO_HOVER
        )
        hoverProc: "ProcedureHoverTranslate" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_WAYPOINT, PROCEDURE_TYPE.PROC_HOVER_TRANSLATE),
            ProcedureHoverTranslate,
        )

        alt: "HoverAltitudeOptions" = hoverProc.altitude_options
        self.HoverAltitudeOptions(alt)

        hoverProc.heading_mode = VTOL_HEADING_MODE.HEADING_INTO_WIND
        Assert.assertEqual(VTOL_HEADING_MODE.HEADING_INTO_WIND, hoverProc.heading_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_absolute_course(5, False)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_relative_course(4)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.set_final_translation_course()
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverProc.final_heading_rate = VTOL_RATE_MODE.ALWAYS_STOP

        hoverProc.heading_mode = VTOL_HEADING_MODE.HEADING_INDEPENDENT
        Assert.assertEqual(VTOL_HEADING_MODE.HEADING_INDEPENDENT, hoverProc.heading_mode)
        hoverProc.set_absolute_course(5, False)
        Assert.assertEqual(VTOL_FINAL_HEADING_MODE.FINAL_HEADING_ABSOLUTE, hoverProc.final_heading_mode)
        absCourse: typing.Any = hoverProc.absolute_course
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertEqual(False, hoverProc.use_magnetic_heading)

        hoverProc.set_relative_course(4)
        Assert.assertEqual(VTOL_FINAL_HEADING_MODE.FINAL_HEADING_RELATIVE, hoverProc.final_heading_mode)
        relCourse: typing.Any = hoverProc.relative_course
        Assert.assertEqual(4, float(relCourse))

        hoverProc.set_final_translation_course()
        Assert.assertEqual(VTOL_FINAL_HEADING_MODE.FINAL_HEADING_TRANSLATION_COURSE, hoverProc.final_heading_mode)

        hoverProc.final_heading_rate = VTOL_RATE_MODE.ALWAYS_STOP
        Assert.assertEqual(VTOL_RATE_MODE.ALWAYS_STOP, hoverProc.final_heading_rate)

        hoverProc.final_course_mode = VTOL_TRANSLATION_FINAL_COURSE_MODE.ANTICIPATE_NEXT_TRANSLATION
        Assert.assertEqual(VTOL_TRANSLATION_FINAL_COURSE_MODE.ANTICIPATE_NEXT_TRANSLATION, hoverProc.final_course_mode)

        hoverProc.smooth_translation_mode = VTOL_RATE_MODE.ALWAYS_STOP
        Assert.assertEqual(VTOL_RATE_MODE.ALWAYS_STOP, hoverProc.smooth_translation_mode)

        hoverProc.radius_factor = 3
        Assert.assertEqual(3, hoverProc.radius_factor)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc1, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(hoverProc, IProcedure))

    # endregion

    # region InFormation
    @category("Procedure Tests")
    def test_InFormation(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        EarlyBoundTests.AG_AvtrProp.propagate()

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj: "IStkObject" = acObj.copy_object("AC2")
        ac2: "Aircraft" = clr.CastAs(ac2Obj, Aircraft)
        route2: "VehiclePropagatorAviator" = clr.CastAs(ac2.route, VehiclePropagatorAviator)
        prop2: "AviatorPropagator" = clr.CastAs(route2.avtr_propagator, AviatorPropagator)
        mission2: "Mission" = prop2.avtr_mission
        phases2: "PhaseCollection" = mission2.phases
        procedures2: "ProcedureCollection" = phases2[0].procedures

        proc2: "IProcedure" = procedures2.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_HOLDING_CIRCULAR
        )
        prop2.propagate()

        formRecov: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_STK_VEHICLE, PROCEDURE_TYPE.PROC_FORMATION_RECOVER
        )
        inFormation: "ProcedureInFormation" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_IN_FORMATION),
            ProcedureInFormation,
        )

        self.TestProcedureName(inFormation.get_as_procedure(), "In-Formation")

        inFormation.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL
        Assert.assertEqual(PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL, inFormation.flight_mode)
        inFormation.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_TAKEOFF
        Assert.assertEqual(PHASE_OF_FLIGHT.FLIGHT_PHASE_TAKEOFF, inFormation.flight_mode)

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.unit_preferences.set_current_unit("Duration", "Sec")

        Assert.assertTrue(("Center" == str(inFormation.formation_point)))
        inFormation.formation_point = "AC2 SubPoint(Detic)"
        Assert.assertTrue(("AC2 SubPoint(Detic)" == str(inFormation.formation_point)))

        inFormation.transition_time = 1
        Assert.assertEqual(1, inFormation.transition_time)
        inFormation.hold_time = 2
        Assert.assertEqual(2, inFormation.hold_time)
        inFormation.display_step_time = 3
        Assert.assertEqual(3, inFormation.display_step_time)

        inFormation.trajectory_blending = TRAJECTORY_BLEND_MODE.BLEND_LH_CUBIC
        Assert.assertEqual(TRAJECTORY_BLEND_MODE.BLEND_LH_CUBIC, inFormation.trajectory_blending)

        inFormation.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL
        Assert.assertEqual(FUEL_FLOW_TYPE.FUEL_FLOW_VTOL, inFormation.fuel_flow_type)
        inFormation.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_TAKEOFF
        Assert.assertEqual(FUEL_FLOW_TYPE.FUEL_FLOW_TAKEOFF, inFormation.fuel_flow_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            inFormation.override_fuel_flow_value = 123
        inFormation.consider_accel_for_fuel_flow = True
        Assert.assertTrue(inFormation.consider_accel_for_fuel_flow)

        inFormation.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE
        inFormation.override_fuel_flow_value = 123
        Assert.assertAlmostEqual(123, inFormation.override_fuel_flow_value, delta=tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            inFormation.consider_accel_for_fuel_flow = True

        currentPhase: "Phase" = EarlyBoundTests.AG_Phases[0]
        vtol: "PerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            inFormation.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            inFormation.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL

        currentPhase.set_default_perf_models()
        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(formRecov, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(inFormation, IProcedure))
        ac2Obj.unload()

    # endregion

    # region Landing
    @category("Procedure Tests")
    def test_Landing(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        landing: "ProcedureLanding" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_LANDING), ProcedureLanding
        )

        headingOptions: "RunwayHeadingOptions" = landing.runway_heading_options
        headingOptions.runway_mode = RUNWAY_HIGH_LOW_END.HEADWIND
        Assert.assertEqual(RUNWAY_HIGH_LOW_END.HEADWIND, headingOptions.runway_mode)

        landing.approach_mode = APPROACH_MODE.STANDARD_INSTRUMENT_APPROACH
        Assert.assertEqual(APPROACH_MODE.STANDARD_INSTRUMENT_APPROACH, landing.approach_mode)
        enrouteOpts: "IEnrouteAndDelayOptions" = landing.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        sia: "LandingStandardInstrumentApproach" = landing.mode_as_standard_instrument_approach
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "LandingEnterDownwindPattern" = landing.mode_as_enter_downwind_pattern
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "LandingInterceptGlideslope" = landing.mode_as_intercept_glideslope

        cruiseOpts: "ICruiseAirspeedAndProfileOptions" = landing.enroute_cruise_airspeed_options
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: bool = cruiseOpts.fly_cruise_airspeed_profile
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            cruiseOpts.fly_cruise_airspeed_profile = True

        vertOpts: "IVerticalPlaneOptions" = landing.vertical_plane_options
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            vertOpts.max_enroute_flight_path_angle = 89
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            vertOpts.min_enroute_flight_path_angle = -89
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            vertOpts.max_vert_plane_radius_factor = 0.99

        sia.approach_altitude = 1201
        Assert.assertEqual(1201, sia.approach_altitude)
        sia.use_runway_terrain = True
        Assert.assertTrue(sia.use_runway_terrain)

        landing.approach_mode = APPROACH_MODE.INTERCEPT_GLIDESLOPE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: float = sia.approach_altitude
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            sia.approach_altitude = 1201
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: bool = sia.use_runway_terrain
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            sia.use_runway_terrain = True
        self.VerticalPlaneOptions(vertOpts)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(landing, IProcedure))

    # endregion

    # region Launch
    @category("Procedure Tests")
    def test_Launch(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        missile: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile")), Missile
        )
        traj: "VehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, VehiclePropagatorBallistic)
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, VehicleImpactLocationPoint)
        impact: "VehicleImpactLLA" = clr.CastAs(impactLocation.impact, VehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()

        missile2: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile2")), Missile
        )
        traj2: "VehiclePropagatorBallistic" = clr.CastAs(missile2.trajectory, VehiclePropagatorBallistic)
        impactLocation2: "VehicleImpactLocationPoint" = clr.CastAs(traj2.impact_location, VehicleImpactLocationPoint)
        impact2: "VehicleImpactLLA" = clr.CastAs(impactLocation2.impact, VehicleImpactLLA)
        impact2.lat = -20
        impact2.lon = -20
        traj2.propagate()

        launchProc: "ProcedureLaunch" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_STK_VEHICLE, PROCEDURE_TYPE.PROC_LAUNCH), ProcedureLaunch
        )

        launchProc.launch_time = "1 Jul 1999 00:00:01.000"
        time: typing.Any = launchProc.launch_time
        Assert.assertTrue(("1 Jul 1999 00:00:01.000" == str(time)))

        # Assert.IsTrue(launchProc.PositionPointName.Length > 0);
        launchProc.position_point_name = "Missile2 SubPoint(Centric)"
        position: typing.Any = launchProc.position_point_name
        Assert.assertTrue(("Missile2 SubPoint(Centric)" == str(position)))

        Assert.assertTrue((len(launchProc.direction_vec_name) > 0))
        launchProc.direction_vec_name = "Missile2 North"
        direction: typing.Any = launchProc.direction_vec_name
        Assert.assertTrue(("Missile2 North" == str(direction)))

        launchProc.attitude_mode = LAUNCH_ATTITUDE_MODE.LAUNCH_HOLD_PARENT_ATTITUDE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.true_course_hint = 1

        launchProc.attitude_mode = LAUNCH_ATTITUDE_MODE.LAUNCH_ALIGN_DIRECTION_VECTOR
        Assert.assertEqual(LAUNCH_ATTITUDE_MODE.LAUNCH_ALIGN_DIRECTION_VECTOR, launchProc.attitude_mode)
        launchProc.true_course_hint = 1
        trueCourseHint: typing.Any = launchProc.true_course_hint
        Assert.assertEqual(1, float(trueCourseHint))

        launchProc.specify_launch_airspeed = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.accel_g = 2
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.override_fuel_flow = 1

        launchProc.specify_launch_airspeed = True
        Assert.assertTrue(launchProc.specify_launch_airspeed)

        launchProc.accel_g = 2
        Assert.assertEqual(2, launchProc.accel_g)

        launchProc.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, launchProc.airspeed_type)
        Assert.assertAlmostEqual(251, launchProc.airspeed, delta=tolerance)
        launchProc.set_airspeed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, launchProc.airspeed_type)
        Assert.assertAlmostEqual(0.4, launchProc.airspeed, delta=tolerance)

        launchProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL
        Assert.assertEqual(FUEL_FLOW_TYPE.FUEL_FLOW_VTOL, launchProc.fuel_flow_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.override_fuel_flow = 1

        launchProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE
        Assert.assertEqual(FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE, launchProc.fuel_flow_type)
        launchProc.override_fuel_flow = 10001
        Assert.assertEqual(10001, launchProc.override_fuel_flow)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(launchProc, IProcedure))
        missileObj: "IStkObject" = clr.CastAs(missile, IStkObject)
        missileObj.unload()
        missileObj2: "IStkObject" = clr.CastAs(missile2, IStkObject)
        missileObj2.unload()

    # endregion

    # region LaunchDynState
    @category("Procedure Tests")
    def test_LaunchDynState(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        missile: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile")), Missile
        )
        traj: "VehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, VehiclePropagatorBallistic)
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, VehicleImpactLocationPoint)
        impact: "VehicleImpactLLA" = clr.CastAs(impactLocation.impact, VehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()

        missile2: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile2")), Missile
        )
        traj2: "VehiclePropagatorBallistic" = clr.CastAs(missile2.trajectory, VehiclePropagatorBallistic)
        impactLocation2: "VehicleImpactLocationPoint" = clr.CastAs(traj2.impact_location, VehicleImpactLocationPoint)
        impact2: "VehicleImpactLLA" = clr.CastAs(impactLocation2.impact, VehicleImpactLLA)
        impact2.lat = -20
        impact2.lon = -20
        traj2.propagate()

        launchProc: "ProcedureLaunchDynState" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_DYN_STATE, PROCEDURE_TYPE.PROC_LAUNCH_DYN_STATE),
            ProcedureLaunchDynState,
        )

        launchProc.launch_time = "1 Jul 1999 00:00:01.000"
        time: typing.Any = launchProc.launch_time
        Assert.assertTrue(("1 Jul 1999 00:00:01.000" == str(time)))

        launchProc.coord_frame = LAUNCH_DYN_STATE_COORD_FRAME.LAUNCH_DYN_STATE_COORD_FRAME_LOCAL_HORIZONTAL
        Assert.assertEqual(
            LAUNCH_DYN_STATE_COORD_FRAME.LAUNCH_DYN_STATE_COORD_FRAME_LOCAL_HORIZONTAL, launchProc.coord_frame
        )

        launchProc.bearing_reference = LAUNCH_DYN_STATE_BEARING_REFERENCE.LAUNCH_DYN_STATE_BEARING_REFERENCE_VELOCITY
        Assert.assertEqual(
            LAUNCH_DYN_STATE_BEARING_REFERENCE.LAUNCH_DYN_STATE_BEARING_REFERENCE_VELOCITY, launchProc.bearing_reference
        )

        launchProc.launch_bearing = 1
        launchBearing: typing.Any = launchProc.launch_bearing
        Assert.assertEqual(1, float(launchBearing))

        launchProc.launch_elevation = 2
        launchElevation: typing.Any = launchProc.launch_elevation
        Assert.assertEqual(2, float(launchElevation))

        launchProc.attitude_mode = LAUNCH_ATTITUDE_MODE.LAUNCH_HOLD_PARENT_ATTITUDE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.true_course_hint = 1

        launchProc.attitude_mode = LAUNCH_ATTITUDE_MODE.LAUNCH_ALIGN_DIRECTION_VECTOR
        Assert.assertEqual(LAUNCH_ATTITUDE_MODE.LAUNCH_ALIGN_DIRECTION_VECTOR, launchProc.attitude_mode)
        launchProc.true_course_hint = 1
        trueCourseHint: typing.Any = launchProc.true_course_hint
        Assert.assertEqual(1, float(trueCourseHint))

        launchProc.specify_launch_airspeed = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.accel_g = 2
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.override_fuel_flow = 1

        launchProc.specify_launch_airspeed = True
        Assert.assertTrue(launchProc.specify_launch_airspeed)

        launchProc.accel_g = 2
        Assert.assertEqual(2, launchProc.accel_g)

        launchProc.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, launchProc.airspeed_type)
        Assert.assertAlmostEqual(251, launchProc.airspeed, delta=tolerance)
        launchProc.set_airspeed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, launchProc.airspeed_type)
        Assert.assertAlmostEqual(0.4, launchProc.airspeed, delta=tolerance)

        launchProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL
        Assert.assertEqual(FUEL_FLOW_TYPE.FUEL_FLOW_VTOL, launchProc.fuel_flow_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.override_fuel_flow = 1

        launchProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE
        Assert.assertEqual(FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE, launchProc.fuel_flow_type)
        launchProc.override_fuel_flow = 10001
        Assert.assertEqual(10001, launchProc.override_fuel_flow)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(launchProc, IProcedure))
        missileObj: "IStkObject" = clr.CastAs(missile, IStkObject)
        missileObj.unload()
        missileObj2: "IStkObject" = clr.CastAs(missile2, IStkObject)
        missileObj2.unload()

    # endregion

    # region LaunchWaypoint
    @category("Procedure Tests")
    def test_LaunchWaypoint(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        launchProc: "ProcedureLaunchWaypoint" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_WAYPOINT, PROCEDURE_TYPE.PROC_LAUNCH_WAYPOINT),
            ProcedureLaunchWaypoint,
        )

        launchProc.launch_time = "1 Jul 1999 00:00:01.000"
        time: typing.Any = launchProc.launch_time
        Assert.assertTrue(("1 Jul 1999 00:00:01.000" == str(time)))

        launchProc.altitude_reference = ALTITUDE_REFERENCE.ALTITUDE_REFERENCE_MSL
        Assert.assertEqual(ALTITUDE_REFERENCE.ALTITUDE_REFERENCE_MSL, launchProc.altitude_reference)

        launchProc.launch_altitude = 10
        Assert.assertEqual(10, launchProc.launch_altitude)

        launchProc.launch_true_bearing = 20
        launchTrueBearing: typing.Any = launchProc.launch_true_bearing
        Assert.assertEqual(20, float(launchTrueBearing))

        launchProc.launch_elevation = 30
        launchElevation: typing.Any = launchProc.launch_elevation
        Assert.assertAlmostEqual(30, float(launchElevation), delta=tolerance)

        launchProc.accel_g = 2
        Assert.assertEqual(2, launchProc.accel_g)

        launchProc.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, launchProc.airspeed_type)
        Assert.assertAlmostEqual(251, launchProc.airspeed, delta=tolerance)
        launchProc.set_airspeed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, launchProc.airspeed_type)
        Assert.assertAlmostEqual(0.4, launchProc.airspeed, delta=tolerance)

        launchProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL
        Assert.assertEqual(FUEL_FLOW_TYPE.FUEL_FLOW_VTOL, launchProc.fuel_flow_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            launchProc.override_fuel_flow = 1

        launchProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE
        Assert.assertEqual(FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE, launchProc.fuel_flow_type)
        launchProc.override_fuel_flow = 10001
        Assert.assertEqual(10001, launchProc.override_fuel_flow)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(launchProc, IProcedure))

    # endregion

    # region ParallelFlightLine
    @category("Procedure Tests")
    def test_ParallelFlightLine(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_FLIGHT_LINE
        )
        parallelProc: "ProcedureParallelFlightLine" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_PARALLEL_FLIGHT_LINE
            ),
            ProcedureParallelFlightLine,
        )

        self.TestProcedureName(parallelProc.get_as_procedure(), "Parallel Flight Line")

        alt: "AltitudeOptions" = parallelProc.altitude_options
        self.AltitudeOptions(alt)

        enroute: "EnrouteOptions" = parallelProc.enroute_options
        self.EnrouteOptions(enroute)

        turnOpts: "EnrouteTurnDirectionOptions" = parallelProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "ICruiseAirspeedAndProfileOptions" = parallelProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeedAndProfile(airspeed)

        parallelProc.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_ENROUTE
        parallelProc.orientation = LINE_ORIENTATION.FLIGHT_LINE_TO_RIGHT
        Assert.assertEqual(LINE_ORIENTATION.FLIGHT_LINE_TO_RIGHT, parallelProc.orientation)
        parallelProc.separation = 11
        Assert.assertEqual(11, parallelProc.separation)
        parallelProc.offset = 12
        Assert.assertEqual(12, parallelProc.offset)
        parallelProc.leg_length = 13
        Assert.assertEqual(13, parallelProc.leg_length)

        parallelProc.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_TERRAIN_FOLLOW
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            parallelProc.must_level_off = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            parallelProc.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_AUTOMATIC_MANEUVER

        parallelProc.procedure_type = FLIGHT_LINE_PROC_TYPE.PROC_TYPE_ENROUTE
        Assert.assertEqual(FLIGHT_LINE_PROC_TYPE.PROC_TYPE_ENROUTE, parallelProc.procedure_type)
        parallelProc.must_level_off = True
        Assert.assertTrue(parallelProc.must_level_off)
        parallelProc.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER
        Assert.assertEqual(ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER, parallelProc.level_off_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(parallelProc, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc1, IProcedure))

    # endregion

    # region ReferenceState
    @category("Procedure Tests")
    def test_ReferenceState(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        refState: "ProcedureReferenceState" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_REFERENCE_STATE, PROCEDURE_TYPE.PROC_REFERENCE_STATE),
            ProcedureReferenceState,
        )

        self.TestProcedureName(refState.get_as_procedure(), "ReferenceState")

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        refState.start_time = 1
        time: typing.Any = refState.start_time
        Assert.assertEqual(1, float(time))

        refState.latitude = 1
        Assert.assertEqual(1, refState.latitude)
        refState.longitude = 2
        Assert.assertEqual(2, refState.longitude)
        refState.use_default_cruise_altitude = False
        Assert.assertEqual(False, refState.use_default_cruise_altitude)
        refState.msl_altitude = 10000
        Assert.assertEqual(10000, refState.msl_altitude)
        refState.use_default_cruise_altitude = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            refState.msl_altitude = 10000

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB
        Assert.assertEqual(REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB, refState.performance_mode)

        refState.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.EARTH_FRAME
        Assert.assertEqual(BASIC_MANEUVER_REFERENCE_FRAME.EARTH_FRAME, refState.reference_frame)

        refState.fuel_flow = 5
        Assert.assertAlmostEqual(5, refState.fuel_flow, delta=tolerance)

        # ////////////// TEST FORWARD FLIGHT OPTIONS ///////////////////////

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_LANDING
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            ffTest: "ReferenceStateForwardFlightOptions" = refState.mode_as_forward_flight

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB
        ff: "ReferenceStateForwardFlightOptions" = refState.mode_as_forward_flight

        ff.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, ff.airspeed_type)
        Assert.assertAlmostEqual(251, ff.airspeed, delta=tolerance)
        ff.set_airspeed(AIRSPEED_TYPE.MACH, 0.3)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, ff.airspeed_type)
        Assert.assertAlmostEqual(0.3, ff.airspeed, delta=tolerance)

        ff.flight_path_angle = 1
        fpa: typing.Any = ff.flight_path_angle
        Assert.assertEqual(1, float(fpa))

        ff.course = 2
        course: typing.Any = ff.course
        Assert.assertEqual(2, float(course))

        ff.roll_angle = 3
        roll: typing.Any = ff.roll_angle
        Assert.assertEqual(3, float(roll))

        ff.aoa = 4
        aoa: typing.Any = ff.aoa
        Assert.assertEqual(4, float(aoa))

        ff.sideslip = 5
        sideslip: typing.Any = ff.sideslip
        Assert.assertEqual(5, float(sideslip))

        with pytest.raises(Exception, match=RegexSubstringMatch("Wind Frame")):
            altRateTest: typing.Any = ff.altitude_rate
        with pytest.raises(Exception, match=RegexSubstringMatch("Wind Frame")):
            headingTest: typing.Any = ff.heading

        refState.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.WIND_FRAME
        with pytest.raises(Exception, match=RegexSubstringMatch("Earth Frame")):
            fpaTest: typing.Any = ff.flight_path_angle
        with pytest.raises(Exception, match=RegexSubstringMatch("Earth Frame")):
            courseTest: typing.Any = ff.course

        ff.altitude_rate = 6
        Assert.assertEqual(6, ff.altitude_rate)

        ff.heading = 7
        heading: typing.Any = ff.heading
        Assert.assertEqual(7, float(heading))

        ff.set_longitudinal_accel(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_GROUND_SPEED_DOT, 0.5)
        Assert.assertEqual(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_GROUND_SPEED_DOT, ff.longitudinal_accel_type)
        Assert.assertEqual(0.5, ff.groundspeed_dot)
        ff.set_longitudinal_accel(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_TAS_DOT, 0.6)
        Assert.assertEqual(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_TAS_DOT, ff.longitudinal_accel_type)
        Assert.assertEqual(0.6, ff.tas_dot)

        ff.set_lateral_accel(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_COURSE_DOT, 1.3)
        Assert.assertEqual(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_COURSE_DOT, ff.lateral_accel_type)
        Assert.assertEqual(1.3, ff.course_dot)
        ff.set_lateral_accel(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_HEADING_DOT, 1.4)
        Assert.assertEqual(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_HEADING_DOT, ff.lateral_accel_type)
        Assert.assertEqual(1.4, ff.heading_dot)

        ff.set_attitude_rate(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PITCH_RATE, 1.5)
        Assert.assertEqual(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PITCH_RATE, ff.attitude_rate_type)
        Assert.assertEqual(1.5, ff.pitch_rate)
        ff.set_attitude_rate(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PUSH_PULL_G, 1.6)
        Assert.assertEqual(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PUSH_PULL_G, ff.attitude_rate_type)
        Assert.assertEqual(1.6, ff.push_pull_g)

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_LANDING
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            airspeedTest: float = ff.airspeed

        # ////////////// TEST TAKEOFF LANDING OPTIONS ///////////////////////
        # Note: Should be same as forward flight options except on different interface

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            tlTest: "ReferenceStateTakeoffLandingOptions" = refState.mode_as_takeoff_landing

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_LANDING
        tl: "ReferenceStateTakeoffLandingOptions" = refState.mode_as_takeoff_landing
        refState.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.EARTH_FRAME

        tl.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, tl.airspeed_type)
        Assert.assertAlmostEqual(251, tl.airspeed, delta=tolerance)
        tl.set_airspeed(AIRSPEED_TYPE.MACH, 0.3)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, tl.airspeed_type)
        Assert.assertAlmostEqual(0.3, tl.airspeed, delta=tolerance)

        tl.flight_path_angle = 1
        fpa = tl.flight_path_angle
        Assert.assertEqual(1, float(fpa))

        tl.course = 2
        course = tl.course
        Assert.assertEqual(2, float(course))

        tl.roll_angle = 3
        roll = tl.roll_angle
        Assert.assertEqual(3, float(roll))

        tl.aoa = 4
        aoa = tl.aoa
        Assert.assertEqual(4, float(aoa))

        tl.sideslip = 5
        sideslip = tl.sideslip
        Assert.assertEqual(5, float(sideslip))

        with pytest.raises(Exception, match=RegexSubstringMatch("Wind Frame")):
            altRateTest: typing.Any = tl.altitude_rate
        with pytest.raises(Exception, match=RegexSubstringMatch("Wind Frame")):
            headingTest: typing.Any = tl.heading

        refState.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.WIND_FRAME
        with pytest.raises(Exception, match=RegexSubstringMatch("Earth Frame")):
            fpaTest: typing.Any = tl.flight_path_angle
        with pytest.raises(Exception, match=RegexSubstringMatch("Earth Frame")):
            courseTest: typing.Any = tl.course

        tl.altitude_rate = 6
        Assert.assertEqual(6, tl.altitude_rate)

        tl.heading = 7
        heading = tl.heading
        Assert.assertEqual(7, float(heading))

        tl.set_longitudinal_accel(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_GROUND_SPEED_DOT, 0.5)
        Assert.assertEqual(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_GROUND_SPEED_DOT, tl.longitudinal_accel_type)
        Assert.assertEqual(0.5, tl.groundspeed_dot)
        tl.set_longitudinal_accel(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_TAS_DOT, 0.6)
        Assert.assertEqual(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_TAS_DOT, tl.longitudinal_accel_type)
        Assert.assertEqual(0.6, tl.tas_dot)

        tl.set_lateral_accel(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_COURSE_DOT, 1.3)
        Assert.assertEqual(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_COURSE_DOT, tl.lateral_accel_type)
        Assert.assertEqual(1.3, tl.course_dot)
        tl.set_lateral_accel(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_HEADING_DOT, 1.4)
        Assert.assertEqual(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_HEADING_DOT, tl.lateral_accel_type)
        Assert.assertEqual(1.4, tl.heading_dot)

        tl.set_attitude_rate(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PITCH_RATE, 1.5)
        Assert.assertEqual(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PITCH_RATE, tl.attitude_rate_type)
        Assert.assertEqual(1.5, tl.pitch_rate)
        tl.set_attitude_rate(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PUSH_PULL_G, 1.6)
        Assert.assertEqual(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PUSH_PULL_G, tl.attitude_rate_type)
        Assert.assertEqual(1.6, tl.push_pull_g)

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            airspeedTest: float = tl.airspeed

        # ////////////// TEST HOVER OPTIONS ///////////////////////

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hoverTest: "ReferenceStateHoverOptions" = refState.mode_as_hover

        currentPhase: "Phase" = EarlyBoundTests.AG_Phases[0]
        vtol: "PerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_HOVER
        currentPhase.set_default_perf_models()

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_HOVER
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            refState.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.EARTH_FRAME

        hoverOpts: "ReferenceStateHoverOptions" = refState.mode_as_hover

        hoverOpts.groundspeed = 200
        Assert.assertEqual(200, hoverOpts.groundspeed)

        hoverOpts.altitude_rate = 6
        Assert.assertEqual(6, hoverOpts.altitude_rate)

        hoverOpts.heading = 7
        heading = hoverOpts.heading
        Assert.assertEqual(7, float(heading))

        hoverOpts.course = 8
        course = hoverOpts.course
        Assert.assertEqual(8, float(course))

        hoverOpts.heading_dot = 9
        Assert.assertEqual(9, hoverOpts.heading_dot)

        hoverOpts.course_dot = 10
        Assert.assertEqual(10, hoverOpts.course_dot)

        hoverOpts.roll_angle = 11
        roll = hoverOpts.roll_angle
        Assert.assertEqual(11, float(roll))

        hoverOpts.aoa = 12
        aoa = hoverOpts.aoa
        Assert.assertEqual(12, float(aoa))

        hoverOpts.set_longitudinal_accel(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_GROUND_SPEED_DOT, 0.5)
        Assert.assertEqual(
            REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_GROUND_SPEED_DOT, hoverOpts.longitudinal_accel_type
        )
        Assert.assertEqual(0.5, hoverOpts.groundspeed_dot)
        hoverOpts.set_longitudinal_accel(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_TAS_DOT, 0.6)
        Assert.assertEqual(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_TAS_DOT, hoverOpts.longitudinal_accel_type)
        Assert.assertEqual(0.6, hoverOpts.tas_dot)

        hoverOpts.set_attitude_rate(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PITCH_RATE, 1.5)
        Assert.assertEqual(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PITCH_RATE, hoverOpts.attitude_rate_type)
        Assert.assertEqual(1.5, hoverOpts.pitch_rate)
        hoverOpts.set_attitude_rate(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PUSH_PULL_G, 1.6)
        Assert.assertEqual(REFERENCE_STATE_ATTITUDE_MODE.SPECIFY_PUSH_PULL_G, hoverOpts.attitude_rate_type)
        Assert.assertEqual(1.6, hoverOpts.push_pull_g)

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            groundspeedTest: float = hoverOpts.groundspeed

        # ////////////// TEST WEIGHT ON WHEELS OPTIONS ///////////////////////

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            wowTest: "ReferenceStateWeightOnWheelsOptions" = refState.mode_as_weight_on_wheels

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_TAKEOFF_RUN
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            refState.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.EARTH_FRAME

        wowOpts: "ReferenceStateWeightOnWheelsOptions" = refState.mode_as_weight_on_wheels

        wowOpts.groundspeed = 200
        Assert.assertEqual(200, wowOpts.groundspeed)

        wowOpts.heading = 7
        heading = wowOpts.heading
        Assert.assertEqual(7, float(heading))

        wowOpts.set_longitudinal_accel(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_GROUND_SPEED_DOT, 0.5)
        Assert.assertEqual(
            REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_GROUND_SPEED_DOT, wowOpts.longitudinal_accel_type
        )
        Assert.assertEqual(0.5, wowOpts.groundspeed_dot)
        wowOpts.set_longitudinal_accel(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_TAS_DOT, 0.6)
        Assert.assertEqual(REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE.SPECIFY_TAS_DOT, wowOpts.longitudinal_accel_type)
        Assert.assertEqual(0.6, wowOpts.tas_dot)

        wowOpts.set_lateral_accel(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_COURSE_DOT, 1.3)
        Assert.assertEqual(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_COURSE_DOT, wowOpts.lateral_accel_type)
        Assert.assertEqual(1.3, wowOpts.course_dot)
        wowOpts.set_lateral_accel(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_HEADING_DOT, 1.4)
        Assert.assertEqual(REFERENCE_STATE_LATERAL_ACCEL_MODE.SPECIFY_HEADING_DOT, wowOpts.lateral_accel_type)
        Assert.assertEqual(1.4, wowOpts.heading_dot)

        refState.performance_mode = REFERENCE_STATE_PERF_MODE.REFERENCE_STATE_CLIMB
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            groundspeedTest: float = wowOpts.groundspeed

        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(refState, IProcedure))

    # endregion

    # region Takeoff
    @category("Procedure Tests")
    def test_Takeoff(self):
        self.EmptyProcedures()

        takeoff: "ProcedureTakeoff" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF), ProcedureTakeoff
        )

        headingOptions: "RunwayHeadingOptions" = takeoff.runway_heading_options
        headingOptions.runway_mode = RUNWAY_HIGH_LOW_END.HEADWIND
        Assert.assertEqual(RUNWAY_HIGH_LOW_END.HEADWIND, headingOptions.runway_mode)

        takeoff.takeoff_mode = TAKEOFF_MODE.TAKEOFF_NORMAL
        takeoffNormal: "TakeoffNormal" = takeoff.mode_as_normal
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "TakeoffDeparturePoint" = takeoff.mode_as_departure_point
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "TakeoffLowTransition" = takeoff.mode_as_low_transition

        takeoffNormal.departure_altitude = 501
        Assert.assertEqual(501, takeoffNormal.departure_altitude)
        takeoffNormal.use_runway_terrain = True
        Assert.assertTrue(takeoffNormal.use_runway_terrain)

        takeoff.takeoff_mode = TAKEOFF_MODE.TAKEOFF_FLY_TO_DEPARTURE_POINT
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: float = takeoffNormal.departure_altitude
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            takeoffNormal.departure_altitude = 501
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: bool = takeoffNormal.use_runway_terrain
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            takeoffNormal.use_runway_terrain = True

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))

    # endregion

    # region TerrainFollowing
    @category("Procedure Tests")
    def test_TerrainFollowing(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        terrainFollow: "ProcedureTerrainFollow" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_TERRAIN_FOLLOWING
            ),
            ProcedureTerrainFollow,
        )

        terrainFollow.altitude_agl = 600
        Assert.assertEqual(600, terrainFollow.altitude_agl)

        nav: "NavigationOptions" = terrainFollow.navigation_options
        self.NavigationOptions(nav)

        terrainAirspeed: "CruiseAirspeedOptions" = terrainFollow.terrain_following_airspeed_options
        self.EnrouteCruiseAirspeed(terrainAirspeed)

        terrainFollow.reduce_turn_radii = True
        Assert.assertTrue(terrainFollow.reduce_turn_radii)
        terrainFollow.turn_factor = 3
        Assert.assertEqual(3, terrainFollow.turn_factor)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(terrainFollow, IProcedure))

    # endregion

    # region TransitionToForwardFlight
    @category("Procedure Tests")
    def test_TransitionToForwardFlight(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        toHover: "ProcedureTransitionToHover" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_TRANSITION_TO_HOVER
            ),
            ProcedureTransitionToHover,
        )
        toFlight: "ProcedureTransitionToForwardFlight" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_TRANSITION_TO_FORWARD_FLIGHT
            ),
            ProcedureTransitionToForwardFlight,
        )

        toFlight.set_transition_into_wind()
        Assert.assertEqual(VTOL_TRANSITION_MODE.TRANSITION_INTO_WIND, toFlight.transition_course_mode)

        toFlight.set_absolute_course(5, True)
        Assert.assertEqual(VTOL_TRANSITION_MODE.TRANSITION_ABSOLUTE_HDG, toFlight.transition_course_mode)
        absCourse: typing.Any = toFlight.absolute_course
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertTrue(toFlight.use_magnetic_heading)

        toFlight.set_relative_course(4)
        relCourse: typing.Any = toFlight.relative_course
        Assert.assertAlmostEqual(4, float(relCourse), delta=tolerance)
        Assert.assertEqual(VTOL_TRANSITION_MODE.TRANSITION_RELATIVE_HDG, toFlight.transition_course_mode)

        toFlight.flight_path_angle = 11
        fpa: typing.Any = toFlight.flight_path_angle
        Assert.assertAlmostEqual(11, float(fpa), delta=tolerance)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(toHover, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(toFlight, IProcedure))

    # endregion

    # region TransitionToHover
    @category("Procedure Tests")
    def test_TransitionToHover(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        toHover: "ProcedureTransitionToHover" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_TRANSITION_TO_HOVER
            ),
            ProcedureTransitionToHover,
        )

        toHover.altitude = 600
        Assert.assertEqual(600, toHover.altitude)
        toHover.altitude_reference = AGL_MSL.ALTITUDE_AGL
        Assert.assertEqual(AGL_MSL.ALTITUDE_AGL, toHover.altitude_reference)

        enrouteOpts: "EnrouteOptions" = toHover.enroute_options
        self.EnrouteOptions(enrouteOpts)

        enrouteTurnDirOpts: "EnrouteTurnDirectionOptions" = toHover.enroute_turn_direction_options
        self.EnrouteTurnDirection(enrouteTurnDirOpts)

        verticalPlaneOpts: "VerticalPlaneAndFlightPathOptions" = toHover.vertical_plane_options
        self.VerticalPlaneAndFlightPathOptions(verticalPlaneOpts)

        toHover.set_transition_into_wind()
        Assert.assertTrue(toHover.transition_into_wind)

        toHover.set_transition_course(5, True)
        course: typing.Any = toHover.course
        Assert.assertAlmostEqual(5, float(course), delta=tolerance)
        Assert.assertTrue(toHover.use_magnetic_heading)

        toHover.smooth_transition_mode = TRANSITION_TO_HOVER_MODE.TRANSLATION_ONLY
        Assert.assertEqual(TRANSITION_TO_HOVER_MODE.TRANSLATION_ONLY, toHover.smooth_transition_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(toHover, IProcedure))

    # endregion

    # region VerticalLanding
    @category("Procedure Tests")
    def test_VerticalLanding(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_VTOL_POINT, PROCEDURE_TYPE.PROC_VERTICAL_TAKEOFF
        )
        vertLanding: "ProcedureVerticalLanding" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_VTOL_POINT, PROCEDURE_TYPE.PROC_VERTICAL_LANDING),
            ProcedureVerticalLanding,
        )

        vertLanding.altitude_above_point = 101
        Assert.assertEqual(101, vertLanding.altitude_above_point)
        vertLanding.final_altitude_rate = VTOL_RATE_MODE.ALWAYS_STOP
        Assert.assertEqual(VTOL_RATE_MODE.ALWAYS_STOP, vertLanding.final_altitude_rate)
        vertLanding.altitude_offset = 5
        Assert.assertEqual(5, vertLanding.altitude_offset)

        vertLanding.heading_mode = VERT_LANDING_MODE.VERT_LANDING_INDEPENDENT
        Assert.assertEqual(VERT_LANDING_MODE.VERT_LANDING_INDEPENDENT, vertLanding.heading_mode)
        vertLanding.heading_mode = VERT_LANDING_MODE.VERT_LANDING_ALIGN_TRANSLATION_COURSE_OVERRIDE
        Assert.assertEqual(VERT_LANDING_MODE.VERT_LANDING_ALIGN_TRANSLATION_COURSE_OVERRIDE, vertLanding.heading_mode)

        vertLanding.set_heading(11, False)
        hdg: typing.Any = vertLanding.heading
        Assert.assertAlmostEqual(11, float(hdg), delta=tolerance)
        Assert.assertEqual(False, vertLanding.use_magnetic_heading)

        vertLanding.heading_mode = VERT_LANDING_MODE.VERT_LANDING_ALIGN_TRANSLATION_COURSE
        Assert.assertEqual(VERT_LANDING_MODE.VERT_LANDING_ALIGN_TRANSLATION_COURSE, vertLanding.heading_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            vertLanding.set_heading(11, False)

        vertLanding.heading_mode = VERT_LANDING_MODE.VERT_LANDING_INTO_WIND
        Assert.assertEqual(VERT_LANDING_MODE.VERT_LANDING_INTO_WIND, vertLanding.heading_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            vertLanding.set_heading(11, False)

        vertLanding.radius_factor = 3
        Assert.assertEqual(3, vertLanding.radius_factor)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc1, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(vertLanding, IProcedure))

    # endregion

    # region VerticalTakeoff
    @category("Procedure Tests")
    def test_VerticalTakeoff(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        vertTakeoff: "ProcedureVerticalTakeoff" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_VTOL_POINT, PROCEDURE_TYPE.PROC_VERTICAL_TAKEOFF),
            ProcedureVerticalTakeoff,
        )

        vertTakeoff.altitude_above_point = 101
        Assert.assertEqual(101, vertTakeoff.altitude_above_point)
        vertTakeoff.final_altitude_rate = VTOL_RATE_MODE.ALWAYS_STOP
        Assert.assertEqual(VTOL_RATE_MODE.ALWAYS_STOP, vertTakeoff.final_altitude_rate)
        vertTakeoff.altitude_offset = 5
        Assert.assertEqual(5, vertTakeoff.altitude_offset)

        vertTakeoff.set_heading(11, False)
        hdg: typing.Any = vertTakeoff.heading
        Assert.assertAlmostEqual(11, float(hdg), delta=tolerance)
        Assert.assertEqual(False, vertTakeoff.use_magnetic_heading)
        Assert.assertEqual(False, vertTakeoff.heading_into_wind)

        vertTakeoff.heading_into_wind = True
        Assert.assertTrue(vertTakeoff.heading_into_wind)

        vertTakeoff.hold_on_deck = "00:00:15.000"
        holdTime: typing.Any = vertTakeoff.hold_on_deck
        Assert.assertTrue(("00:00:15.000" == str(holdTime)))

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(vertTakeoff, IProcedure))

    # endregion

    # region VGTPoint
    @category("Procedure Tests")
    def test_VGTPoint(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER
        )
        EarlyBoundTests.AG_AvtrProp.propagate()

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj: "IStkObject" = acObj.copy_object("AC2")
        ac2: "Aircraft" = clr.CastAs(ac2Obj, Aircraft)
        route2: "VehiclePropagatorAviator" = clr.CastAs(ac2.route, VehiclePropagatorAviator)
        prop2: "AviatorPropagator" = clr.CastAs(route2.avtr_propagator, AviatorPropagator)
        mission2: "Mission" = prop2.avtr_mission
        prop2.propagate()

        EarlyBoundTests.AG_Procedures.remove_at_index(1)
        EarlyBoundTests.AG_Procedures.remove_at_index(0)
        vgtProc: "ProcedureVGTPoint" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_STK_VEHICLE, PROCEDURE_TYPE.PROC_VGT_POINT),
            ProcedureVGTPoint,
        )

        self.TestProcedureName(vgtProc.get_as_procedure(), "VGT Point")

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.unit_preferences.set_current_unit("Duration", "Sec")
        vgtProc.start_time = 2
        startTime: typing.Any = vgtProc.start_time
        Assert.assertEqual(2, float(startTime))

        minTime: typing.Any = vgtProc.minimum_time
        maxTime: typing.Any = vgtProc.maximum_time
        Assert.assertEqual(0, float(minTime))

        Assert.assertTrue(("Center" == str(vgtProc.formation_point)))
        vgtProc.formation_point = "AC2 SubPoint(Detic)"
        Assert.assertTrue(("AC2 SubPoint(Detic)" == str(vgtProc.formation_point)))
        vgtProc.interpolate_point_position_vel = True
        Assert.assertTrue(vgtProc.interpolate_point_position_vel)

        vgtProc.duration = 5
        Assert.assertEqual(5, vgtProc.duration)
        vgtProc.use_max_point_stop_time = True
        Assert.assertTrue(vgtProc.use_max_point_stop_time)

        vgtProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_TAKEOFF
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            vgtProc.override_fuel_flow_value = 123
        vgtProc.consider_accel_for_fuel_flow = True
        Assert.assertTrue(vgtProc.consider_accel_for_fuel_flow)

        vgtProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_OVERRIDE
        vgtProc.override_fuel_flow_value = 123
        Assert.assertAlmostEqual(123, vgtProc.override_fuel_flow_value, delta=tolerance)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            vgtProc.consider_accel_for_fuel_flow = True

        vgtProc.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_TAKEOFF
        Assert.assertEqual(PHASE_OF_FLIGHT.FLIGHT_PHASE_TAKEOFF, vgtProc.flight_mode)
        vgtProc.display_step_time = 4
        Assert.assertEqual(4, vgtProc.display_step_time)

        vgtProc.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL
        Assert.assertEqual(vgtProc.flight_mode, PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL)
        vgtProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL
        Assert.assertEqual(vgtProc.fuel_flow_type, FUEL_FLOW_TYPE.FUEL_FLOW_VTOL)
        currentPhase: "Phase" = EarlyBoundTests.AG_Phases[0]
        vtol: "PerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            vgtProc.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            vgtProc.fuel_flow_type = FUEL_FLOW_TYPE.FUEL_FLOW_VTOL

        currentPhase.set_default_perf_models()
        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(vgtProc, IProcedure))
        ac2Obj.unload()

    # endregion

    # region BasicManeuver
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuver(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.use_max_downrange = True
        basicManeuver.max_downrange = 11
        Assert.assertEqual(11, basicManeuver.max_downrange)

        TestBase.Application.unit_preferences.set_current_unit("Duration", "HMS")
        basicManeuver.use_max_time_of_flight = True
        basicManeuver.max_time_of_flight = "00:01:30.000"
        Assert.assertEqual("00:01:30.000", basicManeuver.max_time_of_flight)

        basicManeuver.use_stop_fuel_state = True
        basicManeuver.stop_fuel_state = 1
        Assert.assertEqual(1, basicManeuver.stop_fuel_state)

        basicManeuver.use_max_downrange = False
        basicManeuver.use_max_time_of_flight = False
        basicManeuver.use_stop_fuel_state = True
        with pytest.raises(Exception, match=RegexSubstringMatch("At least one")):
            basicManeuver.use_stop_fuel_state = False

        basicManeuver.terrain_impact_mode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_CONTINUE
        with pytest.raises(Exception, match=RegexSubstringMatch("terrain impact mode")):
            basicManeuver.terrain_impact_time_offset = 1
        basicManeuver.terrain_impact_mode = BASIC_MANEUVER_ALTITUDE_LIMIT.BASIC_MANEUVER_ALTITUDE_LIMIT_ERROR
        with pytest.raises(Exception, match=RegexSubstringMatch("terrain impact mode")):
            basicManeuver.terrain_impact_time_offset = 1

        basicManeuver.fuel_flow_type = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_CRUISE
        with pytest.raises(Exception, match=RegexSubstringMatch("fuel flow source")):
            basicManeuver.override_fuel_flow_value = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("fuel flow source")):
            testVal: bool = basicManeuver.scale_fuel_flow
        with pytest.raises(Exception, match=RegexSubstringMatch("fuel flow source")):
            basicManeuver.scale_fuel_flow = True

        basicManeuver.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL
        Assert.assertEqual(basicManeuver.flight_mode, PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL)
        basicManeuver.fuel_flow_type = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_VTOL
        Assert.assertEqual(basicManeuver.fuel_flow_type, BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_VTOL)
        currentPhase: "Phase" = EarlyBoundTests.AG_Phases[0]
        vtol: "PerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            basicManeuver.flight_mode = PHASE_OF_FLIGHT.FLIGHT_PHASE_VTOL
        with pytest.raises(Exception, match=RegexSubstringMatch("VTOL")):
            basicManeuver.fuel_flow_type = BASIC_MANEUVER_FUEL_FLOW_TYPE.BASIC_MANEUVER_FUEL_FLOW_VTOL

        currentPhase.set_default_perf_models()
        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAileronRoll
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAileronRoll(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Aileron Roll"
        roll: "BasicManeuverStrategyAileronRoll" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyAileronRoll
        )

        roll.flight_path_option = AILERON_ROLL_FLIGHT_PATH.ZERO_G_FLIGHT_PATH
        Assert.assertEqual(AILERON_ROLL_FLIGHT_PATH.ZERO_G_FLIGHT_PATH, roll.flight_path_option)

        Assert.assertEqual("Aileron Roll", basicManeuver.profile_strategy_type)
        rollProfile: "BasicManeuverStrategyAileronRoll" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyAileronRoll
        )
        Assert.assertEqual(AILERON_ROLL_FLIGHT_PATH.ZERO_G_FLIGHT_PATH, rollProfile.flight_path_option)

        roll.active_mode = AILERON_ROLL_MODE.ROLL_TO_ANGLE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            roll.roll_orientation = ROLL_UPRIGHT_INVERTED.ROLL_INVERTED

        roll.active_mode = AILERON_ROLL_MODE.ROLL_TO_ORIENTATION
        roll.roll_orientation = ROLL_UPRIGHT_INVERTED.ROLL_INVERTED
        Assert.assertEqual(ROLL_UPRIGHT_INVERTED.ROLL_INVERTED, roll.roll_orientation)

        roll.roll_rate_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            angle: typing.Any = roll.override_roll_rate
        roll.roll_rate_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        roll.override_roll_rate = 20
        overrideRollRate: typing.Any = roll.override_roll_rate
        Assert.assertEqual(20, float(overrideRollRate))

        airspeedOpts: "BasicManeuverAirspeedOptions" = roll.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAutopilotNav
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAutopilotNav(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Autopilot - Horizontal Plane"
        autopilot: "BasicManeuverStrategyAutopilotNav" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyAutopilotNav
        )

        mode: "AUTOPILOT_HORIZ_PLANE_MODE"

        for mode in Enum.GetValues(clr.TypeOf(AUTOPILOT_HORIZ_PLANE_MODE)):
            autopilot.active_mode = mode
            autopilot.stop_when_conditions_met = False
            Assert.assertFalse(autopilot.stop_when_conditions_met)

            autopilot.stop_when_conditions_met = True
            Assert.assertTrue(autopilot.stop_when_conditions_met)

            autopilot.active_heading_course_value = 10
            Assert.assertEqual(10, autopilot.active_heading_course_value)

        autopilot.active_mode = AUTOPILOT_HORIZ_PLANE_MODE.AUTOPILOT_COURSE_RATE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            autopilot.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS, 1000)

        autopilot.active_mode = AUTOPILOT_HORIZ_PLANE_MODE.AUTOPILOT_HEADING_RATE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            autopilot.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS, 1000)

        autopilot.compensate_for_coriolis_accel = True
        Assert.assertTrue(autopilot.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAutopilotProfile
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAutopilotProfile(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Autopilot - Vertical Plane"
        autopilot: "BasicManeuverStrategyAutopilotProf" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyAutopilotProf
        )
        autopilot.altitude_mode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_HOLD_INIT_ALTITUDE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: float = autopilot.absolute_altitude
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: float = autopilot.relative_altitude_change
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: float = autopilot.altitude_rate
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: typing.Any = autopilot.fpa

        autopilot.altitude_control_mode = AUTOPILOT_ALTITUDE_CONTROL_MODE.AUTOPILOT_ALTITUDE_RATE
        autopilot.control_altitude_rate_value = 2001
        Assert.assertEqual(2001, autopilot.control_altitude_rate_value)

        autopilot.altitude_control_mode = AUTOPILOT_ALTITUDE_CONTROL_MODE.AUTOPILOT_FPA
        autopilot.control_fpa_value = 11
        controlFPA: typing.Any = autopilot.control_fpa_value
        Assert.assertEqual(11, controlFPA)

        autopilot.altitude_control_mode = AUTOPILOT_ALTITUDE_CONTROL_MODE.AUTOPILOT_PERF_MODELS
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: float = autopilot.control_altitude_rate_value
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: typing.Any = autopilot.control_fpa_value

        autopilot.control_limit_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        autopilot.max_pitch_rate = 11
        pitchRate: typing.Any = autopilot.max_pitch_rate
        Assert.assertEqual(11, pitchRate)
        autopilot.control_limit_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            autopilot.max_pitch_rate = 11

        autopilot.damping_ratio = 1.5
        Assert.assertEqual(1.5, autopilot.damping_ratio)

        autopilot.altitude_mode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_SPECIFY_ALTITUDE
        autopilot.absolute_altitude = 10001
        Assert.assertEqual(10001, autopilot.absolute_altitude)

        autopilot.altitude_mode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_SPECIFY_ALTITUDE_CHANGE
        autopilot.relative_altitude_change = 1
        Assert.assertEqual(1, autopilot.relative_altitude_change)

        autopilot.altitude_mode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_SPECIFY_ALTITUDE_RATE
        autopilot.altitude_rate = 1
        Assert.assertEqual(1, autopilot.altitude_rate)

        autopilot.altitude_mode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_SPECIFY_FPA
        autopilot.fpa = 1
        fpa: typing.Any = autopilot.fpa
        Assert.assertEqual(1, fpa)

        autopilot.altitude_mode = AUTOPILOT_ALTITUDE_MODE.AUTOPILOT_BALLISTIC
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            autopilot.altitude_control_mode = AUTOPILOT_ALTITUDE_CONTROL_MODE.AUTOPILOT_FPA
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            autopilot.damping_ratio = 1.5

        airspeedOpts: "BasicManeuverAirspeedOptions" = autopilot.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        autopilot.compensate_for_coriolis_accel = True
        Assert.assertTrue(autopilot.compensate_for_coriolis_accel)

        mode: "AUTOPILOT_ALTITUDE_MODE"

        for mode in Enum.GetValues(clr.TypeOf(AUTOPILOT_ALTITUDE_MODE)):
            autopilot.altitude_mode = mode
            autopilot.stop_when_conditions_met = False
            Assert.assertFalse(autopilot.stop_when_conditions_met)

            autopilot.stop_when_conditions_met = True
            Assert.assertTrue(autopilot.stop_when_conditions_met)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverBallistic3D
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverBallistic3D(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Ballistic3D"
        ballistic: "BasicManeuverStrategyBallistic3D" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyBallistic3D
        )

        ballistic.control_mode = BALLISTIC_3D_CONTROL_MODE.BALLISTIC_3D_COMPENSATE_FOR_WIND
        Assert.assertEqual(BALLISTIC_3D_CONTROL_MODE.BALLISTIC_3D_COMPENSATE_FOR_WIND, ballistic.control_mode)

        self.BasicManeuverAirspeedOptions(ballistic.airspeed_options)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            ballistic.wind_force_effective_area = 10

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            ballistic.parachute_area = 5
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            ballistic.parachute_cd = 1.5

        ballistic.control_mode = BALLISTIC_3D_CONTROL_MODE.BALLISTIC_3D_WIND_PUSHES_VEHICLE
        Assert.assertEqual(BALLISTIC_3D_CONTROL_MODE.BALLISTIC_3D_WIND_PUSHES_VEHICLE, ballistic.control_mode)

        self.BasicManeuverAirspeedOptions(ballistic.airspeed_options)

        ballistic.wind_force_effective_area = 10
        Assert.assertEqual(10, ballistic.wind_force_effective_area)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            ballistic.parachute_area = 5
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            ballistic.parachute_cd = 1.5

        ballistic.control_mode = BALLISTIC_3D_CONTROL_MODE.BALLISTIC_3D_PARACHUTE_MODE
        Assert.assertEqual(BALLISTIC_3D_CONTROL_MODE.BALLISTIC_3D_PARACHUTE_MODE, ballistic.control_mode)

        ballistic.parachute_area = 5
        Assert.assertEqual(5, ballistic.parachute_area)
        ballistic.parachute_cd = 1.5
        Assert.assertEqual(1.5, ballistic.parachute_cd)

        ballistic.wind_force_effective_area = 11
        Assert.assertEqual(11, ballistic.wind_force_effective_area)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            self.BasicManeuverAirspeedOptions(ballistic.airspeed_options)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverBarrelRoll
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverBarrelRoll(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Barrel Roll"
        roll: "BasicManeuverStrategyBarrelRoll" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategyBarrelRoll)
        roll.helix_angle = 359
        helixAngle: typing.Any = roll.helix_angle
        roll.helix_angle_mode = ANGLE_MODE.RELATIVE_ANGLE
        Assert.assertEqual(359, float(helixAngle))
        Assert.assertEqual(ANGLE_MODE.RELATIVE_ANGLE, roll.helix_angle_mode)

        Assert.assertEqual("Barrel Roll", basicManeuver.profile_strategy_type)
        rollProfile: "BasicManeuverStrategyBarrelRoll" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyBarrelRoll
        )
        helixAngleProfile: typing.Any = rollProfile.helix_angle
        Assert.assertEqual(359, float(helixAngleProfile))
        Assert.assertEqual(ANGLE_MODE.RELATIVE_ANGLE, rollProfile.helix_angle_mode)

        roll.hold_init_tas = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            roll.set_airspeeds(AIRSPEED_TYPE.MACH, 0.1, 0.2)

        roll.hold_init_tas = False
        roll.set_airspeeds(AIRSPEED_TYPE.MACH, 0.1, 0.2)
        Assert.assertEqual(0.1, roll.top_airspeed)
        Assert.assertEqual(0.2, roll.bottom_airspeed)

        roll.set_airspeeds(AIRSPEED_TYPE.TAS, 200, 201)
        Assert.assertEqual(200, roll.top_airspeed)
        Assert.assertEqual(201, roll.bottom_airspeed)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverBezier
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverBezier(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Profile Segment - Bezier"
        bezier: "BasicManeuverStrategyBezier" = clr.CastAs(basicManeuver.profile, BasicManeuverStrategyBezier)

        bezier.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.WIND_FRAME
        Assert.assertEqual(BASIC_MANEUVER_REFERENCE_FRAME.WIND_FRAME, bezier.reference_frame)

        bezier.downrange = 11
        Assert.assertEqual(11, bezier.downrange)
        bezier.altitude = 10000
        Assert.assertEqual(10000, bezier.altitude)
        bezier.set_airspeed(AIRSPEED_TYPE.TAS, 250)
        Assert.assertEqual(250, bezier.airspeed)
        bezier.set_airspeed(AIRSPEED_TYPE.MACH, 0.2)
        Assert.assertEqual(0.2, bezier.airspeed)

        bezier.set_vertical_velocity(FLY_TO_FLIGHT_PATH_ANGLE_MODE.FLY_TO_ALTITUDE_RATE, 1000)
        Assert.assertAlmostEqual(1000, bezier.altitude_rate, delta=tolerance)
        bezier.set_vertical_velocity(FLY_TO_FLIGHT_PATH_ANGLE_MODE.FLY_TO_FLIGHT_PATH_ANGLE, 3)
        angle: typing.Any = bezier.flight_path_angle
        Assert.assertEqual(3, float(angle))

        bezier.set_stop_airspeed(True, AIRSPEED_TYPE.TAS, 260)
        Assert.assertTrue(bezier.use_stop_at_airspeed)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, bezier.stop_airspeed_type)
        Assert.assertEqual(260, bezier.stop_airspeed)

        bezier.set_stop_airspeed(False, AIRSPEED_TYPE.MACH, 0.2)
        Assert.assertEqual(False, bezier.use_stop_at_airspeed)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, bezier.stop_airspeed_type)
        Assert.assertEqual(0.2, bezier.stop_airspeed)

        bezier.set_stop_altitude_rate(True, 5)
        Assert.assertEqual(5, bezier.stop_altitude_rate)

        bezier.compensate_for_coriolis_accel = True
        Assert.assertTrue(bezier.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverCruise
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverCruise(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Cruise Profile"
        cruise: "BasicManeuverStrategyCruiseProfile" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyCruiseProfile
        )

        cruise.use_default_cruise_altitude = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            levelOff: bool = cruise.level_off
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            cruise.level_off = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            cruise.requested_altitude = 10000

        cruise.use_default_cruise_altitude = False
        cruise.level_off = True
        Assert.assertTrue(cruise.level_off)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            cruise.requested_altitude = 10000

        cruise.level_off = False
        cruise.requested_altitude = 10000
        Assert.assertEqual(10000, cruise.requested_altitude)

        self.EnrouteCruiseAirspeed(cruise.cruise_airspeed_options)

        cruise.compensate_for_coriolis_accel = True
        Assert.assertTrue(cruise.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverFlyAOA
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverFlyAOA(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Fly AOA"
        flyAOA: "BasicManeuverStrategyFlyAOA" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategyFlyAOA)

        flyAOA.aoa = 11
        aoa: typing.Any = flyAOA.aoa
        Assert.assertEqual(11, float(aoa))

        Assert.assertEqual("Fly AOA", basicManeuver.profile_strategy_type)
        flyAOAProfile: "BasicManeuverStrategyFlyAOA" = clr.CastAs(basicManeuver.profile, BasicManeuverStrategyFlyAOA)
        aoaProfile: typing.Any = flyAOAProfile.aoa
        Assert.assertEqual(11, float(aoaProfile))

        flyAOA.turn_direction = FLY_AOA_LEFT_RIGHT.FLY_AOA_LEFT
        flyAOA.control_roll_angle = False
        flyAOA.roll_rate_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            value: typing.Any = flyAOA.override_roll_rate
        flyAOA.roll_rate_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        flyAOA.override_roll_rate = 29
        rate: typing.Any = flyAOA.override_roll_rate
        Assert.assertAlmostEqual(29, float(rate), delta=tolerance)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flyAOA.roll_angle = 59
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flyAOA.stop_on_roll_angle = True
        flyAOA.control_roll_angle = True
        flyAOA.roll_angle = 59
        angle: typing.Any = flyAOA.roll_angle
        Assert.assertAlmostEqual(59, float(angle), delta=tolerance)
        flyAOA.stop_on_roll_angle = True
        Assert.assertTrue(flyAOA.stop_on_roll_angle)

        flyAOA.turn_direction = FLY_AOA_LEFT_RIGHT.FLY_AOA_NO_ROLL
        flyAOA.stop_on_roll_angle = False
        Assert.assertFalse(flyAOA.stop_on_roll_angle)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flyAOA.roll_rate_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flyAOA.override_roll_rate = 29
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flyAOA.control_roll_angle = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            flyAOA.roll_angle = 59

        airspeedOpts: "BasicManeuverAirspeedOptions" = flyAOA.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverGlide
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverGlide(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Glide - Vertical Plane"
        glide: "BasicManeuverStrategyGlideProfile" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyGlideProfile
        )

        glide.hold_initial_airspeed = True
        Assert.assertTrue(glide.hold_initial_airspeed)

        with pytest.raises(Exception, match=RegexSubstringMatch("Hold Initial Airspeed must be disabled")):
            glide.set_airspeed(AIRSPEED_TYPE.MACH, 0.5)

        glide.set_glide_speed_control_mode(
            BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE.GLIDE_SPEED_AT_ALTITUDE, 2000
        )  # BUG - this should throw an exception, but does not, and does not change values in the GUI.
        # TryCatchAssertBlock.ExpectedException("Hold Initial Airspeed must be disabled", delegate () { glide.SetGlideSpeedControlMode(BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE.GLIDE_SPEED_AT_ALTITUDE, 2000); });

        glide.hold_initial_airspeed = False
        Assert.assertFalse(glide.hold_initial_airspeed)

        glide.set_airspeed(AIRSPEED_TYPE.MACH, 0.5)
        Assert.assertAlmostEqual(0.5, glide.airspeed, delta=1e-06)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, glide.airspeed_type)

        glide.set_airspeed(AIRSPEED_TYPE.CAS, 0.6)
        Assert.assertAlmostEqual(0.6, glide.airspeed, delta=1e-06)
        Assert.assertEqual(AIRSPEED_TYPE.CAS, glide.airspeed_type)

        glide.set_airspeed(AIRSPEED_TYPE.EAS, 0.7)
        Assert.assertAlmostEqual(0.7, glide.airspeed, delta=1e-06)
        Assert.assertEqual(AIRSPEED_TYPE.EAS, glide.airspeed_type)

        glide.set_airspeed(AIRSPEED_TYPE.TAS, 0.8)
        Assert.assertAlmostEqual(0.8, glide.airspeed, delta=1e-06)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, glide.airspeed_type)

        glide.set_glide_speed_control_mode(BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE.GLIDE_SPEED_IMMEDIATE_CHANGE, 1000)
        Assert.assertEqual(
            BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE.GLIDE_SPEED_IMMEDIATE_CHANGE, glide.glide_speed_control_mode
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("speed control mode must be")):
            x: float = glide.glide_speed_control_altitude

        glide.set_glide_speed_control_mode(BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE.GLIDE_SPEED_AT_ALTITUDE, 2000)
        Assert.assertEqual(
            BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE.GLIDE_SPEED_AT_ALTITUDE, glide.glide_speed_control_mode
        )
        Assert.assertEqual(2000, glide.glide_speed_control_altitude)

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            glide.set_glide_speed_control_mode(BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE.GLIDE_SPEED_AT_ALTITUDE, -1000)

        glide.min_g = 0.6
        Assert.assertEqual(0.6, glide.min_g)

        glide.max_g = 1.6
        Assert.assertEqual(1.6, glide.max_g)

        glide.max_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
        Assert.assertEqual(BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED, glide.max_speed_limits)
        glide.max_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.STOP_IF_VIOLATED
        Assert.assertEqual(BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.STOP_IF_VIOLATED, glide.max_speed_limits)
        glide.max_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.ERROR_IF_VIOLATED
        Assert.assertEqual(BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.ERROR_IF_VIOLATED, glide.max_speed_limits)
        glide.max_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.IGNORE_IF_VIOLATED
        Assert.assertEqual(BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.IGNORE_IF_VIOLATED, glide.max_speed_limits)

        glide.compensate_for_coriolis_accel = False
        Assert.assertFalse(glide.compensate_for_coriolis_accel)
        glide.compensate_for_coriolis_accel = True
        Assert.assertTrue(glide.compensate_for_coriolis_accel)

        glide.powered_cruise_mode = BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE.GLIDE_SPECIFY_UN_POWERED_CRUISE
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE.GLIDE_SPECIFY_UN_POWERED_CRUISE, glide.powered_cruise_mode
        )

        glide.powered_cruise_throttle = 20.0
        thrust1: "PropulsionThrust" = glide.powered_cruise_thrust_model
        # BUG120578 TryCatchAssertBlock.ExpectedException("read only", delegate () { glide.PoweredCruiseThrottle = 20.0; });
        # BUG120578 TryCatchAssertBlock.ExpectedException("read only", delegate () { PropulsionThrust thrust1 = glide.PoweredCruiseThrustModel; });

        glide.powered_cruise_mode = BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE.GLIDE_SPECIFY_THROTTLE
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE.GLIDE_SPECIFY_THROTTLE, glide.powered_cruise_mode
        )

        glide.powered_cruise_throttle = 30.0
        Assert.assertEqual(30.0, glide.powered_cruise_throttle)

        self.Test_IAgAvtrPropulsionThrust(glide.powered_cruise_thrust_model)
        # BUG120578 TryCatchAssertBlock.ExpectedException("read only", delegate () { Test_IAgAvtrPropulsionThrust( glide.PoweredCruiseThrustModel); });

        glide.powered_cruise_mode = BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE.GLIDE_SPECIFY_THRUST_MODEL
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE.GLIDE_SPECIFY_THRUST_MODEL, glide.powered_cruise_mode
        )

        glide.powered_cruise_throttle = 20.0
        # BUG120578 TryCatchAssertBlock.ExpectedException("read only", delegate () { glide.PoweredCruiseThrottle = 20.0; });

        self.Test_IAgAvtrPropulsionThrust(glide.powered_cruise_thrust_model)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region Test_IAgAvtrPropulsionThrust
    def Test_IAgAvtrPropulsionThrust(self, thrust: "PropulsionThrust"):
        thrust.use_constant_thrust = True
        Assert.assertTrue(thrust.use_constant_thrust)

        thrust.constant_thrust = 111
        Assert.assertEqual(111, thrust.constant_thrust)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
            thrust.boost_thrust = 999
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
            thrust.boost_thrust_time_limit = 999
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
            thrust.sustain_thrust = 999
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
            thrust.sustain_thrust_time_limit = 999

        thrust.use_constant_thrust = False
        Assert.assertFalse(thrust.use_constant_thrust)

        thrust.boost_thrust = 222
        Assert.assertEqual(222, thrust.boost_thrust)
        thrust.boost_thrust_time_limit = 333
        Assert.assertEqual(333, thrust.boost_thrust_time_limit)

        thrust.sustain_thrust = 444
        Assert.assertEqual(444, thrust.sustain_thrust)
        thrust.sustain_thrust_time_limit = 555
        Assert.assertEqual(555, thrust.sustain_thrust_time_limit)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
            thrust.constant_thrust = 999

        thrust.set_min_airspeed(AIRSPEED_TYPE.MACH, 666)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, thrust.min_airspeed_type)
        Assert.assertAlmostEqual(666, thrust.min_airspeed, delta=1e-06)
        thrust.set_min_airspeed(AIRSPEED_TYPE.EAS, 777)
        Assert.assertEqual(AIRSPEED_TYPE.EAS, thrust.min_airspeed_type)
        Assert.assertAlmostEqual(777, thrust.min_airspeed, delta=1e-06)

        thrust.set_max_airspeed(AIRSPEED_TYPE.CAS, 888)
        Assert.assertEqual(AIRSPEED_TYPE.CAS, thrust.max_airspeed_type)
        Assert.assertAlmostEqual(888, thrust.max_airspeed, delta=1e-06)
        thrust.set_max_airspeed(AIRSPEED_TYPE.TAS, 999)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, thrust.max_airspeed_type)
        Assert.assertAlmostEqual(999, thrust.max_airspeed, delta=1e-06)

    # endregion

    # region BasicManeuverIntercept
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverIntercept(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Intercept"
        intercept: "BasicManeuverStrategyIntercept" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyIntercept
        )

        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        with pytest.raises(Exception, match=RegexSubstringMatch("not a valid")):
            intercept.target_name = targetName
        missile: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile")), Missile
        )
        traj: "VehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, VehiclePropagatorBallistic)
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, VehicleImpactLocationPoint)
        impact: "VehicleImpactLLA" = clr.CastAs(impactLocation.impact, VehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()
        intercept.target_name = "Missile/Missile"

        intercept.target_resolution = 0.7
        Assert.assertEqual(0.7, intercept.target_resolution)

        intercept.set_stop_slant_range(True, 2)
        Assert.assertTrue(intercept.use_stop_slant_range)
        Assert.assertEqual(2, intercept.stop_slant_range)

        intercept.set_stop_time_to_go(True, 11)
        Assert.assertTrue(intercept.use_stop_time_to_go)
        Assert.assertEqual(11, intercept.stop_time_to_go)

        intercept.intercept_mode = INTERCEPT_MODE.TARGET_ASPECT
        intercept.target_aspect = 0.1
        aspect: typing.Any = intercept.target_aspect
        Assert.assertEqual(0.1, float(aspect))
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            intercept.lateral_separation = 2

        intercept.intercept_mode = INTERCEPT_MODE.LATERAL_SEPARATION
        intercept.lateral_separation = 2
        Assert.assertEqual(2, intercept.lateral_separation)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            intercept.target_aspect = 2

        intercept.maneuver_factor = 0.6
        Assert.assertEqual(0.6, intercept.maneuver_factor)

        intercept.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL, 0)
        Assert.assertEqual(
            intercept.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL
        )
        intercept.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL, 0.1)
        Assert.assertEqual(intercept.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL)
        Assert.assertAlmostEqual(0.1, intercept.control_limit_horiz_accel, delta=tolerance)
        intercept.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE, 0.2)
        Assert.assertEqual(intercept.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE)
        Assert.assertAlmostEqual(0.2, float(intercept.control_limit_turn_rate), delta=tolerance)
        intercept.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS, 700)
        Assert.assertEqual(intercept.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS)
        Assert.assertEqual(700, intercept.control_limit_turn_radius)

        intercept.closure_mode = CLOSURE_MODE.CLOSURE_NOT_SET
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            intercept.hobs_angle_tol = 2
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            intercept.hobs_max_angle = 5

        intercept.closure_mode = CLOSURE_MODE.HOBS
        intercept.hobs_angle_tol = 2
        intercept.hobs_max_angle = 5
        angleTol: typing.Any = intercept.hobs_angle_tol
        Assert.assertEqual(2, float(angleTol))
        maxAngle: typing.Any = intercept.hobs_max_angle
        Assert.assertEqual(5, float(maxAngle))

        intercept.compensate_for_coriolis_accel = True
        Assert.assertTrue(intercept.compensate_for_coriolis_accel)

        self.Test_IAgAvtrBasicManeuverTargetPosVel(intercept.position_vel_strategies)

        missileObj: "IStkObject" = clr.CastAs(missile, IStkObject)
        missileObj.unload()
        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverLoop
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverLoop(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Loop"
        loop: "BasicManeuverStrategyLoop" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategyLoop)
        loop.loop_angle = 359
        loopAngle: typing.Any = loop.loop_angle
        loop.loop_angle_mode = ANGLE_MODE.RELATIVE_ANGLE
        Assert.assertEqual(359, float(loopAngle))
        Assert.assertEqual(ANGLE_MODE.RELATIVE_ANGLE, loop.loop_angle_mode)

        Assert.assertEqual("Loop", basicManeuver.profile_strategy_type)
        loopProfile: "BasicManeuverStrategyLoop" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategyLoop)
        loopAngleProfile: typing.Any = loopProfile.loop_angle
        Assert.assertEqual(359, float(loopAngleProfile))
        Assert.assertEqual(ANGLE_MODE.RELATIVE_ANGLE, loopProfile.loop_angle_mode)

        loop.hold_init_tas = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            loop.set_airspeeds(AIRSPEED_TYPE.MACH, 0.1, 0.2)

        loop.hold_init_tas = False
        loop.set_airspeeds(AIRSPEED_TYPE.MACH, 0.1, 0.2)
        Assert.assertEqual(0.1, loop.top_airspeed)
        Assert.assertEqual(0.2, loop.bottom_airspeed)

        loop.set_airspeeds(AIRSPEED_TYPE.TAS, 200, 201)
        Assert.assertEqual(200, loop.top_airspeed)
        Assert.assertEqual(201, loop.bottom_airspeed)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverLTAHover
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverLTAHover(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Lighter Than Air Hover"
        hover: "BasicManeuverStrategyLTAHover" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategyLTAHover)
        hover.heading_rate = 1.5
        headingRate: typing.Any = hover.heading_rate
        Assert.assertEqual(1.5, float(headingRate))

        Assert.assertEqual("Lighter Than Air Hover", basicManeuver.profile_strategy_type)
        hoverProfile: "BasicManeuverStrategyLTAHover" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyLTAHover
        )
        headingRateProfile: typing.Any = hoverProfile.heading_rate
        Assert.assertEqual(1.5, float(headingRateProfile))

        hover.heading_mode = HOVER_HEADING_MODE.HOVER_INTO_WIND
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.absolute_heading = 1.1
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.use_magnetic_heading = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.relative_heading = 2.2

        hover.heading_mode = HOVER_HEADING_MODE.HOVER_ABSOLUTE
        hover.absolute_heading = 1.1
        absHdg: typing.Any = hover.absolute_heading
        Assert.assertEqual(1.1, float(absHdg))
        hover.use_magnetic_heading = True
        Assert.assertTrue(hover.use_magnetic_heading)

        hover.heading_mode = HOVER_HEADING_MODE.HOVER_RELATIVE
        hover.relative_heading = 2.2
        relHdg: typing.Any = hover.relative_heading
        Assert.assertEqual(2.2, float(relHdg))

        hover.altitude_mode = HOVER_ALTITUDE_MODE.HOVER_HOLD_INIT_ALTITUDE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            test: float = hover.absolute_altitude
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.absolute_altitude = 10001
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            test: float = hover.altitude_rate
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.altitude_rate = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            test: float = hover.control_altitude_rate
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.control_altitude_rate = 501
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            test: float = hover.relative_altitude_change
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.relative_altitude_change = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            test: float = hover.parachute_area
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.parachute_area = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            test: float = hover.parachute_cd
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            hover.parachute_cd = 1

        hover.altitude_mode = HOVER_ALTITUDE_MODE.HOVER_SPECIFY_ALTITUDE
        hover.absolute_altitude = 10001
        Assert.assertEqual(10001, hover.absolute_altitude)
        hover.control_altitude_rate = 501
        Assert.assertEqual(501, hover.control_altitude_rate)

        hover.altitude_mode = HOVER_ALTITUDE_MODE.HOVER_SPECIFY_ALTITUDE_CHANGE
        hover.relative_altitude_change = 1
        Assert.assertEqual(1, hover.relative_altitude_change)
        hover.control_altitude_rate = 501
        Assert.assertEqual(501, hover.control_altitude_rate)

        hover.altitude_mode = HOVER_ALTITUDE_MODE.HOVER_SPECIFY_ALTITUDE_RATE
        hover.altitude_rate = 501
        Assert.assertEqual(501, hover.altitude_rate)

        hover.altitude_mode = HOVER_ALTITUDE_MODE.HOVER_PARACHUTE
        hover.parachute_area = 10
        Assert.assertEqual(10, hover.parachute_area)
        hover.parachute_cd = 1.1
        Assert.assertEqual(1.1, hover.parachute_cd)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverPitch3D
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverPitch3D(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Pitch3D"
        pitch3D: "BasicManeuverStrategyPitch3D" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategyPitch3D)

        pitch3D.control_mode = PITCH_3D_CONTROL_MODE.PITCH_3D_WIND_PUSHES_VEHICLE
        Assert.assertEqual(PITCH_3D_CONTROL_MODE.PITCH_3D_WIND_PUSHES_VEHICLE, pitch3D.control_mode)

        pitch3D.command_fpa = 59
        fpa: typing.Any = pitch3D.command_fpa
        Assert.assertAlmostEqual(59, float(fpa), delta=tolerance)

        pitch3D.control_fpa_dot = 2
        fpaDot: typing.Any = pitch3D.control_fpa_dot
        Assert.assertEqual(2, float(fpaDot))

        pitch3D.stop_when_fpa_achieved = False
        Assert.assertEqual(False, pitch3D.stop_when_fpa_achieved)

        self.BasicManeuverAirspeedOptions(pitch3D.airspeed_options)

        pitch3D.wind_force_effective_area = 11
        Assert.assertEqual(11, pitch3D.wind_force_effective_area)

        pitch3D.control_mode = PITCH_3D_CONTROL_MODE.PITCH_3D_COMPENSATE_FOR_WIND
        Assert.assertEqual(PITCH_3D_CONTROL_MODE.PITCH_3D_COMPENSATE_FOR_WIND, pitch3D.control_mode)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            pitch3D.wind_force_effective_area = 10

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverPull
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverPull(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Pull"
        pull: "BasicManeuverStrategyPull" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategyPull)

        pull.active_mode = PULL_MODE.PULL_TO_ANGLE
        pull.active_angle = 59
        angle: typing.Any = pull.active_angle
        Assert.assertAlmostEqual(59, float(angle), delta=tolerance)

        Assert.assertEqual("Pull", basicManeuver.profile_strategy_type)
        pullProfile: "BasicManeuverStrategyPull" = clr.CastAs(basicManeuver.profile, BasicManeuverStrategyPull)
        angleProfile: typing.Any = pullProfile.active_angle
        Assert.assertAlmostEqual(59, float(angleProfile), delta=tolerance)

        pull.pull_g_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            pull.override_pull_g = 2
        pull.pull_g_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        pull.override_pull_g = 2
        Assert.assertEqual(2, pull.override_pull_g)

        airspeedOpts: "BasicManeuverAirspeedOptions" = pull.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverPushPull
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverPushPull(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Profile Segment - Push/Pull"
        pushPull: "BasicManeuverStrategyPushPull" = clr.CastAs(basicManeuver.profile, BasicManeuverStrategyPushPull)

        pushPull.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.WIND_FRAME
        Assert.assertEqual(BASIC_MANEUVER_REFERENCE_FRAME.WIND_FRAME, pushPull.reference_frame)

        pushPull.push_pull = PUSH_PULL.PUSH_OVER
        pushPull.push_pull_g = 0.99
        Assert.assertEqual(0.99, pushPull.push_pull_g)

        pushPull.accel_mode = ACCEL_MODE.ACCEL
        pushPull.accel_decel_g = 0.98
        Assert.assertEqual(0.98, pushPull.accel_decel_g)

        pushPull.stop_flight_path_angle = 5
        fpa: typing.Any = pushPull.stop_flight_path_angle
        Assert.assertEqual(5, float(fpa))

        pushPull.set_stop_airspeed(True, AIRSPEED_TYPE.TAS, 250)
        Assert.assertTrue(pushPull.use_stop_at_airspeed)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, pushPull.stop_airspeed_type)
        Assert.assertEqual(250, pushPull.stop_airspeed)

        pushPull.set_stop_airspeed(False, AIRSPEED_TYPE.MACH, 0.2)
        Assert.assertEqual(False, pushPull.use_stop_at_airspeed)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, pushPull.stop_airspeed_type)
        Assert.assertEqual(0.2, pushPull.stop_airspeed)

        pushPull.set_stop_altitude(True, 100)
        Assert.assertEqual(100, pushPull.stop_altitude)

        pushPull.set_stop_altitude_rate(True, 0.1)
        Assert.assertAlmostEqual(0.1, pushPull.stop_altitude_rate, delta=tolerance)

        pushPull.compensate_for_coriolis_accel = True
        Assert.assertTrue(pushPull.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRelativeBearing
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRelativeBearing(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Relative Bearing"
        relBearing: "BasicManeuverStrategyRelativeBearing" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyRelativeBearing
        )

        validTargets = relBearing.valid_target_names
        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relBearing.target_name = targetName
        Assert.assertEqual(targetName, relBearing.target_name)

        relBearing.target_resolution = 0.7
        Assert.assertEqual(0.7, relBearing.target_resolution)

        relBearing.rel_bearing = 1
        bearing: typing.Any = relBearing.rel_bearing
        Assert.assertEqual(1, float(bearing))
        relBearing.min_range = 0.5
        Assert.assertEqual(0.5, relBearing.min_range)

        relBearing.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL, 0)
        Assert.assertEqual(
            relBearing.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL
        )
        relBearing.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL, 0.1)
        Assert.assertEqual(relBearing.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL)
        Assert.assertAlmostEqual(0.1, relBearing.control_limit_horiz_accel, delta=tolerance)
        relBearing.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE, 0.2)
        Assert.assertEqual(relBearing.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE)
        Assert.assertAlmostEqual(0.2, float(relBearing.control_limit_turn_rate), delta=tolerance)
        relBearing.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS, 700)
        Assert.assertEqual(relBearing.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS)
        Assert.assertEqual(700, relBearing.control_limit_turn_radius)

        relBearing.compensate_for_coriolis_accel = True
        Assert.assertTrue(relBearing.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRelativeCourse
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRelativeCourse(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Relative Course"
        relCourse: "BasicManeuverStrategyRelativeCourse" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyRelativeCourse
        )

        validTargets = relCourse.valid_target_names
        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relCourse.target_name = targetName
        Assert.assertEqual(targetName, relCourse.target_name)

        relCourse.target_resolution = 0.7
        Assert.assertEqual(0.7, relCourse.target_resolution)

        relCourse.course = 1
        course: typing.Any = relCourse.course
        Assert.assertEqual(1, float(course))
        relCourse.use_relative_course = True
        Assert.assertTrue(relCourse.use_relative_course)

        relCourse.in_track = 1
        Assert.assertEqual(1, relCourse.in_track)
        relCourse.cross_track = 2
        Assert.assertEqual(2, relCourse.cross_track)

        relCourse.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL, 0)
        Assert.assertEqual(
            relCourse.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL
        )
        relCourse.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL, 0.1)
        Assert.assertEqual(relCourse.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL)
        Assert.assertAlmostEqual(0.1, relCourse.control_limit_horiz_accel, delta=tolerance)
        relCourse.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE, 0.2)
        Assert.assertEqual(relCourse.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE)
        Assert.assertAlmostEqual(0.2, float(relCourse.control_limit_turn_rate), delta=tolerance)
        relCourse.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS, 700)
        Assert.assertEqual(relCourse.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS)
        Assert.assertEqual(700, relCourse.control_limit_turn_radius)

        relCourse.closure_mode = CLOSURE_MODE.CLOSURE_NOT_SET
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            relCourse.downrange_offset = 0.5
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            relCourse.hobs_max_angle = 89
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            relCourse.hobs_angle_tol = 4

        relCourse.closure_mode = CLOSURE_MODE.CLOSURE_REQUIRED
        relCourse.downrange_offset = 0.5
        Assert.assertEqual(0.5, relCourse.downrange_offset)

        relCourse.closure_mode = CLOSURE_MODE.HOBS
        relCourse.hobs_max_angle = 89
        angleMax: typing.Any = relCourse.hobs_max_angle
        Assert.assertEqual(89, float(angleMax))
        relCourse.hobs_angle_tol = 4
        angleTol: typing.Any = relCourse.hobs_angle_tol
        Assert.assertEqual(4, float(angleTol))

        relCourse.compensate_for_coriolis_accel = True
        Assert.assertTrue(relCourse.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRelativeFPA
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRelativeFPA(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Relative Course"
        relCourse: "BasicManeuverStrategyRelativeCourse" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyRelativeCourse
        )

        validTargets = relCourse.valid_target_names
        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relCourse.target_name = targetName
        Assert.assertEqual(targetName, relCourse.target_name)

        basicManeuver.profile_strategy_type = "Relative Flight Path Angle"
        relativeFPA: "BasicManeuverStrategyRelativeFPA" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyRelativeFPA
        )

        relativeFPA.fpa = 5
        fpa: typing.Any = relativeFPA.fpa
        Assert.assertEqual(5, float(fpa))
        relativeFPA.anchor_altitude_offset = 100
        Assert.assertEqual(100, relativeFPA.anchor_altitude_offset)

        relativeFPA.maneuver_factor = 0.7
        Assert.assertEqual(0.7, relativeFPA.maneuver_factor)

        relativeFPA.set_control_limit(PROFILE_CONTROL_LIMIT.PROFILE_PITCH_RATE, 5)
        pitchRate: typing.Any = relativeFPA.control_limit_pitch_rate
        Assert.assertEqual(5, float(pitchRate))

        relativeFPA.set_min_absolute_altitude(True, 2)
        Assert.assertEqual(2, relativeFPA.min_absolute_altitude)

        relativeFPA.set_max_absolute_altitude(True, 10000)
        Assert.assertEqual(10000, relativeFPA.max_absolute_altitude)

        relativeFPA.set_min_altitude_rel_anchor(True, 3)
        Assert.assertEqual(3, relativeFPA.min_altitude_rel_anchor)

        relativeFPA.set_max_altitude_rel_anchor(True, 100)
        Assert.assertEqual(100, relativeFPA.max_altitude_rel_anchor)

        airspeedOpts: "BasicManeuverAirspeedOptions" = relativeFPA.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        relativeFPA.compensate_for_coriolis_accel = True
        Assert.assertTrue(relativeFPA.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRelSpeedAlt
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRelSpeedAlt(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Relative Course"
        relCourse: "BasicManeuverStrategyRelativeCourse" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyRelativeCourse
        )

        validTargets = relCourse.valid_target_names
        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relCourse.target_name = targetName
        Assert.assertEqual(targetName, relCourse.target_name)

        basicManeuver.profile_strategy_type = "Relative Speed/Altitude"
        relSpeedAlt: "BasicManeuverStrategyRelSpeedAltitude" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyRelSpeedAltitude
        )

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        testAC: "IStkObject" = acObj.copy_object("LeaderAC")
        relSpeedAlt.target_name = "Aircraft/LeaderAC"
        Assert.assertEqual("Aircraft/LeaderAC", relSpeedAlt.target_name)
        Assert.assertEqual(targetName, relCourse.target_name)

        relSpeedAlt.target_resolution = 4
        Assert.assertEqual(4, relSpeedAlt.target_resolution)

        relSpeedAlt.relative_altitude_mode = RELATIVE_ALTITUDE_MODE.HOLD_OFFSET_ALTITUDE
        relSpeedAlt.altitude_offset = 2
        Assert.assertEqual(2, relSpeedAlt.altitude_offset)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            relSpeedAlt.elevation_angle = 5

        relSpeedAlt.relative_altitude_mode = RELATIVE_ALTITUDE_MODE.HOLD_ELEVATION_ANGLE
        relSpeedAlt.elevation_angle = 5
        angle: typing.Any = relSpeedAlt.elevation_angle
        Assert.assertEqual(5, float(angle))
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            relSpeedAlt.altitude_offset = 2

        relSpeedAlt.use_perf_model_limits = True
        Assert.assertTrue(relSpeedAlt.use_perf_model_limits)
        relSpeedAlt.use_tgt_aspect_for_airspeed = True
        Assert.assertTrue(relSpeedAlt.use_tgt_aspect_for_airspeed)

        relSpeedAlt.range_for_equal_speed = 2
        Assert.assertEqual(2, relSpeedAlt.range_for_equal_speed)
        relSpeedAlt.range_to_transition_speed = 4
        Assert.assertEqual(4, relSpeedAlt.range_to_transition_speed)

        relSpeedAlt.min_altitude = 2
        Assert.assertEqual(2, relSpeedAlt.min_altitude)
        relSpeedAlt.max_altitude = 50001
        Assert.assertEqual(50001, relSpeedAlt.max_altitude)

        relSpeedAlt.set_airspeed_offset(AIRSPEED_TYPE.TAS, 5)
        Assert.assertEqual(5, relSpeedAlt.airspeed_offset)
        relSpeedAlt.set_airspeed_offset(AIRSPEED_TYPE.MACH, 0.1)
        Assert.assertEqual(0.1, relSpeedAlt.airspeed_offset)

        relSpeedAlt.set_min_airspeed(AIRSPEED_TYPE.TAS, 100)
        Assert.assertEqual(100, relSpeedAlt.min_airspeed)
        relSpeedAlt.set_min_airspeed(AIRSPEED_TYPE.MACH, 0.1)
        Assert.assertEqual(0.1, relSpeedAlt.min_airspeed)

        relSpeedAlt.set_max_airspeed(AIRSPEED_TYPE.TAS, 200)
        Assert.assertEqual(200, relSpeedAlt.max_airspeed)
        relSpeedAlt.set_max_airspeed(AIRSPEED_TYPE.MACH, 0.2)
        Assert.assertEqual(0.2, relSpeedAlt.max_airspeed)

        relSpeedAlt.stop_condition = (
            REL_SPEED_ALTITUDE_STOP_CONDITION.REL_SPEED_ALTITUDE_STOP_AFTER_TARGET_CURRENT_PROCEDURE
        )
        Assert.assertEqual(
            REL_SPEED_ALTITUDE_STOP_CONDITION.REL_SPEED_ALTITUDE_STOP_AFTER_TARGET_CURRENT_PROCEDURE,
            relSpeedAlt.stop_condition,
        )

        relSpeedAlt.compensate_for_coriolis_accel = True
        Assert.assertTrue(relSpeedAlt.compensate_for_coriolis_accel)

        testAC.unload()
        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRendezvousFormation
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRendezvousFormation(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        testAC: "IStkObject" = acObj.copy_object("LeaderAC")

        basicManeuver.navigation_strategy_type = "Rendezvous/Formation"
        formation: "BasicManeuverStrategyRendezvous" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyRendezvous
        )

        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        with pytest.raises(Exception, match=RegexSubstringMatch("not a valid")):
            formation.target_name = targetName

        formation.target_name = "Aircraft/LeaderAC"
        Assert.assertEqual("Aircraft/LeaderAC", formation.target_name)

        formation.target_resolution = 0.7
        Assert.assertEqual(0.7, formation.target_resolution)

        formation.relative_bearing = 179
        bearing: typing.Any = formation.relative_bearing
        Assert.assertEqual(179, float(bearing))
        formation.relative_range = 4
        Assert.assertEqual(4, formation.relative_range)
        formation.altitude_split = 200
        Assert.assertEqual(200, formation.altitude_split)

        formation.use_perf_model_limits = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            formation.altitude_rate_control = 1000
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            formation.min_load_factor_g = -3
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            formation.max_load_factor_g = 3

        formation.use_perf_model_limits = False
        formation.altitude_rate_control = 1000
        Assert.assertAlmostEqual(1000, formation.altitude_rate_control, delta=tolerance)
        formation.min_load_factor_g = -3
        Assert.assertEqual(-3, formation.min_load_factor_g)
        formation.max_load_factor_g = 3
        Assert.assertEqual(3, formation.max_load_factor_g)

        formation.maneuver_factor = 0.1
        Assert.assertAlmostEqual(0.1, formation.maneuver_factor, delta=tolerance)

        formation.set_cpa(True, 150)
        Assert.assertEqual(150, formation.cpa)
        Assert.assertTrue(formation.enable_collision_avoidance)

        formation.max_speed_advantage = 51
        Assert.assertEqual(51, formation.max_speed_advantage)

        formation.airspeed_control_mode = ACCEL_PERF_MODEL_OVERRIDE.ACCEL_PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: float = formation.accel_decel_g
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            formation.accel_decel_g = 0.1
        formation.airspeed_control_mode = ACCEL_PERF_MODEL_OVERRIDE.ACCEL_OVERRIDE
        formation.accel_decel_g = 0.1
        Assert.assertEqual(0.1, formation.accel_decel_g)

        formation.set_airspeed_factor(True, 0.2)
        Assert.assertAlmostEqual(0.2, formation.airspeed_factor, delta=tolerance)
        Assert.assertTrue(formation.use_separate_airspeed_control)

        testAC.unload()
        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRollingPull
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRollingPull(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Rolling Pull"
        pull: "BasicManeuverStrategyRollingPull" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyRollingPull
        )
        pull.active_mode = ROLLING_PULL_MODE.PULL_TO_ANGLE_MODE
        pull.angle = 10
        angle: typing.Any = pull.angle
        Assert.assertAlmostEqual(10, float(angle), delta=tolerance)

        Assert.assertEqual("Rolling Pull", basicManeuver.profile_strategy_type)
        pullProfile: "BasicManeuverStrategyRollingPull" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategyRollingPull
        )
        angleProfile: typing.Any = pullProfile.angle
        Assert.assertAlmostEqual(10, float(angleProfile), delta=tolerance)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            pull.roll_orientation = ROLL_UPRIGHT_INVERTED.ROLL_INVERTED
        pull.active_mode = ROLLING_PULL_MODE.ROLL_TO_ORIENTATION_MODE
        pull.roll_orientation = ROLL_UPRIGHT_INVERTED.ROLL_INVERTED
        Assert.assertEqual(ROLL_UPRIGHT_INVERTED.ROLL_INVERTED, pull.roll_orientation)

        pull.roll_rate_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testRate: typing.Any = pull.override_roll_rate
        pull.roll_rate_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        pull.override_roll_rate = 20
        overrideRollRate: typing.Any = pull.override_roll_rate
        Assert.assertEqual(20, float(overrideRollRate))

        pull.pull_g_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            pull.override_pull_g = 2
        pull.pull_g_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        pull.override_pull_g = 2
        Assert.assertEqual(2, pull.override_pull_g)

        airspeedOpts: "BasicManeuverAirspeedOptions" = pull.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverSimpleTurn
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverSimpleTurn(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Simple Turn"
        simpleTurn: "BasicManeuverStrategySimpleTurn" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategySimpleTurn
        )

        simpleTurn.reference_frame = BASIC_MANEUVER_REFERENCE_FRAME.EARTH_FRAME
        Assert.assertEqual(BASIC_MANEUVER_REFERENCE_FRAME.EARTH_FRAME, simpleTurn.reference_frame)

        simpleTurn.turn_angle = 1.2
        turnAngle: typing.Any = simpleTurn.turn_angle
        Assert.assertEqual(1.2, float(turnAngle))

        simpleTurn.turn_radius_factor = 1.1
        Assert.assertEqual(1.1, simpleTurn.turn_radius_factor)

        simpleTurn.compensate_for_coriolis_accel = True
        Assert.assertTrue(simpleTurn.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverSmoothAccel
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverSmoothAccel(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Smooth Accel"
        accel: "BasicManeuverStrategySmoothAccel" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategySmoothAccel
        )
        accel.roll_rate_dot = 29
        rateDot: typing.Any = accel.roll_rate_dot
        Assert.assertAlmostEqual(29, float(rateDot), delta=tolerance)

        Assert.assertEqual("Smooth Accel", basicManeuver.profile_strategy_type)
        accelProfile: "BasicManeuverStrategySmoothAccel" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategySmoothAccel
        )
        rateDotProfile: typing.Any = accelProfile.roll_rate_dot
        Assert.assertAlmostEqual(29, float(rateDotProfile), delta=tolerance)

        accel.turn_direction = SMOOTH_ACCEL_LEFT_RIGHT.SMOOTH_ACCEL_LEFT
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            accel.pitch_angle = 89
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            accel.roll_angle = 89
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            accel.stop_on_pitch_angle = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            accel.stop_on_roll_angle = True

        accel.control_pitch_angle = True
        accel.pitch_angle = 89
        pitchAngle: typing.Any = accel.pitch_angle
        Assert.assertAlmostEqual(89, float(pitchAngle), delta=tolerance)
        accel.stop_on_pitch_angle = True

        accel.control_roll_angle = True
        accel.roll_angle = 89
        rollAngle: typing.Any = accel.roll_angle
        Assert.assertAlmostEqual(89, float(rollAngle), delta=tolerance)
        accel.stop_on_roll_angle = True

        accel.stop_on_roll_angle = False
        accel.control_roll_angle = False
        accel.turn_direction = SMOOTH_ACCEL_LEFT_RIGHT.SMOOTH_ACCEL_NO_ROLL
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            accel.roll_angle = 89
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            accel.control_roll_angle = False
        accel.stop_on_roll_angle = True
        Assert.assertTrue(accel.stop_on_roll_angle)

        airspeedOpts: "BasicManeuverAirspeedOptions" = accel.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverSmoothTurn
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverSmoothTurn(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Smooth Turn"
        turn: "BasicManeuverStrategySmoothTurn" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategySmoothTurn)

        turn.heading_change = 89
        headingChange: typing.Any = turn.heading_change
        Assert.assertAlmostEqual(89, float(headingChange), delta=tolerance)

        Assert.assertEqual("Smooth Turn", basicManeuver.profile_strategy_type)
        turnProfile: "BasicManeuverStrategySmoothTurn" = clr.CastAs(
            basicManeuver.profile, BasicManeuverStrategySmoothTurn
        )
        headingChange = turnProfile.heading_change
        Assert.assertAlmostEqual(89, float(headingChange), delta=tolerance)

        turn.turn_mode = SMOOTH_TURN_MODE.SMOOTH_TURN_LOAD_FACTOR
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            turn.roll_angle = 5
        turn.load_factor_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            turn.override_load_factor = 1
        turn.load_factor_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        turn.override_load_factor = 1
        Assert.assertEqual(1, turn.override_load_factor)

        turn.turn_mode = SMOOTH_TURN_MODE.SMOOTH_TURN_ROLL_ANGLE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            turn.load_factor_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        turn.roll_rate_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            turn.override_roll_rate = 1
        turn.roll_rate_mode = PERF_MODEL_OVERRIDE.OVERRIDE
        turn.override_roll_rate = 1
        overrideRollRate: typing.Any = turn.override_roll_rate
        Assert.assertEqual(1, float(overrideRollRate))

        turn.fpa_mode = SMOOTH_TURN_FPA_MODE.SMOOTH_TURN_FPA_LEVEL_OFF
        Assert.assertEqual(SMOOTH_TURN_FPA_MODE.SMOOTH_TURN_FPA_LEVEL_OFF, turn.fpa_mode)

        airspeedOpts: "BasicManeuverAirspeedOptions" = turn.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverStationkeeping
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverStationkeeping(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Stationkeeping"
        stationNav: "BasicManeuverStrategyStationkeeping" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyStationkeeping
        )

        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        stationNav.target_name = targetName
        Assert.assertEqual(targetName, stationNav.target_name)

        stationNav.target_resolution = 0.7
        Assert.assertEqual(0.7, stationNav.target_resolution)

        stationNav.max_target_speed_fraction = 40
        Assert.assertEqual(40, stationNav.max_target_speed_fraction)

        stationNav.rel_bearing = 89
        bearing: typing.Any = stationNav.rel_bearing
        Assert.assertEqual(89, float(bearing))
        stationNav.rel_range = 2
        Assert.assertEqual(2, stationNav.rel_range)
        stationNav.desired_radius = 4
        Assert.assertEqual(4, stationNav.desired_radius)
        stationNav.maneuver_factor = 6
        Assert.assertEqual(6, stationNav.maneuver_factor)

        stationNav.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL, 0)
        Assert.assertEqual(
            stationNav.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL
        )
        stationNav.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL, 0.1)
        Assert.assertEqual(stationNav.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL)
        Assert.assertAlmostEqual(0.1, stationNav.control_limit_horiz_accel, delta=tolerance)
        stationNav.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE, 0.2)
        Assert.assertEqual(stationNav.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE)
        Assert.assertAlmostEqual(0.2, float(stationNav.control_limit_turn_rate), delta=tolerance)
        stationNav.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS, 700)
        Assert.assertEqual(stationNav.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS)
        Assert.assertEqual(700, stationNav.control_limit_turn_radius)

        scenario: "Scenario" = clr.CastAs(EarlyBoundTests.AG_Scenario, Scenario)
        stationNav.stop_condition = STATIONKEEPING_STOP_CONDITION.STOP_CONDITION_NOT_SET
        Assert.assertEqual(stationNav.stop_condition, STATIONKEEPING_STOP_CONDITION.STOP_CONDITION_NOT_SET)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: float = stationNav.stop_after_duration
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: typing.Any = stationNav.stop_after_time
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            testVal: int = stationNav.stop_after_turn_count
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            stationNav.stop_after_duration = 2
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            stationNav.stop_after_time = scenario.stop_time
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            stationNav.stop_after_turn_count = 5
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            stationNav.stop_course = 2
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            stationNav.use_relative_course = True

        stationNav.stop_condition = STATIONKEEPING_STOP_CONDITION.STOP_AFTER_TURN_COUNT
        Assert.assertEqual(stationNav.stop_condition, STATIONKEEPING_STOP_CONDITION.STOP_AFTER_TURN_COUNT)
        stationNav.stop_after_turn_count = 5
        Assert.assertEqual(5, stationNav.stop_after_turn_count)
        stationNav.use_relative_course = True
        stationNav.stop_course = 2
        course: typing.Any = stationNav.stop_course
        Assert.assertTrue(stationNav.use_relative_course)
        Assert.assertEqual(2, float(course))

        stationNav.stop_condition = STATIONKEEPING_STOP_CONDITION.STOP_AFTER_TIME
        Assert.assertEqual(stationNav.stop_condition, STATIONKEEPING_STOP_CONDITION.STOP_AFTER_TIME)
        stationNav.stop_after_time = scenario.stop_time
        time: typing.Any = stationNav.stop_after_time
        Assert.assertEqual(scenario.stop_time, time)

        stationNav.stop_condition = STATIONKEEPING_STOP_CONDITION.STOP_AFTER_DURATION
        Assert.assertEqual(stationNav.stop_condition, STATIONKEEPING_STOP_CONDITION.STOP_AFTER_DURATION)
        stationNav.stop_after_duration = 2
        Assert.assertEqual(2, stationNav.stop_after_duration)

        stationNav.compensate_for_coriolis_accel = True
        Assert.assertTrue(stationNav.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverStraightAhead
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverStraightAhead(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Straight Ahead"
        straightAhead: "BasicManeuverStrategyStraightAhead" = clr.CastAs(
            basicManeuver.navigation, BasicManeuverStrategyStraightAhead
        )

        straightAhead.reference_frame = STRAIGHT_AHEAD_REFERENCE_FRAME.MAINTAIN_COURSE
        Assert.assertEqual(STRAIGHT_AHEAD_REFERENCE_FRAME.MAINTAIN_COURSE, straightAhead.reference_frame)

        straightAhead.compensate_for_coriolis_accel = True
        Assert.assertTrue(straightAhead.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverWeave
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverWeave(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        basicManeuver: "ProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_END_OF_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_BASIC_MANEUVER),
            ProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Weave"
        weave: "BasicManeuverStrategyWeave" = clr.CastAs(basicManeuver.navigation, BasicManeuverStrategyWeave)

        weave.heading_change = 45
        heading: typing.Any = weave.heading_change
        Assert.assertEqual(45, float(heading))
        weave.max_num_cycles = 3
        Assert.assertEqual(3, weave.max_num_cycles)
        weave.max_distance = 11
        Assert.assertEqual(11, weave.max_distance)

        weave.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL, 0)
        Assert.assertEqual(weave.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_USE_ACCEL_PERF_MODEL)
        weave.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL, 0.1)
        Assert.assertEqual(weave.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_HORIZ_ACCEL)
        Assert.assertAlmostEqual(0.1, weave.control_limit_horiz_accel, delta=tolerance)
        weave.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE, 0.2)
        Assert.assertEqual(weave.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MAX_TURN_RATE)
        Assert.assertAlmostEqual(0.2, float(weave.control_limit_turn_rate), delta=tolerance)
        weave.set_control_limit(BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS, 700)
        Assert.assertEqual(weave.control_limit_mode, BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT.NAV_MIN_TURN_RADIUS)
        Assert.assertEqual(700, weave.control_limit_turn_radius)

        weave.compensate_for_coriolis_accel = True
        Assert.assertTrue(weave.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region RelativeToPrevProcedure
    @category("Site Tests")
    def test_RelativeToPrevProcedure(self):
        self.EmptyProcedures()

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget")
        place: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.PLACE, "Place")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_RELATIVE_TO_PREV_PROCEDURE, PROCEDURE_TYPE.PROC_ENROUTE
        )
        relToPrevProc: "SiteRelToPrevProcedure" = clr.CastAs(proc2.site, SiteRelToPrevProcedure)

        self.TestSiteName(relToPrevProc.get_as_site(), "Relative to Previous Procedure")

        relToPrevProc.bearing_mode = REL_ABS_BEARING.TRUE_BEARING
        Assert.assertEqual(REL_ABS_BEARING.TRUE_BEARING, relToPrevProc.bearing_mode)
        relToPrevProc.bearing = 3
        bearing: typing.Any = relToPrevProc.bearing
        Assert.assertEqual(3, float(bearing))
        relToPrevProc.range = 11
        Assert.assertEqual(11, relToPrevProc.range)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(proc2)
        areaTarget.unload()
        place.unload()

    # endregion

    # region RelativeToStationarySTKObject
    @category("Site Tests")
    def test_RelativeToStationarySTKObject(self):
        self.EmptyProcedures()

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget")
        place: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.PLACE, "Place")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_RELATIVE_TO_STATIONARY_STK_OBJECT, PROCEDURE_TYPE.PROC_ENROUTE
        )
        relToSTKObject: "SiteRelToSTKObject" = clr.CastAs(proc1.site, SiteRelToSTKObject)

        self.TestSiteName(relToSTKObject.get_as_site(), "Relative to stationary STK Object Site")

        relToSTKObject.object_name = "Place/Place"
        name: typing.Any = relToSTKObject.object_name
        Assert.assertTrue(("Place/Place" == str(name)))

        names = relToSTKObject.valid_object_names
        Assert.assertTrue((Array.Length(names) >= 2))

        relToSTKObject.bearing = 5
        bearing: typing.Any = relToSTKObject.bearing
        Assert.assertEqual(5, float(bearing))
        relToSTKObject.use_magnetic_bearing = True
        Assert.assertTrue(relToSTKObject.use_magnetic_bearing)

        relToSTKObject.range = 11
        Assert.assertEqual(11, relToSTKObject.range)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        areaTarget.unload()
        place.unload()

    # endregion

    # region SiteAirportFromCatalog
    @category("Site Tests")
    @category("ARINC424 Test")
    def test_SiteAirportFromCatalog(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_AIRPORT_FROM_CATALOG, PROCEDURE_TYPE.PROC_TAKEOFF
        )
        catAirport: "SiteAirportFromCatalog" = clr.CastAs(proc1.site, SiteAirportFromCatalog)

        arincAirports: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.airport_category.arinc424_airports
        arincSource: "ICatalogSource" = clr.CastAs(arincAirports, ICatalogSource)
        arincNames = arincSource.child_names
        firstArincAirport: "IARINC424Item" = arincAirports.get_arinc424_item(str(arincNames[0]))
        catAirport.set_catalog_airport(clr.CastAs(firstArincAirport, ARINC424Airport))
        arincName: str = firstArincAirport.get_as_catalog_item().name
        Assert.assertEqual(arincName, catAirport.get_as_site().name)
        arincAirport2: "ICatalogItem" = clr.CastAs(catAirport.get_catalog_airport(), ICatalogItem)
        Assert.assertEqual(arincName, arincAirport2.name)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region SiteNavaidFromCatalog
    @category("Site Tests")
    @category("ARINC424 Test")
    def test_SiteNavaidFromCatalog(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_NAVAID_FROM_CATALOG, PROCEDURE_TYPE.PROC_ENROUTE
        )
        catNavaid: "SiteNavaidFromCatalog" = clr.CastAs(proc1.site, SiteNavaidFromCatalog)

        arincNavaids: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.navaid_category.arinc424_navaids
        arincSource: "ICatalogSource" = clr.CastAs(arincNavaids, ICatalogSource)
        arincNames = arincSource.child_names
        firstArincNavaid: "IARINC424Item" = arincNavaids.get_arinc424_item(str(arincNames[0]))
        catNavaid.set_catalog_navaid(clr.CastAs(firstArincNavaid, ARINC424Navaid))
        arincName: str = firstArincNavaid.get_as_catalog_item().name
        Assert.assertEqual(arincName, catNavaid.get_as_site().name)
        arincNavaid2: "ICatalogItem" = clr.CastAs(catNavaid.get_catalog_navaid(), ICatalogItem)
        Assert.assertEqual(arincName, arincNavaid2.name)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region SiteRunway
    @category("Site Tests")
    def test_SiteRunway(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        runway: "SiteRunway" = clr.CastAs(proc1.site, SiteRunway)

        self.TestSiteName(runway.get_as_site(), "Runway")

        runway.latitude = 1
        lat: typing.Any = runway.latitude
        Assert.assertEqual(1, float(lat))
        runway.longitude = 2
        lon: typing.Any = runway.longitude
        Assert.assertEqual(2, float(lon))
        runway.altitude = 5
        Assert.assertEqual(5, runway.altitude)
        runway.altitude_reference = AGL_MSL.ALTITUDE_MSL
        Assert.assertEqual(AGL_MSL.ALTITUDE_MSL, runway.altitude_reference)

        runway.high_end_heading = 195
        highEndHeading: typing.Any = runway.high_end_heading
        Assert.assertAlmostEqual(195, float(highEndHeading), delta=tolerance)
        lowEndHeading: typing.Any = runway.low_end_heading
        Assert.assertAlmostEqual(15, float(lowEndHeading), delta=tolerance)
        runway.is_magnetic = False
        Assert.assertEqual(False, runway.is_magnetic)

        runway.length = 5
        Assert.assertEqual(5, runway.length)

        runway.add_to_catalog(True)

        runway.latitude = 0
        lat = runway.latitude
        Assert.assertEqual(0, float(lat))
        runway.longitude = 0
        lon = runway.longitude
        Assert.assertEqual(0, float(lon))
        runway.altitude = 0
        Assert.assertEqual(0, runway.altitude)

        # Copy the catalog runway you just created
        catRunway: "UserRunway" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways.get_user_runway("Runway")
        runway.copy_from_catalog(clr.CastAs(catRunway, ICatalogRunway))

        lat = runway.latitude
        Assert.assertEqual(1, float(lat))
        runway.longitude = 2
        lon = runway.longitude
        Assert.assertEqual(2, float(lon))
        runway.altitude = 5
        Assert.assertEqual(5, runway.altitude)

        with pytest.raises(Exception):
            runway.add_to_catalog(False)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region SiteWaypoint
    @category("Site Tests")
    def test_SiteWaypoint(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_WAYPOINT, PROCEDURE_TYPE.PROC_ENROUTE)
        waypoint: "SiteWaypoint" = clr.CastAs(proc1.site, SiteWaypoint)

        self.TestSiteName(waypoint.get_as_site(), "Waypoint")

        waypoint.latitude = 1
        lat: typing.Any = waypoint.latitude
        Assert.assertEqual(1, float(lat))
        waypoint.longitude = 2
        lon: typing.Any = waypoint.longitude
        Assert.assertEqual(2, float(lon))

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region SiteReferenceState
    @category("Site Tests")
    def test_SiteReferenceState(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_REFERENCE_STATE, PROCEDURE_TYPE.PROC_REFERENCE_STATE
        )
        refStateSite: "SiteReferenceState" = clr.CastAs(proc1.site, SiteReferenceState)

        self.TestSiteName(refStateSite.get_as_site(), "Reference State Site")

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region STKAreaTarget
    @category("Site Tests")
    def test_STKAreaTarget(self):
        self.EmptyProcedures()

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget")
        areaTarget2: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget2")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_STK_AREA_TARGET, PROCEDURE_TYPE.PROC_AREA_TARGET_SEARCH
        )
        atSite: "SiteSTKAreaTarget" = clr.CastAs(proc1.site, SiteSTKAreaTarget)

        atSite.object_name = "AreaTarget/AreaTarget2"
        name: typing.Any = atSite.object_name
        Assert.assertTrue(("AreaTarget/AreaTarget2" == str(name)))

        names = atSite.valid_object_names
        Assert.assertTrue((Array.Length(names) >= 2))

        EarlyBoundTests.AG_Procedures.remove(proc1)
        areaTarget.unload()
        areaTarget2.unload()

    # endregion

    # region SiteDynState
    @category("Site Tests")
    def test_SiteDynState(self):
        self.EmptyProcedures()

        missile: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile")), Missile
        )
        traj: "VehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, VehiclePropagatorBallistic)
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, VehicleImpactLocationPoint)
        impact: "VehicleImpactLLA" = clr.CastAs(impactLocation.impact, VehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()

        missile2: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile2")), Missile
        )
        traj2: "VehiclePropagatorBallistic" = clr.CastAs(missile2.trajectory, VehiclePropagatorBallistic)
        impactLocation2: "VehicleImpactLocationPoint" = clr.CastAs(traj2.impact_location, VehicleImpactLocationPoint)
        impact2: "VehicleImpactLLA" = clr.CastAs(impactLocation2.impact, VehicleImpactLLA)
        impact2.lat = -20
        impact2.lon = -20
        traj2.propagate()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_DYN_STATE, PROCEDURE_TYPE.PROC_LAUNCH_DYN_STATE
        )
        dynState: "SiteDynState" = clr.CastAs(proc1.site, SiteDynState)

        dynState.object_name = "Missile/Missile2"
        name: typing.Any = dynState.object_name
        Assert.assertTrue(("Missile/Missile2" == str(name)))

        names = dynState.valid_object_names
        Assert.assertTrue((Array.Length(names) >= 2))

        EarlyBoundTests.AG_Procedures.remove(proc1)
        missileObj: "IStkObject" = clr.CastAs(missile, IStkObject)
        missileObj.unload()
        missileObj2: "IStkObject" = clr.CastAs(missile2, IStkObject)
        missileObj2.unload()

    # endregion

    # region STKObjectWaypoint
    @category("Site Tests")
    def test_STKObjectWaypoint(self):
        self.EmptyProcedures()

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget")
        place: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.PLACE, "Place")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_STK_OBJECT_WAYPOINT, PROCEDURE_TYPE.PROC_ENROUTE
        )
        objectWaypointSite: "SiteSTKObjectWaypoint" = clr.CastAs(proc1.site, SiteSTKObjectWaypoint)

        self.TestSiteName(objectWaypointSite.get_as_site(), "STK Object Waypoint Site")

        objectWaypointSite.object_name = "Place/Place"
        name: typing.Any = objectWaypointSite.object_name
        Assert.assertTrue(("Place/Place" == str(name)))

        names = objectWaypointSite.valid_object_names
        Assert.assertTrue((Array.Length(names) >= 2))

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        scenario: "Scenario" = clr.CastAs(EarlyBoundTests.AG_Scenario, Scenario)

        objectWaypointSite.minimize_site_proc_time_diff = MINIMIZE_SITE_PROC_TIME_DIFF.MINIMIZE_TIME_DIFFERENCE_OFF
        Assert.assertEqual(
            MINIMIZE_SITE_PROC_TIME_DIFF.MINIMIZE_TIME_DIFFERENCE_OFF, objectWaypointSite.minimize_site_proc_time_diff
        )

        minTime: typing.Any = objectWaypointSite.min_time
        Assert.assertTrue(("Unlimited" == str(minTime)))
        maxTime: typing.Any = objectWaypointSite.max_time
        Assert.assertTrue(("Unlimited" == str(maxTime)))

        objectWaypointSite.waypoint_time = 30
        Assert.assertEqual(30, objectWaypointSite.waypoint_time)

        objectWaypointSite.minimize_site_proc_time_diff = (
            MINIMIZE_SITE_PROC_TIME_DIFF.MINIMIZE_TIME_DIFFERENCE_NEXT_UPDATE
        )
        Assert.assertEqual(
            MINIMIZE_SITE_PROC_TIME_DIFF.MINIMIZE_TIME_DIFFERENCE_NEXT_UPDATE,
            objectWaypointSite.minimize_site_proc_time_diff,
        )
        objectWaypointSite.minimize_site_proc_time_diff = MINIMIZE_SITE_PROC_TIME_DIFF.MINIMIZE_TIME_DIFFERENCE_ALWAYS
        Assert.assertEqual(
            MINIMIZE_SITE_PROC_TIME_DIFF.MINIMIZE_TIME_DIFFERENCE_ALWAYS,
            objectWaypointSite.minimize_site_proc_time_diff,
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            objectWaypointSite.waypoint_time = 5

        objectWaypointSite.offset_mode = STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_NONE
        Assert.assertEqual(STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_NONE, objectWaypointSite.offset_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            objectWaypointSite.bearing = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            objectWaypointSite.use_magnetic_bearing = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            objectWaypointSite.range = 10
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            objectWaypointSite.vgt_point = "SubPoint(Detic)"

        objectWaypointSite.offset_mode = STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_BEARING_RANGE
        Assert.assertEqual(STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_BEARING_RANGE, objectWaypointSite.offset_mode)
        objectWaypointSite.bearing = 1
        Assert.assertEqual(1, objectWaypointSite.bearing)
        objectWaypointSite.use_magnetic_bearing = True
        Assert.assertTrue(objectWaypointSite.use_magnetic_bearing)
        objectWaypointSite.range = 10
        Assert.assertEqual(10, objectWaypointSite.range)

        objectWaypointSite.offset_mode = STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_RELATIVE_BEARING_RANGE
        Assert.assertEqual(
            STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_RELATIVE_BEARING_RANGE, objectWaypointSite.offset_mode
        )
        objectWaypointSite.bearing = 1
        Assert.assertEqual(1, objectWaypointSite.bearing)
        objectWaypointSite.range = 10
        Assert.assertEqual(10, objectWaypointSite.range)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            objectWaypointSite.use_magnetic_bearing = True

        objectWaypointSite.offset_mode = STK_OBJECT_WAYPOINT_OFFSET_MODE.OFFSET_VGT_POINT
        objectWaypointSite.vgt_point = "SubPoint(Detic)"
        Assert.assertEqual("SubPoint(Detic)", objectWaypointSite.vgt_point)

        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(proc1)
        areaTarget.unload()
        place.unload()

    # endregion

    # region STKStaticObject
    @category("Site Tests")
    def test_STKStaticObject(self):
        self.EmptyProcedures()

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget")
        place: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.PLACE, "Place")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_STK_STATIC_OBJECT, PROCEDURE_TYPE.PROC_ENROUTE
        )
        staticObjectSite: "SiteSTKStaticObject" = clr.CastAs(proc1.site, SiteSTKStaticObject)

        self.TestSiteName(staticObjectSite.get_as_site(), "STK Static Object Site")

        staticObjectSite.object_name = "Place/Place"
        name: typing.Any = staticObjectSite.object_name
        Assert.assertTrue(("Place/Place" == str(name)))

        names = staticObjectSite.valid_object_names
        Assert.assertTrue((Array.Length(names) >= 2))

        EarlyBoundTests.AG_Procedures.remove(proc1)
        areaTarget.unload()
        place.unload()

    # endregion

    # region STKVehicle
    @category("Site Tests")
    def test_STKVehicle(self):
        self.EmptyProcedures()

        missile: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile")), Missile
        )
        traj: "VehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, VehiclePropagatorBallistic)
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, VehicleImpactLocationPoint)
        impact: "VehicleImpactLLA" = clr.CastAs(impactLocation.impact, VehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()

        missile2: "Missile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Missile2")), Missile
        )
        traj2: "VehiclePropagatorBallistic" = clr.CastAs(missile2.trajectory, VehiclePropagatorBallistic)
        impactLocation2: "VehicleImpactLocationPoint" = clr.CastAs(traj2.impact_location, VehicleImpactLocationPoint)
        impact2: "VehicleImpactLLA" = clr.CastAs(impactLocation2.impact, VehicleImpactLLA)
        impact2.lat = -20
        impact2.lon = -20
        traj2.propagate()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_STK_VEHICLE, PROCEDURE_TYPE.PROC_LAUNCH)
        stkVehicleSite: "SiteSTKVehicle" = clr.CastAs(proc1.site, SiteSTKVehicle)

        stkVehicleSite.object_name = "Missile/Missile2"
        name: typing.Any = stkVehicleSite.object_name
        Assert.assertTrue(("Missile/Missile2" == str(name)))

        names = stkVehicleSite.valid_object_names
        Assert.assertTrue((Array.Length(names) >= 2))

        EarlyBoundTests.AG_Procedures.remove(proc1)
        missileObj: "IStkObject" = clr.CastAs(missile, IStkObject)
        missileObj.unload()
        missileObj2: "IStkObject" = clr.CastAs(missile2, IStkObject)
        missileObj2.unload()

    # endregion

    # region SuperProcedure
    @category("Procedure Tests")
    def test_SuperProcedure(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
        superProc: "ProcedureSuperProcedure" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(SITE_TYPE.SITE_SUPER_PROCEDURE, PROCEDURE_TYPE.PROC_SUPER_PROCEDURE),
            ProcedureSuperProcedure,
        )

        self.TestProcedureName(superProc.get_as_procedure(), "Super Procedure")

        Assert.assertEqual(False, EarlyBoundTests.AG_Mission.is_valid)

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.flightprocs")
        with pytest.raises(Exception):
            superProc.load_procedures_from_file(nonexistingfilepath)

        filepath: str = TestBase.GetScenarioFile("basicManeuver.flightprocs")
        superProc.load_procedures_from_file(filepath)
        Assert.assertTrue(EarlyBoundTests.AG_Mission.is_valid)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(superProc, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region SiteSuperProcedure
    @category("Site Tests")
    def test_SiteSuperProcedure(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_SUPER_PROCEDURE, PROCEDURE_TYPE.PROC_SUPER_PROCEDURE
        )
        superProcSite: "SiteSuperProcedure" = clr.CastAs(proc1.site, SiteSuperProcedure)

        self.TestSiteName(superProcSite.get_as_site(), "Super Procedure Site")

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region SiteVTOLPoint
    @category("Site Tests")
    def test_SiteVTOLPoint(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            SITE_TYPE.SITE_VTOL_POINT, PROCEDURE_TYPE.PROC_VERTICAL_TAKEOFF
        )
        vtolSite: "SiteVTOLPoint" = clr.CastAs(proc1.site, SiteVTOLPoint)

        vtolSite.latitude = 1
        lat: typing.Any = vtolSite.latitude
        Assert.assertEqual(1, float(lat))
        vtolSite.longitude = 2
        lon: typing.Any = vtolSite.longitude
        Assert.assertEqual(2, float(lon))
        vtolSite.altitude = 101
        Assert.assertEqual(101, vtolSite.altitude)
        vtolSite.altitude_reference = AGL_MSL.ALTITUDE_AGL
        Assert.assertEqual(AGL_MSL.ALTITUDE_AGL, vtolSite.altitude_reference)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region ReadOnlyCatalogItem
    @category("Aircraft Tests")
    def test_ReadOnlyCatalogItem(self):
        basicAirliner: "AircraftModel" = EarlyBoundTests.AG_AvtrAircraftModels.get_aircraft("Basic Airliner")
        acAsCatalogItem: "ICatalogItem" = basicAirliner.get_as_catalog_item()
        Assert.assertEqual("Basic Airliner", acAsCatalogItem.name)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            acAsCatalogItem.name = ""

        Assert.assertEqual("Basic Airliner", acAsCatalogItem.name)

        isReadOnly: bool = acAsCatalogItem.is_read_only
        Assert.assertTrue(isReadOnly)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            acAsCatalogItem.remove()

    # endregion

    # region AircraftModel
    @category("Aircraft Tests")
    def test_AircraftModel(self):
        acModelsAsCatalogSource: "ICatalogSource" = EarlyBoundTests.AG_AvtrAircraftModels.get_as_catalog_source()

        containsTestAircraft: bool = acModelsAsCatalogSource.contains("NUNIT CSharp Test")
        Assert.assertTrue(containsTestAircraft)

        acTestAsCatalogItem: "ICatalogItem" = EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item()
        containsTest: bool = acTestAsCatalogItem.contains_child_item("Cruise")
        Assert.assertTrue(containsTest)
        containsTest = acTestAsCatalogItem.contains_child_item("Airplane")
        Assert.assertFalse(containsTest)

        Assert.assertEqual("NUNIT CSharp Test", acTestAsCatalogItem.name)
        acTestAsCatalogItem.name = "NUNIT CSharp Test NameChange"
        Assert.assertEqual("NUNIT CSharp Test NameChange", acTestAsCatalogItem.name)
        acTestAsCatalogItem.name = "NUNIT CSharp Test"

        isReadOnly: bool = acTestAsCatalogItem.is_read_only
        Assert.assertFalse(isReadOnly)

        perfModelNames = acTestAsCatalogItem.child_names
        Assert.assertEqual(8, Array.Length(perfModelNames))

        Assert.assertEqual("Acceleration", perfModelNames[0])
        Assert.assertEqual("Climb", perfModelNames[1])
        Assert.assertEqual("Cruise", perfModelNames[2])
        Assert.assertEqual("Descent", perfModelNames[3])
        Assert.assertEqual("Landing", perfModelNames[4])
        Assert.assertEqual("Takeoff", perfModelNames[5])

    # endregion

    # region AdvFixedWingTool
    @category("Aircraft Tests")
    def test_AdvFixedWingTool(self):
        tolerance: float = 1e-09

        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.wing_area = 300
        Assert.assertEqual(300, advFWT.wing_area)
        advFWT.flaps_area = 50
        Assert.assertEqual(50, advFWT.flaps_area)
        advFWT.speedbrakes_area = 10
        Assert.assertEqual(10, advFWT.speedbrakes_area)

        advFWT.max_altitude = 65000
        Assert.assertEqual(65000, advFWT.max_altitude)
        advFWT.max_mach = 0.98
        Assert.assertEqual(0.98, advFWT.max_mach)
        advFWT.max_eas = 460
        Assert.assertAlmostEqual(460, advFWT.max_eas, delta=tolerance)
        advFWT.min_load_factor = -2.5
        Assert.assertEqual(-2.5, advFWT.min_load_factor)
        advFWT.max_load_factor = 4.5
        Assert.assertEqual(4.5, advFWT.max_load_factor)

        advFWT.use_max_temperature_limit = True
        Assert.assertTrue(advFWT.use_max_temperature_limit)
        advFWT.max_temperature = 900
        Assert.assertEqual(900, advFWT.max_temperature)

        advFWT.cache_aero_data = False
        Assert.assertEqual(False, advFWT.cache_aero_data)
        advFWT.cache_fuel_flow = False
        Assert.assertEqual(False, advFWT.cache_fuel_flow)

        advFWT.create_all_perf_models("CreateAllPerfModelsTest", True, False)
        tempAC.acceleration.get_advanced_acceleration_by_name("CreateAllPerfModelsTest")
        tempAC.climb.get_advanced_climb_by_name("CreateAllPerfModelsTest")
        tempAC.cruise.get_advanced_cruise_by_name("CreateAllPerfModelsTest")
        tempAC.descent.get_advanced_descent_by_name("CreateAllPerfModelsTest")
        tempAC.takeoff.get_advanced_takeoff_by_name("CreateAllPerfModelsTest")
        tempAC.landing.get_advanced_landing_by_name("CreateAllPerfModelsTest")

        with pytest.raises(Exception, match=RegexSubstringMatch("already exist")):
            advFWT.create_all_perf_models("CreateAllPerfModelsTest", False, False)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingExternalAero
    @category("Aircraft Tests")
    def test_AdvFixedWingExternalAero(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.aero_strategy = ADVANCED_FIXED_WING_AERO_STRATEGY.SUBSONIC_AERO
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            aeroTest: "AdvancedFixedWingExternalAero" = advFWT.aero_mode_as_external

        advFWT.aero_strategy = ADVANCED_FIXED_WING_AERO_STRATEGY.EXTERNAL_AERO_FILE
        aero: "AdvancedFixedWingExternalAero" = advFWT.aero_mode_as_external

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.aero")
        with pytest.raises(Exception, match=RegexSubstringMatch("Failed to load the file.")):
            aero.set_filepath(nonexistingfilepath)

        filepath: str = TestBase.GetScenarioFile("advAero.aero")
        returnMsg: str = aero.set_filepath(filepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertTrue(aero.is_valid)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingSubSuperHypersonicAero
    @category("Aircraft Tests")
    def test_AdvFixedWingSubSuperHypersonicAero(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.aero_strategy = ADVANCED_FIXED_WING_AERO_STRATEGY.SUBSONIC_AERO
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            aeroTest: "AdvancedFixedWingSubSuperHypersonicAero" = advFWT.aero_mode_as_sub_super_hypersonic

        advFWT.aero_strategy = ADVANCED_FIXED_WING_AERO_STRATEGY.SUB_SUPER_HYPER_AERO
        Assert.assertEqual(ADVANCED_FIXED_WING_AERO_STRATEGY.SUB_SUPER_HYPER_AERO, advFWT.aero_strategy)
        aero: "AdvancedFixedWingSubSuperHypersonicAero" = advFWT.aero_mode_as_sub_super_hypersonic

        aero.transonic_min_mach = 0.81
        Assert.assertEqual(0.81, aero.transonic_min_mach)
        aero.transonic_max_mach = 1.15
        Assert.assertEqual(1.15, aero.transonic_max_mach)
        aero.super_hyper_mach_transition = 4.3
        Assert.assertEqual(4.3, aero.super_hyper_mach_transition)
        aero.max_aoa = 21
        Assert.assertEqual(21, aero.max_aoa)
        aero.leading_edge_frontal_area_ratio = 0.02
        Assert.assertEqual(0.02, aero.leading_edge_frontal_area_ratio)
        aero.subsonic_aspect_ratio = 4.1
        Assert.assertEqual(4.1, aero.subsonic_aspect_ratio)
        aero.transonic_mach_drag_factor = 3.1
        Assert.assertEqual(3.1, aero.transonic_mach_drag_factor)
        aero.wave_drag_factor = 0.9
        Assert.assertEqual(0.9, aero.wave_drag_factor)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingSubsonicAero
    @category("Aircraft Tests")
    def test_AdvFixedWingSubsonicAero(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.aero_strategy = ADVANCED_FIXED_WING_AERO_STRATEGY.SUPERSONIC_AERO
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            aeroTest: "AdvancedFixedWingSubsonicAero" = advFWT.aero_mode_as_subsonic

        advFWT.aero_strategy = ADVANCED_FIXED_WING_AERO_STRATEGY.SUBSONIC_AERO
        Assert.assertEqual(ADVANCED_FIXED_WING_AERO_STRATEGY.SUBSONIC_AERO, advFWT.aero_strategy)
        aero: "AdvancedFixedWingSubsonicAero" = advFWT.aero_mode_as_subsonic

        aero.geometry_type = ADVANCED_FIXED_WING_GEOMETRY.VARIABLE_GEOMETRY
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            basicGeoTest: "AdvancedFixedWingGeometryBasic" = aero.geometry_mode_as_basic
        aero.geometry_type = ADVANCED_FIXED_WING_GEOMETRY.BASIC_GEOMETRY
        basicGeo: "AdvancedFixedWingGeometryBasic" = aero.geometry_mode_as_basic

        basicGeo.set_aspect_ratio(11)
        Assert.assertEqual(11, basicGeo.aspect_ratio)
        basicGeo.wing_sweep = 22
        sweep: typing.Any = basicGeo.wing_sweep
        Assert.assertEqual(22, float(sweep))

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            variableGeoTest: "AdvancedFixedWingGeometryVariable" = aero.geometry_mode_as_variable
        aero.geometry_type = ADVANCED_FIXED_WING_GEOMETRY.VARIABLE_GEOMETRY
        variableGeo: "AdvancedFixedWingGeometryVariable" = aero.geometry_mode_as_variable

        variableGeo.set_aspect_ratio(12)
        Assert.assertEqual(12, variableGeo.aspect_ratio)
        variableGeo.start_sweep_mach = 0.65
        Assert.assertEqual(0.65, variableGeo.start_sweep_mach)
        variableGeo.stop_sweep_mach = 0.85
        Assert.assertEqual(0.85, variableGeo.stop_sweep_mach)
        variableGeo.min_sweep_angle = 26
        sweep1: typing.Any = variableGeo.min_sweep_angle
        Assert.assertEqual(26, float(sweep1))
        variableGeo.max_sweep_angle = 52
        sweep2: typing.Any = variableGeo.max_sweep_angle
        Assert.assertEqual(52, float(sweep2))

        aero.max_aoa = 21
        Assert.assertEqual(21, aero.max_aoa)
        aero.cd0 = 0.03
        Assert.assertEqual(0.03, aero.cd0)
        aero.mach_divergence = 0.85
        Assert.assertEqual(0.85, aero.mach_divergence)
        aero.transonic_mach_drag_factor = 3.1
        Assert.assertEqual(3.1, aero.transonic_mach_drag_factor)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingSupersonicAero
    @category("Aircraft Tests")
    def test_AdvFixedWingSupersonicAero(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.aero_strategy = ADVANCED_FIXED_WING_AERO_STRATEGY.SUBSONIC_AERO
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            aeroTest: "AdvancedFixedWingSupersonicAero" = advFWT.aero_mode_as_supersonic

        advFWT.aero_strategy = ADVANCED_FIXED_WING_AERO_STRATEGY.SUPERSONIC_AERO
        Assert.assertEqual(ADVANCED_FIXED_WING_AERO_STRATEGY.SUPERSONIC_AERO, advFWT.aero_strategy)
        aero: "AdvancedFixedWingSupersonicAero" = advFWT.aero_mode_as_supersonic

        aero.geometry_type = ADVANCED_FIXED_WING_GEOMETRY.VARIABLE_GEOMETRY
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            basicGeoTest: "AdvancedFixedWingGeometryBasic" = aero.geometry_mode_as_basic
        aero.geometry_type = ADVANCED_FIXED_WING_GEOMETRY.BASIC_GEOMETRY
        basicGeo: "AdvancedFixedWingGeometryBasic" = aero.geometry_mode_as_basic

        basicGeo.set_aspect_ratio(11)
        Assert.assertEqual(11, basicGeo.aspect_ratio)
        basicGeo.wing_sweep = 22
        sweep: typing.Any = basicGeo.wing_sweep
        Assert.assertEqual(22, float(sweep))

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            variableGeoTest: "AdvancedFixedWingGeometryVariable" = aero.geometry_mode_as_variable
        aero.geometry_type = ADVANCED_FIXED_WING_GEOMETRY.VARIABLE_GEOMETRY
        variableGeo: "AdvancedFixedWingGeometryVariable" = aero.geometry_mode_as_variable

        variableGeo.set_aspect_ratio(12)
        Assert.assertEqual(12, variableGeo.aspect_ratio)
        variableGeo.start_sweep_mach = 0.65
        Assert.assertEqual(0.65, variableGeo.start_sweep_mach)
        variableGeo.stop_sweep_mach = 0.85
        Assert.assertEqual(0.85, variableGeo.stop_sweep_mach)
        variableGeo.min_sweep_angle = 26
        sweep1: typing.Any = variableGeo.min_sweep_angle
        Assert.assertEqual(26, float(sweep1))
        variableGeo.max_sweep_angle = 52
        sweep2: typing.Any = variableGeo.max_sweep_angle
        Assert.assertEqual(52, float(sweep2))

        aero.max_aoa = 21
        Assert.assertEqual(21, aero.max_aoa)
        aero.subsonic_cd0 = 0.03
        Assert.assertEqual(0.03, aero.subsonic_cd0)
        aero.transonic_min_mach = 0.85
        Assert.assertEqual(0.85, aero.transonic_min_mach)
        aero.supersonic_max_mach = 1.5
        Assert.assertEqual(1.5, aero.supersonic_max_mach)
        aero.transonic_max_mach = 1.2
        Assert.assertEqual(1.2, aero.transonic_max_mach)
        aero.transonic_mach_drag_factor = 2.5
        Assert.assertEqual(2.5, aero.transonic_mach_drag_factor)
        aero.supersonic_mach_drag_factor = 3.5
        Assert.assertEqual(3.5, aero.supersonic_mach_drag_factor)
        aero.leading_edge_suction_efficiency = 75
        Assert.assertEqual(75, aero.leading_edge_suction_efficiency)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingElectricPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingElectricPowerplant(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingElectricPowerplant" = advFWT.powerplant_mode_as_electric

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.ELECTRIC_POWERPLANT
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.ELECTRIC_POWERPLANT, advFWT.powerplant_strategy)
        prop: "AdvancedFixedWingElectricPowerplant" = advFWT.powerplant_mode_as_electric

        prop.max_power = 111
        Assert.assertEqual(111, prop.max_power)
        prop.propeller_count = 2
        Assert.assertEqual(2, prop.propeller_count)
        prop.propeller_diameter = 2.1
        Assert.assertEqual(2.1, prop.propeller_diameter)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingExternalProp
    @category("Aircraft Tests")
    def test_AdvFixedWingExternalProp(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.ELECTRIC_POWERPLANT
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingExternalProp" = advFWT.powerplant_mode_as_external

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE, advFWT.powerplant_strategy)
        prop: "AdvancedFixedWingExternalProp" = advFWT.powerplant_mode_as_external

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.prop")
        with pytest.raises(Exception, match=RegexSubstringMatch("Failed to load the file.")):
            prop.set_filepath(nonexistingfilepath)

        filepath: str = TestBase.GetScenarioFile("advProp.prop")
        returnMsg: str = prop.set_filepath(filepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertTrue(prop.is_valid)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingPistonPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingPistonPowerplant(self):
        tolerance: float = 0.001

        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingPistonPowerplant" = advFWT.powerplant_mode_as_piston

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.PISTON_POWERPLANT
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.PISTON_POWERPLANT, advFWT.powerplant_strategy)
        prop: "AdvancedFixedWingPistonPowerplant" = advFWT.powerplant_mode_as_piston

        prop.max_sea_level_static_power = 111
        Assert.assertEqual(111, prop.max_sea_level_static_power)
        prop.critical_altitude = 50000
        Assert.assertEqual(50000, prop.critical_altitude)
        prop.propeller_count = 2
        Assert.assertEqual(2, prop.propeller_count)
        prop.propeller_diameter = 2.1
        Assert.assertEqual(2.1, prop.propeller_diameter)

        prop.max_sea_level_static_power = 100
        Assert.assertAlmostEqual(55, prop.fuel_flow, delta=tolerance)
        prop.fuel_flow = 70
        Assert.assertAlmostEqual(70, prop.fuel_flow, delta=tolerance)

        TestBase.Application.unit_preferences.reset_units()
        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbopropPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbopropPowerplant(self):
        tolerance: float = 0.001

        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingTurbopropPowerplant" = advFWT.powerplant_mode_as_turboprop

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOPROP
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOPROP, advFWT.powerplant_strategy)
        prop: "AdvancedFixedWingTurbopropPowerplant" = advFWT.powerplant_mode_as_turboprop

        prop.max_sea_level_static_power = 111
        Assert.assertEqual(111, prop.max_sea_level_static_power)
        prop.propeller_count = 2
        Assert.assertEqual(2, prop.propeller_count)
        prop.propeller_diameter = 2.1
        Assert.assertEqual(2.1, prop.propeller_diameter)

        prop.fuel_flow = 70
        Assert.assertAlmostEqual(70, prop.fuel_flow, delta=tolerance)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanHighBypassPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanHighBypassPowerplant(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_HIGH_BYPASS
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_HIGH_BYPASS, advFWT.powerplant_strategy)
        prop: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanLowBypassPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanLowBypassPowerplant(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_LOW_BYPASS
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_LOW_BYPASS, advFWT.powerplant_strategy)
        prop: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanLowBypassAfterburningPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanLowBypassAfterburningPowerplant(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_LOW_BYPASS_AFTERBURNING
        Assert.assertEqual(
            ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_LOW_BYPASS_AFTERBURNING, advFWT.powerplant_strategy
        )
        prop: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanTurbojetPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanTurbojetPowerplant(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOJET
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOJET, advFWT.powerplant_strategy)
        prop: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanTurbojetAfterburningPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanTurbojetAfterburningPowerplant(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOJET_AFTERBURNING
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOJET_AFTERBURNING, advFWT.powerplant_strategy)
        prop: "AdvancedFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbojetBasicABProp
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbojetBasicABProp(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingTurbojetBasicABProp" = advFWT.powerplant_mode_as_basic_turbojet

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOJET_BASIC_AB
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOJET_BASIC_AB, advFWT.powerplant_strategy)
        self.TestTurbojetBasicAB(advFWT.powerplant_mode_as_basic_turbojet)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanBasicABProp
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanBasicABProp(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingTurbofanBasicABProp" = advFWT.powerplant_mode_as_basic_turbofan

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_BASIC_AB
        Assert.assertEqual(ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_BASIC_AB, advFWT.powerplant_strategy)
        self.TestTurbofanBasicAB(advFWT.powerplant_mode_as_basic_turbofan)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingSubSuperHypersonicProp
    @category("Aircraft Tests")
    def test_AdvFixedWingSubSuperHypersonicProp(self):
        tempAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        advFWT: "AdvancedFixedWingTool" = tempAC.advanced_fixed_wing_tool

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.EXTERNAL_PROP_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            propTest: "AdvancedFixedWingSubSuperHypersonicProp" = advFWT.powerplant_mode_as_sub_super_hypersonic

        advFWT.powerplant_strategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.SUB_SUPER_HYPER_POWERPLANT
        Assert.assertEqual(
            ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.SUB_SUPER_HYPER_POWERPLANT, advFWT.powerplant_strategy
        )
        prop: "AdvancedFixedWingSubSuperHypersonicProp" = advFWT.powerplant_mode_as_sub_super_hypersonic

        prop.max_turbine_compression_temp = 901
        Assert.assertEqual(901, prop.max_turbine_compression_temp)
        prop.max_turbine_burner_temp = 1701
        Assert.assertEqual(1701, prop.max_turbine_burner_temp)
        prop.can_ram_compressor_pressure_ratio = 2.1
        Assert.assertEqual(2.1, prop.can_ram_compressor_pressure_ratio)
        prop.must_ram_compressor_pressure_ratio = 1.1
        Assert.assertEqual(1.1, prop.must_ram_compressor_pressure_ratio)
        prop.max_ram_scram_compression_temperature = 1561
        Assert.assertEqual(1561, prop.max_ram_scram_compression_temperature)
        prop.max_ram_scram_burner_total_temperature = 2001
        Assert.assertEqual(2001, prop.max_ram_scram_burner_total_temperature)

        prop.turbine_mode = TURBINE_MODE.TURBINE_MODE_DISABLED
        Assert.assertEqual(TURBINE_MODE.TURBINE_MODE_DISABLED, prop.turbine_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            fanTest: "AdvancedFixedWingTurbofanBasicABProp" = prop.turbine_mode_as_turbofan
        prop.ramjet_mode = RAMJET_MODE.RAMJET_MODE_DISABLED
        Assert.assertEqual(RAMJET_MODE.RAMJET_MODE_DISABLED, prop.ramjet_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            ramTest: "AdvancedFixedWingRamjetBasic" = prop.ramjet_mode_as_basic
        prop.scramjet_mode = SCRAMJET_MODE.SCRAMJET_MODE_DISABLED
        Assert.assertEqual(SCRAMJET_MODE.SCRAMJET_MODE_DISABLED, prop.scramjet_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            scramTest: "AdvancedFixedWingScramjetBasic" = prop.scramjet_mode_as_basic

        # /////////////////// Now test the turbojet turbine ////////////
        prop.turbine_mode = TURBINE_MODE.TURBINE_MODE_TURBOJET_BASIC_AB
        turbojet: "AdvancedFixedWingTurbojetBasicABProp" = prop.turbine_mode_as_turbojet
        self.TestTurbojetBasicAB(turbojet)
        prop.max_turbine_compression_temp = 901
        Assert.assertEqual(901, turbojet.max_compression_temp)
        prop.max_turbine_burner_temp = 1701
        Assert.assertEqual(1701, turbojet.max_burner_temp)

        # /////////////////// Now test the turbofan turbine ////////////
        prop.turbine_mode = TURBINE_MODE.TURBINE_MODE_TURBOFAN_BASIC_AB
        turbofan: "AdvancedFixedWingTurbofanBasicABProp" = prop.turbine_mode_as_turbofan
        self.TestTurbofanBasicAB(turbofan)
        prop.max_turbine_compression_temp = 901
        Assert.assertEqual(901, turbofan.max_compression_temp)
        prop.max_turbine_burner_temp = 1701
        Assert.assertEqual(1701, turbofan.max_burner_temp)

        # /////////////////// Now test the ramjet /////////////////////
        prop.ramjet_mode = RAMJET_MODE.RAMJET_MODE_BASIC
        ramjet: "AdvancedFixedWingRamjetBasic" = prop.ramjet_mode_as_basic

        ramjet.design_altitude = 60001
        Assert.assertEqual(60001, ramjet.design_altitude)
        ramjet.design_mach = 3.1
        Assert.assertEqual(3.1, ramjet.design_mach)
        ramjet.design_thrust = 100001
        Assert.assertEqual(100001, ramjet.design_thrust)

        prop.max_ram_scram_compression_temperature = 1561
        Assert.assertEqual(1561, ramjet.max_compression_temp)
        ramjet.max_compression_temp = 1562
        Assert.assertEqual(1562, ramjet.max_compression_temp)
        prop.max_ram_scram_burner_total_temperature = 2001
        Assert.assertEqual(2001, ramjet.max_burner_temp)
        ramjet.max_burner_temp = 2002
        Assert.assertEqual(2002, ramjet.max_burner_temp)

        ramjet.fuel_type = JET_FUEL_TYPE.KEROSENE_AFPROP
        self.TestFuelAFPROP(ramjet.fuel_mode_as_afprop)
        ramjet.fuel_type = JET_FUEL_TYPE.KEROSENE_CEA
        self.TestFuelCEA(ramjet.fuel_mode_as_cea)

        ramjet.fuel_type = JET_FUEL_TYPE.HYDROGEN
        Assert.assertEqual(JET_FUEL_TYPE.HYDROGEN, ramjet.fuel_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            afprop: "FuelModelKeroseneAFPROP" = ramjet.fuel_mode_as_afprop
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            cea: "FuelModelKeroseneCEA" = ramjet.fuel_mode_as_cea

        self.TestPropulsionEfficienciesRamScram(ramjet.efficiencies_and_losses)

        # /////////////////// Now test the scramjet /////////////////////
        prop.scramjet_mode = SCRAMJET_MODE.SCRAMJET_MODE_BASIC
        scramjet: "AdvancedFixedWingScramjetBasic" = prop.scramjet_mode_as_basic

        scramjet.design_altitude = 90001
        Assert.assertEqual(90001, scramjet.design_altitude)
        scramjet.design_mach = 6.1
        Assert.assertEqual(6.1, scramjet.design_mach)
        scramjet.design_thrust = 100001
        Assert.assertEqual(100001, scramjet.design_thrust)

        prop.max_ram_scram_compression_temperature = 1561
        Assert.assertEqual(1561, scramjet.max_compression_temp)
        scramjet.max_compression_temp = 1562
        Assert.assertEqual(1562, scramjet.max_compression_temp)
        prop.max_ram_scram_burner_total_temperature = 2001
        Assert.assertEqual(2001, scramjet.max_burner_temp)
        scramjet.max_burner_temp = 2002
        Assert.assertEqual(2002, scramjet.max_burner_temp)

        scramjet.fuel_type = JET_FUEL_TYPE.KEROSENE_AFPROP
        self.TestFuelAFPROP(scramjet.fuel_mode_as_afprop)
        scramjet.fuel_type = JET_FUEL_TYPE.KEROSENE_CEA
        self.TestFuelCEA(scramjet.fuel_mode_as_cea)

        scramjet.fuel_type = JET_FUEL_TYPE.HYDROGEN
        Assert.assertEqual(JET_FUEL_TYPE.HYDROGEN, scramjet.fuel_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            afprop: "FuelModelKeroseneAFPROP" = scramjet.fuel_mode_as_afprop
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            cea: "FuelModelKeroseneCEA" = scramjet.fuel_mode_as_cea

        self.TestPropulsionEfficienciesRamScram(scramjet.efficiencies_and_losses)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region PerformanceModelCategory
    @category("Aircraft Tests")
    def test_PerformanceModelCategory(self):
        acc: "AircraftAcceleration" = EarlyBoundTests.AG_AvtrAircraft.acceleration
        accAsCI: "ICatalogItem" = acc.get_as_catalog_item()

        Assert.assertEqual("Acceleration", accAsCI.name)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            accAsCI.name = ""
        Assert.assertEqual("Acceleration", accAsCI.name)

        isReadOnly: bool = accAsCI.is_read_only
        Assert.assertTrue(isReadOnly)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            accAsCI.remove()

        with pytest.raises(Exception):
            accAsCI.duplicate()

    # endregion

    # region BuiltInPerformanceModel
    @category("Aircraft Tests")
    def test_BuiltInPerformanceModel(self):
        acc: "AircraftAcceleration" = EarlyBoundTests.AG_AvtrAircraft.acceleration
        builtInAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()
        accAsCatalogItem: "ICatalogItem" = clr.CastAs(builtInAcc, ICatalogItem)

        Assert.assertEqual("Built-In Model", accAsCatalogItem.name)
        with pytest.raises(Exception):
            accAsCatalogItem.name = ""

        Assert.assertEqual("Built-In Model", accAsCatalogItem.name)

        isReadOnly: bool = accAsCatalogItem.is_read_only
        Assert.assertFalse(isReadOnly)
        with pytest.raises(Exception):
            accAsCatalogItem.remove()

    # endregion

    # region BasicAccelerationModel
    @category("Aircraft Tests")
    def test_BasicAccelerationModel(self):
        acc: "AircraftAcceleration" = EarlyBoundTests.AG_AvtrAircraft.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        levelTurns: "LevelTurns" = basicAcc.level_turns
        levelTurns.maneuver_mode = ACCEL_MANEUVER_MODE.ACCEL_MANEUVER_MODE_NORMAL
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "AeroPropManeuverModeHelper" = levelTurns.maneuver_mode_helper
        levelTurns.maneuver_mode = ACCEL_MANEUVER_MODE.ACCEL_MANEUVER_MODE_DENSITY_SCALE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "AeroPropManeuverModeHelper" = levelTurns.maneuver_mode_helper

        climbDescent: "ClimbAndDescentTransitions" = basicAcc.climb_and_descent_transitions
        climbDescent.maneuver_mode = ACCEL_MANEUVER_MODE.ACCEL_MANEUVER_MODE_NORMAL
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "AeroPropManeuverModeHelper" = climbDescent.maneuver_mode_helper
        climbDescent.maneuver_mode = ACCEL_MANEUVER_MODE.ACCEL_MANEUVER_MODE_DENSITY_SCALE
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "AeroPropManeuverModeHelper" = climbDescent.maneuver_mode_helper

    # endregion

    # region BasicAccelerationAero
    @category("Aircraft Tests")
    def test_BasicAccelerationAero(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "AircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AIRCRAFT_AERO_STRATEGY.AIRCRAFT_AERO_SIMPLE
        Assert.assertEqual(AIRCRAFT_AERO_STRATEGY.AIRCRAFT_AERO_SIMPLE, aero.aero_strategy)

        aero.lift_factor = 1.2
        Assert.assertEqual(1.2, aero.lift_factor)
        aero.drag_factor = 1.3
        Assert.assertEqual(1.3, aero.drag_factor)
        Assert.assertEqual(1.2, aero.lift_factor)

        aero.aero_strategy = AIRCRAFT_AERO_STRATEGY.AIRCRAFT_AERO_ADVANCED_MISSILE
        with pytest.raises(Exception):
            aero.lift_factor = 1.2
        with pytest.raises(Exception):
            aero.drag_factor = 1.3

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationSimpleAero
    @category("Aircraft Tests")
    def test_BasicAccelerationSimpleAero(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "AircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AIRCRAFT_AERO_STRATEGY.AIRCRAFT_AERO_SIMPLE

        simpleAero: "AircraftSimpleAero" = aero.mode_as_simple
        simpleAero.operating_mode = AERO_PROP_SIMPLE_MODE.HELICOPTER
        Assert.assertEqual(AERO_PROP_SIMPLE_MODE.HELICOPTER, simpleAero.operating_mode)

        simpleAero.s_reference = 5
        Assert.assertEqual(5, simpleAero.s_reference)
        simpleAero.cl_max = 3.1
        Assert.assertEqual(3.1, simpleAero.cl_max)
        simpleAero.cd = 0.05
        Assert.assertEqual(0.05, simpleAero.cd)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationBasicFixedWingAero
    @category("Aircraft Tests")
    def test_BasicAccelerationBasicFixedWingAero(self):
        tolerance: float = 1e-06

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "AircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AIRCRAFT_AERO_STRATEGY.AIRCRAFT_AERO_BASIC_FIXED_WING

        bfwAero: "AircraftBasicFixedWingAero" = aero.mode_as_basic_fixed_wing

        bfwAero.forward_flight_reference_area = 0.05
        Assert.assertEqual(0.05, bfwAero.forward_flight_reference_area)
        bfwAero.forward_flight_use_compressible_flow = False
        Assert.assertEqual(False, bfwAero.forward_flight_use_compressible_flow)
        bfwAero.forward_flight_cl0 = 0.01
        Assert.assertEqual(0.01, bfwAero.forward_flight_cl0)
        bfwAero.forward_flight_cl_alpha = 0.07
        Assert.assertAlmostEqual(0.07, bfwAero.forward_flight_cl_alpha, delta=tolerance)
        bfwAero.forward_flight_min_aoa = -89
        minAoA: typing.Any = bfwAero.forward_flight_min_aoa
        Assert.assertAlmostEqual(-89, float(minAoA), delta=tolerance)
        bfwAero.forward_flight_max_aoa = 89
        maxAoA: typing.Any = bfwAero.forward_flight_max_aoa
        Assert.assertAlmostEqual(89, float(maxAoA), delta=tolerance)
        bfwAero.forward_flight_cd0 = 0.021
        Assert.assertEqual(0.021, bfwAero.forward_flight_cd0)
        bfwAero.forward_flight_k = 0.01
        Assert.assertEqual(0.01, bfwAero.forward_flight_k)

        bfwAero.takeoff_landing_reference_area = 0.06
        Assert.assertEqual(0.06, bfwAero.takeoff_landing_reference_area)
        bfwAero.takeoff_landing_use_compressible_flow = False
        Assert.assertEqual(False, bfwAero.takeoff_landing_use_compressible_flow)
        bfwAero.takeoff_landing_cl0 = 0.02
        Assert.assertEqual(0.02, bfwAero.takeoff_landing_cl0)
        bfwAero.takeoff_landing_cl_alpha = 0.08
        Assert.assertAlmostEqual(0.08, bfwAero.takeoff_landing_cl_alpha, delta=tolerance)
        bfwAero.takeoff_landing_min_aoa = -88
        minAoA = bfwAero.takeoff_landing_min_aoa
        Assert.assertAlmostEqual(-88, float(minAoA), delta=tolerance)
        bfwAero.takeoff_landing_max_aoa = 88
        maxAoA = bfwAero.takeoff_landing_max_aoa
        Assert.assertAlmostEqual(88, float(maxAoA), delta=tolerance)
        bfwAero.takeoff_landing_cd0 = 0.022
        Assert.assertEqual(0.022, bfwAero.takeoff_landing_cd0)
        bfwAero.takeoff_landing_k = 0.02
        Assert.assertEqual(0.02, bfwAero.takeoff_landing_k)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationExternalAero
    @category("Aircraft Tests")
    def test_BasicAccelerationExternalAero(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "AircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AIRCRAFT_AERO_STRATEGY.AIRCRAFT_AERO_EXTERNAL_FILE

        externalAero: "AircraftExternalAero" = aero.mode_as_external
        Assert.assertIs(None, externalAero.forward_flight_filepath)
        Assert.assertIs(None, externalAero.takeoff_landing_filepath)
        with pytest.raises(Exception):
            externalAero.set_forward_flight_filepath("")
        with pytest.raises(Exception):
            externalAero.set_takeoff_landing_filepath("")
        with pytest.raises(Exception):
            externalAero.reload_forward_flight_file()
        with pytest.raises(Exception):
            externalAero.reload_takeoff_landing_file()
        Assert.assertEqual(False, externalAero.is_forward_flight_valid)
        Assert.assertEqual(False, externalAero.is_takeoff_landing_valid)

        Assert.assertTrue(externalAero.can_set_forward_flight_reference_area)
        externalAero.forward_flight_reference_area = 0.05
        Assert.assertEqual(0.05, externalAero.forward_flight_reference_area)
        Assert.assertTrue(externalAero.can_set_takeoff_landing_reference_area)
        externalAero.takeoff_landing_reference_area = 0.07
        Assert.assertEqual(0.07, externalAero.takeoff_landing_reference_area)

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.aero")
        with pytest.raises(Exception, match=RegexSubstringMatch("Failed to load the file.")):
            externalAero.set_forward_flight_filepath(nonexistingfilepath)

        aeroFilepath: str = TestBase.GetScenarioFile("simpleAero.aero")
        returnMsg: str = externalAero.set_forward_flight_filepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalAero.can_set_forward_flight_reference_area)
        with pytest.raises(Exception):
            externalAero.forward_flight_reference_area = 0.05
        Assert.assertTrue(externalAero.is_forward_flight_valid)

        returnMsg2: str = externalAero.set_takeoff_landing_filepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg2))
        Assert.assertEqual(False, externalAero.can_set_takeoff_landing_reference_area)
        with pytest.raises(Exception):
            externalAero.takeoff_landing_reference_area = 0.07
        Assert.assertTrue(externalAero.is_takeoff_landing_valid)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationAdvancedMissileAero
    @category("Aircraft Tests")
    def test_BasicAccelerationAdvancedMissileAero(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "AircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AIRCRAFT_AERO_STRATEGY.AIRCRAFT_AERO_ADVANCED_MISSILE
        self.AdvancedMissileAero(aero.mode_as_advanced_missile)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationProp
    @category("Aircraft Tests")
    def test_BasicAccelerationProp(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "AircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_SIMPLE
        Assert.assertEqual(AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_SIMPLE, prop.prop_strategy)
        with pytest.raises(Exception):
            prop.lift_factor = 1.2
        with pytest.raises(Exception):
            prop.drag_factor = 1.3

        prop.prop_strategy = AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_BASIC_FIXED_WING
        Assert.assertEqual(AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_BASIC_FIXED_WING, prop.prop_strategy)

        prop.lift_factor = 1.2
        Assert.assertEqual(1.2, prop.lift_factor)
        prop.drag_factor = 1.3
        Assert.assertEqual(1.3, prop.drag_factor)
        Assert.assertEqual(1.2, prop.lift_factor)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationSimpleProp
    @category("Aircraft Tests")
    def test_BasicAccelerationSimpleProp(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "AircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_SIMPLE
        simpleProp: "AircraftSimpleProp" = prop.mode_as_simple

        simpleProp.max_thrust_accel = 0.6
        Assert.assertEqual(0.6, simpleProp.max_thrust_accel)
        simpleProp.min_thrust_decel = 0.4
        Assert.assertEqual(0.4, simpleProp.min_thrust_decel)

        Assert.assertEqual(False, simpleProp.use_density_scaling)
        simpleProp.set_density_scaling(True, 0.02)
        Assert.assertTrue(simpleProp.use_density_scaling)
        Assert.assertEqual(0.02, simpleProp.density_ratio_exponent)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationExternalProp
    @category("Aircraft Tests")
    def test_BasicAccelerationExternalProp(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "AircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_EXTERNAL_FILE

        externalProp: "AircraftExternalProp" = prop.mode_as_external
        Assert.assertIs(None, externalProp.prop_filepath)
        with pytest.raises(Exception):
            externalProp.set_prop_filepath("")
        with pytest.raises(Exception):
            externalProp.reload_prop_file()
        Assert.assertEqual(False, externalProp.is_valid)

        Assert.assertTrue(externalProp.can_set_accel_decel)
        externalProp.max_thrust_accel = 0.6
        Assert.assertEqual(0.6, externalProp.max_thrust_accel)
        externalProp.min_thrust_decel = 0.4
        Assert.assertEqual(0.4, externalProp.min_thrust_decel)

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.prop")
        with pytest.raises(Exception, match=RegexSubstringMatch("Failed to load the file.")):
            externalProp.set_prop_filepath(nonexistingfilepath)

        propFilepath: str = TestBase.GetScenarioFile("simpleProp.prop")
        returnMsg: str = externalProp.set_prop_filepath(propFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalProp.can_set_accel_decel)
        with pytest.raises(Exception):
            externalProp.max_thrust_accel = 0.6
        Assert.assertTrue(externalProp.is_valid)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationBasicFixedWingProp
    @category("Aircraft Tests")
    def test_BasicAccelerationBasicFixedWingProp(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "AircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_BASIC_FIXED_WING

        bfwProp: "AircraftBasicFixedWingProp" = prop.mode_as_basic_fixed_wing
        bfwProp.propulsion_mode = BASIC_FIXED_WING_PROP_MODE.SPECIFY_THRUST
        Assert.assertEqual(BASIC_FIXED_WING_PROP_MODE.SPECIFY_THRUST, bfwProp.propulsion_mode)
        with pytest.raises(Exception):
            bfwProp.propeller_count = 1
        with pytest.raises(Exception):
            bfwProp.propeller_diameter = 1
        with pytest.raises(Exception):
            bfwProp.propeller_rpm = 1

        bfwProp.min_power_thrust = 1
        Assert.assertEqual(1, bfwProp.min_power_thrust)
        bfwProp.max_power_thrust = 100000
        Assert.assertEqual(100000, bfwProp.max_power_thrust)

        bfwProp.propulsion_mode = BASIC_FIXED_WING_PROP_MODE.SPECIFY_POWER
        bfwProp.propeller_count = 2
        Assert.assertEqual(2, bfwProp.propeller_count)
        bfwProp.propeller_diameter = 4
        Assert.assertEqual(4, bfwProp.propeller_diameter)
        bfwProp.propeller_rpm = 3000
        Assert.assertEqual(3000, bfwProp.propeller_rpm)

        bfwProp.min_power_thrust = 2
        Assert.assertEqual(2, bfwProp.min_power_thrust)
        bfwProp.max_power_thrust = 99000
        Assert.assertEqual(99000, bfwProp.max_power_thrust)
        bfwProp.min_fuel_flow = 123
        Assert.assertAlmostEqual(123, bfwProp.min_fuel_flow, delta=tolerance)
        bfwProp.max_fuel_flow = 12345
        Assert.assertAlmostEqual(12345, bfwProp.max_fuel_flow, delta=tolerance)

        bfwProp.max_thrust_accel = 0.6
        Assert.assertEqual(0.6, bfwProp.max_thrust_accel)
        bfwProp.min_thrust_decel = 0.4
        Assert.assertEqual(0.4, bfwProp.min_thrust_decel)

        Assert.assertEqual(False, bfwProp.use_density_scaling)
        bfwProp.set_density_scaling(True, 0.02)
        Assert.assertTrue(bfwProp.use_density_scaling)
        Assert.assertEqual(0.02, bfwProp.density_ratio_exponent)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationRocketProp
    @category("Aircraft Tests")
    def test_BasicAccelerationRocketProp(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "AircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_MISSILE_ROCKET
        rocketProp: "MissileRocketProp" = prop.mode_as_rocket

        rocketProp.nozzle_expansion_ratio = 7.1
        Assert.assertEqual(7.1, rocketProp.nozzle_expansion_ratio)
        rocketProp.nozzle_exit_diameter = 0.123
        Assert.assertEqual(0.123, rocketProp.nozzle_exit_diameter)
        rocketProp.propellant_specific_heat_ratio = 1.2
        Assert.assertEqual(1.2, rocketProp.propellant_specific_heat_ratio)
        rocketProp.propellant_characteristic_velocity = 3120
        Assert.assertAlmostEqual(3120, rocketProp.propellant_characteristic_velocity, delta=tolerance)
        rocketProp.combustion_chamber_pressure = 13000000.0
        Assert.assertEqual(13000000.0, rocketProp.combustion_chamber_pressure)

        rocketProp.use_boost_sustain_mode = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            rocketProp.boost_fuel_fraction = 60
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            rocketProp.boost_chamber_pressure = 21000000.0
        rocketProp.use_boost_sustain_mode = True
        Assert.assertTrue(rocketProp.use_boost_sustain_mode)
        rocketProp.boost_fuel_fraction = 60
        Assert.assertEqual(60, rocketProp.boost_fuel_fraction)
        rocketProp.boost_chamber_pressure = 21000000.0
        Assert.assertEqual(21000000.0, rocketProp.boost_chamber_pressure)

        rocketProp.no_thrust_when_no_fuel = False
        Assert.assertEqual(False, rocketProp.no_thrust_when_no_fuel)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationRamjetProp
    @category("Aircraft Tests")
    def test_BasicAccelerationRamjetProp(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "AircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_MISSILE_RAMJET
        ramjetProp: "MissileRamjetProp" = prop.mode_as_ramjet

        ramjetProp.design_altitude = 5000
        Assert.assertEqual(5000, ramjetProp.design_altitude)
        ramjetProp.design_mach = 3
        Assert.assertEqual(3, ramjetProp.design_mach)
        ramjetProp.design_thrust = 30000
        Assert.assertEqual(30000, ramjetProp.design_thrust)
        ramjetProp.engine_temp = 2000
        Assert.assertEqual(2000, ramjetProp.engine_temp)

        ramjetProp.fuel_heating_value = 41500000
        Assert.assertEqual(41500000, ramjetProp.fuel_heating_value)
        ramjetProp.inlet_pressure_ratio = 0.9
        Assert.assertEqual(0.9, ramjetProp.inlet_pressure_ratio)
        ramjetProp.burner_pressure_ratio = 0.8
        Assert.assertEqual(0.8, ramjetProp.burner_pressure_ratio)
        ramjetProp.nozzle_pressure_ratio = 0.7
        Assert.assertEqual(0.7, ramjetProp.nozzle_pressure_ratio)
        ramjetProp.p_0over_p9 = 0.5
        Assert.assertEqual(0.5, ramjetProp.p_0over_p9)
        ramjetProp.burner_efficiency = 95
        Assert.assertEqual(95, ramjetProp.burner_efficiency)

        ramjetProp.no_thrust_when_no_fuel = False
        Assert.assertEqual(False, ramjetProp.no_thrust_when_no_fuel)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationTurbojetProp
    @category("Aircraft Tests")
    def test_BasicAccelerationTurbojetProp(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        acc: "AircraftAcceleration" = newAC.acceleration
        basicAcc: "AircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "AircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AIRCRAFT_PROP_STRATEGY.AIRCRAFT_PROP_MISSILE_TURBOJET
        turboProp: "MissileTurbojetProp" = prop.mode_as_turbojet

        turboProp.design_altitude = 5000
        Assert.assertEqual(5000, turboProp.design_altitude)
        turboProp.design_mach = 3
        Assert.assertEqual(3, turboProp.design_mach)
        turboProp.design_thrust = 30000
        Assert.assertEqual(30000, turboProp.design_thrust)
        turboProp.turbine_temp = 2000
        Assert.assertEqual(2000, turboProp.turbine_temp)
        turboProp.compressor_pressure_ratio = 9
        Assert.assertEqual(9, turboProp.compressor_pressure_ratio)

        turboProp.fuel_heating_value = 41500000
        Assert.assertEqual(41500000, turboProp.fuel_heating_value)
        turboProp.inlet_subsonic_pressure_ratio = 0.9
        Assert.assertEqual(0.9, turboProp.inlet_subsonic_pressure_ratio)
        turboProp.burner_pressure_ratio = 0.8
        Assert.assertEqual(0.8, turboProp.burner_pressure_ratio)
        turboProp.nozzle_pressure_ratio = 0.7
        Assert.assertEqual(0.7, turboProp.nozzle_pressure_ratio)
        turboProp.p_0over_p9 = 0.5
        Assert.assertEqual(0.5, turboProp.p_0over_p9)
        turboProp.compressor_efficiency = 99
        Assert.assertEqual(99, turboProp.compressor_efficiency)
        turboProp.turbine_efficiency = 98
        Assert.assertEqual(98, turboProp.turbine_efficiency)
        turboProp.burner_efficiency = 97
        Assert.assertEqual(97, turboProp.burner_efficiency)
        turboProp.mechanical_efficiency = 96
        Assert.assertEqual(96, turboProp.mechanical_efficiency)

        turboProp.no_thrust_when_no_fuel = False
        Assert.assertEqual(False, turboProp.no_thrust_when_no_fuel)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedAccelerationModel
    @category("Aircraft Tests")
    def test_AdvancedAccelerationModel(self):
        acc: "AircraftAcceleration" = EarlyBoundTests.AG_AvtrAircraft.acceleration
        accAsCatalogItem: "ICatalogItem" = acc.get_as_catalog_item()
        accModelNames = accAsCatalogItem.child_names
        count: int = Array.Length(accModelNames)
        advAcc: "AircraftAdvancedAccelerationModel" = clr.CastAs(
            accAsCatalogItem.add_child_of_type("Advanced Acceleration Model", "AdvAcceleration Model Name"),
            AircraftAdvancedAccelerationModel,
        )

        accModelNames = accAsCatalogItem.child_names
        count += 1
        Assert.assertEqual(count, Array.Length(accModelNames))
        Assert.assertEqual("AdvAcceleration Model Name", accModelNames[0])

        accMode: "AircraftAccelerationMode" = advAcc.acceleration_mode
        accMode.accel_mode = ACCELERATION_ADVANCED_ACCEL_MODE.ACCEL_MODE_MAX_ACCEL
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            accMode.accel_g = 1

        advAcc.get_as_catalog_item().remove()
        accModelNames = accAsCatalogItem.child_names
        count -= 1
        Assert.assertEqual(count, Array.Length(accModelNames))

    # endregion

    # region BasicClimbModel
    @category("Aircraft Tests")
    def test_BasicClimbModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        climb: "AircraftClimb" = newAC.climb
        basicClimb: "AircraftBasicClimbModel" = climb.get_built_in_model()

        basicClimb.ceiling_altitude = 70001
        Assert.assertEqual(70001, basicClimb.ceiling_altitude)

        basicClimb.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, basicClimb.airspeed_type)
        Assert.assertAlmostEqual(251, basicClimb.airspeed, delta=tolerance)
        basicClimb.set_airspeed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, basicClimb.airspeed_type)
        Assert.assertEqual(0.4, basicClimb.airspeed)

        basicClimb.altitude_rate = 4001
        Assert.assertAlmostEqual(4001, basicClimb.altitude_rate, delta=tolerance)

        basicClimb.use_aero_prop_fuel = True
        Assert.assertTrue(basicClimb.use_aero_prop_fuel)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            testVal: bool = basicClimb.scale_fuel_flow_by_non_std_density
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicClimb.scale_fuel_flow_by_non_std_density = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            testVal: float = basicClimb.fuel_flow
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicClimb.fuel_flow = 1

        basicClimb.use_aero_prop_fuel = False
        basicClimb.fuel_flow = 9000
        Assert.assertAlmostEqual(9000, basicClimb.fuel_flow, delta=tolerance)

        basicClimb.enable_relative_airspeed_tolerance = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            testVal: float = basicClimb.relative_airspeed_tolerance
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicClimb.relative_airspeed_tolerance = 1

        basicClimb.enable_relative_airspeed_tolerance = True
        basicClimb.relative_airspeed_tolerance = 0.06
        Assert.assertEqual(0.06, basicClimb.relative_airspeed_tolerance)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedClimbModel
    @category("Aircraft Tests")
    def test_AdvancedClimbModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        climb: "AircraftClimb" = newAC.climb
        climb.get_as_catalog_item().add_child_of_type("Advanced Climb Model", "Adv Climb")
        advClimb: "AircraftAdvancedClimbModel" = climb.get_advanced_climb_by_name("Adv Climb")

        advClimb.climb_speed_type = CLIMB_SPEED_TYPE.CLIMB_SPEED_MIN_FUEL
        Assert.assertEqual(CLIMB_SPEED_TYPE.CLIMB_SPEED_MIN_FUEL, advClimb.climb_speed_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advClimb.set_climb_override_airspeed(AIRSPEED_TYPE.TAS, 251)

        advClimb.climb_speed_type = CLIMB_SPEED_TYPE.CLIMB_SPEED_OVERRIDE
        advClimb.set_climb_override_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, advClimb.climb_override_airspeed_type)
        Assert.assertAlmostEqual(251, advClimb.climb_override_airspeed, delta=tolerance)

        advClimb.set_climb_override_airspeed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, advClimb.climb_override_airspeed_type)
        Assert.assertEqual(0.4, advClimb.climb_override_airspeed)

        with pytest.raises(Exception, match=RegexSubstringMatch("not enabled")):
            advClimb.use_afterburner = True
        Assert.assertEqual(False, advClimb.use_afterburner)

        advClimb.use_airspeed_limit = False
        Assert.assertEqual(False, advClimb.use_airspeed_limit)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advClimb.altitude_limit = 9000
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advClimb.set_airspeed_limit(AIRSPEED_TYPE.TAS, 251)

        advClimb.use_airspeed_limit = True
        advClimb.altitude_limit = 9000
        Assert.assertEqual(9000, advClimb.altitude_limit)
        advClimb.set_airspeed_limit(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, advClimb.airspeed_limit_type)
        Assert.assertAlmostEqual(251, advClimb.airspeed_limit, delta=tolerance)
        advClimb.set_airspeed_limit(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, advClimb.airspeed_limit_type)
        Assert.assertEqual(0.4, advClimb.airspeed_limit)

        advClimb.use_flight_path_angle_limit = False
        Assert.assertEqual(False, advClimb.use_flight_path_angle_limit)
        advClimb.set_flight_path_angle(31)
        Assert.assertTrue(advClimb.use_flight_path_angle_limit)
        fpa: typing.Any = advClimb.flight_path_angle
        Assert.assertEqual(31, float(fpa))

        advClimb.compute_delta_altitude = 1001
        Assert.assertEqual(1001, advClimb.compute_delta_altitude)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicCruiseModel
    @category("Aircraft Tests")
    def test_BasicCruiseModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        cruise: "AircraftCruise" = newAC.cruise
        basicCruise: "AircraftBasicCruiseModel" = cruise.get_built_in_model()

        basicCruise.ceiling_altitude = 20000
        Assert.assertEqual(20000, basicCruise.ceiling_altitude)
        basicCruise.default_cruise_altitude = 10000
        Assert.assertEqual(10000, basicCruise.default_cruise_altitude)
        basicCruise.airspeed_type = AIRSPEED_TYPE.CAS
        Assert.assertEqual(AIRSPEED_TYPE.CAS, basicCruise.airspeed_type)
        basicCruise.use_aero_prop_fuel = False
        Assert.assertEqual(False, basicCruise.use_aero_prop_fuel)
        basicCruise.scale_fuel_flow_by_non_std_density = True
        Assert.assertTrue(basicCruise.scale_fuel_flow_by_non_std_density)

        basicCruise.min_airspeed = 101
        Assert.assertAlmostEqual(101, basicCruise.min_airspeed, delta=tolerance)
        basicCruise.max_endurance_airspeed = 102
        Assert.assertEqual(102, basicCruise.max_endurance_airspeed)
        basicCruise.max_airspeed = 553
        Assert.assertAlmostEqual(553, basicCruise.max_airspeed, delta=tolerance)
        basicCruise.max_range_airspeed = 104
        Assert.assertEqual(104, basicCruise.max_range_airspeed)
        basicCruise.max_perf_airspeed = 105
        Assert.assertEqual(105, basicCruise.max_perf_airspeed)

        basicCruise.airspeed_type = AIRSPEED_TYPE.MACH
        Assert.assertEqual(AIRSPEED_TYPE.MACH, basicCruise.airspeed_type)

        # Check that the airspeed was converted properly
        # Assert.AreEqual(0.158222, basicCruise.MinAirspeed, tolerance);

        basicCruise.min_airspeed = 0.1
        Assert.assertEqual(0.1, basicCruise.min_airspeed)
        basicCruise.max_endurance_airspeed = 0.12
        Assert.assertEqual(0.12, basicCruise.max_endurance_airspeed)
        basicCruise.max_airspeed = 0.96
        Assert.assertEqual(0.96, basicCruise.max_airspeed)
        basicCruise.max_range_airspeed = 0.14
        Assert.assertEqual(0.14, basicCruise.max_range_airspeed)
        basicCruise.max_perf_airspeed = 0.15
        Assert.assertEqual(0.15, basicCruise.max_perf_airspeed)

        basicCruise.min_airspeed_fuel_flow = 101.5
        Assert.assertEqual(101.5, basicCruise.min_airspeed_fuel_flow)
        basicCruise.max_endurance_fuel_flow = 102.5
        Assert.assertEqual(102.5, basicCruise.max_endurance_fuel_flow)
        basicCruise.max_airspeed_fuel_flow = 553.5
        Assert.assertAlmostEqual(553.5, basicCruise.max_airspeed_fuel_flow, delta=tolerance)
        basicCruise.max_range_fuel_flow = 104.5
        Assert.assertEqual(104.5, basicCruise.max_range_fuel_flow)
        basicCruise.max_perf_airspeed_fuel_flow = 105.5
        Assert.assertEqual(105.5, basicCruise.max_perf_airspeed_fuel_flow)

        basicCruise.use_aero_prop_fuel = True
        Assert.assertTrue(basicCruise.use_aero_prop_fuel)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            basicCruise.scale_fuel_flow_by_non_std_density = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            basicCruise.min_airspeed_fuel_flow = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            basicCruise.max_endurance_fuel_flow = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            basicCruise.max_airspeed_fuel_flow = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            basicCruise.max_range_fuel_flow = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            basicCruise.max_perf_airspeed_fuel_flow = 100

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedCruiseModel
    @category("Aircraft Tests")
    def test_AdvancedCruiseModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        cruise: "AircraftCruise" = newAC.cruise
        cruise.get_as_catalog_item().add_child_of_type("Advanced Cruise Model", "Adv Cruise")
        advCruise: "AircraftAdvancedCruiseModel" = cruise.get_advanced_cruise_by_name("Adv Cruise")

        advCruise.default_cruise_altitude = 10001
        Assert.assertEqual(10001, advCruise.default_cruise_altitude)
        advCruise.max_perf_airspeed = CRUISE_MAX_PERF_SPEED_TYPE.MAX_SPEED_DRY_THRUST
        Assert.assertEqual(CRUISE_MAX_PERF_SPEED_TYPE.MAX_SPEED_DRY_THRUST, advCruise.max_perf_airspeed)

        advCruise.use_airspeed_limit = False
        Assert.assertEqual(False, advCruise.use_airspeed_limit)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advCruise.altitude_limit = 9000
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advCruise.set_airspeed_limit(AIRSPEED_TYPE.TAS, 251)

        advCruise.use_airspeed_limit = True
        advCruise.altitude_limit = 9000
        Assert.assertEqual(9000, advCruise.altitude_limit)
        advCruise.set_airspeed_limit(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, advCruise.airspeed_limit_type)
        Assert.assertAlmostEqual(251, advCruise.airspeed_limit, delta=tolerance)
        advCruise.set_airspeed_limit(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, advCruise.airspeed_limit_type)
        Assert.assertEqual(0.4, advCruise.airspeed_limit)

        advCruise.compute_delta_downrange = 11
        Assert.assertEqual(11, advCruise.compute_delta_downrange)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicDescentModel
    @category("Aircraft Tests")
    def test_BasicDescentModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        descent: "AircraftDescent" = newAC.descent
        basicDescent: "AircraftBasicDescentModel" = descent.get_built_in_model()

        basicDescent.ceiling_altitude = 70001
        Assert.assertEqual(70001, basicDescent.ceiling_altitude)

        basicDescent.set_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, basicDescent.airspeed_type)
        Assert.assertAlmostEqual(251, basicDescent.airspeed, delta=tolerance)
        basicDescent.set_airspeed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, basicDescent.airspeed_type)
        Assert.assertEqual(0.4, basicDescent.airspeed)

        basicDescent.altitude_rate = -4001
        Assert.assertAlmostEqual(-4001, basicDescent.altitude_rate, delta=tolerance)

        basicDescent.use_aero_prop_fuel = True
        Assert.assertTrue(basicDescent.use_aero_prop_fuel)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            testVal: bool = basicDescent.scale_fuel_flow_by_non_std_density
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicDescent.scale_fuel_flow_by_non_std_density = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            testVal: float = basicDescent.fuel_flow
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicDescent.fuel_flow = 1

        basicDescent.use_aero_prop_fuel = False
        basicDescent.fuel_flow = 9000
        Assert.assertAlmostEqual(9000, basicDescent.fuel_flow, delta=tolerance)

        basicDescent.enable_relative_airspeed_tolerance = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            testVal: float = basicDescent.relative_airspeed_tolerance
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicDescent.relative_airspeed_tolerance = 1

        basicDescent.enable_relative_airspeed_tolerance = True
        basicDescent.relative_airspeed_tolerance = 0.06
        Assert.assertEqual(0.06, basicDescent.relative_airspeed_tolerance)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedDescentModel
    @category("Aircraft Tests")
    def test_AdvancedDescentModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        descent: "AircraftDescent" = newAC.descent
        descent.get_as_catalog_item().add_child_of_type("Advanced Descent Model", "Adv Descent")
        advDescent: "AircraftAdvancedDescentModel" = descent.get_advanced_descent_by_name("Adv Descent")

        advDescent.descent_speed_type = DESCENT_SPEED_TYPE.DESCENT_MAX_RANGE_CRUISE
        Assert.assertEqual(DESCENT_SPEED_TYPE.DESCENT_MAX_RANGE_CRUISE, advDescent.descent_speed_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advDescent.descent_stall_speed_ratio = 1.2
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advDescent.set_descent_override_airspeed(AIRSPEED_TYPE.TAS, 251)

        advDescent.descent_speed_type = DESCENT_SPEED_TYPE.DESCENT_STALL_SPEED_RATIO
        advDescent.descent_stall_speed_ratio = 1.2
        Assert.assertEqual(1.2, advDescent.descent_stall_speed_ratio)

        advDescent.descent_speed_type = DESCENT_SPEED_TYPE.DESCENT_SPEED_OVERRIDE
        advDescent.set_descent_override_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, advDescent.descent_override_airspeed_type)
        Assert.assertAlmostEqual(251, advDescent.descent_override_airspeed, delta=tolerance)

        advDescent.set_descent_override_airspeed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, advDescent.descent_override_airspeed_type)
        Assert.assertEqual(0.4, advDescent.descent_override_airspeed)

        advDescent.speedbrakes = 95
        Assert.assertEqual(95, advDescent.speedbrakes)

        advDescent.use_airspeed_limit = False
        Assert.assertEqual(False, advDescent.use_airspeed_limit)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advDescent.altitude_limit = 9000
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            advDescent.set_airspeed_limit(AIRSPEED_TYPE.TAS, 251)

        advDescent.use_airspeed_limit = True
        advDescent.altitude_limit = 9000
        Assert.assertEqual(9000, advDescent.altitude_limit)
        advDescent.set_airspeed_limit(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, advDescent.airspeed_limit_type)
        Assert.assertAlmostEqual(251, advDescent.airspeed_limit, delta=tolerance)
        advDescent.set_airspeed_limit(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, advDescent.airspeed_limit_type)
        Assert.assertEqual(0.4, advDescent.airspeed_limit)

        advDescent.compute_delta_altitude = 1001
        Assert.assertEqual(1001, advDescent.compute_delta_altitude)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicLandingModel
    @category("Aircraft Tests")
    def test_BasicLandingModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        landing: "AircraftLanding" = newAC.landing
        basicLanding: "AircraftBasicLandingModel" = landing.get_built_in_model()

        basicLanding.set_landing_speed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, basicLanding.landing_speed_type)
        Assert.assertAlmostEqual(251, basicLanding.landing_speed, delta=tolerance)
        basicLanding.set_landing_speed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, basicLanding.landing_speed_type)
        Assert.assertEqual(0.4, basicLanding.landing_speed)

        basicLanding.sea_level_ground_roll = 6
        Assert.assertAlmostEqual(6, basicLanding.sea_level_ground_roll, delta=tolerance)

        basicLanding.use_aero_prop_fuel = True
        Assert.assertTrue(basicLanding.use_aero_prop_fuel)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicLanding.scale_fuel_flow_by_non_std_density = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicLanding.fuel_flow = 9000

        basicLanding.use_aero_prop_fuel = False

        basicLanding.scale_fuel_flow_by_non_std_density = True
        Assert.assertTrue(basicLanding.scale_fuel_flow_by_non_std_density)

        basicLanding.fuel_flow = 9000
        Assert.assertAlmostEqual(9000, basicLanding.fuel_flow, delta=tolerance)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedLandingModel
    @category("Aircraft Tests")
    def test_AdvancedLandingModel(self):
        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        landing: "AircraftLanding" = newAC.landing
        landing.get_as_catalog_item().add_child_of_type("Advanced Landing Model", "Adv Landing")
        advLanding: "AircraftAdvancedLandingModel" = landing.get_advanced_landing_by_name("Adv Landing")

        advLanding.landing_speed_mode = TAKEOFF_LANDING_SPEED_MODE.TAKEOFF_LANDING_ANGLE_OF_ATTACK
        Assert.assertEqual(TAKEOFF_LANDING_SPEED_MODE.TAKEOFF_LANDING_ANGLE_OF_ATTACK, advLanding.landing_speed_mode)

        advLanding.set_angle_of_attack(11)
        angle: typing.Any = advLanding.angle_of_attack
        Assert.assertEqual(11, float(angle))

        advLanding.set_stall_speed_ratio(1.2)
        Assert.assertEqual(TAKEOFF_LANDING_SPEED_MODE.TAKEOFF_LANDING_STALL_SPEED_RATIO, advLanding.landing_speed_mode)
        Assert.assertEqual(1.2, advLanding.stall_speed_ratio)

        advLanding.flaps = 99
        Assert.assertEqual(99, advLanding.flaps)

        advLanding.speedbrakes = 98
        Assert.assertEqual(98, advLanding.speedbrakes)

        advLanding.braking_decel_g = 0.4
        Assert.assertEqual(0.4, advLanding.braking_decel_g)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicTakeoffModel
    @category("Aircraft Tests")
    def test_BasicTakeoffModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        takeoff: "AircraftTakeoff" = newAC.takeoff
        basicTakeoff: "AircraftBasicTakeoffModel" = takeoff.get_built_in_model()

        basicTakeoff.set_takeoff_speed(AIRSPEED_TYPE.TAS, 151)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, basicTakeoff.takeoff_speed_type)
        Assert.assertAlmostEqual(151, basicTakeoff.takeoff_speed, delta=tolerance)
        basicTakeoff.set_takeoff_speed(AIRSPEED_TYPE.MACH, 0.3)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, basicTakeoff.takeoff_speed_type)
        Assert.assertEqual(0.3, basicTakeoff.takeoff_speed)

        basicTakeoff.sea_level_ground_roll = 6
        Assert.assertAlmostEqual(6, basicTakeoff.sea_level_ground_roll, delta=tolerance)

        basicTakeoff.set_departure_speed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, basicTakeoff.departure_speed_type)
        Assert.assertAlmostEqual(251, basicTakeoff.departure_speed, delta=tolerance)
        basicTakeoff.set_departure_speed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, basicTakeoff.departure_speed_type)
        Assert.assertEqual(0.4, basicTakeoff.departure_speed)

        basicTakeoff.use_aero_prop_fuel = True
        Assert.assertTrue(basicTakeoff.use_aero_prop_fuel)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicTakeoff.scale_fuel_flow_by_non_std_density = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicTakeoff.accel_fuel_flow = 8000
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            basicTakeoff.departure_fuel_flow = 9000

        basicTakeoff.use_aero_prop_fuel = False

        basicTakeoff.scale_fuel_flow_by_non_std_density = True
        Assert.assertTrue(basicTakeoff.scale_fuel_flow_by_non_std_density)

        basicTakeoff.accel_fuel_flow = 8000
        Assert.assertAlmostEqual(8000, basicTakeoff.accel_fuel_flow, delta=tolerance)
        basicTakeoff.departure_fuel_flow = 9000
        Assert.assertAlmostEqual(9000, basicTakeoff.departure_fuel_flow, delta=tolerance)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedTakeoffModel
    @category("Aircraft Tests")
    def test_AdvancedTakeoffModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        takeoff: "AircraftTakeoff" = newAC.takeoff
        takeoff.get_as_catalog_item().add_child_of_type("Advanced Takeoff Model", "Adv Takeoff")
        advTakeoff: "AircraftAdvancedTakeoffModel" = takeoff.get_advanced_takeoff_by_name("Adv Takeoff")

        advTakeoff.takeoff_speed_mode = TAKEOFF_LANDING_SPEED_MODE.TAKEOFF_LANDING_ANGLE_OF_ATTACK
        Assert.assertEqual(TAKEOFF_LANDING_SPEED_MODE.TAKEOFF_LANDING_ANGLE_OF_ATTACK, advTakeoff.takeoff_speed_mode)

        advTakeoff.set_angle_of_attack(11)
        angle: typing.Any = advTakeoff.angle_of_attack
        Assert.assertEqual(11, float(angle))

        advTakeoff.set_stall_speed_ratio(1.2)
        Assert.assertEqual(TAKEOFF_LANDING_SPEED_MODE.TAKEOFF_LANDING_STALL_SPEED_RATIO, advTakeoff.takeoff_speed_mode)
        Assert.assertEqual(1.2, advTakeoff.stall_speed_ratio)

        advTakeoff.flaps = 99
        Assert.assertEqual(99, advTakeoff.flaps)

        advTakeoff.departure_speed_mode = DEPARTURE_SPEED_MODE.USE_CLIMB_MODEL
        Assert.assertEqual(DEPARTURE_SPEED_MODE.USE_CLIMB_MODEL, advTakeoff.departure_speed_mode)

        advTakeoff.set_departure_speed_limit(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, advTakeoff.departure_speed_limit_type)
        Assert.assertAlmostEqual(251, advTakeoff.departure_speed_limit, delta=tolerance)
        advTakeoff.set_departure_speed_limit(AIRSPEED_TYPE.MACH, 0.3)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, advTakeoff.departure_speed_limit_type)
        Assert.assertAlmostEqual(0.3, advTakeoff.departure_speed_limit, delta=tolerance)

        with pytest.raises(Exception, match=RegexSubstringMatch("not enabled ")):
            advTakeoff.use_afterburner = True

        newAC.get_as_catalog_item().remove()

    # endregion

    # region TerrainFollowModel
    @category("Aircraft Tests")
    def test_TerrainFollowModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        terrainFollowCategory: "AircraftTerrainFollow" = newAC.terrain_follow
        terrainFollowCategory.get_as_catalog_item().add_child_of_type(
            "AGI TerrainFollow Model", "Test TerrainFollow Model"
        )
        terrainFollow: "AircraftTerrainFollowModel" = terrainFollowCategory.get_terrain_follow_by_name(
            "Test TerrainFollow Model"
        )

        terrainFollow.use_aero_prop_fuel = True
        Assert.assertTrue(terrainFollow.use_aero_prop_fuel)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            terrainFollow.scale_fuel_flow_by_non_std_density = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            terrainFollow.min_airspeed_fuel_flow = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            terrainFollow.max_endurance_fuel_flow = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            terrainFollow.max_airspeed_fuel_flow = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            terrainFollow.max_range_fuel_flow = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            terrainFollow.max_perf_airspeed_fuel_flow = 100

        terrainFollow.use_aero_prop_fuel = False
        Assert.assertEqual(False, terrainFollow.use_aero_prop_fuel)
        terrainFollow.scale_fuel_flow_by_non_std_density = True
        Assert.assertTrue(terrainFollow.scale_fuel_flow_by_non_std_density)

        terrainFollow.airspeed_type = AIRSPEED_TYPE.CAS
        Assert.assertEqual(AIRSPEED_TYPE.CAS, terrainFollow.airspeed_type)

        terrainFollow.min_airspeed = 101
        Assert.assertAlmostEqual(101, terrainFollow.min_airspeed, delta=tolerance)
        terrainFollow.max_endurance_airspeed = 102
        Assert.assertEqual(102, terrainFollow.max_endurance_airspeed)
        terrainFollow.max_airspeed = 553
        Assert.assertAlmostEqual(553, terrainFollow.max_airspeed, delta=tolerance)
        terrainFollow.max_range_airspeed = 104
        Assert.assertEqual(104, terrainFollow.max_range_airspeed)
        terrainFollow.max_perf_airspeed = 105
        Assert.assertEqual(105, terrainFollow.max_perf_airspeed)

        terrainFollow.airspeed_type = AIRSPEED_TYPE.MACH
        Assert.assertEqual(AIRSPEED_TYPE.MACH, terrainFollow.airspeed_type)

        terrainFollow.min_airspeed = 0.1
        Assert.assertEqual(0.1, terrainFollow.min_airspeed)
        terrainFollow.max_endurance_airspeed = 0.12
        Assert.assertEqual(0.12, terrainFollow.max_endurance_airspeed)
        terrainFollow.max_airspeed = 0.96
        Assert.assertEqual(0.96, terrainFollow.max_airspeed)
        terrainFollow.max_range_airspeed = 0.14
        Assert.assertEqual(0.14, terrainFollow.max_range_airspeed)
        terrainFollow.max_perf_airspeed = 0.15
        Assert.assertEqual(0.15, terrainFollow.max_perf_airspeed)

        terrainFollow.min_airspeed_fuel_flow = 101.5
        Assert.assertEqual(101.5, terrainFollow.min_airspeed_fuel_flow)
        terrainFollow.max_endurance_fuel_flow = 102.5
        Assert.assertEqual(102.5, terrainFollow.max_endurance_fuel_flow)
        terrainFollow.max_airspeed_fuel_flow = 553.5
        Assert.assertAlmostEqual(553.5, terrainFollow.max_airspeed_fuel_flow, delta=tolerance)
        terrainFollow.max_range_fuel_flow = 104.5
        Assert.assertEqual(104.5, terrainFollow.max_range_fuel_flow)
        terrainFollow.max_perf_airspeed_fuel_flow = 105.5
        Assert.assertEqual(105.5, terrainFollow.max_perf_airspeed_fuel_flow)

        terrainFollow.max_pitch_angle = 11
        maxPitchAngle: typing.Any = terrainFollow.max_pitch_angle
        Assert.assertEqual(11, float(maxPitchAngle))

        terrainFollow.terrain_window = 4
        Assert.assertEqual(4, terrainFollow.terrain_window)

        Assert.assertTrue((terrainFollow.max_load_factor > 1))

        newAC.get_as_catalog_item().remove()

    # endregion

    # region VTOLModel
    @category("Aircraft Tests")
    def test_VTOLModel(self):
        tolerance: float = 1e-09

        newAC: "AircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), AircraftModel
        )
        vtolCategory: "AircraftVTOL" = newAC.vtol
        vtolCategory.get_as_catalog_item().add_child_of_type("AGI VTOL Model", "Test VTOL Model")
        vtol: "AircraftVTOLModel" = vtolCategory.get_vtol_by_name("Test VTOL Model")

        vtol.max_hover_altitude = 20000
        Assert.assertEqual(20000, vtol.max_hover_altitude)

        vtol.use_aero_prop_fuel = True
        Assert.assertTrue(vtol.use_aero_prop_fuel)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            vtol.scale_fuel_flow_by_non_std_density = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            vtol.hover_fuel = 0.25

        vtol.use_aero_prop_fuel = False
        vtol.scale_fuel_flow_by_non_std_density = True
        Assert.assertTrue(vtol.scale_fuel_flow_by_non_std_density)
        vtol.hover_fuel = 0.25
        Assert.assertEqual(0.25, vtol.hover_fuel)

        vtol.heading_rate = 11
        headingRate: typing.Any = vtol.heading_rate
        Assert.assertEqual(11, float(headingRate))
        vtol.heading_transition_time = 2
        Assert.assertEqual(2, vtol.heading_transition_time)

        vtol.vertical_rate = 1002
        Assert.assertEqual(1002, vtol.vertical_rate)
        vtol.vertical_transition_time = 3
        Assert.assertEqual(3, vtol.vertical_transition_time)

        vtol.translation_rate = 1003
        Assert.assertAlmostEqual(1003, vtol.translation_rate, delta=tolerance)
        vtol.translation_transition_time = 4
        Assert.assertEqual(4, vtol.translation_transition_time)

        vtol.set_forward_flight_airspeed(AIRSPEED_TYPE.TAS, 90)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, vtol.forward_flight_airspeed_type)
        Assert.assertEqual(90, vtol.forward_flight_airspeed)
        vtol.set_forward_flight_airspeed(AIRSPEED_TYPE.MACH, 0.1)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, vtol.forward_flight_airspeed_type)
        Assert.assertEqual(0.1, vtol.forward_flight_airspeed)

        vtol.forward_flight_transition_time = 5
        Assert.assertEqual(5, vtol.forward_flight_transition_time)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region MissileModel
    @category("Missile Tests")
    def test_MissileModel(self):
        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileAsCatalog: "ICatalogItem" = missile.get_as_catalog_item()

        Assert.assertEqual("NUNIT CSharp Test Missile", missileAsCatalog.name)
        missileAsCatalog.name = "NUNIT CSharp Test NameChange"
        Assert.assertEqual("NUNIT CSharp Test NameChange", missileAsCatalog.name)
        missileAsCatalog.name = "NUNIT CSharp Test Missile"

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePerformanceModels
    @category("Missile Tests")
    def test_MissilePerformanceModels(self):
        tolerance: float = 1e-09

        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missile.max_load_factor = 11
        Assert.assertEqual(11, missile.max_load_factor)
        missile.maneuver_mode = ACCEL_MANEUVER_MODE.ACCEL_MANEUVER_MODE_DENSITY_SCALE
        Assert.assertEqual(ACCEL_MANEUVER_MODE.ACCEL_MANEUVER_MODE_DENSITY_SCALE, missile.maneuver_mode)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            testVal: "AeroPropManeuverModeHelper" = missile.maneuver_mode_helper

        missile.maneuver_mode = ACCEL_MANEUVER_MODE.ACCEL_MANEUVER_MODE_AERO_PROP
        self.ManeuverModeHelperOptions(missile.maneuver_mode_helper)

        self.AttitudeTransitionOptions(missile.attitude_transitions)

        missile.ignore_fpa_for_climb_descent_transitions = True
        Assert.assertTrue(missile.ignore_fpa_for_climb_descent_transitions)

        missile.set_climb_airspeed(AIRSPEED_TYPE.MACH, 2.1)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, missile.climb_airspeed_type)
        Assert.assertEqual(2.1, missile.climb_airspeed)
        missile.set_climb_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, missile.climb_airspeed_type)
        Assert.assertAlmostEqual(251, missile.climb_airspeed, delta=tolerance)
        missile.climb_fail_on_insufficient_performance = False
        Assert.assertEqual(False, missile.climb_fail_on_insufficient_performance)

        missile.set_cruise_max_airspeed(AIRSPEED_TYPE.MACH, 2.2)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, missile.cruise_max_airspeed_type)
        Assert.assertEqual(2.2, missile.cruise_max_airspeed)
        missile.set_cruise_max_airspeed(AIRSPEED_TYPE.TAS, 252)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, missile.cruise_max_airspeed_type)
        Assert.assertAlmostEqual(252, missile.cruise_max_airspeed, delta=tolerance)

        missile.set_descent_airspeed(AIRSPEED_TYPE.MACH, 2.3)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, missile.descent_airspeed_type)
        Assert.assertEqual(2.3, missile.descent_airspeed)
        missile.set_descent_airspeed(AIRSPEED_TYPE.TAS, 253)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, missile.descent_airspeed_type)
        Assert.assertAlmostEqual(253, missile.descent_airspeed, delta=tolerance)
        missile.descent_fail_on_insufficient_performance = False
        Assert.assertEqual(False, missile.descent_fail_on_insufficient_performance)

        missile.climb_min_fpa = 3.1
        climbMinFPA: typing.Any = missile.climb_min_fpa
        Assert.assertEqual(3.1, float(climbMinFPA))
        missile.climb_max_fpa = 60.1
        climbMaxFPA: typing.Any = missile.climb_max_fpa
        Assert.assertAlmostEqual(60.1, float(climbMaxFPA), delta=tolerance)

        missile.cruise_default_altitude = 15000
        Assert.assertEqual(15000, missile.cruise_default_altitude)

        missile.descent_min_fpa = -60.2
        descentMinFPA: typing.Any = missile.descent_min_fpa
        Assert.assertAlmostEqual(-60.2, float(descentMinFPA), delta=tolerance)
        missile.descent_max_fpa = -3.2
        descentMaxFPA: typing.Any = missile.descent_max_fpa
        Assert.assertEqual(-3.2, float(descentMaxFPA))

        missile.use_total_temp_limit = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            missile.total_temp_limit = 3000
        missile.use_total_temp_limit = True
        Assert.assertTrue(missile.use_total_temp_limit)
        missile.total_temp_limit = 3000
        Assert.assertEqual(3000, missile.total_temp_limit)

        missile.use_mach_limit = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            missile.mach_limit = 6
        missile.use_mach_limit = True
        Assert.assertTrue(missile.use_mach_limit)
        missile.mach_limit = 6
        Assert.assertEqual(6, missile.mach_limit)

        missile.use_eas_limit = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            missile.eas_limit = 800
        missile.use_eas_limit = True
        Assert.assertTrue(missile.use_eas_limit)
        missile.eas_limit = 800
        Assert.assertEqual(800, missile.eas_limit)

        self.ConfigurationOptions(missile.default_configuration)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissileAeroSimple
    @category("Missile Tests")
    def test_MissileAeroSimple(self):
        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileAero: "MissileAero" = missile.aerodynamics
        missileAero.aero_strategy = MISSILE_AERO_STRATEGY.MISSILE_AERO_SIMPLE
        Assert.assertEqual(MISSILE_AERO_STRATEGY.MISSILE_AERO_SIMPLE, missileAero.aero_strategy)
        simple: "MissileSimpleAero" = missileAero.mode_as_simple

        simple.s_reference = 5
        Assert.assertEqual(5, simple.s_reference)
        simple.cl_max = 2
        Assert.assertEqual(2, simple.cl_max)
        simple.cd = 0.05
        Assert.assertEqual(0.05, simple.cd)

        Assert.assertEqual(False, simple.calculate_aoa)
        simple.set_max_aoa(True, 25)
        aoa: typing.Any = simple.max_aoa
        Assert.assertTrue(simple.calculate_aoa)
        Assert.assertEqual(25, float(aoa))

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissileAeroExternal
    @category("Missile Tests")
    def test_MissileAeroExternal(self):
        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileAero: "MissileAero" = missile.aerodynamics
        missileAero.aero_strategy = MISSILE_AERO_STRATEGY.MISSILE_AERO_EXTERNAL_FILE
        Assert.assertEqual(MISSILE_AERO_STRATEGY.MISSILE_AERO_EXTERNAL_FILE, missileAero.aero_strategy)
        externalAero: "MissileExternalAero" = missileAero.mode_as_external

        externalAero.reference_area = 3
        Assert.assertEqual(3, externalAero.reference_area)
        Assert.assertEqual(False, externalAero.is_valid)

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.aero")
        with pytest.raises(Exception, match=RegexSubstringMatch("Failed to load the file.")):
            externalAero.set_filepath(nonexistingfilepath)

        aeroFilepath: str = TestBase.GetScenarioFile("simpleAero.aero")
        returnMsg: str = externalAero.set_filepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalAero.can_set_reference_area)
        with pytest.raises(Exception):
            externalAero.reference_area = 0.05
        Assert.assertTrue(externalAero.is_valid)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissileAeroAdvanced
    @category("Missile Tests")
    def test_MissileAeroAdvanced(self):
        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileAero: "MissileAero" = missile.aerodynamics
        missileAero.aero_strategy = MISSILE_AERO_STRATEGY.MISSILE_AERO_ADVANCED
        Assert.assertEqual(MISSILE_AERO_STRATEGY.MISSILE_AERO_ADVANCED, missileAero.aero_strategy)
        advancedAero: "MissileAdvancedAero" = missileAero.mode_as_advanced

        self.AdvancedMissileAero(advancedAero)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropSimple
    @category("Missile Tests")
    def test_MissilePropSimple(self):
        tolerance: float = 1e-09

        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "MissileProp" = missile.propulsion
        missileProp.prop_strategy = MISSILE_PROP_STRATEGY.MISSILE_PROP_SIMPLE
        Assert.assertEqual(MISSILE_PROP_STRATEGY.MISSILE_PROP_SIMPLE, missileProp.prop_strategy)
        simpleProp: "MissileSimpleProp" = missileProp.mode_as_simple

        simpleProp.max_thrust = 2000
        Assert.assertEqual(2000, simpleProp.max_thrust)
        simpleProp.fuel_flow = 600
        Assert.assertAlmostEqual(600, simpleProp.fuel_flow, delta=tolerance)
        simpleProp.no_thrust_when_no_fuel = False
        Assert.assertEqual(False, simpleProp.no_thrust_when_no_fuel)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropExternal
    @category("Missile Tests")
    def test_MissilePropExternal(self):
        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "MissileProp" = missile.propulsion
        missileProp.prop_strategy = MISSILE_PROP_STRATEGY.MISSILE_PROP_EXTERNAL_FILE
        Assert.assertEqual(MISSILE_PROP_STRATEGY.MISSILE_PROP_EXTERNAL_FILE, missileProp.prop_strategy)
        externalProp: "MissileExternalProp" = missileProp.mode_as_external

        Assert.assertEqual(False, externalProp.is_valid)

        nonexistingPropFilepath: str = TestBase.GetScenarioFile("DoesNotExist.prop")
        with pytest.raises(Exception, match=RegexSubstringMatch("Failed to load the file.")):
            externalProp.set_filepath(nonexistingPropFilepath)

        propFilepath: str = TestBase.GetScenarioFile("simpleProp.prop")
        returnMsg: str = externalProp.set_filepath(propFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertTrue(externalProp.is_valid)

        returnMsg2: str = externalProp.reload()
        Assert.assertTrue(("processed" in returnMsg2))

        externalProp.no_thrust_when_no_fuel = False
        Assert.assertEqual(False, externalProp.no_thrust_when_no_fuel)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropRamjet
    @category("Missile Tests")
    def test_MissilePropRamjet(self):
        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "MissileProp" = missile.propulsion
        missileProp.prop_strategy = MISSILE_PROP_STRATEGY.MISSILE_PROP_RAMJET
        Assert.assertEqual(MISSILE_PROP_STRATEGY.MISSILE_PROP_RAMJET, missileProp.prop_strategy)
        ramjetProp: "MissileRamjetProp" = missileProp.mode_as_ramjet

        ramjetProp.design_altitude = 5000
        Assert.assertEqual(5000, ramjetProp.design_altitude)
        ramjetProp.design_mach = 3
        Assert.assertEqual(3, ramjetProp.design_mach)
        ramjetProp.design_thrust = 30000
        Assert.assertEqual(30000, ramjetProp.design_thrust)
        ramjetProp.engine_temp = 2000
        Assert.assertEqual(2000, ramjetProp.engine_temp)

        ramjetProp.fuel_heating_value = 41500000
        Assert.assertEqual(41500000, ramjetProp.fuel_heating_value)
        ramjetProp.inlet_pressure_ratio = 0.9
        Assert.assertEqual(0.9, ramjetProp.inlet_pressure_ratio)
        ramjetProp.burner_pressure_ratio = 0.8
        Assert.assertEqual(0.8, ramjetProp.burner_pressure_ratio)
        ramjetProp.nozzle_pressure_ratio = 0.7
        Assert.assertEqual(0.7, ramjetProp.nozzle_pressure_ratio)
        ramjetProp.p_0over_p9 = 0.5
        Assert.assertEqual(0.5, ramjetProp.p_0over_p9)
        ramjetProp.burner_efficiency = 95
        Assert.assertEqual(95, ramjetProp.burner_efficiency)

        ramjetProp.no_thrust_when_no_fuel = False
        Assert.assertEqual(False, ramjetProp.no_thrust_when_no_fuel)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropTurbojet
    @category("Missile Tests")
    def test_MissilePropTurbojet(self):
        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "MissileProp" = missile.propulsion
        missileProp.prop_strategy = MISSILE_PROP_STRATEGY.MISSILE_PROP_TURBOJET
        Assert.assertEqual(MISSILE_PROP_STRATEGY.MISSILE_PROP_TURBOJET, missileProp.prop_strategy)
        turboProp: "MissileTurbojetProp" = missileProp.mode_as_turbojet

        turboProp.design_altitude = 5000
        Assert.assertEqual(5000, turboProp.design_altitude)
        turboProp.design_mach = 3
        Assert.assertEqual(3, turboProp.design_mach)
        turboProp.design_thrust = 30000
        Assert.assertEqual(30000, turboProp.design_thrust)
        turboProp.turbine_temp = 2000
        Assert.assertEqual(2000, turboProp.turbine_temp)
        turboProp.compressor_pressure_ratio = 9
        Assert.assertEqual(9, turboProp.compressor_pressure_ratio)

        turboProp.fuel_heating_value = 41500000
        Assert.assertEqual(41500000, turboProp.fuel_heating_value)
        turboProp.inlet_subsonic_pressure_ratio = 0.9
        Assert.assertEqual(0.9, turboProp.inlet_subsonic_pressure_ratio)
        turboProp.burner_pressure_ratio = 0.8
        Assert.assertEqual(0.8, turboProp.burner_pressure_ratio)
        turboProp.nozzle_pressure_ratio = 0.7
        Assert.assertEqual(0.7, turboProp.nozzle_pressure_ratio)
        turboProp.p_0over_p9 = 0.5
        Assert.assertEqual(0.5, turboProp.p_0over_p9)
        turboProp.compressor_efficiency = 99
        Assert.assertEqual(99, turboProp.compressor_efficiency)
        turboProp.turbine_efficiency = 98
        Assert.assertEqual(98, turboProp.turbine_efficiency)
        turboProp.burner_efficiency = 97
        Assert.assertEqual(97, turboProp.burner_efficiency)
        turboProp.mechanical_efficiency = 96
        Assert.assertEqual(96, turboProp.mechanical_efficiency)

        turboProp.no_thrust_when_no_fuel = False
        Assert.assertEqual(False, turboProp.no_thrust_when_no_fuel)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropRocket
    @category("Missile Tests")
    def test_MissilePropRocket(self):
        tolerance: float = 1e-09

        missileModels: "MissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "MissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "MissileProp" = missile.propulsion
        missileProp.prop_strategy = MISSILE_PROP_STRATEGY.MISSILE_PROP_ROCKET
        Assert.assertEqual(MISSILE_PROP_STRATEGY.MISSILE_PROP_ROCKET, missileProp.prop_strategy)
        rocketProp: "MissileRocketProp" = missileProp.mode_as_rocket

        rocketProp.nozzle_expansion_ratio = 7.1
        Assert.assertEqual(7.1, rocketProp.nozzle_expansion_ratio)
        rocketProp.nozzle_exit_diameter = 0.123
        Assert.assertEqual(0.123, rocketProp.nozzle_exit_diameter)
        rocketProp.propellant_specific_heat_ratio = 1.2
        Assert.assertEqual(1.2, rocketProp.propellant_specific_heat_ratio)
        rocketProp.propellant_characteristic_velocity = 3120
        Assert.assertAlmostEqual(3120, rocketProp.propellant_characteristic_velocity, delta=tolerance)
        rocketProp.combustion_chamber_pressure = 13000000.0
        Assert.assertEqual(13000000.0, rocketProp.combustion_chamber_pressure)

        rocketProp.use_boost_sustain_mode = False
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { rocketProp.BoostFuelFraction = 60; });
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { rocketProp.BoostChamberPressure = 2.1e7; });
        rocketProp.use_boost_sustain_mode = True
        Assert.assertTrue(rocketProp.use_boost_sustain_mode)
        rocketProp.boost_fuel_fraction = 60
        Assert.assertEqual(60, rocketProp.boost_fuel_fraction)
        rocketProp.boost_chamber_pressure = 21000000.0
        Assert.assertEqual(21000000.0, rocketProp.boost_chamber_pressure)

        rocketProp.no_thrust_when_no_fuel = False
        Assert.assertEqual(False, rocketProp.no_thrust_when_no_fuel)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region RotorcraftModel
    @category("Missile Tests")
    def test_RotorcraftModel(self):
        rotorcraftModels: "RotorcraftModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models
        if rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")

        rotorcraft: "RotorcraftModel" = rotorcraftModels.add_rotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.get_as_catalog_item().name)
        Assert.assertTrue(rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

        rotorcraftAsCatalog: "ICatalogItem" = rotorcraft.get_as_catalog_item()

        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraftAsCatalog.name)
        rotorcraftAsCatalog.name = "NUNIT CSharp Test Rotorcraft NameChange"
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft NameChange", rotorcraftAsCatalog.name)
        rotorcraftAsCatalog.name = "NUNIT CSharp Test Rotorcraft"

        rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual(False, rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

    # endregion

    # region RotorcraftPerformanceModels
    @category("Rotorcraft Tests")
    def test_RotorcraftPerformanceModels(self):
        tolerance: float = 1e-09

        rotorcraftModels: "RotorcraftModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models
        if rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")

        rotorcraft: "RotorcraftModel" = rotorcraftModels.add_rotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.get_as_catalog_item().name)
        Assert.assertTrue(rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

        rotorcraft.max_altitude = 11000
        Assert.assertEqual(11000, rotorcraft.max_altitude)
        rotorcraft.default_cruise_altitude = 500
        Assert.assertEqual(500, rotorcraft.default_cruise_altitude)
        rotorcraft.descent_rate_factor = 45
        Assert.assertEqual(45, rotorcraft.descent_rate_factor)
        rotorcraft.max_climb_angle = 55
        maxClimbAngle: typing.Any = rotorcraft.max_climb_angle
        Assert.assertEqual(55, float(maxClimbAngle))
        rotorcraft.climb_at_cruise_airspeed = False
        Assert.assertEqual(False, rotorcraft.climb_at_cruise_airspeed)
        rotorcraft.max_descent_angle = 56
        maxDescentAngle: typing.Any = rotorcraft.max_descent_angle
        Assert.assertEqual(56, float(maxDescentAngle))
        rotorcraft.min_descent_rate = 2000
        Assert.assertAlmostEqual(2000, rotorcraft.min_descent_rate, delta=tolerance)
        rotorcraft.max_load_factor = 1.2
        Assert.assertEqual(1.2, rotorcraft.max_load_factor)

        rotorcraft.roll_rate = 30
        rollRate: typing.Any = rotorcraft.roll_rate
        Assert.assertAlmostEqual(30, float(rollRate), delta=tolerance)
        rotorcraft.pitch_rate = 20
        pitchRate: typing.Any = rotorcraft.pitch_rate
        Assert.assertAlmostEqual(20, float(pitchRate), delta=tolerance)
        rotorcraft.yaw_rate = 15
        yawRate: typing.Any = rotorcraft.yaw_rate
        Assert.assertAlmostEqual(15, float(yawRate), delta=tolerance)
        rotorcraft.yaw_rate_dot = 14
        yawRateDot: typing.Any = rotorcraft.yaw_rate_dot
        Assert.assertAlmostEqual(14, float(yawRateDot), delta=tolerance)
        rotorcraft.max_transition_pitch_angle = 60
        maxTransitionPitchAngle: typing.Any = rotorcraft.max_transition_pitch_angle
        Assert.assertAlmostEqual(60, float(maxTransitionPitchAngle), delta=tolerance)
        rotorcraft.tf_max_flight_path_angle = 20
        tFMaxFlightPathAngle: typing.Any = rotorcraft.tf_max_flight_path_angle
        Assert.assertAlmostEqual(20, float(tFMaxFlightPathAngle), delta=tolerance)
        rotorcraft.tf_terrain_window = 0.01
        Assert.assertEqual(0.01, rotorcraft.tf_terrain_window)
        rotorcraft.compute_delta_altitude = 2000
        Assert.assertEqual(2000, rotorcraft.compute_delta_altitude)

        rotorcraft.set_max_safe_airspeed(AIRSPEED_TYPE.MACH, 0.5)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, rotorcraft.max_safe_airspeed_type)
        Assert.assertEqual(0.5, rotorcraft.max_safe_airspeed)
        rotorcraft.set_max_safe_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, rotorcraft.max_safe_airspeed_type)
        Assert.assertAlmostEqual(251, rotorcraft.max_safe_airspeed, delta=tolerance)

        rotorcraft.set_max_safe_translation_speed(AIRSPEED_TYPE.MACH, 0.4)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, rotorcraft.max_safe_translation_speed_type)
        Assert.assertEqual(0.4, rotorcraft.max_safe_translation_speed)
        rotorcraft.set_max_safe_translation_speed(AIRSPEED_TYPE.TAS, 211)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, rotorcraft.max_safe_translation_speed_type)
        Assert.assertAlmostEqual(211, rotorcraft.max_safe_translation_speed, delta=tolerance)

        rotorcraft.ignore_fpa_for_climb_descent_transitions = True
        Assert.assertTrue(rotorcraft.ignore_fpa_for_climb_descent_transitions)

        self.ConfigurationOptions(rotorcraft.default_configuration)

        rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual(False, rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

    # endregion

    # region RotorcraftAero
    @category("Rotorcraft Tests")
    def test_RotorcraftAero(self):
        rotorcraftModels: "RotorcraftModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models
        if rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")

        rotorcraft: "RotorcraftModel" = rotorcraftModels.add_rotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.get_as_catalog_item().name)
        Assert.assertTrue(rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

        aero: "RotorcraftAero" = rotorcraft.aerodynamics

        aero.rotor_count = 5
        Assert.assertEqual(5, aero.rotor_count)
        aero.rotor_diameter = 0.5
        Assert.assertEqual(0.5, aero.rotor_diameter)
        aero.blades_per_rotor = 3
        Assert.assertEqual(3, aero.blades_per_rotor)
        aero.blade_chord = 0.03
        Assert.assertEqual(0.03, aero.blade_chord)
        aero.rotor_tip_mach = 0.75
        Assert.assertEqual(0.75, aero.rotor_tip_mach)
        aero.fuselage_flat_plate_area = 2
        Assert.assertEqual(2, aero.fuselage_flat_plate_area)

        aero.rotor_count = 5
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { aero.TailRotorOffset = 10.1; });
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { aero.TailRotorDiameter = 2.5; });
        aero.rotor_count = 1
        aero.tail_rotor_offset = 10.1
        Assert.assertEqual(10.1, aero.tail_rotor_offset)
        aero.tail_rotor_diameter = 2.5
        Assert.assertEqual(2.5, aero.tail_rotor_diameter)

        aero.blade_profile_drag_cd0 = 0.02
        Assert.assertEqual(0.02, aero.blade_profile_drag_cd0)
        aero.blade_profile_drag_k = 5
        Assert.assertEqual(5, aero.blade_profile_drag_k)
        aero.induced_power_correction_factor = 1.2
        Assert.assertEqual(1.2, aero.induced_power_correction_factor)

        rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual(False, rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

    # endregion

    # region RotorcraftProp
    @category("Rotorcraft Tests")
    def test_RotorcraftProp(self):
        tolerance: float = 1e-09

        rotorcraftModels: "RotorcraftModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models
        if rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")

        rotorcraft: "RotorcraftModel" = rotorcraftModels.add_rotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.get_as_catalog_item().name)
        Assert.assertTrue(rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

        prop: "RotorcraftProp" = rotorcraft.propulsion

        prop.powerplant_type = ROTORCRAFT_POWERPLANT_TYPE.ROTORCRAFT_ELECTRIC
        Assert.assertEqual(ROTORCRAFT_POWERPLANT_TYPE.ROTORCRAFT_ELECTRIC, prop.powerplant_type)
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { prop.MaxSLFuelFlow = 5; });

        prop.powerplant_type = ROTORCRAFT_POWERPLANT_TYPE.ROTORCRAFT_TURBOSHAFT
        Assert.assertEqual(ROTORCRAFT_POWERPLANT_TYPE.ROTORCRAFT_TURBOSHAFT, prop.powerplant_type)
        prop.max_sl_power = 60
        Assert.assertEqual(60, prop.max_sl_power)
        prop.max_sl_fuel_flow = 5
        Assert.assertAlmostEqual(5, prop.max_sl_fuel_flow, delta=tolerance)

        rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual(False, rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

    # endregion

    # region UserRunwaySource
    @category("Catalog Tests")
    def test_UserRunwaySource(self):
        userRunways: "UserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        names = userRunways.get_as_catalog_source().child_names
        nameCount: int = Array.Length(names)

        nunitRunway: "UserRunway" = userRunways.add_user_runway("NUnitUserRunway")
        Assert.assertEqual("NUnitUserRunway", nunitRunway.get_as_catalog_item().name)
        Assert.assertTrue(userRunways.get_as_catalog_source().contains("NUnitUserRunway"))
        names = userRunways.get_as_catalog_source().child_names
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitRunway2: "UserRunway" = userRunways.get_user_runway("NUnitUserRunway")
        Assert.assertEqual("NUnitUserRunway", nunitRunway2.get_as_catalog_item().name)

        userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")
        names = userRunways.get_as_catalog_source().child_names
        nameCount = nameCount - 1
        Assert.assertEqual(nameCount, Array.Length(names))
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

    # endregion

    # region UserRunway
    @category("Catalog Tests")
    def test_UserRunway(self):
        tolerance: float = 1e-09

        userRunways: "UserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        nunitRunway: "UserRunway" = userRunways.add_user_runway("NUnitUserRunway")

        nunitRunway.latitude = 1
        lat: typing.Any = nunitRunway.latitude
        Assert.assertEqual(1, float(lat))
        nunitRunway.longitude = 2
        lon: typing.Any = nunitRunway.longitude
        Assert.assertEqual(2, float(lon))
        nunitRunway.altitude = 5
        Assert.assertEqual(5, nunitRunway.altitude)
        terrainAlt: float = nunitRunway.get_terrain_altitude()
        Assert.assertEqual(terrainAlt, nunitRunway.altitude)

        nunitRunway.high_end_heading = 195
        highEndHeading: typing.Any = nunitRunway.high_end_heading
        Assert.assertAlmostEqual(195, float(highEndHeading), delta=tolerance)
        lowEndHeading: typing.Any = nunitRunway.low_end_heading
        Assert.assertAlmostEqual(15, float(lowEndHeading), delta=tolerance)
        nunitRunway.is_magnetic = False
        Assert.assertEqual(False, nunitRunway.is_magnetic)

        nunitRunway.length = 5
        Assert.assertEqual(5, nunitRunway.length)

        nunitRunway.copy_site()
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway2"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway2")

        nunitRunway2: "UserRunway" = userRunways.add_user_runway("NUnitUserRunway2")
        nunitRunway2.paste_site()

        lat = nunitRunway2.latitude
        Assert.assertEqual(1, float(lat))
        nunitRunway2.longitude = 2
        lon = nunitRunway2.longitude
        Assert.assertEqual(2, float(lon))
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        if userRunways.get_as_catalog_source().contains("NUnitUserRunway2"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway2")

    # endregion

    # region UserVTOLPointSource
    @category("Catalog Tests")
    def test_UserVTOLPointSource(self):
        userVTOLPoints: "UserVTOLPointSource" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.user_vtol_points
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

        names = userVTOLPoints.get_as_catalog_source().child_names
        nameCount: int = Array.Length(names)

        nunitVTOLPoint: "UserVTOLPoint" = userVTOLPoints.add_user_vtol_point("NUnitUserVTOLPoint")
        Assert.assertEqual("NUnitUserVTOLPoint", nunitVTOLPoint.get_as_catalog_item().name)
        Assert.assertTrue(userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"))
        names = userVTOLPoints.get_as_catalog_source().child_names
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitVTOLPoint2: "UserVTOLPoint" = userVTOLPoints.get_user_vtol_point("NUnitUserVTOLPoint")
        Assert.assertEqual("NUnitUserVTOLPoint", nunitVTOLPoint2.get_as_catalog_item().name)

        userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")
        names = userVTOLPoints.get_as_catalog_source().child_names
        nameCount = nameCount - 1
        Assert.assertEqual(nameCount, Array.Length(names))
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

    # endregion

    # region UserVTOLPoint
    @category("Catalog Tests")
    def test_UserVTOLPoint(self):
        userVTOLPoints: "UserVTOLPointSource" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.user_vtol_points
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

        nunitVTOLPoint: "UserVTOLPoint" = userVTOLPoints.add_user_vtol_point("NUnitUserVTOLPoint")

        nunitVTOLPoint.latitude = 1
        lat: typing.Any = nunitVTOLPoint.latitude
        Assert.assertEqual(1, float(lat))
        nunitVTOLPoint.longitude = 2
        lon: typing.Any = nunitVTOLPoint.longitude
        Assert.assertEqual(2, float(lon))
        nunitVTOLPoint.altitude = 5
        Assert.assertEqual(5, nunitVTOLPoint.altitude)
        terrainAlt: float = nunitVTOLPoint.get_terrain_altitude()
        Assert.assertEqual(terrainAlt, nunitVTOLPoint.altitude)

        nunitVTOLPoint.copy_site()
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint2"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint2")

        nunitVTOLPoint2: "UserVTOLPoint" = userVTOLPoints.add_user_vtol_point("NUnitUserVTOLPoint2")
        nunitVTOLPoint2.paste_site()

        lat = nunitVTOLPoint2.latitude
        Assert.assertEqual(1, float(lat))
        nunitVTOLPoint2.longitude = 2
        lon = nunitVTOLPoint2.longitude
        Assert.assertEqual(2, float(lon))
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint2"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint2")

    # endregion

    # region UserWaypointSource
    @category("Catalog Tests")
    def test_UserWaypointSource(self):
        userWaypoints: "UserWaypointSource" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.user_waypoints
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

        names = userWaypoints.get_as_catalog_source().child_names
        nameCount: int = Array.Length(names)

        nunitWaypoint: "UserWaypoint" = userWaypoints.add_user_waypoint("NUnitUserWaypoint")
        Assert.assertEqual("NUnitUserWaypoint", nunitWaypoint.get_as_catalog_item().name)
        Assert.assertTrue(userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"))
        names = userWaypoints.get_as_catalog_source().child_names
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitWaypoint2: "UserWaypoint" = userWaypoints.get_user_waypoint("NUnitUserWaypoint")
        Assert.assertEqual("NUnitUserWaypoint", nunitWaypoint2.get_as_catalog_item().name)

        userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")
        names = userWaypoints.get_as_catalog_source().child_names
        nameCount = nameCount - 1
        Assert.assertEqual(nameCount, Array.Length(names))
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

    # endregion

    # region UserWaypoint
    @category("Catalog Tests")
    def test_UserWaypoint(self):
        userWaypoints: "UserWaypointSource" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.user_waypoints
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

        nunitWaypoint: "UserWaypoint" = userWaypoints.add_user_waypoint("NUnitUserWaypoint")

        nunitWaypoint.latitude = 1
        lat: typing.Any = nunitWaypoint.latitude
        Assert.assertEqual(1, float(lat))
        nunitWaypoint.longitude = 2
        lon: typing.Any = nunitWaypoint.longitude
        Assert.assertEqual(2, float(lon))

        nunitWaypoint.copy_site()
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint2"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint2")

        nunitWaypoint2: "UserWaypoint" = userWaypoints.add_user_waypoint("NUnitUserWaypoint2")
        nunitWaypoint2.paste_site()

        lat = nunitWaypoint2.latitude
        Assert.assertEqual(1, float(lat))
        nunitWaypoint2.longitude = 2
        lon = nunitWaypoint2.longitude
        Assert.assertEqual(2, float(lon))
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint2"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint2")

    # endregion

    # region ARINC424AirportSource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424AirportSource(self):
        arincAirports: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.airport_category.arinc424_airports
        self.ARINC424Source(arincAirports, "02 RANCH")

    # endregion

    # region ARINC424Airport
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Airport(self):
        tolerance: float = 0.01

        arincAirports: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.airport_category.arinc424_airports
        ranch: "IARINC424Item" = arincAirports.get_arinc424_item("02 RANCH")

        identifier: typing.Any = ranch.get_value("ICAO Code")
        Assert.assertEqual("K4", str(identifier))
        altitude: typing.Any = ranch.get_value("Airport Elevation")
        Assert.assertEqual(3799, int(altitude))

        fields = ranch.get_all_fields()
        Assert.assertEqual("ICAO Code", fields[0])

        fieldsAndValues = ranch.get_all_fields_and_values()
        Assert.assertEqual("ICAO Code: K4", fieldsAndValues[0])

        Assert.assertEqual("02 RANCH", ranch.get_as_catalog_item().name)

        Assert.assertTrue(ranch.get_as_catalog_item().is_read_only)

        ranch.copy_site()

        userRunways: "UserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        nunitRunway: "UserRunway" = userRunways.add_user_runway("NUnitUserRunway")

        nunitRunway.paste_site()
        lat: typing.Any = nunitRunway.latitude
        Assert.assertAlmostEqual(29.875, float(lat), delta=tolerance)
        lon: typing.Any = nunitRunway.longitude
        Assert.assertAlmostEqual(-103.697, float(lon), delta=tolerance)
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

    # endregion

    # region ARINC424HelipadSource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424HelipadSource(self):
        arincHelipads: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.arinc424_helipads
        self.ARINC424Source(arincHelipads, "1001 FOURTH AVENUE PLAZA H1")

    # endregion

    # region ARINC424Helipad
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Helipad(self):
        tolerance: float = 0.01

        arincHelipads: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.arinc424_helipads
        fourthAveH1: "IARINC424Item" = arincHelipads.get_arinc424_item("1001 FOURTH AVENUE PLAZA H1")

        identifier: typing.Any = fourthAveH1.get_value("ICAO Code")
        Assert.assertEqual("K1", str(identifier))
        altitude: typing.Any = fourthAveH1.get_value("Heliport Elevation")
        Assert.assertEqual(716, int(altitude))

        fields = fourthAveH1.get_all_fields()
        Assert.assertEqual("ICAO Code", fields[0])

        fieldsAndValues = fourthAveH1.get_all_fields_and_values()
        Assert.assertEqual("ICAO Code: K1", fieldsAndValues[0])

        Assert.assertEqual("1001 FOURTH AVENUE PLAZA H1", fourthAveH1.get_as_catalog_item().name)

        Assert.assertTrue(fourthAveH1.get_as_catalog_item().is_read_only)

        fourthAveH1.copy_site()

        userVTOLPoints: "UserVTOLPointSource" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.user_vtol_points
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

        nunitVTOLPoint: "UserVTOLPoint" = userVTOLPoints.add_user_vtol_point("NUnitUserVTOLPoint")

        nunitVTOLPoint.paste_site()
        lat: typing.Any = nunitVTOLPoint.latitude
        Assert.assertAlmostEqual(47.607, float(lat), delta=tolerance)
        lon: typing.Any = nunitVTOLPoint.longitude
        Assert.assertAlmostEqual(-122.334, float(lon), delta=tolerance)
        Assert.assertAlmostEqual(716, nunitVTOLPoint.altitude, delta=tolerance)
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

    # endregion

    # region ARINC424NavaidSource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424NavaidSource(self):
        arincNavaids: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.navaid_category.arinc424_navaids
        self.ARINC424Source(arincNavaids, "1B")

    # endregion

    # region ARINC424Navaid
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Navaid(self):
        tolerance: float = 0.01

        arincNavaids: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.navaid_category.arinc424_navaids
        oneb: "IARINC424Item" = arincNavaids.get_arinc424_item("1B")

        identifier: typing.Any = oneb.get_value("Navaid Identifier")
        Assert.assertTrue(("1B" in str(identifier)))
        freq: typing.Any = oneb.get_value("Frequency")
        Assert.assertEqual(277, float(freq))

        fields = oneb.get_all_fields()
        Assert.assertEqual("Navaid Identifier", fields[0])

        fieldsAndValues = oneb.get_all_fields_and_values()
        Assert.assertTrue(("Navaid Identifier: 1B" in str(fieldsAndValues[0])))

        Assert.assertEqual("1B", oneb.get_as_catalog_item().name)

        Assert.assertTrue(oneb.get_as_catalog_item().is_read_only)

        oneb.copy_site()

        userRunways: "UserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        nunitRunway: "UserRunway" = userRunways.add_user_runway("NUnitUserRunway")

        nunitRunway.paste_site()
        lat: typing.Any = nunitRunway.latitude
        Assert.assertAlmostEqual(43.931, float(lat), delta=tolerance)
        lon: typing.Any = nunitRunway.longitude
        Assert.assertAlmostEqual(-60.023, float(lon), delta=tolerance)
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

    # endregion

    # region ARINC424RunwaySource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424RunwaySource(self):
        arincRunways: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.runway_category.arinc424_runways
        self.ARINC424Source(arincRunways, "JOHN F KENNEDY INTL 04L 22R")

    # endregion

    # region ARINC424Runway
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Runway(self):
        tolerance: float = 0.01

        arincRunways: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.runway_category.arinc424_runways
        jfk: "IARINC424Item" = arincRunways.get_arinc424_item("JOHN F KENNEDY INTL 04L 22R")

        identifier: typing.Any = jfk.get_value("Airport ICAO Identifier")
        Assert.assertEqual("KJFK", str(identifier))
        altitude: typing.Any = jfk.get_value("Altitude")
        Assert.assertEqual(12.5, float(altitude))

        fields = jfk.get_all_fields()
        Assert.assertEqual("Airport ICAO Identifier", fields[0])

        fieldsAndValues = jfk.get_all_fields_and_values()
        Assert.assertEqual("Airport ICAO Identifier: KJFK", fieldsAndValues[0])

        Assert.assertEqual("JOHN F KENNEDY INTL 04L 22R", jfk.get_as_catalog_item().name)

        Assert.assertTrue(jfk.get_as_catalog_item().is_read_only)

        jfk.copy_site()

        userRunways: "UserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        nunitRunway: "UserRunway" = userRunways.add_user_runway("NUnitUserRunway")

        nunitRunway.paste_site()
        lat: typing.Any = nunitRunway.latitude
        Assert.assertAlmostEqual(40.63, float(lat), delta=tolerance)
        lon: typing.Any = nunitRunway.longitude
        Assert.assertAlmostEqual(-73.786, float(lon), delta=tolerance)
        Assert.assertAlmostEqual(12.5, nunitRunway.altitude, delta=tolerance)
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

    # endregion

    # region ARINC424WaypointSource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424WaypointSource(self):
        arincWaypoints: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.arinc424_waypoints
        self.ARINC424Source(arincWaypoints, "AAAMY")

    # endregion

    # region ARINC424Waypoint
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Waypoint(self):
        tolerance: float = 0.01

        arincWaypoints: "ARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.arinc424_waypoints
        aaamy: "IARINC424Item" = arincWaypoints.get_arinc424_item("AAAMY")

        identifier: typing.Any = aaamy.get_value("ICAO Code")
        Assert.assertEqual("K5", str(identifier))
        latTest: typing.Any = aaamy.get_value("Latitude")
        Assert.assertAlmostEqual(43.069, float(latTest), delta=tolerance)

        fields = aaamy.get_all_fields()
        Assert.assertEqual("Waypoint Ident", fields[0])

        fieldsAndValues = aaamy.get_all_fields_and_values()
        Assert.assertEqual("Waypoint Ident: AAAMY", fieldsAndValues[0])

        Assert.assertEqual("AAAMY", aaamy.get_as_catalog_item().name)

        Assert.assertTrue(aaamy.get_as_catalog_item().is_read_only)

        aaamy.copy_site()

        userWaypoints: "UserWaypointSource" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.user_waypoints
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

        nunitWaypoint: "UserWaypoint" = userWaypoints.add_user_waypoint("NUnitUserWaypoint")

        nunitWaypoint.paste_site()
        lat: typing.Any = nunitWaypoint.latitude
        Assert.assertAlmostEqual(43.069, float(lat), delta=tolerance)
        lon: typing.Any = nunitWaypoint.longitude
        Assert.assertAlmostEqual(-82.615, float(lon), delta=tolerance)
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

    # endregion

    # region PrivateCatalogMethods

    def AdvancedMissileAero(self, advancedAero: "MissileAdvancedAero"):
        advancedAero.body_width = 0.2
        Assert.assertEqual(0.2, advancedAero.body_width)
        advancedAero.body_height = 0.3
        Assert.assertEqual(0.3, advancedAero.body_height)
        advancedAero.body_length = 3
        Assert.assertEqual(3, advancedAero.body_length)
        advancedAero.nose_length = 0.4
        Assert.assertEqual(0.4, advancedAero.nose_length)
        advancedAero.nose_tip_diameter = 0.05
        Assert.assertEqual(0.05, advancedAero.nose_tip_diameter)
        advancedAero.nozzle_diameter = 0.5
        Assert.assertEqual(0.5, advancedAero.nozzle_diameter)

        advancedAero.min_mach = 0.2
        Assert.assertEqual(0.2, advancedAero.min_mach)
        advancedAero.max_aoa = 50
        aoa: typing.Any = advancedAero.max_aoa
        Assert.assertEqual(50, float(aoa))

        advancedAero.wing_count = 1
        Assert.assertEqual(1, advancedAero.wing_count)
        advancedAero.wing_span = 0.2
        Assert.assertEqual(0.2, advancedAero.wing_span)
        advancedAero.wing_surface_area = 3e-07
        Assert.assertEqual(3e-07, advancedAero.wing_surface_area)
        advancedAero.wing_lift_fraction = 40
        Assert.assertEqual(40, advancedAero.wing_lift_fraction)
        advancedAero.wing_leading_edge_sweep_angle = 50
        sweep: typing.Any = advancedAero.wing_leading_edge_sweep_angle
        Assert.assertEqual(50, float(sweep))
        advancedAero.wing_leading_edge_section_angle = 6
        section: typing.Any = advancedAero.wing_leading_edge_section_angle
        Assert.assertEqual(6, float(section))
        advancedAero.wing_mean_aero_chord_length = 0.07
        Assert.assertEqual(0.07, advancedAero.wing_mean_aero_chord_length)
        advancedAero.wing_max_thickness_along_mac = 0.008
        Assert.assertEqual(0.008, advancedAero.wing_max_thickness_along_mac)

        advancedAero.tail_count = 1
        Assert.assertEqual(1, advancedAero.tail_count)
        advancedAero.tail_span = 0.2
        Assert.assertEqual(0.2, advancedAero.tail_span)
        advancedAero.tail_surface_area = 3e-07
        Assert.assertEqual(3e-07, advancedAero.tail_surface_area)
        advancedAero.tail_lift_fraction = 40
        Assert.assertEqual(40, advancedAero.tail_lift_fraction)
        advancedAero.tail_leading_edge_sweep_angle = 50
        tailSweep: typing.Any = advancedAero.tail_leading_edge_sweep_angle
        Assert.assertEqual(50, float(tailSweep))
        advancedAero.tail_leading_edge_section_angle = 6
        tailSection: typing.Any = advancedAero.tail_leading_edge_section_angle
        Assert.assertEqual(6, float(tailSection))
        advancedAero.tail_mean_aero_chord_length = 0.07
        Assert.assertEqual(0.07, advancedAero.tail_mean_aero_chord_length)
        advancedAero.tail_max_thickness_along_mac = 0.008
        Assert.assertEqual(0.008, advancedAero.tail_max_thickness_along_mac)

    def EmpiricalJetEngineOptions(self, prop: "AdvancedFixedWingEmpiricalJetEngine"):
        tolerance: float = 1e-09

        prop.max_sea_level_static_thrust = 65000
        Assert.assertAlmostEqual(65000, prop.max_sea_level_static_thrust, delta=tolerance)
        prop.design_point_altitude = 2
        Assert.assertEqual(2, prop.design_point_altitude)
        prop.design_point_mach_number = 0.75
        Assert.assertEqual(0.75, prop.design_point_mach_number)

        prop.fuel_flow = 25000
        Assert.assertAlmostEqual(25000, prop.fuel_flow, delta=tolerance)

    def AttitudeTransitionOptions(self, att: "AttitudeTransitions"):
        tolerance: float = 1e-09

        att.pitch_rate = 10
        pitchRate: typing.Any = att.pitch_rate
        Assert.assertAlmostEqual(10, float(pitchRate), delta=tolerance)

        att.yaw_rate = 20
        yawRate: typing.Any = att.yaw_rate
        Assert.assertAlmostEqual(20, float(yawRate), delta=tolerance)

        att.roll_rate = 30
        rollRate: typing.Any = att.roll_rate
        Assert.assertAlmostEqual(30, float(rollRate), delta=tolerance)

    def ManeuverModeHelperOptions(self, helper: "AeroPropManeuverModeHelper"):
        tolerance: float = 1e-09

        helper.mode = ACCEL_MANEUVER_AERO_PROP_MODE.USE_LIFT_COEFFICIENT_ONLY
        Assert.assertEqual(ACCEL_MANEUVER_AERO_PROP_MODE.USE_LIFT_COEFFICIENT_ONLY, helper.mode)

        helper.flight_mode = AERO_PROP_FLIGHT_MODE.FLIGHT_PERF_TAKEOFF
        Assert.assertEqual(AERO_PROP_FLIGHT_MODE.FLIGHT_PERF_TAKEOFF, helper.flight_mode)

        helper.use_afterburner = True
        Assert.assertTrue(helper.use_afterburner)

        helper.reference_weight = 20000
        Assert.assertEqual(20000, helper.reference_weight)
        helper.reference_altitude = 25000
        Assert.assertEqual(25000, helper.reference_altitude)
        helper.set_reference_airspeed(AIRSPEED_TYPE.TAS, 251)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, helper.reference_airspeed_type)
        Assert.assertAlmostEqual(251, helper.reference_airspeed, delta=tolerance)
        helper.set_reference_airspeed(AIRSPEED_TYPE.MACH, 0.6)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, helper.reference_airspeed_type)
        Assert.assertAlmostEqual(0.6, helper.reference_airspeed, delta=tolerance)

        helper.reference_load_factor = 6
        Assert.assertEqual(6, helper.reference_load_factor)

        helper.control_authority = 0.5
        Assert.assertEqual(0.5, helper.control_authority)

    def ConfigurationOptions(self, defConfig: "Configuration"):
        defConfig.empty_weight = 100
        Assert.assertEqual(100, defConfig.empty_weight)

        defConfig.max_landing_weight = 500
        Assert.assertEqual(500, defConfig.max_landing_weight)

        defConfig.base_drag_index = 1
        Assert.assertEqual(1, defConfig.base_drag_index)

        defConfig.set_empty_cg(1, 2, 3)
        Assert.assertEqual(1, defConfig.empty_cgx)
        Assert.assertEqual(2, defConfig.empty_cgy)
        Assert.assertEqual(3, defConfig.empty_cgz)

    def ARINC424Source(self, arincSource: "ARINC424Source", childName: str):
        Assert.assertTrue(arincSource.use_master_data_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("to access this")):
            arincSource.override_data_filepath = "NonExistantPath"

        arincSource.use_master_data_file = False
        arincSource.override_data_filepath = "NonExistantPath"
        Assert.assertEqual("NonExistantPath", arincSource.override_data_filepath)

        arincSource.use_master_data_file = True
        Assert.assertTrue(("FAA" in arincSource.master_data_filepath))

        catalogSource: "ICatalogSource" = clr.CastAs(arincSource, ICatalogSource)
        names = catalogSource.child_names
        Assert.assertTrue((Array.Length(names) > 0))
        Assert.assertTrue(catalogSource.contains(childName))
        with pytest.raises(Exception):
            catalogSource.remove_child(childName)

    def TestPropulsionEfficiencies(self, propEffs: "PropulsionEfficiencies"):
        propEffs.technology_level = JET_ENGINE_TECHNOLOGY_LEVEL.LEVEL5
        Assert.assertEqual(JET_ENGINE_TECHNOLOGY_LEVEL.LEVEL5, propEffs.technology_level)
        propEffs.intake_type = JET_ENGINE_INTAKE_TYPE.SUBSONIC_EMBEDDED
        Assert.assertEqual(JET_ENGINE_INTAKE_TYPE.SUBSONIC_EMBEDDED, propEffs.intake_type)
        propEffs.turbine_type = JET_ENGINE_TURBINE_TYPE.UNCOOLED
        Assert.assertEqual(JET_ENGINE_TURBINE_TYPE.UNCOOLED, propEffs.turbine_type)
        propEffs.exhaust_nozzle_type = JET_ENGINE_EXHAUST_NOZZLE_TYPE.FIXED_AREA_CONVERGENT
        Assert.assertEqual(JET_ENGINE_EXHAUST_NOZZLE_TYPE.FIXED_AREA_CONVERGENT, propEffs.exhaust_nozzle_type)

    def TestPropulsionEfficienciesRamScram(self, propEffs: "PropulsionEfficiencies"):
        # This tests the propulsion efficiencies interface only for Ramjets and Scramjets as the enumeration values are more limited
        propEffs.technology_level = JET_ENGINE_TECHNOLOGY_LEVEL.LEVEL5
        Assert.assertEqual(JET_ENGINE_TECHNOLOGY_LEVEL.LEVEL5, propEffs.technology_level)
        Assert.assertEqual(JET_ENGINE_INTAKE_TYPE.SUPERSONIC_EMBEDDED, propEffs.intake_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("turbine type")):
            turbineTypeTest: "JET_ENGINE_TURBINE_TYPE" = propEffs.turbine_type
        Assert.assertEqual(
            JET_ENGINE_EXHAUST_NOZZLE_TYPE.VARIABLE_AREA_CONVERGENT_DIVERGENT, propEffs.exhaust_nozzle_type
        )

    def TestFuelAFPROP(self, afprop: "FuelModelKeroseneAFPROP"):
        afprop.subtype = AFPROP_FUEL_TYPE.AFPROP_JET_A
        Assert.assertEqual(AFPROP_FUEL_TYPE.AFPROP_JET_A, afprop.subtype)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            afprop.specific_energy = 40

        afprop.subtype = AFPROP_FUEL_TYPE.AFPROP_OVERRIDE
        afprop.specific_energy = 43.21
        Assert.assertEqual(43.21, afprop.specific_energy)

    def TestFuelCEA(self, cea: "FuelModelKeroseneCEA"):
        cea.subtype = CEA_FUEL_TYPE.CEA_JET_A
        Assert.assertEqual(CEA_FUEL_TYPE.CEA_JET_A, cea.subtype)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            cea.specific_energy = 40

        cea.subtype = CEA_FUEL_TYPE.CEA_OVERRIDE
        cea.specific_energy = 43.21
        Assert.assertEqual(43.21, cea.specific_energy)

    def TestTurbofanBasicAB(self, prop: "AdvancedFixedWingTurbofanBasicABProp"):
        prop.can_use_afterburner = False
        Assert.assertEqual(False, prop.can_use_afterburner)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            prop.afterburner_on = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            prop.max_afterburner_temp = 2000

        prop.can_use_afterburner = True
        prop.design_altitude = 33100
        Assert.assertEqual(33100, prop.design_altitude)
        prop.design_mach = 0.75
        Assert.assertEqual(0.75, prop.design_mach)
        prop.design_thrust = 80000
        Assert.assertEqual(80000, prop.design_thrust)
        prop.afterburner_on = True
        Assert.assertTrue(prop.afterburner_on)

        prop.max_compression_temp = 800
        Assert.assertEqual(800, prop.max_compression_temp)
        prop.max_burner_temp = 1400
        Assert.assertEqual(1400, prop.max_burner_temp)
        prop.max_afterburner_temp = 1900
        Assert.assertEqual(1900, prop.max_afterburner_temp)
        prop.hpc_pressure_ratio = 3.8
        Assert.assertEqual(3.8, prop.hpc_pressure_ratio)
        prop.lpc_pressure_ratio = 4.1
        Assert.assertEqual(4.1, prop.lpc_pressure_ratio)
        prop.fan_pressure_ratio = 3.6
        Assert.assertEqual(3.6, prop.fan_pressure_ratio)

        prop.fuel_type = JET_FUEL_TYPE.HYDROGEN
        Assert.assertEqual(JET_FUEL_TYPE.HYDROGEN, prop.fuel_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            afprop: "FuelModelKeroseneAFPROP" = prop.fuel_mode_as_afprop
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            cea: "FuelModelKeroseneCEA" = prop.fuel_mode_as_cea

        prop.fuel_type = JET_FUEL_TYPE.KEROSENE_AFPROP
        self.TestFuelAFPROP(prop.fuel_mode_as_afprop)
        prop.fuel_type = JET_FUEL_TYPE.KEROSENE_CEA
        self.TestFuelCEA(prop.fuel_mode_as_cea)

        self.TestPropulsionEfficiencies(prop.efficiencies_and_losses)

    def TestTurbojetBasicAB(self, prop: "AdvancedFixedWingTurbojetBasicABProp"):
        prop.can_use_afterburner = False
        Assert.assertEqual(False, prop.can_use_afterburner)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            prop.afterburner_on = False
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            prop.max_afterburner_temp = 2000

        prop.can_use_afterburner = True
        prop.design_altitude = 33100
        Assert.assertEqual(33100, prop.design_altitude)
        prop.design_mach = 0.75
        Assert.assertEqual(0.75, prop.design_mach)
        prop.design_thrust = 80000
        Assert.assertEqual(80000, prop.design_thrust)
        prop.afterburner_on = True
        Assert.assertTrue(prop.afterburner_on)

        prop.max_compression_temp = 800
        Assert.assertEqual(800, prop.max_compression_temp)
        prop.max_burner_temp = 1400
        Assert.assertEqual(1400, prop.max_burner_temp)
        prop.max_afterburner_temp = 1900
        Assert.assertEqual(1900, prop.max_afterburner_temp)
        prop.hpc_pressure_ratio = 3.8
        Assert.assertEqual(3.8, prop.hpc_pressure_ratio)
        prop.lpc_pressure_ratio = 3.7
        Assert.assertEqual(3.7, prop.lpc_pressure_ratio)

        prop.fuel_type = JET_FUEL_TYPE.HYDROGEN
        Assert.assertEqual(JET_FUEL_TYPE.HYDROGEN, prop.fuel_type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            afprop: "FuelModelKeroseneAFPROP" = prop.fuel_mode_as_afprop
        with pytest.raises(Exception, match=RegexSubstringMatch("must be")):
            cea: "FuelModelKeroseneCEA" = prop.fuel_mode_as_cea

        prop.fuel_type = JET_FUEL_TYPE.KEROSENE_AFPROP
        self.TestFuelAFPROP(prop.fuel_mode_as_afprop)
        prop.fuel_type = JET_FUEL_TYPE.KEROSENE_CEA
        self.TestFuelCEA(prop.fuel_mode_as_cea)

        self.TestPropulsionEfficiencies(prop.efficiencies_and_losses)

    # endregion

    # region PrivateProcedureMethods

    def EmptyProcedures(self):
        index: int = EarlyBoundTests.AG_Procedures.count - 1
        while index >= 0:
            EarlyBoundTests.AG_Procedures.remove_at_index(index)

            index -= 1

        Assert.assertEqual(0, EarlyBoundTests.AG_Procedures.count)

    def TestProcedureName(self, proc: "IProcedure", name: str):
        Assert.assertEqual(name, proc.name)
        proc.name = "Name Test"
        Assert.assertEqual("Name Test", proc.name)

    def AltitudeOptions(self, alt: "AltitudeOptions"):
        alt.use_default_cruise_altitude = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            alt.altitude = 10000

        alt.use_default_cruise_altitude = False
        alt.altitude_reference = AGL_MSL.ALTITUDE_AGL
        alt.altitude = 5000
        Assert.assertEqual(AGL_MSL.ALTITUDE_AGL, alt.altitude_reference)
        Assert.assertEqual(5000, alt.altitude)

    def AltitudeMSLOptions(self, altitudeOpts: "AltitudeMSLOptions"):
        altitudeOpts.use_default_cruise_altitude = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            altitudeOpts.msl_altitude = 10000

        altitudeOpts.use_default_cruise_altitude = False
        altitudeOpts.msl_altitude = 10000
        Assert.assertEqual(10000, altitudeOpts.msl_altitude)

    def AltitudeMSLAndLevelOffOptions(self, altitudeOpts: "AltitudeMSLAndLevelOffOptions"):
        altitudeOpts.use_default_cruise_altitude = True
        # TryCatchAssertBlock.ExpectedException("must be ", delegate () { altitudeOpts.MSLAltitude = 10000; });

        altitudeOpts.use_default_cruise_altitude = False
        altitudeOpts.msl_altitude = 10000
        Assert.assertEqual(10000, altitudeOpts.msl_altitude)

        altitudeOpts.must_level_off = False
        # TryCatchAssertBlock.ExpectedException("must be ", delegate () { altitudeOpts.LevelOffMode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER; });
        altitudeOpts.must_level_off = True
        altitudeOpts.level_off_mode = ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER
        Assert.assertEqual(ALTITUDE_CONSTRAINT_MANEUVER_MODE.LEVEL_OFF_LEFT_TURN_MANEUVER, altitudeOpts.level_off_mode)

    def ArcAltitudeOptions(self, alt: "ArcAltitudeOptions"):
        alt.use_default_cruise_altitude = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            alt.start_arc_altitude = 10001
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            alt.stop_arc_altitude = 10002

        alt.use_default_cruise_altitude = False
        alt.start_arc_altitude = 10001
        Assert.assertEqual(10001, alt.start_arc_altitude)
        alt.stop_arc_altitude = 10002
        Assert.assertEqual(10002, alt.stop_arc_altitude)

    def ArcAltitudeAndDelayOptions(self, alt: "ArcAltitudeAndDelayOptions"):
        alt.use_default_cruise_altitude = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            alt.delay_arc_climb_descents = True
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            alt.start_arc_altitude = 10001
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            alt.stop_arc_altitude = 10002

        alt.use_default_cruise_altitude = False
        alt.delay_arc_climb_descents = True
        Assert.assertTrue(alt.delay_arc_climb_descents)
        alt.start_arc_altitude = 10001
        Assert.assertEqual(10001, alt.start_arc_altitude)
        alt.stop_arc_altitude = 10002
        Assert.assertEqual(10002, alt.stop_arc_altitude)

    def HoverAltitudeOptions(self, alt: "HoverAltitudeOptions"):
        alt.altitude_reference = AGL_MSL.ALTITUDE_AGL
        Assert.assertEqual(AGL_MSL.ALTITUDE_AGL, alt.altitude_reference)

        alt.altitude = 5000
        Assert.assertEqual(5000, alt.altitude)

        alt.final_altitude_rate = VTOL_RATE_MODE.ALWAYS_STOP
        Assert.assertEqual(VTOL_RATE_MODE.ALWAYS_STOP, alt.final_altitude_rate)

    def ArcOptions(self, arc: "ArcOptions"):
        arc.turn_direction = TURN_DIRECTION.TURN_RIGHT
        Assert.assertEqual(TURN_DIRECTION.TURN_RIGHT, arc.turn_direction)

        arc.start_bearing = 5
        bearing: typing.Any = arc.start_bearing
        Assert.assertEqual(5, float(bearing))
        arc.use_magnetic_heading = False
        Assert.assertEqual(False, arc.use_magnetic_heading)

        arc.radius = 11
        Assert.assertEqual(11, arc.radius)
        arc.turn_angle = 100
        turnAngle: typing.Any = arc.turn_angle
        Assert.assertEqual(100, float(turnAngle))

    def NavigationOptions(self, navOpts: "NavigationOptions"):
        tolerance: float = 1e-09

        navOpts.nav_mode = POINT_TO_POINT_MODE.ARRIVE_ON_COURSE_FOR_NEXT
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            navOpts.arrive_on_course = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("must be ")):
            navOpts.use_magnetic_heading = True

        navOpts.nav_mode = POINT_TO_POINT_MODE.ARRIVE_ON_COURSE
        navOpts.arrive_on_course = 1
        navOpts.use_magnetic_heading = True
        course: typing.Any = navOpts.arrive_on_course
        Assert.assertAlmostEqual(1, float(course), delta=tolerance)
        Assert.assertTrue(navOpts.use_magnetic_heading)

    def EnrouteOptions(self, enrouteOpts: "EnrouteOptions"):
        enrouteOpts.use_max_speed_turns = True
        enrouteOpts.max_turn_radius_factor = 3.5
        Assert.assertTrue(enrouteOpts.use_max_speed_turns)
        Assert.assertEqual(3.5, enrouteOpts.max_turn_radius_factor)

    def EnrouteAndDelayOptions(self, enrouteOpts: "IEnrouteAndDelayOptions"):
        enrouteOpts.delay_enroute_climb_descents = True
        enrouteOpts.use_max_speed_turns = True
        enrouteOpts.max_turn_radius_factor = 3.5
        Assert.assertTrue(enrouteOpts.delay_enroute_climb_descents)
        Assert.assertTrue(enrouteOpts.use_max_speed_turns)
        Assert.assertEqual(3.5, enrouteOpts.max_turn_radius_factor)

    def EnrouteCruiseAirspeed(self, airspeedOpts: "CruiseAirspeedOptions"):
        tolerance: float = 1e-09

        airspeedOpts.cruise_speed_type = CRUISE_SPEED.MAX_AIRSPEED
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            airspeedOpts.set_other_airspeed(AIRSPEED_TYPE.TAS, 200)

        airspeedOpts.cruise_speed_type = CRUISE_SPEED.OTHER_AIRSPEED
        airspeedOpts.set_other_airspeed(AIRSPEED_TYPE.TAS, 200)
        Assert.assertAlmostEqual(200, airspeedOpts.other_airspeed, delta=tolerance)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, airspeedOpts.other_airspeed_type)

        airspeedOpts.set_other_airspeed(AIRSPEED_TYPE.MACH, 0.5)
        Assert.assertAlmostEqual(0.5, airspeedOpts.other_airspeed, delta=tolerance)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, airspeedOpts.other_airspeed_type)

    def EnrouteCruiseAirspeedAndProfile(self, airspeedOpts: "ICruiseAirspeedAndProfileOptions"):
        tolerance: float = 1e-09

        airspeedOpts.fly_cruise_airspeed_profile = False
        Assert.assertEqual(False, airspeedOpts.fly_cruise_airspeed_profile)

        airspeedOpts.cruise_speed_type = CRUISE_SPEED.MAX_AIRSPEED
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set")):
            airspeedOpts.set_other_airspeed(AIRSPEED_TYPE.TAS, 200)

        airspeedOpts.cruise_speed_type = CRUISE_SPEED.OTHER_AIRSPEED
        airspeedOpts.set_other_airspeed(AIRSPEED_TYPE.TAS, 200)
        Assert.assertAlmostEqual(200, airspeedOpts.other_airspeed, delta=tolerance)
        Assert.assertEqual(AIRSPEED_TYPE.TAS, airspeedOpts.other_airspeed_type)

        airspeedOpts.set_other_airspeed(AIRSPEED_TYPE.MACH, 0.5)
        Assert.assertAlmostEqual(0.5, airspeedOpts.other_airspeed, delta=tolerance)
        Assert.assertEqual(AIRSPEED_TYPE.MACH, airspeedOpts.other_airspeed_type)

    def EnrouteTurnDirection(self, turnOpts: "EnrouteTurnDirectionOptions"):
        turnOpts.enroute_first_turn = NAVIGATOR_TURN_DIRECTION.NAVIGATOR_TURN_LEFT
        Assert.assertEqual(NAVIGATOR_TURN_DIRECTION.NAVIGATOR_TURN_LEFT, turnOpts.enroute_first_turn)
        turnOpts.enroute_second_turn = NAVIGATOR_TURN_DIRECTION.NAVIGATOR_TURN_RIGHT
        Assert.assertEqual(NAVIGATOR_TURN_DIRECTION.NAVIGATOR_TURN_RIGHT, turnOpts.enroute_second_turn)

    def VerticalPlaneOptions(self, vertOpts: "IVerticalPlaneOptions"):
        vertOpts.max_vert_plane_radius_factor = 2.5
        Assert.assertEqual(2.5, vertOpts.max_vert_plane_radius_factor)
        vertOpts.min_enroute_flight_path_angle = -89.1
        minAng: typing.Any = vertOpts.min_enroute_flight_path_angle
        Assert.assertEqual(-89.1, float(minAng))
        vertOpts.max_enroute_flight_path_angle = 89.2
        maxAng: typing.Any = vertOpts.max_enroute_flight_path_angle
        Assert.assertEqual(89.2, float(maxAng))

    def VerticalPlaneAndFlightPathOptions(self, vertOpts: "VerticalPlaneAndFlightPathOptions"):
        vertOpts.final_flight_path_angle = 3
        fpa: typing.Any = vertOpts.final_flight_path_angle
        Assert.assertEqual(3, float(fpa))
        vertOpts.max_vert_plane_radius_factor = 2.5
        Assert.assertEqual(2.5, vertOpts.max_vert_plane_radius_factor)
        vertOpts.min_enroute_flight_path_angle = -89.1
        minAng: typing.Any = vertOpts.min_enroute_flight_path_angle
        Assert.assertEqual(-89.1, float(minAng))
        vertOpts.max_enroute_flight_path_angle = 89.2
        maxAng: typing.Any = vertOpts.max_enroute_flight_path_angle
        Assert.assertEqual(89.2, float(maxAng))

    def ArcVerticalPlane(self, vertOpts: "ArcVerticalPlaneOptions"):
        vertOpts.start_arc_flight_path_angle = 3
        startArc: typing.Any = vertOpts.start_arc_flight_path_angle
        Assert.assertEqual(3, float(startArc))
        vertOpts.stop_arc_flight_path_angle = 2
        stopArc: typing.Any = vertOpts.stop_arc_flight_path_angle
        Assert.assertEqual(2, float(stopArc))
        vertOpts.max_vert_plane_radius_factor = 2.5
        Assert.assertEqual(2.5, vertOpts.max_vert_plane_radius_factor)
        vertOpts.min_enroute_flight_path_angle = -89.1
        minAng: typing.Any = vertOpts.min_enroute_flight_path_angle
        Assert.assertEqual(-89.1, float(minAng))
        vertOpts.max_enroute_flight_path_angle = 89.2
        maxAng: typing.Any = vertOpts.max_enroute_flight_path_angle
        Assert.assertEqual(89.2, float(maxAng))

    # endregion

    # region PrivateBasicManeuverMethods
    def BasicManeuverAirspeedOptions(self, airspeedOptions: "BasicManeuverAirspeedOptions"):
        airspeedMode: "BASIC_MANEUVER_AIRSPEED_MODE"
        for airspeedMode in Enum.GetValues(clr.TypeOf(BASIC_MANEUVER_AIRSPEED_MODE)):
            airspeedOptions.airspeed_mode = airspeedMode
            Assert.assertEqual(airspeedMode, airspeedOptions.airspeed_mode)
            if airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_CURRENT_AIRSPEED:
                airspeedOptions.maintain_airspeed_type = AIRSPEED_TYPE.MACH
                Assert.assertEqual(AIRSPEED_TYPE.MACH, airspeedOptions.maintain_airspeed_type)
                airspeedOptions.maintain_airspeed_type = AIRSPEED_TYPE.EAS
                Assert.assertEqual(AIRSPEED_TYPE.EAS, airspeedOptions.maintain_airspeed_type)
                airspeedOptions.maintain_airspeed_type = AIRSPEED_TYPE.CAS
                Assert.assertEqual(AIRSPEED_TYPE.CAS, airspeedOptions.maintain_airspeed_type)
                airspeedOptions.maintain_airspeed_type = AIRSPEED_TYPE.TAS
                Assert.assertEqual(AIRSPEED_TYPE.TAS, airspeedOptions.maintain_airspeed_type)

            if airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_SPECIFIED_AIRSPEED:
                airspeedOptions.specified_airspeed = 111
                Assert.assertEqual(111, airspeedOptions.specified_airspeed)

                airspeedOptions.specified_airspeed_type = AIRSPEED_TYPE.MACH
                Assert.assertEqual(AIRSPEED_TYPE.MACH, airspeedOptions.specified_airspeed_type)
                airspeedOptions.specified_airspeed_type = AIRSPEED_TYPE.EAS
                Assert.assertEqual(AIRSPEED_TYPE.EAS, airspeedOptions.specified_airspeed_type)
                airspeedOptions.specified_airspeed_type = AIRSPEED_TYPE.CAS
                Assert.assertEqual(AIRSPEED_TYPE.CAS, airspeedOptions.specified_airspeed_type)
                airspeedOptions.specified_airspeed_type = AIRSPEED_TYPE.TAS
                Assert.assertEqual(AIRSPEED_TYPE.TAS, airspeedOptions.specified_airspeed_type)

                airspeedOptions.specified_accel_decel_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
                Assert.assertEqual(PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE, airspeedOptions.specified_accel_decel_mode)

                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to override")):
                    airspeedOptions.specified_accel_decel_g = 200

                airspeedOptions.specified_accel_decel_mode = PERF_MODEL_OVERRIDE.OVERRIDE
                Assert.assertEqual(PERF_MODEL_OVERRIDE.OVERRIDE, airspeedOptions.specified_accel_decel_mode)

                airspeedOptions.specified_accel_decel_g = 200
                Assert.assertEqual(200, airspeedOptions.specified_accel_decel_g)

            if (
                (
                    (
                        (airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_MIN_AIRSPEED)
                        or (airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_MAX_ENDURANCE_AIRSPEED)
                    )
                    or (airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_MAX_RANGE_AIRSPEED)
                )
                or (airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_MAX_AIRSPEED)
            ) or (airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.MAINTAIN_MAX_PERFORMANCE_AIRSPEED):
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: float = airspeedOptions.accel_g
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: "PERF_MODEL_OVERRIDE" = airspeedOptions.accel_mode
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: float = airspeedOptions.decel_g
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: "PERF_MODEL_OVERRIDE" = airspeedOptions.decel_mode
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: float = airspeedOptions.interpolate_end_g
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: float = airspeedOptions.interpolate_end_time
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: float = airspeedOptions.interpolate_init_g
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: bool = airspeedOptions.interpolate_stop_at_end_time
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: "AIRSPEED_TYPE" = airspeedOptions.maintain_airspeed_type
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: float = airspeedOptions.specified_accel_decel_g
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: "PERF_MODEL_OVERRIDE" = airspeedOptions.specified_accel_decel_mode
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: float = airspeedOptions.specified_airspeed
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: "AIRSPEED_TYPE" = airspeedOptions.specified_airspeed_type
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: float = airspeedOptions.throttle
                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to the corresponding mode")):
                    value: "PropulsionThrust" = airspeedOptions.thrust

            if airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.ACCEL_AT_G:
                airspeedOptions.accel_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
                Assert.assertEqual(PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE, airspeedOptions.accel_mode)

                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to override")):
                    airspeedOptions.accel_g = 300

                airspeedOptions.accel_mode = PERF_MODEL_OVERRIDE.OVERRIDE
                Assert.assertEqual(PERF_MODEL_OVERRIDE.OVERRIDE, airspeedOptions.accel_mode)

                airspeedOptions.accel_g = 300
                Assert.assertEqual(300, airspeedOptions.accel_g)

            if airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.DECEL_AT_G:
                airspeedOptions.decel_mode = PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE
                Assert.assertEqual(PERF_MODEL_OVERRIDE.PERF_MODEL_VALUE, airspeedOptions.decel_mode)

                with pytest.raises(Exception, match=RegexSubstringMatch("must be set to override")):
                    airspeedOptions.decel_g = 400

                airspeedOptions.decel_mode = PERF_MODEL_OVERRIDE.OVERRIDE
                Assert.assertEqual(PERF_MODEL_OVERRIDE.OVERRIDE, airspeedOptions.decel_mode)

                airspeedOptions.decel_g = 400
                Assert.assertEqual(400, airspeedOptions.decel_g)

            if airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.ACCEL_DECEL_UNDER_GRAVITY:
                pass

            if airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.ACCEL_DECEL_AERO_PROP:
                airspeedOptions.throttle = 55
                Assert.assertEqual(55, airspeedOptions.throttle)

            if airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.THRUST:
                self.Test_IAgAvtrPropulsionThrust(airspeedOptions.thrust)

            if airspeedMode == BASIC_MANEUVER_AIRSPEED_MODE.INTERPOLATE_ACCEL_DECEL:
                airspeedOptions.interpolate_init_g = 5
                Assert.assertEqual(5, airspeedOptions.interpolate_init_g)
                airspeedOptions.interpolate_end_g = 6
                Assert.assertEqual(6, airspeedOptions.interpolate_end_g)
                airspeedOptions.interpolate_end_time = 7
                Assert.assertEqual(7, airspeedOptions.interpolate_end_time)

                airspeedOptions.interpolate_stop_at_end_time = False
                Assert.assertFalse(airspeedOptions.interpolate_stop_at_end_time)
                airspeedOptions.interpolate_stop_at_end_time = True
                Assert.assertTrue(airspeedOptions.interpolate_stop_at_end_time)

        airspeedOptions.min_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED, airspeedOptions.min_speed_limits
        )
        airspeedOptions.min_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.STOP_IF_VIOLATED
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.STOP_IF_VIOLATED, airspeedOptions.min_speed_limits
        )
        airspeedOptions.min_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.ERROR_IF_VIOLATED
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.ERROR_IF_VIOLATED, airspeedOptions.min_speed_limits
        )
        airspeedOptions.min_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.IGNORE_IF_VIOLATED
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.IGNORE_IF_VIOLATED, airspeedOptions.min_speed_limits
        )

        airspeedOptions.max_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.CONSTRAIN_IF_VIOLATED, airspeedOptions.max_speed_limits
        )
        airspeedOptions.max_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.STOP_IF_VIOLATED
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.STOP_IF_VIOLATED, airspeedOptions.max_speed_limits
        )
        airspeedOptions.max_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.ERROR_IF_VIOLATED
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.ERROR_IF_VIOLATED, airspeedOptions.max_speed_limits
        )
        airspeedOptions.max_speed_limits = BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.IGNORE_IF_VIOLATED
        Assert.assertEqual(
            BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS.IGNORE_IF_VIOLATED, airspeedOptions.max_speed_limits
        )

    # endregion

    # region PrivateSiteMethods

    def TestSiteName(self, site: "ISite", name: str):
        Assert.assertEqual(name, site.name)
        site.name = "Name Test"
        Assert.assertEqual("Name Test", site.name)
        site.name = name

    def TestCatalogVTOLPoint(
        self, siteVTOLPointFromCatalog: "SiteVTOLPointFromCatalog", catVTOLPoint: "ICatalogVTOLPoint"
    ):
        siteVTOLPointFromCatalog.set_catalog_vtol_point(catVTOLPoint)
        VTOLPointAsItem: "ICatalogItem" = clr.CastAs(catVTOLPoint, ICatalogItem)
        VTOLPointName: str = VTOLPointAsItem.name
        Assert.assertEqual(VTOLPointName, siteVTOLPointFromCatalog.get_as_site().name)
        catVTOLPoint2: "ICatalogItem" = clr.CastAs(siteVTOLPointFromCatalog.get_catalog_vtol_point(), ICatalogItem)
        Assert.assertEqual(VTOLPointName, catVTOLPoint2.name)

    def TestCatalogWaypoint(self, siteWaypointFromCatalog: "SiteWaypointFromCatalog", catWaypoint: "ICatalogWaypoint"):
        siteWaypointFromCatalog.set_catalog_waypoint(catWaypoint)
        waypointAsItem: "ICatalogItem" = clr.CastAs(catWaypoint, ICatalogItem)
        waypointName: str = waypointAsItem.name
        Assert.assertEqual(waypointName, siteWaypointFromCatalog.get_as_site().name)
        catWaypoint2: "ICatalogItem" = clr.CastAs(siteWaypointFromCatalog.get_catalog_waypoint(), ICatalogItem)
        Assert.assertEqual(waypointName, catWaypoint2.name)

    # endregion

    # region Test_IAgAvtrBasicManeuverTargetPosVel
    def Test_IAgAvtrBasicManeuverTargetPosVel(self, targetPosVel: "BasicManeuverTargetPositionVel"):
        # Initial state
        Assert.assertEqual("DisabledTargetPosVel", targetPosVel.target_position_vel_type_string)
        Assert.assertEqual(TARGET_POSITION_VEL_TYPE.DISABLED_POSITION_VEL, targetPosVel.target_position_vel_type)

        targetPosVel.target_position_vel_type = TARGET_POSITION_VEL_TYPE.DISABLED_POSITION_VEL
        Assert.assertEqual("DisabledTargetPosVel", targetPosVel.target_position_vel_type_string)
        Assert.assertEqual(TARGET_POSITION_VEL_TYPE.DISABLED_POSITION_VEL, targetPosVel.target_position_vel_type)

        targetPosVel.target_position_vel_type = TARGET_POSITION_VEL_TYPE.SURFACE_TARGET_POSITION_VEL
        Assert.assertEqual("NoisySurfaceTargetPosVel", targetPosVel.target_position_vel_type_string)
        Assert.assertEqual(TARGET_POSITION_VEL_TYPE.SURFACE_TARGET_POSITION_VEL, targetPosVel.target_position_vel_type)

        targetPosVel.target_position_vel_type = TARGET_POSITION_VEL_TYPE.BEARING_RANGE_TARGET_POSITION_VEL
        Assert.assertEqual("NoisyBearingRangeTargetPosVel", targetPosVel.target_position_vel_type_string)
        Assert.assertEqual(
            TARGET_POSITION_VEL_TYPE.BEARING_RANGE_TARGET_POSITION_VEL, targetPosVel.target_position_vel_type
        )

        targetPosVel.target_position_vel_type_string = "DisabledTargetPosVel"
        Assert.assertEqual("DisabledTargetPosVel", targetPosVel.target_position_vel_type_string)
        Assert.assertEqual(TARGET_POSITION_VEL_TYPE.DISABLED_POSITION_VEL, targetPosVel.target_position_vel_type)

        targetPosVel.target_position_vel_type_string = "NoisySurfaceTargetPosVel"
        Assert.assertEqual("NoisySurfaceTargetPosVel", targetPosVel.target_position_vel_type_string)
        Assert.assertEqual(TARGET_POSITION_VEL_TYPE.SURFACE_TARGET_POSITION_VEL, targetPosVel.target_position_vel_type)

        targetPosVel.target_position_vel_type_string = "NoisyBearingRangeTargetPosVel"
        Assert.assertEqual("NoisyBearingRangeTargetPosVel", targetPosVel.target_position_vel_type_string)
        Assert.assertEqual(
            TARGET_POSITION_VEL_TYPE.BEARING_RANGE_TARGET_POSITION_VEL, targetPosVel.target_position_vel_type
        )

        with pytest.raises(Exception, match=RegexSubstringMatch("Incorrect PosVel Type specified")):
            targetPosVel.target_position_vel_type_string = "BogusTargetPosVel"

        targetPosVel.target_position_vel_type = TARGET_POSITION_VEL_TYPE.DISABLED_POSITION_VEL
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to noisy bearing range")):
            nbr1: "BasicManeuverTargetPositionVelNoisyBrgRng" = targetPosVel.mode_as_noisy_brg_rng
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to noisy surface target")):
            nst1: "BasicManeuverTargetPositionVelNoisySurfTgt" = targetPosVel.mode_as_noisy_surf_tgt

        targetPosVel.target_position_vel_type = TARGET_POSITION_VEL_TYPE.SURFACE_TARGET_POSITION_VEL
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to noisy bearing range")):
            nbr1: "BasicManeuverTargetPositionVelNoisyBrgRng" = targetPosVel.mode_as_noisy_brg_rng
        self.Test_IAgAvtrBasicManeuverTargetPosVelNoisySurfTgt(targetPosVel.mode_as_noisy_surf_tgt)

        targetPosVel.target_position_vel_type = TARGET_POSITION_VEL_TYPE.BEARING_RANGE_TARGET_POSITION_VEL
        with pytest.raises(Exception, match=RegexSubstringMatch("must be set to noisy surface target")):
            nst1: "BasicManeuverTargetPositionVelNoisySurfTgt" = targetPosVel.mode_as_noisy_surf_tgt
        self.Test_IAgAvtrBasicManeuverTargetPosVelNoisyBrnRng(targetPosVel.mode_as_noisy_brg_rng)

    # endregion

    # region Test_IAgAvtrBasicManeuverTargetPosVelNoisyBrnRng
    def Test_IAgAvtrBasicManeuverTargetPosVelNoisyBrnRng(
        self, noisyBrgRng: "BasicManeuverTargetPositionVelNoisyBrgRng"
    ):
        noisyBrgRng.new_random_engine_seed()

        noisyBrgRng.set_base_dyn_state_link_name("Aircraft/NUNIT_VBS_Test")
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            noisyBrgRng.set_base_dyn_state_link_name("Bogus")

        noisyBrgRng.smoothing_constant = 0.1
        Assert.assertEqual(0.1, noisyBrgRng.smoothing_constant)
        noisyBrgRng.smoothing_constant = 0.9
        Assert.assertEqual(0.9, noisyBrgRng.smoothing_constant)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            noisyBrgRng.smoothing_constant = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            noisyBrgRng.smoothing_constant = 1

        noisyBrgRng.velocity_time_step = 0.001
        Assert.assertEqual(0.001, noisyBrgRng.velocity_time_step)
        noisyBrgRng.velocity_time_step = 5
        Assert.assertEqual(5, noisyBrgRng.velocity_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            noisyBrgRng.velocity_time_step = 0.0005

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            noisyBrgRng.velocity_time_step = 6

        noisyBrgRng.angle_error_std_dev = 0
        Assert.assertEqual(0, noisyBrgRng.angle_error_std_dev)
        noisyBrgRng.angle_error_std_dev = 30
        Assert.assertAlmostEqual(30, noisyBrgRng.angle_error_std_dev, delta=1e-05)

        noisyBrgRng.range_error_std_dev = 0
        Assert.assertEqual(0, noisyBrgRng.range_error_std_dev)
        noisyBrgRng.range_error_std_dev = 40
        Assert.assertAlmostEqual(40, noisyBrgRng.range_error_std_dev, delta=1e-05)

        noisyBrgRng.apply_position_vel()
        # System.Windows.Forms.MessageBox.Show("noisyBrnRng done");

        noisyBrgRng.cancel_position_vel()

    # endregion

    # region Test_IAgAvtrBasicManeuverTargetPosVelNoisySurfTgt
    def Test_IAgAvtrBasicManeuverTargetPosVelNoisySurfTgt(
        self, noisySurfTgt: "BasicManeuverTargetPositionVelNoisySurfTgt"
    ):
        noisySurfTgt.new_random_engine_seed()

        noisySurfTgt.set_base_dyn_state_link_name("Aircraft/NUNIT_CSharp_Test")
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            noisySurfTgt.set_base_dyn_state_link_name("Bogus")

        noisySurfTgt.measurement_time_step = 0.001
        Assert.assertEqual(0.001, noisySurfTgt.measurement_time_step)
        noisySurfTgt.measurement_time_step = 10
        Assert.assertEqual(10, noisySurfTgt.measurement_time_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            noisySurfTgt.measurement_time_step = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid.")):
            noisySurfTgt.measurement_time_step = -1

        noisySurfTgt.position_cep = 0
        Assert.assertEqual(0, noisySurfTgt.position_cep)
        noisySurfTgt.position_cep = 20
        Assert.assertEqual(20, noisySurfTgt.position_cep)

        noisySurfTgt.course_error = 0
        Assert.assertEqual(0, noisySurfTgt.course_error)
        noisySurfTgt.course_error = 30
        Assert.assertAlmostEqual(30, noisySurfTgt.course_error, delta=1e-05)

        noisySurfTgt.speed_error = 0
        Assert.assertEqual(0, noisySurfTgt.speed_error)
        noisySurfTgt.speed_error = 40
        Assert.assertAlmostEqual(40, noisySurfTgt.speed_error, delta=1e-05)

        noisySurfTgt.apply_position_vel()
        # System.Windows.Forms.MessageBox.Show("noisySurfTgt done");

        noisySurfTgt.cancel_position_vel()

    # endregion
