# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        scenario.set_time_period("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")

    @staticmethod
    def InitializeWithNewScenario(makeNewScenario: bool):
        TestBase.Initialize()
        CodeSnippetsTestBase.m_Root = TestBase.Application
        CodeSnippetsTestBase.SafeScenarioUnload()
        if makeNewScenario:
            TestBase.Application.new_scenario("CodeSnippetScenario")
            scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
            scenario.set_time_period("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")

    @staticmethod
    def Uninitialize():
        CodeSnippetsTestBase.SafeScenarioUnload()
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()
        TestBase.Uninitialize()

    @staticmethod
    def SafeScenarioUnload():
        if CodeSnippetsTestBase.m_Root.current_scenario != None:
            CodeSnippetsTestBase.m_Root.close_scenario()
