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

    def __init__(self, oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection"):
        self.m_logger = Logger.Instance
        Assert.assertIsNotNone(oUnits)
        self.m_oUnits: "ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection" = oUnits

    # endregion

    # region Display method
    def Display(self, oPosition: "IPosition"):
        Assert.assertIsNotNone(oPosition)
        if oPosition.PosType == AgEPositionType.eCartesian:
            oCartesian: "ICartesian" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eCartesian), ICartesian)
            Assert.assertIsNotNone(oCartesian)
            self.m_logger.WriteLine6("\t\tCartesian X is: {0}", oCartesian.X)
            self.m_logger.WriteLine6("\t\tCartesian Y is: {0}", oCartesian.Y)
            self.m_logger.WriteLine6("\t\tCartesian Z is: {0}", oCartesian.Z)
        elif oPosition.PosType == AgEPositionType.eCylindrical:
            oCylindrical: "ICylindrical" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eCylindrical), ICylindrical)
            Assert.assertIsNotNone(oCylindrical)
            self.m_logger.WriteLine6("\t\tCylindrical Radius is: {0}", oCylindrical.Radius)
            self.m_logger.WriteLine6("\t\tCylindrical Z is: {0}", oCylindrical.Z)
            self.m_logger.WriteLine6("\t\tCylindrical Lon is: {0}", oCylindrical.Lon)
        elif oPosition.PosType == AgEPositionType.eGeocentric:
            oGeocentric: "IGeocentric" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eGeocentric), IGeocentric)
            Assert.assertIsNotNone(oGeocentric)
            self.m_logger.WriteLine6("\t\tGeocentric Lat is: {0}", oGeocentric.Lat)
            self.m_logger.WriteLine6("\t\tGeocentric Lon is: {0}", oGeocentric.Lon)
            self.m_logger.WriteLine6("\t\tGeocentric Alt is: {0}", oGeocentric.Alt)
        elif oPosition.PosType == AgEPositionType.eGeodetic:
            oGeodetic: "IGeodetic" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eGeodetic), IGeodetic)
            Assert.assertIsNotNone(oGeodetic)
            self.m_logger.WriteLine6("\t\tGeodetic Lat is: {0}", oGeodetic.Lat)
            self.m_logger.WriteLine6("\t\tGeodetic Lon is: {0}", oGeodetic.Lon)
            self.m_logger.WriteLine6("\t\tGeodetic Alt is: {0}", oGeodetic.Alt)
        elif oPosition.PosType == AgEPositionType.eSpherical:
            oSpherical: "ISpherical" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eSpherical), ISpherical)
            Assert.assertIsNotNone(oSpherical)
            self.m_logger.WriteLine6("\t\tSpherical Lat is: {0}", oSpherical.Lat)
            self.m_logger.WriteLine6("\t\tSpherical Lon is: {0}", oSpherical.Lon)
            self.m_logger.WriteLine6("\t\tSpherical Radius is: {0}", oSpherical.Radius)
        else:
            Assert.fail("Invalid Position type!")

    # endregion

    # region Run method
    def Run(self, oPosition: "IPosition", eTypes):
        self.m_logger.WriteLine("----- POSITION TEST ----- BEGIN -----")
        Assert.assertIsNotNone(oPosition)
        self.m_logger.WriteLine6("\tPosition test for: {0} positions", eTypes)
        # set DistanceUnit
        strDistanceUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit format is: {0}", strDistanceUnit)
        self.m_oUnits.SetCurrentUnit("DistanceUnit", "m")
        self.m_logger.WriteLine5(
            "\tThe new DistanceUnit format is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        Assert.assertEqual("m", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # set LatitudeUnit
        strLatitudeUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit")
        self.m_logger.WriteLine5("\tThe current LatitudeUnit format is: {0}", strLatitudeUnit)
        self.m_oUnits.SetCurrentUnit("LatitudeUnit", "rad")
        self.m_logger.WriteLine5(
            "\tThe new LatitudeUnit format is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit")
        )
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))
        # set LongitudeUnit
        strLongitudeUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
        self.m_logger.WriteLine5("\tThe current LongitudeUnit format is: {0}", strLongitudeUnit)
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", "rad")
        self.m_logger.WriteLine5(
            "\tThe new LongitudeUnit format is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
        )
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))
        # set AngleUnit
        strAngleUnit: str = self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit format is: {0}", strAngleUnit)
        self.m_oUnits.SetCurrentUnit("AngleUnit", "rad")
        self.m_logger.WriteLine5("\tThe new AngleUnit format is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        Assert.assertEqual("rad", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))

        self.m_logger.WriteLine6("\tCurrent position type is: {0}", oPosition.PosType)
        self.Display(oPosition)
        if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
            oCartesian: "ICartesian" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eCartesian), ICartesian)
            Assert.assertIsNotNone(oCartesian)
            oCartesian.Assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oCartesian.PosType)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oCartesian)
            oCartesian.X = 1234.5
            oCartesian.Y = 54.321
            oCartesian.Z = 789.012
            oCartesian.AssignCartesian(1234.5, 54.321, 789.012)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oCartesian)

            def action1():
                oCartesian.X = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action1)

            def action2():
                oCartesian.Y = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action2)

            def action3():
                oCartesian.Z = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action3)

            oCartesian.ConvertTo(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oCartesian.ConvertTo(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oCartesian.ConvertTo(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oCartesian.ConvertTo(AgEPositionType.eGeodetic)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oCartesian.ConvertTo(AgEPositionType.eSpherical)

        if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
            oCylindrical: "ICylindrical" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eCylindrical), ICylindrical)
            Assert.assertIsNotNone(oCylindrical)
            oCylindrical.Assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oCylindrical.PosType)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oCylindrical)
            oCylindrical.Radius = 12203.4
            oCylindrical.Z = 3513.17
            oCylindrical.Lon = 1.23
            oCylindrical.AssignCylindrical(12203.4, 3513.17, 1.23)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oCylindrical)

            def action4():
                oCylindrical.Radius = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action4)

            def action5():
                oCylindrical.Z = 567800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action5)

            def action6():
                oCylindrical.Lon = 6.78

            TryCatchAssertBlock.DoAssert("", action6)

            oCylindrical.ConvertTo(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oCylindrical.ConvertTo(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oCylindrical.ConvertTo(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oCylindrical.ConvertTo(AgEPositionType.eGeodetic)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oCylindrical.ConvertTo(AgEPositionType.eSpherical)

        if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
            oGeocentric: "IGeocentric" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eGeocentric), IGeocentric)
            Assert.assertIsNotNone(oGeocentric)
            oGeocentric.Assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oGeocentric.PosType)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oGeocentric)
            oGeocentric.Lat = 1.234
            oGeocentric.Lon = 2.345
            oGeocentric.Alt = 12.34
            oGeocentric.AssignGeocentric(1.234, 2.345, 12.34)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oGeocentric)

            def action7():
                oGeocentric.Lat = 2.34

            TryCatchAssertBlock.DoAssert("", action7)

            def action8():
                oGeocentric.Lon = 6.78

            TryCatchAssertBlock.DoAssert("", action8)

            def action9():
                oGeocentric.Alt = 6780000000000.0

            TryCatchAssertBlock.DoAssert("", action9)

            oGeocentric.ConvertTo(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oGeocentric.ConvertTo(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oGeocentric.ConvertTo(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oGeocentric.ConvertTo(AgEPositionType.eGeodetic)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oGeocentric.ConvertTo(AgEPositionType.eSpherical)

        if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
            oGeodetic: "IGeodetic" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eGeodetic), IGeodetic)
            Assert.assertIsNotNone(oGeodetic)
            oGeodetic.Assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oGeodetic.PosType)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oGeodetic)
            oGeodetic.Lat = 0.190988679940043
            oGeodetic.Lon = -0.743582379766568
            oGeodetic.Alt = 0.640787459798838
            oGeodetic.AssignGeodetic(0.190988679940043, -0.743582379766568, 0.640787459798838)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oGeodetic)

            def action10():
                oGeodetic.Lat = 2.34

            TryCatchAssertBlock.DoAssert("", action10)

            def action11():
                oGeodetic.Lon = 6.78

            TryCatchAssertBlock.DoAssert("", action11)

            def action12():
                oGeodetic.Alt = 6780000000000.0

            TryCatchAssertBlock.DoAssert("", action12)

            oGeodetic.ConvertTo(AgEPositionType.eGeodetic)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oGeodetic.ConvertTo(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oGeodetic.ConvertTo(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oGeodetic.ConvertTo(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
                oGeodetic.ConvertTo(AgEPositionType.eSpherical)

        if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
            oSpherical: "ISpherical" = clr.Convert(oPosition.ConvertTo(AgEPositionType.eSpherical), ISpherical)
            Assert.assertIsNotNone(oSpherical)
            oSpherical.Assign(oPosition)
            self.m_logger.WriteLine6("\tNew position type is: {0}", oSpherical.PosType)
            self.m_logger.WriteLine("\t\tCurrent values:")
            self.Display(oSpherical)
            oSpherical.Lat = 1
            oSpherical.Lon = 2
            oSpherical.Radius = 6355753
            oSpherical.AssignSpherical(1, 2, 6355753)
            self.m_logger.WriteLine("\t\tNew values:")
            self.Display(oSpherical)

            def action13():
                oSpherical.Lat = 2.34

            TryCatchAssertBlock.DoAssert("", action13)

            def action14():
                oSpherical.Lon = 6.78

            TryCatchAssertBlock.DoAssert("", action14)

            def action15():
                oSpherical.Radius = 67800000000000000000000000.0

            TryCatchAssertBlock.DoAssert("", action15)

            oSpherical.ConvertTo(AgEPositionType.eSpherical)
            if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
                oSpherical.ConvertTo(AgEPositionType.eCartesian)
            if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
                oSpherical.ConvertTo(AgEPositionType.eCylindrical)
            if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
                oSpherical.ConvertTo(AgEPositionType.eGeocentric)
            if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
                oSpherical.ConvertTo(AgEPositionType.eGeodetic)

        if ((eTypes & PositionTest.Positions.Cartesian)) == PositionTest.Positions.Cartesian:
            # SetAsCartesian
            # oPosition.AssignCartesian(0.190988679940043, -0.743582379766568, 0.640787459798838); // See 35836
            oPosition.AssignCartesian(6654000, 230000, 113000)
            self.Display(oPosition.ConvertTo(AgEPositionType.eCartesian))

        if ((eTypes & PositionTest.Positions.Cylindrical)) == PositionTest.Positions.Cylindrical:
            # SetAsCylindrical
            oPosition.AssignCylindrical(1, 500, 5)
            self.Display(oPosition.ConvertTo(AgEPositionType.eCylindrical))

        if ((eTypes & PositionTest.Positions.Geocentric)) == PositionTest.Positions.Geocentric:
            # SetAsGeocentric
            oPosition.AssignGeocentric(0, 0, 1)
            self.Display(oPosition.ConvertTo(AgEPositionType.eGeocentric))

        if ((eTypes & PositionTest.Positions.Geodetic)) == PositionTest.Positions.Geodetic:
            # SetAsGeodetic
            oPosition.AssignGeodetic(0.190988679940043, -0.743582379766568, 0.640787459798838)
            self.Display(oPosition.ConvertTo(AgEPositionType.eGeodetic))

        if ((eTypes & PositionTest.Positions.Spherical)) == PositionTest.Positions.Spherical:
            # SetAsSpherical
            oPosition.AssignSpherical(-1, -1, 600355753)
            self.Display(oPosition.ConvertTo(AgEPositionType.eSpherical))

        # restore AngleUnit
        self.m_oUnits.SetCurrentUnit("AngleUnit", strAngleUnit)
        self.m_logger.WriteLine5(
            "\tThe restored AngleUnit format is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit")
        )
        Assert.assertEqual(strAngleUnit, self.m_oUnits.GetCurrentUnitAbbrv("AngleUnit"))
        # restore DistanceUnit
        self.m_oUnits.SetCurrentUnit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5(
            "\tThe restored DistanceUnit format is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit")
        )
        Assert.assertEqual(strDistanceUnit, self.m_oUnits.GetCurrentUnitAbbrv("DistanceUnit"))
        # restore LatitudeUnit
        self.m_oUnits.SetCurrentUnit("LatitudeUnit", strLatitudeUnit)
        self.m_logger.WriteLine5(
            "\tThe restored LatitudeUnit format is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit")
        )
        Assert.assertEqual(strLatitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LatitudeUnit"))
        # restore LongitudeUnit
        self.m_oUnits.SetCurrentUnit("LongitudeUnit", strLongitudeUnit)
        self.m_logger.WriteLine5(
            "\tThe restored LongitudeUnit format is: {0}", self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit")
        )
        Assert.assertEqual(strLongitudeUnit, self.m_oUnits.GetCurrentUnitAbbrv("LongitudeUnit"))
        self.m_logger.WriteLine("----- POSITION TEST ----- END -----")

    # endregion
