import pytest
from test_util import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


# region Orientations enum
class Orientations:
    AzEl = 1
    EulerAngles = 2
    Quaternion = 4
    YPRAngles = 8
    All = 15


# endregion


# ////////////////////////////////////////////////////////////////////////
class OrientationTest(object):
    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # region Display method
    def Display(self, oOrientation: "IOrientation"):
        Assert.assertIsNotNone(oOrientation)
        if oOrientation.orientation_type == OrientationType.AZ_EL:
            oAzEl: "IOrientationAzEl" = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))
            Assert.assertIsNotNone(oAzEl)
            self.m_logger.WriteLine6("\t\tAzEl Azimuth is: {0}", oAzEl.azimuth)
            self.m_logger.WriteLine6("\t\tAzEl Elevation is: {0}", oAzEl.elevation)
            self.m_logger.WriteLine6("\t\tAzEl AboutBoresight is: {0}", oAzEl.about_boresight)
        elif oOrientation.orientation_type == OrientationType.EULER_ANGLES:
            oEulerAngles: "IOrientationEulerAngles" = IOrientationEulerAngles(
                oOrientation.convert_to(OrientationType.EULER_ANGLES)
            )
            Assert.assertIsNotNone(oEulerAngles)
            self.m_logger.WriteLine6("\t\tEulerAngles A is: {0}", oEulerAngles.a)
            self.m_logger.WriteLine6("\t\tEulerAngles B is: {0}", oEulerAngles.b)
            self.m_logger.WriteLine6("\t\tEulerAngles C is: {0}", oEulerAngles.c)
            self.m_logger.WriteLine6("\t\tEulerAngles Sequence is: {0}", oEulerAngles.sequence)
        elif oOrientation.orientation_type == OrientationType.QUATERNION:
            oQuaternion: "IOrientationQuaternion" = IOrientationQuaternion(
                oOrientation.convert_to(OrientationType.QUATERNION)
            )
            Assert.assertIsNotNone(oQuaternion)
            self.m_logger.WriteLine6("\t\tQuaternion QX is: {0}", oQuaternion.qx)
            self.m_logger.WriteLine6("\t\tQuaternion QY is: {0}", oQuaternion.qy)
            self.m_logger.WriteLine6("\t\tQuaternion QZ is: {0}", oQuaternion.qz)
            self.m_logger.WriteLine6("\t\tQuaternion QS is: {0}", oQuaternion.qs)
        elif oOrientation.orientation_type == OrientationType.YPR_ANGLES:
            oYPRAngles: "IOrientationYPRAngles" = IOrientationYPRAngles(
                oOrientation.convert_to(OrientationType.YPR_ANGLES)
            )
            Assert.assertIsNotNone(oYPRAngles)
            self.m_logger.WriteLine6("\t\tYPRAngles Yaw is: {0}", oYPRAngles.yaw)
            self.m_logger.WriteLine6("\t\tYPRAngles Pitch is: {0}", oYPRAngles.pitch)
            self.m_logger.WriteLine6("\t\tYPRAngles Roll is: {0}", oYPRAngles.roll)
            self.m_logger.WriteLine6("\t\tYPRAngles Sequence is: {0}", oYPRAngles.sequence)
        else:
            Assert.fail("Invalid Orientation type!")

    # endregion

    # region Run method
    def Run(self, oOrientation: "IOrientation", eTypes):
        self.m_logger.WriteLine("----- ORIENTATION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oOrientation)
        self.m_logger.WriteLine6("\tOrientation test for: {0} orientations", eTypes)
        # OrientationType
        self.m_logger.WriteLine6("\tThe current OrientationType is: {0}", oOrientation.orientation_type)
        self.Display(oOrientation)

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "deg")
        self.m_logger.WriteLine5("\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("deg", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
            oAzEl: "IOrientationAzEl" = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))
            Assert.assertIsNotNone(oAzEl)
            oAzEl.assign(oOrientation)
            self.m_logger.WriteLine6("\tNew orientation type is: {0}", oAzEl.orientation_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oAzEl)
            oAzEl.azimuth = 123.45
            oAzEl.elevation = 54.321
            oAzEl.about_boresight = AzElAboutBoresight.HOLD
            oAzEl.assign_az_el(123.45, 54.321, AzElAboutBoresight.ROTATE)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oAzEl)
            oAzEl.convert_to(OrientationType.AZ_EL)
            if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
                oAzEl.convert_to(OrientationType.EULER_ANGLES)
            if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
                oAzEl.convert_to(OrientationType.QUATERNION)
            if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
                oAzEl.convert_to(OrientationType.YPR_ANGLES)
            with pytest.raises(Exception):
                oAzEl.azimuth = 1234.5
            with pytest.raises(Exception):
                oAzEl.elevation = -1234.5

        if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
            oEulerAngles: "IOrientationEulerAngles" = IOrientationEulerAngles(
                oOrientation.convert_to(OrientationType.EULER_ANGLES)
            )
            Assert.assertIsNotNone(oEulerAngles)
            oEulerAngles.assign(oOrientation)
            self.m_logger.WriteLine6("\tNew orientation type is: {0}", oEulerAngles.orientation_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oEulerAngles)
            oEulerAngles.a = 123.45
            oEulerAngles.b = 234.51
            oEulerAngles.c = 345.12
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_121
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_123
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_131
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_132
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_212
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_213
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_231
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_232
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_312
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_313
            oEulerAngles.sequence = EulerOrientationSequenceType.SEQUENCE_321
            oEulerAngles.assign_euler_angles(EulerOrientationSequenceType.SEQUENCE_323, 123.45, 234.51, 345.12)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oEulerAngles)
            oEulerAngles.convert_to(OrientationType.EULER_ANGLES)
            if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
                oEulerAngles.convert_to(OrientationType.AZ_EL)
            if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
                oEulerAngles.convert_to(OrientationType.QUATERNION)
            if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
                oEulerAngles.convert_to(OrientationType.YPR_ANGLES)
            with pytest.raises(Exception):
                oEulerAngles.a = 1234.5
            with pytest.raises(Exception):
                oEulerAngles.b = -1234.5
            with pytest.raises(Exception):
                oEulerAngles.c = 1234.5

        if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
            oQuaternion: "IOrientationQuaternion" = IOrientationQuaternion(
                oOrientation.convert_to(OrientationType.QUATERNION)
            )
            Assert.assertIsNotNone(oQuaternion)
            oQuaternion.assign(oOrientation)
            self.m_logger.WriteLine6("\tNew orientation type is: {0}", oQuaternion.orientation_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oQuaternion)
            oQuaternion.qx = 0.123456789
            oQuaternion.qy = 0.987654321
            oQuaternion.qz = 0.3456
            oQuaternion.qs = 0.6543
            oQuaternion.assign_quaternion(0.123456789, 0.987654321, 0.3456, 0.6543)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oQuaternion)
            oQuaternion.convert_to(OrientationType.QUATERNION)
            if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
                oQuaternion.convert_to(OrientationType.AZ_EL)
            if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
                oQuaternion.convert_to(OrientationType.EULER_ANGLES)
            if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
                oQuaternion.convert_to(OrientationType.YPR_ANGLES)
            with pytest.raises(Exception):
                oQuaternion.qx = 1.2345
            with pytest.raises(Exception):
                oQuaternion.qy = -1.2345
            with pytest.raises(Exception):
                oQuaternion.qz = 1.2345
            with pytest.raises(Exception):
                oQuaternion.qs = -1.2345

        if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
            oYPRAngles: "IOrientationYPRAngles" = IOrientationYPRAngles(
                oOrientation.convert_to(OrientationType.YPR_ANGLES)
            )
            Assert.assertIsNotNone(oYPRAngles)
            oYPRAngles.assign(oOrientation)
            self.m_logger.WriteLine6("\tNew orientation type is: {0}", oYPRAngles.orientation_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oYPRAngles)
            oYPRAngles.yaw = 123.45
            oYPRAngles.pitch = 234.51
            oYPRAngles.roll = 345.12
            oYPRAngles.sequence = YPRAnglesSequence.PRY
            oYPRAngles.sequence = YPRAnglesSequence.PYR
            oYPRAngles.sequence = YPRAnglesSequence.RPY
            oYPRAngles.sequence = YPRAnglesSequence.RYP
            oYPRAngles.sequence = YPRAnglesSequence.YPR
            oYPRAngles.assign_ypr_angles(YPRAnglesSequence.YRP, 123.45, 234.51, 345.12)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oYPRAngles)
            oYPRAngles.convert_to(OrientationType.YPR_ANGLES)
            if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
                oYPRAngles.convert_to(OrientationType.AZ_EL)
            if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
                oYPRAngles.convert_to(OrientationType.EULER_ANGLES)
            if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
                oYPRAngles.convert_to(OrientationType.QUATERNION)
            with pytest.raises(Exception):
                oYPRAngles.yaw = 1234.5
            with pytest.raises(Exception):
                oYPRAngles.pitch = -1234.5
            with pytest.raises(Exception):
                oYPRAngles.roll = 1234.5

        if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
            oOrientation.assign_az_el(85.4, 34.5, AzElAboutBoresight.ROTATE)
            self.Display(oOrientation)
            pAzEl: "IOrientationAzEl" = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))
            Assert.assertEqual(85.4, pAzEl.azimuth)
            Assert.assertAlmostEqual(34.5, float(pAzEl.elevation), delta=1e-06)
            Assert.assertEqual(AzElAboutBoresight.ROTATE, pAzEl.about_boresight)

        if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
            oOrientation.assign_euler_angles(EulerOrientationSequenceType.SEQUENCE_121, 34.45, 56.51, 76.12)
            pEuler: "IOrientationEulerAngles" = IOrientationEulerAngles(
                oOrientation.convert_to(OrientationType.EULER_ANGLES)
            )
            self.Display(pEuler)
            pEuler.sequence = EulerOrientationSequenceType.SEQUENCE_121
            Assert.assertEqual(EulerOrientationSequenceType.SEQUENCE_121, pEuler.sequence)
            Assert.assertAlmostEqual(34.45, float(pEuler.a), delta=0.001)
            Assert.assertAlmostEqual(56.51, float(pEuler.b), delta=0.001)
            Assert.assertAlmostEqual(76.12, float(pEuler.c), delta=0.001)

        if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
            oOrientation.assign_quaternion(0, 0, 0, 1)
            self.Display(oOrientation)

        if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
            oOrientation.assign_ypr_angles(YPRAnglesSequence.YRP, 123.45, 234.51, 345.12)
            self.Display(oOrientation)

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        self.m_logger.WriteLine("----- ORIENTATION TEST ----- END -----")


# ////////////////////////////////////////////////////////////////////////
class DirectionsTest(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Display method
    def Display(self, oDirection: "IDirection"):
        Assert.assertIsNotNone(oDirection)
        if oDirection.direction_type == DirectionType.EULER:
            oEuler: "DirectionEuler" = DirectionEuler(oDirection.convert_to(DirectionType.EULER))
            Assert.assertIsNotNone(oEuler)
            self.m_logger.WriteLine6("\t\tEuler B is: {0}", oEuler.b)
            self.m_logger.WriteLine6("\t\tEuler C is: {0}", oEuler.c)
            self.m_logger.WriteLine6("\t\tEuler Sequence is: {0}", oEuler.sequence)
        elif oDirection.direction_type == DirectionType.PR:
            oPR: "DirectionPR" = DirectionPR(oDirection.convert_to(DirectionType.PR))
            Assert.assertIsNotNone(oPR)
            self.m_logger.WriteLine6("\t\tPR Pitch is: {0}", oPR.pitch)
            self.m_logger.WriteLine6("\t\tPR Roll is: {0}", oPR.roll)
            self.m_logger.WriteLine6("\t\tPR Sequence is: {0}", oPR.sequence)
        elif oDirection.direction_type == DirectionType.RA_DEC:
            oRADec: "DirectionRADec" = DirectionRADec(oDirection.convert_to(DirectionType.RA_DEC))
            Assert.assertIsNotNone(oRADec)
            self.m_logger.WriteLine6("\t\tRADec Pitch is: {0}", oRADec.ra)
            self.m_logger.WriteLine6("\t\tRADec Roll is: {0}", oRADec.dec)
        elif oDirection.direction_type == DirectionType.XYZ:
            oXYZ: "DirectionXYZ" = DirectionXYZ(oDirection.convert_to(DirectionType.XYZ))
            Assert.assertIsNotNone(oXYZ)
            self.m_logger.WriteLine6("\t\tX is: {0}", oXYZ.x)
            self.m_logger.WriteLine6("\t\tY is: {0}", oXYZ.y)
            self.m_logger.WriteLine6("\t\tZ is: {0}", oXYZ.z)
        else:
            pass

    # endregion

    # region Run method
    def Run(self, oDirection: "IDirection"):
        self.m_logger.WriteLine("----- DIRECTION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oDirection)
        # DirectionType
        self.m_logger.WriteLine6("\tThe current DirectionType is: {0}", oDirection.direction_type)
        self.Display(oDirection)

        # Euler direction test
        oEuler: "DirectionEuler" = DirectionEuler(oDirection.convert_to(DirectionType.EULER))
        Assert.assertIsNotNone(oEuler)
        oEuler.assign(oDirection)
        oDirection.convert_to(DirectionType.PR)
        oDirection.convert_to(DirectionType.RA_DEC)
        oDirection.convert_to(DirectionType.XYZ)
        self.m_logger.WriteLine6("\tNew direction type is: {0}", oEuler.direction_type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oEuler)
        oEuler.b = 234.5
        oEuler.c = 54.321
        oEuler.sequence = EulerDirectionSequence.SEQUENCE_32
        oEuler.assign_euler(234.5, 54.321, EulerDirectionSequence.SEQUENCE_32)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oEuler)

        # PR direction test
        oPR: "DirectionPR" = DirectionPR(oEuler.convert_to(DirectionType.PR))
        Assert.assertIsNotNone(oPR)
        oPR.assign(oEuler)
        oEuler.convert_to(DirectionType.EULER)
        oEuler.convert_to(DirectionType.RA_DEC)
        oEuler.convert_to(DirectionType.XYZ)
        self.m_logger.WriteLine6("\tNew direction type is: {0}", oPR.direction_type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oPR)
        oPR.pitch = 123.456
        oPR.roll = -54.321
        with pytest.raises(Exception):
            oPR.sequence = PRSequence.PR
        oPR.assign_pr(123.456, -54.321)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oPR)

        # RADec direction test
        oRADec: "DirectionRADec" = DirectionRADec(oPR.convert_to(DirectionType.RA_DEC))
        Assert.assertIsNotNone(oRADec)
        oPR.convert_to(DirectionType.EULER)
        oPR.convert_to(DirectionType.PR)
        oPR.convert_to(DirectionType.XYZ)
        oRADec.assign(oPR)
        self.m_logger.WriteLine6("\tNew direction type is: {0}", oRADec.direction_type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oRADec)
        oRADec.ra = 123.456789
        oRADec.dec = 9.87654321
        oRADec.assign_ra_dec(123.456789, 9.87654321)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oRADec)

        # XYZ direction test
        oXYZ: "DirectionXYZ" = DirectionXYZ(oRADec.convert_to(DirectionType.XYZ))
        Assert.assertIsNotNone(oXYZ)
        oXYZ.assign(oRADec)
        oRADec.convert_to(DirectionType.EULER)
        oRADec.convert_to(DirectionType.PR)
        oRADec.convert_to(DirectionType.RA_DEC)
        self.m_logger.WriteLine6("\tNew direction type is: {0}", oXYZ.direction_type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oXYZ)
        oXYZ.x = 0.190988679940043
        oXYZ.y = -0.743582379766568
        oXYZ.z = 0.640787459798838
        oXYZ.assign_xyz(0.190988679940043, -0.743582379766568, 0.640787459798838)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oXYZ)
        oEuler = DirectionEuler(oXYZ.convert_to(DirectionType.EULER))
        Assert.assertIsNotNone(oEuler)
        oDirection.assign(oEuler)
        oXYZ.convert_to(DirectionType.XYZ)
        oXYZ.convert_to(DirectionType.PR)
        oXYZ.convert_to(DirectionType.RA_DEC)

        #        #			 *        #			 * Testing the helper methods to convert to desired direction type and set its values in one call        #			 *        #			 *
        oDirection.assign_euler(234.5, 54.321, EulerDirectionSequence.SEQUENCE_32)
        self.Display(oDirection.convert_to(DirectionType.EULER))
        # SetAsPR
        oDirection.assign_pr(123.456, -54.321)
        self.Display(oDirection.convert_to(DirectionType.PR))
        # SetAsRADec
        oDirection.assign_ra_dec(123.456789, 9.87654321)
        self.Display(oDirection.convert_to(DirectionType.RA_DEC))
        # SetAsXYZ
        oDirection.assign_xyz(0.190988679940043, -0.743582379766568, 0.640787459798838)
        self.Display(oDirection.convert_to(DirectionType.XYZ))
        self.m_logger.WriteLine("----- DIRECTION TEST ----- END -----")


# ////////////////////////////////////////////////////////////////////////
class PositionTest(object):
    # region Positions enum
    class Positions:
        Cartesian = 1
        Cylindrical = 2
        Geocentric = 4
        Geodetic = 8
        Spherical = 16
        All = 31

    def __init__(self, oUnits: "UnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Display method
    def Display(self, oPosition: "IPosition"):
        Assert.assertIsNotNone(oPosition)
        if oPosition.position_type == PositionType.CARTESIAN:
            oCartesian: "Cartesian" = Cartesian(oPosition.convert_to(PositionType.CARTESIAN))
            Assert.assertIsNotNone(oCartesian)
            self.m_logger.WriteLine6("\t\tCartesian X is: {0}", oCartesian.x)
            self.m_logger.WriteLine6("\t\tCartesian Y is: {0}", oCartesian.y)
            self.m_logger.WriteLine6("\t\tCartesian Z is: {0}", oCartesian.z)
        elif oPosition.position_type == PositionType.CYLINDRICAL:
            oCylindrical: "Cylindrical" = Cylindrical(oPosition.convert_to(PositionType.CYLINDRICAL))
            Assert.assertIsNotNone(oCylindrical)
            self.m_logger.WriteLine6("\t\tCylindrical Radius is: {0}", oCylindrical.radius)
            self.m_logger.WriteLine6("\t\tCylindrical Z is: {0}", oCylindrical.z)
            self.m_logger.WriteLine6("\t\tCylindrical Lon is: {0}", oCylindrical.longitude)
        elif oPosition.position_type == PositionType.GEOCENTRIC:
            oGeocentric: "Geocentric" = Geocentric(oPosition.convert_to(PositionType.GEOCENTRIC))
            Assert.assertIsNotNone(oGeocentric)
            self.m_logger.WriteLine6("\t\tGeocentric Lat is: {0}", oGeocentric.latitude)
            self.m_logger.WriteLine6("\t\tGeocentric Lon is: {0}", oGeocentric.longitude)
            self.m_logger.WriteLine6("\t\tGeocentric Alt is: {0}", oGeocentric.altitude)
        elif oPosition.position_type == PositionType.GEODETIC:
            oGeodetic: "Geodetic" = Geodetic(oPosition.convert_to(PositionType.GEODETIC))
            Assert.assertIsNotNone(oGeodetic)
            self.m_logger.WriteLine6("\t\tGeodetic Lat is: {0}", oGeodetic.latitude)
            self.m_logger.WriteLine6("\t\tGeodetic Lon is: {0}", oGeodetic.longitude)
            self.m_logger.WriteLine6("\t\tGeodetic Alt is: {0}", oGeodetic.altitude)
        elif oPosition.position_type == PositionType.SPHERICAL:
            oSpherical: "Spherical" = Spherical(oPosition.convert_to(PositionType.SPHERICAL))
            Assert.assertIsNotNone(oSpherical)
            self.m_logger.WriteLine6("\t\tSpherical Lat is: {0}", oSpherical.latitude)
            self.m_logger.WriteLine6("\t\tSpherical Lon is: {0}", oSpherical.longitude)
            self.m_logger.WriteLine6("\t\tSpherical Radius is: {0}", oSpherical.radius)
        else:
            Assert.fail("Invalid Position type!")

    # endregion

    # region Run method
    def Run(self, oPosition: "IPosition", eTypes):
        self.m_logger.WriteLine("----- POSITION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oPosition)
        self.m_logger.WriteLine6("\tPosition test for: {0} positions", eTypes)
        # set DistanceUnit
        strDistanceUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit format is: {0}", strDistanceUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "m")
        self.m_logger.WriteLine5(
            "\tThe new DistanceUnit format is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("m", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # set LatitudeUnit
        strLatitudeUnit: str = self.m_oUnits.get_current_unit_abbrv("LatitudeUnit")
        self.m_logger.WriteLine5("\tThe current LatitudeUnit format is: {0}", strLatitudeUnit)
        self.m_oUnits.set_current_unit("LatitudeUnit", "rad")
        self.m_logger.WriteLine5(
            "\tThe new LatitudeUnit format is: {0}", self.m_oUnits.get_current_unit_abbrv("LatitudeUnit")
        )
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("LatitudeUnit"))
        # set LongitudeUnit
        strLongitudeUnit: str = self.m_oUnits.get_current_unit_abbrv("LongitudeUnit")
        self.m_logger.WriteLine5("\tThe current LongitudeUnit format is: {0}", strLongitudeUnit)
        self.m_oUnits.set_current_unit("LongitudeUnit", "rad")
        self.m_logger.WriteLine5(
            "\tThe new LongitudeUnit format is: {0}", self.m_oUnits.get_current_unit_abbrv("LongitudeUnit")
        )
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))
        # set AngleUnit
        strAngleUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit format is: {0}", strAngleUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5(
            "\tThe new AngleUnit format is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        )
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        self.m_logger.WriteLine6("\tCurrent position type is: {0}", oPosition.position_type)
        self.Display(oPosition)
        if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
            oCartesian: "Cartesian" = Cartesian(oPosition.convert_to(PositionType.CARTESIAN))
            Assert.assertIsNotNone(oCartesian)
            oCartesian.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oCartesian.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oCartesian)
            oCartesian.x = 1234.5
            oCartesian.y = 54.321
            oCartesian.z = 789.012
            oCartesian.assign_cartesian(1234.5, 54.321, 789.012)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oCartesian)
            with pytest.raises(Exception):
                oCartesian.x = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            with pytest.raises(Exception):
                oCartesian.y = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            with pytest.raises(Exception):
                oCartesian.z = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            oCartesian.convert_to(PositionType.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oCartesian.convert_to(PositionType.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oCartesian.convert_to(PositionType.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oCartesian.convert_to(PositionType.GEODETIC)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oCartesian.convert_to(PositionType.SPHERICAL)

        if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
            oCylindrical: "Cylindrical" = Cylindrical(oPosition.convert_to(PositionType.CYLINDRICAL))
            Assert.assertIsNotNone(oCylindrical)
            oCylindrical.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oCylindrical.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oCylindrical)
            oCylindrical.radius = 12203.4
            oCylindrical.z = 3513.17
            oCylindrical.longitude = 1.23
            oCylindrical.assign_cylindrical(12203.4, 3513.17, 1.23)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oCylindrical)
            with pytest.raises(Exception):
                oCylindrical.radius = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            with pytest.raises(Exception):
                oCylindrical.z = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            with pytest.raises(Exception):
                oCylindrical.longitude = 6.78

            oCylindrical.convert_to(PositionType.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oCylindrical.convert_to(PositionType.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oCylindrical.convert_to(PositionType.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oCylindrical.convert_to(PositionType.GEODETIC)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oCylindrical.convert_to(PositionType.SPHERICAL)

        if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
            oGeocentric: "Geocentric" = Geocentric(oPosition.convert_to(PositionType.GEOCENTRIC))
            Assert.assertIsNotNone(oGeocentric)
            oGeocentric.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oGeocentric.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oGeocentric)
            oGeocentric.latitude = 1.234
            oGeocentric.longitude = 2.345
            oGeocentric.altitude = 12.34
            oGeocentric.assign_geocentric(1.234, 2.345, 12.34)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oGeocentric)
            with pytest.raises(Exception):
                oGeocentric.latitude = 2.34
            with pytest.raises(Exception):
                oGeocentric.longitude = 6.78
            with pytest.raises(Exception):
                oGeocentric.altitude = 6780000000000.0

            oGeocentric.convert_to(PositionType.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oGeocentric.convert_to(PositionType.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oGeocentric.convert_to(PositionType.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oGeocentric.convert_to(PositionType.GEODETIC)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oGeocentric.convert_to(PositionType.SPHERICAL)

        if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
            oGeodetic: "Geodetic" = Geodetic(oPosition.convert_to(PositionType.GEODETIC))
            Assert.assertIsNotNone(oGeodetic)
            oGeodetic.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oGeodetic.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oGeodetic)
            oGeodetic.latitude = 0.190988679940043
            oGeodetic.longitude = -0.743582379766568
            oGeodetic.altitude = 0.640787459798838
            oGeodetic.assign_geodetic(0.190988679940043, -0.743582379766568, 0.640787459798838)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oGeodetic)
            with pytest.raises(Exception):
                oGeodetic.latitude = 2.34
            with pytest.raises(Exception):
                oGeodetic.longitude = 6.78
            with pytest.raises(Exception):
                oGeodetic.altitude = 6780000000000.0

            oGeodetic.convert_to(PositionType.GEODETIC)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oGeodetic.convert_to(PositionType.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oGeodetic.convert_to(PositionType.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oGeodetic.convert_to(PositionType.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oGeodetic.convert_to(PositionType.SPHERICAL)

        if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
            oSpherical: "Spherical" = Spherical(oPosition.convert_to(PositionType.SPHERICAL))
            Assert.assertIsNotNone(oSpherical)
            oSpherical.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oSpherical.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oSpherical)
            oSpherical.latitude = 1
            oSpherical.longitude = 2
            oSpherical.radius = 6355753
            oSpherical.assign_spherical(1, 2, 6355753)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oSpherical)
            with pytest.raises(Exception):
                oSpherical.latitude = 2.34
            with pytest.raises(Exception):
                oSpherical.longitude = 6.78
            with pytest.raises(Exception):
                oSpherical.radius = 67800000000000000000000000.0

            oSpherical.convert_to(PositionType.SPHERICAL)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oSpherical.convert_to(PositionType.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oSpherical.convert_to(PositionType.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oSpherical.convert_to(PositionType.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oSpherical.convert_to(PositionType.GEODETIC)

        if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
            # SetAsCartesian
            # oPosition.AssignCartesian(0.190988679940043, -0.743582379766568, 0.640787459798838); // See 35836
            oPosition.assign_cartesian(6654000, 230000, 113000)
            self.Display(oPosition.convert_to(PositionType.CARTESIAN))

        if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
            # SetAsCylindrical
            oPosition.assign_cylindrical(1, 500, 5)
            self.Display(oPosition.convert_to(PositionType.CYLINDRICAL))

        if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
            # SetAsGeocentric
            oPosition.assign_geocentric(0, 0, 1)
            self.Display(oPosition.convert_to(PositionType.GEOCENTRIC))

        if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
            # SetAsGeodetic
            oPosition.assign_geodetic(0.190988679940043, -0.743582379766568, 0.640787459798838)
            self.Display(oPosition.convert_to(PositionType.GEODETIC))

        if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
            # SetAsSpherical
            oPosition.assign_spherical(-1, -1, 600355753)
            self.Display(oPosition.convert_to(PositionType.SPHERICAL))

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strAngleUnit)
        self.m_logger.WriteLine5(
            "\tThe restored AngleUnit format is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        )
        Assert.assertEqual(strAngleUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5(
            "\tThe restored DistanceUnit format is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual(strDistanceUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))
        # restore LatitudeUnit
        self.m_oUnits.set_current_unit("LatitudeUnit", strLatitudeUnit)
        self.m_logger.WriteLine5(
            "\tThe restored LatitudeUnit format is: {0}", self.m_oUnits.get_current_unit_abbrv("LatitudeUnit")
        )
        Assert.assertEqual(strLatitudeUnit, self.m_oUnits.get_current_unit_abbrv("LatitudeUnit"))
        # restore LongitudeUnit
        self.m_oUnits.set_current_unit("LongitudeUnit", strLongitudeUnit)
        self.m_logger.WriteLine5(
            "\tThe restored LongitudeUnit format is: {0}", self.m_oUnits.get_current_unit_abbrv("LongitudeUnit")
        )
        Assert.assertEqual(strLongitudeUnit, self.m_oUnits.get_current_unit_abbrv("LongitudeUnit"))
        self.m_logger.WriteLine("----- POSITION TEST ----- END -----")


# ////////////////////////////////////////////////////////////////////////
class LLAPositionTest(object):
    def __init__(self, *args, **kwargs):
        self.m_logger = Logger.Instance

    # endregion

    # region Display method
    def Display(self, oPosition: "ILatitudeLongitudeAltitudePosition"):
        Assert.assertIsNotNone(oPosition)
        if oPosition.type == DeticPositionType.CENTRIC:
            llaGeocentric: "LatitudeLongitudeAltitudeCentric" = LatitudeLongitudeAltitudeCentric(
                oPosition.convert_to(DeticPositionType.CENTRIC)
            )
            Assert.assertIsNotNone(llaGeocentric)
            self.m_logger.WriteLine6("\t\tGeocentric Lat is: {0}", llaGeocentric.latitude)
            self.m_logger.WriteLine6("\t\tGeocentric Lon is: {0}", llaGeocentric.longitude)
            self.m_logger.WriteLine6("\t\tGeocentric Rad is: {0}", llaGeocentric.radius)

            llaGeocentric.assign_centric(10.0, 20.0, 10000.0)
            Assert.assertEqual(10.0, llaGeocentric.latitude)
            Assert.assertEqual(20.0, llaGeocentric.longitude)
            Assert.assertEqual(10000.0, llaGeocentric.radius)

            llaGeocentric.assign_detic(40.0, 50.0, 60.0)
            Assert.assertAlmostEqual(39.81, llaGeocentric.latitude, delta=0.01)
            Assert.assertAlmostEqual(50.0, llaGeocentric.longitude, delta=0.01)
            Assert.assertAlmostEqual(6429, llaGeocentric.radius, delta=1.0)
        elif oPosition.type == DeticPositionType.DETIC:
            llaGeodetic: "LatitudeLongitudeAltitudeDetic" = LatitudeLongitudeAltitudeDetic(
                oPosition.convert_to(DeticPositionType.DETIC)
            )
            Assert.assertIsNotNone(llaGeodetic)
            self.m_logger.WriteLine6("\t\tGeodetic Lat is: {0}", llaGeodetic.latitude)
            self.m_logger.WriteLine6("\t\tGeodetic Lon is: {0}", llaGeodetic.longitude)
            self.m_logger.WriteLine6("\t\tGeodetic Alt is: {0}", llaGeodetic.altitude)

            llaGeodetic.assign_centric(10.0, 20.0, 10000.0)
            Assert.assertAlmostEqual(10.04, llaGeodetic.latitude, delta=0.01)
            Assert.assertAlmostEqual(19.95, llaGeodetic.longitude, delta=0.1)
            Assert.assertAlmostEqual(3622, llaGeodetic.altitude, delta=1.0)

            llaGeodetic.assign_detic(40.0, 50.0, 10000.0)
            Assert.assertEqual(40.0, llaGeodetic.latitude)
            Assert.assertEqual(50.0, llaGeodetic.longitude)
            Assert.assertEqual(10000.0, llaGeodetic.altitude)
        else:
            Assert.fail("Invalid LLA Position type: {0}", oPosition.type)

    # endregion

    # region Run method
    def Run(self, oPosition: "ILatitudeLongitudeAltitudePosition"):
        self.m_logger.WriteLine("----- LLA POSITION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oPosition)
        # Type
        self.m_logger.WriteLine6("\tThe current Type is: {0}", oPosition.type)
        self.Display(oPosition)
        # Geocentric
        # ConvertTo
        oGeocentric: "LatitudeLongitudeAltitudeCentric" = LatitudeLongitudeAltitudeCentric(
            oPosition.convert_to(DeticPositionType.CENTRIC)
        )
        Assert.assertIsNotNone(oGeocentric)
        # Assign
        oGeocentric.assign(oPosition)
        oPosition.convert_to(DeticPositionType.DETIC)
        self.m_logger.WriteLine6("\tThe new Type is: {0}", oGeocentric.type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oGeocentric)
        # Lat
        oGeocentric.latitude = 23.45
        Assert.assertAlmostEqual(23.45, oGeocentric.latitude, delta=0.01)
        with pytest.raises(Exception):
            oGeocentric.latitude = -321
        # Lon
        oGeocentric.longitude = 54.321
        Assert.assertAlmostEqual(54.321, oGeocentric.longitude, delta=0.001)
        with pytest.raises(Exception):
            oGeocentric.longitude = -321
        # Rad
        oGeocentric.radius = 12345.6
        Assert.assertAlmostEqual(12345.6, oGeocentric.radius, delta=0.01)
        with pytest.raises(Exception):
            oGeocentric.radius = -321
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oGeocentric)
        # Geodetic
        # ConvertTo
        oGeodetic: "LatitudeLongitudeAltitudeDetic" = LatitudeLongitudeAltitudeDetic(
            oGeocentric.convert_to(DeticPositionType.DETIC)
        )
        Assert.assertIsNotNone(oGeodetic)
        # Assign
        oGeodetic.assign(oGeocentric)
        oGeodetic.convert_to(DeticPositionType.CENTRIC)
        self.m_logger.WriteLine6("\tThe new Type is: {0}", oGeodetic.type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oGeodetic)
        # Lat
        oGeodetic.latitude = 12.3456
        Assert.assertAlmostEqual(12.3456, oGeodetic.latitude, delta=0.0001)
        with pytest.raises(Exception):
            oGeodetic.latitude = -321
        # Lon
        oGeodetic.longitude = -54.321
        Assert.assertAlmostEqual(-54.321, oGeodetic.longitude, delta=0.001)
        with pytest.raises(Exception):
            oGeodetic.longitude = -321
        # Alt
        oGeodetic.altitude = 123.456
        Assert.assertAlmostEqual(123.456, oGeodetic.altitude, delta=0.001)
        with pytest.raises(Exception):
            oGeodetic.altitude = -321
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oGeodetic)
        with pytest.raises(Exception):
            oPosition.convert_to(DeticPositionType.UNKNOWN)

        # Testing the helper methods to convert to desired LLA position type and set its values in one call
        # SetAsGeocentric
        oPosition.assign_centric(23.45, 54.321, 12345.6)
        self.Display(oPosition.convert_to(DeticPositionType.CENTRIC))
        # SetAsGeodetic
        oPosition.assign_detic(12.3456, -54.321, 123.456)
        self.Display(oPosition.convert_to(DeticPositionType.DETIC))
        self.m_logger.WriteLine("----- LLA POSITION TEST ----- END -----")

    # endregion
    # endregion
