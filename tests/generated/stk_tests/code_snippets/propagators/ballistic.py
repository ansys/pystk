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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eMissile, Ballistic.m_DefaultName
            ),
            IMissile,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eMissile, Ballistic.m_DefaultName)
        self.m_Object = None

    # endregion

    # region ConfigureBallisticPropagator
    def test_ConfigureBallisticPropagator(self):
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("DistanceUnit", "km")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("TimeUnit", "sec")

        self.m_Object.set_trajectory_type(AgEVePropagatorType.ePropagatorBallistic)

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
        propagator.set_launch_type(AgEVeLaunch.eLaunchLLA)

        launch: "IVehicleLaunchLLA" = clr.CastAs(propagator.launch, IVehicleLaunchLLA)
        launch.lat = 40.04
        launch.lon = -76.304
        launch.alt = 1.5

        propagator.set_impact_location_type(AgEVeImpactLocation.eImpactLocationPoint)

        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(
            propagator.impact_location, IVehicleImpactLocationPoint
        )
        impactLocation.set_impact_type(AgEVeImpact.eImpactLLA)
        impactLocation.set_launch_control_type(AgEVeLaunchControl.eLaunchControlFixedDeltaV)

        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
        impact.lat = 40.337
        impact.lon = -75.922
        impact.alt = 0.0

        fixedDeltaV: "IVehicleLaunchControlFixedDeltaV" = clr.CastAs(
            impactLocation.launch_control, IVehicleLaunchControlFixedDeltaV
        )
        fixedDeltaV.delta_v = 7.545

        propagator.propagate()

    # endregion
