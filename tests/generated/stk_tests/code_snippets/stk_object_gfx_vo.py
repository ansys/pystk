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
        facility: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )

        self.SetStkOjbectDisplayToAlwaysOn(facility)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def SetStkOjbectDisplayToAlwaysOn(self, stkObject: "IStkObject"):
        display: "IDisplayTime" = clr.CastAs(stkObject, IDisplayTime)
        display.set_display_status_type(AgEDisplayTimesType.eAlwaysOn)

    # endregion

    # region SetStkObjectDisplayToUseIntervalsMode
    def test_SetStkObjectDisplayToUseIntervalsMode(self):
        facility: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )

        self.SetStkObjectDisplayToUseIntervalsMode(facility)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")

    def SetStkObjectDisplayToUseIntervalsMode(self, stkObject: "IStkObject"):
        # Attempt to cast STK Object to the IDisplayTime interface
        display: "IDisplayTime" = clr.CastAs(stkObject, IDisplayTime)
        if display != None:
            if display.is_display_status_type_supported(AgEDisplayTimesType.eUseIntervals):
                display.set_display_status_type(AgEDisplayTimesType.eUseIntervals)

                # Get IIntervalCollection interface
                intervalCollection: "IIntervalCollection" = clr.CastAs(display.display_times_data, IIntervalCollection)
                intervalCollection.remove_all()

                # Add subsequent intervals
                intervalCollection.add("1 Jan 2012 12:00:00.00", "1 Jan 2012 13:00:00.000")

    # endregion

    # region SetStkObjectDisplayToUseDuringAccessMode
    def test_SetStkObjectDisplayToUseDuringAccessMode(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "satellite1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eStar, "star1")
        facility: "IStkObject" = CodeSnippetsTestBase.m_Root.current_scenario.children.new(
            AgESTKObjectType.eFacility, "facility1"
        )

        self.SetStkObjectDisplayToUseDuringAccessMode(facility)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eFacility, "facility1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eStar, "star1")
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "satellite1")

    def SetStkObjectDisplayToUseDuringAccessMode(self, stkObject: "IStkObject"):
        # Attempt to cast STK Object to the IDisplayTime interface
        display: "IDisplayTime" = clr.CastAs(stkObject, IDisplayTime)
        if display != None:
            if display.is_display_status_type_supported(AgEDisplayTimesType.eDuringAccess):
                display.set_display_status_type(AgEDisplayTimesType.eDuringAccess)

                duringAccess: "IDuringAccess" = clr.CastAs(display.display_times_data, IDuringAccess)

                # Add subsequent existing stk objects to access display
                duringAccess.access_objects.add("Satellite/satellite1")
                duringAccess.access_objects.add("Star/star1")

    # endregion
