import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


@category("Graphics Tests")
class StkObjectGfxVO(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkObjectGfxVO, self).__init__(*args, **kwargs)

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

    # region SetUp
    def setUp(self):
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region SetStkOjbectDisplayToAlwaysOn
    def test_SetStkOjbectDisplayToAlwaysOn(self):
        facility = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "facility1")

        self.SetStkOjbectDisplayToAlwaysOn(facility)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def SetStkOjbectDisplayToAlwaysOn(self, stkObject):
        display = clr.CastAs(stkObject, IDisplayTime)
        display.SetDisplayStatusType(AgEDisplayTimesType.eAlwaysOn)

    # endregion

    # region SetStkObjectDisplayToUseIntervalsMode
    def test_SetStkObjectDisplayToUseIntervalsMode(self):
        facility = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "facility1")

        self.SetStkObjectDisplayToUseIntervalsMode(facility)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")

    def SetStkObjectDisplayToUseIntervalsMode(self, stkObject):
        # Attempt to cast STK Object to the IAgDisplayTm interface
        display = clr.CastAs(stkObject, IDisplayTime)
        if display != None:
            if display.IsDisplayStatusTypeSupported(AgEDisplayTimesType.eUseIntervals):
                display.SetDisplayStatusType(AgEDisplayTimesType.eUseIntervals)

                # Get IAgIntervalCollection interface
                intervalCollection = clr.CastAs(display.DisplayTimesData, IIntervalCollection)
                intervalCollection.RemoveAll()

                # Add subsequent intervals
                intervalCollection.Add("1 Jan 2012 12:00:00.00", "1 Jan 2012 13:00:00.000")

    # endregion

    # region SetStkObjectDisplayToUseDuringAccessMode
    def test_SetStkObjectDisplayToUseDuringAccessMode(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "satellite1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eStar, "star1")
        facility = CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "facility1")

        self.SetStkObjectDisplayToUseDuringAccessMode(facility)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eFacility, "facility1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eStar, "star1")
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "satellite1")

    def SetStkObjectDisplayToUseDuringAccessMode(self, stkObject):
        # Attempt to cast STK Object to the IAgDisplayTm interface
        display = clr.CastAs(stkObject, IDisplayTime)
        if display != None:
            if display.IsDisplayStatusTypeSupported(AgEDisplayTimesType.eDuringAccess):
                display.SetDisplayStatusType(AgEDisplayTimesType.eDuringAccess)

                duringAccess = clr.CastAs(display.DisplayTimesData, IDuringAccess)

                # Add subsequent existing stk objects to access display
                duringAccess.AccessObjects.Add("Satellite/satellite1")
                duringAccess.AccessObjects.Add("Star/star1")

    # endregion
