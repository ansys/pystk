from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from logger import *
from math2 import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


# region GfxRangeContoursHelper
class GfxRangeContoursHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "IGfxRangeContours"):
        self.m_logger.WriteLine("----- THE GRAPHICS RANGE CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # IsVisible
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oContours.IsVisible)
        oContours.IsVisible = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oContours.IsVisible)
        Assert.assertFalse(oContours.IsVisible)
        oContours.IsVisible = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oContours.IsVisible)
        Assert.assertTrue(oContours.IsVisible)
        # IsFillVisible
        self.m_logger.WriteLine4("\tThe current IsFillVisible flag is: {0}", oContours.IsFillVisible)
        oContours.IsFillVisible = False
        self.m_logger.WriteLine4("\tThe new IsFillVisible flag is: {0}", oContours.IsFillVisible)
        Assert.assertFalse(oContours.IsFillVisible)

        def action1():
            oContours.FillStyle = AgEFillStyle.eFillStyleHatch

        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action1)
        oContours.IsFillVisible = True
        self.m_logger.WriteLine4("\tThe new IsFillVisible flag is: {0}", oContours.IsFillVisible)
        Assert.assertTrue(oContours.IsFillVisible)
        # FillStyle
        self.m_logger.WriteLine6("\tThe current FillStyle is: {0}", oContours.FillStyle)
        oContours.FillStyle = AgEFillStyle.eFillStyleDiagonalHatch
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.FillStyle)
        Assert.assertEqual(AgEFillStyle.eFillStyleDiagonalHatch, oContours.FillStyle)
        oContours.FillStyle = AgEFillStyle.eFillStyleDiagonalStripe1
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.FillStyle)
        Assert.assertEqual(AgEFillStyle.eFillStyleDiagonalStripe1, oContours.FillStyle)
        oContours.FillStyle = AgEFillStyle.eFillStyleDiagonalStripe2
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.FillStyle)
        Assert.assertEqual(AgEFillStyle.eFillStyleDiagonalStripe2, oContours.FillStyle)
        oContours.FillStyle = AgEFillStyle.eFillStyleHatch
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.FillStyle)
        Assert.assertEqual(AgEFillStyle.eFillStyleHatch, oContours.FillStyle)
        oContours.FillStyle = AgEFillStyle.eFillStyleHorizontalStripe
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.FillStyle)
        Assert.assertEqual(AgEFillStyle.eFillStyleHorizontalStripe, oContours.FillStyle)
        oContours.FillStyle = AgEFillStyle.eFillStyleScreen
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.FillStyle)
        Assert.assertEqual(AgEFillStyle.eFillStyleScreen, oContours.FillStyle)
        oContours.FillStyle = AgEFillStyle.eFillStyleSolid
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.FillStyle)
        Assert.assertEqual(AgEFillStyle.eFillStyleSolid, oContours.FillStyle)
        oContours.FillStyle = AgEFillStyle.eFillStyleVerticalStripe
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.FillStyle)
        Assert.assertEqual(AgEFillStyle.eFillStyleVerticalStripe, oContours.FillStyle)
        # NumOfDecimalDigits
        self.m_logger.WriteLine3("\tThe current NumOfDecimalDigits is: {0}", oContours.NumOfDecimalDigits)
        oContours.NumOfDecimalDigits = 7
        self.m_logger.WriteLine3("\tThe new NumOfDecimalDigits is: {0}", oContours.NumOfDecimalDigits)
        Assert.assertEqual(7, oContours.NumOfDecimalDigits)

        def action2():
            oContours.NumOfDecimalDigits = 123

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action2)

        def action3():
            oContours.LabelUnit = "test"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action3)

        oContours.FillTranslucency = 55.0
        Assert.assertAlmostEqual(55.0, oContours.FillTranslucency, delta=Math2.Epsilon12)

        availableUnits = oContours.AvailableLabelUnits
        self.m_logger.WriteLine3("The available units contains {0} units.", Array.Length(availableUnits))
        for unit in availableUnits:
            self.m_logger.WriteLine(unit)
            oContours.LabelUnit = unit
            Assert.assertEqual(unit, oContours.LabelUnit)

        # set DistanceUnit
        self.m_logger.WriteLine5(
            "\tThe current DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

        # LevelAttributes
        oLevels = oContours.LevelAttributes
        Assert.assertIsNotNone(oLevels)
        # Count
        self.m_logger.WriteLine3("\tThe Level Attribute Collection contains: {0} elements.", oLevels.Count)
        # _NewEnum
        for oElement in oLevels:
            self.m_logger.WriteLine10(
                "\t\tElement: Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                oElement.Level,
                oElement.Color,
                oElement.LineStyle,
                oElement.LineWidth,
                oElement.LabelVisible,
                oElement.LabelVisible,
                oElement.UserTextVisible,
                oElement.UserText,
                oElement.LabelAngle,
            )

        # AddLevel
        self.m_logger.WriteLine3(
            "\tBefore AddLevel() the Level Attribute Collection contains: {0} elements.", oLevels.Count
        )
        oAdded = oLevels.AddLevel(123.456)
        Assert.assertIsNotNone(oAdded)
        self.m_logger.WriteLine3(
            "\tAfter AddLevel() the Level Attribute Collection contains: {0} elements.", oLevels.Count
        )
        for oElement in oLevels:
            self.m_logger.WriteLine10(
                "\t\tElement: Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                oElement.Level,
                oElement.Color,
                oElement.LineStyle,
                oElement.LineWidth,
                oElement.LabelVisible,
                oElement.LabelVisible,
                oElement.UserTextVisible,
                oElement.UserText,
                oElement.LabelAngle,
            )

        # Remove
        self.m_logger.WriteLine3(
            "\tBefore Remove() the Level Attribute Collection contains: {0} elements.", oLevels.Count
        )
        oLevels.Remove((oLevels.Count - 1))
        self.m_logger.WriteLine3(
            "\tAfter RemoveAt() the Level Attribute Collection contains: {0} elements.", oLevels.Count
        )
        # AddLevelRange
        oLevels.AddLevelRange(12.5, 34.5, 0.5)
        self.m_logger.WriteLine3(
            "\tAfter AddLevelRange() the Level Attribute Collection contains: {0} elements.", oLevels.Count
        )
        if oLevels.Count > 0:
            # Item
            oElement = oLevels[0]
            Assert.assertIsNotNone(oElement)
            self.m_logger.WriteLine10(
                "\t\tElement (Before): Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                oElement.Level,
                oElement.Color,
                oElement.LineStyle,
                oElement.LineWidth,
                oElement.LabelVisible,
                oElement.LabelVisible,
                oElement.UserTextVisible,
                oElement.UserText,
                oElement.LabelAngle,
            )
            oElement.Color = Color.FromArgb((oElement.Color._ToOLECOLOR() + 250))
            oElement.LineStyle = AgELineStyle.eMDash
            oElement.LineWidth = AgELineWidth.e2
            oElement.Level = float(oElement.Level) + 1.5
            oElement.LabelVisible = not oElement.LabelVisible
            oElement.UserTextVisible = True
            oElement.UserText = "UserText test string"
            oElement.LabelAngle = 15
            self.m_logger.WriteLine10(
                "\t\tElement (After): Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                oElement.Level,
                oElement.Color,
                oElement.LineStyle,
                oElement.LineWidth,
                oElement.LabelVisible,
                oElement.LabelVisible,
                oElement.UserTextVisible,
                oElement.UserText,
                oElement.LabelAngle,
            )

            def action4():
                oElement.LabelAngle = 1234

            TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action4)

        def action5():
            oLevels.AddLevelRange(12.34, 34.12, 0.2)

        TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action5)

        # RemoveAll
        oLevels.RemoveAll()
        self.m_logger.WriteLine3("\tAfter RemoveAll() the Elevations Collection contains: {0} elements.", oLevels.Count)
        Assert.assertEqual(0, oLevels.Count)
        self.m_logger.WriteLine("----- THE GRAPHICS RANGE CONTOURS TEST ----- END -----")


# endregion


# region GfxLabelNoteHelper
class GfxLabelNoteHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oCollection: "ILabelNoteCollection"):
        self.m_logger.WriteLine("----- THE GRAPHICS LABELNOTES TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.Count)

        iIndex = 0
        while iIndex < oCollection.Count:
            self.m_logger.WriteLine9(
                "\tElement {0}: Note = {1}, NoteVisible = {2}, LabelVisible = {3}",
                iIndex,
                oCollection[iIndex].Note,
                oCollection[iIndex].NoteVisible,
                oCollection[iIndex].LabelVisible,
            )

            iIndex += 1

        # Count
        iCount = oCollection.Count
        # Add
        oNote = oCollection.Add("Label Note 1")
        Assert.assertIsNotNone(oNote)
        Assert.assertEqual("Label Note 1", oNote.Note)
        Assert.assertEqual((iCount + 1), oCollection.Count)
        # Add
        oNote = oCollection.Add("Label Note 2")
        Assert.assertIsNotNone(oNote)
        Assert.assertEqual("Label Note 2", oNote.Note)
        Assert.assertEqual((iCount + 2), oCollection.Count)
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.Count)

        iIndex = 0
        while iIndex < oCollection.Count:
            # Note, NoteVisible, LabelVisible
            self.m_logger.WriteLine9(
                "\tElement {3}: Note = {0}, NoteVisible = {1}, LabelVisible = {2}",
                oCollection[iIndex].Note,
                oCollection[iIndex].NoteVisible,
                oCollection[iIndex].LabelVisible,
                iIndex,
            )

            iIndex += 1

        # Remove
        self.m_logger.WriteLine3("Before Remove() the LabelNotes collection contains: {0} elements", oCollection.Count)
        oCollection.Remove((oCollection.Count - 1))
        self.m_logger.WriteLine3("After  Remove() the LabelNotes collection contains: {0} elements", oCollection.Count)
        Assert.assertEqual((iCount + 1), oCollection.Count)

        def action6():
            oCollection.Remove((oCollection.Count + 1))

        TryCatchAssertBlock.DoAssert("Remove() should not allow to remove invalid elements.", action6)
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.Count)
        for oElement in oCollection:
            self.m_logger.WriteLine8(
                "\tBefore: Note = {0}, NoteVisible = {1}, LabelVisible = {2}",
                oElement.Note,
                oElement.NoteVisible,
                oElement.LabelVisible,
            )
            # Note
            oElement.Note = "Modified Label Note"
            Assert.assertEqual("Modified Label Note", oElement.Note)
            # LabelVisible
            oElement.LabelVisible = True
            Assert.assertEqual(True, oElement.LabelVisible)
            # NoteVisible
            oElement.NoteVisible = AgENoteShowType.eNoteOn
            Assert.assertEqual(AgENoteShowType.eNoteOn, oElement.NoteVisible)
            oElement.NoteVisible = AgENoteShowType.eNoteIntervals
            Assert.assertEqual(AgENoteShowType.eNoteIntervals, oElement.NoteVisible)
            # Intervals
            oHelper = IntervalCollectionHelper(self.m_oUnits)
            oHelper.Run(oElement.Intervals, IntervalCollectionHelper.IntervalCollectionType.LabelNotes)
            # NoteVisible
            oElement.NoteVisible = AgENoteShowType.eNoteOff
            Assert.assertEqual(AgENoteShowType.eNoteOff, oElement.NoteVisible)

        self.m_logger.WriteLine("----- THE GRAPHICS LABELNOTES TEST ----- END -----")

    # endregion
