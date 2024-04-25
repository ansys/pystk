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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, ShipSnippets.m_DefaultName),
            Ship,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SHIP, ShipSnippets.m_DefaultName)
        ShipSnippets.m_Object = None

    # endregion

    # region CreateShipOnCurrentScenarioCentralBody
    def test_CreateShipOnCurrentScenarioCentralBody(self):
        (IStkObject(ShipSnippets.m_Object)).unload()
        self.CreateShipOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateShipOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Ship
        ship: "Ship" = clr.CastAs(root.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, "MyShip"), Ship)

    # endregion

    # region SetShipToUseGreatArcPropagator
    def test_SetShipToUseGreatArcPropagator(self):
        self.SetShipToUseGreatArcPropagator(ShipSnippets.m_Object)

    def SetShipToUseGreatArcPropagator(self, ship: "Ship"):
        # Set ship route to great arc
        ship.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)

        # Retrieve propagator interface if necessary
        propagator: "VehiclePropagatorGreatArc" = clr.CastAs(ship.route, VehiclePropagatorGreatArc)

    # endregion

    # region SetShipToUseStkExternalPropagator
    def test_SetShipToUseStkExternalPropagator(self):
        self.SetShipToUseStkExternalPropagator(ShipSnippets.m_Object)

    def SetShipToUseStkExternalPropagator(self, ship: "Ship"):
        # Set ship route to STK External propagator
        ship.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_STK_EXTERNAL)

        # Retrieve propagator interface if necessary
        propagator: "VehiclePropagatorStkExternal" = clr.CastAs(ship.route, VehiclePropagatorStkExternal)

    # endregion

    # region SetShipToUseRealtimePropagator
    def test_SetShipToUseRealtimePropagator(self):
        self.SetShipToUseRealtimePropagator(ShipSnippets.m_Object)

    def SetShipToUseRealtimePropagator(self, ship: "Ship"):
        # Set ship route to STK External propagator
        ship.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)

        # Retrieve propagator interface if necessary
        propagator: "VehiclePropagatorRealtime" = clr.CastAs(ship.route, VehiclePropagatorRealtime)

    # endregion
