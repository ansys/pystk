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
        Mto.m_Object: IMto = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eMTO, Mto.m_DefaultName), IMto
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eMTO, Mto.m_DefaultName)
        Mto.m_Object = None

    # endregion

    # region ConfigureMtos
    def test_ConfigureMtos(self):
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("DateFormat", "UTCG")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("Angle", "deg")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("Distance", "m")
        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

    def ConfigureMtos(self, root: "IStkObjectRoot", mto: "IMto"):
        scenario: IScenario = clr.CastAs(root.CurrentScenario, IScenario)
        scenario.SetTimePeriod("1 Feb 2008 12:00:00.000", "2 Feb 2008 12:00:00.000")

        # Number of tracks and points to add
        trackCount = 10
        pointCount = 20

        # Initial values from which we will interpolate
        lat0 = 40.04
        lon0 = -75.595
        alt0 = 0

        root.BeginUpdate()  # Call BeginUpdate for STK engine to delay updates

        i = 0
        while i < trackCount:
            track = mto.Tracks.Add(i)
            date = root.ConversionUtility.NewDate("UTCG", str(scenario.StartTime))

            j = 0
            while j < pointCount:
                lat = lat0 + (1 * i)
                lon = lon0 + (0.1 * j)
                alt = alt0

                date = date.Add("sec", 120)

                track.Points.AddPoint(date.Format("UTCG"), lat, lon, alt)

                j += 1

            i += 1

        root.EndUpdate()

    # endregion

    # region ConfigureMtoGraphics
    @category("Graphics Tests")
    def test_ConfigureMtoGraphics(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Satellite1")
        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        self.ConfigureMtoGraphics(Mto.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "Satellite1")

    def ConfigureMtoGraphics(self, mto: "IMto"):
        tracks = mto.VO.Tracks
        for element in tracks:
            element.Marker.PixelSize = 12
            element.Marker.OrientationMode = AgEVOMarkerOrientation.eVOMarkerOrientationAngle
            element.Marker.XOrigin = AgEVOMarkerOriginType.eRight
            element.Marker.YOrigin = AgEVOMarkerOriginType.eBottom
            element.Marker.Angle = 1.23

            element.Marker.MarkerType = AgEMarkerType.eImageFile
            element.Marker.SetMarkerImageFile(r"STKData\VO\Markers\Fire.ppm")

            element.Model.IsVisible = True
            element.Model.Filename = r"STKData\VO\Models\Land\ariane-lp.mdl"
            element.Model.InitialBearing = 3.0
            element.Model.ScaleValue = 2.0
            element.Model.ZPointsNadir = True

            element.Label.Enable = True
            element.Label.X = 33.5
            element.Label.Y = 82.2
            element.Label.Z = 100.0
            element.Label.OffsetFrame = AgEOffsetFrameType.eOffsetFrameCartesian

    # endregion

    # region ConfigureMtoTrackModel
    @category("Graphics Tests")
    def test_ConfigureMtoTrackModel(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Satellite1")
        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        self.ConfigureMtoTrackModel(Mto.m_Object.VO.Tracks[0])
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "Satellite1")

    def ConfigureMtoTrackModel(self, track: "IMtoVOTrack"):
        model = track.Model
        model.IsVisible = True
        model.Filename = r"STKData\VO\Models\Land\ariane-lp.mdl"
        model.InitialBearing = 3.0
        model.ScaleValue = 2.0
        model.ZPointsNadir = True

    # endregion

    # region ConfigureMtoTrackMarker
    @category("Graphics Tests")
    def test_ConfigureMtoTrackMarker(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Satellite1")
        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        self.ConfigureMtoTrackMarker(Mto.m_Object.VO.Tracks[0])
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "Satellite1")

    def ConfigureMtoTrackMarker(self, track: "IMtoVOTrack"):
        marker = track.Marker
        marker.PixelSize = 12
        marker.OrientationMode = AgEVOMarkerOrientation.eVOMarkerOrientationAngle
        marker.XOrigin = AgEVOMarkerOriginType.eRight
        marker.YOrigin = AgEVOMarkerOriginType.eBottom
        marker.Angle = 1.23
        marker.MarkerType = AgEMarkerType.eImageFile
        marker.SetMarkerImageFile(r"STKData\VO\Markers\Fire.ppm")

    # endregion

    # region CreateMtoOnCurrentScenarioCentralBody
    def test_CreateMtoOnCurrentScenarioCentralBody(self):
        # Unload because all other code snippet's want the mto already loaded except for this one.
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eMTO, Mto.m_DefaultName)
        self.CreateMtoOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateMtoOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the MTO
        mto: IMto = clr.CastAs(root.CurrentScenario.Children.New(AgESTKObjectType.eMTO, "mto1"), IMto)

    # endregion

    # region DetermineWhichTracksAreVisibleFromOtherStkObjectAtSpecifiedTime
    def test_DetermineWhichTracksAreVisibleFromOtherStkObjectAtSpecifiedTime(self):
        satellite: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "J2Satellite"),
            ISatellite,
        )
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: IVehiclePropagatorJ2Perturbation = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.Step = 60
        j2prop.Propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineWhichTracksAreVisibleFromOtherStkObjectAtSpecifiedTime(Mto.m_Object)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "J2Satellite")

    def DetermineWhichTracksAreVisibleFromOtherStkObjectAtSpecifiedTime(self, mto: "IMto"):
        mtoVisibility = mto.Analysis.Visibility
        mtoVisibility.UseTerrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.Entirety = (
            AgEMtoEntirety.eMtoEntiretyPartial
        )  # Only applies if MTO is static (i.e. non time dependent).

        mtoVisibility.StkObjectPath = "Satellite/J2Satellite"

        # ComputeAllTracks returns a two dimensional array whose elements are trackid and visibility
        trackVisibilityArray = mtoVisibility.ComputeAllTracks(
            AgEMtoVisibilityMode.eVisibilityModeEach, "1 Jan 2012 12:00:00.000"
        )

        # Output results
        Console.WriteLine("ComputeAllTracks:")

        i = 0
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
        satellite: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "J2Satellite"),
            ISatellite,
        )
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: IVehiclePropagatorJ2Perturbation = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.Step = 60
        j2prop.Propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineWhichTracksOfSpecifiedSubsetOfTracksAreVisibleFromOtherStkObject(
            CodeSnippetsTestBase.m_Root, Mto.m_Object
        )

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "J2Satellite")

    def DetermineWhichTracksOfSpecifiedSubsetOfTracksAreVisibleFromOtherStkObject(
        self, root: "IStkObjectRoot", mto: "IMto"
    ):
        mtoVisibility = mto.Analysis.Visibility
        mtoVisibility.UseTerrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.Entirety = (
            AgEMtoEntirety.eMtoEntiretyPartial
        )  # Only applies if MTO is static (i.e. non time dependent).

        tracksOfInterest = [1, 2, 7]

        mtoVisibility.StkObjectPath = "Satellite/J2Satellite"

        # ComputeTracks expects as the second parameter a one dimensional array of mto track ids
        # ComputeTracks returns a two dimensional array whose values are track id and visiblity
        trackVisibilityArray = mtoVisibility.ComputeTracks(
            AgEMtoVisibilityMode.eVisibilityModeEach, tracksOfInterest, "1 Jan 2012 12:05:00.000"
        )

        # Output results
        Console.WriteLine("ComputeTracks:")

        i = 0
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
        satellite: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "J2Satellite"),
            ISatellite,
        )
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: IVehiclePropagatorJ2Perturbation = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.Step = 60
        j2prop.Propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineIfAllTracksAreVisibleFromOtherStkObject(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "J2Satellite")

    def DetermineIfAllTracksAreVisibleFromOtherStkObject(self, root: "IStkObjectRoot", mto: "IMto"):
        mtoVisibility = mto.Analysis.Visibility
        mtoVisibility.UseTerrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.Entirety = (
            AgEMtoEntirety.eMtoEntiretyPartial
        )  # Only applies if MTO is static (i.e. non time dependent).

        mtoVisibility.StkObjectPath = "Satellite/J2Satellite"

        tracksOfInterest = [1, 2, 7]

        # AreTracksVisible expects as the second parameter a one dimensional array of mto track ids
        areTracksAreVisible = mtoVisibility.AreTracksVisible(
            AgEMtoTrackEval.eMtoTrackEvalAll, tracksOfInterest, "1 Jan 2012 12:02:00.000"
        )

    # endregion

    # region DetermineIfAnyTrackIsVisibleFromOtherStkObject
    def test_DetermineIfAnyTrackIsVisibleFromOtherStkObject(self):
        satellite: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "J2Satellite"),
            ISatellite,
        )
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: IVehiclePropagatorJ2Perturbation = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.Step = 60
        j2prop.Propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineIfAnyTrackIsVisibleFromOtherStkObject(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "J2Satellite")

    def DetermineIfAnyTrackIsVisibleFromOtherStkObject(self, root: "IStkObjectRoot", mto: "IMto"):
        mtoVisibility = mto.Analysis.Visibility
        mtoVisibility.UseTerrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.Entirety = (
            AgEMtoEntirety.eMtoEntiretyPartial
        )  # Only applies if MTO is static (i.e. non time dependent).

        mtoVisibility.StkObjectPath = "Satellite/J2Satellite"
        anyTrackIsVisible = mtoVisibility.IsAnyTrackVisible("1 Jan 2012 14:02:00.000")

    # endregion

    # region DetermineIfAllTracksAreVisible
    def test_DetermineIfAllTracksAreVisible(self):
        satellite: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "J2Satellite"),
            ISatellite,
        )
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: IVehiclePropagatorJ2Perturbation = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.Step = 60
        j2prop.Propagate()

        self.ConfigureMtos(CodeSnippetsTestBase.m_Root, Mto.m_Object)

        self.DetermineIfAllTracksAreVisible(CodeSnippetsTestBase.m_Root, Mto.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "J2Satellite")

    def DetermineIfAllTracksAreVisible(self, root: "IStkObjectRoot", mto: "IMto"):
        # Are all the tracks visible from the other STK Object at the specified time?

        mtoVisibility = mto.Analysis.Visibility
        mtoVisibility.UseTerrain = False  # Set to true to use terrain instead of line of sight.
        mtoVisibility.Entirety = (
            AgEMtoEntirety.eMtoEntiretyPartial
        )  # Only applies if MTO is static (i.e. non time dependent).

        mtoVisibility.StkObjectPath = "Satellite/J2Satellite"
        allTracksAreVisible = mtoVisibility.AreAllTracksVisible("1 Jan 2012 14:02:00.000")

    # endregion

    # region ExtendMtoTrack
    def test_ExtendMtoTrack(self):
        Mto.m_Object.Tracks.Add(1)
        self.ExtendMtoTrack(Mto.m_Object.Tracks[0].Points)

    def ExtendMtoTrack(self, trackPointCollection: "IMtoTrackPointCollection"):
        time = ["1 Jan 2012 12:20:00.000", "1 Jan 2012 12:30:00.000"]
        latitude = [-18.35, 19.55]
        longitude = [-42.1, 83.21]
        altitude = [30.52, 15.81]

        # Extend expects each parameter to be a two dimensional array,
        # all arrays must have the same length
        trackPointCollection.Extend(time, latitude, longitude, altitude)

    # endregion

    # region AddMtoTrack
    def test_AddMtoTrack(self):
        self.AddMtoTrack(Mto.m_Object)

    def AddMtoTrack(self, mto: "IMto"):
        trackCollection = mto.Tracks

        time = ["1 Jan 2012 12:10:00.000", "1 Jan 2012 12:20:00.000"]
        latitude = [27.97, -26.51]
        longitude = [-80.01, 119.42]
        altitude = [20.1, 44.2]

        # AddTrack expects each safe array parameter to be two dimensional,
        # all arrays must have the same length
        track = trackCollection.AddTrack(1, time, latitude, longitude, altitude)

    # endregion

    # region LoadMtoTrackPointsFromFile
    def test_LoadMtoTrackPointsFromFile(self):
        Mto.m_Object.Tracks.Add(0)
        self.LoadMtoTrackPointsFromFile(Mto.m_Object.Tracks[0], TestBase.GetScenarioFile("TestEph.e"))

    def LoadMtoTrackPointsFromFile(self, track: "IMtoTrack", filePath: str):
        # LoadPoints expects the path an Ephemeris file path
        track.Points.LoadPoints(filePath)

    # endregion

    # region RemoveMtoTrackByIds
    def test_RemoveMtoTracks(self):
        Mto.m_Object.Tracks.Add(1)
        Mto.m_Object.Tracks.Add(4)
        self.RemoveMtoTrackByIds(Mto.m_Object)

    def RemoveMtoTrackByIds(self, mto: "IMto"):
        trackCollection = mto.Tracks

        # RemoveTracksById expects a one dimensional array of mto track ids
        tracks = [1, 4]
        trackCollection.RemoveTracksById(tracks)

    # endregion

    # region RemoveMtoTrack
    def test_RemoveMtoTrack(self):
        Mto.m_Object.Tracks.Add(0)
        Mto.m_Object.Tracks.Add(1)
        Mto.m_Object.Tracks.Add(2)
        Mto.m_Object.Tracks.Add(3)
        self.RemoveMtoTrack(Mto.m_Object)

    def RemoveMtoTrack(self, mto: "IMto"):
        trackCollection = mto.Tracks

        # Build tracksToRemove Array
        tracksToRemove = [trackCollection[0], trackCollection[1]]

        # RemoveTracks expects a one dimensional array of IAgMtoTrack objects
        trackCollection.RemoveTracks(tracksToRemove)

    # endregion

    # region ComputeMtoRange
    def test_ComputeMtoRange(self):
        satellite: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "J2Satellite"),
            ISatellite,
        )
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: IVehiclePropagatorJ2Perturbation = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.Step = 60
        j2prop.Propagate()

        Mto.m_Object.Tracks.Add(1)
        Mto.m_Object.Tracks.Add(4)

        self.ComputeMtoRange(Mto.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "J2Satellite")

    def ComputeMtoRange(self, mto: "IMto"):
        range = mto.Analysis.Range
        range.StkObjectPath = "Satellite/J2Satellite"

        # ComputeRanges expects a one dimensional array of mto track ids
        # ComputeRanges returns a two dimensional array of track id, visibility, and range
        tracks = [1, 4]

        result = range.ComputeRanges(AgEMtoRangeMode.eMtoRangeModeEach, tracks, "1 Jan 2012 12:00:00.000")

        i = 0
        while i < len(result):
            Console.WriteLine("Track #: {0}, Visible: {1}, Range: {2}", result[i][0], result[i][1], result[i][2])

            i += 1

    # endregion

    # region ComputeMtoFieldOfView
    def test_ComputeMtoFieldOfView(self):
        satellite: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "J2Satellite"),
            ISatellite,
        )
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop: IVehiclePropagatorJ2Perturbation = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.Step = 60
        j2prop.Propagate()

        Mto.m_Object.Tracks.Add(1)
        Mto.m_Object.Tracks.Add(4)

        sensor1: ISensor = clr.CastAs(
            (clr.Convert(satellite, IStkObject)).Children.New(AgESTKObjectType.eSensor, "Sensor1"), ISensor
        )
        self.ComputeMtoFieldOfView(Mto.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "J2Satellite")

    def ComputeMtoFieldOfView(self, mto: "IMto"):
        fov = mto.Analysis.FieldOfView
        fov.Sensor = "Satellite/J2Satellite/Sensor/Sensor1"

        # AreTracksInFOV expects a one dimensional array of mto track ids
        tracks = [1, 4]

        tracksInView = fov.AreTracksInFOV(AgEMtoTrackEval.eMtoTrackEvalAny, tracks, "1 Jan 2012 12:00:00.000")

    # endregion
