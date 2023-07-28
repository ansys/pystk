from test_util import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class OrbitStateHelper(object):
    def __init__(self, oApplication: "ansys.stk.core.stkobjects.IStkObjectRoot"):
        self.m_oCartesian: "IOrbitStateCartesian" = None
        self.m_oClassical: "IOrbitStateClassical" = None
        self.m_oGeodetic: "IOrbitStateGeodetic" = None
        self.m_oDelaunay: "IOrbitStateDelaunay" = None
        self.m_oEquinoctial: "IOrbitStateEquinoctial" = None
        self.m_oMixed: "IOrbitStateMixedSpherical" = None
        self.m_oSpherical: "IOrbitStateSpherical" = None
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "ansys.stk.core.stkobjects.IStkObjectRoot" = oApplication
        self.m_oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection" = (
            self.m_oApplication.UnitPreferences
        )

    # region CoordinateSystemTest
    def CoordinateSystemTest(self, eOrbitStateType: "AgEOrbitStateType", eSystemType: "AgECoordinateSystem"):
        oSystem: "IOrbitStateCoordinateSystem" = None
        if eOrbitStateType == AgEOrbitStateType.eOrbitStateCartesian:
            Assert.assertIsNotNone(self.m_oCartesian)
            self.m_oCartesian.CoordinateSystemType = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oCartesian.CoordinateSystemType)
            Assert.assertEqual(eSystemType, self.m_oCartesian.CoordinateSystemType)
            oSystem = self.m_oCartesian.CoordinateSystem
        elif eOrbitStateType == AgEOrbitStateType.eOrbitStateClassical:
            Assert.assertIsNotNone(self.m_oClassical)
            self.m_oClassical.CoordinateSystemType = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oClassical.CoordinateSystemType)
            Assert.assertEqual(eSystemType, self.m_oClassical.CoordinateSystemType)
            oSystem = self.m_oClassical.CoordinateSystem
        elif eOrbitStateType == AgEOrbitStateType.eOrbitStateGeodetic:
            Assert.assertIsNotNone(self.m_oGeodetic)
            self.m_oGeodetic.CoordinateSystemType = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oGeodetic.CoordinateSystemType)
            Assert.assertEqual(eSystemType, self.m_oGeodetic.CoordinateSystemType)
            oSystem = self.m_oGeodetic.CoordinateSystem
        elif eOrbitStateType == AgEOrbitStateType.eOrbitStateDelaunay:
            Assert.assertIsNotNone(self.m_oDelaunay)
            self.m_oDelaunay.CoordinateSystemType = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oDelaunay.CoordinateSystemType)
            Assert.assertEqual(eSystemType, self.m_oDelaunay.CoordinateSystemType)
            oSystem = self.m_oDelaunay.CoordinateSystem
        elif eOrbitStateType == AgEOrbitStateType.eOrbitStateEquinoctial:
            Assert.assertIsNotNone(self.m_oEquinoctial)
            self.m_oEquinoctial.CoordinateSystemType = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oEquinoctial.CoordinateSystemType)
            Assert.assertEqual(eSystemType, self.m_oEquinoctial.CoordinateSystemType)
            oSystem = self.m_oEquinoctial.CoordinateSystem
        elif eOrbitStateType == AgEOrbitStateType.eOrbitStateMixedSpherical:
            Assert.assertIsNotNone(self.m_oMixed)
            self.m_oMixed.CoordinateSystemType = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oMixed.CoordinateSystemType)
            Assert.assertEqual(eSystemType, self.m_oMixed.CoordinateSystemType)
            oSystem = self.m_oMixed.CoordinateSystem
        elif eOrbitStateType == AgEOrbitStateType.eOrbitStateSpherical:
            Assert.assertIsNotNone(self.m_oSpherical)
            self.m_oSpherical.CoordinateSystemType = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oSpherical.CoordinateSystemType)
            Assert.assertEqual(eSystemType, self.m_oSpherical.CoordinateSystemType)
            oSystem = self.m_oSpherical.CoordinateSystem
        else:
            oSystem = None

        Assert.assertIsNotNone(oSystem)
        self.m_logger.WriteLine6("\t\t\tType is: {0}", oSystem.Type)
        self.m_logger.WriteLine6("\t\t\tCurrent Epoch is: {0}", oSystem.CoordinateSystemEpoch.TimeInstant)
        if (
            (
                ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemAlignmentAtEpoch))
                or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemMeanOfEpoch))
            )
            or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemTEMEOfEpoch))
        ) or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemTrueOfEpoch)):
            oSystem.CoordinateSystemEpoch.SetExplicitTime("13 Aug 2005 02:00:00.000")
            self.m_logger.WriteLine6("\t\t\tNew Epoch is: {0}", oSystem.CoordinateSystemEpoch.TimeInstant)
            Assert.assertEqual("13 Aug 2005 02:00:00.000", oSystem.CoordinateSystemEpoch.TimeInstant)
        elif (
            (
                (
                    (
                        (
                            (
                                ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemB1950))
                                or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemFixed))
                            )
                            or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemJ2000))
                        )
                        or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemMeanOfDate))
                    )
                    or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemTEMEOfDate))
                )
                or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemTrueOfDate))
            )
            or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemTrueOfRefDate))
        ) or ((oSystem.Type == AgECoordinateSystem.eCoordinateSystemICRF)):
            bCaught: bool = False
            try:
                bCaught = False
                oSystem.CoordinateSystemEpoch.SetExplicitTime("13 Aug 2005 02:00:00.000")

            except Exception as e:
                bCaught = True
                self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Epoch should be read only!")

        else:
            Assert.fail("Invalid CoordinateSystem type!")

    # endregion

    # region Run method
    def Run(self, oOrbitState: "IOrbitState"):
        Assert.assertIsNotNone(oOrbitState)
        self.m_logger.WriteLine("OrbitState test:")
        self.m_logger.WriteLine6("\tCurrent OrbitState type is: {0}", oOrbitState.OrbitStateType)

        # Cartesian OrbitState test
        self.m_oCartesian = clr.Convert(
            oOrbitState.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian), IOrbitStateCartesian
        )
        Assert.assertIsNotNone(self.m_oCartesian)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oCartesian.OrbitStateType)
        self.m_oCartesian.Assign(oOrbitState)
        self.m_oCartesian.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian)
        self.m_oCartesian.ConvertTo(AgEOrbitStateType.eOrbitStateClassical)
        self.m_oCartesian.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay)
        self.m_oCartesian.ConvertTo(AgEOrbitStateType.eOrbitStateEquinoctial)
        self.m_oCartesian.ConvertTo(AgEOrbitStateType.eOrbitStateGeodetic)
        self.m_oCartesian.ConvertTo(AgEOrbitStateType.eOrbitStateMixedSpherical)
        self.m_oCartesian.ConvertTo(AgEOrbitStateType.eOrbitStateSpherical)

        # See 25151: try to convert an orbit state that's describes open orbits
        # to Delaunay representation; expecting an exception with a user-friendly explanation
        # why conversion cannot be finished.

        tempCart: "IOrbitStateCartesian" = clr.CastAs(
            self.m_oCartesian.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian), IOrbitStateCartesian
        )

        self.m_oUnits.SetCurrentUnit("DistanceUnit", "km")
        self.m_oUnits.SetCurrentUnit("TimeUnit", "sec")
        # position is in 'km' and velocity is in 'km/sec'.
        tempCart.XPosition = 5691.457559
        tempCart.YPosition = 9857.898
        tempCart.ZPosition = 0
        tempCart.XVelocity = 0
        tempCart.YVelocity = 5.917552767
        tempCart.ZVelocity = 5.917552767
        try:
            delaunay: "IOrbitStateDelaunay" = clr.CastAs(
                tempCart.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay), IOrbitStateDelaunay
            )
            Assert.fail()

        except AssertionError as e:
            raise e

        except Exception as ex:
            sExpectedMsg: str = "Invalid orbit has been specified!"
            Assert.assertEqual(sExpectedMsg, str(ex)[0 : len(sExpectedMsg)])
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(ex))

        del tempCart
        # End of 25151

        self.CartesianTest()

        # Classical OrbitState test
        self.m_oClassical = clr.Convert(
            oOrbitState.ConvertTo(AgEOrbitStateType.eOrbitStateClassical), IOrbitStateClassical
        )
        Assert.assertIsNotNone(self.m_oClassical)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oClassical.OrbitStateType)
        self.m_oClassical.Assign(oOrbitState)
        self.m_oClassical.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian)
        self.m_oClassical.ConvertTo(AgEOrbitStateType.eOrbitStateClassical)
        self.m_oClassical.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay)
        self.m_oClassical.ConvertTo(AgEOrbitStateType.eOrbitStateEquinoctial)
        self.m_oClassical.ConvertTo(AgEOrbitStateType.eOrbitStateGeodetic)
        self.m_oClassical.ConvertTo(AgEOrbitStateType.eOrbitStateMixedSpherical)
        self.m_oClassical.ConvertTo(AgEOrbitStateType.eOrbitStateSpherical)
        self.ClassicalTest()

        # Geodetic OrbitState test
        self.m_oGeodetic = clr.Convert(
            oOrbitState.ConvertTo(AgEOrbitStateType.eOrbitStateGeodetic), IOrbitStateGeodetic
        )
        Assert.assertIsNotNone(self.m_oGeodetic)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oGeodetic.OrbitStateType)
        self.m_oGeodetic.Assign(oOrbitState)
        self.m_oGeodetic.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian)
        self.m_oGeodetic.ConvertTo(AgEOrbitStateType.eOrbitStateClassical)
        self.m_oGeodetic.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay)
        self.m_oGeodetic.ConvertTo(AgEOrbitStateType.eOrbitStateEquinoctial)
        self.m_oGeodetic.ConvertTo(AgEOrbitStateType.eOrbitStateGeodetic)
        self.m_oGeodetic.ConvertTo(AgEOrbitStateType.eOrbitStateMixedSpherical)
        self.m_oGeodetic.ConvertTo(AgEOrbitStateType.eOrbitStateSpherical)
        self.GeodeticTest()

        # Delaunay OrbitState test
        self.m_oDelaunay = clr.Convert(
            oOrbitState.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay), IOrbitStateDelaunay
        )
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oDelaunay.OrbitStateType)
        self.m_oDelaunay.Assign(oOrbitState)
        self.m_oDelaunay.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian)
        self.m_oDelaunay.ConvertTo(AgEOrbitStateType.eOrbitStateClassical)
        self.m_oDelaunay.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay)
        self.m_oDelaunay.ConvertTo(AgEOrbitStateType.eOrbitStateEquinoctial)
        self.m_oDelaunay.ConvertTo(AgEOrbitStateType.eOrbitStateGeodetic)
        self.m_oDelaunay.ConvertTo(AgEOrbitStateType.eOrbitStateMixedSpherical)
        self.m_oDelaunay.ConvertTo(AgEOrbitStateType.eOrbitStateSpherical)
        self.DelaunayTest()

        # Equinoctical OrbitState test
        self.m_oEquinoctial = clr.Convert(
            oOrbitState.ConvertTo(AgEOrbitStateType.eOrbitStateEquinoctial), IOrbitStateEquinoctial
        )
        Assert.assertIsNotNone(self.m_oEquinoctial)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oEquinoctial.OrbitStateType)
        self.m_oEquinoctial.Assign(oOrbitState)
        self.m_oEquinoctial.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian)
        self.m_oEquinoctial.ConvertTo(AgEOrbitStateType.eOrbitStateClassical)
        self.m_oEquinoctial.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay)
        self.m_oEquinoctial.ConvertTo(AgEOrbitStateType.eOrbitStateEquinoctial)
        self.m_oEquinoctial.ConvertTo(AgEOrbitStateType.eOrbitStateGeodetic)
        self.m_oEquinoctial.ConvertTo(AgEOrbitStateType.eOrbitStateMixedSpherical)
        self.m_oEquinoctial.ConvertTo(AgEOrbitStateType.eOrbitStateSpherical)
        self.EquinoctialTest()

        # MixedSpherical OrbitState test
        self.m_oMixed = clr.Convert(
            oOrbitState.ConvertTo(AgEOrbitStateType.eOrbitStateMixedSpherical), IOrbitStateMixedSpherical
        )
        Assert.assertIsNotNone(self.m_oMixed)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oMixed.OrbitStateType)
        self.m_oMixed.Assign(oOrbitState)
        self.m_oMixed.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian)
        self.m_oMixed.ConvertTo(AgEOrbitStateType.eOrbitStateClassical)
        self.m_oMixed.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay)
        self.m_oMixed.ConvertTo(AgEOrbitStateType.eOrbitStateEquinoctial)
        self.m_oMixed.ConvertTo(AgEOrbitStateType.eOrbitStateGeodetic)
        self.m_oMixed.ConvertTo(AgEOrbitStateType.eOrbitStateMixedSpherical)
        self.m_oMixed.ConvertTo(AgEOrbitStateType.eOrbitStateSpherical)
        self.MixedSphericalTest()

        # Spherical OrbitState test
        self.m_oSpherical = clr.Convert(
            oOrbitState.ConvertTo(AgEOrbitStateType.eOrbitStateSpherical), IOrbitStateSpherical
        )
        Assert.assertIsNotNone(self.m_oSpherical)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oSpherical.OrbitStateType)
        self.m_oSpherical.Assign(oOrbitState)
        self.m_oSpherical.ConvertTo(AgEOrbitStateType.eOrbitStateCartesian)
        self.m_oSpherical.ConvertTo(AgEOrbitStateType.eOrbitStateClassical)
        self.m_oSpherical.ConvertTo(AgEOrbitStateType.eOrbitStateDelaunay)
        self.m_oSpherical.ConvertTo(AgEOrbitStateType.eOrbitStateEquinoctial)
        self.m_oSpherical.ConvertTo(AgEOrbitStateType.eOrbitStateGeodetic)
        self.m_oSpherical.ConvertTo(AgEOrbitStateType.eOrbitStateMixedSpherical)
        self.m_oSpherical.ConvertTo(AgEOrbitStateType.eOrbitStateSpherical)
        self.SphericalTest()

        # Testing the helper methods to convert to desired orbit state type and set its values in one call
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "km")
        self.m_oUnits.SetCurrentUnit("TimeUnit", "sec")
        self.m_oUnits.SetCurrentUnit("AngleUnit", "deg")

        # SetOrbitStateAsCartesian
        oOrbitState.AssignCartesian(
            AgECoordinateSystem.eCoordinateSystemFixed, -22760.2, 549.443, 0.0, -0.0742022, -3.07376, 0.0
        )
        oOrbitState.AssignClassical(AgECoordinateSystem.eCoordinateSystemJ2000, 22000.1, 0.1, 12.3, 0.2, 358.0, 45.4)
        oOrbitState.AssignEquinoctialPosigrade(
            AgECoordinateSystem.eCoordinateSystemJ2000, 22000.1, 0.1, 0.4, 0.2, 58.0, 45.4
        )
        oOrbitState.AssignGeodetic(
            AgECoordinateSystem.eCoordinateSystemFixed, 0.004011, -99.998868, 35786.032637, 1.51e-07, 0.0, 0.0
        )
        oOrbitState.AssignMixedSpherical(
            AgECoordinateSystem.eCoordinateSystemJ2000, 0.004011, -99.998868, 35786.032637, -0.0, 90.0, 3.074660099
        )
        oOrbitState.AssignSpherical(
            AgECoordinateSystem.eCoordinateSystemJ2000, 178.617119, 0.0, 42164.169637, -0.0, 90.0, 3.074660099
        )

        self.m_oUnits.ResetUnits()

    # endregion

    def Test_IAgOrbitState(self, orbitState: "IOrbitState"):
        centralBodyName: str = orbitState.CentralBodyName
        ost: "AgEOrbitStateType" = orbitState.OrbitStateType

        epochHold: typing.Any = orbitState.Epoch
        orbitState.Epoch = "18 Jan 2003 02:40:24.680"
        Assert.assertEqual("18 Jan 2003 02:40:24.680", orbitState.Epoch)
        orbitState.Epoch = epochHold

        orbitState.AssignCartesian(
            AgECoordinateSystem.eCoordinateSystemFixed, -22760.2, 549.443, 0.0, -0.0742022, -3.07376, 0.0
        )
        orbitState.AssignClassical(AgECoordinateSystem.eCoordinateSystemJ2000, 22000.1, 0.1, 12.3, 0.2, 358.0, 45.4)
        orbitState.AssignEquinoctialPosigrade(
            AgECoordinateSystem.eCoordinateSystemJ2000, 22000.1, 0.1, 0.4, 0.2, 58.0, 45.4
        )
        orbitState.AssignGeodetic(
            AgECoordinateSystem.eCoordinateSystemFixed, 0.004011, -99.998868, 35786.032637, 1.51e-07, 0.0, 0.0
        )
        orbitState.AssignMixedSpherical(
            AgECoordinateSystem.eCoordinateSystemJ2000, 0.004011, -99.998868, 35786.032637, -0.0, 90.0, 3.074660099
        )
        orbitState.AssignSpherical(
            AgECoordinateSystem.eCoordinateSystemJ2000, 178.617119, 0.0, 42164.169637, -0.0, 90.0, 3.074660099
        )

    # region CartesianTest
    def CartesianTest(self):
        Assert.assertIsNotNone(self.m_oCartesian)
        self.Test_IAgOrbitState(self.m_oCartesian)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "nm")
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        Assert.assertEqual("nm", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

        # basic properties test
        # m_logger.WriteLine("\t\tCurrent values:");
        # m_logger.WriteLine("\t\t\t XPosition is: {0}", m_oCartesian.XPosition);
        # m_logger.WriteLine("\t\t\t YPosition is: {0}", m_oCartesian.YPosition);
        # m_logger.WriteLine("\t\t\t ZPosition is: {0}", m_oCartesian.ZPosition);
        # m_logger.WriteLine("\t\t\t XVelocity is: {0}", m_oCartesian.XVelocity);
        # m_logger.WriteLine("\t\t\t YVelocity is: {0}", m_oCartesian.YVelocity);
        # m_logger.WriteLine("\t\t\t ZVelocity is: {0}", m_oCartesian.ZVelocity);
        self.m_oCartesian.XPosition = -22760.2
        self.m_oCartesian.YPosition = 549.443
        self.m_oCartesian.ZPosition = 0.0
        self.m_oCartesian.XVelocity = -0.0742022
        self.m_oCartesian.YVelocity = -3.07376
        self.m_oCartesian.ZVelocity = 0.0
        # m_logger.WriteLine("\t\tNew values:");
        # m_logger.WriteLine("\t\t\t XPosition is: {0}", m_oCartesian.XPosition);
        # m_logger.WriteLine("\t\t\t YPosition is: {0}", m_oCartesian.YPosition);
        # m_logger.WriteLine("\t\t\t ZPosition is: {0}", m_oCartesian.ZPosition);
        # m_logger.WriteLine("\t\t\t XVelocity is: {0}", m_oCartesian.XVelocity);
        # m_logger.WriteLine("\t\t\t YVelocity is: {0}", m_oCartesian.YVelocity);
        # m_logger.WriteLine("\t\t\t ZVelocity is: {0}", m_oCartesian.ZVelocity);
        Assert.assertEqual(-22760.2, self.m_oCartesian.XPosition)
        Assert.assertEqual(549.443, self.m_oCartesian.YPosition)
        Assert.assertEqual(0.0, self.m_oCartesian.ZPosition)
        Assert.assertEqual(-0.0742022, self.m_oCartesian.XVelocity)
        Assert.assertAlmostEqual(-3.07376, self.m_oCartesian.YVelocity, delta=1e-05)
        Assert.assertEqual(0.0, self.m_oCartesian.ZVelocity)
        # out of bounds
        bCaught: bool = False
        try:
            bCaught = False
            self.m_oCartesian.XPosition = 1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set XPosition out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.YPosition = -1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set YPosition out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.ZPosition = 1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ZPosition out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.XVelocity = -1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set XVelocity out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.YVelocity = 1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set YVelocity out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.ZVelocity = -1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ZVelocity out of bounds")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

        # CoordinateSystem test
        arTypes = self.m_oCartesian.SupportedCoordinateSystemTypes
        self.m_logger.WriteLine3("\t\tCartesian supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                clr.Convert(int(arTypes[iIndex][0]), AgECoordinateSystem),
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oCartesian.CoordinateSystemType)
        # eCoordinateSystemAlignmentAtEpoch
        self.CoordinateSystemTest(
            self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemAlignmentAtEpoch
        )
        # eCoordinateSystemB1950
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemB1950)
        # eCoordinateSystemFixed
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemFixed)
        # eCoordinateSystemJ2000
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemJ2000)
        # eCoordinateSystemICRF;
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemICRF)
        # eCoordinateSystemMeanOfDate
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfDate)
        # eCoordinateSystemMeanOfEpoch
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfEpoch)
        # eCoordinateSystemTEMEOfDate
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfDate)
        # eCoordinateSystemTEMEOfEpoch
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfEpoch)
        # eCoordinateSystemTrueOfDate
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfDate)
        # eCoordinateSystemTrueOfEpoch
        self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfEpoch)
        try:
            # eCoordinateSystemTrueOfRefDate
            self.CoordinateSystemTest(
                self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate
            )

        except:
            self.m_logger.WriteLine("\t\tThe eCoordinateSystemTrueOfRefDate does not supported by current licenses.")

        # eCoordinateSystemUnknown
        try:
            self.CoordinateSystemTest(self.m_oCartesian.OrbitStateType, AgECoordinateSystem.eCoordinateSystemUnknown)
            Assert.fail("Cannot set eCoordinateSystemUnknown coordinate system.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

    # endregion

    # region ClassicalTest
    def ClassicalTest(self):
        Assert.assertIsNotNone(self.m_oClassical)
        self.Test_IAgOrbitState(self.m_oClassical)

        # SizeShape test
        self.m_logger.WriteLine6("\t\tCurrent SizeShape type is: {0}", self.m_oClassical.SizeShapeType)
        self.ClassicalSizeShape(AgEClassicalSizeShape.eSizeShapeAltitude)
        self.ClassicalSizeShape(AgEClassicalSizeShape.eSizeShapeMeanMotion)
        self.ClassicalSizeShape(AgEClassicalSizeShape.eSizeShapePeriod)
        self.ClassicalSizeShape(AgEClassicalSizeShape.eSizeShapeRadius)
        self.ClassicalSizeShape(AgEClassicalSizeShape.eSizeShapeSemimajorAxis)
        try:
            self.ClassicalSizeShape(AgEClassicalSizeShape.eSizeShapeUnknown)
            Assert.fail("Cannot set AgEClassicalSizeShape.eSizeShapeUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # Orientation test
        self.ClassicalOrientation(self.m_oClassical.Orientation)

        # Location test
        self.m_logger.WriteLine6("\t\tCurrent Location type is: {0}", self.m_oClassical.LocationType)
        self.ClassicalLocation(AgEClassicalLocation.eLocationArgumentOfLatitude)
        self.ClassicalLocation(AgEClassicalLocation.eLocationEccentricAnomaly)
        self.ClassicalLocation(AgEClassicalLocation.eLocationMeanAnomaly)
        self.ClassicalLocation(AgEClassicalLocation.eLocationTimePastAN)
        self.ClassicalLocation(AgEClassicalLocation.eLocationTimePastPerigee)
        self.ClassicalLocation(AgEClassicalLocation.eLocationTrueAnomaly)
        try:
            self.ClassicalLocation(AgEClassicalLocation.eLocationUnknown)
            Assert.fail("Cannot set AgEClassicalLocation.eLocationUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # CoordinateSystem test
        arTypes = self.m_oClassical.SupportedCoordinateSystemTypes
        self.m_logger.WriteLine3("\t\tClassical supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                clr.Convert(int(arTypes[iIndex][0]), AgECoordinateSystem),
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oClassical.CoordinateSystemType)
        # eCoordinateSystemAlignmentAtEpoch
        self.CoordinateSystemTest(
            self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemAlignmentAtEpoch
        )
        # eCoordinateSystemB1950
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemB1950)
        # eCoordinateSystemFixed
        bCaught: bool = False
        try:
            bCaught = False
            self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemFixed)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemFixed")

        # eCoordinateSystemJ2000
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemJ2000)
        # eCoordinateSystemICRF
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemICRF)
        # eCoordinateSystemMeanOfDate
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfDate)
        # eCoordinateSystemMeanOfEpoch
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfEpoch)
        # eCoordinateSystemTEMEOfDate
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfDate)
        # eCoordinateSystemTEMEOfEpoch
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfEpoch)
        # eCoordinateSystemTrueOfDate
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfDate)
        # eCoordinateSystemTrueOfEpoch
        self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfEpoch)
        # eCoordinateSystemTrueOfRefDate
        # GetLicenses
        oLicenses: "ansys.stk.core.stkutil.IExecCmdResult" = None
        oLicenses = self.m_oApplication.ExecuteCommand("GetLicenses /")
        Assert.assertIsNotNone(oLicenses)

        iI: int = 0
        while iI < oLicenses.Count:
            strLicense: str = oLicenses[iI]
            if strLicense.find("PODS") >= 0:
                if strLicense.find("No License") >= 0:
                    # No License
                    try:
                        bCaught = False
                        self.CoordinateSystemTest(
                            self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate
                        )

                    except Exception as e:
                        bCaught = True
                        self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set eCoordinateSystemTrueOfRefDate")

                else:
                    # License available
                    self.CoordinateSystemTest(
                        self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate
                    )

                break

            iI += 1

        # eCoordinateSystemUnknown
        try:
            self.CoordinateSystemTest(self.m_oClassical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemUnknown)
            Assert.fail("Cannot set AgECoordinateSystem.eCoordinateSystemUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

    # endregion

    # region ClassicalSizeShape
    def ClassicalSizeShape(self, eShapeType: "AgEClassicalSizeShape"):
        Assert.assertIsNotNone(self.m_oClassical)
        # set shape type
        self.m_oClassical.SizeShapeType = eShapeType
        self.m_logger.WriteLine6("\t\tNew SizeShape type is: {0}", self.m_oClassical.SizeShapeType)
        Assert.assertEqual(eShapeType, self.m_oClassical.SizeShapeType)
        if eShapeType == AgEClassicalSizeShape.eSizeShapeAltitude:
            self.ClassicalSizeShapeAltitude(clr.Convert(self.m_oClassical.SizeShape, IClassicalSizeShapeAltitude))
        elif eShapeType == AgEClassicalSizeShape.eSizeShapeMeanMotion:
            self.ClassicalSizeShapeMeanMotion(clr.Convert(self.m_oClassical.SizeShape, IClassicalSizeShapeMeanMotion))
        elif eShapeType == AgEClassicalSizeShape.eSizeShapePeriod:
            self.ClassicalSizeShapePeriod(clr.Convert(self.m_oClassical.SizeShape, IClassicalSizeShapePeriod))
        elif eShapeType == AgEClassicalSizeShape.eSizeShapeRadius:
            self.ClassicalSizeShapeRadius(clr.Convert(self.m_oClassical.SizeShape, IClassicalSizeShapeRadius))
        elif eShapeType == AgEClassicalSizeShape.eSizeShapeSemimajorAxis:
            self.ClassicalSizeShapeSemimajorAxis(
                clr.Convert(self.m_oClassical.SizeShape, IClassicalSizeShapeSemimajorAxis)
            )
        else:
            Assert.fail("Invalid SizeShape type!")

    # endregion

    # region ClassicalSizeShapeAltitude
    def ClassicalSizeShapeAltitude(self, oAltitude: "IClassicalSizeShapeAltitude"):
        Assert.assertIsNotNone(oAltitude)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeAltitude is: {0}", oAltitude.ApogeeAltitude)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeAltitude is: {0}", oAltitude.PerigeeAltitude)
        oAltitude.ApogeeAltitude = 123456.789
        oAltitude.PerigeeAltitude = 987654.321
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeAltitude is: {0}", oAltitude.ApogeeAltitude)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeAltitude is: {0}", oAltitude.PerigeeAltitude)
        Assert.assertEqual(123456.789, oAltitude.ApogeeAltitude)
        Assert.assertAlmostEqual(987654.321, oAltitude.PerigeeAltitude, delta=0.0001)
        bCaught: bool = False
        try:
            bCaught = False
            oAltitude.ApogeeAltitude = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ApogeeAltitude out of bounds")

        try:
            bCaught = False
            oAltitude.PerigeeAltitude = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set PerigeeAltitude out of bounds")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

    # endregion

    # region ClassicalSizeShapeMeanMotion
    def ClassicalSizeShapeMeanMotion(self, oMeanMotion: "IClassicalSizeShapeMeanMotion"):
        Assert.assertIsNotNone(oMeanMotion)
        # set AngleUnit
        strAngleUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strAngleUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        # set TimeUnit
        strTimeUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\t\tThe current TimeUnit is: {0}", strTimeUnit)
        self.m_oUnits.SetCurrentUnit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\t\tThe new TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t MeanMotion is: {0}", oMeanMotion.MeanMotion)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oMeanMotion.Eccentricity)
        # Changed meanmotion to a smaller number to prevent the iterative
        # solution in astro code from going into infinite loop trying to
        # figure out a semimajor axis length (see 25146)
        oMeanMotion.MeanMotion = 1.23456789  # mean motion is in rad/hr
        oMeanMotion.Eccentricity = 0.987654321
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t MeanMotion is: {0}", oMeanMotion.MeanMotion)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oMeanMotion.Eccentricity)
        Assert.assertEqual(1.23456789, oMeanMotion.MeanMotion)
        Assert.assertEqual(0.987654321, oMeanMotion.Eccentricity)

        bCaught: bool = False
        try:
            bCaught = False
            oMeanMotion.MeanMotion = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MeanMotion out of bounds")

        try:
            bCaught = False
            oMeanMotion.Eccentricity = 1.2

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Eccentricity out of bounds")

        # restore TimeUnit
        self.m_oUnits.SetCurrentUnit("TimeUnit", strTimeUnit)
        self.m_logger.WriteLine5("\t\t\tThe new TimeUnit (restored) is: {0}", strTimeUnit)
        Assert.assertEqual(strTimeUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strAngleUnit)
        self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strAngleUnit)
        Assert.assertEqual(strAngleUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

    # endregion

    # region ClassicalSizeShapePeriod
    def ClassicalSizeShapePeriod(self, oPeriod: "IClassicalSizeShapePeriod"):
        Assert.assertIsNotNone(oPeriod)

        # set TimeUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("TimeUnit", "yr")
        self.m_logger.WriteLine5("\t\t\tThe new TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        Assert.assertEqual("yr", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t Period is: {0}", oPeriod.Period)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oPeriod.Eccentricity)
        oPeriod.Period = 123456.789
        oPeriod.Eccentricity = 0.987654321
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t Period is: {0}", oPeriod.Period)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oPeriod.Eccentricity)
        Assert.assertAlmostEqual(123456.789, oPeriod.Period, delta=0.0001)
        Assert.assertEqual(0.987654321, oPeriod.Eccentricity)
        bCaught: bool = False
        try:
            bCaught = False
            oPeriod.Period = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Period out of bounds")

        try:
            bCaught = False
            oPeriod.Eccentricity = 1.2

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Eccentricity out of bounds")

        # restore TimeUnit
        self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new TimeUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

    # endregion

    # region ClassicalSizeShapeRadius
    def ClassicalSizeShapeRadius(self, oRadius: "IClassicalSizeShapeRadius"):
        Assert.assertIsNotNone(oRadius)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.ApogeeRadius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.PerigeeRadius)
        oRadius.ApogeeRadius = 987654.321
        oRadius.PerigeeRadius = 123456.789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.ApogeeRadius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.PerigeeRadius)
        Assert.assertAlmostEqual(987654.321, oRadius.ApogeeRadius, delta=0.0001)
        Assert.assertAlmostEqual(123456.789, oRadius.PerigeeRadius, delta=0.0001)
        bCaught: bool = False
        try:
            bCaught = False
            oRadius.SetSizeShapeRadius(123456.789, 987654.321)

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Expected exception did not occur.")

        # ApogeeRadius < PerigeeRadius
        oRadius.ApogeeRadius = 98765.4
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.ApogeeRadius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.PerigeeRadius)
        Assert.assertAlmostEqual(oRadius.ApogeeRadius, oRadius.PerigeeRadius, delta=0.01)
        # PerigeeRadius > ApogeeRadius
        oRadius.PerigeeRadius = 123456789.0
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.ApogeeRadius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.PerigeeRadius)
        Assert.assertAlmostEqual(oRadius.ApogeeRadius, oRadius.PerigeeRadius, delta=0.01)
        # SetSizeShapeRadius
        oRadius.SetSizeShapeRadius(987654.321, 123456.789)
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.ApogeeRadius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.PerigeeRadius)
        Assert.assertAlmostEqual(123456.789, oRadius.PerigeeRadius, delta=0.0001)
        Assert.assertAlmostEqual(987654.321, oRadius.ApogeeRadius, delta=0.0001)
        oRadius.SetSizeShapeRadius(98765.4321, 12345.6789)
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.ApogeeRadius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.PerigeeRadius)
        Assert.assertAlmostEqual(12345.6789, oRadius.PerigeeRadius, delta=1e-05)
        Assert.assertAlmostEqual(98765.4321, oRadius.ApogeeRadius, delta=1e-05)
        try:
            bCaught = False
            oRadius.ApogeeRadius = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ApogeeRadius out of bounds")

        try:
            bCaught = False
            oRadius.PerigeeRadius = -1.2

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set PerigeeRadius out of bounds")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

    # endregion

    # region ClassicalSizeShapeSemimajorAxis
    def ClassicalSizeShapeSemimajorAxis(self, oAxis: "IClassicalSizeShapeSemimajorAxis"):
        Assert.assertIsNotNone(oAxis)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t SemiMajorAxis is: {0}", oAxis.SemiMajorAxis)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oAxis.Eccentricity)
        oAxis.SemiMajorAxis = 123456.789
        oAxis.Eccentricity = 0.987654321
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t SemiMajorAxis is: {0}", oAxis.SemiMajorAxis)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oAxis.Eccentricity)
        Assert.assertEqual(123456.789, oAxis.SemiMajorAxis)
        Assert.assertEqual(0.987654321, oAxis.Eccentricity)
        bCaught: bool = False
        try:
            bCaught = False
            oAxis.SemiMajorAxis = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set SemiMajorAxis out of bounds")

        try:
            bCaught = False
            oAxis.Eccentricity = -1.2

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Eccentricity out of bounds")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

    # endregion

    # region ClassicalOrientation
    def ClassicalOrientation(self, oOrientation: "IClassicalOrientation"):
        Assert.assertIsNotNone(oOrientation)
        self.m_logger.WriteLine("\t\tOrientation test")

        # set AngleUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # base properties test
        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t Inclination is: {0}", oOrientation.Inclination)
        self.m_logger.WriteLine6("\t\t\t\t ArgOfPerigee is: {0}", oOrientation.ArgOfPerigee)
        oOrientation.Inclination = 1.23456
        oOrientation.ArgOfPerigee = 2.34561
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t Inclination is: {0}", oOrientation.Inclination)
        self.m_logger.WriteLine6("\t\t\t\t ArgOfPerigee is: {0}", oOrientation.ArgOfPerigee)
        Assert.assertEqual(1.23456, oOrientation.Inclination)
        Assert.assertEqual(2.34561, oOrientation.ArgOfPerigee)
        bCaught: bool = False
        try:
            bCaught = False
            oOrientation.Inclination = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Inclination out of bounds")

        try:
            bCaught = False
            oOrientation.ArgOfPerigee = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ArgOfPerigee out of bounds")

        # AscNode test
        self.m_logger.WriteLine6("\t\t\tCurent AscNodeType is: {0}", oOrientation.AscNodeType)
        # LAN test
        oOrientation.AscNodeType = AgEOrientationAscNode.eAscNodeLAN
        self.m_logger.WriteLine6("\t\t\tNew AscNodeType is: {0}", oOrientation.AscNodeType)
        Assert.assertEqual(AgEOrientationAscNode.eAscNodeLAN, oOrientation.AscNodeType)
        oLAN: "IOrientationAscNodeLAN" = clr.Convert(oOrientation.AscNode, IOrientationAscNodeLAN)
        Assert.assertIsNotNone(oLAN)
        self.m_logger.WriteLine6("\t\t\t\t Current LAN value is: {0}", oLAN.Value)
        oLAN.Value = 1.23456
        self.m_logger.WriteLine6("\t\t\t\t New LAN value is: {0}", oLAN.Value)
        Assert.assertEqual(1.23456, oLAN.Value)
        try:
            bCaught = False
            oLAN.Value = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LAN.Value out of bounds")

        # RAAN test
        oOrientation.AscNodeType = AgEOrientationAscNode.eAscNodeRAAN
        self.m_logger.WriteLine6("\t\t\tNew AscNodeType is: {0}", oOrientation.AscNodeType)
        Assert.assertEqual(AgEOrientationAscNode.eAscNodeRAAN, oOrientation.AscNodeType)
        oRAAN: "IOrientationAscNodeRAAN" = clr.Convert(oOrientation.AscNode, IOrientationAscNodeRAAN)
        Assert.assertIsNotNone(oRAAN)
        self.m_logger.WriteLine6("\t\t\t\t Current RAAN value is: {0}", oRAAN.Value)
        oRAAN.Value = 1.23456
        self.m_logger.WriteLine6("\t\t\t\t New RAAN value is: {0}", oRAAN.Value)
        Assert.assertEqual(1.23456, oRAAN.Value)
        try:
            bCaught = False
            oRAAN.Value = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set RAAN.Value out of bounds")

        # eAscNodeUnknown test
        try:
            oOrientation.AscNodeType = AgEOrientationAscNode.eAscNodeUnknown
            Assert.fail("Cannot set AgEOrientationAscNode.eAscNodeUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

    # endregion

    # region ClassicalLocation
    def ClassicalLocation(self, eType: "AgEClassicalLocation"):
        Assert.assertIsNotNone(self.m_oClassical)
        self.m_oClassical.LocationType = eType
        self.m_logger.WriteLine6("\t\tNew Location type is: {0}", self.m_oClassical.LocationType)
        Assert.assertEqual(eType, self.m_oClassical.LocationType)
        bCaught: bool = False
        if eType == AgEClassicalLocation.eLocationArgumentOfLatitude:
            # set AngleUnit
            strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
            self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
            self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
            Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

            oAOL: "IClassicalLocationArgumentOfLatitude" = clr.Convert(
                self.m_oClassical.Location, IClassicalLocationArgumentOfLatitude
            )
            Assert.assertIsNotNone(oAOL)
            self.m_logger.WriteLine6("\t\t\t Current ArgumentOfLatitude value is: {0}", oAOL.Value)
            oAOL.Value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New ArgumentOfLatitude value is: {0}", oAOL.Value)
            Assert.assertEqual(1.23456, oAOL.Value)
            try:
                bCaught = False
                oAOL.Value = -12345.6

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set ArgumentOfLatitude.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        elif eType == AgEClassicalLocation.eLocationEccentricAnomaly:
            # set AngleUnit
            strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
            self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
            self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
            Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

            oEccentric: "IClassicalLocationEccentricAnomaly" = clr.Convert(
                self.m_oClassical.Location, IClassicalLocationEccentricAnomaly
            )
            Assert.assertIsNotNone(oEccentric)
            self.m_logger.WriteLine6("\t\t\t Current EccentricAnomaly value is: {0}", oEccentric.Value)
            oEccentric.Value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New EccentricAnomaly value is: {0}", oEccentric.Value)
            Assert.assertEqual(1.23456, oEccentric.Value)
            try:
                bCaught = False
                oEccentric.Value = -12345.6

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set EccentricAnomaly.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        elif eType == AgEClassicalLocation.eLocationMeanAnomaly:
            # set AngleUnit
            strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
            self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
            self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
            Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

            oMean: "IClassicalLocationMeanAnomaly" = clr.Convert(
                self.m_oClassical.Location, IClassicalLocationMeanAnomaly
            )
            Assert.assertIsNotNone(oMean)
            self.m_logger.WriteLine6("\t\t\t Current MeanAnomaly value is: {0}", oMean.Value)
            oMean.Value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New MeanAnomaly value is: {0}", oMean.Value)
            Assert.assertEqual(1.23456, oMean.Value)
            try:
                bCaught = False
                oMean.Value = -12345.6

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set MeanAnomaly.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        elif eType == AgEClassicalLocation.eLocationTimePastAN:
            # set TimeUnit
            strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
            self.m_logger.WriteLine5("\t\t\tThe current TimeUnit is: {0}", strUnit)
            self.m_oUnits.SetCurrentUnit("TimeUnit", "hr")
            self.m_logger.WriteLine5("\t\t\tThe new TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
            Assert.assertEqual("hr", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

            oAN: "IClassicalLocationTimePastAN" = clr.Convert(self.m_oClassical.Location, IClassicalLocationTimePastAN)
            Assert.assertIsNotNone(oAN)
            self.m_logger.WriteLine6("\t\t\t Current TimePastAN value is: {0}", oAN.Value)
            oAN.Value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New TimePastAN value is: {0}", oAN.Value)
            Assert.assertEqual(1.23456, oAN.Value)
            try:
                bCaught = False
                oAN.Value = -123456000000000000000000000000.0

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set TimePastAN.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new TimeUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        elif eType == AgEClassicalLocation.eLocationTimePastPerigee:
            # set TimeUnit
            strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit")
            self.m_logger.WriteLine5("\t\t\tThe current TimeUnit is: {0}", strUnit)
            self.m_oUnits.SetCurrentUnit("TimeUnit", "hr")
            self.m_logger.WriteLine5("\t\t\tThe new TimeUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
            Assert.assertEqual("hr", self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))

            oPerigee: "IClassicalLocationTimePastPerigee" = clr.Convert(
                self.m_oClassical.Location, IClassicalLocationTimePastPerigee
            )
            Assert.assertIsNotNone(oPerigee)
            self.m_logger.WriteLine6("\t\t\t Current TimePastPerigee value is: {0}", oPerigee.Value)
            oPerigee.Value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New TimePastPerigee value is: {0}", oPerigee.Value)
            Assert.assertEqual(1.23456, oPerigee.Value)
            try:
                bCaught = False
                oPerigee.Value = -123456000000000000000000000000.0

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set TimePastPerigee.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.SetCurrentUnit("TimeUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new TimeUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("TimeUnit"))
        elif eType == AgEClassicalLocation.eLocationTrueAnomaly:
            # set AngleUnit
            strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
            self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
            self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
            Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

            oTrue: "IClassicalLocationTrueAnomaly" = clr.Convert(
                self.m_oClassical.Location, IClassicalLocationTrueAnomaly
            )
            Assert.assertIsNotNone(oTrue)
            self.m_logger.WriteLine6("\t\t\t Current TrueAnomaly value is: {0}", oTrue.Value)
            oTrue.Value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New TrueAnomaly value is: {0}", oTrue.Value)
            Assert.assertEqual(1.23456, oTrue.Value)
            try:
                bCaught = False
                oTrue.Value = -12345.6

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set TrueAnomaly.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        else:
            Assert.fail("Invalid Location type!")

    # endregion

    # region GeodeticTest
    def GeodeticTest(self):
        Assert.assertIsNotNone(self.m_oGeodetic)
        self.Test_IAgOrbitState(self.m_oGeodetic)

        # set AngleUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # basic properties test
        # m_logger.WriteLine("\t\tCurrent values:");
        # m_logger.WriteLine("\t\t\t Latitude is: {0}", m_oGeodetic.Latitude);
        # m_logger.WriteLine("\t\t\t LatitudeRate is: {0}", m_oGeodetic.LatitudeRate);
        # m_logger.WriteLine("\t\t\t Longitude is: {0}", m_oGeodetic.Longitude);
        # m_logger.WriteLine("\t\t\t LongitudeRate is: {0}", m_oGeodetic.LongitudeRate);
        self.m_oGeodetic.Latitude = 1.23456789
        self.m_oGeodetic.LatitudeRate = 2.34567891
        self.m_oGeodetic.Longitude = 3.45678912
        self.m_oGeodetic.LongitudeRate = 4.56789123
        # m_logger.WriteLine("\t\tNew values:");
        # m_logger.WriteLine("\t\t\t Latitude is: {0}", m_oGeodetic.Latitude);
        # m_logger.WriteLine("\t\t\t LatitudeRate is: {0}", m_oGeodetic.LatitudeRate);
        # m_logger.WriteLine("\t\t\t Longitude is: {0}", m_oGeodetic.Longitude);
        # m_logger.WriteLine("\t\t\t LongitudeRate is: {0}", m_oGeodetic.LongitudeRate);
        Assert.assertEqual(1.23456789, self.m_oGeodetic.Latitude)
        Assert.assertEqual(2.34567891, self.m_oGeodetic.LatitudeRate)
        Assert.assertEqual(3.45678912, self.m_oGeodetic.Longitude)
        Assert.assertEqual(4.56789123, self.m_oGeodetic.LongitudeRate)
        # out of bounds
        bCaught: bool = False
        try:
            bCaught = False
            self.m_oGeodetic.Latitude = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Latitude out of bounds")

        try:
            bCaught = False
            self.m_oGeodetic.LatitudeRate = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LatitudeRate out of bounds")

        try:
            bCaught = False
            self.m_oGeodetic.Longitude = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Longitude out of bounds")

        try:
            bCaught = False
            self.m_oGeodetic.LongitudeRate = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LongitudeRate out of bounds")

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # CoordinateSystem test
        arTypes = self.m_oGeodetic.SupportedCoordinateSystemTypes
        self.m_logger.WriteLine3("\t\tGeodetic supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                clr.Convert(int(arTypes[iIndex][0]), AgECoordinateSystem),
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oGeodetic.CoordinateSystemType)
        try:
            bCaught = False
            # eCoordinateSystemAlignmentAtEpoch
            self.CoordinateSystemTest(
                self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemAlignmentAtEpoch
            )

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemAlignmentAtEpoch")

        try:
            bCaught = False
            # eCoordinateSystemB1950
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemB1950)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemB1950")

        # eCoordinateSystemFixed
        self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemFixed)
        try:
            bCaught = False
            # eCoordinateSystemJ2000
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemJ2000)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemJ2000")

        try:
            bCaught = False
            # eCoordinateSystemMeanOfDate
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfDate)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemMeanOfDate")

        try:
            bCaught = False
            # eCoordinateSystemMeanOfEpoch
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfEpoch)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemMeanOfEpoch")

        try:
            bCaught = False
            # eCoordinateSystemTEMEOfDate
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfDate)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemTEMEOfDate")

        try:
            bCaught = False
            # eCoordinateSystemTEMEOfEpoch
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfEpoch)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemTEMEOfEpoch")

        try:
            bCaught = False
            # eCoordinateSystemTrueOfDate
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfDate)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemTrueOfDate")

        try:
            bCaught = False
            # eCoordinateSystemTrueOfEpoch
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfEpoch)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemTrueOfEpoch")

        try:
            bCaught = False
            # eCoordinateSystemTrueOfRefDate
            self.CoordinateSystemTest(
                self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate
            )

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemTrueOfRefDate")

        # eCoordinateSystemUnknown
        try:
            self.CoordinateSystemTest(self.m_oGeodetic.OrbitStateType, AgECoordinateSystem.eCoordinateSystemUnknown)
            Assert.fail("Cannot set AgECoordinateSystem.eCoordinateSystemUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # Geodetic Size (Altitude) test
        self.m_logger.WriteLine6("\t\tCurrent Size type is: {0}", self.m_oGeodetic.SizeType)
        self.m_oGeodetic.SizeType = AgEGeodeticSize.eSizeAltitude
        self.m_logger.WriteLine6("\t\tNew Size type is: {0}", self.m_oGeodetic.SizeType)
        Assert.assertEqual(AgEGeodeticSize.eSizeAltitude, self.m_oGeodetic.SizeType)
        oAltitude: "IGeodeticSizeAltitude" = clr.Convert(self.m_oGeodetic.Size, IGeodeticSizeAltitude)
        Assert.assertIsNotNone(oAltitude)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t Altitude is: {0}", oAltitude.Altitude)
        self.m_logger.WriteLine6("\t\t\t\t Rate is: {0}", oAltitude.Rate)
        oAltitude.Altitude = 1.23456789
        oAltitude.Rate = 2.34567891
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t Altitude is: {0}", oAltitude.Altitude)
        self.m_logger.WriteLine6("\t\t\t\t Rate is: {0}", oAltitude.Rate)
        Assert.assertEqual(1.23456789, oAltitude.Altitude)
        Assert.assertEqual(2.34567891, oAltitude.Rate)
        try:
            bCaught = False
            oAltitude.Altitude = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Altitude out of bounds")

        try:
            bCaught = False
            oAltitude.Rate = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Rate out of bounds")

        # Geodetic Size (Radius) test
        self.m_oGeodetic.SizeType = AgEGeodeticSize.eSizeRadius
        self.m_logger.WriteLine6("\t\tNew Size type is: {0}", self.m_oGeodetic.SizeType)
        Assert.assertEqual(AgEGeodeticSize.eSizeRadius, self.m_oGeodetic.SizeType)
        oRadius: "IGeodeticSizeRadius" = clr.Convert(self.m_oGeodetic.Size, IGeodeticSizeRadius)
        Assert.assertIsNotNone(oRadius)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t Radius is: {0}", oRadius.Radius)
        self.m_logger.WriteLine6("\t\t\t\t Rate is: {0}", oRadius.Rate)
        oRadius.Radius = 1.23456789
        oRadius.Rate = 2.34567891
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t Radius is: {0}", oRadius.Radius)
        self.m_logger.WriteLine6("\t\t\t\t Rate is: {0}", oRadius.Rate)
        Assert.assertEqual(1.23456789, oRadius.Radius)
        Assert.assertEqual(2.34567891, oRadius.Rate)
        try:
            bCaught = False
            oRadius.Radius = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Radius out of bounds")

        try:
            bCaught = False
            oRadius.Rate = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Rate out of bounds")

        # Geodetic Size (Unknown) test
        try:
            bCaught = False
            self.m_oGeodetic.SizeType = AgEGeodeticSize.eGeodeticSizeUnknown

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eGeodeticSizeUnknown")

    # endregion

    # region DelaunayTest
    def DelaunayTest(self):
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.Test_IAgOrbitState(self.m_oDelaunay)

        # set AngleUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # basic properties test
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t MeanAnomaly is: {0}", self.m_oDelaunay.MeanAnomaly)
        self.m_logger.WriteLine6("\t\t\t ArgOfPerigee is: {0}", self.m_oDelaunay.ArgOfPeriapsis)
        self.m_logger.WriteLine6("\t\t\t RAAN is: {0}", self.m_oDelaunay.RAAN)
        self.m_oDelaunay.MeanAnomaly = 1.23456789
        self.m_oDelaunay.ArgOfPeriapsis = 2.34567891
        self.m_oDelaunay.RAAN = 3.45678912
        self.m_logger.WriteLine("\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t MeanAnomaly is: {0}", self.m_oDelaunay.MeanAnomaly)
        self.m_logger.WriteLine6("\t\t\t ArgOfPerigee is: {0}", self.m_oDelaunay.ArgOfPeriapsis)
        self.m_logger.WriteLine6("\t\t\t RAAN is: {0}", self.m_oDelaunay.RAAN)
        Assert.assertEqual(1.23456789, self.m_oDelaunay.MeanAnomaly)
        Assert.assertEqual(2.34567891, self.m_oDelaunay.ArgOfPeriapsis)
        Assert.assertEqual(3.45678912, self.m_oDelaunay.RAAN)
        # out of bounds
        bCaught: bool = False
        try:
            bCaught = False
            self.m_oDelaunay.MeanAnomaly = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MeanAnomaly out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.ArgOfPeriapsis = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ArgOfPeriapsis out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.RAAN = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set RAAN out of bounds")

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # L test
        self.DelaunayLTest()

        # H test
        self.DelaunayHTest()

        # G test
        self.DelaunayGTest()

        # CoordinateSystem test
        arTypes = self.m_oDelaunay.SupportedCoordinateSystemTypes
        self.m_logger.WriteLine3("\t\tDelaunay supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                clr.Convert(int(arTypes[iIndex][0]), AgECoordinateSystem),
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oDelaunay.CoordinateSystemType)
        # eCoordinateSystemAlignmentAtEpoch
        self.CoordinateSystemTest(
            self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemAlignmentAtEpoch
        )

        # eCoordinateSystemB1950
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemB1950)
        # eCoordinateSystemFixed
        try:
            self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemFixed)
            Assert.fail("Cannot set AgECoordinateSystem.eCoordinateSystemFixed.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # eCoordinateSystemJ2000
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemJ2000)
        # eCoordinateSystemICRF
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemICRF)
        # eCoordinateSystemMeanOfDate
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfDate)
        # eCoordinateSystemMeanOfEpoch
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfEpoch)
        # eCoordinateSystemTEMEOfDate
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfDate)
        # eCoordinateSystemTEMEOfEpoch
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfEpoch)
        # eCoordinateSystemTrueOfDate
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfDate)
        # eCoordinateSystemTrueOfEpoch
        self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfEpoch)
        # eCoordinateSystemTrueOfRefDate
        # GetLicenses
        oLicenses: "ansys.stk.core.stkutil.IExecCmdResult" = None
        oLicenses = self.m_oApplication.ExecuteCommand("GetLicenses /")
        Assert.assertIsNotNone(oLicenses)

        iI: int = 0
        while iI < oLicenses.Count:
            strLicense: str = oLicenses[iI]
            if strLicense.find("PODS") >= 0:
                if strLicense.find("No License") >= 0:
                    # No License
                    try:
                        bCaught = False
                        self.CoordinateSystemTest(
                            self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate
                        )

                    except Exception as e:
                        bCaught = True
                        self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set eCoordinateSystemTrueOfRefDate")

                else:
                    # License available
                    self.CoordinateSystemTest(
                        self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate
                    )

                break

            iI += 1

        # eCoordinateSystemUnknown
        try:
            self.CoordinateSystemTest(self.m_oDelaunay.OrbitStateType, AgECoordinateSystem.eCoordinateSystemUnknown)
            Assert.fail("Cannot set AgECoordinateSystem.eCoordinateSystemUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

    # endregion

    # region DelaunayLTest
    def DelaunayLTest(self):
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.m_logger.WriteLine6("\t\tCurrent LType is: {0}", self.m_oDelaunay.LType)
        self.m_oDelaunay.LType = AgEDelaunayLType.eL
        self.m_logger.WriteLine6("\t\tNew LType is: {0}", self.m_oDelaunay.LType)
        Assert.assertEqual(AgEDelaunayLType.eL, self.m_oDelaunay.LType)
        oL: "IDelaunayL" = clr.Convert(self.m_oDelaunay.L, IDelaunayL)
        Assert.assertIsNotNone(oL)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t L is: {0}", oL.L)
        oL.L = 12345678.9
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t L is: {0}", oL.L)
        Assert.assertEqual(12345678.9, oL.L)
        bCaught: bool = False
        try:
            bCaught = False
            oL.L = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set L out of bounds")

        self.m_oDelaunay.LType = AgEDelaunayLType.eLOverSQRTmu
        self.m_logger.WriteLine6("\t\tNew LType is: {0}", self.m_oDelaunay.LType)
        Assert.assertEqual(AgEDelaunayLType.eLOverSQRTmu, self.m_oDelaunay.LType)
        oLOver: "IDelaunayLOverSQRTmu" = clr.Convert(self.m_oDelaunay.L, IDelaunayLOverSQRTmu)
        Assert.assertIsNotNone(oLOver)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t LOverSQRTmu is: {0}", oLOver.LOverSQRTmu)
        oLOver.LOverSQRTmu = 12345678.9
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t LOverSQRTmu is: {0}", oLOver.LOverSQRTmu)
        Assert.assertAlmostEqual(12345678.9, oLOver.LOverSQRTmu, delta=0.01)
        try:
            bCaught = False
            oLOver.LOverSQRTmu = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LOverSQRTmu out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.LType = AgEDelaunayLType.eDelaunayLTypeUnknown

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eDelaunayLTypeUnknown")

    # endregion

    # region DelaunayHTest
    def DelaunayHTest(self):
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.m_logger.WriteLine6("\t\tCurrent HType is: {0}", self.m_oDelaunay.HType)
        self.m_oDelaunay.HType = AgEDelaunayHType.eH
        self.m_logger.WriteLine6("\t\tNew HType is: {0}", self.m_oDelaunay.HType)
        Assert.assertEqual(AgEDelaunayHType.eH, self.m_oDelaunay.HType)
        oH: "IDelaunayH" = clr.Convert(self.m_oDelaunay.H, IDelaunayH)
        Assert.assertIsNotNone(oH)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t H is: {0}", oH.H)
        oH.H = 12.3456789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t H is: {0}", oH.H)
        Assert.assertEqual(12.3456789, oH.H)
        bCaught: bool = False
        try:
            bCaught = False
            oH.H = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set H out of bounds")

        self.m_oDelaunay.HType = AgEDelaunayHType.eHOverSQRTmu
        self.m_logger.WriteLine6("\t\tNew HType is: {0}", self.m_oDelaunay.HType)
        Assert.assertEqual(AgEDelaunayHType.eHOverSQRTmu, self.m_oDelaunay.HType)
        oHOver: "IDelaunayHOverSQRTmu" = clr.Convert(self.m_oDelaunay.H, IDelaunayHOverSQRTmu)
        Assert.assertIsNotNone(oHOver)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t HOverSQRTmu is: {0}", oHOver.HOverSQRTmu)
        oHOver.HOverSQRTmu = 12.3456789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t HOverSQRTmu is: {0}", oHOver.HOverSQRTmu)
        Assert.assertAlmostEqual(12.3456789, oHOver.HOverSQRTmu, delta=1e-08)
        try:
            bCaught = False
            oHOver.HOverSQRTmu = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set HOverSQRTmu out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.HType = AgEDelaunayHType.eDelaunayHTypeUnknown

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eDelaunayHTypeUnknown")

    # endregion

    # region DelaunayGTest
    def DelaunayGTest(self):
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.m_logger.WriteLine6("\t\tCurrent GType is: {0}", self.m_oDelaunay.GType)
        self.m_oDelaunay.GType = AgEDelaunayGType.eG
        self.m_logger.WriteLine6("\t\tNew GType is: {0}", self.m_oDelaunay.GType)
        Assert.assertEqual(AgEDelaunayGType.eG, self.m_oDelaunay.GType)
        oG: "IDelaunayG" = clr.Convert(self.m_oDelaunay.G, IDelaunayG)
        Assert.assertIsNotNone(oG)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t G is: {0}", oG.G)
        oG.G = 12345.6789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t G is: {0}", oG.G)
        Assert.assertEqual(12345.6789, oG.G)
        bCaught: bool = False
        try:
            bCaught = False
            oG.G = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set G out of bounds")

        self.m_oDelaunay.GType = AgEDelaunayGType.eGOverSQRTmu
        self.m_logger.WriteLine6("\t\tNew GType is: {0}", self.m_oDelaunay.GType)
        Assert.assertEqual(AgEDelaunayGType.eGOverSQRTmu, self.m_oDelaunay.GType)
        oGOver: "IDelaunayGOverSQRTmu" = clr.Convert(self.m_oDelaunay.G, IDelaunayGOverSQRTmu)
        Assert.assertIsNotNone(oGOver)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t GOverSQRTmu is: {0}", oGOver.GOverSQRTmu)
        oGOver.GOverSQRTmu = 12345.6789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t GOverSQRTmu is: {0}", oGOver.GOverSQRTmu)
        Assert.assertAlmostEqual(12345.6789, oGOver.GOverSQRTmu, delta=0.0001)
        try:
            bCaught = False
            oGOver.GOverSQRTmu = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set GOverSQRTmu out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.GType = AgEDelaunayGType.eDelaunayGTypeUnknown

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eDelaunayGTypeUnknown")

    # endregion

    # region EquinoctialTest
    def EquinoctialTest(self):
        Assert.assertIsNotNone(self.m_oEquinoctial)
        self.Test_IAgOrbitState(self.m_oEquinoctial)

        bCaught: bool = False

        # CoordinateSystem test
        arTypes = self.m_oEquinoctial.SupportedCoordinateSystemTypes
        self.m_logger.WriteLine3("\t\tEquinoctial supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                clr.Convert(int(arTypes[iIndex][0]), AgECoordinateSystem),
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oEquinoctial.CoordinateSystemType)
        # eCoordinateSystemAlignmentAtEpoch
        self.CoordinateSystemTest(
            self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemAlignmentAtEpoch
        )
        # eCoordinateSystemB1950
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemB1950)
        try:
            bCaught = False
            # eCoordinateSystemFixed
            self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemFixed)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemFixed")

        # eCoordinateSystemJ2000
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemJ2000)
        # eCoordinateSystemICRF
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemICRF)
        # eCoordinateSystemMeanOfDate
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfDate)
        # eCoordinateSystemMeanOfEpoch
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfEpoch)
        # eCoordinateSystemTEMEOfDate
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfDate)
        # eCoordinateSystemTEMEOfEpoch
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfEpoch)
        # eCoordinateSystemTrueOfDate
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfDate)
        # eCoordinateSystemTrueOfEpoch
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfEpoch)
        try:
            # eCoordinateSystemTrueOfRefDate
            self.CoordinateSystemTest(
                self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate
            )

        except:
            self.m_logger.WriteLine("\t\tThe eCoordinateSystemTrueOfRefDate does not supported by current licenses.")

        # eCoordinateSystemUnknown
        try:
            self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemUnknown)
            Assert.fail("Cannot set AgECoordinateSystem.eCoordinateSystemUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # set AngleUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # basic properties test
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t H is: {0}", self.m_oEquinoctial.H)
        self.m_logger.WriteLine6("\t\t\t K is: {0}", self.m_oEquinoctial.K)
        self.m_logger.WriteLine6("\t\t\t P is: {0}", self.m_oEquinoctial.P)
        self.m_logger.WriteLine6("\t\t\t Q is: {0}", self.m_oEquinoctial.Q)
        self.m_logger.WriteLine6("\t\t\t MeanLongitude is: {0}", self.m_oEquinoctial.MeanLongitude)
        self.m_logger.WriteLine6("\t\t\t Formulation is: {0}", self.m_oEquinoctial.Formulation)
        self.m_oEquinoctial.H = 0.123456789
        self.m_oEquinoctial.K = -0.234567891
        self.m_oEquinoctial.P = 3.45678912
        self.m_oEquinoctial.Q = 4.56789123
        self.m_oEquinoctial.MeanLongitude = 5.67891234
        self.m_oEquinoctial.Formulation = AgEEquinoctialFormulation.eFormulationPosigrade
        self.m_logger.WriteLine("\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t H is: {0}", self.m_oEquinoctial.H)
        self.m_logger.WriteLine6("\t\t\t K is: {0}", self.m_oEquinoctial.K)
        self.m_logger.WriteLine6("\t\t\t P is: {0}", self.m_oEquinoctial.P)
        self.m_logger.WriteLine6("\t\t\t Q is: {0}", self.m_oEquinoctial.Q)
        self.m_logger.WriteLine6("\t\t\t MeanLongitude is: {0}", self.m_oEquinoctial.MeanLongitude)
        self.m_logger.WriteLine6("\t\t\t Formulation is: {0}", self.m_oEquinoctial.Formulation)
        Assert.assertEqual(0.123456789, self.m_oEquinoctial.H)
        Assert.assertEqual(-0.234567891, self.m_oEquinoctial.K)
        Assert.assertEqual(3.45678912, self.m_oEquinoctial.P)
        Assert.assertEqual(4.56789123, self.m_oEquinoctial.Q)
        Assert.assertEqual(5.67891234, self.m_oEquinoctial.MeanLongitude)
        Assert.assertEqual(AgEEquinoctialFormulation.eFormulationPosigrade, self.m_oEquinoctial.Formulation)
        self.m_oEquinoctial.Formulation = AgEEquinoctialFormulation.eFormulationRetrograde
        self.m_logger.WriteLine6("\t\t\t Formulation is: {0}", self.m_oEquinoctial.Formulation)
        Assert.assertEqual(AgEEquinoctialFormulation.eFormulationRetrograde, self.m_oEquinoctial.Formulation)
        # out of bounds
        try:
            bCaught = False
            self.m_oEquinoctial.H = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set H out of bounds")

        try:
            bCaught = False
            self.m_oEquinoctial.K = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set K out of bounds")

        try:
            bCaught = False
            self.m_oEquinoctial.P = 123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set P out of bounds")

        try:
            bCaught = False
            self.m_oEquinoctial.Q = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Q out of bounds")

        try:
            bCaught = False
            self.m_oEquinoctial.MeanLongitude = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MeanLongitude out of bounds")

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # SizeShape test
        self.m_logger.WriteLine6("\t\tCurrent SizeShape type is: {0}", self.m_oEquinoctial.SizeShapeType)
        self.EquinoctialSizeShape(AgEEquinoctialSizeShape.eEquinoctialSizeShapeMeanMotion)
        self.EquinoctialSizeShape(AgEEquinoctialSizeShape.eEquinoctialSizeShapeSemimajorAxis)
        try:
            self.EquinoctialSizeShape(AgEEquinoctialSizeShape.eEquinoctialSizeShapeUnknown)
            Assert.fail("Cannot set AgEEquinoctialSizeShape.eEquinoctialSizeShapeUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

    # endregion

    # region EquinoctialSizeShape
    def EquinoctialSizeShape(self, eShapeType: "AgEEquinoctialSizeShape"):
        Assert.assertIsNotNone(self.m_oEquinoctial)
        # set shape type
        self.m_oEquinoctial.SizeShapeType = eShapeType
        self.m_logger.WriteLine6("\t\tNew SizeShape type is: {0}", self.m_oEquinoctial.SizeShapeType)
        Assert.assertEqual(eShapeType, self.m_oEquinoctial.SizeShapeType)
        if eShapeType == AgEEquinoctialSizeShape.eEquinoctialSizeShapeMeanMotion:
            self.EquinoctialSizeShapeMeanMotion(
                clr.Convert(self.m_oEquinoctial.SizeShape, IEquinoctialSizeShapeMeanMotion)
            )
        elif eShapeType == AgEEquinoctialSizeShape.eEquinoctialSizeShapeSemimajorAxis:
            self.EquinoctialSizeShapeSemimajorAxis(
                clr.Convert(self.m_oEquinoctial.SizeShape, IEquinoctialSizeShapeSemimajorAxis)
            )
        else:
            Assert.fail("Invalid SizeShape type!")

    # endregion

    # region EquinoctialSizeShapeMeanMotion
    def EquinoctialSizeShapeMeanMotion(self, oMeanMotion: "IEquinoctialSizeShapeMeanMotion"):
        Assert.assertIsNotNone(oMeanMotion)
        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t MeanMotion is: {0}", oMeanMotion.MeanMotion)
        oMeanMotion.MeanMotion = 123456.789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t MeanMotion is: {0}", oMeanMotion.MeanMotion)
        Assert.assertAlmostEqual(123456.789, oMeanMotion.MeanMotion, delta=0.0001)
        bCaught: bool = False
        try:
            bCaught = False
            oMeanMotion.MeanMotion = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MeanMotion out of bounds")

    # endregion

    # region EquinoctialSizeShapeSemimajorAxis
    def EquinoctialSizeShapeSemimajorAxis(self, oAxis: "IEquinoctialSizeShapeSemimajorAxis"):
        Assert.assertIsNotNone(oAxis)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t SemiMajorAxis is: {0}", oAxis.SemiMajorAxis)
        oAxis.SemiMajorAxis = 123456.789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t SemiMajorAxis is: {0}", oAxis.SemiMajorAxis)
        Assert.assertEqual(123456.789, oAxis.SemiMajorAxis)
        bCaught: bool = False
        try:
            bCaught = False
            oAxis.SemiMajorAxis = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set SemiMajorAxis out of bounds")

        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))

    # endregion

    # region MixedSphericalTest
    def MixedSphericalTest(self):
        Assert.assertIsNotNone(self.m_oMixed)
        self.Test_IAgOrbitState(self.m_oMixed)

        bCaught: bool = False

        # CoordinateSystem test
        arTypes = self.m_oMixed.SupportedCoordinateSystemTypes
        self.m_logger.WriteLine3("\t\tMixedSpherical supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                clr.Convert(int(arTypes[iIndex][0]), AgECoordinateSystem),
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oMixed.CoordinateSystemType)
        # eCoordinateSystemAlignmentAtEpoch
        self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemAlignmentAtEpoch)
        # eCoordinateSystemB1950
        self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemB1950)
        try:
            bCaught = False
            # eCoordinateSystemFixed
            self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemFixed)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set eCoordinateSystemFixed")

        # eCoordinateSystemJ2000
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemJ2000)
        # eCoordinateSystemICRF
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemICRF)
        # eCoordinateSystemMeanOfDate
        self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfDate)
        # eCoordinateSystemMeanOfEpoch
        self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfEpoch)
        # eCoordinateSystemTEMEOfDate
        self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfDate)
        # eCoordinateSystemTEMEOfEpoch
        self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfEpoch)
        # eCoordinateSystemTrueOfDate
        self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfDate)
        # eCoordinateSystemTrueOfEpoch
        self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfEpoch)
        try:
            # eCoordinateSystemTrueOfRefDate
            self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate)

        except:
            self.m_logger.WriteLine("\t\tThe eCoordinateSystemTrueOfRefDate does not supported by current licenses.")

        # eCoordinateSystemUnknown
        try:
            self.CoordinateSystemTest(self.m_oMixed.OrbitStateType, AgECoordinateSystem.eCoordinateSystemUnknown)
            Assert.fail("Cannot set AgECoordinateSystem.eCoordinateSystemUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # set AngleUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # basic properties test
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t Latitude is: {0}", self.m_oMixed.Latitude)
        self.m_logger.WriteLine6("\t\t\t Longitude is: {0}", self.m_oMixed.Longitude)
        self.m_logger.WriteLine6("\t\t\t Altitude is: {0}", self.m_oMixed.Altitude)
        self.m_logger.WriteLine6("\t\t\t Azimuth is: {0}", self.m_oMixed.Azimuth)
        self.m_logger.WriteLine6("\t\t\t Velocity is: {0}", self.m_oMixed.Velocity)
        self.m_oMixed.Latitude = -1.2345
        self.m_oMixed.Longitude = 2.3451
        self.m_oMixed.Altitude = 3456789.12
        self.m_oMixed.Azimuth = 4.5123
        self.m_oMixed.Velocity = 56789.1234
        self.m_logger.WriteLine("\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t Latitude is: {0}", self.m_oMixed.Latitude)
        self.m_logger.WriteLine6("\t\t\t Longitude is: {0}", self.m_oMixed.Longitude)
        self.m_logger.WriteLine6("\t\t\t Altitude is: {0}", self.m_oMixed.Altitude)
        self.m_logger.WriteLine6("\t\t\t Azimuth is: {0}", self.m_oMixed.Azimuth)
        self.m_logger.WriteLine6("\t\t\t Velocity is: {0}", self.m_oMixed.Velocity)
        Assert.assertEqual(-1.2345, self.m_oMixed.Latitude)
        Assert.assertEqual(2.3451, self.m_oMixed.Longitude)
        Assert.assertEqual(3456789.12, self.m_oMixed.Altitude)
        Assert.assertEqual(4.5123, self.m_oMixed.Azimuth)
        Assert.assertEqual(56789.1234, self.m_oMixed.Velocity)
        # out of bounds
        try:
            bCaught = False
            self.m_oMixed.Latitude = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Latitude out of bounds")

        try:
            bCaught = False
            self.m_oMixed.Longitude = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Longitude out of bounds")

        try:
            bCaught = False
            self.m_oMixed.Altitude = 123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Altitude out of bounds")

        try:
            bCaught = False
            self.m_oMixed.Azimuth = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Azimuth out of bounds")

        try:
            bCaught = False
            self.m_oMixed.Velocity = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Velocity out of bounds")

        # FPA (Horizontal) test
        self.m_logger.WriteLine6("\t\tCurrent FPA type is: {0}", self.m_oMixed.FPAType)
        self.m_oMixed.FPAType = AgEMixedSphericalFPA.eFPAHorizontal
        self.m_logger.WriteLine6("\t\tNew FPA type is: {0}", self.m_oMixed.FPAType)
        Assert.assertEqual(AgEMixedSphericalFPA.eFPAHorizontal, self.m_oMixed.FPAType)
        oHorizontal: "IMixedSphericalFPAHorizontal" = clr.Convert(self.m_oMixed.FPA, IMixedSphericalFPAHorizontal)
        Assert.assertIsNotNone(oHorizontal)
        self.m_logger.WriteLine6("\t\t\tCurrent FPA is: {0}", oHorizontal.FPA)
        oHorizontal.FPA = 1.2345
        self.m_logger.WriteLine6("\t\t\tNew FPA is: {0}", oHorizontal.FPA)
        Assert.assertEqual(1.2345, oHorizontal.FPA)
        try:
            bCaught = False
            oHorizontal.FPA = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FPA out of bounds")

        # FPA (Vertical) test
        self.m_oMixed.FPAType = AgEMixedSphericalFPA.eFPAVertical
        self.m_logger.WriteLine6("\t\tNew FPA type is: {0}", self.m_oMixed.FPAType)
        Assert.assertEqual(AgEMixedSphericalFPA.eFPAVertical, self.m_oMixed.FPAType)
        oVertical: "IMixedSphericalFPAVertical" = clr.Convert(self.m_oMixed.FPA, IMixedSphericalFPAVertical)
        Assert.assertIsNotNone(oVertical)
        self.m_logger.WriteLine6("\t\t\tCurrent FPA is: {0}", oVertical.FPA)
        oVertical.FPA = -1.2345
        self.m_logger.WriteLine6("\t\t\tNew FPA is: {0}", oVertical.FPA)
        Assert.assertAlmostEqual(-1.2345, oVertical.FPA, delta=1e-05)
        try:
            bCaught = False
            oVertical.FPA = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FPA out of bounds")

        # FPA (Vertical) test
        try:
            self.m_oMixed.FPAType = AgEMixedSphericalFPA.eFPAUnknown
            Assert.fail("Cannot set AgEMixedSphericalFPA.eFPAUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

    # endregion

    # region SphericalTest
    def SphericalTest(self):
        Assert.assertIsNotNone(self.m_oSpherical)
        self.Test_IAgOrbitState(self.m_oSpherical)

        bCaught: bool = False

        # CoordinateSystem test
        arTypes = self.m_oSpherical.SupportedCoordinateSystemTypes
        self.m_logger.WriteLine3("\t\tSpherical supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})",
                iIndex,
                arTypes[iIndex][1],
                clr.Convert(int(arTypes[iIndex][0]), AgECoordinateSystem),
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oSpherical.CoordinateSystemType)
        # eCoordinateSystemAlignmentAtEpoch
        self.CoordinateSystemTest(
            self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemAlignmentAtEpoch
        )
        # eCoordinateSystemB1950
        self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemB1950)
        # eCoordinateSystemFixed
        self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemFixed)
        # eCoordinateSystemJ2000
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemJ2000)
        # eCoordinateSystemICRF
        self.CoordinateSystemTest(self.m_oEquinoctial.OrbitStateType, AgECoordinateSystem.eCoordinateSystemICRF)
        # eCoordinateSystemMeanOfDate
        self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfDate)
        # eCoordinateSystemMeanOfEpoch
        self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemMeanOfEpoch)
        # eCoordinateSystemTEMEOfDate
        self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfDate)
        # eCoordinateSystemTEMEOfEpoch
        self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTEMEOfEpoch)
        # eCoordinateSystemTrueOfDate
        self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfDate)
        # eCoordinateSystemTrueOfEpoch
        self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfEpoch)
        try:
            # eCoordinateSystemTrueOfRefDate
            self.CoordinateSystemTest(
                self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemTrueOfRefDate
            )

        except:
            self.m_logger.WriteLine("\t\tThe eCoordinateSystemTrueOfRefDate does not supported by current licenses.")

        # eCoordinateSystemUnknown
        try:
            self.CoordinateSystemTest(self.m_oSpherical.OrbitStateType, AgECoordinateSystem.eCoordinateSystemUnknown)
            Assert.fail("Cannot set AgECoordinateSystem.eCoordinateSystemUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # set AngleUnit
        strUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        # basic properties test
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t RightAscension is: {0}", self.m_oSpherical.RightAscension)
        self.m_logger.WriteLine6("\t\t\t Declination is: {0}", self.m_oSpherical.Declination)
        self.m_logger.WriteLine6("\t\t\t Radius is: {0}", self.m_oSpherical.Radius)
        self.m_logger.WriteLine6("\t\t\t Azimuth is: {0}", self.m_oSpherical.Azimuth)
        self.m_logger.WriteLine6("\t\t\t Velocity is: {0}", self.m_oSpherical.Velocity)
        self.m_oSpherical.RightAscension = 2.3451
        self.m_oSpherical.Declination = -1.2345
        self.m_oSpherical.Radius = 3456789.12
        self.m_oSpherical.Azimuth = 4.5123
        self.m_oSpherical.Velocity = 56789.1234
        self.m_logger.WriteLine("\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t RightAscension is: {0}", self.m_oSpherical.RightAscension)
        self.m_logger.WriteLine6("\t\t\t Declination is: {0}", self.m_oSpherical.Declination)
        self.m_logger.WriteLine6("\t\t\t Radius is: {0}", self.m_oSpherical.Radius)
        self.m_logger.WriteLine6("\t\t\t Azimuth is: {0}", self.m_oSpherical.Azimuth)
        self.m_logger.WriteLine6("\t\t\t Velocity is: {0}", self.m_oSpherical.Velocity)
        Assert.assertEqual(2.3451, self.m_oSpherical.RightAscension)
        Assert.assertEqual(-1.2345, self.m_oSpherical.Declination)
        Assert.assertEqual(3456789.12, self.m_oSpherical.Radius)
        Assert.assertEqual(4.5123, self.m_oSpherical.Azimuth)
        Assert.assertEqual(56789.1234, self.m_oSpherical.Velocity)
        # out of bounds
        try:
            bCaught = False
            self.m_oSpherical.RightAscension = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set RightAscension out of bounds")

        try:
            bCaught = False
            self.m_oSpherical.Declination = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Declination out of bounds")

        try:
            bCaught = False
            self.m_oSpherical.Radius = 123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Radius out of bounds")

        try:
            bCaught = False
            self.m_oSpherical.Azimuth = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Azimuth out of bounds")

        try:
            bCaught = False
            self.m_oSpherical.Velocity = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Velocity out of bounds")

        # FPA (Horizontal) test
        self.m_logger.WriteLine6("\t\tCurrent FPA type is: {0}", self.m_oSpherical.FPAType)
        self.m_oSpherical.FPAType = AgESphericalFPA.eSphericalFPAHorizontal
        self.m_logger.WriteLine6("\t\tNew FPA type is: {0}", self.m_oSpherical.FPAType)
        Assert.assertEqual(AgESphericalFPA.eSphericalFPAHorizontal, self.m_oSpherical.FPAType)
        oHorizontal: "ISphericalFPAHorizontal" = clr.Convert(self.m_oSpherical.FPA, ISphericalFPAHorizontal)
        Assert.assertIsNotNone(oHorizontal)
        self.m_logger.WriteLine6("\t\t\tCurrent FPA is: {0}", oHorizontal.FPA)
        oHorizontal.FPA = 1.2345
        self.m_logger.WriteLine6("\t\t\tNew FPA is: {0}", oHorizontal.FPA)
        Assert.assertEqual(1.2345, oHorizontal.FPA)
        try:
            bCaught = False
            oHorizontal.FPA = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FPA out of bounds")

        # FPA (Vertical) test
        self.m_oSpherical.FPAType = AgESphericalFPA.eSphericalFPAVertical
        self.m_logger.WriteLine6("\t\tNew FPA type is: {0}", self.m_oSpherical.FPAType)
        Assert.assertEqual(AgESphericalFPA.eSphericalFPAVertical, self.m_oSpherical.FPAType)
        oVertical: "ISphericalFPAVertical" = clr.Convert(self.m_oSpherical.FPA, ISphericalFPAVertical)
        Assert.assertIsNotNone(oVertical)
        self.m_logger.WriteLine6("\t\t\tCurrent FPA is: {0}", oVertical.FPA)
        oVertical.FPA = -1.2345
        self.m_logger.WriteLine6("\t\t\tNew FPA is: {0}", oVertical.FPA)
        Assert.assertAlmostEqual(-1.2345, oVertical.FPA, delta=1e-05)
        try:
            bCaught = False
            oVertical.FPA = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FPA out of bounds")

        # FPA (Vertical) test
        try:
            self.m_oSpherical.FPAType = AgESphericalFPA.eSphericalFPAUnknown
            Assert.fail("Cannot set AgESphericalFPA.eSphericalFPAUnknown.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

    # endregion
