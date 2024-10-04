import pytest
from test_util import *
from assertion_harness import *
from compatibility.interval_collection_extension_methods import *
from logger import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class BugFixes(TestBase):
    def __init__(self, *args, **kwargs):
        super(BugFixes, self).__init__(*args, **kwargs)

    # region Members
    satellite: "Satellite" = None
    facility: "Facility" = None
    _verbose: bool = False
    # endregion

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        BugFixes.InitHelper()

    @staticmethod
    def InitHelper():
        TestBase.LoadTestScenario(Path.Combine("AccessTests", "AccessTests.sc"))

        BugFixes.satellite = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "AccessBugFixesSat")
        )
        oPropagator: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(BugFixes.satellite.propagator)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.propagate()

        BugFixes.facility = Facility(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "AccessBugFixesFac")
        )
        BugFixes.facility.position.assign_geodetic(26.6255, -78.2985, -0.010997)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        TestBase.Uninitialize()

    # endregion

    def test_BUG61422(self):
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        scene.set_time_period("17 Feb 2010 05:00:00.000", "18 Feb 2010 05:00:00.000")

        myAccess: "StkAccess" = (IStkObject(BugFixes.satellite)).get_access_to_object(IStkObject(BugFixes.facility))
        myAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME

        # these intervals were chosen to be in the inerior of the first access interval if computed using object times
        myAccess.specify_access_time_period("17 Feb 2010 06:13:49.789", "17 Feb 2010 06:17:59.678")
        myAccess.compute_access()

        intColl: "IntervalCollection" = myAccess.computed_access_interval_times
        Assert.assertEqual(1, intColl.count)

        pStart: typing.Any = None
        pStop: typing.Any = None

        (pStart, pStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(intColl, 0)
        Assert.assertEqual("17 Feb 2010 06:13:49.789", pStart)
        Assert.assertEqual("17 Feb 2010 06:17:59.678", pStop)

    @category("Graphics Tests")
    def test_BUG72385(self):
        BugFixes.InitHelper()

        fac: "Facility" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac72385"), Facility
        )
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat72385"), Satellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "VehiclePropagatorTwoBody" = clr.CastAs(sat.propagator, VehiclePropagatorTwoBody)
        twoBody.propagate()
        satObj: "IStkObject" = clr.CastAs(sat, IStkObject)
        access: "StkAccess" = satObj.get_access_to_object(clr.CastAs(fac, IStkObject))

        sat.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM)
        custom: "VehicleGraphics2DAttributesCustom" = clr.CastAs(
            sat.graphics.attributes, VehicleGraphics2DAttributesCustom
        )
        custom.intervals.add("1 Jul 1999 13:00:00.000", "1 Jul 1999 14:30:00.000")
        custom.intervals.add("1 Jul 1999 14:00:00.000", "1 Jul 1999 15:30:00.000")
        custom.intervals.add("1 Jul 1999 15:00:00.000", "1 Jul 1999 16:00:00.000")

        access.compute_access()
        intervals: "IntervalCollection" = access.computed_access_interval_times
        accessTimes = intervals.to_array(0, -1)
        Assert.assertEqual(4, len(accessTimes))
        Assert.assertEqual("1 Jul 1999 13:48:07.978", accessTimes[0][0])
        Assert.assertEqual("1 Jul 1999 13:51:28.353", accessTimes[0][1])
        Assert.assertEqual("1 Jul 1999 15:21:33.719", accessTimes[1][0])
        Assert.assertEqual("1 Jul 1999 15:28:11.894", accessTimes[1][1])
        Assert.assertEqual("1 Jul 1999 16:56:36.471", accessTimes[2][0])
        Assert.assertEqual("1 Jul 1999 17:03:29.482", accessTimes[2][1])
        Assert.assertEqual("1 Jul 1999 18:32:43.541", accessTimes[3][0])
        Assert.assertEqual("1 Jul 1999 18:37:36.132", accessTimes[3][1])

        custom.deconflict()

        access.compute_access()
        intervals = access.computed_access_interval_times
        accessTimes = intervals.to_array(0, -1)
        Assert.assertEqual(4, len(accessTimes))
        Assert.assertEqual("1 Jul 1999 13:48:07.978", accessTimes[0][0])
        Assert.assertEqual("1 Jul 1999 13:51:28.353", accessTimes[0][1])
        Assert.assertEqual("1 Jul 1999 15:21:33.719", accessTimes[1][0])
        Assert.assertEqual("1 Jul 1999 15:28:11.894", accessTimes[1][1])
        Assert.assertEqual("1 Jul 1999 16:56:36.471", accessTimes[2][0])
        Assert.assertEqual("1 Jul 1999 17:03:29.482", accessTimes[2][1])
        Assert.assertEqual("1 Jul 1999 18:32:43.541", accessTimes[3][0])
        Assert.assertEqual("1 Jul 1999 18:37:36.132", accessTimes[3][1])

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "fac72385")
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat72385")

    @category("VO Tests")
    def test_BUG68749_and_BUG75680_Axes_AvailableAxes(self):
        access: "StkAccess" = (clr.CastAs(BugFixes.satellite, IStkObject)).get_access_to_object(
            (clr.CastAs(BugFixes.facility, IStkObject))
        )
        access.compute_access()

        axes: "Graphics3DReferenceVectorGeometryToolAxes" = clr.CastAs(
            BugFixes.satellite.graphics_3d.vector.reference_crdns.get_crdn_by_name(
                GEOMETRIC_ELEM_TYPE.AXES_ELEM, "Satellite/AccessBugFixesSat Body Axes"
            ),
            Graphics3DReferenceVectorGeometryToolAxes,
        )
        (clr.CastAs(axes, IGraphics3DReferenceAnalysisWorkbenchComponent)).visible = True

        found: bool = False
        axesName: str = "Access/Satellite-AccessBugFixesSat-To-Facility-AccessBugFixesFac FromObjectBody Axes"
        avail: str
        for avail in axes.available_axes:
            if avail == axesName:
                found = True
                break

        Assert.assertTrue(found, "axesName not found")
        axes.axes = axesName
        Assert.assertEqual(axesName, axes.axes)

        access.remove_access()

    @category("VO Tests")
    def test_BUG68749_and_BUG75680_Axes_AvailablePoints(self):
        pass

    @category("VO Tests")
    def test_BUG68749_and_BUG75680_Vector_AvailableAxes(self):
        access: "StkAccess" = (clr.CastAs(BugFixes.satellite, IStkObject)).get_access_to_object(
            (clr.CastAs(BugFixes.facility, IStkObject))
        )
        access.compute_access()

        vector: "Graphics3DReferenceVectorGeometryToolVector" = clr.CastAs(
            BugFixes.satellite.graphics_3d.vector.reference_crdns.get_crdn_by_name(
                GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/AccessBugFixesSat Sun Vector"
            ),
            Graphics3DReferenceVectorGeometryToolVector,
        )
        (clr.CastAs(vector, IGraphics3DReferenceAnalysisWorkbenchComponent)).visible = True

        found: bool = False
        axesName: str = "Access/Satellite-AccessBugFixesSat-To-Facility-AccessBugFixesFac FromObjectBody Axes"
        avail: str
        for avail in vector.available_axes:
            if avail == axesName:
                found = True
                break

        Assert.assertTrue(found, "axesName not found")
        vector.axes = axesName
        Assert.assertEqual(axesName, vector.axes)

        access.remove_access()

    @category("VO Tests")
    def test_BUG68749_and_BUG75680_Vector_AvailablePoints(self):
        access: "StkAccess" = (clr.CastAs(BugFixes.satellite, IStkObject)).get_access_to_object(
            (clr.CastAs(BugFixes.facility, IStkObject))
        )
        access.compute_access()

        vector: "Graphics3DReferenceVectorGeometryToolVector" = clr.CastAs(
            BugFixes.satellite.graphics_3d.vector.reference_crdns.get_crdn_by_name(
                GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/AccessBugFixesSat Sun Vector"
            ),
            Graphics3DReferenceVectorGeometryToolVector,
        )
        (clr.CastAs(vector, IGraphics3DReferenceAnalysisWorkbenchComponent)).visible = True

        found: bool = False
        pointName: str = "Access/Satellite-AccessBugFixesSat-To-Facility-AccessBugFixesFac FromObject Point"
        avail: str
        for avail in vector.available_points:
            if avail == pointName:
                found = True
                break

        Assert.assertTrue(found, "pointName not found")
        vector.draw_at_point = True
        vector.point = pointName
        Assert.assertEqual(pointName, vector.point)

        access.remove_access()

    @category("VO Tests")
    def test_BUG68749_and_BUG75680_Point_AvailableSystems(self):
        access: "StkAccess" = (clr.CastAs(BugFixes.satellite, IStkObject)).get_access_to_object(
            (clr.CastAs(BugFixes.facility, IStkObject))
        )
        access.compute_access()

        point: "Graphics3DReferenceVectorGeometryToolPoint" = clr.CastAs(
            BugFixes.satellite.graphics_3d.vector.reference_crdns.add(
                GEOMETRIC_ELEM_TYPE.POINT_ELEM, "Satellite/AccessBugFixesSat Center Point"
            ),
            Graphics3DReferenceVectorGeometryToolPoint,
        )
        (clr.CastAs(point, IGraphics3DReferenceAnalysisWorkbenchComponent)).visible = True

        found: bool = False
        systemName: str = "Access/Satellite-AccessBugFixesSat-To-Facility-AccessBugFixesFac FromObjectBody System"
        avail: str
        for avail in point.available_systems:
            if avail == systemName:
                found = True
                break

        Assert.assertTrue(found, "systemName not found")
        point.system = systemName
        Assert.assertEqual(systemName, point.system)

        access.remove_access()

    @category("VO Tests")
    def test_BUG68749_and_BUG75680_OrbitSystems_SupportedSystems(self):
        access: "StkAccess" = (clr.CastAs(BugFixes.satellite, IStkObject)).get_access_to_object(
            (clr.CastAs(BugFixes.facility, IStkObject))
        )
        access.compute_access()

        found: bool = False
        systemName: str = "Access/Satellite-AccessBugFixesSat-To-Facility-AccessBugFixesFac FromObjectBody System"
        avail: str
        for avail in BugFixes.satellite.graphics_3d.orbit_systems.supported_systems:
            if avail == systemName:
                found = True
                break

        Assert.assertTrue(found, "systemName not found")

        before: int = BugFixes.satellite.graphics_3d.orbit_systems.count
        sysElem: "VehicleGraphics3DSystemsElement" = BugFixes.satellite.graphics_3d.orbit_systems.add(systemName)
        Assert.assertEqual((before + 1), BugFixes.satellite.graphics_3d.orbit_systems.count)
        Assert.assertIsNotNone(sysElem)
        Assert.assertEqual(systemName, sysElem.name)

        access.remove_access()

    class AgAssertEqualString(object):
        def __init__(self, desc: str, s1: str, s2: str):
            self.description: str = desc
            self.expected: str = s1
            self.actual: str = s2

        def Assert(self):
            Assert.assertEqual(self.expected, self.actual, ("Case " + self.description))

        # this operator always evaluates the rhs expression which is what we want (unlike ||)
        @staticmethod
        def BitwiseOr(lhs, rhs):
            return rhs if ((lhs == None)) else lhs

    def CompareIntervalTimes(
        self, caseInfo: str, expectedStartTime: str, expectedStopTime: str, actualStartTime: str, actualStopTime: str
    ):
        ret = None
        if expectedStartTime != actualStartTime:
            TestBase.logger.WriteLine(
                (
                    (
                        (
                            (
                                (("Interval start time mismatch in case " + caseInfo) + ": expected '")
                                + expectedStartTime
                            )
                            + "' but got '"
                        )
                        + actualStartTime
                    )
                    + "'"
                )
            )
            TestBase.logger.WriteLine("")

            ret = BugFixes.AgAssertEqualString(caseInfo, expectedStartTime, actualStartTime)

        if expectedStopTime != actualStopTime:
            TestBase.logger.WriteLine(
                (
                    (
                        (
                            ((("Interval stop time mismatch in case " + caseInfo) + ":  expected '") + expectedStopTime)
                            + "' but got '"
                        )
                        + actualStopTime
                    )
                    + "'"
                )
            )
            TestBase.logger.WriteLine("")
            if ret != None:
                ret = BugFixes.AgAssertEqualString(caseInfo, expectedStopTime, actualStopTime)

        return ret

    def test_BUG109949_HonorAccessClockAndSense(self):
        TestBase.logger.WriteLine("----- BUG110XXX_HonoExistingrAccessClockAndSense ACCESS TEST ----- BEGIN -----")

        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["CalcScalSat"]

        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        agAssert = None

        accStart: typing.Any = None
        accStop: typing.Any = None

        # these values computed from Fac to Satellite usingFac as ClockHost, Receive sense
        SatFacStartA: str = "1 Jul 1999 11:08:25.658"
        SatFacStopA: str = "1 Jul 1999 11:14:48.079"

        oAccess: "StkAccess" = oFacility.get_access_to_object(oSatellite)
        advanced: "StkAccessAdvanced" = oAccess.advanced
        advanced.enable_light_time_delay = True
        advanced.use_default_clock_host_and_signal_sense = False
        advanced.clock_host = IV_CLOCK_HOST.BASE
        advanced.signal_sense_of_clock_host = IV_TIME_SENSE.RECEIVE
        advanced.aberration_type = ABERRATION_TYPE.ANNUAL

        oAccess.compute_access()
        (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
            oAccess.computed_access_interval_times, 0
        )

        agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
            agAssert, self.CompareIntervalTimes("A", SatFacStartA, SatFacStopA, str(accStart), str(accStop))
        )

        # NOW... get another handle to this existing Access
        oAccess2: "StkAccess" = oFacility.get_access_to_object(oSatellite)
        advanced2: "StkAccessAdvanced" = oAccess2.advanced
        Assert.assertFalse(advanced2.use_default_clock_host_and_signal_sense)
        oAccess2.clear_access()

        oAccess.compute_access()
        (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
            oAccess.computed_access_interval_times, 0
        )

        # times should be the same, not the default settings which would be transmit
        agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
            agAssert, self.CompareIntervalTimes("B", SatFacStartA, SatFacStopA, str(accStart), str(accStop))
        )
        if agAssert != None:
            agAssert.Assert()

        TestBase.logger.WriteLine("----- BUG109949_HonorExistingAccessClockAndSense ACCESS TEST ----- END -----")

    def test_BUG107506_UserSpecifiedIntervals(self):
        TestBase.logger.WriteLine("----- UserSpecifiedIntervals ACCESS TEST ----- BEGIN -----")

        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oPlanet: "IStkObject" = TestBase.Application.current_scenario.children["MarsJPL"]
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["CalcScalSat"]

        oMarsSat: "IStkObject" = None
        oFacNoCon: "IStkObject" = None

        try:
            oReceiver: "IStkObject" = oSatellite.children.new(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")
            oTransmitter: "IStkObject" = oSatellite.children.new(STK_OBJECT_TYPE.TRANSMITTER, "TestTransmitter")

            accStart: typing.Any = None
            accStop: typing.Any = None

            # /////////////////////////////////////////////////////////////////////////////////////////////////////
            # /////////////////////////////////////////////////////////////////////////////////////////////////////
            SatFacStartA: str = "1 Jul 1999 11:08:25.658"
            SatFacStopA: str = "1 Jul 1999 11:14:48.079"

            SatFacStartB: str = "1 Jul 1999 11:08:25.641"
            SatFacStopB: str = "1 Jul 1999 11:14:48.060"

            SatFacStartC: str = "1 Jul 1999 11:08:25.649"
            SatFacStopC: str = "1 Jul 1999 11:14:48.070"

            SatFacStartD: str = "1 Jul 1999 11:08:25.650"
            SatFacStopD: str = "1 Jul 1999 11:14:48.068"

            agAssert = None

            # A) Facility to Transmitter: Default values
            oAccess: "StkAccess" = oFacility.get_access_to_object(oTransmitter)
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )

            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("A", SatFacStartA, SatFacStopA, str(accStart), str(accStop))
            )

            # B) Facility to Transmitter: With a specified interval = scenario interval
            oAccess = oFacility.get_access_to_object(oTransmitter)
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period: "AccessTimePeriod" = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("B", SatFacStartA, SatFacStopA, str(accStart), str(accStop))
            )

            # C) Facility to Transmitter: Mode Receive
            oAccess = oFacility.get_access_to_object(oTransmitter)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.RECEIVE
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("C", SatFacStartA, SatFacStopA, str(accStart), str(accStop))
            )

            # D) Facility to Transmitter: Mode Transmit
            oAccess = oFacility.get_access_to_object(oTransmitter)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.TRANSMIT
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("D", SatFacStartB, SatFacStopB, str(accStart), str(accStop))
            )

            # E) Facility to Transmitter: With a specified interval, Mode Receive
            oAccess = oFacility.get_access_to_object(oTransmitter)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.RECEIVE
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("E", SatFacStartA, SatFacStopA, str(accStart), str(accStop))
            )

            # F) Facility to Transmitter: With a specified interval, Mode Transmit
            oAccess = oFacility.get_access_to_object(oTransmitter)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.TRANSMIT
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("F", SatFacStartB, SatFacStopB, str(accStart), str(accStop))
            )

            # G) Facility to Transmitter: Reverse ClockHost
            oAccess = oFacility.get_access_to_object(oTransmitter)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.clock_host = IV_CLOCK_HOST.TARGET
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("G", SatFacStartC, SatFacStopC, str(accStart), str(accStop))
            )

            # H) Facility to Transmitter: With a specified interval, Reverse ClockHost
            oAccess = oFacility.get_access_to_object(oTransmitter)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.clock_host = IV_CLOCK_HOST.TARGET
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("H", SatFacStartC, SatFacStopC, str(accStart), str(accStop))
            )

            # /////////////////////////////////////////////////////////////////////////////////////////////////////
            # /////////////////////////////////////////////////////////////////////////////////////////////////////

            # I) Receiver to Facility: Default values
            oAccess = oReceiver.get_access_to_object(oFacility)
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("I", SatFacStartD, SatFacStopD, str(accStart), str(accStop))
            )

            # J) Receiver to Facility: With a specified interval = scenario interval
            oAccess = oReceiver.get_access_to_object(oFacility)
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("J", SatFacStartD, SatFacStopD, str(accStart), str(accStop))
            )

            # K) Receiver to Facility: Mode Receive
            oAccess = oReceiver.get_access_to_object(oFacility)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.RECEIVE
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("K", SatFacStartD, SatFacStopD, str(accStart), str(accStop))
            )

            # L) Receiver to Facility: Mode Transmit
            oAccess = oReceiver.get_access_to_object(oFacility)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.TRANSMIT
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("L", SatFacStartC, SatFacStopC, str(accStart), str(accStop))
            )

            # M) Receiver to Facility: With a specified interval, Mode Receive
            oAccess = oReceiver.get_access_to_object(oFacility)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.RECEIVE
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("M", SatFacStartD, SatFacStopD, str(accStart), str(accStop))
            )

            # N) Receiver to Facility: With a specified interval, Mode Transmit
            oAccess = oReceiver.get_access_to_object(oFacility)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.TRANSMIT
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("N", SatFacStartC, SatFacStopC, str(accStart), str(accStop))
            )

            # O) Receiver to Facility: Reverse ClockHost
            oAccess = oReceiver.get_access_to_object(oFacility)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.clock_host = IV_CLOCK_HOST.TARGET
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("O", SatFacStartB, SatFacStopB, str(accStart), str(accStop))
            )

            # P) Receiver to Facility: With a specified interval, Reverse ClockHost
            oAccess = oReceiver.get_access_to_object(oFacility)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.clock_host = IV_CLOCK_HOST.TARGET
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("P", SatFacStartB, SatFacStopB, str(accStart), str(accStop))
            )

            # /////////////////////////////////////////////////////////////////////////////////////////////////////
            # /////////////////////////////////////////////////////////////////////////////////////////////////////

            plStart: str = "1 Jul 1999 00:00:00.000"
            plStop: str = "1 Jul 1999 05:31:00.848"

            # Q) Planet to Facility: Default values
            oAccess = oPlanet.get_access_to_object(oFacility)
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("Q", plStart, plStop, str(accStart), str(accStop))
            )

            # R) Planet to Facility: With a specified interval = scenario interval
            oAccess = oPlanet.get_access_to_object(oFacility)
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times(str(scene.start_time), str(scene.stop_time))
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("R", plStart, plStop, str(accStart), str(accStop))
            )

            # /////////////////////////////////////////////////////////////////////////////////////////////////////
            # /////////////////////////////////////////////////////////////////////////////////////////////////////

            # create FacNoConstraints
            oFacNoCon = TestBase.Application.current_scenario.children.new_on_central_body(
                STK_OBJECT_TYPE.FACILITY, "FacNoConstraints", "Earth"
            )
            facNoConColl: "AccessConstraintCollection" = oFacNoCon.access_constraints
            facNoConColl.remove_constraint(ACCESS_CONSTRAINTS.LINE_OF_SIGHT)  # so, the facility has no constraints

            # create MarsSat
            oMarsSat = TestBase.Application.current_scenario.children.new_on_central_body(
                STK_OBJECT_TYPE.SATELLITE, "MarsSat", "Mars"
            )
            sat: "Satellite" = clr.CastAs(oMarsSat, Satellite)
            sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
            twobody: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(sat.propagator)
            twobody.ephemeris_interval.set_explicit_interval(str(scene.start_time), str(scene.stop_time))

            classical: "OrbitStateClassical" = OrbitStateClassical(
                twobody.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL)
            )
            classical.location_type = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
            trueanomaly: "ClassicalLocationTrueAnomaly" = ClassicalLocationTrueAnomaly(classical.location)
            trueanomaly.value = 60.0
            twobody.initial_state.representation.assign(classical)
            (clr.CastAs(sat.propagator, VehiclePropagatorTwoBody)).propagate()

            marsColl: "AccessConstraintCollection" = oMarsSat.access_constraints
            marsColl.remove_constraint(ACCESS_CONSTRAINTS.LINE_OF_SIGHT)  # so, the satellite has no constraints

            oAccess = oFacNoCon.get_access_to_object(oMarsSat)
            oAccess.access_time_period = ACCESS_TIME_TYPE.OBJECT_ACCESS_TIME
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.clock_host = IV_CLOCK_HOST.BASE
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.RECEIVE
            oAccess.compute_access()

            availStartTrunc: str = "1 Jul 1999 00:06:47"  # truncated to whole secs, not rounded
            availStopTrunc: str = "2 Jul 1999 00:06:50"  # truncated to whole secs, not rounded
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            availStart: str = str(accStart)
            availStop: str = str(accStop)
            startTrunc: str = availStart[0 : (0 + Math.Min(19, len(availStart)))]  # drop partial secs
            stopTrunc: str = availStop[0 : (0 + Math.Min(19, len(availStop)))]  # drop partial secs
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("S", availStartTrunc, availStopTrunc, startTrunc, stopTrunc)
            )

            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.TRANSMIT
            oAccess.compute_access()

            availStartTrunc = "30 Jun 1999 23:53:12"  # truncated to whole secs, not rounded
            availStopTrunc = "1 Jul 1999 23:53:09"  # truncated to whole secs, not rounded
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )
            availStart = str(accStart)
            availStop = str(accStop)
            startTrunc = availStart[0 : (0 + Math.Min(20, len(availStart)))]  # drop partial secs
            stopTrunc = availStop[0 : (0 + Math.Min(19, len(availStop)))]  # drop partial secs
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("T", availStartTrunc, availStopTrunc, startTrunc, stopTrunc)
            )

            # /////////////////////////////////////////////////////////////////////////////////////////////////////
            # /////////////////////////////////////////////////////////////////////////////////////////////////////

            oAccess.remove_access()

            marsColl.add_constraint(ACCESS_CONSTRAINTS.LINE_OF_SIGHT)

            oAccess = oFacNoCon.get_access_to_object(oMarsSat)
            oAccess.advanced.use_default_clock_host_and_signal_sense = False
            oAccess.advanced.clock_host = IV_CLOCK_HOST.BASE
            oAccess.advanced.signal_sense_of_clock_host = IV_TIME_SENSE.RECEIVE
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_and_stop_times("1 Jul 1999 21:00:00", "2 Jul 1999 00:03:00")
            oAccess.compute_access()

            intColl: "IntervalCollection" = oAccess.computed_access_interval_times
            Assert.assertEqual(3, intColl.count)

            expectedStartTrunc: str = "1 Jul 1999 23:50:28"  # truncated to whole secs, not rounded
            expectedStopTrunc: str = "2 Jul 1999 00:03:00"  # truncated to whole secs, not rounded
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 2
            )
            availStart = str(accStart)
            availStop = str(accStop)
            startTrunc = availStart[0 : (0 + Math.Min(19, len(availStart)))]  # drop partial secs
            stopTrunc = availStop[0 : (0 + Math.Min(19, len(availStop)))]  # drop partial secs
            agAssert = BugFixes.AgAssertEqualString.BitwiseOr(
                agAssert, self.CompareIntervalTimes("U", expectedStartTrunc, expectedStopTrunc, startTrunc, stopTrunc)
            )
            if agAssert != None:
                agAssert.Assert()

        finally:
            # Clean-up the objects created for this test
            oSatellite.children.unload(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")
            oSatellite.children.unload(STK_OBJECT_TYPE.TRANSMITTER, "TestTransmitter")
            if oMarsSat != None:
                oMarsSat.unload()

            if oFacNoCon != None:
                oFacNoCon.unload()

        TestBase.logger.WriteLine("----- UserSpecifiedIntervals ACCESS TEST ----- END -----")

    def test_BUG108448_SpecifyFixedStepSize(self):
        TestBase.logger.WriteLine("----- BUG108448_SpecifyFixedStepSize ACCESS TEST ----- BEGIN -----")

        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["CalcScalSat"]

        accStart: typing.Any = None
        accStop: typing.Any = None

        try:
            oReceiver: "IStkObject" = oSatellite.children.new(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")

            # Specify a 1-minute time step to see that it is used (interval times will be forced to land on the minute)
            oAccess: "StkAccess" = oFacility.get_access_to_object(oReceiver)
            oAccess.advanced.use_fixed_time_step = True
            oAccess.advanced.fixed_step_size = 60.0
            oAccess.advanced.use_precise_event_times = False
            oAccess.compute_access()
            (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                oAccess.computed_access_interval_times, 0
            )

            Assert.assertEqual("1 Jul 1999 11:09:00.000", str(accStart))
            Assert.assertEqual("1 Jul 1999 11:14:00.000", str(accStop))

        finally:
            # Clean-up the objects created for this test
            oSatellite.children.unload(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")

        TestBase.logger.WriteLine("----- BUG108448_SpecifyFixedStepSize ACCESS TEST ----- END -----")

    def test_BUG108187_ExceptionThrownWhenAccessHasBeenDeleted(self):
        TestBase.logger.WriteLine(
            "----- BUG108187_ExceptionThrownWhenAccessHasBeenDeleted ACCESS TEST ----- BEGIN -----"
        )

        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["CalcScalSat"]

        bDeleteReceiver: bool = True

        try:
            oReceiver: "IStkObject" = oSatellite.children.new(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")

            oAccess: "StkAccess" = oFacility.get_access_to_object(oReceiver)

            # Delete the Receiver, invalidating the Access
            oSatellite.children.unload(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")
            bDeleteReceiver = False

            def code1():
                nonlocal oAccess
                oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME

            Assert.assertRaises(code1)

            def code2():
                nonlocal oAccess
                o: typing.Any = oAccess.access_time_period_data

            Assert.assertRaises(code2)

            def code3():
                nonlocal oAccess
                oAccess.advanced.use_default_clock_host_and_signal_sense = False

            Assert.assertRaises(code3)

            def code4():
                nonlocal oAccess
                oAccess.clear_access()

            Assert.assertRaises(code4)

            def code5():
                nonlocal oAccess
                oAccess.compute_access()

            Assert.assertRaises(code5)

            def code6():
                nonlocal oAccess
                accStart: typing.Any = None
                accStop: typing.Any = None
                (accStart, accStop) = IntervalCollectionExtensionMethods.GetIntervalHelper(
                    oAccess.computed_access_interval_times, 0
                )

            Assert.assertRaises(code6)

            def code7():
                nonlocal oAccess
                oAccess.remove_access()

            Assert.assertRaises(code7)

            def code8():
                nonlocal oAccess
                oAccess.specify_access_time_period("1 Jul 1999 00:00:00.000000000", "2 Jul 1999 00:00:00.000000000")

            Assert.assertRaises(code8)

            def code9():
                nonlocal oAccess
                oAccess.save_computed_data = False

            Assert.assertRaises(code9)
            with pytest.raises(Exception):
                oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            with pytest.raises(Exception):
                o: typing.Any = oAccess.access_time_period_data
            with pytest.raises(Exception):
                oAccess.remove_access()

        finally:
            if bDeleteReceiver:
                oSatellite.children.unload(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")

        TestBase.logger.WriteLine("----- BUG108187_ExceptionThrownWhenAccessHasBeenDeleted ACCESS TEST ----- END -----")

    def test_BUG108228_SaveComputedDataParameter(self):
        TestBase.logger.WriteLine("----- BUG108228_SaveComputedDataParameter ACCESS TEST ----- BEGIN -----")

        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Facility1"]
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["CalcScalSat"]

        try:
            oReceiver: "IStkObject" = oSatellite.children.new(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")

            oAccess: "StkAccess" = oFacility.get_access_to_object(oReceiver)
            bSaveData: bool = oAccess.save_computed_data
            Assert.assertTrue((bSaveData == True))
            oAccess.save_computed_data = False
            oAccess.compute_access()

            oAccess2: "StkAccess" = oFacility.get_access_to_object(oReceiver)
            bSaveData2: bool = oAccess2.save_computed_data
            Assert.assertTrue((bSaveData2 == False))
            oAccess2.save_computed_data = True
            oAccess2.compute_access()

            oAccess3: "StkAccess" = oFacility.get_access_to_object(oReceiver)
            bSaveData3: bool = oAccess3.save_computed_data
            Assert.assertTrue((bSaveData3 == True))

        finally:
            oSatellite.children.unload(STK_OBJECT_TYPE.RECEIVER, "TestReceiver")

        TestBase.logger.WriteLine("----- BUG108228_SaveComputedDataParameter ACCESS TEST ----- END -----")

    def test_BUG108049_AlwaysAvailableObjects(self):
        TestBase.logger.WriteLine("----- BUG108049_AlwaysAvailableObjects ACCESS TEST ----- BEGIN -----")

        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["AccessBugFixesFac"]
        oMarsPlanet: "IStkObject" = TestBase.Application.current_scenario.children["MarsJPL"]

        oAccess: "StkAccess" = None

        try:
            # compute over scenario
            oAccess = oFacility.get_access_to_object(oMarsPlanet)
            oAccess.access_time_period = ACCESS_TIME_TYPE.SCENARIO_ACCESS_TIME
            oAccess.compute_access()
            intColl: "IntervalCollection" = oAccess.computed_access_interval_times
            Assert.assertEqual(2, intColl.count)

            # compute 3 days after scenario - still should have same number of accesses
            dateObj: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", str(scene.start_time))
            startDateObj: "Date" = dateObj.add("Day", 3.0)
            oAccess.access_time_period = ACCESS_TIME_TYPE.USER_SPEC_ACCESS_TIME
            period: "AccessTimePeriod" = AccessTimePeriod(oAccess.access_time_period_data)
            period.access_interval.set_start_time_and_duration(startDateObj.format("UTCG"), "+1 day")
            oAccess.compute_access()
            intColl = oAccess.computed_access_interval_times
            Assert.assertEqual(2, intColl.count)

        finally:
            if oAccess != None:
                oAccess.remove_access()

        TestBase.logger.WriteLine("----- BUG108049_AlwaysAvailableObjects ACCESS TEST ----- END -----")

    def test_BUG108055_IntervalAtAssignedTimeNotUsed(self):
        TestBase.logger.WriteLine("----- BUG108055_IntervalAtAssignedTimeNotUsed ACCESS TEST ----- BEGIN -----")

        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["AccessBugFixesFac"]

        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "sat108055"
        )

        oAccess: "StkAccess" = None

        try:
            leo: "Satellite" = Satellite(oSatellite)

            leo.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
            twobody: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(leo.propagator)

            twobody.ephemeris_interval.set_explicit_interval(str(scene.start_time), str(scene.stop_time))

            classical: "OrbitStateClassical" = OrbitStateClassical(
                twobody.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL)
            )

            (classical).epoch = str(scene.start_time)

            classical.location_type = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
            trueanomaly: "ClassicalLocationTrueAnomaly" = ClassicalLocationTrueAnomaly(classical.location)
            trueanomaly.value = 0
            classical.coordinate_system_type = COORDINATE_SYSTEM.ICRF
            classical.orientation.arg_of_perigee = 0.0
            classical.orientation.inclination = 45.0
            classical.orientation.asc_node_type = ORIENTATION_ASC_NODE.ASC_NODE_RAAN
            oRAAN: "OrientationAscNodeRAAN" = OrientationAscNodeRAAN(classical.orientation.asc_node)
            oRAAN.value = 0.0
            classical.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
            sizeAlt: "ClassicalSizeShapeAltitude" = ClassicalSizeShapeAltitude(classical.size_shape)
            sizeAlt.apogee_altitude = 400.0
            sizeAlt.perigee_altitude = 300.0
            twobody.initial_state.representation.assign(classical)
            twobody.propagate()

            # compute over object times
            oAccess = oFacility.get_access_to_object(oSatellite)
            oAccess.access_time_period = ACCESS_TIME_TYPE.OBJECT_ACCESS_TIME
            oAccess.compute_access()
            intColl: "IntervalCollection" = oAccess.computed_access_interval_times
            Assert.assertEqual(8, intColl.count)

            # compute over umbra times
            oAccess.access_time_period = ACCESS_TIME_TYPE.EVENT_INTERVALS
            oAccess.specify_access_event_intervals(oSatellite.vgt.time_interval_lists["LightingIntervals.Umbra"])
            oAccess.compute_access()
            intColl = oAccess.computed_access_interval_times
            Assert.assertEqual(0, intColl.count)

            oAccess.remove_access()

            # update raan and start over
            oRAAN.value = 50.0
            twobody.initial_state.representation.assign(classical)
            twobody.propagate()

            # compute over object times
            oAccess = oFacility.get_access_to_object(oSatellite)
            oAccess.access_time_period = ACCESS_TIME_TYPE.OBJECT_ACCESS_TIME
            oAccess.compute_access()
            intColl = oAccess.computed_access_interval_times
            Assert.assertEqual(7, intColl.count)

            # compute over umbra times
            oAccess.access_time_period = ACCESS_TIME_TYPE.EVENT_INTERVALS
            oAccess.specify_access_event_intervals(oSatellite.vgt.time_interval_lists["LightingIntervals.Umbra"])
            oAccess.compute_access()
            intColl = oAccess.computed_access_interval_times
            Assert.assertEqual(1, intColl.count)

            oAccess.remove_access()

            # start over - assign the time component, don't compute, update the satellite, then compute
            oAccess = oFacility.get_access_to_object(oSatellite)
            oAccess.access_time_period = ACCESS_TIME_TYPE.EVENT_INTERVALS
            oAccess.specify_access_event_intervals(oSatellite.vgt.time_interval_lists["LightingIntervals.Umbra"])
            # update raan
            oRAAN.value = 0.0
            twobody.initial_state.representation.assign(classical)
            twobody.propagate()
            oAccess.compute_access()
            intColl = oAccess.computed_access_interval_times
            Assert.assertEqual(0, intColl.count)  # get result consistent with raan at 0, not raan at 50!

        finally:
            if oAccess != None:
                oAccess.remove_access()

            oSatellite.unload()

        TestBase.logger.WriteLine("----- BUG108055_IntervalAtAssignedTimeNotUsed ACCESS TEST ----- END -----")

    def test_BUG108208_UseOfDeletedTimeComponent(self):
        TestBase.logger.WriteLine("----- BUG108208_UseOfDeletedTimeComponent ACCESS TEST ----- BEGIN -----")

        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["AccessBugFixesFac"]
        oSatellite: "IStkObject" = TestBase.Application.current_scenario.children["AccessBugFixesSat"]

        compName: str = "bug108208FixedIntrvl"
        group: "TimeToolTimeIntervalListGroup" = None
        oAccess: "StkAccess" = None

        try:
            group = oSatellite.vgt.time_interval_lists
            factory: "TimeToolTimeIntervalListFactory" = group.factory
            intrvlList: "ITimeToolTimeIntervalList" = factory.create_fixed(
                compName, "Fixed interval to test bug 108208"
            )
            Assert.assertIsNotNone(intrvlList)

            intrvlListFxd: "TimeToolTimeIntervalListFixed" = clr.CastAs(intrvlList, TimeToolTimeIntervalListFixed)

            # these intervals are within withe normal access intervals
            start1: str = "1 Jul 1999 13:45:00.000"
            stop1: str = "1 Jul 1999 13:50:00.000"
            start2: str = "1 Jul 1999 20:10:00.000"
            stop2: str = "1 Jul 1999 20:15:00.000"
            arIntervals = [start1, stop1, start2, stop2]
            intrvlListFxd.set_intervals(arIntervals)
            oAccess = oFacility.get_access_to_object(oSatellite)
            oAccess.access_time_period = ACCESS_TIME_TYPE.EVENT_INTERVALS
            oAccess.specify_access_event_intervals(oSatellite.vgt.time_interval_lists[compName])
            oAccess.compute_access()
            intColl: "IntervalCollection" = oAccess.computed_access_interval_times
            Assert.assertEqual(2, intColl.count)

            # now delete the time component
            group.remove(compName)
            Assert.assertFalse(group.contains(compName))
            compName = None  # to avoid removing on finally call below

            # access should have been notified, and updated itself to keep the intervals as before
            intColl = oAccess.computed_access_interval_times
            Assert.assertEqual(2, intColl.count)
            Assert.assertEqual(oAccess.access_time_period, ACCESS_TIME_TYPE.EVENT_INTERVALS)
            accInvtlList: "AccessTimeEventIntervals" = AccessTimeEventIntervals(oAccess.access_time_period_data)
            accInvtlListVals: "ITimeToolTimeIntervalList" = accInvtlList.list_of_intervals
            accCrdn: "IAnalysisWorkbenchComponent" = clr.CastAs(accInvtlListVals, IAnalysisWorkbenchComponent)
            if BugFixes._verbose:
                Console.WriteLine(("Component name is " + accCrdn.name))
                Console.WriteLine(("Component path is " + accCrdn.path))
                Console.WriteLine(("Component description is " + accCrdn.description))
                Console.WriteLine(("Component qualPath is " + accCrdn.qualified_path))

            expectedInstPath: str = (
                ("Access/Facility-" + oFacility.instance_name) + "-To-Satellite-"
            ) + oSatellite.instance_name
            expectedLen: int = len(expectedInstPath)
            accCrdnInstPath: str = accCrdn.path[0 : (0 + Math.Min(expectedLen, len(accCrdn.path)))]
            Assert.assertEqual(expectedInstPath, accCrdnInstPath)

            accIntrvlListType: "EVENT_INTERVAL_LIST_TYPE" = accInvtlListVals.type
            Assert.assertEqual(accIntrvlListType, EVENT_INTERVAL_LIST_TYPE.FIXED)
            res: "TimeToolIntervalListResult" = accInvtlListVals.find_intervals()
            Assert.assertTrue(res.is_valid)
            coll: "TimeToolIntervalCollection" = res.intervals
            Assert.assertEqual(2, coll.count)

            intrvl: "TimeToolInterval" = coll[0]
            Assert.assertEqual(start1, intrvl.start)
            Assert.assertEqual(stop1, intrvl.stop)
            intrvl = coll[1]
            Assert.assertEqual(start2, intrvl.start)
            Assert.assertEqual(stop2, intrvl.stop)

            oAccess.compute_access()
            intColl = oAccess.computed_access_interval_times
            Assert.assertEqual(2, intColl.count)

        finally:
            if oAccess != None:
                oAccess.remove_access()

            if (group != None) and (compName != None):
                group.remove(compName)

        TestBase.logger.WriteLine("----- BUG108208_UseOfDeletedTimeComponent ACCESS TEST ----- END -----")
