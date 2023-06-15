from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class HPOP(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(HPOP, self).__init__(*args, **kwargs)

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
        HPOP.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, HPOP.m_DefaultName),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, HPOP.m_DefaultName)
        HPOP.m_Object = None

    # endregion

    # region ConfigureSatelliteWithHPOPPropagator
    def test_ConfigureSatelliteWithHPOPPropagator(self):
        self.ConfigureSatelliteWithHPOPPropagator(HPOP.m_Object)

    def ConfigureSatelliteWithHPOPPropagator(self, satellite: "ISatellite"):
        # Set satellite propagator to HPOP
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorHPOP)

        # Get IAgVePropagatorLOP interface
        hpopProp = clr.CastAs(satellite.Propagator, IVehiclePropagatorHPOP)

        # Configure force model
        hpopForceModel = hpopProp.ForceModel
        hpopForceModel.CentralBodyGravity.File = r"STKData\CentralBodies\Earth\GGM02C.grv"
        hpopForceModel.CentralBodyGravity.MaxDegree = 45
        hpopForceModel.CentralBodyGravity.MaxOrder = 10
        hpopForceModel.CentralBodyGravity.UseOceanTides = True

        hpopForceModel.Drag.Use = True
        hpopDragModel = clr.CastAs(hpopForceModel.Drag.DragModel, IVehicleHPOPDragModelSpherical)
        hpopDragModel.Cd = 1.89
        hpopDragModel.AreaMassRatio = 0.05
        hpopForceModel.Drag.AtmosphericDensityModel = AgEAtmosphericDensityModel.eMSIS90

        hpopForceModel.ThirdBodyGravity.RemoveThirdBody("Moon")

        # Propagate
        hpopProp.Propagate()

    # endregion
