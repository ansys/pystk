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


class LOPSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LOPSnippets, self).__init__(*args, **kwargs)

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
        LOPSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.SATELLITE, LOPSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, LOPSnippets.m_DefaultName)
        LOPSnippets.m_Object = None

    # endregion

    # region ConfigureLOPPropagator
    def test_ConfigureLOPPropagator(self):
        self.ConfigureLOPPropagator(LOPSnippets.m_Object)

    def ConfigureLOPPropagator(self, satellite: "Satellite"):
        # Set satellite propagator to LOP
        satellite.set_propagator_type(PropagatorType.LOP)

        # Get PropagatorLOP interface
        lopProp: "PropagatorLOP" = clr.CastAs(satellite.propagator, PropagatorLOP)

        # Configure time period
        lopProp.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        lopProp.step = 86400

        # Configure propagator initial state
        orbit: "IOrbitState" = lopProp.initial_state.representation
        orbit.epoch = "1 Jan 2012 12:00:00.000"
        orbit.assign_cartesian(
            CoordinateSystem.FIXED, -1120.32, -9520.84, 0.129, 2.155, -1.54416, 5.668412
        )  # in km/sec

        # Configure force model
        lopForceModel: "VehicleLOPForceModel" = lopProp.force_model
        lopForceModel.central_body_gravity.maximum_degree = 15
        lopForceModel.central_body_gravity.maximum_order = 8
        lopForceModel.drag.use = True
        lopForceModel.drag.cd = 3.55
        lopForceModel.solar_radiation_pressure.use = True
        lopForceModel.solar_radiation_pressure.cp = 1.125
        lopForceModel.solar_radiation_pressure.atmosphere_height = 125
        lopForceModel.physical_data.drag_cross_sectional_area = 0.001555512
        lopForceModel.physical_data.solar_radiation_pressure_cross_sectional_area = 0.001810026
        lopForceModel.physical_data.satellite_mass = 1505.001

        # Propagate
        lopProp.propagate()

    # endregion
