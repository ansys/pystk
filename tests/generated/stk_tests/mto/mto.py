import pytest
from test_util import *
from assert_extension import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from math2 import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
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
        TestBase.LoadTestScenario(Path.Combine("MtoTests", "MtoTests.sc"))
        EarlyBoundTests.AG_MTO = MTO(TestBase.Application.current_scenario.children.new(STKObjectType.MTO, "Mto1"))

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_MTO = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_MTO: "MTO" = None
    # endregion

    # region Visibility
    def test_Visibility(self):
        visibility: "MTOAnalysisVisibility" = EarlyBoundTests.AG_MTO.analysis.visibility
        visibility.entirety = MTOEntirety.ALL
        Assert.assertEqual(MTOEntirety.ALL, visibility.entirety)
        visibility.entirety = MTOEntirety.PARTIAL
        Assert.assertEqual(MTOEntirety.PARTIAL, visibility.entirety)

        visibility.object_path = "Satellite/Satellite1"
        Assert.assertEqual("Satellite/Satellite1", visibility.object_path)

        visibility.object_data = 1
        Assert.assertEqual(1, visibility.object_data)
        visibility.object_interval = MTOObjectInterval.EXTENDED
        Assert.assertEqual(MTOObjectInterval.EXTENDED, visibility.object_interval)
        visibility.object_interval = MTOObjectInterval.NORMAL
        Assert.assertEqual(MTOObjectInterval.NORMAL, visibility.object_interval)
        visibility.use_terrain = False
        Assert.assertFalse(visibility.use_terrain)
        visibility.use_terrain = True
        Assert.assertTrue(visibility.use_terrain)

    # endregion

    # region ZZZ_Visibility_UseTrackTimes
    def test_ZZZ_Visibility_UseTrackTimes(self):
        if TestBase.Application.current_scenario.instance_name != "MtoAnalysisTest":
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("MtoTests", "MTO_UseTrackTimes", "MtoAnalysisTest.sc"))

        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["MTO1"], MTO)
        visibility: "MTOAnalysisVisibility" = mto.analysis.visibility
        visibility.object_path = "Aircraft/Aircraft1"

        Assert.assertTrue(visibility.show_any_track("UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            visibility.show_any_track("UseTrackTimesX")

        Assert.assertTrue(visibility.show_track(1, "UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("4 is an invalid track id")):
            visibility.show_track(4, "UseTrackTimes")
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            visibility.show_track(1, "UseTrackTimesX")

        Assert.assertTrue(visibility.are_all_tracks_visible("UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            visibility.are_all_tracks_visible("UseTrackTimesX")

        Assert.assertTrue(visibility.are_tracks_visible(MTOTrackEvaluationType.ALL, [1, 2, 3], "UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("4 is an invalid track id")):
            visibility.are_tracks_visible(MTOTrackEvaluationType.ALL, [1, 2, 3, 4], "UseTrackTimes")
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            visibility.are_tracks_visible(MTOTrackEvaluationType.ALL, [1, 2, 3], "UseTrackTimesX")

        arTracks = visibility.compute_all_tracks(MTOVisibilityMode.EACH, "UseTrackTimes")
        Assert.assertEqual(3, len(arTracks))
        Assert.assertEqual(1, arTracks[0][0])
        Assert.assertTrue(bool(arTracks[0][1]))
        Assert.assertEqual(2, arTracks[1][0])
        Assert.assertTrue(bool(arTracks[1][1]))
        Assert.assertEqual(3, arTracks[2][0])
        Assert.assertTrue(bool(arTracks[2][1]))
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            visibility.compute_all_tracks(MTOVisibilityMode.EACH, "UseTrackTimesX")

        arTracks = visibility.compute_tracks(MTOVisibilityMode.EACH, [1, 2, 3], "UseTrackTimes")
        Assert.assertEqual(3, len(arTracks))
        Assert.assertEqual(1, arTracks[0][0])
        Assert.assertTrue(bool(arTracks[0][1]))
        Assert.assertEqual(2, arTracks[1][0])
        Assert.assertTrue(bool(arTracks[1][1]))
        Assert.assertEqual(3, arTracks[2][0])
        Assert.assertTrue(bool(arTracks[2][1]))
        with pytest.raises(Exception, match=RegexSubstringMatch("4 is an invalid track id")):
            visibility.compute_tracks(MTOVisibilityMode.EACH, [1, 2, 3, 4], "UseTrackTimes")
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            arTracks = visibility.compute_tracks(MTOVisibilityMode.EACH, [1, 2, 3], "UseTrackTimesX")

    # endregion

    # region Range
    def test_Range(self):
        range: "MTOAnalysisRange" = EarlyBoundTests.AG_MTO.analysis.range
        range.entirety = MTOEntirety.ALL
        Assert.assertEqual(MTOEntirety.ALL, range.entirety)
        range.entirety = MTOEntirety.PARTIAL
        Assert.assertEqual(MTOEntirety.PARTIAL, range.entirety)

        range.lower_limit = 1
        Assert.assertEqual(1, range.lower_limit)
        range.upper_limit = 3000
        Assert.assertEqual(3000, range.upper_limit)

        range.object_path = "Satellite/Satellite1"
        Assert.assertEqual("Satellite/Satellite1", range.object_path)

        range.object_data = 1
        Assert.assertEqual(1, range.object_data)

        range.object_interval = MTOObjectInterval.EXTENDED
        Assert.assertEqual(MTOObjectInterval.EXTENDED, range.object_interval)
        range.object_interval = MTOObjectInterval.NORMAL
        Assert.assertEqual(MTOObjectInterval.NORMAL, range.object_interval)

    # endregion

    # region ZZZ_Range_UseTrackTimes
    def test_ZZZ_Range_UseTrackTimes(self):
        if TestBase.Application.current_scenario.instance_name != "MtoAnalysisTest":
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("MtoTests", "MTO_UseTrackTimes", "MtoAnalysisTest.sc"))

        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["MTO1"], MTO)
        range: "MTOAnalysisRange" = mto.analysis.range
        range.object_path = "Aircraft/Aircraft1"

        Assert.assertTrue(range.is_any_track_in_range("UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            range.is_any_track_in_range("UseTrackTimesX")

        Assert.assertTrue(range.is_track_in_range(1, "UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("4 is an invalid track id")):
            range.is_track_in_range(4, "UseTrackTimes")
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            range.is_track_in_range(1, "UseTrackTimesX")

        Assert.assertFalse(range.are_all_tracks_in_range("UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            range.are_all_tracks_in_range("UseTrackTimesX")

        Assert.assertTrue(range.are_tracks_in_range(MTOTrackEvaluationType.ALL, [1], "UseTrackTimes"))
        Assert.assertFalse(range.are_tracks_in_range(MTOTrackEvaluationType.ALL, [1, 2, 3], "UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("4 is an invalid track id")):
            range.are_tracks_in_range(MTOTrackEvaluationType.ALL, [4], "UseTrackTimes")
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            range.are_tracks_in_range(MTOTrackEvaluationType.ALL, [1, 2, 3], "UseTrackTimesX")

        arTracks = range.compute_all_ranges(MTORangeMode.EACH, "UseTrackTimes")
        Assert.assertEqual(3, len(arTracks))
        Assert.assertEqual(1, arTracks[0][0])
        Assert.assertTrue(bool(arTracks[0][1]))
        Assert.assertEqual(2, arTracks[1][0])
        Assert.assertFalse(bool(arTracks[1][1]))
        Assert.assertEqual(3, arTracks[2][0])
        Assert.assertFalse(bool(arTracks[2][1]))
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            range.compute_all_ranges(MTORangeMode.EACH, "UseTrackTimesX")

        arTracks = range.compute_ranges(
            MTORangeMode.EACH, [1, 2, 3], "UseTrackTimes"
        )  # 4 an invalid track id - BUG100185
        Assert.assertEqual(3, len(arTracks))
        Assert.assertEqual(1, arTracks[0][0])
        Assert.assertTrue(bool(arTracks[0][1]))
        Assert.assertEqual(2, arTracks[1][0])
        Assert.assertFalse(bool(arTracks[1][1]))
        Assert.assertEqual(3, arTracks[2][0])
        Assert.assertFalse(bool(arTracks[2][1]))
        with pytest.raises(Exception, match=RegexSubstringMatch("4 is an invalid track id")):
            arTracks = range.compute_ranges(MTORangeMode.EACH, [1, 2, 3, 4], "UseTrackTimes")
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            arTracks = range.compute_ranges(MTORangeMode.EACH, [1, 2, 3], "UseTrackTimesX")

    # endregion

    # region FieldOfView
    def test_FieldOfView(self):
        fov: "MTOAnalysisFieldOfView" = EarlyBoundTests.AG_MTO.analysis.field_of_view
        fov.entirety = MTOEntirety.ALL
        Assert.assertEqual(MTOEntirety.ALL, fov.entirety)
        fov.entirety = MTOEntirety.PARTIAL
        Assert.assertEqual(MTOEntirety.PARTIAL, fov.entirety)

        with pytest.raises(Exception):
            fov.sensor = "Satellite/Satellite1"

        fov.sensor = "Satellite/Satellite1/Sensor/Sensor2"
        Assert.assertEqual("Satellite/Satellite1/Sensor/Sensor2", fov.sensor)

    # endregion

    # region ZZZ_FieldOfView_UseTrackTimes
    def test_ZZZ_FieldOfView_UseTrackTimes(self):
        Console.WriteLine("ZZZ_FieldOfView_UseTrackTimes begin")
        if TestBase.Application.current_scenario.instance_name != "MtoAnalysisTest":
            TestBase.Application.close_scenario()
            TestBase.LoadTestScenario(TestBase.PathCombine("MtoTests", "MTO_UseTrackTimes", "MtoAnalysisTest.sc"))

        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["MTO1"], MTO)
        fov: "MTOAnalysisFieldOfView" = mto.analysis.field_of_view
        fov.sensor = "Aircraft/Aircraft1/Sensor/Sensor1"

        Assert.assertTrue(fov.is_any_track_in_field_of_view("UseTrackTimes"))
        # PLTFA-1954 TryCatchAssertBlock.ExpectedException("within the expected range", delegate () { fov.IsAnyTrackInFOV("UseTrackTimesX"); });

        Assert.assertTrue(fov.is_track_in_field_of_view(1, "UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("Track id is invalid")):
            fov.is_track_in_field_of_view(4, "UseTrackTimes")
        # PLTFA-1954 TryCatchAssertBlock.ExpectedException("within the expected range", delegate () { fov.IsTrackInFOV(1, "UseTrackTimesX"); });

        Assert.assertTrue(fov.are_all_tracks_in_field_of_view("UseTrackTimes"))
        # PLTFA-1954 TryCatchAssertBlock.ExpectedException("within the expected range", delegate () { fov.AreAllTracksInFOV("UseTrackTimesX"); });

        Assert.assertTrue(fov.are_tracks_in_field_of_view(MTOTrackEvaluationType.ALL, [1, 2, 3], "UseTrackTimes"))
        with pytest.raises(Exception, match=RegexSubstringMatch("4 is an invalid track id")):
            fov.are_tracks_in_field_of_view(MTOTrackEvaluationType.ALL, [1, 2, 3, 4], "UseTrackTimes")
        # PLTFA-1954 TryCatchAssertBlock.ExpectedException("within the expected range", delegate () { fov.AreTracksInFOV(MTOTrackEvaluationType.ALL, new object[] { 1, 2, 3 }, "UseTrackTimesX"); });

        arTracks = fov.compute_all_tracks(MTOVisibilityMode.EACH, "UseTrackTimes")
        Assert.assertEqual(3, len(arTracks))
        Assert.assertEqual(1, arTracks[0][0])
        Assert.assertTrue(bool(arTracks[0][1]))
        Assert.assertEqual(2, arTracks[1][0])
        Assert.assertTrue(bool(arTracks[1][1]))
        Assert.assertEqual(3, arTracks[2][0])
        Assert.assertTrue(bool(arTracks[2][1]))
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            fov.compute_all_tracks(MTOVisibilityMode.EACH, "UseTrackTimesX")

        arTracks = fov.compute_tracks(
            MTOVisibilityMode.EACH, [1, 2, 3], "UseTrackTimes"
        )  # 4 an invalid track id - BUG100185
        Assert.assertEqual(3, len(arTracks))
        Assert.assertEqual(1, arTracks[0][0])
        Assert.assertTrue(bool(arTracks[0][1]))
        Assert.assertEqual(2, arTracks[1][0])
        Assert.assertTrue(bool(arTracks[1][1]))
        Assert.assertEqual(3, arTracks[2][0])
        Assert.assertTrue(bool(arTracks[2][1]))
        with pytest.raises(Exception, match=RegexSubstringMatch("4 is an invalid track id")):
            arTracks = fov.compute_tracks(MTOVisibilityMode.EACH, [1, 2, 3, 4], "UseTrackTimes")
        with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
            arTracks = fov.compute_tracks(MTOVisibilityMode.EACH, [1, 2, 3], "UseTrackTimesX")

    # endregion

    # region InsertMTOPoint
    def test_InsertMtoPoint(self):
        mto: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children.new(STKObjectType.MTO, "InsertMto"), MTO)
        track: "MTOTrack" = mto.tracks.add(1)
        track.points.add("1 Jul 2007 12:00:00.000")
        track.points.add("1 Jul 2007 13:00:00.000")
        track.points.add("1 Jul 2007 14:00:00.000")
        track.points.insert_point("1 Jul 2007 11:00:00.000", 10, 10, 1)
        Assert.assertEqual(4, track.points.count)
        Assert.assertEqual("1 Jul 2007 11:00:00.000", track.points[0].time)
        Assert.assertEqual(10, track.points[0].latitude)
        Assert.assertEqual(10, track.points[0].longitude)
        Assert.assertEqual(1, track.points[0].altitude)
        Assert.assertEqual("1 Jul 2007 12:00:00.000", track.points[1].time)
        Assert.assertEqual(0, track.points[1].latitude)
        Assert.assertEqual(0, track.points[1].longitude)
        Assert.assertEqual(0, track.points[1].altitude)
        Assert.assertEqual("1 Jul 2007 13:00:00.000", track.points[2].time)
        Assert.assertEqual(0, track.points[2].latitude)
        Assert.assertEqual(0, track.points[2].longitude)
        Assert.assertEqual(0, track.points[2].altitude)
        Assert.assertEqual("1 Jul 2007 14:00:00.000", track.points[3].time)
        Assert.assertEqual(0, track.points[3].latitude)
        Assert.assertEqual(0, track.points[3].longitude)
        Assert.assertEqual(0, track.points[3].altitude)

        track.points.insert_point("1 Jul 2007 13:30:00.000", 10, 15, 1)
        Assert.assertEqual(5, track.points.count)
        Assert.assertEqual("1 Jul 2007 11:00:00.000", track.points[0].time)
        Assert.assertEqual("1 Jul 2007 12:00:00.000", track.points[1].time)
        Assert.assertEqual("1 Jul 2007 13:00:00.000", track.points[2].time)
        Assert.assertEqual("1 Jul 2007 13:30:00.000", track.points[3].time)
        Assert.assertEqual("1 Jul 2007 14:00:00.000", track.points[4].time)

        track.points.insert_point("1 Jul 2007 15:00:00.000", 10, 20, 1)
        Assert.assertEqual(6, track.points.count)
        Assert.assertEqual("1 Jul 2007 11:00:00.000", track.points[0].time)
        Assert.assertEqual("1 Jul 2007 12:00:00.000", track.points[1].time)
        Assert.assertEqual("1 Jul 2007 13:00:00.000", track.points[2].time)
        Assert.assertEqual("1 Jul 2007 13:30:00.000", track.points[3].time)
        Assert.assertEqual("1 Jul 2007 14:00:00.000", track.points[4].time)
        Assert.assertEqual("1 Jul 2007 15:00:00.000", track.points[5].time)

        track.points.remove_all()
        Assert.assertEqual(0, track.points.count)

        track.points.insert_point("1 Jul 1999 12:00:00.000", 5, 1, 9)
        Assert.assertEqual(1, track.points.count)
        Assert.assertEqual("1 Jul 1999 12:00:00.000", track.points[0].time)
        Assert.assertEqual(5, track.points[0].latitude)
        Assert.assertEqual(1, track.points[0].longitude)
        Assert.assertEqual(9, track.points[0].altitude)
        TestBase.Application.current_scenario.children.unload(STKObjectType.MTO, "InsertMto")

    # endregion

    # region Position
    def test_Position(self):
        position: "MTOAnalysisPosition" = EarlyBoundTests.AG_MTO.analysis.position
        position.altitude_reference = AltitudeReferenceType.MEAN_SEA_LEVEL
        Assert.assertEqual(AltitudeReferenceType.MEAN_SEA_LEVEL, position.altitude_reference)
        position.altitude_reference = AltitudeReferenceType.TERRAIN
        Assert.assertEqual(AltitudeReferenceType.TERRAIN, position.altitude_reference)
        position.altitude_reference = AltitudeReferenceType.WGS84
        Assert.assertEqual(AltitudeReferenceType.WGS84, position.altitude_reference)

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_MTO, IStkObject))
        oHelper.TestObjectFilesArray((IStkObject(EarlyBoundTests.AG_MTO)).object_files)

    # endregion

    # region BasicTrackPerformance
    # [Test]
    @category("Basic Tests")
    def BasicTrackPerformance(self):
        TestBase.logger.WriteLine("----- Basic MTO Test ----- BEGIN -----")

        # Initialization
        start: int = DateTime.Now.Ticks

        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")

        timeList = []
        latList = []
        lonList = []
        altList = []

        connectStr: str = "Track */MTO/Mto1 Extend 1 10000 "

        i: int = 1
        while i < 100001:
            timeList.append(i)
            connectStr += ('"' + str(i)) + '" '
            latList.append((90 / i))
            connectStr += str(((90 / i))) + " "
            lonList.append((90 / i))
            connectStr += str(((90 / i))) + " "
            altList.append((500 / i))
            connectStr += str(((500 / i))) + " "

            i += 10

        timeArray = timeList
        latArray = latList
        lonArray = lonList
        altArray = altList

        stop: int = DateTime.Now.Ticks
        duration: float = stop - start

        TestBase.logger.WriteLine((("Initialization in " + str((duration / (10000000)))) + " seconds."))

        # Track extend
        start = DateTime.Now.Ticks

        TestBase.Application.begin_update()

        oTrackCollection: "MTOTrackCollection" = EarlyBoundTests.AG_MTO.tracks
        oTrack: "MTOTrack" = oTrackCollection.add(0)
        Assert.assertEqual(1, EarlyBoundTests.AG_MTO.tracks.count)
        oTrack.points.extend(timeArray, latArray, lonArray, altArray)

        TestBase.Application.end_update()

        stop = DateTime.Now.Ticks

        duration = stop - start
        TestBase.logger.WriteLine((("10,000 points in " + str((duration / (10000000)))) + " seconds."))

        EarlyBoundTests.AG_MTO.tracks.remove_all()

        start = DateTime.Now.Ticks

        TestBase.Application.execute_command("SetUnits / EPSEC")
        TestBase.Application.execute_command("BatchGraphics * On")
        TestBase.Application.execute_command("Graphics */MTO/Mto1 BatchGraphics On")

        TestBase.Application.execute_command("Track */MTO/Mto1 Add 1")
        TestBase.Application.execute_command(connectStr)

        TestBase.Application.execute_command("BatchGraphics * Off")
        TestBase.Application.execute_command("Graphics */MTO/Mto1 BatchGraphics Off")

        stop = DateTime.Now.Ticks

        duration = stop - start
        TestBase.logger.WriteLine((("10,000 points through Connect in " + str((duration / (10000000)))) + " seconds."))

        EarlyBoundTests.AG_MTO.tracks.remove_all()

        # Command File
        start = DateTime.Now.Ticks

        TestBase.Application.begin_update()

        EarlyBoundTests.AG_MTO.tracks.load_command_file(TestBase.GetScenarioFile("MtoPerformance.txt"))

        TestBase.Application.end_update()

        stop = DateTime.Now.Ticks

        duration = stop - start
        TestBase.logger.WriteLine((("10,000 points through OM File in " + str((duration / (10000000)))) + " seconds."))

        EarlyBoundTests.AG_MTO.tracks.remove_all()

        start = DateTime.Now.Ticks

        TestBase.Application.execute_command("BatchGraphics * On")
        TestBase.Application.execute_command("Graphics */MTO/Mto1 BatchGraphics On")

        TestBase.Application.execute_command("SetUnits / EPSEC")
        TestBase.Application.execute_command(
            ("Track */MTO/Mto1 File " + TestBase.GetScenarioFile("MtoPerformance.txt"))
        )

        TestBase.Application.execute_command("BatchGraphics * Off")
        TestBase.Application.execute_command("Graphics */MTO/Mto1 BatchGraphics Off")

        stop = DateTime.Now.Ticks

        duration = stop - start
        TestBase.logger.WriteLine(
            (("10,000 points through Connect File in " + str((duration / (10000000)))) + " seconds.")
        )

        EarlyBoundTests.AG_MTO.tracks.remove_all()

        # Track addition
        start = DateTime.Now.Ticks

        TestBase.Application.begin_update()

        i: int = 0
        while i < 1000:
            EarlyBoundTests.AG_MTO.tracks.add(i)

            i += 1

        TestBase.Application.end_update()

        stop = DateTime.Now.Ticks

        duration = stop - start
        TestBase.logger.WriteLine((("1,000 tracks through OM in " + str((duration / (10000000)))) + " seconds."))

        EarlyBoundTests.AG_MTO.tracks.remove_all()

        start = DateTime.Now.Ticks
        TestBase.Application.execute_command("BatchGraphics * On")
        TestBase.Application.execute_command("Graphics */MTO/Mto1 BatchGraphics On")

        i: int = 0
        while i < 1000:
            TestBase.Application.execute_command(("Track */MTO/Mto1 Add " + str(((i + 1)))))

            i += 1

        TestBase.Application.execute_command("BatchGraphics * Off")
        TestBase.Application.execute_command("Graphics */MTO/Mto1 BatchGraphics Off")
        stop = DateTime.Now.Ticks
        duration = stop - start
        TestBase.logger.WriteLine((("1,000 tracks through Connect in " + str((duration / (10000000)))) + " seconds."))

        EarlyBoundTests.AG_MTO.tracks.remove_all()

        TestBase.Application.execute_command("SetUnits / GREG")
        TestBase.logger.WriteLine("----- Basic MTO Test ----- END -----")

    # endregion

    # region BasicTracks
    @category("Basic Tests")
    def test_BasicTracks(self):
        TestBase.logger.WriteLine("----- BASIC TRACKS ----- BEGIN -----")
        # Tracks
        oTrackCollection: "MTOTrackCollection" = EarlyBoundTests.AG_MTO.tracks
        Assert.assertIsNotNone(oTrackCollection)
        self.Units.reset_units()
        # Count
        TestBase.logger.WriteLine3("\tThe current TrackCollection contains: {0} elements.", oTrackCollection.count)

        iIndex: int = 0
        while iIndex < oTrackCollection.count:
            TestBase.logger.WriteLine9(
                "\t\tElement {0}: ID = {2}, Name = {1}, Interpolate = {3}",
                iIndex,
                oTrackCollection[iIndex].name,
                oTrackCollection[iIndex].identifier,
                oTrackCollection[iIndex].interpolate,
            )

            iIndex += 1

        # Recycling
        TestBase.logger.WriteLine4("\tThe current Recycling flag is: {0}", oTrackCollection.recycling)
        oTrackCollection.recycling = True
        TestBase.logger.WriteLine4("\tThe new Recycling flag is: {0}", oTrackCollection.recycling)
        Assert.assertEqual(True, oTrackCollection.recycling)
        oTrackCollection.recycling = False
        TestBase.logger.WriteLine4("\tThe new Recycling flag is: {0}", oTrackCollection.recycling)
        Assert.assertEqual(False, oTrackCollection.recycling)
        # RemoveAll
        oTrackCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)
        # Add
        oTrack: "MTOTrack" = oTrackCollection.add(123)
        Assert.assertIsNotNone(oTrack)
        Assert.assertEqual(1, oTrackCollection.count)
        # Count
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)

        iIndex: int = 0
        while iIndex < oTrackCollection.count:
            # Item
            TestBase.logger.WriteLine9(
                "\t\tElement {0}: ID = {2}, Name = {1}, Interpolate = {3}",
                iIndex,
                oTrackCollection[iIndex].name,
                oTrackCollection[iIndex].identifier,
                oTrackCollection[iIndex].interpolate,
            )

            iIndex += 1

        # GetTrackFromId
        oTrack = oTrackCollection.get_track_from_identifier(123)
        Assert.assertIsNotNone(oTrack)
        with pytest.raises(Exception):
            oTrackCollection.get_track_from_identifier(12)
        # Interpolate
        oTrack.interpolate = True
        Assert.assertEqual(True, oTrack.interpolate)
        # Name
        oTrack.name = "Track" + str(oTrack.identifier)
        Assert.assertEqual(("Track" + str(oTrack.identifier)), oTrack.name)
        # _NewEnum
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        mtoTrack: "MTOTrack"
        for mtoTrack in oTrackCollection:
            TestBase.logger.WriteLine8(
                "\t\tElement: ID = {1}, Name = {0}, Interpolate = {2}",
                mtoTrack.name,
                mtoTrack.identifier,
                mtoTrack.interpolate,
            )

        # RemoveAt
        with pytest.raises(Exception):
            oTrackCollection.remove_at(12)
        oTrackCollection.remove_at(0)
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)
        # RemoveById
        oTrack = oTrackCollection.add(123)
        with pytest.raises(Exception):
            oTrackCollection.remove_by_identifier(10)
        oTrackCollection.remove_by_identifier(123)
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)
        # Remove
        oTrack = oTrackCollection.add(123)
        oTrackCollection.remove(oTrack)
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)
        # AddTrack
        arTime = ["1 Jul 2005 12:10:00.000", "1 Jul 2005 12:20:00.000", "1 Jul 2005 12:30:00.000"]
        arLatitude = [0.0, 5.0, 10.0]
        arLongitude = [0.0, 5.0, 5.0]
        arAltitude = [50.0, 100.0, 150.0]
        oTrack = oTrackCollection.add_track(1, arTime, arLatitude, arLongitude, arAltitude)
        Assert.assertIsNotNone(oTrack)
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        mtoTrack: "MTOTrack"
        for mtoTrack in oTrackCollection:
            TestBase.logger.WriteLine8(
                "\t\tElement: ID = {1}, Name = {0}, Interpolate = {2}",
                mtoTrack.name,
                mtoTrack.identifier,
                mtoTrack.interpolate,
            )

        Assert.assertEqual(1, oTrackCollection.count)
        # RemoveAll
        oTrackCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)
        # AddTracks
        oTrackCollection.add_tracks(1, 100)
        Assert.assertEqual(100, oTrackCollection.count)
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        # RemoveTracksId
        trackIds = []

        i: int = 0
        while i < 100:
            mtoTrack: "MTOTrack" = oTrackCollection[i]
            trackIds.append(mtoTrack.identifier)

            i = i + 2

        trackIdsArray = trackIds
        oTrackCollection.remove_tracks_by_identifier(trackIdsArray)
        Assert.assertEqual(50, oTrackCollection.count)
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        # RemoveTracks
        tracksList = []

        i: int = 0
        while i < 25:
            mtoTrack: "MTOTrack" = oTrackCollection[i]
            Assert.assertIsNotNone(mtoTrack)
            tracksList.append(mtoTrack)

            i += 1

        tracksArray = tracksList
        oTrackCollection.remove_tracks(tracksArray)
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(25, oTrackCollection.count)

        i: int = 0
        while i < 25:
            mtoTrack: "MTOTrack" = oTrackCollection[i]
            Assert.assertEqual((((i + 26)) * 2), mtoTrack.identifier)

            i += 1

        # RemoveAll
        oTrackCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)
        # LoadCommandFile
        oTrackCollection.load_command_file(TestBase.GetScenarioFile("MtoCmd.txt"))
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        mtoTrack: "MTOTrack"
        for mtoTrack in oTrackCollection:
            TestBase.logger.WriteLine8(
                "\t\tElement: ID = {1}, Name = {0}, Interpolate = {2}",
                mtoTrack.name,
                mtoTrack.identifier,
                mtoTrack.interpolate,
            )

        Assert.assertEqual(2, oTrackCollection.count)
        Assert.assertEqual(2, oTrackCollection[0].points.count)
        with pytest.raises(Exception):
            oTrackCollection.load_command_file("InvalidFileName")

        iIndex: int = 0
        while iIndex < oTrackCollection.count:
            self.BasicTrackPointCollectionHelper(oTrackCollection[iIndex].points)

            iIndex += 1

        TestBase.logger.WriteLine("----- BASIC TRACKS ----- END -----")

    # endregion

    # region BasicTrackPointCollectionHelper
    def BasicTrackPointCollectionHelper(self, oPoints: "MTOTrackPointCollection"):
        TestBase.logger.WriteLine("----- BASIC TRACK POINT COLLECTION ----- BEGIN -----")
        Assert.assertIsNotNone(oPoints)

        # Count
        TestBase.logger.WriteLine3("\tThe current TrackPointCollection contains: {0} elements.", oPoints.count)

        iIndex: int = 0
        while iIndex < oPoints.count:
            # Item
            TestBase.logger.WriteLine10(
                "\t\tElement {0}: Time = {1}, Latitude = {2}, Longitude = {3}, Altitude = {4}",
                iIndex,
                oPoints[iIndex].time,
                oPoints[iIndex].latitude,
                oPoints[iIndex].longitude,
                oPoints[iIndex].altitude,
            )

            iIndex += 1

        with pytest.raises(Exception):
            point: "MTOTrackPoint" = oPoints[oPoints.count]

        # Recycling
        TestBase.logger.WriteLine4("\tThe current Recycling flag is: {0}", oPoints.recycling)
        oPoints.recycling = True
        TestBase.logger.WriteLine4("\tThe new Recycling flag is: {0}", oPoints.recycling)
        Assert.assertEqual(True, oPoints.recycling)
        oPoints.recycling = False
        TestBase.logger.WriteLine4("\tThe new Recycling flag is: {0}", oPoints.recycling)
        Assert.assertEqual(False, oPoints.recycling)

        # RemoveAll
        oPoints.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        Assert.assertEqual(0, oPoints.count)

        # // MTOTrackPoint

        # Add
        oPoint: "MTOTrackPoint" = oPoints.add("12 Jul 2005 12:13:14.000")
        Assert.assertIsNotNone(oPoint)
        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        trackPoint: "MTOTrackPoint"
        for trackPoint in oPoints:
            TestBase.logger.WriteLine9(
                "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                trackPoint.time,
                trackPoint.latitude,
                trackPoint.longitude,
                trackPoint.altitude,
            )

        with pytest.raises(Exception):
            oPoint2: "MTOTrackPoint" = oPoints.add("Bogus")

        # Time
        Assert.assertEqual("12 Jul 2005 12:13:14.000", oPoint.time)

        # Latitude
        oPoint.latitude = 12
        Assert.assertEqual(12, oPoint.latitude)
        with pytest.raises(Exception):
            oPoint.latitude = 123

        # Longitude
        oPoint.longitude = 23
        Assert.assertEqual(23, oPoint.longitude)
        with pytest.raises(Exception):
            oPoint.longitude = 1234

        # Altitude
        oPoint.altitude = 34
        Assert.assertEqual(34, oPoint.altitude)
        with pytest.raises(Exception):
            oPoint.altitude = -1234

        # Id
        id: int = oPoint.identifier

        # Position
        pos: "IPosition" = oPoint.position

        lat: typing.Any = None
        lon: typing.Any = None

        alt: float = 0
        (lat, lon, alt) = pos.query_planetocentric()
        Assert.assertAlmostEqual(11.92, float(lat), delta=0.01)
        Assert.assertAlmostEqual(23.0, float(lon), delta=0.01)
        Assert.assertAlmostEqual(34.0, alt, delta=0.01)

        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        trackPoint: "MTOTrackPoint"
        for trackPoint in oPoints:
            TestBase.logger.WriteLine9(
                "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                trackPoint.time,
                trackPoint.latitude,
                trackPoint.longitude,
                trackPoint.altitude,
            )

        # Extend
        #
        # New rule (AgTrack.c, line 124):
        # Description:
        #      It is an error to add times before the last point if there are times.
        #
        arTime = ["13 Jul 2005 12:20:00.000", "13 Jul 2005 12:30:00.000"]
        arLatitude = [5.0, 10.0]
        arLongitude = [15.0, 25.0]
        arAltitude = [100.0, 150.0]
        oPoints.extend(arTime, arLatitude, arLongitude, arAltitude)
        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        trackPoint: "MTOTrackPoint"
        for trackPoint in oPoints:
            TestBase.logger.WriteLine9(
                "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                trackPoint.time,
                trackPoint.latitude,
                trackPoint.longitude,
                trackPoint.altitude,
            )

        Assert.assertEqual(3, oPoints.count)

        # different size arrays
        arTime2 = ["13 Jul 2005 12:20:00.000", "13 Jul 2005 12:30:00.000"]
        arLatitude2 = [5.0, 10.0, 15]
        arLongitude2 = [15.0, 25.0]
        arAltitude2 = [100.0, 150.0]
        with pytest.raises(Exception):
            oPoints.extend(arTime2, arLatitude2, arLongitude2, arAltitude2)

        # RemoveAt
        oPoints.remove_at(0)
        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        trackPoint: "MTOTrackPoint"
        for trackPoint in oPoints:
            TestBase.logger.WriteLine9(
                "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                trackPoint.time,
                trackPoint.latitude,
                trackPoint.longitude,
                trackPoint.altitude,
            )

        Assert.assertEqual(2, oPoints.count)
        with pytest.raises(Exception):
            oPoints.remove_at(oPoints.count)

        # RemoveAll
        oPoints.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        trackPoint: "MTOTrackPoint"
        for trackPoint in oPoints:
            TestBase.logger.WriteLine9(
                "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                trackPoint.time,
                trackPoint.latitude,
                trackPoint.longitude,
                trackPoint.altitude,
            )

        Assert.assertEqual(0, oPoints.count)

        # LoadPoints
        oPoints.load_points(TestBase.GetScenarioFile("TestEph.e"))
        Assert.assertEqual(11, oPoints.count)
        with pytest.raises(Exception):
            oPoints.load_points("InvalidFileName")
        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        trackPoint: "MTOTrackPoint"
        for trackPoint in oPoints:
            TestBase.logger.WriteLine9(
                "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                trackPoint.time,
                trackPoint.latitude,
                trackPoint.longitude,
                trackPoint.altitude,
            )

        # AddPoint
        oPoint = oPoints.add_point("12 Jul 2005 12:13:14.000", 12, 34, 56)
        Assert.assertIsNotNone(oPoint)
        Assert.assertEqual(12, oPoints.count)
        Assert.assertEqual("12 Jul 2005 12:13:14.000", oPoint.time)
        Assert.assertEqual(12, oPoint.latitude)
        Assert.assertEqual(34, oPoint.longitude)
        Assert.assertEqual(56, oPoint.altitude)
        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        trackPoint: "MTOTrackPoint"
        for trackPoint in oPoints:
            TestBase.logger.WriteLine9(
                "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                trackPoint.time,
                trackPoint.latitude,
                trackPoint.longitude,
                trackPoint.altitude,
            )

        with pytest.raises(Exception):
            oPoints.add_point("bogus time", 12, 34, 56)

        # InsertPoint
        oPoints.insert_point("12 Jul 2005 12:13:15.000", 12, 34, 56)
        TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oPoints.count)
        trackPoint: "MTOTrackPoint"
        for trackPoint in oPoints:
            TestBase.logger.WriteLine9(
                "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                trackPoint.time,
                trackPoint.latitude,
                trackPoint.longitude,
                trackPoint.altitude,
            )

        with pytest.raises(Exception):
            oPoints.insert_point("bogus time", 12, 34, 56)

        TestBase.logger.WriteLine("----- BASIC TRACK POINT COLLECTION ----- END -----")

    # endregion

    # region BasicTrackId
    @category("Graphics Tests")
    def test_BasicTrackId(self):
        oTrackCollection: "MTOTrackCollection" = EarlyBoundTests.AG_MTO.tracks
        oTrackCollection.remove_all()
        oTrack: "MTOTrack" = oTrackCollection.add(0)
        Assert.assertEqual(0, oTrack.identifier)
        oTrack1: "MTOTrack" = oTrackCollection.add(1)
        Assert.assertEqual(1, oTrack1.identifier)
        oTrack1.points.add("12 Jul 2005 12:13:14.000")

        oGfxTrackCollection: "MTOGraphics2DTrackCollection" = EarlyBoundTests.AG_MTO.graphics.tracks
        oGfxTrack: "MTOGraphics2DTrack" = oGfxTrackCollection.get_track_from_identifier(oTrack.identifier)
        Assert.assertEqual(oTrack.identifier, oGfxTrack.identifier)
        TestBase.logger.WriteLine7("TrackID = {0}, oGfxTrack = {1}", oTrack.identifier, oGfxTrack.identifier)

        oVOTrackCollection: "MTOGraphics3DTrackCollection" = EarlyBoundTests.AG_MTO.graphics_3d.tracks

        oVOTrack: "MTOGraphics3DTrack" = oVOTrackCollection.get_track_from_identifier(oGfxTrack.identifier)
        Assert.assertEqual(oGfxTrack.identifier, oVOTrack.identifier)
        TestBase.logger.WriteLine7("oGfxTrack = {0}, oVOTrack = {1}", oGfxTrack.identifier, oVOTrack.identifier)

        Assert.assertEqual(oTrack.identifier, oVOTrack.identifier)
        TestBase.logger.WriteLine7("oTrack = {0}, oVOTrack = {1}", oTrack.identifier, oVOTrack.identifier)

        oTrackFromId: "MTOTrack" = oTrackCollection.get_track_from_identifier(1)
        TestBase.logger.WriteLine3("oTrackFromId = {0}", oTrackFromId.identifier)

        Assert.assertEqual(1, oTrackFromId.identifier)
        Assert.assertEqual(1, oTrackFromId.points.count)

        oTrackCollection.remove_all()

    # endregion

    # region BasicTrackRecycling
    @category("Graphics Tests")
    def test_BasicTrackRecycling(self):
        TestBase.logger.WriteLine("----- Basic MTO Test ----- BEGIN -----")

        oTrackCollection: "MTOTrackCollection" = EarlyBoundTests.AG_MTO.tracks
        oTrackCollection.remove_all()
        oTrackCollection.recycling = True

        i: int = 0
        while i < 50:
            track: "MTOTrack" = oTrackCollection.add(i)
            track.interpolate = True
            track.name = str(i)

            i += 1

        oTrackCollectionGfx: "MTOGraphics2DTrackCollection" = EarlyBoundTests.AG_MTO.graphics.tracks
        oTrackCollectionGfx.recycling = True

        oTrackCollectionVO: "MTOGraphics3DTrackCollection" = EarlyBoundTests.AG_MTO.graphics_3d.tracks
        oTrackCollectionVO.recycling = True

        self.Units.set_current_unit("DateFormat", "EpSec")

        i: int = 0
        while i < oTrackCollection.count:
            pointCollection: "MTOTrackPointCollection" = oTrackCollection[i].points
            pointCollection.recycling = True

            j: int = 0
            while j < 5:
                point: "MTOTrackPoint" = pointCollection.add(i)
                point.altitude = j

                j += 1

            i += 1

        i: int = 0
        while i < oTrackCollectionGfx.count:
            oTrackCollectionGfx[i].color = Colors.from_argb(i)
            oTrackCollectionGfx[i].show_graphics = True

            i += 1

        i: int = 0
        while i < oTrackCollectionVO.count:
            oTrackCollectionVO[i].show_graphics = True
            oTrackCollectionVO[i].marker.pixel_size = 2

            i += 1

        EarlyBoundTests.AG_MTO.tracks.remove_all()
        TestBase.logger.WriteLine("----- Basic MTO Test ----- END -----")

    # endregion

    # region BasicGlobalTrack
    @category("Basic Tests")
    def test_BasicGlobalTrack(self):
        TestBase.logger.WriteLine("----- BASIC GLOBAL TRACK OPTIONS ----- BEGIN -----")
        # GlobalTrackOptions
        oOptions: "MTOGlobalTrackOptions" = EarlyBoundTests.AG_MTO.global_track_options
        Assert.assertIsNotNone(oOptions)
        # BlockSize
        TestBase.logger.WriteLine3("\tThe current BlockSize is: {0}", oOptions.block_size)
        oOptions.block_size = 10
        TestBase.logger.WriteLine3("\tThe new BlockSize is: {0}", oOptions.block_size)
        Assert.assertEqual(10, oOptions.block_size)
        # SaveTrackData
        TestBase.logger.WriteLine4("\tThe current SaveTrackData is: {0}", oOptions.save_track_data)
        oOptions.save_track_data = False
        TestBase.logger.WriteLine4("\tThe new SaveTrackData is: {0}", oOptions.save_track_data)
        Assert.assertEqual(False, oOptions.save_track_data)
        oOptions.save_track_data = True
        TestBase.logger.WriteLine4("\tThe new SaveTrackData is: {0}", oOptions.save_track_data)
        Assert.assertEqual(True, oOptions.save_track_data)
        # AltitudeRef (MEAN_SEA_LEVEL)
        TestBase.logger.WriteLine6("\tThe current AltitudeRef is: {0}", oOptions.altitude_reference)
        oTrack: "MTOTrack" = EarlyBoundTests.AG_MTO.tracks.add(0)
        oOptions.altitude_reference = AltitudeReferenceType.MEAN_SEA_LEVEL
        TestBase.logger.WriteLine6("\tThe new AltitudeRef is: {0}", oOptions.altitude_reference)
        Assert.assertEqual(AltitudeReferenceType.MEAN_SEA_LEVEL, oOptions.altitude_reference)
        oPoint: "MTOTrackPoint" = oTrack.points.add_point("1 Jul 2005 12:30:00.000", 10, 10, 200)
        TestBase.logger.WriteLine6("\t\tThe new Altitude is: {0}", oPoint.altitude)
        # AltitudeRef (TERRAIN)
        oOptions.altitude_reference = AltitudeReferenceType.TERRAIN
        TestBase.logger.WriteLine6("\tThe new AltitudeRef is: {0}", oOptions.altitude_reference)
        Assert.assertEqual(AltitudeReferenceType.TERRAIN, oOptions.altitude_reference)
        oPoint = oTrack.points.add_point("1 Jul 2005 12:40:00.000", 10, 10, 200)
        TestBase.logger.WriteLine6("\t\tThe new Altitude is: {0}", oPoint.altitude)
        # AltitudeRef (WGS84)
        oOptions.altitude_reference = AltitudeReferenceType.WGS84
        TestBase.logger.WriteLine6("\tThe new AltitudeRef is: {0}", oOptions.altitude_reference)
        Assert.assertEqual(AltitudeReferenceType.WGS84, oOptions.altitude_reference)
        oPoint = oTrack.points.add_point("1 Jul 2005 12:50:00.000", 10, 10, 200)
        TestBase.logger.WriteLine6("\t\tThe new Altitude is: {0}", oPoint.altitude)
        # IsStatic (true)
        TestBase.logger.WriteLine4("\tThe current IsStatic is: {0}", oOptions.is_static)
        oOptions.is_static = True
        TestBase.logger.WriteLine4("\tThe new IsStatic is: {0}", oOptions.is_static)
        Assert.assertEqual(True, oOptions.is_static)
        with pytest.raises(Exception):
            oOptions.is_static = False
        EarlyBoundTests.AG_MTO.tracks.remove_all()
        Assert.assertEqual(0, EarlyBoundTests.AG_MTO.tracks.count)
        # IsStatic (false)
        oOptions.is_static = False
        TestBase.logger.WriteLine4("\tThe new IsStatic is: {0}", oOptions.is_static)
        Assert.assertEqual(False, oOptions.is_static)
        # ComputationTrackId
        TestBase.logger.WriteLine3("\tThe current ComputationTrackId is: {0}", oOptions.computation_track_identifier)
        with pytest.raises(Exception):
            oOptions.computation_track_identifier = 0
        EarlyBoundTests.AG_MTO.tracks.add(0)
        Assert.assertEqual(1, EarlyBoundTests.AG_MTO.tracks.count)
        oOptions.computation_track_identifier = 0
        TestBase.logger.WriteLine3("\tThe new ComputationTrackId is: {0}", oOptions.computation_track_identifier)
        Assert.assertEqual(0, oOptions.computation_track_identifier)
        oTrack = EarlyBoundTests.AG_MTO.tracks.add(1)
        oOptions.computation_track_identifier = oTrack.identifier
        TestBase.logger.WriteLine3("\tThe new ComputationTrackId is: {0}", oOptions.computation_track_identifier)
        Assert.assertEqual(oTrack.identifier, oOptions.computation_track_identifier)
        EarlyBoundTests.AG_MTO.tracks.remove_all()
        TestBase.logger.WriteLine("----- BASIC GLOBAL TRACK OPTIONS ----- END -----")

    # endregion

    # region BasicDefaultTrack
    @category("Basic Tests")
    def test_BasicDefaultTrack(self):
        TestBase.logger.WriteLine("----- BASIC DEFAULT TRACK ----- BEGIN -----")
        oDefault: "MTODefaultTrack" = EarlyBoundTests.AG_MTO.default_track
        Assert.assertIsNotNone(oDefault)
        # Interpolate
        TestBase.logger.WriteLine4("\tThe current Interpolate flag is: {0}", oDefault.interpolate)
        oDefault.interpolate = False
        TestBase.logger.WriteLine4("\tThe new Interpolate flag is: {0}", oDefault.interpolate)
        Assert.assertEqual(False, oDefault.interpolate)
        oDefault.interpolate = True
        TestBase.logger.WriteLine4("\tThe new Interpolate flag is: {0}", oDefault.interpolate)
        Assert.assertEqual(True, oDefault.interpolate)
        # Name
        TestBase.logger.WriteLine5("\tThe current Name is: {0}", oDefault.name)
        oDefault.name = "Default Name"
        TestBase.logger.WriteLine5("\tThe new Name is: {0}", oDefault.name)
        Assert.assertEqual("Default Name", oDefault.name)
        # verification
        oTrack: "MTOTrack" = EarlyBoundTests.AG_MTO.tracks.add(0)
        Assert.assertEqual(oDefault.interpolate, oTrack.interpolate)
        Assert.assertEqual(oDefault.name, oTrack.name)
        EarlyBoundTests.AG_MTO.tracks.remove_all()
        Assert.assertEqual(0, EarlyBoundTests.AG_MTO.tracks.count)
        TestBase.logger.WriteLine("----- BASIC DEFAULT TRACK ----- END -----")

    # endregion

    # region BasicTracksWithLlaArrays
    @category("Basic Tests")
    def test_BasicTracksWithLlaArrays(self):
        TestBase.logger.WriteLine("----- BASIC TRACKS WITH LLA ARRAYS ----- BEGIN -----")

        # Create a new MTO object
        mto2: "MTO" = MTO(TestBase.Application.current_scenario.children.new(STKObjectType.MTO, "Mto2"))

        # Tracks
        oTrackCollection: "MTOTrackCollection" = mto2.tracks
        Assert.assertIsNotNone(oTrackCollection)
        self.Units.reset_units()

        # Count
        TestBase.logger.WriteLine3("\tThe current TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        # AddTracksWithPosData
        arTrackIdsAdd = [1, 3, 5]
        arNumPtsPerTrackAdd = [2, 1, 3]
        arTimeAdd = [
            "1 Jul 2005 12:00:00.000",
            "1 Jul 2005 12:10:00.000",
            "1 Jul 2005 12:05:00.000",
            "1 Jul 2005 12:00:00.000",
            "1 Jul 2005 12:10:00.000",
            "1 Jul 2005 12:30:00.000",
        ]
        arLatitudeAdd = [0.0, 10.0, 10.0, 0.0, 10.0, 0.0]
        arLongitudeAdd = [0.0, 10.0, 0.0, 10.0, 20.0, 30.0]
        arAltitudeAdd = [0.0, 1000.0, 500.0, 1000.0, 0.0, 10000.0]
        oTrackCollection.add_tracks_with_position_data(
            arTrackIdsAdd,
            arNumPtsPerTrackAdd,
            MTOInputDataType.DETIC,
            arTimeAdd,
            arLatitudeAdd,
            arLongitudeAdd,
            arAltitudeAdd,
        )
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(3, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId5: "MTOTrack" = oTrackCollection.get_track_from_identifier(5)
        Assert.assertAlmostEqual(0.0, trackId5.points[2].latitude, delta=Math2.Epsilon12)
        Assert.assertAlmostEqual(30.0, trackId5.points[2].longitude, delta=Math2.Epsilon12)
        Assert.assertAlmostEqual(10000.0, trackId5.points[2].altitude, delta=Math2.Epsilon12)

        # ExtendTracksWithPosData
        arTrackIdsExtend = [1, 3, 6]
        arNumPtsPerTrackExtend = [2, 1, 2]
        arTimeExtend = [
            "1 Jul 2005 12:20:00.000",
            "1 Jul 2005 12:30:00.000",
            "1 Jul 2005 12:15:00.000",
            "1 Jul 2005 12:40:00.000",
            "1 Jul 2005 12:50:00.000",
        ]
        arLatitudeExtend = [20.0, 30.0, 40.0, 10.0, 20.0]
        arLongitudeExtend = [0.0, -10.0, 50.0, 30.0, 40.0]
        arAltitudeExtend = [0.0, 1000.0, 1500.0, 2000.0, 20000.0]
        oTrackCollection.extend_tracks_with_position_data(
            arTrackIdsExtend,
            arNumPtsPerTrackExtend,
            MTOInputDataType.DETIC,
            arTimeExtend,
            arLatitudeExtend,
            arLongitudeExtend,
            arAltitudeExtend,
        )
        TestBase.logger.WriteLine3("\tThe extended TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(4, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId6: "MTOTrack" = oTrackCollection.get_track_from_identifier(6)
        Assert.assertAlmostEqual(20.0, trackId6.points[1].latitude, delta=Math2.Epsilon12)
        Assert.assertAlmostEqual(40.0, trackId6.points[1].longitude, delta=Math2.Epsilon12)
        Assert.assertAlmostEqual(20000.0, trackId6.points[1].altitude, delta=Math2.Epsilon12)

        # Remove tracks
        arTrackIdsRemove = [1, 3, 6]
        oTrackCollection.remove_tracks_by_identifier(arTrackIdsRemove)
        Assert.assertEqual(1, oTrackCollection.count)
        oTrackCollection.remove_all()
        Assert.assertEqual(0, oTrackCollection.count)

        # AddTracksWithPosData using different units
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "ft")
        TestBase.Application.units_preferences.set_current_unit("AngleUnit", "rad")

        arTimeAdd2 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", arTimeAdd)
        arLatitudeAdd2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "AngleUnit", "deg", "rad", arLatitudeAdd
        )
        arLongitudeAdd2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "AngleUnit", "deg", "rad", arLongitudeAdd
        )
        arAltitudeAdd2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arAltitudeAdd
        )
        oTrackCollection.add_tracks_with_position_data(
            arTrackIdsAdd,
            arNumPtsPerTrackAdd,
            MTOInputDataType.DETIC,
            arTimeAdd2,
            arLatitudeAdd2,
            arLongitudeAdd2,
            arAltitudeAdd2,
        )
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(3, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId5 = oTrackCollection.get_track_from_identifier(5)
        Assert.assertAlmostEqual(
            0.0,
            TestBase.Application.conversion_utility.convert_quantity(
                "AngleUnit", "rad", "deg", trackId5.points[2].latitude
            ),
            delta=Math2.Epsilon12,
        )
        Assert.assertAlmostEqual(
            30.0,
            TestBase.Application.conversion_utility.convert_quantity(
                "AngleUnit", "rad", "deg", trackId5.points[2].longitude
            ),
            delta=Math2.Epsilon12,
        )
        Assert.assertAlmostEqual(
            10000.0,
            TestBase.Application.conversion_utility.convert_quantity(
                "DistanceUnit", "ft", "Km", trackId5.points[2].altitude
            ),
            delta=Math2.Epsilon12,
        )

        # ExtendTracksWithPosData using different units
        arTimeExtend2 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", arTimeExtend)
        arLatitudeExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "AngleUnit", "deg", "rad", arLatitudeExtend
        )
        arLongitudeExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "AngleUnit", "deg", "rad", arLongitudeExtend
        )
        arAltitudeExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arAltitudeExtend
        )
        oTrackCollection.extend_tracks_with_position_data(
            arTrackIdsExtend,
            arNumPtsPerTrackExtend,
            MTOInputDataType.DETIC,
            arTimeExtend2,
            arLatitudeExtend2,
            arLongitudeExtend2,
            arAltitudeExtend2,
        )
        TestBase.logger.WriteLine3("\tThe extended TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(4, oTrackCollection.count)

        trackId6 = oTrackCollection.get_track_from_identifier(6)
        Assert.assertAlmostEqual(
            20.0,
            TestBase.Application.conversion_utility.convert_quantity(
                "AngleUnit", "rad", "deg", trackId6.points[1].latitude
            ),
            delta=Math2.Epsilon12,
        )
        Assert.assertAlmostEqual(
            40.0,
            TestBase.Application.conversion_utility.convert_quantity(
                "AngleUnit", "rad", "deg", trackId6.points[1].longitude
            ),
            delta=Math2.Epsilon12,
        )
        Assert.assertAlmostEqual(
            20000.0,
            TestBase.Application.conversion_utility.convert_quantity(
                "DistanceUnit", "ft", "Km", trackId6.points[1].altitude
            ),
            delta=Math2.Epsilon12,
        )

        # Switch back to default units
        self.Units.reset_units()

        # RemoveAll
        oTrackCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        # Remove Mto2
        TestBase.Application.current_scenario.children.unload(STKObjectType.MTO, "Mto2")

        TestBase.logger.WriteLine("----- BASIC TRACKS WITH LLA ARRAYS ----- END -----")

    # endregion

    # region BasicTracksWithCbfArrays
    @category("Basic Tests")
    def test_BasicTracksWithCbfArrays(self):
        TestBase.logger.WriteLine("----- BASIC TRACKS WITH CBF ARRAYS ----- BEGIN -----")

        # Create a new MTO object
        mto2: "MTO" = MTO(TestBase.Application.current_scenario.children.new(STKObjectType.MTO, "Mto2"))

        # Tracks
        oTrackCollection: "MTOTrackCollection" = mto2.tracks
        Assert.assertIsNotNone(oTrackCollection)
        self.Units.reset_units()

        # Count
        TestBase.logger.WriteLine3("\tThe current TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        # AddTracksWithPosData
        arTrackIdsAdd = [1, 3, 5]
        arNumPtsPerTrackAdd = [2, 1, 3]
        arTimeAdd = [
            "1 Jul 2005 12:00:00.000",
            "1 Jul 2005 12:10:00.000",
            "1 Jul 2005 12:05:00.000",
            "1 Jul 2005 12:00:00.000",
            "1 Jul 2005 12:10:00.000",
            "1 Jul 2005 12:30:00.000",
        ]
        arXAdd = [7000.0, 7500.0, 7200.0, 7000.0, 7700.0, 7900]
        arYAdd = [0.0, 1000.0, -1000.0, -5000.0, -3000.0, 500.0]
        arZAdd = [0.0, 0.0, 1000.0, 7000.0, 900.0, 10000.0]
        oTrackCollection.add_tracks_with_position_data(
            arTrackIdsAdd,
            arNumPtsPerTrackAdd,
            MTOInputDataType.CARTESIAN_IN_CENTRAL_BODY_FIXED,
            arTimeAdd,
            arXAdd,
            arYAdd,
            arZAdd,
        )
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(3, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId5: "MTOTrack" = oTrackCollection.get_track_from_identifier(5)

        x: float = 0
        y: float = 0
        z: float = 0

        (x, y, z) = trackId5.points[2].position.query_cartesian()
        Assert.assertAlmostEqual(7900.0, x, delta=Math2.Epsilon6)
        Assert.assertAlmostEqual(500.0, y, delta=Math2.Epsilon6)
        Assert.assertAlmostEqual(10000.0, z, delta=Math2.Epsilon6)

        # ExtendTracksWithPosData
        arTrackIdsExtend = [1, 3, 6]
        arNumPtsPerTrackExtend = [2, 1, 2]
        arTimeExtend = [
            "1 Jul 2005 12:20:00.000",
            "1 Jul 2005 12:30:00.000",
            "1 Jul 2005 12:15:00.000",
            "1 Jul 2005 12:40:00.000",
            "1 Jul 2005 12:50:00.000",
        ]
        arXExtend = [10000.0, 11000.0, 12000.0, 13000.0, 14000.0]
        arYExtend = [0.0, 0.0, 0.0, 0.0, 0.0]
        arZExtend = [3000.0, 4000.0, 5000.0, 6000.0, 70000.0]
        oTrackCollection.extend_tracks_with_position_data(
            arTrackIdsExtend,
            arNumPtsPerTrackExtend,
            MTOInputDataType.CARTESIAN_IN_CENTRAL_BODY_FIXED,
            arTimeExtend,
            arXExtend,
            arYExtend,
            arZExtend,
        )
        TestBase.logger.WriteLine3("\tThe extended TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(4, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId6: "MTOTrack" = oTrackCollection.get_track_from_identifier(6)
        (x, y, z) = trackId6.points[1].position.query_cartesian()
        Assert.assertAlmostEqual(14000.0, x, delta=Math2.Epsilon6)
        Assert.assertAlmostEqual(0.0, y, delta=Math2.Epsilon6)
        Assert.assertAlmostEqual(70000.0, z, delta=Math2.Epsilon6)

        # Remove tracks
        arTrackIdsRemove = [1, 3, 6]
        oTrackCollection.remove_tracks_by_identifier(arTrackIdsRemove)
        Assert.assertEqual(1, oTrackCollection.count)
        oTrackCollection.remove_all()
        Assert.assertEqual(0, oTrackCollection.count)

        # AddTracksWithPosData using different units
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "ft")

        arTimeAdd2 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", arTimeAdd)
        arXAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arXAdd)
        arYAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arYAdd)
        arZAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arZAdd)
        oTrackCollection.add_tracks_with_position_data(
            arTrackIdsAdd,
            arNumPtsPerTrackAdd,
            MTOInputDataType.CARTESIAN_IN_CENTRAL_BODY_FIXED,
            arTimeAdd2,
            arXAdd2,
            arYAdd2,
            arZAdd2,
        )
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(3, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId5 = oTrackCollection.get_track_from_identifier(5)
        (x, y, z) = trackId5.points[2].position.query_cartesian()
        Assert.assertAlmostEqual(
            7900.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", x),
            delta=Math2.Epsilon6,
        )
        Assert.assertAlmostEqual(
            500.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", y),
            delta=Math2.Epsilon6,
        )
        Assert.assertAlmostEqual(
            10000.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", z),
            delta=Math2.Epsilon6,
        )

        # ExtendTracksWithPosData using different units
        arTimeExtend2 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", arTimeExtend)
        arXExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arXExtend
        )
        arYExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arYExtend
        )
        arZExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arZExtend
        )
        oTrackCollection.extend_tracks_with_position_data(
            arTrackIdsExtend,
            arNumPtsPerTrackExtend,
            MTOInputDataType.CARTESIAN_IN_CENTRAL_BODY_FIXED,
            arTimeExtend2,
            arXExtend2,
            arYExtend2,
            arZExtend2,
        )
        TestBase.logger.WriteLine3("\tThe extended TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(4, oTrackCollection.count)

        trackId6 = oTrackCollection.get_track_from_identifier(6)
        (x, y, z) = trackId6.points[1].position.query_cartesian()
        Assert.assertAlmostEqual(
            14000.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", x),
            delta=Math2.Epsilon6,
        )
        Assert.assertAlmostEqual(
            0.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", y),
            delta=Math2.Epsilon6,
        )
        Assert.assertAlmostEqual(
            70000.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", z),
            delta=Math2.Epsilon6,
        )

        # Switch back to default units
        self.Units.reset_units()

        # RemoveAll
        oTrackCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        # Remove Mto2
        TestBase.Application.current_scenario.children.unload(STKObjectType.MTO, "Mto2")

        TestBase.logger.WriteLine("----- BASIC TRACKS WITH CBF ARRAYS ----- END -----")

    # endregion

    # region BasicTracksWithVGTArrays_ClearInputDataVGTSystem
    @category("Basic Tests")
    def test_BasicTracksWithVGTArrays_ClearInputDataVGTSystem(self):
        TestBase.logger.WriteLine("----- BASIC TRACKS WITH VGT ARRAYS ----- BEGIN -----")

        # Create a new MTO object
        mto2: "MTO" = MTO(TestBase.Application.current_scenario.children.new(STKObjectType.MTO, "Mto2"))

        # Tracks
        oTrackCollection: "MTOTrackCollection" = mto2.tracks
        Assert.assertIsNotNone(oTrackCollection)
        self.Units.reset_units()

        # Count
        TestBase.logger.WriteLine3("\tThe current TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        oTrackCollection.clear_input_data_system()  # *****************************************

        # AddTracksWithPosData
        arTrackIdsAdd = [1, 3, 5]
        arNumPtsPerTrackAdd = [2, 1, 3]
        arTimeAdd = [
            "1 Jul 2005 12:00:00.000",
            "1 Jul 2005 12:10:00.000",
            "1 Jul 2005 12:05:00.000",
            "1 Jul 2005 12:00:00.000",
            "1 Jul 2005 12:10:00.000",
            "1 Jul 2005 12:30:00.000",
        ]
        arXAdd = [7000.0, 7500.0, 7200.0, 7000.0, 7700.0, 7900]
        arYAdd = [0.0, 1000.0, -1000.0, -5000.0, -3000.0, 500.0]
        arZAdd = [0.0, 0.0, 1000.0, 7000.0, 900.0, 10000.0]
        oTrackCollection.add_tracks_with_position_data(
            arTrackIdsAdd,
            arNumPtsPerTrackAdd,
            MTOInputDataType.CARTESIAN_IN_VECTOR_GEOMETRY_TOOL_SYSTEM,
            arTimeAdd,
            arXAdd,
            arYAdd,
            arZAdd,
        )
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(3, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId5: "MTOTrack" = oTrackCollection.get_track_from_identifier(5)

        x: float = 0
        y: float = 0
        z: float = 0

        (x, y, z) = trackId5.points[2].position.query_cartesian()
        Assert.assertAlmostEqual(7900.0, x, delta=Math2.Epsilon6)
        Assert.assertAlmostEqual(500.0, y, delta=Math2.Epsilon6)
        Assert.assertAlmostEqual(10000.0, z, delta=Math2.Epsilon6)

        # ExtendTracksWithPosData
        arTrackIdsExtend = [1, 3, 6]
        arNumPtsPerTrackExtend = [2, 1, 2]
        arTimeExtend = [
            "1 Jul 2005 12:20:00.000",
            "1 Jul 2005 12:30:00.000",
            "1 Jul 2005 12:15:00.000",
            "1 Jul 2005 12:40:00.000",
            "1 Jul 2005 12:50:00.000",
        ]
        arXExtend = [10000.0, 11000.0, 12000.0, 13000.0, 14000.0]
        arYExtend = [0.0, 0.0, 0.0, 0.0, 0.0]
        arZExtend = [3000.0, 4000.0, 5000.0, 6000.0, 70000.0]
        oTrackCollection.extend_tracks_with_position_data(
            arTrackIdsExtend,
            arNumPtsPerTrackExtend,
            MTOInputDataType.CARTESIAN_IN_VECTOR_GEOMETRY_TOOL_SYSTEM,
            arTimeExtend,
            arXExtend,
            arYExtend,
            arZExtend,
        )
        TestBase.logger.WriteLine3("\tThe extended TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(4, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId6: "MTOTrack" = oTrackCollection.get_track_from_identifier(6)
        (x, y, z) = trackId6.points[1].position.query_cartesian()
        Assert.assertAlmostEqual(14000.0, x, delta=Math2.Epsilon6)
        Assert.assertAlmostEqual(0.0, y, delta=Math2.Epsilon6)
        Assert.assertAlmostEqual(70000.0, z, delta=Math2.Epsilon6)

        # Remove tracks
        arTrackIdsRemove = [1, 3, 6]
        oTrackCollection.remove_tracks_by_identifier(arTrackIdsRemove)
        Assert.assertEqual(1, oTrackCollection.count)
        oTrackCollection.remove_all()
        Assert.assertEqual(0, oTrackCollection.count)

        # AddTracksWithPosData using different units
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "ft")

        arTimeAdd2 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", arTimeAdd)
        arXAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arXAdd)
        arYAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arYAdd)
        arZAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arZAdd)
        oTrackCollection.add_tracks_with_position_data(
            arTrackIdsAdd,
            arNumPtsPerTrackAdd,
            MTOInputDataType.CARTESIAN_IN_VECTOR_GEOMETRY_TOOL_SYSTEM,
            arTimeAdd2,
            arXAdd2,
            arYAdd2,
            arZAdd2,
        )
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(3, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId5 = oTrackCollection.get_track_from_identifier(5)
        (x, y, z) = trackId5.points[2].position.query_cartesian()
        Assert.assertAlmostEqual(
            7900.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", x),
            delta=Math2.Epsilon6,
        )
        Assert.assertAlmostEqual(
            500.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", y),
            delta=Math2.Epsilon6,
        )
        Assert.assertAlmostEqual(
            10000.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", z),
            delta=Math2.Epsilon6,
        )

        # ExtendTracksWithPosData using different units
        arTimeExtend2 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", arTimeExtend)
        arXExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arXExtend
        )
        arYExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arYExtend
        )
        arZExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arZExtend
        )
        oTrackCollection.extend_tracks_with_position_data(
            arTrackIdsExtend,
            arNumPtsPerTrackExtend,
            MTOInputDataType.CARTESIAN_IN_VECTOR_GEOMETRY_TOOL_SYSTEM,
            arTimeExtend2,
            arXExtend2,
            arYExtend2,
            arZExtend2,
        )
        TestBase.logger.WriteLine3("\tThe extended TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(4, oTrackCollection.count)

        trackId6 = oTrackCollection.get_track_from_identifier(6)
        (x, y, z) = trackId6.points[1].position.query_cartesian()
        Assert.assertAlmostEqual(
            14000.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", x),
            delta=Math2.Epsilon6,
        )
        Assert.assertAlmostEqual(
            0.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", y),
            delta=Math2.Epsilon6,
        )
        Assert.assertAlmostEqual(
            70000.0,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", z),
            delta=Math2.Epsilon6,
        )

        # Switch back to default units
        self.Units.reset_units()

        # RemoveAll
        oTrackCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        # Remove Mto2
        TestBase.Application.current_scenario.children.unload(STKObjectType.MTO, "Mto2")

        TestBase.logger.WriteLine("----- BASIC TRACKS WITH VGT ARRAYS ----- END -----")

    # endregion

    # region BasicTracksWithVGTArrays_SetInputDataVGTSystem
    @category("Basic Tests")
    def test_BasicTracksWithVGTArrays_SetInputDataVGTSystem(self):
        TestBase.logger.WriteLine("----- BASIC TRACKS WITH VGT ARRAYS ----- BEGIN -----")

        # Create a new MTO object
        mto2: "MTO" = MTO(TestBase.Application.current_scenario.children.new(STKObjectType.MTO, "Mto2"))

        # Tracks
        oTrackCollection: "MTOTrackCollection" = mto2.tracks
        Assert.assertIsNotNone(oTrackCollection)
        self.Units.reset_units()

        # Count
        TestBase.logger.WriteLine3("\tThe current TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        oTrackCollection.set_input_data_vector_geometry_tool_system_name(
            "Satellite/Satellite1 Body System"
        )  # ****************************

        # AddTracksWithPosData
        arTrackIdsAdd = [1, 3, 5]
        arNumPtsPerTrackAdd = [2, 1, 3]
        arTimeAdd = [
            "1 Jul 2005 12:00:00.000",
            "1 Jul 2005 12:10:00.000",
            "1 Jul 2005 12:05:00.000",
            "1 Jul 2005 12:00:00.000",
            "1 Jul 2005 12:10:00.000",
            "1 Jul 2005 12:30:00.000",
        ]
        arXAdd = [7000.0, 7500.0, 7200.0, 7000.0, 7700.0, 7900]
        arYAdd = [0.0, 1000.0, -1000.0, -5000.0, -3000.0, 500.0]
        arZAdd = [0.0, 0.0, 1000.0, 7000.0, 900.0, 10000.0]
        oTrackCollection.add_tracks_with_position_data(
            arTrackIdsAdd,
            arNumPtsPerTrackAdd,
            MTOInputDataType.CARTESIAN_IN_VECTOR_GEOMETRY_TOOL_SYSTEM,
            arTimeAdd,
            arXAdd,
            arYAdd,
            arZAdd,
        )
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(3, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId5: "MTOTrack" = oTrackCollection.get_track_from_identifier(5)

        x: float = 0
        y: float = 0
        z: float = 0

        (x, y, z) = trackId5.points[2].position.query_cartesian()
        # Debug - to compare LLA values to GUI
        # object lat, lon;
        # double alt;
        # trackId5.Points[2].Position.QueryPlanetocentric(out lat, out lon, out alt);
        # System.Windows.Forms.MessageBox.Show(lat.ToString());
        # System.Windows.Forms.MessageBox.Show(lon.ToString());
        # System.Windows.Forms.MessageBox.Show(alt.ToString());

        Assert.assertAlmostEqual(22188.33, x, delta=0.01)
        Assert.assertAlmostEqual(48691.15, y, delta=0.01)
        Assert.assertAlmostEqual(-522.45, z, delta=0.01)

        # ExtendTracksWithPosData
        arTrackIdsExtend = [1, 3, 6]
        arNumPtsPerTrackExtend = [2, 1, 2]
        arTimeExtend = [
            "1 Jul 2005 12:20:00.000",
            "1 Jul 2005 12:30:00.000",
            "1 Jul 2005 12:15:00.000",
            "1 Jul 2005 12:40:00.000",
            "1 Jul 2005 12:50:00.000",
        ]
        arXExtend = [10000.0, 11000.0, 12000.0, 13000.0, 14000.0]
        arYExtend = [0.0, 0.0, 0.0, 0.0, 0.0]
        arZExtend = [3000.0, 4000.0, 5000.0, 6000.0, 70000.0]
        oTrackCollection.extend_tracks_with_position_data(
            arTrackIdsExtend,
            arNumPtsPerTrackExtend,
            MTOInputDataType.CARTESIAN_IN_VECTOR_GEOMETRY_TOOL_SYSTEM,
            arTimeExtend,
            arXExtend,
            arYExtend,
            arZExtend,
        )
        TestBase.logger.WriteLine3("\tThe extended TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(4, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId6: "MTOTrack" = oTrackCollection.get_track_from_identifier(6)
        (x, y, z) = trackId6.points[1].position.query_cartesian()
        Assert.assertAlmostEqual(42080.56, x, delta=0.01)
        Assert.assertAlmostEqual(105459.1, y, delta=0.01)
        Assert.assertAlmostEqual(-26.42, z, delta=0.01)

        # Remove tracks
        arTrackIdsRemove = [1, 3, 6]
        oTrackCollection.remove_tracks_by_identifier(arTrackIdsRemove)
        Assert.assertEqual(1, oTrackCollection.count)
        oTrackCollection.remove_all()
        Assert.assertEqual(0, oTrackCollection.count)

        # AddTracksWithPosData using different units
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "ft")

        arTimeAdd2 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", arTimeAdd)
        arXAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arXAdd)
        arYAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arYAdd)
        arZAdd2 = TestBase.Application.conversion_utility.convert_quantity_array("DistanceUnit", "Km", "ft", arZAdd)
        oTrackCollection.add_tracks_with_position_data(
            arTrackIdsAdd,
            arNumPtsPerTrackAdd,
            MTOInputDataType.CARTESIAN_IN_VECTOR_GEOMETRY_TOOL_SYSTEM,
            arTimeAdd2,
            arXAdd2,
            arYAdd2,
            arZAdd2,
        )
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(3, oTrackCollection.count)

        # Confirm position by looking at last track's last point
        trackId5 = oTrackCollection.get_track_from_identifier(5)
        (x, y, z) = trackId5.points[2].position.query_cartesian()
        Assert.assertAlmostEqual(
            22188.34,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", x),
            delta=0.01,
        )
        Assert.assertAlmostEqual(
            48691.15,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", y),
            delta=0.01,
        )
        Assert.assertAlmostEqual(
            -522.45, TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", z), delta=0.01
        )

        # ExtendTracksWithPosData using different units
        arTimeExtend2 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", arTimeExtend)
        arXExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arXExtend
        )
        arYExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arYExtend
        )
        arZExtend2 = TestBase.Application.conversion_utility.convert_quantity_array(
            "DistanceUnit", "Km", "ft", arZExtend
        )
        oTrackCollection.extend_tracks_with_position_data(
            arTrackIdsExtend,
            arNumPtsPerTrackExtend,
            MTOInputDataType.CARTESIAN_IN_VECTOR_GEOMETRY_TOOL_SYSTEM,
            arTimeExtend2,
            arXExtend2,
            arYExtend2,
            arZExtend2,
        )
        TestBase.logger.WriteLine3("\tThe extended TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(4, oTrackCollection.count)

        trackId6 = oTrackCollection.get_track_from_identifier(6)
        (x, y, z) = trackId6.points[1].position.query_cartesian()
        Assert.assertAlmostEqual(
            42080.56,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", x),
            delta=0.01,
        )
        Assert.assertAlmostEqual(
            105459.1,
            TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", y),
            delta=0.01,
        )
        Assert.assertAlmostEqual(
            -26.42, TestBase.Application.conversion_utility.convert_quantity("DistanceUnit", "ft", "Km", z), delta=0.01
        )

        # Switch back to default units
        self.Units.reset_units()

        # RemoveAll
        oTrackCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        # Remove Mto2
        TestBase.Application.current_scenario.children.unload(STKObjectType.MTO, "Mto2")

        TestBase.logger.WriteLine("----- BASIC TRACKS WITH VGT ARRAYS ----- END -----")

    # endregion

    # region GraphicsTrackHelper
    def GraphicsTrackHelper(self, oGfxTrack: "MTODefaultGraphics2DTrack"):
        oGfxTrack.color = Colors.from_argb(16384250)
        AssertEx.AreEqual(Colors.from_argb(16384250), oGfxTrack.color)

        oGfxTrack.fade_times.use_post_fade = True
        Assert.assertEqual(True, oGfxTrack.fade_times.use_post_fade)
        oGfxTrack.fade_times.use_pre_fade = True
        Assert.assertEqual(True, oGfxTrack.fade_times.use_pre_fade)

        oGfxTrack.fade_times.post_fade_time = 200
        Assert.assertEqual(200, oGfxTrack.fade_times.post_fade_time)
        oGfxTrack.fade_times.pre_fade_time = 100
        Assert.assertEqual(100, oGfxTrack.fade_times.pre_fade_time)

        oGfxTrack.show_graphics = True
        Assert.assertEqual(True, oGfxTrack.show_graphics)
        oGfxTrack.show_label = True
        Assert.assertEqual(True, oGfxTrack.show_label)

        oGfxTrack.label_color = Colors.from_argb(16384251)
        AssertEx.AreEqual(Colors.from_argb(16384251), oGfxTrack.label_color)

        oGfxTrack.lead_trail_times.use_lead_trail = True
        Assert.assertEqual(True, oGfxTrack.lead_trail_times.use_lead_trail)

        oGfxTrack.lead_trail_times.lead_time = 100
        Assert.assertEqual(100, oGfxTrack.lead_trail_times.lead_time)
        oGfxTrack.lead_trail_times.trail_time = 200
        Assert.assertEqual(200, oGfxTrack.lead_trail_times.trail_time)

        oGfxTrack.line.show_graphics = True
        Assert.assertEqual(True, oGfxTrack.line.show_graphics)
        oGfxTrack.line.style = LineStyle.L_DASH
        Assert.assertEqual(LineStyle.L_DASH, oGfxTrack.line.style)
        oGfxTrack.line.width = LineWidth.WIDTH5
        Assert.assertEqual(LineWidth.WIDTH5, oGfxTrack.line.width)
        oGfxTrack.line.color = Colors.from_argb(16384252)
        AssertEx.AreEqual(Colors.from_argb(16384252), oGfxTrack.line.color)
        oGfxTrack.line.translucency = 75
        Assert.assertEqual(75, oGfxTrack.line.translucency)
        oGfxTrack.line.alway_show_entire_line = True
        Assert.assertEqual(True, oGfxTrack.line.alway_show_entire_line)
        oGfxTrack.line.alway_show_entire_line = False
        Assert.assertEqual(False, oGfxTrack.line.alway_show_entire_line)

        oGfxTrack.marker.show_graphics = True
        Assert.assertEqual(True, oGfxTrack.marker.show_graphics)
        oGfxTrack.marker.style = "Star"
        Assert.assertEqual("Star", oGfxTrack.marker.style)
        oGfxTrack.marker.color = Colors.from_argb(16384253)
        AssertEx.AreEqual(Colors.from_argb(16384253), oGfxTrack.marker.color)

        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(oGfxTrack.range_contours)

    def GraphicsTrackHelper2(self, oGfxTrack: "MTOGraphics2DTrack"):
        oGfxTrack.color = Colors.from_argb(16384250)
        AssertEx.AreEqual(Colors.from_argb(16384250), oGfxTrack.color)

        oGfxTrack.fade_times.use_post_fade = True
        Assert.assertEqual(True, oGfxTrack.fade_times.use_post_fade)
        oGfxTrack.fade_times.use_pre_fade = True
        Assert.assertEqual(True, oGfxTrack.fade_times.use_pre_fade)

        oGfxTrack.fade_times.post_fade_time = 200
        Assert.assertEqual(200, oGfxTrack.fade_times.post_fade_time)
        oGfxTrack.fade_times.pre_fade_time = 100
        Assert.assertEqual(100, oGfxTrack.fade_times.pre_fade_time)

        oGfxTrack.show_graphics = True
        Assert.assertEqual(True, oGfxTrack.show_graphics)
        oGfxTrack.show_label = True
        Assert.assertEqual(True, oGfxTrack.show_label)

        oGfxTrack.label_color = Colors.from_argb(16384251)
        AssertEx.AreEqual(Colors.from_argb(16384251), oGfxTrack.label_color)

        oGfxTrack.lead_trail_times.use_lead_trail = True
        Assert.assertEqual(True, oGfxTrack.lead_trail_times.use_lead_trail)

        oGfxTrack.lead_trail_times.lead_time = 100
        Assert.assertEqual(100, oGfxTrack.lead_trail_times.lead_time)
        oGfxTrack.lead_trail_times.trail_time = 200
        Assert.assertEqual(200, oGfxTrack.lead_trail_times.trail_time)

        oGfxTrack.line.show_graphics = True
        Assert.assertEqual(True, oGfxTrack.line.show_graphics)
        oGfxTrack.line.style = LineStyle.L_DASH
        Assert.assertEqual(LineStyle.L_DASH, oGfxTrack.line.style)
        oGfxTrack.line.width = LineWidth.WIDTH5
        Assert.assertEqual(LineWidth.WIDTH5, oGfxTrack.line.width)
        oGfxTrack.line.color = Colors.from_argb(16384252)
        AssertEx.AreEqual(Colors.from_argb(16384252), oGfxTrack.line.color)
        oGfxTrack.line.translucency = 75
        Assert.assertEqual(75, oGfxTrack.line.translucency)

        oGfxTrack.marker.show_graphics = True
        Assert.assertEqual(True, oGfxTrack.marker.show_graphics)
        oGfxTrack.marker.style = "Star"
        Assert.assertEqual("Star", oGfxTrack.marker.style)
        oGfxTrack.marker.color = Colors.from_argb(16384253)
        AssertEx.AreEqual(Colors.from_argb(16384253), oGfxTrack.marker.color)

        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(oGfxTrack.range_contours)

    # endregion

    # region GraphicsTrack
    @category("Graphics Tests")
    def test_GraphicsTrack(self):
        TestBase.logger.WriteLine("----- Basic MTO Graphics Test ----- BEGIN -----")
        EarlyBoundTests.AG_MTO.tracks.remove_all()
        oTrack: "MTOTrack" = EarlyBoundTests.AG_MTO.tracks.add(0)
        oPoint: "MTOTrackPoint" = oTrack.points.add("1 Jul 1999 00:00:00.000")

        oTrack.interpolate = True
        oTrack.name = "Track1"
        oPoint.altitude = 200
        oPoint.latitude = 80
        oPoint.longitude = 60

        oTrackGfxCollection: "MTOGraphics2DTrackCollection" = EarlyBoundTests.AG_MTO.graphics.tracks
        oGfxTrack: "MTOGraphics2DTrack" = oTrackGfxCollection[0]
        Assert.assertEqual(oTrack.identifier, oGfxTrack.identifier)

        # Count
        TestBase.logger.WriteLine3(
            "\tThe current GfxTrack collection contains: {0} elements", oTrackGfxCollection.count
        )
        # _NewEnum
        gfxTrack: "MTOGraphics2DTrack"
        # _NewEnum
        for gfxTrack in oTrackGfxCollection:
            TestBase.logger.WriteLine8(
                "\t\tElement: ID = {0}, Color = {1}, IsVisible = {2}",
                gfxTrack.identifier,
                gfxTrack.color,
                gfxTrack.show_graphics,
            )

        # Recycling
        TestBase.logger.WriteLine4("\tThe current Recycling flag is: {0}", oTrackGfxCollection.recycling)
        oTrackGfxCollection.recycling = not oTrackGfxCollection.recycling
        TestBase.logger.WriteLine4("\tThe new Recycling flag is: {0}", oTrackGfxCollection.recycling)
        oTrackGfxCollection.recycling = not oTrackGfxCollection.recycling
        TestBase.logger.WriteLine4("\tThe new Recycling flag is: {0}", oTrackGfxCollection.recycling)

        TestBase.Application.begin_update()
        self.GraphicsTrackHelper2(oGfxTrack)
        TestBase.Application.end_update()

        EarlyBoundTests.AG_MTO.tracks.remove_all()
        TestBase.logger.WriteLine("----- Basic MTO Graphics Test ----- END -----")

    # endregion

    # region GraphicsDefaultTrack
    @category("Graphics Tests")
    def test_GraphicsDefaultTrack(self):
        TestBase.logger.WriteLine("----- Basic MTO Graphics Test ----- BEGIN -----")
        self.GraphicsTrackHelper(EarlyBoundTests.AG_MTO.graphics.default_track)

        EarlyBoundTests.AG_MTO.tracks.remove_all()
        Assert.assertEqual(0, EarlyBoundTests.AG_MTO.tracks.count)
        EarlyBoundTests.AG_MTO.tracks.add(0)
        oNewGfxTrack: "MTOGraphics2DTrack" = EarlyBoundTests.AG_MTO.graphics.tracks[0]

        AssertEx.AreEqual(Colors.from_argb(16384251), oNewGfxTrack.label_color)
        AssertEx.AreEqual(Colors.from_argb(16384252), oNewGfxTrack.line.color)
        AssertEx.AreEqual(Colors.from_argb(16384253), oNewGfxTrack.marker.color)

        Assert.assertEqual(True, oNewGfxTrack.fade_times.use_post_fade)
        Assert.assertEqual(True, oNewGfxTrack.fade_times.use_pre_fade)

        Assert.assertEqual(200, oNewGfxTrack.fade_times.post_fade_time)
        Assert.assertEqual(100, oNewGfxTrack.fade_times.pre_fade_time)

        Assert.assertEqual(True, oNewGfxTrack.show_graphics)
        Assert.assertEqual(True, oNewGfxTrack.show_label)

        Assert.assertEqual(True, oNewGfxTrack.lead_trail_times.use_lead_trail)
        Assert.assertEqual(100, oNewGfxTrack.lead_trail_times.lead_time)
        Assert.assertEqual(200, oNewGfxTrack.lead_trail_times.trail_time)

        Assert.assertEqual(True, oNewGfxTrack.line.show_graphics)
        Assert.assertEqual(LineStyle.L_DASH, oNewGfxTrack.line.style)
        Assert.assertEqual(LineWidth.WIDTH5, oNewGfxTrack.line.width)
        Assert.assertEqual(75, oNewGfxTrack.line.translucency)

        Assert.assertEqual(True, oNewGfxTrack.marker.show_graphics)
        Assert.assertEqual("Star", oNewGfxTrack.marker.style)
        Assert.assertEqual(0, oNewGfxTrack.identifier)
        TestBase.logger.WriteLine2(oNewGfxTrack.identifier)

        EarlyBoundTests.AG_MTO.tracks.remove_all()
        TestBase.logger.WriteLine("----- Basic MTO Graphics Test ----- END -----")

    # endregion

    # region GraphicsGlobalTrack
    @category("Graphics Tests")
    def test_GraphicsGlobalTrack(self):
        # IsObjectGraphicsVisible
        EarlyBoundTests.AG_MTO.graphics.show_graphics = False
        Assert.assertFalse(EarlyBoundTests.AG_MTO.graphics.show_graphics)
        EarlyBoundTests.AG_MTO.graphics.show_graphics = True
        Assert.assertTrue(EarlyBoundTests.AG_MTO.graphics.show_graphics)

        EarlyBoundTests.AG_MTO.graphics.global_track_options.show_tracks = True
        Assert.assertEqual(True, EarlyBoundTests.AG_MTO.graphics.global_track_options.show_tracks)

    # endregion

    # region VOTrack
    @category("VO Tests")
    def test_VOTrack(self):
        TestBase.logger.WriteLine("----- MTO VO TRACK ----- BEGIN -----")
        EarlyBoundTests.AG_MTO.tracks.remove_all()
        # Tracks
        oTracks: "MTOGraphics3DTrackCollection" = EarlyBoundTests.AG_MTO.graphics_3d.tracks
        Assert.assertIsNotNone(oTracks)
        # Count
        TestBase.logger.WriteLine3("\tThe current VOTrackCollection contains: {0} elements.", oTracks.count)

        iIndex: int = 0
        while iIndex < oTracks.count:
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: ID = {2}, IsVisible = {1}",
                iIndex,
                oTracks[iIndex].show_graphics,
                oTracks[iIndex].identifier,
            )

            iIndex += 1

        if oTracks.count == 0:
            # add a new track
            oTrack: "MTOTrack" = EarlyBoundTests.AG_MTO.tracks.add(12345)
            Assert.assertIsNotNone(oTrack)
            # add first track point
            oPoint: "MTOTrackPoint" = oTrack.points.add("1 Jul 2005 12:10:00.000")
            Assert.assertEqual(1, oTrack.points.count)
            oPoint.altitude = 200
            Assert.assertEqual(200, oPoint.altitude)
            oPoint.latitude = 0
            Assert.assertEqual(0, oPoint.latitude)
            oPoint.longitude = -90
            Assert.assertEqual(-90, oPoint.longitude)
            Assert.assertEqual("1 Jul 2005 12:10:00.000", oPoint.time)
            # add second track point
            oPoint = oTrack.points.add("1 Jul 2005 12:20:00.000")
            Assert.assertEqual(2, oTrack.points.count)
            oPoint.altitude = 100
            Assert.assertEqual(100, oPoint.altitude)
            oPoint.latitude = 0
            Assert.assertEqual(0, oPoint.latitude)
            oPoint.longitude = -100
            Assert.assertEqual(-100, oPoint.longitude)
            Assert.assertEqual("1 Jul 2005 12:20:00.000", oPoint.time)
            # add third track point
            oPoint = oTrack.points.add("1 Jul 2005 12:30:00.000")
            Assert.assertEqual(3, oTrack.points.count)
            oPoint.altitude = 200
            Assert.assertEqual(200, oPoint.altitude)
            oPoint.latitude = 10
            Assert.assertEqual(10, oPoint.latitude)
            oPoint.longitude = -100
            Assert.assertEqual(-100, oPoint.longitude)
            Assert.assertEqual("1 Jul 2005 12:30:00.000", oPoint.time)
            # add forth track point
            oPoint = oTrack.points.add("1 Jul 2005 12:40:00.000")
            Assert.assertEqual(4, oTrack.points.count)
            oPoint.altitude = 300
            Assert.assertEqual(300, oPoint.altitude)
            oPoint.latitude = 5
            Assert.assertEqual(5, oPoint.latitude)
            oPoint.longitude = -95
            Assert.assertEqual(-95, oPoint.longitude)
            Assert.assertEqual("1 Jul 2005 12:40:00.000", oPoint.time)
            # Interpolate
            oTrack.interpolate = True

        # Tracks
        oTracks = EarlyBoundTests.AG_MTO.graphics_3d.tracks
        Assert.assertIsNotNone(oTracks)
        # Count
        TestBase.logger.WriteLine3("\tThe new VOTrackCollection contains: {0} elements.", oTracks.count)

        iIndex: int = 0
        while iIndex < oTracks.count:
            # Item
            TestBase.logger.WriteLine8(
                "\t\tElement {0}: ID = {2}, IsVisible = {1}",
                iIndex,
                oTracks[iIndex].show_graphics,
                oTracks[iIndex].identifier,
            )

            iIndex += 1

        # GetTrackFromId
        oVOTrack: "MTOGraphics3DTrack" = oTracks.get_track_from_identifier(oTracks[0].identifier)
        Assert.assertIsNotNone(oVOTrack)
        # Recycling
        TestBase.logger.WriteLine4("\tThe current Recycling flag is: {0}", oTracks.recycling)
        oTracks.recycling = False
        TestBase.logger.WriteLine4("\tThe new Recycling flag is: {0}", oTracks.recycling)
        Assert.assertEqual(False, oTracks.recycling)
        oTracks.recycling = True
        TestBase.logger.WriteLine4("\tThe new Recycling flag is: {0}", oTracks.recycling)
        Assert.assertEqual(True, oTracks.recycling)
        # _NewEnum
        track: "MTOGraphics3DTrack"
        # _NewEnum
        for track in oTracks:
            self.VOTrackHelper(track)

        TestBase.logger.WriteLine("----- MTO VO TRACK ----- END -----")

    # endregion

    # region VOTrackHelper
    def VOTrackHelper(self, oVOTrack: "MTOGraphics3DTrack"):
        TestBase.logger.WriteLine("----- VO TRACK ----- BEGIN -----")
        Assert.assertIsNotNone(oVOTrack)
        # Id
        TestBase.logger.WriteLine3("\tThe VOTrack Id is: {0}", oVOTrack.identifier)
        # IsVisible (false)
        TestBase.logger.WriteLine4("\tThe current IsVisible flag is: {0}", oVOTrack.show_graphics)
        oVOTrack.show_graphics = False
        TestBase.logger.WriteLine4("\tThe new IsVisible flag is: {0}", oVOTrack.show_graphics)
        Assert.assertEqual(False, oVOTrack.show_graphics)

        TestBase.Application.begin_update()

        # Marker (read-only)
        self.VOTrackMarkerHelper(oVOTrack.marker, True)
        # Point (read-only)
        self.VOTrackPointHelper(oVOTrack.point, True)
        # Model (read-only)
        self.VOTrackModelHelper(oVOTrack.model, True)
        # Label (read-only)
        oOLHelper = VOOffsetLabelHelper(self.Units)
        oOLHelper.Run(oVOTrack.label, True)
        # SwapDistances (read-only)
        self.VOTrackSwapDistancesHelper(oVOTrack.swap_distances, True)

        # IsVisible (true)
        oVOTrack.show_graphics = True
        TestBase.logger.WriteLine4("\tThe new IsVisible flag is: {0}", oVOTrack.show_graphics)
        Assert.assertEqual(True, oVOTrack.show_graphics)
        # Marker
        self.VOTrackMarkerHelper(oVOTrack.marker, False)
        # Point
        self.VOTrackPointHelper(oVOTrack.point, False)
        # Model
        self.VOTrackModelHelper(oVOTrack.model, False)
        # Label
        oOLHelper.Run(oVOTrack.label, False)
        # SwapDistances
        self.VOTrackSwapDistancesHelper(oVOTrack.swap_distances, False)
        # RangeContours
        oRCHelper = VORangeContoursHelper(self.Units)
        oRCHelper.Run(oVOTrack.range_contours)
        # DropLines
        self.VOTrackDropLinesHelper(oVOTrack.drop_lines)

        oVOTrack.should_fade_over_trail_time = True
        Assert.assertTrue(oVOTrack.should_fade_over_trail_time)
        oVOTrack.should_fade_over_trail_time = False
        Assert.assertFalse(oVOTrack.should_fade_over_trail_time)

        TestBase.Application.end_update()

        TestBase.logger.WriteLine("----- VO TRACK ----- END -----")

    # endregion

    # region VOMarkerFileHelper
    def VOMarkerFileHelper(self, oFile: "Graphics3DMarkerFile"):
        Assert.assertIsNotNone(oFile)
        filename: str = TestBase.PathCombine("STKData", "VO", "Markers", "Ship.ppm")
        oFile.filename = filename
        Assert.assertEqual(filename, oFile.filename)

        filepath: str = TestBase.PathCombine(TestBase.GetSTKHomeDir(), filename)
        Assert.assertEqual(Path.GetFullPath(filepath), Path.GetFullPath(oFile.file_path))

        oFile.is_transparent = False
        Assert.assertFalse(oFile.is_transparent)
        oFile.is_transparent = True
        Assert.assertTrue(oFile.is_transparent)

        oFile.use_soft_transparency = False
        Assert.assertFalse(oFile.use_soft_transparency)
        oFile.use_soft_transparency = True
        Assert.assertTrue(oFile.use_soft_transparency)

    # endregion

    # region VOTrackMarkerHelper
    def VOTrackMarkerHelper(self, oMarker: "MTOGraphics3DMarker", bReadOnly: bool):
        Assert.assertIsNotNone(oMarker)

        strAngleUnit: str = self.Units.get_current_unit_abbrv("AngleUnit")
        self.Units.set_current_unit("AngleUnit", "rad")
        if bReadOnly:
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                oMarker.marker_type = MarkerType.SHAPE
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oMarker.pixel_size = 12
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                oMarker.angle = 1.23
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oMarker.rotate_from_north = True
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oMarker.x_origin = Graphics3DMarkerOriginType.RIGHT
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oMarker.y_origin = Graphics3DMarkerOriginType.BOTTOM
            with pytest.raises(Exception, match=RegexSubstringMatch("read")):
                oMarker.set_marker_image_filename(Path.Combine(TestBase.GetSTKHomeDir(), r"VO\Markers\Fire.ppm"))
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oMarker.orientation_mode = Graphics3DMarkerOrientation.FOLLOW_DIRECTION

        else:
            oMarker.marker_type = MarkerType.SHAPE
            Assert.assertEqual(MarkerType.SHAPE, oMarker.marker_type)

            oShape: "Graphics3DMarkerShape" = clr.CastAs(oMarker.marker_data, Graphics3DMarkerShape)
            Assert.assertIsNotNone(oShape)
            oShape.style = MarkerShape3d.SHAPE_CIRCLE
            Assert.assertEqual(MarkerShape3d.SHAPE_CIRCLE, oShape.style)
            oShape.style = MarkerShape3d.SHAPE_POINT
            Assert.assertEqual(MarkerShape3d.SHAPE_POINT, oShape.style)
            with pytest.raises(STKInvalidCastError):
                oF: "Graphics3DMarkerFile" = Graphics3DMarkerFile(oMarker.marker_data)

            oMarker.marker_type = MarkerType.IMAGE_FILE
            Assert.assertEqual(MarkerType.IMAGE_FILE, oMarker.marker_type)

            oFile: "Graphics3DMarkerFile" = clr.CastAs(oMarker.marker_data, Graphics3DMarkerFile)
            Assert.assertIsNotNone(oFile)
            self.VOMarkerFileHelper(oFile)
            with pytest.raises(STKInvalidCastError):
                oShape = Graphics3DMarkerShape(oMarker.marker_data)

            oMarker.pixel_size = 12
            Assert.assertEqual(12, oMarker.pixel_size)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                oMarker.pixel_size = 1234

            oMarker.x_origin = Graphics3DMarkerOriginType.RIGHT
            Assert.assertEqual(Graphics3DMarkerOriginType.RIGHT, oMarker.x_origin)
            with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
                oMarker.x_origin = Graphics3DMarkerOriginType.TOP

            oMarker.y_origin = Graphics3DMarkerOriginType.BOTTOM
            Assert.assertEqual(Graphics3DMarkerOriginType.BOTTOM, oMarker.y_origin)
            with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
                oMarker.y_origin = Graphics3DMarkerOriginType.LEFT

            oMarker.orientation_mode = Graphics3DMarkerOrientation.NONE
            Assert.assertEqual(Graphics3DMarkerOrientation.NONE, oMarker.orientation_mode)

            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                oMarker.angle = 1.23

            oMarker.orientation_mode = Graphics3DMarkerOrientation.FOLLOW_DIRECTION
            Assert.assertEqual(Graphics3DMarkerOrientation.FOLLOW_DIRECTION, oMarker.orientation_mode)

            oMarker.angle = 1.23456
            Assert.assertEqual(1.23456, oMarker.angle)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                oMarker.angle = 12.3

            oMarker.orientation_mode = Graphics3DMarkerOrientation.ANGLE
            Assert.assertEqual(Graphics3DMarkerOrientation.ANGLE, oMarker.orientation_mode)

            oMarker.angle = 1.23456
            Assert.assertEqual(1.23456, oMarker.angle)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                oMarker.angle = 12.3

        self.Units.set_current_unit("AngleUnit", strAngleUnit)

    # endregion

    # region VOTrackPointHelper
    def VOTrackPointHelper(self, oPoint: "MTOGraphics3DPoint", bReadOnly: bool):
        TestBase.logger.WriteLine("----- VO POINT ----- BEGIN -----")
        Assert.assertIsNotNone(oPoint)
        # bReadOnly
        TestBase.logger.WriteLine4("\tRead-only flag: {0}", bReadOnly)
        if bReadOnly:
            # IsVisible (read-only)
            with pytest.raises(Exception):
                oPoint.show_graphics = False
            # Size (read-only)
            with pytest.raises(Exception):
                oPoint.size = 3

        else:
            # IsVisible (false)
            TestBase.logger.WriteLine4("\t\tThe current IsVisible is: {0}", oPoint.show_graphics)
            oPoint.show_graphics = False
            TestBase.logger.WriteLine4("\t\tThe new IsVisible is: {0}", oPoint.show_graphics)
            Assert.assertEqual(False, oPoint.show_graphics)
            # Size (read-only)
            with pytest.raises(Exception):
                oPoint.size = 3
            # IsVisible (true)
            oPoint.show_graphics = True
            TestBase.logger.WriteLine4("\t\tThe new IsVisible is: {0}", oPoint.show_graphics)
            Assert.assertEqual(True, oPoint.show_graphics)
            # Size
            TestBase.logger.WriteLine6("\t\tThe current Size is: {0}", oPoint.size)
            oPoint.size = 3
            TestBase.logger.WriteLine6("\t\tThe new Size is: {0}", oPoint.size)
            Assert.assertEqual(3, oPoint.size)
            with pytest.raises(Exception):
                oPoint.size = 33

        TestBase.logger.WriteLine("----- VO POINT ----- END -----")

    # endregion

    # region VOTrackModelHelper
    def VOTrackModelHelper(self, oModel: "MTOGraphics3DModel", bReadOnly: bool):
        TestBase.logger.WriteLine("----- VO MODEL ----- BEGIN -----")
        Assert.assertIsNotNone(oModel)
        # set AngleUnit
        strAngleUnit: str = self.Units.get_current_unit_abbrv("AngleUnit")
        TestBase.logger.WriteLine5("\tThe current AngleUnit is: {0}", strAngleUnit)
        self.Units.set_current_unit("AngleUnit", "rad")
        TestBase.logger.WriteLine5("\tThe new AngleUnit is: {0}", self.Units.get_current_unit_abbrv("AngleUnit"))
        Assert.assertEqual("rad", self.Units.get_current_unit_abbrv("AngleUnit"))
        # bReadOnly
        TestBase.logger.WriteLine4("\tRead-only flag: {0}", bReadOnly)
        if bReadOnly:
            # IsVisible (read-only)
            with pytest.raises(Exception):
                oModel.show_graphics = False
            # ScaleValue (read-only)
            with pytest.raises(Exception):
                oModel.scale_value = 3
            # InitialBearing (read-only)
            with pytest.raises(Exception):
                oModel.initial_bearing = 3.21
            # ZPointsNadir (read-only)
            with pytest.raises(Exception):
                oModel.z_points_nadir = False
            # Filename (read-only)
            with pytest.raises(Exception):
                oModel.filename = TestBase.GetScenarioFile("VO", "Models", "house.mdl")

        else:
            # IsVisible (false)
            TestBase.logger.WriteLine4("\t\tThe current IsVisible is: {0}", oModel.show_graphics)
            oModel.show_graphics = False
            TestBase.logger.WriteLine4("\t\tThe new IsVisible is: {0}", oModel.show_graphics)
            Assert.assertEqual(False, oModel.show_graphics)
            # ScaleValue (read-only)
            with pytest.raises(Exception):
                oModel.scale_value = 3
            # InitialBearing (read-only)
            with pytest.raises(Exception):
                oModel.initial_bearing = 3.21
            # ZPointsNadir (read-only)
            with pytest.raises(Exception):
                oModel.z_points_nadir = False
            # Filename (read-only)
            with pytest.raises(Exception):
                oModel.filename = TestBase.GetScenarioFile("VO", "Models", "house.mdl")
            # IsVisible (true)
            oModel.show_graphics = True
            TestBase.logger.WriteLine4("\t\tThe new IsVisible is: {0}", oModel.show_graphics)
            Assert.assertEqual(True, oModel.show_graphics)
            # ScaleValue
            TestBase.logger.WriteLine6("\t\tThe current ScaleValue is: {0}", oModel.scale_value)
            oModel.scale_value = 3
            TestBase.logger.WriteLine6("\t\tThe new ScaleValue is: {0}", oModel.scale_value)
            Assert.assertEqual(3, oModel.scale_value)
            with pytest.raises(Exception):
                oModel.scale_value = 12
            # InitialBearing
            TestBase.logger.WriteLine6("\t\tThe current InitialBearing is: {0}", oModel.initial_bearing)
            oModel.initial_bearing = 3
            TestBase.logger.WriteLine6("\t\tThe new InitialBearing is: {0}", oModel.initial_bearing)
            Assert.assertEqual(3, oModel.initial_bearing)
            with pytest.raises(Exception):
                oModel.initial_bearing = 12
            # ZPointsNadir
            TestBase.logger.WriteLine4("\t\tThe current ZPointsNadir is: {0}", oModel.z_points_nadir)
            oModel.z_points_nadir = False
            TestBase.logger.WriteLine4("\t\tThe new ZPointsNadir is: {0}", oModel.z_points_nadir)
            Assert.assertEqual(False, oModel.z_points_nadir)
            oModel.z_points_nadir = True
            TestBase.logger.WriteLine4("\t\tThe new ZPointsNadir is: {0}", oModel.z_points_nadir)
            Assert.assertEqual(True, oModel.z_points_nadir)
            # Filename
            TestBase.logger.WriteLine5("\t\tThe current Filename is: {0}", oModel.filename)
            oModel.filename = TestBase.GetScenarioFile("VO", "Models", "house.mdl")
            TestBase.logger.WriteLine5("\t\tThe new Filename is: {0}", oModel.filename)
            Assert.assertEqual(TestBase.PathCombine("VO", "Models", "house.mdl"), oModel.filename)
            with pytest.raises(Exception):
                oModel.filename = "InvalidFileName"
            # FilePath
            filePath: str = oModel.file_path
            Assert.assertEqual(TestBase.GetScenarioFile("VO", "Models", "house.mdl"), oModel.file_path)

        # restore AngleUnit
        self.Units.set_current_unit("AngleUnit", strAngleUnit)
        TestBase.logger.WriteLine5("\tThe new AngleUnit (restored) is: {0}", strAngleUnit)
        Assert.assertEqual(strAngleUnit, self.Units.get_current_unit_abbrv("AngleUnit"))
        TestBase.logger.WriteLine("----- VO MODEL ----- END -----")

    # endregion

    # region VOTrackArticulations
    @category("VO Tests")
    def test_VOTrackArticulations(self):
        #
        # Setup for Articulation test
        #

        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("mtoArticScen")

        TestBase.Application.execute_command('SetTimePeriod * "28 Jan 2013 17:00:00.000" "29 Jan 2013 17:00:00.000"')
        TestBase.Application.execute_command("animate * reset")

        TestBase.Application.execute_command("New / MTO MTO1")

        TestBase.Application.execute_command("defaultTrack   */MTO/MTO1 Interpolate Yes")
        TestBase.Application.execute_command("defaultTrack2d */MTO/MTO1 UsePreFadetime Yes")
        TestBase.Application.execute_command("defaultTrack2d */MTO/MTO1 UsePostFadetime Yes")

        TestBase.Application.execute_command("defaultTrack3D */MTO/MTO1 SaveArticFileOnSave Yes")
        TestBase.Application.execute_command("defaultTrack3D */MTO/MTO1 ReadArticFileOnLoad Yes")

        TestBase.Application.execute_command(
            'Track */MTO/MTO1 add 1 2 "28 Jan 2013 17:00:00.000"  0 0 100000 "28 Jan 2013 18:00:00.000"  1 1 100000'
        )
        TestBase.Application.execute_command(
            'Track */MTO/MTO1 add 2 2 "28 Jan 2013 17:00:00.000"  0 0 100010 "28 Jan 2013 18:00:00.000"  1 1 100030'
        )
        TestBase.Application.execute_command("Track */MTO/MTO1 ComputeTrackID 1")

        TestBase.Application.execute_command("VO * ViewFromTo Normal From MTO/MTO1")
        TestBase.Application.execute_command("VO */MTO/MTO1 OptimizeForCloseView Yes")

        # Application.ExecuteCommand("Track3D */MTO/MTO1 Model 1 Show On File C:/Misc/scaling_sphere.mdl");
        modelFile: str = TestBase.GetScenarioFile("VO", "Models", "scaling_sphere.mdl")
        command: str = "Track3D */MTO/MTO1 Model 1 Show On File " + TestBase.DoubleQuoted(modelFile)
        TestBase.Application.execute_command(command)

        # /////////////////////////////////////////
        #   Test MTOGraphics3DModelArticulation

        mto1: "MTO" = clr.CastAs(TestBase.Application.current_scenario.children["MTO1"], MTO)
        artic: "MTOGraphics3DModelArticulation" = mto1.graphics_3d.tracks[0].model.articulation

        # EnableDefaultSave
        artic.enable_default_save = False
        Assert.assertEqual(False, artic.enable_default_save)
        artic.enable_default_save = True
        Assert.assertEqual(True, artic.enable_default_save)

        # SaveArticFileOnSave
        artic.save_articulation_file_on_save = False
        Assert.assertFalse(artic.save_articulation_file_on_save)
        artic.save_articulation_file_on_save = True
        Assert.assertTrue(artic.save_articulation_file_on_save)

        # EnableDefaultSave
        # Debug: Application.ExecuteCommand("Track3D */MTO/Mto1 ReadArticFileOnLoad * Yes");
        # Debug: Application.ExecuteCommand("Track3D */MTO/Mto1 ReadArticFileOnLoad * No");
        artic.read_articulation_file_on_load = False
        Assert.assertEqual(False, artic.read_articulation_file_on_load)
        artic.read_articulation_file_on_load = True
        Assert.assertEqual(True, artic.read_articulation_file_on_load)

        # SaveArticFileOnSave
        # Debug: Application.ExecuteCommand("Track3D */MTO/Mto1 SaveArticFileOnSave * Yes");
        # Debug: Application.ExecuteCommand("Track3D */MTO/Mto1 SaveArticFileOnSave * No");
        artic.save_articulation_file_on_save = False
        Assert.assertEqual(False, artic.save_articulation_file_on_save)
        artic.save_articulation_file_on_save = True
        Assert.assertEqual(True, artic.save_articulation_file_on_save)

        iIndex: int = 0
        while iIndex < artic.level_of_detail_count:
            arAvailableArtic = artic.get_available_articulations(iIndex)

            i: int = 0
            while i < Array.Length(arAvailableArtic):
                strArtic: str = str(arAvailableArtic[i])

                # TransCollection test
                oTransformations: "Graphics3DModelTransformationCollection" = artic.get_available_transformations(
                    iIndex, strArtic
                )
                Assert.assertIsNotNone(oTransformations)

                j: int = 0
                while j < oTransformations.count:
                    modelTrans: "Graphics3DModelTransformation" = oTransformations[j]
                    Console.WriteLine(
                        (
                            (
                                (
                                    (((((strArtic + "   ") + modelTrans.name) + "   ") + str(modelTrans.value)) + "   ")
                                    + str(modelTrans.minimum)
                                )
                                + "   "
                            )
                            + str(modelTrans.maximum)
                        )
                    )
                    dMid: float = ((modelTrans.minimum + modelTrans.maximum)) / 2.0

                    artic.set_transformation_value(iIndex, strArtic, modelTrans.name, dMid)
                    Assert.assertEqual(dMid, artic.get_transformation_value(iIndex, strArtic, modelTrans.name))

                    with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):
                        modelTrans.value = modelTrans.maximum * 2

                    j += 1

                # Collection enumeration test
                oItem: "Graphics3DModelTransformation"

                # Collection enumeration test
                for oItem in oTransformations:
                    Assert.assertIsNotNone(oItem)

                i += 1

            iIndex += 1

        TestBase.LoadTestScenario(Path.Combine("MtoTests", "MtoTests.sc"))
        EarlyBoundTests.AG_MTO = MTO(TestBase.Application.current_scenario.children.new(STKObjectType.MTO, "Mto1"))

    # endregion

    # region VOTrackSwapDistancesHelper
    def VOTrackSwapDistancesHelper(self, oSwap: "MTOGraphics3DSwapDistances", bReadOnly: bool):
        TestBase.logger.WriteLine("----- VO SWAP DISTANCES ----- BEGIN -----")
        Assert.assertIsNotNone(oSwap)
        # set DistanceUnit
        strDistanceUnit: str = self.Units.get_current_unit_abbrv("DistanceUnit")
        TestBase.logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.Units.set_current_unit("DistanceUnit", "ft")
        TestBase.logger.WriteLine5("\tThe new DistanceUnit is: {0}", self.Units.get_current_unit_abbrv("DistanceUnit"))
        Assert.assertEqual("ft", self.Units.get_current_unit_abbrv("DistanceUnit"))
        # bReadOnly
        TestBase.logger.WriteLine4("\tRead-only flag: {0}", bReadOnly)
        if bReadOnly:
            # UseSwapDistances (read-only)
            with pytest.raises(Exception):
                oSwap.use_swap_distances = False
            # LabelFrom (read-only)
            with pytest.raises(Exception):
                oSwap.label_from = 3
            # LabelTo (read-only)
            with pytest.raises(Exception):
                oSwap.label_to = 3.21
            # ModelFrom (read-only)
            with pytest.raises(Exception):
                oSwap.model_from = 123
            # ModelTo (read-only)
            with pytest.raises(Exception):
                oSwap.model_to = 1234
            # MarkerFrom (read-only)
            with pytest.raises(Exception):
                oSwap.marker_from = 123
            # MarkerTo (read-only)
            with pytest.raises(Exception):
                oSwap.marker_to = 1234
            # PointFrom (read-only)
            with pytest.raises(Exception):
                oSwap.point_from = 123
            # PointTo (read-only)
            with pytest.raises(Exception):
                oSwap.point_to = 1234

        else:
            # UseSwapDistances (false)
            TestBase.logger.WriteLine4("\t\tThe current UseSwapDistances is: {0}", oSwap.use_swap_distances)
            oSwap.use_swap_distances = False
            TestBase.logger.WriteLine4("\t\tThe new UseSwapDistances is: {0}", oSwap.use_swap_distances)
            Assert.assertEqual(False, oSwap.use_swap_distances)
            # LabelFrom (read-only)
            with pytest.raises(Exception):
                oSwap.label_from = 3
            # LabelTo (read-only)
            with pytest.raises(Exception):
                oSwap.label_to = 3.21
            # ModelFrom (read-only)
            with pytest.raises(Exception):
                oSwap.model_from = 123
            # ModelTo (read-only)
            with pytest.raises(Exception):
                oSwap.model_to = 1234
            # MarkerFrom (read-only)
            with pytest.raises(Exception):
                oSwap.marker_from = 123
            # MarkerTo (read-only)
            with pytest.raises(Exception):
                oSwap.marker_to = 1234
            # PointFrom (read-only)
            with pytest.raises(Exception):
                oSwap.point_from = 123
            # PointTo (read-only)
            with pytest.raises(Exception):
                oSwap.point_to = 1234
            # UseSwapDistances (true)
            oSwap.use_swap_distances = True
            TestBase.logger.WriteLine4("\t\tThe new UseSwapDistances is: {0}", oSwap.use_swap_distances)
            Assert.assertEqual(True, oSwap.use_swap_distances)
            # LabelFrom
            TestBase.logger.WriteLine6("\t\t\tThe current LabelFrom is: {0}", oSwap.label_from)
            oSwap.label_from = 1234.56789
            TestBase.logger.WriteLine6("\t\t\tThe new LabelFrom is: {0}", oSwap.label_from)
            Assert.assertEqual(1234.56789, oSwap.label_from)
            with pytest.raises(Exception):
                oSwap.label_from = -12.34
            # LabelTo
            TestBase.logger.WriteLine6("\t\t\tThe current LabelTo is: {0}", oSwap.label_to)
            oSwap.label_to = 56789.1234
            TestBase.logger.WriteLine6("\t\t\tThe new LabelTo is: {0}", oSwap.label_to)
            Assert.assertEqual(56789.1234, oSwap.label_to)
            with pytest.raises(Exception):
                oSwap.label_to = -12.34
            # ModelFrom
            TestBase.logger.WriteLine6("\t\t\tThe current ModelFrom is: {0}", oSwap.model_from)
            oSwap.model_from = 1234.56789
            TestBase.logger.WriteLine6("\t\t\tThe new ModelFrom is: {0}", oSwap.model_from)
            Assert.assertEqual(1234.56789, oSwap.model_from)
            with pytest.raises(Exception):
                oSwap.model_from = -12.34
            # ModelTo
            TestBase.logger.WriteLine6("\t\t\tThe current ModelTo is: {0}", oSwap.model_to)
            oSwap.model_to = 56789.1234
            TestBase.logger.WriteLine6("\t\t\tThe new ModelTo is: {0}", oSwap.model_to)
            Assert.assertEqual(56789.1234, oSwap.model_to)
            with pytest.raises(Exception):
                oSwap.model_to = -12.34
            # MarkerFrom
            TestBase.logger.WriteLine6("\t\t\tThe current MarkerFrom is: {0}", oSwap.marker_from)
            oSwap.marker_from = 1234.56789
            TestBase.logger.WriteLine6("\t\t\tThe new MarkerFrom is: {0}", oSwap.marker_from)
            Assert.assertEqual(1234.56789, oSwap.marker_from)
            with pytest.raises(Exception):
                oSwap.marker_from = -12.34
            # MarkerTo
            TestBase.logger.WriteLine6("\t\t\tThe current MarkerTo is: {0}", oSwap.marker_to)
            oSwap.marker_to = 56789.1234
            TestBase.logger.WriteLine6("\t\t\tThe new MarkerTo is: {0}", oSwap.marker_to)
            Assert.assertEqual(56789.1234, oSwap.marker_to)
            with pytest.raises(Exception):
                oSwap.marker_to = -12.34
            # PointFrom
            TestBase.logger.WriteLine6("\t\t\tThe current PointFrom is: {0}", oSwap.point_from)
            oSwap.point_from = 1234.56789
            TestBase.logger.WriteLine6("\t\t\tThe new PointFrom is: {0}", oSwap.point_from)
            Assert.assertEqual(1234.56789, oSwap.point_from)
            with pytest.raises(Exception):
                oSwap.point_from = -12.34
            # PointTo
            TestBase.logger.WriteLine6("\t\t\tThe current PointTo is: {0}", oSwap.point_to)
            oSwap.point_to = 56789.1234
            TestBase.logger.WriteLine6("\t\t\tThe new PointTo is: {0}", oSwap.point_to)
            Assert.assertEqual(56789.1234, oSwap.point_to)
            with pytest.raises(Exception):
                oSwap.point_to = -12.34

        # restore DistanceUnit
        self.Units.set_current_unit("DistanceUnit", strDistanceUnit)
        TestBase.logger.WriteLine5("\tThe new DistanceUnit (restored) is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.Units.get_current_unit_abbrv("DistanceUnit"))
        TestBase.logger.WriteLine("----- VO SWAP DISTANCES ----- END -----")

    # endregion

    # region VOTrackDropLinesHelper
    def VOTrackDropLinesHelper(self, oDropLines: "MTOGraphics3DDropLines"):
        TestBase.logger.WriteLine("----- VO DROPLINES ----- BEGIN -----")
        Assert.assertIsNotNone(oDropLines)
        # Position
        oPosHelper = VODropLinePosItemCollectionHelper()
        oPosHelper.Run(oDropLines.position)
        # Ephemeris
        oPathHelper = VODropLinePathItemCollectionHelper()
        oPathHelper.Run(oDropLines.ephemeris)
        TestBase.logger.WriteLine("----- VO DROPLINES ----- END -----")

    # endregion

    # region VODefaultTrack
    @category("VO Tests")
    def test_VODefaultTrack(self):
        TestBase.logger.WriteLine("----- MTO VO DEFAULT TRACK ----- BEGIN -----")
        # DefaultTrack
        oTrack: "MTODefaultGraphics3DTrack" = EarlyBoundTests.AG_MTO.graphics_3d.default_track
        Assert.assertIsNotNone(oTrack)

        # IsVisible (false)
        TestBase.logger.WriteLine4("\tThe current IsVisible flag is: {0}", oTrack.show_graphics)
        oTrack.show_graphics = False
        TestBase.logger.WriteLine4("\tThe new IsVisible flag is: {0}", oTrack.show_graphics)
        Assert.assertEqual(False, oTrack.show_graphics)

        TestBase.Application.begin_update()

        # Marker (read-only)
        self.VOTrackMarkerHelper(oTrack.marker, True)
        # Point (read-only)
        self.VOTrackPointHelper(oTrack.point, True)
        # Model (read-only)
        self.VOTrackModelHelper(oTrack.model, True)
        # Label (read-only)
        oOLHelper = VOOffsetLabelHelper(self.Units)
        oOLHelper.Run(oTrack.label, True)
        # SwapDistances (read-only)
        self.VOTrackSwapDistancesHelper(oTrack.swap_distances, True)

        # IsVisible (true)
        oTrack.show_graphics = True
        TestBase.logger.WriteLine4("\tThe new IsVisible flag is: {0}", oTrack.show_graphics)
        Assert.assertEqual(True, oTrack.show_graphics)
        # Marker
        self.VOTrackMarkerHelper(oTrack.marker, False)
        # Point
        self.VOTrackPointHelper(oTrack.point, False)
        # Model
        self.VOTrackModelHelper(oTrack.model, False)
        # Label
        oOLHelper.Run(oTrack.label, False)
        # SwapDistances
        self.VOTrackSwapDistancesHelper(oTrack.swap_distances, False)
        # RangeContours
        oRCHelper = VORangeContoursHelper(self.Units)
        oRCHelper.Run(oTrack.range_contours)
        # DropLines
        self.VOTrackDropLinesHelper(oTrack.drop_lines)

        oTrack.should_fade_over_trail_time = True
        Assert.assertTrue(oTrack.should_fade_over_trail_time)
        oTrack.should_fade_over_trail_time = False
        Assert.assertFalse(oTrack.should_fade_over_trail_time)

        TestBase.Application.end_update()

        TestBase.logger.WriteLine("----- MTO VO DEFAULT TRACK ----- END -----")

    # endregion

    # region VOGlobalTrack
    @category("VO Tests")
    def test_VOGlobalTrack(self):
        TestBase.logger.WriteLine("----- VO CLOBAL TRACK OPTIONS ----- BEGIN -----")
        # GlobalTrackOptions
        oGTOptions: "MTOGraphics3DGlobalTrackOptions" = EarlyBoundTests.AG_MTO.graphics_3d.global_track_options
        Assert.assertIsNotNone(oGTOptions)
        # TracksVisible (false)
        TestBase.logger.WriteLine4("\tThe current TracksVisible flag is: {0}", oGTOptions.show_tracks)
        oGTOptions.show_tracks = False
        TestBase.logger.WriteLine4("\tThe new TracksVisible flag is: {0}", oGTOptions.show_tracks)
        Assert.assertEqual(False, oGTOptions.show_tracks)
        # LabelsVisible (read-only)
        with pytest.raises(Exception):
            oGTOptions.show_label = True
        # LinesVisible (read-only)
        with pytest.raises(Exception):
            oGTOptions.show_lines = True
        # MarkersVisible (read-only)
        with pytest.raises(Exception):
            oGTOptions.show_markers = True
        # PointsVisible (read-only)
        with pytest.raises(Exception):
            oGTOptions.show_points = True
        # TracksVisible (true)
        oGTOptions.show_tracks = True
        TestBase.logger.WriteLine4("\tThe new TracksVisible flag is: {0}", oGTOptions.show_tracks)
        Assert.assertEqual(True, oGTOptions.show_tracks)
        # LabelsVisible
        TestBase.logger.WriteLine4("\t\tThe current LabelsVisible flag is: {0}", oGTOptions.show_label)
        oGTOptions.show_label = False
        TestBase.logger.WriteLine4("\t\tThe new LabelsVisible flag is: {0}", oGTOptions.show_label)
        Assert.assertEqual(False, oGTOptions.show_label)
        oGTOptions.show_label = True
        TestBase.logger.WriteLine4("\t\tThe new LabelsVisible flag is: {0}", oGTOptions.show_label)
        Assert.assertEqual(True, oGTOptions.show_label)
        # LinesVisible
        TestBase.logger.WriteLine4("\t\tThe current LinesVisible flag is: {0}", oGTOptions.show_lines)
        oGTOptions.show_lines = False
        TestBase.logger.WriteLine4("\t\tThe new LinesVisible flag is: {0}", oGTOptions.show_lines)
        Assert.assertEqual(False, oGTOptions.show_lines)
        oGTOptions.show_lines = True
        TestBase.logger.WriteLine4("\t\tThe new LinesVisible flag is: {0}", oGTOptions.show_lines)
        Assert.assertEqual(True, oGTOptions.show_lines)
        # MarkersVisible
        TestBase.logger.WriteLine4("\t\tThe current MarkersVisible flag is: {0}", oGTOptions.show_markers)
        oGTOptions.show_markers = False
        TestBase.logger.WriteLine4("\t\tThe new MarkersVisible flag is: {0}", oGTOptions.show_markers)
        Assert.assertEqual(False, oGTOptions.show_markers)
        oGTOptions.show_markers = True
        TestBase.logger.WriteLine4("\t\tThe new MarkersVisible flag is: {0}", oGTOptions.show_markers)
        Assert.assertEqual(True, oGTOptions.show_markers)
        # PointsVisible
        TestBase.logger.WriteLine4("\t\tThe current PointsVisible flag is: {0}", oGTOptions.show_points)
        oGTOptions.show_points = False
        TestBase.logger.WriteLine4("\t\tThe new PointsVisible flag is: {0}", oGTOptions.show_points)
        Assert.assertEqual(False, oGTOptions.show_points)
        oGTOptions.show_points = True
        TestBase.logger.WriteLine4("\t\tThe new PointsVisible flag is: {0}", oGTOptions.show_points)
        Assert.assertEqual(True, oGTOptions.show_points)
        # OptimizeLines
        TestBase.logger.WriteLine4("\t\tThe current OptimizeLines flag is: {0}", oGTOptions.optimize_lines)
        oGTOptions.optimize_lines = False
        TestBase.logger.WriteLine4("\t\tThe new OptimizeLines flag is: {0}", oGTOptions.optimize_lines)
        Assert.assertEqual(False, oGTOptions.optimize_lines)
        oGTOptions.optimize_lines = True
        TestBase.logger.WriteLine4("\t\tThe new OptimizeLines flag is: {0}", oGTOptions.optimize_lines)
        Assert.assertEqual(True, oGTOptions.optimize_lines)
        TestBase.logger.WriteLine("----- VO CLOBAL TRACK OPTIONS ----- END -----")

    # endregion

    # region BadTracks
    @category("Basic Tests")
    def test_BadTracks(self):
        TestBase.logger.WriteLine("----- BAD TRACKS ----- BEGIN -----")
        # Tracks
        oTrackCollection: "MTOTrackCollection" = EarlyBoundTests.AG_MTO.tracks
        Assert.assertIsNotNone(oTrackCollection)
        # Count
        TestBase.logger.WriteLine3("\tThe current TrackCollection contains: {0} elements.", oTrackCollection.count)

        iIndex: int = 0
        while iIndex < oTrackCollection.count:
            TestBase.logger.WriteLine9(
                "\t\tElement {0}: ID = {2}, Name = {1}, Interpolate = {3}",
                iIndex,
                oTrackCollection[iIndex].name,
                oTrackCollection[iIndex].identifier,
                oTrackCollection[iIndex].interpolate,
            )

            iIndex += 1

        # RemoveAll
        oTrackCollection.remove_all()
        TestBase.logger.WriteLine3("\tThe new TrackCollection contains: {0} elements.", oTrackCollection.count)
        Assert.assertEqual(0, oTrackCollection.count)

        # AddTrack with out-of-sequence times
        arTime = ["1 Jul 2005 12:10:00.000", "1 Jul 2005 12:05:00.000", "1 Jul 2005 12:30:00.000"]
        arLatitude = [0.0, 5.0, 10.0]
        arLongitude = [0.0, 5.0, 5.0]
        arAltitude = [50.0, 100.0, 150.0]

        # Trouble: the following command allows adding points with out-of-sequence times.
        oTrack: "MTOTrack" = None
        try:
            oTrack = oTrackCollection.add_track(1, arTime, arLatitude, arLongitude, arAltitude)
            Assert.fail()
            Assert.assertIsNotNone(oTrack)
            Assert.assertEqual(3, oTrack.points.count)
            TestBase.logger.WriteLine3("\tThe new TrackPointCollection contains: {0} elements.", oTrack.points.count)
            trackPoint: "MTOTrackPoint"
            for trackPoint in oTrack.points:
                TestBase.logger.WriteLine9(
                    "\t\tElement: Time = {0}, Latitude = {1}, Longitude = {2}, Altitude = {3}",
                    trackPoint.time,
                    trackPoint.latitude,
                    trackPoint.longitude,
                    trackPoint.altitude,
                )

        except AssertionError:
            raise

        except Exception as ex:
            TestBase.logger.WriteLine5("EXPECTED EXCEPTION:{0}", str(ex))

        Assert.assertEqual(0, oTrackCollection.count)

        #  Create a new track
        oTrack = oTrackCollection.add(1)
        Assert.assertIsNotNone(oTrack)

        # Remove All Points
        oTrack.points.remove_all()
        Assert.assertEqual(0, oTrack.points.count)

        # Add a point
        oPoint: "MTOTrackPoint" = oTrack.points.add("1 Jul 2005 12:10:00.000")
        Assert.assertEqual(1, oTrack.points.count)
        Assert.assertIsNotNone(oPoint)
        Assert.assertEqual("1 Jul 2005 12:10:00.000", oPoint.time)

        # Add another point with invalid time
        with pytest.raises(Exception):
            oTrack.points.add("1 Jul 2005 12:09:00.000")

        # Add another point to the end of the point collection.
        # The point's time is greater than the track's last
        # point time so there should not be any exceptions.
        oPoint = oTrack.points.add("1 Jul 2005 12:18:00.000")
        Assert.assertEqual(2, oTrack.points.count)
        Assert.assertIsNotNone(oPoint)

        oTrackCollection.remove_all()
        TestBase.logger.WriteLine("----- BAD TRACKS ----- END -----")

    # endregion

    # region CreateTracksUsingDifferentDateFormats
    @category("Basic Tests")
    def test_CreateTracksUsingDifferentDateFormats(self):
        # This test was written to verify BUG48761

        TestBase.logger.WriteLine("----- CreateTracksUsingDifferentDateFormats ----- BEGIN -----")

        # Create a new MTO for the test
        mto: "MTO" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.MTO, "MTO_BUG48761"), MTO
        )

        # Switch date unit to JDate
        initialDateUnit: str = TestBase.Application.units_preferences.get_current_unit_abbrv("DateFormat")
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "JDate")

        # Add one track using JDate
        times1 = [2454929.0, 2454930.0, 2454931.0, 2454932.0, 2454933.0, 2454934.0]
        lat1 = [0, 1, 2, 3, 4, 5]
        lon1 = [0, 1, 2, 3, 4, 5]
        alt1 = [10000, 10000, 10000, 10000, 10000, 10000]
        mto.tracks.add_track(1, times1, lat1, lon1, alt1)
        # Verify date have been corrected processed
        Assert.assertEqual(2454929.0, Convert.ToDouble(mto.tracks[0].points[0].time))
        Assert.assertEqual(2454930.0, Convert.ToDouble(mto.tracks[0].points[1].time))
        Assert.assertEqual(2454931.0, Convert.ToDouble(mto.tracks[0].points[2].time))
        Assert.assertEqual(2454932.0, Convert.ToDouble(mto.tracks[0].points[3].time))
        Assert.assertEqual(2454933.0, Convert.ToDouble(mto.tracks[0].points[4].time))
        Assert.assertEqual(2454934.0, Convert.ToDouble(mto.tracks[0].points[5].time))

        # Switch date unit to UTCG
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "UTCG")

        # Verify date have been corrected processed
        Assert.assertEqual("7 Apr 2009 12:00:00.000", mto.tracks[0].points[0].time)
        Assert.assertEqual("8 Apr 2009 12:00:00.000", mto.tracks[0].points[1].time)
        Assert.assertEqual("9 Apr 2009 12:00:00.000", mto.tracks[0].points[2].time)
        Assert.assertEqual("10 Apr 2009 12:00:00.000", mto.tracks[0].points[3].time)
        Assert.assertEqual("11 Apr 2009 12:00:00.000", mto.tracks[0].points[4].time)
        Assert.assertEqual("12 Apr 2009 12:00:00.000", mto.tracks[0].points[5].time)

        # Add another track using UTCG
        times2 = ["22 Apr 2009 12:00:00.000", "22 Apr 2009 14:00:00.000", "22 Apr 2009 15:00:00.000"]
        lat2 = [0, 1, 2]
        lon2 = [0, 1, 2]
        alt2 = [10000, 10000, 10000]
        mto.tracks.add_track(2, times2, lat2, lon2, alt2)
        # Verify date have been corrected processed
        Assert.assertEqual("22 Apr 2009 12:00:00.000", mto.tracks[1].points[0].time)
        Assert.assertEqual("22 Apr 2009 14:00:00.000", mto.tracks[1].points[1].time)
        Assert.assertEqual("22 Apr 2009 15:00:00.000", mto.tracks[1].points[2].time)

        # Switch date unit to EpSec
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")

        # Add another track using EpSec
        times3 = TestBase.Application.conversion_utility.convert_date_array("UTCG", "EpSec", times2)
        mto.tracks.add_track(3, times3, lat2, lon2, alt2)
        # Switch date unit to UTCG
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "UTCG")

        # Verify date have been corrected processed
        Assert.assertEqual("22 Apr 2009 12:00:00.000", mto.tracks[2].points[0].time)
        Assert.assertEqual("22 Apr 2009 14:00:00.000", mto.tracks[2].points[1].time)
        Assert.assertEqual("22 Apr 2009 15:00:00.000", mto.tracks[2].points[2].time)

        # Restore initial unit preferences
        TestBase.Application.units_preferences.set_current_unit("DateFormat", initialDateUnit)

        # Delete MTO object that was added for the test
        (IStkObject(mto)).unload()

        TestBase.logger.WriteLine("----- CreateTracksUsingDifferentDateFormats ----- END -----")

    # endregion
