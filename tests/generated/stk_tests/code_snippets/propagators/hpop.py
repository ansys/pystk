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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, HPOP.m_DefaultName),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, HPOP.m_DefaultName)
        HPOP.m_Object = None

    # endregion

    # region ConfigureSatelliteWithHPOPPropagator
    def test_ConfigureSatelliteWithHPOPPropagator(self):
        self.ConfigureSatelliteWithHPOPPropagator(HPOP.m_Object)

    def ConfigureSatelliteWithHPOPPropagator(self, satellite: "ISatellite"):
        # Set satellite propagator to HPOP
        satellite.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)

        # Get IVehiclePropagatorLOP interface
        hpopProp: "IVehiclePropagatorHPOP" = clr.CastAs(satellite.propagator, IVehiclePropagatorHPOP)

        # Configure force model
        hpopForceModel: "IVehicleHPOPForceModel" = hpopProp.force_model
        hpopForceModel.central_body_gravity.file = r"STKData\CentralBodies\Earth\GGM02C.grv"
        hpopForceModel.central_body_gravity.max_degree = 45
        hpopForceModel.central_body_gravity.max_order = 10
        hpopForceModel.central_body_gravity.use_ocean_tides = True

        hpopForceModel.drag.use = True
        hpopDragModel: "IVehicleHPOPDragModelSpherical" = clr.CastAs(
            hpopForceModel.drag.drag_model, IVehicleHPOPDragModelSpherical
        )
        hpopDragModel.cd = 1.89
        hpopDragModel.area_mass_ratio = 0.05
        hpopForceModel.drag.atmospheric_density_model = ATMOSPHERIC_DENSITY_MODEL.MSIS90

        hpopForceModel.third_body_gravity.remove_third_body("Moon")

        # Propagate
        hpopProp.propagate()

    # endregion
