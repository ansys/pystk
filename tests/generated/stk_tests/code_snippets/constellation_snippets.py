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
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class ConstellationSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ConstellationSnippets, self).__init__(*args, **kwargs)

    m_Object: "Constellation" = None
    m_DefaultName: str = "constellation1"

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
        ConstellationSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.CONSTELLATION, ConstellationSnippets.m_DefaultName
            ),
            Constellation,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.CONSTELLATION, ConstellationSnippets.m_DefaultName
        )
        ConstellationSnippets.m_Object = None

    # endregion

    # region AddObjectToConstellationUsingIAgStkObjectInterface
    def test_AddObjectToConstellationUsingIAgStkObjectInterface(self):
        alos: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "Alos")
        self.AddObjectToConstellationUsingIAgStkObjectInterface(ConstellationSnippets.m_Object, alos)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, alos.instance_name)

    def AddObjectToConstellationUsingIAgStkObjectInterface(self, constellation: "Constellation", alos: "IStkObject"):
        # Add object to constellation
        constellation.objects.add_object(alos)

    # endregion

    # region AddObjectToConstellationByStkPath
    def test_AddObjectToConstellationByStkPath(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "Cameo")
        self.AddObjectToConstellationByStkPath(ConstellationSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "Cameo")

    def AddObjectToConstellationByStkPath(self, constellation: "Constellation"):
        # Add object to constellation
        constellation.objects.add("Satellite/Cameo")

    # endregion
