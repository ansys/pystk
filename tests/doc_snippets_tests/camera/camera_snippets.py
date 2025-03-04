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


class CameraSnippets(CodeSnippetsTestBase):
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
    def test_CameraExtentsSnippet(self):
        try:
            scenario = self.get_scenario()
            installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
            imageryTile = scenario.scene_manager.scenes.item(0).central_bodies.earth.imagery.add_uri_string(
                os.path.join(
                    installPath, "Data", "Resources", "stktraining", "imagery", "NPS_OrganPipeCactus_Map.pdttx"
                )
            )

            self.CameraExtentsSnippet(scenario, imageryTile)
        finally:
            scenario.scene_manager.scenes.item(0).central_bodies.earth.imagery.remove(imageryTile)

    @code_snippet(
        name="CameraExtents",
        description="Change camera view to Imagery Extents",
        category="Camera",
        eid="AgSTKGraphicsLib~IAgStkGraphicsCamera",
    )
    def CameraExtentsSnippet(self, scenario, imageryTile):
        # Scenario scenario: Scenario object
        # AGIProcessedImageGlobeOverlay imageryTile: Image Overlay object
        manager = scenario.scene_manager
        extent = imageryTile.extent
        # Change extent in the default 3D window
        manager.scenes.item(0).camera.view_extent("Earth", extent)
        manager.render()

    @category("VO Tests")
    def test_CameraReferenceFrameSnippet(self):
        self.CameraReferenceFrameSnippet(self.get_root(), self.get_scenario())

    @code_snippet(
        name="CameraReferenceFrame",
        description="Change camera reference frame",
        category="Camera",
        eid="AgSTKGraphicsLib~IAgStkGraphicsCamera",
    )
    def CameraReferenceFrameSnippet(self, root, scenario):
        # Scenario scenario: Scenario object
        # StkObjectRoot root: STK Object Model Root
        manager = scenario.scene_manager
        manager.scenes.item(0).camera.view_central_body(
            "Earth", root.central_bodies.earth.analysis_workbench_components.axes.item("Fixed")
        )
        manager.render()
