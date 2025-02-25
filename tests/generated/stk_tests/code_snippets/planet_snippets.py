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
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class PlanetSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(PlanetSnippets, self).__init__(*args, **kwargs)

    m_Object: "Planet" = None
    m_DefaultName: str = "MyPlanet"

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
        PlanetSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.PLANET, PlanetSnippets.m_DefaultName
            ),
            Planet,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.PLANET, PlanetSnippets.m_DefaultName)
        PlanetSnippets.m_Object = None

    # endregion

    # region SpecifyPlanetPositionUsingCommonTasks
    def test_SpecifyPlanetPositionUsingCommonTasks(self):
        self.SpecifyPlanetPositionUsingCommonTasks(
            PlanetSnippets.m_Object, TestBase.GetScenarioFile("CodeSnippetsTests", "Venus.pe")
        )

    def SpecifyPlanetPositionUsingCommonTasks(self, planet: "Planet", planetEphemeris: str):
        # Position source files traditionally have .pe extensions
        planet.common_tasks.set_position_source_file(planetEphemeris)

    # endregion

    # region ConfigurePlanet
    def test_ConfigurePlanet(self):
        self.ConfigurePlanet(PlanetSnippets.m_Object)
        body: "PlanetPositionCentralBody" = clr.CastAs(
            PlanetSnippets.m_Object.position_source_data, PlanetPositionCentralBody
        )

    def ConfigurePlanet(self, planet: "Planet"):
        planet.position_source = PlanetPositionSourceType.CENTRAL_BODY

        # Get PlanetPositionCentralBody interface
        body: "PlanetPositionCentralBody" = clr.CastAs(planet.position_source_data, PlanetPositionCentralBody)

        body.rename_automatically = False
        body.central_body = "Jupiter"
        if Array.IndexOf(body.available_ephemeris_source_types, int(EphemSourceType.ANALYTIC)) != -1:
            body.ephemeris_source = EphemSourceType.ANALYTIC

    # endregion

    # region ConfigurePlanetGraphics
    @category("Graphics Tests")
    def test_ConfigurePlanetGraphics(self):
        self.ConfigurePlanetGraphics(PlanetSnippets.m_Object.graphics)

    def ConfigurePlanetGraphics(self, graphics: "PlanetGraphics"):
        graphics.inherit = False

        graphics.color = Colors.Red
        graphics.marker_style = "Circle"
        graphics.line_style = LineStyle.M_DASH_DOT
        graphics.line_width = LineWidth.WIDTH4

        graphics.show_inertial_position = False
        graphics.show_sub_planet_point = False
        graphics.show_position_label = False
        graphics.show_sub_planet_label = False
        graphics.show_orbit = True
        graphics.orbit_display = PlanetOrbitDisplayType.ORBIT_DISPLAY_TIME
        displayTime: "PlanetOrbitDisplayTime" = clr.CastAs(graphics.orbit_display_data, PlanetOrbitDisplayTime)
        displayTime.time = 10000.0

    # endregion
