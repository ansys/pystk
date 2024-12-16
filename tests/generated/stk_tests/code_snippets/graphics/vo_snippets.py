from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class VOSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(VOSnippets, self).__init__(*args, **kwargs)

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
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite1")
        self.DelayGraphicsUpdates(CodeSnippetsTestBase.m_Root)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "Satellite1")

    def DelayGraphicsUpdates(self, root: "StkObjectRoot"):
        satellite: "Satellite" = clr.CastAs(root.current_scenario.children["Satellite1"], Satellite)
        voElt: "Graphics3DDataDisplayElement" = satellite.graphics_3d.data_display[0]

        root.begin_update()  # Suspend updates

        # Put modifications here
        voElt.show_graphics = True
        voElt.use_background = True
        voElt.background_color = Colors.Green
        voElt.use_background = False

        root.end_update()  # Resume updates now

    # endregion
