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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eMissile, Missile.m_DefaultName),
            IMissile,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eMissile, Missile.m_DefaultName)
        Missile.m_Object = None

    # endregion

    # region DefineMissileTrajectory
    def test_DefineMissileTrajectory(self):
        initialTimeUnit: str = CodeSnippetsTestBase.m_Root.unit_preferences.get_current_unit_abbrv("TimeUnit")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("TimeUnit", "sec")

        self.DefineMissileTrajectory(Missile.m_Object)

        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("TimeUnit", initialTimeUnit)

    def DefineMissileTrajectory(self, missile: "IMissile"):
        # Set missile trajectory type
        missile.set_trajectory_type(AgEVePropagatorType.ePropagatorBallistic)

        # Retrieve the Propagator interface
        trajectory: "IVehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, IVehiclePropagatorBallistic)

        # Set propagator settings if they should be other than defaults
        trajectory.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        trajectory.step = 60.0

        # Set flight parameters
        trajectory.set_launch_type(AgEVeLaunch.eLaunchLLA)
        launch: "IVehicleLaunchLLA" = clr.CastAs(trajectory.launch, IVehicleLaunchLLA)
        launch.lat = 0.0
        launch.lon = 0.0
        launch.alt = 0.0

        # Set impact location type
        trajectory.set_impact_location_type(AgEVeImpactLocation.eImpactLocationPoint)

        # Retrieve the impact point interface
        impactLocation: "IVehicleImpactLocationPoint" = clr.CastAs(
            trajectory.impact_location, IVehicleImpactLocationPoint
        )
        impactLocation.set_launch_control_type(AgEVeLaunchControl.eLaunchControlFixedTimeOfFlight)

        # Retrieve the launch flight interface
        launchControl: "IVehicleLaunchControlFixedTimeOfFlight" = clr.CastAs(
            impactLocation.launch_control, IVehicleLaunchControlFixedTimeOfFlight
        )
        launchControl.time_of_flight = 9000.0

        # Configure missile Impact parameters
        impactLocation.set_impact_type(AgEVeImpact.eImpactLLA)
        impact: "IVehicleImpactLLA" = clr.CastAs(impactLocation.impact, IVehicleImpactLLA)
        impact.lat = -20.0
        impact.lon = -20.0
        impact.alt = 0.0

        # Propagate Missile
        trajectory.propagate()

    # endregion
