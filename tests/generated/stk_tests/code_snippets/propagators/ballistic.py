from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class Ballistic(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object = None
        super(Ballistic, self).__init__(*args, **kwargs)

    m_DefaultName = "MyMissile"

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
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eMissile, Ballistic.m_DefaultName
            ),
            IMissile,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eMissile, Ballistic.m_DefaultName)
        self.m_Object = None

    # endregion

    # region ConfigureBallisticPropagator
    def test_ConfigureBallisticPropagator(self):
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("DistanceUnit", "km")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("TimeUnit", "sec")

        self.m_Object.SetTrajectoryType(AgEVePropagatorType.ePropagatorBallistic)

        propBallistic = clr.CastAs(self.m_Object.Trajectory, IVehiclePropagatorBallistic)
        impactLocation = clr.CastAs(propBallistic.ImpactLocation, IVehicleImpactLocationPoint)
        impact = clr.CastAs(impactLocation.Impact, IVehicleImpactLLA)
        impact.Lat = -20
        impact.Lon = -20
        propBallistic.Step = 59
        propBallistic.Propagate()
        self.ConfigureBallisticPropagator(propBallistic)

    def ConfigureBallisticPropagator(self, propagator):
        propagator.Step = 30
        propagator.SetLaunchType(AgEVeLaunch.eLaunchLLA)

        launch = clr.CastAs(propagator.Launch, IVehicleLaunchLLA)
        launch.Lat = 40.04
        launch.Lon = -76.304
        launch.Alt = 1.5

        propagator.SetImpactLocationType(AgEVeImpactLocation.eImpactLocationPoint)

        impactLocation = clr.CastAs(propagator.ImpactLocation, IVehicleImpactLocationPoint)
        impactLocation.SetImpactType(AgEVeImpact.eImpactLLA)
        impactLocation.SetLaunchControlType(AgEVeLaunchControl.eLaunchControlFixedDeltaV)

        impact = clr.CastAs(impactLocation.Impact, IVehicleImpactLLA)
        impact.Lat = 40.337
        impact.Lon = -75.922
        impact.Alt = 0.0

        fixedDeltaV = clr.CastAs(impactLocation.LaunchControl, IVehicleLaunchControlFixedDeltaV)
        fixedDeltaV.DeltaV = 7.545

        propagator.Propagate()

    # endregion
