# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from test_util import *
from math2 import *
from unit_preference_extension import *
from parameterized import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    AG_MSL: "Missile" = None
    AG_SENSOR: "Sensor" = None

    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("MissileTests", "MissileTests.sc"))
        EarlyBoundTests.AG_MSL = Missile(TestBase.Application.current_scenario.children["Missile1"])
        EarlyBoundTests.AG_SENSOR = Sensor(
            (IStkObject(EarlyBoundTests.AG_MSL)).children.new(STKObjectType.SENSOR, "Sensor1")
        )

    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SENSOR = None
        EarlyBoundTests.AG_MSL = None
        TestBase.Uninitialize()

    def setUp(self):
        TestBase.Application.units_preferences.set_current_unit("AngleUnit", "deg")
        TestBase.Application.units_preferences.set_current_unit("LatitudeUnit", "deg")
        TestBase.Application.units_preferences.set_current_unit("LongitudeUnit", "deg")

    @parameterized.expand([(90, 81, 2.0), (90, 81, 4.0), (92, 83, 2.1), (93.6, 85.2, 2.23)])
    def test_BUG85667_ImpactLocationIsSetCorrectlyForBallisticPropagators(
        self, azimuthInDeg: float, elevationInDeg: float, deltaVInKmPerSecond: float
    ):
        # Verifies the impact location is set correctly for ballistic propagators

        with UnitPreferenceState(TestBase.Application) as unitState:
            TestBase.Application.units_preferences.set_current_unit("LatitudeUnit", "deg")
            TestBase.Application.units_preferences.set_current_unit("LongitudeUnit", "deg")
            TestBase.Application.units_preferences.set_current_unit("AngleUnit", "deg")
            TestBase.Application.units_preferences.set_current_unit("DistanceUnit", "km")
            TestBase.Application.units_preferences.set_current_unit("TimeUnit", "sec")
            if TestBase.Application.current_scenario.children.contains(STKObjectType.MISSILE, "Test"):
                TestBase.Application.current_scenario.children.unload(STKObjectType.MISSILE, "Test")

            missile: "Missile" = Missile(
                TestBase.Application.current_scenario.children.new(STKObjectType.MISSILE, "Test")
            )
            Assert.assertIsNotNone(missile)

            missile.set_trajectory_type(PropagatorType.BALLISTIC)

            propagator: "PropagatorBallistic" = PropagatorBallistic(missile.trajectory)
            Assert.assertIsNotNone(propagator)

            propagator.set_launch_type(VehicleLaunch.DETIC)
            launch: "LaunchVehicleLocationDetic" = LaunchVehicleLocationDetic(propagator.launch)
            Assert.assertIsNotNone(launch)

            launch.latitude = 37.9249
            launch.longitude = -75.4765
            launch.altitude = 0.0

            propagator.set_impact_location_type(VehicleImpactLocation.LAUNCH_AZ_EL)
            impact: "VehicleImpactLocationLaunchAzEl" = VehicleImpactLocationLaunchAzEl(propagator.impact_location)

            impact.azimuth = azimuthInDeg
            impact.elevation = elevationInDeg
            impact.delta_v = deltaVInKmPerSecond  # km/sec

            Assert.assertEqual(azimuthInDeg, impact.azimuth)
            Assert.assertEqual(elevationInDeg, impact.elevation)
            Assert.assertEqual(deltaVInKmPerSecond, impact.delta_v)

            propagator.propagate()

            impact = VehicleImpactLocationLaunchAzEl(propagator.impact_location)

            Assert.assertAlmostEqual(azimuthInDeg, impact.azimuth, delta=Math2.Epsilon9)
            Assert.assertAlmostEqual(elevationInDeg, impact.elevation, delta=Math2.Epsilon9)
            Assert.assertAlmostEqual(deltaVInKmPerSecond, impact.delta_v, delta=Math2.Epsilon9)

    # region BUG97203
    def test_BUG97203(self):
        missile: "Missile" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.MISSILE, "mymissile"), Missile
        )
        traj: "PropagatorBallistic" = clr.CastAs(missile.trajectory, PropagatorBallistic)
        traj.set_launch_type(VehicleLaunch.DETIC)
        launch: "LaunchVehicleLocationDetic" = clr.CastAs(traj.launch, LaunchVehicleLocationDetic)
        launch.latitude = 77
        launch.longitude = 77
        launch.altitude = 7
        traj.set_impact_location_type(VehicleImpactLocation.LAUNCH_AZ_EL)
        impact: "VehicleImpactLocationLaunchAzEl" = clr.CastAs(traj.impact_location, VehicleImpactLocationLaunchAzEl)
        impact.azimuth = 77
        impact.delta_v = 7
        impact.elevation = 77
        traj.propagate()

        dpGroup: "DataProviderGroup" = clr.CastAs(
            TestBase.Application.current_scenario.children["mymissile"].data_providers["LLA State"], DataProviderGroup
        )
        dp: "IDataProvider" = clr.CastAs(dpGroup.group["Fixed"], IDataProvider)
        dpTimeVar: "DataProviderTimeVarying" = clr.CastAs(dp, DataProviderTimeVarying)
        elems = ["Time", "Lat", "Lon", "Alt"]

        result: "DataProviderResult" = dpTimeVar.execute_elements(
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
