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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eLaunchVehicle, RealTime.m_DefaultName
            ),
            ILaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eLaunchVehicle, RealTime.m_DefaultName
        )
        RealTime.m_Object = None

    # endregion

    # region ConfigureRealtimePropagator
    def test_ConfigureRealtimePropagator(self):
        scenarioObject: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario
        scenario: "IScenario" = clr.CastAs(scenarioObject, IScenario)

        scenAnim: "IScenarioAnimation" = None
        anim: "IAnimation" = None
        holdTimeStepType: "AgEScTimeStepType" = AgEScTimeStepType.eScRealTime
        if not TestBase.NoGraphicsMode:
            scenAnim = scenario.animation
            holdTimeStepType = scenAnim.anim_step_type
            scenAnim.anim_step_type = AgEScTimeStepType.eScRealTime
            anim = clr.CastAs(CodeSnippetsTestBase.m_Root, IAnimation)
            anim.play_forward()

        RealTime.m_Object.set_trajectory_type(AgEVePropagatorType.ePropagatorRealtime)
        prop: "IVehiclePropagator" = RealTime.m_Object.trajectory
        propRealtime: "IVehiclePropagatorRealtime" = clr.CastAs(prop, IVehiclePropagatorRealtime)

        self.ConfigureRealtimePropagator(CodeSnippetsTestBase.m_Root, propRealtime)
        if not TestBase.NoGraphicsMode:
            anim.pause()

            # Cleanup
            scenAnim.anim_step_type = holdTimeStepType

    def ConfigureRealtimePropagator(self, root: "IStkObjectRoot", propagator: "IVehiclePropagatorRealtime"):
        # Set Realtime Propagator settings if they should be other than
        # the defaults.
        propagator.interpolation_order = 1
        propagator.timeout_gap = 30.0
        propagator.time_step = 60.0
        if propagator.is_look_ahead_propagator_supported(AgELookAheadPropagator.eLookAheadTwoBody):
            # Set the look ahead type
            propagator.look_ahead_propagator = AgELookAheadPropagator.eLookAheadTwoBody

            # Set the duration time to look ahead and look behind
            duration: "IVehicleDuration" = propagator.duration
            duration.look_ahead = 3600.0
            duration.look_behind = 3600.0

            # Apply the Realtime Propagator settings
            propagator.propagate()

    # endregion

    # region AddRealtimeLLAPositions
    def test_AddRealtimeLLAPositions(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        gv.set_route_type(AgEVePropagatorType.ePropagatorRealtime)
        (clr.Convert(gv.route, IVehiclePropagatorRealtime)).propagate()
        realtime: "IVehiclePropagatorRealtime" = clr.CastAs(gv.route, IVehiclePropagatorRealtime)
        self.AddRealtimeLLAPositions(realtime)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eGroundVehicle, "gv1")

    def AddRealtimeLLAPositions(self, propagator: "IVehiclePropagatorRealtime"):
        points: "IVehicleRealtimeLLAPoints" = propagator.point_builder.lla
        points.add("1 Jan 2012 12:00:00.000", 39.693, -76.399, 0.039, 0.03458, 0.01223, 0.05402)

    # endregion

    # region AddRealtimeLLAPositionsInBatches
    def test_AddRealtimeLLAPositionsInBatches(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        gv.set_route_type(AgEVePropagatorType.ePropagatorRealtime)
        (clr.Convert(gv.route, IVehiclePropagatorRealtime)).propagate()
        realtime: "IVehiclePropagatorRealtime" = clr.CastAs(gv.route, IVehiclePropagatorRealtime)
        self.AddRealtimeLLAPositionsInBatches(realtime)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eGroundVehicle, "gv1")

    def AddRealtimeLLAPositionsInBatches(self, propagator: "IVehiclePropagatorRealtime"):
        # Add realtime LLA points in batches
        times = ["1 Jan 2012 12:00:00.000", "1 Jan 2012 12:01:00.000", "1 Jan 2012 12:02:00.000"]
        lat = [39.693, 41.061, 39.925]
        lon = [-76.399, -74.266, -78.578]
        alt = [0.039, 0.042, 0.281]
        latrate = [0.03458, 0.03215, 0.03188]
        lonrate = [0.01223, 0.01148, 0.01075]
        altrate = [0.05402, 0.0521, 0.05075]

        points: "IVehicleRealtimeLLAPoints" = propagator.point_builder.lla

        # AddBatch expects each parameter to be a one dimensional array and all of the same length
        points.add_batch(times, lat, lon, alt, latrate, lonrate, altrate)

    # endregion
