# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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
from access_constraints.access_constraint_helper import *
from app_provider import *
from antenna.antenna_helper import *
from assertion_harness import *
from interfaces.stk_objects import *
from logger import *
from seet_helper import *
from vehicle.vehicle_basic import *
from vehicle.vehicle_gfx import *
from vehicle.vehicle_vo import *
from ansys.stk.core.stkobjects import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        EarlyBoundTests.InitHelper()

    @staticmethod
    def InitHelper():
        TestBase.LoadTestScenario(Path.Combine("MissileTests", "MissileTests.sc"))
        EarlyBoundTests.AG_MSL = Missile(TestBase.Application.current_scenario.children["Missile1"])

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_MSL = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_MSL: "Missile" = None
    # endregion

    # region AccessConstraints
    @category("AccessConstraints Tests")
    def test_AccessConstraints(self):
        oHelper = AccessConstraintHelper(self.Units)
        oHelper.DoTest(
            EarlyBoundTests.AG_MSL.access_constraints, IStkObject(EarlyBoundTests.AG_MSL), TestBase.TemporaryDirectory
        )

    # endregion

    # region STKObject
    @category("Basic Tests")
    def test_STKObject(self):
        # See 31588
        EarlyBoundTests.AG_MSL.set_trajectory_type(PropagatorType.BALLISTIC)
        Assert.assertEqual(PropagatorType.BALLISTIC, EarlyBoundTests.AG_MSL.trajectory_type)
        ballistic: "PropagatorBallistic" = PropagatorBallistic(EarlyBoundTests.AG_MSL.trajectory)
        ballistic.ephemeris_interval.set_start_and_stop_times(
            "1 Jul 1999 00:00:00.00", ballistic.ephemeris_interval.find_stop_time()
        )
        ballistic.set_impact_location_type(VehicleImpactLocation.POINT)
        point: "VehicleImpactLocationPoint" = VehicleImpactLocationPoint(ballistic.impact_location)
        point.set_launch_control_type(VehicleLaunchControl.FIXED_TIME_OF_FLIGHT)
        tof: "LaunchVehicleControlFixedTimeOfFlight" = LaunchVehicleControlFixedTimeOfFlight(point.launch_control)
        tof.time_of_flight = 9024.46
        ballistic.propagate()
        oHelper = STKObjectHelper()
        mslObject: "IStkObject" = clr.CastAs(EarlyBoundTests.AG_MSL, IStkObject)
        oHelper.Run(mslObject)
        oHelper.TestObjectFilesArray(mslObject.object_files)

    # endregion

    # region BasicDescription
    @category("Basic Tests")
    def test_BasicDescription(self):
        Assert.assertNotEqual(None, EarlyBoundTests.AG_MSL)
        obj: "IStkObject" = IStkObject(EarlyBoundTests.AG_MSL)

        # Short Description test
        obj.short_description = "This is a new short description."
        Assert.assertEqual("This is a new short description.", obj.short_description)
        obj.short_description = ""
        Assert.assertEqual("", obj.short_description)

        # Long Description test
        obj.long_description = "This is a new Long description."
        Assert.assertEqual("This is a new Long description.", obj.long_description)
        obj.long_description = ""
        Assert.assertEqual("", obj.long_description)

    # endregion

    # region BasicGroundEllipses
    @category("Basic Tests")
    def test_BasicGroundEllipses(self):
        oHelper = BasicGroundEllipsesHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.ground_ellipses, True)

    # endregion

    # region BasicAttitudeDifference
    @category("Basic Tests")
    def test_BasicAttitudeDifference(self):
        oHelper = BasicAttitudeDifferenceHelper(TestBase.Application)
        oHelper.Run(clr.CastAs(EarlyBoundTests.AG_MSL, IStkObject))

    # endregion

    # region BasicAttitude
    @category("Basic Tests")
    @category("Orientation Test")
    @category("Causes crashes")
    def test_BasicAttitude(self):
        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")
        # AttitudeType
        TestBase.logger.WriteLine6("\tThe current Attitude type is: {0}", EarlyBoundTests.AG_MSL.attitude_type)
        # AttitudeSupportedTypes
        arTypes = EarlyBoundTests.AG_MSL.attitude_supported_types
        TestBase.logger.WriteLine3("\tThe LaunchVehicle supports: {0} Attitude types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "VehicleAttitude" = VehicleAttitude(int(arTypes[iIndex][0]))
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_MSL.is_attitude_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetAttitudeType
            EarlyBoundTests.AG_MSL.set_attitude_type(eType)
            TestBase.logger.WriteLine6("\t\tThe new Attitude type is: {0}", EarlyBoundTests.AG_MSL.attitude_type)
            eType2: "VehicleAttitude" = EarlyBoundTests.AG_MSL.attitude_type
            Assert.assertEqual(eType, eType2)
            if eType == VehicleAttitude.STANDARD:
                # Attitude
                oHelper = BasicAttitudeStandardHelper(TestBase.Application)
                oHelper.Run(IVehicleAttitudeStandard(EarlyBoundTests.AG_MSL.attitude))
            elif eType == VehicleAttitude.REAL_TIME:
                oHelper = BasicAttitudeRealTimeHelper(
                    TestBase.Application, clr.CastAs(EarlyBoundTests.AG_MSL, IStkObject)
                )
                oHelper.Run(VehicleAttitudeRealTime(EarlyBoundTests.AG_MSL.attitude))
            else:
                Assert.fail("The {0} type should be supported!", eType)

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC ATTITUDE TEST ----- BEGIN -----")

    # endregion

    # region Lighting
    def test_Lighting(self):
        EarlyBoundTests.AG_MSL.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_MSL.use_terrain_in_lighting_computations)

        with pytest.raises(Exception, match=RegexSubstringMatch("read only")):
            EarlyBoundTests.AG_MSL.lighting_maximum_step = 0

        EarlyBoundTests.AG_MSL.use_terrain_in_lighting_computations = True
        Assert.assertTrue(EarlyBoundTests.AG_MSL.use_terrain_in_lighting_computations)

        # deprecated
        EarlyBoundTests.AG_MSL.lighting_maximum_step = 0
        Assert.assertEqual(0, EarlyBoundTests.AG_MSL.lighting_maximum_step)
        EarlyBoundTests.AG_MSL.lighting_maximum_step = 31557600
        Assert.assertEqual(31557600, EarlyBoundTests.AG_MSL.lighting_maximum_step)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_MSL.lighting_maximum_step = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_MSL.lighting_maximum_step = 31557601

        EarlyBoundTests.AG_MSL.lighting_maximum_step_terrain = 10
        Assert.assertEqual(10, EarlyBoundTests.AG_MSL.lighting_maximum_step_terrain)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_MSL.lighting_maximum_step_terrain = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_MSL.lighting_maximum_step_terrain = 31557601

        EarlyBoundTests.AG_MSL.use_terrain_in_lighting_computations = False
        Assert.assertFalse(EarlyBoundTests.AG_MSL.use_terrain_in_lighting_computations)
        EarlyBoundTests.AG_MSL.lighting_maximum_step_central_body_shape = 3600
        Assert.assertEqual(3600, EarlyBoundTests.AG_MSL.lighting_maximum_step_central_body_shape)
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_MSL.lighting_maximum_step_central_body_shape = -1
        with pytest.raises(Exception, match=RegexSubstringMatch("invalid")):
            EarlyBoundTests.AG_MSL.lighting_maximum_step_central_body_shape = 31557601

        Assert.assertEqual(
            10, EarlyBoundTests.AG_MSL.lighting_maximum_step_terrain
        )  # still available for get, though not settable
        EarlyBoundTests.AG_MSL.use_terrain_in_lighting_computations = True
        Assert.assertEqual(
            3600, EarlyBoundTests.AG_MSL.lighting_maximum_step_central_body_shape
        )  # still available for get, though not settable

        helper = EclipsingBodiesHelper()
        helper.Run(EarlyBoundTests.AG_MSL.eclipse_bodies)

    # endregion

    # region SpatialInfo
    @category("SpatialInfo")
    @category("Causes crashes")
    def test_SpatialInfo(self):
        helper = SpatialInfoHelper(TestBase.Application)
        helper.Run(clr.CastAs(EarlyBoundTests.AG_MSL, IStkObject))

    # endregion

    # region BasicTrajectory

    @category("Basic Tests")
    @category("OrbitState Test")
    def test_BasicTrajectory(self):
        TestBase.logger.WriteLine("----- THE BASIC TRAJECTORY TEST ----- BEGIN -----")
        self.Units.reset_units()
        # TrajectoryType
        TestBase.logger.WriteLine6(
            "The current Missile propagator type is: {0}", EarlyBoundTests.AG_MSL.trajectory_type
        )
        # TrajectorySupportedTypes
        arTypes = EarlyBoundTests.AG_MSL.trajectory_supported_types
        TestBase.logger.WriteLine3("The Missile supports: {0} propagator types", len(arTypes))

        iIndex: int = 0
        while iIndex < len(arTypes):
            eType: "PropagatorType" = PropagatorType(int(arTypes[iIndex][0]))
            TestBase.logger.WriteLine8("\tType {0} is: {1} ({2})", iIndex, arTypes[iIndex][1], eType)
            if not EarlyBoundTests.AG_MSL.is_trajectory_type_supported(eType):
                Assert.fail("The {0} type should be supported!", eType)

            # SetTrajectoryType
            EarlyBoundTests.AG_MSL.set_trajectory_type(eType)
            TestBase.logger.WriteLine6(
                "\tThe new Missile propagator type is: {0}", EarlyBoundTests.AG_MSL.trajectory_type
            )
            eType2: "PropagatorType" = EarlyBoundTests.AG_MSL.trajectory_type
            Assert.assertEqual(eType, eType2)
            # Trajectory
            oHelper = BasicPropagatorHelper(TestBase.Application)
            oHelper.Run(
                clr.CastAs(EarlyBoundTests.AG_MSL, IStkObject),
                EarlyBoundTests.AG_MSL.trajectory,
                eType,
                self.EarthGravModel,
            )

            iIndex += 1

        TestBase.logger.WriteLine("----- THE BASIC TRAJECTORY TEST ----- END -----")

    # endregion

    # region SetAttributesType
    def SetAttributesType(self, eType: "VehicleGraphics2DAttributeType"):
        oGfx: "MissileGraphics" = EarlyBoundTests.AG_MSL.graphics
        Assert.assertIsNotNone(oGfx)

        arSupportedTypes = oGfx.attributes_supported_types
        TestBase.logger.WriteLine3("Supported Types array contains: {0} elements", len(arSupportedTypes))

        iIndex: int = 0
        while iIndex < len(arSupportedTypes):
            TestBase.logger.WriteLine8(
                "The {0} supported element is: {1} ({2})",
                iIndex,
                arSupportedTypes[iIndex][1],
                VehicleGraphics2DAttributeType(int(arSupportedTypes[iIndex][0])),
            )

            iIndex += 1

        TestBase.logger.WriteLine6("The current Attributes type is: {0}", oGfx.attributes_type)
        if not oGfx.is_attributes_type_supported(eType):
            Assert.fail("The {0} type should be supported!", eType)

        oGfx.set_attributes_type(eType)
        TestBase.logger.WriteLine6("The new Attributes type is: {0}", oGfx.attributes_type)
        eType2: "VehicleGraphics2DAttributeType" = oGfx.attributes_type
        Assert.assertEqual(eType, eType2)

    # endregion

    # region GfxAttributesBasic
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesBasic(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

        self.SetAttributesType(VehicleGraphics2DAttributeType.BASIC)

        oHelper = GfxAttributesTrajectoryHelper()
        oHelper.Run(VehicleGraphics2DAttributesTrajectory(EarlyBoundTests.AG_MSL.graphics.attributes))
        EarlyBoundTests.AG_MSL.graphics.use_instance_name_label = False
        Assert.assertFalse(EarlyBoundTests.AG_MSL.graphics.use_instance_name_label)
        EarlyBoundTests.AG_MSL.graphics.label_name = "Tester"
        Assert.assertEqual("Tester", EarlyBoundTests.AG_MSL.graphics.label_name)

        EarlyBoundTests.AG_MSL.graphics.show_graphics = False
        Assert.assertFalse(EarlyBoundTests.AG_MSL.graphics.show_graphics)
        EarlyBoundTests.AG_MSL.graphics.show_graphics = True
        Assert.assertTrue(EarlyBoundTests.AG_MSL.graphics.show_graphics)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES BASIC TEST ----- BEGIN -----")

    # endregion

    # region GfxAttributesAccess
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    @category("NUNITTestFails")
    def test_GfxAttributesAccess(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        EarlyBoundTests.InitHelper()

        ac1: "Aircraft" = clr.CastAs(TestBase.Application.current_scenario.children["Boing737"], Aircraft)
        ac1.set_route_type(PropagatorType.GREAT_ARC)
        TestBase.PropagateGreatArc(clr.CastAs(ac1.route, PropagatorGreatArc))

        self.SetAttributesType(VehicleGraphics2DAttributeType.ACCESS)

        oHelper = GfxAttributesAccessHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesAccess(EarlyBoundTests.AG_MSL.graphics.attributes),
            GfxAttributesType.eTrajectory,
            TestBase.Application,
        )

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_MSL.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "VehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("1 Jul 1999 00:43:04.137", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

    # endregion

    # region GfxAttributesCustom
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesCustom(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES CUSTOM TEST ----- BEGIN -----")

        self.SetAttributesType(VehicleGraphics2DAttributeType.CUSTOM)

        # Custom Intervals
        oHelper = GfxAttributesCustomHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesCustom(EarlyBoundTests.AG_MSL.graphics.attributes), GfxAttributesType.eTrajectory
        )

        custom: "VehicleGraphics2DAttributesCustom" = clr.CastAs(
            EarlyBoundTests.AG_MSL.graphics.attributes, VehicleGraphics2DAttributesCustom
        )
        custom.intervals.add("1 Jul 1999 00:00:00.000", "1 Jul 1999 00:01:00.000")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_MSL.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "VehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("1 Jul 1999 00:01:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES CUSTOM TEST ----- END -----")

    # endregion

    # region GfxAttributesTimeComponents
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesTimeComponents(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- BEGIN -----")

        self.SetAttributesType(VehicleGraphics2DAttributeType.TIME_COMPONENTS)

        oHelper = GfxAttributesTimeComponentsHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesTimeComponents(EarlyBoundTests.AG_MSL.graphics.attributes),
            GfxAttributesType.eTrajectory,
            TestBase.Application,
        )

        gfxAttrTimeComp: "VehicleGraphics2DAttributesTimeComponents" = clr.CastAs(
            EarlyBoundTests.AG_MSL.graphics.attributes, VehicleGraphics2DAttributesTimeComponents
        )
        gfxAttrTimeComp.time_components.add("Scenario/Scenario1 AnalysisInterval EventInterval")

        displayState: "IVehicleGraphics2DAttributesDisplayState" = clr.CastAs(
            EarlyBoundTests.AG_MSL.graphics.attributes, IVehicleGraphics2DAttributesDisplayState
        )
        intColl: "VehicleGraphics2DIntervalsCollection" = displayState.get_display_intervals()
        interval: "VehicleGraphics2DInterval" = intColl[0]
        Assert.assertEqual("1 Jul 1999 00:00:00.000", interval.start_time)
        Assert.assertEqual("2 Jul 1999 00:00:00.000", interval.stop_time)

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES ACCESS TEST ----- END -----")

    # endregion

    # region GfxAttributesRealTime
    @category("Graphics Tests")
    @category("GraphicsTests.Attributes")
    def test_GfxAttributesRealTime(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- BEGIN -----")
        if EarlyBoundTests.AG_MSL.trajectory_type != PropagatorType.REAL_TIME:
            bCaught: bool = False
            try:
                bCaught = False
                self.SetAttributesType(VehicleGraphics2DAttributeType.REAL_TIME)

            except Exception as e:
                bCaught = True
                TestBase.logger.WriteLine5("Expected exception: {0}", str(e))

            if not bCaught:
                Assert.fail("The SetAttributesType should not allow to set REAL_TIME value!")

        EarlyBoundTests.AG_MSL.set_trajectory_type(PropagatorType.REAL_TIME)
        (clr.CastAs(EarlyBoundTests.AG_MSL.trajectory, PropagatorRealtime)).propagate()
        self.SetAttributesType(VehicleGraphics2DAttributeType.REAL_TIME)

        oHelper = GfxAttributesRealTimeHelper()
        oHelper.Run(
            VehicleGraphics2DAttributesRealtime(EarlyBoundTests.AG_MSL.graphics.attributes),
            GfxAttributesType.eTrajectory,
        )

        TestBase.logger.WriteLine("----- THE GRAPHICS ATTRIBUTES REAL TIME TEST ----- END -----")

    # endregion

    # region GfxResolution
    @category("Graphics Tests")
    def test_GfxResolution(self):
        oHelper = GfxTrajectoryResolutionHelper()
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics.resolution)

    # endregion

    # region GfxGroundEllipses
    @category("Graphics Tests")
    def test_GfxGroundEllipses(self):
        EarlyBoundTests.InitHelper()
        oBGEHelper = BasicGroundEllipsesHelper(self.Units)
        oBGEHelper.Run(EarlyBoundTests.AG_MSL.ground_ellipses, False)

        oGGEHelper = GfxGroundEllipsesHelper()
        oGGEHelper.Run(EarlyBoundTests.AG_MSL.graphics.ground_ellipses)

    # endregion

    # region GfxElevationContours
    @category("Graphics Tests")
    def test_GfxElevationContours(self):
        oHelper = GfxElevationContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics.elevation_contours)

    # endregion

    # region GfxTrajectory
    @category("Graphics Tests")
    @category("Trail/Lead (2D)")
    def test_GfxTrajectory(self):
        TestBase.logger.WriteLine("----- THE GRAPHICS TRAJECTORY TEST ----- BEGIN -----")

        # GroundTrack
        oHelper = GfxLeadTrailDataHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics.pass_data.ground_track)

        # Trajectory
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics.pass_data.trajectory)

        TestBase.logger.WriteLine("----- THE GRAPHICS TRAJECTORY TEST ----- END -----")

    # endregion

    # region GfxLabelNotes
    @category("Graphics Tests")
    def test_GfxLabelNotes(self):
        oHelper = GfxLabelNoteHelper(TestBase.Application.units_preferences)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics.label_notes)

    # endregion

    # region GfxRangeContours
    @category("Graphics Tests")
    def test_GfxRangeContours(self):
        oHelper = GfxRangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics.range_contours)

    # endregion

    # region GfxSwath
    @category("Graphics Tests")
    def test_GfxSwath(self):
        oHelper = GfxSwathHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics.swath)

    # endregion

    # region GfxLighting
    @category("Graphics Tests")
    def test_GfxLighting(self):
        oHelper = GfxLightingHelper()
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics.lighting)

    # endregion

    # region VOModel
    @category("VO Tests")
    def test_VOModel(self):
        oHelper = VOTrajectoryModelHelper(clr.CastAs(TestBase.Application, StkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.model, False)

    # endregion

    # region VOModelMarker
    @category("VO Tests")
    def test_VOModelMarker(self):
        oHelper = VOMarkerHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.model.ground_marker, True)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.model.trajectory_marker, True)

    # endregion

    # region VOProximity
    @category("VO Tests")
    def test_VOProximity(self):
        oHelper = VOTrajectoryProximityHelper(clr.CastAs(TestBase.Application, StkObjectRoot), self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.proximity)

    # endregion

    # region VOElevationContours
    @category("VO Tests")
    def test_VOElevationContours(self):
        oHelper = VOElevationContoursHelper()
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.elevation_contours)

    # endregion

    # region VOCovariancePointingContour
    @category("VO Tests")
    def test_VOCovariancePointingContour(self):
        oHelper = VOCovariancePointingContourHelper()
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.covariance_pointing_contour)

    # endregion

    # region VORangeContours
    @category("VO Tests")
    def test_VORangeContours(self):
        oHelper = VORangeContoursHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.range_contours)

    # endregion

    # region VOOffsets
    @category("VO Tests")
    def test_VOOffsets(self):
        oHelper = VOOffsetsHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.offsets)

    # endregion

    # region VOCovariance
    @category("VO Tests")
    def test_VOCovariance(self):
        oHelper = VOCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.covariance)

    # endregion

    # region VOVelocityCovariance
    @category("VO Tests")
    def test_VOVelocityCovariance(self):
        oHelper = VOVelocityCovarianceHelper()
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.velocity_covariance)

    # endregion

    # region VOVectors
    @category("VO Tests")
    def test_VOVectors(self):
        oHelper = VOVectorsHelper(self.Units, TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.vector, False)

    # endregion

    # region VODataDisplay
    @category("VO Tests")
    @category("DataDisplay Test")
    def test_VODataDisplay(self):
        # test VO DataDisplay
        oHelper = VODataDisplayHelper(TestBase.Application)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.data_display, False, False)

    # endregion

    # region VOModelPointing
    @category("VO Tests")
    def test_VOModelPointing(self):
        # set VO.Model type to FILE
        oModel: "IGraphics3DModel" = EarlyBoundTests.AG_MSL.graphics_3d.model
        TestBase.logger.WriteLine6("The current ModelType is: {0}", oModel.model_type)
        oModel.model_type = ModelType.FILE
        TestBase.logger.WriteLine6("The new ModelType is: {0}", oModel.model_type)
        Assert.assertEqual(ModelType.FILE, oModel.model_type)
        # set new ModelFile.Filename
        oModelFile: "Graphics3DModelFile" = Graphics3DModelFile(oModel.model_data)
        Assert.assertIsNotNone(oModelFile)
        TestBase.logger.WriteLine5("\tThe current Filename is: {0}", oModelFile.filename)
        oModelFile.filename = TestBase.GetScenarioFile("VO", "Models", "m1a1.mdl")
        TestBase.logger.WriteLine5("\tThe new Filename is: {0}", oModelFile.filename)
        # test ModelPointing
        oHelper = VOModelPointingHelper()
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.model_pointing)

    # endregion

    # region VODropLines
    @category("VO Tests")
    def test_VODropLines(self):
        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- BEGIN -----")
        oVO: "MissileGraphics3D" = EarlyBoundTests.AG_MSL.graphics_3d
        Assert.assertIsNotNone(oVO)
        oDropLines: "VehicleGraphics3DTrajectoryDropLines" = oVO.drop_lines
        Assert.assertIsNotNone(oDropLines)

        # Trajectory test
        oPathHelper = VODropLinePathItemCollectionHelper()
        oPathHelper.Run(oDropLines.trajectory)

        # Position test
        oPosHelper = VODropLinePosItemCollectionHelper()
        oPosHelper.Run(oDropLines.position)

        TestBase.logger.WriteLine("----- THE VO DROP LINES TEST ----- END -----")

    # endregion

    # region VOTrajectory
    @category("VO Tests")
    @category("Trail/Lead (3D)")
    def test_VOTrajectory(self):
        oHelper = VOTrajectoryHelper(self.Units)
        oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.trajectory)

    # endregion

    # region VOTrajectorySystems
    @category("VO Tests")
    def test_VOTrajectorySystems(self):
        oHelper = VOSystemsHelper()
        if TestBase.ApplicationProvider.Target == TestTarget.eStk:
            oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.trajectory_systems, TestBase.Application)

        else:
            oHelper.Run(EarlyBoundTests.AG_MSL.graphics_3d.trajectory_systems, None)

    # endregion

    # region VOVaporTrail
    @category("VO Tests")
    def test_VOVaporTrail(self):
        oHelper = VOVaporTrailHelper()
        oHelper.Run(
            EarlyBoundTests.AG_MSL.graphics_3d.vapor_trail,
            clr.CastAs(EarlyBoundTests.AG_MSL.graphics_3d.model, IGraphics3DModel),
            TestBase.GetSTKHomeDir(),
        )

    # endregion

    # region ExportToDataFile
    def test_ExportToDataFile(self):
        ms: "Missile" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.MISSILE, "ExportMs"), Missile
        )
        ball: "PropagatorBallistic" = clr.CastAs(ms.trajectory, PropagatorBallistic)
        impactLocation: "VehicleImpactLocationPoint" = clr.CastAs(ball.impact_location, VehicleImpactLocationPoint)
        impact: "VehicleImpactLocationDetic" = clr.CastAs(impactLocation.impact, VehicleImpactLocationDetic)
        impact.latitude = -20
        impact.longitude = -20
        ball.step = 56
        ball.propagate()

        exportHelper = ExportDataFileHelper(IStkObject(ms), TestBase.Application)
        exportHelper.AttitudeExportTool(ms.export_tools.get_attitude_export_tool())
        exportHelper.EphemerisSTKExportTool(ms.export_tools.get_ephemeris_stk_export_tool(), False)
        exportHelper.PropDefExportTool(ms.export_tools.get_propagator_definition_export_tool())
        exportHelper.EphemerisStkBinaryExportTool(ms.export_tools.get_ephemeris_stk_binary_export_tool(), False)

        TestBase.Application.current_scenario.children.unload(STKObjectType.MISSILE, "ExportMs")

    # endregion

    # region SEET_Environment
    @category("SEET")
    def test_SEET_Environment(self):
        SEETHelper.TestEnvironment(EarlyBoundTests.AG_MSL.space_environment)

    # endregion

    # region SEET_Thermal
    @category("SEET")
    def test_SEET_Thermal(self):
        SEETHelper.TestThermal(EarlyBoundTests.AG_MSL.space_environment)

    # endregion

    # region SEET_ParticleFlux
    @category("SEET")
    def test_SEET_ParticleFlux(self):
        SEETHelper.TestParticleFlux(EarlyBoundTests.AG_MSL.space_environment)

    # endregion

    # region SEET_Radiation
    @category("SEET")
    def test_SEET_Radiation(self):
        SEETHelper.TestRadiation(EarlyBoundTests.AG_MSL.space_environment)

    # endregion

    # region SEET_Environment_2D
    @category("SEET")
    @category("Graphics Tests")
    def test_SEET_Environment_2D(self):
        SEETHelper.TestEnvironment_2D(
            EarlyBoundTests.AG_MSL.space_environment,
            EarlyBoundTests.AG_MSL.graphics.saa,
            EarlyBoundTests.AG_MSL.graphics_3d.saa,
        )

    # endregion

    # region RF_Atmosphere_AtmosphericAbsorptionModel
    def test_RF_Atmosphere_AtmosphericAbsorptionModel(self):
        helper = AtmosphereHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_MSL.atmosphere)

    # endregion

    # region RF_Atmosphere_LocalRainData
    def test_RF_Atmosphere_LocalRainData(self):
        helper = AtmosphereLocalRainDataHelper()
        helper.Run(EarlyBoundTests.AG_MSL.atmosphere, TestBase.Application)

    # endregion

    # region RF_Radar_Clutter
    def test_RF_Radar_Clutter(self):
        helper = RadarClutterMapInheritableHelper()
        with pytest.raises(Exception, match=RegexSubstringMatch("obsolete")):
            helper.Run(EarlyBoundTests.AG_MSL.radar_clutter_map)

    # endregion

    # region RF_RadarCrossSection
    def test_RF_RadarCrossSection(self):
        helper = RadarCrossSectionInheritableHelper()
        helper.Run(EarlyBoundTests.AG_MSL.radar_cross_section)
        helper.Run_DeprecatedModelInterface(EarlyBoundTests.AG_MSL.radar_cross_section)

    # endregion

    # region Laser_Environment_AtmosphericLoss_BBLL
    def test_Laser_Environment_AtmosphericLoss_BBLL(self):
        helper = PlatformLaserEnvAtmosLossBBLLHelper()
        helper.Run(EarlyBoundTests.AG_MSL.laser_environment)

    # endregion

    # region Laser_Environment_AtmosphericLoss_Modtran
    def test_Laser_Environment_AtmosphericLoss_Modtran(self):
        helper = PlatformLaserEnvAtmosLossModtranHelper()
        helper.Run(EarlyBoundTests.AG_MSL.laser_environment)

    # endregion

    # region Laser_Environment_TroposphericScintillationLoss
    def test_Laser_Environment_TroposphericScintillationLoss(self):
        helper = PlatformLaserEnvTropoScintLossHelper()
        helper.Run(EarlyBoundTests.AG_MSL.laser_environment)

    # endregion

    # region RF_Environment_EnvironmentalData
    def test_RF_Environment_EnvironmentalData(self):
        helper = PlatformRF_Environment_EnvironmentalDataHelper()
        helper.Run(EarlyBoundTests.AG_MSL.rf_environment)

    # endregion

    # region RF_Environment_RainCloudFog_RainModel
    def test_RF_Environment_RainCloudFog_RainModel(self):
        helper = PlatformRF_Environment_RainCloudFog_RainModelHelper()
        helper.Run(EarlyBoundTests.AG_MSL.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_RainCloudFog_CloudsAndFogModel
    def test_RF_Environment_RainCloudFog_CloudsAndFogModel(self):
        helper = PlatformRF_Environment_RainCloudFog_CloudsAndFogModelHelper()
        helper.Run(EarlyBoundTests.AG_MSL.rf_environment, TestBase.Application)

    # endregion

    # region RF_Environment_AtmosphericAbsorption
    def test_RF_Environment_AtmosphericAbsorption(self):
        helper = PlatformRF_Environment_AtmosphericAbsorptionHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_MSL.rf_environment)

    # endregion

    # region RF_Environment_UrbanAndTerrestrial
    def test_RF_Environment_UrbanAndTerrestrial(self):
        helper = PlatformRF_Environment_UrbanAndTerrestrialHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_MSL.rf_environment, True)

    # endregion

    # region RF_Environment_TropoScintillation
    def test_RF_Environment_TropoScintillation(self):
        helper = PlatformRF_Environment_TropoScintillationHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_MSL.rf_environment)

    # endregion

    # region RF_Environment_CustomModels
    def test_RF_Environment_CustomModels(self):
        helper = PlatformRF_Environment_CustomModelsHelper(TestBase.Application)
        helper.Run(EarlyBoundTests.AG_MSL.rf_environment)

    # endregion
