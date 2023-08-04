from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Star(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Star, self).__init__(*args, **kwargs)

    m_Object: "IStar" = None
    m_DefaultName: str = "star1"

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
        Star.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eStar, Star.m_DefaultName), IStar
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eStar, Star.m_DefaultName)
        Star.m_Object = None

    # endregion

    # region CreateStarOnCurrentScenarioCentralBody
    def test_CreateStarOnCurrentScenarioCentralBody(self):
        self.CreateStarOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateStarOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Star
        star: "IStar" = clr.CastAs(root.current_scenario.children.new(AgESTKObjectType.eStar, "MyStar"), IStar)

    # endregion

    # region DefineStarBasicProperties
    def test_DefineStarBasicProperties(self):
        star: "IStar" = clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario.children[Star.m_DefaultName], IStar)
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("TimeUnit", "yr")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("AngleUnit", "arcSec")
        self.DefineStarBasicProperties(star)
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("TimeUnit", "min")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("AngleUnit", "deg")

    def DefineStarBasicProperties(self, star: "IStar"):
        # Units depend on current unit preferences
        star.location_declination = -40.0
        star.location_right_ascension = 120.0  # in arcSec
        star.magnitude = -1.0
        star.parallax = 0.0  # in arcSec
        star.proper_motion_declination = 1.5  # in arcSec
        star.proper_motion_radial_velocity = 0.75  # in meters
        star.proper_motion_right_ascension = -0.5  # in arcSec

    # endregion

    # region CreateStarFromStarDatabase
    def test_CreateStarFromStarDatabase(self):
        Star.CreateStarFromStarDatabase(CodeSnippetsTestBase.m_Root)

    @staticmethod
    def CreateStarFromStarDatabase(root: "IStkObjectRoot"):
        # Import object from database using Connect
        command: str = "ImportFromDB * Star ScenarioCollection VisualMagnitude 0 1.0 RightAsc 200.0 230.0 Constellation ImportedFromStarDB"
        root.execute_command(command)

        star: "IStar" = clr.CastAs(root.get_object_from_path("Star/Star-65474"), IStar)

    # endregion
