from test_util import *
from ansys.stk.core.graphics import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class CodeSnippetsTestBase(TestBase):
    def __init__(self, *args, **kwargs):
        super(CodeSnippetsTestBase, self).__init__(*args, **kwargs)

    m_Root: "IStkObjectRoot" = None

    @staticmethod
    def Initialize():
        TestBase.Initialize()
        CodeSnippetsTestBase.m_Root = TestBase.Application
        CodeSnippetsTestBase.SafeScenarioUnload()

        TestBase.Application.NewScenario("CodeSnippetScenario")
        scenario = clr.Convert(TestBase.Application.CurrentScenario, IScenario)
        scenario.SetTimePeriod("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")

    @staticmethod
    def InitializeWithNewScenario(makeNewScenario: bool):
        TestBase.Initialize()
        CodeSnippetsTestBase.m_Root = TestBase.Application
        CodeSnippetsTestBase.SafeScenarioUnload()
        if makeNewScenario:
            TestBase.Application.NewScenario("CodeSnippetScenario")
            scenario = clr.Convert(TestBase.Application.CurrentScenario, IScenario)
            scenario.SetTimePeriod("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")

    @staticmethod
    def Uninitialize():
        CodeSnippetsTestBase.SafeScenarioUnload()
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()
        TestBase.Uninitialize()

    @staticmethod
    def SafeScenarioUnload():
        if CodeSnippetsTestBase.m_Root.CurrentScenario != None:
            CodeSnippetsTestBase.m_Root.CloseScenario()
