from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class LOPSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LOPSnippets, self).__init__(*args, **kwargs)

    m_Object: "Satellite" = None
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
        LOPSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.SATELLITE, LOPSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, LOPSnippets.m_DefaultName
        )
        LOPSnippets.m_Object = None

    # endregion

    # region ConfigureLOPPropagator
    def test_ConfigureLOPPropagator(self):
        self.ConfigureLOPPropagator(LOPSnippets.m_Object)

    def ConfigureLOPPropagator(self, satellite: "Satellite"):
        # Set satellite propagator to LOP
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_LOP)

        # Get VehiclePropagatorLOP interface
        lopProp: "VehiclePropagatorLOP" = clr.CastAs(satellite.propagator, VehiclePropagatorLOP)

        # Configure time period
        lopProp.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        lopProp.step = 86400

        # Configure propagator initial state
        orbit: "IOrbitState" = lopProp.initial_state.representation
        orbit.epoch = "1 Jan 2012 12:00:00.000"
        orbit.assign_cartesian(
            COORDINATE_SYSTEM.FIXED, -1120.32, -9520.84, 0.129, 2.155, -1.54416, 5.668412
        )  # in km/sec

        # Configure force model
        lopForceModel: "VehicleLOPForceModel" = lopProp.force_model
        lopForceModel.central_body_gravity.max_degree = 15
        lopForceModel.central_body_gravity.max_order = 8
        lopForceModel.drag.use = True
        lopForceModel.drag.cd = 3.55
        lopForceModel.solar_radiation_pressure.use = True
        lopForceModel.solar_radiation_pressure.cp = 1.125
        lopForceModel.solar_radiation_pressure.atmos_height = 125
        lopForceModel.physical_data.drag_cross_sectional_area = 0.001555512
        lopForceModel.physical_data.srp_cross_sectional_area = 0.001810026
        lopForceModel.physical_data.satellite_mass = 1505.001

        # Propagate
        lopProp.propagate()

    # endregion
