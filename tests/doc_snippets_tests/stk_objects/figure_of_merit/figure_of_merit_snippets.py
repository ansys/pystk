# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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
    FigureOfMeritCompute,
    FigureOfMeritDefinitionType,
    FigureOfMeritGraphics2DColorMethod,
    FigureOfMeritGraphics2DContourType,
    STKObjectType,
)
from ansys.stk.core.utilities.colors import Colors

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class FigureOfMeritSnippets(CodeSnippetsTestBase):
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

    def test_CreateFOMSnippet(self):
        try:
            coverage = self.get_scenario().children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")

            self.CreateFOMSnippet(coverage)
        finally:
            coverage.unload()

    @code_snippet(
        name="CreateFOM",
        description="Create a new Figure of Merit of type Access Duration",
        category="STK Objects | Figure Of Merit",
        eid="stkobjects~FigureOfMerit",
    )
    def CreateFOMSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        fom = coverage.children.new(STKObjectType.FIGURE_OF_MERIT, "AccessDuration")
        fom.set_definition_type(FigureOfMeritDefinitionType.ACCESS_DURATION)
        fom.definition.set_compute_type(FigureOfMeritCompute.MAXIMUM)

    @category("Graphics Tests")
    def test_FOMContoursColorRampSnippet(self):
        try:
            coverage = self.get_scenario().children.new(STKObjectType.COVERAGE_DEFINITION, "coverage")
            fom = coverage.children.new(STKObjectType.FIGURE_OF_MERIT, "fom")
            fom.set_definition_type(FigureOfMeritDefinitionType.NUMBER_OF_GAPS)

            self.FOMContoursColorRampSnippet(coverage, fom)
        finally:
            coverage.unload()

    @code_snippet(
        name="FOMContoursColorRamp",
        description="Configure the Contours of the figure of merit (FOM) and define a color ramp",
        category="STK Objects | Figure Of Merit",
        eid="stkobjects~FigureOfMerit",
    )
    def FOMContoursColorRampSnippet(self, coverage, fom):
        # CoverageDefinition coverage: Coverage object
        # FigureOfMerit fom: Figure Of Merit object
        satisfaction = coverage.graphics.static
        satisfaction.show_region = False
        Animation = fom.graphics_3d.animation_graphics_3d_settings
        Animation.show_graphics = False
        VOcontours = fom.graphics_3d.static
        VOcontours.show_graphics = True
        contours = fom.graphics.static.contours
        contours.show_graphics = True
        contours.contour_type = FigureOfMeritGraphics2DContourType.SMOOTH_FILL
        contours.color_method = FigureOfMeritGraphics2DColorMethod.COLOR_RAMP
        contours.level_attributes.remove_all()

        contours.level_attributes.add_level_range(590, 660, 10)  # Start, Start, Step
        contours.ramp_color.start_color = Colors.Red
        contours.ramp_color.end_color = Colors.Blue
