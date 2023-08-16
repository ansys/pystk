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
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "Satellite1")
        self.DelayGraphicsUpdates(CodeSnippetsTestBase.m_Root)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "Satellite1")

    def DelayGraphicsUpdates(self, root: "IStkObjectRoot"):
        satellite: "ISatellite" = clr.CastAs(root.current_scenario.children["Satellite1"], ISatellite)
        voElt: "IVODataDisplayElement" = satellite.vo.data_display[0]

        root.begin_update()  # Suspend updates

        # Put modifications here
        voElt.is_visible = True
        voElt.use_background = True
        voElt.bg_color = Color.Green
        voElt.use_background = False

        root.end_update()  # Resume updates now

    # endregion
