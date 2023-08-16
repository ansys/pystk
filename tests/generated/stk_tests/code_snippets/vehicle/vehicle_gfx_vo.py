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
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.SetVehicleGfxToCustomIntervals(gv.graphics)
        (clr.Convert(gv, IStkObject)).unload()

    def SetVehicleGfxToCustomIntervals(self, graphics: "IGreatArcGraphics"):
        if graphics.is_attributes_type_supported(AgEVeGfxAttributes.eAttributesCustom):
            # Set graphics to custom
            graphics.set_attributes_type(AgEVeGfxAttributes.eAttributesCustom)

            # Get IAgVeGfxAttributesCustom interface
            customAttributes: "IVehicleGfxAttributesCustom" = clr.CastAs(
                graphics.attributes, IVehicleGfxAttributesCustom
            )

    # endregion

    # region ConfigureVehicleGfxCustomIntervals
    def test_ConfigureVehicleGfxCustomIntervals(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        gv.graphics.set_attributes_type(AgEVeGfxAttributes.eAttributesCustom)
        customAttributes: "IVehicleGfxAttributesCustom" = clr.CastAs(
            gv.graphics.attributes, IVehicleGfxAttributesCustom
        )
        self.ConfigureVehicleGfxCustomIntervals(customAttributes)
        (clr.Convert(gv, IStkObject)).unload()

    def ConfigureVehicleGfxCustomIntervals(self, customAttributes: "IVehicleGfxAttributesCustom"):
        customIntervals: "IVehicleGfxIntervalsCollection" = customAttributes.intervals

        # Add intervals
        customIntervals.add("1 Jan 2012 12:00:00.000", "1 Jan 2012 14:00:00.000")
        customIntervals.add("2 Jan 2012 01:00:00.000", "2 Jan 2012 02:00:00.000")

        # Deconflict intervals if necessary
        customAttributes.deconflict()

    # endregion

    # region SetVehicleGfxToBasic
    def test_SetVehicleGfxToBasic(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        self.SetVehicleGfxToBasic(gv.graphics)
        (clr.Convert(gv, IStkObject)).unload()

    def SetVehicleGfxToBasic(self, graphics: "IGreatArcGraphics"):
        if graphics.is_attributes_type_supported(AgEVeGfxAttributes.eAttributesBasic):
            # Set graphics to basic
            graphics.set_attributes_type(AgEVeGfxAttributes.eAttributesBasic)

            # Get IAgVeGfxAttributesBasic interface
            basicAttributes: "IVehicleGfxAttributesBasic" = clr.CastAs(graphics.attributes, IVehicleGfxAttributesBasic)

    # endregion

    # region ConfigureVehicleGfxBasic
    def test_ConfigureVehicleGfxBasic(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        gv.graphics.set_attributes_type(AgEVeGfxAttributes.eAttributesBasic)
        basicAttributes: "IVehicleGfxAttributesBasic" = clr.CastAs(gv.graphics.attributes, IVehicleGfxAttributesBasic)
        self.ConfigureVehicleGfxBasic(basicAttributes)
        (clr.Convert(gv, IStkObject)).unload()

    def ConfigureVehicleGfxBasic(self, basicAttributes: "IVehicleGfxAttributesBasic"):
        # Change display
        basicAttributes.is_visible = True
        basicAttributes.color = Color.Red
        basicAttributes.line.style = AgELineStyle.eDotted
        basicAttributes.line.width = AgELineWidth.e3
        basicAttributes.marker_style = "Square"

    # endregion

    # region SetVehicleGfxToAccessIntervals
    def test_SetVehicleGfxToAccessIntervals(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        self.SetVehicleGfxToAccessIntervals(gv.graphics)
        (clr.Convert(sat, IStkObject)).unload()
        (clr.Convert(gv, IStkObject)).unload()

    def SetVehicleGfxToAccessIntervals(self, graphics: "IGreatArcGraphics"):
        if graphics.is_attributes_type_supported(AgEVeGfxAttributes.eAttributesAccess):
            # Set graphics to access intervals
            graphics.set_attributes_type(AgEVeGfxAttributes.eAttributesAccess)

            # Get IAgVeGfxAttributesAccess interface
            accessAttributes: "IVehicleGfxAttributesAccess" = clr.CastAs(
                graphics.attributes, IVehicleGfxAttributesAccess
            )

    # endregion

    # region ConfigureVehicleGfxAccessIntervals
    def test_ConfigureVehicleGfxAccessIntervals(self):
        gv: "IGroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eGroundVehicle, "gv1"),
            IGroundVehicle,
        )
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        gv.graphics.set_attributes_type(AgEVeGfxAttributes.eAttributesAccess)
        accessAttributes: "IVehicleGfxAttributesAccess" = clr.CastAs(
            gv.graphics.attributes, IVehicleGfxAttributesAccess
        )
        self.ConfigureVehicleGfxAccessIntervals(accessAttributes)
        (clr.Convert(sat, IStkObject)).unload()
        (clr.Convert(gv, IStkObject)).unload()

    def ConfigureVehicleGfxAccessIntervals(self, accessAttributes: "IVehicleGfxAttributesAccess"):
        accessAttributes.access_objects.add("Satellite/sat1")

        accessAttributes.during_access.is_visible = True
        accessAttributes.during_access.color = Color.Yellow
        accessAttributes.no_access.is_visible = True
        accessAttributes.no_access.color = Color.Red

    # endregion

    # region ConfigureVehicleGfxVOElevationContours
    def test_ConfigureVehicleGfxVOElevationContours(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )

        self.ConfigureVehicleGfxVOElevationContours(sat.graphics.elev_contours, sat.vo.elev_contours)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(AgESTKObjectType.eSatellite, "sat1")

    def ConfigureVehicleGfxVOElevationContours(
        self, gfxContours: "IVehicleGfxElevContours", voContours: "IVehicleVOElevContours"
    ):
        gfxContours.is_visible = True
        gfxContours.is_fill_visible = True
        gfxContours.fill_style = AgEFillStyle.eFillStyleHorizontalStripe
        gfxContours.num_of_decimal_digits = 5

        # Add contour elevation level
        elevation: "IVehicleGfxElevationsElement" = gfxContours.elevations.add_level(25.0)

        # Configure contour elevation element
        elevation.color = Color.Red
        elevation.distance_visible = True
        elevation.line_style = AgELineStyle.eDotted
        elevation.line_width = AgELineWidth.e3
        elevation.user_text_visible = True
        elevation.user_text = "My new elevation"

        # Set contours to visible on scenario
        voContours.is_visible = True
        voContours.fill = True
        voContours.fill_translucency = 80.0

    # endregion

    # region ConfigureVehicleGfxVOSunLighting
    def test_ConfigureVehicleGfxVOSunLighting(self):
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        self.ConfigureVehicleGfxVOSunLighting(sat.graphics.lighting)
        (clr.Convert(sat, IStkObject)).unload()

    def ConfigureVehicleGfxVOSunLighting(self, lighting: "IVehicleGfxLighting"):
        sunlight: "IVehicleGfxLightingElement" = lighting.sunlight

        sunlight.visible = True
        sunlight.color = Color.Red
        sunlight.line_style = AgELineStyle.eDotted
        sunlight.line_width = AgELineWidth.e3
        sunlight.marker_style = "Circle"

    # endregion
