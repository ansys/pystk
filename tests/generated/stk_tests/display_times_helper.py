import pytest
from test_util import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


# region DisplayTimesHelper
class DisplayTimesHelper(object):
    def __init__(self, oRoot: "StkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oRoot)
        self.m_oRoot: "StkObjectRoot" = oRoot

    # endregion

    # region Run method
    def Run(self, oDisplay: "IDisplayTime"):
        Assert.assertIsNotNone(oDisplay)
        self.m_logger.WriteLine("DisplayTimes test:")
        # DisplayStatusSupportedTypes
        arTypes = oDisplay.display_status_supported_types
        self.m_logger.WriteLine3("\tDisplayTimes supports {0} types:", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                (
                    DISPLAY_TIMES_TYPE(int(arTypes[iIndex][0]))
                    if (int(arTypes[iIndex][0]) in [item.value for item in DISPLAY_TIMES_TYPE])
                    else int(arTypes[iIndex][0])
                ),
            )

            iIndex += 1

        if not oDisplay.is_display_status_type_supported(DISPLAY_TIMES_TYPE.DURING_CHAIN_ACCESS):
            with pytest.raises(Exception):
                oDisplay.set_display_status_type(DISPLAY_TIMES_TYPE.DURING_CHAIN_ACCESS)

        # TYPE_UNKNOWN
        with pytest.raises(Exception):
            oDisplay.set_display_status_type(DISPLAY_TIMES_TYPE.TYPE_UNKNOWN)
        # DisplayStatusType
        self.m_logger.WriteLine6("\tThe current DisplayStatusType is: {0}", oDisplay.display_status_type)

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "DISPLAY_TIMES_TYPE" = (
                DISPLAY_TIMES_TYPE(int(arTypes[iIndex][0]))
                if (int(arTypes[iIndex][0]) in [item.value for item in DISPLAY_TIMES_TYPE])
                else int(arTypes[iIndex][0])
            )
            if not oDisplay.is_display_status_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetDisplayStatusType
            oDisplay.set_display_status_type(eType)
            self.m_logger.WriteLine6("\tThe new DisplayStatusType is: {0}", oDisplay.display_status_type)
            eType1: "DISPLAY_TIMES_TYPE" = oDisplay.display_status_type
            Assert.assertEqual(eType, eType1)
            if eType == DISPLAY_TIMES_TYPE.TYPE_UNKNOWN:
                Assert.fail("TYPE_UNKNOWN should not be supported!")
            elif (((eType == DISPLAY_TIMES_TYPE.ALWAYS_OFF)) or ((eType == DISPLAY_TIMES_TYPE.ALWAYS_ON))) or (
                (eType == DISPLAY_TIMES_TYPE.DURING_CHAIN_ACCESS)
            ):
                displayTimesData: "IDisplayTimesData" = oDisplay.display_times_data
                Assert.assertIsNone(displayTimesData)
                self.m_logger.WriteLine("\t\tNo DisplayTimesData available.")
            elif eType == DISPLAY_TIMES_TYPE.DURING_ACCESS:
                self.DuringAccess(clr.CastAs(oDisplay.display_times_data, DuringAccess))
            elif eType == DISPLAY_TIMES_TYPE.USE_INTERVALS:
                oHelper = IntervalCollectionHelper(self.m_oRoot.unit_preferences)
                oHelper.Run(
                    IntervalCollection(oDisplay.display_times_data),
                    IntervalCollectionHelper.IntervalCollectionType.Intervals,
                )
            elif eType == DISPLAY_TIMES_TYPE.USE_TIME_COMPONENT:
                self.DisplayTimesTimeComponent(clr.CastAs(oDisplay.display_times_data, DisplayTimesTimeComponent))
            else:
                Assert.fail("Unknown DISPLAY_TIMES_TYPE")

            iIndex += 1

    # endregion

    # region DuringAccess method
    def DuringAccess(self, oAccess: "DuringAccess"):
        Assert.assertIsNotNone(oAccess)
        # AccessObjects
        oOLCHelper = ObjectLinkCollectionHelper()
        oOLCHelper.Run(oAccess.access_objects, self.m_oRoot)
        # DisplayIntervals
        oAccess.access_objects.add("Star/Star1")
        oICHelper = IntervalCollectionHelper(self.m_oRoot.unit_preferences)
        oICHelper.Run(oAccess.display_intervals, IntervalCollectionHelper.IntervalCollectionType.DuringAccess)

    # endregion

    # region DisplayTimesTimeComponent method
    def DisplayTimesTimeComponent(self, dttc: "DisplayTimesTimeComponent"):
        # Only Intervals and Interval Lists are supported.

        Assert.assertIsNotNone(dttc)
        Assert.assertEqual("", dttc.get_qualified_path())

        with pytest.raises(Exception):
            dttc.set_qualified_path("")
        with pytest.raises(Exception):
            dttc.set_qualified_path("Scenario/Scenario1 Bogus Interval")
        with pytest.raises(Exception):
            dttc.set_qualified_path("Scenario/Scenario1 AnalysisStartTime Event")
        with pytest.raises(Exception):
            dttc.set_qualified_path("Facility/Facility1 LightingIntervals EventIntervalCollection")
        with pytest.raises(Exception):
            dttc.set_qualified_path("Scenario/Scenario1 OneMinuteSampleTimes EventArray")

        dttc.set_qualified_path(
            (("Scenario/" + self.m_oRoot.current_scenario.instance_name) + " AnalysisInterval EventInterval")
        )
        Assert.assertEqual(
            (("Scenario/" + self.m_oRoot.current_scenario.instance_name) + " AnalysisInterval EventInterval"),
            dttc.get_qualified_path(),
        )
        dttc.set_qualified_path(
            (("Scenario/" + self.m_oRoot.current_scenario.instance_name) + " AvailabilityIntervals EventIntervalList")
        )
        Assert.assertEqual(
            (("Scenario/" + self.m_oRoot.current_scenario.instance_name) + " AvailabilityIntervals EventIntervalList"),
            dttc.get_qualified_path(),
        )

        crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
            self.m_oRoot.current_scenario.vgt.events["AnalysisStartTime"], IAnalysisWorkbenchComponent
        )
        with pytest.raises(Exception):
            dttc.set_time_component(crdn)
        crdnFac: "IAnalysisWorkbenchComponent" = clr.CastAs(
            self.m_oRoot.current_scenario.children["Facility1"].vgt.event_interval_collections["LightingIntervals"],
            IAnalysisWorkbenchComponent,
        )
        with pytest.raises(Exception):
            dttc.set_time_component(crdnFac)
        crdn = clr.CastAs(
            self.m_oRoot.current_scenario.vgt.event_arrays["OneMinuteSampleTimes"], IAnalysisWorkbenchComponent
        )
        with pytest.raises(Exception):
            dttc.set_time_component(crdn)

        crdn = clr.CastAs(
            self.m_oRoot.current_scenario.vgt.event_intervals["AnalysisInterval"], IAnalysisWorkbenchComponent
        )
        dttc.set_time_component(crdn)
        Assert.assertEqual(
            (("Scenario/" + self.m_oRoot.current_scenario.instance_name) + " AnalysisInterval EventInterval"),
            (clr.CastAs(dttc.get_time_component(), IAnalysisWorkbenchComponent)).qualified_path,
        )

        crdn = clr.CastAs(
            self.m_oRoot.current_scenario.vgt.event_interval_lists["AvailabilityIntervals"], IAnalysisWorkbenchComponent
        )
        dttc.set_time_component(crdn)
        Assert.assertEqual(
            (("Scenario/" + self.m_oRoot.current_scenario.instance_name) + " AvailabilityIntervals EventIntervalList"),
            (clr.CastAs(dttc.get_time_component(), IAnalysisWorkbenchComponent)).qualified_path,
        )

        dttc.reset()
        Assert.assertEqual("", dttc.get_qualified_path())


# endregion


# region IntervalCollectionHelper
class IntervalCollectionHelper(object):
    # region IntervalCollectionType enum
    class IntervalCollectionType:
        Intervals = 0
        DuringAccess = 1
        LabelNotes = 2
        Constraint = 3

    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits
        self.m_bReadOnlyFile: bool = False

    # endregion

    # region SetReadOnly
    def SetReadOnly(self, bIsReadOnly: bool):
        self.m_bReadOnlyFile = bIsReadOnly

    # endregion

    # region Run method
    def Run(self, oCollection: "IntervalCollection", eType):
        Assert.assertIsNotNone(oCollection)
        self.m_logger.WriteLine("IntervalCollection test:")
        # set DateFormat
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DateFormat")
        self.m_logger.WriteLine5("\tThe current DateFormat is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DateFormat", "UTCG")
        self.m_logger.WriteLine5("\tThe new DateFormat is: {0}", self.m_oUnits.get_current_unit_abbrv("DateFormat"))
        Assert.assertEqual("UTCG", self.m_oUnits.get_current_unit_abbrv("DateFormat"))
        # Count
        self.m_logger.WriteLine3("\tThe current IntervalCollection contains: {0} elements", oCollection.count)
        if oCollection.count > 0:
            arIntervals = oCollection.to_array(0, -1)

            iIndex: int = 0
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

        if eType == IntervalCollectionHelper.IntervalCollectionType.Constraint:
            self.Constraint(oCollection)
        elif eType == IntervalCollectionHelper.IntervalCollectionType.DuringAccess:
            self.DuringAccess(oCollection)
        elif eType == IntervalCollectionHelper.IntervalCollectionType.Intervals:
            self.Intervals(oCollection)
        elif eType == IntervalCollectionHelper.IntervalCollectionType.LabelNotes:
            self.LabelNotes(oCollection)
        # restore DateFormat
        self.m_oUnits.set_current_unit("DateFormat", strUnit)
        self.m_logger.WriteLine5("\tThe new DateFormat (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DateFormat"))

    # endregion

    # region DuringAccess
    def DuringAccess(self, oCollection: "IntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        # RemoveAll
        with pytest.raises(Exception):
            oCollection.remove_all()

        oStart: typing.Any = None
        oStop: typing.Any = None

        oStart = "1 Jul 1999 00:00:00.00"
        oStop = "1 Jul 1999 01:00:00.000"
        with pytest.raises(Exception):
            iIndex: int = oCollection.add(oStart, oStop)
        if oCollection.count > 0:
            # ToArray
            arIntervals = oCollection.to_array(0, -1)
            self.m_logger.WriteLine3(
                "\tAfter ToArray() the IntervalCollection contains: {0} elements", len(arIntervals)
            )

            iIndex: int = 0
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

            # GetInterval
            (oStart, oStop) = oCollection.get_interval(0)
            oNewStart: typing.Any = "1 Jun 2004 12:34:56.789"
            oNewStop: typing.Any = "2 Jun 2004 00:00:00.000"
            # ChangeInterval
            with pytest.raises(Exception):
                oCollection.change_interval(0, oNewStart, oNewStop)
            # Deconflict
            with pytest.raises(Exception):
                oCollection.deconflict()
            # RemoveInterval
            with pytest.raises(Exception):
                oCollection.remove_interval(oStart, oStop)
            # RemoveIndex
            with pytest.raises(Exception):
                oCollection.remove_index(0)

        # LoadIntervals
        with pytest.raises(Exception):
            oCollection.load_intervals(TestBase.GetScenarioFile("intervals.int"))
        # Deconflict
        with pytest.raises(Exception):
            oCollection.deconflict()

    # endregion

    # region Constraint
    def Constraint(self, oCollection: "IntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        if self.m_bReadOnlyFile:
            # RemoveAll
            with pytest.raises(Exception):
                oCollection.remove_all()

            oStart: typing.Any = None
            oStop: typing.Any = None

            oStart = "1 Jul 1999 00:00:00.00"
            oStop = "1 Jul 1999 01:00:00.000"
            with pytest.raises(Exception):
                iIndex: int = oCollection.add(oStart, oStop)
            # ToArray
            arIntervals = oCollection.to_array(0, -1)
            self.m_logger.WriteLine3(
                "\tAfter ToArray() the IntervalCollection contains: {0} elements", len(arIntervals)
            )

            iIndex: int = 0
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

            if oCollection.count > 0:
                # GetInterval
                (oStart, oStop) = oCollection.get_interval(0)
                oNewStart: typing.Any = "1 Jun 2004 12:34:56.789"
                oNewStop: typing.Any = "2 Jun 2004 00:00:00.000"
                # ChangeInterval
                with pytest.raises(Exception):
                    oCollection.change_interval(0, oNewStart, oNewStop)
                # Deconflict
                with pytest.raises(Exception):
                    oCollection.deconflict()
                # RemoveInterval
                with pytest.raises(Exception):
                    oCollection.remove_interval(oStart, oStop)
                # RemoveIndex
                with pytest.raises(Exception):
                    oCollection.remove_index(0)

            # LoadIntervals
            oCollection.load_intervals(TestBase.GetScenarioFile("intervals.int"))
            self.m_logger.WriteLine3("\tAfter LoadIntervals() collection contains: {0} elements", oCollection.count)
            Assert.assertEqual(3, oCollection.count)
            arIntervals = oCollection.to_array(0, -1)
            self.m_logger.WriteLine3(
                "\tAfter ToArray() the IntervalCollection contains: {0} elements", len(arIntervals)
            )

            iIndex: int = 0
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

            # Deconflict
            with pytest.raises(Exception):
                oCollection.deconflict()

        else:
            # RemoveAll
            self.m_logger.WriteLine3("\tBefore RemoveAll() collection contains: {0} elements", oCollection.count)
            oCollection.remove_all()
            self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.count)

            oStart: typing.Any = None
            oStop: typing.Any = None

            oStart = "1 Jul 1999 00:00:00.00"
            oStop = "1 Jul 1999 01:00:00.000"
            iIndex: int = oCollection.add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
            )
            self.m_logger.WriteLine3("\t\tThe last added element index is: {0}", iIndex)
            Assert.assertEqual(1, oCollection.count)
            Assert.assertEqual(0, iIndex)
            # Add Duplicate (will not be added)
            iIndex1: int = oCollection.add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) again collection contains: {0} elements", oCollection.count, oStart, oStop
            )
            Assert.assertEqual(1, oCollection.count)
            # Add 2
            oStart = "1 Jul 1999 01:30:00.00"
            oStop = "1 Jul 1999 02:00:00.000"
            iIndex = oCollection.add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
            )
            Assert.assertEqual(2, oCollection.count)
            # Add 3
            oStart = "1 Jul 1999 02:30:00.00"
            oStop = "1 Jul 1999 03:00:00.000"
            iIndex = oCollection.add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
            )
            Assert.assertEqual(3, oCollection.count)
            # ToArray
            arIntervals = oCollection.to_array(0, -1)
            Assert.assertEqual(3, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: Start = {1}, Stop = {2}", iIndex, arIntervals[iIndex][0], arIntervals[iIndex][1]
                )

                iIndex += 1
            # modify interval data
            # GetInterval
            (oStart, oStop) = oCollection.get_interval(0)
            self.m_logger.WriteLine7("\tThe current Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
            oStart = "1 Jun 2004 12:34:56.789"
            oStop = "2 Jun 2004 00:00:00.000"
            # ChangeInterval
            oCollection.change_interval(0, oStart, oStop)
            self.m_logger.WriteLine7("\tThe new Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
            self.m_logger.WriteLine3("\tThe current Interval collection contains: {0} elements", oCollection.count)
            arIntervals = oCollection.to_array(0, -1)
            Assert.assertEqual(oCollection.count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # Deconflict
            with pytest.raises(Exception):
                oCollection.deconflict()
            # RemoveInterval
            (oStart, oStop) = oCollection.get_interval(0)
            oCollection.remove_interval(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter RemoveInterval({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
            )
            arIntervals = oCollection.to_array(0, -1)
            Assert.assertEqual(oCollection.count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # Add
            iNewIndex: int = oCollection.add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
            )
            arIntervals = oCollection.to_array(0, -1)
            Assert.assertEqual(oCollection.count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # RemoveIndex
            oCollection.remove_index(iNewIndex)
            self.m_logger.WriteLine7(
                "\tAfter RemoveIndex({1}) collection contains: {0} elements", oCollection.count, iNewIndex
            )
            arIntervals = oCollection.to_array(0, -1)
            Assert.assertEqual(oCollection.count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # RemoveAll
            oCollection.remove_all()
            self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.count)
            Assert.assertEqual(0, oCollection.count)
            # LoadIntervals
            oCollection.load_intervals(TestBase.GetScenarioFile("intervals.int"))
            self.m_logger.WriteLine3("\tAfter LoadIntervals() collection contains: {0} elements", oCollection.count)
            Assert.assertEqual(3, oCollection.count)
            arIntervals = oCollection.to_array(0, -1)
            Assert.assertEqual(oCollection.count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # LoadIntervals again
            oCollection.load_intervals(TestBase.GetScenarioFile("intervals.int"))
            self.m_logger.WriteLine3(
                "\tAfter Duplicate LoadIntervals() collection contains: {0} elements", oCollection.count
            )
            Assert.assertEqual(3, oCollection.count)
            arIntervals = oCollection.to_array(0, -1)
            Assert.assertEqual(oCollection.count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # Deconflict
            with pytest.raises(Exception):
                oCollection.deconflict()

    # endregion

    # region Intervals
    def Intervals(self, oCollection: "IntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        # RemoveAll
        self.m_logger.WriteLine3("\tBefore RemoveAll() collection contains: {0} elements", oCollection.count)
        oCollection.remove_all()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(0, oCollection.count)

        oStart: typing.Any = None
        oStop: typing.Any = None

        oStart = "1 Jul 1999 00:00:00.00"
        oStop = "1 Jul 1999 01:00:00.000"
        iIndex: int = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        self.m_logger.WriteLine3("\t\tThe last added element index is: {0}", iIndex)
        Assert.assertEqual(1, oCollection.count)
        Assert.assertEqual(0, iIndex)
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Add Duplicate (will not be added)
        iIndex1: int = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) again collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        Assert.assertEqual(1, oCollection.count)
        # Add 2
        oStart = "1 Jul 1999 01:30:00.00"
        oStop = "1 Jul 1999 02:00:00.000"
        iIndex = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        Assert.assertEqual(2, oCollection.count)
        # Add 3
        oStart = "1 Jul 1999 02:30:00.00"
        oStop = "1 Jul 1999 03:00:00.000"
        iIndex = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        Assert.assertEqual(3, oCollection.count)
        # ToArray
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(3, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: Start = {1}, Stop = {2}", iIndex, arIntervals[iIndex][0], arIntervals[iIndex][1]
            )

            iIndex += 1
        # modify interval data
        # GetInterval
        (oStart, oStop) = oCollection.get_interval(0)
        self.m_logger.WriteLine7("\tThe current Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
        oStart = "1 Jun 2004 12:34:56.789"
        oStop = "2 Jun 2004 00:00:00.000"
        # ChangeInterval
        oCollection.change_interval(0, oStart, oStop)
        self.m_logger.WriteLine7("\tThe new Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
        self.m_logger.WriteLine3("\tThe current Interval collection contains: {0} elements", oCollection.count)
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

        # Deconflict
        oCollection.deconflict()
        self.m_logger.WriteLine3("\tAfter Deconflict() collection contains: {0} elements", oCollection.count)
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveInterval
        oCollection.remove_interval(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter RemoveInterval({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Add
        iNewIndex: int = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveIndex
        oCollection.remove_index(iNewIndex)
        self.m_logger.WriteLine7(
            "\tAfter RemoveIndex({1}) collection contains: {0} elements", oCollection.count, iNewIndex
        )
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveAll
        oCollection.remove_all()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(0, oCollection.count)
        # LoadIntervals
        oCollection.load_intervals(TestBase.GetScenarioFile("intervals.int"))
        self.m_logger.WriteLine3("\tAfter LoadIntervals() collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(4, oCollection.count)
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # LoadIntervals again
        oCollection.load_intervals(TestBase.GetScenarioFile("intervals.int"))
        self.m_logger.WriteLine3(
            "\tAfter Duplicate LoadIntervals() collection contains: {0} elements", oCollection.count
        )
        Assert.assertEqual(4, oCollection.count)
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Deconflict
        oCollection.deconflict()
        self.m_logger.WriteLine3("\tAfter Deconflict() collection contains: {0} elements", oCollection.count)
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

    # endregion

    # region LabelNotes
    def LabelNotes(self, oCollection: "IntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        # RemoveAll
        self.m_logger.WriteLine3("\tBefore RemoveAll() collection contains: {0} elements", oCollection.count)
        oCollection.remove_all()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(0, oCollection.count)

        oStart: typing.Any = None
        oStop: typing.Any = None

        oStart = "1 Jul 1999 00:00:00.00"
        oStop = "1 Jul 1999 01:00:00.000"
        iIndex: int = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        self.m_logger.WriteLine3("\t\tThe last added element index is: {0}", iIndex)
        Assert.assertEqual(1, oCollection.count)
        Assert.assertEqual(0, iIndex)
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Add Duplicate (will not be added)
        iIndex1: int = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) again collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        Assert.assertEqual(1, oCollection.count)
        # Add 2
        oStart = "1 Jul 1999 01:00:00.00"
        oStop = "1 Jul 1999 02:00:00.000"
        iIndex = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        Assert.assertEqual(2, oCollection.count)
        # Add 3
        oStart = "1 Jul 1999 02:00:00.00"
        oStop = "1 Jul 1999 03:00:00.000"
        iIndex = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        Assert.assertEqual(3, oCollection.count)
        # ToArray
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(3, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: Start = {1}, Stop = {2}", iIndex, arIntervals[iIndex][0], arIntervals[iIndex][1]
            )

            iIndex += 1
        # modify interval data
        # GetInterval
        (oStart, oStop) = oCollection.get_interval(0)
        self.m_logger.WriteLine7("\tThe current Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
        oStart = "1 Jun 2004 12:34:56.789"
        oStop = "2 Jun 2004 00:00:00.000"
        # ChangeInterval
        oCollection.change_interval(0, oStart, oStop)
        self.m_logger.WriteLine7("\tThe new Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
        self.m_logger.WriteLine3("\tThe current Interval collection contains: {0} elements", oCollection.count)
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

        # Deconflict
        with pytest.raises(Exception):
            oCollection.deconflict()
        # RemoveInterval
        oCollection.remove_interval(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter RemoveInterval({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Add
        iNewIndex: int = oCollection.add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.count, oStart, oStop
        )
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveIndex
        oCollection.remove_index(iNewIndex)
        self.m_logger.WriteLine7(
            "\tAfter RemoveIndex({1}) collection contains: {0} elements", oCollection.count, iNewIndex
        )
        arIntervals = oCollection.to_array(0, -1)
        Assert.assertEqual(oCollection.count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveAll
        oCollection.remove_all()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(0, oCollection.count)
        # LoadIntervals
        with pytest.raises(Exception):
            oCollection.load_intervals(TestBase.GetScenarioFile("intervals.int"))
        # Deconflict
        with pytest.raises(Exception):
            oCollection.deconflict()


# endregion
# region ObjectLinkCollectionHelper
class ObjectLinkCollectionHelper(object):
    def __init__(self, AllowDuplicates: bool = False, RestrictToOneElement: bool = False):
        self.m_logger = Logger.Instance
        self._bAllowDuplicates: bool = AllowDuplicates
        self._bRestrictToOneElement: bool = RestrictToOneElement

    # endregion

    # region Run method
    def Run(self, oCollection: "ObjectLinkCollection", oRoot: "StkObjectRoot"):
        Assert.assertIsNotNone(oCollection)
        Assert.assertIsNotNone(oRoot)
        self.m_logger.WriteLine("ObjectLinkCollection test:")

        # RemoveAll
        oCollection.remove_all()
        Assert.assertEqual(0, oCollection.count)

        # AvailableObjects
        arAvailable = oCollection.available_objects
        self.m_logger.WriteLine3("\tAvailable {0} objects:", Array.Length(arAvailable))

        iIndex: int = 0
        while iIndex < Array.Length(arAvailable):
            self.m_logger.WriteLine7("\t\tObject {0}: {1}", iIndex, arAvailable[iIndex])

            iIndex += 1

        # Count
        self.m_logger.WriteLine3("\tThe current ObjectLink collection contain: {0} elements", oCollection.count)

        # Add 0
        oCollection.add(str(arAvailable[0]))
        self.m_logger.WriteLine6("\t\tObject {0} was added to collection.", arAvailable[0])
        Assert.assertEqual(1, oCollection.count)
        if not self._bAllowDuplicates:
            with pytest.raises(Exception):
                oCollection.add(str(arAvailable[0]))
            Assert.assertEqual(1, oCollection.count)

        else:
            oCollection.add(str(arAvailable[0]))
            Assert.assertEqual(2, oCollection.count)
            # Remove elements with the same name will remove
            # all occurences of the object.
            oCollection.remove_name(str(arAvailable[0]))
            Assert.assertEqual(0, oCollection.count)
            oCollection.add(str(arAvailable[0]))
            Assert.assertEqual(1, oCollection.count)

        with pytest.raises(Exception):
            oCollection.add("InvalidObject")
        Assert.assertEqual(1, oCollection.count)
        self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.count)
        if self._bRestrictToOneElement:
            # BUG83611 exception message below should be more descriptive
            with pytest.raises(Exception, match=RegexSubstringMatch("trying to add")):
                oCollection.add(str(arAvailable[1]))

        else:
            # Add 1
            oCollection.add(str(arAvailable[1]))
            self.m_logger.WriteLine6("\t\tObject {0} was added to collection.", arAvailable[1])
            Assert.assertEqual(2, oCollection.count)
            self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.count)
            oLink: "ObjectLink"
            for oLink in oCollection:
                Console.WriteLine(
                    "\t\tElement: Name = {0}, Path = {1}, Type = {2}, LinkedObject = {3}",
                    oLink.name,
                    oLink.path,
                    oLink.type,
                    oLink.linked_object.path,
                )

        # Contains
        Assert.assertTrue(
            oCollection.contains(
                (((r"/Application/STK/Scenario/" + oRoot.current_scenario.instance_name) + "/") + str(arAvailable[0]))
            ),
            "Contains1",
        )
        Assert.assertTrue(oCollection.contains(str(arAvailable[0])), "Contains2")
        if not self._bRestrictToOneElement:
            Assert.assertTrue(
                oCollection.contains(
                    (
                        ((r"/Application/STK/Scenario/" + oRoot.current_scenario.instance_name) + "/")
                        + str(arAvailable[1])
                    )
                ),
                "Contains3",
            )
            Assert.assertTrue(oCollection.contains(str(arAvailable[1])), "Contains4")

        Assert.assertFalse(
            oCollection.contains(
                ((r"/Application/STK/Scenario/" + oRoot.current_scenario.instance_name) + "/Aircraft/BOGUS")
            ),
            "Contains5",
        )
        Assert.assertFalse(oCollection.contains(r"Aircraft/BOGUS"), "Contains6")

        # IndexOf
        Assert.assertEqual(
            0,
            oCollection.index_of(
                (((r"/Application/STK/Scenario/" + oRoot.current_scenario.instance_name) + "/") + str(arAvailable[0]))
            ),
            "IndexOf1",
        )
        Assert.assertEqual(0, oCollection.index_of(str(arAvailable[0])), "IndexOf2")
        if not self._bRestrictToOneElement:
            Assert.assertEqual(
                1,
                oCollection.index_of(
                    (
                        ((r"/Application/STK/Scenario/" + oRoot.current_scenario.instance_name) + "/")
                        + str(arAvailable[1])
                    )
                ),
                "IndexOf3",
            )
            Assert.assertEqual(1, oCollection.index_of(str(arAvailable[1])), "IndexOf4")

        Assert.assertEqual(-1, oCollection.index_of(r"Aircraft/BOGUS"), "IndexOf5")
        Assert.assertEqual(-1, oCollection.index_of(r""), "IndexOf6")

        # RemoveName
        oCollection.remove_name(str(arAvailable[0]))
        self.m_logger.WriteLine6("\t\tObject {0} was removed from collection.", arAvailable[0])
        if not self._bRestrictToOneElement:
            Assert.assertEqual(1, oCollection.count)

        else:
            Assert.assertEqual(0, oCollection.count)

        with pytest.raises(Exception):
            oCollection.remove_name(str(arAvailable[0]))
        with pytest.raises(Exception):
            oCollection.remove_name("InvalidObject")
        self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.count)

        # Remove
        strName: str = None
        if not self._bRestrictToOneElement:
            strName = oCollection[0].name
            oCollection.remove(0)
            self.m_logger.WriteLine5("\t\tObject {0} was removed from collection.", strName)
            Assert.assertEqual(0, oCollection.count)
            with pytest.raises(Exception):
                oCollection.remove((Array.Length(arAvailable) + 1))
            Assert.assertEqual(0, oCollection.count)
            self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.count)

        # AddObject
        strName = str(arAvailable[0])
        oObject: "IStkObject" = oRoot.get_object_from_path(strName)
        Assert.assertIsNotNone(oObject)
        oCollection.add_object(oObject)
        self.m_logger.WriteLine5("\tObject {0} was added to collection.", oObject.path)
        Assert.assertEqual(1, oCollection.count)
        Assert.assertTrue((((oObject.class_name + "/") + oObject.instance_name) in oCollection[0].path))
        self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.count)

        # RemoveObject
        oCollection.remove_object(oObject)
        self.m_logger.WriteLine5("\t\tObject {0} was removed from collection.", strName)
        Assert.assertEqual(0, oCollection.count)
        self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.count)

    # endregion


# endregion
