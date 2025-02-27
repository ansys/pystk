# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

import os
import sys

from ansys.stk.core.stkobjects import (
    ClassicalLocation,
    ClassicalSizeShape,
    LeadTrailData,
    LineWidth,
    OrientationAscNode,
    STKObjectType,
    VehicleGraphics2DAttributeType,
    VehicleGraphics2DElevation,
    VehicleGraphics2DOptionType,
    VehicleIntegrationModel,
    VehicleInterpolationMethod,
    VehicleMethod,
    AttitudeProfile,
    PropagatorType,
    Graphics3DFontSize,
    Graphics3DMarkerOrientation,
)
from ansys.stk.core.stkutil import CoordinateSystem, LineStyle, OrbitStateType
from ansys.stk.core.utilities.colors import Colors

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class SatelliteSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_root(self):
        return CodeSnippetsTestBase.m_Root

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.current_scenario

    def test_CreateSatelliteSnippet(self):
        self.CreateSatelliteSnippet(self.get_root())

    @code_snippet(
        name="CreateSatellite",
        description="Create a satellite (on the current scenario central body)",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgSatellite",
    )
    def CreateSatelliteSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        satellite = root.current_scenario.children.new(STKObjectType.SATELLITE, "MySatellite")

    def test_SatelliteInitialStateSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.SatelliteInitialStateSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="SatelliteInitialState",
        description="Set initial state of satellite and propagate",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgOrbitStateClassical",
    )
    def SatelliteInitialStateSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        keplerian = satellite.propagator.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
        keplerian.size_shape_type = ClassicalSizeShape.ALTITUDE
        keplerian.location_type = ClassicalLocation.TRUE_ANOMALY
        keplerian.orientation.ascending_node_type = OrientationAscNode.LONGITUDE_ASCENDING_NODE

        # Assign the perigee and apogee altitude values:
        keplerian.size_shape.perigee_altitude = 500  # km
        keplerian.size_shape.apogee_altitude = 600  # km

        # Assign the other desired orbital parameters:
        keplerian.orientation.inclination = 90  # deg
        keplerian.orientation.argument_of_periapsis = 12  # deg
        keplerian.orientation.ascending_node.value = 24  # deg
        keplerian.location.value = 180  # deg

        # Apply the changes made to the satellite's state and propagate:
        satellite.propagator.initial_state.representation.assign(keplerian)
        satellite.propagator.propagate()

    def test_J4SatelliteSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.J4SatelliteSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="J4Satellite",
        description="Set satellite propagator to J4 and assign cartesian position",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgVePropagatorJ4Perturbation",
    )
    def J4SatelliteSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        satellite.set_propagator_type(PropagatorType.J4_PERTURBATION)
        propagator = satellite.propagator
        propagator.initial_state.representation.assign_cartesian(
            CoordinateSystem.ICRF, 6678.14, 0, 0, 0, 6.78953, 3.68641
        )
        propagator.propagate()

    def test_HPOPSatelliteSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.HPOPSatelliteSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="HPOPSatellite",
        description="Set satellite propagator to HPOP and set force model properties",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgVePropagatorHPOP",
    )
    def HPOPSatelliteSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        satellite.set_propagator_type(PropagatorType.HPOP)
        satellite.propagator.step = 60
        satellite.propagator.initial_state.representation.assign_cartesian(
            CoordinateSystem.FIXED, 6406.92, -1787.59, -506.422, 2.10185, 6.48871, 3.64041
        )

        forceModel = satellite.propagator.force_model
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        forceModel.central_body_gravity.file = os.path.join(
            installPath, "STKData", "CentralBodies", "Earth", "WGS84_EGM96.grv"
        )
        forceModel.central_body_gravity.maximum_degree = 21
        forceModel.central_body_gravity.maximum_order = 21
        forceModel.drag.use = True
        forceModel.drag.drag_model.cd = 0.01
        forceModel.drag.drag_model.area_mass_ratio = 0.01
        forceModel.solar_radiation_pressure.use = False

        integrator = satellite.propagator.integrator
        integrator.do_not_propagate_below_altitude = -1e6
        integrator.integration_model = VehicleIntegrationModel.RUNGE_KUTTA_FEHLBERG_78
        integrator.step_size_control.method = VehicleMethod.RELATIVE_ERROR
        integrator.step_size_control.error_tolerance = 1e-13
        integrator.step_size_control.minimum_step_size = 0.1
        integrator.step_size_control.maximum_step_size = 30
        integrator.interpolation.method = VehicleInterpolationMethod.LAGRANGE
        integrator.interpolation.order = 7

        satellite.propagator.propagate()

    def test_AstrogatorSatelliteSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.AstrogatorSatelliteSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="AstrogatorSatellite",
        description="Set satellite propagator to Astrogator and clear segments",
        category="STK Objects | Satellite",
        eid="AgStkGatorLib~IAgVADriverMCS",
    )
    def AstrogatorSatelliteSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        satellite.set_propagator_type(PropagatorType.ASTROGATOR)
        driver = satellite.propagator
        # Clear all segments from the MCS
        driver.main_sequence.remove_all()

    def test_SPICESatelliteSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.SPICESatelliteSnippet(self.get_root(), satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="SPICESatellite",
        description="Set satellite propagator to SPICE and propagate",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgVePropagatorSPICE",
    )
    def SPICESatelliteSnippet(self, root, satellite):
        # Satellitesatellite: Satellite object
        # StkObjectRoot root: STK Object Model Root
        satellite.set_propagator_type(PropagatorType.SPICE)
        propagator = satellite.propagator
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        propagator.spice = os.path.join(
            installPath, "STKData", "Spice", "planets.bsp"
        )  # Make sure this is a valid path
        propagator.body_name = "MARS"

        propagator.ephemeris_interval.set_implicit_interval(
            root.current_scenario.analysis_workbench_components.time_intervals.item("AnalysisInterval")
        )  # Link to scenario period
        propagator.step = 60.0
        propagator.propagate()

    def test_SGP4SatelliteSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.SGP4SatelliteSnippet(self.get_root(), satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="SGP4Satellite",
        description="Set satellite propagator to SGP4 and propagate",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgVePropagatorSGP4",
    )
    def SGP4SatelliteSnippet(self, root, satellite):
        # Satellitesatellite: Satellite object
        satellite.set_propagator_type(PropagatorType.SGP4)
        propagator = satellite.propagator
        propagator.ephemeris_interval.set_implicit_interval(
            root.current_scenario.analysis_workbench_components.time_intervals.item("AnalysisInterval")
        )  # Link to scenario period
        propagator.common_tasks.add_segments_from_online_source("25544")  # International Space Station
        propagator.automatic_update_enabled = True
        propagator.propagate()

    def test_ExportEphemerisFileSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.ExportEphemerisFileSnippet(self.get_root(), satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="ExportEphemerisFile",
        description="Export an ephemeris file to scenario folder",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgSaExportTools",
    )
    def ExportEphemerisFileSnippet(self, root, satellite):
        # StkObjectRoot root: STK Object Model Root
        # Satellitesatellite: Satellite object
        scenPath = root.execute_command("GetDirectory / Scenario").item(0)
        satelliteFilePath = "%s\\%s.e" % (scenPath, satellite.instance_name)
        satelliteFilePath = satelliteFilePath.replace("\\", "\\\\")
        satellite.export_tools.get_ephemeris_stk_export_tool().export(satelliteFilePath)

    def test_SatelliteAttitudeSpinningSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.SatelliteAttitudeSpinningSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="SatelliteAttitudeSpinning",
        description="Set satellite attitude basic spinning",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgSatellite | STKObjects~IAgVeOrbitAttitudeStandard",
    )
    def SatelliteAttitudeSpinningSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        basic = satellite.attitude.basic
        basic.set_profile_type(AttitudeProfile.SPINNING)
        basic.profile.body.assign_xyz(0, 0, 1)
        basic.profile.inertial.assign_xyz(0, 1, 0)
        basic.profile.rate = 6  # rev/sec

    def test_SatelliteAttitudeTargetSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()
            MyAreaTarget = self.get_scenario().children.new(STKObjectType.AREA_TARGET, "MyAreaTarget")

            self.SatelliteAttitudeTargetSnippet(satellite)
        finally:
            satellite.unload()
            MyAreaTarget.unload()

    @code_snippet(
        name="SatelliteAttitudeTarget",
        description="Set satellite attitude targeting",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgSatellite | STKObjects~IAgVeOrbitAttitudeStandard",
    )
    def SatelliteAttitudeTargetSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        attitudePointing = satellite.attitude.pointing
        attitudePointing.use_target_pointing = True
        attitudePointing.targets.remove_all()
        attitudePointing.targets.add("AreaTarget/MyAreaTarget")
        attitudePointing.target_times.use_access_times = True

    def test_SatelliteAttitudeExternalSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.SatelliteAttitudeExternalSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="SatelliteAttitudeExternal",
        description="Set satellite attitude external",
        category="STK Objects | Satellite",
        eid="STKObjects~IAgSatellite | STKObjects~IAgVeOrbitAttitudeStandard",
    )
    def SatelliteAttitudeExternalSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        satellite.attitude.external.load(
            os.path.join(installPath, "Data", "Resources", "stktraining", "text", "AttitudeTimeEulerAngles_Example.a")
        )

    @category("Graphics Tests")
    def test_SatelliteGraphicsResolutionSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.SatelliteGraphicsResolutionSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="SatelliteGraphicsResolution",
        description="Change the graphics resolution of the orbit for a smooth path",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVeGfxPassResolution",
    )
    def SatelliteGraphicsResolutionSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        resolution = satellite.graphics.resolution
        resolution.orbit = 60

    @category("Graphics Tests")
    def test_BasicGraphics2DSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.BasicGraphics2DSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="BasicGraphics2D",
        description="Set 2D Graphics display properties",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVeGfxAttributesBasic",
    )
    def BasicGraphics2DSnippet(self, satellite):
        # StkObjectRoot root: STK Object Model root
        # Satellitesatellite: Satellite object
        # Change the line width, style, color and marker

        graphics = satellite.graphics
        graphics.set_attributes_type(VehicleGraphics2DAttributeType.BASIC)
        attributes = graphics.attributes
        attributes.inherit = False
        attributes.line.width = LineWidth.WIDTH4
        attributes.line.style = LineStyle.LONG_DASH
        attributes.color = Colors.Lime
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        attributes.marker_style = os.path.join(installPath, "STKData", "Pixmaps", "MarkersWin", "m010Satellite.bmp")

    @category("Graphics Tests")
    def test_CustomGraphics2DSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.CustomGraphics2DSnippet(self.get_root(), satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="CustomGraphics2D",
        description="Set 2D Display times to Custom and add intervals",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVeGfxAttributesCustom",
    )
    def CustomGraphics2DSnippet(self, root, satellite):
        # StkObjectRoot root: STK Object Model root
        # Satellitesatellite: Satellite object
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        graphics = satellite.graphics
        graphics.set_attributes_type(VehicleGraphics2DAttributeType.CUSTOM)
        graphics.attributes.default.show_graphics = False

        interval1 = graphics.attributes.intervals.add(0, 3600)
        interval1.graphics_2d_attributes.show_graphics = True
        interval1.graphics_2d_attributes.inherit = False
        interval1.graphics_2d_attributes.line.width = LineWidth.WIDTH2
        interval1.graphics_2d_attributes.line.style = LineStyle.LONG_DASH
        interval1.graphics_2d_attributes.color = Colors.Fuchsia
        interval1.graphics_2d_attributes.marker_style = "X"

        interval2 = satellite.graphics.attributes.intervals.add(7200, 86400)
        interval2.graphics_2d_attributes.show_graphics = True
        interval2.graphics_2d_attributes.inherit = False
        interval2.graphics_2d_attributes.line.width = LineWidth.WIDTH2
        interval2.graphics_2d_attributes.line.style = LineStyle.DASHED
        interval2.graphics_2d_attributes.color = Colors.Lime
        interval2.graphics_2d_attributes.marker_style = "Point"

    @category("Graphics Tests")
    def test_GraphicsElevationContoursSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsElevationContoursSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsElevationContours",
        description="Set 2D/3D Elevation Contours",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVeGfxElevContours",
    )
    def GraphicsElevationContoursSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        # Set the contours in the 2D properties
        contours = satellite.graphics.elevation_contours
        contours.show_graphics = True
        contours.number_of_decimal_digits = 0
        contours.elevations.add_level_range(0, 90, 10)  # Min, Max, Step
        # Turn the contours on in the 3D properties
        satellite.graphics_3d.elevation_contours.show_graphics = True

    @category("Graphics Tests")
    def test_GraphicsRangeContoursSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsRangeContoursSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsRangeContours",
        description="Set 2D/3D Range Contours",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgGfxRangeContours",
    )
    def GraphicsRangeContoursSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        # Set a contour level in the 2D properties
        rangeContours = satellite.graphics.range_contours
        rangeContours.show_graphics = True
        rangeLevel = rangeContours.level_attributes.add_level(2000)  # km
        rangeLevel.color = Colors.Fuchsia
        rangeLevel.line_width = LineWidth.WIDTH5
        rangeLevel.label_angle = 90
        rangeLevel.show_user_text_visible = True
        rangeLevel.user_text = "Range"
        # Turn the contours on in the 3D properties
        satellite.graphics_3d.range_contours.show_graphics = True

    @category("Graphics Tests")
    def test_GraphicsSwathSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsSwathSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsSwath",
        description="Set 2D Swath",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVeGfxSwath",
    )
    def GraphicsSwathSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        # Set swath in the 2D properties
        swath = satellite.graphics.swath
        swath.set_elevation_type(VehicleGraphics2DElevation.ELEVATION_GROUND_ELEVATION)
        swath.elevation.angle = 30  # deg
        satellite.graphics.swath.options = VehicleGraphics2DOptionType.OPTIONS_EDGE_LIMITS

    @category("Graphics Tests")
    def test_GraphicsLightingSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsLightingSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsLighting",
        description="Set Vehicle Lighting Properties",
        category="STK Objects | Satellite | Graphics",
        eid="AgSTKGraphicsLib~IAgStkGraphicsLighting",
    )
    def GraphicsLightingSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        lighting = satellite.graphics.lighting
        # Settings for vehicle in sunlight
        sunlight = lighting.sunlight
        sunlight.visible = True
        sunlight.color = Colors.Yellow
        sunlight.line_width = LineWidth.WIDTH4
        # Settings for vehicle in penumbra
        penumbra = lighting.penumbra
        penumbra.visible = True
        penumbra.color = Colors.Orange
        penumbra.line_width = LineWidth.WIDTH3
        # Settings for vehicle in umbra
        umbra = lighting.umbra
        umbra.visible = True
        umbra.color = Colors.Red
        umbra.line_width = LineWidth.WIDTH2

    @category("Graphics Tests")
    def test_GraphicsPassSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsPassSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsPass",
        description="Set 2D/3D Pass Display Properties",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVeGfxOrbitPassData",
    )
    def GraphicsPassSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        # Display one pass for ground track and orbit on 2D
        passdata = satellite.graphics.pass_data
        groundTrack = passdata.ground_track
        groundTrack.set_lead_data_type(LeadTrailData.ONE_PASS)
        groundTrack.set_trail_same_as_lead
        orbit = passdata.orbit
        orbit.set_lead_data_type(LeadTrailData.ONE_PASS)
        orbit.set_trail_same_as_lead
        # Display one orbit pass and no ground track on 3D
        passdata3D = satellite.graphics_3d.satellite_pass.track_data.pass_data
        groundTrack3D = passdata3D.ground_track
        groundTrack3D.set_lead_data_type(LeadTrailData.NONE)
        groundTrack3D.set_trail_same_as_lead
        orbit3D = passdata3D.orbit
        orbit3D.set_lead_data_type(LeadTrailData.ONE_PASS)
        orbit3D.set_trail_same_as_lead

    @category("Graphics Tests")
    def test_GraphicsLabelSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsLabelSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsLabel",
        description="Change the Display Label of the vehicle",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgSaGraphics",
    )
    def GraphicsLabelSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        satellite.graphics.use_instance_name_label = False
        satellite.graphics.label_name = "Python Satellite"

    @category("VO Tests")
    def test_GraphicsDataDisplaySnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsDataDisplaySnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsDataDisplay",
        description="Add a Data Display to the 3D Window",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVODataDisplayElement",
    )
    def GraphicsDataDisplaySnippet(self, satellite):
        # Satellitesatellite: Satellite object
        # Remove all data displays so you can easily pick one that may already be in
        # the list
        satellite.graphics_3d.data_display.remove_all()
        # Add LLA data display and change size/title
        datadisplay = satellite.graphics_3d.data_display.add("LLA Position")
        datadisplay.show_graphics = True
        datadisplay.font_size = Graphics3DFontSize.MEDIUM
        datadisplay.title_text = "My Data Display"
        datadisplay.show_name = False

    @category("VO Tests")
    def test_GraphicsDroplineSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsDroplineSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsDropline",
        description=" Display droplines in 3D Window",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVeVODropLinePathItemCollection",
    )
    def GraphicsDroplineSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        orbitDroplines = satellite.graphics_3d.drop_lines.orbit
        wgs84 = orbitDroplines.item(0)  # Droplines to WGS84 surface
        wgs84.show_graphics = True
        wgs84.line_width = LineWidth.WIDTH2
        wgs84.use_2d_color = False
        wgs84.color = Colors.Red

    @category("VO Tests")
    def test_GraphicsModelSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsModelSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsModel",
        description="Change the 3D Model and marker properties",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgSaVOModel",
    )
    def GraphicsModelSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        model = satellite.graphics_3d.model
        model.model_data.filename = r"STKData\VO\Models\Space\dsp.glb"
        orbitmarker = model.orbit_marker
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        orbitmarker.set_marker_image_filename(os.path.join(installPath, "STKData", "VO", "Markers", "Satellite.ppm"))
        orbitmarker.marker_data.is_transparent = True
        orbitmarker.pixel_size = 18
        orbitmarker.orientation_mode = Graphics3DMarkerOrientation.FOLLOW_DIRECTION

    @category("VO Tests")
    def test_GraphicsDetailsSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsDetailsSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsDetails",
        description="Modify the Detail Thresholds Levels",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVODetailThreshold",
    )
    def GraphicsDetailsSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        details = satellite.graphics_3d.model.detail_threshold
        details.enable_detail_threshold = True
        details.all = 1  # km
        details.model_label = 2  # km
        details.marker_label = 40000  # km
        details.marker = 500000  # km
        details.point = 500000  # km

    @category("VO Tests")
    def test_GraphicsOrbitSystemSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GraphicsOrbitSystemSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GraphicsOrbitSystem",
        description="Add Fixed System Orbit System in 3D Display",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVeVOSystemsCollection",
    )
    def GraphicsOrbitSystemSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        orbitsystems = satellite.graphics_3d.orbit_systems
        orbitsystems.fixed_by_window.show_graphics = True
        orbitsystems.fixed_by_window.inherit = False
        orbitsystems.fixed_by_window.color = Colors.Yellow

    @category("Graphics Tests")
    def test_AddGraphicsVectorSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()
            MySatellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "MySatellite")
            MySatellite.propagator.propagate()

            self.AddGraphicsVectorSnippet(satellite)
        finally:
            satellite.unload()
            MySatellite.unload()

    @code_snippet(
        name="AddGraphicsVector",
        description="Add a Vector to display in 3D",
        category="STK Objects | Satellite | Graphics",
        eid="STKObjects~IAgVOVector",
    )
    def AddGraphicsVectorSnippet(self, satellite):
        # Satellitesatellite: Satellite object
        vector = satellite.graphics_3d.vector
        angVel = vector.vector_geometry_tool_components.add(0, "Satellite/MySatellite AngVelocity")
        angVel.show_label = True
