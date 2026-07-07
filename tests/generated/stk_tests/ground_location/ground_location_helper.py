# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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
from assert_extension import *
from assertion_harness import *
from display_times_helper import *
from interfaces.stk_objects import *
from logger import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class GroundLocationHelper(object):
    def __init__(self, oApplication: "STKObjectRoot"):
        self.m_oLogger = Logger.Instance
        Assert.assertIsNotNone(oApplication)
        self.m_oApplication: "STKObjectRoot" = oApplication
        self.m_oUnits: "UnitPreferencesDimensionCollection" = oApplication.units_preferences
        self.m_oUnits.reset_units()

    # region Run_Basic method
    def Run_Basic(self, AG_GL: "IGroundLocation"):
        # UseLocalTimeOffset
        AG_GL.use_local_time_offset = True
        Assert.assertEqual(True, AG_GL.use_local_time_offset)

        # LocalTimeOffset
        AG_GL.local_time_offset = 200
        Assert.assertEqual(200, AG_GL.local_time_offset)

        # ResetAzElMask
        AG_GL.reset_az_el_mask()
        # GetAzElMask
        Assert.assertEqual(AzElMaskType.NONE, AG_GL.get_az_el_mask())

        AG_GL.set_az_el_mask(AzElMaskType.TERRAIN_DATA, 0)
        Assert.assertEqual(AzElMaskType.TERRAIN_DATA, AG_GL.get_az_el_mask())
        Assert.assertEqual(0.0, AG_GL.get_az_el_mask_data())

        # km
        AG_GL.max_range_when_computing_az_el_mask = 10.0
        Assert.assertEqual(10.0, AG_GL.max_range_when_computing_az_el_mask)
        with pytest.raises(Exception, match=RegexSubstringMatch("is invalid")):  # km
            AG_GL.max_range_when_computing_az_el_mask = -10.0
        AG_GL.max_range_when_computing_az_el_mask = 0.0
        Assert.assertEqual(0.0, AG_GL.max_range_when_computing_az_el_mask)

        # SaveTerrainMaskDataInBinary
        AG_GL.save_terrain_mask_data_in_binary = True
        Assert.assertTrue(AG_GL.save_terrain_mask_data_in_binary)
        AG_GL.save_terrain_mask_data_in_binary = False
        Assert.assertFalse(AG_GL.save_terrain_mask_data_in_binary)
        AG_GL.reset_az_el_mask()
        Assert.assertEqual(AzElMaskType.NONE, AG_GL.get_az_el_mask())

        # TerrainNorm
        AG_GL.terrain_norm = TerrainNormalType.SLOPE_AZIMUTH
        Assert.assertEqual(TerrainNormalType.SLOPE_AZIMUTH, AG_GL.terrain_norm)
        if AG_GL.terrain_norm == TerrainNormalType.SLOPE_AZIMUTH:
            slopeazimuth: "TerrainNormalSlopeAzimuth" = TerrainNormalSlopeAzimuth(AG_GL.terrain_norm_data)
            Assert.assertIsNotNone(slopeazimuth)
            Assert.assertIsNotNone(slopeazimuth.azimuth)
            Assert.assertIsNotNone(slopeazimuth.slope)

        # AltRef
        eAR: "AltitudeReferenceType" = AG_GL.altitude_reference
        AG_GL.altitude_reference = AltitudeReferenceType.MEAN_SEA_LEVEL
        Assert.assertEqual(AltitudeReferenceType.MEAN_SEA_LEVEL, AG_GL.altitude_reference)
        AG_GL.altitude_reference = eAR
        Assert.assertEqual(eAR, AG_GL.altitude_reference)

        # HeightAboveGround
        dHAG: float = AG_GL.height_above_ground
        AG_GL.height_above_ground = 333.35
        Assert.assertEqual(333.35, AG_GL.height_above_ground)
        AG_GL.height_above_ground = dHAG
        Assert.assertEqual(dHAG, AG_GL.height_above_ground)

        AG_GL.lighting_obstruction_model = LightingObstructionModelType.AZ_EL_MASK
        Assert.assertEqual(LightingObstructionModelType.AZ_EL_MASK, AG_GL.lighting_obstruction_model)

        AG_GL.lighting_maximum_step = 0
        Assert.assertEqual(0, AG_GL.lighting_maximum_step)
        AG_GL.lighting_maximum_step = 31557600
        Assert.assertEqual(31557600, AG_GL.lighting_maximum_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            AG_GL.lighting_maximum_step = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            AG_GL.lighting_maximum_step = 31557601

        AG_GL.lighting_obstruction_model = LightingObstructionModelType.CENTRAL_BODY_SHAPE
        Assert.assertEqual(LightingObstructionModelType.CENTRAL_BODY_SHAPE, AG_GL.lighting_obstruction_model)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            AG_GL.lighting_maximum_step = 31557600

        AG_GL.lighting_obstruction_model = LightingObstructionModelType.GROUND_MODEL
        Assert.assertEqual(LightingObstructionModelType.GROUND_MODEL, AG_GL.lighting_obstruction_model)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            AG_GL.lighting_maximum_step = 31557600

        AG_GL.lighting_obstruction_model = LightingObstructionModelType.TERRAIN
        Assert.assertEqual(LightingObstructionModelType.TERRAIN, AG_GL.lighting_obstruction_model)

        AG_GL.lighting_maximum_step = 0
        Assert.assertEqual(0, AG_GL.lighting_maximum_step)
        AG_GL.lighting_maximum_step = 31557600
        Assert.assertEqual(31557600, AG_GL.lighting_maximum_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            AG_GL.lighting_maximum_step = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            AG_GL.lighting_maximum_step = 31557601

    # endregion

    # region Run_DisplayTimes method
    def Run_DisplayTimes(self, AG_GL: "IGroundLocation"):
        oDisplayTimesHelper = DisplayTimesHelper(self.m_oApplication)
        oDisplayTimesHelper.Run(clr.CastAs(AG_GL, IDisplayTime))

    # endregion

    # region Run_Graphics method
    def Run_Graphics(self, AG_GL: "IGroundLocation"):
        gfx: "IGroundLocationGraphics" = AG_GL.ground_location_graphics
        Assert.assertIsNotNone(gfx)
        gfx.show_graphics = False
        Assert.assertFalse(gfx.show_graphics)
        gfx.show_graphics = True
        Assert.assertTrue(gfx.show_graphics)
        gfx.inherit_from_scenario = True
        Assert.assertEqual(True, gfx.inherit_from_scenario)
        gfx.use_instance_name_label = False
        Assert.assertEqual(False, gfx.use_instance_name_label)
        gfx.label_name = "new label"
        Assert.assertEqual("new label", gfx.label_name)
        gfx.label_color = Colors.from_argb(((128 * 256) * 256))
        AssertEx.AreEqual(Colors.from_argb(((128 * 256) * 256)), gfx.label_color)
        gfx.show_label = True
        Assert.assertEqual(True, gfx.show_label)
        gfx.marker_color = Colors.from_argb((255 * 256))
        AssertEx.AreEqual(Colors.from_argb((255 * 256)), gfx.marker_color)
        gfx.marker_style = "Star"
        Assert.assertEqual("Star", gfx.marker_style)

        self.m_oApplication.load_custom_marker(TestBase.GetScenarioFile("gp_marker.bmp"))
        gfx.marker_style = TestBase.GetScenarioFile("gp_marker.bmp")

        oHelper = GfxLabelNoteHelper(self.m_oUnits)
        oHelper.Run(gfx.label_notes)

        uiLC: Color = gfx.label_color
        uiNewColor: Color = Colors.from_argb(65280)  # Green
        gfx.label_color = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.label_color)

        uiMC: Color = gfx.marker_color
        uiNewColor = Colors.from_argb(16711680)  # Blue
        gfx.marker_color = uiNewColor
        AssertEx.AreEqual(uiNewColor, gfx.marker_color)
        gfx.label_name = "Finish"

    # endregion

    # region Run_GfxRangeContours method
    def Run_GfxRangeContours(self, AG_GL: "IGroundLocation"):
        gfx: "IGroundLocationGraphics" = clr.CastAs(AG_GL.ground_location_graphics, IGroundLocationGraphics)
        oGfxRangeContoursHelper = GfxRangeContoursHelper(self.m_oUnits)
        oGfxRangeContoursHelper.Run(gfx.contours)

    # endregion

    # region Run_GfxAzElMask method
    def Run_GfxAzElMask(self, AG_GL: "IGroundLocation"):
        azel: "BasicAzElMask" = AG_GL.ground_location_graphics.az_el_mask
        azel.show_mask_over_range = True
        Assert.assertTrue(azel.show_mask_over_range)
        azel.display_mask_over_altitude_range = True
        Assert.assertTrue(azel.display_mask_over_altitude_range)
        azel.number_of_altitude_steps = 3
        Assert.assertEqual(3, azel.number_of_altitude_steps)
        azel.number_of_range_steps = 4
        Assert.assertEqual(4, azel.number_of_range_steps)
        azel.display_altitude_maximum = 10
        Assert.assertEqual(10, azel.display_altitude_maximum)
        azel.display_altitude_minimum = 3
        Assert.assertEqual(3, azel.display_altitude_minimum)
        azel.display_range_maximum = 20
        Assert.assertEqual(20, azel.display_range_maximum)
        azel.display_range_minimum = 10
        Assert.assertEqual(10, azel.display_range_minimum)
        azel.display_color_at_altitude = False
        azel.show_color_at_range = False
        with pytest.raises(Exception):
            azel.altitude_color = Colors.Yellow
        with pytest.raises(Exception):
            azel.range_color = Colors.Yellow
        azel.display_color_at_altitude = True
        Assert.assertTrue(azel.display_color_at_altitude)
        azel.altitude_color = Colors.Yellow
        AssertEx.AreEqual(Colors.Yellow, azel.altitude_color)
        azel.show_color_at_range = True
        Assert.assertTrue(azel.show_color_at_range)
        azel.range_color = Colors.Yellow
        AssertEx.AreEqual(Colors.Yellow, azel.range_color)

    # endregion

    # region Run_VO method
    def Run_VO(self, AG_GL: "IGroundLocation"):
        vo: "IGroundLocationGraphics3D" = AG_GL.ground_location_graphics_3d

        oAzElMaskHelper = VOAzElMaskHelper()
        oAzElMaskHelper.Run(vo.az_el_mask)

        oLabelSwapHelper = VOLabelSwapDistanceHelper()
        oLabelSwapHelper.Run(vo.uncertainty_area_label_swap_distance)

        oVectorsHelper = VOVectorsHelper(self.m_oUnits, self.m_oApplication)
        oVectorsHelper.Run(vo.vector, False)

        oDataDisplayHelper = VODataDisplayHelper(self.m_oApplication)
        oDataDisplayHelper.Run(vo.data_displays, False, False)

        oRangeContoursHelper = VORangeContoursHelper(self.m_oUnits)
        oRangeContoursHelper.Run(vo.range_contours)

        oOffsetsHelper = VOOffsetsHelper(self.m_oUnits)
        oOffsetsHelper.Run(vo.offsets)

        oTargetModelHelper = VOTargetModelHelper(self.m_oApplication, self.m_oUnits)
        oTargetModelHelper.Run(vo.model)

        oMarkerHelper = VOMarkerHelper(self.m_oUnits)
        oMarkerHelper.Run(vo.model.marker, False)

        oModel: "IGraphics3DModel" = vo.model
        self.m_oLogger.WriteLine6("\tThe current ModelType is: {0}", oModel.model_type)
        oModel.model_type = ModelType.FILE
        self.m_oLogger.WriteLine6("\tThe new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(ModelType.FILE, oModel.model_type)
        oModelFile: "Graphics3DModelFile" = clr.CastAs(oModel.model_data, Graphics3DModelFile)
        Assert.assertIsNotNone(oModelFile)
        self.m_oLogger.WriteLine5("\t\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        self.m_oLogger.WriteLine5("\t\tThe new Filename is: {0}", oModelFile.filename)
        with pytest.raises(Exception):
            oModelFile.filename = ""

        oModelPointingHelper = VOModelPointingHelper()
        oModelPointingHelper.Run(vo.model_pointing)

        oVaporTrailHelper = VOVaporTrailHelper()
        oVaporTrailHelper.Run(vo.vapor_trail, clr.CastAs(vo.model, IGraphics3DModel), TestBase.GetSTKHomeDir())

    # endregion
