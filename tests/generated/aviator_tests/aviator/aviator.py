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
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eAircraft, "AviatorAC")), IAircraft
        )
        # Set to Propagator to Aviator
        EarlyBoundTests.AG_AC.set_route_type(AgEVePropagatorType.ePropagatorAviator)
        # Get the aircrafts route (still on the STKObjects side)
        aircraftRoute: "IVehiclePropagatorAviator" = clr.CastAs(EarlyBoundTests.AG_AC.route, IVehiclePropagatorAviator)
        # Get the Aviator propagator
        EarlyBoundTests.AG_AvtrProp = clr.CastAs(aircraftRoute.avtr_propagator, IAviatorPropagator)
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
        EarlyBoundTests.AG_AvtrAircraft = clr.CastAs(EarlyBoundTests.AG_Mission.vehicle, IAircraftModel)
        # Create a target object
        EarlyBoundTests.AG_Target = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eTarget, "Target")

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
    AG_AC: "IAircraft" = None
    AG_AvtrProp: "IAviatorPropagator" = None
    AG_AvtrCatalog: "ICatalog" = None
    AG_AvtrAircraftModels: "IAircraftModels" = None
    AG_Mission: "IMission" = None
    AG_Phases: "IPhaseCollection" = None
    AG_Procedures: "IProcedureCollection" = None
    AG_AvtrAircraft: "IAircraftModel" = None
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
        acCopy: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        defConfig: "IConfiguration" = acCopy.default_configuration

        defConfig.base_drag_index = 1
        Assert.assertEqual(1, defConfig.base_drag_index)

        defConfig.set_empty_cg(1, 2, 3)
        Assert.assertEqual(1, defConfig.empty_cgx)
        Assert.assertEqual(2, defConfig.empty_cgy)
        Assert.assertEqual(3, defConfig.empty_cgz)

        defConfig2: "IConfiguration" = EarlyBoundTests.AG_AvtrAircraft.default_configuration
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
        acCopy: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        defConfig: "IConfiguration" = acCopy.default_configuration

        stations: "IStationCollection" = defConfig.get_stations()
        stationCount: int = Array.Length(stations.station_names)

        totalCapacity: float = defConfig.total_capacity
        initialState: float = defConfig.initial_fuel_state

        internalTank: "IFuelTankInternal" = stations.add_internal_fuel_tank()
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

        payloadStation: "IPayloadStation" = stations.add_payload_station()
        stationCount += 1
        payloadStation.name = "Payload Station Name Test"
        Assert.assertTrue(stations.contains_station("Payload Station Name Test"))
        Assert.assertEqual("Payload Station Name Test", stations.station_names[(stationCount - 1)])
        Assert.assertEqual(stationCount, stations.count)

        externalTank: "IFuelTankExternal" = payloadStation.add_external_fuel_tank()
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

        currentTank: "IFuelTankInternal" = stations.add_internal_fuel_tank()
        currentTank.name = "4"
        currentTank = stations.add_internal_fuel_tank()
        currentTank.name = "1"
        currentPayloadStation: "IPayloadStation" = stations.add_payload_station()
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

        tank: "IFuelTankInternal" = clr.CastAs(stations[0], IFuelTankInternal)
        Assert.assertEqual("1", tank.name)
        station3: "IPayloadStation" = clr.CastAs(stations[3], IPayloadStation)
        Assert.assertEqual("3", station3.name)

        def action1():
            testVal: "IStation" = stations[-1]

        TryCatchAssertBlock.ExpectedException("Invalid index", action1)

        def action2():
            testVal: "IStation" = stations[stations.count]

        TryCatchAssertBlock.ExpectedException("Invalid index", action2)

        stations.remove_at_index(3)
        Assert.assertEqual(6, stations.count)
        Assert.assertEqual("2", stations.station_names[2])
        Assert.assertEqual("4", stations.station_names[3])

        def action3():
            stations.remove_at_index(-1)

        TryCatchAssertBlock.ExpectedException("Invalid index", action3)

        def action4():
            stations.remove_at_index(stations.count)

        TryCatchAssertBlock.ExpectedException("Invalid index", action4)

        acCopy.get_as_catalog_item().remove()

    # endregion

    # region Wind
    @category("Weather Tests")
    @category("ExcludeOnLinux")
    def test_Wind(self):
        tolerance: float = 1e-09

        wind: "IWindModel" = EarlyBoundTests.AG_Mission.wind_model

        def action5():
            wind.wind_model_source = AgEAvtrWindAtmosModelSource.eProcedureModel

        TryCatchAssertBlock.ExpectedException("procedure model", action5)

        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.wind_model_type = AgEAvtrWindModelType.eConstantWind
        addsWind: "IWindModelADDS" = None

        def action6():
            addsWind = wind.mode_as_adds

        TryCatchAssertBlock.ExpectedException("must be set", action6)

        constWind: "IWindModelConstant" = wind.mode_as_constant
        constWind.wind_speed = 1
        Assert.assertAlmostEqual(1, constWind.wind_speed, delta=tolerance)
        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eScenarioModel
        wind.wind_model_type = AgEAvtrWindModelType.eConstantWind
        wind.copy()
        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.paste()

        Assert.assertAlmostEqual(0, constWind.wind_speed, delta=tolerance)

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        procWind: "IWindModel" = proc1.wind_model
        procWind.wind_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        procConstWind: "IWindModelConstant" = procWind.mode_as_constant

        Assert.assertAlmostEqual(0, procConstWind.wind_speed, delta=tolerance)

        def action7():
            procWind.wind_model_type = AgEAvtrWindModelType.eConstantWind

        TryCatchAssertBlock.ExpectedException("cannot be edited from the procedure", action7)

        procWind.wind_model_source = AgEAvtrWindAtmosModelSource.eProcedureModel
        procWind.wind_model_type = AgEAvtrWindModelType.eConstantWind
        procConstWind.wind_speed = 1
        Assert.assertAlmostEqual(1, procConstWind.wind_speed, delta=tolerance)

        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eScenarioModel
        wind.copy()
        procWind.paste()
        Assert.assertAlmostEqual(0, procConstWind.wind_speed, delta=tolerance)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region WindModelConstant
    @category("Weather Tests")
    def test_WindModelConstant(self):
        tolerance: float = 1e-09

        wind: "IWindModel" = EarlyBoundTests.AG_Mission.wind_model
        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.wind_model_type = AgEAvtrWindModelType.eConstantWind
        constWind: "IWindModelConstant" = wind.mode_as_constant

        constWind.name = "Constant Name Test"
        Assert.assertEqual("Constant Name Test", constWind.name)
        constWind.wind_speed = 1
        Assert.assertAlmostEqual(1, constWind.wind_speed, delta=tolerance)

        wind.wind_model_type = AgEAvtrWindModelType.eDisabled

        def action8():
            constWind.wind_speed = 1

        TryCatchAssertBlock.ExpectedException("must be set", action8)

        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eScenarioModel
        wind.copy()
        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.paste()

    # endregion

    # region WindModelADDS
    @category("Weather Tests")
    @category("ExcludeOnLinux")
    def test_WindModelADDS(self):
        wind: "IWindModel" = EarlyBoundTests.AG_Mission.wind_model
        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.wind_model_type = AgEAvtrWindModelType.eADDS
        ADDSWind: "IWindModelADDS" = wind.mode_as_adds

        ADDSWind.name = "ADDS Name Test"
        Assert.assertEqual("ADDS Name Test", ADDSWind.name)

        ADDSWind.interp_blend_time = 1
        Assert.assertEqual(1, ADDSWind.interp_blend_time)

        wind.wind_model_type = AgEAvtrWindModelType.eDisabled

        def action9():
            ADDSWind.interp_blend_time = 1

        TryCatchAssertBlock.ExpectedException("must be set", action9)

        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eScenarioModel
        wind.copy()
        wind.wind_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.paste()

    # endregion

    # region Atmosphere
    @category("Weather Tests")
    def test_Atmosphere(self):
        atmos: "IAtmosphereModel" = EarlyBoundTests.AG_Mission.atmosphere_model

        def action10():
            atmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eProcedureModel

        TryCatchAssertBlock.ExpectedException("procedure model", action10)

        atmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        basicAtmos: "IAtmosphereModelBasic" = atmos.mode_as_basic
        basicAtmos.basic_model_type = AgEAvtrAtmosphereModel.eStandard1976

        basicAtmos.use_non_standard_atmosphere = True
        basicAtmos.temperature = 300
        Assert.assertEqual(300, basicAtmos.temperature)

        atmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eScenarioModel
        atmos.copy()
        atmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        atmos.paste()

        Assert.assertEqual(288.15, basicAtmos.temperature)

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        procAtmos: "IAtmosphereModel" = proc1.atmosphere_model
        procAtmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        procAtmosBasic: "IAtmosphereModelBasic" = procAtmos.mode_as_basic

        def action11():
            procAtmosBasic.use_non_standard_atmosphere = True

        TryCatchAssertBlock.ExpectedException("cannot be edited from the procedure", action11)

        procAtmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eProcedureModel
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
        atmos: "IAtmosphereModel" = EarlyBoundTests.AG_Mission.atmosphere_model
        atmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        basicAtmos: "IAtmosphereModelBasic" = atmos.mode_as_basic
        basicAtmos.basic_model_type = AgEAvtrAtmosphereModel.eStandard1976

        Assert.assertEqual(288.15, basicAtmos.temperature)

        def action12():
            basicAtmos.temperature = 290

        TryCatchAssertBlock.ExpectedException("must be ", action12)
        basicAtmos.use_non_standard_atmosphere = True
        basicAtmos.temperature = 290
        Assert.assertEqual(290, basicAtmos.temperature)

        atmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eScenarioModel
        atmos.copy()
        atmos.atmosphere_model_source = AgEAvtrWindAtmosModelSource.eMissionModel
        atmos.paste()

    # endregion

    # region PhaseCollection
    @category("Mission Tests")
    def test_PhaseCollection(self):
        Assert.assertEqual(1, EarlyBoundTests.AG_Phases.count)
        Assert.assertEqual("Phase 1", EarlyBoundTests.AG_Phases[0].name)

        def action13():
            testVal: "IPhase" = EarlyBoundTests.AG_Phases[-1]

        TryCatchAssertBlock.ExpectedException("Invalid index", action13)

        def action14():
            testVal: "IPhase" = EarlyBoundTests.AG_Phases[EarlyBoundTests.AG_Phases.count]

        TryCatchAssertBlock.ExpectedException("Invalid index", action14)

        phase2: "IPhase" = EarlyBoundTests.AG_Phases.add()
        Assert.assertEqual(2, EarlyBoundTests.AG_Phases.count)
        Assert.assertEqual("Phase 2", phase2.name)

        phase0: "IPhase" = EarlyBoundTests.AG_Phases.add_at_index(0)
        phase0.name = "Phase 0"
        Assert.assertEqual("Phase 0", EarlyBoundTests.AG_Phases[0].name)

        def action15():
            EarlyBoundTests.AG_Phases.add_at_index(-1)

        TryCatchAssertBlock.ExpectedException("Invalid index", action15)

        def action16():
            EarlyBoundTests.AG_Phases.add_at_index((EarlyBoundTests.AG_Phases.count + 1))

        TryCatchAssertBlock.ExpectedException("Invalid index", action16)

        countMinusOne: float = EarlyBoundTests.AG_Phases.count - 1
        EarlyBoundTests.AG_Phases.remove(phase0)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Phases.count)
        Assert.assertEqual("Phase 1", EarlyBoundTests.AG_Phases[0].name)

        def action17():
            EarlyBoundTests.AG_Phases.remove(phase0)

        TryCatchAssertBlock.DoAssert2(action17)

        def action18():
            EarlyBoundTests.AG_Phases.remove_at_index(-1)

        TryCatchAssertBlock.ExpectedException("Invalid index", action18)

        def action19():
            EarlyBoundTests.AG_Phases.remove_at_index(EarlyBoundTests.AG_Phases.count)

        TryCatchAssertBlock.ExpectedException("Invalid index", action19)

        EarlyBoundTests.AG_Phases.remove_at_index(1)

        def action20():
            EarlyBoundTests.AG_Phases.remove_at_index(0)

        TryCatchAssertBlock.ExpectedException("must be at least one phase", action20)

        def action21():
            EarlyBoundTests.AG_Phases.remove(phase0)

        TryCatchAssertBlock.DoAssert2(action21)

        Assert.assertEqual(1, EarlyBoundTests.AG_Phases.count)

    # endregion

    # region Phase
    @category("Mission Tests")
    def test_Phase(self):
        currentPhase: "IPhase" = EarlyBoundTests.AG_Phases[0]

        currentPhase.name = "My First Phase"
        Assert.assertEqual("My First Phase", EarlyBoundTests.AG_Phases[0].name)
        currentPhase.name = "Phase 1"

        def action22():
            testPerfModel: "IPerformanceModelOptions" = currentPhase.get_performance_model_by_type("Test")

        TryCatchAssertBlock.ExpectedException("does not contain", action22)

        acc: "IPerformanceModelOptions" = currentPhase.get_performance_model_by_type("Acceleration")

        Assert.assertEqual("Built-In Model", acc.name)

        def action23():
            acc.rename("Test")

        TryCatchAssertBlock.ExpectedException("cannot be renamed", action23)

        def action24():
            acc.delete()

        TryCatchAssertBlock.ExpectedException("cannot be deleted", action24)
        Assert.assertTrue(acc.is_linked_to_catalog)

        acc.link_to_catalog("Built-In Model")
        Assert.assertEqual("Built-In Model", acc.name)
        Assert.assertTrue(acc.is_linked_to_catalog)
        basicAcc: "IAircraftBasicAccelerationModel" = clr.CastAs(acc.properties, IAircraftBasicAccelerationModel)

        acc.copy_from_catalog("Built-In Model")
        Assert.assertEqual("Built-In Model", acc.name)
        Assert.assertEqual(False, acc.is_linked_to_catalog)

        acc.create_new("Advanced Acceleration Model")
        name: str = acc.name
        Assert.assertTrue(("Advanced Acceleration Model" in name))
        Assert.assertEqual(False, acc.is_linked_to_catalog)
        advAcc: "IAircraftAdvAccelerationModel" = clr.CastAs(acc.properties, IAircraftAdvAccelerationModel)

        acc.rename("Test Rename")
        Assert.assertEqual("Test Rename", acc.name)

        vtol: "IPerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")

        vtol.delete()

        def action25():
            vtol.rename("Test")

        TryCatchAssertBlock.ExpectedException("no performance model", action25)

        def action26():
            vtol.delete()

        TryCatchAssertBlock.ExpectedException("no performance model", action26)

        def action27():
            perfModel: "IPerformanceModel" = vtol.properties

        TryCatchAssertBlock.ExpectedException("no performance model", action27)

        def action28():
            isLinked: bool = vtol.is_linked_to_catalog

        TryCatchAssertBlock.ExpectedException("no performance model", action28)

        vtol.link_to_catalog("AGI VTOL Model")
        Assert.assertTrue(vtol.is_linked_to_catalog)
        unknownModel: "IPerformanceModel" = vtol.properties

        currentPhase.set_default_perf_models()
        Assert.assertEqual("Built-In Model", acc.name)

        def action29():
            currentPhase.paste_performance_models()

        TryCatchAssertBlock.ExpectedException("No copy", action29)

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        phase2: "IPhase" = EarlyBoundTests.AG_Phases.add()
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )

        acc.create_new("Advanced Acceleration Model")
        acc.rename("Testing Copy Paste")
        Assert.assertEqual("Testing Copy Paste", acc.name)
        currentPhase.copy_performance_models()
        phase2.paste_performance_models()
        acc2: "IPerformanceModelOptions" = phase2.get_performance_model_by_type("Acceleration")
        Assert.assertEqual("Testing Copy Paste", acc2.name)

        EarlyBoundTests.AG_Phases.remove(phase2)
        currentPhase.procedures.remove(proc2)
        currentPhase.procedures.remove(proc1)

        missileTest: "IMissileModel" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models.add_missile(
            "Missile Perf Model Test"
        )
        EarlyBoundTests.AG_Mission.vehicle = clr.CastAs(missileTest, IAviatorVehicle)
        acc = currentPhase.get_performance_model_by_type("Acceleration")

        def action30():
            perfModel: "IPerformanceModel" = acc.properties

        TryCatchAssertBlock.ExpectedException("", action30)

        rotorcraftTest: "IRotorcraftModel" = (
            EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models.add_rotorcraft(
                "Rotorcraft Perf Model Test"
            )
        )
        EarlyBoundTests.AG_Mission.vehicle = clr.CastAs(rotorcraftTest, IAviatorVehicle)
        acc = currentPhase.get_performance_model_by_type("Acceleration")

        def action31():
            perfModel: "IPerformanceModel" = acc.properties

        TryCatchAssertBlock.ExpectedException("", action31)

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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        proc1.name = "Procedure 1"
        Assert.assertEqual(1, EarlyBoundTests.AG_Procedures.count)

        proc3: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )
        proc3.name = "Procedure 3"

        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add_at_index(
            1, AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )
        proc2.name = "Procedure 2"

        Assert.assertEqual("Procedure 2", EarlyBoundTests.AG_Procedures[1].name)

        def action32():
            testVal: "IProcedure" = EarlyBoundTests.AG_Procedures[-1]

        TryCatchAssertBlock.ExpectedException("Invalid index", action32)

        def action33():
            testVal: "IProcedure" = EarlyBoundTests.AG_Procedures[EarlyBoundTests.AG_Procedures.count]

        TryCatchAssertBlock.ExpectedException("Invalid index", action33)

        def action34():
            EarlyBoundTests.AG_Procedures.add_at_index(
                -1, AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
            )

        TryCatchAssertBlock.ExpectedException("Invalid index", action34)

        def action35():
            EarlyBoundTests.AG_Procedures.add_at_index(
                (EarlyBoundTests.AG_Procedures.count + 1),
                AgEAvtrSiteType.eSiteEndOfPrevProcedure,
                AgEAvtrProcedureType.eProcEnroute,
            )

        TryCatchAssertBlock.ExpectedException("Invalid index", action35)

        def action36():
            EarlyBoundTests.AG_Procedures.remove_at_index(-1)

        TryCatchAssertBlock.ExpectedException("Invalid index", action36)

        def action37():
            EarlyBoundTests.AG_Procedures.remove_at_index(EarlyBoundTests.AG_Procedures.count)

        TryCatchAssertBlock.ExpectedException("Invalid index", action37)

        countMinusOne: float = EarlyBoundTests.AG_Procedures.count - 1
        EarlyBoundTests.AG_Procedures.remove_at_index(1)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Procedures.count)
        Assert.assertEqual("Procedure 3", EarlyBoundTests.AG_Procedures[1].name)

        countMinusOne = EarlyBoundTests.AG_Procedures.count - 1
        EarlyBoundTests.AG_Procedures.remove(proc3)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Procedures.count)

        def action38():
            EarlyBoundTests.AG_Procedures.remove(proc3)

        TryCatchAssertBlock.DoAssert2(action38)

        EarlyBoundTests.AG_Procedures.remove_at_index(0)
        self.EmptyProcedures()

    # endregion

    # region ProcedureTimeOptions
    @category("Mission Tests")
    def test_ProcedureTimeOptions(self):
        tolerance: float = 1e-06

        self.EmptyProcedures()

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )
        proc3: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicPointToPoint
        )
        proc4: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcLanding
        )

        # //////// TESTING TAKEOFF TIME OPTIONS /////////////
        timeOpts: "IProcedureTimeOptions" = proc1.time_options
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

        def action39():
            timeOpts.use_stop_time = True

        TryCatchAssertBlock.ExpectedException("not enabled", action39)

        def action40():
            timeOpts.set_stop_time(timeOpts.stop_time)

        TryCatchAssertBlock.ExpectedException("not enabled", action40)

        # //////// TESTING ENROUTE TIME OPTIONS /////////////

        timeOpts2: "IProcedureTimeOptions" = proc2.time_options
        Assert.assertEqual(False, timeOpts2.start_time_enabled)
        Assert.assertTrue(timeOpts2.interrupt_time_enabled)
        Assert.assertTrue(timeOpts2.stop_time_enabled)

        Assert.assertEqual(False, timeOpts2.use_start_time)

        def action41():
            timeOpts2.use_start_time = True

        TryCatchAssertBlock.ExpectedException("not enabled", action41)

        def action42():
            timeOpts2.set_start_time(timeOpts2.start_time)

        TryCatchAssertBlock.ExpectedException("not enabled", action42)

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

        timeOpts3: "IProcedureTimeOptions" = proc3.time_options
        Assert.assertEqual(False, timeOpts3.start_time_enabled)
        Assert.assertTrue(timeOpts3.interrupt_time_enabled)
        Assert.assertTrue(timeOpts3.stop_time_enabled)

        # //////// TESTING LANDING TIME OPTIONS /////////////

        timeOpts4: "IProcedureTimeOptions" = proc4.time_options
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )

        calcOpts: "ICalculationOptions" = proc1.calculation_options

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

        calcOpts.integrator_type = AgEAvtrNumericalIntegrator.eRK4
        Assert.assertEqual(AgEAvtrNumericalIntegrator.eRK4, calcOpts.integrator_type)
        Assert.assertEqual("RK4", calcOpts.integrator_type_string)

        calcOpts.integrator_type_string = "RK45"
        Assert.assertEqual(AgEAvtrNumericalIntegrator.eRK45, calcOpts.integrator_type)
        Assert.assertEqual("RK45", calcOpts.integrator_type_string)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc1, IProcedure))

    # endregion

    # region RefuelDump
    @category("Mission Tests")
    def test_RefuelDump(self):
        self.EmptyProcedures()

        # Procedure where Refuel/Dump is not supported

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        Assert.assertFalse(proc1.refuel_dump_is_supported)
        rdp: "IRefuelDumpProperties" = proc1.refuel_dump_properties

        def action43():
            rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eRefuelDumpDisabled, 0.0)

        TryCatchAssertBlock.ExpectedException("is not supported", action43)

        def action44():
            o: typing.Any = rdp.refuel_dump_mode

        TryCatchAssertBlock.ExpectedException("is not supported", action44)

        def action45():
            o: typing.Any = rdp.refuel_dump_mode_value

        TryCatchAssertBlock.ExpectedException("is not supported", action45)

        def action46():
            o: typing.Any = rdp.refuel_dump_rate

        TryCatchAssertBlock.ExpectedException("is not supported", action46)

        def action47():
            o: typing.Any = rdp.refuel_dump_time_offset

        TryCatchAssertBlock.ExpectedException("is not supported", action47)

        def action48():
            o: typing.Any = rdp.can_use_end_of_enroute_segment_as_epoch

        TryCatchAssertBlock.ExpectedException("is not supported", action48)

        def action49():
            o: typing.Any = rdp.use_end_of_enroute_segment_as_epoch

        TryCatchAssertBlock.ExpectedException("is not supported", action49)

        # Procedure where Refuel/Dump is supported

        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcArcEnroute
        )
        Assert.assertTrue(proc2.refuel_dump_is_supported)
        rdp = proc2.refuel_dump_properties

        rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eRefuelDumpDisabled, 1.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelDumpDisabled, rdp.refuel_dump_mode)
        Assert.assertEqual(1.0, rdp.refuel_dump_mode_value)  # "not applicable" in GUI

        rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eRefuelTopOff, 2.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelTopOff, rdp.refuel_dump_mode)
        Assert.assertEqual(2.0, rdp.refuel_dump_mode_value)  # "not applicable" in GUI

        rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eRefuelToFuelState, 3.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelToFuelState, rdp.refuel_dump_mode)
        Assert.assertEqual(3.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eRefuelToWeight, 4.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelToWeight, rdp.refuel_dump_mode)
        Assert.assertEqual(4.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eRefuelQuantity, 5.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelQuantity, rdp.refuel_dump_mode)
        Assert.assertEqual(5.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eDumpToFuelState, 6.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eDumpToFuelState, rdp.refuel_dump_mode)
        Assert.assertEqual(6.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eDumpToWeight, 7.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eDumpToWeight, rdp.refuel_dump_mode)
        Assert.assertEqual(7.0, rdp.refuel_dump_mode_value)

        rdp.set_refuel_dump_mode(AgEAvtrRefuelDumpMode.eDumpQuantity, 8.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eDumpQuantity, rdp.refuel_dump_mode)
        Assert.assertEqual(8.0, rdp.refuel_dump_mode_value)

        rdp.refuel_dump_rate = 10
        Assert.assertEqual(10, rdp.refuel_dump_rate)
        rdp.refuel_dump_rate = -11
        Assert.assertEqual(11, rdp.refuel_dump_rate)  # When set to negative number, sets to absolute val. Same as GUI.

        rdp.refuel_dump_time_offset = 20
        Assert.assertEqual(20, rdp.refuel_dump_time_offset)

        def action50():
            rdp.refuel_dump_time_offset = -22

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action50)

        Assert.assertFalse(rdp.can_use_end_of_enroute_segment_as_epoch)

        rdp.use_end_of_enroute_segment_as_epoch = False
        Assert.assertFalse(rdp.use_end_of_enroute_segment_as_epoch)
        rdp.use_end_of_enroute_segment_as_epoch = True
        Assert.assertTrue(rdp.use_end_of_enroute_segment_as_epoch)

        # Procedure where CanUseEndOfEnrouteSegmentAsEpoch

        proc3: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcHoldingCircular
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

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        arcProc: "IProcedureArcEnroute" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcArcEnroute
            ),
            IProcedureArcEnroute,
        )

        alt: "IArcAltitudeAndDelayOptions" = arcProc.altitude_options
        self.ArcAltitudeAndDelayOptions(alt)

        arc: "IArcOptions" = arcProc.arc_options
        self.ArcOptions(arc)

        arcAirspeed: "ICruiseAirspeedOptions" = arcProc.arc_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(arcAirspeed)

        enroute: "IEnrouteAndDelayOptions" = arcProc.enroute_options
        self.EnrouteAndDelayOptions(enroute)

        airspeed: "ICruiseAirspeedOptions" = arcProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        turnOpts: "IEnrouteTurnDirectionOptions" = arcProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(arcProc, IProcedure))

    # endregion

    # region ArcPointToPoint
    @category("Procedure Tests")
    def test_ArcPointToPoint(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        arcProc: "IProcedureArcPointToPoint" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcArcPointToPoint
            ),
            IProcedureArcPointToPoint,
        )

        alt: "IArcAltitudeOptions" = arcProc.altitude_options
        self.ArcAltitudeOptions(alt)

        arc: "IArcOptions" = arcProc.arc_options
        self.ArcOptions(arc)

        arcAirspeed: "ICruiseAirspeedOptions" = arcProc.arc_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(arcAirspeed)

        enroute: "IEnrouteOptions" = arcProc.enroute_options
        self.EnrouteOptions(enroute)

        airspeed: "ICruiseAirspeedOptions" = arcProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        turnOpts: "IEnrouteTurnDirectionOptions" = arcProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        arcProc.fly_cruise_airspeed_profile = False
        Assert.assertEqual(False, arcProc.fly_cruise_airspeed_profile)

        vertOpts: "IArcVerticalPlaneOptions" = arcProc.vertical_plane_options
        self.ArcVerticalPlane(vertOpts)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(arcProc, IProcedure))

    # endregion

    # region AreaTargetSearch
    @category("Procedure Tests")
    def test_AreaTargetSearch(self):
        self.EmptyProcedures()

        areaTargetObj: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(
            AgESTKObjectType.eAreaTarget, "AreaTarget"
        )
        areaTargetProc: "IProcedureAreaTargetSearch" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteSTKAreaTarget, AgEAvtrProcedureType.eProcAreaTargetSearch
            ),
            IProcedureAreaTargetSearch,
        )

        self.TestProcedureName(areaTargetProc.get_as_procedure(), "AreaTargetSearch")
        self.AltitudeOptions(areaTargetProc.altitude_options)
        self.EnrouteOptions(areaTargetProc.enroute_options)
        self.EnrouteCruiseAirspeed(areaTargetProc.enroute_cruise_airspeed_options)

        areaTargetProc.procedure_type = AgEAvtrFlightLineProcType.eProcTypeBasicPointToPoint
        Assert.assertEqual(AgEAvtrFlightLineProcType.eProcTypeBasicPointToPoint, areaTargetProc.procedure_type)
        areaTargetProc.max_separation = 0.2
        Assert.assertEqual(0.2, areaTargetProc.max_separation)
        areaTargetProc.course_mode = AgEAvtrSearchPatternCourseMode.eCourseModeLow
        Assert.assertEqual(AgEAvtrSearchPatternCourseMode.eCourseModeLow, areaTargetProc.course_mode)
        areaTargetProc.first_leg_retrograde = True
        Assert.assertTrue(areaTargetProc.first_leg_retrograde)

        def action51():
            areaTargetProc.centroid_true_course = 5

        TryCatchAssertBlock.ExpectedException("must be", action51)
        areaTargetProc.course_mode = AgEAvtrSearchPatternCourseMode.eCourseModeOverride
        areaTargetProc.centroid_true_course = 5
        course: typing.Any = areaTargetProc.centroid_true_course
        Assert.assertEqual(5, float(course))

        areaTargetProc.fly_cruise_airspeed_profile = False
        Assert.assertEqual(False, areaTargetProc.fly_cruise_airspeed_profile)
        areaTargetProc.procedure_type = AgEAvtrFlightLineProcType.eProcTypeEnroute

        def action52():
            areaTargetProc.fly_cruise_airspeed_profile = False

        TryCatchAssertBlock.ExpectedException("must be", action52)

        areaTargetProc.procedure_type = AgEAvtrFlightLineProcType.eProcTypeBasicPointToPoint

        def action53():
            areaTargetProc.must_level_off = True

        TryCatchAssertBlock.ExpectedException("must be", action53)

        def action54():
            areaTargetProc.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffAutomaticManeuver

        TryCatchAssertBlock.ExpectedException("must be", action54)
        areaTargetProc.procedure_type = AgEAvtrFlightLineProcType.eProcTypeEnroute
        areaTargetProc.must_level_off = True
        Assert.assertTrue(areaTargetProc.must_level_off)
        areaTargetProc.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(
            AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, areaTargetProc.level_off_mode
        )

        takeoffProc: "IProcedure" = EarlyBoundTests.AG_Procedures.add_at_index(
            0, AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        areaTargetProc.course_mode = AgEAvtrSearchPatternCourseMode.eCourseModeHigh
        EarlyBoundTests.AG_AvtrProp.propagate()

        def action55():
            areaTargetProc.first_leg_retrograde = True

        TryCatchAssertBlock.ExpectedException("must be", action55)

        areaTargetObj.unload()
        EarlyBoundTests.AG_Procedures.remove(takeoffProc)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(areaTargetProc, IProcedure))

    # endregion

    # region BasicPointToPoint
    @category("Procedure Tests")
    def test_BasicPointToPoint(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        p2p: "IProcedureBasicPointToPoint" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicPointToPoint
            ),
            IProcedureBasicPointToPoint,
        )

        alt: "IAltitudeOptions" = p2p.altitude_options
        self.AltitudeOptions(alt)

        nav: "INavigationOptions" = p2p.navigation_options
        self.NavigationOptions(nav)

        enroute: "IEnrouteOptions" = p2p.enroute_options
        self.EnrouteOptions(enroute)

        airspeed: "ICruiseAirspeedAndProfileOptions" = p2p.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeedAndProfile(airspeed)

        vert: "IVerticalPlaneAndFlightPathOptions" = p2p.vertical_plane_options
        self.VerticalPlaneAndFlightPathOptions(vert)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(p2p, IProcedure))

    # endregion

    # region Delay
    @category("Procedure Tests")
    def test_Delay(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        delay: "IProcedureDelay" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcDelay),
            IProcedureDelay,
        )

        delay.altitude_mode = AgEAvtrDelayAltMode.eDelayDefaultCruiseAlt

        def action56():
            delay.altitude = 5000

        TryCatchAssertBlock.ExpectedException("must be", action56)

        delay.altitude_mode = AgEAvtrDelayAltMode.eDelayOverride
        delay.altitude = 5000
        Assert.assertEqual(5000, delay.altitude)

        airspeedOpts: "ICruiseAirspeedOptions" = delay.cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeedOpts)

        delay.turn_direction = AgEAvtrNavigatorTurnDir.eNavigatorTurnRight
        Assert.assertEqual(AgEAvtrNavigatorTurnDir.eNavigatorTurnRight, delay.turn_direction)
        delay.turn_radius_factor = 3
        Assert.assertEqual(3, delay.turn_radius_factor)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(delay, IProcedure))

    # endregion

    # region Enroute
    @category("Procedure Tests")
    def test_Enroute(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        enroute: "IProcedureEnroute" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
            ),
            IProcedureEnroute,
        )

        alt: "IAltitudeMSLAndLevelOffOptions" = enroute.altitude_msl_options
        self.AltitudeMSLAndLevelOffOptions(alt)

        nav: "INavigationOptions" = enroute.navigation_options
        self.NavigationOptions(nav)

        enrouteOpts: "IEnrouteAndDelayOptions" = enroute.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        airspeed: "ICruiseAirspeedOptions" = enroute.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(enroute, IProcedure))

    # endregion

    # region ExternalEphemeris
    @category("Procedure Tests")
    def test_ExternalEphemeris(self):
        self.EmptyProcedures()

        extEphem: "IProcedureExtEphem" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteReferenceState, AgEAvtrProcedureType.eProcExtEphem),
            IProcedureExtEphem,
        )

        proc: "IProcedure" = extEphem.get_as_procedure()
        Assert.assertEqual("ExtEphem", proc.name)

        def action57():
            d: float = extEphem.ephemeris_file_duration

        TryCatchAssertBlock.ExpectedException("No ephemeris file set", action57)

        extEphem.ephemeris_file = TestBase.GetScenarioFile("ExternalTestBFW.e")
        Assert.assertTrue(("ExternalTestBFW.e" in extEphem.ephemeris_file))
        Assert.assertAlmostEqual(799.26, extEphem.ephemeris_file_duration, delta=0.01)

        def action58():
            extEphem.ephemeris_file = TestBase.GetScenarioFile("bogus.e")

        TryCatchAssertBlock.ExpectedException("Invalid", action58)

        def action59():
            extEphem.ephemeris_file = TestBase.GetScenarioFile("Aircraft1.ac")

        TryCatchAssertBlock.ExpectedException("Invalid", action59)

        extEphem.flight_mode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightClimb
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightClimb, extEphem.flight_mode)
        extEphem.flight_mode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightCruise
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightCruise, extEphem.flight_mode)
        extEphem.flight_mode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightDescend
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightDescend, extEphem.flight_mode)
        extEphem.flight_mode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeLanding
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeLanding, extEphem.flight_mode)
        extEphem.flight_mode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeLandingWOW
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeLandingWOW, extEphem.flight_mode)
        extEphem.flight_mode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeTakeoff
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeTakeoff, extEphem.flight_mode)
        extEphem.flight_mode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeTakeoffWOW
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeTakeoffWOW, extEphem.flight_mode)
        extEphem.flight_mode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeVTOLHover
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeVTOLHover, extEphem.flight_mode)

        extEphem.use_start_duration = False
        Assert.assertFalse(extEphem.use_start_duration)

        def action60():
            extEphem.start_time = 100

        TryCatchAssertBlock.ExpectedException("not writeable", action60)

        def action61():
            extEphem.duration = 200

        TryCatchAssertBlock.ExpectedException("not writeable", action61)

        extEphem.use_start_duration = True
        Assert.assertTrue(extEphem.use_start_duration)

        extEphem.start_time = 100
        Assert.assertAlmostEqual(100, extEphem.start_time, delta=extEphem.start_time)

        def action62():
            extEphem.start_time = -100

        TryCatchAssertBlock.ExpectedException("must be non-negative", action62)

        extEphem.duration = 200
        Assert.assertAlmostEqual(200, extEphem.duration, delta=extEphem.duration)

        def action63():
            extEphem.duration = -200

        TryCatchAssertBlock.ExpectedException("must be non-negative", action63)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(extEphem, IProcedure))

    # endregion

    # region FlightLine
    @category("Procedure Tests")
    def test_FlightLine(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        flightLine: "IProcedureFlightLine" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcFlightLine
            ),
            IProcedureFlightLine,
        )

        alt: "IAltitudeOptions" = flightLine.altitude_options
        self.AltitudeOptions(alt)

        flightAirspeed: "ICruiseAirspeedOptions" = flightLine.flight_line_airspeed_options
        self.EnrouteCruiseAirspeed(flightAirspeed)

        enroute: "IEnrouteOptions" = flightLine.enroute_options
        self.EnrouteOptions(enroute)

        turnOpts: "IEnrouteTurnDirectionOptions" = flightLine.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "ICruiseAirspeedOptions" = flightLine.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        flightLine.procedure_type = AgEAvtrFlightLineProcType.eProcTypeTerrainFollow
        flightLine.outbound_course = 5
        course: typing.Any = flightLine.outbound_course
        Assert.assertEqual(5, float(course))
        flightLine.use_magnetic_heading = True
        Assert.assertTrue(flightLine.use_magnetic_heading)
        flightLine.leg_length = 11
        Assert.assertEqual(11, flightLine.leg_length)

        flightLine.procedure_type = AgEAvtrFlightLineProcType.eProcTypeTerrainFollow

        def action64():
            flightLine.fly_cruise_airspeed_profile = False

        TryCatchAssertBlock.ExpectedException("must be", action64)

        def action65():
            flightLine.must_level_off = False

        TryCatchAssertBlock.ExpectedException("must be", action65)

        def action66():
            flightLine.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffAutomaticManeuver

        TryCatchAssertBlock.ExpectedException("must be", action66)

        flightLine.procedure_type = AgEAvtrFlightLineProcType.eProcTypeBasicPointToPoint
        flightLine.fly_cruise_airspeed_profile = False
        Assert.assertEqual(False, flightLine.fly_cruise_airspeed_profile)

        flightLine.procedure_type = AgEAvtrFlightLineProcType.eProcTypeEnroute
        flightLine.must_level_off = True
        Assert.assertTrue(flightLine.must_level_off)
        flightLine.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, flightLine.level_off_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(flightLine, IProcedure))

    # endregion

    # region FormationFlyer
    @category("Procedure Tests")
    def test_FormationFlyer(self):
        TestBase.LoadTestScenario(TestBase.PathCombine("AviatorTests", "Formation_Flyer", "Scenario1.sc"))
        EarlyBoundTests.AG_Scenario = TestBase.Application.current_scenario
        EarlyBoundTests.AG_AC = clr.Convert(
            (EarlyBoundTests.AG_Scenario.children.get_item_by_name("Wingman")), IAircraft
        )
        aircraftRoute: "IVehiclePropagatorAviator" = clr.CastAs(EarlyBoundTests.AG_AC.route, IVehiclePropagatorAviator)
        EarlyBoundTests.AG_AvtrProp = clr.CastAs(aircraftRoute.avtr_propagator, IAviatorPropagator)
        EarlyBoundTests.AG_Mission = EarlyBoundTests.AG_AvtrProp.avtr_mission
        EarlyBoundTests.AG_Phases = EarlyBoundTests.AG_Mission.phases
        EarlyBoundTests.AG_Procedures = EarlyBoundTests.AG_Phases[0].procedures

        EarlyBoundTests.AG_Procedures.remove_at_index(2)  # Remove existing Formation Flyer procedure.

        formationFlyer: "IProcedureFormationFlyer" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcFormationFlyer
            ),
            IProcedureFormationFlyer,
        )

        formationFlyer.cross_range_close_rate = 10
        Assert.assertEqual(10, formationFlyer.cross_range_close_rate)

        def action67():
            formationFlyer.cross_range_close_rate = -10

        TryCatchAssertBlock.ExpectedException("out of range", action67)  # Can be set. Should be invalid.

        formationFlyer.initial_close_max_speed_advantage = 20
        Assert.assertEqual(20, formationFlyer.initial_close_max_speed_advantage)

        def action68():
            formationFlyer.initial_close_max_speed_advantage = -20

        TryCatchAssertBlock.ExpectedException("out of bounds", action68)  # Can be set. Should be invalid.

        formationFlyer.max_time_step = 2
        Assert.assertEqual(2, formationFlyer.max_time_step)
        formationFlyer.max_time_step = 1
        Assert.assertEqual(1, formationFlyer.max_time_step)

        def action69():
            formationFlyer.max_time_step = 0

        TryCatchAssertBlock.ExpectedException("out of bounds", action69)  # Can be set. Should be invalid.

        formationFlyer.min_time_step = 0.2
        Assert.assertEqual(0.2, formationFlyer.min_time_step)
        formationFlyer.min_time_step = 0.1
        Assert.assertEqual(0.1, formationFlyer.min_time_step)

        def action70():
            formationFlyer.min_time_step = 0

        TryCatchAssertBlock.ExpectedException("out of bounds", action70)

        stopCond: "AgEAvtrFormationFlyerStopCondition"

        for stopCond in Enum.GetValues(clr.TypeOf(AgEAvtrFormationFlyerStopCondition)):
            formationFlyer.stop_condition = stopCond
            Assert.assertEqual(stopCond, formationFlyer.stop_condition)
            if AgEAvtrFormationFlyerStopCondition.eFormationFlyerStopAfterTime == stopCond:
                formationFlyer.stop_time = 30
                Assert.assertEqual(30, formationFlyer.stop_time)

                def action71():
                    formationFlyer.stop_time = -30

                TryCatchAssertBlock.ExpectedException("out of bounds", action71)

                def action72():
                    formationFlyer.stop_down_range = 40

                TryCatchAssertBlock.ExpectedException("Cannot set", action72)

                def action73():
                    formationFlyer.stop_fuel_state = 50

                TryCatchAssertBlock.ExpectedException("Cannot set", action73)

            elif AgEAvtrFormationFlyerStopCondition.eFormationFlyerStopAfterDownRange == stopCond:

                def action74():
                    formationFlyer.stop_time = 30

                TryCatchAssertBlock.ExpectedException("Cannot set", action74)

                formationFlyer.stop_down_range = 40
                Assert.assertEqual(40, formationFlyer.stop_down_range)

                def action75():
                    formationFlyer.stop_down_range = -40

                TryCatchAssertBlock.ExpectedException("out of bounds", action75)

                def action76():
                    formationFlyer.stop_fuel_state = 50

                TryCatchAssertBlock.ExpectedException("Cannot set", action76)

            elif AgEAvtrFormationFlyerStopCondition.eFormationFlyerStopAfterFuelState == stopCond:

                def action77():
                    formationFlyer.stop_time = 30

                TryCatchAssertBlock.ExpectedException("Cannot set", action77)

                def action78():
                    formationFlyer.stop_down_range = 40

                TryCatchAssertBlock.ExpectedException("Cannot set", action78)

                formationFlyer.stop_fuel_state = 50
                Assert.assertEqual(50, formationFlyer.stop_fuel_state)

                def action79():
                    formationFlyer.stop_fuel_state = -50

                TryCatchAssertBlock.ExpectedException("out of bounds", action79)

            else:

                def action80():
                    formationFlyer.stop_time = 30

                TryCatchAssertBlock.ExpectedException("Cannot set", action80)

                def action81():
                    formationFlyer.stop_down_range = 40

                TryCatchAssertBlock.ExpectedException("Cannot set", action81)

                def action82():
                    formationFlyer.stop_fuel_state = 50

                TryCatchAssertBlock.ExpectedException("Cannot set", action82)

        EarlyBoundTests.InitHelper()

    # endregion

    # region FormationRecover
    @category("Procedure Tests")
    def test_FormationRecover(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        EarlyBoundTests.AG_AvtrProp.propagate()

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj: "IStkObject" = acObj.copy_object("AC2")
        ac2: "IAircraft" = clr.CastAs(ac2Obj, IAircraft)
        route2: "IVehiclePropagatorAviator" = clr.CastAs(ac2.route, IVehiclePropagatorAviator)
        prop2: "IAviatorPropagator" = clr.CastAs(route2.avtr_propagator, IAviatorPropagator)
        mission2: "IMission" = prop2.avtr_mission
        phases2: "IPhaseCollection" = mission2.phases
        procedures2: "IProcedureCollection" = phases2[0].procedures

        proc2: "IProcedure" = procedures2.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingCircular
        )
        prop2.propagate()

        formRecov: "IProcedureFormationRecover" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcFormationRecover
            ),
            IProcedureFormationRecover,
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
        formRecov.interpolate_point_pos_vel = True
        Assert.assertTrue(formRecov.interpolate_point_pos_vel)

        formRecov.altitude_offset = 5
        Assert.assertEqual(5, formRecov.altitude_offset)
        formRecov.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowTakeoff

        def action83():
            formRecov.override_fuel_flow_value = 123

        TryCatchAssertBlock.ExpectedException("must be", action83)
        formRecov.consider_accel_for_fuel_flow = True
        Assert.assertTrue(formRecov.consider_accel_for_fuel_flow)

        formRecov.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowOverride
        formRecov.override_fuel_flow_value = 123
        Assert.assertAlmostEqual(123, formRecov.override_fuel_flow_value, delta=tolerance)

        def action84():
            formRecov.consider_accel_for_fuel_flow = True

        TryCatchAssertBlock.ExpectedException("must be", action84)

        formRecov.first_pause = 1
        Assert.assertEqual(1, formRecov.first_pause)
        formRecov.transition_time = 2
        Assert.assertEqual(2, formRecov.transition_time)
        formRecov.second_pause = 3
        Assert.assertEqual(3, formRecov.second_pause)
        formRecov.display_step_time = 4
        Assert.assertEqual(4, formRecov.display_step_time)

        formRecov.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff
        Assert.assertEqual(AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff, formRecov.flight_mode)

        formRecov.flight_path_angle = 5
        angle: typing.Any = formRecov.flight_path_angle
        Assert.assertEqual(5, float(angle))
        formRecov.radius_factor = 2
        Assert.assertEqual(2, formRecov.radius_factor)

        formRecov.use_delay = True
        Assert.assertTrue(formRecov.use_delay)
        formRecov.delay_turn_dir = AgEAvtrDelayTurnDir.eDelayTurnLeft
        Assert.assertEqual(AgEAvtrDelayTurnDir.eDelayTurnLeft, formRecov.delay_turn_dir)
        formRecov.use_delay = False

        def action85():
            formRecov.delay_turn_dir = AgEAvtrDelayTurnDir.eDelayTurnLeft

        TryCatchAssertBlock.ExpectedException("must be", action85)

        formRecov.use_delay = False

        def action86():
            airspeed: "ICruiseAirspeedOptions" = formRecov.delay_cruise_airspeed_options

        TryCatchAssertBlock.ExpectedException("must be", action86)
        formRecov.use_delay = True
        self.EnrouteCruiseAirspeed(formRecov.delay_cruise_airspeed_options)

        self.EnrouteOptions(formRecov.enroute_options)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_AvtrProp.propagate()

        def action87():
            formRecov.find_first_valid_start_time(minTime, maxTime, 30)

        TryCatchAssertBlock.ExpectedException("first procedure", action87)

        def action88():
            formRecov.flight_path_angle = 1

        TryCatchAssertBlock.ExpectedException("first procedure", action88)

        def action89():
            formRecov.radius_factor = 1

        TryCatchAssertBlock.ExpectedException("first procedure", action89)

        def action90():
            formRecov.use_delay = True

        TryCatchAssertBlock.ExpectedException("first procedure", action90)

        def action91():
            formRecov.delay_turn_dir = AgEAvtrDelayTurnDir.eDelayTurnAuto

        TryCatchAssertBlock.ExpectedException("first procedure", action91)

        def action92():
            enrouteOpts: "IEnrouteOptions" = formRecov.enroute_options

        TryCatchAssertBlock.ExpectedException("first procedure", action92)

        def action93():
            airspeed: "ICruiseAirspeedOptions" = formRecov.delay_cruise_airspeed_options

        TryCatchAssertBlock.ExpectedException("first procedure", action93)

        formRecov.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL
        Assert.assertEqual(formRecov.flight_mode, AgEAvtrPhaseOfFlight.eFlightPhaseVTOL)
        formRecov.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(formRecov.fuel_flow_type, AgEAvtrFuelFlowType.eFuelFlowVTOL)
        currentPhase: "IPhase" = EarlyBoundTests.AG_Phases[0]
        vtol: "IPerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()

        def action94():
            formRecov.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action94)

        def action95():
            formRecov.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action95)

        currentPhase.set_default_perf_models()
        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(formRecov, IProcedure))
        ac2Obj.unload()

    # endregion

    # region HoldingCircular
    @category("Procedure Tests")
    def test_HoldingCircular(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        holdingProc: "IProcedureHoldingCircular" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingCircular
            ),
            IProcedureHoldingCircular,
        )

        alt: "IAltitudeMSLOptions" = holdingProc.altitude_options
        self.AltitudeMSLOptions(alt)

        holdAirspeed: "ICruiseAirspeedOptions" = holdingProc.hold_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts: "IEnrouteAndDelayOptions" = holdingProc.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts: "IEnrouteTurnDirectionOptions" = holdingProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "ICruiseAirspeedOptions" = holdingProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.profile_mode = AgEAvtrHoldingProfileMode.eSTK8Compatible
        Assert.assertEqual(AgEAvtrHoldingProfileMode.eSTK8Compatible, holdingProc.profile_mode)

        holdingProc.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, holdingProc.level_off_mode)

        holdingProc.bearing = 5
        angle: typing.Any = holdingProc.bearing
        Assert.assertEqual(5, float(angle))
        holdingProc.use_magnetic_heading = False
        Assert.assertEqual(False, holdingProc.use_magnetic_heading)

        holdingProc.range = 11
        Assert.assertEqual(11, holdingProc.range)
        holdingProc.diameter = 15
        Assert.assertEqual(15, holdingProc.diameter)

        def action96():
            holdingProc.diameter = 0.01

        TryCatchAssertBlock.ExpectedException("minimum diameter", action96)

        holdingProc.use_alternate_entry_points = True
        Assert.assertTrue(holdingProc.use_alternate_entry_points)
        holdingProc.turn_direction = AgEAvtrHoldingDirection.eOutboundRightTurn
        Assert.assertEqual(AgEAvtrHoldingDirection.eOutboundRightTurn, holdingProc.turn_direction)
        holdingProc.turns = 3
        Assert.assertEqual(3, holdingProc.turns)
        holdingProc.refuel_dump_mode = AgEAvtrHoldRefuelDumpMode.eImmediateExit
        Assert.assertEqual(AgEAvtrHoldRefuelDumpMode.eImmediateExit, holdingProc.refuel_dump_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region HoldingFigure8
    @category("Procedure Tests")
    def test_HoldingFigure8(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        holdingProc: "IProcedureHoldingFigure8" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingFigure8
            ),
            IProcedureHoldingFigure8,
        )

        Assert.assertTrue((clr.Is(holdingProc, IProcedure)))

        alt: "IAltitudeMSLOptions" = holdingProc.altitude_options
        self.AltitudeMSLOptions(alt)

        holdAirspeed: "ICruiseAirspeedOptions" = holdingProc.hold_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts: "IEnrouteAndDelayOptions" = holdingProc.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts: "IEnrouteTurnDirectionOptions" = holdingProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "ICruiseAirspeedOptions" = holdingProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.profile_mode = AgEAvtrHoldingProfileMode.eSTK8Compatible
        Assert.assertEqual(AgEAvtrHoldingProfileMode.eSTK8Compatible, holdingProc.profile_mode)

        holdingProc.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, holdingProc.level_off_mode)

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

        def action97():
            holdingProc.width = 0.01

        TryCatchAssertBlock.ExpectedException("minimum diameter", action97)

        def action98():
            holdingProc.length = 0.01

        TryCatchAssertBlock.ExpectedException("minimum diameter", action98)

        def action99():
            holdingProc.length = 13

        TryCatchAssertBlock.ExpectedException("must be", action99)

        holdingProc.use_alternate_entry_points = True
        Assert.assertTrue(holdingProc.use_alternate_entry_points)
        holdingProc.turns = 3
        Assert.assertEqual(3, holdingProc.turns)
        holdingProc.refuel_dump_mode = AgEAvtrHoldRefuelDumpMode.eImmediateExit
        Assert.assertEqual(AgEAvtrHoldRefuelDumpMode.eImmediateExit, holdingProc.refuel_dump_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region HoldingRacetrack
    @category("Procedure Tests")
    def test_HoldingRacetrack(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        holdingProc: "IProcedureHoldingRacetrack" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingRacetrack
            ),
            IProcedureHoldingRacetrack,
        )

        alt: "IAltitudeMSLOptions" = holdingProc.altitude_options
        self.AltitudeMSLOptions(alt)

        holdAirspeed: "ICruiseAirspeedOptions" = holdingProc.hold_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts: "IEnrouteAndDelayOptions" = holdingProc.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts: "IEnrouteTurnDirectionOptions" = holdingProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "ICruiseAirspeedOptions" = holdingProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.profile_mode = AgEAvtrHoldingProfileMode.eSTK8Compatible
        Assert.assertEqual(AgEAvtrHoldingProfileMode.eSTK8Compatible, holdingProc.profile_mode)

        holdingProc.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, holdingProc.level_off_mode)

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

        def action100():
            holdingProc.width = 0.01

        TryCatchAssertBlock.ExpectedException("minimum diameter", action100)

        holdingProc.entry_maneuver = AgEAvtrHoldingEntryManeuver.eUseAlternateEntryPoints
        Assert.assertEqual(AgEAvtrHoldingEntryManeuver.eUseAlternateEntryPoints, holdingProc.entry_maneuver)
        holdingProc.turns = 3
        Assert.assertEqual(3, holdingProc.turns)
        holdingProc.refuel_dump_mode = AgEAvtrHoldRefuelDumpMode.eImmediateExit
        Assert.assertEqual(AgEAvtrHoldRefuelDumpMode.eImmediateExit, holdingProc.refuel_dump_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region Hover
    @category("Procedure Tests")
    def test_Hover(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToHover
        )
        hoverProc: "IProcedureHover" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHover),
            IProcedureHover,
        )

        alt: "IHoverAltitudeOptions" = hoverProc.altitude_options
        self.HoverAltitudeOptions(alt)

        hoverProc.hover_mode = AgEAvtrHoverMode.eHoverModeFixedTime
        Assert.assertEqual(AgEAvtrHoverMode.eHoverModeFixedTime, hoverProc.hover_mode)
        hoverProc.fixed_time = "00:00:20.000"
        fixedtime: typing.Any = hoverProc.fixed_time
        Assert.assertTrue(("00:00:20.000" == str(fixedtime)))

        def action101():
            hoverProc.heading_mode = AgEAvtrVTOLHeadingMode.eHeadingAlignTranslationCourse

        TryCatchAssertBlock.ExpectedException("must be", action101)

        def action102():
            hoverProc.set_absolute_course(5, False)

        TryCatchAssertBlock.ExpectedException("must be", action102)

        def action103():
            hoverProc.set_relative_course(4)

        TryCatchAssertBlock.ExpectedException("must be", action103)

        def action104():
            hoverProc.set_final_translation_course()

        TryCatchAssertBlock.ExpectedException("must be", action104)

        def action105():
            hoverProc.final_heading_rate = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action105)

        def action106():
            hoverProc.translation_mode = AgEAvtrVTOLTranslationMode.eComeToStop

        TryCatchAssertBlock.ExpectedException("must be", action106)

        def action107():
            hoverProc.bearing = 6

        TryCatchAssertBlock.ExpectedException("must be", action107)

        def action108():
            hoverProc.use_magnetic_bearing = True

        TryCatchAssertBlock.ExpectedException("must be", action108)

        def action109():
            hoverProc.range = 7

        TryCatchAssertBlock.ExpectedException("must be", action109)

        def action110():
            hoverProc.final_course_mode = AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation

        TryCatchAssertBlock.ExpectedException("must be", action110)

        def action111():
            hoverProc.smooth_translation_mode = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action111)

        def action112():
            hoverProc.radius_factor = 3

        TryCatchAssertBlock.ExpectedException("must be", action112)

        hoverProc.hover_mode = AgEAvtrHoverMode.eHoverModeManeuver

        def action113():
            hoverProc.fixed_time = 15

        TryCatchAssertBlock.ExpectedException("must be", action113)

        hoverProc.heading_mode = AgEAvtrVTOLHeadingMode.eHeadingIntoWind
        Assert.assertEqual(AgEAvtrVTOLHeadingMode.eHeadingIntoWind, hoverProc.heading_mode)

        def action114():
            hoverProc.set_absolute_course(5, False)

        TryCatchAssertBlock.ExpectedException("must be", action114)

        def action115():
            hoverProc.set_relative_course(4)

        TryCatchAssertBlock.ExpectedException("must be", action115)

        def action116():
            hoverProc.set_final_translation_course()

        TryCatchAssertBlock.ExpectedException("must be", action116)

        def action117():
            hoverProc.final_heading_rate = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action117)

        hoverProc.heading_mode = AgEAvtrVTOLHeadingMode.eHeadingIndependent
        Assert.assertEqual(AgEAvtrVTOLHeadingMode.eHeadingIndependent, hoverProc.heading_mode)
        hoverProc.set_absolute_course(5, False)
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingAbsolute, hoverProc.final_heading_mode)
        absCourse: typing.Any = hoverProc.absolute_course
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertEqual(False, hoverProc.use_magnetic_heading)

        hoverProc.set_relative_course(4)
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingRelative, hoverProc.final_heading_mode)
        relCourse: typing.Any = hoverProc.relative_course
        Assert.assertEqual(4, float(relCourse))

        hoverProc.set_final_translation_course()
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingTranslationCourse, hoverProc.final_heading_mode)

        hoverProc.final_heading_rate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, hoverProc.final_heading_rate)

        hoverProc.translation_mode = AgEAvtrVTOLTranslationMode.eComeToStop
        Assert.assertEqual(AgEAvtrVTOLTranslationMode.eComeToStop, hoverProc.translation_mode)

        def action118():
            hoverProc.bearing = 6

        TryCatchAssertBlock.ExpectedException("must be", action118)

        def action119():
            hoverProc.use_magnetic_bearing = True

        TryCatchAssertBlock.ExpectedException("must be", action119)

        def action120():
            hoverProc.range = 7

        TryCatchAssertBlock.ExpectedException("must be", action120)

        def action121():
            hoverProc.final_course_mode = AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation

        TryCatchAssertBlock.ExpectedException("must be", action121)

        def action122():
            hoverProc.smooth_translation_mode = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action122)

        def action123():
            hoverProc.radius_factor = 3

        TryCatchAssertBlock.ExpectedException("must be", action123)

        hoverProc.translation_mode = AgEAvtrVTOLTranslationMode.eSetBearingAndRange
        hoverProc.bearing = 6
        bearing: typing.Any = hoverProc.bearing
        Assert.assertEqual(6, float(bearing))

        hoverProc.use_magnetic_bearing = True
        Assert.assertTrue(hoverProc.use_magnetic_bearing)

        hoverProc.range = 7
        Assert.assertEqual(7, hoverProc.range)

        hoverProc.final_course_mode = AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation
        Assert.assertEqual(
            AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation, hoverProc.final_course_mode
        )

        hoverProc.smooth_translation_mode = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, hoverProc.smooth_translation_mode)

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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToHover
        )
        hoverProc: "IProcedureHoverTranslate" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteWaypoint, AgEAvtrProcedureType.eProcHoverTranslate),
            IProcedureHoverTranslate,
        )

        alt: "IHoverAltitudeOptions" = hoverProc.altitude_options
        self.HoverAltitudeOptions(alt)

        hoverProc.heading_mode = AgEAvtrVTOLHeadingMode.eHeadingIntoWind
        Assert.assertEqual(AgEAvtrVTOLHeadingMode.eHeadingIntoWind, hoverProc.heading_mode)

        def action124():
            hoverProc.set_absolute_course(5, False)

        TryCatchAssertBlock.ExpectedException("must be", action124)

        def action125():
            hoverProc.set_relative_course(4)

        TryCatchAssertBlock.ExpectedException("must be", action125)

        def action126():
            hoverProc.set_final_translation_course()

        TryCatchAssertBlock.ExpectedException("must be", action126)

        def action127():
            hoverProc.final_heading_rate = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action127)

        hoverProc.heading_mode = AgEAvtrVTOLHeadingMode.eHeadingIndependent
        Assert.assertEqual(AgEAvtrVTOLHeadingMode.eHeadingIndependent, hoverProc.heading_mode)
        hoverProc.set_absolute_course(5, False)
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingAbsolute, hoverProc.final_heading_mode)
        absCourse: typing.Any = hoverProc.absolute_course
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertEqual(False, hoverProc.use_magnetic_heading)

        hoverProc.set_relative_course(4)
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingRelative, hoverProc.final_heading_mode)
        relCourse: typing.Any = hoverProc.relative_course
        Assert.assertEqual(4, float(relCourse))

        hoverProc.set_final_translation_course()
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingTranslationCourse, hoverProc.final_heading_mode)

        hoverProc.final_heading_rate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, hoverProc.final_heading_rate)

        hoverProc.final_course_mode = AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation
        Assert.assertEqual(
            AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation, hoverProc.final_course_mode
        )

        hoverProc.smooth_translation_mode = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, hoverProc.smooth_translation_mode)

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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        EarlyBoundTests.AG_AvtrProp.propagate()

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj: "IStkObject" = acObj.copy_object("AC2")
        ac2: "IAircraft" = clr.CastAs(ac2Obj, IAircraft)
        route2: "IVehiclePropagatorAviator" = clr.CastAs(ac2.route, IVehiclePropagatorAviator)
        prop2: "IAviatorPropagator" = clr.CastAs(route2.avtr_propagator, IAviatorPropagator)
        mission2: "IMission" = prop2.avtr_mission
        phases2: "IPhaseCollection" = mission2.phases
        procedures2: "IProcedureCollection" = phases2[0].procedures

        proc2: "IProcedure" = procedures2.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingCircular
        )
        prop2.propagate()

        formRecov: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcFormationRecover
        )
        inFormation: "IProcedureInFormation" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcInFormation
            ),
            IProcedureInFormation,
        )

        self.TestProcedureName(inFormation.get_as_procedure(), "In-Formation")

        inFormation.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL
        Assert.assertEqual(AgEAvtrPhaseOfFlight.eFlightPhaseVTOL, inFormation.flight_mode)
        inFormation.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff
        Assert.assertEqual(AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff, inFormation.flight_mode)

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

        inFormation.trajectory_blending = AgEAvtrTrajectoryBlendMode.eBlendLHCubic
        Assert.assertEqual(AgEAvtrTrajectoryBlendMode.eBlendLHCubic, inFormation.trajectory_blending)

        inFormation.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowVTOL, inFormation.fuel_flow_type)
        inFormation.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowTakeoff
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowTakeoff, inFormation.fuel_flow_type)

        def action128():
            inFormation.override_fuel_flow_value = 123

        TryCatchAssertBlock.ExpectedException("must be", action128)
        inFormation.consider_accel_for_fuel_flow = True
        Assert.assertTrue(inFormation.consider_accel_for_fuel_flow)

        inFormation.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowOverride
        inFormation.override_fuel_flow_value = 123
        Assert.assertAlmostEqual(123, inFormation.override_fuel_flow_value, delta=tolerance)

        def action129():
            inFormation.consider_accel_for_fuel_flow = True

        TryCatchAssertBlock.ExpectedException("must be", action129)

        currentPhase: "IPhase" = EarlyBoundTests.AG_Phases[0]
        vtol: "IPerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()

        def action130():
            inFormation.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action130)

        def action131():
            inFormation.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action131)

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

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        landing: "IProcedureLanding" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcLanding),
            IProcedureLanding,
        )

        headingOptions: "IRunwayHeadingOptions" = landing.runway_heading_options
        headingOptions.runway_mode = AgEAvtrRunwayHighLowEnd.eHeadwind
        Assert.assertEqual(AgEAvtrRunwayHighLowEnd.eHeadwind, headingOptions.runway_mode)

        landing.approach_mode = AgEAvtrApproachMode.eStandardInstrumentApproach
        Assert.assertEqual(AgEAvtrApproachMode.eStandardInstrumentApproach, landing.approach_mode)
        enrouteOpts: "IEnrouteAndDelayOptions" = landing.enroute_options
        self.EnrouteAndDelayOptions(enrouteOpts)

        sia: "ILandingStandardInstrumentApproach" = landing.mode_as_standard_instrument_approach

        def action132():
            testVal: "ILandingEnterDownwindPattern" = landing.mode_as_enter_downwind_pattern

        TryCatchAssertBlock.ExpectedException("must be set", action132)

        def action133():
            testVal: "ILandingInterceptGlideslope" = landing.mode_as_intercept_glideslope

        TryCatchAssertBlock.ExpectedException("must be set", action133)

        cruiseOpts: "ICruiseAirspeedAndProfileOptions" = landing.enroute_cruise_airspeed_options

        def action134():
            testVal: bool = cruiseOpts.fly_cruise_airspeed_profile

        TryCatchAssertBlock.ExpectedException("must be set", action134)

        def action135():
            cruiseOpts.fly_cruise_airspeed_profile = True

        TryCatchAssertBlock.ExpectedException("must be set", action135)

        vertOpts: "IVerticalPlaneOptions" = landing.vertical_plane_options

        def action136():
            vertOpts.max_enroute_flight_path_angle = 89

        TryCatchAssertBlock.ExpectedException("must be set", action136)

        def action137():
            vertOpts.min_enroute_flight_path_angle = -89

        TryCatchAssertBlock.ExpectedException("must be set", action137)

        def action138():
            vertOpts.max_vert_plane_radius_factor = 0.99

        TryCatchAssertBlock.ExpectedException("must be set", action138)

        sia.approach_altitude = 1201
        Assert.assertEqual(1201, sia.approach_altitude)
        sia.use_runway_terrain = True
        Assert.assertTrue(sia.use_runway_terrain)

        landing.approach_mode = AgEAvtrApproachMode.eInterceptGlideslope

        def action139():
            testVal: float = sia.approach_altitude

        TryCatchAssertBlock.ExpectedException("must be set", action139)

        def action140():
            sia.approach_altitude = 1201

        TryCatchAssertBlock.ExpectedException("must be set", action140)

        def action141():
            testVal: bool = sia.use_runway_terrain

        TryCatchAssertBlock.ExpectedException("must be set", action141)

        def action142():
            sia.use_runway_terrain = True

        TryCatchAssertBlock.ExpectedException("must be set", action142)
        self.VerticalPlaneOptions(vertOpts)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(landing, IProcedure))

    # endregion

    # region Launch
    @category("Procedure Tests")
    def test_Launch(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        missile: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: "IVehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, IVehiclePropagatorBallistic)
        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, IVehicleImpactLocationPoint)
        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()

        missile2: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile2")), IMissile
        )
        traj2: "IVehiclePropagatorBallistic" = clr.CastAs(missile2.trajectory, IVehiclePropagatorBallistic)
        impactLocation2: "IVehicleImpactLocationPoint" = clr.CastAs(traj2.impact_location, IVehicleImpactLocationPoint)
        impact2: "IVehicleImpactLLA" = clr.CastAs(impactLocation2.impact, IVehicleImpactLLA)
        impact2.lat = -20
        impact2.lon = -20
        traj2.propagate()

        launchProc: "IProcedureLaunch" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcLaunch),
            IProcedureLaunch,
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

        launchProc.attitude_mode = AgEAvtrLaunchAttitudeMode.eLaunchHoldParentAttitude

        def action143():
            launchProc.true_course_hint = 1

        TryCatchAssertBlock.ExpectedException("must be ", action143)

        launchProc.attitude_mode = AgEAvtrLaunchAttitudeMode.eLaunchAlignDirectionVector
        Assert.assertEqual(AgEAvtrLaunchAttitudeMode.eLaunchAlignDirectionVector, launchProc.attitude_mode)
        launchProc.true_course_hint = 1
        trueCourseHint: typing.Any = launchProc.true_course_hint
        Assert.assertEqual(1, float(trueCourseHint))

        launchProc.specify_launch_airspeed = False

        def action144():
            launchProc.accel_g = 2

        TryCatchAssertBlock.ExpectedException("must be ", action144)

        def action145():
            launchProc.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be ", action145)

        def action146():
            launchProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowOverride

        TryCatchAssertBlock.ExpectedException("must be ", action146)

        def action147():
            launchProc.override_fuel_flow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action147)

        launchProc.specify_launch_airspeed = True
        Assert.assertTrue(launchProc.specify_launch_airspeed)

        launchProc.accel_g = 2
        Assert.assertEqual(2, launchProc.accel_g)

        launchProc.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, launchProc.airspeed_type)
        Assert.assertAlmostEqual(251, launchProc.airspeed, delta=tolerance)
        launchProc.set_airspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, launchProc.airspeed_type)
        Assert.assertAlmostEqual(0.4, launchProc.airspeed, delta=tolerance)

        launchProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowVTOL, launchProc.fuel_flow_type)

        def action148():
            launchProc.override_fuel_flow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action148)

        launchProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowOverride
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowOverride, launchProc.fuel_flow_type)
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

        missile: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: "IVehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, IVehiclePropagatorBallistic)
        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, IVehicleImpactLocationPoint)
        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()

        missile2: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile2")), IMissile
        )
        traj2: "IVehiclePropagatorBallistic" = clr.CastAs(missile2.trajectory, IVehiclePropagatorBallistic)
        impactLocation2: "IVehicleImpactLocationPoint" = clr.CastAs(traj2.impact_location, IVehicleImpactLocationPoint)
        impact2: "IVehicleImpactLLA" = clr.CastAs(impactLocation2.impact, IVehicleImpactLLA)
        impact2.lat = -20
        impact2.lon = -20
        traj2.propagate()

        launchProc: "IProcedureLaunchDynState" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteDynState, AgEAvtrProcedureType.eProcLaunchDynState),
            IProcedureLaunchDynState,
        )

        launchProc.launch_time = "1 Jul 1999 00:00:01.000"
        time: typing.Any = launchProc.launch_time
        Assert.assertTrue(("1 Jul 1999 00:00:01.000" == str(time)))

        launchProc.coord_frame = AgEAvtrLaunchDynStateCoordFrame.eLaunchDynStateCoordFrameLocalHorizontal
        Assert.assertEqual(
            AgEAvtrLaunchDynStateCoordFrame.eLaunchDynStateCoordFrameLocalHorizontal, launchProc.coord_frame
        )

        launchProc.bearing_ref = AgEAvtrLaunchDynStateBearingRef.eLaunchDynStateBearingRefVelocity
        Assert.assertEqual(AgEAvtrLaunchDynStateBearingRef.eLaunchDynStateBearingRefVelocity, launchProc.bearing_ref)

        launchProc.launch_bearing = 1
        launchBearing: typing.Any = launchProc.launch_bearing
        Assert.assertEqual(1, float(launchBearing))

        launchProc.launch_elevation = 2
        launchElevation: typing.Any = launchProc.launch_elevation
        Assert.assertEqual(2, float(launchElevation))

        launchProc.attitude_mode = AgEAvtrLaunchAttitudeMode.eLaunchHoldParentAttitude

        def action149():
            launchProc.true_course_hint = 1

        TryCatchAssertBlock.ExpectedException("must be ", action149)

        launchProc.attitude_mode = AgEAvtrLaunchAttitudeMode.eLaunchAlignDirectionVector
        Assert.assertEqual(AgEAvtrLaunchAttitudeMode.eLaunchAlignDirectionVector, launchProc.attitude_mode)
        launchProc.true_course_hint = 1
        trueCourseHint: typing.Any = launchProc.true_course_hint
        Assert.assertEqual(1, float(trueCourseHint))

        launchProc.specify_launch_airspeed = False

        def action150():
            launchProc.accel_g = 2

        TryCatchAssertBlock.ExpectedException("must be ", action150)

        def action151():
            launchProc.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be ", action151)

        def action152():
            launchProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowOverride

        TryCatchAssertBlock.ExpectedException("must be ", action152)

        def action153():
            launchProc.override_fuel_flow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action153)

        launchProc.specify_launch_airspeed = True
        Assert.assertTrue(launchProc.specify_launch_airspeed)

        launchProc.accel_g = 2
        Assert.assertEqual(2, launchProc.accel_g)

        launchProc.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, launchProc.airspeed_type)
        Assert.assertAlmostEqual(251, launchProc.airspeed, delta=tolerance)
        launchProc.set_airspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, launchProc.airspeed_type)
        Assert.assertAlmostEqual(0.4, launchProc.airspeed, delta=tolerance)

        launchProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowVTOL, launchProc.fuel_flow_type)

        def action154():
            launchProc.override_fuel_flow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action154)

        launchProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowOverride
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowOverride, launchProc.fuel_flow_type)
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

        launchProc: "IProcedureLaunchWaypoint" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteWaypoint, AgEAvtrProcedureType.eProcLaunchWaypoint),
            IProcedureLaunchWaypoint,
        )

        launchProc.launch_time = "1 Jul 1999 00:00:01.000"
        time: typing.Any = launchProc.launch_time
        Assert.assertTrue(("1 Jul 1999 00:00:01.000" == str(time)))

        launchProc.altitude_ref = AgEAvtrAltitudeRef.eAltitudeRefMSL
        Assert.assertEqual(AgEAvtrAltitudeRef.eAltitudeRefMSL, launchProc.altitude_ref)

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

        launchProc.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, launchProc.airspeed_type)
        Assert.assertAlmostEqual(251, launchProc.airspeed, delta=tolerance)
        launchProc.set_airspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, launchProc.airspeed_type)
        Assert.assertAlmostEqual(0.4, launchProc.airspeed, delta=tolerance)

        launchProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowVTOL, launchProc.fuel_flow_type)

        def action155():
            launchProc.override_fuel_flow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action155)

        launchProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowOverride
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowOverride, launchProc.fuel_flow_type)
        launchProc.override_fuel_flow = 10001
        Assert.assertEqual(10001, launchProc.override_fuel_flow)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(launchProc, IProcedure))

    # endregion

    # region ParallelFlightLine
    @category("Procedure Tests")
    def test_ParallelFlightLine(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcFlightLine
        )
        parallelProc: "IProcedureParallelFlightLine" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcParallelFlightLine
            ),
            IProcedureParallelFlightLine,
        )

        self.TestProcedureName(parallelProc.get_as_procedure(), "Parallel Flight Line")

        alt: "IAltitudeOptions" = parallelProc.altitude_options
        self.AltitudeOptions(alt)

        enroute: "IEnrouteOptions" = parallelProc.enroute_options
        self.EnrouteOptions(enroute)

        turnOpts: "IEnrouteTurnDirectionOptions" = parallelProc.enroute_turn_direction_options
        self.EnrouteTurnDirection(turnOpts)

        airspeed: "ICruiseAirspeedAndProfileOptions" = parallelProc.enroute_cruise_airspeed_options
        self.EnrouteCruiseAirspeedAndProfile(airspeed)

        parallelProc.procedure_type = AgEAvtrFlightLineProcType.eProcTypeEnroute
        parallelProc.orientation = AgEAvtrLineOrientation.eFlightLineToRight
        Assert.assertEqual(AgEAvtrLineOrientation.eFlightLineToRight, parallelProc.orientation)
        parallelProc.separation = 11
        Assert.assertEqual(11, parallelProc.separation)
        parallelProc.offset = 12
        Assert.assertEqual(12, parallelProc.offset)
        parallelProc.leg_length = 13
        Assert.assertEqual(13, parallelProc.leg_length)

        parallelProc.procedure_type = AgEAvtrFlightLineProcType.eProcTypeTerrainFollow

        def action156():
            parallelProc.must_level_off = False

        TryCatchAssertBlock.ExpectedException("must be", action156)

        def action157():
            parallelProc.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffAutomaticManeuver

        TryCatchAssertBlock.ExpectedException("must be", action157)

        parallelProc.procedure_type = AgEAvtrFlightLineProcType.eProcTypeEnroute
        Assert.assertEqual(AgEAvtrFlightLineProcType.eProcTypeEnroute, parallelProc.procedure_type)
        parallelProc.must_level_off = True
        Assert.assertTrue(parallelProc.must_level_off)
        parallelProc.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, parallelProc.level_off_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(parallelProc, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(proc1, IProcedure))

    # endregion

    # region ReferenceState
    @category("Procedure Tests")
    def test_ReferenceState(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        refState: "IProcedureReferenceState" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteReferenceState, AgEAvtrProcedureType.eProcReferenceState
            ),
            IProcedureReferenceState,
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

        def action158():
            refState.msl_altitude = 10000

        TryCatchAssertBlock.ExpectedException("must be", action158)

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateClimb
        Assert.assertEqual(AgEAvtrRefStatePerfMode.eRefStateClimb, refState.performance_mode)

        refState.reference_frame = AgEAvtrBasicManeuverRefFrame.eEarthFrame
        Assert.assertEqual(AgEAvtrBasicManeuverRefFrame.eEarthFrame, refState.reference_frame)

        refState.fuel_flow = 5
        Assert.assertAlmostEqual(5, refState.fuel_flow, delta=tolerance)

        # ////////////// TEST FORWARD FLIGHT OPTIONS ///////////////////////

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateLanding

        def action159():
            ffTest: "IReferenceStateForwardFlightOptions" = refState.mode_as_forward_flight

        TryCatchAssertBlock.ExpectedException("must be", action159)

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateClimb
        ff: "IReferenceStateForwardFlightOptions" = refState.mode_as_forward_flight

        ff.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, ff.airspeed_type)
        Assert.assertAlmostEqual(251, ff.airspeed, delta=tolerance)
        ff.set_airspeed(AgEAvtrAirspeedType.eMach, 0.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, ff.airspeed_type)
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

        def action160():
            altRateTest: typing.Any = ff.altitude_rate

        TryCatchAssertBlock.ExpectedException("Wind Frame", action160)

        def action161():
            headingTest: typing.Any = ff.heading

        TryCatchAssertBlock.ExpectedException("Wind Frame", action161)

        refState.reference_frame = AgEAvtrBasicManeuverRefFrame.eWindFrame

        def action162():
            fpaTest: typing.Any = ff.flight_path_angle

        TryCatchAssertBlock.ExpectedException("Earth Frame", action162)

        def action163():
            courseTest: typing.Any = ff.course

        TryCatchAssertBlock.ExpectedException("Earth Frame", action163)

        ff.altitude_rate = 6
        Assert.assertEqual(6, ff.altitude_rate)

        ff.heading = 7
        heading: typing.Any = ff.heading
        Assert.assertEqual(7, float(heading))

        ff.set_longitudinal_accel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, 0.5)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, ff.longitudinal_accel_type)
        Assert.assertEqual(0.5, ff.groundspeed_dot)
        ff.set_longitudinal_accel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, 0.6)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, ff.longitudinal_accel_type)
        Assert.assertEqual(0.6, ff.tas_dot)

        ff.set_lateral_accel(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, 1.3)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, ff.lateral_accel_type)
        Assert.assertEqual(1.3, ff.course_dot)
        ff.set_lateral_accel(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, 1.4)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, ff.lateral_accel_type)
        Assert.assertEqual(1.4, ff.heading_dot)

        ff.set_attitude_rate(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, 1.5)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, ff.attitude_rate_type)
        Assert.assertEqual(1.5, ff.pitch_rate)
        ff.set_attitude_rate(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, 1.6)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, ff.attitude_rate_type)
        Assert.assertEqual(1.6, ff.push_pull_g)

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateLanding

        def action164():
            airspeedTest: float = ff.airspeed

        TryCatchAssertBlock.ExpectedException("must be", action164)

        # ////////////// TEST TAKEOFF LANDING OPTIONS ///////////////////////
        # Note: Should be same as forward flight options except on different interface

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action165():
            tlTest: "IReferenceStateTakeoffLandingOptions" = refState.mode_as_takeoff_landing

        TryCatchAssertBlock.ExpectedException("must be", action165)

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateLanding
        tl: "IReferenceStateTakeoffLandingOptions" = refState.mode_as_takeoff_landing
        refState.reference_frame = AgEAvtrBasicManeuverRefFrame.eEarthFrame

        tl.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, tl.airspeed_type)
        Assert.assertAlmostEqual(251, tl.airspeed, delta=tolerance)
        tl.set_airspeed(AgEAvtrAirspeedType.eMach, 0.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, tl.airspeed_type)
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

        def action166():
            altRateTest: typing.Any = tl.altitude_rate

        TryCatchAssertBlock.ExpectedException("Wind Frame", action166)

        def action167():
            headingTest: typing.Any = tl.heading

        TryCatchAssertBlock.ExpectedException("Wind Frame", action167)

        refState.reference_frame = AgEAvtrBasicManeuverRefFrame.eWindFrame

        def action168():
            fpaTest: typing.Any = tl.flight_path_angle

        TryCatchAssertBlock.ExpectedException("Earth Frame", action168)

        def action169():
            courseTest: typing.Any = tl.course

        TryCatchAssertBlock.ExpectedException("Earth Frame", action169)

        tl.altitude_rate = 6
        Assert.assertEqual(6, tl.altitude_rate)

        tl.heading = 7
        heading = tl.heading
        Assert.assertEqual(7, float(heading))

        tl.set_longitudinal_accel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, 0.5)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, tl.longitudinal_accel_type)
        Assert.assertEqual(0.5, tl.groundspeed_dot)
        tl.set_longitudinal_accel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, 0.6)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, tl.longitudinal_accel_type)
        Assert.assertEqual(0.6, tl.tas_dot)

        tl.set_lateral_accel(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, 1.3)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, tl.lateral_accel_type)
        Assert.assertEqual(1.3, tl.course_dot)
        tl.set_lateral_accel(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, 1.4)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, tl.lateral_accel_type)
        Assert.assertEqual(1.4, tl.heading_dot)

        tl.set_attitude_rate(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, 1.5)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, tl.attitude_rate_type)
        Assert.assertEqual(1.5, tl.pitch_rate)
        tl.set_attitude_rate(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, 1.6)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, tl.attitude_rate_type)
        Assert.assertEqual(1.6, tl.push_pull_g)

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action170():
            airspeedTest: float = tl.airspeed

        TryCatchAssertBlock.ExpectedException("must be", action170)

        # ////////////// TEST HOVER OPTIONS ///////////////////////

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action171():
            hoverTest: "IReferenceStateHoverOptions" = refState.mode_as_hover

        TryCatchAssertBlock.ExpectedException("must be", action171)

        currentPhase: "IPhase" = EarlyBoundTests.AG_Phases[0]
        vtol: "IPerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()

        def action172():
            refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateHover

        TryCatchAssertBlock.ExpectedException("VTOL", action172)
        currentPhase.set_default_perf_models()

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateHover

        def action173():
            refState.reference_frame = AgEAvtrBasicManeuverRefFrame.eEarthFrame

        TryCatchAssertBlock.ExpectedException("must be", action173)

        hoverOpts: "IReferenceStateHoverOptions" = refState.mode_as_hover

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

        hoverOpts.set_longitudinal_accel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, 0.5)
        Assert.assertEqual(
            AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, hoverOpts.longitudinal_accel_type
        )
        Assert.assertEqual(0.5, hoverOpts.groundspeed_dot)
        hoverOpts.set_longitudinal_accel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, 0.6)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, hoverOpts.longitudinal_accel_type)
        Assert.assertEqual(0.6, hoverOpts.tas_dot)

        hoverOpts.set_attitude_rate(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, 1.5)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, hoverOpts.attitude_rate_type)
        Assert.assertEqual(1.5, hoverOpts.pitch_rate)
        hoverOpts.set_attitude_rate(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, 1.6)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, hoverOpts.attitude_rate_type)
        Assert.assertEqual(1.6, hoverOpts.push_pull_g)

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action174():
            groundspeedTest: float = hoverOpts.groundspeed

        TryCatchAssertBlock.ExpectedException("must be", action174)

        # ////////////// TEST WEIGHT ON WHEELS OPTIONS ///////////////////////

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action175():
            wowTest: "IReferenceStateWeightOnWheelsOptions" = refState.mode_as_weight_on_wheels

        TryCatchAssertBlock.ExpectedException("must be", action175)

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateTakeoffRun

        def action176():
            refState.reference_frame = AgEAvtrBasicManeuverRefFrame.eEarthFrame

        TryCatchAssertBlock.ExpectedException("must be", action176)

        wowOpts: "IReferenceStateWeightOnWheelsOptions" = refState.mode_as_weight_on_wheels

        wowOpts.groundspeed = 200
        Assert.assertEqual(200, wowOpts.groundspeed)

        wowOpts.heading = 7
        heading = wowOpts.heading
        Assert.assertEqual(7, float(heading))

        wowOpts.set_longitudinal_accel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, 0.5)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, wowOpts.longitudinal_accel_type)
        Assert.assertEqual(0.5, wowOpts.groundspeed_dot)
        wowOpts.set_longitudinal_accel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, 0.6)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, wowOpts.longitudinal_accel_type)
        Assert.assertEqual(0.6, wowOpts.tas_dot)

        wowOpts.set_lateral_accel(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, 1.3)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, wowOpts.lateral_accel_type)
        Assert.assertEqual(1.3, wowOpts.course_dot)
        wowOpts.set_lateral_accel(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, 1.4)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, wowOpts.lateral_accel_type)
        Assert.assertEqual(1.4, wowOpts.heading_dot)

        refState.performance_mode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action177():
            groundspeedTest: float = wowOpts.groundspeed

        TryCatchAssertBlock.ExpectedException("must be", action177)

        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(refState, IProcedure))

    # endregion

    # region Takeoff
    @category("Procedure Tests")
    def test_Takeoff(self):
        self.EmptyProcedures()

        takeoff: "IProcedureTakeoff" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff),
            IProcedureTakeoff,
        )

        headingOptions: "IRunwayHeadingOptions" = takeoff.runway_heading_options
        headingOptions.runway_mode = AgEAvtrRunwayHighLowEnd.eHeadwind
        Assert.assertEqual(AgEAvtrRunwayHighLowEnd.eHeadwind, headingOptions.runway_mode)

        takeoff.takeoff_mode = AgEAvtrTakeoffMode.eTakeoffNormal
        takeoffNormal: "ITakeoffNormal" = takeoff.mode_as_normal

        def action178():
            testVal: "ITakeoffDeparturePoint" = takeoff.mode_as_departure_point

        TryCatchAssertBlock.ExpectedException("must be set", action178)

        def action179():
            testVal: "ITakeoffLowTransition" = takeoff.mode_as_low_transition

        TryCatchAssertBlock.ExpectedException("must be set", action179)

        takeoffNormal.departure_altitude = 501
        Assert.assertEqual(501, takeoffNormal.departure_altitude)
        takeoffNormal.use_runway_terrain = True
        Assert.assertTrue(takeoffNormal.use_runway_terrain)

        takeoff.takeoff_mode = AgEAvtrTakeoffMode.eTakeoffFlyToDeparturePoint

        def action180():
            testVal: float = takeoffNormal.departure_altitude

        TryCatchAssertBlock.ExpectedException("must be set", action180)

        def action181():
            takeoffNormal.departure_altitude = 501

        TryCatchAssertBlock.ExpectedException("must be set", action181)

        def action182():
            testVal: bool = takeoffNormal.use_runway_terrain

        TryCatchAssertBlock.ExpectedException("must be set", action182)

        def action183():
            takeoffNormal.use_runway_terrain = True

        TryCatchAssertBlock.ExpectedException("must be set", action183)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))

    # endregion

    # region TerrainFollowing
    @category("Procedure Tests")
    def test_TerrainFollowing(self):
        self.EmptyProcedures()

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        terrainFollow: "IProcedureTerrainFollow" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTerrainFollowing
            ),
            IProcedureTerrainFollow,
        )

        terrainFollow.altitude_agl = 600
        Assert.assertEqual(600, terrainFollow.altitude_agl)

        nav: "INavigationOptions" = terrainFollow.navigation_options
        self.NavigationOptions(nav)

        terrainAirspeed: "ICruiseAirspeedOptions" = terrainFollow.terrain_following_airspeed_options
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

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        toHover: "IProcedureTransitionToHover" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToHover
            ),
            IProcedureTransitionToHover,
        )
        toFlight: "IProcedureTransitionToForwardFlight" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToForwardFlight
            ),
            IProcedureTransitionToForwardFlight,
        )

        toFlight.set_transition_into_wind()
        Assert.assertEqual(AgEAvtrVTOLTransitionMode.eTransitionIntoWind, toFlight.transition_course_mode)

        toFlight.set_absolute_course(5, True)
        Assert.assertEqual(AgEAvtrVTOLTransitionMode.eTransitionAbsoluteHdg, toFlight.transition_course_mode)
        absCourse: typing.Any = toFlight.absolute_course
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertTrue(toFlight.use_magnetic_heading)

        toFlight.set_relative_course(4)
        relCourse: typing.Any = toFlight.relative_course
        Assert.assertAlmostEqual(4, float(relCourse), delta=tolerance)
        Assert.assertEqual(AgEAvtrVTOLTransitionMode.eTransitionRelativeHdg, toFlight.transition_course_mode)

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

        takeoff: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        toHover: "IProcedureTransitionToHover" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToHover
            ),
            IProcedureTransitionToHover,
        )

        toHover.altitude = 600
        Assert.assertEqual(600, toHover.altitude)
        toHover.altitude_reference = AgEAvtrAGLMSL.eAltAGL
        Assert.assertEqual(AgEAvtrAGLMSL.eAltAGL, toHover.altitude_reference)

        enrouteOpts: "IEnrouteOptions" = toHover.enroute_options
        self.EnrouteOptions(enrouteOpts)

        enrouteTurnDirOpts: "IEnrouteTurnDirectionOptions" = toHover.enroute_turn_direction_options
        self.EnrouteTurnDirection(enrouteTurnDirOpts)

        verticalPlaneOpts: "IVerticalPlaneAndFlightPathOptions" = toHover.vertical_plane_options
        self.VerticalPlaneAndFlightPathOptions(verticalPlaneOpts)

        toHover.set_transition_into_wind()
        Assert.assertTrue(toHover.transition_into_wind)

        toHover.set_transition_course(5, True)
        course: typing.Any = toHover.course
        Assert.assertAlmostEqual(5, float(course), delta=tolerance)
        Assert.assertTrue(toHover.use_magnetic_heading)

        toHover.smooth_transition_mode = AgEAvtrTransitionToHoverMode.eTranslationOnly
        Assert.assertEqual(AgEAvtrTransitionToHoverMode.eTranslationOnly, toHover.smooth_transition_mode)

        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(toHover, IProcedure))

    # endregion

    # region VerticalLanding
    @category("Procedure Tests")
    def test_VerticalLanding(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteVTOLPoint, AgEAvtrProcedureType.eProcVerticalTakeoff
        )
        vertLanding: "IProcedureVerticalLanding" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteVTOLPoint, AgEAvtrProcedureType.eProcVerticalLanding
            ),
            IProcedureVerticalLanding,
        )

        vertLanding.altitude_above_point = 101
        Assert.assertEqual(101, vertLanding.altitude_above_point)
        vertLanding.final_altitude_rate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, vertLanding.final_altitude_rate)
        vertLanding.altitude_offset = 5
        Assert.assertEqual(5, vertLanding.altitude_offset)

        vertLanding.heading_mode = AgEAvtrVertLandingMode.eVertLandingIndependent
        Assert.assertEqual(AgEAvtrVertLandingMode.eVertLandingIndependent, vertLanding.heading_mode)
        vertLanding.heading_mode = AgEAvtrVertLandingMode.eVertLandingAlignTranslationCourseOverride
        Assert.assertEqual(AgEAvtrVertLandingMode.eVertLandingAlignTranslationCourseOverride, vertLanding.heading_mode)

        vertLanding.set_heading(11, False)
        hdg: typing.Any = vertLanding.heading
        Assert.assertAlmostEqual(11, float(hdg), delta=tolerance)
        Assert.assertEqual(False, vertLanding.use_magnetic_heading)

        vertLanding.heading_mode = AgEAvtrVertLandingMode.eVertLandingAlignTranslationCourse
        Assert.assertEqual(AgEAvtrVertLandingMode.eVertLandingAlignTranslationCourse, vertLanding.heading_mode)

        def action184():
            vertLanding.set_heading(11, False)

        TryCatchAssertBlock.ExpectedException("must be", action184)

        vertLanding.heading_mode = AgEAvtrVertLandingMode.eVertLandingIntoWind
        Assert.assertEqual(AgEAvtrVertLandingMode.eVertLandingIntoWind, vertLanding.heading_mode)

        def action185():
            vertLanding.set_heading(11, False)

        TryCatchAssertBlock.ExpectedException("must be", action185)

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

        vertTakeoff: "IProcedureVerticalTakeoff" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteVTOLPoint, AgEAvtrProcedureType.eProcVerticalTakeoff
            ),
            IProcedureVerticalTakeoff,
        )

        vertTakeoff.altitude_above_point = 101
        Assert.assertEqual(101, vertTakeoff.altitude_above_point)
        vertTakeoff.final_altitude_rate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, vertTakeoff.final_altitude_rate)
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
        )
        EarlyBoundTests.AG_AvtrProp.propagate()

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj: "IStkObject" = acObj.copy_object("AC2")
        ac2: "IAircraft" = clr.CastAs(ac2Obj, IAircraft)
        route2: "IVehiclePropagatorAviator" = clr.CastAs(ac2.route, IVehiclePropagatorAviator)
        prop2: "IAviatorPropagator" = clr.CastAs(route2.avtr_propagator, IAviatorPropagator)
        mission2: "IMission" = prop2.avtr_mission
        prop2.propagate()

        EarlyBoundTests.AG_Procedures.remove_at_index(1)
        EarlyBoundTests.AG_Procedures.remove_at_index(0)
        vgtProc: "IProcedureVGTPoint" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcVGTPoint),
            IProcedureVGTPoint,
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
        vgtProc.interpolate_point_pos_vel = True
        Assert.assertTrue(vgtProc.interpolate_point_pos_vel)

        vgtProc.duration = 5
        Assert.assertEqual(5, vgtProc.duration)
        vgtProc.use_max_point_stop_time = True
        Assert.assertTrue(vgtProc.use_max_point_stop_time)

        vgtProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowTakeoff

        def action186():
            vgtProc.override_fuel_flow_value = 123

        TryCatchAssertBlock.ExpectedException("must be", action186)
        vgtProc.consider_accel_for_fuel_flow = True
        Assert.assertTrue(vgtProc.consider_accel_for_fuel_flow)

        vgtProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowOverride
        vgtProc.override_fuel_flow_value = 123
        Assert.assertAlmostEqual(123, vgtProc.override_fuel_flow_value, delta=tolerance)

        def action187():
            vgtProc.consider_accel_for_fuel_flow = True

        TryCatchAssertBlock.ExpectedException("must be", action187)

        vgtProc.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff
        Assert.assertEqual(AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff, vgtProc.flight_mode)
        vgtProc.display_step_time = 4
        Assert.assertEqual(4, vgtProc.display_step_time)

        vgtProc.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL
        Assert.assertEqual(vgtProc.flight_mode, AgEAvtrPhaseOfFlight.eFlightPhaseVTOL)
        vgtProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(vgtProc.fuel_flow_type, AgEAvtrFuelFlowType.eFuelFlowVTOL)
        currentPhase: "IPhase" = EarlyBoundTests.AG_Phases[0]
        vtol: "IPerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()

        def action188():
            vgtProc.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action188)

        def action189():
            vgtProc.fuel_flow_type = AgEAvtrFuelFlowType.eFuelFlowVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action189)

        currentPhase.set_default_perf_models()
        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(vgtProc, IProcedure))
        ac2Obj.unload()

    # endregion

    # region BasicManeuver
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuver(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
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

        def action190():
            basicManeuver.use_stop_fuel_state = False

        TryCatchAssertBlock.ExpectedException("At least one", action190)

        basicManeuver.terrain_impact_mode = AgEAvtrBasicManeuverAltitudeLimit.eBasicManeuverAltLimitContinue

        def action191():
            basicManeuver.terrain_impact_time_offset = 1

        TryCatchAssertBlock.ExpectedException("terrain impact mode", action191)
        basicManeuver.terrain_impact_mode = AgEAvtrBasicManeuverAltitudeLimit.eBasicManeuverAltLimitError

        def action192():
            basicManeuver.terrain_impact_time_offset = 1

        TryCatchAssertBlock.ExpectedException("terrain impact mode", action192)

        basicManeuver.fuel_flow_type = AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowCruise

        def action193():
            basicManeuver.override_fuel_flow_value = 1

        TryCatchAssertBlock.ExpectedException("fuel flow source", action193)

        def action194():
            testVal: bool = basicManeuver.scale_fuel_flow

        TryCatchAssertBlock.ExpectedException("fuel flow source", action194)

        def action195():
            basicManeuver.scale_fuel_flow = True

        TryCatchAssertBlock.ExpectedException("fuel flow source", action195)

        basicManeuver.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL
        Assert.assertEqual(basicManeuver.flight_mode, AgEAvtrPhaseOfFlight.eFlightPhaseVTOL)
        basicManeuver.fuel_flow_type = AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowVTOL
        Assert.assertEqual(basicManeuver.fuel_flow_type, AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowVTOL)
        currentPhase: "IPhase" = EarlyBoundTests.AG_Phases[0]
        vtol: "IPerformanceModelOptions" = currentPhase.get_performance_model_by_type("VTOL")
        vtol.delete()

        def action196():
            basicManeuver.flight_mode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action196)

        def action197():
            basicManeuver.fuel_flow_type = AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action197)

        currentPhase.set_default_perf_models()
        TestBase.Application.unit_preferences.reset_units()
        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAileronRoll
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAileronRoll(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Aileron Roll"
        roll: "IBasicManeuverStrategyAileronRoll" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyAileronRoll
        )

        roll.flight_path_option = AgEAvtrAileronRollFlightPath.eZeroGFlightPath
        Assert.assertEqual(AgEAvtrAileronRollFlightPath.eZeroGFlightPath, roll.flight_path_option)

        Assert.assertEqual("Aileron Roll", basicManeuver.profile_strategy_type)
        rollProfile: "IBasicManeuverStrategyAileronRoll" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategyAileronRoll
        )
        Assert.assertEqual(AgEAvtrAileronRollFlightPath.eZeroGFlightPath, rollProfile.flight_path_option)

        roll.active_mode = AgEAvtrAileronRollMode.eRollToAngle

        def action198():
            roll.roll_orientation = AgEAvtrRollUprightInverted.eRollInverted

        TryCatchAssertBlock.ExpectedException("must be", action198)

        roll.active_mode = AgEAvtrAileronRollMode.eRollToOrientation
        roll.roll_orientation = AgEAvtrRollUprightInverted.eRollInverted
        Assert.assertEqual(AgEAvtrRollUprightInverted.eRollInverted, roll.roll_orientation)

        roll.roll_rate_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action199():
            angle: typing.Any = roll.override_roll_rate

        TryCatchAssertBlock.ExpectedException("must be", action199)
        roll.roll_rate_mode = AgEAvtrPerfModelOverride.eOverride
        roll.override_roll_rate = 20
        overrideRollRate: typing.Any = roll.override_roll_rate
        Assert.assertEqual(20, float(overrideRollRate))

        airspeedOpts: "IBasicManeuverAirspeedOptions" = roll.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAutopilotNav
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAutopilotNav(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Autopilot - Horizontal Plane"
        autopilot: "IBasicManeuverStrategyAutopilotNav" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyAutopilotNav
        )

        autopilot.active_mode = AgEAvtrAutopilotHorizPlaneMode.eAutopilotAbsoluteCourse
        autopilot.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 1000)
        turnRad: float = autopilot.control_limit_turn_radius
        Assert.assertEqual(1000, turnRad)

        autopilot.active_mode = AgEAvtrAutopilotHorizPlaneMode.eAutopilotCourseRate

        def action200():
            autopilot.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 1000)

        TryCatchAssertBlock.ExpectedException("must be", action200)

        autopilot.compensate_for_coriolis_accel = True
        Assert.assertTrue(autopilot.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAutopilotProfile
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAutopilotProfile(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Autopilot - Vertical Plane"
        autopilot: "IBasicManeuverStrategyAutopilotProf" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategyAutopilotProf
        )
        autopilot.altitude_mode = AgEAvtrAutopilotAltitudeMode.eAutopilotHoldInitAltitude

        def action201():
            testVal: float = autopilot.absolute_altitude

        TryCatchAssertBlock.ExpectedException("must be", action201)

        def action202():
            testVal: float = autopilot.relative_altitude_change

        TryCatchAssertBlock.ExpectedException("must be", action202)

        def action203():
            testVal: float = autopilot.altitude_rate

        TryCatchAssertBlock.ExpectedException("must be", action203)

        def action204():
            testVal: typing.Any = autopilot.fpa

        TryCatchAssertBlock.ExpectedException("must be", action204)

        autopilot.altitude_control_mode = AgEAvtrAutopilotAltitudeControlMode.eAutopilotAltitudeRate
        autopilot.control_altitude_rate_value = 2001
        Assert.assertEqual(2001, autopilot.control_altitude_rate_value)

        autopilot.altitude_control_mode = AgEAvtrAutopilotAltitudeControlMode.eAutopilotFPA
        autopilot.control_fpa_value = 11
        controlFPA: typing.Any = autopilot.control_fpa_value
        Assert.assertEqual(11, controlFPA)

        autopilot.altitude_control_mode = AgEAvtrAutopilotAltitudeControlMode.eAutopilotPerfModels

        def action205():
            testVal: float = autopilot.control_altitude_rate_value

        TryCatchAssertBlock.ExpectedException("must be", action205)

        def action206():
            testVal: typing.Any = autopilot.control_fpa_value

        TryCatchAssertBlock.ExpectedException("must be", action206)

        autopilot.control_limit_mode = AgEAvtrPerfModelOverride.eOverride
        autopilot.max_pitch_rate = 11
        pitchRate: typing.Any = autopilot.max_pitch_rate
        Assert.assertEqual(11, pitchRate)
        autopilot.control_limit_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action207():
            autopilot.max_pitch_rate = 11

        TryCatchAssertBlock.ExpectedException("must be", action207)

        autopilot.damping_ratio = 1.5
        Assert.assertEqual(1.5, autopilot.damping_ratio)

        autopilot.altitude_mode = AgEAvtrAutopilotAltitudeMode.eAutopilotSpecifyAltitude
        autopilot.absolute_altitude = 10001
        Assert.assertEqual(10001, autopilot.absolute_altitude)

        autopilot.altitude_mode = AgEAvtrAutopilotAltitudeMode.eAutopilotSpecifyAltitudeChange
        autopilot.relative_altitude_change = 1
        Assert.assertEqual(1, autopilot.relative_altitude_change)

        autopilot.altitude_mode = AgEAvtrAutopilotAltitudeMode.eAutopilotSpecifyAltitudeRate
        autopilot.altitude_rate = 1
        Assert.assertEqual(1, autopilot.altitude_rate)

        autopilot.altitude_mode = AgEAvtrAutopilotAltitudeMode.eAutopilotSpecifyFPA
        autopilot.fpa = 1
        fpa: typing.Any = autopilot.fpa
        Assert.assertEqual(1, fpa)

        autopilot.altitude_mode = AgEAvtrAutopilotAltitudeMode.eAutopilotBallistic

        def action208():
            autopilot.altitude_control_mode = AgEAvtrAutopilotAltitudeControlMode.eAutopilotFPA

        TryCatchAssertBlock.ExpectedException("must be", action208)

        def action209():
            autopilot.damping_ratio = 1.5

        TryCatchAssertBlock.ExpectedException("must be", action209)

        airspeedOpts: "IBasicManeuverAirspeedOptions" = autopilot.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        autopilot.compensate_for_coriolis_accel = True
        Assert.assertTrue(autopilot.compensate_for_coriolis_accel)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverBallistic3D
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverBallistic3D(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Ballistic3D"
        ballistic: "IBasicManeuverStrategyBallistic3D" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyBallistic3D
        )

        ballistic.control_mode = AgEAvtrBallistic3DControlMode.eBallistic3DCompensateForWind
        Assert.assertEqual(AgEAvtrBallistic3DControlMode.eBallistic3DCompensateForWind, ballistic.control_mode)

        self.BasicManeuverAirspeedOptions(ballistic.airspeed_options)

        def action210():
            ballistic.wind_force_effective_area = 10

        TryCatchAssertBlock.ExpectedException("must be", action210)

        def action211():
            ballistic.parachute_area = 5

        TryCatchAssertBlock.ExpectedException("must be", action211)

        def action212():
            ballistic.parachute_cd = 1.5

        TryCatchAssertBlock.ExpectedException("must be", action212)

        ballistic.control_mode = AgEAvtrBallistic3DControlMode.eBallistic3DWindPushesVehicle
        Assert.assertEqual(AgEAvtrBallistic3DControlMode.eBallistic3DWindPushesVehicle, ballistic.control_mode)

        self.BasicManeuverAirspeedOptions(ballistic.airspeed_options)

        ballistic.wind_force_effective_area = 10
        Assert.assertEqual(10, ballistic.wind_force_effective_area)

        def action213():
            ballistic.parachute_area = 5

        TryCatchAssertBlock.ExpectedException("must be", action213)

        def action214():
            ballistic.parachute_cd = 1.5

        TryCatchAssertBlock.ExpectedException("must be", action214)

        ballistic.control_mode = AgEAvtrBallistic3DControlMode.eBallistic3DParachuteMode
        Assert.assertEqual(AgEAvtrBallistic3DControlMode.eBallistic3DParachuteMode, ballistic.control_mode)

        ballistic.parachute_area = 5
        Assert.assertEqual(5, ballistic.parachute_area)
        ballistic.parachute_cd = 1.5
        Assert.assertEqual(1.5, ballistic.parachute_cd)

        ballistic.wind_force_effective_area = 11
        Assert.assertEqual(11, ballistic.wind_force_effective_area)

        def action215():
            self.BasicManeuverAirspeedOptions(ballistic.airspeed_options)

        TryCatchAssertBlock.ExpectedException("must be", action215)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverBarrelRoll
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverBarrelRoll(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Barrel Roll"
        roll: "IBasicManeuverStrategyBarrelRoll" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyBarrelRoll
        )
        roll.helix_angle = 359
        helixAngle: typing.Any = roll.helix_angle
        roll.helix_angle_mode = AgEAvtrAngleMode.eRelativeAngle
        Assert.assertEqual(359, float(helixAngle))
        Assert.assertEqual(AgEAvtrAngleMode.eRelativeAngle, roll.helix_angle_mode)

        Assert.assertEqual("Barrel Roll", basicManeuver.profile_strategy_type)
        rollProfile: "IBasicManeuverStrategyBarrelRoll" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategyBarrelRoll
        )
        helixAngleProfile: typing.Any = rollProfile.helix_angle
        Assert.assertEqual(359, float(helixAngleProfile))
        Assert.assertEqual(AgEAvtrAngleMode.eRelativeAngle, rollProfile.helix_angle_mode)

        roll.hold_init_tas = True

        def action216():
            roll.set_airspeeds(AgEAvtrAirspeedType.eMach, 0.1, 0.2)

        TryCatchAssertBlock.ExpectedException("must be", action216)

        roll.hold_init_tas = False
        roll.set_airspeeds(AgEAvtrAirspeedType.eMach, 0.1, 0.2)
        Assert.assertEqual(0.1, roll.top_airspeed)
        Assert.assertEqual(0.2, roll.bottom_airspeed)

        roll.set_airspeeds(AgEAvtrAirspeedType.eTAS, 200, 201)
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Profile Segment - Bezier"
        bezier: "IBasicManeuverStrategyBezier" = clr.CastAs(basicManeuver.profile, IBasicManeuverStrategyBezier)

        bezier.reference_frame = AgEAvtrBasicManeuverRefFrame.eWindFrame
        Assert.assertEqual(AgEAvtrBasicManeuverRefFrame.eWindFrame, bezier.reference_frame)

        bezier.downrange = 11
        Assert.assertEqual(11, bezier.downrange)
        bezier.altitude = 10000
        Assert.assertEqual(10000, bezier.altitude)
        bezier.set_airspeed(AgEAvtrAirspeedType.eTAS, 250)
        Assert.assertEqual(250, bezier.airspeed)
        bezier.set_airspeed(AgEAvtrAirspeedType.eMach, 0.2)
        Assert.assertEqual(0.2, bezier.airspeed)

        bezier.set_vertical_velocity(AgEAvtrFlyToFlightPathAngleMode.eFlyToAltRate, 1000)
        Assert.assertAlmostEqual(1000, bezier.altitude_rate, delta=tolerance)
        bezier.set_vertical_velocity(AgEAvtrFlyToFlightPathAngleMode.eFlyToFlightPathAngle, 3)
        angle: typing.Any = bezier.flight_path_angle
        Assert.assertEqual(3, float(angle))

        bezier.set_stop_airspeed(True, AgEAvtrAirspeedType.eTAS, 260)
        Assert.assertTrue(bezier.use_stop_at_airspeed)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, bezier.stop_airspeed_type)
        Assert.assertEqual(260, bezier.stop_airspeed)

        bezier.set_stop_airspeed(False, AgEAvtrAirspeedType.eMach, 0.2)
        Assert.assertEqual(False, bezier.use_stop_at_airspeed)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, bezier.stop_airspeed_type)
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Cruise Profile"
        cruise: "IBasicManeuverStrategyCruiseProfile" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategyCruiseProfile
        )

        cruise.use_default_cruise_altitude = True

        def action217():
            levelOff: bool = cruise.level_off

        TryCatchAssertBlock.ExpectedException("must be", action217)

        def action218():
            cruise.level_off = True

        TryCatchAssertBlock.ExpectedException("must be", action218)

        def action219():
            cruise.requested_altitude = 10000

        TryCatchAssertBlock.ExpectedException("must be", action219)

        cruise.use_default_cruise_altitude = False
        cruise.level_off = True
        Assert.assertTrue(cruise.level_off)

        def action220():
            cruise.requested_altitude = 10000

        TryCatchAssertBlock.ExpectedException("must be", action220)

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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Fly AOA"
        flyAOA: "IBasicManeuverStrategyFlyAOA" = clr.CastAs(basicManeuver.navigation, IBasicManeuverStrategyFlyAOA)

        flyAOA.aoa = 11
        aoa: typing.Any = flyAOA.aoa
        Assert.assertEqual(11, float(aoa))

        Assert.assertEqual("Fly AOA", basicManeuver.profile_strategy_type)
        flyAOAProfile: "IBasicManeuverStrategyFlyAOA" = clr.CastAs(basicManeuver.profile, IBasicManeuverStrategyFlyAOA)
        aoaProfile: typing.Any = flyAOAProfile.aoa
        Assert.assertEqual(11, float(aoaProfile))

        flyAOA.turn_direction = AgEAvtrFlyAOALeftRight.eFlyAOALeft
        flyAOA.control_roll_angle = False
        flyAOA.roll_rate_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action221():
            value: typing.Any = flyAOA.override_roll_rate

        TryCatchAssertBlock.ExpectedException("must be", action221)
        flyAOA.roll_rate_mode = AgEAvtrPerfModelOverride.eOverride
        flyAOA.override_roll_rate = 29
        rate: typing.Any = flyAOA.override_roll_rate
        Assert.assertAlmostEqual(29, float(rate), delta=tolerance)

        def action222():
            flyAOA.roll_angle = 59

        TryCatchAssertBlock.ExpectedException("must be", action222)

        def action223():
            flyAOA.stop_on_roll_angle = True

        TryCatchAssertBlock.ExpectedException("must be", action223)
        flyAOA.control_roll_angle = True
        flyAOA.roll_angle = 59
        angle: typing.Any = flyAOA.roll_angle
        Assert.assertAlmostEqual(59, float(angle), delta=tolerance)
        flyAOA.stop_on_roll_angle = True
        Assert.assertTrue(flyAOA.stop_on_roll_angle)

        flyAOA.turn_direction = AgEAvtrFlyAOALeftRight.eFlyAOANoRoll
        flyAOA.stop_on_roll_angle = False
        Assert.assertFalse(flyAOA.stop_on_roll_angle)

        def action224():
            flyAOA.roll_rate_mode = AgEAvtrPerfModelOverride.eOverride

        TryCatchAssertBlock.ExpectedException("must be", action224)

        def action225():
            flyAOA.override_roll_rate = 29

        TryCatchAssertBlock.ExpectedException("must be", action225)

        def action226():
            flyAOA.control_roll_angle = True

        TryCatchAssertBlock.ExpectedException("must be", action226)

        def action227():
            flyAOA.roll_angle = 59

        TryCatchAssertBlock.ExpectedException("must be", action227)

        airspeedOpts: "IBasicManeuverAirspeedOptions" = flyAOA.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverGlide
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverGlide(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Glide - Vertical Plane"
        glide: "IBasicManeuverStrategyGlideProfile" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategyGlideProfile
        )

        glide.hold_initial_airspeed = True
        Assert.assertTrue(glide.hold_initial_airspeed)

        def action228():
            glide.set_airspeed(AgEAvtrAirspeedType.eMach, 0.5)

        TryCatchAssertBlock.ExpectedException("Hold Initial Airspeed must be disabled", action228)

        glide.set_glide_speed_control_mode(
            AgEAvtrBasicManeuverGlideSpeedControlMode.eGlideSpeedAtAltitude, 2000
        )  # BUG - this should throw an exception, but does not, and does not change values in the GUI.
        # TryCatchAssertBlock.ExpectedException("Hold Initial Airspeed must be disabled", delegate () { glide.SetGlideSpeedControlMode(AgEAvtrBasicManeuverGlideSpeedControlMode.eGlideSpeedAtAltitude, 2000); });

        glide.hold_initial_airspeed = False
        Assert.assertFalse(glide.hold_initial_airspeed)

        glide.set_airspeed(AgEAvtrAirspeedType.eMach, 0.5)
        Assert.assertAlmostEqual(0.5, glide.airspeed, delta=1e-06)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, glide.airspeed_type)

        glide.set_airspeed(AgEAvtrAirspeedType.eCAS, 0.6)
        Assert.assertAlmostEqual(0.6, glide.airspeed, delta=1e-06)
        Assert.assertEqual(AgEAvtrAirspeedType.eCAS, glide.airspeed_type)

        glide.set_airspeed(AgEAvtrAirspeedType.eEAS, 0.7)
        Assert.assertAlmostEqual(0.7, glide.airspeed, delta=1e-06)
        Assert.assertEqual(AgEAvtrAirspeedType.eEAS, glide.airspeed_type)

        glide.set_airspeed(AgEAvtrAirspeedType.eTAS, 0.8)
        Assert.assertAlmostEqual(0.8, glide.airspeed, delta=1e-06)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, glide.airspeed_type)

        glide.set_glide_speed_control_mode(AgEAvtrBasicManeuverGlideSpeedControlMode.eGlideSpeedImmediateChange, 1000)
        Assert.assertEqual(
            AgEAvtrBasicManeuverGlideSpeedControlMode.eGlideSpeedImmediateChange, glide.glide_speed_control_mode
        )

        def action229():
            x: float = glide.glide_speed_control_alt

        TryCatchAssertBlock.ExpectedException("speed control mode must be", action229)

        glide.set_glide_speed_control_mode(AgEAvtrBasicManeuverGlideSpeedControlMode.eGlideSpeedAtAltitude, 2000)
        Assert.assertEqual(
            AgEAvtrBasicManeuverGlideSpeedControlMode.eGlideSpeedAtAltitude, glide.glide_speed_control_mode
        )
        Assert.assertEqual(2000, glide.glide_speed_control_alt)

        def action230():
            glide.set_glide_speed_control_mode(AgEAvtrBasicManeuverGlideSpeedControlMode.eGlideSpeedAtAltitude, -1000)

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action230)

        glide.min_g = 0.6
        Assert.assertEqual(0.6, glide.min_g)

        glide.max_g = 1.6
        Assert.assertEqual(1.6, glide.max_g)

        glide.max_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated, glide.max_speed_limits)
        glide.max_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated, glide.max_speed_limits)
        glide.max_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated, glide.max_speed_limits)
        glide.max_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated, glide.max_speed_limits)

        glide.compensate_for_coriolis_accel = False
        Assert.assertFalse(glide.compensate_for_coriolis_accel)
        glide.compensate_for_coriolis_accel = True
        Assert.assertTrue(glide.compensate_for_coriolis_accel)

        glide.powered_cruise_mode = AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyUnPoweredCruise
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyUnPoweredCruise, glide.powered_cruise_mode
        )

        glide.powered_cruise_throttle = 20.0
        thrust1: "IPropulsionThrust" = glide.powered_cruise_thrust_model
        # BUG120578 TryCatchAssertBlock.ExpectedException("read only", delegate () { glide.PoweredCruiseThrottle = 20.0; });
        # BUG120578 TryCatchAssertBlock.ExpectedException("read only", delegate () { IPropulsionThrust thrust1 = glide.PoweredCruiseThrustModel; });

        glide.powered_cruise_mode = AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyThrottle
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyThrottle, glide.powered_cruise_mode
        )

        glide.powered_cruise_throttle = 30.0
        Assert.assertEqual(30.0, glide.powered_cruise_throttle)

        self.Test_IAgAvtrPropulsionThrust(glide.powered_cruise_thrust_model)
        # BUG120578 TryCatchAssertBlock.ExpectedException("read only", delegate () { Test_IAgAvtrPropulsionThrust( glide.PoweredCruiseThrustModel); });

        glide.powered_cruise_mode = AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyThrustModel
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyThrustModel, glide.powered_cruise_mode
        )

        glide.powered_cruise_throttle = 20.0
        # BUG120578 TryCatchAssertBlock.ExpectedException("read only", delegate () { glide.PoweredCruiseThrottle = 20.0; });

        self.Test_IAgAvtrPropulsionThrust(glide.powered_cruise_thrust_model)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region Test_IAgAvtrPropulsionThrust
    def Test_IAgAvtrPropulsionThrust(self, thrust: "IPropulsionThrust"):
        thrust.use_constant_thrust = True
        Assert.assertTrue(thrust.use_constant_thrust)

        thrust.constant_thrust = 111
        Assert.assertEqual(111, thrust.constant_thrust)

        def action231():
            thrust.boost_thrust = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action231)

        def action232():
            thrust.boost_thrust_time_limit = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action232)

        def action233():
            thrust.sustain_thrust = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action233)

        def action234():
            thrust.sustain_thrust_time_limit = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action234)

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

        def action235():
            thrust.constant_thrust = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action235)

        thrust.set_min_airspeed(AgEAvtrAirspeedType.eMach, 666)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, thrust.min_airspeed_type)
        Assert.assertAlmostEqual(666, thrust.min_airspeed, delta=1e-06)
        thrust.set_min_airspeed(AgEAvtrAirspeedType.eEAS, 777)
        Assert.assertEqual(AgEAvtrAirspeedType.eEAS, thrust.min_airspeed_type)
        Assert.assertAlmostEqual(777, thrust.min_airspeed, delta=1e-06)

        thrust.set_max_airspeed(AgEAvtrAirspeedType.eCAS, 888)
        Assert.assertEqual(AgEAvtrAirspeedType.eCAS, thrust.max_airspeed_type)
        Assert.assertAlmostEqual(888, thrust.max_airspeed, delta=1e-06)
        thrust.set_max_airspeed(AgEAvtrAirspeedType.eTAS, 999)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, thrust.max_airspeed_type)
        Assert.assertAlmostEqual(999, thrust.max_airspeed, delta=1e-06)

    # endregion

    # region BasicManeuverIntercept
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverIntercept(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Intercept"
        intercept: "IBasicManeuverStrategyIntercept" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyIntercept
        )

        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name

        def action236():
            intercept.target_name = targetName

        TryCatchAssertBlock.ExpectedException("not a valid", action236)
        missile: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: "IVehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, IVehiclePropagatorBallistic)
        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, IVehicleImpactLocationPoint)
        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
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

        intercept.intercept_mode = AgEAvtrInterceptMode.eTargetAspect
        intercept.target_aspect = 0.1
        aspect: typing.Any = intercept.target_aspect
        Assert.assertEqual(0.1, float(aspect))

        def action237():
            intercept.lateral_separation = 2

        TryCatchAssertBlock.ExpectedException("must be", action237)

        intercept.intercept_mode = AgEAvtrInterceptMode.eLateralSeparation
        intercept.lateral_separation = 2
        Assert.assertEqual(2, intercept.lateral_separation)

        def action238():
            intercept.target_aspect = 2

        TryCatchAssertBlock.ExpectedException("must be", action238)

        intercept.maneuver_factor = 0.6
        Assert.assertEqual(0.6, intercept.maneuver_factor)

        intercept.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(
            intercept.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel
        )
        intercept.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(intercept.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, intercept.control_limit_horiz_accel, delta=tolerance)
        intercept.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(intercept.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(intercept.control_limit_turn_rate), delta=tolerance)
        intercept.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(intercept.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
        Assert.assertEqual(700, intercept.control_limit_turn_radius)

        intercept.closure_mode = AgEAvtrClosureMode.eClosureNotSet

        def action239():
            intercept.hobs_angle_tol = 2

        TryCatchAssertBlock.ExpectedException("must be", action239)

        def action240():
            intercept.hobs_max_angle = 5

        TryCatchAssertBlock.ExpectedException("must be", action240)

        intercept.closure_mode = AgEAvtrClosureMode.eHOBS
        intercept.hobs_angle_tol = 2
        intercept.hobs_max_angle = 5
        angleTol: typing.Any = intercept.hobs_angle_tol
        Assert.assertEqual(2, float(angleTol))
        maxAngle: typing.Any = intercept.hobs_max_angle
        Assert.assertEqual(5, float(maxAngle))

        intercept.compensate_for_coriolis_accel = True
        Assert.assertTrue(intercept.compensate_for_coriolis_accel)

        missileObj: "IStkObject" = clr.CastAs(missile, IStkObject)
        missileObj.unload()
        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverLoop
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverLoop(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Loop"
        loop: "IBasicManeuverStrategyLoop" = clr.CastAs(basicManeuver.navigation, IBasicManeuverStrategyLoop)
        loop.loop_angle = 359
        loopAngle: typing.Any = loop.loop_angle
        loop.loop_angle_mode = AgEAvtrAngleMode.eRelativeAngle
        Assert.assertEqual(359, float(loopAngle))
        Assert.assertEqual(AgEAvtrAngleMode.eRelativeAngle, loop.loop_angle_mode)

        Assert.assertEqual("Loop", basicManeuver.profile_strategy_type)
        loopProfile: "IBasicManeuverStrategyLoop" = clr.CastAs(basicManeuver.navigation, IBasicManeuverStrategyLoop)
        loopAngleProfile: typing.Any = loopProfile.loop_angle
        Assert.assertEqual(359, float(loopAngleProfile))
        Assert.assertEqual(AgEAvtrAngleMode.eRelativeAngle, loopProfile.loop_angle_mode)

        loop.hold_init_tas = True

        def action241():
            loop.set_airspeeds(AgEAvtrAirspeedType.eMach, 0.1, 0.2)

        TryCatchAssertBlock.ExpectedException("must be", action241)

        loop.hold_init_tas = False
        loop.set_airspeeds(AgEAvtrAirspeedType.eMach, 0.1, 0.2)
        Assert.assertEqual(0.1, loop.top_airspeed)
        Assert.assertEqual(0.2, loop.bottom_airspeed)

        loop.set_airspeeds(AgEAvtrAirspeedType.eTAS, 200, 201)
        Assert.assertEqual(200, loop.top_airspeed)
        Assert.assertEqual(201, loop.bottom_airspeed)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverLTAHover
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverLTAHover(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Lighter Than Air Hover"
        hover: "IBasicManeuverStrategyLTAHover" = clr.CastAs(basicManeuver.navigation, IBasicManeuverStrategyLTAHover)
        hover.heading_rate = 1.5
        headingRate: typing.Any = hover.heading_rate
        Assert.assertEqual(1.5, float(headingRate))

        Assert.assertEqual("Lighter Than Air Hover", basicManeuver.profile_strategy_type)
        hoverProfile: "IBasicManeuverStrategyLTAHover" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyLTAHover
        )
        headingRateProfile: typing.Any = hoverProfile.heading_rate
        Assert.assertEqual(1.5, float(headingRateProfile))

        hover.heading_mode = AgEAvtrHoverHeadingMode.eHoverIntoWind

        def action242():
            hover.absolute_heading = 1.1

        TryCatchAssertBlock.ExpectedException("must be", action242)

        def action243():
            hover.use_magnetic_heading = True

        TryCatchAssertBlock.ExpectedException("must be", action243)

        def action244():
            hover.relative_heading = 2.2

        TryCatchAssertBlock.ExpectedException("must be", action244)

        hover.heading_mode = AgEAvtrHoverHeadingMode.eHoverAbsolute
        hover.absolute_heading = 1.1
        absHdg: typing.Any = hover.absolute_heading
        Assert.assertEqual(1.1, float(absHdg))
        hover.use_magnetic_heading = True
        Assert.assertTrue(hover.use_magnetic_heading)

        hover.heading_mode = AgEAvtrHoverHeadingMode.eHoverRelative
        hover.relative_heading = 2.2
        relHdg: typing.Any = hover.relative_heading
        Assert.assertEqual(2.2, float(relHdg))

        hover.altitude_mode = AgEAvtrHoverAltitudeMode.eHoverHoldInitAltitude

        def action245():
            test: float = hover.absolute_altitude

        TryCatchAssertBlock.ExpectedException("must be", action245)

        def action246():
            hover.absolute_altitude = 10001

        TryCatchAssertBlock.ExpectedException("must be", action246)

        def action247():
            test: float = hover.altitude_rate

        TryCatchAssertBlock.ExpectedException("must be", action247)

        def action248():
            hover.altitude_rate = 1

        TryCatchAssertBlock.ExpectedException("must be", action248)

        def action249():
            test: float = hover.control_alt_rate

        TryCatchAssertBlock.ExpectedException("must be", action249)

        def action250():
            hover.control_alt_rate = 501

        TryCatchAssertBlock.ExpectedException("must be", action250)

        def action251():
            test: float = hover.relative_altitude_change

        TryCatchAssertBlock.ExpectedException("must be", action251)

        def action252():
            hover.relative_altitude_change = 1

        TryCatchAssertBlock.ExpectedException("must be", action252)

        def action253():
            test: float = hover.parachute_area

        TryCatchAssertBlock.ExpectedException("must be", action253)

        def action254():
            hover.parachute_area = 1

        TryCatchAssertBlock.ExpectedException("must be", action254)

        def action255():
            test: float = hover.parachute_cd

        TryCatchAssertBlock.ExpectedException("must be", action255)

        def action256():
            hover.parachute_cd = 1

        TryCatchAssertBlock.ExpectedException("must be", action256)

        hover.altitude_mode = AgEAvtrHoverAltitudeMode.eHoverSpecifyAltitude
        hover.absolute_altitude = 10001
        Assert.assertEqual(10001, hover.absolute_altitude)
        hover.control_alt_rate = 501
        Assert.assertEqual(501, hover.control_alt_rate)

        hover.altitude_mode = AgEAvtrHoverAltitudeMode.eHoverSpecifyAltitudeChange
        hover.relative_altitude_change = 1
        Assert.assertEqual(1, hover.relative_altitude_change)
        hover.control_alt_rate = 501
        Assert.assertEqual(501, hover.control_alt_rate)

        hover.altitude_mode = AgEAvtrHoverAltitudeMode.eHoverSpecifyAltitudeRate
        hover.altitude_rate = 501
        Assert.assertEqual(501, hover.altitude_rate)

        hover.altitude_mode = AgEAvtrHoverAltitudeMode.eHoverParachute
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Pitch3D"
        pitch3D: "IBasicManeuverStrategyPitch3D" = clr.CastAs(basicManeuver.navigation, IBasicManeuverStrategyPitch3D)

        pitch3D.control_mode = AgEAvtrPitch3DControlMode.ePitch3DWindPushesVehicle
        Assert.assertEqual(AgEAvtrPitch3DControlMode.ePitch3DWindPushesVehicle, pitch3D.control_mode)

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

        pitch3D.control_mode = AgEAvtrPitch3DControlMode.ePitch3DCompensateForWind
        Assert.assertEqual(AgEAvtrPitch3DControlMode.ePitch3DCompensateForWind, pitch3D.control_mode)

        def action257():
            pitch3D.wind_force_effective_area = 10

        TryCatchAssertBlock.ExpectedException("must be", action257)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverPull
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverPull(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Pull"
        pull: "IBasicManeuverStrategyPull" = clr.CastAs(basicManeuver.navigation, IBasicManeuverStrategyPull)

        pull.active_mode = AgEAvtrPullMode.ePullToAngle
        pull.active_angle = 59
        angle: typing.Any = pull.active_angle
        Assert.assertAlmostEqual(59, float(angle), delta=tolerance)

        Assert.assertEqual("Pull", basicManeuver.profile_strategy_type)
        pullProfile: "IBasicManeuverStrategyPull" = clr.CastAs(basicManeuver.profile, IBasicManeuverStrategyPull)
        angleProfile: typing.Any = pullProfile.active_angle
        Assert.assertAlmostEqual(59, float(angleProfile), delta=tolerance)

        pull.pull_g_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action258():
            pull.override_pull_g = 2

        TryCatchAssertBlock.ExpectedException("must be", action258)
        pull.pull_g_mode = AgEAvtrPerfModelOverride.eOverride
        pull.override_pull_g = 2
        Assert.assertEqual(2, pull.override_pull_g)

        airspeedOpts: "IBasicManeuverAirspeedOptions" = pull.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverPushPull
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverPushPull(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.profile_strategy_type = "Profile Segment - Push/Pull"
        pushPull: "IBasicManeuverStrategyPushPull" = clr.CastAs(basicManeuver.profile, IBasicManeuverStrategyPushPull)

        pushPull.reference_frame = AgEAvtrBasicManeuverRefFrame.eWindFrame
        Assert.assertEqual(AgEAvtrBasicManeuverRefFrame.eWindFrame, pushPull.reference_frame)

        pushPull.push_pull = AgEAvtrPushPull.ePushOver
        pushPull.push_pull_g = 0.99
        Assert.assertEqual(0.99, pushPull.push_pull_g)

        pushPull.accel_mode = AgEAvtrAccelMode.eAccel
        pushPull.accel_decel_g = 0.98
        Assert.assertEqual(0.98, pushPull.accel_decel_g)

        pushPull.stop_flight_path_angle = 5
        fpa: typing.Any = pushPull.stop_flight_path_angle
        Assert.assertEqual(5, float(fpa))

        pushPull.set_stop_airspeed(True, AgEAvtrAirspeedType.eTAS, 250)
        Assert.assertTrue(pushPull.use_stop_at_airspeed)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, pushPull.stop_airspeed_type)
        Assert.assertEqual(250, pushPull.stop_airspeed)

        pushPull.set_stop_airspeed(False, AgEAvtrAirspeedType.eMach, 0.2)
        Assert.assertEqual(False, pushPull.use_stop_at_airspeed)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, pushPull.stop_airspeed_type)
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Relative Bearing"
        relBearing: "IBasicManeuverStrategyRelativeBearing" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyRelativeBearing
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

        relBearing.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(
            relBearing.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel
        )
        relBearing.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(relBearing.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, relBearing.control_limit_horiz_accel, delta=tolerance)
        relBearing.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(relBearing.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(relBearing.control_limit_turn_rate), delta=tolerance)
        relBearing.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(relBearing.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Relative Course"
        relCourse: "IBasicManeuverStrategyRelativeCourse" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyRelativeCourse
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

        relCourse.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(
            relCourse.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel
        )
        relCourse.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(relCourse.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, relCourse.control_limit_horiz_accel, delta=tolerance)
        relCourse.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(relCourse.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(relCourse.control_limit_turn_rate), delta=tolerance)
        relCourse.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(relCourse.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
        Assert.assertEqual(700, relCourse.control_limit_turn_radius)

        relCourse.closure_mode = AgEAvtrClosureMode.eClosureNotSet

        def action259():
            relCourse.downrange_offset = 0.5

        TryCatchAssertBlock.ExpectedException("must be", action259)

        def action260():
            relCourse.hobs_max_angle = 89

        TryCatchAssertBlock.ExpectedException("must be", action260)

        def action261():
            relCourse.hobs_angle_tol = 4

        TryCatchAssertBlock.ExpectedException("must be", action261)

        relCourse.closure_mode = AgEAvtrClosureMode.eClosureRequired
        relCourse.downrange_offset = 0.5
        Assert.assertEqual(0.5, relCourse.downrange_offset)

        relCourse.closure_mode = AgEAvtrClosureMode.eHOBS
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Relative Course"
        relCourse: "IBasicManeuverStrategyRelativeCourse" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyRelativeCourse
        )

        validTargets = relCourse.valid_target_names
        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relCourse.target_name = targetName
        Assert.assertEqual(targetName, relCourse.target_name)

        basicManeuver.profile_strategy_type = "Relative Flight Path Angle"
        relativeFPA: "IBasicManeuverStrategyRelativeFPA" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategyRelativeFPA
        )

        relativeFPA.fpa = 5
        fpa: typing.Any = relativeFPA.fpa
        Assert.assertEqual(5, float(fpa))
        relativeFPA.anchor_alt_offset = 100
        Assert.assertEqual(100, relativeFPA.anchor_alt_offset)

        relativeFPA.maneuver_factor = 0.7
        Assert.assertEqual(0.7, relativeFPA.maneuver_factor)

        relativeFPA.set_control_limit(AgEAvtrProfileControlLimit.eProfilePitchRate, 5)
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

        airspeedOpts: "IBasicManeuverAirspeedOptions" = relativeFPA.airspeed_options
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Relative Course"
        relCourse: "IBasicManeuverStrategyRelativeCourse" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyRelativeCourse
        )

        validTargets = relCourse.valid_target_names
        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relCourse.target_name = targetName
        Assert.assertEqual(targetName, relCourse.target_name)

        basicManeuver.profile_strategy_type = "Relative Speed/Altitude"
        relSpeedAlt: "IBasicManeuverStrategyRelSpeedAltitude" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategyRelSpeedAltitude
        )

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        testAC: "IStkObject" = acObj.copy_object("LeaderAC")
        relSpeedAlt.target_name = "Aircraft/LeaderAC"
        Assert.assertEqual("Aircraft/LeaderAC", relSpeedAlt.target_name)
        Assert.assertEqual(targetName, relCourse.target_name)

        relSpeedAlt.target_resolution = 4
        Assert.assertEqual(4, relSpeedAlt.target_resolution)

        relSpeedAlt.relative_altitude_mode = AgEAvtrRelativeAltitudeMode.eHoldOffsetAlt
        relSpeedAlt.altitude_offset = 2
        Assert.assertEqual(2, relSpeedAlt.altitude_offset)

        def action262():
            relSpeedAlt.elevation_angle = 5

        TryCatchAssertBlock.ExpectedException("must be", action262)

        relSpeedAlt.relative_altitude_mode = AgEAvtrRelativeAltitudeMode.eHoldElevationAngle
        relSpeedAlt.elevation_angle = 5
        angle: typing.Any = relSpeedAlt.elevation_angle
        Assert.assertEqual(5, float(angle))

        def action263():
            relSpeedAlt.altitude_offset = 2

        TryCatchAssertBlock.ExpectedException("must be", action263)

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

        relSpeedAlt.set_airspeed_offset(AgEAvtrAirspeedType.eTAS, 5)
        Assert.assertEqual(5, relSpeedAlt.airspeed_offset)
        relSpeedAlt.set_airspeed_offset(AgEAvtrAirspeedType.eMach, 0.1)
        Assert.assertEqual(0.1, relSpeedAlt.airspeed_offset)

        relSpeedAlt.set_min_airspeed(AgEAvtrAirspeedType.eTAS, 100)
        Assert.assertEqual(100, relSpeedAlt.min_airspeed)
        relSpeedAlt.set_min_airspeed(AgEAvtrAirspeedType.eMach, 0.1)
        Assert.assertEqual(0.1, relSpeedAlt.min_airspeed)

        relSpeedAlt.set_max_airspeed(AgEAvtrAirspeedType.eTAS, 200)
        Assert.assertEqual(200, relSpeedAlt.max_airspeed)
        relSpeedAlt.set_max_airspeed(AgEAvtrAirspeedType.eMach, 0.2)
        Assert.assertEqual(0.2, relSpeedAlt.max_airspeed)

        relSpeedAlt.stop_condition = AgEAvtrRelSpeedAltStopCondition.eRelSpeedAltStopAfterTargetCurrentProcedure
        Assert.assertEqual(
            AgEAvtrRelSpeedAltStopCondition.eRelSpeedAltStopAfterTargetCurrentProcedure, relSpeedAlt.stop_condition
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        acObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        testAC: "IStkObject" = acObj.copy_object("LeaderAC")

        basicManeuver.navigation_strategy_type = "Rendezvous/Formation"
        formation: "IBasicManeuverStrategyRendezvous" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyRendezvous
        )

        targetName: str = (EarlyBoundTests.AG_Target.class_name + "/") + EarlyBoundTests.AG_Target.instance_name

        def action264():
            formation.target_name = targetName

        TryCatchAssertBlock.ExpectedException("not a valid", action264)

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

        def action265():
            formation.altitude_rate_control = 1000

        TryCatchAssertBlock.ExpectedException("must be", action265)

        def action266():
            formation.min_load_factor_g = -3

        TryCatchAssertBlock.ExpectedException("must be", action266)

        def action267():
            formation.max_load_factor_g = 3

        TryCatchAssertBlock.ExpectedException("must be", action267)

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

        formation.airspeed_control_mode = AgEAvtrAccelPerfModelOverride.eAccelPerfModelValue

        def action268():
            testVal: float = formation.accel_decel_g

        TryCatchAssertBlock.ExpectedException("must be", action268)

        def action269():
            formation.accel_decel_g = 0.1

        TryCatchAssertBlock.ExpectedException("must be", action269)
        formation.airspeed_control_mode = AgEAvtrAccelPerfModelOverride.eAccelOverride
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Rolling Pull"
        pull: "IBasicManeuverStrategyRollingPull" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyRollingPull
        )
        pull.active_mode = AgEAvtrRollingPullMode.ePullToAngleMode
        pull.angle = 10
        angle: typing.Any = pull.angle
        Assert.assertAlmostEqual(10, float(angle), delta=tolerance)

        Assert.assertEqual("Rolling Pull", basicManeuver.profile_strategy_type)
        pullProfile: "IBasicManeuverStrategyRollingPull" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategyRollingPull
        )
        angleProfile: typing.Any = pullProfile.angle
        Assert.assertAlmostEqual(10, float(angleProfile), delta=tolerance)

        def action270():
            pull.roll_orientation = AgEAvtrRollUprightInverted.eRollInverted

        TryCatchAssertBlock.ExpectedException("must be", action270)
        pull.active_mode = AgEAvtrRollingPullMode.eRollToOrientationMode
        pull.roll_orientation = AgEAvtrRollUprightInverted.eRollInverted
        Assert.assertEqual(AgEAvtrRollUprightInverted.eRollInverted, pull.roll_orientation)

        pull.roll_rate_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action271():
            testRate: typing.Any = pull.override_roll_rate

        TryCatchAssertBlock.ExpectedException("must be", action271)
        pull.roll_rate_mode = AgEAvtrPerfModelOverride.eOverride
        pull.override_roll_rate = 20
        overrideRollRate: typing.Any = pull.override_roll_rate
        Assert.assertEqual(20, float(overrideRollRate))

        pull.pull_g_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action272():
            pull.override_pull_g = 2

        TryCatchAssertBlock.ExpectedException("must be", action272)
        pull.pull_g_mode = AgEAvtrPerfModelOverride.eOverride
        pull.override_pull_g = 2
        Assert.assertEqual(2, pull.override_pull_g)

        airspeedOpts: "IBasicManeuverAirspeedOptions" = pull.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverSimpleTurn
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverSimpleTurn(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Simple Turn"
        simpleTurn: "IBasicManeuverStrategySimpleTurn" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategySimpleTurn
        )

        simpleTurn.reference_frame = AgEAvtrBasicManeuverRefFrame.eEarthFrame
        Assert.assertEqual(AgEAvtrBasicManeuverRefFrame.eEarthFrame, simpleTurn.reference_frame)

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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Smooth Accel"
        accel: "IBasicManeuverStrategySmoothAccel" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategySmoothAccel
        )
        accel.roll_rate_dot = 29
        rateDot: typing.Any = accel.roll_rate_dot
        Assert.assertAlmostEqual(29, float(rateDot), delta=tolerance)

        Assert.assertEqual("Smooth Accel", basicManeuver.profile_strategy_type)
        accelProfile: "IBasicManeuverStrategySmoothAccel" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategySmoothAccel
        )
        rateDotProfile: typing.Any = accelProfile.roll_rate_dot
        Assert.assertAlmostEqual(29, float(rateDotProfile), delta=tolerance)

        accel.turn_direction = AgEAvtrSmoothAccelLeftRight.eSmoothAccelLeft

        def action273():
            accel.pitch_angle = 89

        TryCatchAssertBlock.ExpectedException("must be", action273)

        def action274():
            accel.roll_angle = 89

        TryCatchAssertBlock.ExpectedException("must be", action274)

        def action275():
            accel.stop_on_pitch_angle = True

        TryCatchAssertBlock.ExpectedException("must be", action275)

        def action276():
            accel.stop_on_roll_angle = True

        TryCatchAssertBlock.ExpectedException("must be", action276)

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
        accel.turn_direction = AgEAvtrSmoothAccelLeftRight.eSmoothAccelNoRoll

        def action277():
            accel.roll_angle = 89

        TryCatchAssertBlock.ExpectedException("must be", action277)

        def action278():
            accel.control_roll_angle = False

        TryCatchAssertBlock.ExpectedException("must be", action278)
        accel.stop_on_roll_angle = True
        Assert.assertTrue(accel.stop_on_roll_angle)

        airspeedOpts: "IBasicManeuverAirspeedOptions" = accel.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverSmoothTurn
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverSmoothTurn(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Smooth Turn"
        turn: "IBasicManeuverStrategySmoothTurn" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategySmoothTurn
        )

        turn.heading_change = 89
        headingChange: typing.Any = turn.heading_change
        Assert.assertAlmostEqual(89, float(headingChange), delta=tolerance)

        Assert.assertEqual("Smooth Turn", basicManeuver.profile_strategy_type)
        turnProfile: "IBasicManeuverStrategySmoothTurn" = clr.CastAs(
            basicManeuver.profile, IBasicManeuverStrategySmoothTurn
        )
        headingChange = turnProfile.heading_change
        Assert.assertAlmostEqual(89, float(headingChange), delta=tolerance)

        turn.turn_mode = AgEAvtrSmoothTurnMode.eSmoothTurnLoadFactor

        def action279():
            turn.roll_angle = 5

        TryCatchAssertBlock.ExpectedException("must be", action279)
        turn.load_factor_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action280():
            turn.override_load_factor = 1

        TryCatchAssertBlock.ExpectedException("must be", action280)
        turn.load_factor_mode = AgEAvtrPerfModelOverride.eOverride
        turn.override_load_factor = 1
        Assert.assertEqual(1, turn.override_load_factor)

        turn.turn_mode = AgEAvtrSmoothTurnMode.eSmoothTurnRollAngle

        def action281():
            turn.load_factor_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        TryCatchAssertBlock.ExpectedException("must be", action281)
        turn.roll_rate_mode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action282():
            turn.override_roll_rate = 1

        TryCatchAssertBlock.ExpectedException("must be", action282)
        turn.roll_rate_mode = AgEAvtrPerfModelOverride.eOverride
        turn.override_roll_rate = 1
        overrideRollRate: typing.Any = turn.override_roll_rate
        Assert.assertEqual(1, float(overrideRollRate))

        turn.fpa_mode = AgEAvtrSmoothTurnFPAMode.eSmoothTurnFPALevelOff
        Assert.assertEqual(AgEAvtrSmoothTurnFPAMode.eSmoothTurnFPALevelOff, turn.fpa_mode)

        airspeedOpts: "IBasicManeuverAirspeedOptions" = turn.airspeed_options
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.remove(proc1)
        EarlyBoundTests.AG_Procedures.remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverStationkeeping
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverStationkeeping(self):
        tolerance: float = 1e-09

        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Stationkeeping"
        stationNav: "IBasicManeuverStrategyStationkeeping" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyStationkeeping
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

        stationNav.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(
            stationNav.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel
        )
        stationNav.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(stationNav.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, stationNav.control_limit_horiz_accel, delta=tolerance)
        stationNav.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(stationNav.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(stationNav.control_limit_turn_rate), delta=tolerance)
        stationNav.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(stationNav.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
        Assert.assertEqual(700, stationNav.control_limit_turn_radius)

        scenario: "IScenario" = clr.CastAs(EarlyBoundTests.AG_Scenario, IScenario)
        stationNav.stop_condition = AgEAvtrStationkeepingStopCondition.eStopConditionNotSet
        Assert.assertEqual(stationNav.stop_condition, AgEAvtrStationkeepingStopCondition.eStopConditionNotSet)

        def action283():
            testVal: float = stationNav.stop_after_duration

        TryCatchAssertBlock.ExpectedException("must be", action283)

        def action284():
            testVal: typing.Any = stationNav.stop_after_time

        TryCatchAssertBlock.ExpectedException("must be", action284)

        def action285():
            testVal: int = stationNav.stop_after_turn_count

        TryCatchAssertBlock.ExpectedException("must be", action285)

        def action286():
            stationNav.stop_after_duration = 2

        TryCatchAssertBlock.ExpectedException("must be", action286)

        def action287():
            stationNav.stop_after_time = scenario.stop_time

        TryCatchAssertBlock.ExpectedException("must be", action287)

        def action288():
            stationNav.stop_after_turn_count = 5

        TryCatchAssertBlock.ExpectedException("must be", action288)

        def action289():
            stationNav.stop_course = 2

        TryCatchAssertBlock.ExpectedException("must be", action289)

        def action290():
            stationNav.use_relative_course = True

        TryCatchAssertBlock.ExpectedException("must be", action290)

        stationNav.stop_condition = AgEAvtrStationkeepingStopCondition.eStopAfterTurnCount
        Assert.assertEqual(stationNav.stop_condition, AgEAvtrStationkeepingStopCondition.eStopAfterTurnCount)
        stationNav.stop_after_turn_count = 5
        Assert.assertEqual(5, stationNav.stop_after_turn_count)
        stationNav.use_relative_course = True
        stationNav.stop_course = 2
        course: typing.Any = stationNav.stop_course
        Assert.assertTrue(stationNav.use_relative_course)
        Assert.assertEqual(2, float(course))

        stationNav.stop_condition = AgEAvtrStationkeepingStopCondition.eStopAfterTime
        Assert.assertEqual(stationNav.stop_condition, AgEAvtrStationkeepingStopCondition.eStopAfterTime)
        stationNav.stop_after_time = scenario.stop_time
        time: typing.Any = stationNav.stop_after_time
        Assert.assertEqual(scenario.stop_time, time)

        stationNav.stop_condition = AgEAvtrStationkeepingStopCondition.eStopAfterDuration
        Assert.assertEqual(stationNav.stop_condition, AgEAvtrStationkeepingStopCondition.eStopAfterDuration)
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Straight Ahead"
        straightAhead: "IBasicManeuverStrategyStraightAhead" = clr.CastAs(
            basicManeuver.navigation, IBasicManeuverStrategyStraightAhead
        )

        straightAhead.reference_frame = AgEAvtrStraightAheadRefFrame.eMaintainCourse
        Assert.assertEqual(AgEAvtrStraightAheadRefFrame.eMaintainCourse, straightAhead.reference_frame)

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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        basicManeuver: "IProcedureBasicManeuver" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.navigation_strategy_type = "Weave"
        weave: "IBasicManeuverStrategyWeave" = clr.CastAs(basicManeuver.navigation, IBasicManeuverStrategyWeave)

        weave.heading_change = 45
        heading: typing.Any = weave.heading_change
        Assert.assertEqual(45, float(heading))
        weave.max_num_cycles = 3
        Assert.assertEqual(3, weave.max_num_cycles)
        weave.max_distance = 11
        Assert.assertEqual(11, weave.max_distance)

        weave.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(weave.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel)
        weave.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(weave.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, weave.control_limit_horiz_accel, delta=tolerance)
        weave.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(weave.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(weave.control_limit_turn_rate), delta=tolerance)
        weave.set_control_limit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(weave.control_limit_mode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
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

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eAreaTarget, "AreaTarget")
        place: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.ePlace, "Place")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        proc2: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRelativeToPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )
        relToPrevProc: "ISiteRelToPrevProcedure" = clr.CastAs(proc2.site, ISiteRelToPrevProcedure)

        self.TestSiteName(relToPrevProc.get_as_site(), "Relative to Previous Procedure")

        relToPrevProc.bearing_mode = AgEAvtrRelAbsBearing.eTrueBearing
        Assert.assertEqual(AgEAvtrRelAbsBearing.eTrueBearing, relToPrevProc.bearing_mode)
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

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eAreaTarget, "AreaTarget")
        place: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.ePlace, "Place")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRelativeToStationarySTKObject, AgEAvtrProcedureType.eProcEnroute
        )
        relToSTKObject: "ISiteRelToSTKObject" = clr.CastAs(proc1.site, ISiteRelToSTKObject)

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
            AgEAvtrSiteType.eSiteAirportFromCatalog, AgEAvtrProcedureType.eProcTakeoff
        )
        catAirport: "ISiteAirportFromCatalog" = clr.CastAs(proc1.site, ISiteAirportFromCatalog)

        arincAirports: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.airport_category.arinc424_airports
        arincSource: "ICatalogSource" = clr.CastAs(arincAirports, ICatalogSource)
        arincNames = arincSource.child_names
        firstArincAirport: "IARINC424Item" = arincAirports.get_arinc424_item(str(arincNames[0]))
        catAirport.set_catalog_airport(clr.CastAs(firstArincAirport, ICatalogAirport))
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
            AgEAvtrSiteType.eSiteNavaidFromCatalog, AgEAvtrProcedureType.eProcEnroute
        )
        catNavaid: "ISiteNavaidFromCatalog" = clr.CastAs(proc1.site, ISiteNavaidFromCatalog)

        arincNavaids: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.navaid_category.arinc424_navaids
        arincSource: "ICatalogSource" = clr.CastAs(arincNavaids, ICatalogSource)
        arincNames = arincSource.child_names
        firstArincNavaid: "IARINC424Item" = arincNavaids.get_arinc424_item(str(arincNames[0]))
        catNavaid.set_catalog_navaid(clr.CastAs(firstArincNavaid, ICatalogNavaid))
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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        runway: "ISiteRunway" = clr.CastAs(proc1.site, ISiteRunway)

        self.TestSiteName(runway.get_as_site(), "Runway")

        runway.latitude = 1
        lat: typing.Any = runway.latitude
        Assert.assertEqual(1, float(lat))
        runway.longitude = 2
        lon: typing.Any = runway.longitude
        Assert.assertEqual(2, float(lon))
        runway.altitude = 5
        Assert.assertEqual(5, runway.altitude)
        runway.altitude_ref = AgEAvtrAGLMSL.eAltMSL
        Assert.assertEqual(AgEAvtrAGLMSL.eAltMSL, runway.altitude_ref)

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
        catRunway: "IUserRunway" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways.get_user_runway("Runway")
        runway.copy_from_catalog(clr.CastAs(catRunway, ICatalogRunway))

        lat = runway.latitude
        Assert.assertEqual(1, float(lat))
        runway.longitude = 2
        lon = runway.longitude
        Assert.assertEqual(2, float(lon))
        runway.altitude = 5
        Assert.assertEqual(5, runway.altitude)

        def action291():
            runway.add_to_catalog(False)

        TryCatchAssertBlock.ExpectedException("", action291)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region SiteWaypoint
    @category("Site Tests")
    def test_SiteWaypoint(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteWaypoint, AgEAvtrProcedureType.eProcEnroute
        )
        waypoint: "ISiteWaypoint" = clr.CastAs(proc1.site, ISiteWaypoint)

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
            AgEAvtrSiteType.eSiteReferenceState, AgEAvtrProcedureType.eProcReferenceState
        )
        refStateSite: "ISiteReferenceState" = clr.CastAs(proc1.site, ISiteReferenceState)

        self.TestSiteName(refStateSite.get_as_site(), "Reference State Site")

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region STKAreaTarget
    @category("Site Tests")
    def test_STKAreaTarget(self):
        self.EmptyProcedures()

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eAreaTarget, "AreaTarget")
        areaTarget2: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(
            AgESTKObjectType.eAreaTarget, "AreaTarget2"
        )

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteSTKAreaTarget, AgEAvtrProcedureType.eProcAreaTargetSearch
        )
        atSite: "ISiteSTKAreaTarget" = clr.CastAs(proc1.site, ISiteSTKAreaTarget)

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

        missile: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: "IVehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, IVehiclePropagatorBallistic)
        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, IVehicleImpactLocationPoint)
        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()

        missile2: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile2")), IMissile
        )
        traj2: "IVehiclePropagatorBallistic" = clr.CastAs(missile2.trajectory, IVehiclePropagatorBallistic)
        impactLocation2: "IVehicleImpactLocationPoint" = clr.CastAs(traj2.impact_location, IVehicleImpactLocationPoint)
        impact2: "IVehicleImpactLLA" = clr.CastAs(impactLocation2.impact, IVehicleImpactLLA)
        impact2.lat = -20
        impact2.lon = -20
        traj2.propagate()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteDynState, AgEAvtrProcedureType.eProcLaunchDynState
        )
        dynState: "ISiteDynState" = clr.CastAs(proc1.site, ISiteDynState)

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

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eAreaTarget, "AreaTarget")
        place: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.ePlace, "Place")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteSTKObjectWaypoint, AgEAvtrProcedureType.eProcEnroute
        )
        objectWaypointSite: "ISiteSTKObjectWaypoint" = clr.CastAs(proc1.site, ISiteSTKObjectWaypoint)

        self.TestSiteName(objectWaypointSite.get_as_site(), "STK Object Waypoint Site")

        objectWaypointSite.object_name = "Place/Place"
        name: typing.Any = objectWaypointSite.object_name
        Assert.assertTrue(("Place/Place" == str(name)))

        names = objectWaypointSite.valid_object_names
        Assert.assertTrue((Array.Length(names) >= 2))

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        scenario: "IScenario" = clr.CastAs(EarlyBoundTests.AG_Scenario, IScenario)

        objectWaypointSite.minimize_site_proc_time_diff = AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceOff
        Assert.assertEqual(
            AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceOff, objectWaypointSite.minimize_site_proc_time_diff
        )

        minTime: typing.Any = objectWaypointSite.min_time
        Assert.assertTrue(("Unlimited" == str(minTime)))
        maxTime: typing.Any = objectWaypointSite.max_time
        Assert.assertTrue(("Unlimited" == str(maxTime)))

        objectWaypointSite.waypoint_time = 30
        Assert.assertEqual(30, objectWaypointSite.waypoint_time)

        objectWaypointSite.minimize_site_proc_time_diff = (
            AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceNextUpdate
        )
        Assert.assertEqual(
            AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceNextUpdate,
            objectWaypointSite.minimize_site_proc_time_diff,
        )
        objectWaypointSite.minimize_site_proc_time_diff = AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceAlways
        Assert.assertEqual(
            AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceAlways,
            objectWaypointSite.minimize_site_proc_time_diff,
        )

        def action292():
            objectWaypointSite.waypoint_time = 5

        TryCatchAssertBlock.ExpectedException("must be", action292)

        objectWaypointSite.offset_mode = AgEAvtrSTKObjectWaypointOffsetMode.eOffsetNone
        Assert.assertEqual(AgEAvtrSTKObjectWaypointOffsetMode.eOffsetNone, objectWaypointSite.offset_mode)

        def action293():
            objectWaypointSite.bearing = 1

        TryCatchAssertBlock.ExpectedException("must be", action293)

        def action294():
            objectWaypointSite.use_magnetic_bearing = True

        TryCatchAssertBlock.ExpectedException("must be", action294)

        def action295():
            objectWaypointSite.range = 10

        TryCatchAssertBlock.ExpectedException("must be", action295)

        def action296():
            objectWaypointSite.vgt_point = "SubPoint(Detic)"

        TryCatchAssertBlock.ExpectedException("must be", action296)

        objectWaypointSite.offset_mode = AgEAvtrSTKObjectWaypointOffsetMode.eOffsetBearingRange
        Assert.assertEqual(AgEAvtrSTKObjectWaypointOffsetMode.eOffsetBearingRange, objectWaypointSite.offset_mode)
        objectWaypointSite.bearing = 1
        Assert.assertEqual(1, objectWaypointSite.bearing)
        objectWaypointSite.use_magnetic_bearing = True
        Assert.assertTrue(objectWaypointSite.use_magnetic_bearing)
        objectWaypointSite.range = 10
        Assert.assertEqual(10, objectWaypointSite.range)

        objectWaypointSite.offset_mode = AgEAvtrSTKObjectWaypointOffsetMode.eOffsetRelativeBearingRange
        Assert.assertEqual(
            AgEAvtrSTKObjectWaypointOffsetMode.eOffsetRelativeBearingRange, objectWaypointSite.offset_mode
        )
        objectWaypointSite.bearing = 1
        Assert.assertEqual(1, objectWaypointSite.bearing)
        objectWaypointSite.range = 10
        Assert.assertEqual(10, objectWaypointSite.range)

        def action297():
            objectWaypointSite.use_magnetic_bearing = True

        TryCatchAssertBlock.ExpectedException("must be", action297)

        objectWaypointSite.offset_mode = AgEAvtrSTKObjectWaypointOffsetMode.eOffsetVGTPoint
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

        areaTarget: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eAreaTarget, "AreaTarget")
        place: "IStkObject" = EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.ePlace, "Place")

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteSTKStaticObject, AgEAvtrProcedureType.eProcEnroute
        )
        staticObjectSite: "ISiteSTKStaticObject" = clr.CastAs(proc1.site, ISiteSTKStaticObject)

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

        missile: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: "IVehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, IVehiclePropagatorBallistic)
        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(traj.impact_location, IVehicleImpactLocationPoint)
        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        traj.propagate()

        missile2: "IMissile" = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.children.new(AgESTKObjectType.eMissile, "Missile2")), IMissile
        )
        traj2: "IVehiclePropagatorBallistic" = clr.CastAs(missile2.trajectory, IVehiclePropagatorBallistic)
        impactLocation2: "IVehicleImpactLocationPoint" = clr.CastAs(traj2.impact_location, IVehicleImpactLocationPoint)
        impact2: "IVehicleImpactLLA" = clr.CastAs(impactLocation2.impact, IVehicleImpactLLA)
        impact2.lat = -20
        impact2.lon = -20
        traj2.propagate()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcLaunch
        )
        stkVehicleSite: "ISiteSTKVehicle" = clr.CastAs(proc1.site, ISiteSTKVehicle)

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

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        superProc: "IProcedureSuperProcedure" = clr.CastAs(
            EarlyBoundTests.AG_Procedures.add(
                AgEAvtrSiteType.eSiteSuperProcedure, AgEAvtrProcedureType.eProcSuperProcedure
            ),
            IProcedureSuperProcedure,
        )

        self.TestProcedureName(superProc.get_as_procedure(), "Super Procedure")

        Assert.assertEqual(False, EarlyBoundTests.AG_Mission.is_valid)

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.flightprocs")

        def action298():
            superProc.load_procedures_from_file(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("", action298)

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
            AgEAvtrSiteType.eSiteSuperProcedure, AgEAvtrProcedureType.eProcSuperProcedure
        )
        superProcSite: "ISiteSuperProcedure" = clr.CastAs(proc1.site, ISiteSuperProcedure)

        self.TestSiteName(superProcSite.get_as_site(), "Super Procedure Site")

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region SiteVTOLPoint
    @category("Site Tests")
    def test_SiteVTOLPoint(self):
        self.EmptyProcedures()

        proc1: "IProcedure" = EarlyBoundTests.AG_Procedures.add(
            AgEAvtrSiteType.eSiteVTOLPoint, AgEAvtrProcedureType.eProcVerticalTakeoff
        )
        vtolSite: "ISiteVTOLPoint" = clr.CastAs(proc1.site, ISiteVTOLPoint)

        vtolSite.latitude = 1
        lat: typing.Any = vtolSite.latitude
        Assert.assertEqual(1, float(lat))
        vtolSite.longitude = 2
        lon: typing.Any = vtolSite.longitude
        Assert.assertEqual(2, float(lon))
        vtolSite.altitude = 101
        Assert.assertEqual(101, vtolSite.altitude)
        vtolSite.altitude_reference = AgEAvtrAGLMSL.eAltAGL
        Assert.assertEqual(AgEAvtrAGLMSL.eAltAGL, vtolSite.altitude_reference)

        EarlyBoundTests.AG_Procedures.remove(proc1)

    # endregion

    # region ReadOnlyCatalogItem
    @category("Aircraft Tests")
    def test_ReadOnlyCatalogItem(self):
        basicAirliner: "IAircraftModel" = EarlyBoundTests.AG_AvtrAircraftModels.get_aircraft("Basic Airliner")
        acAsCatalogItem: "ICatalogItem" = basicAirliner.get_as_catalog_item()
        Assert.assertEqual("Basic Airliner", acAsCatalogItem.name)

        def action299():
            acAsCatalogItem.name = ""

        TryCatchAssertBlock.ExpectedException("read-only", action299)

        Assert.assertEqual("Basic Airliner", acAsCatalogItem.name)

        isReadOnly: bool = acAsCatalogItem.is_read_only
        Assert.assertTrue(isReadOnly)

        def action300():
            acAsCatalogItem.remove()

        TryCatchAssertBlock.ExpectedException("read-only", action300)

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

        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

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
        tempAC.acceleration.get_adv_acceleration_by_name("CreateAllPerfModelsTest")
        tempAC.climb.get_adv_climb_by_name("CreateAllPerfModelsTest")
        tempAC.cruise.get_adv_cruise_by_name("CreateAllPerfModelsTest")
        tempAC.descent.get_adv_descent_by_name("CreateAllPerfModelsTest")
        tempAC.takeoff.get_adv_takeoff_by_name("CreateAllPerfModelsTest")
        tempAC.landing.get_adv_landing_by_name("CreateAllPerfModelsTest")

        def action301():
            advFWT.create_all_perf_models("CreateAllPerfModelsTest", False, False)

        TryCatchAssertBlock.ExpectedException("already exist", action301)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingExternalAero
    @category("Aircraft Tests")
    def test_AdvFixedWingExternalAero(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.aero_strategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero

        def action302():
            aeroTest: "IAdvFixedWingExternalAero" = advFWT.aero_mode_as_external

        TryCatchAssertBlock.ExpectedException("must be", action302)

        advFWT.aero_strategy = AgEAvtrAdvFixedWingAeroStrategy.eExternalAeroFile
        aero: "IAdvFixedWingExternalAero" = advFWT.aero_mode_as_external

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.aero")

        def action303():
            aero.set_filepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action303)

        filepath: str = TestBase.GetScenarioFile("advAero.aero")
        returnMsg: str = aero.set_filepath(filepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertTrue(aero.is_valid)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingSubSuperHypersonicAero
    @category("Aircraft Tests")
    def test_AdvFixedWingSubSuperHypersonicAero(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.aero_strategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero

        def action304():
            aeroTest: "IAdvFixedWingSubSuperHypersonicAero" = advFWT.aero_mode_as_sub_super_hypersonic

        TryCatchAssertBlock.ExpectedException("must be", action304)

        advFWT.aero_strategy = AgEAvtrAdvFixedWingAeroStrategy.eSubSuperHyperAero
        Assert.assertEqual(AgEAvtrAdvFixedWingAeroStrategy.eSubSuperHyperAero, advFWT.aero_strategy)
        aero: "IAdvFixedWingSubSuperHypersonicAero" = advFWT.aero_mode_as_sub_super_hypersonic

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
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.aero_strategy = AgEAvtrAdvFixedWingAeroStrategy.eSupersonicAero

        def action305():
            aeroTest: "IAdvFixedWingSubsonicAero" = advFWT.aero_mode_as_subsonic

        TryCatchAssertBlock.ExpectedException("must be", action305)

        advFWT.aero_strategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero
        Assert.assertEqual(AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero, advFWT.aero_strategy)
        aero: "IAdvFixedWingSubsonicAero" = advFWT.aero_mode_as_subsonic

        aero.geometry_type = AgEAvtrAdvFixedWingGeometry.eVariableGeometry

        def action306():
            basicGeoTest: "IAdvFixedWingGeometryBasic" = aero.geometry_mode_as_basic

        TryCatchAssertBlock.ExpectedException("must be", action306)
        aero.geometry_type = AgEAvtrAdvFixedWingGeometry.eBasicGeometry
        basicGeo: "IAdvFixedWingGeometryBasic" = aero.geometry_mode_as_basic

        basicGeo.set_aspect_ratio(11)
        Assert.assertEqual(11, basicGeo.aspect_ratio)
        basicGeo.wing_sweep = 22
        sweep: typing.Any = basicGeo.wing_sweep
        Assert.assertEqual(22, float(sweep))

        def action307():
            variableGeoTest: "IAdvFixedWingGeometryVariable" = aero.geometry_mode_as_variable

        TryCatchAssertBlock.ExpectedException("must be", action307)
        aero.geometry_type = AgEAvtrAdvFixedWingGeometry.eVariableGeometry
        variableGeo: "IAdvFixedWingGeometryVariable" = aero.geometry_mode_as_variable

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
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.aero_strategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero

        def action308():
            aeroTest: "IAdvFixedWingSupersonicAero" = advFWT.aero_mode_as_supersonic

        TryCatchAssertBlock.ExpectedException("must be", action308)

        advFWT.aero_strategy = AgEAvtrAdvFixedWingAeroStrategy.eSupersonicAero
        Assert.assertEqual(AgEAvtrAdvFixedWingAeroStrategy.eSupersonicAero, advFWT.aero_strategy)
        aero: "IAdvFixedWingSupersonicAero" = advFWT.aero_mode_as_supersonic

        aero.geometry_type = AgEAvtrAdvFixedWingGeometry.eVariableGeometry

        def action309():
            basicGeoTest: "IAdvFixedWingGeometryBasic" = aero.geometry_mode_as_basic

        TryCatchAssertBlock.ExpectedException("must be", action309)
        aero.geometry_type = AgEAvtrAdvFixedWingGeometry.eBasicGeometry
        basicGeo: "IAdvFixedWingGeometryBasic" = aero.geometry_mode_as_basic

        basicGeo.set_aspect_ratio(11)
        Assert.assertEqual(11, basicGeo.aspect_ratio)
        basicGeo.wing_sweep = 22
        sweep: typing.Any = basicGeo.wing_sweep
        Assert.assertEqual(22, float(sweep))

        def action310():
            variableGeoTest: "IAdvFixedWingGeometryVariable" = aero.geometry_mode_as_variable

        TryCatchAssertBlock.ExpectedException("must be", action310)
        aero.geometry_type = AgEAvtrAdvFixedWingGeometry.eVariableGeometry
        variableGeo: "IAdvFixedWingGeometryVariable" = aero.geometry_mode_as_variable

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
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action311():
            propTest: "IAdvFixedWingElectricPowerplant" = advFWT.powerplant_mode_as_electric

        TryCatchAssertBlock.ExpectedException("must be", action311)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eElectricPowerplant
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eElectricPowerplant, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingElectricPowerplant" = advFWT.powerplant_mode_as_electric

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
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eElectricPowerplant

        def action312():
            propTest: "IAdvFixedWingExternalProp" = advFWT.powerplant_mode_as_external

        TryCatchAssertBlock.ExpectedException("must be", action312)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingExternalProp" = advFWT.powerplant_mode_as_external

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.prop")

        def action313():
            prop.set_filepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action313)

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

        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action314():
            propTest: "IAdvFixedWingPistonPowerplant" = advFWT.powerplant_mode_as_piston

        TryCatchAssertBlock.ExpectedException("must be", action314)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.ePistonPowerplant
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.ePistonPowerplant, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingPistonPowerplant" = advFWT.powerplant_mode_as_piston

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

        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action315():
            propTest: "IAdvFixedWingTurbopropPowerplant" = advFWT.powerplant_mode_as_turboprop

        TryCatchAssertBlock.ExpectedException("must be", action315)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurboprop
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurboprop, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingTurbopropPowerplant" = advFWT.powerplant_mode_as_turboprop

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
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action316():
            propTest: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        TryCatchAssertBlock.ExpectedException("must be", action316)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanHighBypass
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanHighBypass, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanLowBypassPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanLowBypassPowerplant(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action317():
            propTest: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        TryCatchAssertBlock.ExpectedException("must be", action317)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanLowBypass
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanLowBypass, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanLowBypassAfterburningPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanLowBypassAfterburningPowerplant(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action318():
            propTest: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        TryCatchAssertBlock.ExpectedException("must be", action318)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanLowBypassAfterburning
        Assert.assertEqual(
            AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanLowBypassAfterburning, advFWT.powerplant_strategy
        )
        prop: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanTurbojetPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanTurbojetPowerplant(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action319():
            propTest: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        TryCatchAssertBlock.ExpectedException("must be", action319)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojet
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojet, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanTurbojetAfterburningPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanTurbojetAfterburningPowerplant(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action320():
            propTest: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        TryCatchAssertBlock.ExpectedException("must be", action320)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojetAfterburning
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojetAfterburning, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingEmpiricalJetEngine" = advFWT.powerplant_mode_as_empirical_jet_engine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbojetBasicABProp
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbojetBasicABProp(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action321():
            propTest: "IAdvFixedWingTurbojetBasicABProp" = advFWT.powerplant_mode_as_basic_turbojet

        TryCatchAssertBlock.ExpectedException("must be", action321)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojetBasicAB
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojetBasicAB, advFWT.powerplant_strategy)
        self.TestTurbojetBasicAB(advFWT.powerplant_mode_as_basic_turbojet)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingTurbofanBasicABProp
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanBasicABProp(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action322():
            propTest: "IAdvFixedWingTurbofanBasicABProp" = advFWT.powerplant_mode_as_basic_turbofan

        TryCatchAssertBlock.ExpectedException("must be", action322)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanBasicAB
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanBasicAB, advFWT.powerplant_strategy)
        self.TestTurbofanBasicAB(advFWT.powerplant_mode_as_basic_turbofan)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region AdvFixedWingSubSuperHypersonicProp
    @category("Aircraft Tests")
    def test_AdvFixedWingSubSuperHypersonicProp(self):
        tempAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        advFWT: "IAdvFixedWingTool" = tempAC.adv_fixed_wing_tool

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action323():
            propTest: "IAdvFixedWingSubSuperHypersonicProp" = advFWT.powerplant_mode_as_sub_super_hypersonic

        TryCatchAssertBlock.ExpectedException("must be", action323)

        advFWT.powerplant_strategy = AgEAvtrAdvFixedWingPowerplantStrategy.eSubSuperHyperPowerplant
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eSubSuperHyperPowerplant, advFWT.powerplant_strategy)
        prop: "IAdvFixedWingSubSuperHypersonicProp" = advFWT.powerplant_mode_as_sub_super_hypersonic

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

        prop.turbine_mode = AgEAvtrTurbineMode.eTurbineModeDisabled
        Assert.assertEqual(AgEAvtrTurbineMode.eTurbineModeDisabled, prop.turbine_mode)

        def action324():
            fanTest: "IAdvFixedWingTurbofanBasicABProp" = prop.turbine_mode_as_turbofan

        TryCatchAssertBlock.ExpectedException("must be", action324)
        prop.ramjet_mode = AgEAvtrRamjetMode.eRamjetModeDisabled
        Assert.assertEqual(AgEAvtrRamjetMode.eRamjetModeDisabled, prop.ramjet_mode)

        def action325():
            ramTest: "IAdvFixedWingRamjetBasic" = prop.ramjet_mode_as_basic

        TryCatchAssertBlock.ExpectedException("must be", action325)
        prop.scramjet_mode = AgEAvtrScramjetMode.eScramjetModeDisabled
        Assert.assertEqual(AgEAvtrScramjetMode.eScramjetModeDisabled, prop.scramjet_mode)

        def action326():
            scramTest: "IAdvFixedWingScramjetBasic" = prop.scramjet_mode_as_basic

        TryCatchAssertBlock.ExpectedException("must be", action326)

        # /////////////////// Now test the turbojet turbine ////////////
        prop.turbine_mode = AgEAvtrTurbineMode.eTurbineModeTurbojetBasicAB
        turbojet: "IAdvFixedWingTurbojetBasicABProp" = prop.turbine_mode_as_turbojet
        self.TestTurbojetBasicAB(turbojet)
        prop.max_turbine_compression_temp = 901
        Assert.assertEqual(901, turbojet.max_compression_temp)
        prop.max_turbine_burner_temp = 1701
        Assert.assertEqual(1701, turbojet.max_burner_temp)

        # /////////////////// Now test the turbofan turbine ////////////
        prop.turbine_mode = AgEAvtrTurbineMode.eTurbineModeTurbofanBasicAB
        turbofan: "IAdvFixedWingTurbofanBasicABProp" = prop.turbine_mode_as_turbofan
        self.TestTurbofanBasicAB(turbofan)
        prop.max_turbine_compression_temp = 901
        Assert.assertEqual(901, turbofan.max_compression_temp)
        prop.max_turbine_burner_temp = 1701
        Assert.assertEqual(1701, turbofan.max_burner_temp)

        # /////////////////// Now test the ramjet /////////////////////
        prop.ramjet_mode = AgEAvtrRamjetMode.eRamjetModeBasic
        ramjet: "IAdvFixedWingRamjetBasic" = prop.ramjet_mode_as_basic

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

        ramjet.fuel_type = AgEAvtrJetFuelType.eKeroseneAFPROP
        self.TestFuelAFPROP(ramjet.fuel_mode_as_afprop)
        ramjet.fuel_type = AgEAvtrJetFuelType.eKeroseneCEA
        self.TestFuelCEA(ramjet.fuel_mode_as_cea)

        ramjet.fuel_type = AgEAvtrJetFuelType.eHydrogen
        Assert.assertEqual(AgEAvtrJetFuelType.eHydrogen, ramjet.fuel_type)

        def action327():
            afprop: "IFuelModelKeroseneAFPROP" = ramjet.fuel_mode_as_afprop

        TryCatchAssertBlock.ExpectedException("must be", action327)

        def action328():
            cea: "IFuelModelKeroseneCEA" = ramjet.fuel_mode_as_cea

        TryCatchAssertBlock.ExpectedException("must be", action328)

        self.TestPropulsionEfficienciesRamScram(ramjet.efficiencies_and_losses)

        # /////////////////// Now test the scramjet /////////////////////
        prop.scramjet_mode = AgEAvtrScramjetMode.eScramjetModeBasic
        scramjet: "IAdvFixedWingScramjetBasic" = prop.scramjet_mode_as_basic

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

        scramjet.fuel_type = AgEAvtrJetFuelType.eKeroseneAFPROP
        self.TestFuelAFPROP(scramjet.fuel_mode_as_afprop)
        scramjet.fuel_type = AgEAvtrJetFuelType.eKeroseneCEA
        self.TestFuelCEA(scramjet.fuel_mode_as_cea)

        scramjet.fuel_type = AgEAvtrJetFuelType.eHydrogen
        Assert.assertEqual(AgEAvtrJetFuelType.eHydrogen, scramjet.fuel_type)

        def action329():
            afprop: "IFuelModelKeroseneAFPROP" = scramjet.fuel_mode_as_afprop

        TryCatchAssertBlock.ExpectedException("must be", action329)

        def action330():
            cea: "IFuelModelKeroseneCEA" = scramjet.fuel_mode_as_cea

        TryCatchAssertBlock.ExpectedException("must be", action330)

        self.TestPropulsionEfficienciesRamScram(scramjet.efficiencies_and_losses)

        tempAC.get_as_catalog_item().remove()

    # endregion

    # region PerformanceModelCategory
    @category("Aircraft Tests")
    def test_PerformanceModelCategory(self):
        acc: "IAircraftAcceleration" = EarlyBoundTests.AG_AvtrAircraft.acceleration
        accAsCI: "ICatalogItem" = acc.get_as_catalog_item()

        Assert.assertEqual("Acceleration", accAsCI.name)

        def action331():
            accAsCI.name = ""

        TryCatchAssertBlock.ExpectedException("read-only", action331)
        Assert.assertEqual("Acceleration", accAsCI.name)

        isReadOnly: bool = accAsCI.is_read_only
        Assert.assertTrue(isReadOnly)

        def action332():
            accAsCI.remove()

        TryCatchAssertBlock.ExpectedException("read-only", action332)

        def action333():
            accAsCI.duplicate()

        TryCatchAssertBlock.ExpectedException("", action333)

    # endregion

    # region BuiltInPerformanceModel
    @category("Aircraft Tests")
    def test_BuiltInPerformanceModel(self):
        acc: "IAircraftAcceleration" = EarlyBoundTests.AG_AvtrAircraft.acceleration
        builtInAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()
        accAsCatalogItem: "ICatalogItem" = clr.CastAs(builtInAcc, ICatalogItem)

        Assert.assertEqual("Built-In Model", accAsCatalogItem.name)

        def action334():
            accAsCatalogItem.name = ""

        TryCatchAssertBlock.DoAssert2(action334)

        Assert.assertEqual("Built-In Model", accAsCatalogItem.name)

        isReadOnly: bool = accAsCatalogItem.is_read_only
        Assert.assertFalse(isReadOnly)

        def action335():
            accAsCatalogItem.remove()

        TryCatchAssertBlock.DoAssert2(action335)

    # endregion

    # region BasicAccelerationModel
    @category("Aircraft Tests")
    def test_BasicAccelerationModel(self):
        acc: "IAircraftAcceleration" = EarlyBoundTests.AG_AvtrAircraft.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        levelTurns: "ILevelTurns" = basicAcc.level_turns
        levelTurns.maneuver_mode = AgEAvtrAccelManeuverMode.eAccelManeuverModeNormal

        def action336():
            testVal: "IAeroPropManeuverModeHelper" = levelTurns.maneuver_mode_helper

        TryCatchAssertBlock.ExpectedException("must be set", action336)
        levelTurns.maneuver_mode = AgEAvtrAccelManeuverMode.eAccelManeuverModeDensityScale

        def action337():
            testVal: "IAeroPropManeuverModeHelper" = levelTurns.maneuver_mode_helper

        TryCatchAssertBlock.ExpectedException("must be set", action337)

        climbDescent: "IClimbAndDescentTransitions" = basicAcc.climb_and_descent_transitions
        climbDescent.maneuver_mode = AgEAvtrAccelManeuverMode.eAccelManeuverModeNormal

        def action338():
            testVal: "IAeroPropManeuverModeHelper" = climbDescent.maneuver_mode_helper

        TryCatchAssertBlock.ExpectedException("must be set", action338)
        climbDescent.maneuver_mode = AgEAvtrAccelManeuverMode.eAccelManeuverModeDensityScale

        def action339():
            testVal: "IAeroPropManeuverModeHelper" = climbDescent.maneuver_mode_helper

        TryCatchAssertBlock.ExpectedException("must be set", action339)

    # endregion

    # region BasicAccelerationAero
    @category("Aircraft Tests")
    def test_BasicAccelerationAero(self):
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "IAircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroSimple
        Assert.assertEqual(AgEAvtrAircraftAeroStrategy.eAircraftAeroSimple, aero.aero_strategy)

        aero.lift_factor = 1.2
        Assert.assertEqual(1.2, aero.lift_factor)
        aero.drag_factor = 1.3
        Assert.assertEqual(1.3, aero.drag_factor)
        Assert.assertEqual(1.2, aero.lift_factor)

        aero.aero_strategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroAdvancedMissile

        def action340():
            aero.lift_factor = 1.2

        TryCatchAssertBlock.ExpectedException("", action340)

        def action341():
            aero.drag_factor = 1.3

        TryCatchAssertBlock.ExpectedException("", action341)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationSimpleAero
    @category("Aircraft Tests")
    def test_BasicAccelerationSimpleAero(self):
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "IAircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroSimple

        simpleAero: "IAircraftSimpleAero" = aero.mode_as_simple
        simpleAero.operating_mode = AgEAvtrAeroPropSimpleMode.eHelicopter
        Assert.assertEqual(AgEAvtrAeroPropSimpleMode.eHelicopter, simpleAero.operating_mode)

        simpleAero.s_ref = 5
        Assert.assertEqual(5, simpleAero.s_ref)
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

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "IAircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroBasicFixedWing

        bfwAero: "IAircraftBasicFixedWingAero" = aero.mode_as_basic_fixed_wing

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
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "IAircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroExternalFile

        externalAero: "IAircraftExternalAero" = aero.mode_as_external
        Assert.assertIs(None, externalAero.forward_flight_filepath)
        Assert.assertIs(None, externalAero.takeoff_landing_filepath)

        def action342():
            externalAero.set_forward_flight_filepath("")

        TryCatchAssertBlock.ExpectedException("", action342)

        def action343():
            externalAero.set_takeoff_landing_filepath("")

        TryCatchAssertBlock.ExpectedException("", action343)

        def action344():
            externalAero.reload_forward_flight_file()

        TryCatchAssertBlock.ExpectedException("", action344)

        def action345():
            externalAero.reload_takeoff_landing_file()

        TryCatchAssertBlock.ExpectedException("", action345)
        Assert.assertEqual(False, externalAero.is_forward_flight_valid)
        Assert.assertEqual(False, externalAero.is_takeoff_landing_valid)

        Assert.assertTrue(externalAero.can_set_forward_flight_ref_area)
        externalAero.forward_flight_ref_area = 0.05
        Assert.assertEqual(0.05, externalAero.forward_flight_ref_area)
        Assert.assertTrue(externalAero.can_set_takeoff_landing_ref_area)
        externalAero.takeoff_landing_ref_area = 0.07
        Assert.assertEqual(0.07, externalAero.takeoff_landing_ref_area)

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.aero")

        def action346():
            externalAero.set_forward_flight_filepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action346)

        aeroFilepath: str = TestBase.GetScenarioFile("simpleAero.aero")
        returnMsg: str = externalAero.set_forward_flight_filepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalAero.can_set_forward_flight_ref_area)

        def action347():
            externalAero.forward_flight_ref_area = 0.05

        TryCatchAssertBlock.ExpectedException("", action347)
        Assert.assertTrue(externalAero.is_forward_flight_valid)

        returnMsg2: str = externalAero.set_takeoff_landing_filepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg2))
        Assert.assertEqual(False, externalAero.can_set_takeoff_landing_ref_area)

        def action348():
            externalAero.takeoff_landing_ref_area = 0.07

        TryCatchAssertBlock.ExpectedException("", action348)
        Assert.assertTrue(externalAero.is_takeoff_landing_valid)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationAdvancedMissileAero
    @category("Aircraft Tests")
    def test_BasicAccelerationAdvancedMissileAero(self):
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        aero: "IAircraftAero" = basicAcc.aerodynamics
        aero.aero_strategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroAdvancedMissile
        self.AdvancedMissileAero(aero.mode_as_advanced_missile)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationProp
    @category("Aircraft Tests")
    def test_BasicAccelerationProp(self):
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "IAircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AgEAvtrAircraftPropStrategy.eAircraftPropSimple
        Assert.assertEqual(AgEAvtrAircraftPropStrategy.eAircraftPropSimple, prop.prop_strategy)

        def action349():
            prop.lift_factor = 1.2

        TryCatchAssertBlock.ExpectedException("", action349)

        def action350():
            prop.drag_factor = 1.3

        TryCatchAssertBlock.ExpectedException("", action350)

        prop.prop_strategy = AgEAvtrAircraftPropStrategy.eAircraftPropBasicFixedWing
        Assert.assertEqual(AgEAvtrAircraftPropStrategy.eAircraftPropBasicFixedWing, prop.prop_strategy)

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
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "IAircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AgEAvtrAircraftPropStrategy.eAircraftPropSimple
        simpleProp: "IAircraftSimpleProp" = prop.mode_as_simple

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
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "IAircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AgEAvtrAircraftPropStrategy.eAircraftPropExternalFile

        externalProp: "IAircraftExternalProp" = prop.mode_as_external
        Assert.assertIs(None, externalProp.prop_filepath)

        def action351():
            externalProp.set_prop_filepath("")

        TryCatchAssertBlock.ExpectedException("", action351)

        def action352():
            externalProp.reload_prop_file()

        TryCatchAssertBlock.ExpectedException("", action352)
        Assert.assertEqual(False, externalProp.is_valid)

        Assert.assertTrue(externalProp.can_set_accel_decel)
        externalProp.max_thrust_accel = 0.6
        Assert.assertEqual(0.6, externalProp.max_thrust_accel)
        externalProp.min_thrust_decel = 0.4
        Assert.assertEqual(0.4, externalProp.min_thrust_decel)

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.prop")

        def action353():
            externalProp.set_prop_filepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action353)

        propFilepath: str = TestBase.GetScenarioFile("simpleProp.prop")
        returnMsg: str = externalProp.set_prop_filepath(propFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalProp.can_set_accel_decel)

        def action354():
            externalProp.max_thrust_accel = 0.6

        TryCatchAssertBlock.ExpectedException("", action354)
        Assert.assertTrue(externalProp.is_valid)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicAccelerationBasicFixedWingProp
    @category("Aircraft Tests")
    def test_BasicAccelerationBasicFixedWingProp(self):
        tolerance: float = 1e-09

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "IAircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AgEAvtrAircraftPropStrategy.eAircraftPropBasicFixedWing

        bfwProp: "IAircraftBasicFixedWingProp" = prop.mode_as_basic_fixed_wing
        bfwProp.propulsion_mode = AgEAvtrBasicFixedWingPropMode.eSpecifyThrust
        Assert.assertEqual(AgEAvtrBasicFixedWingPropMode.eSpecifyThrust, bfwProp.propulsion_mode)

        def action355():
            bfwProp.propeller_count = 1

        TryCatchAssertBlock.ExpectedException("", action355)

        def action356():
            bfwProp.propeller_diameter = 1

        TryCatchAssertBlock.ExpectedException("", action356)

        def action357():
            bfwProp.propeller_rpm = 1

        TryCatchAssertBlock.ExpectedException("", action357)

        bfwProp.min_power_thrust = 1
        Assert.assertEqual(1, bfwProp.min_power_thrust)
        bfwProp.max_power_thrust = 100000
        Assert.assertEqual(100000, bfwProp.max_power_thrust)

        bfwProp.propulsion_mode = AgEAvtrBasicFixedWingPropMode.eSpecifyPower
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

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "IAircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AgEAvtrAircraftPropStrategy.eAircraftPropMissileRocket
        rocketProp: "IMissileRocketProp" = prop.mode_as_rocket

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

        def action358():
            rocketProp.boost_fuel_fraction = 60

        TryCatchAssertBlock.ExpectedException("must be", action358)

        def action359():
            rocketProp.boost_chamber_pressure = 21000000.0

        TryCatchAssertBlock.ExpectedException("must be", action359)
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
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "IAircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AgEAvtrAircraftPropStrategy.eAircraftPropMissileRamjet
        ramjetProp: "IMissileRamjetProp" = prop.mode_as_ramjet

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
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        acc: "IAircraftAcceleration" = newAC.acceleration
        basicAcc: "IAircraftBasicAccelerationModel" = acc.get_built_in_model()

        prop: "IAircraftProp" = basicAcc.propulsion
        prop.prop_strategy = AgEAvtrAircraftPropStrategy.eAircraftPropMissileTurbojet
        turboProp: "IMissileTurbojetProp" = prop.mode_as_turbojet

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
        acc: "IAircraftAcceleration" = EarlyBoundTests.AG_AvtrAircraft.acceleration
        accAsCatalogItem: "ICatalogItem" = acc.get_as_catalog_item()
        accModelNames = accAsCatalogItem.child_names
        count: int = Array.Length(accModelNames)
        advAcc: "IAircraftAdvAccelerationModel" = clr.CastAs(
            accAsCatalogItem.add_child_of_type("Advanced Acceleration Model", "AdvAcceleration Model Name"),
            IAircraftAdvAccelerationModel,
        )

        accModelNames = accAsCatalogItem.child_names
        count += 1
        Assert.assertEqual(count, Array.Length(accModelNames))
        Assert.assertEqual("AdvAcceleration Model Name", accModelNames[0])

        accMode: "IAircraftAccelerationMode" = advAcc.acceleration_mode
        accMode.accel_mode = AgEAvtrAccelerationAdvAccelMode.eAccelModeMaxAccel

        def action360():
            accMode.accel_g = 1

        TryCatchAssertBlock.ExpectedException("must be set", action360)

        advAcc.get_as_catalog_item().remove()
        accModelNames = accAsCatalogItem.child_names
        count -= 1
        Assert.assertEqual(count, Array.Length(accModelNames))

    # endregion

    # region BasicClimbModel
    @category("Aircraft Tests")
    def test_BasicClimbModel(self):
        tolerance: float = 1e-09

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        climb: "IAircraftClimb" = newAC.climb
        basicClimb: "IAircraftBasicClimbModel" = climb.get_built_in_model()

        basicClimb.ceiling_altitude = 70001
        Assert.assertEqual(70001, basicClimb.ceiling_altitude)

        basicClimb.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicClimb.airspeed_type)
        Assert.assertAlmostEqual(251, basicClimb.airspeed, delta=tolerance)
        basicClimb.set_airspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicClimb.airspeed_type)
        Assert.assertEqual(0.4, basicClimb.airspeed)

        basicClimb.altitude_rate = 4001
        Assert.assertAlmostEqual(4001, basicClimb.altitude_rate, delta=tolerance)

        basicClimb.use_aero_prop_fuel = True
        Assert.assertTrue(basicClimb.use_aero_prop_fuel)

        def action361():
            testVal: bool = basicClimb.scale_fuel_flow_by_non_std_density

        TryCatchAssertBlock.ExpectedException("must be ", action361)

        def action362():
            basicClimb.scale_fuel_flow_by_non_std_density = True

        TryCatchAssertBlock.ExpectedException("must be ", action362)

        def action363():
            testVal: float = basicClimb.fuel_flow

        TryCatchAssertBlock.ExpectedException("must be ", action363)

        def action364():
            basicClimb.fuel_flow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action364)

        basicClimb.use_aero_prop_fuel = False
        basicClimb.fuel_flow = 9000
        Assert.assertAlmostEqual(9000, basicClimb.fuel_flow, delta=tolerance)

        basicClimb.enable_relative_airspeed_tolerance = False

        def action365():
            testVal: float = basicClimb.relative_airspeed_tolerance

        TryCatchAssertBlock.ExpectedException("must be ", action365)

        def action366():
            basicClimb.relative_airspeed_tolerance = 1

        TryCatchAssertBlock.ExpectedException("must be ", action366)

        basicClimb.enable_relative_airspeed_tolerance = True
        basicClimb.relative_airspeed_tolerance = 0.06
        Assert.assertEqual(0.06, basicClimb.relative_airspeed_tolerance)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedClimbModel
    @category("Aircraft Tests")
    def test_AdvancedClimbModel(self):
        tolerance: float = 1e-09

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        climb: "IAircraftClimb" = newAC.climb
        climb.get_as_catalog_item().add_child_of_type("Advanced Climb Model", "Adv Climb")
        advClimb: "IAircraftAdvClimbModel" = climb.get_adv_climb_by_name("Adv Climb")

        advClimb.climb_speed_type = AgEAvtrClimbSpeedType.eClimbSpeedMinFuel
        Assert.assertEqual(AgEAvtrClimbSpeedType.eClimbSpeedMinFuel, advClimb.climb_speed_type)

        def action367():
            advClimb.set_climb_override_airspeed(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action367)

        advClimb.climb_speed_type = AgEAvtrClimbSpeedType.eClimbSpeedOverride
        advClimb.set_climb_override_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advClimb.climb_override_airspeed_type)
        Assert.assertAlmostEqual(251, advClimb.climb_override_airspeed, delta=tolerance)

        advClimb.set_climb_override_airspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advClimb.climb_override_airspeed_type)
        Assert.assertEqual(0.4, advClimb.climb_override_airspeed)

        def action368():
            advClimb.use_afterburner = True

        TryCatchAssertBlock.ExpectedException("not enabled", action368)
        Assert.assertEqual(False, advClimb.use_afterburner)

        advClimb.use_airspeed_limit = False
        Assert.assertEqual(False, advClimb.use_airspeed_limit)

        def action369():
            advClimb.altitude_limit = 9000

        TryCatchAssertBlock.ExpectedException("must be", action369)

        def action370():
            advClimb.set_airspeed_limit(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action370)

        advClimb.use_airspeed_limit = True
        advClimb.altitude_limit = 9000
        Assert.assertEqual(9000, advClimb.altitude_limit)
        advClimb.set_airspeed_limit(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advClimb.airspeed_limit_type)
        Assert.assertAlmostEqual(251, advClimb.airspeed_limit, delta=tolerance)
        advClimb.set_airspeed_limit(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advClimb.airspeed_limit_type)
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

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        cruise: "IAircraftCruise" = newAC.cruise
        basicCruise: "IAircraftBasicCruiseModel" = cruise.get_built_in_model()

        basicCruise.ceiling_altitude = 20000
        Assert.assertEqual(20000, basicCruise.ceiling_altitude)
        basicCruise.default_cruise_altitude = 10000
        Assert.assertEqual(10000, basicCruise.default_cruise_altitude)
        basicCruise.airspeed_type = AgEAvtrAirspeedType.eCAS
        Assert.assertEqual(AgEAvtrAirspeedType.eCAS, basicCruise.airspeed_type)
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

        basicCruise.airspeed_type = AgEAvtrAirspeedType.eMach
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicCruise.airspeed_type)

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

        def action371():
            basicCruise.scale_fuel_flow_by_non_std_density = True

        TryCatchAssertBlock.ExpectedException("must be", action371)

        def action372():
            basicCruise.min_airspeed_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action372)

        def action373():
            basicCruise.max_endurance_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action373)

        def action374():
            basicCruise.max_airspeed_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action374)

        def action375():
            basicCruise.max_range_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action375)

        def action376():
            basicCruise.max_perf_airspeed_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action376)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedCruiseModel
    @category("Aircraft Tests")
    def test_AdvancedCruiseModel(self):
        tolerance: float = 1e-09

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        cruise: "IAircraftCruise" = newAC.cruise
        cruise.get_as_catalog_item().add_child_of_type("Advanced Cruise Model", "Adv Cruise")
        advCruise: "IAircraftAdvCruiseModel" = cruise.get_adv_cruise_by_name("Adv Cruise")

        advCruise.default_cruise_altitude = 10001
        Assert.assertEqual(10001, advCruise.default_cruise_altitude)
        advCruise.max_perf_airspeed = AgEAvtrCruiseMaxPerfSpeedType.eMaxSpeedDryThrust
        Assert.assertEqual(AgEAvtrCruiseMaxPerfSpeedType.eMaxSpeedDryThrust, advCruise.max_perf_airspeed)

        advCruise.use_airspeed_limit = False
        Assert.assertEqual(False, advCruise.use_airspeed_limit)

        def action377():
            advCruise.altitude_limit = 9000

        TryCatchAssertBlock.ExpectedException("must be", action377)

        def action378():
            advCruise.set_airspeed_limit(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action378)

        advCruise.use_airspeed_limit = True
        advCruise.altitude_limit = 9000
        Assert.assertEqual(9000, advCruise.altitude_limit)
        advCruise.set_airspeed_limit(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advCruise.airspeed_limit_type)
        Assert.assertAlmostEqual(251, advCruise.airspeed_limit, delta=tolerance)
        advCruise.set_airspeed_limit(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advCruise.airspeed_limit_type)
        Assert.assertEqual(0.4, advCruise.airspeed_limit)

        advCruise.compute_delta_downrange = 11
        Assert.assertEqual(11, advCruise.compute_delta_downrange)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicDescentModel
    @category("Aircraft Tests")
    def test_BasicDescentModel(self):
        tolerance: float = 1e-09

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        descent: "IAircraftDescent" = newAC.descent
        basicDescent: "IAircraftBasicDescentModel" = descent.get_built_in_model()

        basicDescent.ceiling_altitude = 70001
        Assert.assertEqual(70001, basicDescent.ceiling_altitude)

        basicDescent.set_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicDescent.airspeed_type)
        Assert.assertAlmostEqual(251, basicDescent.airspeed, delta=tolerance)
        basicDescent.set_airspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicDescent.airspeed_type)
        Assert.assertEqual(0.4, basicDescent.airspeed)

        basicDescent.altitude_rate = -4001
        Assert.assertAlmostEqual(-4001, basicDescent.altitude_rate, delta=tolerance)

        basicDescent.use_aero_prop_fuel = True
        Assert.assertTrue(basicDescent.use_aero_prop_fuel)

        def action379():
            testVal: bool = basicDescent.scale_fuel_flow_by_non_std_density

        TryCatchAssertBlock.ExpectedException("must be ", action379)

        def action380():
            basicDescent.scale_fuel_flow_by_non_std_density = True

        TryCatchAssertBlock.ExpectedException("must be ", action380)

        def action381():
            testVal: float = basicDescent.fuel_flow

        TryCatchAssertBlock.ExpectedException("must be ", action381)

        def action382():
            basicDescent.fuel_flow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action382)

        basicDescent.use_aero_prop_fuel = False
        basicDescent.fuel_flow = 9000
        Assert.assertAlmostEqual(9000, basicDescent.fuel_flow, delta=tolerance)

        basicDescent.enable_relative_airspeed_tolerance = False

        def action383():
            testVal: float = basicDescent.relative_airspeed_tolerance

        TryCatchAssertBlock.ExpectedException("must be ", action383)

        def action384():
            basicDescent.relative_airspeed_tolerance = 1

        TryCatchAssertBlock.ExpectedException("must be ", action384)

        basicDescent.enable_relative_airspeed_tolerance = True
        basicDescent.relative_airspeed_tolerance = 0.06
        Assert.assertEqual(0.06, basicDescent.relative_airspeed_tolerance)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region AdvancedDescentModel
    @category("Aircraft Tests")
    def test_AdvancedDescentModel(self):
        tolerance: float = 1e-09

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        descent: "IAircraftDescent" = newAC.descent
        descent.get_as_catalog_item().add_child_of_type("Advanced Descent Model", "Adv Descent")
        advDescent: "IAircraftAdvDescentModel" = descent.get_adv_descent_by_name("Adv Descent")

        advDescent.descent_speed_type = AgEAvtrDescentSpeedType.eDescentMaxRangeCruise
        Assert.assertEqual(AgEAvtrDescentSpeedType.eDescentMaxRangeCruise, advDescent.descent_speed_type)

        def action385():
            advDescent.descent_stall_speed_ratio = 1.2

        TryCatchAssertBlock.ExpectedException("must be", action385)

        def action386():
            advDescent.set_descent_override_airspeed(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action386)

        advDescent.descent_speed_type = AgEAvtrDescentSpeedType.eDescentStallSpeedRatio
        advDescent.descent_stall_speed_ratio = 1.2
        Assert.assertEqual(1.2, advDescent.descent_stall_speed_ratio)

        advDescent.descent_speed_type = AgEAvtrDescentSpeedType.eDescentSpeedOverride
        advDescent.set_descent_override_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advDescent.descent_override_airspeed_type)
        Assert.assertAlmostEqual(251, advDescent.descent_override_airspeed, delta=tolerance)

        advDescent.set_descent_override_airspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advDescent.descent_override_airspeed_type)
        Assert.assertEqual(0.4, advDescent.descent_override_airspeed)

        advDescent.speedbrakes = 95
        Assert.assertEqual(95, advDescent.speedbrakes)

        advDescent.use_airspeed_limit = False
        Assert.assertEqual(False, advDescent.use_airspeed_limit)

        def action387():
            advDescent.altitude_limit = 9000

        TryCatchAssertBlock.ExpectedException("must be", action387)

        def action388():
            advDescent.set_airspeed_limit(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action388)

        advDescent.use_airspeed_limit = True
        advDescent.altitude_limit = 9000
        Assert.assertEqual(9000, advDescent.altitude_limit)
        advDescent.set_airspeed_limit(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advDescent.airspeed_limit_type)
        Assert.assertAlmostEqual(251, advDescent.airspeed_limit, delta=tolerance)
        advDescent.set_airspeed_limit(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advDescent.airspeed_limit_type)
        Assert.assertEqual(0.4, advDescent.airspeed_limit)

        advDescent.compute_delta_altitude = 1001
        Assert.assertEqual(1001, advDescent.compute_delta_altitude)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region BasicLandingModel
    @category("Aircraft Tests")
    def test_BasicLandingModel(self):
        tolerance: float = 1e-09

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        landing: "IAircraftLanding" = newAC.landing
        basicLanding: "IAircraftBasicLandingModel" = landing.get_built_in_model()

        basicLanding.set_landing_speed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicLanding.landing_speed_type)
        Assert.assertAlmostEqual(251, basicLanding.landing_speed, delta=tolerance)
        basicLanding.set_landing_speed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicLanding.landing_speed_type)
        Assert.assertEqual(0.4, basicLanding.landing_speed)

        basicLanding.sea_level_ground_roll = 6
        Assert.assertAlmostEqual(6, basicLanding.sea_level_ground_roll, delta=tolerance)

        basicLanding.use_aero_prop_fuel = True
        Assert.assertTrue(basicLanding.use_aero_prop_fuel)

        def action389():
            basicLanding.scale_fuel_flow_by_non_std_density = True

        TryCatchAssertBlock.ExpectedException("must be ", action389)

        def action390():
            basicLanding.fuel_flow = 9000

        TryCatchAssertBlock.ExpectedException("must be ", action390)

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
        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        landing: "IAircraftLanding" = newAC.landing
        landing.get_as_catalog_item().add_child_of_type("Advanced Landing Model", "Adv Landing")
        advLanding: "IAircraftAdvLandingModel" = landing.get_adv_landing_by_name("Adv Landing")

        advLanding.landing_speed_mode = AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingAngleOfAttack
        Assert.assertEqual(AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingAngleOfAttack, advLanding.landing_speed_mode)

        advLanding.set_angle_of_attack(11)
        angle: typing.Any = advLanding.angle_of_attack
        Assert.assertEqual(11, float(angle))

        advLanding.set_stall_speed_ratio(1.2)
        Assert.assertEqual(AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingStallSpeedRatio, advLanding.landing_speed_mode)
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

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        takeoff: "IAircraftTakeoff" = newAC.takeoff
        basicTakeoff: "IAircraftBasicTakeoffModel" = takeoff.get_built_in_model()

        basicTakeoff.set_takeoff_speed(AgEAvtrAirspeedType.eTAS, 151)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicTakeoff.takeoff_speed_type)
        Assert.assertAlmostEqual(151, basicTakeoff.takeoff_speed, delta=tolerance)
        basicTakeoff.set_takeoff_speed(AgEAvtrAirspeedType.eMach, 0.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicTakeoff.takeoff_speed_type)
        Assert.assertEqual(0.3, basicTakeoff.takeoff_speed)

        basicTakeoff.sea_level_ground_roll = 6
        Assert.assertAlmostEqual(6, basicTakeoff.sea_level_ground_roll, delta=tolerance)

        basicTakeoff.set_departure_speed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicTakeoff.departure_speed_type)
        Assert.assertAlmostEqual(251, basicTakeoff.departure_speed, delta=tolerance)
        basicTakeoff.set_departure_speed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicTakeoff.departure_speed_type)
        Assert.assertEqual(0.4, basicTakeoff.departure_speed)

        basicTakeoff.use_aero_prop_fuel = True
        Assert.assertTrue(basicTakeoff.use_aero_prop_fuel)

        def action391():
            basicTakeoff.scale_fuel_flow_by_non_std_density = True

        TryCatchAssertBlock.ExpectedException("must be ", action391)

        def action392():
            basicTakeoff.accel_fuel_flow = 8000

        TryCatchAssertBlock.ExpectedException("must be ", action392)

        def action393():
            basicTakeoff.departure_fuel_flow = 9000

        TryCatchAssertBlock.ExpectedException("must be ", action393)

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

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        takeoff: "IAircraftTakeoff" = newAC.takeoff
        takeoff.get_as_catalog_item().add_child_of_type("Advanced Takeoff Model", "Adv Takeoff")
        advTakeoff: "IAircraftAdvTakeoffModel" = takeoff.get_adv_takeoff_by_name("Adv Takeoff")

        advTakeoff.takeoff_speed_mode = AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingAngleOfAttack
        Assert.assertEqual(AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingAngleOfAttack, advTakeoff.takeoff_speed_mode)

        advTakeoff.set_angle_of_attack(11)
        angle: typing.Any = advTakeoff.angle_of_attack
        Assert.assertEqual(11, float(angle))

        advTakeoff.set_stall_speed_ratio(1.2)
        Assert.assertEqual(AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingStallSpeedRatio, advTakeoff.takeoff_speed_mode)
        Assert.assertEqual(1.2, advTakeoff.stall_speed_ratio)

        advTakeoff.flaps = 99
        Assert.assertEqual(99, advTakeoff.flaps)

        advTakeoff.departure_speed_mode = AgEAvtrDepartureSpeedMode.eUseClimbModel
        Assert.assertEqual(AgEAvtrDepartureSpeedMode.eUseClimbModel, advTakeoff.departure_speed_mode)

        advTakeoff.set_departure_speed_limit(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advTakeoff.departure_speed_limit_type)
        Assert.assertAlmostEqual(251, advTakeoff.departure_speed_limit, delta=tolerance)
        advTakeoff.set_departure_speed_limit(AgEAvtrAirspeedType.eMach, 0.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advTakeoff.departure_speed_limit_type)
        Assert.assertAlmostEqual(0.3, advTakeoff.departure_speed_limit, delta=tolerance)

        def action394():
            advTakeoff.use_afterburner = True

        TryCatchAssertBlock.ExpectedException("not enabled ", action394)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region TerrainFollowModel
    @category("Aircraft Tests")
    def test_TerrainFollowModel(self):
        tolerance: float = 1e-09

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        terrainFollowCategory: "IAircraftTerrainFollow" = newAC.terrain_follow
        terrainFollowCategory.get_as_catalog_item().add_child_of_type(
            "AGI TerrainFollow Model", "Test TerrainFollow Model"
        )
        terrainFollow: "IAircraftTerrainFollowModel" = terrainFollowCategory.get_terrain_follow_by_name(
            "Test TerrainFollow Model"
        )

        terrainFollow.use_aero_prop_fuel = True
        Assert.assertTrue(terrainFollow.use_aero_prop_fuel)

        def action395():
            terrainFollow.scale_fuel_flow_by_non_std_density = True

        TryCatchAssertBlock.ExpectedException("must be", action395)

        def action396():
            terrainFollow.min_airspeed_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action396)

        def action397():
            terrainFollow.max_endurance_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action397)

        def action398():
            terrainFollow.max_airspeed_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action398)

        def action399():
            terrainFollow.max_range_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action399)

        def action400():
            terrainFollow.max_perf_airspeed_fuel_flow = 100

        TryCatchAssertBlock.ExpectedException("must be", action400)

        terrainFollow.use_aero_prop_fuel = False
        Assert.assertEqual(False, terrainFollow.use_aero_prop_fuel)
        terrainFollow.scale_fuel_flow_by_non_std_density = True
        Assert.assertTrue(terrainFollow.scale_fuel_flow_by_non_std_density)

        terrainFollow.airspeed_type = AgEAvtrAirspeedType.eCAS
        Assert.assertEqual(AgEAvtrAirspeedType.eCAS, terrainFollow.airspeed_type)

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

        terrainFollow.airspeed_type = AgEAvtrAirspeedType.eMach
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, terrainFollow.airspeed_type)

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

        newAC: "IAircraftModel" = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.get_as_catalog_item().duplicate(), IAircraftModel
        )
        vtolCategory: "IAircraftVTOL" = newAC.vtol
        vtolCategory.get_as_catalog_item().add_child_of_type("AGI VTOL Model", "Test VTOL Model")
        vtol: "IAircraftVTOLModel" = vtolCategory.get_vtol_by_name("Test VTOL Model")

        vtol.max_hover_altitude = 20000
        Assert.assertEqual(20000, vtol.max_hover_altitude)

        vtol.use_aero_prop_fuel = True
        Assert.assertTrue(vtol.use_aero_prop_fuel)

        def action401():
            vtol.scale_fuel_flow_by_non_std_density = True

        TryCatchAssertBlock.ExpectedException("must be ", action401)

        def action402():
            vtol.hover_fuel = 0.25

        TryCatchAssertBlock.ExpectedException("must be ", action402)

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

        vtol.set_forward_flight_airspeed(AgEAvtrAirspeedType.eTAS, 90)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, vtol.forward_flight_airspeed_type)
        Assert.assertEqual(90, vtol.forward_flight_airspeed)
        vtol.set_forward_flight_airspeed(AgEAvtrAirspeedType.eMach, 0.1)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, vtol.forward_flight_airspeed_type)
        Assert.assertEqual(0.1, vtol.forward_flight_airspeed)

        vtol.forward_flight_transition_time = 5
        Assert.assertEqual(5, vtol.forward_flight_transition_time)

        newAC.get_as_catalog_item().remove()

    # endregion

    # region MissileModel
    @category("Missile Tests")
    def test_MissileModel(self):
        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
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

        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missile.max_load_factor = 11
        Assert.assertEqual(11, missile.max_load_factor)
        missile.maneuver_mode = AgEAvtrAccelManeuverMode.eAccelManeuverModeDensityScale
        Assert.assertEqual(AgEAvtrAccelManeuverMode.eAccelManeuverModeDensityScale, missile.maneuver_mode)

        def action403():
            testVal: "IAeroPropManeuverModeHelper" = missile.maneuver_mode_helper

        TryCatchAssertBlock.ExpectedException("must be set", action403)

        missile.maneuver_mode = AgEAvtrAccelManeuverMode.eAccelManeuverModeAeroProp
        self.ManeuverModeHelperOptions(missile.maneuver_mode_helper)

        self.AttitudeTransitionOptions(missile.attitude_transitions)

        missile.ignore_fpa_for_climb_descent_transitions = True
        Assert.assertTrue(missile.ignore_fpa_for_climb_descent_transitions)

        missile.set_climb_airspeed(AgEAvtrAirspeedType.eMach, 2.1)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, missile.climb_airspeed_type)
        Assert.assertEqual(2.1, missile.climb_airspeed)
        missile.set_climb_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, missile.climb_airspeed_type)
        Assert.assertAlmostEqual(251, missile.climb_airspeed, delta=tolerance)
        missile.climb_fail_on_insufficient_performance = False
        Assert.assertEqual(False, missile.climb_fail_on_insufficient_performance)

        missile.set_cruise_max_airspeed(AgEAvtrAirspeedType.eMach, 2.2)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, missile.cruise_max_airspeed_type)
        Assert.assertEqual(2.2, missile.cruise_max_airspeed)
        missile.set_cruise_max_airspeed(AgEAvtrAirspeedType.eTAS, 252)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, missile.cruise_max_airspeed_type)
        Assert.assertAlmostEqual(252, missile.cruise_max_airspeed, delta=tolerance)

        missile.set_descent_airspeed(AgEAvtrAirspeedType.eMach, 2.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, missile.descent_airspeed_type)
        Assert.assertEqual(2.3, missile.descent_airspeed)
        missile.set_descent_airspeed(AgEAvtrAirspeedType.eTAS, 253)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, missile.descent_airspeed_type)
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

        def action404():
            missile.total_temp_limit = 3000

        TryCatchAssertBlock.ExpectedException("must be", action404)
        missile.use_total_temp_limit = True
        Assert.assertTrue(missile.use_total_temp_limit)
        missile.total_temp_limit = 3000
        Assert.assertEqual(3000, missile.total_temp_limit)

        missile.use_mach_limit = False

        def action405():
            missile.mach_limit = 6

        TryCatchAssertBlock.ExpectedException("must be", action405)
        missile.use_mach_limit = True
        Assert.assertTrue(missile.use_mach_limit)
        missile.mach_limit = 6
        Assert.assertEqual(6, missile.mach_limit)

        missile.use_eas_limit = False

        def action406():
            missile.eas_limit = 800

        TryCatchAssertBlock.ExpectedException("must be", action406)
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
        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileAero: "IMissileAero" = missile.aerodynamics
        missileAero.aero_strategy = AgEAvtrMissileAeroStrategy.eMissileAeroSimple
        Assert.assertEqual(AgEAvtrMissileAeroStrategy.eMissileAeroSimple, missileAero.aero_strategy)
        simple: "IMissileSimpleAero" = missileAero.mode_as_simple

        simple.s_ref = 5
        Assert.assertEqual(5, simple.s_ref)
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
        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileAero: "IMissileAero" = missile.aerodynamics
        missileAero.aero_strategy = AgEAvtrMissileAeroStrategy.eMissileAeroExternalFile
        Assert.assertEqual(AgEAvtrMissileAeroStrategy.eMissileAeroExternalFile, missileAero.aero_strategy)
        externalAero: "IMissileExternalAero" = missileAero.mode_as_external

        externalAero.ref_area = 3
        Assert.assertEqual(3, externalAero.ref_area)
        Assert.assertEqual(False, externalAero.is_valid)

        nonexistingfilepath: str = TestBase.GetScenarioFile("DoesNotExist.aero")

        def action407():
            externalAero.set_filepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action407)

        aeroFilepath: str = TestBase.GetScenarioFile("simpleAero.aero")
        returnMsg: str = externalAero.set_filepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalAero.can_set_ref_area)

        def action408():
            externalAero.ref_area = 0.05

        TryCatchAssertBlock.ExpectedException("", action408)
        Assert.assertTrue(externalAero.is_valid)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissileAeroAdvanced
    @category("Missile Tests")
    def test_MissileAeroAdvanced(self):
        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileAero: "IMissileAero" = missile.aerodynamics
        missileAero.aero_strategy = AgEAvtrMissileAeroStrategy.eMissileAeroAdvanced
        Assert.assertEqual(AgEAvtrMissileAeroStrategy.eMissileAeroAdvanced, missileAero.aero_strategy)
        advancedAero: "IMissileAdvancedAero" = missileAero.mode_as_advanced

        self.AdvancedMissileAero(advancedAero)

        missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropSimple
    @category("Missile Tests")
    def test_MissilePropSimple(self):
        tolerance: float = 1e-09

        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "IMissileProp" = missile.propulsion
        missileProp.prop_strategy = AgEAvtrMissilePropStrategy.eMissilePropSimple
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropSimple, missileProp.prop_strategy)
        simpleProp: "IMissileSimpleProp" = missileProp.mode_as_simple

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
        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "IMissileProp" = missile.propulsion
        missileProp.prop_strategy = AgEAvtrMissilePropStrategy.eMissilePropExternalFile
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropExternalFile, missileProp.prop_strategy)
        externalProp: "IMissileExternalProp" = missileProp.mode_as_external

        Assert.assertEqual(False, externalProp.is_valid)

        nonexistingPropFilepath: str = TestBase.GetScenarioFile("DoesNotExist.prop")

        def action409():
            externalProp.set_filepath(nonexistingPropFilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action409)

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
        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "IMissileProp" = missile.propulsion
        missileProp.prop_strategy = AgEAvtrMissilePropStrategy.eMissilePropRamjet
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropRamjet, missileProp.prop_strategy)
        ramjetProp: "IMissileRamjetProp" = missileProp.mode_as_ramjet

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
        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "IMissileProp" = missile.propulsion
        missileProp.prop_strategy = AgEAvtrMissilePropStrategy.eMissilePropTurbojet
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropTurbojet, missileProp.prop_strategy)
        turboProp: "IMissileTurbojetProp" = missileProp.mode_as_turbojet

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

        missileModels: "IMissileModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.missile_models
        if missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"):
            missileModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Missile")

        missile: "IMissileModel" = missileModels.add_missile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.get_as_catalog_item().name)
        Assert.assertTrue(missileModels.get_as_catalog_source().contains("NUNIT CSharp Test Missile"))

        missileProp: "IMissileProp" = missile.propulsion
        missileProp.prop_strategy = AgEAvtrMissilePropStrategy.eMissilePropRocket
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropRocket, missileProp.prop_strategy)
        rocketProp: "IMissileRocketProp" = missileProp.mode_as_rocket

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
        rotorcraftModels: "IRotorcraftModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models
        if rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")

        rotorcraft: "IRotorcraftModel" = rotorcraftModels.add_rotorcraft("NUNIT CSharp Test Rotorcraft")
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

        rotorcraftModels: "IRotorcraftModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models
        if rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")

        rotorcraft: "IRotorcraftModel" = rotorcraftModels.add_rotorcraft("NUNIT CSharp Test Rotorcraft")
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
        rotorcraft.compute_delta_alt = 2000
        Assert.assertEqual(2000, rotorcraft.compute_delta_alt)

        rotorcraft.set_max_safe_airspeed(AgEAvtrAirspeedType.eMach, 0.5)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, rotorcraft.max_safe_airspeed_type)
        Assert.assertEqual(0.5, rotorcraft.max_safe_airspeed)
        rotorcraft.set_max_safe_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, rotorcraft.max_safe_airspeed_type)
        Assert.assertAlmostEqual(251, rotorcraft.max_safe_airspeed, delta=tolerance)

        rotorcraft.set_max_safe_translation_speed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, rotorcraft.max_safe_translation_speed_type)
        Assert.assertEqual(0.4, rotorcraft.max_safe_translation_speed)
        rotorcraft.set_max_safe_translation_speed(AgEAvtrAirspeedType.eTAS, 211)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, rotorcraft.max_safe_translation_speed_type)
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
        rotorcraftModels: "IRotorcraftModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models
        if rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")

        rotorcraft: "IRotorcraftModel" = rotorcraftModels.add_rotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.get_as_catalog_item().name)
        Assert.assertTrue(rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

        aero: "IRotorcraftAero" = rotorcraft.aerodynamics

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

        rotorcraftModels: "IRotorcraftModels" = EarlyBoundTests.AG_AvtrCatalog.aircraft_category.rotorcraft_models
        if rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.get_as_catalog_source().remove_child("NUNIT CSharp Test Rotorcraft")

        rotorcraft: "IRotorcraftModel" = rotorcraftModels.add_rotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.get_as_catalog_item().name)
        Assert.assertTrue(rotorcraftModels.get_as_catalog_source().contains("NUNIT CSharp Test Rotorcraft"))

        prop: "IRotorcraftProp" = rotorcraft.propulsion

        prop.powerplant_type = AgEAvtrRotorcraftPowerplantType.eRotorcraftElectric
        Assert.assertEqual(AgEAvtrRotorcraftPowerplantType.eRotorcraftElectric, prop.powerplant_type)
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { prop.MaxSLFuelFlow = 5; });

        prop.powerplant_type = AgEAvtrRotorcraftPowerplantType.eRotorcraftTurboshaft
        Assert.assertEqual(AgEAvtrRotorcraftPowerplantType.eRotorcraftTurboshaft, prop.powerplant_type)
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
        userRunways: "IUserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        names = userRunways.get_as_catalog_source().child_names
        nameCount: int = Array.Length(names)

        nunitRunway: "IUserRunway" = userRunways.add_user_runway("NUnitUserRunway")
        Assert.assertEqual("NUnitUserRunway", nunitRunway.get_as_catalog_item().name)
        Assert.assertTrue(userRunways.get_as_catalog_source().contains("NUnitUserRunway"))
        names = userRunways.get_as_catalog_source().child_names
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitRunway2: "IUserRunway" = userRunways.get_user_runway("NUnitUserRunway")
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

        userRunways: "IUserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        nunitRunway: "IUserRunway" = userRunways.add_user_runway("NUnitUserRunway")

        nunitRunway.latitude = 1
        lat: typing.Any = nunitRunway.latitude
        Assert.assertEqual(1, float(lat))
        nunitRunway.longitude = 2
        lon: typing.Any = nunitRunway.longitude
        Assert.assertEqual(2, float(lon))
        nunitRunway.altitude = 5
        Assert.assertEqual(5, nunitRunway.altitude)
        terrainAlt: float = nunitRunway.get_terrain_alt()
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

        nunitRunway2: "IUserRunway" = userRunways.add_user_runway("NUnitUserRunway2")
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
        userVTOLPoints: "IUserVTOLPointSource" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.user_vtol_points
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

        names = userVTOLPoints.get_as_catalog_source().child_names
        nameCount: int = Array.Length(names)

        nunitVTOLPoint: "IUserVTOLPoint" = userVTOLPoints.add_user_vtol_point("NUnitUserVTOLPoint")
        Assert.assertEqual("NUnitUserVTOLPoint", nunitVTOLPoint.get_as_catalog_item().name)
        Assert.assertTrue(userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"))
        names = userVTOLPoints.get_as_catalog_source().child_names
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitVTOLPoint2: "IUserVTOLPoint" = userVTOLPoints.get_user_vtol_point("NUnitUserVTOLPoint")
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
        userVTOLPoints: "IUserVTOLPointSource" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.user_vtol_points
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

        nunitVTOLPoint: "IUserVTOLPoint" = userVTOLPoints.add_user_vtol_point("NUnitUserVTOLPoint")

        nunitVTOLPoint.latitude = 1
        lat: typing.Any = nunitVTOLPoint.latitude
        Assert.assertEqual(1, float(lat))
        nunitVTOLPoint.longitude = 2
        lon: typing.Any = nunitVTOLPoint.longitude
        Assert.assertEqual(2, float(lon))
        nunitVTOLPoint.altitude = 5
        Assert.assertEqual(5, nunitVTOLPoint.altitude)
        terrainAlt: float = nunitVTOLPoint.get_terrain_alt()
        Assert.assertEqual(terrainAlt, nunitVTOLPoint.altitude)

        nunitVTOLPoint.copy_site()
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint2"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint2")

        nunitVTOLPoint2: "IUserVTOLPoint" = userVTOLPoints.add_user_vtol_point("NUnitUserVTOLPoint2")
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
        userWaypoints: "IUserWaypointSource" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.user_waypoints
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

        names = userWaypoints.get_as_catalog_source().child_names
        nameCount: int = Array.Length(names)

        nunitWaypoint: "IUserWaypoint" = userWaypoints.add_user_waypoint("NUnitUserWaypoint")
        Assert.assertEqual("NUnitUserWaypoint", nunitWaypoint.get_as_catalog_item().name)
        Assert.assertTrue(userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"))
        names = userWaypoints.get_as_catalog_source().child_names
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitWaypoint2: "IUserWaypoint" = userWaypoints.get_user_waypoint("NUnitUserWaypoint")
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
        userWaypoints: "IUserWaypointSource" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.user_waypoints
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

        nunitWaypoint: "IUserWaypoint" = userWaypoints.add_user_waypoint("NUnitUserWaypoint")

        nunitWaypoint.latitude = 1
        lat: typing.Any = nunitWaypoint.latitude
        Assert.assertEqual(1, float(lat))
        nunitWaypoint.longitude = 2
        lon: typing.Any = nunitWaypoint.longitude
        Assert.assertEqual(2, float(lon))

        nunitWaypoint.copy_site()
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint2"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint2")

        nunitWaypoint2: "IUserWaypoint" = userWaypoints.add_user_waypoint("NUnitUserWaypoint2")
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
        arincAirports: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.airport_category.arinc424_airports
        self.ARINC424Source(arincAirports, "02 RANCH")

    # endregion

    # region ARINC424Airport
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Airport(self):
        tolerance: float = 0.01

        arincAirports: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.airport_category.arinc424_airports
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

        userRunways: "IUserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        nunitRunway: "IUserRunway" = userRunways.add_user_runway("NUnitUserRunway")

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
        arincHelipads: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.arinc424_helipads
        self.ARINC424Source(arincHelipads, "1001 FOURTH AVENUE PLAZA H1")

    # endregion

    # region ARINC424Helipad
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Helipad(self):
        tolerance: float = 0.01

        arincHelipads: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.arinc424_helipads
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

        userVTOLPoints: "IUserVTOLPointSource" = EarlyBoundTests.AG_AvtrCatalog.vtol_point_category.user_vtol_points
        if userVTOLPoints.get_as_catalog_source().contains("NUnitUserVTOLPoint"):
            userVTOLPoints.get_as_catalog_source().remove_child("NUnitUserVTOLPoint")

        nunitVTOLPoint: "IUserVTOLPoint" = userVTOLPoints.add_user_vtol_point("NUnitUserVTOLPoint")

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
        arincNavaids: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.navaid_category.arinc424_navaids
        self.ARINC424Source(arincNavaids, "1B")

    # endregion

    # region ARINC424Navaid
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Navaid(self):
        tolerance: float = 0.01

        arincNavaids: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.navaid_category.arinc424_navaids
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

        userRunways: "IUserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        nunitRunway: "IUserRunway" = userRunways.add_user_runway("NUnitUserRunway")

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
        arincRunways: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.runway_category.arinc424_runways
        self.ARINC424Source(arincRunways, "JOHN F KENNEDY INTL 04L 22R")

    # endregion

    # region ARINC424Runway
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Runway(self):
        tolerance: float = 0.01

        arincRunways: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.runway_category.arinc424_runways
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

        userRunways: "IUserRunwaySource" = EarlyBoundTests.AG_AvtrCatalog.runway_category.user_runways
        if userRunways.get_as_catalog_source().contains("NUnitUserRunway"):
            userRunways.get_as_catalog_source().remove_child("NUnitUserRunway")

        nunitRunway: "IUserRunway" = userRunways.add_user_runway("NUnitUserRunway")

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
        arincWaypoints: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.arinc424_waypoints
        self.ARINC424Source(arincWaypoints, "AAAMY")

    # endregion

    # region ARINC424Waypoint
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Waypoint(self):
        tolerance: float = 0.01

        arincWaypoints: "IARINC424Source" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.arinc424_waypoints
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

        userWaypoints: "IUserWaypointSource" = EarlyBoundTests.AG_AvtrCatalog.waypoint_category.user_waypoints
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

        nunitWaypoint: "IUserWaypoint" = userWaypoints.add_user_waypoint("NUnitUserWaypoint")

        nunitWaypoint.paste_site()
        lat: typing.Any = nunitWaypoint.latitude
        Assert.assertAlmostEqual(43.069, float(lat), delta=tolerance)
        lon: typing.Any = nunitWaypoint.longitude
        Assert.assertAlmostEqual(-82.615, float(lon), delta=tolerance)
        if userWaypoints.get_as_catalog_source().contains("NUnitUserWaypoint"):
            userWaypoints.get_as_catalog_source().remove_child("NUnitUserWaypoint")

    # endregion

    # region PrivateCatalogMethods

    def AdvancedMissileAero(self, advancedAero: "IMissileAdvancedAero"):
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

    def EmpiricalJetEngineOptions(self, prop: "IAdvFixedWingEmpiricalJetEngine"):
        tolerance: float = 1e-09

        prop.max_sea_level_static_thrust = 65000
        Assert.assertAlmostEqual(65000, prop.max_sea_level_static_thrust, delta=tolerance)
        prop.design_point_altitude = 2
        Assert.assertEqual(2, prop.design_point_altitude)
        prop.design_point_mach_number = 0.75
        Assert.assertEqual(0.75, prop.design_point_mach_number)

        prop.fuel_flow = 25000
        Assert.assertAlmostEqual(25000, prop.fuel_flow, delta=tolerance)

    def AttitudeTransitionOptions(self, att: "IAttitudeTransitions"):
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

    def ManeuverModeHelperOptions(self, helper: "IAeroPropManeuverModeHelper"):
        tolerance: float = 1e-09

        helper.mode = AgEAvtrAccelManeuverAeroPropMode.eUseLiftCoefficientOnly
        Assert.assertEqual(AgEAvtrAccelManeuverAeroPropMode.eUseLiftCoefficientOnly, helper.mode)

        helper.flight_mode = AgEAvtrAeroPropFlightMode.eFlightPerfTakeoff
        Assert.assertEqual(AgEAvtrAeroPropFlightMode.eFlightPerfTakeoff, helper.flight_mode)

        helper.use_afterburner = True
        Assert.assertTrue(helper.use_afterburner)

        helper.ref_weight = 20000
        Assert.assertEqual(20000, helper.ref_weight)
        helper.ref_altitude = 25000
        Assert.assertEqual(25000, helper.ref_altitude)
        helper.set_ref_airspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, helper.ref_airspeed_type)
        Assert.assertAlmostEqual(251, helper.ref_airspeed, delta=tolerance)
        helper.set_ref_airspeed(AgEAvtrAirspeedType.eMach, 0.6)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, helper.ref_airspeed_type)
        Assert.assertAlmostEqual(0.6, helper.ref_airspeed, delta=tolerance)

        helper.ref_load_factor = 6
        Assert.assertEqual(6, helper.ref_load_factor)

        helper.control_authority = 0.5
        Assert.assertEqual(0.5, helper.control_authority)

    def ConfigurationOptions(self, defConfig: "IConfiguration"):
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

    def ARINC424Source(self, arincSource: "IARINC424Source", childName: str):
        Assert.assertTrue(arincSource.use_master_data_file)

        def action410():
            arincSource.override_data_filepath = "NonExistantPath"

        TryCatchAssertBlock.ExpectedException("to access this", action410)

        arincSource.use_master_data_file = False
        arincSource.override_data_filepath = "NonExistantPath"
        Assert.assertEqual("NonExistantPath", arincSource.override_data_filepath)

        arincSource.use_master_data_file = True
        Assert.assertTrue(("FAA" in arincSource.master_data_filepath))

        catalogSource: "ICatalogSource" = clr.CastAs(arincSource, ICatalogSource)
        names = catalogSource.child_names
        Assert.assertTrue((Array.Length(names) > 0))
        Assert.assertTrue(catalogSource.contains(childName))

        def action411():
            catalogSource.remove_child(childName)

        TryCatchAssertBlock.ExpectedException("", action411)

    def TestPropulsionEfficiencies(self, propEffs: "IPropulsionEfficiencies"):
        propEffs.technology_level = AgEAvtrJetEngineTechnologyLevel.eLevel5
        Assert.assertEqual(AgEAvtrJetEngineTechnologyLevel.eLevel5, propEffs.technology_level)
        propEffs.intake_type = AgEAvtrJetEngineIntakeType.eSubsonicEmbedded
        Assert.assertEqual(AgEAvtrJetEngineIntakeType.eSubsonicEmbedded, propEffs.intake_type)
        propEffs.turbine_type = AgEAvtrJetEngineTurbineType.eUncooled
        Assert.assertEqual(AgEAvtrJetEngineTurbineType.eUncooled, propEffs.turbine_type)
        propEffs.exhaust_nozzle_type = AgEAvtrJetEngineExhaustNozzleType.eFixedAreaConvergent
        Assert.assertEqual(AgEAvtrJetEngineExhaustNozzleType.eFixedAreaConvergent, propEffs.exhaust_nozzle_type)

    def TestPropulsionEfficienciesRamScram(self, propEffs: "IPropulsionEfficiencies"):
        # This tests the propulsion efficiencies interface only for Ramjets and Scramjets as the enumeration values are more limited
        propEffs.technology_level = AgEAvtrJetEngineTechnologyLevel.eLevel5
        Assert.assertEqual(AgEAvtrJetEngineTechnologyLevel.eLevel5, propEffs.technology_level)
        Assert.assertEqual(AgEAvtrJetEngineIntakeType.eSupersonicEmbedded, propEffs.intake_type)

        def action412():
            turbineTypeTest: "AgEAvtrJetEngineTurbineType" = propEffs.turbine_type

        TryCatchAssertBlock.ExpectedException("turbine type", action412)
        Assert.assertEqual(
            AgEAvtrJetEngineExhaustNozzleType.eVariableAreaConvergentDivergent, propEffs.exhaust_nozzle_type
        )

    def TestFuelAFPROP(self, afprop: "IFuelModelKeroseneAFPROP"):
        afprop.subtype = AgEAvtrAFPROPFuelType.eAFPROPJetA
        Assert.assertEqual(AgEAvtrAFPROPFuelType.eAFPROPJetA, afprop.subtype)

        def action413():
            afprop.specific_energy = 40

        TryCatchAssertBlock.ExpectedException("must be", action413)

        afprop.subtype = AgEAvtrAFPROPFuelType.eAFPROPOverride
        afprop.specific_energy = 43.21
        Assert.assertEqual(43.21, afprop.specific_energy)

    def TestFuelCEA(self, cea: "IFuelModelKeroseneCEA"):
        cea.subtype = AgEAvtrCEAFuelType.eCEAJetA
        Assert.assertEqual(AgEAvtrCEAFuelType.eCEAJetA, cea.subtype)

        def action414():
            cea.specific_energy = 40

        TryCatchAssertBlock.ExpectedException("must be", action414)

        cea.subtype = AgEAvtrCEAFuelType.eCEAOverride
        cea.specific_energy = 43.21
        Assert.assertEqual(43.21, cea.specific_energy)

    def TestTurbofanBasicAB(self, prop: "IAdvFixedWingTurbofanBasicABProp"):
        prop.can_use_afterburner = False
        Assert.assertEqual(False, prop.can_use_afterburner)

        def action415():
            prop.afterburner_on = False

        TryCatchAssertBlock.ExpectedException("must be", action415)

        def action416():
            prop.max_afterburner_temp = 2000

        TryCatchAssertBlock.ExpectedException("must be", action416)

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

        prop.fuel_type = AgEAvtrJetFuelType.eHydrogen
        Assert.assertEqual(AgEAvtrJetFuelType.eHydrogen, prop.fuel_type)

        def action417():
            afprop: "IFuelModelKeroseneAFPROP" = prop.fuel_mode_as_afprop

        TryCatchAssertBlock.ExpectedException("must be", action417)

        def action418():
            cea: "IFuelModelKeroseneCEA" = prop.fuel_mode_as_cea

        TryCatchAssertBlock.ExpectedException("must be", action418)

        prop.fuel_type = AgEAvtrJetFuelType.eKeroseneAFPROP
        self.TestFuelAFPROP(prop.fuel_mode_as_afprop)
        prop.fuel_type = AgEAvtrJetFuelType.eKeroseneCEA
        self.TestFuelCEA(prop.fuel_mode_as_cea)

        self.TestPropulsionEfficiencies(prop.efficiencies_and_losses)

    def TestTurbojetBasicAB(self, prop: "IAdvFixedWingTurbojetBasicABProp"):
        prop.can_use_afterburner = False
        Assert.assertEqual(False, prop.can_use_afterburner)

        def action419():
            prop.afterburner_on = False

        TryCatchAssertBlock.ExpectedException("must be", action419)

        def action420():
            prop.max_afterburner_temp = 2000

        TryCatchAssertBlock.ExpectedException("must be", action420)

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

        prop.fuel_type = AgEAvtrJetFuelType.eHydrogen
        Assert.assertEqual(AgEAvtrJetFuelType.eHydrogen, prop.fuel_type)

        def action421():
            afprop: "IFuelModelKeroseneAFPROP" = prop.fuel_mode_as_afprop

        TryCatchAssertBlock.ExpectedException("must be", action421)

        def action422():
            cea: "IFuelModelKeroseneCEA" = prop.fuel_mode_as_cea

        TryCatchAssertBlock.ExpectedException("must be", action422)

        prop.fuel_type = AgEAvtrJetFuelType.eKeroseneAFPROP
        self.TestFuelAFPROP(prop.fuel_mode_as_afprop)
        prop.fuel_type = AgEAvtrJetFuelType.eKeroseneCEA
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

    def AltitudeOptions(self, alt: "IAltitudeOptions"):
        alt.use_default_cruise_altitude = True

        def action423():
            alt.altitude = 10000

        TryCatchAssertBlock.ExpectedException("must be ", action423)

        alt.use_default_cruise_altitude = False
        alt.altitude_reference = AgEAvtrAGLMSL.eAltAGL
        alt.altitude = 5000
        Assert.assertEqual(AgEAvtrAGLMSL.eAltAGL, alt.altitude_reference)
        Assert.assertEqual(5000, alt.altitude)

    def AltitudeMSLOptions(self, altitudeOpts: "IAltitudeMSLOptions"):
        altitudeOpts.use_default_cruise_altitude = True

        def action424():
            altitudeOpts.msl_altitude = 10000

        TryCatchAssertBlock.ExpectedException("must be ", action424)

        altitudeOpts.use_default_cruise_altitude = False
        altitudeOpts.msl_altitude = 10000
        Assert.assertEqual(10000, altitudeOpts.msl_altitude)

    def AltitudeMSLAndLevelOffOptions(self, altitudeOpts: "IAltitudeMSLAndLevelOffOptions"):
        altitudeOpts.use_default_cruise_altitude = True
        # TryCatchAssertBlock.ExpectedException("must be ", delegate () { altitudeOpts.MSLAltitude = 10000; });

        altitudeOpts.use_default_cruise_altitude = False
        altitudeOpts.msl_altitude = 10000
        Assert.assertEqual(10000, altitudeOpts.msl_altitude)

        altitudeOpts.must_level_off = False
        # TryCatchAssertBlock.ExpectedException("must be ", delegate () { altitudeOpts.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver; });
        altitudeOpts.must_level_off = True
        altitudeOpts.level_off_mode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, altitudeOpts.level_off_mode)

    def ArcAltitudeOptions(self, alt: "IArcAltitudeOptions"):
        alt.use_default_cruise_altitude = True

        def action425():
            alt.start_arc_altitude = 10001

        TryCatchAssertBlock.ExpectedException("must be ", action425)

        def action426():
            alt.stop_arc_altitude = 10002

        TryCatchAssertBlock.ExpectedException("must be ", action426)

        alt.use_default_cruise_altitude = False
        alt.start_arc_altitude = 10001
        Assert.assertEqual(10001, alt.start_arc_altitude)
        alt.stop_arc_altitude = 10002
        Assert.assertEqual(10002, alt.stop_arc_altitude)

    def ArcAltitudeAndDelayOptions(self, alt: "IArcAltitudeAndDelayOptions"):
        alt.use_default_cruise_altitude = True

        def action427():
            alt.delay_arc_climb_descents = True

        TryCatchAssertBlock.ExpectedException("must be ", action427)

        def action428():
            alt.start_arc_altitude = 10001

        TryCatchAssertBlock.ExpectedException("must be ", action428)

        def action429():
            alt.stop_arc_altitude = 10002

        TryCatchAssertBlock.ExpectedException("must be ", action429)

        alt.use_default_cruise_altitude = False
        alt.delay_arc_climb_descents = True
        Assert.assertTrue(alt.delay_arc_climb_descents)
        alt.start_arc_altitude = 10001
        Assert.assertEqual(10001, alt.start_arc_altitude)
        alt.stop_arc_altitude = 10002
        Assert.assertEqual(10002, alt.stop_arc_altitude)

    def HoverAltitudeOptions(self, alt: "IHoverAltitudeOptions"):
        alt.altitude_reference = AgEAvtrAGLMSL.eAltAGL
        Assert.assertEqual(AgEAvtrAGLMSL.eAltAGL, alt.altitude_reference)

        alt.altitude = 5000
        Assert.assertEqual(5000, alt.altitude)

        alt.final_altitude_rate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, alt.final_altitude_rate)

    def ArcOptions(self, arc: "IArcOptions"):
        arc.turn_direction = AgEAvtrTurnDirection.eTurnRight
        Assert.assertEqual(AgEAvtrTurnDirection.eTurnRight, arc.turn_direction)

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

    def NavigationOptions(self, navOpts: "INavigationOptions"):
        tolerance: float = 1e-09

        navOpts.nav_mode = AgEAvtrPointToPointMode.eArriveOnCourseForNext

        def action430():
            navOpts.arrive_on_course = 1

        TryCatchAssertBlock.ExpectedException("must be ", action430)

        def action431():
            navOpts.use_magnetic_heading = True

        TryCatchAssertBlock.ExpectedException("must be ", action431)

        navOpts.nav_mode = AgEAvtrPointToPointMode.eArriveOnCourse
        navOpts.arrive_on_course = 1
        navOpts.use_magnetic_heading = True
        course: typing.Any = navOpts.arrive_on_course
        Assert.assertAlmostEqual(1, float(course), delta=tolerance)
        Assert.assertTrue(navOpts.use_magnetic_heading)

    def EnrouteOptions(self, enrouteOpts: "IEnrouteOptions"):
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

    def EnrouteCruiseAirspeed(self, airspeedOpts: "ICruiseAirspeedOptions"):
        tolerance: float = 1e-09

        airspeedOpts.cruise_speed_type = AgEAvtrCruiseSpeed.eMaxAirspeed

        def action432():
            airspeedOpts.set_other_airspeed(AgEAvtrAirspeedType.eTAS, 200)

        TryCatchAssertBlock.ExpectedException("must be set", action432)

        airspeedOpts.cruise_speed_type = AgEAvtrCruiseSpeed.eOtherAirspeed
        airspeedOpts.set_other_airspeed(AgEAvtrAirspeedType.eTAS, 200)
        Assert.assertAlmostEqual(200, airspeedOpts.other_airspeed, delta=tolerance)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, airspeedOpts.other_airspeed_type)

        airspeedOpts.set_other_airspeed(AgEAvtrAirspeedType.eMach, 0.5)
        Assert.assertAlmostEqual(0.5, airspeedOpts.other_airspeed, delta=tolerance)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, airspeedOpts.other_airspeed_type)

    def EnrouteCruiseAirspeedAndProfile(self, airspeedOpts: "ICruiseAirspeedAndProfileOptions"):
        tolerance: float = 1e-09

        airspeedOpts.fly_cruise_airspeed_profile = False
        Assert.assertEqual(False, airspeedOpts.fly_cruise_airspeed_profile)

        airspeedOpts.cruise_speed_type = AgEAvtrCruiseSpeed.eMaxAirspeed

        def action433():
            airspeedOpts.set_other_airspeed(AgEAvtrAirspeedType.eTAS, 200)

        TryCatchAssertBlock.ExpectedException("must be set", action433)

        airspeedOpts.cruise_speed_type = AgEAvtrCruiseSpeed.eOtherAirspeed
        airspeedOpts.set_other_airspeed(AgEAvtrAirspeedType.eTAS, 200)
        Assert.assertAlmostEqual(200, airspeedOpts.other_airspeed, delta=tolerance)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, airspeedOpts.other_airspeed_type)

        airspeedOpts.set_other_airspeed(AgEAvtrAirspeedType.eMach, 0.5)
        Assert.assertAlmostEqual(0.5, airspeedOpts.other_airspeed, delta=tolerance)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, airspeedOpts.other_airspeed_type)

    def EnrouteTurnDirection(self, turnOpts: "IEnrouteTurnDirectionOptions"):
        turnOpts.enroute_first_turn = AgEAvtrNavigatorTurnDir.eNavigatorTurnLeft
        Assert.assertEqual(AgEAvtrNavigatorTurnDir.eNavigatorTurnLeft, turnOpts.enroute_first_turn)
        turnOpts.enroute_second_turn = AgEAvtrNavigatorTurnDir.eNavigatorTurnRight
        Assert.assertEqual(AgEAvtrNavigatorTurnDir.eNavigatorTurnRight, turnOpts.enroute_second_turn)

    def VerticalPlaneOptions(self, vertOpts: "IVerticalPlaneOptions"):
        vertOpts.max_vert_plane_radius_factor = 2.5
        Assert.assertEqual(2.5, vertOpts.max_vert_plane_radius_factor)
        vertOpts.min_enroute_flight_path_angle = -89.1
        minAng: typing.Any = vertOpts.min_enroute_flight_path_angle
        Assert.assertEqual(-89.1, float(minAng))
        vertOpts.max_enroute_flight_path_angle = 89.2
        maxAng: typing.Any = vertOpts.max_enroute_flight_path_angle
        Assert.assertEqual(89.2, float(maxAng))

    def VerticalPlaneAndFlightPathOptions(self, vertOpts: "IVerticalPlaneAndFlightPathOptions"):
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

    def ArcVerticalPlane(self, vertOpts: "IArcVerticalPlaneOptions"):
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
    def BasicManeuverAirspeedOptions(self, airspeedOptions: "IBasicManeuverAirspeedOptions"):
        airspeedMode: "AgEAvtrBasicManeuverAirspeedMode"
        for airspeedMode in Enum.GetValues(clr.TypeOf(AgEAvtrBasicManeuverAirspeedMode)):
            airspeedOptions.airspeed_mode = airspeedMode
            Assert.assertEqual(airspeedMode, airspeedOptions.airspeed_mode)
            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainCurrentAirspeed:
                airspeedOptions.maintain_airspeed_type = AgEAvtrAirspeedType.eMach
                Assert.assertEqual(AgEAvtrAirspeedType.eMach, airspeedOptions.maintain_airspeed_type)
                airspeedOptions.maintain_airspeed_type = AgEAvtrAirspeedType.eEAS
                Assert.assertEqual(AgEAvtrAirspeedType.eEAS, airspeedOptions.maintain_airspeed_type)
                airspeedOptions.maintain_airspeed_type = AgEAvtrAirspeedType.eCAS
                Assert.assertEqual(AgEAvtrAirspeedType.eCAS, airspeedOptions.maintain_airspeed_type)
                airspeedOptions.maintain_airspeed_type = AgEAvtrAirspeedType.eTAS
                Assert.assertEqual(AgEAvtrAirspeedType.eTAS, airspeedOptions.maintain_airspeed_type)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainSpecifiedAirspeed:
                airspeedOptions.specified_airspeed = 111
                Assert.assertEqual(111, airspeedOptions.specified_airspeed)

                airspeedOptions.specified_airspeed_type = AgEAvtrAirspeedType.eMach
                Assert.assertEqual(AgEAvtrAirspeedType.eMach, airspeedOptions.specified_airspeed_type)
                airspeedOptions.specified_airspeed_type = AgEAvtrAirspeedType.eEAS
                Assert.assertEqual(AgEAvtrAirspeedType.eEAS, airspeedOptions.specified_airspeed_type)
                airspeedOptions.specified_airspeed_type = AgEAvtrAirspeedType.eCAS
                Assert.assertEqual(AgEAvtrAirspeedType.eCAS, airspeedOptions.specified_airspeed_type)
                airspeedOptions.specified_airspeed_type = AgEAvtrAirspeedType.eTAS
                Assert.assertEqual(AgEAvtrAirspeedType.eTAS, airspeedOptions.specified_airspeed_type)

                airspeedOptions.specified_accel_decel_mode = AgEAvtrPerfModelOverride.ePerfModelValue
                Assert.assertEqual(AgEAvtrPerfModelOverride.ePerfModelValue, airspeedOptions.specified_accel_decel_mode)

                def action434():
                    airspeedOptions.specified_accel_decel_g = 200

                TryCatchAssertBlock.ExpectedException("must be set to override", action434)

                airspeedOptions.specified_accel_decel_mode = AgEAvtrPerfModelOverride.eOverride
                Assert.assertEqual(AgEAvtrPerfModelOverride.eOverride, airspeedOptions.specified_accel_decel_mode)

                airspeedOptions.specified_accel_decel_g = 200
                Assert.assertEqual(200, airspeedOptions.specified_accel_decel_g)

            if (
                (
                    (
                        (airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainMinAirspeed)
                        or (airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainMaxEnduranceAirspeed)
                    )
                    or (airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainMaxRangeAirspeed)
                )
                or (airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainMaxAirspeed)
            ) or (airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainMaxPerformanceAirspeed):

                def action435():
                    value: float = airspeedOptions.accel_g

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action435)

                def action436():
                    value: "AgEAvtrPerfModelOverride" = airspeedOptions.accel_mode

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action436)

                def action437():
                    value: float = airspeedOptions.decel_g

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action437)

                def action438():
                    value: "AgEAvtrPerfModelOverride" = airspeedOptions.decel_mode

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action438)

                def action439():
                    value: float = airspeedOptions.interpolate_end_g

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action439)

                def action440():
                    value: float = airspeedOptions.interpolate_end_time

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action440)

                def action441():
                    value: float = airspeedOptions.interpolate_init_g

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action441)

                def action442():
                    value: bool = airspeedOptions.interpolate_stop_at_end_time

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action442)

                def action443():
                    value: "AgEAvtrAirspeedType" = airspeedOptions.maintain_airspeed_type

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action443)

                def action444():
                    value: float = airspeedOptions.specified_accel_decel_g

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action444)

                def action445():
                    value: "AgEAvtrPerfModelOverride" = airspeedOptions.specified_accel_decel_mode

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action445)

                def action446():
                    value: float = airspeedOptions.specified_airspeed

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action446)

                def action447():
                    value: "AgEAvtrAirspeedType" = airspeedOptions.specified_airspeed_type

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action447)

                def action448():
                    value: float = airspeedOptions.throttle

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action448)

                def action449():
                    value: "IPropulsionThrust" = airspeedOptions.thrust

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action449)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eAccelAtG:
                airspeedOptions.accel_mode = AgEAvtrPerfModelOverride.ePerfModelValue
                Assert.assertEqual(AgEAvtrPerfModelOverride.ePerfModelValue, airspeedOptions.accel_mode)

                def action450():
                    airspeedOptions.accel_g = 300

                TryCatchAssertBlock.ExpectedException("must be set to override", action450)

                airspeedOptions.accel_mode = AgEAvtrPerfModelOverride.eOverride
                Assert.assertEqual(AgEAvtrPerfModelOverride.eOverride, airspeedOptions.accel_mode)

                airspeedOptions.accel_g = 300
                Assert.assertEqual(300, airspeedOptions.accel_g)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eDecelAtG:
                airspeedOptions.decel_mode = AgEAvtrPerfModelOverride.ePerfModelValue
                Assert.assertEqual(AgEAvtrPerfModelOverride.ePerfModelValue, airspeedOptions.decel_mode)

                def action451():
                    airspeedOptions.decel_g = 400

                TryCatchAssertBlock.ExpectedException("must be set to override", action451)

                airspeedOptions.decel_mode = AgEAvtrPerfModelOverride.eOverride
                Assert.assertEqual(AgEAvtrPerfModelOverride.eOverride, airspeedOptions.decel_mode)

                airspeedOptions.decel_g = 400
                Assert.assertEqual(400, airspeedOptions.decel_g)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eAccelDecelUnderGravity:
                pass

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eAccelDecelAeroProp:
                airspeedOptions.throttle = 55
                Assert.assertEqual(55, airspeedOptions.throttle)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eThrust:
                self.Test_IAgAvtrPropulsionThrust(airspeedOptions.thrust)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eInterpolateAccelDecel:
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

        airspeedOptions.min_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated, airspeedOptions.min_speed_limits
        )
        airspeedOptions.min_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated, airspeedOptions.min_speed_limits
        )
        airspeedOptions.min_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated, airspeedOptions.min_speed_limits
        )
        airspeedOptions.min_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated, airspeedOptions.min_speed_limits
        )

        airspeedOptions.max_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated, airspeedOptions.max_speed_limits
        )
        airspeedOptions.max_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated, airspeedOptions.max_speed_limits
        )
        airspeedOptions.max_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated, airspeedOptions.max_speed_limits
        )
        airspeedOptions.max_speed_limits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated, airspeedOptions.max_speed_limits
        )

    # endregion

    # region PrivateSiteMethods

    def TestSiteName(self, site: "ISite", name: str):
        Assert.assertEqual(name, site.name)
        site.name = "Name Test"
        Assert.assertEqual("Name Test", site.name)
        site.name = name

    def TestCatalogVTOLPoint(
        self, siteVTOLPointFromCatalog: "ISiteVTOLPointFromCatalog", catVTOLPoint: "ICatalogVTOLPoint"
    ):
        siteVTOLPointFromCatalog.set_catalog_vtol_point(catVTOLPoint)
        VTOLPointAsItem: "ICatalogItem" = clr.CastAs(catVTOLPoint, ICatalogItem)
        VTOLPointName: str = VTOLPointAsItem.name
        Assert.assertEqual(VTOLPointName, siteVTOLPointFromCatalog.get_as_site().name)
        catVTOLPoint2: "ICatalogItem" = clr.CastAs(siteVTOLPointFromCatalog.get_catalog_vtol_point(), ICatalogItem)
        Assert.assertEqual(VTOLPointName, catVTOLPoint2.name)

    def TestCatalogWaypoint(self, siteWaypointFromCatalog: "ISiteWaypointFromCatalog", catWaypoint: "ICatalogWaypoint"):
        siteWaypointFromCatalog.set_catalog_waypoint(catWaypoint)
        waypointAsItem: "ICatalogItem" = clr.CastAs(catWaypoint, ICatalogItem)
        waypointName: str = waypointAsItem.name
        Assert.assertEqual(waypointName, siteWaypointFromCatalog.get_as_site().name)
        catWaypoint2: "ICatalogItem" = clr.CastAs(siteWaypointFromCatalog.get_catalog_waypoint(), ICatalogItem)
        Assert.assertEqual(waypointName, catWaypoint2.name)

    # endregion
