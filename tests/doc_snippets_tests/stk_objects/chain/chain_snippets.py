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

from ansys.stk.core.stkobjects import ChainTimePeriodType, DataSaveMode, STKObjectType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class ChainSnippets(CodeSnippetsTestBase):
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

    def test_CreateChainSnippet(self):
        self.CreateChainSnippet(self.get_root())

    @code_snippet(
        name="CreateChain",
        description="Create a chain (on the current scenario central body)",
        category="STK Objects | Chain",
        eid="stkobjects~Chain",
    )
    def CreateChainSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        # Create the Chain on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        chain = root.current_scenario.children.new(STKObjectType.CHAIN, "MyChain")

    def test_ComputeChainSnippet(self):
        try:
            chain = self.get_scenario().children.new(STKObjectType.CHAIN, "chain")
            MyFacility = self.get_scenario().children.new(STKObjectType.FACILITY, "MyFacility")
            MySatellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "MySatellite")
            MySatellite.propagator.propagate()

            self.ComputeChainSnippet(chain)
        finally:
            chain.unload()
            MyFacility.unload()
            MySatellite.unload()

    @code_snippet(
        name="ComputeChain",
        description="Define and compute a chain (basic)",
        category="STK Objects | Chain",
        eid="stkobjects~Chain",
    )
    def ComputeChainSnippet(self, chain):
        # Chain chain: Chain object

        # Add some objects to chain (using STK path)
        chain.objects.add("Facility/MyFacility")
        chain.objects.add("Satellite/MySatellite")

        # Compute the chain
        chain.compute_access()

    def test_CreateChainAdvancedSnippet(self):
        try:
            chain = self.get_scenario().children.new(STKObjectType.CHAIN, "chain")
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()
            MyFacility = self.get_scenario().children.new(STKObjectType.FACILITY, "MyFacility")

            self.CreateChainAdvancedSnippet(self.get_root(), chain, satellite)
        finally:
            chain.unload()
            satellite.unload()
            MyFacility.unload()

    @code_snippet(
        name="CreateChainAdvanced",
        description="Define and compute a chain (advanced)",
        category="STK Objects | Chain",
        eid="stkobjects~Chain",
    )
    def CreateChainAdvancedSnippet(self, root, chain, satellite):
        # Chain chain: Chain object
        # Satellite satellite: Satellite object

        # Remove all previous accesses
        chain.clear_access()

        # Add some objects to chain
        chain.objects.add("Facility/MyFacility")
        chain.objects.add_object(satellite)

        # Configure chain parameters
        chain.recompute_automatically = False
        chain.enable_light_time_delay = False
        chain.time_convergence = 0.001
        chain.data_save_mode = DataSaveMode.SAVE_ACCESSES

        # Specify our own time period
        chain.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)

        # Get chain time period interface
        chainUserTimePeriod = chain.time_period
        chainUserTimePeriod.time_interval.set_explicit_interval(
            root.current_scenario.analysis_interval.find_start_time(),
            root.current_scenario.analysis_interval.find_stop_time(),
        )  # Set to scenario period

        # Compute the chain
        chain.compute_access()

    def test_ChainStrandIntervalsSnippet(self):
        try:
            chain = self.get_scenario().children.new(STKObjectType.CHAIN, "chain")

            self.ChainStrandIntervalsSnippet(chain)
        finally:
            chain.unload()

    @code_snippet(
        name="ChainStrandIntervals",
        description="Prints the strand intervals of chain object",
        category="STK Objects | Chain",
        eid="stkobjects~Chain",
    )
    def ChainStrandIntervalsSnippet(self, chain):
        # Chain chain: Chain Object
        # Compute the chain access if not done already.
        chain.compute_access()

        # Considered Start and Stop time
        print(
            "Chain considered start time: %s"
            % chain.analysis_workbench_components.time_instants.item("ConsideredStartTime").find_occurrence().epoch
        )
        print(
            "Chain considered stop time: %s"
            % chain.analysis_workbench_components.time_instants.item("ConsideredStopTime").find_occurrence().epoch
        )

        objectParticipationIntervals = chain.analysis_workbench_components.time_interval_collections.item(
            "StrandAccessIntervals"
        )
        intervalListResult = objectParticipationIntervals.find_interval_collection()

        for i in range(0, intervalListResult.interval_collections.count):
            if intervalListResult.IsValid:
                print("Link Name: %s" % objectParticipationIntervals.Labels(i + 1))
                print("--------------")
                for j in range(0, intervalListResult.IntervalCollections.Item(i).Count):
                    startTime = intervalListResult.IntervalCollections.Item(i).Item(j).Start
                    stopTime = intervalListResult.IntervalCollections.Item(i).Item(j).Stop
                    print("Start: %s Stop: %s" % (startTime, stopTime))
