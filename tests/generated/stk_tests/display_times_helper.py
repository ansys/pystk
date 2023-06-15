from test_util import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


# region IntervalCollectionHelper
class IntervalCollectionHelper(object):
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

        def action1():
            oCollection.RemoveAll()

        # RemoveAll
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action1)
        oStart = "1 Jul 1999 00:00:00.00"
        oStop = "1 Jul 1999 01:00:00.000"

        def action2():
            iIndex = oCollection.Add(oStart, oStop)

        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action2)
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

            def action3():
                oCollection.ChangeInterval(0, oNewStart, oNewStop)

            # ChangeInterval
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action3)

            def action4():
                oCollection.Deconflict()

            # Deconflict
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action4)

            def action5():
                oCollection.RemoveInterval(oStart, oStop)

            # RemoveInterval
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action5)

            def action6():
                oCollection.RemoveIndex(0)

            # RemoveIndex
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action6)

        def action7():
            oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))

        # LoadIntervals
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action7)

        def action8():
            oCollection.Deconflict()

        # Deconflict
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action8)

    # endregion

    # region Constraint
    def Constraint(self, oCollection: "IIntervalCollection"):
        Assert.assertIsNotNone(oCollection)
        if self.m_bReadOnlyFile:

            def action9():
                oCollection.RemoveAll()

            # RemoveAll
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action9)
            oStart = "1 Jul 1999 00:00:00.00"
            oStop = "1 Jul 1999 01:00:00.000"

            def action10():
                iIndex = oCollection.Add(oStart, oStop)

            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action10)
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

                def action11():
                    oCollection.ChangeInterval(0, oNewStart, oNewStop)

                # ChangeInterval
                TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action11)

                def action12():
                    oCollection.Deconflict()

                # Deconflict
                TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action12)

                def action13():
                    oCollection.RemoveInterval(oStart, oStop)

                # RemoveInterval
                TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action13)

                def action14():
                    oCollection.RemoveIndex(0)

                # RemoveIndex
                TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action14)

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

            def action15():
                oCollection.Deconflict()

            # Deconflict
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action15)

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

            def action16():
                oCollection.Deconflict()

            # Deconflict
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action16)
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

            def action17():
                oCollection.Deconflict()

            # Deconflict
            TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action17)

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

        def action18():
            oCollection.Deconflict()

        # Deconflict
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action18)
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

        def action19():
            oCollection.LoadIntervals(TestBase.GetScenarioFile("intervals.int"))

        # LoadIntervals
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action19)

        def action20():
            oCollection.Deconflict()

        # Deconflict
        TryCatchAssertBlock.DoAssert("Should not allow to modify collection!", action20)

    # endregion
