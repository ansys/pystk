import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


# region VOSigmaScaleProbabilityHelper
class VOSigmaScaleProbabilityHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oProbability: "VehicleGraphics3DSigmaScaleProbability"):
        Assert.assertIsNotNone(oProbability)
        self.m_logger.WriteLine6("\tThe current Probability value is: {0}", oProbability.probability)
        oProbability.probability = 34.567
        self.m_logger.WriteLine6("\tThe new Probability value is: {0}", oProbability.probability)
        Assert.assertEqual(34.567, oProbability.probability)
        bCaught: bool = False
        try:
            bCaught = False
            oProbability.probability = -1.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Probability should not allow to set negative value.")

        try:
            bCaught = False
            oProbability.probability = 120.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Probability should not allow to set a value more then 99.999")


# endregion


# region VOSigmaScaleScaleHelper
class VOSigmaScaleScaleHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oScale: "VehicleGraphics3DSigmaScaleScale"):
        Assert.assertIsNotNone(oScale)
        self.m_logger.WriteLine6("\tThe current Scale value is: {0}", oScale.scale_value)
        oScale.scale_value = 3.456
        self.m_logger.WriteLine6("\tThe new Scale value is: {0}", oScale.scale_value)
        Assert.assertEqual(3.456, oScale.scale_value)
        bCaught: bool = False
        try:
            bCaught = False
            oScale.scale_value = -1.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Scale should not allow to set negative value.")

        try:
            bCaught = False
            oScale.scale_value = 12.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Scale should not allow to set a value more then 5.1")


# endregion


# region VOAttributesBasicHelper
class VOAttributesBasicHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oBasic: "VehicleGraphics3DAttributesBasic"):
        Assert.assertIsNotNone(oBasic)
        self.m_logger.WriteLine4("\tCurrent Visible flag is: {0}", oBasic.show_graphics)
        oBasic.show_graphics = False
        self.m_logger.WriteLine4("\tNew Visible flag is: {0}", oBasic.show_graphics)
        Assert.assertEqual(False, oBasic.show_graphics)
        bCaught: bool = False
        try:
            bCaught = False
            oBasic.color = Colors.from_argb(16711935)

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Color should be readonly when Visible flag is False.")

        try:
            bCaught = False
            oBasic.line_width = LINE_WIDTH.WIDTH5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The LineWidth should be readonly when Visible flag is False.")

        oBasic.show_graphics = True
        self.m_logger.WriteLine4("\tNew Visible flag is: {0}", oBasic.show_graphics)
        Assert.assertEqual(True, oBasic.show_graphics)

        # Color
        useCustomColor: bool = oBasic.use_custom_color
        self.m_logger.WriteLine4("\tCurrent UseCustomColor is: {0}", oBasic.use_custom_color)
        oBasic.use_custom_color = not oBasic.use_custom_color
        self.m_logger.WriteLine4("\tNew UseCustomColor is: {0}", oBasic.use_custom_color)
        Assert.assertEqual(oBasic.use_custom_color, (not useCustomColor))
        oBasic.use_custom_color = True
        self.m_logger.WriteLine6("\tCurrent Color is: {0}", oBasic.color)
        oBasic.color = Colors.from_argb(16711935)
        self.m_logger.WriteLine6("\tNew Color is: {0}", oBasic.color)
        AssertEx.AreEqual(Colors.from_argb(16711935), oBasic.color)

        # LineWidth
        self.m_logger.WriteLine6("\tCurrent LineWidth is: {0}", oBasic.line_width)
        oBasic.line_width = LINE_WIDTH.WIDTH5
        self.m_logger.WriteLine6("\tNew LineWidth is: {0}", oBasic.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH5, oBasic.line_width)
        with pytest.raises(Exception):
            oBasic.line_width = -1
        with pytest.raises(Exception):
            oBasic.line_width = 11

        oBasic.translucency = 50
        Assert.assertEqual(50, oBasic.translucency)


# endregion


# region VOAttributesIntervalsHelper
class VOAttributesIntervalsHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oIntervals: "VehicleGraphics3DAttributesIntervals"):
        Assert.assertIsNotNone(oIntervals)
        # Default
        oDefault: "VehicleGraphics3DDefaultAttributes" = oIntervals.default_attributes
        Assert.assertIsNotNone(oDefault)
        # IsVisible
        self.m_logger.WriteLine4("\tCurrent Visible flag is: {0}", oDefault.show_graphics)
        oDefault.show_graphics = False
        self.m_logger.WriteLine4("\tNew Visible flag is: {0}", oDefault.show_graphics)
        Assert.assertEqual(False, oDefault.show_graphics)
        # Color
        self.m_logger.WriteLine6("\tCurrent Color is: {0}", oDefault.color)
        oDefault.color = Colors.from_argb(65535)
        self.m_logger.WriteLine6("\tNew Color is: {0}", oDefault.color)
        AssertEx.AreEqual(Colors.from_argb(65535), oDefault.color)
        # LineWidth
        self.m_logger.WriteLine6("\tCurrent LineWidth is: {0}", oDefault.line_width)
        oDefault.line_width = LINE_WIDTH.WIDTH2
        self.m_logger.WriteLine6("\tNew LineWidth is: {0}", oDefault.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH2, oDefault.line_width)
        oDefault.show_graphics = True
        self.m_logger.WriteLine4("\tNew Visible flag is: {0}", oDefault.show_graphics)
        Assert.assertEqual(True, oDefault.show_graphics)
        oDefault.color = Colors.from_argb(255)
        self.m_logger.WriteLine6("\tNew Color is: {0}", oDefault.color)
        AssertEx.AreEqual(Colors.from_argb(255), oDefault.color)
        oDefault.line_width = LINE_WIDTH.WIDTH4
        self.m_logger.WriteLine6("\tNew LineWidth is: {0}", oDefault.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH4, oDefault.line_width)
        oDefault.translucency = 50
        Assert.assertEqual(50, oDefault.translucency)

        # Loaded
        oCollection: "VehicleGraphics3DIntervalsCollection" = oIntervals.intervals
        Assert.assertIsNotNone(oCollection)
        self.m_logger.WriteLine3("\tThe current Intervals Collection contains: {0} elements", oCollection.count)
        intervalsElement: "VehicleGraphics3DIntervalsElement" = None

        iIndex: int = 0
        while iIndex < oCollection.count:
            intervalsElement = oCollection[iIndex]
            Assert.assertIsNotNone(intervalsElement)
            self.m_logger.WriteLine10(
                "\t\tElement {0}: StartTime = {1}, StopTime = {2}, Visible = {3}, Color = {4}, LineWidth = {5}",
                iIndex,
                intervalsElement.start_time,
                intervalsElement.stop_time,
                intervalsElement.show_graphics,
                intervalsElement.color,
                intervalsElement.line_width,
            )

            iIndex += 1

        oNewElement1: "VehicleGraphics3DIntervalsElement" = oCollection.add(
            "1 Jul 1999 04:00:00.000", "1 Jul 1999 08:00:00.000"
        )
        Assert.assertIsNotNone(oNewElement1)
        oNewElement2: "VehicleGraphics3DIntervalsElement" = oCollection.add(
            "1 Jul 1999 12:00:00.000", "1 Jul 1999 16:00:00.000"
        )
        Assert.assertIsNotNone(oNewElement2)
        oNewElement3: "VehicleGraphics3DIntervalsElement" = oCollection.add(
            "1 Jul 1999 20:00:00.000", "1 Jul 1999 24:00:00.000"
        )
        Assert.assertIsNotNone(oNewElement3)
        self.m_logger.WriteLine3("\tUpdated Intervals Collection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            intervalsElement = oCollection[iIndex]
            Assert.assertIsNotNone(intervalsElement)
            self.m_logger.WriteLine10(
                "\t\tElement {0}: StartTime = {1}, StopTime = {2}, Visible = {3}, Color = {4}, LineWidth = {5}, Translucency = {6}",
                iIndex,
                intervalsElement.start_time,
                intervalsElement.stop_time,
                intervalsElement.show_graphics,
                intervalsElement.color,
                intervalsElement.line_width,
                intervalsElement.translucency,
            )

            iIndex += 1

        iSize: int = oCollection.count
        oCollection.remove_at(0)
        self.m_logger.WriteLine3(
            "\tAfter RemoveAt(0) the Intervals Collection contains: {0} elements.", oCollection.count
        )
        Assert.assertEqual((iSize - 1), oCollection.count)
        oElmnt: "VehicleGraphics3DIntervalsElement"
        for oElmnt in oCollection:
            self.m_logger.WriteLine10(
                "\t\tElement: StartTime = {0}, StopTime = {1}, Visible = {2}, Color = {3}, LineWidth = {4}, Translucency = {5}",
                oElmnt.start_time,
                oElmnt.stop_time,
                oElmnt.show_graphics,
                oElmnt.color,
                oElmnt.line_width,
                oElmnt.translucency,
            )

        # Element modification test
        intervalsElement = oCollection[0]
        Assert.assertIsNotNone(intervalsElement)
        self.m_logger.WriteLine10(
            "\tElement 0 (before modification): StartTime = {0}, StopTime = {1}, Visible = {2}, Color = {3}, LineWidth = {4}, Translucency = {5}",
            intervalsElement.start_time,
            intervalsElement.stop_time,
            intervalsElement.show_graphics,
            intervalsElement.color,
            intervalsElement.line_width,
            intervalsElement.translucency,
        )
        intervalsElement.start_time = "1 Jan 2000 02:00:00.000"
        intervalsElement.stop_time = "1 Jan 2000 06:00:00.000"

        intervalsElement.translucency = 50
        Assert.assertEqual(50, intervalsElement.translucency)

        intervalsElement.show_graphics = False
        bCaught: bool = False
        try:
            bCaught = False
            intervalsElement.color = Colors.from_argb(6636321)

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Color property should be read only!")

        try:
            bCaught = False
            intervalsElement.line_width = LINE_WIDTH.WIDTH2

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Color property should be read only!")

        self.m_logger.WriteLine10(
            "\tElement 0 (after  modification): StartTime = {0}, StopTime = {1}, Visible = {2}, Color = {3}, LineWidth = {4}",
            intervalsElement.start_time,
            intervalsElement.stop_time,
            intervalsElement.show_graphics,
            intervalsElement.color,
            intervalsElement.line_width,
        )

        oCollection.remove_all()
        self.m_logger.WriteLine3(
            "\tAfter RemoveAll() the Intervals Collection contains: {0} elements.", oCollection.count
        )
        Assert.assertEqual(0, oCollection.count)


# endregion


# region VOCovarianceHelper
class VOCovarianceHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCovariance: "VehicleGraphics3DCovariance"):
        self.m_logger.WriteLine("----- THE VO COVARIANCE TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCovariance)
        # SigmaScaleSupportedTypes
        arChoices = oCovariance.sigma_scale_supported_types
        self.m_logger.WriteLine3("Number of supported Sigma Scale types is: {0}", len(arChoices))

        iIndex: int = 0
        while iIndex < len(arChoices):
            self.m_logger.WriteLine8(
                "\tElement {0}: {1} ({2})",
                iIndex,
                arChoices[iIndex][1],
                VEHICLE_GRAPHICS_3D_SIGMA_SCALE(int(arChoices[iIndex][0])),
            )

            iIndex += 1

        # Scale test
        self.m_logger.WriteLine6("The current Sigma Scale type is: {0}", oCovariance.sigma_scale_type)
        if not oCovariance.is_sigma_scale_type_supported(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.SCALE):
            Assert.fail("The {0} type should be supported.", VEHICLE_GRAPHICS_3D_SIGMA_SCALE.SCALE)

        oCovariance.set_sigma_scale_type(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.SCALE)
        self.m_logger.WriteLine6("The new Sigma Scale type is: {0}", oCovariance.sigma_scale_type)
        Assert.assertEqual(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.SCALE, oCovariance.sigma_scale_type)

        oSSSHelper = VOSigmaScaleScaleHelper()
        oSSSHelper.Run(VehicleGraphics3DSigmaScaleScale(oCovariance.sigma_scale))
        if not oCovariance.is_sigma_scale_type_supported(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.PROBABILITY):
            Assert.fail("The {0} type should be supported.", VEHICLE_GRAPHICS_3D_SIGMA_SCALE.PROBABILITY)

        oCovariance.set_sigma_scale_type(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.PROBABILITY)
        self.m_logger.WriteLine6("The new Sigma Scale type is: {0}", oCovariance.sigma_scale_type)
        Assert.assertEqual(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.PROBABILITY, oCovariance.sigma_scale_type)

        oSSPHelper = VOSigmaScaleProbabilityHelper()
        oSSPHelper.Run(VehicleGraphics3DSigmaScaleProbability(oCovariance.sigma_scale))
        if oCovariance.is_sigma_scale_type_supported(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.UNKNOWN):
            Assert.fail("The UNKNOWN type should be unsupported!")

        with pytest.raises(Exception):
            oCovariance.set_sigma_scale_type(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.UNKNOWN)

        # Attributes test
        arChoices = oCovariance.attributes_supported_types
        Assert.assertIsNotNone(arChoices)
        self.m_logger.WriteLine3("Number of supported Attributes types is: {0}", len(arChoices))

        iIndex: int = 0
        while iIndex < len(arChoices):
            self.m_logger.WriteLine8(
                "\tElement {0}: {1} ({2})",
                iIndex,
                arChoices[iIndex][1],
                VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE(int(arChoices[iIndex][0])),
            )

            iIndex += 1

        # Basic attributes test
        self.m_logger.WriteLine6("The current Attributes type is: {0}", oCovariance.attributes_type)
        if not oCovariance.is_attributes_type_supported(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC):
            Assert.fail("The {0} type should be supported.", VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC)

        oCovariance.set_attributes_type(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC)
        self.m_logger.WriteLine6("The new Attributes type is: {0}", oCovariance.attributes_type)
        Assert.assertEqual(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC, oCovariance.attributes_type)

        oABHelper = VOAttributesBasicHelper()
        oABHelper.Run(VehicleGraphics3DAttributesBasic(oCovariance.attributes))
        if not oCovariance.is_attributes_type_supported(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS):
            Assert.fail("The {0} type should be supported.", VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS)

        oCovariance.set_attributes_type(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS)
        self.m_logger.WriteLine6("The new Attributes type is: {0}", oCovariance.attributes_type)
        Assert.assertEqual(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS, oCovariance.attributes_type)

        oAIHelper = VOAttributesIntervalsHelper()
        oAIHelper.Run(VehicleGraphics3DAttributesIntervals(oCovariance.attributes))
        if oCovariance.is_attributes_type_supported(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.UNKNOWN):
            Assert.fail("The UNKNOWN type should be unsupported!")

        with pytest.raises(Exception):
            oCovariance.set_attributes_type(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.UNKNOWN)

        self.m_logger.WriteLine("----- THE VO COVARIANCE TEST ----- END -----")


# endregion


# region VOVelocityCovarianceHelper
class VOVelocityCovarianceHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oVelCovariance: "VehicleGraphics3DVelCovariance"):
        self.m_logger.WriteLine("----- THE VO VELOCITY COVARIANCE TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oVelCovariance)

        # Scale test
        oVelCovariance.scale = 0.0
        Assert.assertEqual(0.0, oVelCovariance.scale)
        oVelCovariance.scale = 1000000000.0
        Assert.assertEqual(1000000000.0, oVelCovariance.scale)
        # BUG107257
        # TryCatchAssertBlock.ExpectedException("invalid", delegate () { oVelCovariance.Scale = -1;  });
        # TryCatchAssertBlock.ExpectedException("invalid", delegate () { oVelCovariance.Scale = 1e10; });

        # Attributes test
        arChoices = oVelCovariance.attributes_supported_types
        Assert.assertIsNotNone(arChoices)
        self.m_logger.WriteLine3("Number of supported Attributes types is: {0}", len(arChoices))

        iIndex: int = 0
        while iIndex < len(arChoices):
            self.m_logger.WriteLine8(
                "\tElement {0}: {1} ({2})",
                iIndex,
                arChoices[iIndex][1],
                VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE(int(arChoices[iIndex][0])),
            )

            iIndex += 1

        # Basic attributes test
        self.m_logger.WriteLine6("The current Attributes type is: {0}", oVelCovariance.attributes_type)
        if not oVelCovariance.is_attributes_type_supported(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC):
            Assert.fail("The {0} type should be supported.", VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC)

        oVelCovariance.set_attributes_type(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC)
        self.m_logger.WriteLine6("The new Attributes type is: {0}", oVelCovariance.attributes_type)
        Assert.assertEqual(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC, oVelCovariance.attributes_type)

        oABHelper = VOAttributesBasicHelper()
        oABHelper.Run(VehicleGraphics3DAttributesBasic(oVelCovariance.attributes))
        if not oVelCovariance.is_attributes_type_supported(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS):
            Assert.fail("The {0} type should be supported.", VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS)

        oVelCovariance.set_attributes_type(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS)
        self.m_logger.WriteLine6("The new Attributes type is: {0}", oVelCovariance.attributes_type)
        Assert.assertEqual(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS, oVelCovariance.attributes_type)

        oAIHelper = VOAttributesIntervalsHelper()
        oAIHelper.Run(VehicleGraphics3DAttributesIntervals(oVelCovariance.attributes))
        if oVelCovariance.is_attributes_type_supported(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.UNKNOWN):
            Assert.fail("The UNKNOWN type should be unsupported!")

        with pytest.raises(Exception):
            oVelCovariance.set_attributes_type(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.UNKNOWN)

        self.m_logger.WriteLine("----- THE VO VELOCITY COVARIANCE TEST ----- END -----")


# endregion


# region VOCovariancePointingContourHelper
class VOCovariancePointingContourHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCPContour: "VehicleGraphics3DCovariancePointingContour"):
        self.m_logger.WriteLine("----- THE VO COVARIANCE POINTING CONTOUR TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oCPContour)
        arSupportedTypes = oCPContour.attributes_supported_types
        self.m_logger.WriteLine3("Array of supported types contains: {0} elements.", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            self.m_logger.WriteLine8(
                "\tElement {0} is: {1} ({2})",
                iIndex,
                arSupportedTypes[iIndex][1],
                VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE(int(arSupportedTypes[iIndex][0])),
            )

            iIndex += 1

        # Attributes test
        bCaught: bool = False

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            eType: "VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE" = VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE(
                int(arSupportedTypes[iIndex][0])
            )
            if (eType != VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC) and (
                eType != VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS
            ):
                Assert.fail("Invalid type: {0}.", eType)

            if not oCPContour.is_attributes_type_supported(eType):
                Assert.fail("The {0} type should be supported.", eType)

            self.m_logger.WriteLine6("The current Attributes Type is: {0}", oCPContour.attributes_type)
            oCPContour.set_attributes_type(eType)
            self.m_logger.WriteLine6("The new Attributes Type is: {0}", oCPContour.attributes_type)
            eType2: "VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE" = oCPContour.attributes_type
            Assert.assertEqual(eType, eType2)
            if eType == VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.BASIC:
                oHelper = VOAttributesBasicHelper()
                oHelper.Run(VehicleGraphics3DAttributesBasic(oCPContour.attributes))
            elif eType == VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.INTERVALS:
                oHelper = VOAttributesIntervalsHelper()
                oHelper.Run(VehicleGraphics3DAttributesIntervals(oCPContour.attributes))
            else:
                Assert.fail("The {0} type is not supported.", eType)

            iIndex += 1

        if oCPContour.is_attributes_type_supported(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.UNKNOWN):
            Assert.fail("The UNKNOWN type should be unsupported!")

        try:
            bCaught = False
            oCPContour.set_attributes_type(VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE.UNKNOWN)

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Allows to set UNKNOWN type!")

        # SigmaScale test
        arSupportedTypes = oCPContour.sigma_scale_supported_types
        self.m_logger.WriteLine3("Array of supported SigmaScale types contains: {0} elements.", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            self.m_logger.WriteLine8(
                "\tElement {0} is: {1} ({2})",
                iIndex,
                arSupportedTypes[iIndex][1],
                VEHICLE_GRAPHICS_3D_SIGMA_SCALE(int(arSupportedTypes[iIndex][0])),
            )

            iIndex += 1

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            eType: "VEHICLE_GRAPHICS_3D_SIGMA_SCALE" = VEHICLE_GRAPHICS_3D_SIGMA_SCALE(int(arSupportedTypes[iIndex][0]))
            if (eType != VEHICLE_GRAPHICS_3D_SIGMA_SCALE.PROBABILITY) and (
                eType != VEHICLE_GRAPHICS_3D_SIGMA_SCALE.SCALE
            ):
                Assert.fail("Invalid type: {0}.", eType)

            if not oCPContour.is_sigma_scale_type_supported(eType):
                Assert.fail("The {0} type should be supported.", eType)

            self.m_logger.WriteLine6("The current Sigma Scale Type is: {0}", oCPContour.sigma_scale_type)
            oCPContour.set_sigma_scale_type(eType)
            self.m_logger.WriteLine6("The new Sigma Scale Type is: {0}", oCPContour.sigma_scale_type)
            eType2: "VEHICLE_GRAPHICS_3D_SIGMA_SCALE" = oCPContour.sigma_scale_type
            Assert.assertEqual(eType, eType2)
            if eType == VEHICLE_GRAPHICS_3D_SIGMA_SCALE.PROBABILITY:
                oSSPHelper = VOSigmaScaleProbabilityHelper()
                oSSPHelper.Run(VehicleGraphics3DSigmaScaleProbability(oCPContour.sigma_scale))
            elif eType == VEHICLE_GRAPHICS_3D_SIGMA_SCALE.SCALE:
                oSSSHelper = VOSigmaScaleScaleHelper()
                oSSSHelper.Run(VehicleGraphics3DSigmaScaleScale(oCPContour.sigma_scale))
            else:
                Assert.fail("The {0} should not be supported!", eType)

            iIndex += 1

        if oCPContour.is_sigma_scale_type_supported(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.UNKNOWN):
            Assert.fail("The UNKNOWN type should be unsupported!")

        try:
            bCaught = False
            oCPContour.set_sigma_scale_type(VEHICLE_GRAPHICS_3D_SIGMA_SCALE.UNKNOWN)

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Allows to set UNKNOWN type!")

        # ConeVisible test
        self.m_logger.WriteLine4("The current Cone Visible flag is: {0}", oCPContour.show_cone)
        oCPContour.show_cone = False
        self.m_logger.WriteLine4("The new Cone Visible flag is: {0}", oCPContour.show_cone)
        Assert.assertEqual(False, oCPContour.show_cone)
        oCPContour.show_cone = True
        self.m_logger.WriteLine4("The new Cone Visible flag is: {0}", oCPContour.show_cone)
        Assert.assertEqual(True, oCPContour.show_cone)

        # Size test
        oSize: "VehicleGraphics3DSize" = oCPContour.size
        Assert.assertIsNotNone(oSize)
        self.m_logger.WriteLine4("The current Scale to Attitude Sphere flag is: {0}", oSize.scale_to_attitude_sphere)
        oSize.scale_to_attitude_sphere = True
        self.m_logger.WriteLine4("The new Scale to Attitude Sphere flag is: {0}", oSize.scale_to_attitude_sphere)
        Assert.assertEqual(True, oSize.scale_to_attitude_sphere)
        try:
            bCaught = False
            oSize.scale_value = 5.6789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Scale should be readonly when Scale to Attitude Sphere flag is True.")

        oSize.scale_to_attitude_sphere = False
        self.m_logger.WriteLine4("The new Scale to Attitude Sphere flag is: {0}", oSize.scale_to_attitude_sphere)
        Assert.assertEqual(False, oSize.scale_to_attitude_sphere)
        self.m_logger.WriteLine6("The current Scale is: {0}", oSize.scale_value)
        oSize.scale_value = 5.6789
        self.m_logger.WriteLine6("The new Scale is: {0}", oSize.scale_value)
        Assert.assertEqual(5.6789, oSize.scale_value)
        try:
            bCaught = False
            oSize.scale_value = 333.3

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Scale should not allow to set value > 10.")

        # LinkToObject test
        oLTOHelper = LinkToObjectHelper()
        oLTOHelper.Run(oCPContour.to_object, "CovariancePointingContour")
        self.m_logger.WriteLine("----- THE VO COVARIANCE POINTING CONTOUR TEST ----- END -----")


# endregion


# region VODropLinePosItemCollectionHelper
class VODropLinePosItemCollectionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "VehicleGraphics3DDropLinePositionItemCollection"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The DropLinePosItem collection contains: {0} elements", oCollection.count)
        # _NewEnum
        oItem: "VehicleGraphics3DDropLinePositionItem"
        # _NewEnum
        for oItem in oCollection:
            self.m_logger.WriteLine6("\tElement: {0}", oItem.type)

        iIndex: int = 0
        while iIndex < oCollection.count:
            dropLinePosItem: "VehicleGraphics3DDropLinePositionItem" = oCollection[iIndex]
            Assert.assertIsNotNone(dropLinePosItem)
            # Type
            self.m_logger.WriteLine7("Element {0} is: {1}", iIndex, dropLinePosItem.type)
            # IsVisible (false)
            self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", dropLinePosItem.show_graphics)
            dropLinePosItem.show_graphics = False
            self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", dropLinePosItem.show_graphics)
            Assert.assertEqual(False, dropLinePosItem.show_graphics)
            # Use2DColor
            with pytest.raises(Exception):
                dropLinePosItem.use_2d_color = False
            # Color
            with pytest.raises(Exception):
                dropLinePosItem.color = Colors.from_argb(16448250)
            # LineWidth
            with pytest.raises(Exception):
                dropLinePosItem.line_width = LINE_WIDTH.WIDTH3
            # LineStyle
            with pytest.raises(Exception):
                dropLinePosItem.line_style = LINE_STYLE.DOTTED
            # IsVisible (true)
            dropLinePosItem.show_graphics = True
            self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", dropLinePosItem.show_graphics)
            Assert.assertEqual(True, dropLinePosItem.show_graphics)
            # Use2DColor (true)
            self.m_logger.WriteLine4("\tThe current Use2DColor flag is: {0}", dropLinePosItem.use_2d_color)
            dropLinePosItem.use_2d_color = True
            self.m_logger.WriteLine4("\tThe new Use2DColor flag is: {0}", dropLinePosItem.use_2d_color)
            Assert.assertEqual(True, dropLinePosItem.use_2d_color)
            # Color
            with pytest.raises(Exception):
                dropLinePosItem.color = Colors.from_argb(16448250)
            # Use2DColor (false)
            dropLinePosItem.use_2d_color = False
            self.m_logger.WriteLine4("\tThe new Use2DColor flag is: {0}", dropLinePosItem.use_2d_color)
            Assert.assertEqual(False, dropLinePosItem.use_2d_color)
            # Color
            self.m_logger.WriteLine6("\tThe current Color is: {0}", dropLinePosItem.color)
            dropLinePosItem.color = Colors.from_argb(16448175)
            self.m_logger.WriteLine6("\tThe new Color is: {0}", dropLinePosItem.color)
            AssertEx.AreEqual(Colors.from_argb(16448175), dropLinePosItem.color)
            # LineWidth
            self.m_logger.WriteLine6("\tThe current LineWidth  is: {0}", dropLinePosItem.line_width)
            dropLinePosItem.line_width = LINE_WIDTH.WIDTH3
            self.m_logger.WriteLine6("\tThe new LineWidth is: {0}", dropLinePosItem.line_width)
            Assert.assertEqual(LINE_WIDTH.WIDTH3, dropLinePosItem.line_width)
            # LineStyle
            self.m_logger.WriteLine6("\tThe current LineStyle is: {0}", dropLinePosItem.line_style)
            dropLinePosItem.line_style = LINE_STYLE.DASHED  # Dashed
            self.m_logger.WriteLine6("\tThe new LineStyle is: {0}", dropLinePosItem.line_style)
            Assert.assertEqual(LINE_STYLE.DASHED, dropLinePosItem.line_style)

            iIndex += 1


# endregion


# region VODropLinePathItemCollectionHelper
class VODropLinePathItemCollectionHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oCollection: "VehicleGraphics3DDropLinePathItemCollection"):
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("The DropLinePathItem collection contains: {0} elements", oCollection.count)
        # _NewEnum
        oItem: "VehicleGraphics3DDropLinePathItem"
        # _NewEnum
        for oItem in oCollection:
            self.m_logger.WriteLine6("\tElement: {0}", oItem.type)

        iIndex: int = 0
        while iIndex < oCollection.count:
            dropLinePathItem: "VehicleGraphics3DDropLinePathItem" = oCollection[iIndex]
            Assert.assertIsNotNone(dropLinePathItem)
            # Type
            self.m_logger.WriteLine7("Element {0} is: {1}", iIndex, dropLinePathItem.type)
            # IsVisible (false)
            self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", dropLinePathItem.show_graphics)
            dropLinePathItem.show_graphics = False
            self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", dropLinePathItem.show_graphics)
            Assert.assertEqual(False, dropLinePathItem.show_graphics)
            # Use2DColor
            with pytest.raises(Exception):
                dropLinePathItem.use_2d_color = False
            # Color
            with pytest.raises(Exception):
                dropLinePathItem.color = Colors.from_argb(16448250)
            # LineWidth
            with pytest.raises(Exception):
                dropLinePathItem.line_width = LINE_WIDTH.WIDTH3
            # LineStyle
            with pytest.raises(Exception):
                dropLinePathItem.line_style = LINE_STYLE.SOLID
            # Interval
            with pytest.raises(Exception):
                dropLinePathItem.interval = 123.456
            # IsVisible (true)
            dropLinePathItem.show_graphics = True
            self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", dropLinePathItem.show_graphics)
            Assert.assertEqual(True, dropLinePathItem.show_graphics)
            # Use2DColor (true)
            self.m_logger.WriteLine4("\tThe current Use2DColor flag is: {0}", dropLinePathItem.use_2d_color)
            dropLinePathItem.use_2d_color = True
            self.m_logger.WriteLine4("\tThe new Use2DColor flag is: {0}", dropLinePathItem.use_2d_color)
            Assert.assertEqual(True, dropLinePathItem.use_2d_color)
            # Color
            with pytest.raises(Exception):
                dropLinePathItem.color = Colors.from_argb(16448250)
            # Use2DColor (false)
            dropLinePathItem.use_2d_color = False
            self.m_logger.WriteLine4("\tThe new Use2DColor flag is: {0}", dropLinePathItem.use_2d_color)
            Assert.assertEqual(False, dropLinePathItem.use_2d_color)
            # Color
            self.m_logger.WriteLine6("\tThe current Color is: {0}", dropLinePathItem.color)
            dropLinePathItem.color = Colors.from_argb(16448018)
            self.m_logger.WriteLine6("\tThe new Color is: {0}", dropLinePathItem.color)
            AssertEx.AreEqual(Colors.from_argb(16448018), dropLinePathItem.color)
            # LineWidth
            self.m_logger.WriteLine6("\tThe current LineWidth  is: {0}", dropLinePathItem.line_width)
            dropLinePathItem.line_width = LINE_WIDTH.WIDTH3
            self.m_logger.WriteLine6("\tThe new LineWidth is: {0}", dropLinePathItem.line_width)
            Assert.assertEqual(LINE_WIDTH.WIDTH3, dropLinePathItem.line_width)
            # LineStyle
            self.m_logger.WriteLine6("\tThe current LineStyle is: {0}", dropLinePathItem.line_style)
            dropLinePathItem.line_style = LINE_STYLE.DASHED  # Dashed
            self.m_logger.WriteLine6("\tThe new LineStyle is: {0}", dropLinePathItem.line_style)
            Assert.assertEqual(LINE_STYLE.DASHED, dropLinePathItem.line_style)
            # Interval
            self.m_logger.WriteLine6("\tThe current Interval is: {0}", dropLinePathItem.interval)
            dropLinePathItem.interval = 123.456
            self.m_logger.WriteLine6("\tThe new Interval is: {0}", dropLinePathItem.interval)
            Assert.assertEqual(123.456, dropLinePathItem.interval)
            with pytest.raises(Exception):
                dropLinePathItem.interval = -123.456

            iIndex += 1


# endregion


# region VOElevationContoursHelper
class VOElevationContoursHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oContours: "VehicleGraphics3DElevationContours"):
        self.m_logger.WriteLine("----- THE VO ELEVATION CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        bCaught: bool = False
        self.m_logger.WriteLine4("The current Visible flag is: {0}", oContours.show_graphics)
        oContours.show_graphics = False
        self.m_logger.WriteLine4("The new Visible flag is: {0}", oContours.show_graphics)
        Assert.assertEqual(False, oContours.show_graphics)
        try:
            bCaught = False
            oContours.show_filled_cones = False

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Visible Cones flag should be readonly when Visible flag is False.")

        try:
            bCaught = False
            oContours.translucency = 50.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Cones Translucency should be readonly when Visible flag is False.")

        try:
            bCaught = False
            oContours.fill = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Fill flag should be readonly when Visible flag is False.")

        try:
            bCaught = False
            oContours.fill_translucency = 30.3

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Fill Translucency should be readonly when Visible flag is False.")

        oContours.show_graphics = True
        self.m_logger.WriteLine4("The new Visible flag is: {0}", oContours.show_graphics)
        Assert.assertEqual(True, oContours.show_graphics)
        self.m_logger.WriteLine4("The current Cones Visible flag is: {0}", oContours.show_filled_cones)
        oContours.show_filled_cones = False
        self.m_logger.WriteLine4("The new Cones Visible flag is: {0}", oContours.show_filled_cones)
        Assert.assertEqual(False, oContours.show_filled_cones)
        try:
            bCaught = False
            oContours.translucency = 50.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Cones Translucency should be readonly when Cones Visible flag is False.")

        oContours.show_filled_cones = True
        self.m_logger.WriteLine4("The new Cones Visible flag is: {0}", oContours.show_filled_cones)
        Assert.assertEqual(True, oContours.show_filled_cones)
        self.m_logger.WriteLine6("\tThe current Cones Translucency is: {0}", oContours.translucency)
        oContours.translucency = 55.55
        self.m_logger.WriteLine6("\tThe new Cones Translucency is: {0}", oContours.translucency)
        Assert.assertEqual(55.55, oContours.translucency)
        try:
            bCaught = False
            oContours.translucency = 555.555

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Cones Translucency should not allow to set value > 100.")

        try:
            bCaught = False
            oContours.translucency = -5.5

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Cones Translucency should not allow to set negative values.")

        self.m_logger.WriteLine4("The current Fill flag is: {0}", oContours.fill)
        oContours.fill = False
        self.m_logger.WriteLine4("The new Fill flag is: {0}", oContours.fill)
        Assert.assertEqual(False, oContours.fill)
        try:
            bCaught = False
            oContours.fill_translucency = 33.33

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Fill Translucency should be readonly when Fill flag is False.")

        oContours.fill = True
        self.m_logger.WriteLine4("The new Fill flag is: {0}", oContours.fill)
        Assert.assertEqual(True, oContours.fill)
        self.m_logger.WriteLine6("\tThe current Fill Translucency is: {0}", oContours.fill_translucency)
        oContours.fill_translucency = 33.33
        self.m_logger.WriteLine6("\tThe new Fill Translucency is: {0}", oContours.fill_translucency)
        Assert.assertEqual(33.33, oContours.fill_translucency)
        try:
            bCaught = False
            oContours.fill_translucency = 333.333

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Fill Translucency should not allow to set value > 100.")

        try:
            bCaught = False
            oContours.fill_translucency = -3.3

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Fill Translucency should not allow to set negative values.")

        self.m_logger.WriteLine("----- THE VO ELEVATION CONTOURS TEST ----- END -----")


# endregion


# region VORouteModelHelper
class VORouteModelHelper(object):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self._root: "StkObjectRoot" = root
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oModel: "VehicleGraphics3DModelRoute"):
        self.m_logger.WriteLine("----- THE VO MODEL TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oModel)

        # IsPointVisible (false)
        self.m_logger.WriteLine4("\tThe current IsPointVisible is: {0}", oModel.show_point)
        oModel.show_point = False
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.show_point)
        Assert.assertEqual(False, oModel.show_point)
        # PointSize
        with pytest.raises(Exception):
            oModel.point_size = 12.3456
        # IsPointVisible (true)
        oModel.show_point = True
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.show_point)
        Assert.assertEqual(True, oModel.show_point)
        # PointSize
        self.m_logger.WriteLine6("\tThe current PointSize is: {0}", oModel.point_size)
        oModel.point_size = 12.3456
        self.m_logger.WriteLine6("\tThe new PointSize is: {0}", oModel.point_size)
        Assert.assertAlmostEqual(12.3456, float(oModel.point_size), delta=0.0001)
        with pytest.raises(Exception):
            oModel.point_size = 123.456

        # GLTF

        (clr.CastAs(oModel.model_data, Graphics3DModelFile)).filename = Path.Combine(
            TestBase.ModelDirectory, "scaling_sphere.mdl"
        )  # need a model that does not support GLTF settings
        with pytest.raises(Exception, match=RegexSubstringMatch("glTF settings are not available")):
            oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT
        (
            clr.CastAs(oModel.model_data, Graphics3DModelFile)
        ).filename = r"STKData\VO\Models\Land\facility.glb"  # need a model that supports GLTF settings
        oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT
        Assert.assertEqual(MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT, oModel.gltf_reflection_map_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not set to Image Based")):
            x: "Graphics3DModelglTFImageBased" = oModel.gltf_image_based

        oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.IMAGE_BASED
        Assert.assertEqual(MODEL_GLTF_REFLECTION_MAP_TYPE.IMAGE_BASED, oModel.gltf_reflection_map_type)

        gltfImageBased: "Graphics3DModelglTFImageBased" = oModel.gltf_image_based
        gltfImageBased.filename = TestBase.GetScenarioFile("over_the_clouds.hdr")
        Assert.assertEqual("over_the_clouds.hdr", gltfImageBased.filename)
        Assert.assertTrue(("over_the_clouds.hdr" in gltfImageBased.file_path))

        gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 ICRF"
        Assert.assertEqual("Satellite/Satellite1 ICRF", gltfImageBased.reflection_reference_frame)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 Bogus"

        # Base class properties test
        oModelHelper = VOModelHelper(self._root, self.m_oUnits)
        oModelHelper.Run(oModel)

        self.m_logger.WriteLine("----- THE VO MODEL TEST ----- END -----")


# endregion


# region VOMarkerHelper
class VOMarkerHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Test_IAgVOMarkerFile method
    def Test_IAgVOMarkerFile(self, oFile: "Graphics3DMarkerFile"):
        oFile.filename = TestBase.PathCombine("STKData", "VO", "Markers", "Star.ppm")
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Markers", "Star.ppm"), oFile.filename)
        oFile.filename = TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm")
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm"), oFile.filename)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            oFile.filename = TestBase.PathCombine("STKData", "VO", "Markers", "Bogus.ppm")

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
    def Run(self, oMarker: "Graphics3DMarker", bIsVehicle: bool):
        Assert.assertIsNotNone(oMarker)

        oMarker.visible = False
        Assert.assertFalse(oMarker.visible)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oMarker.angle = 1.23
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oMarker.marker_type = MARKER_TYPE.IMAGE_FILE
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oMarker.orientation_mode = GRAPHICS_3D_MARKER_ORIENTATION.ANGLE
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oMarker.pixel_size = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oMarker.x_origin = 0
        # BUG86168 TryCatchAssertBlock.ExpectedException("read-only", delegate() { oMarker.YOrigin = 0; }); "Value does not fall within the expected range"

        oMarker.visible = True
        Assert.assertTrue(oMarker.visible)

        oMarker.marker_type = MARKER_TYPE.SHAPE
        Assert.assertEqual(MARKER_TYPE.SHAPE, oMarker.marker_type)

        oShape: "Graphics3DMarkerShape" = clr.CastAs(oMarker.marker_data, Graphics3DMarkerShape)
        Assert.assertIsNotNone(oShape)
        oShape.style = MARKER_SHAPE_3D.SHAPE_CIRCLE
        Assert.assertEqual(MARKER_SHAPE_3D.SHAPE_CIRCLE, oShape.style)
        oShape.style = MARKER_SHAPE_3D.SHAPE_POINT
        Assert.assertEqual(MARKER_SHAPE_3D.SHAPE_POINT, oShape.style)
        with pytest.raises(STKInvalidCastError):
            voMarkerFileX: "Graphics3DMarkerFile" = Graphics3DMarkerFile(oMarker.marker_data)

        oMarker.marker_type = (
            MARKER_TYPE.IMAGE_FILE
        )  # This property will not be set to this enum. See below, and see helpstrings.
        oMarker.set_marker_image_filename(
            TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm")
        )  # This will set the MarkerType to IMAGE_FILE

        Assert.assertEqual(MARKER_TYPE.IMAGE_FILE, oMarker.marker_type)
        oFile: "Graphics3DMarkerFile" = clr.CastAs(oMarker.marker_data, Graphics3DMarkerFile)
        Assert.assertIsNotNone(oFile)
        self.Test_IAgVOMarkerFile(oFile)
        with pytest.raises(STKInvalidCastError):
            oShape = Graphics3DMarkerShape(oMarker.marker_data)

        oMarker.pixel_size = 12
        Assert.assertEqual(12, oMarker.pixel_size)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oMarker.pixel_size = 1234

        oMarker.x_origin = GRAPHICS_3D_MARKER_ORIGIN_TYPE.RIGHT
        Assert.assertEqual(GRAPHICS_3D_MARKER_ORIGIN_TYPE.RIGHT, oMarker.x_origin)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            oMarker.x_origin = GRAPHICS_3D_MARKER_ORIGIN_TYPE.TOP

        oMarker.y_origin = GRAPHICS_3D_MARKER_ORIGIN_TYPE.BOTTOM
        Assert.assertEqual(GRAPHICS_3D_MARKER_ORIGIN_TYPE.BOTTOM, oMarker.y_origin)
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            oMarker.y_origin = GRAPHICS_3D_MARKER_ORIGIN_TYPE.LEFT

        oMarker.orientation_mode = GRAPHICS_3D_MARKER_ORIENTATION.NONE
        Assert.assertEqual(GRAPHICS_3D_MARKER_ORIENTATION.NONE, oMarker.orientation_mode)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oMarker.angle = 1.23
        if bIsVehicle:
            oMarker.orientation_mode = GRAPHICS_3D_MARKER_ORIENTATION.FOLLOW_DIRECTION
            Assert.assertEqual(GRAPHICS_3D_MARKER_ORIENTATION.FOLLOW_DIRECTION, oMarker.orientation_mode)

            oMarker.angle = 1.23456
            Assert.assertEqual(1.23456, oMarker.angle)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                oMarker.angle = 361

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("Only supported for vehicle")):
                oMarker.orientation_mode = GRAPHICS_3D_MARKER_ORIENTATION.FOLLOW_DIRECTION

        oMarker.orientation_mode = GRAPHICS_3D_MARKER_ORIENTATION.ANGLE
        Assert.assertEqual(GRAPHICS_3D_MARKER_ORIENTATION.ANGLE, oMarker.orientation_mode)

        oMarker.angle = 1.23456
        Assert.assertEqual(1.23456, oMarker.angle)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oMarker.angle = 361


# endregion


# region VOModelHelper
class VOModelHelper(object):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self._root: "StkObjectRoot" = root
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oModel: "IGraphics3DModel"):
        Assert.assertIsNotNone(oModel)
        self.m_logger.WriteLine("VO Model test:")

        # Visible
        self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oModel.visible)
        oModel.visible = False
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oModel.visible)
        Assert.assertFalse(oModel.visible)
        with pytest.raises(Exception):
            oModel.scale_value = 3.3
        with pytest.raises(Exception):
            oModel.model_type = MODEL_TYPE.FILE

        oModel.visible = True
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oModel.visible)
        Assert.assertTrue(oModel.visible)
        # ScaleValue
        self.m_logger.WriteLine6("\tThe current Scale flag is: {0}", oModel.scale_value)
        oModel.scale_value = 3.33
        self.m_logger.WriteLine6("\tThe new Scale flag is: {0}", oModel.scale_value)
        Assert.assertEqual(3.33, oModel.scale_value)
        with pytest.raises(Exception):
            oModel.scale_value = -12.34

        # ModelType (File)
        self.m_logger.WriteLine6("\tThe current ModelType is: {0}", oModel.model_type)
        oModel.model_type = MODEL_TYPE.FILE
        self.m_logger.WriteLine6("\tThe new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        oModelFile: "Graphics3DModelFile" = clr.CastAs(oModel.model_data, Graphics3DModelFile)
        Assert.assertIsNotNone(oModelFile)
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "pegasus.mdl")
        Assert.assertEqual(TestBase.PathCombine("VO", "Models", "pegasus.mdl"), oModelFile.filename)
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.filename)
        with pytest.raises(Exception):
            oModelFile.filename = "sat.mdl"
        with pytest.raises(Exception):
            oModelFile.filename = ""
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "satellite.dae")
        Assert.assertEqual(TestBase.PathCombine("VO", "Models", "satellite.dae"), oModelFile.filename)
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.filename)
        # FilePath
        Assert.assertEqual(TestBase.GetScenarioFile("VO", "Models", "satellite.dae"), oModelFile.file_path)

        # ModelType (List)
        oModel.model_type = MODEL_TYPE.LIST
        self.m_logger.WriteLine6("\tThe new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.LIST, oModel.model_type)
        oModelList: "Graphics3DModelCollection" = clr.CastAs(oModel.model_data, Graphics3DModelCollection)
        Assert.assertIsNotNone(oModelList)
        iSize: int = oModelList.count
        self.m_logger.WriteLine3("\t\tThe Model list collection contains: {0} elements", iSize)

        iIndex: int = 0
        while iIndex < iSize:
            self.m_logger.WriteLine8(
                "\t\t\tElement {0}: ModelFile = {1}, SwitchTime = {2}",
                iIndex,
                oModelList[iIndex].graphics_3d_model_file.file_path,
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
        with pytest.raises(Exception):
            oModelList.add(oModelList[0].switch_time, oModelList[0].graphics_3d_model_file.file_path)
        oModelList.add((time + 1), oModelList[0].graphics_3d_model_file.file_path)
        iSize = oModelList.count
        self.m_logger.WriteLine3("\t\tThe Model list collection contains: {0} elements", iSize)

        iIndex: int = 0
        while iIndex < iSize:
            self.m_logger.WriteLine8(
                "\t\t\tElement {0}: ModelFile = {1}, SwitchTime = {2}",
                iIndex,
                oModelList[iIndex].graphics_3d_model_file.file_path,
                oModelList[iIndex].switch_time,
            )

            iIndex += 1

        if iSize > 1:
            oModelList.remove(0)
            self.m_logger.WriteLine3("\t\tAfter Remove(0) the ModelList contains: {0} elements", oModelList.count)
            oItem: "Graphics3DModelItem"
            for oItem in oModelList:
                self.m_logger.WriteLine7(
                    "\t\t\tElement (before modification): ModelFile = {0}, SwitchTime = {1}",
                    oItem.graphics_3d_model_file.file_path,
                    oItem.switch_time,
                )
                oItem.graphics_3d_model_file.filename = oItem.graphics_3d_model_file.filename
                oItem.switch_time = time - 12
                self.m_logger.WriteLine7(
                    "\t\t\tElement (after modification): ModelFile = {0}, SwitchTime = {1}",
                    oItem.graphics_3d_model_file.file_path,
                    oItem.switch_time,
                )

                voModelFile: "Graphics3DModelFile" = oItem.graphics_3d_model_file
                Assert.assertEqual((TestBase.PathCombine("VO", "Models", "satellite.dae")), voModelFile.filename)
                Assert.assertTrue((TestBase.PathCombine("VO", "Models", "satellite.dae") in voModelFile.file_path))
                voModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "pegasus.mdl")
                Assert.assertEqual(TestBase.PathCombine("VO", "Models", "pegasus.mdl"), voModelFile.filename)
                Assert.assertTrue((TestBase.PathCombine("VO", "Models", "pegasus.mdl") in voModelFile.file_path))
                with pytest.raises(Exception, match=RegexSubstringMatch("file does not exist")):
                    voModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "bogus.dae")

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
        oModel.model_type = MODEL_TYPE.FILE
        Assert.assertTrue((oModel.model_type == MODEL_TYPE.FILE))
        oldModel: str = (clr.CastAs(oModel.model_data, Graphics3DModelFile)).filename
        self._root.begin_update()
        try:
            oModel.model_type = MODEL_TYPE.FILE
            modelFile: "Graphics3DModelFile" = clr.CastAs(oModel.model_data, Graphics3DModelFile)
            modelFile.filename = Path.Combine(TestBase.ModelDirectory, "hubble.glb")

            oModel.articulation.set_transformation_value(0, "HGA_Arm_1", "Fold", 90)

        finally:
            self._root.end_update()

        oModel.model_type = MODEL_TYPE.LIST
        modelList: "Graphics3DModelCollection" = clr.CastAs(oModel.model_data, Graphics3DModelCollection)
        while modelList.count > 1:
            modelList.remove((modelList.count - 1))
        modelList[0].graphics_3d_model_file.filename = oldModel
        with pytest.raises(Exception):
            oModel.articulation.set_transformation_value(0, "HGA_Arm_1", "Fold", 90)

        self._root.begin_update()
        try:
            modelList[0].graphics_3d_model_file.filename = Path.Combine(TestBase.ModelDirectory, "hubble.glb")
            oModel.articulation.set_transformation_value(0, "HGA_Arm_1", "Fold", 90)

        finally:
            self._root.end_update()
            oModel.model_type = MODEL_TYPE.FILE

    # endregion

    # region VODetailThreshold
    def VODetailThreshold(self, oDetail: "Graphics3DDetailThreshold"):
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
    def VOArticulation(self, oArticulation: "Graphics3DModelArticulation"):
        Assert.assertIsNotNone(oArticulation)

        oArticulation.enable_default_save = False
        Assert.assertEqual(False, oArticulation.enable_default_save)
        oArticulation.enable_default_save = True
        Assert.assertEqual(True, oArticulation.enable_default_save)

        oArticulation.save_articulation_file_on_save = False
        Assert.assertEqual(False, oArticulation.save_articulation_file_on_save)
        oArticulation.save_articulation_file_on_save = True
        Assert.assertEqual(True, oArticulation.save_articulation_file_on_save)

        oArticulation.save_articulation_file_on_save = False
        Assert.assertEqual(False, oArticulation.save_articulation_file_on_save)
        oArticulation.save_articulation_file_on_save = True
        Assert.assertEqual(True, oArticulation.save_articulation_file_on_save)

        oArticulation.use_object_color_for_model = False
        Assert.assertFalse(oArticulation.use_object_color_for_model)
        oArticulation.use_object_color_for_model = True
        Assert.assertTrue(oArticulation.use_object_color_for_model)

        articFile: "Graphics3DArticulationFile" = oArticulation.graphics_3d_articulation_file
        oArticulation.use_articulation_file = False

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            articFile.filename = TestBase.GetScenarioFile("Test.sama")

        oArticulation.use_articulation_file = True

        with pytest.raises(Exception, match=RegexSubstringMatch("not found")):
            articFile.filename = TestBase.GetScenarioFile("Bogus.sama")

        articFile.filename = TestBase.GetScenarioFile("Test.sama")
        Assert.assertTrue(("Test.sama" in articFile.filename))

        articFile.reload()

        # LODs test
        self.m_logger.WriteLine3("\tThe number of LODs is: {0}", oArticulation.level_of_detail_count)

        iIndex: int = 0
        while iIndex < oArticulation.level_of_detail_count:
            self.m_logger.WriteLine3("\t\tLODs: {0}", iIndex)
            arAvailableArtic = oArticulation.get_available_articulations(iIndex)
            self.m_logger.WriteLine3("\t\t\tThere are {0} available Articulations.", Array.Length(arAvailableArtic))

            i: int = 0
            while i < Array.Length(arAvailableArtic):
                strArtic: str = str(arAvailableArtic[i])
                self.m_logger.WriteLine7("\t\t\t\tArticulation {0} is: {1}", i, strArtic)
                # TransCollection test
                oTransformations: "Graphics3DModelTransformationCollection" = (
                    oArticulation.get_available_transformations(iIndex, strArtic)
                )
                Assert.assertIsNotNone(oTransformations)
                self.m_logger.WriteLine5("\t\t\t\tTransformation name is: {0}.", oTransformations.name)
                self.m_logger.WriteLine3("\t\t\t\tThere are {0} available Transformations.", oTransformations.count)

                j: int = 0
                while j < oTransformations.count:
                    modelTrans: "Graphics3DModelTransformation" = oTransformations[j]
                    strTrans: str = modelTrans.name
                    self.m_logger.WriteLine7("\t\t\t\t\tTransformation {0} is: {1}", j, strTrans)
                    self.m_logger.WriteLine8(
                        "\t\t\t\t\t\tCurrent value: {0} [Min = {1}, Max = {2}]",
                        modelTrans.value,
                        modelTrans.minimum,
                        modelTrans.maximum,
                    )
                    dMax: float = (
                        modelTrans.maximum
                        if ((Math.Abs(modelTrans.maximum) > Math.Abs(modelTrans.minimum)))
                        else modelTrans.minimum
                    )
                    dMin: float = (
                        modelTrans.maximum
                        if ((Math.Abs(modelTrans.maximum) < Math.Abs(modelTrans.minimum)))
                        else modelTrans.minimum
                    )
                    dMidle: float = ((dMax - dMin)) / 2.0
                    modelTrans.value = dMidle
                    oArticulation.set_transformation_value(iIndex, strArtic, strTrans, dMidle)
                    self.m_logger.WriteLine6(
                        "\t\t\t\t\t\tNew value: {0}", oArticulation.get_transformation_value(iIndex, strArtic, strTrans)
                    )
                    Assert.assertEqual(dMidle, oArticulation.get_transformation_value(iIndex, strArtic, strTrans))
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
                oItem: "Graphics3DModelTransformation"
                # Collection enumeration test
                for oItem in oTransformations:
                    Assert.assertIsNotNone(oItem)

                i += 1

            iIndex += 1


# endregion


# region VOTargetModelHelper
class VOTargetModelHelper(object):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self._root: "StkObjectRoot" = root
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oModel: "PointTargetGraphics3DModel"):
        Assert.assertIsNotNone(oModel)
        # IsPointVisible (false)
        self.m_logger.WriteLine4("\tThe current IsPointVisible is: {0}", oModel.show_point)
        oModel.show_point = False
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.show_point)
        Assert.assertEqual(False, oModel.show_point)
        # PointSize
        with pytest.raises(Exception):
            oModel.point_size = 12.3456
        # IsPointVisible (true)
        oModel.show_point = True
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.show_point)
        Assert.assertEqual(True, oModel.show_point)
        # PointSize
        self.m_logger.WriteLine6("\tThe current PointSize is: {0}", oModel.point_size)
        oModel.point_size = 12.3456
        self.m_logger.WriteLine6("\tThe new PointSize is: {0}", oModel.point_size)
        Assert.assertAlmostEqual(12.3456, float(oModel.point_size), delta=0.0001)
        with pytest.raises(Exception):
            oModel.point_size = 123.456

        # GLTF

        (clr.CastAs(oModel.model_data, Graphics3DModelFile)).filename = Path.Combine(
            TestBase.ModelDirectory, "scaling_sphere.mdl"
        )  # need a model that does not support GLTF settings
        with pytest.raises(Exception, match=RegexSubstringMatch("glTF settings are not available")):
            oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT
        (
            clr.CastAs(oModel.model_data, Graphics3DModelFile)
        ).filename = r"STKData\VO\Models\Land\facility.glb"  # need a model that supports GLTF settings
        oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT
        Assert.assertEqual(MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT, oModel.gltf_reflection_map_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not set to Image Based")):
            x: "Graphics3DModelglTFImageBased" = oModel.gltf_image_based

        oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.IMAGE_BASED
        Assert.assertEqual(MODEL_GLTF_REFLECTION_MAP_TYPE.IMAGE_BASED, oModel.gltf_reflection_map_type)

        gltfImageBased: "Graphics3DModelglTFImageBased" = oModel.gltf_image_based
        gltfImageBased.filename = TestBase.GetScenarioFile("over_the_clouds.hdr")
        Assert.assertEqual("over_the_clouds.hdr", gltfImageBased.filename)
        Assert.assertTrue(("over_the_clouds.hdr" in gltfImageBased.file_path))

        gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 ICRF"
        Assert.assertEqual("Satellite/Satellite1 ICRF", gltfImageBased.reflection_reference_frame)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 Bogus"

        # Base class properties test
        oModelHelper = VOModelHelper(self._root, self.m_oUnits)
        oModelHelper.Run(oModel)


# endregion


# region VOTrajectoryModelHelper
class VOTrajectoryModelHelper(object):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self._root: "StkObjectRoot" = root
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oModel: "VehicleGraphics3DModelTrajectory", IsLaunchVehicle: bool):
        self.m_logger.WriteLine("----- THE VO MODEL TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oModel)

        # IsPointVisible (false)
        self.m_logger.WriteLine4("\tThe current IsPointVisible is: {0}", oModel.show_point)
        oModel.show_point = False
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.show_point)
        Assert.assertEqual(False, oModel.show_point)
        # PointSize
        with pytest.raises(Exception):
            oModel.point_size = 12.3456
        # IsPointVisible (true)
        oModel.show_point = True
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.show_point)
        Assert.assertEqual(True, oModel.show_point)
        # PointSize
        self.m_logger.WriteLine6("\tThe current PointSize is: {0}", oModel.point_size)
        oModel.point_size = 12.3456
        self.m_logger.WriteLine6("\tThe new PointSize is: {0}", oModel.point_size)
        Assert.assertAlmostEqual(12.3456, float(oModel.point_size), delta=0.0001)
        with pytest.raises(Exception):
            oModel.point_size = 123.456

        # GLTF

        (clr.CastAs(oModel.model_data, Graphics3DModelFile)).filename = Path.Combine(
            TestBase.ModelDirectory, "scaling_sphere.mdl"
        )  # need a model that does not support GLTF settings
        with pytest.raises(Exception, match=RegexSubstringMatch("glTF settings are not available")):
            oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT
        (
            clr.CastAs(oModel.model_data, Graphics3DModelFile)
        ).filename = r"STKData\VO\Models\Land\facility.glb"  # need a model that supports GLTF settings
        oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT
        Assert.assertEqual(MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT, oModel.gltf_reflection_map_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not set to Image Based")):
            x: "Graphics3DModelglTFImageBased" = oModel.gltf_image_based

        oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.IMAGE_BASED
        Assert.assertEqual(MODEL_GLTF_REFLECTION_MAP_TYPE.IMAGE_BASED, oModel.gltf_reflection_map_type)

        gltfImageBased: "Graphics3DModelglTFImageBased" = oModel.gltf_image_based
        gltfImageBased.filename = TestBase.GetScenarioFile("over_the_clouds.hdr")
        Assert.assertEqual("over_the_clouds.hdr", gltfImageBased.filename)
        Assert.assertTrue(("over_the_clouds.hdr" in gltfImageBased.file_path))

        gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 ICRF"
        Assert.assertEqual("Satellite/Satellite1 ICRF", gltfImageBased.reflection_reference_frame)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 Bogus"

        # Base class properties test
        oModelHelper = VOModelHelper(self._root, self.m_oUnits)
        oModelHelper.Run(oModel)

        # TrajectoryMarker test
        oMarkerHelper = VOMarkerHelper(self.m_oUnits)
        oMarkerHelper.Run(oModel.trajectory_marker, True)

        # GroundMarker test
        oMarkerHelper.Run(oModel.ground_marker, True)

        self.m_logger.WriteLine("----- THE VO MODEL TEST ----- END -----")


# endregion


# region VOSatelliteModelHelper
class VOSatelliteModelHelper(object):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        Assert.assertIsNotNone(root)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits
        self._root: "StkObjectRoot" = root

    # endregion

    # region Run method
    def Run(self, oModel: "SatelliteGraphics3DModel"):
        self.m_logger.WriteLine("----- THE VO MODEL TEST ----- BEGIN -----")

        Assert.assertIsNotNone(oModel)

        # IsPointVisible (false)
        self.m_logger.WriteLine4("\tThe current IsPointVisible is: {0}", oModel.show_point)
        oModel.show_point = False
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.show_point)
        Assert.assertEqual(False, oModel.show_point)
        # PointSize
        with pytest.raises(Exception):
            oModel.point_size = 12.3456
        # IsPointVisible (true)
        oModel.show_point = True
        self.m_logger.WriteLine4("\tThe new IsPointVisible is: {0}", oModel.show_point)
        Assert.assertEqual(True, oModel.show_point)
        # PointSize
        self.m_logger.WriteLine6("\tThe current PointSize is: {0}", oModel.point_size)
        oModel.point_size = 12.3456
        self.m_logger.WriteLine6("\tThe new PointSize is: {0}", oModel.point_size)
        Assert.assertAlmostEqual(12.3456, float(oModel.point_size), delta=0.0001)
        with pytest.raises(Exception):
            oModel.point_size = 123.456

        # GLTF

        (clr.CastAs(oModel.model_data, Graphics3DModelFile)).filename = Path.Combine(
            TestBase.ModelDirectory, "scaling_sphere.mdl"
        )  # need a model that does not support GLTF settings
        with pytest.raises(Exception, match=RegexSubstringMatch("glTF settings are not available")):
            oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT
        (
            clr.CastAs(oModel.model_data, Graphics3DModelFile)
        ).filename = r"STKData\VO\Models\Land\facility.glb"  # need a model that supports GLTF settings
        oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT
        Assert.assertEqual(MODEL_GLTF_REFLECTION_MAP_TYPE.PROCEDURAL_ENVIRONMENT, oModel.gltf_reflection_map_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not set to Image Based")):
            x: "Graphics3DModelglTFImageBased" = oModel.gltf_image_based

        oModel.gltf_reflection_map_type = MODEL_GLTF_REFLECTION_MAP_TYPE.IMAGE_BASED
        Assert.assertEqual(MODEL_GLTF_REFLECTION_MAP_TYPE.IMAGE_BASED, oModel.gltf_reflection_map_type)

        gltfImageBased: "Graphics3DModelglTFImageBased" = oModel.gltf_image_based
        gltfImageBased.filename = TestBase.GetScenarioFile("over_the_clouds.hdr")
        Assert.assertEqual("over_the_clouds.hdr", gltfImageBased.filename)
        Assert.assertTrue(("over_the_clouds.hdr" in gltfImageBased.file_path))

        gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 ICRF"
        Assert.assertEqual("Satellite/Satellite1 ICRF", gltfImageBased.reflection_reference_frame)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            gltfImageBased.reflection_reference_frame = "Satellite/Satellite1 Bogus"

        # Base class properties test
        oModelHelper = VOModelHelper(self._root, self.m_oUnits)
        oModelHelper.Run(oModel)

        # OrbitMarker test
        oMarkerHelper = VOMarkerHelper(self.m_oUnits)
        oMarkerHelper.Run(oModel.orbit_marker, True)

        # GroundMarker test
        oMarkerHelper.Run(oModel.ground_marker, True)

        # SolarPanelPointAtSun test
        self.m_logger.WriteLine4("The current SolarPanelsPointAtSun flag is: {0}", oModel.solar_panels_point_at_sun)
        oModel.solar_panels_point_at_sun = False
        self.m_logger.WriteLine4("The new SolarPanelsPointAtSun flag is: {0}", oModel.solar_panels_point_at_sun)
        Assert.assertEqual(False, oModel.solar_panels_point_at_sun)
        oModel.solar_panels_point_at_sun = True
        self.m_logger.WriteLine4("The new SolarPanelsPointAtSun flag is: {0}", oModel.solar_panels_point_at_sun)
        Assert.assertEqual(True, oModel.solar_panels_point_at_sun)

        self.m_logger.WriteLine("----- THE VO MODEL TEST ----- END -----")


# endregion


# region VOModelPointingHelper
class VOModelPointingHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oModelPointing: "Graphics3DModelPointing"):
        self.m_logger.WriteLine("----- THE VO MODEL POINTING TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oModelPointing)
        # PointableElements
        oPECollection: "Graphics3DPointableElementsCollection" = oModelPointing.pointable_elements
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
            pointableElementsElement: "Graphics3DPointableElementsElement" = oPECollection[iIndex]
            Assert.assertIsNotNone(pointableElementsElement)
            self.m_logger.WriteLine7("\tElement {0} is: {1}", iIndex, pointableElementsElement.pointing_name)
            with pytest.raises(Exception):
                pointableElementsElement.pointing_name = "NewName"

            oHelper = LinkToObjectHelper()
            oHelper.Run(pointableElementsElement.assigned_target_object, pointableElementsElement.pointing_name)

            iIndex += 1

        # Add
        self.m_logger.WriteLine3("The Pointable Elements collection still contains: {0} elements", oPECollection.count)

        iIndex: int = 0
        while iIndex < oPECollection.count:
            self.m_logger.WriteLine5("\tElement: {0}", oPECollection[iIndex].pointing_name)

            iIndex += 1

        with pytest.raises(Exception):
            oNewElement: "Graphics3DPointableElementsElement" = oPECollection.add()
        # RemoveAt
        with pytest.raises(Exception):
            oPECollection.remove_at(0)
        # RemoveAll
        with pytest.raises(Exception):
            oPECollection.remove_all()
        self.m_logger.WriteLine3("The Pointable Elements collection still contains: {0} elements", oPECollection.count)
        oTempElement: "Graphics3DPointableElementsElement"
        for oTempElement in oPECollection:
            self.m_logger.WriteLine5("\tElement: {0}", oTempElement.pointing_name)

        # Testing model pointing intervals
        Assert.assertTrue((oPECollection.count > 0))
        oTempElement: "Graphics3DPointableElementsElement"
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
        oTempElement: "Graphics3DPointableElementsElement"

        # Verify that we can add intervals to existing pointable elements
        for oTempElement in oPECollection:
            # need to use a full path
            self.m_logger.WriteLine(oTempElement.pointing_name)
            oTempElement.assigned_target_object.bind_to_object(sPlanetTargetObject)
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
            with pytest.raises(Exception):
                oTempElement.intervals.add("1 Jul 1999 03:00:000.00", "1 Jul 1999 01:00:000.00")

        # adding a Sun target
        iCount: int = oPECollection.count
        oModelPointing.add_interval(
            oPECollection[0].pointing_name, "Sun", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
        )
        Assert.assertEqual((iCount + 1), oPECollection.count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.count)
        oTempElement: "Graphics3DPointableElementsElement"
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.pointing_name)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.assigned_target_object.name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.intervals.count)
            self.PrintIntervals(oTempElement.intervals)

        with pytest.raises(Exception):
            oModelPointing.add_interval(
                "WrongPointingName", "Sun", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
            )
        with pytest.raises(Exception):
            oModelPointing.add_interval(
                oPECollection[2].pointing_name, "WrongTargetName", "1 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
            )
        with pytest.raises(Exception):
            oModelPointing.add_interval(
                oPECollection[2].pointing_name, "Earth", "3 Jul 1999 13:00:000.00", "2 Jul 1999 00:00:000.00"
            )

        # adding a Slew Interval target
        iCount = oPECollection.count
        oModelPointing.add_interval(
            oPECollection[1].pointing_name, "Slew", "1 Jul 1999 02:00:000.00", "1 Jul 1999 03:00:000.00"
        )
        Assert.assertEqual((iCount + 1), oPECollection.count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.count)
        oTempElement: "Graphics3DPointableElementsElement"
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.pointing_name)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.assigned_target_object.name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.intervals.count)
            self.PrintIntervals(oTempElement.intervals)

        # RemoveInterval
        oModelPointing.remove_interval(oPECollection[1].pointing_name, "Slew")
        Assert.assertEqual(iCount, oPECollection.count)
        self.m_logger.WriteLine3("The new PointebleElements collection contains: {0} elements", oPECollection.count)
        oTempElement: "Graphics3DPointableElementsElement"
        for oTempElement in oPECollection:
            self.m_logger.WriteLine(oTempElement.pointing_name)
            self.m_logger.WriteLine5("\tTargetObject: {0}", oTempElement.assigned_target_object.name)
            self.m_logger.WriteLine3("\t\tThe new number of intervals: {0}", oTempElement.intervals.count)
            self.PrintIntervals(oTempElement.intervals)

        with pytest.raises(Exception):
            oModelPointing.remove_interval("WrongPointingName", "Sun")
        with pytest.raises(Exception):
            oModelPointing.remove_interval(oPECollection[2].pointing_name, "WrongTargetName")
        with pytest.raises(Exception):
            oModelPointing.remove_interval(oPECollection[1].pointing_name, "Earth")

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

        with pytest.raises(Exception):
            oModelPointing.load_intervals(
                TestBase.GetScenarioFile("MdlPtgIntsBad.int"), oModelPointing.pointable_elements[0].pointing_name
            )

        self.m_logger.WriteLine("----- THE VO MODEL POINTING TEST ----- END -----")

    # endregion

    # region PrintIntervals method
    def PrintIntervals(self, oCollection: "TimeIntervalCollection"):
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
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oOffset: "Graphics3DOffset"):
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
        oAHelper.Run(oOffset.attachment_point)

        self.m_logger.WriteLine("----- THE VO OFFSET TEST ----- END -----")


# endregion


# region VOOffsetRotationalHelper
class VOOffsetRotationalHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oRotational: "Graphics3DOffsetRotate"):
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
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oTranslational: "Graphics3DOffsetTransformation"):
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
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oLabel: "Graphics3DOffsetLabel", bReadOnly: bool):
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
            # Enable
            with pytest.raises(Exception):
                oLabel.enable = False
            # OffsetFrame
            with pytest.raises(Exception):
                oLabel.offset_frame = OFFSET_FRAME_TYPE.CARTESIAN
            # X
            with pytest.raises(Exception):
                oLabel.x = 10.1
            # Y
            with pytest.raises(Exception):
                oLabel.y = 11.11
            # Z
            with pytest.raises(Exception):
                oLabel.z = 12.12

        else:
            # Enable (false)
            self.m_logger.WriteLine4("\t\tThe current Enable is: {0}", oLabel.enable)
            oLabel.enable = False
            self.m_logger.WriteLine4("\t\tThe new Enable is: {0}", oLabel.enable)
            Assert.assertEqual(False, oLabel.enable)
            # OffsetFrame
            with pytest.raises(Exception):
                oLabel.offset_frame = OFFSET_FRAME_TYPE.CARTESIAN
            # X
            with pytest.raises(Exception):
                oLabel.x = 10.1
            # Y
            with pytest.raises(Exception):
                oLabel.y = 11.11
            # Z
            with pytest.raises(Exception):
                oLabel.z = 12.12
            # Enable (true)
            oLabel.enable = True
            self.m_logger.WriteLine4("\t\tThe new Enable is: {0}", oLabel.enable)
            Assert.assertEqual(True, oLabel.enable)
            # OffsetFrame (Cartesian)
            self.m_logger.WriteLine6("\t\t\tThe current OffsetFrame is: {0}", oLabel.offset_frame)
            oLabel.offset_frame = OFFSET_FRAME_TYPE.CARTESIAN
            self.m_logger.WriteLine6("\t\t\tThe new OffsetFrame is: {0}", oLabel.offset_frame)
            Assert.assertEqual(OFFSET_FRAME_TYPE.CARTESIAN, oLabel.offset_frame)
            # X
            self.m_logger.WriteLine6("\t\t\t\tThe current X is: {0}", oLabel.x)
            oLabel.x = 10.1
            self.m_logger.WriteLine6("\t\t\t\tThe new X is: {0}", oLabel.x)
            Assert.assertAlmostEqual(10.1, oLabel.x, delta=0.01)
            with pytest.raises(Exception):
                oLabel.x = 12340000000000000000000.0
            # Y
            self.m_logger.WriteLine6("\t\t\t\tThe current Y is: {0}", oLabel.y)
            oLabel.y = 11.11
            self.m_logger.WriteLine6("\t\t\t\tThe new Y is: {0}", oLabel.y)
            Assert.assertAlmostEqual(11.11, oLabel.y, delta=0.001)
            with pytest.raises(Exception):
                oLabel.y = -34120000000000.0
            # Z
            self.m_logger.WriteLine6("\t\t\t\tThe current Z is: {0}", oLabel.z)
            oLabel.z = 12.12
            self.m_logger.WriteLine6("\t\t\t\tThe new Z is: {0}", oLabel.z)
            Assert.assertAlmostEqual(12.12, oLabel.z, delta=0.001)
            with pytest.raises(Exception):
                oLabel.z = 210900000000000000000000000000000000.0
            # OffsetFrame (Pixel)
            oLabel.offset_frame = OFFSET_FRAME_TYPE.PIXEL
            self.m_logger.WriteLine6("\t\t\tThe new OffsetFrame is: {0}", oLabel.offset_frame)
            Assert.assertEqual(OFFSET_FRAME_TYPE.PIXEL, oLabel.offset_frame)
            # X
            self.m_logger.WriteLine6("\t\t\t\tThe current X is: {0}", oLabel.x)
            oLabel.x = 13.13
            self.m_logger.WriteLine6("\t\t\t\tThe new X is: {0}", oLabel.x)
            Assert.assertAlmostEqual(13.13, oLabel.x, delta=0.001)
            with pytest.raises(Exception):
                oLabel.x = 12340000000000000000000.0
            # Y
            self.m_logger.WriteLine6("\t\t\t\tThe current Y is: {0}", oLabel.y)
            oLabel.y = 14.14
            self.m_logger.WriteLine6("\t\t\t\tThe new Y is: {0}", oLabel.y)
            Assert.assertAlmostEqual(14.14, oLabel.y, delta=0.001)
            with pytest.raises(Exception):
                oLabel.y = -34120000000000.0
            # Z
            with pytest.raises(Exception):
                oLabel.z = 15.15

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
    def Run(self, oAttach: "Graphics3DOffsetAttachment"):
        Assert.assertIsNotNone(oAttach)
        self.m_logger.WriteLine("Offsets Attach Points test:")
        # AvailableAttachPoints
        arPoints = oAttach.available_attachment_points
        # Enable (false)
        self.m_logger.WriteLine4("\tThe current Enable flag is: {0}", oAttach.enable)
        oAttach.enable = False
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oAttach.enable)
        Assert.assertEqual(False, oAttach.enable)
        if Array.Length(arPoints) > 0:
            with pytest.raises(Exception):
                oAttach.attachment_point_name = str(arPoints[0])

        # Enable (true)
        oAttach.enable = True
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oAttach.enable)
        Assert.assertEqual(True, oAttach.enable)
        # AttachPtName
        self.m_logger.WriteLine5("\tThe current AttachPtName is: {0}", oAttach.attachment_point_name)
        self.m_logger.WriteLine3("\tThe AvailableAttachPoints array contains: {0} elements.", Array.Length(arPoints))
        if Array.Length(arPoints) > 0:
            strName: str = str(arPoints[0])
            self.m_logger.WriteLine5("\t\tElement: {0}", strName)
            oAttach.attachment_point_name = strName
            self.m_logger.WriteLine5("\t\t\tThe new AttachPtName is: {0}", oAttach.attachment_point_name)
            Assert.assertEqual(strName, oAttach.attachment_point_name)

        with pytest.raises(Exception):
            oAttach.attachment_point_name = "InvalidName"


# endregion


# region VOProximityHelper
class VOProximityHelper(object):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_root: "StkObjectRoot" = root
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Proximity Area Object
    def TestProximityAreObjectBase(self, oAreaObject: "IVehicleGraphics3DProximityAreaObject"):
        self.m_logger.WriteLine("IVehicleGraphics3DProximityAreaObject test:")
        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oAreaObject.show_graphics)
        oAreaObject.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oAreaObject.show_graphics)
        Assert.assertEqual(False, oAreaObject.show_graphics)
        # Color (readonly)
        with pytest.raises(Exception):
            oAreaObject.color = Colors.from_argb(12414)
        # IsLabelVisible (readonly)
        with pytest.raises(Exception):
            oAreaObject.show_label = True
        # IsTextVisible (readonly)
        with pytest.raises(Exception):
            oAreaObject.show_text = True
        # LineStyle (readonly)
        with pytest.raises(Exception):
            oAreaObject.line_style = LINE_STYLE.DASHED
        # LineWidth (readonly)
        with pytest.raises(Exception):
            oAreaObject.line_width = LINE_WIDTH.WIDTH2
        # Text (readonly)
        with pytest.raises(Exception):
            oAreaObject.text = "Area Of Uncertainty"
        # IsVisible (true)
        oAreaObject.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oAreaObject.show_graphics)
        Assert.assertEqual(True, oAreaObject.show_graphics)
        # Color
        color: Color = Colors.Red
        self.m_logger.WriteLine6("\tThe current Color is: {0}", oAreaObject.color)
        oAreaObject.color = color
        self.m_logger.WriteLine6("\tThe new Color is: {0}", oAreaObject.color)
        AssertEx.AreEqual(color, oAreaObject.color)
        # IsLabelVisible
        self.m_logger.WriteLine4("\tThe current IsLabelVisible flag is: {0}", oAreaObject.show_label)
        oAreaObject.show_label = False
        self.m_logger.WriteLine4("\tThe new IsLabelVisible flag is: {0}", oAreaObject.show_label)
        Assert.assertEqual(False, oAreaObject.show_label)
        oAreaObject.show_label = True
        self.m_logger.WriteLine4("\tThe new IsLabelVisible flag is: {0}", oAreaObject.show_label)
        Assert.assertEqual(True, oAreaObject.show_label)
        # Text
        self.m_logger.WriteLine5("\tThe current Text is: {0}", oAreaObject.text)
        oAreaObject.text = "Test Message"
        self.m_logger.WriteLine5("\tThe new Text is: {0}", oAreaObject.text)
        Assert.assertEqual("Test Message", oAreaObject.text)
        oAreaObject.text = ""
        self.m_logger.WriteLine5("\tThe new Text is: {0}", oAreaObject.text)
        Assert.assertEqual("", oAreaObject.text)
        # IsTextVisible
        self.m_logger.WriteLine4("\tThe current IsTextVisible flag is: {0}", oAreaObject.show_text)
        oAreaObject.show_text = False
        self.m_logger.WriteLine4("\tThe new IsTextVisible flag is: {0}", oAreaObject.show_text)
        Assert.assertEqual(False, oAreaObject.show_text)
        oAreaObject.show_text = True
        self.m_logger.WriteLine4("\tThe new IsTextVisible flag is: {0}", oAreaObject.show_text)
        Assert.assertEqual(True, oAreaObject.show_text)
        # LineStyle
        self.m_logger.WriteLine6("\tThe current LineStyle is: {0}", oAreaObject.line_style)
        oAreaObject.line_style = LINE_STYLE.DASHED
        self.m_logger.WriteLine6("\tThe new LineStyle is: {0}", oAreaObject.line_style)
        Assert.assertEqual(LINE_STYLE.DASHED, oAreaObject.line_style)
        # LineWidth
        self.m_logger.WriteLine6("\tThe current LineWidth is: {0}", oAreaObject.line_width)
        oAreaObject.line_width = LINE_WIDTH.WIDTH2
        self.m_logger.WriteLine6("\tThe new LineWidth is: {0}", oAreaObject.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH2, oAreaObject.line_width)

    # endregion

    # region ControlBox
    def TestControlBox(self, oBox: "VehicleGraphics3DControlBox"):
        self.TestProximityAreObjectBase(oBox)

        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_oUnits.set_current_unit("DistanceUnit", "m")

        oBox.show_graphics = False
        Assert.assertEqual(False, oBox.show_graphics)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oBox.x_axis_length = 124
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oBox.x_offset = 124
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oBox.y_axis_length = 124
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oBox.y_offset = 124
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oBox.z_axis_length = 124
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oBox.z_offset = 124

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBox.use_translucency = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBox.translucency = 0.8

        oBox.show_graphics = True
        Assert.assertEqual(True, oBox.show_graphics)

        oBox.x_axis_length = 10000
        Assert.assertEqual(10000, oBox.x_axis_length)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oBox.x_axis_length = -123.456
        oBox.x_offset = 1000
        Assert.assertEqual(1000, oBox.x_offset)

        oBox.y_axis_length = 20000
        Assert.assertEqual(20000, oBox.y_axis_length)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oBox.y_axis_length = -123.456
        oBox.y_offset = 2000
        Assert.assertEqual(2000, oBox.y_offset)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oBox.y_offset = -123.456

        oBox.z_axis_length = 30000
        Assert.assertEqual(30000, oBox.z_axis_length)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oBox.z_axis_length = -123.456
        oBox.z_offset = 3000
        Assert.assertEqual(3000, oBox.z_offset)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oBox.z_offset = -123.456

        oBox.use_translucency = False
        Assert.assertEqual(False, oBox.use_translucency)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oBox.translucency = 12.3456
        oBox.use_translucency = True
        Assert.assertEqual(True, oBox.use_translucency)
        oBox.translucency = 50.0
        Assert.assertAlmostEqual(50.0, oBox.translucency, delta=1e-05)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
            oBox.translucency = 123.456

        newAxes: "IVectorGeometryToolAxes" = self.m_root.analysis_workbench_components_root.get_provider(
            "Satellite/Satellite1"
        ).axes[0]
        oBox.reference_frame = newAxes
        Assert.assertEqual(
            (clr.CastAs(newAxes, IAnalysisWorkbenchComponent)).name,
            (clr.CastAs(oBox.reference_frame, IAnalysisWorkbenchComponent)).name,
        )
        # ENG113854
        with pytest.raises(Exception):
            oBox.reference_frame = None
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)

    # endregion

    # region BearingBox
    def TestBearingBox(self, oBox: "VehicleGraphics3DBearingBox"):
        # base properties test
        self.TestProximityAreObjectBase(oBox)

        self.m_logger.WriteLine("VehicleGraphics3DBearingBox test:")
        # set DistanceUnit
        strDistanceUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "mi")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("mi", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # set AngleUnit
        strAngleUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit is: {0}", strAngleUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oBox.show_graphics)
        oBox.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBox.show_graphics)
        Assert.assertEqual(False, oBox.show_graphics)
        # Bearing (readonly)
        with pytest.raises(Exception):
            oBox.bearing = 1234.56789
        # Length (readonly)
        with pytest.raises(Exception):
            oBox.length = 1234.56789
        # Width (readonly)
        with pytest.raises(Exception):
            oBox.width = 1234.56789
        # Height (readonly)
        with pytest.raises(Exception):
            oBox.height = 1234.56789
        # LengthOffset (readonly)
        with pytest.raises(Exception):
            oBox.length_offset = 1234.56789
        # WidthOffset (readonly)
        with pytest.raises(Exception):
            oBox.width_offset = 1234.56789
        # HeightOffset (readonly)
        with pytest.raises(Exception):
            oBox.height_offset = 1234.56789
        # UseTranslucency
        with pytest.raises(Exception):
            oBox.use_translucency = True
        # Translucency
        with pytest.raises(Exception):
            oBox.translucency = 0.56789
        # IsVisible (true)
        oBox.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBox.show_graphics)
        Assert.assertEqual(True, oBox.show_graphics)
        # Bearing
        self.m_logger.WriteLine6("\tThe current Bearing is: {0}", oBox.bearing)
        oBox.bearing = 50000
        self.m_logger.WriteLine6("\tThe new Bearing is: {0}", oBox.bearing)
        Assert.assertEqual(50000, oBox.bearing)
        # Length
        self.m_logger.WriteLine6("\tThe current Length is: {0}", oBox.length)
        oBox.length = 120000
        self.m_logger.WriteLine6("\tThe new Length is: {0}", oBox.length)
        Assert.assertEqual(120000, oBox.length)
        with pytest.raises(Exception):
            oBox.length = -123.456
        # Width
        self.m_logger.WriteLine6("\tThe current Width is: {0}", oBox.width)
        oBox.width = 130000
        self.m_logger.WriteLine6("\tThe new Width is: {0}", oBox.width)
        Assert.assertEqual(130000, oBox.width)
        with pytest.raises(Exception):
            oBox.width = -123.456
        # Height
        self.m_logger.WriteLine6("\tThe current Height is: {0}", oBox.height)
        oBox.height = 100000
        self.m_logger.WriteLine6("\tThe new Height is: {0}", oBox.height)
        Assert.assertEqual(100000, oBox.height)
        with pytest.raises(Exception):
            oBox.height = -123.456
        # HeightOffset
        self.m_logger.WriteLine6("\tThe current HeightOffset is: {0}", oBox.height_offset)
        oBox.height_offset = 2000
        self.m_logger.WriteLine6("\tThe new HeightOffset is: {0}", oBox.height_offset)
        Assert.assertEqual(2000, oBox.height_offset)
        with pytest.raises(Exception):
            oBox.height_offset = -123.456
        # LengthOffset
        self.m_logger.WriteLine6("\tThe current LengthOffset is: {0}", oBox.length_offset)
        oBox.length_offset = 3000
        self.m_logger.WriteLine6("\tThe new LengthOffset is: {0}", oBox.length_offset)
        Assert.assertEqual(3000, oBox.length_offset)
        # WidthOffset
        self.m_logger.WriteLine6("\tThe current WidthOffset is: {0}", oBox.width_offset)
        oBox.width_offset = 4000
        self.m_logger.WriteLine6("\tThe new WidthOffset is: {0}", oBox.width_offset)
        Assert.assertEqual(4000, oBox.width_offset)
        with pytest.raises(Exception):
            oBox.width_offset = -123.456
        # UseTranslucency
        self.m_logger.WriteLine4("\tThe current UseTranslucency flag is: {0}", oBox.use_translucency)
        oBox.use_translucency = False
        self.m_logger.WriteLine4("\tThe new UseTranslucency flag is: {0}", oBox.use_translucency)
        Assert.assertEqual(False, oBox.use_translucency)
        with pytest.raises(Exception):
            oBox.translucency = 12.3456
        oBox.use_translucency = True
        self.m_logger.WriteLine4("\tThe new UseTranslucency flag is: {0}", oBox.use_translucency)
        Assert.assertEqual(True, oBox.use_translucency)
        # Translucency
        self.m_logger.WriteLine6("\tThe current Translucency is: {0}", oBox.translucency)
        oBox.translucency = 30.5
        self.m_logger.WriteLine6("\tThe new Translucency is: {0}", oBox.translucency)
        Assert.assertAlmostEqual(30.5, oBox.translucency, delta=1e-05)
        with pytest.raises(Exception):
            oBox.translucency = 123.456
        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strAngleUnit)
        self.m_logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strAngleUnit)
        Assert.assertEqual(strAngleUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region BearingEllipse
    def TestBearingEllipse(self, oBox: "VehicleGraphics3DBearingEllipse"):
        # base properties test
        self.TestProximityAreObjectBase(oBox)

        self.m_logger.WriteLine("VehicleGraphics3DBearingEllipse test:")
        # set DistanceUnit
        strDistanceUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "mi")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("mi", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # set AngleUnit
        strAngleUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit is: {0}", strAngleUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oBox.show_graphics)
        oBox.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBox.show_graphics)
        Assert.assertEqual(False, oBox.show_graphics)
        # Bearing (readonly)
        with pytest.raises(Exception):
            oBox.bearing = 1234.56789
        # MajorAxis (readonly)
        with pytest.raises(Exception):
            oBox.semi_major_axis = 1234.56789
        # MinorAxis (readonly)
        with pytest.raises(Exception):
            oBox.semi_minor_axis = 1234.56789
        # Granularity (readonly)
        with pytest.raises(Exception):
            oBox.granularity = 1234.56789
        # MajorAxisOffset (readonly)
        with pytest.raises(Exception):
            oBox.major_axis_offset = 1234.56789
        # MinorAxisOffset (readonly)
        with pytest.raises(Exception):
            oBox.minor_axis_offset = 1234.56789
        # IsVisible (true)
        oBox.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBox.show_graphics)
        Assert.assertEqual(True, oBox.show_graphics)
        # Bearing
        self.m_logger.WriteLine6("\tThe current Bearing is: {0}", oBox.bearing)
        oBox.bearing = 50000
        self.m_logger.WriteLine6("\tThe new Bearing is: {0}", oBox.bearing)
        Assert.assertEqual(50000, oBox.bearing)
        # MajorAxis
        self.m_logger.WriteLine6("\tThe current MajorAxis is: {0}", oBox.semi_major_axis)
        oBox.semi_major_axis = 120000
        self.m_logger.WriteLine6("\tThe new MajorAxis is: {0}", oBox.semi_major_axis)
        Assert.assertEqual(120000, oBox.semi_major_axis)
        with pytest.raises(Exception):
            oBox.semi_major_axis = -123.456
        # MinorAxis
        self.m_logger.WriteLine6("\tThe current MinorAxis is: {0}", oBox.semi_minor_axis)
        oBox.semi_minor_axis = 130000
        self.m_logger.WriteLine6("\tThe new MinorAxis is: {0}", oBox.semi_minor_axis)
        Assert.assertEqual(130000, oBox.semi_minor_axis)
        with pytest.raises(Exception):
            oBox.semi_minor_axis = -123.456
        # Granularity
        self.m_logger.WriteLine6("\tThe current Granularity is: {0}", oBox.granularity)
        oBox.granularity = 0.54321
        self.m_logger.WriteLine6("\tThe new Granularity is: {0}", oBox.granularity)
        Assert.assertAlmostEqual(0.54321, oBox.granularity, delta=1e-05)
        # MajorAxisOffset
        self.m_logger.WriteLine6("\tThe current MajorAxisOffset is: {0}", oBox.major_axis_offset)
        oBox.major_axis_offset = 2000
        self.m_logger.WriteLine6("\tThe new MajorAxisOffset is: {0}", oBox.major_axis_offset)
        Assert.assertEqual(2000, oBox.major_axis_offset)
        # MinorAxisOffset
        self.m_logger.WriteLine6("\tThe current MinorAxisOffset is: {0}", oBox.minor_axis_offset)
        oBox.minor_axis_offset = 3000
        self.m_logger.WriteLine6("\tThe new MinorAxisOffset is: {0}", oBox.minor_axis_offset)
        Assert.assertEqual(3000, oBox.minor_axis_offset)
        with pytest.raises(Exception):
            oBox.minor_axis_offset = -123.456
        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strAngleUnit)
        self.m_logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strAngleUnit)
        Assert.assertEqual(strAngleUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region LineOfBearing
    def TestLineOfBearing(self, oBox: "VehicleGraphics3DLineOfBearing"):
        # base properties test
        self.TestProximityAreObjectBase(oBox)

        self.m_logger.WriteLine("VehicleGraphics3DLineOfBearing test:")
        # set DistanceUnit
        strDistanceUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "mi")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("mi", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # set AngleUnit
        strAngleUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit is: {0}", strAngleUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oBox.show_graphics)
        oBox.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBox.show_graphics)
        Assert.assertEqual(False, oBox.show_graphics)
        # Bearing (readonly)
        with pytest.raises(Exception):
            oBox.bearing = 1234.56789
        # OriginLatitude (readonly)
        with pytest.raises(Exception):
            oBox.origin_latitude = 123.456789
        # OriginLongitude (readonly)
        with pytest.raises(Exception):
            oBox.origin_longitude = 123.456789
        # OriginAltitude (readonly)
        with pytest.raises(Exception):
            oBox.origin_altitude = 123.456789
        # Length (readonly)
        with pytest.raises(Exception):
            oBox.length = 123.456789
        # BearingError (readonly)
        with pytest.raises(Exception):
            oBox.bearing_error = 123.456789
        # ErrorColor (readonly)
        with pytest.raises(Exception):
            oBox.error_color = Colors.from_argb(9991764)
        # ErrorLineWidth (readonly)
        with pytest.raises(Exception):
            oBox.error_line_width = LINE_WIDTH.WIDTH5
        # IsVisible (true)
        oBox.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oBox.show_graphics)
        Assert.assertEqual(True, oBox.show_graphics)
        # Bearing
        self.m_logger.WriteLine6("\tThe current Bearing is: {0}", oBox.bearing)
        oBox.bearing = 50000
        self.m_logger.WriteLine6("\tThe new Bearing is: {0}", oBox.bearing)
        Assert.assertEqual(50000, oBox.bearing)
        # OriginLatitude
        self.m_logger.WriteLine6("\tThe current OriginLatitude is: {0}", oBox.origin_latitude)
        oBox.origin_latitude = 1.234
        self.m_logger.WriteLine6("\tThe new OriginLatitude is: {0}", oBox.origin_latitude)
        Assert.assertEqual(1.234, oBox.origin_latitude)
        with pytest.raises(Exception):
            oBox.origin_latitude = -91
        # OriginLongitude
        self.m_logger.WriteLine6("\tThe current OriginLongitude is: {0}", oBox.origin_longitude)
        oBox.origin_longitude = 3.45
        self.m_logger.WriteLine6("\tThe new OriginLongitude is: {0}", oBox.origin_longitude)
        Assert.assertEqual(3.45, oBox.origin_longitude)
        with pytest.raises(Exception):
            oBox.origin_longitude = -361
        # OriginAltitude
        self.m_logger.WriteLine6("\tThe current OriginAltitude is: {0}", oBox.origin_altitude)
        oBox.origin_altitude = 54321.0
        self.m_logger.WriteLine6("\tThe new OriginAltitude is: {0}", oBox.origin_altitude)
        Assert.assertAlmostEqual(54321.0, oBox.origin_altitude, delta=0.01)
        # Length
        self.m_logger.WriteLine6("\tThe current Length is: {0}", oBox.length)
        oBox.length = 2000
        self.m_logger.WriteLine6("\tThe new Length is: {0}", oBox.length)
        Assert.assertEqual(2000, oBox.length)
        with pytest.raises(Exception):
            oBox.length = -123456.789
        # BearingError
        self.m_logger.WriteLine6("\tThe current BearingError is: {0}", oBox.bearing_error)
        oBox.bearing_error = 2.345
        self.m_logger.WriteLine6("\tThe new BearingError is: {0}", oBox.bearing_error)
        Assert.assertAlmostEqual(2.345, oBox.bearing_error, delta=0.0001)
        with pytest.raises(Exception):
            oBox.bearing_error = -1
        # ErrorColor
        self.m_logger.WriteLine6("\tThe current ErrorColor is: {0}", oBox.error_color)
        oBox.error_color = Colors.from_argb(11259375)
        self.m_logger.WriteLine6("\tThe new ErrorColor is: {0}", oBox.error_color)
        AssertEx.AreEqual(Colors.from_argb(11259375), oBox.error_color)
        # ErrorLineWidth
        self.m_logger.WriteLine6("\tThe current ErrorLineWidth is: {0}", oBox.error_line_width)
        oBox.error_line_width = LINE_WIDTH.WIDTH4
        self.m_logger.WriteLine6("\tThe new ErrorLineWidth is: {0}", oBox.error_line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH4, oBox.error_line_width)
        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strAngleUnit)
        self.m_logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strAngleUnit)
        Assert.assertEqual(strAngleUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region AOULabelSwapDistance
    def TestAOULabelSwapDistance(self, oSwapDist: "Graphics3DLabelSwapDistance"):
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(oSwapDist)


# endregion


# region VOOrbitProximityHelper
class VOOrbitProximityHelper(VOProximityHelper):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        super(VOOrbitProximityHelper, self).__init__(root, oUnits)

    # endregion

    # region GeoBox method
    def GeoBox(self, oGeoBox: "VehicleGraphics3DGeoBox"):
        # Hold original values
        holdLongitude: float = oGeoBox.longitude
        holdNorthSouth: float = oGeoBox.north_south
        holdEastWest: float = oGeoBox.east_west
        holdRadius: float = oGeoBox.radius
        holdColor: Color = oGeoBox.color

        oGeoBox.show_graphics = False
        Assert.assertFalse(oGeoBox.show_graphics)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oGeoBox.longitude = 10
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oGeoBox.north_south = 10
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oGeoBox.east_west = 10
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oGeoBox.radius = 10
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oGeoBox.color = Colors.Red
        # BUG STK-77 TryCatchAssertBlock.ExpectedException("read only", delegate () { oGeoBox.Reposition(); });

        oGeoBox.show_graphics = True
        Assert.assertTrue(oGeoBox.show_graphics)

        oGeoBox.longitude = -360
        Assert.assertEqual(-360, oGeoBox.longitude)
        oGeoBox.longitude = 360
        Assert.assertEqual(360, oGeoBox.longitude)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oGeoBox.longitude = -361
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oGeoBox.longitude = 361

        oGeoBox.north_south = 0
        Assert.assertEqual(0, oGeoBox.north_south)
        oGeoBox.north_south = 45
        Assert.assertEqual(45, oGeoBox.north_south)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oGeoBox.north_south = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oGeoBox.north_south = 46

        oGeoBox.east_west = 0
        Assert.assertEqual(0, oGeoBox.east_west)
        oGeoBox.east_west = 45
        Assert.assertEqual(45, oGeoBox.east_west)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oGeoBox.east_west = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oGeoBox.east_west = 46

        oGeoBox.radius = 0.001
        Assert.assertEqual(0.001, oGeoBox.radius)
        oGeoBox.radius = 10000000000.0
        Assert.assertEqual(10000000000.0, oGeoBox.radius)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oGeoBox.radius = 0

        oGeoBox.color = Colors.Blue
        Assert.assertEqual(Colors.Blue, oGeoBox.color)

        # BUG STK-77 - Need support for "Use animation time" checkbox, and different "Recenter..." buttons.

        oGeoBox.reposition()

        # Restore original values
        oGeoBox.longitude = holdLongitude
        oGeoBox.north_south = holdNorthSouth
        oGeoBox.east_west = holdEastWest
        oGeoBox.radius = holdRadius
        oGeoBox.color = holdColor

        oGeoBox.reposition()

    # endregion

    # region Run method
    def Run(self, oProximity: "VehicleGraphics3DOrbitProximity"):
        self.m_logger.WriteLine("----- THE VO PROXIMITY TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oProximity)

        # Geostationary Box test
        self.GeoBox(oProximity.geo_box)

        # ControlBox
        self.TestControlBox(oProximity.control_box)
        # BearingBox
        self.TestBearingBox(oProximity.bearing_box)
        # BearingEllipse
        self.TestBearingEllipse(oProximity.bearing_ellipse)
        # LineOfBearing
        self.TestLineOfBearing(oProximity.line_of_bearing)
        # AOULabelSwapDistance
        self.TestAOULabelSwapDistance(oProximity.uncertainty_area_label_swap_distance)

        self.m_logger.WriteLine("----- THE VO PROXIMITY TEST ----- END -----")


# endregion


# region VORouteProximityHelper
class VORouteProximityHelper(VOProximityHelper):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        super(VORouteProximityHelper, self).__init__(root, oUnits)

    # endregion

    # region Run method
    def Run(self, oProximity: "VehicleGraphics3DRouteProximity"):
        self.m_logger.WriteLine("----- THE VO PROXIMITY TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oProximity)

        # ControlBox
        self.TestControlBox(oProximity.control_box)
        # BearingBox
        self.TestBearingBox(oProximity.bearing_box)
        # BearingEllipse
        self.TestBearingEllipse(oProximity.bearing_ellipse)
        # LineOfBearing
        self.TestLineOfBearing(oProximity.line_of_bearing)
        # AOULabelSwapDistance
        self.TestAOULabelSwapDistance(oProximity.uncertainty_area_label_swap_distance)

        self.m_logger.WriteLine("----- THE VO PROXIMITY TEST ----- END -----")


# endregion


# region VOTrajectoryProximityHelper
class VOTrajectoryProximityHelper(VOProximityHelper):
    def __init__(self, root: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        super(VOTrajectoryProximityHelper, self).__init__(root, oUnits)

    # endregion

    # region Run method
    def Run(self, oProximity: "VehicleGraphics3DTrajectoryProximity"):
        self.m_logger.WriteLine("----- THE VO PROXIMITY TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oProximity)

        # ControlBox
        self.TestControlBox(oProximity.control_box)
        # BearingBox
        self.TestBearingBox(oProximity.bearing_box)
        # BearingEllipse
        self.TestBearingEllipse(oProximity.bearing_ellipse)
        # LineOfBearing
        self.TestLineOfBearing(oProximity.line_of_bearing)
        # AOULabelSwapDistance
        self.TestAOULabelSwapDistance(oProximity.uncertainty_area_label_swap_distance)

        self.m_logger.WriteLine("----- THE VO PROXIMITY TEST ----- END -----")


# endregion


# region VORangeContoursHelper
class VORangeContoursHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oContours: "Graphics3DRangeContours"):
        self.m_logger.WriteLine("----- THE VO RANGE CONTOURS TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oContours)
        # Visible
        self.m_logger.WriteLine4("\tThe current Visible flag is: {0}", oContours.show_graphics)
        oContours.show_graphics = False
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oContours.show_graphics)
        Assert.assertEqual(False, oContours.show_graphics)
        # TranslucentLines
        with pytest.raises(Exception):
            oContours.translucent_lines = False
        # PercentTranslucency
        with pytest.raises(Exception):
            oContours.percent_translucency = 34.56789

        # LabelSwapDistance
        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(oContours.label_swap_distance)

        # BorderWall (ReadOnly) test
        oHelper = VOBorderWallHelper(self.m_oUnits)
        oHelper.Run(oContours.border_wall, True)

        # Visible
        oContours.show_graphics = True
        self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", oContours.show_graphics)
        Assert.assertEqual(True, oContours.show_graphics)
        # TranslucentLines
        self.m_logger.WriteLine4("\t\tThe current TranslucentLines flag is: {0}", oContours.translucent_lines)
        oContours.translucent_lines = False
        self.m_logger.WriteLine4("\t\tThe new TranslucentLines flag is: {0}", oContours.translucent_lines)
        Assert.assertEqual(False, oContours.translucent_lines)
        # PercentTranslucency
        with pytest.raises(Exception):
            oContours.percent_translucency = 34.56789
        # TranslucentLines
        oContours.translucent_lines = True
        self.m_logger.WriteLine4("\t\tThe new TranslucentLines flag is: {0}", oContours.translucent_lines)
        Assert.assertEqual(True, oContours.translucent_lines)
        # PercentTranslucency
        self.m_logger.WriteLine6("\t\tThe current Percent Translucency is: {0}", oContours.percent_translucency)
        oContours.percent_translucency = 34.56789
        self.m_logger.WriteLine6("\t\tThe new Percent Translucency is: {0}", oContours.percent_translucency)
        Assert.assertEqual(34.56789, oContours.percent_translucency)
        # range test
        with pytest.raises(Exception):
            oContours.percent_translucency = 1234.56789

        # BorderWall (NotReadOnly) test
        oHelper.Run(oContours.border_wall, False)
        self.m_logger.WriteLine("----- THE VO RANGE CONTOURS TEST ----- END -----")


# endregion


# region VOBorderWallHelper
class VOBorderWallHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oWall: "Graphics3DBorderWall", bReadOnly: bool):
        Assert.assertIsNotNone(oWall)
        if bReadOnly:
            self.ReadOnly(oWall)

        else:
            self.NotReadOnly(oWall)

    # endregion

    # region ReadOnly method
    def ReadOnly(self, oWall: "Graphics3DBorderWall"):
        Assert.assertIsNotNone(oWall)
        self.m_logger.WriteLine("Border Wall (ReadOnly) test:")
        # UseBorderWall
        with pytest.raises(Exception):
            oWall.use_border_wall = False
        # UpperEdgeAltRef
        with pytest.raises(Exception):
            oWall.upper_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.MEAN_SEA_LEVEL
        # LowerEdgeAltRef
        with pytest.raises(Exception):
            oWall.lower_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.TERRAIN
        # UpperEdgeHeight
        with pytest.raises(Exception):
            oWall.upper_edge_height = 12.34
        # LowerEdgeHeight
        with pytest.raises(Exception):
            oWall.lower_edge_height = 34.12
        # UseWallTranslucency
        with pytest.raises(Exception):
            oWall.use_wall_translucency = False
        # UseLineTranslucency
        with pytest.raises(Exception):
            oWall.use_line_translucency = False
        # WallTranslucency
        with pytest.raises(Exception):
            oWall.wall_translucency = 34.56
        # LineTranslucency
        with pytest.raises(Exception):
            oWall.line_translucency = 56.34

    # endregion

    # region NotReadOnly method
    def NotReadOnly(self, oWall: "Graphics3DBorderWall"):
        Assert.assertIsNotNone(oWall)
        self.m_logger.WriteLine("Border Wall (NotReadOnly) test:")
        # UseBorderWall
        self.m_logger.WriteLine4("\tThe current UseBorderWall flag is: {0}", oWall.use_border_wall)
        oWall.use_border_wall = False
        self.m_logger.WriteLine4("\tThe new UseBorderWall flag is: {0}", oWall.use_border_wall)
        Assert.assertEqual(False, oWall.use_border_wall)
        # UpperEdgeAltRef
        with pytest.raises(Exception):
            oWall.upper_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.MEAN_SEA_LEVEL
        # LowerEdgeAltRef
        with pytest.raises(Exception):
            oWall.lower_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.TERRAIN
        # UpperEdgeHeight
        with pytest.raises(Exception):
            oWall.upper_edge_height = 12.34
        # LowerEdgeHeight
        with pytest.raises(Exception):
            oWall.lower_edge_height = 34.12
        # UseWallTranslucency
        with pytest.raises(Exception):
            oWall.use_wall_translucency = False
        # UseLineTranslucency
        with pytest.raises(Exception):
            oWall.use_line_translucency = False
        # WallTranslucency
        with pytest.raises(Exception):
            oWall.wall_translucency = 34.56
        # LineTranslucency
        with pytest.raises(Exception):
            oWall.line_translucency = 56.34
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
            "\tIsAltRefTypeSupported MEAN_SEA_LEVEL is: {0}",
            oWall.is_altitude_reference_type_supported(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.MEAN_SEA_LEVEL),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported OBJECT is: {0}",
            oWall.is_altitude_reference_type_supported(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.OBJECT),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported TERRAIN is: {0}",
            oWall.is_altitude_reference_type_supported(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.TERRAIN),
        )
        self.m_logger.WriteLine4(
            "\tIsAltRefTypeSupported WGS84 is: {0}",
            oWall.is_altitude_reference_type_supported(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.WGS84),
        )

        # UpperEdgeAltRef
        self.m_logger.WriteLine6("\t\tThe current UpperEdge is: {0}", oWall.upper_edge_altitude_reference)
        oWall.upper_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.MEAN_SEA_LEVEL
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.upper_edge_altitude_reference)
        Assert.assertEqual(
            BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.MEAN_SEA_LEVEL, oWall.upper_edge_altitude_reference
        )
        oWall.upper_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.OBJECT
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.upper_edge_altitude_reference)
        Assert.assertEqual(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.OBJECT, oWall.upper_edge_altitude_reference)
        oWall.upper_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.TERRAIN
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.upper_edge_altitude_reference)
        Assert.assertEqual(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.TERRAIN, oWall.upper_edge_altitude_reference)
        oWall.upper_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.WGS84
        self.m_logger.WriteLine6("\t\tThe new UpperEdge is: {0}", oWall.upper_edge_altitude_reference)
        Assert.assertEqual(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.WGS84, oWall.upper_edge_altitude_reference)
        # UpperEdgeHeight
        self.m_logger.WriteLine6("\t\tThe current UpperEdge Height is: {0}", oWall.upper_edge_height)
        oWall.upper_edge_height = 123.4567
        self.m_logger.WriteLine6("\t\tThe new UpperEdge Height is: {0}", oWall.upper_edge_height)
        Assert.assertEqual(123.4567, oWall.upper_edge_height)
        # UpperEdgeHeight
        with pytest.raises(Exception):
            oWall.upper_edge_height = -9876543210.1
        # LowerEdgeAltRef
        self.m_logger.WriteLine6("\t\tThe current LowerEdge is: {0}", oWall.lower_edge_altitude_reference)
        oWall.lower_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.MEAN_SEA_LEVEL
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.lower_edge_altitude_reference)
        Assert.assertEqual(
            BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.MEAN_SEA_LEVEL, oWall.lower_edge_altitude_reference
        )
        oWall.lower_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.OBJECT
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.lower_edge_altitude_reference)
        Assert.assertEqual(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.OBJECT, oWall.lower_edge_altitude_reference)
        oWall.lower_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.TERRAIN
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.lower_edge_altitude_reference)
        Assert.assertEqual(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.TERRAIN, oWall.lower_edge_altitude_reference)
        oWall.lower_edge_altitude_reference = BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.WGS84
        self.m_logger.WriteLine6("\t\tThe new LowerEdge is: {0}", oWall.lower_edge_altitude_reference)
        Assert.assertEqual(BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE.WGS84, oWall.lower_edge_altitude_reference)
        # LowerEdgeHeight
        self.m_logger.WriteLine6("\t\tThe current LowerEdge Height is: {0}", oWall.lower_edge_height)
        oWall.lower_edge_height = 123.4567
        self.m_logger.WriteLine6("\t\tThe new LowerEdge Height is: {0}", oWall.lower_edge_height)
        Assert.assertEqual(123.4567, oWall.lower_edge_height)
        # LowerEdgeHeight
        with pytest.raises(Exception):
            oWall.lower_edge_height = -9876543210.1
        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit (restored) is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # UseWallTranslucency
        self.m_logger.WriteLine4("\t\tThe current UseWallTranslucency flag is: {0}", oWall.use_wall_translucency)
        oWall.use_wall_translucency = False
        self.m_logger.WriteLine4("\t\tThe new UseWallTranslucency flag is: {0}", oWall.use_wall_translucency)
        Assert.assertEqual(False, oWall.use_wall_translucency)
        # WallTranslucency
        with pytest.raises(Exception):
            oWall.wall_translucency = 34.56
        # UseWallTranslucency
        oWall.use_wall_translucency = True
        self.m_logger.WriteLine4("\t\tThe new UseWallTranslucency flag is: {0}", oWall.use_wall_translucency)
        Assert.assertEqual(True, oWall.use_wall_translucency)
        # WallTranslucency
        self.m_logger.WriteLine6("\t\tThe current WallTranslucency is: {0}", oWall.wall_translucency)
        oWall.wall_translucency = 34.56
        self.m_logger.WriteLine6("\t\tThe new WallTranslucency is: {0}", oWall.wall_translucency)
        Assert.assertAlmostEqual(34.56, oWall.wall_translucency, delta=0.01)
        # WallTranslucency
        with pytest.raises(Exception):
            oWall.wall_translucency = 1234.56
        # UseLineTranslucency
        self.m_logger.WriteLine4("\t\tThe current UseLineTranslucency flag is: {0}", oWall.use_line_translucency)
        oWall.use_line_translucency = False
        self.m_logger.WriteLine4("\t\tThe new UseLineTranslucency flag is: {0}", oWall.use_line_translucency)
        Assert.assertEqual(False, oWall.use_line_translucency)
        # LineTranslucency
        with pytest.raises(Exception):
            oWall.line_translucency = 34.56
        # UseLineTranslucency
        oWall.use_line_translucency = True
        self.m_logger.WriteLine4("\t\tThe new UseLineTranslucency flag is: {0}", oWall.use_line_translucency)
        Assert.assertEqual(True, oWall.use_line_translucency)
        # LineTranslucency
        self.m_logger.WriteLine6("\t\tThe current LineTranslucency is: {0}", oWall.line_translucency)
        oWall.line_translucency = 34.56
        self.m_logger.WriteLine6("\t\tThe new LineTranslucency is: {0}", oWall.line_translucency)
        Assert.assertAlmostEqual(34.56, oWall.line_translucency, delta=0.01)
        # LineTranslucency
        with pytest.raises(Exception):
            oWall.line_translucency = 1234.56


# endregion


# region VORouteHelper
class VORouteHelper(object):
    def __init__(self, app: "StkObjectRoot", oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits
        self._app: "StkObjectRoot" = app

    # endregion

    @property
    def Application(self):
        return self._app

    # region Run method
    def Run(self, oRoute: "VehicleGraphics3DRoute"):
        self.m_logger.WriteLine("----- THE VO ROUTE TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oRoute)

        # InheritTrackDataFrom2D
        self.m_logger.WriteLine4("The current InheritTrackDataFrom2D flag is: {0}", oRoute.inherit_track_data_from_2d)
        oRoute.inherit_track_data_from_2d = True
        self.m_logger.WriteLine4("The new InheritTrackDataFrom2D flag is: {0}", oRoute.inherit_track_data_from_2d)
        Assert.assertEqual(True, oRoute.inherit_track_data_from_2d)

        # TrackData (ReadOnly) test
        oLTHelper = VOLeadTrailDataHelper(self.m_oUnits)
        oLTHelper.Run(oRoute.track_data, True)

        oRoute.inherit_track_data_from_2d = False
        self.m_logger.WriteLine4("The new InheritTrackDataFrom2D flag is: {0}", oRoute.inherit_track_data_from_2d)
        Assert.assertEqual(False, oRoute.inherit_track_data_from_2d)

        # TrackData (NotReadOnly) test
        oLTHelper.Run(oRoute.track_data, False)

        # WaypointMarkers
        oWMHelper = VOWaypointMarkersHelper(self.Application)
        oWMHelper.Run(oRoute.waypoint_markers)

        self.m_logger.WriteLine("----- THE VO ROUTE TEST ----- END -----")


# endregion


# region VOLeadTrailDataHelper
class VOLeadTrailDataHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, leadTrailData: "VehicleGraphics3DLeadTrailData", bReadOnly: bool):
        Assert.assertIsNotNone(leadTrailData)
        if bReadOnly:
            self.ReadOnly(leadTrailData)

        else:
            self.NotReadOnly(leadTrailData)

    # endregion

    # region ReadOnly method
    def ReadOnly(self, leadTrailData: "VehicleGraphics3DLeadTrailData"):
        Assert.assertIsNotNone(leadTrailData)
        self.m_logger.WriteLine("VOLeadTrailData (ReadOnly) test:")
        bCaught: bool = False
        try:
            bCaught = False
            leadTrailData.set_lead_data_type(LEAD_TRAIL_DATA.QUARTER)
            self.m_logger.WriteLine6("The new LeadDataType flag is: {0}", leadTrailData.lead_data_type)

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The LeadDataType should be readonly.")

        try:
            bCaught = False
            leadTrailData.set_trail_data_type(LEAD_TRAIL_DATA.HALF)

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TrailDataType should be readonly.")

        try:
            bCaught = False
            leadTrailData.set_trail_same_as_lead()

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TrailDataType should be readonly.")

    # endregion

    # region NotReadOnly method
    def NotReadOnly(self, leadTrailData: "VehicleGraphics3DLeadTrailData"):
        Assert.assertIsNotNone(leadTrailData)
        self.m_logger.WriteLine("VOLeadTrailData (NotReadOnly) test:")
        bCaught: bool = False
        # SupportedDataTypes
        arSupportedTypes = leadTrailData.supported_data_types
        self.m_logger.WriteLine3("\tThe LeadTrailData supports: {0} types", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            self.m_logger.WriteLine8(
                "\t\tType {0} is: {1} ({2})",
                iIndex,
                str(arSupportedTypes[iIndex][1]),
                LEAD_TRAIL_DATA(int(arSupportedTypes[iIndex][0])),
            )

            iIndex += 1

        # LeadDataType
        self.m_logger.WriteLine6("\tThe current LeadDataType is: {0}", leadTrailData.lead_data_type)

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            eType: "LEAD_TRAIL_DATA" = LEAD_TRAIL_DATA(int(arSupportedTypes[iIndex][0]))
            if not leadTrailData.is_data_type_supported(eType):
                Assert.fail("The {0} LeadType should be supported!", eType)

            # SetLeadDataType
            leadTrailData.set_lead_data_type(eType)
            self.m_logger.WriteLine6("\tThe new LeadDataType is: {0}", leadTrailData.lead_data_type)
            eType2: "LEAD_TRAIL_DATA" = leadTrailData.lead_data_type
            Assert.assertEqual(eType, eType2)
            if leadTrailData.has_lead_data:
                if eType == LEAD_TRAIL_DATA.FRACTION:
                    # LeadData
                    oFraction: "IVehicleLeadTrailDataFraction" = IVehicleLeadTrailDataFraction(leadTrailData.lead_data)
                    Assert.assertIsNotNone(oFraction)
                    # Fraction
                    self.m_logger.WriteLine6("\t\tThe current Fraction is: {0}", oFraction.fraction)
                    oFraction.fraction = 12.3456
                    self.m_logger.WriteLine6("\t\tThe new Fraction is: {0}", oFraction.fraction)
                    Assert.assertEqual(12.3456, oFraction.fraction)
                    # range test
                    try:
                        bCaught = False
                        oFraction.fraction = -56.34

                    except Exception as e:
                        bCaught = True
                        self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set value out of range!")

                elif eType == LEAD_TRAIL_DATA.TIME:
                    # LeadData
                    oTime: "IVehicleLeadTrailDataTime" = IVehicleLeadTrailDataTime(leadTrailData.lead_data)
                    Assert.assertIsNotNone(oTime)
                    # set TimeUnit
                    strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
                    self.m_logger.WriteLine5("\tThe current TimeUnit is: {0}", strUnit)
                    self.m_oUnits.set_current_unit("TimeUnit", "hr")
                    self.m_logger.WriteLine5(
                        "\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
                    )
                    Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
                    # Time
                    self.m_logger.WriteLine6("\t\tThe current Time is: {0}", oTime.time)
                    oTime.time = 123.456
                    self.m_logger.WriteLine6("\t\tThe new Time is: {0}", oTime.time)
                    Assert.assertEqual(123.456, oTime.time)
                    # range test
                    try:
                        bCaught = False
                        oTime.time = 56340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

                    except Exception as e:
                        bCaught = True
                        self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set value out of range!")

                    # restore TimeUnit
                    self.m_oUnits.set_current_unit("TimeUnit", strUnit)
                    self.m_logger.WriteLine5("\tThe new TimeUnit (restored) is: {0}", strUnit)
                    Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
                else:
                    Assert.fail("Invalid LeadDataType has a LeadData!")

            else:
                self.m_logger.WriteLine6("\tThe LeadData is not supported by {0}.", leadTrailData.lead_data_type)

            iIndex += 1

        # TrailDataType
        self.m_logger.WriteLine6("\tThe current TrailDataType is: {0}", leadTrailData.trail_data_type)

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            eType: "LEAD_TRAIL_DATA" = LEAD_TRAIL_DATA(int(arSupportedTypes[iIndex][0]))
            if not leadTrailData.is_data_type_supported(eType):
                Assert.fail("The {0} TrailType should be supported!", eType)

            # SetTrailDataType
            leadTrailData.set_trail_data_type(eType)
            self.m_logger.WriteLine6("\tThe new TrailDataType is: {0}", leadTrailData.trail_data_type)
            eType2: "LEAD_TRAIL_DATA" = leadTrailData.trail_data_type
            Assert.assertEqual(eType, eType2)
            if leadTrailData.has_trail_data:
                if eType == LEAD_TRAIL_DATA.FRACTION:
                    # TrailData
                    oFraction: "IVehicleLeadTrailDataFraction" = IVehicleLeadTrailDataFraction(leadTrailData.trail_data)
                    Assert.assertIsNotNone(oFraction)
                    # Fraction
                    self.m_logger.WriteLine6("\t\tThe current Fraction is: {0}", oFraction.fraction)
                    oFraction.fraction = 12.3456
                    self.m_logger.WriteLine6("\t\tThe new Fraction is: {0}", oFraction.fraction)
                    Assert.assertEqual(12.3456, oFraction.fraction)
                    # range test
                    try:
                        bCaught = False
                        oFraction.fraction = -56.34

                    except Exception as e:
                        bCaught = True
                        self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set value out of range!")

                elif eType == LEAD_TRAIL_DATA.TIME:
                    # TrailData
                    oTime: "IVehicleLeadTrailDataTime" = IVehicleLeadTrailDataTime(leadTrailData.trail_data)
                    Assert.assertIsNotNone(oTime)
                    # set TimeUnit
                    strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
                    self.m_logger.WriteLine5("\tThe current TimeUnit is: {0}", strUnit)
                    self.m_oUnits.set_current_unit("TimeUnit", "hr")
                    self.m_logger.WriteLine5(
                        "\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
                    )
                    Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
                    # Time
                    self.m_logger.WriteLine6("\t\tThe current Time is: {0}", oTime.time)
                    oTime.time = 123.456
                    self.m_logger.WriteLine6("\t\tThe new Time is: {0}", oTime.time)
                    Assert.assertEqual(123.456, oTime.time)
                    # range test
                    try:
                        bCaught = False
                        oTime.time = 56340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

                    except Exception as e:
                        bCaught = True
                        self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set value out of range!")

                    # restore TimeUnit
                    self.m_oUnits.set_current_unit("TimeUnit", strUnit)
                    self.m_logger.WriteLine5("\tThe new TimeUnit (restored) is: {0}", strUnit)
                    Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
                else:
                    Assert.fail("Invalid TrailDataType has a TrailData!")

            else:
                self.m_logger.WriteLine6("\tThe TrailData is not supported by {0}.", leadTrailData.trail_data_type)

            iIndex += 1

        # SetTrailSameAsLead
        leadTrailData.set_trail_data_type(LEAD_TRAIL_DATA(int(arSupportedTypes[0][0])))
        self.m_logger.WriteLine7(
            "\tBefore: TrailDataType = {0}, LeadDataType = {1}",
            leadTrailData.trail_data_type,
            leadTrailData.lead_data_type,
        )
        leadTrailData.set_trail_same_as_lead()
        self.m_logger.WriteLine7(
            "\tAfter:  TrailDataType = {0}, LeadDataType = {1}",
            leadTrailData.trail_data_type,
            leadTrailData.lead_data_type,
        )
        Assert.assertEqual(leadTrailData.lead_data_type, leadTrailData.trail_data_type)


# endregion


# region VOWaypointMarkersHelper
class VOWaypointMarkersHelper(object):
    def __init__(self, app: "StkObjectRoot"):
        self.m_logger = Logger.Instance
        self._app: "StkObjectRoot" = app

    # endregion

    @property
    def Application(self):
        return self._app

    # region Run method
    def Run(self, oCollection: "VehicleGraphics3DWaypointMarkersCollection"):
        self.m_logger.WriteLine("VOWaypointMarkersCollection test:")
        Assert.assertIsNotNone(oCollection)
        # Count
        self.m_logger.WriteLine3("\tCollection contains: {0} elements", oCollection.count)
        # enumeration test
        waypointMarkersElement: "VehicleGraphics3DWaypointMarkersElement"
        # enumeration test
        for waypointMarkersElement in oCollection:
            self.m_logger.WriteLine10(
                "\t\tElement: Time = {0}, Shape = {1}, MarkerType = {2}, PixelSize = {3}, IsTransparent = {4}, MarkerFile = {5}",
                waypointMarkersElement.time,
                waypointMarkersElement.shape,
                waypointMarkersElement.marker_type,
                waypointMarkersElement.pixel_size,
                waypointMarkersElement.is_transparent,
                waypointMarkersElement.marker_filename,
            )

        # Item test
        bCaught: bool = False
        self.m_logger.WriteLine("\tCollection elements test:")

        iIndex: int = 0
        while iIndex < oCollection.count:
            waypointMarkersElement: "VehicleGraphics3DWaypointMarkersElement" = oCollection[iIndex]
            Assert.assertIsNotNone(waypointMarkersElement)
            self.m_logger.WriteLine3("\t\tElement {0}:", iIndex)
            self.m_logger.WriteLine10(
                "\t\t\tBefore: Time = {0}, Shape = {1}, MarkerType = {2}, PixelSize = {3}, IsTransparent = {4}, MarkerFile = {5}",
                waypointMarkersElement.time,
                waypointMarkersElement.shape,
                waypointMarkersElement.marker_type,
                waypointMarkersElement.pixel_size,
                waypointMarkersElement.is_transparent,
                waypointMarkersElement.marker_filename,
            )
            # PixelSize
            waypointMarkersElement.pixel_size = 12
            Assert.assertEqual(12, waypointMarkersElement.pixel_size)
            try:
                bCaught = False
                waypointMarkersElement.pixel_size = -34

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set value out of range!")

            # MarkerType (MARKER)
            waypointMarkersElement.marker_type = ROUTE_GRAPHICS_3D_MARKER_TYPE.MARKER
            Assert.assertEqual(ROUTE_GRAPHICS_3D_MARKER_TYPE.MARKER, waypointMarkersElement.marker_type)
            # Shape
            waypointMarkersElement.shape = MARKER_SHAPE_3D.SHAPE_TRIANGLE
            Assert.assertEqual(MARKER_SHAPE_3D.SHAPE_TRIANGLE, waypointMarkersElement.shape)
            try:
                bCaught = False
                waypointMarkersElement.marker_filename = "STKData\\VO\\Markers\\Aircraft.ppm"

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The MarkerFile should be readonly.")

            try:
                bCaught = False
                waypointMarkersElement.is_transparent = True

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The IsTransparent should be readonly.")

            # MarkerType (IMAGE)
            self.Application.begin_update()
            try:
                waypointMarkersElement.marker_type = ROUTE_GRAPHICS_3D_MARKER_TYPE.IMAGE
                # MarkerFile
                waypointMarkersElement.marker_filename = "STKData\\VO\\Markers\\Aircraft.ppm"

            finally:
                self.Application.end_update()

            Assert.assertEqual(ROUTE_GRAPHICS_3D_MARKER_TYPE.IMAGE, waypointMarkersElement.marker_type)
            Assert.assertEqual(
                TestBase.PathCombine("STKData", "VO", "Markers", "Aircraft.ppm"), waypointMarkersElement.marker_filename
            )

            waypointMarkersElement.marker_type = ROUTE_GRAPHICS_3D_MARKER_TYPE.MARKER
            Assert.assertEqual(ROUTE_GRAPHICS_3D_MARKER_TYPE.MARKER, waypointMarkersElement.marker_type)

            strFilename: str = r"VO\Markers\SampleAircraft.ppm"
            waypointMarkersElement.set_image_file(TestBase.GetScenarioFile(strFilename))
            Assert.assertEqual(ROUTE_GRAPHICS_3D_MARKER_TYPE.IMAGE, waypointMarkersElement.marker_type)
            Assert.assertEqual(
                TestBase.PathCombine("VO", "Markers", "SampleAircraft.ppm"), waypointMarkersElement.marker_filename
            )

            # IsTransparent
            waypointMarkersElement.is_transparent = True
            Assert.assertEqual(True, waypointMarkersElement.is_transparent)
            try:
                bCaught = False
                waypointMarkersElement.shape = MARKER_SHAPE_3D.SHAPE_PLUS

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The Shape should be readonly.")

            self.m_logger.WriteLine10(
                "\t\t\tAfter: Time = {0}, Shape = {1}, MarkerType = {2}, PixelSize = {3}, IsTransparent = {4}, MarkerFile = {5}",
                waypointMarkersElement.time,
                waypointMarkersElement.shape,
                waypointMarkersElement.marker_type,
                waypointMarkersElement.pixel_size,
                waypointMarkersElement.is_transparent,
                waypointMarkersElement.marker_filename,
            )

            iIndex += 1


# endregion


# region VOTrajectoryHelper
class VOTrajectoryHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oTrajectory: "VehicleGraphics3DTrajectory"):
        self.m_logger.WriteLine("----- THE VO TRAJECTORY TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oTrajectory)

        # TrackData test
        self.TrackData(oTrajectory.track_data)

        # TickMarks test
        self.TickMarks(oTrajectory.tick_marks)

        self.m_logger.WriteLine("----- THE VO TRAJECTORY TEST ----- END -----")

    # endregion

    # region TrackData method
    def TrackData(self, oTrackData: "VehicleGraphics3DTrajectoryTrackData"):
        self.m_logger.WriteLine("VOTrajectoryTrackData test:")
        Assert.assertIsNotNone(oTrackData)

        # InheritTrackDataFrom2D
        self.m_logger.WriteLine4("The current InheritFrom2D flag is: {0}", oTrackData.inherit_from_2d)
        oTrackData.inherit_from_2d = True
        self.m_logger.WriteLine4("The new InheritFrom2D flag is: {0}", oTrackData.inherit_from_2d)
        Assert.assertEqual(True, oTrackData.inherit_from_2d)

        # GroundTrack (ReadOnly) test
        oHelper = VOLeadTrailDataHelper(self.m_oUnits)
        oHelper.Run(oTrackData.pass_data.ground_track, True)

        # Trajectory (ReadOnly) test
        oHelper.Run(oTrackData.pass_data.trajectory, True)

        oTrackData.inherit_from_2d = False
        self.m_logger.WriteLine4("The new InheritFrom2D flag is: {0}", oTrackData.inherit_from_2d)
        Assert.assertEqual(False, oTrackData.inherit_from_2d)

        # GroundTrack (NotReadOnly) test
        oHelper.Run(oTrackData.pass_data.ground_track, False)

        # Trajectory (NotReadOnly) test
        oHelper.Run(oTrackData.pass_data.trajectory, False)

    # endregion

    # region TickMarks method
    def TickMarks(self, oTickMarks: "VehicleGraphics3DTrajectoryTickMarks"):
        self.m_logger.WriteLine("VOTrajectoryTrackData test:")
        Assert.assertIsNotNone(oTickMarks)
        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("TimeUnit", "min")
        self.m_logger.WriteLine5("\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("min", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        # TimeBetweenTicks (ReadOnly)
        self.m_logger.WriteLine6("\tThe current TimeBetweenTicks is: {0}", oTickMarks.time_between_ticks)
        bCaught: bool = False
        try:
            bCaught = False
            oTickMarks.time_between_ticks = 12345.6789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TimeBetweenTicks should be readonly.")

        # GroundTrack test
        oHelper = VOPathTickMarksHelper(self.m_oUnits)
        oHelper.Run(oTickMarks.ground_track)

        # Trajectory test
        oHelper.Run(oTickMarks.trajectory)

        # TimeBetweenTicks (NotReadOnly)
        oTickMarks.time_between_ticks = 12345.6789
        self.m_logger.WriteLine6("\tThe new TimeBetweenTicks is: {0}", oTickMarks.time_between_ticks)
        Assert.assertEqual(12345.6789, oTickMarks.time_between_ticks)
        # range test
        try:
            bCaught = False
            oTickMarks.time_between_ticks = -12345.6789

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new TimeUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))


# endregion


# region VOPathTickMarksHelper
class VOPathTickMarksHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oPath: "VehicleGraphics3DPathTickMarks"):
        self.m_logger.WriteLine("VOPathTickMarks test:")
        Assert.assertIsNotNone(oPath)
        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "mi")
        self.m_logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("mi", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # TickDataType
        self.m_logger.WriteLine6("\tThe current Type is: {0}", oPath.tick_data_type)
        # TickDataSupportedTypes
        arTypes = oPath.tick_data_supported_types
        self.m_logger.WriteLine3("\tThe PathTickMarks supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\tType {0} is: {1} ({2})", iIndex, str(arTypes[iIndex][1]), TICK_DATA(int(arTypes[iIndex][0]))
            )

            iIndex += 1

        # IsVisible
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oPath.show_graphics)
        oPath.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oPath.show_graphics)
        Assert.assertEqual(False, oPath.show_graphics)
        # readonly test
        bCaught: bool = False
        try:
            bCaught = False
            oPath.set_tick_data_type(TICK_DATA(arTypes[0][0]))

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TickDataType should be readonly.")

        if oPath.tick_data_type == TICK_DATA.POINT:
            oPoint: "VehicleGraphics3DTickDataPoint" = VehicleGraphics3DTickDataPoint(oPath.tick_data)
            Assert.assertIsNotNone(oPoint)
            try:
                bCaught = False
                oPoint.size = 2

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The Size should be readonly.")

        elif oPath.tick_data_type == TICK_DATA.UNKNOWN:
            pass
        else:
            oLine: "VehicleGraphics3DTickDataLine" = VehicleGraphics3DTickDataLine(oPath.tick_data)
            Assert.assertIsNotNone(oLine)
            try:
                bCaught = False
                oLine.length = 123.456

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The Length should be readonly.")

            try:
                bCaught = False
                oLine.line_width = LINE_WIDTH.WIDTH5

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The LineWidth should be readonly.")

        oPath.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oPath.show_graphics)
        Assert.assertEqual(True, oPath.show_graphics)

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "TICK_DATA" = TICK_DATA(int(arTypes[iIndex][0]))
            if not oPath.is_tick_data_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetTickDataType
            oPath.set_tick_data_type(eType)
            # TickDataType
            self.m_logger.WriteLine6("\t\tNew Type is: {0}", oPath.tick_data_type)
            if oPath.tick_data_type == TICK_DATA.UNKNOWN:
                Assert.fail("The UNKNOWN type should not be supported!")
            elif oPath.tick_data_type == TICK_DATA.POINT:
                oPoint: "VehicleGraphics3DTickDataPoint" = VehicleGraphics3DTickDataPoint(oPath.tick_data)
                Assert.assertIsNotNone(oPoint)
                # Size
                self.m_logger.WriteLine6("\t\t\tThe current Size is: {0}", oPoint.size)
                oPoint.size = 1.2345
                self.m_logger.WriteLine6("\t\t\tThe new Size is: {0}", oPoint.size)
                Assert.assertEqual(1.2345, oPoint.size)
                # range test
                try:
                    bCaught = False
                    oPoint.size = 25

                except Exception as e:
                    bCaught = True
                    self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

                if not bCaught:
                    Assert.fail("Cannot set value out of range!")

            else:
                oLine: "VehicleGraphics3DTickDataLine" = VehicleGraphics3DTickDataLine(oPath.tick_data)
                Assert.assertIsNotNone(oLine)
                # LineWith
                self.m_logger.WriteLine6("\t\t\tThe current LineWith is: {0}", oLine.line_width)
                oLine.line_width = LINE_WIDTH.WIDTH2
                self.m_logger.WriteLine6("\t\t\tThe new LineWith is: {0}", oLine.line_width)
                Assert.assertEqual(LINE_WIDTH.WIDTH2, oLine.line_width)
                # Length
                self.m_logger.WriteLine6("\t\t\tThe current Length is: {0}", oLine.length)
                oLine.length = 12.34
                self.m_logger.WriteLine6("\t\t\tThe new Length is: {0}", oLine.length)
                Assert.assertEqual(12.34, oLine.length)
                # range test
                try:
                    bCaught = False
                    oLine.length = -123.456

                except Exception as e:
                    bCaught = True
                    self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

                if not bCaught:
                    Assert.fail("Cannot set value out of range!")

            iIndex += 1

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))


# endregion


# region VOPassHelper
class VOPassHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Run method
    def Run(self, oPass: "VehicleGraphics3DPass"):
        Assert.assertIsNotNone(oPass)
        self.TrackData(oPass.track_data)
        self.TickMarks(oPass.tick_marks)

    # endregion

    # region TrackData method
    def TrackData(self, oTrackData: "VehicleGraphics3DOrbitTrackData"):
        self.m_logger.WriteLine("VOOrbitTrackData test:")
        Assert.assertIsNotNone(oTrackData)

        # InheritTrackDataFrom2D
        self.m_logger.WriteLine4("The current InheritFrom2D flag is: {0}", oTrackData.inherit_from_2d)
        oTrackData.inherit_from_2d = True
        self.m_logger.WriteLine4("The new InheritFrom2D flag is: {0}", oTrackData.inherit_from_2d)
        Assert.assertEqual(True, oTrackData.inherit_from_2d)

        # GroundTrack (ReadOnly) test
        oHelper = VOLeadTrailDataHelper(self.m_oUnits)
        oHelper.Run(oTrackData.pass_data.ground_track, True)

        # Orbit (ReadOnly) test
        oHelper.Run(oTrackData.pass_data.orbit, True)

        oTrackData.inherit_from_2d = False
        self.m_logger.WriteLine4("The new InheritFrom2D flag is: {0}", oTrackData.inherit_from_2d)
        Assert.assertEqual(False, oTrackData.inherit_from_2d)

        # GroundTrack (NotReadOnly) test
        oHelper.Run(oTrackData.pass_data.ground_track, False)

        # Orbit (NotReadOnly) test
        oHelper.Run(oTrackData.pass_data.orbit, False)

    # endregion

    # region TickMarks method
    def TickMarks(self, oTickMarks: "VehicleGraphics3DOrbitTickMarks"):
        self.m_logger.WriteLine("VOOrbitTrackData test:")
        Assert.assertIsNotNone(oTickMarks)

        # TimeBetweenTicks (ReadOnly)
        self.m_logger.WriteLine6("\tThe current TimeBetweenTicks is: {0}", oTickMarks.time_between_ticks)
        with pytest.raises(Exception):
            oTickMarks.time_between_ticks = 12345.6789

        # GroundTrack test
        oHelper = VOPathTickMarksHelper(self.m_oUnits)
        oHelper.Run(oTickMarks.ground_track)

        # Orbit test
        oHelper.Run(oTickMarks.orbit)

        # TimeBetweenTicks (NotReadOnly)
        oTickMarks.time_between_ticks = 12345.6789
        self.m_logger.WriteLine6("\tThe new TimeBetweenTicks is: {0}", oTickMarks.time_between_ticks)
        Assert.assertEqual(12345.6789, oTickMarks.time_between_ticks)
        # range test
        with pytest.raises(Exception):
            oTickMarks.time_between_ticks = -12345.6789


# endregion


# region VOAzElMaskHelper
class VOAzElMaskHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oMask: "Graphics3DAzElMask"):
        self.m_logger.WriteLine("----- THE VO AZ/EL MASK TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oMask)
        # CompassDirectionsVisible
        self.m_logger.WriteLine4("The current CompassDirectionsVisible flag is: {0}", oMask.show_compass_directions)
        oMask.show_compass_directions = False
        self.m_logger.WriteLine4("The new CompassDirectionsVisible flag is: {0}", oMask.show_compass_directions)
        Assert.assertEqual(False, oMask.show_compass_directions)
        oMask.show_compass_directions = True
        self.m_logger.WriteLine4("The new CompassDirectionsVisible flag is: {0}", oMask.show_compass_directions)
        Assert.assertEqual(True, oMask.show_compass_directions)
        # AltLabelsVisible
        self.m_logger.WriteLine4("The current AltLabelsVisible flag is: {0}", oMask.altitude_labels_visible)
        oMask.altitude_labels_visible = False
        self.m_logger.WriteLine4("The new AltLabelsVisible flag is: {0}", oMask.altitude_labels_visible)
        Assert.assertEqual(False, oMask.altitude_labels_visible)
        bCaught: bool = False
        try:
            bCaught = False
            oMask.number_of_altitude_labels = 12

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The NumbAltLabels should be readonly.")

        oMask.altitude_labels_visible = True
        self.m_logger.WriteLine4("The new AltLabelsVisible flag is: {0}", oMask.altitude_labels_visible)
        Assert.assertEqual(True, oMask.altitude_labels_visible)
        # NumbAltLabels
        self.m_logger.WriteLine3("\tThe current NumbAltLabels flag is: {0}", oMask.number_of_altitude_labels)
        oMask.number_of_altitude_labels = 45
        self.m_logger.WriteLine3("\tThe new NumbAltLabels flag is: {0}", oMask.number_of_altitude_labels)
        Assert.assertEqual(45, oMask.number_of_altitude_labels)
        try:
            bCaught = False
            oMask.number_of_altitude_labels = 123

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
    def Run(self, oSwapDist: "Graphics3DLabelSwapDistance"):
        self.m_logger.WriteLine("----- VO LABEL SWAP DISTANCE TEST ----- BEGIN -----")
        # DistanceValue
        self.m_logger.WriteLine6("\tThe current DistanceValue is: {0}", oSwapDist.distance_value)
        oSwapDist.distance_value = 0.56789
        self.m_logger.WriteLine6("\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        Assert.assertEqual(0.56789, oSwapDist.distance_value)
        with pytest.raises(Exception):
            oSwapDist.distance_value = -34.56789
        # DistanceLevel
        self.m_logger.WriteLine6("\tThe current DistanceLevel is: {0}", oSwapDist.distance_level)
        # SetDistanceLevel (ALL)
        oSwapDist.set_distance_level(GRAPHICS_3D_LABEL_SWAP_DISTANCE.ALL)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(GRAPHICS_3D_LABEL_SWAP_DISTANCE.ALL, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (MARKER)
        oSwapDist.set_distance_level(GRAPHICS_3D_LABEL_SWAP_DISTANCE.MARKER)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(GRAPHICS_3D_LABEL_SWAP_DISTANCE.MARKER, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (MARKER_LABEL)
        oSwapDist.set_distance_level(GRAPHICS_3D_LABEL_SWAP_DISTANCE.MARKER_LABEL)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(GRAPHICS_3D_LABEL_SWAP_DISTANCE.MARKER_LABEL, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (MODEL_LABEL)
        oSwapDist.set_distance_level(GRAPHICS_3D_LABEL_SWAP_DISTANCE.MODEL_LABEL)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(GRAPHICS_3D_LABEL_SWAP_DISTANCE.MODEL_LABEL, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (POINT)
        oSwapDist.set_distance_level(GRAPHICS_3D_LABEL_SWAP_DISTANCE.POINT)
        self.m_logger.WriteLine6("\tThe new DistanceLevel is: {0}", oSwapDist.distance_level)
        Assert.assertEqual(GRAPHICS_3D_LABEL_SWAP_DISTANCE.POINT, oSwapDist.distance_level)
        self.m_logger.WriteLine6("\t\tThe new DistanceValue is: {0}", oSwapDist.distance_value)
        # SetDistanceLevel (CUSTOM)
        with pytest.raises(Exception):
            oSwapDist.set_distance_level(GRAPHICS_3D_LABEL_SWAP_DISTANCE.CUSTOM)
        # SetDistanceLevel (UNKNOWN)
        with pytest.raises(Exception):
            oSwapDist.set_distance_level(GRAPHICS_3D_LABEL_SWAP_DISTANCE.UNKNOWN)
        self.m_logger.WriteLine("----- VO LABEL SWAP DISTANCE TEST ----- END -----")


# endregion


# region VOSAAContoursHelper
class VOSAAContoursHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oSAA: "VehicleGraphics3DSAA"):
        Assert.assertIsNotNone(oSAA)

        oSAA.show_graphics = False
        Assert.assertEqual(False, oSAA.show_graphics)

        oSAA.show_graphics = True
        Assert.assertEqual(True, oSAA.show_graphics)


# endregion


# region VOSystemsHelper
class VOSystemsHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oSystems: "VehicleGraphics3DSystemsCollection", root: "StkObjectRoot"):
        self.m_logger.WriteLine("----- VO SYSTEMS COLLECTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oSystems)
        # Count
        self.m_logger.WriteLine3("\tThe current Systems collection contains: {0} elements.", oSystems.count)
        # RemoveAll
        oSystems.remove_all()
        self.m_logger.WriteLine3("\tThe new Systems collection contains: {0} elements.", oSystems.count)
        Assert.assertEqual(0, oSystems.count)
        # SupportedSystems
        arSupported = oSystems.supported_systems
        self.m_logger.WriteLine3("\tThe Systems collection supports: {0} systems.", Array.Length(arSupported))
        # Add
        strSystem: str = str(arSupported[0])
        systemsElement: "VehicleGraphics3DSystemsElement" = oSystems.add(strSystem)
        Assert.assertIsNotNone(systemsElement)
        Assert.assertEqual(1, oSystems.count)
        systemsElement.show_graphics = False
        Assert.assertFalse(systemsElement.show_graphics)
        systemsElement.show_graphics = True
        Assert.assertTrue(systemsElement.show_graphics)

        arWindowIDs = None
        arNewWindowIDs = None
        if root != None:
            # Create 2 new VO windows
            root.execute_command("Window3D * CreateWindow Type Normal")
            root.execute_command("Window3D * CreateWindow Type Normal")

            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(0, len(arWindowIDs))

            arNewWindowIDs = [1]
            systemsElement.set_graphics_3d_window_identifiers(arNewWindowIDs)
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(1, len(arWindowIDs))  # number of window ids
            Assert.assertEqual(1, arWindowIDs[0])  # WindowID 1

            systemsElement.graphics_3d_window = "All"  # "clears" the list of specific WindowIds Set (sets to all)
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(0, len(arWindowIDs))

            arNewWindowIDs = [2]
            systemsElement.set_graphics_3d_window_identifiers(arNewWindowIDs)
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(1, len(arWindowIDs))  # number of window ids
            Assert.assertEqual(2, arWindowIDs[0])  # WindowID 2

            systemsElement.graphics_3d_window = "All"

            arNewWindowIDs = [3]
            systemsElement.set_graphics_3d_window_identifiers(arNewWindowIDs)
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(1, len(arWindowIDs))  # number of window ids
            Assert.assertEqual(3, arWindowIDs[0])  # WindowID 3

            systemsElement.graphics_3d_window = "All"

            arNewWindowIDs = [1, 2]
            systemsElement.set_graphics_3d_window_identifiers(arNewWindowIDs)
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(2, len(arWindowIDs))  # number of window ids
            Assert.assertEqual(1, arWindowIDs[0])  # WindowID 1
            Assert.assertEqual(2, arWindowIDs[1])  # WindowID 2

            systemsElement.graphics_3d_window = "All"

            arNewWindowIDs = [2, 3]
            systemsElement.set_graphics_3d_window_identifiers(arNewWindowIDs)
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(2, len(arWindowIDs))  # number of window ids
            Assert.assertEqual(2, arWindowIDs[0])  # WindowID 2
            Assert.assertEqual(3, arWindowIDs[1])  # WindowID 3

            systemsElement.graphics_3d_window = "All"

            arNewWindowIDs = [1, 2, 3, 4]
            with pytest.raises(Exception):
                systemsElement.set_graphics_3d_window_identifiers(arNewWindowIDs)

            # Remove the 2 new VO windows
            root.execute_command("Window3D * Remove WindowID 2")
            root.execute_command("Window3D * Remove WindowID 3")

        else:
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(0, len(arWindowIDs))

            arNewWindowIDs = [1]
            systemsElement.set_graphics_3d_window_identifiers(arNewWindowIDs)
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(1, len(arWindowIDs))  # number of window ids
            Assert.assertEqual(1, arWindowIDs[0])  # WindowID 1

            systemsElement.graphics_3d_window = "All"  # "clears" the list of specific WindowIds Set (sets to all)
            arWindowIDs = systemsElement.get_graphics_3d_window_identifiers()
            Assert.assertEqual(0, len(arWindowIDs))

            arNewWindowIDs = [1, 2, 3, 4]
            with pytest.raises(Exception):
                systemsElement.set_graphics_3d_window_identifiers(arNewWindowIDs)

        with pytest.raises(Exception):
            oSystems.add("")

        try:
            oSystems.add("InvalidSystem")
            Assert.fail("Should not allow to set an invalid value.")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        self.SystemElementBase(systemsElement, False)

        # Item
        self.m_logger.WriteLine3("\tThe new Systems collection contains: {0} elements.", oSystems.count)
        self.m_logger.WriteLine9(
            "\t\tElement: System = {0}, Color = {1}, Inherit = {2}, VOWindow = {3}",
            oSystems[0].name,
            oSystems[0].color,
            oSystems[0].inherit,
            oSystems[0].graphics_3d_window,
        )

        # Add
        strSystem = str(arSupported[1])
        systemsElement = oSystems.add(strSystem)
        Assert.assertIsNotNone(systemsElement)
        Assert.assertEqual(2, oSystems.count)
        with pytest.raises(Exception):
            oSystems.add("")
        with pytest.raises(Exception):
            oSystems.add("InvalidSystem")
        self.SystemElementBase(systemsElement, False)

        # _NewEnum
        self.m_logger.WriteLine3("\tThe new Systems collection contains: {0} elements.", oSystems.count)
        oElem: "VehicleGraphics3DSystemsElement"
        for oElem in oSystems:
            self.m_logger.WriteLine9(
                "\t\tElement: System = {0}, Color = {1}, Inherit = {2}, VOWindow = {3}",
                oElem.name,
                oElem.color,
                oElem.inherit,
                oElem.graphics_3d_window,
            )

        if not oSystems.contains(strSystem):
            Assert.fail("The Systems collection contains the {0} element.", strSystem)

        self.m_logger.WriteLine5("The Systems collection contains the {0} element.", strSystem)

        # RemoveAt
        oSystems.remove_at(1)
        Assert.assertEqual(1, oSystems.count)
        with pytest.raises(Exception):
            oSystems.remove_at(12)
        self.m_logger.WriteLine3("\tThe new Systems collection contains: {0} elements.", oSystems.count)
        oElem: "VehicleGraphics3DSystemsElement"
        for oElem in oSystems:
            self.m_logger.WriteLine9(
                "\t\tElement: System = {0}, Color = {1}, Inherit = {2}, VOWindow = {3}",
                oElem.name,
                oElem.color,
                oElem.inherit,
                oElem.graphics_3d_window,
            )

        if oSystems.contains(strSystem):
            Assert.fail("The Systems collection does not contain the {0} element.", strSystem)

        self.m_logger.WriteLine5("\tThe Systems collection does not contain the {0} element.", strSystem)
        # RemoveAll
        oSystems.remove_all()
        self.m_logger.WriteLine3("\tThe new Systems collection contains: {0} elements.", oSystems.count)
        Assert.assertEqual(0, oSystems.count)
        # Remove
        oSystems.add(strSystem)
        self.m_logger.WriteLine3("\tThe new Systems collection contains: {0} elements.", oSystems.count)
        Assert.assertTrue(oSystems.contains(strSystem))
        Assert.assertEqual(1, oSystems.count)
        oSystems.remove(strSystem)
        self.m_logger.WriteLine3("\tThe new Systems collection contains: {0} elements.", oSystems.count)
        Assert.assertFalse(oSystems.contains(strSystem))
        Assert.assertEqual(0, oSystems.count)
        with pytest.raises(Exception):
            oSystems.remove("")
        with pytest.raises(Exception):
            oSystems.remove("InvalidSystem")

        # Test Fixed by Window element
        oSpecial: "VehicleGraphics3DSystemsSpecialElement" = oSystems.fixed_by_window
        Assert.assertIsNotNone(oSpecial)
        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oSpecial.show_graphics)
        oSpecial.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oSpecial.show_graphics)
        Assert.assertFalse(oSpecial.show_graphics)
        self.SystemElementBase(oSpecial, True)
        # IsVisible (true)
        oSpecial.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oSpecial.show_graphics)
        Assert.assertTrue(oSpecial.show_graphics)
        self.SystemElementBase(oSpecial, False)

        # Test Inertial by Window element
        oSpecial = oSystems.inertial_by_window
        Assert.assertIsNotNone(oSpecial)
        # IsVisible (false)
        self.m_logger.WriteLine4("\tThe current IsVisible flag is: {0}", oSpecial.show_graphics)
        oSpecial.show_graphics = False
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oSpecial.show_graphics)
        Assert.assertFalse(oSpecial.show_graphics)
        self.SystemElementBase(oSpecial, True)
        # IsVisible (true)
        oSpecial.show_graphics = True
        self.m_logger.WriteLine4("\tThe new IsVisible flag is: {0}", oSpecial.show_graphics)
        Assert.assertTrue(oSpecial.show_graphics)
        self.SystemElementBase(oSpecial, False)

        arWindowIDs = oSpecial.get_graphics_3d_window_identifiers()
        Assert.assertEqual(0, len(arWindowIDs))

        arNewWindowIDs = [1]
        oSpecial.set_graphics_3d_window_identifiers(arNewWindowIDs)
        arWindowIDs = oSpecial.get_graphics_3d_window_identifiers()
        Assert.assertEqual(1, len(arWindowIDs))  # number of window ids
        Assert.assertEqual(1, arWindowIDs[0])  # WindowID 1

        arNewWindowIDs = [1, 2, 3]
        with pytest.raises(Exception):
            oSpecial.set_graphics_3d_window_identifiers(arNewWindowIDs)

        self.m_logger.WriteLine("----- THE VO SYSTEMS TEST ----- END -----")

    # endregion

    # region SystemElementBase
    def SystemElementBase(self, oVeVOSystemsElementBase: "IVehicleGraphics3DSystemsElementBase", bReadOnly: bool):
        self.m_logger.WriteLine("----- VO SYSTEMS ELEMENT BASE TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oVeVOSystemsElementBase)
        if bReadOnly:
            # Inherit
            with pytest.raises(Exception):
                oVeVOSystemsElementBase.inherit = False
            # Color
            with pytest.raises(Exception):
                oVeVOSystemsElementBase.color = Colors.from_argb(4660)
            # VOWindow
            with pytest.raises(Exception):
                oVeVOSystemsElementBase.graphics_3d_window = oVeVOSystemsElementBase.graphics_3d_window

        else:
            # Inherit
            self.m_logger.WriteLine4("\tThe current Inherit flag is: {0}", oVeVOSystemsElementBase.inherit)
            oVeVOSystemsElementBase.inherit = True
            self.m_logger.WriteLine4("\tThe new Inherit flag is: {0}", oVeVOSystemsElementBase.inherit)
            Assert.assertEqual(True, oVeVOSystemsElementBase.inherit)
            with pytest.raises(Exception):
                oVeVOSystemsElementBase.color = Colors.from_argb(4660)
            oVeVOSystemsElementBase.inherit = False
            self.m_logger.WriteLine4("\tThe new Inherit flag is: {0}", oVeVOSystemsElementBase.inherit)
            Assert.assertEqual(False, oVeVOSystemsElementBase.inherit)

            # Color
            self.m_logger.WriteLine6("\tThe current Color is: 0x{0:X}", oVeVOSystemsElementBase.color)
            oVeVOSystemsElementBase.color = Colors.Red
            self.m_logger.WriteLine6("\tThe new Color is: 0x{0:X}", oVeVOSystemsElementBase.color)
            AssertEx.AreEqual(Colors.Red, oVeVOSystemsElementBase.color)

            # PersistForAllPasses
            oVeVOSystemsElementBase.persist_for_all_passes = True
            Assert.assertTrue(oVeVOSystemsElementBase.persist_for_all_passes)
            oVeVOSystemsElementBase.persist_for_all_passes = False
            Assert.assertFalse(oVeVOSystemsElementBase.persist_for_all_passes)

            # AvailableVOWindows
            arWindows = oVeVOSystemsElementBase.available_graphics_3d_windows
            self.m_logger.WriteLine3("\tAvailable: {0} VO Windows.", Array.Length(arWindows))
            strWindow: str
            for strWindow in arWindows:
                self.m_logger.WriteLine5("\t\tWindow: {0}", strWindow)

            # VOWindow
            self.m_logger.WriteLine5("\tThe current VOWindow is: {0}", oVeVOSystemsElementBase.graphics_3d_window)

            i: int = 0
            while i < Array.Length(arWindows):
                oVeVOSystemsElementBase.graphics_3d_window = str(arWindows[i])
                self.m_logger.WriteLine5("\t\tThe new VOWindow is: {0}", oVeVOSystemsElementBase.graphics_3d_window)
                Assert.assertEqual(arWindows[i], oVeVOSystemsElementBase.graphics_3d_window)

                i += 1

            with pytest.raises(Exception):
                oVeVOSystemsElementBase.graphics_3d_window = ""
            with pytest.raises(Exception):
                oVeVOSystemsElementBase.graphics_3d_window = "InvalidWindow"

        self.m_logger.WriteLine("----- VO SYSTEMS ELEMENT BASE TEST ----- END -----")


# endregion


# region VOVectorsHelper
class VOVectorsHelper(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection", root: "StkObjectRoot"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits
        self.m_oRoot: "StkObjectRoot" = root

    # endregion

    # region Run method
    def Run(self, oVector: "Graphics3DVector", bScaleRelativeReadOnly: bool):
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
        self.RefCrdnsCollection(oVector.vector_geometry_tool_components)

        self.m_logger.WriteLine("----- THE VO VECTORS TEST ----- END -----")

    # endregion

    # region RefCrdnsCollection method
    def RefCrdnsCollection(self, oCollection: "Graphics3DReferenceVectorGeometryToolComponentCollection"):
        Assert.assertIsNotNone(oCollection)
        self.m_logger.WriteLine("VORefCrdnCollection test:")

        # Count
        self.m_logger.WriteLine3("The current VectorCollection contains: {0} elements", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection[iIndex]
            Assert.assertIsNotNone(refCrdn)
            self.m_logger.WriteLine8(
                "\tElement {0}: Name = {1}, Type = {2}", iIndex, refCrdn.name, refCrdn.type_identifier
            )

            iIndex += 1

        with pytest.raises(Exception):
            refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection[oCollection.count]

        voRefCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent"

        for voRefCrdn in oCollection:
            name: str = voRefCrdn.name

        # RemoveAll
        oCollection.remove_all()
        self.m_logger.WriteLine3("After RemoveAll() the Vector Collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(0, oCollection.count)

        # AvailableCrdns
        arAvailable = oCollection.available_vector_geometry_tool_components
        self.m_logger.WriteLine3("The AvailableCrdns array contains {0} elements", len(arAvailable))

        with pytest.raises(Exception):
            refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.add(
                GEOMETRIC_ELEMENT_TYPE.ANGLE_ELEMENT, "bogus"
            )

        with pytest.raises(Exception):
            oElement2: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.get_component_by_name(-1, "bogus")
        with pytest.raises(Exception):
            oElement2: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.get_component_by_name(
                GEOMETRIC_ELEMENT_TYPE.ANGLE_ELEMENT, ""
            )

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "GEOMETRIC_ELEMENT_TYPE" = GEOMETRIC_ELEMENT_TYPE(int(arAvailable[iIndex][1]))
            if eType == GEOMETRIC_ELEMENT_TYPE.ANGLE_ELEMENT:
                refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.add(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertIsNotNone(refCrdn)
                self.m_logger.WriteLine7(
                    "\tAdded element: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_identifier
                )
                oElement2: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.get_component_by_name(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertEqual(oElement2.name, refCrdn.name)
                break

            iIndex += 1

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "GEOMETRIC_ELEMENT_TYPE" = GEOMETRIC_ELEMENT_TYPE(int(arAvailable[iIndex][1]))
            if eType == GEOMETRIC_ELEMENT_TYPE.AXES_ELEMENT:
                refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.add(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertIsNotNone(refCrdn)
                self.m_logger.WriteLine7(
                    "\tAdded element: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_identifier
                )
                oElement2: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.get_component_by_name(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertEqual(oElement2.name, refCrdn.name)
                break

            iIndex += 1

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "GEOMETRIC_ELEMENT_TYPE" = GEOMETRIC_ELEMENT_TYPE(int(arAvailable[iIndex][1]))
            if eType == GEOMETRIC_ELEMENT_TYPE.PLANE_ELEMENT:
                refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.add(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertIsNotNone(refCrdn)
                self.m_logger.WriteLine7(
                    "\tAdded element: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_identifier
                )
                oElement2: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.get_component_by_name(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertEqual(oElement2.name, refCrdn.name)
                break

            iIndex += 1

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "GEOMETRIC_ELEMENT_TYPE" = GEOMETRIC_ELEMENT_TYPE(int(arAvailable[iIndex][1]))
            if eType == GEOMETRIC_ELEMENT_TYPE.POINT_ELEMENT:
                refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.add(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertIsNotNone(refCrdn)
                self.m_logger.WriteLine7(
                    "\tAdded element: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_identifier
                )
                oElement2: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.get_component_by_name(
                    eType, str(arAvailable[iIndex][0])
                )
                Assert.assertEqual(oElement2.name, refCrdn.name)
                break

            iIndex += 1

        # Add Vector element
        bFound: bool = False

        iIndex: int = 0
        while iIndex < len(arAvailable):
            eType: "GEOMETRIC_ELEMENT_TYPE" = GEOMETRIC_ELEMENT_TYPE(int(arAvailable[iIndex][1]))
            if eType == GEOMETRIC_ELEMENT_TYPE.VECTOR_ELEMENT:
                oVector: "Graphics3DReferenceVector" = Graphics3DReferenceVector(
                    oCollection.add(eType, str(arAvailable[iIndex][0]))
                )
                Assert.assertIsNotNone(oVector)
                strMagnitudeDim: str = oVector.magnitude_dimension
                if (strMagnitudeDim != "Unitless") and (strMagnitudeDim.find("Rate") == -1):
                    self.m_logger.WriteLine7(
                        "\tAdded element: Name = {0}, Type = {1}", oVector.name, oVector.type_identifier
                    )
                    oElement2: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection.get_component_by_name(
                        eType, str(arAvailable[iIndex][0])
                    )
                    Assert.assertEqual(oElement2.name, oVector.name)
                    break

                if not bFound:
                    self.m_logger.WriteLine7(
                        "\tAdded element: Name = {0}, Type = {1}", oVector.name, oVector.type_identifier
                    )
                    bFound = True

                else:
                    oCollection.remove_by_name(eType, oVector.name)

            iIndex += 1

        # Count
        self.m_logger.WriteLine3("The new VectorCollection contains: {0} elements", oCollection.count)
        refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent"
        for refCrdn in oCollection:
            self.m_logger.WriteLine7("\tElement: Name = {0}, Type = {1}", refCrdn.name, refCrdn.type_identifier)

        moonVector: "Graphics3DReferenceVector" = clr.CastAs(
            oCollection.add(GEOMETRIC_ELEMENT_TYPE.VECTOR_ELEMENT, "Satellite/Satellite1 Moon Vector"),
            Graphics3DReferenceVector,
        )  # add for Vector test

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = oCollection[iIndex]
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
                refCrdn.color = Colors.from_argb(52)

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The Color should be readonly.")

            try:
                bCaught = False
                refCrdn.show_label = True

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The LabelVisible should be readonly.")

            if refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.ANGLE_ELEMENT:
                self.RefCrdnAngleReadOnly(Graphics3DReferenceAngle(refCrdn))
            elif refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.AXES_ELEMENT:
                self.RefCrdnAxesReadOnly(Graphics3DReferenceAxes(refCrdn))
            elif refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.PLANE_ELEMENT:
                self.RefCrdnPlaneReadOnly(Graphics3DReferencePlane(refCrdn))
            elif refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.POINT_ELEMENT:
                self.RefCrdnPointReadOnly(Graphics3DReferencePoint(refCrdn))
            elif refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.VECTOR_ELEMENT:
                self.RefCrdnVectorReadOnly(Graphics3DReferenceVector(refCrdn))
            else:
                Assert.fail("Invalid TypeID!")

            # Visible (true)
            refCrdn.visible = True
            self.m_logger.WriteLine4("\tThe new Visible flag is: {0}", refCrdn.visible)
            Assert.assertEqual(True, refCrdn.visible)

            # Color
            self.m_logger.WriteLine6("\tThe current Color is: {0}", refCrdn.color)
            refCrdn.color = Colors.from_argb(9990945)
            self.m_logger.WriteLine6("\tThe new Color is: {0}", refCrdn.color)
            AssertEx.AreEqual(Colors.from_argb(9990945), refCrdn.color)

            # LabelVisible
            self.m_logger.WriteLine4("\tThe current LabelVisible flag is: {0}", refCrdn.show_label)
            refCrdn.show_label = True
            self.m_logger.WriteLine4("\tThe new LabelVisible flag is: {0}", refCrdn.show_label)
            Assert.assertEqual(True, refCrdn.show_label)
            if refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.ANGLE_ELEMENT:
                self.RefCrdnAngle(Graphics3DReferenceAngle(refCrdn))
            elif refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.AXES_ELEMENT:
                self.RefCrdnAxes(Graphics3DReferenceAxes(refCrdn))
            elif refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.PLANE_ELEMENT:
                self.RefCrdnPlane(Graphics3DReferencePlane(refCrdn))
            elif refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.POINT_ELEMENT:
                # 38619: Earth Center point freezes STK
                self.RefCrdnPoint(Graphics3DReferencePoint(refCrdn))
            elif refCrdn.type_identifier == GEOMETRIC_ELEMENT_TYPE.VECTOR_ELEMENT:
                self.RefCrdnVector(Graphics3DReferenceVector(refCrdn))
            else:
                Assert.fail("Invalid TypeID!")

            oHelper = DisplayTimesHelper(self.m_oRoot)
            oHelper.Run(IDisplayTime(refCrdn))

            iIndex += 1

        # Remove
        self.m_logger.WriteLine3("Before Remove(0) the Vector Collection contains: {0} elements", oCollection.count)
        oCollection.remove(0)
        self.m_logger.WriteLine3("After Remove(0) the Vector Collection contains: {0} elements", oCollection.count)

        with pytest.raises(Exception):
            oCollection.remove(oCollection.count)

        # RemoveByName
        self.m_logger.WriteLine3(
            "Before RemoveByName() the Vector Collection contains: {0} elements", oCollection.count
        )
        oCollection.remove_by_name(oCollection[0].type_identifier, oCollection[0].name)
        self.m_logger.WriteLine3("After RemoveByName() the Vector Collection contains: {0} elements", oCollection.count)

        with pytest.raises(Exception):
            oCollection.remove_by_name(-1, "bogus")
        with pytest.raises(Exception):
            oCollection.remove_by_name(GEOMETRIC_ELEMENT_TYPE.ANGLE_ELEMENT, "bogus")

        # RemoveAll
        self.m_logger.WriteLine3("Before RemoveAll() the Vector Collection contains: {0} elements", oCollection.count)
        oCollection.remove_all()
        self.m_logger.WriteLine3("After RemoveAll() the Vector Collection contains: {0} elements", oCollection.count)
        Assert.assertEqual(0, oCollection.count)

    # endregion

    # region RefCrdnAngleReadOnly method
    def RefCrdnAngleReadOnly(self, oAngle: "Graphics3DReferenceAngle"):
        Assert.assertIsNotNone(oAngle)
        self.m_logger.WriteLine("\tRefCrdnAngle test (ReadOnly):")
        bCaught: bool = False
        try:
            bCaught = False
            oAngle.show_angle_value = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AngleValueVisible should be readonly.")

        try:
            bCaught = False
            oAngle.angle_unit_abbreviation = "rad"

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
    def RefCrdnAngle(self, oAngle: "Graphics3DReferenceAngle"):
        Assert.assertIsNotNone(oAngle)
        self.m_logger.WriteLine("\tRefCrdnAngle test:")
        # AngleValueVisible
        self.m_logger.WriteLine4("\t\tThe current AngleValueVisible flag is: {0}", oAngle.show_angle_value)
        oAngle.show_angle_value = False
        self.m_logger.WriteLine4("\t\tThe new AngleValueVisible flag is: {0}", oAngle.show_angle_value)
        Assert.assertEqual(False, oAngle.show_angle_value)
        bCaught: bool = False
        try:
            bCaught = False
            oAngle.angle_unit_abbreviation = "mrad"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AngleUnitAbrv should be readonly.")

        oAngle.show_angle_value = True
        self.m_logger.WriteLine4("\t\tThe new AngleValueVisible flag is: {0}", oAngle.show_angle_value)
        Assert.assertEqual(True, oAngle.show_angle_value)
        # AngleUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current AngleUnitAbrv is: {0}", oAngle.angle_unit_abbreviation)
        oAngle.angle_unit_abbreviation = "mdeg"
        self.m_logger.WriteLine5("\t\tThe new AngleUnitAbrv is: {0}", oAngle.angle_unit_abbreviation)
        Assert.assertEqual("mdeg", oAngle.angle_unit_abbreviation)
        try:
            bCaught = False
            oAngle.angle_unit_abbreviation = "abcdefgh"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

    # endregion

    # region RefCrdnAxesReadOnly method
    def RefCrdnAxesReadOnly(self, oAxes: "Graphics3DReferenceAxes"):
        Assert.assertIsNotNone(oAxes)
        self.m_logger.WriteLine("\tRefCrdnAxes test (ReadOnly):")
        bCaught: bool = False
        try:
            bCaught = False
            oAxes.draw_at_central_body = False

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The DrawAtCB should be readonly.")

        try:
            bCaught = False
            oAxes.show_persistence = False

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
            oAxes.connect = VECTOR_AXES_CONNECT_TYPE.LINE

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
    def RefCrdnAxes(self, oAxes: "Graphics3DReferenceAxes"):
        availableAxes = oAxes.available_axes
        Assert.assertTrue((Array.Length(availableAxes) > 0))

        oAxes.axes = "Satellite/Satellite1 Equinoctial Axes"
        Assert.assertEqual("Satellite/Satellite1 Equinoctial Axes", oAxes.axes)

        # BUG121438
        # for (int i=0; i<10; i++)
        # {
        #    Console.WriteLine("XXX " + availableAxes.GetValue(i).ToString());
        # }

        oAxes.draw_at_point = False
        Assert.assertFalse(oAxes.draw_at_point)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAxes.point = "Satellite/Satellite1 SunGlint Point"

        oAxes.draw_at_central_body = False
        Assert.assertFalse(oAxes.draw_at_central_body)
        oAxes.draw_at_central_body = True
        Assert.assertTrue(oAxes.draw_at_central_body)

        oAxes.draw_at_point = True
        Assert.assertTrue(oAxes.draw_at_point)

        oAxes.point = "Satellite/Satellite1 SunGlint Point"
        Assert.assertEqual("Satellite/Satellite1 SunGlint Point", oAxes.point)
        with pytest.raises(Exception, match=RegexSubstringMatch("not a valid choice")):
            oAxes.point = "Satellite/Satellite1 Bogus Point"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAxes.draw_at_central_body = False

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            oAxes.thickness = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            oAxes.thickness = 0
        oAxes.thickness = 1
        Assert.assertEqual(1, oAxes.thickness)
        oAxes.thickness = 100
        Assert.assertEqual(100, oAxes.thickness)

        oAxes.show_persistence = False
        Assert.assertFalse(oAxes.show_persistence)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # "Fade" checkbox in GUI
            oAxes.transparent = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oAxes.duration = 600
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oAxes.connect = VECTOR_AXES_CONNECT_TYPE.LINE

        oAxes.show_persistence = True
        Assert.assertTrue(oAxes.show_persistence)

        oAxes.transparent = False  # "Fade" checkbox in GUI
        Assert.assertFalse(oAxes.transparent)
        oAxes.transparent = True  # "Fade" checkbox in GUI
        Assert.assertTrue(oAxes.transparent)

        oAxes.duration = 0
        Assert.assertEqual(0, oAxes.duration)
        oAxes.duration = 10000000
        Assert.assertEqual(10000000, oAxes.duration)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oAxes.duration = -1

        oAxes.connect = VECTOR_AXES_CONNECT_TYPE.SWEEP
        Assert.assertEqual(VECTOR_AXES_CONNECT_TYPE.SWEEP, oAxes.connect)
        oAxes.connect = VECTOR_AXES_CONNECT_TYPE.TRACE
        Assert.assertEqual(VECTOR_AXES_CONNECT_TYPE.TRACE, oAxes.connect)
        oAxes.connect = VECTOR_AXES_CONNECT_TYPE.LINE
        Assert.assertEqual(VECTOR_AXES_CONNECT_TYPE.LINE, oAxes.connect)

    # endregion

    # region RefCrdnPlaneReadOnly method
    def RefCrdnPlaneReadOnly(self, oPlane: "Graphics3DReferencePlane"):
        Assert.assertIsNotNone(oPlane)
        self.m_logger.WriteLine("\tRefCrdnPlane test (ReadOnly):")
        bCaught: bool = False
        try:
            bCaught = False
            oPlane.show_axis_labels = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The AxisLabelsVisible should be readonly.")

        try:
            bCaught = False
            oPlane.is_plane_transparent = True

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
            oPlane.show_rectangular_grid = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RectGridVisible should be readonly.")

        try:
            bCaught = False
            oPlane.show_circle_grid = True

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
    def RefCrdnPlane(self, oPlane: "Graphics3DReferencePlane"):
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
        self.m_logger.WriteLine4("\t\tThe current AxisLabelsVisible flag is: {0}", oPlane.show_axis_labels)
        oPlane.show_axis_labels = False
        self.m_logger.WriteLine4("\t\tThe new AxisLabelsVisible flag is: {0}", oPlane.show_axis_labels)
        Assert.assertEqual(False, oPlane.show_axis_labels)
        oPlane.show_axis_labels = True
        self.m_logger.WriteLine4("\t\tThe new AxisLabelsVisible flag is: {0}", oPlane.show_axis_labels)
        Assert.assertEqual(True, oPlane.show_axis_labels)
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
        self.m_logger.WriteLine4("\t\tThe current TransparentPlaneVisible flag is: {0}", oPlane.is_plane_transparent)
        oPlane.is_plane_transparent = False
        self.m_logger.WriteLine4("\t\tThe new TransparentPlaneVisible flag is: {0}", oPlane.is_plane_transparent)
        Assert.assertEqual(False, oPlane.is_plane_transparent)
        try:
            bCaught = False
            oPlane.transparency = 23.45

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The Transparency should be readonly.")

        oPlane.is_plane_transparent = True
        self.m_logger.WriteLine4("\t\tThe new TransparentPlaneVisible flag is: {0}", oPlane.is_plane_transparent)
        Assert.assertEqual(True, oPlane.is_plane_transparent)
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
        self.m_logger.WriteLine4("\t\tThe current RectGridVisible flag is: {0}", oPlane.show_rectangular_grid)
        oPlane.show_rectangular_grid = False
        self.m_logger.WriteLine4("\t\tThe new RectGridVisible flag is: {0}", oPlane.show_rectangular_grid)
        Assert.assertEqual(False, oPlane.show_rectangular_grid)
        # CircGridVisible (false)
        self.m_logger.WriteLine4("\t\tThe current CircGridVisible flag is: {0}", oPlane.show_circle_grid)
        oPlane.show_circle_grid = False
        self.m_logger.WriteLine4("\t\tThe new CircGridVisible flag is: {0}", oPlane.show_circle_grid)
        Assert.assertEqual(False, oPlane.show_circle_grid)
        try:
            bCaught = False
            oPlane.plane_grid_spacing = 123.45

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The PlaneGridSpacing should be readonly.")

        # RectGridVisible (true)
        oPlane.show_rectangular_grid = True
        self.m_logger.WriteLine4("\t\tThe new RectGridVisible flag is: {0}", oPlane.show_rectangular_grid)
        Assert.assertEqual(True, oPlane.show_rectangular_grid)
        # PlaneGridSpacing
        self.m_logger.WriteLine6("\t\tThe current PlaneGridSpacing is: {0}", oPlane.plane_grid_spacing)
        oPlane.plane_grid_spacing = 987.654
        self.m_logger.WriteLine6("\t\tThe new PlaneGridSpacing is: {0}", oPlane.plane_grid_spacing)
        Assert.assertAlmostEqual(987.654, oPlane.plane_grid_spacing, delta=0.0001)
        # CircGridVisible (true)
        oPlane.show_circle_grid = True
        self.m_logger.WriteLine4("\t\tThe new CircGridVisible flag is: {0}", oPlane.show_circle_grid)
        Assert.assertEqual(True, oPlane.show_circle_grid)
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
    def RefCrdnPointReadOnly(self, oPoint: "Graphics3DReferencePoint"):
        Assert.assertIsNotNone(oPoint)
        self.m_logger.WriteLine("\tRefCrdnPoint test (ReadOnly):")
        bCaught: bool = False
        try:
            bCaught = False
            oPoint.trajectory_type = TRAJECTORY_TYPE.TRACE

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The TrajectoryType should be readonly.")

        try:
            bCaught = False
            oPoint.show_right_ascension_declination_values = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecVisible should be readonly.")

        try:
            bCaught = False
            oPoint.right_ascension_declination_units_abbreviation = "arcMin"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecUnitAbrv should be readonly.")

        try:
            bCaught = False
            oPoint.show_cartesian_value = True

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CartesianVisible should be readonly.")

        try:
            bCaught = False
            oPoint.cartesian_units_abbreviation = "Au"

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
    def RefCrdnPoint(self, oPoint: "Graphics3DReferencePoint"):
        Assert.assertIsNotNone(oPoint)
        self.m_logger.WriteLine("\tRefCrdnPoint test:")
        # TrajectoryType
        self.m_logger.WriteLine6("\t\tThe current TrajectoryType is: {0}", oPoint.trajectory_type)
        oPoint.trajectory_type = TRAJECTORY_TYPE.LINE
        self.m_logger.WriteLine6("\t\tThe new TrajectoryType flag is: {0}", oPoint.trajectory_type)
        Assert.assertEqual(TRAJECTORY_TYPE.LINE, oPoint.trajectory_type)
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
        self.m_logger.WriteLine4(
            "\t\tThe current RADecVisible flag is: {0}", oPoint.show_right_ascension_declination_values
        )
        oPoint.show_right_ascension_declination_values = False
        self.m_logger.WriteLine4(
            "\t\tThe new RADecVisible flag is: {0}", oPoint.show_right_ascension_declination_values
        )
        Assert.assertEqual(False, oPoint.show_right_ascension_declination_values)
        try:
            bCaught = False
            oPoint.right_ascension_declination_units_abbreviation = "deg"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The RADecUnitAbrv should be readonly.")

        oPoint.show_right_ascension_declination_values = True
        self.m_logger.WriteLine4(
            "\t\tThe new RADecVisible flag is: {0}", oPoint.show_right_ascension_declination_values
        )
        Assert.assertEqual(True, oPoint.show_right_ascension_declination_values)
        # RADecUnitAbrv
        self.m_logger.WriteLine5(
            "\t\tThe current RADecUnitAbrv is: {0}", oPoint.right_ascension_declination_units_abbreviation
        )
        oPoint.right_ascension_declination_units_abbreviation = "mrad"
        self.m_logger.WriteLine5(
            "\t\tThe new RADecUnitAbrv is: {0}", oPoint.right_ascension_declination_units_abbreviation
        )
        Assert.assertEqual("mrad", oPoint.right_ascension_declination_units_abbreviation)
        try:
            bCaught = False
            oPoint.right_ascension_declination_units_abbreviation = "Abc"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal RADecUnitAbrv!")

        # MagnitudeVisible
        self.m_logger.WriteLine4("\t\tThe current MagnitudeVisible flag is: {0}", oPoint.show_magnitude_value)
        oPoint.show_magnitude_value = False
        self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oPoint.show_magnitude_value)
        Assert.assertEqual(False, oPoint.show_magnitude_value)
        try:
            bCaught = False
            oPoint.magnitude_units_abbreviation = "fur"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The MagnitudeUnitAbrv should be readonly.")

        oPoint.show_magnitude_value = True
        self.m_logger.WriteLine4("\t\tThe new MagnitudeVisible flag is: {0}", oPoint.show_magnitude_value)
        Assert.assertEqual(True, oPoint.show_magnitude_value)
        # MagnitudeUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current MagnitudeUnitAbrv is: {0}", oPoint.magnitude_units_abbreviation)
        oPoint.magnitude_units_abbreviation = "fur"
        self.m_logger.WriteLine5("\t\tThe new MagnitudeUnitAbrv is: {0}", oPoint.magnitude_units_abbreviation)
        Assert.assertEqual("fur", oPoint.magnitude_units_abbreviation)
        try:
            bCaught = False
            oPoint.magnitude_units_abbreviation = "Abc"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal MagnitudeUnitAbrv!")

        # CartesianVisible
        self.m_logger.WriteLine4("\t\tThe current CartesianVisible flag is: {0}", oPoint.show_cartesian_value)
        oPoint.show_cartesian_value = False
        self.m_logger.WriteLine4("\t\tThe new CartesianVisible flag is: {0}", oPoint.show_cartesian_value)
        Assert.assertEqual(False, oPoint.show_cartesian_value)
        try:
            bCaught = False
            oPoint.cartesian_units_abbreviation = "kft"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("The CartesianUnitAbrv should be readonly.")

        oPoint.show_cartesian_value = True
        self.m_logger.WriteLine4("\t\tThe new CartesianVisible flag is: {0}", oPoint.show_cartesian_value)
        Assert.assertEqual(True, oPoint.show_cartesian_value)
        # CartesianUnitAbrv
        self.m_logger.WriteLine5("\t\tThe current CartesianUnitAbrv is: {0}", oPoint.cartesian_units_abbreviation)
        oPoint.cartesian_units_abbreviation = "kft"
        self.m_logger.WriteLine5("\t\tThe new CartesianUnitAbrv is: {0}", oPoint.cartesian_units_abbreviation)
        Assert.assertEqual("kft", oPoint.cartesian_units_abbreviation)
        try:
            bCaught = False
            oPoint.cartesian_units_abbreviation = "Abc"

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set illegal CartesianUnitAbrv!")

    # endregion

    # region RefCrdnVectorReadOnly method
    def RefCrdnVectorReadOnly(self, oVector: "Graphics3DReferenceVector"):
        Assert.assertIsNotNone(oVector)
        self.m_logger.WriteLine("\tRefCrdnVector test (ReadOnly):")
        # DrawAtCB
        with pytest.raises(Exception):
            oVector.draw_at_central_body = True
        # RADecVisible
        with pytest.raises(Exception):
            oVector.show_right_ascension_declination_values = True
        # RADecUnitAbrv
        with pytest.raises(Exception):
            oVector.right_ascension_declination_units_abbreviation = "semiC"
        # MagnitudeVisible
        with pytest.raises(Exception):
            oVector.show_magnitude_value = True
        # PersistenceVisible
        with pytest.raises(Exception):
            oVector.show_persistence = True
        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        # Duration
        with pytest.raises(Exception):
            oVector.duration = 123.456
        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        self.m_logger.WriteLine5(
            "\t\tThe new (restored) TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        )
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        # Connect
        with pytest.raises(Exception):
            oVector.connect = VECTOR_AXES_CONNECT_TYPE.LINE
        # Transparent
        with pytest.raises(Exception):
            oVector.transparent = True
        # Axes
        with pytest.raises(Exception):
            oVector.axes = "CentralBody/Earth Fixed Axes"
        # DrawAtPoint
        with pytest.raises(Exception):
            oVector.draw_at_point = True
        # Point
        with pytest.raises(Exception):
            oVector.point = "Satellite/Satellite1 Center Point"
        # TrueScale
        with pytest.raises(Exception):
            oVector.true_scale = True

    # endregion

    # region RefCrdnVector method
    def RefCrdnVector(self, oVector: "Graphics3DReferenceVector"):
        availableAxes = oVector.available_axes
        Assert.assertTrue((Array.Length(availableAxes) > 0))

        oVector.axes = "Satellite/Satellite1 Equinoctial Axes"
        Assert.assertEqual("Satellite/Satellite1 Equinoctial Axes", oVector.axes)

        # BUG121438
        # for (int i = 0; i < 10; i++)
        # {
        #    Console.WriteLine("XXX " + availableAxes.GetValue(i).ToString());
        # }

        oVector.draw_at_point = False
        Assert.assertFalse(oVector.draw_at_point)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oVector.point = "Satellite/Satellite1 SunGlint Point"

        oVector.draw_at_central_body = False
        Assert.assertFalse(oVector.draw_at_central_body)
        oVector.draw_at_central_body = True
        Assert.assertTrue(oVector.draw_at_central_body)

        oVector.draw_at_point = True
        Assert.assertTrue(oVector.draw_at_point)

        oVector.point = "Satellite/Satellite1 SunGlint Point"
        Assert.assertEqual("Satellite/Satellite1 SunGlint Point", oVector.point)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oVector.draw_at_central_body = False

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            oVector.thickness = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            oVector.thickness = 0
        oVector.thickness = 1
        Assert.assertEqual(1, oVector.thickness)
        oVector.thickness = 100
        Assert.assertEqual(100, oVector.thickness)

        oVector.show_persistence = False
        Assert.assertFalse(oVector.show_persistence)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # "Fade" checkbox in GUI
            oVector.transparent = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            oVector.duration = 600
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oVector.connect = VECTOR_AXES_CONNECT_TYPE.LINE

        oVector.show_persistence = True
        Assert.assertTrue(oVector.show_persistence)

        oVector.transparent = False  # "Fade" checkbox in GUI
        Assert.assertFalse(oVector.transparent)
        oVector.transparent = True  # "Fade" checkbox in GUI
        Assert.assertTrue(oVector.transparent)

        oVector.duration = 0
        Assert.assertEqual(0, oVector.duration)
        oVector.duration = 10000000
        Assert.assertEqual(10000000, oVector.duration)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            oVector.duration = -1

        oVector.connect = VECTOR_AXES_CONNECT_TYPE.SWEEP
        Assert.assertEqual(VECTOR_AXES_CONNECT_TYPE.SWEEP, oVector.connect)
        oVector.connect = VECTOR_AXES_CONNECT_TYPE.TRACE
        Assert.assertEqual(VECTOR_AXES_CONNECT_TYPE.TRACE, oVector.connect)
        oVector.connect = VECTOR_AXES_CONNECT_TYPE.LINE
        Assert.assertEqual(VECTOR_AXES_CONNECT_TYPE.LINE, oVector.connect)

        oVector.show_right_ascension_declination_values = False
        Assert.assertFalse(oVector.show_right_ascension_declination_values)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            oVector.right_ascension_declination_units_abbreviation = "rad"

        oVector.show_right_ascension_declination_values = True
        Assert.assertTrue(oVector.show_right_ascension_declination_values)

        oVector.right_ascension_declination_units_abbreviation = "rad"
        Assert.assertEqual("rad", oVector.right_ascension_declination_units_abbreviation)
        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            oVector.right_ascension_declination_units_abbreviation = "bogus"
        if (
            clr.CastAs(oVector, IGraphics3DReferenceAnalysisWorkbenchComponent)
        ).name == "Aircraft/Boing737 Body.-X Vector":
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # because not a distance unit vector
                oVector.true_scale = False

            Assert.assertEqual("Unitless", oVector.magnitude_dimension)

            oVector.show_magnitude_value = False
            Assert.assertFalse(oVector.show_magnitude_value)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oVector.magnitude_units_abbreviation = "rad"

            oVector.show_magnitude_value = True
            Assert.assertTrue(oVector.show_magnitude_value)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # because Unitless
                oVector.magnitude_units_abbreviation = "rad"
        elif (
            clr.CastAs(oVector, IGraphics3DReferenceAnalysisWorkbenchComponent)
        ).name == "Aircraft/Boing737 MagField(IGRF) Vector":
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # because not a distance unit vector
                oVector.true_scale = False

            Assert.assertEqual("MagneticFieldUnit", oVector.magnitude_dimension)

            oVector.show_magnitude_value = False
            Assert.assertFalse(oVector.show_magnitude_value)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oVector.magnitude_units_abbreviation = "gauss"

            oVector.show_magnitude_value = True
            Assert.assertTrue(oVector.show_magnitude_value)

            oVector.magnitude_units_abbreviation = "gauss"
            Assert.assertEqual("gauss", oVector.magnitude_units_abbreviation)
        elif (
            clr.CastAs(oVector, IGraphics3DReferenceAnalysisWorkbenchComponent)
        ).name == "Satellite/Satellite1 Moon Vector":
            oVector.true_scale = False
            Assert.assertFalse(oVector.true_scale)
            oVector.true_scale = True
            Assert.assertTrue(oVector.true_scale)

            Assert.assertEqual("DistanceUnit", oVector.magnitude_dimension)

            oVector.show_magnitude_value = False
            Assert.assertFalse(oVector.show_magnitude_value)

            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oVector.magnitude_units_abbreviation = "m"

            oVector.show_magnitude_value = True
            Assert.assertTrue(oVector.show_magnitude_value)

            oVector.magnitude_units_abbreviation = "m"
            Assert.assertEqual("m", oVector.magnitude_units_abbreviation)
        else:
            pass


# endregion


# region VOVaporTrail
class VOVaporTrailHelper(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Run method
    def Run(self, oVaporTrail: "Graphics3DVaporTrail", oModel: "IGraphics3DModel", strDataPath: str):
        self.m_logger.WriteLine("----- VO VAPOR TRAIL TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oVaporTrail)
        Assert.assertIsNotNone(oModel)
        # Visible (false)
        self.m_logger.WriteLine4("\tThe current Visible is: {0}", oVaporTrail.visible)
        oVaporTrail.visible = False
        self.m_logger.WriteLine4("\tThe new Visible is: {0}", oVaporTrail.visible)
        Assert.assertFalse(oVaporTrail.visible)
        # MaxNumOfPuffs (read only)
        with pytest.raises(Exception):
            oVaporTrail.maximum_number_of_puffs = 34
        # Density (read only)
        with pytest.raises(Exception):
            oVaporTrail.density = 3.4
        # Radius (read only)
        with pytest.raises(Exception):
            oVaporTrail.radius = 34.56
        # Color (read only)
        with pytest.raises(Exception):
            oVaporTrail.color = Colors.from_argb(1218646)
        # ImageFile (read only)
        with pytest.raises(Exception):
            oVaporTrail.image_filename = strDataPath + r"\STKData\VO/Textures/smoke.pgm"
        # UseAttachPoint (read only)
        with pytest.raises(Exception):
            oVaporTrail.use_attach_point = False
        # AttachPointName (read only)
        with pytest.raises(Exception):
            oVaporTrail.attachment_point_name = "InvalidPointName"
        # Visible (true)
        oVaporTrail.visible = True
        self.m_logger.WriteLine4("\tThe new Visible is: {0}", oVaporTrail.visible)
        Assert.assertTrue(oVaporTrail.visible)
        # MaxNumOfPuffs
        self.m_logger.WriteLine3("\tThe current MaxNumOfPuffs is: {0}", oVaporTrail.maximum_number_of_puffs)
        oVaporTrail.maximum_number_of_puffs = 34
        self.m_logger.WriteLine3("\tThe new MaxNumOfPuffs is: {0}", oVaporTrail.maximum_number_of_puffs)
        Assert.assertEqual(34, oVaporTrail.maximum_number_of_puffs)
        with pytest.raises(Exception):
            oVaporTrail.maximum_number_of_puffs = 12345
        # Density
        self.m_logger.WriteLine6("\tThe current Density is: {0}", oVaporTrail.density)
        oVaporTrail.density = 123.456
        self.m_logger.WriteLine6("\tThe new Density is: {0}", oVaporTrail.density)
        Assert.assertAlmostEqual(123.456, oVaporTrail.density, delta=0.0001)
        with pytest.raises(Exception):
            oVaporTrail.density = 12345.6789
        # Radius
        self.m_logger.WriteLine6("\tThe current Radius is: {0}", oVaporTrail.radius)
        oVaporTrail.radius = 1234.56
        self.m_logger.WriteLine6("\tThe new Radius is: {0}", oVaporTrail.radius)
        Assert.assertAlmostEqual(1234.56, oVaporTrail.radius, delta=0.001)
        with pytest.raises(Exception):
            oVaporTrail.radius = -12345.6789
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
        oVaporTrail.color = Colors.from_argb(4660)
        self.m_logger.WriteLine6("\tThe new Color is: {0}", oVaporTrail.color)
        AssertEx.AreEqual(Colors.from_argb(4660), oVaporTrail.color)
        # ImageFile
        self.m_logger.WriteLine5("\tThe current ImageFile is: {0}", oVaporTrail.image_filename)
        oVaporTrail.image_filename = strDataPath + r"\STKData\VO\Textures\smoke.pgm"
        self.m_logger.WriteLine5("\tThe new ImageFile is: {0}", oVaporTrail.image_filename)
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Textures", "smoke.pgm"), oVaporTrail.image_filename)
        with pytest.raises(Exception):
            oVaporTrail.image_filename = "InvalidImageFile.Name"

        # AvailableAttachPoints
        file: "Graphics3DModelFile" = clr.CastAs(oModel.model_data, Graphics3DModelFile)
        arAvailablePoints = oVaporTrail.available_attachment_points
        self.m_logger.WriteLine3(
            "\tThe current model contains: {0} available attach points.", Array.Length(arAvailablePoints)
        )
        if file.filename.endswith("aircraft.glb"):
            Assert.assertEqual(2, Array.Length(arAvailablePoints))

        elif file.filename.endswith("facility.glb"):
            Assert.assertEqual(0, Array.Length(arAvailablePoints))
            with pytest.raises(Exception):
                oVaporTrail.use_attach_point = False

        with pytest.raises(Exception):
            oVaporTrail.attachment_point_name = "InvalidPointName"

        # Load a VOModel with attached points
        oModel.visible = True
        Assert.assertTrue(oModel.visible)
        oModel.model_type = MODEL_TYPE.FILE
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        oModelFile: "Graphics3DModelFile" = Graphics3DModelFile(oModel.model_data)
        Assert.assertIsNotNone(oModelFile)
        self.m_logger.WriteLine5("\tThe current VOModel file is: {0}", oModelFile.filename)
        oModelFile.filename = strDataPath + r"\STKData\VO\Models\Space\pegasus.glb"
        self.m_logger.WriteLine5("\tThe new VOModel file is: {0}", oModelFile.filename)
        Assert.assertEqual(TestBase.PathCombine("STKData", "VO", "Models", "Space", "pegasus.glb"), oModelFile.filename)
        arAvailablePoints = oVaporTrail.available_attachment_points
        self.m_logger.WriteLine3(
            "\tThe current model contains: {0} available attach points.", Array.Length(arAvailablePoints)
        )
        Assert.assertEqual(3, Array.Length(arAvailablePoints))
        # UseAttachPoint (false)
        self.m_logger.WriteLine4("\tThe current UseAttachPoint is: {0}", oVaporTrail.use_attach_point)
        oVaporTrail.use_attach_point = False
        self.m_logger.WriteLine4("\tThe new UseAttachPoint is: {0}", oVaporTrail.use_attach_point)
        Assert.assertFalse(oVaporTrail.use_attach_point)
        # AttachPointName (read only)
        with pytest.raises(Exception):
            oVaporTrail.attachment_point_name = "InvalidPointName"
        # UseAttachPoint (true)
        oVaporTrail.use_attach_point = True
        self.m_logger.WriteLine4("\tThe new UseAttachPoint is: {0}", oVaporTrail.use_attach_point)
        Assert.assertTrue(oVaporTrail.use_attach_point)
        # AttachPointName
        self.m_logger.WriteLine5("\tThe current AttachPointName is: {0}", oVaporTrail.attachment_point_name)

        iIndex: int = 0
        while iIndex < Array.Length(arAvailablePoints):
            oVaporTrail.attachment_point_name = str(arAvailablePoints[iIndex])
            self.m_logger.WriteLine5("\tThe new AttachPointName is: {0}", oVaporTrail.attachment_point_name)
            Assert.assertEqual(str(arAvailablePoints[iIndex]), oVaporTrail.attachment_point_name)

            iIndex += 1

        with pytest.raises(Exception):
            oVaporTrail.attachment_point_name = "InvalidPointName"
        self.m_logger.WriteLine("----- VO VAPOR TRAIL TEST ----- END -----")

    # endregion
