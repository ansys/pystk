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

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class TargetSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object: "Target" = None
        super(TargetSnippets, self).__init__(*args, **kwargs)

    m_DefaultName: str = "MyTarget"

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
                STKObjectType.TARGET, TargetSnippets.m_DefaultName
            ),
            Target,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.TARGET, TargetSnippets.m_DefaultName)
        self.m_Object = None

    # endregion

    # region CreateTargetOnCurrentScenarioCentralBody
    def test_CreateTargetOnCurrentScenarioCentralBody(self):
        self.CreateTargetOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateTargetOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Target on the current scenario central body (use
        # NewOnCentralBody to specify explicitly the central body)
        areaTarget: "Target" = clr.CastAs(
            root.current_scenario.children.new(STKObjectType.AREA_TARGET, "MyAreaTarget"), Target
        )

    # endregion

    # region ChangeTargetPosition
    def test_ChangeTargetPosition(self):
        self.ChangeTargetPosition(self.m_Object)

    def ChangeTargetPosition(self, target: "Target"):
        pos: "IPosition" = target.position
        pos.assign_geodetic(39.95, 15.58, 231.54)

    # endregion

    # region ConfigureTargetAzElMask
    def test_ConfigureTargetAzElMask(self):
        self.ConfigureTargetAzElMask(self.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "maskfile.aem"))

    def ConfigureTargetAzElMask(self, target: "Target", maskfile: str):
        target.use_local_time_offset = True
        target.local_time_offset = 200.0
        target.use_terrain = True
        # Note, if SetAzElMask is set to a type other than AzElMaskType.MASK_FILE,
        # the second parameter is ignored.
        target.set_az_el_mask(AzElMaskType.MASK_FILE, maskfile)
        target.terrain_normal = TerrainNormalType.SLOPE_AZIMUTH
        target.altitude_reference = AltitudeReferenceType.MEAN_SEA_LEVEL
        target.height_above_ground = 1472.0

    # endregion
