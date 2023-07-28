from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


# region VOMarkerHelper
class VOMarkerHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

    # endregion

    # region Test_IAgVOMarkerFile method
    def Test_IAgVOMarkerFile(self, oFile: "IVOMarkerFile"):
        oFile.Filename = TestBase.PathCombine("STKData", "VO", "Markers", "Star.ppm")
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Markers", "Star.ppm"), oFile.Filename)
        oFile.Filename = TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm")
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm"), oFile.Filename)

        def action1():
            oFile.Filename = TestBase.PathCombine("STKData", "VO", "Markers", "Bogus.ppm")

        TryCatchAssertBlock.ExpectedException("does not exist", action1)

        Assert.assertEqual(
            Path.GetFullPath(TestBase.PathCombine(TestBase.GetSTKHomeDir(), "STKData", "VO", "Markers", "Ship.ppm")),
            Path.GetFullPath(oFile.FilePath),
        )

        oFile.IsTransparent = False
        Assert.assertFalse(oFile.IsTransparent)
        oFile.IsTransparent = True
        Assert.assertTrue(oFile.IsTransparent)

        oFile.UseSoftTransparency = False
        Assert.assertFalse(oFile.UseSoftTransparency)
        oFile.UseSoftTransparency = True
        Assert.assertTrue(oFile.UseSoftTransparency)

    # endregion

    # region Run method
    def Run(self, oMarker: "IVOMarker", bIsVehicle: bool):
        Assert.assertIsNotNone(oMarker)

        oMarker.Visible = False
        Assert.assertFalse(oMarker.Visible)

        def action2():
            oMarker.Angle = 1.23

        TryCatchAssertBlock.ExpectedException("read only", action2)

        def action3():
            oMarker.MarkerType = AgEMarkerType.eImageFile

        TryCatchAssertBlock.ExpectedException("read only", action3)

        def action4():
            oMarker.OrientationMode = AgEVOMarkerOrientation.eVOMarkerOrientationAngle

        TryCatchAssertBlock.ExpectedException("read-only", action4)

        def action5():
            oMarker.PixelSize = 1

        TryCatchAssertBlock.ExpectedException("read-only", action5)

        def action6():
            oMarker.XOrigin = 0

        TryCatchAssertBlock.ExpectedException("read-only", action6)
        # BUG86168 TryCatchAssertBlock.ExpectedException("read-only", delegate() { oMarker.YOrigin = 0; }); "Value does not fall within the expected range"

        oMarker.Visible = True
        Assert.assertTrue(oMarker.Visible)

        oMarker.MarkerType = AgEMarkerType.eShape
        Assert.assertEqual(AgEMarkerType.eShape, oMarker.MarkerType)

        oShape: IVOMarkerShape = clr.CastAs(oMarker.MarkerData, IVOMarkerShape)
        Assert.assertIsNotNone(oShape)
        oShape.Style = AgE3dMarkerShape.e3dShapeCircle
        Assert.assertEqual(AgE3dMarkerShape.e3dShapeCircle, oShape.Style)
        oShape.Style = AgE3dMarkerShape.e3dShapePoint
        Assert.assertEqual(AgE3dMarkerShape.e3dShapePoint, oShape.Style)

        def action7():
            voMarkerFileX = clr.Convert(oMarker.MarkerData, IVOMarkerFile)

        TryCatchAssertBlock.DoAssertInvalidCast(action7)

        oMarker.MarkerType = (
            AgEMarkerType.eImageFile
        )  # This property will not be set to this enum. See below, and see helpstrings.
        oMarker.SetMarkerImageFile(
            TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm")
        )  # This will set the MarkerType to eImageFile

        Assert.assertEqual(AgEMarkerType.eImageFile, oMarker.MarkerType)
        oFile: IVOMarkerFile = clr.CastAs(oMarker.MarkerData, IVOMarkerFile)
        Assert.assertIsNotNone(oFile)
        self.Test_IAgVOMarkerFile(oFile)

        def action8():
            oShape = clr.Convert(oMarker.MarkerData, IVOMarkerShape)

        TryCatchAssertBlock.DoAssertInvalidCast(action8)

        oMarker.PixelSize = 12
        Assert.assertEqual(12, oMarker.PixelSize)

        def action9():
            oMarker.PixelSize = 1234

        TryCatchAssertBlock.ExpectedException("invalid", action9)

        oMarker.XOrigin = AgEVOMarkerOriginType.eRight
        Assert.assertEqual(AgEVOMarkerOriginType.eRight, oMarker.XOrigin)

        def action10():
            oMarker.XOrigin = AgEVOMarkerOriginType.eTop

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action10)

        oMarker.YOrigin = AgEVOMarkerOriginType.eBottom
        Assert.assertEqual(AgEVOMarkerOriginType.eBottom, oMarker.YOrigin)

        def action11():
            oMarker.YOrigin = AgEVOMarkerOriginType.eLeft

        TryCatchAssertBlock.ExpectedException("One or more arguments are invalid", action11)

        oMarker.OrientationMode = AgEVOMarkerOrientation.eVOMarkerOrientationNone
        Assert.assertEqual(AgEVOMarkerOrientation.eVOMarkerOrientationNone, oMarker.OrientationMode)

        def action12():
            oMarker.Angle = 1.23

        TryCatchAssertBlock.ExpectedException("read only", action12)
        if bIsVehicle:
            oMarker.OrientationMode = AgEVOMarkerOrientation.eVOMarkerOrientationFollowDirection
            Assert.assertEqual(AgEVOMarkerOrientation.eVOMarkerOrientationFollowDirection, oMarker.OrientationMode)

            oMarker.Angle = 1.23456
            Assert.assertEqual(1.23456, oMarker.Angle)

            def action13():
                oMarker.Angle = 361

            TryCatchAssertBlock.ExpectedException("invalid", action13)

        else:

            def action14():
                oMarker.OrientationMode = AgEVOMarkerOrientation.eVOMarkerOrientationFollowDirection

            TryCatchAssertBlock.ExpectedException("Only supported for vehicle", action14)

        oMarker.OrientationMode = AgEVOMarkerOrientation.eVOMarkerOrientationAngle
        Assert.assertEqual(AgEVOMarkerOrientation.eVOMarkerOrientationAngle, oMarker.OrientationMode)

        oMarker.Angle = 1.23456
        Assert.assertEqual(1.23456, oMarker.Angle)

        def action15():
            oMarker.Angle = 361

        TryCatchAssertBlock.ExpectedException("invalid", action15)


# endregion


# region VOModelHelper
class VOModelHelper(object):
    def __init__(self, root: "IStkObjectRoot", oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self._root = root
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oModel: "IVOModel"):
        Assert.assertIsNotNone(oModel)
        self.m_logger.WriteLine("VO Model test:")

        # Visible
        self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oModel.Visible)
        oModel.Visible = False
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oModel.Visible)
        Assert.assertFalse(oModel.Visible)

        def action16():
            oModel.ScaleValue = 3.3

        TryCatchAssertBlock.DoAssert("The Scale is readonly when Visible flag is False.", action16)

        def action17():
            oModel.ModelType = AgEModelType.eModelFile

        TryCatchAssertBlock.DoAssert("The ModelType is readonly when Visible flag is False.", action17)

        oModel.Visible = True
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oModel.Visible)
        Assert.assertTrue(oModel.Visible)
        # ScaleValue
        self.m_logger.WriteLine6("\tThe current Scale flag is: {0}", oModel.ScaleValue)
        oModel.ScaleValue = 3.33
        self.m_logger.WriteLine6("\tThe new Scale flag is: {0}", oModel.ScaleValue)
        Assert.assertEqual(3.33, oModel.ScaleValue)

        def action18():
            oModel.ScaleValue = -12.34

        TryCatchAssertBlock.DoAssert("Cannot set illegal ScaleValue (out of range)!", action18)

        # ModelType (File)
        self.m_logger.WriteLine6("\tThe current ModelType is: {0}", oModel.ModelType)
        oModel.ModelType = AgEModelType.eModelFile
        self.m_logger.WriteLine6("\tThe new ModelType is: {0}", oModel.ModelType)
        Assert.assertEqual(AgEModelType.eModelFile, oModel.ModelType)
        oModelFile: IVOModelFile = clr.CastAs(oModel.ModelData, IVOModelFile)
        Assert.assertIsNotNone(oModelFile)
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.Filename)
        oModelFile.Filename = TestBase.GetScenarioFile(TestBase.PathCombine("VO", "Models", "pegasus.mdl"))
        Assert.assertEqual(TestBase.PathCombine("VO", "Models", "pegasus.mdl"), oModelFile.Filename)
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.Filename)

        def action19():
            oModelFile.Filename = "sat.mdl"

        TryCatchAssertBlock.DoAssert("The Filename should not allow to set invalid filename.", action19)

        def action20():
            oModelFile.Filename = ""

        TryCatchAssertBlock.DoAssert("The Filename should not allow to set invalid filename.", action20)
        oModelFile.Filename = TestBase.GetScenarioFile(TestBase.PathCombine("VO", "Models", "satellite.dae"))
        Assert.assertEqual(TestBase.PathCombine("VO", "Models", "satellite.dae"), oModelFile.Filename)
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.Filename)
        # FilePath
        Assert.assertEqual(
            TestBase.GetScenarioFile(TestBase.PathCombine("VO", "Models", "satellite.dae")), oModelFile.FilePath
        )

        # ModelType (List)
        oModel.ModelType = AgEModelType.eModelList
        self.m_logger.WriteLine6("\tThe new ModelType is: {0}", oModel.ModelType)
        Assert.assertEqual(AgEModelType.eModelList, oModel.ModelType)
        oModelList: IVOModelCollection = clr.CastAs(oModel.ModelData, IVOModelCollection)
        Assert.assertIsNotNone(oModelList)
        iSize = oModelList.Count
        self.m_logger.WriteLine3("\t\tThe Model list collection contains: {0} elements", iSize)

        iIndex = 0
        while iIndex < iSize:
            self.m_logger.WriteLine8(
                "\t\t\tElement {0}: ModelFile = {1}, SwitchTime = {2}",
                iIndex,
                oModelList[iIndex].VOModelFile.FilePath,
                oModelList[iIndex].SwitchTime,
            )

            iIndex += 1

        oModelList.Add(
            "1 Jan 2007 12:00:00.000", TestBase.GetScenarioFile(TestBase.PathCombine("VO", "Models", "satellite.dae"))
        )
        Assert.assertEqual(2, oModelList.Count)
        oModelList.Remove(1)
        Assert.assertEqual(1, oModelList.Count)

        # set DateFormat
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DateFormat")
        self.m_logger.WriteLine5("\t\tThe current DateFormat is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DateFormat", "EpSec")
        self.m_logger.WriteLine5("\t\tThe new DateFormat is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DateFormat"))
        Assert.assertEqual("EpSec", self.m_oUnits.GetCurrentUnitAbbrv("DateFormat"))

        time = float(oModelList[0].SwitchTime)
        self.m_logger.WriteLine6("\t\tOriginal SwitchTime = {0}", oModelList[0].SwitchTime)
        self.m_logger.WriteLine6("\t\tDouble format SwitchTime = {0}", time)

        def action21():
            oModelList.Add(oModelList[0].SwitchTime, oModelList[0].VOModelFile.FilePath)

        TryCatchAssertBlock.DoAssert("The Add() method should not allow to add duplicated elements.", action21)
        oModelList.Add((time + 1), oModelList[0].VOModelFile.FilePath)
        iSize = oModelList.Count
        self.m_logger.WriteLine3("\t\tThe Model list collection contains: {0} elements", iSize)

        iIndex = 0
        while iIndex < iSize:
            self.m_logger.WriteLine8(
                "\t\t\tElement {0}: ModelFile = {1}, SwitchTime = {2}",
                iIndex,
                oModelList[iIndex].VOModelFile.FilePath,
                oModelList[iIndex].SwitchTime,
            )

            iIndex += 1

        if iSize > 1:
            oModelList.Remove(0)
            self.m_logger.WriteLine3("\t\tAfter Remove(0) the ModelList contains: {0} elements", oModelList.Count)
            for oItem in oModelList:
                self.m_logger.WriteLine7(
                    "\t\t\tElement (before modification): ModelFile = {0}, SwitchTime = {1}",
                    oItem.VOModelFile.FilePath,
                    oItem.SwitchTime,
                )
                oItem.VOModelFile.Filename = oItem.VOModelFile.Filename
                oItem.SwitchTime = time - 12
                self.m_logger.WriteLine7(
                    "\t\t\tElement (after modification): ModelFile = {0}, SwitchTime = {1}",
                    oItem.VOModelFile.FilePath,
                    oItem.SwitchTime,
                )

                voModelFile = oItem.VOModelFile
                Assert.assertEqual((TestBase.PathCombine("VO", "Models", "satellite.dae")), voModelFile.Filename)
                Assert.assertTrue((TestBase.PathCombine("VO", "Models", "satellite.dae") in voModelFile.FilePath))
                voModelFile.Filename = TestBase.GetScenarioFile(TestBase.PathCombine("VO", "Models", "pegasus.mdl"))
                Assert.assertEqual(TestBase.PathCombine("VO", "Models", "pegasus.mdl"), voModelFile.Filename)
                Assert.assertTrue((TestBase.PathCombine("VO", "Models", "pegasus.mdl") in voModelFile.FilePath))

                def action22():
                    voModelFile.Filename = TestBase.GetScenarioFile(TestBase.PathCombine("VO", "Models", "bogus.dae"))

                TryCatchAssertBlock.ExpectedException("file does not exist", action22)

        # restore DateFormat
        self.m_oUnits.SetCurrentUnit("DateFormat", strUnit)
        self.m_logger.WriteLine5("\t\tThe new DateFormat (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DateFormat"))

        # DetailThreshold test
        self.VODetailThreshold(oModel.DetailThreshold)

        # Articulation test
        self.VOArticulation(oModel.Articulation)

        # ------------------------------------------------------------
        # Testing the behavior of the object's model when
        # the graphics updates have been suspended using BeginUpdate.
        # The expected behavior is for the Object Model to silently
        # load the specified model even if the BeginUpdate was
        # invoked. This way the users do not have to call EndUpdate
        # after setting a new model to set desired articulations.
        # ------------------------------------------------------------
        oModel.ModelType = AgEModelType.eModelFile
        Assert.assertTrue((oModel.ModelType == AgEModelType.eModelFile))
        oldModel = (clr.CastAs(oModel.ModelData, IVOModelFile)).Filename
        self._root.BeginUpdate()
        try:
            oModel.ModelType = AgEModelType.eModelFile
            modelFile: IVOModelFile = clr.CastAs(oModel.ModelData, IVOModelFile)
            modelFile.Filename = "\\STKData\\VO\\Models\\Space\\hubble.mdl"

            oModel.Articulation.SetTransValue(0, "HGA_Arm_1", "Fold", 90)

        finally:
            self._root.EndUpdate()

        oModel.ModelType = AgEModelType.eModelList
        modelList: IVOModelCollection = clr.CastAs(oModel.ModelData, IVOModelCollection)
        while modelList.Count > 1:
            modelList.Remove((modelList.Count - 1))
        modelList[0].VOModelFile.Filename = oldModel

        def action23():
            oModel.Articulation.SetTransValue(0, "HGA_Arm_1", "Fold", 90)

        TryCatchAssertBlock.DoAssert("Must not allow setting invalid articulations.", action23)

        self._root.BeginUpdate()
        try:
            modelList[0].VOModelFile.Filename = "\\STKData\\VO\\Models\\Space\\hubble.mdl"
            oModel.Articulation.SetTransValue(0, "HGA_Arm_1", "Fold", 90)

        finally:
            self._root.EndUpdate()
            oModel.ModelType = AgEModelType.eModelFile

    # endregion

    # region VODetailThreshold
    def VODetailThreshold(self, oDetail: "IVODetailThreshold"):
        Assert.assertIsNotNone(oDetail)
        self.m_logger.WriteLine("VO DetailThreshold test:")
        # set DistanceUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # EnableDetailThreshold
        self.m_logger.WriteLine4("\tThe current EnableDetailThreshold flag is: {0}", oDetail.EnableDetailThreshold)
        oDetail.EnableDetailThreshold = False
        self.m_logger.WriteLine4("\tThe new EnableDetailThreshold flag is: {0}", oDetail.EnableDetailThreshold)
        Assert.assertEqual(False, oDetail.EnableDetailThreshold)
        try:
            bCaught = False
            oDetail.All = 2.2

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The ModelDetail is readonly when Enable flag is False.")

        try:
            bCaught = False
            oDetail.MarkerLabel = 3.3

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The MarkerLabel is readonly when Enable flag is False.")

        try:
            bCaught = False
            oDetail.Marker = 4.4

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Marker is readonly when Enable flag is False.")

        try:
            bCaught = False
            oDetail.All = 5.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The ModelDetail is readonly when Enable flag is False.")

        try:
            bCaught = False
            oDetail.Point = 6.6

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Point Detail is readonly when Enable flag is False.")

        oDetail.EnableDetailThreshold = True
        self.m_logger.WriteLine4("\tThe new EnableDetailThreshold flag is: {0}", oDetail.EnableDetailThreshold)
        Assert.assertEqual(True, oDetail.EnableDetailThreshold)
        # Marker
        self.m_logger.WriteLine6("\t\tThe current Marker is: {0}", oDetail.Marker)
        oDetail.Marker = 99.99
        self.m_logger.WriteLine6("\t\tThe new Marker is: {0}", oDetail.Marker)
        Assert.assertEqual(99.99, oDetail.Marker)
        try:
            bCaught = False
            oDetail.Marker = -2.2

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal Marker value!")

        # MarkerLabel
        self.m_logger.WriteLine6("\t\tThe current Marker Label is: {0}", oDetail.MarkerLabel)
        oDetail.MarkerLabel = 88.88
        self.m_logger.WriteLine6("\t\tThe new Marker Label is: {0}", oDetail.MarkerLabel)
        Assert.assertEqual(88.88, oDetail.MarkerLabel)
        try:
            bCaught = False
            oDetail.MarkerLabel = -3.3

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal MarkerLabel value!")

        # ModelLabel
        self.m_logger.WriteLine6("\t\tThe current Model Label is: {0}", oDetail.ModelLabel)
        oDetail.ModelLabel = 77.77
        self.m_logger.WriteLine6("\t\tThe new Model Label is: {0}", oDetail.ModelLabel)
        Assert.assertAlmostEqual(77.77, oDetail.ModelLabel, delta=0.001)
        try:
            bCaught = False
            oDetail.ModelLabel = -4.4

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal ModelLabel value!")

        # All
        self.m_logger.WriteLine6("\t\tThe current Model Detail is: {0}", oDetail.All)
        oDetail.All = 66.66
        self.m_logger.WriteLine6("\t\tThe new Model Detail is: {0}", oDetail.All)
        Assert.assertEqual(66.66, oDetail.All)
        try:
            bCaught = False
            oDetail.All = -5.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal All value!")

        # Point
        self.m_logger.WriteLine6("\t\tThe current Point Detail is: {0}", oDetail.Point)
        oDetail.Point = 55.55
        self.m_logger.WriteLine6("\t\tThe new Point Detail is: {0}", oDetail.Point)
        Assert.assertEqual(55.55, oDetail.Point)
        try:
            bCaught = False
            oDetail.Point = -6.6

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal Point value!")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

    # endregion

    # region VOArticulation
    def VOArticulation(self, oArticulation: "IVOModelArtic"):
        Assert.assertIsNotNone(oArticulation)

        oArticulation.EnableDefaultSave = False
        Assert.assertEqual(False, oArticulation.EnableDefaultSave)
        oArticulation.EnableDefaultSave = True
        Assert.assertEqual(True, oArticulation.EnableDefaultSave)

        oArticulation.SaveArticFileOnSave = False
        Assert.assertEqual(False, oArticulation.SaveArticFileOnSave)
        oArticulation.SaveArticFileOnSave = True
        Assert.assertEqual(True, oArticulation.SaveArticFileOnSave)

        oArticulation.SaveArticFileOnSave = False
        Assert.assertEqual(False, oArticulation.SaveArticFileOnSave)
        oArticulation.SaveArticFileOnSave = True
        Assert.assertEqual(True, oArticulation.SaveArticFileOnSave)

        oArticulation.UseObjectColorForModel = False
        Assert.assertFalse(oArticulation.UseObjectColorForModel)
        oArticulation.UseObjectColorForModel = True
        Assert.assertTrue(oArticulation.UseObjectColorForModel)

        articFile = oArticulation.VOArticulationFile
        oArticulation.UseArticulationFile = False

        def action24():
            articFile.Filename = TestBase.GetScenarioFile("Test.sama")

        TryCatchAssertBlock.ExpectedException("read-only", action24)

        oArticulation.UseArticulationFile = True

        def action25():
            articFile.Filename = TestBase.GetScenarioFile("Bogus.sama")

        TryCatchAssertBlock.ExpectedException("not found", action25)

        articFile.Filename = TestBase.GetScenarioFile("Test.sama")
        Assert.assertTrue(("Test.sama" in articFile.Filename))

        articFile.Reload()

        # LODs test
        self.m_logger.WriteLine3("\tThe number of LODs is: {0}", oArticulation.LODCount)

        iIndex = 0
        while iIndex < oArticulation.LODCount:
            self.m_logger.WriteLine3("\t\tLODs: {0}", iIndex)
            arAvailableArtic = oArticulation.GetAvailableArticulations(iIndex)
            self.m_logger.WriteLine3("\t\t\tThere are {0} available Articulations.", Array.Length(arAvailableArtic))

            i = 0
            while i < Array.Length(arAvailableArtic):
                strArtic = str(arAvailableArtic[i])
                self.m_logger.WriteLine7("\t\t\t\tArticulation {0} is: {1}", i, strArtic)
                # TransCollection test
                oTransformations = oArticulation.GetAvailableTransformations(iIndex, strArtic)
                Assert.assertIsNotNone(oTransformations)
                self.m_logger.WriteLine5("\t\t\t\tTransformation name is: {0}.", oTransformations.Name)
                self.m_logger.WriteLine3("\t\t\t\tThere are {0} available Transformations.", oTransformations.Count)

                j = 0
                while j < oTransformations.Count:
                    oElement = oTransformations[j]
                    strTrans = oElement.Name
                    self.m_logger.WriteLine7("\t\t\t\t\tTransformation {0} is: {1}", j, strTrans)
                    self.m_logger.WriteLine8(
                        "\t\t\t\t\t\tCurrent value: {0} [Min = {1}, Max = {2}]",
                        oElement.Value,
                        oElement.Min,
                        oElement.Max,
                    )
                    dMax = oElement.Max if ((Math.Abs(oElement.Max) > Math.Abs(oElement.Min))) else oElement.Min
                    dMin = oElement.Max if ((Math.Abs(oElement.Max) < Math.Abs(oElement.Min))) else oElement.Min
                    dMidle = ((dMax - dMin)) / 2.0
                    oElement.Value = dMidle
                    oArticulation.SetTransValue(iIndex, strArtic, strTrans, dMidle)
                    self.m_logger.WriteLine6(
                        "\t\t\t\t\t\tNew value: {0}", oArticulation.GetTransValue(iIndex, strArtic, strTrans)
                    )
                    Assert.assertEqual(dMidle, oArticulation.GetTransValue(iIndex, strArtic, strTrans))
                    try:
                        bCaught = False
                        oElement.Value = dMax * 2
                        self.m_logger.WriteLine6("\t\t\t\t\t\tNew value (illegal): {0}", oElement.Value)

                    except Exception as e:
                        bCaught = True
                        self.m_logger.WriteLine5("\t\t\t\t\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set illegal value (out of range)!")

                    j += 1

                # Collection enumeration test
                for oItem in oTransformations:
                    Assert.assertIsNotNone(oItem)

                i += 1

            iIndex += 1


# endregion


# region VOTargetModelHelper
class VOTargetModelHelper(object):
    def __init__(self, root: "IStkObjectRoot", oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self._root = root
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oModel: "IPointTargetVOModel"):
        Assert.assertIsNotNone(oModel)
        # IsPointVisible (false)
        self.m_logger.WriteLine4("\tThe current IsPointVisible is: {0}", oModel.IsPointVisible)
        oModel.IsPointVisible = False
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.IsPointVisible)
        Assert.assertEqual(False, oModel.IsPointVisible)

        def action26():
            oModel.PointSize = 12.3456

        # PointSize
        TryCatchAssertBlock.DoAssert("Allows to modify a readonly property!", action26)
        # IsPointVisible (true)
        oModel.IsPointVisible = True
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.IsPointVisible)
        Assert.assertEqual(True, oModel.IsPointVisible)
        # PointSize
        self.m_logger.WriteLine6("\tThe current PointSize is: {0}", oModel.PointSize)
        oModel.PointSize = 12.3456
        self.m_logger.WriteLine6("\tThe new PointSize is: {0}", oModel.PointSize)
        Assert.assertAlmostEqual(12.3456, float(oModel.PointSize), delta=0.0001)

        def action27():
            oModel.PointSize = 123.456

        TryCatchAssertBlock.DoAssert("Allows to set illegal value!", action27)

        def action28():
            oModel.GltfReflectionMapType = AgEModelGltfReflectionMapType.eModelGltfProceduralEnvironment

        # GLTF

        TryCatchAssertBlock.ExpectedException("glTF settings are not available", action28)
        (
            clr.CastAs(oModel.ModelData, IVOModelFile)
        ).Filename = r"STKData\VO\Models\Land\facility.glb"  # need a model that supports GLTF
        oModel.GltfReflectionMapType = AgEModelGltfReflectionMapType.eModelGltfProceduralEnvironment
        Assert.assertEqual(AgEModelGltfReflectionMapType.eModelGltfProceduralEnvironment, oModel.GltfReflectionMapType)

        def action29():
            x = oModel.GltfImageBased

        TryCatchAssertBlock.ExpectedException("is not set to Image Based", action29)

        oModel.GltfReflectionMapType = AgEModelGltfReflectionMapType.eModelGltfImageBased
        Assert.assertEqual(AgEModelGltfReflectionMapType.eModelGltfImageBased, oModel.GltfReflectionMapType)

        gltfImageBased = oModel.GltfImageBased
        gltfImageBased.Filename = TestBase.GetScenarioFile("over_the_clouds.hdr")
        Assert.assertEqual("over_the_clouds.hdr", gltfImageBased.Filename)
        Assert.assertTrue(("over_the_clouds.hdr" in gltfImageBased.FilePath))

        gltfImageBased.ReflectionReferenceFrame = "Satellite/Satellite1 ICRF"
        Assert.assertEqual("Satellite/Satellite1 ICRF", gltfImageBased.ReflectionReferenceFrame)

        def action30():
            gltfImageBased.ReflectionReferenceFrame = "Satellite/Satellite1 Bogus"

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
        oPECollection = oModelPointing.PointableElements
        Assert.assertIsNotNone(oPECollection)
        # Count
        self.m_logger.WriteLine3("The Pointable Elements collection contains: {0} elements", oPECollection.Count)

        iIndex = 0
        while iIndex < oPECollection.Count:
            # Index
            self.m_logger.WriteLine5("\tElement: {0}", oPECollection[iIndex].PointingName)

            iIndex += 1

        self.m_logger.WriteLine3("The Pointable Elements collection contains: {0} elements.", oPECollection.Count)

        iIndex = 0
        while iIndex < oPECollection.Count:
            oElement = oPECollection[iIndex]
            Assert.assertIsNotNone(oElement)
            self.m_logger.WriteLine7("\tElement {0} is: {1}", iIndex, oElement.PointingName)

            def action31():
                oElement.PointingName = "NewName"

            TryCatchAssertBlock.DoAssert("The PointingName should be readonly!", action31)

            oHelper = LinkToObjectHelper()
            oHelper.Run(oElement.AssignedTargetObject, oElement.PointingName)

            iIndex += 1

        # Add
        self.m_logger.WriteLine3("The Pointable Elements collection still contains: {0} elements", oPECollection.Count)

        iIndex = 0
        while iIndex < oPECollection.Count:
            self.m_logger.WriteLine5("\tElement: {0}", oPECollection[iIndex].PointingName)

            iIndex += 1

        def action32():
            oNewElement = oPECollection.Add()

        TryCatchAssertBlock.DoAssert("The PointableElementsCollection should be readonly!", action32)

        def action33():
            oPECollection.RemoveAt(0)

        # RemoveAt
        TryCatchAssertBlock.DoAssert("The PointableElementsCollection should be readonly!", action33)

        def action34():
            oPECollection.RemoveAll()

        # RemoveAll
        TryCatchAssertBlock.DoAssert("The PointableElementsCollection should be readonly!", action34)
        self.m_logger.WriteLine3("The Pointable Elements collection still contains: {0} elements", oPECollection.Count)
        for oTempElement in oPECollection:
            self.m_logger.WriteLine5("\tElement: {0}", oTempElement.PointingName)

        # Testing model pointing intervals
        Assert.assertTrue((oPECollection.Count > 0))
        for oTempElement in oPECollection:
            oTempElement.Intervals.RemoveAll()
            Assert.assertEqual(
                0,
                oTempElement.Intervals.Count,
                (('Failed to clear intervals for the element "' + oTempElement.PointingName) + '"'),
            )

        # Planet Target
        sPlanetTargetObject = "Planet/MarsJPL"

        # Verify that we can add intervals to existing pointable elements
        for oTempElement in oPECollection:
            # need to use a full path
            self.m_logger.WriteLine(oTempElement.PointingName)
            oTempElement.AssignedTargetObject.BindTo(sPlanetTargetObject)
            Assert.assertEqual(sPlanetTargetObject, oTempElement.AssignedTargetObject.Name)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.AssignedTargetObject.Name)
            # Intervals
            nCount = oTempElement.Intervals.Count
            self.m_logger.WriteLine3("\t\tThe current number of intervals: {0}", nCount)
            oTempElement.Intervals.Add("1 Jul 1999 01:00:000.00", "1 Jul 1999 02:00:000.00")
            Assert.assertEqual((nCount + 1), oTempElement.Intervals.Count)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.Intervals.Count)
            self.PrintIntervals(oTempElement.Intervals)
            oTempElement.Intervals.Add("1 Jul 1999 03:00:000.00", "1 Jul 1999 04:00:000.00")
            Assert.assertEqual((nCount + 2), oTempElement.Intervals.Count)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.Intervals.Count)
            self.PrintIntervals(oTempElement.Intervals)

            def action35():
                oTempElement.Intervals.Add("1 Jul 1999 03:00:000.00", "1 Jul 1999 01:00:000.00")

            TryCatchAssertBlock.DoAssert("Should not allow to set illegal time interval!", action35)

        # adding a Sun target
        iCount = oPECollection.Count
        oModelPointing.AddInterval(
            oPECollection[0].PointingName, "Sun", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
        )
        Assert.assertEqual((iCount + 1), oPECollection.Count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.Count)
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.PointingName)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.AssignedTargetObject.Name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.Intervals.Count)
            self.PrintIntervals(oTempElement.Intervals)

        def action36():
            oModelPointing.AddInterval("WrongPointingName", "Sun", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00")

        TryCatchAssertBlock.DoAssert("Should not allow to set illegal interval!", action36)

        def action37():
            oModelPointing.AddInterval(
                oPECollection[2].PointingName, "WrongTargetName", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
            )

        TryCatchAssertBlock.DoAssert("Should not allow to set illegal interval!", action37)

        def action38():
            oModelPointing.AddInterval(
                oPECollection[2].PointingName, "Earth", "3 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
            )

        TryCatchAssertBlock.DoAssert("Should not allow to set illegal interval!", action38)

        # adding a Slew Interval target
        iCount = oPECollection.Count
        oModelPointing.AddInterval(
            oPECollection[1].PointingName, "Slew", "1 Jul 1999 02:00:000.00", "1 Jul 1999 03:00:000.00"
        )
        Assert.assertEqual((iCount + 1), oPECollection.Count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.Count)
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.PointingName)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.AssignedTargetObject.Name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.Intervals.Count)
            self.PrintIntervals(oTempElement.Intervals)

        # RemoveInterval
        oModelPointing.RemoveInterval(oPECollection[1].PointingName, "Slew")
        Assert.assertEqual(iCount, oPECollection.Count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.Count)
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.PointingName)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.AssignedTargetObject.Name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.Intervals.Count)
            self.PrintIntervals(oTempElement.Intervals)

        def action39():
            oModelPointing.RemoveInterval("WrongPointingName", "Sun")

        TryCatchAssertBlock.DoAssert("Should not allow to remove illegal interval!", action39)

        def action40():
            oModelPointing.RemoveInterval(oPECollection[2].PointingName, "WrongTargetName")

        TryCatchAssertBlock.DoAssert("Should not allow to remove illegal interval!", action40)

        def action41():
            oModelPointing.RemoveInterval(oPECollection[1].PointingName, "Earth")

        TryCatchAssertBlock.DoAssert("Should not allow to remove illegal interval!", action41)

        # Sort
        oPECollection.Sort()

        availObjects = oModelPointing.PointableElements[0].AssignedTargetObject.AvailableObjects
        for availObject in availObjects:
            self.m_logger.WriteLine5("Available target: {0}", availObject)
            Assert.assertTrue((not ("Slew" == availObject)))

        oModelPointing.PointableElements[0].Intervals.RemoveAll()

        i = 0
        while i < oModelPointing.PointableElements.Count:
            oModelPointing.PointableElements[i].Intervals.RemoveAll()

            i += 1

        oModelPointing.LoadIntervals(
            TestBase.GetScenarioFile("MdlPtgInts.int"), oModelPointing.PointableElements[0].PointingName
        )

        i = 0
        while i < oModelPointing.PointableElements.Count:
            self.m_logger.WriteLine(oModelPointing.PointableElements[i].PointingName)
            self.m_logger.WriteLine(oModelPointing.PointableElements[i].AssignedTargetObject.Name)
            self.PrintIntervals(oModelPointing.PointableElements[i].Intervals)

            i += 1

        def action42():
            oModelPointing.LoadIntervals(
                TestBase.GetScenarioFile("MdlPtgIntsBad.int"), oModelPointing.PointableElements[0].PointingName
            )

        TryCatchAssertBlock.DoAssert("This file is invalid and should throw an exception.", action42)

        self.m_logger.WriteLine("----- THE VO MODEL POINTING TEST ----- END -----")

    # endregion

    # region PrintIntervals method
    def PrintIntervals(self, oCollection: "IIntervalCollection"):
        iIndex = 0
        while iIndex < oCollection.Count:
            (oStart, oStop) = oCollection.GetInterval(iIndex)
            self.m_logger.WriteLine8("\t\t\tInterval {0}: StartTime = {1}, StopTime = {2}", iIndex, oStart, oStop)

            iIndex += 1


# endregion


# region VOOffsetsHelper
class VOOffsetsHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oOffset: "IVOOffset"):
        self.m_logger.WriteLine("----- THE VO OFFSET TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oOffset)

        # Rotational
        oRHelper = VOOffsetRotationalHelper(self.m_oUnits)
        oRHelper.Run(oOffset.Rotational)

        # Translational
        oTHelper = VOOffsetTranslationalHelper(self.m_oUnits)
        oTHelper.Run(oOffset.Translational)

        # Label
        oLHelper = VOOffsetLabelHelper(self.m_oUnits)
        oLHelper.Run(oOffset.Label, False)

        # Attach Point
        oAHelper = VOOffsetAttachHelper()
        oAHelper.Run(oOffset.AttachPoint)

        self.m_logger.WriteLine("----- THE VO OFFSET TEST ----- END -----")


# endregion


# region VOOffsetRotationalHelper
class VOOffsetRotationalHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oRotational: "IVOOffsetRotate"):
        Assert.assertIsNotNone(oRotational)
        self.m_logger.WriteLine("Offsets Rotational test:")
        # set AngleUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        # Enable flag
        self.m_logger.WriteLine4("\tThe current Enable flag is: {0}", oRotational.Enable)
        oRotational.Enable = False
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oRotational.Enable)
        Assert.assertEqual(False, oRotational.Enable)
        try:
            bCaught = False
            oRotational.X = 2.3456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The X should be readonly when Enable flag is False.")

        try:
            bCaught = False
            oRotational.Y = 1.234

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Y should be readonly when Enable flag is False.")

        try:
            bCaught = False
            oRotational.Z = -1.234

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Z should be readonly when Enable flag is False.")

        oRotational.Enable = True
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oRotational.Enable)
        Assert.assertEqual(True, oRotational.Enable)
        # X
        self.m_logger.WriteLine6("\t\tThe current X is: {0}", oRotational.X)
        oRotational.X = 2.3456
        self.m_logger.WriteLine6("\t\tThe new X is: {0}", oRotational.X)
        Assert.assertEqual(2.3456, oRotational.X)
        # Y
        self.m_logger.WriteLine6("\t\tThe current Y is: {0}", oRotational.Y)
        oRotational.Y = -1.23456
        self.m_logger.WriteLine6("\t\tThe new Y is: {0}", oRotational.Y)
        Assert.assertEqual(-1.23456, oRotational.Y)
        # Z
        self.m_logger.WriteLine6("\t\tThe current Z is: {0}", oRotational.Z)
        oRotational.Z = 1.234
        self.m_logger.WriteLine6("\t\tThe new Z is: {0}", oRotational.Z)
        Assert.assertEqual(1.234, oRotational.Z)
        # ranges test
        try:
            bCaught = False
            oRotational.X = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The X should not allow to set values > 180 deg.")

        try:
            bCaught = False
            oRotational.Y = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Y should not allow to set values < -180 deg.")

        try:
            bCaught = False
            oRotational.Z = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Z should not allow to set values > 180 deg.")

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))


# endregion


# region VOOffsetTranslationalHelper
class VOOffsetTranslationalHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oTranslational: "IVOOffsetTransformation"):
        Assert.assertIsNotNone(oTranslational)
        self.m_logger.WriteLine("Offsets Translational test:")
        # set DistanceUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # Enable flag
        self.m_logger.WriteLine4("\tThe current Enable flag is: {0}", oTranslational.Enable)
        oTranslational.Enable = False
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oTranslational.Enable)
        Assert.assertEqual(False, oTranslational.Enable)
        try:
            bCaught = False
            oTranslational.X = 34.56

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The X should be readonly when Enable flag is False.")

        try:
            bCaught = False
            oTranslational.Y = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Y should be readonly when Enable flag is False.")

        try:
            bCaught = False
            oTranslational.Z = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Z should be readonly when Enable flag is False.")

        oTranslational.Enable = True
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oTranslational.Enable)
        Assert.assertEqual(True, oTranslational.Enable)
        # X
        self.m_logger.WriteLine6("\t\tThe current X is: {0}", oTranslational.X)
        oTranslational.X = 123.456
        self.m_logger.WriteLine6("\t\tThe new X is: {0}", oTranslational.X)
        Assert.assertEqual(123.456, oTranslational.X)
        # Y
        self.m_logger.WriteLine6("\t\tThe current Y is: {0}", oTranslational.Y)
        oTranslational.Y = -123.456
        self.m_logger.WriteLine6("\t\tThe new Y is: {0}", oTranslational.Y)
        Assert.assertEqual(-123.456, oTranslational.Y)
        # Z
        self.m_logger.WriteLine6("\t\tThe current Z is: {0}", oTranslational.Z)
        oTranslational.Z = 23.4
        self.m_logger.WriteLine6("\t\tThe new Z is: {0}", oTranslational.Z)
        Assert.assertEqual(23.4, oTranslational.Z)
        # ranges test
        try:
            bCaught = False
            oTranslational.X = 123456789000000

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The X should not allow to set values > 1000000 km.")

        try:
            bCaught = False
            oTranslational.Y = -123456789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Y should not allow to set values < -1000000 km.")

        try:
            bCaught = False
            oTranslational.Z = 123456789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Z should not allow to set values > 1000000 km.")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))


# endregion


# region VOOffsetLabelHelper
class VOOffsetLabelHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oLabel: "IVOOffsetLabel", bReadOnly: bool):
        self.m_logger.WriteLine("----- VO OFFSET LABEL ----- BEGIN -----")
        Assert.assertIsNotNone(oLabel)
        # set SmallDistanceUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit")
        self.m_logger.WriteLine5("\tThe current SmallDistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("SmallDistanceUnit", "in")
        self.m_logger.WriteLine5(
            "\tThe new SmallDistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit")
        )
        Assert.assertEqual("in", self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit"))
        # bReadOnly
        self.m_logger.WriteLine4("\tRead-only flag: {0}", bReadOnly)
        if bReadOnly:

            def action43():
                oLabel.Enable = False

            # Enable
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action43)

            def action44():
                oLabel.OffsetFrame = AgEOffsetFrameType.eOffsetFrameCartesian

            # OffsetFrame
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action44)

            def action45():
                oLabel.X = 10.1

            # X
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action45)

            def action46():
                oLabel.Y = 11.11

            # Y
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action46)

            def action47():
                oLabel.Z = 12.12

            # Z
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action47)

        else:
            # Enable (false)
            self.m_logger.WriteLine4("\t\tThe current Enable is: {0}", oLabel.Enable)
            oLabel.Enable = False
            self.m_logger.WriteLine4("\t\tThe new Enable is: {0}", oLabel.Enable)
            Assert.assertEqual(False, oLabel.Enable)

            def action48():
                oLabel.OffsetFrame = AgEOffsetFrameType.eOffsetFrameCartesian

            # OffsetFrame
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action48)

            def action49():
                oLabel.X = 10.1

            # X
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action49)

            def action50():
                oLabel.Y = 11.11

            # Y
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action50)

            def action51():
                oLabel.Z = 12.12

            # Z
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action51)
            # Enable (true)
            oLabel.Enable = True
            self.m_logger.WriteLine4("\t\tThe new Enable is: {0}", oLabel.Enable)
            Assert.assertEqual(True, oLabel.Enable)
            # OffsetFrame (Cartesian)
            self.m_logger.WriteLine6("\t\t\tThe current OffsetFrame is: {0}", oLabel.OffsetFrame)
            oLabel.OffsetFrame = AgEOffsetFrameType.eOffsetFrameCartesian
            self.m_logger.WriteLine6("\t\t\tThe new OffsetFrame is: {0}", oLabel.OffsetFrame)
            Assert.assertEqual(AgEOffsetFrameType.eOffsetFrameCartesian, oLabel.OffsetFrame)
            # X
            self.m_logger.WriteLine6("\t\t\t\tThe current X is: {0}", oLabel.X)
            oLabel.X = 10.1
            self.m_logger.WriteLine6("\t\t\t\tThe new X is: {0}", oLabel.X)
            Assert.assertAlmostEqual(10.1, oLabel.X, delta=0.01)

            def action52():
                oLabel.X = 12340000000000000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action52)
            # Y
            self.m_logger.WriteLine6("\t\t\t\tThe current Y is: {0}", oLabel.Y)
            oLabel.Y = 11.11
            self.m_logger.WriteLine6("\t\t\t\tThe new Y is: {0}", oLabel.Y)
            Assert.assertAlmostEqual(11.11, oLabel.Y, delta=0.001)

            def action53():
                oLabel.Y = -34120000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action53)
            # Z
            self.m_logger.WriteLine6("\t\t\t\tThe current Z is: {0}", oLabel.Z)
            oLabel.Z = 12.12
            self.m_logger.WriteLine6("\t\t\t\tThe new Z is: {0}", oLabel.Z)
            Assert.assertAlmostEqual(12.12, oLabel.Z, delta=0.001)

            def action54():
                oLabel.Z = 210900000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action54)
            # OffsetFrame (Pixel)
            oLabel.OffsetFrame = AgEOffsetFrameType.eOffsetFramePixel
            self.m_logger.WriteLine6("\t\t\tThe new OffsetFrame is: {0}", oLabel.OffsetFrame)
            Assert.assertEqual(AgEOffsetFrameType.eOffsetFramePixel, oLabel.OffsetFrame)
            # X
            self.m_logger.WriteLine6("\t\t\t\tThe current X is: {0}", oLabel.X)
            oLabel.X = 13.13
            self.m_logger.WriteLine6("\t\t\t\tThe new X is: {0}", oLabel.X)
            Assert.assertAlmostEqual(13.13, oLabel.X, delta=0.001)

            def action55():
                oLabel.X = 12340000000000000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action55)
            # Y
            self.m_logger.WriteLine6("\t\t\t\tThe current Y is: {0}", oLabel.Y)
            oLabel.Y = 14.14
            self.m_logger.WriteLine6("\t\t\t\tThe new Y is: {0}", oLabel.Y)
            Assert.assertAlmostEqual(14.14, oLabel.Y, delta=0.001)

            def action56():
                oLabel.Y = -34120000000000.0

            TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value!", action56)

            def action57():
                oLabel.Z = 15.15

            # Z
            TryCatchAssertBlock.DoAssert("Should not allow to change a read-only property!", action57)

        # restore SmallDistanceUnit
        self.m_oUnits.SetCurrentUnit("SmallDistanceUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new SmallDistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("SmallDistanceUnit"))
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
        arPoints = oAttach.AvailableAttachPoints
        # Enable (false)
        self.m_logger.WriteLine4("\tThe current Enable flag is: {0}", oAttach.Enable)
        oAttach.Enable = False
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oAttach.Enable)
        Assert.assertEqual(False, oAttach.Enable)
        if Array.Length(arPoints) > 0:

            def action58():
                oAttach.AttachPtName = str(arPoints[0])

            TryCatchAssertBlock.DoAssert("Allows to modify a readonly property!", action58)

        # Enable (true)
        oAttach.Enable = True
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oAttach.Enable)
        Assert.assertEqual(True, oAttach.Enable)
        # AttachPtName
        self.m_logger.WriteLine5("\tThe current AttachPtName is: {0}", oAttach.AttachPtName)
        self.m_logger.WriteLine3("\tThe AvailableAttachPoints array contains: {0} elements.", Array.Length(arPoints))
        if Array.Length(arPoints) > 0:
            strName = str(arPoints[0])
            self.m_logger.WriteLine5("\t\tElement: {0}", strName)
            oAttach.AttachPtName = strName
            self.m_logger.WriteLine5("\t\t\tThe new AttachPtName is: {0}", oAttach.AttachPtName)
            Assert.assertEqual(strName, oAttach.AttachPtName)

        def action59():
            oAttach.AttachPtName = "InvalidName"

        TryCatchAssertBlock.DoAssert("Allows to set illegal value!", action59)


# endregion


# region VORangeContoursHelper
class VORangeContoursHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "IVORangeContours"):
        self.m_logger.WriteLine("----- THE VO RANGE CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # Visible
        self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oContours.IsVisible)
        oContours.IsVisible = False
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oContours.IsVisible)
        Assert.assertEqual(False, oContours.IsVisible)

        def action60():
            oContours.TranslucentLines = False

        # TranslucentLines
        TryCatchAssertBlock.DoAssert("The Translucent Lines should be readonly when Visible flag is False.", action60)

        def action61():
            oContours.PercentTranslucency = 34.56789

        # PercentTranslucency
        TryCatchAssertBlock.DoAssert("The Translucency should be readonly when Visible flag is False.", action61)

        # LabelSwapDistance
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(oContours.LabelSwapDistance)

        # BorderWall (ReadOnly) test
        oHelper = VOBorderWallHelper(self.m_oUnits)
        oHelper.Run(oContours.BorderWall, True)

        # Visible
        oContours.IsVisible = True
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oContours.IsVisible)
        Assert.assertEqual(True, oContours.IsVisible)
        # TranslucentLines
        self.m_logger.WriteLine4("\t\tThe current TranslucentLines flag is: {0}", oContours.TranslucentLines)
        oContours.TranslucentLines = False
        self.m_logger.WriteLine4("\t\tThe new TranslucentLines flag is: {0}", oContours.TranslucentLines)
        Assert.assertEqual(False, oContours.TranslucentLines)

        def action62():
            oContours.PercentTranslucency = 34.56789

        # PercentTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Translucency should be readonly when Translucent Lines flag is False.", action62
        )
        # TranslucentLines
        oContours.TranslucentLines = True
        self.m_logger.WriteLine4("\t\tThe new TranslucentLines flag is: {0}", oContours.TranslucentLines)
        Assert.assertEqual(True, oContours.TranslucentLines)
        # PercentTranslucency
        self.m_logger.WriteLine6("\t\tThe current Percent Translucency is: {0}", oContours.PercentTranslucency)
        oContours.PercentTranslucency = 34.56789
        self.m_logger.WriteLine6("\t\tThe new Percent Translucency is: {0}", oContours.PercentTranslucency)
        Assert.assertEqual(34.56789, oContours.PercentTranslucency)

        def action63():
            oContours.PercentTranslucency = 1234.56789

        # range test
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action63)

        # BorderWall (NotReadOnly) test
        oHelper.Run(oContours.BorderWall, False)
        self.m_logger.WriteLine("----- THE VO RANGE CONTOURS TEST ----- END -----")


# endregion


# region VOBorderWallHelper
class VOBorderWallHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits

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
            oWall.UseBorderWall = False

        # UseBorderWall
        TryCatchAssertBlock.DoAssert("The Use Border Wall should be readonly.", action64)

        def action65():
            oWall.UpperEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL

        # UpperEdgeAltRef
        TryCatchAssertBlock.DoAssert("The Upper Edge should be readonly.", action65)

        def action66():
            oWall.LowerEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain

        # LowerEdgeAltRef
        TryCatchAssertBlock.DoAssert("The Lower Edge should be readonly.", action66)

        def action67():
            oWall.UpperEdgeHeight = 12.34

        # UpperEdgeHeight
        TryCatchAssertBlock.DoAssert("The Upper Edge Height should be readonly.", action67)

        def action68():
            oWall.LowerEdgeHeight = 34.12

        # LowerEdgeHeight
        TryCatchAssertBlock.DoAssert("The Lower Edge Height should be readonly.", action68)

        def action69():
            oWall.UseWallTranslucency = False

        # UseWallTranslucency
        TryCatchAssertBlock.DoAssert("The Use Wall Translucency should be readonly.", action69)

        def action70():
            oWall.UseLineTranslucency = False

        # UseLineTranslucency
        TryCatchAssertBlock.DoAssert("The Use Line Translucency should be readonly.", action70)

        def action71():
            oWall.WallTranslucency = 34.56

        # WallTranslucency
        TryCatchAssertBlock.DoAssert("The Wall Translucency should be readonly.", action71)

        def action72():
            oWall.LineTranslucency = 56.34

        # LineTranslucency
        TryCatchAssertBlock.DoAssert("The Line Translucency should be readonly.", action72)

    # endregion

    # region NotReadOnly method
    def NotReadOnly(self, oWall: "IVOBorderWall"):
        Assert.assertIsNotNone(oWall)
        self.m_logger.WriteLine("Border Wall (NotReadOnly) test:")
        # UseBorderWall
        self.m_logger.WriteLine4("\tThe current UseBorderWall flag is: {0}", oWall.UseBorderWall)
        oWall.UseBorderWall = False
        self.m_logger.WriteLine4("\tThe new UseBorderWall flag is: {0}", oWall.UseBorderWall)
        Assert.assertEqual(False, oWall.UseBorderWall)

        def action73():
            oWall.UpperEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL

        # UpperEdgeAltRef
        TryCatchAssertBlock.DoAssert("The Upper Edge should be readonly when Use Border Wall flag is False.", action73)

        def action74():
            oWall.LowerEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain

        # LowerEdgeAltRef
        TryCatchAssertBlock.DoAssert("The Lower Edge should be readonly when Use Border Wall flag is False.", action74)

        def action75():
            oWall.UpperEdgeHeight = 12.34

        # UpperEdgeHeight
        TryCatchAssertBlock.DoAssert(
            "The Upper Edge Height should be readonly when Use Border Wall flag is False.", action75
        )

        def action76():
            oWall.LowerEdgeHeight = 34.12

        # LowerEdgeHeight
        TryCatchAssertBlock.DoAssert(
            "The Lower Edge Height should be readonly when Use Border Wall flag is False.", action76
        )

        def action77():
            oWall.UseWallTranslucency = False

        # UseWallTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Use Wall Translucency should be readonly when Use Border Wall flag is False.", action77
        )

        def action78():
            oWall.UseLineTranslucency = False

        # UseLineTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Use Line Translucency should be readonly when Use Border Wall flag is False.", action78
        )

        def action79():
            oWall.WallTranslucency = 34.56

        # WallTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Wall Translucency should be readonly when Use Border Wall flag is False.", action79
        )

        def action80():
            oWall.LineTranslucency = 56.34

        # LineTranslucency
        TryCatchAssertBlock.DoAssert(
            "The Line Translucency should be readonly when Use Border Wall flag is False.", action80
        )
        # UseBorderWall
        oWall.UseBorderWall = True
        self.m_logger.WriteLine4("\tThe new UseBorderWall flag is: {0}", oWall.UseBorderWall)
        Assert.assertEqual(True, oWall.UseBorderWall)
        # set DistanceUnit
        strDistanceUnit = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "mi")
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        Assert.assertEqual("mi", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # IsAltRefTypeSupported
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported eAltRefMSL is: {0}",
            oWall.IsAltRefTypeSupported(AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported eAltRefObject is: {0}",
            oWall.IsAltRefTypeSupported(AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported eAltRefTerrain is: {0}",
            oWall.IsAltRefTypeSupported(AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported eAltRefWGS84 is: {0}",
            oWall.IsAltRefTypeSupported(AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84),
        )

        # UpperEdgeAltRef
        self.m_logger.WriteLine6("\t\tThe current UpperEdge is: {0}", oWall.UpperEdgeAltRef)
        oWall.UpperEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.UpperEdgeAltRef)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL, oWall.UpperEdgeAltRef)
        oWall.UpperEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.UpperEdgeAltRef)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject, oWall.UpperEdgeAltRef)
        oWall.UpperEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.UpperEdgeAltRef)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain, oWall.UpperEdgeAltRef)
        oWall.UpperEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.UpperEdgeAltRef)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84, oWall.UpperEdgeAltRef)
        # UpperEdgeHeight
        self.m_logger.WriteLine6("\t\tThe current UpperEdge Height is: {0}", oWall.UpperEdgeHeight)
        oWall.UpperEdgeHeight = 123.4567
        self.m_logger.WriteLine6("\t\tThe new UpperEdge Height is: {0}", oWall.UpperEdgeHeight)
        Assert.assertEqual(123.4567, oWall.UpperEdgeHeight)

        def action81():
            oWall.UpperEdgeHeight = -9876543210.1

        # UpperEdgeHeight
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action81)
        # LowerEdgeAltRef
        self.m_logger.WriteLine6("\t\tThe current LowerEdge is: {0}", oWall.LowerEdgeAltRef)
        oWall.LowerEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.LowerEdgeAltRef)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefMSL, oWall.LowerEdgeAltRef)
        oWall.LowerEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.LowerEdgeAltRef)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefObject, oWall.LowerEdgeAltRef)
        oWall.LowerEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.LowerEdgeAltRef)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefTerrain, oWall.LowerEdgeAltRef)
        oWall.LowerEdgeAltRef = AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.LowerEdgeAltRef)
        Assert.assertEqual(AgEBorderWallUpperLowerEdgeAltRef.eAltRefWGS84, oWall.LowerEdgeAltRef)
        # LowerEdgeHeight
        self.m_logger.WriteLine6("\t\tThe current LowerEdge Height is: {0}", oWall.LowerEdgeHeight)
        oWall.LowerEdgeHeight = 123.4567
        self.m_logger.WriteLine6("\t\tThe new LowerEdge Height is: {0}", oWall.LowerEdgeHeight)
        Assert.assertEqual(123.4567, oWall.LowerEdgeHeight)

        def action82():
            oWall.LowerEdgeHeight = -9876543210.1

        # LowerEdgeHeight
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action82)
        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit (restored) is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # UseWallTranslucency
        self.m_logger.WriteLine4("\t\tThe current UseWallTranslucency flag is: {0}", oWall.UseWallTranslucency)
        oWall.UseWallTranslucency = False
        self.m_logger.WriteLine4("\t\tThe new UseWallTranslucency flag is: {0}", oWall.UseWallTranslucency)
        Assert.assertEqual(False, oWall.UseWallTranslucency)

        def action83():
            oWall.WallTranslucency = 34.56

        # WallTranslucency
        TryCatchAssertBlock.DoAssert("The Wall Translucency should be readonly.", action83)
        # UseWallTranslucency
        oWall.UseWallTranslucency = True
        self.m_logger.WriteLine4("\t\tThe new UseWallTranslucency flag is: {0}", oWall.UseWallTranslucency)
        Assert.assertEqual(True, oWall.UseWallTranslucency)
        # WallTranslucency
        self.m_logger.WriteLine6("\t\tThe current WallTranslucency is: {0}", oWall.WallTranslucency)
        oWall.WallTranslucency = 34.56
        self.m_logger.WriteLine6("\t\tThe new WallTranslucency is: {0}", oWall.WallTranslucency)
        Assert.assertAlmostEqual(34.56, oWall.WallTranslucency, delta=0.01)

        def action84():
            oWall.WallTranslucency = 1234.56

        # WallTranslucency
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action84)
        # UseLineTranslucency
        self.m_logger.WriteLine4("\t\tThe current UseLineTranslucency flag is: {0}", oWall.UseLineTranslucency)
        oWall.UseLineTranslucency = False
        self.m_logger.WriteLine4("\t\tThe new UseLineTranslucency flag is: {0}", oWall.UseLineTranslucency)
        Assert.assertEqual(False, oWall.UseLineTranslucency)

        def action85():
            oWall.LineTranslucency = 34.56

        # LineTranslucency
        TryCatchAssertBlock.DoAssert("The Line Translucency should be readonly.", action85)
        # UseLineTranslucency
        oWall.UseLineTranslucency = True
        self.m_logger.WriteLine4("\t\tThe new UseLineTranslucency flag is: {0}", oWall.UseLineTranslucency)
        Assert.assertEqual(True, oWall.UseLineTranslucency)
        # LineTranslucency
        self.m_logger.WriteLine6("\t\tThe current LineTranslucency is: {0}", oWall.LineTranslucency)
        oWall.LineTranslucency = 34.56
        self.m_logger.WriteLine6("\t\tThe new LineTranslucency is: {0}", oWall.LineTranslucency)
        Assert.assertAlmostEqual(34.56, oWall.LineTranslucency, delta=0.01)

        def action86():
            oWall.LineTranslucency = 1234.56

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
        self.m_logger.WriteLine4("The current CompassDirectionsVisible flag is: {0}", oMask.CompassDirectionsVisible)
        oMask.CompassDirectionsVisible = False
        self.m_logger.WriteLine4("The new CompassDirectionsVisible flag is: {0}", oMask.CompassDirectionsVisible)
        Assert.assertEqual(False, oMask.CompassDirectionsVisible)
        oMask.CompassDirectionsVisible = True
        self.m_logger.WriteLine4("The new CompassDirectionsVisible flag is: {0}", oMask.CompassDirectionsVisible)
        Assert.assertEqual(True, oMask.CompassDirectionsVisible)
        # AltLabelsVisible
        self.m_logger.WriteLine4("The current AltLabelsVisible flag is: {0}", oMask.AltLabelsVisible)
        oMask.AltLabelsVisible = False
        self.m_logger.WriteLine4("The new AltLabelsVisible flag is: {0}", oMask.AltLabelsVisible)
        Assert.assertEqual(False, oMask.AltLabelsVisible)
        try:
            bCaught = False
            oMask.NumbAltLabels = 12

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The NumbAltLabels should be readonly.")

        oMask.AltLabelsVisible = True
        self.m_logger.WriteLine4("The new AltLabelsVisible flag is: {0}", oMask.AltLabelsVisible)
        Assert.assertEqual(True, oMask.AltLabelsVisible)
        # NumbAltLabels
        self.m_logger.WriteLine3("\tThe current NumbAltLabels flag is: {0}", oMask.NumbAltLabels)
        oMask.NumbAltLabels = 45
        self.m_logger.WriteLine3("\tThe new NumbAltLabels flag is: {0}", oMask.NumbAltLabels)
        Assert.assertEqual(45, oMask.NumbAltLabels)
        try:
            bCaught = False
            oMask.NumbAltLabels = 123

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # InteriorTranslucency
        self.m_logger.WriteLine6("\tThe current InteriorTranslucency flag is: {0}", oMask.InteriorTranslucency)
        oMask.InteriorTranslucency = 98.76
        self.m_logger.WriteLine6("\tThe new InteriorTranslucency flag is: {0}", oMask.InteriorTranslucency)
        Assert.assertAlmostEqual(98.76, oMask.InteriorTranslucency, delta=0.01)
        try:
            bCaught = False
            oMask.InteriorTranslucency = 123

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # LineTranslucency
        self.m_logger.WriteLine6("\tThe current LineTranslucency flag is: {0}", oMask.LineTranslucency)
        oMask.LineTranslucency = 12.34
        self.m_logger.WriteLine6("\tThe new LineTranslucency flag is: {0}", oMask.LineTranslucency)
        Assert.assertAlmostEqual(12.34, oMask.LineTranslucency, delta=0.01)
        try:
            bCaught = False
            oMask.LineTranslucency = 123

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(oMask.LabelSwapDistance)

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
        self.m_logger.WriteLine6("\tThe current DistanceValue is: {0}", oSwapDist.DistanceValue)
        oSwapDist.DistanceValue = 0.56789
        self.m_logger.WriteLine6("\tThe new DistanceValue is: {0}", oSwapDist.DistanceValue)
        Assert.assertEqual(0.56789, oSwapDist.DistanceValue)

        def action87():
            oSwapDist.DistanceValue = -34.56789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action87)
        # DistanceLevel
        self.m_logger.WriteLine6("\tThe current DistanceLevel is: {0}", oSwapDist.DistanceLevel)
        # SetDistanceLevel (eSwapAll)
        oSwapDist.SetDistanceLevel(AgEVOLabelSwapDistance.eSwapAll)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.DistanceLevel)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapAll, oSwapDist.DistanceLevel)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.DistanceValue)
        # SetDistanceLevel (eSwapMarker)
        oSwapDist.SetDistanceLevel(AgEVOLabelSwapDistance.eSwapMarker)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.DistanceLevel)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapMarker, oSwapDist.DistanceLevel)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.DistanceValue)
        # SetDistanceLevel (eSwapMarkerLabel)
        oSwapDist.SetDistanceLevel(AgEVOLabelSwapDistance.eSwapMarkerLabel)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.DistanceLevel)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapMarkerLabel, oSwapDist.DistanceLevel)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.DistanceValue)
        # SetDistanceLevel (eSwapModelLabel)
        oSwapDist.SetDistanceLevel(AgEVOLabelSwapDistance.eSwapModelLabel)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.DistanceLevel)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapModelLabel, oSwapDist.DistanceLevel)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.DistanceValue)
        # SetDistanceLevel (eSwapPoint)
        oSwapDist.SetDistanceLevel(AgEVOLabelSwapDistance.eSwapPoint)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.DistanceLevel)
        Assert.assertEqual(AgEVOLabelSwapDistance.eSwapPoint, oSwapDist.DistanceLevel)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.DistanceValue)

        def action88():
            oSwapDist.SetDistanceLevel(AgEVOLabelSwapDistance.eSwapCustom)

        # SetDistanceLevel (eSwapCustom)
        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action88)

        def action89():
            oSwapDist.SetDistanceLevel(AgEVOLabelSwapDistance.eSwapUnknown)

        # SetDistanceLevel (eSwapUnknown)
        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action89)
        self.m_logger.WriteLine("----- VO LABEL SWAP DISTANCE TEST ----- END -----")


# endregion


# region VOVectorsHelper
class VOVectorsHelper(object):
    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection", root: "IStkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits = oUnits
        self.m_oRoot = root

    # endregion

    # region Run method
    def Run(self, oVector: "IVOVector", bScaleRelativeReadOnly: bool):
        self.m_logger.WriteLine("----- THE VO VECTORS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oVector)
        # ScaleRelativeToModel
        self.m_logger.WriteLine4("The current ScaleRelativeToModel flag is: {0}", oVector.ScaleRelativeToModel)
        if not bScaleRelativeReadOnly:
            oVector.ScaleRelativeToModel = False
            self.m_logger.WriteLine4("The new ScaleRelativeToModel flag is: {0}", oVector.ScaleRelativeToModel)
            Assert.assertEqual(False, oVector.ScaleRelativeToModel)
            oVector.ScaleRelativeToModel = True
            self.m_logger.WriteLine4("The new ScaleRelativeToModel flag is: {0}", oVector.ScaleRelativeToModel)
            Assert.assertEqual(True, oVector.ScaleRelativeToModel)

        else:
            try:
                bCaught = False
                oVector.ScaleRelativeToModel = True

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("Expected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The ScaleRelativeToModel should be readonly.")

        # VectorSizeScale
        self.m_logger.WriteLine6("The current Vector Size Scale is: {0}", oVector.VectorSizeScale)
        oVector.VectorSizeScale = 9.87654321
        self.m_logger.WriteLine6("The new Vector Size Scale is: {0}", oVector.VectorSizeScale)
        Assert.assertEqual(9.87654321, oVector.VectorSizeScale)
        # range test
        try:
            bCaught = False
            oVector.VectorSizeScale = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # AngleSizeScale
        self.m_logger.WriteLine6("The current Angle Size Scale is: {0}", oVector.AngleSizeScale)
        oVector.AngleSizeScale = 3.21987654
        self.m_logger.WriteLine6("The new Angle Size Scale is: {0}", oVector.AngleSizeScale)
        Assert.assertEqual(3.21987654, oVector.AngleSizeScale)
        # range test
        try:
            bCaught = False
            oVector.AngleSizeScale = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # RefCrdns
        self.RefCrdnsCollection(oVector.RefCrdns)

        self.m_logger.WriteLine("----- THE VO VECTORS TEST ----- END -----")

    # endregion

    # region RefCrdnsCollection method
    def RefCrdnsCollection(self, oCollection: "IVOReferenceAnalysisWorkbenchCollection"):
        Assert.assertIsNotNone(oCollection)
        self.m_logger.WriteLine("VORefCrdnCollection test:")

        # Count
        self.m_logger.WriteLine3("The current VectorCollection contains: {0} elements", oCollection.Count)

        iIndex = 0
        while iIndex < oCollection.Count:
            oElement = oCollection[iIndex]
            Assert.assertIsNotNone(oElement)
            self.m_logger.WriteLine8("\tElement {0}: Name = {1}, Type = {2}", iIndex, oElement.Name, oElement.TypeID)

            iIndex += 1

        def action90():
            oElement = oCollection[oCollection.Count]

        TryCatchAssertBlock.DoAssert("Invalid index", action90)

        for voRefCrdn in oCollection:
            name = voRefCrdn.Name

        # RemoveAll
        oCollection.RemoveAll()
        self.m_logger.WriteLine3("After RemoveAll() the Vector Collection contains: {0} elements", oCollection.Count)
        Assert.assertEqual(0, oCollection.Count)

        # AvailableCrdns
        arAvailable = oCollection.AvailableCrdns
        self.m_logger.WriteLine3("The AvailableCrdns array contains {0} elements", len(arAvailable))

        def action91():
            oElement = oCollection.Add(AgEGeometricElemType.eAngleElem, "bogus")

        TryCatchAssertBlock.DoAssert("Invalid object.", action91)

        def action92():
            oElement2 = oCollection.GetCrdnByName(clr.Convert((-1), AgEGeometricElemType), "bogus")

        TryCatchAssertBlock.DoAssert("Invalid AgEGeometricElemType", action92)

        def action93():
            oElement2 = oCollection.GetCrdnByName(AgEGeometricElemType.eAngleElem, "")

        TryCatchAssertBlock.DoAssert("Invalid crdn name", action93)

        iIndex = 0
        while iIndex < len(arAvailable):
            eType = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.eAngleElem:
                oElement = oCollection.Add(eType, str(arAvailable[iIndex][0]))
                Assert.assertIsNotNone(oElement)
                self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", oElement.Name, oElement.TypeID)
                oElement2 = oCollection.GetCrdnByName(eType, str(arAvailable[iIndex][0]))
                Assert.assertEqual(oElement2.Name, oElement.Name)
                break

            iIndex += 1

        iIndex = 0
        while iIndex < len(arAvailable):
            eType = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.eAxesElem:
                oElement = oCollection.Add(eType, str(arAvailable[iIndex][0]))
                Assert.assertIsNotNone(oElement)
                self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", oElement.Name, oElement.TypeID)
                oElement2 = oCollection.GetCrdnByName(eType, str(arAvailable[iIndex][0]))
                Assert.assertEqual(oElement2.Name, oElement.Name)
                break

            iIndex += 1

        iIndex = 0
        while iIndex < len(arAvailable):
            eType = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.ePlaneElem:
                oElement = oCollection.Add(eType, str(arAvailable[iIndex][0]))
                Assert.assertIsNotNone(oElement)
                self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", oElement.Name, oElement.TypeID)
                oElement2 = oCollection.GetCrdnByName(eType, str(arAvailable[iIndex][0]))
                Assert.assertEqual(oElement2.Name, oElement.Name)
                break

            iIndex += 1

        iIndex = 0
        while iIndex < len(arAvailable):
            eType = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.ePointElem:
                oElement = oCollection.Add(eType, str(arAvailable[iIndex][0]))
                Assert.assertIsNotNone(oElement)
                self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", oElement.Name, oElement.TypeID)
                oElement2 = oCollection.GetCrdnByName(eType, str(arAvailable[iIndex][0]))
                Assert.assertEqual(oElement2.Name, oElement.Name)
                break

            iIndex += 1

        # Add Vector element
        bFound = False

        iIndex = 0
        while iIndex < len(arAvailable):
            eType = clr.Convert(int(arAvailable[iIndex][1]), AgEGeometricElemType)
            if eType == AgEGeometricElemType.eVectorElem:
                oVector = clr.Convert(
                    oCollection.Add(eType, str(arAvailable[iIndex][0])), IVOReferenceVectorGeometryToolVector
                )
                Assert.assertIsNotNone(oVector)
                strMagnitudeDim = oVector.MagnitudeDimension
                if (strMagnitudeDim != "Unitless") and (strMagnitudeDim.find("Rate") == -1):
                    self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", oVector.Name, oVector.TypeID)
                    oElement2 = oCollection.GetCrdnByName(eType, str(arAvailable[iIndex][0]))
                    Assert.assertEqual(oElement2.Name, oVector.Name)
                    break

                if not bFound:
                    self.m_logger.WriteLine7("\tAdded element: Name = {0}, Type = {1}", oVector.Name, oVector.TypeID)
                    bFound = True

                else:
                    oCollection.RemoveByName(eType, oVector.Name)

            iIndex += 1

        # Count
        self.m_logger.WriteLine3("The new VectorCollection contains: {0} elements", oCollection.Count)
        for oElement in oCollection:
            self.m_logger.WriteLine7("\tElement: Name = {0}, Type = {1}", oElement.Name, oElement.TypeID)

        iIndex = 0
        while iIndex < oCollection.Count:
            # Item
            oElement = oCollection[iIndex]
            Assert.assertIsNotNone(oElement)
            self.m_logger.WriteLine5("-> {0}", oElement.Name)

            # Visible (false)
            self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oElement.Visible)
            oElement.Visible = False
            self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oElement.Visible)
            Assert.assertEqual(False, oElement.Visible)
            try:
                bCaught = False
                oElement.Color = Color.FromArgb(52)

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The Color should be readonly.")

            try:
                bCaught = False
                oElement.LabelVisible = True

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The LabelVisible should be readonly.")

            if oElement.TypeID == AgEGeometricElemType.eAngleElem:
                self.RefCrdnAngleReadOnly(clr.Convert(oElement, IVOReferenceVectorGeometryToolAngle))
            elif oElement.TypeID == AgEGeometricElemType.eAxesElem:
                self.RefCrdnAxesReadOnly(clr.Convert(oElement, IVOReferenceVectorGeometryToolAxes))
            elif oElement.TypeID == AgEGeometricElemType.ePlaneElem:
                self.RefCrdnPlaneReadOnly(clr.Convert(oElement, IVOReferenceVectorGeometryToolPlane))
            elif oElement.TypeID == AgEGeometricElemType.ePointElem:
                self.RefCrdnPointReadOnly(clr.Convert(oElement, IVOReferenceVectorGeometryToolPoint))
            elif oElement.TypeID == AgEGeometricElemType.eVectorElem:
                self.RefCrdnVectorReadOnly(clr.Convert(oElement, IVOReferenceVectorGeometryToolVector))
            else:
                Assert.fail("Invalid TypeID!")

            # Visible (true)
            oElement.Visible = True
            self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oElement.Visible)
            Assert.assertEqual(True, oElement.Visible)

            # Color
            self.m_logger.WriteLine6("\tThe current Color is: {0}", oElement.Color)
            oElement.Color = Color.FromArgb(9990945)
            self.m_logger.WriteLine6("\tThe new Color is: {0}", oElement.Color)
            AssertEx.AreEqual(Color.FromArgb(9990945), oElement.Color)

            # LabelVisible
            self.m_logger.WriteLine4("\tThe current LabelVisible flag is: {0}", oElement.LabelVisible)
            oElement.LabelVisible = True
            self.m_logger.WriteLine4("\tThe new LabelVisible flag is: {0}", oElement.LabelVisible)
            Assert.assertEqual(True, oElement.LabelVisible)
            if oElement.TypeID == AgEGeometricElemType.eAngleElem:
                self.RefCrdnAngle(clr.Convert(oElement, IVOReferenceVectorGeometryToolAngle))
            elif oElement.TypeID == AgEGeometricElemType.eAxesElem:
                self.RefCrdnAxes(clr.Convert(oElement, IVOReferenceVectorGeometryToolAxes))
            elif oElement.TypeID == AgEGeometricElemType.ePlaneElem:
                self.RefCrdnPlane(clr.Convert(oElement, IVOReferenceVectorGeometryToolPlane))
            elif oElement.TypeID == AgEGeometricElemType.ePointElem:
                # 38619: Earth Center point freezes STK
                self.RefCrdnPoint(clr.Convert(oElement, IVOReferenceVectorGeometryToolPoint))
            elif oElement.TypeID == AgEGeometricElemType.eVectorElem:
                self.RefCrdnVector(clr.Convert(oElement, IVOReferenceVectorGeometryToolVector))
            else:
                Assert.fail("Invalid TypeID!")

            oHelper = DisplayTimesHelper(self.m_oRoot)
            oHelper.Run(clr.Convert(oElement, IDisplayTime))

            iIndex += 1

        # Remove
        self.m_logger.WriteLine3("Before Remove(0) the Vector Collection contains: {0} elements", oCollection.Count)
        oCollection.Remove(0)
        self.m_logger.WriteLine3("After Remove(0) the Vector Collection contains: {0} elements", oCollection.Count)

        def action94():
            oCollection.Remove(oCollection.Count)

        TryCatchAssertBlock.DoAssert("Invalid Remove index", action94)

        # RemoveByName
        self.m_logger.WriteLine3(
            "Before RemoveByName() the Vector Collection contains: {0} elements", oCollection.Count
        )
        oCollection.RemoveByName(oCollection[0].TypeID, oCollection[0].Name)
        self.m_logger.WriteLine3("After RemoveByName() the Vector Collection contains: {0} elements", oCollection.Count)

        def action95():
            oCollection.RemoveByName(clr.Convert((-1), AgEGeometricElemType), "bogus")

        TryCatchAssertBlock.DoAssert("Invalid Remove type", action95)

        def action96():
            oCollection.RemoveByName(AgEGeometricElemType.eAngleElem, "bogus")

        TryCatchAssertBlock.DoAssert("Invalid Remove name", action96)

        # RemoveAll
        self.m_logger.WriteLine3("Before RemoveAll() the Vector Collection contains: {0} elements", oCollection.Count)
        oCollection.RemoveAll()
        self.m_logger.WriteLine3("After RemoveAll() the Vector Collection contains: {0} elements", oCollection.Count)
        Assert.assertEqual(0, oCollection.Count)

    # endregion

    # region RefCrdnAngleReadOnly method
    def RefCrdnAngleReadOnly(self, oAngle: "IVOReferenceVectorGeometryToolAngle"):
        Assert.assertIsNotNone(oAngle)
        self.m_logger.WriteLine("\tRefCrdnAngle test (ReadOnly):")
        try:
            bCaught = False
            oAngle.AngleValueVisible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AngleValueVisible should be readonly.")

        try:
            bCaught = False
            oAngle.AngleUnitAbrv = "rad"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AngleUnitAbrv should be readonly.")

        try:
            bCaught = False
            oAngle.ShowDihedralAngleSupportingArcs = True

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
        self.m_logger.WriteLine4("\t\tThe current AngleValueVisible flag is: {0}", oAngle.AngleValueVisible)
        oAngle.AngleValueVisible = False
        self.m_logger.WriteLine4("\t\tThe new AngleValueVisible flag is: {0}", oAngle.AngleValueVisible)
        Assert.assertEqual(False, oAngle.AngleValueVisible)
        try:
            bCaught = False
            oAngle.AngleUnitAbrv = "mrad"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AngleUnitAbrv should be readonly.")

        oAngle.AngleValueVisible = True
        self.m_logger.WriteLine4("\t\tThe new AngleValueVisible flag is: {0}", oAngle.AngleValueVisible)
        Assert.assertEqual(True, oAngle.AngleValueVisible)
        # AngleUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current AngleUnitAbrv is: {0}", oAngle.AngleUnitAbrv)
        oAngle.AngleUnitAbrv = "mdeg"
        self.m_logger.WriteLine5("\t\tThe new AngleUnitAbrv is: {0}", oAngle.AngleUnitAbrv)
        Assert.assertEqual("mdeg", oAngle.AngleUnitAbrv)
        try:
            bCaught = False
            oAngle.AngleUnitAbrv = "abcdefgh"

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
        try:
            bCaught = False
            oAxes.DrawAtCB = False

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The DrawAtCB should be readonly.")

        try:
            bCaught = False
            oAxes.PersistenceVisible = False

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The PersistenceVisible should be readonly.")

        # set TimeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        try:
            bCaught = False
            oAxes.Duration = 123.456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Duration should be readonly.")

        # restore TimeUnit
        self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        try:
            bCaught = False
            oAxes.Connect = AgEVectorAxesConnectType.eConnectLine

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Connect should be readonly.")

        try:
            bCaught = False
            oAxes.Transparent = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparent should be readonly.")

        try:
            bCaught = False
            oAxes.Axes = "CentralBody/Earth Fixed Axes"

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
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        # DrawAtCB
        self.m_logger.WriteLine4("\t\tThe current DrawAtCB flag is: {0}", oAxes.DrawAtCB)
        oAxes.DrawAtCB = True
        self.m_logger.WriteLine4("\t\tThe new DrawAtCB flag is: {0}", oAxes.DrawAtCB)
        Assert.assertEqual(True, oAxes.DrawAtCB)
        # Axes
        self.m_logger.WriteLine5("\t\tThe current Axes is: {0}", oAxes.Axes)
        # AvailableAxes
        arAxes = oAxes.AvailableAxes
        self.m_logger.WriteLine3("\t\tThe AvailableAxes array contains: {0} elements.", len(arAxes))
        # PersistenceVisible (false)
        self.m_logger.WriteLine4("\t\tThe current PersistenceVisible flag is: {0}", oAxes.PersistenceVisible)
        oAxes.PersistenceVisible = False
        self.m_logger.WriteLine4("\t\tThe new PersistenceVisible flag is: {0}", oAxes.PersistenceVisible)
        Assert.assertEqual(False, oAxes.PersistenceVisible)
        try:
            bCaught = False
            oAxes.Duration = 123.456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Duration should be readonly.")

        try:
            bCaught = False
            oAxes.Connect = AgEVectorAxesConnectType.eConnectLine

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Connect should be readonly.")

        try:
            bCaught = False
            oAxes.Transparent = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparent should be readonly.")

        # PersistenceVisible (true)
        oAxes.PersistenceVisible = True
        self.m_logger.WriteLine4("\t\tThe new PersistenceVisible flag is: {0}", oAxes.PersistenceVisible)
        Assert.assertEqual(True, oAxes.PersistenceVisible)
        # Transparent
        self.m_logger.WriteLine4("\t\tThe current Transparent flag is: {0}", oAxes.Transparent)
        oAxes.Transparent = False
        self.m_logger.WriteLine4("\t\tThe new Transparent flag is: {0}", oAxes.Transparent)
        Assert.assertEqual(False, oAxes.Transparent)
        # Connect
        self.m_logger.WriteLine6("\t\tThe current Connect is: {0}", oAxes.Connect)
        oAxes.Connect = AgEVectorAxesConnectType.eConnectTrace
        self.m_logger.WriteLine6("\t\tThe new Connect is: {0}", oAxes.Connect)
        Assert.assertEqual(AgEVectorAxesConnectType.eConnectTrace, oAxes.Connect)
        # Duration
        self.m_logger.WriteLine6("\t\tThe current Duration is: {0}", oAxes.Duration)
        oAxes.Duration = 12345.6789
        self.m_logger.WriteLine6("\t\tThe new Duration is: {0}", oAxes.Duration)
        Assert.assertAlmostEqual(12345.6789, oAxes.Duration, delta=1e-05)
        # range test
        try:
            bCaught = False
            oAxes.Duration = -1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # restore TimeUnit
        self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

    # endregion

    # region RefCrdnPlaneReadOnly method
    def RefCrdnPlaneReadOnly(self, oPlane: "IVOReferenceVectorGeometryToolPlane"):
        Assert.assertIsNotNone(oPlane)
        self.m_logger.WriteLine("\tRefCrdnPlane test (ReadOnly):")
        try:
            bCaught = False
            oPlane.AxisLabelsVisible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AxisLabelsVisible should be readonly.")

        try:
            bCaught = False
            oPlane.TransparentPlaneVisible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TransparentPlaneVisible should be readonly.")

        try:
            bCaught = False
            oPlane.Transparency = 12

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparency should be readonly.")

        try:
            bCaught = False
            oPlane.DrawAtObject = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The DrawAtObject should be readonly.")

        try:
            bCaught = False
            oPlane.RectGridVisible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RectGridVisible should be readonly.")

        try:
            bCaught = False
            oPlane.CircGridVisible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CircGridVisible should be readonly.")

        # set DistanceUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "ft")
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        Assert.assertEqual("ft", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        try:
            bCaught = False
            oPlane.PlaneGridSpacing = 123.456

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The PlaneGridSpacing should be readonly.")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        try:
            bCaught = False
            oPlane.Size = 123.456

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
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "Re")
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        Assert.assertEqual("Re", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # AxisLabelsVisible
        self.m_logger.WriteLine4("\t\tThe current AxisLabelsVisible flag is: {0}", oPlane.AxisLabelsVisible)
        oPlane.AxisLabelsVisible = False
        self.m_logger.WriteLine4("\t\tThe new AxisLabelsVisible flag is: {0}", oPlane.AxisLabelsVisible)
        Assert.assertEqual(False, oPlane.AxisLabelsVisible)
        oPlane.AxisLabelsVisible = True
        self.m_logger.WriteLine4("\t\tThe new AxisLabelsVisible flag is: {0}", oPlane.AxisLabelsVisible)
        Assert.assertEqual(True, oPlane.AxisLabelsVisible)
        # DrawAtObject
        self.m_logger.WriteLine4("\t\tThe current DrawAtObject flag is: {0}", oPlane.DrawAtObject)
        oPlane.DrawAtObject = False
        self.m_logger.WriteLine4("\t\tThe new DrawAtObject flag is: {0}", oPlane.DrawAtObject)
        Assert.assertEqual(False, oPlane.DrawAtObject)
        oPlane.DrawAtObject = True
        self.m_logger.WriteLine4("\t\tThe new DrawAtObject flag is: {0}", oPlane.DrawAtObject)
        Assert.assertEqual(True, oPlane.DrawAtObject)
        # Size
        self.m_logger.WriteLine6("\t\tThe current Size is: {0}", oPlane.Size)
        oPlane.Size = 3.21
        self.m_logger.WriteLine6("\t\tThe new Size is: {0}", oPlane.Size)
        Assert.assertEqual(3.21, oPlane.Size)
        # range test
        try:
            bCaught = False
            oPlane.Size = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # TransparentPlaneVisible
        self.m_logger.WriteLine4("\t\tThe current TransparentPlaneVisible flag is: {0}", oPlane.TransparentPlaneVisible)
        oPlane.TransparentPlaneVisible = False
        self.m_logger.WriteLine4("\t\tThe new TransparentPlaneVisible flag is: {0}", oPlane.TransparentPlaneVisible)
        Assert.assertEqual(False, oPlane.TransparentPlaneVisible)
        try:
            bCaught = False
            oPlane.Transparency = 23.45

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparency should be readonly.")

        oPlane.TransparentPlaneVisible = True
        self.m_logger.WriteLine4("\t\tThe new TransparentPlaneVisible flag is: {0}", oPlane.TransparentPlaneVisible)
        Assert.assertEqual(True, oPlane.TransparentPlaneVisible)
        # Transparency
        self.m_logger.WriteLine6("\t\tThe current Transparency is: {0}", oPlane.Transparency)
        oPlane.Transparency = 12.34
        self.m_logger.WriteLine6("\t\tThe new Transparency is: {0}", oPlane.Transparency)
        Assert.assertAlmostEqual(12.34, oPlane.Transparency, delta=0.001)
        # range test
        try:
            bCaught = False
            oPlane.Transparency = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # RectGridVisible (false)
        self.m_logger.WriteLine4("\t\tThe current RectGridVisible flag is: {0}", oPlane.RectGridVisible)
        oPlane.RectGridVisible = False
        self.m_logger.WriteLine4("\t\tThe new RectGridVisible flag is: {0}", oPlane.RectGridVisible)
        Assert.assertEqual(False, oPlane.RectGridVisible)
        # CircGridVisible (false)
        self.m_logger.WriteLine4("\t\tThe current CircGridVisible flag is: {0}", oPlane.CircGridVisible)
        oPlane.CircGridVisible = False
        self.m_logger.WriteLine4("\t\tThe new CircGridVisible flag is: {0}", oPlane.CircGridVisible)
        Assert.assertEqual(False, oPlane.CircGridVisible)
        try:
            bCaught = False
            oPlane.PlaneGridSpacing = 123.45

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The PlaneGridSpacing should be readonly.")

        # RectGridVisible (true)
        oPlane.RectGridVisible = True
        self.m_logger.WriteLine4("\t\tThe new RectGridVisible flag is: {0}", oPlane.RectGridVisible)
        Assert.assertEqual(True, oPlane.RectGridVisible)
        # PlaneGridSpacing
        self.m_logger.WriteLine6("\t\tThe current PlaneGridSpacing is: {0}", oPlane.PlaneGridSpacing)
        oPlane.PlaneGridSpacing = 987.654
        self.m_logger.WriteLine6("\t\tThe new PlaneGridSpacing is: {0}", oPlane.PlaneGridSpacing)
        Assert.assertAlmostEqual(987.654, oPlane.PlaneGridSpacing, delta=0.0001)
        # CircGridVisible (true)
        oPlane.CircGridVisible = True
        self.m_logger.WriteLine4("\t\tThe new CircGridVisible flag is: {0}", oPlane.CircGridVisible)
        Assert.assertEqual(True, oPlane.CircGridVisible)
        # range test
        try:
            bCaught = False
            oPlane.PlaneGridSpacing = -1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

    # endregion

    # region RefCrdnPointReadOnly method
    def RefCrdnPointReadOnly(self, oPoint: "IVOReferenceVectorGeometryToolPoint"):
        Assert.assertIsNotNone(oPoint)
        self.m_logger.WriteLine("\tRefCrdnPoint test (ReadOnly):")
        try:
            bCaught = False
            oPoint.TrajectoryType = AgETrajectoryType.eTrajTrace

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TrajectoryType should be readonly.")

        try:
            bCaught = False
            oPoint.RADecVisible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecVisible should be readonly.")

        try:
            bCaught = False
            oPoint.RADecUnitAbrv = "arcMin"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecUnitAbrv should be readonly.")

        try:
            bCaught = False
            oPoint.CartesianVisible = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CartesianVisible should be readonly.")

        try:
            bCaught = False
            oPoint.CartesianUnitAbrv = "Au"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CartesianUnitAbrv should be readonly.")

        try:
            bCaught = False
            oPoint.System = "CentralBody/Sun PseudoFixed System"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The System should be readonly.")

        try:
            bCaught = False
            oPoint.Size = 5

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
        self.m_logger.WriteLine6("\t\tThe current TrajectoryType is: {0}", oPoint.TrajectoryType)
        oPoint.TrajectoryType = AgETrajectoryType.eTrajLine
        self.m_logger.WriteLine6("\t\tThe new TrajectoryType flag is: {0}", oPoint.TrajectoryType)
        Assert.assertEqual(AgETrajectoryType.eTrajLine, oPoint.TrajectoryType)
        # Size
        self.m_logger.WriteLine6("\t\tThe current Size is: {0}", oPoint.Size)
        oPoint.Size = 3.21
        self.m_logger.WriteLine6("\t\tThe new Size is: {0}", oPoint.Size)
        Assert.assertAlmostEqual(3.21, oPoint.Size, delta=0.001)
        # range test
        try:
            bCaught = False
            oPoint.Size = 1234.56789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # System
        self.m_logger.WriteLine5("\t\tThe current System is: {0}", oPoint.System)
        #
        arSystems = oPoint.AvailableSystems
        self.m_logger.WriteLine3("\t\tThe AvailableSystems array contains: {0} elements.", Array.Length(arSystems))
        # range test
        try:
            bCaught = False
            oPoint.System = "Abcdefgh"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal System!")

        # RADecVisible
        self.m_logger.WriteLine4("\t\tThe current RADecVisible flag is: {0}", oPoint.RADecVisible)
        oPoint.RADecVisible = False
        self.m_logger.WriteLine4("\t\tThe new RADecVisible flag is: {0}", oPoint.RADecVisible)
        Assert.assertEqual(False, oPoint.RADecVisible)
        try:
            bCaught = False
            oPoint.RADecUnitAbrv = "deg"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecUnitAbrv should be readonly.")

        oPoint.RADecVisible = True
        self.m_logger.WriteLine4("\t\tThe new RADecVisible flag is: {0}", oPoint.RADecVisible)
        Assert.assertEqual(True, oPoint.RADecVisible)
        # RADecUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current RADecUnitAbrv is: {0}", oPoint.RADecUnitAbrv)
        oPoint.RADecUnitAbrv = "mrad"
        self.m_logger.WriteLine5("\t\tThe new RADecUnitAbrv is: {0}", oPoint.RADecUnitAbrv)
        Assert.assertEqual("mrad", oPoint.RADecUnitAbrv)
        try:
            bCaught = False
            oPoint.RADecUnitAbrv = "Abc"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal RADecUnitAbrv!")

        # MagnitudeVisible
        self.m_logger.WriteLine4("\t\tThe current MagnitudeVisible flag is: {0}", oPoint.MagnitudeVisible)
        oPoint.MagnitudeVisible = False
        self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oPoint.MagnitudeVisible)
        Assert.assertEqual(False, oPoint.MagnitudeVisible)
        try:
            bCaught = False
            oPoint.MagnitudeUnitAbrv = "fur"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The MagnitudeUnitAbrv should be readonly.")

        oPoint.MagnitudeVisible = True
        self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oPoint.MagnitudeVisible)
        Assert.assertEqual(True, oPoint.MagnitudeVisible)
        # MagnitudeUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current MagnitudeUnitAbrv is: {0}", oPoint.MagnitudeUnitAbrv)
        oPoint.MagnitudeUnitAbrv = "fur"
        self.m_logger.WriteLine5("\t\tThe new MagnitudeUnitAbrv is: {0}", oPoint.MagnitudeUnitAbrv)
        Assert.assertEqual("fur", oPoint.MagnitudeUnitAbrv)
        try:
            bCaught = False
            oPoint.MagnitudeUnitAbrv = "Abc"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal MagnitudeUnitAbrv!")

        # CartesianVisible
        self.m_logger.WriteLine4("\t\tThe current CartesianVisible flag is: {0}", oPoint.CartesianVisible)
        oPoint.CartesianVisible = False
        self.m_logger.WriteLine4("\t\tThe new CartesianVisible flag is: {0}", oPoint.CartesianVisible)
        Assert.assertEqual(False, oPoint.CartesianVisible)
        try:
            bCaught = False
            oPoint.CartesianUnitAbrv = "kft"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CartesianUnitAbrv should be readonly.")

        oPoint.CartesianVisible = True
        self.m_logger.WriteLine4("\t\tThe new CartesianVisible flag is: {0}", oPoint.CartesianVisible)
        Assert.assertEqual(True, oPoint.CartesianVisible)
        # CartesianUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current CartesianUnitAbrv is: {0}", oPoint.CartesianUnitAbrv)
        oPoint.CartesianUnitAbrv = "kft"
        self.m_logger.WriteLine5("\t\tThe new CartesianUnitAbrv is: {0}", oPoint.CartesianUnitAbrv)
        Assert.assertEqual("kft", oPoint.CartesianUnitAbrv)
        try:
            bCaught = False
            oPoint.CartesianUnitAbrv = "Abc"

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
            oVector.DrawAtCB = True

        # DrawAtCB
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action97)

        def action98():
            oVector.RADecVisible = True

        # RADecVisible
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action98)

        def action99():
            oVector.RADecUnitAbrv = "semiC"

        # RADecUnitAbrv
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action99)

        def action100():
            oVector.MagnitudeVisible = True

        # MagnitudeVisible
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action100)

        def action101():
            oVector.PersistenceVisible = True

        # PersistenceVisible
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action101)
        # set TimeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

        def action102():
            oVector.Duration = 123.456

        # Duration
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action102)
        # restore TimeUnit
        self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

        def action103():
            oVector.Connect = AgEVectorAxesConnectType.eConnectLine

        # Connect
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action103)

        def action104():
            oVector.Transparent = True

        # Transparent
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action104)

        def action105():
            oVector.Axes = "CentralBody/Earth Fixed Axes"

        # Axes
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action105)

        def action106():
            oVector.DrawAtPoint = True

        # DrawAtPoint
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action106)

        def action107():
            oVector.Point = "Satellite/Satellite1 Center Point"

        # Point
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action107)

        def action108():
            oVector.TrueScale = True

        # TrueScale
        TryCatchAssertBlock.DoAssert("The property should be readonly.", action108)

    # endregion

    # region RefCrdnVector method
    def RefCrdnVector(self, oVector: "IVOReferenceVectorGeometryToolVector"):
        Assert.assertIsNotNone(oVector)
        self.m_logger.WriteLine("\tRefCrdnVector test:")
        # DrawAtCB
        self.m_logger.WriteLine4("\t\tThe current DrawAtCB flag is: {0}", oVector.DrawAtCB)
        oVector.DrawAtCB = False
        self.m_logger.WriteLine4("\t\tThe new DrawAtCB flag is: {0}", oVector.DrawAtCB)
        Assert.assertEqual(False, oVector.DrawAtCB)
        oVector.DrawAtCB = True
        self.m_logger.WriteLine4("\t\tThe new DrawAtCB flag is: {0}", oVector.DrawAtCB)
        Assert.assertEqual(True, oVector.DrawAtCB)
        # TrueScale
        self.m_logger.WriteLine4("\t\tThe current TrueScale flag is: {0}", oVector.TrueScale)
        if oVector.MagnitudeDimension == "DistanceUnit":
            oVector.TrueScale = False
            self.m_logger.WriteLine4("\t\tThe new TrueScale flag is: {0}", oVector.TrueScale)
            Assert.assertEqual(False, oVector.TrueScale)
            oVector.TrueScale = True
            self.m_logger.WriteLine4("\t\tThe new TrueScale flag is: {0}", oVector.TrueScale)
            Assert.assertEqual(True, oVector.TrueScale)

        else:

            def action109():
                oVector.TrueScale = False

            TryCatchAssertBlock.DoAssert("This property should be readonly", action109)

        # AvailableAxes
        arAxes = oVector.AvailableAxes
        self.m_logger.WriteLine3("\t\tThe Vector has {0} available Axes", Array.Length(arAxes))
        # Axes
        self.m_logger.WriteLine5("\t\tThe current Axes is: {0}", oVector.Axes)
        if Array.Length(arAxes) > 0:
            oVector.Axes = str(arAxes[0])
            self.m_logger.WriteLine5("\t\tThe new Axes is: {0}", oVector.Axes)
            Assert.assertEqual(arAxes[0], oVector.Axes)

        else:
            self.m_logger.WriteLine("\t\tNo available Axes")

        def action110():
            oVector.Axes = "Abcdefgh"

        TryCatchAssertBlock.DoAssert("Cannot set illegal Axes!", action110)
        # DrawAtPoint
        self.m_logger.WriteLine4("\t\tThe current DrawAtPoint flag is: {0}", oVector.DrawAtPoint)
        oVector.DrawAtPoint = False
        self.m_logger.WriteLine4("\t\tThe new DrawAtPoint flag is: {0}", oVector.DrawAtPoint)
        Assert.assertEqual(False, oVector.DrawAtPoint)

        def action111():
            oVector.Point = "Satellite/Satellite1 Center Point"

        TryCatchAssertBlock.DoAssert("The Point should be readonly.", action111)
        oVector.DrawAtPoint = True
        self.m_logger.WriteLine4("\t\tThe new DrawAtPoint flag is: {0}", oVector.DrawAtPoint)
        Assert.assertEqual(True, oVector.DrawAtPoint)
        # AvailablePoints
        arPoints = oVector.AvailablePoints
        self.m_logger.WriteLine3("\t\tThe Vector has {0} available Points", Array.Length(arPoints))
        # Point
        self.m_logger.WriteLine5("\t\tThe current Point is: {0}", oVector.Point)
        if Array.Length(arPoints) > 0:
            oVector.Point = str(arPoints[0])
            self.m_logger.WriteLine5("\t\tThe new Point is: {0}", oVector.Point)
            Assert.assertEqual(arPoints[0], oVector.Point)

        else:
            self.m_logger.WriteLine("\t\tNo available Points")

        def action112():
            oVector.Point = "Abcdefgh"

        TryCatchAssertBlock.DoAssert("Cannot set illegal Point!", action112)
        # RADecVisible
        self.m_logger.WriteLine4("\t\tThe current RADecVisible flag is: {0}", oVector.RADecVisible)
        oVector.RADecVisible = False
        self.m_logger.WriteLine4("\t\tThe new RADecVisible flag is: {0}", oVector.RADecVisible)
        Assert.assertEqual(False, oVector.RADecVisible)

        def action113():
            oVector.RADecUnitAbrv = "mdeg"

        TryCatchAssertBlock.DoAssert("The RADecUnitAbrv should be readonly.", action113)
        oVector.RADecVisible = True
        self.m_logger.WriteLine4("\t\tThe new RADecVisible flag is: {0}", oVector.RADecVisible)
        Assert.assertEqual(True, oVector.RADecVisible)
        # RADecUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current RADecUnitAbrv is: {0}", oVector.RADecUnitAbrv)
        oVector.RADecUnitAbrv = "rad"
        self.m_logger.WriteLine5("\t\tThe new RADecUnitAbrv is: {0}", oVector.RADecUnitAbrv)
        Assert.assertEqual("rad", oVector.RADecUnitAbrv)

        def action114():
            oVector.RADecUnitAbrv = "Abc"

        TryCatchAssertBlock.DoAssert("Cannot set illegal RADecUnitAbrv!", action114)
        # MagnitudeDimension
        strMagnitudeDim = oVector.MagnitudeDimension
        self.m_logger.WriteLine5("\t\tThe MagnitudeDimension is: {0}", strMagnitudeDim)
        if (strMagnitudeDim != "Unitless") and (strMagnitudeDim.find("Rate") == -1):
            strCurrentDimensionAbrv = self.m_oUnits.GetCurrentUnitAbbrv(strMagnitudeDim)
            self.m_logger.WriteLine5("\t\tThe current DimensionAbbreviature is: {0}", strCurrentDimensionAbrv)
            # MagnitudeVisible
            self.m_logger.WriteLine4("\t\tThe current MagnitudeVisible flag is: {0}", oVector.MagnitudeVisible)
            oVector.MagnitudeVisible = False
            self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oVector.MagnitudeVisible)
            Assert.assertEqual(False, oVector.MagnitudeVisible)

            def action115():
                oVector.MagnitudeUnitAbrv = strCurrentDimensionAbrv

            TryCatchAssertBlock.DoAssert("The MagnitudeUnitAbrv should be readonly.", action115)
            oVector.MagnitudeVisible = True
            self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oVector.MagnitudeVisible)
            Assert.assertEqual(True, oVector.MagnitudeVisible)
            # MagnitudeUnitAbrv
            self.m_logger.WriteLine5("\t\tThe current MagnitudeUnitAbrv is: {0}", oVector.MagnitudeUnitAbrv)
            try:
                oVector.MagnitudeUnitAbrv = strCurrentDimensionAbrv
                self.m_logger.WriteLine5("\t\tThe new MagnitudeUnitAbrv is: {0}", oVector.MagnitudeUnitAbrv)

            except Exception as e:
                self.m_logger.WriteLine5("\t\tThe MagnitudeUnitAbrv is readonly in: {0}", oVector.Name)
                self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

            def action116():
                oVector.MagnitudeUnitAbrv = "Abc"

            TryCatchAssertBlock.DoAssert("Cannot set illegal MagnitudeUnitAbrv!", action116)

        # set TimeUnit
        strUnit = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        # PersistenceVisible (false)
        self.m_logger.WriteLine4("\t\tThe current PersistenceVisible flag is: {0}", oVector.PersistenceVisible)
        oVector.PersistenceVisible = False
        self.m_logger.WriteLine4("\t\tThe new PersistenceVisible flag is: {0}", oVector.PersistenceVisible)
        Assert.assertEqual(False, oVector.PersistenceVisible)

        def action117():
            oVector.Duration = 123.456

        TryCatchAssertBlock.DoAssert("The Duration should be readonly.", action117)

        def action118():
            oVector.Connect = AgEVectorAxesConnectType.eConnectLine

        TryCatchAssertBlock.DoAssert("The Connect should be readonly.", action118)

        def action119():
            oVector.Transparent = True

        TryCatchAssertBlock.DoAssert("The Transparent should be readonly.", action119)
        # PersistenceVisible (true)
        oVector.PersistenceVisible = True
        self.m_logger.WriteLine4("\t\tThe new PersistenceVisible flag is: {0}", oVector.PersistenceVisible)
        Assert.assertEqual(True, oVector.PersistenceVisible)
        # Transparent
        self.m_logger.WriteLine4("\t\tThe current Transparent flag is: {0}", oVector.Transparent)
        oVector.Transparent = False
        self.m_logger.WriteLine4("\t\tThe new Transparent flag is: {0}", oVector.Transparent)
        Assert.assertEqual(False, oVector.Transparent)
        # Connect
        self.m_logger.WriteLine6("\t\tThe current Connect is: {0}", oVector.Connect)
        oVector.Connect = AgEVectorAxesConnectType.eConnectTrace
        self.m_logger.WriteLine6("\t\tThe new Connect is: {0}", oVector.Connect)
        Assert.assertEqual(AgEVectorAxesConnectType.eConnectTrace, oVector.Connect)
        # Duration
        self.m_logger.WriteLine6("\t\tThe current Duration is: {0}", oVector.Duration)
        oVector.Duration = 12345.6789
        self.m_logger.WriteLine6("\t\tThe new Duration is: {0}", oVector.Duration)
        Assert.assertAlmostEqual(12345.6789, oVector.Duration, delta=1e-05)

        def action120():
            oVector.Duration = -1234.56789

        # range test
        TryCatchAssertBlock.DoAssert("Cannot set value out of range!", action120)
        # restore TimeUnit
        self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))


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
        self.m_logger.WriteLine4("\tThe current Visible is: {0}", oVaporTrail.Visible)
        oVaporTrail.Visible = False
        self.m_logger.WriteLine4("\tThe new Visible is: {0}", oVaporTrail.Visible)
        Assert.assertFalse(oVaporTrail.Visible)

        def action121():
            oVaporTrail.MaxNumOfPuffs = 34

        # MaxNumOfPuffs (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action121)

        def action122():
            oVaporTrail.Density = 3.4

        # Density (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action122)

        def action123():
            oVaporTrail.Radius = 34.56

        # Radius (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action123)

        def action124():
            oVaporTrail.Color = Color.FromArgb(1218646)

        # Color (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action124)

        def action125():
            oVaporTrail.ImageFile = strDataPath + r"\STKData\VO/Textures/smoke.pgm"

        # ImageFile (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action125)

        def action126():
            oVaporTrail.UseAttachPoint = False

        # UseAttachPoint (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action126)

        def action127():
            oVaporTrail.AttachPointName = "InvalidPointName"

        # AttachPointName (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action127)
        # Visible (true)
        oVaporTrail.Visible = True
        self.m_logger.WriteLine4("\tThe new Visible is: {0}", oVaporTrail.Visible)
        Assert.assertTrue(oVaporTrail.Visible)
        # MaxNumOfPuffs
        self.m_logger.WriteLine3("\tThe current MaxNumOfPuffs is: {0}", oVaporTrail.MaxNumOfPuffs)
        oVaporTrail.MaxNumOfPuffs = 34
        self.m_logger.WriteLine3("\tThe new MaxNumOfPuffs is: {0}", oVaporTrail.MaxNumOfPuffs)
        Assert.assertEqual(34, oVaporTrail.MaxNumOfPuffs)

        def action128():
            oVaporTrail.MaxNumOfPuffs = 12345

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action128)
        # Density
        self.m_logger.WriteLine6("\tThe current Density is: {0}", oVaporTrail.Density)
        oVaporTrail.Density = 123.456
        self.m_logger.WriteLine6("\tThe new Density is: {0}", oVaporTrail.Density)
        Assert.assertAlmostEqual(123.456, oVaporTrail.Density, delta=0.0001)

        def action129():
            oVaporTrail.Density = 12345.6789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action129)
        # Radius
        self.m_logger.WriteLine6("\tThe current Radius is: {0}", oVaporTrail.Radius)
        oVaporTrail.Radius = 1234.56
        self.m_logger.WriteLine6("\tThe new Radius is: {0}", oVaporTrail.Radius)
        Assert.assertAlmostEqual(1234.56, oVaporTrail.Radius, delta=0.001)

        def action130():
            oVaporTrail.Radius = -12345.6789

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action130)
        # StartTime / EndTime
        self.m_logger.WriteLine6("\tThe current StartTime is: {0}", oVaporTrail.DisplayInterval.GetStartEpoch())
        self.m_logger.WriteLine6("\tThe current EndTime is: {0}", oVaporTrail.DisplayInterval.GetStopEpoch())
        oVaporTrail.DisplayInterval.SetStartAndStopTimes("11 Jul 1999 05:00:00.000", "13 Jul 1999 15:00:00.000")
        self.m_logger.WriteLine6("\tThe new StartTime is: {0}", oVaporTrail.DisplayInterval.GetStartEpoch())
        Assert.assertEqual("11 Jul 1999 05:00:00.000", oVaporTrail.DisplayInterval.GetStartEpoch().TimeInstant)
        self.m_logger.WriteLine6("\tThe new EndTime is: {0}", oVaporTrail.DisplayInterval.GetStopEpoch())
        Assert.assertEqual("13 Jul 1999 15:00:00.000", oVaporTrail.DisplayInterval.GetStopEpoch().TimeInstant)
        # Color
        self.m_logger.WriteLine6("\tThe current Color is: {0}", oVaporTrail.Color)
        oVaporTrail.Color = Color.FromArgb(4660)
        self.m_logger.WriteLine6("\tThe new Color is: {0}", oVaporTrail.Color)
        AssertEx.AreEqual(Color.FromArgb(4660), oVaporTrail.Color)
        # ImageFile
        self.m_logger.WriteLine5("\tThe current ImageFile is: {0}", oVaporTrail.ImageFile)
        oVaporTrail.ImageFile = strDataPath + r"\STKData\VO\Textures\smoke.pgm"
        self.m_logger.WriteLine5("\tThe new ImageFile is: {0}", oVaporTrail.ImageFile)
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Textures", "smoke.pgm"), oVaporTrail.ImageFile)

        def action131():
            oVaporTrail.ImageFile = "InvalidImageFile.Name"

        TryCatchAssertBlock.DoAssert("Should not allow to set an illegal value.", action131)

        # AvailableAttachPoints
        file: IVOModelFile = clr.CastAs(oModel.ModelData, IVOModelFile)
        arAvailablePoints = oVaporTrail.AvailableAttachPoints
        self.m_logger.WriteLine3(
            "\tThe current model contains: {0} available attach points.", Array.Length(arAvailablePoints)
        )
        if file.Filename.endswith("launchvehicle.dae") or file.Filename.endswith("missile.mdl"):
            Assert.assertEqual(3, Array.Length(arAvailablePoints))

        else:
            Assert.assertEqual(0, Array.Length(arAvailablePoints))

            def action132():
                oVaporTrail.UseAttachPoint = False

            TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action132)

        def action133():
            oVaporTrail.AttachPointName = "InvalidPointName"

        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action133)

        # Load a VOModel with attached points
        oModel.Visible = True
        Assert.assertTrue(oModel.Visible)
        oModel.ModelType = AgEModelType.eModelFile
        Assert.assertEqual(AgEModelType.eModelFile, oModel.ModelType)
        oModelFile = clr.Convert(oModel.ModelData, IVOModelFile)
        Assert.assertIsNotNone(oModelFile)
        self.m_logger.WriteLine5("\tThe current VOModel file is: {0}", oModelFile.Filename)
        oModelFile.Filename = strDataPath + r"\STKData\VO\Models\Space\pegasus.mdl"
        self.m_logger.WriteLine5("\tThe new VOModel file is: {0}", oModelFile.Filename)
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Models", "Space", "pegasus.mdl"), oModelFile.Filename)
        arAvailablePoints = oVaporTrail.AvailableAttachPoints
        self.m_logger.WriteLine3(
            "\tThe current model contains: {0} available attach points.", Array.Length(arAvailablePoints)
        )
        Assert.assertEqual(3, Array.Length(arAvailablePoints))
        # UseAttachPoint (false)
        self.m_logger.WriteLine4("\tThe current UseAttachPoint is: {0}", oVaporTrail.UseAttachPoint)
        oVaporTrail.UseAttachPoint = False
        self.m_logger.WriteLine4("\tThe new UseAttachPoint is: {0}", oVaporTrail.UseAttachPoint)
        Assert.assertFalse(oVaporTrail.UseAttachPoint)

        def action134():
            oVaporTrail.AttachPointName = "InvalidPointName"

        # AttachPointName (read only)
        TryCatchAssertBlock.DoAssert("Should not allow to change a readonly value.", action134)
        # UseAttachPoint (true)
        oVaporTrail.UseAttachPoint = True
        self.m_logger.WriteLine4("\tThe new UseAttachPoint is: {0}", oVaporTrail.UseAttachPoint)
        Assert.assertTrue(oVaporTrail.UseAttachPoint)
        # AttachPointName
        self.m_logger.WriteLine5("\tThe current AttachPointName is: {0}", oVaporTrail.AttachPointName)

        iIndex = 0
        while iIndex < Array.Length(arAvailablePoints):
            oVaporTrail.AttachPointName = str(arAvailablePoints[iIndex])
            self.m_logger.WriteLine5("\tThe new AttachPointName is: {0}", oVaporTrail.AttachPointName)
            Assert.assertEqual(str(arAvailablePoints[iIndex]), oVaporTrail.AttachPointName)

            iIndex += 1

        def action135():
            oVaporTrail.AttachPointName = "InvalidPointName"

        TryCatchAssertBlock.DoAssert("Should not allow to set an invalid value.", action135)
        self.m_logger.WriteLine("----- VO VAPOR TRAIL TEST ----- END -----")

    # endregion
