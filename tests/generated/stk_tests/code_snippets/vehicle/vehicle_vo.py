from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


@category("VO Tests")
class VehicleVO(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(VehicleVO, self).__init__(*args, **kwargs)

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
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region ConfigureVeVOPass
    def test_ConfigureVeVOPass(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        self.ConfigureVeVOPass(sat.vo.pass_method)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "sat1")

    def ConfigureVeVOPass(self, veVoPass: "IVehicleVOPass"):
        # Set lead data type to fraction, retrieved IAgVeGfxLeadData implementation
        veVoPass.track_data.pass_data.ground_track.set_lead_data_type(AgELeadTrailData.eDataQuarter)

        veVoPass.track_data.pass_data.ground_track.set_trail_data_type(AgELeadTrailData.eDataHalf)
        veVoPass.track_data.pass_data.orbit.set_lead_data_type(AgELeadTrailData.eDataQuarter)
        veVoPass.track_data.pass_data.orbit.set_trail_same_as_lead()

        veVoPass.tick_marks.ground_track.is_visible = True
        veVoPass.tick_marks.ground_track.set_tick_data_type(AgETickData.eTickDataRadial)
        veVoPass.tick_marks.orbit.is_visible = True
        veVoPass.tick_marks.orbit.set_tick_data_type(AgETickData.eTickDataRadialAndCrossTrack)
        veVoPass.tick_marks.time_between_ticks = 180

    # endregion

    # region ConfigureVeVODropline
    def test_ConfigureVeVODropline(self):
        satellite: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        self.ConfigureVeVODropline(satellite.vo.drop_lines.orbit[0])
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "satellite1")

    def ConfigureVeVODropline(self, dropLine: "IVehicleVODropLinePathItem"):
        dropLine.is_visible = True
        dropLine.use2_d_color = False
        dropLine.color = Color.Red
        dropLine.line_style = AgELineStyle.eDashed
        dropLine.line_width = AgELineWidth.e4
        dropLine.interval = 100.0  # in sec

    # endregion
