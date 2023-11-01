from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class MissileSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(MissileSnippets, self).__init__(*args, **kwargs)

    m_Object: "Missile" = None
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
        MissileSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.MISSILE, MissileSnippets.m_DefaultName
            ),
            Missile,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.MISSILE, MissileSnippets.m_DefaultName
        )
        MissileSnippets.m_Object = None

    # endregion

    # region DefineMissileTrajectory
    def test_DefineMissileTrajectory(self):
        initialTimeUnit: str = CodeSnippetsTestBase.m_Root.unit_preferences.get_current_unit_abbrv("TimeUnit")
        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("TimeUnit", "sec")

        self.DefineMissileTrajectory(MissileSnippets.m_Object)

        CodeSnippetsTestBase.m_Root.unit_preferences.set_current_unit("TimeUnit", initialTimeUnit)

    def DefineMissileTrajectory(self, missile: "Missile"):
        # Set missile trajectory type
        missile.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_BALLISTIC)

        # Retrieve the Propagator interface
        trajectory: "VehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, VehiclePropagatorBallistic)

        # Set propagator settings if they should be other than defaults
        trajectory.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        trajectory.step = 60.0

        # Set flight parameters
        trajectory.set_launch_type(VEHICLE_LAUNCH.LAUNCH_LLA)
        launch: "VehicleLaunchLLA" = clr.CastAs(trajectory.launch, VehicleLaunchLLA)
        launch.lat = 0.0
        launch.lon = 0.0
        launch.altitude = 0.0

        # Set impact location type
        trajectory.set_impact_location_type(VEHICLE_IMPACT_LOCATION.IMPACT_LOCATION_POINT)

        # Retrieve the impact point interface
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(
            trajectory.impact_location, VehicleImpactLocationPoint
        )
        impactLocation.set_launch_control_type(VEHICLE_LAUNCH_CONTROL.LAUNCH_CONTROL_FIXED_TIME_OF_FLIGHT)

        # Retrieve the launch flight interface
        launchControl: "VehicleLaunchControlFixedTimeOfFlight" = clr.CastAs(
            impactLocation.launch_control, VehicleLaunchControlFixedTimeOfFlight
        )
        launchControl.time_of_flight = 9000.0

        # Configure missile Impact parameters
        impactLocation.set_impact_type(VEHICLE_IMPACT.IMPACT_LLA)
        impact: "VehicleImpactLLA" = clr.CastAs(impactLocation.impact, VehicleImpactLLA)
        impact.lat = -20.0
        impact.lon = -20.0
        impact.altitude = 0.0

        # Propagate Missile
        trajectory.propagate()

    # endregion
