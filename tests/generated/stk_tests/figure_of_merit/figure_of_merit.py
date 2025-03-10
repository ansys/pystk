# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from test_util import *
from assertion_harness import *
from fom_helper import *
from interfaces.stk_objects import *
from logger import *
from ansys.stk.core.stkobjects import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("FigureOfMeritTests", "FigureOfMeritTests.sc"))
            EarlyBoundTests.AG_COV = CoverageDefinition(
                TestBase.Application.current_scenario.children.new(
                    STKObjectType.COVERAGE_DEFINITION, "CoverageDefinition1"
                )
            )
            covObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)
            EarlyBoundTests.AG_FOM = FigureOfMerit(covObj.children.new(STKObjectType.FIGURE_OF_MERIT, "FigureOfMerit1"))

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
    AG_FOM: "FigureOfMerit" = None
    AG_COV: "CoverageDefinition" = None
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
            eType: "FigureOfMeritDefinitionType" = FigureOfMeritDefinitionType(int(arTypes[iIndex][0]))
            if not EarlyBoundTests.AG_FOM.is_definition_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            if eType == FigureOfMeritDefinitionType.ACCESS_CONSTRAINT:
                fdac: "FigureOfMeritDefinitionAccessConstraint" = None

                # SetAccessConstraintDefinition
                fdac = EarlyBoundTests.AG_FOM.set_access_constraint_definition(FigureOfMeritConstraintName.AZIMUTH_RATE)
                Assert.assertIsNotNone(fdac)

                # SetAccessConstraintDefinitionName
                fdac = EarlyBoundTests.AG_FOM.set_access_constraint_definition_name("AzimuthRate")
                Assert.assertIsNotNone(fdac)

            elif eType == FigureOfMeritDefinitionType.SCALAR_CALCULATION:
                defScalarCalc: "FigureOfMeritDefinitionScalarCalculation" = None

                # SetScalarCalculationDefinition
                defScalarCalc = EarlyBoundTests.AG_FOM.set_scalar_calculation_definition(
                    "Satellite/Satellite1 ElapsedTimeFromStop"
                )
                Assert.assertIsNotNone(defScalarCalc)

            else:
                # SetDefinitionType
                EarlyBoundTests.AG_FOM.set_definition_type(eType)

            TestBase.logger.WriteLine6("\t\tThe new DefinitionType is: {0}", EarlyBoundTests.AG_FOM.definition_type)
            eType2: "FigureOfMeritDefinitionType" = EarlyBoundTests.AG_FOM.definition_type
            Assert.assertEqual(eType, eType2)
            # Definition
            helper.Definition(EarlyBoundTests.AG_FOM.definition, eType, EarlyBoundTests.AG_COV.asset_list)

            iIndex += 1

        TestBase.logger.WriteLine("----- BASIC TEST ----- END -----")

    # endregion

    # region BUG72717
    @category("Graphics Tests")
    def test_BUG72717(self):
        gfx: "FigureOfMeritGraphics" = EarlyBoundTests.AG_FOM.graphics
        gfxAnim: "FigureOfMeritGraphics2DAttributesAnimation" = gfx.animation_settings
        gfxStatic: "IFigureOfMeritGraphics2DAttributes" = gfx.static

        # Hold original values
        holdHideAll: bool = gfx.show_graphics
        holdAnimationIsVisible: bool = gfxAnim.show_graphics
        holdStaticIsVisible: bool = gfxStatic.show_graphics

        # The "Show" properties can be set, regardless of the "Hide All" property (for backward compatibility)
        gfx.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)
        gfxAnim.show_graphics = True
        Assert.assertTrue(gfxAnim.show_graphics)
        gfxAnim.show_graphics = False
        Assert.assertFalse(gfxAnim.show_graphics)
        gfxStatic.show_graphics = True
        Assert.assertTrue(gfxStatic.show_graphics)
        gfxStatic.show_graphics = False
        Assert.assertFalse(gfxStatic.show_graphics)

        gfx.show_graphics = False
        Assert.assertFalse(gfx.show_graphics)
        gfxAnim.show_graphics = True
        Assert.assertTrue(gfxAnim.show_graphics)
        gfxAnim.show_graphics = False
        Assert.assertFalse(gfxAnim.show_graphics)
        gfxStatic.show_graphics = True
        Assert.assertTrue(gfxStatic.show_graphics)
        gfxStatic.show_graphics = False
        Assert.assertFalse(gfxStatic.show_graphics)

        # Setting either of the "Show" properties to true should reset the "Hide All" property
        gfx.show_graphics = False
        gfxAnim.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)  # value changed

        gfx.show_graphics = False
        gfxStatic.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)  # value changed

        # When "Hide All" is set to false, the "Show" properties should return false.
        gfxAnim.show_graphics = True
        gfx.show_graphics = False
        Assert.assertFalse(gfxAnim.show_graphics)  # value changed

        gfxStatic.show_graphics = True
        gfx.show_graphics = False
        Assert.assertFalse(gfxStatic.show_graphics)  # value changed

        # Restore original values
        gfx.show_graphics = holdHideAll
        gfxAnim.show_graphics = holdAnimationIsVisible
        gfxStatic.show_graphics = holdStaticIsVisible

    # endregion

    # region DefinitionTypes
    def test_DefinitionTypes(self):
        defType: "FigureOfMeritDefinitionType"
        for defType in Enum.GetValues(clr.TypeOf(FigureOfMeritDefinitionType)):
            if EarlyBoundTests.AG_FOM.is_definition_type_supported(defType):
                if defType == FigureOfMeritDefinitionType.ACCESS_CONSTRAINT:
                    EarlyBoundTests.AG_FOM.set_access_constraint_definition(FigureOfMeritConstraintName.ALTITUDE)
                    Assert.assertEqual(
                        FigureOfMeritDefinitionType.ACCESS_CONSTRAINT, EarlyBoundTests.AG_FOM.definition_type
                    )

                elif defType == FigureOfMeritDefinitionType.SCALAR_CALCULATION:
                    EarlyBoundTests.AG_FOM.set_scalar_calculation_definition("CentralBody/Earth ElapsedTimeFromStart")
                    Assert.assertEqual(
                        FigureOfMeritDefinitionType.SCALAR_CALCULATION, EarlyBoundTests.AG_FOM.definition_type
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
        oHelper.TestObjectFilesArray((IStkObject(EarlyBoundTests.AG_FOM)).object_files)

    # endregion

    # region GridInspector
    @category("Basic Tests")
    @category("Grid Inspector")
    def test_GridInspector(self):
        TestBase.logger.WriteLine("----- GRID INSPECTOR TEST ----- BEGIN -----")
        oSatellite: "Satellite" = Satellite(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "sat2")
        )
        Assert.assertIsNotNone(oSatellite)
        oPropagator: "PropagatorTwoBody" = PropagatorTwoBody(oSatellite.propagator)
        Assert.assertIsNotNone(oPropagator)
        oPropagator.propagate()

        # BoundsType (LATITUDE)
        TestBase.logger.WriteLine6("\tThe current BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        EarlyBoundTests.AG_COV.grid.bounds_type = CoverageBounds.LATITUDE
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        Assert.assertEqual(CoverageBounds.LATITUDE, EarlyBoundTests.AG_COV.grid.bounds_type)
        # Bounds
        lat: "CoverageBoundsLatitude" = CoverageBoundsLatitude(EarlyBoundTests.AG_COV.grid.bounds)
        Assert.assertIsNotNone(lat)
        TestBase.logger.WriteLine7(
            "\t\tThe current Bounds is: MinLatitude = {0}, MaxLatitude = {1}",
            lat.minimum_latitude,
            lat.maximum_latitude,
        )
        lat.minimum_latitude = -15
        lat.maximum_latitude = 15
        TestBase.logger.WriteLine7(
            "\t\tThe new Bounds is: MinLatitude = {0}, MaxLatitude = {1}", lat.minimum_latitude, lat.maximum_latitude
        )
        Assert.assertAlmostEqual(-15, float(lat.minimum_latitude), delta=0.001)
        Assert.assertAlmostEqual(15, float(lat.maximum_latitude), delta=0.001)

        # AssetList.Add
        EarlyBoundTests.AG_COV.asset_list.remove_all()
        assetListElement: "CoverageAssetListElement" = EarlyBoundTests.AG_COV.asset_list.add("Satellite/sat2")
        Assert.assertIsNotNone(assetListElement)
        # AssetStatus (ACTIVE)
        TestBase.logger.WriteLine6("\tThe current AssetStatus is: {0}", assetListElement.asset_status)
        assetListElement.asset_status = CoverageAssetStatus.ACTIVE
        TestBase.logger.WriteLine6("\tThe new AssetStatus is: {0}", assetListElement.asset_status)
        Assert.assertEqual(CoverageAssetStatus.ACTIVE, assetListElement.asset_status)

        # SetDefinitionType (N_ASSET_COVERAGE)
        TestBase.logger.WriteLine6("\tThe current DefinitionType is: {0}", EarlyBoundTests.AG_FOM.definition_type)
        EarlyBoundTests.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.N_ASSET_COVERAGE)
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
        oInspector: "FigureOfMeritGridInspector" = EarlyBoundTests.AG_FOM.grid_inspector
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
        oTimeVar: "DataProviderTimeVarying" = DataProviderTimeVarying(oInspector.point_figure_of_merit)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.execute_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointFOM result:")
        oResult.Dump()
        # PointSatisfaction
        oInterval: "DataProviderInterval" = DataProviderInterval(oInspector.point_satisfaction)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.execute("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointSatisfaction result:")
        oResult.Dump()
        # SelectRegion
        with pytest.raises(Exception):
            oInspector.select_region("AreaTarget1")
        # RegionFOM
        oTimeVar = DataProviderTimeVarying(oInspector.region_figure_of_merit)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.execute_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionFOM result:")
        oResult.Dump()
        # RegionSatisfaction
        oInterval = DataProviderInterval(oInspector.region_satisfaction)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.execute("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionSatisfaction result:")
        oResult.Dump()
        # ClearSelection
        oInspector.clear_selection()
        TestBase.logger.WriteLine5("\n\tThe ClearSelection message:{0}", oInspector.message)
        Assert.assertEqual("", oInspector.message)

        # BoundsType (CUSTOM_REGIONS)
        EarlyBoundTests.AG_COV.grid.bounds_type = CoverageBounds.CUSTOM_REGIONS
        TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", EarlyBoundTests.AG_COV.grid.bounds_type)
        Assert.assertEqual(CoverageBounds.CUSTOM_REGIONS, EarlyBoundTests.AG_COV.grid.bounds_type)
        # Bounds
        oCustom: "CoverageBoundsCustomRegions" = CoverageBoundsCustomRegions(EarlyBoundTests.AG_COV.grid.bounds)
        Assert.assertIsNotNone(oCustom)
        oCustom.area_targets.add("AreaTarget/AreaTarget1")

        # SelectRegion
        oInspector.select_region("AreaTarget1")
        # Message
        TestBase.logger.WriteLine5("\tThe SelectRegion message:\n{0}", oInspector.message)
        with pytest.raises(Exception):
            oInspector.select_region("Invalid.Region")
        # PointFOM
        oTimeVar = DataProviderTimeVarying(oInspector.point_figure_of_merit)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.execute_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointFOM result:")
        oResult.Dump()
        # PointSatisfaction
        oInterval = DataProviderInterval(oInspector.point_satisfaction)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.execute("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tPointSatisfaction result:")
        oResult.Dump()
        # RegionFOM
        oTimeVar = DataProviderTimeVarying(oInspector.region_figure_of_merit)
        Assert.assertIsNotNone(oTimeVar)
        oResult = DataProviderResultWriter(oTimeVar.execute_single("1 Jul 1999 00:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionFOM result:")
        oResult.Dump()
        # RegionSatisfaction
        oInterval = DataProviderInterval(oInspector.region_satisfaction)
        Assert.assertIsNotNone(oInterval)
        oResult = DataProviderResultWriter(oInterval.execute("1 Jul 1999 00:00:00.00", "1 Jul 1999 12:00:00.00"))
        TestBase.logger.WriteLine("\n\tRegionSatisfaction result:")
        oResult.Dump()
        # ClearSelection
        oInspector.clear_selection()
        TestBase.logger.WriteLine5("\n\tThe ClearSelection message:{0}", oInspector.message)
        Assert.assertEqual("", oInspector.message)
        # ClearAccesses
        EarlyBoundTests.AG_COV.clear_accesses()
        # Unload (eSatellite)
        TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "sat2")
        TestBase.logger.WriteLine("----- GRID INSPECTOR TEST ----- END -----")

    # endregion

    # region Graphics
    @category("Graphics Tests")
    def test_Graphics(self):
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- BEGIN -----")
        # Graphics
        oGraphics: "FigureOfMeritGraphics" = EarlyBoundTests.AG_FOM.graphics
        Assert.assertIsNotNone(oGraphics)

        # IsObjectGraphicsVisible
        oGraphics.show_graphics = False
        Assert.assertFalse(oGraphics.show_graphics)
        oGraphics.show_graphics = True
        Assert.assertTrue(oGraphics.show_graphics)

        helper = FOMHelper(TestBase.Application)
        # Static
        helper.GfxAttributes(oGraphics.static, False)
        # Contours (readonly)
        EarlyBoundTests.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.ACCESS_SEPARATION)
        Assert.assertEqual(FigureOfMeritDefinitionType.ACCESS_SEPARATION, EarlyBoundTests.AG_FOM.definition_type)
        helper.GfxContours(oGraphics.static.contours, True, True)
        helper.GfxContourLines(oGraphics.static.contours, True)
        # Contours
        EarlyBoundTests.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.TIME_AVERAGE_GAP)
        Assert.assertEqual(FigureOfMeritDefinitionType.TIME_AVERAGE_GAP, EarlyBoundTests.AG_FOM.definition_type)
        helper.GfxContours(oGraphics.static.contours, False, False)
        oldFillPoints: bool = oGraphics.static.fill_points
        oGraphics.static.fill_points = True
        helper.GfxContourLines(oGraphics.static.contours, False)
        oGraphics.static.fill_points = oldFillPoints

        # Animation (readonly)
        helper.GfxAnimationAttributes(oGraphics.animation_settings, True)
        # Animation
        EarlyBoundTests.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.SIMPLE_COVERAGE)
        Assert.assertEqual(FigureOfMeritDefinitionType.SIMPLE_COVERAGE, EarlyBoundTests.AG_FOM.definition_type)
        helper.GfxAnimationAttributes(oGraphics.animation_settings, False)
        # Contours (readonly)
        helper.GfxAnimationContours(oGraphics.animation_settings.contours, True, True)
        helper.GfxContourLines(oGraphics.animation_settings.contours, True)
        # Contours
        EarlyBoundTests.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.REVISIT_TIME)
        Assert.assertEqual(FigureOfMeritDefinitionType.REVISIT_TIME, EarlyBoundTests.AG_FOM.definition_type)
        EarlyBoundTests.AG_FOM.graphics.animation_settings.contours.show_graphics = True
        helper.GfxAnimationContours(oGraphics.animation_settings.contours, False, False)
        helper.GfxContourLines(oGraphics.animation_settings.contours, False)
        TestBase.logger.WriteLine("----- GRAPHICS TEST ----- END -----")

    # endregion

    # region VO
    @category("VO Tests")
    def test_VO(self):
        TestBase.logger.WriteLine("----- VO TEST ----- BEGIN -----")
        # VO
        oVO: "FigureOfMeritGraphics3D" = EarlyBoundTests.AG_FOM.graphics_3d
        Assert.assertIsNotNone(oVO)

        # Granularity
        TestBase.logger.WriteLine6("\tThe current Granularity is: {0}", oVO.granularity)
        oVO.granularity = 1.23
        TestBase.logger.WriteLine6("\tThe new Granularity is: {0}", oVO.granularity)
        Assert.assertEqual(1.23, oVO.granularity)
        with pytest.raises(Exception):
            oVO.granularity = 12.3
        # PixelsPerDeg
        TestBase.logger.WriteLine6("\tThe current PixelsPerDeg is: {0}", oVO.pixels_per_degree)
        oVO.pixels_per_degree = 12.3
        TestBase.logger.WriteLine6("\tThe new PixelsPerDeg is: {0}", oVO.pixels_per_degree)
        Assert.assertEqual(12.3, oVO.pixels_per_degree)
        with pytest.raises(Exception):
            oVO.pixels_per_degree = -12.3

        # Static
        self.VOAttributes(oVO.static, False)
        # Animation (readonly)
        EarlyBoundTests.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.TIME_AVERAGE_GAP)
        Assert.assertEqual(FigureOfMeritDefinitionType.TIME_AVERAGE_GAP, EarlyBoundTests.AG_FOM.definition_type)
        self.VOAttributes(oVO.animation_graphics_3d_settings, True)
        # Animation
        EarlyBoundTests.AG_FOM.set_definition_type(FigureOfMeritDefinitionType.SIMPLE_COVERAGE)
        Assert.assertEqual(FigureOfMeritDefinitionType.SIMPLE_COVERAGE, EarlyBoundTests.AG_FOM.definition_type)
        self.VOAttributes(oVO.animation_graphics_3d_settings, False)
        TestBase.logger.WriteLine("----- VO TEST ----- END -----")

    # endregion

    # region VOAttributes
    def VOAttributes(self, oAttributes: "FigureOfMeritGraphics3DAttributes", bReadOnly: bool):
        TestBase.logger.WriteLine4("----- VO ATTRIBUTES TEST (ReadOnly = {0})----- BEGIN -----", bReadOnly)
        Assert.assertIsNotNone(oAttributes)
        if bReadOnly:
            #  (readonly)
            with pytest.raises(Exception):
                oAttributes.show_graphics = True
            # PointSize (readonly)
            with pytest.raises(Exception):
                oAttributes.point_size = 5.6
            # Translucency (readonly)
            with pytest.raises(Exception):
                oAttributes.translucency = 56.78

        else:
            # IsVisible (false)
            TestBase.logger.WriteLine4("\tThe current IsVisible is: {0}", oAttributes.show_graphics)
            oAttributes.show_graphics = False
            TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.show_graphics)
            Assert.assertFalse(oAttributes.show_graphics)
            # PointSize (readonly)
            with pytest.raises(Exception):
                oAttributes.point_size = 5.6
            # Translucency (readonly)
            with pytest.raises(Exception):
                oAttributes.translucency = 56.78
            # IsVisible (true)
            oAttributes.show_graphics = True
            TestBase.logger.WriteLine4("\tThe new IsVisible is: {0}", oAttributes.show_graphics)
            Assert.assertTrue(oAttributes.show_graphics)
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
        oCovDef: "CoverageDefinition" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "CovDef_012341212"),
            CoverageDefinition,
        )
        Assert.assertIsNotNone(oCovDef)

        oFOMerit: "FigureOfMerit" = clr.CastAs(
            (IStkObject(oCovDef)).children.new(STKObjectType.FIGURE_OF_MERIT, "FOM_2352353"), FigureOfMerit
        )
        Assert.assertIsNotNone(oFOMerit)

        try:
            TestBase.logger.WriteLine6("\tThe current BoundsType is: {0}", oCovDef.grid.bounds_type)
            noSmoothFillBounds: "List[CoverageBounds]" = [CoverageBounds.CUSTOM_BOUNDARY]
            eBound: "CoverageBounds"
            for eBound in noSmoothFillBounds:
                oCovDef.grid.bounds_type = eBound
                TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oCovDef.grid.bounds_type)
                eBound2: "CoverageBounds" = oCovDef.grid.bounds_type
                Assert.assertEqual(eBound, eBound2)
                self.TestFOMGfxContours(oFOMerit, False)

            SmoothFillBounds: "List[CoverageBounds]" = [
                CoverageBounds.LATITUDE_LINE,
                CoverageBounds.LONGITUDE_LINE,
                CoverageBounds.CUSTOM_REGIONS,
                CoverageBounds.GLOBAL,
                CoverageBounds.LATITUDE,
            ]
            eBound: "CoverageBounds"
            for eBound in SmoothFillBounds:
                oCovDef.grid.bounds_type = eBound
                TestBase.logger.WriteLine6("\tThe new BoundsType is: {0}", oCovDef.grid.bounds_type)
                eBound2: "CoverageBounds" = oCovDef.grid.bounds_type
                Assert.assertEqual(eBound, eBound2)
                self.TestFOMGfxContours(oFOMerit, True)

        finally:
            (IStkObject(oCovDef)).children.unload(
                (IStkObject(oFOMerit)).class_type, (IStkObject(oFOMerit)).instance_name
            )
            TestBase.Application.current_scenario.children.unload(
                (IStkObject(oCovDef)).class_type, (IStkObject(oCovDef)).instance_name
            )

        TestBase.logger.WriteLine("----- GRAPHICS SMOOTH CONTOURS ----- END -----")

    # endregion

    # region TestFOMGfxContours
    def TestFOMGfxContours(self, fom: "FigureOfMerit", bIsSmoothFillSupported: bool):
        # SetDefinitionType (ACCESS_DURATION)
        TestBase.logger.WriteLine6("\t\tThe current DefinitionType is: {0}", fom.definition_type)
        fom.set_definition_type(FigureOfMeritDefinitionType.ACCESS_DURATION)
        TestBase.logger.WriteLine6("\t\tThe new DefinitionType is: {0}", fom.definition_type)
        Assert.assertEqual(FigureOfMeritDefinitionType.ACCESS_DURATION, fom.definition_type)
        # Graphics.Static.IsVisible
        TestBase.logger.WriteLine4(
            "\t\tThe current Graphics.Static.IsVisible is: {0}", fom.graphics.static.show_graphics
        )
        fom.graphics.static.show_graphics = True
        TestBase.logger.WriteLine4("\t\tThe new Graphics.Static.IsVisible is: {0}", fom.graphics.static.show_graphics)
        Assert.assertTrue(fom.graphics.static.show_graphics)
        # Graphics.Static.Contours.IsVisible
        TestBase.logger.WriteLine4(
            "\t\tThe current Graphics.Static.Contours.IsVisible is: {0}", fom.graphics.static.contours.show_graphics
        )
        fom.graphics.static.contours.show_graphics = True
        TestBase.logger.WriteLine4(
            "\t\tThe new Graphics.Static.Contours.IsVisible is: {0}", fom.graphics.static.contours.show_graphics
        )
        Assert.assertTrue(fom.graphics.static.contours.show_graphics)
        # Graphics.Static.Contours.ContourType
        TestBase.logger.WriteLine6(
            "\t\tThe current Graphics.Static.Contours.ContourType is: {0}", fom.graphics.static.contours.contour_type
        )
        if not bIsSmoothFillSupported:
            with pytest.raises(Exception):
                fom.graphics.static.contours.contour_type = FigureOfMeritGraphics2DContourType.SMOOTH_FILL

        else:
            fom.graphics.static.contours.contour_type = FigureOfMeritGraphics2DContourType.SMOOTH_FILL
            TestBase.logger.WriteLine6(
                "\t\tThe new Graphics.Static.Contours.ContourType is: {0}", fom.graphics.static.contours.contour_type
            )
            Assert.assertEqual(
                FigureOfMeritGraphics2DContourType.SMOOTH_FILL, fom.graphics.static.contours.contour_type
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
            STKObjectType.FACILITY, "Fac1Bug44875"
        )
        recobj: "IStkObject" = facobj.children.new(STKObjectType.RECEIVER, "Rcv1Bug44875")

        # Create cov def
        covdefobj: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STKObjectType.COVERAGE_DEFINITION, "CD1Bug44875"
        )
        covdef: "CoverageDefinition" = clr.CastAs(covdefobj, CoverageDefinition)
        covdef.point_definition.use_grid_seed = True
        covdef.point_definition.use_object_as_seed = True
        covdef.point_definition.grid_class = CoverageGridClass.RECEIVER
        covdef.point_definition.seed_instance = "Facility/Fac1Bug44875/Receiver/Rcv1Bug44875"
        covchilds: "IStkObjectCollection" = covdefobj.children

        fomobj1: "IStkObject" = covchilds.new(STKObjectType.FIGURE_OF_MERIT, "FM1Bug44875")
        fom1: "FigureOfMerit" = clr.CastAs(fomobj1, FigureOfMerit)
        fomcs1: "FigureOfMeritDefinitionAccessConstraint" = None
        fomcs1 = fom1.set_access_constraint_definition_name("C/No")
        if not TestBase.NoGraphicsMode:
            fomc1: "IFigureOfMeritGraphics2DContours" = fom1.graphics.static.contours
            fomc1.show_graphics = True
            col1: "FigureOfMeritGraphics2DLevelAttributesCollection" = fomc1.level_attributes
            unit1a: str = TestBase.Application.units_preferences.get_current_unit_abbrv("RatioUnit")
            unit2a: str = TestBase.Application.units_preferences.get_current_unit_abbrv("BandwidthUnit")
            TestBase.Application.units_preferences.set_current_unit("RatioUnit", "dB")
            TestBase.Application.units_preferences.set_current_unit("BandwidthUnit", "MHz")
            col1.add_level_range(-100, 0, 10)
            Assert.assertEqual(11, col1.count)
            TestBase.logger.WriteLine(("unit1a = " + unit1a))
            TestBase.logger.WriteLine(("unit2a = " + unit2a))
            TestBase.Application.units_preferences.set_current_unit("RatioUnit", unit1a)
            TestBase.Application.units_preferences.set_current_unit("BandwidthUnit", unit2a)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                fomc1: "IFigureOfMeritGraphics2DContours" = fom1.graphics.static.contours

        fomobj2: "IStkObject" = covchilds.new(STKObjectType.FIGURE_OF_MERIT, "FM2Bug44875")
        fom2: "FigureOfMerit" = clr.CastAs(fomobj2, FigureOfMerit)
        fomcs2: "FigureOfMeritDefinitionAccessConstraint" = None
        fomcs2 = fom2.set_access_constraint_definition_name("PowerFluxDensity")
        if not TestBase.NoGraphicsMode:
            fomc2: "IFigureOfMeritGraphics2DContours" = fom2.graphics.static.contours
            fomc2.show_graphics = True
            col2: "FigureOfMeritGraphics2DLevelAttributesCollection" = fomc2.level_attributes
            unit1b: str = TestBase.Application.units_preferences.get_current_unit_abbrv("Power")
            unit2b: str = TestBase.Application.units_preferences.get_current_unit_abbrv("SmallDistance")
            TestBase.Application.units_preferences.set_current_unit("Power", "GW")
            TestBase.Application.units_preferences.set_current_unit("SmallDistance", "ft")
            col2.add_level_range(0.1, 100, 10)
            Assert.assertEqual(10, col2.count)
            TestBase.logger.WriteLine(("unit1b = " + unit1b))
            TestBase.logger.WriteLine(("unit2b = " + unit2b))
            TestBase.Application.units_preferences.set_current_unit("Power", unit1b)
            TestBase.Application.units_preferences.set_current_unit("SmallDistance", unit2b)

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                fomc2: "IFigureOfMeritGraphics2DContours" = fom2.graphics.static.contours

        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("FigureOfMeritTests", "FigureOfMeritTests.sc"))
        EarlyBoundTests.AG_COV = CoverageDefinition(
            TestBase.Application.current_scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "CoverageDefinition1")
        )
        covObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)
        EarlyBoundTests.AG_FOM = FigureOfMerit(covObj.children.new(STKObjectType.FIGURE_OF_MERIT, "FigureOfMerit1"))
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
        facobj: "IStkObject" = TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Fac1X45332")
        recobj: "IStkObject" = facobj.children.new(STKObjectType.RECEIVER, ("Rcv1" + bugNum))

        # Create cov def
        covdefobj: "IStkObject" = TestBase.Application.current_scenario.children.new(
            STKObjectType.COVERAGE_DEFINITION, ("CD1" + bugNum)
        )
        covdef: "CoverageDefinition" = clr.CastAs(covdefobj, CoverageDefinition)
        covdef.point_definition.use_grid_seed = True
        covdef.point_definition.use_object_as_seed = True
        covdef.point_definition.grid_class = CoverageGridClass.RECEIVER
        covdef.point_definition.seed_instance = (("Facility/Fac1" + bugNum) + "/Receiver/Rcv1") + bugNum
        covchilds: "IStkObjectCollection" = covdefobj.children

        fomobj: "IStkObject" = covchilds.new(STKObjectType.FIGURE_OF_MERIT, ("FM1" + bugNum))
        fom: "FigureOfMerit" = clr.CastAs(fomobj, FigureOfMerit)
        fomcs: "FigureOfMeritDefinitionAccessConstraint" = None

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
            fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.LINE_OF_SIGHT)
            Assert.fail("Line of Sight access constraint not applicable for scenario setup")

        except Exception as e:
            msg: str = str(e)
            Assert.assertEqual("ConstraintName is not an available access constraint.", msg)
            TestBase.logger.WriteLine(("Expected exception: " + msg))

        try:
            fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.ACCESS_CONSTRAINT_PLUGIN)
            Assert.fail("Access Constraint Plugin access constraint not applicable for scenario setup")

        except Exception as e:
            msg: str = str(e)
            Assert.assertEqual("For Access Constraint Plugins, set the definition using the name of the plugin.", msg)
            TestBase.logger.WriteLine(("Expected exception: " + msg))

        # ===================================================================
        # Altitude
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.ALTITUDE)
        Assert.assertEqual(FigureOfMeritConstraintName.ALTITUDE, fomcs.constraint_name)
        Assert.assertEqual("Altitude", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("Altitude")
        Assert.assertEqual("Altitude", fomcs.constraint)
        Assert.assertEqual(FigureOfMeritConstraintName.ALTITUDE, fomcs.constraint_name)

        # ===================================================================
        # BER+I
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.BER_PLUS_I)
        Assert.assertEqual(FigureOfMeritConstraintName.BER_PLUS_I, fomcs.constraint_name)
        Assert.assertEqual("BER+I", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("BER+I")
        Assert.assertEqual("BER+I", fomcs.constraint)
        Assert.assertEqual(FigureOfMeritConstraintName.BER_PLUS_I, fomcs.constraint_name)

        # ===================================================================
        # C/No
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.C_OVER_N0)
        Assert.assertEqual(FigureOfMeritConstraintName.C_OVER_N0, fomcs.constraint_name)
        Assert.assertEqual("C/No", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("C/No")
        Assert.assertEqual("C/No", fomcs.constraint)
        Assert.assertEqual(FigureOfMeritConstraintName.C_OVER_N0, fomcs.constraint_name)

        # ===================================================================
        # J/S
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.J_OVER_S)
        Assert.assertEqual(FigureOfMeritConstraintName.J_OVER_S, fomcs.constraint_name)
        Assert.assertEqual("J/S", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("J/S")
        Assert.assertEqual("J/S", fomcs.constraint)
        Assert.assertEqual(FigureOfMeritConstraintName.J_OVER_S, fomcs.constraint_name)

        # ===================================================================
        # SrchTrkSinglePulseJOverS
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.SEARCH_TRACK_SINGLE_PULSE_J_OVER_S)
        Assert.assertEqual(FigureOfMeritConstraintName.SEARCH_TRACK_SINGLE_PULSE_J_OVER_S, fomcs.constraint_name)
        Assert.assertEqual("SrchTrkSinglePulseJOverS", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("SrchTrkSinglePulseJOverS")
        Assert.assertEqual("SrchTrkSinglePulseJOverS", fomcs.constraint)
        Assert.assertEqual(FigureOfMeritConstraintName.SEARCH_TRACK_SINGLE_PULSE_J_OVER_S, fomcs.constraint_name)

        # ===================================================================
        # CrdnCondition
        # ===================================================================
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.CONDITION)
        Assert.assertEqual(FigureOfMeritConstraintName.CONDITION, fomcs.constraint_name)
        Assert.assertEqual("CrdnCondition", fomcs.constraint)
        # Set to other than the access constraint we are going to test.
        fomcs = fom.set_access_constraint_definition(FigureOfMeritConstraintName.FREQUENCY)
        fomcs = fom.set_access_constraint_definition_name("CrdnCondition")
        Assert.assertEqual("CrdnCondition", fomcs.constraint)
        Assert.assertEqual(FigureOfMeritConstraintName.CONDITION, fomcs.constraint_name)

        TestBase.Application.close_scenario()
        TestBase.LoadTestScenario(Path.Combine("FigureOfMeritTests", "FigureOfMeritTests.sc"))
        EarlyBoundTests.AG_COV = CoverageDefinition(
            TestBase.Application.current_scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "CoverageDefinition1")
        )
        covObj: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_COV, IStkObject)
        EarlyBoundTests.AG_FOM = FigureOfMerit(covObj.children.new(STKObjectType.FIGURE_OF_MERIT, "FigureOfMerit1"))
        TestBase.logger.WriteLine("-----  ACCESS CONSTRAINT DEFINITION ----- END -----")

    # endregion

    # ----------------------------------------------------------------

    # region DP_PreData_Unit
    def test_DP_PreData_Unit(self):
        holdDateFormat: str = TestBase.Application.units_preferences.get_current_unit_abbrv("DateFormat")

        try:
            TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")

            coverageDefinitionObj: "IStkObject" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(
                    STKObjectType.COVERAGE_DEFINITION, "CoverageDefinitionPreDataTest"
                ),
                IStkObject,
            )
            coverageDefinition: "CoverageDefinition" = clr.CastAs(coverageDefinitionObj, CoverageDefinition)
            coverageDefinition.compute_accesses()
            figureOfMerit: "FigureOfMerit" = clr.CastAs(
                coverageDefinitionObj.children.new(STKObjectType.FIGURE_OF_MERIT, "FigureOfMeritPreDataTest"),
                FigureOfMerit,
            )

            dp: "IDataProvider" = clr.CastAs(
                (clr.CastAs(figureOfMerit, IStkObject)).data_providers["Time Value By Point"], IDataProvider
            )
            dpFixed: "DataProviderFixed" = clr.CastAs(dp, DataProviderFixed)
            dp.pre_data = "90"
            result: "DataProviderResult" = dpFixed.execute()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "Bogus"
            result = dpFixed.execute()
            Assert.assertEqual("Data Unavailable", str(result.message.messages[0]))

            satelliteObj: "IStkObject" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "SatellitePreDataTest"),
                IStkObject,
            )
            satellite: "Satellite" = clr.CastAs(satelliteObj, Satellite)
            satellite.set_propagator_type(PropagatorType.TWO_BODY)
            satelliteProp: "PropagatorTwoBody" = clr.CastAs(satellite.propagator, PropagatorTwoBody)
            satelliteProp.propagate()
            attitudeCoverageObj: "IStkObject" = clr.CastAs(
                satelliteObj.children.new(STKObjectType.ATTITUDE_COVERAGE, "AttitudeCoveragePreDataTest"), IStkObject
            )
            attitudeFigureOfMeritObj: "IStkObject" = clr.CastAs(
                attitudeCoverageObj.children.new(
                    STKObjectType.ATTITUDE_FIGURE_OF_MERIT, "AttitudeFigureOfMeritPreDataTest"
                ),
                IStkObject,
            )
            TestBase.Application.execute_command((("AttCov " + attitudeCoverageObj.path) + " Access Compute"))

            dp: "IDataProvider" = clr.CastAs(
                attitudeFigureOfMeritObj.data_providers["Time Value By Point"], IDataProvider
            )
            dpFixed: "DataProviderFixed" = clr.CastAs(dp, DataProviderFixed)
            dp.pre_data = "90"
            TestBase.Application.execute_command((("AttCov " + attitudeCoverageObj.path) + " Access Compute"))
            result: "DataProviderResult" = dpFixed.execute()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "Bogus"
            TestBase.Application.execute_command((("AttCov " + attitudeCoverageObj.path) + " Access Compute"))
            result = dpFixed.execute()
            Assert.assertEqual("Data Unavailable", str(result.message.messages[0]))

        finally:
            TestBase.Application.current_scenario.children.unload(
                STKObjectType.COVERAGE_DEFINITION, "CoverageDefinitionPreDataTest"
            )
            TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "SatellitePreDataTest")
            TestBase.Application.units_preferences.set_current_unit("DateFormat", holdDateFormat)

    # endregion
