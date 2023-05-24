import sys
import os

sys.path.insert(1, os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class SPICE(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SPICE, self).__init__(*args, **kwargs)

    m_Object = None
    m_DefaultName = "MySatellite"

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
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, SPICE.m_DefaultName),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, SPICE.m_DefaultName)
        SPICE.m_Object = None

    # endregion

    # region ConfigureSPICEPropagator
    def test_ConfigureSPICEPropagator(self):
        SPICE.m_Object.SetPropagatorType(AgEVePropagatorType.ePropagatorSPICE)
        spiceProp = clr.CastAs(SPICE.m_Object.Propagator, IVehiclePropagatorSPICE)
        self.ConfigureSPICEPropagator(
            spiceProp, TestBase.GetScenarioFile(TestBase.PathCombine("External", "Satellite1.bsp"))
        )

    def ConfigureSPICEPropagator(self, propagator, spiceFile):
        # Set the SPICE file
        propagator.Spice = spiceFile

        # Configure time period
        propagator.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        propagator.Step = 60.0
        propagator.BodyName = "-200000"

        # Propagate
        propagator.Propagate()

    # endregion
