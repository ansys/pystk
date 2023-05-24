from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class Ship(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Ship, self).__init__(*args, **kwargs)

    m_Object = None
    m_DefaultName = "MyShip"

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
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eShip, Ship.m_DefaultName), IShip
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eShip, Ship.m_DefaultName)
        Ship.m_Object = None

    # endregion

    # region CreateShipOnCurrentScenarioCentralBody
    def test_CreateShipOnCurrentScenarioCentralBody(self):
        (clr.Convert(Ship.m_Object, IStkObject)).Unload()
        self.CreateShipOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateShipOnCurrentScenarioCentralBody(self, root):
        # Create the Ship
        ship = clr.CastAs(root.CurrentScenario.Children.New(AgESTKObjectType.eShip, "MyShip"), IShip)

    # endregion

    # region SetShipToUseGreatArcPropagator
    def test_SetShipToUseGreatArcPropagator(self):
        self.SetShipToUseGreatArcPropagator(Ship.m_Object)

    def SetShipToUseGreatArcPropagator(self, ship):
        # Set ship route to great arc
        ship.SetRouteType(AgEVePropagatorType.ePropagatorGreatArc)

        # Retrieve propagator interface if necessary
        propagator = clr.CastAs(ship.Route, IVehiclePropagatorGreatArc)

    # endregion

    # region SetShipToUseStkExternalPropagator
    def test_SetShipToUseStkExternalPropagator(self):
        self.SetShipToUseStkExternalPropagator(Ship.m_Object)

    def SetShipToUseStkExternalPropagator(self, ship):
        # Set ship route to STK External propagator
        ship.SetRouteType(AgEVePropagatorType.ePropagatorStkExternal)

        # Retrieve propagator interface if necessary
        propagator = clr.CastAs(ship.Route, IVehiclePropagatorStkExternal)

    # endregion

    # region SetShipToUseRealtimePropagator
    def test_SetShipToUseRealtimePropagator(self):
        self.SetShipToUseRealtimePropagator(Ship.m_Object)

    def SetShipToUseRealtimePropagator(self, ship):
        # Set ship route to STK External propagator
        ship.SetRouteType(AgEVePropagatorType.ePropagatorRealtime)

        # Retrieve propagator interface if necessary
        propagator = clr.CastAs(ship.Route, IVehiclePropagatorRealtime)

    # endregion
