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

from ansys.stk.core.stkobjects import STKObjectType
from ansys.stk.core.utilities.colors import Colors

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class MTOSnippets(CodeSnippetsTestBase):
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

    @category("Graphics Tests")
    def test_CreateMTOSnippet(self):
        self.CreateMTOSnippet(self.get_root(), self.get_scenario())

    @code_snippet(
        name="CreateMTO",
        description="Create a New MTO (on the current scenario central body)",
        category="STK Objects | MTO",
        eid="stkobjects~MTO",
    )
    def CreateMTOSnippet(self, root, scenario):
        # Scenario scenario: Scenario object
        mto = scenario.children.new(STKObjectType.MTO, "MyMTO")

        root.units_preferences.set_current_unit("DateFormat", "EpSec")

        mtoTimes = [[0], [7200]]
        mtoLats = [[36.77], [34.80]]
        mtoLons = [[-77.25], [-78.37]]
        mtoAlts = [[5], [5]]

        track1 = mto.tracks.add_track(1, mtoTimes, mtoLats, mtoLons, mtoAlts)
        track1.interpolate = True
        # Change the color of the track
        mto.graphics.tracks.get_track_from_identifier(1).color = Colors.Red

    def test_MTOLoadTrackSnippet(self):
        try:
            mto = self.get_scenario().children.new(STKObjectType.MTO, "mto")

            self.MTOLoadTrackSnippet(mto)
        finally:
            mto.unload()

    @code_snippet(
        name="MTOLoadTrack",
        description="Load multi-track object (MTO) track points from a file",
        category="STK Objects | MTO",
        eid="stkobjects~MTO",
    )
    def MTOLoadTrackSnippet(self, mto):
        # load_points expects the path an Ephemeris file path
        # MTO mto: MTO Object
        track2 = mto.tracks.add(2)
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        track2.points.load_points(
            os.path.join(installPath, "Data", "Resources", "stktraining", "text", "EphemerisLLATimePosVel_Example.e")
        )
        track2.interpolate = True
