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
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class VOSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(VOSnippets, self).__init__(*args, **kwargs)

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

    # region SetUp
    def setUp(self):
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region DelayGraphicsUpdates
    @category("VO Tests")
    def test_DelayGraphicsUpdates(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite1")
        self.DelayGraphicsUpdates(CodeSnippetsTestBase.m_Root)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "Satellite1")

    def DelayGraphicsUpdates(self, root: "StkObjectRoot"):
        satellite: "Satellite" = clr.CastAs(root.current_scenario.children["Satellite1"], Satellite)
        voElt: "Graphics3DDataDisplayElement" = satellite.graphics_3d.data_display[0]

        root.begin_update()  # Suspend updates

        # Put modifications here
        voElt.show_graphics = True
        voElt.use_background = True
        voElt.background_color = Colors.Green
        voElt.use_background = False

        root.end_update()  # Resume updates now

    # endregion
