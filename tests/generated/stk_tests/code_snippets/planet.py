from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Planet(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Planet, self).__init__(*args, **kwargs)

    m_Object: "IPlanet" = None
    m_DefaultName: str = "MyPlanet"

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
        Planet.m_Object: IPlanet = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.ePlanet, Planet.m_DefaultName),
            IPlanet,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.ePlanet, Planet.m_DefaultName)
        Planet.m_Object = None

    # endregion

    # region SpecifyPlanetPositionUsingCommonTasks
    def test_SpecifyPlanetPositionUsingCommonTasks(self):
        self.SpecifyPlanetPositionUsingCommonTasks(
            Planet.m_Object, TestBase.GetScenarioFile(TestBase.PathCombine("CodeSnippetsTests", "Venus.pe"))
        )

    def SpecifyPlanetPositionUsingCommonTasks(self, planet: "IPlanet", planetEphemeris: str):
        # Position source files traditionally have .pe extensions
        planet.CommonTasks.SetPositionSourceFile(planetEphemeris)

    # endregion

    # region ConfigurePlanet
    def test_ConfigurePlanet(self):
        self.ConfigurePlanet(Planet.m_Object)
        body: IPlanetPositionCentralBody = clr.CastAs(Planet.m_Object.PositionSourceData, IPlanetPositionCentralBody)

    def ConfigurePlanet(self, planet: "IPlanet"):
        planet.PositionSource = AgEPlPositionSourceType.ePosCentralBody

        # Get IAgPlPosCentralBody interface
        body: IPlanetPositionCentralBody = clr.CastAs(planet.PositionSourceData, IPlanetPositionCentralBody)

        body.AutoRename = False
        body.CentralBody = "Jupiter"
        if Array.IndexOf(body.AvailableEphemSourceTypes, int(AgEEphemSourceType.eEphemAnalytic)) != -1:
            body.EphemSource = AgEEphemSourceType.eEphemAnalytic

    # endregion

    # region ConfigurePlanetGraphics
    @category("Graphics Tests")
    def test_ConfigurePlanetGraphics(self):
        self.ConfigurePlanetGraphics(Planet.m_Object.Graphics)

    def ConfigurePlanetGraphics(self, graphics: "IPlanetGraphics"):
        graphics.Inherit = False

        graphics.Color = Color.Red
        graphics.MarkerStyle = "Circle"
        graphics.LineStyle = AgELineStyle.eMDashDot
        graphics.LineWidth = AgELineWidth.e4

        graphics.InertialPositionVisible = False
        graphics.SubPlanetPointVisible = False
        graphics.PositionLabelVisible = False
        graphics.SubPlanetLabelVisible = False
        graphics.OrbitVisible = True
        graphics.OrbitDisplay = AgEPlOrbitDisplayType.eOrbitDisplayTime
        displayTime: IPlanetOrbitDisplayTime = clr.CastAs(graphics.OrbitDisplayData, IPlanetOrbitDisplayTime)
        displayTime.Time = 10000.0

    # endregion
