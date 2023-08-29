from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class Vehicle(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_DefaultName: str = "MyVehicle"
        super(Vehicle, self).__init__(*args, **kwargs)

    m_Object: "IGroundVehicle" = None

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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.GROUND_VEHICLE, self.m_DefaultName
            ),
            IGroundVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        (clr.Convert(Vehicle.m_Object, IStkObject)).unload()

    # endregion

    # region ExportVehicleToStkEphemerisFile
    def test_ExportVehicleToStkEphemerisFile(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            IGroundVehicle,
        )
        ga: "IVehiclePropagatorGreatArc" = clr.CastAs(gv.route, IVehiclePropagatorGreatArc)
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()
        ephemFilePath: str = TestBase.TemporaryDirectory + "\\OMExternalFileStk.e"
        self.ExportVehicleToStkEphemerisFile(
            clr.Convert(CodeSnippetsTestBase.m_Root.current_scenario, IScenario),
            gv.export_tools.get_ephemeris_stk_export_tool(),
            ephemFilePath,
        )
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1")

    def ExportVehicleToStkEphemerisFile(
        self, scenario: "IScenario", stkEphem: "IVehicleEphemerisStkExportTool", ephemFilePath: str
    ):
        # set export parameters
        stkEphem.coordinate_system = STK_EPHEM_COORDINATE_SYSTEM.FIXED
        stkEphem.include_interp = True
        stkEphem.version_format = EXPORT_TOOL_VERSION_FORMAT.CURRENT
        stkEphem.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY

        # Set the ephemeris to the Scenario start and stop times
        stkEphem.time_period.start = scenario.start_time
        stkEphem.time_period.stop = scenario.stop_time

        stkEphem.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.EPHEM
        stkEphem.export(ephemFilePath)

    # endregion

    # region ExportVehicleToAttitudeFile
    def test_ExportVehicleToAttitudeFile(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            IGroundVehicle,
        )
        ga: "IVehiclePropagatorGreatArc" = clr.CastAs(gv.route, IVehiclePropagatorGreatArc)
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()
        self.ExportVehicleToAttitudeFile(
            clr.Convert(CodeSnippetsTestBase.m_Root.current_scenario, IScenario),
            gv.export_tools.get_attitude_export_tool(),
        )
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1")

    def ExportVehicleToAttitudeFile(self, scenario: "IScenario", attitudeExport: "IVehicleAttitudeExportTool"):
        # Set and configure attitude coordinate axes
        attitudeExport.set_coordinate_axes_type(ATT_COORDINATE_AXES.CUSTOM)
        customAxes: "IVehicleCoordinateAxesCustom" = clr.CastAs(
            attitudeExport.coordinate_axes, IVehicleCoordinateAxesCustom
        )
        customAxes.reference_axes_name = "CentralBody/Sun J2000 Axes"

        attitudeExport.version_format = EXPORT_TOOL_VERSION_FORMAT.CURRENT
        attitudeExport.include = ATT_INCLUDE.QUATERNIONS_ANGULAR_VELOCITY

        # Set the attitude file to use Scenario start and stop time
        attitudeExport.time_period.time_period_type = EXPORT_TOOL_TIME_PERIOD.SPECIFY
        attitudeExport.time_period.start = scenario.start_time
        attitudeExport.time_period.stop = scenario.stop_time

        attitudeExport.step_size.step_size_type = EXPORT_TOOL_STEP_SIZE.SPECIFY
        attitudeExport.step_size.value = 3600

        # Save Attitude File
        attitudeExport.export("OMExternalFileAttitude.a")

    # endregion

    # region AddGroundEllipseElementAndDataElement
    def test_AddGroundEllipseElementAndDataElement(self):
        self.AddGroundEllipseElementAndDataElement(Vehicle.m_Object.ground_ellipses)

    def AddGroundEllipseElementAndDataElement(self, ellipsesCollection: "IVehicleGroundEllipsesCollection"):
        # Add ground ellipse
        ellipse: "IVehicleGroundEllipseElement" = ellipsesCollection.add("MyEllipses")

        # Add ellipse data element
        element: "IVehicleEllipseDataElement" = ellipse.ellipse_data.add()

        # Configure element properties
        element.time = "1 Jan 2012 12:00:00.000"
        element.latitude = 35.292
        element.longitude = -93.7299
        element.semi_major_axis = 400.0
        element.semi_minor_axis = 300.0
        element.bearing = 35.71

    # endregion
