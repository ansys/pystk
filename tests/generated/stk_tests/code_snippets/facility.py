from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Facility(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Facility, self).__init__(*args, **kwargs)

    m_Object: "IFacility" = None
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
        Facility.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, Facility.m_DefaultName),
            IFacility,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, Facility.m_DefaultName)
        Facility.m_Object = None

    # endregion

    # region CreateDefaultFacilityOnCurrentScenarioCentralBody
    def test_CreateDefaultFacilityOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, Facility.m_DefaultName)
        self.CreateDefaultFacilityOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateDefaultFacilityOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create a facility on current scenario central body
        facility: "IFacility" = clr.CastAs(
            root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "MyFacility"), IFacility
        )

    # endregion

    # region CreateFacilityOnEarth
    def test_CreateFacilityOnEarth(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, Facility.m_DefaultName)
        self.CreateFacilityOnEarth(CodeSnippetsTestBase.m_Root)

    def CreateFacilityOnEarth(self, root: "IStkObjectRoot"):
        facility: "IFacility" = clr.CastAs(
            root.current_scenario.children.new_on_central_body(STK_OBJECT_TYPE.FACILITY, "MyFacility", "Earth"),
            IFacility,
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        facility.position.assign_planetodetic(0.4506, -1.4011, 4)

    # endregion

    # region CreateFacilityOnOtherPlanet
    def test_CreateFacilityOnOtherPlanet(self):
        self.CreateFacilityOnOtherPlanet(CodeSnippetsTestBase.m_Root)

    def CreateFacilityOnOtherPlanet(self, root: "IStkObjectRoot"):
        facObject: "IFacility" = clr.CastAs(
            root.current_scenario.children.new_on_central_body(STK_OBJECT_TYPE.FACILITY, "Facility1", "Mars"), IFacility
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        facObject.position.assign_planetodetic(-5.4245, 0.1902, 0)

    # endregion

    # region CreateFacilityFromFacilityDatabase
    def test_CreateFacilityFromFacilityDatabase(self):
        self.CreateFacilityFromFacilityDatabase(CodeSnippetsTestBase.m_Root)

    def CreateFacilityFromFacilityDatabase(self, root: "IStkObjectRoot"):
        # Get STK database location using Connect
        result: "IExecCmdResult" = root.execute_command("GetDirectory / Database Facility")
        facDataDir: str = result[0]
        filelocation: str = Path.Combine(facDataDir, r"stkFacility.fd")

        # Import object from database using Connect
        command: str = ('ImportFromDB * Facility "' + filelocation) + '" Class Facility SiteName Weilheim'
        root.execute_command(command)

        facility: "IFacility" = clr.CastAs(root.get_object_from_path("Facility/Weilheim"), IFacility)

    # endregion

    # region ChangePositionWithUseTerrain
    def test_ChangePositionWithUseTerrain(self):
        self.ChangePositionWithUseTerrain(Facility.m_Object)

    def ChangePositionWithUseTerrain(self, fac: "IFacility"):
        # Set altitude automatically by using terrain data
        fac.use_terrain = True

        # Set the position ignores the altitude value in AssignGeodetic
        fac.position.assign_geodetic(29.98, -90.25, 9)

        # Ignores the altitude value in AssignGeocentric
        fac.position.assign_geocentric(32.12, -110.93, 787)

        # Ignores the radius value in AssignSpherical
        fac.position.assign_spherical(40.65, -73.78, 7)

    # endregion
