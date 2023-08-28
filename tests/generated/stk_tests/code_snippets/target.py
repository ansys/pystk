from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Target(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object: "ITarget" = None
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
        self.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.TARGET, Target.m_DefaultName),
            ITarget,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.TARGET, Target.m_DefaultName)
        self.m_Object = None

    # endregion

    # region CreateTargetOnCurrentScenarioCentralBody
    def test_CreateTargetOnCurrentScenarioCentralBody(self):
        self.CreateTargetOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateTargetOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Target on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        areaTarget: "ITarget" = clr.CastAs(
            root.current_scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "MyAreaTarget"), ITarget
        )

    # endregion

    # region ChangeTargetPosition
    def test_ChangeTargetPosition(self):
        self.ChangeTargetPosition(self.m_Object)

    def ChangeTargetPosition(self, target: "ITarget"):
        pos: "IPosition" = target.position
        pos.assign_geodetic(39.95, 15.58, 231.54)

    # endregion

    # region ConfigureTargetAzElMask
    def test_ConfigureTargetAzElMask(self):
        self.ConfigureTargetAzElMask(self.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "maskfile.aem"))

    def ConfigureTargetAzElMask(self, target: "ITarget", maskfile: str):
        target.use_local_time_offset = True
        target.local_time_offset = 200.0
        target.use_terrain = True
        # Note, if SetAzElMask is set to a type other than AZ_EL_MASK_TYPE.eMaskFile,
        # the second parameter is ignored.
        target.set_az_el_mask(AZ_EL_MASK_TYPE.MASK_FILE, maskfile)
        target.terrain_norm = TERRAIN_NORM_TYPE.SLOPE_AZIMUTH
        target.alt_ref = ALT_REF_TYPE.MSL
        target.height_above_ground = 1472.0

    # endregion
