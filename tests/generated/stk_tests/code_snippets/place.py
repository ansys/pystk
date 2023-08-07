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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.ePlace, Place.m_DefaultName),
            IPlace,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.ePlace, Place.m_DefaultName)
        Place.m_Object = None

    # endregion

    # region CreateDefaultPlaceOnCurrentScenarioCentralBody
    def test_CreateDefaultPlaceOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.ePlace, Place.m_DefaultName)
        self.CreateDefaultPlaceOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateDefaultPlaceOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create a place on current scenario central body
        place: "IPlace" = clr.CastAs(root.current_scenario.children.new(AgESTKObjectType.ePlace, "MyPlace"), IPlace)

    # endregion

    # region CreatePlaceOnEarth
    def test_CreatePlaceOnEarth(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.ePlace, Place.m_DefaultName)
        self.CreatePlaceOnEarth(CodeSnippetsTestBase.m_Root)

    def CreatePlaceOnEarth(self, root: "IStkObjectRoot"):
        place: "IPlace" = clr.CastAs(
            root.current_scenario.children.new_on_central_body(AgESTKObjectType.ePlace, "MyPlace", "Earth"), IPlace
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        place.position.assign_planetodetic(0.4506, -1.4011, 4)

    # endregion

    # region CreatePlaceOnOtherPlanet
    def test_CreatePlaceOnOtherPlanet(self):
        self.CreatePlaceOnOtherPlanet(CodeSnippetsTestBase.m_Root)

    def CreatePlaceOnOtherPlanet(self, root: "IStkObjectRoot"):
        placeObject: "IPlace" = clr.CastAs(
            root.current_scenario.children.new_on_central_body(AgESTKObjectType.ePlace, "Place1", "Mars"), IPlace
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        placeObject.position.assign_planetodetic(-5.4245, 0.1902, 0)

    # endregion

    # region CreatePlaceFromFacilityDatabase
    def test_CreatePlaceFromFacilityDatabase(self):
        self.CreatePlaceFromFacilityDatabase(CodeSnippetsTestBase.m_Root)

    def CreatePlaceFromFacilityDatabase(self, root: "IStkObjectRoot"):
        # Get STK database location using Connect
        result: "IExecCmdResult" = root.execute_command("GetDirectory / Database Facility")
        facDataDir: str = result[0]
        filelocation: str = Path.Combine(facDataDir, "stkFacility.fd")

        # Import object from database using Connect
        command: str = ('ImportFromDB * Facility "' + filelocation) + '" Class Place SiteName Weilheim'
        root.execute_command(command)

        place: "IPlace" = clr.CastAs(root.get_object_from_path("Place/Weilheim"), IPlace)

    # endregion

    # region ChangePositionWithUseTerrain
    def test_ChangePositionWithUseTerrain(self):
        self.ChangePositionWithUseTerrain(Place.m_Object)

    def ChangePositionWithUseTerrain(self, place: "IPlace"):
        # Set altitude automatically by using terrain data
        place.use_terrain = True

        # Set the position ignores the altitude value in AssignGeodetic
        place.position.assign_geodetic(29.98, -90.25, 9)

        # Ignores the altitude value in AssignGeocentric
        place.position.assign_geocentric(32.12, -110.93, 787)

        # Ignores the radius value in AssignSpherical
        place.position.assign_spherical(40.65, -73.78, 7)

    # endregion
