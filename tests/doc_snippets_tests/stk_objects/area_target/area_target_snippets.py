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

from ansys.stk.core.stkobjects import AreaType, STKObjectType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase


class AreaTargetSnippets(CodeSnippetsTestBase):
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

    def test_CreateAreaTargetSnippet(self):
        self.CreateAreaTargetSnippet(self.get_root())

    @code_snippet(
        name="CreateAreaTarget",
        description="Create an area target (on the current scenario central body)",
        category="STK Objects | Area Target",
        eid="stkobjects~AreaTarget",
    )
    def CreateAreaTargetSnippet(self, root):
        # StkObjectRoot root: STK Object Model Root

        # Create the AreaTarget on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        areaTarget = root.current_scenario.children.new(STKObjectType.AREA_TARGET, "MyAreaTarget")

    def test_CreateEllipticalAreaTargetSnippet(self):
        try:
            areaTarget = self.get_scenario().children.new(STKObjectType.AREA_TARGET, "areaTarget")

            self.CreateEllipticalAreaTargetSnippet(self.get_root(), areaTarget)
        finally:
            areaTarget.unload()

    @code_snippet(
        name="CreateEllipticalAreaTarget",
        description="Set an elliptical area target",
        category="STK Objects | Area Target",
        eid="stkobjects~AreaTarget",
    )
    def CreateEllipticalAreaTargetSnippet(self, root, areaTarget):
        # StkObjectRoot root: STK Object Model Root
        # AreaTarget areaTarget: AreaTarget object

        # By using the fine grained interfaces,
        # BeginUpdate/EndUpdate prevent intermediate redraws
        root.begin_update()
        areaTarget.area_type = AreaType.ELLIPSE
        ellipse = areaTarget.area_type_data
        ellipse.semi_major_axis = 85.25  # in km (distance dimension)
        ellipse.semi_minor_axis = 80.75  # in km (distance dimension)
        ellipse.bearing = 44  # in deg (angle dimension)
        root.end_update()

    def test_CreateAreaTargetCommonSnippet(self):
        try:
            areaTarget = self.get_scenario().children.new(STKObjectType.AREA_TARGET, "areaTarget")

            self.CreateAreaTargetCommonSnippet(areaTarget)
        finally:
            areaTarget.unload()

    @code_snippet(
        name="CreateAreaTargetCommon",
        description="Set an elliptical area target (using common tasks)",
        category="STK Objects | Area Target",
        eid="stkobjects~AreaTarget",
    )
    def CreateAreaTargetCommonSnippet(self, areaTarget):
        # StkObjectRoot root: STK Object Model Root
        # AreaTarget areaTarget: AreaTarget object

        # By using the CommonTasks interface
        areaTarget.common_tasks.set_area_type_ellipse(85.25, 80.75, 44)

    def test_CreateBoundaryAreaTargetSnippet(self):
        try:
            areaTarget = self.get_scenario().children.new(STKObjectType.AREA_TARGET, "areaTarget")

            self.CreateBoundaryAreaTargetSnippet(self.get_root(), areaTarget)
        finally:
            areaTarget.unload()

    @code_snippet(
        name="CreateBoundaryAreaTarget",
        description="Define an area target boundary and position from a list of lat/lon/alt",
        category="STK Objects | Area Target",
        eid="stkobjects~AreaTarget | stkobjects~AreaTypePatternCollection",
    )
    def CreateBoundaryAreaTargetSnippet(self, root, areaTarget):
        # StkObjectRoot root: STK Object Model Root
        # AreaTarget areaTarget: AreaTarget object

        # By using the fine grained interfaces,
        # BeginUpdate/EndUpdate prevent intermediate redraws
        root.begin_update()
        areaTarget.area_type = AreaType.PATTERN
        patterns = areaTarget.area_type_data
        patterns.add(48.897, 18.637)
        patterns.add(46.534, 13.919)
        patterns.add(44.173, 21.476)
        root.end_update()
        areaTarget.automatic_computation_of_centroid = True

    def test_CreateBoundaryAreaTargetListSnippet(self):
        try:
            areaTarget = self.get_scenario().children.new(STKObjectType.AREA_TARGET, "areaTarget")

            self.CreateBoundaryAreaTargetListSnippet(areaTarget)
        finally:
            areaTarget.unload()

    @code_snippet(
        name="CreateBoundaryAreaTargetList",
        description="Define an area target boundary and position from a list of lat/lon/alt (using common tasks)",
        category="STK Objects | Area Target",
        eid="stkobjects~AreaTarget",
    )
    def CreateBoundaryAreaTargetListSnippet(self, areaTarget):
        # AreaTarget areaTarget: AreaTarget object
        # Remove all points in the area target
        areaTarget.area_type_data.remove_all()

        # By using the CommonTasks interface,
        # make an array of latitude and longitude boundary points
        boundary = [[29, -12], [29, 34], [6, 34], [6, -12]]

        # SetAreaTypePattern expects a two dimensional array of latitude and longitude values
        areaTarget.common_tasks.set_area_type_pattern(boundary)

    def test_ListAreaTargetPointsSnippet(self):
        try:
            areaTarget = self.get_scenario().children.new(STKObjectType.AREA_TARGET, "areaTarget")

            self.ListAreaTargetPointsSnippet(areaTarget)
        finally:
            areaTarget.unload()

    @code_snippet(
        name="ListAreaTargetPoints",
        description="List all points in an area target",
        category="STK Objects | Area Target",
        eid="stkobjects~AreaTarget",
    )
    def ListAreaTargetPointsSnippet(self, areaTarget):
        # AreaTarget areaTarget: AreaTarget object
        if areaTarget.area_type == AreaType.PATTERN:
            # Get IAgAreaTypePatternCollection interface from AreaTypeData
            patternPoints = areaTarget.area_type_data

            # ToArray returns a two dimensional array of latitude and longitude points
            areaTargetPoints = patternPoints.to_array()

            print("All points in Area Target")
            for i in range(0, len(areaTargetPoints)):
                print("Latitude: %s Longitude: %s" % (str(areaTargetPoints[i][0]), str(areaTargetPoints[i][1])))
