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
        result: "IExecCmdResult" = root.execute_command("New / */Satellite JeffSAT")

    # endregion

    # region ExecuteMultipleConnectCommands
    @category("Graphics Tests")
    def test_ExecuteMultipleConnectCommands(self):
        self.ExecuteMultipleConnectCommands(CodeSnippetsTestBase.m_Root)

    def ExecuteMultipleConnectCommands(self, root: "IStkObjectRoot"):
        connectCommands = ["New / */Satellite MySatellite", "Graphics */Satellite/MySatellite SetColor red"]

        # ExecuteMultipleCommands expect a one dimensional array of Connect commands
        result: "IExecMultiCmdResult" = root.execute_multiple_commands(
            connectCommands, EXEC_MULTI_CMD_RESULT_ACTION.EXCEPTION_ON_ERROR
        )

    # endregion

    # region ExtractDataFromExecConnectResult
    def test_ExtractDataFromExecConnectResult(self):
        result: "IExecCmdResult" = CodeSnippetsTestBase.m_Root.execute_command("GetSTKVersion /")
        self.ExtractDataFromExecConnectResult(result)

    def ExtractDataFromExecConnectResult(self, result: "IExecCmdResult"):
        if result.is_succeeded:
            i: int = 0
            while i < result.count:
                Console.WriteLine(result[i])

                i += 1

    # endregion

    # region ExtractDataFromMultiExecConnectResult
    def test_ExtractDataFromMultiExecConnectResult(self):
        obj = ["GetSTKVersion /"]

        result: "IExecMultiCmdResult" = CodeSnippetsTestBase.m_Root.execute_multiple_commands(
            obj, EXEC_MULTI_CMD_RESULT_ACTION.CONTINUE_ON_ERROR
        )
        self.ExtractDataFromMultiExecConnectResult(result)

    def ExtractDataFromMultiExecConnectResult(self, result: "IExecMultiCmdResult"):
        i: int = 0
        while i < result.count:
            if result[i].is_succeeded:
                j: int = 0
                while j < result[i].count:
                    Console.WriteLine(result[j])

                    j += 1

            i += 1

    # endregion
