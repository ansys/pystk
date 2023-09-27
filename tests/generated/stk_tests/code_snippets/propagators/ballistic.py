from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class Ballistic(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object: "IMissile" = None
        super(Ballistic, self).__init__(*args, **kwargs)

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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.MISSILE, Ballistic.m_DefaultName),
            IMissile,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.MISSILE, Ballistic.m_DefaultName)
        self.m_Object = None

    # endregion

    # region ConfigureBallisticPropagator
    def test_ConfigureBallisticPropagator(self):
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("DistanceUnit", "km")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("TimeUnit", "sec")

        self.m_Object.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_BALLISTIC)

        propBallistic: "IVehiclePropagatorBallistic" = clr.CastAs(self.m_Object.trajectory, IVehiclePropagatorBallistic)
        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(
            propBallistic.impact_location, IVehicleImpactLocationPoint
        )
        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
        impact.lat = -20
        impact.lon = -20
        propBallistic.step = 59
        propBallistic.propagate()
        self.ConfigureBallisticPropagator(propBallistic)

    def ConfigureBallisticPropagator(self, propagator: "IVehiclePropagatorBallistic"):
        propagator.step = 30
        propagator.set_launch_type(VEHICLE_LAUNCH.LAUNCH_LLA)

        launch: "IVehicleLaunchLLA" = clr.CastAs(propagator.launch, IVehicleLaunchLLA)
        launch.lat = 40.04
        launch.lon = -76.304
        launch.altitude = 1.5

        propagator.set_impact_location_type(VEHICLE_IMPACT_LOCATION.IMPACT_LOCATION_POINT)

        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(
            propagator.impact_location, IVehicleImpactLocationPoint
        )
        impactLocation.set_impact_type(VEHICLE_IMPACT.IMPACT_LLA)
        impactLocation.set_launch_control_type(VEHICLE_LAUNCH_CONTROL.LAUNCH_CONTROL_FIXED_DELTA_V)

        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
        impact.lat = 40.337
        impact.lon = -75.922
        impact.altitude = 0.0

        fixedDeltaV: "IVehicleLaunchControlFixedDeltaV" = clr.CastAs(
            impactLocation.launch_control, IVehicleLaunchControlFixedDeltaV
        )
        fixedDeltaV.delta_v = 7.545

        propagator.propagate()

    # endregion
