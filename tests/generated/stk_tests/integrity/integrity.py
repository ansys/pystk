import pytest
from test_util import *
from assertion_harness import *
from logger import *
from report_comparison import *
from parameterized import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


@category("EarlyBoundTests")
# [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
class Propagation(TestBase):
    def __init__(self, *args, **kwargs):
        super(Propagation, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        Console.WriteLine("Integrity - Propagation - OneTimeSetUp")
        TestBase.Initialize()
        Propagation.InitHelper()

    @staticmethod
    def InitHelper():
        TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])
        Propagation.AG_AC = Aircraft(TestBase.Application.current_scenario.children["Boing737"])
        Propagation.AG_SH = Ship(TestBase.Application.current_scenario.children["Ship1"])
        Propagation.AG_MS = Missile(TestBase.Application.current_scenario.children["Missile1"])
        satelliteName: str = "Satellite_BUG76220"
        if TestBase.Application.current_scenario.children.contains(STKObjectType.SATELLITE, satelliteName):
            TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, satelliteName)

        # Create a test satellite
        Propagation._SGP_SAT = Satellite(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, satelliteName)
        )
        Propagation._SGP_SAT.set_propagator_type(PropagatorType.SGP4)
        prop: "PropagatorSGP4" = PropagatorSGP4(Propagation._SGP_SAT.propagator)
        prop.automatic_update_enabled = False

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        Propagation.AG_SAT = None
        Propagation.AG_AC = None
        Propagation.AG_SH = None
        Propagation.AG_MS = None
        Propagation._SGP_SAT = None
        TestBase.Uninitialize()
        Console.WriteLine("Integrity - Propagation - OneTimeTearDown")

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    AG_AC: "Aircraft" = None
    AG_SH: "Ship" = None
    AG_MS: "Missile" = None
    _SGP_SAT: "Satellite" = None
    # endregion

    # region TLE
    def DumpSeg(self, seg: "PropagatorSGP4Segment"):
        Console.WriteLine(("seg.ArgOfPerigee = " + str(seg.argument_of_periapsis)))
        Console.WriteLine(("seg.BStar = " + str(seg.bstar)))
        Console.WriteLine(("seg.Classification = " + seg.classification))
        Console.WriteLine(("seg.Eccentricity = " + str(seg.eccentricity)))
        Console.WriteLine(("seg.Enabled = " + str(seg.enabled)))
        Console.WriteLine(("seg.Epoch = " + str(seg.epoch)))
        Console.WriteLine(("seg.Inclination = " + str(seg.inclination)))
        Console.WriteLine(("seg.IntlDesignator = " + seg.international_designator))
        Console.WriteLine(("seg.MeanAnomaly = " + str(seg.mean_anomaly)))
        Console.WriteLine(("seg.MeanMotion = " + str(seg.mean_motion)))
        Console.WriteLine(("seg.MeanMotionDot = " + str(seg.mean_motion_dot)))
        Console.WriteLine(("seg.MotionDotDot = " + str(seg.motion_dot_dot)))
        Console.WriteLine(("seg.RAAN = " + str(seg.right_ascension_ascending_node)))
        Console.WriteLine(("seg.Range = " + str(seg.range)))
        Console.WriteLine(("seg.RevNumber = " + str(seg.revolution_number)))
        Console.WriteLine(("seg.SSCNum = " + seg.ssc_number))
        Console.WriteLine(("seg.SwitchingMethod = " + str(seg.switching_method)))
        Console.WriteLine(("seg.SwitchTime = " + str(seg.switch_time)))

    def AddAndConfigureSeg1(self, segments: "PropagatorSGP4SegmentCollection"):
        seg: "PropagatorSGP4Segment" = segments.add_segment()
        seg.argument_of_periapsis = 286.2668
        seg.bstar = 9.2648e-05
        seg.classification = "U"
        seg.eccentricity = 0.0003541
        seg.enabled = True
        seg.epoch = 13220.53564935
        seg.inclination = 51.6491
        seg.international_designator = "98067A "
        seg.mean_anomaly = 170.2641
        seg.mean_motion = 0.06459207129166666
        seg.right_ascension_ascending_node = 208.9552
        # READ ONLY  seg.Range = 0.0;
        seg.revolution_number = 84282
        seg.switching_method = PropagatorSGP4SwitchMethod.OVERRIDE  # so SwitchTime can be set
        seg.switch_time = "8 Aug 2013 12:51:20.104"
        seg.switching_method = PropagatorSGP4SwitchMethod.EPOCH

    def AddAndConfigureSeg2(self, segments: "PropagatorSGP4SegmentCollection"):
        seg: "PropagatorSGP4Segment" = segments.add_segment()
        seg.argument_of_periapsis = 287.4472
        seg.bstar = 9.3124e-05
        seg.classification = "U"
        seg.eccentricity = 0.0003569
        seg.enabled = True
        seg.epoch = 13220.70972222
        seg.inclination = 51.6492
        seg.international_designator = "98067A "
        seg.mean_anomaly = 61.1837
        seg.mean_motion = 0.06459215375
        seg.right_ascension_ascending_node = 208.0924
        # READ ONLY  seg.Range = 0.0;
        seg.revolution_number = 84284
        seg.switching_method = PropagatorSGP4SwitchMethod.OVERRIDE  # so SwitchTime can be set
        seg.switch_time = "8 Aug 2013 17:02:00.000"
        seg.switching_method = PropagatorSGP4SwitchMethod.EPOCH

    def AddAndConfigureSeg3(self, segments: "PropagatorSGP4SegmentCollection"):
        seg: "PropagatorSGP4Segment" = segments.add_segment()
        seg.argument_of_periapsis = 287.7002
        seg.bstar = 9.2805e-05
        seg.classification = "U"
        seg.eccentricity = 0.000361
        seg.enabled = True
        seg.epoch = 13220.7756713
        seg.inclination = 51.6489
        seg.international_designator = "98067A "
        seg.mean_anomaly = 69.2197
        seg.mean_motion = 0.06459217875
        seg.right_ascension_ascending_node = 207.7649
        # READ ONLY seg.Range = 0.0;
        seg.revolution_number = 84285
        seg.switching_method = PropagatorSGP4SwitchMethod.OVERRIDE  # so SwitchTime can be set
        seg.switch_time = "8 Aug 2013 18:36:58.000"
        seg.switching_method = PropagatorSGP4SwitchMethod.EPOCH

    def CompareTleEphemeris(self, sat1: "Satellite", sat2: "Satellite", startTime: typing.Any, stopTime: typing.Any):
        elements = ["x", "y", "z"]

        oGroup1: "DataProviderGroup" = DataProviderGroup(
            (clr.CastAs(sat1, IStkObject)).data_providers["Cartesian Position"]
        )
        oProvider1: "IDataProvider" = IDataProvider(oGroup1.group["Fixed"])
        result1: "DataProviderResult" = (DataProviderTimeVarying(oProvider1)).execute_elements(
            startTime, stopTime, 60, elements
        )

        oGroup2: "DataProviderGroup" = DataProviderGroup(
            (clr.CastAs(sat2, IStkObject)).data_providers["Cartesian Position"]
        )
        oProvider2: "IDataProvider" = IDataProvider(oGroup2.group["Fixed"])
        result2: "DataProviderResult" = (DataProviderTimeVarying(oProvider2)).execute_elements(
            startTime, stopTime, 60, elements
        )

        i: int = 0
        while i < result1.data_sets.count:
            vals1 = result1.data_sets[i].get_values()
            vals2 = result2.data_sets[i].get_values()
            Assert.assertEqual(Array.Length(vals1), Array.Length(vals2))

            j: int = 0
            while j < Array.Length(vals1):
                Console.WriteLine(((str(vals1[j]) + "     ") + str(vals2[j])))
                Assert.assertAlmostEqual(float(vals1[j]), float(vals2[j]), delta=0.001)

                j += 1

            i += 1

    @parameterized.expand(
        [
            ("tle1.tle", "single"),
            ("tle12.tle", "2 segs"),
            ("tle12.tle", "2 segs reversed"),
            ("tle13.tle", "3 segs remove 2nd"),
        ]
    )
    def test_TLE(self, tleFile: str, testCase: str):
        # Setup
        satName: str
        # Setup
        for satName in ["tle-25544", "tle-25544-viaOM"]:
            if TestBase.Application.current_scenario.children.contains(STKObjectType.SATELLITE, satName):
                TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, satName)

        # Create a satellite by loading a TLE file, then propagate it.
        TestBase.Application.execute_command(
            (
                ("ImportTLEFile * " + TestBase.DoubleQuoted(TestBase.GetScenarioFile(tleFile)))
                + " SSCNumber 25544 Merge On"
            )
        )
        sat1: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["tle-25544"], Satellite)
        sat1.set_propagator_type(PropagatorType.SGP4)
        sgp4_1: "PropagatorSGP4" = clr.CastAs(sat1.propagator, PropagatorSGP4)
        sgp4_1.ephemeris_interval.set_explicit_interval("8 Aug 2013 12:51:21", "8 Aug 2013 14:24:14")
        sgp4_1.step = 60
        sgp4_1.propagate()

        # Create an SGP4 satellite, set the segment properties, and propagate it.
        sat2: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "tle-25544-viaOM"), Satellite
        )
        sat2.set_propagator_type(PropagatorType.SGP4)
        sgp4_2: "PropagatorSGP4" = clr.CastAs(sat2.propagator, PropagatorSGP4)
        sgp4_2.ephemeris_interval.set_explicit_interval(
            sgp4_1.ephemeris_interval.find_start_time(), sgp4_1.ephemeris_interval.find_stop_time()
        )
        sgp4_2.step = sgp4_1.step
        sgp4_2.segments.ssc_number = "25544"
        if testCase == "single":
            self.AddAndConfigureSeg1(sgp4_2.segments)

        elif testCase == "2 segs":
            self.AddAndConfigureSeg1(sgp4_2.segments)
            self.AddAndConfigureSeg2(sgp4_2.segments)

        elif testCase == "2 segs reversed":
            self.AddAndConfigureSeg2(sgp4_2.segments)
            self.AddAndConfigureSeg1(sgp4_2.segments)

        elif testCase == "3 segs remove 2nd":
            self.AddAndConfigureSeg1(sgp4_2.segments)
            self.AddAndConfigureSeg2(sgp4_2.segments)
            self.AddAndConfigureSeg3(sgp4_2.segments)
            sgp4_2.propagate()
            sgp4_2.segments.remove_segment(1)  # Remove the second seg

        else:
            Assert.fail("TLE tests: Bad testcase name")

        sgp4_2.propagate()

        self.CompareTleEphemeris(
            sat1, sat2, sgp4_2.ephemeris_interval.find_start_time(), sgp4_2.ephemeris_interval.find_stop_time()
        )

    # endregion

    # region STKExternal
    def test_STKExternal(self):
        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Propagator Inputs"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.STK_EXTERNAL)
        ext: "PropagatorStkExternal" = PropagatorStkExternal(Propagation.AG_SAT.propagator)
        strPath: str = TestBase.GetScenarioFile("TestEph.e")
        ext.filename = strPath
        ext.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command((('SetStateFile */Satellite/Satellite1 "' + strPath) + '"'))
        TestBase.Application.execute_command(
            'Propagate */Satellite/Satellite1 "1 Nov 2000 00:00:00.00" "1 Nov 2000 08:00:00.00"'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region Ballistic
    def test_Ballistic(self):
        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(
            clr.CastAs(Propagation.AG_MS, IStkObject),
            '"Euler Angles" "1 Oct 1999 00:00:00" "1 Oct 1999 01:00:00" 600.0',
            0.01,
        )
        ComparisionUtility.AddReport2(
            clr.CastAs(Propagation.AG_MS, IStkObject),
            '"LLA Position" "1 oct 1999 00:00:00" "1 oct 1999 01:00:00" 600.0',
            0.01,
        )

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeod 55.0 100.0 1.5 TOF 9000.0 ImLatGeod 12.0 5.0 0.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory: "PropagatorBallistic" = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.DETIC)
        launch: "LaunchVehicleLocationDetic" = LaunchVehicleLocationDetic(trajectory.launch)
        launch.latitude = 55.0
        launch.longitude = 100.0
        launch.altitude = 1.5
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        impactloc: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        impactloc.set_launch_control_type(VehicleLaunchControl.FIXED_TIME_OF_FLIGHT)
        launchcontrol3: "LaunchVehicleControlFixedTimeOfFlight" = LaunchVehicleControlFixedTimeOfFlight(
            impactloc.launch_control
        )
        launchcontrol3.time_of_flight = 9000.0
        impactloc.set_impact_type(VehicleImpact.IMPACT_LOCATION_DETIC)
        impact: "VehicleImpactLocationDetic" = VehicleImpactLocationDetic(impactloc.impact)
        impact.latitude = 12.0
        impact.longitude = 5.0
        impact.altitude = 0.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeod 55.0 100.0 1.5 TOF 9000.0 ImLatGeoc 12.0 5.0 6400000.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.DETIC)
        launch10: "LaunchVehicleLocationDetic" = LaunchVehicleLocationDetic(trajectory.launch)
        launch10.latitude = 55.0
        launch10.longitude = 100.0
        launch10.altitude = 1.5
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        impactloc33: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        impactloc33.set_launch_control_type(VehicleLaunchControl.FIXED_TIME_OF_FLIGHT)
        launchcontrol2: "LaunchVehicleControlFixedTimeOfFlight" = LaunchVehicleControlFixedTimeOfFlight(
            impactloc33.launch_control
        )
        launchcontrol2.time_of_flight = 9000.0
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        impactloc33.set_impact_type(VehicleImpact.IMPACT_LOCATION_CENTRIC)
        impact2: "VehicleImpactLocationCentric" = VehicleImpactLocationCentric(impactloc33.impact)
        impact2.latitude = 12.0
        impact2.longitude = 5.0
        impact2.radius = 6400000.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeod 55.0 100.0 1.5 DeltaV 9500.0 ImLatGeod 12.0 5.0 0.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.DETIC)
        launch12: "LaunchVehicleLocationDetic" = LaunchVehicleLocationDetic(trajectory.launch)
        launch12.latitude = 55.0
        launch12.longitude = 100.0
        launch12.altitude = 1.5
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        impactloc2: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        impactloc.set_launch_control_type(VehicleLaunchControl.FIXED_DELTA_V)
        launchcontrol: "LaunchVehicleControlFixedDeltaV" = LaunchVehicleControlFixedDeltaV(impactloc.launch_control)
        launchcontrol.delta_v = 9500.0
        impactloc2.set_impact_type(VehicleImpact.IMPACT_LOCATION_DETIC)
        impact0: "VehicleImpactLocationDetic" = VehicleImpactLocationDetic(impactloc.impact)
        impact0.latitude = 12.0
        impact0.longitude = 5.0
        impact0.altitude = 0.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeod 55.0 100.0 1.5 DeltaV 9500.0 ImLatGeoc 12.0 5.0 6400000.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.DETIC)
        launch9: "LaunchVehicleLocationDetic" = LaunchVehicleLocationDetic(trajectory.launch)
        launch9.latitude = 55.0
        launch9.longitude = 100.0
        launch9.altitude = 1.5
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        locpoint12: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        locpoint12.set_launch_control_type(VehicleLaunchControl.FIXED_DELTA_V)
        launchcontrol8: "LaunchVehicleControlFixedDeltaV" = LaunchVehicleControlFixedDeltaV(locpoint12.launch_control)
        launchcontrol8.delta_v = 9500.0
        locpoint12.set_impact_type(VehicleImpact.IMPACT_LOCATION_CENTRIC)
        impact3: "VehicleImpactLocationCentric" = VehicleImpactLocationCentric(locpoint12.impact)
        impact3.latitude = 12.0
        impact3.longitude = 5.0
        impact3.radius = 6400000.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeod 55.0 100.0 1.5 DeltaV 9500.0 LaunchAzEl 20.0 45.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.DETIC)
        launch2: "LaunchVehicleLocationDetic" = LaunchVehicleLocationDetic(trajectory.launch)
        launch2.latitude = 55.0
        launch2.longitude = 100.0
        launch2.altitude = 1.5
        trajectory.set_impact_location_type(VehicleImpactLocation.LAUNCH_AZ_EL)
        impactloc4: "VehicleImpactLocationLaunchAzEl" = VehicleImpactLocationLaunchAzEl(trajectory.impact_location)
        impactloc4.delta_v = 9500.0
        impactloc4.azimuth = 20.0
        impactloc4.elevation = 45.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeod 55.0 100.0 1.5 ApogeeAlt  2000000.0 ImLatGeod 12.0 5.0 0.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.DETIC)
        launch3: "LaunchVehicleLocationDetic" = LaunchVehicleLocationDetic(trajectory.launch)
        launch3.latitude = 55.0
        launch3.longitude = 100.0
        launch3.altitude = 1.5
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        impactloc1: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        impactloc1.set_launch_control_type(VehicleLaunchControl.FIXED_APOGEE_ALTITUDE)
        launchcontrol5: "LaunchVehicleControlFixedApogeeAltitude" = LaunchVehicleControlFixedApogeeAltitude(
            impactloc1.launch_control
        )
        launchcontrol5.apogee_altitude = 2000000.0
        impactloc1.set_impact_type(VehicleImpact.IMPACT_LOCATION_DETIC)
        impact8: "VehicleImpactLocationDetic" = VehicleImpactLocationDetic(impactloc1.impact)
        impact8.latitude = 12.0
        impact8.longitude = 5.0
        impact8.altitude = 0.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeod 55.0 100.0 1.5 ApogeeAlt  2000000.0 ImLatGeoc 12.0 5.0 6400000.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.DETIC)
        launch4: "LaunchVehicleLocationDetic" = LaunchVehicleLocationDetic(trajectory.launch)
        launch4.latitude = 55.0
        launch4.longitude = 100.0
        launch4.altitude = 1.5
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        locpoint00: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        locpoint00.set_launch_control_type(VehicleLaunchControl.FIXED_APOGEE_ALTITUDE)
        launchcontrol7: "LaunchVehicleControlFixedApogeeAltitude" = LaunchVehicleControlFixedApogeeAltitude(
            locpoint00.launch_control
        )
        launchcontrol7.apogee_altitude = 2000000.0
        locpoint00.set_impact_type(VehicleImpact.IMPACT_LOCATION_CENTRIC)
        impact6: "VehicleImpactLocationCentric" = VehicleImpactLocationCentric(locpoint00.impact)
        impact6.latitude = 12.0
        impact6.longitude = 5.0
        impact6.radius = 6400000.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeoc 55.0 100.0 6400000.0 TOF 9000.0 ImLatGeod 12.0 5.0 0.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.CENTRIC)
        launch5: "LaunchVehicleLocationCentric" = LaunchVehicleLocationCentric(trajectory.launch)
        launch5.latitude = 55.0
        launch5.longitude = 100.0
        launch5.radius = 6400000.0
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        locpoint14: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        locpoint14.set_launch_control_type(VehicleLaunchControl.FIXED_TIME_OF_FLIGHT)
        launchcontrol6: "LaunchVehicleControlFixedTimeOfFlight" = LaunchVehicleControlFixedTimeOfFlight(
            locpoint14.launch_control
        )
        launchcontrol6.time_of_flight = 9000.0
        locpoint14.set_impact_type(VehicleImpact.IMPACT_LOCATION_DETIC)
        impact1: "VehicleImpactLocationDetic" = VehicleImpactLocationDetic(locpoint14.impact)
        impact1.latitude = 12.0
        impact1.longitude = 5.0
        impact1.altitude = 0.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeoc 55.0 100.0 6400000.0 TOF 9000.0 ImLatGeoc 12.0 5.0 6400000.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.CENTRIC)
        launch6: "LaunchVehicleLocationCentric" = LaunchVehicleLocationCentric(trajectory.launch)
        launch6.latitude = 55.0
        launch6.longitude = 100.0
        launch6.radius = 6400000.0
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        locpoint: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        locpoint.set_launch_control_type(VehicleLaunchControl.FIXED_TIME_OF_FLIGHT)
        launchcontrol4: "LaunchVehicleControlFixedTimeOfFlight" = LaunchVehicleControlFixedTimeOfFlight(
            locpoint.launch_control
        )
        launchcontrol4.time_of_flight = 9000.0
        locpoint.set_impact_type(VehicleImpact.IMPACT_LOCATION_CENTRIC)
        impact11: "VehicleImpactLocationCentric" = VehicleImpactLocationCentric(locpoint.impact)
        impact11.latitude = 12.0
        impact11.longitude = 5.0
        impact11.radius = 6400000.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeoc 55.0 100.0 6400000.0 DeltaV 9500.0 ImLatGeod 12.0 5.0 0.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.CENTRIC)
        launch7: "LaunchVehicleLocationCentric" = LaunchVehicleLocationCentric(trajectory.launch)
        launch7.latitude = 55.0
        launch7.longitude = 100.0
        launch7.radius = 6400000.0
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        locpoint15: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        locpoint15.set_launch_control_type(VehicleLaunchControl.FIXED_DELTA_V)
        launchcontrol9: "LaunchVehicleControlFixedDeltaV" = LaunchVehicleControlFixedDeltaV(locpoint15.launch_control)
        launchcontrol9.delta_v = 9500.0
        locpoint15.set_impact_type(VehicleImpact.IMPACT_LOCATION_DETIC)
        impact9: "VehicleImpactLocationDetic" = VehicleImpactLocationDetic(locpoint15.impact)
        impact9.latitude = 12.0
        impact9.longitude = 5.0
        impact9.altitude = 0.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeoc 55.0 100.0 6400000.0 DeltaV 9500.0 ImLatGeoc 12.0 5.0 6400000.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.CENTRIC)
        launch8: "LaunchVehicleLocationCentric" = LaunchVehicleLocationCentric(trajectory.launch)
        launch8.latitude = 55.0
        launch8.longitude = 100.0
        launch8.radius = 6400000.0
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        locp: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        locp.set_launch_control_type(VehicleLaunchControl.FIXED_DELTA_V)
        launchcontrol10: "LaunchVehicleControlFixedDeltaV" = LaunchVehicleControlFixedDeltaV(locp.launch_control)
        launchcontrol10.delta_v = 9500.0
        locp.set_impact_type(VehicleImpact.IMPACT_LOCATION_CENTRIC)
        impact7: "VehicleImpactLocationCentric" = VehicleImpactLocationCentric(locp.impact)
        impact7.latitude = 12.0
        impact7.longitude = 5.0
        impact7.radius = 6400000.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeoc 55.0 100.0 6400000.0 DeltaV 9500.0 LaunchAzEl 20.0 45.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.CENTRIC)
        launch1: "LaunchVehicleLocationCentric" = LaunchVehicleLocationCentric(trajectory.launch)
        launch1.latitude = 55.0
        launch1.longitude = 100.0
        launch1.radius = 6400000.0
        trajectory.set_impact_location_type(VehicleImpactLocation.LAUNCH_AZ_EL)
        impactloc22: "VehicleImpactLocationLaunchAzEl" = VehicleImpactLocationLaunchAzEl(trajectory.impact_location)
        impactloc22.delta_v = 9500.0
        impactloc22.azimuth = 20.0
        impactloc22.elevation = 45.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeoc 55.0 100.0 6400000.0 ApogeeAlt  2000000.0 ImLatGeod 12.0 5.0 0.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.CENTRIC)
        launch11: "LaunchVehicleLocationCentric" = LaunchVehicleLocationCentric(trajectory.launch)
        launch11.latitude = 55.0
        launch11.longitude = 100.0
        launch11.radius = 6400000.0
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        impactloc01: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        impactloc01.set_launch_control_type(0)
        launchcontrol0: "LaunchVehicleControlFixedApogeeAltitude" = LaunchVehicleControlFixedApogeeAltitude(
            impactloc01.launch_control
        )
        launchcontrol0.apogee_altitude = 2000000.0
        impactloc01.set_impact_type(VehicleImpact.IMPACT_LOCATION_DETIC)
        impact4: "VehicleImpactLocationDetic" = VehicleImpactLocationDetic(impactloc01.impact)
        impact4.latitude = 12.0
        impact4.longitude = 5.0
        impact4.altitude = 0.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Missile  */Missile/Missile1 Trajectory "1 oct 1999 00:00:00" 30.0 LnLatGeoc 55.0 100.0 6400000.0 ApogeeAlt  2000000.0 ImLatGeoc 12.0 5.0 6400000.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        Propagation.AG_MS.set_trajectory_type(PropagatorType.BALLISTIC)
        trajectory = PropagatorBallistic(Propagation.AG_MS.trajectory)
        trajectory.ephemeris_interval.set_explicit_interval("1 oct 1999 00:00:00", "1 oct 1999 01:00:00")
        trajectory.step = 30.0
        trajectory.set_launch_type(VehicleLaunch.CENTRIC)
        launch13: "LaunchVehicleLocationCentric" = LaunchVehicleLocationCentric(trajectory.launch)
        launch13.latitude = 55.0
        launch13.longitude = 100.0
        launch13.radius = 6400000.0
        trajectory.set_impact_location_type(VehicleImpactLocation.POINT)
        locpoint1: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(trajectory.impact_location)
        locpoint1.set_launch_control_type(VehicleLaunchControl.FIXED_APOGEE_ALTITUDE)
        launchcontrol1: "LaunchVehicleControlFixedApogeeAltitude" = LaunchVehicleControlFixedApogeeAltitude(
            locpoint1.launch_control
        )
        launchcontrol1.apogee_altitude = 2000000.0
        locpoint1.set_impact_type(VehicleImpact.IMPACT_LOCATION_CENTRIC)
        impact5: "VehicleImpactLocationCentric" = VehicleImpactLocationCentric(locpoint1.impact)
        impact5.latitude = 12.0
        impact5.longitude = 5.0
        impact5.radius = 6400000.0

        trajectory.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region SimpleAscent
    def test_SimpleAscent(self):
        ComparisionUtility = ReportComparison(self.Units)
        oLV: "LaunchVehicle" = LaunchVehicle(
            TestBase.Application.current_scenario.children.new(STKObjectType.LAUNCH_VEHICLE, "LaunchVehicle1")
        )
        Assert.assertIsNotNone(oLV)
        ComparisionUtility.AddReport2(
            clr.CastAs(oLV, IStkObject), '"Euler Angles" "1 Oct 1999 00:00:00" "2 Oct 1999 01:00:00" 60.0', 0.01
        )
        ComparisionUtility.AddReport2(
            clr.CastAs(oLV, IStkObject), '"LLA Position" "1 Oct 1999 00:00:00" "2 Oct 1999 01:00:00" 60.0', 0.01
        )

        TestBase.Application.execute_command(
            'SetState */LaunchVehicle/LaunchVehicle1 SimpleAscent "1 Oct 1999 01:00:00" 60.0 Geodetic 12.0 -40.0 1500.0 7800.0 23.0 10.0 200000.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)  # Connect does not consider stop time

        oPropagator: "PropagatorSimpleAscent" = PropagatorSimpleAscent(oLV.trajectory)
        oPropagator.ephemeris_interval.set_explicit_interval("1 Oct 1999 01:00:00", "1 Oct 1999 01:10:00")
        oPropagator.step = 60
        oInitState: "LaunchVehicleInitialState" = oPropagator.initial_state
        Launch: "LatitudeLongitudeAltitudeDetic" = LatitudeLongitudeAltitudeDetic(
            oInitState.launch.convert_to(DeticPositionType.DETIC)
        )
        Launch.latitude = 12.0
        Launch.longitude = -40.0
        Launch.altitude = 1500
        oInitState.burnout_velocity = 7800.0
        oInitState.launch.assign(Launch)
        Burnout: "LatitudeLongitudeAltitudeDetic" = LatitudeLongitudeAltitudeDetic(
            oInitState.burnout.convert_to(DeticPositionType.DETIC)
        )
        Burnout.latitude = 23.0
        Burnout.longitude = 10.0
        Burnout.altitude = 200000.0
        oInitState.burnout.assign(Burnout)
        oPropagator.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'SetState */LaunchVehicle/LaunchVehicle1 SimpleAscent "1 Oct 1999 00:00:00" 60.0 Geocentric 12.0 -40.0 6400000.0 7800.0  23.0 10.0 6600000.0'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        oPropagator.ephemeris_interval.set_explicit_interval("1 Oct 1999 00:00:00", "1 Oct 1999 00:10:00")
        oPropagator.step = 60
        oInitState = oPropagator.initial_state
        LaunchGeoCent: "LatitudeLongitudeAltitudeCentric" = LatitudeLongitudeAltitudeCentric(
            oInitState.launch.convert_to(DeticPositionType.CENTRIC)
        )
        LaunchGeoCent.latitude = 12.0
        LaunchGeoCent.longitude = -40.0
        LaunchGeoCent.radius = 6400000
        oInitState.burnout_velocity = 7800.0
        oInitState.launch.assign(LaunchGeoCent)
        BurnoutGeoCent: "LatitudeLongitudeAltitudeCentric" = LatitudeLongitudeAltitudeCentric(
            oInitState.burnout.convert_to(DeticPositionType.CENTRIC)
        )
        BurnoutGeoCent.latitude = 23.0
        BurnoutGeoCent.longitude = 10.0
        BurnoutGeoCent.radius = 6600000.0
        oInitState.burnout.assign(BurnoutGeoCent)
        oPropagator.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region GreatArc
    def test_GreatArc(self):
        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_AC, IStkObject), '"Waypoints"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_AC, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_AC, IStkObject), '"ECF Position Velocity"')

        # Units
        self.Units.set_current_unit("DateFormat", "EpSec")
        self.Units.set_current_unit("DistanceUnit", "km")

        # OM Setup
        Propagation.AG_AC.set_route_type(PropagatorType.GREAT_ARC)
        greatarc: "PropagatorGreatArc" = PropagatorGreatArc(Propagation.AG_AC.route)
        greatarc.waypoints.remove_all()
        greatarc.method = VehicleWaypointComputationMethod.DETERMINE_VELOCITY_FROM_TIME
        waypt: "VehicleWaypointsElement" = greatarc.waypoints.add()
        waypt.latitude = 32.8
        waypt.longitude = -99.0
        waypt.altitude = 3.05
        waypt.time = 0.0
        waypt = greatarc.waypoints.add()
        waypt.latitude = 33.8
        waypt.longitude = -99.7
        waypt.altitude = 3.05
        waypt.time = 1604.83
        waypt = greatarc.waypoints.add()
        waypt.latitude = 34.0
        waypt.longitude = -101.3
        waypt.altitude = 3.05
        waypt.time = 3397.0
        waypt = greatarc.waypoints.add()
        waypt.latitude = 32.9
        waypt.longitude = -101.8
        waypt.altitude = 3.05
        waypt.time = 5172.3
        waypt = greatarc.waypoints.add()
        waypt.latitude = 31.4
        waypt.longitude = -101.3
        waypt.altitude = 3.0
        waypt.time = 7390.42

        greatarc.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Propagate */Aircraft/Boing737 "1 Nov 2000 00:00:00.00" "8 Nov 2000 08:00:00.00"'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region LOP
    def test_LOP(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.LOP)
        lop: "PropagatorLOP" = PropagatorLOP(Propagation.AG_SAT.propagator)
        lop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "10 Nov 2000 00:00:00.00")
        lop.step = 86400.0
        spher: "OrbitStateSpherical" = OrbitStateSpherical(
            lop.initial_state.representation.convert_to(OrbitStateType.SPHERICAL)
        )
        spher.coordinate_system_type = CoordinateSystem.J2000
        # Epoch was deprecated
        # lop.InitialState.Epoch = "1 Nov 2000 00:00:00.00";
        (spher).epoch = "1 Nov 2000 00:00:00.00"
        spher.right_ascension = 0.0
        spher.declination = 0.0
        spher.radius = 8059000.0
        spher.flight_path_angle_type = 0
        hor: "SphericalFlightPathAngleHorizontal" = SphericalFlightPathAngleHorizontal(spher.flight_path_angle)
        hor.flight_path_angle = 0.0
        spher.azimuth = 26.5
        spher.velocity = 7033.0

        lop.initial_state.representation.assign(spher)

        lop.force_model.central_body_gravity.maximum_degree = 14
        lop.force_model.central_body_gravity.maximum_order = 13
        lop.force_model.third_body_gravity.use_solar_gravity = True
        lop.force_model.third_body_gravity.use_lunar_gravity = False
        # lop.ForceModel.SolarRadiationPressure.Use = true;
        # lop.ForceModel.SolarRadiationPressure.Cp = 2.332;
        # lop.ForceModel.SolarRadiationPressure.AtmosHeight = 87.59;
        # lop.ForceModel.PhysicalData.SRPCrossSectionalArea = 18.17;

        lop.force_model.drag.use = True
        lop.force_model.drag.cd = 3.5
        lop.force_model.physical_data.drag_cross_sectional_area = 20
        lop.force_model.drag.advanced.atmospheric_density_model = AtmosphericDensityModel.EXPONENTIAL_MODEL
        lop.force_model.drag.advanced.exponential_density_model_parameters.reference_density = 0.003
        lop.force_model.drag.advanced.exponential_density_model_parameters.reference_height = 123.0
        lop.force_model.drag.advanced.exponential_density_model_parameters.scale_height = 234.0
        lop.force_model.drag.advanced.use_osculating_altitude = False
        lop.force_model.drag.advanced.maximum_drag_altitude = 65.0
        lop.force_model.drag.advanced.density_weighing_factor = 1.023

        lop.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Spherical LOP "1 Nov 2000 00:00:00.00" "10 Nov 2000 00:00:00.00" 86400.0 J2000 "1 Nov 2000 00:00:00.00" 0.0 0.0 8059000.0 0.0 26.5 7033.0'
        )

        TestBase.Application.execute_command("LOP */Satellite/Satellite1 Force EarthGravity 14 13")
        TestBase.Application.execute_command("LOP */Satellite/Satellite1 Force ThirdBodyGravity On Off")
        # Application.ExecuteCommand("LOP */Satellite/Satellite1 Force SolarRadPressure On 2.332 87.59 18.17");

        TestBase.Application.execute_command("LOP */Satellite/Satellite1 Drag Basic On 3.5 20")
        TestBase.Application.execute_command("LOP */Satellite/Satellite1 Drag Model Exponential 0.003 123.0 234.0")
        TestBase.Application.execute_command("LOP */Satellite/Satellite1 Drag Advanced Off 65.0 1.023")

        TestBase.Application.execute_command(
            'Propagate */Satellite/Satellite1 "1 Nov 2000 00:00:00.00" "10 Nov 2000 00:00:00.00"'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region SGP4
    def test_SGP4(self):
        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.SGP4)
        sgp4: "PropagatorSGP4" = PropagatorSGP4(Propagation.AG_SAT.propagator)
        sgp4.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        sgp4.step = 120.0
        sgp4.segments.ssc_number = "98765"
        seg: "PropagatorSGP4Segment" = sgp4.segments.add_segment()
        seg.epoch = 231.5
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "day")
        seg.mean_motion = 2.0
        self.Units.reset_units()
        self.Units.set_current_unit("DistanceUnit", "m")
        seg.eccentricity = 0.0
        seg.inclination = 55.0
        seg.argument_of_periapsis = 0.0
        seg.right_ascension_ascending_node = 0.0
        seg.mean_anomaly = 0.0
        seg.bstar = 0.12345

        sgp4.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 SGP4 "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 120.0 98765 00231.50 2.0 0.0 55.0 0.0 0.0 0.0 0.0 0.0 .12345'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.SGP4)
        sgp4: "PropagatorSGP4" = PropagatorSGP4(Propagation.AG_SAT.propagator)
        sgp4.ephemeris_interval.set_explicit_interval("1 Jul 2009 15:00:00.00", "1 Jul 2009 19:00:00.00")
        sgp4.step = 60
        sgp4.segments.ssc_number = "11417"
        sgp4.automatic_update_enabled = True
        sgp4.automatic_update_settings.selected_source = VehicleSGP4AutomaticUpdateSourceType.FILE
        sgp4.automatic_update_settings.file_source.filename = TestBase.GetScenarioFile("B44150.tle")
        sgp4.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        cmd: str = (
            'SetState */Satellite/Satellite1 SGP4 "1 Jul 2009 15:00:00.00" "1 Jul 2009 19:00:00.00" 60.0 11417 TLESource Automatic Source File "'
            + TestBase.GetScenarioFile("B44150.tle")
        ) + '"'
        TestBase.Application.execute_command(cmd)

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region GPS
    def test_GPS(self):
        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.GPS)
        gps: "PropagatorGPS" = PropagatorGPS(Propagation.AG_SAT.propagator)
        gps.prn = 23
        gps.automatic_update_enabled = False
        gps.specify_catalog.filename = TestBase.GetScenarioFile("GPSAlmanac.al3")
        almanacPropertiesSEM: "VehicleGPSAlmanacPropertiesSEM" = clr.CastAs(
            gps.specify_catalog.properties, VehicleGPSAlmanacPropertiesSEM
        )
        Assert.assertIsNotNone(almanacPropertiesSEM)
        almanacPropertiesSEM.reference_week = GPSReferenceWeek.WEEK06_JAN1980
        gps.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        cmd: str = (
            'SetState */Satellite/Satellite1 GPS 23 WeekRefEpoch 06Jan1980 Catalog "'
            + TestBase.GetScenarioFile("GPSAlmanac.al3")
        ) + '"'
        TestBase.Application.execute_command(cmd)

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.GPS)
        gps: "PropagatorGPS" = PropagatorGPS(Propagation.AG_SAT.propagator)
        gps.prn = 23
        gps.automatic_update_enabled = True
        gps.automatic_update_settings.selected_source = VehicleGPSAutomaticUpdateSourceType.FILE
        gps.automatic_update_settings.file_source.filename = TestBase.GetScenarioFile("GPSAlmanac.al3")
        autoUpdateProperties: "VehicleGPSAutoUpdateProperties" = clr.CastAs(
            gps.automatic_update_settings.properties, VehicleGPSAutoUpdateProperties
        )
        Assert.assertIsNotNone(autoUpdateProperties)
        autoUpdateProperties.week_reference_epoch = GPSReferenceWeek.WEEK06_JAN1980
        gps.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        cmd: str = (
            'SetState */Satellite/Satellite1 GPS 23 WeekRefEpoch 06Jan1980 UpdateMode FromFiles SourceFile "'
            + TestBase.GetScenarioFile("GPSAlmanac.al3")
        ) + '"'
        TestBase.Application.execute_command(cmd)

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region Astrogator
    def test_Astrogator(self):
        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Inertial Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.ASTROGATOR)
        driverMCS: "MCSDriver" = MCSDriver(Propagation.AG_SAT.propagator)
        driverMCS.main_sequence.insert(SegmentType.MANEUVER, "Maneuver", "Propagate")
        ts: "MCSTargetSequence" = MCSTargetSequence(
            driverMCS.main_sequence.insert(SegmentType.TARGET_SEQUENCE, "Target_Sequence", "-")
        )
        maneuver: "MCSManeuver" = MCSManeuver(ts.segments.insert(SegmentType.MANEUVER, "Maneuver", "-"))

        maneuver.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)

        driverMCS.run_mcs()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Cleanup OM
        ts.segments.remove("Maneuver")
        driverMCS.main_sequence.remove("Target_Sequence")
        driverMCS.main_sequence.remove("Maneuver")
        driverMCS.run_mcs()

        # Connect Setup
        TestBase.Application.execute_command("Astrogator */Satellite/Satellite1 SetProp")
        TestBase.Application.execute_command(
            "Astrogator */Satellite/Satellite1 InsertSegment MainSequence.SegmentList.Propagate Maneuver"
        )
        TestBase.Application.execute_command(
            "Astrogator */Satellite/Satellite1 InsertSegment MainSequence.SegmentList.- Target_Sequence"
        )
        TestBase.Application.execute_command(
            "Astrogator */Satellite/Satellite1 InsertSegment MainSequence.SegmentList.Target_Sequence.SegmentList.- Maneuver"
        )

        TestBase.Application.execute_command(
            "Astrogator */Satellite/Satellite1 AddMCSSegmentControl MainSequence.SegmentList.Target_Sequence.SegmentList.Maneuver ImpulsiveMnvr.Cartesian.X"
        )

        TestBase.Application.execute_command("Astrogator */Satellite/Satellite1 RunMCS")

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region InvalidPropagationIntervals
    def test_InvalidPropagationIntervals(self):
        # J2 propagator type
        TestBase.logger.WriteLine6("The current Propagator type is: {0}", Propagation.AG_SAT.propagator_type)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        TestBase.logger.WriteLine6("The new Propagator type is: {0}", Propagation.AG_SAT.propagator_type)
        Assert.assertEqual(PropagatorType.J2_PERTURBATION, Propagation.AG_SAT.propagator_type)
        # J2 propagator
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Propagation.AG_SAT.propagator)
        Assert.assertIsNotNone(j2prop)
        # StartTime / StopTime
        TestBase.logger.WriteLine6("\tThe current StartTime is: {0}", j2prop.ephemeris_interval.find_start_time())
        TestBase.logger.WriteLine6("\tThe current StopTime is: {0}", j2prop.ephemeris_interval.find_stop_time())
        with pytest.raises(Exception):
            j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 03:00:00.000", "1 Nov 2000 02:00:00.000")

        # LOP propagator type
        TestBase.logger.WriteLine6("The current Propagator type is: {0}", Propagation.AG_SAT.propagator_type)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.LOP)
        TestBase.logger.WriteLine6("The new Propagator type is: {0}", Propagation.AG_SAT.propagator_type)
        Assert.assertEqual(PropagatorType.LOP, Propagation.AG_SAT.propagator_type)
        # LOP propagator
        oLOP: "PropagatorLOP" = PropagatorLOP(Propagation.AG_SAT.propagator)
        Assert.assertIsNotNone(oLOP)

        # StartTime / StopTime
        TestBase.logger.WriteLine6("\tThe current StartTime is: {0}", oLOP.ephemeris_interval.find_start_time())
        TestBase.logger.WriteLine6("\tThe current StopTime is: {0}", oLOP.ephemeris_interval.find_stop_time())
        with pytest.raises(Exception):
            oLOP.ephemeris_interval.set_explicit_interval("1 Nov 2000 03:00:00.000", "1 Nov 2000 02:00:00.000")

        # SGP4 propagator type
        TestBase.logger.WriteLine6("The current Propagator type is: {0}", Propagation.AG_SAT.propagator_type)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.SGP4)
        TestBase.logger.WriteLine6("The new Propagator type is: {0}", Propagation.AG_SAT.propagator_type)
        Assert.assertEqual(PropagatorType.SGP4, Propagation.AG_SAT.propagator_type)
        # SGP4 propagator
        oSGP4: "PropagatorSGP4" = PropagatorSGP4(Propagation.AG_SAT.propagator)
        Assert.assertIsNotNone(oSGP4)
        # StartTime / StopTime
        TestBase.logger.WriteLine6("\tThe current StartTime is: {0}", oSGP4.ephemeris_interval.find_start_time())
        TestBase.logger.WriteLine6("\tThe current StopTime is: {0}", oSGP4.ephemeris_interval.find_stop_time())
        with pytest.raises(Exception):
            oSGP4.ephemeris_interval.set_explicit_interval("1 Nov 2000 03:00:00.000", "1 Nov 2000 02:00:00.000")

        # SPICE propagator type
        TestBase.logger.WriteLine6("The current Propagator type is: {0}", Propagation.AG_SAT.propagator_type)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.SPICE)
        TestBase.logger.WriteLine6("The new Propagator type is: {0}", Propagation.AG_SAT.propagator_type)
        Assert.assertEqual(PropagatorType.SPICE, Propagation.AG_SAT.propagator_type)
        # SPICE propagator
        oSPICE: "PropagatorSPICE" = PropagatorSPICE(Propagation.AG_SAT.propagator)
        Assert.assertIsNotNone(oSPICE)
        # StartTime / StopTime
        TestBase.logger.WriteLine6("\tThe current StartTime is: {0}", oSPICE.ephemeris_interval.find_start_time())
        TestBase.logger.WriteLine6("\tThe current StopTime is: {0}", oSPICE.ephemeris_interval.find_stop_time())
        with pytest.raises(Exception):
            oSPICE.ephemeris_interval.set_explicit_interval("1 Nov 2000 03:00:00.000", "1 Nov 2000 02:00:00.000")

        # LaunchVehicle propagator test
        oLV: "LaunchVehicle" = LaunchVehicle(
            TestBase.Application.current_scenario.children.new(STKObjectType.LAUNCH_VEHICLE, "LV")
        )
        # SimpleAscent propagator type
        TestBase.logger.WriteLine6("The current TrajectoryType is: {0}", oLV.trajectory_type)
        oLV.set_trajectory_type(PropagatorType.SIMPLE_ASCENT)
        TestBase.logger.WriteLine6("The new TrajectoryType is: {0}", oLV.trajectory_type)
        Assert.assertEqual(PropagatorType.SIMPLE_ASCENT, oLV.trajectory_type)
        # SimpleAscent propagator
        oSimple: "PropagatorSimpleAscent" = PropagatorSimpleAscent(oLV.trajectory)
        Assert.assertIsNotNone(oSimple)
        # StartTime / StopTime
        TestBase.logger.WriteLine6("\tThe current StartTime is: {0}", oSimple.ephemeris_interval.find_start_time())
        TestBase.logger.WriteLine6("\tThe current StopTime is: {0}", oSimple.ephemeris_interval.find_stop_time())
        with pytest.raises(Exception):
            oSimple.ephemeris_interval.set_explicit_interval("1 Nov 2000 03:00:00.000", "1 Nov 2000 02:00:00.000")

        # TwoBody propagator type
        Propagation.AG_MS = Missile(TestBase.Application.current_scenario.children["Missile1"])
        Assert.assertIsNotNone(Propagation.AG_MS)
        TestBase.logger.WriteLine6("The current TrajectoryType is: {0}", Propagation.AG_MS.trajectory_type)
        Propagation.AG_MS.set_trajectory_type(PropagatorType.TWO_BODY)
        TestBase.logger.WriteLine6("The new TrajectoryType is: {0}", Propagation.AG_MS.trajectory_type)
        Assert.assertEqual(PropagatorType.TWO_BODY, Propagation.AG_MS.trajectory_type)
        # TwoBody propagator
        oTwoBody: "PropagatorTwoBody" = PropagatorTwoBody(Propagation.AG_MS.trajectory)
        Assert.assertIsNotNone(oTwoBody)
        # StartTime / StopTime
        TestBase.logger.WriteLine6("\tThe current StartTime is: {0}", oTwoBody.ephemeris_interval.find_start_time())
        TestBase.logger.WriteLine6("\tThe current StopTime is: {0}", oTwoBody.ephemeris_interval.find_stop_time())
        with pytest.raises(Exception):
            oTwoBody.ephemeris_interval.set_explicit_interval("1 Nov 2000 03:00:00.000", "1 Nov 2000 02:00:00.000")

    # endregion

    # region J2Perturbation
    def test_J2Perturbation(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Propagation.AG_SAT.propagator)
        j2prop.initial_state.ellipse_options = VehicleEllipseOptionType.OSCULATING
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 03:00:00.00", "1 Nov 2000 04:00:00.00")
        j2prop.step = 60
        classical: "OrbitStateClassical" = OrbitStateClassical(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch is deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 7322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.099
        classical.orientation.inclination = 99.5
        classical.orientation.argument_of_periapsis = 1.2
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.2
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 22.2
        j2prop.initial_state.representation.assign(classical)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetStateClassical */Satellite/Satellite1 J2Perturbation "1 Nov 2000 03:00:00.00" "1 Nov 2000 04:00:00.00" 60 J2000 "1 Nov 2000 02:00:00.00" 7322000.122 0.099 99.5 1.2 122.2 22.2'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        j2prop.initial_state.ellipse_options = VehicleEllipseOptionType.SECULARLY_PRECESSING
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPropSpecific */Satellite/Satellite1 EllipseType SecPrecessing")

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region J4Perturbation
    def test_J4Perturbation(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.J4_PERTURBATION)
        j4prop: "PropagatorJ4Perturbation" = PropagatorJ4Perturbation(Propagation.AG_SAT.propagator)
        j4prop.initial_state.ellipse_options = VehicleEllipseOptionType.OSCULATING
        j4prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 12:00:00.00")
        j4prop.step = 600
        classical: "OrbitStateClassical" = OrbitStateClassical(
            j4prop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # j4prop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 8322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.079
        classical.orientation.inclination = 88.4
        classical.orientation.argument_of_periapsis = 1.8
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 132.4
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 26.4

        j4prop.initial_state.representation.assign(classical)
        j4prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetStateClassical */Satellite/Satellite1 J4Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 12:00:00.00" 600 J2000 "1 Nov 2000 02:00:00.00" 8322000.122 0.079 88.4 1.8 132.4 26.4'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        j4prop.initial_state.ellipse_options = VehicleEllipseOptionType.SECULARLY_PRECESSING
        j4prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPropSpecific */Satellite/Satellite1 EllipseType SecPrecessing")

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region TwoBody
    def test_TwoBody(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.TWO_BODY)
        twobody: "PropagatorTwoBody" = PropagatorTwoBody(Propagation.AG_SAT.propagator)
        twobody.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 12:00:00.00")
        twobody.step = 600
        classical: "OrbitStateClassical" = OrbitStateClassical(
            twobody.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # twobody.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 8022000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.09
        classical.orientation.inclination = 88.4
        classical.orientation.argument_of_periapsis = 1.3
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.4
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 21.4
        twobody.initial_state.representation.assign(classical)
        twobody.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetStateClassical */Satellite/Satellite1 TwoBody "1 Nov 2000 00:00:00.00" "1 Nov 2000 12:00:00.00" 600 J2000 "1 Nov 2000 02:00:00.00" 8022000.122 0.09 88.4 1.3 122.4 21.4'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region LeapSecond
    def test_LeapSecond(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), '"LLA Position"')

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.TWO_BODY)
        twobody: "PropagatorTwoBody" = PropagatorTwoBody(Propagation.AG_SAT.propagator)

        # "30 Jun 2012 23:59:55.000" "1 Jul 2012 00:00:05.000"  - across a leap second

        twobody.ephemeris_interval.set_explicit_interval("30 Jun 2012 23:59:55.000", "1 Jul 2012 00:00:05.000")
        twobody.step = 1
        classical: "OrbitStateClassical" = OrbitStateClassical(
            twobody.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        (classical).epoch = "30 Jun 2012 23:59:55.000"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 8022000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.09
        classical.orientation.inclination = 88.4
        classical.orientation.argument_of_periapsis = 1.3
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.4
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 21.4
        twobody.initial_state.representation.assign(classical)
        twobody.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetStateClassical */Satellite/Satellite1 TwoBody "30 Jun 2012 23:59:55.000" "1 Jul 2012 00:00:05.000" 1 J2000 "30 Jun 2012 23:59:55.000" 8022000.122 0.09 88.4 1.3 122.4 21.4'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region MeanMotion
    def test_MeanMotion(self):
        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        hpop: "PropagatorHPOP" = PropagatorHPOP(Propagation.AG_SAT.propagator)
        hpop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 12:00:00.00")
        hpop.step = 120
        classical: "OrbitStateClassical" = OrbitStateClassical(
            hpop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 8322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.079

        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "hr")
        sizeshape1.mean_motion = 1
        Assert.assertEqual(1, sizeshape1.mean_motion)

        hpop.initial_state.representation.assign(classical)
        hpop.propagate()

    # endregion

    # region HPOP
    def test_HPOP(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Propagation.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport2(
            clr.CastAs(Propagation.AG_SAT, IStkObject),
            '"LLA Position" "1 Nov 2000 00:00:00.00" "1 Nov 2000 12:00:00.00" 120',
            1e-05,
        )
        ComparisionUtility.AddReport2(
            clr.CastAs(Propagation.AG_SAT, IStkObject),
            '"Cartesian Position Velocity" "1 Nov 2000 00:00:00.00" "1 Nov 2000 12:00:00.00" 120',
            1e-05,
        )
        ComparisionUtility.AddReport2(
            clr.CastAs(Propagation.AG_SAT, IStkObject),
            '"Euler Angles" "1 Nov 2000 00:00:00.00" "1 Nov 2000 12:00:00.00" 120',
            1e-05,
        )

        # OM Setup
        Propagation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        hpop: "PropagatorHPOP" = PropagatorHPOP(Propagation.AG_SAT.propagator)
        hpop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 12:00:00.00")
        hpop.step = 120
        classical: "OrbitStateClassical" = OrbitStateClassical(
            hpop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 8322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.079
        classical.orientation.inclination = 88.4
        classical.orientation.argument_of_periapsis = 1.8
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 132.4
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 26.4
        hpop.force_model.central_body_gravity.file = TestBase.GetScenarioFile("WGS84_EGM96.grv")

        hpop.initial_state.representation.assign(classical)

        hpop.force_model.solar_radiation_pressure.use = True
        hpop.force_model.solar_radiation_pressure.solar_radiation_pressure_model.set_model_type(
            SolarRadiationPressureModelType.SPHERICAL
        )
        (
            SolarRadiationPressureModelSpherical(
                (hpop.force_model.solar_radiation_pressure.solar_radiation_pressure_model.model)
            )
        ).cr = 3.2
        (
            SolarRadiationPressureModelSpherical(
                (hpop.force_model.solar_radiation_pressure.solar_radiation_pressure_model.model)
            )
        ).area_mass_ratio = 5.6
        merc: "PropagatorHPOPThirdBodyGravityElement" = hpop.force_model.third_body_gravity.add_third_body("Mercury")
        merc.source = ThirdBodyGravitySourceType.USER_SPECIFIED
        merc.gravity_value = 123.89
        hpop.force_model.central_body_gravity.solid_tide_type = SolidTide.FULL
        hpop.force_model.more_options.solid_tides.include_time_dependent_solid_tides = True
        hpop.force_model.more_options.solid_tides.minimum_amplitude = 0.02
        hpop.force_model.more_options.radiation_pressure.include_albedo = True
        hpop.force_model.more_options.radiation_pressure.ck = 56
        hpop.force_model.more_options.radiation_pressure.include_thermal = True
        hpop.force_model.more_options.radiation_pressure.area_mass_ratio = 4
        hpop.force_model.drag.use = True
        hpop.force_model.drag.atmospheric_density_model = AtmosphericDensityModel.MSIS90
        hpop.force_model.drag.set_drag_model_type(DragModel.SPHERICAL)
        (VehicleHPOPDragModelSpherical(hpop.force_model.drag.drag_model)).cd = 2.08
        (VehicleHPOPDragModelSpherical(hpop.force_model.drag.drag_model)).area_mass_ratio = 0.175
        hpop.force_model.drag.set_solar_flux_geo_magnitude_type(VehicleSolarFluxGeomagneticType.MANUAL_ENTRY)
        solarflux: "SolarFluxGeoMagneticValueSettings" = SolarFluxGeoMagneticValueSettings(
            hpop.force_model.drag.solar_flux_geo_magnitude
        )
        solarflux.daily_f107 = 120
        solarflux.average_f107 = 105
        solarflux.geomagnetic_index = 3.5

        hpop.covariance.compute_covariance = True
        hpop.covariance.gravity.maximum_degree = 4
        hpop.covariance.gravity.maximum_order = 2

        hpop.covariance.position_velocity[0].x = 100
        hpop.covariance.position_velocity[1].x = 0.0
        hpop.covariance.position_velocity[1].y = 400.0
        hpop.covariance.position_velocity[2].x = 0.0
        hpop.covariance.position_velocity[2].y = 0.0
        hpop.covariance.position_velocity[2].z = 900.0
        hpop.covariance.position_velocity[3].x = 0.0
        hpop.covariance.position_velocity[3].y = 0.0
        hpop.covariance.position_velocity[3].z = 0.0
        hpop.covariance.position_velocity[3].vx = 16.0
        hpop.covariance.position_velocity[4].x = 0.0
        hpop.covariance.position_velocity[4].y = 0.0
        hpop.covariance.position_velocity[4].z = 0.0
        hpop.covariance.position_velocity[4].vx = 0.0
        hpop.covariance.position_velocity[4].vy = 25.0
        hpop.covariance.position_velocity[5].x = 0.0
        hpop.covariance.position_velocity[5].y = 0.0
        hpop.covariance.position_velocity[5].z = 0.0
        hpop.covariance.position_velocity[5].vx = 0.0
        hpop.covariance.position_velocity[5].vy = 0.0
        hpop.covariance.position_velocity[5].vz = 26.0

        hpop.covariance.include_consider_analysis = True
        drag: "VehicleConsiderAnalysisCollectionElement" = hpop.covariance.consider_analysis_list.add(
            VehicleConsiderAnalysisType.DRAG
        )
        drag.value = 0.1
        drag.x = 0.0
        drag.y = 0.0
        drag.z = 0.0
        drag.vx = 0.0
        drag.vy = 0.0
        drag.vz = 0.0
        srp: "VehicleConsiderAnalysisCollectionElement" = hpop.covariance.consider_analysis_list.add(
            VehicleConsiderAnalysisType.SOLAR_RADIATION_PRESSURE
        )
        srp.value = 0.4
        srp.x = 0.0
        srp.y = 0.0
        srp.z = 0.0
        srp.vx = 0.0
        srp.vy = 0.0
        srp.vz = 0.0

        hpop.covariance.include_consider_cross_correlation = True
        correlation: "VehicleCorrelationListElement" = hpop.covariance.correlation_list.add()
        correlation.row = VehicleCorrelationListType.DRAG
        correlation.column = VehicleCorrelationListType.SOLAR_RADIATION_PRESSURE
        correlation.value = 0.16

        hpop.integrator.integration_model = VehicleIntegrationModel.RUNGE_KUTTA_FEHLBERG_78
        hpop.integrator.step_size_control.method = VehicleMethod.RELATIVE_ERROR
        hpop.integrator.step_size_control.error_tolerance = 1e-13

        #
        # Test min/max on StepSizeControl.MinMaxStepSize
        #

        minStepSize: float = hpop.integrator.step_size_control.minimum_step_size
        maxStepSize: float = hpop.integrator.step_size_control.maximum_step_size

        with pytest.raises(Exception):
            hpop.integrator.step_size_control.minimum_step_size = maxStepSize + 1

        with pytest.raises(Exception):
            hpop.integrator.step_size_control.maximum_step_size = minStepSize - 1

        # Restore original values
        hpop.integrator.step_size_control.minimum_step_size = minStepSize
        hpop.integrator.step_size_control.maximum_step_size = maxStepSize

        hpop.propagate()
        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        strPath: str = TestBase.GetScenarioFile("WGS84_EGM96.grv")
        TestBase.Application.execute_command(
            'SetStateClassical */Satellite/Satellite1 HPOP "1 Nov 2000 00:00:00.00" "1 Nov 2000 12:00:00.00" 120 J2000 "1 Nov 2000 02:00:00.00" 8322000.122 0.079 88.4 1.8 132.4 26.4'
        )
        TestBase.Application.execute_command((('HPOP */Satellite/Satellite1 Force Gravity "' + strPath) + '" 21 21'))

        TestBase.Application.execute_command("HPOP */Satellite/Satellite1 Force SolarRad On 3.2 5.6")
        TestBase.Application.execute_command((('HPOP */Satellite/Satellite1 Force Gravity "' + strPath) + '" 21 21'))
        TestBase.Application.execute_command(
            "HPOP */Satellite/Satellite1 Force ThirdBodyGravity Mercury On User 123.89"
        )
        TestBase.Application.execute_command(
            "HPOP */Satellite/Satellite1 Force SolidTides On IncTimeDep On MinAmplitude 0.02"
        )
        TestBase.Application.execute_command(
            "HPOP */Satellite/Satellite1 Force RadiationPressure Albedo On Coefficient 56"
        )
        TestBase.Application.execute_command(
            "HPOP */Satellite/Satellite1 Force RadiationPressure Thermal On AreaMassRatio 4"
        )
        TestBase.Application.execute_command(
            'HPOP */Satellite/Satellite1 Drag On 2.08 0.175 "MSISE 1990" Manual 120 105 3.5'
        )
        TestBase.Application.execute_command("HPOP */Satellite/Satellite1 Covariance On")
        TestBase.Application.execute_command("HPOP */Satellite/Satellite1 Covariance Gravity 4 2")
        TestBase.Application.execute_command(
            "HPOP */Satellite/Satellite1 Covariance PosVel 100. 0.0 400. 0.0 0.0 900. 0.0 0.0 0.0 16. 0.0 0.0 0.0 0.0 25. 0.0 0.0 0.0 0.0 0.0 36."
        )
        TestBase.Application.execute_command(
            "HPOP */Satellite/Satellite1 Covariance ConsiderParam Drag 0.1 0.0 0.0 0.0 0.0 0.0 0.0"
        )
        TestBase.Application.execute_command(
            "HPOP */Satellite/Satellite1 Covariance ConsiderParam SRP .4 0.0 0.0 0.0 0.0 0.0 0.0"
        )
        TestBase.Application.execute_command("HPOP */Satellite/Satellite1 Covariance ConsiderParam Drag SRP .16 ")
        TestBase.Application.execute_command(
            "HPOP */Satellite/Satellite1 Integrator IntegMethod RKF78 StepControl RelativeError 1.0e-13"
        )
        TestBase.Application.execute_command(
            'Propagate */Satellite/Satellite1 "1 Nov 2000 00:00:00.00" "1 Nov 2000 12:00:00.00"'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region InterplanetaryHPOP
    # The purpose of this test is to exercise HPOP in interplanetary settings
    # see also //stktest/branches/R_TEST_STK_v8.x/STK/Tests/InterplanetaryProp.pl
    def test_InterplanetaryHPOP(self):
        # load scenario
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(
            TestBase.GetScenarioFile("InterplanetaryProp", "InterplanetaryPropagation.sc")
        )

        # Reports initialization
        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopSun"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        oComparator1 = ReportComparison(self.Units)
        oComparator1.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), 'PreData "RIC" "Satellite/AstgSun" ')

        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopMoon"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        oComparator2 = ReportComparison(self.Units)
        oComparator2.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), 'PreData "RIC" "Satellite/AstgMoon" ')

        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopMars"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        oComparator3 = ReportComparison(self.Units)
        oComparator3.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), 'PreData "RIC" "Satellite/AstgMars" ')

        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopEuropa"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        oComparator4 = ReportComparison(self.Units)
        oComparator4.AddReport(clr.CastAs(Propagation.AG_SAT, IStkObject), 'PreData "RIC" "Satellite/AstgEuropa" ')

        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopJupiterVOP"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        oComparator5 = ReportComparison(self.Units)
        oComparator5.AddReport(
            clr.CastAs(Propagation.AG_SAT, IStkObject),
            'PreData "RIC" "Satellite/AstgJupiterVOP" "2 Jul 2007 11:59:59.99" "2 Jul 2007 12:00:00.00" 0.01',
        )

        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["LopEarth"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        oComparator6 = ReportComparison(self.Units)
        oComparator6.AddReport2(
            clr.CastAs(Propagation.AG_SAT, IStkObject),
            '"LLA Position" "1 Jul 2007 12:00:00.00" "10 Jul 2007 12:00:00.00" 86400',
            1e-05,
        )

        # Connect
        # Sun - 10 days - Fixed Step
        TestBase.Application.execute_command(
            'Propagate */Satellite/HpopSun "1 Jul 2007 12:00:00.00" "11 Jul 2007 12:00:00.00"'
        )
        TestBase.Application.execute_command(
            'Propagate */Satellite/AstgSun "1 Jul 2007 12:00:00.00" "11 Jul 2007 12:00:00.00"'
        )
        oComparator1.TakeConnectSnapshot(TestBase.Application)

        # Moon - 1 day - Fixed Step
        TestBase.Application.execute_command(
            'Propagate */Satellite/HpopMoon "1 Jul 2007 12:00:00.00" "2 Jul 2007 12:00:00.00"'
        )
        TestBase.Application.execute_command(
            'Propagate */Satellite/AstgMoon "1 Jul 2007 12:00:00.00" "2 Jul 2007 12:00:00.00"'
        )
        oComparator2.TakeConnectSnapshot(TestBase.Application)

        # Mars - 1 day -  Fixed Step
        TestBase.Application.execute_command(
            'Propagate */Satellite/HpopMars "1 Jul 2007 12:00:00.00" "2 Jul 2007 12:00:00.00"'
        )
        TestBase.Application.execute_command(
            'Propagate */Satellite/AstgMars "1 Jul 2007 12:00:00.00" "2 Jul 2007 12:00:00.00"'
        )
        oComparator3.TakeConnectSnapshot(TestBase.Application)

        # Europa - 1 day -  Fixed Step
        TestBase.Application.execute_command(
            'Propagate */Satellite/HpopEuropa "1 Jul 2007 12:00:00.00" "2 Jul 2007 12:00:00.00"'
        )
        TestBase.Application.execute_command(
            'Propagate */Satellite/AstgEuropa "1 Jul 2007 12:00:00.00" "2 Jul 2007 12:00:00.00"'
        )
        oComparator4.TakeConnectSnapshot(TestBase.Application)

        # Jupiter - 1 day - VOP using step error control
        TestBase.Application.execute_command(
            'Propagate */Satellite/HpopJupiterVOP "1 Jul 2007 12:00:00.00" "2 Jul 2007 12:00:00.00"'
        )
        TestBase.Application.execute_command(
            'Propagate */Satellite/AstgJupiterVOP "1 Jul 2007 12:00:00.00" "2 Jul 2007 12:00:00.00"'
        )
        # only ask at the end, since there will be interpolation diffs because the integrator choose different nodes
        oComparator5.TakeConnectSnapshot(TestBase.Application)

        # Earth - 10 day with Lop
        TestBase.Application.execute_command(
            'Propagate */Satellite/LopEarth "1 Jul 2007 12:00:00.00" "10 Jul 2007 12:00:00.00"'
        )
        oComparator6.TakeConnectSnapshot(TestBase.Application)

        # Object Model
        # load scenario
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(
            TestBase.GetScenarioFile("InterplanetaryProp", "InterplanetaryPropagation.sc")
        )

        # Sun - 10 days - Fixed Step
        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopSun"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        Assert.assertEqual(PropagatorType.HPOP, Propagation.AG_SAT.propagator_type)
        oHPOP: "PropagatorHPOP" = clr.CastAs(Propagation.AG_SAT.propagator, PropagatorHPOP)
        Assert.assertIsNotNone(oHPOP)
        oHPOP.ephemeris_interval.set_explicit_interval("1 Jul 2007 12:00:00.000", "11 Jul 2007 12:00:00.000")
        Assert.assertEqual("1 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_start_time())
        Assert.assertEqual("11 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_stop_time())
        oHPOP.propagate()
        # Astrogator is not implemented in OM
        AstgSun: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["AstgSun"], Satellite)
        AstgSun.set_propagator_type(PropagatorType.ASTROGATOR)
        astgSunDriver: "MCSDriver" = clr.CastAs(AstgSun.propagator, MCSDriver)
        astgSunInitialState: "MCSInitialState" = clr.CastAs(
            astgSunDriver.main_sequence["Initial State"], MCSInitialState
        )
        astgSunInitialState.orbit_epoch = "1 Jul 2007 12:00:00.000"
        astgSunPropagate: "MCSPropagate" = clr.CastAs(astgSunDriver.main_sequence["Propagate"], MCSPropagate)
        stoppingCondition: "StoppingCondition" = clr.CastAs(
            astgSunPropagate.stopping_conditions[0].properties, StoppingCondition
        )
        stoppingCondition.trip = 864000
        astgSunDriver.run_mcs()
        oComparator1.TakeOMSnapshot(TestBase.Application)

        # Moon - 1 day - Fixed Step
        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopMoon"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        Assert.assertEqual(PropagatorType.HPOP, Propagation.AG_SAT.propagator_type)
        oHPOP = None
        oHPOP = clr.CastAs(Propagation.AG_SAT.propagator, PropagatorHPOP)
        Assert.assertIsNotNone(oHPOP)
        oHPOP.ephemeris_interval.set_explicit_interval("1 Jul 2007 12:00:00.000", "2 Jul 2007 12:00:00.000")
        Assert.assertEqual("1 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_stop_time())
        oHPOP.step = 60.0
        Assert.assertEqual(60.0, oHPOP.step)
        oHPOP.propagate()

        # Application.ExecuteCommand("Propagate */Satellite/AstgMoon \"1 Jul 2007 12:00:00.00\" \"2 Jul 2007 12:00:00.00\" 60.0");
        AstgMoon: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["AstgMoon"], Satellite)
        AstgMoon.set_propagator_type(PropagatorType.ASTROGATOR)
        astgMoonDriver: "MCSDriver" = clr.CastAs(AstgMoon.propagator, MCSDriver)
        astgMoonInitialState: "MCSInitialState" = clr.CastAs(
            astgMoonDriver.main_sequence["Initial State"], MCSInitialState
        )
        astgMoonInitialState.orbit_epoch = "1 Jul 2007 12:00:00.000"
        astgMoonPropagate: "MCSPropagate" = clr.CastAs(astgMoonDriver.main_sequence["Propagate"], MCSPropagate)
        stoppingCondition = clr.CastAs(astgMoonPropagate.stopping_conditions[0].properties, StoppingCondition)
        stoppingCondition.trip = 86400
        astgMoonDriver.run_mcs()
        oComparator2.TakeOMSnapshot(TestBase.Application)

        # Mars - 1 day -  Fixed Step
        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopMars"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        Assert.assertEqual(PropagatorType.HPOP, Propagation.AG_SAT.propagator_type)
        oHPOP = None
        oHPOP = clr.CastAs(Propagation.AG_SAT.propagator, PropagatorHPOP)
        Assert.assertIsNotNone(oHPOP)
        oHPOP.ephemeris_interval.set_explicit_interval("1 Jul 2007 12:00:00.000", "2 Jul 2007 12:00:00.000")
        Assert.assertEqual("1 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_stop_time())
        oHPOP.step = 60.0
        Assert.assertEqual(60.0, oHPOP.step)
        oHPOP.propagate()

        # Application.ExecuteCommand("Propagate */Satellite/AstgMars \"1 Jul 2007 12:00:00.00\" \"2 Jul 2007 12:00:00.00\" 60.0");
        AstgMars: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["AstgMars"], Satellite)
        AstgMars.set_propagator_type(PropagatorType.ASTROGATOR)
        astgMarsDriver: "MCSDriver" = clr.CastAs(AstgMars.propagator, MCSDriver)
        astgMarsInitialState: "MCSInitialState" = clr.CastAs(
            astgMarsDriver.main_sequence["Initial State"], MCSInitialState
        )
        astgMarsInitialState.orbit_epoch = "1 Jul 2007 12:00:00.000"
        astgMarsPropagate: "MCSPropagate" = clr.CastAs(astgMarsDriver.main_sequence["Propagate"], MCSPropagate)
        stoppingCondition = clr.CastAs(astgMarsPropagate.stopping_conditions[0].properties, StoppingCondition)
        stoppingCondition.trip = 86400
        astgMarsDriver.run_mcs()
        oComparator3.TakeOMSnapshot(TestBase.Application)

        # Europa - 1 day -  Fixed Step
        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopEuropa"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        Assert.assertEqual(PropagatorType.HPOP, Propagation.AG_SAT.propagator_type)
        oHPOP = None
        oHPOP = clr.CastAs(Propagation.AG_SAT.propagator, PropagatorHPOP)
        Assert.assertIsNotNone(oHPOP)
        oHPOP.ephemeris_interval.set_explicit_interval("1 Jul 2007 12:00:00.000", "2 Jul 2007 12:00:00.000")
        Assert.assertEqual("1 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_stop_time())
        oHPOP.step = 60.0
        Assert.assertEqual(60.0, oHPOP.step)
        oHPOP.propagate()

        # Application.ExecuteCommand("Propagate */Satellite/AstgEuropa \"1 Jul 2007 12:00:00.00\" \"2 Jul 2007 12:00:00.00\" 60.0");
        AstgEuropa: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["AstgEuropa"], Satellite)
        AstgEuropa.set_propagator_type(PropagatorType.ASTROGATOR)
        astgEuropaDriver: "MCSDriver" = clr.CastAs(AstgEuropa.propagator, MCSDriver)
        astgEuropaInitialState: "MCSInitialState" = clr.CastAs(
            astgEuropaDriver.main_sequence["Initial State"], MCSInitialState
        )
        astgEuropaInitialState.orbit_epoch = "1 Jul 2007 12:00:00.000"
        astgEuropaPropagate: "MCSPropagate" = clr.CastAs(astgEuropaDriver.main_sequence["Propagate"], MCSPropagate)
        stoppingCondition = clr.CastAs(astgEuropaPropagate.stopping_conditions[0].properties, StoppingCondition)
        stoppingCondition.trip = 86400
        astgEuropaDriver.run_mcs()
        oComparator4.TakeOMSnapshot(TestBase.Application)

        # Jupiter - 1 day - VOP using step error control
        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["HpopJupiterVOP"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        Assert.assertEqual(PropagatorType.HPOP, Propagation.AG_SAT.propagator_type)
        oHPOP = None
        oHPOP = clr.CastAs(Propagation.AG_SAT.propagator, PropagatorHPOP)
        Assert.assertIsNotNone(oHPOP)
        oHPOP.ephemeris_interval.set_explicit_interval("1 Jul 2007 12:00:00.000", "2 Jul 2007 12:00:00.000")
        Assert.assertEqual("1 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_start_time())
        Assert.assertEqual("2 Jul 2007 12:00:00.000", oHPOP.ephemeris_interval.find_stop_time())
        oHPOP.step = 600.0
        Assert.assertEqual(600.0, oHPOP.step)
        oHPOP.propagate()

        #          Application.ExecuteCommand("Propagate */Satellite/AstgJupiterVOP \"1 Jul 2007 12:00:00.00\" \"2 Jul 2007 12:00:00.00\" 600.0");
        AstgJupiterVOP: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children["AstgJupiterVOP"], Satellite
        )
        AstgJupiterVOP.set_propagator_type(PropagatorType.ASTROGATOR)
        astgJupiterVOPDriver: "MCSDriver" = clr.CastAs(AstgJupiterVOP.propagator, MCSDriver)
        astgJupiterVOPInitialState: "MCSInitialState" = clr.CastAs(
            astgJupiterVOPDriver.main_sequence["Initial State"], MCSInitialState
        )
        astgJupiterVOPInitialState.orbit_epoch = "1 Jul 2007 12:00:00.000"
        astgJupiterVOPPropagate: "MCSPropagate" = clr.CastAs(
            astgJupiterVOPDriver.main_sequence["Propagate"], MCSPropagate
        )
        stoppingCondition = clr.CastAs(astgJupiterVOPPropagate.stopping_conditions[0].properties, StoppingCondition)
        stoppingCondition.trip = 86400
        astgJupiterVOPDriver.run_mcs()
        # only ask at the end, since there will be interpolation diffs because the integrator choose different nodes
        oComparator5.TakeOMSnapshot(TestBase.Application)

        # Earth 10 day Lop
        Propagation.AG_SAT = None
        Propagation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["LopEarth"])
        Assert.assertIsNotNone(Propagation.AG_SAT)
        Propagation.AG_SAT.set_propagator_type(PropagatorType.LOP)
        Assert.assertEqual(PropagatorType.LOP, Propagation.AG_SAT.propagator_type)
        oLOP: "PropagatorLOP" = clr.CastAs(Propagation.AG_SAT.propagator, PropagatorLOP)
        Assert.assertIsNotNone(oLOP)
        oLOP.ephemeris_interval.set_explicit_interval("1 Jul 2007 12:00:00.000", "10 Jul 2007 12:00:00.000")
        Assert.assertEqual("1 Jul 2007 12:00:00.000", oLOP.ephemeris_interval.find_start_time())
        Assert.assertEqual("10 Jul 2007 12:00:00.000", oLOP.ephemeris_interval.find_stop_time())
        oLOP.step = 86400.0
        Assert.assertEqual(86400.0, oLOP.step)
        oLOP.propagate()
        oComparator6.TakeOMSnapshot(TestBase.Application)

        # compare results
        try:
            oComparator1.CompareReportSnapshots()
            oComparator2.CompareReportSnapshots()
            oComparator3.CompareReportSnapshots()
            oComparator4.CompareReportSnapshots()
            oComparator5.CompareReportSnapshots()
            oComparator6.CompareReportSnapshots()

        finally:
            Propagation.InitHelper()


@category("EarlyBoundTests")

# [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
class Coordinate(TestBase):
    def __init__(self, *args, **kwargs):
        super(Coordinate, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))
            Coordinate.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        Coordinate.AG_SAT = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    # endregion

    # region Fixed
    def test_Fixed(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Coordinate.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Coordinate.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN)
        )
        cart.coordinate_system_type = CoordinateSystem.FIXED
        coordsys: "OrbitStateCoordinateSystem" = cart.coordinate_system

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 Fixed "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region J2000
    def test_J2000(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Coordinate.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Coordinate.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN)
        )
        cart.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = cart.coordinate_system

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 J2000 "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region B1950
    def test_B1950(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Coordinate.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Coordinate.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN)
        )
        cart.coordinate_system_type = CoordinateSystem.B1950
        coordsys: "OrbitStateCoordinateSystem" = cart.coordinate_system

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 B1950 "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region Date
    def test_Date(self):
        # Report initialization
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Euler Angles"')
        ComparisionUtility.ResetUnits()

        Coordinate.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Coordinate.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        #            j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN)
        )

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.coordinate_system_type = CoordinateSystem.MEAN_OF_DATE

        coordsys: "OrbitStateCoordinateSystem" = cart.coordinate_system

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.ResetUnits()

        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart = OrbitStateCartesian(j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN))

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.coordinate_system_type = CoordinateSystem.TEME_OF_DATE
        coordsys = cart.coordinate_system

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.ResetUnits()

        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart = OrbitStateCartesian(j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN))

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.coordinate_system_type = CoordinateSystem.TRUE_OF_DATE
        coordsys = cart.coordinate_system

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.ResetUnits()

        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart = OrbitStateCartesian(j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN))

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        with pytest.raises(
            Exception,
            match=RegexSubstringMatch(
                "Enumeration, must be in {AlignmentAtEpoch, B1950, Fixed, ICRF, J2000, MeanOfDate, MeanOfEpoch, TEMEOfDate, TEMEOfEpoch, TrueOfDate, TrueOfDateRotating, TrueOfEpoch}"
            ),
        ):
            cart.coordinate_system_type = CoordinateSystem.TRUE_OF_REFERENCE_DATE

        coordsys = cart.coordinate_system

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 MeanOfDate "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 TEMEOfDate "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 TrueOfDate "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region Epoch
    def test_Epoch(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Coordinate.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Coordinate.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Coordinate.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN)
        )

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.coordinate_system_type = CoordinateSystem.ALIGNMENT_AT_EPOCH
        coordsys: "OrbitStateCoordinateSystem" = cart.coordinate_system
        coordsys.coordinate_system_epoch.set_explicit_time("1 Nov 2000 00:45:00.000")

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.ResetUnits()

        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart = OrbitStateCartesian(j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN))

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.coordinate_system_type = CoordinateSystem.MEAN_OF_EPOCH
        coordsys = cart.coordinate_system
        coordsys.coordinate_system_epoch.set_explicit_time("1 Nov 2000 00:45:00.000")

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.ResetUnits()

        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart = OrbitStateCartesian(j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN))

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.coordinate_system_type = CoordinateSystem.TEME_OF_EPOCH
        coordsys = cart.coordinate_system
        coordsys.coordinate_system_epoch.set_explicit_time("1 Nov 2000 00:45:00.000")

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.ResetUnits()

        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        j2prop.step = 60
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart = OrbitStateCartesian(j2prop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN))

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.coordinate_system_type = CoordinateSystem.TRUE_OF_EPOCH
        coordsys = cart.coordinate_system
        coordsys.coordinate_system_epoch.set_explicit_time("1 Nov 2000 00:45:00.000")

        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        j2prop.initial_state.representation.assign(cart)
        j2prop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)
        ComparisionUtility.ResetUnits()

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 AlignmentAtEpoch "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768 "1 Nov 2000 00:45:00.000"'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 MeanOfEpoch "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768 "1 Nov 2000 00:45:00.000"'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 TEMEOfEpoch "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768 "1 Nov 2000 00:45:00.000"'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian J2Perturbation "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 60.0 TrueOfEpoch "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768 "1 Nov 2000 00:45:00.000"'
        )
        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)

        ComparisionUtility.CompareReportSnapshots()


@category("EarlyBoundTests")

# [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
class Representation(TestBase):
    def __init__(self, *args, **kwargs):
        super(Representation, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            Console.WriteLine("Integrity - Representation - OneTimeSetUp")
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))
            Representation.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        Representation.AG_SAT = None
        TestBase.Uninitialize()
        Console.WriteLine("Integrity - Representation - OneTimeTearDown")

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    # endregion

    # region MixedSpherical
    def test_MixedSpherical(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Propagator Inputs"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Representation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        hpop: "PropagatorHPOP" = PropagatorHPOP(Representation.AG_SAT.propagator)
        hpop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        hpop.step = 120.0
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        mixed: "OrbitStateMixedSpherical" = OrbitStateMixedSpherical(
            hpop.initial_state.representation.convert_to(OrbitStateType.MIXED_SPHERICAL)
        )

        (mixed).epoch = "1 Nov 2000 00:30:00.00"

        mixed.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = mixed.coordinate_system

        mixed.longitude = 110.0
        mixed.latitude = 0.0
        mixed.altitude = 1681000.0
        mixed.flight_path_angle_type = MixedSphericalFlightPathAngleType.HORIZONTAL
        hor: "MixedSphericalFlightPathAngleHorizontal" = MixedSphericalFlightPathAngleHorizontal(
            mixed.flight_path_angle
        )
        hor.flight_path_angle = 0.0
        mixed.azimuth = 26.5
        mixed.velocity = 7033.0

        hpop.initial_state.representation.assign(mixed)
        hpop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 MixedSpherical HPOP "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 120.0 J2000 "1 Nov 2000 00:30:00.00" 110.0 0.0 1681000.0 0.0 26.5 7033.0'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region Classical
    def test_Classical(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport2(clr.CastAs(Representation.AG_SAT, IStkObject), '"Propagator Inputs"', 0.001)
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Representation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        hpop: "PropagatorHPOP" = PropagatorHPOP(Representation.AG_SAT.propagator)
        hpop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 02:00:00.00")
        hpop.step = 120
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        classical: "OrbitStateClassical" = OrbitStateClassical(
            hpop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )

        (classical).epoch = "1 Nov 2000 02:00:00.00"

        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 8322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.079
        classical.orientation.inclination = 88.4
        classical.orientation.argument_of_periapsis = 1.8
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 132.4
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 26.4

        hpop.initial_state.representation.assign(classical)
        hpop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetStateClassical */Satellite/Satellite1 HPOP "1 Nov 2000 00:00:00.00" "1 Nov 2000 02:00:00.00" 120 J2000 "1 Nov 2000 02:00:00.00" 8322000.122 0.079 88.4 1.8 132.4 26.4'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region Cartesian
    def test_Cartesian(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Propagator Inputs"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Representation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        hpop: "PropagatorHPOP" = PropagatorHPOP(Representation.AG_SAT.propagator)
        hpop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        hpop.step = 120.0
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        cart: "OrbitStateCartesian" = OrbitStateCartesian(
            hpop.initial_state.representation.convert_to(OrbitStateType.CARTESIAN)
        )

        (cart).epoch = "1 Nov 2000 00:30:00.00"

        cart.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = cart.coordinate_system
        cart.x_position = -4485030.694
        cart.y_position = 4738911.923
        cart.z_position = 4172026.222
        cart.x_velocity = 2402.559
        cart.y_velocity = -2895.996
        cart.z_velocity = 6393.768

        hpop.initial_state.representation.assign(cart)
        Assert.assertEqual(cart.epoch, hpop.initial_state.orbit_epoch.time_instant)
        Assert.assertEqual(cart.epoch, (ITimeToolInstant(hpop.initial_state.orbit_epoch)).find_occurrence().epoch)
        Assert.assertEqual("1 Nov 2000 00:00:00.000", hpop.ephemeris_interval.find_start_time())
        Assert.assertEqual("1 Nov 2000 01:00:00.000", hpop.ephemeris_interval.find_stop_time())
        hpop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Cartesian HPOP "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 120.0 J2000 "1 Nov 2000 00:30:00.00" -4485030.694 4738911.923 4172026.222 2402.559 -2895.996 6393.768'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region Spherical
    def test_Spherical(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Propagator Inputs"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Representation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        hpop: "PropagatorHPOP" = PropagatorHPOP(Representation.AG_SAT.propagator)
        hpop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        hpop.step = 120.0
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        spher: "OrbitStateSpherical" = OrbitStateSpherical(
            hpop.initial_state.representation.convert_to(OrbitStateType.SPHERICAL)
        )

        (spher).epoch = "1 Nov 2000 00:30:00.00"

        spher.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = spher.coordinate_system

        spher.right_ascension = 133.32
        spher.declination = -71.2
        spher.radius = 7744584.2
        spher.flight_path_angle_type = SphericalFlightPathAzimuthType.HORIZONTAL
        hor: "SphericalFlightPathAngleHorizontal" = SphericalFlightPathAngleHorizontal(spher.flight_path_angle)
        hor.flight_path_angle = 2.5
        spher.azimuth = 82.4
        spher.velocity = 7418.85

        hpop.initial_state.representation.assign(spher)
        hpop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Spherical HPOP "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 120.0 J2000 "1 Nov 2000 00:30:00.00" 133.32 -71.20 7744584.2 2.5 82.4 7418.85'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()

    # endregion

    # region Equinoctial
    def test_Equinoctial(self):
        # Report initialization
        self.Units.set_current_unit("DistanceUnit", "m")
        ComparisionUtility = ReportComparison(self.Units)
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Propagator Inputs"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"LLA Position"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Cartesian Position Velocity"')
        ComparisionUtility.AddReport(clr.CastAs(Representation.AG_SAT, IStkObject), '"Euler Angles"')

        # OM Setup
        Representation.AG_SAT.set_propagator_type(PropagatorType.HPOP)
        hpop: "PropagatorHPOP" = PropagatorHPOP(Representation.AG_SAT.propagator)
        hpop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 01:00:00.00")
        hpop.step = 120.0
        # Epoch was deprecated
        # hpop.InitialState.Epoch = "1 Nov 2000 00:30:00.00";
        equin: "OrbitStateEquinoctial" = OrbitStateEquinoctial(
            hpop.initial_state.representation.convert_to(OrbitStateType.EQUINOCTIAL)
        )

        (equin).epoch = "1 Nov 2000 00:30:00.00"

        equin.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = equin.coordinate_system

        equin.size_shape_type = EquinoctialSizeShape.SEMIMAJOR_AXIS
        eqsizeshape: "EquinoctialSizeShapeSemimajorAxis" = EquinoctialSizeShapeSemimajorAxis(equin.size_shape)
        eqsizeshape.semi_major_axis = 8321993.91
        equin.h = 0.08177
        equin.k = -0.0045
        equin.p = -0.41498
        equin.q = -0.5861
        equin.mean_longitude = 122.795
        equin.formulation = EquinoctialFormulation.POSIGRADE

        hpop.initial_state.representation.assign(equin)
        hpop.propagate()

        ComparisionUtility.TakeOMSnapshot(TestBase.Application)

        # Connect Setup
        TestBase.Application.execute_command(
            'SetState */Satellite/Satellite1 Equi HPOP "1 Nov 2000 00:00:00.00" "1 Nov 2000 01:00:00.00" 120.0 J2000 "1 Nov 2000 00:30:00.00" 8321993.91 .08177 -.0045 -.41498 -.5861 122.795 Posigrade'
        )

        ComparisionUtility.TakeConnectSnapshot(TestBase.Application)
        ComparisionUtility.CompareReportSnapshots()


@category("EarlyBoundTests")

# [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
class Attitude(TestBase):
    def __init__(self, *args, **kwargs):
        super(Attitude, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))
            Attitude.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        Attitude.AG_SAT = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    # endregion

    # region InertFix
    def test_InertFix(self):
        YPRCompare = ReportComparison(self.Units)
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Yaw Pitch Roll" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Attitude Quaternions" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        EulerCompare = ReportComparison(self.Units)
        EulerCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Euler Angles" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        EulerCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Attitude Quaternions" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        QuatCompare = ReportComparison(self.Units)
        QuatCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Attitude Quaternions" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )

        # Propagator Initialization
        Attitude.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Attitude.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 4:00:00.00")
        j2prop.step = 60
        classical: "OrbitStateClassical" = OrbitStateClassical(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";

        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 7322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.099
        classical.orientation.inclination = 99.5
        classical.orientation.argument_of_periapsis = 1.2
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.2
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 22.2
        j2prop.initial_state.representation.assign(classical)
        j2prop.propagate()

        # Test Attitude
        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard: "AttitudeStandardOrbit" = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix: "AttitudeProfileInertial" = AttitudeProfileInertial(standard.basic.profile)

        quat: "IOrientationQuaternion" = IOrientationQuaternion(
            interfix.inertial.convert_to(OrientationType.QUATERNION)
        )
        quat.qx = 0.5
        quat.qy = 0.5
        quat.qz = 0.5
        quat.qs = 0.5
        interfix.inertial.assign(quat)

        QuatCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Quat 0.5 0.5 0.5 0.5")
        QuatCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        ypr: "IOrientationYPRAngles" = IOrientationYPRAngles(interfix.inertial.convert_to(OrientationType.YPR_ANGLES))
        ypr.sequence = YPRAnglesSequence.RPY
        ypr.yaw = 10.0
        ypr.pitch = 20.0
        ypr.roll = 30.0
        interfix.inertial.assign(ypr)

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix YPR 10.0 20.0 30.0 RPY")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        ypr = IOrientationYPRAngles(interfix.inertial.convert_to(OrientationType.YPR_ANGLES))
        ypr.sequence = YPRAnglesSequence.RYP
        ypr.yaw = 10.0
        ypr.pitch = 20.0
        ypr.roll = 30.0
        interfix.inertial.assign(ypr)

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix YPR 10.0 20.0 30.0 RYP")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        ypr = IOrientationYPRAngles(interfix.inertial.convert_to(OrientationType.YPR_ANGLES))
        ypr.sequence = YPRAnglesSequence.PRY
        ypr.yaw = 10.0
        ypr.pitch = 20.0
        ypr.roll = 30.0
        interfix.inertial.assign(ypr)

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix YPR 10.0 20.0 30.0 PRY")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        ypr = IOrientationYPRAngles(interfix.inertial.convert_to(OrientationType.YPR_ANGLES))
        ypr.sequence = YPRAnglesSequence.PYR
        ypr.yaw = 10.0
        ypr.pitch = 20.0
        ypr.roll = 30.0
        interfix.inertial.assign(ypr)

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix YPR 10.0 20.0 30.0 PYR")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        ypr = IOrientationYPRAngles(interfix.inertial.convert_to(OrientationType.YPR_ANGLES))
        ypr.sequence = YPRAnglesSequence.YRP
        ypr.yaw = 10.0
        ypr.pitch = 20.0
        ypr.roll = 30.0
        interfix.inertial.assign(ypr)

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix YPR 10.0 20.0 30.0 YRP")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        EulerCompare.ResetUnits()

        ypr = IOrientationYPRAngles(interfix.inertial.convert_to(OrientationType.YPR_ANGLES))
        ypr.sequence = YPRAnglesSequence.YPR
        ypr.yaw = 10.0
        ypr.pitch = 20.0
        ypr.roll = 30.0
        interfix.inertial.assign(ypr)

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix YPR 10.0 20.0 30.0 YPR")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler: "IOrientationEulerAngles" = IOrientationEulerAngles(
            interfix.inertial.convert_to(OrientationType.EULER_ANGLES)
        )
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_121
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 121")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_123
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 123")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_131
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 131")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_132
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 132")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_212
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 212")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_213
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 213")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_231
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 231")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_231
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            "SetAttitude */Satellite/Satellite1 Profile  InertFix Euler 10.0 20.0 30.0 231"
        )
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_232
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 232")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_312
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 312")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_313
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 313")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_321
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 321")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix = AttitudeProfileInertial(standard.basic.profile)

        euler = IOrientationEulerAngles(interfix.inertial.convert_to(OrientationType.EULER_ANGLES))
        euler.sequence = EulerOrientationSequenceType.SEQUENCE_323
        euler.a = 10.0
        euler.b = 20.0
        euler.c = 30.0
        interfix.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 InertFix Euler 10.0 20.0 30.0 323")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        QuatCompare.CompareReportSnapshots()
        YPRCompare.CompareReportSnapshots()
        EulerCompare.CompareReportSnapshots()

    # endregion

    # region Yaw
    def test_Yaw(self):
        YPRCompare = ReportComparison(self.Units)
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Yaw Pitch Roll" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Attitude Quaternions" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        EulerCompare = ReportComparison(self.Units)
        EulerCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Euler Angles" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        EulerCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Attitude Quaternions" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )

        # Propagator Initialization
        Attitude.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Attitude.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 4:00:00.00")
        j2prop.step = 60
        classical: "OrbitStateClassical" = OrbitStateClassical(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 7322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.099
        classical.orientation.inclination = 99.5
        classical.orientation.argument_of_periapsis = 1.2
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.2
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 22.2
        j2prop.initial_state.representation.assign(classical)
        j2prop.propagate()

        # Test Attitude
        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard: "AttitudeStandardOrbit" = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.YAW_TO_NADIR)
        inertial: "AttitudeProfileYawToNadir" = AttitudeProfileYawToNadir(standard.basic.profile)
        pr: "DirectionPR" = DirectionPR(inertial.inertial.convert_to(DirectionType.PR))
        pr.pitch = 10.0
        pr.roll = 20.0
        inertial.inertial.assign(pr)

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 YawNadir PR 10.0 20.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.YAW_TO_NADIR)
        inertial = AttitudeProfileYawToNadir(standard.basic.profile)

        spher: "DirectionRADec" = DirectionRADec(inertial.inertial.convert_to(DirectionType.RA_DEC))
        spher.ra = 10.0
        spher.dec = 20.0
        inertial.inertial.assign(spher)

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 YawNadir RaDec 10.0 20.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.YAW_TO_NADIR)
        inertial = AttitudeProfileYawToNadir(standard.basic.profile)

        euler: "DirectionEuler" = DirectionEuler(inertial.inertial.convert_to(DirectionType.EULER))
        euler.sequence = EulerDirectionSequence.SEQUENCE_12
        euler.b = 10.0
        euler.c = 20.0
        inertial.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 YawNadir Euler 10.0 20.0 12")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.YAW_TO_NADIR)
        inertial = AttitudeProfileYawToNadir(standard.basic.profile)

        euler = DirectionEuler(inertial.inertial.convert_to(DirectionType.EULER))
        euler.sequence = EulerDirectionSequence.SEQUENCE_21
        euler.b = 10.0
        euler.c = 20.0
        inertial.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitude */Satellite/Satellite1 Profile YawNadir Euler 10.0 20.0 21")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.YAW_TO_NADIR)
        inertial = AttitudeProfileYawToNadir(standard.basic.profile)

        euler = DirectionEuler(inertial.inertial.convert_to(DirectionType.EULER))
        euler.sequence = EulerDirectionSequence.SEQUENCE_31
        euler.b = 10.0
        euler.c = 20.0
        inertial.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 YawNadir Euler 10.0 20.0 31")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.YAW_TO_NADIR)
        inertial = AttitudeProfileYawToNadir(standard.basic.profile)

        euler = DirectionEuler(inertial.inertial.convert_to(DirectionType.EULER))
        euler.sequence = EulerDirectionSequence.SEQUENCE_32
        euler.b = 10.0
        euler.c = 20.0
        inertial.inertial.assign(euler)

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 YawNadir Euler 10.0 20.0 32")
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        YPRCompare.CompareReportSnapshots()
        EulerCompare.CompareReportSnapshots()

    # endregion

    # region Spin
    def test_Spin(self):
        YPRCompare = ReportComparison(self.Units)
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Yaw Pitch Roll" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        # YPRCompare.AddReport(AG_SAT, "\"Attitude Quaternions\" \"1 Nov 2000 00:00:00.00\" \"1 Nov 2000 00:02:00.00\" 60");
        EulerCompare = ReportComparison(self.Units)
        EulerCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Euler Angles" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        EulerCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Attitude Quaternions" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )

        # Propagator Initialization
        Attitude.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Attitude.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 4:00:00.00")
        j2prop.step = 60
        classical: "OrbitStateClassical" = OrbitStateClassical(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 7322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.099
        classical.orientation.inclination = 99.5
        classical.orientation.argument_of_periapsis = 1.2
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.2
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 22.2
        j2prop.initial_state.representation.assign(classical)
        j2prop.propagate()

        # Test Attitude
        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard: "AttitudeStandardOrbit" = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SPIN_ABOUT_NADIR)
        spin: "AttitudeProfileSpinAboutSettings" = AttitudeProfileSpinAboutSettings(standard.basic.profile)
        spin.smart_epoch.set_explicit_time("1 nov 2000 00:00:00")
        spin.offset = 10.0
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        spin.rate = 1.4
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetAttitudeType */Satellite/Satellite1 SpinNadir 1.4 10.0 "1 nov 2000 00:00:00"'
        )
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SPIN_ABOUT_SUN_VECTOR)
        spin = AttitudeProfileSpinAboutSettings(standard.basic.profile)

        spin.smart_epoch.set_explicit_time("1 nov 2000 00:00:00")
        spin.offset = 10.0
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        spin.rate = 1.4
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetAttitudeType */Satellite/Satellite1 SpinSun 1.4 10.0 "1 nov 2000 00:00:00"'
        )
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        # Spinning
        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SPINNING)
        spinning: "AttitudeProfileSpinning" = AttitudeProfileSpinning(standard.basic.profile)

        pr: "DirectionPR" = DirectionPR(spinning.inertial.convert_to(DirectionType.PR))
        pr.pitch = 10.0
        pr.roll = 20.0
        spinning.inertial.assign(pr)

        spinning.smart_epoch.set_explicit_time("1 nov 2000 00:00:00")
        spinning.offset = 10.0
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        spinning.rate = 1.4
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetAttitudeType */Satellite/Satellite1 Spinning PR 10.0 20.0 1.4 10.0 "1 nov 2000 00:00:00"'
        )
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SPINNING)
        spinning = AttitudeProfileSpinning(standard.basic.profile)

        spher: "DirectionRADec" = DirectionRADec(spinning.inertial.convert_to(DirectionType.RA_DEC))
        spher.ra = 10.0
        spher.dec = 20.0
        spinning.inertial.assign(spher)

        spinning.smart_epoch.set_explicit_time("1 nov 2000 00:00:00")
        spinning.offset = 10.0
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        spinning.rate = 1.4
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetAttitudeType */Satellite/Satellite1 Spinning RaDec 10.0 20.0 1.4 10.0 "1 nov 2000 00:00:00"'
        )
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SPINNING)
        spinning = AttitudeProfileSpinning(standard.basic.profile)

        euler: "DirectionEuler" = DirectionEuler(spinning.inertial.convert_to(DirectionType.EULER))
        euler.sequence = EulerDirectionSequence.SEQUENCE_12
        euler.b = 10.0
        euler.c = 20.0
        spinning.inertial.assign(euler)

        spinning.smart_epoch.set_explicit_time("1 nov 2000 00:00:00")
        spinning.offset = 10.0
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        spinning.rate = 1.4
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetAttitudeType */Satellite/Satellite1 Spinning Euler 10.0 20.0 12 1.4 10.0 "1 nov 2000 00:00:00"'
        )
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SPINNING)
        spinning = AttitudeProfileSpinning(standard.basic.profile)

        euler = DirectionEuler(spinning.inertial.convert_to(DirectionType.EULER))
        euler.sequence = EulerDirectionSequence.SEQUENCE_21
        euler.b = 10.0
        euler.c = 20.0
        spinning.inertial.assign(euler)

        spinning.smart_epoch.set_explicit_time("1 nov 2000 00:00:00")
        spinning.offset = 10.0
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        spinning.rate = 1.4
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetAttitudeType */Satellite/Satellite1 Spinning Euler 10.0 20.0 21 1.4 10.0 "1 nov 2000 00:00:00"'
        )
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SPINNING)
        spinning = AttitudeProfileSpinning(standard.basic.profile)

        euler = DirectionEuler(spinning.inertial.convert_to(DirectionType.EULER))
        euler.sequence = EulerDirectionSequence.SEQUENCE_31
        euler.b = 10.0
        euler.c = 20.0
        spinning.inertial.assign(euler)

        spinning.smart_epoch.set_explicit_time("1 nov 2000 00:00:00")
        spinning.offset = 10.0
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        spinning.rate = 1.4
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetAttitudeType */Satellite/Satellite1 Spinning Euler 10.0 20.0 31 1.4 10.0 "1 nov 2000 00:00:00"'
        )
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SPINNING)
        spinning = AttitudeProfileSpinning(standard.basic.profile)

        euler = DirectionEuler(spinning.inertial.convert_to(DirectionType.EULER))
        euler.sequence = EulerDirectionSequence.SEQUENCE_32
        euler.b = 10.0
        euler.c = 20.0
        spinning.inertial.assign(euler)

        spinning.smart_epoch.set_explicit_time("1 nov 2000 00:00:00")
        spinning.offset = 10.0
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        spinning.rate = 1.4
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")

        EulerCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command(
            'SetAttitudeType */Satellite/Satellite1 Spinning Euler 10.0 20.0 32 1.4 10.0 "1 nov 2000 00:00:00"'
        )
        EulerCompare.TakeConnectSnapshot(TestBase.Application)

        YPRCompare.CompareReportSnapshots()
        EulerCompare.CompareReportSnapshots()

    # endregion

    # region Sun
    def test_Sun(self):
        YPRCompare = ReportComparison(self.Units)
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Yaw Pitch Roll" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Attitude Quaternions" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )

        # Propagator Initialization
        Attitude.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Attitude.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 4:00:00.00")
        j2prop.step = 60
        classical: "OrbitStateClassical" = OrbitStateClassical(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 7322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.099
        classical.orientation.inclination = 99.5
        classical.orientation.argument_of_periapsis = 1.2
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.2
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 22.2
        j2prop.initial_state.representation.assign(classical)
        j2prop.propagate()

        # Test Attitude
        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard: "AttitudeStandardOrbit" = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SUN_ALIGNMENT_WITH_NADIR_CONSTRAINT)
        constraint: "AttitudeProfileAlignmentOffset" = AttitudeProfileAlignmentOffset(standard.basic.profile)
        constraint.alignment_offset = 20.0
        j2prop.propagate()

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitude */Satellite/Satellite1 Profile SunNadir 20.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SUN_ALIGNMENT_WITH_ECLIPTIC_NORMAL_CONSTRAINT)
        constraint = AttitudeProfileAlignmentOffset(standard.basic.profile)
        constraint.alignment_offset = 10.0

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 SunEcliptic 10.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SUN_ALIGNMENT_WITH_INERTIAL_Z_AXIS_CONSTRAINT)
        constraint = AttitudeProfileAlignmentOffset(standard.basic.profile)
        constraint.alignment_offset = 10.0

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 SunEciZ 10.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.SUN_ALIGNMENT_OCCULTATION_NORMAL_CONSTRAINT)
        constraint = AttitudeProfileAlignmentOffset(standard.basic.profile)
        constraint.alignment_offset = 10.0

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 SunOccult 10.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        YPRCompare.CompareReportSnapshots()

    # endregion

    # region Nadir
    def test_Nadir(self):
        # Report initialization
        YPRCompare = ReportComparison(self.Units)
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Yaw Pitch Roll" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )
        YPRCompare.AddReport(
            clr.CastAs(Attitude.AG_SAT, IStkObject),
            '"Attitude Quaternions" "1 Nov 2000 00:00:00.00" "1 Nov 2000 00:02:00.00" 60',
        )

        # Propagator Initialization
        Attitude.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Attitude.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 4:00:00.00")
        j2prop.step = 60
        classical: "OrbitStateClassical" = OrbitStateClassical(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 7322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.099
        classical.orientation.inclination = 99.5
        classical.orientation.argument_of_periapsis = 1.2
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.2
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 22.2
        j2prop.initial_state.representation.assign(classical)

        # Nadir
        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard: "AttitudeStandardOrbit" = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.NADIR_ALIGNMENT_WITH_INERTIAL_VELOCITY_CONSTRAINT)
        constraint: "AttitudeProfileConstraintOffset" = AttitudeProfileConstraintOffset(standard.basic.profile)
        constraint.constraint_offset = 20.0

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitude */Satellite/Satellite1 Profile NadirEciVel 20.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.NADIR_ALIGNMENT_WITH_FIXED_VELOCITY_CONSTRAINT)
        constraint = AttitudeProfileConstraintOffset(standard.basic.profile)
        constraint.constraint_offset = 10.0

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 NadirEcfVel 10.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.NADIR_ALIGNMENT_WITH_SUN_CONSTRAINT)
        constraint = AttitudeProfileConstraintOffset(standard.basic.profile)
        constraint.constraint_offset = 10.0
        j2prop.propagate()

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 NadirSun 10.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.NADIR_ALIGNMENT_WITH_ORBIT_NORMAL_CONSTRAINT)
        constraint = AttitudeProfileConstraintOffset(standard.basic.profile)
        constraint.constraint_offset = 10.0

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 NadirOrbit 10.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.INERTIAL_VELOCITY_ALIGNMENT_WITH_NADIR_CONSTRAINT)
        constraint = AttitudeProfileConstraintOffset(standard.basic.profile)
        constraint.constraint_offset = 10.0
        j2prop.propagate()

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 EciVelNadir 10.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        Attitude.AG_SAT.set_attitude_type(VehicleAttitude.STANDARD)
        standard = AttitudeStandardOrbit(Attitude.AG_SAT.attitude)
        standard.basic.set_profile_type(AttitudeProfile.FIXED_VELOCITY_ALIGNMENT_WITH_NADIR_CONSTRAINT)
        constraint = AttitudeProfileConstraintOffset(standard.basic.profile)
        constraint.constraint_offset = 10.0

        YPRCompare.TakeOMSnapshot(TestBase.Application)
        TestBase.Application.execute_command("SetAttitudeType */Satellite/Satellite1 EcfVelNadir 10.0")
        YPRCompare.TakeConnectSnapshot(TestBase.Application)

        YPRCompare.CompareReportSnapshots()

    # endregion

    # region Slew
    # BUG76799 [Test]
    def Slew(self):
        fac: "Facility" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "FacSlew"), Facility
        )
        fac.position.assign_geodetic(0.0, 0.0, 0.0)

        miss: "Missile" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.MISSILE, "MissSlew"), Missile
        )
        miss.set_trajectory_type(PropagatorType.BALLISTIC)
        ballistic: "PropagatorBallistic" = clr.CastAs(miss.trajectory, PropagatorBallistic)
        ballistic.step = 60.0
        ballistic.propagate()

        miss.set_attitude_type(VehicleAttitude.STANDARD)
        trajAttStandard: "AttitudeStandardTrajectory" = clr.CastAs(miss.attitude, AttitudeStandardTrajectory)
        trajAttStandard.pointing.use_target_pointing = True
        trajAttStandard.pointing.targets.add("Facility/FacSlew")
        trajAttStandard.pointing.target_slew.set_slew_mode_type(VehicleSlewMode.FIXED_RATE)

        realtimeCompare = ReportComparison(self.Units)
        # realtimeCompare.AddReport(miss as IStkObject, "\"Attitude Quaternions\" \"1 Jul 1999 00:00:00.00\" \"2 Jul 1999 00:00:00.00\" 60.0");
        realtimeCompare.AddReport(
            clr.CastAs(miss, IStkObject),
            '"Attitude Schedule"    "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 60.0',
        )
        realtimeCompare.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetAttitude */Missile/MissSlew Standard")
        TestBase.Application.execute_command("SetAttitude */Missile/MissSlew Target On")
        TestBase.Application.execute_command("SetAttitude */Missile/MissSlew Target ADD Facility/FacSlew")
        TestBase.Application.execute_command("SetAttitude */Missile/MissSlew Target Slew Mode FixedRate")

        realtimeCompare.TakeConnectSnapshot(TestBase.Application)
        realtimeCompare.CompareReportSnapshots()

    # endregion

    # region Realtime
    def test_Realtime(self):
        startTime: typing.Any = "1 Jul 1999 00:00:00.000"
        stopTime: typing.Any = "2 Jul 1999 00:00:00.000"

        TestBase.Application.units_preferences.set_current_unit("DateFormat", "UTCG")
        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "m")
        TestBase.Application.units_preferences.set_current_unit("AngleUnit", "deg")
        TestBase.Application.execute_command("SetUnits / Meter Second UTCG Degrees Degrees")

        # Create satellite
        testSat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "TestSatellite"), Satellite
        )
        testSat.set_propagator_type(PropagatorType.TWO_BODY)
        twoBody: "PropagatorTwoBody" = clr.CastAs(testSat.propagator, PropagatorTwoBody)
        twoBody.propagate()

        # Configure realtime attitude
        testSat.set_attitude_type(VehicleAttitude.REAL_TIME)
        attitude: "VehicleAttitudeRealTime" = clr.CastAs(testSat.attitude, VehicleAttitudeRealTime)
        attitude.look_ahead_method = VehicleLookAheadMethod.HOLD
        attitude.duration.look_ahead = 1800
        attitude.duration.look_behind = 1800
        attitude.block_factor = 20
        attitude.data_reference.set_profile_type(AttitudeProfile.FIXED_IN_AXES)
        profile: "AttitudeProfileFixedInAxes" = clr.CastAs(attitude.data_reference.profile, AttitudeProfileFixedInAxes)
        profile.reference_axes = "CentralBody/Earth Fixed"
        profile.orientation.assign_quaternion(0, 0, 0, 1)

        # Add attitude info
        attitude.add_euler_angles("1 Jul 1999 00:00:00.000", "321", 0, 0, 0)
        attitude.add_quaternion_relative_to_central_body_fixed("1 Jul 1999 00:01:00.000", 1, 0, 0, 0)
        attitude.add_ypr_angles_relative_to_central_body_inertial("1 Jul 1999 00:02:00.000", "231", 30.0, 45.0, 60.0)
        attitude.add_quaternion("1 Jul 1999 00:03:00.000", 0, 1, 0, 0)
        attitude.add_ypl_angles("1 Jul 1999 00:04:00.000", "123", 0.1, 0.1, 0.1)

        realtimeCompare = ReportComparison(self.Units)
        realtimeCompare.AddReport(
            clr.CastAs(testSat, IStkObject),
            '"Attitude Quaternions" "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 60',
        )
        realtimeCompare.TakeOMSnapshot(TestBase.Application)

        attitude.clear_all()

        # Configure realtime attitude
        TestBase.Application.execute_command("SETATTITUDE */Satellite/TestSatellite RealTime Hold 1800 1800 20")
        TestBase.Application.execute_command(
            'SETATTITUDE */Satellite/TestSatellite DataReference Fixed Quat 0 0 0 1 "CentralBody/Earth Fixed"'
        )

        # Add attitude info
        TestBase.Application.execute_command(
            'ADDATTITUDE */Satellite/TestSatellite EULER   "1 Jul 1999 00:00:00.000" 321 0 0 0'
        )
        TestBase.Application.execute_command(
            'ADDATTITUDE */Satellite/TestSatellite CBFQUAT "1 Jul 1999 00:01:00.000" 1 0 0 0'
        )
        TestBase.Application.execute_command(
            'ADDATTITUDE */Satellite/TestSatellite ECIYPR  "1 Jul 1999 00:02:00.000" 231 30.0 45.0 60.0'
        )
        TestBase.Application.execute_command(
            'ADDATTITUDE */Satellite/TestSatellite QUAT    "1 Jul 1999 00:03:00.000" 0 1 0 0'
        )
        TestBase.Application.execute_command(
            'ADDATTITUDE */Satellite/TestSatellite YPR     "1 Jul 1999 00:04:00.000" 123 0.1 0.1 0.1'
        )

        # Compare results
        realtimeCompare.TakeConnectSnapshot(TestBase.Application)
        realtimeCompare.CompareReportSnapshots()


@category("EarlyBoundTests")

# [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
class Pointing(TestBase):
    def __init__(self, *args, **kwargs):
        super(Pointing, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            Console.WriteLine("Integrity - Pointing - OneTimeSetUp 1")
            TestBase.Initialize()
            Console.WriteLine("Integrity - Pointing - OneTimeSetUp 2")
            TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))
            Console.WriteLine("Integrity - Pointing - OneTimeSetUp 3")
            Pointing.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])
            Console.WriteLine("Integrity - Pointing - OneTimeSetUp 4")
            Pointing.AG_SN1 = Sensor(TestBase.Application.current_scenario.children["Facility1"].children["Sensor1"])
            Console.WriteLine("Integrity - Pointing - OneTimeSetUp 5")
            Pointing.AG_SN2 = Sensor(TestBase.Application.current_scenario.children["Satellite1"].children["Sensor2"])
            Console.WriteLine("Integrity - Pointing - OneTimeSetUp 6")

        except Exception as e:
            Console.WriteLine(("Integrity - Pointing - OneTimeSetUp before throw " + str(e)))
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        Console.WriteLine("Integrity - Pointing - OneTimeTearDown begin")
        TestBase.Uninitialize()
        Console.WriteLine("Integrity - Pointing - OneTimeTearDown end")

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    AG_SN1: "Sensor" = None
    AG_SN2: "Sensor" = None
    # endregion

    # region Fixed
    def test_Fixed(self):
        Console.WriteLine("Integrity - Pointing - Fixed")
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 00:50:00.00" "1 Jul 1999 00:50:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 01:05:00.00" "1 Jul 1999 01:05:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 01:03:00.00" "1 Jul 1999 01:03:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Boresight AzEl" "1 Jul 1999 01:00:00.00" "1 Jul 1999 01:00:00.00" 60.0',
        )

        TestBase.Application.execute_command("Point */Facility/Facility1/Sensor/Sensor1 Fixed AzEl 10.0 -45.0")
        TestBase.Application.execute_command("Point */Satellite/Satellite1/Sensor/Sensor2 Fixed AzEl 10.0 75.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed: "SensorPointingFixed" = SensorPointingFixed(Pointing.AG_SN1.pointing)
        oOrientation: "IOrientation" = oFixed.orientation
        oAzEl: "IOrientationAzEl" = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))
        oAzEl.azimuth = 10.0
        oAzEl.elevation = -45.0
        oOrientation.assign(oAzEl)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN2.pointing)
        oOrientation = oFixed.orientation
        oAzEl = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))
        oAzEl.azimuth = 10.0
        oAzEl.elevation = 75.0
        oOrientation.assign(oAzEl)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Fixed Euler 321 90.0 125.0 -45.0"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Fixed Euler 321 90.0 125.0 -125.0"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN1.pointing)
        oOrientation = oFixed.orientation
        oEuler: "IOrientationEulerAngles" = IOrientationEulerAngles(
            oOrientation.convert_to(OrientationType.EULER_ANGLES)
        )
        oEuler.sequence = EulerOrientationSequenceType.SEQUENCE_321
        oEuler.a = 90.0
        oEuler.b = 125.0
        oEuler.c = -45.0
        oOrientation.assign(oEuler)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN2.pointing)
        oOrientation = oFixed.orientation
        oEuler = IOrientationEulerAngles(oOrientation.convert_to(OrientationType.EULER_ANGLES))
        oEuler.sequence = EulerOrientationSequenceType.SEQUENCE_321
        oEuler.a = 90.0
        oEuler.b = 125.0
        oEuler.c = -125.0
        oOrientation.assign(oEuler)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Fixed YPR 321 150.0 -160.0 50.0"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Fixed YPR 321 150.0 -60.0 50.0"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN1.pointing)
        oOrientation = oFixed.orientation
        oYPR: "IOrientationYPRAngles" = IOrientationYPRAngles(oOrientation.convert_to(OrientationType.YPR_ANGLES))
        oYPR.sequence = YPRAnglesSequence.YPR
        oYPR.yaw = 150.0
        oYPR.pitch = -160.0
        oYPR.roll = 50.0
        oOrientation.assign(oYPR)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN2.pointing)
        oOrientation = oFixed.orientation
        oYPR = IOrientationYPRAngles(oOrientation.convert_to(OrientationType.YPR_ANGLES))

        oYPR.sequence = YPRAnglesSequence.YPR
        oYPR.yaw = 150.0
        oYPR.pitch = -60.0
        oYPR.roll = 50.0
        oOrientation.assign(oYPR)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Fixed Quaternion -0.34298 -0.470812 0.70345 0.40725"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Fixed Quaternion -0.34298 -0.470812 0.70345 0.40725"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN1.pointing)
        oOrientation = oFixed.orientation
        oQuater: "IOrientationQuaternion" = IOrientationQuaternion(oOrientation.convert_to(OrientationType.QUATERNION))

        oQuater.qx = -0.34298
        oQuater.qy = -0.470812
        oQuater.qz = 0.70345
        oQuater.qs = 0.40725
        oOrientation.assign(oQuater)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN2.pointing)
        oOrientation = oFixed.orientation
        oQuater = IOrientationQuaternion(oOrientation.convert_to(OrientationType.QUATERNION))

        oQuater.qx = -0.34298
        oQuater.qy = -0.470812
        oQuater.qz = 0.70345
        oQuater.qs = 0.40725
        oOrientation.assign(oQuater)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Point */Facility/Facility1/Sensor/Sensor1 Fixed AzEl 10.0 -45.0 Rotate")
        TestBase.Application.execute_command("Point */Satellite/Satellite1/Sensor/Sensor2 Fixed AzEl 10.0 75.0 Hold")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN1.pointing)
        oOrientation = oFixed.orientation
        oAzEl = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))

        oAzEl.azimuth = 10.0
        oAzEl.elevation = -45.0
        oAzEl.about_boresight = AzElAboutBoresight.ROTATE
        oOrientation.assign(oAzEl)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.FIXED_IN_PARENT_BODY_AXES)
        oFixed = SensorPointingFixed(Pointing.AG_SN2.pointing)
        oOrientation = oFixed.orientation
        oAzEl = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))

        oAzEl.azimuth = 10.0
        oAzEl.elevation = 75.0
        oAzEl.about_boresight = AzElAboutBoresight.HOLD
        oOrientation.assign(oAzEl)

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()
        Console.WriteLine("Integrity - Pointing - Fixed - End")

    # endregion

    # region FixedInAxes
    def test_FixedInAxes(self):
        Console.WriteLine("Integrity - Pointing - FixedInAxes")
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 01:00:00.00" "1 Jul 1999 01:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 12:00:00.00" "1 Jul 1999 12:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 02:30:00.00" "1 Jul 1999 02:30:00.00" 60.0',
        )

        Pointing.AG_SN1.set_pointing_type(SensorPointing.FIXED_IN_AXES)
        oFixedAxes: "SensorPointingFixedInAxes" = SensorPointingFixedInAxes(Pointing.AG_SN1.pointing)
        quat: "IOrientationQuaternion" = IOrientationQuaternion(
            oFixedAxes.orientation.convert_to(OrientationType.QUATERNION)
        )
        quat.qx = -0.34298
        quat.qy = -0.470812
        quat.qz = 0.70345
        quat.qs = 0.40725
        oFixedAxes.orientation.assign(quat)
        oFixedAxes.reference_axes = "CentralBody/Sun MOJ2000 Axes"

        Pointing.AG_SN2.set_pointing_type(SensorPointing.FIXED_IN_AXES)
        oFixedAxes = SensorPointingFixedInAxes(Pointing.AG_SN2.pointing)
        quat = IOrientationQuaternion(oFixedAxes.orientation.convert_to(OrientationType.QUATERNION))
        quat.qx = -0.34298
        quat.qy = -0.470812
        quat.qz = 0.70345
        quat.qs = 0.40725
        oFixedAxes.orientation.assign(quat)
        oFixedAxes.reference_axes = "CentralBody/Sun MOJ2000 Axes"

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'Point */Facility/Facility1/Sensor/Sensor1 FixedInRef Quaternion -0.34298 -0.470812 0.70345 0.40725 "CentralBody/Sun MOJ2000"'
        )
        TestBase.Application.execute_command(
            'Point */Satellite/Satellite1/Sensor/Sensor2 FixedInRef Quaternion -0.34298 -0.470812 0.70345 0.40725 "CentralBody/Sun MOJ2000"'
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()
        Console.WriteLine("Integrity - Pointing - FixedInAxes - End")

    # endregion

    # region Spinning
    def test_Spinning(self):
        Console.WriteLine("Integrity - Pointing - Spinning")
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 01:00:00.00" "1 Jul 1999 01:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 12:00:00.00" "1 Jul 1999 12:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 02:30:00.00" "1 Jul 1999 02:30:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Boresight AzEl" "1 Jul 1999 01:00:00.00" "1 Jul 1999 01:00:00.00" 60.0',
        )

        Pointing.AG_SN1.set_pointing_type(SensorPointing.SPINNING)
        oSpinning: "SensorPointingSpinning" = SensorPointingSpinning(Pointing.AG_SN1.pointing)

        oSpinning.spin_axis_azimuth = 12.34
        oSpinning.spin_axis_elevation = 9.87654321
        oSpinning.spin_axis_cone_angle = 43.21
        oSpinning.scan_mode = SensorScanMode.CONTINUOUS
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        oSpinning.spin_rate = 98.7654321
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")
        oSpinning.offset_angle = 123.456789

        Pointing.AG_SN2.set_pointing_type(SensorPointing.SPINNING)
        oSpinning = SensorPointingSpinning(Pointing.AG_SN2.pointing)

        oSpinning.spin_axis_azimuth = 12.34
        oSpinning.spin_axis_elevation = 9.87654321
        oSpinning.spin_axis_cone_angle = 43.21
        oSpinning.scan_mode = SensorScanMode.CONTINUOUS
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        oSpinning.spin_rate = 98.7654321
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")
        oSpinning.offset_angle = 123.456789

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Spinning 12.34 9.87654321 43.21 Continuous 98.7654321 123.456789"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Spinning 12.34 9.87654321 43.21 Continuous 98.7654321 123.456789"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.SPINNING)
        oSpinning = SensorPointingSpinning(Pointing.AG_SN1.pointing)

        oSpinning.spin_axis_azimuth = 9.34
        oSpinning.spin_axis_elevation = 8.876543
        oSpinning.spin_axis_cone_angle = 35.21
        oSpinning.scan_mode = SensorScanMode.BIDIRECTIONAL
        oSpinning.clock_angle_start = -100.456789
        oSpinning.clock_angle_stop = 70.456789
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        oSpinning.spin_rate = 88.7654321
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")
        oSpinning.offset_angle = 100.456789

        Pointing.AG_SN2.set_pointing_type(SensorPointing.SPINNING)
        oSpinning = SensorPointingSpinning(Pointing.AG_SN2.pointing)

        oSpinning.spin_axis_azimuth = 9.34
        oSpinning.spin_axis_elevation = 8.876543
        oSpinning.spin_axis_cone_angle = 35.21
        oSpinning.scan_mode = SensorScanMode.BIDIRECTIONAL
        oSpinning.clock_angle_start = -100.456789
        oSpinning.clock_angle_stop = 70.456789
        self.Units.set_current_unit("AngleUnit", "revs")
        self.Units.set_current_unit("TimeUnit", "min")
        oSpinning.spin_rate = 88.7654321
        self.Units.set_current_unit("AngleUnit", "deg")
        self.Units.set_current_unit("TimeUnit", "sec")
        oSpinning.offset_angle = 100.456789

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Spinning 9.34 8.876543 35.21 Bidirectional -100.456789 70.456789 88.7654321 100.456789"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Spinning 9.34 8.876543 35.21 Bidirectional -100.456789 70.456789 88.7654321 100.456789"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()
        Console.WriteLine("Integrity - Pointing - Spinning - End")

    # endregion

    # region Targeted
    def test_Targeted(self):
        Console.WriteLine("Integrity - Pointing - Targeted")
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 01:00:00.00" "1 Jul 1999 01:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 12:00:00.00" "1 Jul 1999 12:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 02:30:00.00" "1 Jul 1999 02:30:00.00" 60.0',
        )

        TestBase.Application.execute_command("Define */Satellite/Satellite1/Sensor/Sensor2 SimpleCone 40.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN2.set_pattern_type(SensorPattern.SIMPLE_CONIC)
        patterndata: "SensorSimpleConicPattern" = SensorSimpleConicPattern(Pointing.AG_SN2.pattern)
        patterndata.cone_angle = 40.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted Tracking Satellite/Satellite1"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Tracking Facility/Facility1"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.TARGETED)
        oTarget: "SensorPointingTargeted" = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.TRACKING
        oTargetCollection: "SensorTargetCollection" = oTarget.targets
        oTargetCollection.remove_all()
        oTargetCollection.add("*/Satellite/Satellite1")

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.TRACKING
        oTargetCollection = oTarget.targets
        oTargetCollection.remove_all()
        oTargetCollection.add("*/Facility/Facility1")

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted Tracking Satellite/Satellite1 Level"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Tracking Facility/Facility1 Hold"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.TRACKING
        oTracking: "SensorPointingTargetedBoresightTrack" = SensorPointingTargetedBoresightTrack(oTarget.boresight_data)
        oTracking.about_boresight = BoresightType.LEVEL
        oTargetCollection = oTarget.targets

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.TRACKING
        oTracking = SensorPointingTargetedBoresightTrack(oTarget.boresight_data)
        oTracking.about_boresight = BoresightType.HOLD
        oTargetCollection = oTarget.targets

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted Fixed Satellite/Satellite1 AzEl 12.0 -45.0"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Fixed Facility/Facility1 AzEl 10.0 75.0"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed: "SensorPointingTargetedBoresightFixed" = SensorPointingTargetedBoresightFixed(
            oTarget.boresight_data
        )
        oOrientation: "IOrientation" = oBrstFixed.orientation
        oAzEl: "IOrientationAzEl" = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))

        oAzEl.azimuth = 12.0
        oAzEl.elevation = -45.0
        oAzEl.about_boresight = AzElAboutBoresight.ROTATE
        oOrientation.assign(oAzEl)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oAzEl = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))

        oAzEl.azimuth = 10.0
        oAzEl.elevation = 75.0
        oAzEl.about_boresight = AzElAboutBoresight.ROTATE
        oOrientation.assign(oAzEl)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted Fixed Satellite/Satellite1 Quaternion -0.34298 -0.470812 0.70345 0.40725"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Fixed Facility/Facility1 Quaternion -0.34298 -0.470812 0.70345 0.40725"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oQuater: "IOrientationQuaternion" = IOrientationQuaternion(oOrientation.convert_to(OrientationType.QUATERNION))

        oQuater.qx = -0.34298
        oQuater.qy = -0.470812
        oQuater.qz = 0.70345
        oQuater.qs = 0.40725
        oOrientation.assign(oQuater)
        oTargetCollection = oTarget.targets

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oQuater = IOrientationQuaternion(oOrientation.convert_to(OrientationType.QUATERNION))

        oQuater.qx = -0.34298
        oQuater.qy = -0.470812
        oQuater.qz = 0.70345
        oQuater.qs = 0.40725
        oOrientation.assign(oQuater)
        oTargetCollection = oTarget.targets

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted Fixed Satellite/Satellite1 Euler 232 100.0 130.0 -95.0"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Fixed Facility/Facility1 Euler 232 140.0 132.0 -141.0"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oEuler: "IOrientationEulerAngles" = IOrientationEulerAngles(
            oOrientation.convert_to(OrientationType.EULER_ANGLES)
        )

        oEuler.sequence = EulerOrientationSequenceType.SEQUENCE_232
        oEuler.a = 100.0
        oEuler.b = 130.0
        oEuler.c = -95.0
        oOrientation.assign(oEuler)
        oTargetCollection = oTarget.targets

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oEuler = IOrientationEulerAngles(oOrientation.convert_to(OrientationType.EULER_ANGLES))

        oEuler.sequence = EulerOrientationSequenceType.SEQUENCE_232
        oEuler.a = 140.0
        oEuler.b = 132.0
        oEuler.c = -141.0
        oOrientation.assign(oEuler)
        oTargetCollection = oTarget.targets

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted Fixed Satellite/Satellite1 YPR 123 -8.5 -15.0 135.0"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Fixed Facility/Facility1 YPR 123 116 5.68 -71"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oYPR: "IOrientationYPRAngles" = IOrientationYPRAngles(oOrientation.convert_to(OrientationType.YPR_ANGLES))

        oYPR.sequence = YPRAnglesSequence.RPY
        oYPR.yaw = -8.5
        oYPR.pitch = -15.0
        oYPR.roll = 135.0
        oOrientation.assign(oYPR)
        oTargetCollection = oTarget.targets

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oYPR = IOrientationYPRAngles(oOrientation.convert_to(OrientationType.YPR_ANGLES))

        oYPR.sequence = YPRAnglesSequence.RPY
        oYPR.yaw = 116
        oYPR.pitch = 5.68
        oYPR.roll = -71
        oOrientation.assign(oYPR)
        oTargetCollection = oTarget.targets

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted Fixed Satellite/Satellite1 AzEl 12.0 -45.0 Hold"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Fixed Facility/Facility1 AzEl 10.0 75.0 Rotate"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN1.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oAzEl = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))

        oAzEl.azimuth = 12.0
        oAzEl.elevation = -45.0
        oAzEl.about_boresight = AzElAboutBoresight.HOLD
        oOrientation.assign(oAzEl)
        oTargetCollection = oTarget.targets

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oAzEl = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))

        oAzEl.azimuth = 10.0
        oAzEl.elevation = 75.0
        oAzEl.about_boresight = AzElAboutBoresight.ROTATE
        oOrientation.assign(oAzEl)
        oTargetCollection = oTarget.targets

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Fixed Facility/Facility1 AzEl 0.0 90.0"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.FIXED
        oBrstFixed = SensorPointingTargetedBoresightFixed(oTarget.boresight_data)
        oOrientation = oBrstFixed.orientation
        oAzEl = IOrientationAzEl(oOrientation.convert_to(OrientationType.AZ_EL))

        oAzEl.azimuth = 0.0
        oAzEl.elevation = 90.0
        oOrientation.assign(oAzEl)
        oTargetCollection = oTarget.targets

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        secondSat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "SecondSat"), Satellite
        )
        twoBody: "PropagatorTwoBody" = clr.CastAs(secondSat.propagator, PropagatorTwoBody)
        twoBody.propagate()
        TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "SecondFac")

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted AssignTarget Satellite/SecondSat"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted AssignTarget Facility/SecondFac"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oTarget = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTargetCollection = oTarget.targets
        oTargetCollection.remove_all()
        oTargetCollection.add("*/Satellite/SecondSat")

        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTargetCollection = oTarget.targets
        oTargetCollection.remove_all()
        oTargetCollection.add("*/Facility/SecondFac")

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Facility/Facility1/Sensor/Sensor1 Targeted RemoveTarget Satellite/SecondSat"
        )
        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted RemoveTarget Facility/SecondFac"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oTarget = SensorPointingTargeted(Pointing.AG_SN1.pointing)
        oTargetCollection = oTarget.targets
        oTargetCollection.remove_target("*/Satellite/SecondSat")

        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTargetCollection = oTarget.targets
        oTargetCollection.remove_target("*/Facility/SecondFac")

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Point */Satellite/Satellite1/Sensor/Sensor2 Targeted Tracking Facility/Facility1"
        )
        TestBase.Application.execute_command(
            'AddTgtSched  */Satellite/Satellite1/Sensor/Sensor2 Facility/Facility1 "29 Feb 2000 02:00:00.00" "29 Feb 2000 03:00:00.00" '
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.TARGETED)
        oTarget = SensorPointingTargeted(Pointing.AG_SN2.pointing)
        oTarget.boresight = SensorPointingTargetedBoresightType.TRACKING
        oTargetCollection = oTarget.targets
        oTargetCollection.remove_all()
        oTargetCollection.add("*/Facility/Facility1")
        oTarget.enable_access_times = False
        oSchedTimes: "ScheduleTimeCollection" = oTarget.schedule_times
        oSchedTimes.remove_all()
        oSchedTimes.add("29 Feb 2000 02:00:00.00", "29 Feb 2000 03:00:00.00", "Facility/Facility1")

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("AddTgtSched  */Satellite/Satellite1/Sensor/Sensor2 CLEAR")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        with pytest.raises(Exception):
            oSchedTimes.remove_all()

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()
        Console.WriteLine("Integrity - Pointing - Targeted - End")

    # endregion

    # region External
    def test_External(self):
        Console.WriteLine("Integrity - Pointing - External")
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 01:00:00.00" "1 Jul 1999 01:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 12:00:00.00" "1 Jul 1999 12:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 02:30:00.00" "1 Jul 1999 02:30:00.00" 60.0',
        )

        Console.WriteLine("Integrity - Pointing - External - 1")
        strPath: str = TestBase.GetScenarioFile("SensorPointing_External.sp")
        Console.WriteLine(strPath)
        Console.WriteLine((('Point */Facility/Facility1/Sensor/Sensor1 External "' + strPath) + '"'))
        TestBase.Application.execute_command((('Point */Facility/Facility1/Sensor/Sensor1 External "' + strPath) + '"'))
        Console.WriteLine("after ExecuteCommand")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Console.WriteLine("before SetPointingExternalFile")
        Pointing.AG_SN1.set_pointing_external_file(strPath)
        Console.WriteLine("after SetPointingExternalFile")

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()
        Console.WriteLine("Integrity - Pointing - External - End")

    # endregion

    # region GrazingAlt
    def test_GrazingAlt(self):
        Console.WriteLine("Integrity - Pointing - GrazingAlt")
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 12:00:00.00" "1 Jul 1999 12:00:00.00" 60.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Pointing.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 02:30:00.00" "1 Jul 1999 02:30:00.00" 60.0',
        )

        TestBase.Application.execute_command("Define */Satellite/Satellite1/Sensor/Sensor2 SimpleCone 40.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN2.set_pattern_type(SensorPattern.SIMPLE_CONIC)
        patterndata: "SensorSimpleConicPattern" = SensorSimpleConicPattern(Pointing.AG_SN2.pattern)
        patterndata.cone_angle = 40.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Point */Satellite/Satellite1/Sensor/Sensor2 GrazingAlt 127.0 2000.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Pointing.AG_SN2.set_pointing_type(SensorPointing.BORESIGHT_GRAZING_ALTITUDE)
        oGraze: "SensorPointingGrazingAltitude" = SensorPointingGrazingAltitude(Pointing.AG_SN2.pointing)
        oGraze.azimuth_offset = 127.0
        oGraze.grazing_altitude = 2000.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()
        Console.WriteLine("Integrity - Pointing - GrazingAlt - End")


@category("EarlyBoundTests")

# [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
class Definition(TestBase):
    def __init__(self, *args, **kwargs):
        super(Definition, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        Console.WriteLine("Integrity - Definition - OneTimeSetUp")
        TestBase.Initialize()
        Definition.InitHelper()

    @staticmethod
    def InitHelper():
        TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))
        Definition.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])
        Definition.AG_PL = Planet(TestBase.Application.current_scenario.children["Planet1"])
        Definition.AG_ST = Star(TestBase.Application.current_scenario.children["Star1"])
        Definition.AG_SN1 = Sensor(TestBase.Application.current_scenario.children["Facility1"].children["Sensor1"])
        Definition.AG_SN2 = Sensor(TestBase.Application.current_scenario.children["Satellite1"].children["Sensor2"])
        Definition.AG_FA = Facility(TestBase.Application.current_scenario.children["Facility1"])
        Definition.AG_TA = Target(TestBase.Application.current_scenario.children["Target1"])
        Definition.AG_AT = AreaTarget(TestBase.Application.current_scenario.children["AreaTarget1"])
        Definition.AG_SC = Scenario(TestBase.Application.current_scenario)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        TestBase.Uninitialize()
        Console.WriteLine("Integrity - Definition - OneTimeTearDown")

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    AG_PL: "Planet" = None
    AG_ST: "Star" = None
    AG_SN1: "Sensor" = None
    AG_SN2: "Sensor" = None
    AG_FA: "Facility" = None
    AG_TA: "Target" = None
    AG_AT: "AreaTarget" = None
    AG_SC: "Scenario" = None
    AG_COV: "CoverageDefinition" = None
    AG_FOM: "FigureOfMerit" = None
    AG_FOM2: "FigureOfMerit" = None
    AG_CHAIN: "Chain" = None
    AG_LT: "LineTarget" = None
    # endregion

    # region CopyObject
    def test_CopyObject(self):
        (IStkObject(Definition.AG_SAT)).children.new(STKObjectType.SENSOR, "SensorIntegrity")

        # Copy Satellite1 with sensor via OM
        satCopy: "IStkObject" = TestBase.Application.current_scenario.children.copy_object(
            clr.CastAs(Definition.AG_SAT, IStkObject), "SatCopyOM"
        )

        # Copy Satellite1 with sensor via Connect
        TestBase.Application.execute_command("Copy / */Satellite/Satellite1 Name SatCopyConnect")

    # endregion

    # region Vehicle
    def test_Vehicle(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_SAT, IStkObject),
            '"Pass Data" "1 Nov 2000 00:00:00.00" "2 Nov 2000 00:00:00.00" 60.0',
        )
        CompareUtility.AddReport(clr.CastAs(Definition.AG_SAT, IStkObject), '"Mass"')

        # Propagator Initialization
        Definition.AG_SAT.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = PropagatorJ2Perturbation(Definition.AG_SAT.propagator)
        j2prop.ephemeris_interval.set_explicit_interval("1 Nov 2000 00:00:00.00", "1 Nov 2000 4:00:00.00")
        j2prop.step = 60
        classical: "OrbitStateClassical" = OrbitStateClassical(
            j2prop.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        )
        classical.coordinate_system_type = CoordinateSystem.J2000
        coordsys: "OrbitStateCoordinateSystem" = classical.coordinate_system
        # Epoch was deprecated
        # j2prop.InitialState.Epoch = "1 Nov 2000 02:00:00.00";
        (classical).epoch = "1 Nov 2000 02:00:00.00"
        classical.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
        sizeshape: "ClassicalSizeShapeSemimajorAxis" = ClassicalSizeShapeSemimajorAxis(classical.size_shape)
        sizeshape.semi_major_axis = 7322000.122
        classical.size_shape_type = ClassicalSizeShape.MEAN_MOTION
        sizeshape1: "ClassicalSizeShapeMeanMotion" = ClassicalSizeShapeMeanMotion(classical.size_shape)
        sizeshape1.eccentricity = 0.099
        classical.orientation.inclination = 99.5
        classical.orientation.argument_of_periapsis = 1.2
        classical.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE
        raan: "OrientationRightAscensionOfAscendingNode" = OrientationRightAscensionOfAscendingNode(
            classical.orientation.ascending_node
        )
        raan.value = 122.2
        classical.location_type = ClassicalLocation.MEAN_ANOMALY
        loc: "ClassicalLocationMeanAnomaly" = ClassicalLocationMeanAnomaly(classical.location)
        loc.value = 22.2
        j2prop.initial_state.representation.assign(classical)
        j2prop.propagate()

        # Pass
        TestBase.Application.execute_command("SetPassNumber */Satellite/Satellite1 786")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SAT.pass_break.set_pass_numbering_type(VehiclePassNumbering.FIRST_PASS_NUMBER)
        first: "PassBreakNumberingFirstPassNumber" = PassBreakNumberingFirstPassNumber(
            Definition.AG_SAT.pass_break.pass_numbering
        )
        first.first_pass_number = 786
        j2prop.propagate()

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            'PassBreak */Satellite/Satellite1 Number AtDate 2 "1 Nov 2000 12:00:00.00"'
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SAT.pass_break.set_pass_numbering_type(VehiclePassNumbering.DATE_OF_FIRST_PASS)
        date: "PassBreakNumberingDateOfFirstPass" = PassBreakNumberingDateOfFirstPass(
            Definition.AG_SAT.pass_break.pass_numbering
        )
        date.first_pass_number = 2
        date.pass_data_epoch.set_explicit_time("1 Nov 2000 12:00:00.00")
        j2prop.propagate()

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("PassBreak */Satellite/Satellite1 Latitude 45.0")
        TestBase.Application.execute_command("PassBreak */Satellite/Satellite1 Descending")
        TestBase.Application.execute_command("PassBreak */Satellite/Satellite1 Partial Angle")
        TestBase.Application.execute_command("PassBreak */Satellite/Satellite1 Number Maintain")
        TestBase.Application.execute_command("PassBreak */Satellite/Satellite1 CoordSys CBF")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SAT.pass_break.definition.direction = VehicleDirection.DESCENDING
        Definition.AG_SAT.pass_break.definition.set_break_angle_type(VehicleBreakAngleType.BY_LATITUDE)
        lat: "VehicleBreakAngleBreakByLatitude" = VehicleBreakAngleBreakByLatitude(
            Definition.AG_SAT.pass_break.definition.break_angle
        )
        lat.latitude = 45.0
        Definition.AG_SAT.pass_break.set_pass_numbering_type(VehiclePassNumbering.MAINTAIN_PASS_NUMBER)
        Definition.AG_SAT.pass_break.partial_pass_measurement = VehiclePartialPassMeasurement.ANGLE
        Definition.AG_SAT.pass_break.coordinate_system = VehicleCoordinateSystem.CENTRAL_BODY_FIXED

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetMass */Satellite/Satellite1 value 4321.654")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SAT.mass_properties.mass = 4321.654

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetMass */Satellite/Satellite1 matrix 30 4700 20 70 10 120")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SAT.mass_properties.inertia.ixx = 30
        Definition.AG_SAT.mass_properties.inertia.ixy = 4700
        Definition.AG_SAT.mass_properties.inertia.ixz = 20
        Definition.AG_SAT.mass_properties.inertia.iyy = 70
        Definition.AG_SAT.mass_properties.inertia.iyz = 10
        Definition.AG_SAT.mass_properties.inertia.izz = 120

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Facility
    def test_Facility(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_FA, IStkObject),
            '"Cartesian Position" "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 43200.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_FA, IStkObject),
            '"LLA Position" "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 43200.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_FA, IStkObject),
            '"Eclipse Times" "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 43200.0',
        )
        CompareUtility.AddReport3(("Position " + (IStkObject(Definition.AG_FA)).path))

        # Position
        pos: "IPosition" = Definition.AG_FA.position
        Definition.AG_FA.height_above_ground = 0.0

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Geodetic  40.0 -106.0 10.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet: "Geodetic" = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 10.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Cartesian  0.0 -6400000.0 0.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        cart: "Cartesian" = Cartesian(pos.convert_to(PositionType.CARTESIAN))
        cart.x = 0.0
        cart.y = -6400000.0
        cart.z = 0.0
        pos.assign(cart)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Cylindrical  6400000.0 180.0 -100000.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        cyl: "Cylindrical" = Cylindrical(pos.convert_to(PositionType.CYLINDRICAL))
        cyl.radius = 6400000.0
        cyl.longitude = 180.0
        cyl.z = -100000.0
        pos.assign(cyl)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Spherical  90.0 -270.0 6400000.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        sph: "Spherical" = Spherical(pos.convert_to(PositionType.SPHERICAL))
        sph.latitude = 90.0
        sph.longitude = -270.0
        sph.radius = 6400000.0
        pos.assign(sph)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Geocentric  0.0 -180.0 100.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geo: "Geocentric" = Geocentric(pos.convert_to(PositionType.GEOCENTRIC))
        geo.latitude = 0.0
        geo.longitude = -180.0
        geo.altitude = 100.0
        pos.assign(geo)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Geodetic  40.0 -106.0 10.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 10.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Geodetic  40.0 -106.0 Terrain")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        Definition.AG_FA.use_terrain = True

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        pos.assign(geodet)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Geocentric  0.0 -180.0 Terrain")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geo = Geocentric(pos.convert_to(PositionType.GEOCENTRIC))
        geo.latitude = 0.0
        geo.longitude = -180.0
        Definition.AG_FA.use_terrain = True
        pos.assign(geo)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Spherical  90.0 -270.0 Terrain")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        sph = Spherical(pos.convert_to(PositionType.SPHERICAL))
        sph.latitude = 90.0
        sph.longitude = -270.0
        Definition.AG_FA.use_terrain = True
        pos.assign(sph)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Facility/Facility1 Geodetic  40.0 -106.0 0.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FA.use_terrain = False
        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 0.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Scenario
    def test_Scenario(self):
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport3("GetEpoch *")
        CompareUtility.AddReport3("GetTimePeriod *")
        CompareUtility.AddReport3("AllInstanceNames /")

        TestBase.Application.execute_command('SetEpoch * "1 Oct 1999 01:00:00.00"')
        TestBase.Application.execute_command('SetTimePeriod * "1 Oct 1999 01:00:00.00" "1 Oct 1999 05:00:00.00"')

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SC.epoch = "1 Oct 1999 01:00:00.00"
        Definition.AG_SC.start_time = "1 Oct 1999 01:00:00.00"
        Definition.AG_SC.stop_time = "1 Oct 1999 05:00:00.00"

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command('New / */Facility "TestFacility"')
        TestBase.Application.execute_command('New / */Ship "TestShip"')

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Unload / */Facility/TestFacility")
        TestBase.Application.execute_command("Unload / */Ship/TestShip")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        (IStkObject(Definition.AG_SC)).children.new(STKObjectType.FACILITY, "TestFacility")
        (IStkObject(Definition.AG_SC)).children.new(STKObjectType.SHIP, "TestShip")

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        (IStkObject(Definition.AG_SC)).children.unload(STKObjectType.FACILITY, "TestFacility")
        (IStkObject(Definition.AG_SC)).children.unload(STKObjectType.SHIP, "TestShip")

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region AreaTarget
    def test_AreaTarget(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport2(clr.CastAs(Definition.AG_AT, IStkObject), '"Boundary Points"', 1e-05)
        CompareUtility.AddReport3(("Position " + (IStkObject(Definition.AG_AT)).path))

        # Boundary
        TestBase.Application.execute_command("SetBoundary */AreaTarget/AreaTarget1 Ellipse 100.0 50.0 45.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_AT.area_type = AreaType.ELLIPSE
        ellipse: "AreaTypeEllipse" = AreaTypeEllipse(Definition.AG_AT.area_type_data)
        ellipse.semi_minor_axis = 50.0
        ellipse.bearing = 45.0
        ellipse.semi_major_axis = 100.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "SetBoundary */AreaTarget/AreaTarget1 Pattern 4 20.0 -10.0 20.0 10.0 -20.0 10.0 -20.0 -10.0"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_AT.area_type = AreaType.PATTERN
        patterns: "AreaTypePatternCollection" = AreaTypePatternCollection(Definition.AG_AT.area_type_data)
        patterns.remove_all()
        patterns.add(20.0, -10.0)
        patterns.add(20.0, 10.0)
        patterns.add(-20.0, 10.0)
        patterns.add(-20.0, -10.0)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Position
        pos: "IPosition" = Definition.AG_AT.position
        Definition.AG_AT.automatic_computation_of_centroid = False

        TestBase.Application.execute_command("SetPosition */AreaTarget/AreaTarget1 Geodetic  40.0 -106.0 10.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet: "Geodetic" = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 10.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */AreaTarget/AreaTarget1 Cartesian  0.0 -6400000.0 0.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        cart: "Cartesian" = Cartesian(pos.convert_to(PositionType.CARTESIAN))
        cart.x = 0.0
        cart.y = -6400000.0
        cart.z = 0.0
        pos.assign(cart)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "SetPosition */AreaTarget/AreaTarget1 Cylindrical  6400000.0 180.0 -100000.0"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        cyl: "Cylindrical" = Cylindrical(pos.convert_to(PositionType.CYLINDRICAL))
        cyl.radius = 6400000.0
        cyl.longitude = 180.0
        cyl.z = -100000.0
        pos.assign(cyl)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */AreaTarget/AreaTarget1 Spherical  90.0 -270.0 6400000.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        sph: "Spherical" = Spherical(pos.convert_to(PositionType.SPHERICAL))
        sph.latitude = 90.0
        sph.longitude = -270.0
        sph.radius = 6400000.0
        pos.assign(sph)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */AreaTarget/AreaTarget1 Geocentric  0.0 -180.0 100.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geo: "Geocentric" = Geocentric(pos.convert_to(PositionType.GEOCENTRIC))
        geo.latitude = 0.0
        geo.longitude = -180.0
        geo.altitude = 100.0
        pos.assign(geo)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */AreaTarget/AreaTarget1 Geodetic  40.0 -106.0 10.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 10.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */AreaTarget/AreaTarget1 Geodetic  40.0 -106.0 Terrain")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        Definition.AG_AT.use_terrain_data = True

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        pos.assign(geodet)

        TestBase.Application.execute_command("SetPosition */AreaTarget/AreaTarget1 Geocentric  0.0 -180.0 Terrain")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geo = Geocentric(pos.convert_to(PositionType.GEOCENTRIC))
        geo.latitude = 0.0
        geo.longitude = -180.0
        Definition.AG_AT.use_terrain_data = True
        pos.assign(geo)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */AreaTarget/AreaTarget1 Geodetic  40.0 -106.0 0.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_AT.use_terrain_data = False
        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 0.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Target
    def test_TargetTest(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_TA, IStkObject),
            '"Cartesian Position" "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 43200.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_TA, IStkObject),
            '"LLA Position" "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 43200.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_TA, IStkObject),
            '"Eclipse Times" "1 Jul 1999 00:00:00.00" "2 Jul 1999 00:00:00.00" 43200.0',
        )
        CompareUtility.AddReport3(("Position " + (IStkObject(Definition.AG_TA)).path))

        # Position
        pos: "IPosition" = Definition.AG_TA.position
        Definition.AG_TA.height_above_ground = 0.0

        TestBase.Application.execute_command("SetPosition */Target/Target1 Geodetic  40.0 -106.0 10.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet: "Geodetic" = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 10.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Cartesian  0.0 -6400000.0 0.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        cart: "Cartesian" = Cartesian(pos.convert_to(PositionType.CARTESIAN))
        cart.x = 0.0
        cart.y = -6400000.0
        cart.z = 0.0
        pos.assign(cart)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Cylindrical  6400000.0 180.0 -100000.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        cyl: "Cylindrical" = Cylindrical(pos.convert_to(PositionType.CYLINDRICAL))
        cyl.radius = 6400000.0
        cyl.longitude = 180.0
        cyl.z = -100000.0
        pos.assign(cyl)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Spherical  90.0 -270.0 6400000.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        sph: "Spherical" = Spherical(pos.convert_to(PositionType.SPHERICAL))
        sph.latitude = 90.0
        sph.longitude = -270.0
        sph.radius = 6400000.0
        pos.assign(sph)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Geocentric  0.0 -180.0 100.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geo: "Geocentric" = Geocentric(pos.convert_to(PositionType.GEOCENTRIC))
        geo.latitude = 0.0
        geo.longitude = -180.0
        geo.altitude = 100.0
        pos.assign(geo)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Geodetic  40.0 -106.0 10.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 10.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Geodetic  40.0 -106.0 Terrain")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        Definition.AG_TA.use_terrain = True

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        pos.assign(geodet)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Geocentric  0.0 -180.0 Terrain")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        geo = Geocentric(pos.convert_to(PositionType.GEOCENTRIC))
        geo.latitude = 0.0
        geo.longitude = -180.0
        Definition.AG_TA.use_terrain = True
        pos.assign(geo)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Spherical  90.0 -270.0 Terrain")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        sph = Spherical(pos.convert_to(PositionType.SPHERICAL))
        sph.latitude = 90.0
        sph.longitude = -270.0
        Definition.AG_TA.use_terrain = True
        pos.assign(sph)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetPosition */Target/Target1 Geodetic  40.0 -106.0 0.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_TA.use_terrain = False
        geodet = Geodetic(pos.convert_to(PositionType.GEODETIC))
        geodet.latitude = 40.0
        geodet.longitude = -106.0
        geodet.altitude = 0.0
        pos.assign(geodet)

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Planet
    def test_Planet(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_PL, IStkObject),
            '"Helio Position Velocity" "1 Nov 2000 00:00:00.00" "10 Nov 2000 00:00:00.00" 43200.0',
        )

        # Definition
        body: "PlanetPositionCentralBody" = PlanetPositionCentralBody(Definition.AG_PL.position_source_data)
        body.rename_automatically = False

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Mercury")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Mercury"
        ephemSource: "EphemSourceType" = EphemSourceType.JPL_DEVELOPMENTAL_EPHEMERIS
        body.ephemeris_source = ephemSource

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Venus")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Venus"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Earth")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Earth"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Mars JPL")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Mars"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Jupiter")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Jupiter"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Saturn")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Saturn"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Neptune")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Neptune"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Uranus")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Uranus"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Pluto")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Pluto"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Moon")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Moon"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 JPLDEFile Sun")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Sun"
        body.ephemeris_source = ephemSource
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Mercury Analytic")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Mercury"
        body.ephemeris_source = EphemSourceType.ANALYTIC
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Venus Analytic")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Venus"
        body.ephemeris_source = EphemSourceType.ANALYTIC
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Mars Analytic")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Mars"
        body.ephemeris_source = EphemSourceType.ANALYTIC
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Jupiter Analytic")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Jupiter"
        body.ephemeris_source = EphemSourceType.ANALYTIC
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Saturn Analytic")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Saturn"
        body.ephemeris_source = EphemSourceType.ANALYTIC
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Neptune Analytic")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Neptune"
        body.ephemeris_source = EphemSourceType.ANALYTIC
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Uranus Analytic")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Uranus"
        body.ephemeris_source = EphemSourceType.ANALYTIC
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Pluto Analytic")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Pluto"
        body.ephemeris_source = EphemSourceType.ANALYTIC
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Planet/Planet1 CentralBody Sun Default")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.CENTRAL_BODY
        body.central_body = "Sun"
        body.ephemeris_source = EphemSourceType.DEFAULT
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        strPath: str = TestBase.GetScenarioFile("Venus.pe")
        TestBase.Application.execute_command((('Define */Planet/Planet1 File "' + strPath) + '"'))
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_PL.position_source = PlanetPositionSourceType.FILE
        file: "PlanetPositionFile" = PlanetPositionFile(Definition.AG_PL.position_source_data)
        file.filename = strPath
        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Star
    def test_Star(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Definition.AG_ST, IStkObject), '"J2000 Position"')
        CompareUtility.AddReport(clr.CastAs(Definition.AG_ST, IStkObject), '"J2000 Cartesian Position"')

        # Definition
        Definition.AG_ST.location_right_ascension = 120.0
        Definition.AG_ST.location_declination = -40.0
        self.Units.set_current_unit("TimeUnit", "yr")
        self.Units.set_current_unit("AngleUnit", "arcSec")
        Definition.AG_ST.proper_motion_right_ascension = -1.0
        Definition.AG_ST.proper_motion_declination = 2.0
        Definition.AG_ST.parallax = 2.3
        Definition.AG_ST.magnitude = -1.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Star/Star1 Position  120.0  -40.0")
        TestBase.Application.execute_command("Define */Star/Star1 Motion   -1.0  2.0")
        TestBase.Application.execute_command("Define */Star/Star1 Parallax   2.3")
        TestBase.Application.execute_command("Define */Star/Star1 Magnitude   -1.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Sensor
    def test_Sensor(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_SN2, IStkObject),
            '"Pattern Intersection" "1 Jul 1999 00:00:00.00" "1 Jul 1999 00:00:00.00" 60.0',
        )

        TestBase.Application.execute_command("Define */Facility/Facility1/Sensor/Sensor1 SimpleCone 80.0")
        TestBase.Application.execute_command("Define */Satellite/Satellite1/Sensor/Sensor2 SimpleCone 80.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SN1.set_pattern_type(SensorPattern.SIMPLE_CONIC)
        patterndata: "SensorSimpleConicPattern" = SensorSimpleConicPattern(Definition.AG_SN1.pattern)
        patterndata.cone_angle = 80.0

        Definition.AG_SN2.set_pattern_type(SensorPattern.SIMPLE_CONIC)
        patterndata = SensorSimpleConicPattern(Definition.AG_SN2.pattern)
        patterndata.cone_angle = 80.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Facility/Facility1/Sensor/Sensor1 Conical 10.0 70.0 20.0 220.0")
        TestBase.Application.execute_command(
            "Define */Satellite/Satellite1/Sensor/Sensor2 Conical 10.0 70.0 20.0 220.0"
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SN1.set_pattern_type(SensorPattern.COMPLEX_CONIC)
        patterndata1: "SensorComplexConicPattern" = SensorComplexConicPattern(Definition.AG_SN1.pattern)
        patterndata1.inner_cone_half_angle = 10.0
        patterndata1.outer_cone_half_angle = 70.0
        patterndata1.minimum_clock_angle = 20.0
        patterndata1.maximum_clock_angle = 220.0

        Definition.AG_SN2.set_pattern_type(SensorPattern.COMPLEX_CONIC)
        patterndata1 = SensorComplexConicPattern(Definition.AG_SN2.pattern)
        patterndata1.inner_cone_half_angle = 10.0
        patterndata1.outer_cone_half_angle = 70.0
        patterndata1.minimum_clock_angle = 20.0
        patterndata1.maximum_clock_angle = 220.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Facility/Facility1/Sensor/Sensor1 HalfPower 12.5  3.4")
        TestBase.Application.execute_command("Define */Satellite/Satellite1/Sensor/Sensor2 HalfPower 12.5  3.4")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SN1.set_pattern_type(SensorPattern.HALF_POWER)
        patterndata2: "SensorHalfPowerPattern" = SensorHalfPowerPattern(Definition.AG_SN1.pattern)
        patterndata2.frequency = 12.5
        patterndata2.antenna_diameter = 3.4

        Definition.AG_SN2.set_pattern_type(SensorPattern.HALF_POWER)
        patterndata2 = SensorHalfPowerPattern(Definition.AG_SN2.pattern)
        patterndata2.frequency = 12.5
        patterndata2.antenna_diameter = 3.4

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Facility/Facility1/Sensor/Sensor1 Rectangular 30.0 40.0")
        TestBase.Application.execute_command("Define */Satellite/Satellite1/Sensor/Sensor2 Rectangular 30.0 40.0")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SN1.set_pattern_type(SensorPattern.RECTANGULAR)
        patterndata3: "SensorRectangularPattern" = SensorRectangularPattern(Definition.AG_SN1.pattern)
        patterndata3.vertical_half_angle = 30.0
        patterndata3.horizontal_half_angle = 40.0

        Definition.AG_SN2.set_pattern_type(SensorPattern.RECTANGULAR)
        patterndata3 = SensorRectangularPattern(Definition.AG_SN2.pattern)
        patterndata3.vertical_half_angle = 30.0
        patterndata3.horizontal_half_angle = 40.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        strPath: str = TestBase.GetScenarioFile("Custom.Pattern")
        TestBase.Application.execute_command((('Define */Facility/Facility1/Sensor/Sensor1 Custom "' + strPath) + '"'))
        TestBase.Application.execute_command(
            (('Define */Satellite/Satellite1/Sensor/Sensor2 Custom "' + strPath) + '"')
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SN1.set_pattern_type(SensorPattern.CUSTOM)
        patterndata4: "SensorCustomPattern" = SensorCustomPattern(Definition.AG_SN1.pattern)
        patterndata4.filename = strPath

        Definition.AG_SN2.set_pattern_type(SensorPattern.CUSTOM)
        patterndata4 = SensorCustomPattern(Definition.AG_SN2.pattern)
        patterndata4.filename = strPath

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Define */Facility/Facility1/Sensor/Sensor1 SAR 10.0 60.0 40.0 30.0 700.0")
        TestBase.Application.execute_command(
            "Define */Satellite/Satellite1/Sensor/Sensor2 SAR 10.0 60.0 40.0 30.0 700.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SN1.set_pattern_type(SensorPattern.SAR)
        patterndata5: "SensorSARPattern" = SensorSARPattern(Definition.AG_SN1.pattern)
        patterndata5.minimum_elevation_angle = 10.0
        patterndata5.maximum_elevation_angle = 60.0
        patterndata5.fore_exclusion_angle = 40.0
        patterndata5.aft_exclusion_angle = 30.0
        patterndata5.parent_altitude = 700.0

        Definition.AG_SN2.set_pattern_type(SensorPattern.SAR)
        patterndata5 = SensorSARPattern(Definition.AG_SN2.pattern)
        patterndata5.minimum_elevation_angle = 10.0
        patterndata5.maximum_elevation_angle = 60.0
        patterndata5.fore_exclusion_angle = 40.0
        patterndata5.aft_exclusion_angle = 30.0
        patterndata5.parent_altitude = 700.0

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Chain
    def test_Chain(self):
        self.ChainTest()
        self.ChainV2Test()

    def ChainTest(self):
        # Report initialization
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainTest", "ChainTest.sc"))
        angBetween: "Chain" = Chain(TestBase.Application.current_scenario.children["AngBtwn"])
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(angBetween, IStkObject), '"Angle Between"')

        # Connect
        TestBase.Application.execute_command("New / Scenario/ChainTest/Chain MolnyaChain")
        TestBase.Application.execute_command("New / */Chain JeffChain")
        TestBase.Application.execute_command("New / */Satellite JeffSAT")
        TestBase.Application.execute_command("Chains */Chain/JeffChain Add Satellite/JeffSAT")
        TestBase.Application.execute_command("Chains */Chain/JeffChain AutoRecompute On")
        TestBase.Application.execute_command("Chains */Chain/JeffChain AutoRecompute Off")
        TestBase.Application.execute_command("Chains */Chain/JeffChain SetComputeTime UseObjects")
        TestBase.Application.execute_command("Chains */Chain/JeffChain SetComputeTime UseScenario")
        TestBase.Application.execute_command(
            'Chains */Chain/JeffChain SetComputeTime UserSpecified "1 Jun 2002 12:00:00.00" "2 Jun 2002 12:00:00.00"'
        )
        TestBase.Application.execute_command("Chains */Chain/JeffChain Remove Satellite/JeffSAT")
        TestBase.Application.execute_command("New / */Constellation JeffCon")
        TestBase.Application.execute_command("Chains */Constellation/JeffCon Add Planet/Jupiter")
        TestBase.Application.execute_command("Chains */Constellation/JeffCon Add Satellite/Molnya")
        TestBase.Application.execute_command("Chains */Constellation/JeffCon Add Facility/North")

        TestBase.Application.execute_command("AddObject Scenario/ChainTest/Chain/MolnyaChain   Planet/Jupiter")
        TestBase.Application.execute_command("AddObject Scenario/ChainTest/Chain/MolnyaChain   Satellite/Molnya")
        TestBase.Application.execute_command("AddObject Scenario/ChainTest/Chain/MolnyaChain   Facility/North")
        TestBase.Application.execute_command("ListSubObjects Scenario/ChainTest/Chain/MolnyaChain ")
        TestBase.Application.execute_command("RemoveObject Scenario/ChainTest/Chain/MolnyaChain Satellite/Molnya")
        TestBase.Application.execute_command("ListSubObjects Scenario/ChainTest/Chain/MolnyaChain ")
        TestBase.Application.execute_command("RemoveObject Scenario/ChainTest/Chain/MolnyaChain Facility/North")
        TestBase.Application.execute_command("ListSubObjects Scenario/ChainTest/Chain/MolnyaChain ")
        TestBase.Application.execute_command("AddObject Scenario/ChainTest/Chain/MolnyaChain   Satellite/Molnya")
        TestBase.Application.execute_command("AddObject Scenario/ChainTest/Chain/MolnyaChain   Facility/North")

        TestBase.Application.execute_command("Chains_R */Constellation/JeffCon Operator")
        TestBase.Application.execute_command("Chains_R */Chain/MolnyaChain SubObjects")
        TestBase.Application.execute_command("Chains_RM / Access All")
        TestBase.Application.execute_command("Chains_RM / Access Intervals")
        TestBase.Application.execute_command("Chains_RM / Access Strands")
        TestBase.Application.execute_command("Chains_RM / Access TwoObject")
        TestBase.Application.execute_command("Chains_RM / Access EndObjectStrands Facility/North")

        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MaxAngleBetween On")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MaxAngleBetween 10.0")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MaxAngleBetween Off")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MinAngleBetween 10.0")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MinAngleBetween Off")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MinAngleBetween On")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MinLinkTime 10.0")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MinLinkTime On ")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/MolnyaChain MinLinkTime Off")

        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/AngBtwn MaxAngleBetween 60.0")
        TestBase.Application.execute_command("SetConstraint /Scenario/ChainTest/Chain/AngBtwn MinAngleBetween 40.0")

        TestBase.Application.execute_command("Compute /Scenario/ChainTest/Chain/AngBtwn")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainTest", "ChainTest.sc"))

        TestBase.Application.current_scenario.children.new(STKObjectType.CHAIN, "MolnyaChain")
        oJeffChain: "Chain" = Chain(
            TestBase.Application.current_scenario.children.new(STKObjectType.CHAIN, "JeffChain")
        )
        TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "JeffSAT")

        oJeffChain.objects.add("Satellite/JeffSAT")
        oJeffChain.recompute_automatically = True
        oJeffChain.recompute_automatically = False
        oJeffChain.set_time_period_type(ChainTimePeriodType.OBJECT_TIME_PERIODS)
        oJeffChain.set_time_period_type(ChainTimePeriodType.SCENARIO_TIME_PERIOD)
        oJeffChain.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)
        oUser: "ChainUserSpecifiedTimePeriod" = ChainUserSpecifiedTimePeriod(oJeffChain.time_period)
        oUser.time_interval.set_explicit_interval("1 Jun 2002 12:00:00.00", "2 Jun 2002 12:00:00.00")
        oJeffChain.objects.remove_name("Satellite/JeffSAT")

        oJeffCon: "Constellation" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.CONSTELLATION, "JeffCon"), Constellation
        )
        oJeffCon.objects.add("Planet/Jupiter")
        oJeffCon.objects.add("Satellite/Molnya")
        oJeffCon.objects.add("Facility/North")

        oMolynaChain: "Chain" = Chain(TestBase.Application.current_scenario.children["MolnyaChain"])

        oMolynaChain.objects.add("Planet/Jupiter")
        oMolynaChain.objects.add("Satellite/Molnya")
        oMolynaChain.objects.add("Facility/North")
        oMolynaChain.objects.remove_name("Satellite/Molnya")
        oMolynaChain.objects.remove_name("Facility/North")
        oMolynaChain.objects.add("Satellite/Molnya")
        oMolynaChain.objects.add("Facility/North")
        oMolynaChain.objects.remove_name("Satellite/Molnya")
        oMolynaChain.objects.remove_name("Facility/North")
        oMolynaChain.objects.add("Satellite/Molnya")
        oMolynaChain.objects.add("Facility/North")

        TestBase.Application.execute_command("Chains_R */Constellation/JeffCon Operator")  # Not currently supported
        TestBase.Application.execute_command("Chains_R */Chain/MolnyaChain SubObjects")
        TestBase.Application.execute_command("Chains_RM / Access All")
        TestBase.Application.execute_command("Chains_RM / Access Intervals")
        TestBase.Application.execute_command("Chains_RM / Access Strands")
        TestBase.Application.execute_command("Chains_RM / Access TwoObject")
        TestBase.Application.execute_command("Chains_RM / Access EndObjectStrands Facility/North")

        oMolynaChain.constraints.use_maximum_angle = True
        oMolynaChain.constraints.maximum_angle = 10.0
        oMolynaChain.constraints.use_maximum_angle = False
        oMolynaChain.constraints.use_minimum_angle = True
        oMolynaChain.constraints.minimum_angle = 10.0
        oMolynaChain.constraints.use_minimum_angle = False
        oMolynaChain.constraints.use_minimum_link_time = True
        oMolynaChain.constraints.minimum_link_time = 10.0
        oMolynaChain.constraints.use_minimum_link_time = False

        # This line is required because the scenario has been reloaded.
        angBetween = Chain(TestBase.Application.current_scenario.children["AngBtwn"])
        angBetween.constraints.use_maximum_angle = True
        angBetween.constraints.use_minimum_angle = True
        angBetween.constraints.maximum_angle = 60.0
        angBetween.constraints.minimum_angle = 40.0

        # oMolynaChain.AutoRecompute = true;
        # Application.ExecuteCommand("Compute /Scenario/ChainTest/Chain/AngBtwn");

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()
        Definition.InitHelper()

    def ChainV2Test(self):
        # ///////////////////////////////////////////////////////////////////////////

        # Report initialization
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        fac1sat1fac2: "Chain" = Chain(TestBase.Application.current_scenario.children["Fac1Sat1Fac2"])
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(fac1sat1fac2, IStkObject), '"Angle Between"')
        CompareUtility.AddReport(clr.CastAs(fac1sat1fac2, IStkObject), '"Complete Chain Access"')
        CompareUtility.AddReport(clr.CastAs(fac1sat1fac2, IStkObject), '"Individual Object Access"')
        CompareUtility.AddReport(clr.CastAs(fac1sat1fac2, IStkObject), '"Individual Strand Access"')
        CompareUtility.AddReport(clr.CastAs(fac1sat1fac2, IStkObject), '"Time Ordered Access"')

        # Connect
        TestBase.Application.execute_command(
            "Access /Scenario/ChainV2Scenario/Aircraft/ChainAircraft1 /Scenario/ChainV2Scenario/Satellite/TDRS_6"
        )  # Not currently supported
        TestBase.Application.execute_command(
            "AER /Scenario/ChainV2Scenario/Aircraft/ChainAircraft1 /Scenario/ChainV2Scenario/Satellite/TDRS_6"
        )  # Not currently supported
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        oChainAircraft1: "IStkObject" = TestBase.Application.current_scenario.children["ChainAircraft1"]
        oTDRS_6: "IStkObject" = TestBase.Application.current_scenario.children["TDRS_6"]
        Assert.assertIsNotNone(oChainAircraft1)
        Assert.assertIsNotNone(oTDRS_6)
        oAccess: "Access" = oChainAircraft1.get_access_to_object(oTDRS_6)
        Assert.assertIsNotNone(oAccess)
        oAccess.compute_access()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Compare
        CompareUtility.CompareReportSnapshots()

        # ///////////////////////////////////////////////////////////////////////////

        # Report initialization                Any
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat: "Constellation" = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        canadaConstSatGreenland: "Chain" = Chain(
            TestBase.Application.current_scenario.children["CanadaConstSatGreenland"]
        )
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(canadaConstSatGreenland, IStkObject), '"Complete Chain Access"')

        # Connect
        TestBase.Application.execute_command("SetOperator Scenario/ChainV2Scenario/Constellation/ConstSat Any")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        constSat.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.ANY_OF)
        constSat.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.ANY_OF)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Compare
        CompareUtility.CompareReportSnapshots()

        # ///////////////////////////////////////////////////////////////////////////

        # Report initialization                All
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        canadaConstSatGreenland = Chain(TestBase.Application.current_scenario.children["CanadaConstSatGreenland"])
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(canadaConstSatGreenland, IStkObject), '"Complete Chain Access"')

        # Connect
        TestBase.Application.execute_command("SetOperator Scenario/ChainV2Scenario/Constellation/ConstSat All")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        constSat.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.ALL_OF)
        constSat.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.ALL_OF)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Compare
        CompareUtility.CompareReportSnapshots()

        # ///////////////////////////////////////////////////////////////////////////

        # Report initialization                AtLeast 2
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        canadaConstSatGreenland = Chain(TestBase.Application.current_scenario.children["CanadaConstSatGreenland"])
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(canadaConstSatGreenland, IStkObject), '"Complete Chain Access"')

        # Connect
        TestBase.Application.execute_command("SetOperator Scenario/ChainV2Scenario/Constellation/ConstSat AtLeast 2")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        constSat.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.AT_LEAST_N)
        constSat.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.AT_LEAST_N)
        (ConstellationConstraintObjectRestriction(constSat.constraints.from_restriction)).number_of_objects = 2
        (ConstellationConstraintObjectRestriction(constSat.constraints.to_restriction)).number_of_objects = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Compare
        CompareUtility.CompareReportSnapshots()

        # ///////////////////////////////////////////////////////////////////////////

        # Report initialization                Exactly 2
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        canadaConstSatGreenland = Chain(TestBase.Application.current_scenario.children["CanadaConstSatGreenland"])
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(canadaConstSatGreenland, IStkObject), '"Complete Chain Access"')

        # Connect
        TestBase.Application.execute_command("SetOperator Scenario/ChainV2Scenario/Constellation/ConstSat Exactly 2")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        constSat.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.EXACTLY_N)
        constSat.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.EXACTLY_N)
        (ConstellationConstraintObjectRestriction(constSat.constraints.from_restriction)).number_of_objects = 2
        (ConstellationConstraintObjectRestriction(constSat.constraints.to_restriction)).number_of_objects = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Compare
        CompareUtility.CompareReportSnapshots()

        # ///////////////////////////////////////////////////////////////////////////

        # Report initialization                NoneOf
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        canadaConstSatGreenland = Chain(TestBase.Application.current_scenario.children["CanadaConstSatGreenland"])
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(canadaConstSatGreenland, IStkObject), '"Complete Chain Access"')

        # Connect
        TestBase.Application.execute_command("SetOperator Scenario/ChainV2Scenario/Constellation/ConstSat NoneOf")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("ChainV2Test", "ChainV2Scenario.sc"))
        constSat = Constellation(TestBase.Application.current_scenario.children["ConstSat"])
        constSat.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.NONE_OF)
        constSat.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.NONE_OF)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Compare
        CompareUtility.CompareReportSnapshots()

        # ///////////////////////////////////////////////////////////////////////////

        Definition.InitHelper()

    # endregion

    # region CoverageDefinition
    def test_CoverageDefinition(self):
        TestBase.Application.execute_command("ConControl / VerboseOff")
        self.GeneralCoverageDefinitionTest()
        self.CoverageDefinitionPointTest()  # not finished yet
        Definition.InitHelper()

    # region GeneralCoverageDefinitionTest
    # Perform Coverage and Grid Inspector testing, including definition, asset and
    # grid settings, as well as computations and data export.
    def GeneralCoverageDefinitionTest(self):
        # Report initialization
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("CovDefTest", "CovDefTest.sc"))
        Definition.AG_COV = CoverageDefinition(
            TestBase.Application.current_scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "TestCovDef")
        )

        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Percent Coverage"')
        CompareUtility.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Access Duration"')
        CompareUtility.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Coverage By Asset"')

        oComparator1 = ReportComparison(self.Units)
        oComparator1.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Access Duration"')
        oComparator1.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Coverage By Asset"')
        oComparator1.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Coverage By Latitude"')
        oComparator1.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Gap Duration"')
        oComparator1.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Gaps in Global Coverage"')
        oComparator1.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Global Coverage"')
        oComparator1.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Percent Coverage"')
        oComparator1.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Time To Cover By Region"')

        oAccLoadedCovDef: "CoverageDefinition" = clr.CastAs(
            TestBase.Application.current_scenario.children["AccLoadedCovDef"], CoverageDefinition
        )
        Assert.assertIsNotNone(oAccLoadedCovDef)

        oComparator2 = ReportComparison(self.Units)
        oComparator2.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"Access Duration"')
        oComparator2.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"Coverage By Asset"')
        oComparator2.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"Coverage By Latitude"')
        oComparator2.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"Gap Duration"')
        oComparator2.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"Gaps in Global Coverage"')
        oComparator2.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"Global Coverage"')
        oComparator2.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"Percent Coverage"')
        oComparator2.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"Time To Cover By Region"')

        oAccCompCovDef: "CoverageDefinition" = clr.CastAs(
            TestBase.Application.current_scenario.children["AccCompCovDef"], CoverageDefinition
        )
        Assert.assertIsNotNone(oAccCompCovDef)

        oComparator3 = ReportComparison(self.Units)
        oComparator3.AddReport(clr.CastAs(oAccCompCovDef, IStkObject), '"Access Duration"')
        oComparator3.AddReport(clr.CastAs(oAccCompCovDef, IStkObject), '"Gap Duration"')
        oComparator3.AddReport(clr.CastAs(oAccCompCovDef, IStkObject), '"Gaps in Global Coverage"')
        oComparator3.AddReport(clr.CastAs(oAccCompCovDef, IStkObject), '"Global Coverage"')
        oComparator3.AddReport(clr.CastAs(oAccCompCovDef, IStkObject), '"Time To Cover By Region"')

        oCompOnLoadCovDef: "CoverageDefinition" = clr.CastAs(
            TestBase.Application.current_scenario.children["CompOnLoadCovDef"], CoverageDefinition
        )
        Assert.assertIsNotNone(oCompOnLoadCovDef)

        oComparator4 = ReportComparison(self.Units)
        oComparator4.AddReport(clr.CastAs(oCompOnLoadCovDef, IStkObject), '"Access Duration"')
        oComparator4.AddReport(clr.CastAs(oCompOnLoadCovDef, IStkObject), '"Gap Duration"')

        oComparator5 = ReportComparison(self.Units)
        oComparator5.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"GI Region Coverage"')
        oComparator5.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"GI Region Full Coverage"')
        oComparator5.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"GI Region Partial Coverage"')
        oComparator5.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"GI Region Pass Coverage"')
        oComparator5.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"GI Region Time To Cover"')

        oComparator6 = ReportComparison(self.Units)
        oComparator6.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"GI Point Coverage"')
        oComparator6.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"GI Point Daily Coverage"')
        oComparator6.AddReport(clr.CastAs(oAccLoadedCovDef, IStkObject), '"GI Point Prob Of Coverage"')

        # Connect
        # 1 - Define the grid resolution
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid Resolution LatLon 3.0")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid Resolution Area 200000")
        TestBase.Application.execute_command("SetUnits / km")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid Resolution Distance 300")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid Definition Global")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 2 - Define a Lat Bounds grid
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid Definition LatBounds -10.0 40.0")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 3 - Define a Longitude Line grid
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid Definition LongLine -60.0 30.0 185.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 4 - Define a Custom grid using area targets
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid Definition Custom AreaTarget AreaTarget/Crosses0AT AreaTarget AreaTarget/Crosses180AT"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 5 - Define a Custom grid using a region list
        TestBase.Application.execute_command(
            (
                (
                    'Cov */CoverageDefinition/TestCovDef Grid Definition Custom Region "'
                    + TestBase.GetScenarioFile("CovDefTest", "usstates.rl")
                )
                + '"'
            )
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 6 - Define a Custom grid using area targets and a region list
        TestBase.Application.execute_command(
            (
                (
                    'Cov */CoverageDefinition/TestCovDef Grid Definition Custom Region "'
                    + TestBase.GetScenarioFile("CovDefTest", "usstates.rl")
                )
                + '" AreaTarget AreaTarget/Crosses0AT '
            )
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 7 - Coverage Grid Point Definitions 1
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid PointDef Aircraft 100000.0")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 8 - Coverage Grid Point Definitions 2
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid PointDef Facility 0.0")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid PointDef Facility ")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 9 - Coverage Grid Point Definitions 3
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef Facility 0.0 Facility/CovDefTest"
        )
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef Facility Facility/CovDefTest"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 10 - Coverage Grid Point Definitions 4
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef Radar 100000 Aircraft/CovDefTest/Radar/CovDefTest  "
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 11 - Coverage Grid Point Definitions 5
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef Receiver 9000 Facility/CovDefTest/Receiver/CovDefTest"
        )
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef Receiver Facility/CovDefTest/Receiver/CovDefTest"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 12 - Coverage Grid Point Definitions 6
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid PointDef Satellite 200000.0")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 13 - Coverage Grid Point Definitions 7
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef Satellite 200000.0 Satellite/CovDefTest1"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 14 - Coverage Grid Point Definitions 8
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef Transmitter 100000 Aircraft/CovDefTest/Transmitter/CovDefTest"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 15 - Coverage Grid Point Definitions 9
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid PointDef Target 0.0")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid PointDef Target")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 16 - Coverage Grid Point Definitions 10
        TestBase.Application.execute_command(
            (
                (
                    'Cov */CoverageDefinition/TestCovDef Grid PointDef Custom "'
                    + TestBase.GetScenarioFile("CovDefTest", "Sample.pnt")
                )
                + '"'
            )
        )
        TestBase.Application.execute_command("Cov_RM */CoverageDefinition/TestCovDef GridPoints")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 17 - Coverage Assets and Coverage Computation 1
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Asset */Chain/CovDefTest Assign")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Constellation/CovDefTest2 Assign"
        )
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Satellite/CovDefTest2/Sensor/SimpleCone Assign"
        )
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Asset */Aircraft/CovDefTest Assign")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Compute")
        TestBase.Application.execute_command("Cov */CoverageDefinition/AccCompCovDef Access Compute")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access AutoRecompute Off")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 18 - Coverage Assets and Coverage Computation 2
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Constellation/CovDefTest2 DeAssign"
        )
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Satellite/CovDefTest2/Sensor/SimpleCone DeAssign"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 19 - Coverage Assets and Coverage Computation 3
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Constellation/CovDefTest2 Assign"
        )
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Satellite/CovDefTest2/Sensor/SimpleCone Assign"
        )
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Asset */Chain/CovDefTest DeActivate")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Aircraft/CovDefTest DeActivate"
        )
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Satellite/CovDefTest1 DeActivate"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 20 - Coverage Assets and Coverage Computation 4
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access AutoRecompute On")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 21 - Coverage Assets and Coverage Computation 5
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Asset */Chain/CovDefTest Activate")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Asset */Aircraft/CovDefTest Activate")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Satellite/CovDefTest1 Activate"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 22 - Coverage Assets and Coverage Computation 6
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Clear")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 23 - Coverage Assets and Coverage Computation 7
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Compute")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 24 - Access save mode and data export 1
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access SaveMode Save")
        TestBase.Application.execute_command(
            (('Save / */CoverageDefinition/TestCovDef "' + TestBase.GetScenarioFile("CovDefTest", "Test")) + '"')
        )
        TestBase.Application.execute_command("Unload / */CoverageDefinition/TestCovDef")
        TestBase.Application.execute_command(
            (('Load / */CoverageDefinition "' + TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef.cv")) + '"')
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 25 - Access save mode and data export 2
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access SaveMode NoSave")
        TestBase.Application.execute_command(
            (('Save / */CoverageDefinition/TestCovDef "' + TestBase.GetScenarioFile("CovDefTest", "Test")) + '"')
        )
        TestBase.Application.execute_command("Unload / */CoverageDefinition/TestCovDef")
        TestBase.Application.execute_command(
            (('Load / */CoverageDefinition "' + TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef.cv")) + '"')
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 26 - Access save mode and data export 3
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access SaveMode ComputeOnLoad")
        TestBase.Application.execute_command(
            (('Save / */CoverageDefinition/TestCovDef "' + TestBase.GetScenarioFile("CovDefTest", "Test")) + '"')
        )
        TestBase.Application.execute_command("Unload / */CoverageDefinition/TestCovDef")
        TestBase.Application.execute_command(
            (('Load / */CoverageDefinition "' + TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef.cv")) + '"')
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 27 - Access save mode and data export 4
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access DataRetention Static")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Clear")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Compute")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 28 - Access save mode and data export 5
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access DataRetention All")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Clear")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Compute")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 29 - Coverage definition interval 1
        TestBase.Application.execute_command(
            'Cov */CoverageDefinition/TestCovDef Interval "1 Oct 2000 06:00:00" "1 Oct 2000 18:00:00"'
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 30 - Coverage definition interval 2
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Interval Scenario")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 31 - Report new CovDef data
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid Definition Custom AreaTarget AreaTarget/Crosses0AT "
        )
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid Resolution LatLon 2.0")
        oComparator1.TakeConnectSnapshot(TestBase.Application)
        oComparator2.TakeConnectSnapshot(TestBase.Application)
        oComparator3.TakeConnectSnapshot(TestBase.Application)
        oComparator4.TakeConnectSnapshot(TestBase.Application)

        # 32 - Test the grid inspector 1
        TestBase.Application.execute_command("Cov_R */CoverageDefinition/AccLoadedCovDef Inspector Region Crosses0AT")
        oComparator5.TakeConnectSnapshot(TestBase.Application)

        # 33 - Test the grid inspector 2
        TestBase.Application.execute_command("Cov_R */CoverageDefinition/AccLoadedCovDef Inspector Point 20.0 20.0")
        oComparator6.TakeConnectSnapshot(TestBase.Application)

        # 34 - Coverage Grid sending custom points directly 1
        TestBase.Application.execute_command(
            (
                (
                    'Cov */CoverageDefinition/TestCovDef Grid Definition Custom Region "'
                    + TestBase.GetScenarioFile("CovDefTest", "usstates.rl")
                )
                + '" AreaTarget AreaTarget/Crosses0AT '
            )
        )
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef SetPointsLLA 4 6.9346423789e+01    -5.0260748372e+01    0.0000000000e+00  3.9613371741e+01    -6.6285429903e+01    0.0000000000e+00  3.9880319688e+01    -7.3881767479e+01    0.0000000000e+00 -4.0700636942e+01    -1.1224999998e+02    0.0000000000e+00"
        )
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Compute")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 35 - Coverage Grid sending custom points directly 2
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef SetPointsLLA 4 48.0 -115.0 0.00  48.0  -91.0  0.0  33.0 -91.0  0.0 33.0 -115.0  0.0"
        )
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Compute")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 36 - Coverage Grid sending custom points directly 3
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Grid PointDef Satellite Altitude 200")
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Compute")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 37 - Coverage Grid sending custom points directly 4
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Grid PointDef Satellite AltAboveTerrain 200"
        )
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Access Compute")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 38 - Coverage Asset group and separate actions 1
        TestBase.Application.execute_command("Cov */CoverageDefinition/TestCovDef Asset */Chain/CovDefTest Deassign")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Constellation/CovDefTest1 Assign"
        )
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Constellation/CovDefTest1 Group"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # 39 - Coverage Asset group and separate actions
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/TestCovDef Asset */Constellation/CovDefTest1 Separate"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # Object Model
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("CovDefTest", "CovDefTest.sc"))
        Definition.AG_COV = CoverageDefinition(
            TestBase.Application.current_scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "TestCovDef")
        )

        oGrid: "CoverageGrid" = Definition.AG_COV.grid
        oGrid.resolution_type = CoverageResolution.RESOLUTION_LATITUDE_LONGITUDE
        oResolution: "ICoverageResolution" = oGrid.resolution
        oLat: "CoverageResolutionLatLon" = clr.CastAs(oResolution, CoverageResolutionLatLon)
        oLat.latitude_longitude = 3.0

        oGrid.resolution_type = CoverageResolution.RESOLUTION_AREA
        oResolution = oGrid.resolution
        oArea: "CoverageResolutionArea" = clr.CastAs(oResolution, CoverageResolutionArea)
        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "km")
        oArea.area = 200000

        oGrid.resolution_type = CoverageResolution.RESOLUTION_DISTANCE
        oResolution = oGrid.resolution
        oDistance: "CoverageResolutionDistance" = clr.CastAs(oResolution, CoverageResolutionDistance)
        oDistance.distance = 300

        # 1
        oGrid.bounds_type = CoverageBounds.GLOBAL
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 2
        oGrid.bounds_type = CoverageBounds.LATITUDE
        oBounds: "ICoverageBounds" = oGrid.bounds
        oBoundsLat: "CoverageBoundsLatitude" = clr.CastAs(oBounds, CoverageBoundsLatitude)
        oBoundsLat.minimum_latitude = -10.0
        oBoundsLat.maximum_latitude = 40.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 3
        oGrid.bounds_type = CoverageBounds.LONGITUDE_LINE
        oBoundsLonLine: "CoverageBoundsLongitudeLine" = clr.CastAs(oGrid.bounds, CoverageBoundsLongitudeLine)
        oBoundsLonLine.minimum_latitude = -60.0
        oBoundsLonLine.maximum_latitude = 30.0
        oBoundsLonLine.longitude = 185.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 4
        oGrid.bounds_type = CoverageBounds.CUSTOM_REGIONS
        oBoundsCustom: "CoverageBoundsCustomRegions" = clr.CastAs(oGrid.bounds, CoverageBoundsCustomRegions)
        oBoundsCustom.area_targets.add("AreaTarget/Crosses0AT")
        oBoundsCustom.area_targets.add("AreaTarget/Crosses180AT")
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 5
        oBoundsCustom.area_targets.remove_all()
        oBoundsCustom.region_files.add(TestBase.GetScenarioFile("CovDefTest", "usstates.rl"))
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 6
        oBoundsCustom.area_targets.add("AreaTarget/Crosses0AT")
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 7
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.AIRCRAFT
        TestBase.logger.WriteLine2(Definition.AG_COV.point_definition.ground_altitude_method)
        Definition.AG_COV.point_definition.altitude_method = CoverageAltitudeMethod.ABOVE_ELLIPSOID
        Definition.AG_COV.point_definition.altitude = 100000.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 8
        Definition.AG_COV.point_definition.use_grid_seed = True
        Definition.AG_COV.point_definition.use_object_as_seed = True
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.FACILITY
        Definition.AG_COV.point_definition.altitude = 0
        Definition.AG_COV.point_definition.altitude_method = CoverageAltitudeMethod.ABOVE_ELLIPSOID
        Definition.AG_COV.point_definition.ground_altitude_method = CoverageGroundAltitudeMethod.USE_POINT_ALTITUDE
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 9
        Definition.AG_COV.point_definition.use_grid_seed = True
        Definition.AG_COV.point_definition.use_object_as_seed = True
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.FACILITY
        Definition.AG_COV.point_definition.seed_instance = "Facility/CovDefTest"
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 10
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.RADAR
        Definition.AG_COV.point_definition.use_object_as_seed = True
        Definition.AG_COV.point_definition.seed_instance = "Aircraft/CovDefTest/Radar/CovDefTest"
        Definition.AG_COV.point_definition.altitude_method = CoverageAltitudeMethod.ABOVE_ELLIPSOID
        Definition.AG_COV.point_definition.altitude = 100000.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # // 11
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.RECEIVER
        Definition.AG_COV.point_definition.seed_instance = "Facility/CovDefTest/Receiver/CovDefTest"
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 12
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.SATELLITE
        Definition.AG_COV.point_definition.altitude_method = CoverageAltitudeMethod.ABOVE_ELLIPSOID
        Definition.AG_COV.point_definition.altitude = 200000
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 13
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.SATELLITE
        Definition.AG_COV.point_definition.use_grid_seed = True
        Definition.AG_COV.point_definition.altitude_method = CoverageAltitudeMethod.ABOVE_ELLIPSOID
        Definition.AG_COV.point_definition.altitude = 200000
        Definition.AG_COV.point_definition.seed_instance = "Satellite/CovDefTest1"
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 14
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.TRANSMITTER
        Definition.AG_COV.point_definition.seed_instance = "Aircraft/CovDefTest/Transmitter/CovDefTest"
        Definition.AG_COV.point_definition.altitude_method = CoverageAltitudeMethod.ABOVE_ELLIPSOID
        Definition.AG_COV.point_definition.altitude = 100000
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 15
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.TARGET
        Definition.AG_COV.point_definition.ground_altitude_method = CoverageGroundAltitudeMethod.USE_POINT_ALTITUDE
        Definition.AG_COV.point_definition.altitude = 0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 16
        Definition.AG_COV.point_definition.point_location_method = CoveragePointLocationMethod.SPECIFY_CUSTOM_LOCATIONS
        Definition.AG_COV.point_definition.point_file_list.add(TestBase.GetScenarioFile("CovDefTest", "Sample.pnt"))
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 17
        Definition.AG_COV.asset_list.add("Chain/CovDefTest")
        Definition.AG_COV.asset_list.add("Constellation/CovDefTest2")
        Definition.AG_COV.asset_list.add("Satellite/CovDefTest2/Sensor/SimpleCone")
        Definition.AG_COV.asset_list.add("Aircraft/CovDefTest")
        Definition.AG_COV.compute_accesses()
        AG_COV2: "CoverageDefinition" = CoverageDefinition(
            TestBase.Application.current_scenario.children["AccCompCovDef"]
        )
        Assert.assertIsNotNone(AG_COV2)
        AG_COV2.compute_accesses()
        Definition.AG_COV.advanced.recompute_automatically = False
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 18
        Definition.AG_COV.asset_list.remove("Constellation/CovDefTest2")
        Definition.AG_COV.asset_list.remove("Satellite/CovDefTest2/Sensor/SimpleCone")
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 19
        Definition.AG_COV.asset_list.add("Constellation/CovDefTest2")
        Definition.AG_COV.asset_list.add("Satellite/CovDefTest2/Sensor/SimpleCone")
        assetListElement: "CoverageAssetListElement"
        for assetListElement in Definition.AG_COV.asset_list:
            TestBase.logger.WriteLine7(
                "Name = {0}, Grouping = {1}", assetListElement.object_name, assetListElement.grouping
            )
            if (assetListElement.object_name == "Chain/CovDefTest") or (
                assetListElement.object_name == "Aircraft/CovDefTest"
            ):
                assetListElement.asset_status = CoverageAssetStatus.INACTIVE

            elif assetListElement.object_name == "Constellation/CovDefTest2":
                subAssets: "CoverageAssetListCollection" = assetListElement.sub_asset_list
                subAsset: "CoverageAssetListElement"
                for subAsset in subAssets:
                    if subAsset.object_name == "Satellite/CovDefTest1":
                        subAsset.asset_status = CoverageAssetStatus.INACTIVE

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 20
        Definition.AG_COV.advanced.recompute_automatically = True
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 21
        assetListElement: "CoverageAssetListElement"

        # 21
        for assetListElement in Definition.AG_COV.asset_list:
            if (assetListElement.object_name == "Chain/CovDefTest") or (
                assetListElement.object_name == "Aircraft/CovDefTest"
            ):
                assetListElement.asset_status = CoverageAssetStatus.ACTIVE

            elif assetListElement.object_name == "Constellation/CovDefTest2":
                subAssets: "CoverageAssetListCollection" = assetListElement.sub_asset_list
                subAsset: "CoverageAssetListElement"
                for subAsset in subAssets:
                    if subAsset.object_name == "Satellite/CovDefTest1":
                        subAsset.asset_status = CoverageAssetStatus.ACTIVE

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 22
        Definition.AG_COV.clear_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 23
        Definition.AG_COV.compute_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 24
        Definition.AG_COV.advanced.save_mode = DataSaveMode.SAVE_ACCESSES
        (IStkObject(Definition.AG_COV)).export(TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef"))
        TestBase.Application.current_scenario.children.unload(STKObjectType.COVERAGE_DEFINITION, "TestCovDef")
        TestBase.Application.current_scenario.children.import_object(
            TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef.cv")
        )
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 25
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["TestCovDef"])
        Definition.AG_COV.advanced.save_mode = DataSaveMode.DONT_SAVE_ACCESSES
        (IStkObject(Definition.AG_COV)).export(TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef"))
        TestBase.Application.current_scenario.children.unload(STKObjectType.COVERAGE_DEFINITION, "TestCovDef")
        TestBase.Application.current_scenario.children.import_object(
            TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef.cv")
        )
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 26
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["TestCovDef"])
        Definition.AG_COV.advanced.save_mode = DataSaveMode.DONT_SAVE_COMPUTE_ON_LOAD
        (IStkObject(Definition.AG_COV)).export(TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef"))
        TestBase.Application.current_scenario.children.unload(STKObjectType.COVERAGE_DEFINITION, "TestCovDef")
        TestBase.Application.current_scenario.children.import_object(
            TestBase.GetScenarioFile("CovDefTest", "Test", "TestCovDef.cv")
        )
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 27
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["TestCovDef"])
        Definition.AG_COV.advanced.data_retention = CoverageDataRetention.STATIC_DATA_ONLY
        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.compute_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 28
        Definition.AG_COV.advanced.data_retention = CoverageDataRetention.ALL_DATA
        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.compute_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 29 - Coverage definition interval 1
        Definition.AG_COV.interval.use_scenario_interval = False
        Definition.AG_COV.interval.analysis_interval.set_explicit_interval("1 Oct 2000 06:00:00", "1 Oct 2000 18:00:00")
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 30 - Coverage definition interval 2
        Definition.AG_COV.interval.use_scenario_interval = True
        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.compute_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 31 - Report new CovDef data
        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.grid.bounds_type = CoverageBounds.CUSTOM_REGIONS
        oBoundsCustom = clr.CastAs(Definition.AG_COV.grid.bounds, CoverageBoundsCustomRegions)
        oBoundsCustom.region_files.remove_all()
        oBoundsCustom.area_targets.remove_all()
        oBoundsCustom.area_targets.add("AreaTarget/Crosses0AT")
        Definition.AG_COV.grid.resolution_type = CoverageResolution.RESOLUTION_LATITUDE_LONGITUDE
        oLat = clr.CastAs(Definition.AG_COV.grid.resolution, CoverageResolutionLatLon)
        oLat.latitude_longitude = 2.0
        Definition.AG_COV.compute_accesses()
        oComparator1.TakeOMSnapshot(TestBase.Application)
        oComparator2.TakeOMSnapshot(TestBase.Application)
        oComparator3.TakeOMSnapshot(TestBase.Application)
        oComparator4.TakeOMSnapshot(TestBase.Application)

        # 32 - Test the grid inspector 1
        oAccLoadedCovDef = clr.CastAs(
            TestBase.Application.current_scenario.children["AccLoadedCovDef"], CoverageDefinition
        )
        oAccLoadedCovDef.grid_inspector.select_region("Crosses0AT")
        oComparator5.TakeOMSnapshot(TestBase.Application)

        # 33 - Test the grid inspector 2
        oAccLoadedCovDef.grid_inspector.select_point(20.0, 20.0)
        oComparator6.TakeOMSnapshot(TestBase.Application)

        # 34 - Coverage Grid sending custom points directly 1
        Definition.AG_COV.grid.bounds_type = CoverageBounds.CUSTOM_REGIONS
        oBoundsCustom = clr.CastAs(Definition.AG_COV.grid.bounds, CoverageBoundsCustomRegions)
        oBoundsCustom.region_files.remove_all()
        oBoundsCustom.region_files.add(TestBase.GetScenarioFile("CovDefTest", "usstates.rl"))
        oBoundsCustom.area_targets.remove_all()
        oBoundsCustom.area_targets.add("AreaTarget/Crosses0AT")
        points = Array.CreateInstance(clr.TypeOf(Object), 4, 3)
        points[0][0] = 69.346423789
        points[0][1] = -50.260748372
        points[0][2] = 0.0
        points[1][0] = 39.613371741
        points[1][1] = -66.285429903
        points[1][2] = 0.0
        points[2][0] = 39.880319688
        points[2][1] = -73.881767479
        points[2][2] = 0.0
        points[3][0] = -40.700636942
        points[3][1] = -112.24999998
        points[3][2] = 0.0
        Definition.AG_COV.point_definition.set_points_detic(points)
        Definition.AG_COV.compute_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 35 - Coverage Grid sending custom points directly 2
        points = Array.CreateInstance(clr.TypeOf(Object), 4, 3)
        points[0][0] = 48.0
        points[0][1] = -115.0
        points[0][2] = 0
        points[1][0] = 48
        points[1][1] = -91.0
        points[1][2] = 0
        points[2][0] = 33
        points[2][1] = -91
        points[2][2] = 0
        points[3][0] = 33
        points[3][1] = -115
        points[3][2] = 0
        Definition.AG_COV.point_definition.ground_altitude_method = CoverageGroundAltitudeMethod.USE_POINT_ALTITUDE
        Definition.AG_COV.point_definition.set_points_detic(points)
        Definition.AG_COV.compute_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 36 - Coverage Grid sending custom points directly 3
        Definition.AG_COV.point_definition.grid_class = CoverageGridClass.SATELLITE
        Definition.AG_COV.point_definition.altitude = 200
        Definition.AG_COV.compute_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 37 - Coverage Grid sending custom points directly 4
        Definition.AG_COV.point_definition.altitude_method = CoverageAltitudeMethod.ABOVE_TERRAIN
        Definition.AG_COV.point_definition.altitude = 200
        Definition.AG_COV.compute_accesses()
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 38 - Coverage Asset group and separate actions 1
        Definition.AG_COV.asset_list.remove("Chain/CovDefTest")
        oAssetElement: "CoverageAssetListElement" = Definition.AG_COV.asset_list.add("Constellation/CovDefTest1")
        oAssetElement.grouping = CoverageAssetGrouping.GROUPED
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # 39 - Coverage Asset group and separate actions 2
        oAssetElement.grouping = CoverageAssetGrouping.SEPARATE
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        CompareUtility.CompareReportSnapshots()
        oComparator1.CompareReportSnapshots()
        oComparator2.CompareReportSnapshots()
        oComparator3.CompareReportSnapshots()
        oComparator4.CompareReportSnapshots()
        oComparator5.CompareReportSnapshots()
        oComparator5.CompareReportSnapshots()

        TestBase.Application.execute_command("SetUnits / METER")

    # endregion

    # region CoverageDefinitionPointTest
    # The purpose of this test is to test the Coverage Module by determining coverage
    # information for a single Point, which then can be compared using standard
    # Chains and Access capabilities
    def CoverageDefinitionPointTest(self):
        # Connect
        # Load the Scenario
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("CovPointTest", "CovPointTest.sc"))

        # 1 - Facility LLA Position
        Definition.AG_FA = Facility(
            TestBase.Application.current_scenario.children.get_elements(STKObjectType.FACILITY)["MidNorth"]
        )
        Assert.assertIsNotNone(Definition.AG_FA)

        # Report initialization
        oComparator1 = ReportComparison(self.Units)
        oComparator1.AddReport(clr.CastAs(Definition.AG_FA, IStkObject), '"LLA Position"')
        oComparator1.TakeConnectSnapshot(TestBase.Application)

        # 2 - CoverageDefinition (MidNorth) Grid Point Information
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorth"])
        Assert.assertIsNotNone(Definition.AG_COV)
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Clear")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access AutoRecompute Off")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access UseLightTimeDelay Off")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access TimeConvergence 0.001")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access SaveMode NoSave")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access AssetsRequired AtLeast 1")
        TestBase.Application.execute_command(
            'Cov */CoverageDefinition/MidNorth Interval "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )

        # Report initialization
        oComparator2 = ReportComparison(self.Units)
        oComparator2.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Grid Point Information"')
        oComparator2.TakeConnectSnapshot(TestBase.Application)

        # 3 - CoverageDefinition (MidNorthExercise) Grid Point Information
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorthExercise"])
        Assert.assertIsNotNone(Definition.AG_COV)
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthExercise Access Clear")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthExercise Access AutoRecompute Off")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthExercise Access UseLightTimeDelay Off")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthExercise Access TimeConvergence 0.001")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthExercise Access SaveMode NoSave")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/MidNorthExercise Access AssetsRequired AtLeast 1"
        )
        TestBase.Application.execute_command(
            'Cov */CoverageDefinition/MidNorthExercise Interval "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )

        # Report initialization
        oComparator3 = ReportComparison(self.Units)
        oComparator3.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Grid Point Information"')
        oComparator3.TakeConnectSnapshot(TestBase.Application)

        # 4 - CoverageDefinition (MidNorth-Meos) Grid Point Information
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorth-Meos"])
        Assert.assertIsNotNone(Definition.AG_COV)
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access Clear")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access AutoRecompute Off")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access UseLightTimeDelay Off")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access TimeConvergence 0.001")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access SaveMode NoSave")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access AssetsRequired AtLeast 1")
        TestBase.Application.execute_command(
            'Cov */CoverageDefinition/MidNorth-Meos Interval "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )

        # Report initialization
        oComparator4 = ReportComparison(self.Units)
        oComparator4.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Grid Point Information"')
        oComparator4.TakeConnectSnapshot(TestBase.Application)

        # 5 - CoverageDefinition (MidNorthUK) Grid Point Information
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorthUK"])
        Assert.assertIsNotNone(Definition.AG_COV)
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthUK Access Clear")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthUK Access AutoRecompute Off")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthUK Access UseLightTimeDelay Off")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthUK Access TimeConvergence 0.001")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthUK Access SaveMode NoSave")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorthUK Access AssetsRequired AtLeast 1")
        TestBase.Application.execute_command(
            'Cov */CoverageDefinition/MidNorthUK Interval "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )

        # Report initialization
        oComparator5 = ReportComparison(self.Units)
        oComparator5.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Grid Point Information"')
        oComparator5.TakeConnectSnapshot(TestBase.Application)

        # 6 - Chains
        # MidNorthChn
        TestBase.Application.execute_command("Chains */Chain/MidNorthChn ClearAccesses")
        TestBase.Application.execute_command("Chains */Chain/MidNorthChn AutoRecompute Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorthChn UseLightTimeDelay Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorthChn TimeConvergence 0.001")
        TestBase.Application.execute_command(
            'Chains */Chain/MidNorthChn SetComputeTime UserSpecified "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )
        # MidNorth-to-OnlyLeo28
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-OnlyLeo28 ClearAccesses")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-OnlyLeo28 AutoRecompute Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-OnlyLeo28 UseLightTimeDelay Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-OnlyLeo28 TimeConvergence 0.001")
        TestBase.Application.execute_command(
            'Chains */Chain/MidNorth-to-OnlyLeo28 SetComputeTime UserSpecified "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )
        # MidNorth-to-Leo28
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leo28 ClearAccesses")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leo28 AutoRecompute Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leo28 UseLightTimeDelay Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leo28 TimeConvergence 0.001")
        TestBase.Application.execute_command(
            'Chains */Chain/MidNorth-to-Leo28 SetComputeTime UserSpecified "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )
        # MidNorth-to-Leos
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos ClearAccesses")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos AutoRecompute Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos UseLightTimeDelay Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos TimeConvergence 0.001")
        TestBase.Application.execute_command(
            'Chains */Chain/MidNorth-to-Leos SetComputeTime UserSpecified "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )
        # MidNorth-to-Meos
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Meos ClearAccesses")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Meos AutoRecompute Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Meos UseLightTimeDelay Off")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Meos TimeConvergence 0.001")
        TestBase.Application.execute_command(
            'Chains */Chain/MidNorth-to-Meos SetComputeTime UserSpecified "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )
        # UK-to-Meos
        TestBase.Application.execute_command("Chains */Chain/UK-to-Meos ClearAccesses")
        TestBase.Application.execute_command("Chains */Chain/UK-to-Meos AutoRecompute Off")
        TestBase.Application.execute_command("Chains */Chain/UK-to-Meos UseLightTimeDelay Off")
        TestBase.Application.execute_command("Chains */Chain/UK-to-Meos TimeConvergence 0.001")
        TestBase.Application.execute_command(
            'Chains */Chain/UK-to-Meos SetComputeTime UserSpecified "1 Jul 2005 12:00:00" "2 Jul 2005 12:00:00"'
        )

        # 7 - Constellations
        TestBase.Application.execute_command("SetConstraint */Constellation/OnlyLeo28 Operator Any")
        TestBase.Application.execute_command("SetConstraint */Constellation/Leos Operator Any")
        TestBase.Application.execute_command("SetConstraint */Constellation/Meos Operator Any")

        # Section 2: Test capabilities for previous to STK 8.1
        # Asset: Single Object
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorth"])
        Assert.assertIsNotNone(Definition.AG_COV)

        oComparator6 = ReportComparison(self.Units)
        oComparator6.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Global Coverage Times"')

        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Asset */Satellite/Leo_28 Assign")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Compute")

        oComparator6.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Clear")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Asset */Satellite/Leo_28 Deassign")

        # Asset: Constellation of 1 object
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Asset */Constellation/OnlyLeo28 Assign")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Compute")

        oComparator6.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Clear")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/MidNorth Asset */Constellation/OnlyLeo28 Deassign"
        )

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-OnlyLeo28"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)

        oComparator7 = ReportComparison(self.Units)
        oComparator7.AddReport(clr.CastAs(Definition.AG_CHAIN, IStkObject), '"Complete Chain Access"')

        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-OnlyLeo28 Compute")

        oComparator7.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-OnlyLeo28 ClearAccesses")

        # Asset: Constellation of 3 objects (AnyOf)
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Asset */Constellation/Leos Assign")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Compute")

        oComparator6.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Clear")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos Compute")

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Leos"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)

        oComparator8 = ReportComparison(self.Units)
        oComparator8.AddReport(clr.CastAs(Definition.AG_CHAIN, IStkObject), '"Complete Chain Access"')
        oComparator8.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos ClearAccesses")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Asset */Constellation/Leos Deassign")

        # Asset: Chain of single objects
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Asset */Chain/MidNorth-to-Leo28 Assign")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Compute")

        oComparator6.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Clear")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/MidNorth Asset */Chain/MidNorth-to-Leo28 Deassign"
        )
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leo28 Compute")

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Leo28"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)

        oComparator9 = ReportComparison(self.Units)
        oComparator9.AddReport(clr.CastAs(Definition.AG_CHAIN, IStkObject), '"Complete Chain Access"')
        oComparator9.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leo28 ClearAccesses")

        # Asset: Chain ending in Constellation
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Asset */Chain/MidNorth-to-Leos Assign")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Compute")

        oComparator6.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth Access Clear")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/MidNorth Asset */Chain/MidNorth-to-Leos Deassign"
        )
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos Compute")

        oComparator8.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos ClearAccesses")

        # Section 3: Test NAsset capability of coverage
        # NAsset: AtLeast 2
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access Compute")
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/MidNorth-Meos/FigureOfMerit/NAsset FOMDefine Satisfaction AtLeast 2"
        )

        Definition.AG_FOM = None
        Definition.AG_FOM = FigureOfMerit(
            TestBase.Application.current_scenario.children["MidNorth-Meos"].children["NAsset"]
        )
        Assert.assertIsNotNone(Definition.AG_FOM)

        oComparator10 = ReportComparison(self.Units)
        oComparator10.AddReport(clr.CastAs(Definition.AG_FOM, IStkObject), '"Global Satisfaction Intervals"')

        oComparator10.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access AssetsRequired AtLeast 2")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access Compute")

        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorth-Meos"])
        Assert.assertIsNotNone(Definition.AG_COV)

        oComparator11 = ReportComparison(self.Units)
        oComparator11.AddReport(clr.CastAs(Definition.AG_COV, IStkObject), '"Global Coverage Times"')

        oComparator11.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access Clear")
        TestBase.Application.execute_command("Cov */CoverageDefinition/MidNorth-Meos Access Compute")

        oComparator11.TakeConnectSnapshot(TestBase.Application)
        oComparator10.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Meos"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)

        oComparator12 = ReportComparison(self.Units)
        oComparator12.AddReport(clr.CastAs(Definition.AG_CHAIN, IStkObject), '"Complete Chain Access"')

        TestBase.Application.execute_command("SetConstraint */Constellation/Meos Operator AtLeast 2")
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Meos Compute")

        oComparator12.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Meos ClearAccesses")

        # NAsset: Exactly 3

        # Object Model
        # Load the Scenario
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("CovPointTest", "CovPointTest.sc"))

        # 1 - Facility LLA Position
        Definition.AG_FA = None
        Definition.AG_FA = Facility(
            TestBase.Application.current_scenario.children.get_elements(STKObjectType.FACILITY)["MidNorth"]
        )
        Assert.assertIsNotNone(Definition.AG_FA)

        oComparator1.TakeOMSnapshot(TestBase.Application)

        # 2 - CoverageDefinition (MidNorth) Grid Point Information
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorth"])
        Assert.assertIsNotNone(Definition.AG_COV)

        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.advanced.recompute_automatically = False
        Definition.AG_COV.advanced.enable_light_time_delay = False
        Definition.AG_COV.advanced.save_mode = DataSaveMode.DONT_SAVE_ACCESSES
        Definition.AG_COV.advanced.n_assets_satisfaction_type = CoverageSatisfactionType.AT_LEAST
        Definition.AG_COV.advanced.n_assets_satisfaction_threshold = 1
        Definition.AG_COV.interval.use_scenario_interval = False
        Definition.AG_COV.interval.analysis_interval.set_explicit_interval("1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00")
        Definition.AG_COV.compute_accesses()

        oComparator2.TakeOMSnapshot(TestBase.Application)

        # 3 - CoverageDefinition (MidNorthExercise) Grid Point Information
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorthExercise"])
        Assert.assertIsNotNone(Definition.AG_COV)

        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.advanced.recompute_automatically = False
        Definition.AG_COV.advanced.enable_light_time_delay = False
        Definition.AG_COV.advanced.save_mode = DataSaveMode.DONT_SAVE_ACCESSES
        Definition.AG_COV.advanced.n_assets_satisfaction_type = CoverageSatisfactionType.AT_LEAST
        Definition.AG_COV.advanced.n_assets_satisfaction_threshold = 1
        Definition.AG_COV.interval.use_scenario_interval = False
        Definition.AG_COV.interval.analysis_interval.set_explicit_interval("1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00")
        Definition.AG_COV.compute_accesses()

        oComparator3.TakeOMSnapshot(TestBase.Application)

        # 4 - CoverageDefinition (MidNorth-Meos) Grid Point Information
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorth-Meos"])
        Assert.assertIsNotNone(Definition.AG_COV)

        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.advanced.recompute_automatically = False
        Definition.AG_COV.advanced.enable_light_time_delay = False
        Definition.AG_COV.advanced.save_mode = DataSaveMode.DONT_SAVE_ACCESSES
        Definition.AG_COV.advanced.n_assets_satisfaction_type = CoverageSatisfactionType.AT_LEAST
        Definition.AG_COV.advanced.n_assets_satisfaction_threshold = 1
        Definition.AG_COV.interval.use_scenario_interval = False
        Definition.AG_COV.interval.analysis_interval.set_explicit_interval("1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00")
        Definition.AG_COV.compute_accesses()

        oComparator4.TakeOMSnapshot(TestBase.Application)

        # 5 - CoverageDefinition (MidNorthUK) Grid Point Information
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorthUK"])
        Assert.assertIsNotNone(Definition.AG_COV)

        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.advanced.recompute_automatically = False
        Definition.AG_COV.advanced.enable_light_time_delay = False
        Definition.AG_COV.advanced.save_mode = DataSaveMode.DONT_SAVE_ACCESSES
        Definition.AG_COV.advanced.n_assets_satisfaction_type = CoverageSatisfactionType.AT_LEAST
        Definition.AG_COV.advanced.n_assets_satisfaction_threshold = 1
        Definition.AG_COV.interval.use_scenario_interval = False
        Definition.AG_COV.interval.analysis_interval.set_explicit_interval("1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00")
        Definition.AG_COV.compute_accesses()

        oComparator5.TakeOMSnapshot(TestBase.Application)

        # 6 - Chains
        # MidNorthChn
        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorthChn"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)
        Definition.AG_CHAIN.clear_access()
        Definition.AG_CHAIN.recompute_automatically = False
        Definition.AG_CHAIN.enable_light_time_delay = False
        Definition.AG_CHAIN.time_convergence = 0.001
        Definition.AG_CHAIN.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)
        (ChainUserSpecifiedTimePeriod(Definition.AG_CHAIN.time_period)).time_interval.set_explicit_interval(
            "1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00"
        )
        Definition.AG_CHAIN.compute_access()
        # MidNorth-to-OnlyLeo28
        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-OnlyLeo28"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)
        Definition.AG_CHAIN.clear_access()
        Definition.AG_CHAIN.recompute_automatically = False
        Definition.AG_CHAIN.enable_light_time_delay = False
        Definition.AG_CHAIN.time_convergence = 0.001
        Definition.AG_CHAIN.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)
        (ChainUserSpecifiedTimePeriod(Definition.AG_CHAIN.time_period)).time_interval.set_explicit_interval(
            "1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00"
        )
        Definition.AG_CHAIN.compute_access()
        # MidNorth-to-Leo28
        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Leo28"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)
        Definition.AG_CHAIN.clear_access()
        Definition.AG_CHAIN.recompute_automatically = False
        Definition.AG_CHAIN.enable_light_time_delay = False
        Definition.AG_CHAIN.time_convergence = 0.001
        Definition.AG_CHAIN.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)
        (ChainUserSpecifiedTimePeriod(Definition.AG_CHAIN.time_period)).time_interval.set_explicit_interval(
            "1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00"
        )
        Definition.AG_CHAIN.compute_access()
        # MidNorth-to-Leos
        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Leos"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)
        Definition.AG_CHAIN.clear_access()
        Definition.AG_CHAIN.recompute_automatically = False
        Definition.AG_CHAIN.enable_light_time_delay = False
        Definition.AG_CHAIN.time_convergence = 0.001
        Definition.AG_CHAIN.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)
        (ChainUserSpecifiedTimePeriod(Definition.AG_CHAIN.time_period)).time_interval.set_explicit_interval(
            "1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00"
        )
        Definition.AG_CHAIN.compute_access()
        # MidNorth-to-Meos
        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Meos"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)
        Definition.AG_CHAIN.clear_access()
        Definition.AG_CHAIN.recompute_automatically = False
        Definition.AG_CHAIN.enable_light_time_delay = False
        Definition.AG_CHAIN.time_convergence = 0.001
        Definition.AG_CHAIN.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)
        (ChainUserSpecifiedTimePeriod(Definition.AG_CHAIN.time_period)).time_interval.set_explicit_interval(
            "1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00"
        )
        Definition.AG_CHAIN.compute_access()
        # UK-to-Meos
        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["UK-to-Meos"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)
        Definition.AG_CHAIN.clear_access()
        Definition.AG_CHAIN.recompute_automatically = False
        Definition.AG_CHAIN.enable_light_time_delay = False
        Definition.AG_CHAIN.time_convergence = 0.001
        Definition.AG_CHAIN.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)
        (ChainUserSpecifiedTimePeriod(Definition.AG_CHAIN.time_period)).time_interval.set_explicit_interval(
            "1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00"
        )
        Definition.AG_CHAIN.compute_access()

        # 7 - Constellations
        AG_CON: "Constellation" = Constellation(TestBase.Application.current_scenario.children["OnlyLeo28"])
        Assert.assertIsNotNone(AG_CON)
        AG_CON.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.ANY_OF)
        AG_CON.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.ANY_OF)
        Assert.assertEqual(ConstellationConstraintRestrictionType.ANY_OF, AG_CON.constraints.from_restriction_type)
        Assert.assertEqual(ConstellationConstraintRestrictionType.ANY_OF, AG_CON.constraints.to_restriction_type)

        AG_CON = None
        AG_CON = Constellation(TestBase.Application.current_scenario.children["Leos"])
        Assert.assertIsNotNone(AG_CON)
        AG_CON.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.ANY_OF)
        AG_CON.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.ANY_OF)
        Assert.assertEqual(ConstellationConstraintRestrictionType.ANY_OF, AG_CON.constraints.from_restriction_type)
        Assert.assertEqual(ConstellationConstraintRestrictionType.ANY_OF, AG_CON.constraints.to_restriction_type)

        AG_CON = None
        AG_CON = Constellation(TestBase.Application.current_scenario.children["Meos"])
        Assert.assertIsNotNone(AG_CON)
        AG_CON.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.ANY_OF)
        AG_CON.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.ANY_OF)
        Assert.assertEqual(ConstellationConstraintRestrictionType.ANY_OF, AG_CON.constraints.from_restriction_type)
        Assert.assertEqual(ConstellationConstraintRestrictionType.ANY_OF, AG_CON.constraints.to_restriction_type)

        # Section 2: Test capabilities for previous to STK 8.1
        # Asset: Single Object
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorth"])
        Assert.assertIsNotNone(Definition.AG_COV)
        Definition.AG_COV.compute_accesses()

        oComparator6.TakeOMSnapshot(TestBase.Application)

        # Asset: Constellation of 1 object
        Definition.AG_COV.asset_list.remove("Satellite/Leo_28")
        assetListElement: "CoverageAssetListElement" = Definition.AG_COV.asset_list.add("Constellation/OnlyLeo28")
        assetListElement.asset_status = CoverageAssetStatus.ACTIVE
        Definition.AG_COV.compute_accesses()

        oComparator6.TakeOMSnapshot(TestBase.Application)

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-OnlyLeo28"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)

        Definition.AG_CHAIN.compute_access()

        oComparator7.TakeOMSnapshot(TestBase.Application)

        Definition.AG_CHAIN.clear_access()

        # Asset: Constellation of 3 objects (AnyOf)
        Definition.AG_COV.asset_list.remove_all()
        Definition.AG_COV.asset_list.add("Constellation/Leos")
        Definition.AG_COV.compute_accesses()

        oComparator6.TakeOMSnapshot(TestBase.Application)

        Definition.AG_COV.clear_accesses()
        TestBase.Application.execute_command("Chains */Chain/MidNorth-to-Leos Compute")

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Leos"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)
        Definition.AG_CHAIN.compute_access()

        oComparator8.TakeOMSnapshot(TestBase.Application)

        Definition.AG_CHAIN.clear_access()
        Definition.AG_COV.asset_list.remove_all()

        # Asset: Chain of single objects
        Definition.AG_COV.asset_list.add("Chain/MidNorth-to-Leo28")
        Definition.AG_COV.compute_accesses()

        oComparator6.TakeOMSnapshot(TestBase.Application)

        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.asset_list.remove("Chain/MidNorth-to-Leo28")

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Leo28"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)

        Definition.AG_CHAIN.compute_access()

        oComparator9.TakeOMSnapshot(TestBase.Application)

        Definition.AG_CHAIN.clear_access()

        # Asset: Chain ending in Constellation
        Definition.AG_COV.asset_list.remove_all()
        Definition.AG_COV.asset_list.add("Chain/MidNorth-to-Leos")
        Definition.AG_COV.compute_accesses()

        oComparator6.TakeOMSnapshot(TestBase.Application)

        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.asset_list.remove_all()

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Leos"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)

        Definition.AG_CHAIN.compute_access()

        oComparator8.TakeOMSnapshot(TestBase.Application)

        Definition.AG_CHAIN.clear_access()

        # Section 3: Test NAsset capability of coverage
        # NAsset: AtLeast 2
        Definition.AG_COV = None
        Definition.AG_COV = CoverageDefinition(TestBase.Application.current_scenario.children["MidNorth-Meos"])
        Assert.assertIsNotNone(Definition.AG_COV)
        Definition.AG_COV.compute_accesses()
        Definition.AG_FOM = None
        Definition.AG_FOM = FigureOfMerit(
            TestBase.Application.current_scenario.children["MidNorth-Meos"].children["NAsset"]
        )
        Assert.assertIsNotNone(Definition.AG_FOM)

        Definition.AG_FOM.definition.satisfaction.satisfaction_type = FigureOfMeritSatisfactionType.AT_LEAST
        Definition.AG_FOM.definition.satisfaction.satisfaction_threshold = 2

        oComparator10.TakeOMSnapshot(TestBase.Application)

        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.advanced.n_assets_satisfaction_type = CoverageSatisfactionType.AT_LEAST
        Definition.AG_COV.advanced.n_assets_satisfaction_threshold = 2
        Definition.AG_COV.compute_accesses()

        oComparator11.TakeOMSnapshot(TestBase.Application)

        Definition.AG_COV.clear_accesses()
        Definition.AG_COV.compute_accesses()

        oComparator11.TakeOMSnapshot(TestBase.Application)
        oComparator10.TakeOMSnapshot(TestBase.Application)

        Definition.AG_CHAIN = None
        Definition.AG_CHAIN = Chain(TestBase.Application.current_scenario.children["MidNorth-to-Meos"])
        Assert.assertIsNotNone(Definition.AG_CHAIN)

        AG_CON = None
        AG_CON = Constellation(TestBase.Application.current_scenario.children["Meos"])
        Assert.assertIsNotNone(AG_CON)
        AG_CON.constraints.set_from_restriction_type(ConstellationConstraintRestrictionType.AT_LEAST_N)
        AG_CON.constraints.set_to_restriction_type(ConstellationConstraintRestrictionType.AT_LEAST_N)
        (ConstellationConstraintObjectRestriction(AG_CON.constraints.from_restriction)).number_of_objects = 2
        (ConstellationConstraintObjectRestriction(AG_CON.constraints.to_restriction)).number_of_objects = 2

        Definition.AG_CHAIN.compute_access()

        oComparator12.TakeOMSnapshot(TestBase.Application)

        Definition.AG_CHAIN.clear_access()

        # Compare results
        oComparator1.CompareReportSnapshots()
        oComparator2.CompareReportSnapshots()
        oComparator3.CompareReportSnapshots()
        oComparator4.CompareReportSnapshots()
        oComparator5.CompareReportSnapshots()
        oComparator6.CompareReportSnapshots()
        oComparator7.CompareReportSnapshots()
        oComparator8.CompareReportSnapshots()
        oComparator9.CompareReportSnapshots()
        oComparator10.CompareReportSnapshots()
        oComparator11.CompareReportSnapshots()
        oComparator12.CompareReportSnapshots()

    # endregion
    # endregion

    # region FigureOfMerit
    def test_FigureOfMerit(self):
        # Report initialization
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("FOMTest", "FOMTest.sc"))
        Definition.AG_COV = CoverageDefinition(
            TestBase.Application.current_scenario.children.get_elements(STKObjectType.COVERAGE_DEFINITION)["FOMTest"]
        )
        Definition.AG_FOM = FigureOfMerit(
            (IStkObject(Definition.AG_COV)).children.new(STKObjectType.FIGURE_OF_MERIT, "FOMTest")
        )
        Definition.AG_FOM2 = FigureOfMerit(
            TestBase.Application.current_scenario.children["FOMTestDOP"].children["FOMTestDOP"]
        )
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Definition.AG_FOM, IStkObject), '"Grid Stats"')
        CompareUtility.AddReport(clr.CastAs(Definition.AG_FOM, IStkObject), '"GI Point Static Value"')
        CompareUtility.AddReport(clr.CastAs(Definition.AG_FOM, IStkObject), '"Value By Grid Point"')
        CompareUtility.AddReport(clr.CastAs(Definition.AG_FOM, IStkObject), '"Percent Satisfied"')
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_FOM, IStkObject),
            '"Grid Stats Over Time" "1 Jan 2001 02:00:00.00" "1 Jan 2001 04:00:00.00" 300.0',
        )
        CompareUtility.AddReport(
            clr.CastAs(Definition.AG_FOM, IStkObject),
            '"Satisfied By Time" "1 Jan 2001 00:00:00.00" "1 Jan 2001 12:00:00.00" 300.0',
        )
        CompareUtility.AddReport(clr.CastAs(Definition.AG_FOM2, IStkObject), '"GI Point Static Value"')

        # Simple
        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition Simple"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.SIMPLE_COVERAGE)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NAsset Minimum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.N_ASSET_COVERAGE)
        oDefCompute: "IFigureOfMeritDefinitionCompute" = IFigureOfMeritDefinitionCompute(Definition.AG_FOM.definition)
        oDefCompute.set_compute_type(FigureOfMeritCompute.MINIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NAsset Maximum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NAsset Average"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.AVERAGE)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NAsset PercentAbove 90.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PERCENT_ABOVE)
        dataPercentLevel: "FigureOfMeritDefinitionDataPercentLevel" = FigureOfMeritDefinitionDataPercentLevel(
            oDefCompute.compute
        )
        dataPercentLevel.percent_level = 90.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # CoverageTime

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime Percent"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.COVERAGE_TIME)
        oDefCompute = IFigureOfMeritDefinitionCompute(Definition.AG_FOM.definition)
        oDefCompute.set_compute_type(FigureOfMeritCompute.PERCENT)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime Total"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.TOTAL)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime PerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime PercentPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PERCENT_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime MinPercentPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MINIMUM_PERCENT_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime MaxPercentPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MAXIMUM_PERCENT_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime MinPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MINIMUM_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime MaxPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MAXIMUM_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime PercentPerDayStdDev"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PERCENT_PER_DAY_STANDARD_DEVIATION)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime PerDayStdDev"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PER_DAY_STANDARD_DEVIATION)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime PercentTimeAbove 2"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PERCENT_TIME_ABOVE)
        oDataAssets: "FigureOfMeritDefinitionDataMinimumNumberOfAssets" = clr.CastAs(
            oDefCompute.compute, FigureOfMeritDefinitionDataMinimumNumberOfAssets
        )
        oDataAssets.minimum_assets = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition CoverageTime TotalTimeAbove 2"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.TOTAL_TIME_ABOVE)
        oDataAssets = clr.CastAs(oDefCompute.compute, FigureOfMeritDefinitionDataMinimumNumberOfAssets)
        oDataAssets.minimum_assets = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # RevisitTime

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime Minimum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.REVISIT_TIME)
        oDefRevisit: "FigureOfMeritDefinitionRevisitTime" = FigureOfMeritDefinitionRevisitTime(
            Definition.AG_FOM.definition
        )
        oDefRevisit.set_compute_type(FigureOfMeritCompute.MINIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime Maximum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefRevisit.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime Average"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefRevisit.set_compute_type(FigureOfMeritCompute.AVERAGE)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime StdDev"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefRevisit.set_compute_type(FigureOfMeritCompute.STD_DEVIATION)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime PercentBelow 90.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefRevisit.set_compute_type(FigureOfMeritCompute.PERCENT_BELOW)
        oDataPercent: "FigureOfMeritDefinitionDataPercentLevel" = clr.CastAs(
            oDefRevisit.compute, FigureOfMeritDefinitionDataPercentLevel
        )
        oDataPercent.percent_level = 90.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime PercentBelowGapsOnly 90.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefRevisit.set_compute_type(FigureOfMeritCompute.PERCENT_BELOW_GAPS_ONLY)
        oDataPercent = clr.CastAs(oDefRevisit.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 90.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime PercentNumBelow 90.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefRevisit.set_compute_type(FigureOfMeritCompute.NUMBER_PERCENT_BELOW)
        oDataPercent = clr.CastAs(oDefCompute.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 90.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime Maximum 2"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefRevisit.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        oDefRevisit.minimum_assets = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition RevisitTime PercentBelow 90.0 2"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefRevisit.set_compute_type(FigureOfMeritCompute.PERCENT_BELOW)
        oDataPercent = clr.CastAs(oDefRevisit.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 90.0
        oDefRevisit.minimum_assets = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # AccessDuration

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessDuration Minimum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.ACCESS_DURATION)
        oDefCompute = IFigureOfMeritDefinitionCompute(Definition.AG_FOM.definition)
        oDefCompute.set_compute_type(FigureOfMeritCompute.MINIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessDuration Maximum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessDuration Average"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.AVERAGE)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessDuration StdDev"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.STD_DEVIATION)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessDuration PercentAbove 80.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PERCENT_ABOVE)
        oDataPercent = clr.CastAs(oDefCompute.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 80.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # NumberOfAccesses

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfAccesses Total"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.NUMBER_OF_ACCESSES)
        oDefCompute = IFigureOfMeritDefinitionCompute(Definition.AG_FOM.definition)
        oDefCompute.set_compute_type(FigureOfMeritCompute.TOTAL)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfAccesses MinPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MINIMUM_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfAccesses MaxPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MAXIMUM_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfAccesses AvgPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.AVERAGE_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfAccesses InSpan 60 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.IN_SPAN)
        oDataMinMax: "FigureOfMeritDefinitionDataMinimumMaximum" = clr.CastAs(
            oDefCompute.compute, FigureOfMeritDefinitionDataMinimumMaximum
        )
        oDataMinMax.minimum_value = 60
        oDataMinMax.maximum_value = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfAccesses InSpanPerDay 60 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.IN_SPAN_PER_DAY)
        oDataMinMax = clr.CastAs(oDefCompute.compute, FigureOfMeritDefinitionDataMinimumMaximum)
        oDataMinMax.minimum_value = 60
        oDataMinMax.maximum_value = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # AccessSeparation

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessSeparation 360 3600"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.ACCESS_SEPARATION)
        oSeparation: "FigureOfMeritDefinitionAccessSeparation" = clr.CastAs(
            Definition.AG_FOM.definition, FigureOfMeritDefinitionAccessSeparation
        )
        oSeparation.minimum_maximum_data.minimum_value = 360
        oSeparation.minimum_maximum_data.maximum_value = 3600
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # NumberOfGaps

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfGaps Total"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.NUMBER_OF_GAPS)
        oDefCompute = IFigureOfMeritDefinitionCompute(Definition.AG_FOM.definition)
        oDefCompute.set_compute_type(FigureOfMeritCompute.TOTAL)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfGaps MinPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MINIMUM_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfGaps MaxPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.MAXIMUM_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfGaps AvgPerDay"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.AVERAGE_PER_DAY)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfGaps InSpan 60 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.IN_SPAN)
        oDataMinMax = clr.CastAs(oDefCompute.compute, FigureOfMeritDefinitionDataMinimumMaximum)
        oDataMinMax.minimum_value = 60
        oDataMinMax.maximum_value = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NumberOfGaps InSpanPerDay 60 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.IN_SPAN_PER_DAY)
        oDataMinMax = clr.CastAs(oDefCompute.compute, FigureOfMeritDefinitionDataMinimumMaximum)
        oDataMinMax.minimum_value = 60
        oDataMinMax.maximum_value = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # TimeAverageGap

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition TimeAverageGap"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.TIME_AVERAGE_GAP)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # ResponseTime

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition ResponseTime Minimum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.RESPONSE_TIME)
        oDefResponse: "IFigureOfMeritDefinitionResponseTime" = IFigureOfMeritDefinitionResponseTime(
            Definition.AG_FOM.definition
        )
        oDefResponse.set_compute_type(FigureOfMeritCompute.MINIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition ResponseTime Maximum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefResponse.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition ResponseTime Average"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefResponse.set_compute_type(FigureOfMeritCompute.AVERAGE)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition ResponseTime PercentBelow 85.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PERCENT_BELOW)
        oDataPercent = clr.CastAs(oDefCompute.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 85.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition ResponseTime PercentBelowGapsOnly 85.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefCompute.set_compute_type(FigureOfMeritCompute.PERCENT_BELOW_GAPS_ONLY)
        oDataPercent = clr.CastAs(oDefCompute.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 85.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition ResponseTime Maximum 2"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefResponse.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        oDefResponse.minimum_assets = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition ResponseTime PercentBelowGapsOnly 85.0 2"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefResponse.set_compute_type(FigureOfMeritCompute.PERCENT_BELOW_GAPS_ONLY)
        oDataPercent = clr.CastAs(oDefResponse.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 85.0
        oDefResponse.minimum_assets = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # AccessConstraint - Altitude

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessConstraint Altitude Minimum Minimum 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_access_constraint_definition(FigureOfMeritConstraintName.ALTITUDE)
        oDefAccessCnstr: "FigureOfMeritDefinitionAccessConstraint" = FigureOfMeritDefinitionAccessConstraint(
            Definition.AG_FOM.definition
        )
        oDefAccessCnstr.set_compute_type(FigureOfMeritCompute.MINIMUM)
        oDefAccessCnstr.across_assets = FigureOfMeritAcrossAssets.MINIMUM
        oDefAccessCnstr.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessConstraint Altitude Minimum Maximum 60"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefAccessCnstr.across_assets = FigureOfMeritAcrossAssets.MAXIMUM
        oDefAccessCnstr.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessConstraint Altitude Minimum Average 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefAccessCnstr.across_assets = FigureOfMeritAcrossAssets.AVERAGE
        oDefAccessCnstr.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition AccessConstraint Altitude Maximum Minimum 60"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefAccessCnstr.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        oDefAccessCnstr.across_assets = FigureOfMeritAcrossAssets.MINIMUM
        oDefAccessCnstr.time_step = 60
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # DOP - Minimum

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum GDOP OverDetermined 360 "
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM2.set_definition_type(FigureOfMeritDefinitionType.DILUTION_OF_PRECISION)
        oDefDOP: "IFigureOfMeritDefinitionDilutionOfPrecision" = IFigureOfMeritDefinitionDilutionOfPrecision(
            Definition.AG_FOM2.definition
        )
        oDefDOP.set_compute_type(FigureOfMeritCompute.MINIMUM)
        oDefDOP.set_method(FigureOfMeritMethod.GDOP)
        oDefDOP.set_type(FigureOfMeritNavigationComputeType.OVER_DETERMINED)
        oDefDOP.time_step = 360
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum GDOP Best4 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_4)
        oDefDOP.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum GDOP BestN 5 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_N)
        oBestN: "FigureOfMeritDefinitionDataBestN" = clr.CastAs(oDefDOP.type_data, FigureOfMeritDefinitionDataBestN)
        oBestN.best_n = 5
        oDefDOP.time_step = 360
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum PDOP OverDetermined 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_method(FigureOfMeritMethod.PDOP)
        oDefDOP.set_type(FigureOfMeritNavigationComputeType.OVER_DETERMINED)
        oDefDOP.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum PDOP Best4 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_4)
        oDefDOP.time_step = 360
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum PDOP BestN 6 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_N)
        oBestN = clr.CastAs(oDefDOP.type_data, FigureOfMeritDefinitionDataBestN)
        oBestN.best_n = 6
        oDefDOP.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum HDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_method(FigureOfMeritMethod.HDOP)
        oDefDOP.set_type(FigureOfMeritNavigationComputeType.OVER_DETERMINED)
        oDefDOP.time_step = 360
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum HDOP Best4 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_4)
        oDefDOP.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum HDOP BestN 5 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_N)
        oBestN = clr.CastAs(oDefDOP.type_data, FigureOfMeritDefinitionDataBestN)
        oBestN.best_n = 5
        oDefDOP.time_step = 360
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum VDOP OverDetermined 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_method(FigureOfMeritMethod.VDOP)
        oDefDOP.set_type(FigureOfMeritNavigationComputeType.OVER_DETERMINED)
        oDefDOP.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum VDOP Best4 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_4)
        oDefDOP.time_step = 360
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum VDOP BestN 6 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_N)
        oBestN = clr.CastAs(oDefDOP.type_data, FigureOfMeritDefinitionDataBestN)
        oBestN.best_n = 6
        oDefDOP.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum TDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_method(FigureOfMeritMethod.TDOP)
        oDefDOP.set_type(FigureOfMeritNavigationComputeType.OVER_DETERMINED)
        oDefDOP.time_step = 360
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum TDOP Best4 120"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_4)
        oDefDOP.time_step = 120
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum TDOP BestN 5 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_N)
        oBestN = clr.CastAs(oDefDOP.type_data, FigureOfMeritDefinitionDataBestN)
        oBestN.best_n = 5
        oDefDOP.time_step = 360
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP PercentBelow 95 TDOP BestN 99 300"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oDefDOP.set_compute_type(FigureOfMeritCompute.PERCENT_BELOW)
        oDataPercent = clr.CastAs(oDefDOP.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 95
        oDefDOP.set_type(FigureOfMeritNavigationComputeType.BEST_N)
        oBestN = clr.CastAs(oDefDOP.type_data, FigureOfMeritDefinitionDataBestN)
        oBestN.best_n = 99
        oDefDOP.time_step = 300
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Satisfaction

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition ResponseTime PercentBelow 90.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.RESPONSE_TIME)
        oDefResponse = IFigureOfMeritDefinitionResponseTime(Definition.AG_FOM.definition)
        oDefResponse.set_compute_type(FigureOfMeritCompute.PERCENT_BELOW)
        oDataPercent = clr.CastAs(oDefResponse.compute, FigureOfMeritDefinitionDataPercentLevel)
        oDataPercent.percent_level = 90
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction On"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction: "FigureOfMeritSatisfaction" = oDefResponse.satisfaction
        oSatisfaction.enable_satisfaction = True
        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.GREATER_THAN
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction GreaterThan 5.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.GREATER_THAN
        oSatisfaction.satisfaction_threshold = 5.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction AtLeast 2.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.AT_LEAST
        oSatisfaction.satisfaction_threshold = 2.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction Equal 3.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.EQUAL_TO
        oSatisfaction.satisfaction_threshold = 3.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction AtMost 5.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.AT_MOST
        oSatisfaction.satisfaction_threshold = 5.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction LessThan 6.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.LESS_THAN
        oSatisfaction.satisfaction_threshold = 6.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction Off"
        )
        # CompareUtility.TakeConnectSnapshot(Application);

        oSatisfaction.enable_satisfaction = False
        # CompareUtility.TakeOMSnapshot(Application);           //Connect reports extra 0.0 % Satisfied data in report.

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Definition NAsset Maximum"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.N_ASSET_COVERAGE)
        oDefCompute = IFigureOfMeritDefinitionCompute(Definition.AG_FOM.definition)
        oDefCompute.set_compute_type(FigureOfMeritCompute.MAXIMUM)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction On"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.enable_satisfaction = True
        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.GREATER_THAN
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction GreaterThan 5.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.GREATER_THAN
        oSatisfaction.satisfaction_threshold = 5
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction AtLeast 2.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.AT_LEAST
        oSatisfaction.satisfaction_threshold = 2
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction Equal 3.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.EQUAL_TO
        oSatisfaction.satisfaction_threshold = 3
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction AtMost 5.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.AT_MOST
        oSatisfaction.satisfaction_threshold = 5
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTest/FigureOfMerit/FOMTest FomDefine Satisfaction LessThan 6.0"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        oSatisfaction.satisfaction_type = FigureOfMeritSatisfactionType.LESS_THAN
        oSatisfaction.satisfaction_threshold = 6
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        CompareUtility.CompareReportSnapshots()
        Definition.InitHelper()

    def test_FigureOfMerit_DOP(self):
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("FOMTest", "FOMTest.sc"))

        Definition.AG_FOM2 = FigureOfMerit(
            TestBase.Application.current_scenario.children["FOMTestDOP"].children["FOMTestDOP"]
        )
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Definition.AG_FOM2, IStkObject), '"Grid Stats"')

        Definition.AG_FOM2.set_definition_type(FigureOfMeritDefinitionType.DILUTION_OF_PRECISION)
        dop: "IFigureOfMeritDefinitionDilutionOfPrecision" = IFigureOfMeritDefinitionDilutionOfPrecision(
            Definition.AG_FOM2.definition
        )
        dop.set_type(FigureOfMeritNavigationComputeType.OVER_DETERMINED)
        dop.time_step = 360

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum EDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.EDOP)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum EDOP_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.EDOP3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum GDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.GDOP)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum HDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.HDOP)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum HDOP_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.HDOP3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum NDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.NDOP)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum NDOP_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.NDOP3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum PDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.PDOP)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum PDOP_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.PDOP3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum TDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.TDOP)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum VDOP OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.VDOP)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition DOP Minimum VDOP_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        dop.set_method(FigureOfMeritMethod.VDOP3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        CompareUtility.CompareReportSnapshots()
        Definition.InitHelper()

    def test_FigureOfMerit_NavAccuracy(self):
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("FOMTest", "FOMTest.sc"))

        Definition.AG_FOM2 = FigureOfMerit(
            TestBase.Application.current_scenario.children["FOMTestDOP"].children["FOMTestDOP"]
        )
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Definition.AG_FOM2, IStkObject), '"Grid Stats"')

        Definition.AG_FOM2.set_definition_type(FigureOfMeritDefinitionType.NAVIGATION_ACCURACY)
        navAccuracy: "FigureOfMeritDefinitionNavigationAccuracy" = FigureOfMeritDefinitionNavigationAccuracy(
            Definition.AG_FOM2.definition
        )
        navAccuracy.set_type(FigureOfMeritNavigationComputeType.OVER_DETERMINED)
        navAccuracy.time_step = 360

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum EACC OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.EACC)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum EACC_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.EACC3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum GACC OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.GACC)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum HACC OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.HACC)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum HACC_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.HACC3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum NACC OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.NACC)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum NACC_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.NACC3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum PACC OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.PACC)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum PACC_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.PACC3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum TACC OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.TACC)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum VACC OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.VACC)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            "Cov */CoverageDefinition/FOMTestDOP/FigureOfMerit/FOMTestDOP FomDefine Definition NAVACCURACY Minimum VACC_3 OverDetermined 360"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        navAccuracy.set_method(FigureOfMeritMethod.VACC3)
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        CompareUtility.CompareReportSnapshots()
        Definition.InitHelper()

    # endregion

    # region LineTarget
    def test_LineTarget(self):
        self.AccessLineTarget()
        self.AccessLineTargetDifferentCBs()
        self.AccessLineTargetMultipleObjects()
        Definition.InitHelper()

    # region AccessLineTarget
    def AccessLineTarget(self):
        # Load scenario
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("LineTarget", "LineTarget.sc"))

        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport3(
            'GetReport */Aircraft/Aircraft1/Sensor/SensorAirComplex "Access Detailed" */LineTarget/LineTarget1'
        )
        CompareUtility.AddReport3('GetReport */Satellite/Satellite1 "Access Detailed" */LineTarget/LineTarget1')
        CompareUtility.AddReport3(
            'GetReport */Satellite/Satellite1/Sensor/SensorSatLineTargeted "Access Detailed" */LineTarget/LineTarget1'
        )

        # Report accesses to line target
        TestBase.Application.execute_command(
            "Define */Aircraft/Aircraft1/Sensor/SensorAirComplex Conical 30.0 40.0 20.0 20.1"
        )
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_SN1 = None
        Definition.AG_SN1 = Sensor(
            TestBase.Application.current_scenario.children["Aircraft1"].children["SensorAirComplex"]
        )
        Definition.AG_SN1.set_pattern_type(SensorPattern.COMPLEX_CONIC)
        oComplexConic: "SensorComplexConicPattern" = SensorComplexConicPattern(Definition.AG_SN1.pattern)
        oComplexConic.inner_cone_half_angle = 30.0
        oComplexConic.outer_cone_half_angle = 40.0
        oComplexConic.maximum_clock_angle = 20.1
        oComplexConic.minimum_clock_angle = 20.0
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        # Test "Access to Whole Object" constraint
        TestBase.Application.execute_command("SetAccessOption */LineTarget/LineTarget1 Whole")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_LT = None
        Definition.AG_LT = LineTarget(TestBase.Application.current_scenario.children["LineTarget1"])
        Definition.AG_LT.allow_object_access = True
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetAccessOption */LineTarget/LineTarget1 Any")
        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        Definition.AG_LT.allow_object_access = False
        CompareUtility.TakeOMSnapshot(TestBase.Application)

        CompareUtility.CompareReportSnapshots()
        Definition.AG_SN1 = None
        Definition.AG_LT = None

    # endregion

    # region AccessLineTargetDifferentCBs
    # Test Access between Sensors and LineTargets with different central bodies.
    def AccessLineTargetDifferentCBs(self):
        # Load scenario
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(
            TestBase.GetScenarioFile("Bug_Access_SensorFOV-AT-LT_24088", "Bug_Access_SensorFOV-AT-LT_24088.sc")
        )

        CompareUtility = ReportComparison(self.Units)

        CompareUtility.AddReport3(
            'GetReport */Facility/MarsFac/Sensor/MarsFacSen "Access Configuration" */LineTarget/NewJersey_LT'
        )
        CompareUtility.AddReport3(
            'GetReport */Facility/EarthFac/Sensor/EarthFacSen "Access Configuration" */LineTarget/Mars_LT'
        )
        CompareUtility.AddReport3(
            'GetReport */Satellite/MarsSat_EarthEphem/Sensor/MarsSatSen "Access Configuration" */LineTarget/Mars_LT'
        )
        CompareUtility.AddReport3('GetReport */Facility/MarsFac/Sensor/MarsFacSen "Access" */LineTarget/NewJersey_LT')
        CompareUtility.AddReport3('GetReport */Facility/EarthFac/Sensor/EarthFacSen "Access" */LineTarget/Mars_LT')
        CompareUtility.AddReport3(
            'GetReport */Satellite/MarsSat_EarthEphem/Sensor/MarsSatSen "Access" */LineTarget/Mars_LT'
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region AccessLineTargetMultipleObjects
    # Test Access computations for Sensors targeting multiple objects.
    def AccessLineTargetMultipleObjects(self):
        # Load scenario
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(
            TestBase.GetScenarioFile("Bug_Access_TgtSensor_23617", "Bug_Access_TgtSensor_23617.sc")
        )

        CompareUtility = ReportComparison(self.Units)

        CompareUtility.AddReport3(
            'GetReport */Satellite/Satellite1/Sensor/Sensor1 "Access Configuration" */LineTarget/LineTarget1'
        )
        CompareUtility.AddReport3('GetReport */Satellite/Satellite1/Sensor/Sensor1 "Access" */LineTarget/LineTarget1')
        CompareUtility.AddReport3(
            'GetReport */Satellite/Satellite1/Sensor/Sensor1 "Access Detailed" */LineTarget/LineTarget1'
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)
        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # endregion

    # region MTO
    # [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
    def test_MTO(self):
        self.Visibility()
        self.Visibility2()
        (
            IAnimation(TestBase.Application)
        ).current_time = 0  # Set back to original because this gets changed in NoGfx case.
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("MTO_Integrity", "MTO_Test.sc"))
        self.Range()
        self.Position()
        self.FieldOfView()
        TestBase.Application.close_scenario()
        Definition.InitHelper()

    # region FieldOfView

    class FOVValues:
        def __init__(self, *args, **kwargs):
            self._TrackId = None
            self._InFOV = None

        @property
        def TrackId(self):
            return self._TrackId

        @TrackId.setter
        def TrackId(self, value):
            self._TrackId = value

        @property
        def InFOV(self):
            return self._InFOV

        @InFOV.setter
        def InFOV(self, value):
            self._InFOV = value

        def __eq__(self, obj: typing.Any):
            if Object.ReferenceEquals(None, obj):
                return False
            if Object.ReferenceEquals(self, obj):
                return True
            if type(obj) != type(self):
                return False
            return self.Equals(obj)

        def GetHashCode(self):
            return ((self.TrackId * 397)) ^ self.InFOV

        def Equals(self, other):
            if Object.ReferenceEquals(None, other):
                return False
            if Object.ReferenceEquals(self, other):
                return True
            return (self.TrackId == other.TrackId) and (self.InFOV == other.InFOV)

    def FieldOfView(self):
        MasterMap = []
        geo: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["Geo1"], Satellite)
        sensor: "Sensor" = clr.CastAs(
            TestBase.Application.current_scenario.children["Geo1"].children["A_Sensor"], Sensor
        )
        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["A_MTO"], MTO)
        fov: "MTOAnalysisFieldOfView" = mto.analysis.field_of_view
        fov.sensor = "Satellite/Geo1/Sensor/A_Sensor"
        date: "Date" = TestBase.Application.conversion_utility.new_date(
            "EpSec", Double.ToString((IAnimation(TestBase.Application)).current_time)
        )

        results: "ExecuteCommandResult" = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor"
        )
        isInFOV: bool = fov.is_any_track_in_field_of_view(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        results = TestBase.Application.execute_command(
            'FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Time "1 Jul 2005 12:00:00.000"'
        )
        isInFOV = fov.is_any_track_in_field_of_view("1 Jul 2005 12:00:00.000")
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        results = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Mode Any"
        )
        isInFOV = fov.is_any_track_in_field_of_view(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        results = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Mode All"
        )
        isInFOV = fov.are_all_tracks_in_field_of_view(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        self.MTOFOVHelper(MasterMap, "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Mode Each")
        self.CompareFOVResults(MasterMap, fov.compute_all_tracks(MTOVisibilityMode.EACH, date.format("UTCG")))

        self.MTOFOVHelper(
            MasterMap, "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Mode EachVisible"
        )
        self.CompareFOVResults(MasterMap, fov.compute_all_tracks(MTOVisibilityMode.EACH_VISIBLE, date.format("UTCG")))

        self.MTOFOVHelper(
            MasterMap, "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Mode EachNotVisible"
        )
        self.CompareFOVResults(
            MasterMap, fov.compute_all_tracks(MTOVisibilityMode.EACH_NOT_VISIBLE, date.format("UTCG"))
        )

        results = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Track 2"
        )
        isInFOV = fov.is_track_in_field_of_view(2, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        results = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Track 3"
        )
        isInFOV = fov.is_track_in_field_of_view(3, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        tracks = []
        tracks.append(1)
        tracks.append(2)
        tracks.append(3)
        tracks.append(4)
        refTracks = tracks

        results = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Tracks 1 2 3 4"
        )
        isInFOV = fov.are_tracks_in_field_of_view(MTOTrackEvaluationType.ANY, refTracks, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        results = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Entirety All"
        )
        fov.entirety = MTOEntirety.ALL
        isInFOV = fov.is_any_track_in_field_of_view(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        results = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Entirety Partial"
        )
        fov.entirety = MTOEntirety.PARTIAL
        isInFOV = fov.is_any_track_in_field_of_view(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        results = TestBase.Application.execute_command(
            'FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Time "1 Jul 2005 12:00:00.000" Mode Any Track 1 Track 2 Track 3 Track 4 Entirety All'
        )
        fov.entirety = MTOEntirety.ALL
        isInFOV = fov.are_tracks_in_field_of_view(MTOTrackEvaluationType.ANY, refTracks, "1 Jul 2005 12:00:00.000")
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        results = TestBase.Application.execute_command(
            "FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Entirety Partial Mode All Tracks 1 2 4 3"
        )
        fov.entirety = MTOEntirety.PARTIAL
        isInFOV = fov.are_tracks_in_field_of_view(MTOTrackEvaluationType.ALL, refTracks, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

        tracks.clear()
        tracks.append(1)
        tracks.append(4)
        refTracks = tracks
        self.MTOFOVHelper(
            MasterMap,
            'FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Mode each Track 1 Track 4 Time "1 Jul 2005 12:00:00.000"',
        )
        self.CompareFOVResults(
            MasterMap, fov.compute_tracks(MTOVisibilityMode.EACH, refTracks, "1 Jul 2005 12:00:00.000")
        )

        results = TestBase.Application.execute_command(
            'FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Track 1 Track 4 Mode eachVisible Time "1 Jul 2005 23:00:00.000"'
        )
        Assert.assertEqual("No Visibility", results[0])
        noTracks = fov.compute_tracks(MTOVisibilityMode.EACH_VISIBLE, refTracks, "1 Jul 2005 23:00:00.000")
        Assert.assertEqual(0, Array.Length(noTracks))

        tracks.clear()
        tracks.append(1)
        tracks.append(2)
        tracks.append(3)
        tracks.append(4)
        tracks.append(4)
        tracks.append(3)
        tracks.append(2)
        tracks.append(1)
        refTracks = tracks
        results = TestBase.Application.execute_command(
            'FieldOfView_RM */MTO/A_MTO Object */Satellite/Geo1/Sensor/A_Sensor Time "1 Jul 2005 12:00:00.000" Mode Any Tracks 1 2 3 4 4 3 2 1'
        )
        isInFOV = fov.are_tracks_in_field_of_view(MTOTrackEvaluationType.ANY, refTracks, "1 Jul 2005 12:00:00.000")
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInFOV))

    def CompareFOVResults(self, MasterMap, tracksVisibility):
        Assert.assertEqual(len(MasterMap), len(tracksVisibility))

        i: int = 0
        while i < len(tracksVisibility):
            values = Definition.FOVValues()
            values.TrackId = Convert.ToInt32(tracksVisibility[i][0])
            values.InFOV = Convert.ToInt32(tracksVisibility[i][1])
            Assert.assertTrue((values in MasterMap))

            i += 1

    def MTOFOVHelper(self, dictionary, command: str):
        dictionary.clear()
        separator: "List[int]" = [","]
        result: "ExecuteCommandResult" = TestBase.Application.execute_command(command)
        value: str
        for value in result:
            values: "List[str]" = String.Split(value, separator)
            fov = Definition.FOVValues()
            fov.TrackId = Convert.ToInt32(values[0])
            fov.InFOV = Convert.ToInt32(values[1])
            dictionary.append(fov)

    # endregion

    class PositionValues:
        def __init__(self, *args, **kwargs):
            self._X = None
            self._Y = None
            self._Z = None
            self._Lat = None
            self._Lon = None
            self._Alt = None
            self._TrackId = None

        @property
        def X(self):
            return self._X

        @X.setter
        def X(self, value):
            self._X = value

        @property
        def Y(self):
            return self._Y

        @Y.setter
        def Y(self, value):
            self._Y = value

        @property
        def Z(self):
            return self._Z

        @Z.setter
        def Z(self, value):
            self._Z = value

        @property
        def Lat(self):
            return self._Lat

        @Lat.setter
        def Lat(self, value):
            self._Lat = value

        @property
        def Lon(self):
            return self._Lon

        @Lon.setter
        def Lon(self, value):
            self._Lon = value

        @property
        def Alt(self):
            return self._Alt

        @Alt.setter
        def Alt(self, value):
            self._Alt = value

        @property
        def TrackId(self):
            return self._TrackId

        @TrackId.setter
        def TrackId(self, value):
            self._TrackId = value

        def __eq__(self, obj: typing.Any):
            if Object.ReferenceEquals(None, obj):
                return False
            if Object.ReferenceEquals(self, obj):
                return True
            if type(obj) != type(self):
                return False
            return self.Equals(obj)

        def GetHashCode(self):
            hashCode: int = self.X.GetHashCode()
            hashCode = ((hashCode * 397)) ^ self.Y.GetHashCode()
            hashCode = ((hashCode * 397)) ^ self.Z.GetHashCode()
            hashCode = ((hashCode * 397)) ^ self.Lat.GetHashCode()
            hashCode = ((hashCode * 397)) ^ self.Lon.GetHashCode()
            hashCode = ((hashCode * 397)) ^ self.Alt.GetHashCode()
            hashCode = ((hashCode * 397)) ^ self.TrackId
            return hashCode

        def Equals(self, other):
            if Object.ReferenceEquals(None, other):
                return False
            if Object.ReferenceEquals(self, other):
                return True
            return (
                (
                    (
                        (((other.X == self.X) and (other.Y == self.Y)) and (other.Z == self.Z))
                        and (other.Lat == self.Lat)
                    )
                    and (other.Lon == self.Lon)
                )
                and (other.Alt == self.Alt)
            ) and (self.TrackId == other.TrackId)

    def Position(self):
        results: "ExecuteCommandResult" = TestBase.Application.execute_command("Position_RM */MTO/A_MTO")
        date: "Date" = TestBase.Application.conversion_utility.new_date(
            "EpSec", Double.ToString((IAnimation(TestBase.Application)).current_time)
        )
        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["A_MTO"], MTO)
        position: "MTOAnalysisPosition" = mto.analysis.position
        points: "MTOTrackPointCollection" = position.compute_all_tracks(date.format("UTCG"))

        x: float = 0
        y: float = 0
        z: float = 0

        separator: "List[int]" = [","]
        connect = []
        om = []

        i: int = 0
        while i < results.count:
            result: str = results[i]
            point: "MTOTrackPoint" = points[i]
            values: "List[str]" = String.Split(result, separator)
            pvConnect = Definition.PositionValues()
            pvConnect.TrackId = Convert.ToInt32(values[0])
            pvConnect.Lat = Math.Round(Convert.ToDouble(values[1]), 3)
            pvConnect.Lon = Math.Round(Convert.ToDouble(values[2]), 3)
            pvConnect.Alt = Math.Round(Convert.ToDouble(values[3]), 3)
            pvConnect.X = Math.Round(Convert.ToDouble(values[4]), 3)
            pvConnect.Y = Math.Round(Convert.ToDouble(values[5]), 3)
            pvConnect.Z = Math.Round(Convert.ToDouble(values[6]), 3)
            connect.append(pvConnect)

            pvOM = Definition.PositionValues()
            pvOM.TrackId = point.identifier
            pvOM.Lat = Math.Round(point.latitude, 3)
            pvOM.Lon = Math.Round(point.longitude, 3)
            pvOM.Alt = Math.Round(point.altitude, 3)
            (x, y, z) = point.position.query_cartesian()
            pvOM.X = Math.Round(x, 3)
            pvOM.Y = Math.Round(y, 3)
            pvOM.Z = Math.Round(z, 3)
            om.append(pvOM)

            i += 1

        Assert.assertEqual(len(connect), len(om))

        i: int = 0
        while i < len(om):
            Assert.assertTrue((om[i] in connect))

            i += 1

        results = TestBase.Application.execute_command("Position_RM */MTO/A_MTO Track 1 Track 2")
        tracks = []
        tracks.append(1)
        tracks.append(2)
        refTracks = tracks

        points = position.compute_tracks(refTracks, date.format("UTCG"))
        om.clear()
        connect.clear()

        i: int = 0
        while i < results.count:
            result: str = results[i]
            point: "MTOTrackPoint" = points[i]
            values: "List[str]" = String.Split(result, separator)
            pvConnect = Definition.PositionValues()
            pvConnect.TrackId = Convert.ToInt32(values[0])
            pvConnect.Lat = Math.Round(Convert.ToDouble(values[1]), 3)
            pvConnect.Lon = Math.Round(Convert.ToDouble(values[2]), 3)
            pvConnect.Alt = Math.Round(Convert.ToDouble(values[3]), 3)
            pvConnect.X = Math.Round(Convert.ToDouble(values[4]), 3)
            pvConnect.Y = Math.Round(Convert.ToDouble(values[5]), 3)
            pvConnect.Z = Math.Round(Convert.ToDouble(values[6]), 3)
            connect.append(pvConnect)

            pvOM = Definition.PositionValues()
            pvOM.TrackId = point.identifier
            pvOM.Lat = Math.Round(point.latitude, 3)
            pvOM.Lon = Math.Round(point.longitude, 3)
            pvOM.Alt = Math.Round(point.altitude, 3)
            (x, y, z) = point.position.query_cartesian()
            pvOM.X = Math.Round(x, 3)
            pvOM.Y = Math.Round(y, 3)
            pvOM.Z = Math.Round(z, 3)
            om.append(pvOM)

            i += 1

        Assert.assertEqual(len(connect), len(om))

        i: int = 0
        while i < len(om):
            Assert.assertTrue((om[i] in connect))

            i += 1

        results = TestBase.Application.execute_command("Position_RM */MTO/A_MTO Track 3")
        values1: "List[str]" = String.Split(results[0], separator)
        tp: "MTOTrackPoint" = position.compute_track(3, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(values1[0]), tp.identifier)
        Assert.assertEqual(Math.Round(Convert.ToDouble(values1[1]), 3), Math.Round(tp.latitude, 3))
        Assert.assertEqual(Math.Round(Convert.ToDouble(values1[2]), 3), Math.Round(tp.longitude, 3))
        Assert.assertEqual(Math.Round(Convert.ToDouble(values1[3]), 3), Math.Round(tp.altitude, 3))
        (x, y, z) = tp.position.query_cartesian()
        Assert.assertEqual(Math.Round(Convert.ToDouble(values1[4]), 3), Math.Round(x, 3))
        Assert.assertEqual(Math.Round(Convert.ToDouble(values1[5]), 3), Math.Round(y, 3))
        Assert.assertEqual(Math.Round(Convert.ToDouble(values1[6]), 3), Math.Round(z, 3))

    # region Range

    class RangeValues:
        def __init__(self, *args, **kwargs):
            self._TrackId = None
            self._InRange = None
            self._Range = None

        @property
        def TrackId(self):
            return self._TrackId

        @TrackId.setter
        def TrackId(self, value):
            self._TrackId = value

        @property
        def InRange(self):
            return self._InRange

        @InRange.setter
        def InRange(self, value):
            self._InRange = value

        @property
        def Range(self):
            return self._Range

        @Range.setter
        def Range(self, value):
            self._Range = value

        def __eq__(self, obj: typing.Any):
            if Object.ReferenceEquals(None, obj):
                return False
            if Object.ReferenceEquals(self, obj):
                return True
            if type(obj) != type(self):
                return False
            return self.Equals(obj)

        def GetHashCode(self):
            hashCode: int = self.TrackId
            hashCode = ((hashCode * 397)) ^ self.InRange
            hashCode = ((hashCode * 397)) ^ self.Range.GetHashCode()
            return hashCode

        def Equals(self, other):
            if Object.ReferenceEquals(None, other):
                return False
            if Object.ReferenceEquals(self, other):
                return True
            return ((self.TrackId == other.TrackId) and (self.InRange == other.InRange)) and (other.Range == self.Range)

    def Range(self):
        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "m")
        geo: "Satellite" = clr.CastAs(TestBase.Application.current_scenario.children["Geo1"], Satellite)
        sensor: "Sensor" = clr.CastAs(
            TestBase.Application.current_scenario.children["Geo1"].children["A_Sensor"], Sensor
        )
        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["A_MTO"], MTO)
        range: "MTOAnalysisRange" = mto.analysis.range
        range.object_path = "Satellite/Geo1"
        results: "ExecuteCommandResult" = TestBase.Application.execute_command(
            "Range_RM */MTO/A_MTO Object */Satellite/Geo1"
        )
        date: "Date" = TestBase.Application.conversion_utility.new_date(
            "EpSec", Double.ToString((IAnimation(TestBase.Application)).current_time)
        )
        isInRange: bool = range.is_any_track_in_range(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command(
            'Range_RM */MTO/A_MTO Object */Satellite/Geo1 Time "1 Jul 2005 12:00:00.000"'
        )
        isInRange = range.is_any_track_in_range("1 Jul 2005 12:00:00.000")
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Mode Any")
        isInRange = range.is_any_track_in_range(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Mode All")
        isInRange = range.are_all_tracks_in_range(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        MasterList = []

        self.MTORangeHelper(MasterList, "Range_RM */MTO/A_MTO Object */Satellite/Geo1 Mode Each")
        self.CompareRangeResults(MasterList, range.compute_all_ranges(MTORangeMode.EACH, date.format("UTCG")))

        self.MTORangeHelper(MasterList, "Range_RM */MTO/A_MTO Object */Satellite/Geo1 Mode EachInRange")
        self.CompareRangeResults(MasterList, range.compute_all_ranges(MTORangeMode.EACH_IN_RANGE, date.format("UTCG")))

        self.MTORangeHelper(MasterList, "Range_RM */MTO/A_MTO Object */Satellite/Geo1 Mode EachNotInRange")
        self.CompareRangeResults(
            MasterList, range.compute_all_ranges(MTORangeMode.EACH_NOT_IN_RANGE, date.format("UTCG"))
        )

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Track 2")
        isInRange = range.is_track_in_range(2, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Track 3")
        isInRange = range.is_track_in_range(3, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Tracks 1 2 3 4")
        tracks = [1, 2, 3, 4]

        isInRange = range.are_tracks_in_range(MTOTrackEvaluationType.ANY, tracks, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 LowerLimit 500.2")
        lowerLimit: float = range.lower_limit
        upperLimit: float = range.upper_limit
        range.lower_limit = 500.2
        isInRange = range.is_any_track_in_range(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 UpperLimit 500.2")
        range.lower_limit = lowerLimit
        range.upper_limit = 500.2
        isInRange = range.is_any_track_in_range(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        TestBase.Application.execute_command("Track */MTO/A_MTO Static On")
        range.upper_limit = upperLimit

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Entirety All")
        range.entirety = MTOEntirety.ALL
        isInRange = range.is_any_track_in_range(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Entirety Partial")
        range.entirety = MTOEntirety.PARTIAL

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Objectdata -1")
        range.object_data = -1
        isInRange = range.is_any_track_in_range(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Objectdata 0")
        range.object_data = 0
        isInRange = range.is_any_track_in_range(date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command("Range_RM */MTO/A_MTO Object */Satellite/Geo1 Objectdata 45")
        range.object_data = 45
        isInRange = range.is_any_track_in_range(date.format("UTCG"))

        results = TestBase.Application.execute_command(
            'Range_RM */MTO/A_MTO Object */Satellite/Geo1 Time "1 Jul 2005 12:00:00.000" Mode Any Track 1 Track 2 Track 3 Track 4 Entirety All LowerLimit 45 UpperLimit 900 Objectdata 3'
        )
        range.entirety = MTOEntirety.ALL
        range.lower_limit = 45
        range.upper_limit = 900
        range.object_data = 3
        isInRange = range.are_tracks_in_range(MTOTrackEvaluationType.ANY, tracks, "1 Jul 2005 12:00:00.000")
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        results = TestBase.Application.execute_command(
            "Range_RM */MTO/A_MTO Object */Satellite/Geo1 Entirety Partial Mode All Objectdata 5 Tracks 1 2 4 3"
        )
        range.entirety = MTOEntirety.PARTIAL
        range.object_data = 5
        range.upper_limit = upperLimit
        range.lower_limit = lowerLimit
        isInRange = range.are_tracks_in_range(MTOTrackEvaluationType.ALL, tracks, date.format("UTCG"))
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

        self.MTORangeHelper(
            MasterList,
            'Range_RM */MTO/A_MTO Object */Satellite/Geo1 Mode each Track 1 Track 4 Time "1 Jul 2005 12:00:00.000" UpperLimit 8004.34',
        )
        range.object_data = -1
        range.upper_limit = 8004.34
        tracks = [1, 4]

        self.CompareRangeResults(MasterList, range.compute_ranges(MTORangeMode.EACH, tracks, "1 Jul 2005 12:00:00.000"))
        range.upper_limit = upperLimit

        self.MTORangeHelper(
            MasterList, 'Range_RM */MTO/A_MTO Object */Satellite/Geo1 Mode eachInRange Time "1 Jul 2005 23:00:00.000"'
        )
        self.CompareRangeResults(
            MasterList, range.compute_all_ranges(MTORangeMode.EACH_IN_RANGE, "1 Jul 2005 23:00:00.000")
        )

        results = TestBase.Application.execute_command(
            'Range_RM */MTO/A_MTO Object */Satellite/Geo1 Time "1 Jul 2005 12:00:00.000" Mode Any Tracks 1 2 3 4 4 3 2 1'
        )
        tracks = [1, 2, 3, 4, 4, 5, 2, 1]

        isInRange = range.are_tracks_in_range(MTOTrackEvaluationType.ANY, tracks, "1 Jul 2005 12:00:00.000")
        Assert.assertEqual(Convert.ToInt32(results[0]), Convert.ToInt32(isInRange))

    def CompareRangeResults(self, MasterList, tracksRange):
        Assert.assertEqual(len(MasterList), len(tracksRange))

        i: int = 0
        while i < len(tracksRange):
            rv = Definition.RangeValues()
            rv.TrackId = int(tracksRange[i][0])
            rv.InRange = Convert.ToInt32(tracksRange[i][1])
            rv.Range = Math.Round(float(tracksRange[i][2]), 3)
            TestBase.logger.WriteLine8("{0}, {1}, {2}", rv.TrackId, rv.InRange, rv.Range)
            Assert.assertTrue((rv in MasterList))

            i += 1

    def MTORangeHelper(self, dictionary, command: str):
        dictionary.clear()
        separator: "List[int]" = [","]
        result: "ExecuteCommandResult" = TestBase.Application.execute_command(command)
        value: str
        for value in result:
            values: "List[str]" = String.Split(value, separator)
            rv = Definition.RangeValues()
            rv.TrackId = Convert.ToInt32(values[0])
            rv.InRange = Convert.ToInt32(values[1])
            rv.Range = Math.Round(Convert.ToDouble(values[2]), 3)
            TestBase.logger.WriteLine8("{0}, {1}, {2}", rv.TrackId, rv.InRange, rv.Range)
            dictionary.append(rv)

    # endregion

    # region Visibility
    def Visibility(self):
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("MTOVisibility", "MTO_VisTest.sc"))
        MasterMap = {}

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode Each Track 500 Track 549 Track 470',
        )

        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["AircraftMTO"], MTO)
        visibility: "MTOAnalysisVisibility" = mto.analysis.visibility

        visibility.use_terrain = False
        visibility.object_path = "Aircraft/Aircraft1"
        tracks = []
        tracks.append(500)
        tracks.append(549)
        tracks.append(470)

        tracksRef = tracks

        tracksVisibility = visibility.compute_tracks(MTOVisibilityMode.EACH, tracksRef, "1 Jul 2007 12:05:00.000")
        self.CompareVisibilityResults(MasterMap, tracksVisibility)

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode Each Track 549 Track 550',
        )
        tracks.clear()
        tracks.append(549)
        tracks.append(550)
        tracksRef = tracks
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_tracks(MTOVisibilityMode.EACH, tracksRef, "1 Jul 2007 12:05:00.000")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode Each Track 500 Track 549 Track 470',
        )
        tracks.clear()
        tracks.append(549)
        tracks.append(500)
        tracks.append(470)
        tracksRef = tracks
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_tracks(MTOVisibilityMode.EACH, tracksRef, "1 Jul 2007 12:05:00.000")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode Each Track 500 Track 549 Track 470 Track 550',
        )
        tracks.append(550)
        tracksRef = tracks
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_tracks(MTOVisibilityMode.EACH, tracksRef, "1 Jul 2007 12:05:00.000")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode Each Tracks 500  549  470 550',
        )
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_tracks(MTOVisibilityMode.EACH, tracksRef, "1 Jul 2007 12:05:00.000")
        )

        result: "ExecuteCommandResult" = TestBase.Application.execute_command(
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode Any Tracks 500  549  470 550'
        )
        isVis: bool = visibility.are_tracks_visible(MTOTrackEvaluationType.ANY, tracksRef, "1 Jul 2007 12:05:00")
        Assert.assertEqual(Convert.ToInt32(result[0]), Convert.ToInt32(isVis))

        result = TestBase.Application.execute_command(
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode All Tracks 500  549  470 550'
        )
        isVis = visibility.are_tracks_visible(MTOTrackEvaluationType.ALL, tracksRef, "1 Jul 2007 12:05:00")
        Assert.assertEqual(Convert.ToInt32(result[0]), Convert.ToInt32(isVis))

        Assert.assertFalse(visibility.are_all_tracks_visible("1 Jul 2007 12:05:00"))
        Assert.assertTrue(visibility.show_any_track("1 Jul 2007 12:05:00"))
        Assert.assertFalse(visibility.show_track(2, "1 Jul 2007 12:05:00"))

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode Each Tracks 500  549  470 550',
        )
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_tracks(MTOVisibilityMode.EACH, tracksRef, "1 Jul 2007 12:05:00")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode Each',
        )
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_all_tracks(MTOVisibilityMode.EACH, "1 Jul 2007 12:05:00")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:05:00" Terrain No Mode EachVisible',
        )
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_all_tracks(MTOVisibilityMode.EACH_VISIBLE, "1 Jul 2007 12:05:00")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:37:00" Terrain No Mode EachVisible',
        )
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_all_tracks(MTOVisibilityMode.EACH_VISIBLE, "1 Jul 2007 12:37:00")
        )

        result = TestBase.Application.execute_command(
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 12:37:00" Terrain No Mode EachVisible Track 390'
        )
        Assert.assertEqual("No Visibility", result[0])
        tracks.clear()
        tracks.append(390)
        tracksRef = tracks
        emptyArray = visibility.compute_tracks(MTOVisibilityMode.EACH_VISIBLE, tracksRef, "1 Jul 2007 12:37:00")
        Assert.assertEqual(0, len(emptyArray))

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 13:31:00" Terrain No Mode EachVisible',
        )
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_all_tracks(MTOVisibilityMode.EACH_VISIBLE, "1 Jul 2007 13:31:00")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 13:40:00" Terrain Yes Mode EachVisible',
        )
        visibility.use_terrain = True
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_all_tracks(MTOVisibilityMode.EACH_VISIBLE, "1 Jul 2007 13:40:00")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 13:40:00" Terrain Yes Mode EachVisible Tracks 390 391 392 393',
        )
        tracks.clear()
        tracks.append(390)
        tracks.append(391)
        tracks.append(392)
        tracks.append(393)
        tracksRef = tracks
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_tracks(MTOVisibilityMode.EACH_VISIBLE, tracksRef, "1 Jul 2007 13:40:00")
        )

        self.MTOVisibilityHelper(
            MasterMap,
            'Visibility_RM */MTO/AircraftMTO Object */Aircraft/Aircraft1 Time "1 Jul 2007 13:40:00" Terrain No Mode EachVisible Tracks 390 391 392 393',
        )
        visibility.use_terrain = False
        self.CompareVisibilityResults(
            MasterMap, visibility.compute_tracks(MTOVisibilityMode.EACH_VISIBLE, tracksRef, "1 Jul 2007 13:40:00")
        )

    def CompareVisibilityResults(self, MasterMap, tracksVisibility):
        Assert.assertEqual(len(MasterMap), len(tracksVisibility))

        i: int = 0
        while i < len(tracksVisibility):
            Assert.assertTrue((int(tracksVisibility[i][0]) in MasterMap))
            Assert.assertEqual(MasterMap[int(tracksVisibility[i][0])], Convert.ToInt32(tracksVisibility[i][1]))

            i += 1

    def MTOVisibilityHelper(self, dictionary, command: str):
        dictionary.clear()
        separator: "List[int]" = [","]
        result: "ExecuteCommandResult" = TestBase.Application.execute_command(command)
        value: str
        for value in result:
            values: "List[str]" = String.Split(value, separator)
            dictionary[int(values[0])] = int(values[1])

    # endregion

    # region Visibility2
    def Visibility2(self):
        TestBase.Application.close_scenario()
        TestBase.Application.load_scenario(TestBase.GetScenarioFile("MTOVisibility2", "MTO_VisTest2.sc"))

        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["VisTest2_MTO"], MTO)
        visibility: "MTOAnalysisVisibility" = mto.analysis.visibility

        visibility.use_terrain = False
        visibility.object_path = "Satellite/VisTest2_Sat"

        with pytest.raises(Exception):
            visibility.object_path = "Satellite/Bogus_Sat"

        result: "ExecuteCommandResult" = TestBase.Application.execute_command(
            'Visibility_RM */MTO/VisTest2_MTO Object */Satellite/VisTest2_Sat Time "23 Feb 2009 17:07:00" Terrain No Mode All Tracks 2'
        )
        Assert.assertEqual("1", result[0], "MTOVisibility2 - 1")
        bIsTrackVisible1a: bool = visibility.show_track(2, "23 Feb 2009 17:07:00.000")
        Assert.assertEqual(True, bIsTrackVisible1a, "MTOVisibility2 - 2")

        result = TestBase.Application.execute_command(
            'Visibility_RM */MTO/VisTest2_MTO Object */Satellite/VisTest2_Sat Time "23 Feb 2009 17:08:00" Terrain No Mode All Tracks 2'
        )
        Assert.assertEqual("0", result[0], "MTOVisibility2 - 3")
        bIsTrackVisible2a: bool = visibility.show_track(2, "23 Feb 2009 17:08:00.000")
        Assert.assertEqual(False, bIsTrackVisible2a, "MTOVisibility2 - 4")

        result = TestBase.Application.execute_command(
            'Visibility_RM */MTO/VisTest2_MTO Object */Satellite/VisTest2_Sat Time "23 Feb 2009 17:09:00" Terrain No Mode All Tracks 2'
        )
        Assert.assertEqual("0", result[0], "MTOVisibility2 - 5")
        bIsTrackVisible3a: bool = visibility.show_track(2, "23 Feb 2009 17:09:00.000")
        Assert.assertEqual(False, bIsTrackVisible3a, "MTOVisibility2 - 6")

        result = TestBase.Application.execute_command(
            'Visibility_RM */MTO/VisTest2_MTO Object */Satellite/VisTest2_Sat Time "23 Feb 2009 17:07:00" Terrain No Mode All Tracks 3'
        )
        Assert.assertEqual("1", result[0], "MTOVisibility2 - 7")
        bIsTrackVisible1b: bool = visibility.show_track(3, "23 Feb 2009 17:07:00.000")
        Assert.assertEqual(True, bIsTrackVisible1b, "MTOVisibility2 - 8")

        result = TestBase.Application.execute_command(
            'Visibility_RM */MTO/VisTest2_MTO Object */Satellite/VisTest2_Sat Time "23 Feb 2009 17:08:00" Terrain No Mode All Tracks 3'
        )
        Assert.assertEqual("1", result[0], "MTOVisibility2 - 9")
        bIsTrackVisible2b: bool = visibility.show_track(3, "23 Feb 2009 17:08:00.000")
        Assert.assertEqual(True, bIsTrackVisible2b, "MTOVisibility2 - 10")

        result = TestBase.Application.execute_command(
            'Visibility_RM */MTO/VisTest2_MTO Object */Satellite/VisTest2_Sat Time "23 Feb 2009 17:09:00" Terrain No Mode All Tracks 3'
        )
        Assert.assertEqual("0", result[0], "MTOVisibility2 - 11")
        bIsTrackVisible3b: bool = visibility.show_track(3, "23 Feb 2009 17:09:00.000")
        Assert.assertEqual(False, bIsTrackVisible3b, "MTOVisibility2 - 12")

        with pytest.raises(Exception):
            visibility.show_track(3, "23 Bad 2009 17:09:00.000")

        tracksOfInterest = [2, 3]

        bAreTracksVisible1a: bool = visibility.are_tracks_visible(
            MTOTrackEvaluationType.ANY, tracksOfInterest, "23 Feb 2009 17:07:00.000"
        )
        Assert.assertEqual(True, bAreTracksVisible1a, "MTOVisibility2 - 13")
        bAreTracksVisible2a: bool = visibility.are_tracks_visible(
            MTOTrackEvaluationType.ANY, tracksOfInterest, "23 Feb 2009 17:08:00.000"
        )
        Assert.assertEqual(True, bAreTracksVisible2a, "MTOVisibility2 - 14")
        bAreTracksVisible3a: bool = visibility.are_tracks_visible(
            MTOTrackEvaluationType.ANY, tracksOfInterest, "23 Feb 2009 17:09:00.000"
        )
        Assert.assertEqual(False, bAreTracksVisible3a, "MTOVisibility2 - 15")

        bIsAnyTrackVisible1: bool = visibility.show_any_track("23 Feb 2009 17:07:00.000")
        Assert.assertEqual(True, bIsAnyTrackVisible1, "MTOVisibility2 - 16")
        bIsAnyTrackVisible2: bool = visibility.show_any_track("23 Feb 2009 17:08:00.000")
        Assert.assertEqual(True, bIsAnyTrackVisible2, "MTOVisibility2 - 17")
        bIsAnyTrackVisible3: bool = visibility.show_any_track("23 Feb 2009 17:09:00.000")
        Assert.assertEqual(False, bIsAnyTrackVisible3, "MTOVisibility2 - 18")

        with pytest.raises(Exception):
            visibility.show_any_track("23 Bad 2009 17:09:00.000")

        bAreTracksVisible1b: bool = visibility.are_tracks_visible(
            MTOTrackEvaluationType.ALL, tracksOfInterest, "23 Feb 2009 17:07:00.000"
        )
        Assert.assertEqual(True, bAreTracksVisible1b, "MTOVisibility2 - 19")
        bAreTracksVisible2b: bool = visibility.are_tracks_visible(
            MTOTrackEvaluationType.ALL, tracksOfInterest, "23 Feb 2009 17:08:00.000"
        )
        Assert.assertEqual(False, bAreTracksVisible2b, "MTOVisibility2 - 20")
        bAreTracksVisible3b: bool = visibility.are_tracks_visible(
            MTOTrackEvaluationType.ALL, tracksOfInterest, "23 Feb 2009 17:09:00.000"
        )
        Assert.assertEqual(False, bAreTracksVisible3b, "MTOVisibility2 - 21")

        bAreAllTracksVisible1: bool = visibility.are_all_tracks_visible("23 Feb 2009 17:07:00.000")
        Assert.assertEqual(True, bAreAllTracksVisible1, "MTOVisibility2 - 22")
        bAreAllTracksVisible2: bool = visibility.are_all_tracks_visible("23 Feb 2009 17:08:00.000")
        Assert.assertEqual(False, bAreAllTracksVisible2, "MTOVisibility2 - 23")
        bAreAllTracksVisible3: bool = visibility.are_all_tracks_visible("23 Feb 2009 17:09:00.000")
        Assert.assertEqual(False, bAreAllTracksVisible3, "MTOVisibility2 - 24")

        with pytest.raises(Exception):
            visibility.are_all_tracks_visible("23 Bad 2009 17:09:00.000")

        with pytest.raises(Exception):
            visibility.are_tracks_visible(MTOTrackEvaluationType.ALL, tracksOfInterest, "23 Bad 2009 17:09:00.000")

        with pytest.raises(Exception):
            visibility.are_tracks_visible(-1, tracksOfInterest, "23 Feb 2009 17:09:00.000")

        tracksOfInterest2 = [-2, -3]

        with pytest.raises(Exception):
            visibility.are_tracks_visible(MTOTrackEvaluationType.ALL, tracksOfInterest2, "23 Feb 2009 17:09:00.000")


@category("EarlyBoundTests")

# [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
class Constraints(TestBase):
    def __init__(self, *args, **kwargs):
        super(Constraints, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))
            Constraints.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    # endregion

    # region Advanced
    def test_Advanced(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Constraints.AG_SAT, IStkObject), '"Active Constraints"')

        # Advanced
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GrazingAlt Min -50.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GrazingAlt Max  700000.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GrazingAngle Min  -22.2")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GrazingAngle Max  66.6")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GroundElevAngle Min  -4.32")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GroundElevAngle Max  67.89")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 BetaAngle Min  -83.38")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 BetaAngle Max   78.99")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Background Ground")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GroundTrack descending")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GrazingAlt Min off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GrazingAlt Max  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GrazingAngle Min  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GrazingAngle Max  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GroundElevAngle Min  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GroundElevAngle Max  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 BetaAngle Min  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 BetaAngle Max   off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Background off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GroundTrack off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM Setup
        acc: "AccessConstraintCollection" = Constraints.AG_SAT.access_constraints
        minmax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.GRAZING_ALTITUDE)
        )
        minmax.enable_minimum = True
        minmax.minimum = -50.0
        minmax.enable_maximum = True
        minmax.maximum = 700000.0

        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.GRAZING_ANGLE))
        minmax.enable_minimum = True
        minmax.minimum = -22.2
        minmax.enable_maximum = True
        minmax.maximum = 66.6

        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.GROUND_ELEVATION_ANGLE))
        minmax.enable_minimum = True
        minmax.minimum = -4.32
        minmax.enable_maximum = True
        minmax.maximum = 67.89

        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.BETA_ANGLE))
        minmax.enable_minimum = True
        minmax.minimum = -83.38
        minmax.enable_maximum = True
        minmax.maximum = 78.99

        back: "AccessConstraintBackground" = AccessConstraintBackground(
            acc.add_constraint(AccessConstraintType.BACKGROUND)
        )
        back.background = ConstraintBackground.GROUND

        ground: "AccessConstraintGroundTrack" = AccessConstraintGroundTrack(
            acc.add_constraint(AccessConstraintType.GROUND_TRACK)
        )
        ground.direction = ConstraintGroundTrack.DESCENDING

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.remove_constraint(AccessConstraintType.GRAZING_ALTITUDE)
        acc.remove_constraint(AccessConstraintType.GRAZING_ANGLE)
        acc.remove_constraint(AccessConstraintType.GROUND_ELEVATION_ANGLE)
        acc.remove_constraint(AccessConstraintType.BETA_ANGLE)
        acc.remove_constraint(AccessConstraintType.BACKGROUND)
        acc.remove_constraint(AccessConstraintType.GROUND_TRACK)

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Zones
    def test_Zones(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Constraints.AG_SAT, IStkObject), '"Active Constraints"')

        # Zones
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ExclusionZone -20 -30 40 50")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ExclusionZone -15 -20 20 40")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Latitude Min  -56.78")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Latitude Max   76.54")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Latitude Min  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Latitude Max   off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ExclusionZone off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ExclusionZone on")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ExclusionZone off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM Setup
        acc: "AccessConstraintCollection" = Constraints.AG_SAT.access_constraints
        minmax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.LATITUDE)
        )
        minmax.enable_minimum = True
        minmax.minimum = -56.78
        minmax.enable_maximum = True
        minmax.maximum = 76.54
        exczone: "AccessConstraintLatitudeLongitudeZone" = AccessConstraintLatitudeLongitudeZone(
            acc.add_constraint(AccessConstraintType.EXCLUSION_ZONE)
        )
        exc: "AccessConstraintExclZonesCollection" = AccessConstraintExclZonesCollection(
            acc.get_active_constraint(AccessConstraintType.EXCLUSION_ZONE)
        )
        exc.change_exclusion_zone(0, -20, -30, 40, 50)
        exczone = AccessConstraintLatitudeLongitudeZone(acc.add_constraint(AccessConstraintType.EXCLUSION_ZONE))
        exc = AccessConstraintExclZonesCollection(acc.get_active_constraint(AccessConstraintType.EXCLUSION_ZONE))
        exc.change_exclusion_zone(1, -15, -20, 20, 40)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.remove_constraint(AccessConstraintType.LATITUDE)
        exc.remove_all()

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.add_constraint(AccessConstraintType.EXCLUSION_ZONE)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        exc.remove_all()

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Sun
    def test_Sun(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Constraints.AG_SAT, IStkObject), '"Active Constraints"')

        # Sun
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunElevationAngle Min 22.2")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunElevationAngle Max 77.7")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 LunarElevationAngle Min 11.1")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 LunarElevationAngle Max 88.8")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunGroundElevAngle Min 33.3")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunGroundElevAngle Max 87.6")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunExclusion 176.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 LunarExclusion 111.1")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ThirdBodyObstruction on")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Lighting DirectSun")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunElevationAngle Min off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunElevationAngle Max off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 LunarElevationAngle Min off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 LunarElevationAngle Max off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunGroundElevAngle Min off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunGroundElevAngle Max off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 SunExclusion off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 LunarExclusion off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ThirdBodyObstruction off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Lighting Umbra")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Lighting PenumbraDirectSun")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Lighting PenumbraUmbra")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Lighting Penumbra")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Lighting UmbraDirectSun")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Lighting off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM Setup
        acc: "AccessConstraintCollection" = Constraints.AG_SAT.access_constraints
        minmax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.SUN_ELEVATION_ANGLE)
        )
        minmax.enable_minimum = True
        minmax.minimum = 22.2
        minmax.enable_maximum = True
        minmax.maximum = 77.7

        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.LUNAR_ELEVATION_ANGLE))
        minmax.enable_minimum = True
        minmax.minimum = 11.1
        minmax.enable_maximum = True
        minmax.maximum = 88.8

        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.SUN_GROUND_ELEVATION_ANGLE))
        minmax.enable_minimum = True
        minmax.minimum = 33.3
        minmax.enable_maximum = True
        minmax.maximum = 87.6

        angle: "AccessConstraintAngle" = AccessConstraintAngle(
            acc.add_constraint(AccessConstraintType.LIGHT_OF_SIGHT_SOLAR_EXCLUSION_ANGLE)
        )
        angle.angle = 176.0

        angle = AccessConstraintAngle(acc.add_constraint(AccessConstraintType.LIGHT_OF_SIGHT_LUNAR_EXCLUSION_ANGLE))
        angle.angle = 111.1

        thirdbody: "AccessConstraintThirdBody" = AccessConstraintThirdBody(
            acc.add_constraint(AccessConstraintType.THIRD_BODY_OBSTRUCTION)
        )
        availableThirdBodies = thirdbody.available_obstructions
        body: str
        for body in availableThirdBodies:
            thirdbody.add_obstruction(body)

        light: "AccessConstraintCondition" = AccessConstraintCondition(
            acc.add_constraint(AccessConstraintType.LIGHTING)
        )
        light.condition = ConstraintLighting.DIRECT_SUN

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.remove_constraint(AccessConstraintType.SUN_ELEVATION_ANGLE)
        acc.remove_constraint(AccessConstraintType.LUNAR_ELEVATION_ANGLE)
        acc.remove_constraint(AccessConstraintType.SUN_GROUND_ELEVATION_ANGLE)
        acc.remove_constraint(AccessConstraintType.LIGHT_OF_SIGHT_SOLAR_EXCLUSION_ANGLE)
        acc.remove_constraint(AccessConstraintType.LIGHT_OF_SIGHT_LUNAR_EXCLUSION_ANGLE)
        body: str
        for body in availableThirdBodies:
            thirdbody.remove_obstruction(body)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        light.condition = ConstraintLighting.UMBRA

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        light.condition = ConstraintLighting.PENUMBRA_OR_DIRECT_SUN

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        light.condition = ConstraintLighting.PENUMBRA_OR_UMBRA

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        light.condition = ConstraintLighting.PENUMBRA

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        light.condition = ConstraintLighting.UMBRA_OR_DIRECT_SUN

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.remove_constraint(AccessConstraintType.LIGHTING)

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Temporal
    def test_Temporal(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Constraints.AG_SAT, IStkObject), '"Active Constraints"')
        strPath: str = TestBase.GetScenarioFile("times.int")

        # Temporal
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Duration Min 22.2 Max 12345.6")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 LocalTime 00:04:56 12:34:56")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GMT -12:12:12 12:12:12")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ApparentTime -04:00:00 18:00:00")
        TestBase.Application.execute_command(
            (('SetConstraint */Satellite/Satellite1 Intervals Exclude "' + strPath) + '"')
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Duration off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 LocalTime off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 GMT off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ApparentTime off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Intervals off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command(
            (('SetConstraint */Satellite/Satellite1 Intervals Include "' + strPath) + '"')
        )

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Intervals off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM Setup
        acc: "AccessConstraintCollection" = Constraints.AG_SAT.access_constraints
        minmax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.DURATION)
        )
        minmax.enable_minimum = True
        minmax.minimum = 22.2
        minmax.enable_maximum = True
        minmax.maximum = 12345.6

        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.LOCAL_TIME))
        minmax.enable_minimum = True
        minmax.minimum = "00:04:56"
        minmax.enable_maximum = True
        minmax.maximum = "12:34:56"

        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.GMT))
        minmax.enable_minimum = True
        minmax.minimum = "-12:12:12"
        minmax.enable_maximum = True
        minmax.maximum = "12:12:12"

        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.APPARENT_TIME))
        minmax.enable_minimum = True
        minmax.minimum = "-04:00:00"
        minmax.enable_maximum = True
        minmax.maximum = "18:00:00"

        intervals: "AccessConstraintIntervals" = AccessConstraintIntervals(
            acc.add_constraint(AccessConstraintType.INTERVALS)
        )
        intervals.action_type = ActionType.EXCLUDE
        intervals.filename = strPath

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.remove_constraint(AccessConstraintType.DURATION)
        acc.remove_constraint(AccessConstraintType.LOCAL_TIME)
        acc.remove_constraint(AccessConstraintType.GMT)
        acc.remove_constraint(AccessConstraintType.APPARENT_TIME)
        acc.remove_constraint(AccessConstraintType.INTERVALS)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        intervals = AccessConstraintIntervals(acc.add_constraint(AccessConstraintType.INTERVALS))
        intervals.action_type = ActionType.INCLUDE
        intervals.filename = strPath

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.remove_constraint(AccessConstraintType.INTERVALS)

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()

    # endregion

    # region Basic
    def test_Basic(self):
        # Report initialization
        CompareUtility = ReportComparison(self.Units)
        CompareUtility.AddReport(clr.CastAs(Constraints.AG_SAT, IStkObject), '"Active Constraints"')

        # Basic Constraints
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 AzimuthAngle Min  -11.22 Max  123.4")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ElevationAngle Min   22.2")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ElevationAngle Max   44.4")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 RangeRate Min  -1111.11")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 RangeRate Max  4444.44")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Range Min 4000000.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Range Max 8000000.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Altitude Min -300.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Altitude Max 1300.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 AngularRate Min 0.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 AngularRate Max 12.3")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 PropagationDelay Min  0.004")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 PropagationDelay Max  4.5")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 AzimuthAngle off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ElevationAngle Min   off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ElevationAngle Max   off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 RangeRate Min  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 RangeRate Max  off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Range Min off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Range Max off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Altitude Min off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 Altitude Max off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 AngularRate Min off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 AngularRate Max off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 PropagationDelay Min off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 PropagationDelay Max  off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 AzimuthAngle Min  -11.22 Max 360.0")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ElevationAngle Min   22.2")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 AzimuthAngle off")
        TestBase.Application.execute_command("SetConstraint */Satellite/Satellite1 ElevationAngle Min   off")

        CompareUtility.TakeConnectSnapshot(TestBase.Application)

        # OM Setup
        acc: "AccessConstraintCollection" = Constraints.AG_SAT.access_constraints
        azimuthangle: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.AZIMUTH_ANGLE)
        )
        azimuthangle.enable_minimum = True
        azimuthangle.minimum = -11.22
        azimuthangle.enable_maximum = True
        azimuthangle.maximum = 123.4

        elevationangle: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.ELEVATION_ANGLE)
        )
        elevationangle.enable_minimum = True
        elevationangle.minimum = 22.2
        elevationangle.enable_maximum = True
        elevationangle.maximum = 44.4

        rangerate: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.RANGE_RATE)
        )
        rangerate.enable_minimum = True
        rangerate.minimum = -1111.11
        rangerate.enable_maximum = True
        rangerate.maximum = 4444.44

        range: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.RANGE)
        )
        range.enable_minimum = True
        range.minimum = 4000000.0
        range.enable_maximum = True
        range.maximum = 8000000.0

        altit: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.ALTITUDE)
        )
        altit.enable_minimum = True
        altit.minimum = -300.0
        altit.enable_maximum = True
        altit.maximum = 1300.0

        angularrate: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.ANGULAR_RATE)
        )
        angularrate.enable_minimum = True
        angularrate.minimum = 0.0
        angularrate.enable_maximum = True
        angularrate.maximum = 12.3

        propdelay: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.PROPAGATION_DELAY)
        )
        propdelay.enable_minimum = True
        propdelay.minimum = 0.004
        propdelay.enable_maximum = True
        propdelay.maximum = 4.5

        with pytest.raises(Exception):
            acc.add_constraint(AccessConstraintType.LINE_OF_SIGHT)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.remove_constraint(AccessConstraintType.AZIMUTH_ANGLE)
        acc.remove_constraint(AccessConstraintType.ELEVATION_ANGLE)
        acc.remove_constraint(AccessConstraintType.RANGE_RATE)
        acc.remove_constraint(AccessConstraintType.RANGE)
        acc.remove_constraint(AccessConstraintType.ALTITUDE)
        acc.remove_constraint(AccessConstraintType.ANGULAR_RATE)
        acc.remove_constraint(AccessConstraintType.PROPAGATION_DELAY)

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        minmax: "IAccessConstraintMinMaxBase" = IAccessConstraintMinMaxBase(
            acc.add_constraint(AccessConstraintType.AZIMUTH_ANGLE)
        )
        minmax.enable_minimum = True
        minmax.minimum = -11.22
        minmax.enable_maximum = True
        minmax.maximum = 360.0
        minmax = IAccessConstraintMinMaxBase(acc.add_constraint(AccessConstraintType.ELEVATION_ANGLE))
        minmax.enable_minimum = True
        minmax.minimum = 22.2

        CompareUtility.TakeOMSnapshot(TestBase.Application)

        acc.remove_constraint(AccessConstraintType.AZIMUTH_ANGLE)
        acc.remove_constraint(AccessConstraintType.ELEVATION_ANGLE)

        CompareUtility.TakeOMSnapshot(TestBase.Application)
        CompareUtility.CompareReportSnapshots()


@category("EarlyBoundTests")

# [Ignore("To diagnose Regression Suite hang"), Category("Ignored")]
class Access(TestBase):
    def __init__(self, *args, **kwargs):
        super(Access, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        if TestBase.Application.current_scenario.children.contains(STKObjectType.SATELLITE, "Sat_Access"):
            TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "Sat_Access")

        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    AG_FAC: "Facility" = None
    # endregion

    def CompareAccessResults(self, execResult: "ExecuteCommandResult", drResult: "DataProviderResult"):
        result: str = execResult[0]
        token: "List[int]" = [" "]
        connectParsed: "List[str]" = String.Split(result, token)
        s: str
        for s in connectParsed:
            Console.WriteLine(s)

        arStartTimes = drResult.data_sets[0].get_values()
        arStopTimes = drResult.data_sets[1].get_values()

        i: int = 0
        while i < Array.Length(arStartTimes):
            Console.WriteLine(((str(arStartTimes[i]) + "  ") + str(arStopTimes[i])))

            i += 1

        if float(arStartTimes[0]) == Convert.ToDouble(connectParsed[4]):
            i: int = 0
            while i < Array.Length(arStartTimes):
                dDPstart: float = float(arStartTimes[i])
                dDPstop: float = float(arStopTimes[i])
                dCONstart: float = Convert.ToDouble(connectParsed[(4 + ((i * 2)))])
                dCONstop: float = Convert.ToDouble(connectParsed[((4 + ((i * 2))) + 1)])

                Assert.assertAlmostEqual(dDPstart, dCONstart, delta=3)
                Assert.assertAlmostEqual(dDPstop, dCONstop, delta=3)

                i += 1

    @parameterized.expand(
        [
            ("*/Satellite/Satellite1", "*/Facility/Facility1"),
            ("*/Facility/Facility1", "*/Satellite/Satellite1"),
            ("*/Satellite/Satellite1", "*/Facility/Facility1/Sensor/Sensor1/Transmitter/Transmitter1"),
            ("*/Facility/Facility1/Sensor/Sensor1/Transmitter/Transmitter1", "*/Satellite/Satellite1"),
            ("*/Facility/Facility1", "*/Satellite/Satellite1/Sensor/Sensor2/Receiver/Receiver1"),
            ("*/Satellite/Satellite1/Sensor/Sensor2/Receiver/Receiver1", "*/Facility/Facility1"),
            (
                "*/Facility/Facility1/Sensor/Sensor1/Transmitter/Transmitter1",
                "*/Satellite/Satellite1/Sensor/Sensor2/Receiver/Receiver1",
            ),
            (
                "*/Satellite/Satellite1/Sensor/Sensor2/Receiver/Receiver1",
                "*/Facility/Facility1/Sensor/Sensor1/Transmitter/Transmitter1",
            ),
        ]
    )
    def test_AccessTest(self, objPath1: str, objPath2: str):
        if not ("DummyScenario1" in TestBase.Application.current_scenario.instance_name):
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("IntegrityTests", "DummyScenario1", "DummyScenario1.sc"))

        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.execute_command("SetUnits / EPSEC")

        startTime: str = str((Scenario(TestBase.Application.current_scenario)).start_time)
        stopTime: str = str((Scenario(TestBase.Application.current_scenario)).stop_time)

        obj1: "IStkObject" = TestBase.Application.get_object_from_path(objPath1)
        obj2: "IStkObject" = TestBase.Application.get_object_from_path(objPath2)
        arCols = ["Start Time", "Stop Time"]

        #
        # Use Object Time Periods (OBJECT_ACCESS_TIME)
        #
        execResult: "ExecuteCommandResult" = TestBase.Application.execute_command(
            ((("Access " + objPath1) + " ") + objPath2)
        )
        TestBase.Application.execute_command(((("RemoveAccess " + objPath1) + " ") + objPath2))

        access: "Access" = obj1.get_access_to_object(obj2)
        access.access_time_period = AccessTimeType.OBJECT_ACCESS_TIME
        access.compute_access()
        intervalDp: "DataProviderInterval" = DataProviderInterval(access.data_providers["Access Data"])
        drResult: "DataProviderResult" = intervalDp.execute_elements(startTime, stopTime, arCols)
        access.remove_access()

        self.CompareAccessResults(execResult, drResult)

        # Use Scenario Time Periods (SCENARIO_INTERVAL)
        execResult = TestBase.Application.execute_command(
            (((("Access " + objPath1) + " ") + objPath2) + " TimePeriod Scenario")
        )
        TestBase.Application.execute_command(((("RemoveAccess " + objPath1) + " ") + objPath2))

        access = obj1.get_access_to_object(obj2)
        access.access_time_period = AccessTimeType.SCENARIO_INTERVAL
        access.compute_access()
        intervalDp = DataProviderInterval(access.data_providers["Access Data"])
        drResult = intervalDp.execute_elements(startTime, stopTime, arCols)
        access.remove_access()

        self.CompareAccessResults(execResult, drResult)

        #
        # Use Time Intervals (eAccessTimeEventIntervalList)
        #
        execResult = TestBase.Application.execute_command(
            (
                ((("Access " + objPath1) + " ") + objPath2)
                + ' TimePeriod "Scenario/IntegrityTests AvailabilityIntervals Interval List"'
            )
        )
        TestBase.Application.execute_command(((("RemoveAccess " + objPath1) + " ") + objPath2))

        access = obj1.get_access_to_object(obj2)
        access.access_time_period = AccessTimeType.TIME_INTERVAL_LIST
        access.specify_access_event_intervals(
            TestBase.Application.current_scenario.analysis_workbench_components.time_interval_lists[
                "AvailabilityIntervals"
            ]
        )
        access.compute_access()
        intervalDp = DataProviderInterval(access.data_providers["Access Data"])
        drResult = intervalDp.execute_elements(startTime, stopTime, arCols)
        access.remove_access()

        self.CompareAccessResults(execResult, drResult)

        #
        # Specify Time Periods (SPECIFIED_TIME_PERIOD)
        #
        execResult = TestBase.Application.execute_command(
            (((("Access " + objPath1) + " ") + objPath2) + ' TimePeriod "0" "84600"')
        )
        TestBase.Application.execute_command(((("RemoveAccess " + objPath1) + " ") + objPath2))

        access = obj1.get_access_to_object(obj2)
        access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
        access.specify_access_time_period(0, 84600)
        access.compute_access()
        intervalDp = DataProviderInterval(access.data_providers["Access Data"])
        drResult = intervalDp.execute_elements(startTime, stopTime, arCols)
        access.remove_access()

        self.CompareAccessResults(execResult, drResult)

        #
        # Specify Time Periods (TIME_INTERVALS)
        #
        execResult = TestBase.Application.execute_command(
            (
                ((("Access " + objPath1) + " ") + objPath2)
                + ' TimePeriod "Satellite/Satellite1 AvailabilityIntervals.First Interval"'
            )
        )
        TestBase.Application.execute_command(((("RemoveAccess " + objPath1) + " ") + objPath2))

        access = obj1.get_access_to_object(obj2)
        access.access_time_period = AccessTimeType.TIME_INTERVALS
        intervalCollection: "TimeIntervalCollection" = clr.CastAs(
            access.access_time_period_data, TimeIntervalCollection
        )

        interval: "ITimeToolTimeInterval" = (
            TestBase.Application.current_scenario.analysis_workbench_components.time_intervals[
                "AvailabilityIntervals.First"
            ]
        )
        intervalResult: "TimeToolTimeIntervalResult" = interval.find_interval()
        intervalCollection.add(intervalResult.interval.start, intervalResult.interval.stop)

        access.compute_access()
        intervalDp = DataProviderInterval(access.data_providers["Access Data"])
        drResult = intervalDp.execute_elements(startTime, stopTime, arCols)
        access.remove_access()

        self.CompareAccessResults(execResult, drResult)

        TestBase.Application.units_preferences.reset_units()
        TestBase.Application.execute_command("SetUnits / UTCG")

    def test_OnePointAccess(self):
        TestBase.LoadTestScenario(Path.Combine("IntegrityTests", "IntegrityTests.sc"))
        Access.AG_SAT = Satellite(TestBase.Application.current_scenario.children["Satellite1"])
        Access.AG_FAC = Facility(TestBase.Application.current_scenario.children["Facility1"])

        # Connect
        cmd: str = "OnePointAccess */Satellite/Satellite1 */Facility/Facility1 Create"
        TestBase.Application.execute_command(cmd)

        cmd = 'OnePointAccess */Satellite/Satellite1 */Facility/Facility1 Compute "1 Jul 1999 00:00:00.000" "2 Jul 1999 00:00:00.000" 2400'
        connectResult: "ExecuteCommandResult" = TestBase.Application.execute_command(cmd)
        # foreach (string s in connectResult)
        # {
        #    logger.WriteLine(s);
        # }

        # OM
        onePtAccess: "OnePointAccess" = (IStkObject(Access.AG_SAT)).create_one_point_access("Facility/Facility1")
        onePtAccess.start_time = "1 Jul 1999 00:00:00.000"
        onePtAccess.stop_time = "2 Jul 1999 00:00:00.000"
        onePtAccess.step_size = 2400
        onePtAccess.summary_option = OnePointAccessSummary.DETAILED
        omResults: "OnePointAccessResultCollection" = onePtAccess.compute()
        # foreach (OnePointAccessResult r in omResults)
        # {
        #    logger.WriteLine(r.Time);
        #    logger.WriteLine(r.AccessSatisfied);
        #    foreach (OnePointAccessConstraint c in r.Constraints)
        #    {
        #        logger.WriteLine(c.Constraint);
        #        logger.WriteLine(c.ObjectPath);
        #        logger.WriteLine(c.Status);
        #        logger.WriteLine(c.Value);
        #    }
        # }

        # Compare

        # Sample Connect Result (3 lines):
        #
        #      1 Jul 1999 00:00:00.000	Yes
        #      Facility/Facility1	LineOfSight	Ok	6.062615559563e-001
        #      Facility/Facility1	ElevationAngle	Ok	6.062615559563e-001

        Assert.assertEqual(connectResult.count, (3 * omResults.count), "OnePointAccess counts differ")

        i: int = 0
        while i < omResults.count:
            sConnectResultLine1: str = connectResult[(3 * i)]
            tokens: "List[str]" = String.Split(sConnectResultLine1, [" ", "\t"])
            connectTime: str = (((((tokens[0] + " ") + tokens[1]) + " ") + tokens[2]) + " ") + tokens[3]
            connectAccessSatisfied: bool = tokens[4] == "Yes"

            sConnectResultLine2: str = connectResult[((3 * i) + 1)]
            tokens = String.Split(sConnectResultLine2, [" ", "\t"])
            connectObjectPath1: str = tokens[0]
            connectConstraint1: str = tokens[1]
            connectStatus1: str = tokens[2]
            connectValue1: float = float(tokens[3])

            sConnectResultLine3: str = connectResult[((3 * i) + 2)]
            tokens = String.Split(sConnectResultLine3, [" ", "\t"])
            connectObjectPath2: str = tokens[0]
            connectConstraint2: str = tokens[1]
            connectStatus2: str = tokens[2]
            connectValue2: float = float(tokens[3])

            omResult: "OnePointAccessResult" = omResults[i]

            Assert.assertEqual(connectTime, omResult.time, "OnePointAccess times differ")
            Assert.assertEqual(
                connectAccessSatisfied, omResult.access_is_satisfied, "OnePointAccess AccessSatisfied differ"
            )

            Assert.assertEqual(
                connectObjectPath1, omResult.constraints[0].object_path, "OnePointAccess ObjectPath differ"
            )
            Assert.assertEqual(connectConstraint1, "LineOfSight", "OnePointAccess Connect Constraint1 differ")
            Assert.assertEqual(
                omResult.constraints[0].constraint,
                AccessConstraintType.LINE_OF_SIGHT,
                "OnePointAccess OM Constraint1 differ",
            )
            Assert.assertEqual(connectStatus1, "Ok", "OnePointAccess Connect Status1 differ")
            Assert.assertEqual(
                omResult.constraints[0].status, OnePointAccessStatus.OK, "OnePointAccess OM Status1 differ"
            )
            Assert.assertAlmostEqual(
                connectValue1, omResult.constraints[0].value, delta=1e-08, msg="OnePointAccess Value1 differ"
            )

            Assert.assertEqual(
                connectObjectPath2, omResult.constraints[1].object_path, "OnePointAccess ObjectPath differ"
            )
            Assert.assertEqual(connectConstraint2, "ElevationAngle", "OnePointAccess Connect Constraint1 differ")
            Assert.assertEqual(
                omResult.constraints[1].constraint,
                AccessConstraintType.ELEVATION_ANGLE,
                "OnePointAccess OM Constraint1 differ",
            )
            Assert.assertEqual(connectStatus2, "Ok", "OnePointAccess Connect Status1 differ")
            Assert.assertEqual(
                omResult.constraints[1].status, OnePointAccessStatus.OK, "OnePointAccess OM Status1 differ"
            )
            Assert.assertAlmostEqual(
                connectValue2, omResult.constraints[1].value, delta=1e-08, msg="OnePointAccess Value1 differ"
            )

            i += 1

    # endregion
    # endregion
    # endregion
    # endregion
    # endregion
    # endregion
    # endregion
    # endregion
