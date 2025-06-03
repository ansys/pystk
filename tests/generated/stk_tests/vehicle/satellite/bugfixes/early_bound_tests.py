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
from parameterized import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.analysis_workbench import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    AG_SAT: "Satellite" = None

    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("SatelliteTests", "SatelliteTests.sc"))
        EarlyBoundTests.AG_SAT = Satellite(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "Satellite2")
        )
        EarlyBoundTests.AG_SAT.set_propagator_type(PropagatorType.TWO_BODY)
        (PropagatorTwoBody(EarlyBoundTests.AG_SAT.propagator)).propagate()

    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SAT = None
        TestBase.Uninitialize()

    def setUp(self):
        TestBase.Application.units_preferences.set_current_unit("AngleUnit", "deg")
        TestBase.Application.units_preferences.set_current_unit("LatitudeUnit", "deg")
        TestBase.Application.units_preferences.set_current_unit("LongitudeUnit", "deg")
        if not TestBase.NoGraphicsMode:
            EarlyBoundTests.AG_SAT.graphics.time_events.remove_all()

        else:
            with pytest.raises(Exception, match=RegexSubstringMatch("NoGraphics property is set to true")):
                EarlyBoundTests.AG_SAT.graphics.time_events.remove_all()

    def test_BUG63355_ExceptionOnBreakAngleTypeUnknown(self):
        def code1():
            EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VehicleBreakAngleType.UNKNOWN)

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("Invalid", str(ex), "Exception message mismatch")

    @category("VO Tests")
    def test_PLAT_40277_IAgVORefCrdnCollection_input_formats(self):
        refColl: "Graphics3DReferenceVectorGeometryToolComponentCollection" = (
            EarlyBoundTests.AG_SAT.graphics_3d.vector.vector_geometry_tool_components
        )

        # Axes

        refColl.add(GeometricElementType.AXES_ELEMENT, "Satellite/Satellite2 Equinoctial Axes")  # full name
        refColl.add(GeometricElementType.AXES_ELEMENT, "ICR Axes")  # short name

        refCrdn: "IGraphics3DReferenceAnalysisWorkbenchComponent" = refColl.get_component_by_name(
            GeometricElementType.AXES_ELEMENT, "Satellite/Satellite2 Equinoctial Axes"
        )
        Assert.assertEqual("Satellite/Satellite2 Equinoctial Axes", refCrdn.name)

        refCrdn = refColl.get_component_by_name(GeometricElementType.AXES_ELEMENT, "Equinoctial Axes")
        Assert.assertEqual("Satellite/Satellite2 Equinoctial Axes", refCrdn.name)

        refCrdn = refColl.get_component_by_name(GeometricElementType.AXES_ELEMENT, "Satellite/Satellite2 ICR Axes")
        Assert.assertEqual("Satellite/Satellite2 ICR Axes", refCrdn.name)

        refCrdn = refColl.get_component_by_name(GeometricElementType.AXES_ELEMENT, "ICR Axes")
        Assert.assertEqual("Satellite/Satellite2 ICR Axes", refCrdn.name)

        refColl.remove_by_name(GeometricElementType.AXES_ELEMENT, "Satellite/Satellite2 Equinoctial Axes")
        refColl.remove_by_name(GeometricElementType.AXES_ELEMENT, "Satellite/Satellite2 ICR Axes")

        # Vectors

        refColl.add(GeometricElementType.VECTOR_ELEMENT, "Satellite/Satellite2 AngMomentum Vector")  # full name
        refColl.add(GeometricElementType.VECTOR_ELEMENT, "AngVelocity Vector")  # short name

        refCrdn = refColl.get_component_by_name(
            GeometricElementType.VECTOR_ELEMENT, "Satellite/Satellite2 AngMomentum Vector"
        )
        Assert.assertEqual("Satellite/Satellite2 AngMomentum Vector", refCrdn.name)

        refCrdn = refColl.get_component_by_name(GeometricElementType.VECTOR_ELEMENT, "AngMomentum Vector")
        Assert.assertEqual("Satellite/Satellite2 AngMomentum Vector", refCrdn.name)

        refCrdn = refColl.get_component_by_name(
            GeometricElementType.VECTOR_ELEMENT, "Satellite/Satellite2 AngVelocity Vector"
        )
        Assert.assertEqual("Satellite/Satellite2 AngVelocity Vector", refCrdn.name)

        refCrdn = refColl.get_component_by_name(GeometricElementType.VECTOR_ELEMENT, "AngVelocity Vector")
        Assert.assertEqual("Satellite/Satellite2 AngVelocity Vector", refCrdn.name)

        refColl.remove_by_name(GeometricElementType.VECTOR_ELEMENT, "Satellite/Satellite2 AngMomentum Vector")
        refColl.remove_by_name(GeometricElementType.VECTOR_ELEMENT, "Satellite/Satellite2 AngVelocity Vector")

    def test_BUG62983_BUG67662_StkExternalOverride(self):
        # Improper default value of false for PropagatorSTKExternal.Override
        satellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "StkExternalSatellite1"),
            Satellite,
        )
        satellite.set_propagator_type(PropagatorType.STK_EXTERNAL)
        prop: "PropagatorSTKExternal" = clr.CastAs(satellite.propagator, PropagatorSTKExternal)
        prop.filename = TestBase.GetScenarioFile("External", "Satellite1.e")
        prop.propagate()
        Assert.assertEqual("9 Sep 2009 16:00:00.000", prop.start_time)
        Assert.assertEqual("10 Sep 2009 16:00:00.000", prop.stop_time)
        # Verify that the "Override" flag is set to false by default.
        Assert.assertFalse(prop.override)

    def test_BUG67722_SGP4SatelliteDuration(self):
        sat2: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "sat2"), Satellite
        )
        sat2.set_propagator_type(PropagatorType.SGP4)
        prop2: "PropagatorSGP4" = clr.CastAs(sat2.propagator, PropagatorSGP4)
        prop2.propagate()
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        Assert.assertEqual(scenario.start_time, prop2.ephemeris_interval.find_start_time())
        Assert.assertEqual(scenario.stop_time, prop2.ephemeris_interval.find_stop_time())
        TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "sat2")

    def test_BUG65831_VectorConstraints(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "BUG65831"), Satellite
        )
        sat.set_propagator_type(PropagatorType.SGP4)
        sgp4: "PropagatorSGP4" = clr.CastAs(sat.propagator, PropagatorSGP4)
        sgp4.propagate()
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        cnstrAngle: "AccessConstraintAnalysisWorkbenchComponent" = clr.CastAs(
            sat.access_constraints.add_constraint(AccessConstraintType.VECTOR_GEOMETRY_TOOL_ANGLE),
            AccessConstraintAnalysisWorkbenchComponent,
        )
        Assert.assertEqual("Satellite/BUG65831 VelocityAzimuth Angle", cnstrAngle.reference)

        cnstrCondition: "AccessConstraintAnalysisWorkbenchComponent" = clr.CastAs(
            sat.access_constraints.add_constraint(AccessConstraintType.CONDITION),
            AccessConstraintAnalysisWorkbenchComponent,
        )
        Assert.assertEqual("Satellite/BUG65831 AfterStart Condition", cnstrCondition.reference)

        cnstrVectorMag: "AccessConstraintAnalysisWorkbenchComponent" = clr.CastAs(
            sat.access_constraints.add_constraint(AccessConstraintType.VECTOR_MAGNITUDE),
            AccessConstraintAnalysisWorkbenchComponent,
        )
        Assert.assertEqual("Satellite/BUG65831 Velocity Vector", cnstrVectorMag.reference)

        TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "BUG65831")

    # [Test]
    # public void BUG68243_CoordinateEpoch()
    # {
    #    Satellite sat = Application.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "BUG68243") as Satellite;
    #    sat.SetPropagatorType(AgEVePropagatorType.J2_PERTURBATION);
    #    PropagatorJ2Perturbation j2prop = sat.Propagator as PropagatorJ2Perturbation;

    #    OrbitStateCartesian cart = (OrbitStateCartesian)j2prop.InitialState.Representation.ConvertTo(
    #        AgEOrbitStateType.CARTESIAN);

    #    cart.CoordinateSystemType = AgECoordinateSystem.MEAN_OF_EPOCH;
    #    OrbitStateCoordinateSystem coordsys = (OrbitStateCoordinateSystem)cart.CoordinateSystem;
    #    ITimeToolInstant referenceEvent = Application.CurrentScenario.Vgt.Events["AnalysisStartTime"];
    #    cart.CoordinateSystem.CoordinateSystemEpoch.SetImplicitTime(referenceEvent);

    #    j2prop.InitialState.Representation.Assign(cart);
    #    j2prop.Propagate();

    #    Application.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "BUG68243");
    # }

    @category("Graphics Tests")
    def test_BUG86580_AddSingleGfxTimeEvent(self):
        timeEvent: "VehicleGraphics2DTimeEventsElement" = EarlyBoundTests.AG_SAT.graphics.time_events.add()

        Assert.assertEqual(timeEvent.time_event_type, VehicleGraphics2DTimeEventType.MARKER)

        data: "VehicleGraphics2DTimeEventTypeMarker" = VehicleGraphics2DTimeEventTypeMarker(
            timeEvent.time_event_type_data
        )
        Assert.assertEqual("TimeEvent1", data.unique_identifer)

    @category("Graphics Tests")
    def test_BUG86580_AddTwoGfxTimeEvents(self):
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        timeEvent: "VehicleGraphics2DTimeEventsElement" = EarlyBoundTests.AG_SAT.graphics.time_events.add()

        Assert.assertEqual(2, EarlyBoundTests.AG_SAT.graphics.time_events.count)

        Assert.assertEqual(timeEvent.time_event_type, VehicleGraphics2DTimeEventType.MARKER)

        data: "VehicleGraphics2DTimeEventTypeMarker" = VehicleGraphics2DTimeEventTypeMarker(
            timeEvent.time_event_type_data
        )
        Assert.assertEqual("TimeEvent2", data.unique_identifer)

    @category("Graphics Tests")
    def test_BUG86580_AddThreeRemoveOneAddOneGfxTimeEvents(self):
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        EarlyBoundTests.AG_SAT.graphics.time_events.remove_at(0)

        timeEvent: "VehicleGraphics2DTimeEventsElement" = EarlyBoundTests.AG_SAT.graphics.time_events.add()

        Assert.assertEqual(3, EarlyBoundTests.AG_SAT.graphics.time_events.count)

        Assert.assertEqual(timeEvent.time_event_type, VehicleGraphics2DTimeEventType.MARKER)

        data: "VehicleGraphics2DTimeEventTypeMarker" = VehicleGraphics2DTimeEventTypeMarker(
            timeEvent.time_event_type_data
        )
        Assert.assertEqual("TimeEvent1", data.unique_identifer)

    @category("Graphics Tests")
    def test_BUG112927_IAgVORefCrdnAngle_ShowDihedralAngleSupportingArcs(self):
        TestBase.Application.analysis_workbench_components_root.get_provider(
            "Satellite/Satellite1"
        ).angles.factory.create("BUG112927_Dihedral", "", AngleType.DIHEDRAL_ANGLE)
        dihedral: "Graphics3DReferenceAngle" = clr.CastAs(
            EarlyBoundTests.AG_SAT.graphics_3d.vector.vector_geometry_tool_components.add(
                GeometricElementType.ANGLE_ELEMENT, "Satellite/Satellite1 BUG112927_Dihedral Angle"
            ),
            Graphics3DReferenceAngle,
        )

        dihedral.visible = False
        Assert.assertFalse(dihedral.visible)
        dihedral.visible = True
        Assert.assertTrue(dihedral.visible)

        dihedral.show_label = False
        Assert.assertFalse(dihedral.show_label)
        dihedral.show_label = True
        Assert.assertTrue(dihedral.show_label)

        dihedral.show_angle_value = False
        Assert.assertFalse(dihedral.show_angle_value)
        dihedral.show_angle_value = True
        Assert.assertTrue(dihedral.show_angle_value)

        dihedral.show_dihedral_angle_supporting_arcs = False
        Assert.assertFalse(dihedral.show_dihedral_angle_supporting_arcs)
        dihedral.show_dihedral_angle_supporting_arcs = True
        Assert.assertTrue(dihedral.show_dihedral_angle_supporting_arcs)

    def test_BUG119916_StoppingConditions_MaxTripTimes(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "BUG119916"), Satellite
        )
        sat.set_propagator_type(PropagatorType.ASTROGATOR)

        mcs: "MCSDriver" = clr.CastAs(sat.propagator, MCSDriver)
        propagate: "MCSPropagate" = clr.CastAs(mcs.main_sequence.get_item_by_name("Propagate"), MCSPropagate)

        stopCond: "StoppingCondition" = clr.CastAs(
            propagate.stopping_conditions["Duration"].properties, StoppingCondition
        )
        with pytest.raises(Exception, match=RegexSubstringMatch("read-only")):  # read-only without a Sequence set
            stopCond.max_trip_times = 10001

        mcs.auto_sequence.add("AutoSeq1")
        stopCond.sequence = "AutoSeq1"
        stopCond.max_trip_times = 10001
        Assert.assertEqual(10001, stopCond.max_trip_times)  # settable when a Sequence is set

        TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "BUG119916")

    def test_FEA119646_CCSDS_CB_and_RefFrames(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "FEA119646"), Satellite
        )
        sat.set_propagator_type(PropagatorType.TWO_BODY)
        twoBody: "PropagatorTwoBody" = clr.CastAs(sat.propagator, PropagatorTwoBody)
        twoBody.propagate()

        exportTool: "VehicleEphemerisCCSDSExportTool" = sat.export_tools.get_ephemeris_ccsds_export_tool()
        exportTool.originator = "originator"
        exportTool.object_identifier = "objectid"
        outputFile: str = TestBase.GetScenarioFile("test.out")

        exportTool.central_body_name = "Earth"

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.EME2000,
            CCSDSReferenceFrame.FIXED,
            CCSDSReferenceFrame.ICRF,
            CCSDSReferenceFrame.ITRF,
            CCSDSReferenceFrame.ITRF2000,
            CCSDSReferenceFrame.ITRF2005,
            CCSDSReferenceFrame.ITRF2008,
            CCSDSReferenceFrame.ITRF2014,
            CCSDSReferenceFrame.ITRF2020,
            CCSDSReferenceFrame.TEME_OF_DATE,
            CCSDSReferenceFrame.TOD,
            CCSDSReferenceFrame.GCRF,
        ]:
            exportTool.reference_frame = refFrame
            exportTool.export(outputFile)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            exportTool.reference_frame = CCSDSReferenceFrame.MEAN_EARTH

        exportTool.central_body_name = "Moon"

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.EME2000,
            CCSDSReferenceFrame.FIXED,
            CCSDSReferenceFrame.ICRF,
            CCSDSReferenceFrame.MEAN_EARTH,
            CCSDSReferenceFrame.TOD,
        ]:
            exportTool.reference_frame = refFrame
            exportTool.export(outputFile)

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.ITRF,
            CCSDSReferenceFrame.ITRF2000,
            CCSDSReferenceFrame.ITRF2005,
            CCSDSReferenceFrame.ITRF2008,
            CCSDSReferenceFrame.ITRF2014,
            CCSDSReferenceFrame.ITRF2020,
            CCSDSReferenceFrame.TEME_OF_DATE,
            CCSDSReferenceFrame.GCRF,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.reference_frame = refFrame

        exportTool.central_body_name = "Mars"

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.EME2000,
            CCSDSReferenceFrame.FIXED,
            CCSDSReferenceFrame.ICRF,
            CCSDSReferenceFrame.TOD,
        ]:
            exportTool.reference_frame = refFrame
            exportTool.export(outputFile)

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.MEAN_EARTH,
            CCSDSReferenceFrame.ITRF,
            CCSDSReferenceFrame.ITRF2000,
            CCSDSReferenceFrame.ITRF2005,
            CCSDSReferenceFrame.ITRF2008,
            CCSDSReferenceFrame.ITRF2014,
            CCSDSReferenceFrame.ITRF2020,
            CCSDSReferenceFrame.TEME_OF_DATE,
            CCSDSReferenceFrame.GCRF,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.reference_frame = refFrame

        #
        # Do the same as above with CCSDSv2
        #

        exportToolv2: "VehicleEphemerisCCSDSv2ExportTool" = sat.export_tools.get_ephemeris_ccsds_v2_export_tool()
        exportToolv2.originator = "originator"
        exportToolv2.object_identifier = "objectid"
        outputFile = TestBase.GetScenarioFile("test.out")

        exportToolv2.central_body_name = "Earth"

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.EME2000,
            CCSDSReferenceFrame.FIXED,
            CCSDSReferenceFrame.ICRF,
            CCSDSReferenceFrame.ITRF,
            CCSDSReferenceFrame.ITRF2000,
            CCSDSReferenceFrame.ITRF2005,
            CCSDSReferenceFrame.ITRF2008,
            CCSDSReferenceFrame.ITRF2014,
            CCSDSReferenceFrame.ITRF2020,
            CCSDSReferenceFrame.TEME_OF_DATE,
            CCSDSReferenceFrame.TOD,
            CCSDSReferenceFrame.GCRF,
        ]:
            exportToolv2.reference_frame = refFrame
            exportToolv2.export(outputFile)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            exportToolv2.reference_frame = CCSDSReferenceFrame.MEAN_EARTH

        exportToolv2.central_body_name = "Moon"

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.EME2000,
            CCSDSReferenceFrame.FIXED,
            CCSDSReferenceFrame.ICRF,
            CCSDSReferenceFrame.MEAN_EARTH,
            CCSDSReferenceFrame.TOD,
        ]:
            exportToolv2.reference_frame = refFrame
            exportToolv2.export(outputFile)

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.ITRF,
            CCSDSReferenceFrame.ITRF2000,
            CCSDSReferenceFrame.ITRF2005,
            CCSDSReferenceFrame.ITRF2008,
            CCSDSReferenceFrame.ITRF2014,
            CCSDSReferenceFrame.ITRF2020,
            CCSDSReferenceFrame.TEME_OF_DATE,
            CCSDSReferenceFrame.GCRF,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportToolv2.reference_frame = refFrame

        exportToolv2.central_body_name = "Mars"

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.EME2000,
            CCSDSReferenceFrame.FIXED,
            CCSDSReferenceFrame.ICRF,
            CCSDSReferenceFrame.TOD,
        ]:
            exportToolv2.reference_frame = refFrame
            exportToolv2.export(outputFile)

        refFrame: "CCSDSReferenceFrame"

        for refFrame in [
            CCSDSReferenceFrame.MEAN_EARTH,
            CCSDSReferenceFrame.ITRF,
            CCSDSReferenceFrame.ITRF2000,
            CCSDSReferenceFrame.ITRF2005,
            CCSDSReferenceFrame.ITRF2008,
            CCSDSReferenceFrame.ITRF2014,
            CCSDSReferenceFrame.ITRF2020,
            CCSDSReferenceFrame.TEME_OF_DATE,
            CCSDSReferenceFrame.GCRF,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportToolv2.reference_frame = refFrame

        TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "FEA119646")

    def test_FEA119465_STKEphem_CB_and_RefFrames(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "FEA119465"), Satellite
        )
        sat.set_propagator_type(PropagatorType.TWO_BODY)
        twoBody: "PropagatorTwoBody" = clr.CastAs(sat.propagator, PropagatorTwoBody)
        twoBody.propagate()

        outputFile: str = TestBase.GetScenarioFile("test.out")

        # STK Binary Ephemeris

        exportTool: "VehicleEphemerisExportTool" = sat.export_tools.get_ephemeris_stk_export_tool()
        exportTool.use_vehicle_central_body = False

        exportTool.central_body_name = "Earth"

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.INERTIAL,
            EphemerisCoordinateSystemType.FIXED,
            EphemerisCoordinateSystemType.J2000,
            EphemerisCoordinateSystemType.ICRF,
            EphemerisCoordinateSystemType.TRUE_OF_DATE,
            EphemerisCoordinateSystemType.TEME_OF_DATE,
            EphemerisCoordinateSystemType.ITRF2000,
            EphemerisCoordinateSystemType.ITRF2005,
            EphemerisCoordinateSystemType.ITRF2008,
            EphemerisCoordinateSystemType.ITRF2014,
            EphemerisCoordinateSystemType.ITRF2020,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [EphemerisCoordinateSystemType.MEAN_EARTH]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        exportTool.central_body_name = "Moon"

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.FIXED,
            EphemerisCoordinateSystemType.INERTIAL,
            EphemerisCoordinateSystemType.J2000,
            EphemerisCoordinateSystemType.ICRF,
            EphemerisCoordinateSystemType.TRUE_OF_DATE,
            EphemerisCoordinateSystemType.MEAN_EARTH,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.TEME_OF_DATE,
            EphemerisCoordinateSystemType.ITRF2000,
            EphemerisCoordinateSystemType.ITRF2005,
            EphemerisCoordinateSystemType.ITRF2008,
            EphemerisCoordinateSystemType.ITRF2014,
            EphemerisCoordinateSystemType.ITRF2020,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        exportTool.central_body_name = "Mars"

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.FIXED,
            EphemerisCoordinateSystemType.INERTIAL,
            EphemerisCoordinateSystemType.J2000,
            EphemerisCoordinateSystemType.ICRF,
            EphemerisCoordinateSystemType.TRUE_OF_DATE,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.MEAN_EARTH,
            EphemerisCoordinateSystemType.TEME_OF_DATE,
            EphemerisCoordinateSystemType.ITRF2000,
            EphemerisCoordinateSystemType.ITRF2005,
            EphemerisCoordinateSystemType.ITRF2008,
            EphemerisCoordinateSystemType.ITRF2014,
            EphemerisCoordinateSystemType.ITRF2020,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        #
        # Do the same with STK Binary Ephemeris
        #

        exportTool2: "VehicleEphemerisBinaryExportTool" = sat.export_tools.get_ephemeris_stk_binary_export_tool()
        exportTool2.use_vehicle_central_body = False

        exportTool2.central_body_name = "Earth"

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.INERTIAL,
            EphemerisCoordinateSystemType.FIXED,
            EphemerisCoordinateSystemType.J2000,
            EphemerisCoordinateSystemType.ICRF,
            EphemerisCoordinateSystemType.TRUE_OF_DATE,
            EphemerisCoordinateSystemType.TEME_OF_DATE,
            EphemerisCoordinateSystemType.ITRF2000,
            EphemerisCoordinateSystemType.ITRF2005,
            EphemerisCoordinateSystemType.ITRF2008,
            EphemerisCoordinateSystemType.ITRF2014,
            EphemerisCoordinateSystemType.ITRF2020,
        ]:
            exportTool2.coordinate_system = coordSys
            exportTool2.export(outputFile)

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [EphemerisCoordinateSystemType.MEAN_EARTH]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool2.coordinate_system = coordSys

        exportTool.central_body_name = "Moon"

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.FIXED,
            EphemerisCoordinateSystemType.INERTIAL,
            EphemerisCoordinateSystemType.J2000,
            EphemerisCoordinateSystemType.ICRF,
            EphemerisCoordinateSystemType.TRUE_OF_DATE,
            EphemerisCoordinateSystemType.MEAN_EARTH,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.TEME_OF_DATE,
            EphemerisCoordinateSystemType.ITRF2000,
            EphemerisCoordinateSystemType.ITRF2005,
            EphemerisCoordinateSystemType.ITRF2008,
            EphemerisCoordinateSystemType.ITRF2014,
            EphemerisCoordinateSystemType.ITRF2020,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        exportTool.central_body_name = "Mars"

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.FIXED,
            EphemerisCoordinateSystemType.INERTIAL,
            EphemerisCoordinateSystemType.J2000,
            EphemerisCoordinateSystemType.ICRF,
            EphemerisCoordinateSystemType.TRUE_OF_DATE,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EphemerisCoordinateSystemType"

        for coordSys in [
            EphemerisCoordinateSystemType.MEAN_EARTH,
            EphemerisCoordinateSystemType.TEME_OF_DATE,
            EphemerisCoordinateSystemType.ITRF2000,
            EphemerisCoordinateSystemType.ITRF2005,
            EphemerisCoordinateSystemType.ITRF2008,
            EphemerisCoordinateSystemType.ITRF2014,
            EphemerisCoordinateSystemType.ITRF2020,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        TestBase.Application.current_scenario.children.unload(STKObjectType.SATELLITE, "FEA119465")
