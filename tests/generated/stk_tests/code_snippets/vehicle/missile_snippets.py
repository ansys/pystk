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
        initialTimeUnit: str = CodeSnippetsTestBase.m_Root.units_preferences.get_current_unit_abbrv("TimeUnit")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("TimeUnit", "sec")

        self.DefineMissileTrajectory(MissileSnippets.m_Object)

        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("TimeUnit", initialTimeUnit)

    def DefineMissileTrajectory(self, missile: "Missile"):
        # Set missile trajectory type
        missile.set_trajectory_type(PROPAGATOR_TYPE.BALLISTIC)

        # Retrieve the Propagator interface
        trajectory: "PropagatorBallistic" = clr.CastAs(missile.trajectory, PropagatorBallistic)

        # Set propagator settings if they should be other than defaults
        trajectory.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        trajectory.step = 60.0

        # Set flight parameters
        trajectory.set_launch_type(VEHICLE_LAUNCH.DETIC)
        launch: "LaunchVehicleLocationDetic" = clr.CastAs(trajectory.launch, LaunchVehicleLocationDetic)
        launch.latitude = 0.0
        launch.longitude = 0.0
        launch.altitude = 0.0

        # Set impact location type
        trajectory.set_impact_location_type(VEHICLE_IMPACT_LOCATION.POINT)

        # Retrieve the impact point interface
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(
            trajectory.impact_location, VehicleImpactLocationPoint
        )
        impactLocation.set_launch_control_type(VEHICLE_LAUNCH_CONTROL.FIXED_TIME_OF_FLIGHT)

        # Retrieve the launch flight interface
        launchControl: "LaunchVehicleControlFixedTimeOfFlight" = clr.CastAs(
            impactLocation.launch_control, LaunchVehicleControlFixedTimeOfFlight
        )
        launchControl.time_of_flight = 9000.0

        # Configure missile Impact parameters
        impactLocation.set_impact_type(VEHICLE_IMPACT.IMPACT_LOCATION_DETIC)
        impact: "VehicleImpactLocationDetic" = clr.CastAs(impactLocation.impact, VehicleImpactLocationDetic)
        impact.latitude = -20.0
        impact.longitude = -20.0
        impact.altitude = 0.0

        # Propagate Missile
        trajectory.propagate()

    # endregion
