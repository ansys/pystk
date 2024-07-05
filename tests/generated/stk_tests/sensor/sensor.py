import pytest
from test_util import *
from access_constraints.access_constraint_helper import *
from app_provider import *
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from math2 import *
from orientation_helper import *
from vehicle.vehicle_basic import *
from vehicle.vehicle_vo import *
from ansys.stk.core.utilities.colors import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


@category("EarlyBoundTests")
@category("Causes crashes")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("SensorTests", "SensorTests.sc"))
            ac1: "Aircraft" = clr.CastAs(TestBase.Application.current_scenario.children["Boing737"], Aircraft)
            ac1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            ga: "VehiclePropagatorGreatArc" = clr.CastAs(ac1.route, VehiclePropagatorGreatArc)

            TestBase.PropagateGreatArc(ga)

            gv1: "GroundVehicle" = clr.CastAs(
                TestBase.Application.current_scenario.children["GroundVehicle1"], GroundVehicle
            )
            gv1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            ga = clr.CastAs(gv1.route, VehiclePropagatorGreatArc)
            TestBase.PropagateGreatArc(ga)

            sh1: "Ship" = clr.CastAs(TestBase.Application.current_scenario.children["Ship1"], Ship)
            sh1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
            ga = clr.CastAs(sh1.route, VehiclePropagatorGreatArc)
            TestBase.PropagateGreatArc(ga)

            ms1: "Missile" = clr.CastAs(TestBase.Application.current_scenario.children["Missile1"], Missile)
            ms1.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_BALLISTIC)
            ballistic: "VehiclePropagatorBallistic" = clr.CastAs(ms1.trajectory, VehiclePropagatorBallistic)
            ballistic.step = 59
            ballistic.propagate()

            lt: "LineTarget" = clr.CastAs(TestBase.Application.current_scenario.children["LineTarget2"], LineTarget)
            lt.points.add(0, 0)
            lt.points.add(2, 2)

        except Exception as e:
            Assert.fail("Test initialization error: {0}", str(e))

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        TestBase.Uninitialize()

    # endregion

    # region FacilitySensor
    def test_FacilitySensor(self):
        oHelper = SensorHelper(TestBase.Application)
        oHelper.Run("Facility1", "Sensor1", TestBase.TemporaryDirectory)

    # endregion

    # region TargetSensor
    def test_TargetSensor(self):
        oHelper = SensorHelper(TestBase.Application)
        oHelper.Run("Target1", "Sensor1", TestBase.TemporaryDirectory)

    # endregion

    # region AircraftSensor
    def test_AircraftSensor(self):
        oHelper = SensorHelper(TestBase.Application)
        oHelper.Run("Boing737", "Sensor1", TestBase.TemporaryDirectory)

    # endregion

    # region GroundVehicleSensor
    def test_GroundVehicleSensor(self):
        oHelper = SensorHelper(TestBase.Application)
        oHelper.Run("GroundVehicle1", "Sensor1", TestBase.TemporaryDirectory)

    # endregion

    # region LaunchVehicleSensor
    def test_LaunchVehicleSensor(self):
        oHelper = SensorHelper(TestBase.Application)
        oLV: "LaunchVehicle" = LaunchVehicle(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "MIR")
        )
        Assert.assertIsNotNone(oLV)
        oLV.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SIMPLE_ASCENT)
        ascent: "VehiclePropagatorSimpleAscent" = clr.CastAs(oLV.trajectory, VehiclePropagatorSimpleAscent)
        ascent.ephemeris_interval.set_explicit_interval(
            ascent.ephemeris_interval.find_start_time(), "1 Jul 1999 00:10:00.000"
        )
        ascent.step = 60
        ascent.propagate()
        oHelper.Run("MIR", "Sensor1", TestBase.TemporaryDirectory)
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "MIR")

    # endregion

    # region MissileSensor
    def test_MissileSensor(self):
        oHelper = SensorHelper(TestBase.Application)
        oHelper.Run("Missile1", "Sensor1", TestBase.TemporaryDirectory)

    # endregion

    # region SatelliteSensor
    def test_SatelliteSensor(self):
        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("SensorTests", "SensorTests.sc"))
        ac1: "Aircraft" = clr.CastAs(TestBase.Application.current_scenario.children["Boing737"], Aircraft)
        ac1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        ga: "VehiclePropagatorGreatArc" = clr.CastAs(ac1.route, VehiclePropagatorGreatArc)
        TestBase.PropagateGreatArc(ga)

        gv1: "GroundVehicle" = clr.CastAs(
            TestBase.Application.current_scenario.children["GroundVehicle1"], GroundVehicle
        )
        gv1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        ga = clr.CastAs(gv1.route, VehiclePropagatorGreatArc)
        TestBase.PropagateGreatArc(ga)

        sh1: "Ship" = clr.CastAs(TestBase.Application.current_scenario.children["Ship1"], Ship)
        sh1.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
        ga = clr.CastAs(sh1.route, VehiclePropagatorGreatArc)
        TestBase.PropagateGreatArc(ga)

        ms1: "Missile" = clr.CastAs(TestBase.Application.current_scenario.children["Missile1"], Missile)
        ms1.set_trajectory_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_BALLISTIC)
        ballistic: "VehiclePropagatorBallistic" = clr.CastAs(ms1.trajectory, VehiclePropagatorBallistic)
        ballistic.step = 59
        ballistic.propagate()

        lt: "LineTarget" = clr.CastAs(TestBase.Application.current_scenario.children["LineTarget2"], LineTarget)
        lt.points.add(0, 0)
        lt.points.add(2, 2)

        oHelper = SensorHelper(TestBase.Application)
        oHelper.Run("Satellite1", "Sensor1", TestBase.TemporaryDirectory)

    # endregion

    # region ShipSensor
    def test_ShipSensor(self):
        oHelper = SensorHelper(TestBase.Application)
        oHelper.Run("Ship1", "Sensor1", TestBase.TemporaryDirectory)

    # endregion

    def test_SpatialInfoTest(self):
        helper = SpatialInfoHelper(TestBase.Application)
        o: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        if not o.children.contains(STK_OBJECT_TYPE.SENSOR, "Sensor1"):
            o.children.new(STK_OBJECT_TYPE.SENSOR, "Sensor1")
        helper.Run(TestBase.Application.current_scenario.children["Satellite1"].children["Sensor1"])


@category("BugFixes")
class BugFixes(TestBase):
    def __init__(self, *args, **kwargs):
        super(BugFixes, self).__init__(*args, **kwargs)

    _sensor: "Sensor" = None
    _sat: "Satellite" = None

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("SensorTests", "SensorTests.sc"))

        except Exception as e:
            Assert.fail("Test initialization error: {0}", str(e))

    # endregion

    # region TestSetUp
    def setUp(self):
        BugFixes._sat = clr.CastAs(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        BugFixes._sensor = Sensor((IStkObject(BugFixes._sat)).children.new(STK_OBJECT_TYPE.SENSOR, "Bug66700Sensor"))

    # endregion

    # region TestTearDown
    def tearDown(self):
        TestBase.Application.current_scenario.children["Satellite1"].children.unload(
            STK_OBJECT_TYPE.SENSOR, "Bug66700Sensor"
        )
        BugFixes._sensor = None

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        TestBase.Uninitialize()

    # endregion

    # region BUG66309
    @category("Graphics Tests")
    def test_BUG66309(self):
        #
        # Test conditions where ComputationalMethod can be set to Analytical or Numerical
        #

        objFac: "IStkObject" = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "SwathFac")
        facSensor: "Sensor" = clr.CastAs(objFac.children.new(STK_OBJECT_TYPE.SENSOR, "SwathFacSensor"), Sensor)

        objSat: "IStkObject" = TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "SwathSat")
        sat: "Satellite" = clr.CastAs(objSat, Satellite)
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twobody: "VehiclePropagatorTwoBody" = VehiclePropagatorTwoBody(sat.propagator)
        twobody.propagate()

        satSensor: "Sensor" = clr.CastAs(objSat.children.new(STK_OBJECT_TYPE.SENSOR, "SwathSatSensor"), Sensor)
        satSensor.swath.enable = True

        classicalX: "OrbitStateClassical" = OrbitStateClassical(
            twobody.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL)
        )
        classicalX.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_PERIOD
        periodX: "ClassicalSizeShapePeriod" = ClassicalSizeShapePeriod(classicalX.size_shape)
        periodX.eccentricity = 0
        twobody.initial_state.representation.assign(classicalX)

        standard: "VehicleOrbitAttitudeStandard" = VehicleOrbitAttitudeStandard(sat.attitude)
        standard.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_NADIR_ALIGNMENT_WITH_ECF_VELOCITY_CONSTRAINT)
        twobody.propagate()

        # Neither can be set for non-Vehicle
        with pytest.raises(Exception):
            facSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.UNKNOWN
        with pytest.raises(Exception):
            facSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.ANALYTICAL
        with pytest.raises(Exception):
            facSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.NUMERICAL

        # Analytical can be set for sat sensor, circular orbit, default attitude, and sensor: nadir pointing
        satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.ANALYTICAL
        Assert.assertEqual(SWATH_COMPUTATIONAL_METHOD.ANALYTICAL, satSensor.swath.computational_method)
        satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.NUMERICAL
        Assert.assertEqual(SWATH_COMPUTATIONAL_METHOD.NUMERICAL, satSensor.swath.computational_method)

        # Analytical should fail for non-circular
        classical: "OrbitStateClassical" = OrbitStateClassical(
            twobody.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL)
        )
        classical.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_PERIOD
        period: "ClassicalSizeShapePeriod" = ClassicalSizeShapePeriod(classical.size_shape)
        period.eccentricity = 0.01
        twobody.initial_state.representation.assign(classical)
        twobody.propagate()
        with pytest.raises(Exception):
            satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.ANALYTICAL
        period.eccentricity = 0.0
        twobody.initial_state.representation.assign(classical)
        twobody.propagate()

        # Analytical should fail for different attitude
        orbit: "VehicleOrbitAttitudeStandard" = VehicleOrbitAttitudeStandard(sat.attitude)
        orbit.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_NADIR_ALIGNMENT_WITH_ECI_VELOCITY_CONSTRAINT)
        twobody.propagate()
        with pytest.raises(Exception):
            satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.ANALYTICAL
        orbit.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_NADIR_ALIGNMENT_WITH_ECF_VELOCITY_CONSTRAINT)
        twobody.propagate()

        # Analytical should fail for non-Nadir pointing sensor
        satSensor.set_pointing_type(SENSOR_POINTING.POINT_3D_MODEL)
        with pytest.raises(Exception):
            satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.ANALYTICAL
        satSensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)

        # Should work again
        satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.ANALYTICAL
        Assert.assertEqual(SWATH_COMPUTATIONAL_METHOD.ANALYTICAL, satSensor.swath.computational_method)

        # Numerical can be set for non-custom sensor, but not for custom sensor
        satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.NUMERICAL
        Assert.assertEqual(SWATH_COMPUTATIONAL_METHOD.NUMERICAL, satSensor.swath.computational_method)

        satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.ANALYTICAL
        Assert.assertEqual(SWATH_COMPUTATIONAL_METHOD.ANALYTICAL, satSensor.swath.computational_method)

        satSensor.common_tasks.set_pattern_custom(TestBase.GetScenarioFile("AreaTgtWeird", "RedSensor.Pattern"))
        with pytest.raises(Exception):
            satSensor.swath.computational_method = SWATH_COMPUTATIONAL_METHOD.NUMERICAL

        objFac.unload()
        objSat.unload()

    # endregion

    # region BUG66700

    def test_BUG66700_1(self):
        def code1():
            # - verify that the sensor location (point) cannot be set to sensor's center point
            BugFixes._sensor.set_location_type(SENSOR_LOCATION.VECTOR_GEOMETRY_TOOL_POINT)
            vgtPoint: "LocationVectorGeometryToolPoint" = clr.CastAs(
                BugFixes._sensor.location_data, LocationVectorGeometryToolPoint
            )
            # vgtPoint.PointPath = "Satellite/Satellite1 Center";
            # vgtPoint.PointPath = "Place/Place1 Center";
            # vgtPoint.PointPath = "Place/Place1/Sensor/Sensor3 Center";
            vgtPoint.point_path = "Satellite/Satellite1/Sensor/Bug66700Sensor Center"

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    def test_BUG66700_2a(self):
        def code2():
            # - verify that the sensor's pointing (fixed at axes) does not allow setting the reference axes to the body axes of the current sensor [ or to an axes dependent upon the sensor's body axes;]
            BugFixes._sensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED_AXES)
            fixedAxes: "SensorPointingFixedAxes" = clr.CastAs(BugFixes._sensor.pointing, SensorPointingFixedAxes)
            # fixedAxes.ReferenceAxes = "Place/Place1/Sensor/Sensor3 Body Axes";
            fixedAxes.reference_axes = "Satellite/Satellite1/Sensor/Bug66700Sensor Body Axes"

        ex = ExceptionAssert.Throws(code2)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    def test_BUG66700_2b(self):
        def code3():
            # - ... or to an axes dependent upon the sensor's body axes;
            objSensor: "IStkObject" = clr.CastAs(BugFixes._sensor, IStkObject)
            depOnSensorsBodyAxes: "IVectorGeometryToolAxes" = objSensor.vgt.axes.factory.create(
                "DepOnSensorsBodyAxes", "", VECTOR_GEOMETRY_TOOL_AXES_TYPE.FIXED
            )
            depOnSensorsBodyAxesFixed: "VectorGeometryToolAxesFixed" = clr.CastAs(
                depOnSensorsBodyAxes, VectorGeometryToolAxesFixed
            )
            depOnSensorsBodyAxesFixed.reference_axes.set_path("Satellite/Satellite1/Sensor/Bug66700Sensor Body")

            BugFixes._sensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED_AXES)
            fixedAxes: "SensorPointingFixedAxes" = clr.CastAs(BugFixes._sensor.pointing, SensorPointingFixedAxes)
            fixedAxes.reference_axes = "Satellite/Satellite1/Sensor/Bug66700Sensor DepOnSensorsBodyAxes Axes"

        ex = ExceptionAssert.Throws(code3)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    def test_BUG66700_3a(self):
        def code4():
            # - verify that the satellite's precessing spin attitude profile does not allow setting the reference axes
            # to the body axes of the current satellite [or to an axes dependent upon the satellite's body axes;]
            BugFixes._sat.set_attitude_type(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
            attitude: "VehicleOrbitAttitudeStandard" = clr.CastAs(BugFixes._sat.attitude, VehicleOrbitAttitudeStandard)
            attitude.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_PRECESSING_SPIN)
            profilePrecessingSpin: "VehicleProfilePrecessingSpin" = clr.CastAs(
                attitude.basic.profile, VehicleProfilePrecessingSpin
            )
            # profilePrecessingSpin.ReferenceAxes = "Place/Place1/Sensor/Sensor3 Body Axes";
            profilePrecessingSpin.reference_axes = "Satellite/Satellite1 Body Axes"

        ex = ExceptionAssert.Throws(code4)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    def test_BUG66700_3b(self):
        def code5():
            # ... or to an axes dependent upon the satellite's body axes
            objSat: "IStkObject" = clr.CastAs(BugFixes._sat, IStkObject)
            depOnSatsBodyAxes: "IVectorGeometryToolAxes" = objSat.vgt.axes.factory.create(
                "DepOnSatsBodyAxes3b", "", VECTOR_GEOMETRY_TOOL_AXES_TYPE.FIXED
            )
            depOnSatsBodyAxesFixed: "VectorGeometryToolAxesFixed" = clr.CastAs(
                depOnSatsBodyAxes, VectorGeometryToolAxesFixed
            )
            depOnSatsBodyAxesFixed.reference_axes.set_path("Satellite/Satellite1 Body")

            BugFixes._sat.set_attitude_type(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
            attitude: "VehicleOrbitAttitudeStandard" = clr.CastAs(BugFixes._sat.attitude, VehicleOrbitAttitudeStandard)
            attitude.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_PRECESSING_SPIN)
            profilePrecessingSpin: "VehicleProfilePrecessingSpin" = clr.CastAs(
                attitude.basic.profile, VehicleProfilePrecessingSpin
            )
            # profilePrecessingSpin.ReferenceAxes = "Place/Place1/Sensor/Sensor3 Body Axes";
            profilePrecessingSpin.reference_axes = "Satellite/Satellite1 DepOnSatsBodyAxes3b Axes"

        ex = ExceptionAssert.Throws(code5)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    def test_BUG66700_4a(self):
        def code6():
            # - verify that the satellite's fixed in axes attitude profile does not allow setting the reference axes
            # to the body axes of the current satellite [or to an axes dependent upon the satellite's body axes;]
            BugFixes._sat.set_attitude_type(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
            attitude: "VehicleOrbitAttitudeStandard" = clr.CastAs(BugFixes._sat.attitude, VehicleOrbitAttitudeStandard)
            attitude.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_FIXED_IN_AXES)
            profileFixedInAxes: "VehicleProfileFixedInAxes" = clr.CastAs(
                attitude.basic.profile, VehicleProfileFixedInAxes
            )
            # profileFixedInAxes.ReferenceAxes = "Place/Place1/Sensor/Sensor3 Body Axes";
            profileFixedInAxes.reference_axes = "Satellite/Satellite1 Body Axes"

        ex = ExceptionAssert.Throws(code6)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    def test_BUG66700_4b(self):
        def code7():
            # ... or to an axes dependent upon the satellite's body axes
            objSat: "IStkObject" = clr.CastAs(BugFixes._sat, IStkObject)
            depOnSatsBodyAxes: "IVectorGeometryToolAxes" = objSat.vgt.axes.factory.create(
                "DepOnSatsBodyAxes4b", "", VECTOR_GEOMETRY_TOOL_AXES_TYPE.FIXED
            )
            depOnSatsBodyAxesFixed: "VectorGeometryToolAxesFixed" = clr.CastAs(
                depOnSatsBodyAxes, VectorGeometryToolAxesFixed
            )
            depOnSatsBodyAxesFixed.reference_axes.set_path("Satellite/Satellite1 Body")

            BugFixes._sat.set_attitude_type(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
            attitude: "VehicleOrbitAttitudeStandard" = clr.CastAs(BugFixes._sat.attitude, VehicleOrbitAttitudeStandard)
            attitude.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_FIXED_IN_AXES)
            profileFixedInAxes: "VehicleProfileFixedInAxes" = clr.CastAs(
                attitude.basic.profile, VehicleProfileFixedInAxes
            )
            # profileFixedInAxes.ReferenceAxes = "Place/Place1/Sensor/Sensor3 Body Axes";
            profileFixedInAxes.reference_axes = "Satellite/Satellite1 DepOnSatsBodyAxes4b Axes"

        ex = ExceptionAssert.Throws(code7)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    def test_BUG66700_5a(self):
        def code8():
            # - verify that the satellite's aligned and constrained attitude profile does not allow setting
            # the reference vectors to a vector that is dependent upon the satellite's body axes.
            # (AlignedVector)
            objSat: "IStkObject" = clr.CastAs(BugFixes._sat, IStkObject)
            depOnSatsBodyAxes: "IVectorGeometryToolVector" = objSat.vgt.vectors.factory.create(
                "DepOnSatsBodyAxes5a", "", VECTOR_GEOMETRY_TOOL_VECTOR_TYPE.FIXED_IN_AXES
            )
            depOnSatsBodyVectorFixed: "VectorGeometryToolVectorFixedInAxes" = clr.CastAs(
                depOnSatsBodyAxes, VectorGeometryToolVectorFixedInAxes
            )
            depOnSatsBodyVectorFixed.reference_axes.set_path("Satellite/Satellite1 Body")

            BugFixes._sat.set_attitude_type(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
            attitude: "VehicleOrbitAttitudeStandard" = clr.CastAs(BugFixes._sat.attitude, VehicleOrbitAttitudeStandard)
            attitude.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_ALIGNED_AND_CONSTRAINED)
            profileAandC: "VehicleProfileAlignedAndConstrained" = clr.CastAs(
                attitude.basic.profile, VehicleProfileAlignedAndConstrained
            )
            # profileAandC.AlignedVector.ReferenceVector = "Aircraft/Boing737 East Vector";
            profileAandC.aligned_vector.reference_vector = "Satellite/Satellite1 DepOnSatsBodyAxes5a Vector"

        ex = ExceptionAssert.Throws(code8)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    def test_BUG66700_5b(self):
        def code9():
            # - verify that the satellite's aligned and constrained attitude profile does not allow setting
            # the reference vectors to a vector that is dependent upon the satellite's body axes.
            # (ConstrainedVector)
            objSat: "IStkObject" = clr.CastAs(BugFixes._sat, IStkObject)
            depOnSatsBodyAxes: "IVectorGeometryToolVector" = objSat.vgt.vectors.factory.create(
                "DepOnSatsBodyAxes5b", "", VECTOR_GEOMETRY_TOOL_VECTOR_TYPE.FIXED_IN_AXES
            )
            depOnSatsBodyVectorFixed: "VectorGeometryToolVectorFixedInAxes" = clr.CastAs(
                depOnSatsBodyAxes, VectorGeometryToolVectorFixedInAxes
            )
            depOnSatsBodyVectorFixed.reference_axes.set_path("Satellite/Satellite1 Body")

            BugFixes._sat.set_attitude_type(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
            attitude: "VehicleOrbitAttitudeStandard" = clr.CastAs(BugFixes._sat.attitude, VehicleOrbitAttitudeStandard)
            attitude.basic.set_profile_type(VEHICLE_PROFILE.PROFILE_ALIGNED_AND_CONSTRAINED)
            profileAandC: "VehicleProfileAlignedAndConstrained" = clr.CastAs(
                attitude.basic.profile, VehicleProfileAlignedAndConstrained
            )
            # profileAandC.ConstrainedVector.ReferenceVector = "Aircraft/Boing737 East Vector";
            profileAandC.constrained_vector.reference_vector = "Satellite/Satellite1 DepOnSatsBodyAxes5b Vector"

        ex = ExceptionAssert.Throws(code9)
        StringAssert.Contains("not a valid choice", str(ex), "Exception message mismatch")

    # endregion

    # region BUG73834
    def test_BUG73834(self):
        shuttleSat: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "Shuttle1"
        )
        sensor: "Sensor" = Sensor(shuttleSat.children.new(STK_OBJECT_TYPE.SENSOR, "Horizon1"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)

        # Supported Pattern Types

        TestBase.Application.execute_command("Define */Satellite/Shuttle1/Sensor/Horizon1 Conical 30.0 40.0 20.0 20.1")
        Assert.assertEqual(SENSOR_PATTERN.COMPLEX_CONIC, sensor.pattern_type)
        pattern: "ISensorPattern" = sensor.pattern
        Assert.assertIsNotNone(pattern)

        TestBase.Application.execute_command("Define */Satellite/Shuttle1/Sensor/Horizon1 HalfPower 12.5  3.4")
        Assert.assertEqual(SENSOR_PATTERN.HALF_POWER, sensor.pattern_type)
        pattern = sensor.pattern
        Assert.assertIsNotNone(pattern)

        cmd: str = (
            'Define */Satellite/Shuttle1/Sensor/Horizon1 Custom "'
            + TestBase.GetScenarioFile("AreaTgtWeird", "RedSensor.Pattern")
        ) + '"'
        Console.WriteLine(cmd)
        TestBase.Application.execute_command(cmd)
        Assert.assertEqual(SENSOR_PATTERN.CUSTOM, sensor.pattern_type)
        pattern = sensor.pattern
        Assert.assertIsNotNone(pattern)

        TestBase.Application.execute_command("Define */Satellite/Shuttle1/Sensor/Horizon1 Rectangular 30.0 40.0")
        Assert.assertEqual(SENSOR_PATTERN.RECTANGULAR, sensor.pattern_type)
        pattern = sensor.pattern
        Assert.assertIsNotNone(pattern)

        TestBase.Application.execute_command("Define */Satellite/Shuttle1/Sensor/Horizon1 Rectangular 30.0 40.0")
        Assert.assertEqual(SENSOR_PATTERN.RECTANGULAR, sensor.pattern_type)
        pattern = sensor.pattern
        Assert.assertIsNotNone(pattern)

        TestBase.Application.execute_command(
            "Define */Satellite/Shuttle1/Sensor/Horizon1 SAR 10.0 60.0 40.0 30.0 700.0"
        )
        Assert.assertEqual(SENSOR_PATTERN.SAR, sensor.pattern_type)
        pattern = sensor.pattern
        Assert.assertIsNotNone(pattern)

        TestBase.Application.execute_command("Define */Satellite/Shuttle1/Sensor/Horizon1 SimpleCone 80.0")
        Assert.assertEqual(SENSOR_PATTERN.SIMPLE_CONIC, sensor.pattern_type)
        pattern = sensor.pattern
        Assert.assertIsNotNone(pattern)

        # Unsupported Pattern Types

        cmd = String.Format(
            'Define */Satellite/Shuttle1/Sensor/Horizon1 TmConical Add "{0}" "{1}" 45.0 30.0 90 90',
            scenario.start_time,
            scenario.stop_time,
        )
        Console.WriteLine(cmd)
        TestBase.Application.execute_command(cmd)
        Assert.assertEqual(SENSOR_PATTERN.UNKNOWN_PATTERN, sensor.pattern_type)
        pattern = sensor.pattern
        Assert.assertIsNotNone(pattern)

        cmd = String.Format(
            'Define */Satellite/Shuttle1/Sensor/Horizon1 TmVarying Add "{0}" "{1}" 45.0 30.0 90 90',
            scenario.start_time,
            scenario.stop_time,
        )
        Console.WriteLine(cmd)
        TestBase.Application.execute_command(cmd)
        Assert.assertEqual(SENSOR_PATTERN.UNKNOWN_PATTERN, sensor.pattern_type)
        pattern = sensor.pattern
        Assert.assertIsNotNone(pattern)

        # "SimpleEllipse" is not implemented.  See BUG01976
        # Application.ExecuteCommand("Define */Satellite/Shuttle1/Sensor/Horizon1 SimpleEllipse 45.0 30.0 20.0");
        # Assert.AreEqual(AgESnPattern.UNKNOWN_PATTERN, sensor.PatternType);
        # pattern = sensor.Pattern;
        # Assert.IsNotNull(pattern);

        (IStkObject(sensor)).unload()
        shuttleSat.unload()

    # endregion

    # region BUG73914

    def test_BUG73914(self):
        shuttleSat: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, "Shuttle"
        )
        sensor: "Sensor" = Sensor(shuttleSat.children.new(STK_OBJECT_TYPE.SENSOR, "Horizon"))
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")

        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        cmd: str = String.Format(
            'Point */Satellite/Shuttle/Sensor/Horizon Schedule AddLLA "{0}" -33.17 -70.08 0.36', scenario.start_time
        )
        Console.WriteLine(cmd)
        TestBase.Application.execute_command(cmd)

        Assert.assertEqual(SENSOR_POINTING.POINT_SCHEDULE, sensor.pointing_type)

        pointingMethod: "SensorPointingSchedule" = clr.CastAs(sensor.pointing, SensorPointingSchedule)
        Assert.assertIsNotNone(pointingMethod)
        Assert.assertTrue(pointingMethod.enabled)

        TestBase.Application.execute_command("Point */Satellite/Shuttle/Sensor/Horizon Schedule Off")
        Assert.assertFalse(pointingMethod.enabled)

        (IStkObject(sensor)).unload()
        shuttleSat.unload()


class SensorHelper(object):
    def __init__(self, oRoot: "StkObjectRoot"):
        self.m_logger = Logger.Instance
        self.m_oRoot: "StkObjectRoot" = oRoot
        self.m_oSensor: "Sensor" = None
        self.m_strDataDir: str = None

        try:
            self.m_strDataDir: str = TestBase.GetSTKHomeDir()

        except Exception as e:
            self.m_logger.WriteLine(str(e))
            self.m_logger.WriteLine(e.StackTrace)

    # endregion

    # region Run method
    def Run(self, strParentName: str, strSensorName: str, temporaryDirectory: str):
        if self.m_oRoot == None:
            Assert.fail("The Root object is invalid!")
        self.m_oSensor = None
        Assert.assertIsNotNone(self.m_oRoot.current_scenario)
        # get parent object
        oParent: "IStkObject" = self.m_oRoot.current_scenario.children[strParentName]
        Assert.assertIsNotNone(oParent)
        # get (create) sensor
        try:
            self.m_oSensor = Sensor(oParent.children[strSensorName])

        except Exception as e:
            self.m_logger.WriteLine(str(e))
            self.m_oSensor = Sensor(oParent.children.new(STK_OBJECT_TYPE.SENSOR, strSensorName))
            self.m_logger.WriteLine5("Object {0} was created.", strSensorName)

        Assert.assertIsNotNone(self.m_oSensor)

        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.AccessConstraints(temporaryDirectory)
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.STKObject()
        self.BasicCoarseDefinition()
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.BasicDefinition()
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.BasicLocation()
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.BasicPointing(oParent.class_type)
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.BasicRefraction()
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.BasicResolution()
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.BasicSensorAzElMask()
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        self.StarsInFOV()
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
        if not TestBase.NoGraphicsMode:
            self.Graphics()
            Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
            self.DisplayTimes()
            Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
            self.VO()
            Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
            self.VODataDisplay()
            Console.WriteLine(DateTime.Now.TimeOfDay.ToString())
            self.VOVectors()
            Console.WriteLine(DateTime.Now.TimeOfDay.ToString())

            # region Swath
            # Swath test
            self.m_logger.WriteLine6("The Parent object is: {0}", oParent.class_type)
            if (
                ((oParent.class_type == STK_OBJECT_TYPE.AIRCRAFT))
                or ((oParent.class_type == STK_OBJECT_TYPE.GROUND_VEHICLE))
            ) or ((oParent.class_type == STK_OBJECT_TYPE.SHIP)):
                self.Swath(True)
            elif oParent.class_type == STK_OBJECT_TYPE.LAUNCH_VEHICLE:
                oLV: "LaunchVehicle" = LaunchVehicle(oParent)

                # ProfileType
                simpleAsc: "VehiclePropagatorSimpleAscent" = VehiclePropagatorSimpleAscent(oLV.trajectory)
                simpleAsc.propagate()
                # Swath
                self.Swath(True)
            elif oParent.class_type == STK_OBJECT_TYPE.MISSILE:
                oMissile: "Missile" = Missile(oParent)
                Assert.assertIsNotNone(oMissile)
                oBallistic: "VehiclePropagatorBallistic" = VehiclePropagatorBallistic(oMissile.trajectory)
                self.m_oRoot.unit_preferences.set_current_unit("TimeUnit", "day")
                oBallistic.step = 0.001  # 86.4 seconds
                self.m_oRoot.unit_preferences.reset_units()
                self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)
                ptFixed: "SensorPointingFixed" = clr.CastAs(self.m_oSensor.pointing, SensorPointingFixed)
                ptFixed.orientation.assign_az_el(160, 0, AZ_EL_ABOUT_BORESIGHT.ROTATE)
                oBallistic.propagate()
                # Swath
                self.Swath(True)
            elif oParent.class_type == STK_OBJECT_TYPE.SATELLITE:
                oSatellite: "Satellite" = Satellite(oParent)
                Assert.assertIsNotNone(oSatellite)
                # Swath
                self.Swath(True)
            else:
                self.Swath(False)
            # endregion
            Console.WriteLine(DateTime.Now.TimeOfDay.ToString())

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                self.Graphics()

        self.SpatialInfo()
        Console.WriteLine(DateTime.Now.TimeOfDay.ToString())

    # endregion

    # region AccessConstraints
    def AccessConstraints(self, temporaryDirectory: str):
        oHelper = AccessConstraintHelper(self.m_oRoot.unit_preferences)
        oHelper.DoTest(self.m_oSensor.access_constraints, IStkObject(self.m_oSensor), temporaryDirectory)

    # endregion

    # region BasicDefinition
    def BasicDefinition(self):
        self.m_logger.WriteLine("----- THE BASIC DEFINITION TEST ----- BEGIN -----")

        # set Unit prefs
        self.m_oRoot.unit_preferences.set_current_unit("AngleUnit", "deg")
        Assert.assertEqual("deg", self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit"))

        self.m_oRoot.unit_preferences.set_current_unit("SmallDistanceUnit", "mm")
        Assert.assertEqual("mm", self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"))

        self.m_oRoot.unit_preferences.set_current_unit("FrequencyUnit", "GHz")
        Assert.assertEqual("GHz", self.m_oRoot.unit_preferences.get_current_unit_abbrv("FrequencyUnit"))

        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", "km")
        Assert.assertEqual("km", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))

        # SetPatternType(SIMPLE_CONIC)
        self.m_oSensor.set_pattern_type(SENSOR_PATTERN.SIMPLE_CONIC)
        Assert.assertEqual(SENSOR_PATTERN.SIMPLE_CONIC, self.m_oSensor.pattern_type)
        oSimpleConic: "SensorSimpleConicPattern" = SensorSimpleConicPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oSimpleConic)

        oSimpleConic.cone_angle = 23.123456789
        Assert.assertEqual(oSimpleConic.cone_angle, 23.123456789)
        with pytest.raises(Exception):
            oSimpleConic.cone_angle = 5678.1234

        oSimpleConic.angular_resolution = 0.1
        Assert.assertAlmostEqual(float(oSimpleConic.angular_resolution), 0.1, delta=1e-06)
        oSimpleConic.angular_resolution = 10.0
        Assert.assertAlmostEqual(float(oSimpleConic.angular_resolution), 10.0, delta=1e-06)
        with pytest.raises(Exception):
            oSimpleConic.angular_resolution = 0.001
        with pytest.raises(Exception):
            oSimpleConic.angular_resolution = 10.1

        # SetPatternType(COMPLEX_CONIC)
        self.m_oSensor.set_pattern_type(SENSOR_PATTERN.COMPLEX_CONIC)
        Assert.assertEqual(SENSOR_PATTERN.COMPLEX_CONIC, self.m_oSensor.pattern_type)
        oComplexConic: "SensorComplexConicPattern" = SensorComplexConicPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oComplexConic)

        oComplexConic.inner_cone_half_angle = 12.34
        Assert.assertEqual(12.34, oComplexConic.inner_cone_half_angle)
        with pytest.raises(Exception):
            oComplexConic.inner_cone_half_angle = 567.123

        oComplexConic.outer_cone_half_angle = 12.34
        Assert.assertEqual(12.34, oComplexConic.outer_cone_half_angle)
        with pytest.raises(Exception):
            oComplexConic.outer_cone_half_angle = 567.123

        oComplexConic.minimum_clock_angle = 123.456
        Assert.assertAlmostEqual(123.456, float(oComplexConic.minimum_clock_angle), delta=0.0001)
        with pytest.raises(Exception):
            oComplexConic.minimum_clock_angle = -567.123

        oComplexConic.maximum_clock_angle = 234.567
        Assert.assertAlmostEqual(234.567, float(oComplexConic.maximum_clock_angle), delta=0.0001)
        with pytest.raises(Exception):
            oComplexConic.maximum_clock_angle = 567.123
        with pytest.raises(Exception):
            oComplexConic.minimum_clock_angle = 567.123
        with pytest.raises(Exception):
            oComplexConic.maximum_clock_angle = -567.123
        with pytest.raises(Exception):
            oComplexConic.maximum_clock_angle = 100

        oComplexConic.set_clock_angles(140, 160)
        Assert.assertEqual(140, oComplexConic.minimum_clock_angle)
        Assert.assertEqual(160, oComplexConic.maximum_clock_angle)
        try:
            oComplexConic.set_clock_angles(150, 140)
            Assert.fail("Should not allow to set illegal value!")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

        oComplexConic.angular_resolution = 0.1
        Assert.assertAlmostEqual(float(oComplexConic.angular_resolution), 0.1, delta=1e-06)
        oComplexConic.angular_resolution = 10.0
        Assert.assertAlmostEqual(float(oComplexConic.angular_resolution), 10.0, delta=1e-06)
        try:
            oComplexConic.angular_resolution = 0.001
            Assert.fail()

        except AssertionError:
            raise

        except Exception as ex:
            self.m_logger.WriteLine7("EXPECTED EXCEPTION: {0}", str(ex), "Exception message mismatch")

        try:
            oComplexConic.angular_resolution = 10.1
            Assert.fail()

        except AssertionError:
            raise

        except Exception as ex:
            self.m_logger.WriteLine7("EXPECTED EXCEPTION: {0}", str(ex), "Exception message mismatch")

        oComplexConic.set_cone_half_angles(110, 120)
        Assert.assertAlmostEqual(110, float(oComplexConic.inner_cone_half_angle), delta=1e-06)
        Assert.assertAlmostEqual(120, float(oComplexConic.outer_cone_half_angle), delta=1e-06)
        try:
            oComplexConic.set_cone_half_angles(150, 140)
            Assert.fail("Should not allow to set illegal value!")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

        # SetPatternType(CUSTOM)
        self.m_oSensor.set_pattern_type(SENSOR_PATTERN.CUSTOM)
        Assert.assertEqual(SENSOR_PATTERN.CUSTOM, self.m_oSensor.pattern_type)
        oCustom: "SensorCustomPattern" = SensorCustomPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oCustom)

        oCustom.filename = TestBase.GetScenarioFile("AreaTgtWeird", "RedSensor.Pattern")
        Assert.assertEqual(TestBase.PathCombine("AreaTgtWeird", "RedSensor.Pattern"), oCustom.filename)
        with pytest.raises(Exception):
            oCustom.filename = TestBase.GetScenarioFile("AreaTgtWeird", "UnrealFile.Pattern")
        with pytest.raises(Exception):
            oCustom.filename = ""

        oCustom.angular_resolution = 0.1
        Assert.assertAlmostEqual(float(oCustom.angular_resolution), 0.1, delta=1e-06)
        oCustom.angular_resolution = 10.0
        Assert.assertAlmostEqual(float(oCustom.angular_resolution), 10.0, delta=1e-06)
        with pytest.raises(Exception):
            oCustom.angular_resolution = 0.001
        with pytest.raises(Exception):
            oCustom.angular_resolution = 10.1

        Assert.assertIsNotNone(oCustom)
        oCustom.use_native_resolution = True
        Assert.assertEqual(True, oCustom.use_native_resolution)
        Assert.assertIsNotNone(oCustom)
        oCustom.use_native_resolution = False
        Assert.assertEqual(False, oCustom.use_native_resolution)

        # SetPatternType(HALF_POWER)
        self.m_oSensor.set_pattern_type(SENSOR_PATTERN.HALF_POWER)
        self.m_logger.WriteLine6("\tThe new PatternType is: {0}", self.m_oSensor.pattern_type)
        Assert.assertEqual(SENSOR_PATTERN.HALF_POWER, self.m_oSensor.pattern_type)
        oHalfPower: "SensorHalfPowerPattern" = SensorHalfPowerPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oHalfPower)

        self.m_logger.WriteLine6("\t\tThe current HalfAngle is: {0}", oHalfPower.half_angle)

        oHalfPower.frequency = 12345.6789
        Assert.assertEqual(12345.6789, oHalfPower.frequency)
        with pytest.raises(Exception):
            oHalfPower.frequency = -123.456

        oHalfPower.antenna_diameter = 12345.6789
        Assert.assertEqual(12345.6789, oHalfPower.antenna_diameter)
        with pytest.raises(Exception):
            oHalfPower.antenna_diameter = -123.456

        oHalfPower.angular_resolution = 0.1
        Assert.assertAlmostEqual(float(oHalfPower.angular_resolution), 0.1, delta=1e-06)
        oHalfPower.angular_resolution = 10.0
        Assert.assertAlmostEqual(float(oHalfPower.angular_resolution), 10.0, delta=1e-06)
        with pytest.raises(Exception):
            oHalfPower.angular_resolution = 0.001
        with pytest.raises(Exception):
            oHalfPower.angular_resolution = 10.1

        # SetPatternType(RECTANGULAR)
        self.m_oSensor.set_pattern_type(SENSOR_PATTERN.RECTANGULAR)
        Assert.assertEqual(SENSOR_PATTERN.RECTANGULAR, self.m_oSensor.pattern_type)

        oRectangular: "SensorRectangularPattern" = SensorRectangularPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oRectangular)

        oRectangular.vertical_half_angle = 12.34
        Assert.assertEqual(12.34, oRectangular.vertical_half_angle)
        with pytest.raises(Exception):
            oRectangular.vertical_half_angle = 123.456

        oRectangular.horizontal_half_angle = 43.21
        Assert.assertEqual(43.21, oRectangular.horizontal_half_angle)
        with pytest.raises(Exception):
            oRectangular.horizontal_half_angle = 123.456

        oRectangular.angular_resolution = 0.1
        Assert.assertAlmostEqual(float(oRectangular.angular_resolution), 0.1, delta=1e-06)
        oRectangular.angular_resolution = 10.0
        Assert.assertAlmostEqual(float(oRectangular.angular_resolution), 10.0, delta=1e-06)
        with pytest.raises(Exception):
            oRectangular.angular_resolution = 0.001
        with pytest.raises(Exception):
            oRectangular.angular_resolution = 10.1

        # SetPatternType(SAR)
        self.m_oSensor.set_pattern_type(SENSOR_PATTERN.SAR)
        Assert.assertEqual(SENSOR_PATTERN.SAR, self.m_oSensor.pattern_type)
        oSAR: "SensorSARPattern" = SensorSARPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oSAR)

        oSAR.min_elevation_angle = 12.3456789
        Assert.assertEqual(12.3456789, oSAR.min_elevation_angle)
        with pytest.raises(Exception):
            oSAR.min_elevation_angle = 123.456
        with pytest.raises(Exception):
            oSAR.min_elevation_angle = -1.23456

        oSAR.max_elevation_angle = 89.7654321
        Assert.assertEqual(89.7654321, oSAR.max_elevation_angle)
        with pytest.raises(Exception):
            oSAR.max_elevation_angle = 123.456
        with pytest.raises(Exception):
            oSAR.max_elevation_angle = 1.23456
        with pytest.raises(Exception):
            oSAR.min_elevation_angle = 90

        oSAR.set_elevation_angles(14, 15)
        Assert.assertAlmostEqual(14, float(oSAR.min_elevation_angle), delta=1e-08)
        Assert.assertAlmostEqual(15, float(oSAR.max_elevation_angle), delta=1e-08)
        with pytest.raises(Exception):
            oSAR.set_elevation_angles(15, 14)

        oSAR.fore_exclusion_angle = 56.789
        Assert.assertEqual(56.789, oSAR.fore_exclusion_angle)
        with pytest.raises(Exception):
            oSAR.fore_exclusion_angle = 90

        oSAR.aft_exclusion_angle = 34.56789
        Assert.assertEqual(34.56789, oSAR.aft_exclusion_angle)
        with pytest.raises(Exception):
            oSAR.aft_exclusion_angle = 90

        oSAR.parent_altitude = 1.4
        Assert.assertEqual(1.4, oSAR.parent_altitude)
        with pytest.raises(Exception):
            oSAR.parent_altitude = -12.34

        oSAR.angular_resolution = 0.1
        Assert.assertAlmostEqual(float(oSAR.angular_resolution), 0.1, delta=1e-06)
        oSAR.angular_resolution = 10.0
        Assert.assertAlmostEqual(float(oSAR.angular_resolution), 10.0, delta=1e-06)
        with pytest.raises(Exception):
            oSAR.angular_resolution = 0.001
        with pytest.raises(Exception):
            oSAR.angular_resolution = 10.1

        oSAR.track_parent_altitude = False
        Assert.assertEqual(False, oSAR.track_parent_altitude)
        oSAR.track_parent_altitude = True
        Assert.assertEqual(True, oSAR.track_parent_altitude)

        # SetPatternType(EOIR) is tested in EOIR test

        # restore Units
        self.m_oRoot.unit_preferences.reset_units()
        self.m_logger.WriteLine("----- THE BASIC DEFINITION TEST ----- END -----")

    # endregion

    # region STKObject
    def STKObject(self):
        oHelper = STKObjectHelper()
        oSensor: "IStkObject" = clr.CastAs(self.m_oSensor, IStkObject)
        oHelper.Run(oSensor)
        oHelper.TestObjectFilesArray(oSensor.object_files)

    # endregion

    # region BasicLocation
    def BasicLocation(self):
        self.m_logger.WriteLine("----- THE BASIC LOCATION TEST ----- BEGIN -----")
        # LocationType
        self.m_logger.WriteLine6("\tThe current LocationType is: {0}", self.m_oSensor.location_type)
        # SetLocationType(MODEL_3D)
        self.m_oSensor.set_location_type(SENSOR_LOCATION.MODEL_3D)
        self.m_logger.WriteLine6("\tThe new LocationType is: {0}", self.m_oSensor.location_type)
        Assert.assertEqual(SENSOR_LOCATION.MODEL_3D, self.m_oSensor.location_type)
        # LocationData
        with pytest.raises(Exception):
            locationData: "Position" = self.m_oSensor.location_data

        # SetLocationType(MODEL_3D_WITH_SCALE)
        self.m_oSensor.set_location_type(SENSOR_LOCATION.MODEL_3D_WITH_SCALE)
        self.m_logger.WriteLine6("\tThe new LocationType is: {0}", self.m_oSensor.location_type)
        Assert.assertEqual(SENSOR_LOCATION.MODEL_3D_WITH_SCALE, self.m_oSensor.location_type)
        # LocationData
        with pytest.raises(Exception):
            locationData: "Position" = self.m_oSensor.location_data

        # SetLocationType(CENTER)
        self.m_oSensor.set_location_type(SENSOR_LOCATION.CENTER)
        self.m_logger.WriteLine6("\tThe new LocationType is: {0}", self.m_oSensor.location_type)
        Assert.assertEqual(SENSOR_LOCATION.CENTER, self.m_oSensor.location_type)
        # LocationData
        with pytest.raises(Exception):
            locationData: "Position" = self.m_oSensor.location_data

        self.m_oSensor.set_location_type(SENSOR_LOCATION.VECTOR_GEOMETRY_TOOL_POINT)
        Assert.assertEqual(SENSOR_LOCATION.VECTOR_GEOMETRY_TOOL_POINT, self.m_oSensor.location_type)
        vgtPoint: "LocationVectorGeometryToolPoint" = clr.CastAs(
            self.m_oSensor.location_data, LocationVectorGeometryToolPoint
        )
        vgtPoint.point_path = "Facility/Facility1 Center"
        Assert.assertEqual("Facility/Facility1 Center", vgtPoint.point_path)

        # SetLocationType(FIXED)
        self.m_oSensor.set_location_type(SENSOR_LOCATION.FIXED)
        self.m_logger.WriteLine6("\tThe new LocationType is: {0}", self.m_oSensor.location_type)
        Assert.assertEqual(SENSOR_LOCATION.FIXED, self.m_oSensor.location_type)

        # Stopped using the position test for sensors because the values are too generic and invalid for this test.
        pos: "IPosition" = clr.CastAs(self.m_oSensor.location_data, IPosition)
        pos.assign_cartesian(0, 0, 0)
        cart: "Cartesian" = clr.CastAs(pos.convert_to(POSITION_TYPE.CARTESIAN), Cartesian)
        Assert.assertEqual(0, cart.x)
        Assert.assertEqual(0, cart.y)
        Assert.assertEqual(0, cart.z)
        pos.assign_spherical(0, 0, 0)
        sphere: "Spherical" = clr.CastAs(pos.convert_to(POSITION_TYPE.SPHERICAL), Spherical)
        Assert.assertEqual(0, sphere.lat)
        Assert.assertEqual(0, sphere.lon)
        Assert.assertEqual(0, sphere.radius)
        # PositionTest oPositionTest = new PositionTest(m_oRoot.UnitPreferences);        #			Assert.IsNotNull(oPositionTest);        #			PositionTest.Positions eTypes = PositionTest.Positions.Cartesian | PositionTest.Positions.Spherical;        #			oPositionTest.Run( (IPosition)m_oSensor.LocationData, eTypes );

        self.m_logger.WriteLine("----- THE BASIC LOCATION TEST ----- END -----")

    # endregion

    # region BasicPointing
    def BasicPointing(self, eType: "STK_OBJECT_TYPE"):
        self.m_logger.WriteLine("----- THE BASIC POINTING TEST ----- BEGIN -----")
        # set AngleUnit
        strAngleUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit is: {0}", strAngleUnit)
        self.m_oRoot.unit_preferences.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5(
            "\tThe new AngleUnit is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit")
        )
        Assert.assertEqual("rad", self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit"))
        # set DateFormat
        strDateFormat: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat")
        self.m_logger.WriteLine5("\tThe current DateFormat is: {0}", strDateFormat)
        self.m_oRoot.unit_preferences.set_current_unit("DateFormat", "UTCG")
        self.m_logger.WriteLine5(
            "\tThe new DateFormat is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat")
        )
        Assert.assertEqual("UTCG", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat"))
        # set DistanceUnit
        strDistanceUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", "m")
        self.m_logger.WriteLine5(
            "\tThe new DistanceUnit is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("m", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))

        # PointingType
        self.m_logger.WriteLine6("\tThe current PointingType is: {0}", self.m_oSensor.pointing_type)
        if TestBase.NoGraphicsMode:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_3D_MODEL)

        else:
            self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_3D_MODEL)
            self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
            Assert.assertEqual(SENSOR_POINTING.POINT_3D_MODEL, self.m_oSensor.pointing_type)
            # Pointing
            o3DModel: "SensorPointing3DModel" = SensorPointing3DModel(self.m_oSensor.pointing)
            Assert.assertIsNotNone(o3DModel)
            self.m_logger.WriteLine5("\t\tThe current AttachName is: {0}", o3DModel.attach_name)
            arElements = o3DModel.available_elements
            self.m_logger.WriteLine3("\t\tThere are {0} available elements:", Array.Length(arElements))

            iIndex: int = 0
            while iIndex < Array.Length(arElements):
                o3DModel.attach_name = str(arElements[iIndex])
                self.m_logger.WriteLine5("\t\t\tThe new AttachName is: {0}", o3DModel.attach_name)
                Assert.assertEqual(str(arElements[iIndex]), o3DModel.attach_name)

                iIndex += 1

            with pytest.raises(Exception):
                o3DModel.attach_name = "InvalidName"

        # endregion

        # region POINT_EXTERNAL
        # SetPointingType(POINT_EXTERNAL)
        strCorrect: str = TestBase.GetScenarioFile("SensorPointing_External.sp")
        strIncorrect: str = TestBase.GetScenarioFile("SensorPointing_External78.sp")
        try:
            self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_EXTERNAL)
            Assert.fail("The SetPointing method should not allow to set a eSensorPointingExternal pointing type.")

        except AssertionError as e:
            raise e

        except Exception as e:
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        with pytest.raises(Exception):
            self.m_oSensor.set_pointing_external_file(strIncorrect)
        with pytest.raises(Exception):
            self.m_oSensor.set_pointing_external_file("")
        # SetPointingExternalFile
        self.m_oSensor.set_pointing_external_file(strCorrect)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_EXTERNAL, self.m_oSensor.pointing_type)
        # Pointing
        oExternal: "SensorPointingExternal" = SensorPointingExternal(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oExternal)
        # Filename
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oExternal.filename)
        oExternal.filename = TestBase.GetScenarioFile("AttTimeAzElAngs_Example.sp")
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oExternal.filename)
        with pytest.raises(Exception):
            oExternal.filename = strIncorrect
        # endregion

        # region POINT_FIXED
        # SetPointingType(POINT_FIXED)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED, self.m_oSensor.pointing_type)
        # Pointing
        oFixed: "SensorPointingFixed" = SensorPointingFixed(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oFixed)
        # Orientation
        oHelper = OrientationTest(self.m_oRoot.unit_preferences)
        oHelper.Run(oFixed.orientation, Orientations.All)
        # endregion

        # region POINT_FIXED_AXES
        # SetPointingType(POINT_FIXED_AXES)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED_AXES)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED_AXES, self.m_oSensor.pointing_type)
        # Pointing
        oFixedAxes: "SensorPointingFixedAxes" = SensorPointingFixedAxes(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oFixedAxes)
        # ReferenceAxes
        self.m_logger.WriteLine5("\t\tThe current ReferenceAxes is: {0}", oFixedAxes.reference_axes)
        oFixedAxes.reference_axes = "CentralBody/Sun MOJ2000 Axes"
        self.m_logger.WriteLine5("\t\tThe new ReferenceAxes is: {0}", oFixedAxes.reference_axes)
        Assert.assertEqual("CentralBody/Sun MOJ2000 Axes", oFixedAxes.reference_axes)
        with pytest.raises(Exception):
            oFixedAxes.reference_axes = "Sun MOJ2000"
        # AvailableAxes
        arAxes = oFixedAxes.available_axes
        self.m_logger.WriteLine3("\t\tAvailable {0} Reference Axes:", Array.Length(arAxes))
        if Array.Length(arAxes) > 0:
            strAxes: str = str(arAxes[0])
            self.m_logger.WriteLine7("\t\t\tAxes {0}: {1}", 0, strAxes)
            oSensor: "IStkObject" = clr.CastAs(self.m_oSensor, IStkObject)
            if (
                ((strAxes.find(oSensor.parent.class_name) != -1) and (strAxes.find(oSensor.parent.instance_name) != -1))
                and (strAxes.find(oSensor.class_name) != -1)
            ) and (strAxes.find(oSensor.instance_name) != -1):
                self.m_logger.WriteLine("\t\t\t\tCannot set reference to itself.")
                with pytest.raises(Exception):
                    oFixedAxes.reference_axes = strAxes

            else:
                oFixedAxes.reference_axes = strAxes
                self.m_logger.WriteLine5("\t\t\t\tThe new ReferenceAxes is: {0}", oFixedAxes.reference_axes)
                Assert.assertEqual(strAxes, oFixedAxes.reference_axes)

        # Orientation
        oHelper.Run(oFixedAxes.orientation, Orientations.All)
        if ((eType == STK_OBJECT_TYPE.TARGET) or (eType == STK_OBJECT_TYPE.FACILITY)) or (
            eType == STK_OBJECT_TYPE.PLACE
        ):
            self.m_logger.WriteLine4(
                "\t\tThe current UseRefAxesFlippedAboutX is: {0}", oFixedAxes.use_reference_axes_flipped_about_x
            )
            Assert.assertTrue(oFixedAxes.use_reference_axes_flipped_about_x)
            oFixedAxes.use_reference_axes_flipped_about_x = False
            self.m_logger.WriteLine4(
                "\t\tThe new UseRefAxesFlippedAboutX is: {0}", oFixedAxes.use_reference_axes_flipped_about_x
            )
            Assert.assertFalse(oFixedAxes.use_reference_axes_flipped_about_x)
            self.m_logger.WriteLine4(
                "\t\tThe current UseRefAxesFlippedAboutX is: {0}", oFixedAxes.use_reference_axes_flipped_about_x
            )
            oFixedAxes.use_reference_axes_flipped_about_x = True
            self.m_logger.WriteLine4(
                "\t\tThe new UseRefAxesFlippedAboutX is: {0}", oFixedAxes.use_reference_axes_flipped_about_x
            )
            Assert.assertTrue(oFixedAxes.use_reference_axes_flipped_about_x)

        else:
            self.m_logger.WriteLine4(
                "\t\tThe current UseRefAxesFlippedAboutX is: {0}", oFixedAxes.use_reference_axes_flipped_about_x
            )
            Assert.assertFalse(oFixedAxes.use_reference_axes_flipped_about_x)
            with pytest.raises(Exception):
                oFixedAxes.use_reference_axes_flipped_about_x = True

        # endregion

        # region POINT_SPINNING
        # SetPointingType(POINT_SPINNING)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_SPINNING)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_SPINNING, self.m_oSensor.pointing_type)
        # Pointing
        oSpinning: "SensorPointingSpinning" = SensorPointingSpinning(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oSpinning)

        # region CONTINUOUS
        # ScanMode (CONTINUOUS)
        self.m_logger.WriteLine6("\t\tThe current ScanMode is: {0}", oSpinning.scan_mode)
        oSpinning.scan_mode = SENSOR_SCAN_MODE.CONTINUOUS
        self.m_logger.WriteLine6("\t\tThe new ScanMode is: {0}", oSpinning.scan_mode)
        Assert.assertEqual(SENSOR_SCAN_MODE.CONTINUOUS, oSpinning.scan_mode)
        # ClockAngleStart
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = 1.234
        # ClockAngleStop
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 3.456
        # SpinRate
        self.m_logger.WriteLine6("\t\t\tThe current SpinRate is: {0}", oSpinning.spin_rate)
        oSpinning.spin_rate = 98.7654321
        self.m_logger.WriteLine6("\t\t\tThe new SpinRate is: {0}", oSpinning.spin_rate)
        Assert.assertAlmostEqual(98.7654321, oSpinning.spin_rate, delta=1e-07)
        with pytest.raises(Exception):
            oSpinning.spin_rate = 3400000000000000000000000000000000000000000000000000000000.0
        # OffsetAngle
        self.m_logger.WriteLine6("\t\t\tThe current OffsetAngle is: {0}", oSpinning.offset_angle)
        oSpinning.offset_angle = 0.123
        self.m_logger.WriteLine6("\t\t\tThe new OffsetAngle is: {0}", oSpinning.offset_angle)
        Assert.assertEqual(0.123, oSpinning.offset_angle)
        with pytest.raises(Exception):
            oSpinning.offset_angle = 12.34
        # SpinAxisAzimuth
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        oSpinning.spin_axis_azimuth = -0.123
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        if (eType == STK_OBJECT_TYPE.FACILITY) or (eType == STK_OBJECT_TYPE.TARGET):
            Assert.assertAlmostEqual(6.16, float(oSpinning.spin_axis_azimuth), delta=0.001)
        else:
            Assert.assertAlmostEqual(-0.123, float(oSpinning.spin_axis_azimuth), delta=0.001)
        with pytest.raises(Exception):
            oSpinning.spin_axis_azimuth = 12.34
        # SpinAxisElevation
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        oSpinning.spin_axis_elevation = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        Assert.assertEqual(1.23, oSpinning.spin_axis_elevation)
        with pytest.raises(Exception):
            oSpinning.spin_axis_elevation = 12.34
        # SpinAxisConeAngle
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        oSpinning.spin_axis_cone_angle = 2.3
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        Assert.assertEqual(2.3, oSpinning.spin_axis_cone_angle)
        with pytest.raises(Exception):
            oSpinning.spin_axis_cone_angle = 12.34
        # endregion

        # region BIDIRECTIONAL
        # ScanMode (BIDIRECTIONAL)
        oSpinning.scan_mode = SENSOR_SCAN_MODE.BIDIRECTIONAL
        self.m_logger.WriteLine6("\t\tThe new ScanMode is: {0}", oSpinning.scan_mode)
        Assert.assertEqual(SENSOR_SCAN_MODE.BIDIRECTIONAL, oSpinning.scan_mode)
        # ClockAngleStart
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        oSpinning.clock_angle_start = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        Assert.assertEqual(1.23, oSpinning.clock_angle_start)
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = -56
        # ClockAngleStop
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        oSpinning.clock_angle_stop = 3.21
        self.m_logger.WriteLine6("\t\t\tThe new ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        Assert.assertEqual(3.21, oSpinning.clock_angle_stop)
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 56
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = 5.6
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 0.56
        with pytest.raises(Exception):
            oSpinning.set_clock_angles(5, 3)
        # SetClockAngles
        oSpinning.set_clock_angles(3, 5)
        Assert.assertEqual(3, oSpinning.clock_angle_start)
        Assert.assertEqual(5, oSpinning.clock_angle_stop)
        # SpinRate
        self.m_logger.WriteLine6("\t\t\tThe current SpinRate is: {0}", oSpinning.spin_rate)
        oSpinning.spin_rate = 98.7654321
        self.m_logger.WriteLine6("\t\t\tThe new SpinRate is: {0}", oSpinning.spin_rate)
        Assert.assertAlmostEqual(98.7654321, oSpinning.spin_rate, delta=1e-06)
        with pytest.raises(Exception):
            oSpinning.spin_rate = 3400000000000000000000000000000000000000000000000000000000.0
        # OffsetAngle
        self.m_logger.WriteLine6("\t\t\tThe current OffsetAngle is: {0}", oSpinning.offset_angle)
        oSpinning.offset_angle = 0.123
        self.m_logger.WriteLine6("\t\t\tThe new OffsetAngle is: {0}", oSpinning.offset_angle)
        Assert.assertEqual(0.123, oSpinning.offset_angle)
        with pytest.raises(Exception):
            oSpinning.offset_angle = 12.34
        # SpinAxisAzimuth
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        oSpinning.spin_axis_azimuth = -0.123
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        if (eType == STK_OBJECT_TYPE.FACILITY) or (eType == STK_OBJECT_TYPE.TARGET):
            Assert.assertAlmostEqual(6.16, float(oSpinning.spin_axis_azimuth), delta=0.001)
        else:
            Assert.assertAlmostEqual(-0.123, float(oSpinning.spin_axis_azimuth), delta=0.001)
        with pytest.raises(Exception):
            oSpinning.spin_axis_azimuth = 12.34
        # SpinAxisElevation
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        oSpinning.spin_axis_elevation = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        Assert.assertEqual(1.23, oSpinning.spin_axis_elevation)
        with pytest.raises(Exception):
            oSpinning.spin_axis_elevation = 12.34
        # SpinAxisConeAngle
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        oSpinning.spin_axis_cone_angle = 2.3
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        Assert.assertEqual(2.3, oSpinning.spin_axis_cone_angle)
        with pytest.raises(Exception):
            oSpinning.spin_axis_cone_angle = 12.34
        # endregion

        # region UNIDIRECTIONAL
        # ScanMode (UNIDIRECTIONAL)
        oSpinning.scan_mode = SENSOR_SCAN_MODE.UNIDIRECTIONAL
        self.m_logger.WriteLine6("\t\tThe new ScanMode is: {0}", oSpinning.scan_mode)
        Assert.assertEqual(SENSOR_SCAN_MODE.UNIDIRECTIONAL, oSpinning.scan_mode)
        # ClockAngleStart
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        oSpinning.clock_angle_start = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        Assert.assertEqual(1.23, oSpinning.clock_angle_start)
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = -56
        # ClockAngleStop
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        oSpinning.clock_angle_stop = 3.21
        self.m_logger.WriteLine6("\t\t\tThe new ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        Assert.assertEqual(3.21, oSpinning.clock_angle_stop)
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 56
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = 5.6
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 0.56
        with pytest.raises(Exception):
            oSpinning.set_clock_angles(5, 3)
        # SetClockAngles
        oSpinning.set_clock_angles(3, 5)
        Assert.assertEqual(3, oSpinning.clock_angle_start)
        Assert.assertEqual(5, oSpinning.clock_angle_stop)
        # SpinRate
        self.m_logger.WriteLine6("\t\t\tThe current SpinRate is: {0}", oSpinning.spin_rate)
        oSpinning.spin_rate = 98.7654321
        self.m_logger.WriteLine6("\t\t\tThe new SpinRate is: {0}", oSpinning.spin_rate)
        Assert.assertAlmostEqual(98.7654321, oSpinning.spin_rate, delta=1e-07)
        with pytest.raises(Exception):
            oSpinning.spin_rate = 3400000000000000000000000000000000000000000000000000000000.0
        # OffsetAngle
        self.m_logger.WriteLine6("\t\t\tThe current OffsetAngle is: {0}", oSpinning.offset_angle)
        oSpinning.offset_angle = 0.123
        self.m_logger.WriteLine6("\t\t\tThe new OffsetAngle is: {0}", oSpinning.offset_angle)
        Assert.assertEqual(0.123, oSpinning.offset_angle)
        with pytest.raises(Exception):
            oSpinning.offset_angle = 12.34
        # SpinAxisAzimuth
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        oSpinning.spin_axis_azimuth = -0.123
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        if (eType == STK_OBJECT_TYPE.FACILITY) or (eType == STK_OBJECT_TYPE.TARGET):
            Assert.assertAlmostEqual(6.16, float(oSpinning.spin_axis_azimuth), delta=0.001)
        else:
            Assert.assertAlmostEqual(-0.123, float(oSpinning.spin_axis_azimuth), delta=0.001)
        with pytest.raises(Exception):
            oSpinning.spin_axis_azimuth = 12.34
        # SpinAxisElevation
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        oSpinning.spin_axis_elevation = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        Assert.assertEqual(1.23, oSpinning.spin_axis_elevation)
        with pytest.raises(Exception):
            oSpinning.spin_axis_elevation = 12.34
        # SpinAxisConeAngle
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        oSpinning.spin_axis_cone_angle = 2.3
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        Assert.assertEqual(2.3, oSpinning.spin_axis_cone_angle)
        with pytest.raises(Exception):
            oSpinning.spin_axis_cone_angle = 12.34
        # endregion

        # endregion

        # region POINT_TARGETED
        # SetPointingType(POINT_TARGETED)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_TARGETED)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_TARGETED, self.m_oSensor.pointing_type)
        # Pointing
        oTarget: "SensorPointingTargeted" = SensorPointingTargeted(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oTarget)
        oTarget.save_target_access = False
        Assert.assertEqual(False, oTarget.save_target_access)
        self.m_logger.WriteLine4("Target SaveTargetAccess = {0}", oTarget.save_target_access)

        # region Boresight
        # Boresight (TRACKING)
        oTarget.boresight = SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.TRACKING
        Assert.assertEqual(SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.TRACKING, oTarget.boresight)

        # BoresightData
        oTracking: "SensorPointingTargetedBoresightTrack" = SensorPointingTargetedBoresightTrack(oTarget.boresight_data)
        Assert.assertIsNotNone(oTracking)

        # AboutBoresight
        oTracking.about_boresight = BORESIGHT_TYPE.HOLD
        Assert.assertEqual(BORESIGHT_TYPE.HOLD, oTracking.about_boresight)
        with pytest.raises(Exception):
            oTracking.constraint_vector_for_up_vector_boresight = "Aircraft/Boing737 Body.-X"
        with pytest.raises(Exception):
            oTracking.clock_angle_offset_for_up_vector_boresight = 1.2

        oTracking.about_boresight = BORESIGHT_TYPE.LEVEL
        Assert.assertEqual(BORESIGHT_TYPE.LEVEL, oTracking.about_boresight)
        with pytest.raises(Exception):
            oTracking.constraint_vector_for_up_vector_boresight = "Aircraft/Boing737 Body.-X"
        with pytest.raises(Exception):
            oTracking.clock_angle_offset_for_up_vector_boresight = 1.4

        oTracking.about_boresight = BORESIGHT_TYPE.ROTATE
        Assert.assertEqual(BORESIGHT_TYPE.ROTATE, oTracking.about_boresight)
        with pytest.raises(Exception):
            oTracking.constraint_vector_for_up_vector_boresight = "Aircraft/Boing737 Body.-X"
        with pytest.raises(Exception):
            oTracking.clock_angle_offset_for_up_vector_boresight = 1.6

        oTracking.about_boresight = BORESIGHT_TYPE.UP_VECTOR
        Assert.assertEqual(BORESIGHT_TYPE.UP_VECTOR, oTracking.about_boresight)

        arAvailConstraintVecs = oTracking.available_constraint_vectors
        Assert.assertTrue((len(arAvailConstraintVecs) > 0))

        oTracking.constraint_vector_for_up_vector_boresight = "Aircraft/Boing737 Body.-Y"
        Assert.assertEqual("Aircraft/Boing737 Body.-Y", oTracking.constraint_vector_for_up_vector_boresight)
        with pytest.raises(Exception):
            oTracking.constraint_vector_for_up_vector_boresight = "Aircraft/Bogus Body.-Y"

        oTracking.clock_angle_offset_for_up_vector_boresight = 0.8
        Assert.assertEqual(0.8, oTracking.clock_angle_offset_for_up_vector_boresight)

        # TrackMode
        self.m_logger.WriteLine6("\t\t\tThe current TrackMode is: {0}", oTracking.track_mode)
        oTracking.track_mode = TRACK_MODE_TYPE.RECEIVE
        self.m_logger.WriteLine6("\t\t\tThe new TrackMode is: {0}", oTracking.track_mode)
        Assert.assertEqual(TRACK_MODE_TYPE.RECEIVE, oTracking.track_mode)
        oTracking.track_mode = TRACK_MODE_TYPE.TRANSMIT
        self.m_logger.WriteLine6("\t\t\tThe new TrackMode is: {0}", oTracking.track_mode)
        Assert.assertEqual(TRACK_MODE_TYPE.TRANSMIT, oTracking.track_mode)
        oTracking.track_mode = TRACK_MODE_TYPE.TRANSPOND
        self.m_logger.WriteLine6("\t\t\tThe new TrackMode is: {0}", oTracking.track_mode)
        Assert.assertEqual(TRACK_MODE_TYPE.TRANSPOND, oTracking.track_mode)

        # Boresight (FIXED)
        oTarget.boresight = SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.FIXED
        self.m_logger.WriteLine6("\t\tThe new Boresight is: {0}", oTarget.boresight)
        Assert.assertEqual(SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.FIXED, oTarget.boresight)
        # BoresightData
        oBrstFixed: "SensorPointingTargetedBoresightFixed" = SensorPointingTargetedBoresightFixed(
            oTarget.boresight_data
        )
        Assert.assertIsNotNone(oBrstFixed)
        # Orientation
        oHelper.Run(oBrstFixed.orientation, Orientations.All)
        # endregion

        # region Targets
        # Targets
        oTargetCollection: "SensorTargetCollection" = oTarget.targets
        Assert.assertIsNotNone(oTargetCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe current TargetCollection contains: {0} elements", oTargetCollection.count)
        # _NewEnum
        target: "SensorTarget"
        # _NewEnum
        for target in oTargetCollection:
            # Name
            self.m_logger.WriteLine5("\t\tElement: {0}", target.name)

        # RemoveAll
        oTargetCollection.remove_all()
        self.m_logger.WriteLine3(
            "\t\tAfter RemoveAll() the TargetCollection contains: {0} elements", oTargetCollection.count
        )
        Assert.assertEqual(0, oTargetCollection.count)
        # EnableAccessTimes
        self.m_logger.WriteLine4("\t\tThe current EnableAccessTimes flag is: {0}", oTarget.enable_access_times)
        with pytest.raises(Exception):
            oTarget.enable_access_times = False
        # AvailableTargets
        arTargets = oTarget.available_targets
        self.m_logger.WriteLine3("\t\tThe AvailableTargets array contains: {0} elements", Array.Length(arTargets))
        if Array.Length(arTargets) > 0:
            strTarget: str = str(arTargets[0])
            self.m_logger.WriteLine7("\t\t\tElement {0}: {1}", 0, strTarget)
            oTargetCollection.add(strTarget)
            self.m_logger.WriteLine5("\t\t\t\tThe element {0} was added to the TargetCollection.", strTarget)
            Assert.assertEqual(1, oTargetCollection.count)
            # Remove
            self.m_logger.WriteLine3(
                "\t\tBefore Remove() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            oTargetCollection.remove(0)
            self.m_logger.WriteLine3(
                "\t\tAfter Remove() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            Assert.assertEqual(0, oTargetCollection.count)
            oTargetCollection.add(strTarget)
            self.m_logger.WriteLine5("\t\t\t\tThe element {0} was added to the TargetCollection.", strTarget)
            Assert.assertEqual(1, oTargetCollection.count)
            # RemoveTarget
            oTargetCollection.remove_target(oTargetCollection[0].name)
            self.m_logger.WriteLine3(
                "\t\tAfter RemoveTarget() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            Assert.assertEqual(0, oTargetCollection.count)
            # AddObject
            oObject: "IStkObject" = self.m_oRoot.current_scenario.children["NeptuneFile"]
            Assert.assertIsNotNone(oObject)
            oTargetCollection.add_object(oObject)
            self.m_logger.WriteLine3(
                "\t\tAfter AddObject() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            Assert.assertEqual(1, oTargetCollection.count)
            # RemoveObject
            oTargetCollection.remove_object(oObject)
            self.m_logger.WriteLine3(
                "\t\tAfter RemoveObject() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            Assert.assertEqual(0, oTargetCollection.count)
            oTargetCollection.add(strTarget)
            self.m_logger.WriteLine5("\t\t\t\tThe element {0} was added to the TargetCollection.", strTarget)
            Assert.assertEqual(1, oTargetCollection.count)

        # endregion

        # region AccessTimes
        # Access time
        oATH = AccessTimeHelper()
        oATH.Run(oTarget.access_times)
        # EnableAccessTimes (true)
        self.m_logger.WriteLine4("\t\tThe current EnableAccessTimes flag is: {0}", oTarget.enable_access_times)
        oTarget.enable_access_times = True
        self.m_logger.WriteLine4("\t\tThe new EnableAccessTimes flag is: {0}", oTarget.enable_access_times)
        Assert.assertEqual(True, oTarget.enable_access_times)
        # ScheduleTimes
        oScheduleTimeCollection: "ScheduleTimeCollection" = oTarget.schedule_times
        Assert.assertIsNotNone(oScheduleTimeCollection)
        oStart: typing.Any = None
        oStop: typing.Any = None
        strName: str = ""
        if oScheduleTimeCollection.count > 0:
            oStart = oScheduleTimeCollection[0].start_time
            oStop = oScheduleTimeCollection[0].stop_time
            strName = oScheduleTimeCollection[0].target
            # RemoveIndex
            with pytest.raises(Exception):
                oScheduleTimeCollection.remove_index(0)
            # Add
            with pytest.raises(Exception):
                oScheduleTimeCollection.add(oStart, oStop, strName)
            # RemoveSchedule
            with pytest.raises(Exception):
                oScheduleTimeCollection.remove_schedule(oStart, oStop, strName)
            # RemoveAll
            with pytest.raises(Exception):
                oScheduleTimeCollection.remove_all()

        # EnableAccessTimes (false)
        oTarget.enable_access_times = False
        self.m_logger.WriteLine4("\t\tThe new EnableAccessTimes flag is: {0}", oTarget.enable_access_times)
        Assert.assertEqual(False, oTarget.enable_access_times)
        # endregion

        # region ScheduleTimes
        # ScheduleTimes
        oScheduleTimeCollection = oTarget.schedule_times
        Assert.assertIsNotNone(oScheduleTimeCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count)
        # _NewEnum
        scheduleTime: "ScheduleTime"
        # _NewEnum
        for scheduleTime in oScheduleTimeCollection:
            self.m_logger.WriteLine8(
                "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                scheduleTime.start_time,
                scheduleTime.stop_time,
                "Target",
            )

        # Deconflict
        oScheduleTimeCollection.deconflict()
        if oScheduleTimeCollection.count == 0:
            oScheduleTimeCollection.add("1 Jun 1999 11:00:00.000", "1 Jul 1999 12:00:00.000", oTarget.targets[0].name)
            self.m_logger.WriteLine3(
                "\t\tAfter Add() the ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count
            )
            Assert.assertEqual(1, oScheduleTimeCollection.count)
            scheduleTime: "ScheduleTime"
            for scheduleTime in oScheduleTimeCollection:
                self.m_logger.WriteLine8(
                    "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                    scheduleTime.start_time,
                    scheduleTime.stop_time,
                    scheduleTime.target,
                )

        # Item
        oStart = oScheduleTimeCollection[0].start_time
        oStop = oScheduleTimeCollection[0].stop_time
        strName = oScheduleTimeCollection[0].target
        strName = oTarget.targets[0].name
        iCount: int = oScheduleTimeCollection.count
        # RemoveIndex
        oScheduleTimeCollection.remove_index(0)
        self.m_logger.WriteLine3(
            "\t\tAfter RemoveIndex() the ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count
        )
        Assert.assertEqual((iCount - 1), oScheduleTimeCollection.count)
        scheduleTime: "ScheduleTime"
        for scheduleTime in oScheduleTimeCollection:
            self.m_logger.WriteLine8(
                "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                scheduleTime.start_time,
                scheduleTime.stop_time,
                "Target",
            )

        with pytest.raises(Exception):
            oScheduleTimeCollection.remove_index(-12)
        # Add
        oScheduleTimeCollection.add(oStart, oStop, strName)
        self.m_logger.WriteLine3(
            "\t\tAfter Add() the ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count
        )
        Assert.assertEqual(iCount, oScheduleTimeCollection.count)
        scheduleTime: "ScheduleTime"
        for scheduleTime in oScheduleTimeCollection:
            self.m_logger.WriteLine8(
                "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                scheduleTime.start_time,
                scheduleTime.stop_time,
                "Target",
            )

        with pytest.raises(Exception):
            oScheduleTimeCollection.add(oStart, oStop, "InvalidName")
        # RemoveSchedule
        oScheduleTimeCollection.remove_schedule(oStart, oStop, strName)
        self.m_logger.WriteLine3(
            "\t\tAfter RemoveSchedule() the ScheduleTimeCollection contains: {0} elements",
            oScheduleTimeCollection.count,
        )
        Assert.assertEqual((iCount - 1), oScheduleTimeCollection.count)
        with pytest.raises(Exception):
            oScheduleTimeCollection.remove_schedule(oStart, oStop, "InvalidName")
        # RemoveAll
        oScheduleTimeCollection.remove_all()
        self.m_logger.WriteLine3(
            "\t\tAfter RemoveAll() the ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count
        )
        Assert.assertEqual(0, oScheduleTimeCollection.count)
        # Add
        oStart = "1 Jun 2004 12:00:00.000"
        oStop = "1 Jun 2004 15:00:00.000"
        strName = oTarget.targets[0].name
        oScheduleTime: "ScheduleTime" = oScheduleTimeCollection.add(oStart, oStop, strName)
        Assert.assertIsNotNone(oScheduleTime)
        Assert.assertEqual(oStart, oScheduleTime.start_time)
        Assert.assertEqual(oStop, oScheduleTime.stop_time)
        Assert.assertEqual(strName, oScheduleTime.target)
        Assert.assertEqual(1, oScheduleTimeCollection.count)
        scheduleTime: "ScheduleTime"
        for scheduleTime in oScheduleTimeCollection:
            self.m_logger.WriteLine8(
                "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                scheduleTime.start_time,
                scheduleTime.stop_time,
                scheduleTime.target,
            )

        # StopTime
        oScheduleTime.stop_time = oStop
        Assert.assertEqual(oStop, oScheduleTime.stop_time)
        with pytest.raises(Exception):
            oScheduleTime.stop_time = "1 Jun 2004 09:00:00.000"
        # StartTime
        oScheduleTime.start_time = oStart
        Assert.assertEqual(oStart, oScheduleTime.start_time)
        with pytest.raises(Exception):
            oScheduleTime.start_time = "1 Jun 2004 18:00:00.000"
        # Target
        oScheduleTime.target = strName
        Assert.assertEqual(strName, oScheduleTime.target)
        with pytest.raises(Exception):
            oScheduleTime.target = "InvalidName"
        # Add
        with pytest.raises(Exception):
            oScheduleTimeCollection.add("1 Jun 2004 12:00:00.00", "1 Jun 2004 11:00:00.00", "Star/Star1")
        # endregion

        # region Advanced
        # Advanced
        oAdvanced: "SensorAccessAdvanced" = oTarget.advanced
        Assert.assertIsNotNone(oAdvanced)
        # AberrationType
        self.m_logger.WriteLine6("\tThe current AberrationType is: {0}", oAdvanced.aberration_type)
        (oAdvanced).aberration_type = ABERRATION_TYPE.ANNUAL
        self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
        Assert.assertEqual(ABERRATION_TYPE.ANNUAL, oAdvanced.aberration_type)
        (oAdvanced).aberration_type = ABERRATION_TYPE.NONE
        self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
        Assert.assertEqual(ABERRATION_TYPE.NONE, oAdvanced.aberration_type)
        (oAdvanced).aberration_type = ABERRATION_TYPE.TOTAL
        self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
        Assert.assertEqual(ABERRATION_TYPE.TOTAL, oAdvanced.aberration_type)
        with pytest.raises(Exception):
            (oAdvanced).aberration_type = ABERRATION_TYPE.UNKNOWN
        # TimeDelayConvergence
        self.m_logger.WriteLine6("\tThe current TimeDelayConvergence is: {0}", oAdvanced.time_delay_convergence)
        oAdvanced.time_delay_convergence = 0.1
        self.m_logger.WriteLine6("\tThe new TimeDelayConvergence is: {0}", oAdvanced.time_delay_convergence)
        Assert.assertEqual(0.1, oAdvanced.time_delay_convergence)
        with pytest.raises(Exception):
            oAdvanced.time_delay_convergence = 0.5
        # EventDetection
        oEDHelper = AccessEventDetectionHelper()
        oEDHelper.Run(oAdvanced.event_detection, False)
        # Sampling
        oSHelper = AccessSamplingHelper()
        oSHelper.Run(oAdvanced.sampling, False)
        # endregion

        # endregion

        # region POINT_GRAZING_ALTITUDE
        # SetPointingType(POINT_GRAZING_ALTITUDE);
        try:
            self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_GRAZING_ALTITUDE)
            self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
            Assert.assertEqual(SENSOR_POINTING.POINT_GRAZING_ALTITUDE, self.m_oSensor.pointing_type)
            # Pointing
            oGrazing: "SensorPointingGrazingAltitude" = SensorPointingGrazingAltitude(self.m_oSensor.pointing)
            Assert.assertIsNotNone(oGrazing)
            # AzimuthOffset
            self.m_logger.WriteLine6("\t\tThe current AzimuthOffset is: {0}", oGrazing.azimuth_offset)
            oGrazing.azimuth_offset = 3.45
            self.m_logger.WriteLine6("\t\tThe new AzimuthOffset is: {0}", oGrazing.azimuth_offset)
            Assert.assertEqual(3.45, oGrazing.azimuth_offset)
            with pytest.raises(Exception):
                oGrazing.azimuth_offset = 9.876
            # GrazingAlt
            self.m_logger.WriteLine6("\t\tThe current GrazingAlt is: {0}", oGrazing.grazing_altitude)
            oGrazing.grazing_altitude = 12345.6789
            self.m_logger.WriteLine6("\t\tThe new GrazingAlt is: {0}", oGrazing.grazing_altitude)
            Assert.assertEqual(12345.6789, oGrazing.grazing_altitude)
            with pytest.raises(Exception):
                oGrazing.grazing_altitude = -9.876

        except Exception as e:
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        # endregion

        # region POINT_ALONG_VECTOR
        # SetPointingType(POINT_ALONG_VECTOR)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_ALONG_VECTOR)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_ALONG_VECTOR, self.m_oSensor.pointing_type)
        # Pointing
        alongVector: "SensorPointingAlongVector" = SensorPointingAlongVector(self.m_oSensor.pointing)
        Assert.assertIsNotNone(alongVector)

        arAvailAlignmentVecs = alongVector.available_alignment_vectors
        Assert.assertTrue((len(arAvailAlignmentVecs) > 0))
        alongVector.alignment_vector = "Aircraft/Boing737 Body.-X"
        Assert.assertEqual("Aircraft/Boing737 Body.-X", alongVector.alignment_vector)

        arAvailConstraintVecs = alongVector.available_constraint_vectors
        Assert.assertTrue((len(arAvailConstraintVecs) > 0))
        alongVector.constraint_vector = "Aircraft/Boing737 Body.-Y"
        Assert.assertEqual("Aircraft/Boing737 Body.-Y", alongVector.constraint_vector)

        self.m_oRoot.unit_preferences.set_current_unit("AngleUnit", "deg")
        alongVector.clock_angle_offset = 10
        Assert.assertEqual(10, alongVector.clock_angle_offset)
        # endregion

        # restore Units
        self.m_oRoot.unit_preferences.reset_units()
        self.m_logger.WriteLine("----- THE BASIC POINTING TEST ----- END -----")

    # region BasicResolution
    def BasicResolution(self):
        self.m_logger.WriteLine("----- THE BASIC RESOLUTION TEST ----- BEGIN -----")
        # set SmallDistanceUnit
        strSmallDistanceUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit")
        self.m_logger.WriteLine5("\tThe current SmallDistanceUnit format is: {0}", strSmallDistanceUnit)
        self.m_oRoot.unit_preferences.set_current_unit("SmallDistanceUnit", "cm")
        self.m_logger.WriteLine5(
            "\tThe new SmallDistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"),
        )
        Assert.assertEqual("cm", self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"))

        # FocalLength
        self.m_logger.WriteLine6("\tThe current FocalLength is: {0}", self.m_oSensor.focal_length)
        self.m_oSensor.focal_length = 1234567890.123
        self.m_logger.WriteLine6("\tThe new FocalLength is: {0}", self.m_oSensor.focal_length)
        Assert.assertEqual(1234567890.123, self.m_oSensor.focal_length)
        with pytest.raises(Exception):
            self.m_oSensor.focal_length = -1234.5678
        # DetectorPitch
        self.m_logger.WriteLine6("\tThe current DetectorPitch is: {0}", self.m_oSensor.detector_pitch)
        self.m_oSensor.detector_pitch = 12.34
        self.m_logger.WriteLine6("\tThe new DetectorPitch is: {0}", self.m_oSensor.detector_pitch)
        Assert.assertEqual(12.34, self.m_oSensor.detector_pitch)
        with pytest.raises(Exception):
            self.m_oSensor.detector_pitch = -5678.1234

        # restore SmallDistanceUnit
        self.m_oRoot.unit_preferences.set_current_unit("SmallDistanceUnit", strSmallDistanceUnit)
        self.m_logger.WriteLine5(
            "\tRestored SmallDistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"),
        )
        Assert.assertEqual(
            strSmallDistanceUnit, self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit")
        )
        self.m_logger.WriteLine("----- THE BASIC RESOLUTION TEST ----- END -----")

    # endregion

    # region BasicSensorAzElMask
    def BasicSensorAzElMask(self):
        self.m_logger.WriteLine("----- THE BASIC SENSOR AZ/EL MASK TEST ----- BEGIN -----")
        # AzElMask
        self.m_logger.WriteLine6("\tThe current AzElMask is: {0}", self.m_oSensor.az_el_mask)
        # ResetAzElMask
        self.m_oSensor.reset_az_el_mask()
        self.m_logger.WriteLine6("\tAfter ResetAzElMask the AzElMask is: {0}", self.m_oSensor.az_el_mask)
        # SetAzElMask(NONE)
        self.m_oSensor.set_az_el_mask(AZ_EL_MASK_TYPE.NONE)
        Assert.assertEqual(AZ_EL_MASK_TYPE.NONE, self.m_oSensor.az_el_mask)
        with pytest.raises(Exception):
            azElMaskData: "SensorAzElMaskFile" = self.m_oSensor.az_el_mask_data
        # SetAzElMask(MASK_FILE)
        with pytest.raises(Exception):
            self.m_oSensor.set_az_el_mask(AZ_EL_MASK_TYPE.MASK_FILE)
        Assert.assertEqual(AZ_EL_MASK_TYPE.NONE, self.m_oSensor.az_el_mask)
        # SetAzElMaskFile
        self.m_oSensor.set_az_el_mask_file(TestBase.GetScenarioFile("maskfile.aem"))
        self.m_logger.WriteLine6("\tThe new AzElMask is: {0}", self.m_oSensor.az_el_mask)
        Assert.assertEqual(AZ_EL_MASK_TYPE.MASK_FILE, self.m_oSensor.az_el_mask)
        with pytest.raises(Exception):
            self.m_oSensor.set_az_el_mask_file(TestBase.GetScenarioFile("InvalidName.aem"))
        # AzElMaskData
        oMaskFile: "SensorAzElMaskFile" = SensorAzElMaskFile(self.m_oSensor.az_el_mask_data)
        Assert.assertIsNotNone(oMaskFile)
        # Filename
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oMaskFile.filename)
        # BoresightAxis(PLUS_MINUS_X)
        self.m_logger.WriteLine6("\t\tThe current BoresightAxis is: {0}", oMaskFile.boresight_axis)
        oMaskFile.boresight_axis = SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE.PLUS_MINUS_X
        self.m_logger.WriteLine6("\t\tThe new BoresightAxis is: {0}", oMaskFile.boresight_axis)
        Assert.assertEqual(SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE.PLUS_MINUS_X, oMaskFile.boresight_axis)
        # BoresightAxis(PLUS_MINUS_Y)
        oMaskFile.boresight_axis = SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE.PLUS_MINUS_Y
        self.m_logger.WriteLine6("\t\tThe new BoresightAxis is: {0}", oMaskFile.boresight_axis)
        Assert.assertEqual(SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE.PLUS_MINUS_Y, oMaskFile.boresight_axis)
        # BoresightAxis()
        oMaskFile.boresight_axis = SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE.PLUS_MINUS_Z
        self.m_logger.WriteLine6("\t\tThe new BoresightAxis is: {0}", oMaskFile.boresight_axis)
        Assert.assertEqual(SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE.PLUS_MINUS_Z, oMaskFile.boresight_axis)
        # SetAzElMask(TERRAIN_DATA)
        with pytest.raises(Exception):
            self.m_oSensor.set_az_el_mask(AZ_EL_MASK_TYPE.TERRAIN_DATA)
        Assert.assertEqual(AZ_EL_MASK_TYPE.MASK_FILE, self.m_oSensor.az_el_mask)
        # ResetAzElMask
        self.m_oSensor.reset_az_el_mask()
        self.m_logger.WriteLine6("\tAfter ResetAzElMask the AzElMask is: {0}", self.m_oSensor.az_el_mask)
        Assert.assertEqual(AZ_EL_MASK_TYPE.NONE, self.m_oSensor.az_el_mask)
        self.m_logger.WriteLine("----- THE BASIC SENSOR AZ/EL MASK TEST ----- END -----")

    # endregion

    # region Graphics
    def Graphics(self):
        self.m_logger.WriteLine("----- THE GRAPHICS TEST ----- BEGIN -----")
        # Graphics
        oGraphics: "SensorGraphics" = self.m_oSensor.graphics
        Assert.assertIsNotNone(oGraphics)

        # IsObjectGraphicsVisible
        self.m_logger.WriteLine4("\tThe current IsObjectGraphicsVisible is: {0}", oGraphics.is_object_graphics_visible)
        oGraphics.is_object_graphics_visible = False
        self.m_logger.WriteLine4("\tThe new IsObjectGraphicsVisible is: {0}", oGraphics.is_object_graphics_visible)
        Assert.assertFalse(oGraphics.is_object_graphics_visible)
        oGraphics.is_object_graphics_visible = True
        Assert.assertTrue(oGraphics.is_object_graphics_visible)

        # Color
        self.m_logger.WriteLine6("\tThe current Color is: {0}", oGraphics.color)
        oGraphics.color = Colors.from_argb(16384250)
        self.m_logger.WriteLine6("\tThe new Color is: {0}", oGraphics.color)
        AssertEx.AreEqual(Colors.from_argb(16384250), oGraphics.color)
        # LineStyle
        self.m_logger.WriteLine6("\tThe current LineStyle is: {0}", oGraphics.line_style)
        oGraphics.line_style = LINE_STYLE.DASHED  # Dashed
        self.m_logger.WriteLine6("\tThe new LineStyle is: {0}", oGraphics.line_style)
        Assert.assertEqual(LINE_STYLE.DASHED, oGraphics.line_style)

        # LineWidth
        self.m_logger.WriteLine6("\tThe current LineWidth is: {0}", oGraphics.line_width)
        oGraphics.line_width = LINE_WIDTH.WIDTH1  # WIDTH1
        self.m_logger.WriteLine6("\tThe new LineWidth is: {0}", oGraphics.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH1, oGraphics.line_width)
        with pytest.raises(Exception):
            oGraphics.line_width = -1
        with pytest.raises(Exception):
            oGraphics.line_width = 11

        # InheritFromScenario (true)
        self.m_logger.WriteLine4("\tThe current InheritFromScenario flag is: {0}", oGraphics.inherit_from_scenario)
        oGraphics.inherit_from_scenario = True
        self.m_logger.WriteLine4("\tThe new InheritFromScenario flag is: {0}", oGraphics.inherit_from_scenario)
        Assert.assertEqual(oGraphics.inherit_from_scenario, True)
        with pytest.raises(Exception):
            oGraphics.enable = False
        # InheritFromScenario (false)
        oGraphics.inherit_from_scenario = False
        self.m_logger.WriteLine4("\tThe new InheritFromScenario flag is: {0}", oGraphics.inherit_from_scenario)
        Assert.assertEqual(oGraphics.inherit_from_scenario, False)
        # Enable
        self.m_logger.WriteLine4("\tThe current Enable flag is: {0}", oGraphics.enable)
        oGraphics.enable = False
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oGraphics.enable)
        Assert.assertEqual(oGraphics.enable, False)
        # InheritFromScenario (true)
        oGraphics.inherit_from_scenario = True
        self.m_logger.WriteLine4("\tThe new Inheritance flag is: {0}", oGraphics.inherit_from_scenario)
        Assert.assertEqual(oGraphics.inherit_from_scenario, True)
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oGraphics.enable)
        Assert.assertEqual(oGraphics.enable, False)
        # FillVisible
        self.m_logger.WriteLine4("\tThe current FillVisible flag is: {0}", oGraphics.fill_visible)
        oGraphics.fill_visible = False
        self.m_logger.WriteLine4("\tThe new FillVisible flag is: {0}", oGraphics.fill_visible)
        Assert.assertEqual(False, oGraphics.fill_visible)
        oGraphics.fill_visible = True
        self.m_logger.WriteLine4("\tThe new FillVisible flag is: {0}", oGraphics.fill_visible)
        Assert.assertEqual(True, oGraphics.fill_visible)
        # EnableBoresightGfx (false)
        self.m_logger.WriteLine4(
            "\tThe current EnableBoresightGfx flag is: {0}", oGraphics.enable_boresight_graphics_2d
        )
        oGraphics.enable_boresight_graphics_2d = False
        self.m_logger.WriteLine4("\tThe new EnableBoresightGfx flag is: {0}", oGraphics.enable_boresight_graphics_2d)
        Assert.assertEqual(False, oGraphics.enable_boresight_graphics_2d)
        with pytest.raises(Exception):
            oGraphics.boresight_color = Colors.from_argb(11468975)
        with pytest.raises(Exception):
            oGraphics.boresight_marker_style = "Plus"
        # EnableBoresightGfx (true)
        oGraphics.enable_boresight_graphics_2d = True
        self.m_logger.WriteLine4("\tThe new EnableBoresightGfx flag is: {0}", oGraphics.enable_boresight_graphics_2d)
        Assert.assertEqual(True, oGraphics.enable_boresight_graphics_2d)
        # BoresightColor
        self.m_logger.WriteLine6("\tThe current BoresightColor is: {0}", oGraphics.boresight_color)
        oGraphics.boresight_color = Colors.from_argb(11468975)
        self.m_logger.WriteLine6("\tThe new BoresightColor is: {0}", oGraphics.boresight_color)
        AssertEx.AreEqual(Colors.from_argb(11468975), oGraphics.boresight_color)
        # BoresightMarkerStyle
        self.m_logger.WriteLine5("\tThe current BoresightMarkerStyle is: {0}", oGraphics.boresight_marker_style)
        oGraphics.boresight_marker_style = "Plus"
        self.m_logger.WriteLine5("\tThe new BoresightMarkerStyle is: {0}", oGraphics.boresight_marker_style)
        Assert.assertEqual("Plus", oGraphics.boresight_marker_style)

        oGraphics.percent_translucency = 55.0
        Assert.assertAlmostEqual(55.0, oGraphics.percent_translucency, delta=Math2.Epsilon12)

        # Projection
        self.GraphicsProjection(oGraphics.projection)
        self.m_logger.WriteLine("----- THE GRAPHICS TEST ----- END -----")

    # endregion

    # region GraphicsProjection
    def GraphicsProjection(self, oProjection: "SensorProjection"):
        Assert.assertIsNotNone(oProjection)
        # set TimeUnit
        strTimeUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("TimeUnit")
        self.m_logger.WriteLine5("\tThe current TimeUnit format is: {0}", strTimeUnit)
        self.m_oRoot.unit_preferences.set_current_unit("TimeUnit", "min")
        self.m_logger.WriteLine5(
            "\tThe new TimeUnit format is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("TimeUnit")
        )
        Assert.assertEqual("min", self.m_oRoot.unit_preferences.get_current_unit_abbrv("TimeUnit"))

        # Persistence
        self.m_logger.WriteLine6("\tThe current Persistence is: {0}", oProjection.persistence)
        oProjection.persistence = 12345.6789
        self.m_logger.WriteLine6("\tThe new Persistence is: {0}", oProjection.persistence)
        Assert.assertEqual(12345.6789, oProjection.persistence)
        with pytest.raises(Exception):
            oProjection.persistence = -123.456
        # ForwardPersistence
        self.m_logger.WriteLine4("\tThe current ForwardPersistence flag is: {0}", oProjection.forward_persistence)
        oProjection.forward_persistence = False
        self.m_logger.WriteLine4("\tThe new ForwardPersistence flag is: {0}", oProjection.forward_persistence)
        Assert.assertEqual(False, oProjection.forward_persistence)
        oProjection.forward_persistence = True
        self.m_logger.WriteLine4("\tThe new ForwardPersistence flag is: {0}", oProjection.forward_persistence)
        Assert.assertEqual(True, oProjection.forward_persistence)
        # FillPersistence
        self.m_logger.WriteLine4("\tThe current FillPersistence flag is: {0}", oProjection.fill_persistence)
        oProjection.fill_persistence = False
        self.m_logger.WriteLine4("\tThe new FillPersistence flag is: {0}", oProjection.fill_persistence)
        Assert.assertEqual(False, oProjection.fill_persistence)
        oProjection.fill_persistence = True
        self.m_logger.WriteLine4("\tThe new FillPersistence flag is: {0}", oProjection.fill_persistence)
        Assert.assertEqual(True, oProjection.fill_persistence)
        # DisplayTimesHidesPersistance
        self.m_logger.WriteLine4(
            "\tThe current DisplayTimesHidesPersistance flag is: {0}", oProjection.display_times_hides_persistance
        )
        oProjection.display_times_hides_persistance = True
        self.m_logger.WriteLine4(
            "\tThe new DisplayTimesHidesPersistance flag is: {0}", oProjection.display_times_hides_persistance
        )
        Assert.assertEqual(True, oProjection.display_times_hides_persistance)
        oProjection.display_times_hides_persistance = False
        self.m_logger.WriteLine4(
            "\tThe new DisplayTimesHidesPersistance flag is: {0}", oProjection.display_times_hides_persistance
        )
        Assert.assertEqual(False, oProjection.display_times_hides_persistance)
        # ShowOn2DMap
        self.m_logger.WriteLine4("\tThe current ShowOn2DMap flag is: {0}", oProjection.show_on_2d_map)
        oProjection.show_on_2d_map = False
        self.m_logger.WriteLine4("\tThe new ShowOn2DMap flag is: {0}", oProjection.show_on_2d_map)
        Assert.assertEqual(False, oProjection.show_on_2d_map)
        oProjection.show_on_2d_map = True
        self.m_logger.WriteLine4("\tThe new ShowOn2DMap flag is: {0}", oProjection.show_on_2d_map)
        Assert.assertEqual(True, oProjection.show_on_2d_map)
        # IntersectionType (CENTRAL_BODY)
        self.m_logger.WriteLine6("\tThe current IntersectionType is: {0}", oProjection.intersection_type)
        oProjection.intersection_type = INTERSECTION_TYPE.CENTRAL_BODY
        self.m_logger.WriteLine6("\tThe new IntersectionType is: {0}", oProjection.intersection_type)
        Assert.assertEqual(INTERSECTION_TYPE.CENTRAL_BODY, oProjection.intersection_type)
        # IntersectionType (NONE)
        oProjection.intersection_type = INTERSECTION_TYPE.NONE
        self.m_logger.WriteLine6("\tThe new IntersectionType is: {0}", oProjection.intersection_type)
        Assert.assertEqual(INTERSECTION_TYPE.NONE, oProjection.intersection_type)
        # IntersectionType (TERRAIN)
        oProjection.intersection_type = INTERSECTION_TYPE.TERRAIN
        self.m_logger.WriteLine6("\tThe new IntersectionType is: {0}", oProjection.intersection_type)
        Assert.assertEqual(INTERSECTION_TYPE.TERRAIN, oProjection.intersection_type)

        # UseConstraints (false)
        self.m_logger.WriteLine4("\tThe current UseConstraints flag is: {0}", oProjection.use_constraints)
        oProjection.use_constraints = False
        self.m_logger.WriteLine4("\tThe new UseConstraints flag is: {0}", oProjection.use_constraints)
        Assert.assertEqual(False, oProjection.use_constraints)
        # AvailableConstraints
        arAvailable = oProjection.available_constraints()
        self.m_logger.WriteLine3("\tThe AvailableConstraints array contains: {0} elements.", Array.Length(arAvailable))

        iIndex: int = 0
        while iIndex < Array.Length(arAvailable):
            self.m_logger.WriteLine7("\t\tElement {0}: {1}", iIndex, arAvailable[iIndex])

            iIndex += 1

        Assert.assertFalse((Array.Length(arAvailable) == 0))
        # EnabledConstraints
        arEnabled = oProjection.enabled_constraints()
        self.m_logger.WriteLine3("\tThe EnabledConstraints array contains: {0} elements.", Array.Length(arEnabled))

        iIndex: int = 0
        while iIndex < Array.Length(arEnabled):
            self.m_logger.WriteLine7("\t\tElement {0}: {1}", iIndex, arEnabled[iIndex])

            iIndex += 1

        Assert.assertEqual(0, Array.Length(arEnabled))
        # EnableConstraint (readonly)
        with pytest.raises(Exception):
            oProjection.enable_constraint(str(arAvailable[0]))
        # DisableConstraint (readonly)
        with pytest.raises(Exception):
            oProjection.disable_constraint(str(arAvailable[0]))
        # UseConstraints (true)
        oProjection.use_constraints = True
        self.m_logger.WriteLine4("\tThe new Use Constraints flag is: {0}", oProjection.use_constraints)
        Assert.assertEqual(True, oProjection.use_constraints)
        if Array.Length(arAvailable) > 0:
            strConstraint: str = str(arAvailable[0])
            oProjection.enable_constraint(strConstraint)
            self.m_logger.WriteLine5("\t\tConstraint {0} is enabled.", strConstraint)
            # EnableConstraint (duplicate)
            with pytest.raises(Exception):
                oProjection.enable_constraint(strConstraint)
            # EnabledConstraints
            arEnabled = oProjection.enabled_constraints()
            self.m_logger.WriteLine3("\tNow EnabledConstraints array contains: {0} elements.", Array.Length(arEnabled))
            # DisableConstraint
            oProjection.disable_constraint(strConstraint)
            self.m_logger.WriteLine5("\t\t\tConstraint {0} is disabled.", strConstraint)
            # DisableConstraint (duplicate)
            arEnabled = oProjection.enabled_constraints()
            self.m_logger.WriteLine3(
                "\tNow an Enabled constraints array contains: {0} elements.", Array.Length(arEnabled)
            )
            with pytest.raises(Exception):
                oProjection.disable_constraint(strConstraint)

            # REQ38094
            bSunGroundElevAngleSupported: bool = False
            s: str
            for s in oProjection.available_constraints():
                if String.Compare("SunGroundElevAngle", s, True) == 0:
                    bSunGroundElevAngleSupported = True
                    break

            if bSunGroundElevAngleSupported:
                oProjection.enable_constraint("SunGroundElevAngle")
                constraints = oProjection.enabled_constraints()
                found: bool = False
                constraint: str
                for constraint in constraints:
                    if constraint == "SunGroundElevAngle":
                        found = True

                if not found:
                    Assert.fail("SunGroundElevAngle was not added as a constraint.")

                oProjection.disable_constraint("SunGroundElevAngle")

        # AvailableAltitudeObjects
        arObjects = oProjection.available_altitude_objects()
        self.m_logger.WriteLine3(
            "\tThe Available Altitude objects array contains: {0} elements.", Array.Length(arObjects)
        )

        # UseDistance (false)
        self.m_logger.WriteLine4("\tThe current UseDistance is: {0}", oProjection.use_distance)
        oProjection.use_distance = False
        self.m_logger.WriteLine4("\tThe new UseDistance is: {0}", oProjection.use_distance)
        Assert.assertEqual(False, oProjection.use_distance)
        # DistanceType (readonly)
        with pytest.raises(Exception):
            oProjection.distance_type = SENSOR_PROJECTION_DISTANCE_TYPE.CONSTANT_ALTITUDE
        if Array.Length(arObjects) > 0:
            with pytest.raises(Exception):
                oProjection.project_at_altitude_object = str(arObjects[0])

        # UseDistance (true)
        oProjection.use_distance = True
        self.m_logger.WriteLine4("\tThe new UseDistance is: {0}", oProjection.use_distance)
        Assert.assertEqual(True, oProjection.use_distance)

        # DistanceType (CONSTANT_ALTITUDE)
        self.m_logger.WriteLine6("\t\tThe current DistanceType is: {0}", oProjection.distance_type)
        oProjection.distance_type = SENSOR_PROJECTION_DISTANCE_TYPE.CONSTANT_ALTITUDE
        self.m_logger.WriteLine6("\t\tThe new DistanceType is: {0}", oProjection.distance_type)
        Assert.assertEqual(SENSOR_PROJECTION_DISTANCE_TYPE.CONSTANT_ALTITUDE, oProjection.distance_type)
        # DistanceData
        self.GraphicsProjectionConstantAlt(SensorProjectionConstantAltitude(oProjection.distance_data), False)
        # DistanceType (CONSTANT_RANGE_FROM_PARENT)
        oProjection.distance_type = SENSOR_PROJECTION_DISTANCE_TYPE.CONSTANT_RANGE_FROM_PARENT
        self.m_logger.WriteLine6("\t\tThe new DistanceType is: {0}", oProjection.distance_type)
        Assert.assertEqual(SENSOR_PROJECTION_DISTANCE_TYPE.CONSTANT_RANGE_FROM_PARENT, oProjection.distance_type)
        # DistanceData
        self.GraphicsProjectionDisplayDistance(ISensorProjectionDisplayDistance(oProjection.distance_data), False)
        # DistanceType (OBJECT_ALTITUDE)
        oProjection.distance_type = SENSOR_PROJECTION_DISTANCE_TYPE.OBJECT_ALTITUDE
        self.m_logger.WriteLine6("\t\tThe new DistanceType is: {0}", oProjection.distance_type)
        Assert.assertEqual(SENSOR_PROJECTION_DISTANCE_TYPE.OBJECT_ALTITUDE, oProjection.distance_type)
        # DistanceData
        self.GraphicsProjectionObjectAlt(SensorProjectionObjectAltitude(oProjection.distance_data))

        # DistanceType (RANGE_CONSTRAINT)
        oProjection.distance_type = SENSOR_PROJECTION_DISTANCE_TYPE.RANGE_CONSTRAINT
        self.m_logger.WriteLine6("\t\tThe new DistanceType is: {0}", oProjection.distance_type)
        Assert.assertEqual(SENSOR_PROJECTION_DISTANCE_TYPE.RANGE_CONSTRAINT, oProjection.distance_type)
        # DistanceData
        with pytest.raises(Exception):
            self.GraphicsProjectionDisplayDistance(ISensorProjectionDisplayDistance(oProjection.distance_data), True)

        # ProjectAtAltObject
        self.m_logger.WriteLine5("\t\tThe current ProjectAtAltObject is: {0}", oProjection.project_at_altitude_object)
        # AvailableAltitudeObjects
        self.m_logger.WriteLine3(
            "\t\tThe Available Altitude objects array contains: {0} elements.", Array.Length(arObjects)
        )

        iIndex: int = 0
        while iIndex < Array.Length(arObjects):
            strName: str = str(arObjects[iIndex])
            self.m_logger.WriteLine7("\t\t\tElement {0}: {1}", iIndex, strName)
            oProjection.project_at_altitude_object = strName
            self.m_logger.WriteLine5(
                "\t\t\t\tThe new ProjectAtAltObject is: {0}", oProjection.project_at_altitude_object
            )

            iIndex += 1

        with pytest.raises(Exception):
            oProjection.project_at_altitude_object = "AbstractString"

        # restore TimeUnit
        self.m_oRoot.unit_preferences.set_current_unit("TimeUnit", strTimeUnit)
        self.m_logger.WriteLine5("\tThe restored TimeUnit format is: {0}", strTimeUnit)
        Assert.assertEqual(strTimeUnit, self.m_oRoot.unit_preferences.get_current_unit_abbrv("TimeUnit"))

    # endregion

    # region GraphicsProjectionDisplayDistance
    def GraphicsProjectionDisplayDistance(self, oDispData: "ISensorProjectionDisplayDistance", bReadOnly: bool):
        Assert.assertIsNotNone(oDispData)
        # set DistanceUnit
        strDistanceUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit format is: {0}", strDistanceUnit)
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", "ft")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"),
        )
        Assert.assertEqual("ft", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))
        if bReadOnly:
            # Min
            self.m_logger.WriteLine6("\t\t\tThe current Min is: {0}", oDispData.min)
            with pytest.raises(Exception):
                oDispData.min = 1234.56789
            # Max
            self.m_logger.WriteLine6("\t\t\tThe current Max is: {0}", oDispData.max)
            with pytest.raises(Exception):
                oDispData.max = 9876.54321
            # NumberOfSteps
            self.m_logger.WriteLine3("\t\t\tThe current NumberOfSteps is: {0}", oDispData.number_of_steps)
            with pytest.raises(Exception):
                oDispData.number_of_steps = 21

        else:
            # Min
            self.m_logger.WriteLine6("\t\t\tThe current Min is: {0}", oDispData.min)
            oDispData.min = 123.456789
            self.m_logger.WriteLine6("\t\t\tThe new Min is: {0}", oDispData.min)
            Assert.assertEqual(123.456789, oDispData.min)
            with pytest.raises(Exception):
                oDispData.min = -3380.84
            # Max
            self.m_logger.WriteLine6("\t\t\tThe current Max is: {0}", oDispData.max)
            oDispData.max = 987.654321
            self.m_logger.WriteLine6("\t\t\tThe new Max is: {0}", oDispData.max)
            Assert.assertAlmostEqual(987.654321, oDispData.max, delta=1e-07)
            with pytest.raises(Exception):
                oDispData.max = 3380840000000000000000.0
            with pytest.raises(Exception):
                oDispData.max = 12.3456
            with pytest.raises(Exception):
                oDispData.min = 1234.56
            # NumberOfSteps
            self.m_logger.WriteLine3("\t\t\tThe current NumberOfSteps is: {0}", oDispData.number_of_steps)
            oDispData.number_of_steps = 1
            self.m_logger.WriteLine3("\t\t\tThe new NumberOfSteps is: {0}", oDispData.number_of_steps)
            Assert.assertEqual(1, oDispData.number_of_steps)
            with pytest.raises(Exception):
                oDispData.number_of_steps = 1234
            # ProjectsThruCrossing
            self.m_logger.WriteLine4("\t\t\tThe current ProjectsThruCrossing is: {0}", oDispData.projects_thru_crossing)
            oDispData.projects_thru_crossing = False
            self.m_logger.WriteLine4("\t\t\tThe new ProjectsThruCrossing is: {0}", oDispData.projects_thru_crossing)
            Assert.assertEqual(False, oDispData.projects_thru_crossing)
            oDispData.projects_thru_crossing = True
            self.m_logger.WriteLine4("\t\t\tThe new ProjectsThruCrossing is: {0}", oDispData.projects_thru_crossing)
            Assert.assertEqual(True, oDispData.projects_thru_crossing)
            # AltCrossingSides (ALTITUDE_CROSSING_ONE_SIDE)
            self.m_logger.WriteLine6("\t\t\tThe current AltCrossingSides is: {0}", oDispData.altitude_crossing_sides)
            oDispData.altitude_crossing_sides = SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_ONE_SIDE
            self.m_logger.WriteLine6("\t\t\tThe new AltCrossingSides is: {0}", oDispData.altitude_crossing_sides)
            Assert.assertEqual(
                SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_ONE_SIDE, oDispData.altitude_crossing_sides
            )
            # AltCrossingSides (ALTITUDE_CROSSING_BOTH_SIDES)
            self.m_logger.WriteLine6("\t\t\tThe current AltCrossingSides is: {0}", oDispData.altitude_crossing_sides)
            oDispData.altitude_crossing_sides = SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_BOTH_SIDES
            self.m_logger.WriteLine6("\t\t\tThe new AltCrossingSides is: {0}", oDispData.altitude_crossing_sides)
            Assert.assertEqual(
                SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_BOTH_SIDES, oDispData.altitude_crossing_sides
            )
            # AltCrossingSides (ALTITUDE_CROSSING_UNKNOWN)
            with pytest.raises(Exception):
                oDispData.altitude_crossing_sides = SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_UNKNOWN
            # Direction (DIRECTION_EITHER)
            self.m_logger.WriteLine6("\t\t\tThe current Direction is: {0}", oDispData.direction)
            oDispData.direction = SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_EITHER
            self.m_logger.WriteLine6("\t\t\tThe new Direction is: {0}", oDispData.direction)
            Assert.assertEqual(SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_EITHER, oDispData.direction)
            # Direction (DIRECTION_INSIDE_OUT)
            self.m_logger.WriteLine6("\t\t\tThe current Direction is: {0}", oDispData.direction)
            oDispData.direction = SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_INSIDE_OUT
            self.m_logger.WriteLine6("\t\t\tThe new Direction is: {0}", oDispData.direction)
            Assert.assertEqual(SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_INSIDE_OUT, oDispData.direction)
            # Direction (DIRECTION_OUTSIDE_IN)
            self.m_logger.WriteLine6("\t\t\tThe current Direction is: {0}", oDispData.direction)
            oDispData.direction = SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_OUTSIDE_IN
            self.m_logger.WriteLine6("\t\t\tThe new Direction is: {0}", oDispData.direction)
            Assert.assertEqual(SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_OUTSIDE_IN, oDispData.direction)
            # Direction (DIRECTION_UNKNOWN)
            with pytest.raises(Exception):
                oDispData.direction = SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_UNKNOWN

        # restore DistanceUnit
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\t\tThe restored DistanceUnit format is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region DisplayTimes
    def DisplayTimes(self):
        self.m_logger.WriteLine("----- THE DISPLAY TIMES TEST ----- BEGIN -----")
        oHelper = DisplayTimesHelper(self.m_oRoot)
        oHelper.Run(IDisplayTime(self.m_oSensor))
        self.m_logger.WriteLine("----- THE DISPLAY TIMES TEST ----- END -----")

    # endregion

    # region StarsInFOV
    def StarsInFOV(self):
        self.m_logger.WriteLine("----- THE StarsInFOV TEST ----- BEGIN -----")
        StarColl: "CelestialBodyCollection" = self.m_oSensor.get_stars_in_fov(0.0)

        # BUG58418 - verify that calling this with time before object time does not crash.
        StarColl = self.m_oSensor.get_stars_in_fov(-100.0)

        self.m_logger.WriteLine("----- THE StarsInFOV TEST ----- END -----")

    # endregion

    # region VO
    def VO(self):
        self.m_logger.WriteLine("----- THE VO TEST ----- BEGIN -----")
        originalType: "SENSOR_POINTING" = self.m_oSensor.pointing_type
        # System.Windows.Forms.MessageBox.Show(m_oSensor.PointingType.ToString());
        # VO
        oVO: "SensorGraphics3D" = self.m_oSensor.graphics_3d
        Assert.assertIsNotNone(oVO)
        # BoresightMarkerVisible
        self.m_logger.WriteLine4("\tThe current BoresightMarkerVisible flag is: {0}", oVO.boresight_marker_visible)
        oVO.boresight_marker_visible = True
        self.m_logger.WriteLine4("\tThe new BoresightMarkerVisible flag is: {0}", oVO.boresight_marker_visible)
        Assert.assertEqual(True, oVO.boresight_marker_visible)
        oVO.boresight_marker_visible = False
        self.m_logger.WriteLine4("\tThe new BoresightMarkerVisible flag is: {0}", oVO.boresight_marker_visible)
        Assert.assertEqual(False, oVO.boresight_marker_visible)
        # RadialLinesVisible
        self.m_logger.WriteLine4("\tThe current RadialLinesVisible flag is: {0}", oVO.radial_lines_visible)
        oVO.radial_lines_visible = True
        self.m_logger.WriteLine4("\tThe new RadialLinesVisible flag is: {0}", oVO.radial_lines_visible)
        Assert.assertEqual(True, oVO.radial_lines_visible)
        oVO.radial_lines_visible = False
        self.m_logger.WriteLine4("\tThe new RadialLinesVisible flag is: {0}", oVO.radial_lines_visible)
        Assert.assertEqual(False, oVO.radial_lines_visible)
        # TranslucentLinesVisible
        self.m_logger.WriteLine4("\tThe current TranslucencyLinesVisible flag is: {0}", oVO.translucent_lines_visible)
        oVO.translucent_lines_visible = True
        self.m_logger.WriteLine4("\tThe new TranslucencyLinesVisible flag is: {0}", oVO.translucent_lines_visible)
        Assert.assertEqual(True, oVO.translucent_lines_visible)
        oVO.translucent_lines_visible = False
        self.m_logger.WriteLine4("\tThe new TranslucencyLinesVisible flag is: {0}", oVO.translucent_lines_visible)
        Assert.assertEqual(False, oVO.translucent_lines_visible)
        # PercentTranslucency
        self.m_logger.WriteLine6("\tThe current PercentTranslucency is: {0}", oVO.percent_translucency)
        oVO.percent_translucency = 12.3456789
        self.m_logger.WriteLine6("\tThe new PercentTranslucency is: {0}", oVO.percent_translucency)
        Assert.assertEqual(12.3456789, oVO.percent_translucency)
        with pytest.raises(Exception):
            oVO.percent_translucency = -123.456
        # FillVisible
        self.m_logger.WriteLine4("\tThe current FillVisible flag is: {0}", oVO.fill_visible)
        oVO.fill_visible = False
        self.m_logger.WriteLine4("\tThe new FillVisible flag is: {0}", oVO.fill_visible)
        Assert.assertEqual(False, oVO.fill_visible)
        with pytest.raises(Exception):
            oVO.fill_translucency = 12.3456
        oVO.fill_visible = True
        self.m_logger.WriteLine4("\tThe new FillVisible flag is: {0}", oVO.fill_visible)
        Assert.assertEqual(True, oVO.fill_visible)
        # FillTranslucency
        self.m_logger.WriteLine6("\tThe current FillTranslucency is: {0}", oVO.fill_translucency)
        oVO.fill_translucency = 98.7654321
        self.m_logger.WriteLine6("\tThe new FillTranslucency is: {0}", oVO.fill_translucency)
        Assert.assertAlmostEqual(98.7654321, oVO.fill_translucency, delta=1e-08)
        with pytest.raises(Exception):
            oVO.fill_translucency = -123.456
        # FillResolution
        self.m_logger.WriteLine6("\tThe current FillResolution is: {0}", oVO.fill_resolution)
        oVO.fill_resolution = 98.7654321
        self.m_logger.WriteLine6("\tThe new FillResolution is: {0}", oVO.fill_resolution)
        Assert.assertAlmostEqual(98.7654321, oVO.fill_resolution, delta=1e-08)
        with pytest.raises(Exception):
            oVO.fill_resolution = -123.456

        # ProjectionType(PROJECTION_EARTH_INTERSECTIONS)
        self.m_logger.WriteLine6("\tThe current ProjectionType is: {0}", oVO.projection_type)
        oVO.projection_type = SENSOR_GRAPHICS_3D_PROJECTION_TYPE.PROJECTION_EARTH_INTERSECTIONS
        self.m_logger.WriteLine6("\tThe new ProjectionType is: {0}", oVO.projection_type)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PROJECTION_TYPE.PROJECTION_EARTH_INTERSECTIONS, oVO.projection_type)
        # ProjectionType(PROJECTION_ALL_INTERSECTIONS)
        oVO.projection_type = SENSOR_GRAPHICS_3D_PROJECTION_TYPE.PROJECTION_ALL_INTERSECTIONS
        self.m_logger.WriteLine6("\tThe new ProjectionType is: {0}", oVO.projection_type)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PROJECTION_TYPE.PROJECTION_ALL_INTERSECTIONS, oVO.projection_type)
        # ProjectionType(PROJECTION_NONE)
        oVO.projection_type = SENSOR_GRAPHICS_3D_PROJECTION_TYPE.PROJECTION_NONE
        self.m_logger.WriteLine6("\tThe new ProjectionType is: {0}", oVO.projection_type)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PROJECTION_TYPE.PROJECTION_NONE, oVO.projection_type)
        # EnableConstExtLength
        self.m_logger.WriteLine4("\tThe current EnableConstExtLength flag is: {0}", oVO.enable_const_ext_length)
        oVO.enable_const_ext_length = False
        self.m_logger.WriteLine4("\tThe new EnableConstExtLength flag is: {0}", oVO.enable_const_ext_length)
        Assert.assertEqual(False, oVO.enable_const_ext_length)
        oVO.enable_const_ext_length = True
        self.m_logger.WriteLine4("\tThe new EnableConstExtLength flag is: {0}", oVO.enable_const_ext_length)
        Assert.assertEqual(True, oVO.enable_const_ext_length)
        # EnableRangeConstraint
        self.m_logger.WriteLine4("\tThe current EnableRangeConstraint flag is: {0}", oVO.enable_range_constraint)
        oVO.enable_range_constraint = True
        self.m_logger.WriteLine4("\tThe new EnableRangeConstraint flag is: {0}", oVO.enable_range_constraint)
        Assert.assertEqual(True, oVO.enable_const_ext_length)
        oVO.enable_range_constraint = False
        self.m_logger.WriteLine4("\tThe new EnableRangeConstraint flag is: {0}", oVO.enable_range_constraint)
        Assert.assertEqual(False, oVO.enable_range_constraint)
        # set DistanceUnit
        strDistanceUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit format is: {0}", strDistanceUnit)
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", "m")
        self.m_logger.WriteLine5(
            "\tThe new DistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"),
        )
        Assert.assertEqual("m", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))
        # System.Windows.Forms.MessageBox.Show("Z");
        # OptimizeVisualAppearance is now deprecated
        # Don't allow set because will always set "AtCenter" since
        # always drawing relative to eye.
        # see CL260100, AgSn3dAttr.cpp, method lAgSn3DSetVisAppear()

        # InheritFrom2D
        self.m_logger.WriteLine6("\tThe current InheritFrom2D is: {0}", oVO.inherit_from_2d)
        oVO.inherit_from_2d = SENSOR_GRAPHICS_3D_INHERIT_FROM_2D.EXTENT_ONLY
        self.m_logger.WriteLine6("\tThe new InheritFrom2D is: {0}", oVO.inherit_from_2d)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_INHERIT_FROM_2D.EXTENT_ONLY, oVO.inherit_from_2d)
        oVO.inherit_from_2d = SENSOR_GRAPHICS_3D_INHERIT_FROM_2D.NO
        self.m_logger.WriteLine6("\tThe new InheritFrom2D is: {0}", oVO.inherit_from_2d)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_INHERIT_FROM_2D.NO, oVO.inherit_from_2d)
        oVO.inherit_from_2d = SENSOR_GRAPHICS_3D_INHERIT_FROM_2D.YES
        self.m_logger.WriteLine6("\tThe new InheritFrom2D is: {0}", oVO.inherit_from_2d)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_INHERIT_FROM_2D.YES, oVO.inherit_from_2d)
        with pytest.raises(Exception):
            oVO.inherit_from_2d = SENSOR_GRAPHICS_3D_INHERIT_FROM_2D.UNKNOWN
        # System.Windows.Forms.MessageBox.Show("A");
        senObj: "IStkObject" = IStkObject(self.m_oSensor)
        if not (clr.Is(senObj.parent, Missile)):
            # SpaceProjection
            oVO.projection_time_dependency = SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE.CONSTANT
            Assert.assertEqual(
                SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE.CONSTANT, oVO.projection_time_dependency
            )

            oVO.space_projection = 0.0
            Assert.assertEqual(0.0, oVO.space_projection)
            oVO.space_projection = 1000000000.0
            Assert.assertEqual(1000000000.0, oVO.space_projection)
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                oVO.space_projection = -123.456
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                oVO.space_projection = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0

            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                oVO.targeting = 5000.0
            oSPCollection: "SensorGraphics3DSpaceProjectionCollection" = oVO.space_projection_intervals
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only attribute")):
                oSPCollection.add()
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only attribute")):
                oSPCollection.remove_all()
            with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
                oSPCollection.remove_at(0)

            # Targeting
            # System.Windows.Forms.MessageBox.Show("X");
            self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_TARGETED)
            # System.Windows.Forms.MessageBox.Show(m_oSensor.PointingType.ToString());
            oVO.targeting = 5000.0
            Assert.assertEqual(5000.0, oVO.targeting)
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                oVO.space_projection = 5000.0
            oTPCollection: "SensorGraphics3DTargetProjectionCollection" = oVO.target_projection_intervals
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oTPCollection.add()
            with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
                oTPCollection.remove_all()
            with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
                oSPCollection.remove_at(0)
            self.m_oSensor.set_pointing_type(originalType)
            # System.Windows.Forms.MessageBox.Show(m_oSensor.PointingType.ToString());
            # Test the space & target projection
            # IsTargeted
            self.m_logger.WriteLine4("\tThe current IsTargeted is: {0}", oVO.is_targeted)

            # SpaceProjectionIntervals
            oVO.projection_time_dependency = SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE.TIME_VARYING
            Assert.assertEqual(
                SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE.TIME_VARYING, oVO.projection_time_dependency
            )

            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                oVO.space_projection = 123.456

            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only attribute")):
                oTPCollection.add()
            with pytest.raises(Exception, match=RegexSubstringMatch("Cannot modify read-only attribute")):
                oTPCollection.remove_all()
            with pytest.raises(Exception, match=RegexSubstringMatch("One or more arguments are invalid")):
                oSPCollection.remove_at(0)
            with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
                oVO.space_projection = 5000.0

            oSPCollection = oVO.space_projection_intervals
            Assert.assertIsNotNone(oSPCollection)
            # RemoveAll
            oSPCollection.remove_all()
            # Count
            self.m_logger.WriteLine3(
                "\tThe current Space Projection Intervals collection contains: {0} elements", oSPCollection.count
            )
            Assert.assertEqual(0, oSPCollection.count)
            # Add 1
            oProjection: "SensorGraphics3DProjectionElement" = oSPCollection.add()
            Assert.assertIsNotNone(oProjection)
            self.m_logger.WriteLine3(
                "\tThe new Space Projection Intervals collection contains: {0} elements", oSPCollection.count
            )
            Assert.assertEqual(1, oSPCollection.count)

            # _NewEnum
            oPElement: "SensorGraphics3DProjectionElement"

            # _NewEnum
            for oPElement in oSPCollection:
                self.m_logger.WriteLine7("\t\tElement: Distance = {0}, Time = {1}", oPElement.distance, oPElement.time)

            # Distance
            self.m_logger.WriteLine6("\tThe current Distance is: {0}", oProjection.distance)
            oProjection.distance = 1000
            self.m_logger.WriteLine6("\tThe new Distance is: {0}", oProjection.distance)
            Assert.assertAlmostEqual(1000, oProjection.distance, delta=1e-05)
            with pytest.raises(Exception):
                oProjection.distance = -1000
            # Time
            self.m_logger.WriteLine6("\tThe current Time is: {0}", oProjection.time)
            oProjection.time = "12 Jun 2005 12:34:56.789"
            self.m_logger.WriteLine6("\tThe new Time is: {0}", oProjection.time)
            Assert.assertEqual("12 Jun 2005 12:34:56.789", oProjection.time)
            with pytest.raises(Exception):
                oProjection.time = "Some string"
            # Add 2
            oProjection = oSPCollection.add()
            Assert.assertIsNotNone(oProjection)
            self.m_logger.WriteLine3(
                "\tThe new Space Projection Intervals collection contains: {0} elements", oSPCollection.count
            )
            Assert.assertEqual(2, oSPCollection.count)

            iIndex: int = 0
            while iIndex < oSPCollection.count:
                self.m_logger.WriteLine8(
                    "\t\tElement {0}: Distance = {1}, Time = {2}",
                    iIndex,
                    oSPCollection[iIndex].distance,
                    oSPCollection[iIndex].time,
                )

                iIndex += 1

            # RemoveAt
            oSPCollection.remove_at(1)
            Assert.assertEqual(1, oSPCollection.count)
            self.m_logger.WriteLine3(
                "\tThe new Space Projection Intervals collection contains: {0} elements", oSPCollection.count
            )
            with pytest.raises(Exception):
                oSPCollection.remove_at(23)

            iIndex: int = 0
            while iIndex < oSPCollection.count:
                self.m_logger.WriteLine8(
                    "\t\tElement {0}: Distance = {1}, Time = {2}",
                    iIndex,
                    oSPCollection[iIndex].distance,
                    oSPCollection[iIndex].time,
                )

                iIndex += 1

            oSPCollection.remove_all()

            # TargetProjectionIntervals
            self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_TARGETED)
            # System.Windows.Forms.MessageBox.Show(m_oSensor.PointingType.ToString());

            with pytest.raises(Exception):
                oSPCollection.add()
            with pytest.raises(Exception):
                oSPCollection.remove_all()
            with pytest.raises(Exception):
                oSPCollection.remove_at(0)
            with pytest.raises(Exception):
                oVO.targeting = 5000.0

            oTPCollection = oVO.target_projection_intervals
            Assert.assertIsNotNone(oTPCollection)
            # RemoveAll
            oTPCollection.remove_all()
            self.m_logger.WriteLine3(
                "\tThe current Target Projection Intervals collection contains: {0} elements", oTPCollection.count
            )
            # Add 1
            oProjection = oTPCollection.add()
            Assert.assertIsNotNone(oProjection)
            self.m_logger.WriteLine3(
                "\tThe new Target Projection Intervals collection contains: {0} elements", oTPCollection.count
            )
            Assert.assertEqual(1, oTPCollection.count)
            # _NewEnum
            oPElement: "SensorGraphics3DProjectionElement"
            # _NewEnum
            for oPElement in oTPCollection:
                self.m_logger.WriteLine7("\t\tElement: Distance = {0}, Time = {1}", oPElement.distance, oPElement.time)

            # Distance
            self.m_logger.WriteLine6("\tThe current Distance is: {0}", oProjection.distance)
            oProjection.distance = 3000
            self.m_logger.WriteLine6("\tThe new Distance is: {0}", oProjection.distance)
            Assert.assertAlmostEqual(3000, oProjection.distance, delta=1e-05)
            oProjection.distance = -3000
            self.m_logger.WriteLine6("\tThe new Distance is: {0}", oProjection.distance)
            Assert.assertAlmostEqual(-3000, oProjection.distance, delta=1e-05)
            with pytest.raises(Exception):
                oProjection.distance = (
                    -10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
                )
            # Time
            self.m_logger.WriteLine6("\tThe current Time is: {0}", oProjection.time)
            oProjection.time = "13 Jun 2005 23:45:01.234"
            self.m_logger.WriteLine6("\tThe new Time is: {0}", oProjection.time)
            Assert.assertEqual("13 Jun 2005 23:45:01.234", oProjection.time)
            with pytest.raises(Exception):
                oProjection.time = "Some string"
            # Add 2
            oProjection = oTPCollection.add()
            Assert.assertIsNotNone(oProjection)
            self.m_logger.WriteLine3(
                "\tThe new Target Projection Intervals collection contains: {0} elements", oTPCollection.count
            )
            Assert.assertEqual(2, oTPCollection.count)

            iIndex: int = 0
            while iIndex < oTPCollection.count:
                self.m_logger.WriteLine8(
                    "\t\tElement {0}: Distance = {1}, Time = {2}",
                    iIndex,
                    oTPCollection[iIndex].distance,
                    oTPCollection[iIndex].time,
                )

                iIndex += 1

            # RemoveAt
            oTPCollection.remove_at(1)
            Assert.assertEqual(1, oTPCollection.count)
            with pytest.raises(Exception):
                oTPCollection.remove_at(23)
            # Item
            self.m_logger.WriteLine3(
                "\tThe new Target Projection Intervals collection contains: {0} elements", oTPCollection.count
            )

            iIndex: int = 0
            while iIndex < oTPCollection.count:
                self.m_logger.WriteLine8(
                    "\t\tElement {0}: Distance = {1}, Time = {2}",
                    iIndex,
                    oTPCollection[iIndex].distance,
                    oTPCollection[iIndex].time,
                )

                iIndex += 1

            oTPCollection.remove_all()
            self.m_oSensor.set_pointing_type(originalType)
            # System.Windows.Forms.MessageBox.Show(m_oSensor.PointingType.ToString());
            oVO.projection_time_dependency = SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE.CONSTANT

        oVO.persist_projected_lines_in_space = True
        Assert.assertTrue(oVO.persist_projected_lines_in_space)
        oVO.persist_projected_lines_in_space = False
        Assert.assertFalse(oVO.persist_projected_lines_in_space)

        oVO.persist_partial_central_body_intersection_lines = False
        Assert.assertFalse(oVO.persist_partial_central_body_intersection_lines)
        oVO.persist_partial_central_body_intersection_lines = True
        Assert.assertTrue(oVO.persist_partial_central_body_intersection_lines)

        # Pulse
        self.VOPulse(oVO.pulse)
        # VertexOffset
        self.VOVertexOffset(oVO.vertex_offset)

        # restore DistanceUnit
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\tThe restored DistanceUnit format is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))
        self.m_logger.WriteLine("----- THE VO TEST ----- END -----")

    # endregion

    # region VOPulse
    def VOPulse(self, oPulse: "SensorGraphics3DPulse"):
        Assert.assertIsNotNone(oPulse)
        self.m_logger.WriteLine("\tVOPulse test:")
        # set FrequencyUnit
        strFreqUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("FrequencyUnit")
        self.m_logger.WriteLine5("\t\tThe current FrequencyUnit format is: {0}", strFreqUnit)
        self.m_oRoot.unit_preferences.set_current_unit("FrequencyUnit", "Hz")
        self.m_logger.WriteLine5(
            "\t\tThe new FrequencyUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("FrequencyUnit"),
        )
        Assert.assertEqual("Hz", self.m_oRoot.unit_preferences.get_current_unit_abbrv("FrequencyUnit"))
        # PulseVisible (false)
        self.m_logger.WriteLine4("\t\tThe current PulseVisible flag is: {0}", oPulse.pulse_visible)
        oPulse.pulse_visible = False
        self.m_logger.WriteLine4("\t\tThe new PulseVisible flag is: {0}", oPulse.pulse_visible)
        Assert.assertEqual(False, oPulse.pulse_visible)
        # Amplitude (readonly)
        with pytest.raises(Exception):
            oPulse.amplitude = 0.123456
        # Length (readonly)
        with pytest.raises(Exception):
            oPulse.length = 123.456
        # Style (readonly)
        with pytest.raises(Exception):
            oPulse.style = SENSOR_GRAPHICS_3D_PULSE_STYLE.PULSE_STYLE_POSITION_BOX
        # EnableSmooth (readonly)
        with pytest.raises(Exception):
            oPulse.enable_smooth = True
        # PreselFreq (readonly)
        with pytest.raises(Exception):
            oPulse.presel_freq = SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_FAST
        # FreqValue (readonly)
        with pytest.raises(Exception):
            oPulse.freq_value = 12.34
        # FreqReverseDir (readonly)
        with pytest.raises(Exception):
            oPulse.freq_reverse_direction = True
        # ResetToDefaults (readonly)
        with pytest.raises(Exception):
            oPulse.reset_to_defaults()
        # PulseVisible (true)
        oPulse.pulse_visible = True
        self.m_logger.WriteLine4("\t\tThe new PulseVisible flag is: {0}", oPulse.pulse_visible)
        Assert.assertEqual(True, oPulse.pulse_visible)
        # Amplitude
        self.m_logger.WriteLine6("\t\t\tThe current Amplitude is: {0}", oPulse.amplitude)
        oPulse.amplitude = 0.123456789
        self.m_logger.WriteLine6("\t\t\tThe new Amplitude is: {0}", oPulse.amplitude)
        Assert.assertEqual(0.123456789, oPulse.amplitude)
        with pytest.raises(Exception):
            oPulse.amplitude = 1.23456789
        # Length
        self.m_logger.WriteLine6("\t\t\tThe current Length is: {0}", oPulse.length)
        oPulse.length = 987.654321
        self.m_logger.WriteLine6("\t\t\tThe new Length is: {0}", oPulse.length)
        Assert.assertEqual(987.654321, oPulse.length)
        with pytest.raises(Exception):
            oPulse.length = -1.23456789
        # Style
        self.m_logger.WriteLine6("\t\t\tThe current Style is: {0}", oPulse.style)
        oPulse.style = SENSOR_GRAPHICS_3D_PULSE_STYLE.PULSE_STYLE_NEG_SINE
        self.m_logger.WriteLine6("\t\t\tThe new Style is: {0}", oPulse.style)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PULSE_STYLE.PULSE_STYLE_NEG_SINE, oPulse.style)
        # EnableSmooth
        self.m_logger.WriteLine4("\t\t\tThe current EnableSmooth is: {0}", oPulse.enable_smooth)
        oPulse.enable_smooth = True
        self.m_logger.WriteLine4("\t\t\tThe new EnableSmooth is: {0}", oPulse.enable_smooth)
        Assert.assertEqual(True, oPulse.enable_smooth)
        # PreselFreq (PULSE_FREQUENCY_SLOW)
        self.m_logger.WriteLine6("\t\t\tThe current FreqValue is: {0}", oPulse.freq_value)
        self.m_logger.WriteLine6("\t\t\tThe current PreselFreq is: {0}", oPulse.presel_freq)
        oPulse.presel_freq = SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_SLOW
        self.m_logger.WriteLine6("\t\t\tThe new FreqValue is: {0}", oPulse.freq_value)
        self.m_logger.WriteLine6("\t\t\tThe new PreselFreq is: {0}", oPulse.presel_freq)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_SLOW, oPulse.presel_freq)
        # PreselFreq (PULSE_FREQUENCY_MEDIUM)
        oPulse.presel_freq = SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_MEDIUM
        self.m_logger.WriteLine6("\t\t\tThe new FreqValue is: {0}", oPulse.freq_value)
        self.m_logger.WriteLine6("\t\t\tThe new PreselFreq is: {0}", oPulse.presel_freq)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_MEDIUM, oPulse.presel_freq)
        # PreselFreq (PULSE_FREQUENCY_FAST)
        oPulse.presel_freq = SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_FAST
        self.m_logger.WriteLine6("\t\t\tThe new FreqValue is: {0}", oPulse.freq_value)
        self.m_logger.WriteLine6("\t\t\tThe new PreselFreq is: {0}", oPulse.presel_freq)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_FAST, oPulse.presel_freq)
        # PreselFreq (PULSE_FREQUENCY_CUSTOM)
        oPulse.presel_freq = SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_CUSTOM
        self.m_logger.WriteLine6("\t\t\tThe new FreqValue is: {0}", oPulse.freq_value)
        self.m_logger.WriteLine6("\t\t\tThe new PreselFreq is: {0}", oPulse.presel_freq)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_FAST, oPulse.presel_freq)
        # FreqValue
        oPulse.freq_value = 12.3456789
        self.m_logger.WriteLine6("\t\t\tThe new FreqValue is: {0}", oPulse.freq_value)
        self.m_logger.WriteLine6("\t\t\tThe new PreselFreq is: {0}", oPulse.presel_freq)
        Assert.assertEqual(12.3456789, oPulse.freq_value)
        Assert.assertEqual(SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET.PULSE_FREQUENCY_CUSTOM, oPulse.presel_freq)
        with pytest.raises(Exception):
            oPulse.freq_value = -1.23456789
        # FreqReverseDir
        self.m_logger.WriteLine4("\t\t\tThe current FreqReverseDir is: {0}", oPulse.freq_reverse_direction)
        oPulse.freq_reverse_direction = True
        self.m_logger.WriteLine4("\t\t\tThe new FreqReverseDir is: {0}", oPulse.freq_reverse_direction)
        Assert.assertEqual(True, oPulse.freq_reverse_direction)
        # ResetToDefaults
        oPulse.reset_to_defaults()
        # restore FrequencyUnit
        self.m_oRoot.unit_preferences.set_current_unit("FrequencyUnit", strFreqUnit)
        self.m_logger.WriteLine5("\t\tThe restored FrequencyUnit format is: {0}", strFreqUnit)
        Assert.assertEqual(strFreqUnit, self.m_oRoot.unit_preferences.get_current_unit_abbrv("FrequencyUnit"))

    # endregion

    # region VOVertexOffset
    def VOVertexOffset(self, oOffset: "SensorGraphics3DOffset"):
        Assert.assertIsNotNone(oOffset)
        self.m_logger.WriteLine("\tVOVertexOffset test:")
        # AvailableAttachPoints
        arPoints = oOffset.available_attach_points
        self.m_logger.WriteLine3("\t\tThe AvailableAttachPoints array contains: {0} elements.", Array.Length(arPoints))

        iIndex: int = 0
        while iIndex < Array.Length(arPoints):
            self.m_logger.WriteLine7("\t\t\tElement {0}: {1}", iIndex, arPoints[iIndex])

            iIndex += 1

        # InheritFromParentObj (true)
        self.m_logger.WriteLine4("\t\tThe current InheritFromParentObj flag is: {0}", oOffset.inherit_from_parent_obj)
        oOffset.inherit_from_parent_obj = True
        self.m_logger.WriteLine4("\t\tThe new InheritFromParentObj flag is: {0}", oOffset.inherit_from_parent_obj)
        Assert.assertEqual(True, oOffset.inherit_from_parent_obj)
        # EnableTranslational (readonly)
        with pytest.raises(Exception):
            oOffset.enable_translational = True
        # X (readonly)
        with pytest.raises(Exception):
            oOffset.x = 123.456
        # Y (readonly)
        with pytest.raises(Exception):
            oOffset.y = 123.456
        # Z (readonly)
        with pytest.raises(Exception):
            oOffset.z = 123.456
        # SENSOR_RADIUS (readonly)
        with pytest.raises(Exception):
            oOffset.set_axis_offset_value(AXIS_OFFSET.SENSOR_RADIUS, 123.456)
        # BORESIGHT_OFFSET (readonly)
        with pytest.raises(Exception):
            oOffset.set_axis_offset_value(AXIS_OFFSET.BORESIGHT_OFFSET, 123.456)
        # EnableAttachPoint (readonly)
        with pytest.raises(Exception):
            oOffset.enable_attach_point = True
        if Array.Length(arPoints) > 0:
            with pytest.raises(Exception):
                oOffset.attach_point_name = str(arPoints[0])

        # InheritFromParentObj {false)
        oOffset.inherit_from_parent_obj = False
        self.m_logger.WriteLine4("\t\tThe new InheritFromParentObj flag is: {0}", oOffset.inherit_from_parent_obj)
        Assert.assertEqual(False, oOffset.inherit_from_parent_obj)
        # EnableTranslational (false)
        self.m_logger.WriteLine4("\t\t\tThe current EnableTranslational flag is: {0}", oOffset.enable_translational)
        oOffset.enable_translational = False
        self.m_logger.WriteLine4("\t\t\tThe new EnableTranslational flag is: {0}", oOffset.enable_translational)
        Assert.assertEqual(False, oOffset.enable_translational)
        # EnableAttachPoint (false)
        self.m_logger.WriteLine4("\t\t\tThe current EnableAttachPoint flag is: {0}", oOffset.enable_attach_point)
        oOffset.enable_attach_point = False
        self.m_logger.WriteLine4("\t\t\tThe new EnableAttachPoint flag is: {0}", oOffset.enable_attach_point)
        Assert.assertEqual(False, oOffset.enable_attach_point)
        # X (readonly)
        with pytest.raises(Exception):
            oOffset.x = 123.456
        # Y (readonly)
        with pytest.raises(Exception):
            oOffset.y = 123.456
        # Z (readonly)
        with pytest.raises(Exception):
            oOffset.z = 123.456
        # SENSOR_RADIUS (readonly)
        with pytest.raises(Exception):
            oOffset.set_axis_offset_value(AXIS_OFFSET.SENSOR_RADIUS, 123.456)
        # BORESIGHT_OFFSET (readonly)
        with pytest.raises(Exception):
            oOffset.set_axis_offset_value(AXIS_OFFSET.BORESIGHT_OFFSET, 123.456)
        if Array.Length(arPoints) > 0:
            with pytest.raises(Exception):
                oOffset.attach_point_name = str(arPoints[0])

        # EnableTranslational (true)
        oOffset.enable_translational = True
        self.m_logger.WriteLine4("\t\t\tThe new EnableTranslational flag is: {0}", oOffset.enable_translational)
        Assert.assertEqual(True, oOffset.enable_translational)
        # X
        self.m_logger.WriteLine6("\t\t\t\tThe current X is: {0}", oOffset.x)
        oOffset.x = 12345.6789
        self.m_logger.WriteLine6("\t\t\t\tThe new X is: {0}", oOffset.x)
        Assert.assertEqual(12345.6789, oOffset.x)
        with pytest.raises(Exception):
            oOffset.x = 100000000000000000000000.0
        # Y
        self.m_logger.WriteLine6("\t\t\t\tThe current Y is: {0}", oOffset.y)
        oOffset.y = 12345.6789
        self.m_logger.WriteLine6("\t\t\t\tThe new Y is: {0}", oOffset.y)
        Assert.assertEqual(12345.6789, oOffset.y)
        with pytest.raises(Exception):
            oOffset.y = 100000000000000000000000.0
        # Z
        self.m_logger.WriteLine6("\t\t\t\tThe current Z is: {0}", oOffset.z)
        oOffset.z = 12345.6789
        self.m_logger.WriteLine6("\t\t\t\tThe new Z is: {0}", oOffset.z)
        Assert.assertEqual(12345.6789, oOffset.z)
        with pytest.raises(Exception):
            oOffset.z = 100000000000000000000000.0
        # set SmallDistanceUnit
        strSmallDistanceUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit")
        self.m_logger.WriteLine5("\t\t\t\tThe current SmallDistanceUnit is: {0}", strSmallDistanceUnit)
        self.m_oRoot.unit_preferences.set_current_unit("SmallDistanceUnit", "mm")
        self.m_logger.WriteLine5(
            "\t\t\t\tThe new SmallDistanceUnit is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"),
        )
        Assert.assertEqual("mm", self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"))
        # GetAxisOffsetValue (SENSOR_RADIUS)
        self.m_logger.WriteLine6(
            "\t\t\t\tThe current SENSOR_RADIUS is: {0}", oOffset.get_axis_offset_value(AXIS_OFFSET.SENSOR_RADIUS)
        )
        # SetAxisOffsetValue (SENSOR_RADIUS)
        oOffset.set_axis_offset_value(AXIS_OFFSET.SENSOR_RADIUS, 12345678.9)
        self.m_logger.WriteLine6(
            "\t\t\t\tThe new SENSOR_RADIUS is: {0}", oOffset.get_axis_offset_value(AXIS_OFFSET.SENSOR_RADIUS)
        )
        Assert.assertEqual(12345678.9, oOffset.get_axis_offset_value(AXIS_OFFSET.SENSOR_RADIUS))
        with pytest.raises(Exception):
            oOffset.set_axis_offset_value(AXIS_OFFSET.SENSOR_RADIUS, 100000000000000000000000.0)
        # GetAxisOffsetValue (BORESIGHT_OFFSET)
        self.m_logger.WriteLine6(
            "\t\t\t\tThe current Boresight Offset is: {0}", oOffset.get_axis_offset_value(AXIS_OFFSET.BORESIGHT_OFFSET)
        )
        # SetAxisOffsetValue (BORESIGHT_OFFSET)
        oOffset.set_axis_offset_value(AXIS_OFFSET.BORESIGHT_OFFSET, 98765432.1)
        self.m_logger.WriteLine6(
            "\t\t\t\tThe new Boresight Offset is: {0}", oOffset.get_axis_offset_value(AXIS_OFFSET.BORESIGHT_OFFSET)
        )
        Assert.assertEqual(98765432.1, oOffset.get_axis_offset_value(AXIS_OFFSET.BORESIGHT_OFFSET))
        with pytest.raises(Exception):
            oOffset.set_axis_offset_value(AXIS_OFFSET.BORESIGHT_OFFSET, 100000000000000000000000.0)
        # restore SmallDistanceUnit
        self.m_oRoot.unit_preferences.set_current_unit("SmallDistanceUnit", strSmallDistanceUnit)
        self.m_logger.WriteLine5("\t\t\t\tThe restored SmallDistanceUnit is: {0}", strSmallDistanceUnit)
        Assert.assertEqual(
            strSmallDistanceUnit, self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit")
        )
        # EnableAttachPoint (true)
        oOffset.enable_attach_point = True
        self.m_logger.WriteLine4("\t\t\tThe new EnableAttachPoint flag is: {0}", oOffset.enable_attach_point)
        Assert.assertEqual(True, oOffset.enable_attach_point)
        # AttachPtName
        self.m_logger.WriteLine5("\t\t\t\tThe current AttachPtName is: {0}", oOffset.attach_point_name)
        if Array.Length(arPoints) > 0:
            iIndex: int = 0
            while iIndex < Array.Length(arPoints):
                strName: str = str(arPoints[iIndex])
                oOffset.attach_point_name = strName
                self.m_logger.WriteLine5("\t\t\t\tThe new AttachPtName is: {0}", oOffset.attach_point_name)
                Assert.assertEqual(strName, oOffset.attach_point_name)

                iIndex += 1

        with pytest.raises(Exception):
            oOffset.attach_point_name = "bla-bla-bla"

    # endregion

    # region VODataDisplay
    def VODataDisplay(self):
        # test VO DataDisplay
        oHelper = VODataDisplayHelper(self.m_oRoot)
        oHelper.Run(self.m_oSensor.graphics_3d.data_displays, False, False)

    # endregion

    # region VOVectors
    def VOVectors(self):
        oHelper = VOVectorsHelper(self.m_oRoot.unit_preferences, self.m_oRoot)
        oHelper.Run(self.m_oSensor.graphics_3d.vector, True)

    # endregion

    # region Swath
    def Swath(self, bShouldBeAvailable: bool):
        self.m_logger.WriteLine("----- THE SWATH TEST ----- BEGIN -----")

        bFound: bool = False
        oSwath: "Swath" = None
        try:
            oSwath = self.m_oSensor.swath
            bFound = True

        except Exception as e:
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        if (not bShouldBeAvailable) and bFound:
            Assert.fail("The Swath should not be available for this object!")

        if bShouldBeAvailable and (not bFound):
            Assert.fail("The Swath should be available for this object!")

        if (not bShouldBeAvailable) and (not bFound):
            self.m_logger.WriteLine("----- THE SWATH TEST ----- END -----")
            return

        # set DateFormat
        strDateFormat: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat")
        self.m_logger.WriteLine5("\tThe current DateFormat is: {0}", strDateFormat)
        self.m_oRoot.unit_preferences.set_current_unit("DateFormat", "DD/MM/YYYY")
        self.m_logger.WriteLine5(
            "\tThe new DateFormat is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat")
        )
        Assert.assertEqual("DD/MM/YYYY", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat"))

        # Enable (false)
        Assert.assertIsNotNone(oSwath)
        oSwath.enable = False
        Assert.assertFalse(oSwath.enable)

        # Color (readonly)
        with pytest.raises(Exception):
            oSwath.color = Colors.from_argb(16711680)
        # LineStyle (readonly)
        with pytest.raises(Exception):
            oSwath.line_style = LINE_STYLE.DASH_DOT
        # LineWidth (readonly)
        with pytest.raises(Exception):
            oSwath.line_width = LINE_WIDTH.WIDTH4

        # Enable (true)
        oSwath.enable = True
        self.m_logger.WriteLine4("\tThe new Enable flag is: {0}", oSwath.enable)
        Assert.assertTrue(oSwath.enable)

        # Color
        self.m_logger.WriteLine6("\t\tThe current Color is: {0}", oSwath.color)
        oSwath.color = Colors.from_argb(16711680)
        self.m_logger.WriteLine6("\t\tThe new Color is: {0}", oSwath.color)
        AssertEx.AreEqual(Colors.from_argb(16711680), oSwath.color)
        # LineStyle
        self.m_logger.WriteLine6("\t\tThe current LineStyle is: {0}", oSwath.line_style)
        oSwath.line_style = LINE_STYLE.LMS_DASH
        self.m_logger.WriteLine6("\t\tThe new LineStyle is: {0}", oSwath.line_style)
        Assert.assertEqual(LINE_STYLE.LMS_DASH, oSwath.line_style)
        # LineWidth
        self.m_logger.WriteLine6("\t\tThe current LineWidth is: {0}", oSwath.line_width)
        oSwath.line_width = LINE_WIDTH.WIDTH2
        self.m_logger.WriteLine6("\t\tThe new LineWidth is: {0}", oSwath.line_width)
        Assert.assertEqual(LINE_WIDTH.WIDTH2, oSwath.line_width)

        # TimeIntervalCount
        self.m_logger.WriteLine3("\t\tThe current number of Time Intervals is: {0}", oSwath.time_interval_count)
        Assert.assertEqual(0, oSwath.time_interval_count)
        # AddTimeInterval
        oSwath.add_time_interval("20/07/2005 11:22:33.000", "20/07/2005 11:22:36.000")
        Assert.assertEqual(1, oSwath.time_interval_count)
        oSwath.add_time_interval("22/07/2005 11:22:33.000", "22/07/2005 11:22:36.000")
        Assert.assertEqual(2, oSwath.time_interval_count)
        self.m_logger.WriteLine3("\t\tThe new number of Time Intervals is: {0}", oSwath.time_interval_count)
        # ToArray
        arIntervals = oSwath.to_array(0, -1)

        iIndex: int = 0
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

        with pytest.raises(Exception):
            oSwath.add_time_interval("22/07/2005 11:22:33.000", "22/07/2005 11:22:32.000")
        # GetTimeIntervalIndex
        nIndex: int = oSwath.get_time_interval_index("20/07/2005 11:22:33.000", "20/07/2005 11:22:36.000")
        with pytest.raises(Exception):
            oSwath.get_time_interval_index("25/07/2005 11:22:33.000", "26/07/2005 11:22:33.000")
        # ModifyTimeInterval
        oSwath.modify_time_interval(nIndex, "20/07/2005 22:33:11.000", "20/07/2005 22:33:18.000")
        self.m_logger.WriteLine3("\t\tThe new number of Time Intervals is: {0}", oSwath.time_interval_count)
        # ToArray
        arIntervals = oSwath.to_array(0, -1)

        iIndex: int = 0
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

        # RemoveTimeIntervalIndex
        oSwath.remove_time_interval_index(nIndex)
        self.m_logger.WriteLine3("\t\tThe new number of Time Intervals is: {0}", oSwath.time_interval_count)
        # ToArray
        arIntervals = oSwath.to_array(0, -1)

        iIndex: int = 0
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

        with pytest.raises(Exception):
            oSwath.remove_time_interval_index(12)
        # RemoveTimeInterval
        oSwath.remove_time_interval("22/07/2005 11:22:33.000", "22/07/2005 11:22:36.000")
        self.m_logger.WriteLine3("\t\tThe new number of Time Intervals is: {0}", oSwath.time_interval_count)
        # ToArray
        arIntervals = oSwath.to_array(0, -1)

        iIndex: int = 0
        while iIndex < len(arIntervals):
            self.m_logger.WriteLine8(
                "\t\t\tInterval {0}: StartTime = {1}, StopTime = {2}",
                iIndex,
                arIntervals[iIndex][0],
                arIntervals[iIndex][1],
            )

            iIndex += 1

        with pytest.raises(Exception):
            oSwath.remove_time_interval("22/07/2005 11:22:33.000", "23/07/2005 11:22:33.000")
        # RemoveAllIntervals
        oSwath.remove_all_intervals()
        self.m_logger.WriteLine3("\t\tThe new number of Time Intervals is: {0}", oSwath.time_interval_count)
        Assert.assertEqual(0, oSwath.time_interval_count)
        # restore DateFormat
        self.m_oRoot.unit_preferences.set_current_unit("DateFormat", strDateFormat)
        self.m_logger.WriteLine5(
            "\tThe restored DateFormat is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat")
        )
        Assert.assertEqual(strDateFormat, self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat"))

        # ----------------------------------
        # New swath properties
        # ----------------------------------
        oSwath.use_maximum_cone = True
        Assert.assertTrue(oSwath.use_maximum_cone)
        oSwath.use_maximum_cone = False
        Assert.assertFalse(oSwath.use_maximum_cone)
        oSwath.curvature_tolerance = 0.0
        Assert.assertEqual(0.0, oSwath.curvature_tolerance)
        oSwath.curvature_tolerance = 180
        Assert.assertEqual(180, oSwath.curvature_tolerance)
        oSwath.scattering_tolerance = 0.0
        Assert.assertEqual(0.0, oSwath.scattering_tolerance)
        oSwath.scattering_tolerance = 180
        Assert.assertEqual(180, oSwath.scattering_tolerance)
        oSwath.minimum_step = 0
        Assert.assertEqual(0, oSwath.minimum_step)
        oSwath.minimum_step = 9999999999
        Assert.assertAlmostEqual(9999999999, oSwath.minimum_step, delta=0.0)
        oSwath.maximum_step = 0
        Assert.assertEqual(0, oSwath.maximum_step)
        oSwath.maximum_step = 9999999999
        Assert.assertAlmostEqual(9999999999, oSwath.maximum_step, delta=0.0)

        oSwath.enable = False
        Assert.assertFalse(oSwath.enable)
        with pytest.raises(Exception):
            oSwath.maximum_step = 1
        with pytest.raises(Exception):
            oSwath.minimum_step = 1
        with pytest.raises(Exception):
            oSwath.scattering_tolerance = 1
        with pytest.raises(Exception):
            oSwath.use_maximum_cone = True
        with pytest.raises(Exception):
            oSwath.curvature_tolerance = 1

        self.m_logger.WriteLine("----- THE SWATH TEST ----- END -----")

    # endregion

    # region BasicRefraction
    def BasicRefraction(self):
        self.m_logger.WriteLine("----- BASIC REFRACTION TEST ----- BEGIN -----")
        #        #			 * UseRefractionInAccess can mutate and become read-only for objects        #			 * whose central body is different than the central body associated        #			 * with the refraction model. For example, the Mars-based receiver        #			 * will have the UseRefractionInAccess flag read-only for some        #			 * models. Right now, there is no easy way to tell when this        #			 * may happen. Perhaps, we should have the models expose a property        #			 * telling us if the model can be used.        #
        self.m_oSensor.use_refraction_in_access = True
        Assert.assertEqual(True, self.m_oSensor.use_refraction_in_access)
        self.m_oSensor.use_refraction_in_access = False
        Assert.assertEqual(False, self.m_oSensor.use_refraction_in_access)
        # Refraction
        self.m_logger.WriteLine6("\tThe current RefractionType is: {0}", self.m_oSensor.refraction)
        # RefractionSupportedTypes
        arTypes = self.m_oSensor.refraction_supported_types
        self.m_logger.WriteLine3("\tThe Sensor supports: {0} refraction types.", len(arTypes))
        Assert.assertEqual(3, len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "SENSOR_REFRACTION_TYPE" = SENSOR_REFRACTION_TYPE(int(arTypes[iIndex][0]))
            if not self.m_oSensor.is_refraction_type_supported(eType):
                Assert.fail("The Refraction Type {0} should be supported!", eType)

            # Refraction
            self.m_oSensor.refraction = eType
            self.m_logger.WriteLine6("\tThe new RefractionType is: {0}", self.m_oSensor.refraction)
            if eType == SENSOR_REFRACTION_TYPE.EARTH_4_3_RADIUS_METHOD:
                # RefractionModel
                modelEffectiveRadiusMethod: "RefractionModelEffectiveRadiusMethod" = (
                    RefractionModelEffectiveRadiusMethod(self.m_oSensor.refraction_model)
                )
                Assert.assertIsNotNone(modelEffectiveRadiusMethod)
                # Ceiling
                self.m_logger.WriteLine6("\t\tThe current Ceiling is: {0}", modelEffectiveRadiusMethod.ceiling)
                modelEffectiveRadiusMethod.ceiling = 10
                self.m_logger.WriteLine6("\t\tThe new Ceiling is: {0}", modelEffectiveRadiusMethod.ceiling)
                Assert.assertEqual(10, modelEffectiveRadiusMethod.ceiling)
                with pytest.raises(Exception):
                    modelEffectiveRadiusMethod.ceiling = -234
                # EffRad
                self.m_logger.WriteLine6("\t\tThe current EffRad is: {0}", modelEffectiveRadiusMethod.eff_rad)
                modelEffectiveRadiusMethod.eff_rad = 10
                self.m_logger.WriteLine6("\t\tThe new EffRad is: {0}", modelEffectiveRadiusMethod.eff_rad)
                Assert.assertEqual(10, modelEffectiveRadiusMethod.eff_rad)
                with pytest.raises(Exception):
                    modelEffectiveRadiusMethod.eff_rad = -234
                # MaxTargetAltitude
                self.m_logger.WriteLine6(
                    "\t\tThe current MaxTargetAltitude is: {0}", modelEffectiveRadiusMethod.max_target_altitude
                )
                modelEffectiveRadiusMethod.max_target_altitude = 103
                self.m_logger.WriteLine6(
                    "\t\tThe new MaxTargetAltitude is: {0}", modelEffectiveRadiusMethod.max_target_altitude
                )
                Assert.assertEqual(103, modelEffectiveRadiusMethod.max_target_altitude)
                with pytest.raises(Exception):
                    modelEffectiveRadiusMethod.max_target_altitude = -234
                # UseExtrapolation
                self.m_logger.WriteLine4(
                    "\t\tThe current UseExtrapolation is: {0}", modelEffectiveRadiusMethod.use_extrapolation
                )
                modelEffectiveRadiusMethod.use_extrapolation = False
                self.m_logger.WriteLine4(
                    "\t\tThe new UseExtrapolation is: {0}", modelEffectiveRadiusMethod.use_extrapolation
                )
                Assert.assertEqual(False, modelEffectiveRadiusMethod.use_extrapolation)
                modelEffectiveRadiusMethod.use_extrapolation = True
                self.m_logger.WriteLine4(
                    "\t\tThe new UseExtrapolation is: {0}", modelEffectiveRadiusMethod.use_extrapolation
                )
                Assert.assertEqual(True, modelEffectiveRadiusMethod.use_extrapolation)
            elif eType == SENSOR_REFRACTION_TYPE.ITU_R_P834_4:
                # RefractionModel
                modelITURP8344: "RefractionModelITURP8344" = RefractionModelITURP8344(self.m_oSensor.refraction_model)
                Assert.assertIsNotNone(modelITURP8344)
                # Ceiling
                self.m_logger.WriteLine6("\t\tThe current Ceiling is: {0}", modelITURP8344.ceiling)
                modelITURP8344.ceiling = 234
                self.m_logger.WriteLine6("\t\tThe new Ceiling is: {0}", modelITURP8344.ceiling)
                Assert.assertEqual(234, modelITURP8344.ceiling)
                with pytest.raises(Exception):
                    modelITURP8344.ceiling = -234
                # AtmosAltitude
                self.m_logger.WriteLine6("\t\tThe current AtmosAltitude is: {0}", modelITURP8344.atmos_altitude)
                modelITURP8344.atmos_altitude = 345
                self.m_logger.WriteLine6("\t\tThe new AtmosAltitude is: {0}", modelITURP8344.atmos_altitude)
                Assert.assertEqual(345, modelITURP8344.atmos_altitude)
                with pytest.raises(Exception):
                    modelITURP8344.ceiling = -345
                # KneeBendFactor
                self.m_logger.WriteLine6("\t\tThe current KneeBendFactor is: {0}", modelITURP8344.knee_bend_factor)
                modelITURP8344.knee_bend_factor = 0.345
                self.m_logger.WriteLine6("\t\tThe new KneeBendFactor is: {0}", modelITURP8344.knee_bend_factor)
                Assert.assertEqual(0.345, modelITURP8344.knee_bend_factor)
                with pytest.raises(Exception):
                    modelITURP8344.knee_bend_factor = 3.45
            elif eType == SENSOR_REFRACTION_TYPE.SCF_METHOD:
                # RefractionModel
                modelSCFMethod: "RefractionModelSCFMethod" = RefractionModelSCFMethod(self.m_oSensor.refraction_model)
                Assert.assertIsNotNone(modelSCFMethod)
                # MinTargetAltitude
                self.m_logger.WriteLine6(
                    "\t\tThe current MinTargetAltitude is: {0}", modelSCFMethod.min_target_altitude
                )
                modelSCFMethod.min_target_altitude = 14
                self.m_logger.WriteLine6("\t\tThe new MinTargetAltitude is: {0}", modelSCFMethod.min_target_altitude)
                Assert.assertEqual(14, modelSCFMethod.min_target_altitude)
                with pytest.raises(Exception):
                    modelSCFMethod.min_target_altitude = -3.45
                # Ceiling
                self.m_logger.WriteLine6("\t\tThe current Ceiling is: {0}", modelSCFMethod.ceiling)
                modelSCFMethod.ceiling = 234
                self.m_logger.WriteLine6("\t\tThe new Ceiling is: {0}", modelSCFMethod.ceiling)
                Assert.assertEqual(234, modelSCFMethod.ceiling)
                with pytest.raises(Exception):
                    modelSCFMethod.ceiling = -234
                # AtmosAltitude
                self.m_logger.WriteLine6("\t\tThe current AtmosAltitude is: {0}", modelSCFMethod.atmos_altitude)
                modelSCFMethod.atmos_altitude = 345
                self.m_logger.WriteLine6("\t\tThe new AtmosAltitude is: {0}", modelSCFMethod.atmos_altitude)
                Assert.assertEqual(345, modelSCFMethod.atmos_altitude)
                with pytest.raises(Exception):
                    modelSCFMethod.ceiling = -345
                # KneeBendFactor
                self.m_logger.WriteLine6("\t\tThe current KneeBendFactor is: {0}", modelSCFMethod.knee_bend_factor)
                modelSCFMethod.knee_bend_factor = 0.345
                self.m_logger.WriteLine6("\t\tThe new KneeBendFactor is: {0}", modelSCFMethod.knee_bend_factor)
                Assert.assertEqual(0.345, modelSCFMethod.knee_bend_factor)
                with pytest.raises(Exception):
                    modelSCFMethod.knee_bend_factor = 3.45
                # UseExtrapolation
                self.m_logger.WriteLine4("\t\tThe current UseExtrapolation is: {0}", modelSCFMethod.use_extrapolation)
                modelSCFMethod.use_extrapolation = False
                self.m_logger.WriteLine4("\t\tThe new UseExtrapolation is: {0}", modelSCFMethod.use_extrapolation)
                Assert.assertEqual(False, modelSCFMethod.use_extrapolation)
                modelSCFMethod.use_extrapolation = True
                self.m_logger.WriteLine4("\t\tThe new UseExtrapolation is: {0}", modelSCFMethod.use_extrapolation)
                Assert.assertEqual(True, modelSCFMethod.use_extrapolation)
                # UseRefractionIndex
                self.m_logger.WriteLine4(
                    "\t\tThe current UseRefractionIndex is: {0}", modelSCFMethod.use_refraction_index
                )
                modelSCFMethod.use_refraction_index = True
                self.m_logger.WriteLine4("\t\tThe new UseRefractionIndex is: {0}", modelSCFMethod.use_refraction_index)
                Assert.assertEqual(True, modelSCFMethod.use_refraction_index)

                # RefractionIndex
                self.m_logger.WriteLine6("\t\tThe current RefractionIndex is: {0}", modelSCFMethod.refraction_index)
                modelSCFMethod.refraction_index = 34.5
                self.m_logger.WriteLine6("\t\tThe new RefractionIndex is: {0}", modelSCFMethod.refraction_index)
                Assert.assertEqual(34.5, modelSCFMethod.refraction_index)
                with pytest.raises(Exception):
                    modelSCFMethod.refraction_index = -3.45

                with pytest.raises(Exception):
                    modelSCFMethod.coefficients.c0 = 345
                modelSCFMethod.use_refraction_index = False
                self.m_logger.WriteLine4("\t\tThe new UseRefractionIndex is: {0}", modelSCFMethod.use_refraction_index)
                Assert.assertEqual(False, modelSCFMethod.use_refraction_index)
                with pytest.raises(Exception):
                    modelSCFMethod.refraction_index = 123
                # Coefficients
                oCoefficients: "RefractionCoefficients" = modelSCFMethod.coefficients
                Assert.assertIsNotNone(oCoefficients)
                # C0
                self.m_logger.WriteLine6("\t\tThe current C0 is: {0}", oCoefficients.c0)
                oCoefficients.c0 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C0 is: {0}", oCoefficients.c0)
                Assert.assertEqual(123.456, oCoefficients.c0)
                with pytest.raises(Exception):
                    oCoefficients.c0 = -3.45
                # C1
                self.m_logger.WriteLine6("\t\tThe current C1 is: {0}", oCoefficients.c1)
                oCoefficients.c1 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C1 is: {0}", oCoefficients.c1)
                Assert.assertEqual(123.456, oCoefficients.c1)
                with pytest.raises(Exception):
                    oCoefficients.c1 = -3450000000000000000000000000000.0
                # C2
                self.m_logger.WriteLine6("\t\tThe current C2 is: {0}", oCoefficients.c2)
                oCoefficients.c2 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C2 is: {0}", oCoefficients.c2)
                Assert.assertEqual(123.456, oCoefficients.c2)
                with pytest.raises(Exception):
                    oCoefficients.c2 = -3450000000000000000000000000000.0
                # C3
                self.m_logger.WriteLine6("\t\tThe current C3 is: {0}", oCoefficients.c3)
                oCoefficients.c3 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C3 is: {0}", oCoefficients.c3)
                Assert.assertEqual(123.456, oCoefficients.c3)
                with pytest.raises(Exception):
                    oCoefficients.c3 = -3450000000000000000000000000000.0
                # C4
                self.m_logger.WriteLine6("\t\tThe current C4 is: {0}", oCoefficients.c4)
                oCoefficients.c4 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C4 is: {0}", oCoefficients.c4)
                Assert.assertEqual(123.456, oCoefficients.c4)
                with pytest.raises(Exception):
                    oCoefficients.c4 = -3450000000000000000000000000000.0
                # C5
                self.m_logger.WriteLine6("\t\tThe current C5 is: {0}", oCoefficients.c5)
                oCoefficients.c5 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C5 is: {0}", oCoefficients.c5)
                Assert.assertEqual(123.456, oCoefficients.c5)
                with pytest.raises(Exception):
                    oCoefficients.c5 = -3450000000000000000000000000000.0
                # C6
                self.m_logger.WriteLine6("\t\tThe current C6 is: {0}", oCoefficients.c6)
                oCoefficients.c6 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C6 is: {0}", oCoefficients.c6)
                Assert.assertEqual(123.456, oCoefficients.c6)
                with pytest.raises(Exception):
                    oCoefficients.c6 = -3450000000000000000000000000000.0
                # C7
                self.m_logger.WriteLine6("\t\tThe current C7 is: {0}", oCoefficients.c7)
                oCoefficients.c7 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C7 is: {0}", oCoefficients.c7)
                Assert.assertEqual(123.456, oCoefficients.c7)
                with pytest.raises(Exception):
                    oCoefficients.c7 = -3450000000000000000000000000000.0
                # C8
                self.m_logger.WriteLine6("\t\tThe current C8 is: {0}", oCoefficients.c8)
                oCoefficients.c8 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C8 is: {0}", oCoefficients.c8)
                Assert.assertEqual(123.456, oCoefficients.c8)
                with pytest.raises(Exception):
                    oCoefficients.c8 = -3450000000000000000000000000000.0
                # C9
                self.m_logger.WriteLine6("\t\tThe current C9 is: {0}", oCoefficients.c9)
                oCoefficients.c9 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C9 is: {0}", oCoefficients.c9)
                Assert.assertEqual(123.456, oCoefficients.c9)
                with pytest.raises(Exception):
                    oCoefficients.c9 = -3450000000000000000000000000000.0
                # C10
                self.m_logger.WriteLine6("\t\tThe current C10 is: {0}", oCoefficients.c10)
                oCoefficients.c10 = 123.456
                self.m_logger.WriteLine6("\t\tThe new C10 is: {0}", oCoefficients.c10)
                Assert.assertEqual(123.456, oCoefficients.c10)
                with pytest.raises(Exception):
                    oCoefficients.c10 = -3450000000000000000000000000000.0
            else:
                Assert.fail("The Refraction Type {0} should be supported!", eType)

            iIndex += 1

        self.m_logger.WriteLine("----- BASIC REFRACTION TEST ----- END -----")

    # endregion

    # region BasicCoarseDefinition
    def BasicCoarseDefinition(self):
        self.m_logger.WriteLine("----- BASIC COARSE DEFINITION TEST ----- BEGIN -----")
        # set AngleUnit
        self.m_logger.WriteLine5(
            "\tThe current AngleUnit format is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit")
        )
        self.m_oRoot.unit_preferences.set_current_unit("AngleUnit", "deg")
        self.m_logger.WriteLine5(
            "\tThe new AngleUnit format is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit")
        )
        Assert.assertEqual("deg", self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit"))
        # set SmallDistanceUnit
        self.m_logger.WriteLine5(
            "\tThe current SmallDistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"),
        )
        self.m_oRoot.unit_preferences.set_current_unit("SmallDistanceUnit", "mm")
        self.m_logger.WriteLine5(
            "\tThe new SmallDistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"),
        )
        Assert.assertEqual("mm", self.m_oRoot.unit_preferences.get_current_unit_abbrv("SmallDistanceUnit"))
        # set FrequencyUnit
        self.m_logger.WriteLine5(
            "\tThe current FrequencyUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("FrequencyUnit"),
        )
        self.m_oRoot.unit_preferences.set_current_unit("FrequencyUnit", "GHz")
        self.m_logger.WriteLine5(
            "\tThe new FrequencyUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("FrequencyUnit"),
        )
        Assert.assertEqual("GHz", self.m_oRoot.unit_preferences.get_current_unit_abbrv("FrequencyUnit"))
        # set DistanceUnit
        self.m_logger.WriteLine5(
            "\tThe current DistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"),
        )
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", "km")
        self.m_logger.WriteLine5(
            "\tThe new DistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"),
        )
        Assert.assertEqual("km", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))

        #
        #  SensorCommonTasks
        #

        # DefineSimpleConic
        self.m_logger.WriteLine6("\tThe current PatternType is: {0}", self.m_oSensor.pattern_type)
        # SetPatternType(SIMPLE_CONIC)
        self.m_oSensor.common_tasks.set_pattern_simple_conic(23.123456789, 5)
        self.m_logger.WriteLine6("\tThe new PatternType is: {0}", self.m_oSensor.pattern_type)
        Assert.assertEqual(SENSOR_PATTERN.SIMPLE_CONIC, self.m_oSensor.pattern_type)
        # Pattern
        oSimpleConic: "SensorSimpleConicPattern" = SensorSimpleConicPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oSimpleConic)
        # ConeAngle
        self.m_logger.WriteLine6("\t\tThe new ConeAngle is: {0}", oSimpleConic.cone_angle)
        Assert.assertEqual(oSimpleConic.cone_angle, 23.123456789)

        # DefineComplexConic
        self.m_oSensor.common_tasks.set_pattern_complex_conic(12.34, 12.34, 123.456, 234.567)
        self.m_logger.WriteLine6("\tThe new PatternType is: {0}", self.m_oSensor.pattern_type)
        Assert.assertEqual(SENSOR_PATTERN.COMPLEX_CONIC, self.m_oSensor.pattern_type)
        # Pattern
        oComplexConic: "SensorComplexConicPattern" = SensorComplexConicPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oComplexConic)
        # InnerConeHalfAngle
        self.m_logger.WriteLine6("\t\tThe current InnerConeHalfAngle is: {0}", oComplexConic.inner_cone_half_angle)
        self.m_logger.WriteLine6("\t\tThe new InnerConeHalfAngle is: {0}", oComplexConic.inner_cone_half_angle)
        Assert.assertEqual(12.34, oComplexConic.inner_cone_half_angle)
        # OuterConeHalfAngle
        self.m_logger.WriteLine6("\t\tThe current OuterConeHalfAngle is: {0}", oComplexConic.outer_cone_half_angle)
        self.m_logger.WriteLine6("\t\tThe new OuterConeHalfAngle is: {0}", oComplexConic.outer_cone_half_angle)
        Assert.assertEqual(12.34, oComplexConic.outer_cone_half_angle)
        # MinimumClockAngle
        self.m_logger.WriteLine6("\t\tThe current MinimumClockAngle is: {0}", oComplexConic.minimum_clock_angle)
        self.m_logger.WriteLine6("\t\tThe new MinimumClockAngle is: {0}", oComplexConic.minimum_clock_angle)
        Assert.assertAlmostEqual(123.456, float(oComplexConic.minimum_clock_angle), delta=0.0001)
        # MaximumClockAngle
        self.m_logger.WriteLine6("\t\tThe current MaximumClockAngle is: {0}", oComplexConic.maximum_clock_angle)
        self.m_logger.WriteLine6("\t\tThe new MaximumClockAngle is: {0}", oComplexConic.maximum_clock_angle)
        Assert.assertAlmostEqual(234.567, float(oComplexConic.maximum_clock_angle), delta=0.0001)

        # DefineCustom
        self.m_oSensor.common_tasks.set_pattern_custom(TestBase.GetScenarioFile("AreaTgtWeird", "RedSensor.Pattern"))
        self.m_logger.WriteLine6("\tThe new PatternType is: {0}", self.m_oSensor.pattern_type)
        Assert.assertEqual(SENSOR_PATTERN.CUSTOM, self.m_oSensor.pattern_type)
        # Pattern
        oCustom: "SensorCustomPattern" = SensorCustomPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oCustom)
        oCustom.angular_resolution = 5
        Assert.assertEqual(5, oCustom.angular_resolution)
        oCustom.use_native_resolution = False
        Assert.assertEqual(False, oCustom.use_native_resolution)

        # Filename
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oCustom.filename)

        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oCustom.filename)
        Assert.assertEqual(TestBase.PathCombine("AreaTgtWeird", "RedSensor.Pattern"), oCustom.filename)

        # DefineHalfPower
        self.m_oSensor.common_tasks.set_pattern_half_power(12345.6789, 12345.6789, 5)
        self.m_logger.WriteLine6("\tThe new PatternType is: {0}", self.m_oSensor.pattern_type)
        Assert.assertEqual(SENSOR_PATTERN.HALF_POWER, self.m_oSensor.pattern_type)
        # Pattern
        oHalfPower: "SensorHalfPowerPattern" = SensorHalfPowerPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oHalfPower)
        # HalfAngle
        self.m_logger.WriteLine6("\t\tThe current HalfAngle is: {0}", oHalfPower.half_angle)
        # Frequency
        self.m_logger.WriteLine6("\t\tThe current Frequency is: {0}", oHalfPower.frequency)
        self.m_logger.WriteLine6("\t\tThe new Frequency is: {0}", oHalfPower.frequency)
        Assert.assertEqual(12345.6789, oHalfPower.frequency)
        self.m_logger.WriteLine6("\t\tThe new HalfAngle is: {0}", oHalfPower.half_angle)
        # AntennaDiameter
        self.m_logger.WriteLine6("\t\tThe current AntennaDiameter is: {0}", oHalfPower.antenna_diameter)
        self.m_logger.WriteLine6("\t\tThe new AntennaDiameter is: {0}", oHalfPower.antenna_diameter)
        Assert.assertEqual(12345.6789, oHalfPower.antenna_diameter)
        self.m_logger.WriteLine6("\t\tThe new HalfAngle is: {0}", oHalfPower.half_angle)

        # DefineRectangular
        self.m_oSensor.common_tasks.set_pattern_rectangular(12.34, 43.21)
        self.m_logger.WriteLine6("\tThe new PatternType is: {0}", self.m_oSensor.pattern_type)
        Assert.assertEqual(SENSOR_PATTERN.RECTANGULAR, self.m_oSensor.pattern_type)
        # Pattern
        oRectangular: "SensorRectangularPattern" = SensorRectangularPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oRectangular)
        # VerticalHalfAngle
        self.m_logger.WriteLine6("\t\tThe current VerticalHalfAngle is: {0}", oRectangular.vertical_half_angle)
        self.m_logger.WriteLine6("\t\tThe new VerticalHalfAngle is: {0}", oRectangular.vertical_half_angle)
        Assert.assertEqual(12.34, oRectangular.vertical_half_angle)
        # HorizontalHalfAngle
        self.m_logger.WriteLine6("\t\tThe current HorizontalHalfAngle is: {0}", oRectangular.horizontal_half_angle)
        self.m_logger.WriteLine6("\t\tThe new HorizontalHalfAngle is: {0}", oRectangular.horizontal_half_angle)
        Assert.assertEqual(43.21, oRectangular.horizontal_half_angle)

        # DefineSAR
        self.m_oSensor.common_tasks.set_pattern_sar(12.3456789, 89.7654321, 56.789, 34.56789, 123.456789)
        self.m_logger.WriteLine6("\tThe new PatternType is: {0}", self.m_oSensor.pattern_type)
        Assert.assertEqual(SENSOR_PATTERN.SAR, self.m_oSensor.pattern_type)
        # Pattern
        oSAR: "SensorSARPattern" = SensorSARPattern(self.m_oSensor.pattern)
        Assert.assertIsNotNone(oSAR)
        # MinElevationAngle
        self.m_logger.WriteLine6("\t\tThe current MinElevationAngle is: {0}", oSAR.min_elevation_angle)
        self.m_logger.WriteLine6("\t\tThe new MinElevationAngle is: {0}", oSAR.min_elevation_angle)
        Assert.assertEqual(12.3456789, oSAR.min_elevation_angle)
        # MaxElevationAngle
        self.m_logger.WriteLine6("\t\tThe current MaxElevationAngle is: {0}", oSAR.max_elevation_angle)
        self.m_logger.WriteLine6("\t\tThe new MaxElevationAngle is: {0}", oSAR.max_elevation_angle)
        Assert.assertEqual(89.7654321, oSAR.max_elevation_angle)
        # ForeExclusionAngle
        self.m_logger.WriteLine6("\t\tThe current ForeExclusionAngle is: {0}", oSAR.fore_exclusion_angle)
        self.m_logger.WriteLine6("\t\tThe new ForeExclusionAngle is: {0}", oSAR.fore_exclusion_angle)
        Assert.assertEqual(56.789, oSAR.fore_exclusion_angle)
        # AftExclusionAngle
        self.m_logger.WriteLine6("\t\tThe current AftExclusionAngle is: {0}", oSAR.aft_exclusion_angle)
        self.m_logger.WriteLine6("\t\tThe new AftExclusionAngle is: {0}", oSAR.aft_exclusion_angle)
        Assert.assertEqual(34.56789, oSAR.aft_exclusion_angle)
        # ParentAltitude
        self.m_logger.WriteLine6("\t\tThe current ParentAltitude is: {0}", oSAR.parent_altitude)
        self.m_logger.WriteLine6("\t\tThe new ParentAltitude is: {0}", oSAR.parent_altitude)
        Assert.assertEqual(123.456789, oSAR.parent_altitude)

        # SetPointingFixedAzEl
        oFixed1: "SensorPointingFixed" = self.m_oSensor.common_tasks.set_pointing_fixed_az_el(
            10, 20, AZ_EL_ABOUT_BORESIGHT.ROTATE
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oFixed1)
        oOrientation1: "IOrientation" = oFixed1.orientation
        Assert.assertIsNotNone(oOrientation1)

        az: typing.Any = None
        el: typing.Any = None

        eAzElAboutBoresight: "AZ_EL_ABOUT_BORESIGHT" = None
        (az, el, eAzElAboutBoresight) = oOrientation1.query_az_el()
        Assert.assertAlmostEqual(10, float(az), delta=1e-08)
        Assert.assertAlmostEqual(20, float(el), delta=1e-08)
        Assert.assertEqual(
            AZ_EL_ABOUT_BORESIGHT.ROTATE, eAzElAboutBoresight, "SetPointingFixedAzEl AZ_EL_ABOUT_BORESIGHT problem"
        )

        # SetPointingFixedEuler
        oFixed2: "SensorPointingFixed" = self.m_oSensor.common_tasks.set_pointing_fixed_euler(
            EULER_ORIENTATION_SEQUENCE.SEQUENCE_132, 30, 40, 50
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oFixed2)
        oOrientation2: "IOrientation" = oFixed2.orientation
        Assert.assertIsNotNone(oOrientation2)

        a: typing.Any = None
        b: typing.Any = None
        c: typing.Any = None

        (a, b, c) = oOrientation2.query_euler_angles(EULER_ORIENTATION_SEQUENCE.SEQUENCE_132)
        Assert.assertAlmostEqual(30, float(a), delta=1e-08)
        Assert.assertAlmostEqual(40, float(b), delta=1e-08)
        Assert.assertAlmostEqual(50, float(c), delta=1e-08)

        # SetPointingFixedQuat
        oFixed3: "SensorPointingFixed" = self.m_oSensor.common_tasks.set_pointing_fixed_quat(0.1, 0.2, 0.3, 0.4)
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oFixed3)
        oOrientation3: "IOrientation" = oFixed3.orientation
        Assert.assertIsNotNone(oOrientation3)

        qx: float = 0
        qy: float = 0
        qz: float = 0
        qs: float = 0

        (qx, qy, qz, qs) = oOrientation3.query_quaternion()
        Assert.assertEqual(0.182574, Math.Round(qx, 6))  # Values are normalized
        Assert.assertEqual(0.365148, Math.Round(qy, 6))
        Assert.assertEqual(0.547723, Math.Round(qz, 6))
        Assert.assertEqual(0.730297, Math.Round(qs, 6))

        # SetPointingFixedYPR
        oFixed4: "SensorPointingFixed" = self.m_oSensor.common_tasks.set_pointing_fixed_ypr(
            YPR_ANGLES_SEQUENCE.RPY, 12, 24, 36
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oFixed4)
        oOrientation4: "IOrientation" = oFixed4.orientation
        Assert.assertIsNotNone(oOrientation4)

        y: typing.Any = None
        p: typing.Any = None
        r: typing.Any = None

        (y, p, r) = oOrientation4.query_ypr_angles(YPR_ANGLES_SEQUENCE.RPY)
        Assert.assertAlmostEqual(12, float(y), delta=1e-08)
        Assert.assertAlmostEqual(24, float(p), delta=1e-08)
        Assert.assertAlmostEqual(36, float(r), delta=1e-08)

        # SetPointingFixedAxesAzEl
        oFixedAxes5: "SensorPointingFixedAxes" = self.m_oSensor.common_tasks.set_pointing_fixed_axes_az_el(
            "CentralBody/Sun MOJ2000 Axes", 11, 22, AZ_EL_ABOUT_BORESIGHT.HOLD
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED_AXES, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oFixedAxes5)
        oOrientation5: "IOrientation" = oFixedAxes5.orientation
        Assert.assertIsNotNone(oOrientation5)
        sReferenceAxes5: str = oFixedAxes5.reference_axes
        Assert.assertEqual("CentralBody/Sun MOJ2000 Axes", sReferenceAxes5)

        az5: typing.Any = None
        el5: typing.Any = None

        eAzElAboutBoresight5: "AZ_EL_ABOUT_BORESIGHT" = None
        (az5, el5, eAzElAboutBoresight5) = oOrientation5.query_az_el()
        Assert.assertAlmostEqual(11, float(az5), delta=1e-08)
        Assert.assertAlmostEqual(22, float(el5), delta=1e-08)
        Assert.assertEqual(
            AZ_EL_ABOUT_BORESIGHT.HOLD, eAzElAboutBoresight5, "SetPointingFixedAzEl AZ_EL_ABOUT_BORESIGHT5 problem"
        )

        # SetPointingFixedAxesEuler
        oFixedAxes6: "SensorPointingFixedAxes" = self.m_oSensor.common_tasks.set_pointing_fixed_axes_euler(
            "CentralBody/Sun J2000 Axes", EULER_ORIENTATION_SEQUENCE.SEQUENCE_132, 30, 40, 50
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED_AXES, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oFixedAxes6)
        oOrientation6: "IOrientation" = oFixedAxes6.orientation
        Assert.assertIsNotNone(oOrientation6)
        sReferenceAxes6: str = oFixedAxes6.reference_axes
        Assert.assertEqual("CentralBody/Sun J2000 Axes", sReferenceAxes6)

        a6: typing.Any = None
        b6: typing.Any = None
        c6: typing.Any = None

        (a6, b6, c6) = oOrientation6.query_euler_angles(EULER_ORIENTATION_SEQUENCE.SEQUENCE_132)
        Assert.assertAlmostEqual(30, float(a6), delta=1e-08)
        Assert.assertAlmostEqual(40, float(b6), delta=1e-08)
        Assert.assertAlmostEqual(50, float(c6), delta=1e-08)

        # SetPointingFixedAxesQuat
        oFixedAxes7: "SensorPointingFixedAxes" = self.m_oSensor.common_tasks.set_pointing_fixed_axes_quat(
            "CentralBody/Sun MOJ2000 Axes", 0.1, 0.2, 0.3, 0.4
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED_AXES, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oFixedAxes7)
        oOrientation7: "IOrientation" = oFixedAxes7.orientation
        Assert.assertIsNotNone(oOrientation7)
        sReferenceAxes7: str = oFixedAxes7.reference_axes
        Assert.assertEqual("CentralBody/Sun MOJ2000 Axes", sReferenceAxes7)

        qx7: float = 0
        qy7: float = 0
        qz7: float = 0
        qs7: float = 0

        (qx7, qy7, qz7, qs7) = oOrientation7.query_quaternion()
        Assert.assertEqual(0.182574, Math.Round(qx, 6))  # Values are normalized
        Assert.assertEqual(0.365148, Math.Round(qy, 6))
        Assert.assertEqual(0.547723, Math.Round(qz, 6))
        Assert.assertEqual(0.730297, Math.Round(qs, 6))

        # SetPointingFixedAxesYPR
        oFixedAxes8: "SensorPointingFixedAxes" = self.m_oSensor.common_tasks.set_pointing_fixed_axes_ypr(
            "CentralBody/Sun J2000 Axes", YPR_ANGLES_SEQUENCE.RYP, 11, 22, 33
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED_AXES, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oFixedAxes8)
        oOrientation8: "IOrientation" = oFixedAxes8.orientation
        Assert.assertIsNotNone(oOrientation8)

        y8: typing.Any = None
        p8: typing.Any = None
        r8: typing.Any = None

        (y8, p8, r8) = oOrientation8.query_ypr_angles(YPR_ANGLES_SEQUENCE.RYP)
        Assert.assertAlmostEqual(11, float(y8), delta=1e-08)
        Assert.assertAlmostEqual(22, float(p8), delta=1e-08)
        Assert.assertAlmostEqual(33, float(r8), delta=1e-08)
        if TestBase.NoGraphicsMode:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_3D_MODEL)

        else:
            # SetPointing3DModel
            self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_3D_MODEL)
            o3DModel: "SensorPointing3DModel" = SensorPointing3DModel(self.m_oSensor.pointing)
            if Array.Length(o3DModel.available_elements) > 0:
                sAttachName: str = str(o3DModel.available_elements[0])  # try the first one
                self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)  # set to something else to test below

                o3DModel2: "SensorPointing3DModel" = self.m_oSensor.common_tasks.set_pointing_3d_model(sAttachName)
                Assert.assertIsNotNone(o3DModel2)
                Assert.assertEqual(SENSOR_POINTING.POINT_3D_MODEL, self.m_oSensor.pointing_type)
                Assert.assertEqual(sAttachName, o3DModel2.attach_name)

            with pytest.raises(Exception):
                o3DModel3: "SensorPointing3DModel" = self.m_oSensor.common_tasks.set_pointing_3d_model(
                    "BogusAttachName"
                )

        if ((IStkObject(self.m_oSensor)).parent.class_name != "Facility") and (
            (IStkObject(self.m_oSensor)).parent.class_name != "Target"
        ):
            oGrazingAlt: "SensorPointingGrazingAltitude" = self.m_oSensor.common_tasks.set_pointing_grazing_altitude(
                9.9, 100
            )
            Assert.assertEqual(SENSOR_POINTING.POINT_GRAZING_ALTITUDE, self.m_oSensor.pointing_type)
            Assert.assertIsNotNone(oGrazingAlt)
            Assert.assertEqual(9.9, oGrazingAlt.azimuth_offset)
            Assert.assertEqual(100, oGrazingAlt.grazing_altitude)

        # SetPointingSpinning (Continuous)
        oSpinning: "SensorPointingSpinning" = self.m_oSensor.common_tasks.set_pointing_spinning(
            1.0, 1.05, 1.1, SENSOR_SCAN_MODE.CONTINUOUS, 1.2, 1.3, 1.4, 1.5
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_SPINNING, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oSpinning)
        Assert.assertEqual(1.0, Math.Round(float(oSpinning.spin_axis_azimuth), 9))
        Assert.assertEqual(1.05, Math.Round(float(oSpinning.spin_axis_elevation), 9))
        Assert.assertEqual(1.1, Math.Round(float(oSpinning.spin_axis_cone_angle), 9))
        Assert.assertEqual(SENSOR_SCAN_MODE.CONTINUOUS, oSpinning.scan_mode)
        Assert.assertEqual(1.2, Math.Round(float(oSpinning.spin_rate), 9))
        Assert.assertEqual(1.3, Math.Round(float(oSpinning.offset_angle), 9))
        # ignored Assert.AreEqual(1.4,  Math.Round( (double)oSpinning.ClockAngleStart, 9) );
        # ignored Assert.AreEqual(1.5,  Math.Round( (double)oSpinning.ClockAngleStop, 9));

        # SetPointingSpinning (Continuous)
        oSpinning = self.m_oSensor.common_tasks.set_pointing_spinning(
            1.0, 1.05, 1.1, SENSOR_SCAN_MODE.BIDIRECTIONAL, 1.2, 1.3, 1.4, 1.5
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_SPINNING, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oSpinning)
        Assert.assertEqual(1.0, Math.Round(float(oSpinning.spin_axis_azimuth), 9))
        Assert.assertEqual(1.05, Math.Round(float(oSpinning.spin_axis_elevation), 9))
        Assert.assertEqual(1.1, Math.Round(float(oSpinning.spin_axis_cone_angle), 9))
        Assert.assertEqual(SENSOR_SCAN_MODE.BIDIRECTIONAL, oSpinning.scan_mode)
        Assert.assertEqual(1.2, Math.Round(float(oSpinning.spin_rate), 9))
        Assert.assertEqual(1.3, Math.Round(float(oSpinning.offset_angle), 9))
        Assert.assertEqual(1.4, Math.Round(float(oSpinning.clock_angle_start), 9))
        Assert.assertEqual(1.5, Math.Round(float(oSpinning.clock_angle_stop), 9))

        # SetPointingTargetedTracking
        oTargeted: "SensorPointingTargeted" = self.m_oSensor.common_tasks.set_pointing_targeted_tracking(
            TRACK_MODE_TYPE.TRANSMIT, BORESIGHT_TYPE.LEVEL, "*/AreaTarget/AreaTarget1"
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_TARGETED, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(oTargeted)
        oTrgtBsight: "ISensorPointingTargetedBoresight" = oTargeted.boresight_data
        Assert.assertIsNotNone(oTrgtBsight)
        oBoresightTrack: "SensorPointingTargetedBoresightTrack" = clr.CastAs(
            oTrgtBsight, SensorPointingTargetedBoresightTrack
        )
        Assert.assertIsNotNone(oBoresightTrack)
        Assert.assertEqual(TRACK_MODE_TYPE.TRANSMIT, oBoresightTrack.track_mode)
        Assert.assertEqual(BORESIGHT_TYPE.LEVEL, oBoresightTrack.about_boresight)
        targetCollection: "SensorTargetCollection" = oTargeted.targets
        Assert.assertEqual(1, targetCollection.count, "count should be 1")
        Assert.assertEqual("AreaTarget/AreaTarget1", targetCollection[0].name, "wrong target name")
        target: "SensorTarget"
        for target in targetCollection:
            # Name
            self.m_logger.WriteLine5("\t\tElement: {0}", target.name)

        # SetPointingAlongVector
        alongVector: "SensorPointingAlongVector" = self.m_oSensor.common_tasks.set_pointing_along_vector(
            "Aircraft/Boing737 Body.-X", "Aircraft/Boing737 Body.-Y", 10
        )
        Assert.assertEqual(SENSOR_POINTING.POINT_ALONG_VECTOR, self.m_oSensor.pointing_type)
        Assert.assertIsNotNone(alongVector)
        arAvailAlignmentVecs = alongVector.available_alignment_vectors
        Assert.assertTrue((len(arAvailAlignmentVecs) > 0))
        Assert.assertEqual("Aircraft/Boing737 Body.-X", alongVector.alignment_vector)
        arAvailConstraintVecs = alongVector.available_constraint_vectors
        Assert.assertTrue((len(arAvailConstraintVecs) > 0))
        Assert.assertEqual("Aircraft/Boing737 Body.-Y", alongVector.constraint_vector)
        Assert.assertEqual(10, alongVector.clock_angle_offset)

        # restore Units
        self.m_oRoot.unit_preferences.reset_units()
        self.m_logger.WriteLine("----- THE BASIC COARSE DEFINITION TEST ----- END -----")

    # endregion

    # region BasicPointing
    def BasicCoarsePointing(self, eType: "STK_OBJECT_TYPE"):
        self.m_logger.WriteLine("----- THE BASIC COARSE POINTING TEST ----- BEGIN -----")
        # set AngleUnit
        strAngleUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit")
        self.m_logger.WriteLine5("\tThe current AngleUnit is: {0}", strAngleUnit)
        self.m_oRoot.unit_preferences.set_current_unit("AngleUnit", "rad")
        self.m_logger.WriteLine5(
            "\tThe new AngleUnit is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit")
        )
        Assert.assertEqual("rad", self.m_oRoot.unit_preferences.get_current_unit_abbrv("AngleUnit"))
        # set DateFormat
        strDateFormat: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat")
        self.m_logger.WriteLine5("\tThe current DateFormat is: {0}", strDateFormat)
        self.m_oRoot.unit_preferences.set_current_unit("DateFormat", "UTCG")
        self.m_logger.WriteLine5(
            "\tThe new DateFormat is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat")
        )
        Assert.assertEqual("UTCG", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DateFormat"))
        # set DistanceUnit
        strDistanceUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\tThe current DistanceUnit is: {0}", strDistanceUnit)
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", "m")
        self.m_logger.WriteLine5(
            "\tThe new DistanceUnit is: {0}", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        )
        Assert.assertEqual("m", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))

        # PointingType
        self.m_logger.WriteLine6("\tThe current PointingType is: {0}", self.m_oSensor.pointing_type)

        # region POINT_3D_MODEL
        with pytest.raises(Exception):
            self.m_oSensor.common_tasks.set_pointing_3d_model("InvalidName")
        # endregion

        # region POINT_EXTERNAL
        # SetPointingType(POINT_EXTERNAL)
        strCorrect: str = TestBase.GetScenarioFile("SensorPointing_External.sp")
        strIncorrect: str = TestBase.GetScenarioFile("SensorPointing_External78.sp")
        with pytest.raises(Exception):
            self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_EXTERNAL)
        with pytest.raises(Exception):
            self.m_oSensor.set_pointing_external_file(strIncorrect)
        with pytest.raises(Exception):
            self.m_oSensor.set_pointing_external_file("")
        # SetPointingExternalFile
        self.m_oSensor.set_pointing_external_file(strCorrect)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_EXTERNAL, self.m_oSensor.pointing_type)
        # Pointing
        oExternal: "SensorPointingExternal" = SensorPointingExternal(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oExternal)
        # Filename
        self.m_logger.WriteLine5("\t\tThe current Filename is: {0}", oExternal.filename)
        oExternal.filename = TestBase.GetScenarioFile("AttTimeAzElAngs_Example.sp")
        self.m_logger.WriteLine5("\t\tThe new Filename is: {0}", oExternal.filename)
        with pytest.raises(Exception):
            oExternal.filename = strIncorrect
        # endregion

        # region POINT_FIXED
        # SetPointingType(POINT_FIXED)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED, self.m_oSensor.pointing_type)
        # Pointing
        oFixed: "SensorPointingFixed" = SensorPointingFixed(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oFixed)
        # Orientation
        oHelper = OrientationTest(self.m_oRoot.unit_preferences)
        oHelper.Run(oFixed.orientation, Orientations.All)
        # endregion

        # region POINT_FIXED_AXES
        # SetPointingType(POINT_FIXED_AXES)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_FIXED_AXES)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_FIXED_AXES, self.m_oSensor.pointing_type)
        # Pointing
        oFixedAxes: "SensorPointingFixedAxes" = SensorPointingFixedAxes(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oFixedAxes)
        # ReferenceAxes
        self.m_logger.WriteLine5("\t\tThe current ReferenceAxes is: {0}", oFixedAxes.reference_axes)
        oFixedAxes.reference_axes = "CentralBody/Sun MOJ2000 Axes"
        self.m_logger.WriteLine5("\t\tThe new ReferenceAxes is: {0}", oFixedAxes.reference_axes)
        Assert.assertEqual("CentralBody/Sun MOJ2000 Axes", oFixedAxes.reference_axes)
        with pytest.raises(Exception):
            oFixedAxes.reference_axes = "Sun MOJ2000"
        # AvailableAxes
        arAxes = oFixedAxes.available_axes
        self.m_logger.WriteLine3("\t\tAvailable {0} Reference Axes:", Array.Length(arAxes))
        if Array.Length(arAxes) > 0:
            strAxes: str = str(arAxes[0])
            self.m_logger.WriteLine7("\t\t\tAxes {0}: {1}", 0, strAxes)
            if (
                (
                    (strAxes.find((IStkObject(self.m_oSensor)).parent.class_name) != -1)
                    and (strAxes.find((IStkObject(self.m_oSensor)).parent.instance_name) != -1)
                )
                and (strAxes.find((IStkObject(self.m_oSensor)).class_name) != -1)
            ) and (strAxes.find((IStkObject(self.m_oSensor)).instance_name) != -1):
                self.m_logger.WriteLine("\t\t\t\tCannot set reference to itself.")

            oFixedAxes.reference_axes = strAxes
            self.m_logger.WriteLine5("\t\t\t\tThe new ReferenceAxes is: {0}", oFixedAxes.reference_axes)
            Assert.assertEqual(strAxes, oFixedAxes.reference_axes)

        # Orientation
        oHelper.Run(oFixedAxes.orientation, Orientations.All)
        # endregion

        # region POINT_SPINNING
        # SetPointingType(POINT_SPINNING)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_SPINNING)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_SPINNING, self.m_oSensor.pointing_type)
        # Pointing
        oSpinning: "SensorPointingSpinning" = SensorPointingSpinning(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oSpinning)

        # region CONTINUOUS
        # ScanMode (CONTINUOUS)
        self.m_logger.WriteLine6("\t\tThe current ScanMode is: {0}", oSpinning.scan_mode)
        oSpinning.scan_mode = SENSOR_SCAN_MODE.CONTINUOUS
        self.m_logger.WriteLine6("\t\tThe new ScanMode is: {0}", oSpinning.scan_mode)
        Assert.assertEqual(SENSOR_SCAN_MODE.CONTINUOUS, oSpinning.scan_mode)
        # ClockAngleStart
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = 1.234
        # ClockAngleStop
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 3.456
        # SpinRate
        self.m_logger.WriteLine6("\t\t\tThe current SpinRate is: {0}", oSpinning.spin_rate)
        oSpinning.spin_rate = 98.7654321
        self.m_logger.WriteLine6("\t\t\tThe new SpinRate is: {0}", oSpinning.spin_rate)
        Assert.assertAlmostEqual(98.7654321, oSpinning.spin_rate, delta=1e-07)
        with pytest.raises(Exception):
            oSpinning.spin_rate = 3400000000000000000000000000000000000000000000000000000000.0
        # OffsetAngle
        self.m_logger.WriteLine6("\t\t\tThe current OffsetAngle is: {0}", oSpinning.offset_angle)
        oSpinning.offset_angle = 0.123
        self.m_logger.WriteLine6("\t\t\tThe new OffsetAngle is: {0}", oSpinning.offset_angle)
        Assert.assertEqual(0.123, oSpinning.offset_angle)
        with pytest.raises(Exception):
            oSpinning.offset_angle = 12.34
        # SpinAxisAzimuth
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        oSpinning.spin_axis_azimuth = -0.123
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        if (eType == STK_OBJECT_TYPE.FACILITY) or (eType == STK_OBJECT_TYPE.TARGET):
            Assert.assertAlmostEqual(6.16, float(oSpinning.spin_axis_azimuth), delta=0.001)
        else:
            Assert.assertAlmostEqual(-0.123, float(oSpinning.spin_axis_azimuth), delta=0.001)
        with pytest.raises(Exception):
            oSpinning.spin_axis_azimuth = 12.34
        # SpinAxisElevation
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        oSpinning.spin_axis_elevation = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        Assert.assertEqual(1.23, oSpinning.spin_axis_elevation)
        with pytest.raises(Exception):
            oSpinning.spin_axis_elevation = 12.34
        # SpinAxisConeAngle
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        oSpinning.spin_axis_cone_angle = 2.3
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        Assert.assertEqual(2.3, oSpinning.spin_axis_cone_angle)
        with pytest.raises(Exception):
            oSpinning.spin_axis_cone_angle = 12.34
        # endregion

        # region BIDIRECTIONAL
        # ScanMode (BIDIRECTIONAL)
        oSpinning.scan_mode = SENSOR_SCAN_MODE.BIDIRECTIONAL
        self.m_logger.WriteLine6("\t\tThe new ScanMode is: {0}", oSpinning.scan_mode)
        Assert.assertEqual(SENSOR_SCAN_MODE.BIDIRECTIONAL, oSpinning.scan_mode)
        # ClockAngleStart
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        oSpinning.clock_angle_start = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        Assert.assertEqual(1.23, oSpinning.clock_angle_start)
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = -56
        # ClockAngleStop
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        oSpinning.clock_angle_stop = 3.21
        self.m_logger.WriteLine6("\t\t\tThe new ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        Assert.assertEqual(3.21, oSpinning.clock_angle_stop)
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 56
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = 5.6
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 0.56
        with pytest.raises(Exception):
            oSpinning.set_clock_angles(5, 3)
        # SetClockAngles
        oSpinning.set_clock_angles(3, 5)
        Assert.assertEqual(3, oSpinning.clock_angle_start)
        Assert.assertEqual(5, oSpinning.clock_angle_stop)
        # SpinRate
        self.m_logger.WriteLine6("\t\t\tThe current SpinRate is: {0}", oSpinning.spin_rate)
        oSpinning.spin_rate = 98.7654321
        self.m_logger.WriteLine6("\t\t\tThe new SpinRate is: {0}", oSpinning.spin_rate)
        Assert.assertAlmostEqual(98.7654321, oSpinning.spin_rate, delta=1e-06)
        with pytest.raises(Exception):
            oSpinning.spin_rate = 3400000000000000000000000000000000000000000000000000000000.0
        # OffsetAngle
        self.m_logger.WriteLine6("\t\t\tThe current OffsetAngle is: {0}", oSpinning.offset_angle)
        oSpinning.offset_angle = 0.123
        self.m_logger.WriteLine6("\t\t\tThe new OffsetAngle is: {0}", oSpinning.offset_angle)
        Assert.assertEqual(0.123, oSpinning.offset_angle)
        with pytest.raises(Exception):
            oSpinning.offset_angle = 12.34
        # SpinAxisAzimuth
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        oSpinning.spin_axis_azimuth = -0.123
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        if (eType == STK_OBJECT_TYPE.FACILITY) or (eType == STK_OBJECT_TYPE.TARGET):
            Assert.assertAlmostEqual(6.16, float(oSpinning.spin_axis_azimuth), delta=0.001)
        else:
            Assert.assertAlmostEqual(-0.123, float(oSpinning.spin_axis_azimuth), delta=0.001)
        with pytest.raises(Exception):
            oSpinning.spin_axis_azimuth = 12.34
        # SpinAxisElevation
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        oSpinning.spin_axis_elevation = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        Assert.assertEqual(1.23, oSpinning.spin_axis_elevation)
        with pytest.raises(Exception):
            oSpinning.spin_axis_elevation = 12.34
        # SpinAxisConeAngle
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        oSpinning.spin_axis_cone_angle = 2.3
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        Assert.assertEqual(2.3, oSpinning.spin_axis_cone_angle)
        with pytest.raises(Exception):
            oSpinning.spin_axis_cone_angle = 12.34
        # endregion

        # region UNIDIRECTIONAL
        # ScanMode (UNIDIRECTIONAL)
        oSpinning.scan_mode = SENSOR_SCAN_MODE.UNIDIRECTIONAL
        self.m_logger.WriteLine6("\t\tThe new ScanMode is: {0}", oSpinning.scan_mode)
        Assert.assertEqual(SENSOR_SCAN_MODE.UNIDIRECTIONAL, oSpinning.scan_mode)
        # ClockAngleStart
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        oSpinning.clock_angle_start = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new ClockAngleStart is: {0}", oSpinning.clock_angle_start)
        Assert.assertEqual(1.23, oSpinning.clock_angle_start)
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = -56
        # ClockAngleStop
        self.m_logger.WriteLine6("\t\t\tThe current ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        oSpinning.clock_angle_stop = 3.21
        self.m_logger.WriteLine6("\t\t\tThe new ClockAngleStop is: {0}", oSpinning.clock_angle_stop)
        Assert.assertEqual(3.21, oSpinning.clock_angle_stop)
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 56
        with pytest.raises(Exception):
            oSpinning.clock_angle_start = 5.6
        with pytest.raises(Exception):
            oSpinning.clock_angle_stop = 0.56
        with pytest.raises(Exception):
            oSpinning.set_clock_angles(5, 3)
        # SetClockAngles
        oSpinning.set_clock_angles(3, 5)
        Assert.assertEqual(3, oSpinning.clock_angle_start)
        Assert.assertEqual(5, oSpinning.clock_angle_stop)
        # SpinRate
        self.m_logger.WriteLine6("\t\t\tThe current SpinRate is: {0}", oSpinning.spin_rate)
        oSpinning.spin_rate = 98.7654321
        self.m_logger.WriteLine6("\t\t\tThe new SpinRate is: {0}", oSpinning.spin_rate)
        Assert.assertAlmostEqual(98.7654321, oSpinning.spin_rate, delta=1e-07)
        with pytest.raises(Exception):
            oSpinning.spin_rate = 3400000000000000000000000000000000000000000000000000000000.0
        # OffsetAngle
        self.m_logger.WriteLine6("\t\t\tThe current OffsetAngle is: {0}", oSpinning.offset_angle)
        oSpinning.offset_angle = 0.123
        self.m_logger.WriteLine6("\t\t\tThe new OffsetAngle is: {0}", oSpinning.offset_angle)
        Assert.assertEqual(0.123, oSpinning.offset_angle)
        with pytest.raises(Exception):
            oSpinning.offset_angle = 12.34
        # SpinAxisAzimuth
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        oSpinning.spin_axis_azimuth = -0.123
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisAzimuth is: {0}", oSpinning.spin_axis_azimuth)
        if (eType == STK_OBJECT_TYPE.FACILITY) or (eType == STK_OBJECT_TYPE.TARGET):
            Assert.assertAlmostEqual(6.16, float(oSpinning.spin_axis_azimuth), delta=0.001)
        else:
            Assert.assertAlmostEqual(-0.123, float(oSpinning.spin_axis_azimuth), delta=0.001)
        with pytest.raises(Exception):
            oSpinning.spin_axis_azimuth = 12.34
        # SpinAxisElevation
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        oSpinning.spin_axis_elevation = 1.23
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisElevation is: {0}", oSpinning.spin_axis_elevation)
        Assert.assertEqual(1.23, oSpinning.spin_axis_elevation)
        with pytest.raises(Exception):
            oSpinning.spin_axis_elevation = 12.34
        # SpinAxisConeAngle
        self.m_logger.WriteLine6("\t\t\tThe current SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        oSpinning.spin_axis_cone_angle = 2.3
        self.m_logger.WriteLine6("\t\t\tThe new SpinAxisConeAngle is: {0}", oSpinning.spin_axis_cone_angle)
        Assert.assertEqual(2.3, oSpinning.spin_axis_cone_angle)
        with pytest.raises(Exception):
            oSpinning.spin_axis_cone_angle = 12.34
        # endregion

        # endregion

        # region POINT_TARGETED
        # SetPointingType(POINT_TARGETED)
        self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_TARGETED)
        self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
        Assert.assertEqual(SENSOR_POINTING.POINT_TARGETED, self.m_oSensor.pointing_type)
        # Pointing
        oTarget: "SensorPointingTargeted" = SensorPointingTargeted(self.m_oSensor.pointing)
        Assert.assertIsNotNone(oTarget)

        # region Boresight
        # Boresight (TRACKING)
        self.m_logger.WriteLine6("\t\tThe current Boresight is: {0}", oTarget.boresight)
        oTarget.boresight = SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.TRACKING
        self.m_logger.WriteLine6("\t\tThe new Boresight is: {0}", oTarget.boresight)
        Assert.assertEqual(SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.TRACKING, oTarget.boresight)
        # BoresightData
        oTracking: "SensorPointingTargetedBoresightTrack" = SensorPointingTargetedBoresightTrack(oTarget.boresight_data)
        Assert.assertIsNotNone(oTracking)
        # AboutBoresight
        self.m_logger.WriteLine6("\t\t\tThe current AboutBoresight is: {0}", oTracking.about_boresight)
        oTracking.about_boresight = BORESIGHT_TYPE.HOLD
        self.m_logger.WriteLine6("\t\t\tThe new AboutBoresight is: {0}", oTracking.about_boresight)
        Assert.assertEqual(BORESIGHT_TYPE.HOLD, oTracking.about_boresight)
        oTracking.about_boresight = BORESIGHT_TYPE.LEVEL
        self.m_logger.WriteLine6("\t\t\tThe new AboutBoresight is: {0}", oTracking.about_boresight)
        Assert.assertEqual(BORESIGHT_TYPE.LEVEL, oTracking.about_boresight)
        oTracking.about_boresight = BORESIGHT_TYPE.ROTATE
        self.m_logger.WriteLine6("\t\t\tThe new AboutBoresight is: {0}", oTracking.about_boresight)
        Assert.assertEqual(BORESIGHT_TYPE.ROTATE, oTracking.about_boresight)
        # TrackMode
        self.m_logger.WriteLine6("\t\t\tThe current TrackMode is: {0}", oTracking.track_mode)
        oTracking.track_mode = TRACK_MODE_TYPE.RECEIVE
        self.m_logger.WriteLine6("\t\t\tThe new TrackMode is: {0}", oTracking.track_mode)
        Assert.assertEqual(TRACK_MODE_TYPE.RECEIVE, oTracking.track_mode)
        oTracking.track_mode = TRACK_MODE_TYPE.TRANSMIT
        self.m_logger.WriteLine6("\t\t\tThe new TrackMode is: {0}", oTracking.track_mode)
        Assert.assertEqual(TRACK_MODE_TYPE.TRANSMIT, oTracking.track_mode)
        oTracking.track_mode = TRACK_MODE_TYPE.TRANSPOND
        self.m_logger.WriteLine6("\t\t\tThe new TrackMode is: {0}", oTracking.track_mode)
        Assert.assertEqual(TRACK_MODE_TYPE.TRANSPOND, oTracking.track_mode)

        # Boresight (FIXED)
        oTarget.boresight = SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.FIXED
        self.m_logger.WriteLine6("\t\tThe new Boresight is: {0}", oTarget.boresight)
        Assert.assertEqual(SENSOR_POINTING_TARGETED_BORESIGHT_TYPE.FIXED, oTarget.boresight)
        # BoresightData
        oBrstFixed: "SensorPointingTargetedBoresightFixed" = SensorPointingTargetedBoresightFixed(
            oTarget.boresight_data
        )
        Assert.assertIsNotNone(oBrstFixed)
        # Orientation
        oHelper.Run(oBrstFixed.orientation, Orientations.All)
        # endregion

        # region Targets
        # Targets
        oTargetCollection: "SensorTargetCollection" = oTarget.targets
        Assert.assertIsNotNone(oTargetCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe current TargetCollection contains: {0} elements", oTargetCollection.count)
        # _NewEnum
        target: "SensorTarget"
        # _NewEnum
        for target in oTargetCollection:
            # Name
            self.m_logger.WriteLine5("\t\tElement: {0}", target.name)

        # RemoveAll
        oTargetCollection.remove_all()
        self.m_logger.WriteLine3(
            "\t\tAfter RemoveAll() the TargetCollection contains: {0} elements", oTargetCollection.count
        )
        Assert.assertEqual(0, oTargetCollection.count)
        # EnableAccessTimes
        self.m_logger.WriteLine4("\t\tThe current EnableAccessTimes flag is: {0}", oTarget.enable_access_times)
        with pytest.raises(Exception):
            oTarget.enable_access_times = False
        # AvailableTargets
        arTargets = oTarget.available_targets
        self.m_logger.WriteLine3("\t\tThe AvailableTargets array contains: {0} elements", Array.Length(arTargets))
        if Array.Length(arTargets) > 0:
            strTarget: str = str(arTargets[0])
            self.m_logger.WriteLine7("\t\t\tElement {0}: {1}", 0, strTarget)
            oTargetCollection.add(strTarget)
            self.m_logger.WriteLine5("\t\t\t\tThe element {0} was added to the TargetCollection.", strTarget)
            Assert.assertEqual(1, oTargetCollection.count)
            # Remove
            self.m_logger.WriteLine3(
                "\t\tBefore Remove() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            oTargetCollection.remove(0)
            self.m_logger.WriteLine3(
                "\t\tAfter Remove() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            Assert.assertEqual(0, oTargetCollection.count)
            oTargetCollection.add(strTarget)
            self.m_logger.WriteLine5("\t\t\t\tThe element {0} was added to the TargetCollection.", strTarget)
            Assert.assertEqual(1, oTargetCollection.count)
            # RemoveTarget
            oTargetCollection.remove_target(oTargetCollection[0].name)
            self.m_logger.WriteLine3(
                "\t\tAfter RemoveTarget() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            Assert.assertEqual(0, oTargetCollection.count)
            # AddObject
            oObject: "IStkObject" = self.m_oRoot.current_scenario.children["NeptuneFile"]
            Assert.assertIsNotNone(oObject)
            oTargetCollection.add_object(oObject)
            self.m_logger.WriteLine3(
                "\t\tAfter AddObject() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            Assert.assertEqual(1, oTargetCollection.count)
            # RemoveObject
            oTargetCollection.remove_object(oObject)
            self.m_logger.WriteLine3(
                "\t\tAfter RemoveObject() the TargetCollection contains: {0} elements", oTargetCollection.count
            )
            Assert.assertEqual(0, oTargetCollection.count)
            oTargetCollection.add(strTarget)
            self.m_logger.WriteLine5("\t\t\t\tThe element {0} was added to the TargetCollection.", strTarget)
            Assert.assertEqual(1, oTargetCollection.count)

        # endregion

        # region AccessTimes
        # Access time
        oATH = AccessTimeHelper()
        oATH.Run(oTarget.access_times)
        # EnableAccessTimes (true)
        self.m_logger.WriteLine4("\t\tThe current EnableAccessTimes flag is: {0}", oTarget.enable_access_times)
        oTarget.enable_access_times = True
        self.m_logger.WriteLine4("\t\tThe new EnableAccessTimes flag is: {0}", oTarget.enable_access_times)
        Assert.assertEqual(True, oTarget.enable_access_times)
        # ScheduleTimes
        oScheduleTimeCollection: "ScheduleTimeCollection" = oTarget.schedule_times
        Assert.assertIsNotNone(oScheduleTimeCollection)
        oStart: typing.Any = None
        oStop: typing.Any = None
        strName: str = ""
        if oScheduleTimeCollection.count > 0:
            oStart = oScheduleTimeCollection[0].start_time
            oStop = oScheduleTimeCollection[0].stop_time
            strName = oScheduleTimeCollection[0].target
            # RemoveIndex
            with pytest.raises(Exception):
                oScheduleTimeCollection.remove_index(0)
            # Add
            with pytest.raises(Exception):
                oScheduleTimeCollection.add(oStart, oStop, strName)
            # RemoveSchedule
            with pytest.raises(Exception):
                oScheduleTimeCollection.remove_schedule(oStart, oStop, strName)
            # RemoveAll
            with pytest.raises(Exception):
                oScheduleTimeCollection.remove_all()

        # EnableAccessTimes (false)
        oTarget.enable_access_times = False
        self.m_logger.WriteLine4("\t\tThe new EnableAccessTimes flag is: {0}", oTarget.enable_access_times)
        Assert.assertEqual(False, oTarget.enable_access_times)
        # endregion

        # region ScheduleTimes
        # ScheduleTimes
        oScheduleTimeCollection = oTarget.schedule_times
        Assert.assertIsNotNone(oScheduleTimeCollection)
        # Count
        self.m_logger.WriteLine3("\t\tThe ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count)
        # _NewEnum
        scheduleTime: "ScheduleTime"
        # _NewEnum
        for scheduleTime in oScheduleTimeCollection:
            self.m_logger.WriteLine8(
                "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                scheduleTime.start_time,
                scheduleTime.stop_time,
                "Target",
            )

        # Deconflict
        oScheduleTimeCollection.deconflict()
        if oScheduleTimeCollection.count == 0:
            oScheduleTimeCollection.add("1 Jun 1999 11:00:00.000", "1 Jul 1999 12:00:00.000", oTarget.targets[0].name)
            self.m_logger.WriteLine3(
                "\t\tAfter Add() the ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count
            )
            Assert.assertEqual(1, oScheduleTimeCollection.count)
            scheduleTime: "ScheduleTime"
            for scheduleTime in oScheduleTimeCollection:
                self.m_logger.WriteLine8(
                    "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                    scheduleTime.start_time,
                    scheduleTime.stop_time,
                    scheduleTime.target,
                )

        # Item
        oStart = oScheduleTimeCollection[0].start_time
        oStop = oScheduleTimeCollection[0].stop_time
        strName = oScheduleTimeCollection[0].target
        strName = oTarget.targets[0].name
        iCount: int = oScheduleTimeCollection.count
        # RemoveIndex
        oScheduleTimeCollection.remove_index(0)
        self.m_logger.WriteLine3(
            "\t\tAfter RemoveIndex() the ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count
        )
        Assert.assertEqual((iCount - 1), oScheduleTimeCollection.count)
        scheduleTime: "ScheduleTime"
        for scheduleTime in oScheduleTimeCollection:
            self.m_logger.WriteLine8(
                "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                scheduleTime.start_time,
                scheduleTime.stop_time,
                "Target",
            )

        try:
            oScheduleTimeCollection.remove_index(-12)
            Assert.fail("Should not allow to use illegal value!")
        except AssertionError as e:
            raise e

        except Exception as e:
            self.m_logger.WriteLine5("\t\t\tExpected exception: {0}", str(e))

        # Add
        oScheduleTimeCollection.add(oStart, oStop, strName)
        self.m_logger.WriteLine3(
            "\t\tAfter Add() the ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count
        )
        Assert.assertEqual(iCount, oScheduleTimeCollection.count)
        scheduleTime: "ScheduleTime"
        for scheduleTime in oScheduleTimeCollection:
            self.m_logger.WriteLine8(
                "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                scheduleTime.start_time,
                scheduleTime.stop_time,
                "Target",
            )

        with pytest.raises(Exception):
            oScheduleTimeCollection.add(oStart, oStop, "InvalidName")
        # RemoveSchedule
        oScheduleTimeCollection.remove_schedule(oStart, oStop, strName)
        self.m_logger.WriteLine3(
            "\t\tAfter RemoveSchedule() the ScheduleTimeCollection contains: {0} elements",
            oScheduleTimeCollection.count,
        )
        Assert.assertEqual((iCount - 1), oScheduleTimeCollection.count)
        with pytest.raises(Exception):
            oScheduleTimeCollection.remove_schedule(oStart, oStop, "InvalidName")
        # RemoveAll
        oScheduleTimeCollection.remove_all()
        self.m_logger.WriteLine3(
            "\t\tAfter RemoveAll() the ScheduleTimeCollection contains: {0} elements", oScheduleTimeCollection.count
        )
        Assert.assertEqual(0, oScheduleTimeCollection.count)
        # Add
        oStart = "1 Jun 2004 12:00:00.000"
        oStop = "1 Jun 2004 15:00:00.000"
        strName = oTarget.targets[0].name
        oScheduleTime: "ScheduleTime" = oScheduleTimeCollection.add(oStart, oStop, strName)
        Assert.assertIsNotNone(oScheduleTime)
        Assert.assertEqual(oStart, oScheduleTime.start_time)
        Assert.assertEqual(oStop, oScheduleTime.stop_time)
        Assert.assertEqual(strName, oScheduleTime.target)
        Assert.assertEqual(1, oScheduleTimeCollection.count)
        scheduleTime: "ScheduleTime"
        for scheduleTime in oScheduleTimeCollection:
            self.m_logger.WriteLine8(
                "\t\t\tElement: Target = {2}, StartTime = {0}, StopTime = {1}",
                scheduleTime.start_time,
                scheduleTime.stop_time,
                scheduleTime.target,
            )

        # StopTime
        oScheduleTime.stop_time = oStop
        Assert.assertEqual(oStop, oScheduleTime.stop_time)
        with pytest.raises(Exception):
            oScheduleTime.stop_time = "1 Jun 2004 09:00:00.000"
        # StartTime
        oScheduleTime.start_time = oStart
        Assert.assertEqual(oStart, oScheduleTime.start_time)
        with pytest.raises(Exception):
            oScheduleTime.start_time = "1 Jun 2004 18:00:00.000"
        # Target
        oScheduleTime.target = strName
        Assert.assertEqual(strName, oScheduleTime.target)
        with pytest.raises(Exception):
            oScheduleTime.target = "InvalidName"
        # Add
        with pytest.raises(Exception):
            oScheduleTimeCollection.add("1 Jun 2004 12:00:00.00", "1 Jun 2004 11:00:00.00", "Star/Star1")
        # endregion

        # region Advanced
        # Advanced
        oAdvanced: "SensorAccessAdvanced" = oTarget.advanced
        Assert.assertIsNotNone(oAdvanced)
        # AberrationType
        self.m_logger.WriteLine6("\tThe current AberrationType is: {0}", oAdvanced.aberration_type)
        (oAdvanced).aberration_type = ABERRATION_TYPE.ANNUAL
        self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
        Assert.assertEqual(ABERRATION_TYPE.ANNUAL, oAdvanced.aberration_type)
        (oAdvanced).aberration_type = ABERRATION_TYPE.NONE
        self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
        Assert.assertEqual(ABERRATION_TYPE.NONE, oAdvanced.aberration_type)
        (oAdvanced).aberration_type = ABERRATION_TYPE.TOTAL
        self.m_logger.WriteLine6("\tThe new AberrationType is: {0}", oAdvanced.aberration_type)
        Assert.assertEqual(ABERRATION_TYPE.TOTAL, oAdvanced.aberration_type)
        with pytest.raises(Exception):
            (oAdvanced).aberration_type = ABERRATION_TYPE.UNKNOWN
        # TimeDelayConvergence
        self.m_logger.WriteLine6("\tThe current TimeDelayConvergence is: {0}", oAdvanced.time_delay_convergence)
        oAdvanced.time_delay_convergence = 0.1
        self.m_logger.WriteLine6("\tThe new TimeDelayConvergence is: {0}", oAdvanced.time_delay_convergence)
        Assert.assertEqual(0.1, oAdvanced.time_delay_convergence)
        with pytest.raises(Exception):
            oAdvanced.time_delay_convergence = 0.5
        # EventDetection
        oEDHelper = AccessEventDetectionHelper()
        oEDHelper.Run(oAdvanced.event_detection, False)
        # Sampling
        oSHelper = AccessSamplingHelper()
        oSHelper.Run(oAdvanced.sampling, False)
        # endregion

        # endregion

        # region POINT_GRAZING_ALTITUDE
        # SetPointingType(POINT_GRAZING_ALTITUDE)
        try:
            self.m_oSensor.set_pointing_type(SENSOR_POINTING.POINT_GRAZING_ALTITUDE)
            self.m_logger.WriteLine6("\tThe new PointingType is: {0}", self.m_oSensor.pointing_type)
            Assert.assertEqual(SENSOR_POINTING.POINT_GRAZING_ALTITUDE, self.m_oSensor.pointing_type)
            # Pointing
            oGrazing: "SensorPointingGrazingAltitude" = SensorPointingGrazingAltitude(self.m_oSensor.pointing)
            Assert.assertIsNotNone(oGrazing)
            # AzimuthOffset
            self.m_logger.WriteLine6("\t\tThe current AzimuthOffset is: {0}", oGrazing.azimuth_offset)
            oGrazing.azimuth_offset = 3.45
            self.m_logger.WriteLine6("\t\tThe new AzimuthOffset is: {0}", oGrazing.azimuth_offset)
            Assert.assertEqual(3.45, oGrazing.azimuth_offset)
            with pytest.raises(Exception):
                oGrazing.azimuth_offset = 9.876
            # GrazingAlt
            self.m_logger.WriteLine6("\t\tThe current GrazingAlt is: {0}", oGrazing.grazing_altitude)
            oGrazing.grazing_altitude = 12345.6789
            self.m_logger.WriteLine6("\t\tThe new GrazingAlt is: {0}", oGrazing.grazing_altitude)
            Assert.assertEqual(12345.6789, oGrazing.grazing_altitude)
            with pytest.raises(Exception):
                oGrazing.grazing_altitude = -9.876

        except Exception as e:
            self.m_logger.WriteLine5("\tExpected exception: {0}", str(e))

        # endregion

        # restore Units
        self.m_oRoot.unit_preferences.reset_units()
        self.m_logger.WriteLine("----- THE BASIC COARSE POINTING TEST ----- END -----")

    # endregion

    # region GraphicsProjectionConstantAlt
    def GraphicsProjectionConstantAlt(self, oConstantAlt: "SensorProjectionConstantAltitude", bReadOnly: bool):
        Assert.assertIsNotNone(oConstantAlt)
        # set DistanceUnit
        strDistanceUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit format is: {0}", strDistanceUnit)
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", "ft")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"),
        )
        Assert.assertEqual("ft", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))
        if bReadOnly:
            # Min
            self.m_logger.WriteLine6("\t\t\tThe current Min is: {0}", oConstantAlt.min)
            with pytest.raises(Exception):
                oConstantAlt.min = 1234.56789
            # Max
            self.m_logger.WriteLine6("\t\t\tThe current Max is: {0}", oConstantAlt.max)
            with pytest.raises(Exception):
                oConstantAlt.max = 9876.54321
            # NumberOfSteps
            self.m_logger.WriteLine3("\t\t\tThe current NumberOfSteps is: {0}", oConstantAlt.number_of_steps)
            with pytest.raises(Exception):
                oConstantAlt.number_of_steps = 21

        else:
            # Min
            self.m_logger.WriteLine6("\t\t\tThe current Min is: {0}", oConstantAlt.min)
            oConstantAlt.min = 123.456789
            self.m_logger.WriteLine6("\t\t\tThe new Min is: {0}", oConstantAlt.min)
            Assert.assertEqual(123.456789, oConstantAlt.min)
            with pytest.raises(Exception):
                oConstantAlt.min = -3380.84
            # Max
            self.m_logger.WriteLine6("\t\t\tThe current Max is: {0}", oConstantAlt.max)
            oConstantAlt.max = 987.654321
            self.m_logger.WriteLine6("\t\t\tThe new Max is: {0}", oConstantAlt.max)
            Assert.assertAlmostEqual(987.654321, oConstantAlt.max, delta=1e-07)
            with pytest.raises(Exception):
                oConstantAlt.max = 3380840000000000000000.0
            with pytest.raises(Exception):
                oConstantAlt.max = 12.3456
            with pytest.raises(Exception):
                oConstantAlt.min = 1234.56
            # NumberOfSteps
            self.m_logger.WriteLine3("\t\t\tThe current NumberOfSteps is: {0}", oConstantAlt.number_of_steps)
            oConstantAlt.number_of_steps = 1
            self.m_logger.WriteLine3("\t\t\tThe new NumberOfSteps is: {0}", oConstantAlt.number_of_steps)
            Assert.assertEqual(1, oConstantAlt.number_of_steps)
            with pytest.raises(Exception):
                oConstantAlt.number_of_steps = 1234
            # ProjectsThruCrossing
            self.m_logger.WriteLine4(
                "\t\t\tThe current ProjectsThruCrossing is: {0}", oConstantAlt.projects_thru_crossing
            )
            oConstantAlt.projects_thru_crossing = False
            self.m_logger.WriteLine4("\t\t\tThe new ProjectsThruCrossing is: {0}", oConstantAlt.projects_thru_crossing)
            Assert.assertEqual(False, oConstantAlt.projects_thru_crossing)
            oConstantAlt.projects_thru_crossing = True
            self.m_logger.WriteLine4("\t\t\tThe new ProjectsThruCrossing is: {0}", oConstantAlt.projects_thru_crossing)
            Assert.assertEqual(True, oConstantAlt.projects_thru_crossing)
            # AltCrossingSides (ALTITUDE_CROSSING_ONE_SIDE)
            self.m_logger.WriteLine6("\t\t\tThe current AltCrossingSides is: {0}", oConstantAlt.altitude_crossing_sides)
            oConstantAlt.altitude_crossing_sides = SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_ONE_SIDE
            self.m_logger.WriteLine6("\t\t\tThe new AltCrossingSides is: {0}", oConstantAlt.altitude_crossing_sides)
            Assert.assertEqual(
                SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_ONE_SIDE, oConstantAlt.altitude_crossing_sides
            )
            # AltCrossingSides (ALTITUDE_CROSSING_BOTH_SIDES)
            self.m_logger.WriteLine6("\t\t\tThe current AltCrossingSides is: {0}", oConstantAlt.altitude_crossing_sides)
            oConstantAlt.altitude_crossing_sides = SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_BOTH_SIDES
            self.m_logger.WriteLine6("\t\t\tThe new AltCrossingSides is: {0}", oConstantAlt.altitude_crossing_sides)
            Assert.assertEqual(
                SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_BOTH_SIDES, oConstantAlt.altitude_crossing_sides
            )
            # AltCrossingSides (ALTITUDE_CROSSING_UNKNOWN)
            with pytest.raises(Exception):
                oConstantAlt.altitude_crossing_sides = SENSOR_ALTITUDE_CROSSING_SIDES.ALTITUDE_CROSSING_UNKNOWN
            # Direction (DIRECTION_EITHER)
            self.m_logger.WriteLine6("\t\t\tThe current Direction is: {0}", oConstantAlt.direction)
            oConstantAlt.direction = SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_EITHER
            self.m_logger.WriteLine6("\t\t\tThe new Direction is: {0}", oConstantAlt.direction)
            Assert.assertEqual(SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_EITHER, oConstantAlt.direction)
            # Direction (DIRECTION_INSIDE_OUT)
            self.m_logger.WriteLine6("\t\t\tThe current Direction is: {0}", oConstantAlt.direction)
            oConstantAlt.direction = SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_INSIDE_OUT
            self.m_logger.WriteLine6("\t\t\tThe new Direction is: {0}", oConstantAlt.direction)
            Assert.assertEqual(SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_INSIDE_OUT, oConstantAlt.direction)
            # Direction (DIRECTION_OUTSIDE_IN)
            self.m_logger.WriteLine6("\t\t\tThe current Direction is: {0}", oConstantAlt.direction)
            oConstantAlt.direction = SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_OUTSIDE_IN
            self.m_logger.WriteLine6("\t\t\tThe new Direction is: {0}", oConstantAlt.direction)
            Assert.assertEqual(SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_OUTSIDE_IN, oConstantAlt.direction)
            # Direction (DIRECTION_UNKNOWN)
            with pytest.raises(Exception):
                oConstantAlt.direction = SENSOR_ALTITUDE_CROSSING_DIRECTION.DIRECTION_UNKNOWN
            # ExcludeHorizonArcs
            self.m_logger.WriteLine4("\t\t\tThe current ExcludeHorizonArcs is: {0}", oConstantAlt.exclude_horizon_arcs)
            oConstantAlt.exclude_horizon_arcs = False
            self.m_logger.WriteLine4("\t\t\tThe new ExcludeHorizonArcs is: {0}", oConstantAlt.exclude_horizon_arcs)
            Assert.assertEqual(False, oConstantAlt.exclude_horizon_arcs)
            oConstantAlt.exclude_horizon_arcs = True
            self.m_logger.WriteLine4("\t\t\tThe new ExcludeHorizonArcs is: {0}", oConstantAlt.exclude_horizon_arcs)
            Assert.assertEqual(True, oConstantAlt.exclude_horizon_arcs)

        # restore DistanceUnit
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\t\tThe restored DistanceUnit format is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    # region GraphicsProjectionObjectAlt
    def GraphicsProjectionObjectAlt(self, oObjectAlt: "SensorProjectionObjectAltitude"):
        Assert.assertIsNotNone(oObjectAlt)
        # set DistanceUnit
        strDistanceUnit: str = self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit")
        self.m_logger.WriteLine5("\t\t\tThe current DistanceUnit format is: {0}", strDistanceUnit)
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", "ft")
        self.m_logger.WriteLine5(
            "\t\t\tThe new DistanceUnit format is: {0}",
            self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"),
        )
        Assert.assertEqual("ft", self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))

        # ExcludeHorizonArcs
        self.m_logger.WriteLine4("\t\t\tThe current ExcludeHorizonArcs is: {0}", oObjectAlt.exclude_horizon_arcs)
        oObjectAlt.exclude_horizon_arcs = False
        self.m_logger.WriteLine4("\t\t\tThe new ExcludeHorizonArcs is: {0}", oObjectAlt.exclude_horizon_arcs)
        Assert.assertEqual(False, oObjectAlt.exclude_horizon_arcs)
        oObjectAlt.exclude_horizon_arcs = True
        self.m_logger.WriteLine4("\t\t\tThe new ExcludeHorizonArcs is: {0}", oObjectAlt.exclude_horizon_arcs)
        Assert.assertEqual(True, oObjectAlt.exclude_horizon_arcs)

        # restore DistanceUnit
        self.m_oRoot.unit_preferences.set_current_unit("DistanceUnit", strDistanceUnit)
        self.m_logger.WriteLine5("\t\tThe restored DistanceUnit format is: {0}", strDistanceUnit)
        Assert.assertEqual(strDistanceUnit, self.m_oRoot.unit_preferences.get_current_unit_abbrv("DistanceUnit"))

    # endregion

    def SpatialInfo(self):
        helper = SpatialInfoHelper(self.m_oRoot)
        helper.Run(clr.CastAs(self.m_oSensor, IStkObject))


class EOIRHelper(object):
    def __init__(self, oRoot: "StkObjectRoot", testTarget):
        self.m_oRoot: "StkObjectRoot" = oRoot
        self.m_testTarget = testTarget

    # region Run method
    def Run(self):
        if self.m_oRoot.current_scenario.children.contains(STK_OBJECT_TYPE.SATELLITE, "EOIR_SAT"):
            self.m_oRoot.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "EOIR_SAT")

        objSat: "IStkObject" = self.m_oRoot.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "EOIR_SAT")
        objSen: "IStkObject" = objSat.children.new(STK_OBJECT_TYPE.SENSOR, "EOIR_SEN")

        sensor: "Sensor" = clr.CastAs(objSen, Sensor)

        sensor.set_pattern_type(SENSOR_PATTERN.EOIR)

        Assert.assertEqual(SENSOR_PATTERN.EOIR, sensor.pattern_type)
        eoirPattern: "SensorEOIRPattern" = SensorEOIRPattern(sensor.pattern)
        Assert.assertIsNotNone(eoirPattern)

        self.Test_IAgSnEOIRPattern(eoirPattern)

        # SetPatternEOIR
        objSat2: "IStkObject" = self.m_oRoot.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "EOIR_SAT2")
        objSen2: "IStkObject" = objSat.children.new(STK_OBJECT_TYPE.SENSOR, "EOIR_SEN2")
        sensor2: "Sensor" = clr.CastAs(objSen2, Sensor)

        sensor2.common_tasks.set_pattern_eoir(5, SENSOR_EOIR_PROCESSING_LEVELS.RADIOMETRIC_INPUT)
        Assert.assertEqual(SENSOR_PATTERN.EOIR, sensor2.pattern_type)
        oEOIR: "SensorEOIRPattern" = SensorEOIRPattern(sensor2.pattern)
        Assert.assertIsNotNone(oEOIR)
        Assert.assertEqual(5, oEOIR.line_of_site_jitter)
        Assert.assertEqual(SENSOR_EOIR_PROCESSING_LEVELS.RADIOMETRIC_INPUT, oEOIR.processing_level)
        if self.m_oRoot.current_scenario.children.contains(STK_OBJECT_TYPE.SATELLITE, "EOIR_SAT"):
            self.m_oRoot.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "EOIR_SAT")

        if self.m_oRoot.current_scenario.children.contains(STK_OBJECT_TYPE.SATELLITE, "EOIR_SAT2"):
            self.m_oRoot.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "EOIR_SAT2")

    # endregion

    # region EOIR Helper methods
    def Test_IAgSnEOIRPattern(self, eoirPattern: "SensorEOIRPattern"):
        self.Test_AgSnEOIRBandCollection(eoirPattern.bands)

        eoirPattern.processing_level = SENSOR_EOIR_PROCESSING_LEVELS.GEOMETRIC_INPUT
        Assert.assertEqual(SENSOR_EOIR_PROCESSING_LEVELS.GEOMETRIC_INPUT, eoirPattern.processing_level)
        eoirPattern.processing_level = SENSOR_EOIR_PROCESSING_LEVELS.RADIOMETRIC_INPUT
        Assert.assertEqual(SENSOR_EOIR_PROCESSING_LEVELS.RADIOMETRIC_INPUT, eoirPattern.processing_level)
        eoirPattern.processing_level = SENSOR_EOIR_PROCESSING_LEVELS.SENSOR_OFF
        Assert.assertEqual(SENSOR_EOIR_PROCESSING_LEVELS.SENSOR_OFF, eoirPattern.processing_level)
        eoirPattern.processing_level = SENSOR_EOIR_PROCESSING_LEVELS.SENSOR_OUTPUT
        Assert.assertEqual(SENSOR_EOIR_PROCESSING_LEVELS.SENSOR_OUTPUT, eoirPattern.processing_level)

        eoirPattern.scan_mode = SENSOR_EOIR_SCAN_MODES.FRAMING_ARRAY
        Assert.assertEqual(SENSOR_EOIR_SCAN_MODES.FRAMING_ARRAY, eoirPattern.scan_mode)

        eoirPattern.along_scan_smear_rate = -6283
        Assert.assertEqual(-6283, eoirPattern.along_scan_smear_rate)
        eoirPattern.along_scan_smear_rate = 6283
        Assert.assertEqual(6283, eoirPattern.along_scan_smear_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.along_scan_smear_rate = -6284
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.along_scan_smear_rate = 6284

        eoirPattern.across_scan_smear_rate = -785
        Assert.assertEqual(-785, eoirPattern.across_scan_smear_rate)
        eoirPattern.across_scan_smear_rate = 785
        Assert.assertEqual(785, eoirPattern.across_scan_smear_rate)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.across_scan_smear_rate = -786
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.across_scan_smear_rate = 786

        eoirPattern.use_motion_blur = True
        Assert.assertTrue(eoirPattern.use_motion_blur)
        eoirPattern.use_motion_blur = False
        Assert.assertFalse(eoirPattern.use_motion_blur)

        eoirPattern.jitter_type = SENSOR_EOIR_JITTER_TYPES.LOS_GAUSSIAN
        Assert.assertEqual(SENSOR_EOIR_JITTER_TYPES.LOS_GAUSSIAN, eoirPattern.jitter_type)

        eoirPattern.line_of_site_jitter = 0
        Assert.assertEqual(0, eoirPattern.line_of_site_jitter)
        eoirPattern.line_of_site_jitter = 785
        Assert.assertEqual(785, eoirPattern.line_of_site_jitter)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.line_of_site_jitter = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.line_of_site_jitter = 786

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.jitter_data_file = "something"
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.jitter_data_file_spatial_sampling = 100
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.jitter_data_file_frequency_sampling = 100

        eoirPattern.jitter_type = SENSOR_EOIR_JITTER_TYPES.MTF_FILE
        Assert.assertEqual(SENSOR_EOIR_JITTER_TYPES.MTF_FILE, eoirPattern.jitter_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.line_of_site_jitter = 1

        eoirPattern.jitter_data_file = "2dButterworth1Order1Width64x64.csv"
        Assert.assertEqual("2dButterworth1Order1Width64x64.csv", eoirPattern.jitter_data_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            eoirPattern.jitter_data_file = "bogus"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.jitter_data_file_spatial_sampling = 100

        eoirPattern.jitter_data_file_frequency_sampling = 0.0001
        Assert.assertEqual(0.0001, eoirPattern.jitter_data_file_frequency_sampling)
        eoirPattern.jitter_data_file_frequency_sampling = 1000000.0
        Assert.assertEqual(1000000.0, eoirPattern.jitter_data_file_frequency_sampling)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.jitter_data_file_frequency_sampling = 1e-05
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.jitter_data_file_frequency_sampling = 10000000.0

        eoirPattern.jitter_type = SENSOR_EOIR_JITTER_TYPES.PSF_FILE
        Assert.assertEqual(SENSOR_EOIR_JITTER_TYPES.PSF_FILE, eoirPattern.jitter_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.line_of_site_jitter = 1

        eoirPattern.jitter_data_file = "2dButterworth1Order2Width64x64.csv"
        Assert.assertEqual("2dButterworth1Order2Width64x64.csv", eoirPattern.jitter_data_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            eoirPattern.jitter_data_file = "bogus"

        eoirPattern.jitter_data_file_spatial_sampling = 1e-06
        Assert.assertEqual(1e-06, eoirPattern.jitter_data_file_spatial_sampling)
        eoirPattern.jitter_data_file_spatial_sampling = 10000
        Assert.assertEqual(10000, eoirPattern.jitter_data_file_spatial_sampling)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.jitter_data_file_spatial_sampling = 1e-07
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.jitter_data_file_spatial_sampling = 10001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.jitter_data_file_frequency_sampling = 100

        eoirPattern.jitter_type = SENSOR_EOIR_JITTER_TYPES.PSD_FILE
        Assert.assertEqual(SENSOR_EOIR_JITTER_TYPES.PSD_FILE, eoirPattern.jitter_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.line_of_site_jitter = 1

        eoirPattern.jitter_data_file = "2dButterworth1Order3Width64x64.csv"
        Assert.assertEqual("2dButterworth1Order3Width64x64.csv", eoirPattern.jitter_data_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            eoirPattern.jitter_data_file = "bogus"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            eoirPattern.jitter_data_file_spatial_sampling = 100

        eoirPattern.jitter_data_file_frequency_sampling = 0.0001
        Assert.assertEqual(0.0001, eoirPattern.jitter_data_file_frequency_sampling)
        eoirPattern.jitter_data_file_frequency_sampling = 1000000.0
        Assert.assertEqual(1000000.0, eoirPattern.jitter_data_file_frequency_sampling)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.jitter_data_file_frequency_sampling = 1e-05
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            eoirPattern.jitter_data_file_frequency_sampling = 10000000.0

    def Test_AgSnEOIRBandCollection(self, bandColl: "SensorEOIRBandCollection"):
        Assert.assertEqual(1, bandColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("cannot be removed")):
            bandColl.remove_at(0)

        self.Test_IAgSnEOIRBand(bandColl[0])

    def Test_IAgSnEOIRBand(self, band: "SensorEOIRBand"):
        band.render_band = False
        Assert.assertFalse(band.render_band)
        band.render_band = True
        Assert.assertTrue(band.render_band)

        band.band_name = ""
        Assert.assertEqual("", band.band_name)
        band.band_name = "Band Name Here"
        Assert.assertEqual("Band Name Here", band.band_name)

        self.Test_SpatialTab(band)
        self.Test_SpectralTab(band)
        self.Test_OpticalTab(band)
        self.Test_RadiometricTab(band)

    def Test_SpatialTab(self, band: "SensorEOIRBand"):
        band.spatial_auto_rebalance = True
        Assert.assertTrue(band.spatial_auto_rebalance)
        band.spatial_auto_rebalance = False
        Assert.assertFalse(band.spatial_auto_rebalance)

        band.spatial_input_mode = SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE.FO_VAND_PIXEL_PITCH
        Assert.assertEqual(SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE.FO_VAND_PIXEL_PITCH, band.spatial_input_mode)

        # Values change after setting as if clicking Apply in the GUI.

        band.horizontal_half_angle = 1
        Assert.assertAlmostEqual(1.343, float(band.horizontal_half_angle), delta=0.001)
        Assert.assertEqual(3.0, band.horizontal_pixels)

        band.horizontal_half_angle = 82
        Assert.assertAlmostEqual(82.002, float(band.horizontal_half_angle), delta=0.001)
        Assert.assertEqual(911.0, band.horizontal_pixels)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.horizontal_pixels = 82
        with pytest.raises(Exception, match=RegexSubstringMatch("Value would invalidate")):
            band.horizontal_half_angle = 0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("Value would invalidate")):
            band.horizontal_half_angle = 89
        band.horizontal_half_angle = 45  # back to default
        Assert.assertEqual(45, band.horizontal_half_angle)

        band.vertical_half_angle = 1
        Assert.assertAlmostEqual(1.343, float(band.vertical_half_angle), delta=0.001)
        Assert.assertEqual(3.0, band.vertical_pixels)

        band.vertical_half_angle = 82
        Assert.assertAlmostEqual(82.002, float(band.vertical_half_angle), delta=0.001)
        Assert.assertEqual(911.0, band.vertical_pixels)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.vertical_pixels = 82
        with pytest.raises(Exception, match=RegexSubstringMatch("Value would invalidate")):
            band.vertical_half_angle = 0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("Value would invalidate")):
            band.vertical_half_angle = 89.5
        band.vertical_half_angle = 45  # back to default
        Assert.assertEqual(45, band.vertical_half_angle)

        band.horizontal_pp = 300
        Assert.assertEqual(300, band.horizontal_pp)
        Assert.assertAlmostEqual(2.727, float(band.horizontal_ifov), delta=0.001)

        band.horizontal_pp = 10000
        Assert.assertEqual(10000, band.horizontal_pp)
        Assert.assertAlmostEqual(90.847, float(band.horizontal_ifov), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("Value would invalidate")):
            band.horizontal_pp = 0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("Value would invalidate")):
            band.horizontal_pp = 1000000
        band.horizontal_pp = 1718.75  # back to default

        band.vertical_pp = 300
        Assert.assertEqual(300, band.vertical_pp)
        Assert.assertAlmostEqual(2.727, float(band.vertical_ifov), delta=0.001)

        band.vertical_pp = 10000
        Assert.assertEqual(10000, band.vertical_pp)
        Assert.assertAlmostEqual(90.847, float(band.vertical_ifov), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("Value would invalidate")):
            band.vertical_pp = 0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("Value would invalidate")):
            band.vertical_pp = 1000000
        band.vertical_pp = 1718.75  # back to default

        band.spatial_input_mode = SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE.FO_VAND_NUM_PIX
        Assert.assertEqual(SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE.FO_VAND_NUM_PIX, band.spatial_input_mode)

        # Values change after setting as if clicking Apply in the GUI.

        band.horizontal_half_angle = 1
        Assert.assertAlmostEqual(1, float(band.horizontal_half_angle), delta=0.001)
        Assert.assertAlmostEqual(28.658, band.horizontal_pp, delta=0.001)
        Assert.assertAlmostEqual(0.261, band.horizontal_ifov, delta=0.001)

        band.horizontal_half_angle = 10
        Assert.assertAlmostEqual(10, float(band.horizontal_half_angle), delta=0.001)
        Assert.assertAlmostEqual(289.492, band.horizontal_pp, delta=0.001)
        Assert.assertAlmostEqual(2.632, band.horizontal_ifov, delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.horizontal_half_angle = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.horizontal_half_angle = 90

        band.vertical_half_angle = 1
        Assert.assertAlmostEqual(1, float(band.vertical_half_angle), delta=0.001)
        Assert.assertAlmostEqual(28.658, band.vertical_pp, delta=0.001)
        Assert.assertAlmostEqual(0.261, band.vertical_ifov, delta=0.001)

        band.vertical_half_angle = 10
        Assert.assertAlmostEqual(10, float(band.vertical_half_angle), delta=0.001)
        Assert.assertAlmostEqual(289.492, band.vertical_pp, delta=0.001)
        Assert.assertAlmostEqual(2.632, band.vertical_ifov, delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.vertical_half_angle = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.vertical_half_angle = 90

        band.horizontal_pixels = 1
        Assert.assertAlmostEqual(1, float(band.horizontal_pixels), delta=0.001)
        Assert.assertAlmostEqual(38791.936, band.horizontal_pp, delta=0.001)
        Assert.assertAlmostEqual(349.066, band.horizontal_ifov, delta=0.001)

        band.horizontal_pixels = 1024
        Assert.assertAlmostEqual(1024, float(band.horizontal_pixels), delta=0.001)
        Assert.assertAlmostEqual(37.883, band.horizontal_pp, delta=0.001)
        Assert.assertAlmostEqual(0.344, band.horizontal_ifov, delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.horizontal_pixels = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.horizontal_pixels = 6001

        band.vertical_pixels = 1
        Assert.assertAlmostEqual(1, float(band.vertical_pixels), delta=0.001)
        Assert.assertAlmostEqual(38791.936, band.vertical_pp, delta=0.001)
        Assert.assertAlmostEqual(349.066, band.vertical_ifov, delta=0.001)

        band.vertical_pixels = 1024
        Assert.assertAlmostEqual(1024, float(band.vertical_pixels), delta=0.001)
        Assert.assertAlmostEqual(37.883, band.vertical_pp, delta=0.001)
        Assert.assertAlmostEqual(0.344, band.vertical_ifov, delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.vertical_pixels = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.vertical_pixels = 6001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.horizontal_pp = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.vertical_pp = 1000000000000.0

        band.spatial_input_mode = SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE.NUM_PIX_AND_PIXEL_PITCH
        Assert.assertEqual(SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE.NUM_PIX_AND_PIXEL_PITCH, band.spatial_input_mode)

        band.horizontal_pixels = 1
        Assert.assertAlmostEqual(1, float(band.horizontal_pixels), delta=0.001)
        Assert.assertAlmostEqual(0.01, float(band.horizontal_half_angle), delta=0.001)

        band.horizontal_pixels = 1024
        Assert.assertAlmostEqual(1024, float(band.horizontal_pixels), delta=0.001)
        Assert.assertAlmostEqual(10, float(band.horizontal_half_angle), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.horizontal_pixels = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.horizontal_pixels = 6001

        band.vertical_pixels = 1
        Assert.assertAlmostEqual(1, float(band.vertical_pixels), delta=0.001)
        Assert.assertAlmostEqual(0.01, float(band.vertical_half_angle), delta=0.001)

        band.vertical_pixels = 1024
        Assert.assertAlmostEqual(1024, float(band.vertical_pixels), delta=0.001)
        Assert.assertAlmostEqual(10, float(band.vertical_half_angle), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.vertical_pixels = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.vertical_pixels = 6001

        band.horizontal_pp = 1
        Assert.assertAlmostEqual(1, float(band.horizontal_pp), delta=0.001)
        Assert.assertAlmostEqual(0.009, float(band.horizontal_ifov), delta=0.001)

        band.horizontal_pp = 1000
        Assert.assertAlmostEqual(1000, float(band.horizontal_pp), delta=0.001)
        Assert.assertAlmostEqual(9.091, float(band.horizontal_ifov), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.horizontal_pp = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.horizontal_pp = 1000000000000.0

        band.vertical_pp = 1
        Assert.assertAlmostEqual(1, float(band.vertical_pp), delta=0.001)
        Assert.assertAlmostEqual(0.009, float(band.vertical_ifov), delta=0.001)

        band.vertical_pp = 1000
        Assert.assertAlmostEqual(1000, float(band.vertical_pp), delta=0.001)
        Assert.assertAlmostEqual(9.091, float(band.vertical_ifov), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.vertical_pp = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.vertical_pp = 1000000000000.0

        Assert.assertAlmostEqual(77.875, float(band.horizontal_half_angle), delta=0.001)
        Assert.assertAlmostEqual(77.875, float(band.vertical_half_angle), delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            band.horizontal_half_angle = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            band.vertical_half_angle = 1000000000000.0

    def Test_SpectralTab(self, band: "SensorEOIRBand"):
        holdLowBandEdgeWL: float = band.low_band_edge_wl
        holdHighBandEdgeWL: float = band.high_band_edge_wl

        band.low_band_edge_wl = 0.28
        Assert.assertEqual(0.28, band.low_band_edge_wl)
        band.low_band_edge_wl = 0.699  # max because HighBandEdgeWL is 0.7
        Assert.assertEqual(0.699, band.low_band_edge_wl)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.low_band_edge_wl = 0.27
        with pytest.raises(Exception, match=RegexSubstringMatch("Value is within")):
            band.low_band_edge_wl = 0.6991
        with pytest.raises(Exception, match=RegexSubstringMatch("by at least 1 nanometer")):
            band.low_band_edge_wl = 0.71

        band.high_band_edge_wl = 0.7  # because Low is 0.699
        Assert.assertEqual(0.7, band.high_band_edge_wl)
        band.high_band_edge_wl = 28
        Assert.assertEqual(28, band.high_band_edge_wl)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.high_band_edge_wl = 28.001
        with pytest.raises(Exception, match=RegexSubstringMatch("Value is within")):
            band.high_band_edge_wl = 0.6991
        with pytest.raises(Exception, match=RegexSubstringMatch("by at least 1 nanometer")):
            band.high_band_edge_wl = 0.6

        band.num_intervals = 1
        Assert.assertEqual(1, band.num_intervals)
        band.num_intervals = 1000000
        Assert.assertEqual(1000000, band.num_intervals)
        band.num_intervals = 6
        Assert.assertEqual(6, band.num_intervals)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.num_intervals = 0

        band.spectral_shape = SENSOR_EOIR_BAND_SPECTRAL_SHAPE.PROVIDE_RSR
        Assert.assertEqual(SENSOR_EOIR_BAND_SPECTRAL_SHAPE.PROVIDE_RSR, band.spectral_shape)

        band.system_relative_spectral_response_file = "SWIR_RSR.srf"
        Assert.assertEqual("SWIR_RSR.srf", band.system_relative_spectral_response_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            band.system_relative_spectral_response_file = "bogus.srf"

        band.rsr_units = SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS.ENERGY_UNITS
        Assert.assertEqual(SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS.ENERGY_UNITS, band.rsr_units)
        band.rsr_units = SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS.QUANTA_UNITS
        Assert.assertEqual(SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS.QUANTA_UNITS, band.rsr_units)

        band.spectral_shape = SENSOR_EOIR_BAND_SPECTRAL_SHAPE.DEFAULT
        Assert.assertEqual(SENSOR_EOIR_BAND_SPECTRAL_SHAPE.DEFAULT, band.spectral_shape)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.system_relative_spectral_response_file = "SWIR_RSR.srf"
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.rsr_units = SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS.ENERGY_UNITS

        band.low_band_edge_wl = holdLowBandEdgeWL
        band.high_band_edge_wl = holdHighBandEdgeWL

    def Test_OpticalTab(self, band: "SensorEOIRBand"):
        band.optical_auto_rebalance = True
        Assert.assertTrue(band.optical_auto_rebalance)
        band.optical_auto_rebalance = False
        Assert.assertFalse(band.optical_auto_rebalance)

        band.optical_input_mode = SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE.F_NUMBER_AND_APERTURE_DIAMETER
        Assert.assertEqual(SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE.F_NUMBER_AND_APERTURE_DIAMETER, band.optical_input_mode)

        band.fnumber = 1
        Assert.assertEqual(1, band.fnumber)
        band.fnumber = 10000
        Assert.assertEqual(10000, band.fnumber)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.fnumber = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.fnumber = 10000000.0
        band.fnumber = 2

        band.entrance_p_dia = 1
        Assert.assertEqual(1, band.entrance_p_dia)
        band.entrance_p_dia = 10000
        Assert.assertEqual(10000, band.entrance_p_dia)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.entrance_p_dia = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.entrance_p_dia = 10000000
        band.entrance_p_dia = 5.5

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.eff_focal_l = 1

        band.optical_input_mode = SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE.F_NUMBER_AND_FOCAL_LENGTH
        Assert.assertEqual(SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE.F_NUMBER_AND_FOCAL_LENGTH, band.optical_input_mode)

        band.fnumber = 1
        Assert.assertEqual(1, band.fnumber)
        band.fnumber = 10000
        Assert.assertEqual(10000, band.fnumber)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.fnumber = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.fnumber = 10000000.0
        band.fnumber = 2

        band.eff_focal_l = 10
        Assert.assertEqual(10, band.eff_focal_l)
        band.eff_focal_l = 1000
        Assert.assertEqual(1000, band.eff_focal_l)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.eff_focal_l = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("would invalidate")):
            band.eff_focal_l = 100000000.0
        band.eff_focal_l = 11

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.entrance_p_dia = 0.001

        band.optical_input_mode = SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE.FOCAL_LENGTH_AND_APERTURE_DIAMETER
        Assert.assertEqual(
            SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE.FOCAL_LENGTH_AND_APERTURE_DIAMETER, band.optical_input_mode
        )

        band.eff_focal_l = 10
        Assert.assertEqual(10, band.eff_focal_l)
        band.eff_focal_l = 1000
        Assert.assertEqual(1000, band.eff_focal_l)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.eff_focal_l = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("would invalidate")):
            band.eff_focal_l = 100000000.0
        band.eff_focal_l = 11

        band.entrance_p_dia = 1
        Assert.assertEqual(1, band.entrance_p_dia)
        band.entrance_p_dia = 10000
        Assert.assertEqual(10000, band.entrance_p_dia)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.entrance_p_dia = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.entrance_p_dia = 1000000
        band.entrance_p_dia = 5.5

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.fnumber = 0.01

        # IMAGE QUALITY

        band.image_quality = SENSOR_EOIR_BAND_IMAGE_QUALITY.CUSTOM_MTF
        Assert.assertEqual(SENSOR_EOIR_BAND_IMAGE_QUALITY.CUSTOM_MTF, band.image_quality)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.rms_wavefront_error = 0

        band.optical_quality_data_file = "2dButterworth1Order1Width64x64.csv"
        Assert.assertEqual("2dButterworth1Order1Width64x64.csv", band.optical_quality_data_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            band.optical_quality_data_file = "bogus"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_spatial_sampling = 5

        band.optical_quality_data_file_frequency_sampling = 1e-06
        Assert.assertEqual(1e-06, band.optical_quality_data_file_frequency_sampling)
        band.optical_quality_data_file_frequency_sampling = 1000
        Assert.assertEqual(1000, band.optical_quality_data_file_frequency_sampling)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.optical_quality_data_file_frequency_sampling = 1e-07
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.optical_quality_data_file_frequency_sampling = 1001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.long_d_focus = 0

        band.image_quality = SENSOR_EOIR_BAND_IMAGE_QUALITY.CUSTOM_PSF
        Assert.assertEqual(SENSOR_EOIR_BAND_IMAGE_QUALITY.CUSTOM_PSF, band.image_quality)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.rms_wavefront_error = 0

        band.optical_quality_data_file = "2dButterworth1Order1Width64x64.csv"
        Assert.assertEqual("2dButterworth1Order1Width64x64.csv", band.optical_quality_data_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            band.optical_quality_data_file = "bogus"

        band.optical_quality_data_file_spatial_sampling = 0.001
        Assert.assertEqual(0.001, band.optical_quality_data_file_spatial_sampling)
        band.optical_quality_data_file_spatial_sampling = 1000000.0
        Assert.assertEqual(1000000.0, band.optical_quality_data_file_spatial_sampling)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.optical_quality_data_file_spatial_sampling = 0.0001
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.optical_quality_data_file_spatial_sampling = 1000001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_frequency_sampling = 0.0001

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.long_d_focus = 0

        band.image_quality = SENSOR_EOIR_BAND_IMAGE_QUALITY.CUSTOM_WAVEFRONT_ERROR
        Assert.assertEqual(SENSOR_EOIR_BAND_IMAGE_QUALITY.CUSTOM_WAVEFRONT_ERROR, band.image_quality)

        band.rms_wavefront_error = 0
        Assert.assertEqual(0, band.rms_wavefront_error)
        band.rms_wavefront_error = 0.75
        Assert.assertEqual(0.75, band.rms_wavefront_error)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.rms_wavefront_error = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.rms_wavefront_error = 0.8

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file = "2dButterworth1Order1Width64x64.csv"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_spatial_sampling = 0.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_frequency_sampling = 0.0001

        band.long_d_focus = 0
        Assert.assertEqual(0, band.long_d_focus)
        band.long_d_focus = 10
        Assert.assertEqual(10, band.long_d_focus)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = 11

        band.image_quality = SENSOR_EOIR_BAND_IMAGE_QUALITY.DIFFRACTION_LIMITED
        Assert.assertEqual(SENSOR_EOIR_BAND_IMAGE_QUALITY.DIFFRACTION_LIMITED, band.image_quality)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.rms_wavefront_error = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file = "2dButterworth1Order1Width64x64.csv"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_spatial_sampling = 0.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_frequency_sampling = 0.0001

        band.long_d_focus = 0
        Assert.assertEqual(0, band.long_d_focus)
        band.long_d_focus = 10
        Assert.assertEqual(10, band.long_d_focus)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = 11

        band.image_quality = SENSOR_EOIR_BAND_IMAGE_QUALITY.MILD_ABERRATIONS
        Assert.assertEqual(SENSOR_EOIR_BAND_IMAGE_QUALITY.MILD_ABERRATIONS, band.image_quality)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.rms_wavefront_error = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file = "2dButterworth1Order1Width64x64.csv"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_spatial_sampling = 0.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_frequency_sampling = 0.0001

        band.long_d_focus = 0
        Assert.assertEqual(0, band.long_d_focus)
        band.long_d_focus = 10
        Assert.assertEqual(10, band.long_d_focus)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = 11

        band.image_quality = SENSOR_EOIR_BAND_IMAGE_QUALITY.MODERATE_ABERRATIONS
        Assert.assertEqual(SENSOR_EOIR_BAND_IMAGE_QUALITY.MODERATE_ABERRATIONS, band.image_quality)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.rms_wavefront_error = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file = "2dButterworth1Order1Width64x64.csv"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_spatial_sampling = 0.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_frequency_sampling = 0.0001

        band.long_d_focus = 0
        Assert.assertEqual(0, band.long_d_focus)
        band.long_d_focus = 10
        Assert.assertEqual(10, band.long_d_focus)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = 11

        band.image_quality = SENSOR_EOIR_BAND_IMAGE_QUALITY.NEGLIGIBLE_ABERRATIONS
        Assert.assertEqual(SENSOR_EOIR_BAND_IMAGE_QUALITY.NEGLIGIBLE_ABERRATIONS, band.image_quality)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.rms_wavefront_error = 0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file = "2dButterworth1Order1Width64x64.csv"

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_spatial_sampling = 0.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_quality_data_file_frequency_sampling = 0.0001

        band.long_d_focus = 0
        Assert.assertEqual(0, band.long_d_focus)
        band.long_d_focus = 10
        Assert.assertEqual(10, band.long_d_focus)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.long_d_focus = 11

        # OPTICAL TRANSMISSION

        band.optical_transmission_mode = SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE.BAND_EFFECTIVE_TRANSMISSION
        Assert.assertEqual(
            SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE.BAND_EFFECTIVE_TRANSMISSION, band.optical_transmission_mode
        )

        band.optical_transmission = 1e-06
        Assert.assertEqual(1e-06, band.optical_transmission)
        band.optical_transmission = 1.0
        Assert.assertEqual(1.0, band.optical_transmission)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.optical_transmission = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.optical_transmission = 1.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_transmission_spectral_response_file = "Mirror_Trans.srf"

        band.optical_transmission_mode = SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE.TRANSMISSION_DATA_FILE
        Assert.assertEqual(
            SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE.TRANSMISSION_DATA_FILE, band.optical_transmission_mode
        )

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.optical_transmission = 0

        band.optical_transmission_spectral_response_file = "Mirror_Trans.srf"
        Assert.assertEqual("Mirror_Trans.srf", band.optical_transmission_spectral_response_file)
        with pytest.raises(Exception, match=RegexSubstringMatch("does not exist")):
            band.optical_transmission_spectral_response_file = "bogus"

        # DIFFRACTION WAVELENGTH

        band.wavelength_type = SENSOR_EOIR_BAND_WAVELENGTH_TYPE.BAND_CENTER
        Assert.assertEqual(SENSOR_EOIR_BAND_WAVELENGTH_TYPE.BAND_CENTER, band.wavelength_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.wavelength = 1

        band.wavelength_type = SENSOR_EOIR_BAND_WAVELENGTH_TYPE.HIGH_BAND_EDGE
        Assert.assertEqual(SENSOR_EOIR_BAND_WAVELENGTH_TYPE.HIGH_BAND_EDGE, band.wavelength_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.wavelength = 1

        band.wavelength_type = SENSOR_EOIR_BAND_WAVELENGTH_TYPE.LOW_BAND_EDGE
        Assert.assertEqual(SENSOR_EOIR_BAND_WAVELENGTH_TYPE.LOW_BAND_EDGE, band.wavelength_type)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.wavelength = 1

        band.wavelength_type = SENSOR_EOIR_BAND_WAVELENGTH_TYPE.USER_DEFINED_WAVELENGTH
        Assert.assertEqual(SENSOR_EOIR_BAND_WAVELENGTH_TYPE.USER_DEFINED_WAVELENGTH, band.wavelength_type)

        band.wavelength = 0.4
        Assert.assertEqual(0.4, band.wavelength)
        band.wavelength = 0.7
        Assert.assertEqual(0.7, band.wavelength)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.wavelength = 0.27
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.wavelength = 28.1

    def Test_RadiometricTab(self, band: "SensorEOIRBand"):
        # Not on GUI
        band.calculating_parameters = False
        Assert.assertFalse(band.calculating_parameters)
        band.calculating_parameters = True
        Assert.assertTrue(band.calculating_parameters)

        band.saturation_mode = SENSOR_EOIR_BAND_SATURATION_MODE.IRRADIANCE
        Assert.assertEqual(SENSOR_EOIR_BAND_SATURATION_MODE.IRRADIANCE, band.saturation_mode)
        band.saturation_mode = SENSOR_EOIR_BAND_SATURATION_MODE.RADIANCE
        Assert.assertEqual(SENSOR_EOIR_BAND_SATURATION_MODE.RADIANCE, band.saturation_mode)

        # "Simulate Saturation" on the GUI
        band.dynamic_range_mode = True
        Assert.assertTrue(band.dynamic_range_mode)
        band.dynamic_range_mode = False
        Assert.assertFalse(band.dynamic_range_mode)

        band.simulate_quantization = True
        Assert.assertTrue(band.simulate_quantization)
        band.simulate_quantization = False
        Assert.assertFalse(band.simulate_quantization)

        self.Test_RadiometricTab_HighLevel(band)

        self.Test_RadiometricTab_LowLevel(band)

        # set up for below
        band.saturation_mode = SENSOR_EOIR_BAND_SATURATION_MODE.IRRADIANCE
        pair: "SensorEOIRRadiometricPair" = band.sensitivities.add()
        pair.integration_time = 100
        pair.equivalent_value = 100
        band.dynamic_range_mode = True
        pair = band.saturations.add()
        pair.integration_time = 100
        pair.equivalent_value = 100
        band.integration_time = 5000

    def Test_RadiometricTab_HighLevel(self, band: "SensorEOIRBand"):
        band.rad_param_level = SENSOR_EOIR_BAND_RAD_PARAM_LEVEL.HIGH_LEVEL_RAD_PARAMS
        Assert.assertEqual(SENSOR_EOIR_BAND_RAD_PARAM_LEVEL.HIGH_LEVEL_RAD_PARAMS, band.rad_param_level)

        # These properties tested in both HighLevel and LowLevel
        band.integration_time = 0.001
        Assert.assertEqual(0.001, band.integration_time)
        band.integration_time = 3600000.0
        Assert.assertEqual(3600000.0, band.integration_time)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.integration_time = 0.0001
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.integration_time = 3700000.0
        band.integration_time = 100.0  # set back to default
        Assert.assertAlmostEqual(3000.0, band.dynamic_range, delta=0.001)
        Assert.assertAlmostEqual(1e-15, band.nei, delta=1e-18)
        Assert.assertAlmostEqual(3e-12, band.sei, delta=1e-15)

        self.Test_IAgSnEOIRSensitivityCollection(band.sensitivities)

        self.Test_IAgSnEOIRSaturationCollection(band.saturations)

    def Test_RadiometricTab_LowLevel(self, band: "SensorEOIRBand"):
        band.rad_param_level = SENSOR_EOIR_BAND_RAD_PARAM_LEVEL.LOW_LEVEL_RAD_PARAMS
        Assert.assertEqual(SENSOR_EOIR_BAND_RAD_PARAM_LEVEL.LOW_LEVEL_RAD_PARAMS, band.rad_param_level)

        # These properties tested in both HighLevel and LowLevel
        band.integration_time = 0.001
        Assert.assertEqual(0.001, band.integration_time)
        band.integration_time = 3600000.0
        Assert.assertEqual(3600000.0, band.integration_time)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.integration_time = 0.0001
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.integration_time = 3700000.0
        band.integration_time = 100.0  # set back to default
        Assert.assertAlmostEqual(95346.259, band.dynamic_range, delta=0.001)
        Assert.assertAlmostEqual(4.2e-17, band.nei, delta=1e-18)
        Assert.assertAlmostEqual(4e-12, band.sei, delta=1e-13)

        band.qe_mode = SENSOR_EOIR_BAND_QE_MODE.QE_BAND_EFFECTIVE  # "Band Effective" on dropdown in GUI
        Assert.assertEqual(SENSOR_EOIR_BAND_QE_MODE.QE_BAND_EFFECTIVE, band.qe_mode)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.qe_file = r"C:\Temp\temp.txt"

        band.qe_value = 1e-06
        Assert.assertEqual(1e-06, band.qe_value)
        band.qe_value = 1.0
        Assert.assertEqual(1.0, band.qe_value)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.qe_value = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.qe_value = 1.1

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.qe_file = "bogus"

        band.qe_mode = SENSOR_EOIR_BAND_QE_MODE.QE_SPECTRAL_DATA_FILE  # "Spectral Response" on dropdown in GUI
        Assert.assertEqual(SENSOR_EOIR_BAND_QE_MODE.QE_SPECTRAL_DATA_FILE, band.qe_mode)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.qe_value = 2

        holdQEFile: str = band.qe_file
        with pytest.raises(Exception, match=RegexSubstringMatch("file does not exist")):
            band.qe_file = "bogus.srf"
        Assert.assertTrue(("BackIllumSi_QE.srf" in band.qe_file))
        newQEFile: str = holdQEFile.replace("Back", "Front")
        band.qe_file = newQEFile
        Assert.assertTrue(("FrontIllumSi_QE.srf" in band.qe_file))
        band.qe_file = holdQEFile
        Assert.assertTrue(("BackIllumSi_QE.srf" in band.qe_file))

        # EOIR-243 and EOIR-1029
        # band.DetectorFillFactor = 0.0;
        # Assert.AreEqual(0.0, band.DetectorFillFactor);
        band.detector_fill_factor = 1.0
        Assert.assertEqual(1.0, band.detector_fill_factor)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.detector_fill_factor = -0.1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.detector_fill_factor = 1.1

        band.read_noise = 0.0
        Assert.assertEqual(0.0, band.read_noise)
        band.read_noise = 1000000.0
        Assert.assertEqual(1000000.0, band.read_noise)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.read_noise = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.read_noise = 10000000.0

        band.dark_current = 0.0
        Assert.assertEqual(0.0, band.dark_current)
        band.dark_current = 100000000000000.0
        Assert.assertEqual(100000000000000.0, band.dark_current)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.dark_current = -1.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.dark_current = 1000000000000000.0

        band.quantization_mode = SENSOR_EOIR_BAND_QUANTIZATION_MODE.BIT_DEPTH_AND_NOISE
        Assert.assertEqual(SENSOR_EOIR_BAND_QUANTIZATION_MODE.BIT_DEPTH_AND_NOISE, band.quantization_mode)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.detector_full_well_capacity = 0.0

        band.bit_depth = 1
        Assert.assertEqual(1, band.bit_depth)
        band.bit_depth = 128
        Assert.assertEqual(128, band.bit_depth)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.bit_depth = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.bit_depth = 129

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.qss = 0.0

        band.quantization_mode = SENSOR_EOIR_BAND_QUANTIZATION_MODE.BIT_DEPTH_AND_QSS
        Assert.assertEqual(SENSOR_EOIR_BAND_QUANTIZATION_MODE.BIT_DEPTH_AND_QSS, band.quantization_mode)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.detector_full_well_capacity = 0.0

        band.bit_depth = 1
        Assert.assertEqual(1, band.bit_depth)
        band.bit_depth = 128
        Assert.assertEqual(128, band.bit_depth)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.bit_depth = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.bit_depth = 129

        band.qss = 1.0
        Assert.assertEqual(1.0, band.qss)
        band.qss = 1000000000000.0
        Assert.assertEqual(1000000000000.0, band.qss)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.qss = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.qss = 10000000000000.0

        band.quantization_mode = SENSOR_EOIR_BAND_QUANTIZATION_MODE.FULL_WELL_AND_NOISE
        Assert.assertEqual(SENSOR_EOIR_BAND_QUANTIZATION_MODE.FULL_WELL_AND_NOISE, band.quantization_mode)

        band.detector_full_well_capacity = 1
        Assert.assertEqual(1, band.detector_full_well_capacity)
        band.detector_full_well_capacity = 1000000000000000.0
        Assert.assertEqual(1000000000000000.0, band.detector_full_well_capacity)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.detector_full_well_capacity = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.detector_full_well_capacity = 10000000000000000.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.bit_depth = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.qss = 1.0

        band.quantization_mode = SENSOR_EOIR_BAND_QUANTIZATION_MODE.FULL_WELL_AND_QSS
        Assert.assertEqual(SENSOR_EOIR_BAND_QUANTIZATION_MODE.FULL_WELL_AND_QSS, band.quantization_mode)

        band.detector_full_well_capacity = 1
        Assert.assertEqual(1, band.detector_full_well_capacity)
        band.detector_full_well_capacity = 1000000000000000.0
        Assert.assertEqual(1000000000000000.0, band.detector_full_well_capacity)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.detector_full_well_capacity = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.detector_full_well_capacity = 10000000000000000.0

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            band.bit_depth = 1

        band.qss = 1.0
        Assert.assertEqual(1.0, band.qss)
        band.qss = 1000000000000.0
        Assert.assertEqual(1000000000000.0, band.qss)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.qss = 0.0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            band.qss = 10000000000000.0

    def Test_IAgSnEOIRSensitivityCollection(self, sensColl: "SensorEOIRSensitivityCollection"):
        Assert.assertEqual(1, sensColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("cannot be removed")):
            sensColl.remove_at(0)
        Assert.assertEqual(1, sensColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid Index")):
            sensColl.remove_at(1)

        pair: "SensorEOIRRadiometricPair" = None
        pair = sensColl.add()
        pair = sensColl.add()
        pair = sensColl.add()
        pair = sensColl.add()
        pair = sensColl.add()
        Assert.assertEqual(6, sensColl.count)

        pairx: "SensorEOIRRadiometricPair"

        for pairx in sensColl:
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pairx.integration_time = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pairx.equivalent_value = -1
            pairx.integration_time = 1
            Assert.assertEqual(1, pairx.integration_time)
            pairx.equivalent_value = 2
            Assert.assertEqual(2, pairx.equivalent_value)

        i: int = 0
        while i < sensColl.count:
            pair = sensColl[i]
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pair.integration_time = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pair.equivalent_value = -1
            pair.integration_time = 1000000
            Assert.assertEqual(1000000, pair.integration_time)
            pair.equivalent_value = 2000000
            Assert.assertEqual(2000000, pair.equivalent_value)

            i += 1

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            pair = sensColl[6]

        sensColl.remove_at(0)
        sensColl.remove_at(0)
        sensColl.remove_at(0)
        sensColl.remove_at(0)
        sensColl.remove_at(0)
        Assert.assertEqual(1, sensColl.count)

    def Test_IAgSnEOIRSaturationCollection(self, saturColl: "SensorEOIRSaturationCollection"):
        Assert.assertEqual(1, saturColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("cannot be removed")):
            saturColl.remove_at(0)
        Assert.assertEqual(1, saturColl.count)
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid Index")):
            saturColl.remove_at(1)

        pair: "SensorEOIRRadiometricPair" = None
        pair = saturColl.add()
        pair = saturColl.add()
        pair = saturColl.add()
        pair = saturColl.add()
        pair = saturColl.add()
        Assert.assertEqual(6, saturColl.count)

        pairx: "SensorEOIRRadiometricPair"

        for pairx in saturColl:
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pairx.integration_time = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pairx.equivalent_value = -1
            pairx.integration_time = 1
            Assert.assertEqual(1, pairx.integration_time)
            pairx.equivalent_value = 2
            Assert.assertEqual(2, pairx.equivalent_value)

        i: int = 0
        while i < saturColl.count:
            pair = saturColl[i]
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pair.integration_time = -1
            with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
                pair.equivalent_value = -1
            pair.integration_time = 1000000
            Assert.assertEqual(1000000, pair.integration_time)
            pair.equivalent_value = 2000000
            Assert.assertEqual(2000000, pair.equivalent_value)

            i += 1

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            pair = saturColl[6]

        saturColl.remove_at(0)
        saturColl.remove_at(0)
        saturColl.remove_at(0)
        saturColl.remove_at(0)
        saturColl.remove_at(0)
        Assert.assertEqual(1, saturColl.count)

    # endregion
