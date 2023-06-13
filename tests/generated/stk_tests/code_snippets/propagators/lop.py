from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class LOP(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LOP, self).__init__(*args, **kwargs)

    m_Object: "ISatellite" = None
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
        LOP.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, LOP.m_DefaultName),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, LOP.m_DefaultName)
        LOP.m_Object = None

    # endregion

    # region ConfigureLOPPropagator
    def test_ConfigureLOPPropagator(self):
        self.ConfigureLOPPropagator(LOP.m_Object)

    def ConfigureLOPPropagator(self, satellite: "ISatellite"):
        # Set satellite propagator to LOP
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorLOP)

        # Get IAgVePropagatorLOP interface
        lopProp = clr.CastAs(satellite.Propagator, IVehiclePropagatorLOP)

        # Configure time period
        lopProp.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        lopProp.Step = 86400

        # Configure propagator initial state
        orbit = lopProp.InitialState.Representation
        orbit.Epoch = "1 Jan 2012 12:00:00.000"
        orbit.AssignCartesian(
            AgECoordinateSystem.eCoordinateSystemFixed, -1120.32, -9520.84, 0.129, 2.155, -1.54416, 5.668412
        )  # in km/sec

        # Configure force model
        lopForceModel = lopProp.ForceModel
        lopForceModel.CentralBodyGravity.MaxDegree = 15
        lopForceModel.CentralBodyGravity.MaxOrder = 8
        lopForceModel.Drag.Use = True
        lopForceModel.Drag.Cd = 3.55
        lopForceModel.SolarRadiationPressure.Use = True
        lopForceModel.SolarRadiationPressure.Cp = 1.125
        lopForceModel.SolarRadiationPressure.AtmosHeight = 125
        lopForceModel.PhysicalData.DragCrossSectionalArea = 0.001555512
        lopForceModel.PhysicalData.SRPCrossSectionalArea = 0.001810026
        lopForceModel.PhysicalData.SatelliteMass = 1505.001

        # Propagate
        lopProp.Propagate()

    # endregion
