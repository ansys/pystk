from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Constellation(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Constellation, self).__init__(*args, **kwargs)

    m_Object: "IConstellation" = None
    m_DefaultName: str = "constellation1"

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
        Constellation.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eConstellation, Constellation.m_DefaultName
            ),
            IConstellation,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eConstellation, Constellation.m_DefaultName
        )
        Constellation.m_Object = None

    # endregion

    # region AddObjectToConstellationUsingIAgStkObjectInterface
    def test_AddObjectToConstellationUsingIAgStkObjectInterface(self):
        alos: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eSatellite, "Alos"
        )
        self.AddObjectToConstellationUsingIAgStkObjectInterface(Constellation.m_Object, alos)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, alos.instance_name)

    def AddObjectToConstellationUsingIAgStkObjectInterface(self, constellation: "IConstellation", alos: "IStkObject"):
        # Add object to constellation
        constellation.objects.add_object(alos)

    # endregion

    # region AddObjectToConstellationByStkPath
    def test_AddObjectToConstellationByStkPath(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "Cameo")
        self.AddObjectToConstellationByStkPath(Constellation.m_Object)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "Cameo")

    def AddObjectToConstellationByStkPath(self, constellation: "IConstellation"):
        # Add object to constellation
        constellation.objects.add("Satellite/Cameo")

    # endregion
