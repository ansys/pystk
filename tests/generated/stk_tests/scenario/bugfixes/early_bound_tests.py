import pytest
from test_util import *
from assertion_harness import *
from events.simple_animation_monitor import *
from logger import *
from parameterized import *
from ansys.stk.core.stkobjects import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region Static DataMembers
    _animation: "StkObjectRoot" = None
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))

        EarlyBoundTests._animation = clr.CastAs(TestBase.Application, StkObjectRoot)
        Assert.assertIsNotNone(EarlyBoundTests._animation)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        del EarlyBoundTests._animation
        TestBase.Uninitialize()

    # endregion

    # region SetUp
    def setUp(self):
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "epSec")
        if not TestBase.NoGraphicsMode:
            EarlyBoundTests._animation.rewind()

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                EarlyBoundTests._animation.rewind()

    # endregion

    # region Animation Tests

    @parameterized.expand(
        [
            (ANIMATION_MODES.NORMAL,),
            (ANIMATION_MODES.X_REALTIME,),
            (ANIMATION_MODES.REALTIME,),
            (ANIMATION_MODES.TIME_ARRAY,),
        ]
    )
    @category("Graphics Tests")
    def test_AnimationModes(self, mode: "ANIMATION_MODES"):
        (Scenario(TestBase.Application.current_scenario)).set_time_period(0, 360)

        EarlyBoundTests._animation.mode = mode
        Assert.assertEqual(mode, EarlyBoundTests._animation.mode)

    @parameterized.expand([(0, 360, 60)])
    @category("Graphics Tests")
    def test_AnimationFlags(self, startTime: typing.Any, stopTime: typing.Any, stepInSecs: int):
        sc: "Scenario" = Scenario(TestBase.Application.current_scenario)
        sc.set_time_period(startTime, stopTime)

        # Change the animation step to test the animation mode
        sc.animation.anim_step_type = SCENARIO_TIME_STEP_TYPE.STEP
        sc.animation.anim_step_value = stepInSecs

        EarlyBoundTests._animation.high_speed = False
        Assert.assertFalse(EarlyBoundTests._animation.high_speed)
        EarlyBoundTests._animation.high_speed = True
        Assert.assertTrue(EarlyBoundTests._animation.high_speed)

        step: str = EarlyBoundTests._animation.step
        Assert.assertEqual(String.Format("Time Step: {0}.00 sec", stepInSecs), EarlyBoundTests._animation.step)

        currentTime: float = EarlyBoundTests._animation.current_time
        EarlyBoundTests._animation.current_time = 1.0
        Assert.assertEqual(1.0, EarlyBoundTests._animation.current_time)
        EarlyBoundTests._animation.current_time = currentTime

    # endregion

    def test_BUG51942_UseAnalysisStartForEpoch(self):
        sc: "Scenario" = Scenario(TestBase.Application.current_scenario)
        sc.set_time_period("Today", "Tomorrow")
        sc.use_analysis_start_time_for_epoch = True
        Assert.assertTrue(sc.use_analysis_start_time_for_epoch)
        sc.use_analysis_start_time_for_epoch = False
        Assert.assertFalse(sc.use_analysis_start_time_for_epoch)

    def test_Bug64212(self):
        TestBase.Application.close_scenario()
        codeBase: str = TestBase.CodeBaseDir
        di = DirectoryInfo(Path.Combine(codeBase, "EmptyDirectory"))
        if di.Exists:
            di.Delete(True)
        di.Create()
        with pytest.raises(Exception):
            TestBase.Application.load_scenario(di.FullName)
        Assert.assertTrue((len(di.GetFiles()) == 0))
        di.Delete(True)

    def test_BUG51942_SaveScenarioTimesAsTodayTomorrow(self):
        scenarioTitle: str = "BUG51942"
        TestBase.Application.close_scenario()
        filepath: str = Path.Combine(TestBase.TemporaryDirectory, (scenarioTitle + ".sc"))
        try:
            TestBase.Application.new_scenario(scenarioTitle)
            (Scenario(TestBase.Application.current_scenario)).set_time_period("Today", "Tomorrow")
            TestBase.Application.save_scenario_as(filepath)
            TestBase.Application.close_scenario()

            TestBase.Application.load_scenario(filepath)
            sc: "Scenario" = Scenario(TestBase.Application.current_scenario)

        finally:
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))

    def test_BUG64494(self):
        scenarioTitle: str = "BUG64494"
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario(scenarioTitle)
        TestBase.Application.close_scenario()
        TestBase.Application.execute_command("new / Scenario BUG64494 nodefault")
        TestBase.Application.close_scenario()
        TestBase.Application.execute_command("new / Scenario BUG64494 nodefault")
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("ScenarioTests", "ScenarioTests.sc"))

    def test_BUG65596_SetTimePeriod(self):
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        sc: "Scenario" = Scenario(TestBase.Application.current_scenario)

        starttime1: str = str(sc.start_time)
        stoptime1: str = str(sc.stop_time)

        sc.set_time_period("Today", "Now")

        starttime2: str = str(sc.start_time)
        stoptime2: str = str(sc.stop_time)

        sc.set_time_period("1 Jan 2000 00:00:00.000", "+1 day")

        starttime3: str = str(sc.start_time)
        stoptime3: str = str(sc.stop_time)

        sc.set_time_period("Today", "1 Jan 2030 00:00:00.000")

        # See BUG65596.
        # At this point, the StartTime is "1 Jan 2000 00:00:00.000" when it should be today's date.

        starttime4: str = str(sc.start_time)
        stoptime4: str = str(sc.stop_time)

    def test_BUG66310_ScenTimes_CovDef(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("BUG66310")

        covDef: "CoverageDefinition" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef"),
            CoverageDefinition,
        )
        covDef.interval.use_scenario_interval = True
        scenFilename: str = Path.Combine(TestBase.TemporaryDirectory, "BUG66310.sc")
        TestBase.Application.save_scenario_as(scenFilename)
        TestBase.Application.close_scenario()

        TestBase.Application.load_scenario(scenFilename)
        covDef = clr.CastAs(TestBase.Application.current_scenario.children["CovDef"], CoverageDefinition)
        Assert.assertTrue(covDef.interval.use_scenario_interval)

        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        scenario.analysis_interval.set_explicit_interval("11 Jul 2011 15:00:00.000", "12 Jul 2011 15:00:00.000")
        covDef = clr.CastAs(TestBase.Application.current_scenario.children["CovDef"], CoverageDefinition)
        Assert.assertTrue(covDef.interval.use_scenario_interval)

    def test_BUG68297_HeapCorruption(self):
        dateFormat: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat")
        try:
            TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
            self.HeapCorruption()

        finally:
            TestBase.Application.unit_preferences.set_current_unit("DateFormat", dateFormat)

    def HeapCorruption(self):
        sc: "Scenario" = Scenario(TestBase.Application.current_scenario)
        oSatOnMars: "IStkObject" = TestBase.Application.current_scenario.children.new_on_central_body(
            STK_OBJECT_TYPE.SATELLITE, "SatelliteOnMars", "Mars"
        )
        Assert.assertIsNotNone(oSatOnMars)

        sc.set_time_period("1 May 1999 12:00:00.00", "1 Jul 1999 12:00:00.00")

        # StartTime
        TestBase.logger.WriteLine6("The current StartTime is: {0}", sc.start_time)
        sc.start_time = "1 Jun 1999 12:00:00.00"
        TestBase.logger.WriteLine6("The new StartTime is: {0}", sc.start_time)
        Assert.assertEqual("1 Jun 1999 12:00:00.000", sc.start_time)
        # StopTime
        TestBase.logger.WriteLine6("The current StopTime is: {0}", sc.stop_time)
        sc.stop_time = "10 Jun 1999 12:00:00.01"
        TestBase.logger.WriteLine6("The new StopTime is: {0}", sc.stop_time)
        Assert.assertEqual("10 Jun 1999 12:00:00.010", sc.stop_time)

    @category("VO Tests")
    def test_BUG70140_DynamicDisplay_RequiresPreData(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("BUG70140")
        scen: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        sat1: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), Satellite
        )
        sat1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        (clr.CastAs(sat1.propagator, VehiclePropagatorTwoBody)).propagate()

        sat2: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat2"), Satellite
        )
        sat2.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        (clr.CastAs(sat2.propagator, VehiclePropagatorTwoBody)).propagate()

        sat1.graphics_3d.data_display.remove_all()

        # Graphics3DDataDisplayElement ele3 = sat1.VO.DataDisplay.AddDataDisplayRequiringPreData("EphemerisChooseAxes", "Satellite/sat1 Body Axes");
        ele: "Graphics3DDataDisplayElement" = sat1.graphics_3d.data_display.add_data_display_requiring_pre_data(
            "RIC", "Satellite/Satellite2"
        )
        ele.is_visible = True
        Assert.assertTrue(ele.is_visible)
        Assert.assertEqual("RIC", ele.name)
        (StkObjectRoot(TestBase.Application)).rewind()

    @category("VO Tests")
    def test_BUG70140_DynamicDisplay_RequiresPreData_Fail(self):
        def code1():
            TestBase.Application.close_scenario()
            TestBase.Application.new_scenario("BUG70140")
            scen: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

            sat1: "Satellite" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), Satellite
            )
            sat1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
            (clr.CastAs(sat1.propagator, VehiclePropagatorTwoBody)).propagate()

            sat2: "Satellite" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat2"), Satellite
            )
            sat2.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
            (clr.CastAs(sat2.propagator, VehiclePropagatorTwoBody)).propagate()

            sat1.graphics_3d.data_display.remove_all()

            ele2: "Graphics3DDataDisplayElement" = sat1.graphics_3d.data_display.add("EphemerisChooseAxes")

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("requires predata", str(ex), "Exception message mismatch")

    def test_BUG70140_LoadVDF_SaveScenarioAs(self):
        TestBase.Application.close_scenario()
        TestBase.Application.load_vdf(
            Path.Combine(TestBase.GetSTKHomeDir(), r"Data\ExampleScenarios\Intro_STK_Aircraft_Systems.vdf"), ""
        )

        tempScenarioPathname: str = Path.Combine(TestBase.TemporaryDirectory, "SubDir")
        tempScenarioPathname = Path.Combine(TestBase.TemporaryDirectory, "BUG70140.sc")
        TestBase.Application.save_scenario_as(tempScenarioPathname)
        if File.Exists(tempScenarioPathname):
            File.Delete(tempScenarioPathname)

        else:
            Assert.fail("Scenario file was not created.")

        TestBase.Application.close_scenario()
        TestBase.CleanupUserDirectory()
