from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Mto(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Mto, self).__init__(*args, **kwargs)

    m_Object: "IMto" = None
    m_DefaultName: str = "mto1"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region SetUp
    def setUp(self):
        Mto.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.MTO, Mto.m_DefaultName), IMto
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.MTO, Mto.m_DefaultName)
        Mto.m_Object = None

    # endregion

    # region ConfigureMtos
    def test_ConfigureMtos(self):
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("DateFormat", "UTCG")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("Angle", "deg")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("Distance", "m")
        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

    def ConfigureMtos(self, root: "IStkObjectRoot", mto: "IMto"):
        scenario: "IScenario" = clr.CastAs(root.current_scenario, IScenario)
        scenario.set_time_period("1 Feb 2008 12:00:00.000", "2 Feb 2008 12:00:00.000")

        # Number of tracks and points to add
        trackCount: float = 10
        pointCount: float = 20

        # Initial values from which we will interpolate
        lat0: float = 40.04
        lon0: float = -75.595
        alt0: float = 0

        root.begin_update()  # Call BeginUpdate for STK engine to delay updates

        i: int = 0
        while i < trackCount:
            track: "IMtoTrack" = mto.tracks.add(i)
            date: "IDate" = root.conversion_utility.new_date("UTCG", str(scenario.start_time))

            j: int = 0
            while j < pointCount:
                lat: float = lat0 + (1 * i)
                lon: float = lon0 + (0.1 * j)
                alt: float = alt0

                date = date.add("sec", 120)

                track.points.add_point(date.format("UTCG"), lat, lon, alt)

                j += 1

            i += 1

        root.end_update()

    # endregion

    # region ConfigureMtoGraphics
    @category("Graphics Tests")
    def test_ConfigureMtoGraphics(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1")
        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        self.ConfigureMtoGraphics(Mto.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "Satellite1")

    def ConfigureMtoGraphics(self, mto: "IMto"):
        tracks: "IMtoVOTrackCollection" = mto.vo.tracks
        element: "IMtoVOTrack"
        for element in tracks:
            element.marker.pixel_size = 12
            element.marker.orientation_mode = VO_MARKER_ORIENTATION.ANGLE
            element.marker.x_origin = VO_MARKER_ORIGIN_TYPE.RIGHT
            element.marker.y_origin = VO_MARKER_ORIGIN_TYPE.BOTTOM
            element.marker.angle = 1.23

            element.marker.marker_type = MARKER_TYPE.IMAGE_FILE
            element.marker.set_marker_image_file(r"STKData\VO\Markers\Fire.ppm")

            element.model.is_visible = True
            element.model.filename = r"STKData\VO\Models\Land\ariane-lp.mdl"
            element.model.initial_bearing = 3.0
            element.model.scale_value = 2.0
            element.model.z_points_nadir = True

            element.label.enable = True
            element.label.x = 33.5
            element.label.y = 82.2
            element.label.z = 100.0
            element.label.offset_frame = OFFSET_FRAME_TYPE.CARTESIAN

    # endregion

    # region ConfigureMtoTrackModel
    @category("Graphics Tests")
    def test_ConfigureMtoTrackModel(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1")
        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        self.ConfigureMtoTrackModel(Mto.m_Object.vo.tracks[0])
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "Satellite1")

    def ConfigureMtoTrackModel(self, track: "IMtoVOTrack"):
        model: "IMtoVOModel" = track.model
        model.is_visible = True
        model.filename = r"STKData\VO\Models\Land\ariane-lp.mdl"
        model.initial_bearing = 3.0
        model.scale_value = 2.0
        model.z_points_nadir = True

    # endregion

    # region ConfigureMtoTrackMarker
    @category("Graphics Tests")
    def test_ConfigureMtoTrackMarker(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1")
        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        self.ConfigureMtoTrackMarker(Mto.m_Object.vo.tracks[0])
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "Satellite1")

    def ConfigureMtoTrackMarker(self, track: "IMtoVOTrack"):
        marker: "IMtoVOMarker" = track.marker
        marker.pixel_size = 12
        marker.orientation_mode = VO_MARKER_ORIENTATION.ANGLE
        marker.x_origin = VO_MARKER_ORIGIN_TYPE.RIGHT
        marker.y_origin = VO_MARKER_ORIGIN_TYPE.BOTTOM
        marker.angle = 1.23
        marker.marker_type = MARKER_TYPE.IMAGE_FILE
        marker.set_marker_image_file(r"STKData\VO\Markers\Fire.ppm")

    # endregion

    # region CreateMtoOnCurrentScenarioCentralBody
    def test_CreateMtoOnCurrentScenarioCentralBody(self):
        # Unload because all other code snippet's want the mto already loaded except for this one.
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.MTO, Mto.m_DefaultName)
        self.CreateMtoOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateMtoOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the MTO
        mto: "IMto" = clr.CastAs(root.current_scenario.children.new(STK_OBJECT_TYPE.MTO, "mto1"), IMto)

    # endregion

    # region DetermineWhichTracksAreVisibleFromOtherStkObjectAtSpecifiedTime
    def test_DetermineWhichTracksAreVisibleFromOtherStkObjectAtSpecifiedTime(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "J2Satellite"),
            ISatellite,
        )
        satellite.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60
        j2prop.propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineWhichTracksAreVisibleFromOtherStkObjectAtSpecifiedTime(Mto.m_Object)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "J2Satellite")

    def DetermineWhichTracksAreVisibleFromOtherStkObjectAtSpecifiedTime(self, mto: "IMto"):
        mtoVisibility: "IMtoAnalysisVisibility" = mto.analysis.visibility
        mtoVisibility.use_terrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.entirety = MTO_ENTIRETY.PARTIAL  # Only applies if MTO is static (i.e. non time dependent).

        mtoVisibility.stk_object_path = "Satellite/J2Satellite"

        # ComputeAllTracks returns a two dimensional array whose elements are trackid and visibility
        trackVisibilityArray = mtoVisibility.compute_all_tracks(
            MTO_VISIBILITY_MODE.VISIBILITY_MODE_EACH, "1 Jan 2012 12:00:00.000"
        )

        # Output results
        Console.WriteLine("ComputeAllTracks:")

        i: int = 0
        while i < len(trackVisibilityArray):
            Console.WriteLine(
                "   Track {0} visibility: {1}",
                Convert.ToInt32(trackVisibilityArray[i][0]),
                Convert.ToInt32(trackVisibilityArray[i][1]),
            )

            i += 1

    # endregion

    # region DetermineWhichTracksOfSpecifiedSubsetOfTracksAreVisibleFromOtherStkObject
    def test_DetermineWhichTracksOfSpecifiedSubsetOfTracksAreVisibleFromOtherStkObject(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "J2Satellite"),
            ISatellite,
        )
        satellite.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60
        j2prop.propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineWhichTracksOfSpecifiedSubsetOfTracksAreVisibleFromOtherStkObject(
            CodeSnippetsTestBase.m_Root, Mto.m_Object
        )

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "J2Satellite")

    def DetermineWhichTracksOfSpecifiedSubsetOfTracksAreVisibleFromOtherStkObject(
        self, root: "IStkObjectRoot", mto: "IMto"
    ):
        mtoVisibility: "IMtoAnalysisVisibility" = mto.analysis.visibility
        mtoVisibility.use_terrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.entirety = MTO_ENTIRETY.PARTIAL  # Only applies if MTO is static (i.e. non time dependent).

        tracksOfInterest = [1, 2, 7]

        mtoVisibility.stk_object_path = "Satellite/J2Satellite"

        # ComputeTracks expects as the second parameter a one dimensional array of mto track ids
        # ComputeTracks returns a two dimensional array whose values are track id and visiblity
        trackVisibilityArray = mtoVisibility.compute_tracks(
            MTO_VISIBILITY_MODE.VISIBILITY_MODE_EACH, tracksOfInterest, "1 Jan 2012 12:05:00.000"
        )

        # Output results
        Console.WriteLine("ComputeTracks:")

        i: int = 0
        while i < len(trackVisibilityArray):
            Console.WriteLine(
                "   Track {0} visibility: {1}",
                Convert.ToInt32(trackVisibilityArray[i][0]),
                Convert.ToInt32(trackVisibilityArray[i][1]),
            )

            i += 1

    # endregion

    # region DetermineIfAllTracksAreVisibleFromOtherStkObject
    def test_DetermineIfAllTracksAreVisibleFromOtherStkObject(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "J2Satellite"),
            ISatellite,
        )
        satellite.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60
        j2prop.propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineIfAllTracksAreVisibleFromOtherStkObject(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "J2Satellite")

    def DetermineIfAllTracksAreVisibleFromOtherStkObject(self, root: "IStkObjectRoot", mto: "IMto"):
        mtoVisibility: "IMtoAnalysisVisibility" = mto.analysis.visibility
        mtoVisibility.use_terrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.entirety = MTO_ENTIRETY.PARTIAL  # Only applies if MTO is static (i.e. non time dependent).

        mtoVisibility.stk_object_path = "Satellite/J2Satellite"

        tracksOfInterest = [1, 2, 7]

        # AreTracksVisible expects as the second parameter a one dimensional array of mto track ids
        areTracksAreVisible: bool = mtoVisibility.are_tracks_visible(
            MTO_TRACK_EVAL.ALL, tracksOfInterest, "1 Jan 2012 12:02:00.000"
        )

    # endregion

    # region DetermineIfAnyTrackIsVisibleFromOtherStkObject
    def test_DetermineIfAnyTrackIsVisibleFromOtherStkObject(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "J2Satellite"),
            ISatellite,
        )
        satellite.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60
        j2prop.propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineIfAnyTrackIsVisibleFromOtherStkObject(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "J2Satellite")

    def DetermineIfAnyTrackIsVisibleFromOtherStkObject(self, root: "IStkObjectRoot", mto: "IMto"):
        mtoVisibility: "IMtoAnalysisVisibility" = mto.analysis.visibility
        mtoVisibility.use_terrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.entirety = MTO_ENTIRETY.PARTIAL  # Only applies if MTO is static (i.e. non time dependent).

        mtoVisibility.stk_object_path = "Satellite/J2Satellite"
        anyTrackIsVisible: bool = mtoVisibility.is_any_track_visible("1 Jan 2012 14:02:00.000")

    # endregion

    # region DetermineIfAllTracksAreVisible
    def test_DetermineIfAllTracksAreVisible(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "J2Satellite"),
            ISatellite,
        )
        satellite.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60
        j2prop.propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineIfAllTracksAreVisible(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "J2Satellite")

    def DetermineIfAllTracksAreVisible(self, root: "IStkObjectRoot", mto: "IMto"):
        # Are all the tracks visible from the other STK Object at the specified time?

        mtoVisibility: "IMtoAnalysisVisibility" = mto.analysis.visibility
        mtoVisibility.use_terrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.entirety = MTO_ENTIRETY.PARTIAL  # Only applies if MTO is static (i.e. non time dependent).

        mtoVisibility.stk_object_path = "Satellite/J2Satellite"
        allTracksAreVisible: bool = mtoVisibility.are_all_tracks_visible("1 Jan 2012 14:02:00.000")

    # endregion

    # region ExtendMtoTrack
    def test_ExtendMtoTrack(self):
        Mto.m_Object.tracks.add(1)
        self.ExtendMtoTrack(Mto.m_Object.tracks[0].points)

    def ExtendMtoTrack(self, trackPointCollection: "IMtoTrackPointCollection"):
        time = ["1 Jan 2012 12:20:00.000", "1 Jan 2012 12:30:00.000"]
        latitude = [-18.35, 19.55]
        longitude = [-42.1, 83.21]
        altitude = [30.52, 15.81]

        # Extend expects each parameter to be a two dimensional array,
        # all arrays must have the same length
        trackPointCollection.extend(time, latitude, longitude, altitude)

    # endregion

    # region AddMtoTrack
    def test_AddMtoTrack(self):
        self.AddMtoTrack(Mto.m_Object)

    def AddMtoTrack(self, mto: "IMto"):
        trackCollection: "IMtoTrackCollection" = mto.tracks

        time = ["1 Jan 2012 12:10:00.000", "1 Jan 2012 12:20:00.000"]
        latitude = [27.97, -26.51]
        longitude = [-80.01, 119.42]
        altitude = [20.1, 44.2]

        # AddTrack expects each safe array parameter to be two dimensional,
        # all arrays must have the same length
        track: "IMtoTrack" = trackCollection.add_track(1, time, latitude, longitude, altitude)

    # endregion

    # region LoadMtoTrackPointsFromFile
    def test_LoadMtoTrackPointsFromFile(self):
        Mto.m_Object.tracks.add(0)
        self.LoadMtoTrackPointsFromFile(
            Mto.m_Object.tracks[0], TestBase.GetScenarioFile("CodeSnippetsTests", "TestEph.e")
        )

    def LoadMtoTrackPointsFromFile(self, track: "IMtoTrack", filePath: str):
        # LoadPoints expects the path an Ephemeris file path
        track.points.load_points(filePath)

    # endregion

    # region RemoveMtoTrackByIds
    def test_RemoveMtoTracks(self):
        Mto.m_Object.tracks.add(1)
        Mto.m_Object.tracks.add(4)
        self.RemoveMtoTrackByIds(Mto.m_Object)

    def RemoveMtoTrackByIds(self, mto: "IMto"):
        trackCollection: "IMtoTrackCollection" = mto.tracks

        # RemoveTracksById expects a one dimensional array of mto track ids
        tracks = [1, 4]
        trackCollection.remove_tracks_by_id(tracks)

    # endregion

    # region RemoveMtoTrack
    def test_RemoveMtoTrack(self):
        Mto.m_Object.tracks.add(0)
        Mto.m_Object.tracks.add(1)
        Mto.m_Object.tracks.add(2)
        Mto.m_Object.tracks.add(3)
        self.RemoveMtoTrack(Mto.m_Object)

    def RemoveMtoTrack(self, mto: "IMto"):
        trackCollection: "IMtoTrackCollection" = mto.tracks

        # Build tracksToRemove Array
        tracksToRemove = [trackCollection[0], trackCollection[1]]

        # RemoveTracks expects a one dimensional array of IMtoTrack objects
        trackCollection.remove_tracks(tracksToRemove)

    # endregion

    # region ComputeMtoRange
    def test_ComputeMtoRange(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "J2Satellite"),
            ISatellite,
        )
        satellite.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60
        j2prop.propagate()

        Mto.m_Object.tracks.add(1)
        Mto.m_Object.tracks.add(4)

        self.ComputeMtoRange(Mto.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "J2Satellite")

    def ComputeMtoRange(self, mto: "IMto"):
        range: "IMtoAnalysisRange" = mto.analysis.range
        range.stk_object_path = "Satellite/J2Satellite"

        # ComputeRanges expects a one dimensional array of mto track ids
        # ComputeRanges returns a two dimensional array of track id, visibility, and range
        tracks = [1, 4]

        result = range.compute_ranges(MTO_RANGE_MODE.EACH, tracks, "1 Jan 2012 12:00:00.000")

        i: int = 0
        while i < len(result):
            Console.WriteLine("Track #: {0}, Visible: {1}, Range: {2}", result[i][0], result[i][1], result[i][2])

            i += 1

    # endregion

    # region ComputeMtoFieldOfView
    def test_ComputeMtoFieldOfView(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "J2Satellite"),
            ISatellite,
        )
        satellite.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60
        j2prop.propagate()

        Mto.m_Object.tracks.add(1)
        Mto.m_Object.tracks.add(4)

        sensor1: "ISensor" = clr.CastAs(
            (clr.Convert(satellite, IStkObject)).children.new(STK_OBJECT_TYPE.SENSOR, "Sensor1"), ISensor
        )
        self.ComputeMtoFieldOfView(Mto.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "J2Satellite")

    def ComputeMtoFieldOfView(self, mto: "IMto"):
        fov: "IMtoAnalysisFieldOfView" = mto.analysis.field_of_view
        fov.sensor = "Satellite/J2Satellite/Sensor/Sensor1"

        # AreTracksInFOV expects a one dimensional array of mto track ids
        tracks = [1, 4]

        tracksInView: bool = fov.are_tracks_in_fov(MTO_TRACK_EVAL.ANY, tracks, "1 Jan 2012 12:00:00.000")

    # endregion
