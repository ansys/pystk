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
                STK_OBJECT_TYPE.GROUND_VEHICLE, GroundVehicleSnippets.m_DefaultName
            ),
            GroundVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.GROUND_VEHICLE, GroundVehicleSnippets.m_DefaultName
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
            root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "MyGroundVehicle"), GroundVehicle
        )

    # endregion

    # region SetGroundVehicleToUseGreatArcPropagator
    def test_SetGroundVehicleToUseGreatArcPropagator(self):
        self.SetGroundVehicleToUseGreatArcPropagator(GroundVehicleSnippets.m_Object)

    def SetGroundVehicleToUseGreatArcPropagator(self, groundVehicle: "GroundVehicle"):
        # Set ground vehicle route to great arc
        groundVehicle.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)

        # Retrieve propagator interface if necessary
        propagator: "VehiclePropagatorGreatArc" = clr.CastAs(groundVehicle.route, VehiclePropagatorGreatArc)

    # endregion

    # region SetGroundVehicleToUseStkExternalPropagator
    def test_SetGroundVehicleToUseStkExternalPropagator(self):
        self.SetGroundVehicleToUseStkExternalPropagator(GroundVehicleSnippets.m_Object)

    def SetGroundVehicleToUseStkExternalPropagator(self, groundVehicle: "GroundVehicle"):
        # Set groundVehicle route to STK External propagator
        groundVehicle.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_STK_EXTERNAL)

        # Retrieve propagator interface if necessary
        propagator: "VehiclePropagatorStkExternal" = clr.CastAs(groundVehicle.route, VehiclePropagatorStkExternal)

    # endregion

    # region SetGroundVehicleToUseRealtimePropagator
    def test_SetGroundVehicleToUseRealtimePropagator(self):
        self.SetGroundVehicleToUseRealtimePropagator(GroundVehicleSnippets.m_Object)

    def SetGroundVehicleToUseRealtimePropagator(self, groundVehicle: "GroundVehicle"):
        # Set ground vehicle route to STK External propagator
        groundVehicle.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)

        # Retrieve propagator interface if necessary
        propagator: "VehiclePropagatorRealtime" = clr.CastAs(groundVehicle.route, VehiclePropagatorRealtime)

    # endregion

    # region GetExportStkEphemerisTool
    def test_GetExportStkEphemerisTool(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        self.GetExportStkEphemerisTool(gv)
        (IStkObject(gv)).unload()

    def GetExportStkEphemerisTool(self, groundVehicle: "GroundVehicle"):
        stkEphem: "VehicleEphemerisStkExportTool" = groundVehicle.export_tools.get_ephemeris_stk_export_tool()

    # endregion

    # region GetExportAttitudeTool
    def test_GetExportAttitudeTool(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        self.GetExportPropDefTool(gv)
        (IStkObject(gv)).unload()

    def GetExportPropDefTool(self, groundVehicle: "GroundVehicle"):
        attExTool: "VehiclePropulsionDefinitionExportTool" = (
            groundVehicle.export_tools.get_propulsion_definition_export_tool()
        )

    # endregion
