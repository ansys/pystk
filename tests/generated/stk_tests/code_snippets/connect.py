from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Connect(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Connect, self).__init__(*args, **kwargs)

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

    # region ExecuteConnectCommand
    def test_ExecuteConnectCommand(self):
        self.ExecuteConnectCommand(CodeSnippetsTestBase.m_Root)

    def ExecuteConnectCommand(self, root: "IStkObjectRoot"):
        result: "IExecCmdResult" = root.ExecuteCommand("New / */Satellite JeffSAT")

    # endregion

    # region ExecuteMultipleConnectCommands
    @category("Graphics Tests")
    def test_ExecuteMultipleConnectCommands(self):
        self.ExecuteMultipleConnectCommands(CodeSnippetsTestBase.m_Root)

    def ExecuteMultipleConnectCommands(self, root: "IStkObjectRoot"):
        connectCommands = ["New / */Satellite MySatellite", "Graphics */Satellite/MySatellite SetColor red"]

        # ExecuteMultipleCommands expect a one dimensional array of Connect commands
        result: "IExecMultiCmdResult" = root.ExecuteMultipleCommands(
            connectCommands, AgEExecMultiCmdResultAction.eExceptionOnError
        )

    # endregion

    # region ExtractDataFromExecConnectResult
    def test_ExtractDataFromExecConnectResult(self):
        result: "IExecCmdResult" = CodeSnippetsTestBase.m_Root.ExecuteCommand("GetSTKVersion /")
        self.ExtractDataFromExecConnectResult(result)

    def ExtractDataFromExecConnectResult(self, result: "IExecCmdResult"):
        if result.IsSucceeded:
            i: int = 0
            while i < result.Count:
                Console.WriteLine(result[i])

                i += 1

    # endregion

    # region ExtractDataFromMultiExecConnectResult
    def test_ExtractDataFromMultiExecConnectResult(self):
        obj = ["GetSTKVersion /"]

        result: "IExecMultiCmdResult" = CodeSnippetsTestBase.m_Root.ExecuteMultipleCommands(
            obj, AgEExecMultiCmdResultAction.eContinueOnError
        )
        self.ExtractDataFromMultiExecConnectResult(result)

    def ExtractDataFromMultiExecConnectResult(self, result: "IExecMultiCmdResult"):
        i: int = 0
        while i < result.Count:
            if result[i].IsSucceeded:
                j: int = 0
                while j < result[i].Count:
                    Console.WriteLine(result[j])

                    j += 1

            i += 1

    # endregion
