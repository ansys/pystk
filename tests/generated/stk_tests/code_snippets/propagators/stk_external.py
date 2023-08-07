from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class StkExternal(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkExternal, self).__init__(*args, **kwargs)

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
        StkExternal.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eSatellite, StkExternal.m_DefaultName
            ),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eSatellite, StkExternal.m_DefaultName
        )
        StkExternal.m_Object = None

    # endregion

    # region CreateSatelliteFromExternalEphemerisFile
    def test_CreateSatelliteFromExternalEphemerisFile(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eSatellite, StkExternal.m_DefaultName
        )
        self.CreateSatelliteFromExternalEphemerisFile(
            CodeSnippetsTestBase.m_Root, TestBase.GetScenarioFile("CodeSnippetsTests", "TestEph.e")
        )

    def CreateSatelliteFromExternalEphemerisFile(self, root: "IStkObjectRoot", ephemerisFilePath: str):
        satellite: "ISatellite" = clr.CastAs(
            root.current_scenario.children.new(AgESTKObjectType.eSatellite, "MySatellite"), ISatellite
        )

        # Configure propagator's external file path
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorStkExternal)
        ext: "IVehiclePropagatorStkExternal" = clr.CastAs(satellite.propagator, IVehiclePropagatorStkExternal)
        ext.filename = ephemerisFilePath

        # Propagate
        ext.propagate()

    # endregion
