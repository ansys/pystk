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

import os
import sys

from ansys.stk.core.stkobjects import FigureOfMeritCompute, FigureOfMeritDefinitionType, STKObjectType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class ObjectCoverageSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_root(self):
        return CodeSnippetsTestBase.m_Root

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.current_scenario

    def test_ComputeObjectCoverageSnippet(self):
        try:
            aircraft = self.get_scenario().children.new(STKObjectType.AIRCRAFT, "aircraft")
            MySatellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "MySatellite")
            MySatellite.propagator.propagate()

            self.ComputeObjectCoverageSnippet(aircraft)
        finally:
            aircraft.unload()
            MySatellite.unload()

    @code_snippet(
        name="ComputeObjectCoverage",
        description="Compute Object Coverage",
        category="STK Objects | Object Coverage",
        eid="stkobjects~ObjectCoverage",
    )
    def ComputeObjectCoverageSnippet(self, aircraft):
        # Aircraft aircraft: Aircraft object
        objCoverage = aircraft.object_coverage
        objCoverage.assets.remove_all
        objCoverage.assets.add("Satellite/MySatellite")
        objCoverage.use_object_times = True
        objCoverage.compute()

        objCoverageFOM = objCoverage.figure_of_merit
        objCoverageFOM.set_definition_type(FigureOfMeritDefinitionType.COVERAGE_TIME)
        objCoverageFOM.definition.set_compute_type(FigureOfMeritCompute.TOTAL)
