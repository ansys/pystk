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
    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # region Display method
    def Display(self, oOrientation: "IOrientation"):
        Assert.assertIsNotNone(oOrientation)
        if oOrientation.orientation_type == ORIENTATION_TYPE.AZ_EL:
            oAzEl: "IOrientationAzEl" = clr.Convert(oOrientation.convert_to(ORIENTATION_TYPE.AZ_EL), IOrientationAzEl)
            Assert.assertIsNotNone(oAzEl)
            self.m_logger.WriteLine6("\t\tAzEl Azimuth is: {0}", oAzEl.azimuth)
            self.m_logger.WriteLine6("\t\tAzEl Elevation is: {0}", oAzEl.elevation)
            self.m_logger.WriteLine6("\t\tAzEl AboutBoresight is: {0}", oAzEl.about_boresight)
        elif oOrientation.orientation_type == ORIENTATION_TYPE.EULER_ANGLES:
            oEulerAngles: "IOrientationEulerAngles" = clr.Convert(
                oOrientation.convert_to(ORIENTATION_TYPE.EULER_ANGLES), IOrientationEulerAngles
            )
            Assert.assertIsNotNone(oEulerAngles)
            self.m_logger.WriteLine6("\t\tEulerAngles A is: {0}", oEulerAngles.a)
            self.m_logger.WriteLine6("\t\tEulerAngles B is: {0}", oEulerAngles.b)
            self.m_logger.WriteLine6("\t\tEulerAngles C is: {0}", oEulerAngles.c)
            self.m_logger.WriteLine6("\t\tEulerAngles Sequence is: {0}", oEulerAngles.sequence)
        elif oOrientation.orientation_type == ORIENTATION_TYPE.QUATERNION:
            oQuaternion: "IOrientationQuaternion" = clr.Convert(
                oOrientation.convert_to(ORIENTATION_TYPE.QUATERNION), IOrientationQuaternion
            )
            Assert.assertIsNotNone(oQuaternion)
            self.m_logger.WriteLine6("\t\tQuaternion QX is: {0}", oQuaternion.qx)
            self.m_logger.WriteLine6("\t\tQuaternion QY is: {0}", oQuaternion.qy)
            self.m_logger.WriteLine6("\t\tQuaternion QZ is: {0}", oQuaternion.qz)
            self.m_logger.WriteLine6("\t\tQuaternion QS is: {0}", oQuaternion.qs)
        elif oOrientation.orientation_type == ORIENTATION_TYPE.YPR_ANGLES:
            oYPRAngles: "IOrientationYPRAngles" = clr.Convert(
                oOrientation.convert_to(ORIENTATION_TYPE.YPR_ANGLES), IOrientationYPRAngles
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
            oAzEl: "IOrientationAzEl" = clr.Convert(oOrientation.convert_to(ORIENTATION_TYPE.AZ_EL), IOrientationAzEl)
            Assert.assertIsNotNone(oAzEl)
            oAzEl.assign(oOrientation)
            self.m_logger.WriteLine6("\tNew orientation type is: {0}", oAzEl.orientation_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oAzEl)
            oAzEl.azimuth = 123.45
            oAzEl.elevation = 54.321
            oAzEl.about_boresight = AZ_EL_ABOUT_BORESIGHT.HOLD
            oAzEl.assign_az_el(123.45, 54.321, AZ_EL_ABOUT_BORESIGHT.ROTATE)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oAzEl)
            oAzEl.convert_to(ORIENTATION_TYPE.AZ_EL)
            if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
                oAzEl.convert_to(ORIENTATION_TYPE.EULER_ANGLES)
            if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
                oAzEl.convert_to(ORIENTATION_TYPE.QUATERNION)
            if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
                oAzEl.convert_to(ORIENTATION_TYPE.YPR_ANGLES)

            def action1():
                oAzEl.azimuth = 1234.5

            TryCatchAssertBlock.DoAssert("", action1)

            def action2():
                oAzEl.elevation = -1234.5

            TryCatchAssertBlock.DoAssert("", action2)

        if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
            oEulerAngles: "IOrientationEulerAngles" = clr.Convert(
                oOrientation.convert_to(ORIENTATION_TYPE.EULER_ANGLES), IOrientationEulerAngles
            )
            Assert.assertIsNotNone(oEulerAngles)
            oEulerAngles.assign(oOrientation)
            self.m_logger.WriteLine6("\tNew orientation type is: {0}", oEulerAngles.orientation_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oEulerAngles)
            oEulerAngles.a = 123.45
            oEulerAngles.b = 234.51
            oEulerAngles.c = 345.12
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_121
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_123
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_131
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_132
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_212
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_213
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_231
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_232
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_312
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_313
            oEulerAngles.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_321
            oEulerAngles.assign_euler_angles(EULER_ORIENTATION_SEQUENCE.SEQUENCE_323, 123.45, 234.51, 345.12)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oEulerAngles)
            oEulerAngles.convert_to(ORIENTATION_TYPE.EULER_ANGLES)
            if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
                oEulerAngles.convert_to(ORIENTATION_TYPE.AZ_EL)
            if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
                oEulerAngles.convert_to(ORIENTATION_TYPE.QUATERNION)
            if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
                oEulerAngles.convert_to(ORIENTATION_TYPE.YPR_ANGLES)

            def action3():
                oEulerAngles.a = 1234.5

            TryCatchAssertBlock.DoAssert("", action3)

            def action4():
                oEulerAngles.b = -1234.5

            TryCatchAssertBlock.DoAssert("", action4)

            def action5():
                oEulerAngles.c = 1234.5

            TryCatchAssertBlock.DoAssert("", action5)

        if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
            oQuaternion: "IOrientationQuaternion" = clr.Convert(
                oOrientation.convert_to(ORIENTATION_TYPE.QUATERNION), IOrientationQuaternion
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
            oQuaternion.convert_to(ORIENTATION_TYPE.QUATERNION)
            if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
                oQuaternion.convert_to(ORIENTATION_TYPE.AZ_EL)
            if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
                oQuaternion.convert_to(ORIENTATION_TYPE.EULER_ANGLES)
            if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
                oQuaternion.convert_to(ORIENTATION_TYPE.YPR_ANGLES)

            def action6():
                oQuaternion.qx = 1.2345

            TryCatchAssertBlock.DoAssert("", action6)

            def action7():
                oQuaternion.qy = -1.2345

            TryCatchAssertBlock.DoAssert("", action7)

            def action8():
                oQuaternion.qz = 1.2345

            TryCatchAssertBlock.DoAssert("", action8)

            def action9():
                oQuaternion.qs = -1.2345

            TryCatchAssertBlock.DoAssert("", action9)

        if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
            oYPRAngles: "IOrientationYPRAngles" = clr.Convert(
                oOrientation.convert_to(ORIENTATION_TYPE.YPR_ANGLES), IOrientationYPRAngles
            )
            Assert.assertIsNotNone(oYPRAngles)
            oYPRAngles.assign(oOrientation)
            self.m_logger.WriteLine6("\tNew orientation type is: {0}", oYPRAngles.orientation_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oYPRAngles)
            oYPRAngles.yaw = 123.45
            oYPRAngles.pitch = 234.51
            oYPRAngles.roll = 345.12
            oYPRAngles.sequence = YPR_ANGLES_SEQUENCE.PRY
            oYPRAngles.sequence = YPR_ANGLES_SEQUENCE.PYR
            oYPRAngles.sequence = YPR_ANGLES_SEQUENCE.RPY
            oYPRAngles.sequence = YPR_ANGLES_SEQUENCE.RYP
            oYPRAngles.sequence = YPR_ANGLES_SEQUENCE.YPR
            oYPRAngles.assign_ypr_angles(YPR_ANGLES_SEQUENCE.YRP, 123.45, 234.51, 345.12)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oYPRAngles)
            oYPRAngles.convert_to(ORIENTATION_TYPE.YPR_ANGLES)
            if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
                oYPRAngles.convert_to(ORIENTATION_TYPE.AZ_EL)
            if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
                oYPRAngles.convert_to(ORIENTATION_TYPE.EULER_ANGLES)
            if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
                oYPRAngles.convert_to(ORIENTATION_TYPE.QUATERNION)

            def action10():
                oYPRAngles.yaw = 1234.5

            TryCatchAssertBlock.DoAssert("", action10)

            def action11():
                oYPRAngles.pitch = -1234.5

            TryCatchAssertBlock.DoAssert("", action11)

            def action12():
                oYPRAngles.roll = 1234.5

            TryCatchAssertBlock.DoAssert("", action12)

        if ((eTypes & Orientations.AzEl)) == Orientations.AzEl:
            oOrientation.assign_az_el(85.4, 34.5, AZ_EL_ABOUT_BORESIGHT.ROTATE)
            self.Display(oOrientation)
            pAzEl: "IOrientationAzEl" = clr.Convert(oOrientation.convert_to(ORIENTATION_TYPE.AZ_EL), IOrientationAzEl)
            Assert.assertEqual(85.4, pAzEl.azimuth)
            Assert.assertAlmostEqual(34.5, float(pAzEl.elevation), delta=1e-06)
            Assert.assertEqual(AZ_EL_ABOUT_BORESIGHT.ROTATE, pAzEl.about_boresight)

        if ((eTypes & Orientations.EulerAngles)) == Orientations.EulerAngles:
            oOrientation.assign_euler_angles(EULER_ORIENTATION_SEQUENCE.SEQUENCE_121, 34.45, 56.51, 76.12)
            pEuler: "IOrientationEulerAngles" = clr.Convert(
                oOrientation.convert_to(ORIENTATION_TYPE.EULER_ANGLES), IOrientationEulerAngles
            )
            self.Display(pEuler)
            pEuler.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_121
            Assert.assertEqual(EULER_ORIENTATION_SEQUENCE.SEQUENCE_121, pEuler.sequence)
            Assert.assertAlmostEqual(34.45, float(pEuler.a), delta=0.001)
            Assert.assertAlmostEqual(56.51, float(pEuler.b), delta=0.001)
            Assert.assertAlmostEqual(76.12, float(pEuler.c), delta=0.001)

        if ((eTypes & Orientations.Quaternion)) == Orientations.Quaternion:
            oOrientation.assign_quaternion(0, 0, 0, 1)
            self.Display(oOrientation)

        if ((eTypes & Orientations.YPRAngles)) == Orientations.YPRAngles:
            oOrientation.assign_ypr_angles(YPR_ANGLES_SEQUENCE.YRP, 123.45, 234.51, 345.12)
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
        if oDirection.direction_type == DIRECTION_TYPE.EULER:
            oEuler: "IDirectionEuler" = clr.Convert(oDirection.convert_to(DIRECTION_TYPE.EULER), IDirectionEuler)
            Assert.assertIsNotNone(oEuler)
            self.m_logger.WriteLine6("\t\tEuler B is: {0}", oEuler.b)
            self.m_logger.WriteLine6("\t\tEuler C is: {0}", oEuler.c)
            self.m_logger.WriteLine6("\t\tEuler Sequence is: {0}", oEuler.sequence)
        elif oDirection.direction_type == DIRECTION_TYPE.PR:
            oPR: "IDirectionPR" = clr.Convert(oDirection.convert_to(DIRECTION_TYPE.PR), IDirectionPR)
            Assert.assertIsNotNone(oPR)
            self.m_logger.WriteLine6("\t\tPR Pitch is: {0}", oPR.pitch)
            self.m_logger.WriteLine6("\t\tPR Roll is: {0}", oPR.roll)
            self.m_logger.WriteLine6("\t\tPR Sequence is: {0}", oPR.sequence)
        elif oDirection.direction_type == DIRECTION_TYPE.RA_DEC:
            oRADec: "IDirectionRADec" = clr.Convert(oDirection.convert_to(DIRECTION_TYPE.RA_DEC), IDirectionRADec)
            Assert.assertIsNotNone(oRADec)
            self.m_logger.WriteLine6("\t\tRADec Pitch is: {0}", oRADec.ra)
            self.m_logger.WriteLine6("\t\tRADec Roll is: {0}", oRADec.dec)
        elif oDirection.direction_type == DIRECTION_TYPE.XYZ:
            oXYZ: "IDirectionXYZ" = clr.Convert(oDirection.convert_to(DIRECTION_TYPE.XYZ), IDirectionXYZ)
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
        oEuler: "IDirectionEuler" = clr.Convert(oDirection.convert_to(DIRECTION_TYPE.EULER), IDirectionEuler)
        Assert.assertIsNotNone(oEuler)
        oEuler.assign(oDirection)
        oDirection.convert_to(DIRECTION_TYPE.PR)
        oDirection.convert_to(DIRECTION_TYPE.RA_DEC)
        oDirection.convert_to(DIRECTION_TYPE.XYZ)
        self.m_logger.WriteLine6("\tNew direction type is: {0}", oEuler.direction_type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oEuler)
        oEuler.b = 234.5
        oEuler.c = 54.321
        oEuler.sequence = EULER_DIRECTION_SEQUENCE.SEQUENCE_32
        oEuler.assign_euler(234.5, 54.321, EULER_DIRECTION_SEQUENCE.SEQUENCE_32)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oEuler)

        # PR direction test
        oPR: "IDirectionPR" = clr.Convert(oEuler.convert_to(DIRECTION_TYPE.PR), IDirectionPR)
        Assert.assertIsNotNone(oPR)
        oPR.assign(oEuler)
        oEuler.convert_to(DIRECTION_TYPE.EULER)
        oEuler.convert_to(DIRECTION_TYPE.RA_DEC)
        oEuler.convert_to(DIRECTION_TYPE.XYZ)
        self.m_logger.WriteLine6("\tNew direction type is: {0}", oPR.direction_type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oPR)
        oPR.pitch = 123.456
        oPR.roll = -54.321

        def action13():
            oPR.sequence = PR_SEQUENCE.PR

        TryCatchAssertBlock.DoAssert("", action13)
        oPR.assign_pr(123.456, -54.321)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oPR)

        # RADec direction test
        oRADec: "IDirectionRADec" = clr.Convert(oPR.convert_to(DIRECTION_TYPE.RA_DEC), IDirectionRADec)
        Assert.assertIsNotNone(oRADec)
        oPR.convert_to(DIRECTION_TYPE.EULER)
        oPR.convert_to(DIRECTION_TYPE.PR)
        oPR.convert_to(DIRECTION_TYPE.XYZ)
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
        oXYZ: "IDirectionXYZ" = clr.Convert(oRADec.convert_to(DIRECTION_TYPE.XYZ), IDirectionXYZ)
        Assert.assertIsNotNone(oXYZ)
        oXYZ.assign(oRADec)
        oRADec.convert_to(DIRECTION_TYPE.EULER)
        oRADec.convert_to(DIRECTION_TYPE.PR)
        oRADec.convert_to(DIRECTION_TYPE.RA_DEC)
        self.m_logger.WriteLine6("\tNew direction type is: {0}", oXYZ.direction_type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oXYZ)
        oXYZ.x = 0.190988679940043
        oXYZ.y = -0.743582379766568
        oXYZ.z = 0.640787459798838
        oXYZ.assign_xyz(0.190988679940043, -0.743582379766568, 0.640787459798838)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oXYZ)
        oEuler = clr.Convert(oXYZ.convert_to(DIRECTION_TYPE.EULER), IDirectionEuler)
        Assert.assertIsNotNone(oEuler)
        oDirection.assign(oEuler)
        oXYZ.convert_to(DIRECTION_TYPE.XYZ)
        oXYZ.convert_to(DIRECTION_TYPE.PR)
        oXYZ.convert_to(DIRECTION_TYPE.RA_DEC)

        #        #			 *        #			 * Testing the helper methods to convert to desired direction type and set its values in one call        #			 *        #			 *
        oDirection.assign_euler(234.5, 54.321, EULER_DIRECTION_SEQUENCE.SEQUENCE_32)
        self.Display(oDirection.convert_to(DIRECTION_TYPE.EULER))
        # SetAsPR
        oDirection.assign_pr(123.456, -54.321)
        self.Display(oDirection.convert_to(DIRECTION_TYPE.PR))
        # SetAsRADec
        oDirection.assign_ra_dec(123.456789, 9.87654321)
        self.Display(oDirection.convert_to(DIRECTION_TYPE.RA_DEC))
        # SetAsXYZ
        oDirection.assign_xyz(0.190988679940043, -0.743582379766568, 0.640787459798838)
        self.Display(oDirection.convert_to(DIRECTION_TYPE.XYZ))
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

    def __init__(self, oUnits: "IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Display method
    def Display(self, oPosition: "IPosition"):
        Assert.assertIsNotNone(oPosition)
        if oPosition.position_type == POSITION_TYPE.CARTESIAN:
            oCartesian: "ICartesian" = clr.Convert(oPosition.convert_to(POSITION_TYPE.CARTESIAN), ICartesian)
            Assert.assertIsNotNone(oCartesian)
            self.m_logger.WriteLine6("\t\tCartesian X is: {0}", oCartesian.x)
            self.m_logger.WriteLine6("\t\tCartesian Y is: {0}", oCartesian.y)
            self.m_logger.WriteLine6("\t\tCartesian Z is: {0}", oCartesian.z)
        elif oPosition.position_type == POSITION_TYPE.CYLINDRICAL:
            oCylindrical: "ICylindrical" = clr.Convert(oPosition.convert_to(POSITION_TYPE.CYLINDRICAL), ICylindrical)
            Assert.assertIsNotNone(oCylindrical)
            self.m_logger.WriteLine6("\t\tCylindrical Radius is: {0}", oCylindrical.radius)
            self.m_logger.WriteLine6("\t\tCylindrical Z is: {0}", oCylindrical.z)
            self.m_logger.WriteLine6("\t\tCylindrical Lon is: {0}", oCylindrical.lon)
        elif oPosition.position_type == POSITION_TYPE.GEOCENTRIC:
            oGeocentric: "IGeocentric" = clr.Convert(oPosition.convert_to(POSITION_TYPE.GEOCENTRIC), IGeocentric)
            Assert.assertIsNotNone(oGeocentric)
            self.m_logger.WriteLine6("\t\tGeocentric Lat is: {0}", oGeocentric.lat)
            self.m_logger.WriteLine6("\t\tGeocentric Lon is: {0}", oGeocentric.lon)
            self.m_logger.WriteLine6("\t\tGeocentric Alt is: {0}", oGeocentric.altitude)
        elif oPosition.position_type == POSITION_TYPE.GEODETIC:
            oGeodetic: "IGeodetic" = clr.Convert(oPosition.convert_to(POSITION_TYPE.GEODETIC), IGeodetic)
            Assert.assertIsNotNone(oGeodetic)
            self.m_logger.WriteLine6("\t\tGeodetic Lat is: {0}", oGeodetic.lat)
            self.m_logger.WriteLine6("\t\tGeodetic Lon is: {0}", oGeodetic.lon)
            self.m_logger.WriteLine6("\t\tGeodetic Alt is: {0}", oGeodetic.altitude)
        elif oPosition.position_type == POSITION_TYPE.SPHERICAL:
            oSpherical: "ISpherical" = clr.Convert(oPosition.convert_to(POSITION_TYPE.SPHERICAL), ISpherical)
            Assert.assertIsNotNone(oSpherical)
            self.m_logger.WriteLine6("\t\tSpherical Lat is: {0}", oSpherical.lat)
            self.m_logger.WriteLine6("\t\tSpherical Lon is: {0}", oSpherical.lon)
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
            oCartesian: "ICartesian" = clr.Convert(oPosition.convert_to(POSITION_TYPE.CARTESIAN), ICartesian)
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

            def action14():
                oCartesian.x = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action14)

            def action15():
                oCartesian.y = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action15)

            def action16():
                oCartesian.z = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action16)

            oCartesian.convert_to(POSITION_TYPE.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oCartesian.convert_to(POSITION_TYPE.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oCartesian.convert_to(POSITION_TYPE.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oCartesian.convert_to(POSITION_TYPE.GEODETIC)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oCartesian.convert_to(POSITION_TYPE.SPHERICAL)

        if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
            oCylindrical: "ICylindrical" = clr.Convert(oPosition.convert_to(POSITION_TYPE.CYLINDRICAL), ICylindrical)
            Assert.assertIsNotNone(oCylindrical)
            oCylindrical.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oCylindrical.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oCylindrical)
            oCylindrical.radius = 12203.4
            oCylindrical.z = 3513.17
            oCylindrical.lon = 1.23
            oCylindrical.assign_cylindrical(12203.4, 3513.17, 1.23)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oCylindrical)

            def action17():
                oCylindrical.radius = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action17)

            def action18():
                oCylindrical.z = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action18)

            def action19():
                oCylindrical.lon = 6.78

            TryCatchAssertBlock.DoAssert("", action19)

            oCylindrical.convert_to(POSITION_TYPE.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oCylindrical.convert_to(POSITION_TYPE.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oCylindrical.convert_to(POSITION_TYPE.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oCylindrical.convert_to(POSITION_TYPE.GEODETIC)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oCylindrical.convert_to(POSITION_TYPE.SPHERICAL)

        if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
            oGeocentric: "IGeocentric" = clr.Convert(oPosition.convert_to(POSITION_TYPE.GEOCENTRIC), IGeocentric)
            Assert.assertIsNotNone(oGeocentric)
            oGeocentric.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oGeocentric.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oGeocentric)
            oGeocentric.lat = 1.234
            oGeocentric.lon = 2.345
            oGeocentric.altitude = 12.34
            oGeocentric.assign_geocentric(1.234, 2.345, 12.34)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oGeocentric)

            def action20():
                oGeocentric.lat = 2.34

            TryCatchAssertBlock.DoAssert("", action20)

            def action21():
                oGeocentric.lon = 6.78

            TryCatchAssertBlock.DoAssert("", action21)

            def action22():
                oGeocentric.altitude = 6780000000000.0

            TryCatchAssertBlock.DoAssert("", action22)

            oGeocentric.convert_to(POSITION_TYPE.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oGeocentric.convert_to(POSITION_TYPE.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oGeocentric.convert_to(POSITION_TYPE.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oGeocentric.convert_to(POSITION_TYPE.GEODETIC)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oGeocentric.convert_to(POSITION_TYPE.SPHERICAL)

        if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
            oGeodetic: "IGeodetic" = clr.Convert(oPosition.convert_to(POSITION_TYPE.GEODETIC), IGeodetic)
            Assert.assertIsNotNone(oGeodetic)
            oGeodetic.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oGeodetic.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oGeodetic)
            oGeodetic.lat = 0.190988679940043
            oGeodetic.lon = -0.743582379766568
            oGeodetic.altitude = 0.640787459798838
            oGeodetic.assign_geodetic(0.190988679940043, -0.743582379766568, 0.640787459798838)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oGeodetic)

            def action23():
                oGeodetic.lat = 2.34

            TryCatchAssertBlock.DoAssert("", action23)

            def action24():
                oGeodetic.lon = 6.78

            TryCatchAssertBlock.DoAssert("", action24)

            def action25():
                oGeodetic.altitude = 6780000000000.0

            TryCatchAssertBlock.DoAssert("", action25)

            oGeodetic.convert_to(POSITION_TYPE.GEODETIC)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oGeodetic.convert_to(POSITION_TYPE.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oGeodetic.convert_to(POSITION_TYPE.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oGeodetic.convert_to(POSITION_TYPE.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oGeodetic.convert_to(POSITION_TYPE.SPHERICAL)

        if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
            oSpherical: "ISpherical" = clr.Convert(oPosition.convert_to(POSITION_TYPE.SPHERICAL), ISpherical)
            Assert.assertIsNotNone(oSpherical)
            oSpherical.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oSpherical.position_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oSpherical)
            oSpherical.lat = 1
            oSpherical.lon = 2
            oSpherical.radius = 6355753
            oSpherical.assign_spherical(1, 2, 6355753)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oSpherical)

            def action26():
                oSpherical.lat = 2.34

            TryCatchAssertBlock.DoAssert("", action26)

            def action27():
                oSpherical.lon = 6.78

            TryCatchAssertBlock.DoAssert("", action27)

            def action28():
                oSpherical.radius = 67800000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action28)

            oSpherical.convert_to(POSITION_TYPE.SPHERICAL)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oSpherical.convert_to(POSITION_TYPE.CARTESIAN)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oSpherical.convert_to(POSITION_TYPE.CYLINDRICAL)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oSpherical.convert_to(POSITION_TYPE.GEOCENTRIC)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oSpherical.convert_to(POSITION_TYPE.GEODETIC)

        if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
            # SetAsCartesian
            # oPosition.AssignCartesian(0.190988679940043, -0.743582379766568, 0.640787459798838); // See 35836
            oPosition.assign_cartesian(6654000, 230000, 113000)
            self.Display(oPosition.convert_to(POSITION_TYPE.CARTESIAN))

        if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
            # SetAsCylindrical
            oPosition.assign_cylindrical(1, 500, 5)
            self.Display(oPosition.convert_to(POSITION_TYPE.CYLINDRICAL))

        if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
            # SetAsGeocentric
            oPosition.assign_geocentric(0, 0, 1)
            self.Display(oPosition.convert_to(POSITION_TYPE.GEOCENTRIC))

        if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
            # SetAsGeodetic
            oPosition.assign_geodetic(0.190988679940043, -0.743582379766568, 0.640787459798838)
            self.Display(oPosition.convert_to(POSITION_TYPE.GEODETIC))

        if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
            # SetAsSpherical
            oPosition.assign_spherical(-1, -1, 600355753)
            self.Display(oPosition.convert_to(POSITION_TYPE.SPHERICAL))

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
    def Display(self, oPosition: "ILLAPosition"):
        Assert.assertIsNotNone(oPosition)
        if oPosition.type == LLA_POSITION_TYPE.GEOCENTRIC:
            llaGeocentric: "ILLAGeocentric" = clr.Convert(
                oPosition.convert_to(LLA_POSITION_TYPE.GEOCENTRIC), ILLAGeocentric
            )
            Assert.assertIsNotNone(llaGeocentric)
            self.m_logger.WriteLine6("\t\tGeocentric Lat is: {0}", llaGeocentric.lat)
            self.m_logger.WriteLine6("\t\tGeocentric Lon is: {0}", llaGeocentric.lon)
            self.m_logger.WriteLine6("\t\tGeocentric Rad is: {0}", llaGeocentric.rad)

            llaGeocentric.assign_geocentric(10.0, 20.0, 10000.0)
            Assert.assertEqual(10.0, llaGeocentric.lat)
            Assert.assertEqual(20.0, llaGeocentric.lon)
            Assert.assertEqual(10000.0, llaGeocentric.rad)

            llaGeocentric.assign_geodetic(40.0, 50.0, 60.0)
            Assert.assertAlmostEqual(39.81, llaGeocentric.lat, delta=0.01)
            Assert.assertAlmostEqual(50.0, llaGeocentric.lon, delta=0.01)
            Assert.assertAlmostEqual(6429, llaGeocentric.rad, delta=1.0)
        elif oPosition.type == LLA_POSITION_TYPE.GEODETIC:
            llaGeodetic: "ILLAGeodetic" = clr.Convert(oPosition.convert_to(LLA_POSITION_TYPE.GEODETIC), ILLAGeodetic)
            Assert.assertIsNotNone(llaGeodetic)
            self.m_logger.WriteLine6("\t\tGeodetic Lat is: {0}", llaGeodetic.lat)
            self.m_logger.WriteLine6("\t\tGeodetic Lon is: {0}", llaGeodetic.lon)
            self.m_logger.WriteLine6("\t\tGeodetic Alt is: {0}", llaGeodetic.altitude)

            llaGeodetic.assign_geocentric(10.0, 20.0, 10000.0)
            Assert.assertAlmostEqual(10.04, llaGeodetic.lat, delta=0.01)
            Assert.assertAlmostEqual(19.95, llaGeodetic.lon, delta=0.1)
            Assert.assertAlmostEqual(3622, llaGeodetic.altitude, delta=1.0)

            llaGeodetic.assign_geodetic(40.0, 50.0, 10000.0)
            Assert.assertEqual(40.0, llaGeodetic.lat)
            Assert.assertEqual(50.0, llaGeodetic.lon)
            Assert.assertEqual(10000.0, llaGeodetic.altitude)
        else:
            Assert.fail("Invalid LLA Position type: {0}", oPosition.type)

    # endregion

    # region Run method
    def Run(self, oPosition: "ILLAPosition"):
        self.m_logger.WriteLine("----- LLA POSITION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oPosition)
        # Type
        self.m_logger.WriteLine6("\tThe current Type is: {0}", oPosition.type)
        self.Display(oPosition)
        # Geocentric
        # ConvertTo
        oGeocentric: "ILLAGeocentric" = clr.Convert(oPosition.convert_to(LLA_POSITION_TYPE.GEOCENTRIC), ILLAGeocentric)
        Assert.assertIsNotNone(oGeocentric)
        # Assign
        oGeocentric.assign(oPosition)
        oPosition.convert_to(LLA_POSITION_TYPE.GEODETIC)
        self.m_logger.WriteLine6("\tThe new Type is: {0}", oGeocentric.type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oGeocentric)
        # Lat
        oGeocentric.lat = 23.45
        Assert.assertAlmostEqual(23.45, oGeocentric.lat, delta=0.01)

        def action29():
            oGeocentric.lat = -321

        TryCatchAssertBlock.DoAssert("", action29)
        # Lon
        oGeocentric.lon = 54.321
        Assert.assertAlmostEqual(54.321, oGeocentric.lon, delta=0.001)

        def action30():
            oGeocentric.lon = -321

        TryCatchAssertBlock.DoAssert("", action30)
        # Rad
        oGeocentric.rad = 12345.6
        Assert.assertAlmostEqual(12345.6, oGeocentric.rad, delta=0.01)

        def action31():
            oGeocentric.rad = -321

        TryCatchAssertBlock.DoAssert("", action31)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oGeocentric)
        # Geodetic
        # ConvertTo
        oGeodetic: "ILLAGeodetic" = clr.Convert(oGeocentric.convert_to(LLA_POSITION_TYPE.GEODETIC), ILLAGeodetic)
        Assert.assertIsNotNone(oGeodetic)
        # Assign
        oGeodetic.assign(oGeocentric)
        oGeodetic.convert_to(LLA_POSITION_TYPE.GEOCENTRIC)
        self.m_logger.WriteLine6("\tThe new Type is: {0}", oGeodetic.type)
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.Display(oGeodetic)
        # Lat
        oGeodetic.lat = 12.3456
        Assert.assertAlmostEqual(12.3456, oGeodetic.lat, delta=0.0001)

        def action32():
            oGeodetic.lat = -321

        TryCatchAssertBlock.DoAssert("", action32)
        # Lon
        oGeodetic.lon = -54.321
        Assert.assertAlmostEqual(-54.321, oGeodetic.lon, delta=0.001)

        def action33():
            oGeodetic.lon = -321

        TryCatchAssertBlock.DoAssert("", action33)
        # Alt
        oGeodetic.altitude = 123.456
        Assert.assertAlmostEqual(123.456, oGeodetic.altitude, delta=0.001)

        def action34():
            oGeodetic.altitude = -321

        TryCatchAssertBlock.DoAssert("", action34)
        self.m_logger.WriteLine("\t\tNew values:")
        self.Display(oGeodetic)

        def action35():
            oPosition.convert_to(LLA_POSITION_TYPE.UNKNOWN)

        TryCatchAssertBlock.DoAssert("", action35)

        # Testing the helper methods to convert to desired LLA position type and set its values in one call
        # SetAsGeocentric
        oPosition.assign_geocentric(23.45, 54.321, 12345.6)
        self.Display(oPosition.convert_to(LLA_POSITION_TYPE.GEOCENTRIC))
        # SetAsGeodetic
        oPosition.assign_geodetic(12.3456, -54.321, 123.456)
        self.Display(oPosition.convert_to(LLA_POSITION_TYPE.GEODETIC))
        self.m_logger.WriteLine("----- LLA POSITION TEST ----- END -----")

    # endregion
    # endregion
