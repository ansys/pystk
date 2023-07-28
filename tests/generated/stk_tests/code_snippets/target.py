from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Target(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object = None
        super(Target, self).__init__(*args, **kwargs)

    m_DefaultName: str = "MyTarget"

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
        self.m_Object: ITarget = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eTarget, Target.m_DefaultName),
            ITarget,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eTarget, Target.m_DefaultName)
        self.m_Object = None

    # endregion

    # region CreateTargetOnCurrentScenarioCentralBody
    def test_CreateTargetOnCurrentScenarioCentralBody(self):
        self.CreateTargetOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateTargetOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Target on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        areaTarget: ITarget = clr.CastAs(
            root.CurrentScenario.Children.New(AgESTKObjectType.eAreaTarget, "MyAreaTarget"), ITarget
        )

    # endregion

    # region ChangeTargetPosition
    def test_ChangeTargetPosition(self):
        self.ChangeTargetPosition(self.m_Object)

    def ChangeTargetPosition(self, target: "ITarget"):
        pos = target.Position
        pos.AssignGeodetic(39.95, 15.58, 231.54)

    # endregion

    # region ConfigureTargetAzElMask
    def test_ConfigureTargetAzElMask(self):
        self.ConfigureTargetAzElMask(self.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "maskfile.aem"))

    def ConfigureTargetAzElMask(self, target: "ITarget", maskfile: str):
        target.UseLocalTimeOffset = True
        target.LocalTimeOffset = 200.0
        target.UseTerrain = True
        # Note, if SetAzElMask is set to a type other than AgEAzElMaskType.eMaskFile,
        # the second parameter is ignored.
        target.SetAzElMask(AgEAzElMaskType.eMaskFile, maskfile)
        target.TerrainNorm = AgETerrainNormType.eSlopeAzimuth
        target.AltRef = AgEAltRefType.eMSL
        target.HeightAboveGround = 1472.0

    # endregion
