import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Constellation(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Constellation, self).__init__(*args, **kwargs)

    m_Object = None
    m_DefaultName = "constellation1"

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
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eConstellation, Constellation.m_DefaultName
            ),
            IConstellation,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eConstellation, Constellation.m_DefaultName
        )
        Constellation.m_Object = None

    # endregion

    # region AddObjectToConstellationUsingIAgStkObjectInterface
    def test_AddObjectToConstellationUsingIAgStkObjectInterface(self):
        alos = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Alos")
        self.AddObjectToConstellationUsingIAgStkObjectInterface(Constellation.m_Object, alos)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, alos.InstanceName)

    def AddObjectToConstellationUsingIAgStkObjectInterface(self, constellation, alos):
        # Add object to constellation
        constellation.Objects.AddObject(alos)

    # endregion

    # region AddObjectToConstellationByStkPath
    def test_AddObjectToConstellationByStkPath(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Cameo")
        self.AddObjectToConstellationByStkPath(Constellation.m_Object)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "Cameo")

    def AddObjectToConstellationByStkPath(self, constellation):
        # Add object to constellation
        constellation.Objects.Add("Satellite/Cameo")

    # endregion
