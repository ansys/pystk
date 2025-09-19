# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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
from interfaces.stk_objects import *
from ansys.stk.core.utilities.colors import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        Console.WriteLine("XXX Volumetric OneTimeSetUp - START")
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("VolumetricTests", "VolumetricTests.sc"))
        EarlyBoundTests.AG_VOL = Volumetric(
            TestBase.Application.current_scenario.children.new(STKObjectType.VOLUMETRIC, "Volumetric1")
        )
        Console.WriteLine("XXX Volumetric OneTimeSetUp - END")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        Console.WriteLine("XXX Volumetric OneTimeTearDown - START")
        TestBase.Application.current_scenario.children.unload(STKObjectType.VOLUMETRIC, "Volumetric1")
        EarlyBoundTests.AG_VOL = None
        TestBase.Uninitialize()
        Console.WriteLine("XXX Volumetric OneTimeTearDown - END")

    # endregion

    # region Static DataMembers
    AG_VOL: "Volumetric" = None
    # endregion

    # ----------------------------------------------------------------

    # region Definition
    def test_Definition(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - START")

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            EarlyBoundTests.AG_VOL.set_volume_grid_definition_type(VolumetricDefinitionType.UNKNOWN)

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - Before setting to GRID_SPATIAL_CALCULATION")
        EarlyBoundTests.AG_VOL.set_volume_grid_definition_type(VolumetricDefinitionType.GRID_SPATIAL_CALCULATION)
        Assert.assertEqual(
            VolumetricDefinitionType.GRID_SPATIAL_CALCULATION, EarlyBoundTests.AG_VOL.volume_grid_definition_type
        )

        vmGridSpatialCalculation: "VolumetricGridSpatialCalculation" = clr.CastAs(
            EarlyBoundTests.AG_VOL.volume_grid_definition, VolumetricGridSpatialCalculation
        )

        Console.WriteLine(
            "XXX Volumetric.EarlyBoundTests.Definition - Before setting vmGridSpatialCalculation properties"
        )
        vmGridSpatialCalculation.volume_grid = "CentralBody/Earth GlobalCartographicUpTo1000km"
        Assert.assertEqual("CentralBody/Earth GlobalCartographicUpTo1000km", vmGridSpatialCalculation.volume_grid)
        vmGridSpatialCalculation.volume_grid = "CentralBody/Sun GlobalCartographicUpTo1000km"
        Assert.assertEqual("CentralBody/Sun GlobalCartographicUpTo1000km", vmGridSpatialCalculation.volume_grid)
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not create")):
            vmGridSpatialCalculation.volume_grid = "CentralBody/Earth Bogus"

        vmGridSpatialCalculation.use_spatial_calculation = False
        Assert.assertFalse(vmGridSpatialCalculation.use_spatial_calculation)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmGridSpatialCalculation.spatial_calculation = "Satellite/Satellite1 Altitude"

        vmGridSpatialCalculation.use_spatial_calculation = True
        Assert.assertTrue(vmGridSpatialCalculation.use_spatial_calculation)

        vmGridSpatialCalculation.spatial_calculation = "Satellite/Satellite1 Altitude"
        Assert.assertEqual("Satellite/Satellite1 Altitude", vmGridSpatialCalculation.spatial_calculation)
        with pytest.raises(Exception, match=RegexSubstringMatch("Could not create")):
            vmGridSpatialCalculation.spatial_calculation = "Satellite/Satellite1 Bogus"

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - Before setting to FILE")
        EarlyBoundTests.AG_VOL.set_volume_grid_definition_type(VolumetricDefinitionType.FILE)
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - After setting to FILE")
        Assert.assertEqual(VolumetricDefinitionType.FILE, EarlyBoundTests.AG_VOL.volume_grid_definition_type)

        vmExternalFile: "VolumetricExternalFile" = clr.CastAs(
            EarlyBoundTests.AG_VOL.volume_grid_definition, VolumetricExternalFile
        )

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - Before setting vmExternalFile properties")
        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid file name")):
            vmExternalFile.reload()

        filename: str = TestBase.GetScenarioFile("Volumetric1.vmc.IncludeLink.h5")
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - Before setting Filename")

        try:
            vmExternalFile.filename = filename

        except Exception as ex:
            Assert.fail(("XXX CATCH: Exception message: " + str(ex)))

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - After setting Filename")
        Assert.assertEqual(filename, vmExternalFile.filename)

        # filename = GetScenarioFile("Volumetric1.vmc.EmbedAll.h5");
        # Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - Before setting Filename - 2");
        # vmExternalFile.Filename = filename;
        # Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - After setting Filename - 2");
        # Assert.AreEqual(filename, vmExternalFile.Filename);

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid file name")):
            vmExternalFile.filename = ""
        with pytest.raises(Exception, match=RegexSubstringMatch("File not found")):
            vmExternalFile.filename = "bogus"

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - Before calling Reload")
        vmExternalFile.reload()
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - After calling Reload")

        # Return setting to original to avoid other tests failing
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - Before setting to GRID_SPATIAL_CALCULATION")
        EarlyBoundTests.AG_VOL.set_volume_grid_definition_type(VolumetricDefinitionType.GRID_SPATIAL_CALCULATION)
        Assert.assertEqual(
            VolumetricDefinitionType.GRID_SPATIAL_CALCULATION, EarlyBoundTests.AG_VOL.volume_grid_definition_type
        )

        Console.WriteLine(
            "XXX Volumetric.EarlyBoundTests.Definition - Before setting vmGridSpatialCalculation2 properties"
        )
        vmGridSpatialCalculation2: "VolumetricGridSpatialCalculation" = clr.CastAs(
            EarlyBoundTests.AG_VOL.volume_grid_definition, VolumetricGridSpatialCalculation
        )

        vmGridSpatialCalculation2.volume_grid = "CentralBody/Earth GlobalCartographicUpTo1000km"
        Assert.assertEqual("CentralBody/Earth GlobalCartographicUpTo1000km", vmGridSpatialCalculation2.volume_grid)

        vmGridSpatialCalculation2.use_spatial_calculation = True
        Assert.assertTrue(vmGridSpatialCalculation2.use_spatial_calculation)

        vmGridSpatialCalculation2.spatial_calculation = "Satellite/Satellite1 Altitude"
        Assert.assertEqual("Satellite/Satellite1 Altitude", vmGridSpatialCalculation2.spatial_calculation)

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Definition - END")

    # endregion

    # region Interval_AnalysisInterval
    def test_Interval_AnalysisInterval(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Interval_AnalysisInterval - START")

        vmAnalysisInterval: "VolumetricAnalysisInterval" = EarlyBoundTests.AG_VOL.volume_analysis_interval

        vmAnalysisInterval.analysis_interval = "Satellite/Satellite1 AvailabilityTimeSpan Interval"
        Assert.assertEqual("Satellite/Satellite1 AvailabilityTimeSpan Interval", vmAnalysisInterval.analysis_interval)
        vmAnalysisInterval.analysis_interval = "Scenario/VolumetricTests AnalysisInterval Interval"
        Assert.assertEqual("Scenario/VolumetricTests AnalysisInterval Interval", vmAnalysisInterval.analysis_interval)

        with pytest.raises(Exception, match=RegexSubstringMatch("Could not create")):
            vmAnalysisInterval.analysis_interval = "Scenario/VolumetricTests Bogus Interval"

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Interval_AnalysisInterval - END")

    # endregion

    # region Interval_Evaluation
    def test_Interval_Evaluation(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Interval_Evaluation - START")

        vmAnalysisInterval: "VolumetricAnalysisInterval" = EarlyBoundTests.AG_VOL.volume_analysis_interval

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            vmAnalysisInterval.set_spatial_calcuation_evaluation_type(
                VolumetricSpatialCalculationEvaluationType.UNKNOWN
            )

        vmAnalysisInterval.set_spatial_calcuation_evaluation_type(
            VolumetricSpatialCalculationEvaluationType.AT_INSTANT_IN_TIME
        )
        Assert.assertEqual(
            VolumetricSpatialCalculationEvaluationType.AT_INSTANT_IN_TIME,
            vmAnalysisInterval.evaluation_of_spatial_calculation_type,
        )

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmAnalysisInterval.time_array = "Scenario/VolumetricTests OneMinuteSampleTimes"
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmAnalysisInterval.step_size = 60

        vmAnalysisInterval.set_spatial_calcuation_evaluation_type(
            VolumetricSpatialCalculationEvaluationType.AT_TIMES_FROM_TIME_ARRAY
        )
        Assert.assertEqual(
            VolumetricSpatialCalculationEvaluationType.AT_TIMES_FROM_TIME_ARRAY,
            vmAnalysisInterval.evaluation_of_spatial_calculation_type,
        )

        vmAnalysisInterval.time_array = "Satellite/Satellite1 EphemerisTimes"
        Assert.assertEqual("Satellite/Satellite1 EphemerisTimes", vmAnalysisInterval.time_array)
        vmAnalysisInterval.time_array = "Scenario/VolumetricTests OneMinuteSampleTimes"
        Assert.assertEqual("Scenario/VolumetricTests OneMinuteSampleTimes", vmAnalysisInterval.time_array)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmAnalysisInterval.step_size = 60

        vmAnalysisInterval.set_spatial_calcuation_evaluation_type(
            VolumetricSpatialCalculationEvaluationType.AT_TIMES_AT_STEP_SIZE
        )
        Assert.assertEqual(
            VolumetricSpatialCalculationEvaluationType.AT_TIMES_AT_STEP_SIZE,
            vmAnalysisInterval.evaluation_of_spatial_calculation_type,
        )

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmAnalysisInterval.time_array = "Scenario/VolumetricTests OneMinuteSampleTimes"

        vmAnalysisInterval.step_size = 0.001
        Assert.assertEqual(0.001, vmAnalysisInterval.step_size)
        vmAnalysisInterval.step_size = 86400
        Assert.assertEqual(86400, vmAnalysisInterval.step_size)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmAnalysisInterval.step_size = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmAnalysisInterval.step_size = 86401

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Interval_Evaluation - END")

    # endregion

    # region Advanced
    def test_Advanced(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Advanced - START")

        vmAdvanced: "VolumetricAdvancedSettings" = EarlyBoundTests.AG_VOL.advanced

        vmAdvanced.recompute_automatically = True
        Assert.assertTrue(vmAdvanced.recompute_automatically)
        vmAdvanced.recompute_automatically = False
        Assert.assertFalse(vmAdvanced.recompute_automatically)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            vmAdvanced.save_computed_data_type = VolumetricSaveComputedDataType.UNKNOWN
        vmAdvanced.save_computed_data_type = VolumetricSaveComputedDataType.NO_SAVE
        Assert.assertEqual(VolumetricSaveComputedDataType.NO_SAVE, vmAdvanced.save_computed_data_type)
        vmAdvanced.save_computed_data_type = VolumetricSaveComputedDataType.NO_SAVE_COMPUTE_ON_LOAD
        Assert.assertEqual(VolumetricSaveComputedDataType.NO_SAVE_COMPUTE_ON_LOAD, vmAdvanced.save_computed_data_type)
        vmAdvanced.save_computed_data_type = VolumetricSaveComputedDataType.SAVE
        Assert.assertEqual(VolumetricSaveComputedDataType.SAVE, vmAdvanced.save_computed_data_type)

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Advanced - END")

    # endregion

    # region Compute
    def test_Compute(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Compute - START")

        # AG_VOL.Clear();  // test
        EarlyBoundTests.AG_VOL.compute()

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Compute - END")

    # endregion

    # region Clear
    def test_Clear(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Clear - START")

        # AG_VOL.Compute();  // test
        EarlyBoundTests.AG_VOL.clear()

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Clear - END")

    # endregion

    # region ComputeInParallel
    def test_ComputeInParallel(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.ComputeInParallel - START")

        # AG_VOL.Clear();  // test
        EarlyBoundTests.AG_VOL.compute_in_parallel()

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.ComputeInParallel - END")

    # endregion

    # region Export
    def test_Export(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Export - START")

        exportTool: "VolumetricExportTool" = EarlyBoundTests.AG_VOL.get_volumetric_export_tool()

        exportTool.export_data_format_type = VolumetricDataExportFormatType.HDF5
        Assert.assertEqual(VolumetricDataExportFormatType.HDF5, exportTool.export_data_format_type)

        exportTool.volume_grid_export_type = VolumetricVolumeGridExportType.INCLUDE_LINK_TO_VOLUME_GRID
        Assert.assertEqual(
            VolumetricVolumeGridExportType.INCLUDE_LINK_TO_VOLUME_GRID, exportTool.volume_grid_export_type
        )
        exportTool.volume_grid_export_type = VolumetricVolumeGridExportType.EMBED_VOLUME_GRID_DEFINITION
        Assert.assertEqual(
            VolumetricVolumeGridExportType.EMBED_VOLUME_GRID_DEFINITION, exportTool.volume_grid_export_type
        )

        exportTool.include_grid_point_cartesian = False
        Assert.assertFalse(exportTool.include_grid_point_cartesian)
        exportTool.include_grid_point_cartesian = True
        Assert.assertTrue(exportTool.include_grid_point_cartesian)

        exportTool.include_grid_point_native = False
        Assert.assertFalse(exportTool.include_grid_point_native)
        exportTool.include_grid_point_native = True
        Assert.assertTrue(exportTool.include_grid_point_native)

        exportTool.include_grid_reference = False
        Assert.assertFalse(exportTool.include_grid_reference)
        exportTool.include_grid_reference = True
        Assert.assertTrue(exportTool.include_grid_reference)

        filename: str = Path.Combine(TestBase.TemporaryDirectory, "VolumetricTest.h5")

        EarlyBoundTests.AG_VOL.set_volume_grid_definition_type(VolumetricDefinitionType.GRID_SPATIAL_CALCULATION)
        vmGridSpatialCalculation: "VolumetricGridSpatialCalculation" = clr.CastAs(
            EarlyBoundTests.AG_VOL.volume_grid_definition, VolumetricGridSpatialCalculation
        )
        vmGridSpatialCalculation.use_spatial_calculation = True
        vmGridSpatialCalculation.spatial_calculation = "Satellite/Satellite1 Altitude"

        with pytest.raises(Exception, match=RegexSubstringMatch("Invalid")):
            exportTool.export("")

        exportTool.export(filename)
        Assert.assertTrue(File.Exists(filename))

        # Cleanup
        File.Delete(filename)
        vmGridSpatialCalculation.spatial_calculation = "CentralBody/Earth Altitude"
        vmGridSpatialCalculation.use_spatial_calculation = False

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.Export - END")

    # endregion

    # region VO_Attributes
    @category("VO Tests")
    def test_VO_Attributes(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Attributes - START")

        vmVO: "VolumetricGraphics3D" = EarlyBoundTests.AG_VOL.graphics_3d

        vmVO.visible = True
        Assert.assertTrue(vmVO.visible)
        vmVO.visible = False
        Assert.assertFalse(vmVO.visible)

        vmVO.smoothing = True
        Assert.assertTrue(vmVO.smoothing)
        vmVO.smoothing = False
        Assert.assertFalse(vmVO.smoothing)

        vmVO.shading = True
        Assert.assertTrue(vmVO.shading)
        vmVO.shading = False
        Assert.assertFalse(vmVO.shading)

        vmVO.quality = VolumetricDisplayQualityType.QUALITY_LOW
        Assert.assertEqual(VolumetricDisplayQualityType.QUALITY_LOW, vmVO.quality)
        vmVO.quality = VolumetricDisplayQualityType.QUALITY_MEDIUM
        Assert.assertEqual(VolumetricDisplayQualityType.QUALITY_MEDIUM, vmVO.quality)
        vmVO.quality = VolumetricDisplayQualityType.QUALITY_HIGH
        Assert.assertEqual(VolumetricDisplayQualityType.QUALITY_HIGH, vmVO.quality)
        vmVO.quality = VolumetricDisplayQualityType.QUALITY_VERY_HIGH
        Assert.assertEqual(VolumetricDisplayQualityType.QUALITY_VERY_HIGH, vmVO.quality)

        #
        # Test VolumeType property
        #
        # Save previous value to restore when done
        vType: "VolumetricDisplayVolumeType" = vmVO.volume_type

        # Test Spatial Calculation Levels volume type when valid
        # spatial calc component is set.
        vmGridSpatialCalculation: "VolumetricGridSpatialCalculation" = clr.CastAs(
            EarlyBoundTests.AG_VOL.volume_grid_definition, VolumetricGridSpatialCalculation
        )
        vmGridSpatialCalculation.use_spatial_calculation = True
        vmGridSpatialCalculation.spatial_calculation = "Satellite/Satellite1 Altitude"
        vmVO.volume_type = VolumetricDisplayVolumeType.SPATIAL_CALCULATION_VALUE_LEVELS
        Assert.assertTrue((vmVO.volume_type == VolumetricDisplayVolumeType.SPATIAL_CALCULATION_VALUE_LEVELS))

        # Test Active Grid Points volume type
        vmVO.volume_type = VolumetricDisplayVolumeType.ACTIVE_GRID_POINTS
        Assert.assertTrue((vmVO.volume_type == VolumetricDisplayVolumeType.ACTIVE_GRID_POINTS))

        # Test Spatial Calculation Levels volume type when invalid
        # spatial calc component is set.  An exception should be thrown
        # when this occurs.
        vmGridSpatialCalculation.use_spatial_calculation = False
        with pytest.raises(Exception, match=RegexSubstringMatch("Spatial calculation is unavailable")):
            vmVO.volume_type = VolumetricDisplayVolumeType.SPATIAL_CALCULATION_VALUE_LEVELS
        Assert.assertTrue((vmVO.volume_type == VolumetricDisplayVolumeType.ACTIVE_GRID_POINTS))

        # Restore inital state
        vmVO.volume_type = vType

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Attributes - END")

    # endregion

    # region VO_Grid
    @category("VO Tests")
    def test_VO_Grid(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Grid - START")

        vmVOGrid: "VolumetricGraphics3DGrid" = EarlyBoundTests.AG_VOL.graphics_3d.grid

        vmVOGrid.show_grid = False
        Assert.assertFalse(vmVOGrid.show_grid)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOGrid.show_grid_points = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOGrid.show_grid_lines = True
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOGrid.point_size = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOGrid.point_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOGrid.line_color = Colors.Red

        vmVOGrid.show_grid = True
        Assert.assertTrue(vmVOGrid.show_grid)

        vmVOGrid.show_grid_points = False
        Assert.assertFalse(vmVOGrid.show_grid_points)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOGrid.point_size = 1
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOGrid.point_color = Colors.Red

        vmVOGrid.show_grid_points = True
        Assert.assertTrue(vmVOGrid.show_grid_points)

        vmVOGrid.point_size = 1
        Assert.assertEqual(1, vmVOGrid.point_size)
        vmVOGrid.point_size = 20
        Assert.assertEqual(20, vmVOGrid.point_size)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmVOGrid.point_size = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmVOGrid.point_size = 21

        vmVOGrid.point_color = Colors.Red
        Assert.assertEqual(Colors.Red, vmVOGrid.point_color)
        vmVOGrid.point_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, vmVOGrid.point_color)

        vmVOGrid.show_grid_lines = False
        Assert.assertFalse(vmVOGrid.show_grid_lines)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOGrid.line_color = Colors.Red

        vmVOGrid.show_grid_lines = True
        Assert.assertTrue(vmVOGrid.show_grid_lines)

        vmVOGrid.line_color = Colors.Red
        Assert.assertEqual(Colors.Red, vmVOGrid.line_color)
        vmVOGrid.line_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, vmVOGrid.line_color)

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Grid - END")

    # endregion

    # region VO_Volume_ActiveGridPoints
    @category("VO Tests")
    def test_VO_Volume_ActiveGridPoints(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Volume_ActiveGridPoints - START")

        vmVOVolume: "VolumetricGraphics3DVolume" = EarlyBoundTests.AG_VOL.graphics_3d.volume
        vmVOActiveGridPoints: "VolumetricGraphics3DActiveGridPoints" = vmVOVolume.active_grid_points

        # Active/Inactive Boundary

        vmVOActiveGridPoints.show_active_inactive_boundary = False
        Assert.assertFalse(vmVOActiveGridPoints.show_active_inactive_boundary)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOActiveGridPoints.active_inactive_boundary_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOActiveGridPoints.active_inactive_boundary_translucency = 0

        vmVOActiveGridPoints.show_active_inactive_boundary = True
        Assert.assertTrue(vmVOActiveGridPoints.show_active_inactive_boundary)

        vmVOActiveGridPoints.active_inactive_boundary_color = Colors.Red
        Assert.assertEqual(Colors.Red, vmVOActiveGridPoints.active_inactive_boundary_color)
        vmVOActiveGridPoints.active_inactive_boundary_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, vmVOActiveGridPoints.active_inactive_boundary_color)

        vmVOActiveGridPoints.active_inactive_boundary_translucency = 0
        Assert.assertEqual(0, vmVOActiveGridPoints.active_inactive_boundary_translucency)
        vmVOActiveGridPoints.active_inactive_boundary_translucency = 100
        Assert.assertEqual(100, vmVOActiveGridPoints.active_inactive_boundary_translucency)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmVOActiveGridPoints.active_inactive_boundary_translucency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmVOActiveGridPoints.active_inactive_boundary_translucency = 101

        # Active/Inactive Fill

        vmVOActiveGridPoints.show_active_inactive_fill = False
        Assert.assertFalse(vmVOActiveGridPoints.show_active_inactive_fill)

        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOActiveGridPoints.inactive_fill_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOActiveGridPoints.inactive_fill_translucency = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOActiveGridPoints.active_fill_color = Colors.Red
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):
            vmVOActiveGridPoints.active_fill_translucency = 0

        vmVOActiveGridPoints.show_active_inactive_fill = True
        Assert.assertTrue(vmVOActiveGridPoints.show_active_inactive_fill)

        vmVOActiveGridPoints.inactive_fill_color = Colors.Red
        Assert.assertEqual(Colors.Red, vmVOActiveGridPoints.inactive_fill_color)
        vmVOActiveGridPoints.inactive_fill_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, vmVOActiveGridPoints.inactive_fill_color)

        vmVOActiveGridPoints.inactive_fill_translucency = 0
        Assert.assertEqual(0, vmVOActiveGridPoints.inactive_fill_translucency)
        vmVOActiveGridPoints.inactive_fill_translucency = 100
        Assert.assertEqual(100, vmVOActiveGridPoints.inactive_fill_translucency)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmVOActiveGridPoints.inactive_fill_translucency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmVOActiveGridPoints.inactive_fill_translucency = 101

        vmVOActiveGridPoints.active_fill_color = Colors.Red
        Assert.assertEqual(Colors.Red, vmVOActiveGridPoints.active_fill_color)
        vmVOActiveGridPoints.active_fill_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, vmVOActiveGridPoints.active_fill_color)

        vmVOActiveGridPoints.active_fill_translucency = 0
        Assert.assertEqual(0, vmVOActiveGridPoints.active_fill_translucency)
        vmVOActiveGridPoints.active_fill_translucency = 100
        Assert.assertEqual(100, vmVOActiveGridPoints.active_fill_translucency)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmVOActiveGridPoints.active_fill_translucency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            vmVOActiveGridPoints.active_fill_translucency = 101

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Volume_ActiveGridPoints - END")

    # endregion

    # region VO_Volume_SpatialCalculationLevels
    @category("VO Tests")
    def test_VO_Volume_SpatialCalculationLevels(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Volume_SpatialCalculationLevels - START")

        # Setup
        EarlyBoundTests.AG_VOL.set_volume_grid_definition_type(VolumetricDefinitionType.GRID_SPATIAL_CALCULATION)
        Assert.assertEqual(
            VolumetricDefinitionType.GRID_SPATIAL_CALCULATION, EarlyBoundTests.AG_VOL.volume_grid_definition_type
        )

        vmGridSpatialCalculation: "VolumetricGridSpatialCalculation" = clr.CastAs(
            EarlyBoundTests.AG_VOL.volume_grid_definition, VolumetricGridSpatialCalculation
        )

        vmGridSpatialCalculation.volume_grid = "CentralBody/Earth GlobalCartographicUpTo1000km"
        Assert.assertEqual("CentralBody/Earth GlobalCartographicUpTo1000km", vmGridSpatialCalculation.volume_grid)

        vmGridSpatialCalculation.use_spatial_calculation = True
        Assert.assertTrue(vmGridSpatialCalculation.use_spatial_calculation)

        vmGridSpatialCalculation.spatial_calculation = "Satellite/Satellite1 Altitude"
        Assert.assertEqual("Satellite/Satellite1 Altitude", vmGridSpatialCalculation.spatial_calculation)

        vmVOVolume: "VolumetricGraphics3DVolume" = EarlyBoundTests.AG_VOL.graphics_3d.volume
        vmVOSpatialCalculationLevels: "VolumetricGraphics3DSpatialCalculationLevels" = (
            vmVOVolume.spatial_calculation_levels
        )

        # Boundary Levels

        vmVOSpatialCalculationLevels.show_boundary_levels = False
        Assert.assertFalse(vmVOSpatialCalculationLevels.show_boundary_levels)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not enabled")):
            vmVOSpatialCalculationLevels.boundary_levels.add(1, Colors.Red, 10)

        vmVOSpatialCalculationLevels.show_boundary_levels = True
        Assert.assertTrue(vmVOSpatialCalculationLevels.show_boundary_levels)

        self.Test_IAgVmVOSpatialCalculationLevelCollection(vmVOSpatialCalculationLevels.boundary_levels)

        # Fill Levels

        vmVOSpatialCalculationLevels.display_colors_outside_minimum_maximum = False
        Assert.assertFalse(vmVOSpatialCalculationLevels.display_colors_outside_minimum_maximum)
        vmVOSpatialCalculationLevels.display_colors_outside_minimum_maximum = True
        Assert.assertTrue(vmVOSpatialCalculationLevels.display_colors_outside_minimum_maximum)

        vmVOSpatialCalculationLevels.show_fill_levels = False
        Assert.assertFalse(vmVOSpatialCalculationLevels.show_fill_levels)

        with pytest.raises(Exception, match=RegexSubstringMatch("is not enabled")):
            vmVOSpatialCalculationLevels.fill_levels.add(1, Colors.Red, 10)

        vmVOSpatialCalculationLevels.show_fill_levels = True
        Assert.assertTrue(vmVOSpatialCalculationLevels.show_fill_levels)

        self.Test_IAgVmVOSpatialCalculationLevelCollection(vmVOSpatialCalculationLevels.fill_levels)

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Volume_SpatialCalculationLevels - END")

    # endregion

    def Test_IAgVmVOSpatialCalculationLevelCollection(
        self, levelColl: "VolumetricGraphics3DSpatialCalculationLevelCollection"
    ):
        Assert.assertEqual(0, levelColl.count)

        # Add some
        levelColl.add(1, Colors.Red, 10)
        levelColl.add(2, Colors.Green, 20)
        levelColl.add(3, Colors.Blue, 30)
        Assert.assertEqual(3, levelColl.count)

        Assert.assertEqual(1, levelColl[0].value)
        Assert.assertEqual(Colors.Red, levelColl[0].color)
        Assert.assertAlmostEqual(10, levelColl[0].translucency, delta=0.0001)

        Assert.assertEqual(2, levelColl[1].value)
        Assert.assertEqual(Colors.Green, levelColl[1].color)
        Assert.assertAlmostEqual(20, levelColl[1].translucency, delta=0.0001)

        Assert.assertEqual(3, levelColl[2].value)
        Assert.assertEqual(Colors.Blue, levelColl[2].color)
        Assert.assertAlmostEqual(30, levelColl[2].translucency, delta=0.0001)

        # Change some (call Add on an existing value will actually change it).
        levelColl.add(1, Colors.Yellow, 40)
        levelColl.add(2, Colors.Black, 50)
        Assert.assertEqual(3, levelColl.count)

        Assert.assertEqual(1, levelColl[0].value)
        Assert.assertEqual(Colors.Yellow, levelColl[0].color)
        Assert.assertAlmostEqual(40, levelColl[0].translucency, delta=0.0001)

        Assert.assertEqual(2, levelColl[1].value)
        Assert.assertEqual(Colors.Black, levelColl[1].color)
        Assert.assertAlmostEqual(50, levelColl[1].translucency, delta=0.0001)

        level0: "VolumetricGraphics3DSpatialCalculationLevel" = levelColl[0]
        Assert.assertEqual(1, level0.value)
        Assert.assertEqual(Colors.Yellow, level0.color)
        Assert.assertAlmostEqual(40, level0.translucency, delta=0.001)

        level1: "VolumetricGraphics3DSpatialCalculationLevel" = levelColl[1]
        Assert.assertEqual(2, level1.value)
        Assert.assertEqual(Colors.Black, level1.color)
        Assert.assertAlmostEqual(50, level1.translucency, delta=0.001)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            level3: "VolumetricGraphics3DSpatialCalculationLevel" = levelColl[3]

        i: int = 0
        while i < levelColl.count:
            Assert.assertTrue((levelColl[i].translucency > 5))

            i += 1

        level: "VolumetricGraphics3DSpatialCalculationLevel"

        for level in levelColl:
            Assert.assertTrue((level.translucency > 5))

        levelColl.remove_at(1)
        Assert.assertEqual(2, levelColl.count)
        Assert.assertEqual(2, level1.value)
        Assert.assertEqual(Colors.Black, level1.color)
        Assert.assertEqual(50, level1.translucency)

        with pytest.raises(Exception, match=RegexSubstringMatch("out of range")):
            levelColl.remove_at(3)

        levelColl.remove_all()
        Assert.assertEqual(0, levelColl.count)

    # region VO_Legends_FillLegend
    @category("VO Tests")
    def test_VO_Legends_FillLegend(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Legends_FillLegend - START")

        vmVO: "VolumetricGraphics3D" = EarlyBoundTests.AG_VOL.graphics_3d

        vmVO.show_fill_legend = False
        Assert.assertFalse(vmVO.show_fill_legend)

        with pytest.raises(Exception, match=RegexSubstringMatch("not enabled")):
            legend: "VolumetricGraphics3DLegend" = vmVO.fill_legend

        vmVO.show_fill_legend = True
        Assert.assertTrue(vmVO.show_fill_legend)

        self.Test_IAgVmVOLegend(vmVO.fill_legend)

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Legends_FillLegend - END")

    # endregion

    # region VO_Legends_BoundaryLegend
    @category("VO Tests")
    def test_VO_Legends_BoundaryLegend(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Legends_BoundaryLegend - START")

        vmVO: "VolumetricGraphics3D" = EarlyBoundTests.AG_VOL.graphics_3d

        vmVO.show_boundary_legend = False
        Assert.assertFalse(vmVO.show_boundary_legend)

        with pytest.raises(Exception, match=RegexSubstringMatch("not enabled")):
            legend: "VolumetricGraphics3DLegend" = vmVO.boundary_legend

        vmVO.show_boundary_legend = True
        Assert.assertTrue(vmVO.show_boundary_legend)

        self.Test_IAgVmVOLegend(vmVO.boundary_legend)

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.VO_Legends_BoundaryLegend - END")

    # endregion

    def Test_IAgVmVOLegend(self, legend: "VolumetricGraphics3DLegend"):
        legend.position_x = 0
        Assert.assertEqual(0, legend.position_x)
        legend.position_x = 5000
        Assert.assertEqual(5000, legend.position_x)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.position_x = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.position_x = 5001

        legend.position_y = 0
        Assert.assertEqual(0, legend.position_y)
        legend.position_y = 5000
        Assert.assertEqual(5000, legend.position_y)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.position_y = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.position_y = 5001

        legend.translucency = 0
        Assert.assertEqual(0, legend.translucency)
        legend.translucency = 100
        Assert.assertEqual(100, legend.translucency)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.translucency = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.translucency = 101

        legend.background_color = Colors.Red
        Assert.assertEqual(Colors.Red, legend.background_color)
        legend.background_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, legend.background_color)

        legend.title = "My Title"
        Assert.assertEqual("My Title", legend.title)

        legend.decimal_digits = 0
        Assert.assertEqual(0, legend.decimal_digits)
        legend.decimal_digits = 99
        Assert.assertEqual(99, legend.decimal_digits)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.decimal_digits = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.decimal_digits = 100

        legend.notation = VolumetricLegendNumericNotationType.FLOATING_POINT
        Assert.assertEqual(VolumetricLegendNumericNotationType.FLOATING_POINT, legend.notation)
        legend.notation = VolumetricLegendNumericNotationType.SCIENTIFIC_LOWERCASE_E
        Assert.assertEqual(VolumetricLegendNumericNotationType.SCIENTIFIC_LOWERCASE_E, legend.notation)
        legend.notation = VolumetricLegendNumericNotationType.SCIENTIFIC_UPPERCASE_E
        Assert.assertEqual(VolumetricLegendNumericNotationType.SCIENTIFIC_UPPERCASE_E, legend.notation)

        legend.text_color = Colors.Red
        Assert.assertEqual(Colors.Red, legend.text_color)
        legend.text_color = Colors.Blue
        Assert.assertEqual(Colors.Blue, legend.text_color)

        legend.level_order = VolumetricLevelOrder.HORIZONTAL_MINIMUM_TO_MAXIMUM
        Assert.assertEqual(VolumetricLevelOrder.HORIZONTAL_MINIMUM_TO_MAXIMUM, legend.level_order)

        legend.maximum_color_squares = 1
        Assert.assertEqual(1, legend.maximum_color_squares)
        legend.maximum_color_squares = 1000
        Assert.assertEqual(1000, legend.maximum_color_squares)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.maximum_color_squares = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.maximum_color_squares = 1001

        legend.level_order = VolumetricLevelOrder.HORIZONTAL_MAXIMUM_TO_MINIMUM
        Assert.assertEqual(VolumetricLevelOrder.HORIZONTAL_MAXIMUM_TO_MINIMUM, legend.level_order)

        legend.maximum_color_squares = 1
        Assert.assertEqual(1, legend.maximum_color_squares)
        legend.maximum_color_squares = 1000
        Assert.assertEqual(1000, legend.maximum_color_squares)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.maximum_color_squares = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.maximum_color_squares = 1001

        legend.level_order = VolumetricLevelOrder.VERTICAL_MINIMUM_TO_MAXIMUM
        Assert.assertEqual(VolumetricLevelOrder.VERTICAL_MINIMUM_TO_MAXIMUM, legend.level_order)

        legend.maximum_color_squares = 1
        Assert.assertEqual(1, legend.maximum_color_squares)
        legend.maximum_color_squares = 1000
        Assert.assertEqual(1000, legend.maximum_color_squares)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.maximum_color_squares = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.maximum_color_squares = 1001

        legend.level_order = VolumetricLevelOrder.VERTICAL_MAXIMUM_TO_MINIMUM
        Assert.assertEqual(VolumetricLevelOrder.VERTICAL_MAXIMUM_TO_MINIMUM, legend.level_order)

        legend.maximum_color_squares = 1
        Assert.assertEqual(1, legend.maximum_color_squares)
        legend.maximum_color_squares = 1000
        Assert.assertEqual(1000, legend.maximum_color_squares)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.maximum_color_squares = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.maximum_color_squares = 1001

        legend.color_square_height = 1
        Assert.assertEqual(1, legend.color_square_height)
        legend.color_square_height = 100
        Assert.assertEqual(100, legend.color_square_height)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.color_square_height = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.color_square_height = 101

        legend.color_square_width = 1
        Assert.assertEqual(1, legend.color_square_width)
        legend.color_square_width = 100
        Assert.assertEqual(100, legend.color_square_width)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.color_square_width = 0
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            legend.color_square_width = 101

    # region STKObject
    def test_STKObject(self):
        Console.WriteLine("XXX Volumetric.EarlyBoundTests.STKObject - START")

        oHelper = STKObjectHelper()
        volObject: "ISTKObject" = clr.CastAs(EarlyBoundTests.AG_VOL, ISTKObject)
        oHelper.Run(volObject)
        oHelper.TestObjectFilesArray(volObject.object_files)

        Console.WriteLine("XXX Volumetric.EarlyBoundTests.STKObject - END")

    # endregion

    # ----------------------------------------------------------------

    # region DP_PreData_Unit
    def test_DP_PreData_Unit(self):
        holdDateFormat: str = TestBase.Application.units_preferences.get_current_unit_abbrv("DateFormat")

        try:
            TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")

            volumetric: "Volumetric" = clr.CastAs(
                TestBase.Application.current_scenario.children.new(STKObjectType.VOLUMETRIC, "VolumetricPreDataTest"),
                Volumetric,
            )
            volumetric.compute()

            dp: "IDataProvider" = clr.CastAs(
                (clr.CastAs(volumetric, ISTKObject)).data_providers["Active Grid Points at Time"], IDataProvider
            )
            dpFixed: "DataProviderFixed" = clr.CastAs(dp, DataProviderFixed)
            dp.pre_data = "90"
            result: "DataProviderResult" = dpFixed.execute()

            # This test will currently always pass even though an incorrect value for a unit type is passed
            # because although data provider's pre-service call will fail, the actual data provider will ignore it and execute
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "Bogus 90"
            result = dpFixed.execute()

            # This test will currently always pass even though an incorrect value for a unit type is passed
            # because although data provider's pre-service call will fail, the actual data provider will ignore it and execute
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp = clr.CastAs(
                (clr.CastAs(volumetric, ISTKObject)).data_providers["Volumetric Values at Time"], IDataProvider
            )
            dpFixed = clr.CastAs(dp, DataProviderFixed)
            dp.pre_data = "90"
            result = dpFixed.execute()
            Assert.assertEqual("OK", str(result.message.messages[0]))

            dp.pre_data = "Bogus 90"
            result = dpFixed.execute()
            Assert.assertEqual("Data Unavailable", str(result.message.messages[0]))

        finally:
            TestBase.Application.current_scenario.children.unload(STKObjectType.VOLUMETRIC, "VolumetricPreDataTest")
            TestBase.Application.units_preferences.set_current_unit("DateFormat", holdDateFormat)

    # endregion
