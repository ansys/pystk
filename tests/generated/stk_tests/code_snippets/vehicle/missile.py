from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class Missile(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Missile, self).__init__(*args, **kwargs)

    m_Object: "IMissile" = None
    m_DefaultName: str = "missile1"

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
        Missile.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eMissile, Missile.m_DefaultName),
            IMissile,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eMissile, Missile.m_DefaultName)
        Missile.m_Object = None

    # endregion

    # region DefineMissileTrajectory
    def test_DefineMissileTrajectory(self):
        initialTimeUnit: str = CodeSnippetsTestBase.m_Root.UnitPreferences.GetCurrentUnitAbbrv("TimeUnit")
        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("TimeUnit", "sec")

        self.DefineMissileTrajectory(Missile.m_Object)

        CodeSnippetsTestBase.m_Root.UnitPreferences.SetCurrentUnit("TimeUnit", initialTimeUnit)

    def DefineMissileTrajectory(self, missile: "IMissile"):
        # Set missile trajectory type
        missile.SetTrajectoryType(AgEVePropagatorType.ePropagatorBallistic)

        # Retrieve the Propagator interface
        trajectory: "IVehiclePropagatorBallistic" = clr.CastAs(missile.Trajectory, IVehiclePropagatorBallistic)

        # Set propagator settings if they should be other than defaults
        trajectory.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        trajectory.Step = 60.0

        # Set flight parameters
        trajectory.SetLaunchType(AgEVeLaunch.eLaunchLLA)
        launch: "IVehicleLaunchLLA" = clr.CastAs(trajectory.Launch, IVehicleLaunchLLA)
        launch.Lat = 0.0
        launch.Lon = 0.0
        launch.Alt = 0.0

        # Set impact location type
        trajectory.SetImpactLocationType(AgEVeImpactLocation.eImpactLocationPoint)

        # Retrieve the impact point interface
        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(
            trajectory.ImpactLocation, IVehicleImpactLocationPoint
        )
        impactLocation.SetLaunchControlType(AgEVeLaunchControl.eLaunchControlFixedTimeOfFlight)

        # Retrieve the launch flight interface
        launchControl: "IVehicleLaunchControlFixedTimeOfFlight" = clr.CastAs(
            impactLocation.LaunchControl, IVehicleLaunchControlFixedTimeOfFlight
        )
        launchControl.TimeOfFlight = 9000.0

        # Configure missile Impact parameters
        impactLocation.SetImpactType(AgEVeImpact.eImpactLLA)
        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.Impact, IVehicleImpactLLA)
        impact.Lat = -20.0
        impact.Lon = -20.0
        impact.Alt = 0.0

        # Propagate Missile
        trajectory.Propagate()

    # endregion
