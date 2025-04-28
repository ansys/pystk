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


class StkExternalSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkExternalSnippets, self).__init__(*args, **kwargs)

    m_Object: "Satellite" = None
    m_DefaultName: str = "MySatellite"

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
        StkExternalSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.SATELLITE, StkExternalSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, StkExternalSnippets.m_DefaultName
        )
        StkExternalSnippets.m_Object = None

    # endregion

    # region CreateSatelliteFromExternalEphemerisFile
    def test_CreateSatelliteFromExternalEphemerisFile(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, StkExternalSnippets.m_DefaultName
        )
        self.CreateSatelliteFromExternalEphemerisFile(
            CodeSnippetsTestBase.m_Root, TestBase.GetScenarioFile("CodeSnippetsTests", "TestEph.e")
        )

    def CreateSatelliteFromExternalEphemerisFile(self, root: "StkObjectRoot", ephemerisFilePath: str):
        satellite: "Satellite" = clr.CastAs(
            root.current_scenario.children.new(STKObjectType.SATELLITE, "MySatellite"), Satellite
        )

        # Configure propagator's external file path
        satellite.set_propagator_type(PropagatorType.STK_EXTERNAL)
        ext: "PropagatorStkExternal" = clr.CastAs(satellite.propagator, PropagatorStkExternal)
        ext.filename = ephemerisFilePath

        # Propagate
        ext.propagate()

    # endregion
