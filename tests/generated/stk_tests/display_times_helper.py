from test_util import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


# region DisplayTimesHelper
class DisplayTimesHelper(object):
    def __init__(self, oRoot: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oRoot)
        self.m_oRoot = oRoot

    # endregion

    # region Run method
    def Run(self, oDisplay: "IDisplayTime"):
        Assert.assertIsNotNone(oDisplay)
        self.m_logger.WriteLine("DisplayTimes test:")
        # DisplayStatusSupportedTypes
        arTypes = oDisplay.DisplayStatusSupportedTypes
        self.m_logger.WriteLine3("\tDisplayTimes supports {0} types:", len(arTypes))

        iIndex = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                clr.Convert(int(arTypes[iIndex][0]), AgEDisplayTimesType),
            )

            iIndex += 1

        if not oDisplay.IsDisplayStatusTypeSupported(AgEDisplayTimesType.eDuringChainAccess):

            def action1():
                oDisplay.SetDisplayStatusType(AgEDisplayTimesType.eDuringChainAccess)

            TryCatchAssertBlock.DoAssert("Cannot set eDuringChainAccess type!", action1)

        def action2():
            oDisplay.SetDisplayStatusType(AgEDisplayTimesType.eDisplayTypeUnknown)

        # eDisplayTypeUnknown
        TryCatchAssertBlock.DoAssert("Cannot set eDisplayTypeUnknown type!", action2)
        # DisplayStatusType
        self.m_logger.WriteLine6("\tThe current DisplayStatusType is: {0}", oDisplay.DisplayStatusType)

        iIndex = 0
        while iIndex < len(arTypes):
            eType = clr.Convert(int(arTypes[iIndex][0]), AgEDisplayTimesType)
            if not oDisplay.IsDisplayStatusTypeSupported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetDisplayStatusType
            oDisplay.SetDisplayStatusType(eType)
            self.m_logger.WriteLine6("\tThe new DisplayStatusType is: {0}", oDisplay.DisplayStatusType)
            eType1 = oDisplay.DisplayStatusType
            Assert.assertEqual(eType, eType1)
            if eType == AgEDisplayTimesType.eDisplayTypeUnknown:
                Assert.fail("eDisplayTypeUnknown should not be supported!")
            elif (((eType == AgEDisplayTimesType.eAlwaysOff)) or ((eType == AgEDisplayTimesType.eAlwaysOn))) or (
                (eType == AgEDisplayTimesType.eDuringChainAccess)
            ):
                oData = oDisplay.DisplayTimesData
                Assert.assertIsNone(oData)
                self.m_logger.WriteLine("\t\tNo DisplayTimesData available.")
            elif eType == AgEDisplayTimesType.eDuringAccess:
                self.DuringAccess(clr.CastAs(oDisplay.DisplayTimesData, IDuringAccess))
            elif eType == AgEDisplayTimesType.eUseIntervals:
                oHelper = IntervalCollectionHelper(self.m_oRoot.UnitPreferences)
                oHelper.Run(
                    clr.Convert(oDisplay.DisplayTimesData, IIntervalCollection),
                    IntervalCollectionHelper.IntervalCollectionType.Intervals,
                )
            elif eType == AgEDisplayTimesType.eUseTimeComponent:
                self.DisplayTimesTimeComponent(clr.CastAs(oDisplay.DisplayTimesData, IDisplayTimesTimeComponent))
            else:
                Assert.fail("Unknown AgEDisplayTimesType")

            iIndex += 1

    # endregion

    # region DuringAccess method
    def DuringAccess(self, oAccess: "IDuringAccess"):
        Assert.assertIsNotNone(oAccess)
        # AccessObjects
        oOLCHelper = ObjectLinkCollectionHelper()
        oOLCHelper.Run(oAccess.AccessObjects, self.m_oRoot)
        # DisplayIntervals
        oAccess.AccessObjects.Add("Star/Star1")
        oICHelper = IntervalCollectionHelper(self.m_oRoot.UnitPreferences)
        oICHelper.Run(oAccess.DisplayIntervals, IntervalCollectionHelper.IntervalCollectionType.DuringAccess)

    # endregion

    # region DisplayTimesTimeComponent method
    def DisplayTimesTimeComponent(self, dttc: "IDisplayTimesTimeComponent"):
        # Only Intervals and Interval Lists are supported.

        Assert.assertIsNotNone(dttc)
        Assert.assertEqual("", dttc.GetQualifiedPath())

        def action3():
            dttc.SetQualifiedPath("")

        TryCatchAssertBlock.DoAssert("Setting blank component", action3)

        def action4():
            dttc.SetQualifiedPath("Scenario/Scenario1 Bogus Interval")

        TryCatchAssertBlock.DoAssert("Setting bogus component", action4)

        def action5():
            dttc.SetQualifiedPath("Scenario/Scenario1 AnalysisStartTime Event")

        TryCatchAssertBlock.DoAssert("Setting event component", action5)

        def action6():
            dttc.SetQualifiedPath("Facility/Facility1 LightingIntervals EventIntervalCollection")

        TryCatchAssertBlock.DoAssert("Setting IntervalCollection component", action6)

        def action7():
            dttc.SetQualifiedPath("Scenario/Scenario1 OneMinuteSampleTimes EventArray")

        TryCatchAssertBlock.DoAssert("Setting EventArray component", action7)

        dttc.SetQualifiedPath(
            (("Scenario/" + self.m_oRoot.CurrentScenario.InstanceName) + " AnalysisInterval EventInterval")
        )
        Assert.assertEqual(
            (("Scenario/" + self.m_oRoot.CurrentScenario.InstanceName) + " AnalysisInterval EventInterval"),
            dttc.GetQualifiedPath(),
        )
        dttc.SetQualifiedPath(
            (("Scenario/" + self.m_oRoot.CurrentScenario.InstanceName) + " AvailabilityIntervals EventIntervalList")
        )
        Assert.assertEqual(
            (("Scenario/" + self.m_oRoot.CurrentScenario.InstanceName) + " AvailabilityIntervals EventIntervalList"),
            dttc.GetQualifiedPath(),
        )

        crdn: IAnalysisWorkbenchComponent = clr.CastAs(
            self.m_oRoot.CurrentScenario.Vgt.Events["AnalysisStartTime"], IAnalysisWorkbenchComponent
        )

        def action8():
            dttc.SetTimeComponent(crdn)

        TryCatchAssertBlock.DoAssert("Setting event component", action8)
        crdnFac: IAnalysisWorkbenchComponent = clr.CastAs(
            self.m_oRoot.CurrentScenario.Children["Facility1"].Vgt.EventIntervalCollections["LightingIntervals"],
            IAnalysisWorkbenchComponent,
        )

        def action9():
            dttc.SetTimeComponent(crdnFac)

        TryCatchAssertBlock.DoAssert("Setting IntervalCollection component", action9)
        crdn: IAnalysisWorkbenchComponent = clr.CastAs(
            self.m_oRoot.CurrentScenario.Vgt.EventArrays["OneMinuteSampleTimes"], IAnalysisWorkbenchComponent
        )

        def action10():
            dttc.SetTimeComponent(crdn)

        TryCatchAssertBlock.DoAssert("Setting EventArray component", action10)

        crdn: IAnalysisWorkbenchComponent = clr.CastAs(
            self.m_oRoot.CurrentScenario.Vgt.EventIntervals["AnalysisInterval"], IAnalysisWorkbenchComponent
        )
        dttc.SetTimeComponent(crdn)
        Assert.assertEqual(
            (("Scenario/" + self.m_oRoot.CurrentScenario.InstanceName) + " AnalysisInterval EventInterval"),
            (clr.CastAs(dttc.GetTimeComponent(), IAnalysisWorkbenchComponent)).QualifiedPath,
        )

        crdn: IAnalysisWorkbenchComponent = clr.CastAs(
            self.m_oRoot.CurrentScenario.Vgt.EventIntervalLists["AvailabilityIntervals"], IAnalysisWorkbenchComponent
        )
        dttc.SetTimeComponent(crdn)
        Assert.assertEqual(
            (("Scenario/" + self.m_oRoot.CurrentScenario.InstanceName) + " AvailabilityIntervals EventIntervalList"),
            (clr.CastAs(dttc.GetTimeComponent(), IAnalysisWorkbenchComponent)).QualifiedPath,
        )

        dttc.Reset()
        Assert.assertEqual("", dttc.GetQualifiedPath())


# endregion


# region IntervalCollectionHelper
class IntervalCollectionHelper(object):
    # region IntervalCollectionType enum
    class IntervalCollectionType:
        Intervals = 0
        DuringAccess = 1
        LabelNotes = 2
        Constraint = 3

    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits
        self.m_bReadOnlyFile = False

    # endregion

    # region SetReadOnly
    def SetReadOnly(self, bIsReadOnly: bool):
        self.m_bReadOnlyFile = bIsReadOnly

    # endregion

    # region Run method
    def Run(self, oCollection: "IIntervalCollection", eType):
        Assert.assertIsNotNone(oCollection)
        self.m_logger.WriteLine("IntervalCollection test:")
        # set DateFormat
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DateFormat")
        self.m_logger.WriteLine5("\tThe current DateFormat is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DateFormat", "UTCG")
        self.m_logger.WriteLine5("\tThe new DateFormat is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DateFormat"))
        Assert.assertEqual("UTCG", self.m_oUnits.GetCurrentUnitAbbrv("DateFormat"))
        # Count
        self.m_logger.WriteLine3("\tThe current IntervalCollection contains: {0} elements", oCollection.Count)
        if oCollection.Count > 0:
            arIntervals = oCollection.ToArray(0, -1)

            iIndex = 0
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
        self.m_oUnits.SetCurrentUnit("DateFormat", strUnit)
        self.m_logger.WriteLine5("\tThe new DateFormat (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DateFormat"))

    # endregion

    # region DuringAccess
    def DuringAccess(self, oCollection: "IIntervalCollection"):
        Assert.assertIsNotNone(oCollection)

        def action11():
            oCollection.RemoveAll()

        # RemoveAll
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action11)
        oStart = "1 Jul 1999 00:00:00.00"
        oStop = "1 Jul 1999 01:00:00.000"

        def action12():
            iIndex = oCollection.Add(oStart, oStop)

        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action12)
        if oCollection.Count > 0:
            # ToArray
            arIntervals = oCollection.ToArray(0, -1)
            self.m_logger.WriteLine3(
                "\tAfter ToArray() the IntervalCollection contains: {0} elements", len(arIntervals)
            )

            iIndex = 0
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

            # GetInterval
            (oStart, oStop) = oCollection.GetInterval(0)
            oNewStart = "1 Jun 2004 12:34:56.789"
            oNewStop = "2 Jun 2004 00:00:00.000"

            def action13():
                oCollection.ChangeInterval(0, oNewStart, oNewStop)

            # ChangeInterval
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action13)

            def action14():
                oCollection.Deconflict()

            # Deconflict
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action14)

            def action15():
                oCollection.RemoveInterval(oStart, oStop)

            # RemoveInterval
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action15)

            def action16():
                oCollection.RemoveIndex(0)

            # RemoveIndex
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action16)

        def action17():
            oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))

        # LoadIntervals
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action17)

        def action18():
            oCollection.Deconflict()

        # Deconflict
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action18)

    # endregion

    # region Constraint
    def Constraint(self, oCollection: "IIntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        if self.m_bReadOnlyFile:

            def action19():
                oCollection.RemoveAll()

            # RemoveAll
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action19)
            oStart = "1 Jul 1999 00:00:00.00"
            oStop = "1 Jul 1999 01:00:00.000"

            def action20():
                iIndex = oCollection.Add(oStart, oStop)

            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action20)
            # ToArray
            arIntervals = oCollection.ToArray(0, -1)
            self.m_logger.WriteLine3(
                "\tAfter ToArray() the IntervalCollection contains: {0} elements", len(arIntervals)
            )

            iIndex = 0
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

            if oCollection.Count > 0:
                # GetInterval
                (oStart, oStop) = oCollection.GetInterval(0)
                oNewStart = "1 Jun 2004 12:34:56.789"
                oNewStop = "2 Jun 2004 00:00:00.000"

                def action21():
                    oCollection.ChangeInterval(0, oNewStart, oNewStop)

                # ChangeInterval
                TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action21)

                def action22():
                    oCollection.Deconflict()

                # Deconflict
                TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action22)

                def action23():
                    oCollection.RemoveInterval(oStart, oStop)

                # RemoveInterval
                TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action23)

                def action24():
                    oCollection.RemoveIndex(0)

                # RemoveIndex
                TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action24)

            # LoadIntervals
            oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))
            self.m_logger.WriteLine3("\tAfter LoadIntervals() collection contains: {0} elements", oCollection.Count)
            Assert.assertEqual(3, oCollection.Count)
            arIntervals = oCollection.ToArray(0, -1)
            self.m_logger.WriteLine3(
                "\tAfter ToArray() the IntervalCollection contains: {0} elements", len(arIntervals)
            )

            iIndex = 0
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

            def action25():
                oCollection.Deconflict()

            # Deconflict
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action25)

        else:
            # RemoveAll
            self.m_logger.WriteLine3("\tBefore RemoveAll() collection contains: {0} elements", oCollection.Count)
            oCollection.RemoveAll()
            self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.Count)
            oStart = "1 Jul 1999 00:00:00.00"
            oStop = "1 Jul 1999 01:00:00.000"
            iIndex = oCollection.Add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
            )
            self.m_logger.WriteLine3("\t\tThe last added element index is: {0}", iIndex)
            Assert.assertEqual(1, oCollection.Count)
            Assert.assertEqual(0, iIndex)
            # Add Duplicate (will not be added)
            iIndex1 = oCollection.Add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) again collection contains: {0} elements", oCollection.Count, oStart, oStop
            )
            Assert.assertEqual(1, oCollection.Count)
            # Add 2
            oStart = "1 Jul 1999 01:30:00.00"
            oStop = "1 Jul 1999 02:00:00.000"
            iIndex = oCollection.Add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
            )
            Assert.assertEqual(2, oCollection.Count)
            # Add 3
            oStart = "1 Jul 1999 02:30:00.00"
            oStop = "1 Jul 1999 03:00:00.000"
            iIndex = oCollection.Add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
            )
            Assert.assertEqual(3, oCollection.Count)
            # ToArray
            arIntervals = oCollection.ToArray(0, -1)
            Assert.assertEqual(3, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: Start = {1}, Stop = {2}", iIndex, arIntervals[iIndex][0], arIntervals[iIndex][1]
                )

                iIndex += 1
            # modify interval data
            # GetInterval
            (oStart, oStop) = oCollection.GetInterval(0)
            self.m_logger.WriteLine7("\tThe current Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
            oStart = "1 Jun 2004 12:34:56.789"
            oStop = "2 Jun 2004 00:00:00.000"
            # ChangeInterval
            oCollection.ChangeInterval(0, oStart, oStop)
            self.m_logger.WriteLine7("\tThe new Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
            self.m_logger.WriteLine3("\tThe current Interval collection contains: {0} elements", oCollection.Count)
            arIntervals = oCollection.ToArray(0, -1)
            Assert.assertEqual(oCollection.Count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

            def action26():
                oCollection.Deconflict()

            # Deconflict
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action26)
            # RemoveInterval
            (oStart, oStop) = oCollection.GetInterval(0)
            oCollection.RemoveInterval(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter RemoveInterval({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
            )
            arIntervals = oCollection.ToArray(0, -1)
            Assert.assertEqual(oCollection.Count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # Add
            iNewIndex = oCollection.Add(oStart, oStop)
            self.m_logger.WriteLine8(
                "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
            )
            arIntervals = oCollection.ToArray(0, -1)
            Assert.assertEqual(oCollection.Count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # RemoveIndex
            oCollection.RemoveIndex(iNewIndex)
            self.m_logger.WriteLine7(
                "\tAfter RemoveIndex({1}) collection contains: {0} elements", oCollection.Count, iNewIndex
            )
            arIntervals = oCollection.ToArray(0, -1)
            Assert.assertEqual(oCollection.Count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # RemoveAll
            oCollection.RemoveAll()
            self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.Count)
            Assert.assertEqual(0, oCollection.Count)
            # LoadIntervals
            oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))
            self.m_logger.WriteLine3("\tAfter LoadIntervals() collection contains: {0} elements", oCollection.Count)
            Assert.assertEqual(3, oCollection.Count)
            arIntervals = oCollection.ToArray(0, -1)
            Assert.assertEqual(oCollection.Count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1
            # LoadIntervals again
            oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))
            self.m_logger.WriteLine3(
                "\tAfter Duplicate LoadIntervals() collection contains: {0} elements", oCollection.Count
            )
            Assert.assertEqual(3, oCollection.Count)
            arIntervals = oCollection.ToArray(0, -1)
            Assert.assertEqual(oCollection.Count, len(arIntervals))
            while iIndex < len(arIntervals):
                self.m_logger.WriteLine8(
                    "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                    iIndex,
                    arIntervals[iIndex][0],
                    arIntervals[iIndex][1],
                )

                iIndex += 1

            def action27():
                oCollection.Deconflict()

            # Deconflict
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action27)

    # endregion

    # region Intervals
    def Intervals(self, oCollection: "IIntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        # RemoveAll
        self.m_logger.WriteLine3("\tBefore RemoveAll() collection contains: {0} elements", oCollection.Count)
        oCollection.RemoveAll()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.Count)
        Assert.assertEqual(0, oCollection.Count)
        oStart = "1 Jul 1999 00:00:00.00"
        oStop = "1 Jul 1999 01:00:00.000"
        iIndex = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        self.m_logger.WriteLine3("\t\tThe last added element index is: {0}", iIndex)
        Assert.assertEqual(1, oCollection.Count)
        Assert.assertEqual(0, iIndex)
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Add Duplicate (will not be added)
        iIndex1 = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) again collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        Assert.assertEqual(1, oCollection.Count)
        # Add 2
        oStart = "1 Jul 1999 01:30:00.00"
        oStop = "1 Jul 1999 02:00:00.000"
        iIndex = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        Assert.assertEqual(2, oCollection.Count)
        # Add 3
        oStart = "1 Jul 1999 02:30:00.00"
        oStop = "1 Jul 1999 03:00:00.000"
        iIndex = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        Assert.assertEqual(3, oCollection.Count)
        # ToArray
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(3, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: Start = {1}, Stop = {2}", iIndex, arIntervals[iIndex][0], arIntervals[iIndex][1]
            )

            iIndex += 1
        # modify interval data
        # GetInterval
        (oStart, oStop) = oCollection.GetInterval(0)
        self.m_logger.WriteLine7("\tThe current Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
        oStart = "1 Jun 2004 12:34:56.789"
        oStop = "2 Jun 2004 00:00:00.000"
        # ChangeInterval
        oCollection.ChangeInterval(0, oStart, oStop)
        self.m_logger.WriteLine7("\tThe new Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
        self.m_logger.WriteLine3("\tThe current Interval collection contains: {0} elements", oCollection.Count)
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

        # Deconflict
        oCollection.Deconflict()
        self.m_logger.WriteLine3("\tAfter Deconflict() collection contains: {0} elements", oCollection.Count)
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveInterval
        oCollection.RemoveInterval(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter RemoveInterval({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Add
        iNewIndex = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveIndex
        oCollection.RemoveIndex(iNewIndex)
        self.m_logger.WriteLine7(
            "\tAfter RemoveIndex({1}) collection contains: {0} elements", oCollection.Count, iNewIndex
        )
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveAll
        oCollection.RemoveAll()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.Count)
        Assert.assertEqual(0, oCollection.Count)
        # LoadIntervals
        oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))
        self.m_logger.WriteLine3("\tAfter LoadIntervals() collection contains: {0} elements", oCollection.Count)
        Assert.assertEqual(4, oCollection.Count)
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # LoadIntervals again
        oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))
        self.m_logger.WriteLine3(
            "\tAfter Duplicate LoadIntervals() collection contains: {0} elements", oCollection.Count
        )
        Assert.assertEqual(4, oCollection.Count)
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Deconflict
        oCollection.Deconflict()
        self.m_logger.WriteLine3("\tAfter Deconflict() collection contains: {0} elements", oCollection.Count)
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
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
    def LabelNotes(self, oCollection: "IIntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        # RemoveAll
        self.m_logger.WriteLine3("\tBefore RemoveAll() collection contains: {0} elements", oCollection.Count)
        oCollection.RemoveAll()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.Count)
        Assert.assertEqual(0, oCollection.Count)
        oStart = "1 Jul 1999 00:00:00.00"
        oStop = "1 Jul 1999 01:00:00.000"
        iIndex = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        self.m_logger.WriteLine3("\t\tThe last added element index is: {0}", iIndex)
        Assert.assertEqual(1, oCollection.Count)
        Assert.assertEqual(0, iIndex)
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Add Duplicate (will not be added)
        iIndex1 = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) again collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        Assert.assertEqual(1, oCollection.Count)
        # Add 2
        oStart = "1 Jul 1999 01:00:00.00"
        oStop = "1 Jul 1999 02:00:00.000"
        iIndex = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        Assert.assertEqual(2, oCollection.Count)
        # Add 3
        oStart = "1 Jul 1999 02:00:00.00"
        oStop = "1 Jul 1999 03:00:00.000"
        iIndex = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        Assert.assertEqual(3, oCollection.Count)
        # ToArray
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(3, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: Start = {1}, Stop = {2}", iIndex, arIntervals[iIndex][0], arIntervals[iIndex][1]
            )

            iIndex += 1
        # modify interval data
        # GetInterval
        (oStart, oStop) = oCollection.GetInterval(0)
        self.m_logger.WriteLine7("\tThe current Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
        oStart = "1 Jun 2004 12:34:56.789"
        oStop = "2 Jun 2004 00:00:00.000"
        # ChangeInterval
        oCollection.ChangeInterval(0, oStart, oStop)
        self.m_logger.WriteLine7("\tThe new Interval 0 is: Start = {0}, Stop = {1}", oStart, oStop)
        self.m_logger.WriteLine3("\tThe current Interval collection contains: {0} elements", oCollection.Count)
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

        def action28():
            oCollection.Deconflict()

        # Deconflict
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action28)
        # RemoveInterval
        oCollection.RemoveInterval(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter RemoveInterval({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # Add
        iNewIndex = oCollection.Add(oStart, oStop)
        self.m_logger.WriteLine8(
            "\tAfter Add({1},{2}) collection contains: {0} elements", oCollection.Count, oStart, oStop
        )
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveIndex
        oCollection.RemoveIndex(iNewIndex)
        self.m_logger.WriteLine7(
            "\tAfter RemoveIndex({1}) collection contains: {0} elements", oCollection.Count, iNewIndex
        )
        arIntervals = oCollection.ToArray(0, -1)
        Assert.assertEqual(oCollection.Count, len(arIntervals))
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1
        # RemoveAll
        oCollection.RemoveAll()
        self.m_logger.WriteLine3("\tAfter RemoveAll() collection contains: {0} elements", oCollection.Count)
        Assert.assertEqual(0, oCollection.Count)

        def action29():
            oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))

        # LoadIntervals
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action29)

        def action30():
            oCollection.Deconflict()

        # Deconflict
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action30)


# endregion
# region ObjectLinkCollectionHelper
class ObjectLinkCollectionHelper(object):
    def __init__(self, AllowDuplicates: bool = False, RestrictToOneElement: bool = False):
        self.m_logger = Logger.Instance
        self._bAllowDuplicates = AllowDuplicates
        self._bRestrictToOneElement = RestrictToOneElement

    # endregion

    # region Run method
    def Run(self, oCollection: "IObjectLinkCollection", oRoot: "IStkObjectRoot"):
        Assert.assertIsNotNone(oCollection)
        Assert.assertIsNotNone(oRoot)
        self.m_logger.WriteLine("ObjectLinkCollection test:")

        # RemoveAll
        oCollection.RemoveAll()
        Assert.assertEqual(0, oCollection.Count)

        # AvailableObjects
        arAvailable = oCollection.AvailableObjects
        self.m_logger.WriteLine3("\tAvailable {0} objects:", Array.Length(arAvailable))

        iIndex = 0
        while iIndex < Array.Length(arAvailable):
            self.m_logger.WriteLine7("\t\tObject {0}: {1}", iIndex, arAvailable[iIndex])

            iIndex += 1

        # Count
        self.m_logger.WriteLine3("\tThe current ObjectLink collection contain: {0} elements", oCollection.Count)

        # Add 0
        oCollection.Add(str(arAvailable[0]))
        self.m_logger.WriteLine6("\t\tObject {0} was added to collection.", arAvailable[0])
        Assert.assertEqual(1, oCollection.Count)
        if not self._bAllowDuplicates:

            def action31():
                oCollection.Add(str(arAvailable[0]))

            TryCatchAssertBlock.DoAssert("Should not allow to add duplicated objects to collection.", action31)
            Assert.assertEqual(1, oCollection.Count)

        else:
            oCollection.Add(str(arAvailable[0]))
            Assert.assertEqual(2, oCollection.Count)
            # Remove elements with the same name will remove
            # all occurences of the object.
            oCollection.RemoveName(str(arAvailable[0]))
            Assert.assertEqual(0, oCollection.Count)
            oCollection.Add(str(arAvailable[0]))
            Assert.assertEqual(1, oCollection.Count)

        def action32():
            oCollection.Add("InvalidObject")

        TryCatchAssertBlock.DoAssert("Should not allow to add invalid object to collection.", action32)
        Assert.assertEqual(1, oCollection.Count)
        self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.Count)
        if self._bRestrictToOneElement:

            def action33():
                oCollection.Add(str(arAvailable[1]))

            # BUG83611 exception message below should be more descriptive
            TryCatchAssertBlock.ExpectedException("trying to add", action33)

        else:
            # Add 1
            oCollection.Add(str(arAvailable[1]))
            self.m_logger.WriteLine6("\t\tObject {0} was added to collection.", arAvailable[1])
            Assert.assertEqual(2, oCollection.Count)
            self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.Count)
            for oLink in oCollection:
                Console.WriteLine(
                    "\t\tElement: Name = {0}, Path = {1}, Type = {2}, LinkedObject = {3}",
                    oLink.Name,
                    oLink.Path,
                    oLink.Type,
                    oLink.LinkedObject.Path,
                )

        # Contains
        Assert.assertTrue(
            oCollection.Contains(
                (((r"/Application/STK/Scenario/" + oRoot.CurrentScenario.InstanceName) + "/") + str(arAvailable[0]))
            ),
            "Contains1",
        )
        Assert.assertTrue(oCollection.Contains(str(arAvailable[0])), "Contains2")
        if not self._bRestrictToOneElement:
            Assert.assertTrue(
                oCollection.Contains(
                    (((r"/Application/STK/Scenario/" + oRoot.CurrentScenario.InstanceName) + "/") + str(arAvailable[1]))
                ),
                "Contains3",
            )
            Assert.assertTrue(oCollection.Contains(str(arAvailable[1])), "Contains4")

        Assert.assertFalse(
            oCollection.Contains(
                ((r"/Application/STK/Scenario/" + oRoot.CurrentScenario.InstanceName) + "/Aircraft/BOGUS")
            ),
            "Contains5",
        )
        Assert.assertFalse(oCollection.Contains(r"Aircraft/BOGUS"), "Contains6")

        # IndexOf
        Assert.assertEqual(
            0,
            oCollection.IndexOf(
                (((r"/Application/STK/Scenario/" + oRoot.CurrentScenario.InstanceName) + "/") + str(arAvailable[0]))
            ),
            "IndexOf1",
        )
        Assert.assertEqual(0, oCollection.IndexOf(str(arAvailable[0])), "IndexOf2")
        if not self._bRestrictToOneElement:
            Assert.assertEqual(
                1,
                oCollection.IndexOf(
                    (((r"/Application/STK/Scenario/" + oRoot.CurrentScenario.InstanceName) + "/") + str(arAvailable[1]))
                ),
                "IndexOf3",
            )
            Assert.assertEqual(1, oCollection.IndexOf(str(arAvailable[1])), "IndexOf4")

        Assert.assertEqual(-1, oCollection.IndexOf(r"Aircraft/BOGUS"), "IndexOf5")
        Assert.assertEqual(-1, oCollection.IndexOf(r""), "IndexOf6")

        # RemoveName
        oCollection.RemoveName(str(arAvailable[0]))
        self.m_logger.WriteLine6("\t\tObject {0} was removed from collection.", arAvailable[0])
        if not self._bRestrictToOneElement:
            Assert.assertEqual(1, oCollection.Count)

        else:
            Assert.assertEqual(0, oCollection.Count)

        def action34():
            oCollection.RemoveName(str(arAvailable[0]))

        TryCatchAssertBlock.DoAssert("Should not allow to remove an invalid object from collection.", action34)

        def action35():
            oCollection.RemoveName("InvalidObject")

        TryCatchAssertBlock.DoAssert("Should not allow to remove an invalid object from collection.", action35)
        self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.Count)
        if not self._bRestrictToOneElement:
            strName = oCollection[0].Name
            oCollection.Remove(0)
            self.m_logger.WriteLine5("\t\tObject {0} was removed from collection.", strName)
            Assert.assertEqual(0, oCollection.Count)

            def action36():
                oCollection.Remove((Array.Length(arAvailable) + 1))

            TryCatchAssertBlock.DoAssert("Should not allow to remove an invalid object from collection.", action36)
            Assert.assertEqual(0, oCollection.Count)
            self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.Count)

        # AddObject
        strName = str(arAvailable[0])
        oObject = oRoot.GetObjectFromPath(strName)
        Assert.assertIsNotNone(oObject)
        oCollection.AddObject(oObject)
        self.m_logger.WriteLine5("\tObject {0} was added to collection.", oObject.Path)
        Assert.assertEqual(1, oCollection.Count)
        Assert.assertTrue((((oObject.ClassName + "/") + oObject.InstanceName) in oCollection[0].Path))
        self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.Count)

        # RemoveObject
        oCollection.RemoveObject(oObject)
        self.m_logger.WriteLine5("\t\tObject {0} was removed from collection.", strName)
        Assert.assertEqual(0, oCollection.Count)
        self.m_logger.WriteLine3("\tThe new ObjectLink collection contain: {0} elements", oCollection.Count)

    # endregion


# endregion
