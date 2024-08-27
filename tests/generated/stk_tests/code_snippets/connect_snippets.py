from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class ConnectSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ConnectSnippets, self).__init__(*args, **kwargs)

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

    def ExecuteConnectCommand(self, root: "StkObjectRoot"):
        result: "ExecuteCommandResult" = root.execute_command("New / */Satellite JeffSAT")

    # endregion

    # region ExecuteMultipleConnectCommands
    @category("Graphics Tests")
    def test_ExecuteMultipleConnectCommands(self):
        self.ExecuteMultipleConnectCommands(CodeSnippetsTestBase.m_Root)

    def ExecuteMultipleConnectCommands(self, root: "StkObjectRoot"):
        connectCommands = ["New / */Satellite MySatellite", "Graphics */Satellite/MySatellite SetColor red"]

        # ExecuteMultipleCommands expect a one dimensional array of Connect commands
        result: "ExecuteMultipleCommandResult" = root.execute_multiple_commands(
            connectCommands, EXECUTE_MULTIPLE_COMMANDS_MODE.EXCEPTION_ON_ERROR
        )

    # endregion

    # region ExtractDataFromExecConnectResult
    def test_ExtractDataFromExecConnectResult(self):
        result: "ExecuteCommandResult" = CodeSnippetsTestBase.m_Root.execute_command("GetSTKVersion /")
        self.ExtractDataFromExecConnectResult(result)

    def ExtractDataFromExecConnectResult(self, result: "ExecuteCommandResult"):
        if result.is_succeeded:
            i: int = 0
            while i < result.count:
                Console.WriteLine(result[i])

                i += 1

    # endregion

    # region ExtractDataFromMultiExecConnectResult
    def test_ExtractDataFromMultiExecConnectResult(self):
        obj = ["GetSTKVersion /"]

        result: "ExecuteMultipleCommandResult" = CodeSnippetsTestBase.m_Root.execute_multiple_commands(
            obj, EXECUTE_MULTIPLE_COMMANDS_MODE.CONTINUE_ON_ERROR
        )
        self.ExtractDataFromMultiExecConnectResult(result)

    def ExtractDataFromMultiExecConnectResult(self, result: "ExecuteMultipleCommandResult"):
        i: int = 0
        while i < result.count:
            if result[i].is_succeeded:
                j: int = 0
                while j < result[i].count:
                    Console.WriteLine(result[j])

                    j += 1

            i += 1

    # endregion
