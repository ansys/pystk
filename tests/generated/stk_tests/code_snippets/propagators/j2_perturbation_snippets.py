from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class J2PerturbationSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(J2PerturbationSnippets, self).__init__(*args, **kwargs)

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
        J2PerturbationSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.SATELLITE, J2PerturbationSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, J2PerturbationSnippets.m_DefaultName
        )
        J2PerturbationSnippets.m_Object = None

    # endregion

    # region ConfigureSatelliteWithJ2PerturbationPropagator
    def test_ConfigureSatelliteWithJ2PerturbationPropagator(self):
        self.ConfigureSatelliteWithJ2PerturbationPropagator(J2PerturbationSnippets.m_Object)

    def ConfigureSatelliteWithJ2PerturbationPropagator(self, satellite: "Satellite"):
        # Set propagator to SGP4
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)

        # J2 Perturbation propagator
        j2prop: "VehiclePropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, VehiclePropagatorJ2Perturbation)

        # Configure time period
        j2prop.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.step = 60.0

        # Configure propagator initial state
        initial: "VehicleJxInitialState" = j2prop.initial_state
        initial.representation.epoch = "1 Jan 2012 12:00:00.000"
        initial.representation.assign_cartesian(
            COORDINATE_SYSTEM.FIXED, -1514.4, -6790.1, -1.25, 4.8151, 1.771, 5.6414
        )  # in km/sec
        initial.ellipse_options = VEHICLE_ELLIPSE_OPTIONS.SECULARLY_PRECESSING

        # Propagate
        j2prop.propagate()

    # endregion
