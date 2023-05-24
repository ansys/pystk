from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class StkExternal(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkExternal, self).__init__(*args, **kwargs)

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
        StkExternal.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eSatellite, StkExternal.m_DefaultName
            ),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eSatellite, StkExternal.m_DefaultName
        )
        StkExternal.m_Object = None

    # endregion

    # region CreateSatelliteFromExternalEphemerisFile
    def test_CreateSatelliteFromExternalEphemerisFile(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eSatellite, StkExternal.m_DefaultName
        )
        self.CreateSatelliteFromExternalEphemerisFile(
            CodeSnippetsTestBase.m_Root, TestBase.GetScenarioFile("TestEph.e")
        )

    def CreateSatelliteFromExternalEphemerisFile(self, root, ephemerisFilePath):
        satellite = clr.CastAs(
            root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "MySatellite"), ISatellite
        )

        # Configure propagator's external file path
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorStkExternal)
        ext = clr.CastAs(satellite.Propagator, IVehiclePropagatorStkExternal)
        ext.Filename = ephemerisFilePath

        # Propagate
        ext.Propagate()

    # endregion
