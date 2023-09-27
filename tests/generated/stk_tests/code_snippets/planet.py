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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.PLANET, Planet.m_DefaultName),
            IPlanet,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.PLANET, Planet.m_DefaultName)
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
        planet.position_source = PLANET_POSITION_SOURCE_TYPE.POSITION_CENTRAL_BODY

        # Get IPlanetPositionCentralBody interface
        body: "IPlanetPositionCentralBody" = clr.CastAs(planet.position_source_data, IPlanetPositionCentralBody)

        body.auto_rename = False
        body.central_body = "Jupiter"
        if Array.IndexOf(body.available_ephem_source_types, int(EPHEM_SOURCE_TYPE.ANALYTIC)) != -1:
            body.ephem_source = EPHEM_SOURCE_TYPE.ANALYTIC

    # endregion

    # region ConfigurePlanetGraphics
    @category("Graphics Tests")
    def test_ConfigurePlanetGraphics(self):
        self.ConfigurePlanetGraphics(Planet.m_Object.graphics)

    def ConfigurePlanetGraphics(self, graphics: "IPlanetGraphics"):
        graphics.inherit = False

        graphics.color = Color.Red
        graphics.marker_style = "Circle"
        graphics.line_style = LINE_STYLE.M_DASH_DOT
        graphics.line_width = LINE_WIDTH.WIDTH4

        graphics.inertial_position_visible = False
        graphics.sub_planet_point_visible = False
        graphics.position_label_visible = False
        graphics.sub_planet_label_visible = False
        graphics.orbit_visible = True
        graphics.orbit_display = PLANET_ORBIT_DISPLAY_TYPE.ORBIT_DISPLAY_TIME
        displayTime: "IPlanetOrbitDisplayTime" = clr.CastAs(graphics.orbit_display_data, IPlanetOrbitDisplayTime)
        displayTime.time = 10000.0

    # endregion
