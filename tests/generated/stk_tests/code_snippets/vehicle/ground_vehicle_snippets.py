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
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class GroundVehicleSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(GroundVehicleSnippets, self).__init__(*args, **kwargs)

    m_Object: "GroundVehicle" = None
    m_DefaultName: str = "MyGroundVehicle"

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
        GroundVehicleSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.GROUND_VEHICLE, GroundVehicleSnippets.m_DefaultName
            ),
            GroundVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.GROUND_VEHICLE, GroundVehicleSnippets.m_DefaultName
        )
        GroundVehicleSnippets.m_Object = None

    # endregion

    # region CreateGroundVehicleOnCurrentScenarioCentralBody
    def test_CreateGroundVehicleOnCurrentScenarioCentralBody(self):
        (IStkObject(GroundVehicleSnippets.m_Object)).unload()
        self.CreateGroundVehicleOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateGroundVehicleOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the ground vehicle
        launchVehicle: "GroundVehicle" = clr.CastAs(
            root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "MyGroundVehicle"), GroundVehicle
        )

    # endregion

    # region SetGroundVehicleToUseGreatArcPropagator
    def test_SetGroundVehicleToUseGreatArcPropagator(self):
        self.SetGroundVehicleToUseGreatArcPropagator(GroundVehicleSnippets.m_Object)

    def SetGroundVehicleToUseGreatArcPropagator(self, groundVehicle: "GroundVehicle"):
        # Set ground vehicle route to great arc
        groundVehicle.set_route_type(PropagatorType.GREAT_ARC)

        # Retrieve propagator interface if necessary
        propagator: "PropagatorGreatArc" = clr.CastAs(groundVehicle.route, PropagatorGreatArc)

    # endregion

    # region SetGroundVehicleToUseStkExternalPropagator
    def test_SetGroundVehicleToUseStkExternalPropagator(self):
        self.SetGroundVehicleToUseStkExternalPropagator(GroundVehicleSnippets.m_Object)

    def SetGroundVehicleToUseStkExternalPropagator(self, groundVehicle: "GroundVehicle"):
        # Set groundVehicle route to STK External propagator
        groundVehicle.set_route_type(PropagatorType.STK_EXTERNAL)

        # Retrieve propagator interface if necessary
        propagator: "PropagatorStkExternal" = clr.CastAs(groundVehicle.route, PropagatorStkExternal)

    # endregion

    # region SetGroundVehicleToUseRealtimePropagator
    def test_SetGroundVehicleToUseRealtimePropagator(self):
        self.SetGroundVehicleToUseRealtimePropagator(GroundVehicleSnippets.m_Object)

    def SetGroundVehicleToUseRealtimePropagator(self, groundVehicle: "GroundVehicle"):
        # Set ground vehicle route to STK External propagator
        groundVehicle.set_route_type(PropagatorType.REAL_TIME)

        # Retrieve propagator interface if necessary
        propagator: "PropagatorRealtime" = clr.CastAs(groundVehicle.route, PropagatorRealtime)

    # endregion

    # region GetExportStkEphemerisTool
    def test_GetExportStkEphemerisTool(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        self.GetExportStkEphemerisTool(gv)
        (IStkObject(gv)).unload()

    def GetExportStkEphemerisTool(self, groundVehicle: "GroundVehicle"):
        stkEphem: "VehicleEphemerisExportTool" = groundVehicle.export_tools.get_ephemeris_stk_export_tool()

    # endregion

    # region GetExportAttitudeTool
    def test_GetExportAttitudeTool(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        self.GetExportAttitudeTool(gv)
        (IStkObject(gv)).unload()

    def GetExportAttitudeTool(self, groundVehicle: "GroundVehicle"):
        attExTool: "VehicleAttitudeExportTool" = groundVehicle.export_tools.get_attitude_export_tool()

    # endregion

    # region GetExportPropDefTool
    def test_GetExportPropDefTool(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        self.GetExportPropDefTool(gv)
        (IStkObject(gv)).unload()

    def GetExportPropDefTool(self, groundVehicle: "GroundVehicle"):
        attExTool: "PropagatorDefinitionExportTool" = groundVehicle.export_tools.get_propagator_definition_export_tool()

    # endregion
