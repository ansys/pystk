from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Place(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Place, self).__init__(*args, **kwargs)

    m_Object: "IPlace" = None
    m_DefaultName: str = "MyPlace"

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

    # region TestSetUp
    def setUp(self):
        Place.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.ePlace, Place.m_DefaultName),
            IPlace,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.ePlace, Place.m_DefaultName)
        Place.m_Object = None

    # endregion

    # region CreateDefaultPlaceOnCurrentScenarioCentralBody
    def test_CreateDefaultPlaceOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.ePlace, Place.m_DefaultName)
        self.CreateDefaultPlaceOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateDefaultPlaceOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create a place on current scenario central body
        place: "IPlace" = clr.CastAs(root.CurrentScenario.Children.New(AgESTKObjectType.ePlace, "MyPlace"), IPlace)

    # endregion

    # region CreatePlaceOnEarth
    def test_CreatePlaceOnEarth(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.ePlace, Place.m_DefaultName)
        self.CreatePlaceOnEarth(CodeSnippetsTestBase.m_Root)

    def CreatePlaceOnEarth(self, root: "IStkObjectRoot"):
        place: "IPlace" = clr.CastAs(
            root.CurrentScenario.Children.NewOnCentralBody(AgESTKObjectType.ePlace, "MyPlace", "Earth"), IPlace
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        place.Position.AssignPlanetodetic(0.4506, -1.4011, 4)

    # endregion

    # region CreatePlaceOnOtherPlanet
    def test_CreatePlaceOnOtherPlanet(self):
        self.CreatePlaceOnOtherPlanet(CodeSnippetsTestBase.m_Root)

    def CreatePlaceOnOtherPlanet(self, root: "IStkObjectRoot"):
        placeObject: "IPlace" = clr.CastAs(
            root.CurrentScenario.Children.NewOnCentralBody(AgESTKObjectType.ePlace, "Place1", "Mars"), IPlace
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        placeObject.Position.AssignPlanetodetic(-5.4245, 0.1902, 0)

    # endregion

    # region CreatePlaceFromFacilityDatabase
    def test_CreatePlaceFromFacilityDatabase(self):
        self.CreatePlaceFromFacilityDatabase(CodeSnippetsTestBase.m_Root)

    def CreatePlaceFromFacilityDatabase(self, root: "IStkObjectRoot"):
        # Get STK database location using Connect
        result: "IExecCmdResult" = root.ExecuteCommand("GetDirectory / Database Facility")
        facDataDir: str = result[0]
        filelocation: str = Path.Combine(facDataDir, "stkFacility.fd")

        # Import object from database using Connect
        command: str = ('ImportFromDB * Facility "' + filelocation) + '" Class Place SiteName Weilheim'
        root.ExecuteCommand(command)

        place: "IPlace" = clr.CastAs(root.GetObjectFromPath("Place/Weilheim"), IPlace)

    # endregion

    # region ChangePositionWithUseTerrain
    def test_ChangePositionWithUseTerrain(self):
        self.ChangePositionWithUseTerrain(Place.m_Object)

    def ChangePositionWithUseTerrain(self, place: "IPlace"):
        # Set altitude automatically by using terrain data
        place.UseTerrain = True

        # Set the position ignores the altitude value in AssignGeodetic
        place.Position.AssignGeodetic(29.98, -90.25, 9)

        # Ignores the altitude value in AssignGeocentric
        place.Position.AssignGeocentric(32.12, -110.93, 787)

        # Ignores the radius value in AssignSpherical
        place.Position.AssignSpherical(40.65, -73.78, 7)

    # endregion
