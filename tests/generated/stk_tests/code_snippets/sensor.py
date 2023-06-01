from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Sensor(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Sensor, self).__init__(*args, **kwargs)

    m_Object = None
    m_Satellite = None
    m_DefaultName = "sensor1"
    m_SatelliteName = "satellite1"

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
        Sensor.m_Satellite = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
            AgESTKObjectType.eSatellite, Sensor.m_SatelliteName
        )
        Sensor.m_Object = clr.CastAs(
            Sensor.m_Satellite.Children.New(AgESTKObjectType.eSensor, Sensor.m_DefaultName), ISensor
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, Sensor.m_SatelliteName)

    # endregion

    # region DefineSimpleConicSensor
    def test_DefineSimpleConicSensor(self):
        self.DefineSimpleConicSensor(Sensor.m_Object)

    def DefineSimpleConicSensor(self, sensor):
        patternData = sensor.CommonTasks.SetPatternSimpleConic(40.0, 0.1)

    # endregion

    # region DefineComplexSensor
    def test_DefineComplexSensor(self):
        self.DefineComplexSensor(Sensor.m_Object)

    def DefineComplexSensor(self, sensor):
        patterndata = sensor.CommonTasks.SetPatternComplexConic(10.0, 70.0, 20.0, 220.0)
        patterndata.AngularResolution = 0.5

    # endregion

    # region DefineCustomSensor
    def test_DefineCustomSensor(self):
        self.DefineCustomSensor(Sensor.m_Object, TestBase.GetScenarioFile("Custom.Pattern"))

    def DefineCustomSensor(self, sensor, sensorPatternPath):
        # Set pattern type to Custom
        customPattern = sensor.CommonTasks.SetPatternCustom(sensorPatternPath)
        customPattern.AngularResolution = 6.0
        customPattern.UseNativeResolution = False

    # endregion

    # region DefineHalfPowerSensor
    def test_DefineHalfPowerSensor(self):
        self.DefineHalfPowerSensor(Sensor.m_Object)

    def DefineHalfPowerSensor(self, sensor):
        # Configure pattern
        pattern = sensor.CommonTasks.SetPatternHalfPower(12.5, 3.4, 6.0)

    # endregion

    # region DefineSARSensor
    def test_DefineSARSensor(self):
        self.DefineSARSensor(Sensor.m_Object)

    def DefineSARSensor(self, sensor):
        # Configure pattern
        patterndata = sensor.CommonTasks.SetPatternSAR(10.0, 60.0, 40.0, 30.0, 700.0)

    # endregion

    # region DefineSensorPointingFixedAzEl
    def test_DefineSensorPointingFixedAzEl(self):
        self.DefineSensorPointingFixedAzEl(Sensor.m_Object)

    def DefineSensorPointingFixedAzEl(self, sensor):
        fixedSensor = sensor.CommonTasks.SetPointingFixedAzEl(
            4.5, -45.0, AgEAzElAboutBoresight.eAzElAboutBoresightRotate
        )

    # endregion

    # region DefineSensorPointingFixedAxesAzEl
    def test_DefineSensorPointingFixedAxesAzEl(self):
        self.DefineSensorPointingFixedAxesAzEl(Sensor.m_Object)

    def DefineSensorPointingFixedAxesAzEl(self, sensor):
        fixedAxesSensor = sensor.CommonTasks.SetPointingFixedAxesAzEl(
            "CentralBody/Sun J2000 Axes", 11, 22, AgEAzElAboutBoresight.eAzElAboutBoresightHold
        )

    # endregion

    # region DefineSensorPointingFixedEuler
    def test_DefineSensorPointingFixedEuler(self):
        self.DefineSensorPointingFixedEuler(Sensor.m_Object)

    def DefineSensorPointingFixedEuler(self, sensor):
        fixedSensor = sensor.CommonTasks.SetPointingFixedEuler(AgEEulerOrientationSequence.e132, 30, 40, 50)

    # endregion

    # region DefineSensorPointingFixedAxesEuler
    def test_DefineSensorPointingFixedAxesEuler(self):
        self.DefineSensorPointingFixedAxesEuler(Sensor.m_Object)

    def DefineSensorPointingFixedAxesEuler(self, sensor):
        fixedAxesSensor = sensor.CommonTasks.SetPointingFixedAxesEuler(
            "CentralBody/Sun J2000 Axes", AgEEulerOrientationSequence.e132, 30, 40, 50
        )

    # endregion

    # region DefineSensorPointingFixedQuaternion
    def test_DefineSensorPointingFixedQuaternion(self):
        self.DefineSensorPointingFixedQuaternion(Sensor.m_Object)

    def DefineSensorPointingFixedQuaternion(self, sensor):
        fixedSensor = sensor.CommonTasks.SetPointingFixedQuat(0.1, 0.2, 0.3, 0.4)

    # endregion

    # region DefineSensorPointingFixedAxesQuaternion
    def test_DefineSensorPointingFixedAxesQuaternion(self):
        self.DefineSensorPointingFixedAxesQuaternion(Sensor.m_Object)

    def DefineSensorPointingFixedAxesQuaternion(self, sensor):
        fixedAxesSensor = sensor.CommonTasks.SetPointingFixedAxesQuat("CentralBody/Sun J2000 Axes", 0.1, 0.2, 0.3, 0.4)

    # endregion

    # region DefineSensorPointingFixedYPR
    def test_DefineSensorPointingFixedYPR(self):
        self.DefineSensorPointingFixedYPR(Sensor.m_Object)

    def DefineSensorPointingFixedYPR(self, sensor):
        fixedSensor = sensor.CommonTasks.SetPointingFixedYPR(AgEYPRAnglesSequence.eRPY, 12, 24, 36)

    # endregion

    # region DefineSensorPointingFixedAxesYPR
    def test_DefineSensorPointingFixedAxesYPR(self):
        self.DefineSensorPointingFixedAxesYPR(Sensor.m_Object)

    def DefineSensorPointingFixedAxesYPR(self, sensor):
        fixedAxesSensor = sensor.CommonTasks.SetPointingFixedAxesYPR(
            "CentralBody/Sun J2000 Axes", AgEYPRAnglesSequence.eRYP, 11, 22, 33
        )

    # endregion

    # region DefineTargetSensorPointing
    def test_DefineTargetSensorPointing(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eAreaTarget, "AreaTarget1")
        self.DefineTargetSensorPointing(Sensor.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eAreaTarget, "AreaTarget1")

    def DefineTargetSensorPointing(self, sensor):
        targetedSensor = sensor.CommonTasks.SetPointingTargetedTracking(
            AgETrackModeType.eTrackModeTransmit, AgEBoresightType.eBoresightLevel, "*/AreaTarget/AreaTarget1"
        )

    # endregion

    # region DefineSpinningSensorPointing
    def test_DefineSpinningSensorPointing(self):
        self.DefineSpinningSensorPointing(CodeSnippetsTestBase.m_Root, Sensor.m_Object)

    def DefineSpinningSensorPointing(self, root, sensor):
        # Set pattern type to Spinning
        sensor.SetPointingType(AgESnPointing.eSnPtSpinning)
        spinning = clr.CastAs(sensor.Pointing, ISensorPointingSpinning)

        # Configure sensor
        spinning.SpinAxisAzimuth = 14.24
        spinning.SpinAxisElevation = 7.68
        spinning.SpinAxisConeAngle = 42.46
        spinning.ScanMode = AgESnScanMode.eSnContinuous
        spinning.SpinRate = 88.921
        spinning.OffsetAngle = 110.44

    # endregion

    # region DefineSpinningSensorPointingUsingCommonTasks
    def test_DefineSpinningSensorPointingUsingCommonTasks(self):
        self.DefineSpinningSensorPointingUsingCommonTasks(Sensor.m_Object)

    def DefineSpinningSensorPointingUsingCommonTasks(self, sensor):
        # Configure sensor (using common taks)
        sensor.CommonTasks.SetPointingSpinning(
            14.24, 7.68, 42.46, AgESnScanMode.eSnContinuous, 88.921, 110.44, 1.2, 3.5
        )

    # endregion

    # region DefineExternalSensorPointing
    def test_DefineExternalSensorPointing(self):
        self.DefineExternalSensorPointing(Sensor.m_Object, TestBase.GetScenarioFile("SensorPointing_External.sp"))

    def DefineExternalSensorPointing(self, sensor, externalSensorPointingPath):
        # Sensor pointing data files traditionally have .sp extensions
        sensor.SetPointingExternalFile(externalSensorPointingPath)

        external = clr.CastAs(sensor.Pointing, ISensorPointingExternal)

    # endregion

    # region DefineFixedLocation
    def test_DefineFixedLocation(self):
        self.DefineFixedLocation(Sensor.m_Object)

    def DefineFixedLocation(self, sensor):
        # Set sensor's location to fixed
        sensor.SetLocationType(AgESnLocation.eSnFixed)

        # Configure sensor location
        pos = clr.CastAs(sensor.LocationData, IPosition)
        pos.AssignCartesian(595.2, -110.12, 4.6)

    # endregion

    # region DefineLocationOn3DModel
    @category("VO Tests")
    def test_DefineLocationOn3DModel(self):
        if TestBase.NoGraphicsMode:
            Assert.skipTest("Test cannot be run in NoGraphicsMode (because it uses VO)")

        satellite = clr.CastAs(Sensor.m_Satellite, ISatellite)
        modelFile = clr.CastAs(satellite.VO.Model.ModelData, IVOModelFile)
        modelFile.Filename = r"\STKData\VO\Models\Space\satellite.dae"
        self.DefineLocationOn3DModel(Sensor.m_Object)

    def DefineLocationOn3DModel(self, sensor):
        # Set pointing type to 3d model
        sensor.SetPointingType(AgESnPointing.eSnPt3DModel)

        # Point to model attach point (in this example: "SolarArrays-000000")
        model = sensor.CommonTasks.SetPointing3DModel("Solar_PanelsNode")

    # endregion

    # region DefineLocationFromCrdnPoint
    def test_DefineLocationFromCrdnPoint(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility1")
        self.DefineLocationFromCrdnPoint(Sensor.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "Facility1")

    def DefineLocationFromCrdnPoint(self, sensor):
        # Set location type to VGT
        sensor.SetLocationType(AgESnLocation.eSnLocationCrdnPoint)

        # Get IAgLocationCrdnPoint interface
        vgtPoint = clr.CastAs(sensor.LocationData, ILocationCrdnPoint)

        # point sensor to an already existing object
        vgtPoint.PointPath = "Facility/Facility1 Center"

    # endregion

    # region DefineSensorAzElMask
    def test_DefineSensorAzElMask(self):
        self.DefineSensorAzElMask(Sensor.m_Object, TestBase.GetScenarioFile("maskfile.aem"))

    def DefineSensorAzElMask(self, sensor, maskFilePath):
        # Specify Mask file
        sensor.SetAzElMaskFile(maskFilePath)

        # Get Mask File interface
        maskFile = clr.CastAs(sensor.AzElMaskData, ISensorAzElMaskFile)

        # Configure MaskFile as needed
        maskFile.BoresightAxis = AgESnAzElBsightAxisType.ePlus_MinusZ

    # endregion

    # region ConfigureAndComputeSensorSwath
    @category("VO Tests")
    def test_ConfigureAndComputeSensorSwath(self):
        if TestBase.NoGraphicsMode:
            Assert.skipTest("Test cannot be run in NoGraphicsMode (because it uses swath)")

        (clr.Convert(Sensor.m_Satellite, ISatellite)).SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        tb = clr.CastAs((clr.Convert(Sensor.m_Satellite, ISatellite)).Propagator, IVehiclePropagatorTwoBody)
        # Propagate
        tb.Propagate()
        self.ConfigureAndComputeSensorSwath(Sensor.m_Object)

    def ConfigureAndComputeSensorSwath(self, sensor):
        # Configure swath display properties
        swath = sensor.Swath
        swath.Enable = True
        swath.Color = Color.Red  # red
        swath.LineStyle = AgELineStyle.eLMSDash
        swath.LineWidth = AgELineWidth.e2

        # New swath properties
        swath.UseMaximumCone = True
        swath.CurvatureTolerance = 90.0
        swath.ScatteringTolerance = 70.0
        swath.MinimumStep = 5
        swath.MaximumStep = 10

        swath.AddTimeInterval("1 Jan 2012 12:00:00.000", "1 Jan 2012 13:00:00.000")
        swath.AddTimeInterval("1 Jan 2012 14:00:00.000", "1 Jan 2012 15:00:00.000")

    # endregion

    # region ConfigureSensorVOProjection
    @category("VO Tests")
    def test_ConfigureSensorVOProjection(self):
        if TestBase.NoGraphicsMode:
            Assert.skipTest("Test cannot be run in NoGraphicsMode (because it uses VO)")

        self.ConfigureSensorVOProjection(Sensor.m_Object.VO)

    def ConfigureSensorVOProjection(self, sensorVo):
        sensorVo.ProjectionType = AgESnVOProjectionType.eProjectionAllIntersections
        sensorVo.InheritFrom2D = AgESnVOInheritFrom2D.eSnVOInheritFrom2DExtentOnly
        sensorVo.SpaceProjection = 2000.0

    # endregion

    # region ConfigureSensorVOProjectionTimeVarying
    @category("VO Tests")
    def test_ConfigureSensorVOProjectionTimeVarying(self):
        if TestBase.NoGraphicsMode:
            Assert.skipTest("Test cannot be run in NoGraphicsMode (because it uses VO)")

        self.ConfigureSensorVOProjectionTimeVarying(Sensor.m_Object.VO)

    def ConfigureSensorVOProjectionTimeVarying(self, sensorVo):
        sensorVo.ProjectionType = AgESnVOProjectionType.eProjectionAllIntersections
        sensorVo.ProjectionTimeDependency = AgESnVOProjectionTimeDependencyType.eSnVOTimeVarying
        elem1 = sensorVo.SpaceProjectionIntervals.Add()
        elem1.Distance = 5000.0
        elem1.Time = "1 Jan 2012 12:00:00.000"
        elem2 = sensorVo.SpaceProjectionIntervals.Add()
        elem2.Distance = 2000.0
        elem2.Time = "1 Jan 2012 16:00:00.000"
        elem3 = sensorVo.SpaceProjectionIntervals.Add()
        elem3.Distance = 4000.0
        elem3.Time = "1 Jan 2012 20:00:00.000"

    # endregion
