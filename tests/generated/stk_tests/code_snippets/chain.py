import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class Chain(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Chain, self).__init__(*args, **kwargs)

    m_Object = None
    m_DefaultName = "MyChain"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("DateFormat", "UTCG")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("Angle", "deg")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("Distance", "m")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        Chain.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eChain, Chain.m_DefaultName),
            IChain,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eChain, Chain.m_DefaultName)
        Chain.m_Object = None

    # endregion

    # region CreateChainOnCurrentScenarioCentralBody
    def test_CreateChainOnCurrentScenarioCentralBody(self):
        (clr.Convert(Chain.m_Object, IStkObject)).Unload()
        self.CreateChainOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)
        Chain.m_Object = clr.CastAs(CodeSnippetsTestBase.m_Root.CurrentScenario.Children[Chain.m_DefaultName], IChain)

    def CreateChainOnCurrentScenarioCentralBody(self, root):
        # Create the Chain on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        chain = clr.CastAs(root.CurrentScenario.Children.New(AgESTKObjectType.eChain, "MyChain"), IChain)

    # endregion

    # region DefineAndComputeChainBasic
    def test_DefineAndComputeChainBasic(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat2")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eAircraft, "air1")
        self.DefineAndComputeChainBasic(Chain.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eAircraft, "air1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat2")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "fac1")

    def DefineAndComputeChainBasic(self, chain):
        # Add some objects to chain (using STK path)
        chain.Objects.Add("Facility/fac1")
        chain.Objects.Add("Satellite/sat1")
        chain.Objects.Add("Satellite/sat2")
        chain.Objects.Add("Aircraft/air1")

        # Compute the chain
        chain.ComputeAccess()

    # endregion

    # region DefineAndComputeChainAdvanced
    def test_DefineAndComputeChainAdvanced(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "fac1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat2")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eAircraft, "air1")
        self.DefineAndComputeChainAdvanced(Chain.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eAircraft, "air1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat2")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "fac1")

    def DefineAndComputeChainAdvanced(self, chain):
        # Remove all previous accesses
        chain.ClearAccess()

        # Add some objects to chain
        chain.Objects.Add("Facility/fac1")
        chain.Objects.Add("Satellite/sat1")
        chain.Objects.Add("Satellite/sat2")
        chain.Objects.Add("Aircraft/air1")

        # Configure chain parameters
        chain.AutoRecompute = False
        chain.EnableLightTimeDelay = False
        chain.TimeConvergence = 0.001
        chain.DataSaveMode = AgEDataSaveMode.eSaveAccesses

        # Specify our own time period
        chain.SetTimePeriodType(AgEChTimePeriodType.eUserSpecifiedTimePeriod)

        # Get chain time period interface
        chainUserTimePeriod = clr.CastAs(chain.TimePeriod, IChainUserSpecifiedTimePeriod)
        chainUserTimePeriod.TimeInterval.SetExplicitInterval("1 Jul 2005 12:00:00", "2 Jul 2005 12:00:00")

        # Compute the chain
        chain.ComputeAccess()

    # endregion

    # region ConfigureChainComputeTimePeriod
    def test_ConfigureChainComputeTimePeriod(self):
        scenario = TestBase.Application.CurrentScenario

        satellite = clr.Convert(scenario.Children.New(AgESTKObjectType.eSatellite, "GEO"), ISatellite)
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        twoBody = clr.Convert(satellite.Propagator, IVehiclePropagatorTwoBody)
        twoBody.EphemerisInterval.SetStartTimeAndDuration("1 May 2012 04:00:00.000", "+1 hour")
        twoBody.Propagate()

        aircraft = scenario.Children.New(AgESTKObjectType.eAircraft, "DummyAircraft")

        chain = clr.Convert(scenario.Children.New(AgESTKObjectType.eChain, "ChainForCodeSnippet"), IChain)

        chain.Objects.Add("Satellite/GEO")
        chain.Objects.Add("Aircraft/DummyAircraft")

        try:
            self.ConfigureChainComputeTimePeriod(clr.Convert(chain, IChain))

        finally:
            (clr.Convert(satellite, IStkObject)).Unload()
            aircraft.Unload()
            (clr.Convert(chain, IStkObject)).Unload()

    def ConfigureChainComputeTimePeriod(self, chain):
        chain.SetTimePeriodType(AgEChTimePeriodType.eUserSpecifiedTimePeriod)
        userSpecifiedTimePeriod = clr.CastAs(chain.TimePeriod, IChainUserSpecifiedTimePeriod)
        userSpecifiedTimePeriod.TimeInterval.SetExplicitInterval("1 May 2015 04:00:00.000", "1 May 2015 05:00:00.000")

    # endregion

    # region PrintChainStrainIntervalsTimes
    def test_PrintChainStrainIntervalsTimes(self):
        scenario = clr.Convert(TestBase.Application.CurrentScenario, IStkObject)

        satellite = clr.Convert(scenario.Children.New(AgESTKObjectType.eSatellite, "GEO"), ISatellite)
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        twoBody = clr.Convert(satellite.Propagator, IVehiclePropagatorTwoBody)
        twoBody.EphemerisInterval.SetStartTimeAndDuration("2 May 2012 04:00:00.000", "+1 hour")
        twoBody.Propagate()

        aircraft = scenario.Children.New(AgESTKObjectType.eAircraft, "DummyAircraft")

        chain = clr.Convert(scenario.Children.New(AgESTKObjectType.eChain, "ChainForCodeSnippet"), IChain)

        chain.Objects.Add("Satellite/GEO")
        chain.Objects.Add("Aircraft/DummyAircraft")

        try:
            self.PrintChainStrainIntervalsTimes(clr.Convert(chain, IChain))

        finally:
            (clr.Convert(satellite, IStkObject)).Unload()
            aircraft.Unload()
            (clr.Convert(chain, IStkObject)).Unload()

    def PrintChainStrainIntervalsTimes(self, chain):
        chainAsStkObject = clr.CastAs(chain, IStkObject)

        # Compute the chain access if not done already.
        chain.ComputeAccess()

        # Considered Start and Stop time
        Console.WriteLine(
            "Chain considered start time: {0}",
            chainAsStkObject.Vgt.Events["ConsideredStartTime"].FindOccurrence().Epoch,
        )
        Console.WriteLine(
            "Chain considered stop time: {0}", chainAsStkObject.Vgt.Events["ConsideredStopTime"].FindOccurrence().Epoch
        )

        objectParticipationIntervals = chainAsStkObject.Vgt.EventIntervalCollections["StrandAccessIntervals"]
        intervalListResult = objectParticipationIntervals.FindIntervalCollection()

        i = 0
        while i < intervalListResult.IntervalCollections.Count:
            if intervalListResult.IsValid:
                Console.WriteLine("Link Name: {0}", objectParticipationIntervals.Labels[i])
                Console.WriteLine("--------------")

                j = 0
                while j < intervalListResult.IntervalCollections[i].Count:
                    startTime = intervalListResult.IntervalCollections[i][j].Start
                    stopTime = intervalListResult.IntervalCollections[i][j].Stop
                    Console.WriteLine("Start: {0}, Stop: {1}", startTime, stopTime)

                    j += 1

            i += 1

    # endregion
