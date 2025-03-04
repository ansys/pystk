# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

from ansys.stk.core.stkobjects import CoverageBounds, CoverageDataRetention, DataSaveMode, STKObjectType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class CoverageDefinitionSnippets(CodeSnippetsTestBase):
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

    @category("Graphics Tests")
    def test_CreateCoverageSnippet(self):
        try:
            scenario = self.get_scenario()
            MyAreaTarget = self.get_scenario().children.new(STKObjectType.AREA_TARGET, "MyAreaTarget")
            MySatellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "MySatellite")
            MySatellite.propagator.propagate()

            self.CreateCoverageSnippet(scenario)
        finally:
            MyAreaTarget.unload()
            MySatellite.unload()

    @code_snippet(
        name="CreateCoverage",
        description="Create a New Coverage Definition (on the current scenario central body)",
        category="STK Objects | Coverage Definition",
        eid="STKObjects~IAgCoverageDefinition",
    )
    def CreateCoverageSnippet(self, scenario):
        # Scenario scenario: Scenario object
        # Create new Coverage Definition and set the Bounds to an area target
        coverage = scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "MyCoverage")
        coverage.grid.bounds_type = CoverageBounds.CUSTOM_REGIONS
        covGrid = coverage.grid
        bounds = covGrid.bounds
        bounds.area_targets.add("AreaTarget/MyAreaTarget")
        # Define the Grid Resolution
        Res = covGrid.resolution
        Res.latitude_longitude = 0.5  # deg
        # Set the satellite as the Asset
        coverage.asset_list.add("Satellite/MySatellite")

        # Turn off Show Grid Points
        coverage.graphics.static.show_points = False

    def test_CoverageIntervalSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()
            coverage = self.get_scenario().children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")

            self.CoverageIntervalSnippet(satellite, coverage)
        finally:
            satellite.unload()
            coverage.unload()

    @code_snippet(
        name="SetCoverageIntervalToAvailability",
        description="Set the Coverage Interval to an object's availability Analysis interval",
        category="STK Objects | Coverage Definition",
        eid="STKObjects~IAgCoverageDefinition",
    )
    def CoverageIntervalSnippet(self, satellite, coverage):
        # Satellite satellite: Satellite object
        # CoverageDefinition coverage: Coverage object
        satVGT = satellite.analysis_workbench_components
        AvailTimeSpan = satVGT.time_intervals.item("AvailabilityTimeSpan")
        IntResult = AvailTimeSpan.find_interval()
        coverage.interval.analysis_interval.set_start_and_stop_times(IntResult.interval.start, IntResult.interval.stop)

    def test_CoverageAdvancedSnippet(self):
        try:
            coverage = self.get_scenario().children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")

            self.CoverageAdvancedSnippet(coverage)
        finally:
            coverage.unload()

    @code_snippet(
        name="CoverageAdvanced",
        description="Set Advanced Settings for Coverage",
        category="STK Objects | Coverage Definition",
        eid="STKObjects~IAgCoverageDefinition",
    )
    def CoverageAdvancedSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        advanced = coverage.advanced
        advanced.recompute_automatically = False
        advanced.data_retention = CoverageDataRetention.ALL_DATA
        advanced.save_mode = DataSaveMode.SAVE_ACCESSES

    def test_CoverageComputeSnippet(self):
        try:
            coverage = self.get_scenario().children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")

            self.CoverageComputeSnippet(coverage)
        finally:
            coverage.unload()

    @code_snippet(
        name="CoverageCompute",
        description="Compute Coverage",
        category="STK Objects | Coverage Definition",
        eid="STKObjects~IAgCoverageDefinition",
    )
    def CoverageComputeSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        coverage.compute_accesses()
