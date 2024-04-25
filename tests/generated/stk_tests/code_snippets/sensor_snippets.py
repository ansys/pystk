from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.utilities.colors import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class SensorSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SensorSnippets, self).__init__(*args, **kwargs)

    m_Object: "Sensor" = None
    m_Satellite: "IStkObject" = None
    m_DefaultName: str = "sensor1"
    m_SatelliteName: str = "satellite1"

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

    # region TestSetUp
    def setUp(self):
        SensorSnippets.m_Satellite = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            STK_OBJECT_TYPE.SATELLITE, SensorSnippets.m_SatelliteName
        )
        SensorSnippets.m_Object = clr.CastAs(
            SensorSnippets.m_Satellite.children.new(STK_OBJECT_TYPE.SENSOR, SensorSnippets.m_DefaultName), Sensor
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, SensorSnippets.m_SatelliteName
        )

    # endregion

    # region DefineSimpleConicSensor
    def test_DefineSimpleConicSensor(self):
        self.DefineSimpleConicSensor(SensorSnippets.m_Object)

    def DefineSimpleConicSensor(self, sensor: "Sensor"):
        patternData: "SensorSimpleConicPattern" = sensor.common_tasks.set_pattern_simple_conic(40.0, 0.1)

    # endregion

    # region DefineComplexSensor
    def test_DefineComplexSensor(self):
        self.DefineComplexSensor(SensorSnippets.m_Object)

    def DefineComplexSensor(self, sensor: "Sensor"):
        patterndata: "SensorComplexConicPattern" = sensor.common_tasks.set_pattern_complex_conic(
            10.0, 70.0, 20.0, 220.0
        )
        patterndata.angular_resolution = 0.5

    # endregion

    # region DefineCustomSensor
    def test_DefineCustomSensor(self):
        self.DefineCustomSensor(
            SensorSnippets.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "Custom.Pattern")
        )

    def DefineCustomSensor(self, sensor: "Sensor", sensorPatternPath: str):
        # Set pattern type to Custom
        customPattern: "SensorCustomPattern" = sensor.common_tasks.set_pattern_custom(sensorPatternPath)
        customPattern.angular_resolution = 6.0
        customPattern.use_native_resolution = False

    # endregion

    # region DefineHalfPowerSensor
    def test_DefineHalfPowerSensor(self):
        self.DefineHalfPowerSensor(SensorSnippets.m_Object)

    def DefineHalfPowerSensor(self, sensor: "Sensor"):
        # Configure pattern
        pattern: "SensorHalfPowerPattern" = sensor.common_tasks.set_pattern_half_power(12.5, 3.4, 6.0)

    # endregion

    # region DefineSARSensor
    def test_DefineSARSensor(self):
        self.DefineSARSensor(SensorSnippets.m_Object)

    def DefineSARSensor(self, sensor: "Sensor"):
        # Configure pattern
        patterndata: "SensorSARPattern" = sensor.common_tasks.set_pattern_sar(10.0, 60.0, 40.0, 30.0, 700.0)

    # endregion

    # region DefineSensorPointingFixedAzEl
    def test_DefineSensorPointingFixedAzEl(self):
        self.DefineSensorPointingFixedAzEl(SensorSnippets.m_Object)

    def DefineSensorPointingFixedAzEl(self, sensor: "Sensor"):
        fixedSensor: "SensorPointingFixed" = sensor.common_tasks.set_pointing_fixed_az_el(
            4.5, -45.0, AZ_EL_ABOUT_BORESIGHT.ROTATE
        )

    # endregion

    # region DefineSensorPointingFixedAxesAzEl
    def test_DefineSensorPointingFixedAxesAzEl(self):
        self.DefineSensorPointingFixedAxesAzEl(SensorSnippets.m_Object)

    def DefineSensorPointingFixedAxesAzEl(self, sensor: "Sensor"):
        fixedAxesSensor: "SensorPointingFixedAxes" = sensor.common_tasks.set_pointing_fixed_axes_az_el(
            "CentralBody/Sun J2000 Axes", 11, 22, AZ_EL_ABOUT_BORESIGHT.HOLD
        )

    # endregion

    # region DefineSensorPointingFixedEuler
    def test_DefineSensorPointingFixedEuler(self):
        self.DefineSensorPointingFixedEuler(SensorSnippets.m_Object)

    def DefineSensorPointingFixedEuler(self, sensor: "Sensor"):
        fixedSensor: "SensorPointingFixed" = sensor.common_tasks.set_pointing_fixed_euler(
            EULER_ORIENTATION_SEQUENCE.SEQUENCE_132, 30, 40, 50
        )

    # endregion

    # region DefineSensorPointingFixedAxesEuler
    def test_DefineSensorPointingFixedAxesEuler(self):
        self.DefineSensorPointingFixedAxesEuler(SensorSnippets.m_Object)

    def DefineSensorPointingFixedAxesEuler(self, sensor: "Sensor"):
        fixedAxesSensor: "SensorPointingFixedAxes" = sensor.common_tasks.set_pointing_fixed_axes_euler(
            "CentralBody/Sun J2000 Axes", EULER_ORIENTATION_SEQUENCE.SEQUENCE_132, 30, 40, 50
        )

    # endregion

    # region DefineSensorPointingFixedQuaternion
    def test_DefineSensorPointingFixedQuaternion(self):
        self.DefineSensorPointingFixedQuaternion(SensorSnippets.m_Object)

    def DefineSensorPointingFixedQuaternion(self, sensor: "Sensor"):
        fixedSensor: "SensorPointingFixed" = sensor.common_tasks.set_pointing_fixed_quat(0.1, 0.2, 0.3, 0.4)

    # endregion

    # region DefineSensorPointingFixedAxesQuaternion
    def test_DefineSensorPointingFixedAxesQuaternion(self):
        self.DefineSensorPointingFixedAxesQuaternion(SensorSnippets.m_Object)

    def DefineSensorPointingFixedAxesQuaternion(self, sensor: "Sensor"):
        fixedAxesSensor: "SensorPointingFixedAxes" = sensor.common_tasks.set_pointing_fixed_axes_quat(
            "CentralBody/Sun J2000 Axes", 0.1, 0.2, 0.3, 0.4
        )

    # endregion

    # region DefineSensorPointingFixedYPR
    def test_DefineSensorPointingFixedYPR(self):
        self.DefineSensorPointingFixedYPR(SensorSnippets.m_Object)

    def DefineSensorPointingFixedYPR(self, sensor: "Sensor"):
        fixedSensor: "SensorPointingFixed" = sensor.common_tasks.set_pointing_fixed_ypr(
            YPR_ANGLES_SEQUENCE.RPY, 12, 24, 36
        )

    # endregion

    # region DefineSensorPointingFixedAxesYPR
    def test_DefineSensorPointingFixedAxesYPR(self):
        self.DefineSensorPointingFixedAxesYPR(SensorSnippets.m_Object)

    def DefineSensorPointingFixedAxesYPR(self, sensor: "Sensor"):
        fixedAxesSensor: "SensorPointingFixedAxes" = sensor.common_tasks.set_pointing_fixed_axes_ypr(
            "CentralBody/Sun J2000 Axes", YPR_ANGLES_SEQUENCE.RYP, 11, 22, 33
        )

    # endregion

    # region DefineTargetSensorPointing
    def test_DefineTargetSensorPointing(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget1")
        self.DefineTargetSensorPointing(SensorSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.AREA_TARGET, "AreaTarget1")

    def DefineTargetSensorPointing(self, sensor: "Sensor"):
        targetedSensor: "SensorPointingTargeted" = sensor.common_tasks.set_pointing_targeted_tracking(
            TRACK_MODE_TYPE.TRANSMIT, BORESIGHT_TYPE.LEVEL, "*/AreaTarget/AreaTarget1"
        )

    # endregion

    # region DefineSpinningSensorPointing
    def test_DefineSpinningSensorPointing(self):
        self.DefineSpinningSensorPointing(CodeSnippetsTestBase.m_Root, SensorSnippets.m_Object)

    def DefineSpinningSensorPointing(self, root: "StkObjectRoot", sensor: "Sensor"):
        # Set pattern type to Spinning
        sensor.set_pointing_type(SENSOR_POINTING.POINT_SPINNING)
        spinning: "SensorPointingSpinning" = clr.CastAs(sensor.pointing, SensorPointingSpinning)

        # Configure sensor
        spinning.spin_axis_azimuth = 14.24
        spinning.spin_axis_elevation = 7.68
        spinning.spin_axis_cone_angle = 42.46
        spinning.scan_mode = SENSOR_SCAN_MODE.CONTINUOUS
        spinning.spin_rate = 88.921
        spinning.offset_angle = 110.44

    # endregion

    # region DefineSpinningSensorPointingUsingCommonTasks
    def test_DefineSpinningSensorPointingUsingCommonTasks(self):
        self.DefineSpinningSensorPointingUsingCommonTasks(SensorSnippets.m_Object)

    def DefineSpinningSensorPointingUsingCommonTasks(self, sensor: "Sensor"):
        # Configure sensor (using common taks)
        sensor.common_tasks.set_pointing_spinning(
            14.24, 7.68, 42.46, SENSOR_SCAN_MODE.CONTINUOUS, 88.921, 110.44, 1.2, 3.5
        )

    # endregion

    # region DefineExternalSensorPointing
    def test_DefineExternalSensorPointing(self):
        self.DefineExternalSensorPointing(
            SensorSnippets.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "SensorPointing_External.sp")
        )

    def DefineExternalSensorPointing(self, sensor: "Sensor", externalSensorPointingPath: str):
        # Sensor pointing data files traditionally have .sp extensions
        sensor.set_pointing_external_file(externalSensorPointingPath)

        external: "SensorPointingExternal" = clr.CastAs(sensor.pointing, SensorPointingExternal)

    # endregion

    # region DefineFixedLocation
    def test_DefineFixedLocation(self):
        self.DefineFixedLocation(SensorSnippets.m_Object)

    def DefineFixedLocation(self, sensor: "Sensor"):
        # Set sensor's location to fixed
        sensor.set_location_type(SENSOR_LOCATION.FIXED)

        # Configure sensor location
        pos: "IPosition" = clr.CastAs(sensor.location_data, IPosition)
        pos.assign_cartesian(595.2, -110.12, 4.6)

    # endregion

    # region DefineLocationOn3DModel
    @category("VO Tests")
    def test_DefineLocationOn3DModel(self):
        if TestBase.NoGraphicsMode:
            Assert.skipTest("Test cannot be run in NoGraphicsMode (because it uses VO)")

        satellite: "Satellite" = clr.CastAs(SensorSnippets.m_Satellite, Satellite)
        modelFile: "Graphics3DModelFile" = clr.CastAs(satellite.graphics_3d.model.model_data, Graphics3DModelFile)
        modelFile.filename = r"\STKData\VO\Models\Space\satellite.glb"
        self.DefineLocationOn3DModel(SensorSnippets.m_Object)

    def DefineLocationOn3DModel(self, sensor: "Sensor"):
        # Set pointing type to 3d model
        sensor.set_pointing_type(SENSOR_POINTING.POINT_3D_MODEL)

        # Point to model attach point (in this example: "SolarPanels")
        model: "SensorPointing3DModel" = sensor.common_tasks.set_pointing_3d_model("SolarPanels")

    # endregion

    # region DefineLocationFromCrdnPoint
    def test_DefineLocationFromCrdnPoint(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "Facility1")
        self.DefineLocationFromCrdnPoint(SensorSnippets.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.FACILITY, "Facility1")

    def DefineLocationFromCrdnPoint(self, sensor: "Sensor"):
        # Set location type to VGT
        sensor.set_location_type(SENSOR_LOCATION.VECTOR_GEOMETRY_TOOL_POINT)

        # Get LocationVectorGeometryToolPoint interface
        vgtPoint: "LocationVectorGeometryToolPoint" = clr.CastAs(sensor.location_data, LocationVectorGeometryToolPoint)

        # point sensor to an already existing object
        vgtPoint.point_path = "Facility/Facility1 Center"

    # endregion

    # region DefineSensorAzElMask
    def test_DefineSensorAzElMask(self):
        self.DefineSensorAzElMask(
            SensorSnippets.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "maskfile.aem")
        )

    def DefineSensorAzElMask(self, sensor: "Sensor", maskFilePath: str):
        # Specify Mask file
        sensor.set_az_el_mask_file(maskFilePath)

        # Get Mask File interface
        maskFile: "SensorAzElMaskFile" = clr.CastAs(sensor.az_el_mask_data, SensorAzElMaskFile)

        # Configure MaskFile as needed
        maskFile.boresight_axis = SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE.PLUS_MINUS_Z

    # endregion

    # region ConfigureAndComputeSensorSwath
    @category("VO Tests")
    def test_ConfigureAndComputeSensorSwath(self):
        if TestBase.NoGraphicsMode:
            Assert.skipTest("Test cannot be run in NoGraphicsMode (because it uses swath)")

        (Satellite(SensorSnippets.m_Satellite)).set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        tb: "VehiclePropagatorTwoBody" = clr.CastAs(
            (Satellite(SensorSnippets.m_Satellite)).propagator, VehiclePropagatorTwoBody
        )
        # Propagate
        tb.propagate()
        self.ConfigureAndComputeSensorSwath(SensorSnippets.m_Object)

    def ConfigureAndComputeSensorSwath(self, sensor: "Sensor"):
        # Configure swath display properties
        swath: "Swath" = sensor.swath
        swath.enable = True
        swath.color = Colors.Red  # red
        swath.line_style = LINE_STYLE.LMS_DASH
        swath.line_width = LINE_WIDTH.WIDTH2

        # New swath properties
        swath.use_maximum_cone = True
        swath.curvature_tolerance = 90.0
        swath.scattering_tolerance = 70.0
        swath.minimum_step = 5
        swath.maximum_step = 10

        swath.add_time_interval("1 Jan 2012 12:00:00.000", "1 Jan 2012 13:00:00.000")
        swath.add_time_interval("1 Jan 2012 14:00:00.000", "1 Jan 2012 15:00:00.000")

    # endregion

    # region ConfigureSensorVOProjection
    @category("VO Tests")
    def test_ConfigureSensorVOProjection(self):
        if TestBase.NoGraphicsMode:
            Assert.skipTest("Test cannot be run in NoGraphicsMode (because it uses VO)")

        self.ConfigureSensorVOProjection(SensorSnippets.m_Object.graphics_3d)

    def ConfigureSensorVOProjection(self, sensorVo: "SensorGraphics3D"):
        sensorVo.projection_type = SENSOR_GRAPHICS_3D_PROJECTION_TYPE.PROJECTION_ALL_INTERSECTIONS
        sensorVo.inherit_from_2d = SENSOR_GRAPHICS_3D_INHERIT_FROM_2D.EXTENT_ONLY
        sensorVo.space_projection = 2000.0

    # endregion

    # region ConfigureSensorVOProjectionTimeVarying
    @category("VO Tests")
    def test_ConfigureSensorVOProjectionTimeVarying(self):
        if TestBase.NoGraphicsMode:
            Assert.skipTest("Test cannot be run in NoGraphicsMode (because it uses VO)")

        self.ConfigureSensorVOProjectionTimeVarying(SensorSnippets.m_Object.graphics_3d)

    def ConfigureSensorVOProjectionTimeVarying(self, sensorVo: "SensorGraphics3D"):
        sensorVo.projection_type = SENSOR_GRAPHICS_3D_PROJECTION_TYPE.PROJECTION_ALL_INTERSECTIONS
        sensorVo.projection_time_dependency = SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE.TIME_VARYING
        elem1: "SensorGraphics3DProjectionElement" = sensorVo.space_projection_intervals.add()
        elem1.distance = 5000.0
        elem1.time = "1 Jan 2012 12:00:00.000"
        elem2: "SensorGraphics3DProjectionElement" = sensorVo.space_projection_intervals.add()
        elem2.distance = 2000.0
        elem2.time = "1 Jan 2012 16:00:00.000"
        elem3: "SensorGraphics3DProjectionElement" = sensorVo.space_projection_intervals.add()
        elem3.distance = 4000.0
        elem3.time = "1 Jan 2012 20:00:00.000"

    # endregion
