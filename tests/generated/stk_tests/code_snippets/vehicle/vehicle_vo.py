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
        sat: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        self.ConfigureVeVOPass(sat.VO.Pass)
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")

    def ConfigureVeVOPass(self, veVoPass: "IVehicleVOPass"):
        # Set lead data type to fraction, retrieved IAgVeGfxLeadData implementation
        veVoPass.TrackData.PassData.GroundTrack.SetLeadDataType(AgELeadTrailData.eDataQuarter)

        veVoPass.TrackData.PassData.GroundTrack.SetTrailDataType(AgELeadTrailData.eDataHalf)
        veVoPass.TrackData.PassData.Orbit.SetLeadDataType(AgELeadTrailData.eDataQuarter)
        veVoPass.TrackData.PassData.Orbit.SetTrailSameAsLead()

        veVoPass.TickMarks.GroundTrack.IsVisible = True
        veVoPass.TickMarks.GroundTrack.SetTickDataType(AgETickData.eTickDataRadial)
        veVoPass.TickMarks.Orbit.IsVisible = True
        veVoPass.TickMarks.Orbit.SetTickDataType(AgETickData.eTickDataRadialAndCrossTrack)
        veVoPass.TickMarks.TimeBetweenTicks = 180

    # endregion

    # region ConfigureVeVODropline
    def test_ConfigureVeVODropline(self):
        satellite: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "satellite1"),
            ISatellite,
        )
        self.ConfigureVeVODropline(satellite.VO.DropLines.Orbit[0])
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "satellite1")

    def ConfigureVeVODropline(self, dropLine: "IVehicleVODropLinePathItem"):
        dropLine.IsVisible = True
        dropLine.Use2DColor = False
        dropLine.Color = Color.Red
        dropLine.LineStyle = AgELineStyle.eDashed
        dropLine.LineWidth = AgELineWidth.e4
        dropLine.Interval = 100.0  # in sec

    # endregion
