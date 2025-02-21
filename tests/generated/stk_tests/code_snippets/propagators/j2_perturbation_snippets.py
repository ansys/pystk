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
from ansys.stk.core.stkutil import *


class J2PerturbationSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(J2PerturbationSnippets, self).__init__(*args, **kwargs)

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
        J2PerturbationSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.SATELLITE, J2PerturbationSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, J2PerturbationSnippets.m_DefaultName
        )
        J2PerturbationSnippets.m_Object = None

    # endregion

    # region ConfigureSatelliteWithJ2PerturbationPropagator
    def test_ConfigureSatelliteWithJ2PerturbationPropagator(self):
        self.ConfigureSatelliteWithJ2PerturbationPropagator(J2PerturbationSnippets.m_Object)

    def ConfigureSatelliteWithJ2PerturbationPropagator(self, satellite: "Satellite"):
        # Set propagator to SGP4
        satellite.set_propagator_type(PropagatorType.J2_PERTURBATION)

        # J2 Perturbation propagator
        j2prop: "PropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, PropagatorJ2Perturbation)

        # Configure time period
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60.0

        # Configure propagator initial state
        initial: "VehicleZonalPropagatorInitialState" = j2prop.initial_state
        initial.representation.epoch = "1 Jan 2012 12:00:00.000"
        initial.representation.assign_cartesian(
            CoordinateSystem.FIXED, -1514.4, -6790.1, -1.25, 4.8151, 1.771, 5.6414
        )  # in km/sec
        initial.ellipse_options = VehicleEllipseOptionType.SECULARLY_PRECESSING

        # Propagate
        j2prop.propagate()

    # endregion
