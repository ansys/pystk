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
        Planet.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.ePlanet, Planet.m_DefaultName),
            IPlanet,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.ePlanet, Planet.m_DefaultName)
        Planet.m_Object = None

    # endregion

    # region SpecifyPlanetPositionUsingCommonTasks
    def test_SpecifyPlanetPositionUsingCommonTasks(self):
        self.SpecifyPlanetPositionUsingCommonTasks(
            Planet.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "Venus.pe")
        )

    def SpecifyPlanetPositionUsingCommonTasks(self, planet: "IPlanet", planetEphemeris: str):
        # Position source files traditionally have .pe extensions
        planet.common_tasks.set_position_source_file(planetEphemeris)

    # endregion

    # region ConfigurePlanet
    def test_ConfigurePlanet(self):
        self.ConfigurePlanet(Planet.m_Object)
        body: "IPlanetPositionCentralBody" = clr.CastAs(
            Planet.m_Object.position_source_data, IPlanetPositionCentralBody
        )

    def ConfigurePlanet(self, planet: "IPlanet"):
        planet.position_source = AgEPlPositionSourceType.ePosCentralBody

        # Get IAgPlPosCentralBody interface
        body: "IPlanetPositionCentralBody" = clr.CastAs(planet.position_source_data, IPlanetPositionCentralBody)

        body.auto_rename = False
        body.central_body = "Jupiter"
        if Array.IndexOf(body.available_ephem_source_types, int(AgEEphemSourceType.eEphemAnalytic)) != -1:
            body.ephem_source = AgEEphemSourceType.eEphemAnalytic

    # endregion

    # region ConfigurePlanetGraphics
    @category("Graphics Tests")
    def test_ConfigurePlanetGraphics(self):
        self.ConfigurePlanetGraphics(Planet.m_Object.graphics)

    def ConfigurePlanetGraphics(self, graphics: "IPlanetGraphics"):
        graphics.inherit = False

        graphics.color = Color.Red
        graphics.marker_style = "Circle"
        graphics.line_style = AgELineStyle.eMDashDot
        graphics.line_width = AgELineWidth.e4

        graphics.inertial_position_visible = False
        graphics.sub_planet_point_visible = False
        graphics.position_label_visible = False
        graphics.sub_planet_label_visible = False
        graphics.orbit_visible = True
        graphics.orbit_display = AgEPlOrbitDisplayType.eOrbitDisplayTime
        displayTime: "IPlanetOrbitDisplayTime" = clr.CastAs(graphics.orbit_display_data, IPlanetOrbitDisplayTime)
        displayTime.time = 10000.0

    # endregion
