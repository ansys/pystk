from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


# region VOMarkerHelper
class VOMarkerHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Test_IAgVOMarkerFile method
    def Test_IAgVOMarkerFile(self, oFile: "IVOMarkerFile"):
        oFile.filename = TestBase.PathCombine("STKData", "VO", "Markers", "Star.ppm")
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Markers", "Star.ppm"), oFile.filename)
        oFile.filename = TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm")
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm"), oFile.filename)

        def action1():
            oFile.filename = TestBase.PathCombine("STKData", "VO", "Markers", "Bogus.ppm")

        TryCatchAssertBlock.ExpectedException("does not exist", action1)

        Assert.assertEqual(
            Path.GetFullPath(TestBase.PathCombine(TestBase.GetSTKHomeDir(), "STKData", "VO", "Markers", "Ship.ppm")),
            Path.GetFullPath(oFile.file_path),
        )

        oFile.is_transparent = False
        Assert.assertFalse(oFile.is_transparent)
        oFile.is_transparent = True
        Assert.assertTrue(oFile.is_transparent)

        oFile.use_soft_transparency = False
        Assert.assertFalse(oFile.use_soft_transparency)
        oFile.use_soft_transparency = True
        Assert.assertTrue(oFile.use_soft_transparency)

    # endregion

    # region Run method
    def Run(self, oMarker: "IVOMarker", bIsVehicle: bool):
        Assert.assertIsNotNone(oMarker)

        oMarker.visible = False
        Assert.assertFalse(oMarker.visible)

        def action2():
            oMarker.angle = 1.23

        TryCatchAssertBlock.ExpectedException("read only", action2)

        def action3():
            oMarker.marker_type = AgEMarkerType.eImageFile

        TryCatchAssertBlock.ExpectedException("read only", action3)

        def action4():
            oMarker.orientation_mode = AgEVOMarkerOrientation.eVOMarkerOrientationAngle

        TryCatchAssertBlock.ExpectedException("read-only", action4)

        def action5():
            oMarker.pixel_size = 1

        TryCatchAssertBlock.ExpectedException("read-only", action5)

        def action6():
            oMarker.x_origin = 0

        TryCatchAssertBlock.ExpectedException("read-only", action6)
        # BUG86168 TryCatchAssertBlock.ExpectedException("read-only", delegate() { oMarker.YOrigin = 0; }); "Value does not fall within the expected range"

        oMarker.visible = True
        Assert.assertTrue(oMarker.visible)

        oMarker.marker_type = AgEMarkerType.eShape
        Assert.assertEqual(AgEMarkerType.eShape, oMarker.marker_type)

        oShape: "IVOMarkerShape" = clr.CastAs(oMarker.marker_data, IVOMarkerShape)
        Assert.assertIsNotNone(oShape)
        oShape.style = AgE3dMarkerShape.e3dShapeCircle
        Assert.assertEqual(AgE3dMarkerShape.e3dShapeCircle, oShape.style)
        oShape.style = AgE3dMarkerShape.e3dShapePoint
        Assert.assertEqual(AgE3dMarkerShape.e3dShapePoint, oShape.style)

        def action7():
            voMarkerFileX: "IVOMarkerFile" = clr.Convert(oMarker.marker_data, IVOMarkerFile)

        TryCatchAssertBlock.DoAssertInvalidCast(action7)

        oMarker.marker_type = (
            AgEMarkerType.eImageFile
        )  # This property will not be set to this enum. See below, and see helpstrings.
        oMarker.set_marker_image_file(
            TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm")
        )  # This will set the MarkerType to eImageFile

        Assert.assertEqual(AgEMarkerType.eImageFile, oMarker.marker_type)
        oFile: "IVOMarkerFile" = clr.CastAs(oMarker.marker_data, IVOMarkerFile)
        Assert.assertIsNotNone(oFile)
        self.Test_IAgVOMarkerFile(oFile)

        def action8():
            oShape = clr.Convert(oMarker.marker_data, IVOMarkerShape)

        TryCatchAssertBlock.DoAssertInvalidCast(action8)

        oMarker.pixel_size = 12
        Assert.assertEqual(12, oMarker.pixel_size)

        def action9():
            oMarker.pixel_size = 1234

        TryCatchAssertBlock.ExpectedException("invalid", action9)

        oMarker.x_origin = AgEVOMarkerOriginType.eRight
        Assert.assertEqual(AgEVOMarkerOriginType.eRight, oMarker.x_origin)

        def action10():
            oMarker.x_origin = AgEVOMarkerOriginType.eTop

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action10)

        oMarker.y_origin = AgEVOMarkerOriginType.eBottom
        Assert.assertEqual(AgEVOMarkerOriginType.eBottom, oMarker.y_origin)

        def action11():
            oMarker.y_origin = AgEVOMarkerOriginType.eLeft

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action11)

        oMarker.orientation_mode = AgEVOMarkerOrientation.eVOMarkerOrientationNone
        Assert.assertEqual(AgEVOMarkerOrientation.eVOMarkerOrientationNone, oMarker.orientation_mode)

        def action12():
            oMarker.angle = 1.23

        TryCatchAssertBlock.ExpectedException("read only", action12)
        if bIsVehicle:
            oMarker.orientation_mode = AgEVOMarkerOrientation.eVOMarkerOrientationFollowDirection
            Assert.assertEqual(AgEVOMarkerOrientation.eVOMarkerOrientationFollowDirection, oMarker.orientation_mode)

            oMarker.angle = 1.23456
            Assert.assertEqual(1.23456, oMarker.angle)

            def action13():
                oMarker.angle = 361

            TryCatchAssertBlock.ExpectedException("invalid", action13)

        else:

            def action14():
                oMarker.orientation_mode = AgEVOMarkerOrientation.eVOMarkerOrientationFollowDirection

            TryCatchAssertBlock.ExpectedException("Only supported for vehicle", action14)

        oMarker.orientation_mode = AgEVOMarkerOrientation.eVOMarkerOrientationAngle
        Assert.assertEqual(AgEVOMarkerOrientation.eVOMarkerOrientationAngle, oMarker.orientation_mode)

        oMarker.angle = 1.23456
        Assert.assertEqual(1.23456, oMarker.angle)

        def action15():
            oMarker.angle = 361

        TryCatchAssertBlock.ExpectedException("invalid", action15)


# endregion


# region VOModelHelper
class VOModelHelper(object):
    def __init__(self, root: "IStkObjectRoot", oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self._root: "IStkObjectRoot" = root
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oModel: "IVOModel"):
        Assert.assertIsNotNone(oModel)
        self.m_logger.WriteLine("VO Model test:")

        # Visible
        self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oModel.visible)
        oModel.visible = False
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oModel.visible)
        Assert.assertFalse(oModel.visible)

        def action16():
            oModel.scale_value = 3.3

        TryCatchAssertBlock.DoAssert("The Scale is readonly when Visible flag is False.", action16)

        def action17():
            oModel.model_type = AgEModelType.eModelFile

        TryCatchAssertBlock.DoAssert("The ModelType is readonly when Visible flag is False.", action17)

        oModel.visible = True
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oModel.visible)
        Assert.assertTrue(oModel.visible)
        # ScaleValue
        self.m_logger.WriteLine6("\tThe current Scale flag is: {0}", oModel.scale_value)
        oModel.scale_value = 3.33
        self.m_logger.WriteLine6("\tThe new Scale flag is: {0}", oModel.scale_value)
        Assert.assertEqual(3.33, oModel.scale_value)

        def action18():
            oModel.scale_value = -12.34

        TryCatchAssertBlock.DoAssert("Cannot set illegal ScaleValue (out of range)!", action18)

        # ModelType (File)
        self.m_logger.WriteLine6("\tThe current ModelType is: {0}", oModel.model_type)
        oModel.model_type = AgEModelType.eModelFile
        self.m_logger.WriteLine6("\tThe new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(AgEModelType.eModelFile, oModel.model_type)
        oModelFile: "IVOModelFile" = clr.CastAs(oModel.model_data, IVOModelFile)
        Assert.assertIsNotNone(oModelFile)
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "pegasus.mdl")
        Assert.assertEqual(TestBase.PathCombine("VO", "Models", "pegasus.mdl"), oModelFile.filename)
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.filename)

        def action19():
            oModelFile.filename = "sat.mdl"

        TryCatchAssertBlock.DoAssert("The Filename should not allow to set invalid filename.", action19)

        def action20():
            oModelFile.filename = ""

        TryCatchAssertBlock.DoAssert("The Filename should not allow to set invalid filename.", action20)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "satellite.dae")
        Assert.assertEqual(TestBase.PathCombine("VO", "Models", "satellite.dae"), oModelFile.filename)
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.filename)
        # FilePath
        Assert.assertEqual(TestBase.GetScenarioFile("VO", "Models", "satellite.dae"), oModelFile.file_path)

        # ModelType (List)
        oModel.model_type = AgEModelType.eModelList
        self.m_logger.WriteLine6("\tThe new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(AgEModelType.eModelList, oModel.model_type)
        oModelList: "IVOModelCollection" = clr.CastAs(oModel.model_data, IVOModelCollection)
        Assert.assertIsNotNone(oModelList)
        iSize: int = oModelList.count
        self.m_logger.WriteLine3("\t\tThe Model list collection contains: {0} elements", iSize)

        iIndex: int = 0
        while iIndex < iSize:
            self.m_logger.WriteLine8(
                "\t\t\tElement {0}: ModelFile = {1}, SwitchTime = {2}",
                iIndex,
                oModelList[iIndex].vo_model_file.file_path,
                oModelList[iIndex].switch_time,
            )

            iIndex += 1

        oModelList.add("1 Jan 2007 12:00:00.000", TestBase.GetScenarioFile("VO", "Models", "satellite.dae"))
        Assert.assertEqual(2, oModelList.count)
        oModelList.remove(1)
        Assert.assertEqual(1, oModelList.count)

        # set DateFormat
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DateFormat")
        self.m_logger.WriteLine5("\t\tThe current DateFormat is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DateFormat", "EpSec")
        self.m_logger.WriteLine5("\t\tThe new DateFormat is: {0}", self.m_oUnits.get_current_unit_abbrv("DateFormat"))
        Assert.assertEqual("EpSec", self.m_oUnits.get_current_unit_abbrv("DateFormat"))

        time: float = float(oModelList[0].switch_time)
        self.m_logger.WriteLine6("\t\tOriginal SwitchTime = {0}", oModelList[0].switch_time)
        self.m_logger.WriteLine6("\t\tDouble format SwitchTime = {0}", time)

        def action21():
            oModelList.add(oModelList[0].switch_time, oModelList[0].vo_model_file.file_path)

        TryCatchAssertBlock.DoAssert("The Add() method should not allow to add duplicated elements.", action21)
        oModelList.add((time + 1), oModelList[0].vo_model_file.file_path)
        iSize = oModelList.count
        self.m_logger.WriteLine3("\t\tThe Model list collection contains: {0} elements", iSize)

        iIndex: int = 0
        while iIndex < iSize:
            self.m_logger.WriteLine8(
                "\t\t\tElement {0}: ModelFile = {1}, SwitchTime = {2}",
                iIndex,
                oModelList[iIndex].vo_model_file.file_path,
                oModelList[iIndex].switch_time,
            )

            iIndex += 1

        if iSize > 1:
            oModelList.remove(0)
            self.m_logger.WriteLine3("\t\tAfter Remove(0) the ModelList contains: {0} elements", oModelList.count)
            oItem: "IVOModelItem"
            for oItem in oModelList:
                self.m_logger.WriteLine7(
                    "\t\t\tElement (before modification): ModelFile = {0}, SwitchTime = {1}",
                    oItem.vo_model_file.file_path,
                    oItem.switch_time,
                )
                oItem.vo_model_file.filename = oItem.vo_model_file.filename
                oItem.switch_time = time - 12
                self.m_logger.WriteLine7(
                    "\t\t\tElement (after modification): ModelFile = {0}, SwitchTime = {1}",
                    oItem.vo_model_file.file_path,
                    oItem.switch_time,
                )

                voModelFile: "IVOModelFile" = oItem.vo_model_file
                Assert.assertEqual((TestBase.PathCombine("VO", "Models", "satellite.dae")), voModelFile.filename)
                Assert.assertTrue((TestBase.PathCombine("VO", "Models", "satellite.dae") in voModelFile.file_path))
                voModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "pegasus.mdl")
                Assert.assertEqual(TestBase.PathCombine("VO", "Models", "pegasus.mdl"), voModelFile.filename)
                Assert.assertTrue((TestBase.PathCombine("VO", "Models", "pegasus.mdl") in voModelFile.file_path))

                def action22():
                    voModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "bogus.dae")

                TryCatchAssertBlock.ExpectedException("file does not exist", action22)

        # restore DateFormat
        self.m_oUnits.set_current_unit("DateFormat", strUnit)
        self.m_logger.WriteLine5("\t\tThe new DateFormat (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DateFormat"))

        # DetailThreshold test
        self.VODetailThreshold(oModel.detail_threshold)

        # Articulation test
        self.VOArticulation(oModel.articulation)

        # ------------------------------------------------------------
        # Testing the behavior of the object's model when
        # the graphics updates have been suspended using BeginUpdate.
        # The expected behavior is for the Object Model to silently
        # load the specified model even if the BeginUpdate was
        # invoked. This way the users do not have to call EndUpdate
        # after setting a new model to set desired articulations.
        # ------------------------------------------------------------
        oModel.model_type = AgEModelType.eModelFile
        Assert.assertTrue((oModel.model_type == AgEModelType.eModelFile))
        oldModel: str = (clr.CastAs(oModel.model_data, IVOModelFile)).filename
        self._root.begin_update()
        try:
            oModel.model_type = AgEModelType.eModelFile
            modelFile: "IVOModelFile" = clr.CastAs(oModel.model_data, IVOModelFile)
            modelFile.filename = "\\STKData\\VO\\Models\\Space\\hubble.mdl"

            oModel.articulation.set_trans_value(0, "HGA_Arm_1", "Fold", 90)

        finally:
            self._root.end_update()

        oModel.model_type = AgEModelType.eModelList
        modelList: "IVOModelCollection" = clr.CastAs(oModel.model_data, IVOModelCollection)
        while modelList.count > 1:
            modelList.remove((modelList.count - 1))
        modelList[0].vo_model_file.filename = oldModel

        def action23():
            oModel.articulation.set_trans_value(0, "HGA_Arm_1", "Fold", 90)

        TryCatchAssertBlock.DoAssert("Must not allow setting invalid articulations.", action23)

        self._root.begin_update()
        try:
            modelList[0].vo_model_file.filename = "\\STKData\\VO\\Models\\Space\\hubble.mdl"
            oModel.articulation.set_trans_value(0, "HGA_Arm_1", "Fold", 90)

        finally:
            self._root.end_update()
            oModel.model_type = AgEModelType.eModelFile

    # endregion

    # region VODetailThreshold
    def VODetailThreshold(self, oDetail: "IVODetailThreshold"):
        Assert.assertIsNotNone(oDetail)
        self.m_logger.WriteLine("VO DetailThreshold test:")
        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # EnableDetailThreshold
        self.m_logger.WriteLine4("\tThe current EnableDetailThreshold flag is: {0}", oDetail.enable_detail_threshold)
        oDetail.enable_detail_threshold = False
        self.m_logger.WriteLine4("\tThe new EnableDetailThreshold flag is: {0}", oDetail.enable_detail_threshold)
        Assert.assertEqual(False, oDetail.enable_detail_threshold)
        bCaught: bool = False
        try:
            bCaught = False
            oDetail.all = 2.2

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The ModelDetail is readonly when Enable flag is False.")

        try:
            bCaught = False
            oDetail.marker_label = 3.3

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The MarkerLabel is readonly when Enable flag is False.")

        try:
            bCaught = False
            oDetail.marker = 4.4

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Marker is readonly when Enable flag is False.")

        try:
            bCaught = False
            oDetail.all = 5.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The ModelDetail is readonly when Enable flag is False.")

        try:
            bCaught = False
            oDetail.point = 6.6

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Point Detail is readonly when Enable flag is False.")

        oDetail.enable_detail_threshold = True
        self.m_logger.WriteLine4("\tThe new EnableDetailThreshold flag is: {0}", oDetail.enable_detail_threshold)
        Assert.assertEqual(True, oDetail.enable_detail_threshold)
        # Marker
        self.m_logger.WriteLine6("\t\tThe current Marker is: {0}", oDetail.marker)
        oDetail.marker = 99.99
        self.m_logger.WriteLine6("\t\tThe new Marker is: {0}", oDetail.marker)
        Assert.assertEqual(99.99, oDetail.marker)
        try:
            bCaught = False
            oDetail.marker = -2.2

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal Marker value!")

        # MarkerLabel
        self.m_logger.WriteLine6("\t\tThe current Marker Label is: {0}", oDetail.marker_label)
        oDetail.marker_label = 88.88
        self.m_logger.WriteLine6("\t\tThe new Marker Label is: {0}", oDetail.marker_label)
        Assert.assertEqual(88.88, oDetail.marker_label)
        try:
            bCaught = False
            oDetail.marker_label = -3.3

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal MarkerLabel value!")

        # ModelLabel
        self.m_logger.WriteLine6("\t\tThe current Model Label is: {0}", oDetail.model_label)
        oDetail.model_label = 77.77
        self.m_logger.WriteLine6("\t\tThe new Model Label is: {0}", oDetail.model_label)
        Assert.assertAlmostEqual(77.77, oDetail.model_label, delta=0.001)
        try:
            bCaught = False
            oDetail.model_label = -4.4

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal ModelLabel value!")

        # All
        self.m_logger.WriteLine6("\t\tThe current Model Detail is: {0}", oDetail.all)
        oDetail.all = 66.66
        self.m_logger.WriteLine6("\t\tThe new Model Detail is: {0}", oDetail.all)
        Assert.assertEqual(66.66, oDetail.all)
        try:
            bCaught = False
            oDetail.all = -5.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal All value!")

        # Point
        self.m_logger.WriteLine6("\t\tThe current Point Detail is: {0}", oDetail.point)
        oDetail.point = 55.55
        self.m_logger.WriteLine6("\t\tThe new Point Detail is: {0}", oDetail.point)
        Assert.assertEqual(55.55, oDetail.point)
        try:
            bCaught = False
            oDetail.point = -6.6

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal Point value!")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region VOArticulation
    def VOArticulation(self, oArticulation: "IVOModelArtic"):
        Assert.assertIsNotNone(oArticulation)

        oArticulation.enable_default_save = False
        Assert.assertEqual(False, oArticulation.enable_default_save)
        oArticulation.enable_default_save = True
        Assert.assertEqual(True, oArticulation.enable_default_save)

        oArticulation.save_artic_file_on_save = False
        Assert.assertEqual(False, oArticulation.save_artic_file_on_save)
        oArticulation.save_artic_file_on_save = True
        Assert.assertEqual(True, oArticulation.save_artic_file_on_save)

        oArticulation.save_artic_file_on_save = False
        Assert.assertEqual(False, oArticulation.save_artic_file_on_save)
        oArticulation.save_artic_file_on_save = True
        Assert.assertEqual(True, oArticulation.save_artic_file_on_save)

        oArticulation.use_object_color_for_model = False
        Assert.assertFalse(oArticulation.use_object_color_for_model)
        oArticulation.use_object_color_for_model = True
        Assert.assertTrue(oArticulation.use_object_color_for_model)

        articFile: "IVOArticulationFile" = oArticulation.vo_articulation_file
        oArticulation.use_articulation_file = False

        def action24():
            articFile.filename = TestBase.GetScenarioFile("Test.sama")

        TryCatchAssertBlock.ExpectedException("read-only", action24)

        oArticulation.use_articulation_file = True

        def action25():
            articFile.filename = TestBase.GetScenarioFile("Bogus.sama")

        TryCatchAssertBlock.ExpectedException("not found", action25)

        articFile.filename = TestBase.GetScenarioFile("Test.sama")
        Assert.assertTrue(("Test.sama" in articFile.filename))

        articFile.reload()

        # LODs test
        self.m_logger.WriteLine3("\tThe number of LODs is: {0}", oArticulation.lod_count)

        iIndex: int = 0
        while iIndex < oArticulation.lod_count:
            self.m_logger.WriteLine3("\t\tLODs: {0}", iIndex)
            arAvailableArtic = oArticulation.get_available_articulations(iIndex)
            self.m_logger.WriteLine3("\t\t\tThere are {0} available Articulations.", Array.Length(arAvailableArtic))

            i: int = 0
            while i < Array.Length(arAvailableArtic):
                strArtic: str = str(arAvailableArtic[i])
                self.m_logger.WriteLine7("\t\t\t\tArticulation {0} is: {1}", i, strArtic)
                # TransCollection test
                oTransformations: "IVOModelTransformationCollection" = oArticulation.get_available_transformations(
                    iIndex, strArtic
                )
                Assert.assertIsNotNone(oTransformations)
                self.m_logger.WriteLine5("\t\t\t\tTransformation name is: {0}.", oTransformations.name)
                self.m_logger.WriteLine3("\t\t\t\tThere are {0} available Transformations.", oTransformations.count)

                j: int = 0
                while j < oTransformations.count:
                    modelTrans: "IVOModelTransformation" = oTransformations[j]
                    strTrans: str = modelTrans.name
                    self.m_logger.WriteLine7("\t\t\t\t\tTransformation {0} is: {1}", j, strTrans)
                    self.m_logger.WriteLine8(
                        "\t\t\t\t\t\tCurrent value: {0} [Min = {1}, Max = {2}]",
                        modelTrans.value,
                        modelTrans.min,
                        modelTrans.max,
                    )
                    dMax: float = (
                        modelTrans.max if ((Math.Abs(modelTrans.max) > Math.Abs(modelTrans.min))) else modelTrans.min
                    )
                    dMin: float = (
                        modelTrans.max if ((Math.Abs(modelTrans.max) < Math.Abs(modelTrans.min))) else modelTrans.min
                    )
                    dMidle: float = ((dMax - dMin)) / 2.0
                    modelTrans.value = dMidle
                    oArticulation.set_trans_value(iIndex, strArtic, strTrans, dMidle)
                    self.m_logger.WriteLine6(
                        "\t\t\t\t\t\tNew value: {0}", oArticulation.get_trans_value(iIndex, strArtic, strTrans)
                    )
                    Assert.assertEqual(dMidle, oArticulation.get_trans_value(iIndex, strArtic, strTrans))
                    bCaught: bool = False
                    try:
                        bCaught = False
                        modelTrans.value = dMax * 2
                        self.m_logger.WriteLine6("\t\t\t\t\t\tNew value (illegal): {0}", modelTrans.value)

                    except Exception as e:
                        bCaught = True
                        self.m_logger.WriteLine5("\t\t\t\t\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set illegal value (out of range)!")

                    j += 1

                # Collection enumeration test
                oItem: "IVOModelTransformation"
                # Collection enumeration test
                for oItem in oTransformations:
                    Assert.assertIsNotNone(oItem)

                i += 1

            iIndex += 1


# endregion


# region VOTargetModelHelper
class VOTargetModelHelper(object):
    def __init__(self, root: "IStkObjectRoot", oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self._root: "IStkObjectRoot" = root
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oModel: "IPointTargetVOModel"):
        Assert.assertIsNotNone(oModel)
        # IsPointVisible (false)
        self.m_logger.WriteLine4("\tThe current IsPointVisible is: {0}", oModel.is_point_visible)
        oModel.is_point_visible = False
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.is_point_visible)
        Assert.assertEqual(False, oModel.is_point_visible)

        def action26():
            oModel.point_size = 12.3456

        # PointSize
        TryCatchAssertBlock.DoAssert("Allows to modify a readonly property!", action26)
        # IsPointVisible (true)
        oModel.is_point_visible = True
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.is_point_visible)
        Assert.assertEqual(True, oModel.is_point_visible)
        # PointSize
        self.m_logger.WriteLine6("\tThe current PointSize is: {0}", oModel.point_size)
        oModel.point_size = 12.3456
        self.m_logger.WriteLine6("\tThe new PointSize is: {0}", oModel.point_size)
        Assert.assertAlmostEqual(12.3456, float(oModel.point_size), delta=0.0001)

        def action27():
            oModel.point_size = 123.456

        TryCatchAssertBlock.DoAssert("Allows to set illegal value!", action27)

        def action28():
            oModel.gltf_reflection_map_type = AgEModelGltfReflectionMapType.eModelGltfProceduralEnvironment

        # GLTF

        TryCatchAssertBlock.ExpectedException("glTF settings are not available", action28)
        (
            clr.CastAs(oModel.model_data, IVOModelFile)
        ).filename = r"STKData\VO\Models\Land\facility.glb"  # need a model that supports GLTF
        oModel.gltf_reflection_map_type = AgEModelGltfReflectionMapType.eModelGltfProceduralEnvironment
        Assert.assertEqual(
            AgEModelGltfReflectionMapType.eModelGltfProceduralEnvironment, oModel.gltf_reflection_map_type
        )

        def action29():
            x: "IVOModelGltfImageBased" = oModel.gltf_image_based

        TryCatchAssertBlock.ExpectedException("is not set to Image Based", action29)

        oModel.gltf_reflection_map_type = AgEModelGltfReflectionMapType.eModelGltfImageBased
        Assert.assertEqual(AgEModelGltfReflectionMapType.eModelGltfImageBased, oModel.gltf_reflection_map_type)

        gltfImageBased: "IVOModelGltfImageBased" = oModel.gltf_image_based
        gltfImageBased.filename = TestBase.GetScenarioFile("over_the_clouds.hdr")
        Assert.assertEqual("over_the_clouds.hdr", gltfImageBased.filename)
        Assert.assertTrue(("over_the_clouds.hdr" in gltfImageBased.file_path))

        gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 ICRF"
        Assert.assertEqual("Satellite/Satellite1 ICRF", gltfImageBased.reflection_reference_frame)

        def action30():
            gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 Bogus"

        TryCatchAssertBlock.ExpectedException("Invalid", action30)

        # Base class properties test
        oModelHelper = VOModelHelper(self._root, self.m_oUnits)
        oModelHelper.Run(oModel)


# endregion


# region VOModelPointingHelper
class VOModelPointingHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oModelPointing: "IVOModelPointing"):
        self.m_logger.WriteLine("----- THE VO MODEL POINTING TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oModelPointing)
        # PointableElements
        oPECollection: "IVOPointableElementsCollection" = oModelPointing.pointable_elements
        Assert.assertIsNotNone(oPECollection)
        # Count
        self.m_logger.WriteLine3("The Pointable Elements collection contains: {0} elements", oPECollection.count)

        iIndex: int = 0
        while iIndex < oPECollection.count:
            # Index
            self.m_logger.WriteLine5("\tElement: {0}", oPECollection[iIndex].pointing_name)

            iIndex += 1

        self.m_logger.WriteLine3("The Pointable Elements collection contains: {0} elements.", oPECollection.count)

        iIndex: int = 0
        while iIndex < oPECollection.count:
            pointableElementsElement: "IVOPointableElementsElement" = oPECollection[iIndex]
            Assert.assertIsNotNone(pointableElementsElement)
            self.m_logger.WriteLine7("\tElement {0} is: {1}", iIndex, pointableElementsElement.pointing_name)

            def action31():
                pointableElementsElement.pointing_name = "NewName"

            TryCatchAssertBlock.DoAssert("The PointingName should be readonly!", action31)

            oHelper = LinkToObjectHelper()
            oHelper.Run(pointableElementsElement.assigned_target_object, pointableElementsElement.pointing_name)

            iIndex += 1

        # Add
        self.m_logger.WriteLine3("The Pointable Elements collection still contains: {0} elements", oPECollection.count)

        iIndex: int = 0
        while iIndex < oPECollection.count:
            self.m_logger.WriteLine5("\tElement: {0}", oPECollection[iIndex].pointing_name)

            iIndex += 1

        def action32():
            oNewElement: "IVOPointableElementsElement" = oPECollection.add()

        TryCatchAssertBlock.DoAssert("The PointableElementsCollection should be readonly!", action32)

        def action33():
            oPECollection.remove_at(0)

        # RemoveAt
        TryCatchAssertBlock.DoAssert("The PointableElementsCollection should be readonly!", action33)

        def action34():
            oPECollection.remove_all()

        # RemoveAll
        TryCatchAssertBlock.DoAssert("The PointableElementsCollection should be readonly!", action34)
        self.m_logger.WriteLine3("The Pointable Elements collection still contains: {0} elements", oPECollection.count)
        oTempElement: "IVOPointableElementsElement"
        for oTempElement in oPECollection:
            self.m_logger.WriteLine5("\tElement: {0}", oTempElement.pointing_name)

        # Testing model pointing intervals
        Assert.assertTrue((oPECollection.count > 0))
        oTempElement: "IVOPointableElementsElement"
        for oTempElement in oPECollection:
            oTempElement.intervals.remove_all()
            Assert.assertEqual(
                0,
                oTempElement.intervals.count,
                (('Failed to clear intervals for the element "' + oTempElement.pointing_name) + '"'),
            )

        # Planet Target
        sPlanetTargetObject: str = "Planet/MarsJPL"

        # Verify that we can add intervals to existing pointable elements
        oTempElement: "IVOPointableElementsElement"

        # Verify that we can add intervals to existing pointable elements
        for oTempElement in oPECollection:
            # need to use a full path
            self.m_logger.WriteLine(oTempElement.pointing_name)
            oTempElement.assigned_target_object.bind_to(sPlanetTargetObject)
            Assert.assertEqual(sPlanetTargetObject, oTempElement.assigned_target_object.name)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.assigned_target_object.name)
            # Intervals
            nCount: int = oTempElement.intervals.count
            self.m_logger.WriteLine3("\t\tThe current number of intervals: {0}", nCount)
            oTempElement.intervals.add("1 Jul 1999 01:00:000.00", "1 Jul 1999 02:00:000.00")
            Assert.assertEqual((nCount + 1), oTempElement.intervals.count)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.intervals.count)
            self.PrintIntervals(oTempElement.intervals)
            oTempElement.intervals.add("1 Jul 1999 03:00:000.00", "1 Jul 1999 04:00:000.00")
            Assert.assertEqual((nCount + 2), oTempElement.intervals.count)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.intervals.count)
            self.PrintIntervals(oTempElement.intervals)

            def action35():
                oTempElement.intervals.add("1 Jul 1999 03:00:000.00", "1 Jul 1999 01:00:000.00")

            TryCatchAssertBlock.DoAssert("Should not allow to set illegal time interval!", action35)

        # adding a Sun target
        iCount: int = oPECollection.count
        oModelPointing.add_interval(
            oPECollection[0].pointing_name, "Sun", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
        )
        Assert.assertEqual((iCount + 1), oPECollection.count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.count)
        oTempElement: "IVOPointableElementsElement"
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.pointing_name)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.assigned_target_object.name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.intervals.count)
            self.PrintIntervals(oTempElement.intervals)

        def action36():
            oModelPointing.add_interval(
                "WrongPointingName", "Sun", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
            )

        TryCatchAssertBlock.DoAssert("Should not allow to set illegal interval!", action36)

        def action37():
            oModelPointing.add_interval(
                oPECollection[2].pointing_name, "WrongTargetName", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
            )

        TryCatchAssertBlock.DoAssert("Should not allow to set illegal interval!", action37)

        def action38():
            oModelPointing.add_interval(
                oPECollection[2].pointing_name, "Earth", "3 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
            )

        TryCatchAssertBlock.DoAssert("Should not allow to set illegal interval!", action38)

        # adding a Slew Interval target
        iCount = oPECollection.count
        oModelPointing.add_interval(
            oPECollection[1].pointing_name, "Slew", "1 Jul 1999 02:00:000.00", "1 Jul 1999 03:00:000.00"
        )
        Assert.assertEqual((iCount + 1), oPECollection.count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.count)
        oTempElement: "IVOPointableElementsElement"
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.pointing_name)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.assigned_target_object.name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.intervals.count)
            self.PrintIntervals(oTempElement.intervals)

        # RemoveInterval
        oModelPointing.remove_interval(oPECollection[1].pointing_name, "Slew")
        Assert.assertEqual(iCount, oPECollection.count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.count)
        oTempElement: "IVOPointableElementsElement"
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.pointing_name)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.assigned_target_object.name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.intervals.count)
            self.PrintIntervals(oTempElement.intervals)

        def action39():
            oModelPointing.remove_interval("WrongPointingName", "Sun")

        TryCatchAssertBlock.DoAssert("Should not allow to remove illegal interval!", action39)

        def action40():
            oModelPointing.remove_interval(oPECollection[2].pointing_name, "WrongTargetName")

        TryCatchAssertBlock.DoAssert("Should not allow to remove illegal interval!", action40)

        def action41():
            oModelPointing.remove_interval(oPECollection[1].pointing_name, "Earth")

        TryCatchAssertBlock.DoAssert("Should not allow to remove illegal interval!", action41)

        # Sort
        oPECollection.sort()

        availObjects = oModelPointing.pointable_elements[0].assigned_target_object.available_objects
        availObject: str
        for availObject in availObjects:
            self.m_logger.WriteLine5("Available target: {0}", availObject)
            Assert.assertTrue((not ("Slew" == availObject)))

        oModelPointing.pointable_elements[0].intervals.remove_all()

        i: int = 0
        while i < oModelPointing.pointable_elements.count:
            oModelPointing.pointable_elements[i].intervals.remove_all()

            i += 1

        oModelPointing.load_intervals(
            TestBase.GetScenarioFile("MdlPtgInts.int"), oModelPointing.pointable_elements[0].pointing_name
        )

        i: int = 0
        while i < oModelPointing.pointable_elements.count:
            self.m_logger.WriteLine(oModelPointing.pointable_elements[i].pointing_name)
            self.m_logger.WriteLine(oModelPointing.pointable_elements[i].assigned_target_object.name)
            self.PrintIntervals(oModelPointing.pointable_elements[i].intervals)

            i += 1

        def action42():
            oModelPointing.load_intervals(
                TestBase.GetScenarioFile("MdlPtgIntsBad.int"), oModelPointing.pointable_elements[0].pointing_name
            )

        TryCatchAssertBlock.DoAssert("This file is invalid and should throw an exception.", action42)

        self.m_logger.WriteLine("----- THE VO MODEL POINTING TEST ----- END -----")

    # endregion

    # region PrintIntervals method
    def PrintIntervals(self, oCollection: "IIntervalCollection"):
        iIndex: int = 0
        while iIndex < oCollection.count:
            oStart: typing.Any = None
            oStop: typing.Any = None

            (oStart, oStop) = oCollection.get_interval(iIndex)
            self.m_logger.WriteLine8("\t\t\tInterval {0}: StartTime = {1}, StopTime = {2}", iIndex, oStart, oStop)

            iIndex += 1


# endregion


# region VOOffsetsHelper
class VOOffsetsHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oOffset: "IVOOffset"):
        self.m_logger.WriteLine("----- THE VO OFFSET TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oOffset)

        # Rotational
        oRHelper = VOOffsetRotationalHelper(self.m_oUnits)
        oRHelper.Run(oOffset.rotational)

        # Translational
        oTHelper = VOOffsetTranslationalHelper(self.m_oUnits)
        oTHelper.Run(oOffset.translational)

        # Label
        oLHelper = VOOffsetLabelHelper(self.m_oUnits)
        oLHelper.Run(oOffset.label, False)

        # Attach Point
        oAHelper = VOOffsetAttachHelper()
        oAHelper.Run(oOffset.attach_point)

        self.m_logger.WriteLine("----- THE VO OFFSET TEST ----- END -----")


# endregion


# region VOOffsetRotationalHelper
class VOOffsetRotationalHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oRotational: "IVOOffsetRotate"):
        Assert.assertIsNotNone(oRotational)
        self.m_logger.WriteLine("Offsets Rotational test:")
        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # Enable flag
        self.m_logger.WriteLine4("\tThe current Enable flag is: {0}", oRotational.enable)
        oRotational.enable = False
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oRotational.enable)
        Assert.assertEqual(False, oRotational.enable)
        bCaught: bool = False
        try:
            bCaught = False
            oRotational.x = 2.3456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The X should be readonly when Enable flag is False.")

        try:
            bCaught = False
            oRotational.y = 1.234

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Y should be readonly when Enable flag is False.")

        try:
            bCaught = False
            oRotational.z = -1.234

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Z should be readonly when Enable flag is False.")

        oRotational.enable = True
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oRotational.enable)
        Assert.assertEqual(True, oRotational.enable)
        # X
        self.m_logger.WriteLine6("\t\tThe current X is: {0}", oRotational.x)
        oRotational.x = 2.3456
        self.m_logger.WriteLine6("\t\tThe new X is: {0}", oRotational.x)
        Assert.assertEqual(2.3456, oRotational.x)
        # Y
        self.m_logger.WriteLine6("\t\tThe current Y is: {0}", oRotational.y)
        oRotational.y = -1.23456
        self.m_logger.WriteLine6("\t\tThe new Y is: {0}", oRotational.y)
        Assert.assertEqual(-1.23456, oRotational.y)
        # Z
        self.m_logger.WriteLine6("\t\tThe current Z is: {0}", oRotational.z)
        oRotational.z = 1.234
        self.m_logger.WriteLine6("\t\tThe new Z is: {0}", oRotational.z)
        Assert.assertEqual(1.234, oRotational.z)
        # ranges test
        try:
            bCaught = False
            oRotational.x = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The X should not allow to set values > 180 deg.")

        try:
            bCaught = False
            oRotational.y = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Y should not allow to set values < -180 deg.")

        try:
            bCaught = False
            oRotational.z = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Z should not allow to set values > 180 deg.")

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))


# endregion


# region VOOffsetTranslationalHelper
class VOOffsetTranslationalHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oTranslational: "IVOOffsetTransformation"):
        Assert.assertIsNotNone(oTranslational)
        self.m_logger.WriteLine("Offsets Translational test:")
        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # Enable flag
        self.m_logger.WriteLine4("\tThe current Enable flag is: {0}", oTranslational.enable)
        oTranslational.enable = False
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oTranslational.enable)
        Assert.assertEqual(False, oTranslational.enable)
        bCaught: bool = False
        try:
            bCaught = False
            oTranslational.x = 34.56

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The X should be readonly when Enable flag is False.")

        try:
            bCaught = False
            oTranslational.y = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Y should be readonly when Enable flag is False.")

        try:
            bCaught = False
            oTranslational.z = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Z should be readonly when Enable flag is False.")

        oTranslational.enable = True
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oTranslational.enable)
        Assert.assertEqual(True, oTranslational.enable)
        # X
        self.m_logger.WriteLine6("\t\tThe current X is: {0}", oTranslational.x)
        oTranslational.x = 123.456
        self.m_logger.WriteLine6("\t\tThe new X is: {0}", oTranslational.x)
        Assert.assertEqual(123.456, oTranslational.x)
        # Y
        self.m_logger.WriteLine6("\t\tThe current Y is: {0}", oTranslational.y)
        oTranslational.y = -123.456
        self.m_logger.WriteLine6("\t\tThe new Y is: {0}", oTranslational.y)
        Assert.assertEqual(-123.456, oTranslational.y)
        # Z
        self.m_logger.WriteLine6("\t\tThe current Z is: {0}", oTranslational.z)
        oTranslational.z = 23.4
        self.m_logger.WriteLine6("\t\tThe new Z is: {0}", oTranslational.z)
        Assert.assertEqual(23.4, oTranslational.z)
        # ranges test
        try:
            bCaught = False
            oTranslational.x = 123456789000000

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The X should not allow to set values > 1000000 km.")

        try:
            bCaught = False
            oTranslational.y = -123456789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Y should not allow to set values < -1000000 km.")

        try:
            bCaught = False
            oTranslational.z = 123456789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Z should not allow to set values > 1000000 km.")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))


# endregion


# region VOOffsetLabelHelper
class VOOffsetLabelHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oLabel: "IVOOffsetLabel", bReadOnly: bool):
        self.m_logger.WriteLine("----- VO OFFSET LABEL ----- BEGIN -----")
        Assert.assertIsNotNone(oLabel)
        # set SmallDistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit")
        self.m_logger.WriteLine5("\tThe current SmallDistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("SmallDistanceUnit", "in")
        self.m_logger.WriteLine5(
            "\tThe new SmallDistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit")
        )
        Assert.assertEqual("in", self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit"))
        # bReadOnly
        self.m_logger.WriteLine4("\tRead-only flag: {0}", bReadOnly)
        if bReadOnly:

            def action43():
                oLabel.enable = False

            # Enable
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action43)

            def action44():
                oLabel.offset_frame = AgEOffsetFrameType.eOffsetFrameCartesian

            # OffsetFrame
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action44)

            def action45():
                oLabel.x = 10.1

            # X
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action45)

            def action46():
                oLabel.y = 11.11

            # Y
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action46)

            def action47():
                oLabel.z = 12.12

            # Z
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action47)

        else:
            # Enable (false)
            self.m_logger.WriteLine4("\t\tThe current Enable is: {0}", oLabel.enable)
            oLabel.enable = False
            self.m_logger.WriteLine4("\t\tThe new Enable is: {0}", oLabel.enable)
            Assert.assertEqual(False, oLabel.enable)

            def action48():
                oLabel.offset_frame = AgEOffsetFrameType.eOffsetFrameCartesian

            # OffsetFrame
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action48)

            def action49():
                oLabel.x = 10.1

            # X
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action49)

            def action50():
                oLabel.y = 11.11

            # Y
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action50)

            def action51():
                oLabel.z = 12.12

            # Z
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action51)
            # Enable (true)
            oLabel.enable = True
            self.m_logger.WriteLine4("\t\tThe new Enable is: {0}", oLabel.enable)
            Assert.assertEqual(True, oLabel.enable)
            # OffsetFrame (Cartesian)
            self.m_logger.WriteLine6("\t\t\tThe current OffsetFrame is: {0}", oLabel.offset_frame)
            oLabel.offset_frame = AgEOffsetFrameType.eOffsetFrameCartesian
            self.m_logger.WriteLine6("\t\t\tThe new OffsetFrame is: {0}", oLabel.offset_frame)
            Assert.assertEqual(AgEOffsetFrameType.eOffsetFrameCartesian, oLabel.offset_frame)
            # X
            self.m_logger.WriteLine6("\t\t\t\tThe current X is: {0}", oLabel.x)
            oLabel.x = 10.1
            self.m_logger.WriteLine6("\t\t\t\tThe new X is: {0}", oLabel.x)
            Assert.assertAlmostEqual(10.1, oLabel.x, delta=0.01)

            def action52():
                oLabel.x = 12340000000000000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action52)
            # Y
            self.m_logger.WriteLine6("\t\t\t\tThe current Y is: {0}", oLabel.y)
            oLabel.y = 11.11
            self.m_logger.WriteLine6("\t\t\t\tThe new Y is: {0}", oLabel.y)
            Assert.assertAlmostEqual(11.11, oLabel.y, delta=0.001)

            def action53():
                oLabel.y = -34120000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action53)
            # Z
            self.m_logger.WriteLine6("\t\t\t\tThe current Z is: {0}", oLabel.z)
            oLabel.z = 12.12
            self.m_logger.WriteLine6("\t\t\t\tThe new Z is: {0}", oLabel.z)
            Assert.assertAlmostEqual(12.12, oLabel.z, delta=0.001)

            def action54():
                oLabel.z = 210900000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action54)
            # OffsetFrame (Pixel)
            oLabel.offset_frame = AgEOffsetFrameType.eOffsetFramePixel
            self.m_logger.WriteLine6("\t\t\tThe new OffsetFrame is: {0}", oLabel.offset_frame)
            Assert.assertEqual(AgEOffsetFrameType.eOffsetFramePixel, oLabel.offset_frame)
            # X
            self.m_logger.WriteLine6("\t\t\t\tThe current X is: {0}", oLabel.x)
            oLabel.x = 13.13
            self.m_logger.WriteLine6("\t\t\t\tThe new X is: {0}", oLabel.x)
            Assert.assertAlmostEqual(13.13, oLabel.x, delta=0.001)

            def action55():
                oLabel.x = 12340000000000000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action55)
            # Y
            self.m_logger.WriteLine6("\t\t\t\tThe current Y is: {0}", oLabel.y)
            oLabel.y = 14.14
            self.m_logger.WriteLine6("\t\t\t\tThe new Y is: {0}", oLabel.y)
            Assert.assertAlmostEqual(14.14, oLabel.y, delta=0.001)

            def action56():
                oLabel.y = -34120000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action56)

            def action57():
                oLabel.z = 15.15

            # Z
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action57)

        # restore SmallDistanceUnit
        self.m_oUnits.set_current_unit("SmallDistanceUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new SmallDistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("SmallDistanceUnit"))
        self.m_logger.WriteLine("----- VO OFFSET LABEL ----- END -----")


# endregion


# region VOOffsetAttachHelper
class VOOffsetAttachHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oAttach: "IVOOffsetAttach"):
        Assert.assertIsNotNone(oAttach)
        self.m_logger.WriteLine("Offsets Attach Points test:")
        # AvailableAttachPoints
        arPoints = oAttach.available_attach_points
        # Enable (false)
        self.m_logger.WriteLine4("\tThe current Enable flag is: {0}", oAttach.enable)
        oAttach.enable = False
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oAttach.enable)
        Assert.assertEqual(False, oAttach.enable)
        if Array.Length(arPoints) > 0:

            def action58():
                oAttach.attach_pt_name = str(arPoints[0])

            TryCatchAssertBlock.DoAssert("Allows to modify a readonly property!", action58)

        # Enable (true)
        oAttach.enable = True
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oAttach.enable)
        Assert.assertEqual(True, oAttach.enable)
        # AttachPtName
        self.m_logger.WriteLine5("\tThe current AttachPtName is: {0}", oAttach.attach_pt_name)
        self.m_logger.WriteLine3("\tThe AvailableAttachPoints array contains: {0} elements.", Array.Length(arPoints))
        if Array.Length(arPoints) > 0:
            strName: str = str(arPoints[0])
            self.m_logger.WriteLine5("\t\tElement: {0}", strName)
            oAttach.attach_pt_name = strName
            self.m_logger.WriteLine5("\t\t\tThe new AttachPtName is: {0}", oAttach.attach_pt_name)
            Assert.assertEqual(strName, oAttach.attach_pt_name)

        def action59():
            oAttach.attach_pt_name = "InvalidName"

        TryCatchAssertBlock.DoAssert("Allows to set illegal value!", action59)


# endregion


# region VORangeContoursHelper
class VORangeContoursHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "IVORangeContours"):
        self.m_logger.WriteLine("----- THE VO RANGE CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # Visible
        self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oContours.is_visible)
        oContours.is_visible = False
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oContours.is_visible)
        Assert.assertEqual(False, oContours.is_visible)

        def action60():
            oContours.translucent_lines = False

        # TranslucentLines
        TryCatchAssertBlock.DoAssert("The Translucent Lines should be readonly when Visible flag is False.", action60)

        def action61():
            oContours.percent_translucency = 34.56789

        # PercentTranslucency
        TryCatchAssertBlock.DoAssert("The Translucency should be readonly when Visible flag is False.", action61)

        # LabelSwapDistance
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(oContours.label_swap_distance)

        # BorderWall (ReadOnly) test
        oHelper = VOBorderWallHelper(self.m_oUnits)
        oHelper.Run(oContours.border_wall, True)

        # Visible
        oContours.is_visible = True
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oContours.is_visible)
        Assert.assertEqual(True, oContours.is_visible)
        # TranslucentLines
        self.m_logger.WriteLine4("\t\tThe current TranslucentLines flag is: {0}", oContours.translucent_lines)
        oContours.translucent_lines = False
        self.m_logger.WriteLine4("\t\tThe new TranslucentLines flag is: {0}", oContours.translucent_lines)
        Assert.assertEqual(False, oContours.translucent_lines)

        def action62():
            oContours.percent_translucency = 34.56789

        # PercentTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Translucency should be readonly when Translucent Lines flag is False.", action62
        )
        # TranslucentLines
        oContours.translucent_lines = True
        self.m_logger.WriteLine4("\t\tThe new TranslucentLines flag is: {0}", oContours.translucent_lines)
        Assert.assertEqual(True, oContours.translucent_lines)
        # PercentTranslucency
        self.m_logger.WriteLine6("\t\tThe current Percent Translucency is: {0}", oContours.percent_translucency)
        oContours.percent_translucency = 34.56789
        self.m_logger.WriteLine6("\t\tThe new Percent Translucency is: {0}", oContours.percent_translucency)
        Assert.assertEqual(34.56789, oContours.percent_translucency)

        def action63():
            oContours.percent_translucency = 1234.56789

        # range test
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action63)

        # BorderWall (NotReadOnly) test
        oHelper.Run(oContours.border_wall, False)
        self.m_logger.WriteLine("----- THE VO RANGE CONTOURS TEST ----- END -----")


# endregion


# region VOBorderWallHelper
class VOBorderWallHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oWall: "IVOBorderWall", bReadOnly: bool):
        Assert.assertIsNotNone(oWall)
        if bReadOnly:
            self.ReadOnly(oWall)

        else:
            self.NotReadOnly(oWall)

    # endregion

    # region ReadOnly method
    def ReadOnly(self, oWall: "IVOBorderWall"):
        Assert.assertIsNotNone(oWall)
        self.m_logger.WriteLine("Border Wall (ReadOnly) test:")

        def action64():
            oWall.use_border_wall = False

        # UseBorderWall
        TryCatchAssertBlock.DoAssert("The Use Border Wall should be readonly.", action64)

        def action65():
            oWall.upper_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL

        # UpperEdgeAltRef
        TryCatchAssertBlock.DoAssert("The Upper Edge should be readonly.", action65)

        def action66():
            oWall.lower_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain

        # LowerEdgeAltRef
        TryCatchAssertBlock.DoAssert("The Lower Edge should be readonly.", action66)

        def action67():
            oWall.upper_edge_height = 12.34

        # UpperEdgeHeight
        TryCatchAssertBlock.DoAssert("The Upper Edge Height should be readonly.", action67)

        def action68():
            oWall.lower_edge_height = 34.12

        # LowerEdgeHeight
        TryCatchAssertBlock.DoAssert("The Lower Edge Height should be readonly.", action68)

        def action69():
            oWall.use_wall_translucency = False

        # UseWallTranslucency
        TryCatchAssertBlock.DoAssert("The Use Wall Translucency should be readonly.", action69)

        def action70():
            oWall.use_line_translucency = False

        # UseLineTranslucency
        TryCatchAssertBlock.DoAssert("The Use Line Translucency should be readonly.", action70)

        def action71():
            oWall.wall_translucency = 34.56

        # WallTranslucency
        TryCatchAssertBlock.DoAssert("The Wall Translucency should be readonly.", action71)

        def action72():
            oWall.line_translucency = 56.34

        # LineTranslucency
        TryCatchAssertBlock.DoAssert("The Line Translucency should be readonly.", action72)

    # endregion

    # region NotReadOnly method
    def NotReadOnly(self, oWall: "IVOBorderWall"):
        Assert.assertIsNotNone(oWall)
        self.m_logger.WriteLine("Border Wall (NotReadOnly) test:")
        # UseBorderWall
        self.m_logger.WriteLine4("\tThe current UseBorderWall flag is: {0}", oWall.use_border_wall)
        oWall.use_border_wall = False
        self.m_logger.WriteLine4("\tThe new UseBorderWall flag is: {0}", oWall.use_border_wall)
        Assert.assertEqual(False, oWall.use_border_wall)

        def action73():
            oWall.upper_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL

        # UpperEdgeAltRef
        TryCatchAssertBlock.DoAssert("The Upper Edge should be readonly when Use Border Wall flag is False.", action73)

        def action74():
            oWall.lower_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain

        # LowerEdgeAltRef
        TryCatchAssertBlock.DoAssert("The Lower Edge should be readonly when Use Border Wall flag is False.", action74)

        def action75():
            oWall.upper_edge_height = 12.34

        # UpperEdgeHeight
        TryCatchAssertBlock.DoAssert(
            "The Upper Edge Height should be readonly when Use Border Wall flag is False.", action75
        )

        def action76():
            oWall.lower_edge_height = 34.12

        # LowerEdgeHeight
        TryCatchAssertBlock.DoAssert(
            "The Lower Edge Height should be readonly when Use Border Wall flag is False.", action76
        )

        def action77():
            oWall.use_wall_translucency = False

        # UseWallTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Use Wall Translucency should be readonly when Use Border Wall flag is False.", action77
        )

        def action78():
            oWall.use_line_translucency = False

        # UseLineTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Use Line Translucency should be readonly when Use Border Wall flag is False.", action78
        )

        def action79():
            oWall.wall_translucency = 34.56

        # WallTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Wall Translucency should be readonly when Use Border Wall flag is False.", action79
        )

        def action80():
            oWall.line_translucency = 56.34

        # LineTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Line Translucency should be readonly when Use Border Wall flag is False.", action80
        )
        # UseBorderWall
        oWall.use_border_wall = True
        self.m_logger.WriteLine4("\tThe new UseBorderWall flag is: {0}", oWall.use_border_wall)
        Assert.assertEqual(True, oWall.use_border_wall)
        # set DistanceUnit
        strDistanceUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "mi")
        self.m_logger.WriteLine5(
            "\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("mi", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # IsAltRefTypeSupported
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported eAltRefMSL is: {0}",
            oWall.is_alt_ref_type_supported(AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported eAltRefObject is: {0}",
            oWall.is_alt_ref_type_supported(AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported eAltRefTerrain is: {0}",
            oWall.is_alt_ref_type_supported(AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported eAltRefWGS84 is: {0}",
            oWall.is_alt_ref_type_supported(AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84),
        )

        # UpperEdgeAltRef
        self.m_logger.WriteLine6("\t\tThe current UpperEdge is: {0}", oWall.upper_edge_alt_ref)
        oWall.upper_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.upper_edge_alt_ref)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL, oWall.upper_edge_alt_ref)
        oWall.upper_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.upper_edge_alt_ref)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject, oWall.upper_edge_alt_ref)
        oWall.upper_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.upper_edge_alt_ref)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain, oWall.upper_edge_alt_ref)
        oWall.upper_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.upper_edge_alt_ref)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84, oWall.upper_edge_alt_ref)
        # UpperEdgeHeight
        self.m_logger.WriteLine6("\t\tThe current UpperEdge Height is: {0}", oWall.upper_edge_height)
        oWall.upper_edge_height = 123.4567
        self.m_logger.WriteLine6("\t\tThe new UpperEdge Height is: {0}", oWall.upper_edge_height)
        Assert.assertEqual(123.4567, oWall.upper_edge_height)

        def action81():
            oWall.upper_edge_height = -9876543210.1

        # UpperEdgeHeight
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action81)
        # LowerEdgeAltRef
        self.m_logger.WriteLine6("\t\tThe current LowerEdge is: {0}", oWall.lower_edge_alt_ref)
        oWall.lower_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.lower_edge_alt_ref)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL, oWall.lower_edge_alt_ref)
        oWall.lower_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.lower_edge_alt_ref)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject, oWall.lower_edge_alt_ref)
        oWall.lower_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.lower_edge_alt_ref)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain, oWall.lower_edge_alt_ref)
        oWall.lower_edge_alt_ref = AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.lower_edge_alt_ref)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84, oWall.lower_edge_alt_ref)
        # LowerEdgeHeight
        self.m_logger.WriteLine6("\t\tThe current LowerEdge Height is: {0}", oWall.lower_edge_height)
        oWall.lower_edge_height = 123.4567
        self.m_logger.WriteLine6("\t\tThe new LowerEdge Height is: {0}", oWall.lower_edge_height)
        Assert.assertEqual(123.4567, oWall.lower_edge_height)

        def action82():
            oWall.lower_edge_height = -9876543210.1

        # LowerEdgeHeight
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action82)
        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit (restored) is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # UseWallTranslucency
        self.m_logger.WriteLine4("\t\tThe current UseWallTranslucency flag is: {0}", oWall.use_wall_translucency)
        oWall.use_wall_translucency = False
        self.m_logger.WriteLine4("\t\tThe new UseWallTranslucency flag is: {0}", oWall.use_wall_translucency)
        Assert.assertEqual(False, oWall.use_wall_translucency)

        def action83():
            oWall.wall_translucency = 34.56

        # WallTranslucency
        TryCatchAssertBlock.DoAssert("The Wall Translucency should be readonly.", action83)
        # UseWallTranslucency
        oWall.use_wall_translucency = True
        self.m_logger.WriteLine4("\t\tThe new UseWallTranslucency flag is: {0}", oWall.use_wall_translucency)
        Assert.assertEqual(True, oWall.use_wall_translucency)
        # WallTranslucency
        self.m_logger.WriteLine6("\t\tThe current WallTranslucency is: {0}", oWall.wall_translucency)
        oWall.wall_translucency = 34.56
        self.m_logger.WriteLine6("\t\tThe new WallTranslucency is: {0}", oWall.wall_translucency)
        Assert.assertAlmostEqual(34.56, oWall.wall_translucency, delta=0.01)

        def action84():
            oWall.wall_translucency = 1234.56

        # WallTranslucency
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action84)
        # UseLineTranslucency
        self.m_logger.WriteLine4("\t\tThe current UseLineTranslucency flag is: {0}", oWall.use_line_translucency)
        oWall.use_line_translucency = False
        self.m_logger.WriteLine4("\t\tThe new UseLineTranslucency flag is: {0}", oWall.use_line_translucency)
        Assert.assertEqual(False, oWall.use_line_translucency)

        def action85():
            oWall.line_translucency = 34.56

        # LineTranslucency
        TryCatchAssertBlock.DoAssert("The Line Translucency should be readonly.", action85)
        # UseLineTranslucency
        oWall.use_line_translucency = True
        self.m_logger.WriteLine4("\t\tThe new UseLineTranslucency flag is: {0}", oWall.use_line_translucency)
        Assert.assertEqual(True, oWall.use_line_translucency)
        # LineTranslucency
        self.m_logger.WriteLine6("\t\tThe current LineTranslucency is: {0}", oWall.line_translucency)
        oWall.line_translucency = 34.56
        self.m_logger.WriteLine6("\t\tThe new LineTranslucency is: {0}", oWall.line_translucency)
        Assert.assertAlmostEqual(34.56, oWall.line_translucency, delta=0.01)

        def action86():
            oWall.line_translucency = 1234.56

        # LineTranslucency
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action86)


# endregion


# region VOAzElMaskHelper
class VOAzElMaskHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oMask: "IVOAzElMask"):
        self.m_logger.WriteLine("----- THE VO AZ/EL MASK TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oMask)
        # CompassDirectionsVisible
        self.m_logger.WriteLine4("The current CompassDirectionsVisible flag is: {0}", oMask.compass_directions_visible)
        oMask.compass_directions_visible = False
        self.m_logger.WriteLine4("The new CompassDirectionsVisible flag is: {0}", oMask.compass_directions_visible)
        Assert.assertEqual(False, oMask.compass_directions_visible)
        oMask.compass_directions_visible = True
        self.m_logger.WriteLine4("The new CompassDirectionsVisible flag is: {0}", oMask.compass_directions_visible)
        Assert.assertEqual(True, oMask.compass_directions_visible)
        # AltLabelsVisible
        self.m_logger.WriteLine4("The current AltLabelsVisible flag is: {0}", oMask.alt_labels_visible)
        oMask.alt_labels_visible = False
        self.m_logger.WriteLine4("The new AltLabelsVisible flag is: {0}", oMask.alt_labels_visible)
        Assert.assertEqual(False, oMask.alt_labels_visible)
        bCaught: bool = False
        try:
            bCaught = False
            oMask.numb_alt_labels = 12

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The NumbAltLabels should be readonly.")

        oMask.alt_labels_visible = True
        self.m_logger.WriteLine4("The new AltLabelsVisible flag is: {0}", oMask.alt_labels_visible)
        Assert.assertEqual(True, oMask.alt_labels_visible)
        # NumbAltLabels
        self.m_logger.WriteLine3("\tThe current NumbAltLabels flag is: {0}", oMask.numb_alt_labels)
        oMask.numb_alt_labels = 45
        self.m_logger.WriteLine3("\tThe new NumbAltLabels flag is: {0}", oMask.numb_alt_labels)
        Assert.assertEqual(45, oMask.numb_alt_labels)
        try:
            bCaught = False
            oMask.numb_alt_labels = 123

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # InteriorTranslucency
        self.m_logger.WriteLine6("\tThe current InteriorTranslucency flag is: {0}", oMask.interior_translucency)
        oMask.interior_translucency = 98.76
        self.m_logger.WriteLine6("\tThe new InteriorTranslucency flag is: {0}", oMask.interior_translucency)
        Assert.assertAlmostEqual(98.76, oMask.interior_translucency, delta=0.01)
        try:
            bCaught = False
            oMask.interior_translucency = 123

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # LineTranslucency
        self.m_logger.WriteLine6("\tThe current LineTranslucency flag is: {0}", oMask.line_translucency)
        oMask.line_translucency = 12.34
        self.m_logger.WriteLine6("\tThe new LineTranslucency flag is: {0}", oMask.line_translucency)
        Assert.assertAlmostEqual(12.34, oMask.line_translucency, delta=0.01)
        try:
            bCaught = False
            oMask.line_translucency = 123

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(oMask.label_swap_distance)

        self.m_logger.WriteLine("----- THE VO AZ/EL MASK TEST ----- END -----")


# endregion


# region VOLabelSwapDistance
class VOLabelSwapDistanceHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oSwapDist: "IVOLabelSwapDistance"):
        self.m_logger.WriteLine("----- VO LABEL SWAP DISTANCE TEST ----- BEGIN -----")
        # DistanceValue
        self.m_logger.WriteLine6("\tThe current DistanceValue is: {0}", oSwapDist.distance_value)
        oSwapDist.distance_value = 0.56789
        self.m_logger.WriteLine6("\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        Assert.assertEqual(0.56789, oSwapDist.distance_value)

        def action87():
            oSwapDist.distance_value = -34.56789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action87)
        # DistanceLevel
        self.m_logger.WriteLine6("\tThe current DistanceLevel is: {0}", oSwapDist.distance_level)
        # SetDistanceLevel (eSwapAll)
        oSwapDist.set_distance_level(AgEVOLabelSwapDistance.eSwapAll)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapAll, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (eSwapMarker)
        oSwapDist.set_distance_level(AgEVOLabelSwapDistance.eSwapMarker)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapMarker, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (eSwapMarkerLabel)
        oSwapDist.set_distance_level(AgEVOLabelSwapDistance.eSwapMarkerLabel)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapMarkerLabel, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (eSwapModelLabel)
        oSwapDist.set_distance_level(AgEVOLabelSwapDistance.eSwapModelLabel)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapModelLabel, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (eSwapPoint)
        oSwapDist.set_distance_level(AgEVOLabelSwapDistance.eSwapPoint)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapPoint, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)

        def action88():
            oSwapDist.set_distance_level(AgEVOLabelSwapDistance.eSwapCustom)

        # SetDistanceLevel (eSwapCustom)
        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action88)

        def action89():
            oSwapDist.set_distance_level(AgEVOLabelSwapDistance.eSwapUnknown)

        # SetDistanceLevel (eSwapUnknown)
        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action89)
        self.m_logger.WriteLine("----- VO LABEL SWAP DISTANCE TEST ----- END -----")


# endregion


# region VOVectorsHelper
class VOVectorsHelper(object):
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection", root: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits
        self.m_oRoot: "IStkObjectRoot" = root

    # endregion

    # region Run method
    def Run(self, oVector: "IVOVector", bScaleRelativeReadOnly: bool):
        self.m_logger.WriteLine("----- THE VO VECTORS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oVector)
        bCaught: bool = False
        # ScaleRelativeToModel
        self.m_logger.WriteLine4("The current ScaleRelativeToModel flag is: {0}", oVector.scale_relative_to_model)
        if not bScaleRelativeReadOnly:
            oVector.scale_relative_to_model = False
            self.m_logger.WriteLine4("The new ScaleRelativeToModel flag is: {0}", oVector.scale_relative_to_model)
            Assert.assertEqual(False, oVector.scale_relative_to_model)
            oVector.scale_relative_to_model = True
            self.m_logger.WriteLine4("The new ScaleRelativeToModel flag is: {0}", oVector.scale_relative_to_model)
            Assert.assertEqual(True, oVector.scale_relative_to_model)

        else:
            try:
                bCaught = False
                oVector.scale_relative_to_model = True

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("Expected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The ScaleRelativeToModel should be readonly.")

        # VectorSizeScale
        self.m_logger.WriteLine6("The current Vector Size Scale is: {0}", oVector.vector_size_scale)
        oVector.vector_size_scale = 9.87654321
        self.m_logger.WriteLine6("The new Vector Size Scale is: {0}", oVector.vector_size_scale)
        Assert.assertEqual(9.87654321, oVector.vector_size_scale)
        # range test
        try:
            bCaught = False
            oVector.vector_size_scale = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # AngleSizeScale
        self.m_logger.WriteLine6("The current Angle Size Scale is: {0}", oVector.angle_size_scale)
        oVector.angle_size_scale = 3.21987654
        self.m_logger.WriteLine6("The new Angle Size Scale is: {0}", oVector.angle_size_scale)
        Assert.assertEqual(3.21987654, oVector.angle_size_scale)
        # range test
        try:
            bCaught = False
            oVector.angle_size_scale = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # RefCrdns
        self.RefCrdnsCollection(oVector.ref_crdns)

        self.m_logger.WriteLine("----- THE VO VECTORS TEST ----- END -----")

    # endregion

    # region RefCrdnsCollection method
    def RefCrdnsCollection(self, oCollection: "IVOReferenceAnalysisWorkbenchCollection"):
        Assert.assertIsNotNone(oCollection)
        self.m_logger.WriteLine("VORefCrdnCollection test:")

        # Count
        self.m_logger.WriteLine3("The current VectorCollection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            refCrdn: "IVOReferenceAnalysisWorkbenchComponent" = oCollection[iIndex]
            Assert.assertIsNotNone(refCrdn)
            self.m_logger.WriteLine8("\tElement {0}: Name = {1}, Type = {2}", iIndex, refCrdn.name, refCrdn.type_id)

            iIndex += 1

        def action90():
            refCrdn: "IVOReferenceAnalysisWorkbenchComponent" = oCollection[oCollection.count]

        TryCatchAssertBlock.DoAssert("Invalid index", action90)

        voRefCrdn: "IVOReferenceAnalysisWorkbenchComponent"

        for voRefCrdn in oCollection:
            name: str = voRefCrdn.name

        # RemoveAll
        oCollection.remove_all()
        self.m_logger.WriteLine3("After RemoveAll() the Vector Collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(0, oCollection.count)

        # AvailableCrdns
        arAvailable = oCollection.available_crdns
        self.m_logger.WriteLine3("The AvailableCrdns array contains {0} elements", len(arAvailable))

        def action91():
            refCrdn: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.add(
                AgEGeometricElemType.eAngleElem, "bogus"
            )

        TryCatchAssertBlock.DoAssert("Invalid object.", action91)

        def action92():
            oElement2: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.get_crdn_by_name(
                clr.Convert((-1), AgEGeometricElemType), "bogus"
            )

        TryCatchAssertBlock.DoAssert("Invalid AgEGeometricElemType", action92)

        def action93():
            oElement2: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.get_crdn_by_name(
                AgEGeometricElemType.eAngleElem, ""
            )

        TryCatchAssertBlock.DoAssert("Invalid crdn name", action93)

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "AgEGeometricElemType" = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.eAngleElem:
                refCrdn: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.add(eType, str(arAvailable[iIndex][0]))
                Assert.assertIsNotNone(refCrdn)
                self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_id)
                oElement2: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.get_crdn_by_name(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertEqual(oElement2.name, refCrdn.name)
                break

            iIndex += 1

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "AgEGeometricElemType" = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.eAxesElem:
                refCrdn: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.add(eType, str(arAvailable[iIndex][0]))
                Assert.assertIsNotNone(refCrdn)
                self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_id)
                oElement2: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.get_crdn_by_name(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertEqual(oElement2.name, refCrdn.name)
                break

            iIndex += 1

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "AgEGeometricElemType" = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.ePlaneElem:
                refCrdn: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.add(eType, str(arAvailable[iIndex][0]))
                Assert.assertIsNotNone(refCrdn)
                self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_id)
                oElement2: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.get_crdn_by_name(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertEqual(oElement2.name, refCrdn.name)
                break

            iIndex += 1

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "AgEGeometricElemType" = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.ePointElem:
                refCrdn: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.add(eType, str(arAvailable[iIndex][0]))
                Assert.assertIsNotNone(refCrdn)
                self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_id)
                oElement2: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.get_crdn_by_name(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertEqual(oElement2.name, refCrdn.name)
                break

            iIndex += 1

        # Add Vector element
        bFound: bool = False

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "AgEGeometricElemType" = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.eVectorElem:
                oVector: "IVOReferenceVectorGeometryToolVector" = clr.Convert(
                    oCollection.add(eType, str(arAvailable[iIndex][0])), IVOReferenceVectorGeometryToolVector
                )
                Assert.assertIsNotNone(oVector)
                strMagnitudeDim: str = oVector.magnitude_dimension
                if (strMagnitudeDim != "Unitless") and (strMagnitudeDim.find("Rate") == -1):
                    self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", oVector.name, oVector.type_id)
                    oElement2: "IVOReferenceAnalysisWorkbenchComponent" = oCollection.get_crdn_by_name(
                        eType, str(arAvailable[iIndex][0])
                    )
                    Assert.assertEqual(oElement2.name, oVector.name)
                    break

                if not bFound:
                    self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", oVector.name, oVector.type_id)
                    bFound = True

                else:
                    oCollection.remove_by_name(eType, oVector.name)

            iIndex += 1

        # Count
        self.m_logger.WriteLine3("The new VectorCollection contains: {0} elements", oCollection.count)
        refCrdn: "IVOReferenceAnalysisWorkbenchComponent"
        for refCrdn in oCollection:
            self.m_logger.WriteLine7("\tElement: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_id)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            refCrdn: "IVOReferenceAnalysisWorkbenchComponent" = oCollection[iIndex]
            Assert.assertIsNotNone(refCrdn)
            self.m_logger.WriteLine5("-> {0}", refCrdn.name)

            # Visible (false)
            self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", refCrdn.visible)
            refCrdn.visible = False
            self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", refCrdn.visible)
            Assert.assertEqual(False, refCrdn.visible)

            bCaught: bool = False
            try:
                bCaught = False
                refCrdn.color = Color.FromArgb(52)

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The Color should be readonly.")

            try:
                bCaught = False
                refCrdn.label_visible = True

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The LabelVisible should be readonly.")

            if refCrdn.type_id == AgEGeometricElemType.eAngleElem:
                self.RefCrdnAngleReadOnly(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolAngle))
            elif refCrdn.type_id == AgEGeometricElemType.eAxesElem:
                self.RefCrdnAxesReadOnly(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolAxes))
            elif refCrdn.type_id == AgEGeometricElemType.ePlaneElem:
                self.RefCrdnPlaneReadOnly(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolPlane))
            elif refCrdn.type_id == AgEGeometricElemType.ePointElem:
                self.RefCrdnPointReadOnly(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolPoint))
            elif refCrdn.type_id == AgEGeometricElemType.eVectorElem:
                self.RefCrdnVectorReadOnly(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolVector))
            else:
                Assert.fail("Invalid TypeID!")

            # Visible (true)
            refCrdn.visible = True
            self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", refCrdn.visible)
            Assert.assertEqual(True, refCrdn.visible)

            # Color
            self.m_logger.WriteLine6("\tThe current Color is: {0}", refCrdn.color)
            refCrdn.color = Color.FromArgb(9990945)
            self.m_logger.WriteLine6("\tThe new Color is: {0}", refCrdn.color)
            AssertEx.AreEqual(Color.FromArgb(9990945), refCrdn.color)

            # LabelVisible
            self.m_logger.WriteLine4("\tThe current LabelVisible flag is: {0}", refCrdn.label_visible)
            refCrdn.label_visible = True
            self.m_logger.WriteLine4("\tThe new LabelVisible flag is: {0}", refCrdn.label_visible)
            Assert.assertEqual(True, refCrdn.label_visible)
            if refCrdn.type_id == AgEGeometricElemType.eAngleElem:
                self.RefCrdnAngle(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolAngle))
            elif refCrdn.type_id == AgEGeometricElemType.eAxesElem:
                self.RefCrdnAxes(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolAxes))
            elif refCrdn.type_id == AgEGeometricElemType.ePlaneElem:
                self.RefCrdnPlane(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolPlane))
            elif refCrdn.type_id == AgEGeometricElemType.ePointElem:
                # 38619: Earth Center point freezes STK
                self.RefCrdnPoint(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolPoint))
            elif refCrdn.type_id == AgEGeometricElemType.eVectorElem:
                self.RefCrdnVector(clr.Convert(refCrdn, IVOReferenceVectorGeometryToolVector))
            else:
                Assert.fail("Invalid TypeID!")

            oHelper = DisplayTimesHelper(self.m_oRoot)
            oHelper.Run(clr.Convert(refCrdn, IDisplayTime))

            iIndex += 1

        # Remove
        self.m_logger.WriteLine3("Before Remove(0) the Vector Collection contains: {0} elements", oCollection.count)
        oCollection.remove(0)
        self.m_logger.WriteLine3("After Remove(0) the Vector Collection contains: {0} elements", oCollection.count)

        def action94():
            oCollection.remove(oCollection.count)

        TryCatchAssertBlock.DoAssert("Invalid Remove index", action94)

        # RemoveByName
        self.m_logger.WriteLine3(
            "Before RemoveByName() the Vector Collection contains: {0} elements", oCollection.count
        )
        oCollection.remove_by_name(oCollection[0].type_id, oCollection[0].name)
        self.m_logger.WriteLine3("After RemoveByName() the Vector Collection contains: {0} elements", oCollection.count)

        def action95():
            oCollection.remove_by_name(clr.Convert((-1), AgEGeometricElemType), "bogus")

        TryCatchAssertBlock.DoAssert("Invalid Remove type", action95)

        def action96():
            oCollection.remove_by_name(AgEGeometricElemType.eAngleElem, "bogus")

        TryCatchAssertBlock.DoAssert("Invalid Remove name", action96)

        # RemoveAll
        self.m_logger.WriteLine3("Before RemoveAll() the Vector Collection contains: {0} elements", oCollection.count)
        oCollection.remove_all()
        self.m_logger.WriteLine3("After RemoveAll() the Vector Collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(0, oCollection.count)

    # endregion

    # region RefCrdnAngleReadOnly method
    def RefCrdnAngleReadOnly(self, oAngle: "IVOReferenceVectorGeometryToolAngle"):
        Assert.assertIsNotNone(oAngle)
        self.m_logger.WriteLine("\tRefCrdnAngle test (ReadOnly):")
        bCaught: bool = False
        try:
            bCaught = False
            oAngle.angle_value_visible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AngleValueVisible should be readonly.")

        try:
            bCaught = False
            oAngle.angle_unit_abrv = "rad"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AngleUnitAbrv should be readonly.")

        try:
            bCaught = False
            oAngle.show_dihedral_angle_supporting_arcs = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The ShowDihedralAngleSupportingArcs should be readonly.")

    # endregion

    # region RefCrdnAngle method
    def RefCrdnAngle(self, oAngle: "IVOReferenceVectorGeometryToolAngle"):
        Assert.assertIsNotNone(oAngle)
        self.m_logger.WriteLine("\tRefCrdnAngle test:")
        # AngleValueVisible
        self.m_logger.WriteLine4("\t\tThe current AngleValueVisible flag is: {0}", oAngle.angle_value_visible)
        oAngle.angle_value_visible = False
        self.m_logger.WriteLine4("\t\tThe new AngleValueVisible flag is: {0}", oAngle.angle_value_visible)
        Assert.assertEqual(False, oAngle.angle_value_visible)
        bCaught: bool = False
        try:
            bCaught = False
            oAngle.angle_unit_abrv = "mrad"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AngleUnitAbrv should be readonly.")

        oAngle.angle_value_visible = True
        self.m_logger.WriteLine4("\t\tThe new AngleValueVisible flag is: {0}", oAngle.angle_value_visible)
        Assert.assertEqual(True, oAngle.angle_value_visible)
        # AngleUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current AngleUnitAbrv is: {0}", oAngle.angle_unit_abrv)
        oAngle.angle_unit_abrv = "mdeg"
        self.m_logger.WriteLine5("\t\tThe new AngleUnitAbrv is: {0}", oAngle.angle_unit_abrv)
        Assert.assertEqual("mdeg", oAngle.angle_unit_abrv)
        try:
            bCaught = False
            oAngle.angle_unit_abrv = "abcdefgh"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

    # endregion

    # region RefCrdnAxesReadOnly method
    def RefCrdnAxesReadOnly(self, oAxes: "IVOReferenceVectorGeometryToolAxes"):
        Assert.assertIsNotNone(oAxes)
        self.m_logger.WriteLine("\tRefCrdnAxes test (ReadOnly):")
        bCaught: bool = False
        try:
            bCaught = False
            oAxes.draw_at_cb = False

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The DrawAtCB should be readonly.")

        try:
            bCaught = False
            oAxes.persistence_visible = False

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The PersistenceVisible should be readonly.")

        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        try:
            bCaught = False
            oAxes.duration = 123.456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Duration should be readonly.")

        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        try:
            bCaught = False
            oAxes.connect = AgEVectorAxesConnectType.eConnectLine

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Connect should be readonly.")

        try:
            bCaught = False
            oAxes.transparent = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparent should be readonly.")

        try:
            bCaught = False
            oAxes.axes = "CentralBody/Earth Fixed Axes"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Axes should be readonly.")

    # endregion

    # region RefCrdnAxes method
    def RefCrdnAxes(self, oAxes: "IVOReferenceVectorGeometryToolAxes"):
        Assert.assertIsNotNone(oAxes)
        self.m_logger.WriteLine("\tRefCrdnAxes test:")
        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        # DrawAtCB
        self.m_logger.WriteLine4("\t\tThe current DrawAtCB flag is: {0}", oAxes.draw_at_cb)
        oAxes.draw_at_cb = True
        self.m_logger.WriteLine4("\t\tThe new DrawAtCB flag is: {0}", oAxes.draw_at_cb)
        Assert.assertEqual(True, oAxes.draw_at_cb)
        # Axes
        self.m_logger.WriteLine5("\t\tThe current Axes is: {0}", oAxes.axes)
        # AvailableAxes
        arAxes = oAxes.available_axes
        self.m_logger.WriteLine3("\t\tThe AvailableAxes array contains: {0} elements.", len(arAxes))
        # PersistenceVisible (false)
        self.m_logger.WriteLine4("\t\tThe current PersistenceVisible flag is: {0}", oAxes.persistence_visible)
        oAxes.persistence_visible = False
        self.m_logger.WriteLine4("\t\tThe new PersistenceVisible flag is: {0}", oAxes.persistence_visible)
        Assert.assertEqual(False, oAxes.persistence_visible)
        bCaught: bool = False
        try:
            bCaught = False
            oAxes.duration = 123.456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Duration should be readonly.")

        try:
            bCaught = False
            oAxes.connect = AgEVectorAxesConnectType.eConnectLine

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Connect should be readonly.")

        try:
            bCaught = False
            oAxes.transparent = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparent should be readonly.")

        # PersistenceVisible (true)
        oAxes.persistence_visible = True
        self.m_logger.WriteLine4("\t\tThe new PersistenceVisible flag is: {0}", oAxes.persistence_visible)
        Assert.assertEqual(True, oAxes.persistence_visible)
        # Transparent
        self.m_logger.WriteLine4("\t\tThe current Transparent flag is: {0}", oAxes.transparent)
        oAxes.transparent = False
        self.m_logger.WriteLine4("\t\tThe new Transparent flag is: {0}", oAxes.transparent)
        Assert.assertEqual(False, oAxes.transparent)
        # Connect
        self.m_logger.WriteLine6("\t\tThe current Connect is: {0}", oAxes.connect)
        oAxes.connect = AgEVectorAxesConnectType.eConnectTrace
        self.m_logger.WriteLine6("\t\tThe new Connect is: {0}", oAxes.connect)
        Assert.assertEqual(AgEVectorAxesConnectType.eConnectTrace, oAxes.connect)
        # Duration
        self.m_logger.WriteLine6("\t\tThe current Duration is: {0}", oAxes.duration)
        oAxes.duration = 12345.6789
        self.m_logger.WriteLine6("\t\tThe new Duration is: {0}", oAxes.duration)
        Assert.assertAlmostEqual(12345.6789, oAxes.duration, delta=1e-05)
        # range test
        try:
            bCaught = False
            oAxes.duration = -1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

    # endregion

    # region RefCrdnPlaneReadOnly method
    def RefCrdnPlaneReadOnly(self, oPlane: "IVOReferenceVectorGeometryToolPlane"):
        Assert.assertIsNotNone(oPlane)
        self.m_logger.WriteLine("\tRefCrdnPlane test (ReadOnly):")
        bCaught: bool = False
        try:
            bCaught = False
            oPlane.axis_labels_visible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AxisLabelsVisible should be readonly.")

        try:
            bCaught = False
            oPlane.transparent_plane_visible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TransparentPlaneVisible should be readonly.")

        try:
            bCaught = False
            oPlane.transparency = 12

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparency should be readonly.")

        try:
            bCaught = False
            oPlane.draw_at_object = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The DrawAtObject should be readonly.")

        try:
            bCaught = False
            oPlane.rect_grid_visible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RectGridVisible should be readonly.")

        try:
            bCaught = False
            oPlane.circ_grid_visible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CircGridVisible should be readonly.")

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "ft")
        self.m_logger.WriteLine5(
            "\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("ft", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        try:
            bCaught = False
            oPlane.plane_grid_spacing = 123.456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The PlaneGridSpacing should be readonly.")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        try:
            bCaught = False
            oPlane.size = 123.456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Size should be readonly.")

    # endregion

    # region RefCrdnPlane method
    def RefCrdnPlane(self, oPlane: "IVOReferenceVectorGeometryToolPlane"):
        Assert.assertIsNotNone(oPlane)
        self.m_logger.WriteLine("\tRefCrdnPlane test:")
        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "Re")
        self.m_logger.WriteLine5(
            "\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("Re", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # AxisLabelsVisible
        self.m_logger.WriteLine4("\t\tThe current AxisLabelsVisible flag is: {0}", oPlane.axis_labels_visible)
        oPlane.axis_labels_visible = False
        self.m_logger.WriteLine4("\t\tThe new AxisLabelsVisible flag is: {0}", oPlane.axis_labels_visible)
        Assert.assertEqual(False, oPlane.axis_labels_visible)
        oPlane.axis_labels_visible = True
        self.m_logger.WriteLine4("\t\tThe new AxisLabelsVisible flag is: {0}", oPlane.axis_labels_visible)
        Assert.assertEqual(True, oPlane.axis_labels_visible)
        # DrawAtObject
        self.m_logger.WriteLine4("\t\tThe current DrawAtObject flag is: {0}", oPlane.draw_at_object)
        oPlane.draw_at_object = False
        self.m_logger.WriteLine4("\t\tThe new DrawAtObject flag is: {0}", oPlane.draw_at_object)
        Assert.assertEqual(False, oPlane.draw_at_object)
        oPlane.draw_at_object = True
        self.m_logger.WriteLine4("\t\tThe new DrawAtObject flag is: {0}", oPlane.draw_at_object)
        Assert.assertEqual(True, oPlane.draw_at_object)
        # Size
        self.m_logger.WriteLine6("\t\tThe current Size is: {0}", oPlane.size)
        oPlane.size = 3.21
        self.m_logger.WriteLine6("\t\tThe new Size is: {0}", oPlane.size)
        Assert.assertEqual(3.21, oPlane.size)
        bCaught: bool = False
        # range test
        try:
            bCaught = False
            oPlane.size = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # TransparentPlaneVisible
        self.m_logger.WriteLine4(
            "\t\tThe current TransparentPlaneVisible flag is: {0}", oPlane.transparent_plane_visible
        )
        oPlane.transparent_plane_visible = False
        self.m_logger.WriteLine4("\t\tThe new TransparentPlaneVisible flag is: {0}", oPlane.transparent_plane_visible)
        Assert.assertEqual(False, oPlane.transparent_plane_visible)
        try:
            bCaught = False
            oPlane.transparency = 23.45

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparency should be readonly.")

        oPlane.transparent_plane_visible = True
        self.m_logger.WriteLine4("\t\tThe new TransparentPlaneVisible flag is: {0}", oPlane.transparent_plane_visible)
        Assert.assertEqual(True, oPlane.transparent_plane_visible)
        # Transparency
        self.m_logger.WriteLine6("\t\tThe current Transparency is: {0}", oPlane.transparency)
        oPlane.transparency = 12.34
        self.m_logger.WriteLine6("\t\tThe new Transparency is: {0}", oPlane.transparency)
        Assert.assertAlmostEqual(12.34, oPlane.transparency, delta=0.001)
        # range test
        try:
            bCaught = False
            oPlane.transparency = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # RectGridVisible (false)
        self.m_logger.WriteLine4("\t\tThe current RectGridVisible flag is: {0}", oPlane.rect_grid_visible)
        oPlane.rect_grid_visible = False
        self.m_logger.WriteLine4("\t\tThe new RectGridVisible flag is: {0}", oPlane.rect_grid_visible)
        Assert.assertEqual(False, oPlane.rect_grid_visible)
        # CircGridVisible (false)
        self.m_logger.WriteLine4("\t\tThe current CircGridVisible flag is: {0}", oPlane.circ_grid_visible)
        oPlane.circ_grid_visible = False
        self.m_logger.WriteLine4("\t\tThe new CircGridVisible flag is: {0}", oPlane.circ_grid_visible)
        Assert.assertEqual(False, oPlane.circ_grid_visible)
        try:
            bCaught = False
            oPlane.plane_grid_spacing = 123.45

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The PlaneGridSpacing should be readonly.")

        # RectGridVisible (true)
        oPlane.rect_grid_visible = True
        self.m_logger.WriteLine4("\t\tThe new RectGridVisible flag is: {0}", oPlane.rect_grid_visible)
        Assert.assertEqual(True, oPlane.rect_grid_visible)
        # PlaneGridSpacing
        self.m_logger.WriteLine6("\t\tThe current PlaneGridSpacing is: {0}", oPlane.plane_grid_spacing)
        oPlane.plane_grid_spacing = 987.654
        self.m_logger.WriteLine6("\t\tThe new PlaneGridSpacing is: {0}", oPlane.plane_grid_spacing)
        Assert.assertAlmostEqual(987.654, oPlane.plane_grid_spacing, delta=0.0001)
        # CircGridVisible (true)
        oPlane.circ_grid_visible = True
        self.m_logger.WriteLine4("\t\tThe new CircGridVisible flag is: {0}", oPlane.circ_grid_visible)
        Assert.assertEqual(True, oPlane.circ_grid_visible)
        # range test
        try:
            bCaught = False
            oPlane.plane_grid_spacing = -1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region RefCrdnPointReadOnly method
    def RefCrdnPointReadOnly(self, oPoint: "IVOReferenceVectorGeometryToolPoint"):
        Assert.assertIsNotNone(oPoint)
        self.m_logger.WriteLine("\tRefCrdnPoint test (ReadOnly):")
        bCaught: bool = False
        try:
            bCaught = False
            oPoint.trajectory_type = AgETrajectoryType.eTrajTrace

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TrajectoryType should be readonly.")

        try:
            bCaught = False
            oPoint.ra_dec_visible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecVisible should be readonly.")

        try:
            bCaught = False
            oPoint.ra_dec_unit_abrv = "arcMin"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecUnitAbrv should be readonly.")

        try:
            bCaught = False
            oPoint.cartesian_visible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CartesianVisible should be readonly.")

        try:
            bCaught = False
            oPoint.cartesian_unit_abrv = "Au"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CartesianUnitAbrv should be readonly.")

        try:
            bCaught = False
            oPoint.system = "CentralBody/Sun PseudoFixed System"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The System should be readonly.")

        try:
            bCaught = False
            oPoint.size = 5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Size should be readonly.")

    # endregion

    # region RefCrdnPoint method
    def RefCrdnPoint(self, oPoint: "IVOReferenceVectorGeometryToolPoint"):
        Assert.assertIsNotNone(oPoint)
        self.m_logger.WriteLine("\tRefCrdnPoint test:")
        # TrajectoryType
        self.m_logger.WriteLine6("\t\tThe current TrajectoryType is: {0}", oPoint.trajectory_type)
        oPoint.trajectory_type = AgETrajectoryType.eTrajLine
        self.m_logger.WriteLine6("\t\tThe new TrajectoryType flag is: {0}", oPoint.trajectory_type)
        Assert.assertEqual(AgETrajectoryType.eTrajLine, oPoint.trajectory_type)
        # Size
        self.m_logger.WriteLine6("\t\tThe current Size is: {0}", oPoint.size)
        oPoint.size = 3.21
        self.m_logger.WriteLine6("\t\tThe new Size is: {0}", oPoint.size)
        Assert.assertAlmostEqual(3.21, oPoint.size, delta=0.001)
        bCaught: bool = False
        # range test
        try:
            bCaught = False
            oPoint.size = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # System
        self.m_logger.WriteLine5("\t\tThe current System is: {0}", oPoint.system)
        #
        arSystems = oPoint.available_systems
        self.m_logger.WriteLine3("\t\tThe AvailableSystems array contains: {0} elements.", Array.Length(arSystems))
        # range test
        try:
            bCaught = False
            oPoint.system = "Abcdefgh"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal System!")

        # RADecVisible
        self.m_logger.WriteLine4("\t\tThe current RADecVisible flag is: {0}", oPoint.ra_dec_visible)
        oPoint.ra_dec_visible = False
        self.m_logger.WriteLine4("\t\tThe new RADecVisible flag is: {0}", oPoint.ra_dec_visible)
        Assert.assertEqual(False, oPoint.ra_dec_visible)
        try:
            bCaught = False
            oPoint.ra_dec_unit_abrv = "deg"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecUnitAbrv should be readonly.")

        oPoint.ra_dec_visible = True
        self.m_logger.WriteLine4("\t\tThe new RADecVisible flag is: {0}", oPoint.ra_dec_visible)
        Assert.assertEqual(True, oPoint.ra_dec_visible)
        # RADecUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current RADecUnitAbrv is: {0}", oPoint.ra_dec_unit_abrv)
        oPoint.ra_dec_unit_abrv = "mrad"
        self.m_logger.WriteLine5("\t\tThe new RADecUnitAbrv is: {0}", oPoint.ra_dec_unit_abrv)
        Assert.assertEqual("mrad", oPoint.ra_dec_unit_abrv)
        try:
            bCaught = False
            oPoint.ra_dec_unit_abrv = "Abc"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal RADecUnitAbrv!")

        # MagnitudeVisible
        self.m_logger.WriteLine4("\t\tThe current MagnitudeVisible flag is: {0}", oPoint.magnitude_visible)
        oPoint.magnitude_visible = False
        self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oPoint.magnitude_visible)
        Assert.assertEqual(False, oPoint.magnitude_visible)
        try:
            bCaught = False
            oPoint.magnitude_unit_abrv = "fur"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The MagnitudeUnitAbrv should be readonly.")

        oPoint.magnitude_visible = True
        self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oPoint.magnitude_visible)
        Assert.assertEqual(True, oPoint.magnitude_visible)
        # MagnitudeUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current MagnitudeUnitAbrv is: {0}", oPoint.magnitude_unit_abrv)
        oPoint.magnitude_unit_abrv = "fur"
        self.m_logger.WriteLine5("\t\tThe new MagnitudeUnitAbrv is: {0}", oPoint.magnitude_unit_abrv)
        Assert.assertEqual("fur", oPoint.magnitude_unit_abrv)
        try:
            bCaught = False
            oPoint.magnitude_unit_abrv = "Abc"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal MagnitudeUnitAbrv!")

        # CartesianVisible
        self.m_logger.WriteLine4("\t\tThe current CartesianVisible flag is: {0}", oPoint.cartesian_visible)
        oPoint.cartesian_visible = False
        self.m_logger.WriteLine4("\t\tThe new CartesianVisible flag is: {0}", oPoint.cartesian_visible)
        Assert.assertEqual(False, oPoint.cartesian_visible)
        try:
            bCaught = False
            oPoint.cartesian_unit_abrv = "kft"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CartesianUnitAbrv should be readonly.")

        oPoint.cartesian_visible = True
        self.m_logger.WriteLine4("\t\tThe new CartesianVisible flag is: {0}", oPoint.cartesian_visible)
        Assert.assertEqual(True, oPoint.cartesian_visible)
        # CartesianUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current CartesianUnitAbrv is: {0}", oPoint.cartesian_unit_abrv)
        oPoint.cartesian_unit_abrv = "kft"
        self.m_logger.WriteLine5("\t\tThe new CartesianUnitAbrv is: {0}", oPoint.cartesian_unit_abrv)
        Assert.assertEqual("kft", oPoint.cartesian_unit_abrv)
        try:
            bCaught = False
            oPoint.cartesian_unit_abrv = "Abc"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal CartesianUnitAbrv!")

    # endregion

    # region RefCrdnVectorReadOnly method
    def RefCrdnVectorReadOnly(self, oVector: "IVOReferenceVectorGeometryToolVector"):
        Assert.assertIsNotNone(oVector)
        self.m_logger.WriteLine("\tRefCrdnVector test (ReadOnly):")

        def action97():
            oVector.draw_at_cb = True

        # DrawAtCB
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action97)

        def action98():
            oVector.ra_dec_visible = True

        # RADecVisible
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action98)

        def action99():
            oVector.ra_dec_unit_abrv = "semiC"

        # RADecUnitAbrv
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action99)

        def action100():
            oVector.magnitude_visible = True

        # MagnitudeVisible
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action100)

        def action101():
            oVector.persistence_visible = True

        # PersistenceVisible
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action101)
        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

        def action102():
            oVector.duration = 123.456

        # Duration
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action102)
        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

        def action103():
            oVector.connect = AgEVectorAxesConnectType.eConnectLine

        # Connect
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action103)

        def action104():
            oVector.transparent = True

        # Transparent
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action104)

        def action105():
            oVector.axes = "CentralBody/Earth Fixed Axes"

        # Axes
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action105)

        def action106():
            oVector.draw_at_point = True

        # DrawAtPoint
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action106)

        def action107():
            oVector.point = "Satellite/Satellite1 Center Point"

        # Point
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action107)

        def action108():
            oVector.true_scale = True

        # TrueScale
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action108)

    # endregion

    # region RefCrdnVector method
    def RefCrdnVector(self, oVector: "IVOReferenceVectorGeometryToolVector"):
        Assert.assertIsNotNone(oVector)
        self.m_logger.WriteLine("\tRefCrdnVector test:")
        # DrawAtCB
        self.m_logger.WriteLine4("\t\tThe current DrawAtCB flag is: {0}", oVector.draw_at_cb)
        oVector.draw_at_cb = False
        self.m_logger.WriteLine4("\t\tThe new DrawAtCB flag is: {0}", oVector.draw_at_cb)
        Assert.assertEqual(False, oVector.draw_at_cb)
        oVector.draw_at_cb = True
        self.m_logger.WriteLine4("\t\tThe new DrawAtCB flag is: {0}", oVector.draw_at_cb)
        Assert.assertEqual(True, oVector.draw_at_cb)
        # TrueScale
        self.m_logger.WriteLine4("\t\tThe current TrueScale flag is: {0}", oVector.true_scale)
        if oVector.magnitude_dimension == "DistanceUnit":
            oVector.true_scale = False
            self.m_logger.WriteLine4("\t\tThe new TrueScale flag is: {0}", oVector.true_scale)
            Assert.assertEqual(False, oVector.true_scale)
            oVector.true_scale = True
            self.m_logger.WriteLine4("\t\tThe new TrueScale flag is: {0}", oVector.true_scale)
            Assert.assertEqual(True, oVector.true_scale)

        else:

            def action109():
                oVector.true_scale = False

            TryCatchAssertBlock.DoAssert("This property should be readonly", action109)

        # AvailableAxes
        arAxes = oVector.available_axes
        self.m_logger.WriteLine3("\t\tThe Vector has {0} available Axes", Array.Length(arAxes))
        # Axes
        self.m_logger.WriteLine5("\t\tThe current Axes is: {0}", oVector.axes)
        if Array.Length(arAxes) > 0:
            oVector.axes = str(arAxes[0])
            self.m_logger.WriteLine5("\t\tThe new Axes is: {0}", oVector.axes)
            Assert.assertEqual(arAxes[0], oVector.axes)

        else:
            self.m_logger.WriteLine("\t\tNo available Axes")

        def action110():
            oVector.axes = "Abcdefgh"

        TryCatchAssertBlock.DoAssert("Cannot set illegal Axes!", action110)
        # DrawAtPoint
        self.m_logger.WriteLine4("\t\tThe current DrawAtPoint flag is: {0}", oVector.draw_at_point)
        oVector.draw_at_point = False
        self.m_logger.WriteLine4("\t\tThe new DrawAtPoint flag is: {0}", oVector.draw_at_point)
        Assert.assertEqual(False, oVector.draw_at_point)

        def action111():
            oVector.point = "Satellite/Satellite1 Center Point"

        TryCatchAssertBlock.DoAssert("The Point should be readonly.", action111)
        oVector.draw_at_point = True
        self.m_logger.WriteLine4("\t\tThe new DrawAtPoint flag is: {0}", oVector.draw_at_point)
        Assert.assertEqual(True, oVector.draw_at_point)
        # AvailablePoints
        arPoints = oVector.available_points
        self.m_logger.WriteLine3("\t\tThe Vector has {0} available Points", Array.Length(arPoints))
        # Point
        self.m_logger.WriteLine5("\t\tThe current Point is: {0}", oVector.point)
        if Array.Length(arPoints) > 0:
            oVector.point = str(arPoints[0])
            self.m_logger.WriteLine5("\t\tThe new Point is: {0}", oVector.point)
            Assert.assertEqual(arPoints[0], oVector.point)

        else:
            self.m_logger.WriteLine("\t\tNo available Points")

        def action112():
            oVector.point = "Abcdefgh"

        TryCatchAssertBlock.DoAssert("Cannot set illegal Point!", action112)
        # RADecVisible
        self.m_logger.WriteLine4("\t\tThe current RADecVisible flag is: {0}", oVector.ra_dec_visible)
        oVector.ra_dec_visible = False
        self.m_logger.WriteLine4("\t\tThe new RADecVisible flag is: {0}", oVector.ra_dec_visible)
        Assert.assertEqual(False, oVector.ra_dec_visible)

        def action113():
            oVector.ra_dec_unit_abrv = "mdeg"

        TryCatchAssertBlock.DoAssert("The RADecUnitAbrv should be readonly.", action113)
        oVector.ra_dec_visible = True
        self.m_logger.WriteLine4("\t\tThe new RADecVisible flag is: {0}", oVector.ra_dec_visible)
        Assert.assertEqual(True, oVector.ra_dec_visible)
        # RADecUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current RADecUnitAbrv is: {0}", oVector.ra_dec_unit_abrv)
        oVector.ra_dec_unit_abrv = "rad"
        self.m_logger.WriteLine5("\t\tThe new RADecUnitAbrv is: {0}", oVector.ra_dec_unit_abrv)
        Assert.assertEqual("rad", oVector.ra_dec_unit_abrv)

        def action114():
            oVector.ra_dec_unit_abrv = "Abc"

        TryCatchAssertBlock.DoAssert("Cannot set illegal RADecUnitAbrv!", action114)
        # MagnitudeDimension
        strMagnitudeDim: str = oVector.magnitude_dimension
        self.m_logger.WriteLine5("\t\tThe MagnitudeDimension is: {0}", strMagnitudeDim)
        if (strMagnitudeDim != "Unitless") and (strMagnitudeDim.find("Rate") == -1):
            strCurrentDimensionAbrv: str = self.m_oUnits.get_current_unit_abbrv(strMagnitudeDim)
            self.m_logger.WriteLine5("\t\tThe current DimensionAbbreviature is: {0}", strCurrentDimensionAbrv)
            # MagnitudeVisible
            self.m_logger.WriteLine4("\t\tThe current MagnitudeVisible flag is: {0}", oVector.magnitude_visible)
            oVector.magnitude_visible = False
            self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oVector.magnitude_visible)
            Assert.assertEqual(False, oVector.magnitude_visible)

            def action115():
                oVector.magnitude_unit_abrv = strCurrentDimensionAbrv

            TryCatchAssertBlock.DoAssert("The MagnitudeUnitAbrv should be readonly.", action115)
            oVector.magnitude_visible = True
            self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oVector.magnitude_visible)
            Assert.assertEqual(True, oVector.magnitude_visible)
            # MagnitudeUnitAbrv
            self.m_logger.WriteLine5("\t\tThe current MagnitudeUnitAbrv is: {0}", oVector.magnitude_unit_abrv)
            try:
                oVector.magnitude_unit_abrv = strCurrentDimensionAbrv
                self.m_logger.WriteLine5("\t\tThe new MagnitudeUnitAbrv is: {0}", oVector.magnitude_unit_abrv)

            except Exception as e:
                self.m_logger.WriteLine5("\t\tThe MagnitudeUnitAbrv is readonly in: {0}", oVector.name)
                self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

            def action116():
                oVector.magnitude_unit_abrv = "Abc"

            TryCatchAssertBlock.DoAssert("Cannot set illegal MagnitudeUnitAbrv!", action116)

        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        # PersistenceVisible (false)
        self.m_logger.WriteLine4("\t\tThe current PersistenceVisible flag is: {0}", oVector.persistence_visible)
        oVector.persistence_visible = False
        self.m_logger.WriteLine4("\t\tThe new PersistenceVisible flag is: {0}", oVector.persistence_visible)
        Assert.assertEqual(False, oVector.persistence_visible)

        def action117():
            oVector.duration = 123.456

        TryCatchAssertBlock.DoAssert("The Duration should be readonly.", action117)

        def action118():
            oVector.connect = AgEVectorAxesConnectType.eConnectLine

        TryCatchAssertBlock.DoAssert("The Connect should be readonly.", action118)

        def action119():
            oVector.transparent = True

        TryCatchAssertBlock.DoAssert("The Transparent should be readonly.", action119)
        # PersistenceVisible (true)
        oVector.persistence_visible = True
        self.m_logger.WriteLine4("\t\tThe new PersistenceVisible flag is: {0}", oVector.persistence_visible)
        Assert.assertEqual(True, oVector.persistence_visible)
        # Transparent
        self.m_logger.WriteLine4("\t\tThe current Transparent flag is: {0}", oVector.transparent)
        oVector.transparent = False
        self.m_logger.WriteLine4("\t\tThe new Transparent flag is: {0}", oVector.transparent)
        Assert.assertEqual(False, oVector.transparent)
        # Connect
        self.m_logger.WriteLine6("\t\tThe current Connect is: {0}", oVector.connect)
        oVector.connect = AgEVectorAxesConnectType.eConnectTrace
        self.m_logger.WriteLine6("\t\tThe new Connect is: {0}", oVector.connect)
        Assert.assertEqual(AgEVectorAxesConnectType.eConnectTrace, oVector.connect)
        # Duration
        self.m_logger.WriteLine6("\t\tThe current Duration is: {0}", oVector.duration)
        oVector.duration = 12345.6789
        self.m_logger.WriteLine6("\t\tThe new Duration is: {0}", oVector.duration)
        Assert.assertAlmostEqual(12345.6789, oVector.duration, delta=1e-05)

        def action120():
            oVector.duration = -1234.56789

        # range test
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action120)
        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))


# endregion


# region VOVaporTrail
class VOVaporTrailHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oVaporTrail: "IVOVaporTrail", oModel: "IVOModel", strDataPath: str):
        self.m_logger.WriteLine("----- VO VAPOR TRAIL TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oVaporTrail)
        Assert.assertIsNotNone(oModel)
        # Visible (false)
        self.m_logger.WriteLine4("\tThe current Visible is: {0}", oVaporTrail.visible)
        oVaporTrail.visible = False
        self.m_logger.WriteLine4("\tThe new Visible is: {0}", oVaporTrail.visible)
        Assert.assertFalse(oVaporTrail.visible)

        def action121():
            oVaporTrail.max_num_of_puffs = 34

        # MaxNumOfPuffs (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action121)

        def action122():
            oVaporTrail.density = 3.4

        # Density (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action122)

        def action123():
            oVaporTrail.radius = 34.56

        # Radius (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action123)

        def action124():
            oVaporTrail.color = Color.FromArgb(1218646)

        # Color (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action124)

        def action125():
            oVaporTrail.image_file = strDataPath + r"\STKData\VO/Textures/smoke.pgm"

        # ImageFile (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action125)

        def action126():
            oVaporTrail.use_attach_point = False

        # UseAttachPoint (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action126)

        def action127():
            oVaporTrail.attach_point_name = "InvalidPointName"

        # AttachPointName (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action127)
        # Visible (true)
        oVaporTrail.visible = True
        self.m_logger.WriteLine4("\tThe new Visible is: {0}", oVaporTrail.visible)
        Assert.assertTrue(oVaporTrail.visible)
        # MaxNumOfPuffs
        self.m_logger.WriteLine3("\tThe current MaxNumOfPuffs is: {0}", oVaporTrail.max_num_of_puffs)
        oVaporTrail.max_num_of_puffs = 34
        self.m_logger.WriteLine3("\tThe new MaxNumOfPuffs is: {0}", oVaporTrail.max_num_of_puffs)
        Assert.assertEqual(34, oVaporTrail.max_num_of_puffs)

        def action128():
            oVaporTrail.max_num_of_puffs = 12345

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action128)
        # Density
        self.m_logger.WriteLine6("\tThe current Density is: {0}", oVaporTrail.density)
        oVaporTrail.density = 123.456
        self.m_logger.WriteLine6("\tThe new Density is: {0}", oVaporTrail.density)
        Assert.assertAlmostEqual(123.456, oVaporTrail.density, delta=0.0001)

        def action129():
            oVaporTrail.density = 12345.6789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action129)
        # Radius
        self.m_logger.WriteLine6("\tThe current Radius is: {0}", oVaporTrail.radius)
        oVaporTrail.radius = 1234.56
        self.m_logger.WriteLine6("\tThe new Radius is: {0}", oVaporTrail.radius)
        Assert.assertAlmostEqual(1234.56, oVaporTrail.radius, delta=0.001)

        def action130():
            oVaporTrail.radius = -12345.6789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action130)
        # StartTime / EndTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oVaporTrail.display_interval.get_start_epoch())
        self.m_logger.WriteLine6("\tThe current EndTime is: {0}", oVaporTrail.display_interval.get_stop_epoch())
        oVaporTrail.display_interval.set_start_and_stop_times("11 Jul 1999 05:00:00.000", "13 Jul 1999 15:00:00.000")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oVaporTrail.display_interval.get_start_epoch())
        Assert.assertEqual("11 Jul 1999 05:00:00.000", oVaporTrail.display_interval.get_start_epoch().time_instant)
        self.m_logger.WriteLine6("\tThe new EndTime is: {0}", oVaporTrail.display_interval.get_stop_epoch())
        Assert.assertEqual("13 Jul 1999 15:00:00.000", oVaporTrail.display_interval.get_stop_epoch().time_instant)
        # Color
        self.m_logger.WriteLine6("\tThe current Color is: {0}", oVaporTrail.color)
        oVaporTrail.color = Color.FromArgb(4660)
        self.m_logger.WriteLine6("\tThe new Color is: {0}", oVaporTrail.color)
        AssertEx.AreEqual(Color.FromArgb(4660), oVaporTrail.color)
        # ImageFile
        self.m_logger.WriteLine5("\tThe current ImageFile is: {0}", oVaporTrail.image_file)
        oVaporTrail.image_file = strDataPath + r"\STKData\VO\Textures\smoke.pgm"
        self.m_logger.WriteLine5("\tThe new ImageFile is: {0}", oVaporTrail.image_file)
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Textures", "smoke.pgm"), oVaporTrail.image_file)

        def action131():
            oVaporTrail.image_file = "InvalidImageFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action131)

        # AvailableAttachPoints
        file: "IVOModelFile" = clr.CastAs(oModel.model_data, IVOModelFile)
        arAvailablePoints = oVaporTrail.available_attach_points
        self.m_logger.WriteLine3(
            "\tThe current model contains: {0} available attach points.", Array.Length(arAvailablePoints)
        )
        if file.filename.endswith("launchvehicle.dae") or file.filename.endswith("missile.mdl"):
            Assert.assertEqual(3, Array.Length(arAvailablePoints))

        else:
            Assert.assertEqual(0, Array.Length(arAvailablePoints))

            def action132():
                oVaporTrail.use_attach_point = False

            TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action132)

        def action133():
            oVaporTrail.attach_point_name = "InvalidPointName"

        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action133)

        # Load a VOModel with attached points
        oModel.visible = True
        Assert.assertTrue(oModel.visible)
        oModel.model_type = AgEModelType.eModelFile
        Assert.assertEqual(AgEModelType.eModelFile, oModel.model_type)
        oModelFile: "IVOModelFile" = clr.Convert(oModel.model_data, IVOModelFile)
        Assert.assertIsNotNone(oModelFile)
        self.m_logger.WriteLine5("\tThe current VOModel file is: {0}", oModelFile.filename)
        oModelFile.filename = strDataPath + r"\STKData\VO\Models\Space\pegasus.mdl"
        self.m_logger.WriteLine5("\tThe new VOModel file is: {0}", oModelFile.filename)
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Models", "Space", "pegasus.mdl"), oModelFile.filename)
        arAvailablePoints = oVaporTrail.available_attach_points
        self.m_logger.WriteLine3(
            "\tThe current model contains: {0} available attach points.", Array.Length(arAvailablePoints)
        )
        Assert.assertEqual(3, Array.Length(arAvailablePoints))
        # UseAttachPoint (false)
        self.m_logger.WriteLine4("\tThe current UseAttachPoint is: {0}", oVaporTrail.use_attach_point)
        oVaporTrail.use_attach_point = False
        self.m_logger.WriteLine4("\tThe new UseAttachPoint is: {0}", oVaporTrail.use_attach_point)
        Assert.assertFalse(oVaporTrail.use_attach_point)

        def action134():
            oVaporTrail.attach_point_name = "InvalidPointName"

        # AttachPointName (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action134)
        # UseAttachPoint (true)
        oVaporTrail.use_attach_point = True
        self.m_logger.WriteLine4("\tThe new UseAttachPoint is: {0}", oVaporTrail.use_attach_point)
        Assert.assertTrue(oVaporTrail.use_attach_point)
        # AttachPointName
        self.m_logger.WriteLine5("\tThe current AttachPointName is: {0}", oVaporTrail.attach_point_name)

        iIndex: int = 0
        while iIndex < Array.Length(arAvailablePoints):
            oVaporTrail.attach_point_name = str(arAvailablePoints[iIndex])
            self.m_logger.WriteLine5("\tThe new AttachPointName is: {0}", oVaporTrail.attach_point_name)
            Assert.assertEqual(str(arAvailablePoints[iIndex]), oVaporTrail.attach_point_name)

            iIndex += 1

        def action135():
            oVaporTrail.attach_point_name = "InvalidPointName"

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action135)
        self.m_logger.WriteLine("----- VO VAPOR TRAIL TEST ----- END -----")

    # endregion
