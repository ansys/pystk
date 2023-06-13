from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class Interfaces(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Interfaces, self).__init__(*args, **kwargs)

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
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region LoadVDF
    def test_LoadVDF(self):
        CodeSnippetsTestBase.m_Root.CloseScenario()
        self.LoadVDF(
            CodeSnippetsTestBase.m_Root,
            Path.Combine(TestBase.GetSTKHomeDir(), r"Data\ExampleScenarios\Intro_STK_Aircraft_Systems.vdf"),
            "",
        )

    def LoadVDF(self, root: "IStkObjectRoot", vdfPath: str, vdfPassword: str):
        # Pass an empty string if there is no password to the VDF.
        root.LoadVDF(vdfPath, vdfPassword)

    # endregion
