from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class Chain(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Chain, self).__init__(*args, **kwargs)

    m_Object: "IChain" = None
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
        Chain.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.CHAIN, Chain.m_DefaultName),
            IChain,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.CHAIN, Chain.m_DefaultName)
        Chain.m_Object = None

    # endregion

    # region CreateChainOnCurrentScenarioCentralBody
    def test_CreateChainOnCurrentScenarioCentralBody(self):
        (clr.Convert(Chain.m_Object, IStkObject)).unload()
        self.CreateChainOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)
        Chain.m_Object = clr.CastAs(CodeSnippetsTestBase.m_Root.current_scenario.children[Chain.m_DefaultName], IChain)

    def CreateChainOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Chain on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        chain: "IChain" = clr.CastAs(root.current_scenario.children.new(STK_OBJECT_TYPE.CHAIN, "MyChain"), IChain)

    # endregion

    # region DefineAndComputeChainBasic
    def test_DefineAndComputeChainBasic(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "fac1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "air1")
        self.DefineAndComputeChainBasic(Chain.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "air1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "fac1")

    def DefineAndComputeChainBasic(self, chain: "IChain"):
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
        self.DefineAndComputeChainAdvanced(Chain.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.AIRCRAFT, "air1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat2")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "fac1")

    def DefineAndComputeChainAdvanced(self, chain: "IChain"):
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
        chainUserTimePeriod: "IChainUserSpecifiedTimePeriod" = clr.CastAs(
            chain.time_period, IChainUserSpecifiedTimePeriod
        )
        chainUserTimePeriod.time_interval.set_explicit_interval("1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00")

        # Compute the chain
        chain.compute_access()

    # endregion

    # region ConfigureChainComputeTimePeriod
    def test_ConfigureChainComputeTimePeriod(self):
        scenario: "IStkObject" = TestBase.Application.current_scenario

        satellite: "ISatellite" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "GEO"), ISatellite)
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "IVehiclePropagatorTwoBody" = clr.Convert(satellite.propagator, IVehiclePropagatorTwoBody)
        twoBody.ephemeris_interval.set_start_time_and_duration("1 May 2012 04:00:00.000", "+1 hour")
        twoBody.propagate()

        aircraft: "IStkObject" = scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "DummyAircraft")

        chain: "IChain" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.CHAIN, "ChainForCodeSnippet"), IChain)

        chain.objects.add("Satellite/GEO")
        chain.objects.add("Aircraft/DummyAircraft")

        try:
            self.ConfigureChainComputeTimePeriod(clr.Convert(chain, IChain))

        finally:
            (clr.Convert(satellite, IStkObject)).unload()
            aircraft.unload()
            (clr.Convert(chain, IStkObject)).unload()

    def ConfigureChainComputeTimePeriod(self, chain: "IChain"):
        chain.set_time_period_type(CHAIN_TIME_PERIOD_TYPE.USER_SPECIFIED_TIME_PERIOD)
        userSpecifiedTimePeriod: "IChainUserSpecifiedTimePeriod" = clr.CastAs(
            chain.time_period, IChainUserSpecifiedTimePeriod
        )
        userSpecifiedTimePeriod.time_interval.set_explicit_interval(
            "1 May 2015 04:00:00.000", "1 May 2015 05:00:00.000"
        )

    # endregion

    # region PrintChainStrainIntervalsTimes
    def test_PrintChainStrainIntervalsTimes(self):
        scenario: "IStkObject" = clr.Convert(TestBase.Application.current_scenario, IStkObject)

        satellite: "ISatellite" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "GEO"), ISatellite)
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "IVehiclePropagatorTwoBody" = clr.Convert(satellite.propagator, IVehiclePropagatorTwoBody)
        twoBody.ephemeris_interval.set_start_time_and_duration("2 May 2012 04:00:00.000", "+1 hour")
        twoBody.propagate()

        aircraft: "IStkObject" = scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "DummyAircraft")

        chain: "IChain" = clr.Convert(scenario.children.new(STK_OBJECT_TYPE.CHAIN, "ChainForCodeSnippet"), IChain)

        chain.objects.add("Satellite/GEO")
        chain.objects.add("Aircraft/DummyAircraft")

        try:
            self.PrintChainStrainIntervalsTimes(clr.Convert(chain, IChain))

        finally:
            (clr.Convert(satellite, IStkObject)).unload()
            aircraft.unload()
            (clr.Convert(chain, IStkObject)).unload()

    def PrintChainStrainIntervalsTimes(self, chain: "IChain"):
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
        intervalListResult: "ITimeToolIntervalsVectorResult" = objectParticipationIntervals.find_interval_collection()

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
