from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class PlaceSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(PlaceSnippets, self).__init__(*args, **kwargs)

    m_Object: "Place" = None
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
        PlaceSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.PLACE, PlaceSnippets.m_DefaultName
            ),
            Place,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.PLACE, PlaceSnippets.m_DefaultName)
        PlaceSnippets.m_Object = None

    # endregion

    # region CreateDefaultPlaceOnCurrentScenarioCentralBody
    def test_CreateDefaultPlaceOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.PLACE, PlaceSnippets.m_DefaultName)
        self.CreateDefaultPlaceOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateDefaultPlaceOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create a place on current scenario central body
        place: "Place" = clr.CastAs(root.current_scenario.children.new(STK_OBJECT_TYPE.PLACE, "MyPlace"), Place)

    # endregion

    # region CreatePlaceOnEarth
    def test_CreatePlaceOnEarth(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.PLACE, PlaceSnippets.m_DefaultName)
        self.CreatePlaceOnEarth(CodeSnippetsTestBase.m_Root)

    def CreatePlaceOnEarth(self, root: "StkObjectRoot"):
        place: "Place" = clr.CastAs(
            root.current_scenario.children.new_on_central_body(STK_OBJECT_TYPE.PLACE, "MyPlace", "Earth"), Place
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        place.position.assign_planetodetic(0.4506, -1.4011, 4)

    # endregion

    # region CreatePlaceOnOtherPlanet
    def test_CreatePlaceOnOtherPlanet(self):
        self.CreatePlaceOnOtherPlanet(CodeSnippetsTestBase.m_Root)

    def CreatePlaceOnOtherPlanet(self, root: "StkObjectRoot"):
        placeObject: "Place" = clr.CastAs(
            root.current_scenario.children.new_on_central_body(STK_OBJECT_TYPE.PLACE, "Place1", "Mars"), Place
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        placeObject.position.assign_planetodetic(-5.4245, 0.1902, 0)

    # endregion

    # region CreatePlaceFromFacilityDatabase
    def test_CreatePlaceFromFacilityDatabase(self):
        self.CreatePlaceFromFacilityDatabase(CodeSnippetsTestBase.m_Root)

    def CreatePlaceFromFacilityDatabase(self, root: "StkObjectRoot"):
        # Get STK database location using Connect
        result: "ExecCmdResult" = root.execute_command("GetDirectory / Database Facility")
        facDataDir: str = result[0]
        filelocation: str = Path.Combine(facDataDir, "stkFacility.fd")

        # Import object from database using Connect
        command: str = ('ImportFromDB * Facility "' + filelocation) + '" Class Place SiteName Weilheim'
        root.execute_command(command)

        place: "Place" = clr.CastAs(root.get_object_from_path("Place/Weilheim"), Place)

    # endregion

    # region ChangePositionWithUseTerrain
    def test_ChangePositionWithUseTerrain(self):
        self.ChangePositionWithUseTerrain(PlaceSnippets.m_Object)

    def ChangePositionWithUseTerrain(self, place: "Place"):
        # Set altitude automatically by using terrain data
        place.use_terrain = True

        # Set the position ignores the altitude value in AssignGeodetic
        place.position.assign_geodetic(29.98, -90.25, 9)

        # Ignores the altitude value in AssignGeocentric
        place.position.assign_geocentric(32.12, -110.93, 787)

        # Ignores the radius value in AssignSpherical
        place.position.assign_spherical(40.65, -73.78, 7)

    # endregion
