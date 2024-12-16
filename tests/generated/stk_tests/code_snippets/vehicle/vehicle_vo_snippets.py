from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


@category("VO Tests")
class VehicleVOSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(VehicleVOSnippets, self).__init__(*args, **kwargs)

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
        sat: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat1"), Satellite
        )
        self.ConfigureVeVOPass(sat.graphics_3d.satellite_pass)
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat1")

    def ConfigureVeVOPass(self, veVoPass: "VehicleGraphics3DPass"):
        # Set lead data type to fraction, retrieved IAgVeGfxLeadData implementation
        veVoPass.track_data.pass_data.ground_track.set_lead_data_type(LeadTrailData.QUARTER)

        veVoPass.track_data.pass_data.ground_track.set_trail_data_type(LeadTrailData.HALF)
        veVoPass.track_data.pass_data.orbit.set_lead_data_type(LeadTrailData.QUARTER)
        veVoPass.track_data.pass_data.orbit.set_trail_same_as_lead()

        veVoPass.tick_marks.ground_track.show_graphics = True
        veVoPass.tick_marks.ground_track.set_tick_data_type(TickData.RADIAL)
        veVoPass.tick_marks.orbit.show_graphics = True
        veVoPass.tick_marks.orbit.set_tick_data_type(TickData.RADIAL_AND_CROSS_TRACK)
        veVoPass.tick_marks.time_between_ticks = 180

    # endregion

    # region ConfigureVeVODropline
    def test_ConfigureVeVODropline(self):
        satellite: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite1"), Satellite
        )
        self.ConfigureVeVODropline(satellite.graphics_3d.drop_lines.orbit[0])
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "satellite1")

    def ConfigureVeVODropline(self, dropLine: "VehicleGraphics3DDropLinePathItem"):
        dropLine.show_graphics = True
        dropLine.use_2d_color = False
        dropLine.color = Colors.Red
        dropLine.line_style = LineStyle.DASHED
        dropLine.line_width = LineWidth.WIDTH4
        dropLine.interval = 100.0  # in sec

    # endregion
