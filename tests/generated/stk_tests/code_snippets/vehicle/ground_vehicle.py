from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class GroundVehicle(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(GroundVehicle, self).__init__(*args, **kwargs)

    m_Object: "IGroundVehicle" = None
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

    def CreateGroundVehicleOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the ground vehicle
        launchVehicle: "IGroundVehicle" = clr.CastAs(
            root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "MyGroundVehicle"), IGroundVehicle
        )

    # endregion

    # region SetGroundVehicleToUseGreatArcPropagator
    def test_SetGroundVehicleToUseGreatArcPropagator(self):
        self.SetGroundVehicleToUseGreatArcPropagator(GroundVehicle.m_Object)

    def SetGroundVehicleToUseGreatArcPropagator(self, groundVehicle: "IGroundVehicle"):
        # Set ground vehicle route to great arc
        groundVehicle.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Retrieve propagator interface if necessary
        propagator: "IVehiclePropagatorGreatArc" = clr.CastAs(groundVehicle.Route, IVehiclePropagatorGreatArc)

    # endregion

    # region SetGroundVehicleToUseStkExternalPropagator
    def test_SetGroundVehicleToUseStkExternalPropagator(self):
        self.SetGroundVehicleToUseStkExternalPropagator(GroundVehicle.m_Object)

    def SetGroundVehicleToUseStkExternalPropagator(self, groundVehicle: "IGroundVehicle"):
        # Set groundVehicle route to STK External propagator
        groundVehicle.SetRouteType(AgEVePropagatorType.ePropagatorStkExternal)

        # Retrieve propagator interface if necessary
        propagator: "IVehiclePropagatorStkExternal" = clr.CastAs(groundVehicle.Route, IVehiclePropagatorStkExternal)

    # endregion

    # region SetGroundVehicleToUseRealtimePropagator
    def test_SetGroundVehicleToUseRealtimePropagator(self):
        self.SetGroundVehicleToUseRealtimePropagator(GroundVehicle.m_Object)

    def SetGroundVehicleToUseRealtimePropagator(self, groundVehicle: "IGroundVehicle"):
        # Set ground vehicle route to STK External propagator
        groundVehicle.SetRouteType(AgEVePropagatorType.ePropagatorRealtime)

        # Retrieve propagator interface if necessary
        propagator: "IVehiclePropagatorRealtime" = clr.CastAs(groundVehicle.Route, IVehiclePropagatorRealtime)

    # endregion

    # region GetExportStkEphemerisTool
    def test_GetExportStkEphemerisTool(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.GetExportStkEphemerisTool(gv)
        (clr.Convert(gv, IStkObject)).Unload()

    def GetExportStkEphemerisTool(self, groundVehicle: "IGroundVehicle"):
        stkEphem: "IVehicleEphemerisStkExportTool" = groundVehicle.ExportTools.GetEphemerisStkExportTool()

    # endregion

    # region GetExportAttitudeTool
    def test_GetExportAttitudeTool(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.GetExportAttitudeTool(gv)
        (clr.Convert(gv, IStkObject)).Unload()

    def GetExportAttitudeTool(self, groundVehicle: "IGroundVehicle"):
        attExTool: "IVehicleAttitudeExportTool" = groundVehicle.ExportTools.GetAttitudeExportTool()

    # endregion

    # region GetExportPropDefTool
    def test_GetExportPropDefTool(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.GetExportPropDefTool(gv)
        (clr.Convert(gv, IStkObject)).Unload()

    def GetExportPropDefTool(self, groundVehicle: "IGroundVehicle"):
        attExTool: "IVehiclePropDefinitionExportTool" = groundVehicle.ExportTools.GetPropDefExportTool()

    # endregion
