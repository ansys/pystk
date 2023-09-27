from test_util import *
from math2 import *
from unit_preference_extension import *
from parameterized import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    AG_MSL: "IMissile" = None
    AG_SENSOR: "ISensor" = None

    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("MissileTests", "MissileTests.sc"))
        EarlyBoundTests.AG_MSL = clr.Convert(TestBase.Application.current_scenario.children["Missile1"], IMissile)
        EarlyBoundTests.AG_SENSOR = clr.Convert(
            (clr.Convert(EarlyBoundTests.AG_MSL, IStkObject)).children.new(STK_OBJECT_TYPE.SENSOR, "Sensor1"), ISensor
        )

    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SENSOR = None
        EarlyBoundTests.AG_MSL = None
        TestBase.Uninitialize()

    def setUp(self):
        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")
        TestBase.Application.unit_preferences.set_current_unit("LatitudeUnit", "deg")
        TestBase.Application.unit_preferences.set_current_unit("LongitudeUnit", "deg")

    @parameterized.expand([(90, 81, 2.0), (90, 81, 4.0), (92, 83, 2.1), (93.6, 85.2, 2.23)])
    def test_BUG85667_ImpactLocationIsSetCorrectlyForBallisticPropagators(
        self, azimuthInDeg: float, elevationInDeg: float, deltaVInKmPerSecond: float
    ):
        # Verifies the impact location is set correctly for ballistic propagators

        with UnitPreferenceState(TestBase.Application) as unitState:
            TestBase.Application.unit_preferences.set_current_unit("LatitudeUnit", "deg")
            TestBase.Application.unit_preferences.set_current_unit("LongitudeUnit", "deg")
            TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")
            TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", "km")
            TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
            if TestBase.Application.current_scenario.children.contains(STK_OBJECT_TYPE.MISSILE, "Test"):
                TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.MISSILE, "Test")

            missile: "IMissile" = clr.Convert(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.MISSILE, "Test"), IMissile
            )
            Assert.assertIsNotNone(missile)

            missile.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_BALLISTIC)

            propagator: "IVehiclePropagatorBallistic" = clr.Convert(missile.trajectory, IVehiclePropagatorBallistic)
            Assert.assertIsNotNone(propagator)

            propagator.set_launch_type(VEHICLE_LAUNCH.LAUNCH_LLA)
            launch: "IVehicleLaunchLLA" = clr.Convert(propagator.launch, IVehicleLaunchLLA)
            Assert.assertIsNotNone(launch)

            launch.lat = 37.9249
            launch.lon = -75.4765
            launch.altitude = 0.0

            propagator.set_impact_location_type(VEHICLE_IMPACT_LOCATION.IMPACT_LOCATION_LAUNCH_AZ_EL)
            impact: "IVehicleImpactLocationLaunchAzEl" = clr.Convert(
                propagator.impact_location, IVehicleImpactLocationLaunchAzEl
            )

            impact.azimuth = azimuthInDeg
            impact.elevation = elevationInDeg
            impact.delta_v = deltaVInKmPerSecond  # km/sec

            Assert.assertEqual(azimuthInDeg, impact.azimuth)
            Assert.assertEqual(elevationInDeg, impact.elevation)
            Assert.assertEqual(deltaVInKmPerSecond, impact.delta_v)

            propagator.propagate()

            impact = clr.Convert(propagator.impact_location, IVehicleImpactLocationLaunchAzEl)

            Assert.assertAlmostEqual(azimuthInDeg, impact.azimuth, delta=Math2.Epsilon9)
            Assert.assertAlmostEqual(elevationInDeg, impact.elevation, delta=Math2.Epsilon9)
            Assert.assertAlmostEqual(deltaVInKmPerSecond, impact.delta_v, delta=Math2.Epsilon9)

    # region BUG97203
    def test_BUG97203(self):
        missile: "IMissile" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.MISSILE, "mymissile"), IMissile
        )
        traj: "IVehiclePropagatorBallistic" = clr.CastAs(missile.trajectory, IVehiclePropagatorBallistic)
        traj.set_launch_type(VEHICLE_LAUNCH.LAUNCH_LLA)
        launch: "IVehicleLaunchLLA" = clr.CastAs(traj.launch, IVehicleLaunchLLA)
        launch.lat = 77
        launch.lon = 77
        launch.altitude = 7
        traj.set_impact_location_type(VEHICLE_IMPACT_LOCATION.IMPACT_LOCATION_LAUNCH_AZ_EL)
        impact: "IVehicleImpactLocationLaunchAzEl" = clr.CastAs(traj.impact_location, IVehicleImpactLocationLaunchAzEl)
        impact.azimuth = 77
        impact.delta_v = 7
        impact.elevation = 77
        traj.propagate()

        dpGroup: "IDataProviderGroup" = clr.CastAs(
            TestBase.Application.current_scenario.children["mymissile"].data_providers["LLA State"], IDataProviderGroup
        )
        dp: "IDataProvider" = clr.CastAs(dpGroup.group["Fixed"], IDataProvider)
        dpTimeVar: "IDataProviderTimeVarying" = clr.CastAs(dp, IDataProviderTimeVarying)
        elems = ["Time", "Lat", "Lon", "Alt"]

        result: "IDataProviderResult" = dpTimeVar.exec_elements(
            traj.ephemeris_interval.find_start_time(), traj.ephemeris_interval.find_stop_time(), 240, elems
        )
        arTime = result.data_sets[0].get_values()
        arLat = result.data_sets[1].get_values()
        arLon = result.data_sets[2].get_values()
        arAlt = result.data_sets[3].get_values()

        count: int = result.data_sets[0].count

        i: int = 0
        while i < count:
            Console.WriteLine(
                ((((((str(arTime[i]) + "   ") + str(arLat[i])) + "   ") + str(arLon[i])) + "   ") + str(arAlt[i]))
            )

            i += 1

    # endregion
