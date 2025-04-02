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
from code_snippets_test_base import CodeSnippetsTestBase


class ConnectSnippets(CodeSnippetsTestBase):
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

    def test_GetSetRGBColorSnippet(self):
        self.GetSetRGBColorSnippet(self.get_root())

    @code_snippet(
        name="GetSetRGBColor",
        description="Get and set a three-channel color for the graphics of an STK object",
        category="Colors",
        eid="AgColors~Color | AgColors~Colors",
    )
    def GetSetRGBColorSnippet(self, root):
        from ansys.stk.core.stkobjects import STKObjectType
        from ansys.stk.core.utilities.colors import Color, Colors

        facility = root.current_scenario.children.new(STKObjectType.FACILITY, "facility1")

        facility.graphics.color = Colors.Blue
        facility.graphics.color = Color.from_rgb(127, 255, 212)
        (r, g, b) = facility.graphics.color.get_rgb()

    def test_GetSetRGBAColorSnippet(self):
        self.GetSetRGBAColorSnippet(self.get_root())

    @code_snippet(
        name="GetSetRGBAColor",
        description="Get and set a four-channel color for the graphics of an STK object",
        category="Colors",
        eid="AgColors~Color | AgColors~ColorRGBA | AgColors~Colors",
    )
    def GetSetRGBAColorSnippet(self, root):
        from ansys.stk.core.utilities.colors import Colors, ColorRGBA

        manager = root.current_scenario.scene_manager
        point = manager.initializers.point_batch_primitive.initialize()
        
        lla_pts = [ 39.88, -75.25, 0,
                    38.85, -77.04, 0,
                    37.37, -121.92, 0 ]

        colors = [ Colors.Red,
                ColorRGBA(Colors.Blue, 127),
                Colors.from_rgba(0, 255, 0, 127) ]

        point.set_cartographic_with_colors('Earth', lla_pts, colors)

