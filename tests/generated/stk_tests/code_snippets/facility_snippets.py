from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class FacilitySnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(FacilitySnippets, self).__init__(*args, **kwargs)

    m_Object: "Facility" = None
    m_DefaultName: str = "MyFacility"

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
        FacilitySnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.FACILITY, FacilitySnippets.m_DefaultName
            ),
            Facility,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.FACILITY, FacilitySnippets.m_DefaultName
        )
        FacilitySnippets.m_Object = None

    # endregion

    # region CreateDefaultFacilityOnCurrentScenarioCentralBody
    def test_CreateDefaultFacilityOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.FACILITY, FacilitySnippets.m_DefaultName
        )
        self.CreateDefaultFacilityOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateDefaultFacilityOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create a facility on current scenario central body
        facility: "Facility" = clr.CastAs(
            root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "MyFacility"), Facility
        )

    # endregion

    # region CreateFacilityOnEarth
    def test_CreateFacilityOnEarth(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.FACILITY, FacilitySnippets.m_DefaultName
        )
        self.CreateFacilityOnEarth(CodeSnippetsTestBase.m_Root)

    def CreateFacilityOnEarth(self, root: "StkObjectRoot"):
        facility: "Facility" = clr.CastAs(
            root.current_scenario.children.new_on_central_body(STK_OBJECT_TYPE.FACILITY, "MyFacility", "Earth"),
            Facility,
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        facility.position.assign_planetodetic(0.4506, -1.4011, 4)

    # endregion

    # region CreateFacilityOnOtherPlanet
    def test_CreateFacilityOnOtherPlanet(self):
        self.CreateFacilityOnOtherPlanet(CodeSnippetsTestBase.m_Root)

    def CreateFacilityOnOtherPlanet(self, root: "StkObjectRoot"):
        facObject: "Facility" = clr.CastAs(
            root.current_scenario.children.new_on_central_body(STK_OBJECT_TYPE.FACILITY, "Facility1", "Mars"), Facility
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        facObject.position.assign_planetodetic(-5.4245, 0.1902, 0)

    # endregion

    # region CreateFacilityFromFacilityDatabase
    def test_CreateFacilityFromFacilityDatabase(self):
        self.CreateFacilityFromFacilityDatabase(CodeSnippetsTestBase.m_Root)

    def CreateFacilityFromFacilityDatabase(self, root: "StkObjectRoot"):
        # Get STK database location using Connect
        result: "ExecCmdResult" = root.execute_command("GetDirectory / Database Facility")
        facDataDir: str = result[0]
        filelocation: str = Path.Combine(facDataDir, r"stkFacility.fd")

        # Import object from database using Connect
        command: str = ('ImportFromDB * Facility "' + filelocation) + '" Class Facility SiteName Weilheim'
        root.execute_command(command)

        facility: "Facility" = clr.CastAs(root.get_object_from_path("Facility/Weilheim"), Facility)

    # endregion

    # region ChangePositionWithUseTerrain
    def test_ChangePositionWithUseTerrain(self):
        self.ChangePositionWithUseTerrain(FacilitySnippets.m_Object)

    def ChangePositionWithUseTerrain(self, fac: "Facility"):
        # Set altitude automatically by using terrain data
        fac.use_terrain = True

        # Set the position ignores the altitude value in AssignGeodetic
        fac.position.assign_geodetic(29.98, -90.25, 9)

        # Ignores the altitude value in AssignGeocentric
        fac.position.assign_geocentric(32.12, -110.93, 787)

        # Ignores the radius value in AssignSpherical
        fac.position.assign_spherical(40.65, -73.78, 7)

    # endregion
