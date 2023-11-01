from test_util import *
from ansys.stk.core.graphics import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class CodeSnippetsTestBase(TestBase):
    def __init__(self, *args, **kwargs):
        super(CodeSnippetsTestBase, self).__init__(*args, **kwargs)

    m_Root: "StkObjectRoot" = None

    @staticmethod
    def Initialize():
        TestBase.Initialize()
        CodeSnippetsTestBase.m_Root = TestBase.Application
        CodeSnippetsTestBase.SafeScenarioUnload()

        TestBase.Application.new_scenario("CodeSnippetScenario")
        scenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)
        scenario.set_time_period("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")

    @staticmethod
    def InitializeWithNewScenario(makeNewScenario: bool):
        TestBase.Initialize()
        CodeSnippetsTestBase.m_Root = TestBase.Application
        CodeSnippetsTestBase.SafeScenarioUnload()
        if makeNewScenario:
            TestBase.Application.new_scenario("CodeSnippetScenario")
            scenario: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)
            scenario.set_time_period("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")

    @staticmethod
    def Uninitialize():
        CodeSnippetsTestBase.SafeScenarioUnload()
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()
        TestBase.Uninitialize()

    @staticmethod
    def SafeScenarioUnload():
        if CodeSnippetsTestBase.m_Root.current_scenario != None:
            CodeSnippetsTestBase.m_Root.close_scenario()
