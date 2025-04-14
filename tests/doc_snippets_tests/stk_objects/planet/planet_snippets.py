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

from ansys.stk.core.stkobjects import EphemSourceType, STKObjectType
from ansys.stk.core.utilities.colors import Colors

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class PlanetSnippets(CodeSnippetsTestBase):
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

    def test_CreatePlanetSnippet(self):
        self.CreatePlanetSnippet(self.get_scenario())

    @code_snippet(
        name="CreatePlanet",
        description="Create a New Planet",
        category="STK Objects | Planet",
        eid="stkobjects~Planet",
    )
    def CreatePlanetSnippet(self, scenario):
        # Scenario scenario: Scenario object
        planet = scenario.children.new(STKObjectType.PLANET, "Mars")
        planet.common_tasks.set_position_source_central_body("Mars", EphemSourceType.JPL_DEVELOPMENTAL_EPHEMERIS)

    @category("Graphics Tests")
    def test_PlanetGraphicsSnippet(self):
        try:
            planet = self.get_scenario().children.new(STKObjectType.PLANET, "planet")

            self.PlanetGraphicsSnippet(planet)
        finally:
            planet.unload()

    @code_snippet(
        name="ModifyPlanet2DGraphics",
        description="Modify Planet 2D Properties",
        category="STK Objects | Planet | Graphics",
        eid="stkobjects~Planet",
    )
    def PlanetGraphicsSnippet(self, planet):
        # Planet planet: Planet object
        planet2D = planet.graphics
        planet2D.color = Colors.Red
        planet2D.inherit = False
        planet2D.show_orbit = True
        planet2D.show_sub_planet_point = False
        planet2D.show_sub_planet_label = False
