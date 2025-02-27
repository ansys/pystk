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


# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class GlobeOverlaysSnippets(CodeSnippetsTestBase):
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
    def test_AddTerrainImagerySnippet(self):
        self.AddTerrainImagerySnippet(self.get_scenario())

    @code_snippet(
        name="AddTerrainImagery",
        description="Add Imagery and Terrain to the Scene",
        category="Graphics | GlobeOverlays",
        eid="AgSTKGraphicsLib~IAgStkGraphicsCentralBodyGraphics",
    )
    def AddTerrainImagerySnippet(self, scenario):
        # Scenario scenario: Scenario object
        # Retrieve the boundaries of the imported files
        manager = scenario.scene_manager
        # Add Terrain
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        terrainTile = manager.scenes.item(0).central_bodies.earth.terrain.add_uri_string(
            os.path.join(installPath, "Data", "Resources", "stktraining", "samples", "SRTM_Skopje.pdtt")
        )
        extentTerrain = terrainTile.extent
        print(
            "Terrain boundaries: LatMin: %s LatMax: %s LonMin: %s LonMax: %s"
            % (str(extentTerrain[0]), str(extentTerrain[2]), str(extentTerrain[1]), str(extentTerrain[3]))
        )
        # Add Imagery
        imageryTile = manager.scenes.item(0).central_bodies.earth.imagery.add_uri_string(
            os.path.join(installPath, "Data", "Resources", "stktraining", "imagery", "NPS_OrganPipeCactus_Map.pdttx")
        )
        extentImagery = imageryTile.extent
        print(
            "Imagery boundaries: LatMin: %s LatMax: %s LonMin: %s LonMax: %s"
            % (str(extentImagery[0]), str(extentImagery[2]), str(extentImagery[1]), str(extentImagery[3]))
        )

    @category("VO Tests")
    def test_DisplayStarsWaterSnippet(self):
        self.DisplayStarsWaterSnippet(self.get_scenario())

    @code_snippet(
        name="DisplayStarsWater",
        description="Control Display of Stars and Water Texture",
        category="Graphics | GlobeOverlays",
        eid="AgSTKGraphicsLib~IAgStkGraphicsScene",
    )
    def DisplayStarsWaterSnippet(self, scenario):
        # Scenario scenario: Scenario object
        # Turn off the stars and water texture
        manager = scenario.scene_manager
        manager.scenes.item(0).show_stars = False
        manager.scenes.item(0).show_water_surface = False

    @category("VO Tests")
    def test_SceneLightingSnippet(self):
        self.SceneLightingSnippet(self.get_scenario())

    @code_snippet(
        name="SceneLighting",
        description="Control the Lighting of the 3D scene",
        category="Graphics | GlobeOverlays",
        eid="AgSTKGraphicsLib~IAgStkGraphicsLighting",
    )
    def SceneLightingSnippet(self, scenario):
        # Scenario scenario: Scenario object
        # Modify the lighting levels
        manager = scenario.scene_manager
        lighting = manager.scenes.item(0).lighting
        lighting.ambient_intensity = 0.20  # Percent
        lighting.diffuse_intensity = 4  # Percent
        lighting.night_lights_intensity = 5  # Percent
