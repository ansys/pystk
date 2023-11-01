from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class ChainSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ChainSnippets, self).__init__(*args, **kwargs)

    m_Object: "Chain" = None
    m_DefaultName: str = "MyChain"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("DateFormat", "UTCG")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("Angle", "deg")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("Distance", "m")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        ChainSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.CHAIN, ChainSnippets.m_DefaultName
            ),
            Chain,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.CHAIN, ChainSnippets.m_DefaultName)
        ChainSnippets.m_Object = None

    # endregion

    # region CreateChainOnCurrentScenarioCentralBody
    def test_CreateChainOnCurrentScenarioCentralBody(self):
        (clr.Convert(ChainSnippets.m_Object, IStkObject)).unload()
        self.CreateChainOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)
        ChainSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children[ChainSnippets.m_DefaultName], Chain
        )

    def CreateChainOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Chain on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        chain: "Chain" = clr.CastAs(root.current_scenario.children.new(STK_OBJECT_TYPE.CHAIN, "MyChain"), Chain)

    # endregion

    # region DefineAndComputeChainBasic
    def test_DefineAndComputeChainBasic(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "air1")
        self.DefineAndComputeChainBasic(ChainSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "air1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "fac1")

    def DefineAndComputeChainBasic(self, chain: "Chain"):
        # Add some objects to chain (using STK path)
        chain.objects.add("Facility/fac1")
        chain.objects.add("Satellite/sat1")
        chain.objects.add("Satellite/sat2")
        chain.objects.add("Aircraft/air1")

        # Compute the chain
        chain.compute_access()

    # endregion

    # region DefineAndComputeChainAdvanced
    def test_DefineAndComputeChainAdvanced(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "air1")
        self.DefineAndComputeChainAdvanced(ChainSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "air1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "fac1")

    def DefineAndComputeChainAdvanced(self, chain: "Chain"):
        # Remove all previous accesses
        chain.clear_access()

        # Add some objects to chain
        chain.objects.add("Facility/fac1")
        chain.objects.add("Satellite/sat1")
        chain.objects.add("Satellite/sat2")
        chain.objects.add("Aircraft/air1")

        # Configure chain parameters
        chain.auto_recompute = False
        chain.enable_light_time_delay = False
        chain.time_convergence = 0.001
        chain.data_save_mode = DATA_SAVE_MODE.SAVE_ACCESSES

        # Specify our own time period
        chain.set_time_period_type(CHAIN_TIME_PERIOD_TYPE.USER_SPECIFIED_TIME_PERIOD)

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
        scenario: "IStkObject" = TestBase.Application.current_scenario

        satellite: "Satellite" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "GEO"), Satellite)
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "VehiclePropagatorTwoBody" = clr.Convert(satellite.propagator, VehiclePropagatorTwoBody)
        twoBody.ephemeris_interval.set_start_time_and_duration("1 May 2012 04:00:00.000", "+1 hour")
        twoBody.propagate()

        aircraft: "IStkObject" = scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "DummyAircraft")

        chain: "Chain" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.CHAIN, "ChainForCodeSnippet"), Chain)

        chain.objects.add("Satellite/GEO")
        chain.objects.add("Aircraft/DummyAircraft")

        try:
            self.ConfigureChainComputeTimePeriod(clr.Convert(chain, Chain))

        finally:
            (clr.Convert(satellite, IStkObject)).unload()
            aircraft.unload()
            (clr.Convert(chain, IStkObject)).unload()

    def ConfigureChainComputeTimePeriod(self, chain: "Chain"):
        chain.set_time_period_type(CHAIN_TIME_PERIOD_TYPE.USER_SPECIFIED_TIME_PERIOD)
        userSpecifiedTimePeriod: "ChainUserSpecifiedTimePeriod" = clr.CastAs(
            chain.time_period, ChainUserSpecifiedTimePeriod
        )
        userSpecifiedTimePeriod.time_interval.set_explicit_interval(
            "1 May 2015 04:00:00.000", "1 May 2015 05:00:00.000"
        )

    # endregion

    # region PrintChainStrainIntervalsTimes
    def test_PrintChainStrainIntervalsTimes(self):
        scenario: "IStkObject" = clr.Convert(TestBase.Application.current_scenario, IStkObject)

        satellite: "Satellite" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "GEO"), Satellite)
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "VehiclePropagatorTwoBody" = clr.Convert(satellite.propagator, VehiclePropagatorTwoBody)
        twoBody.ephemeris_interval.set_start_time_and_duration("2 May 2012 04:00:00.000", "+1 hour")
        twoBody.propagate()

        aircraft: "IStkObject" = scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "DummyAircraft")

        chain: "Chain" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.CHAIN, "ChainForCodeSnippet"), Chain)

        chain.objects.add("Satellite/GEO")
        chain.objects.add("Aircraft/DummyAircraft")

        try:
            self.PrintChainStrainIntervalsTimes(clr.Convert(chain, Chain))

        finally:
            (clr.Convert(satellite, IStkObject)).unload()
            aircraft.unload()
            (clr.Convert(chain, IStkObject)).unload()

    def PrintChainStrainIntervalsTimes(self, chain: "Chain"):
        chainAsStkObject: "IStkObject" = clr.CastAs(chain, IStkObject)

        # Compute the chain access if not done already.
        chain.compute_access()

        # Considered Start and Stop time
        Console.WriteLine(
            "Chain considered start time: {0}",
            chainAsStkObject.vgt.events["ConsideredStartTime"].find_occurrence().epoch,
        )
        Console.WriteLine(
            "Chain considered stop time: {0}", chainAsStkObject.vgt.events["ConsideredStopTime"].find_occurrence().epoch
        )

        objectParticipationIntervals: "ITimeToolEventIntervalCollection" = (
            chainAsStkObject.vgt.event_interval_collections["StrandAccessIntervals"]
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
