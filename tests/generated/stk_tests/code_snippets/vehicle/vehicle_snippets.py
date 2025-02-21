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
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class VehicleSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_DefaultName: str = "MyVehicle"
        super(VehicleSnippets, self).__init__(*args, **kwargs)

    m_Object: "GroundVehicle" = None

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
        VehicleSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, self.m_DefaultName),
            GroundVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        (IStkObject(VehicleSnippets.m_Object)).unload()

    # endregion

    # region ExportVehicleToStkEphemerisFile
    def test_ExportVehicleToStkEphemerisFile(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        ga: "PropagatorGreatArc" = clr.CastAs(gv.route, PropagatorGreatArc)
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()
        ephemFilePath: str = TestBase.TemporaryDirectory + "\\OMExternalFileStk.e"
        self.ExportVehicleToStkEphemerisFile(
            Scenario(CodeSnippetsTestBase.m_Root.current_scenario),
            gv.export_tools.get_ephemeris_stk_export_tool(),
            ephemFilePath,
        )
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.GROUND_VEHICLE, "gv1")

    def ExportVehicleToStkEphemerisFile(
        self, scenario: "Scenario", stkEphem: "VehicleEphemerisExportTool", ephemFilePath: str
    ):
        # set export parameters
        stkEphem.coordinate_system = EphemerisCoordinateSystemType.FIXED
        stkEphem.include_interpolation_boundaries = True
        stkEphem.version_format = ExportToolVersionFormat.CURRENT
        stkEphem.time_period.time_period_type = ExportToolTimePeriodType.SPECIFY

        # Set the ephemeris to the Scenario start and stop times
        stkEphem.time_period.start = scenario.start_time
        stkEphem.time_period.stop = scenario.stop_time

        stkEphem.step_size.step_size_type = ExportToolStepSizeType.EPHEMERIS
        stkEphem.export(ephemFilePath)

    # endregion

    # region ExportVehicleToAttitudeFile
    def test_ExportVehicleToAttitudeFile(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        ga: "PropagatorGreatArc" = clr.CastAs(gv.route, PropagatorGreatArc)
        ga.waypoints.add()
        ga.waypoints.add()
        ga.propagate()
        self.ExportVehicleToAttitudeFile(
            Scenario(CodeSnippetsTestBase.m_Root.current_scenario), gv.export_tools.get_attitude_export_tool()
        )
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.GROUND_VEHICLE, "gv1")

    def ExportVehicleToAttitudeFile(self, scenario: "Scenario", attitudeExport: "VehicleAttitudeExportTool"):
        # Set and configure attitude coordinate axes
        attitudeExport.set_coordinate_axes_type(AttitudeCoordinateAxes.CUSTOM)
        customAxes: "VehicleCoordinateAxesCustom" = clr.CastAs(
            attitudeExport.coordinate_axes, VehicleCoordinateAxesCustom
        )
        customAxes.reference_axes_name = "CentralBody/Sun J2000 Axes"

        attitudeExport.version_format = ExportToolVersionFormat.CURRENT
        attitudeExport.include = AttitudeInclude.QUATERNIONS_AND_ANGULAR_VELOCITY

        # Set the attitude file to use Scenario start and stop time
        attitudeExport.time_period.time_period_type = ExportToolTimePeriodType.SPECIFY
        attitudeExport.time_period.start = scenario.start_time
        attitudeExport.time_period.stop = scenario.stop_time

        attitudeExport.step_size.step_size_type = ExportToolStepSizeType.SPECIFY
        attitudeExport.step_size.value = 3600

        # Save Attitude File
        attitudeExport.export("OMExternalFileAttitude.a")

    # endregion

    # region AddGroundEllipseElementAndDataElement
    def test_AddGroundEllipseElementAndDataElement(self):
        self.AddGroundEllipseElementAndDataElement(VehicleSnippets.m_Object.ground_ellipses)

    def AddGroundEllipseElementAndDataElement(self, ellipsesCollection: "VehicleGroundEllipsesCollection"):
        # Add ground ellipse
        ellipse: "VehicleGroundEllipseElement" = ellipsesCollection.add("MyEllipses")

        # Add ellipse data element
        element: "VehicleEllipseDataElement" = ellipse.ellipse_data.add()

        # Configure element properties
        element.time = "1 Jan 2012 12:00:00.000"
        element.latitude = 35.292
        element.longitude = -93.7299
        element.semi_major_axis = 400.0
        element.semi_minor_axis = 300.0
        element.bearing = 35.71

    # endregion
