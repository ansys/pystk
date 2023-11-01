from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class StkExternalSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkExternalSnippets, self).__init__(*args, **kwargs)

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
        StkExternalSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.SATELLITE, StkExternalSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, StkExternalSnippets.m_DefaultName
        )
        StkExternalSnippets.m_Object = None

    # endregion

    # region CreateSatelliteFromExternalEphemerisFile
    def test_CreateSatelliteFromExternalEphemerisFile(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, StkExternalSnippets.m_DefaultName
        )
        self.CreateSatelliteFromExternalEphemerisFile(
            CodeSnippetsTestBase.m_Root, TestBase.GetScenarioFile("CodeSnippetsTests", "TestEph.e")
        )

    def CreateSatelliteFromExternalEphemerisFile(self, root: "StkObjectRoot", ephemerisFilePath: str):
        satellite: "Satellite" = clr.CastAs(
            root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "MySatellite"), Satellite
        )

        # Configure propagator's external file path
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_STK_EXTERNAL)
        ext: "VehiclePropagatorStkExternal" = clr.CastAs(satellite.propagator, VehiclePropagatorStkExternal)
        ext.filename = ephemerisFilePath

        # Propagate
        ext.propagate()

    # endregion
