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
from ansys.stk.core.analysis_workbench import *


class ChainSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ChainSnippets, self).__init__(*args, **kwargs)

    m_Object: "Chain" = None
    m_DefaultName: str = "MyChain"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("DateFormat", "UTCG")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("Angle", "deg")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("Distance", "m")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        ChainSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.CHAIN, ChainSnippets.m_DefaultName),
            Chain,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.CHAIN, ChainSnippets.m_DefaultName)
        ChainSnippets.m_Object = None

    # endregion

    # region CreateChainOnCurrentScenarioCentralBody
    def test_CreateChainOnCurrentScenarioCentralBody(self):
        (ISTKObject(ChainSnippets.m_Object)).unload()
        self.CreateChainOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)
        ChainSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children[ChainSnippets.m_DefaultName], Chain
        )

    def CreateChainOnCurrentScenarioCentralBody(self, root: "STKObjectRoot"):
        # Create the Chain on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        chain: "Chain" = clr.CastAs(root.current_scenario.children.new(STKObjectType.CHAIN, "MyChain"), Chain)

    # endregion

    # region DefineAndComputeChainBasic
    def test_DefineAndComputeChainBasic(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.AIRCRAFT, "air1")
        self.DefineAndComputeChainBasic(CodeSnippetsTestBase.m_Root.current_scenario, ChainSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.AIRCRAFT, "air1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "fac1")

    def DefineAndComputeChainBasic(self, scenarioObj: "ISTKObject", chain: "Chain"):
        chain.start_object = scenarioObj.children.get_item_by_name("fac1")
        chain.end_object = scenarioObj.children.get_item_by_name("air1")

        connections: "ChainConnectionCollection" = chain.connections
        connections.add(
            scenarioObj.children.get_item_by_name("sat2"), scenarioObj.children.get_item_by_name("air1"), 1, 1
        )
        connections.add(
            scenarioObj.children.get_item_by_name("fac1"), scenarioObj.children.get_item_by_name("sat1"), 1, 1
        )
        connections.add(
            scenarioObj.children.get_item_by_name("sat1"), scenarioObj.children.get_item_by_name("sat2"), 1, 1
        )

        # Compute the chain
        chain.compute_access()

    # endregion

    # region DefineAndComputeChainAdvanced
    def test_DefineAndComputeChainAdvanced(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.FACILITY, "fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.AIRCRAFT, "air1")
        self.DefineAndComputeChainAdvanced(CodeSnippetsTestBase.m_Root.current_scenario, ChainSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.AIRCRAFT, "air1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.FACILITY, "fac1")

    def DefineAndComputeChainAdvanced(self, scenarioObj: "ISTKObject", chain: "Chain"):
        # Remove all previous accesses
        chain.clear_access()

        # Add some objects to chain
        chain.start_object = scenarioObj.children.get_item_by_name("fac1")
        chain.end_object = scenarioObj.children.get_item_by_name("air1")

        connections: "ChainConnectionCollection" = chain.connections
        connections.add(
            scenarioObj.children.get_item_by_name("sat2"), scenarioObj.children.get_item_by_name("air1"), 1, 1
        )
        connections.add(
            scenarioObj.children.get_item_by_name("fac1"), scenarioObj.children.get_item_by_name("sat1"), 1, 1
        )
        connections.add(
            scenarioObj.children.get_item_by_name("sat1"), scenarioObj.children.get_item_by_name("sat2"), 1, 1
        )

        # Configure chain parameters
        chain.recompute_automatically = False
        chain.enable_light_time_delay = False
        chain.time_convergence = 0.001
        chain.data_save_mode = DataSaveMode.SAVE_ACCESSES

        # Specify our own time period
        chain.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)

        # Get chain time period interface
        chainUserTimePeriod: "ChainUserSpecifiedTimePeriod" = clr.CastAs(
            chain.time_period, ChainUserSpecifiedTimePeriod
        )
        chainUserTimePeriod.time_interval.set_explicit_interval("1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00")

        # Compute the chain
        chain.compute_access()

    # endregion

    # region ConfigureChainComputeTimePeriod
    def test_ConfigureChainComputeTimePeriod(self):
        scenario: "ISTKObject" = TestBase.Application.current_scenario

        satellite: "Satellite" = Satellite(scenario.children.new(STKObjectType.SATELLITE, "GEO"))
        satellite.set_propagator_type(PropagatorType.TWO_BODY)
        twoBody: "PropagatorTwoBody" = PropagatorTwoBody(satellite.propagator)
        twoBody.ephemeris_interval.set_start_time_and_duration("1 May 2012 04:00:00.000", "+1 hour")
        twoBody.propagate()

        aircraft: "ISTKObject" = scenario.children.new(STKObjectType.AIRCRAFT, "DummyAircraft")

        chain: "Chain" = Chain(scenario.children.new(STKObjectType.CHAIN, "ChainForCodeSnippet"))
        chain.start_object = scenario.children.get_item_by_name("GEO")
        chain.end_object = scenario.children.get_item_by_name("DummyAircraft")

        connections: "ChainConnectionCollection" = chain.connections
        connections.add(
            scenario.children.get_item_by_name("GEO"), scenario.children.get_item_by_name("DummyAircraft"), 1, 1
        )

        try:
            self.ConfigureChainComputeTimePeriod(chain)

        finally:
            (ISTKObject(satellite)).unload()
            aircraft.unload()
            (ISTKObject(chain)).unload()

    def ConfigureChainComputeTimePeriod(self, chain: "Chain"):
        chain.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)
        userSpecifiedTimePeriod: "ChainUserSpecifiedTimePeriod" = clr.CastAs(
            chain.time_period, ChainUserSpecifiedTimePeriod
        )
        userSpecifiedTimePeriod.time_interval.set_explicit_interval(
            "1 May 2015 04:00:00.000", "1 May 2015 05:00:00.000"
        )

    # endregion

    # region PrintChainStrainIntervalsTimes
    def test_PrintChainStrainIntervalsTimes(self):
        scenario: "ISTKObject" = TestBase.Application.current_scenario

        satellite: "Satellite" = Satellite(scenario.children.new(STKObjectType.SATELLITE, "GEO"))
        satellite.set_propagator_type(PropagatorType.TWO_BODY)
        twoBody: "PropagatorTwoBody" = PropagatorTwoBody(satellite.propagator)
        twoBody.ephemeris_interval.set_start_time_and_duration("2 May 2012 04:00:00.000", "+1 hour")
        twoBody.propagate()

        aircraft: "ISTKObject" = scenario.children.new(STKObjectType.AIRCRAFT, "DummyAircraft")

        chain: "Chain" = Chain(scenario.children.new(STKObjectType.CHAIN, "ChainForCodeSnippet"))
        chain.start_object = scenario.children.get_item_by_name("GEO")
        chain.end_object = scenario.children.get_item_by_name("DummyAircraft")

        connections: "ChainConnectionCollection" = chain.connections
        connections.add(
            scenario.children.get_item_by_name("GEO"), scenario.children.get_item_by_name("DummyAircraft"), 1, 1
        )

        try:
            self.PrintChainStrainIntervalsTimes(chain)

        finally:
            (ISTKObject(satellite)).unload()
            aircraft.unload()
            (ISTKObject(chain)).unload()

    def PrintChainStrainIntervalsTimes(self, chain: "Chain"):
        chainAsStkObject: "ISTKObject" = clr.CastAs(chain, ISTKObject)

        # Compute the chain access if not done already.
        chain.compute_access()

        # Considered Start and Stop time
        Console.WriteLine(
            "Chain considered start time: {0}",
            chainAsStkObject.analysis_workbench_components.time_instants["ConsideredStartTime"].find_occurrence().epoch,
        )
        Console.WriteLine(
            "Chain considered stop time: {0}",
            chainAsStkObject.analysis_workbench_components.time_instants["ConsideredStopTime"].find_occurrence().epoch,
        )

        objectParticipationIntervals: "ITimeToolTimeIntervalCollection" = (
            chainAsStkObject.analysis_workbench_components.time_interval_collections["StrandAccessIntervals"]
        )
        intervalListResult: "TimeToolIntervalsVectorResult" = objectParticipationIntervals.find_interval_collection()

        i: int = 0
        while i < intervalListResult.interval_collections.count:
            if intervalListResult.is_valid:
                Console.WriteLine("Link Name: {0}", objectParticipationIntervals.labels[i])
                Console.WriteLine("--------------")

                j: int = 0
                while j < intervalListResult.interval_collections[i].count:
                    startTime: typing.Any = intervalListResult.interval_collections[i][j].start
                    stopTime: typing.Any = intervalListResult.interval_collections[i][j].stop
                    Console.WriteLine("Start: {0}, Stop: {1}", startTime, stopTime)

                    j += 1

            i += 1

    # endregion
