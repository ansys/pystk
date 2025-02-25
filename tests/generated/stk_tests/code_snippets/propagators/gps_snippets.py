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
from ansys.stk.core.stkutil import *


class GPSSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(GPSSnippets, self).__init__(*args, **kwargs)

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
        GPSSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.SATELLITE, GPSSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, GPSSnippets.m_DefaultName)
        GPSSnippets.m_Object = None

    # endregion

    # region ConfigureGPSWithAlmanac
    def test_ConfigureGPSWithAlmanac(self):
        GPSSnippets.m_Object.set_propagator_type(PropagatorType.GPS)

        propagator: "PropagatorGPS" = clr.CastAs(GPSSnippets.m_Object.propagator, PropagatorGPS)

        self.ConfigureGPSWithAlmanac(
            propagator,
            TestBase.GetScenarioFile("CodeSnippetsTests", "GPSAlmanac.alm"),
            (IStkObject(GPSSnippets.m_Object)).root.current_scenario,
        )

    def ConfigureGPSWithAlmanac(self, propagator: "PropagatorGPS", almanacPath: str, scenario: "IStkObject"):
        # Configure properties
        # Use the scenario's analysis interval
        propagator.ephemeris_interval.set_implicit_interval(
            scenario.analysis_workbench_components.time_intervals["AnalysisInterval"]
        )

        # PRN must be set before configuring GPS almanac
        propagator.prn = int(str(propagator.available_prns[0]))

        # Turn the Auto-update off
        propagator.automatic_update_enabled = False

        # Specify a catalog
        propagator.specify_catalog.filename = almanacPath
        if propagator.specify_catalog.properties.type == VehicleGPSAlmanacType.SEM:
            # configure the SEM almanac
            sem: "VehicleGPSAlmanacPropertiesSEM" = clr.CastAs(
                propagator.specify_catalog.properties, VehicleGPSAlmanacPropertiesSEM
            )
            sem.reference_week = GPSReferenceWeek.WEEK22_AUG1999
        elif propagator.specify_catalog.properties.type == VehicleGPSAlmanacType.SP3:
            # SP3 almanac contains no configurable properties
            sp3: "VehicleGPSAlmanacPropertiesSP3" = clr.CastAs(
                propagator.specify_catalog.properties, VehicleGPSAlmanacPropertiesSP3
            )
        elif propagator.specify_catalog.properties.type == VehicleGPSAlmanacType.YUMA:
            # configure the YUMA almanac
            yuma: "VehicleGPSAlmanacPropertiesYUMA" = clr.CastAs(
                propagator.specify_catalog.properties, VehicleGPSAlmanacPropertiesYUMA
            )
            yuma.reference_week = GPSReferenceWeek.WEEK22_AUG1999

        # Propagate
        propagator.propagate()

    # endregion
