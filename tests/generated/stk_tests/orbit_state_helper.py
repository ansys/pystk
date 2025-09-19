# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from test_util import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class OrbitStateHelper(object):
    def __init__(self, oApplication: "STKObjectRoot"):
        self.m_oCartesian: "OrbitStateCartesian" = None
        self.m_oClassical: "OrbitStateClassical" = None
        self.m_oGeodetic: "OrbitStateDetic" = None
        self.m_oDelaunay: "OrbitStateDelaunay" = None
        self.m_oEquinoctial: "OrbitStateEquinoctial" = None
        self.m_oMixed: "OrbitStateMixedSpherical" = None
        self.m_oSpherical: "OrbitStateSpherical" = None
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "STKObjectRoot" = oApplication
        self.m_oUnits: "UnitPreferencesDimensionCollection" = self.m_oApplication.units_preferences

    # region CoordinateSystemTest
    def CoordinateSystemTest(self, eOrbitStateType: "OrbitStateType", eSystemType: "CoordinateSystem"):
        oSystem: "OrbitStateCoordinateSystem" = None
        if eOrbitStateType == OrbitStateType.CARTESIAN:
            Assert.assertIsNotNone(self.m_oCartesian)
            self.m_oCartesian.coordinate_system_type = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oCartesian.coordinate_system_type)
            Assert.assertEqual(eSystemType, self.m_oCartesian.coordinate_system_type)
            oSystem = self.m_oCartesian.coordinate_system
        elif eOrbitStateType == OrbitStateType.CLASSICAL:
            Assert.assertIsNotNone(self.m_oClassical)
            self.m_oClassical.coordinate_system_type = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oClassical.coordinate_system_type)
            Assert.assertEqual(eSystemType, self.m_oClassical.coordinate_system_type)
            oSystem = self.m_oClassical.coordinate_system
        elif eOrbitStateType == OrbitStateType.GEODETIC:
            Assert.assertIsNotNone(self.m_oGeodetic)
            self.m_oGeodetic.coordinate_system_type = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oGeodetic.coordinate_system_type)
            Assert.assertEqual(eSystemType, self.m_oGeodetic.coordinate_system_type)
            oSystem = self.m_oGeodetic.coordinate_system
        elif eOrbitStateType == OrbitStateType.DELAUNAY:
            Assert.assertIsNotNone(self.m_oDelaunay)
            self.m_oDelaunay.coordinate_system_type = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oDelaunay.coordinate_system_type)
            Assert.assertEqual(eSystemType, self.m_oDelaunay.coordinate_system_type)
            oSystem = self.m_oDelaunay.coordinate_system
        elif eOrbitStateType == OrbitStateType.EQUINOCTIAL:
            Assert.assertIsNotNone(self.m_oEquinoctial)
            self.m_oEquinoctial.coordinate_system_type = eSystemType
            self.m_logger.WriteLine6(
                "\t\tNew CoordinateSystem type is: {0}", self.m_oEquinoctial.coordinate_system_type
            )
            Assert.assertEqual(eSystemType, self.m_oEquinoctial.coordinate_system_type)
            oSystem = self.m_oEquinoctial.coordinate_system
        elif eOrbitStateType == OrbitStateType.MIXED_SPHERICAL:
            Assert.assertIsNotNone(self.m_oMixed)
            self.m_oMixed.coordinate_system_type = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oMixed.coordinate_system_type)
            Assert.assertEqual(eSystemType, self.m_oMixed.coordinate_system_type)
            oSystem = self.m_oMixed.coordinate_system
        elif eOrbitStateType == OrbitStateType.SPHERICAL:
            Assert.assertIsNotNone(self.m_oSpherical)
            self.m_oSpherical.coordinate_system_type = eSystemType
            self.m_logger.WriteLine6("\t\tNew CoordinateSystem type is: {0}", self.m_oSpherical.coordinate_system_type)
            Assert.assertEqual(eSystemType, self.m_oSpherical.coordinate_system_type)
            oSystem = self.m_oSpherical.coordinate_system
        else:
            oSystem = None

        Assert.assertIsNotNone(oSystem)
        self.m_logger.WriteLine6("\t\t\tType is: {0}", oSystem.type)
        self.m_logger.WriteLine6("\t\t\tCurrent Epoch is: {0}", oSystem.coordinate_system_epoch.time_instant)
        if (
            (
                ((oSystem.type == CoordinateSystem.ALIGNMENT_AT_EPOCH))
                or ((oSystem.type == CoordinateSystem.MEAN_OF_EPOCH))
            )
            or ((oSystem.type == CoordinateSystem.TEME_OF_EPOCH))
        ) or ((oSystem.type == CoordinateSystem.TRUE_OF_EPOCH)):
            oSystem.coordinate_system_epoch.set_explicit_time("13 Aug 2005 02:00:00.000")
            self.m_logger.WriteLine6("\t\t\tNew Epoch is: {0}", oSystem.coordinate_system_epoch.time_instant)
            Assert.assertEqual("13 Aug 2005 02:00:00.000", oSystem.coordinate_system_epoch.time_instant)
        elif (
            (
                (
                    (
                        (
                            (((oSystem.type == CoordinateSystem.B1950)) or ((oSystem.type == CoordinateSystem.FIXED)))
                            or ((oSystem.type == CoordinateSystem.J2000))
                        )
                        or ((oSystem.type == CoordinateSystem.MEAN_OF_DATE))
                    )
                    or ((oSystem.type == CoordinateSystem.TEME_OF_DATE))
                )
                or ((oSystem.type == CoordinateSystem.TRUE_OF_DATE))
            )
            or ((oSystem.type == CoordinateSystem.TRUE_OF_REFERENCE_DATE))
        ) or ((oSystem.type == CoordinateSystem.ICRF)):
            bCaught: bool = False
            try:
                bCaught = False
                oSystem.coordinate_system_epoch.set_explicit_time("13 Aug 2005 02:00:00.000")

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
        self.m_logger.WriteLine6("\tCurrent OrbitState type is: {0}", oOrbitState.orbit_state_type)

        # Cartesian OrbitState test
        self.m_oCartesian = OrbitStateCartesian(oOrbitState.convert_to(OrbitStateType.CARTESIAN))
        Assert.assertIsNotNone(self.m_oCartesian)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oCartesian.orbit_state_type)
        self.m_oCartesian.assign(oOrbitState)
        self.m_oCartesian.convert_to(OrbitStateType.CARTESIAN)
        self.m_oCartesian.convert_to(OrbitStateType.CLASSICAL)
        self.m_oCartesian.convert_to(OrbitStateType.DELAUNAY)
        self.m_oCartesian.convert_to(OrbitStateType.EQUINOCTIAL)
        self.m_oCartesian.convert_to(OrbitStateType.GEODETIC)
        self.m_oCartesian.convert_to(OrbitStateType.MIXED_SPHERICAL)
        self.m_oCartesian.convert_to(OrbitStateType.SPHERICAL)

        # See 25151: try to convert an orbit state that's describes open orbits
        # to Delaunay representation; expecting an exception with a user-friendly explanation
        # why conversion cannot be finished.

        tempCart: "OrbitStateCartesian" = clr.CastAs(
            self.m_oCartesian.convert_to(OrbitStateType.CARTESIAN), OrbitStateCartesian
        )

        self.m_oUnits.set_current_unit("DistanceUnit", "km")
        self.m_oUnits.set_current_unit("TimeUnit", "sec")
        # position is in 'km' and velocity is in 'km/sec'.
        tempCart.x_position = 5691.457559
        tempCart.y_position = 9857.898
        tempCart.z_position = 0
        tempCart.x_velocity = 0
        tempCart.y_velocity = 5.917552767
        tempCart.z_velocity = 5.917552767
        try:
            delaunay: "OrbitStateDelaunay" = clr.CastAs(
                tempCart.convert_to(OrbitStateType.DELAUNAY), OrbitStateDelaunay
            )
            Assert.fail()

        except AssertionError as e:
            raise e

        except Exception as ex:
            sExpectedMsg: str = "Invalid orbit has been specified!"
            Assert.assertEqual(sExpectedMsg, str(ex)[0 : (0 + len(sExpectedMsg))])
            self.m_logger.WriteLine5("\t\tExpected exception: {0}", str(ex))

        del tempCart
        # End of 25151

        self.CartesianTest()

        # Classical OrbitState test
        self.m_oClassical = OrbitStateClassical(oOrbitState.convert_to(OrbitStateType.CLASSICAL))
        Assert.assertIsNotNone(self.m_oClassical)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oClassical.orbit_state_type)
        self.m_oClassical.assign(oOrbitState)
        self.m_oClassical.convert_to(OrbitStateType.CARTESIAN)
        self.m_oClassical.convert_to(OrbitStateType.CLASSICAL)
        self.m_oClassical.convert_to(OrbitStateType.DELAUNAY)
        self.m_oClassical.convert_to(OrbitStateType.EQUINOCTIAL)
        self.m_oClassical.convert_to(OrbitStateType.GEODETIC)
        self.m_oClassical.convert_to(OrbitStateType.MIXED_SPHERICAL)
        self.m_oClassical.convert_to(OrbitStateType.SPHERICAL)
        self.ClassicalTest()

        # Geodetic OrbitState test
        self.m_oGeodetic = OrbitStateDetic(oOrbitState.convert_to(OrbitStateType.GEODETIC))
        Assert.assertIsNotNone(self.m_oGeodetic)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oGeodetic.orbit_state_type)
        self.m_oGeodetic.assign(oOrbitState)
        self.m_oGeodetic.convert_to(OrbitStateType.CARTESIAN)
        self.m_oGeodetic.convert_to(OrbitStateType.CLASSICAL)
        self.m_oGeodetic.convert_to(OrbitStateType.DELAUNAY)
        self.m_oGeodetic.convert_to(OrbitStateType.EQUINOCTIAL)
        self.m_oGeodetic.convert_to(OrbitStateType.GEODETIC)
        self.m_oGeodetic.convert_to(OrbitStateType.MIXED_SPHERICAL)
        self.m_oGeodetic.convert_to(OrbitStateType.SPHERICAL)
        self.GeodeticTest()

        # Delaunay OrbitState test
        self.m_oDelaunay = OrbitStateDelaunay(oOrbitState.convert_to(OrbitStateType.DELAUNAY))
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oDelaunay.orbit_state_type)
        self.m_oDelaunay.assign(oOrbitState)
        self.m_oDelaunay.convert_to(OrbitStateType.CARTESIAN)
        self.m_oDelaunay.convert_to(OrbitStateType.CLASSICAL)
        self.m_oDelaunay.convert_to(OrbitStateType.DELAUNAY)
        self.m_oDelaunay.convert_to(OrbitStateType.EQUINOCTIAL)
        self.m_oDelaunay.convert_to(OrbitStateType.GEODETIC)
        self.m_oDelaunay.convert_to(OrbitStateType.MIXED_SPHERICAL)
        self.m_oDelaunay.convert_to(OrbitStateType.SPHERICAL)
        self.DelaunayTest()

        # Equinoctical OrbitState test
        self.m_oEquinoctial = OrbitStateEquinoctial(oOrbitState.convert_to(OrbitStateType.EQUINOCTIAL))
        Assert.assertIsNotNone(self.m_oEquinoctial)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oEquinoctial.orbit_state_type)
        self.m_oEquinoctial.assign(oOrbitState)
        self.m_oEquinoctial.convert_to(OrbitStateType.CARTESIAN)
        self.m_oEquinoctial.convert_to(OrbitStateType.CLASSICAL)
        self.m_oEquinoctial.convert_to(OrbitStateType.DELAUNAY)
        self.m_oEquinoctial.convert_to(OrbitStateType.EQUINOCTIAL)
        self.m_oEquinoctial.convert_to(OrbitStateType.GEODETIC)
        self.m_oEquinoctial.convert_to(OrbitStateType.MIXED_SPHERICAL)
        self.m_oEquinoctial.convert_to(OrbitStateType.SPHERICAL)
        self.EquinoctialTest()

        # MixedSpherical OrbitState test
        self.m_oMixed = OrbitStateMixedSpherical(oOrbitState.convert_to(OrbitStateType.MIXED_SPHERICAL))
        Assert.assertIsNotNone(self.m_oMixed)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oMixed.orbit_state_type)
        self.m_oMixed.assign(oOrbitState)
        self.m_oMixed.convert_to(OrbitStateType.CARTESIAN)
        self.m_oMixed.convert_to(OrbitStateType.CLASSICAL)
        self.m_oMixed.convert_to(OrbitStateType.DELAUNAY)
        self.m_oMixed.convert_to(OrbitStateType.EQUINOCTIAL)
        self.m_oMixed.convert_to(OrbitStateType.GEODETIC)
        self.m_oMixed.convert_to(OrbitStateType.MIXED_SPHERICAL)
        self.m_oMixed.convert_to(OrbitStateType.SPHERICAL)
        self.MixedSphericalTest()

        # Spherical OrbitState test
        self.m_oSpherical = OrbitStateSpherical(oOrbitState.convert_to(OrbitStateType.SPHERICAL))
        Assert.assertIsNotNone(self.m_oSpherical)
        self.m_logger.WriteLine6("\tNew OrbitState type is: {0}", self.m_oSpherical.orbit_state_type)
        self.m_oSpherical.assign(oOrbitState)
        self.m_oSpherical.convert_to(OrbitStateType.CARTESIAN)
        self.m_oSpherical.convert_to(OrbitStateType.CLASSICAL)
        self.m_oSpherical.convert_to(OrbitStateType.DELAUNAY)
        self.m_oSpherical.convert_to(OrbitStateType.EQUINOCTIAL)
        self.m_oSpherical.convert_to(OrbitStateType.GEODETIC)
        self.m_oSpherical.convert_to(OrbitStateType.MIXED_SPHERICAL)
        self.m_oSpherical.convert_to(OrbitStateType.SPHERICAL)
        self.SphericalTest()

        # Testing the helper methods to convert to desired orbit state type and set its values in one call
        self.m_oUnits.set_current_unit("DistanceUnit", "km")
        self.m_oUnits.set_current_unit("TimeUnit", "sec")
        self.m_oUnits.set_current_unit("AngleUnit", "deg")

        # SetOrbitStateAsCartesian
        oOrbitState.assign_cartesian(CoordinateSystem.FIXED, -22760.2, 549.443, 0.0, -0.0742022, -3.07376, 0.0)
        oOrbitState.assign_classical(CoordinateSystem.J2000, 22000.1, 0.1, 12.3, 0.2, 358.0, 45.4)
        oOrbitState.assign_equinoctial_posigrade(CoordinateSystem.J2000, 22000.1, 0.1, 0.4, 0.2, 58.0, 45.4)
        oOrbitState.assign_geodetic(CoordinateSystem.FIXED, 0.004011, -99.998868, 35786.032637, 1.51e-07, 0.0, 0.0)
        oOrbitState.assign_mixed_spherical(
            CoordinateSystem.J2000, 0.004011, -99.998868, 35786.032637, -0.0, 90.0, 3.074660099
        )
        oOrbitState.assign_spherical(CoordinateSystem.J2000, 178.617119, 0.0, 42164.169637, -0.0, 90.0, 3.074660099)

        self.m_oUnits.reset_units()

    # endregion

    def Test_IAgOrbitState(self, orbitState: "IOrbitState"):
        centralBodyName: str = orbitState.central_body_name
        ost: "OrbitStateType" = orbitState.orbit_state_type

        epochHold: typing.Any = orbitState.epoch
        orbitState.epoch = "18 Jan 2003 02:40:24.680"
        Assert.assertEqual("18 Jan 2003 02:40:24.680", orbitState.epoch)
        orbitState.epoch = epochHold

        orbitState.assign_cartesian(CoordinateSystem.FIXED, -22760.2, 549.443, 0.0, -0.0742022, -3.07376, 0.0)
        orbitState.assign_classical(CoordinateSystem.J2000, 22000.1, 0.1, 12.3, 0.2, 358.0, 45.4)
        orbitState.assign_equinoctial_posigrade(CoordinateSystem.J2000, 22000.1, 0.1, 0.4, 0.2, 58.0, 45.4)
        orbitState.assign_geodetic(CoordinateSystem.FIXED, 0.004011, -99.998868, 35786.032637, 1.51e-07, 0.0, 0.0)
        orbitState.assign_mixed_spherical(
            CoordinateSystem.J2000, 0.004011, -99.998868, 35786.032637, -0.0, 90.0, 3.074660099
        )
        orbitState.assign_spherical(CoordinateSystem.J2000, 178.617119, 0.0, 42164.169637, -0.0, 90.0, 3.074660099)

    # region CartesianTest
    def CartesianTest(self):
        Assert.assertIsNotNone(self.m_oCartesian)
        self.Test_IAgOrbitState(self.m_oCartesian)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        # basic properties test
        # m_logger.WriteLine("\t\tCurrent values:");
        # m_logger.WriteLine("\t\t\t XPosition is: {0}", m_oCartesian.XPosition);
        # m_logger.WriteLine("\t\t\t YPosition is: {0}", m_oCartesian.YPosition);
        # m_logger.WriteLine("\t\t\t ZPosition is: {0}", m_oCartesian.ZPosition);
        # m_logger.WriteLine("\t\t\t XVelocity is: {0}", m_oCartesian.XVelocity);
        # m_logger.WriteLine("\t\t\t YVelocity is: {0}", m_oCartesian.YVelocity);
        # m_logger.WriteLine("\t\t\t ZVelocity is: {0}", m_oCartesian.ZVelocity);
        self.m_oCartesian.x_position = -22760.2
        self.m_oCartesian.y_position = 549.443
        self.m_oCartesian.z_position = 0.0
        self.m_oCartesian.x_velocity = -0.0742022
        self.m_oCartesian.y_velocity = -3.07376
        self.m_oCartesian.z_velocity = 0.0
        # m_logger.WriteLine("\t\tNew values:");
        # m_logger.WriteLine("\t\t\t XPosition is: {0}", m_oCartesian.XPosition);
        # m_logger.WriteLine("\t\t\t YPosition is: {0}", m_oCartesian.YPosition);
        # m_logger.WriteLine("\t\t\t ZPosition is: {0}", m_oCartesian.ZPosition);
        # m_logger.WriteLine("\t\t\t XVelocity is: {0}", m_oCartesian.XVelocity);
        # m_logger.WriteLine("\t\t\t YVelocity is: {0}", m_oCartesian.YVelocity);
        # m_logger.WriteLine("\t\t\t ZVelocity is: {0}", m_oCartesian.ZVelocity);
        Assert.assertEqual(-22760.2, self.m_oCartesian.x_position)
        Assert.assertEqual(549.443, self.m_oCartesian.y_position)
        Assert.assertEqual(0.0, self.m_oCartesian.z_position)
        Assert.assertEqual(-0.0742022, self.m_oCartesian.x_velocity)
        Assert.assertAlmostEqual(-3.07376, self.m_oCartesian.y_velocity, delta=1e-05)
        Assert.assertEqual(0.0, self.m_oCartesian.z_velocity)
        # out of bounds
        bCaught: bool = False
        try:
            bCaught = False
            self.m_oCartesian.x_position = 1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set XPosition out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.y_position = -1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set YPosition out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.z_position = 1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ZPosition out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.x_velocity = -1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set XVelocity out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.y_velocity = 1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set YVelocity out of bounds")

        try:
            bCaught = False
            self.m_oCartesian.z_velocity = -1234567890123460000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ZVelocity out of bounds")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        # CoordinateSystem test
        arTypes = self.m_oCartesian.supported_coordinate_system_types
        self.m_logger.WriteLine3("\t\tCartesian supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})", iIndex, arTypes[iIndex][1], CoordinateSystem(int(arTypes[iIndex][0]))
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oCartesian.coordinate_system_type)
        # ALIGNMENT_AT_EPOCH
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.ALIGNMENT_AT_EPOCH)
        # B1950
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.B1950)
        # FIXED
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.FIXED)
        # J2000
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.J2000)
        # ICRF;
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.ICRF)
        # MEAN_OF_DATE
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.MEAN_OF_DATE)
        # MEAN_OF_EPOCH
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.MEAN_OF_EPOCH)
        # TEME_OF_DATE
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.TEME_OF_DATE)
        # TEME_OF_EPOCH
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.TEME_OF_EPOCH)
        # TRUE_OF_DATE
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.TRUE_OF_DATE)
        # TRUE_OF_EPOCH
        self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.TRUE_OF_EPOCH)
        try:
            # TRUE_OF_REFERENCE_DATE
            self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE)

        except:
            self.m_logger.WriteLine("\t\tThe TRUE_OF_REFERENCE_DATE does not supported by current licenses.")

        # UNKNOWN
        try:
            self.CoordinateSystemTest(self.m_oCartesian.orbit_state_type, CoordinateSystem.UNKNOWN)
            Assert.fail("Cannot set UNKNOWN coordinate system.")

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
        self.m_logger.WriteLine6("\t\tCurrent SizeShape type is: {0}", self.m_oClassical.size_shape_type)
        self.ClassicalSizeShape(ClassicalSizeShape.ALTITUDE)
        self.ClassicalSizeShape(ClassicalSizeShape.MEAN_MOTION)
        self.ClassicalSizeShape(ClassicalSizeShape.PERIOD)
        self.ClassicalSizeShape(ClassicalSizeShape.RADIUS)
        self.ClassicalSizeShape(ClassicalSizeShape.SEMIMAJOR_AXIS)
        try:
            self.ClassicalSizeShape(ClassicalSizeShape.UNKNOWN)
            Assert.fail("Cannot set ClassicalSizeShape.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # Orientation test
        self.ClassicalOrientation(self.m_oClassical.orientation)

        # Location test
        self.m_logger.WriteLine6("\t\tCurrent Location type is: {0}", self.m_oClassical.location_type)
        self.ClassicalLocation(ClassicalLocation.ARGUMENT_OF_LATITUDE)
        self.ClassicalLocation(ClassicalLocation.ECCENTRIC_ANOMALY)
        self.ClassicalLocation(ClassicalLocation.MEAN_ANOMALY)
        self.ClassicalLocation(ClassicalLocation.TIME_PAST_ASCENDING_NODE)
        self.ClassicalLocation(ClassicalLocation.TIME_PAST_PERIGEE)
        self.ClassicalLocation(ClassicalLocation.TRUE_ANOMALY)
        try:
            self.ClassicalLocation(ClassicalLocation.UNKNOWN)
            Assert.fail("Cannot set ClassicalLocation.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # CoordinateSystem test
        arTypes = self.m_oClassical.supported_coordinate_system_types
        self.m_logger.WriteLine3("\t\tClassical supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})", iIndex, arTypes[iIndex][1], CoordinateSystem(int(arTypes[iIndex][0]))
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oClassical.coordinate_system_type)
        # ALIGNMENT_AT_EPOCH
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.ALIGNMENT_AT_EPOCH)
        # B1950
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.B1950)
        # FIXED
        bCaught: bool = False
        try:
            bCaught = False
            self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.FIXED)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FIXED")

        # J2000
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.J2000)
        # ICRF
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.ICRF)
        # MEAN_OF_DATE
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.MEAN_OF_DATE)
        # MEAN_OF_EPOCH
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.MEAN_OF_EPOCH)
        # TEME_OF_DATE
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.TEME_OF_DATE)
        # TEME_OF_EPOCH
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.TEME_OF_EPOCH)
        # TRUE_OF_DATE
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.TRUE_OF_DATE)
        # TRUE_OF_EPOCH
        self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.TRUE_OF_EPOCH)
        # TRUE_OF_REFERENCE_DATE
        # GetLicenses
        oLicenses: "ExecuteCommandResult" = None
        oLicenses = self.m_oApplication.execute_command("GetLicenses /")
        Assert.assertIsNotNone(oLicenses)

        iI: int = 0
        while iI < oLicenses.count:
            strLicense: str = oLicenses[iI]
            if strLicense.find("PODS") >= 0:
                if strLicense.find("No License") >= 0:
                    # No License
                    try:
                        bCaught = False
                        self.CoordinateSystemTest(
                            self.m_oClassical.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE
                        )

                    except Exception as e:
                        bCaught = True
                        self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set TRUE_OF_REFERENCE_DATE")

                else:
                    # License available
                    self.CoordinateSystemTest(
                        self.m_oClassical.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE
                    )

                break

            iI += 1

        # UNKNOWN
        try:
            self.CoordinateSystemTest(self.m_oClassical.orbit_state_type, CoordinateSystem.UNKNOWN)
            Assert.fail("Cannot set CoordinateSystem.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

    # endregion

    # region ClassicalSizeShape
    def ClassicalSizeShape(self, eShapeType: "ClassicalSizeShape"):
        Assert.assertIsNotNone(self.m_oClassical)
        # set shape type
        self.m_oClassical.size_shape_type = eShapeType
        self.m_logger.WriteLine6("\t\tNew SizeShape type is: {0}", self.m_oClassical.size_shape_type)
        Assert.assertEqual(eShapeType, self.m_oClassical.size_shape_type)
        if eShapeType == ClassicalSizeShape.ALTITUDE:
            self.ClassicalSizeShapeAltitude(ClassicalSizeShapeAltitude(self.m_oClassical.size_shape))
        elif eShapeType == ClassicalSizeShape.MEAN_MOTION:
            self.ClassicalSizeShapeMeanMotion(ClassicalSizeShapeMeanMotion(self.m_oClassical.size_shape))
        elif eShapeType == ClassicalSizeShape.PERIOD:
            self.ClassicalSizeShapePeriod(ClassicalSizeShapePeriod(self.m_oClassical.size_shape))
        elif eShapeType == ClassicalSizeShape.RADIUS:
            self.ClassicalSizeShapeRadius(ClassicalSizeShapeRadius(self.m_oClassical.size_shape))
        elif eShapeType == ClassicalSizeShape.SEMIMAJOR_AXIS:
            self.ClassicalSizeShapeSemimajorAxis(ClassicalSizeShapeSemimajorAxis(self.m_oClassical.size_shape))
        else:
            Assert.fail("Invalid SizeShape type!")

    # endregion

    # region ClassicalSizeShapeAltitude
    def ClassicalSizeShapeAltitude(self, oAltitude: "ClassicalSizeShapeAltitude"):
        Assert.assertIsNotNone(oAltitude)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeAltitude is: {0}", oAltitude.apogee_altitude)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeAltitude is: {0}", oAltitude.perigee_altitude)
        oAltitude.apogee_altitude = 123456.789
        oAltitude.perigee_altitude = 987654.321
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeAltitude is: {0}", oAltitude.apogee_altitude)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeAltitude is: {0}", oAltitude.perigee_altitude)
        Assert.assertEqual(123456.789, oAltitude.apogee_altitude)
        Assert.assertAlmostEqual(987654.321, oAltitude.perigee_altitude, delta=0.0001)
        bCaught: bool = False
        try:
            bCaught = False
            oAltitude.apogee_altitude = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ApogeeAltitude out of bounds")

        try:
            bCaught = False
            oAltitude.perigee_altitude = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set PerigeeAltitude out of bounds")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region ClassicalSizeShapeMeanMotion
    def ClassicalSizeShapeMeanMotion(self, oMeanMotion: "ClassicalSizeShapeMeanMotion"):
        Assert.assertIsNotNone(oMeanMotion)
        # set AngleUnit
        strAngleUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strAngleUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        # set TimeUnit
        strTimeUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\t\tThe current TimeUnit is: {0}", strTimeUnit)
        self.m_oUnits.set_current_unit("TimeUnit", "hr")
        self.m_logger.WriteLine5("\t\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t MeanMotion is: {0}", oMeanMotion.mean_motion)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oMeanMotion.eccentricity)
        # Changed meanmotion to a smaller number to prevent the iterative
        # solution in astro code from going into infinite loop trying to
        # figure out a semimajor axis length (see 25146)
        oMeanMotion.mean_motion = 1.23456789  # mean motion is in rad/hr
        oMeanMotion.eccentricity = 0.987654321
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t MeanMotion is: {0}", oMeanMotion.mean_motion)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oMeanMotion.eccentricity)
        Assert.assertEqual(1.23456789, oMeanMotion.mean_motion)
        Assert.assertEqual(0.987654321, oMeanMotion.eccentricity)

        bCaught: bool = False
        try:
            bCaught = False
            oMeanMotion.mean_motion = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MeanMotion out of bounds")

        try:
            bCaught = False
            oMeanMotion.eccentricity = 1.2

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Eccentricity out of bounds")

        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strTimeUnit)
        self.m_logger.WriteLine5("\t\t\tThe new TimeUnit (restored) is: {0}", strTimeUnit)
        Assert.assertEqual(strTimeUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strAngleUnit)
        self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strAngleUnit)
        Assert.assertEqual(strAngleUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

    # endregion

    # region ClassicalSizeShapePeriod
    def ClassicalSizeShapePeriod(self, oPeriod: "ClassicalSizeShapePeriod"):
        Assert.assertIsNotNone(oPeriod)

        # set TimeUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\t\t\tThe current TimeUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("TimeUnit", "yr")
        self.m_logger.WriteLine5("\t\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("yr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t Period is: {0}", oPeriod.period)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oPeriod.eccentricity)
        oPeriod.period = 123456.789
        oPeriod.eccentricity = 0.987654321
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t Period is: {0}", oPeriod.period)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oPeriod.eccentricity)
        Assert.assertAlmostEqual(123456.789, oPeriod.period, delta=0.0001)
        Assert.assertEqual(0.987654321, oPeriod.eccentricity)
        bCaught: bool = False
        try:
            bCaught = False
            oPeriod.period = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Period out of bounds")

        try:
            bCaught = False
            oPeriod.eccentricity = 1.2

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Eccentricity out of bounds")

        # restore TimeUnit
        self.m_oUnits.set_current_unit("TimeUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new TimeUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

    # endregion

    # region ClassicalSizeShapeRadius
    def ClassicalSizeShapeRadius(self, oRadius: "ClassicalSizeShapeRadius"):
        Assert.assertIsNotNone(oRadius)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.apogee_radius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.perigee_radius)
        oRadius.apogee_radius = 987654.321
        oRadius.perigee_radius = 123456.789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.apogee_radius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.perigee_radius)
        Assert.assertAlmostEqual(987654.321, oRadius.apogee_radius, delta=0.0001)
        Assert.assertAlmostEqual(123456.789, oRadius.perigee_radius, delta=0.0001)
        bCaught: bool = False
        try:
            bCaught = False
            oRadius.set_size_shape_radius(123456.789, 987654.321)

        except Exception as e:
            bCaught = True
            self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Expected exception did not occur.")

        # ApogeeRadius < PerigeeRadius
        oRadius.apogee_radius = 98765.4
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.apogee_radius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.perigee_radius)
        Assert.assertAlmostEqual(oRadius.apogee_radius, oRadius.perigee_radius, delta=0.01)
        # PerigeeRadius > ApogeeRadius
        oRadius.perigee_radius = 123456789.0
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.apogee_radius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.perigee_radius)
        Assert.assertAlmostEqual(oRadius.apogee_radius, oRadius.perigee_radius, delta=0.01)
        # SetSizeShapeRadius
        oRadius.set_size_shape_radius(987654.321, 123456.789)
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.apogee_radius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.perigee_radius)
        Assert.assertAlmostEqual(123456.789, oRadius.perigee_radius, delta=0.0001)
        Assert.assertAlmostEqual(987654.321, oRadius.apogee_radius, delta=0.0001)
        oRadius.set_size_shape_radius(98765.4321, 12345.6789)
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t ApogeeRadius is: {0}", oRadius.apogee_radius)
        self.m_logger.WriteLine6("\t\t\t\t PerigeeRadius is: {0}", oRadius.perigee_radius)
        Assert.assertAlmostEqual(12345.6789, oRadius.perigee_radius, delta=1e-05)
        Assert.assertAlmostEqual(98765.4321, oRadius.apogee_radius, delta=1e-05)
        try:
            bCaught = False
            oRadius.apogee_radius = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ApogeeRadius out of bounds")

        try:
            bCaught = False
            oRadius.perigee_radius = -1.2

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set PerigeeRadius out of bounds")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region ClassicalSizeShapeSemimajorAxis
    def ClassicalSizeShapeSemimajorAxis(self, oAxis: "ClassicalSizeShapeSemimajorAxis"):
        Assert.assertIsNotNone(oAxis)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t SemiMajorAxis is: {0}", oAxis.semi_major_axis)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oAxis.eccentricity)
        oAxis.semi_major_axis = 123456.789
        oAxis.eccentricity = 0.987654321
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t SemiMajorAxis is: {0}", oAxis.semi_major_axis)
        self.m_logger.WriteLine6("\t\t\t\t Eccentricity is: {0}", oAxis.eccentricity)
        Assert.assertEqual(123456.789, oAxis.semi_major_axis)
        Assert.assertEqual(0.987654321, oAxis.eccentricity)
        bCaught: bool = False
        try:
            bCaught = False
            oAxis.semi_major_axis = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set SemiMajorAxis out of bounds")

        try:
            bCaught = False
            oAxis.eccentricity = -1.2

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Eccentricity out of bounds")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region ClassicalOrientation
    def ClassicalOrientation(self, oOrientation: "ClassicalOrientation"):
        Assert.assertIsNotNone(oOrientation)
        self.m_logger.WriteLine("\t\tOrientation test")

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # base properties test
        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t Inclination is: {0}", oOrientation.inclination)
        self.m_logger.WriteLine6("\t\t\t\t ArgOfPerigee is: {0}", oOrientation.argument_of_periapsis)
        oOrientation.inclination = 1.23456
        oOrientation.argument_of_periapsis = 2.34561
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t Inclination is: {0}", oOrientation.inclination)
        self.m_logger.WriteLine6("\t\t\t\t ArgOfPerigee is: {0}", oOrientation.argument_of_periapsis)
        Assert.assertEqual(1.23456, oOrientation.inclination)
        Assert.assertEqual(2.34561, oOrientation.argument_of_periapsis)
        bCaught: bool = False
        try:
            bCaught = False
            oOrientation.inclination = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Inclination out of bounds")

        try:
            bCaught = False
            oOrientation.argument_of_periapsis = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ArgOfPerigee out of bounds")

        # AscNode test
        self.m_logger.WriteLine6("\t\t\tCurent AscNodeType is: {0}", oOrientation.ascending_node_type)
        # LAN test
        oOrientation.ascending_node_type = OrientationAscNode.LONGITUDE_ASCENDING_NODE
        self.m_logger.WriteLine6("\t\t\tNew AscNodeType is: {0}", oOrientation.ascending_node_type)
        Assert.assertEqual(OrientationAscNode.LONGITUDE_ASCENDING_NODE, oOrientation.ascending_node_type)
        oLAN: "OrientationLongitudeOfAscending" = OrientationLongitudeOfAscending(oOrientation.ascending_node)
        Assert.assertIsNotNone(oLAN)
        self.m_logger.WriteLine6("\t\t\t\t Current LAN value is: {0}", oLAN.value)
        oLAN.value = 1.23456
        self.m_logger.WriteLine6("\t\t\t\t New LAN value is: {0}", oLAN.value)
        Assert.assertEqual(1.23456, oLAN.value)
        try:
            bCaught = False
            oLAN.value = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LAN.Value out of bounds")

        # RAAN test
        oOrientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        self.m_logger.WriteLine6("\t\t\tNew AscNodeType is: {0}", oOrientation.ascending_node_type)
        Assert.assertEqual(OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE, oOrientation.ascending_node_type)
        oRAAN: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            oOrientation.ascending_node
        )
        Assert.assertIsNotNone(oRAAN)
        self.m_logger.WriteLine6("\t\t\t\t Current RAAN value is: {0}", oRAAN.value)
        oRAAN.value = 1.23456
        self.m_logger.WriteLine6("\t\t\t\t New RAAN value is: {0}", oRAAN.value)
        Assert.assertEqual(1.23456, oRAAN.value)
        try:
            bCaught = False
            oRAAN.value = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set RAAN.Value out of bounds")

        # UNKNOWN test
        try:
            oOrientation.ascending_node_type = OrientationAscNode.UNKNOWN
            Assert.fail("Cannot set OrientationAscNode.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

    # endregion

    # region ClassicalLocation
    def ClassicalLocation(self, eType: "ClassicalLocation"):
        Assert.assertIsNotNone(self.m_oClassical)
        self.m_oClassical.location_type = eType
        self.m_logger.WriteLine6("\t\tNew Location type is: {0}", self.m_oClassical.location_type)
        Assert.assertEqual(eType, self.m_oClassical.location_type)
        bCaught: bool = False
        if eType == ClassicalLocation.ARGUMENT_OF_LATITUDE:
            # set AngleUnit
            strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
            self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
            self.m_oUnits.set_current_unit("AngleUnit", "rad")
            self.m_logger.WriteLine5(
                "\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit")
            )
            Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

            oAOL: "ClassicalLocationArgumentOfLatitude" = ClassicalLocationArgumentOfLatitude(
                self.m_oClassical.location
            )
            Assert.assertIsNotNone(oAOL)
            self.m_logger.WriteLine6("\t\t\t Current ArgumentOfLatitude value is: {0}", oAOL.value)
            oAOL.value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New ArgumentOfLatitude value is: {0}", oAOL.value)
            Assert.assertEqual(1.23456, oAOL.value)
            try:
                bCaught = False
                oAOL.value = -12345.6

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set ArgumentOfLatitude.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.set_current_unit("AngleUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        elif eType == ClassicalLocation.ECCENTRIC_ANOMALY:
            # set AngleUnit
            strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
            self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
            self.m_oUnits.set_current_unit("AngleUnit", "rad")
            self.m_logger.WriteLine5(
                "\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit")
            )
            Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

            oEccentric: "ClassicalLocationEccentricAnomaly" = ClassicalLocationEccentricAnomaly(
                self.m_oClassical.location
            )
            Assert.assertIsNotNone(oEccentric)
            self.m_logger.WriteLine6("\t\t\t Current EccentricAnomaly value is: {0}", oEccentric.value)
            oEccentric.value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New EccentricAnomaly value is: {0}", oEccentric.value)
            Assert.assertEqual(1.23456, oEccentric.value)
            try:
                bCaught = False
                oEccentric.value = -12345.6

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set EccentricAnomaly.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.set_current_unit("AngleUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        elif eType == ClassicalLocation.MEAN_ANOMALY:
            # set AngleUnit
            strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
            self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
            self.m_oUnits.set_current_unit("AngleUnit", "rad")
            self.m_logger.WriteLine5(
                "\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit")
            )
            Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

            oMean: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(self.m_oClassical.location)
            Assert.assertIsNotNone(oMean)
            self.m_logger.WriteLine6("\t\t\t Current MeanAnomaly value is: {0}", oMean.value)
            oMean.value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New MeanAnomaly value is: {0}", oMean.value)
            Assert.assertEqual(1.23456, oMean.value)
            try:
                bCaught = False
                oMean.value = -12345.6

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set MeanAnomaly.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.set_current_unit("AngleUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        elif eType == ClassicalLocation.TIME_PAST_ASCENDING_NODE:
            # set TimeUnit
            strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
            self.m_logger.WriteLine5("\t\t\tThe current TimeUnit is: {0}", strUnit)
            self.m_oUnits.set_current_unit("TimeUnit", "hr")
            self.m_logger.WriteLine5("\t\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
            Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

            oAN: "ClassicalLocationTimePastAscendingNode" = ClassicalLocationTimePastAscendingNode(
                self.m_oClassical.location
            )
            Assert.assertIsNotNone(oAN)
            self.m_logger.WriteLine6("\t\t\t Current TimePastAN value is: {0}", oAN.value)
            oAN.value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New TimePastAN value is: {0}", oAN.value)
            Assert.assertEqual(1.23456, oAN.value)
            try:
                bCaught = False
                oAN.value = -123456000000000000000000000000.0

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set TimePastAN.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.set_current_unit("TimeUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new TimeUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        elif eType == ClassicalLocation.TIME_PAST_PERIGEE:
            # set TimeUnit
            strUnit: str = self.m_oUnits.get_current_unit_abbrv("TimeUnit")
            self.m_logger.WriteLine5("\t\t\tThe current TimeUnit is: {0}", strUnit)
            self.m_oUnits.set_current_unit("TimeUnit", "hr")
            self.m_logger.WriteLine5("\t\t\tThe new TimeUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
            Assert.assertEqual("hr", self.m_oUnits.get_current_unit_abbrv("TimeUnit"))

            oPerigee: "ClassicalLocationTimePastPerigee" = ClassicalLocationTimePastPerigee(self.m_oClassical.location)
            Assert.assertIsNotNone(oPerigee)
            self.m_logger.WriteLine6("\t\t\t Current TimePastPerigee value is: {0}", oPerigee.value)
            oPerigee.value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New TimePastPerigee value is: {0}", oPerigee.value)
            Assert.assertEqual(1.23456, oPerigee.value)
            try:
                bCaught = False
                oPerigee.value = -123456000000000000000000000000.0

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set TimePastPerigee.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.set_current_unit("TimeUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new TimeUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("TimeUnit"))
        elif eType == ClassicalLocation.TRUE_ANOMALY:
            # set AngleUnit
            strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
            self.m_logger.WriteLine5("\t\t\tThe current AngleUnit is: {0}", strUnit)
            self.m_oUnits.set_current_unit("AngleUnit", "rad")
            self.m_logger.WriteLine5(
                "\t\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit")
            )
            Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

            oTrue: "ClassicalLocationTrueAnomaly" = ClassicalLocationTrueAnomaly(self.m_oClassical.location)
            Assert.assertIsNotNone(oTrue)
            self.m_logger.WriteLine6("\t\t\t Current TrueAnomaly value is: {0}", oTrue.value)
            oTrue.value = 1.23456
            self.m_logger.WriteLine6("\t\t\t New TrueAnomaly value is: {0}", oTrue.value)
            Assert.assertEqual(1.23456, oTrue.value)
            try:
                bCaught = False
                oTrue.value = -12345.6

            except Exception as e:
                bCaught = True
                self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("Cannot set TrueAnomaly.Value out of bounds")

            # restore AngleUnit
            self.m_oUnits.set_current_unit("AngleUnit", strUnit)
            self.m_logger.WriteLine5("\t\t\tThe new AngleUnit (restored) is: {0}", strUnit)
            Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        else:
            Assert.fail("Invalid Location type!")

    # endregion

    # region GeodeticTest
    def GeodeticTest(self):
        Assert.assertIsNotNone(self.m_oGeodetic)
        self.Test_IAgOrbitState(self.m_oGeodetic)

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # basic properties test
        # m_logger.WriteLine("\t\tCurrent values:");
        # m_logger.WriteLine("\t\t\t Latitude is: {0}", m_oGeodetic.Latitude);
        # m_logger.WriteLine("\t\t\t LatitudeRate is: {0}", m_oGeodetic.LatitudeRate);
        # m_logger.WriteLine("\t\t\t Longitude is: {0}", m_oGeodetic.Longitude);
        # m_logger.WriteLine("\t\t\t LongitudeRate is: {0}", m_oGeodetic.LongitudeRate);
        self.m_oGeodetic.latitude = 1.23456789
        self.m_oGeodetic.latitude_rate = 2.34567891
        self.m_oGeodetic.longitude = 3.45678912
        self.m_oGeodetic.longitude_rate = 4.56789123
        # m_logger.WriteLine("\t\tNew values:");
        # m_logger.WriteLine("\t\t\t Latitude is: {0}", m_oGeodetic.Latitude);
        # m_logger.WriteLine("\t\t\t LatitudeRate is: {0}", m_oGeodetic.LatitudeRate);
        # m_logger.WriteLine("\t\t\t Longitude is: {0}", m_oGeodetic.Longitude);
        # m_logger.WriteLine("\t\t\t LongitudeRate is: {0}", m_oGeodetic.LongitudeRate);
        Assert.assertEqual(1.23456789, self.m_oGeodetic.latitude)
        Assert.assertEqual(2.34567891, self.m_oGeodetic.latitude_rate)
        Assert.assertEqual(3.45678912, self.m_oGeodetic.longitude)
        Assert.assertEqual(4.56789123, self.m_oGeodetic.longitude_rate)
        # out of bounds
        bCaught: bool = False
        try:
            bCaught = False
            self.m_oGeodetic.latitude = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Latitude out of bounds")

        try:
            bCaught = False
            self.m_oGeodetic.latitude_rate = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LatitudeRate out of bounds")

        try:
            bCaught = False
            self.m_oGeodetic.longitude = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Longitude out of bounds")

        try:
            bCaught = False
            self.m_oGeodetic.longitude_rate = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LongitudeRate out of bounds")

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # CoordinateSystem test
        arTypes = self.m_oGeodetic.supported_coordinate_system_types
        self.m_logger.WriteLine3("\t\tGeodetic supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})", iIndex, arTypes[iIndex][1], CoordinateSystem(int(arTypes[iIndex][0]))
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oGeodetic.coordinate_system_type)
        try:
            bCaught = False
            # ALIGNMENT_AT_EPOCH
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.ALIGNMENT_AT_EPOCH)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ALIGNMENT_AT_EPOCH")

        try:
            bCaught = False
            # B1950
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.B1950)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set B1950")

        # FIXED
        self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.FIXED)
        try:
            bCaught = False
            # J2000
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.J2000)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set J2000")

        try:
            bCaught = False
            # MEAN_OF_DATE
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.MEAN_OF_DATE)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MEAN_OF_DATE")

        try:
            bCaught = False
            # MEAN_OF_EPOCH
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.MEAN_OF_EPOCH)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MEAN_OF_EPOCH")

        try:
            bCaught = False
            # TEME_OF_DATE
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.TEME_OF_DATE)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set TEME_OF_DATE")

        try:
            bCaught = False
            # TEME_OF_EPOCH
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.TEME_OF_EPOCH)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set TEME_OF_EPOCH")

        try:
            bCaught = False
            # TRUE_OF_DATE
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.TRUE_OF_DATE)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set TRUE_OF_DATE")

        try:
            bCaught = False
            # TRUE_OF_EPOCH
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.TRUE_OF_EPOCH)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set TRUE_OF_EPOCH")

        try:
            bCaught = False
            # TRUE_OF_REFERENCE_DATE
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set TRUE_OF_REFERENCE_DATE")

        # UNKNOWN
        try:
            self.CoordinateSystemTest(self.m_oGeodetic.orbit_state_type, CoordinateSystem.UNKNOWN)
            Assert.fail("Cannot set CoordinateSystem.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # Geodetic Size (Altitude) test
        self.m_logger.WriteLine6("\t\tCurrent Size type is: {0}", self.m_oGeodetic.size_type)
        self.m_oGeodetic.size_type = GeodeticSize.ALTITUDE
        self.m_logger.WriteLine6("\t\tNew Size type is: {0}", self.m_oGeodetic.size_type)
        Assert.assertEqual(GeodeticSize.ALTITUDE, self.m_oGeodetic.size_type)
        oAltitude: "DeticSizeAltitude" = DeticSizeAltitude(self.m_oGeodetic.size)
        Assert.assertIsNotNone(oAltitude)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t Altitude is: {0}", oAltitude.altitude)
        self.m_logger.WriteLine6("\t\t\t\t Rate is: {0}", oAltitude.rate)
        oAltitude.altitude = 1.23456789
        oAltitude.rate = 2.34567891
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t Altitude is: {0}", oAltitude.altitude)
        self.m_logger.WriteLine6("\t\t\t\t Rate is: {0}", oAltitude.rate)
        Assert.assertEqual(1.23456789, oAltitude.altitude)
        Assert.assertEqual(2.34567891, oAltitude.rate)
        try:
            bCaught = False
            oAltitude.altitude = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Altitude out of bounds")

        try:
            bCaught = False
            oAltitude.rate = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Rate out of bounds")

        # Geodetic Size (Radius) test
        self.m_oGeodetic.size_type = GeodeticSize.RADIUS
        self.m_logger.WriteLine6("\t\tNew Size type is: {0}", self.m_oGeodetic.size_type)
        Assert.assertEqual(GeodeticSize.RADIUS, self.m_oGeodetic.size_type)
        oRadius: "DeticSizeRadius" = DeticSizeRadius(self.m_oGeodetic.size)
        Assert.assertIsNotNone(oRadius)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t Radius is: {0}", oRadius.radius)
        self.m_logger.WriteLine6("\t\t\t\t Rate is: {0}", oRadius.rate)
        oRadius.radius = 1.23456789
        oRadius.rate = 2.34567891
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t Radius is: {0}", oRadius.radius)
        self.m_logger.WriteLine6("\t\t\t\t Rate is: {0}", oRadius.rate)
        Assert.assertEqual(1.23456789, oRadius.radius)
        Assert.assertEqual(2.34567891, oRadius.rate)
        try:
            bCaught = False
            oRadius.radius = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Radius out of bounds")

        try:
            bCaught = False
            oRadius.rate = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Rate out of bounds")

        # Geodetic Size (Unknown) test
        try:
            bCaught = False
            self.m_oGeodetic.size_type = GeodeticSize.UNKNOWN

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set UNKNOWN")

    # endregion

    # region DelaunayTest
    def DelaunayTest(self):
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.Test_IAgOrbitState(self.m_oDelaunay)

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # basic properties test
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t MeanAnomaly is: {0}", self.m_oDelaunay.mean_anomaly)
        self.m_logger.WriteLine6("\t\t\t ArgOfPerigee is: {0}", self.m_oDelaunay.argument_of_periapsis)
        self.m_logger.WriteLine6("\t\t\t RAAN is: {0}", self.m_oDelaunay.right_ascension_ascending_node)
        self.m_oDelaunay.mean_anomaly = 1.23456789
        self.m_oDelaunay.argument_of_periapsis = 2.34567891
        self.m_oDelaunay.right_ascension_ascending_node = 3.45678912
        self.m_logger.WriteLine("\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t MeanAnomaly is: {0}", self.m_oDelaunay.mean_anomaly)
        self.m_logger.WriteLine6("\t\t\t ArgOfPerigee is: {0}", self.m_oDelaunay.argument_of_periapsis)
        self.m_logger.WriteLine6("\t\t\t RAAN is: {0}", self.m_oDelaunay.right_ascension_ascending_node)
        Assert.assertEqual(1.23456789, self.m_oDelaunay.mean_anomaly)
        Assert.assertEqual(2.34567891, self.m_oDelaunay.argument_of_periapsis)
        Assert.assertEqual(3.45678912, self.m_oDelaunay.right_ascension_ascending_node)
        # out of bounds
        bCaught: bool = False
        try:
            bCaught = False
            self.m_oDelaunay.mean_anomaly = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MeanAnomaly out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.argument_of_periapsis = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set ArgOfPeriapsis out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.right_ascension_ascending_node = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set RAAN out of bounds")

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # L test
        self.DelaunayLTest()

        # H test
        self.DelaunayHTest()

        # G test
        self.DelaunayGTest()

        # CoordinateSystem test
        arTypes = self.m_oDelaunay.supported_coordinate_system_types
        self.m_logger.WriteLine3("\t\tDelaunay supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})", iIndex, arTypes[iIndex][1], CoordinateSystem(int(arTypes[iIndex][0]))
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oDelaunay.coordinate_system_type)
        # ALIGNMENT_AT_EPOCH
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.ALIGNMENT_AT_EPOCH)

        # B1950
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.B1950)
        # FIXED
        try:
            self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.FIXED)
            Assert.fail("Cannot set CoordinateSystem.FIXED.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # J2000
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.J2000)
        # ICRF
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.ICRF)
        # MEAN_OF_DATE
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.MEAN_OF_DATE)
        # MEAN_OF_EPOCH
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.MEAN_OF_EPOCH)
        # TEME_OF_DATE
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.TEME_OF_DATE)
        # TEME_OF_EPOCH
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.TEME_OF_EPOCH)
        # TRUE_OF_DATE
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.TRUE_OF_DATE)
        # TRUE_OF_EPOCH
        self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.TRUE_OF_EPOCH)
        # TRUE_OF_REFERENCE_DATE
        # GetLicenses
        oLicenses: "ExecuteCommandResult" = None
        oLicenses = self.m_oApplication.execute_command("GetLicenses /")
        Assert.assertIsNotNone(oLicenses)

        iI: int = 0
        while iI < oLicenses.count:
            strLicense: str = oLicenses[iI]
            if strLicense.find("PODS") >= 0:
                if strLicense.find("No License") >= 0:
                    # No License
                    try:
                        bCaught = False
                        self.CoordinateSystemTest(
                            self.m_oDelaunay.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE
                        )

                    except Exception as e:
                        bCaught = True
                        self.m_logger.Write2("\t\t\tExpected exception: {0}", str(e))

                    if not bCaught:
                        Assert.fail("Cannot set TRUE_OF_REFERENCE_DATE")

                else:
                    # License available
                    self.CoordinateSystemTest(
                        self.m_oDelaunay.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE
                    )

                break

            iI += 1

        # UNKNOWN
        try:
            self.CoordinateSystemTest(self.m_oDelaunay.orbit_state_type, CoordinateSystem.UNKNOWN)
            Assert.fail("Cannot set CoordinateSystem.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

    # endregion

    # region DelaunayLTest
    def DelaunayLTest(self):
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.m_logger.WriteLine6("\t\tCurrent LType is: {0}", self.m_oDelaunay.l_type)
        self.m_oDelaunay.l_type = DelaunayLType.L
        self.m_logger.WriteLine6("\t\tNew LType is: {0}", self.m_oDelaunay.l_type)
        Assert.assertEqual(DelaunayLType.L, self.m_oDelaunay.l_type)
        oL: "DelaunayL" = DelaunayL(self.m_oDelaunay.l)
        Assert.assertIsNotNone(oL)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t L is: {0}", oL.l)
        oL.l = 12345678.9
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t L is: {0}", oL.l)
        Assert.assertEqual(12345678.9, oL.l)
        bCaught: bool = False
        try:
            bCaught = False
            oL.l = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set L out of bounds")

        self.m_oDelaunay.l_type = DelaunayLType.L_OVER_SQRT_MU
        self.m_logger.WriteLine6("\t\tNew LType is: {0}", self.m_oDelaunay.l_type)
        Assert.assertEqual(DelaunayLType.L_OVER_SQRT_MU, self.m_oDelaunay.l_type)
        oLOver: "DelaunayLOverSQRTmu" = DelaunayLOverSQRTmu(self.m_oDelaunay.l)
        Assert.assertIsNotNone(oLOver)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t LOverSQRTmu is: {0}", oLOver.l_over_sqrt_mu)
        oLOver.l_over_sqrt_mu = 12345678.9
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t LOverSQRTmu is: {0}", oLOver.l_over_sqrt_mu)
        Assert.assertAlmostEqual(12345678.9, oLOver.l_over_sqrt_mu, delta=0.01)
        try:
            bCaught = False
            oLOver.l_over_sqrt_mu = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LOverSQRTmu out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.l_type = DelaunayLType.UNKNOWN

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set UNKNOWN")

    # endregion

    # region DelaunayHTest
    def DelaunayHTest(self):
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.m_logger.WriteLine6("\t\tCurrent HType is: {0}", self.m_oDelaunay.h_type)
        self.m_oDelaunay.h_type = DelaunayHType.H
        self.m_logger.WriteLine6("\t\tNew HType is: {0}", self.m_oDelaunay.h_type)
        Assert.assertEqual(DelaunayHType.H, self.m_oDelaunay.h_type)
        oH: "DelaunayH" = DelaunayH(self.m_oDelaunay.h)
        Assert.assertIsNotNone(oH)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t H is: {0}", oH.h)
        oH.h = 12.3456789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t H is: {0}", oH.h)
        Assert.assertEqual(12.3456789, oH.h)
        bCaught: bool = False
        try:
            bCaught = False
            oH.h = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set H out of bounds")

        self.m_oDelaunay.h_type = DelaunayHType.H_OVER_SQRT_MU
        self.m_logger.WriteLine6("\t\tNew HType is: {0}", self.m_oDelaunay.h_type)
        Assert.assertEqual(DelaunayHType.H_OVER_SQRT_MU, self.m_oDelaunay.h_type)
        oHOver: "DelaunayHOverSQRTmu" = DelaunayHOverSQRTmu(self.m_oDelaunay.h)
        Assert.assertIsNotNone(oHOver)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t HOverSQRTmu is: {0}", oHOver.h_over_sqrt_mu)
        oHOver.h_over_sqrt_mu = 12.3456789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t HOverSQRTmu is: {0}", oHOver.h_over_sqrt_mu)
        Assert.assertAlmostEqual(12.3456789, oHOver.h_over_sqrt_mu, delta=1e-08)
        try:
            bCaught = False
            oHOver.h_over_sqrt_mu = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set HOverSQRTmu out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.h_type = DelaunayHType.UNKNOWN

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set UNKNOWN")

    # endregion

    # region DelaunayGTest
    def DelaunayGTest(self):
        Assert.assertIsNotNone(self.m_oDelaunay)
        self.m_logger.WriteLine6("\t\tCurrent GType is: {0}", self.m_oDelaunay.g_type)
        self.m_oDelaunay.g_type = DelaunayGType.G
        self.m_logger.WriteLine6("\t\tNew GType is: {0}", self.m_oDelaunay.g_type)
        Assert.assertEqual(DelaunayGType.G, self.m_oDelaunay.g_type)
        oG: "DelaunayG" = DelaunayG(self.m_oDelaunay.g)
        Assert.assertIsNotNone(oG)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t G is: {0}", oG.g)
        oG.g = 12345.6789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t G is: {0}", oG.g)
        Assert.assertEqual(12345.6789, oG.g)
        bCaught: bool = False
        try:
            bCaught = False
            oG.g = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set G out of bounds")

        self.m_oDelaunay.g_type = DelaunayGType.G_OVER_SQRT_MU
        self.m_logger.WriteLine6("\t\tNew GType is: {0}", self.m_oDelaunay.g_type)
        Assert.assertEqual(DelaunayGType.G_OVER_SQRT_MU, self.m_oDelaunay.g_type)
        oGOver: "DelaunayGOverSQRTmu" = DelaunayGOverSQRTmu(self.m_oDelaunay.g)
        Assert.assertIsNotNone(oGOver)
        self.m_logger.WriteLine("\t\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t\t GOverSQRTmu is: {0}", oGOver.g_over_sqrt_mu)
        oGOver.g_over_sqrt_mu = 12345.6789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t GOverSQRTmu is: {0}", oGOver.g_over_sqrt_mu)
        Assert.assertAlmostEqual(12345.6789, oGOver.g_over_sqrt_mu, delta=0.0001)
        try:
            bCaught = False
            oGOver.g_over_sqrt_mu = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set GOverSQRTmu out of bounds")

        try:
            bCaught = False
            self.m_oDelaunay.g_type = DelaunayGType.UNKNOWN

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set UNKNOWN")

    # endregion

    # region EquinoctialTest
    def EquinoctialTest(self):
        Assert.assertIsNotNone(self.m_oEquinoctial)
        self.Test_IAgOrbitState(self.m_oEquinoctial)

        bCaught: bool = False

        # CoordinateSystem test
        arTypes = self.m_oEquinoctial.supported_coordinate_system_types
        self.m_logger.WriteLine3("\t\tEquinoctial supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})", iIndex, arTypes[iIndex][1], CoordinateSystem(int(arTypes[iIndex][0]))
            )

            iIndex += 1

        self.m_logger.WriteLine6(
            "\t\tCurrent CoordinateSystem type is: {0}", self.m_oEquinoctial.coordinate_system_type
        )
        # ALIGNMENT_AT_EPOCH
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.ALIGNMENT_AT_EPOCH)
        # B1950
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.B1950)
        try:
            bCaught = False
            # FIXED
            self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.FIXED)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FIXED")

        # J2000
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.J2000)
        # ICRF
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.ICRF)
        # MEAN_OF_DATE
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.MEAN_OF_DATE)
        # MEAN_OF_EPOCH
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.MEAN_OF_EPOCH)
        # TEME_OF_DATE
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.TEME_OF_DATE)
        # TEME_OF_EPOCH
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.TEME_OF_EPOCH)
        # TRUE_OF_DATE
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.TRUE_OF_DATE)
        # TRUE_OF_EPOCH
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.TRUE_OF_EPOCH)
        try:
            # TRUE_OF_REFERENCE_DATE
            self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE)

        except:
            self.m_logger.WriteLine("\t\tThe TRUE_OF_REFERENCE_DATE does not supported by current licenses.")

        # UNKNOWN
        try:
            self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.UNKNOWN)
            Assert.fail("Cannot set CoordinateSystem.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # basic properties test
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t H is: {0}", self.m_oEquinoctial.h)
        self.m_logger.WriteLine6("\t\t\t K is: {0}", self.m_oEquinoctial.k)
        self.m_logger.WriteLine6("\t\t\t P is: {0}", self.m_oEquinoctial.p)
        self.m_logger.WriteLine6("\t\t\t Q is: {0}", self.m_oEquinoctial.q)
        self.m_logger.WriteLine6("\t\t\t MeanLongitude is: {0}", self.m_oEquinoctial.mean_longitude)
        self.m_logger.WriteLine6("\t\t\t Formulation is: {0}", self.m_oEquinoctial.formulation)
        self.m_oEquinoctial.h = 0.123456789
        self.m_oEquinoctial.k = -0.234567891
        self.m_oEquinoctial.p = 3.45678912
        self.m_oEquinoctial.q = 4.56789123
        self.m_oEquinoctial.mean_longitude = 5.67891234
        self.m_oEquinoctial.formulation = EquinoctialFormulation.POSIGRADE
        self.m_logger.WriteLine("\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t H is: {0}", self.m_oEquinoctial.h)
        self.m_logger.WriteLine6("\t\t\t K is: {0}", self.m_oEquinoctial.k)
        self.m_logger.WriteLine6("\t\t\t P is: {0}", self.m_oEquinoctial.p)
        self.m_logger.WriteLine6("\t\t\t Q is: {0}", self.m_oEquinoctial.q)
        self.m_logger.WriteLine6("\t\t\t MeanLongitude is: {0}", self.m_oEquinoctial.mean_longitude)
        self.m_logger.WriteLine6("\t\t\t Formulation is: {0}", self.m_oEquinoctial.formulation)
        Assert.assertEqual(0.123456789, self.m_oEquinoctial.h)
        Assert.assertEqual(-0.234567891, self.m_oEquinoctial.k)
        Assert.assertEqual(3.45678912, self.m_oEquinoctial.p)
        Assert.assertEqual(4.56789123, self.m_oEquinoctial.q)
        Assert.assertEqual(5.67891234, self.m_oEquinoctial.mean_longitude)
        Assert.assertEqual(EquinoctialFormulation.POSIGRADE, self.m_oEquinoctial.formulation)
        self.m_oEquinoctial.formulation = EquinoctialFormulation.RETROGRADE
        self.m_logger.WriteLine6("\t\t\t Formulation is: {0}", self.m_oEquinoctial.formulation)
        Assert.assertEqual(EquinoctialFormulation.RETROGRADE, self.m_oEquinoctial.formulation)
        # out of bounds
        try:
            bCaught = False
            self.m_oEquinoctial.h = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set H out of bounds")

        try:
            bCaught = False
            self.m_oEquinoctial.k = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set K out of bounds")

        try:
            bCaught = False
            self.m_oEquinoctial.p = 123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set P out of bounds")

        try:
            bCaught = False
            self.m_oEquinoctial.q = -123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Q out of bounds")

        try:
            bCaught = False
            self.m_oEquinoctial.mean_longitude = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MeanLongitude out of bounds")

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # SizeShape test
        self.m_logger.WriteLine6("\t\tCurrent SizeShape type is: {0}", self.m_oEquinoctial.size_shape_type)
        self.EquinoctialSizeShape(EquinoctialSizeShape.MEAN_MOTION)
        self.EquinoctialSizeShape(EquinoctialSizeShape.SEMIMAJOR_AXIS)
        try:
            self.EquinoctialSizeShape(EquinoctialSizeShape.UNKNOWN)
            Assert.fail("Cannot set EquinoctialSizeShape.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

    # endregion

    # region EquinoctialSizeShape
    def EquinoctialSizeShape(self, eShapeType: "EquinoctialSizeShape"):
        Assert.assertIsNotNone(self.m_oEquinoctial)
        # set shape type
        self.m_oEquinoctial.size_shape_type = eShapeType
        self.m_logger.WriteLine6("\t\tNew SizeShape type is: {0}", self.m_oEquinoctial.size_shape_type)
        Assert.assertEqual(eShapeType, self.m_oEquinoctial.size_shape_type)
        if eShapeType == EquinoctialSizeShape.MEAN_MOTION:
            self.EquinoctialSizeShapeMeanMotion(EquinoctialSizeShapeMeanMotion(self.m_oEquinoctial.size_shape))
        elif eShapeType == EquinoctialSizeShape.SEMIMAJOR_AXIS:
            self.EquinoctialSizeShapeSemimajorAxis(EquinoctialSizeShapeSemimajorAxis(self.m_oEquinoctial.size_shape))
        else:
            Assert.fail("Invalid SizeShape type!")

    # endregion

    # region EquinoctialSizeShapeMeanMotion
    def EquinoctialSizeShapeMeanMotion(self, oMeanMotion: "EquinoctialSizeShapeMeanMotion"):
        Assert.assertIsNotNone(oMeanMotion)
        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t MeanMotion is: {0}", oMeanMotion.mean_motion)
        oMeanMotion.mean_motion = 123456.789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t MeanMotion is: {0}", oMeanMotion.mean_motion)
        Assert.assertAlmostEqual(123456.789, oMeanMotion.mean_motion, delta=0.0001)
        bCaught: bool = False
        try:
            bCaught = False
            oMeanMotion.mean_motion = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set MeanMotion out of bounds")

    # endregion

    # region EquinoctialSizeShapeSemimajorAxis
    def EquinoctialSizeShapeSemimajorAxis(self, oAxis: "EquinoctialSizeShapeSemimajorAxis"):
        Assert.assertIsNotNone(oAxis)

        # set DistanceUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("DistanceUnit", "nm")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("nm", self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

        self.m_logger.WriteLine("\t\t\tCurent values:")
        self.m_logger.WriteLine6("\t\t\t\t SemiMajorAxis is: {0}", oAxis.semi_major_axis)
        oAxis.semi_major_axis = 123456.789
        self.m_logger.WriteLine("\t\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t\t SemiMajorAxis is: {0}", oAxis.semi_major_axis)
        Assert.assertEqual(123456.789, oAxis.semi_major_axis)
        bCaught: bool = False
        try:
            bCaught = False
            oAxis.semi_major_axis = -12345.6

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\t\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set SemiMajorAxis out of bounds")

        # restore DistanceUnit
        self.m_oUnits.set_current_unit("DistanceUnit", strUnit)
        self.m_logger.WriteLine5("\t\t\tThe new DistanceUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region MixedSphericalTest
    def MixedSphericalTest(self):
        Assert.assertIsNotNone(self.m_oMixed)
        self.Test_IAgOrbitState(self.m_oMixed)

        bCaught: bool = False

        # CoordinateSystem test
        arTypes = self.m_oMixed.supported_coordinate_system_types
        self.m_logger.WriteLine3("\t\tMixedSpherical supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})", iIndex, arTypes[iIndex][1], CoordinateSystem(int(arTypes[iIndex][0]))
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oMixed.coordinate_system_type)
        # ALIGNMENT_AT_EPOCH
        self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.ALIGNMENT_AT_EPOCH)
        # B1950
        self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.B1950)
        try:
            bCaught = False
            # FIXED
            self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.FIXED)

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FIXED")

        # J2000
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.J2000)
        # ICRF
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.ICRF)
        # MEAN_OF_DATE
        self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.MEAN_OF_DATE)
        # MEAN_OF_EPOCH
        self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.MEAN_OF_EPOCH)
        # TEME_OF_DATE
        self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.TEME_OF_DATE)
        # TEME_OF_EPOCH
        self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.TEME_OF_EPOCH)
        # TRUE_OF_DATE
        self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.TRUE_OF_DATE)
        # TRUE_OF_EPOCH
        self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.TRUE_OF_EPOCH)
        try:
            # TRUE_OF_REFERENCE_DATE
            self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE)

        except:
            self.m_logger.WriteLine("\t\tThe TRUE_OF_REFERENCE_DATE does not supported by current licenses.")

        # UNKNOWN
        try:
            self.CoordinateSystemTest(self.m_oMixed.orbit_state_type, CoordinateSystem.UNKNOWN)
            Assert.fail("Cannot set CoordinateSystem.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # basic properties test
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t Latitude is: {0}", self.m_oMixed.latitude)
        self.m_logger.WriteLine6("\t\t\t Longitude is: {0}", self.m_oMixed.longitude)
        self.m_logger.WriteLine6("\t\t\t Altitude is: {0}", self.m_oMixed.altitude)
        self.m_logger.WriteLine6("\t\t\t Azimuth is: {0}", self.m_oMixed.azimuth)
        self.m_logger.WriteLine6("\t\t\t Velocity is: {0}", self.m_oMixed.velocity)
        self.m_oMixed.latitude = -1.2345
        self.m_oMixed.longitude = 2.3451
        self.m_oMixed.altitude = 3456789.12
        self.m_oMixed.azimuth = 4.5123
        self.m_oMixed.velocity = 56789.1234
        self.m_logger.WriteLine("\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t Latitude is: {0}", self.m_oMixed.latitude)
        self.m_logger.WriteLine6("\t\t\t Longitude is: {0}", self.m_oMixed.longitude)
        self.m_logger.WriteLine6("\t\t\t Altitude is: {0}", self.m_oMixed.altitude)
        self.m_logger.WriteLine6("\t\t\t Azimuth is: {0}", self.m_oMixed.azimuth)
        self.m_logger.WriteLine6("\t\t\t Velocity is: {0}", self.m_oMixed.velocity)
        Assert.assertEqual(-1.2345, self.m_oMixed.latitude)
        Assert.assertEqual(2.3451, self.m_oMixed.longitude)
        Assert.assertEqual(3456789.12, self.m_oMixed.altitude)
        Assert.assertEqual(4.5123, self.m_oMixed.azimuth)
        Assert.assertEqual(56789.1234, self.m_oMixed.velocity)
        # out of bounds
        try:
            bCaught = False
            self.m_oMixed.latitude = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Latitude out of bounds")

        try:
            bCaught = False
            self.m_oMixed.longitude = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Longitude out of bounds")

        try:
            bCaught = False
            self.m_oMixed.altitude = 123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Altitude out of bounds")

        try:
            bCaught = False
            self.m_oMixed.azimuth = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Azimuth out of bounds")

        try:
            bCaught = False
            self.m_oMixed.velocity = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Velocity out of bounds")

        # FPA (Horizontal) test
        self.m_logger.WriteLine6("\t\tCurrent FPA type is: {0}", self.m_oMixed.flight_path_angle_type)
        self.m_oMixed.flight_path_angle_type = MixedSphericalFlightPathAngleType.HORIZONTAL
        self.m_logger.WriteLine6("\t\tNew FPA type is: {0}", self.m_oMixed.flight_path_angle_type)
        Assert.assertEqual(MixedSphericalFlightPathAngleType.HORIZONTAL, self.m_oMixed.flight_path_angle_type)
        oHorizontal: "MixedSphericalFlightPathAngleHorizontal" = MixedSphericalFlightPathAngleHorizontal(
            self.m_oMixed.flight_path_angle
        )
        Assert.assertIsNotNone(oHorizontal)
        self.m_logger.WriteLine6("\t\t\tCurrent FPA is: {0}", oHorizontal.flight_path_angle)
        oHorizontal.flight_path_angle = 1.2345
        self.m_logger.WriteLine6("\t\t\tNew FPA is: {0}", oHorizontal.flight_path_angle)
        Assert.assertEqual(1.2345, oHorizontal.flight_path_angle)
        try:
            bCaught = False
            oHorizontal.flight_path_angle = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FPA out of bounds")

        # FPA (Vertical) test
        self.m_oMixed.flight_path_angle_type = MixedSphericalFlightPathAngleType.VERTICAL
        self.m_logger.WriteLine6("\t\tNew FPA type is: {0}", self.m_oMixed.flight_path_angle_type)
        Assert.assertEqual(MixedSphericalFlightPathAngleType.VERTICAL, self.m_oMixed.flight_path_angle_type)
        oVertical: "MixedSphericalFlightPathAngleVertical" = MixedSphericalFlightPathAngleVertical(
            self.m_oMixed.flight_path_angle
        )
        Assert.assertIsNotNone(oVertical)
        self.m_logger.WriteLine6("\t\t\tCurrent FPA is: {0}", oVertical.flight_path_angle)
        oVertical.flight_path_angle = -1.2345
        self.m_logger.WriteLine6("\t\t\tNew FPA is: {0}", oVertical.flight_path_angle)
        Assert.assertAlmostEqual(-1.2345, oVertical.flight_path_angle, delta=1e-05)
        try:
            bCaught = False
            oVertical.flight_path_angle = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FPA out of bounds")

        # FPA (Vertical) test
        try:
            self.m_oMixed.flight_path_angle_type = MixedSphericalFlightPathAngleType.UNKNOWN
            Assert.fail("Cannot set MixedSphericalFlightPathAngleType.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

    # endregion

    # region SphericalTest
    def SphericalTest(self):
        Assert.assertIsNotNone(self.m_oSpherical)
        self.Test_IAgOrbitState(self.m_oSpherical)

        bCaught: bool = False

        # CoordinateSystem test
        arTypes = self.m_oSpherical.supported_coordinate_system_types
        self.m_logger.WriteLine3("\t\tSpherical supports: {0} types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            self.m_logger.WriteLine8(
                "\t\t\tType {0}: {1} ({2})", iIndex, arTypes[iIndex][1], CoordinateSystem(int(arTypes[iIndex][0]))
            )

            iIndex += 1

        self.m_logger.WriteLine6("\t\tCurrent CoordinateSystem type is: {0}", self.m_oSpherical.coordinate_system_type)
        # ALIGNMENT_AT_EPOCH
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.ALIGNMENT_AT_EPOCH)
        # B1950
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.B1950)
        # FIXED
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.FIXED)
        # J2000
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.J2000)
        # ICRF
        self.CoordinateSystemTest(self.m_oEquinoctial.orbit_state_type, CoordinateSystem.ICRF)
        # MEAN_OF_DATE
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.MEAN_OF_DATE)
        # MEAN_OF_EPOCH
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.MEAN_OF_EPOCH)
        # TEME_OF_DATE
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.TEME_OF_DATE)
        # TEME_OF_EPOCH
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.TEME_OF_EPOCH)
        # TRUE_OF_DATE
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.TRUE_OF_DATE)
        # TRUE_OF_EPOCH
        self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.TRUE_OF_EPOCH)
        try:
            # TRUE_OF_REFERENCE_DATE
            self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.TRUE_OF_REFERENCE_DATE)

        except:
            self.m_logger.WriteLine("\t\tThe TRUE_OF_REFERENCE_DATE does not supported by current licenses.")

        # UNKNOWN
        try:
            self.CoordinateSystemTest(self.m_oSpherical.orbit_state_type, CoordinateSystem.UNKNOWN)
            Assert.fail("Cannot set CoordinateSystem.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # set AngleUnit
        strUnit: str = self.m_oUnits.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\t\tThe current AngleUnit is: {0}", strUnit)
        self.m_oUnits.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\t\tThe new AngleUnit is: {0}", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

        # basic properties test
        self.m_logger.WriteLine("\t\tCurrent values:")
        self.m_logger.WriteLine6("\t\t\t RightAscension is: {0}", self.m_oSpherical.right_ascension)
        self.m_logger.WriteLine6("\t\t\t Declination is: {0}", self.m_oSpherical.declination)
        self.m_logger.WriteLine6("\t\t\t Radius is: {0}", self.m_oSpherical.radius)
        self.m_logger.WriteLine6("\t\t\t Azimuth is: {0}", self.m_oSpherical.azimuth)
        self.m_logger.WriteLine6("\t\t\t Velocity is: {0}", self.m_oSpherical.velocity)
        self.m_oSpherical.right_ascension = 2.3451
        self.m_oSpherical.declination = -1.2345
        self.m_oSpherical.radius = 3456789.12
        self.m_oSpherical.azimuth = 4.5123
        self.m_oSpherical.velocity = 56789.1234
        self.m_logger.WriteLine("\t\tNew values:")
        self.m_logger.WriteLine6("\t\t\t RightAscension is: {0}", self.m_oSpherical.right_ascension)
        self.m_logger.WriteLine6("\t\t\t Declination is: {0}", self.m_oSpherical.declination)
        self.m_logger.WriteLine6("\t\t\t Radius is: {0}", self.m_oSpherical.radius)
        self.m_logger.WriteLine6("\t\t\t Azimuth is: {0}", self.m_oSpherical.azimuth)
        self.m_logger.WriteLine6("\t\t\t Velocity is: {0}", self.m_oSpherical.velocity)
        Assert.assertEqual(2.3451, self.m_oSpherical.right_ascension)
        Assert.assertEqual(-1.2345, self.m_oSpherical.declination)
        Assert.assertEqual(3456789.12, self.m_oSpherical.radius)
        Assert.assertEqual(4.5123, self.m_oSpherical.azimuth)
        Assert.assertEqual(56789.1234, self.m_oSpherical.velocity)
        # out of bounds
        try:
            bCaught = False
            self.m_oSpherical.right_ascension = 12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set RightAscension out of bounds")

        try:
            bCaught = False
            self.m_oSpherical.declination = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Declination out of bounds")

        try:
            bCaught = False
            self.m_oSpherical.radius = 123400000000000000000000000.0

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Radius out of bounds")

        try:
            bCaught = False
            self.m_oSpherical.azimuth = -12.34

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Azimuth out of bounds")

        try:
            bCaught = False
            self.m_oSpherical.velocity = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set Velocity out of bounds")

        # FPA (Horizontal) test
        self.m_logger.WriteLine6("\t\tCurrent FPA type is: {0}", self.m_oSpherical.flight_path_angle_type)
        self.m_oSpherical.flight_path_angle_type = SphericalFlightPathAzimuthType.HORIZONTAL
        self.m_logger.WriteLine6("\t\tNew FPA type is: {0}", self.m_oSpherical.flight_path_angle_type)
        Assert.assertEqual(SphericalFlightPathAzimuthType.HORIZONTAL, self.m_oSpherical.flight_path_angle_type)
        oHorizontal: "SphericalFlightPathAngleHorizontal" = SphericalFlightPathAngleHorizontal(
            self.m_oSpherical.flight_path_angle
        )
        Assert.assertIsNotNone(oHorizontal)
        self.m_logger.WriteLine6("\t\t\tCurrent FPA is: {0}", oHorizontal.flight_path_angle)
        oHorizontal.flight_path_angle = 1.2345
        self.m_logger.WriteLine6("\t\t\tNew FPA is: {0}", oHorizontal.flight_path_angle)
        Assert.assertEqual(1.2345, oHorizontal.flight_path_angle)
        try:
            bCaught = False
            oHorizontal.flight_path_angle = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FPA out of bounds")

        # FPA (Vertical) test
        self.m_oSpherical.flight_path_angle_type = SphericalFlightPathAzimuthType.VERTICAL
        self.m_logger.WriteLine6("\t\tNew FPA type is: {0}", self.m_oSpherical.flight_path_angle_type)
        Assert.assertEqual(SphericalFlightPathAzimuthType.VERTICAL, self.m_oSpherical.flight_path_angle_type)
        oVertical: "SphericalFlightPathAngleVertical" = SphericalFlightPathAngleVertical(
            self.m_oSpherical.flight_path_angle
        )
        Assert.assertIsNotNone(oVertical)
        self.m_logger.WriteLine6("\t\t\tCurrent FPA is: {0}", oVertical.flight_path_angle)
        oVertical.flight_path_angle = -1.2345
        self.m_logger.WriteLine6("\t\t\tNew FPA is: {0}", oVertical.flight_path_angle)
        Assert.assertAlmostEqual(-1.2345, oVertical.flight_path_angle, delta=1e-05)
        try:
            bCaught = False
            oVertical.flight_path_angle = -1234

        except Exception as e:
            bCaught = True
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FPA out of bounds")

        # FPA (Vertical) test
        try:
            self.m_oSpherical.flight_path_angle_type = SphericalFlightPathAzimuthType.UNKNOWN
            Assert.fail("Cannot set SphericalFlightPathAzimuthType.UNKNOWN.")

        except AssertionError as e:
            Assert.fail(str(e))

        except Exception as e:
            self.m_logger.Write2("\t\tExpected exception: {0}", str(e))

        # restore AngleUnit
        self.m_oUnits.set_current_unit("AngleUnit", strUnit)
        self.m_logger.WriteLine5("\t\tThe new AngleUnit (restored) is: {0}", strUnit)
        Assert.assertEqual(strUnit, self.m_oUnits.get_current_unit_abbrv("AngleUnit"))

    # endregion
