import pytest
from test_util import *
from assertion_harness import *
from compatibility.interval_collection_extension_methods import *
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("AccessTests", "AccessTests.sc"))
        EarlyBoundTests._satellite = Satellite(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "Spy")
        )
        Assert.assertIsNotNone(EarlyBoundTests._satellite)
        # propagate satellite
        oPropagator: "PropagatorTwoBody" = PropagatorTwoBody(EarlyBoundTests._satellite.propagator)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.propagate()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        if TestBase.Application.current_scenario.children.contains(STKObjectType.SATELLITE, "Spy"):
            TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "Spy")

        EarlyBoundTests._satellite = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    _satellite: "Satellite" = None
    # endregion

    # region BasicTest
    def test_BasicTest(self):
        TestBase.logger.WriteLine("----- THE BASIC ACCESS TEST ----- BEGIN -----")

        access: "Access" = (IStkObject(EarlyBoundTests._satellite)).get_access("Facility/Facility1")

        Assert.assertEqual(r"Satellite-Spy-To-Facility-Facility1", access.name)
        Assert.assertEqual(r"/Application/STK/Scenario/AccessTests/Satellite/Spy", access.base.path)
        Assert.assertEqual(r"/Application/STK/Scenario/AccessTests/Facility/Facility1", access.target.path)

        advanced: "AccessAdvancedSettings" = access.advanced
        advanced.enable_light_time_delay = False
        Assert.assertFalse(advanced.enable_light_time_delay)
        advanced.enable_light_time_delay = True
        Assert.assertTrue(advanced.enable_light_time_delay)
        Assert.assertTrue(access.advanced.enable_light_time_delay)

        advanced.time_light_delay_convergence = 0.005
        Assert.assertEqual(0.005, advanced.time_light_delay_convergence)
        advanced.aberration_type = AberrationType.ANNUAL
        Assert.assertEqual(AberrationType.ANNUAL, advanced.aberration_type)
        advanced.aberration_type = AberrationType.NONE
        Assert.assertEqual(AberrationType.NONE, advanced.aberration_type)
        advanced.aberration_type = AberrationType.TOTAL
        Assert.assertEqual(AberrationType.TOTAL, advanced.aberration_type)

        advanced.use_default_clock_host_and_signal_sense = False
        Assert.assertFalse(advanced.use_default_clock_host_and_signal_sense)
        advanced.clock_host = IvClockHost.BASE
        Assert.assertEqual(IvClockHost.BASE, advanced.clock_host)
        advanced.clock_host = IvClockHost.TARGET
        Assert.assertEqual(IvClockHost.TARGET, advanced.clock_host)

        advanced.use_default_clock_host_and_signal_sense = True
        with pytest.raises(Exception):
            advanced.clock_host = IvClockHost.BASE
        Assert.assertTrue(advanced.use_default_clock_host_and_signal_sense)

        advanced.use_precise_event_times = True
        Assert.assertTrue(advanced.use_precise_event_times)
        advanced.time_convergence = 0.003
        Assert.assertEqual(0.003, advanced.time_convergence)
        advanced.relative_tolerance = 0.0001
        Assert.assertEqual(0.0001, advanced.relative_tolerance)
        advanced.absolute_tolerance = 1e-10
        Assert.assertEqual(1e-10, advanced.absolute_tolerance)
        advanced.use_precise_event_times = False
        Assert.assertFalse(advanced.use_precise_event_times)
        with pytest.raises(Exception):
            advanced.time_convergence = 0.002

        advanced.use_fixed_time_step = True
        Assert.assertTrue(advanced.use_fixed_time_step)
        with pytest.raises(Exception):
            advanced.maximum_time_step = 330

        advanced.fixed_step_size = 340
        Assert.assertEqual(340, advanced.fixed_step_size)
        advanced.fixed_time_bound = 1
        Assert.assertEqual(1, advanced.fixed_time_bound)

        advanced.use_fixed_time_step = False
        Assert.assertFalse(advanced.use_fixed_time_step)
        with pytest.raises(Exception):
            advanced.fixed_time_bound = 2
        advanced.maximum_time_step = 345
        Assert.assertEqual(345, advanced.maximum_time_step)
        advanced.minimum_time_step = 0.04
        Assert.assertEqual(0.04, advanced.minimum_time_step)

        #
        # VGT for Access object
        #

        Assert.assertIsNotNone(access.analysis_workbench_components)  # Verify that Access reference is initialized

        access.compute_access()
        provider: "AnalysisWorkbenchComponentProvider" = access.analysis_workbench_components
        Assert.assertIsNotNone(provider)

        Assert.assertTrue(provider.supports(VectorGeometryToolComponentType.ANGLE))
        type: "AngleType"
        for type in Enum.GetValues(clr.TypeOf(AngleType)):
            if provider.angles.factory.is_type_supported(type):
                obj: "IVectorGeometryToolAngle" = provider.angles.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.angles.remove("NameHere")

        Assert.assertTrue(provider.supports(VectorGeometryToolComponentType.AXES))
        type: "AxesType"
        for type in Enum.GetValues(clr.TypeOf(AxesType)):
            if provider.axes.factory.is_type_supported(type) and (type != AxesType.PLUGIN):
                obj: "IVectorGeometryToolAxes" = provider.axes.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.axes.remove("NameHere")

        Assert.assertTrue(provider.supports(VectorGeometryToolComponentType.PLANE))
        type: "PlaneType"
        for type in Enum.GetValues(clr.TypeOf(PlaneType)):
            if provider.planes.factory.is_type_supported(type):
                obj: "IVectorGeometryToolPlane" = provider.planes.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.planes.remove("NameHere")

        Assert.assertTrue(provider.supports(VectorGeometryToolComponentType.POINT))
        type: "PointType"
        for type in Enum.GetValues(clr.TypeOf(PointType)):
            if provider.points.factory.is_type_supported(type) and (type != PointType.PLUGIN):
                obj: "IVectorGeometryToolPoint" = provider.points.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.points.remove("NameHere")

        Assert.assertTrue(provider.supports(VectorGeometryToolComponentType.SYSTEM))
        type: "SystemType"
        for type in Enum.GetValues(clr.TypeOf(SystemType)):
            if provider.systems.factory.is_type_supported(type):
                obj: "IVectorGeometryToolSystem" = provider.systems.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.systems.remove("NameHere")

        Assert.assertTrue(provider.supports(VectorGeometryToolComponentType.VECTOR))
        type: "VectorType"
        for type in Enum.GetValues(clr.TypeOf(VectorType)):
            if provider.vectors.factory.is_type_supported(type) and (type != VectorType.PLUGIN):
                obj: "IVectorGeometryToolVector" = provider.vectors.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.vectors.remove("NameHere")

        type: "EventArrayType"

        for type in Enum.GetValues(clr.TypeOf(EventArrayType)):
            if provider.time_arrays.factory.is_type_supported(type):
                obj: "ITimeToolTimeArray" = provider.time_arrays.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.time_arrays.remove("NameHere")

        type: "EventIntervalType"
        for type in Enum.GetValues(clr.TypeOf(EventIntervalType)):
            if provider.time_intervals.factory.is_type_supported(type):
                obj: "ITimeToolTimeInterval" = provider.time_intervals.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.time_intervals.remove("NameHere")

        type: "EventIntervalListType"
        for type in Enum.GetValues(clr.TypeOf(EventIntervalListType)):
            if provider.time_interval_lists.factory.is_type_supported(type):
                obj: "ITimeToolTimeIntervalList" = provider.time_interval_lists.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.time_interval_lists.remove("NameHere")

        type: "EventIntervalType"
        for type in Enum.GetValues(clr.TypeOf(EventIntervalType)):
            if provider.time_intervals.factory.is_type_supported(type):
                obj: "ITimeToolTimeInterval" = provider.time_intervals.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.time_intervals.remove("NameHere")

        type: "TimeEventType"
        for type in Enum.GetValues(clr.TypeOf(TimeEventType)):
            if provider.time_instants.factory.is_type_supported(type):
                obj: "ITimeToolInstant" = provider.time_instants.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.time_instants.remove("NameHere")

        type: "CalculationScalarType"

        for type in Enum.GetValues(clr.TypeOf(CalculationScalarType)):
            if provider.calculation_scalars.factory.is_type_supported(type) and (type != CalculationScalarType.PLUGIN):
                obj: "ICalculationToolScalar" = provider.calculation_scalars.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.calculation_scalars.remove("NameHere")

        type: "ConditionType"
        for type in Enum.GetValues(clr.TypeOf(ConditionType)):
            if provider.conditions.factory.is_type_supported(type):
                obj: "ICalculationToolCondition" = provider.conditions.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.conditions.remove("NameHere")

        type: "ParameterSetType"
        for type in Enum.GetValues(clr.TypeOf(ParameterSetType)):
            if provider.parameter_sets.factory.is_type_supported(type):
                obj: "ICalculationToolParameterSet" = provider.parameter_sets.factory.create("NameHere", "", type)
                Assert.assertIsNotNone(obj)
                provider.parameter_sets.remove("NameHere")

        type: "VolumeGridType"
        for type in Enum.GetValues(clr.TypeOf(VolumeGridType)):
            pass

        access.save_computed_data = True
        Assert.assertTrue(access.save_computed_data)
        access.save_computed_data = False
        Assert.assertFalse(access.save_computed_data)

        access.clear_access()
        access.remove_access()

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        access: "Access" = (IStkObject(EarlyBoundTests._satellite)).get_access("Facility/Facility1")
        oGraphics: "AccessGraphics" = access.graphics
        Assert.assertIsNotNone(oGraphics)
        # Inherit (true)
        TestBase.logger.WriteLine4("\tThe current Inherit is: {0}", oGraphics.inherit)
        oGraphics.inherit = True
        TestBase.logger.WriteLine4("\tThe new Inherit is: {0}", oGraphics.inherit)
        Assert.assertTrue(oGraphics.inherit)
        # AnimateGfx (readonly)
        with pytest.raises(Exception):
            oGraphics.show_animation_highlight_graphics_2d = True
        # LineVisible (readonly)
        with pytest.raises(Exception):
            oGraphics.show_line = True
        # StaticGfx (readonly)
        with pytest.raises(Exception):
            oGraphics.static_graphics_2d = True
        # Inherit (false)
        oGraphics.inherit = False
        TestBase.logger.WriteLine4("\tThe new Inherit is: {0}", oGraphics.inherit)
        Assert.assertFalse(oGraphics.inherit)
        # AnimateGfx
        TestBase.logger.WriteLine4("\tThe current AnimateGfx is: {0}", oGraphics.show_animation_highlight_graphics_2d)
        oGraphics.show_animation_highlight_graphics_2d = True
        TestBase.logger.WriteLine4("\tThe new AnimateGfx is: {0}", oGraphics.show_animation_highlight_graphics_2d)
        Assert.assertTrue(oGraphics.show_animation_highlight_graphics_2d)
        oGraphics.show_animation_highlight_graphics_2d = False
        TestBase.logger.WriteLine4("\tThe new AnimateGfx is: {0}", oGraphics.show_animation_highlight_graphics_2d)
        Assert.assertFalse(oGraphics.show_animation_highlight_graphics_2d)
        # LineVisible
        TestBase.logger.WriteLine4("\tThe current LineVisible is: {0}", oGraphics.show_line)
        oGraphics.show_line = True
        TestBase.logger.WriteLine4("\tThe new LineVisible is: {0}", oGraphics.show_line)
        Assert.assertTrue(oGraphics.show_line)
        oGraphics.show_line = False
        TestBase.logger.WriteLine4("\tThe new LineVisible is: {0}", oGraphics.show_line)
        Assert.assertFalse(oGraphics.show_line)
        # StaticGfx
        TestBase.logger.WriteLine4("\tThe current StaticGfx is: {0}", oGraphics.static_graphics_2d)
        oGraphics.static_graphics_2d = True
        TestBase.logger.WriteLine4("\tThe new StaticGfx is: {0}", oGraphics.static_graphics_2d)
        Assert.assertTrue(oGraphics.static_graphics_2d)
        oGraphics.static_graphics_2d = False
        TestBase.logger.WriteLine4("\tThe new StaticGfx is: {0}", oGraphics.static_graphics_2d)
        Assert.assertFalse(oGraphics.static_graphics_2d)

    # endregion

    # region DataDisplays
    @category("VO Tests")
    def test_DataDisplays(self):
        access: "Access" = (IStkObject(EarlyBoundTests._satellite)).get_access("Facility/Facility1")
        access.compute_access()
        oDDHelper = VODataDisplayHelper(clr.CastAs(TestBase.Application, StkObjectRoot))
        oDDHelper.Run(access.data_displays, True, False)
        access.remove_access()

    # endregion

    # region BasicComputingAccess
    @category("Basic Tests")
    def test_BasicComputingAccess(self):
        TestBase.logger.WriteLine("----- THE (early bound) BASIC COMPUTE ACCESS TEST ----- BEGIN -----")

        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        Assert.assertIsNotNone(oFacility)
        # compute access
        oAccess: "Access" = (IStkObject(EarlyBoundTests._satellite)).get_access_to_object(oFacility)
        Assert.assertIsNotNone(oAccess)
        oAccess.advanced.enable_light_time_delay = False
        oAccess.advanced.use_fixed_time_step = True  # change to test config persistence
        oAccess.advanced.fixed_step_size = (
            100.0  # don't take too large a step to miss the accesses when computed this way
        )
        oAccess.advanced.use_precise_event_times = False  # change to test config persistence
        oAccess.compute_access()
        Assert.assertEqual(4, oAccess.computed_access_interval_times.count)

        # Clear Access, then re-Compute
        oAccess.clear_access()
        Assert.assertEqual(0, oAccess.computed_access_interval_times.count)
        oAccess.compute_access()
        Assert.assertEqual(4, oAccess.computed_access_interval_times.count)

        # ensure that access config is retained
        Assert.assertFalse(oAccess.advanced.enable_light_time_delay)
        Assert.assertTrue(oAccess.advanced.use_fixed_time_step)
        Assert.assertFalse(oAccess.advanced.use_precise_event_times)

        # reset properties to default, and re-Compute
        oAccess.advanced.use_fixed_time_step = False  # set back to default
        oAccess.advanced.use_precise_event_times = True  # set back to default
        oAccess.compute_access()

        # get result report
        oDPCollection: "DataProviderCollection" = oAccess.data_providers
        Assert.assertIsNotNone(oDPCollection)
        TestBase.logger.WriteLine3("\tAvailable: {0} Data Providers.", oDPCollection.count)
        # get data provider info
        oDPInfo: "IDataProviderInfo" = oDPCollection["Access Data"]
        Assert.assertIsNotNone(oDPInfo)
        TestBase.logger.WriteLine8(
            "\tName: {0}, Type = {1}, IsGroup = {2}", oDPInfo.name, oDPInfo.type, oDPInfo.is_group()
        )
        Assert.assertEqual("Access Data", oDPInfo.name)
        Assert.assertEqual(DataProviderType.INTERVAL, oDPInfo.type)
        Assert.assertFalse(oDPInfo.is_group())
        #
        oProvider: "IDataProvider" = clr.CastAs(oDPInfo, IDataProvider)
        Assert.assertIsNotNone(oProvider)
        # Exec data provider
        oDPInterval: "DataProviderInterval" = clr.CastAs(oDPInfo, DataProviderInterval)
        Assert.assertIsNotNone(oDPInterval)
        dtStart: typing.Any = "1 Jul 1999 00:00:00.00"
        dtStop: typing.Any = "2 Jul 1999 00:00:00.00"
        arFields = ["Start Time", "Stop Time", "Duration"]

        oResult1: "DataProviderResult" = oDPInterval.execute_elements(dtStart, dtStop, arFields)
        Assert.assertIsNotNone(oResult1)

        oNewAccess: "Access" = oFacility.get_access_to_object(clr.CastAs(EarlyBoundTests._satellite, IStkObject))
        Assert.assertIsNotNone(oNewAccess)
        oNewAccess.advanced.enable_light_time_delay = False
        dtStart = "1 Jul 1999 15:20:00.000"
        dtStop = "1 Jul 1999 17:29:00.000"
        oNewAccess.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        oNewAccess.specify_access_time_period(dtStart, dtStop)
        oNewAccess.compute_access()
        # get result report
        oDPCollection = oNewAccess.data_providers
        Assert.assertIsNotNone(oDPCollection)
        TestBase.logger.WriteLine3("\tAvailable: {0} Data Providers.", oDPCollection.count)
        # get data provider info
        oDPInfo = oDPCollection["Access Data"]
        Assert.assertIsNotNone(oDPInfo)
        TestBase.logger.WriteLine8(
            "\tName: {0}, Type = {1}, IsGroup = {2}", oDPInfo.name, oDPInfo.type, oDPInfo.is_group()
        )
        Assert.assertEqual("Access Data", oDPInfo.name)
        Assert.assertEqual(DataProviderType.INTERVAL, oDPInfo.type)
        Assert.assertFalse(oDPInfo.is_group())
        #
        oProvider = clr.CastAs(oDPInfo, IDataProvider)
        Assert.assertIsNotNone(oProvider)
        # Exec data provider
        oDPInterval = clr.CastAs(oDPInfo, DataProviderInterval)
        Assert.assertIsNotNone(oDPInterval)
        dtStart = "1 Jul 1999 00:00:00.00"
        dtStop = "2 Jul 1999 00:00:00.00"
        oResult2: "DataProviderResult" = oDPInterval.execute_elements(dtStart, dtStop, arFields)
        Assert.assertIsNotNone(oResult2)
        # compare reports
        oDataSets1: "DataProviderResultDataSetCollection" = oResult1.data_sets
        Assert.assertIsNotNone(oDataSets1)
        oDataSets2: "DataProviderResultDataSetCollection" = oResult2.data_sets
        Assert.assertIsNotNone(oDataSets2)

        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        # StartTime
        arValues1 = oDataSets1[0].get_values()
        arValues2 = oDataSets2[0].get_values()
        Assert.assertEqual(4, Array.Length(arValues1))
        Assert.assertEqual(2, Array.Length(arValues2))

        Assert.assertEqual(55293.76, Math.Round(float(arValues1[1]), 3))

        TestBase.logger.WriteLine6("StartTime {0}", arValues1[1])
        Assert.assertAlmostEqual(float(arValues1[1]), float(arValues2[0]), delta=0.01)
        Assert.assertAlmostEqual(float(arValues1[2]), float(arValues2[1]), delta=0.01)

        # StopTime
        arValues1 = oDataSets1[1].get_values()
        arValues2 = oDataSets2[1].get_values()
        TestBase.logger.WriteLine6("StopTime {0}", arValues1[1])

        Assert.assertEqual(55691.898, Math.Round(float(arValues1[1]), 3))

        Assert.assertEqual(4, Array.Length(arValues1))
        Assert.assertEqual(2, Array.Length(arValues2))
        Assert.assertAlmostEqual(float(arValues1[1]), float(arValues2[0]), delta=0.01)
        Assert.assertAlmostEqual(float(arValues1[2]), float(arValues2[1]), delta=0.01)

        # Duration
        arValues1 = oDataSets1[2].get_values()
        arValues2 = oDataSets2[2].get_values()
        Assert.assertEqual(4, Array.Length(arValues1))
        Assert.assertEqual(2, Array.Length(arValues2))
        TestBase.logger.WriteLine6("Duration {0}", arValues1[1])

        Assert.assertAlmostEqual(398.13, float(arValues1[1]), delta=0.01)

        Assert.assertAlmostEqual(float(arValues1[1]), float(arValues2[0]), delta=0.01)
        Assert.assertAlmostEqual(float(arValues1[2]), float(arValues2[1]), delta=0.01)

        oNewAccess.remove_access()
        TestBase.Application.units_preferences.reset_units()
        TestBase.logger.WriteLine("----- THE BASIC COMPUTE ACCESS TEST ----- END -----")

    # endregion

    # region TimePeriod
    def test_TimePeriod(self):
        TestBase.logger.WriteLine("----- THE TIME PERIOD TEST ----- BEGIN -----")

        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Test")
        date: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", "1 Jul 2007 00:00:00.000")
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        scene.set_time_period(date.format("UTCG"), "+1 day")

        oSatellite: "Satellite" = Satellite(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "Spy")
        )
        oFacility: "Facility" = Facility(
            TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Facility1")
        )
        Assert.assertIsNotNone(oSatellite)

        oPropagator: "PropagatorTwoBody" = PropagatorTwoBody(oSatellite.propagator)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.propagate()

        access: "Access" = (IStkObject(oSatellite)).get_access("Facility/Facility1")
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        accessTimePeriod: "AccessTimePeriod" = clr.CastAs(access.access_time_period_data, AccessTimePeriod)
        tp: "ITimePeriod" = clr.CastAs(access.access_time_period_data, ITimePeriod)
        Assert.assertIsNotNone(tp)

        Assert.assertEqual(scene.start_time, tp.start_time.value)
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)

        Assert.assertEqual(scene.stop_time, tp.stop_time.value)
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.stop_time.type)

        accessTimePeriod.start_time.type = TimePeriodValueType.SPECIFY
        Assert.assertEqual(TimePeriodValueType.SPECIFY, accessTimePeriod.start_time.type)
        accessTimePeriod.start_time.type = TimePeriodValueType.TODAY
        Assert.assertEqual(TimePeriodValueType.TODAY, accessTimePeriod.start_time.type)
        accessTimePeriod.start_time.type = TimePeriodValueType.TOMORROW
        Assert.assertEqual(TimePeriodValueType.TOMORROW, accessTimePeriod.start_time.type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            accessTimePeriod.start_time.type = TimePeriodValueType.DURATION

        accessTimePeriod.stop_time.type = TimePeriodValueType.SPECIFY
        Assert.assertEqual(TimePeriodValueType.SPECIFY, accessTimePeriod.stop_time.type)
        accessTimePeriod.stop_time.type = TimePeriodValueType.TODAY  # result: Specify
        Assert.assertEqual(TimePeriodValueType.TODAY, accessTimePeriod.stop_time.type)
        accessTimePeriod.stop_time.type = TimePeriodValueType.TOMORROW  # result: Specify
        Assert.assertEqual(TimePeriodValueType.TOMORROW, accessTimePeriod.stop_time.type)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            accessTimePeriod.stop_time.type = TimePeriodValueType.DURATION

        # testing the access's start time

        scene.set_time_period("Today", "+2 day")
        tp.start_time.type = TimePeriodValueType.TODAY
        Assert.assertEqual(TimePeriodValueType.TODAY, tp.start_time.type)
        Assert.assertNotEqual("Today", tp.start_time.value)
        TestBase.logger.WriteLine2(tp.start_time.value)

        tp.start_time.type = TimePeriodValueType.TOMORROW
        Assert.assertEqual(TimePeriodValueType.TOMORROW, tp.start_time.type)
        Assert.assertNotEqual("Tomorrow", tp.start_time.value)
        TestBase.logger.WriteLine2(tp.start_time.value)

        tp.start_time.type = TimePeriodValueType.SPECIFY
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            tp.start_time.type = TimePeriodValueType.DURATION

        # reset the start time
        scene.set_time_period(date.format("UTCG"), "+1 day")
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        tp.start_time.value = scene.start_time
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.start_time.type)

        # cannot cast to -1 in Java
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            tp.start_time.type = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid value")):
            tp.start_time.value = ""

        # ** Test the access's stop time
        scene.set_time_period("Today", "+1 day")
        tp.stop_time.type = TimePeriodValueType.TODAY
        Assert.assertEqual(TimePeriodValueType.TODAY, tp.stop_time.type)
        Assert.assertNotEqual("Today", tp.stop_time.value)

        date.set_date("UTCG", "Tomorrow")
        date = date.add("day", 1)
        scene.stop_time = date.format("UTCG")
        tp.stop_time.type = TimePeriodValueType.TOMORROW
        Assert.assertEqual(TimePeriodValueType.TOMORROW, tp.stop_time.type)
        Assert.assertNotEqual("Tomorrow", tp.stop_time.value)

        tp.stop_time.type = TimePeriodValueType.SPECIFY
        Assert.assertEqual(TimePeriodValueType.SPECIFY, tp.stop_time.type)
        hold: typing.Any = tp.stop_time.value
        tp.stop_time.value = tp.start_time.value
        Assert.assertEqual(tp.start_time.value, tp.stop_time.value)
        tp.stop_time.value = hold

        # cannot cast to -1 in Java
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            tp.stop_time.type = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid value")):
            tp.stop_time.value = ""
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            tp.stop_time.type = TimePeriodValueType.DURATION

        # ** Testing scenario's duration
        tp.duration = "+1 sec"
        Assert.assertEqual("+1 sec", tp.duration)
        Assert.assertEqual(TimePeriodValueType.DURATION, tp.stop_time.type)

        oStartDate: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.start_time.value))
        oStopDate: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.stop_time.value))
        oDateSpan: "Quantity" = oStopDate.span(oStartDate)
        Assert.assertEqual(1, oDateSpan.value)

        tp.duration = "+1 day"
        Assert.assertEqual("+1 day", tp.duration)
        Assert.assertEqual(TimePeriodValueType.DURATION, tp.stop_time.type)

        oStartDate = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.start_time.value))
        oStopDate = TestBase.Application.conversion_utility.new_date("UTCG", str(tp.stop_time.value))
        oDateSpan = oStopDate.span(oStartDate)
        Assert.assertEqual(86400, oDateSpan.value)

    # endregion

    # region ComputeWithIntervals
    def test_ComputeWithIntervals(self):
        access: "Access" = (IStkObject(EarlyBoundTests._satellite)).get_access("Facility/Facility1")
        access.advanced.use_precise_event_times = True
        access.advanced.time_convergence = 0.0002
        access.compute_access()
        intervals: "TimeIntervalCollection" = access.computed_access_interval_times
        accessTimes = intervals.to_array(0, -1)
        Assert.assertEqual(4, len(accessTimes))

        Assert.assertEqual("1 Jul 1999 13:48:08.041", accessTimes[0][0])
        Assert.assertEqual("1 Jul 1999 13:51:28.342", accessTimes[0][1])
        Assert.assertEqual("1 Jul 1999 15:21:33.757", accessTimes[1][0])
        Assert.assertEqual("1 Jul 1999 15:28:11.903", accessTimes[1][1])
        Assert.assertEqual("1 Jul 1999 16:56:36.506", accessTimes[2][0])
        Assert.assertEqual("1 Jul 1999 17:03:29.482", accessTimes[2][1])
        Assert.assertEqual("1 Jul 1999 18:32:43.597", accessTimes[3][0])
        Assert.assertEqual("1 Jul 1999 18:37:36.101", accessTimes[3][1])

        access.remove_access()

        accessTimes[0][0] = "1 Jul 1999 13:48:00.000"
        access = (IStkObject(EarlyBoundTests._satellite)).get_access("Facility/Facility1")
        access.advanced.use_precise_event_times = True
        access.advanced.time_convergence = 0.0002
        access.specify_access_intervals(accessTimes)
        access.compute_access()
        accessTimes = access.computed_access_interval_times.to_array(0, -1)

        Assert.assertEqual("1 Jul 1999 13:48:08.041", accessTimes[0][0])
        Assert.assertEqual("1 Jul 1999 13:51:28.342", accessTimes[0][1])
        Assert.assertEqual("1 Jul 1999 15:21:33.757", accessTimes[1][0])
        Assert.assertEqual("1 Jul 1999 15:28:11.903", accessTimes[1][1])
        Assert.assertEqual("1 Jul 1999 16:56:36.506", accessTimes[2][0])
        Assert.assertEqual("1 Jul 1999 17:03:29.482", accessTimes[2][1])
        Assert.assertEqual("1 Jul 1999 18:32:43.598", accessTimes[3][0])
        Assert.assertEqual("1 Jul 1999 18:37:36.101", accessTimes[3][1])

        access.remove_access()

        accessTimes[0][0] = "1 Jul 1999 13:49:00.000"
        access = (IStkObject(EarlyBoundTests._satellite)).get_access("Facility/Facility1")
        access.advanced.use_precise_event_times = True
        access.advanced.time_convergence = 0.0002
        access.specify_access_intervals(accessTimes)
        access.compute_access()
        accessTimes = access.computed_access_interval_times.to_array(0, -1)
        Assert.assertEqual("1 Jul 1999 13:49:00.000", accessTimes[0][0])

        Assert.assertEqual("1 Jul 1999 13:49:00.000", accessTimes[0][0])
        Assert.assertEqual("1 Jul 1999 13:51:28.342", accessTimes[0][1])
        Assert.assertEqual("1 Jul 1999 15:21:33.757", accessTimes[1][0])
        Assert.assertEqual("1 Jul 1999 15:28:11.903", accessTimes[1][1])
        Assert.assertEqual("1 Jul 1999 16:56:36.506", accessTimes[2][0])
        Assert.assertEqual("1 Jul 1999 17:03:29.482", accessTimes[2][1])
        Assert.assertEqual("1 Jul 1999 18:32:43.598", accessTimes[3][0])
        Assert.assertEqual("1 Jul 1999 18:37:36.101", accessTimes[3][1])

        access.remove_access()

    # endregion

    # region SpecifyAccessTimePeriod
    def test_SpecifyAccessTimePeriod(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Test55961")

        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        scene.start_time = "17 Feb 2010 05:00:00.000"
        scene.stop_time = "17 Feb 2010 06:00:00.000"

        # Reset the scenario's epoch to the value that allows the test to pass
        # with as few modifications as possible.
        scene.epoch = "1 Jul 1999 00:00:00.000"

        oFacility: "Facility" = Facility(
            TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "GB2Y")
        )
        oFacility.position.assign_geodetic(26.6255, -78.2985, -0.010997)

        oSatellite: "Satellite" = Satellite(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite1")
        )
        oSatellite.set_propagator_type(PropagatorType.J4_PERTURBATION)
        j4: "PropagatorJ4Perturbation" = clr.CastAs(oSatellite.propagator, PropagatorJ4Perturbation)

        classical: "OrbitStateClassical" = OrbitStateClassical(
            j4.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sma: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sma.semi_major_axis = 6878.14
        sma.eccentricity = 3.70942e-16
        classical.orientation.inclination = 45
        classical.orientation.ascending_node_type = OrientationAscNode.LONGITUDE_ASCENDING_NODE
        (clr.CastAs(classical.orientation.ascending_node, OrientationLongitudeOfAscending)).value = 0

        j4.initial_state.representation.assign(classical)
        j4.propagate()

        myAccess: "Access" = (IStkObject(oFacility)).get_access_to_object(IStkObject(oSatellite))
        myAccess.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD  # 2
        myAccess.specify_access_time_period("17 Feb 2010 05:34:09.161", "17 Feb 2010 05:41:01.680")
        myAccess.compute_access()

        intColl: "TimeIntervalCollection" = myAccess.computed_access_interval_times
        Assert.assertEqual(1, intColl.count)

        pStart: typing.Any = None
        pStop: typing.Any = None

        (pStart, pStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(intColl, 0)
        Assert.assertEqual("17 Feb 2010 05:34:09.161", pStart)
        Assert.assertEqual("17 Feb 2010 05:41:01.680", pStop)

        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("AccessTests", "AccessTests.sc"))

    # endregion

    def test_SignalSenseOfClockHostThrowsExceptionWhenReadOnly(self):
        def code1():
            access: "Access" = (IStkObject(EarlyBoundTests._satellite)).get_access("Facility/Facility1")
            advanced: "AccessAdvancedSettings" = access.advanced

            advanced.use_default_clock_host_and_signal_sense = True
            Assert.assertTrue(advanced.use_default_clock_host_and_signal_sense)

            advanced.signal_sense_of_clock_host = IvTimeSense.RECEIVE

        ExceptionAssert.Throws(code1)

    # region BUG107492
    def test_Bug107492Test(self):
        root: "StkObjectRoot" = clr.CastAs(TestBase.Application, StkObjectRoot)
        try:
            # Create a place and a satellite
            place: "Place" = clr.CastAs(
                root.current_scenario.children.new(STKObjectType.PLACE, "PlaceBug107492"), Place
            )
            satellite: "Satellite" = clr.CastAs(
                root.current_scenario.children.new(STKObjectType.SATELLITE, "SatelliteBug107492"), Satellite
            )
            (PropagatorTwoBody(satellite.propagator)).propagate()

            # Force the creation of the PlaceBug107492-to-SatelliteBug107492 access object with an allocated step control data
            root.execute_command("Access */Place/PlaceBug107492 */Satellite/SatelliteBug107492 FixedSampleStep 0.1")

            # Create an object model access that duplicates the access request but before the fix
            # pointed to the same step control data
            access1: "Access" = (IStkObject(place)).get_access_to_object(IStkObject(satellite))
            del access1  # the common step control data is deleted here

            # Create a second object model access that duplicates the access request and
            # before the fix pointed to the deleted step control data
            access2: "Access" = (IStkObject(place)).get_access_to_object(IStkObject(satellite))

            # Before the fix assertion on the next line in debug when running in the debugger
            # [HEAP[nunit3-console.exe]: Invalid address specified to RtlValidateHeap]
            del access2

        finally:
            # Clean-up the objects created for this test
            root.current_scenario.children.unload(STKObjectType.PLACE, "PlaceBug107492")
            root.current_scenario.children.unload(STKObjectType.SATELLITE, "SatelliteBug107492")

    # endregion

    # region ZZZ_OnePointAccess_FirstSatisfaction
    def test_ZZZ_OnePointAccess_FirstSatisfaction(self):
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(TestBase.GetScenarioFile("SuperAccess", "AllSensors.sc"))

        objSat: "IStkObject" = TestBase.Application.current_scenario.children["AllSenSat"]
        onePtAccess: "OnePointAccess" = objSat.create_one_point_access("Satellite/GEO/Sensor/SpinRect")

        # OnePointAccess */Satellite/AllSenSat */Satellite/GEO/Sensor/SpinRect FirstSatisfaction "01 Jan 1997 00:00:00" "01 Jan 1997 04:00:00" 1 3.0
        # returns:  1 Jan 1997 01:05:12.375 1 Jan 1997 01:05:15.563
        intColl: "TimeIntervalCollectionReadOnly" = onePtAccess.compute_first_satisfaction(
            "1 Jan 1997 01:05:00.000", "1 Jan 1997 01:20:00.000", 1, 3.0
        )

        start: typing.Any = None
        stop: typing.Any = None

        (start, stop) = IntervalCollectionExtensionMethods.GetIntervalHelper2(intColl, 0)
        Assert.assertEqual("1 Jan 1997 01:05:12.375", start)
        Assert.assertEqual("1 Jan 1997 01:05:15.563", stop)

        # OnePointAccess */Satellite/AllSenSat */Satellite/GEO/Sensor/SpinRect FirstSatisfaction "01 Jan 1997 01:05:00" "01 Jan 1997 01:20:00" 3 2.0
        # returns:
        # I Return entry 1:
        # I 1     1 Jan 1997 01:05:00.484 1 Jan 1997 01:05:03.104         2.620
        # I Return entry 2:
        # I 2     1 Jan 1997 01:05:06.433 1 Jan 1997 01:05:09.311         2.878
        # I Return entry 3:
        # I 3     1 Jan 1997 01:05:12.375 1 Jan 1997 01:05:15.563         3.188
        intColl = onePtAccess.compute_first_satisfaction("1 Jan 1997 01:05:00.000", "1 Jan 1997 01:20:00.000", 3, 2.0)
        Assert.assertEqual(3, intColl.count)
        (start, stop) = IntervalCollectionExtensionMethods.GetIntervalHelper2(intColl, 0)
        Assert.assertEqual("1 Jan 1997 01:05:00.484", start)
        Assert.assertEqual("1 Jan 1997 01:05:03.104", stop)
        (start, stop) = IntervalCollectionExtensionMethods.GetIntervalHelper2(intColl, 1)
        Assert.assertEqual("1 Jan 1997 01:05:06.433", start)
        Assert.assertEqual("1 Jan 1997 01:05:09.311", stop)
        (start, stop) = IntervalCollectionExtensionMethods.GetIntervalHelper2(intColl, 2)
        Assert.assertEqual("1 Jan 1997 01:05:12.375", start)
        Assert.assertEqual("1 Jan 1997 01:05:15.563", stop)

    # endregion

    # ----------------------------------------------------------------

    # region DP_PreData_Unit
    def test_DP_PreData_Unit(self):
        holdDateFormat: str = TestBase.Application.units_preferences.get_current_unit_abbrv("DateFormat")
        placeObj: "IStkObject" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.PLACE, "PlacePreDataTest"), IStkObject
        )
        satelliteObj: "IStkObject" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "SatellitePreDataTest"),
            IStkObject,
        )

        try:
            TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")

            scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
            rFEnvironment: "RFEnvironment" = clr.CastAs(scenario.rf_environment, RFEnvironment)
            propagationChannel: "PropagationChannel" = clr.CastAs(rFEnvironment.propagation_channel, PropagationChannel)
            propagationChannel.enable_atmospheric_absorption = True
            propagationChannel.set_atmospheric_absorption_model("VOACAP")
            satellite: "Satellite" = clr.CastAs(satelliteObj, Satellite)
            satellite.set_propagator_type(PropagatorType.TWO_BODY)
            satelliteProp: "PropagatorTwoBody" = clr.CastAs(satellite.propagator, PropagatorTwoBody)
            satelliteProp.propagate()

            radarObj: "IStkObject" = clr.CastAs(
                satelliteObj.children.new(STKObjectType.RADAR, "RadarPreDataTest"), IStkObject
            )
            accessObj: "Access" = clr.CastAs(radarObj.get_access(placeObj.path), Access)

            dp: "IDataProvider" = clr.CastAs(accessObj.data_providers["Radar VOACAP Files"], IDataProvider)
            dpFixed: "DataProviderFixed" = clr.CastAs(dp, DataProviderFixed)
            dp.pre_data = "Time '61200' SaveFilesToScenario true"
            result: "DataProviderResult" = dpFixed.execute()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "BogusTime '61200' SaveFilesToScenario true"
            result = dpFixed.execute()
            Assert.assertEqual("Data Unavailable", str(result.message.messages[0]))

            transmitterObj: "IStkObject" = clr.CastAs(
                satelliteObj.children.new(STKObjectType.TRANSMITTER, "TransmitterPreDataTest"), IStkObject
            )
            receiverObj: "IStkObject" = clr.CastAs(
                placeObj.children.new(STKObjectType.RECEIVER, "ReceiverPreDataTest"), IStkObject
            )
            accessObj: "Access" = clr.CastAs(transmitterObj.get_access(receiverObj.path), Access)

            dp: "IDataProvider" = clr.CastAs(accessObj.data_providers["Comm VOACAP Files"], IDataProvider)
            dpFixed: "DataProviderFixed" = clr.CastAs(dp, DataProviderFixed)
            dp.pre_data = "Time '61200' SaveFilesToScenario true"
            result: "DataProviderResult" = dpFixed.execute()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "BogusTime '61200' SaveFilesToScenario true"
            result = dpFixed.execute()
            Assert.assertEqual("Data Unavailable", str(result.message.messages[0]))

        finally:
            TestBase.Application.units_preferences.set_current_unit("DateFormat", holdDateFormat)
            TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "SatellitePreDataTest")
            TestBase.Application.current_scenario.children.unload(STKObjectType.PLACE, "PlacePreDataTest")

    # endregion
