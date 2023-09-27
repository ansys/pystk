from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class SPICE(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SPICE, self).__init__(*args, **kwargs)

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
        SPICE.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, SPICE.m_DefaultName),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, SPICE.m_DefaultName)
        SPICE.m_Object = None

    # endregion

    # region ConfigureSPICEPropagator
    def test_ConfigureSPICEPropagator(self):
        SPICE.m_Object.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SPICE)
        spiceProp: "IVehiclePropagatorSPICE" = clr.CastAs(SPICE.m_Object.propagator, IVehiclePropagatorSPICE)
        self.ConfigureSPICEPropagator(
            spiceProp, TestBase.GetScenarioFile("CodeSnippetsTests", "External", "Satellite1.bsp")
        )

    def ConfigureSPICEPropagator(self, propagator: "IVehiclePropagatorSPICE", spiceFile: str):
        # Set the SPICE file
        propagator.spice = spiceFile

        # Configure time period
        propagator.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        propagator.step = 60.0
        propagator.body_name = "-200000"

        # Propagate
        propagator.propagate()

    # endregion
