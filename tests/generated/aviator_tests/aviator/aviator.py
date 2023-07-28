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

        scenario: IStkObject = clr.CastAs(TestBase.Application.CurrentScenario, IStkObject)
        EarlyBoundTests.AG_Scenario = TestBase.Application.CurrentScenario
        EarlyBoundTests.AG_AC = clr.Convert(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eAircraft, "AviatorAC")), IAircraft
        )
        # Set to Propagator to Aviator
        EarlyBoundTests.AG_AC.SetRouteType(AgEVePropagatorType.ePropagatorAviator)
        # Get the aircrafts route (still on the STKObjects side)
        aircraftRoute: IVehiclePropagatorAviator = clr.CastAs(EarlyBoundTests.AG_AC.Route, IVehiclePropagatorAviator)
        # Get the Aviator propagator
        EarlyBoundTests.AG_AvtrProp: IAviatorPropagator = clr.CastAs(aircraftRoute.AvtrPropagator, IAviatorPropagator)
        # Get the Aviator mission
        EarlyBoundTests.AG_Mission = EarlyBoundTests.AG_AvtrProp.AvtrMission
        # Get the phases
        EarlyBoundTests.AG_Phases = EarlyBoundTests.AG_Mission.Phases
        # Get the procedures
        EarlyBoundTests.AG_Procedures = EarlyBoundTests.AG_Phases[0].Procedures
        # Get the Aviator Catalog
        EarlyBoundTests.AG_AvtrCatalog = EarlyBoundTests.AG_AvtrProp.AvtrCatalog
        # Get the User Aircraft Models
        EarlyBoundTests.AG_AvtrAircraftModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.AircraftModels
        # Get the Aviator Aircraft
        EarlyBoundTests.AG_AvtrAircraft: IAircraftModel = clr.CastAs(EarlyBoundTests.AG_Mission.Vehicle, IAircraftModel)
        # Create a target object
        EarlyBoundTests.AG_Target = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eTarget, "Target")

        acModelsAsCatalogSource = EarlyBoundTests.AG_AvtrAircraftModels.GetAsCatalogSource()
        EarlyBoundTests.AG_AvtrAircraft = EarlyBoundTests.AG_AvtrAircraftModels.GetAircraft("NUNIT CSharp Test")
        # Assign the aircraft
        EarlyBoundTests.AG_Mission.Vehicle: IAviatorVehicle = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft, IAviatorVehicle
        )

        # Setting up Aviator Catalog databases
        arincPath = TestBase.GetScenarioFile("FAANFD18_SlimForTestOnly")
        EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.ARINC424Runways.MasterDataFilepath = arincPath
        EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.ARINC424Runways.GetAsCatalogSource().Save()

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
        Assert.assertEqual("NUNIT CSharp Test", EarlyBoundTests.AG_Mission.Vehicle.GetAsCatalogItem().Name)

    # endregion

    # region Configuration
    @category("Configuration Tests")
    def test_Configuration(self):
        acCopy: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        defConfig = acCopy.DefaultConfiguration

        defConfig.BaseDragIndex = 1
        Assert.assertEqual(1, defConfig.BaseDragIndex)

        defConfig.SetEmptyCG(1, 2, 3)
        Assert.assertEqual(1, defConfig.EmptyCGX)
        Assert.assertEqual(2, defConfig.EmptyCGY)
        Assert.assertEqual(3, defConfig.EmptyCGZ)

        defConfig2 = EarlyBoundTests.AG_AvtrAircraft.DefaultConfiguration
        Assert.assertEqual(0, defConfig2.EmptyCGX)
        Assert.assertEqual(0, defConfig2.EmptyCGY)
        Assert.assertEqual(0, defConfig2.EmptyCGZ)

        defConfig.PasteConfiguration(defConfig2)
        Assert.assertEqual(0, defConfig.EmptyCGX)
        Assert.assertEqual(0, defConfig.EmptyCGY)
        Assert.assertEqual(0, defConfig.EmptyCGZ)

        acCopy.GetAsCatalogItem().Remove()

    # endregion

    # region Stations
    @category("Configuration Tests")
    def test_Stations(self):
        acCopy: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        defConfig = acCopy.DefaultConfiguration

        stations = defConfig.GetStations()
        stationCount = Array.Length(stations.StationNames)

        totalCapacity = defConfig.TotalCapacity
        initialState = defConfig.InitialFuelState

        internalTank = stations.AddInternalFuelTank()
        stationCount += 1
        internalTank.Name = "Tank Name Test"
        Assert.assertTrue(stations.ContainsStation("Tank Name Test"))
        Assert.assertEqual("Tank Name Test", stations.StationNames[(stationCount - 1)])
        Assert.assertEqual(stationCount, stations.Count)

        internalTankSize = 2000
        internalTank.Capacity = internalTankSize
        internalTank.InitialFuelState = internalTankSize
        Assert.assertEqual((totalCapacity + internalTankSize), defConfig.TotalCapacity)
        Assert.assertEqual((initialState + internalTankSize), defConfig.InitialFuelState)

        stations.RemoveStationByName("Tank Name Test")
        stationCount -= 1
        Assert.assertEqual(stationCount, stations.Count)
        Assert.assertEqual(totalCapacity, defConfig.TotalCapacity)
        Assert.assertEqual(initialState, defConfig.InitialFuelState)

        payloadStation = stations.AddPayloadStation()
        stationCount += 1
        payloadStation.Name = "Payload Station Name Test"
        Assert.assertTrue(stations.ContainsStation("Payload Station Name Test"))
        Assert.assertEqual("Payload Station Name Test", stations.StationNames[(stationCount - 1)])
        Assert.assertEqual(stationCount, stations.Count)

        externalTank = payloadStation.AddExternalFuelTank()
        externalTankSize = 3000
        externalTank.Capacity = externalTankSize
        externalTank.InitialFuelState = externalTankSize
        # Need to save the aircraft to update these values.
        # Assert.AreEqual(totalCapacity + externalTankSize, defConfig.TotalCapacity);
        # Assert.AreEqual(initialState + externalTankSize, defConfig.InitialFuelState);

        payloadStation.RemoveSubItem()
        Assert.assertEqual(totalCapacity, defConfig.TotalCapacity)
        Assert.assertEqual(initialState, defConfig.InitialFuelState)

        # Check that the stations are always returned in alphabetical order
        stations.RemoveStationByName("Payload Station Name Test")
        Assert.assertEqual(0, stations.Count)

        currentTank = stations.AddInternalFuelTank()
        currentTank.Name = "4"
        currentTank = stations.AddInternalFuelTank()
        currentTank.Name = "1"
        currentPayloadStation = stations.AddPayloadStation()
        currentPayloadStation.Name = "3"
        currentPayloadStation = stations.AddPayloadStation()
        currentPayloadStation.Name = "2"
        currentPayloadStation = stations.AddPayloadStation()
        currentPayloadStation.Name = "1.5"
        currentPayloadStation = stations.AddPayloadStation()
        currentPayloadStation.Name = "Station 1"
        currentPayloadStation = stations.AddPayloadStation()
        currentPayloadStation.Name = "Station 2"

        Assert.assertEqual(7, stations.Count)

        Assert.assertEqual("1", stations.StationNames[0])
        Assert.assertEqual("1.5", stations.StationNames[1])
        Assert.assertEqual("2", stations.StationNames[2])
        Assert.assertEqual("3", stations.StationNames[3])
        Assert.assertEqual("4", stations.StationNames[4])
        Assert.assertEqual("Station 1", stations.StationNames[5])
        Assert.assertEqual("Station 2", stations.StationNames[6])

        tank: IFuelTankInternal = clr.CastAs(stations[0], IFuelTankInternal)
        Assert.assertEqual("1", tank.Name)
        station3: IPayloadStation = clr.CastAs(stations[3], IPayloadStation)
        Assert.assertEqual("3", station3.Name)

        def action1():
            testVal = stations[-1]

        TryCatchAssertBlock.ExpectedException("Invalid index", action1)

        def action2():
            testVal = stations[stations.Count]

        TryCatchAssertBlock.ExpectedException("Invalid index", action2)

        stations.RemoveAtIndex(3)
        Assert.assertEqual(6, stations.Count)
        Assert.assertEqual("2", stations.StationNames[2])
        Assert.assertEqual("4", stations.StationNames[3])

        def action3():
            stations.RemoveAtIndex(-1)

        TryCatchAssertBlock.ExpectedException("Invalid index", action3)

        def action4():
            stations.RemoveAtIndex(stations.Count)

        TryCatchAssertBlock.ExpectedException("Invalid index", action4)

        acCopy.GetAsCatalogItem().Remove()

    # endregion

    # region Wind
    @category("Weather Tests")
    @category("ExcludeOnLinux")
    def test_Wind(self):
        tolerance = 1e-09

        wind = EarlyBoundTests.AG_Mission.WindModel

        def action5():
            wind.WindModelSource = AgEAvtrWindAtmosModelSource.eProcedureModel

        TryCatchAssertBlock.ExpectedException("procedure model", action5)

        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.WindModelType = AgEAvtrWindModelType.eConstantWind

        def action6():
            addsWind = wind.ModeAsADDS

        TryCatchAssertBlock.ExpectedException("must be set", action6)

        constWind = wind.ModeAsConstant
        constWind.WindSpeed = 1
        Assert.assertAlmostEqual(1, constWind.WindSpeed, delta=tolerance)
        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eScenarioModel
        wind.WindModelType = AgEAvtrWindModelType.eConstantWind
        wind.Copy()
        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.Paste()

        Assert.assertAlmostEqual(0, constWind.WindSpeed, delta=tolerance)

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        procWind = proc1.WindModel
        procWind.WindModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        procConstWind = procWind.ModeAsConstant

        Assert.assertAlmostEqual(0, procConstWind.WindSpeed, delta=tolerance)

        def action7():
            procWind.WindModelType = AgEAvtrWindModelType.eConstantWind

        TryCatchAssertBlock.ExpectedException("cannot be edited from the procedure", action7)

        procWind.WindModelSource = AgEAvtrWindAtmosModelSource.eProcedureModel
        procWind.WindModelType = AgEAvtrWindModelType.eConstantWind
        procConstWind.WindSpeed = 1
        Assert.assertAlmostEqual(1, procConstWind.WindSpeed, delta=tolerance)

        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eScenarioModel
        wind.Copy()
        procWind.Paste()
        Assert.assertAlmostEqual(0, procConstWind.WindSpeed, delta=tolerance)

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region WindModelConstant
    @category("Weather Tests")
    def test_WindModelConstant(self):
        tolerance = 1e-09

        wind = EarlyBoundTests.AG_Mission.WindModel
        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.WindModelType = AgEAvtrWindModelType.eConstantWind
        constWind = wind.ModeAsConstant

        constWind.Name = "Constant Name Test"
        Assert.assertEqual("Constant Name Test", constWind.Name)
        constWind.WindSpeed = 1
        Assert.assertAlmostEqual(1, constWind.WindSpeed, delta=tolerance)

        wind.WindModelType = AgEAvtrWindModelType.eDisabled

        def action8():
            constWind.WindSpeed = 1

        TryCatchAssertBlock.ExpectedException("must be set", action8)

        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eScenarioModel
        wind.Copy()
        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.Paste()

    # endregion

    # region WindModelADDS
    @category("Weather Tests")
    @category("ExcludeOnLinux")
    def test_WindModelADDS(self):
        wind = EarlyBoundTests.AG_Mission.WindModel
        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.WindModelType = AgEAvtrWindModelType.eADDS
        ADDSWind = wind.ModeAsADDS

        ADDSWind.Name = "ADDS Name Test"
        Assert.assertEqual("ADDS Name Test", ADDSWind.Name)

        ADDSWind.InterpBlendTime = 1
        Assert.assertEqual(1, ADDSWind.InterpBlendTime)

        wind.WindModelType = AgEAvtrWindModelType.eDisabled

        def action9():
            ADDSWind.InterpBlendTime = 1

        TryCatchAssertBlock.ExpectedException("must be set", action9)

        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eScenarioModel
        wind.Copy()
        wind.WindModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        wind.Paste()

    # endregion

    # region Atmosphere
    @category("Weather Tests")
    def test_Atmosphere(self):
        atmos = EarlyBoundTests.AG_Mission.AtmosphereModel

        def action10():
            atmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eProcedureModel

        TryCatchAssertBlock.ExpectedException("procedure model", action10)

        atmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        basicAtmos = atmos.ModeAsBasic
        basicAtmos.BasicModelType = AgEAvtrAtmosphereModel.eStandard1976

        basicAtmos.UseNonStandardAtmosphere = True
        basicAtmos.Temperature = 300
        Assert.assertEqual(300, basicAtmos.Temperature)

        atmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eScenarioModel
        atmos.Copy()
        atmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        atmos.Paste()

        Assert.assertEqual(288.15, basicAtmos.Temperature)

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        procAtmos = proc1.AtmosphereModel
        procAtmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        procAtmosBasic = procAtmos.ModeAsBasic

        def action11():
            procAtmosBasic.UseNonStandardAtmosphere = True

        TryCatchAssertBlock.ExpectedException("cannot be edited from the procedure", action11)

        procAtmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eProcedureModel
        procAtmosBasic.UseNonStandardAtmosphere = True
        Assert.assertTrue(procAtmosBasic.UseNonStandardAtmosphere)

        atmos.Copy()
        procAtmos.Paste()
        Assert.assertFalse(procAtmosBasic.UseNonStandardAtmosphere)

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region BasicAtmosphereModel
    @category("Weather Tests")
    def test_BasicAtmosphereModel(self):
        atmos = EarlyBoundTests.AG_Mission.AtmosphereModel
        atmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        basicAtmos = atmos.ModeAsBasic
        basicAtmos.BasicModelType = AgEAvtrAtmosphereModel.eStandard1976

        Assert.assertEqual(288.15, basicAtmos.Temperature)

        def action12():
            basicAtmos.Temperature = 290

        TryCatchAssertBlock.ExpectedException("must be ", action12)
        basicAtmos.UseNonStandardAtmosphere = True
        basicAtmos.Temperature = 290
        Assert.assertEqual(290, basicAtmos.Temperature)

        atmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eScenarioModel
        atmos.Copy()
        atmos.AtmosphereModelSource = AgEAvtrWindAtmosModelSource.eMissionModel
        atmos.Paste()

    # endregion

    # region PhaseCollection
    @category("Mission Tests")
    def test_PhaseCollection(self):
        Assert.assertEqual(1, EarlyBoundTests.AG_Phases.Count)
        Assert.assertEqual("Phase 1", EarlyBoundTests.AG_Phases[0].Name)

        def action13():
            testVal = EarlyBoundTests.AG_Phases[-1]

        TryCatchAssertBlock.ExpectedException("Invalid index", action13)

        def action14():
            testVal = EarlyBoundTests.AG_Phases[EarlyBoundTests.AG_Phases.Count]

        TryCatchAssertBlock.ExpectedException("Invalid index", action14)

        phase2 = EarlyBoundTests.AG_Phases.Add()
        Assert.assertEqual(2, EarlyBoundTests.AG_Phases.Count)
        Assert.assertEqual("Phase 2", phase2.Name)

        phase0 = EarlyBoundTests.AG_Phases.AddAtIndex(0)
        phase0.Name = "Phase 0"
        Assert.assertEqual("Phase 0", EarlyBoundTests.AG_Phases[0].Name)

        def action15():
            EarlyBoundTests.AG_Phases.AddAtIndex(-1)

        TryCatchAssertBlock.ExpectedException("Invalid index", action15)

        def action16():
            EarlyBoundTests.AG_Phases.AddAtIndex((EarlyBoundTests.AG_Phases.Count + 1))

        TryCatchAssertBlock.ExpectedException("Invalid index", action16)

        countMinusOne = EarlyBoundTests.AG_Phases.Count - 1
        EarlyBoundTests.AG_Phases.Remove(phase0)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Phases.Count)
        Assert.assertEqual("Phase 1", EarlyBoundTests.AG_Phases[0].Name)

        def action17():
            EarlyBoundTests.AG_Phases.Remove(phase0)

        TryCatchAssertBlock.DoAssert2(action17)

        def action18():
            EarlyBoundTests.AG_Phases.RemoveAtIndex(-1)

        TryCatchAssertBlock.ExpectedException("Invalid index", action18)

        def action19():
            EarlyBoundTests.AG_Phases.RemoveAtIndex(EarlyBoundTests.AG_Phases.Count)

        TryCatchAssertBlock.ExpectedException("Invalid index", action19)

        EarlyBoundTests.AG_Phases.RemoveAtIndex(1)

        def action20():
            EarlyBoundTests.AG_Phases.RemoveAtIndex(0)

        TryCatchAssertBlock.ExpectedException("must be at least one phase", action20)

        def action21():
            EarlyBoundTests.AG_Phases.Remove(phase0)

        TryCatchAssertBlock.DoAssert2(action21)

        Assert.assertEqual(1, EarlyBoundTests.AG_Phases.Count)

    # endregion

    # region Phase
    @category("Mission Tests")
    def test_Phase(self):
        currentPhase = EarlyBoundTests.AG_Phases[0]

        currentPhase.Name = "My First Phase"
        Assert.assertEqual("My First Phase", EarlyBoundTests.AG_Phases[0].Name)
        currentPhase.Name = "Phase 1"

        def action22():
            testPerfModel = currentPhase.GetPerformanceModelByType("Test")

        TryCatchAssertBlock.ExpectedException("does not contain", action22)

        acc = currentPhase.GetPerformanceModelByType("Acceleration")

        Assert.assertEqual("Built-In Model", acc.Name)

        def action23():
            acc.Rename("Test")

        TryCatchAssertBlock.ExpectedException("cannot be renamed", action23)

        def action24():
            acc.Delete()

        TryCatchAssertBlock.ExpectedException("cannot be deleted", action24)
        Assert.assertTrue(acc.IsLinkedToCatalog)

        acc.LinkToCatalog("Built-In Model")
        Assert.assertEqual("Built-In Model", acc.Name)
        Assert.assertTrue(acc.IsLinkedToCatalog)
        basicAcc: IAircraftBasicAccelerationModel = clr.CastAs(acc.Properties, IAircraftBasicAccelerationModel)

        acc.CopyFromCatalog("Built-In Model")
        Assert.assertEqual("Built-In Model", acc.Name)
        Assert.assertEqual(False, acc.IsLinkedToCatalog)

        acc.CreateNew("Advanced Acceleration Model")
        name = acc.Name
        Assert.assertTrue(("Advanced Acceleration Model" in name))
        Assert.assertEqual(False, acc.IsLinkedToCatalog)
        advAcc: IAircraftAdvAccelerationModel = clr.CastAs(acc.Properties, IAircraftAdvAccelerationModel)

        acc.Rename("Test Rename")
        Assert.assertEqual("Test Rename", acc.Name)

        vtol = currentPhase.GetPerformanceModelByType("VTOL")

        vtol.Delete()

        def action25():
            vtol.Rename("Test")

        TryCatchAssertBlock.ExpectedException("no performance model", action25)

        def action26():
            vtol.Delete()

        TryCatchAssertBlock.ExpectedException("no performance model", action26)

        def action27():
            perfModel = vtol.Properties

        TryCatchAssertBlock.ExpectedException("no performance model", action27)

        def action28():
            isLinked = vtol.IsLinkedToCatalog

        TryCatchAssertBlock.ExpectedException("no performance model", action28)

        vtol.LinkToCatalog("AGI VTOL Model")
        Assert.assertTrue(vtol.IsLinkedToCatalog)
        unknownModel = vtol.Properties

        currentPhase.SetDefaultPerfModels()
        Assert.assertEqual("Built-In Model", acc.Name)

        def action29():
            currentPhase.PastePerformanceModels()

        TryCatchAssertBlock.ExpectedException("No copy", action29)

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        phase2 = EarlyBoundTests.AG_Phases.Add()
        proc2 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )

        acc.CreateNew("Advanced Acceleration Model")
        acc.Rename("Testing Copy Paste")
        Assert.assertEqual("Testing Copy Paste", acc.Name)
        currentPhase.CopyPerformanceModels()
        phase2.PastePerformanceModels()
        acc2 = phase2.GetPerformanceModelByType("Acceleration")
        Assert.assertEqual("Testing Copy Paste", acc2.Name)

        EarlyBoundTests.AG_Phases.Remove(phase2)
        currentPhase.Procedures.Remove(proc2)
        currentPhase.Procedures.Remove(proc1)

        missileTest = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels.AddMissile(
            "Missile Perf Model Test"
        )
        EarlyBoundTests.AG_Mission.Vehicle: IAviatorVehicle = clr.CastAs(missileTest, IAviatorVehicle)
        acc = currentPhase.GetPerformanceModelByType("Acceleration")

        def action30():
            perfModel = acc.Properties

        TryCatchAssertBlock.ExpectedException("", action30)

        rotorcraftTest = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.RotorcraftModels.AddRotorcraft(
            "Rotorcraft Perf Model Test"
        )
        EarlyBoundTests.AG_Mission.Vehicle: IAviatorVehicle = clr.CastAs(rotorcraftTest, IAviatorVehicle)
        acc = currentPhase.GetPerformanceModelByType("Acceleration")

        def action31():
            perfModel = acc.Properties

        TryCatchAssertBlock.ExpectedException("", action31)

        EarlyBoundTests.AG_Mission.Vehicle: IAviatorVehicle = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft, IAviatorVehicle
        )
        EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels.GetAsCatalogSource().RemoveChild(
            "Missile Perf Model Test"
        )
        EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.RotorcraftModels.GetAsCatalogSource().RemoveChild(
            "Rotorcraft Perf Model Test"
        )
        Assert.assertEqual(0, currentPhase.Procedures.Count)
        currentPhase.SetDefaultPerfModels()

    # endregion

    # region ProcedureCollection
    @category("Mission Tests")
    def test_ProcedureCollection(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        proc1.Name = "Procedure 1"
        Assert.assertEqual(1, EarlyBoundTests.AG_Procedures.Count)

        proc3 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )
        proc3.Name = "Procedure 3"

        proc2 = EarlyBoundTests.AG_Procedures.AddAtIndex(
            1, AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )
        proc2.Name = "Procedure 2"

        Assert.assertEqual("Procedure 2", EarlyBoundTests.AG_Procedures[1].Name)

        def action32():
            testVal = EarlyBoundTests.AG_Procedures[-1]

        TryCatchAssertBlock.ExpectedException("Invalid index", action32)

        def action33():
            testVal = EarlyBoundTests.AG_Procedures[EarlyBoundTests.AG_Procedures.Count]

        TryCatchAssertBlock.ExpectedException("Invalid index", action33)

        def action34():
            EarlyBoundTests.AG_Procedures.AddAtIndex(
                -1, AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
            )

        TryCatchAssertBlock.ExpectedException("Invalid index", action34)

        def action35():
            EarlyBoundTests.AG_Procedures.AddAtIndex(
                (EarlyBoundTests.AG_Procedures.Count + 1),
                AgEAvtrSiteType.eSiteEndOfPrevProcedure,
                AgEAvtrProcedureType.eProcEnroute,
            )

        TryCatchAssertBlock.ExpectedException("Invalid index", action35)

        def action36():
            EarlyBoundTests.AG_Procedures.RemoveAtIndex(-1)

        TryCatchAssertBlock.ExpectedException("Invalid index", action36)

        def action37():
            EarlyBoundTests.AG_Procedures.RemoveAtIndex(EarlyBoundTests.AG_Procedures.Count)

        TryCatchAssertBlock.ExpectedException("Invalid index", action37)

        countMinusOne = EarlyBoundTests.AG_Procedures.Count - 1
        EarlyBoundTests.AG_Procedures.RemoveAtIndex(1)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Procedures.Count)
        Assert.assertEqual("Procedure 3", EarlyBoundTests.AG_Procedures[1].Name)

        countMinusOne = EarlyBoundTests.AG_Procedures.Count - 1
        EarlyBoundTests.AG_Procedures.Remove(proc3)
        Assert.assertEqual(countMinusOne, EarlyBoundTests.AG_Procedures.Count)

        def action38():
            EarlyBoundTests.AG_Procedures.Remove(proc3)

        TryCatchAssertBlock.DoAssert2(action38)

        EarlyBoundTests.AG_Procedures.RemoveAtIndex(0)
        self.EmptyProcedures()

    # endregion

    # region ProcedureTimeOptions
    @category("Mission Tests")
    def test_ProcedureTimeOptions(self):
        tolerance = 1e-06

        self.EmptyProcedures()

        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        proc2 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )
        proc3 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicPointToPoint
        )
        proc4 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcLanding)

        # //////// TESTING TAKEOFF TIME OPTIONS /////////////
        timeOpts = proc1.TimeOptions
        Assert.assertTrue(timeOpts.StartTimeEnabled)
        Assert.assertTrue(timeOpts.InterruptTimeEnabled)
        Assert.assertEqual(False, timeOpts.StopTimeEnabled)

        timeOpts.SetStartTime(0)
        start = float(timeOpts.StartTime)
        Assert.assertEqual(0, start)
        timeOpts.SetStartTime((start + 1))
        start = float(timeOpts.StartTime)
        Assert.assertEqual(1, start)
        Assert.assertTrue(timeOpts.UseStartTime)
        timeOpts.UseStartTime = False
        Assert.assertEqual(False, timeOpts.UseStartTime)
        start = float(timeOpts.StartTime)
        Assert.assertEqual(0, start)

        oldTime = float(timeOpts.InterruptTime)
        timeOpts.SetInterruptTime((oldTime - 1))
        newTime = float(timeOpts.InterruptTime)
        Assert.assertEqual((oldTime - 1), newTime)
        Assert.assertTrue(timeOpts.UseInterruptTime)
        timeOpts.UseInterruptTime = False
        Assert.assertEqual(False, timeOpts.UseInterruptTime)
        newTime = float(timeOpts.InterruptTime)
        Assert.assertEqual(oldTime, newTime)

        Assert.assertEqual(False, timeOpts.UseStopTime)

        def action39():
            timeOpts.UseStopTime = True

        TryCatchAssertBlock.ExpectedException("not enabled", action39)

        def action40():
            timeOpts.SetStopTime(timeOpts.StopTime)

        TryCatchAssertBlock.ExpectedException("not enabled", action40)

        # //////// TESTING ENROUTE TIME OPTIONS /////////////

        timeOpts2 = proc2.TimeOptions
        Assert.assertEqual(False, timeOpts2.StartTimeEnabled)
        Assert.assertTrue(timeOpts2.InterruptTimeEnabled)
        Assert.assertTrue(timeOpts2.StopTimeEnabled)

        Assert.assertEqual(False, timeOpts2.UseStartTime)

        def action41():
            timeOpts2.UseStartTime = True

        TryCatchAssertBlock.ExpectedException("not enabled", action41)

        def action42():
            timeOpts2.SetStartTime(timeOpts2.StartTime)

        TryCatchAssertBlock.ExpectedException("not enabled", action42)

        oldTime = float(timeOpts2.InterruptTime)
        timeOpts2.SetInterruptTime((float(oldTime) - 1))
        newTime = float(timeOpts2.InterruptTime)
        Assert.assertEqual((float(oldTime) - 1), float(newTime))
        Assert.assertTrue(timeOpts2.UseInterruptTime)
        timeOpts2.UseInterruptTime = False
        Assert.assertEqual(False, timeOpts2.UseInterruptTime)
        newTime = float(timeOpts2.InterruptTime)
        Assert.assertEqual(float(oldTime), float(newTime))

        oldstopTime = float(timeOpts2.StopTime)
        timeOpts2.SetStopTime((oldstopTime - 1))
        newStopTime = float(timeOpts2.StopTime)
        Assert.assertEqual((oldstopTime - 1), newStopTime)
        Assert.assertTrue(timeOpts2.UseStopTime)
        timeOpts2.UseStopTime = False
        Assert.assertEqual(False, timeOpts2.UseStopTime)
        newStopTime = float(timeOpts2.StopTime)
        # The stop time doesn't go back to the original time until
        # the start time of the first procedure is rest
        Assert.assertAlmostEqual((oldstopTime - 1), newStopTime, delta=tolerance)
        timeOpts.SetStartTime(0)
        timeOpts.UseStartTime = False
        newStopTime = float(timeOpts2.StopTime)
        Assert.assertAlmostEqual(oldstopTime, newStopTime, delta=tolerance)

        # //////// TESTING BASIC POINT TO POINT TIME OPTIONS /////////////

        timeOpts3 = proc3.TimeOptions
        Assert.assertEqual(False, timeOpts3.StartTimeEnabled)
        Assert.assertTrue(timeOpts3.InterruptTimeEnabled)
        Assert.assertTrue(timeOpts3.StopTimeEnabled)

        # //////// TESTING LANDING TIME OPTIONS /////////////

        timeOpts4 = proc4.TimeOptions
        Assert.assertEqual(False, timeOpts4.StartTimeEnabled)
        Assert.assertTrue(timeOpts4.InterruptTimeEnabled)
        Assert.assertTrue(timeOpts4.StopTimeEnabled)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc1, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc3, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc4, IProcedure))
        TestBase.Application.UnitPreferences.ResetUnits()

    # endregion

    # region CalculationOptions
    @category("Mission Tests")
    def test_CalculationOptions(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)

        calcOpts = proc1.CalculationOptions

        calcOpts.MaxRelMotionFactor = 1.1
        Assert.assertEqual(1.1, calcOpts.MaxRelMotionFactor)
        calcOpts.StateCacheTimeInterval = 0.002
        Assert.assertEqual(0.002, calcOpts.StateCacheTimeInterval)

        calcOpts.TimeResolution = 0.003
        Assert.assertEqual(0.003, calcOpts.TimeResolution)
        calcOpts.MaxIterations = 54
        Assert.assertEqual(54, calcOpts.MaxIterations)
        calcOpts.MaxBadSteps = 5
        Assert.assertEqual(5, calcOpts.MaxBadSteps)

        calcOpts.IntegratorType = AgEAvtrNumericalIntegrator.eRK4
        Assert.assertEqual(AgEAvtrNumericalIntegrator.eRK4, calcOpts.IntegratorType)
        Assert.assertEqual("RK4", calcOpts.IntegratorTypeString)

        calcOpts.IntegratorTypeString = "RK45"
        Assert.assertEqual(AgEAvtrNumericalIntegrator.eRK45, calcOpts.IntegratorType)
        Assert.assertEqual("RK45", calcOpts.IntegratorTypeString)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc1, IProcedure))

    # endregion

    # region RefuelDump
    @category("Mission Tests")
    def test_RefuelDump(self):
        self.EmptyProcedures()

        # Procedure where Refuel/Dump is not supported

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        Assert.assertFalse(proc1.RefuelDumpIsSupported)
        rdp = proc1.RefuelDumpProperties

        def action43():
            rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eRefuelDumpDisabled, 0.0)

        TryCatchAssertBlock.ExpectedException("is not supported", action43)

        def action44():
            o = rdp.RefuelDumpMode

        TryCatchAssertBlock.ExpectedException("is not supported", action44)

        def action45():
            o = rdp.RefuelDumpModeValue

        TryCatchAssertBlock.ExpectedException("is not supported", action45)

        def action46():
            o = rdp.RefuelDumpRate

        TryCatchAssertBlock.ExpectedException("is not supported", action46)

        def action47():
            o = rdp.RefuelDumpTimeOffset

        TryCatchAssertBlock.ExpectedException("is not supported", action47)

        def action48():
            o = rdp.CanUseEndOfEnrouteSegmentAsEpoch

        TryCatchAssertBlock.ExpectedException("is not supported", action48)

        def action49():
            o = rdp.UseEndOfEnrouteSegmentAsEpoch

        TryCatchAssertBlock.ExpectedException("is not supported", action49)

        # Procedure where Refuel/Dump is supported

        proc2 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcArcEnroute)
        Assert.assertTrue(proc2.RefuelDumpIsSupported)
        rdp = proc2.RefuelDumpProperties

        rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eRefuelDumpDisabled, 1.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelDumpDisabled, rdp.RefuelDumpMode)
        Assert.assertEqual(1.0, rdp.RefuelDumpModeValue)  # "not applicable" in GUI

        rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eRefuelTopOff, 2.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelTopOff, rdp.RefuelDumpMode)
        Assert.assertEqual(2.0, rdp.RefuelDumpModeValue)  # "not applicable" in GUI

        rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eRefuelToFuelState, 3.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelToFuelState, rdp.RefuelDumpMode)
        Assert.assertEqual(3.0, rdp.RefuelDumpModeValue)

        rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eRefuelToWeight, 4.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelToWeight, rdp.RefuelDumpMode)
        Assert.assertEqual(4.0, rdp.RefuelDumpModeValue)

        rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eRefuelQuantity, 5.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eRefuelQuantity, rdp.RefuelDumpMode)
        Assert.assertEqual(5.0, rdp.RefuelDumpModeValue)

        rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eDumpToFuelState, 6.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eDumpToFuelState, rdp.RefuelDumpMode)
        Assert.assertEqual(6.0, rdp.RefuelDumpModeValue)

        rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eDumpToWeight, 7.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eDumpToWeight, rdp.RefuelDumpMode)
        Assert.assertEqual(7.0, rdp.RefuelDumpModeValue)

        rdp.SetRefuelDumpMode(AgEAvtrRefuelDumpMode.eDumpQuantity, 8.0)
        Assert.assertEqual(AgEAvtrRefuelDumpMode.eDumpQuantity, rdp.RefuelDumpMode)
        Assert.assertEqual(8.0, rdp.RefuelDumpModeValue)

        rdp.RefuelDumpRate = 10
        Assert.assertEqual(10, rdp.RefuelDumpRate)
        rdp.RefuelDumpRate = -11
        Assert.assertEqual(11, rdp.RefuelDumpRate)  # When set to negative number, sets to absolute val. Same as GUI.

        rdp.RefuelDumpTimeOffset = 20
        Assert.assertEqual(20, rdp.RefuelDumpTimeOffset)

        def action50():
            rdp.RefuelDumpTimeOffset = -22

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action50)

        Assert.assertFalse(rdp.CanUseEndOfEnrouteSegmentAsEpoch)

        rdp.UseEndOfEnrouteSegmentAsEpoch = False
        Assert.assertFalse(rdp.UseEndOfEnrouteSegmentAsEpoch)
        rdp.UseEndOfEnrouteSegmentAsEpoch = True
        Assert.assertTrue(rdp.UseEndOfEnrouteSegmentAsEpoch)

        # Procedure where CanUseEndOfEnrouteSegmentAsEpoch

        proc3 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcHoldingCircular
        )
        Assert.assertTrue(proc3.RefuelDumpIsSupported)
        rdp = proc3.RefuelDumpProperties

        Assert.assertTrue(rdp.CanUseEndOfEnrouteSegmentAsEpoch)

        rdp.UseEndOfEnrouteSegmentAsEpoch = False
        Assert.assertFalse(rdp.UseEndOfEnrouteSegmentAsEpoch)
        rdp.UseEndOfEnrouteSegmentAsEpoch = True
        Assert.assertTrue(rdp.UseEndOfEnrouteSegmentAsEpoch)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(proc2)
        EarlyBoundTests.AG_Procedures.Remove(proc3)

    # endregion

    # region ArcEnroute
    @category("Procedure Tests")
    def test_ArcEnroute(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        arcProc: IProcedureArcEnroute = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcArcEnroute
            ),
            IProcedureArcEnroute,
        )

        alt = arcProc.AltitudeOptions
        self.ArcAltitudeAndDelayOptions(alt)

        arc = arcProc.ArcOptions
        self.ArcOptions(arc)

        arcAirspeed = arcProc.ArcCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(arcAirspeed)

        enroute = arcProc.EnrouteOptions
        self.EnrouteAndDelayOptions(enroute)

        airspeed = arcProc.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(airspeed)

        turnOpts = arcProc.EnrouteTurnDirectionOptions
        self.EnrouteTurnDirection(turnOpts)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(arcProc, IProcedure))

    # endregion

    # region ArcPointToPoint
    @category("Procedure Tests")
    def test_ArcPointToPoint(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        arcProc: IProcedureArcPointToPoint = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcArcPointToPoint
            ),
            IProcedureArcPointToPoint,
        )

        alt = arcProc.AltitudeOptions
        self.ArcAltitudeOptions(alt)

        arc = arcProc.ArcOptions
        self.ArcOptions(arc)

        arcAirspeed = arcProc.ArcCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(arcAirspeed)

        enroute = arcProc.EnrouteOptions
        self.EnrouteOptions(enroute)

        airspeed = arcProc.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(airspeed)

        turnOpts = arcProc.EnrouteTurnDirectionOptions
        self.EnrouteTurnDirection(turnOpts)

        arcProc.FlyCruiseAirspeedProfile = False
        Assert.assertEqual(False, arcProc.FlyCruiseAirspeedProfile)

        vertOpts = arcProc.VerticalPlaneOptions
        self.ArcVerticalPlane(vertOpts)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(arcProc, IProcedure))

    # endregion

    # region AreaTargetSearch
    @category("Procedure Tests")
    def test_AreaTargetSearch(self):
        self.EmptyProcedures()

        areaTargetObj = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget")
        areaTargetProc: IProcedureAreaTargetSearch = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteSTKAreaTarget, AgEAvtrProcedureType.eProcAreaTargetSearch
            ),
            IProcedureAreaTargetSearch,
        )

        self.TestProcedureName(areaTargetProc.GetAsProcedure(), "AreaTargetSearch")
        self.AltitudeOptions(areaTargetProc.AltitudeOptions)
        self.EnrouteOptions(areaTargetProc.EnrouteOptions)
        self.EnrouteCruiseAirspeed(areaTargetProc.EnrouteCruiseAirspeedOptions)

        areaTargetProc.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeBasicPointToPoint
        Assert.assertEqual(AgEAvtrFlightLineProcType.eProcTypeBasicPointToPoint, areaTargetProc.ProcedureType)
        areaTargetProc.MaxSeparation = 0.2
        Assert.assertEqual(0.2, areaTargetProc.MaxSeparation)
        areaTargetProc.CourseMode = AgEAvtrSearchPatternCourseMode.eCourseModeLow
        Assert.assertEqual(AgEAvtrSearchPatternCourseMode.eCourseModeLow, areaTargetProc.CourseMode)
        areaTargetProc.FirstLegRetrograde = True
        Assert.assertTrue(areaTargetProc.FirstLegRetrograde)

        def action51():
            areaTargetProc.CentroidTrueCourse = 5

        TryCatchAssertBlock.ExpectedException("must be", action51)
        areaTargetProc.CourseMode = AgEAvtrSearchPatternCourseMode.eCourseModeOverride
        areaTargetProc.CentroidTrueCourse = 5
        course = areaTargetProc.CentroidTrueCourse
        Assert.assertEqual(5, float(course))

        areaTargetProc.FlyCruiseAirspeedProfile = False
        Assert.assertEqual(False, areaTargetProc.FlyCruiseAirspeedProfile)
        areaTargetProc.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeEnroute

        def action52():
            areaTargetProc.FlyCruiseAirspeedProfile = False

        TryCatchAssertBlock.ExpectedException("must be", action52)

        areaTargetProc.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeBasicPointToPoint

        def action53():
            areaTargetProc.MustLevelOff = True

        TryCatchAssertBlock.ExpectedException("must be", action53)

        def action54():
            areaTargetProc.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffAutomaticManeuver

        TryCatchAssertBlock.ExpectedException("must be", action54)
        areaTargetProc.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeEnroute
        areaTargetProc.MustLevelOff = True
        Assert.assertTrue(areaTargetProc.MustLevelOff)
        areaTargetProc.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, areaTargetProc.LevelOffMode)

        takeoffProc = EarlyBoundTests.AG_Procedures.AddAtIndex(
            0, AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff
        )
        areaTargetProc.CourseMode = AgEAvtrSearchPatternCourseMode.eCourseModeHigh
        EarlyBoundTests.AG_AvtrProp.Propagate()

        def action55():
            areaTargetProc.FirstLegRetrograde = True

        TryCatchAssertBlock.ExpectedException("must be", action55)

        areaTargetObj.Unload()
        EarlyBoundTests.AG_Procedures.Remove(takeoffProc)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(areaTargetProc, IProcedure))

    # endregion

    # region BasicPointToPoint
    @category("Procedure Tests")
    def test_BasicPointToPoint(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        p2p: IProcedureBasicPointToPoint = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicPointToPoint
            ),
            IProcedureBasicPointToPoint,
        )

        alt = p2p.AltitudeOptions
        self.AltitudeOptions(alt)

        nav = p2p.NavigationOptions
        self.NavigationOptions(nav)

        enroute = p2p.EnrouteOptions
        self.EnrouteOptions(enroute)

        airspeed = p2p.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeedAndProfile(airspeed)

        vert = p2p.VerticalPlaneOptions
        self.VerticalPlaneAndFlightPathOptions(vert)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(p2p, IProcedure))

    # endregion

    # region Delay
    @category("Procedure Tests")
    def test_Delay(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        delay: IProcedureDelay = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcDelay),
            IProcedureDelay,
        )

        delay.AltitudeMode = AgEAvtrDelayAltMode.eDelayDefaultCruiseAlt

        def action56():
            delay.Altitude = 5000

        TryCatchAssertBlock.ExpectedException("must be", action56)

        delay.AltitudeMode = AgEAvtrDelayAltMode.eDelayOverride
        delay.Altitude = 5000
        Assert.assertEqual(5000, delay.Altitude)

        airspeedOpts = delay.CruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(airspeedOpts)

        delay.TurnDirection = AgEAvtrNavigatorTurnDir.eNavigatorTurnRight
        Assert.assertEqual(AgEAvtrNavigatorTurnDir.eNavigatorTurnRight, delay.TurnDirection)
        delay.TurnRadiusFactor = 3
        Assert.assertEqual(3, delay.TurnRadiusFactor)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(delay, IProcedure))

    # endregion

    # region Enroute
    @category("Procedure Tests")
    def test_Enroute(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        enroute: IProcedureEnroute = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcEnroute
            ),
            IProcedureEnroute,
        )

        alt = enroute.AltitudeMSLOptions
        self.AltitudeMSLAndLevelOffOptions(alt)

        nav = enroute.NavigationOptions
        self.NavigationOptions(nav)

        enrouteOpts = enroute.EnrouteOptions
        self.EnrouteAndDelayOptions(enrouteOpts)

        airspeed = enroute.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(airspeed)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(enroute, IProcedure))

    # endregion

    # region ExternalEphemeris
    @category("Procedure Tests")
    def test_ExternalEphemeris(self):
        self.EmptyProcedures()

        extEphem: IProcedureExtEphem = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteReferenceState, AgEAvtrProcedureType.eProcExtEphem),
            IProcedureExtEphem,
        )

        proc = extEphem.GetAsProcedure()
        Assert.assertEqual("ExtEphem", proc.Name)

        def action57():
            d = extEphem.EphemerisFileDuration

        TryCatchAssertBlock.ExpectedException("No ephemeris file set", action57)

        extEphem.EphemerisFile = TestBase.GetScenarioFile("ExternalTestBFW.e")
        Assert.assertTrue(("ExternalTestBFW.e" in extEphem.EphemerisFile))
        Assert.assertAlmostEqual(799.26, extEphem.EphemerisFileDuration, delta=0.01)

        def action58():
            extEphem.EphemerisFile = TestBase.GetScenarioFile("bogus.e")

        TryCatchAssertBlock.ExpectedException("Invalid", action58)

        def action59():
            extEphem.EphemerisFile = TestBase.GetScenarioFile("Aircraft1.ac")

        TryCatchAssertBlock.ExpectedException("Invalid", action59)

        extEphem.FlightMode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightClimb
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightClimb, extEphem.FlightMode)
        extEphem.FlightMode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightCruise
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightCruise, extEphem.FlightMode)
        extEphem.FlightMode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightDescend
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeForwardFlightDescend, extEphem.FlightMode)
        extEphem.FlightMode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeLanding
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeLanding, extEphem.FlightMode)
        extEphem.FlightMode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeLandingWOW
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeLandingWOW, extEphem.FlightMode)
        extEphem.FlightMode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeTakeoff
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeTakeoff, extEphem.FlightMode)
        extEphem.FlightMode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeTakeoffWOW
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeTakeoffWOW, extEphem.FlightMode)
        extEphem.FlightMode = AgEAvtrExtEphemFlightMode.eExtEphemFlightModeVTOLHover
        Assert.assertEqual(AgEAvtrExtEphemFlightMode.eExtEphemFlightModeVTOLHover, extEphem.FlightMode)

        extEphem.UseStartDuration = False
        Assert.assertFalse(extEphem.UseStartDuration)

        def action60():
            extEphem.StartTime = 100

        TryCatchAssertBlock.ExpectedException("not writeable", action60)

        def action61():
            extEphem.Duration = 200

        TryCatchAssertBlock.ExpectedException("not writeable", action61)

        extEphem.UseStartDuration = True
        Assert.assertTrue(extEphem.UseStartDuration)

        extEphem.StartTime = 100
        Assert.assertAlmostEqual(100, extEphem.StartTime, delta=extEphem.StartTime)

        def action62():
            extEphem.StartTime = -100

        TryCatchAssertBlock.ExpectedException("must be non-negative", action62)

        extEphem.Duration = 200
        Assert.assertAlmostEqual(200, extEphem.Duration, delta=extEphem.Duration)

        def action63():
            extEphem.Duration = -200

        TryCatchAssertBlock.ExpectedException("must be non-negative", action63)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(extEphem, IProcedure))

    # endregion

    # region FlightLine
    @category("Procedure Tests")
    def test_FlightLine(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        flightLine: IProcedureFlightLine = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcFlightLine
            ),
            IProcedureFlightLine,
        )

        alt = flightLine.AltitudeOptions
        self.AltitudeOptions(alt)

        flightAirspeed = flightLine.FlightLineAirspeedOptions
        self.EnrouteCruiseAirspeed(flightAirspeed)

        enroute = flightLine.EnrouteOptions
        self.EnrouteOptions(enroute)

        turnOpts = flightLine.EnrouteTurnDirectionOptions
        self.EnrouteTurnDirection(turnOpts)

        airspeed = flightLine.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(airspeed)

        flightLine.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeTerrainFollow
        flightLine.OutboundCourse = 5
        course = flightLine.OutboundCourse
        Assert.assertEqual(5, float(course))
        flightLine.UseMagneticHeading = True
        Assert.assertTrue(flightLine.UseMagneticHeading)
        flightLine.LegLength = 11
        Assert.assertEqual(11, flightLine.LegLength)

        flightLine.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeTerrainFollow

        def action64():
            flightLine.FlyCruiseAirspeedProfile = False

        TryCatchAssertBlock.ExpectedException("must be", action64)

        def action65():
            flightLine.MustLevelOff = False

        TryCatchAssertBlock.ExpectedException("must be", action65)

        def action66():
            flightLine.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffAutomaticManeuver

        TryCatchAssertBlock.ExpectedException("must be", action66)

        flightLine.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeBasicPointToPoint
        flightLine.FlyCruiseAirspeedProfile = False
        Assert.assertEqual(False, flightLine.FlyCruiseAirspeedProfile)

        flightLine.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeEnroute
        flightLine.MustLevelOff = True
        Assert.assertTrue(flightLine.MustLevelOff)
        flightLine.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, flightLine.LevelOffMode)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(flightLine, IProcedure))

    # endregion

    # region FormationFlyer
    @category("Procedure Tests")
    def test_FormationFlyer(self):
        TestBase.LoadTestScenario(Path.Combine("AviatorTests", "Formation_Flyer", "Scenario1.sc"))
        EarlyBoundTests.AG_Scenario = TestBase.Application.CurrentScenario
        EarlyBoundTests.AG_AC = clr.Convert((EarlyBoundTests.AG_Scenario.Children.GetItemByName("Wingman")), IAircraft)
        aircraftRoute: IVehiclePropagatorAviator = clr.CastAs(EarlyBoundTests.AG_AC.Route, IVehiclePropagatorAviator)
        EarlyBoundTests.AG_AvtrProp: IAviatorPropagator = clr.CastAs(aircraftRoute.AvtrPropagator, IAviatorPropagator)
        EarlyBoundTests.AG_Mission = EarlyBoundTests.AG_AvtrProp.AvtrMission
        EarlyBoundTests.AG_Phases = EarlyBoundTests.AG_Mission.Phases
        EarlyBoundTests.AG_Procedures = EarlyBoundTests.AG_Phases[0].Procedures

        EarlyBoundTests.AG_Procedures.RemoveAtIndex(2)  # Remove existing Formation Flyer procedure.

        formationFlyer: IProcedureFormationFlyer = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcFormationFlyer
            ),
            IProcedureFormationFlyer,
        )

        formationFlyer.CrossRangeCloseRate = 10
        Assert.assertEqual(10, formationFlyer.CrossRangeCloseRate)

        def action67():
            formationFlyer.CrossRangeCloseRate = -10

        TryCatchAssertBlock.ExpectedException("out of range", action67)  # Can be set. Should be invalid.

        formationFlyer.InitialCloseMaxSpeedAdvantage = 20
        Assert.assertEqual(20, formationFlyer.InitialCloseMaxSpeedAdvantage)

        def action68():
            formationFlyer.InitialCloseMaxSpeedAdvantage = -20

        TryCatchAssertBlock.ExpectedException("out of bounds", action68)  # Can be set. Should be invalid.

        formationFlyer.MaxTimeStep = 2
        Assert.assertEqual(2, formationFlyer.MaxTimeStep)
        formationFlyer.MaxTimeStep = 1
        Assert.assertEqual(1, formationFlyer.MaxTimeStep)

        def action69():
            formationFlyer.MaxTimeStep = 0

        TryCatchAssertBlock.ExpectedException("out of bounds", action69)  # Can be set. Should be invalid.

        formationFlyer.MinTimeStep = 0.2
        Assert.assertEqual(0.2, formationFlyer.MinTimeStep)
        formationFlyer.MinTimeStep = 0.1
        Assert.assertEqual(0.1, formationFlyer.MinTimeStep)

        def action70():
            formationFlyer.MinTimeStep = 0

        TryCatchAssertBlock.ExpectedException("out of bounds", action70)

        for stopCond in Enum.GetValues(clr.TypeOf(AgEAvtrFormationFlyerStopCondition)):
            formationFlyer.StopCondition = stopCond
            Assert.assertEqual(stopCond, formationFlyer.StopCondition)
            if AgEAvtrFormationFlyerStopCondition.eFormationFlyerStopAfterTime == stopCond:
                formationFlyer.StopTime = 30
                Assert.assertEqual(30, formationFlyer.StopTime)

                def action71():
                    formationFlyer.StopTime = -30

                TryCatchAssertBlock.ExpectedException("out of bounds", action71)

                def action72():
                    formationFlyer.StopDownRange = 40

                TryCatchAssertBlock.ExpectedException("Cannot set", action72)

                def action73():
                    formationFlyer.StopFuelState = 50

                TryCatchAssertBlock.ExpectedException("Cannot set", action73)

            elif AgEAvtrFormationFlyerStopCondition.eFormationFlyerStopAfterDownRange == stopCond:

                def action74():
                    formationFlyer.StopTime = 30

                TryCatchAssertBlock.ExpectedException("Cannot set", action74)

                formationFlyer.StopDownRange = 40
                Assert.assertEqual(40, formationFlyer.StopDownRange)

                def action75():
                    formationFlyer.StopDownRange = -40

                TryCatchAssertBlock.ExpectedException("out of bounds", action75)

                def action76():
                    formationFlyer.StopFuelState = 50

                TryCatchAssertBlock.ExpectedException("Cannot set", action76)

            elif AgEAvtrFormationFlyerStopCondition.eFormationFlyerStopAfterFuelState == stopCond:

                def action77():
                    formationFlyer.StopTime = 30

                TryCatchAssertBlock.ExpectedException("Cannot set", action77)

                def action78():
                    formationFlyer.StopDownRange = 40

                TryCatchAssertBlock.ExpectedException("Cannot set", action78)

                formationFlyer.StopFuelState = 50
                Assert.assertEqual(50, formationFlyer.StopFuelState)

                def action79():
                    formationFlyer.StopFuelState = -50

                TryCatchAssertBlock.ExpectedException("out of bounds", action79)

            else:

                def action80():
                    formationFlyer.StopTime = 30

                TryCatchAssertBlock.ExpectedException("Cannot set", action80)

                def action81():
                    formationFlyer.StopDownRange = 40

                TryCatchAssertBlock.ExpectedException("Cannot set", action81)

                def action82():
                    formationFlyer.StopFuelState = 50

                TryCatchAssertBlock.ExpectedException("Cannot set", action82)

        EarlyBoundTests.InitHelper()

    # endregion

    # region FormationRecover
    @category("Procedure Tests")
    def test_FormationRecover(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        EarlyBoundTests.AG_AvtrProp.Propagate()

        acObj: IStkObject = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj = acObj.CopyObject("AC2")
        ac2: IAircraft = clr.CastAs(ac2Obj, IAircraft)
        route2: IVehiclePropagatorAviator = clr.CastAs(ac2.Route, IVehiclePropagatorAviator)
        prop2: IAviatorPropagator = clr.CastAs(route2.AvtrPropagator, IAviatorPropagator)
        mission2 = prop2.AvtrMission
        phases2 = mission2.Phases
        procedures2 = phases2[0].Procedures

        proc2 = procedures2.Add(AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingCircular)
        prop2.Propagate()

        formRecov: IProcedureFormationRecover = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcFormationRecover
            ),
            IProcedureFormationRecover,
        )

        self.TestProcedureName(formRecov.GetAsProcedure(), "Formation/Recover")

        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        TestBase.Application.UnitPreferences.SetCurrentUnit("Duration", "Sec")
        formRecov.StartTime = 2
        startTime = formRecov.StartTime
        Assert.assertEqual(2, float(startTime))

        minTime = formRecov.GetMinimumTime(False)
        maxTime = formRecov.MaximumTime
        Assert.assertEqual(0, float(minTime))
        firstStartTime = formRecov.FindFirstValidStartTime(minTime, maxTime, 30)
        startTime = formRecov.StartTime
        Assert.assertEqual(float(startTime), float(firstStartTime))

        Assert.assertTrue(("Center" == str(formRecov.FormationPoint)))
        formRecov.FormationPoint = "Missile SubPoint(Detic)"
        Assert.assertTrue(("Missile SubPoint(Detic)" == str(formRecov.FormationPoint)))
        formRecov.InterpolatePointPosVel = True
        Assert.assertTrue(formRecov.InterpolatePointPosVel)

        formRecov.AltitudeOffset = 5
        Assert.assertEqual(5, formRecov.AltitudeOffset)
        formRecov.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowTakeoff

        def action83():
            formRecov.OverrideFuelFlowValue = 123

        TryCatchAssertBlock.ExpectedException("must be", action83)
        formRecov.ConsiderAccelForFuelFlow = True
        Assert.assertTrue(formRecov.ConsiderAccelForFuelFlow)

        formRecov.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowOverride
        formRecov.OverrideFuelFlowValue = 123
        Assert.assertAlmostEqual(123, formRecov.OverrideFuelFlowValue, delta=tolerance)

        def action84():
            formRecov.ConsiderAccelForFuelFlow = True

        TryCatchAssertBlock.ExpectedException("must be", action84)

        formRecov.FirstPause = 1
        Assert.assertEqual(1, formRecov.FirstPause)
        formRecov.TransitionTime = 2
        Assert.assertEqual(2, formRecov.TransitionTime)
        formRecov.SecondPause = 3
        Assert.assertEqual(3, formRecov.SecondPause)
        formRecov.DisplayStepTime = 4
        Assert.assertEqual(4, formRecov.DisplayStepTime)

        formRecov.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff
        Assert.assertEqual(AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff, formRecov.FlightMode)

        formRecov.FlightPathAngle = 5
        angle = formRecov.FlightPathAngle
        Assert.assertEqual(5, float(angle))
        formRecov.RadiusFactor = 2
        Assert.assertEqual(2, formRecov.RadiusFactor)

        formRecov.UseDelay = True
        Assert.assertTrue(formRecov.UseDelay)
        formRecov.DelayTurnDir = AgEAvtrDelayTurnDir.eDelayTurnLeft
        Assert.assertEqual(AgEAvtrDelayTurnDir.eDelayTurnLeft, formRecov.DelayTurnDir)
        formRecov.UseDelay = False

        def action85():
            formRecov.DelayTurnDir = AgEAvtrDelayTurnDir.eDelayTurnLeft

        TryCatchAssertBlock.ExpectedException("must be", action85)

        formRecov.UseDelay = False

        def action86():
            airspeed = formRecov.DelayCruiseAirspeedOptions

        TryCatchAssertBlock.ExpectedException("must be", action86)
        formRecov.UseDelay = True
        self.EnrouteCruiseAirspeed(formRecov.DelayCruiseAirspeedOptions)

        self.EnrouteOptions(formRecov.EnrouteOptions)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_AvtrProp.Propagate()

        def action87():
            formRecov.FindFirstValidStartTime(minTime, maxTime, 30)

        TryCatchAssertBlock.ExpectedException("first procedure", action87)

        def action88():
            formRecov.FlightPathAngle = 1

        TryCatchAssertBlock.ExpectedException("first procedure", action88)

        def action89():
            formRecov.RadiusFactor = 1

        TryCatchAssertBlock.ExpectedException("first procedure", action89)

        def action90():
            formRecov.UseDelay = True

        TryCatchAssertBlock.ExpectedException("first procedure", action90)

        def action91():
            formRecov.DelayTurnDir = AgEAvtrDelayTurnDir.eDelayTurnAuto

        TryCatchAssertBlock.ExpectedException("first procedure", action91)

        def action92():
            enrouteOpts = formRecov.EnrouteOptions

        TryCatchAssertBlock.ExpectedException("first procedure", action92)

        def action93():
            airspeed = formRecov.DelayCruiseAirspeedOptions

        TryCatchAssertBlock.ExpectedException("first procedure", action93)

        formRecov.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL
        Assert.assertEqual(formRecov.FlightMode, AgEAvtrPhaseOfFlight.eFlightPhaseVTOL)
        formRecov.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(formRecov.FuelFlowType, AgEAvtrFuelFlowType.eFuelFlowVTOL)
        currentPhase = EarlyBoundTests.AG_Phases[0]
        vtol = currentPhase.GetPerformanceModelByType("VTOL")
        vtol.Delete()

        def action94():
            formRecov.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action94)

        def action95():
            formRecov.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action95)

        currentPhase.SetDefaultPerfModels()
        TestBase.Application.UnitPreferences.ResetUnits()
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(formRecov, IProcedure))
        ac2Obj.Unload()

    # endregion

    # region HoldingCircular
    @category("Procedure Tests")
    def test_HoldingCircular(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        holdingProc: IProcedureHoldingCircular = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingCircular
            ),
            IProcedureHoldingCircular,
        )

        alt = holdingProc.AltitudeOptions
        self.AltitudeMSLOptions(alt)

        holdAirspeed = holdingProc.HoldCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts = holdingProc.EnrouteOptions
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts = holdingProc.EnrouteTurnDirectionOptions
        self.EnrouteTurnDirection(turnOpts)

        airspeed = holdingProc.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.ProfileMode = AgEAvtrHoldingProfileMode.eSTK8Compatible
        Assert.assertEqual(AgEAvtrHoldingProfileMode.eSTK8Compatible, holdingProc.ProfileMode)

        holdingProc.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, holdingProc.LevelOffMode)

        holdingProc.Bearing = 5
        angle = holdingProc.Bearing
        Assert.assertEqual(5, float(angle))
        holdingProc.UseMagneticHeading = False
        Assert.assertEqual(False, holdingProc.UseMagneticHeading)

        holdingProc.Range = 11
        Assert.assertEqual(11, holdingProc.Range)
        holdingProc.Diameter = 15
        Assert.assertEqual(15, holdingProc.Diameter)

        def action96():
            holdingProc.Diameter = 0.01

        TryCatchAssertBlock.ExpectedException("minimum diameter", action96)

        holdingProc.UseAlternateEntryPoints = True
        Assert.assertTrue(holdingProc.UseAlternateEntryPoints)
        holdingProc.TurnDirection = AgEAvtrHoldingDirection.eOutboundRightTurn
        Assert.assertEqual(AgEAvtrHoldingDirection.eOutboundRightTurn, holdingProc.TurnDirection)
        holdingProc.Turns = 3
        Assert.assertEqual(3, holdingProc.Turns)
        holdingProc.RefuelDumpMode = AgEAvtrHoldRefuelDumpMode.eImmediateExit
        Assert.assertEqual(AgEAvtrHoldRefuelDumpMode.eImmediateExit, holdingProc.RefuelDumpMode)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region HoldingFigure8
    @category("Procedure Tests")
    def test_HoldingFigure8(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        holdingProc: IProcedureHoldingFigure8 = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingFigure8
            ),
            IProcedureHoldingFigure8,
        )

        Assert.assertTrue((clr.Is(holdingProc, IProcedure)))

        alt = holdingProc.AltitudeOptions
        self.AltitudeMSLOptions(alt)

        holdAirspeed = holdingProc.HoldCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts = holdingProc.EnrouteOptions
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts = holdingProc.EnrouteTurnDirectionOptions
        self.EnrouteTurnDirection(turnOpts)

        airspeed = holdingProc.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.ProfileMode = AgEAvtrHoldingProfileMode.eSTK8Compatible
        Assert.assertEqual(AgEAvtrHoldingProfileMode.eSTK8Compatible, holdingProc.ProfileMode)

        holdingProc.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, holdingProc.LevelOffMode)

        holdingProc.Bearing = 5
        angle = holdingProc.Bearing
        Assert.assertEqual(5, float(angle))
        holdingProc.UseMagneticHeading = False
        Assert.assertEqual(False, holdingProc.UseMagneticHeading)

        holdingProc.Range = 11
        Assert.assertEqual(11, holdingProc.Range)
        holdingProc.Width = 14
        Assert.assertEqual(14, holdingProc.Width)
        holdingProc.Length = 15
        Assert.assertEqual(15, holdingProc.Length)

        def action97():
            holdingProc.Width = 0.01

        TryCatchAssertBlock.ExpectedException("minimum diameter", action97)

        def action98():
            holdingProc.Length = 0.01

        TryCatchAssertBlock.ExpectedException("minimum diameter", action98)

        def action99():
            holdingProc.Length = 13

        TryCatchAssertBlock.ExpectedException("must be", action99)

        holdingProc.UseAlternateEntryPoints = True
        Assert.assertTrue(holdingProc.UseAlternateEntryPoints)
        holdingProc.Turns = 3
        Assert.assertEqual(3, holdingProc.Turns)
        holdingProc.RefuelDumpMode = AgEAvtrHoldRefuelDumpMode.eImmediateExit
        Assert.assertEqual(AgEAvtrHoldRefuelDumpMode.eImmediateExit, holdingProc.RefuelDumpMode)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region HoldingRacetrack
    @category("Procedure Tests")
    def test_HoldingRacetrack(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        holdingProc: IProcedureHoldingRacetrack = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingRacetrack
            ),
            IProcedureHoldingRacetrack,
        )

        alt = holdingProc.AltitudeOptions
        self.AltitudeMSLOptions(alt)

        holdAirspeed = holdingProc.HoldCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(holdAirspeed)

        enrouteOpts = holdingProc.EnrouteOptions
        self.EnrouteAndDelayOptions(enrouteOpts)

        turnOpts = holdingProc.EnrouteTurnDirectionOptions
        self.EnrouteTurnDirection(turnOpts)

        airspeed = holdingProc.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeed(airspeed)

        holdingProc.ProfileMode = AgEAvtrHoldingProfileMode.eSTK8Compatible
        Assert.assertEqual(AgEAvtrHoldingProfileMode.eSTK8Compatible, holdingProc.ProfileMode)

        holdingProc.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, holdingProc.LevelOffMode)

        holdingProc.Bearing = 5
        angle = holdingProc.Bearing
        Assert.assertEqual(5, float(angle))
        holdingProc.UseMagneticHeading = False
        Assert.assertEqual(False, holdingProc.UseMagneticHeading)

        holdingProc.Range = 11
        Assert.assertEqual(11, holdingProc.Range)
        holdingProc.Width = 14
        Assert.assertEqual(14, holdingProc.Width)
        holdingProc.Length = 15
        Assert.assertEqual(15, holdingProc.Length)

        def action100():
            holdingProc.Width = 0.01

        TryCatchAssertBlock.ExpectedException("minimum diameter", action100)

        holdingProc.EntryManeuver = AgEAvtrHoldingEntryManeuver.eUseAlternateEntryPoints
        Assert.assertEqual(AgEAvtrHoldingEntryManeuver.eUseAlternateEntryPoints, holdingProc.EntryManeuver)
        holdingProc.Turns = 3
        Assert.assertEqual(3, holdingProc.Turns)
        holdingProc.RefuelDumpMode = AgEAvtrHoldRefuelDumpMode.eImmediateExit
        Assert.assertEqual(AgEAvtrHoldRefuelDumpMode.eImmediateExit, holdingProc.RefuelDumpMode)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(holdingProc, IProcedure))

    # endregion

    # region Hover
    @category("Procedure Tests")
    def test_Hover(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        proc2 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToHover
        )
        hoverProc: IProcedureHover = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHover),
            IProcedureHover,
        )

        alt = hoverProc.AltitudeOptions
        self.HoverAltitudeOptions(alt)

        hoverProc.HoverMode = AgEAvtrHoverMode.eHoverModeFixedTime
        Assert.assertEqual(AgEAvtrHoverMode.eHoverModeFixedTime, hoverProc.HoverMode)
        hoverProc.FixedTime = "00:00:20.000"
        fixedtime = hoverProc.FixedTime
        Assert.assertTrue(("00:00:20.000" == str(fixedtime)))

        def action101():
            hoverProc.HeadingMode = AgEAvtrVTOLHeadingMode.eHeadingAlignTranslationCourse

        TryCatchAssertBlock.ExpectedException("must be", action101)

        def action102():
            hoverProc.SetAbsoluteCourse(5, False)

        TryCatchAssertBlock.ExpectedException("must be", action102)

        def action103():
            hoverProc.SetRelativeCourse(4)

        TryCatchAssertBlock.ExpectedException("must be", action103)

        def action104():
            hoverProc.SetFinalTranslationCourse()

        TryCatchAssertBlock.ExpectedException("must be", action104)

        def action105():
            hoverProc.FinalHeadingRate = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action105)

        def action106():
            hoverProc.TranslationMode = AgEAvtrVTOLTranslationMode.eComeToStop

        TryCatchAssertBlock.ExpectedException("must be", action106)

        def action107():
            hoverProc.Bearing = 6

        TryCatchAssertBlock.ExpectedException("must be", action107)

        def action108():
            hoverProc.UseMagneticBearing = True

        TryCatchAssertBlock.ExpectedException("must be", action108)

        def action109():
            hoverProc.Range = 7

        TryCatchAssertBlock.ExpectedException("must be", action109)

        def action110():
            hoverProc.FinalCourseMode = AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation

        TryCatchAssertBlock.ExpectedException("must be", action110)

        def action111():
            hoverProc.SmoothTranslationMode = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action111)

        def action112():
            hoverProc.RadiusFactor = 3

        TryCatchAssertBlock.ExpectedException("must be", action112)

        hoverProc.HoverMode = AgEAvtrHoverMode.eHoverModeManeuver

        def action113():
            hoverProc.FixedTime = 15

        TryCatchAssertBlock.ExpectedException("must be", action113)

        hoverProc.HeadingMode = AgEAvtrVTOLHeadingMode.eHeadingIntoWind
        Assert.assertEqual(AgEAvtrVTOLHeadingMode.eHeadingIntoWind, hoverProc.HeadingMode)

        def action114():
            hoverProc.SetAbsoluteCourse(5, False)

        TryCatchAssertBlock.ExpectedException("must be", action114)

        def action115():
            hoverProc.SetRelativeCourse(4)

        TryCatchAssertBlock.ExpectedException("must be", action115)

        def action116():
            hoverProc.SetFinalTranslationCourse()

        TryCatchAssertBlock.ExpectedException("must be", action116)

        def action117():
            hoverProc.FinalHeadingRate = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action117)

        hoverProc.HeadingMode = AgEAvtrVTOLHeadingMode.eHeadingIndependent
        Assert.assertEqual(AgEAvtrVTOLHeadingMode.eHeadingIndependent, hoverProc.HeadingMode)
        hoverProc.SetAbsoluteCourse(5, False)
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingAbsolute, hoverProc.FinalHeadingMode)
        absCourse = hoverProc.AbsoluteCourse
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertEqual(False, hoverProc.UseMagneticHeading)

        hoverProc.SetRelativeCourse(4)
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingRelative, hoverProc.FinalHeadingMode)
        relCourse = hoverProc.RelativeCourse
        Assert.assertEqual(4, float(relCourse))

        hoverProc.SetFinalTranslationCourse()
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingTranslationCourse, hoverProc.FinalHeadingMode)

        hoverProc.FinalHeadingRate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, hoverProc.FinalHeadingRate)

        hoverProc.TranslationMode = AgEAvtrVTOLTranslationMode.eComeToStop
        Assert.assertEqual(AgEAvtrVTOLTranslationMode.eComeToStop, hoverProc.TranslationMode)

        def action118():
            hoverProc.Bearing = 6

        TryCatchAssertBlock.ExpectedException("must be", action118)

        def action119():
            hoverProc.UseMagneticBearing = True

        TryCatchAssertBlock.ExpectedException("must be", action119)

        def action120():
            hoverProc.Range = 7

        TryCatchAssertBlock.ExpectedException("must be", action120)

        def action121():
            hoverProc.FinalCourseMode = AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation

        TryCatchAssertBlock.ExpectedException("must be", action121)

        def action122():
            hoverProc.SmoothTranslationMode = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action122)

        def action123():
            hoverProc.RadiusFactor = 3

        TryCatchAssertBlock.ExpectedException("must be", action123)

        hoverProc.TranslationMode = AgEAvtrVTOLTranslationMode.eSetBearingAndRange
        hoverProc.Bearing = 6
        bearing = hoverProc.Bearing
        Assert.assertEqual(6, float(bearing))

        hoverProc.UseMagneticBearing = True
        Assert.assertTrue(hoverProc.UseMagneticBearing)

        hoverProc.Range = 7
        Assert.assertEqual(7, hoverProc.Range)

        hoverProc.FinalCourseMode = AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation
        Assert.assertEqual(AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation, hoverProc.FinalCourseMode)

        hoverProc.SmoothTranslationMode = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, hoverProc.SmoothTranslationMode)

        hoverProc.RadiusFactor = 3
        Assert.assertEqual(3, hoverProc.RadiusFactor)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc1, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(hoverProc, IProcedure))

    # endregion

    # region HoverTranslate
    @category("Procedure Tests")
    def test_HoverTranslate(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        proc2 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToHover
        )
        hoverProc: IProcedureHoverTranslate = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteWaypoint, AgEAvtrProcedureType.eProcHoverTranslate),
            IProcedureHoverTranslate,
        )

        alt = hoverProc.AltitudeOptions
        self.HoverAltitudeOptions(alt)

        hoverProc.HeadingMode = AgEAvtrVTOLHeadingMode.eHeadingIntoWind
        Assert.assertEqual(AgEAvtrVTOLHeadingMode.eHeadingIntoWind, hoverProc.HeadingMode)

        def action124():
            hoverProc.SetAbsoluteCourse(5, False)

        TryCatchAssertBlock.ExpectedException("must be", action124)

        def action125():
            hoverProc.SetRelativeCourse(4)

        TryCatchAssertBlock.ExpectedException("must be", action125)

        def action126():
            hoverProc.SetFinalTranslationCourse()

        TryCatchAssertBlock.ExpectedException("must be", action126)

        def action127():
            hoverProc.FinalHeadingRate = AgEAvtrVTOLRateMode.eAlwaysStop

        TryCatchAssertBlock.ExpectedException("must be", action127)

        hoverProc.HeadingMode = AgEAvtrVTOLHeadingMode.eHeadingIndependent
        Assert.assertEqual(AgEAvtrVTOLHeadingMode.eHeadingIndependent, hoverProc.HeadingMode)
        hoverProc.SetAbsoluteCourse(5, False)
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingAbsolute, hoverProc.FinalHeadingMode)
        absCourse = hoverProc.AbsoluteCourse
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertEqual(False, hoverProc.UseMagneticHeading)

        hoverProc.SetRelativeCourse(4)
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingRelative, hoverProc.FinalHeadingMode)
        relCourse = hoverProc.RelativeCourse
        Assert.assertEqual(4, float(relCourse))

        hoverProc.SetFinalTranslationCourse()
        Assert.assertEqual(AgEAvtrVTOLFinalHeadingMode.eFinalHeadingTranslationCourse, hoverProc.FinalHeadingMode)

        hoverProc.FinalHeadingRate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, hoverProc.FinalHeadingRate)

        hoverProc.FinalCourseMode = AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation
        Assert.assertEqual(AgEAvtrVTOLTranslationFinalCourseMode.eAnticipateNextTranslation, hoverProc.FinalCourseMode)

        hoverProc.SmoothTranslationMode = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, hoverProc.SmoothTranslationMode)

        hoverProc.RadiusFactor = 3
        Assert.assertEqual(3, hoverProc.RadiusFactor)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc1, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(hoverProc, IProcedure))

    # endregion

    # region InFormation
    @category("Procedure Tests")
    def test_InFormation(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        EarlyBoundTests.AG_AvtrProp.Propagate()

        acObj: IStkObject = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj = acObj.CopyObject("AC2")
        ac2: IAircraft = clr.CastAs(ac2Obj, IAircraft)
        route2: IVehiclePropagatorAviator = clr.CastAs(ac2.Route, IVehiclePropagatorAviator)
        prop2: IAviatorPropagator = clr.CastAs(route2.AvtrPropagator, IAviatorPropagator)
        mission2 = prop2.AvtrMission
        phases2 = mission2.Phases
        procedures2 = phases2[0].Procedures

        proc2 = procedures2.Add(AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcHoldingCircular)
        prop2.Propagate()

        formRecov = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcFormationRecover
        )
        inFormation: IProcedureInFormation = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcInFormation
            ),
            IProcedureInFormation,
        )

        self.TestProcedureName(inFormation.GetAsProcedure(), "In-Formation")

        inFormation.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL
        Assert.assertEqual(AgEAvtrPhaseOfFlight.eFlightPhaseVTOL, inFormation.FlightMode)
        inFormation.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff
        Assert.assertEqual(AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff, inFormation.FlightMode)

        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        TestBase.Application.UnitPreferences.SetCurrentUnit("Duration", "Sec")

        Assert.assertTrue(("Center" == str(inFormation.FormationPoint)))
        inFormation.FormationPoint = "AC2 SubPoint(Detic)"
        Assert.assertTrue(("AC2 SubPoint(Detic)" == str(inFormation.FormationPoint)))

        inFormation.TransitionTime = 1
        Assert.assertEqual(1, inFormation.TransitionTime)
        inFormation.HoldTime = 2
        Assert.assertEqual(2, inFormation.HoldTime)
        inFormation.DisplayStepTime = 3
        Assert.assertEqual(3, inFormation.DisplayStepTime)

        inFormation.TrajectoryBlending = AgEAvtrTrajectoryBlendMode.eBlendLHCubic
        Assert.assertEqual(AgEAvtrTrajectoryBlendMode.eBlendLHCubic, inFormation.TrajectoryBlending)

        inFormation.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowVTOL, inFormation.FuelFlowType)
        inFormation.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowTakeoff
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowTakeoff, inFormation.FuelFlowType)

        def action128():
            inFormation.OverrideFuelFlowValue = 123

        TryCatchAssertBlock.ExpectedException("must be", action128)
        inFormation.ConsiderAccelForFuelFlow = True
        Assert.assertTrue(inFormation.ConsiderAccelForFuelFlow)

        inFormation.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowOverride
        inFormation.OverrideFuelFlowValue = 123
        Assert.assertAlmostEqual(123, inFormation.OverrideFuelFlowValue, delta=tolerance)

        def action129():
            inFormation.ConsiderAccelForFuelFlow = True

        TryCatchAssertBlock.ExpectedException("must be", action129)

        currentPhase = EarlyBoundTests.AG_Phases[0]
        vtol = currentPhase.GetPerformanceModelByType("VTOL")
        vtol.Delete()

        def action130():
            inFormation.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action130)

        def action131():
            inFormation.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action131)

        currentPhase.SetDefaultPerfModels()
        TestBase.Application.UnitPreferences.ResetUnits()
        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(formRecov, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(inFormation, IProcedure))
        ac2Obj.Unload()

    # endregion

    # region Landing
    @category("Procedure Tests")
    def test_Landing(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        landing: IProcedureLanding = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcLanding),
            IProcedureLanding,
        )

        headingOptions = landing.RunwayHeadingOptions
        headingOptions.RunwayMode = AgEAvtrRunwayHighLowEnd.eHeadwind
        Assert.assertEqual(AgEAvtrRunwayHighLowEnd.eHeadwind, headingOptions.RunwayMode)

        landing.ApproachMode = AgEAvtrApproachMode.eStandardInstrumentApproach
        Assert.assertEqual(AgEAvtrApproachMode.eStandardInstrumentApproach, landing.ApproachMode)
        enrouteOpts = landing.EnrouteOptions
        self.EnrouteAndDelayOptions(enrouteOpts)

        sia = landing.ModeAsStandardInstrumentApproach

        def action132():
            testVal = landing.ModeAsEnterDownwindPattern

        TryCatchAssertBlock.ExpectedException("must be set", action132)

        def action133():
            testVal = landing.ModeAsInterceptGlideslope

        TryCatchAssertBlock.ExpectedException("must be set", action133)

        cruiseOpts = landing.EnrouteCruiseAirspeedOptions

        def action134():
            testVal = cruiseOpts.FlyCruiseAirspeedProfile

        TryCatchAssertBlock.ExpectedException("must be set", action134)

        def action135():
            cruiseOpts.FlyCruiseAirspeedProfile = True

        TryCatchAssertBlock.ExpectedException("must be set", action135)

        vertOpts = landing.VerticalPlaneOptions

        def action136():
            vertOpts.MaxEnrouteFlightPathAngle = 89

        TryCatchAssertBlock.ExpectedException("must be set", action136)

        def action137():
            vertOpts.MinEnrouteFlightPathAngle = -89

        TryCatchAssertBlock.ExpectedException("must be set", action137)

        def action138():
            vertOpts.MaxVertPlaneRadiusFactor = 0.99

        TryCatchAssertBlock.ExpectedException("must be set", action138)

        sia.ApproachAltitude = 1201
        Assert.assertEqual(1201, sia.ApproachAltitude)
        sia.UseRunwayTerrain = True
        Assert.assertTrue(sia.UseRunwayTerrain)

        landing.ApproachMode = AgEAvtrApproachMode.eInterceptGlideslope

        def action139():
            testVal = sia.ApproachAltitude

        TryCatchAssertBlock.ExpectedException("must be set", action139)

        def action140():
            sia.ApproachAltitude = 1201

        TryCatchAssertBlock.ExpectedException("must be set", action140)

        def action141():
            testVal = sia.UseRunwayTerrain

        TryCatchAssertBlock.ExpectedException("must be set", action141)

        def action142():
            sia.UseRunwayTerrain = True

        TryCatchAssertBlock.ExpectedException("must be set", action142)
        self.VerticalPlaneOptions(vertOpts)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(landing, IProcedure))

    # endregion

    # region Launch
    @category("Procedure Tests")
    def test_Launch(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        missile: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: IVehiclePropagatorBallistic = clr.CastAs(missile.Trajectory, IVehiclePropagatorBallistic)
        impactLocation: IVehicleImpactLocationPoint = clr.CastAs(traj.ImpactLocation, IVehicleImpactLocationPoint)
        impact: IVehicleImpactLLA = clr.CastAs(impactLocation.Impact, IVehicleImpactLLA)
        impact.Lat = -20
        impact.Lon = -20
        traj.Propagate()

        missile2: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile2")), IMissile
        )
        traj2: IVehiclePropagatorBallistic = clr.CastAs(missile2.Trajectory, IVehiclePropagatorBallistic)
        impactLocation2: IVehicleImpactLocationPoint = clr.CastAs(traj2.ImpactLocation, IVehicleImpactLocationPoint)
        impact2: IVehicleImpactLLA = clr.CastAs(impactLocation2.Impact, IVehicleImpactLLA)
        impact2.Lat = -20
        impact2.Lon = -20
        traj2.Propagate()

        launchProc: IProcedureLaunch = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcLaunch),
            IProcedureLaunch,
        )

        launchProc.LaunchTime = "1 Jul 1999 00:00:01.000"
        time = launchProc.LaunchTime
        Assert.assertTrue(("1 Jul 1999 00:00:01.000" == str(time)))

        # Assert.IsTrue(launchProc.PositionPointName.Length > 0);
        launchProc.PositionPointName = "Missile2 SubPoint(Centric)"
        position = launchProc.PositionPointName
        Assert.assertTrue(("Missile2 SubPoint(Centric)" == str(position)))

        Assert.assertTrue((len(launchProc.DirectionVecName) > 0))
        launchProc.DirectionVecName = "Missile2 North"
        direction = launchProc.DirectionVecName
        Assert.assertTrue(("Missile2 North" == str(direction)))

        launchProc.AttitudeMode = AgEAvtrLaunchAttitudeMode.eLaunchHoldParentAttitude

        def action143():
            launchProc.TrueCourseHint = 1

        TryCatchAssertBlock.ExpectedException("must be ", action143)

        launchProc.AttitudeMode = AgEAvtrLaunchAttitudeMode.eLaunchAlignDirectionVector
        Assert.assertEqual(AgEAvtrLaunchAttitudeMode.eLaunchAlignDirectionVector, launchProc.AttitudeMode)
        launchProc.TrueCourseHint = 1
        trueCourseHint = launchProc.TrueCourseHint
        Assert.assertEqual(1, float(trueCourseHint))

        launchProc.SpecifyLaunchAirspeed = False

        def action144():
            launchProc.AccelG = 2

        TryCatchAssertBlock.ExpectedException("must be ", action144)

        def action145():
            launchProc.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be ", action145)

        def action146():
            launchProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowOverride

        TryCatchAssertBlock.ExpectedException("must be ", action146)

        def action147():
            launchProc.OverrideFuelFlow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action147)

        launchProc.SpecifyLaunchAirspeed = True
        Assert.assertTrue(launchProc.SpecifyLaunchAirspeed)

        launchProc.AccelG = 2
        Assert.assertEqual(2, launchProc.AccelG)

        launchProc.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, launchProc.AirspeedType)
        Assert.assertAlmostEqual(251, launchProc.Airspeed, delta=tolerance)
        launchProc.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, launchProc.AirspeedType)
        Assert.assertAlmostEqual(0.4, launchProc.Airspeed, delta=tolerance)

        launchProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowVTOL, launchProc.FuelFlowType)

        def action148():
            launchProc.OverrideFuelFlow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action148)

        launchProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowOverride
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowOverride, launchProc.FuelFlowType)
        launchProc.OverrideFuelFlow = 10001
        Assert.assertEqual(10001, launchProc.OverrideFuelFlow)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(launchProc, IProcedure))
        missileObj: IStkObject = clr.CastAs(missile, IStkObject)
        missileObj.Unload()
        missileObj2: IStkObject = clr.CastAs(missile2, IStkObject)
        missileObj2.Unload()

    # endregion

    # region LaunchDynState
    @category("Procedure Tests")
    def test_LaunchDynState(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        missile: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: IVehiclePropagatorBallistic = clr.CastAs(missile.Trajectory, IVehiclePropagatorBallistic)
        impactLocation: IVehicleImpactLocationPoint = clr.CastAs(traj.ImpactLocation, IVehicleImpactLocationPoint)
        impact: IVehicleImpactLLA = clr.CastAs(impactLocation.Impact, IVehicleImpactLLA)
        impact.Lat = -20
        impact.Lon = -20
        traj.Propagate()

        missile2: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile2")), IMissile
        )
        traj2: IVehiclePropagatorBallistic = clr.CastAs(missile2.Trajectory, IVehiclePropagatorBallistic)
        impactLocation2: IVehicleImpactLocationPoint = clr.CastAs(traj2.ImpactLocation, IVehicleImpactLocationPoint)
        impact2: IVehicleImpactLLA = clr.CastAs(impactLocation2.Impact, IVehicleImpactLLA)
        impact2.Lat = -20
        impact2.Lon = -20
        traj2.Propagate()

        launchProc: IProcedureLaunchDynState = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteDynState, AgEAvtrProcedureType.eProcLaunchDynState),
            IProcedureLaunchDynState,
        )

        launchProc.LaunchTime = "1 Jul 1999 00:00:01.000"
        time = launchProc.LaunchTime
        Assert.assertTrue(("1 Jul 1999 00:00:01.000" == str(time)))

        launchProc.CoordFrame = AgEAvtrLaunchDynStateCoordFrame.eLaunchDynStateCoordFrameLocalHorizontal
        Assert.assertEqual(
            AgEAvtrLaunchDynStateCoordFrame.eLaunchDynStateCoordFrameLocalHorizontal, launchProc.CoordFrame
        )

        launchProc.BearingRef = AgEAvtrLaunchDynStateBearingRef.eLaunchDynStateBearingRefVelocity
        Assert.assertEqual(AgEAvtrLaunchDynStateBearingRef.eLaunchDynStateBearingRefVelocity, launchProc.BearingRef)

        launchProc.LaunchBearing = 1
        launchBearing = launchProc.LaunchBearing
        Assert.assertEqual(1, float(launchBearing))

        launchProc.LaunchElevation = 2
        launchElevation = launchProc.LaunchElevation
        Assert.assertEqual(2, float(launchElevation))

        launchProc.AttitudeMode = AgEAvtrLaunchAttitudeMode.eLaunchHoldParentAttitude

        def action149():
            launchProc.TrueCourseHint = 1

        TryCatchAssertBlock.ExpectedException("must be ", action149)

        launchProc.AttitudeMode = AgEAvtrLaunchAttitudeMode.eLaunchAlignDirectionVector
        Assert.assertEqual(AgEAvtrLaunchAttitudeMode.eLaunchAlignDirectionVector, launchProc.AttitudeMode)
        launchProc.TrueCourseHint = 1
        trueCourseHint = launchProc.TrueCourseHint
        Assert.assertEqual(1, float(trueCourseHint))

        launchProc.SpecifyLaunchAirspeed = False

        def action150():
            launchProc.AccelG = 2

        TryCatchAssertBlock.ExpectedException("must be ", action150)

        def action151():
            launchProc.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be ", action151)

        def action152():
            launchProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowOverride

        TryCatchAssertBlock.ExpectedException("must be ", action152)

        def action153():
            launchProc.OverrideFuelFlow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action153)

        launchProc.SpecifyLaunchAirspeed = True
        Assert.assertTrue(launchProc.SpecifyLaunchAirspeed)

        launchProc.AccelG = 2
        Assert.assertEqual(2, launchProc.AccelG)

        launchProc.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, launchProc.AirspeedType)
        Assert.assertAlmostEqual(251, launchProc.Airspeed, delta=tolerance)
        launchProc.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, launchProc.AirspeedType)
        Assert.assertAlmostEqual(0.4, launchProc.Airspeed, delta=tolerance)

        launchProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowVTOL, launchProc.FuelFlowType)

        def action154():
            launchProc.OverrideFuelFlow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action154)

        launchProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowOverride
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowOverride, launchProc.FuelFlowType)
        launchProc.OverrideFuelFlow = 10001
        Assert.assertEqual(10001, launchProc.OverrideFuelFlow)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(launchProc, IProcedure))
        missileObj: IStkObject = clr.CastAs(missile, IStkObject)
        missileObj.Unload()
        missileObj2: IStkObject = clr.CastAs(missile2, IStkObject)
        missileObj2.Unload()

    # endregion

    # region LaunchWaypoint
    @category("Procedure Tests")
    def test_LaunchWaypoint(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        launchProc: IProcedureLaunchWaypoint = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteWaypoint, AgEAvtrProcedureType.eProcLaunchWaypoint),
            IProcedureLaunchWaypoint,
        )

        launchProc.LaunchTime = "1 Jul 1999 00:00:01.000"
        time = launchProc.LaunchTime
        Assert.assertTrue(("1 Jul 1999 00:00:01.000" == str(time)))

        launchProc.AltitudeRef = AgEAvtrAltitudeRef.eAltitudeRefMSL
        Assert.assertEqual(AgEAvtrAltitudeRef.eAltitudeRefMSL, launchProc.AltitudeRef)

        launchProc.LaunchAltitude = 10
        Assert.assertEqual(10, launchProc.LaunchAltitude)

        launchProc.LaunchTrueBearing = 20
        launchTrueBearing = launchProc.LaunchTrueBearing
        Assert.assertEqual(20, float(launchTrueBearing))

        launchProc.LaunchElevation = 30
        launchElevation = launchProc.LaunchElevation
        Assert.assertAlmostEqual(30, float(launchElevation), delta=tolerance)

        launchProc.AccelG = 2
        Assert.assertEqual(2, launchProc.AccelG)

        launchProc.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, launchProc.AirspeedType)
        Assert.assertAlmostEqual(251, launchProc.Airspeed, delta=tolerance)
        launchProc.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, launchProc.AirspeedType)
        Assert.assertAlmostEqual(0.4, launchProc.Airspeed, delta=tolerance)

        launchProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowVTOL, launchProc.FuelFlowType)

        def action155():
            launchProc.OverrideFuelFlow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action155)

        launchProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowOverride
        Assert.assertEqual(AgEAvtrFuelFlowType.eFuelFlowOverride, launchProc.FuelFlowType)
        launchProc.OverrideFuelFlow = 10001
        Assert.assertEqual(10001, launchProc.OverrideFuelFlow)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(launchProc, IProcedure))

    # endregion

    # region ParallelFlightLine
    @category("Procedure Tests")
    def test_ParallelFlightLine(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        proc2 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcFlightLine
        )
        parallelProc: IProcedureParallelFlightLine = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcParallelFlightLine
            ),
            IProcedureParallelFlightLine,
        )

        self.TestProcedureName(parallelProc.GetAsProcedure(), "Parallel Flight Line")

        alt = parallelProc.AltitudeOptions
        self.AltitudeOptions(alt)

        enroute = parallelProc.EnrouteOptions
        self.EnrouteOptions(enroute)

        turnOpts = parallelProc.EnrouteTurnDirectionOptions
        self.EnrouteTurnDirection(turnOpts)

        airspeed = parallelProc.EnrouteCruiseAirspeedOptions
        self.EnrouteCruiseAirspeedAndProfile(airspeed)

        parallelProc.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeEnroute
        parallelProc.Orientation = AgEAvtrLineOrientation.eFlightLineToRight
        Assert.assertEqual(AgEAvtrLineOrientation.eFlightLineToRight, parallelProc.Orientation)
        parallelProc.Separation = 11
        Assert.assertEqual(11, parallelProc.Separation)
        parallelProc.Offset = 12
        Assert.assertEqual(12, parallelProc.Offset)
        parallelProc.LegLength = 13
        Assert.assertEqual(13, parallelProc.LegLength)

        parallelProc.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeTerrainFollow

        def action156():
            parallelProc.MustLevelOff = False

        TryCatchAssertBlock.ExpectedException("must be", action156)

        def action157():
            parallelProc.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffAutomaticManeuver

        TryCatchAssertBlock.ExpectedException("must be", action157)

        parallelProc.ProcedureType = AgEAvtrFlightLineProcType.eProcTypeEnroute
        Assert.assertEqual(AgEAvtrFlightLineProcType.eProcTypeEnroute, parallelProc.ProcedureType)
        parallelProc.MustLevelOff = True
        Assert.assertTrue(parallelProc.MustLevelOff)
        parallelProc.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, parallelProc.LevelOffMode)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(parallelProc, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc2, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc1, IProcedure))

    # endregion

    # region ReferenceState
    @category("Procedure Tests")
    def test_ReferenceState(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        refState: IProcedureReferenceState = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteReferenceState, AgEAvtrProcedureType.eProcReferenceState
            ),
            IProcedureReferenceState,
        )

        self.TestProcedureName(refState.GetAsProcedure(), "ReferenceState")

        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        refState.StartTime = 1
        time = refState.StartTime
        Assert.assertEqual(1, float(time))

        refState.Latitude = 1
        Assert.assertEqual(1, refState.Latitude)
        refState.Longitude = 2
        Assert.assertEqual(2, refState.Longitude)
        refState.UseDefaultCruiseAltitude = False
        Assert.assertEqual(False, refState.UseDefaultCruiseAltitude)
        refState.MSLAltitude = 10000
        Assert.assertEqual(10000, refState.MSLAltitude)
        refState.UseDefaultCruiseAltitude = True

        def action158():
            refState.MSLAltitude = 10000

        TryCatchAssertBlock.ExpectedException("must be", action158)

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateClimb
        Assert.assertEqual(AgEAvtrRefStatePerfMode.eRefStateClimb, refState.PerformanceMode)

        refState.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eEarthFrame
        Assert.assertEqual(AgEAvtrBasicManeuverRefFrame.eEarthFrame, refState.ReferenceFrame)

        refState.FuelFlow = 5
        Assert.assertAlmostEqual(5, refState.FuelFlow, delta=tolerance)

        # ////////////// TEST FORWARD FLIGHT OPTIONS ///////////////////////

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateLanding

        def action159():
            ffTest = refState.ModeAsForwardFlight

        TryCatchAssertBlock.ExpectedException("must be", action159)

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateClimb
        ff = refState.ModeAsForwardFlight

        ff.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, ff.AirspeedType)
        Assert.assertAlmostEqual(251, ff.Airspeed, delta=tolerance)
        ff.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, ff.AirspeedType)
        Assert.assertAlmostEqual(0.3, ff.Airspeed, delta=tolerance)

        ff.FlightPathAngle = 1
        fpa = ff.FlightPathAngle
        Assert.assertEqual(1, float(fpa))

        ff.Course = 2
        course = ff.Course
        Assert.assertEqual(2, float(course))

        ff.RollAngle = 3
        roll = ff.RollAngle
        Assert.assertEqual(3, float(roll))

        ff.AOA = 4
        aoa = ff.AOA
        Assert.assertEqual(4, float(aoa))

        ff.Sideslip = 5
        sideslip = ff.Sideslip
        Assert.assertEqual(5, float(sideslip))

        def action160():
            altRateTest = ff.AltitudeRate

        TryCatchAssertBlock.ExpectedException("Wind Frame", action160)

        def action161():
            headingTest = ff.Heading

        TryCatchAssertBlock.ExpectedException("Wind Frame", action161)

        refState.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eWindFrame

        def action162():
            fpaTest = ff.FlightPathAngle

        TryCatchAssertBlock.ExpectedException("Earth Frame", action162)

        def action163():
            courseTest = ff.Course

        TryCatchAssertBlock.ExpectedException("Earth Frame", action163)

        ff.AltitudeRate = 6
        Assert.assertEqual(6, ff.AltitudeRate)

        ff.Heading = 7
        heading = ff.Heading
        Assert.assertEqual(7, float(heading))

        ff.SetLongitudinalAccel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, 0.5)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, ff.LongitudinalAccelType)
        Assert.assertEqual(0.5, ff.GroundspeedDot)
        ff.SetLongitudinalAccel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, 0.6)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, ff.LongitudinalAccelType)
        Assert.assertEqual(0.6, ff.TASDot)

        ff.SetLateralAccel(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, 1.3)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, ff.LateralAccelType)
        Assert.assertEqual(1.3, ff.CourseDot)
        ff.SetLateralAccel(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, 1.4)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, ff.LateralAccelType)
        Assert.assertEqual(1.4, ff.HeadingDot)

        ff.SetAttitudeRate(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, 1.5)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, ff.AttitudeRateType)
        Assert.assertEqual(1.5, ff.PitchRate)
        ff.SetAttitudeRate(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, 1.6)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, ff.AttitudeRateType)
        Assert.assertEqual(1.6, ff.PushPullG)

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateLanding

        def action164():
            airspeedTest = ff.Airspeed

        TryCatchAssertBlock.ExpectedException("must be", action164)

        # ////////////// TEST TAKEOFF LANDING OPTIONS ///////////////////////
        # Note: Should be same as forward flight options except on different interface

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action165():
            tlTest = refState.ModeAsTakeoffLanding

        TryCatchAssertBlock.ExpectedException("must be", action165)

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateLanding
        tl = refState.ModeAsTakeoffLanding
        refState.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eEarthFrame

        tl.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, tl.AirspeedType)
        Assert.assertAlmostEqual(251, tl.Airspeed, delta=tolerance)
        tl.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, tl.AirspeedType)
        Assert.assertAlmostEqual(0.3, tl.Airspeed, delta=tolerance)

        tl.FlightPathAngle = 1
        fpa = tl.FlightPathAngle
        Assert.assertEqual(1, float(fpa))

        tl.Course = 2
        course = tl.Course
        Assert.assertEqual(2, float(course))

        tl.RollAngle = 3
        roll = tl.RollAngle
        Assert.assertEqual(3, float(roll))

        tl.AOA = 4
        aoa = tl.AOA
        Assert.assertEqual(4, float(aoa))

        tl.Sideslip = 5
        sideslip = tl.Sideslip
        Assert.assertEqual(5, float(sideslip))

        def action166():
            altRateTest = tl.AltitudeRate

        TryCatchAssertBlock.ExpectedException("Wind Frame", action166)

        def action167():
            headingTest = tl.Heading

        TryCatchAssertBlock.ExpectedException("Wind Frame", action167)

        refState.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eWindFrame

        def action168():
            fpaTest = tl.FlightPathAngle

        TryCatchAssertBlock.ExpectedException("Earth Frame", action168)

        def action169():
            courseTest = tl.Course

        TryCatchAssertBlock.ExpectedException("Earth Frame", action169)

        tl.AltitudeRate = 6
        Assert.assertEqual(6, tl.AltitudeRate)

        tl.Heading = 7
        heading = tl.Heading
        Assert.assertEqual(7, float(heading))

        tl.SetLongitudinalAccel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, 0.5)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, tl.LongitudinalAccelType)
        Assert.assertEqual(0.5, tl.GroundspeedDot)
        tl.SetLongitudinalAccel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, 0.6)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, tl.LongitudinalAccelType)
        Assert.assertEqual(0.6, tl.TASDot)

        tl.SetLateralAccel(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, 1.3)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, tl.LateralAccelType)
        Assert.assertEqual(1.3, tl.CourseDot)
        tl.SetLateralAccel(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, 1.4)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, tl.LateralAccelType)
        Assert.assertEqual(1.4, tl.HeadingDot)

        tl.SetAttitudeRate(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, 1.5)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, tl.AttitudeRateType)
        Assert.assertEqual(1.5, tl.PitchRate)
        tl.SetAttitudeRate(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, 1.6)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, tl.AttitudeRateType)
        Assert.assertEqual(1.6, tl.PushPullG)

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action170():
            airspeedTest = tl.Airspeed

        TryCatchAssertBlock.ExpectedException("must be", action170)

        # ////////////// TEST HOVER OPTIONS ///////////////////////

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action171():
            hoverTest = refState.ModeAsHover

        TryCatchAssertBlock.ExpectedException("must be", action171)

        currentPhase = EarlyBoundTests.AG_Phases[0]
        vtol = currentPhase.GetPerformanceModelByType("VTOL")
        vtol.Delete()

        def action172():
            refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateHover

        TryCatchAssertBlock.ExpectedException("VTOL", action172)
        currentPhase.SetDefaultPerfModels()

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateHover

        def action173():
            refState.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eEarthFrame

        TryCatchAssertBlock.ExpectedException("must be", action173)

        hoverOpts = refState.ModeAsHover

        hoverOpts.Groundspeed = 200
        Assert.assertEqual(200, hoverOpts.Groundspeed)

        hoverOpts.AltitudeRate = 6
        Assert.assertEqual(6, hoverOpts.AltitudeRate)

        hoverOpts.Heading = 7
        heading = hoverOpts.Heading
        Assert.assertEqual(7, float(heading))

        hoverOpts.Course = 8
        course = hoverOpts.Course
        Assert.assertEqual(8, float(course))

        hoverOpts.HeadingDot = 9
        Assert.assertEqual(9, hoverOpts.HeadingDot)

        hoverOpts.CourseDot = 10
        Assert.assertEqual(10, hoverOpts.CourseDot)

        hoverOpts.RollAngle = 11
        roll = hoverOpts.RollAngle
        Assert.assertEqual(11, float(roll))

        hoverOpts.AOA = 12
        aoa = hoverOpts.AOA
        Assert.assertEqual(12, float(aoa))

        hoverOpts.SetLongitudinalAccel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, 0.5)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, hoverOpts.LongitudinalAccelType)
        Assert.assertEqual(0.5, hoverOpts.GroundspeedDot)
        hoverOpts.SetLongitudinalAccel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, 0.6)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, hoverOpts.LongitudinalAccelType)
        Assert.assertEqual(0.6, hoverOpts.TASDot)

        hoverOpts.SetAttitudeRate(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, 1.5)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPitchRate, hoverOpts.AttitudeRateType)
        Assert.assertEqual(1.5, hoverOpts.PitchRate)
        hoverOpts.SetAttitudeRate(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, 1.6)
        Assert.assertEqual(AgEAvtrRefStateAttitudeMode.eSpecifyPushPullG, hoverOpts.AttitudeRateType)
        Assert.assertEqual(1.6, hoverOpts.PushPullG)

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action174():
            groundspeedTest = hoverOpts.Groundspeed

        TryCatchAssertBlock.ExpectedException("must be", action174)

        # ////////////// TEST WEIGHT ON WHEELS OPTIONS ///////////////////////

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action175():
            wowTest = refState.ModeAsWeightOnWheels

        TryCatchAssertBlock.ExpectedException("must be", action175)

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateTakeoffRun

        def action176():
            refState.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eEarthFrame

        TryCatchAssertBlock.ExpectedException("must be", action176)

        wowOpts = refState.ModeAsWeightOnWheels

        wowOpts.Groundspeed = 200
        Assert.assertEqual(200, wowOpts.Groundspeed)

        wowOpts.Heading = 7
        heading = wowOpts.Heading
        Assert.assertEqual(7, float(heading))

        wowOpts.SetLongitudinalAccel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, 0.5)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyGroundSpeedDot, wowOpts.LongitudinalAccelType)
        Assert.assertEqual(0.5, wowOpts.GroundspeedDot)
        wowOpts.SetLongitudinalAccel(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, 0.6)
        Assert.assertEqual(AgEAvtrRefStateLongitudinalAccelMode.eSpecifyTASDot, wowOpts.LongitudinalAccelType)
        Assert.assertEqual(0.6, wowOpts.TASDot)

        wowOpts.SetLateralAccel(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, 1.3)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyCourseDot, wowOpts.LateralAccelType)
        Assert.assertEqual(1.3, wowOpts.CourseDot)
        wowOpts.SetLateralAccel(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, 1.4)
        Assert.assertEqual(AgEAvtrRefStateLateralAccelMode.eSpecifyHeadingDot, wowOpts.LateralAccelType)
        Assert.assertEqual(1.4, wowOpts.HeadingDot)

        refState.PerformanceMode = AgEAvtrRefStatePerfMode.eRefStateClimb

        def action177():
            groundspeedTest = wowOpts.Groundspeed

        TryCatchAssertBlock.ExpectedException("must be", action177)

        TestBase.Application.UnitPreferences.ResetUnits()
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(refState, IProcedure))

    # endregion

    # region Takeoff
    @category("Procedure Tests")
    def test_Takeoff(self):
        self.EmptyProcedures()

        takeoff: IProcedureTakeoff = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff),
            IProcedureTakeoff,
        )

        headingOptions = takeoff.RunwayHeadingOptions
        headingOptions.RunwayMode = AgEAvtrRunwayHighLowEnd.eHeadwind
        Assert.assertEqual(AgEAvtrRunwayHighLowEnd.eHeadwind, headingOptions.RunwayMode)

        takeoff.TakeoffMode = AgEAvtrTakeoffMode.eTakeoffNormal
        takeoffNormal = takeoff.ModeAsNormal

        def action178():
            testVal = takeoff.ModeAsDeparturePoint

        TryCatchAssertBlock.ExpectedException("must be set", action178)

        def action179():
            testVal = takeoff.ModeAsLowTransition

        TryCatchAssertBlock.ExpectedException("must be set", action179)

        takeoffNormal.DepartureAltitude = 501
        Assert.assertEqual(501, takeoffNormal.DepartureAltitude)
        takeoffNormal.UseRunwayTerrain = True
        Assert.assertTrue(takeoffNormal.UseRunwayTerrain)

        takeoff.TakeoffMode = AgEAvtrTakeoffMode.eTakeoffFlyToDeparturePoint

        def action180():
            testVal = takeoffNormal.DepartureAltitude

        TryCatchAssertBlock.ExpectedException("must be set", action180)

        def action181():
            takeoffNormal.DepartureAltitude = 501

        TryCatchAssertBlock.ExpectedException("must be set", action181)

        def action182():
            testVal = takeoffNormal.UseRunwayTerrain

        TryCatchAssertBlock.ExpectedException("must be set", action182)

        def action183():
            takeoffNormal.UseRunwayTerrain = True

        TryCatchAssertBlock.ExpectedException("must be set", action183)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))

    # endregion

    # region TerrainFollowing
    @category("Procedure Tests")
    def test_TerrainFollowing(self):
        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        terrainFollow: IProcedureTerrainFollow = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTerrainFollowing
            ),
            IProcedureTerrainFollow,
        )

        terrainFollow.AltitudeAGL = 600
        Assert.assertEqual(600, terrainFollow.AltitudeAGL)

        nav = terrainFollow.NavigationOptions
        self.NavigationOptions(nav)

        terrainAirspeed = terrainFollow.TerrainFollowingAirspeedOptions
        self.EnrouteCruiseAirspeed(terrainAirspeed)

        terrainFollow.ReduceTurnRadii = True
        Assert.assertTrue(terrainFollow.ReduceTurnRadii)
        terrainFollow.TurnFactor = 3
        Assert.assertEqual(3, terrainFollow.TurnFactor)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(terrainFollow, IProcedure))

    # endregion

    # region TransitionToForwardFlight
    @category("Procedure Tests")
    def test_TransitionToForwardFlight(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        toHover: IProcedureTransitionToHover = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToHover
            ),
            IProcedureTransitionToHover,
        )
        toFlight: IProcedureTransitionToForwardFlight = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToForwardFlight
            ),
            IProcedureTransitionToForwardFlight,
        )

        toFlight.SetTransitionIntoWind()
        Assert.assertEqual(AgEAvtrVTOLTransitionMode.eTransitionIntoWind, toFlight.TransitionCourseMode)

        toFlight.SetAbsoluteCourse(5, True)
        Assert.assertEqual(AgEAvtrVTOLTransitionMode.eTransitionAbsoluteHdg, toFlight.TransitionCourseMode)
        absCourse = toFlight.AbsoluteCourse
        Assert.assertAlmostEqual(5, float(absCourse), delta=tolerance)
        Assert.assertTrue(toFlight.UseMagneticHeading)

        toFlight.SetRelativeCourse(4)
        relCourse = toFlight.RelativeCourse
        Assert.assertAlmostEqual(4, float(relCourse), delta=tolerance)
        Assert.assertEqual(AgEAvtrVTOLTransitionMode.eTransitionRelativeHdg, toFlight.TransitionCourseMode)

        toFlight.FlightPathAngle = 11
        fpa = toFlight.FlightPathAngle
        Assert.assertAlmostEqual(11, float(fpa), delta=tolerance)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(toHover, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(toFlight, IProcedure))

    # endregion

    # region TransitionToHover
    @category("Procedure Tests")
    def test_TransitionToHover(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        takeoff = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        toHover: IProcedureTransitionToHover = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcTransitionToHover
            ),
            IProcedureTransitionToHover,
        )

        toHover.Altitude = 600
        Assert.assertEqual(600, toHover.Altitude)
        toHover.AltitudeReference = AgEAvtrAGLMSL.eAltAGL
        Assert.assertEqual(AgEAvtrAGLMSL.eAltAGL, toHover.AltitudeReference)

        enrouteOpts = toHover.EnrouteOptions
        self.EnrouteOptions(enrouteOpts)

        enrouteTurnDirOpts = toHover.EnrouteTurnDirectionOptions
        self.EnrouteTurnDirection(enrouteTurnDirOpts)

        verticalPlaneOpts = toHover.VerticalPlaneOptions
        self.VerticalPlaneAndFlightPathOptions(verticalPlaneOpts)

        toHover.SetTransitionIntoWind()
        Assert.assertTrue(toHover.TransitionIntoWind)

        toHover.SetTransitionCourse(5, True)
        course = toHover.Course
        Assert.assertAlmostEqual(5, float(course), delta=tolerance)
        Assert.assertTrue(toHover.UseMagneticHeading)

        toHover.SmoothTransitionMode = AgEAvtrTransitionToHoverMode.eTranslationOnly
        Assert.assertEqual(AgEAvtrTransitionToHoverMode.eTranslationOnly, toHover.SmoothTransitionMode)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(takeoff, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(toHover, IProcedure))

    # endregion

    # region VerticalLanding
    @category("Procedure Tests")
    def test_VerticalLanding(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteVTOLPoint, AgEAvtrProcedureType.eProcVerticalTakeoff
        )
        vertLanding: IProcedureVerticalLanding = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteVTOLPoint, AgEAvtrProcedureType.eProcVerticalLanding
            ),
            IProcedureVerticalLanding,
        )

        vertLanding.AltitudeAbovePoint = 101
        Assert.assertEqual(101, vertLanding.AltitudeAbovePoint)
        vertLanding.FinalAltitudeRate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, vertLanding.FinalAltitudeRate)
        vertLanding.AltitudeOffset = 5
        Assert.assertEqual(5, vertLanding.AltitudeOffset)

        vertLanding.HeadingMode = AgEAvtrVertLandingMode.eVertLandingIndependent
        Assert.assertEqual(AgEAvtrVertLandingMode.eVertLandingIndependent, vertLanding.HeadingMode)
        vertLanding.HeadingMode = AgEAvtrVertLandingMode.eVertLandingAlignTranslationCourseOverride
        Assert.assertEqual(AgEAvtrVertLandingMode.eVertLandingAlignTranslationCourseOverride, vertLanding.HeadingMode)

        vertLanding.SetHeading(11, False)
        hdg = vertLanding.Heading
        Assert.assertAlmostEqual(11, float(hdg), delta=tolerance)
        Assert.assertEqual(False, vertLanding.UseMagneticHeading)

        vertLanding.HeadingMode = AgEAvtrVertLandingMode.eVertLandingAlignTranslationCourse
        Assert.assertEqual(AgEAvtrVertLandingMode.eVertLandingAlignTranslationCourse, vertLanding.HeadingMode)

        def action184():
            vertLanding.SetHeading(11, False)

        TryCatchAssertBlock.ExpectedException("must be", action184)

        vertLanding.HeadingMode = AgEAvtrVertLandingMode.eVertLandingIntoWind
        Assert.assertEqual(AgEAvtrVertLandingMode.eVertLandingIntoWind, vertLanding.HeadingMode)

        def action185():
            vertLanding.SetHeading(11, False)

        TryCatchAssertBlock.ExpectedException("must be", action185)

        vertLanding.RadiusFactor = 3
        Assert.assertEqual(3, vertLanding.RadiusFactor)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(proc1, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(vertLanding, IProcedure))

    # endregion

    # region VerticalTakeoff
    @category("Procedure Tests")
    def test_VerticalTakeoff(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        vertTakeoff: IProcedureVerticalTakeoff = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteVTOLPoint, AgEAvtrProcedureType.eProcVerticalTakeoff
            ),
            IProcedureVerticalTakeoff,
        )

        vertTakeoff.AltitudeAbovePoint = 101
        Assert.assertEqual(101, vertTakeoff.AltitudeAbovePoint)
        vertTakeoff.FinalAltitudeRate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, vertTakeoff.FinalAltitudeRate)
        vertTakeoff.AltitudeOffset = 5
        Assert.assertEqual(5, vertTakeoff.AltitudeOffset)

        vertTakeoff.SetHeading(11, False)
        hdg = vertTakeoff.Heading
        Assert.assertAlmostEqual(11, float(hdg), delta=tolerance)
        Assert.assertEqual(False, vertTakeoff.UseMagneticHeading)
        Assert.assertEqual(False, vertTakeoff.HeadingIntoWind)

        vertTakeoff.HeadingIntoWind = True
        Assert.assertTrue(vertTakeoff.HeadingIntoWind)

        vertTakeoff.HoldOnDeck = "00:00:15.000"
        holdTime = vertTakeoff.HoldOnDeck
        Assert.assertTrue(("00:00:15.000" == str(holdTime)))

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(vertTakeoff, IProcedure))

    # endregion

    # region VGTPoint
    @category("Procedure Tests")
    def test_VGTPoint(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        proc2 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
        )
        EarlyBoundTests.AG_AvtrProp.Propagate()

        acObj: IStkObject = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        ac2Obj = acObj.CopyObject("AC2")
        ac2: IAircraft = clr.CastAs(ac2Obj, IAircraft)
        route2: IVehiclePropagatorAviator = clr.CastAs(ac2.Route, IVehiclePropagatorAviator)
        prop2: IAviatorPropagator = clr.CastAs(route2.AvtrPropagator, IAviatorPropagator)
        mission2 = prop2.AvtrMission
        prop2.Propagate()

        EarlyBoundTests.AG_Procedures.RemoveAtIndex(1)
        EarlyBoundTests.AG_Procedures.RemoveAtIndex(0)
        vgtProc: IProcedureVGTPoint = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcVGTPoint),
            IProcedureVGTPoint,
        )

        self.TestProcedureName(vgtProc.GetAsProcedure(), "VGT Point")

        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        TestBase.Application.UnitPreferences.SetCurrentUnit("Duration", "Sec")
        vgtProc.StartTime = 2
        startTime = vgtProc.StartTime
        Assert.assertEqual(2, float(startTime))

        minTime = vgtProc.MinimumTime
        maxTime = vgtProc.MaximumTime
        Assert.assertEqual(0, float(minTime))

        Assert.assertTrue(("Center" == str(vgtProc.FormationPoint)))
        vgtProc.FormationPoint = "AC2 SubPoint(Detic)"
        Assert.assertTrue(("AC2 SubPoint(Detic)" == str(vgtProc.FormationPoint)))
        vgtProc.InterpolatePointPosVel = True
        Assert.assertTrue(vgtProc.InterpolatePointPosVel)

        vgtProc.Duration = 5
        Assert.assertEqual(5, vgtProc.Duration)
        vgtProc.UseMaxPointStopTime = True
        Assert.assertTrue(vgtProc.UseMaxPointStopTime)

        vgtProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowTakeoff

        def action186():
            vgtProc.OverrideFuelFlowValue = 123

        TryCatchAssertBlock.ExpectedException("must be", action186)
        vgtProc.ConsiderAccelForFuelFlow = True
        Assert.assertTrue(vgtProc.ConsiderAccelForFuelFlow)

        vgtProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowOverride
        vgtProc.OverrideFuelFlowValue = 123
        Assert.assertAlmostEqual(123, vgtProc.OverrideFuelFlowValue, delta=tolerance)

        def action187():
            vgtProc.ConsiderAccelForFuelFlow = True

        TryCatchAssertBlock.ExpectedException("must be", action187)

        vgtProc.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff
        Assert.assertEqual(AgEAvtrPhaseOfFlight.eFlightPhaseTakeoff, vgtProc.FlightMode)
        vgtProc.DisplayStepTime = 4
        Assert.assertEqual(4, vgtProc.DisplayStepTime)

        vgtProc.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL
        Assert.assertEqual(vgtProc.FlightMode, AgEAvtrPhaseOfFlight.eFlightPhaseVTOL)
        vgtProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL
        Assert.assertEqual(vgtProc.FuelFlowType, AgEAvtrFuelFlowType.eFuelFlowVTOL)
        currentPhase = EarlyBoundTests.AG_Phases[0]
        vtol = currentPhase.GetPerformanceModelByType("VTOL")
        vtol.Delete()

        def action188():
            vgtProc.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action188)

        def action189():
            vgtProc.FuelFlowType = AgEAvtrFuelFlowType.eFuelFlowVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action189)

        currentPhase.SetDefaultPerfModels()
        TestBase.Application.UnitPreferences.ResetUnits()
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(vgtProc, IProcedure))
        ac2Obj.Unload()

    # endregion

    # region BasicManeuver
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuver(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.UseMaxDownrange = True
        basicManeuver.MaxDownrange = 11
        Assert.assertEqual(11, basicManeuver.MaxDownrange)

        TestBase.Application.UnitPreferences.SetCurrentUnit("Duration", "HMS")
        basicManeuver.UseMaxTimeOfFlight = True
        basicManeuver.MaxTimeOfFlight = "00:01:30.000"
        Assert.assertEqual("00:01:30.000", basicManeuver.MaxTimeOfFlight)

        basicManeuver.UseStopFuelState = True
        basicManeuver.StopFuelState = 1
        Assert.assertEqual(1, basicManeuver.StopFuelState)

        basicManeuver.UseMaxDownrange = False
        basicManeuver.UseMaxTimeOfFlight = False
        basicManeuver.UseStopFuelState = True

        def action190():
            basicManeuver.UseStopFuelState = False

        TryCatchAssertBlock.ExpectedException("At least one", action190)

        basicManeuver.TerrainImpactMode = AgEAvtrBasicManeuverAltitudeLimit.eBasicManeuverAltLimitContinue

        def action191():
            basicManeuver.TerrainImpactTimeOffset = 1

        TryCatchAssertBlock.ExpectedException("terrain impact mode", action191)
        basicManeuver.TerrainImpactMode = AgEAvtrBasicManeuverAltitudeLimit.eBasicManeuverAltLimitError

        def action192():
            basicManeuver.TerrainImpactTimeOffset = 1

        TryCatchAssertBlock.ExpectedException("terrain impact mode", action192)

        basicManeuver.FuelFlowType = AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowCruise

        def action193():
            basicManeuver.OverrideFuelFlowValue = 1

        TryCatchAssertBlock.ExpectedException("fuel flow source", action193)

        def action194():
            testVal = basicManeuver.ScaleFuelFlow

        TryCatchAssertBlock.ExpectedException("fuel flow source", action194)

        def action195():
            basicManeuver.ScaleFuelFlow = True

        TryCatchAssertBlock.ExpectedException("fuel flow source", action195)

        basicManeuver.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL
        Assert.assertEqual(basicManeuver.FlightMode, AgEAvtrPhaseOfFlight.eFlightPhaseVTOL)
        basicManeuver.FuelFlowType = AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowVTOL
        Assert.assertEqual(basicManeuver.FuelFlowType, AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowVTOL)
        currentPhase = EarlyBoundTests.AG_Phases[0]
        vtol = currentPhase.GetPerformanceModelByType("VTOL")
        vtol.Delete()

        def action196():
            basicManeuver.FlightMode = AgEAvtrPhaseOfFlight.eFlightPhaseVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action196)

        def action197():
            basicManeuver.FuelFlowType = AgEAvtrBasicManeuverFuelFlowType.eBasicManeuverFuelFlowVTOL

        TryCatchAssertBlock.ExpectedException("VTOL", action197)

        currentPhase.SetDefaultPerfModels()
        TestBase.Application.UnitPreferences.ResetUnits()
        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAileronRoll
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAileronRoll(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Aileron Roll"
        roll: IBasicManeuverStrategyAileronRoll = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyAileronRoll
        )

        roll.FlightPathOption = AgEAvtrAileronRollFlightPath.eZeroGFlightPath
        Assert.assertEqual(AgEAvtrAileronRollFlightPath.eZeroGFlightPath, roll.FlightPathOption)

        Assert.assertEqual("Aileron Roll", basicManeuver.ProfileStrategyType)
        rollProfile: IBasicManeuverStrategyAileronRoll = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategyAileronRoll
        )
        Assert.assertEqual(AgEAvtrAileronRollFlightPath.eZeroGFlightPath, rollProfile.FlightPathOption)

        roll.ActiveMode = AgEAvtrAileronRollMode.eRollToAngle

        def action198():
            roll.RollOrientation = AgEAvtrRollUprightInverted.eRollInverted

        TryCatchAssertBlock.ExpectedException("must be", action198)

        roll.ActiveMode = AgEAvtrAileronRollMode.eRollToOrientation
        roll.RollOrientation = AgEAvtrRollUprightInverted.eRollInverted
        Assert.assertEqual(AgEAvtrRollUprightInverted.eRollInverted, roll.RollOrientation)

        roll.RollRateMode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action199():
            angle = roll.OverrideRollRate

        TryCatchAssertBlock.ExpectedException("must be", action199)
        roll.RollRateMode = AgEAvtrPerfModelOverride.eOverride
        roll.OverrideRollRate = 20
        overrideRollRate = roll.OverrideRollRate
        Assert.assertEqual(20, float(overrideRollRate))

        airspeedOpts = roll.AirspeedOptions
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAutopilotNav
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAutopilotNav(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Autopilot - Horizontal Plane"
        autopilot: IBasicManeuverStrategyAutopilotNav = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyAutopilotNav
        )

        autopilot.ActiveMode = AgEAvtrAutopilotHorizPlaneMode.eAutopilotAbsoluteCourse
        autopilot.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 1000)
        turnRad = autopilot.ControlLimitTurnRadius
        Assert.assertEqual(1000, turnRad)

        autopilot.ActiveMode = AgEAvtrAutopilotHorizPlaneMode.eAutopilotCourseRate

        def action200():
            autopilot.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 1000)

        TryCatchAssertBlock.ExpectedException("must be", action200)

        autopilot.CompensateForCoriolisAccel = True
        Assert.assertTrue(autopilot.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverAutopilotProfile
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverAutopilotProfile(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.ProfileStrategyType = "Autopilot - Vertical Plane"
        autopilot: IBasicManeuverStrategyAutopilotProf = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategyAutopilotProf
        )
        autopilot.AltitudeMode = AgEAvtrAutopilotAltitudeMode.eAutopilotHoldInitAltitude

        def action201():
            testVal = autopilot.AbsoluteAltitude

        TryCatchAssertBlock.ExpectedException("must be", action201)

        def action202():
            testVal = autopilot.RelativeAltitudeChange

        TryCatchAssertBlock.ExpectedException("must be", action202)

        def action203():
            testVal = autopilot.AltitudeRate

        TryCatchAssertBlock.ExpectedException("must be", action203)

        def action204():
            testVal = autopilot.FPA

        TryCatchAssertBlock.ExpectedException("must be", action204)

        autopilot.AltitudeControlMode = AgEAvtrAutopilotAltitudeControlMode.eAutopilotAltitudeRate
        autopilot.ControlAltitudeRateValue = 2001
        Assert.assertEqual(2001, autopilot.ControlAltitudeRateValue)

        autopilot.AltitudeControlMode = AgEAvtrAutopilotAltitudeControlMode.eAutopilotFPA
        autopilot.ControlFPAValue = 11
        controlFPA = autopilot.ControlFPAValue
        Assert.assertEqual(11, controlFPA)

        autopilot.AltitudeControlMode = AgEAvtrAutopilotAltitudeControlMode.eAutopilotPerfModels

        def action205():
            testVal = autopilot.ControlAltitudeRateValue

        TryCatchAssertBlock.ExpectedException("must be", action205)

        def action206():
            testVal = autopilot.ControlFPAValue

        TryCatchAssertBlock.ExpectedException("must be", action206)

        autopilot.ControlLimitMode = AgEAvtrPerfModelOverride.eOverride
        autopilot.MaxPitchRate = 11
        pitchRate = autopilot.MaxPitchRate
        Assert.assertEqual(11, pitchRate)
        autopilot.ControlLimitMode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action207():
            autopilot.MaxPitchRate = 11

        TryCatchAssertBlock.ExpectedException("must be", action207)

        autopilot.DampingRatio = 1.5
        Assert.assertEqual(1.5, autopilot.DampingRatio)

        autopilot.AltitudeMode = AgEAvtrAutopilotAltitudeMode.eAutopilotSpecifyAltitude
        autopilot.AbsoluteAltitude = 10001
        Assert.assertEqual(10001, autopilot.AbsoluteAltitude)

        autopilot.AltitudeMode = AgEAvtrAutopilotAltitudeMode.eAutopilotSpecifyAltitudeChange
        autopilot.RelativeAltitudeChange = 1
        Assert.assertEqual(1, autopilot.RelativeAltitudeChange)

        autopilot.AltitudeMode = AgEAvtrAutopilotAltitudeMode.eAutopilotSpecifyAltitudeRate
        autopilot.AltitudeRate = 1
        Assert.assertEqual(1, autopilot.AltitudeRate)

        autopilot.AltitudeMode = AgEAvtrAutopilotAltitudeMode.eAutopilotSpecifyFPA
        autopilot.FPA = 1
        fpa = autopilot.FPA
        Assert.assertEqual(1, fpa)

        autopilot.AltitudeMode = AgEAvtrAutopilotAltitudeMode.eAutopilotBallistic

        def action208():
            autopilot.AltitudeControlMode = AgEAvtrAutopilotAltitudeControlMode.eAutopilotFPA

        TryCatchAssertBlock.ExpectedException("must be", action208)

        def action209():
            autopilot.DampingRatio = 1.5

        TryCatchAssertBlock.ExpectedException("must be", action209)

        airspeedOpts = autopilot.AirspeedOptions
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        autopilot.CompensateForCoriolisAccel = True
        Assert.assertTrue(autopilot.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverBallistic3D
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverBallistic3D(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Ballistic3D"
        ballistic: IBasicManeuverStrategyBallistic3D = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyBallistic3D
        )

        ballistic.ControlMode = AgEAvtrBallistic3DControlMode.eBallistic3DCompensateForWind
        Assert.assertEqual(AgEAvtrBallistic3DControlMode.eBallistic3DCompensateForWind, ballistic.ControlMode)

        self.BasicManeuverAirspeedOptions(ballistic.AirspeedOptions)

        def action210():
            ballistic.WindForceEffectiveArea = 10

        TryCatchAssertBlock.ExpectedException("must be", action210)

        def action211():
            ballistic.ParachuteArea = 5

        TryCatchAssertBlock.ExpectedException("must be", action211)

        def action212():
            ballistic.ParachuteCd = 1.5

        TryCatchAssertBlock.ExpectedException("must be", action212)

        ballistic.ControlMode = AgEAvtrBallistic3DControlMode.eBallistic3DWindPushesVehicle
        Assert.assertEqual(AgEAvtrBallistic3DControlMode.eBallistic3DWindPushesVehicle, ballistic.ControlMode)

        self.BasicManeuverAirspeedOptions(ballistic.AirspeedOptions)

        ballistic.WindForceEffectiveArea = 10
        Assert.assertEqual(10, ballistic.WindForceEffectiveArea)

        def action213():
            ballistic.ParachuteArea = 5

        TryCatchAssertBlock.ExpectedException("must be", action213)

        def action214():
            ballistic.ParachuteCd = 1.5

        TryCatchAssertBlock.ExpectedException("must be", action214)

        ballistic.ControlMode = AgEAvtrBallistic3DControlMode.eBallistic3DParachuteMode
        Assert.assertEqual(AgEAvtrBallistic3DControlMode.eBallistic3DParachuteMode, ballistic.ControlMode)

        ballistic.ParachuteArea = 5
        Assert.assertEqual(5, ballistic.ParachuteArea)
        ballistic.ParachuteCd = 1.5
        Assert.assertEqual(1.5, ballistic.ParachuteCd)

        ballistic.WindForceEffectiveArea = 11
        Assert.assertEqual(11, ballistic.WindForceEffectiveArea)

        def action215():
            self.BasicManeuverAirspeedOptions(ballistic.AirspeedOptions)

        TryCatchAssertBlock.ExpectedException("must be", action215)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverBarrelRoll
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverBarrelRoll(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Barrel Roll"
        roll: IBasicManeuverStrategyBarrelRoll = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyBarrelRoll)
        roll.HelixAngle = 359
        helixAngle = roll.HelixAngle
        roll.HelixAngleMode = AgEAvtrAngleMode.eRelativeAngle
        Assert.assertEqual(359, float(helixAngle))
        Assert.assertEqual(AgEAvtrAngleMode.eRelativeAngle, roll.HelixAngleMode)

        Assert.assertEqual("Barrel Roll", basicManeuver.ProfileStrategyType)
        rollProfile: IBasicManeuverStrategyBarrelRoll = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategyBarrelRoll
        )
        helixAngleProfile = rollProfile.HelixAngle
        Assert.assertEqual(359, float(helixAngleProfile))
        Assert.assertEqual(AgEAvtrAngleMode.eRelativeAngle, rollProfile.HelixAngleMode)

        roll.HoldInitTAS = True

        def action216():
            roll.SetAirspeeds(AgEAvtrAirspeedType.eMach, 0.1, 0.2)

        TryCatchAssertBlock.ExpectedException("must be", action216)

        roll.HoldInitTAS = False
        roll.SetAirspeeds(AgEAvtrAirspeedType.eMach, 0.1, 0.2)
        Assert.assertEqual(0.1, roll.TopAirspeed)
        Assert.assertEqual(0.2, roll.BottomAirspeed)

        roll.SetAirspeeds(AgEAvtrAirspeedType.eTAS, 200, 201)
        Assert.assertEqual(200, roll.TopAirspeed)
        Assert.assertEqual(201, roll.BottomAirspeed)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverBezier
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverBezier(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.ProfileStrategyType = "Profile Segment - Bezier"
        bezier: IBasicManeuverStrategyBezier = clr.CastAs(basicManeuver.Profile, IBasicManeuverStrategyBezier)

        bezier.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eWindFrame
        Assert.assertEqual(AgEAvtrBasicManeuverRefFrame.eWindFrame, bezier.ReferenceFrame)

        bezier.Downrange = 11
        Assert.assertEqual(11, bezier.Downrange)
        bezier.Altitude = 10000
        Assert.assertEqual(10000, bezier.Altitude)
        bezier.SetAirspeed(AgEAvtrAirspeedType.eTAS, 250)
        Assert.assertEqual(250, bezier.Airspeed)
        bezier.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.2)
        Assert.assertEqual(0.2, bezier.Airspeed)

        bezier.SetVerticalVelocity(AgEAvtrFlyToFlightPathAngleMode.eFlyToAltRate, 1000)
        Assert.assertAlmostEqual(1000, bezier.AltitudeRate, delta=tolerance)
        bezier.SetVerticalVelocity(AgEAvtrFlyToFlightPathAngleMode.eFlyToFlightPathAngle, 3)
        angle = bezier.FlightPathAngle
        Assert.assertEqual(3, float(angle))

        bezier.SetStopAirspeed(True, AgEAvtrAirspeedType.eTAS, 260)
        Assert.assertTrue(bezier.UseStopAtAirspeed)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, bezier.StopAirspeedType)
        Assert.assertEqual(260, bezier.StopAirspeed)

        bezier.SetStopAirspeed(False, AgEAvtrAirspeedType.eMach, 0.2)
        Assert.assertEqual(False, bezier.UseStopAtAirspeed)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, bezier.StopAirspeedType)
        Assert.assertEqual(0.2, bezier.StopAirspeed)

        bezier.SetStopAltitudeRate(True, 5)
        Assert.assertEqual(5, bezier.StopAltitudeRate)

        bezier.CompensateForCoriolisAccel = True
        Assert.assertTrue(bezier.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverCruise
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverCruise(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.ProfileStrategyType = "Cruise Profile"
        cruise: IBasicManeuverStrategyCruiseProfile = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategyCruiseProfile
        )

        cruise.UseDefaultCruiseAltitude = True

        def action217():
            levelOff = cruise.LevelOff

        TryCatchAssertBlock.ExpectedException("must be", action217)

        def action218():
            cruise.LevelOff = True

        TryCatchAssertBlock.ExpectedException("must be", action218)

        def action219():
            cruise.RequestedAltitude = 10000

        TryCatchAssertBlock.ExpectedException("must be", action219)

        cruise.UseDefaultCruiseAltitude = False
        cruise.LevelOff = True
        Assert.assertTrue(cruise.LevelOff)

        def action220():
            cruise.RequestedAltitude = 10000

        TryCatchAssertBlock.ExpectedException("must be", action220)

        cruise.LevelOff = False
        cruise.RequestedAltitude = 10000
        Assert.assertEqual(10000, cruise.RequestedAltitude)

        self.EnrouteCruiseAirspeed(cruise.CruiseAirspeedOptions)

        cruise.CompensateForCoriolisAccel = True
        Assert.assertTrue(cruise.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverFlyAOA
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverFlyAOA(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Fly AOA"
        flyAOA: IBasicManeuverStrategyFlyAOA = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyFlyAOA)

        flyAOA.AOA = 11
        aoa = flyAOA.AOA
        Assert.assertEqual(11, float(aoa))

        Assert.assertEqual("Fly AOA", basicManeuver.ProfileStrategyType)
        flyAOAProfile: IBasicManeuverStrategyFlyAOA = clr.CastAs(basicManeuver.Profile, IBasicManeuverStrategyFlyAOA)
        aoaProfile = flyAOAProfile.AOA
        Assert.assertEqual(11, float(aoaProfile))

        flyAOA.TurnDirection = AgEAvtrFlyAOALeftRight.eFlyAOALeft
        flyAOA.ControlRollAngle = False
        flyAOA.RollRateMode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action221():
            value = flyAOA.OverrideRollRate

        TryCatchAssertBlock.ExpectedException("must be", action221)
        flyAOA.RollRateMode = AgEAvtrPerfModelOverride.eOverride
        flyAOA.OverrideRollRate = 29
        rate = flyAOA.OverrideRollRate
        Assert.assertAlmostEqual(29, float(rate), delta=tolerance)

        def action222():
            flyAOA.RollAngle = 59

        TryCatchAssertBlock.ExpectedException("must be", action222)

        def action223():
            flyAOA.StopOnRollAngle = True

        TryCatchAssertBlock.ExpectedException("must be", action223)
        flyAOA.ControlRollAngle = True
        flyAOA.RollAngle = 59
        angle = flyAOA.RollAngle
        Assert.assertAlmostEqual(59, float(angle), delta=tolerance)
        flyAOA.StopOnRollAngle = True
        Assert.assertTrue(flyAOA.StopOnRollAngle)

        flyAOA.TurnDirection = AgEAvtrFlyAOALeftRight.eFlyAOANoRoll
        flyAOA.StopOnRollAngle = False
        Assert.assertFalse(flyAOA.StopOnRollAngle)

        def action224():
            flyAOA.RollRateMode = AgEAvtrPerfModelOverride.eOverride

        TryCatchAssertBlock.ExpectedException("must be", action224)

        def action225():
            flyAOA.OverrideRollRate = 29

        TryCatchAssertBlock.ExpectedException("must be", action225)

        def action226():
            flyAOA.ControlRollAngle = True

        TryCatchAssertBlock.ExpectedException("must be", action226)

        def action227():
            flyAOA.RollAngle = 59

        TryCatchAssertBlock.ExpectedException("must be", action227)

        airspeedOpts = flyAOA.AirspeedOptions
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverGlide
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverGlide(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.ProfileStrategyType = "Glide - Vertical Plane"
        glide: IBasicManeuverStrategyGlideProfile = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategyGlideProfile
        )

        glide.HoldInitialAirspeed = True
        Assert.assertTrue(glide.HoldInitialAirspeed)

        def action228():
            glide.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.5)

        TryCatchAssertBlock.ExpectedException("must be", action228)
        # BUG  missing Speed Mode     TryCatchAssertBlock.ExpectedException("must be", delegate () { glide.SpeedMode = ???; });

        glide.HoldInitialAirspeed = False
        Assert.assertFalse(glide.HoldInitialAirspeed)

        glide.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.5)  # BUG - sets to 0.257222
        Assert.assertAlmostEqual(0.5, glide.Airspeed, delta=1e-06)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, glide.AirspeedType)

        # BUG  missing Speed Mode   // glide.SpeedMode = ???;
        # Assert.AreEqual(???, glide.SpeedMode);

        glide.MinG = 0.6
        Assert.assertEqual(0.6, glide.MinG)

        glide.MaxG = 1.6
        Assert.assertEqual(1.6, glide.MaxG)

        glide.MaxSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated, glide.MaxSpeedLimits)
        glide.MaxSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated, glide.MaxSpeedLimits)
        glide.MaxSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated, glide.MaxSpeedLimits)
        glide.MaxSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated, glide.MaxSpeedLimits)

        glide.CompensateForCoriolisAccel = False
        Assert.assertFalse(glide.CompensateForCoriolisAccel)
        glide.CompensateForCoriolisAccel = True
        Assert.assertTrue(glide.CompensateForCoriolisAccel)

        glide.PoweredCruiseMode = AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyUnPoweredCruise
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyUnPoweredCruise, glide.PoweredCruiseMode
        )

        glide.PoweredCruiseThrottle = 20.0
        thrust1 = glide.PoweredCruiseThrustModel
        # TryCatchAssertBlock.ExpectedException("read only", delegate () { glide.PoweredCruiseThrottle = 20.0; });
        # TryCatchAssertBlock.ExpectedException("read only", delegate () { IAgAvtrPropulsionThrust thrust1 = glide.PoweredCruiseThrustModel; });

        glide.PoweredCruiseMode = AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyThrottle
        Assert.assertEqual(AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyThrottle, glide.PoweredCruiseMode)

        glide.PoweredCruiseThrottle = 30.0
        Assert.assertEqual(30.0, glide.PoweredCruiseThrottle)

        self.Test_IAgAvtrPropulsionThrust(glide.PoweredCruiseThrustModel)
        # TryCatchAssertBlock.ExpectedException("read only", delegate () { Test_IAgAvtrPropulsionThrust( glide.PoweredCruiseThrustModel); });

        glide.PoweredCruiseMode = AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyThrustModel
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyPoweredCruiseMode.eGlideSpecifyThrustModel, glide.PoweredCruiseMode
        )

        glide.PoweredCruiseThrottle = 20.0
        # TryCatchAssertBlock.ExpectedException("read only", delegate () { glide.PoweredCruiseThrottle = 20.0; });

        self.Test_IAgAvtrPropulsionThrust(glide.PoweredCruiseThrustModel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region Test_IAgAvtrPropulsionThrust
    def Test_IAgAvtrPropulsionThrust(self, thrust: "IPropulsionThrust"):
        thrust.UseConstantThrust = True
        Assert.assertTrue(thrust.UseConstantThrust)

        thrust.ConstantThrust = 111
        Assert.assertEqual(111, thrust.ConstantThrust)

        def action229():
            thrust.BoostThrust = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action229)

        def action230():
            thrust.BoostThrustTimeLimit = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action230)

        def action231():
            thrust.SustainThrust = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action231)

        def action232():
            thrust.SustainThrustTimeLimit = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action232)

        thrust.UseConstantThrust = False
        Assert.assertFalse(thrust.UseConstantThrust)

        thrust.BoostThrust = 222
        Assert.assertEqual(222, thrust.BoostThrust)
        thrust.BoostThrustTimeLimit = 333
        Assert.assertEqual(333, thrust.BoostThrustTimeLimit)

        thrust.SustainThrust = 444
        Assert.assertEqual(444, thrust.SustainThrust)
        thrust.SustainThrustTimeLimit = 555
        Assert.assertEqual(555, thrust.SustainThrustTimeLimit)

        def action233():
            thrust.ConstantThrust = 999

        TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action233)

        thrust.SetMinAirspeed(AgEAvtrAirspeedType.eMach, 666)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, thrust.MinAirspeedType)
        Assert.assertAlmostEqual(666, thrust.MinAirspeed, delta=1e-06)
        thrust.SetMinAirspeed(AgEAvtrAirspeedType.eEAS, 777)
        Assert.assertEqual(AgEAvtrAirspeedType.eEAS, thrust.MinAirspeedType)
        Assert.assertAlmostEqual(777, thrust.MinAirspeed, delta=1e-06)

        thrust.SetMaxAirspeed(AgEAvtrAirspeedType.eCAS, 888)
        Assert.assertEqual(AgEAvtrAirspeedType.eCAS, thrust.MaxAirspeedType)
        Assert.assertAlmostEqual(888, thrust.MaxAirspeed, delta=1e-06)
        thrust.SetMaxAirspeed(AgEAvtrAirspeedType.eTAS, 999)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, thrust.MaxAirspeedType)
        Assert.assertAlmostEqual(999, thrust.MaxAirspeed, delta=1e-06)

    # endregion

    # region BasicManeuverIntercept
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverIntercept(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Intercept"
        intercept: IBasicManeuverStrategyIntercept = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyIntercept
        )

        targetName = (EarlyBoundTests.AG_Target.ClassName + "/") + EarlyBoundTests.AG_Target.InstanceName

        def action234():
            intercept.TargetName = targetName

        TryCatchAssertBlock.ExpectedException("not a valid", action234)
        missile: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: IVehiclePropagatorBallistic = clr.CastAs(missile.Trajectory, IVehiclePropagatorBallistic)
        impactLocation: IVehicleImpactLocationPoint = clr.CastAs(traj.ImpactLocation, IVehicleImpactLocationPoint)
        impact: IVehicleImpactLLA = clr.CastAs(impactLocation.Impact, IVehicleImpactLLA)
        impact.Lat = -20
        impact.Lon = -20
        traj.Propagate()
        intercept.TargetName = "Missile/Missile"

        intercept.TargetResolution = 0.7
        Assert.assertEqual(0.7, intercept.TargetResolution)

        intercept.SetStopSlantRange(True, 2)
        Assert.assertTrue(intercept.UseStopSlantRange)
        Assert.assertEqual(2, intercept.StopSlantRange)

        intercept.SetStopTimeToGo(True, 11)
        Assert.assertTrue(intercept.UseStopTimeToGo)
        Assert.assertEqual(11, intercept.StopTimeToGo)

        intercept.InterceptMode = AgEAvtrInterceptMode.eTargetAspect
        intercept.TargetAspect = 0.1
        aspect = intercept.TargetAspect
        Assert.assertEqual(0.1, float(aspect))

        def action235():
            intercept.LateralSeparation = 2

        TryCatchAssertBlock.ExpectedException("must be", action235)

        intercept.InterceptMode = AgEAvtrInterceptMode.eLateralSeparation
        intercept.LateralSeparation = 2
        Assert.assertEqual(2, intercept.LateralSeparation)

        def action236():
            intercept.TargetAspect = 2

        TryCatchAssertBlock.ExpectedException("must be", action236)

        intercept.ManeuverFactor = 0.6
        Assert.assertEqual(0.6, intercept.ManeuverFactor)

        intercept.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(
            intercept.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel
        )
        intercept.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(intercept.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, intercept.ControlLimitHorizAccel, delta=tolerance)
        intercept.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(intercept.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(intercept.ControlLimitTurnRate), delta=tolerance)
        intercept.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(intercept.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
        Assert.assertEqual(700, intercept.ControlLimitTurnRadius)

        intercept.ClosureMode = AgEAvtrClosureMode.eClosureNotSet

        def action237():
            intercept.HOBSAngleTol = 2

        TryCatchAssertBlock.ExpectedException("must be", action237)

        def action238():
            intercept.HOBSMaxAngle = 5

        TryCatchAssertBlock.ExpectedException("must be", action238)

        intercept.ClosureMode = AgEAvtrClosureMode.eHOBS
        intercept.HOBSAngleTol = 2
        intercept.HOBSMaxAngle = 5
        angleTol = intercept.HOBSAngleTol
        Assert.assertEqual(2, float(angleTol))
        maxAngle = intercept.HOBSMaxAngle
        Assert.assertEqual(5, float(maxAngle))

        intercept.CompensateForCoriolisAccel = True
        Assert.assertTrue(intercept.CompensateForCoriolisAccel)

        missileObj: IStkObject = clr.CastAs(missile, IStkObject)
        missileObj.Unload()
        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverLoop
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverLoop(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Loop"
        loop: IBasicManeuverStrategyLoop = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyLoop)
        loop.LoopAngle = 359
        loopAngle = loop.LoopAngle
        loop.LoopAngleMode = AgEAvtrAngleMode.eRelativeAngle
        Assert.assertEqual(359, float(loopAngle))
        Assert.assertEqual(AgEAvtrAngleMode.eRelativeAngle, loop.LoopAngleMode)

        Assert.assertEqual("Loop", basicManeuver.ProfileStrategyType)
        loopProfile: IBasicManeuverStrategyLoop = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyLoop)
        loopAngleProfile = loopProfile.LoopAngle
        Assert.assertEqual(359, float(loopAngleProfile))
        Assert.assertEqual(AgEAvtrAngleMode.eRelativeAngle, loopProfile.LoopAngleMode)

        loop.HoldInitTAS = True

        def action239():
            loop.SetAirspeeds(AgEAvtrAirspeedType.eMach, 0.1, 0.2)

        TryCatchAssertBlock.ExpectedException("must be", action239)

        loop.HoldInitTAS = False
        loop.SetAirspeeds(AgEAvtrAirspeedType.eMach, 0.1, 0.2)
        Assert.assertEqual(0.1, loop.TopAirspeed)
        Assert.assertEqual(0.2, loop.BottomAirspeed)

        loop.SetAirspeeds(AgEAvtrAirspeedType.eTAS, 200, 201)
        Assert.assertEqual(200, loop.TopAirspeed)
        Assert.assertEqual(201, loop.BottomAirspeed)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverLTAHover
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverLTAHover(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Lighter Than Air Hover"
        hover: IBasicManeuverStrategyLTAHover = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyLTAHover)
        hover.HeadingRate = 1.5
        headingRate = hover.HeadingRate
        Assert.assertEqual(1.5, float(headingRate))

        Assert.assertEqual("Lighter Than Air Hover", basicManeuver.ProfileStrategyType)
        hoverProfile: IBasicManeuverStrategyLTAHover = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyLTAHover
        )
        headingRateProfile = hoverProfile.HeadingRate
        Assert.assertEqual(1.5, float(headingRateProfile))

        hover.HeadingMode = AgEAvtrHoverHeadingMode.eHoverIntoWind

        def action240():
            hover.AbsoluteHeading = 1.1

        TryCatchAssertBlock.ExpectedException("must be", action240)

        def action241():
            hover.UseMagneticHeading = True

        TryCatchAssertBlock.ExpectedException("must be", action241)

        def action242():
            hover.RelativeHeading = 2.2

        TryCatchAssertBlock.ExpectedException("must be", action242)

        hover.HeadingMode = AgEAvtrHoverHeadingMode.eHoverAbsolute
        hover.AbsoluteHeading = 1.1
        absHdg = hover.AbsoluteHeading
        Assert.assertEqual(1.1, float(absHdg))
        hover.UseMagneticHeading = True
        Assert.assertTrue(hover.UseMagneticHeading)

        hover.HeadingMode = AgEAvtrHoverHeadingMode.eHoverRelative
        hover.RelativeHeading = 2.2
        relHdg = hover.RelativeHeading
        Assert.assertEqual(2.2, float(relHdg))

        hover.AltitudeMode = AgEAvtrHoverAltitudeMode.eHoverHoldInitAltitude

        def action243():
            test = hover.AbsoluteAltitude

        TryCatchAssertBlock.ExpectedException("must be", action243)

        def action244():
            hover.AbsoluteAltitude = 10001

        TryCatchAssertBlock.ExpectedException("must be", action244)

        def action245():
            test = hover.AltitudeRate

        TryCatchAssertBlock.ExpectedException("must be", action245)

        def action246():
            hover.AltitudeRate = 1

        TryCatchAssertBlock.ExpectedException("must be", action246)

        def action247():
            test = hover.ControlAltRate

        TryCatchAssertBlock.ExpectedException("must be", action247)

        def action248():
            hover.ControlAltRate = 501

        TryCatchAssertBlock.ExpectedException("must be", action248)

        def action249():
            test = hover.RelativeAltitudeChange

        TryCatchAssertBlock.ExpectedException("must be", action249)

        def action250():
            hover.RelativeAltitudeChange = 1

        TryCatchAssertBlock.ExpectedException("must be", action250)

        def action251():
            test = hover.ParachuteArea

        TryCatchAssertBlock.ExpectedException("must be", action251)

        def action252():
            hover.ParachuteArea = 1

        TryCatchAssertBlock.ExpectedException("must be", action252)

        def action253():
            test = hover.ParachuteCd

        TryCatchAssertBlock.ExpectedException("must be", action253)

        def action254():
            hover.ParachuteCd = 1

        TryCatchAssertBlock.ExpectedException("must be", action254)

        hover.AltitudeMode = AgEAvtrHoverAltitudeMode.eHoverSpecifyAltitude
        hover.AbsoluteAltitude = 10001
        Assert.assertEqual(10001, hover.AbsoluteAltitude)
        hover.ControlAltRate = 501
        Assert.assertEqual(501, hover.ControlAltRate)

        hover.AltitudeMode = AgEAvtrHoverAltitudeMode.eHoverSpecifyAltitudeChange
        hover.RelativeAltitudeChange = 1
        Assert.assertEqual(1, hover.RelativeAltitudeChange)
        hover.ControlAltRate = 501
        Assert.assertEqual(501, hover.ControlAltRate)

        hover.AltitudeMode = AgEAvtrHoverAltitudeMode.eHoverSpecifyAltitudeRate
        hover.AltitudeRate = 501
        Assert.assertEqual(501, hover.AltitudeRate)

        hover.AltitudeMode = AgEAvtrHoverAltitudeMode.eHoverParachute
        hover.ParachuteArea = 10
        Assert.assertEqual(10, hover.ParachuteArea)
        hover.ParachuteCd = 1.1
        Assert.assertEqual(1.1, hover.ParachuteCd)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverPitch3D
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverPitch3D(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Pitch3D"
        pitch3D: IBasicManeuverStrategyPitch3D = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyPitch3D)

        pitch3D.ControlMode = AgEAvtrPitch3DControlMode.ePitch3DWindPushesVehicle
        Assert.assertEqual(AgEAvtrPitch3DControlMode.ePitch3DWindPushesVehicle, pitch3D.ControlMode)

        pitch3D.CommandFPA = 59
        fpa = pitch3D.CommandFPA
        Assert.assertAlmostEqual(59, float(fpa), delta=tolerance)

        pitch3D.ControlFPADot = 2
        fpaDot = pitch3D.ControlFPADot
        Assert.assertEqual(2, float(fpaDot))

        pitch3D.StopWhenFPAAchieved = False
        Assert.assertEqual(False, pitch3D.StopWhenFPAAchieved)

        self.BasicManeuverAirspeedOptions(pitch3D.AirspeedOptions)

        pitch3D.WindForceEffectiveArea = 11
        Assert.assertEqual(11, pitch3D.WindForceEffectiveArea)

        pitch3D.ControlMode = AgEAvtrPitch3DControlMode.ePitch3DCompensateForWind
        Assert.assertEqual(AgEAvtrPitch3DControlMode.ePitch3DCompensateForWind, pitch3D.ControlMode)

        def action255():
            pitch3D.WindForceEffectiveArea = 10

        TryCatchAssertBlock.ExpectedException("must be", action255)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverPull
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverPull(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Pull"
        pull: IBasicManeuverStrategyPull = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyPull)

        pull.ActiveMode = AgEAvtrPullMode.ePullToAngle
        pull.ActiveAngle = 59
        angle = pull.ActiveAngle
        Assert.assertAlmostEqual(59, float(angle), delta=tolerance)

        Assert.assertEqual("Pull", basicManeuver.ProfileStrategyType)
        pullProfile: IBasicManeuverStrategyPull = clr.CastAs(basicManeuver.Profile, IBasicManeuverStrategyPull)
        angleProfile = pullProfile.ActiveAngle
        Assert.assertAlmostEqual(59, float(angleProfile), delta=tolerance)

        pull.PullGMode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action256():
            pull.OverridePullG = 2

        TryCatchAssertBlock.ExpectedException("must be", action256)
        pull.PullGMode = AgEAvtrPerfModelOverride.eOverride
        pull.OverridePullG = 2
        Assert.assertEqual(2, pull.OverridePullG)

        airspeedOpts = pull.AirspeedOptions
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverPushPull
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverPushPull(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.ProfileStrategyType = "Profile Segment - Push/Pull"
        pushPull: IBasicManeuverStrategyPushPull = clr.CastAs(basicManeuver.Profile, IBasicManeuverStrategyPushPull)

        pushPull.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eWindFrame
        Assert.assertEqual(AgEAvtrBasicManeuverRefFrame.eWindFrame, pushPull.ReferenceFrame)

        pushPull.PushPull = AgEAvtrPushPull.ePushOver
        pushPull.PushPullG = 0.99
        Assert.assertEqual(0.99, pushPull.PushPullG)

        pushPull.AccelMode = AgEAvtrAccelMode.eAccel
        pushPull.AccelDecelG = 0.98
        Assert.assertEqual(0.98, pushPull.AccelDecelG)

        pushPull.StopFlightPathAngle = 5
        fpa = pushPull.StopFlightPathAngle
        Assert.assertEqual(5, float(fpa))

        pushPull.SetStopAirspeed(True, AgEAvtrAirspeedType.eTAS, 250)
        Assert.assertTrue(pushPull.UseStopAtAirspeed)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, pushPull.StopAirspeedType)
        Assert.assertEqual(250, pushPull.StopAirspeed)

        pushPull.SetStopAirspeed(False, AgEAvtrAirspeedType.eMach, 0.2)
        Assert.assertEqual(False, pushPull.UseStopAtAirspeed)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, pushPull.StopAirspeedType)
        Assert.assertEqual(0.2, pushPull.StopAirspeed)

        pushPull.SetStopAltitude(True, 100)
        Assert.assertEqual(100, pushPull.StopAltitude)

        pushPull.SetStopAltitudeRate(True, 0.1)
        Assert.assertAlmostEqual(0.1, pushPull.StopAltitudeRate, delta=tolerance)

        pushPull.CompensateForCoriolisAccel = True
        Assert.assertTrue(pushPull.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRelativeBearing
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRelativeBearing(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Relative Bearing"
        relBearing: IBasicManeuverStrategyRelativeBearing = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyRelativeBearing
        )

        validTargets = relBearing.ValidTargetNames
        targetName = (EarlyBoundTests.AG_Target.ClassName + "/") + EarlyBoundTests.AG_Target.InstanceName
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relBearing.TargetName = targetName
        Assert.assertEqual(targetName, relBearing.TargetName)

        relBearing.TargetResolution = 0.7
        Assert.assertEqual(0.7, relBearing.TargetResolution)

        relBearing.RelBearing = 1
        bearing = relBearing.RelBearing
        Assert.assertEqual(1, float(bearing))
        relBearing.MinRange = 0.5
        Assert.assertEqual(0.5, relBearing.MinRange)

        relBearing.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(
            relBearing.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel
        )
        relBearing.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(relBearing.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, relBearing.ControlLimitHorizAccel, delta=tolerance)
        relBearing.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(relBearing.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(relBearing.ControlLimitTurnRate), delta=tolerance)
        relBearing.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(relBearing.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
        Assert.assertEqual(700, relBearing.ControlLimitTurnRadius)

        relBearing.CompensateForCoriolisAccel = True
        Assert.assertTrue(relBearing.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRelativeCourse
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRelativeCourse(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Relative Course"
        relCourse: IBasicManeuverStrategyRelativeCourse = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyRelativeCourse
        )

        validTargets = relCourse.ValidTargetNames
        targetName = (EarlyBoundTests.AG_Target.ClassName + "/") + EarlyBoundTests.AG_Target.InstanceName
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relCourse.TargetName = targetName
        Assert.assertEqual(targetName, relCourse.TargetName)

        relCourse.TargetResolution = 0.7
        Assert.assertEqual(0.7, relCourse.TargetResolution)

        relCourse.Course = 1
        course = relCourse.Course
        Assert.assertEqual(1, float(course))
        relCourse.UseRelativeCourse = True
        Assert.assertTrue(relCourse.UseRelativeCourse)

        relCourse.InTrack = 1
        Assert.assertEqual(1, relCourse.InTrack)
        relCourse.CrossTrack = 2
        Assert.assertEqual(2, relCourse.CrossTrack)

        relCourse.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(
            relCourse.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel
        )
        relCourse.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(relCourse.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, relCourse.ControlLimitHorizAccel, delta=tolerance)
        relCourse.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(relCourse.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(relCourse.ControlLimitTurnRate), delta=tolerance)
        relCourse.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(relCourse.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
        Assert.assertEqual(700, relCourse.ControlLimitTurnRadius)

        relCourse.ClosureMode = AgEAvtrClosureMode.eClosureNotSet

        def action257():
            relCourse.DownrangeOffset = 0.5

        TryCatchAssertBlock.ExpectedException("must be", action257)

        def action258():
            relCourse.HOBSMaxAngle = 89

        TryCatchAssertBlock.ExpectedException("must be", action258)

        def action259():
            relCourse.HOBSAngleTol = 4

        TryCatchAssertBlock.ExpectedException("must be", action259)

        relCourse.ClosureMode = AgEAvtrClosureMode.eClosureRequired
        relCourse.DownrangeOffset = 0.5
        Assert.assertEqual(0.5, relCourse.DownrangeOffset)

        relCourse.ClosureMode = AgEAvtrClosureMode.eHOBS
        relCourse.HOBSMaxAngle = 89
        angleMax = relCourse.HOBSMaxAngle
        Assert.assertEqual(89, float(angleMax))
        relCourse.HOBSAngleTol = 4
        angleTol = relCourse.HOBSAngleTol
        Assert.assertEqual(4, float(angleTol))

        relCourse.CompensateForCoriolisAccel = True
        Assert.assertTrue(relCourse.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRelativeFPA
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRelativeFPA(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Relative Course"
        relCourse: IBasicManeuverStrategyRelativeCourse = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyRelativeCourse
        )

        validTargets = relCourse.ValidTargetNames
        targetName = (EarlyBoundTests.AG_Target.ClassName + "/") + EarlyBoundTests.AG_Target.InstanceName
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relCourse.TargetName = targetName
        Assert.assertEqual(targetName, relCourse.TargetName)

        basicManeuver.ProfileStrategyType = "Relative Flight Path Angle"
        relativeFPA: IBasicManeuverStrategyRelativeFPA = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategyRelativeFPA
        )

        relativeFPA.FPA = 5
        fpa = relativeFPA.FPA
        Assert.assertEqual(5, float(fpa))
        relativeFPA.AnchorAltOffset = 100
        Assert.assertEqual(100, relativeFPA.AnchorAltOffset)

        relativeFPA.ManeuverFactor = 0.7
        Assert.assertEqual(0.7, relativeFPA.ManeuverFactor)

        relativeFPA.SetControlLimit(AgEAvtrProfileControlLimit.eProfilePitchRate, 5)
        pitchRate = relativeFPA.ControlLimitPitchRate
        Assert.assertEqual(5, float(pitchRate))

        relativeFPA.SetMinAbsoluteAltitude(True, 2)
        Assert.assertEqual(2, relativeFPA.MinAbsoluteAltitude)

        relativeFPA.SetMaxAbsoluteAltitude(True, 10000)
        Assert.assertEqual(10000, relativeFPA.MaxAbsoluteAltitude)

        relativeFPA.SetMinAltitudeRelAnchor(True, 3)
        Assert.assertEqual(3, relativeFPA.MinAltitudeRelAnchor)

        relativeFPA.SetMaxAltitudeRelAnchor(True, 100)
        Assert.assertEqual(100, relativeFPA.MaxAltitudeRelAnchor)

        airspeedOpts = relativeFPA.AirspeedOptions
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        relativeFPA.CompensateForCoriolisAccel = True
        Assert.assertTrue(relativeFPA.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRelSpeedAlt
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRelSpeedAlt(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Relative Course"
        relCourse: IBasicManeuverStrategyRelativeCourse = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyRelativeCourse
        )

        validTargets = relCourse.ValidTargetNames
        targetName = (EarlyBoundTests.AG_Target.ClassName + "/") + EarlyBoundTests.AG_Target.InstanceName
        Assert.assertTrue((Array.Length(validTargets) > 0))
        relCourse.TargetName = targetName
        Assert.assertEqual(targetName, relCourse.TargetName)

        basicManeuver.ProfileStrategyType = "Relative Speed/Altitude"
        relSpeedAlt: IBasicManeuverStrategyRelSpeedAltitude = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategyRelSpeedAltitude
        )

        acObj: IStkObject = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        testAC = acObj.CopyObject("LeaderAC")
        relSpeedAlt.TargetName = "Aircraft/LeaderAC"
        Assert.assertEqual("Aircraft/LeaderAC", relSpeedAlt.TargetName)
        Assert.assertEqual(targetName, relCourse.TargetName)

        relSpeedAlt.TargetResolution = 4
        Assert.assertEqual(4, relSpeedAlt.TargetResolution)

        relSpeedAlt.RelativeAltitudeMode = AgEAvtrRelativeAltitudeMode.eHoldOffsetAlt
        relSpeedAlt.AltitudeOffset = 2
        Assert.assertEqual(2, relSpeedAlt.AltitudeOffset)

        def action260():
            relSpeedAlt.ElevationAngle = 5

        TryCatchAssertBlock.ExpectedException("must be", action260)

        relSpeedAlt.RelativeAltitudeMode = AgEAvtrRelativeAltitudeMode.eHoldElevationAngle
        relSpeedAlt.ElevationAngle = 5
        angle = relSpeedAlt.ElevationAngle
        Assert.assertEqual(5, float(angle))

        def action261():
            relSpeedAlt.AltitudeOffset = 2

        TryCatchAssertBlock.ExpectedException("must be", action261)

        relSpeedAlt.UsePerfModelLimits = True
        Assert.assertTrue(relSpeedAlt.UsePerfModelLimits)
        relSpeedAlt.UseTgtAspectForAirspeed = True
        Assert.assertTrue(relSpeedAlt.UseTgtAspectForAirspeed)

        relSpeedAlt.RangeForEqualSpeed = 2
        Assert.assertEqual(2, relSpeedAlt.RangeForEqualSpeed)
        relSpeedAlt.RangeToTransitionSpeed = 4
        Assert.assertEqual(4, relSpeedAlt.RangeToTransitionSpeed)

        relSpeedAlt.MinAltitude = 2
        Assert.assertEqual(2, relSpeedAlt.MinAltitude)
        relSpeedAlt.MaxAltitude = 50001
        Assert.assertEqual(50001, relSpeedAlt.MaxAltitude)

        relSpeedAlt.SetAirspeedOffset(AgEAvtrAirspeedType.eTAS, 5)
        Assert.assertEqual(5, relSpeedAlt.AirspeedOffset)
        relSpeedAlt.SetAirspeedOffset(AgEAvtrAirspeedType.eMach, 0.1)
        Assert.assertEqual(0.1, relSpeedAlt.AirspeedOffset)

        relSpeedAlt.SetMinAirspeed(AgEAvtrAirspeedType.eTAS, 100)
        Assert.assertEqual(100, relSpeedAlt.MinAirspeed)
        relSpeedAlt.SetMinAirspeed(AgEAvtrAirspeedType.eMach, 0.1)
        Assert.assertEqual(0.1, relSpeedAlt.MinAirspeed)

        relSpeedAlt.SetMaxAirspeed(AgEAvtrAirspeedType.eTAS, 200)
        Assert.assertEqual(200, relSpeedAlt.MaxAirspeed)
        relSpeedAlt.SetMaxAirspeed(AgEAvtrAirspeedType.eMach, 0.2)
        Assert.assertEqual(0.2, relSpeedAlt.MaxAirspeed)

        relSpeedAlt.StopCondition = AgEAvtrRelSpeedAltStopCondition.eRelSpeedAltStopAfterTargetCurrentProcedure
        Assert.assertEqual(
            AgEAvtrRelSpeedAltStopCondition.eRelSpeedAltStopAfterTargetCurrentProcedure, relSpeedAlt.StopCondition
        )

        relSpeedAlt.CompensateForCoriolisAccel = True
        Assert.assertTrue(relSpeedAlt.CompensateForCoriolisAccel)

        testAC.Unload()
        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRendezvousFormation
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRendezvousFormation(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        acObj: IStkObject = clr.CastAs(EarlyBoundTests.AG_AC, IStkObject)
        testAC = acObj.CopyObject("LeaderAC")

        basicManeuver.NavigationStrategyType = "Rendezvous/Formation"
        formation: IBasicManeuverStrategyRendezvous = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyRendezvous
        )

        targetName = (EarlyBoundTests.AG_Target.ClassName + "/") + EarlyBoundTests.AG_Target.InstanceName

        def action262():
            formation.TargetName = targetName

        TryCatchAssertBlock.ExpectedException("not a valid", action262)

        formation.TargetName = "Aircraft/LeaderAC"
        Assert.assertEqual("Aircraft/LeaderAC", formation.TargetName)

        formation.TargetResolution = 0.7
        Assert.assertEqual(0.7, formation.TargetResolution)

        formation.RelativeBearing = 179
        bearing = formation.RelativeBearing
        Assert.assertEqual(179, float(bearing))
        formation.RelativeRange = 4
        Assert.assertEqual(4, formation.RelativeRange)
        formation.AltitudeSplit = 200
        Assert.assertEqual(200, formation.AltitudeSplit)

        formation.UsePerfModelLimits = True

        def action263():
            formation.AltitudeRateControl = 1000

        TryCatchAssertBlock.ExpectedException("must be", action263)

        def action264():
            formation.MinLoadFactorG = -3

        TryCatchAssertBlock.ExpectedException("must be", action264)

        def action265():
            formation.MaxLoadFactorG = 3

        TryCatchAssertBlock.ExpectedException("must be", action265)

        formation.UsePerfModelLimits = False
        formation.AltitudeRateControl = 1000
        Assert.assertAlmostEqual(1000, formation.AltitudeRateControl, delta=tolerance)
        formation.MinLoadFactorG = -3
        Assert.assertEqual(-3, formation.MinLoadFactorG)
        formation.MaxLoadFactorG = 3
        Assert.assertEqual(3, formation.MaxLoadFactorG)

        formation.ManeuverFactor = 0.1
        Assert.assertAlmostEqual(0.1, formation.ManeuverFactor, delta=tolerance)

        formation.SetCPA(True, 150)
        Assert.assertEqual(150, formation.CPA)
        Assert.assertTrue(formation.EnableCollisionAvoidance)

        formation.MaxSpeedAdvantage = 51
        Assert.assertEqual(51, formation.MaxSpeedAdvantage)

        formation.AirspeedControlMode = AgEAvtrAccelPerfModelOverride.eAccelPerfModelValue

        def action266():
            testVal = formation.AccelDecelG

        TryCatchAssertBlock.ExpectedException("must be", action266)

        def action267():
            formation.AccelDecelG = 0.1

        TryCatchAssertBlock.ExpectedException("must be", action267)
        formation.AirspeedControlMode = AgEAvtrAccelPerfModelOverride.eAccelOverride
        formation.AccelDecelG = 0.1
        Assert.assertEqual(0.1, formation.AccelDecelG)

        formation.SetAirspeedFactor(True, 0.2)
        Assert.assertAlmostEqual(0.2, formation.AirspeedFactor, delta=tolerance)
        Assert.assertTrue(formation.UseSeparateAirspeedControl)

        testAC.Unload()
        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverRollingPull
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverRollingPull(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Rolling Pull"
        pull: IBasicManeuverStrategyRollingPull = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyRollingPull
        )
        pull.ActiveMode = AgEAvtrRollingPullMode.ePullToAngleMode
        pull.Angle = 10
        angle = pull.Angle
        Assert.assertAlmostEqual(10, float(angle), delta=tolerance)

        Assert.assertEqual("Rolling Pull", basicManeuver.ProfileStrategyType)
        pullProfile: IBasicManeuverStrategyRollingPull = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategyRollingPull
        )
        angleProfile = pullProfile.Angle
        Assert.assertAlmostEqual(10, float(angleProfile), delta=tolerance)

        def action268():
            pull.RollOrientation = AgEAvtrRollUprightInverted.eRollInverted

        TryCatchAssertBlock.ExpectedException("must be", action268)
        pull.ActiveMode = AgEAvtrRollingPullMode.eRollToOrientationMode
        pull.RollOrientation = AgEAvtrRollUprightInverted.eRollInverted
        Assert.assertEqual(AgEAvtrRollUprightInverted.eRollInverted, pull.RollOrientation)

        pull.RollRateMode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action269():
            testRate = pull.OverrideRollRate

        TryCatchAssertBlock.ExpectedException("must be", action269)
        pull.RollRateMode = AgEAvtrPerfModelOverride.eOverride
        pull.OverrideRollRate = 20
        overrideRollRate = pull.OverrideRollRate
        Assert.assertEqual(20, float(overrideRollRate))

        pull.PullGMode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action270():
            pull.OverridePullG = 2

        TryCatchAssertBlock.ExpectedException("must be", action270)
        pull.PullGMode = AgEAvtrPerfModelOverride.eOverride
        pull.OverridePullG = 2
        Assert.assertEqual(2, pull.OverridePullG)

        airspeedOpts = pull.AirspeedOptions
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverSimpleTurn
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverSimpleTurn(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Simple Turn"
        simpleTurn: IBasicManeuverStrategySimpleTurn = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategySimpleTurn
        )

        simpleTurn.ReferenceFrame = AgEAvtrBasicManeuverRefFrame.eEarthFrame
        Assert.assertEqual(AgEAvtrBasicManeuverRefFrame.eEarthFrame, simpleTurn.ReferenceFrame)

        simpleTurn.TurnAngle = 1.2
        turnAngle = simpleTurn.TurnAngle
        Assert.assertEqual(1.2, float(turnAngle))

        simpleTurn.TurnRadiusFactor = 1.1
        Assert.assertEqual(1.1, simpleTurn.TurnRadiusFactor)

        simpleTurn.CompensateForCoriolisAccel = True
        Assert.assertTrue(simpleTurn.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverSmoothAccel
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverSmoothAccel(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Smooth Accel"
        accel: IBasicManeuverStrategySmoothAccel = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategySmoothAccel
        )
        accel.RollRateDot = 29
        rateDot = accel.RollRateDot
        Assert.assertAlmostEqual(29, float(rateDot), delta=tolerance)

        Assert.assertEqual("Smooth Accel", basicManeuver.ProfileStrategyType)
        accelProfile: IBasicManeuverStrategySmoothAccel = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategySmoothAccel
        )
        rateDotProfile = accelProfile.RollRateDot
        Assert.assertAlmostEqual(29, float(rateDotProfile), delta=tolerance)

        accel.TurnDirection = AgEAvtrSmoothAccelLeftRight.eSmoothAccelLeft

        def action271():
            accel.PitchAngle = 89

        TryCatchAssertBlock.ExpectedException("must be", action271)

        def action272():
            accel.RollAngle = 89

        TryCatchAssertBlock.ExpectedException("must be", action272)

        def action273():
            accel.StopOnPitchAngle = True

        TryCatchAssertBlock.ExpectedException("must be", action273)

        def action274():
            accel.StopOnRollAngle = True

        TryCatchAssertBlock.ExpectedException("must be", action274)

        accel.ControlPitchAngle = True
        accel.PitchAngle = 89
        pitchAngle = accel.PitchAngle
        Assert.assertAlmostEqual(89, float(pitchAngle), delta=tolerance)
        accel.StopOnPitchAngle = True

        accel.ControlRollAngle = True
        accel.RollAngle = 89
        rollAngle = accel.RollAngle
        Assert.assertAlmostEqual(89, float(rollAngle), delta=tolerance)
        accel.StopOnRollAngle = True

        accel.StopOnRollAngle = False
        accel.ControlRollAngle = False
        accel.TurnDirection = AgEAvtrSmoothAccelLeftRight.eSmoothAccelNoRoll

        def action275():
            accel.RollAngle = 89

        TryCatchAssertBlock.ExpectedException("must be", action275)

        def action276():
            accel.ControlRollAngle = False

        TryCatchAssertBlock.ExpectedException("must be", action276)
        accel.StopOnRollAngle = True
        Assert.assertTrue(accel.StopOnRollAngle)

        airspeedOpts = accel.AirspeedOptions
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverSmoothTurn
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverSmoothTurn(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Smooth Turn"
        turn: IBasicManeuverStrategySmoothTurn = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategySmoothTurn)

        turn.HeadingChange = 89
        headingChange = turn.HeadingChange
        Assert.assertAlmostEqual(89, float(headingChange), delta=tolerance)

        Assert.assertEqual("Smooth Turn", basicManeuver.ProfileStrategyType)
        turnProfile: IBasicManeuverStrategySmoothTurn = clr.CastAs(
            basicManeuver.Profile, IBasicManeuverStrategySmoothTurn
        )
        headingChange = turnProfile.HeadingChange
        Assert.assertAlmostEqual(89, float(headingChange), delta=tolerance)

        turn.TurnMode = AgEAvtrSmoothTurnMode.eSmoothTurnLoadFactor

        def action277():
            turn.RollAngle = 5

        TryCatchAssertBlock.ExpectedException("must be", action277)
        turn.LoadFactorMode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action278():
            turn.OverrideLoadFactor = 1

        TryCatchAssertBlock.ExpectedException("must be", action278)
        turn.LoadFactorMode = AgEAvtrPerfModelOverride.eOverride
        turn.OverrideLoadFactor = 1
        Assert.assertEqual(1, turn.OverrideLoadFactor)

        turn.TurnMode = AgEAvtrSmoothTurnMode.eSmoothTurnRollAngle

        def action279():
            turn.LoadFactorMode = AgEAvtrPerfModelOverride.ePerfModelValue

        TryCatchAssertBlock.ExpectedException("must be", action279)
        turn.RollRateMode = AgEAvtrPerfModelOverride.ePerfModelValue

        def action280():
            turn.OverrideRollRate = 1

        TryCatchAssertBlock.ExpectedException("must be", action280)
        turn.RollRateMode = AgEAvtrPerfModelOverride.eOverride
        turn.OverrideRollRate = 1
        overrideRollRate = turn.OverrideRollRate
        Assert.assertEqual(1, float(overrideRollRate))

        turn.FPAMode = AgEAvtrSmoothTurnFPAMode.eSmoothTurnFPALevelOff
        Assert.assertEqual(AgEAvtrSmoothTurnFPAMode.eSmoothTurnFPALevelOff, turn.FPAMode)

        airspeedOpts = turn.AirspeedOptions
        self.BasicManeuverAirspeedOptions(airspeedOpts)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverStationkeeping
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverStationkeeping(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Stationkeeping"
        stationNav: IBasicManeuverStrategyStationkeeping = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyStationkeeping
        )

        targetName = (EarlyBoundTests.AG_Target.ClassName + "/") + EarlyBoundTests.AG_Target.InstanceName
        stationNav.TargetName = targetName
        Assert.assertEqual(targetName, stationNav.TargetName)

        stationNav.TargetResolution = 0.7
        Assert.assertEqual(0.7, stationNav.TargetResolution)

        stationNav.MaxTargetSpeedFraction = 40
        Assert.assertEqual(40, stationNav.MaxTargetSpeedFraction)

        stationNav.RelBearing = 89
        bearing = stationNav.RelBearing
        Assert.assertEqual(89, float(bearing))
        stationNav.RelRange = 2
        Assert.assertEqual(2, stationNav.RelRange)
        stationNav.DesiredRadius = 4
        Assert.assertEqual(4, stationNav.DesiredRadius)
        stationNav.ManeuverFactor = 6
        Assert.assertEqual(6, stationNav.ManeuverFactor)

        stationNav.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(
            stationNav.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel
        )
        stationNav.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(stationNav.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, stationNav.ControlLimitHorizAccel, delta=tolerance)
        stationNav.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(stationNav.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(stationNav.ControlLimitTurnRate), delta=tolerance)
        stationNav.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(stationNav.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
        Assert.assertEqual(700, stationNav.ControlLimitTurnRadius)

        scenario: IScenario = clr.CastAs(EarlyBoundTests.AG_Scenario, IScenario)
        stationNav.StopCondition = AgEAvtrStationkeepingStopCondition.eStopConditionNotSet
        Assert.assertEqual(stationNav.StopCondition, AgEAvtrStationkeepingStopCondition.eStopConditionNotSet)

        def action281():
            testVal = stationNav.StopAfterDuration

        TryCatchAssertBlock.ExpectedException("must be", action281)

        def action282():
            testVal = stationNav.StopAfterTime

        TryCatchAssertBlock.ExpectedException("must be", action282)

        def action283():
            testVal = stationNav.StopAfterTurnCount

        TryCatchAssertBlock.ExpectedException("must be", action283)

        def action284():
            stationNav.StopAfterDuration = 2

        TryCatchAssertBlock.ExpectedException("must be", action284)

        def action285():
            stationNav.StopAfterTime = scenario.StopTime

        TryCatchAssertBlock.ExpectedException("must be", action285)

        def action286():
            stationNav.StopAfterTurnCount = 5

        TryCatchAssertBlock.ExpectedException("must be", action286)

        def action287():
            stationNav.StopCourse = 2

        TryCatchAssertBlock.ExpectedException("must be", action287)

        def action288():
            stationNav.UseRelativeCourse = True

        TryCatchAssertBlock.ExpectedException("must be", action288)

        stationNav.StopCondition = AgEAvtrStationkeepingStopCondition.eStopAfterTurnCount
        Assert.assertEqual(stationNav.StopCondition, AgEAvtrStationkeepingStopCondition.eStopAfterTurnCount)
        stationNav.StopAfterTurnCount = 5
        Assert.assertEqual(5, stationNav.StopAfterTurnCount)
        stationNav.UseRelativeCourse = True
        stationNav.StopCourse = 2
        course = stationNav.StopCourse
        Assert.assertTrue(stationNav.UseRelativeCourse)
        Assert.assertEqual(2, float(course))

        stationNav.StopCondition = AgEAvtrStationkeepingStopCondition.eStopAfterTime
        Assert.assertEqual(stationNav.StopCondition, AgEAvtrStationkeepingStopCondition.eStopAfterTime)
        stationNav.StopAfterTime = scenario.StopTime
        time = stationNav.StopAfterTime
        Assert.assertEqual(scenario.StopTime, time)

        stationNav.StopCondition = AgEAvtrStationkeepingStopCondition.eStopAfterDuration
        Assert.assertEqual(stationNav.StopCondition, AgEAvtrStationkeepingStopCondition.eStopAfterDuration)
        stationNav.StopAfterDuration = 2
        Assert.assertEqual(2, stationNav.StopAfterDuration)

        stationNav.CompensateForCoriolisAccel = True
        Assert.assertTrue(stationNav.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverStraightAhead
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverStraightAhead(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Straight Ahead"
        straightAhead: IBasicManeuverStrategyStraightAhead = clr.CastAs(
            basicManeuver.Navigation, IBasicManeuverStrategyStraightAhead
        )

        straightAhead.ReferenceFrame = AgEAvtrStraightAheadRefFrame.eMaintainCourse
        Assert.assertEqual(AgEAvtrStraightAheadRefFrame.eMaintainCourse, straightAhead.ReferenceFrame)

        straightAhead.CompensateForCoriolisAccel = True
        Assert.assertTrue(straightAhead.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region BasicManeuverWeave
    @category("Basic Maneuver Procedure Tests")
    def test_BasicManeuverWeave(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        basicManeuver: IProcedureBasicManeuver = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteEndOfPrevProcedure, AgEAvtrProcedureType.eProcBasicManeuver
            ),
            IProcedureBasicManeuver,
        )

        basicManeuver.NavigationStrategyType = "Weave"
        weave: IBasicManeuverStrategyWeave = clr.CastAs(basicManeuver.Navigation, IBasicManeuverStrategyWeave)

        weave.HeadingChange = 45
        heading = weave.HeadingChange
        Assert.assertEqual(45, float(heading))
        weave.MaxNumCycles = 3
        Assert.assertEqual(3, weave.MaxNumCycles)
        weave.MaxDistance = 11
        Assert.assertEqual(11, weave.MaxDistance)

        weave.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel, 0)
        Assert.assertEqual(weave.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavUseAccelPerfModel)
        weave.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel, 0.1)
        Assert.assertEqual(weave.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxHorizAccel)
        Assert.assertAlmostEqual(0.1, weave.ControlLimitHorizAccel, delta=tolerance)
        weave.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate, 0.2)
        Assert.assertEqual(weave.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMaxTurnRate)
        Assert.assertAlmostEqual(0.2, float(weave.ControlLimitTurnRate), delta=tolerance)
        weave.SetControlLimit(AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius, 700)
        Assert.assertEqual(weave.ControlLimitMode, AgEAvtrBasicManeuverStrategyNavControlLimit.eNavMinTurnRadius)
        Assert.assertEqual(700, weave.ControlLimitTurnRadius)

        weave.CompensateForCoriolisAccel = True
        Assert.assertTrue(weave.CompensateForCoriolisAccel)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(basicManeuver, IProcedure))

    # endregion

    # region RelativeToPrevProcedure
    @category("Site Tests")
    def test_RelativeToPrevProcedure(self):
        self.EmptyProcedures()

        areaTarget = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget")
        place = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.ePlace, "Place")

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        proc2 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRelativeToPrevProcedure, AgEAvtrProcedureType.eProcEnroute
        )
        relToPrevProc: ISiteRelToPrevProcedure = clr.CastAs(proc2.Site, ISiteRelToPrevProcedure)

        self.TestSiteName(relToPrevProc.GetAsSite(), "Relative to Previous Procedure")

        relToPrevProc.BearingMode = AgEAvtrRelAbsBearing.eTrueBearing
        Assert.assertEqual(AgEAvtrRelAbsBearing.eTrueBearing, relToPrevProc.BearingMode)
        relToPrevProc.Bearing = 3
        bearing = relToPrevProc.Bearing
        Assert.assertEqual(3, float(bearing))
        relToPrevProc.Range = 11
        Assert.assertEqual(11, relToPrevProc.Range)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        EarlyBoundTests.AG_Procedures.Remove(proc2)
        areaTarget.Unload()
        place.Unload()

    # endregion

    # region RelativeToStationarySTKObject
    @category("Site Tests")
    def test_RelativeToStationarySTKObject(self):
        self.EmptyProcedures()

        areaTarget = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget")
        place = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.ePlace, "Place")

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteRelativeToStationarySTKObject, AgEAvtrProcedureType.eProcEnroute
        )
        relToSTKObject: ISiteRelToSTKObject = clr.CastAs(proc1.Site, ISiteRelToSTKObject)

        self.TestSiteName(relToSTKObject.GetAsSite(), "Relative to stationary STK Object Site")

        relToSTKObject.ObjectName = "Place/Place"
        name = relToSTKObject.ObjectName
        Assert.assertTrue(("Place/Place" == str(name)))

        names = relToSTKObject.ValidObjectNames
        Assert.assertTrue((Array.Length(names) >= 2))

        relToSTKObject.Bearing = 5
        bearing = relToSTKObject.Bearing
        Assert.assertEqual(5, float(bearing))
        relToSTKObject.UseMagneticBearing = True
        Assert.assertTrue(relToSTKObject.UseMagneticBearing)

        relToSTKObject.Range = 11
        Assert.assertEqual(11, relToSTKObject.Range)

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        areaTarget.Unload()
        place.Unload()

    # endregion

    # region SiteAirportFromCatalog
    @category("Site Tests")
    @category("ARINC424 Test")
    def test_SiteAirportFromCatalog(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteAirportFromCatalog, AgEAvtrProcedureType.eProcTakeoff
        )
        catAirport: ISiteAirportFromCatalog = clr.CastAs(proc1.Site, ISiteAirportFromCatalog)

        arincAirports = EarlyBoundTests.AG_AvtrCatalog.AirportCategory.ARINC424Airports
        arincSource: ICatalogSource = clr.CastAs(arincAirports, ICatalogSource)
        arincNames = arincSource.ChildNames
        firstArincAirport = arincAirports.GetARINC424Item(str(arincNames[0]))
        catAirport.SetCatalogAirport(clr.CastAs(firstArincAirport, ICatalogAirport))
        arincName = firstArincAirport.GetAsCatalogItem().Name
        Assert.assertEqual(arincName, catAirport.GetAsSite().Name)
        arincAirport2: ICatalogItem = clr.CastAs(catAirport.GetCatalogAirport(), ICatalogItem)
        Assert.assertEqual(arincName, arincAirport2.Name)

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region SiteNavaidFromCatalog
    @category("Site Tests")
    @category("ARINC424 Test")
    def test_SiteNavaidFromCatalog(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteNavaidFromCatalog, AgEAvtrProcedureType.eProcEnroute
        )
        catNavaid: ISiteNavaidFromCatalog = clr.CastAs(proc1.Site, ISiteNavaidFromCatalog)

        arincNavaids = EarlyBoundTests.AG_AvtrCatalog.NavaidCategory.ARINC424Navaids
        arincSource: ICatalogSource = clr.CastAs(arincNavaids, ICatalogSource)
        arincNames = arincSource.ChildNames
        firstArincNavaid = arincNavaids.GetARINC424Item(str(arincNames[0]))
        catNavaid.SetCatalogNavaid(clr.CastAs(firstArincNavaid, ICatalogNavaid))
        arincName = firstArincNavaid.GetAsCatalogItem().Name
        Assert.assertEqual(arincName, catNavaid.GetAsSite().Name)
        arincNavaid2: ICatalogItem = clr.CastAs(catNavaid.GetCatalogNavaid(), ICatalogItem)
        Assert.assertEqual(arincName, arincNavaid2.Name)

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region SiteRunway
    @category("Site Tests")
    def test_SiteRunway(self):
        tolerance = 1e-09

        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        runway: ISiteRunway = clr.CastAs(proc1.Site, ISiteRunway)

        self.TestSiteName(runway.GetAsSite(), "Runway")

        runway.Latitude = 1
        lat = runway.Latitude
        Assert.assertEqual(1, float(lat))
        runway.Longitude = 2
        lon = runway.Longitude
        Assert.assertEqual(2, float(lon))
        runway.Altitude = 5
        Assert.assertEqual(5, runway.Altitude)
        runway.AltitudeRef = AgEAvtrAGLMSL.eAltMSL
        Assert.assertEqual(AgEAvtrAGLMSL.eAltMSL, runway.AltitudeRef)

        runway.HighEndHeading = 195
        highEndHeading = runway.HighEndHeading
        Assert.assertAlmostEqual(195, float(highEndHeading), delta=tolerance)
        lowEndHeading = runway.LowEndHeading
        Assert.assertAlmostEqual(15, float(lowEndHeading), delta=tolerance)
        runway.IsMagnetic = False
        Assert.assertEqual(False, runway.IsMagnetic)

        runway.Length = 5
        Assert.assertEqual(5, runway.Length)

        runway.AddToCatalog(True)

        runway.Latitude = 0
        lat = runway.Latitude
        Assert.assertEqual(0, float(lat))
        runway.Longitude = 0
        lon = runway.Longitude
        Assert.assertEqual(0, float(lon))
        runway.Altitude = 0
        Assert.assertEqual(0, runway.Altitude)

        # Copy the catalog runway you just created
        catRunway = EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.UserRunways.GetUserRunway("Runway")
        runway.CopyFromCatalog(clr.CastAs(catRunway, ICatalogRunway))

        lat = runway.Latitude
        Assert.assertEqual(1, float(lat))
        runway.Longitude = 2
        lon = runway.Longitude
        Assert.assertEqual(2, float(lon))
        runway.Altitude = 5
        Assert.assertEqual(5, runway.Altitude)

        def action289():
            runway.AddToCatalog(False)

        TryCatchAssertBlock.ExpectedException("", action289)

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region SiteWaypoint
    @category("Site Tests")
    def test_SiteWaypoint(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteWaypoint, AgEAvtrProcedureType.eProcEnroute)
        waypoint: ISiteWaypoint = clr.CastAs(proc1.Site, ISiteWaypoint)

        self.TestSiteName(waypoint.GetAsSite(), "Waypoint")

        waypoint.Latitude = 1
        lat = waypoint.Latitude
        Assert.assertEqual(1, float(lat))
        waypoint.Longitude = 2
        lon = waypoint.Longitude
        Assert.assertEqual(2, float(lon))

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region SiteReferenceState
    @category("Site Tests")
    def test_SiteReferenceState(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteReferenceState, AgEAvtrProcedureType.eProcReferenceState
        )
        refStateSite: ISiteReferenceState = clr.CastAs(proc1.Site, ISiteReferenceState)

        self.TestSiteName(refStateSite.GetAsSite(), "Reference State Site")

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region STKAreaTarget
    @category("Site Tests")
    def test_STKAreaTarget(self):
        self.EmptyProcedures()

        areaTarget = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget")
        areaTarget2 = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget2")

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteSTKAreaTarget, AgEAvtrProcedureType.eProcAreaTargetSearch
        )
        atSite: ISiteSTKAreaTarget = clr.CastAs(proc1.Site, ISiteSTKAreaTarget)

        atSite.ObjectName = "AreaTarget/AreaTarget2"
        name = atSite.ObjectName
        Assert.assertTrue(("AreaTarget/AreaTarget2" == str(name)))

        names = atSite.ValidObjectNames
        Assert.assertTrue((Array.Length(names) >= 2))

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        areaTarget.Unload()
        areaTarget2.Unload()

    # endregion

    # region SiteDynState
    @category("Site Tests")
    def test_SiteDynState(self):
        self.EmptyProcedures()

        missile: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: IVehiclePropagatorBallistic = clr.CastAs(missile.Trajectory, IVehiclePropagatorBallistic)
        impactLocation: IVehicleImpactLocationPoint = clr.CastAs(traj.ImpactLocation, IVehicleImpactLocationPoint)
        impact: IVehicleImpactLLA = clr.CastAs(impactLocation.Impact, IVehicleImpactLLA)
        impact.Lat = -20
        impact.Lon = -20
        traj.Propagate()

        missile2: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile2")), IMissile
        )
        traj2: IVehiclePropagatorBallistic = clr.CastAs(missile2.Trajectory, IVehiclePropagatorBallistic)
        impactLocation2: IVehicleImpactLocationPoint = clr.CastAs(traj2.ImpactLocation, IVehicleImpactLocationPoint)
        impact2: IVehicleImpactLLA = clr.CastAs(impactLocation2.Impact, IVehicleImpactLLA)
        impact2.Lat = -20
        impact2.Lon = -20
        traj2.Propagate()

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteDynState, AgEAvtrProcedureType.eProcLaunchDynState
        )
        dynState: ISiteDynState = clr.CastAs(proc1.Site, ISiteDynState)

        dynState.ObjectName = "Missile/Missile2"
        name = dynState.ObjectName
        Assert.assertTrue(("Missile/Missile2" == str(name)))

        names = dynState.ValidObjectNames
        Assert.assertTrue((Array.Length(names) >= 2))

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        missileObj: IStkObject = clr.CastAs(missile, IStkObject)
        missileObj.Unload()
        missileObj2: IStkObject = clr.CastAs(missile2, IStkObject)
        missileObj2.Unload()

    # endregion

    # region STKObjectWaypoint
    @category("Site Tests")
    def test_STKObjectWaypoint(self):
        self.EmptyProcedures()

        areaTarget = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget")
        place = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.ePlace, "Place")

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteSTKObjectWaypoint, AgEAvtrProcedureType.eProcEnroute
        )
        objectWaypointSite: ISiteSTKObjectWaypoint = clr.CastAs(proc1.Site, ISiteSTKObjectWaypoint)

        self.TestSiteName(objectWaypointSite.GetAsSite(), "STK Object Waypoint Site")

        objectWaypointSite.ObjectName = "Place/Place"
        name = objectWaypointSite.ObjectName
        Assert.assertTrue(("Place/Place" == str(name)))

        names = objectWaypointSite.ValidObjectNames
        Assert.assertTrue((Array.Length(names) >= 2))

        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        scenario: IScenario = clr.CastAs(EarlyBoundTests.AG_Scenario, IScenario)

        objectWaypointSite.MinimizeSiteProcTimeDiff = AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceOff
        Assert.assertEqual(
            AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceOff, objectWaypointSite.MinimizeSiteProcTimeDiff
        )

        minTime = objectWaypointSite.MinTime
        Assert.assertTrue(("Unlimited" == str(minTime)))
        maxTime = objectWaypointSite.MaxTime
        Assert.assertTrue(("Unlimited" == str(maxTime)))

        objectWaypointSite.WaypointTime = 30
        Assert.assertEqual(30, objectWaypointSite.WaypointTime)

        objectWaypointSite.MinimizeSiteProcTimeDiff = AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceNextUpdate
        Assert.assertEqual(
            AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceNextUpdate,
            objectWaypointSite.MinimizeSiteProcTimeDiff,
        )
        objectWaypointSite.MinimizeSiteProcTimeDiff = AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceAlways
        Assert.assertEqual(
            AgEAvtrMinimizeSiteProcTimeDiff.eMinimizeTimeDifferenceAlways, objectWaypointSite.MinimizeSiteProcTimeDiff
        )

        def action290():
            objectWaypointSite.WaypointTime = 5

        TryCatchAssertBlock.ExpectedException("must be", action290)

        objectWaypointSite.OffsetMode = AgEAvtrSTKObjectWaypointOffsetMode.eOffsetNone
        Assert.assertEqual(AgEAvtrSTKObjectWaypointOffsetMode.eOffsetNone, objectWaypointSite.OffsetMode)

        def action291():
            objectWaypointSite.Bearing = 1

        TryCatchAssertBlock.ExpectedException("must be", action291)

        def action292():
            objectWaypointSite.UseMagneticBearing = True

        TryCatchAssertBlock.ExpectedException("must be", action292)

        def action293():
            objectWaypointSite.Range = 10

        TryCatchAssertBlock.ExpectedException("must be", action293)

        def action294():
            objectWaypointSite.VGTPoint = "SubPoint(Detic)"

        TryCatchAssertBlock.ExpectedException("must be", action294)

        objectWaypointSite.OffsetMode = AgEAvtrSTKObjectWaypointOffsetMode.eOffsetBearingRange
        Assert.assertEqual(AgEAvtrSTKObjectWaypointOffsetMode.eOffsetBearingRange, objectWaypointSite.OffsetMode)
        objectWaypointSite.Bearing = 1
        Assert.assertEqual(1, objectWaypointSite.Bearing)
        objectWaypointSite.UseMagneticBearing = True
        Assert.assertTrue(objectWaypointSite.UseMagneticBearing)
        objectWaypointSite.Range = 10
        Assert.assertEqual(10, objectWaypointSite.Range)

        objectWaypointSite.OffsetMode = AgEAvtrSTKObjectWaypointOffsetMode.eOffsetRelativeBearingRange
        Assert.assertEqual(
            AgEAvtrSTKObjectWaypointOffsetMode.eOffsetRelativeBearingRange, objectWaypointSite.OffsetMode
        )
        objectWaypointSite.Bearing = 1
        Assert.assertEqual(1, objectWaypointSite.Bearing)
        objectWaypointSite.Range = 10
        Assert.assertEqual(10, objectWaypointSite.Range)

        def action295():
            objectWaypointSite.UseMagneticBearing = True

        TryCatchAssertBlock.ExpectedException("must be", action295)

        objectWaypointSite.OffsetMode = AgEAvtrSTKObjectWaypointOffsetMode.eOffsetVGTPoint
        objectWaypointSite.VGTPoint = "SubPoint(Detic)"
        Assert.assertEqual("SubPoint(Detic)", objectWaypointSite.VGTPoint)

        TestBase.Application.UnitPreferences.ResetUnits()
        EarlyBoundTests.AG_Procedures.Remove(proc1)
        areaTarget.Unload()
        place.Unload()

    # endregion

    # region STKStaticObject
    @category("Site Tests")
    def test_STKStaticObject(self):
        self.EmptyProcedures()

        areaTarget = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget")
        place = EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.ePlace, "Place")

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteSTKStaticObject, AgEAvtrProcedureType.eProcEnroute
        )
        staticObjectSite: ISiteSTKStaticObject = clr.CastAs(proc1.Site, ISiteSTKStaticObject)

        self.TestSiteName(staticObjectSite.GetAsSite(), "STK Static Object Site")

        staticObjectSite.ObjectName = "Place/Place"
        name = staticObjectSite.ObjectName
        Assert.assertTrue(("Place/Place" == str(name)))

        names = staticObjectSite.ValidObjectNames
        Assert.assertTrue((Array.Length(names) >= 2))

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        areaTarget.Unload()
        place.Unload()

    # endregion

    # region STKVehicle
    @category("Site Tests")
    def test_STKVehicle(self):
        self.EmptyProcedures()

        missile: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile")), IMissile
        )
        traj: IVehiclePropagatorBallistic = clr.CastAs(missile.Trajectory, IVehiclePropagatorBallistic)
        impactLocation: IVehicleImpactLocationPoint = clr.CastAs(traj.ImpactLocation, IVehicleImpactLocationPoint)
        impact: IVehicleImpactLLA = clr.CastAs(impactLocation.Impact, IVehicleImpactLLA)
        impact.Lat = -20
        impact.Lon = -20
        traj.Propagate()

        missile2: IMissile = clr.CastAs(
            (EarlyBoundTests.AG_Scenario.Children.New(AgESTKObjectType.eMissile, "Missile2")), IMissile
        )
        traj2: IVehiclePropagatorBallistic = clr.CastAs(missile2.Trajectory, IVehiclePropagatorBallistic)
        impactLocation2: IVehicleImpactLocationPoint = clr.CastAs(traj2.ImpactLocation, IVehicleImpactLocationPoint)
        impact2: IVehicleImpactLLA = clr.CastAs(impactLocation2.Impact, IVehicleImpactLLA)
        impact2.Lat = -20
        impact2.Lon = -20
        traj2.Propagate()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteSTKVehicle, AgEAvtrProcedureType.eProcLaunch)
        stkVehicleSite: ISiteSTKVehicle = clr.CastAs(proc1.Site, ISiteSTKVehicle)

        stkVehicleSite.ObjectName = "Missile/Missile2"
        name = stkVehicleSite.ObjectName
        Assert.assertTrue(("Missile/Missile2" == str(name)))

        names = stkVehicleSite.ValidObjectNames
        Assert.assertTrue((Array.Length(names) >= 2))

        EarlyBoundTests.AG_Procedures.Remove(proc1)
        missileObj: IStkObject = clr.CastAs(missile, IStkObject)
        missileObj.Unload()
        missileObj2: IStkObject = clr.CastAs(missile2, IStkObject)
        missileObj2.Unload()

    # endregion

    # region SuperProcedure
    @category("Procedure Tests")
    def test_SuperProcedure(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(AgEAvtrSiteType.eSiteRunway, AgEAvtrProcedureType.eProcTakeoff)
        superProc: IProcedureSuperProcedure = clr.CastAs(
            EarlyBoundTests.AG_Procedures.Add(
                AgEAvtrSiteType.eSiteSuperProcedure, AgEAvtrProcedureType.eProcSuperProcedure
            ),
            IProcedureSuperProcedure,
        )

        self.TestProcedureName(superProc.GetAsProcedure(), "Super Procedure")

        Assert.assertEqual(False, EarlyBoundTests.AG_Mission.IsValid)

        nonexistingfilepath = TestBase.GetScenarioFile("DoesNotExist.flightprocs")

        def action296():
            superProc.LoadProceduresFromFile(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("", action296)

        filepath = TestBase.GetScenarioFile("basicManeuver.flightprocs")
        superProc.LoadProceduresFromFile(filepath)
        Assert.assertTrue(EarlyBoundTests.AG_Mission.IsValid)

        EarlyBoundTests.AG_Procedures.Remove(clr.CastAs(superProc, IProcedure))
        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region SiteSuperProcedure
    @category("Site Tests")
    def test_SiteSuperProcedure(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteSuperProcedure, AgEAvtrProcedureType.eProcSuperProcedure
        )
        superProcSite: ISiteSuperProcedure = clr.CastAs(proc1.Site, ISiteSuperProcedure)

        self.TestSiteName(superProcSite.GetAsSite(), "Super Procedure Site")

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region SiteVTOLPoint
    @category("Site Tests")
    def test_SiteVTOLPoint(self):
        self.EmptyProcedures()

        proc1 = EarlyBoundTests.AG_Procedures.Add(
            AgEAvtrSiteType.eSiteVTOLPoint, AgEAvtrProcedureType.eProcVerticalTakeoff
        )
        vtolSite: ISiteVTOLPoint = clr.CastAs(proc1.Site, ISiteVTOLPoint)

        vtolSite.Latitude = 1
        lat = vtolSite.Latitude
        Assert.assertEqual(1, float(lat))
        vtolSite.Longitude = 2
        lon = vtolSite.Longitude
        Assert.assertEqual(2, float(lon))
        vtolSite.Altitude = 101
        Assert.assertEqual(101, vtolSite.Altitude)
        vtolSite.AltitudeReference = AgEAvtrAGLMSL.eAltAGL
        Assert.assertEqual(AgEAvtrAGLMSL.eAltAGL, vtolSite.AltitudeReference)

        EarlyBoundTests.AG_Procedures.Remove(proc1)

    # endregion

    # region ReadOnlyCatalogItem
    @category("Aircraft Tests")
    def test_ReadOnlyCatalogItem(self):
        basicAirliner = EarlyBoundTests.AG_AvtrAircraftModels.GetAircraft("Basic Airliner")
        acAsCatalogItem = basicAirliner.GetAsCatalogItem()
        Assert.assertEqual("Basic Airliner", acAsCatalogItem.Name)

        def action297():
            acAsCatalogItem.Name = ""

        TryCatchAssertBlock.ExpectedException("read-only", action297)

        Assert.assertEqual("Basic Airliner", acAsCatalogItem.Name)

        isReadOnly = acAsCatalogItem.IsReadOnly
        Assert.assertTrue(isReadOnly)

        def action298():
            acAsCatalogItem.Remove()

        TryCatchAssertBlock.ExpectedException("read-only", action298)

    # endregion

    # region AircraftModel
    @category("Aircraft Tests")
    def test_AircraftModel(self):
        acModelsAsCatalogSource = EarlyBoundTests.AG_AvtrAircraftModels.GetAsCatalogSource()

        containsTestAircraft = acModelsAsCatalogSource.Contains("NUNIT CSharp Test")
        Assert.assertTrue(containsTestAircraft)

        acTestAsCatalogItem = EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem()
        containsTest = acTestAsCatalogItem.ContainsChildItem("Cruise")
        Assert.assertTrue(containsTest)
        containsTest = acTestAsCatalogItem.ContainsChildItem("Airplane")
        Assert.assertFalse(containsTest)

        Assert.assertEqual("NUNIT CSharp Test", acTestAsCatalogItem.Name)
        acTestAsCatalogItem.Name = "NUNIT CSharp Test NameChange"
        Assert.assertEqual("NUNIT CSharp Test NameChange", acTestAsCatalogItem.Name)
        acTestAsCatalogItem.Name = "NUNIT CSharp Test"

        isReadOnly = acTestAsCatalogItem.IsReadOnly
        Assert.assertFalse(isReadOnly)

        perfModelNames = acTestAsCatalogItem.ChildNames
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
        tolerance = 1e-09

        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.WingArea = 300
        Assert.assertEqual(300, advFWT.WingArea)
        advFWT.FlapsArea = 50
        Assert.assertEqual(50, advFWT.FlapsArea)
        advFWT.SpeedbrakesArea = 10
        Assert.assertEqual(10, advFWT.SpeedbrakesArea)

        advFWT.MaxAltitude = 65000
        Assert.assertEqual(65000, advFWT.MaxAltitude)
        advFWT.MaxMach = 0.98
        Assert.assertEqual(0.98, advFWT.MaxMach)
        advFWT.MaxEAS = 460
        Assert.assertAlmostEqual(460, advFWT.MaxEAS, delta=tolerance)
        advFWT.MinLoadFactor = -2.5
        Assert.assertEqual(-2.5, advFWT.MinLoadFactor)
        advFWT.MaxLoadFactor = 4.5
        Assert.assertEqual(4.5, advFWT.MaxLoadFactor)

        advFWT.UseMaxTemperatureLimit = True
        Assert.assertTrue(advFWT.UseMaxTemperatureLimit)
        advFWT.MaxTemperature = 900
        Assert.assertEqual(900, advFWT.MaxTemperature)

        advFWT.CacheAeroData = False
        Assert.assertEqual(False, advFWT.CacheAeroData)
        advFWT.CacheFuelFlow = False
        Assert.assertEqual(False, advFWT.CacheFuelFlow)

        advFWT.CreateAllPerfModels("CreateAllPerfModelsTest", True, False)
        tempAC.Acceleration.GetAdvAccelerationByName("CreateAllPerfModelsTest")
        tempAC.Climb.GetAdvClimbByName("CreateAllPerfModelsTest")
        tempAC.Cruise.GetAdvCruiseByName("CreateAllPerfModelsTest")
        tempAC.Descent.GetAdvDescentByName("CreateAllPerfModelsTest")
        tempAC.Takeoff.GetAdvTakeoffByName("CreateAllPerfModelsTest")
        tempAC.Landing.GetAdvLandingByName("CreateAllPerfModelsTest")

        def action299():
            advFWT.CreateAllPerfModels("CreateAllPerfModelsTest", False, False)

        TryCatchAssertBlock.ExpectedException("already exist", action299)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingExternalAero
    @category("Aircraft Tests")
    def test_AdvFixedWingExternalAero(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero

        def action300():
            aeroTest = advFWT.AeroModeAsExternal

        TryCatchAssertBlock.ExpectedException("must be", action300)

        advFWT.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eExternalAeroFile
        aero = advFWT.AeroModeAsExternal

        nonexistingfilepath = TestBase.GetScenarioFile("DoesNotExist.aero")

        def action301():
            aero.SetFilepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action301)

        filepath = TestBase.GetScenarioFile("advAero.aero")
        returnMsg = aero.SetFilepath(filepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertTrue(aero.IsValid)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingSubSuperHypersonicAero
    @category("Aircraft Tests")
    def test_AdvFixedWingSubSuperHypersonicAero(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero

        def action302():
            aeroTest = advFWT.AeroModeAsSubSuperHypersonic

        TryCatchAssertBlock.ExpectedException("must be", action302)

        advFWT.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eSubSuperHyperAero
        Assert.assertEqual(AgEAvtrAdvFixedWingAeroStrategy.eSubSuperHyperAero, advFWT.AeroStrategy)
        aero = advFWT.AeroModeAsSubSuperHypersonic

        aero.TransonicMinMach = 0.81
        Assert.assertEqual(0.81, aero.TransonicMinMach)
        aero.TransonicMaxMach = 1.15
        Assert.assertEqual(1.15, aero.TransonicMaxMach)
        aero.SuperHyperMachTransition = 4.3
        Assert.assertEqual(4.3, aero.SuperHyperMachTransition)
        aero.MaxAOA = 21
        Assert.assertEqual(21, aero.MaxAOA)
        aero.LeadingEdgeFrontalAreaRatio = 0.02
        Assert.assertEqual(0.02, aero.LeadingEdgeFrontalAreaRatio)
        aero.SubsonicAspectRatio = 4.1
        Assert.assertEqual(4.1, aero.SubsonicAspectRatio)
        aero.TransonicMachDragFactor = 3.1
        Assert.assertEqual(3.1, aero.TransonicMachDragFactor)
        aero.WaveDragFactor = 0.9
        Assert.assertEqual(0.9, aero.WaveDragFactor)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingSubsonicAero
    @category("Aircraft Tests")
    def test_AdvFixedWingSubsonicAero(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eSupersonicAero

        def action303():
            aeroTest = advFWT.AeroModeAsSubsonic

        TryCatchAssertBlock.ExpectedException("must be", action303)

        advFWT.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero
        Assert.assertEqual(AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero, advFWT.AeroStrategy)
        aero = advFWT.AeroModeAsSubsonic

        aero.GeometryType = AgEAvtrAdvFixedWingGeometry.eVariableGeometry

        def action304():
            basicGeoTest = aero.GeometryModeAsBasic

        TryCatchAssertBlock.ExpectedException("must be", action304)
        aero.GeometryType = AgEAvtrAdvFixedWingGeometry.eBasicGeometry
        basicGeo = aero.GeometryModeAsBasic

        basicGeo.SetAspectRatio(11)
        Assert.assertEqual(11, basicGeo.AspectRatio)
        basicGeo.WingSweep = 22
        sweep = basicGeo.WingSweep
        Assert.assertEqual(22, float(sweep))

        def action305():
            variableGeoTest = aero.GeometryModeAsVariable

        TryCatchAssertBlock.ExpectedException("must be", action305)
        aero.GeometryType = AgEAvtrAdvFixedWingGeometry.eVariableGeometry
        variableGeo = aero.GeometryModeAsVariable

        variableGeo.SetAspectRatio(12)
        Assert.assertEqual(12, variableGeo.AspectRatio)
        variableGeo.StartSweepMach = 0.65
        Assert.assertEqual(0.65, variableGeo.StartSweepMach)
        variableGeo.StopSweepMach = 0.85
        Assert.assertEqual(0.85, variableGeo.StopSweepMach)
        variableGeo.MinSweepAngle = 26
        sweep1 = variableGeo.MinSweepAngle
        Assert.assertEqual(26, float(sweep1))
        variableGeo.MaxSweepAngle = 52
        sweep2 = variableGeo.MaxSweepAngle
        Assert.assertEqual(52, float(sweep2))

        aero.MaxAOA = 21
        Assert.assertEqual(21, aero.MaxAOA)
        aero.Cd0 = 0.03
        Assert.assertEqual(0.03, aero.Cd0)
        aero.MachDivergence = 0.85
        Assert.assertEqual(0.85, aero.MachDivergence)
        aero.TransonicMachDragFactor = 3.1
        Assert.assertEqual(3.1, aero.TransonicMachDragFactor)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingSupersonicAero
    @category("Aircraft Tests")
    def test_AdvFixedWingSupersonicAero(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eSubsonicAero

        def action306():
            aeroTest = advFWT.AeroModeAsSupersonic

        TryCatchAssertBlock.ExpectedException("must be", action306)

        advFWT.AeroStrategy = AgEAvtrAdvFixedWingAeroStrategy.eSupersonicAero
        Assert.assertEqual(AgEAvtrAdvFixedWingAeroStrategy.eSupersonicAero, advFWT.AeroStrategy)
        aero = advFWT.AeroModeAsSupersonic

        aero.GeometryType = AgEAvtrAdvFixedWingGeometry.eVariableGeometry

        def action307():
            basicGeoTest = aero.GeometryModeAsBasic

        TryCatchAssertBlock.ExpectedException("must be", action307)
        aero.GeometryType = AgEAvtrAdvFixedWingGeometry.eBasicGeometry
        basicGeo = aero.GeometryModeAsBasic

        basicGeo.SetAspectRatio(11)
        Assert.assertEqual(11, basicGeo.AspectRatio)
        basicGeo.WingSweep = 22
        sweep = basicGeo.WingSweep
        Assert.assertEqual(22, float(sweep))

        def action308():
            variableGeoTest = aero.GeometryModeAsVariable

        TryCatchAssertBlock.ExpectedException("must be", action308)
        aero.GeometryType = AgEAvtrAdvFixedWingGeometry.eVariableGeometry
        variableGeo = aero.GeometryModeAsVariable

        variableGeo.SetAspectRatio(12)
        Assert.assertEqual(12, variableGeo.AspectRatio)
        variableGeo.StartSweepMach = 0.65
        Assert.assertEqual(0.65, variableGeo.StartSweepMach)
        variableGeo.StopSweepMach = 0.85
        Assert.assertEqual(0.85, variableGeo.StopSweepMach)
        variableGeo.MinSweepAngle = 26
        sweep1 = variableGeo.MinSweepAngle
        Assert.assertEqual(26, float(sweep1))
        variableGeo.MaxSweepAngle = 52
        sweep2 = variableGeo.MaxSweepAngle
        Assert.assertEqual(52, float(sweep2))

        aero.MaxAOA = 21
        Assert.assertEqual(21, aero.MaxAOA)
        aero.SubsonicCd0 = 0.03
        Assert.assertEqual(0.03, aero.SubsonicCd0)
        aero.TransonicMinMach = 0.85
        Assert.assertEqual(0.85, aero.TransonicMinMach)
        aero.SupersonicMaxMach = 1.5
        Assert.assertEqual(1.5, aero.SupersonicMaxMach)
        aero.TransonicMaxMach = 1.2
        Assert.assertEqual(1.2, aero.TransonicMaxMach)
        aero.TransonicMachDragFactor = 2.5
        Assert.assertEqual(2.5, aero.TransonicMachDragFactor)
        aero.SupersonicMachDragFactor = 3.5
        Assert.assertEqual(3.5, aero.SupersonicMachDragFactor)
        aero.LeadingEdgeSuctionEfficiency = 75
        Assert.assertEqual(75, aero.LeadingEdgeSuctionEfficiency)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingElectricPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingElectricPowerplant(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action309():
            propTest = advFWT.PowerplantModeAsElectric

        TryCatchAssertBlock.ExpectedException("must be", action309)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eElectricPowerplant
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eElectricPowerplant, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsElectric

        prop.MaxPower = 111
        Assert.assertEqual(111, prop.MaxPower)
        prop.PropellerCount = 2
        Assert.assertEqual(2, prop.PropellerCount)
        prop.PropellerDiameter = 2.1
        Assert.assertEqual(2.1, prop.PropellerDiameter)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingExternalProp
    @category("Aircraft Tests")
    def test_AdvFixedWingExternalProp(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eElectricPowerplant

        def action310():
            propTest = advFWT.PowerplantModeAsExternal

        TryCatchAssertBlock.ExpectedException("must be", action310)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsExternal

        nonexistingfilepath = TestBase.GetScenarioFile("DoesNotExist.prop")

        def action311():
            prop.SetFilepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action311)

        filepath = TestBase.GetScenarioFile("advProp.prop")
        returnMsg = prop.SetFilepath(filepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertTrue(prop.IsValid)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingPistonPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingPistonPowerplant(self):
        tolerance = 0.001

        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action312():
            propTest = advFWT.PowerplantModeAsPiston

        TryCatchAssertBlock.ExpectedException("must be", action312)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.ePistonPowerplant
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.ePistonPowerplant, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsPiston

        prop.MaxSeaLevelStaticPower = 111
        Assert.assertEqual(111, prop.MaxSeaLevelStaticPower)
        prop.CriticalAltitude = 50000
        Assert.assertEqual(50000, prop.CriticalAltitude)
        prop.PropellerCount = 2
        Assert.assertEqual(2, prop.PropellerCount)
        prop.PropellerDiameter = 2.1
        Assert.assertEqual(2.1, prop.PropellerDiameter)

        prop.MaxSeaLevelStaticPower = 100
        Assert.assertAlmostEqual(55, prop.FuelFlow, delta=tolerance)
        prop.FuelFlow = 70
        Assert.assertAlmostEqual(70, prop.FuelFlow, delta=tolerance)

        TestBase.Application.UnitPreferences.ResetUnits()
        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingTurbopropPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbopropPowerplant(self):
        tolerance = 0.001

        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action313():
            propTest = advFWT.PowerplantModeAsTurboprop

        TryCatchAssertBlock.ExpectedException("must be", action313)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurboprop
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurboprop, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsTurboprop

        prop.MaxSeaLevelStaticPower = 111
        Assert.assertEqual(111, prop.MaxSeaLevelStaticPower)
        prop.PropellerCount = 2
        Assert.assertEqual(2, prop.PropellerCount)
        prop.PropellerDiameter = 2.1
        Assert.assertEqual(2.1, prop.PropellerDiameter)

        prop.FuelFlow = 70
        Assert.assertAlmostEqual(70, prop.FuelFlow, delta=tolerance)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingTurbofanHighBypassPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanHighBypassPowerplant(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action314():
            propTest = advFWT.PowerplantModeAsEmpiricalJetEngine

        TryCatchAssertBlock.ExpectedException("must be", action314)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanHighBypass
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanHighBypass, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsEmpiricalJetEngine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingTurbofanLowBypassPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanLowBypassPowerplant(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action315():
            propTest = advFWT.PowerplantModeAsEmpiricalJetEngine

        TryCatchAssertBlock.ExpectedException("must be", action315)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanLowBypass
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanLowBypass, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsEmpiricalJetEngine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingTurbofanLowBypassAfterburningPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanLowBypassAfterburningPowerplant(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action316():
            propTest = advFWT.PowerplantModeAsEmpiricalJetEngine

        TryCatchAssertBlock.ExpectedException("must be", action316)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanLowBypassAfterburning
        Assert.assertEqual(
            AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanLowBypassAfterburning, advFWT.PowerplantStrategy
        )
        prop = advFWT.PowerplantModeAsEmpiricalJetEngine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingTurbofanTurbojetPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanTurbojetPowerplant(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action317():
            propTest = advFWT.PowerplantModeAsEmpiricalJetEngine

        TryCatchAssertBlock.ExpectedException("must be", action317)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojet
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojet, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsEmpiricalJetEngine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingTurbofanTurbojetAfterburningPowerplant
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanTurbojetAfterburningPowerplant(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action318():
            propTest = advFWT.PowerplantModeAsEmpiricalJetEngine

        TryCatchAssertBlock.ExpectedException("must be", action318)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojetAfterburning
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojetAfterburning, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsEmpiricalJetEngine

        self.EmpiricalJetEngineOptions(prop)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingTurbojetBasicABProp
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbojetBasicABProp(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action319():
            propTest = advFWT.PowerplantModeAsBasicTurbojet

        TryCatchAssertBlock.ExpectedException("must be", action319)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojetBasicAB
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbojetBasicAB, advFWT.PowerplantStrategy)
        self.TestTurbojetBasicAB(advFWT.PowerplantModeAsBasicTurbojet)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingTurbofanBasicABProp
    @category("Aircraft Tests")
    def test_AdvFixedWingTurbofanBasicABProp(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action320():
            propTest = advFWT.PowerplantModeAsBasicTurbofan

        TryCatchAssertBlock.ExpectedException("must be", action320)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanBasicAB
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eTurbofanBasicAB, advFWT.PowerplantStrategy)
        self.TestTurbofanBasicAB(advFWT.PowerplantModeAsBasicTurbofan)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvFixedWingSubSuperHypersonicProp
    @category("Aircraft Tests")
    def test_AdvFixedWingSubSuperHypersonicProp(self):
        tempAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        advFWT = tempAC.AdvFixedWingTool

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eExternalPropFile

        def action321():
            propTest = advFWT.PowerplantModeAsSubSuperHypersonic

        TryCatchAssertBlock.ExpectedException("must be", action321)

        advFWT.PowerplantStrategy = AgEAvtrAdvFixedWingPowerplantStrategy.eSubSuperHyperPowerplant
        Assert.assertEqual(AgEAvtrAdvFixedWingPowerplantStrategy.eSubSuperHyperPowerplant, advFWT.PowerplantStrategy)
        prop = advFWT.PowerplantModeAsSubSuperHypersonic

        prop.MaxTurbineCompressionTemp = 901
        Assert.assertEqual(901, prop.MaxTurbineCompressionTemp)
        prop.MaxTurbineBurnerTemp = 1701
        Assert.assertEqual(1701, prop.MaxTurbineBurnerTemp)
        prop.CanRamCompressorPressureRatio = 2.1
        Assert.assertEqual(2.1, prop.CanRamCompressorPressureRatio)
        prop.MustRamCompressorPressureRatio = 1.1
        Assert.assertEqual(1.1, prop.MustRamCompressorPressureRatio)
        prop.MaxRamScramCompressionTemperature = 1561
        Assert.assertEqual(1561, prop.MaxRamScramCompressionTemperature)
        prop.MaxRamScramBurnerTotalTemperature = 2001
        Assert.assertEqual(2001, prop.MaxRamScramBurnerTotalTemperature)

        prop.TurbineMode = AgEAvtrTurbineMode.eTurbineModeDisabled
        Assert.assertEqual(AgEAvtrTurbineMode.eTurbineModeDisabled, prop.TurbineMode)

        def action322():
            fanTest = prop.TurbineModeAsTurbofan

        TryCatchAssertBlock.ExpectedException("must be", action322)
        prop.RamjetMode = AgEAvtrRamjetMode.eRamjetModeDisabled
        Assert.assertEqual(AgEAvtrRamjetMode.eRamjetModeDisabled, prop.RamjetMode)

        def action323():
            ramTest = prop.RamjetModeAsBasic

        TryCatchAssertBlock.ExpectedException("must be", action323)
        prop.ScramjetMode = AgEAvtrScramjetMode.eScramjetModeDisabled
        Assert.assertEqual(AgEAvtrScramjetMode.eScramjetModeDisabled, prop.ScramjetMode)

        def action324():
            scramTest = prop.ScramjetModeAsBasic

        TryCatchAssertBlock.ExpectedException("must be", action324)

        # /////////////////// Now test the turbojet turbine ////////////
        prop.TurbineMode = AgEAvtrTurbineMode.eTurbineModeTurbojetBasicAB
        turbojet = prop.TurbineModeAsTurbojet
        self.TestTurbojetBasicAB(turbojet)
        prop.MaxTurbineCompressionTemp = 901
        Assert.assertEqual(901, turbojet.MaxCompressionTemp)
        prop.MaxTurbineBurnerTemp = 1701
        Assert.assertEqual(1701, turbojet.MaxBurnerTemp)

        # /////////////////// Now test the turbofan turbine ////////////
        prop.TurbineMode = AgEAvtrTurbineMode.eTurbineModeTurbofanBasicAB
        turbofan = prop.TurbineModeAsTurbofan
        self.TestTurbofanBasicAB(turbofan)
        prop.MaxTurbineCompressionTemp = 901
        Assert.assertEqual(901, turbofan.MaxCompressionTemp)
        prop.MaxTurbineBurnerTemp = 1701
        Assert.assertEqual(1701, turbofan.MaxBurnerTemp)

        # /////////////////// Now test the ramjet /////////////////////
        prop.RamjetMode = AgEAvtrRamjetMode.eRamjetModeBasic
        ramjet = prop.RamjetModeAsBasic

        ramjet.DesignAltitude = 60001
        Assert.assertEqual(60001, ramjet.DesignAltitude)
        ramjet.DesignMach = 3.1
        Assert.assertEqual(3.1, ramjet.DesignMach)
        ramjet.DesignThrust = 100001
        Assert.assertEqual(100001, ramjet.DesignThrust)

        prop.MaxRamScramCompressionTemperature = 1561
        Assert.assertEqual(1561, ramjet.MaxCompressionTemp)
        ramjet.MaxCompressionTemp = 1562
        Assert.assertEqual(1562, ramjet.MaxCompressionTemp)
        prop.MaxRamScramBurnerTotalTemperature = 2001
        Assert.assertEqual(2001, ramjet.MaxBurnerTemp)
        ramjet.MaxBurnerTemp = 2002
        Assert.assertEqual(2002, ramjet.MaxBurnerTemp)

        ramjet.FuelType = AgEAvtrJetFuelType.eKeroseneAFPROP
        self.TestFuelAFPROP(ramjet.FuelModeAsAFPROP)
        ramjet.FuelType = AgEAvtrJetFuelType.eKeroseneCEA
        self.TestFuelCEA(ramjet.FuelModeAsCEA)

        ramjet.FuelType = AgEAvtrJetFuelType.eHydrogen
        Assert.assertEqual(AgEAvtrJetFuelType.eHydrogen, ramjet.FuelType)

        def action325():
            afprop = ramjet.FuelModeAsAFPROP

        TryCatchAssertBlock.ExpectedException("must be", action325)

        def action326():
            cea = ramjet.FuelModeAsCEA

        TryCatchAssertBlock.ExpectedException("must be", action326)

        self.TestPropulsionEfficienciesRamScram(ramjet.EfficienciesAndLosses)

        # /////////////////// Now test the scramjet /////////////////////
        prop.ScramjetMode = AgEAvtrScramjetMode.eScramjetModeBasic
        scramjet = prop.ScramjetModeAsBasic

        scramjet.DesignAltitude = 90001
        Assert.assertEqual(90001, scramjet.DesignAltitude)
        scramjet.DesignMach = 6.1
        Assert.assertEqual(6.1, scramjet.DesignMach)
        scramjet.DesignThrust = 100001
        Assert.assertEqual(100001, scramjet.DesignThrust)

        prop.MaxRamScramCompressionTemperature = 1561
        Assert.assertEqual(1561, scramjet.MaxCompressionTemp)
        scramjet.MaxCompressionTemp = 1562
        Assert.assertEqual(1562, scramjet.MaxCompressionTemp)
        prop.MaxRamScramBurnerTotalTemperature = 2001
        Assert.assertEqual(2001, scramjet.MaxBurnerTemp)
        scramjet.MaxBurnerTemp = 2002
        Assert.assertEqual(2002, scramjet.MaxBurnerTemp)

        scramjet.FuelType = AgEAvtrJetFuelType.eKeroseneAFPROP
        self.TestFuelAFPROP(scramjet.FuelModeAsAFPROP)
        scramjet.FuelType = AgEAvtrJetFuelType.eKeroseneCEA
        self.TestFuelCEA(scramjet.FuelModeAsCEA)

        scramjet.FuelType = AgEAvtrJetFuelType.eHydrogen
        Assert.assertEqual(AgEAvtrJetFuelType.eHydrogen, scramjet.FuelType)

        def action327():
            afprop = scramjet.FuelModeAsAFPROP

        TryCatchAssertBlock.ExpectedException("must be", action327)

        def action328():
            cea = scramjet.FuelModeAsCEA

        TryCatchAssertBlock.ExpectedException("must be", action328)

        self.TestPropulsionEfficienciesRamScram(scramjet.EfficienciesAndLosses)

        tempAC.GetAsCatalogItem().Remove()

    # endregion

    # region PerformanceModelCategory
    @category("Aircraft Tests")
    def test_PerformanceModelCategory(self):
        acc = EarlyBoundTests.AG_AvtrAircraft.Acceleration
        accAsCI = acc.GetAsCatalogItem()

        Assert.assertEqual("Acceleration", accAsCI.Name)

        def action329():
            accAsCI.Name = ""

        TryCatchAssertBlock.ExpectedException("read-only", action329)
        Assert.assertEqual("Acceleration", accAsCI.Name)

        isReadOnly = accAsCI.IsReadOnly
        Assert.assertTrue(isReadOnly)

        def action330():
            accAsCI.Remove()

        TryCatchAssertBlock.ExpectedException("read-only", action330)

        def action331():
            accAsCI.Duplicate()

        TryCatchAssertBlock.ExpectedException("", action331)

    # endregion

    # region BuiltInPerformanceModel
    @category("Aircraft Tests")
    def test_BuiltInPerformanceModel(self):
        acc = EarlyBoundTests.AG_AvtrAircraft.Acceleration
        builtInAcc = acc.GetBuiltInModel()
        accAsCatalogItem: ICatalogItem = clr.CastAs(builtInAcc, ICatalogItem)

        Assert.assertEqual("Built-In Model", accAsCatalogItem.Name)

        def action332():
            accAsCatalogItem.Name = ""

        TryCatchAssertBlock.DoAssert2(action332)

        Assert.assertEqual("Built-In Model", accAsCatalogItem.Name)

        isReadOnly = accAsCatalogItem.IsReadOnly
        Assert.assertFalse(isReadOnly)

        def action333():
            accAsCatalogItem.Remove()

        TryCatchAssertBlock.DoAssert2(action333)

    # endregion

    # region BasicAccelerationModel
    @category("Aircraft Tests")
    def test_BasicAccelerationModel(self):
        acc = EarlyBoundTests.AG_AvtrAircraft.Acceleration
        basicAcc = acc.GetBuiltInModel()

        levelTurns = basicAcc.LevelTurns
        levelTurns.ManeuverMode = AgEAvtrAccelManeuverMode.eAccelManeuverModeNormal

        def action334():
            testVal = levelTurns.ManeuverModeHelper

        TryCatchAssertBlock.ExpectedException("must be set", action334)
        levelTurns.ManeuverMode = AgEAvtrAccelManeuverMode.eAccelManeuverModeDensityScale

        def action335():
            testVal = levelTurns.ManeuverModeHelper

        TryCatchAssertBlock.ExpectedException("must be set", action335)

        climbDescent = basicAcc.ClimbAndDescentTransitions
        climbDescent.ManeuverMode = AgEAvtrAccelManeuverMode.eAccelManeuverModeNormal

        def action336():
            testVal = climbDescent.ManeuverModeHelper

        TryCatchAssertBlock.ExpectedException("must be set", action336)
        climbDescent.ManeuverMode = AgEAvtrAccelManeuverMode.eAccelManeuverModeDensityScale

        def action337():
            testVal = climbDescent.ManeuverModeHelper

        TryCatchAssertBlock.ExpectedException("must be set", action337)

    # endregion

    # region BasicAccelerationAero
    @category("Aircraft Tests")
    def test_BasicAccelerationAero(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        aero = basicAcc.Aerodynamics
        aero.AeroStrategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroSimple
        Assert.assertEqual(AgEAvtrAircraftAeroStrategy.eAircraftAeroSimple, aero.AeroStrategy)

        aero.LiftFactor = 1.2
        Assert.assertEqual(1.2, aero.LiftFactor)
        aero.DragFactor = 1.3
        Assert.assertEqual(1.3, aero.DragFactor)
        Assert.assertEqual(1.2, aero.LiftFactor)

        aero.AeroStrategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroAdvancedMissile

        def action338():
            aero.LiftFactor = 1.2

        TryCatchAssertBlock.ExpectedException("", action338)

        def action339():
            aero.DragFactor = 1.3

        TryCatchAssertBlock.ExpectedException("", action339)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationSimpleAero
    @category("Aircraft Tests")
    def test_BasicAccelerationSimpleAero(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        aero = basicAcc.Aerodynamics
        aero.AeroStrategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroSimple

        simpleAero = aero.ModeAsSimple
        simpleAero.OperatingMode = AgEAvtrAeroPropSimpleMode.eHelicopter
        Assert.assertEqual(AgEAvtrAeroPropSimpleMode.eHelicopter, simpleAero.OperatingMode)

        simpleAero.SRef = 5
        Assert.assertEqual(5, simpleAero.SRef)
        simpleAero.ClMax = 3.1
        Assert.assertEqual(3.1, simpleAero.ClMax)
        simpleAero.Cd = 0.05
        Assert.assertEqual(0.05, simpleAero.Cd)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationBasicFixedWingAero
    @category("Aircraft Tests")
    def test_BasicAccelerationBasicFixedWingAero(self):
        tolerance = 1e-06

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        aero = basicAcc.Aerodynamics
        aero.AeroStrategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroBasicFixedWing

        bfwAero = aero.ModeAsBasicFixedWing

        bfwAero.ForwardFlightReferenceArea = 0.05
        Assert.assertEqual(0.05, bfwAero.ForwardFlightReferenceArea)
        bfwAero.ForwardFlightUseCompressibleFlow = False
        Assert.assertEqual(False, bfwAero.ForwardFlightUseCompressibleFlow)
        bfwAero.ForwardFlightCl0 = 0.01
        Assert.assertEqual(0.01, bfwAero.ForwardFlightCl0)
        bfwAero.ForwardFlightClAlpha = 0.07
        Assert.assertAlmostEqual(0.07, bfwAero.ForwardFlightClAlpha, delta=tolerance)
        bfwAero.ForwardFlightMinAOA = -89
        minAoA = bfwAero.ForwardFlightMinAOA
        Assert.assertAlmostEqual(-89, float(minAoA), delta=tolerance)
        bfwAero.ForwardFlightMaxAOA = 89
        maxAoA = bfwAero.ForwardFlightMaxAOA
        Assert.assertAlmostEqual(89, float(maxAoA), delta=tolerance)
        bfwAero.ForwardFlightCd0 = 0.021
        Assert.assertEqual(0.021, bfwAero.ForwardFlightCd0)
        bfwAero.ForwardFlightK = 0.01
        Assert.assertEqual(0.01, bfwAero.ForwardFlightK)

        bfwAero.TakeoffLandingReferenceArea = 0.06
        Assert.assertEqual(0.06, bfwAero.TakeoffLandingReferenceArea)
        bfwAero.TakeoffLandingUseCompressibleFlow = False
        Assert.assertEqual(False, bfwAero.TakeoffLandingUseCompressibleFlow)
        bfwAero.TakeoffLandingCl0 = 0.02
        Assert.assertEqual(0.02, bfwAero.TakeoffLandingCl0)
        bfwAero.TakeoffLandingClAlpha = 0.08
        Assert.assertAlmostEqual(0.08, bfwAero.TakeoffLandingClAlpha, delta=tolerance)
        bfwAero.TakeoffLandingMinAOA = -88
        minAoA = bfwAero.TakeoffLandingMinAOA
        Assert.assertAlmostEqual(-88, float(minAoA), delta=tolerance)
        bfwAero.TakeoffLandingMaxAOA = 88
        maxAoA = bfwAero.TakeoffLandingMaxAOA
        Assert.assertAlmostEqual(88, float(maxAoA), delta=tolerance)
        bfwAero.TakeoffLandingCd0 = 0.022
        Assert.assertEqual(0.022, bfwAero.TakeoffLandingCd0)
        bfwAero.TakeoffLandingK = 0.02
        Assert.assertEqual(0.02, bfwAero.TakeoffLandingK)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationExternalAero
    @category("Aircraft Tests")
    def test_BasicAccelerationExternalAero(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        aero = basicAcc.Aerodynamics
        aero.AeroStrategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroExternalFile

        externalAero = aero.ModeAsExternal
        Assert.assertIs(None, externalAero.ForwardFlightFilepath)
        Assert.assertIs(None, externalAero.TakeoffLandingFilepath)

        def action340():
            externalAero.SetForwardFlightFilepath("")

        TryCatchAssertBlock.ExpectedException("", action340)

        def action341():
            externalAero.SetTakeoffLandingFilepath("")

        TryCatchAssertBlock.ExpectedException("", action341)

        def action342():
            externalAero.ReloadForwardFlightFile()

        TryCatchAssertBlock.ExpectedException("", action342)

        def action343():
            externalAero.ReloadTakeoffLandingFile()

        TryCatchAssertBlock.ExpectedException("", action343)
        Assert.assertEqual(False, externalAero.IsForwardFlightValid)
        Assert.assertEqual(False, externalAero.IsTakeoffLandingValid)

        Assert.assertTrue(externalAero.CanSetForwardFlightRefArea)
        externalAero.ForwardFlightRefArea = 0.05
        Assert.assertEqual(0.05, externalAero.ForwardFlightRefArea)
        Assert.assertTrue(externalAero.CanSetTakeoffLandingRefArea)
        externalAero.TakeoffLandingRefArea = 0.07
        Assert.assertEqual(0.07, externalAero.TakeoffLandingRefArea)

        nonexistingfilepath = TestBase.GetScenarioFile("DoesNotExist.aero")

        def action344():
            externalAero.SetForwardFlightFilepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action344)

        aeroFilepath = TestBase.GetScenarioFile("simpleAero.aero")
        returnMsg = externalAero.SetForwardFlightFilepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalAero.CanSetForwardFlightRefArea)

        def action345():
            externalAero.ForwardFlightRefArea = 0.05

        TryCatchAssertBlock.ExpectedException("", action345)
        Assert.assertTrue(externalAero.IsForwardFlightValid)

        returnMsg2 = externalAero.SetTakeoffLandingFilepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg2))
        Assert.assertEqual(False, externalAero.CanSetTakeoffLandingRefArea)

        def action346():
            externalAero.TakeoffLandingRefArea = 0.07

        TryCatchAssertBlock.ExpectedException("", action346)
        Assert.assertTrue(externalAero.IsTakeoffLandingValid)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationAdvancedMissileAero
    @category("Aircraft Tests")
    def test_BasicAccelerationAdvancedMissileAero(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        aero = basicAcc.Aerodynamics
        aero.AeroStrategy = AgEAvtrAircraftAeroStrategy.eAircraftAeroAdvancedMissile
        self.AdvancedMissileAero(aero.ModeAsAdvancedMissile)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationProp
    @category("Aircraft Tests")
    def test_BasicAccelerationProp(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        prop = basicAcc.Propulsion
        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropSimple
        Assert.assertEqual(AgEAvtrAircraftPropStrategy.eAircraftPropSimple, prop.PropStrategy)

        def action347():
            prop.LiftFactor = 1.2

        TryCatchAssertBlock.ExpectedException("", action347)

        def action348():
            prop.DragFactor = 1.3

        TryCatchAssertBlock.ExpectedException("", action348)

        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropBasicFixedWing
        Assert.assertEqual(AgEAvtrAircraftPropStrategy.eAircraftPropBasicFixedWing, prop.PropStrategy)

        prop.LiftFactor = 1.2
        Assert.assertEqual(1.2, prop.LiftFactor)
        prop.DragFactor = 1.3
        Assert.assertEqual(1.3, prop.DragFactor)
        Assert.assertEqual(1.2, prop.LiftFactor)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationSimpleProp
    @category("Aircraft Tests")
    def test_BasicAccelerationSimpleProp(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        prop = basicAcc.Propulsion
        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropSimple
        simpleProp = prop.ModeAsSimple

        simpleProp.MaxThrustAccel = 0.6
        Assert.assertEqual(0.6, simpleProp.MaxThrustAccel)
        simpleProp.MinThrustDecel = 0.4
        Assert.assertEqual(0.4, simpleProp.MinThrustDecel)

        Assert.assertEqual(False, simpleProp.UseDensityScaling)
        simpleProp.SetDensityScaling(True, 0.02)
        Assert.assertTrue(simpleProp.UseDensityScaling)
        Assert.assertEqual(0.02, simpleProp.DensityRatioExponent)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationExternalProp
    @category("Aircraft Tests")
    def test_BasicAccelerationExternalProp(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        prop = basicAcc.Propulsion
        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropExternalFile

        externalProp = prop.ModeAsExternal
        Assert.assertIs(None, externalProp.PropFilepath)

        def action349():
            externalProp.SetPropFilepath("")

        TryCatchAssertBlock.ExpectedException("", action349)

        def action350():
            externalProp.ReloadPropFile()

        TryCatchAssertBlock.ExpectedException("", action350)
        Assert.assertEqual(False, externalProp.IsValid)

        Assert.assertTrue(externalProp.CanSetAccelDecel)
        externalProp.MaxThrustAccel = 0.6
        Assert.assertEqual(0.6, externalProp.MaxThrustAccel)
        externalProp.MinThrustDecel = 0.4
        Assert.assertEqual(0.4, externalProp.MinThrustDecel)

        nonexistingfilepath = TestBase.GetScenarioFile("DoesNotExist.prop")

        def action351():
            externalProp.SetPropFilepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action351)

        propFilepath = TestBase.GetScenarioFile("simpleProp.prop")
        returnMsg = externalProp.SetPropFilepath(propFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalProp.CanSetAccelDecel)

        def action352():
            externalProp.MaxThrustAccel = 0.6

        TryCatchAssertBlock.ExpectedException("", action352)
        Assert.assertTrue(externalProp.IsValid)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationBasicFixedWingProp
    @category("Aircraft Tests")
    def test_BasicAccelerationBasicFixedWingProp(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        prop = basicAcc.Propulsion
        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropBasicFixedWing

        bfwProp = prop.ModeAsBasicFixedWing
        bfwProp.PropulsionMode = AgEAvtrBasicFixedWingPropMode.eSpecifyThrust
        Assert.assertEqual(AgEAvtrBasicFixedWingPropMode.eSpecifyThrust, bfwProp.PropulsionMode)

        def action353():
            bfwProp.PropellerCount = 1

        TryCatchAssertBlock.ExpectedException("", action353)

        def action354():
            bfwProp.PropellerDiameter = 1

        TryCatchAssertBlock.ExpectedException("", action354)

        def action355():
            bfwProp.PropellerRPM = 1

        TryCatchAssertBlock.ExpectedException("", action355)

        bfwProp.MinPowerThrust = 1
        Assert.assertEqual(1, bfwProp.MinPowerThrust)
        bfwProp.MaxPowerThrust = 100000
        Assert.assertEqual(100000, bfwProp.MaxPowerThrust)

        bfwProp.PropulsionMode = AgEAvtrBasicFixedWingPropMode.eSpecifyPower
        bfwProp.PropellerCount = 2
        Assert.assertEqual(2, bfwProp.PropellerCount)
        bfwProp.PropellerDiameter = 4
        Assert.assertEqual(4, bfwProp.PropellerDiameter)
        bfwProp.PropellerRPM = 3000
        Assert.assertEqual(3000, bfwProp.PropellerRPM)

        bfwProp.MinPowerThrust = 2
        Assert.assertEqual(2, bfwProp.MinPowerThrust)
        bfwProp.MaxPowerThrust = 99000
        Assert.assertEqual(99000, bfwProp.MaxPowerThrust)
        bfwProp.MinFuelFlow = 123
        Assert.assertAlmostEqual(123, bfwProp.MinFuelFlow, delta=tolerance)
        bfwProp.MaxFuelFlow = 12345
        Assert.assertAlmostEqual(12345, bfwProp.MaxFuelFlow, delta=tolerance)

        bfwProp.MaxThrustAccel = 0.6
        Assert.assertEqual(0.6, bfwProp.MaxThrustAccel)
        bfwProp.MinThrustDecel = 0.4
        Assert.assertEqual(0.4, bfwProp.MinThrustDecel)

        Assert.assertEqual(False, bfwProp.UseDensityScaling)
        bfwProp.SetDensityScaling(True, 0.02)
        Assert.assertTrue(bfwProp.UseDensityScaling)
        Assert.assertEqual(0.02, bfwProp.DensityRatioExponent)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationRocketProp
    @category("Aircraft Tests")
    def test_BasicAccelerationRocketProp(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        prop = basicAcc.Propulsion
        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropMissileRocket
        rocketProp = prop.ModeAsRocket

        rocketProp.NozzleExpansionRatio = 7.1
        Assert.assertEqual(7.1, rocketProp.NozzleExpansionRatio)
        rocketProp.NozzleExitDiameter = 0.123
        Assert.assertEqual(0.123, rocketProp.NozzleExitDiameter)
        rocketProp.PropellantSpecificHeatRatio = 1.2
        Assert.assertEqual(1.2, rocketProp.PropellantSpecificHeatRatio)
        rocketProp.PropellantCharacteristicVelocity = 3120
        Assert.assertAlmostEqual(3120, rocketProp.PropellantCharacteristicVelocity, delta=tolerance)
        rocketProp.CombustionChamberPressure = 13000000.0
        Assert.assertEqual(13000000.0, rocketProp.CombustionChamberPressure)

        rocketProp.UseBoostSustainMode = False

        def action356():
            rocketProp.BoostFuelFraction = 60

        TryCatchAssertBlock.ExpectedException("must be", action356)

        def action357():
            rocketProp.BoostChamberPressure = 21000000.0

        TryCatchAssertBlock.ExpectedException("must be", action357)
        rocketProp.UseBoostSustainMode = True
        Assert.assertTrue(rocketProp.UseBoostSustainMode)
        rocketProp.BoostFuelFraction = 60
        Assert.assertEqual(60, rocketProp.BoostFuelFraction)
        rocketProp.BoostChamberPressure = 21000000.0
        Assert.assertEqual(21000000.0, rocketProp.BoostChamberPressure)

        rocketProp.NoThrustWhenNoFuel = False
        Assert.assertEqual(False, rocketProp.NoThrustWhenNoFuel)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationRamjetProp
    @category("Aircraft Tests")
    def test_BasicAccelerationRamjetProp(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        prop = basicAcc.Propulsion
        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropMissileRamjet
        ramjetProp = prop.ModeAsRamjet

        ramjetProp.DesignAltitude = 5000
        Assert.assertEqual(5000, ramjetProp.DesignAltitude)
        ramjetProp.DesignMach = 3
        Assert.assertEqual(3, ramjetProp.DesignMach)
        ramjetProp.DesignThrust = 30000
        Assert.assertEqual(30000, ramjetProp.DesignThrust)
        ramjetProp.EngineTemp = 2000
        Assert.assertEqual(2000, ramjetProp.EngineTemp)

        ramjetProp.FuelHeatingValue = 41500000
        Assert.assertEqual(41500000, ramjetProp.FuelHeatingValue)
        ramjetProp.InletPressureRatio = 0.9
        Assert.assertEqual(0.9, ramjetProp.InletPressureRatio)
        ramjetProp.BurnerPressureRatio = 0.8
        Assert.assertEqual(0.8, ramjetProp.BurnerPressureRatio)
        ramjetProp.NozzlePressureRatio = 0.7
        Assert.assertEqual(0.7, ramjetProp.NozzlePressureRatio)
        ramjetProp.P0overP9 = 0.5
        Assert.assertEqual(0.5, ramjetProp.P0overP9)
        ramjetProp.BurnerEfficiency = 95
        Assert.assertEqual(95, ramjetProp.BurnerEfficiency)

        ramjetProp.NoThrustWhenNoFuel = False
        Assert.assertEqual(False, ramjetProp.NoThrustWhenNoFuel)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicAccelerationTurbojetProp
    @category("Aircraft Tests")
    def test_BasicAccelerationTurbojetProp(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        acc = newAC.Acceleration
        basicAcc = acc.GetBuiltInModel()

        prop = basicAcc.Propulsion
        prop.PropStrategy = AgEAvtrAircraftPropStrategy.eAircraftPropMissileTurbojet
        turboProp = prop.ModeAsTurbojet

        turboProp.DesignAltitude = 5000
        Assert.assertEqual(5000, turboProp.DesignAltitude)
        turboProp.DesignMach = 3
        Assert.assertEqual(3, turboProp.DesignMach)
        turboProp.DesignThrust = 30000
        Assert.assertEqual(30000, turboProp.DesignThrust)
        turboProp.TurbineTemp = 2000
        Assert.assertEqual(2000, turboProp.TurbineTemp)
        turboProp.CompressorPressureRatio = 9
        Assert.assertEqual(9, turboProp.CompressorPressureRatio)

        turboProp.FuelHeatingValue = 41500000
        Assert.assertEqual(41500000, turboProp.FuelHeatingValue)
        turboProp.InletSubsonicPressureRatio = 0.9
        Assert.assertEqual(0.9, turboProp.InletSubsonicPressureRatio)
        turboProp.BurnerPressureRatio = 0.8
        Assert.assertEqual(0.8, turboProp.BurnerPressureRatio)
        turboProp.NozzlePressureRatio = 0.7
        Assert.assertEqual(0.7, turboProp.NozzlePressureRatio)
        turboProp.P0overP9 = 0.5
        Assert.assertEqual(0.5, turboProp.P0overP9)
        turboProp.CompressorEfficiency = 99
        Assert.assertEqual(99, turboProp.CompressorEfficiency)
        turboProp.TurbineEfficiency = 98
        Assert.assertEqual(98, turboProp.TurbineEfficiency)
        turboProp.BurnerEfficiency = 97
        Assert.assertEqual(97, turboProp.BurnerEfficiency)
        turboProp.MechanicalEfficiency = 96
        Assert.assertEqual(96, turboProp.MechanicalEfficiency)

        turboProp.NoThrustWhenNoFuel = False
        Assert.assertEqual(False, turboProp.NoThrustWhenNoFuel)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvancedAccelerationModel
    @category("Aircraft Tests")
    def test_AdvancedAccelerationModel(self):
        acc = EarlyBoundTests.AG_AvtrAircraft.Acceleration
        accAsCatalogItem = acc.GetAsCatalogItem()
        accModelNames = accAsCatalogItem.ChildNames
        count = Array.Length(accModelNames)
        advAcc: IAircraftAdvAccelerationModel = clr.CastAs(
            accAsCatalogItem.AddChildOfType("Advanced Acceleration Model", "AdvAcceleration Model Name"),
            IAircraftAdvAccelerationModel,
        )

        accModelNames = accAsCatalogItem.ChildNames
        count += 1
        Assert.assertEqual(count, Array.Length(accModelNames))
        Assert.assertEqual("AdvAcceleration Model Name", accModelNames[0])

        accMode = advAcc.AccelerationMode
        accMode.AccelMode = AgEAvtrAccelerationAdvAccelMode.eAccelModeMaxAccel

        def action358():
            accMode.AccelG = 1

        TryCatchAssertBlock.ExpectedException("must be set", action358)

        advAcc.GetAsCatalogItem().Remove()
        accModelNames = accAsCatalogItem.ChildNames
        count -= 1
        Assert.assertEqual(count, Array.Length(accModelNames))

    # endregion

    # region BasicClimbModel
    @category("Aircraft Tests")
    def test_BasicClimbModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        climb = newAC.Climb
        basicClimb = climb.GetBuiltInModel()

        basicClimb.CeilingAltitude = 70001
        Assert.assertEqual(70001, basicClimb.CeilingAltitude)

        basicClimb.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicClimb.AirspeedType)
        Assert.assertAlmostEqual(251, basicClimb.Airspeed, delta=tolerance)
        basicClimb.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicClimb.AirspeedType)
        Assert.assertEqual(0.4, basicClimb.Airspeed)

        basicClimb.AltitudeRate = 4001
        Assert.assertAlmostEqual(4001, basicClimb.AltitudeRate, delta=tolerance)

        basicClimb.UseAeroPropFuel = True
        Assert.assertTrue(basicClimb.UseAeroPropFuel)

        def action359():
            testVal = basicClimb.ScaleFuelFlowByNonStdDensity

        TryCatchAssertBlock.ExpectedException("must be ", action359)

        def action360():
            basicClimb.ScaleFuelFlowByNonStdDensity = True

        TryCatchAssertBlock.ExpectedException("must be ", action360)

        def action361():
            testVal = basicClimb.FuelFlow

        TryCatchAssertBlock.ExpectedException("must be ", action361)

        def action362():
            basicClimb.FuelFlow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action362)

        basicClimb.UseAeroPropFuel = False
        basicClimb.FuelFlow = 9000
        Assert.assertAlmostEqual(9000, basicClimb.FuelFlow, delta=tolerance)

        basicClimb.EnableRelativeAirspeedTolerance = False

        def action363():
            testVal = basicClimb.RelativeAirspeedTolerance

        TryCatchAssertBlock.ExpectedException("must be ", action363)

        def action364():
            basicClimb.RelativeAirspeedTolerance = 1

        TryCatchAssertBlock.ExpectedException("must be ", action364)

        basicClimb.EnableRelativeAirspeedTolerance = True
        basicClimb.RelativeAirspeedTolerance = 0.06
        Assert.assertEqual(0.06, basicClimb.RelativeAirspeedTolerance)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvancedClimbModel
    @category("Aircraft Tests")
    def test_AdvancedClimbModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        climb = newAC.Climb
        climb.GetAsCatalogItem().AddChildOfType("Advanced Climb Model", "Adv Climb")
        advClimb = climb.GetAdvClimbByName("Adv Climb")

        advClimb.ClimbSpeedType = AgEAvtrClimbSpeedType.eClimbSpeedMinFuel
        Assert.assertEqual(AgEAvtrClimbSpeedType.eClimbSpeedMinFuel, advClimb.ClimbSpeedType)

        def action365():
            advClimb.SetClimbOverrideAirspeed(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action365)

        advClimb.ClimbSpeedType = AgEAvtrClimbSpeedType.eClimbSpeedOverride
        advClimb.SetClimbOverrideAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advClimb.ClimbOverrideAirspeedType)
        Assert.assertAlmostEqual(251, advClimb.ClimbOverrideAirspeed, delta=tolerance)

        advClimb.SetClimbOverrideAirspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advClimb.ClimbOverrideAirspeedType)
        Assert.assertEqual(0.4, advClimb.ClimbOverrideAirspeed)

        def action366():
            advClimb.UseAfterburner = True

        TryCatchAssertBlock.ExpectedException("not enabled", action366)
        Assert.assertEqual(False, advClimb.UseAfterburner)

        advClimb.UseAirspeedLimit = False
        Assert.assertEqual(False, advClimb.UseAirspeedLimit)

        def action367():
            advClimb.AltitudeLimit = 9000

        TryCatchAssertBlock.ExpectedException("must be", action367)

        def action368():
            advClimb.SetAirspeedLimit(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action368)

        advClimb.UseAirspeedLimit = True
        advClimb.AltitudeLimit = 9000
        Assert.assertEqual(9000, advClimb.AltitudeLimit)
        advClimb.SetAirspeedLimit(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advClimb.AirspeedLimitType)
        Assert.assertAlmostEqual(251, advClimb.AirspeedLimit, delta=tolerance)
        advClimb.SetAirspeedLimit(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advClimb.AirspeedLimitType)
        Assert.assertEqual(0.4, advClimb.AirspeedLimit)

        advClimb.UseFlightPathAngleLimit = False
        Assert.assertEqual(False, advClimb.UseFlightPathAngleLimit)
        advClimb.SetFlightPathAngle(31)
        Assert.assertTrue(advClimb.UseFlightPathAngleLimit)
        fpa = advClimb.FlightPathAngle
        Assert.assertEqual(31, float(fpa))

        advClimb.ComputeDeltaAltitude = 1001
        Assert.assertEqual(1001, advClimb.ComputeDeltaAltitude)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicCruiseModel
    @category("Aircraft Tests")
    def test_BasicCruiseModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        cruise = newAC.Cruise
        basicCruise = cruise.GetBuiltInModel()

        basicCruise.CeilingAltitude = 20000
        Assert.assertEqual(20000, basicCruise.CeilingAltitude)
        basicCruise.DefaultCruiseAltitude = 10000
        Assert.assertEqual(10000, basicCruise.DefaultCruiseAltitude)
        basicCruise.AirspeedType = AgEAvtrAirspeedType.eCAS
        Assert.assertEqual(AgEAvtrAirspeedType.eCAS, basicCruise.AirspeedType)
        basicCruise.UseAeroPropFuel = False
        Assert.assertEqual(False, basicCruise.UseAeroPropFuel)
        basicCruise.ScaleFuelFlowByNonStdDensity = True
        Assert.assertTrue(basicCruise.ScaleFuelFlowByNonStdDensity)

        basicCruise.MinAirspeed = 101
        Assert.assertAlmostEqual(101, basicCruise.MinAirspeed, delta=tolerance)
        basicCruise.MaxEnduranceAirspeed = 102
        Assert.assertEqual(102, basicCruise.MaxEnduranceAirspeed)
        basicCruise.MaxAirspeed = 553
        Assert.assertAlmostEqual(553, basicCruise.MaxAirspeed, delta=tolerance)
        basicCruise.MaxRangeAirspeed = 104
        Assert.assertEqual(104, basicCruise.MaxRangeAirspeed)
        basicCruise.MaxPerfAirspeed = 105
        Assert.assertEqual(105, basicCruise.MaxPerfAirspeed)

        basicCruise.AirspeedType = AgEAvtrAirspeedType.eMach
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicCruise.AirspeedType)

        # Check that the airspeed was converted properly
        # Assert.AreEqual(0.158222, basicCruise.MinAirspeed, tolerance);

        basicCruise.MinAirspeed = 0.1
        Assert.assertEqual(0.1, basicCruise.MinAirspeed)
        basicCruise.MaxEnduranceAirspeed = 0.12
        Assert.assertEqual(0.12, basicCruise.MaxEnduranceAirspeed)
        basicCruise.MaxAirspeed = 0.96
        Assert.assertEqual(0.96, basicCruise.MaxAirspeed)
        basicCruise.MaxRangeAirspeed = 0.14
        Assert.assertEqual(0.14, basicCruise.MaxRangeAirspeed)
        basicCruise.MaxPerfAirspeed = 0.15
        Assert.assertEqual(0.15, basicCruise.MaxPerfAirspeed)

        basicCruise.MinAirspeedFuelFlow = 101.5
        Assert.assertEqual(101.5, basicCruise.MinAirspeedFuelFlow)
        basicCruise.MaxEnduranceFuelFlow = 102.5
        Assert.assertEqual(102.5, basicCruise.MaxEnduranceFuelFlow)
        basicCruise.MaxAirspeedFuelFlow = 553.5
        Assert.assertAlmostEqual(553.5, basicCruise.MaxAirspeedFuelFlow, delta=tolerance)
        basicCruise.MaxRangeFuelFlow = 104.5
        Assert.assertEqual(104.5, basicCruise.MaxRangeFuelFlow)
        basicCruise.MaxPerfAirspeedFuelFlow = 105.5
        Assert.assertEqual(105.5, basicCruise.MaxPerfAirspeedFuelFlow)

        basicCruise.UseAeroPropFuel = True
        Assert.assertTrue(basicCruise.UseAeroPropFuel)

        def action369():
            basicCruise.ScaleFuelFlowByNonStdDensity = True

        TryCatchAssertBlock.ExpectedException("must be", action369)

        def action370():
            basicCruise.MinAirspeedFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action370)

        def action371():
            basicCruise.MaxEnduranceFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action371)

        def action372():
            basicCruise.MaxAirspeedFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action372)

        def action373():
            basicCruise.MaxRangeFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action373)

        def action374():
            basicCruise.MaxPerfAirspeedFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action374)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvancedCruiseModel
    @category("Aircraft Tests")
    def test_AdvancedCruiseModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        cruise = newAC.Cruise
        cruise.GetAsCatalogItem().AddChildOfType("Advanced Cruise Model", "Adv Cruise")
        advCruise = cruise.GetAdvCruiseByName("Adv Cruise")

        advCruise.DefaultCruiseAltitude = 10001
        Assert.assertEqual(10001, advCruise.DefaultCruiseAltitude)
        advCruise.MaxPerfAirspeed = AgEAvtrCruiseMaxPerfSpeedType.eMaxSpeedDryThrust
        Assert.assertEqual(AgEAvtrCruiseMaxPerfSpeedType.eMaxSpeedDryThrust, advCruise.MaxPerfAirspeed)

        advCruise.UseAirspeedLimit = False
        Assert.assertEqual(False, advCruise.UseAirspeedLimit)

        def action375():
            advCruise.AltitudeLimit = 9000

        TryCatchAssertBlock.ExpectedException("must be", action375)

        def action376():
            advCruise.SetAirspeedLimit(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action376)

        advCruise.UseAirspeedLimit = True
        advCruise.AltitudeLimit = 9000
        Assert.assertEqual(9000, advCruise.AltitudeLimit)
        advCruise.SetAirspeedLimit(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advCruise.AirspeedLimitType)
        Assert.assertAlmostEqual(251, advCruise.AirspeedLimit, delta=tolerance)
        advCruise.SetAirspeedLimit(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advCruise.AirspeedLimitType)
        Assert.assertEqual(0.4, advCruise.AirspeedLimit)

        advCruise.ComputeDeltaDownrange = 11
        Assert.assertEqual(11, advCruise.ComputeDeltaDownrange)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicDescentModel
    @category("Aircraft Tests")
    def test_BasicDescentModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        descent = newAC.Descent
        basicDescent = descent.GetBuiltInModel()

        basicDescent.CeilingAltitude = 70001
        Assert.assertEqual(70001, basicDescent.CeilingAltitude)

        basicDescent.SetAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicDescent.AirspeedType)
        Assert.assertAlmostEqual(251, basicDescent.Airspeed, delta=tolerance)
        basicDescent.SetAirspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicDescent.AirspeedType)
        Assert.assertEqual(0.4, basicDescent.Airspeed)

        basicDescent.AltitudeRate = -4001
        Assert.assertAlmostEqual(-4001, basicDescent.AltitudeRate, delta=tolerance)

        basicDescent.UseAeroPropFuel = True
        Assert.assertTrue(basicDescent.UseAeroPropFuel)

        def action377():
            testVal = basicDescent.ScaleFuelFlowByNonStdDensity

        TryCatchAssertBlock.ExpectedException("must be ", action377)

        def action378():
            basicDescent.ScaleFuelFlowByNonStdDensity = True

        TryCatchAssertBlock.ExpectedException("must be ", action378)

        def action379():
            testVal = basicDescent.FuelFlow

        TryCatchAssertBlock.ExpectedException("must be ", action379)

        def action380():
            basicDescent.FuelFlow = 1

        TryCatchAssertBlock.ExpectedException("must be ", action380)

        basicDescent.UseAeroPropFuel = False
        basicDescent.FuelFlow = 9000
        Assert.assertAlmostEqual(9000, basicDescent.FuelFlow, delta=tolerance)

        basicDescent.EnableRelativeAirspeedTolerance = False

        def action381():
            testVal = basicDescent.RelativeAirspeedTolerance

        TryCatchAssertBlock.ExpectedException("must be ", action381)

        def action382():
            basicDescent.RelativeAirspeedTolerance = 1

        TryCatchAssertBlock.ExpectedException("must be ", action382)

        basicDescent.EnableRelativeAirspeedTolerance = True
        basicDescent.RelativeAirspeedTolerance = 0.06
        Assert.assertEqual(0.06, basicDescent.RelativeAirspeedTolerance)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvancedDescentModel
    @category("Aircraft Tests")
    def test_AdvancedDescentModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        descent = newAC.Descent
        descent.GetAsCatalogItem().AddChildOfType("Advanced Descent Model", "Adv Descent")
        advDescent = descent.GetAdvDescentByName("Adv Descent")

        advDescent.DescentSpeedType = AgEAvtrDescentSpeedType.eDescentMaxRangeCruise
        Assert.assertEqual(AgEAvtrDescentSpeedType.eDescentMaxRangeCruise, advDescent.DescentSpeedType)

        def action383():
            advDescent.DescentStallSpeedRatio = 1.2

        TryCatchAssertBlock.ExpectedException("must be", action383)

        def action384():
            advDescent.SetDescentOverrideAirspeed(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action384)

        advDescent.DescentSpeedType = AgEAvtrDescentSpeedType.eDescentStallSpeedRatio
        advDescent.DescentStallSpeedRatio = 1.2
        Assert.assertEqual(1.2, advDescent.DescentStallSpeedRatio)

        advDescent.DescentSpeedType = AgEAvtrDescentSpeedType.eDescentSpeedOverride
        advDescent.SetDescentOverrideAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advDescent.DescentOverrideAirspeedType)
        Assert.assertAlmostEqual(251, advDescent.DescentOverrideAirspeed, delta=tolerance)

        advDescent.SetDescentOverrideAirspeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advDescent.DescentOverrideAirspeedType)
        Assert.assertEqual(0.4, advDescent.DescentOverrideAirspeed)

        advDescent.Speedbrakes = 95
        Assert.assertEqual(95, advDescent.Speedbrakes)

        advDescent.UseAirspeedLimit = False
        Assert.assertEqual(False, advDescent.UseAirspeedLimit)

        def action385():
            advDescent.AltitudeLimit = 9000

        TryCatchAssertBlock.ExpectedException("must be", action385)

        def action386():
            advDescent.SetAirspeedLimit(AgEAvtrAirspeedType.eTAS, 251)

        TryCatchAssertBlock.ExpectedException("must be", action386)

        advDescent.UseAirspeedLimit = True
        advDescent.AltitudeLimit = 9000
        Assert.assertEqual(9000, advDescent.AltitudeLimit)
        advDescent.SetAirspeedLimit(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advDescent.AirspeedLimitType)
        Assert.assertAlmostEqual(251, advDescent.AirspeedLimit, delta=tolerance)
        advDescent.SetAirspeedLimit(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advDescent.AirspeedLimitType)
        Assert.assertEqual(0.4, advDescent.AirspeedLimit)

        advDescent.ComputeDeltaAltitude = 1001
        Assert.assertEqual(1001, advDescent.ComputeDeltaAltitude)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicLandingModel
    @category("Aircraft Tests")
    def test_BasicLandingModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        landing = newAC.Landing
        basicLanding = landing.GetBuiltInModel()

        basicLanding.SetLandingSpeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicLanding.LandingSpeedType)
        Assert.assertAlmostEqual(251, basicLanding.LandingSpeed, delta=tolerance)
        basicLanding.SetLandingSpeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicLanding.LandingSpeedType)
        Assert.assertEqual(0.4, basicLanding.LandingSpeed)

        basicLanding.SeaLevelGroundRoll = 6
        Assert.assertAlmostEqual(6, basicLanding.SeaLevelGroundRoll, delta=tolerance)

        basicLanding.UseAeroPropFuel = True
        Assert.assertTrue(basicLanding.UseAeroPropFuel)

        def action387():
            basicLanding.ScaleFuelFlowByNonStdDensity = True

        TryCatchAssertBlock.ExpectedException("must be ", action387)

        def action388():
            basicLanding.FuelFlow = 9000

        TryCatchAssertBlock.ExpectedException("must be ", action388)

        basicLanding.UseAeroPropFuel = False

        basicLanding.ScaleFuelFlowByNonStdDensity = True
        Assert.assertTrue(basicLanding.ScaleFuelFlowByNonStdDensity)

        basicLanding.FuelFlow = 9000
        Assert.assertAlmostEqual(9000, basicLanding.FuelFlow, delta=tolerance)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvancedLandingModel
    @category("Aircraft Tests")
    def test_AdvancedLandingModel(self):
        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        landing = newAC.Landing
        landing.GetAsCatalogItem().AddChildOfType("Advanced Landing Model", "Adv Landing")
        advLanding = landing.GetAdvLandingByName("Adv Landing")

        advLanding.LandingSpeedMode = AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingAngleOfAttack
        Assert.assertEqual(AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingAngleOfAttack, advLanding.LandingSpeedMode)

        advLanding.SetAngleOfAttack(11)
        angle = advLanding.AngleOfAttack
        Assert.assertEqual(11, float(angle))

        advLanding.SetStallSpeedRatio(1.2)
        Assert.assertEqual(AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingStallSpeedRatio, advLanding.LandingSpeedMode)
        Assert.assertEqual(1.2, advLanding.StallSpeedRatio)

        advLanding.Flaps = 99
        Assert.assertEqual(99, advLanding.Flaps)

        advLanding.Speedbrakes = 98
        Assert.assertEqual(98, advLanding.Speedbrakes)

        advLanding.BrakingDecelG = 0.4
        Assert.assertEqual(0.4, advLanding.BrakingDecelG)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region BasicTakeoffModel
    @category("Aircraft Tests")
    def test_BasicTakeoffModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        takeoff = newAC.Takeoff
        basicTakeoff = takeoff.GetBuiltInModel()

        basicTakeoff.SetTakeoffSpeed(AgEAvtrAirspeedType.eTAS, 151)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicTakeoff.TakeoffSpeedType)
        Assert.assertAlmostEqual(151, basicTakeoff.TakeoffSpeed, delta=tolerance)
        basicTakeoff.SetTakeoffSpeed(AgEAvtrAirspeedType.eMach, 0.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicTakeoff.TakeoffSpeedType)
        Assert.assertEqual(0.3, basicTakeoff.TakeoffSpeed)

        basicTakeoff.SeaLevelGroundRoll = 6
        Assert.assertAlmostEqual(6, basicTakeoff.SeaLevelGroundRoll, delta=tolerance)

        basicTakeoff.SetDepartureSpeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, basicTakeoff.DepartureSpeedType)
        Assert.assertAlmostEqual(251, basicTakeoff.DepartureSpeed, delta=tolerance)
        basicTakeoff.SetDepartureSpeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, basicTakeoff.DepartureSpeedType)
        Assert.assertEqual(0.4, basicTakeoff.DepartureSpeed)

        basicTakeoff.UseAeroPropFuel = True
        Assert.assertTrue(basicTakeoff.UseAeroPropFuel)

        def action389():
            basicTakeoff.ScaleFuelFlowByNonStdDensity = True

        TryCatchAssertBlock.ExpectedException("must be ", action389)

        def action390():
            basicTakeoff.AccelFuelFlow = 8000

        TryCatchAssertBlock.ExpectedException("must be ", action390)

        def action391():
            basicTakeoff.DepartureFuelFlow = 9000

        TryCatchAssertBlock.ExpectedException("must be ", action391)

        basicTakeoff.UseAeroPropFuel = False

        basicTakeoff.ScaleFuelFlowByNonStdDensity = True
        Assert.assertTrue(basicTakeoff.ScaleFuelFlowByNonStdDensity)

        basicTakeoff.AccelFuelFlow = 8000
        Assert.assertAlmostEqual(8000, basicTakeoff.AccelFuelFlow, delta=tolerance)
        basicTakeoff.DepartureFuelFlow = 9000
        Assert.assertAlmostEqual(9000, basicTakeoff.DepartureFuelFlow, delta=tolerance)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region AdvancedTakeoffModel
    @category("Aircraft Tests")
    def test_AdvancedTakeoffModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        takeoff = newAC.Takeoff
        takeoff.GetAsCatalogItem().AddChildOfType("Advanced Takeoff Model", "Adv Takeoff")
        advTakeoff = takeoff.GetAdvTakeoffByName("Adv Takeoff")

        advTakeoff.TakeoffSpeedMode = AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingAngleOfAttack
        Assert.assertEqual(AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingAngleOfAttack, advTakeoff.TakeoffSpeedMode)

        advTakeoff.SetAngleOfAttack(11)
        angle = advTakeoff.AngleOfAttack
        Assert.assertEqual(11, float(angle))

        advTakeoff.SetStallSpeedRatio(1.2)
        Assert.assertEqual(AgEAvtrTakeoffLandingSpeedMode.eTakeoffLandingStallSpeedRatio, advTakeoff.TakeoffSpeedMode)
        Assert.assertEqual(1.2, advTakeoff.StallSpeedRatio)

        advTakeoff.Flaps = 99
        Assert.assertEqual(99, advTakeoff.Flaps)

        advTakeoff.DepartureSpeedMode = AgEAvtrDepartureSpeedMode.eUseClimbModel
        Assert.assertEqual(AgEAvtrDepartureSpeedMode.eUseClimbModel, advTakeoff.DepartureSpeedMode)

        advTakeoff.SetDepartureSpeedLimit(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, advTakeoff.DepartureSpeedLimitType)
        Assert.assertAlmostEqual(251, advTakeoff.DepartureSpeedLimit, delta=tolerance)
        advTakeoff.SetDepartureSpeedLimit(AgEAvtrAirspeedType.eMach, 0.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, advTakeoff.DepartureSpeedLimitType)
        Assert.assertAlmostEqual(0.3, advTakeoff.DepartureSpeedLimit, delta=tolerance)

        def action392():
            advTakeoff.UseAfterburner = True

        TryCatchAssertBlock.ExpectedException("not enabled ", action392)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region TerrainFollowModel
    @category("Aircraft Tests")
    def test_TerrainFollowModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        terrainFollowCategory = newAC.TerrainFollow
        terrainFollowCategory.GetAsCatalogItem().AddChildOfType("AGI TerrainFollow Model", "Test TerrainFollow Model")
        terrainFollow = terrainFollowCategory.GetTerrainFollowByName("Test TerrainFollow Model")

        terrainFollow.UseAeroPropFuel = True
        Assert.assertTrue(terrainFollow.UseAeroPropFuel)

        def action393():
            terrainFollow.ScaleFuelFlowByNonStdDensity = True

        TryCatchAssertBlock.ExpectedException("must be", action393)

        def action394():
            terrainFollow.MinAirspeedFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action394)

        def action395():
            terrainFollow.MaxEnduranceFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action395)

        def action396():
            terrainFollow.MaxAirspeedFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action396)

        def action397():
            terrainFollow.MaxRangeFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action397)

        def action398():
            terrainFollow.MaxPerfAirspeedFuelFlow = 100

        TryCatchAssertBlock.ExpectedException("must be", action398)

        terrainFollow.UseAeroPropFuel = False
        Assert.assertEqual(False, terrainFollow.UseAeroPropFuel)
        terrainFollow.ScaleFuelFlowByNonStdDensity = True
        Assert.assertTrue(terrainFollow.ScaleFuelFlowByNonStdDensity)

        terrainFollow.AirspeedType = AgEAvtrAirspeedType.eCAS
        Assert.assertEqual(AgEAvtrAirspeedType.eCAS, terrainFollow.AirspeedType)

        terrainFollow.MinAirspeed = 101
        Assert.assertAlmostEqual(101, terrainFollow.MinAirspeed, delta=tolerance)
        terrainFollow.MaxEnduranceAirspeed = 102
        Assert.assertEqual(102, terrainFollow.MaxEnduranceAirspeed)
        terrainFollow.MaxAirspeed = 553
        Assert.assertAlmostEqual(553, terrainFollow.MaxAirspeed, delta=tolerance)
        terrainFollow.MaxRangeAirspeed = 104
        Assert.assertEqual(104, terrainFollow.MaxRangeAirspeed)
        terrainFollow.MaxPerfAirspeed = 105
        Assert.assertEqual(105, terrainFollow.MaxPerfAirspeed)

        terrainFollow.AirspeedType = AgEAvtrAirspeedType.eMach
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, terrainFollow.AirspeedType)

        terrainFollow.MinAirspeed = 0.1
        Assert.assertEqual(0.1, terrainFollow.MinAirspeed)
        terrainFollow.MaxEnduranceAirspeed = 0.12
        Assert.assertEqual(0.12, terrainFollow.MaxEnduranceAirspeed)
        terrainFollow.MaxAirspeed = 0.96
        Assert.assertEqual(0.96, terrainFollow.MaxAirspeed)
        terrainFollow.MaxRangeAirspeed = 0.14
        Assert.assertEqual(0.14, terrainFollow.MaxRangeAirspeed)
        terrainFollow.MaxPerfAirspeed = 0.15
        Assert.assertEqual(0.15, terrainFollow.MaxPerfAirspeed)

        terrainFollow.MinAirspeedFuelFlow = 101.5
        Assert.assertEqual(101.5, terrainFollow.MinAirspeedFuelFlow)
        terrainFollow.MaxEnduranceFuelFlow = 102.5
        Assert.assertEqual(102.5, terrainFollow.MaxEnduranceFuelFlow)
        terrainFollow.MaxAirspeedFuelFlow = 553.5
        Assert.assertAlmostEqual(553.5, terrainFollow.MaxAirspeedFuelFlow, delta=tolerance)
        terrainFollow.MaxRangeFuelFlow = 104.5
        Assert.assertEqual(104.5, terrainFollow.MaxRangeFuelFlow)
        terrainFollow.MaxPerfAirspeedFuelFlow = 105.5
        Assert.assertEqual(105.5, terrainFollow.MaxPerfAirspeedFuelFlow)

        terrainFollow.MaxPitchAngle = 11
        maxPitchAngle = terrainFollow.MaxPitchAngle
        Assert.assertEqual(11, float(maxPitchAngle))

        terrainFollow.TerrainWindow = 4
        Assert.assertEqual(4, terrainFollow.TerrainWindow)

        Assert.assertTrue((terrainFollow.MaxLoadFactor > 1))

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region VTOLModel
    @category("Aircraft Tests")
    def test_VTOLModel(self):
        tolerance = 1e-09

        newAC: IAircraftModel = clr.CastAs(
            EarlyBoundTests.AG_AvtrAircraft.GetAsCatalogItem().Duplicate(), IAircraftModel
        )
        vtolCategory = newAC.VTOL
        vtolCategory.GetAsCatalogItem().AddChildOfType("AGI VTOL Model", "Test VTOL Model")
        vtol = vtolCategory.GetVTOLByName("Test VTOL Model")

        vtol.MaxHoverAltitude = 20000
        Assert.assertEqual(20000, vtol.MaxHoverAltitude)

        vtol.UseAeroPropFuel = True
        Assert.assertTrue(vtol.UseAeroPropFuel)

        def action399():
            vtol.ScaleFuelFlowByNonStdDensity = True

        TryCatchAssertBlock.ExpectedException("must be ", action399)

        def action400():
            vtol.HoverFuel = 0.25

        TryCatchAssertBlock.ExpectedException("must be ", action400)

        vtol.UseAeroPropFuel = False
        vtol.ScaleFuelFlowByNonStdDensity = True
        Assert.assertTrue(vtol.ScaleFuelFlowByNonStdDensity)
        vtol.HoverFuel = 0.25
        Assert.assertEqual(0.25, vtol.HoverFuel)

        vtol.HeadingRate = 11
        headingRate = vtol.HeadingRate
        Assert.assertEqual(11, float(headingRate))
        vtol.HeadingTransitionTime = 2
        Assert.assertEqual(2, vtol.HeadingTransitionTime)

        vtol.VerticalRate = 1002
        Assert.assertEqual(1002, vtol.VerticalRate)
        vtol.VerticalTransitionTime = 3
        Assert.assertEqual(3, vtol.VerticalTransitionTime)

        vtol.TranslationRate = 1003
        Assert.assertAlmostEqual(1003, vtol.TranslationRate, delta=tolerance)
        vtol.TranslationTransitionTime = 4
        Assert.assertEqual(4, vtol.TranslationTransitionTime)

        vtol.SetForwardFlightAirspeed(AgEAvtrAirspeedType.eTAS, 90)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, vtol.ForwardFlightAirspeedType)
        Assert.assertEqual(90, vtol.ForwardFlightAirspeed)
        vtol.SetForwardFlightAirspeed(AgEAvtrAirspeedType.eMach, 0.1)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, vtol.ForwardFlightAirspeedType)
        Assert.assertEqual(0.1, vtol.ForwardFlightAirspeed)

        vtol.ForwardFlightTransitionTime = 5
        Assert.assertEqual(5, vtol.ForwardFlightTransitionTime)

        newAC.GetAsCatalogItem().Remove()

    # endregion

    # region MissileModel
    @category("Missile Tests")
    def test_MissileModel(self):
        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileAsCatalog = missile.GetAsCatalogItem()

        Assert.assertEqual("NUNIT CSharp Test Missile", missileAsCatalog.Name)
        missileAsCatalog.Name = "NUNIT CSharp Test NameChange"
        Assert.assertEqual("NUNIT CSharp Test NameChange", missileAsCatalog.Name)
        missileAsCatalog.Name = "NUNIT CSharp Test Missile"

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePerformanceModels
    @category("Missile Tests")
    def test_MissilePerformanceModels(self):
        tolerance = 1e-09

        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missile.MaxLoadFactor = 11
        Assert.assertEqual(11, missile.MaxLoadFactor)
        missile.ManeuverMode = AgEAvtrAccelManeuverMode.eAccelManeuverModeDensityScale
        Assert.assertEqual(AgEAvtrAccelManeuverMode.eAccelManeuverModeDensityScale, missile.ManeuverMode)

        def action401():
            testVal = missile.ManeuverModeHelper

        TryCatchAssertBlock.ExpectedException("must be set", action401)

        missile.ManeuverMode = AgEAvtrAccelManeuverMode.eAccelManeuverModeAeroProp
        self.ManeuverModeHelperOptions(missile.ManeuverModeHelper)

        self.AttitudeTransitionOptions(missile.AttitudeTransitions)

        missile.IgnoreFPAForClimbDescentTransitions = True
        Assert.assertTrue(missile.IgnoreFPAForClimbDescentTransitions)

        missile.SetClimbAirspeed(AgEAvtrAirspeedType.eMach, 2.1)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, missile.ClimbAirspeedType)
        Assert.assertEqual(2.1, missile.ClimbAirspeed)
        missile.SetClimbAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, missile.ClimbAirspeedType)
        Assert.assertAlmostEqual(251, missile.ClimbAirspeed, delta=tolerance)
        missile.ClimbFailOnInsufficientPerformance = False
        Assert.assertEqual(False, missile.ClimbFailOnInsufficientPerformance)

        missile.SetCruiseMaxAirspeed(AgEAvtrAirspeedType.eMach, 2.2)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, missile.CruiseMaxAirspeedType)
        Assert.assertEqual(2.2, missile.CruiseMaxAirspeed)
        missile.SetCruiseMaxAirspeed(AgEAvtrAirspeedType.eTAS, 252)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, missile.CruiseMaxAirspeedType)
        Assert.assertAlmostEqual(252, missile.CruiseMaxAirspeed, delta=tolerance)

        missile.SetDescentAirspeed(AgEAvtrAirspeedType.eMach, 2.3)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, missile.DescentAirspeedType)
        Assert.assertEqual(2.3, missile.DescentAirspeed)
        missile.SetDescentAirspeed(AgEAvtrAirspeedType.eTAS, 253)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, missile.DescentAirspeedType)
        Assert.assertAlmostEqual(253, missile.DescentAirspeed, delta=tolerance)
        missile.DescentFailOnInsufficientPerformance = False
        Assert.assertEqual(False, missile.DescentFailOnInsufficientPerformance)

        missile.ClimbMinFPA = 3.1
        climbMinFPA = missile.ClimbMinFPA
        Assert.assertEqual(3.1, float(climbMinFPA))
        missile.ClimbMaxFPA = 60.1
        climbMaxFPA = missile.ClimbMaxFPA
        Assert.assertAlmostEqual(60.1, float(climbMaxFPA), delta=tolerance)

        missile.CruiseDefaultAltitude = 15000
        Assert.assertEqual(15000, missile.CruiseDefaultAltitude)

        missile.DescentMinFPA = -60.2
        descentMinFPA = missile.DescentMinFPA
        Assert.assertAlmostEqual(-60.2, float(descentMinFPA), delta=tolerance)
        missile.DescentMaxFPA = -3.2
        descentMaxFPA = missile.DescentMaxFPA
        Assert.assertEqual(-3.2, float(descentMaxFPA))

        missile.UseTotalTempLimit = False

        def action402():
            missile.TotalTempLimit = 3000

        TryCatchAssertBlock.ExpectedException("must be", action402)
        missile.UseTotalTempLimit = True
        Assert.assertTrue(missile.UseTotalTempLimit)
        missile.TotalTempLimit = 3000
        Assert.assertEqual(3000, missile.TotalTempLimit)

        missile.UseMachLimit = False

        def action403():
            missile.MachLimit = 6

        TryCatchAssertBlock.ExpectedException("must be", action403)
        missile.UseMachLimit = True
        Assert.assertTrue(missile.UseMachLimit)
        missile.MachLimit = 6
        Assert.assertEqual(6, missile.MachLimit)

        missile.UseEASLimit = False

        def action404():
            missile.EASLimit = 800

        TryCatchAssertBlock.ExpectedException("must be", action404)
        missile.UseEASLimit = True
        Assert.assertTrue(missile.UseEASLimit)
        missile.EASLimit = 800
        Assert.assertEqual(800, missile.EASLimit)

        self.ConfigurationOptions(missile.DefaultConfiguration)

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissileAeroSimple
    @category("Missile Tests")
    def test_MissileAeroSimple(self):
        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileAero = missile.Aerodynamics
        missileAero.AeroStrategy = AgEAvtrMissileAeroStrategy.eMissileAeroSimple
        Assert.assertEqual(AgEAvtrMissileAeroStrategy.eMissileAeroSimple, missileAero.AeroStrategy)
        simple = missileAero.ModeAsSimple

        simple.SRef = 5
        Assert.assertEqual(5, simple.SRef)
        simple.ClMax = 2
        Assert.assertEqual(2, simple.ClMax)
        simple.Cd = 0.05
        Assert.assertEqual(0.05, simple.Cd)

        Assert.assertEqual(False, simple.CalculateAOA)
        simple.SetMaxAOA(True, 25)
        aoa = simple.MaxAOA
        Assert.assertTrue(simple.CalculateAOA)
        Assert.assertEqual(25, float(aoa))

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissileAeroExternal
    @category("Missile Tests")
    def test_MissileAeroExternal(self):
        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileAero = missile.Aerodynamics
        missileAero.AeroStrategy = AgEAvtrMissileAeroStrategy.eMissileAeroExternalFile
        Assert.assertEqual(AgEAvtrMissileAeroStrategy.eMissileAeroExternalFile, missileAero.AeroStrategy)
        externalAero = missileAero.ModeAsExternal

        externalAero.RefArea = 3
        Assert.assertEqual(3, externalAero.RefArea)
        Assert.assertEqual(False, externalAero.IsValid)

        nonexistingfilepath = TestBase.GetScenarioFile("DoesNotExist.aero")

        def action405():
            externalAero.SetFilepath(nonexistingfilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action405)

        aeroFilepath = TestBase.GetScenarioFile("simpleAero.aero")
        returnMsg = externalAero.SetFilepath(aeroFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertEqual(False, externalAero.CanSetRefArea)

        def action406():
            externalAero.RefArea = 0.05

        TryCatchAssertBlock.ExpectedException("", action406)
        Assert.assertTrue(externalAero.IsValid)

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissileAeroAdvanced
    @category("Missile Tests")
    def test_MissileAeroAdvanced(self):
        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileAero = missile.Aerodynamics
        missileAero.AeroStrategy = AgEAvtrMissileAeroStrategy.eMissileAeroAdvanced
        Assert.assertEqual(AgEAvtrMissileAeroStrategy.eMissileAeroAdvanced, missileAero.AeroStrategy)
        advancedAero = missileAero.ModeAsAdvanced

        self.AdvancedMissileAero(advancedAero)

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropSimple
    @category("Missile Tests")
    def test_MissilePropSimple(self):
        tolerance = 1e-09

        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileProp = missile.Propulsion
        missileProp.PropStrategy = AgEAvtrMissilePropStrategy.eMissilePropSimple
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropSimple, missileProp.PropStrategy)
        simpleProp = missileProp.ModeAsSimple

        simpleProp.MaxThrust = 2000
        Assert.assertEqual(2000, simpleProp.MaxThrust)
        simpleProp.FuelFlow = 600
        Assert.assertAlmostEqual(600, simpleProp.FuelFlow, delta=tolerance)
        simpleProp.NoThrustWhenNoFuel = False
        Assert.assertEqual(False, simpleProp.NoThrustWhenNoFuel)

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropExternal
    @category("Missile Tests")
    def test_MissilePropExternal(self):
        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileProp = missile.Propulsion
        missileProp.PropStrategy = AgEAvtrMissilePropStrategy.eMissilePropExternalFile
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropExternalFile, missileProp.PropStrategy)
        externalProp = missileProp.ModeAsExternal

        Assert.assertEqual(False, externalProp.IsValid)

        nonexistingPropFilepath = TestBase.GetScenarioFile("DoesNotExist.prop")

        def action407():
            externalProp.SetFilepath(nonexistingPropFilepath)

        TryCatchAssertBlock.ExpectedException("Failed to load the file.", action407)

        propFilepath = TestBase.GetScenarioFile("simpleProp.prop")
        returnMsg = externalProp.SetFilepath(propFilepath)
        Assert.assertTrue(("processed" in returnMsg))
        Assert.assertTrue(externalProp.IsValid)

        returnMsg2 = externalProp.Reload()
        Assert.assertTrue(("processed" in returnMsg2))

        externalProp.NoThrustWhenNoFuel = False
        Assert.assertEqual(False, externalProp.NoThrustWhenNoFuel)

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropRamjet
    @category("Missile Tests")
    def test_MissilePropRamjet(self):
        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileProp = missile.Propulsion
        missileProp.PropStrategy = AgEAvtrMissilePropStrategy.eMissilePropRamjet
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropRamjet, missileProp.PropStrategy)
        ramjetProp = missileProp.ModeAsRamjet

        ramjetProp.DesignAltitude = 5000
        Assert.assertEqual(5000, ramjetProp.DesignAltitude)
        ramjetProp.DesignMach = 3
        Assert.assertEqual(3, ramjetProp.DesignMach)
        ramjetProp.DesignThrust = 30000
        Assert.assertEqual(30000, ramjetProp.DesignThrust)
        ramjetProp.EngineTemp = 2000
        Assert.assertEqual(2000, ramjetProp.EngineTemp)

        ramjetProp.FuelHeatingValue = 41500000
        Assert.assertEqual(41500000, ramjetProp.FuelHeatingValue)
        ramjetProp.InletPressureRatio = 0.9
        Assert.assertEqual(0.9, ramjetProp.InletPressureRatio)
        ramjetProp.BurnerPressureRatio = 0.8
        Assert.assertEqual(0.8, ramjetProp.BurnerPressureRatio)
        ramjetProp.NozzlePressureRatio = 0.7
        Assert.assertEqual(0.7, ramjetProp.NozzlePressureRatio)
        ramjetProp.P0overP9 = 0.5
        Assert.assertEqual(0.5, ramjetProp.P0overP9)
        ramjetProp.BurnerEfficiency = 95
        Assert.assertEqual(95, ramjetProp.BurnerEfficiency)

        ramjetProp.NoThrustWhenNoFuel = False
        Assert.assertEqual(False, ramjetProp.NoThrustWhenNoFuel)

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropTurbojet
    @category("Missile Tests")
    def test_MissilePropTurbojet(self):
        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileProp = missile.Propulsion
        missileProp.PropStrategy = AgEAvtrMissilePropStrategy.eMissilePropTurbojet
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropTurbojet, missileProp.PropStrategy)
        turboProp = missileProp.ModeAsTurbojet

        turboProp.DesignAltitude = 5000
        Assert.assertEqual(5000, turboProp.DesignAltitude)
        turboProp.DesignMach = 3
        Assert.assertEqual(3, turboProp.DesignMach)
        turboProp.DesignThrust = 30000
        Assert.assertEqual(30000, turboProp.DesignThrust)
        turboProp.TurbineTemp = 2000
        Assert.assertEqual(2000, turboProp.TurbineTemp)
        turboProp.CompressorPressureRatio = 9
        Assert.assertEqual(9, turboProp.CompressorPressureRatio)

        turboProp.FuelHeatingValue = 41500000
        Assert.assertEqual(41500000, turboProp.FuelHeatingValue)
        turboProp.InletSubsonicPressureRatio = 0.9
        Assert.assertEqual(0.9, turboProp.InletSubsonicPressureRatio)
        turboProp.BurnerPressureRatio = 0.8
        Assert.assertEqual(0.8, turboProp.BurnerPressureRatio)
        turboProp.NozzlePressureRatio = 0.7
        Assert.assertEqual(0.7, turboProp.NozzlePressureRatio)
        turboProp.P0overP9 = 0.5
        Assert.assertEqual(0.5, turboProp.P0overP9)
        turboProp.CompressorEfficiency = 99
        Assert.assertEqual(99, turboProp.CompressorEfficiency)
        turboProp.TurbineEfficiency = 98
        Assert.assertEqual(98, turboProp.TurbineEfficiency)
        turboProp.BurnerEfficiency = 97
        Assert.assertEqual(97, turboProp.BurnerEfficiency)
        turboProp.MechanicalEfficiency = 96
        Assert.assertEqual(96, turboProp.MechanicalEfficiency)

        turboProp.NoThrustWhenNoFuel = False
        Assert.assertEqual(False, turboProp.NoThrustWhenNoFuel)

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region MissilePropRocket
    @category("Missile Tests")
    def test_MissilePropRocket(self):
        tolerance = 1e-09

        missileModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.MissileModels
        if missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"):
            missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")

        missile = missileModels.AddMissile("NUNIT CSharp Test Missile")
        Assert.assertEqual("NUNIT CSharp Test Missile", missile.GetAsCatalogItem().Name)
        Assert.assertTrue(missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

        missileProp = missile.Propulsion
        missileProp.PropStrategy = AgEAvtrMissilePropStrategy.eMissilePropRocket
        Assert.assertEqual(AgEAvtrMissilePropStrategy.eMissilePropRocket, missileProp.PropStrategy)
        rocketProp = missileProp.ModeAsRocket

        rocketProp.NozzleExpansionRatio = 7.1
        Assert.assertEqual(7.1, rocketProp.NozzleExpansionRatio)
        rocketProp.NozzleExitDiameter = 0.123
        Assert.assertEqual(0.123, rocketProp.NozzleExitDiameter)
        rocketProp.PropellantSpecificHeatRatio = 1.2
        Assert.assertEqual(1.2, rocketProp.PropellantSpecificHeatRatio)
        rocketProp.PropellantCharacteristicVelocity = 3120
        Assert.assertAlmostEqual(3120, rocketProp.PropellantCharacteristicVelocity, delta=tolerance)
        rocketProp.CombustionChamberPressure = 13000000.0
        Assert.assertEqual(13000000.0, rocketProp.CombustionChamberPressure)

        rocketProp.UseBoostSustainMode = False
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { rocketProp.BoostFuelFraction = 60; });
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { rocketProp.BoostChamberPressure = 2.1e7; });
        rocketProp.UseBoostSustainMode = True
        Assert.assertTrue(rocketProp.UseBoostSustainMode)
        rocketProp.BoostFuelFraction = 60
        Assert.assertEqual(60, rocketProp.BoostFuelFraction)
        rocketProp.BoostChamberPressure = 21000000.0
        Assert.assertEqual(21000000.0, rocketProp.BoostChamberPressure)

        rocketProp.NoThrustWhenNoFuel = False
        Assert.assertEqual(False, rocketProp.NoThrustWhenNoFuel)

        missileModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Missile")
        Assert.assertEqual(False, missileModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Missile"))

    # endregion

    # region RotorcraftModel
    @category("Missile Tests")
    def test_RotorcraftModel(self):
        rotorcraftModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.RotorcraftModels
        if rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Rotorcraft")

        rotorcraft = rotorcraftModels.AddRotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.GetAsCatalogItem().Name)
        Assert.assertTrue(rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"))

        rotorcraftAsCatalog = rotorcraft.GetAsCatalogItem()

        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraftAsCatalog.Name)
        rotorcraftAsCatalog.Name = "NUNIT CSharp Test Rotorcraft NameChange"
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft NameChange", rotorcraftAsCatalog.Name)
        rotorcraftAsCatalog.Name = "NUNIT CSharp Test Rotorcraft"

        rotorcraftModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual(False, rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"))

    # endregion

    # region RotorcraftPerformanceModels
    @category("Rotorcraft Tests")
    def test_RotorcraftPerformanceModels(self):
        tolerance = 1e-09

        rotorcraftModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.RotorcraftModels
        if rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Rotorcraft")

        rotorcraft = rotorcraftModels.AddRotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.GetAsCatalogItem().Name)
        Assert.assertTrue(rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"))

        rotorcraft.MaxAltitude = 11000
        Assert.assertEqual(11000, rotorcraft.MaxAltitude)
        rotorcraft.DefaultCruiseAltitude = 500
        Assert.assertEqual(500, rotorcraft.DefaultCruiseAltitude)
        rotorcraft.DescentRateFactor = 45
        Assert.assertEqual(45, rotorcraft.DescentRateFactor)
        rotorcraft.MaxClimbAngle = 55
        maxClimbAngle = rotorcraft.MaxClimbAngle
        Assert.assertEqual(55, float(maxClimbAngle))
        rotorcraft.ClimbAtCruiseAirspeed = False
        Assert.assertEqual(False, rotorcraft.ClimbAtCruiseAirspeed)
        rotorcraft.MaxDescentAngle = 56
        maxDescentAngle = rotorcraft.MaxDescentAngle
        Assert.assertEqual(56, float(maxDescentAngle))
        rotorcraft.MinDescentRate = 2000
        Assert.assertAlmostEqual(2000, rotorcraft.MinDescentRate, delta=tolerance)
        rotorcraft.MaxLoadFactor = 1.2
        Assert.assertEqual(1.2, rotorcraft.MaxLoadFactor)

        rotorcraft.RollRate = 30
        rollRate = rotorcraft.RollRate
        Assert.assertAlmostEqual(30, float(rollRate), delta=tolerance)
        rotorcraft.PitchRate = 20
        pitchRate = rotorcraft.PitchRate
        Assert.assertAlmostEqual(20, float(pitchRate), delta=tolerance)
        rotorcraft.YawRate = 15
        yawRate = rotorcraft.YawRate
        Assert.assertAlmostEqual(15, float(yawRate), delta=tolerance)
        rotorcraft.YawRateDot = 14
        yawRateDot = rotorcraft.YawRateDot
        Assert.assertAlmostEqual(14, float(yawRateDot), delta=tolerance)
        rotorcraft.MaxTransitionPitchAngle = 60
        maxTransitionPitchAngle = rotorcraft.MaxTransitionPitchAngle
        Assert.assertAlmostEqual(60, float(maxTransitionPitchAngle), delta=tolerance)
        rotorcraft.TFMaxFlightPathAngle = 20
        tFMaxFlightPathAngle = rotorcraft.TFMaxFlightPathAngle
        Assert.assertAlmostEqual(20, float(tFMaxFlightPathAngle), delta=tolerance)
        rotorcraft.TFTerrainWindow = 0.01
        Assert.assertEqual(0.01, rotorcraft.TFTerrainWindow)
        rotorcraft.ComputeDeltaAlt = 2000
        Assert.assertEqual(2000, rotorcraft.ComputeDeltaAlt)

        rotorcraft.SetMaxSafeAirspeed(AgEAvtrAirspeedType.eMach, 0.5)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, rotorcraft.MaxSafeAirspeedType)
        Assert.assertEqual(0.5, rotorcraft.MaxSafeAirspeed)
        rotorcraft.SetMaxSafeAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, rotorcraft.MaxSafeAirspeedType)
        Assert.assertAlmostEqual(251, rotorcraft.MaxSafeAirspeed, delta=tolerance)

        rotorcraft.SetMaxSafeTranslationSpeed(AgEAvtrAirspeedType.eMach, 0.4)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, rotorcraft.MaxSafeTranslationSpeedType)
        Assert.assertEqual(0.4, rotorcraft.MaxSafeTranslationSpeed)
        rotorcraft.SetMaxSafeTranslationSpeed(AgEAvtrAirspeedType.eTAS, 211)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, rotorcraft.MaxSafeTranslationSpeedType)
        Assert.assertAlmostEqual(211, rotorcraft.MaxSafeTranslationSpeed, delta=tolerance)

        rotorcraft.IgnoreFPAForClimbDescentTransitions = True
        Assert.assertTrue(rotorcraft.IgnoreFPAForClimbDescentTransitions)

        self.ConfigurationOptions(rotorcraft.DefaultConfiguration)

        rotorcraftModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual(False, rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"))

    # endregion

    # region RotorcraftAero
    @category("Rotorcraft Tests")
    def test_RotorcraftAero(self):
        rotorcraftModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.RotorcraftModels
        if rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Rotorcraft")

        rotorcraft = rotorcraftModels.AddRotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.GetAsCatalogItem().Name)
        Assert.assertTrue(rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"))

        aero = rotorcraft.Aerodynamics

        aero.RotorCount = 5
        Assert.assertEqual(5, aero.RotorCount)
        aero.RotorDiameter = 0.5
        Assert.assertEqual(0.5, aero.RotorDiameter)
        aero.BladesPerRotor = 3
        Assert.assertEqual(3, aero.BladesPerRotor)
        aero.BladeChord = 0.03
        Assert.assertEqual(0.03, aero.BladeChord)
        aero.RotorTipMach = 0.75
        Assert.assertEqual(0.75, aero.RotorTipMach)
        aero.FuselageFlatPlateArea = 2
        Assert.assertEqual(2, aero.FuselageFlatPlateArea)

        aero.RotorCount = 5
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { aero.TailRotorOffset = 10.1; });
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { aero.TailRotorDiameter = 2.5; });
        aero.RotorCount = 1
        aero.TailRotorOffset = 10.1
        Assert.assertEqual(10.1, aero.TailRotorOffset)
        aero.TailRotorDiameter = 2.5
        Assert.assertEqual(2.5, aero.TailRotorDiameter)

        aero.BladeProfileDragCD0 = 0.02
        Assert.assertEqual(0.02, aero.BladeProfileDragCD0)
        aero.BladeProfileDragK = 5
        Assert.assertEqual(5, aero.BladeProfileDragK)
        aero.InducedPowerCorrectionFactor = 1.2
        Assert.assertEqual(1.2, aero.InducedPowerCorrectionFactor)

        rotorcraftModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual(False, rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"))

    # endregion

    # region RotorcraftProp
    @category("Rotorcraft Tests")
    def test_RotorcraftProp(self):
        tolerance = 1e-09

        rotorcraftModels = EarlyBoundTests.AG_AvtrCatalog.AircraftCategory.RotorcraftModels
        if rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"):
            rotorcraftModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Rotorcraft")

        rotorcraft = rotorcraftModels.AddRotorcraft("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual("NUNIT CSharp Test Rotorcraft", rotorcraft.GetAsCatalogItem().Name)
        Assert.assertTrue(rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"))

        prop = rotorcraft.Propulsion

        prop.PowerplantType = AgEAvtrRotorcraftPowerplantType.eRotorcraftElectric
        Assert.assertEqual(AgEAvtrRotorcraftPowerplantType.eRotorcraftElectric, prop.PowerplantType)
        # TryCatchAssertBlock.ExpectedException("must be", delegate () { prop.MaxSLFuelFlow = 5; });

        prop.PowerplantType = AgEAvtrRotorcraftPowerplantType.eRotorcraftTurboshaft
        Assert.assertEqual(AgEAvtrRotorcraftPowerplantType.eRotorcraftTurboshaft, prop.PowerplantType)
        prop.MaxSLPower = 60
        Assert.assertEqual(60, prop.MaxSLPower)
        prop.MaxSLFuelFlow = 5
        Assert.assertAlmostEqual(5, prop.MaxSLFuelFlow, delta=tolerance)

        rotorcraftModels.GetAsCatalogSource().RemoveChild("NUNIT CSharp Test Rotorcraft")
        Assert.assertEqual(False, rotorcraftModels.GetAsCatalogSource().Contains("NUNIT CSharp Test Rotorcraft"))

    # endregion

    # region UserRunwaySource
    @category("Catalog Tests")
    def test_UserRunwaySource(self):
        userRunways = EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.UserRunways
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

        names = userRunways.GetAsCatalogSource().ChildNames
        nameCount = Array.Length(names)

        nunitRunway = userRunways.AddUserRunway("NUnitUserRunway")
        Assert.assertEqual("NUnitUserRunway", nunitRunway.GetAsCatalogItem().Name)
        Assert.assertTrue(userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"))
        names = userRunways.GetAsCatalogSource().ChildNames
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitRunway2 = userRunways.GetUserRunway("NUnitUserRunway")
        Assert.assertEqual("NUnitUserRunway", nunitRunway2.GetAsCatalogItem().Name)

        userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")
        names = userRunways.GetAsCatalogSource().ChildNames
        nameCount = nameCount - 1
        Assert.assertEqual(nameCount, Array.Length(names))
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

    # endregion

    # region UserRunway
    @category("Catalog Tests")
    def test_UserRunway(self):
        tolerance = 1e-09

        userRunways = EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.UserRunways
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

        nunitRunway = userRunways.AddUserRunway("NUnitUserRunway")

        nunitRunway.Latitude = 1
        lat = nunitRunway.Latitude
        Assert.assertEqual(1, float(lat))
        nunitRunway.Longitude = 2
        lon = nunitRunway.Longitude
        Assert.assertEqual(2, float(lon))
        nunitRunway.Altitude = 5
        Assert.assertEqual(5, nunitRunway.Altitude)
        terrainAlt = nunitRunway.GetTerrainAlt()
        Assert.assertEqual(terrainAlt, nunitRunway.Altitude)

        nunitRunway.HighEndHeading = 195
        highEndHeading = nunitRunway.HighEndHeading
        Assert.assertAlmostEqual(195, float(highEndHeading), delta=tolerance)
        lowEndHeading = nunitRunway.LowEndHeading
        Assert.assertAlmostEqual(15, float(lowEndHeading), delta=tolerance)
        nunitRunway.IsMagnetic = False
        Assert.assertEqual(False, nunitRunway.IsMagnetic)

        nunitRunway.Length = 5
        Assert.assertEqual(5, nunitRunway.Length)

        nunitRunway.CopySite()
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway2"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway2")

        nunitRunway2 = userRunways.AddUserRunway("NUnitUserRunway2")
        nunitRunway2.PasteSite()

        lat = nunitRunway2.Latitude
        Assert.assertEqual(1, float(lat))
        nunitRunway2.Longitude = 2
        lon = nunitRunway2.Longitude
        Assert.assertEqual(2, float(lon))
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway2"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway2")

    # endregion

    # region UserVTOLPointSource
    @category("Catalog Tests")
    def test_UserVTOLPointSource(self):
        userVTOLPoints = EarlyBoundTests.AG_AvtrCatalog.VTOLPointCategory.UserVTOLPoints
        if userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint"):
            userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint")

        names = userVTOLPoints.GetAsCatalogSource().ChildNames
        nameCount = Array.Length(names)

        nunitVTOLPoint = userVTOLPoints.AddUserVTOLPoint("NUnitUserVTOLPoint")
        Assert.assertEqual("NUnitUserVTOLPoint", nunitVTOLPoint.GetAsCatalogItem().Name)
        Assert.assertTrue(userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint"))
        names = userVTOLPoints.GetAsCatalogSource().ChildNames
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitVTOLPoint2 = userVTOLPoints.GetUserVTOLPoint("NUnitUserVTOLPoint")
        Assert.assertEqual("NUnitUserVTOLPoint", nunitVTOLPoint2.GetAsCatalogItem().Name)

        userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint")
        names = userVTOLPoints.GetAsCatalogSource().ChildNames
        nameCount = nameCount - 1
        Assert.assertEqual(nameCount, Array.Length(names))
        if userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint"):
            userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint")

    # endregion

    # region UserVTOLPoint
    @category("Catalog Tests")
    def test_UserVTOLPoint(self):
        userVTOLPoints = EarlyBoundTests.AG_AvtrCatalog.VTOLPointCategory.UserVTOLPoints
        if userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint"):
            userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint")

        nunitVTOLPoint = userVTOLPoints.AddUserVTOLPoint("NUnitUserVTOLPoint")

        nunitVTOLPoint.Latitude = 1
        lat = nunitVTOLPoint.Latitude
        Assert.assertEqual(1, float(lat))
        nunitVTOLPoint.Longitude = 2
        lon = nunitVTOLPoint.Longitude
        Assert.assertEqual(2, float(lon))
        nunitVTOLPoint.Altitude = 5
        Assert.assertEqual(5, nunitVTOLPoint.Altitude)
        terrainAlt = nunitVTOLPoint.GetTerrainAlt()
        Assert.assertEqual(terrainAlt, nunitVTOLPoint.Altitude)

        nunitVTOLPoint.CopySite()
        if userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint2"):
            userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint2")

        nunitVTOLPoint2 = userVTOLPoints.AddUserVTOLPoint("NUnitUserVTOLPoint2")
        nunitVTOLPoint2.PasteSite()

        lat = nunitVTOLPoint2.Latitude
        Assert.assertEqual(1, float(lat))
        nunitVTOLPoint2.Longitude = 2
        lon = nunitVTOLPoint2.Longitude
        Assert.assertEqual(2, float(lon))
        if userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint"):
            userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint")

        if userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint2"):
            userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint2")

    # endregion

    # region UserWaypointSource
    @category("Catalog Tests")
    def test_UserWaypointSource(self):
        userWaypoints = EarlyBoundTests.AG_AvtrCatalog.WaypointCategory.UserWaypoints
        if userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint"):
            userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint")

        names = userWaypoints.GetAsCatalogSource().ChildNames
        nameCount = Array.Length(names)

        nunitWaypoint = userWaypoints.AddUserWaypoint("NUnitUserWaypoint")
        Assert.assertEqual("NUnitUserWaypoint", nunitWaypoint.GetAsCatalogItem().Name)
        Assert.assertTrue(userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint"))
        names = userWaypoints.GetAsCatalogSource().ChildNames
        nameCount = nameCount + 1
        Assert.assertEqual(nameCount, Array.Length(names))

        nunitWaypoint2 = userWaypoints.GetUserWaypoint("NUnitUserWaypoint")
        Assert.assertEqual("NUnitUserWaypoint", nunitWaypoint2.GetAsCatalogItem().Name)

        userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint")
        names = userWaypoints.GetAsCatalogSource().ChildNames
        nameCount = nameCount - 1
        Assert.assertEqual(nameCount, Array.Length(names))
        if userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint"):
            userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint")

    # endregion

    # region UserWaypoint
    @category("Catalog Tests")
    def test_UserWaypoint(self):
        userWaypoints = EarlyBoundTests.AG_AvtrCatalog.WaypointCategory.UserWaypoints
        if userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint"):
            userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint")

        nunitWaypoint = userWaypoints.AddUserWaypoint("NUnitUserWaypoint")

        nunitWaypoint.Latitude = 1
        lat = nunitWaypoint.Latitude
        Assert.assertEqual(1, float(lat))
        nunitWaypoint.Longitude = 2
        lon = nunitWaypoint.Longitude
        Assert.assertEqual(2, float(lon))

        nunitWaypoint.CopySite()
        if userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint2"):
            userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint2")

        nunitWaypoint2 = userWaypoints.AddUserWaypoint("NUnitUserWaypoint2")
        nunitWaypoint2.PasteSite()

        lat = nunitWaypoint2.Latitude
        Assert.assertEqual(1, float(lat))
        nunitWaypoint2.Longitude = 2
        lon = nunitWaypoint2.Longitude
        Assert.assertEqual(2, float(lon))
        if userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint"):
            userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint")

        if userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint2"):
            userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint2")

    # endregion

    # region ARINC424AirportSource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424AirportSource(self):
        arincAirports = EarlyBoundTests.AG_AvtrCatalog.AirportCategory.ARINC424Airports
        self.ARINC424Source(arincAirports, "02 RANCH")

    # endregion

    # region ARINC424Airport
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Airport(self):
        tolerance = 0.01

        arincAirports = EarlyBoundTests.AG_AvtrCatalog.AirportCategory.ARINC424Airports
        ranch = arincAirports.GetARINC424Item("02 RANCH")

        identifier = ranch.GetValue("ICAO Code")
        Assert.assertEqual("K4", str(identifier))
        altitude = ranch.GetValue("Airport Elevation")
        Assert.assertEqual(3799, int(altitude))

        fields = ranch.GetAllFields()
        Assert.assertEqual("ICAO Code", fields[0])

        fieldsAndValues = ranch.GetAllFieldsAndValues()
        Assert.assertEqual("ICAO Code: K4", fieldsAndValues[0])

        Assert.assertEqual("02 RANCH", ranch.GetAsCatalogItem().Name)

        Assert.assertTrue(ranch.GetAsCatalogItem().IsReadOnly)

        ranch.CopySite()

        userRunways = EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.UserRunways
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

        nunitRunway = userRunways.AddUserRunway("NUnitUserRunway")

        nunitRunway.PasteSite()
        lat = nunitRunway.Latitude
        Assert.assertAlmostEqual(29.875, float(lat), delta=tolerance)
        lon = nunitRunway.Longitude
        Assert.assertAlmostEqual(-103.697, float(lon), delta=tolerance)
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

    # endregion

    # region ARINC424HelipadSource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424HelipadSource(self):
        arincHelipads = EarlyBoundTests.AG_AvtrCatalog.VTOLPointCategory.ARINC424Helipads
        self.ARINC424Source(arincHelipads, "1001 FOURTH AVENUE PLAZA H1")

    # endregion

    # region ARINC424Helipad
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Helipad(self):
        tolerance = 0.01

        arincHelipads = EarlyBoundTests.AG_AvtrCatalog.VTOLPointCategory.ARINC424Helipads
        fourthAveH1 = arincHelipads.GetARINC424Item("1001 FOURTH AVENUE PLAZA H1")

        identifier = fourthAveH1.GetValue("ICAO Code")
        Assert.assertEqual("K1", str(identifier))
        altitude = fourthAveH1.GetValue("Heliport Elevation")
        Assert.assertEqual(716, int(altitude))

        fields = fourthAveH1.GetAllFields()
        Assert.assertEqual("ICAO Code", fields[0])

        fieldsAndValues = fourthAveH1.GetAllFieldsAndValues()
        Assert.assertEqual("ICAO Code: K1", fieldsAndValues[0])

        Assert.assertEqual("1001 FOURTH AVENUE PLAZA H1", fourthAveH1.GetAsCatalogItem().Name)

        Assert.assertTrue(fourthAveH1.GetAsCatalogItem().IsReadOnly)

        fourthAveH1.CopySite()

        userVTOLPoints = EarlyBoundTests.AG_AvtrCatalog.VTOLPointCategory.UserVTOLPoints
        if userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint"):
            userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint")

        nunitVTOLPoint = userVTOLPoints.AddUserVTOLPoint("NUnitUserVTOLPoint")

        nunitVTOLPoint.PasteSite()
        lat = nunitVTOLPoint.Latitude
        Assert.assertAlmostEqual(47.607, float(lat), delta=tolerance)
        lon = nunitVTOLPoint.Longitude
        Assert.assertAlmostEqual(-122.334, float(lon), delta=tolerance)
        Assert.assertAlmostEqual(716, nunitVTOLPoint.Altitude, delta=tolerance)
        if userVTOLPoints.GetAsCatalogSource().Contains("NUnitUserVTOLPoint"):
            userVTOLPoints.GetAsCatalogSource().RemoveChild("NUnitUserVTOLPoint")

    # endregion

    # region ARINC424NavaidSource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424NavaidSource(self):
        arincNavaids = EarlyBoundTests.AG_AvtrCatalog.NavaidCategory.ARINC424Navaids
        self.ARINC424Source(arincNavaids, "1B")

    # endregion

    # region ARINC424Navaid
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Navaid(self):
        tolerance = 0.01

        arincNavaids = EarlyBoundTests.AG_AvtrCatalog.NavaidCategory.ARINC424Navaids
        oneb = arincNavaids.GetARINC424Item("1B")

        identifier = oneb.GetValue("Navaid Identifier")
        Assert.assertTrue(("1B" in str(identifier)))
        freq = oneb.GetValue("Frequency")
        Assert.assertEqual(277, float(freq))

        fields = oneb.GetAllFields()
        Assert.assertEqual("Navaid Identifier", fields[0])

        fieldsAndValues = oneb.GetAllFieldsAndValues()
        Assert.assertTrue(("Navaid Identifier: 1B" in str(fieldsAndValues[0])))

        Assert.assertEqual("1B", oneb.GetAsCatalogItem().Name)

        Assert.assertTrue(oneb.GetAsCatalogItem().IsReadOnly)

        oneb.CopySite()

        userRunways = EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.UserRunways
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

        nunitRunway = userRunways.AddUserRunway("NUnitUserRunway")

        nunitRunway.PasteSite()
        lat = nunitRunway.Latitude
        Assert.assertAlmostEqual(43.931, float(lat), delta=tolerance)
        lon = nunitRunway.Longitude
        Assert.assertAlmostEqual(-60.023, float(lon), delta=tolerance)
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

    # endregion

    # region ARINC424RunwaySource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424RunwaySource(self):
        arincRunways = EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.ARINC424Runways
        self.ARINC424Source(arincRunways, "JOHN F KENNEDY INTL 04L 22R")

    # endregion

    # region ARINC424Runway
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Runway(self):
        tolerance = 0.01

        arincRunways = EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.ARINC424Runways
        jfk = arincRunways.GetARINC424Item("JOHN F KENNEDY INTL 04L 22R")

        identifier = jfk.GetValue("Airport ICAO Identifier")
        Assert.assertEqual("KJFK", str(identifier))
        altitude = jfk.GetValue("Altitude")
        Assert.assertEqual(12.5, float(altitude))

        fields = jfk.GetAllFields()
        Assert.assertEqual("Airport ICAO Identifier", fields[0])

        fieldsAndValues = jfk.GetAllFieldsAndValues()
        Assert.assertEqual("Airport ICAO Identifier: KJFK", fieldsAndValues[0])

        Assert.assertEqual("JOHN F KENNEDY INTL 04L 22R", jfk.GetAsCatalogItem().Name)

        Assert.assertTrue(jfk.GetAsCatalogItem().IsReadOnly)

        jfk.CopySite()

        userRunways = EarlyBoundTests.AG_AvtrCatalog.RunwayCategory.UserRunways
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

        nunitRunway = userRunways.AddUserRunway("NUnitUserRunway")

        nunitRunway.PasteSite()
        lat = nunitRunway.Latitude
        Assert.assertAlmostEqual(40.63, float(lat), delta=tolerance)
        lon = nunitRunway.Longitude
        Assert.assertAlmostEqual(-73.786, float(lon), delta=tolerance)
        Assert.assertAlmostEqual(12.5, nunitRunway.Altitude, delta=tolerance)
        if userRunways.GetAsCatalogSource().Contains("NUnitUserRunway"):
            userRunways.GetAsCatalogSource().RemoveChild("NUnitUserRunway")

    # endregion

    # region ARINC424WaypointSource
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424WaypointSource(self):
        arincWaypoints = EarlyBoundTests.AG_AvtrCatalog.WaypointCategory.ARINC424Waypoints
        self.ARINC424Source(arincWaypoints, "AAAMY")

    # endregion

    # region ARINC424Waypoint
    @category("Catalog Tests")
    @category("ARINC424 Tests")
    def test_ARINC424Waypoint(self):
        tolerance = 0.01

        arincWaypoints = EarlyBoundTests.AG_AvtrCatalog.WaypointCategory.ARINC424Waypoints
        aaamy = arincWaypoints.GetARINC424Item("AAAMY")

        identifier = aaamy.GetValue("ICAO Code")
        Assert.assertEqual("K5", str(identifier))
        latTest = aaamy.GetValue("Latitude")
        Assert.assertAlmostEqual(43.069, float(latTest), delta=tolerance)

        fields = aaamy.GetAllFields()
        Assert.assertEqual("Waypoint Ident", fields[0])

        fieldsAndValues = aaamy.GetAllFieldsAndValues()
        Assert.assertEqual("Waypoint Ident: AAAMY", fieldsAndValues[0])

        Assert.assertEqual("AAAMY", aaamy.GetAsCatalogItem().Name)

        Assert.assertTrue(aaamy.GetAsCatalogItem().IsReadOnly)

        aaamy.CopySite()

        userWaypoints = EarlyBoundTests.AG_AvtrCatalog.WaypointCategory.UserWaypoints
        if userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint"):
            userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint")

        nunitWaypoint = userWaypoints.AddUserWaypoint("NUnitUserWaypoint")

        nunitWaypoint.PasteSite()
        lat = nunitWaypoint.Latitude
        Assert.assertAlmostEqual(43.069, float(lat), delta=tolerance)
        lon = nunitWaypoint.Longitude
        Assert.assertAlmostEqual(-82.615, float(lon), delta=tolerance)
        if userWaypoints.GetAsCatalogSource().Contains("NUnitUserWaypoint"):
            userWaypoints.GetAsCatalogSource().RemoveChild("NUnitUserWaypoint")

    # endregion

    # region PrivateCatalogMethods

    def AdvancedMissileAero(self, advancedAero: "IMissileAdvancedAero"):
        advancedAero.BodyWidth = 0.2
        Assert.assertEqual(0.2, advancedAero.BodyWidth)
        advancedAero.BodyHeight = 0.3
        Assert.assertEqual(0.3, advancedAero.BodyHeight)
        advancedAero.BodyLength = 3
        Assert.assertEqual(3, advancedAero.BodyLength)
        advancedAero.NoseLength = 0.4
        Assert.assertEqual(0.4, advancedAero.NoseLength)
        advancedAero.NoseTipDiameter = 0.05
        Assert.assertEqual(0.05, advancedAero.NoseTipDiameter)
        advancedAero.NozzleDiameter = 0.5
        Assert.assertEqual(0.5, advancedAero.NozzleDiameter)

        advancedAero.MinMach = 0.2
        Assert.assertEqual(0.2, advancedAero.MinMach)
        advancedAero.MaxAOA = 50
        aoa = advancedAero.MaxAOA
        Assert.assertEqual(50, float(aoa))

        advancedAero.WingCount = 1
        Assert.assertEqual(1, advancedAero.WingCount)
        advancedAero.WingSpan = 0.2
        Assert.assertEqual(0.2, advancedAero.WingSpan)
        advancedAero.WingSurfaceArea = 3e-07
        Assert.assertEqual(3e-07, advancedAero.WingSurfaceArea)
        advancedAero.WingLiftFraction = 40
        Assert.assertEqual(40, advancedAero.WingLiftFraction)
        advancedAero.WingLeadingEdgeSweepAngle = 50
        sweep = advancedAero.WingLeadingEdgeSweepAngle
        Assert.assertEqual(50, float(sweep))
        advancedAero.WingLeadingEdgeSectionAngle = 6
        section = advancedAero.WingLeadingEdgeSectionAngle
        Assert.assertEqual(6, float(section))
        advancedAero.WingMeanAeroChordLength = 0.07
        Assert.assertEqual(0.07, advancedAero.WingMeanAeroChordLength)
        advancedAero.WingMaxThicknessAlongMAC = 0.008
        Assert.assertEqual(0.008, advancedAero.WingMaxThicknessAlongMAC)

        advancedAero.TailCount = 1
        Assert.assertEqual(1, advancedAero.TailCount)
        advancedAero.TailSpan = 0.2
        Assert.assertEqual(0.2, advancedAero.TailSpan)
        advancedAero.TailSurfaceArea = 3e-07
        Assert.assertEqual(3e-07, advancedAero.TailSurfaceArea)
        advancedAero.TailLiftFraction = 40
        Assert.assertEqual(40, advancedAero.TailLiftFraction)
        advancedAero.TailLeadingEdgeSweepAngle = 50
        tailSweep = advancedAero.TailLeadingEdgeSweepAngle
        Assert.assertEqual(50, float(tailSweep))
        advancedAero.TailLeadingEdgeSectionAngle = 6
        tailSection = advancedAero.TailLeadingEdgeSectionAngle
        Assert.assertEqual(6, float(tailSection))
        advancedAero.TailMeanAeroChordLength = 0.07
        Assert.assertEqual(0.07, advancedAero.TailMeanAeroChordLength)
        advancedAero.TailMaxThicknessAlongMAC = 0.008
        Assert.assertEqual(0.008, advancedAero.TailMaxThicknessAlongMAC)

    def EmpiricalJetEngineOptions(self, prop: "IAdvFixedWingEmpiricalJetEngine"):
        tolerance = 1e-09

        prop.MaxSeaLevelStaticThrust = 65000
        Assert.assertAlmostEqual(65000, prop.MaxSeaLevelStaticThrust, delta=tolerance)
        prop.DesignPointAltitude = 2
        Assert.assertEqual(2, prop.DesignPointAltitude)
        prop.DesignPointMachNumber = 0.75
        Assert.assertEqual(0.75, prop.DesignPointMachNumber)

        prop.FuelFlow = 25000
        Assert.assertAlmostEqual(25000, prop.FuelFlow, delta=tolerance)

    def AttitudeTransitionOptions(self, att: "IAttitudeTransitions"):
        tolerance = 1e-09

        att.PitchRate = 10
        pitchRate = att.PitchRate
        Assert.assertAlmostEqual(10, float(pitchRate), delta=tolerance)

        att.YawRate = 20
        yawRate = att.YawRate
        Assert.assertAlmostEqual(20, float(yawRate), delta=tolerance)

        att.RollRate = 30
        rollRate = att.RollRate
        Assert.assertAlmostEqual(30, float(rollRate), delta=tolerance)

    def ManeuverModeHelperOptions(self, helper: "IAeroPropManeuverModeHelper"):
        tolerance = 1e-09

        helper.Mode = AgEAvtrAccelManeuverAeroPropMode.eUseLiftCoefficientOnly
        Assert.assertEqual(AgEAvtrAccelManeuverAeroPropMode.eUseLiftCoefficientOnly, helper.Mode)

        helper.FlightMode = AgEAvtrAeroPropFlightMode.eFlightPerfTakeoff
        Assert.assertEqual(AgEAvtrAeroPropFlightMode.eFlightPerfTakeoff, helper.FlightMode)

        helper.UseAfterburner = True
        Assert.assertTrue(helper.UseAfterburner)

        helper.RefWeight = 20000
        Assert.assertEqual(20000, helper.RefWeight)
        helper.RefAltitude = 25000
        Assert.assertEqual(25000, helper.RefAltitude)
        helper.SetRefAirspeed(AgEAvtrAirspeedType.eTAS, 251)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, helper.RefAirspeedType)
        Assert.assertAlmostEqual(251, helper.RefAirspeed, delta=tolerance)
        helper.SetRefAirspeed(AgEAvtrAirspeedType.eMach, 0.6)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, helper.RefAirspeedType)
        Assert.assertAlmostEqual(0.6, helper.RefAirspeed, delta=tolerance)

        helper.RefLoadFactor = 6
        Assert.assertEqual(6, helper.RefLoadFactor)

        helper.ControlAuthority = 0.5
        Assert.assertEqual(0.5, helper.ControlAuthority)

    def ConfigurationOptions(self, defConfig: "IConfiguration"):
        defConfig.EmptyWeight = 100
        Assert.assertEqual(100, defConfig.EmptyWeight)

        defConfig.MaxLandingWeight = 500
        Assert.assertEqual(500, defConfig.MaxLandingWeight)

        defConfig.BaseDragIndex = 1
        Assert.assertEqual(1, defConfig.BaseDragIndex)

        defConfig.SetEmptyCG(1, 2, 3)
        Assert.assertEqual(1, defConfig.EmptyCGX)
        Assert.assertEqual(2, defConfig.EmptyCGY)
        Assert.assertEqual(3, defConfig.EmptyCGZ)

    def ARINC424Source(self, arincSource: "IARINC424Source", childName: str):
        Assert.assertTrue(arincSource.UseMasterDataFile)

        def action408():
            arincSource.OverrideDataFilepath = "NonExistantPath"

        TryCatchAssertBlock.ExpectedException("to access this", action408)

        arincSource.UseMasterDataFile = False
        arincSource.OverrideDataFilepath = "NonExistantPath"
        Assert.assertEqual("NonExistantPath", arincSource.OverrideDataFilepath)

        arincSource.UseMasterDataFile = True
        Assert.assertTrue(("FAA" in arincSource.MasterDataFilepath))

        catalogSource: ICatalogSource = clr.CastAs(arincSource, ICatalogSource)
        names = catalogSource.ChildNames
        Assert.assertTrue((Array.Length(names) > 0))
        Assert.assertTrue(catalogSource.Contains(childName))

        def action409():
            catalogSource.RemoveChild(childName)

        TryCatchAssertBlock.ExpectedException("", action409)

    def TestPropulsionEfficiencies(self, propEffs: "IPropulsionEfficiencies"):
        propEffs.TechnologyLevel = AgEAvtrJetEngineTechnologyLevel.eLevel5
        Assert.assertEqual(AgEAvtrJetEngineTechnologyLevel.eLevel5, propEffs.TechnologyLevel)
        propEffs.IntakeType = AgEAvtrJetEngineIntakeType.eSubsonicEmbedded
        Assert.assertEqual(AgEAvtrJetEngineIntakeType.eSubsonicEmbedded, propEffs.IntakeType)
        propEffs.TurbineType = AgEAvtrJetEngineTurbineType.eUncooled
        Assert.assertEqual(AgEAvtrJetEngineTurbineType.eUncooled, propEffs.TurbineType)
        propEffs.ExhaustNozzleType = AgEAvtrJetEngineExhaustNozzleType.eFixedAreaConvergent
        Assert.assertEqual(AgEAvtrJetEngineExhaustNozzleType.eFixedAreaConvergent, propEffs.ExhaustNozzleType)

    def TestPropulsionEfficienciesRamScram(self, propEffs: "IPropulsionEfficiencies"):
        # This tests the propulsion efficiencies interface only for Ramjets and Scramjets as the enumeration values are more limited
        propEffs.TechnologyLevel = AgEAvtrJetEngineTechnologyLevel.eLevel5
        Assert.assertEqual(AgEAvtrJetEngineTechnologyLevel.eLevel5, propEffs.TechnologyLevel)
        Assert.assertEqual(AgEAvtrJetEngineIntakeType.eSupersonicEmbedded, propEffs.IntakeType)

        def action410():
            turbineTypeTest = propEffs.TurbineType

        TryCatchAssertBlock.ExpectedException("turbine type", action410)
        Assert.assertEqual(
            AgEAvtrJetEngineExhaustNozzleType.eVariableAreaConvergentDivergent, propEffs.ExhaustNozzleType
        )

    def TestFuelAFPROP(self, afprop: "IFuelModelKeroseneAFPROP"):
        afprop.Subtype = AgEAvtrAFPROPFuelType.eAFPROPJetA
        Assert.assertEqual(AgEAvtrAFPROPFuelType.eAFPROPJetA, afprop.Subtype)

        def action411():
            afprop.SpecificEnergy = 40

        TryCatchAssertBlock.ExpectedException("must be", action411)

        afprop.Subtype = AgEAvtrAFPROPFuelType.eAFPROPOverride
        afprop.SpecificEnergy = 43.21
        Assert.assertEqual(43.21, afprop.SpecificEnergy)

    def TestFuelCEA(self, cea: "IFuelModelKeroseneCEA"):
        cea.Subtype = AgEAvtrCEAFuelType.eCEAJetA
        Assert.assertEqual(AgEAvtrCEAFuelType.eCEAJetA, cea.Subtype)

        def action412():
            cea.SpecificEnergy = 40

        TryCatchAssertBlock.ExpectedException("must be", action412)

        cea.Subtype = AgEAvtrCEAFuelType.eCEAOverride
        cea.SpecificEnergy = 43.21
        Assert.assertEqual(43.21, cea.SpecificEnergy)

    def TestTurbofanBasicAB(self, prop: "IAdvFixedWingTurbofanBasicABProp"):
        prop.CanUseAfterburner = False
        Assert.assertEqual(False, prop.CanUseAfterburner)

        def action413():
            prop.AfterburnerOn = False

        TryCatchAssertBlock.ExpectedException("must be", action413)

        def action414():
            prop.MaxAfterburnerTemp = 2000

        TryCatchAssertBlock.ExpectedException("must be", action414)

        prop.CanUseAfterburner = True
        prop.DesignAltitude = 33100
        Assert.assertEqual(33100, prop.DesignAltitude)
        prop.DesignMach = 0.75
        Assert.assertEqual(0.75, prop.DesignMach)
        prop.DesignThrust = 80000
        Assert.assertEqual(80000, prop.DesignThrust)
        prop.AfterburnerOn = True
        Assert.assertTrue(prop.AfterburnerOn)

        prop.MaxCompressionTemp = 800
        Assert.assertEqual(800, prop.MaxCompressionTemp)
        prop.MaxBurnerTemp = 1400
        Assert.assertEqual(1400, prop.MaxBurnerTemp)
        prop.MaxAfterburnerTemp = 1900
        Assert.assertEqual(1900, prop.MaxAfterburnerTemp)
        prop.HPCPressureRatio = 3.8
        Assert.assertEqual(3.8, prop.HPCPressureRatio)
        prop.LPCPressureRatio = 4.1
        Assert.assertEqual(4.1, prop.LPCPressureRatio)
        prop.FanPressureRatio = 3.6
        Assert.assertEqual(3.6, prop.FanPressureRatio)

        prop.FuelType = AgEAvtrJetFuelType.eHydrogen
        Assert.assertEqual(AgEAvtrJetFuelType.eHydrogen, prop.FuelType)

        def action415():
            afprop = prop.FuelModeAsAFPROP

        TryCatchAssertBlock.ExpectedException("must be", action415)

        def action416():
            cea = prop.FuelModeAsCEA

        TryCatchAssertBlock.ExpectedException("must be", action416)

        prop.FuelType = AgEAvtrJetFuelType.eKeroseneAFPROP
        self.TestFuelAFPROP(prop.FuelModeAsAFPROP)
        prop.FuelType = AgEAvtrJetFuelType.eKeroseneCEA
        self.TestFuelCEA(prop.FuelModeAsCEA)

        self.TestPropulsionEfficiencies(prop.EfficienciesAndLosses)

    def TestTurbojetBasicAB(self, prop: "IAdvFixedWingTurbojetBasicABProp"):
        prop.CanUseAfterburner = False
        Assert.assertEqual(False, prop.CanUseAfterburner)

        def action417():
            prop.AfterburnerOn = False

        TryCatchAssertBlock.ExpectedException("must be", action417)

        def action418():
            prop.MaxAfterburnerTemp = 2000

        TryCatchAssertBlock.ExpectedException("must be", action418)

        prop.CanUseAfterburner = True
        prop.DesignAltitude = 33100
        Assert.assertEqual(33100, prop.DesignAltitude)
        prop.DesignMach = 0.75
        Assert.assertEqual(0.75, prop.DesignMach)
        prop.DesignThrust = 80000
        Assert.assertEqual(80000, prop.DesignThrust)
        prop.AfterburnerOn = True
        Assert.assertTrue(prop.AfterburnerOn)

        prop.MaxCompressionTemp = 800
        Assert.assertEqual(800, prop.MaxCompressionTemp)
        prop.MaxBurnerTemp = 1400
        Assert.assertEqual(1400, prop.MaxBurnerTemp)
        prop.MaxAfterburnerTemp = 1900
        Assert.assertEqual(1900, prop.MaxAfterburnerTemp)
        prop.HPCPressureRatio = 3.8
        Assert.assertEqual(3.8, prop.HPCPressureRatio)
        prop.LPCPressureRatio = 3.7
        Assert.assertEqual(3.7, prop.LPCPressureRatio)

        prop.FuelType = AgEAvtrJetFuelType.eHydrogen
        Assert.assertEqual(AgEAvtrJetFuelType.eHydrogen, prop.FuelType)

        def action419():
            afprop = prop.FuelModeAsAFPROP

        TryCatchAssertBlock.ExpectedException("must be", action419)

        def action420():
            cea = prop.FuelModeAsCEA

        TryCatchAssertBlock.ExpectedException("must be", action420)

        prop.FuelType = AgEAvtrJetFuelType.eKeroseneAFPROP
        self.TestFuelAFPROP(prop.FuelModeAsAFPROP)
        prop.FuelType = AgEAvtrJetFuelType.eKeroseneCEA
        self.TestFuelCEA(prop.FuelModeAsCEA)

        self.TestPropulsionEfficiencies(prop.EfficienciesAndLosses)

    # endregion

    # region PrivateProcedureMethods

    def EmptyProcedures(self):
        index = EarlyBoundTests.AG_Procedures.Count - 1
        while index >= 0:
            EarlyBoundTests.AG_Procedures.RemoveAtIndex(index)

            index -= 1

        Assert.assertEqual(0, EarlyBoundTests.AG_Procedures.Count)

    def TestProcedureName(self, proc: "IProcedure", name: str):
        Assert.assertEqual(name, proc.Name)
        proc.Name = "Name Test"
        Assert.assertEqual("Name Test", proc.Name)

    def AltitudeOptions(self, alt: "IAltitudeOptions"):
        alt.UseDefaultCruiseAltitude = True

        def action421():
            alt.Altitude = 10000

        TryCatchAssertBlock.ExpectedException("must be ", action421)

        alt.UseDefaultCruiseAltitude = False
        alt.AltitudeReference = AgEAvtrAGLMSL.eAltAGL
        alt.Altitude = 5000
        Assert.assertEqual(AgEAvtrAGLMSL.eAltAGL, alt.AltitudeReference)
        Assert.assertEqual(5000, alt.Altitude)

    def AltitudeMSLOptions(self, altitudeOpts: "IAltitudeMSLOptions"):
        altitudeOpts.UseDefaultCruiseAltitude = True

        def action422():
            altitudeOpts.MSLAltitude = 10000

        TryCatchAssertBlock.ExpectedException("must be ", action422)

        altitudeOpts.UseDefaultCruiseAltitude = False
        altitudeOpts.MSLAltitude = 10000
        Assert.assertEqual(10000, altitudeOpts.MSLAltitude)

    def AltitudeMSLAndLevelOffOptions(self, altitudeOpts: "IAltitudeMSLAndLevelOffOptions"):
        altitudeOpts.UseDefaultCruiseAltitude = True
        # TryCatchAssertBlock.ExpectedException("must be ", delegate () { altitudeOpts.MSLAltitude = 10000; });

        altitudeOpts.UseDefaultCruiseAltitude = False
        altitudeOpts.MSLAltitude = 10000
        Assert.assertEqual(10000, altitudeOpts.MSLAltitude)

        altitudeOpts.MustLevelOff = False
        # TryCatchAssertBlock.ExpectedException("must be ", delegate () { altitudeOpts.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver; });
        altitudeOpts.MustLevelOff = True
        altitudeOpts.LevelOffMode = AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver
        Assert.assertEqual(AgEAvtrAltitudeConstraintManeuverMode.eLevelOffLeftTurnManeuver, altitudeOpts.LevelOffMode)

    def ArcAltitudeOptions(self, alt: "IArcAltitudeOptions"):
        alt.UseDefaultCruiseAltitude = True

        def action423():
            alt.StartArcAltitude = 10001

        TryCatchAssertBlock.ExpectedException("must be ", action423)

        def action424():
            alt.StopArcAltitude = 10002

        TryCatchAssertBlock.ExpectedException("must be ", action424)

        alt.UseDefaultCruiseAltitude = False
        alt.StartArcAltitude = 10001
        Assert.assertEqual(10001, alt.StartArcAltitude)
        alt.StopArcAltitude = 10002
        Assert.assertEqual(10002, alt.StopArcAltitude)

    def ArcAltitudeAndDelayOptions(self, alt: "IArcAltitudeAndDelayOptions"):
        alt.UseDefaultCruiseAltitude = True

        def action425():
            alt.DelayArcClimbDescents = True

        TryCatchAssertBlock.ExpectedException("must be ", action425)

        def action426():
            alt.StartArcAltitude = 10001

        TryCatchAssertBlock.ExpectedException("must be ", action426)

        def action427():
            alt.StopArcAltitude = 10002

        TryCatchAssertBlock.ExpectedException("must be ", action427)

        alt.UseDefaultCruiseAltitude = False
        alt.DelayArcClimbDescents = True
        Assert.assertTrue(alt.DelayArcClimbDescents)
        alt.StartArcAltitude = 10001
        Assert.assertEqual(10001, alt.StartArcAltitude)
        alt.StopArcAltitude = 10002
        Assert.assertEqual(10002, alt.StopArcAltitude)

    def HoverAltitudeOptions(self, alt: "IHoverAltitudeOptions"):
        alt.AltitudeReference = AgEAvtrAGLMSL.eAltAGL
        Assert.assertEqual(AgEAvtrAGLMSL.eAltAGL, alt.AltitudeReference)

        alt.Altitude = 5000
        Assert.assertEqual(5000, alt.Altitude)

        alt.FinalAltitudeRate = AgEAvtrVTOLRateMode.eAlwaysStop
        Assert.assertEqual(AgEAvtrVTOLRateMode.eAlwaysStop, alt.FinalAltitudeRate)

    def ArcOptions(self, arc: "IArcOptions"):
        arc.TurnDirection = AgEAvtrTurnDirection.eTurnRight
        Assert.assertEqual(AgEAvtrTurnDirection.eTurnRight, arc.TurnDirection)

        arc.StartBearing = 5
        bearing = arc.StartBearing
        Assert.assertEqual(5, float(bearing))
        arc.UseMagneticHeading = False
        Assert.assertEqual(False, arc.UseMagneticHeading)

        arc.Radius = 11
        Assert.assertEqual(11, arc.Radius)
        arc.TurnAngle = 100
        turnAngle = arc.TurnAngle
        Assert.assertEqual(100, float(turnAngle))

    def NavigationOptions(self, navOpts: "INavigationOptions"):
        tolerance = 1e-09

        navOpts.NavMode = AgEAvtrPointToPointMode.eArriveOnCourseForNext

        def action428():
            navOpts.ArriveOnCourse = 1

        TryCatchAssertBlock.ExpectedException("must be ", action428)

        def action429():
            navOpts.UseMagneticHeading = True

        TryCatchAssertBlock.ExpectedException("must be ", action429)

        navOpts.NavMode = AgEAvtrPointToPointMode.eArriveOnCourse
        navOpts.ArriveOnCourse = 1
        navOpts.UseMagneticHeading = True
        course = navOpts.ArriveOnCourse
        Assert.assertAlmostEqual(1, float(course), delta=tolerance)
        Assert.assertTrue(navOpts.UseMagneticHeading)

    def EnrouteOptions(self, enrouteOpts: "IEnrouteOptions"):
        enrouteOpts.UseMaxSpeedTurns = True
        enrouteOpts.MaxTurnRadiusFactor = 3.5
        Assert.assertTrue(enrouteOpts.UseMaxSpeedTurns)
        Assert.assertEqual(3.5, enrouteOpts.MaxTurnRadiusFactor)

    def EnrouteAndDelayOptions(self, enrouteOpts: "IEnrouteAndDelayOptions"):
        enrouteOpts.DelayEnrouteClimbDescents = True
        enrouteOpts.UseMaxSpeedTurns = True
        enrouteOpts.MaxTurnRadiusFactor = 3.5
        Assert.assertTrue(enrouteOpts.DelayEnrouteClimbDescents)
        Assert.assertTrue(enrouteOpts.UseMaxSpeedTurns)
        Assert.assertEqual(3.5, enrouteOpts.MaxTurnRadiusFactor)

    def EnrouteCruiseAirspeed(self, airspeedOpts: "ICruiseAirspeedOptions"):
        tolerance = 1e-09

        airspeedOpts.CruiseSpeedType = AgEAvtrCruiseSpeed.eMaxAirspeed

        def action430():
            airspeedOpts.SetOtherAirspeed(AgEAvtrAirspeedType.eTAS, 200)

        TryCatchAssertBlock.ExpectedException("must be set", action430)

        airspeedOpts.CruiseSpeedType = AgEAvtrCruiseSpeed.eOtherAirspeed
        airspeedOpts.SetOtherAirspeed(AgEAvtrAirspeedType.eTAS, 200)
        Assert.assertAlmostEqual(200, airspeedOpts.OtherAirspeed, delta=tolerance)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, airspeedOpts.OtherAirspeedType)

        airspeedOpts.SetOtherAirspeed(AgEAvtrAirspeedType.eMach, 0.5)
        Assert.assertAlmostEqual(0.5, airspeedOpts.OtherAirspeed, delta=tolerance)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, airspeedOpts.OtherAirspeedType)

    def EnrouteCruiseAirspeedAndProfile(self, airspeedOpts: "ICruiseAirspeedAndProfileOptions"):
        tolerance = 1e-09

        airspeedOpts.FlyCruiseAirspeedProfile = False
        Assert.assertEqual(False, airspeedOpts.FlyCruiseAirspeedProfile)

        airspeedOpts.CruiseSpeedType = AgEAvtrCruiseSpeed.eMaxAirspeed

        def action431():
            airspeedOpts.SetOtherAirspeed(AgEAvtrAirspeedType.eTAS, 200)

        TryCatchAssertBlock.ExpectedException("must be set", action431)

        airspeedOpts.CruiseSpeedType = AgEAvtrCruiseSpeed.eOtherAirspeed
        airspeedOpts.SetOtherAirspeed(AgEAvtrAirspeedType.eTAS, 200)
        Assert.assertAlmostEqual(200, airspeedOpts.OtherAirspeed, delta=tolerance)
        Assert.assertEqual(AgEAvtrAirspeedType.eTAS, airspeedOpts.OtherAirspeedType)

        airspeedOpts.SetOtherAirspeed(AgEAvtrAirspeedType.eMach, 0.5)
        Assert.assertAlmostEqual(0.5, airspeedOpts.OtherAirspeed, delta=tolerance)
        Assert.assertEqual(AgEAvtrAirspeedType.eMach, airspeedOpts.OtherAirspeedType)

    def EnrouteTurnDirection(self, turnOpts: "IEnrouteTurnDirectionOptions"):
        turnOpts.EnrouteFirstTurn = AgEAvtrNavigatorTurnDir.eNavigatorTurnLeft
        Assert.assertEqual(AgEAvtrNavigatorTurnDir.eNavigatorTurnLeft, turnOpts.EnrouteFirstTurn)
        turnOpts.EnrouteSecondTurn = AgEAvtrNavigatorTurnDir.eNavigatorTurnRight
        Assert.assertEqual(AgEAvtrNavigatorTurnDir.eNavigatorTurnRight, turnOpts.EnrouteSecondTurn)

    def VerticalPlaneOptions(self, vertOpts: "IVerticalPlaneOptions"):
        vertOpts.MaxVertPlaneRadiusFactor = 2.5
        Assert.assertEqual(2.5, vertOpts.MaxVertPlaneRadiusFactor)
        vertOpts.MinEnrouteFlightPathAngle = -89.1
        minAng = vertOpts.MinEnrouteFlightPathAngle
        Assert.assertEqual(-89.1, float(minAng))
        vertOpts.MaxEnrouteFlightPathAngle = 89.2
        maxAng = vertOpts.MaxEnrouteFlightPathAngle
        Assert.assertEqual(89.2, float(maxAng))

    def VerticalPlaneAndFlightPathOptions(self, vertOpts: "IVerticalPlaneAndFlightPathOptions"):
        vertOpts.FinalFlightPathAngle = 3
        fpa = vertOpts.FinalFlightPathAngle
        Assert.assertEqual(3, float(fpa))
        vertOpts.MaxVertPlaneRadiusFactor = 2.5
        Assert.assertEqual(2.5, vertOpts.MaxVertPlaneRadiusFactor)
        vertOpts.MinEnrouteFlightPathAngle = -89.1
        minAng = vertOpts.MinEnrouteFlightPathAngle
        Assert.assertEqual(-89.1, float(minAng))
        vertOpts.MaxEnrouteFlightPathAngle = 89.2
        maxAng = vertOpts.MaxEnrouteFlightPathAngle
        Assert.assertEqual(89.2, float(maxAng))

    def ArcVerticalPlane(self, vertOpts: "IArcVerticalPlaneOptions"):
        vertOpts.StartArcFlightPathAngle = 3
        startArc = vertOpts.StartArcFlightPathAngle
        Assert.assertEqual(3, float(startArc))
        vertOpts.StopArcFlightPathAngle = 2
        stopArc = vertOpts.StopArcFlightPathAngle
        Assert.assertEqual(2, float(stopArc))
        vertOpts.MaxVertPlaneRadiusFactor = 2.5
        Assert.assertEqual(2.5, vertOpts.MaxVertPlaneRadiusFactor)
        vertOpts.MinEnrouteFlightPathAngle = -89.1
        minAng = vertOpts.MinEnrouteFlightPathAngle
        Assert.assertEqual(-89.1, float(minAng))
        vertOpts.MaxEnrouteFlightPathAngle = 89.2
        maxAng = vertOpts.MaxEnrouteFlightPathAngle
        Assert.assertEqual(89.2, float(maxAng))

    # endregion

    # region PrivateBasicManeuverMethods
    def BasicManeuverAirspeedOptions(self, airspeedOptions: "IBasicManeuverAirspeedOptions"):
        for airspeedMode in Enum.GetValues(clr.TypeOf(AgEAvtrBasicManeuverAirspeedMode)):
            airspeedOptions.AirspeedMode = airspeedMode
            Assert.assertEqual(airspeedMode, airspeedOptions.AirspeedMode)
            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainCurrentAirspeed:
                airspeedOptions.MaintainAirspeedType = AgEAvtrAirspeedType.eMach
                Assert.assertEqual(AgEAvtrAirspeedType.eMach, airspeedOptions.MaintainAirspeedType)
                airspeedOptions.MaintainAirspeedType = AgEAvtrAirspeedType.eEAS
                Assert.assertEqual(AgEAvtrAirspeedType.eEAS, airspeedOptions.MaintainAirspeedType)
                airspeedOptions.MaintainAirspeedType = AgEAvtrAirspeedType.eCAS
                Assert.assertEqual(AgEAvtrAirspeedType.eCAS, airspeedOptions.MaintainAirspeedType)
                airspeedOptions.MaintainAirspeedType = AgEAvtrAirspeedType.eTAS
                Assert.assertEqual(AgEAvtrAirspeedType.eTAS, airspeedOptions.MaintainAirspeedType)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eMaintainSpecifiedAirspeed:
                airspeedOptions.SpecifiedAirspeed = 111
                Assert.assertEqual(111, airspeedOptions.SpecifiedAirspeed)

                airspeedOptions.SpecifiedAirspeedType = AgEAvtrAirspeedType.eMach
                Assert.assertEqual(AgEAvtrAirspeedType.eMach, airspeedOptions.SpecifiedAirspeedType)
                airspeedOptions.SpecifiedAirspeedType = AgEAvtrAirspeedType.eEAS
                Assert.assertEqual(AgEAvtrAirspeedType.eEAS, airspeedOptions.SpecifiedAirspeedType)
                airspeedOptions.SpecifiedAirspeedType = AgEAvtrAirspeedType.eCAS
                Assert.assertEqual(AgEAvtrAirspeedType.eCAS, airspeedOptions.SpecifiedAirspeedType)
                airspeedOptions.SpecifiedAirspeedType = AgEAvtrAirspeedType.eTAS
                Assert.assertEqual(AgEAvtrAirspeedType.eTAS, airspeedOptions.SpecifiedAirspeedType)

                airspeedOptions.SpecifiedAccelDecelMode = AgEAvtrPerfModelOverride.ePerfModelValue
                Assert.assertEqual(AgEAvtrPerfModelOverride.ePerfModelValue, airspeedOptions.SpecifiedAccelDecelMode)

                def action432():
                    airspeedOptions.SpecifiedAccelDecelG = 200

                TryCatchAssertBlock.ExpectedException("must be set to override", action432)

                airspeedOptions.SpecifiedAccelDecelMode = AgEAvtrPerfModelOverride.eOverride
                Assert.assertEqual(AgEAvtrPerfModelOverride.eOverride, airspeedOptions.SpecifiedAccelDecelMode)

                airspeedOptions.SpecifiedAccelDecelG = 200
                Assert.assertEqual(200, airspeedOptions.SpecifiedAccelDecelG)

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

                def action433():
                    value = airspeedOptions.AccelG

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action433)

                def action434():
                    value = airspeedOptions.AccelMode

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action434)

                def action435():
                    value = airspeedOptions.DecelG

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action435)

                def action436():
                    value = airspeedOptions.DecelMode

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action436)

                def action437():
                    value = airspeedOptions.InterpolateEndG

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action437)

                def action438():
                    value = airspeedOptions.InterpolateEndTime

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action438)

                def action439():
                    value = airspeedOptions.InterpolateInitG

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action439)

                def action440():
                    value = airspeedOptions.InterpolateStopAtEndTime

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action440)

                def action441():
                    value = airspeedOptions.MaintainAirspeedType

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action441)

                def action442():
                    value = airspeedOptions.SpecifiedAccelDecelG

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action442)

                def action443():
                    value = airspeedOptions.SpecifiedAccelDecelMode

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action443)

                def action444():
                    value = airspeedOptions.SpecifiedAirspeed

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action444)

                def action445():
                    value = airspeedOptions.SpecifiedAirspeedType

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action445)

                def action446():
                    value = airspeedOptions.Throttle

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action446)

                def action447():
                    value = airspeedOptions.Thrust

                TryCatchAssertBlock.ExpectedException("must be set to the corresponding mode", action447)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eAccelAtG:
                airspeedOptions.AccelMode = AgEAvtrPerfModelOverride.ePerfModelValue
                Assert.assertEqual(AgEAvtrPerfModelOverride.ePerfModelValue, airspeedOptions.AccelMode)

                def action448():
                    airspeedOptions.AccelG = 300

                TryCatchAssertBlock.ExpectedException("must be set to override", action448)

                airspeedOptions.AccelMode = AgEAvtrPerfModelOverride.eOverride
                Assert.assertEqual(AgEAvtrPerfModelOverride.eOverride, airspeedOptions.AccelMode)

                airspeedOptions.AccelG = 300
                Assert.assertEqual(300, airspeedOptions.AccelG)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eDecelAtG:
                airspeedOptions.DecelMode = AgEAvtrPerfModelOverride.ePerfModelValue
                Assert.assertEqual(AgEAvtrPerfModelOverride.ePerfModelValue, airspeedOptions.DecelMode)

                def action449():
                    airspeedOptions.DecelG = 400

                TryCatchAssertBlock.ExpectedException("must be set to override", action449)

                airspeedOptions.DecelMode = AgEAvtrPerfModelOverride.eOverride
                Assert.assertEqual(AgEAvtrPerfModelOverride.eOverride, airspeedOptions.DecelMode)

                airspeedOptions.DecelG = 400
                Assert.assertEqual(400, airspeedOptions.DecelG)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eAccelDecelUnderGravity:
                pass

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eAccelDecelAeroProp:
                airspeedOptions.Throttle = 55
                Assert.assertEqual(55, airspeedOptions.Throttle)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eThrust:
                self.Test_IAgAvtrPropulsionThrust(airspeedOptions.Thrust)

            if airspeedMode == AgEAvtrBasicManeuverAirspeedMode.eInterpolateAccelDecel:
                airspeedOptions.InterpolateInitG = 5
                Assert.assertEqual(5, airspeedOptions.InterpolateInitG)
                airspeedOptions.InterpolateEndG = 6
                Assert.assertEqual(6, airspeedOptions.InterpolateEndG)
                airspeedOptions.InterpolateEndTime = 7
                Assert.assertEqual(7, airspeedOptions.InterpolateEndTime)

                airspeedOptions.InterpolateStopAtEndTime = False
                Assert.assertFalse(airspeedOptions.InterpolateStopAtEndTime)
                airspeedOptions.InterpolateStopAtEndTime = True
                Assert.assertTrue(airspeedOptions.InterpolateStopAtEndTime)

        airspeedOptions.MinSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated, airspeedOptions.MinSpeedLimits
        )
        airspeedOptions.MinSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated, airspeedOptions.MinSpeedLimits
        )
        airspeedOptions.MinSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated, airspeedOptions.MinSpeedLimits
        )
        airspeedOptions.MinSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated, airspeedOptions.MinSpeedLimits
        )

        airspeedOptions.MaxSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eConstrainIfViolated, airspeedOptions.MaxSpeedLimits
        )
        airspeedOptions.MaxSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eStopIfViolated, airspeedOptions.MaxSpeedLimits
        )
        airspeedOptions.MaxSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eErrorIfViolated, airspeedOptions.MaxSpeedLimits
        )
        airspeedOptions.MaxSpeedLimits = AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated
        Assert.assertEqual(
            AgEAvtrBasicManeuverStrategyAirspeedPerfLimits.eIgnoreIfViolated, airspeedOptions.MaxSpeedLimits
        )

    # endregion

    # region PrivateSiteMethods

    def TestSiteName(self, site: "ISite", name: str):
        Assert.assertEqual(name, site.Name)
        site.Name = "Name Test"
        Assert.assertEqual("Name Test", site.Name)
        site.Name = name

    def TestCatalogVTOLPoint(
        self, siteVTOLPointFromCatalog: "ISiteVTOLPointFromCatalog", catVTOLPoint: "ICatalogVTOLPoint"
    ):
        siteVTOLPointFromCatalog.SetCatalogVTOLPoint(catVTOLPoint)
        VTOLPointAsItem: ICatalogItem = clr.CastAs(catVTOLPoint, ICatalogItem)
        VTOLPointName = VTOLPointAsItem.Name
        Assert.assertEqual(VTOLPointName, siteVTOLPointFromCatalog.GetAsSite().Name)
        catVTOLPoint2: ICatalogItem = clr.CastAs(siteVTOLPointFromCatalog.GetCatalogVTOLPoint(), ICatalogItem)
        Assert.assertEqual(VTOLPointName, catVTOLPoint2.Name)

    def TestCatalogWaypoint(self, siteWaypointFromCatalog: "ISiteWaypointFromCatalog", catWaypoint: "ICatalogWaypoint"):
        siteWaypointFromCatalog.SetCatalogWaypoint(catWaypoint)
        waypointAsItem: ICatalogItem = clr.CastAs(catWaypoint, ICatalogItem)
        waypointName = waypointAsItem.Name
        Assert.assertEqual(waypointName, siteWaypointFromCatalog.GetAsSite().Name)
        catWaypoint2: ICatalogItem = clr.CastAs(siteWaypointFromCatalog.GetCatalogWaypoint(), ICatalogItem)
        Assert.assertEqual(waypointName, catWaypoint2.Name)

    # endregion
