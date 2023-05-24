import sys
import os

sys.path.insert(1, os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class Vehicle(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_DefaultName = "MyVehicle"
        super(Vehicle, self).__init__(*args, **kwargs)

    m_Object = None

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
        Vehicle.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eGroundVehicle, self.m_DefaultName
            ),
            IGroundVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        (clr.Convert(Vehicle.m_Object, IStkObject)).Unload()

    # endregion

    # region ExportVehicleToStkEphemerisFile
    @category("PySTKFixTest-NoServerAvailable")
    def test_ExportVehicleToStkEphemerisFile(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        ga = clr.CastAs(gv.Route, IVehiclePropagatorGreatArc)
        ga.Waypoints.Add()
        ga.Waypoints.Add()
        ga.Propagate()
        ephemFilePath = TestBase.TemporaryDirectory + "\\OMExternalFileStk.e"
        self.ExportVehicleToStkEphemerisFile(
            clr.Convert(CodeSnippetsTestBase.m_Root.CurrentScenario, IScenario),
            gv.ExportTools.GetEphemerisStkExportTool(),
            ephemFilePath,
        )
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eGroundVehicle, "gv1")

    def ExportVehicleToStkEphemerisFile(self, scenario, stkEphem, ephemFilePath):
        # set export parameters
        stkEphem.CoordinateSystem = AgEStkEphemCoordinateSystem.eStkEphemCoordinateSystemFixed
        stkEphem.IncludeInterp = True
        stkEphem.VersionFormat = AgEExportToolVersionFormat.eExportToolVersionFormatCurrent
        stkEphem.TimePeriod.TimePeriodType = AgEExportToolTimePeriod.eExportToolTimePeriodSpecify

        # Set the ephemeris to the Scenario start and stop times
        stkEphem.TimePeriod.Start = scenario.StartTime
        stkEphem.TimePeriod.Stop = scenario.StopTime

        stkEphem.StepSize.StepSizeType = AgEExportToolStepSize.eExportToolStepSizeEphem
        stkEphem.Export(ephemFilePath)

    # endregion

    # region ExportVehicleToAttitudeFile
    @category("PySTKFixTest-NoServerAvailable")
    def test_ExportVehicleToAttitudeFile(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        ga = clr.CastAs(gv.Route, IVehiclePropagatorGreatArc)
        ga.Waypoints.Add()
        ga.Waypoints.Add()
        ga.Propagate()
        self.ExportVehicleToAttitudeFile(
            clr.Convert(CodeSnippetsTestBase.m_Root.CurrentScenario, IScenario), gv.ExportTools.GetAttitudeExportTool()
        )
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eGroundVehicle, "gv1")

    def ExportVehicleToAttitudeFile(self, scenario, attitudeExport):
        # Set and configure attitude coordinate axes
        attitudeExport.SetCoordinateAxesType(AgEAttCoordinateAxes.eAttCoordinateAxesCustom)
        customAxes = clr.CastAs(attitudeExport.CoordinateAxes, IVehicleCoordinateAxesCustom)
        customAxes.ReferenceAxesName = "CentralBody/Sun J2000 Axes"

        attitudeExport.VersionFormat = AgEExportToolVersionFormat.eExportToolVersionFormatCurrent
        attitudeExport.Include = AgEAttInclude.eAttIncludeQuaternionsAngularVelocity

        # Set the attitude file to use Scenario start and stop time
        attitudeExport.TimePeriod.TimePeriodType = AgEExportToolTimePeriod.eExportToolTimePeriodSpecify
        attitudeExport.TimePeriod.Start = scenario.StartTime
        attitudeExport.TimePeriod.Stop = scenario.StopTime

        attitudeExport.StepSize.StepSizeType = AgEExportToolStepSize.eExportToolStepSizeSpecify
        attitudeExport.StepSize.Value = 3600

        # Save Attitude File
        attitudeExport.Export("OMExternalFileAttitude.a")

    # endregion

    # region AddGroundEllipseElementAndDataElement
    def test_AddGroundEllipseElementAndDataElement(self):
        self.AddGroundEllipseElementAndDataElement(Vehicle.m_Object.GroundEllipses)

    def AddGroundEllipseElementAndDataElement(self, ellipsesCollection):
        # Add ground ellipse
        ellipse = ellipsesCollection.Add("MyEllipses")

        # Add ellipse data element
        element = ellipse.EllipseData.Add()

        # Configure element properties
        element.Time = "1 Jan 2012 12:00:00.000"
        element.Latitude = 35.292
        element.Longitude = -93.7299
        element.SemiMajorAxis = 400.0
        element.SemiMinorAxis = 300.0
        element.Bearing = 35.71

    # endregion
