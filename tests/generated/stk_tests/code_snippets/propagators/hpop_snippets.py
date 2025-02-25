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


class HPOPSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(HPOPSnippets, self).__init__(*args, **kwargs)

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
        HPOPSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.SATELLITE, HPOPSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, HPOPSnippets.m_DefaultName
        )
        HPOPSnippets.m_Object = None

    # endregion

    # region ConfigureSatelliteWithHPOPPropagator
    def test_ConfigureSatelliteWithHPOPPropagator(self):
        self.ConfigureSatelliteWithHPOPPropagator(HPOPSnippets.m_Object)

    def ConfigureSatelliteWithHPOPPropagator(self, satellite: "Satellite"):
        # Set satellite propagator to HPOP
        satellite.set_propagator_type(PropagatorType.HPOP)

        # Get PropagatorLOP interface
        hpopProp: "PropagatorHPOP" = clr.CastAs(satellite.propagator, PropagatorHPOP)

        # Configure force model
        hpopForceModel: "VehicleHPOPForceModel" = hpopProp.force_model
        hpopForceModel.central_body_gravity.file = r"STKData\CentralBodies\Earth\GGM02C.grv"
        hpopForceModel.central_body_gravity.maximum_degree = 45
        hpopForceModel.central_body_gravity.maximum_order = 10
        hpopForceModel.central_body_gravity.use_ocean_tides = True

        hpopForceModel.drag.use = True
        hpopDragModel: "VehicleHPOPDragModelSpherical" = clr.CastAs(
            hpopForceModel.drag.drag_model, VehicleHPOPDragModelSpherical
        )
        hpopDragModel.cd = 1.89
        hpopDragModel.area_mass_ratio = 0.05
        hpopForceModel.drag.atmospheric_density_model = AtmosphericDensityModel.MSIS90

        hpopForceModel.third_body_gravity.remove_third_body("Moon")

        # Propagate
        hpopProp.propagate()

    # endregion
