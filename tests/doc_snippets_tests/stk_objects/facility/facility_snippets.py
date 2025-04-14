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

from ansys.stk.core.stkobjects import AzElMaskType, STKObjectType
from ansys.stk.core.utilities.colors import Colors

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class FacilitySnippets(CodeSnippetsTestBase):
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

    def test_CreateFacilitySnippet(self):
        self.CreateFacilitySnippet(self.get_root())

    @code_snippet(
        name="CreateFacility",
        description="Create a facility (on the current scenario central body)",
        category="STK Objects | Facility",
        eid="stkobjects~Facility",
    )
    def CreateFacilitySnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        facility = root.current_scenario.children.new(STKObjectType.FACILITY, "MyFacility")

    def test_GetValidFacilitySnippet(self):
        try:
            self.GetValidFacilitySnippet(self.get_root())
        finally:
            facility = self.get_scenario().children.get_item_by_name("facility1")
            facility.unload()

    @code_snippet(
        name="GetValidFacility",
        description="Get a valid reference to a facility",
        category="STK Objects | Facility",
        eid="",
    )
    def GetValidFacilitySnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        from ansys.stk.core.utilities.exceptions import STKRuntimeError
        from ansys.stk.core.stkobjects import Facility, STKObjectType

        try:
            # this facility is not a valid STK reference
            my_facility_attempt = Facility()
            my_facility_attempt.height_above_ground = 123.4
        except STKRuntimeError as e:
            print(e)

        # this facility represents a valid STK object
        facility = Facility(root.current_scenario.children.new(STKObjectType.FACILITY, "facility1"))
        facility.height_above_ground = 123.4

    def test_SetHeightFacilitySnippet(self):
        try:
            self.SetHeightFacilitySnippet(self.get_root())
        finally:
            facility = self.get_scenario().children.get_item_by_name("facility1")
            facility.unload()

    @code_snippet(
        name="SetHeightFacility",
        description="Create a facility and set its height relative to ground level",
        category="STK Objects | Facility",
        eid="stkobjects~Facility",
    )
    def SetHeightFacilitySnippet(self, root):
        # StkObjectRoot root: STK Object Model Root
        from ansys.stk.core.stkobjects import Facility, STKObjectType

        facility = Facility(root.current_scenario.children.new(STKObjectType.FACILITY, "facility1"))
        facility.height_above_ground = 123.4

    def test_SetPositionFacilitySnippet(self):
        try:
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "facility")

            self.SetPositionFacilitySnippet(facility)
        finally:
            facility.unload()

    @code_snippet(
        name="SetPositionFacility",
        description="Set the geodetic position of a facility",
        category="STK Objects | Facility",
        eid="stkobjects~Facility",
    )
    def SetPositionFacilitySnippet(self, facility):
        # Facility facility: Facility Object
        facility.position.assign_geodetic(41.9849, 21.4039, 0)  # Latitude, Longitude, Altitude

        # Set altitude to height of terrain
        facility.use_terrain = True

        # Set altitude to a distance above the ground
        facility.height_above_ground = 0.05  # km

    def test_GetPositionFacilitySnippet(self):
        try:
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "facility")

            self.GetPositionFacilitySnippet(facility)
        finally:
            facility.unload()

    @code_snippet(
        name="GetPositionFacility",
        description="Get the cartesian position of a facility",
        category="STK Objects | Facility",
        eid="stkobjects~Facility",
    )
    def GetPositionFacilitySnippet(self, facility):
        # Facility facility: Facility Object
        (x, y, z) = facility.position.query_cartesian()

    def test_AzElMaskFacilitySnippet(self):
        try:
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "facility")

            self.AzElMaskFacilitySnippet(facility)
        finally:
            facility.unload()

    @code_snippet(
        name="AzElMaskFacility",
        description="Add an AzEl Mask to a Facility",
        category="STK Objects | Facility",
        eid="stkobjects~Facility",
    )
    def AzElMaskFacilitySnippet(self, facility):
        # Facility facility: Facility Object
        facility.set_az_el_mask(AzElMaskType.TERRAIN_DATA, 0)

    @category("Graphics Tests")
    def test_FacilityAzElMaskDisplaySnippet(self):
        try:
            facility = self.get_scenario().children.new(STKObjectType.FACILITY, "facility")

            self.FacilityAzElMaskDisplaySnippet(facility)
        finally:
            facility.unload()

    @code_snippet(
        name="FacilityAzElMaskDisplay",
        description="Display the AzEl Mask in 2D/3D",
        category="STK Objects | Facility | Graphics",
        eid="stkobjects~BasicAzElMask",
    )
    def FacilityAzElMaskDisplaySnippet(self, facility):
        # Facility facility: Facility Object
        azelMask = facility.graphics.az_el_mask
        azelMask.show_mask_over_range = True
        azelMask.number_of_range_steps = 10
        azelMask.display_range_minimum = 0  # km
        azelMask.display_range_maximum = 100  # km
        azelMask.show_color_at_range = True
        azelMask.range_color = Colors.Cyan
