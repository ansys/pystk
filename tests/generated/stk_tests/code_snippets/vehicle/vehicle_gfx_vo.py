from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


@category("Graphics Tests")
class VehicleGfxVO(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(VehicleGfxVO, self).__init__(*args, **kwargs)

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

    # region SetVehicleGfxToCustomIntervals
    def test_SetVehicleGfxToCustomIntervals(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.SetVehicleGfxToCustomIntervals(gv.Graphics)
        (clr.Convert(gv, IStkObject)).Unload()

    def SetVehicleGfxToCustomIntervals(self, graphics: "IGreatArcGraphics"):
        if graphics.IsAttributesTypeSupported(AgEVeGfxAttributes.eAttributesCustom):
            # Set graphics to custom
            graphics.SetAttributesType(AgEVeGfxAttributes.eAttributesCustom)

            # Get IAgVeGfxAttributesCustom interface
            customAttributes = clr.CastAs(graphics.Attributes, IVehicleGfxAttributesCustom)

    # endregion

    # region ConfigureVehicleGfxCustomIntervals
    def test_ConfigureVehicleGfxCustomIntervals(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        gv.Graphics.SetAttributesType(AgEVeGfxAttributes.eAttributesCustom)
        customAttributes = clr.CastAs(gv.Graphics.Attributes, IVehicleGfxAttributesCustom)
        self.ConfigureVehicleGfxCustomIntervals(customAttributes)
        (clr.Convert(gv, IStkObject)).Unload()

    def ConfigureVehicleGfxCustomIntervals(self, customAttributes: "IVehicleGfxAttributesCustom"):
        customIntervals = customAttributes.Intervals

        # Add intervals
        customIntervals.Add("1 Jan 2012 12:00:00.000", "1 Jan 2012 14:00:00.000")
        customIntervals.Add("2 Jan 2012 01:00:00.000", "2 Jan 2012 02:00:00.000")

        # Deconflict intervals if necessary
        customAttributes.Deconflict()

    # endregion

    # region SetVehicleGfxToBasic
    def test_SetVehicleGfxToBasic(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.SetVehicleGfxToBasic(gv.Graphics)
        (clr.Convert(gv, IStkObject)).Unload()

    def SetVehicleGfxToBasic(self, graphics: "IGreatArcGraphics"):
        if graphics.IsAttributesTypeSupported(AgEVeGfxAttributes.eAttributesBasic):
            # Set graphics to basic
            graphics.SetAttributesType(AgEVeGfxAttributes.eAttributesBasic)

            # Get IAgVeGfxAttributesBasic interface
            basicAttributes = clr.CastAs(graphics.Attributes, IVehicleGfxAttributesBasic)

    # endregion

    # region ConfigureVehicleGfxBasic
    def test_ConfigureVehicleGfxBasic(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        gv.Graphics.SetAttributesType(AgEVeGfxAttributes.eAttributesBasic)
        basicAttributes = clr.CastAs(gv.Graphics.Attributes, IVehicleGfxAttributesBasic)
        self.ConfigureVehicleGfxBasic(basicAttributes)
        (clr.Convert(gv, IStkObject)).Unload()

    def ConfigureVehicleGfxBasic(self, basicAttributes: "IVehicleGfxAttributesBasic"):
        # Change display
        basicAttributes.IsVisible = True
        basicAttributes.Color = Color.Red
        basicAttributes.Line.Style = AgELineStyle.eDotted
        basicAttributes.Line.Width = AgELineWidth.e3
        basicAttributes.MarkerStyle = "Square"

    # endregion

    # region SetVehicleGfxToAccessIntervals
    def test_SetVehicleGfxToAccessIntervals(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        sat = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        self.SetVehicleGfxToAccessIntervals(gv.Graphics)
        (clr.Convert(sat, IStkObject)).Unload()
        (clr.Convert(gv, IStkObject)).Unload()

    def SetVehicleGfxToAccessIntervals(self, graphics: "IGreatArcGraphics"):
        if graphics.IsAttributesTypeSupported(AgEVeGfxAttributes.eAttributesAccess):
            # Set graphics to access intervals
            graphics.SetAttributesType(AgEVeGfxAttributes.eAttributesAccess)

            # Get IAgVeGfxAttributesAccess interface
            accessAttributes = clr.CastAs(graphics.Attributes, IVehicleGfxAttributesAccess)

    # endregion

    # region ConfigureVehicleGfxAccessIntervals
    def test_ConfigureVehicleGfxAccessIntervals(self):
        gv = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        sat = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        gv.Graphics.SetAttributesType(AgEVeGfxAttributes.eAttributesAccess)
        accessAttributes = clr.CastAs(gv.Graphics.Attributes, IVehicleGfxAttributesAccess)
        self.ConfigureVehicleGfxAccessIntervals(accessAttributes)
        (clr.Convert(sat, IStkObject)).Unload()
        (clr.Convert(gv, IStkObject)).Unload()

    def ConfigureVehicleGfxAccessIntervals(self, accessAttributes: "IVehicleGfxAttributesAccess"):
        accessAttributes.AccessObjects.Add("Satellite/sat1")

        accessAttributes.DuringAccess.IsVisible = True
        accessAttributes.DuringAccess.Color = Color.Yellow
        accessAttributes.NoAccess.IsVisible = True
        accessAttributes.NoAccess.Color = Color.Red

    # endregion

    # region ConfigureVehicleGfxVOElevationContours
    def test_ConfigureVehicleGfxVOElevationContours(self):
        sat = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )

        self.ConfigureVehicleGfxVOElevationContours(sat.Graphics.ElevContours, sat.VO.ElevContours)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")

    def ConfigureVehicleGfxVOElevationContours(
        self, gfxContours: "IVehicleGfxElevContours", voContours: "IVehicleVOElevContours"
    ):
        gfxContours.IsVisible = True
        gfxContours.IsFillVisible = True
        gfxContours.FillStyle = AgEFillStyle.eFillStyleHorizontalStripe
        gfxContours.NumOfDecimalDigits = 5

        # Add contour elevation level
        elevation = gfxContours.Elevations.AddLevel(25.0)

        # Configure contour elevation element
        elevation.Color = Color.Red
        elevation.DistanceVisible = True
        elevation.LineStyle = AgELineStyle.eDotted
        elevation.LineWidth = AgELineWidth.e3
        elevation.UserTextVisible = True
        elevation.UserText = "My new elevation"

        # Set contours to visible on scenario
        voContours.IsVisible = True
        voContours.Fill = True
        voContours.FillTranslucency = 80.0

    # endregion

    # region ConfigureVehicleGfxVOSunLighting
    def test_ConfigureVehicleGfxVOSunLighting(self):
        sat = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        self.ConfigureVehicleGfxVOSunLighting(sat.Graphics.Lighting)
        (clr.Convert(sat, IStkObject)).Unload()

    def ConfigureVehicleGfxVOSunLighting(self, lighting: "IVehicleGfxLighting"):
        sunlight = lighting.Sunlight

        sunlight.Visible = True
        sunlight.Color = Color.Red
        sunlight.LineStyle = AgELineStyle.eDotted
        sunlight.LineWidth = AgELineWidth.e3
        sunlight.MarkerStyle = "Circle"

    # endregion
