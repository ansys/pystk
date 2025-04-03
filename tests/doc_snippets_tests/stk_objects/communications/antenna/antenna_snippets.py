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

from ansys.stk.core.stkobjects import AntennaContourType, SensorRefractionType, STKObjectType
from ansys.stk.core.stkutil import AzElAboutBoresight

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class AntennaSnippets(CodeSnippetsTestBase):
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

    def test_CreateAntennaSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.CreateAntennaSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="CreateAntenna",
        description="Create a New Antenna Object",
        category="STK Objects | Communications | Antenna",
        eid="stkobjects~Antenna",
    )
    def CreateAntennaSnippet(self, satellite):
        # IStkObject satellite: STK object
        antenna = satellite.children.new(STKObjectType.ANTENNA, "MyAntenna")

    def test_ModifyAntennaSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            antenna = parent.children.new(STKObjectType.ANTENNA, "antenna")

            self.ModifyAntennaSnippet(antenna)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyAntenna",
        description="Modify Antenna Model Type",
        category="STK Objects | Communications | Antenna",
        eid="stkobjects~Antenna",
    )
    def ModifyAntennaSnippet(self, antenna):
        # Antenna antenna: Antenna object
        antenna.set_model("Dipole")
        antennaModel = antenna.model
        antennaModel.design_frequency = 15  # GHz
        antennaModel.length = 1.5  # m
        antennaModel.length_to_wavelength_ratio = 45
        antennaModel.efficiency = 85  # Percent

    def test_ModifyAntennaRefractionSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            antenna = parent.children.new(STKObjectType.ANTENNA, "antenna")

            self.ModifyAntennaRefractionSnippet(antenna)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyAntennaRefraction",
        description="Modify Antenna Refraction",
        category="STK Objects | Communications | Antenna",
        eid="stkobjects~Antenna",
    )
    def ModifyAntennaRefractionSnippet(self, antenna):
        # Antenna antenna: Antenna object
        antenna.use_refraction_in_access = True
        antenna.refraction = SensorRefractionType.ITU_R_P834_4
        refraction = antenna.refraction_model
        refraction.ceiling = 5000  # m
        refraction.atmosphere_altitude = 10000  # m
        refraction.knee_bend_factor = 0.2

    def test_ModifyAntennaOrientationSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            antenna = parent.children.new(STKObjectType.ANTENNA, "antenna")

            self.ModifyAntennaOrientationSnippet(antenna)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyAntennaOrientation",
        description="Modify Antenna Orientation and Position",
        category="STK Objects | Communications | Antenna",
        eid="stkobjects~Antenna",
    )
    def ModifyAntennaOrientationSnippet(self, antenna):
        # Antenna antenna: Antenna object
        antOrientation = antenna.orientation
        antOrientation.assign_az_el(0, -90, AzElAboutBoresight.ROTATE)
        antOrientation.position_offset.x = 0.0  # m
        antOrientation.position_offset.y = 1  # m
        antOrientation.position_offset.z = 0.25  # m

    @category("Graphics Tests")
    def test_ModifyAntennaGraphicsSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            antenna = parent.children.new(STKObjectType.ANTENNA, "antenna")

            self.ModifyAntennaGraphicsSnippet(antenna)
        finally:
            parent.unload()

    @code_snippet(
        name="ModifyAntennaGraphics",
        description="Modify Antenna Graphics",
        category="STK Objects | Communications | Antenna",
        eid="stkobjects~Antenna",
    )
    def ModifyAntennaGraphicsSnippet(self, antenna):
        # Antenna antenna: Antenna object
        contours = antenna.graphics.contour_graphics
        contours.set_contour_type(AntennaContourType.GAIN)
        contours.show = True
        for i in range(-30, 30, 5):
            contours.contour.levels.add(i)
        antenna.graphics_3d.show_contours = True
        antenna.graphics_3d.volume_graphics.show = True
