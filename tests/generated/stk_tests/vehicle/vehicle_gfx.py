from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from logger import *
from math2 import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


# region GfxRangeContoursHelper
class GfxRangeContoursHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "IGfxRangeContours"):
        self.m_logger.WriteLine("----- THE GRAPHICS RANGE CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # IsVisible
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oContours.is_visible)
        oContours.is_visible = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oContours.is_visible)
        Assert.assertFalse(oContours.is_visible)
        oContours.is_visible = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oContours.is_visible)
        Assert.assertTrue(oContours.is_visible)
        # IsFillVisible
        self.m_logger.WriteLine4("\tThe current IsFillVisible flag is: {0}", oContours.is_fill_visible)
        oContours.is_fill_visible = False
        self.m_logger.WriteLine4("\tThe new IsFillVisible flag is: {0}", oContours.is_fill_visible)
        Assert.assertFalse(oContours.is_fill_visible)

        def action1():
            oContours.fill_style = AgEFillStyle.eFillStyleHatch

        TryCatchAssertBlock.DoAssert("Should not allow to modify a readonly property.", action1)
        oContours.is_fill_visible = True
        self.m_logger.WriteLine4("\tThe new IsFillVisible flag is: {0}", oContours.is_fill_visible)
        Assert.assertTrue(oContours.is_fill_visible)
        # FillStyle
        self.m_logger.WriteLine6("\tThe current FillStyle is: {0}", oContours.fill_style)
        oContours.fill_style = AgEFillStyle.eFillStyleDiagonalHatch
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(AgEFillStyle.eFillStyleDiagonalHatch, oContours.fill_style)
        oContours.fill_style = AgEFillStyle.eFillStyleDiagonalStripe1
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(AgEFillStyle.eFillStyleDiagonalStripe1, oContours.fill_style)
        oContours.fill_style = AgEFillStyle.eFillStyleDiagonalStripe2
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(AgEFillStyle.eFillStyleDiagonalStripe2, oContours.fill_style)
        oContours.fill_style = AgEFillStyle.eFillStyleHatch
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(AgEFillStyle.eFillStyleHatch, oContours.fill_style)
        oContours.fill_style = AgEFillStyle.eFillStyleHorizontalStripe
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(AgEFillStyle.eFillStyleHorizontalStripe, oContours.fill_style)
        oContours.fill_style = AgEFillStyle.eFillStyleScreen
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(AgEFillStyle.eFillStyleScreen, oContours.fill_style)
        oContours.fill_style = AgEFillStyle.eFillStyleSolid
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(AgEFillStyle.eFillStyleSolid, oContours.fill_style)
        oContours.fill_style = AgEFillStyle.eFillStyleVerticalStripe
        self.m_logger.WriteLine6("\tThe new FillStyle is: {0}", oContours.fill_style)
        Assert.assertEqual(AgEFillStyle.eFillStyleVerticalStripe, oContours.fill_style)
        # NumOfDecimalDigits
        self.m_logger.WriteLine3("\tThe current NumOfDecimalDigits is: {0}", oContours.num_of_decimal_digits)
        oContours.num_of_decimal_digits = 7
        self.m_logger.WriteLine3("\tThe new NumOfDecimalDigits is: {0}", oContours.num_of_decimal_digits)
        Assert.assertEqual(7, oContours.num_of_decimal_digits)

        def action2():
            oContours.num_of_decimal_digits = 123

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action2)

        def action3():
            oContours.label_unit = "test"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action3)

        oContours.fill_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oContours.fill_translucency, delta=Math2.Epsilon12)

        availableUnits = oContours.available_label_units
        self.m_logger.WriteLine3("The available units contains {0} units.", Array.Length(availableUnits))
        unit: str
        for unit in availableUnits:
            self.m_logger.WriteLine(unit)
            oContours.label_unit = unit
            Assert.assertEqual(unit, oContours.label_unit)

        # set DistanceUnit
        self.m_logger.WriteLine5(
            "\tThe current DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        # LevelAttributes
        oLevels: "ILevelAttributeCollection" = oContours.level_attributes
        Assert.assertIsNotNone(oLevels)
        # Count
        self.m_logger.WriteLine3("\tThe Level Attribute Collection contains: {0} elements.", oLevels.count)
        # _NewEnum
        levelAttribute: "ILevelAttribute"
        # _NewEnum
        for levelAttribute in oLevels:
            self.m_logger.WriteLine10(
                "\t\tElement: Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.label_visible,
                levelAttribute.label_visible,
                levelAttribute.user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )

        # AddLevel
        self.m_logger.WriteLine3(
            "\tBefore AddLevel() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        oAdded: "ILevelAttribute" = oLevels.add_level(123.456)
        Assert.assertIsNotNone(oAdded)
        self.m_logger.WriteLine3(
            "\tAfter AddLevel() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        levelAttribute: "ILevelAttribute"
        for levelAttribute in oLevels:
            self.m_logger.WriteLine10(
                "\t\tElement: Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.label_visible,
                levelAttribute.label_visible,
                levelAttribute.user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )

        # Remove
        self.m_logger.WriteLine3(
            "\tBefore Remove() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        oLevels.remove((oLevels.count - 1))
        self.m_logger.WriteLine3(
            "\tAfter RemoveAt() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        # AddLevelRange
        oLevels.add_level_range(12.5, 34.5, 0.5)
        self.m_logger.WriteLine3(
            "\tAfter AddLevelRange() the Level Attribute Collection contains: {0} elements.", oLevels.count
        )
        if oLevels.count > 0:
            # Item
            levelAttribute: "ILevelAttribute" = oLevels[0]
            Assert.assertIsNotNone(levelAttribute)
            self.m_logger.WriteLine10(
                "\t\tElement (Before): Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.label_visible,
                levelAttribute.label_visible,
                levelAttribute.user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )
            levelAttribute.color = Color.FromArgb((levelAttribute.color._ToOLECOLOR() + 250))
            levelAttribute.line_style = AgELineStyle.eMDash
            levelAttribute.line_width = AgELineWidth.e2
            levelAttribute.level = float(levelAttribute.level) + 1.5
            levelAttribute.label_visible = not levelAttribute.label_visible
            levelAttribute.user_text_visible = True
            levelAttribute.user_text = "UserText test string"
            levelAttribute.label_angle = 15
            self.m_logger.WriteLine10(
                "\t\tElement (After): Level = {0}, Color = {1}, LineStyle = {2}, LineWidth = {3}, LabelVisible = {4}, UserTextVisible = {5}, UserText = {6}, LabelAngle = {7}",
                levelAttribute.level,
                levelAttribute.color,
                levelAttribute.line_style,
                levelAttribute.line_width,
                levelAttribute.label_visible,
                levelAttribute.label_visible,
                levelAttribute.user_text_visible,
                levelAttribute.user_text,
                levelAttribute.label_angle,
            )

            def action4():
                levelAttribute.label_angle = 1234

            TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action4)

        def action5():
            oLevels.add_level_range(12.34, 34.12, 0.2)

        TryCatchAssertBlock.DoAssert("Cannot set value out-of-range.", action5)

        # RemoveAll
        oLevels.remove_all()
        self.m_logger.WriteLine3("\tAfter RemoveAll() the Elevations Collection contains: {0} elements.", oLevels.count)
        Assert.assertEqual(0, oLevels.count)
        self.m_logger.WriteLine("----- THE GRAPHICS RANGE CONTOURS TEST ----- END -----")


# endregion


# region GfxLabelNoteHelper
class GfxLabelNoteHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oCollection: "ILabelNoteCollection"):
        self.m_logger.WriteLine("----- THE GRAPHICS LABELNOTES TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            self.m_logger.WriteLine9(
                "\tElement {0}: Note = {1}, NoteVisible = {2}, LabelVisible = {3}",
                iIndex,
                oCollection[iIndex].note,
                oCollection[iIndex].note_visible,
                oCollection[iIndex].label_visible,
            )

            iIndex += 1

        # Count
        iCount: int = oCollection.count
        # Add
        oNote: "ILabelNote" = oCollection.add("Label Note 1")
        Assert.assertIsNotNone(oNote)
        Assert.assertEqual("Label Note 1", oNote.note)
        Assert.assertEqual((iCount + 1), oCollection.count)
        # Add
        oNote = oCollection.add("Label Note 2")
        Assert.assertIsNotNone(oNote)
        Assert.assertEqual("Label Note 2", oNote.note)
        Assert.assertEqual((iCount + 2), oCollection.count)
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Note, NoteVisible, LabelVisible
            self.m_logger.WriteLine9(
                "\tElement {3}: Note = {0}, NoteVisible = {1}, LabelVisible = {2}",
                oCollection[iIndex].note,
                oCollection[iIndex].note_visible,
                oCollection[iIndex].label_visible,
                iIndex,
            )

            iIndex += 1

        # Remove
        self.m_logger.WriteLine3("Before Remove() the LabelNotes collection contains: {0} elements", oCollection.count)
        oCollection.remove((oCollection.count - 1))
        self.m_logger.WriteLine3("After  Remove() the LabelNotes collection contains: {0} elements", oCollection.count)
        Assert.assertEqual((iCount + 1), oCollection.count)

        def action6():
            oCollection.remove((oCollection.count + 1))

        TryCatchAssertBlock.DoAssert("Remove() should not allow to remove invalid elements.", action6)
        self.m_logger.WriteLine3("The LabelNotes collection contains: {0} elements.", oCollection.count)
        labelNote: "ILabelNote"
        for labelNote in oCollection:
            self.m_logger.WriteLine8(
                "\tBefore: Note = {0}, NoteVisible = {1}, LabelVisible = {2}",
                labelNote.note,
                labelNote.note_visible,
                labelNote.label_visible,
            )
            # Note
            labelNote.note = "Modified Label Note"
            Assert.assertEqual("Modified Label Note", labelNote.note)
            # LabelVisible
            labelNote.label_visible = True
            Assert.assertEqual(True, labelNote.label_visible)
            # NoteVisible
            labelNote.note_visible = AgENoteShowType.eNoteOn
            Assert.assertEqual(AgENoteShowType.eNoteOn, labelNote.note_visible)
            labelNote.note_visible = AgENoteShowType.eNoteIntervals
            Assert.assertEqual(AgENoteShowType.eNoteIntervals, labelNote.note_visible)
            # Intervals
            oHelper = IntervalCollectionHelper(self.m_oUnits)
            oHelper.Run(labelNote.intervals, IntervalCollectionHelper.IntervalCollectionType.LabelNotes)
            # NoteVisible
            labelNote.note_visible = AgENoteShowType.eNoteOff
            Assert.assertEqual(AgENoteShowType.eNoteOff, labelNote.note_visible)

        self.m_logger.WriteLine("----- THE GRAPHICS LABELNOTES TEST ----- END -----")

    # endregion
