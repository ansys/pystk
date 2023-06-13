from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class VO(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(VO, self).__init__(*args, **kwargs)

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

    # region SetUp
    def setUp(self):
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region DelayGraphicsUpdates
    @category("VO Tests")
    def test_DelayGraphicsUpdates(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Satellite1")
        self.DelayGraphicsUpdates(CodeSnippetsTestBase.m_Root)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "Satellite1")

    def DelayGraphicsUpdates(self, root: "IStkObjectRoot"):
        satellite = clr.CastAs(root.CurrentScenario.Children["Satellite1"], ISatellite)
        voElt = satellite.VO.DataDisplay[0]

        root.BeginUpdate()  # Suspend updates

        # Put modifications here
        voElt.IsVisible = True
        voElt.UseBackground = True
        voElt.BgColor = Color.Green
        voElt.UseBackground = False

        root.EndUpdate()  # Resume updates now

    # endregion
