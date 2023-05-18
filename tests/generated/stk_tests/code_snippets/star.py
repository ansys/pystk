import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Star(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Star, self).__init__(*args, **kwargs)

    m_Object = None
    m_DefaultName = "star1"

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
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eStar, Star.m_DefaultName), IStar
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eStar, Star.m_DefaultName)
        Star.m_Object = None

    # endregion

    # region CreateStarOnCurrentScenarioCentralBody
    def test_CreateStarOnCurrentScenarioCentralBody(self):
        self.CreateStarOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateStarOnCurrentScenarioCentralBody(self, root):
        # Create the Star
        star = clr.CastAs(root.CurrentScenario.Children.New(AgESTKObjectType.eStar, "MyStar"), IStar)

    # endregion

    # region DefineStarBasicProperties
    def test_DefineStarBasicProperties(self):
        star = clr.CastAs(CodeSnippetsTestBase.m_Root.CurrentScenario.Children[Star.m_DefaultName], IStar)
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("TimeUnit", "yr")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("AngleUnit", "arcSec")
        self.DefineStarBasicProperties(star)
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("TimeUnit", "min")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("AngleUnit", "deg")

    def DefineStarBasicProperties(self, star):
        # Units depend on current unit preferences
        star.LocationDeclination = -40.0
        star.LocationRightAscension = 120.0  # in arcSec
        star.Magnitude = -1.0
        star.Parallax = 0.0  # in arcSec
        star.ProperMotionDeclination = 1.5  # in arcSec
        star.ProperMotionRadialVelocity = 0.75  # in meters
        star.ProperMotionRightAscension = -0.5  # in arcSec

    # endregion

    # region CreateStarFromStarDatabase
    def test_CreateStarFromStarDatabase(self):
        Star.CreateStarFromStarDatabase(CodeSnippetsTestBase.m_Root)

    @staticmethod
    def CreateStarFromStarDatabase(root):
        # Import object from database using Connect
        command = "ImportFromDB * Star ScenarioCollection VisualMagnitude 0 1.0 RightAsc 200.0 230.0 Constellation ImportedFromStarDB"
        root.ExecuteCommand(command)

        star = clr.CastAs(root.GetObjectFromPath("Star/Star-65474"), IStar)

    # endregion
