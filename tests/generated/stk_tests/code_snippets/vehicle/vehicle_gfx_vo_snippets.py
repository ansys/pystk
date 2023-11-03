from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


@category("Graphics Tests")
class VehicleGfxVOSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(VehicleGfxVOSnippets, self).__init__(*args, **kwargs)

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
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        self.SetVehicleGfxToCustomIntervals(gv.graphics)
        (clr.Convert(gv, IStkObject)).unload()

    def SetVehicleGfxToCustomIntervals(self, graphics: "IGreatArcGraphics"):
        if graphics.is_attributes_type_supported(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM):
            # Set graphics to custom
            graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM)

            # Get VehicleGraphics2DAttributesCustom interface
            customAttributes: "VehicleGraphics2DAttributesCustom" = clr.CastAs(
                graphics.attributes, VehicleGraphics2DAttributesCustom
            )

    # endregion

    # region ConfigureVehicleGfxCustomIntervals
    def test_ConfigureVehicleGfxCustomIntervals(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        gv.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_CUSTOM)
        customAttributes: "VehicleGraphics2DAttributesCustom" = clr.CastAs(
            gv.graphics.attributes, VehicleGraphics2DAttributesCustom
        )
        self.ConfigureVehicleGfxCustomIntervals(customAttributes)
        (clr.Convert(gv, IStkObject)).unload()

    def ConfigureVehicleGfxCustomIntervals(self, customAttributes: "VehicleGraphics2DAttributesCustom"):
        customIntervals: "VehicleGraphics2DIntervalsCollection" = customAttributes.intervals

        # Add intervals
        customIntervals.add("1 Jan 2012 12:00:00.000", "1 Jan 2012 14:00:00.000")
        customIntervals.add("2 Jan 2012 01:00:00.000", "2 Jan 2012 02:00:00.000")

        # Deconflict intervals if necessary
        customAttributes.deconflict()

    # endregion

    # region SetVehicleGfxToBasic
    def test_SetVehicleGfxToBasic(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        self.SetVehicleGfxToBasic(gv.graphics)
        (clr.Convert(gv, IStkObject)).unload()

    def SetVehicleGfxToBasic(self, graphics: "IGreatArcGraphics"):
        if graphics.is_attributes_type_supported(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC):
            # Set graphics to basic
            graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)

            # Get IVehicleGraphics2DAttributesBasic interface
            basicAttributes: "IVehicleGraphics2DAttributesBasic" = clr.CastAs(
                graphics.attributes, IVehicleGraphics2DAttributesBasic
            )

    # endregion

    # region ConfigureVehicleGfxBasic
    def test_ConfigureVehicleGfxBasic(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        gv.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)
        basicAttributes: "IVehicleGraphics2DAttributesBasic" = clr.CastAs(
            gv.graphics.attributes, IVehicleGraphics2DAttributesBasic
        )
        self.ConfigureVehicleGfxBasic(basicAttributes)
        (clr.Convert(gv, IStkObject)).unload()

    def ConfigureVehicleGfxBasic(self, basicAttributes: "IVehicleGraphics2DAttributesBasic"):
        # Change display
        basicAttributes.is_visible = True
        basicAttributes.color = Color.Red
        basicAttributes.line.style = LINE_STYLE.DOTTED
        basicAttributes.line.width = LINE_WIDTH.WIDTH3
        basicAttributes.marker_style = "Square"

    # endregion

    # region SetVehicleGfxToAccessIntervals
    def test_SetVehicleGfxToAccessIntervals(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        sat: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), Satellite
        )
        self.SetVehicleGfxToAccessIntervals(gv.graphics)
        (clr.Convert(sat, IStkObject)).unload()
        (clr.Convert(gv, IStkObject)).unload()

    def SetVehicleGfxToAccessIntervals(self, graphics: "IGreatArcGraphics"):
        if graphics.is_attributes_type_supported(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS):
            # Set graphics to access intervals
            graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS)

            # Get VehicleGraphics2DAttributesAccess interface
            accessAttributes: "VehicleGraphics2DAttributesAccess" = clr.CastAs(
                graphics.attributes, VehicleGraphics2DAttributesAccess
            )

    # endregion

    # region ConfigureVehicleGfxAccessIntervals
    def test_ConfigureVehicleGfxAccessIntervals(self):
        gv: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )
        sat: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), Satellite
        )
        gv.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_ACCESS)
        accessAttributes: "VehicleGraphics2DAttributesAccess" = clr.CastAs(
            gv.graphics.attributes, VehicleGraphics2DAttributesAccess
        )
        self.ConfigureVehicleGfxAccessIntervals(accessAttributes)
        (clr.Convert(sat, IStkObject)).unload()
        (clr.Convert(gv, IStkObject)).unload()

    def ConfigureVehicleGfxAccessIntervals(self, accessAttributes: "VehicleGraphics2DAttributesAccess"):
        accessAttributes.access_objects.add("Satellite/sat1")

        accessAttributes.during_access.is_visible = True
        accessAttributes.during_access.color = Color.Yellow
        accessAttributes.no_access.is_visible = True
        accessAttributes.no_access.color = Color.Red

    # endregion

    # region ConfigureVehicleGfxVOElevationContours
    def test_ConfigureVehicleGfxVOElevationContours(self):
        sat: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), Satellite
        )

        self.ConfigureVehicleGfxVOElevationContours(sat.graphics.elev_contours, sat.graphics_3d.elev_contours)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")

    def ConfigureVehicleGfxVOElevationContours(
        self, gfxContours: "VehicleGraphics2DElevContours", voContours: "VehicleGraphics3DElevContours"
    ):
        gfxContours.is_visible = True
        gfxContours.is_fill_visible = True
        gfxContours.fill_style = FILL_STYLE.HORIZONTAL_STRIPE
        gfxContours.num_of_decimal_digits = 5

        # Add contour elevation level
        elevation: "VehicleGraphics2DElevationsElement" = gfxContours.elevations.add_level(25.0)

        # Configure contour elevation element
        elevation.color = Color.Red
        elevation.distance_visible = True
        elevation.line_style = LINE_STYLE.DOTTED
        elevation.line_width = LINE_WIDTH.WIDTH3
        elevation.user_text_visible = True
        elevation.user_text = "My new elevation"

        # Set contours to visible on scenario
        voContours.is_visible = True
        voContours.fill = True
        voContours.fill_translucency = 80.0

    # endregion

    # region ConfigureVehicleGfxVOSunLighting
    def test_ConfigureVehicleGfxVOSunLighting(self):
        sat: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), Satellite
        )
        self.ConfigureVehicleGfxVOSunLighting(sat.graphics.lighting)
        (clr.Convert(sat, IStkObject)).unload()

    def ConfigureVehicleGfxVOSunLighting(self, lighting: "VehicleGraphics2DLighting"):
        sunlight: "VehicleGraphics2DLightingElement" = lighting.sunlight

        sunlight.visible = True
        sunlight.color = Color.Red
        sunlight.line_style = LINE_STYLE.DOTTED
        sunlight.line_width = LINE_WIDTH.WIDTH3
        sunlight.marker_style = "Circle"

    # endregion
