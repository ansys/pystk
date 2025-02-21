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
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class ShipSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ShipSnippets, self).__init__(*args, **kwargs)

    m_Object: "Ship" = None
    m_DefaultName: str = "MyShip"

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
        ShipSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SHIP, ShipSnippets.m_DefaultName),
            Ship,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SHIP, ShipSnippets.m_DefaultName)
        ShipSnippets.m_Object = None

    # endregion

    # region CreateShipOnCurrentScenarioCentralBody
    def test_CreateShipOnCurrentScenarioCentralBody(self):
        (IStkObject(ShipSnippets.m_Object)).unload()
        self.CreateShipOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateShipOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Ship
        ship: "Ship" = clr.CastAs(root.current_scenario.children.new(STKObjectType.SHIP, "MyShip"), Ship)

    # endregion

    # region SetShipToUseGreatArcPropagator
    def test_SetShipToUseGreatArcPropagator(self):
        self.SetShipToUseGreatArcPropagator(ShipSnippets.m_Object)

    def SetShipToUseGreatArcPropagator(self, ship: "Ship"):
        # Set ship route to great arc
        ship.set_route_type(PropagatorType.GREAT_ARC)

        # Retrieve propagator interface if necessary
        propagator: "PropagatorGreatArc" = clr.CastAs(ship.route, PropagatorGreatArc)

    # endregion

    # region SetShipToUseStkExternalPropagator
    def test_SetShipToUseStkExternalPropagator(self):
        self.SetShipToUseStkExternalPropagator(ShipSnippets.m_Object)

    def SetShipToUseStkExternalPropagator(self, ship: "Ship"):
        # Set ship route to STK External propagator
        ship.set_route_type(PropagatorType.STK_EXTERNAL)

        # Retrieve propagator interface if necessary
        propagator: "PropagatorStkExternal" = clr.CastAs(ship.route, PropagatorStkExternal)

    # endregion

    # region SetShipToUseRealtimePropagator
    def test_SetShipToUseRealtimePropagator(self):
        self.SetShipToUseRealtimePropagator(ShipSnippets.m_Object)

    def SetShipToUseRealtimePropagator(self, ship: "Ship"):
        # Set ship route to STK External propagator
        ship.set_route_type(PropagatorType.REAL_TIME)

        # Retrieve propagator interface if necessary
        propagator: "PropagatorRealtime" = clr.CastAs(ship.route, PropagatorRealtime)

    # endregion
