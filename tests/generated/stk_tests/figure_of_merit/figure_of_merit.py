from test_util import *
from assertion_harness import *
from fom_helper import *
from interfaces.stk_objects import *
from logger import *
from pytest import *
from ansys.stk.core.stkobjects import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("FigureOfMeritTests", "FigureOfMeritTests.sc"))
            EarlyBoundTests.AG_COV = clr.Convert(
                TestBase.Application.current_scenario.children.new(
                    STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CoverageDefinition1"
                ),
                ICoverageDefinition,
            )
            EarlyBoundTests.AG_FOM = clr.Convert(
                (clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)).children.new(
                    STK_OBJECT_TYPE.FIGURE_OF_MERIT, "FigureOfMerit1"
                ),
                IFigureOfMerit,
            )

        except Exception as e:
            raise e

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_FOM = None
        EarlyBoundTests.AG_COV = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_FOM: "IFigureOfMerit" = None
    AG_COV: "ICoverageDefinition" = None
    # endregion

    # region Basic
    @category("Basic Tests")
    def test_Basic(self):
        helper = FOMHelper(TestBase.Application)

        TestBase.logger.WriteLine("----- BASIC TEST ----- BEGIN -----")
        # DefinitionType
        TestBase.logger.WriteLine6("\tThe current DefinitionType is: {0}", EarlyBoundTests.AG_FOM.definition_type)
        # DefinitionSupportedTypes
        arTypes = EarlyBoundTests.AG_FOM.definition_supported_types
        TestBase.logger.WriteLine3("\tThe FigureOfMerit supports: {0} definition types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "FIGURE_OF_MERIT_DEFINITION_TYPE" = clr.Convert(
                int(arTypes[iIndex][0]), FIGURE_OF_MERIT_DEFINITION_TYPE
            )
            if not EarlyBoundTests.AG_FOM.is_definition_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            if eType == FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_CONSTRAINT:
                fdac: "IFigureOfMeritDefinitionAccessConstraint" = None

                # SetAccessConstraintDefinition
                fdac = EarlyBoundTests.AG_FOM.set_access_constraint_definition(
                    FIGURE_OF_MERIT_CONSTRAINT_NAME.AZIMUTH_RATE
                )
                Assert.assertIsNotNone(fdac)

                # SetAccessConstraintDefinitionName
                fdac = EarlyBoundTests.AG_FOM.set_access_constraint_definition_name("AzimuthRate")
                Assert.assertIsNotNone(fdac)

            elif eType == FIGURE_OF_MERIT_DEFINITION_TYPE.SCALAR_CALCULATION:
                defScalarCalc: "IFigureOfMeritDefinitionScalarCalculation" = None

                # SetScalarCalculationDefinition
                defScalarCalc = EarlyBoundTests.AG_FOM.set_scalar_calculation_definition(
                    "Satellite/Satellite1 ElapsedTimeFromStop"
                )
                Assert.assertIsNotNone(defScalarCalc)

            else:
                # SetDefinitionType
                EarlyBoundTests.AG_FOM.set_definition_type(eType)

            TestBase.logger.WriteLine6("\t\tThe new DefinitionType is: {0}", EarlyBoundTests.AG_FOM.definition_type)
            eType2: "FIGURE_OF_MERIT_DEFINITION_TYPE" = EarlyBoundTests.AG_FOM.definition_type
            Assert.assertEqual(eType, eType2)
            # Definition
            helper.Definition(EarlyBoundTests.AG_FOM.definition, eType, EarlyBoundTests.AG_COV.asset_list)

            iIndex += 1

        TestBase.logger.WriteLine("----- BASIC TEST ----- END -----")

    # endregion

    # region BUG72717
    @category("Graphics Tests")
    def test_BUG72717(self):
        gfx: "IFigureOfMeritGraphics" = EarlyBoundTests.AG_FOM.graphics
        gfxAnim: "IFigureOfMeritGraphics2DAttributesAnimation" = gfx.animation
        gfxStatic: "IFigureOfMeritGraphics2DAttributes" = gfx.static

        # Hold original values
        holdHideAll: bool = gfx.is_object_graphics_visible
        holdAnimationIsVisible: bool = gfxAnim.is_visible
        holdStaticIsVisible: bool = gfxStatic.is_visible

        # The "Show" properties can be set, regardless of the "Hide All" property (for backward compatibility)
        gfx.is_object_graphics_visible = True
        Assert.assertTrue(gfx.is_object_graphics_visible)
        gfxAnim.is_visible = True
        Assert.assertTrue(gfxAnim.is_visible)
        gfxAnim.is_visible = False
        Assert.assertFalse(gfxAnim.is_visible)
        gfxStatic.is_visible = True
        Assert.assertTrue(gfxStatic.is_visible)
        gfxStatic.is_visible = False
        Assert.assertFalse(gfxStatic.is_visible)

        gfx.is_object_graphics_visible = False
        Assert.assertFalse(gfx.is_object_graphics_visible)
        gfxAnim.is_visible = True
        Assert.assertTrue(gfxAnim.is_visible)
        gfxAnim.is_visible = False
        Assert.assertFalse(gfxAnim.is_visible)
        gfxStatic.is_visible = True
        Assert.assertTrue(gfxStatic.is_visible)
        gfxStatic.is_visible = False
        Assert.assertFalse(gfxStatic.is_visible)

        # Setting either of the "Show" properties to true should reset the "Hide All" property
        gfx.is_object_graphics_visible = False
        gfxAnim.is_visible = True
        Assert.assertTrue(gfx.is_object_graphics_visible)  # value changed

        gfx.is_object_graphics_visible = False
        gfxStatic.is_visible = True
        Assert.assertTrue(gfx.is_object_graphics_visible)  # value changed

        # When "Hide All" is set to false, the "Show" properties should return false.
        gfxAnim.is_visible = True
        gfx.is_object_graphics_visible = False
        Assert.assertFalse(gfxAnim.is_visible)  # value changed

        gfxStatic.is_visible = True
        gfx.is_object_graphics_visible = False
        Assert.assertFalse(gfxStatic.is_visible)  # value changed

        # Restore original values
        gfx.is_object_graphics_visible = holdHideAll
        gfxAnim.is_visible = holdAnimationIsVisible
        gfxStatic.is_visible = holdStaticIsVisible

    # endregion

    # region DefinitionTypes
    def test_DefinitionTypes(self):
        defType: "FIGURE_OF_MERIT_DEFINITION_TYPE"
        for defType in Enum.GetValues(clr.TypeOf(FIGURE_OF_MERIT_DEFINITION_TYPE)):
            if EarlyBoundTests.AG_FOM.is_definition_type_supported(defType):
                if defType == FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_CONSTRAINT:
                    EarlyBoundTests.AG_FOM.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.ALTITUDE)
                    Assert.assertEqual(
                        FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_CONSTRAINT, EarlyBoundTests.AG_FOM.definition_type
                    )

                elif defType == FIGURE_OF_MERIT_DEFINITION_TYPE.SCALAR_CALCULATION:
                    EarlyBoundTests.AG_FOM.set_scalar_calculation_definition("CentralBody/Earth ElapsedTimeFromStart")
                    Assert.assertEqual(
                        FIGURE_OF_MERIT_DEFINITION_TYPE.SCALAR_CALCULATION, EarlyBoundTests.AG_FOM.definition_type
                    )

                else:
                    EarlyBoundTests.AG_FOM.set_definition_type(defType)
                    Assert.assertEqual(defType, EarlyBoundTests.AG_FOM.definition_type)

            else:
                Assert.fail("FOM DefinitionType not supported.")

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        oHelper = STKObjectHelper()
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_FOM, IStkObject))
        oHelper.TestObjectFilesArray((clr.Convert(EarlyBoundTests.AG_FOM, IStkObject)).object_files)

    # endregion

    # region GridInspector
    @category("Basic Tests")
    @category("Grid Inspector")
    def test_GridInspector(self):
        TestBase.logger.WriteLine("----- GRID INSPECTOR TEST ----- BEGIN -----")
        oSatellite: "ISatellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat2"), ISatellite
        )
        Assert.assertIsNotNone(oSatellite)
        oPropagator: "IVehiclePropagatorTwoBody" = clr.Convert(oSatellite.propagator, IVehiclePropagatorTwoBody)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.propagate()

        # BoundsType (eBoundsLat)
        TestBase.logger.WriteLine6("\tThe current BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        EarlyBoundTests.AG_COV.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_LAT, EarlyBoundTests.AG_COV.grid.bounds_type)
        # Bounds
        lat: "ICoverageBoundsLat" = clr.Convert(EarlyBoundTests.AG_COV.grid.bounds, ICoverageBoundsLat)
        Assert.assertIsNotNone(lat)
        TestBase.logger.WriteLine7(
            "\t\tThe current Bounds is: MinLatitude = {0}, MaxLatitude = {1}", lat.min_latitude, lat.max_latitude
        )
        lat.min_latitude = -15
        lat.max_latitude = 15
        TestBase.logger.WriteLine7(
            "\t\tThe new Bounds is: MinLatitude = {0}, MaxLatitude = {1}", lat.min_latitude, lat.max_latitude
        )
        Assert.assertAlmostEqual(-15, float(lat.min_latitude), delta=0.001)
        Assert.assertAlmostEqual(15, float(lat.max_latitude), delta=0.001)

        # AssetList.Add
        EarlyBoundTests.AG_COV.asset_list.remove_all()
        assetListElement: "ICoverageAssetListElement" = EarlyBoundTests.AG_COV.asset_list.add("Satellite/sat2")
        Assert.assertIsNotNone(assetListElement)
        # AssetStatus (eActive)
        TestBase.logger.WriteLine6("\tThe current AssetStatus is: {0}", assetListElement.asset_status)
        assetListElement.asset_status = COVERAGE_ASSET_STATUS.ACTIVE
        TestBase.logger.WriteLine6("\tThe new AssetStatus is: {0}", assetListElement.asset_status)
        Assert.assertEqual(COVERAGE_ASSET_STATUS.ACTIVE, assetListElement.asset_status)

        # SetDefinitionType (eFmNAssetCoverage)
        TestBase.logger.WriteLine6("\tThe current DefinitionType is: {0}", EarlyBoundTests.AG_FOM.definition_type)
        EarlyBoundTests.AG_FOM.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.N_ASSET_COVERAGE)
        TestBase.logger.WriteLine6("\tThe new DefinitionType is: {0}", EarlyBoundTests.AG_FOM.definition_type)
        # Definition
        oDefinition: "IFigureOfMeritDefinition" = EarlyBoundTests.AG_FOM.definition
        Assert.assertIsNotNone(oDefinition)
        # EnableSatisfaction
        TestBase.logger.WriteLine4(
            "\tThe current EnableSatisfaction is: {0}", oDefinition.satisfaction.enable_satisfaction
        )
        oDefinition.satisfaction.enable_satisfaction = True
        TestBase.logger.WriteLine4("\tThe new EnableSatisfaction is: {0}", oDefinition.satisfaction.enable_satisfaction)
        Assert.assertTrue(oDefinition.satisfaction.enable_satisfaction)

        # ComputeAccesses
        EarlyBoundTests.AG_COV.compute_accesses()
        # GridInspector
        oInspector: "IFigureOfMeritGridInspector" = EarlyBoundTests.AG_FOM.grid_inspector
        Assert.assertIsNotNone(oInspector)
        # SelectPoint
        oInspector.select_point(0, 0)
        # Message
        TestBase.logger.WriteLine5("\tThe SelectPoint message:\n{0}", oInspector.message)
        with pytest.raises(Exception):
            oInspector.select_point("one", 0)
        with pytest.raises(Exception):
            oInspector.select_point(-12, "two")
        # PointFOM
        oTimeVar: "IDataProviderTimeVarying" = clr.Convert(oInspector.point_figure_of_merit, IDataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.exec_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointFOM result:")
        oResult.Dump()
        # PointSatisfaction
        oInterval: "IDataProviderInterval" = clr.Convert(oInspector.point_satisfaction, IDataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointSatisfaction result:")
        oResult.Dump()
        # SelectRegion
        with pytest.raises(Exception):
            oInspector.select_region("AreaTarget1")
        # RegionFOM
        oTimeVar = clr.Convert(oInspector.region_figure_of_merit, IDataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.exec_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionFOM result:")
        oResult.Dump()
        # RegionSatisfaction
        oInterval = clr.Convert(oInspector.region_satisfaction, IDataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionSatisfaction result:")
        oResult.Dump()
        # ClearSelection
        oInspector.clear_selection()
        TestBase.logger.WriteLine5("\n\tThe ClearSelection message:{0}", oInspector.message)
        Assert.assertEqual("", oInspector.message)

        # BoundsType (eBoundsCustomRegions)
        EarlyBoundTests.AG_COV.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        Assert.assertEqual(COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS, EarlyBoundTests.AG_COV.grid.bounds_type)
        # Bounds
        oCustom: "ICoverageBoundsCustomRegions" = clr.Convert(
            EarlyBoundTests.AG_COV.grid.bounds, ICoverageBoundsCustomRegions
        )
        Assert.assertIsNotNone(oCustom)
        oCustom.area_targets.add("AreaTarget/AreaTarget1")

        # SelectRegion
        oInspector.select_region("AreaTarget1")
        # Message
        TestBase.logger.WriteLine5("\tThe SelectRegion message:\n{0}", oInspector.message)
        with pytest.raises(Exception):
            oInspector.select_region("Invalid.Region")
        # PointFOM
        oTimeVar = clr.Convert(oInspector.point_figure_of_merit, IDataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.exec_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointFOM result:")
        oResult.Dump()
        # PointSatisfaction
        oInterval = clr.Convert(oInspector.point_satisfaction, IDataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointSatisfaction result:")
        oResult.Dump()
        # RegionFOM
        oTimeVar = clr.Convert(oInspector.region_figure_of_merit, IDataProviderTimeVarying)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.exec_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionFOM result:")
        oResult.Dump()
        # RegionSatisfaction
        oInterval = clr.Convert(oInspector.region_satisfaction, IDataProviderInterval)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.exec("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionSatisfaction result:")
        oResult.Dump()
        # ClearSelection
        oInspector.clear_selection()
        TestBase.logger.WriteLine5("\n\tThe ClearSelection message:{0}", oInspector.message)
        Assert.assertEqual("", oInspector.message)
        # ClearAccesses
        EarlyBoundTests.AG_COV.clear_accesses()
        # Unload (eSatellite)
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat2")
        TestBase.logger.WriteLine("----- GRID INSPECTOR TEST ----- END -----")

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- BEGIN -----")
        # Graphics
        oGraphics: "IFigureOfMeritGraphics" = EarlyBoundTests.AG_FOM.graphics
        Assert.assertIsNotNone(oGraphics)

        # IsObjectGraphicsVisible
        oGraphics.is_object_graphics_visible = False
        Assert.assertFalse(oGraphics.is_object_graphics_visible)
        oGraphics.is_object_graphics_visible = True
        Assert.assertTrue(oGraphics.is_object_graphics_visible)

        helper = FOMHelper(TestBase.Application)
        # Static
        helper.GfxAttributes(oGraphics.static, False)
        # Contours (readonly)
        EarlyBoundTests.AG_FOM.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_SEPARATION)
        Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_SEPARATION, EarlyBoundTests.AG_FOM.definition_type)
        helper.GfxContours(oGraphics.static.contours, True, True)
        helper.GfxContourLines(oGraphics.static.contours, True)
        # Contours
        EarlyBoundTests.AG_FOM.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.TIME_AVERAGE_GAP)
        Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.TIME_AVERAGE_GAP, EarlyBoundTests.AG_FOM.definition_type)
        helper.GfxContours(oGraphics.static.contours, False, False)
        oldFillPoints: bool = oGraphics.static.fill_points
        oGraphics.static.fill_points = True
        helper.GfxContourLines(oGraphics.static.contours, False)
        oGraphics.static.fill_points = oldFillPoints

        # Animation (readonly)
        helper.GfxAnimationAttributes(oGraphics.animation, True)
        # Animation
        EarlyBoundTests.AG_FOM.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.SIMPLE_COVERAGE)
        Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.SIMPLE_COVERAGE, EarlyBoundTests.AG_FOM.definition_type)
        helper.GfxAnimationAttributes(oGraphics.animation, False)
        # Contours (readonly)
        helper.GfxAnimationContours(oGraphics.animation.contours, True, True)
        helper.GfxContourLines(oGraphics.animation.contours, True)
        # Contours
        EarlyBoundTests.AG_FOM.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.REVISIT_TIME)
        Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.REVISIT_TIME, EarlyBoundTests.AG_FOM.definition_type)
        EarlyBoundTests.AG_FOM.graphics.animation.contours.is_visible = True
        helper.GfxAnimationContours(oGraphics.animation.contours, False, False)
        helper.GfxContourLines(oGraphics.animation.contours, False)
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- VO TEST ----- BEGIN -----")
        # VO
        oVO: "IFigureOfMeritGraphics3D" = EarlyBoundTests.AG_FOM.graphics_3d
        Assert.assertIsNotNone(oVO)

        # Granularity
        TestBase.logger.WriteLine6("\tThe current Granularity is: {0}", oVO.granularity)
        oVO.granularity = 1.23
        TestBase.logger.WriteLine6("\tThe new Granularity is: {0}", oVO.granularity)
        Assert.assertEqual(1.23, oVO.granularity)
        with pytest.raises(Exception):
            oVO.granularity = 12.3
        # PixelsPerDeg
        TestBase.logger.WriteLine6("\tThe current PixelsPerDeg is: {0}", oVO.pixels_per_deg)
        oVO.pixels_per_deg = 12.3
        TestBase.logger.WriteLine6("\tThe new PixelsPerDeg is: {0}", oVO.pixels_per_deg)
        Assert.assertEqual(12.3, oVO.pixels_per_deg)
        with pytest.raises(Exception):
            oVO.pixels_per_deg = -12.3

        # Static
        self.VOAttributes(oVO.static, False)
        # Animation (readonly)
        EarlyBoundTests.AG_FOM.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.TIME_AVERAGE_GAP)
        Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.TIME_AVERAGE_GAP, EarlyBoundTests.AG_FOM.definition_type)
        self.VOAttributes(oVO.animation, True)
        # Animation
        EarlyBoundTests.AG_FOM.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.SIMPLE_COVERAGE)
        Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.SIMPLE_COVERAGE, EarlyBoundTests.AG_FOM.definition_type)
        self.VOAttributes(oVO.animation, False)
        TestBase.logger.WriteLine("----- VO TEST ----- END -----")

    # endregion

    # region VOAttributes
    def VOAttributes(self, oAttributes: "IFigureOfMeritGraphics3DAttributes", bReadOnly: bool):
        TestBase.logger.WriteLine4("----- VO ATTRIBUTES TEST (ReadOnly = {0})----- BEGIN -----", bReadOnly)
        Assert.assertIsNotNone(oAttributes)
        if bReadOnly:
            #  (readonly)
            with pytest.raises(Exception):
                oAttributes.is_visible = True
            # PointSize (readonly)
            with pytest.raises(Exception):
                oAttributes.point_size = 5.6
            # Translucency (readonly)
            with pytest.raises(Exception):
                oAttributes.translucency = 56.78

        else:
            # IsVisible (false)
            TestBase.logger.WriteLine4("\tThe current IsVisible is: {0}", oAttributes.is_visible)
            oAttributes.is_visible = False
            TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.is_visible)
            Assert.assertFalse(oAttributes.is_visible)
            # PointSize (readonly)
            with pytest.raises(Exception):
                oAttributes.point_size = 5.6
            # Translucency (readonly)
            with pytest.raises(Exception):
                oAttributes.translucency = 56.78
            # IsVisible (true)
            oAttributes.is_visible = True
            TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.is_visible)
            Assert.assertTrue(oAttributes.is_visible)
            # PointSize
            TestBase.logger.WriteLine6("\tThe current PointSize is: {0}", oAttributes.point_size)
            oAttributes.point_size = 5.6
            TestBase.logger.WriteLine6("\tThe new PointSize is: {0}", oAttributes.point_size)
            Assert.assertEqual(5.6, oAttributes.point_size)
            with pytest.raises(Exception):
                oAttributes.point_size = 12.3
            # Translucency
            TestBase.logger.WriteLine6("\tThe current Translucency is: {0}", oAttributes.translucency)
            oAttributes.translucency = 56.78
            TestBase.logger.WriteLine6("\tThe new Translucency is: {0}", oAttributes.translucency)
            Assert.assertAlmostEqual(56.78, oAttributes.translucency, delta=0.001)
            with pytest.raises(Exception):
                oAttributes.translucency = 123

        TestBase.logger.WriteLine("----- VO ATTRIBUTES TEST ----- END -----")

    # endregion

    # region GfxSmoothContours
    @category("Graphics Tests")
    def test_GfxSmoothContours(self):
        TestBase.logger.WriteLine("----- GRAPHICS SMOOTH CONTOURS ----- BEGIN -----")
        oCovDef: "ICoverageDefinition" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CovDef_012341212"),
            ICoverageDefinition,
        )
        Assert.assertIsNotNone(oCovDef)

        oFOMerit: "IFigureOfMerit" = clr.CastAs(
            (clr.Convert(oCovDef, IStkObject)).children.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, "FOM_2352353"),
            IFigureOfMerit,
        )
        Assert.assertIsNotNone(oFOMerit)

        try:
            TestBase.logger.WriteLine6("\tThe current BoundsType is: {0}", oCovDef.grid.bounds_type)
            noSmoothFillBounds: "COVERAGE_BOUNDS[]" = [COVERAGE_BOUNDS.BOUNDS_CUSTOM_BOUNDARY]
            eBound: "COVERAGE_BOUNDS"
            for eBound in noSmoothFillBounds:
                oCovDef.grid.bounds_type = eBound
                TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oCovDef.grid.bounds_type)
                eBound2: "COVERAGE_BOUNDS" = oCovDef.grid.bounds_type
                Assert.assertEqual(eBound, eBound2)
                self.TestFOMGfxContours(oFOMerit, False)

            SmoothFillBounds: "COVERAGE_BOUNDS[]" = [
                COVERAGE_BOUNDS.BOUNDS_LAT_LINE,
                COVERAGE_BOUNDS.BOUNDS_LON_LINE,
                COVERAGE_BOUNDS.BOUNDS_CUSTOM_REGIONS,
                COVERAGE_BOUNDS.BOUNDS_GLOBAL,
                COVERAGE_BOUNDS.BOUNDS_LAT,
            ]
            eBound: "COVERAGE_BOUNDS"
            for eBound in SmoothFillBounds:
                oCovDef.grid.bounds_type = eBound
                TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oCovDef.grid.bounds_type)
                eBound2: "COVERAGE_BOUNDS" = oCovDef.grid.bounds_type
                Assert.assertEqual(eBound, eBound2)
                self.TestFOMGfxContours(oFOMerit, True)

        finally:
            (clr.Convert(oCovDef, IStkObject)).children.unload(
                (clr.Convert(oFOMerit, IStkObject)).class_type, (clr.Convert(oFOMerit, IStkObject)).instance_name
            )
            TestBase.Application.current_scenario.children.unload(
                (clr.Convert(oCovDef, IStkObject)).class_type, (clr.Convert(oCovDef, IStkObject)).instance_name
            )

        TestBase.logger.WriteLine("----- GRAPHICS SMOOTH CONTOURS ----- END -----")

    # endregion

    # region TestFOMGfxContours
    def TestFOMGfxContours(self, fom: "IFigureOfMerit", bIsSmoothFillSupported: bool):
        # SetDefinitionType (eFmAccessDuration)
        TestBase.logger.WriteLine6("\t\tThe current DefinitionType is: {0}", fom.definition_type)
        fom.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_DURATION)
        TestBase.logger.WriteLine6("\t\tThe new DefinitionType is: {0}", fom.definition_type)
        Assert.assertEqual(FIGURE_OF_MERIT_DEFINITION_TYPE.ACCESS_DURATION, fom.definition_type)
        # Graphics.Static.IsVisible
        TestBase.logger.WriteLine4("\t\tThe current Graphics.Static.IsVisible is: {0}", fom.graphics.static.is_visible)
        fom.graphics.static.is_visible = True
        TestBase.logger.WriteLine4("\t\tThe new Graphics.Static.IsVisible is: {0}", fom.graphics.static.is_visible)
        Assert.assertTrue(fom.graphics.static.is_visible)
        # Graphics.Static.Contours.IsVisible
        TestBase.logger.WriteLine4(
            "\t\tThe current Graphics.Static.Contours.IsVisible is: {0}", fom.graphics.static.contours.is_visible
        )
        fom.graphics.static.contours.is_visible = True
        TestBase.logger.WriteLine4(
            "\t\tThe new Graphics.Static.Contours.IsVisible is: {0}", fom.graphics.static.contours.is_visible
        )
        Assert.assertTrue(fom.graphics.static.contours.is_visible)
        # Graphics.Static.Contours.ContourType
        TestBase.logger.WriteLine6(
            "\t\tThe current Graphics.Static.Contours.ContourType is: {0}", fom.graphics.static.contours.contour_type
        )
        if not bIsSmoothFillSupported:
            with pytest.raises(Exception):
                fom.graphics.static.contours.contour_type = FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.SMOOTH_FILL

        else:
            fom.graphics.static.contours.contour_type = FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.SMOOTH_FILL
            TestBase.logger.WriteLine6(
                "\t\tThe new Graphics.Static.Contours.ContourType is: {0}", fom.graphics.static.contours.contour_type
            )
            Assert.assertEqual(
                FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE.SMOOTH_FILL, fom.graphics.static.contours.contour_type
            )

    # endregion

    # region NonLinearContourLevels
    @category("NonLinearContourLevels Tests")
    def test_NonLinearContourLevels(self):
        # See 44875 and 45060

        TestBase.logger.WriteLine("-----  NON LINEAR CONTOUR LEVELS ----- BEGIN -----")

        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Bug44875")

        # create facility
        facobj: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.FACILITY, "Fac1Bug44875"
        )
        recobj: "IStkObject" = facobj.children.new(STK_OBJECT_TYPE.RECEIVER, "Rcv1Bug44875")

        # Create cov def
        covdefobj: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CD1Bug44875"
        )
        covdef: "ICoverageDefinition" = clr.CastAs(covdefobj, ICoverageDefinition)
        covdef.point_definition.use_grid_seed = True
        covdef.point_definition.use_object_as_seed = True
        covdef.point_definition.grid_class = COVERAGE_GRID_CLASS.GRID_CLASS_RECEIVER
        covdef.point_definition.seed_instance = "Facility/Fac1Bug44875/Receiver/Rcv1Bug44875"
        covchilds: "IStkObjectCollection" = covdefobj.children

        fomobj1: "IStkObject" = covchilds.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, "FM1Bug44875")
        fom1: "IFigureOfMerit" = clr.CastAs(fomobj1, IFigureOfMerit)
        fomcs1: "IFigureOfMeritDefinitionAccessConstraint" = None
        fomcs1 = fom1.set_access_constraint_definition_name("C/No")
        if not TestBase.NoGraphicsMode:
            fomc1: "IFigureOfMeritGraphics2DContours" = fom1.graphics.static.contours
            fomc1.is_visible = True
            col1: "IFigureOfMeritGraphics2DLevelAttributesCollection" = fomc1.level_attributes
            unit1a: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("RatioUnit")
            unit2a: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("BandwidthUnit")
            TestBase.Application.unit_preferences.set_current_unit("RatioUnit", "dB")
            TestBase.Application.unit_preferences.set_current_unit("BandwidthUnit", "MHz")
            col1.add_level_range(-100, 0, 10)
            Assert.assertEqual(11, col1.count)
            TestBase.logger.WriteLine(("unit1a = " + unit1a))
            TestBase.logger.WriteLine(("unit2a = " + unit2a))
            TestBase.Application.unit_preferences.set_current_unit("RatioUnit", unit1a)
            TestBase.Application.unit_preferences.set_current_unit("BandwidthUnit", unit2a)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                fomc1: "IFigureOfMeritGraphics2DContours" = fom1.graphics.static.contours

        fomobj2: "IStkObject" = covchilds.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, "FM2Bug44875")
        fom2: "IFigureOfMerit" = clr.CastAs(fomobj2, IFigureOfMerit)
        fomcs2: "IFigureOfMeritDefinitionAccessConstraint" = None
        fomcs2 = fom2.set_access_constraint_definition_name("PowerFluxDensity")
        if not TestBase.NoGraphicsMode:
            fomc2: "IFigureOfMeritGraphics2DContours" = fom2.graphics.static.contours
            fomc2.is_visible = True
            col2: "IFigureOfMeritGraphics2DLevelAttributesCollection" = fomc2.level_attributes
            unit1b: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("Power")
            unit2b: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("SmallDistance")
            TestBase.Application.unit_preferences.set_current_unit("Power", "GW")
            TestBase.Application.unit_preferences.set_current_unit("SmallDistance", "ft")
            col2.add_level_range(0.1, 100, 10)
            Assert.assertEqual(10, col2.count)
            TestBase.logger.WriteLine(("unit1b = " + unit1b))
            TestBase.logger.WriteLine(("unit2b = " + unit2b))
            TestBase.Application.unit_preferences.set_current_unit("Power", unit1b)
            TestBase.Application.unit_preferences.set_current_unit("SmallDistance", unit2b)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                fomc2: "IFigureOfMeritGraphics2DContours" = fom2.graphics.static.contours

        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("FigureOfMeritTests", "FigureOfMeritTests.sc"))
        EarlyBoundTests.AG_COV = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CoverageDefinition1"
            ),
            ICoverageDefinition,
        )
        EarlyBoundTests.AG_FOM = clr.Convert(
            (clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)).children.new(
                STK_OBJECT_TYPE.FIGURE_OF_MERIT, "FigureOfMerit1"
            ),
            IFigureOfMerit,
        )
        TestBase.logger.WriteLine("-----  NON LINEAR CONTOUR LEVELS ----- END -----")

    # endregion

    # region AccessConstraintDefinitions
    @category("AccessConstraintDefinitions Tests")
    def test_AccessConstraintDefinitions(self):
        TestBase.logger.WriteLine("----- ACCESS CONSTRAINT DEFINITION ----- BEGIN -----")
        bugNum: str = "X45332"

        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario(bugNum)

        # create facility
        facobj: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.FACILITY, "Fac1X45332"
        )
        recobj: "IStkObject" = facobj.children.new(STK_OBJECT_TYPE.RECEIVER, ("Rcv1" + bugNum))

        # Create cov def
        covdefobj: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STK_OBJECT_TYPE.COVERAGE_DEFINITION, ("CD1" + bugNum)
        )
        covdef: "ICoverageDefinition" = clr.CastAs(covdefobj, ICoverageDefinition)
        covdef.point_definition.use_grid_seed = True
        covdef.point_definition.use_object_as_seed = True
        covdef.point_definition.grid_class = COVERAGE_GRID_CLASS.GRID_CLASS_RECEIVER
        covdef.point_definition.seed_instance = (("Facility/Fac1" + bugNum) + "/Receiver/Rcv1") + bugNum
        covchilds: "IStkObjectCollection" = covdefobj.children

        fomobj: "IStkObject" = covchilds.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, ("FM1" + bugNum))
        fom: "IFigureOfMerit" = clr.CastAs(fomobj, IFigureOfMerit)
        fomcs: "IFigureOfMeritDefinitionAccessConstraint" = None

        try:
            fomcs = fom.set_access_constraint_definition_name("LineOfSight")
            Assert.fail("'Not a constraint' access constraint not applicable for scenario setup")

        except Exception as e:
            msg: str = str(e)
            Assert.assertEqual("ConstraintName is not an available access constraint.", msg)
            TestBase.logger.WriteLine(("Expected exception: " + msg))

        try:
            fomcs = fom.set_access_constraint_definition_name("Not a constraint")
            Assert.fail("'Not a constraint' access constraint not applicable for scenario setup")

        except Exception as e:
            msg: str = str(e)
            Assert.assertEqual("ConstraintName is not an available access constraint.", msg)
            TestBase.logger.WriteLine(("Expected exception: " + msg))

        try:
            fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.LINE_OF_SIGHT)
            Assert.fail("Line of Sight access constraint not applicable for scenario setup")

        except Exception as e:
            msg: str = str(e)
            Assert.assertEqual("ConstraintName is not an available access constraint.", msg)
            TestBase.logger.WriteLine(("Expected exception: " + msg))

        try:
            fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.ACCESS_CONSTRAINT_PLUGIN)
            Assert.fail("Access Constraint Plugin access constraint not applicable for scenario setup")

        except Exception as e:
            msg: str = str(e)
            Assert.assertEqual(
                "eFmAccessConstraintPlugin not a valid parameter, use SetAccessConstraintDefintionName() with name of plugin.",
                msg,
            )
            TestBase.logger.WriteLine(("Expected exception: " + msg))

        # ===================================================================
        # Altitude
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.ALTITUDE)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.ALTITUDE, fomcs.constraint_name)
        Assert.assertEqual("Altitude", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("Altitude")
        Assert.assertEqual("Altitude", fomcs.constraint)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.ALTITUDE, fomcs.constraint_name)

        # ===================================================================
        # BER+I
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.BER_PLUS_I)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.BER_PLUS_I, fomcs.constraint_name)
        Assert.assertEqual("BER+I", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("BER+I")
        Assert.assertEqual("BER+I", fomcs.constraint)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.BER_PLUS_I, fomcs.constraint_name)

        # ===================================================================
        # C/No
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.OVER_NO)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.OVER_NO, fomcs.constraint_name)
        Assert.assertEqual("C/No", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("C/No")
        Assert.assertEqual("C/No", fomcs.constraint)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.OVER_NO, fomcs.constraint_name)

        # ===================================================================
        # J/S
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.J_OVER_S)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.J_OVER_S, fomcs.constraint_name)
        Assert.assertEqual("J/S", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("J/S")
        Assert.assertEqual("J/S", fomcs.constraint)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.J_OVER_S, fomcs.constraint_name)

        # ===================================================================
        # SrchTrkSinglePulseJOverS
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.SRCH_TRK_SINGLE_PULSE_J_OVER_S)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.SRCH_TRK_SINGLE_PULSE_J_OVER_S, fomcs.constraint_name)
        Assert.assertEqual("SrchTrkSinglePulseJOverS", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("SrchTrkSinglePulseJOverS")
        Assert.assertEqual("SrchTrkSinglePulseJOverS", fomcs.constraint)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.SRCH_TRK_SINGLE_PULSE_J_OVER_S, fomcs.constraint_name)

        # ===================================================================
        # CrdnCondition
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.CRDN_CONDITION)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.CRDN_CONDITION, fomcs.constraint_name)
        Assert.assertEqual("CrdnCondition", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FIGURE_OF_MERIT_CONSTRAINT_NAME.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("CrdnCondition")
        Assert.assertEqual("CrdnCondition", fomcs.constraint)
        Assert.assertEqual(FIGURE_OF_MERIT_CONSTRAINT_NAME.CRDN_CONDITION, fomcs.constraint_name)

        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("FigureOfMeritTests", "FigureOfMeritTests.sc"))
        EarlyBoundTests.AG_COV = clr.Convert(
            TestBase.Application.current_scenario.children.new(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CoverageDefinition1"
            ),
            ICoverageDefinition,
        )
        EarlyBoundTests.AG_FOM = clr.Convert(
            (clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)).children.new(
                STK_OBJECT_TYPE.FIGURE_OF_MERIT, "FigureOfMerit1"
            ),
            IFigureOfMerit,
        )
        TestBase.logger.WriteLine("-----  ACCESS CONSTRAINT DEFINITION ----- END -----")

    # endregion

    # ----------------------------------------------------------------

    # region DP_PreData_Unit
    def test_DP_PreData_Unit(self):
        holdDateFormat: str = TestBase.Application.unit_preferences.get_current_unit_abbrv("DateFormat")

        try:
            TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")

            coverageDefinitionObj: "IStkObject" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(
                    STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CoverageDefinitionPreDataTest"
                ),
                IStkObject,
            )
            coverageDefinition: "ICoverageDefinition" = clr.CastAs(coverageDefinitionObj, ICoverageDefinition)
            coverageDefinition.compute_accesses()
            figureOfMerit: "IFigureOfMerit" = clr.CastAs(
                coverageDefinitionObj.children.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, "FigureOfMeritPreDataTest"),
                IFigureOfMerit,
            )

            dp: "IDataProvider" = clr.CastAs(
                (clr.CastAs(figureOfMerit, IStkObject)).data_providers["Time Value By Point"], IDataProvider
            )
            dpFixed: "IDataProviderFixed" = clr.CastAs(dp, IDataProviderFixed)
            dp.pre_data = "90"
            result: "IDataProviderResult" = dpFixed.exec()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "Bogus"
            result = dpFixed.exec()
            Assert.assertEqual("Data Unavailable", str(result.message.messages[0]))

            satelliteObj: "IStkObject" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "SatellitePreDataTest"),
                IStkObject,
            )
            satellite: "ISatellite" = clr.CastAs(satelliteObj, ISatellite)
            satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
            satelliteProp: "IVehiclePropagatorTwoBody" = clr.CastAs(satellite.propagator, IVehiclePropagatorTwoBody)
            satelliteProp.propagate()
            attitudeCoverageObj: "IStkObject" = clr.CastAs(
                satelliteObj.children.new(STK_OBJECT_TYPE.ATTITUDE_COVERAGE, "AttitudeCoveragePreDataTest"), IStkObject
            )
            attitudeFigureOfMeritObj: "IStkObject" = clr.CastAs(
                attitudeCoverageObj.children.new(
                    STK_OBJECT_TYPE.ATTITUDE_FIGURE_OF_MERIT, "AttitudeFigureOfMeritPreDataTest"
                ),
                IStkObject,
            )
            TestBase.Application.execute_command((("AttCov " + attitudeCoverageObj.path) + " Access Compute"))

            dp: "IDataProvider" = clr.CastAs(
                attitudeFigureOfMeritObj.data_providers["Time Value By Point"], IDataProvider
            )
            dpFixed: "IDataProviderFixed" = clr.CastAs(dp, IDataProviderFixed)
            dp.pre_data = "90"
            TestBase.Application.execute_command((("AttCov " + attitudeCoverageObj.path) + " Access Compute"))
            result: "IDataProviderResult" = dpFixed.exec()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "Bogus"
            TestBase.Application.execute_command((("AttCov " + attitudeCoverageObj.path) + " Access Compute"))
            result = dpFixed.exec()
            Assert.assertEqual("Data Unavailable", str(result.message.messages[0]))

        finally:
            TestBase.Application.current_scenario.children.unload(
                STK_OBJECT_TYPE.COVERAGE_DEFINITION, "CoverageDefinitionPreDataTest"
            )
            TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "SatellitePreDataTest")
            TestBase.Application.unit_preferences.set_current_unit("DateFormat", holdDateFormat)

    # endregion
