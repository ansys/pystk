# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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


class SGP4Snippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SGP4Snippets, self).__init__(*args, **kwargs)

    m_Object: "Satellite" = None
    m_DefaultName: str = "MySatellite"

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
        SGP4Snippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.SATELLITE, SGP4Snippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, SGP4Snippets.m_DefaultName
        )
        SGP4Snippets.m_Object = None

    # endregion

    # region ConfigureSGP4WithFileSource
    def test_ConfigureSGP4WithFileSource(self):
        SGP4Snippets.m_Object.set_propagator_type(PropagatorType.SGP4)

        sgp4: "PropagatorSGP4" = clr.CastAs(SGP4Snippets.m_Object.propagator, PropagatorSGP4)
        self.ConfigureSGP4WithFileSource(
            sgp4, TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

    def ConfigureSGP4WithFileSource(self, propagator: "PropagatorSGP4", tleFilePath: str):
        # Configure propagator's TLE file path
        propagator.common_tasks.add_segments_from_file("2215", tleFilePath)

        # Propagate
        propagator.propagate()

    def ConfigureSGP4WithOnlineSource(self, propagator: "PropagatorSGP4"):
        # Configure time period
        propagator.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        propagator.step = 60.0

        # Add segments
        propagator.common_tasks.add_segments_from_online_source("25544")

        # Propagate
        propagator.propagate()

    # endregion

    # region SetSGP4ToAutoUpdateFromFileSource
    def test_SetSGP4ToAutoUpdateFromFileSource(self):
        # Set propagator
        SGP4Snippets.m_Object.set_propagator_type(PropagatorType.SGP4)
        sgp4: "PropagatorSGP4" = clr.CastAs(SGP4Snippets.m_Object.propagator, PropagatorSGP4)

        sgp4.common_tasks.add_segments_from_file(
            "2215", TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

        self.SetSGP4ToAutoUpdateFromFileSource(sgp4, TestBase.GetScenarioFile("CodeSnippetsTests", "stkAllTLE.tle"))

    def SetSGP4ToAutoUpdateFromFileSource(self, propagator: "PropagatorSGP4", fileUpdateSource: str):
        propagator.automatic_update_enabled = True
        propagator.automatic_update_settings.selected_source = VehicleSGP4AutomaticUpdateSourceType.FILE
        propagator.automatic_update_settings.file_source.filename = fileUpdateSource

        # Preview TLEs (optional)
        # Preview() returns a one dimension string of tles
        tles = propagator.automatic_update_settings.file_source.preview()

        rx = Regex(r"^(?<ssc>[-]?\d+) (?<orbitepoch>[-]?\d+[.]?\d+) (?<revnumber>[-]?\d+)$")
        line: typing.Any
        for line in tles:
            m = rx.Match(str(line))
            Console.WriteLine(
                "SCC: {0}, orbit epoch: {1}, rev number: {2}",
                m.Groups["ssc"],
                m.Groups["orbitepoch"],
                m.Groups["revnumber"],
            )

        # Propagate
        propagator.propagate()

    # endregion

    # region SetSGP4ToAutoUpdateFromOnlineSource
    def test_SetSGP4ToAutoUpdateFromOnlineSource(self):
        # Set propagator
        SGP4Snippets.m_Object.set_propagator_type(PropagatorType.SGP4)
        sgp4: "PropagatorSGP4" = clr.CastAs(SGP4Snippets.m_Object.propagator, PropagatorSGP4)

        sgp4.common_tasks.add_segments_from_file(
            "2215", TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

        self.SetSGP4ToAutoUpdateFromOnlineSource(sgp4)

    def SetSGP4ToAutoUpdateFromOnlineSource(self, propagator: "PropagatorSGP4"):
        propagator.automatic_update_enabled = True
        propagator.automatic_update_settings.selected_source = VehicleSGP4AutomaticUpdateSourceType.ONLINE

        # Preview TLEs (optional)
        # Preview() returns a one dimension string of tles
        tles = propagator.automatic_update_settings.file_source.preview()

        rx = Regex(r"^(?<ssc>[-]?\d+) (?<orbitepoch>[-]?\d+[.]?\d+) (?<revnumber>[-]?\d+)$")
        line: typing.Any
        for line in tles:
            m = rx.Match(str(line))
            Console.WriteLine(
                "SCC: {0}, orbit epoch: {1}, rev number: {2}",
                m.Groups["ssc"],
                m.Groups["orbitepoch"],
                m.Groups["revnumber"],
            )

        # Propagate
        propagator.propagate()

    # endregion
