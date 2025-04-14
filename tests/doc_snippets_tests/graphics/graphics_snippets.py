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

from ansys.stk.core.graphics import FontStyle, ScreenOverlayOrigin, ScreenOverlayUnit
from ansys.stk.core.stkobjects import STKObjectType
from ansys.stk.core.stkutil import AzElAboutBoresight
from ansys.stk.core.utilities.colors import Colors

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class GraphicsSnippets(CodeSnippetsTestBase):
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

    @category("VO Tests")
    def test_GreatArcInterpolatorSnippet(self):
        self.GreatArcInterpolatorSnippet(self.get_scenario())

    @code_snippet(
        name="GreatArcInterpolatorPrimitives",
        description="Great Arc Interpolator Primitives",
        category="Graphics",
        eid="graphics~GreatArcInterpolatorFactory",
    )
    def GreatArcInterpolatorSnippet(self, scenario):
        # Scenario scenario: Scenario object
        # Create a array of LLA values and interoplate them over the specified
        # central body
        positionArray = [[35.017], [-118.540], [0], [44.570], [-96.474], [0], [31.101], [-82.619], [0]]
        manager = scenario.scene_manager
        # Interpolate points over great arc
        interpolator = manager.initializers.great_arc_interpolator.initialize_with_central_body("Earth")
        interpolator.granularity = 0.1
        result = interpolator.interpolate(positionArray)

    @category("VO Tests")
    def test_SurfaceMeshPrimitiveSnippet(self):
        self.SurfaceMeshPrimitiveSnippet(self.get_scenario())

    @code_snippet(
        name="DrawNewSurfaceMeshPrimitive",
        description="Draw a new Surface Mesh",
        category="Graphics",
        eid="graphics~SurfaceMeshPrimitive",
    )
    def SurfaceMeshPrimitiveSnippet(self, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        cartesianPts = [
            [6030.721052],
            [1956.627139],
            [-692.397578],
            [5568.375825],
            [2993.600713],
            [-841.076362],
            [5680.743568],
            [2490.379622],
            [-1480.882721],
        ]  # X, Y, Z (km)

        triangles = manager.initializers.surface_polygon_triangulator.compute("Earth", cartesianPts)
        surfaceMesh = manager.initializers.surface_mesh_primitive.initialize()
        surfaceMesh.color = Colors.Red
        surfaceMesh.set(triangles)
        manager.primitives.add(surfaceMesh)
        manager.render()

    @category("VO Tests")
    def test_SurfaceExtentTriangulatorSnippet(self):
        self.SurfaceExtentTriangulatorSnippet(self.get_scenario())

    @code_snippet(
        name="SurfaceExtentTriangulator",
        description="Draw a new Surface Extent Triangulator",
        category="Graphics",
        eid="graphics~SurfacePolygonTriangulatorInitializer",
    )
    def SurfaceExtentTriangulatorSnippet(self, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        texture_path = os.path.join(installPath, "STKData", "VO", "Textures", "AGI_logo_small.png")
        texture = manager.textures.load_from_string_uri(texture_path)
        mesh = manager.initializers.surface_mesh_primitive.initialize()
        mesh.texture = texture
        mesh.translucency = 0
        cartographicExtent = [[-55], [10], [-24], [30]]

        triangles = manager.initializers.surface_extent_triangulator.compute_simple("Earth", cartographicExtent)
        mesh.set(triangles)
        mesh.translucency = 0.25
        c0 = [[10], [-55]]
        c1 = [[30], [-55]]
        c2 = [[30], [-24]]
        c3 = [[10], [-24]]

        mesh.texture_matrix = manager.initializers.texture_matrix.initialize_with_rectangles(c0, c1, c2, c3)
        mesh.transparent_texture_border = True
        manager.primitives.add(mesh)
        manager.render()

    @category("VO Tests")
    def test_TextPrimitiveSnippet(self):
        self.TextPrimitiveSnippet(self.get_scenario())

    @code_snippet(
        name="TextPrimitive",
        description="Draw a new Text Primitive",
        category="Graphics",
        eid="graphics~TextBatchPrimitive",
    )
    def TextPrimitiveSnippet(self, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        font = manager.initializers.graphics_font.initialize_with_name_size_font_style_outline(
            "MS Sans Serif", 24, FontStyle.BOLD, True
        )
        textBatch = manager.initializers.text_batch_primitive.initialize_with_graphics_font(font)
        textBatch.set_cartographic("Earth", [[0], [0], [0]], ["Example Text"])  # Lat, Lon, Alt
        manager.primitives.add(textBatch)

    @category("VO Tests")
    def test_TextureScreenOverlaySnippet(self):
        self.TextureScreenOverlaySnippet(self.get_scenario())

    @code_snippet(
        name="DrawNewTextureScreenOverlay",
        description="Draw a new Texture Screen Overlay",
        category="Graphics",
        eid="graphics~TextureScreenOverlay",
    )
    def TextureScreenOverlaySnippet(self, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        overlays = manager.screen_overlays.overlays
        textureOverlay = manager.initializers.texture_screen_overlay.initialize_with_xy_width_height(0, 0, 128, 128)
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        textureOverlay.texture = manager.textures.load_from_string_uri(
            os.path.join(installPath, "STKData", "VO", "Textures", "agilogo3.ppm")
        )
        textureOverlay.maintain_aspect_ratio = True
        textureOverlay.origin = ScreenOverlayOrigin.TOP_LEFT
        textureOverlay.position = [
            [0],
            [20],
            [int(ScreenOverlayUnit.PIXEL)],
            [int(ScreenOverlayUnit.PIXEL)],
        ]
        overlays.add(textureOverlay)
        # Render the Scene
        manager.render()

    @category("VO Tests")
    def test_BoundingSpherePrimitiveSnippet(self):
        self.BoundingSpherePrimitiveSnippet(self.get_scenario())

    @code_snippet(
        name="BoundingSpherePrimitive",
        description="Create a Bounding Sphere",
        category="Graphics",
        eid="graphics~BoundingSphere",
    )
    def BoundingSpherePrimitiveSnippet(self, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        sphere = manager.initializers.bounding_sphere.initialize([[-1061.22], [-5773.98], [4456.04]], 100)

    @category("VO Tests")
    def test_PointPrimitiveSnippet(self):
        self.PointPrimitiveSnippet(self.get_scenario())

    @code_snippet(
        name="PointPrimitive",
        description="Draw a Point Primitive and set properties",
        category="Graphics",
        eid="graphics~PointBatchPrimitive",
    )
    def PointPrimitiveSnippet(self, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        point = manager.initializers.point_batch_primitive.initialize()
        ptPosition = [[0], [-1], [0]]  # Lat, Lon, Alt

        point.set_cartographic("Earth", ptPosition)
        point.pixel_size = 15
        point.color = Colors.Lime
        point.display_outline = True
        point.outline_width = 5
        point.outline_color = Colors.Red

        manager.primitives.add(point)
        # Render the Scene
        manager.render()

    @category("VO Tests")
    def test_SolidBoxPrimitiveSnippet(self):
        self.SolidBoxPrimitiveSnippet(self.get_root(), self.get_scenario())

    @code_snippet(
        name="SolidBoxPrimitive",
        description="Draw a Solid Box Primitive and set properties",
        category="Graphics",
        eid="graphics~SolidPrimitive",
    )
    def SolidBoxPrimitiveSnippet(self, root, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        originBox = root.conversion_utility.new_position_on_earth()
        originBox.assign_geodetic(0, 3, 100)

        orientBox = root.conversion_utility.new_orientation()
        orientBox.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

        size = [[100], [100], [200]]
        result = manager.initializers.box_triangulator.compute(size)
        solidBox = manager.initializers.solid_primitive.initialize()
        solidBox.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item("Fixed")
        solidBox.position = originBox.query_cartesian_array()
        solidBox.set_with_result(result)
        solidBox.color = Colors.Red
        solidBox.outline_color = Colors.Cyan
        solidBox.translucency = 0.75
        solidBox.rotation = orientBox
        manager.primitives.add(solidBox)
        manager.render()

    @category("VO Tests")
    def test_SolidEllipsoidPrimitiveSnippet(self):
        self.SolidEllipsoidPrimitiveSnippet(self.get_root(), self.get_scenario())

    @code_snippet(
        name="SolidEllipsoidPrimitive",
        description="Draw a Solid Ellipsoid Primitive and set properties",
        category="Graphics",
        eid="graphics~SolidPrimitive",
    )
    def SolidEllipsoidPrimitiveSnippet(self, root, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        originEllipsoid = root.conversion_utility.new_position_on_earth()
        originEllipsoid.assign_geodetic(0, 5, 100)

        orientEllipsoid = root.conversion_utility.new_orientation()
        orientEllipsoid.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

        radii = [[200], [100], [100]]
        ellipsoid = manager.initializers.ellipsoid_triangulator.compute_simple(radii)
        solidEllipsoid = manager.initializers.solid_primitive.initialize()
        solidEllipsoid.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item(
            "Fixed"
        )  # vgtSat.Systems.item('Body')
        solidEllipsoid.position = originEllipsoid.query_cartesian_array()
        solidEllipsoid.set_with_result(ellipsoid)
        solidEllipsoid.color = Colors.White
        solidEllipsoid.outline_color = Colors.DeepPink
        solidEllipsoid.translucency = 0.75
        solidEllipsoid.rotation = orientEllipsoid
        manager.primitives.add(solidEllipsoid)
        manager.render()

    @category("VO Tests")
    def test_SolidCylinderPrimitiveSnippet(self):
        self.SolidCylinderPrimitiveSnippet(self.get_root(), self.get_scenario())

    @code_snippet(
        name="SolidCylinderPrimitive",
        description="Draw a Solid Cylinder Primitive and set properties",
        category="Graphics",
        eid="graphics~SolidPrimitive",
    )
    def SolidCylinderPrimitiveSnippet(self, root, scenario):
        # Scenario scenario: Scenario object
        manager = scenario.scene_manager
        originCylinder = root.conversion_utility.new_position_on_earth()
        originCylinder.assign_geodetic(0, 7, 100)

        orientCylinder = root.conversion_utility.new_orientation()
        orientCylinder.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

        cylinder = manager.initializers.cylinder_triangulator.create_simple(200, 100)
        solidCylinder = manager.initializers.solid_primitive.initialize()
        solidCylinder.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item("Fixed")
        solidCylinder.position = originCylinder.query_cartesian_array()
        solidCylinder.set_with_result(cylinder)
        solidCylinder.color = Colors.Lime
        solidCylinder.outline_color = Colors.Blue
        solidCylinder.outline_width = 3
        solidCylinder.translucency = 0.75
        solidCylinder.rotation = orientCylinder
        manager.primitives.add(solidCylinder)
        manager.render()

    @category("VO Tests")
    def test_DisplayPrimitiveIntervalSnippet(self):
        try:
            scenario = self.get_scenario()
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            manager = self.get_scenario().scene_manager
            model = manager.initializers.model_primitive.initialize()
            manager.primitives.add(model)

            self.DisplayPrimitiveIntervalSnippet(self.get_root(), scenario, model)
        finally:
            parent.unload()
            manager.primitives.remove(model)

    @code_snippet(
        name="DisplayPrimitiveInterval",
        description="Display a Primitive During an Interval",
        category="Graphics",
        eid="graphics~CompositeDisplayCondition",
    )
    def DisplayPrimitiveIntervalSnippet(self, root, scenario, model):
        # Scenario scenario: Scenario object
        # ModelPrimitive model: Graphics Primitive
        manager = scenario.scene_manager
        composite = manager.initializers.composite_display_condition.initialize()
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        start = root.conversion_utility.new_date("EpSec", str(scenario.start_time))
        stop = root.conversion_utility.new_date("EpSec", str(scenario.start_time + 600))
        timeInterval = manager.initializers.time_interval_display_condition.initialize_with_times(start, stop)
        composite.add(timeInterval)
        model.display_condition = composite
