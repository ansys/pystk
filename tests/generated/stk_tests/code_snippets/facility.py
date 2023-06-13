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
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eFacility, Facility.m_DefaultName
            ),
            IFacility,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, Facility.m_DefaultName)
        Facility.m_Object = None

    # endregion

    # region CreateDefaultFacilityOnCurrentScenarioCentralBody
    def test_CreateDefaultFacilityOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, Facility.m_DefaultName)
        self.CreateDefaultFacilityOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateDefaultFacilityOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create a facility on current scenario central body
        facility = clr.CastAs(root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "MyFacility"), IFacility)

    # endregion

    # region CreateFacilityOnEarth
    def test_CreateFacilityOnEarth(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, Facility.m_DefaultName)
        self.CreateFacilityOnEarth(CodeSnippetsTestBase.m_Root)

    def CreateFacilityOnEarth(self, root: "IStkObjectRoot"):
        facility = clr.CastAs(
            root.CurrentScenario.Children.NewOnCentralBody(AgESTKObjectType.eFacility, "MyFacility", "Earth"), IFacility
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        facility.Position.AssignPlanetodetic(0.4506, -1.4011, 4)

    # endregion

    # region CreateFacilityOnOtherPlanet
    def test_CreateFacilityOnOtherPlanet(self):
        self.CreateFacilityOnOtherPlanet(CodeSnippetsTestBase.m_Root)

    def CreateFacilityOnOtherPlanet(self, root: "IStkObjectRoot"):
        facObject = clr.CastAs(
            root.CurrentScenario.Children.NewOnCentralBody(AgESTKObjectType.eFacility, "Facility1", "Mars"), IFacility
        )

        # Assuming unit preferences are set to radians for latitude and longitude and km for distance
        facObject.Position.AssignPlanetodetic(-5.4245, 0.1902, 0)

    # endregion

    # region CreateFacilityFromFacilityDatabase
    def test_CreateFacilityFromFacilityDatabase(self):
        self.CreateFacilityFromFacilityDatabase(CodeSnippetsTestBase.m_Root)

    def CreateFacilityFromFacilityDatabase(self, root: "IStkObjectRoot"):
        # Get STK database location using Connect
        result = root.ExecuteCommand("GetDirectory / Database Facility")
        facDataDir = result[0]
        filelocation = Path.Combine(facDataDir, r"stkFacility.fd")

        # Import object from database using Connect
        command = ('ImportFromDB * Facility "' + filelocation) + '" Class Facility SiteName Weilheim'
        root.ExecuteCommand(command)

        facility = clr.CastAs(root.GetObjectFromPath("Facility/Weilheim"), IFacility)

    # endregion

    # region ChangePositionWithUseTerrain
    def test_ChangePositionWithUseTerrain(self):
        self.ChangePositionWithUseTerrain(Facility.m_Object)

    def ChangePositionWithUseTerrain(self, fac: "IFacility"):
        # Set altitude automatically by using terrain data
        fac.UseTerrain = True

        # Set the position ignores the altitude value in AssignGeodetic
        fac.Position.AssignGeodetic(29.98, -90.25, 9)

        # Ignores the altitude value in AssignGeocentric
        fac.Position.AssignGeocentric(32.12, -110.93, 787)

        # Ignores the radius value in AssignSpherical
        fac.Position.AssignSpherical(40.65, -73.78, 7)

    # endregion
