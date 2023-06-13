from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class RealTime(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(RealTime, self).__init__(*args, **kwargs)

    m_Object: "ILaunchVehicle" = None
    m_DefaultName: str = "MyLaunchVehicle"

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

    # region SetUp
    def setUp(self):
        RealTime.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eLaunchVehicle, RealTime.m_DefaultName
            ),
            ILaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eLaunchVehicle, RealTime.m_DefaultName
        )
        RealTime.m_Object = None

    # endregion

    # region ConfigureRealtimePropagator
    def test_ConfigureRealtimePropagator(self):
        scenarioObject = CodeSnippetsTestBase.m_Root.CurrentScenario
        scenario = clr.CastAs(scenarioObject, IScenario)

        scenAnim = None
        anim = None
        holdTimeStepType = AgEScTimeStepType.eScRealTime
        if not TestBase.NoGraphicsMode:
            scenAnim = scenario.Animation
            holdTimeStepType = scenAnim.AnimStepType
            scenAnim.AnimStepType = AgEScTimeStepType.eScRealTime
            anim = clr.CastAs(CodeSnippetsTestBase.m_Root, IAnimation)
            anim.PlayForward()

        RealTime.m_Object.SetTrajectoryType(AgEVePropagatorType.ePropagatorRealtime)
        prop = RealTime.m_Object.Trajectory
        propRealtime = clr.CastAs(prop, IVehiclePropagatorRealtime)

        self.ConfigureRealtimePropagator(CodeSnippetsTestBase.m_Root, propRealtime)
        if not TestBase.NoGraphicsMode:
            anim.Pause()

            # Cleanup
            scenAnim.AnimStepType = holdTimeStepType

    def ConfigureRealtimePropagator(self, root: "IStkObjectRoot", propagator: "IVehiclePropagatorRealtime"):
        # Set Realtime Propagator settings if they should be other than
        # the defaults.
        propagator.InterpolationOrder = 1
        propagator.TimeoutGap = 30.0
        propagator.TimeStep = 60.0
        if propagator.IsLookAheadPropagatorSupported(AgELookAheadPropagator.eLookAheadTwoBody):
            # Set the look ahead type
            propagator.LookAheadPropagator = AgELookAheadPropagator.eLookAheadTwoBody

            # Set the duration time to look ahead and look behind
            duration = propagator.Duration
            duration.LookAhead = 3600.0
            duration.LookBehind = 3600.0

            # Apply the Realtime Propagator settings
            propagator.Propagate()

    # endregion

    # region AddRealtimeLLAPositions
    def test_AddRealtimeLLAPositions(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        gv.SetRouteType(AgEVePropagatorType.ePropagatorRealtime)
        (clr.Convert(gv.Route, IVehiclePropagatorRealtime)).Propagate()
        realtime = clr.CastAs(gv.Route, IVehiclePropagatorRealtime)
        self.AddRealtimeLLAPositions(realtime)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eGroundVehicle, "gv1")

    def AddRealtimeLLAPositions(self, propagator: "IVehiclePropagatorRealtime"):
        points = propagator.PointBuilder.LLA
        points.Add("1 Jan 2012 12:00:00.000", 39.693, -76.399, 0.039, 0.03458, 0.01223, 0.05402)

    # endregion

    # region AddRealtimeLLAPositionsInBatches
    def test_AddRealtimeLLAPositionsInBatches(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        gv.SetRouteType(AgEVePropagatorType.ePropagatorRealtime)
        (clr.Convert(gv.Route, IVehiclePropagatorRealtime)).Propagate()
        realtime = clr.CastAs(gv.Route, IVehiclePropagatorRealtime)
        self.AddRealtimeLLAPositionsInBatches(realtime)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eGroundVehicle, "gv1")

    def AddRealtimeLLAPositionsInBatches(self, propagator: "IVehiclePropagatorRealtime"):
        # Add realtime LLA points in batches
        times = ["1 Jan 2012 12:00:00.000", "1 Jan 2012 12:01:00.000", "1 Jan 2012 12:02:00.000"]
        lat = [39.693, 41.061, 39.925]
        lon = [-76.399, -74.266, -78.578]
        alt = [0.039, 0.042, 0.281]
        latrate = [0.03458, 0.03215, 0.03188]
        lonrate = [0.01223, 0.01148, 0.01075]
        altrate = [0.05402, 0.0521, 0.05075]

        points = propagator.PointBuilder.LLA

        # AddBatch expects each parameter to be a one dimensional array and all of the same length
        points.AddBatch(times, lat, lon, alt, latrate, lonrate, altrate)

    # endregion
