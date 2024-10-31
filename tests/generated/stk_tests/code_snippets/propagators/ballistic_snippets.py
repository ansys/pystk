from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class BallisticSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object: "Missile" = None
        super(BallisticSnippets, self).__init__(*args, **kwargs)

    m_DefaultName: str = "MyMissile"

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
        self.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.MISSILE, BallisticSnippets.m_DefaultName
            ),
            Missile,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.MISSILE, BallisticSnippets.m_DefaultName
        )
        self.m_Object = None

    # endregion

    # region ConfigureBallisticPropagator
    def test_ConfigureBallisticPropagator(self):
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("DistanceUnit", "km")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("TimeUnit", "sec")

        self.m_Object.set_trajectory_type(PROPAGATOR_TYPE.BALLISTIC)

        propBallistic: "PropagatorBallistic" = clr.CastAs(self.m_Object.trajectory, PropagatorBallistic)
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(
            propBallistic.impact_location, VehicleImpactLocationPoint
        )
        impact: "VehicleImpactLocationDetic" = clr.CastAs(impactLocation.impact, VehicleImpactLocationDetic)
        impact.latitude = -20
        impact.longitude = -20
        propBallistic.step = 59
        propBallistic.propagate()
        self.ConfigureBallisticPropagator(propBallistic)

    def ConfigureBallisticPropagator(self, propagator: "PropagatorBallistic"):
        propagator.step = 30
        propagator.set_launch_type(VEHICLE_LAUNCH.DETIC)

        launch: "LaunchVehicleLocationDetic" = clr.CastAs(propagator.launch, LaunchVehicleLocationDetic)
        launch.latitude = 40.04
        launch.longitude = -76.304
        launch.altitude = 1.5

        propagator.set_impact_location_type(VEHICLE_IMPACT_LOCATION.POINT)

        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(
            propagator.impact_location, VehicleImpactLocationPoint
        )
        impactLocation.set_impact_type(VEHICLE_IMPACT.IMPACT_LOCATION_DETIC)
        impactLocation.set_launch_control_type(VEHICLE_LAUNCH_CONTROL.FIXED_DELTA_V)

        impact: "VehicleImpactLocationDetic" = clr.CastAs(impactLocation.impact, VehicleImpactLocationDetic)
        impact.latitude = 40.337
        impact.longitude = -75.922
        impact.altitude = 0.0

        fixedDeltaV: "LaunchVehicleControlFixedDeltaV" = clr.CastAs(
            impactLocation.launch_control, LaunchVehicleControlFixedDeltaV
        )
        fixedDeltaV.delta_v = 7.545

        propagator.propagate()

    # endregion
