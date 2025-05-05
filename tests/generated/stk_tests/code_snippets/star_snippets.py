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


class StarSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StarSnippets, self).__init__(*args, **kwargs)

    m_Object: "Star" = None
    m_DefaultName: str = "star1"

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
        StarSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.STAR, StarSnippets.m_DefaultName),
            Star,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.STAR, StarSnippets.m_DefaultName)
        StarSnippets.m_Object = None

    # endregion

    # region CreateStarOnCurrentScenarioCentralBody
    def test_CreateStarOnCurrentScenarioCentralBody(self):
        self.CreateStarOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateStarOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Star
        star: "Star" = clr.CastAs(root.current_scenario.children.new(STKObjectType.STAR, "MyStar"), Star)

    # endregion

    # region DefineStarBasicProperties
    def test_DefineStarBasicProperties(self):
        star: "Star" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children[StarSnippets.m_DefaultName], Star
        )
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("TimeUnit", "yr")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("AngleUnit", "arcSec")
        self.DefineStarBasicProperties(star)
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("TimeUnit", "min")
        CodeSnippetsTestBase.m_Root.units_preferences.set_current_unit("AngleUnit", "deg")

    def DefineStarBasicProperties(self, star: "Star"):
        # Units depend on current unit preferences
        star.location_declination = -40.0
        star.location_right_ascension = 120.0  # in arcSec
        star.magnitude = -1.0
        star.parallax = 0.0  # in arcSec
        star.proper_motion_declination = 1.5  # in arcSec
        star.proper_motion_radial_velocity = 0.75  # in meters
        star.proper_motion_right_ascension = -0.5  # in arcSec

    # endregion

    # region CreateStarFromStarDatabase
    def test_CreateStarFromStarDatabase(self):
        StarSnippets.CreateStarFromStarDatabase(CodeSnippetsTestBase.m_Root)

    @staticmethod
    def CreateStarFromStarDatabase(root: "StkObjectRoot"):
        # Import object from database using Connect
        command: str = "ImportFromDB * Star ScenarioCollection VisualMagnitude 0 1.0 RightAsc 200.0 230.0 Constellation ImportedFromStarDB"
        root.execute_command(command)

        star: "Star" = clr.CastAs(root.get_object_from_path("Star/Star-65474"), Star)

    # endregion
