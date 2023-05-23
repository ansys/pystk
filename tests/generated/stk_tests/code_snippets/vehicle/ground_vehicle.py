import sys
import os

sys.path.insert(1, os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class GroundVehicle(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(GroundVehicle, self).__init__(*args, **kwargs)

    m_Object = None
    m_DefaultName = "MyGroundVehicle"

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
        GroundVehicle.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eGroundVehicle, GroundVehicle.m_DefaultName
            ),
            IGroundVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eGroundVehicle, GroundVehicle.m_DefaultName
        )
        GroundVehicle.m_Object = None

    # endregion

    # region CreateGroundVehicleOnCurrentScenarioCentralBody
    def test_CreateGroundVehicleOnCurrentScenarioCentralBody(self):
        (clr.Convert(GroundVehicle.m_Object, IStkObject)).Unload()
        self.CreateGroundVehicleOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateGroundVehicleOnCurrentScenarioCentralBody(self, root):
        # Create the ground vehicle
        launchVehicle = clr.CastAs(
            root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "MyGroundVehicle"), IGroundVehicle
        )

    # endregion

    # region SetGroundVehicleToUseGreatArcPropagator
    def test_SetGroundVehicleToUseGreatArcPropagator(self):
        self.SetGroundVehicleToUseGreatArcPropagator(GroundVehicle.m_Object)

    def SetGroundVehicleToUseGreatArcPropagator(self, groundVehicle):
        # Set ground vehicle route to great arc
        groundVehicle.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Retrieve propagator interface if necessary
        propagator = clr.CastAs(groundVehicle.Route, IVehiclePropagatorGreatArc)

    # endregion

    # region SetGroundVehicleToUseStkExternalPropagator
    def test_SetGroundVehicleToUseStkExternalPropagator(self):
        self.SetGroundVehicleToUseStkExternalPropagator(GroundVehicle.m_Object)

    def SetGroundVehicleToUseStkExternalPropagator(self, groundVehicle):
        # Set groundVehicle route to STK External propagator
        groundVehicle.SetRouteType(AgEVePropagatorType.ePropagatorStkExternal)

        # Retrieve propagator interface if necessary
        propagator = clr.CastAs(groundVehicle.Route, IVehiclePropagatorStkExternal)

    # endregion

    # region SetGroundVehicleToUseRealtimePropagator
    def test_SetGroundVehicleToUseRealtimePropagator(self):
        self.SetGroundVehicleToUseRealtimePropagator(GroundVehicle.m_Object)

    def SetGroundVehicleToUseRealtimePropagator(self, groundVehicle):
        # Set ground vehicle route to STK External propagator
        groundVehicle.SetRouteType(AgEVePropagatorType.ePropagatorRealtime)

        # Retrieve propagator interface if necessary
        propagator = clr.CastAs(groundVehicle.Route, IVehiclePropagatorRealtime)

    # endregion

    # region GetExportStkEphemerisTool
    def test_GetExportStkEphemerisTool(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.GetExportStkEphemerisTool(gv)
        (clr.Convert(gv, IStkObject)).Unload()

    def GetExportStkEphemerisTool(self, groundVehicle):
        stkEphem = groundVehicle.ExportTools.GetEphemerisStkExportTool()

    # endregion

    # region GetExportAttitudeTool
    def test_GetExportAttitudeTool(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.GetExportAttitudeTool(gv)
        (clr.Convert(gv, IStkObject)).Unload()

    def GetExportAttitudeTool(self, groundVehicle):
        attExTool = groundVehicle.ExportTools.GetAttitudeExportTool()

    # endregion

    # region GetExportPropDefTool
    def test_GetExportPropDefTool(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.GetExportPropDefTool(gv)
        (clr.Convert(gv, IStkObject)).Unload()

    def GetExportPropDefTool(self, groundVehicle):
        attExTool = groundVehicle.ExportTools.GetPropDefExportTool()

    # endregion
