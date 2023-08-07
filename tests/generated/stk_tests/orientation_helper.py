from test_util import *
from assertion_harness import *
from logger import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


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
        if oPosition.pos_type == AgEPositionType.eCartesian:
            oCartesian: "ICartesian" = clr.Convert(oPosition.convert_to(AgEPositionType.eCartesian), ICartesian)
            Assert.assertIsNotNone(oCartesian)
            self.m_logger.WriteLine6("\t\tCartesian X is: {0}", oCartesian.x)
            self.m_logger.WriteLine6("\t\tCartesian Y is: {0}", oCartesian.y)
            self.m_logger.WriteLine6("\t\tCartesian Z is: {0}", oCartesian.z)
        elif oPosition.pos_type == AgEPositionType.eCylindrical:
            oCylindrical: "ICylindrical" = clr.Convert(oPosition.convert_to(AgEPositionType.eCylindrical), ICylindrical)
            Assert.assertIsNotNone(oCylindrical)
            self.m_logger.WriteLine6("\t\tCylindrical Radius is: {0}", oCylindrical.radius)
            self.m_logger.WriteLine6("\t\tCylindrical Z is: {0}", oCylindrical.z)
            self.m_logger.WriteLine6("\t\tCylindrical Lon is: {0}", oCylindrical.lon)
        elif oPosition.pos_type == AgEPositionType.eGeocentric:
            oGeocentric: "IGeocentric" = clr.Convert(oPosition.convert_to(AgEPositionType.eGeocentric), IGeocentric)
            Assert.assertIsNotNone(oGeocentric)
            self.m_logger.WriteLine6("\t\tGeocentric Lat is: {0}", oGeocentric.lat)
            self.m_logger.WriteLine6("\t\tGeocentric Lon is: {0}", oGeocentric.lon)
            self.m_logger.WriteLine6("\t\tGeocentric Alt is: {0}", oGeocentric.alt)
        elif oPosition.pos_type == AgEPositionType.eGeodetic:
            oGeodetic: "IGeodetic" = clr.Convert(oPosition.convert_to(AgEPositionType.eGeodetic), IGeodetic)
            Assert.assertIsNotNone(oGeodetic)
            self.m_logger.WriteLine6("\t\tGeodetic Lat is: {0}", oGeodetic.lat)
            self.m_logger.WriteLine6("\t\tGeodetic Lon is: {0}", oGeodetic.lon)
            self.m_logger.WriteLine6("\t\tGeodetic Alt is: {0}", oGeodetic.alt)
        elif oPosition.pos_type == AgEPositionType.eSpherical:
            oSpherical: "ISpherical" = clr.Convert(oPosition.convert_to(AgEPositionType.eSpherical), ISpherical)
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

        self.m_logger.WriteLine6("\tCurrent position type is: {0}", oPosition.pos_type)
        self.Display(oPosition)
        if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
            oCartesian: "ICartesian" = clr.Convert(oPosition.convert_to(AgEPositionType.eCartesian), ICartesian)
            Assert.assertIsNotNone(oCartesian)
            oCartesian.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oCartesian.pos_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oCartesian)
            oCartesian.x = 1234.5
            oCartesian.y = 54.321
            oCartesian.z = 789.012
            oCartesian.assign_cartesian(1234.5, 54.321, 789.012)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oCartesian)

            def action1():
                oCartesian.x = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action1)

            def action2():
                oCartesian.y = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action2)

            def action3():
                oCartesian.z = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action3)

            oCartesian.convert_to(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oCartesian.convert_to(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oCartesian.convert_to(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oCartesian.convert_to(AgEPositionType.eGeodetic)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oCartesian.convert_to(AgEPositionType.eSpherical)

        if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
            oCylindrical: "ICylindrical" = clr.Convert(oPosition.convert_to(AgEPositionType.eCylindrical), ICylindrical)
            Assert.assertIsNotNone(oCylindrical)
            oCylindrical.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oCylindrical.pos_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oCylindrical)
            oCylindrical.radius = 12203.4
            oCylindrical.z = 3513.17
            oCylindrical.lon = 1.23
            oCylindrical.assign_cylindrical(12203.4, 3513.17, 1.23)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oCylindrical)

            def action4():
                oCylindrical.radius = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action4)

            def action5():
                oCylindrical.z = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action5)

            def action6():
                oCylindrical.lon = 6.78

            TryCatchAssertBlock.DoAssert("", action6)

            oCylindrical.convert_to(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oCylindrical.convert_to(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oCylindrical.convert_to(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oCylindrical.convert_to(AgEPositionType.eGeodetic)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oCylindrical.convert_to(AgEPositionType.eSpherical)

        if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
            oGeocentric: "IGeocentric" = clr.Convert(oPosition.convert_to(AgEPositionType.eGeocentric), IGeocentric)
            Assert.assertIsNotNone(oGeocentric)
            oGeocentric.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oGeocentric.pos_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oGeocentric)
            oGeocentric.lat = 1.234
            oGeocentric.lon = 2.345
            oGeocentric.alt = 12.34
            oGeocentric.assign_geocentric(1.234, 2.345, 12.34)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oGeocentric)

            def action7():
                oGeocentric.lat = 2.34

            TryCatchAssertBlock.DoAssert("", action7)

            def action8():
                oGeocentric.lon = 6.78

            TryCatchAssertBlock.DoAssert("", action8)

            def action9():
                oGeocentric.alt = 6780000000000.0

            TryCatchAssertBlock.DoAssert("", action9)

            oGeocentric.convert_to(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oGeocentric.convert_to(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oGeocentric.convert_to(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oGeocentric.convert_to(AgEPositionType.eGeodetic)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oGeocentric.convert_to(AgEPositionType.eSpherical)

        if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
            oGeodetic: "IGeodetic" = clr.Convert(oPosition.convert_to(AgEPositionType.eGeodetic), IGeodetic)
            Assert.assertIsNotNone(oGeodetic)
            oGeodetic.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oGeodetic.pos_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oGeodetic)
            oGeodetic.lat = 0.190988679940043
            oGeodetic.lon = -0.743582379766568
            oGeodetic.alt = 0.640787459798838
            oGeodetic.assign_geodetic(0.190988679940043, -0.743582379766568, 0.640787459798838)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oGeodetic)

            def action10():
                oGeodetic.lat = 2.34

            TryCatchAssertBlock.DoAssert("", action10)

            def action11():
                oGeodetic.lon = 6.78

            TryCatchAssertBlock.DoAssert("", action11)

            def action12():
                oGeodetic.alt = 6780000000000.0

            TryCatchAssertBlock.DoAssert("", action12)

            oGeodetic.convert_to(AgEPositionType.eGeodetic)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oGeodetic.convert_to(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oGeodetic.convert_to(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oGeodetic.convert_to(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oGeodetic.convert_to(AgEPositionType.eSpherical)

        if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
            oSpherical: "ISpherical" = clr.Convert(oPosition.convert_to(AgEPositionType.eSpherical), ISpherical)
            Assert.assertIsNotNone(oSpherical)
            oSpherical.assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oSpherical.pos_type)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oSpherical)
            oSpherical.lat = 1
            oSpherical.lon = 2
            oSpherical.radius = 6355753
            oSpherical.assign_spherical(1, 2, 6355753)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oSpherical)

            def action13():
                oSpherical.lat = 2.34

            TryCatchAssertBlock.DoAssert("", action13)

            def action14():
                oSpherical.lon = 6.78

            TryCatchAssertBlock.DoAssert("", action14)

            def action15():
                oSpherical.radius = 67800000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action15)

            oSpherical.convert_to(AgEPositionType.eSpherical)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oSpherical.convert_to(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oSpherical.convert_to(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oSpherical.convert_to(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oSpherical.convert_to(AgEPositionType.eGeodetic)

        if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
            # SetAsCartesian
            # oPosition.AssignCartesian(0.190988679940043, -0.743582379766568, 0.640787459798838); // See 35836
            oPosition.assign_cartesian(6654000, 230000, 113000)
            self.Display(oPosition.convert_to(AgEPositionType.eCartesian))

        if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
            # SetAsCylindrical
            oPosition.assign_cylindrical(1, 500, 5)
            self.Display(oPosition.convert_to(AgEPositionType.eCylindrical))

        if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
            # SetAsGeocentric
            oPosition.assign_geocentric(0, 0, 1)
            self.Display(oPosition.convert_to(AgEPositionType.eGeocentric))

        if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
            # SetAsGeodetic
            oPosition.assign_geodetic(0.190988679940043, -0.743582379766568, 0.640787459798838)
            self.Display(oPosition.convert_to(AgEPositionType.eGeodetic))

        if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
            # SetAsSpherical
            oPosition.assign_spherical(-1, -1, 600355753)
            self.Display(oPosition.convert_to(AgEPositionType.eSpherical))

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

    # endregion
