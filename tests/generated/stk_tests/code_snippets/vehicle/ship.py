from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class Ship(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Ship, self).__init__(*args, **kwargs)

    m_Object: "IShip" = None
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
        Ship.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, Ship.m_DefaultName), IShip
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SHIP, Ship.m_DefaultName)
        Ship.m_Object = None

    # endregion

    # region CreateShipOnCurrentScenarioCentralBody
    def test_CreateShipOnCurrentScenarioCentralBody(self):
        (clr.Convert(Ship.m_Object, IStkObject)).unload()
        self.CreateShipOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateShipOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Ship
        ship: "IShip" = clr.CastAs(root.current_scenario.children.new(STK_OBJECT_TYPE.SHIP, "MyShip"), IShip)

    # endregion

    # region SetShipToUseGreatArcPropagator
    def test_SetShipToUseGreatArcPropagator(self):
        self.SetShipToUseGreatArcPropagator(Ship.m_Object)

    def SetShipToUseGreatArcPropagator(self, ship: "IShip"):
        # Set ship route to great arc
        ship.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)

        # Retrieve propagator interface if necessary
        propagator: "IVehiclePropagatorGreatArc" = clr.CastAs(ship.route, IVehiclePropagatorGreatArc)

    # endregion

    # region SetShipToUseStkExternalPropagator
    def test_SetShipToUseStkExternalPropagator(self):
        self.SetShipToUseStkExternalPropagator(Ship.m_Object)

    def SetShipToUseStkExternalPropagator(self, ship: "IShip"):
        # Set ship route to STK External propagator
        ship.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_STK_EXTERNAL)

        # Retrieve propagator interface if necessary
        propagator: "IVehiclePropagatorStkExternal" = clr.CastAs(ship.route, IVehiclePropagatorStkExternal)

    # endregion

    # region SetShipToUseRealtimePropagator
    def test_SetShipToUseRealtimePropagator(self):
        self.SetShipToUseRealtimePropagator(Ship.m_Object)

    def SetShipToUseRealtimePropagator(self, ship: "IShip"):
        # Set ship route to STK External propagator
        ship.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)

        # Retrieve propagator interface if necessary
        propagator: "IVehiclePropagatorRealtime" = clr.CastAs(ship.route, IVehiclePropagatorRealtime)

    # endregion
