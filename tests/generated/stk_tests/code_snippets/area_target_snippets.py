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

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class AreaTargetSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object: "AreaTarget" = None
        super(AreaTargetSnippets, self).__init__(*args, **kwargs)

    m_DefaultName: str = "MyAreaTarget"

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
        self.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.AREA_TARGET, AreaTargetSnippets.m_DefaultName
            ),
            AreaTarget,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.AREA_TARGET, AreaTargetSnippets.m_DefaultName
        )
        self.m_Object = None

    # endregion

    # region CreateAreaTargetOnCurrentScenarioCentralBody
    def test_CreateAreaTargetOnCurrentScenarioCentralBody(self):
        (IStkObject(self.m_Object)).unload()
        self.CreateAreaTargetOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)
        self.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children[AreaTargetSnippets.m_DefaultName], AreaTarget
        )

    def CreateAreaTargetOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the AreaTarget on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        areaTarget: "AreaTarget" = clr.CastAs(
            root.current_scenario.children.new(STKObjectType.AREA_TARGET, "MyAreaTarget"), AreaTarget
        )

    # endregion

    # region SetAreaTargetBoundaryAndPosition
    def test_SetAreaTargetBoundaryAndPosition(self):
        self.SetAreaTargetBoundaryAndPosition(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetAreaTargetBoundaryAndPosition(self, root: "StkObjectRoot", areaTarget: "AreaTarget"):
        # By using the fine grained interfaces,
        # BeginUpdate/EndUpdate prevent intermediate redraws
        root.begin_update()
        areaTarget.area_type = AreaType.PATTERN
        patterns: "AreaTypePatternCollection" = clr.CastAs(areaTarget.area_type_data, AreaTypePatternCollection)
        patterns.add(40.04, -76.304)
        patterns.add(40.337, -75.922)
        patterns.add(40.028, -75.628)
        root.end_update()

    # endregion

    # region SetAreaTargetBoundaryAndPositionCommonTask
    def test_SetAreaTargetBoundaryAndPositionCommonTask(self):
        self.SetAreaTargetBoundaryAndPositionCommonTask(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetAreaTargetBoundaryAndPositionCommonTask(self, root: "StkObjectRoot", areaTarget: "AreaTarget"):
        # By using the CommonTasks interface,
        # make an array of lattitude and longitude boundary points
        boundary = [[40.04, -76.304], [40.337, -75.922], [40.028, -75.628]]

        # SetAreaTypePattern expects a two dimensional array of latitude and longitude values
        areaTarget.common_tasks.set_area_type_pattern(boundary)

    # endregion

    # region SetEllipticalAreaTarget
    def test_SetEllipticalAreaTarget(self):
        self.SetEllipticalAreaTarget(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetEllipticalAreaTarget(self, root: "StkObjectRoot", areaTarget: "AreaTarget"):
        # By using the fine grained interfaces,
        # BeginUpdate/EndUpdate prevent intermediate redraws
        root.begin_update()
        areaTarget.area_type = AreaType.ELLIPSE
        ellipse: "AreaTypeEllipse" = clr.CastAs(areaTarget.area_type_data, AreaTypeEllipse)
        ellipse.semi_major_axis = 85.25  # in km (distance dimension)
        ellipse.semi_minor_axis = 80.75  # in km (distance dimension)
        ellipse.bearing = 44  # in deg (angle dimension)
        root.end_update()

    # endregion

    # region SetEllipticalAreaTargetCommonTask
    def test_SetEllipticalAreaTargetCommonTask(self):
        self.SetEllipticalAreaTargetCommonTask(CodeSnippetsTestBase.m_Root, self.m_Object)

    def SetEllipticalAreaTargetCommonTask(self, root: "StkObjectRoot", areaTarget: "AreaTarget"):
        # By using the CommonTasks interface
        areaTarget.common_tasks.set_area_type_ellipse(85.25, 80.75, 44)

    # endregion

    # region ListAllPointsInAnAreaTarget
    def test_ListAllPointsInAnAreaTarget(self):
        self.SetAreaTargetBoundaryAndPosition(CodeSnippetsTestBase.m_Root, self.m_Object)
        self.ListAllPointsInAnAreaTarget(self.m_Object)

    def ListAllPointsInAnAreaTarget(self, areaTarget: "AreaTarget"):
        if areaTarget.area_type == AreaType.PATTERN:
            # Get AreaTypePatternCollection interface from AreaTypeData
            patternPoints: "AreaTypePatternCollection" = clr.CastAs(
                areaTarget.area_type_data, AreaTypePatternCollection
            )

            # ToArray returns a two dimensional array of latitude and longitude points
            areaTargetPoints = patternPoints.to_array()

            Console.WriteLine("All points in Area Target")

            i: int = 0
            while i < len(areaTargetPoints):
                Console.WriteLine(
                    "  Latitude {0} Longitude: {1}",
                    Convert.ToDouble(areaTargetPoints[i][0]),
                    Convert.ToDouble(areaTargetPoints[i][1]),
                )

                i += 1

    # endregion
