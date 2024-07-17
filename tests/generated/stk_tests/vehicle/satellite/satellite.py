import pytest
from test_util import *
from access_constraints.access_constraint_helper import *
from app_provider import *
from antenna.antenna_helper import *
from assert_extension import *
from assertion_harness import *
from events.log_message_monitor import *
from events.object_changed_monitor import *
from interfaces.stk_objects import *
from logger import *
from report_comparison import *
from seet_helper import *
from vehicle.vehicle_basic import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from parameterized import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        EarlyBoundTests.InitHelper()

    @staticmethod
    def InitHelper():
        TestBase.LoadTestScenario(Path.Combine("SatelliteTests", "SatelliteTests.sc"))
        EarlyBoundTests.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SAT = None
        TestBase.Uninitialize()

    # endregion

    AG_SAT: "Satellite" = None

    def test_ReferenceVehicle(self):
        sat1: "Satellite" = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "REQ48908")
        )
        (VehiclePropagatorTwoBody(sat1.propagator)).propagate()
        link: "LinkToObject" = sat1.reference_vehicle
        objects = link.available_objects
        Console.WriteLine(link.name)
        stkObject: str
        for stkObject in objects:
            Console.WriteLine(stkObject)

        link.bind_to("Aircraft/Boing737")
        Assert.assertEqual(
            "Aircraft/Boing737", ((link.linked_object.class_name + "/") + link.linked_object.instance_name)
        )
        (IStkObject(sat1)).unload()

    # region X47133

    def FindGPSElementUsingEpoch(self, preview: "VehicleGPSElementCollection", epoch: typing.Any):
        Assert.assertIsNotNone(preview)
        elt: "VehicleGPSElement"
        for elt in preview:
            if str(elt.epoch).startswith(str(epoch)):
                return True
        return False

    def test_BasicSGP4(self):
        satellite: "Satellite" = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "MySatellite_12125")
        )

        # Configure propagator's TLE file path
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
        sgp4: "VehiclePropagatorSGP4" = VehiclePropagatorSGP4(satellite.propagator)

        dbpath: str = Path.Combine(TestBase.GetSTKDBDir(), r"Databases\Satellite\stkAllTLE.tce")
        sgp4.common_tasks.add_segs_from_file("2215", dbpath)

        sgp4.auto_update_enabled = True
        sgp4.segments.ssc_number = "2215"
        sgp4.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        sgp4.auto_update.file_source.filename = dbpath

        preview = sgp4.auto_update.file_source.preview()
        Assert.assertTrue((Array.Length(preview) != 0))

        # Propagate
        sgp4.propagate()

        preview = sgp4.auto_update.file_source.preview()
        Assert.assertTrue((Array.Length(preview) != 0))
        rx = Regex(r"^([-]?\d+) ([-]?\d+[.]?\d+) ([-]?\d+)$")
        line: typing.Any
        for line in preview:
            m = rx.Match(str(line))
            Assert.assertEqual(str(m.Groups[1]), sgp4.segments.ssc_number)

        (IStkObject(satellite)).unload()

    # endregion

    # region X46894
    @parameterized.expand([(29, "GPSSatellite1", "1 Jan 1993 00:00:00.000", "29 Oct 2007 00:00:00.000")])
    def test_BasicGPSPolicyStepOutOfRangeException(
        self, nPRN: int, sInstanceName: str, startTime: typing.Any, stopTime: typing.Any
    ):
        def code1():
            sat: "Satellite" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, sInstanceName), Satellite
            )
            try:
                sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GPS)
                gps: "VehiclePropagatorGPS" = clr.CastAs(sat.propagator, VehiclePropagatorGPS)
                gps.auto_update_enabled = True
                gps.auto_update.selected_source = VEHICLE_GPS_AUTO_UPDATE_SOURCE.GPS_AUTO_UPDATE_SOURCE_ONLINE
                gps.prn = nPRN
                gps.auto_update.properties.selection = VEHICLE_GPS_ELEM_SELECTION.GPS_ELEM_SELECTION_USE_FIRST

                gps.ephemeris_interval.set_start_and_stop_times(startTime, stopTime)

                gps.step = 0.0001

            finally:
                TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, sInstanceName)

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("Value range is 0.00100000 sec to", str(ex), "Exception message mismatch")

    # endregion

    # region X46894
    @parameterized.expand([(29, "GPSSatellite1", "1 Jan 1993 00:00:00.000", "29 Oct 2007 00:00:00.000")])
    def test_BasicGPSPolicyStepSize(self, nPRN: int, sInstanceName: str, startTime: typing.Any, stopTime: typing.Any):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, sInstanceName), Satellite
        )
        try:
            sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GPS)
            gps: "VehiclePropagatorGPS" = clr.CastAs(sat.propagator, VehiclePropagatorGPS)
            gps.auto_update_enabled = True
            gps.auto_update.selected_source = VEHICLE_GPS_AUTO_UPDATE_SOURCE.GPS_AUTO_UPDATE_SOURCE_ONLINE
            gps.prn = nPRN
            gps.auto_update.properties.selection = VEHICLE_GPS_ELEM_SELECTION.GPS_ELEM_SELECTION_USE_FIRST

            gps.ephemeris_interval.set_start_and_stop_times(startTime, stopTime)

            gps.step = Double.MaxValue
            gps.step = TestBase.Application.conversion_utility.convert_quantity("TimeUnit", "yr", "sec", 1)

        finally:
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, sInstanceName)

    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.TestConstraintCollection(EarlyBoundTests.AG_SAT.access_constraints)
        oHelper.DoTest(
            EarlyBoundTests.AG_SAT.access_constraints, IStkObject(EarlyBoundTests.AG_SAT), TestBase.TemporaryDirectory
        )

    # endregion

    # region BasicAttitudeDifference
    @category("Basic Tests")
    def test_BasicAttitudeDifference(self):
        oHelper = BasicAttitudeDifferenceHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_SAT, IStkObject))

    # endregion

    # region BasicAttitude
    @category("Basic Tests")
    def test_BasicAttitude(self):
        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")

        # Propagate the Satellite
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY, EarlyBoundTests.AG_SAT.propagator_type)

        oPropagator: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(EarlyBoundTests.AG_SAT.propagator)
        Assert.assertIsNotNone(oPropagator)

        oPropagator.propagate()

        # AttitudeType
        TestBase.logger.WriteLine6("\tThe current Attitude type is: {0}", EarlyBoundTests.AG_SAT.attitude_type)
        # AttitudeSupportedTypes
        arTypes = EarlyBoundTests.AG_SAT.attitude_supported_types
        TestBase.logger.WriteLine3("\tThe LaunchVehicle supports: {0} Attitude types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VEHICLE_ATTITUDE" = VEHICLE_ATTITUDE(int(arTypes[iIndex][0]))
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_SAT.is_attitude_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetAttitudeType
            EarlyBoundTests.AG_SAT.set_attitude_type(eType)
            TestBase.logger.WriteLine6("\t\tThe new Attitude type is: {0}", EarlyBoundTests.AG_SAT.attitude_type)
            Assert.assertEqual(eType, EarlyBoundTests.AG_SAT.attitude_type)
            if eType == VEHICLE_ATTITUDE.ATTITUDE_STANDARD:
                # Attitude
                oHelper = BasicAttitudeStandardHelper(TestBase.Application)
                oHelper.Run(IVehicleAttitudeStandard(EarlyBoundTests.AG_SAT.attitude))
            elif eType == VEHICLE_ATTITUDE.ATTITUDE_REAL_TIME:
                oHelper = BasicAttitudeRealTimeHelper(
                    TestBase.Application, clr.CastAs(EarlyBoundTests.AG_SAT, IStkObject)
                )
                oHelper.Run(VehicleAttitudeRealTime(EarlyBoundTests.AG_SAT.attitude))
            else:
                Assert.fail("The {0} type should be supported!", eType)

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")

    # endregion

    # region BasicComputingAccess
    @category("Basic Tests")
    def test_BasicComputingAccess(self):
        # create a new Satellite
        oSatellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Spy"), Satellite
        )
        Assert.assertIsNotNone(oSatellite, "XZCCNZ384")

        # propagate satellite
        oPropagator: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(oSatellite.propagator)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.propagate()
        oFacility: "IStkObject" = TestBase.Application.current_scenario.children["Target1"]
        Assert.assertIsNotNone(oFacility)

        # compute access
        oAccess: "StkAccess" = (IStkObject(oSatellite)).get_access_to_object(oFacility)
        Assert.assertIsNotNone(oAccess)
        oAccess.compute_access()

        # Get and display the Computed Access Intervals
        oIntervalCollection: "IntervalCollection" = oAccess.computed_access_interval_times
        Assert.assertIsNotNone(oIntervalCollection)

        # Set the intervals to use to the Computed Access Intervals
        arIntervals = oIntervalCollection.to_array(0, -1)
        oAccess.specify_access_intervals(arIntervals)

    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_SAT)
        obj: "IStkObject" = IStkObject(EarlyBoundTests.AG_SAT)

        # Short Description test
        obj.short_description = "This is a new short description."
        Assert.assertEqual("This is a new short description.", obj.short_description)
        obj.short_description = ""
        Assert.assertEqual("", obj.short_description)

        # Long Description test
        obj.long_description = "This is a new Long description."
        Assert.assertEqual("This is a new Long description.", obj.long_description)
        obj.long_description = ""
        Assert.assertEqual("", obj.long_description)

    # endregion

    # region BasicPassBreak
    @category("Basic Tests")
    def test_BasicPassBreak(self):
        EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LATITUDE)
        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.CENTRAL_BODY_FIXED
        Assert.assertEqual(
            VEHICLE_COORDINATE_SYSTEM.CENTRAL_BODY_FIXED, EarlyBoundTests.AG_SAT.pass_break.coordinate_system
        )
        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.INERTIAL
        Assert.assertEqual(VEHICLE_COORDINATE_SYSTEM.INERTIAL, EarlyBoundTests.AG_SAT.pass_break.coordinate_system)

        EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LATITUDE)
        Assert.assertEqual(
            VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LATITUDE, EarlyBoundTests.AG_SAT.pass_break.definition.break_angle_type
        )
        EarlyBoundTests.AG_SAT.pass_break.definition.direction = VEHICLE_DIRECTION.ASCENDING
        Assert.assertEqual(VEHICLE_DIRECTION.ASCENDING, EarlyBoundTests.AG_SAT.pass_break.definition.direction)
        EarlyBoundTests.AG_SAT.pass_break.definition.direction = VEHICLE_DIRECTION.DESCENDING
        Assert.assertEqual(VEHICLE_DIRECTION.DESCENDING, EarlyBoundTests.AG_SAT.pass_break.definition.direction)

        EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LATITUDE)
        Assert.assertEqual(
            VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LATITUDE, EarlyBoundTests.AG_SAT.pass_break.definition.break_angle_type
        )
        lat: "VehicleBreakAngleBreakByLatitude" = VehicleBreakAngleBreakByLatitude(
            EarlyBoundTests.AG_SAT.pass_break.definition.break_angle
        )
        lat.latitude = 6
        Assert.assertEqual(6, lat.latitude)

        EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LONGITUDE)
        Assert.assertEqual(
            VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LONGITUDE, EarlyBoundTests.AG_SAT.pass_break.definition.break_angle_type
        )
        lon: "VehicleBreakAngleBreakByLongitude" = VehicleBreakAngleBreakByLongitude(
            EarlyBoundTests.AG_SAT.pass_break.definition.break_angle
        )
        lon.longitude = 4
        Assert.assertEqual(4, lon.longitude)
        bCaught: bool = False
        try:
            EarlyBoundTests.AG_SAT.pass_break.definition.direction = VEHICLE_DIRECTION.ASCENDING

        except:
            bCaught = True
            TestBase.logger.WriteLine6(
                "We are not able to set Definition Direction when using {0}",
                EarlyBoundTests.AG_SAT.pass_break.definition.break_angle_type,
            )

        if not bCaught:
            Assert.fail()

        bCaught = False
        try:
            EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.CENTRAL_BODY_FIXED

        except:
            bCaught = True
            TestBase.logger.WriteLine6(
                "We are not able to set Coordinate System when using {0}",
                EarlyBoundTests.AG_SAT.pass_break.definition.break_angle_type,
            )

        if not bCaught:
            Assert.fail()

        bCaught = False

        EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LATITUDE)
        Assert.assertEqual(
            VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LATITUDE, EarlyBoundTests.AG_SAT.pass_break.definition.break_angle_type
        )

        EarlyBoundTests.AG_SAT.pass_break.partial_pass_measurement = VEHICLE_PARTIAL_PASS_MEASUREMENT.ANGLE
        Assert.assertEqual(
            VEHICLE_PARTIAL_PASS_MEASUREMENT.ANGLE, EarlyBoundTests.AG_SAT.pass_break.partial_pass_measurement
        )
        EarlyBoundTests.AG_SAT.pass_break.partial_pass_measurement = VEHICLE_PARTIAL_PASS_MEASUREMENT.MEAN_ARG_OF_LAT
        Assert.assertEqual(
            VEHICLE_PARTIAL_PASS_MEASUREMENT.MEAN_ARG_OF_LAT, EarlyBoundTests.AG_SAT.pass_break.partial_pass_measurement
        )
        EarlyBoundTests.AG_SAT.pass_break.partial_pass_measurement = VEHICLE_PARTIAL_PASS_MEASUREMENT.TIME
        Assert.assertEqual(
            VEHICLE_PARTIAL_PASS_MEASUREMENT.TIME, EarlyBoundTests.AG_SAT.pass_break.partial_pass_measurement
        )

        EarlyBoundTests.AG_SAT.pass_break.repeat_ground_track_numbering.first_path_num = 5
        Assert.assertEqual(5, EarlyBoundTests.AG_SAT.pass_break.repeat_ground_track_numbering.first_path_num)

        EarlyBoundTests.AG_SAT.pass_break.repeat_ground_track_numbering.revs_to_repeat = 6
        Assert.assertEqual(6, EarlyBoundTests.AG_SAT.pass_break.repeat_ground_track_numbering.revs_to_repeat)

        oPassBreak: "VehiclePassBreak" = EarlyBoundTests.AG_SAT.pass_break
        Assert.assertIsNotNone(oPassBreak)
        TestBase.logger.WriteLine6("The current Pass Numbering type is: {0}", oPassBreak.pass_numbering_type)
        # PASS_NUMBERING_FIRST_PASS_NUM
        oPassBreak.set_pass_numbering_type(VEHICLE_PASS_NUMBERING.PASS_NUMBERING_FIRST_PASS_NUM)
        TestBase.logger.WriteLine6("The new Pass Numbering type is: {0}", oPassBreak.pass_numbering_type)
        Assert.assertEqual(VEHICLE_PASS_NUMBERING.PASS_NUMBERING_FIRST_PASS_NUM, oPassBreak.pass_numbering_type)
        oPass1: "VehiclePassNumberingFirstPassNum" = VehiclePassNumberingFirstPassNum(oPassBreak.pass_numbering)
        Assert.assertIsNotNone(oPass1)
        TestBase.logger.WriteLine3("The current First Pass Num is: {0}", oPass1.first_pass_num)
        oPass1.first_pass_num = 4
        TestBase.logger.WriteLine3("The new First Pass Num is: {0}", oPass1.first_pass_num)
        Assert.assertEqual(4, oPass1.first_pass_num)
        # PASS_NUMBERING_DATE_OF_FIRST_PASS
        oPassBreak.set_pass_numbering_type(VEHICLE_PASS_NUMBERING.PASS_NUMBERING_DATE_OF_FIRST_PASS)
        TestBase.logger.WriteLine6("The new Pass Numbering type is: {0}", oPassBreak.pass_numbering_type)
        Assert.assertEqual(VEHICLE_PASS_NUMBERING.PASS_NUMBERING_DATE_OF_FIRST_PASS, oPassBreak.pass_numbering_type)
        oPass2: "VehiclePassNumberingDateOfFirstPass" = VehiclePassNumberingDateOfFirstPass(oPassBreak.pass_numbering)
        Assert.assertIsNotNone(oPass2)
        TestBase.logger.WriteLine3("The current First Pass Num is: {0}", oPass2.first_pass_num)
        oPass2.first_pass_num = 14
        TestBase.logger.WriteLine3("The new First Pass Num is: {0}", oPass2.first_pass_num)
        Assert.assertEqual(14, oPass2.first_pass_num)
        TestBase.logger.WriteLine6(
            "The current Pass Data Epoch Time Instant is: {0}", oPass2.pass_data_epoch.time_instant
        )
        oPass2.pass_data_epoch.set_explicit_time("12 Oct 2005 12:34:56.789")
        TestBase.logger.WriteLine6("The new Pass Data Epoch Time Instant is: {0}", oPass2.pass_data_epoch.time_instant)
        Assert.assertEqual("12 Oct 2005 12:34:56.789", oPass2.pass_data_epoch.time_instant)
        # PASS_NUMBERING_MAINTAIN_PASS_NUM
        oPassBreak.set_pass_numbering_type(VEHICLE_PASS_NUMBERING.PASS_NUMBERING_MAINTAIN_PASS_NUM)
        TestBase.logger.WriteLine6("The new Pass Numbering type is: {0}", oPassBreak.pass_numbering_type)
        Assert.assertEqual(VEHICLE_PASS_NUMBERING.PASS_NUMBERING_MAINTAIN_PASS_NUM, oPassBreak.pass_numbering_type)
        oPass3: "IVehiclePassNumbering" = oPassBreak.pass_numbering
        if oPass3 == None:
            TestBase.logger.WriteLine("The PassNumbering returned NULL for the PASS_NUMBERING_MAINTAIN_PASS_NUM type.")

        else:
            Assert.fail("The PassNumbering should return NULL!")

        # PASS_NUMBERING_USE_PROPAGATOR_PASS_DATA
        oPassBreak.set_pass_numbering_type(VEHICLE_PASS_NUMBERING.PASS_NUMBERING_USE_PROPAGATOR_PASS_DATA)
        TestBase.logger.WriteLine6("The new Pass Numbering type is: {0}", oPassBreak.pass_numbering_type)
        Assert.assertEqual(
            VEHICLE_PASS_NUMBERING.PASS_NUMBERING_USE_PROPAGATOR_PASS_DATA, oPassBreak.pass_numbering_type
        )
        oPass3 = oPassBreak.pass_numbering
        if oPass3 == None:
            TestBase.logger.WriteLine(
                "The PassNumbering returned NULL for the PASS_NUMBERING_USE_PROPAGATOR_PASS_DATA type."
            )

        else:
            Assert.fail("The PassNumbering should return NULL!")

        # PASS_NUMBERING_UNKNOWN
        try:
            bCaught = False
            oPassBreak.set_pass_numbering_type(VEHICLE_PASS_NUMBERING.PASS_NUMBERING_UNKNOWN)

        except Exception as e:
            bCaught = True
            TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

        if not bCaught:
            Assert.fail()

        # --------------------------------------
        # New coordinate systems
        # --------------------------------------

        supportedCoordinateSystems = EarlyBoundTests.AG_SAT.pass_break.supported_coordinate_systems

        EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LATITUDE)

        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.CENTRAL_BODY_FIXED
        Assert.assertEqual(
            EarlyBoundTests.AG_SAT.pass_break.coordinate_system, VEHICLE_COORDINATE_SYSTEM.CENTRAL_BODY_FIXED
        )
        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.INERTIAL
        Assert.assertEqual(EarlyBoundTests.AG_SAT.pass_break.coordinate_system, VEHICLE_COORDINATE_SYSTEM.INERTIAL)
        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.TRUE_OF_DATE
        Assert.assertEqual(EarlyBoundTests.AG_SAT.pass_break.coordinate_system, VEHICLE_COORDINATE_SYSTEM.TRUE_OF_DATE)
        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.TRUE_OF_EPOCH
        Assert.assertEqual(EarlyBoundTests.AG_SAT.pass_break.coordinate_system, VEHICLE_COORDINATE_SYSTEM.TRUE_OF_EPOCH)

        EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VEHICLE_BREAK_ANGLE_TYPE.BREAK_BY_LONGITUDE)

        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.INERTIAL
        Assert.assertEqual(EarlyBoundTests.AG_SAT.pass_break.coordinate_system, VEHICLE_COORDINATE_SYSTEM.INERTIAL)
        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.TRUE_OF_DATE
        Assert.assertEqual(EarlyBoundTests.AG_SAT.pass_break.coordinate_system, VEHICLE_COORDINATE_SYSTEM.TRUE_OF_DATE)
        EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.TRUE_OF_EPOCH
        Assert.assertEqual(EarlyBoundTests.AG_SAT.pass_break.coordinate_system, VEHICLE_COORDINATE_SYSTEM.TRUE_OF_EPOCH)

        with pytest.raises(Exception):
            EarlyBoundTests.AG_SAT.pass_break.coordinate_system = VEHICLE_COORDINATE_SYSTEM.CENTRAL_BODY_FIXED

    # endregion

    # region BasicMassProperties
    @category("Basic Tests")
    def test_BasicMassProperties(self):
        TestBase.Application.unit_preferences.set_current_unit("MassUnit", "kg")

        oldMass: float = EarlyBoundTests.AG_SAT.mass_properties.mass

        EarlyBoundTests.AG_SAT.mass_properties.mass = 0.002
        Assert.assertEqual(0.002, EarlyBoundTests.AG_SAT.mass_properties.mass)

        bCaught: bool = False
        try:
            EarlyBoundTests.AG_SAT.mass_properties.mass = -5

        except:
            bCaught = True
            TestBase.logger.WriteLine("Satellite Mass bounds are .001 to 1 billion.")

        if not bCaught:
            Assert.fail()

        EarlyBoundTests.AG_SAT.mass_properties.inertia.ixx = 30
        EarlyBoundTests.AG_SAT.mass_properties.inertia.ixy = 4700
        EarlyBoundTests.AG_SAT.mass_properties.inertia.ixz = 20
        EarlyBoundTests.AG_SAT.mass_properties.inertia.iyy = 70
        EarlyBoundTests.AG_SAT.mass_properties.inertia.iyz = 10
        EarlyBoundTests.AG_SAT.mass_properties.inertia.izz = 120

        Assert.assertEqual(30, EarlyBoundTests.AG_SAT.mass_properties.inertia.ixx)
        Assert.assertEqual(4700, EarlyBoundTests.AG_SAT.mass_properties.inertia.ixy)
        Assert.assertEqual(20, EarlyBoundTests.AG_SAT.mass_properties.inertia.ixz)
        Assert.assertEqual(70, EarlyBoundTests.AG_SAT.mass_properties.inertia.iyy)
        Assert.assertEqual(10, EarlyBoundTests.AG_SAT.mass_properties.inertia.iyz)
        Assert.assertEqual(120, EarlyBoundTests.AG_SAT.mass_properties.inertia.izz)

        EarlyBoundTests.AG_SAT.mass_properties.mass = oldMass

    # endregion

    # region BasicGroundEllipses
    @category("Basic Tests")
    def test_BasicGroundEllipses(self):
        oHelper = BasicGroundEllipsesHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.ground_ellipses, True)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        satObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_SAT, IStkObject)
        oHelper.Run(satObject)
        oHelper.TestObjectFilesArray(satObject.object_files)

    # endregion

    # region SpatialInfo
    @category("SpatialInfo")
    def test_SpatialInfo(self):
        helper = SpatialInfoHelper(TestBase.Application)
        helper.Run(clr.CastAs(EarlyBoundTests.AG_SAT, IStkObject))

    # endregion

    # region SGP4Default
    def test_SGP4Default(self):
        sInstanceName: str = "SGP4BackwardCompat_Satellite"
        # ----------------------------------------------------------
        # Uses default SGP4 configuration to propagate a vehicle.
        # The test is used to make sure the backward compatibility
        # ----------------------------------------------------------
        TestBase.Application.unit_preferences.reset_units()

        oSat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, sInstanceName), Satellite
        )
        o: "IStkObject" = clr.CastAs(oSat, IStkObject)
        oSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)

        with ObjectChangedMonitor(TestBase.Application) as monitor:
            (clr.CastAs(oSat.propagator, VehiclePropagatorSGP4)).propagate()
            # Wait for about two seconds
            dt = DateTime.Now
            dt = dt.AddSeconds(1)
            while True:
                TestBase.DoEvents()
                if DateTime.Now > dt:
                    break

                import time

                time.sleep((100 / 1000.0))

                if not True:
                    break
            Assert.assertTrue((monitor.Counter != 0))
            Assert.assertEqual(monitor.Sender, o.path)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, sInstanceName)

    # endregion

    # region DragModelTest
    def test_DragModelTest(self):
        TestBase.logger.WriteLine("----- THE DRAG MODEL TEST ----- BEGIN -----")
        # ResetUnits
        TestBase.Application.unit_preferences.reset_units()
        dragSat: "Satellite" = Satellite(
            (TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "HPOPTest"))
        )
        dragSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        TestBase.logger.WriteLine6("\t\tThe new PropagatorType is: {0}", dragSat.propagator_type)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP, dragSat.propagator_type)
        # Drag
        # AtmosphericDensityModel (CIRA72)
        oDrag: "VehicleHPOPForceModelDrag" = (VehiclePropagatorHPOP((dragSat.propagator))).force_model.drag
        oDrag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.CIRA72
        TestBase.logger.WriteLine6("\tThe new AtmosphericDensityModel is: {0}", oDrag.atmospheric_density_model)
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.CIRA72, oDrag.atmospheric_density_model)

        # LowAltAtmosphericDensityModel (MSIS00)
        oDrag.low_altitude_atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS00
        TestBase.logger.WriteLine6(
            "\tThe new LowAltAtmosphericDensityModel is: {0}", oDrag.low_altitude_atmospheric_density_model
        )
        Assert.assertEqual(ATMOSPHERIC_DENSITY_MODEL.MSIS00, oDrag.low_altitude_atmospheric_density_model)

        # LowAltAtmosDensityModel (MSIS00)
        oDrag.low_altitude_atmos_density_model = LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_MSISE1990
        TestBase.logger.WriteLine6("\tThe new LowAltAtmosDensityModel is: {0}", oDrag.low_altitude_atmos_density_model)
        Assert.assertEqual(
            LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_MSISE1990, oDrag.low_altitude_atmos_density_model
        )
        # Reset LowAltAtmosDensityModel
        oDrag.low_altitude_atmos_density_model = LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL.DEN_MODEL_NONE

        # Drag Model
        oDrag.set_drag_model_type(DRAG_MODEL.SPHERICAL)
        TestBase.logger.WriteLine6("\t\tThe new Drag Model type is :{0}", oDrag.drag_model_type)
        Assert.assertEqual(DRAG_MODEL.SPHERICAL, oDrag.drag_model_type)
        # Spherical Drag Model
        # Cd
        (VehicleHPOPDragModelSpherical((oDrag.drag_model))).cd = -1.23
        TestBase.logger.WriteLine6("\tThe new Cd is: {0}", (VehicleHPOPDragModelSpherical((oDrag.drag_model))).cd)
        Assert.assertEqual(-1.23, (VehicleHPOPDragModelSpherical((oDrag.drag_model))).cd)

        with pytest.raises(Exception):
            (VehicleHPOPDragModelSpherical((oDrag.drag_model))).cd = 120.34

        # AreaMassRatio
        TestBase.logger.WriteLine6(
            "\tThe current AreaMassRatio is: {0}", (VehicleHPOPDragModelSpherical((oDrag.drag_model))).area_mass_ratio
        )
        (VehicleHPOPDragModelSpherical((oDrag.drag_model))).area_mass_ratio = 123
        TestBase.logger.WriteLine6(
            "\tThe new AreaMassRatio is: {0}", (VehicleHPOPDragModelSpherical((oDrag.drag_model))).area_mass_ratio
        )
        Assert.assertEqual(123, (VehicleHPOPDragModelSpherical((oDrag.drag_model))).area_mass_ratio)

        with pytest.raises(Exception):
            (VehicleHPOPDragModelSpherical((oDrag.drag_model))).area_mass_ratio = -12.34

        TestBase.logger.WriteLine("----- THE DRAG MODEL TEST ----- END -----")

    # endregion

    def MoonOrbitGeodeticPosition(self, hpop: "VehiclePropagatorHPOP"):
        geo: "OrbitStateGeodetic" = None
        coordSet = []
        coordSet.append(COORDINATE_SYSTEM.FIXED_NO_LIBRATION)
        coordSet.append(COORDINATE_SYSTEM.FIXED_IAU2003)
        coordSet.append(COORDINATE_SYSTEM.PRINCIPAL_AXES403)
        coordSet.append(COORDINATE_SYSTEM.PRINCIPAL_AXES421)

        geo = OrbitStateGeodetic(hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.GEODETIC))
        supportedCSTypes = geo.supported_coordinate_system_types

        i: int = 0
        while i < len(supportedCSTypes):
            coordType: "COORDINATE_SYSTEM" = COORDINATE_SYSTEM(int(supportedCSTypes[i][0]))
            geo.coordinate_system_type = coordType
            hpop.initial_state.representation.assign(geo)
            hpop.propagate()

            geo = OrbitStateGeodetic(hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.GEODETIC))
            Assert.assertEqual(geo.coordinate_system_type, coordType)
            if coordType in coordSet:
                Assert.assertTrue(List.Remove(coordSet, coordType))

            i += 1

        sb = StringBuilder()
        cs: "COORDINATE_SYSTEM"
        for cs in coordSet:
            if sb.Length != 0:
                sb.Append(",")
            sb.Append(cs.name)

        # Make sure the centralbody-specific coordinate systems have been tested
        Assert.assertTrue(
            (len(coordSet) == 0), String.Format("Some coordinate systems remained untested: {0}", sb.ToString())
        )

    def MoonOrbitCartesianPosition(self, hpop: "VehiclePropagatorHPOP"):
        cart: "OrbitStateCartesian" = None
        coordSet = []
        coordSet.append(COORDINATE_SYSTEM.FIXED_NO_LIBRATION)
        coordSet.append(COORDINATE_SYSTEM.FIXED_IAU2003)
        coordSet.append(COORDINATE_SYSTEM.PRINCIPAL_AXES403)
        coordSet.append(COORDINATE_SYSTEM.PRINCIPAL_AXES421)
        cart = OrbitStateCartesian(hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN))

        supportedCSTypes = cart.supported_coordinate_system_types

        i: int = 0
        while i < len(supportedCSTypes):
            coordType: "COORDINATE_SYSTEM" = COORDINATE_SYSTEM(int(supportedCSTypes[i][0]))
            cart.coordinate_system_type = coordType
            hpop.initial_state.representation.assign(cart)
            hpop.propagate()

            cart = OrbitStateCartesian(hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN))
            Assert.assertEqual(cart.coordinate_system_type, coordType)
            if coordType in coordSet:
                Assert.assertTrue(List.Remove(coordSet, coordType))

            i += 1

        sb = StringBuilder()
        cs: "COORDINATE_SYSTEM"
        for cs in coordSet:
            if sb.Length != 0:
                sb.Append(",")
            sb.Append(cs.name)

        # Make sure the centralbody-specific coordinate systems have been tested
        Assert.assertTrue(
            (len(coordSet) == 0), String.Format("Some coordinate systems remained untested: {0}", sb.ToString())
        )

    def MoonOrbitSphericalPosition(self, hpop: "VehiclePropagatorHPOP"):
        sph: "OrbitStateSpherical" = None
        coordSet = []
        coordSet.append(COORDINATE_SYSTEM.FIXED_NO_LIBRATION)
        coordSet.append(COORDINATE_SYSTEM.FIXED_IAU2003)
        coordSet.append(COORDINATE_SYSTEM.PRINCIPAL_AXES403)
        coordSet.append(COORDINATE_SYSTEM.PRINCIPAL_AXES421)
        sph = OrbitStateSpherical(hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.SPHERICAL))

        supportedCSTypes = sph.supported_coordinate_system_types

        i: int = 0
        while i < len(supportedCSTypes):
            coordType: "COORDINATE_SYSTEM" = COORDINATE_SYSTEM(int(supportedCSTypes[i][0]))
            sph.coordinate_system_type = coordType
            hpop.initial_state.representation.assign(sph)
            hpop.propagate()

            sph = OrbitStateSpherical(hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.SPHERICAL))
            Assert.assertEqual(sph.coordinate_system_type, coordType)
            if coordType in coordSet:
                Assert.assertTrue(List.Remove(coordSet, coordType))

            i += 1

        sb = StringBuilder()
        cs: "COORDINATE_SYSTEM"
        for cs in coordSet:
            if sb.Length != 0:
                sb.Append(",")
            sb.Append(cs.name)

        # Make sure the centralbody-specific coordinate systems have been tested
        Assert.assertTrue(
            (len(coordSet) == 0), String.Format("Some coordinate systems remained untested: {0}", sb.ToString())
        )

    # region BasicMoonOrbit
    @category("Basic Tests")
    @category("OrbitState Test")
    def test_BasicMoonOrbit(self):
        TestBase.logger.WriteLine("----- THE BASIC MOON ORBIT TEST ----- START -----")
        # Create a temp satellite
        sat: "Satellite" = Satellite(
            TestBase.Application.current_scenario.children.new_on_central_body(
                STK_OBJECT_TYPE.SATELLITE, "MoonSatellite", "Moon"
            )
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop: "VehiclePropagatorHPOP" = VehiclePropagatorHPOP(sat.propagator)
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN)
        )
        supportedCoordTypes = cart.supported_coordinate_system_types

        i: int = 0
        while i < len(supportedCoordTypes):
            TestBase.logger.WriteLine7(
                "Coordinate System Name: {0}, value: {1}", supportedCoordTypes[i][0], supportedCoordTypes[i][1]
            )

            cart.coordinate_system_type = COORDINATE_SYSTEM(int(supportedCoordTypes[i][0]))

            i += 1

        cart.coordinate_system_type = COORDINATE_SYSTEM.FIXED_NO_LIBRATION
        cart.x_position = -2008.7
        cart.y_position = -2820.13
        cart.z_position = 293.62
        cart.x_velocity = 0.662564
        cart.y_velocity = -0.378015
        cart.z_velocity = 0.901981
        hpop.initial_state.representation.assign(cart)
        hpop.force_model.central_body_gravity.file = (
            r"STKData\CentralBodies\Moon\GLGM2.grv"  # for Moon-centered vehicles
        )
        hpop.force_model.central_body_gravity.max_degree = 48
        hpop.force_model.central_body_gravity.max_order = 48
        hpop.force_model.central_body_gravity.solid_tide_type = SOLID_TIDE.PERMANENT

        # See: 47217 UseOceanTides is grayed out in GUI but writtable via the Object Model
        # UseOceanTides can only be set(not-grayed out) if the central body is earth.
        try:
            hpop.force_model.central_body_gravity.use_ocean_tides = False
            Assert.fail("Should not allow setting UseOceanTides for non-Earth central bodies")

        except Exception as ex:
            msg: str = str(ex)
            Assert.assertEqual("Central Body was not Earth.", msg)
            TestBase.logger.WriteLine5("EXPECTED EXCEPTION: {0}", msg)

        hpop.propagate()

        self.MoonOrbitCartesianPosition(hpop)
        self.MoonOrbitGeodeticPosition(hpop)
        self.MoonOrbitSphericalPosition(hpop)

        # Delete the temp satellite
        TestBase.Application.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, (IStkObject(sat)).instance_name
        )
        TestBase.logger.WriteLine("----- THE BASIC MOON ORBIT TEST ----- END -----")

    # endregion

    # region X42637
    def test_CentralBodyCoordinateSystems(self):
        cart: "OrbitStateCartesian" = None
        oMoonSat: "IStkObject" = TestBase.Application.current_scenario.children.new_on_central_body(
            STK_OBJECT_TYPE.SATELLITE, "SatelliteOnMoon", "Moon"
        )
        oEarthSat: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "SatelliteOnEarth"
        )

        moonSat: "Satellite" = clr.CastAs(oMoonSat, Satellite)
        earthSat: "Satellite" = clr.CastAs(oEarthSat, Satellite)

        moonSatPropagator: "VehiclePropagatorTwoBody" = clr.CastAs(moonSat.propagator, VehiclePropagatorTwoBody)
        earthSatPropagator: "VehiclePropagatorTwoBody" = clr.CastAs(earthSat.propagator, VehiclePropagatorTwoBody)

        moonSatPropagator.propagate()
        earthSatPropagator.propagate()

        cart = OrbitStateCartesian(
            moonSatPropagator.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN)
        )

        # Print the coordinate systems for the moon satellite
        TestBase.logger.WriteLine("Coordinate systems for the Moon satellite")
        moonCoordTypes = cart.supported_coordinate_system_types

        i: int = 0
        while i < len(moonCoordTypes):
            TestBase.logger.WriteLine7(
                "Coordinate System Name: {0}, value: {1}", moonCoordTypes[i][0], moonCoordTypes[i][1]
            )

            cart.coordinate_system_type = COORDINATE_SYSTEM(int(moonCoordTypes[i][0]))

            i += 1

        cart = OrbitStateCartesian(
            earthSatPropagator.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN)
        )
        # Print the coordinate systems for the moon satellite
        TestBase.logger.WriteLine("Coordinate systems for the Moon satellite")
        earthCoordTypes = cart.supported_coordinate_system_types

        i: int = 0
        while i < len(earthCoordTypes):
            TestBase.logger.WriteLine7(
                "Coordinate System Name: {0}, value: {1}", earthCoordTypes[i][0], earthCoordTypes[i][1]
            )

            cart.coordinate_system_type = COORDINATE_SYSTEM(int(earthCoordTypes[i][0]))

            i += 1

        # Moon and Earth support 14 and 12 coordinate systems respectively
        Assert.assertNotEqual(Array.Length(moonCoordTypes), Array.Length(earthCoordTypes))

    # endregion

    # region PropagationFrame
    def test_PropagationFrame(self):
        j2: "VehiclePropagatorJ2Perturbation" = None
        j4: "VehiclePropagatorJ4Perturbation" = None
        twobody: "VehiclePropagatorTwoBody" = None
        cart: "OrbitStateCartesian" = None

        # ----------------------------------------------------
        # Verify propagation frame with j2 propagator
        # ----------------------------------------------------
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        Assert.assertEqual(EarlyBoundTests.AG_SAT.propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2 = VehiclePropagatorJ2Perturbation(EarlyBoundTests.AG_SAT.propagator)

        j2.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_INERTIAL
        j2.propagate()
        Assert.assertEqual(j2.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_INERTIAL)

        j2.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_DATE
        j2.propagate()
        Assert.assertEqual(j2.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_DATE)

        j2.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_EPOCH
        j2.propagate()
        Assert.assertEqual(
            j2.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_EPOCH
        )

        # Epoch was deprecated
        # object epoch = j2.InitialState.Epoch;
        # j2.InitialState.Epoch = epoch;
        # Assert.AreEqual(epoch, j2.InitialState.Epoch);
        cart = OrbitStateCartesian(j2.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN))
        epoch: typing.Any = cart.epoch
        (cart).epoch = epoch
        Assert.assertEqual(epoch, cart.epoch)
        j2.initial_state.representation.assign(cart)

        ellipseOptions: "VEHICLE_ELLIPSE_OPTIONS" = j2.initial_state.ellipse_options
        j2.initial_state.ellipse_options = ellipseOptions
        Assert.assertEqual(ellipseOptions, j2.initial_state.ellipse_options)

        propagationFrames = j2.initial_state.supported_propagation_frames

        # ----------------------------------------------------
        # Verify propagation frame with j4 propagator
        # ----------------------------------------------------
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        Assert.assertEqual(EarlyBoundTests.AG_SAT.propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        j4 = VehiclePropagatorJ4Perturbation(EarlyBoundTests.AG_SAT.propagator)

        j4.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_INERTIAL
        j4.propagate()
        Assert.assertEqual(j4.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_INERTIAL)

        j4.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_DATE
        j4.propagate()
        Assert.assertEqual(j4.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_DATE)

        j4.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_EPOCH
        j4.propagate()
        Assert.assertEqual(
            j4.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_EPOCH
        )

        # Epoch was deprecated
        # epoch = j4.InitialState.Epoch;
        # j4.InitialState.Epoch = epoch;
        # Assert.AreEqual(epoch, j4.InitialState.Epoch);
        cart = OrbitStateCartesian(j4.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN))
        epoch = cart.epoch
        (cart).epoch = epoch
        Assert.assertEqual(epoch, cart.epoch)
        j4.initial_state.representation.assign(cart)

        ellipseOptions = j4.initial_state.ellipse_options
        j4.initial_state.ellipse_options = ellipseOptions
        Assert.assertEqual(ellipseOptions, j4.initial_state.ellipse_options)

        propagationFrames = j4.initial_state.supported_propagation_frames

        # ----------------------------------------------------
        # Verify propagation frame with TwoBody propagator
        # ----------------------------------------------------
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        Assert.assertEqual(EarlyBoundTests.AG_SAT.propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twobody = VehiclePropagatorTwoBody(EarlyBoundTests.AG_SAT.propagator)

        twobody.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_INERTIAL
        twobody.propagate()
        Assert.assertEqual(
            twobody.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_INERTIAL
        )

        twobody.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_DATE
        twobody.propagate()
        Assert.assertEqual(
            twobody.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_DATE
        )

        twobody.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_EPOCH
        twobody.propagate()
        Assert.assertEqual(
            twobody.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_TRUE_OF_EPOCH
        )

        # Epoch was deprecated
        # epoch = twobody.InitialState.Epoch;
        # twobody.InitialState.Epoch = epoch;
        # Assert.AreEqual(epoch, twobody.InitialState.Epoch);
        cart = OrbitStateCartesian(twobody.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN))
        epoch = cart.epoch
        (cart).epoch = epoch
        Assert.assertEqual(epoch, cart.epoch)
        twobody.initial_state.representation.assign(cart)

        propagationFrames = twobody.initial_state.supported_propagation_frames

        # ------------------------------------------------------------------------------------------
        # Verify propagation frame with HPOP propagator (See 76432: read-only, and value = Unknown)
        # ------------------------------------------------------------------------------------------
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        Assert.assertEqual(EarlyBoundTests.AG_SAT.propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop: "VehiclePropagatorHPOP" = VehiclePropagatorHPOP(EarlyBoundTests.AG_SAT.propagator)
        Assert.assertEqual(hpop.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_UNKNOWN)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            hpop.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_INERTIAL

        # ------------------------------------------------------------------------------------------
        # Verify propagation frame with LOP propagator (See 76432: read-only, and value = Unknown)
        # ------------------------------------------------------------------------------------------
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_LOP)
        Assert.assertEqual(EarlyBoundTests.AG_SAT.propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_LOP)
        lop: "VehiclePropagatorLOP" = VehiclePropagatorLOP(EarlyBoundTests.AG_SAT.propagator)
        Assert.assertEqual(lop.initial_state.propagation_frame, VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_UNKNOWN)
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            lop.initial_state.propagation_frame = VEHICLE_PROPAGATION_FRAME.PROPAGATION_FRAME_INERTIAL

    # endregion

    # region Lighting
    def test_Lighting(self):
        EarlyBoundTests.AG_SAT.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_SAT.use_terrain_in_lighting_computations)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.AG_SAT.lighting_max_step = 0

        EarlyBoundTests.AG_SAT.use_terrain_in_lighting_computations = True
        Assert.assertTrue(EarlyBoundTests.AG_SAT.use_terrain_in_lighting_computations)

        # deprecated
        EarlyBoundTests.AG_SAT.lighting_max_step = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_SAT.lighting_max_step)
        EarlyBoundTests.AG_SAT.lighting_max_step = 31557600
        Assert.assertEqual(31557600, EarlyBoundTests.AG_SAT.lighting_max_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SAT.lighting_max_step = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SAT.lighting_max_step = 31557601

        EarlyBoundTests.AG_SAT.lighting_max_step_terrain = 10
        Assert.assertEqual(10, EarlyBoundTests.AG_SAT.lighting_max_step_terrain)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SAT.lighting_max_step_terrain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SAT.lighting_max_step_terrain = 31557601

        EarlyBoundTests.AG_SAT.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_SAT.use_terrain_in_lighting_computations)
        EarlyBoundTests.AG_SAT.lighting_max_step_central_body_shape = 3600
        Assert.assertEqual(3600, EarlyBoundTests.AG_SAT.lighting_max_step_central_body_shape)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SAT.lighting_max_step_central_body_shape = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_SAT.lighting_max_step_central_body_shape = 31557601

        Assert.assertEqual(
            10, EarlyBoundTests.AG_SAT.lighting_max_step_terrain
        )  # still available for get, though not settable
        EarlyBoundTests.AG_SAT.use_terrain_in_lighting_computations = True
        Assert.assertEqual(
            3600, EarlyBoundTests.AG_SAT.lighting_max_step_central_body_shape
        )  # still available for get, though not settable

        helper = EclipsingBodiesHelper()
        helper.Run(EarlyBoundTests.AG_SAT.eclipse_bodies)

    # endregion

    # region Sgp4RevNumber
    def test_Sgp4RevNumber(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("test")
        sat1: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "SGP4Sat"), Satellite
        )
        sat1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
        sgp4: "VehiclePropagatorSGP4" = clr.CastAs(sat1.propagator, VehiclePropagatorSGP4)
        sgp4.segments.load_method_type = LOAD_METHOD_TYPE.FILE_LOAD
        fileLoad: "VehicleSGP4LoadFile" = clr.CastAs(sgp4.segments.load_method, VehicleSGP4LoadFile)
        fileLoad.file = TestBase.GetScenarioFile("stkAllTLE.tle")
        sscNums = fileLoad.get_ssc_nums_from_file()
        segments = fileLoad.get_segs_from_file(str(sscNums[0]))
        fileLoad.add_segs_from_file(segments)
        sgp4.propagate()
        revNumber: int = sgp4.segments[0].rev_number
        TestBase.Application.save_scenario_as(Path.Combine(TestBase.TemporaryDirectory, "MyTest.sc"))
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(Path.Combine(TestBase.TemporaryDirectory, "MyTest.sc"))
        sat1 = clr.CastAs(TestBase.Application.current_scenario.children["SGP4Sat"], Satellite)
        sgp4 = clr.CastAs(sat1.propagator, VehiclePropagatorSGP4)
        Assert.assertEqual(revNumber, sgp4.segments[0].rev_number)
        TestBase.LoadTestScenario(Path.Combine("SatelliteTests", "SatelliteTests.sc"))
        EarlyBoundTests.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

    # endregion

    # region HPOPForceModelSolidTides
    @category("Basic Tests")
    def test_HPOPForceModelSolidTides(self):
        TestBase.logger.WriteLine("----- THE HPOP FORCEMODEL SOLIDTIDES TEST ----- BEGIN -----")
        rnd = Random(10000)
        instName: str = String.Format("Satellite_{0}", rnd.Next(1000))
        TestBase.logger.WriteLine5("\tThe new Satellite name is: {0}", instName)
        oSatellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new_on_central_body(
                STK_OBJECT_TYPE.SATELLITE, instName, "Moon"
            ),
            Satellite,
        )
        Assert.assertIsNotNone(oSatellite)
        try:
            # SetPropagatorType (PROPAGATOR_HPOP)
            TestBase.logger.WriteLine6("\tThe current PropagatorType is: {0}", oSatellite.propagator_type)
            oSatellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
            TestBase.logger.WriteLine6("\tThe new PropagatorType is: {0}", oSatellite.propagator_type)
            Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP, oSatellite.propagator_type)
            # Propagator
            oHPOP: "VehiclePropagatorHPOP" = VehiclePropagatorHPOP(oSatellite.propagator)
            Assert.assertIsNotNone(oHPOP)

            # ---------------------------------------------------------
            # ENG31390: Verify the gravity field and the solid tides.
            # Some gravity fields cannot be used when the solid
            # tides are on.
            # ---------------------------------------------------------

            # SolidTideType
            oHPOP.force_model.central_body_gravity.solid_tide_type = SOLID_TIDE.NONE
            Assert.assertEqual(SOLID_TIDE.NONE, oHPOP.force_model.central_body_gravity.solid_tide_type)
            oHPOP.force_model.central_body_gravity.solid_tide_type = SOLID_TIDE.PERMANENT
            Assert.assertEqual(SOLID_TIDE.PERMANENT, oHPOP.force_model.central_body_gravity.solid_tide_type)
            oHPOP.force_model.central_body_gravity.solid_tide_type = SOLID_TIDE.FULL
            Assert.assertEqual(SOLID_TIDE.FULL, oHPOP.force_model.central_body_gravity.solid_tide_type)
            # File
            TestBase.logger.WriteLine5("\tThe current File is: {0}", oHPOP.force_model.central_body_gravity.file)
            oHPOP.force_model.central_body_gravity.file = "STKData\\CentralBodies\\Moon\\LP100K.grv"
            TestBase.logger.WriteLine5("\tThe new File is: {0}", oHPOP.force_model.central_body_gravity.file)
            try:
                oHPOP.propagate()

            except Exception as ex:
                if not str(ex).startswith("Solid tides are not available for this gravity file"):
                    raise ex

                TestBase.logger.WriteLine7("\t\tExpected exception: {0}", str(ex), "Exception message mismatch")

            oHPOP.force_model.central_body_gravity.file = "STKData\\CentralBodies\\Moon\\LP150Q.grv"
            TestBase.logger.WriteLine5("\tThe new File is: {0}", oHPOP.force_model.central_body_gravity.file)
            oHPOP.propagate()  # shall succeed!

        finally:
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, instName)

        oSatellite = None
        TestBase.logger.WriteLine("----- THE HPOP FORCEMODEL SOLIDTIDES TEST ----- END -----")

    # endregion

    # region CoordinateSystemThruConnect
    @category("Basic Tests")
    @category("OrbitState Test")
    def test_CoordinateSystemThruConnect(self):
        command: str = String.Format(
            'SetState */Satellite/{0} Cartesian J2Perturbation "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 60 MeanOfEpoch "1 Jul 1999 00:00:00.00" -5465000.513055 4630000.194365 0.0 712.713627 841.292034 7377.687805 "3 Jul 1999 00:00:00.00"',
            (IStkObject(EarlyBoundTests.AG_SAT)).instance_name,
        )
        res: "ExecCmdResult" = TestBase.Application.execute_command(command)
        del res

        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION, EarlyBoundTests.AG_SAT.propagator_type)
        prop: "VehiclePropagatorJ2Perturbation" = clr.CastAs(
            EarlyBoundTests.AG_SAT.propagator, VehiclePropagatorJ2Perturbation
        )

        keplerian: "OrbitStateClassical" = clr.CastAs(
            prop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL), OrbitStateClassical
        )

        Assert.assertEqual(COORDINATE_SYSTEM.MEAN_OF_EPOCH, keplerian.coordinate_system_type)
        Assert.assertEqual("3 Jul 1999 00:00:00.000", keplerian.coordinate_system.coordinate_system_epoch.time_instant)

    # endregion

    # region SetAttributesType
    def SetAttributesType(self, eType: "VEHICLE_GRAPHICS_2D_ATTRIBUTES"):
        oGfx: "SatelliteGraphics" = EarlyBoundTests.AG_SAT.graphics
        Assert.assertIsNotNone(oGfx)

        arSupportedTypes = oGfx.attributes_supported_types
        TestBase.logger.WriteLine3("Supported Types array contains: {0} elements", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            TestBase.logger.WriteLine8(
                "The {0} supported element is: {1} ({2})",
                iIndex,
                arSupportedTypes[iIndex][1],
                VEHICLE_GRAPHICS_2D_ATTRIBUTES(int(arSupportedTypes[iIndex][0])),
            )

            iIndex += 1

        TestBase.logger.WriteLine6("The current Attributes type is: {0}", oGfx.attributes_type)
        if not oGfx.is_attributes_type_supported(eType):
            Assert.fail("The {0} type should be supported!", eType)

        oGfx.set_attributes_type(eType)
        TestBase.logger.WriteLine6("The new Attributes type is: {0}", oGfx.attributes_type)
        Assert.assertEqual(eType, oGfx.attributes_type)

    # endregion

    # region GfxAttributesBasic
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesBasic(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)

        oHelper = GfxAttributesOrbitHelper()
        oHelper.Run(VehicleGraphics2DAttributesOrbit(EarlyBoundTests.AG_SAT.graphics.attributes))
        EarlyBoundTests.AG_SAT.graphics.use_inst_name_label = False
        Assert.assertFalse(EarlyBoundTests.AG_SAT.graphics.use_inst_name_label)
        EarlyBoundTests.AG_SAT.graphics.label_name = "Tester"
        Assert.assertEqual("Tester", EarlyBoundTests.AG_SAT.graphics.label_name)

        EarlyBoundTests.AG_SAT.graphics.is_object_graphics_visible = False
        Assert.assertFalse(EarlyBoundTests.AG_SAT.graphics.is_object_graphics_visible)
        EarlyBoundTests.AG_SAT.graphics.is_object_graphics_visible = True
        Assert.assertTrue(EarlyBoundTests.AG_SAT.graphics.is_object_graphics_visible)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- END -----")

    # endregion

    # region GfxAttributesAccess
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesAccess(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        EarlyBoundTests.InitHelper()

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS)

        oHelper = GfxAttributesAccessHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesAccess(EarlyBoundTests.AG_SAT.graphics.attributes),
            GfxAttributesType.eOrbit,
            TestBase.Application,
        )

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_SAT.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        Assert.assertEqual(0, intColl.count)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

    # endregion

    # region GfxAttributesCustom
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesCustom(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES CUSTOM TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM)

        # Custom Intervals
        oHelper = GfxAttributesCustomHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesCustom(EarlyBoundTests.AG_SAT.graphics.attributes), GfxAttributesType.eOrbit
        )

        custom: "VehicleGraphics2DAttributesCustom" = clr.CastAs(
            EarlyBoundTests.AG_SAT.graphics.attributes, VehicleGraphics2DAttributesCustom
        )
        custom.intervals.add("1 Jul 1999 00:00:00.000", "1 Jul 1999 00:01:00.000")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_SAT.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "VehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("1 Jul 1999 00:01:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES CUSTOM TEST ----- BEGIN -----")

    # endregion

    # region GfxAttributesTimeComponents
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesTimeComponents(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_TIME_COMPONENTS)

        oHelper = GfxAttributesTimeComponentsHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesTimeComponents(EarlyBoundTests.AG_SAT.graphics.attributes),
            GfxAttributesType.eOrbit,
            TestBase.Application,
        )

        gfxAttrTimeComp: "VehicleGraphics2DAttributesTimeComponents" = clr.CastAs(
            EarlyBoundTests.AG_SAT.graphics.attributes, VehicleGraphics2DAttributesTimeComponents
        )
        gfxAttrTimeComp.time_components.add("Scenario/Scenario1 AnalysisInterval EventInterval")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_SAT.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "VehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("2 Jul 1999 00:00:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

    # endregion

    # region GfxAttributesRealTime
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesRealTime(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- BEGIN -----")
        if EarlyBoundTests.AG_SAT.propagator_type != VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME:
            bCaught: bool = False
            try:
                bCaught = False
                self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)

            except Exception as e:
                bCaught = True
                TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The SetAttributesType should not allow to set ATTRIBUTES_REALTIME value!")

        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        (clr.CastAs(EarlyBoundTests.AG_SAT.propagator, VehiclePropagatorRealtime)).propagate()
        self.SetAttributesType(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)

        oHelper = GfxAttributesRealTimeHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesRealtime(EarlyBoundTests.AG_SAT.graphics.attributes), GfxAttributesType.eOrbit
        )

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- END -----")

    # endregion

    # region GfxTimeEvents
    @category("Graphics Tests")
    def test_GfxTimeEvents(self):
        oHelper = GfxTimeEventsHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT, EarlyBoundTests.AG_SAT.graphics.time_events)

    # endregion

    # region GfxLighting
    @category("Graphics Tests")
    def test_GfxLighting(self):
        oHelper = GfxLightingHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics.lighting)

    # endregion

    # region GfxSwath
    @category("Graphics Tests")
    def test_GfxSwath(self):
        # create non geostationary satellite
        oSatellite: "Satellite" = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Voyager")
        )
        Assert.assertIsNotNone(oSatellite)

        # test swath
        oHelper = GfxSwathHelper(self.Units)
        oHelper.Run(oSatellite.graphics.swath)

        # remove it from scenario
        iCount: int = TestBase.Application.current_scenario.children.count
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "Voyager")
        Assert.assertEqual((iCount - 1), TestBase.Application.current_scenario.children.count)

    # endregion

    # region GfxGroundEllipses
    @category("Graphics Tests")
    def test_GfxGroundEllipses(self):
        oBGEHelper = BasicGroundEllipsesHelper(self.Units)
        oBGEHelper.Run(EarlyBoundTests.AG_SAT.ground_ellipses, False)

        oGGEHelper = GfxGroundEllipsesHelper()
        oGGEHelper.Run(EarlyBoundTests.AG_SAT.graphics.ground_ellipses)

    # endregion

    # region GfxPass
    @category("Graphics Tests")
    @category("Trail/Lead (2D)")
    def test_GfxPass(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS PASS TEST ----- BEGIN -----")
        oPasses: "VehicleGraphics2DPasses" = EarlyBoundTests.AG_SAT.graphics.passes
        Assert.assertIsNotNone(oPasses)
        # VisibleSides
        TestBase.logger.WriteLine6("The current VisibleSides type is: {0}", oPasses.visible_sides)
        oPasses.visible_sides = VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_NONE
        TestBase.logger.WriteLine6("The new VisibleSides type is: {0}", oPasses.visible_sides)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_NONE, oPasses.visible_sides)
        oPasses.visible_sides = VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_ASCENDING
        TestBase.logger.WriteLine6("The new VisibleSides type is: {0}", oPasses.visible_sides)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_ASCENDING, oPasses.visible_sides)
        oPasses.visible_sides = VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_BOTH
        TestBase.logger.WriteLine6("The new VisibleSides type is: {0}", oPasses.visible_sides)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_BOTH, oPasses.visible_sides)
        oPasses.visible_sides = VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_DESCENDING
        TestBase.logger.WriteLine6("The new VisibleSides type is: {0}", oPasses.visible_sides)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_VISIBLE_SIDES.VISIBLE_SIDES_DESCENDING, oPasses.visible_sides)
        # IsPassLabelsVisible
        TestBase.logger.WriteLine4("The current IsPassLabelsVisible flag is: {0}", oPasses.is_pass_labels_visible)
        oPasses.is_pass_labels_visible = True
        TestBase.logger.WriteLine4("The new IsPassLabelsVisible flag is: {0}", oPasses.is_pass_labels_visible)
        Assert.assertEqual(True, oPasses.is_pass_labels_visible)
        # IsPathLabelsVisible
        TestBase.logger.WriteLine4("The current IsPathLabelsVisible flag is: {0}", oPasses.is_path_labels_visible)
        oPasses.is_path_labels_visible = True
        TestBase.logger.WriteLine4("The new IsPathLabelsVisible flag is: {0}", oPasses.is_path_labels_visible)
        Assert.assertEqual(True, oPasses.is_path_labels_visible)
        # PassSupportedTypes
        arSupportedTypes = oPasses.pass_supported_types
        TestBase.logger.WriteLine3("The Pass supported {0} types.", len(arSupportedTypes))

        i: int = 0
        while i < len(arSupportedTypes):
            TestBase.logger.WriteLine8(
                "\tPass type {0}: {1} ({2})",
                i,
                arSupportedTypes[i][1],
                VEHICLE_GRAPHICS_2D_PASS(int(arSupportedTypes[i][0])),
            )

            i += 1

        if not oPasses.is_pass_type_supported(VEHICLE_GRAPHICS_2D_PASS.PASS_SHOW_ALL):
            Assert.fail("The PASS_SHOW_ALL type should be supported!")

        if not oPasses.is_pass_type_supported(VEHICLE_GRAPHICS_2D_PASS.PASS_SHOW_PASSES):
            Assert.fail("The PASS_SHOW_PASSES type should be supported!")

        # PassType
        TestBase.logger.WriteLine6("The current PassType is: {0}", oPasses.pass_type)
        # SetPassType
        oPasses.set_pass_type(VEHICLE_GRAPHICS_2D_PASS.PASS_SHOW_ALL)
        TestBase.logger.WriteLine6("The new PassType is: {0}", oPasses.pass_type)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_PASS.PASS_SHOW_ALL, oPasses.pass_type)
        Assert.assertIsNone(oPasses.pass_method)
        # SetPassType
        oPasses.set_pass_type(VEHICLE_GRAPHICS_2D_PASS.PASS_SHOW_PASSES)
        TestBase.logger.WriteLine6("The new PassType is: {0}", oPasses.pass_type)
        Assert.assertEqual(VEHICLE_GRAPHICS_2D_PASS.PASS_SHOW_PASSES, oPasses.pass_type)
        # Pass
        oShow: "VehicleGraphics2DPassShowPasses" = VehicleGraphics2DPassShowPasses(oPasses.pass_method)
        Assert.assertIsNotNone(oShow)
        # FirstPass
        TestBase.logger.WriteLine3("The current FirstPass is: {0}", oShow.first_pass)
        oShow.first_pass = 5
        TestBase.logger.WriteLine3("The new FirstPass is: {0}", oShow.first_pass)
        Assert.assertEqual(5, oShow.first_pass)
        bCaught: bool = False
        try:
            bCaught = False
            oShow.first_pass = -1

        except Exception as e:
            bCaught = True
            TestBase.logger.Write2("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        # LastPass
        TestBase.logger.WriteLine3("The current LastPass is: {0}", oShow.last_pass)
        oShow.last_pass = 10
        TestBase.logger.WriteLine3("The new LastPass is: {0}", oShow.last_pass)
        Assert.assertEqual(10, oShow.last_pass)
        try:
            bCaught = False
            oShow.last_pass = -1

        except Exception as e:
            bCaught = True
            TestBase.logger.Write2("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set value out of range!")

        try:
            bCaught = False
            oShow.first_pass = 100

        except Exception as e:
            bCaught = True
            TestBase.logger.Write2("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set FirstPass more then LastPass!")

        try:
            bCaught = False
            oShow.last_pass = 1

        except Exception as e:
            bCaught = True
            TestBase.logger.Write2("\tExpected exception: {0}", str(e))

        if not bCaught:
            Assert.fail("Cannot set LastPass less then FirstPass!")

        # GroundTrack
        TestBase.logger.Write("GroundTrack - ")
        oHelper = GfxLeadTrailDataHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics.pass_data.ground_track)

        # Orbit
        TestBase.logger.Write("Orbit - ")
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics.pass_data.orbit)

        TestBase.logger.WriteLine("----- THE GRAPHICS PASS TEST ----- END -----")

    # endregion

    # region GfxGroundTrackCentralBodyDisplay
    @category("Graphics Tests")
    def test_GfxGroundTrackCentralBodyDisplay(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS GROUNDTRACK CENTRALBODY DISPLAY TEST ----- BEGIN -----")
        oBodies: "VehicleCentralBodies" = EarlyBoundTests.AG_SAT.graphics.ground_track_central_body_display
        Assert.assertIsNotNone(oBodies)
        # AvailableCentralBodies
        arAvailableBodies = oBodies.available_central_bodies
        TestBase.logger.WriteLine3(
            "\tThe Available CentralBodies array contains: {0} elements", Array.Length(arAvailableBodies)
        )

        iIndex: int = 0
        while iIndex < Array.Length(arAvailableBodies):
            strBody: str = str(arAvailableBodies[iIndex])
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: CentralBody = {1}, IsAssigned = {2}",
                iIndex,
                strBody,
                oBodies.is_central_body_assigned(strBody),
            )
            if not oBodies.is_central_body_assigned(strBody):
                # AssignCentralBody
                oBodies.assign_central_body(strBody)
                if oBodies.is_central_body_assigned(strBody):
                    TestBase.logger.WriteLine5("\t\t\tThe {0} CentralBody was assigned.", strBody)

                else:
                    Assert.fail("The {0} CentralBody should be assigned!", strBody)

            else:
                TestBase.logger.WriteLine("\t\t\tThe {0} CentralBody is already assigned.")

            iIndex += 1

        # AssignedCentralBodies
        arAssignedBodies = oBodies.assigned_central_bodies
        TestBase.logger.WriteLine3(
            "\tThe Assigned CentralBodies array contains: {0} elements", Array.Length(arAssignedBodies)
        )

        iIndex: int = 0
        while iIndex < Array.Length(arAssignedBodies):
            strBody: str = str(arAssignedBodies[iIndex])
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: CentralBody = {1}, IsAssigned = {2}",
                iIndex,
                strBody,
                oBodies.is_central_body_assigned(strBody),
            )

            iIndex += 1

        # the length should be the same
        Assert.assertEqual(Array.Length(arAvailableBodies), Array.Length(arAssignedBodies))
        # RemoveCentralBody
        iLength: int = Array.Length(arAssignedBodies)
        TestBase.logger.WriteLine3(
            "\tBefore RemoveCentralBody the Assigned CentralBodies array contains: {0} elements", iLength
        )
        oBodies.remove_central_body(str(arAssignedBodies[0]))
        arAssignedBodies = oBodies.assigned_central_bodies
        TestBase.logger.WriteLine3(
            "\tAfter RemoveCentralBody the Assigned CentralBodies array contains: {0} elements",
            Array.Length(arAssignedBodies),
        )
        Assert.assertEqual((iLength - 1), Array.Length(arAssignedBodies))
        # IsCentralBodyAssigned
        Assert.assertFalse(oBodies.is_central_body_assigned("Invalid CentralBody"))
        # AssignCentralBody
        with pytest.raises(Exception):
            oBodies.assign_central_body("Invalid CentralBody")
        # RemoveCentralBody
        with pytest.raises(Exception):
            oBodies.remove_central_body("Invalid CentralBody")
        # RemoveAll
        TestBase.logger.WriteLine3(
            "\tBefore RemoveAll the Assigned CentralBodies array contains: {0} elements", Array.Length(arAssignedBodies)
        )
        oBodies.remove_all()
        arAssignedBodies = oBodies.assigned_central_bodies
        TestBase.logger.WriteLine3(
            "\tAfter RemoveAll the Assigned CentralBodies array contains: {0} elements", Array.Length(arAssignedBodies)
        )
        Assert.assertEqual(0, Array.Length(arAssignedBodies))
        TestBase.logger.WriteLine("----- THE GRAPHICS GROUNDTRACK CENTRALBODY DISPLAY TEST ----- END -----")

    # endregion

    # region GfxResolution
    @category("Graphics Tests")
    def test_GfxResolution(self):
        oHelper = GfxPassResolutionHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics.resolution)

    # endregion

    # region GfxLabelNotes
    @category("Graphics Tests")
    def test_GfxLabelNotes(self):
        oHelper = GfxLabelNoteHelper(TestBase.Application.unit_preferences)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics.label_notes)

    # endregion

    # region GfxElevationContours
    @category("Graphics Tests")
    def test_GfxElevationContours(self):
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        Assert.assertEqual(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP, EarlyBoundTests.AG_SAT.propagator_type)

        hpop: "VehiclePropagatorHPOP" = VehiclePropagatorHPOP(EarlyBoundTests.AG_SAT.propagator)
        Assert.assertIsNotNone(hpop)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 1999 00:00:00.000", "2 Jul 1999 00:00:00.000")
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 1999 00:00:00.000";
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN)
        )
        (cart).epoch = "1 Jul 1999 00:00:00.000"
        hpop.initial_state.representation.assign(cart)
        hpop.propagate()

        scen: "Scenario" = Scenario(TestBase.Application.current_scenario)
        scen.animation.start_time = "1 Jul 1999 00:00:00.000"

        oHelper = GfxElevationContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics.elev_contours)

    # endregion

    # region GfxSAAContours
    @category("Graphics Tests")
    @category("Excluded From RegFree")
    @category("SEET")
    def test_GfxSAAContours(self):
        oHelper = GfxSAAContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics.saa)

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics.range_contours)

    # endregion

    # region VOCovariance
    @category("VO Tests")
    def test_VOCovariance(self):
        oHelper = VOCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.covariance)

    # endregion

    # region VOVelocityCovariance
    @category("VO Tests")
    def test_VOVelocityCovariance(self):
        oHelper = VOVelocityCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.velocity_covariance)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.range_contours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.offsets)

    # endregion

    # region VOPass
    @category("VO Tests")
    @category("Trail/Lead (3D)")
    def test_VOPass(self):
        oHelper = VOPassHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.pass_method)

    # endregion

    # region VOElevationContours
    @category("VO Tests")
    def test_VOElevationContours(self):
        oHelper = VOElevationContoursHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.elev_contours)

    # endregion

    # region VOSAAContours
    @category("SEET")
    @category("VO Tests")
    @category("Excluded From RegFree")
    def test_VOSAAContours(self):
        oHelper = VOSAAContoursHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.saa)

    # endregion

    # region VOCovariancePointingContour
    @category("VO Tests")
    def test_VOCovariancePointingContour(self):
        oHelper = VOCovariancePointingContourHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.covariance_pointing_contour)

    # endregion

    # region VODropLines
    @category("VO Tests")
    def test_VODropLines(self):
        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- BEGIN -----")

        oDropLines: "VehicleGraphics3DOrbitDropLines" = EarlyBoundTests.AG_SAT.graphics_3d.drop_lines
        Assert.assertIsNotNone(oDropLines)

        # Orbit test
        oPathHelper = VODropLinePathItemCollectionHelper()
        oPathHelper.Run(oDropLines.orbit)

        # Position test
        oPosHelper = VODropLinePosItemCollectionHelper()
        oPosHelper.Run(oDropLines.position)

        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- END -----")

    # endregion

    # region VOProximity
    @category("VO Tests")
    def test_VOProximity(self):
        oHelper = VOOrbitProximityHelper(clr.CastAs(TestBase.Application, StkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.proximity)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        # set VO.Model type to FILE
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_SAT.graphics_3d.model
        TestBase.logger.WriteLine6("The current ModelType is: {0}", oModel.model_type)
        oModel.model_type = MODEL_TYPE.FILE
        TestBase.logger.WriteLine6("The new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(MODEL_TYPE.FILE, oModel.model_type)
        # set new ModelFile.Filename
        oModelFile: "Graphics3DModelFile" = Graphics3DModelFile(oModel.model_data)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\tThe new Filename is: {0}", oModelFile.filename)
        # test ModelPointing
        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.model_pointing)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VOSatelliteModelHelper(clr.CastAs(TestBase.Application, StkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.model)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.model.ground_marker, True)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.model.orbit_marker, True)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.vector, False)
        sat: "Satellite" = clr.CastAs(EarlyBoundTests.AG_SAT, Satellite)

        origCount: int = sat.graphics_3d.vector.reference_crdns.count
        sat.graphics_3d.vector.reference_crdns.add(
            GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/Satellite1 Earth(True) Vector"
        )
        sat.graphics_3d.vector.reference_crdns.add(
            GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/Satellite1 MagField(IGRF) Vector"
        )

        Assert.assertEqual((origCount + 2), sat.graphics_3d.vector.reference_crdns.count)

    # endregion

    @parameterized.expand(
        [
            ("Satellite/Satellite1 Bogus Vector", GEOMETRIC_ELEM_TYPE.VECTOR_ELEM),
            ("Satellite/Satellite1 Bogus", GEOMETRIC_ELEM_TYPE.VECTOR_ELEM),
            ("Satellite/Satellite1", GEOMETRIC_ELEM_TYPE.VECTOR_ELEM),
            ("Satellite/Bogus", GEOMETRIC_ELEM_TYPE.VECTOR_ELEM),
            ("Satellite/Satellite1 Bogus Axes", GEOMETRIC_ELEM_TYPE.AXES_ELEM),
            ("Satellite/Satellite1 Bogus", GEOMETRIC_ELEM_TYPE.AXES_ELEM),
            ("Satellite/Satellite1", GEOMETRIC_ELEM_TYPE.AXES_ELEM),
            ("Satellite/Bogus", GEOMETRIC_ELEM_TYPE.AXES_ELEM),
            ("Satellite/Satellite1 Bogus Point", GEOMETRIC_ELEM_TYPE.POINT_ELEM),
            ("Satellite/Satellite1 Bogus", GEOMETRIC_ELEM_TYPE.POINT_ELEM),
            ("Satellite/Satellite1", GEOMETRIC_ELEM_TYPE.POINT_ELEM),
            ("Satellite/Bogus", GEOMETRIC_ELEM_TYPE.POINT_ELEM),
            ("Satellite/Satellite1 Bogus Plane", GEOMETRIC_ELEM_TYPE.PLANE_ELEM),
            ("Satellite/Satellite1 Bogus", GEOMETRIC_ELEM_TYPE.PLANE_ELEM),
            ("Satellite/Satellite1", GEOMETRIC_ELEM_TYPE.PLANE_ELEM),
            ("Satellite/Bogus", GEOMETRIC_ELEM_TYPE.PLANE_ELEM),
            ("Satellite/Satellite1 Bogus Angle", GEOMETRIC_ELEM_TYPE.ANGLE_ELEM),
            ("Satellite/Satellite1 Bogus", GEOMETRIC_ELEM_TYPE.ANGLE_ELEM),
            ("Satellite/Satellite1", GEOMETRIC_ELEM_TYPE.ANGLE_ELEM),
            ("Satellite/Bogus", GEOMETRIC_ELEM_TYPE.ANGLE_ELEM),
        ]
    )
    @category("VO Tests")
    @category("VO/Vector (3D)")
    def test_VOVectorsInvalidChoiceException(self, invalidElementName: str, elementType: "GEOMETRIC_ELEM_TYPE"):
        def code2():
            sat: "Satellite" = clr.CastAs(EarlyBoundTests.AG_SAT, Satellite)
            sat.graphics_3d.vector.reference_crdns.add(elementType, invalidElementName)

        ex = ExceptionAssert.Throws(code2)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    @parameterized.expand(
        [
            ("Satellite/Satellite1 Bogus Axes",),
            ("Satellite/Satellite1 Bogus",),
            ("Satellite/Satellite1 ",),
            ("Satellite/Bogus",),
        ]
    )
    @category("VO Tests")
    @category("VO/Vector (3D)")
    def test_VOVectorsInvalidVectorAxesException(self, invalidElementName: str):
        def code3():
            sat: "Satellite" = clr.CastAs(EarlyBoundTests.AG_SAT, Satellite)
            vector: "Graphics3DReferenceVectorGeometryToolVector" = clr.CastAs(
                sat.graphics_3d.vector.reference_crdns.add(
                    GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/Satellite1 North Vector"
                ),
                Graphics3DReferenceVectorGeometryToolVector,
            )
            Assert.assertIsNotNone(vector)
            try:
                vector.axes = invalidElementName

            finally:
                # Clean up so the test can be multiple times
                sat.graphics_3d.vector.reference_crdns.remove_by_name(
                    GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/Satellite1 North Vector"
                )

        ex = ExceptionAssert.Throws(code3)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    @parameterized.expand(
        [
            ("Satellite/Satellite1 Bogus Point",),
            ("Satellite/Satellite1 Bogus",),
            ("Satellite/Satellite1 ",),
            ("Satellite/Bogus",),
        ]
    )
    @category("VO Tests")
    @category("VO/Vector (3D)")
    def test_VOVectorsInvalidVectorPointException(self, invalidElementName: str):
        def code4():
            sat: "Satellite" = clr.CastAs(EarlyBoundTests.AG_SAT, Satellite)
            vector: "Graphics3DReferenceVectorGeometryToolVector" = clr.CastAs(
                sat.graphics_3d.vector.reference_crdns.add(
                    GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/Satellite1 North Vector"
                ),
                Graphics3DReferenceVectorGeometryToolVector,
            )
            Assert.assertIsNotNone(vector)
            vector.draw_at_point = True
            try:
                vector.point = invalidElementName

            finally:
                # Clean up so the test can be multiple times
                sat.graphics_3d.vector.reference_crdns.remove_by_name(
                    GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/Satellite1 North Vector"
                )

        ex = ExceptionAssert.Throws(code4)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    @parameterized.expand(
        [
            ("Satellite/Satellite1 Bogus Axes",),
            ("Satellite/Satellite1 Bogus",),
            ("Satellite/Satellite1 ",),
            ("Satellite/Bogus",),
        ]
    )
    @category("VO Tests")
    @category("VO/Vector (3D)")
    def test_VOVectorsInvalidAxesAxesException(self, invalidElementName: str):
        def code5():
            sat: "Satellite" = clr.CastAs(EarlyBoundTests.AG_SAT, Satellite)
            axes: "Graphics3DReferenceVectorGeometryToolAxes" = clr.CastAs(
                sat.graphics_3d.vector.reference_crdns.add(
                    GEOMETRIC_ELEM_TYPE.AXES_ELEM, "Satellite/Satellite1 ICRF Axes"
                ),
                Graphics3DReferenceVectorGeometryToolAxes,
            )
            Assert.assertIsNotNone(axes)
            try:
                axes.axes = invalidElementName

            finally:
                # Clean up so the test can be multiple times
                sat.graphics_3d.vector.reference_crdns.remove_by_name(
                    GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/Satellite1 ICRF Axes"
                )

        ex = ExceptionAssert.Throws(code5)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    @parameterized.expand(
        [
            ("Satellite/Satellite1 Bogus System",),
            ("Satellite/Satellite1 Bogus",),
            ("Satellite/Satellite1 ",),
            ("Satellite/Bogus",),
        ]
    )
    @category("VO Tests")
    @category("VO/Vector (3D)")
    def test_VOVectorsInvalidPointSystemException(self, invalidElementName: str):
        def code6():
            sat: "Satellite" = clr.CastAs(EarlyBoundTests.AG_SAT, Satellite)
            point: "Graphics3DReferenceVectorGeometryToolPoint" = clr.CastAs(
                sat.graphics_3d.vector.reference_crdns.add(
                    GEOMETRIC_ELEM_TYPE.AXES_ELEM, "Satellite/Satellite1 L1 Point"
                ),
                Graphics3DReferenceVectorGeometryToolPoint,
            )
            Assert.assertIsNotNone(point)
            try:
                point.system = invalidElementName

            finally:
                # Clean up so the test can be multiple times
                sat.graphics_3d.vector.reference_crdns.remove_by_name(
                    GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Satellite/Satellite1 L2 Point"
                )

        ex = ExceptionAssert.Throws(code6)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        oHelper = VODataDisplayHelper(TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.data_display, False, False)

    # endregion

    # region VOOrbitSystems
    @category("VO Tests")
    def test_VOOrbitSystems(self):
        oHelper = VOSystemsHelper()
        if TestBase.ApplicationProvider.Target == TestTarget.eStk:
            oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.orbit_systems, TestBase.Application)

        else:
            oHelper.Run(EarlyBoundTests.AG_SAT.graphics_3d.orbit_systems, None)

    # endregion

    # region VOBPlane
    @category("VO Tests")
    def test_VOBPlane(self):
        # BPlanes
        oBPlanes: "VehicleGraphics3DBPlanes" = EarlyBoundTests.AG_SAT.graphics_3d.b_planes
        Assert.assertIsNotNone(oBPlanes)

        # Templates collection test
        self.VOBPlaneTemplatesCollectionTest(oBPlanes.templates, False)

        # Instance collection test
        Assert.assertFalse((oBPlanes.templates.count == 0))
        oTemplate: "VehicleGraphics3DBPlaneTemplate"
        for oTemplate in oBPlanes.templates:
            self.VOBPlaneInstancesCollectionTest(oBPlanes.instances, oTemplate.name)

        if oBPlanes.instances.count == 0:
            oBPlaneInstance: "VehicleGraphics3DBPlaneInstance" = oBPlanes.instances.add(oBPlanes.templates[0].name)
            Assert.assertIsNotNone(oBPlaneInstance)

        # Attempts to remove a b-plane template currently being used shall fail.
        with pytest.raises(Exception):
            oBPlanes.templates.remove_at(0)
        TestBase.logger.WriteLine("Trying to remove all bplane templates...")
        with pytest.raises(Exception):
            oBPlanes.templates.remove_all()

    # endregion

    # region VOBPlaneTemplatesCollectionTest
    def VOBPlaneTemplatesCollectionTest(
        self, oCollection: "VehicleGraphics3DBPlaneTemplatesCollection", bClearCollection: bool
    ):
        Assert.assertIsNotNone(oCollection)
        # Count
        TestBase.logger.WriteLine3("The current BPlaneTemplates collection contain: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            TestBase.logger.WriteLine10(
                "\tElement {0}: Name = {1}, Description = {2}, CentralBody = {3}, ReferenceVector = {4}",
                iIndex,
                oCollection[iIndex].name,
                oCollection[iIndex].description,
                oCollection[iIndex].central_body,
                oCollection[iIndex].reference_vector,
            )

            iIndex += 1

        # RemoveAll
        oCollection.remove_all()
        TestBase.logger.WriteLine3(
            "After RemoveAll the BPlaneTemplates collection contain: {0} elements.", oCollection.count
        )
        Assert.assertEqual(0, oCollection.count)
        # Add 1
        oNewTemplate1: "VehicleGraphics3DBPlaneTemplate" = oCollection.add()
        Assert.assertIsNotNone(oNewTemplate1)
        TestBase.logger.WriteLine3(
            "After adding first Template the BPlaneTemplates collection contain: {0} elements.", oCollection.count
        )

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            TestBase.logger.WriteLine10(
                "\tElement {0}: Name = {1}, Description = {2}, CentralBody = {3}, ReferenceVector = {4}",
                iIndex,
                oCollection[iIndex].name,
                oCollection[iIndex].description,
                oCollection[iIndex].central_body,
                oCollection[iIndex].reference_vector,
            )

            iIndex += 1

        # Add 2
        oNewTemplate2: "VehicleGraphics3DBPlaneTemplate" = oCollection.add()
        Assert.assertIsNotNone(oNewTemplate2)
        TestBase.logger.WriteLine3(
            "After adding second Template the BPlaneTemplates collection contain: {0} elements.", oCollection.count
        )
        bPlaneTemplate: "VehicleGraphics3DBPlaneTemplate"
        for bPlaneTemplate in oCollection:
            # _NewEnum
            TestBase.logger.WriteLine9(
                "\tElement: Name = {0}, Description = {1}, CentralBody = {2}, ReferenceVector = {3}",
                bPlaneTemplate.name,
                bPlaneTemplate.description,
                bPlaneTemplate.central_body,
                bPlaneTemplate.reference_vector,
            )

        # RemoveAt
        Assert.assertEqual(2, oCollection.count)
        oCollection.remove_at(1)
        TestBase.logger.WriteLine3(
            "After removing second Template the BPlaneTemplates collection contain: {0} elements.", oCollection.count
        )
        bPlaneTemplate: "VehicleGraphics3DBPlaneTemplate"
        for bPlaneTemplate in oCollection:
            # _NewEnum
            TestBase.logger.WriteLine9(
                "\tElement: Name = {0}, Description = {1}, CentralBody = {2}, ReferenceVector = {3}",
                bPlaneTemplate.name,
                bPlaneTemplate.description,
                bPlaneTemplate.central_body,
                bPlaneTemplate.reference_vector,
            )

        with pytest.raises(Exception):
            oCollection.remove_at(12)
        # VOBPlaneTemplateTest
        self.VOBPlaneTemplateTest(oCollection[0])
        if bClearCollection:
            oCollection.remove_all()
            TestBase.logger.WriteLine3(
                "After RemoveAll the BPlaneTemplates collection contain: {0} elements.", oCollection.count
            )
            Assert.assertEqual(0, oCollection.count)

    # endregion

    # region VOBPlaneTemplateTest
    def VOBPlaneTemplateTest(self, oTemplate: "VehicleGraphics3DBPlaneTemplate"):
        TestBase.logger.WriteLine("VehicleGraphics3DBPlaneTemplate test:")
        Assert.assertIsNotNone(oTemplate)
        # Name
        TestBase.logger.WriteLine5("\tThe current Name is: {0}", oTemplate.name)
        oTemplate.name = "XYZ"
        TestBase.logger.WriteLine5("\tThe new Name is: {0}", oTemplate.name)
        Assert.assertEqual("XYZ", oTemplate.name)
        # Description
        TestBase.logger.WriteLine5("\tThe current Description is: {0}", oTemplate.description)
        oTemplate.description = "There is a place for your advertisement."
        TestBase.logger.WriteLine5("\tThe new Description is: {0}", oTemplate.description)
        Assert.assertEqual("There is a place for your advertisement.", oTemplate.description)
        # CentralBody
        TestBase.logger.WriteLine5("\tThe current CentralBody is: {0}", oTemplate.central_body)
        oTemplate.central_body = "Pluto"
        TestBase.logger.WriteLine5("\tThe new CentralBody is: {0}", oTemplate.central_body)
        Assert.assertEqual("Pluto", oTemplate.central_body)
        with pytest.raises(Exception):
            oTemplate.central_body = "AbstractBody"
        # AvailableCentralBodies
        arBodies = oTemplate.available_central_bodies
        TestBase.logger.WriteLine3("\tAvailable CentralBodies array contains: {0} elements", Array.Length(arBodies))

        iIndex: int = 0
        while iIndex < Array.Length(arBodies):
            strBody: str = str(arBodies[iIndex])
            TestBase.logger.WriteLine7("\t\tElement {0}: {1}", iIndex, strBody)
            oTemplate.central_body = strBody
            TestBase.logger.WriteLine5("\t\t\tThe new CentralBody is: {0}", oTemplate.central_body)
            Assert.assertEqual(strBody, oTemplate.central_body)

            iIndex += 1

        # ReferenceVector
        TestBase.logger.WriteLine5("\tThe current ReferenceVector is: {0}", oTemplate.reference_vector)
        oTemplate.reference_vector = "CentralBody/Earth EclipticNormal Vector"
        TestBase.logger.WriteLine5("\tThe new ReferenceVector is: {0}", oTemplate.reference_vector)
        Assert.assertEqual("CentralBody/Earth EclipticNormal Vector", oTemplate.reference_vector)

        try:
            oTemplate.reference_vector = "AbstractVector"

        except Exception as e:
            if not ("not a valid choice" in str(e)):
                Assert.fail("VehicleGraphics3DBPlaneTemplate.ReferenceVector - invalid choice")

        # AvailableVectors
        arVectors = oTemplate.available_vectors
        TestBase.logger.WriteLine3("\tAvailable ReferenceVector array contains: {0} elements", Array.Length(arVectors))

        iIndex: int = 0
        while iIndex < Array.Length(arVectors):
            strVector: str = str(arVectors[iIndex])
            TestBase.logger.WriteLine7("\t\tElement {0}: {1}", iIndex, strVector)
            oTemplate.reference_vector = strVector
            TestBase.logger.WriteLine5("\t\t\tThe new ReferenceVector is: {0}", oTemplate.reference_vector)
            Assert.assertEqual(strVector, oTemplate.reference_vector)

            iIndex += 1

        # IsCartesianGridVisible
        TestBase.logger.WriteLine4("\tThe current IsCartesianGridVisible is: {0}", oTemplate.is_cartesian_grid_visible)
        oTemplate.is_cartesian_grid_visible = False
        TestBase.logger.WriteLine4("\tThe new IsCartesianGridVisible is: {0}", oTemplate.is_cartesian_grid_visible)
        Assert.assertEqual(False, oTemplate.is_cartesian_grid_visible)
        oTemplate.is_cartesian_grid_visible = True
        TestBase.logger.WriteLine4("\tThe new IsCartesianGridVisible is: {0}", oTemplate.is_cartesian_grid_visible)
        Assert.assertEqual(True, oTemplate.is_cartesian_grid_visible)
        # IsPolarGridVisible
        TestBase.logger.WriteLine4("\tThe current IsPolarGridVisible is: {0}", oTemplate.is_polar_grid_visible)
        oTemplate.is_polar_grid_visible = False
        TestBase.logger.WriteLine4("\tThe new IsPolarGridVisible is: {0}", oTemplate.is_polar_grid_visible)
        Assert.assertEqual(False, oTemplate.is_polar_grid_visible)
        oTemplate.is_polar_grid_visible = True
        TestBase.logger.WriteLine4("\tThe new IsPolarGridVisible is: {0}", oTemplate.is_polar_grid_visible)
        Assert.assertEqual(True, oTemplate.is_polar_grid_visible)
        # set DistanceUnit
        strDistanceUnit: str = self.Units.get_current_unit_abbrv("DistanceUnit")
        TestBase.logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.Units.set_current_unit("DistanceUnit", "mi")
        TestBase.logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.Units.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("mi", self.Units.get_current_unit_abbrv("DistanceUnit"))
        # GridSpacing
        TestBase.logger.WriteLine6("\tThe current GridSpacing is: {0}", oTemplate.grid_spacing)
        oTemplate.grid_spacing = 123.456
        TestBase.logger.WriteLine6("\tThe new GridSpacing is: {0}", oTemplate.grid_spacing)
        Assert.assertEqual(123.456, oTemplate.grid_spacing)
        with pytest.raises(Exception):
            oTemplate.grid_spacing = -123.456
        # restore DistanceUnit
        self.Units.set_current_unit("DistanceUnit", strDistanceUnit)
        TestBase.logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.Units.get_current_unit_abbrv("DistanceUnit"))
        # DisplayElements
        self.VOBPlaneTemplateDisplayCollectionTest(oTemplate.display_elements)

    # endregion

    # region VOBPlaneTemplateDisplayCollectionTest
    def VOBPlaneTemplateDisplayCollectionTest(self, oCollection: "VehicleGraphics3DBPlaneTemplateDisplayCollection"):
        TestBase.logger.WriteLine("VehicleGraphics3DBPlaneTemplateDisplayCollection test:")
        Assert.assertIsNotNone(oCollection)
        # Count
        TestBase.logger.WriteLine3("\tThe BPlaneTemplateDisplay collection contain: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            TestBase.logger.WriteLine10(
                "\tElement {0}: Name = {1}, Color = {2}, Scale = {3}, IsVisible = {4}, IsLabelVisible = {5}",
                iIndex,
                oCollection[iIndex].name,
                oCollection[iIndex].color,
                oCollection[iIndex].scale_factor,
                oCollection[iIndex].is_visible,
                oCollection[iIndex].is_label_visible,
            )

            iIndex += 1

        Assert.assertEqual(8, oCollection.count)
        # _NewEnum
        bPlaneTemplateDisplayElement: "VehicleGraphics3DBPlaneTemplateDisplayElement"
        # _NewEnum
        for bPlaneTemplateDisplayElement in oCollection:
            TestBase.logger.WriteLine5("\tElement: Name = {0}", bPlaneTemplateDisplayElement.name)
            # IsVisible (false)
            TestBase.logger.WriteLine4("\t\tThe current IsVisible is: {0}", bPlaneTemplateDisplayElement.is_visible)
            bPlaneTemplateDisplayElement.is_visible = False
            TestBase.logger.WriteLine4("\t\tThe new IsVisible is: {0}", bPlaneTemplateDisplayElement.is_visible)
            Assert.assertEqual(False, bPlaneTemplateDisplayElement.is_visible)
            # Color (readonly)
            with pytest.raises(Exception):
                bPlaneTemplateDisplayElement.color = Colors.from_argb(1193046)
            # ScaleFactor (readonly)
            with pytest.raises(Exception):
                bPlaneTemplateDisplayElement.scale_factor = 12.3456
            # IsLabelVisible (readonly)
            with pytest.raises(Exception):
                bPlaneTemplateDisplayElement.is_label_visible = True
            # IsVisible (true)
            bPlaneTemplateDisplayElement.is_visible = True
            TestBase.logger.WriteLine4("\t\tThe new IsVisible is: {0}", bPlaneTemplateDisplayElement.is_visible)
            Assert.assertEqual(True, bPlaneTemplateDisplayElement.is_visible)
            # Name
            TestBase.logger.WriteLine5("\t\t\tThe current Name is: {0}", bPlaneTemplateDisplayElement.name)
            # Color
            TestBase.logger.WriteLine6("\t\t\tThe current Color is: {0}", bPlaneTemplateDisplayElement.color)
            bPlaneTemplateDisplayElement.color = Colors.from_argb(9991764)
            TestBase.logger.WriteLine6("\t\t\tThe new Color is: {0}", bPlaneTemplateDisplayElement.color)
            AssertEx.AreEqual(Colors.from_argb(9991764), bPlaneTemplateDisplayElement.color)
            # ScaleFactor
            TestBase.logger.WriteLine6(
                "\t\t\tThe current ScaleFactor is: {0}", bPlaneTemplateDisplayElement.scale_factor
            )
            if bPlaneTemplateDisplayElement.name == "BVector":
                with pytest.raises(Exception):
                    bPlaneTemplateDisplayElement.scale_factor = 98.7654

            else:
                bPlaneTemplateDisplayElement.scale_factor = 98.7654
                TestBase.logger.WriteLine6(
                    "\t\t\tThe new ScaleFactor is: {0}", bPlaneTemplateDisplayElement.scale_factor
                )
                Assert.assertEqual(98.7654, bPlaneTemplateDisplayElement.scale_factor)
                with pytest.raises(Exception):
                    bPlaneTemplateDisplayElement.scale_factor = -123.456

            # IsLabelVisible
            TestBase.logger.WriteLine4(
                "\t\t\tThe current IsLabelVisible is: {0}", bPlaneTemplateDisplayElement.is_label_visible
            )
            bPlaneTemplateDisplayElement.is_label_visible = False
            TestBase.logger.WriteLine4(
                "\t\t\tThe new IsLabelVisible is: {0}", bPlaneTemplateDisplayElement.is_label_visible
            )
            Assert.assertEqual(False, bPlaneTemplateDisplayElement.is_label_visible)
            bPlaneTemplateDisplayElement.is_label_visible = True
            TestBase.logger.WriteLine4(
                "\t\t\tThe new IsLabelVisible is: {0}", bPlaneTemplateDisplayElement.is_label_visible
            )
            Assert.assertEqual(True, bPlaneTemplateDisplayElement.is_label_visible)

    # endregion

    # region VOBPlaneInstancesCollectionTest
    def VOBPlaneInstancesCollectionTest(
        self, oCollection: "VehicleGraphics3DBPlaneInstancesCollection", strTemplateName: str
    ):
        Assert.assertIsNotNone(oCollection)
        TestBase.logger.WriteLine5(
            "VehicleGraphics3DBPlaneInstancesCollection test: Template Name = {0}", strTemplateName
        )
        # Count
        TestBase.logger.WriteLine3("\tThe current BPlaneInstances collection contain: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: Name = {1}, Description = {2}, Definition = {3}, EventName = {4}, VOWindow = {5}",
                iIndex,
                oCollection[iIndex].name,
                oCollection[iIndex].description,
                oCollection[iIndex].definition,
                oCollection[iIndex].event_name,
                oCollection[iIndex].graphics_3d_window,
            )

            iIndex += 1

        # RemoveAll
        oCollection.remove_all()
        TestBase.logger.WriteLine3(
            "\tAfter RemoveAll the BPlaneInstances collection contain: {0} elements.", oCollection.count
        )
        Assert.assertEqual(0, oCollection.count)
        # Add 1
        oNewInstance1: "VehicleGraphics3DBPlaneInstance" = oCollection.add(strTemplateName)
        Assert.assertIsNotNone(oNewInstance1)
        TestBase.logger.WriteLine3(
            "\tAfter adding first Instance the BPlaneInstances collection contain: {0} elements.", oCollection.count
        )

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: Name = {1}, Description = {2}, Definition = {3}, EventName = {4}, VOWindow = {5}",
                iIndex,
                oCollection[iIndex].name,
                oCollection[iIndex].description,
                oCollection[iIndex].definition,
                oCollection[iIndex].event_name,
                oCollection[iIndex].graphics_3d_window,
            )

            iIndex += 1

        # Add 2
        oNewInstance2: "VehicleGraphics3DBPlaneInstance" = oCollection.add(strTemplateName)
        Assert.assertIsNotNone(oNewInstance2)
        TestBase.logger.WriteLine3(
            "\tAfter adding second Instance the BPlaneInstances collection contain: {0} elements.", oCollection.count
        )
        bPlaneInstance: "VehicleGraphics3DBPlaneInstance"
        for bPlaneInstance in oCollection:
            # _NewEnum
            TestBase.logger.WriteLine10(
                "\t\tElement: Name = {0}, Description = {1}, Definition = {2}, EventName = {3}, VOWindow = {4}",
                bPlaneInstance.name,
                bPlaneInstance.description,
                bPlaneInstance.definition,
                bPlaneInstance.event_name,
                bPlaneInstance.graphics_3d_window,
            )

        # Add (illegal value)
        with pytest.raises(Exception):
            oCollection.add("Something")
        # RemoveAt
        Assert.assertEqual(2, oCollection.count)
        oCollection.remove_at(1)
        TestBase.logger.WriteLine3(
            "\tAfter removing second Instance the BPlaneInstances collection contain: {0} elements.", oCollection.count
        )
        bPlaneInstance: "VehicleGraphics3DBPlaneInstance"
        for bPlaneInstance in oCollection:
            # _NewEnum
            TestBase.logger.WriteLine10(
                "\t\tElement: Name = {0}, Description = {1}, Definition = {2}, EventName = {3}, VOWindow = {4}",
                bPlaneInstance.name,
                bPlaneInstance.description,
                bPlaneInstance.definition,
                bPlaneInstance.event_name,
                bPlaneInstance.graphics_3d_window,
            )

        with pytest.raises(Exception):
            oCollection.remove_at(12)
        # VOBPlaneInstanceTest
        self.VOBPlaneInstanceTest(oCollection[0])

    # endregion

    # region VOBPlaneInstanceTest
    def VOBPlaneInstanceTest(self, oInstance: "VehicleGraphics3DBPlaneInstance"):
        TestBase.logger.WriteLine("VehicleGraphics3DBPlaneInstance test:")
        Assert.assertIsNotNone(oInstance)
        # some precondition steps
        oInstance.is_visible = True
        oInstance.additional_points.add()
        # IsVisible (false)
        TestBase.logger.WriteLine4("\tThe current IsVisible is: {0}", oInstance.is_visible)
        oInstance.is_visible = False
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oInstance.is_visible)
        Assert.assertEqual(False, oInstance.is_visible)
        # Name
        with pytest.raises(Exception):
            oInstance.name = "Name"
        # Description
        with pytest.raises(Exception):
            oInstance.description = "Description"
        # EventName
        with pytest.raises(Exception):
            oInstance.event_name = "EventName"
        # PointColor
        with pytest.raises(Exception):
            oInstance.additional_points.point_color = Colors.from_argb(2241348)
        # IsLabelVisible
        with pytest.raises(Exception):
            oInstance.is_label_visible = True
        # PointSize
        with pytest.raises(Exception):
            oInstance.point_size = 3
        # FirstPointColor
        with pytest.raises(Exception):
            oInstance.additional_points.first_point_color = Colors.from_argb(3359829)
        # IsConnectPointsVisible
        with pytest.raises(Exception):
            oInstance.is_connect_points_visible = True
        # ConnectPointsColor
        with pytest.raises(Exception):
            oInstance.connect_points_color = Colors.from_argb(4478310)
        # ConnectPointLineWidth
        with pytest.raises(Exception):
            oInstance.connect_point_line_width = LINE_WIDTH.WIDTH1
        # VOWindow
        with pytest.raises(Exception):
            oInstance.graphics_3d_window = "All"
        # Event
        self.VOBPlaneEventTest(oInstance.event, True)
        # TargetPoint
        self.VOBPlaneTargetPointTest(oInstance.target_point, True)
        # AdditionalPoints
        self.VOBPlanePointCollectionTest(oInstance.additional_points, True)

        # IsVisible (true)
        oInstance.is_visible = True
        TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oInstance.is_visible)
        Assert.assertEqual(True, oInstance.is_visible)
        # Name
        TestBase.logger.WriteLine5("\t\tThe current Name is: {0}", oInstance.name)
        oInstance.name = "NewInstanceName"
        TestBase.logger.WriteLine5("\t\tThe new Name is: {0}", oInstance.name)
        Assert.assertEqual("NewInstanceName", oInstance.name)
        with pytest.raises(Exception):
            oInstance.name = "New Instance Name"
        # Description
        TestBase.logger.WriteLine5("\t\tThe current Description is: {0}", oInstance.description)
        oInstance.description = "There is a new description."
        TestBase.logger.WriteLine5("\t\tThe new Description is: {0}", oInstance.description)
        Assert.assertEqual("There is a new description.", oInstance.description)
        # Definition (always readonly)
        TestBase.logger.WriteLine5("\t\tThe current Definition is: {0}", oInstance.definition)
        # EventName
        TestBase.logger.WriteLine5("\t\tThe current EventName is: {0}", oInstance.event_name)
        oInstance.event_name = "The new Event Name"
        TestBase.logger.WriteLine5("\t\tThe new EventName is: {0}", oInstance.event_name)
        Assert.assertEqual("The new Event Name", oInstance.event_name)
        # PointColor
        TestBase.logger.WriteLine6("\t\tThe current PointColor is: {0}", oInstance.additional_points.point_color)
        oInstance.additional_points.point_color = Colors.from_argb(1122867)
        TestBase.logger.WriteLine6("\t\tThe new PointColor is: {0}", oInstance.additional_points.point_color)
        AssertEx.AreEqual(Colors.from_argb(1122867), oInstance.additional_points.point_color)
        # IsLabelVisible
        TestBase.logger.WriteLine4("\t\tThe current IsLabelVisible is: {0}", oInstance.is_label_visible)
        oInstance.is_label_visible = False
        TestBase.logger.WriteLine4("\t\tThe new IsLabelVisible is: {0}", oInstance.is_label_visible)
        Assert.assertEqual(False, oInstance.is_label_visible)
        oInstance.is_label_visible = True
        TestBase.logger.WriteLine4("\t\tThe new IsLabelVisible is: {0}", oInstance.is_label_visible)
        Assert.assertEqual(True, oInstance.is_label_visible)
        # PointSize
        TestBase.logger.WriteLine6("\t\tThe current PointSize is: {0}", oInstance.point_size)
        oInstance.point_size = 7
        TestBase.logger.WriteLine6("\t\tThe new PointSize is: {0}", oInstance.point_size)
        Assert.assertEqual(7, oInstance.point_size)
        with pytest.raises(Exception):
            oInstance.point_size = 17
        # FirstPointColor
        TestBase.logger.WriteLine6(
            "\t\tThe current FirstPointColor is: {0}", oInstance.additional_points.first_point_color
        )
        oInstance.additional_points.first_point_color = Colors.from_argb(2241348)
        TestBase.logger.WriteLine6("\t\tThe new FirstPointColor is: {0}", oInstance.additional_points.first_point_color)
        AssertEx.AreEqual(Colors.from_argb(2241348), oInstance.additional_points.first_point_color)
        # IsConnectPointsVisible (false)
        TestBase.logger.WriteLine4(
            "\t\tThe current IsConnectPointsVisible is: {0}", oInstance.is_connect_points_visible
        )
        oInstance.is_connect_points_visible = False
        TestBase.logger.WriteLine4("\t\tThe new IsConnectPointsVisible is: {0}", oInstance.is_connect_points_visible)
        Assert.assertEqual(False, oInstance.is_connect_points_visible)
        # ConnectPointsColor
        with pytest.raises(Exception):
            oInstance.connect_points_color = Colors.from_argb(4478310)
        # ConnectPointLineWidth
        with pytest.raises(Exception):
            oInstance.connect_point_line_width = LINE_WIDTH.WIDTH1
        # IsConnectPointsVisible (true)
        oInstance.is_connect_points_visible = True
        TestBase.logger.WriteLine4("\t\tThe new IsConnectPointsVisible is: {0}", oInstance.is_connect_points_visible)
        Assert.assertEqual(True, oInstance.is_connect_points_visible)
        # ConnectPointsColor
        TestBase.logger.WriteLine6("\t\tThe current ConnectPointsColor is: {0}", oInstance.connect_points_color)
        oInstance.connect_points_color = Colors.from_argb(4478310)
        TestBase.logger.WriteLine6("\t\tThe new ConnectPointsColor is: {0}", oInstance.connect_points_color)
        AssertEx.AreEqual(Colors.from_argb(4478310), oInstance.connect_points_color)
        # ConnectPointLineWidth
        TestBase.logger.WriteLine6("\t\tThe current ConnectPointLineWidth is: {0}", oInstance.connect_point_line_width)
        oInstance.connect_point_line_width = LINE_WIDTH.WIDTH1
        TestBase.logger.WriteLine6("\t\tThe new ConnectPointLineWidth is: {0}", oInstance.connect_point_line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH1, oInstance.connect_point_line_width)
        # VOWindow
        TestBase.logger.WriteLine5("\t\tThe current VOWindow is: {0}", oInstance.graphics_3d_window)
        # AvailableVOWindows
        arWindows = oInstance.available_graphics_3d_windows
        TestBase.logger.WriteLine3("\t\tAvailable: {0} VO windows.", Array.Length(arWindows))

        iIndex: int = 0
        while iIndex < Array.Length(arWindows):
            TestBase.logger.WriteLine7("\t\t\tWindow {0}: {1}", iIndex, arWindows[iIndex])
            oInstance.graphics_3d_window = str(arWindows[iIndex])
            TestBase.logger.WriteLine5("\t\t\t\tThe new VOWindow is: {0}", oInstance.graphics_3d_window)
            Assert.assertEqual(arWindows[iIndex], oInstance.graphics_3d_window)

            iIndex += 1

        # Event
        self.VOBPlaneEventTest(oInstance.event, False)
        # TargetPoint
        self.VOBPlaneTargetPointTest(oInstance.target_point, False)
        # AdditionalPoints
        self.VOBPlanePointCollectionTest(oInstance.additional_points, False)

    # endregion

    # region VOBPlaneEventTest
    def VOBPlaneEventTest(self, oEvent: "VehicleGraphics3DBPlaneEvent", bReadOnly: bool):
        TestBase.logger.WriteLine4("VehicleGraphics3DBPlaneEvent test: ReadOnly = {0}", bReadOnly)
        Assert.assertIsNotNone(oEvent)
        # set DateFormat
        strDate: str = self.Units.get_current_unit_abbrv("DateFormat")
        TestBase.logger.WriteLine5("\tThe current DateFormat is: {0}", strDate)
        self.Units.set_current_unit("DateFormat", "UTCG")
        TestBase.logger.WriteLine5("\tThe new DateFormat is: {0}", self.Units.get_current_unit_abbrv("DateFormat"))
        Assert.assertEqual("UTCG", self.Units.get_current_unit_abbrv("DateFormat"))
        # set TimeUnit
        strTime: str = self.Units.get_current_unit_abbrv("TimeUnit")
        TestBase.logger.WriteLine5("\tThe current TimeUnit is: {0}", strTime)
        self.Units.set_current_unit("TimeUnit", "hr")
        TestBase.logger.WriteLine5("\tThe new TimeUnit is: {0}", self.Units.get_current_unit_abbrv("TimeUnit"))
        Assert.assertEqual("hr", self.Units.get_current_unit_abbrv("TimeUnit"))
        if bReadOnly:
            # EventEpoch
            with pytest.raises(Exception):
                oEvent.event_epoch = "1 Jul 1999 01:00:00.000"
            # AlwaysDisplay
            with pytest.raises(Exception):
                oEvent.always_display = False
            # BeforeEvent
            with pytest.raises(Exception):
                oEvent.before_event = 1
            # AfterEvent
            with pytest.raises(Exception):
                oEvent.after_event = 2

        else:
            # EventEpoch
            TestBase.logger.WriteLine6("\t\tThe current EventEpoch is: {0}", oEvent.event_epoch)
            oEvent.event_epoch = "1 Jul 1999 05:00:00.000"
            TestBase.logger.WriteLine6("\t\tThe new EventEpoch is: {0}", oEvent.event_epoch)
            Assert.assertEqual("1 Jul 1999 05:00:00.000", oEvent.event_epoch)
            # AlwaysDisplay (true)
            TestBase.logger.WriteLine4("\t\tThe current AlwaysDisplay is: {0}", oEvent.always_display)
            oEvent.always_display = True
            TestBase.logger.WriteLine4("\t\tThe new AlwaysDisplay is: {0}", oEvent.always_display)
            Assert.assertEqual(True, oEvent.always_display)
            # BeforeEvent
            with pytest.raises(Exception):
                oEvent.before_event = 1
            # AfterEvent
            with pytest.raises(Exception):
                oEvent.after_event = 2
            # AlwaysDisplay (false)
            oEvent.always_display = False
            TestBase.logger.WriteLine4("\t\tThe new AlwaysDisplay is: {0}", oEvent.always_display)
            Assert.assertEqual(False, oEvent.always_display)
            # BeforeEvent
            TestBase.logger.WriteLine6("\t\tThe current BeforeEvent is: {0}", oEvent.before_event)
            oEvent.before_event = 12
            TestBase.logger.WriteLine6("\t\tThe new BeforeEvent is: {0}", oEvent.before_event)
            Assert.assertEqual(12, oEvent.before_event)
            with pytest.raises(Exception):
                oEvent.before_event = 1200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            # AfterEvent
            TestBase.logger.WriteLine6("\t\tThe current AfterEvent is: {0}", oEvent.after_event)
            oEvent.after_event = 21
            TestBase.logger.WriteLine6("\t\tThe new AfterEvent is: {0}", oEvent.after_event)
            Assert.assertEqual(21, oEvent.after_event)
            with pytest.raises(Exception):
                oEvent.after_event = 2300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

        # restore TimeUnit
        self.Units.set_current_unit("TimeUnit", strTime)
        TestBase.logger.WriteLine5("\tThe new TimeUnit (restored) is: {0}", strTime)
        Assert.assertEqual(strTime, self.Units.get_current_unit_abbrv("TimeUnit"))
        # restore DateFormat
        self.Units.set_current_unit("DateFormat", strDate)
        TestBase.logger.WriteLine5("\tThe new DateFormat (restored) is: {0}", strDate)
        Assert.assertEqual(strDate, self.Units.get_current_unit_abbrv("DateFormat"))

    # endregion

    # region VOBPlaneTargetPointTest
    def VOBPlaneTargetPointTest(self, oPoint: "VehicleGraphics3DBPlaneTargetPoint", bReadOnly: bool):
        TestBase.logger.WriteLine4("VehicleGraphics3DBPlaneTargetPoint test: ReadOnly = {0}", bReadOnly)
        Assert.assertIsNotNone(oPoint)
        if bReadOnly:
            # IsVisible
            with pytest.raises(Exception):
                oPoint.is_visible = True
            # Color
            with pytest.raises(Exception):
                oPoint.color = Colors.from_argb(11189196)
            # SetPositionType
            with pytest.raises(Exception):
                oPoint.set_position_type(oPoint.position_type)
            if oPoint.position_type == VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION.POSITION_CARTESIAN:
                # Position
                oCartesian: "VehicleGraphics3DBPlaneTargetPointPositionCartesian" = (
                    VehicleGraphics3DBPlaneTargetPointPositionCartesian(oPoint.position)
                )
                Assert.assertIsNotNone(oCartesian)
                self.VOBPlaneTargetPointPositionCartesianTest(oCartesian, True)
            elif oPoint.position_type == VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION.POSITION_POLAR:
                # Position
                oPolar: "VehicleGraphics3DBPlaneTargetPointPositionPolar" = (
                    VehicleGraphics3DBPlaneTargetPointPositionPolar(oPoint.position)
                )
                Assert.assertIsNotNone(oPolar)
                self.VOBPlaneTargetPointPositionPolarTest(oPolar, True)
            else:
                Assert.fail("Invalid Position type!")

        else:
            # IsVisible (false)
            TestBase.logger.WriteLine4("\t\tThe current IsVisible is: {0}", oPoint.is_visible)
            oPoint.is_visible = False
            TestBase.logger.WriteLine4("\t\tThe new IsVisible is: {0}", oPoint.is_visible)
            Assert.assertEqual(False, oPoint.is_visible)
            # Color
            with pytest.raises(Exception):
                oPoint.color = Colors.from_argb(11189196)
            # SetPositionType
            with pytest.raises(Exception):
                oPoint.set_position_type(oPoint.position_type)
            if oPoint.position_type == VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION.POSITION_CARTESIAN:
                # Position
                oCartesian: "VehicleGraphics3DBPlaneTargetPointPositionCartesian" = (
                    VehicleGraphics3DBPlaneTargetPointPositionCartesian(oPoint.position)
                )
                Assert.assertIsNotNone(oCartesian)
                self.VOBPlaneTargetPointPositionCartesianTest(oCartesian, True)
            elif oPoint.position_type == VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION.POSITION_POLAR:
                # Position
                oPolar: "VehicleGraphics3DBPlaneTargetPointPositionPolar" = (
                    VehicleGraphics3DBPlaneTargetPointPositionPolar(oPoint.position)
                )
                Assert.assertIsNotNone(oPolar)
                self.VOBPlaneTargetPointPositionPolarTest(oPolar, True)
            else:
                Assert.fail("Invalid Position type!")

            #  IsVisible (true)
            oPoint.is_visible = True
            TestBase.logger.WriteLine4("\t\tThe new IsVisible is: {0}", oPoint.is_visible)
            Assert.assertEqual(True, oPoint.is_visible)
            # Color
            TestBase.logger.WriteLine6("\t\tThe current Color is: {0}", oPoint.color)
            oPoint.color = Colors.from_argb(65280)
            TestBase.logger.WriteLine6("\t\tThe new Color is: {0}", oPoint.color)
            AssertEx.AreEqual(Colors.from_argb(65280), oPoint.color)
            # PositionType
            TestBase.logger.WriteLine6("\t\tThe current PositionType is: {0}", oPoint.position_type)
            # PositionSupportedTypes
            arTypes = oPoint.position_supported_types
            TestBase.logger.WriteLine3("\t\tSupported: {0} types.", len(arTypes))

            iIndex: int = 0
            while iIndex < len(arTypes):
                ePosition: "VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION" = (
                    VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION(int(arTypes[iIndex][0]))
                )
                TestBase.logger.WriteLine7("\t\t\tType {0}: {1}", iIndex, ePosition)
                if not oPoint.is_position_type_supported(ePosition):
                    Assert.fail("Type {0} should be supported!", ePosition)

                # SetPositionType
                oPoint.set_position_type(ePosition)
                TestBase.logger.WriteLine6("\t\t\t\tThe new PositionType is: {0}", oPoint.position_type)
                Assert.assertEqual(ePosition, oPoint.position_type)
                if ePosition == VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION.POSITION_CARTESIAN:
                    # Position
                    oCartesian: "VehicleGraphics3DBPlaneTargetPointPositionCartesian" = (
                        VehicleGraphics3DBPlaneTargetPointPositionCartesian(oPoint.position)
                    )
                    Assert.assertIsNotNone(oCartesian)
                    self.VOBPlaneTargetPointPositionCartesianTest(oCartesian, False)
                elif ePosition == VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION.POSITION_POLAR:
                    # Position
                    oPolar: "VehicleGraphics3DBPlaneTargetPointPositionPolar" = (
                        VehicleGraphics3DBPlaneTargetPointPositionPolar(oPoint.position)
                    )
                    Assert.assertIsNotNone(oPolar)
                    self.VOBPlaneTargetPointPositionPolarTest(oPolar, False)
                else:
                    Assert.fail("Invalid Position type!")

                iIndex += 1

    # endregion

    # region VOBPlaneTargetPointPositionCartesianTest
    def VOBPlaneTargetPointPositionCartesianTest(
        self, oPosition: "VehicleGraphics3DBPlaneTargetPointPositionCartesian", bReadOnly: bool
    ):
        TestBase.logger.WriteLine4(
            "VehicleGraphics3DBPlaneTargetPointPositionCartesian test: ReadOnly = {0}", bReadOnly
        )
        Assert.assertIsNotNone(oPosition)
        # set DistanceUnit
        strDistance: str = self.Units.get_current_unit_abbrv("DistanceUnit")
        TestBase.logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistance)
        self.Units.set_current_unit("DistanceUnit", "kft")
        TestBase.logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.Units.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("kft", self.Units.get_current_unit_abbrv("DistanceUnit"))
        if bReadOnly:
            with pytest.raises(Exception):
                oPosition.b_mul_t = 1234.56789
            with pytest.raises(Exception):
                oPosition.b_mul_r = 1234.56789

        else:
            # BMulT
            TestBase.logger.WriteLine6("\tThe current BMulT is: {0}", oPosition.b_mul_t)
            oPosition.b_mul_t = 123.456
            TestBase.logger.WriteLine6("\tThe new BMulT is: {0}", oPosition.b_mul_t)
            Assert.assertEqual(123.456, oPosition.b_mul_t)
            with pytest.raises(Exception):
                oPosition.b_mul_t = 1234000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            # BMulR
            TestBase.logger.WriteLine6("\tThe current BMulR is: {0}", oPosition.b_mul_r)
            oPosition.b_mul_r = 123.456
            TestBase.logger.WriteLine6("\tThe new BMulR is: {0}", oPosition.b_mul_r)
            Assert.assertEqual(123.456, oPosition.b_mul_r)
            with pytest.raises(Exception):
                oPosition.b_mul_r = 1234000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

        # restore DistanceUnit
        self.Units.set_current_unit("DistanceUnit", strDistance)
        TestBase.logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strDistance)
        Assert.assertEqual(strDistance, self.Units.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region VOBPlaneTargetPointPositionPolarTest
    def VOBPlaneTargetPointPositionPolarTest(
        self, oPosition: "VehicleGraphics3DBPlaneTargetPointPositionPolar", bReadOnly: bool
    ):
        TestBase.logger.WriteLine4("VehicleGraphics3DBPlaneTargetPointPositionPolar test: ReadOnly = {0}", bReadOnly)
        Assert.assertIsNotNone(oPosition)
        # set DistanceUnit
        strDistance: str = self.Units.get_current_unit_abbrv("DistanceUnit")
        TestBase.logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistance)
        self.Units.set_current_unit("DistanceUnit", "kft")
        TestBase.logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.Units.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("kft", self.Units.get_current_unit_abbrv("DistanceUnit"))
        # set AngleUnit
        strAngle: str = self.Units.get_current_unit_abbrv("AngleUnit")
        TestBase.logger.WriteLine5("\tThe current AngleUnit is: {0}", strAngle)
        self.Units.set_current_unit("AngleUnit", "rad")
        TestBase.logger.WriteLine5("\tThe new AngleUnit is: {0}", self.Units.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.Units.get_current_unit_abbrv("AngleUnit"))
        if bReadOnly:
            with pytest.raises(Exception):
                oPosition.b_magnitude = 1234.56789
            with pytest.raises(Exception):
                oPosition.theta = 1.234

        else:
            # BMag
            TestBase.logger.WriteLine6("\tThe current BMag is: {0}", oPosition.b_magnitude)
            oPosition.b_magnitude = 123.456
            TestBase.logger.WriteLine6("\tThe new BMag is: {0}", oPosition.b_magnitude)
            Assert.assertEqual(123.456, oPosition.b_magnitude)
            with pytest.raises(Exception):
                oPosition.b_magnitude = 1234000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            # Theta
            TestBase.logger.WriteLine6("\tThe current Theta is: {0}", oPosition.theta)
            oPosition.theta = 3.456
            TestBase.logger.WriteLine6("\tThe new Theta is: {0}", oPosition.theta)
            Assert.assertEqual(3.456, oPosition.theta)
            with pytest.raises(Exception):
                oPosition.theta = 12.34

        # restore AngleUnit
        self.Units.set_current_unit("AngleUnit", strAngle)
        TestBase.logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strAngle)
        Assert.assertEqual(strAngle, self.Units.get_current_unit_abbrv("AngleUnit"))
        # restore DistanceUnit
        self.Units.set_current_unit("DistanceUnit", strDistance)
        TestBase.logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strDistance)
        Assert.assertEqual(strDistance, self.Units.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region VOBPlanePointCollectionTest
    def VOBPlanePointCollectionTest(self, oCollection: "VehicleGraphics3DBPlanePointCollection", bReadOnly: bool):
        Assert.assertIsNotNone(oCollection)
        TestBase.logger.WriteLine4("VehicleGraphics3DBPlanePointCollection test: ReadOnly = {0}", bReadOnly)
        # Count
        TestBase.logger.WriteLine3("\tThe current BPlanePoint collection contain: {0} elements.", oCollection.count)

        iIndex: int = 0
        while iIndex < oCollection.count:
            # Item
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: Name = {1}, BMulT = {2}, BMulR = {3}, BMag = {4}, Theta = {5}",
                iIndex,
                oCollection[iIndex].name,
                oCollection[iIndex].b_mul_t,
                oCollection[iIndex].b_mul_r,
                oCollection[iIndex].b_magnitude,
                oCollection[iIndex].theta,
            )

            iIndex += 1

        if bReadOnly:
            # PointColor
            with pytest.raises(Exception):
                oCollection.point_color = Colors.from_argb(65535)
            # FirstPointColor
            with pytest.raises(Exception):
                oCollection.first_point_color = Colors.from_argb(16776960)
            # RemoveAll
            with pytest.raises(Exception):
                oCollection.remove_all()
            # Add
            with pytest.raises(Exception):
                oCollection.add()
            if oCollection.count > 0:
                with pytest.raises(Exception):
                    oCollection.remove_at(0)

            if oCollection.count > 0:
                self.VOBPlanePointTest(oCollection[0], True)

        else:
            # RemoveAll
            oCollection.remove_all()
            TestBase.logger.WriteLine3(
                "\tAfter RemoveAll the BPlanePoint collection contain: {0} elements.", oCollection.count
            )
            Assert.assertEqual(0, oCollection.count)
            # Add 1
            oNewPoint1: "VehicleGraphics3DBPlanePoint" = oCollection.add()
            Assert.assertIsNotNone(oNewPoint1)
            TestBase.logger.WriteLine3(
                "\tAfter adding first Point the BPlanePoint collection contain: {0} elements.", oCollection.count
            )

            iIndex: int = 0
            while iIndex < oCollection.count:
                # Item
                TestBase.logger.WriteLine10(
                    "\t\tElement {0}: Name = {1}, BMulT = {2}, BMulR = {3}, BMag = {4}, Theta = {5}",
                    iIndex,
                    oCollection[iIndex].name,
                    oCollection[iIndex].b_mul_t,
                    oCollection[iIndex].b_mul_r,
                    oCollection[iIndex].b_magnitude,
                    oCollection[iIndex].theta,
                )

                iIndex += 1

            # Add 2
            oNewPoint2: "VehicleGraphics3DBPlanePoint" = oCollection.add()
            Assert.assertIsNotNone(oNewPoint2)
            TestBase.logger.WriteLine3(
                "\tAfter adding second Point the BPlanePoint collection contain: {0} elements.", oCollection.count
            )
            bPlanePoint: "VehicleGraphics3DBPlanePoint"
            for bPlanePoint in oCollection:
                # _NewEnum
                TestBase.logger.WriteLine10(
                    "\t\tElement: Name = {0}, BMulT = {1}, BMulR = {2}, BMag = {3}, Theta = {4}",
                    bPlanePoint.name,
                    bPlanePoint.b_mul_t,
                    bPlanePoint.b_mul_r,
                    bPlanePoint.b_magnitude,
                    bPlanePoint.theta,
                )

            # RemoveAt
            Assert.assertEqual(2, oCollection.count)
            oCollection.remove_at(1)
            TestBase.logger.WriteLine3(
                "\tAfter removing second Point the BPlanePoint collection contain: {0} elements.", oCollection.count
            )
            bPlanePoint: "VehicleGraphics3DBPlanePoint"
            for bPlanePoint in oCollection:
                # _NewEnum
                TestBase.logger.WriteLine10(
                    "\t\tElement: Name = {0}, BMulT = {1}, BMulR = {2}, BMag = {3}, Theta = {4}",
                    bPlanePoint.name,
                    bPlanePoint.b_mul_t,
                    bPlanePoint.b_mul_r,
                    bPlanePoint.b_magnitude,
                    bPlanePoint.theta,
                )

            with pytest.raises(Exception):
                oCollection.remove_at(12)

            with pytest.raises(Exception):
                oCollection[23].name = "CartesianPoint"

            self.VOBPlanePointTest(oCollection[0], False)

    # endregion

    # region VOBPlanePointTest
    def VOBPlanePointTest(self, oPoint: "VehicleGraphics3DBPlanePoint", bReadOnly: bool):
        Assert.assertIsNotNone(oPoint)
        TestBase.logger.WriteLine4("VehicleGraphics3DBPlanePoint test: ReadOnly = {0}", bReadOnly)
        # set DistanceUnit
        strDistance: str = self.Units.get_current_unit_abbrv("DistanceUnit")
        TestBase.logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistance)
        self.Units.set_current_unit("DistanceUnit", "kft")
        TestBase.logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.Units.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("kft", self.Units.get_current_unit_abbrv("DistanceUnit"))
        # set AngleUnit
        strAngle: str = self.Units.get_current_unit_abbrv("AngleUnit")
        TestBase.logger.WriteLine5("\tThe current AngleUnit is: {0}", strAngle)
        self.Units.set_current_unit("AngleUnit", "rad")
        TestBase.logger.WriteLine5("\tThe new AngleUnit is: {0}", self.Units.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.Units.get_current_unit_abbrv("AngleUnit"))
        if bReadOnly:
            # Name
            with pytest.raises(Exception):
                oPoint.name = "CartesianPoint"
            # BMulT
            with pytest.raises(Exception):
                oPoint.b_mul_t = 12.34
            # BMulR
            with pytest.raises(Exception):
                oPoint.b_mul_r = 34.12
            # BMag
            with pytest.raises(Exception):
                oPoint.b_magnitude = 12.34
            # Theta
            with pytest.raises(Exception):
                oPoint.theta = 34.12

        else:
            # Name
            TestBase.logger.WriteLine5("\tThe current Name is: {0}", oPoint.name)
            oPoint.name = "CartesianPoint"
            TestBase.logger.WriteLine5("\tThe new Name is: {0}", oPoint.name)
            Assert.assertEqual("CartesianPoint", oPoint.name)
            # BMulT
            TestBase.logger.WriteLine6("\tThe current BMulT is: {0}", oPoint.b_mul_t)
            oPoint.b_mul_t = 12.34
            TestBase.logger.WriteLine6("\tThe new BMulT is: {0}", oPoint.b_mul_t)
            Assert.assertEqual(12.34, oPoint.b_mul_t)
            with pytest.raises(Exception):
                oPoint.b_mul_t = 12340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            # BMulR
            TestBase.logger.WriteLine6("\tThe current BMulR is: {0}", oPoint.b_mul_r)
            oPoint.b_mul_r = 34.12
            TestBase.logger.WriteLine6("\tThe new BMulR is: {0}", oPoint.b_mul_r)
            Assert.assertEqual(34.12, oPoint.b_mul_r)
            with pytest.raises(Exception):
                oPoint.b_mul_r = 34120000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            # BMag
            TestBase.logger.WriteLine6("\tThe current BMag is: {0}", oPoint.b_magnitude)
            oPoint.b_magnitude = 12.34
            TestBase.logger.WriteLine6("\tThe new BMag is: {0}", oPoint.b_magnitude)
            Assert.assertEqual(12.34, oPoint.b_magnitude)
            with pytest.raises(Exception):
                oPoint.b_magnitude = 12340000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
            # Theta
            TestBase.logger.WriteLine6("\tThe current Theta is: {0}", oPoint.theta)
            oPoint.theta = 3.412
            TestBase.logger.WriteLine6("\tThe new Theta is: {0}", oPoint.theta)
            Assert.assertEqual(3.412, oPoint.theta)
            with pytest.raises(Exception):
                oPoint.theta = 34120000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

        # restore AngleUnit
        self.Units.set_current_unit("AngleUnit", strAngle)
        TestBase.logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strAngle)
        Assert.assertEqual(strAngle, self.Units.get_current_unit_abbrv("AngleUnit"))
        # restore DistanceUnit
        self.Units.set_current_unit("DistanceUnit", strDistance)
        TestBase.logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strDistance)
        Assert.assertEqual(strDistance, self.Units.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_SAT.graphics_3d.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_SAT.graphics_3d.model, IGraphics3DModel),
            TestBase.GetSTKHomeDir(),
        )

    def TestMinMaxStep(self, newSat: "Satellite", centralBody):
        newSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop: "VehiclePropagatorHPOP" = clr.CastAs(newSat.propagator, VehiclePropagatorHPOP)
        # Step size cannot be larger than 1200.0 for vehicles with Earth as their central body
        hpop.step = 1200.0
        if centralBody == EarlyBoundTests.CentralBodyType.Earth:
            with pytest.raises(Exception):
                hpop.step = 1201.0

        elif centralBody == EarlyBoundTests.CentralBodyType.Sun:
            hpop.force_model.central_body_gravity.file = r"STKData\CentralBodies\Sun\ZonalsToJ4.grv"
            hpop.force_model.central_body_gravity.solid_tide_type = SOLID_TIDE.NONE

            # See: 47217 UseOceanTides is grayed out in GUI but writtable via the Object Model
            # UseOceanTides can only be set(not-grayed out) if the central body is earth.
            try:
                hpop.force_model.central_body_gravity.use_ocean_tides = False
                Assert.fail("Should not allow setting UseOceanTides for non-Earth central bodies")

            except Exception as ex:
                msg: str = str(ex)
                Assert.assertEqual("Central Body was not Earth.", msg)
                TestBase.logger.WriteLine5("EXPECTED EXCEPTION: {0}", msg)

            cart: "OrbitStateCartesian" = clr.CastAs(
                hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN), OrbitStateCartesian
            )
            cart.x_position = 2243970.0
            cart.y_velocity = 171.962
            cart.z_velocity = 171.962
            hpop.initial_state.representation.assign(cart)
            with pytest.raises(Exception):
                hpop.step = (10 * 86400.0) + 1

        else:
            hpop.force_model.central_body_gravity.file = r"STKData\CentralBodies\Moon\ZonalsToJ4.grv"
            hpop.force_model.central_body_gravity.max_order = 0
            hpop.force_model.central_body_gravity.max_degree = 4
            hpop.force_model.central_body_gravity.solid_tide_type = SOLID_TIDE.NONE

            # See: 47217 UseOceanTides is grayed out in GUI but writtable via the Object Model
            # UseOceanTides can only be set(not-grayed out) if the central body is earth.
            try:
                hpop.force_model.central_body_gravity.use_ocean_tides = False
                Assert.fail("Should not allow setting UseOceanTides for non-Earth central bodies")

            except Exception as ex:
                msg: str = str(ex)
                Assert.assertEqual("Central Body was not Earth.", msg)
                TestBase.logger.WriteLine5("EXPECTED EXCEPTION: {0}", msg)

            with pytest.raises(Exception):
                hpop.step = 86400.0 + 1

        sStartTime: str = str((clr.CastAs(TestBase.Application.current_scenario, Scenario)).start_time)
        sStopTime: str = str((clr.CastAs(TestBase.Application.current_scenario, Scenario)).stop_time)

        oScenarioStart: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", sStartTime)
        oScenarioStop: "Date" = TestBase.Application.conversion_utility.new_date("UTCG", sStopTime)

        # Simulate the situation when the interval is smaller than the step
        hpop.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 1199).format("UTCG")
        )
        hpop.step = 1200.0
        with pytest.raises(Exception):
            hpop.propagate()
        # Move the stop time so that the interval exceeds the step
        hpop.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 86400).format("UTCG")
        )

        hpop.propagate()

        newSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twobody: "VehiclePropagatorTwoBody" = clr.CastAs(newSat.propagator, VehiclePropagatorTwoBody)
        twobody.step = 1201

        # Simulate the situation when the interval is smaller than the step
        twobody.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 1199).format("UTCG")
        )
        twobody.step = 1200.0
        with pytest.raises(Exception):
            twobody.propagate()
        # Move the stop time so that the interval exceeds the step
        twobody.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 86400).format("UTCG")
        )

        twobody.propagate()

        newSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2: "VehiclePropagatorJ2Perturbation" = clr.CastAs(newSat.propagator, VehiclePropagatorJ2Perturbation)
        j2.step = 1201

        # Simulate the situation when the interval is smaller than the step
        j2.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 1199).format("UTCG")
        )
        j2.step = 1200.0
        with pytest.raises(Exception):
            j2.propagate()
        # Move the stop time so that the interval exceeds the step
        j2.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 86400).format("UTCG")
        )

        j2.propagate()

        newSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        j4: "VehiclePropagatorJ4Perturbation" = clr.CastAs(newSat.propagator, VehiclePropagatorJ4Perturbation)
        j4.step = 1201

        # Simulate the situation when the interval is smaller than the step
        j4.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 1199).format("UTCG")
        )
        j4.step = 1200.0
        with pytest.raises(Exception):
            j4.propagate()
        # Move the stop time so that the interval exceeds the step
        j4.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 86400).format("UTCG")
        )

        j4.propagate()

        newSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
        sgp4: "VehiclePropagatorSGP4" = clr.CastAs(newSat.propagator, VehiclePropagatorSGP4)

        sgp4.settings.use_sgp4_one_point_interpolation = True
        if sgp4.segments.routine_type != "SGP4":
            sgp4.segments.routine_type = "SGP4"

        Assert.assertEqual("SGP4", sgp4.segments.routine_type)
        sgp4.step = 1201.0

        # Simulate the situation when the interval is smaller than the step
        sgp4.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 1199).format("UTCG")
        )
        sgp4.step = 1200.0
        with pytest.raises(Exception):
            sgp4.propagate()
        # Move the stop time so that the interval exceeds the step
        sgp4.ephemeris_interval.set_start_and_stop_times(
            oScenarioStart.format("UTCG"), oScenarioStart.add("sec", 86400).format("UTCG")
        )

        # As of 9.0 SSC number must be specified for the propagator to succeed.
        sgp4.common_tasks.add_segs_from_online_source("0005")

        sgp4.propagate()

        # Step vs. Use flag (see 47678)
        sgp4.settings.use_sgp4_one_point_interpolation = True
        sgp4.step = 1199
        Assert.assertEqual(1199, sgp4.step)
        sgp4.step = 1201
        Assert.assertEqual(1201, sgp4.step)

        sgp4.settings.use_sgp4_one_point_interpolation = False
        sgp4.step = 1200
        Assert.assertEqual(1200, sgp4.step)
        with pytest.raises(Exception):
            sgp4.step = 1201

    # endregion

    def test_ExportToDataFile(self):
        sat2: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ExportSat"), Satellite
        )
        twoBody: "VehiclePropagatorTwoBody" = clr.CastAs(sat2.propagator, VehiclePropagatorTwoBody)
        twoBody.propagate()

        exportHelper = ExportDataFileHelper(IStkObject(sat2), TestBase.Application)
        exportHelper.AttitudeExportTool(sat2.export_tools.get_attitude_export_tool())
        exportHelper.EphemerisCCSDSExportTool(sat2.export_tools.get_ephemeris_ccsds_export_tool())
        exportHelper.EphemerisCCSDSv2ExportTool(sat2.export_tools.get_ephemeris_ccsd_sv2_export_tool())
        exportHelper.EphemerisCode500ExportTool(sat2.export_tools.get_ephemeris_code500_export_tool())
        exportHelper.EphemerisSpiceExportTool(sat2.export_tools.get_ephemeris_spice_export_tool())
        exportHelper.EphemerisSTKExportTool(sat2.export_tools.get_ephemeris_stk_export_tool(), True)
        exportHelper.PropDefExportTool(sat2.export_tools.get_prop_definition_export_tool())
        exportHelper.EphemerisStkBinaryExportTool(sat2.export_tools.get_ephemeris_stk_binary_export_tool(), True)

        sat2.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop: "VehiclePropagatorHPOP" = clr.CastAs(sat2.propagator, VehiclePropagatorHPOP)
        hpop.covariance.compute_covariance = True
        hpop.covariance.include_consider_analysis = False
        hpop.propagate()
        typeSTK: "VehicleEphemerisStkExportTool" = sat2.export_tools.get_ephemeris_stk_export_tool()

        typeSTK.covariance_type = STK_EPHEM_COVARIANCE_TYPE.POSITION_VELOCITY6_X6
        Assert.assertEqual(STK_EPHEM_COVARIANCE_TYPE.POSITION_VELOCITY6_X6, typeSTK.covariance_type)
        typeSTK.covariance_type = STK_EPHEM_COVARIANCE_TYPE.POSITION3_X3
        Assert.assertEqual(STK_EPHEM_COVARIANCE_TYPE.POSITION3_X3, typeSTK.covariance_type)
        typeSTK.covariance_type = STK_EPHEM_COVARIANCE_TYPE.NONE
        Assert.assertEqual(STK_EPHEM_COVARIANCE_TYPE.NONE, typeSTK.covariance_type)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "ExportSat")

    def test_UiDisplayOrientationType(self):
        ers1: "Satellite" = None
        sensor: "Sensor" = None
        fixed: "SensorPointingFixed" = None
        hpop: "VehiclePropagatorHPOP" = None

        ers1 = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ERS1_Orientation")
        )
        ers1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop = VehiclePropagatorHPOP(ers1.propagator)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 2002 00:00:00.00", "1 Jul 2002 04:00:00.00")
        hpop.step = 60
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 2002 00:00:00.00";
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN)
        )
        (cart).epoch = "1 Jul 2002 00:00:00.00"
        hpop.initial_state.representation.assign(cart)
        hpop.propagate()

        # *** AzEl
        ers1Obj: "IStkObject" = clr.CastAs(ers1, IStkObject)
        sensor = Sensor(ers1Obj.children.new(STK_OBJECT_TYPE.SENSOR, "Sensor_AzEl"))
        sensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)
        fixed = SensorPointingFixed(sensor.pointing)
        azel: "IOrientationAzEl" = IOrientationAzEl(fixed.orientation.convert_to(ORIENTATION_TYPE.AZ_EL))
        azel.about_boresight = AZ_EL_ABOUT_BORESIGHT.ROTATE
        fixed.orientation.assign(azel)

        # *** Euler
        sensor = Sensor(ers1Obj.children.new(STK_OBJECT_TYPE.SENSOR, "Sensor_Euler"))
        sensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)
        fixed = SensorPointingFixed(sensor.pointing)
        euler: "IOrientationEulerAngles" = IOrientationEulerAngles(
            fixed.orientation.convert_to(ORIENTATION_TYPE.EULER_ANGLES)
        )
        euler.sequence = EULER_ORIENTATION_SEQUENCE.SEQUENCE_212
        fixed.orientation.assign(euler)

        # *** Quaternion
        sensor = Sensor(ers1Obj.children.new(STK_OBJECT_TYPE.SENSOR, "Sensor_Quaternion"))
        sensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)
        fixed = SensorPointingFixed(sensor.pointing)
        quat: "IOrientationQuaternion" = IOrientationQuaternion(
            fixed.orientation.convert_to(ORIENTATION_TYPE.QUATERNION)
        )
        fixed.orientation.assign(quat)

        # *** Quaternion
        sensor = Sensor(ers1Obj.children.new(STK_OBJECT_TYPE.SENSOR, "Sensor_YPR"))
        sensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)
        fixed = SensorPointingFixed(sensor.pointing)
        ypr: "IOrientationYPRAngles" = IOrientationYPRAngles(fixed.orientation.convert_to(ORIENTATION_TYPE.YPR_ANGLES))
        ypr.sequence = YPR_ANGLES_SEQUENCE.RYP
        fixed.orientation.assign(ypr)

        TestBase.Application.save_scenario_as(Path.Combine(TestBase.TemporaryDirectory, "Scenario_Orientation.sc"))

        TestBase.LoadTestScenario(Path.Combine("SatelliteTests", "SatelliteTests.sc"))

        EarlyBoundTests.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

    def test_UiDisplayOrbitStateType(self):
        sScenarioName: str = Path.Combine(TestBase.TemporaryDirectory, "Scenario_SatelliteOrbitStates.sc")
        ers1: "Satellite" = None
        orbitState: "IOrbitState" = None
        hpop: "VehiclePropagatorHPOP" = None

        ers1 = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ERS1_Cartesian")
        )
        ers1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop = VehiclePropagatorHPOP(ers1.propagator)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 2002 00:00:00.00", "1 Jul 2002 04:00:00.00")
        hpop.step = 60
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 2002 00:00:00.00";
        cartesian: "OrbitStateCartesian" = OrbitStateCartesian(
            hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CARTESIAN)
        )
        (cartesian).epoch = "1 Jul 2002 00:00:00.00"

        cartesian.coordinate_system_type = COORDINATE_SYSTEM.J2000

        cartesian.x_position = 7678.14
        cartesian.y_position = 0.0
        cartesian.z_position = 0.0
        cartesian.x_velocity = 0.0
        cartesian.y_velocity = 6.7895
        cartesian.z_velocity = 3.6864

        hpop.initial_state.representation.assign(cartesian)
        hpop.propagate()

        # ** configure the initial orbit state using classical (keplerian) orbit elements
        ers1 = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ERS1_Classical")
        )
        ers1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop = VehiclePropagatorHPOP(ers1.propagator)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 2002 00:00:00.00", "1 Jul 2002 04:00:00.00")
        hpop.step = 60
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 2002 00:00:00.00";
        orbitState = hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL)
        orbitState.epoch = "1 Jul 2002 00:00:00.00"
        hpop.initial_state.representation.assign(orbitState)
        hpop.propagate()

        # ** Delaunay
        ers1 = Satellite(TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ERS1_Delaunay"))
        ers1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop = VehiclePropagatorHPOP(ers1.propagator)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 2002 00:00:00.00", "1 Jul 2002 04:00:00.00")
        hpop.step = 60
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 2002 00:00:00.00";
        orbitState = hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.DELAUNAY)
        orbitState.epoch = "1 Jul 2002 00:00:00.00"
        hpop.initial_state.representation.assign(orbitState)
        hpop.propagate()

        # ** Equinoctial
        ers1 = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ERS1_Equinoctial")
        )
        ers1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop = VehiclePropagatorHPOP(ers1.propagator)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 2002 00:00:00.00", "1 Jul 2002 04:00:00.00")
        hpop.step = 60
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 2002 00:00:00.00";
        orbitState = hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.EQUINOCTIAL)
        orbitState.epoch = "1 Jul 2002 00:00:00.00"
        hpop.initial_state.representation.assign(orbitState)
        hpop.propagate()

        # ** Geodetic
        ers1 = Satellite(TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ERS1_Geodetic"))
        ers1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop = VehiclePropagatorHPOP(ers1.propagator)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 2002 00:00:00.00", "1 Jul 2002 04:00:00.00")
        hpop.step = 60
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 2002 00:00:00.00";
        orbitState = hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.GEODETIC)
        Assert.assertEqual(ORBIT_STATE_TYPE.GEODETIC, orbitState.orbit_state_type)
        orbitState.epoch = "1 Jul 2002 00:00:00.00"
        hpop.initial_state.representation.assign(orbitState)
        hpop.propagate()

        # ** MixedSpherical
        ers1 = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ERS1_MixedSpherical")
        )
        ers1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop = VehiclePropagatorHPOP(ers1.propagator)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 2002 00:00:00.00", "1 Jul 2002 04:00:00.00")
        hpop.step = 60
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 2002 00:00:00.00";
        orbitState = hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.MIXED_SPHERICAL)
        orbitState.epoch = "1 Jul 2002 00:00:00.00"
        hpop.initial_state.representation.assign(orbitState)
        hpop.propagate()

        # ** Spherical
        ers1 = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ERS1_Spherical")
        )
        ers1.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
        hpop = VehiclePropagatorHPOP(ers1.propagator)
        hpop.ephemeris_interval.set_start_and_stop_times("1 Jul 2002 00:00:00.00", "1 Jul 2002 04:00:00.00")
        hpop.step = 60
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Jul 2002 00:00:00.00";
        orbitState = hpop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.SPHERICAL)
        orbitState.epoch = "1 Jul 2002 00:00:00.00"
        hpop.initial_state.representation.assign(orbitState)
        hpop.propagate()

        TestBase.Application.save_scenario_as(sScenarioName)
        if not TestBase.NoGraphicsMode:
            (IAnimation(TestBase.Application)).rewind()

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                (IAnimation(TestBase.Application)).rewind()

        TestBase.LoadTestScenario(Path.Combine("SatelliteTests", "SatelliteTests.sc"))

        EarlyBoundTests.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

    # region RealtimePointPerformance
    # Runs two tests to compare the performance of CONNECT vs Object Model
    def test_RealtimePointPerformance(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Realtime_Scenario")
        TestBase.logger.WriteLine("********** USING OM ********************")
        newsat: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "RealtimeSatellite1"
        )
        (Satellite(newsat)).set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        Assert.assertEqual((Satellite(newsat)).propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        rtp: "VehiclePropagatorRealtime" = VehiclePropagatorRealtime((Satellite(newsat)).propagator)
        rtp.time_step = 60
        rtp.timeout_gap = 60
        rtp.duration.look_ahead = 1
        rtp.duration.look_behind = 1800
        rtp.look_ahead_propagator = LOOK_AHEAD_PROPAGATOR.HOLD_CBF_POSITION
        rtp.propagate()

        t1 = DateTime.Now

        # Temporary test code for 45590
        # VehiclePropagatorRealtime realtime = (newsat as Satellite).Propagator as VehiclePropagatorRealtime;
        # realtime.Duration.LookAhead = 10;
        # Assert.AreEqual(10, realtime.Duration.LookAhead);

        helper = OMRealtimePointBuilderHelper()
        helper.Run(newsat, (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder)
        TestBase.logger.WriteLine6("Time taken to populate ephemeris using OM: {0}", DateTime.Now.Subtract(t1))

        TestBase.Application.current_scenario.children.unload(newsat.class_type, newsat.instance_name)
        TestBase.logger.WriteLine("********** USING CONNECT ********************")
        newsat = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "RealtimeSatellite1")
        (Satellite(newsat)).set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        Assert.assertEqual((Satellite(newsat)).propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).propagate()

        t1 = DateTime.Now
        helper = ConnectRealtimePointBuilderHelper()
        helper.Run(newsat)
        TestBase.logger.WriteLine6("Time taken to populate ephemeris using CON: {0}", DateTime.Now.Subtract(t1))

        TestBase.Application.current_scenario.children.unload(newsat.class_type, newsat.instance_name)
        TestBase.logger.WriteLine("********** USING BOOSTED OM W/ VELOCITY INFO ********************")
        newsat = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "RealtimeSatellite1")
        (Satellite(newsat)).set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        Assert.assertEqual((Satellite(newsat)).propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).propagate()

        t1 = None
        helper = None
        helper = BoostedOMRealtimePointBuilderHelper(TestBase.Application, True)

        t1 = DateTime.Now
        helper.Run(newsat, (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.msl_lla)
        TestBase.logger.WriteLine6(
            "Time taken to populate ephemeris using Boosted OM with velocity info: {0}", DateTime.Now.Subtract(t1)
        )

        (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.remove_all_points()

        t1 = DateTime.Now
        helper.Run(newsat, (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.agl_lla)
        TestBase.logger.WriteLine6(
            "Time taken to populate ephemeris using Boosted OM with velocity info: {0}", DateTime.Now.Subtract(t1)
        )

        (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.remove_all_points()

        t1 = DateTime.Now
        # Realtime data includes the velocity information
        helper.Run(newsat, (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.lla)
        TestBase.logger.WriteLine6(
            "Time taken to populate ephemeris using Boosted OM with velocity info: {0}", DateTime.Now.Subtract(t1)
        )

        TestBase.Application.current_scenario.children.unload(newsat.class_type, newsat.instance_name)
        TestBase.logger.WriteLine("********** USING BOOSTED OM W/O VELOCITY INFO ********************")
        newsat = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "RealtimeSatellite1")
        (Satellite(newsat)).set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        Assert.assertEqual((Satellite(newsat)).propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).propagate()

        t1 = None
        helper = None

        helper = BoostedOMRealtimePointBuilderHelper(TestBase.Application, False)

        t1 = DateTime.Now
        # Realtime data includes the velocity information
        helper.Run(newsat, (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.msl_lla)
        TestBase.logger.WriteLine6(
            "Time taken to populate ephemeris using Boosted OM w/o velocity info: {0}", DateTime.Now.Subtract(t1)
        )

        (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.remove_all_points()

        t1 = DateTime.Now
        # Realtime data includes the velocity information
        helper.Run(newsat, (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.agl_lla)
        TestBase.logger.WriteLine6(
            "Time taken to populate ephemeris using Boosted OM w/o velocity info: {0}", DateTime.Now.Subtract(t1)
        )

        (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.remove_all_points()

        t1 = DateTime.Now
        # Realtime data includes the velocity information
        helper.Run(newsat, (VehiclePropagatorRealtime((Satellite(newsat)).propagator)).point_builder.lla)
        TestBase.logger.WriteLine6(
            "Time taken to populate ephemeris using Boosted OM w/o velocity info: {0}", DateTime.Now.Subtract(t1)
        )

        TestBase.Application.current_scenario.children.unload(newsat.class_type, newsat.instance_name)

        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("SatelliteTests", "SatelliteTests.sc"))
        EarlyBoundTests.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

    # endregion

    # region RealtimePointBuilders
    class RealtimeBuilderTemplate(object):
        def __init__(self, o: "IStkObject", llaPoints: "List[List[float]]", bPositionOnly: bool):
            self._pb: "VehicleRealtimePointBuilder" = None
            self._increment: float = 0
            self._llaPoints: "List[List[float]]" = llaPoints
            self._o: "IStkObject" = o
            self._bPositionOnly: bool = bPositionOnly

        @property
        def PointBuilder(self):
            return self._pb

        @property
        def StkObject(self):
            return self._o

        @property
        def UsePositionOnly(self):
            return self._bPositionOnly

        def Invoke(self, d, posTypeStr: str):
            Assert.assertIsNotNone(d)
            Assert.assertIsNotNone(self._o)
            Assert.assertTrue(clr.Is(self._o, Satellite))
            Assert.assertTrue(((Satellite(self._o)).propagator_type == VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME))
            rtp: "VehiclePropagatorRealtime" = VehiclePropagatorRealtime((Satellite(self._o)).propagator)
            self._pb = rtp.point_builder

            # Configure the unit preferences
            self._o.root.unit_preferences.set_current_unit("DateFormat", "EpSec")
            self._o.root.unit_preferences.set_current_unit("Latitude", "deg")
            self._o.root.unit_preferences.set_current_unit("Longitude", "deg")
            self._o.root.unit_preferences.set_current_unit("Distance", "km")
            self._o.root.unit_preferences.set_current_unit("Angle", "deg")

            rptComparer = None
            rptComparer = ReportComparison(self._o.root.unit_preferences)
            rptComparer.AddReport(self._o, '"LLA Position"')

            point: "List[float]"

            for point in self._llaPoints:
                copy: "List[float]" = Array.Create(Array.Length(point))
                Array.CopyTo(point, copy, 0)
                copy[0] = copy[0] + self._increment
                d(self, copy)

            rptComparer.TakeOMSnapshot(self._o.root)

            self._pb.remove_all_points()

            self._o.root.execute_command("SetUnits / km Latitude deg Longitude deg")

            def action1(point: "List[float]"):
                utcg: str = self._o.root.conversion_utility.convert_date(
                    "EpSec", "UTCG", Double.ToString(((point[0] + self._increment)))
                )
                if posTypeStr == "AddCustomReferencePoint":
                    if not self._bPositionOnly:
                        s: str = String.Format(
                            (
                                ((("SetPosition {0} " + '"') + "Facility/Facility1 Body") + '"')
                                + ' "{1}" {2} {3} {4} {5} {6} {7}'
                            ),
                            self._o.path,
                            utcg,
                            point[1],
                            point[2],
                            point[3],
                            point[4],
                            point[5],
                            point[6],
                        )
                        self._o.root.execute_command(s)

                    else:
                        s: str = String.Format(
                            (((("SetPosition {0} " + '"') + "Facility/Facility1 Body") + '"') + ' "{1}" {2} {3} {4}'),
                            self._o.path,
                            utcg,
                            point[1],
                            point[2],
                            point[3],
                        )
                        self._o.root.execute_command(s)

                elif posTypeStr == "UTM":
                    if not self._bPositionOnly:
                        self._o.root.execute_command(
                            String.Format(
                                (("SetPosition {0} " + posTypeStr) + ' "{1}" 18S 523.222 3706.636 0.0 0.0 0.0 0.0'),
                                self._o.path,
                                utcg,
                            )
                        )

                    else:
                        self._o.root.execute_command(
                            String.Format(
                                (("SetPosition {0} " + posTypeStr) + ' "{1}" 18S 523.222 3706.636 0.0'),
                                self._o.path,
                                utcg,
                            )
                        )

                else:
                    if not self._bPositionOnly:
                        self._o.root.execute_command(
                            String.Format(
                                (("SetPosition {0} " + posTypeStr) + ' "{1}" {2} {3} {4} {5} {6} {7}'),
                                self._o.path,
                                utcg,
                                point[1],
                                point[2],
                                point[3],
                                point[4],
                                point[5],
                                point[6],
                            )
                        )

                    else:
                        self._o.root.execute_command(
                            String.Format(
                                (("SetPosition {0} " + posTypeStr) + ' "{1}" {2} {3} {4}'),
                                self._o.path,
                                utcg,
                                point[1],
                                point[2],
                                point[3],
                            )
                        )

            Array.ForEach(self._llaPoints, action1)

            rptComparer.TakeConnectSnapshot(self._o.root)

            rptComparer.CompareReportSnapshots()

            self._increment = self._increment + (
                (60 * 2) * 60
            )  # next batch of points will be added with the 2 hours increment

            self._pb.remove_all_points()

    def AddLLAPoint(self, template, point: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.lla.add(point[0], point[1], point[2], point[3], point[4], point[5], point[6])
            with pytest.raises(Exception):
                ptBuilder.lla.add("bogus", point[1], point[2], point[3], point[4], point[5], point[6])

        else:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.lla.add_position(point[0], point[1], point[2], point[3])
            with pytest.raises(Exception):
                ptBuilder.lla.add_position("bogus", point[1], point[2], point[3])

    def AddAGL_LLAPoint(self, template, point: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.agl_lla.add(point[0], point[1], point[2], point[3], point[4], point[5], point[6])
            with pytest.raises(Exception):
                ptBuilder.agl_lla.add("bogus", point[1], point[2], point[3], point[4], point[5], point[6])

        else:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.agl_lla.add_position(point[0], point[1], point[2], point[3])
            with pytest.raises(Exception):
                ptBuilder.agl_lla.add_position("bogus", point[1], point[2], point[3])

    def AddLLAHPSPoint(self, template, point: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.llahps.add(point[0], point[1], point[2], point[3], point[4], point[5], point[6])
            with pytest.raises(Exception):
                ptBuilder.llahps.add("bogus", point[1], point[2], point[3], point[4], point[5], point[6])

    def AddMSL_LLAPoint(self, template, point: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.msl_lla.add(point[0], point[1], point[2], point[3], point[4], point[5], point[6])
            with pytest.raises(Exception):
                ptBuilder.msl_lla.add("bogus", point[1], point[2], point[3], point[4], point[5], point[6])

        else:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.msl_lla.add_position(point[0], point[1], point[2], point[3])
            with pytest.raises(Exception):
                ptBuilder.msl_lla.add_position("bogus", point[1], point[2], point[3])

    def AddB1950Point(self, template, xyz: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.b1950.add(xyz[0], xyz[1], xyz[2], xyz[3], xyz[4], xyz[5], xyz[6])
            with pytest.raises(Exception):
                ptBuilder.b1950.add("bogus", xyz[1], xyz[2], xyz[3], xyz[4], xyz[5], xyz[6])

        else:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.b1950.add_position(xyz[0], xyz[1], xyz[2], xyz[3])
            with pytest.raises(Exception):
                ptBuilder.b1950.add_position("bogus", xyz[1], xyz[2], xyz[3])

    def AddCustomReferencePoint(self, template, xyz: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.get_points_in_frame("Facility/Facility1 Body").add(
                xyz[0], xyz[1], xyz[2], xyz[3], xyz[4], xyz[5], xyz[6]
            )
            with pytest.raises(Exception):
                ptBuilder.get_points_in_frame("Facility/Facility1 Body").add(
                    "bogus", xyz[1], xyz[2], xyz[3], xyz[4], xyz[5], xyz[6]
                )

    def AddECFPoint(self, template, xyz: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.ecf.add(xyz[0], xyz[1], xyz[2], xyz[3], xyz[4], xyz[5], xyz[6])
            with pytest.raises(Exception):
                ptBuilder.ecf.add("bogus", xyz[1], xyz[2], xyz[3], xyz[4], xyz[5], xyz[6])

        else:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.ecf.add_position(xyz[0], xyz[1], xyz[2], xyz[3])
            with pytest.raises(Exception):
                ptBuilder.ecf.add_position("bogus", xyz[1], xyz[2], xyz[3])

    def AddECIPoint(self, template, xyz: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.eci.add(xyz[0], xyz[1], xyz[2], xyz[3], xyz[4], xyz[5], xyz[6])
            with pytest.raises(Exception):
                ptBuilder.eci.add("bogus", xyz[1], xyz[2], xyz[3], xyz[4], xyz[5], xyz[6])

        else:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.eci.add_position(xyz[0], xyz[1], xyz[2], xyz[3])
            with pytest.raises(Exception):
                ptBuilder.eci.add_position("bogus", xyz[1], xyz[2], xyz[3])

    def AddUTMPoint(self, template, xyz: "List[float]"):
        if not template.UsePositionOnly:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.utm.add(xyz[0], "18S", 523.222, 3706.636, 0.0, 0.0, 0.0, 0.0)
            with pytest.raises(Exception):
                ptBuilder.utm.add("bogus", "18S", 523.222, 3706.636, 0.0, 0.0, 0.0, 0.0)

        else:
            ptBuilder: "VehicleRealtimePointBuilder" = template.PointBuilder
            ptBuilder.utm.add_position(xyz[0], "18S", 523.222, 3706.636, 0.0)
            with pytest.raises(Exception):
                ptBuilder.utm.add_position("bogus", "18S", 523.222, 3706.636, 0.0)

    def test_RealtimePointBuilders(self):
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Realtime_Scenario")
        sc: "Scenario" = Scenario(TestBase.Application.current_scenario)
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        sc.set_time_period("1 Jul 2007 12:00", "1 Jul 2007 18:00")
        fac: "IStkObject" = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "Facility1")
        newsat: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "RealtimeSatellite1"
        )
        sat: "Satellite" = clr.CastAs(newsat, Satellite)
        Assert.assertIsNotNone(sat)
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)
        Assert.assertEqual(sat.propagator_type, VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)

        rtp: "VehiclePropagatorRealtime" = clr.CastAs(sat.propagator, VehiclePropagatorRealtime)
        Assert.assertIsNotNone(rtp)

        rtp.time_step = 600
        rtp.timeout_gap = 3600
        rtp.duration.look_ahead = 3600
        rtp.duration.look_behind = 3600
        rtp.look_ahead_propagator = LOOK_AHEAD_PROPAGATOR.J2_PERTURBATION
        rtp.propagate()
        pb: "VehicleRealtimePointBuilder" = (clr.CastAs(sat.propagator, VehiclePropagatorRealtime)).point_builder
        Assert.assertIsNotNone(pb)
        if not TestBase.NoGraphicsMode:
            sat.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)
            gfxAttributesRealtime: "VehicleGraphics2DAttributesRealtime" = VehicleGraphics2DAttributesRealtime(
                sat.graphics.attributes
            )
            gfxAttributesRealtime.history.is_visible = True
            gfxAttributesRealtime.spline.is_visible = True

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                sat.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_REALTIME)

        # --------------------------------------------------------------
        # Testing the point builders and make sure
        # they produce adequate results
        # --------------------------------------------------------------
        llaPoints: "List[List[float]]" = [
            [1200, 33.228, -124.048, 5499.893923, 0.020872, -0.019911, 1.894301],
            [1800, 44.334, -136.636, 6519.040995, 0.016347, -0.022419, 1.498066],
            [2400, 52.975, -151.364, 7293.946325, 0.012494, -0.027073, 1.084131],
            [3000, 59.276, -169.508, 7819.339978, 0.008404, -0.033665, 0.667509],
            [3600, 62.874, 168.322, 8095.11196, 0.003422, -0.039799, 0.252113],
            [4200, 22.363, 61.824, 4543.473336, -0.025588, -0.019411, -2.165989],
            [4800, -4.7, -142.655, 2564.433222, 0.039046, -0.023753, 2.371868],
            [5400, 62.379, 127.69, 8058.434558, 0.004535, -0.038806, 0.338061],
            [6000, 25.456, 18.716, 4808.633112, -0.024201, -0.019408, -2.099771],
            [6600, -9.712, 174.885, 2271.550874, 0.041627, -0.025567, 2.33665],
        ]
        template = None

        template = EarlyBoundTests.RealtimeBuilderTemplate(newsat, llaPoints, False)
        template.Invoke(self.AddLLAPoint, "LLA")
        template.Invoke(self.AddAGL_LLAPoint, "AGL_LLA")
        template.Invoke(self.AddMSL_LLAPoint, "MSL_LLA")
        template.Invoke(self.AddLLAHPSPoint, "LLAHPS")
        template.Invoke(self.AddUTMPoint, "UTM")

        template = EarlyBoundTests.RealtimeBuilderTemplate(newsat, llaPoints, True)
        template.Invoke(self.AddAGL_LLAPoint, "AGL_LLA")
        template.Invoke(self.AddLLAPoint, "LLA")
        template.Invoke(self.AddMSL_LLAPoint, "MSL_LLA")
        # Requires all six elements to be specified, skipping...
        # template.Invoke(AddLLAHPSPoint, "LLAHPS");
        template.Invoke(self.AddUTMPoint, "UTM")

        xyzPoints: "List[List[float]]" = [
            [1200, -5566.02923, -8237.014508, 6488.958938, -2.424759, 2.582109, 4.650424],
            [1800, -6712.154343, -6339.3299, 8990.466501, -1.391726, 3.654763, 3.676547],
            [2400, -7233.04941, -3949.429322, 10892.152493, -0.3504, 4.245331, 2.660486],
            [3000, -7140.26682, -1322.315482, 12181.482087, 0.648506, 4.459348, 1.638093],
            [3600, -6470.13082, 1337.293606, 12858.243496, 1.570127, 4.361812, 0.618708],
            [4200, 4770.515327, 8905.853116, 4140.319943, 2.945003, -1.751083, -5.32099],
            [4800, -7085.557338, -5406.484592, -729.254644, -4.515713, 1.201949, 5.850651],
            [5400, -4096.893913, 5302.653917, 12768.240318, 4.115019, 2.097187, 0.829621],
            [6000, 9569.968235, 3242.215983, 4791.616571, 1.220801, -3.200114, -5.157094],
            [6600, -8492.358879, 760.174946, -1452.106907, -3.005724, 4.088879, 5.770694],
        ]
        template = EarlyBoundTests.RealtimeBuilderTemplate(newsat, xyzPoints, False)
        template.Invoke(self.AddECFPoint, "ECF")
        template.Invoke(self.AddECIPoint, "ECI")
        template.Invoke(self.AddB1950Point, "B1950")

        template = EarlyBoundTests.RealtimeBuilderTemplate(newsat, xyzPoints, True)
        template.Invoke(self.AddECFPoint, "ECF")
        template.Invoke(self.AddECIPoint, "ECI")
        template.Invoke(self.AddB1950Point, "B1950")

        template = EarlyBoundTests.RealtimeBuilderTemplate(newsat, xyzPoints, False)
        template.Invoke(self.AddCustomReferencePoint, "AddCustomReferencePoint")

    # endregion

    # region SEET_Environment
    @category("SEET")
    def test_SEET_Environment(self):
        SEETHelper.TestEnvironment(EarlyBoundTests.AG_SAT.space_environment)

    # endregion

    # region SEET_Thermal
    @category("SEET")
    def test_SEET_Thermal(self):
        SEETHelper.TestThermal(EarlyBoundTests.AG_SAT.space_environment)

    # endregion

    # region SEET_ParticleFlux
    @category("SEET")
    def test_SEET_ParticleFlux(self):
        SEETHelper.TestParticleFlux(EarlyBoundTests.AG_SAT.space_environment)

    # endregion

    # region SEET_Radiation
    @category("SEET")
    def test_SEET_Radiation(self):
        SEETHelper.TestRadiation(EarlyBoundTests.AG_SAT.space_environment)

    # endregion

    # region SEET_Environment_2D
    @category("SEET")
    @category("Graphics Tests")
    def test_SEET_Environment_2D(self):
        SEETHelper.TestEnvironment_2D(
            EarlyBoundTests.AG_SAT.space_environment,
            EarlyBoundTests.AG_SAT.graphics.saa,
            EarlyBoundTests.AG_SAT.graphics_3d.saa,
        )

    # endregion

    # region SEET_Computations
    @category("SEET")
    def test_SEET_Computations(self):
        seetSat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "SEET_SAT"), Satellite
        )
        seetSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twobody: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(seetSat.propagator)
        # OrbitStateClassical classical =
        #    (OrbitStateClassical)twobody.InitialState.Representation.ConvertTo(AgEOrbitStateType.CLASSICAL);
        # classical.SizeShapeType = AgEClassicalSizeShape.SIZE_SHAPE_PERIOD;
        # ClassicalSizeShapePeriod period = (ClassicalSizeShapePeriod)classical.SizeShape;
        # period.Eccentricity = 0.01;
        # period.Period = 10000;
        # twobody.InitialState.Representation.Assign(classical);
        twobody.propagate()

        startTime: typing.Any = (clr.CastAs(TestBase.Application.current_scenario, Scenario)).start_time
        stopTime: typing.Any = (clr.CastAs(TestBase.Application.current_scenario, Scenario)).stop_time
        SEETHelper.TestComputations(clr.CastAs(seetSat, IStkObject), seetSat.space_environment, startTime, stopTime)

    # endregion

    # region HPOP Third Body Grativity

    @category("BUG60013: Lunar HPOP satellite cant add earth as a third body if it gets removed")
    def test_AddEarthToLunarSatelliteThirdBodyGravity(self):
        satelliteName: str = "Satellite12345678"

        def action2():
            sat: "Satellite" = Satellite(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.SATELLITE, satelliteName, "Moon"
                )
            )
            # Set HPOP as the satellite's propagator
            sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
            propagator: "VehiclePropagatorHPOP" = VehiclePropagatorHPOP(sat.propagator)
            propagator.force_model.third_body_gravity.remove_all()
            Assert.assertEqual(0, propagator.force_model.third_body_gravity.count)
            # Get a list of available third body names
            thirdBodyNames: "List[typing.Any]" = CSToJavaArrayHelper.ToOneDimensionalObjectArray(
                propagator.force_model.third_body_gravity.available_third_body_names
            )
            Array.Sort(thirdBodyNames)
            index: int = Array.BinarySearch(thirdBodyNames, "Earth")
            Assert.assertTrue((index >= 0))
            index = Array.BinarySearch(thirdBodyNames, "Moon")
            Assert.assertTrue((index < 0))
            # Verify that Earth can be added to a list of third body gravities
            # for lunar satellite
            propagator.force_model.third_body_gravity.add_third_body("Earth")
            Assert.assertEqual(1, propagator.force_model.third_body_gravity.count)

        def finalizer1():
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, satelliteName)

        #        #             * Verifies that the list of third body gravities contains Earth for lunar satellite.        #             *
        TryCatchAssertBlock.DoActionRunFinalize(action2, finalizer1)

    @category("BUG60013: Lunar HPOP satellite cant add earth as a third body if it gets removed")
    def test_AddMoonToGeoSatelliteThirdBodyGravity(self):
        satelliteName: str = "Satellite12345678"

        def action3():
            sat: "Satellite" = Satellite(
                TestBase.Application.current_scenario.children.new_on_central_body(
                    STK_OBJECT_TYPE.SATELLITE, satelliteName, "Earth"
                )
            )
            # Set HPOP as the satellite's propagator
            sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)
            propagator: "VehiclePropagatorHPOP" = VehiclePropagatorHPOP(sat.propagator)
            propagator.force_model.third_body_gravity.remove_all()
            Assert.assertEqual(0, propagator.force_model.third_body_gravity.count)
            # Get a list of available third body names
            thirdBodyNames: "List[typing.Any]" = CSToJavaArrayHelper.ToOneDimensionalObjectArray(
                propagator.force_model.third_body_gravity.available_third_body_names
            )
            Array.Sort(thirdBodyNames)
            index: int = Array.BinarySearch(thirdBodyNames, "Moon")
            Assert.assertTrue((index >= 0))
            index = Array.BinarySearch(thirdBodyNames, "Earth")
            Assert.assertTrue((index < 0))
            # Verify that Earth can be added to a list of third body gravities
            # for lunar satellite
            propagator.force_model.third_body_gravity.add_third_body("Moon")
            Assert.assertEqual(1, propagator.force_model.third_body_gravity.count)

        def finalizer2():
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, satelliteName)

        #        #             * Verifies that the list of third body gravities contains Moon for geocentric satellite.        #             *
        TryCatchAssertBlock.DoActionRunFinalize(action3, finalizer2)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()
        with pytest.raises(Exception, match=RegexSubstringMatch("obsolete")):
            helper.Run(EarlyBoundTests.AG_SAT.radar_clutter_map)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_SAT.radar_cross_section)

    # endregion
