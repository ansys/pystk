import pytest
from test_util import *
from assertion_harness import *
from parameterized import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.vgt import *


class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    AG_SAT: "Satellite" = None

    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("SatelliteTests", "SatelliteTests.sc"))
        EarlyBoundTests.AG_SAT = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite2")
        )
        EarlyBoundTests.AG_SAT.set_propagator_type(PROPAGATOR_TYPE.TWO_BODY)
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
            EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(VEHICLE_BREAK_ANGLE_TYPE.UNKNOWN)

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("Invalid", str(ex), "Exception message mismatch")

    def test_BUG62983_BUG67662_StkExternalOverride(self):
        # Improper default value of false for PropagatorStkExternal.Override
        satellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "StkExternalSatellite1"),
            Satellite,
        )
        satellite.set_propagator_type(PROPAGATOR_TYPE.STK_EXTERNAL)
        prop: "PropagatorStkExternal" = clr.CastAs(satellite.propagator, PropagatorStkExternal)
        prop.filename = TestBase.GetScenarioFile("External", "Satellite1.e")
        prop.propagate()
        Assert.assertEqual("9 Sep 2009 16:00:00.000", prop.start_time)
        Assert.assertEqual("10 Sep 2009 16:00:00.000", prop.stop_time)
        # Verify that the "Override" flag is set to false by default.
        Assert.assertFalse(prop.override)

    def test_BUG67722_SGP4SatelliteDuration(self):
        sat2: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat2"), Satellite
        )
        sat2.set_propagator_type(PROPAGATOR_TYPE.SGP4)
        prop2: "PropagatorSGP4" = clr.CastAs(sat2.propagator, PropagatorSGP4)
        prop2.propagate()
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        Assert.assertEqual(scenario.start_time, prop2.ephemeris_interval.find_start_time())
        Assert.assertEqual(scenario.stop_time, prop2.ephemeris_interval.find_stop_time())
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat2")

    def test_BUG65831_VectorConstraints(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "BUG65831"), Satellite
        )
        sat.set_propagator_type(PROPAGATOR_TYPE.SGP4)
        sgp4: "PropagatorSGP4" = clr.CastAs(sat.propagator, PropagatorSGP4)
        sgp4.propagate()
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)

        cnstrAngle: "AccessConstraintAnalysisWorkbenchComponent" = clr.CastAs(
            sat.access_constraints.add_constraint(ACCESS_CONSTRAINT_TYPE.VECTOR_GEOMETRY_TOOL_ANGLE),
            AccessConstraintAnalysisWorkbenchComponent,
        )
        Assert.assertEqual("Satellite/BUG65831 VelocityAzimuth Angle", cnstrAngle.reference)

        cnstrCondition: "AccessConstraintAnalysisWorkbenchComponent" = clr.CastAs(
            sat.access_constraints.add_constraint(ACCESS_CONSTRAINT_TYPE.CONDITION),
            AccessConstraintAnalysisWorkbenchComponent,
        )
        Assert.assertEqual("Satellite/BUG65831 AfterStart Condition", cnstrCondition.reference)

        cnstrVectorMag: "AccessConstraintAnalysisWorkbenchComponent" = clr.CastAs(
            sat.access_constraints.add_constraint(ACCESS_CONSTRAINT_TYPE.VECTOR_MAGNITUDE),
            AccessConstraintAnalysisWorkbenchComponent,
        )
        Assert.assertEqual("Satellite/BUG65831 Velocity Vector", cnstrVectorMag.reference)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "BUG65831")

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

        Assert.assertEqual(timeEvent.time_event_type, VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE.MARKER)

        data: "VehicleGraphics2DTimeEventTypeMarker" = VehicleGraphics2DTimeEventTypeMarker(
            timeEvent.time_event_type_data
        )
        Assert.assertEqual("TimeEvent1", data.unique_identifer)

    @category("Graphics Tests")
    def test_BUG86580_AddTwoGfxTimeEvents(self):
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        timeEvent: "VehicleGraphics2DTimeEventsElement" = EarlyBoundTests.AG_SAT.graphics.time_events.add()

        Assert.assertEqual(2, EarlyBoundTests.AG_SAT.graphics.time_events.count)

        Assert.assertEqual(timeEvent.time_event_type, VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE.MARKER)

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

        Assert.assertEqual(timeEvent.time_event_type, VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE.MARKER)

        data: "VehicleGraphics2DTimeEventTypeMarker" = VehicleGraphics2DTimeEventTypeMarker(
            timeEvent.time_event_type_data
        )
        Assert.assertEqual("TimeEvent1", data.unique_identifer)

    @category("Graphics Tests")
    def test_BUG112927_IAgVORefCrdnAngle_ShowDihedralAngleSupportingArcs(self):
        TestBase.Application.analysis_workbench_components_root.get_provider(
            "Satellite/Satellite1"
        ).angles.factory.create("BUG112927_Dihedral", "", ANGLE_TYPE.DIHEDRAL_ANGLE)
        dihedral: "Graphics3DReferenceAngle" = clr.CastAs(
            EarlyBoundTests.AG_SAT.graphics_3d.vector.vector_geometry_tool_components.add(
                GEOMETRIC_ELEMENT_TYPE.ANGLE_ELEMENT, "Satellite/Satellite1 BUG112927_Dihedral Angle"
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
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "BUG119916"), Satellite
        )
        sat.set_propagator_type(PROPAGATOR_TYPE.ASTROGATOR)

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

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "BUG119916")

    def test_FEA119646_CCSDS_CB_and_RefFrames(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "FEA119646"), Satellite
        )
        sat.set_propagator_type(PROPAGATOR_TYPE.TWO_BODY)
        twoBody: "PropagatorTwoBody" = clr.CastAs(sat.propagator, PropagatorTwoBody)
        twoBody.propagate()

        exportTool: "VehicleEphemerisCCSDSExportTool" = sat.export_tools.get_ephemeris_ccsds_export_tool()
        exportTool.originator = "originator"
        exportTool.object_identifier = "objectid"
        outputFile: str = TestBase.GetScenarioFile("test.out")

        exportTool.central_body_name = "Earth"

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.EME2000,
            CCSDS_REFERENCE_FRAME.FIXED,
            CCSDS_REFERENCE_FRAME.ICRF,
            CCSDS_REFERENCE_FRAME.ITRF,
            CCSDS_REFERENCE_FRAME.ITRF2000,
            CCSDS_REFERENCE_FRAME.ITRF2005,
            CCSDS_REFERENCE_FRAME.ITRF2008,
            CCSDS_REFERENCE_FRAME.ITRF2014,
            CCSDS_REFERENCE_FRAME.ITRF2020,
            CCSDS_REFERENCE_FRAME.TEME_OF_DATE,
            CCSDS_REFERENCE_FRAME.TOD,
            CCSDS_REFERENCE_FRAME.GCRF,
        ]:
            exportTool.reference_frame = refFrame
            exportTool.export(outputFile)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            exportTool.reference_frame = CCSDS_REFERENCE_FRAME.MEAN_EARTH

        exportTool.central_body_name = "Moon"

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.EME2000,
            CCSDS_REFERENCE_FRAME.FIXED,
            CCSDS_REFERENCE_FRAME.ICRF,
            CCSDS_REFERENCE_FRAME.MEAN_EARTH,
            CCSDS_REFERENCE_FRAME.TOD,
        ]:
            exportTool.reference_frame = refFrame
            exportTool.export(outputFile)

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.ITRF,
            CCSDS_REFERENCE_FRAME.ITRF2000,
            CCSDS_REFERENCE_FRAME.ITRF2005,
            CCSDS_REFERENCE_FRAME.ITRF2008,
            CCSDS_REFERENCE_FRAME.ITRF2014,
            CCSDS_REFERENCE_FRAME.ITRF2020,
            CCSDS_REFERENCE_FRAME.TEME_OF_DATE,
            CCSDS_REFERENCE_FRAME.GCRF,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.reference_frame = refFrame

        exportTool.central_body_name = "Mars"

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.EME2000,
            CCSDS_REFERENCE_FRAME.FIXED,
            CCSDS_REFERENCE_FRAME.ICRF,
            CCSDS_REFERENCE_FRAME.TOD,
        ]:
            exportTool.reference_frame = refFrame
            exportTool.export(outputFile)

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.MEAN_EARTH,
            CCSDS_REFERENCE_FRAME.ITRF,
            CCSDS_REFERENCE_FRAME.ITRF2000,
            CCSDS_REFERENCE_FRAME.ITRF2005,
            CCSDS_REFERENCE_FRAME.ITRF2008,
            CCSDS_REFERENCE_FRAME.ITRF2014,
            CCSDS_REFERENCE_FRAME.ITRF2020,
            CCSDS_REFERENCE_FRAME.TEME_OF_DATE,
            CCSDS_REFERENCE_FRAME.GCRF,
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

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.EME2000,
            CCSDS_REFERENCE_FRAME.FIXED,
            CCSDS_REFERENCE_FRAME.ICRF,
            CCSDS_REFERENCE_FRAME.ITRF,
            CCSDS_REFERENCE_FRAME.ITRF2000,
            CCSDS_REFERENCE_FRAME.ITRF2005,
            CCSDS_REFERENCE_FRAME.ITRF2008,
            CCSDS_REFERENCE_FRAME.ITRF2014,
            CCSDS_REFERENCE_FRAME.ITRF2020,
            CCSDS_REFERENCE_FRAME.TEME_OF_DATE,
            CCSDS_REFERENCE_FRAME.TOD,
            CCSDS_REFERENCE_FRAME.GCRF,
        ]:
            exportToolv2.reference_frame = refFrame
            exportToolv2.export(outputFile)

        with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
            exportToolv2.reference_frame = CCSDS_REFERENCE_FRAME.MEAN_EARTH

        exportToolv2.central_body_name = "Moon"

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.EME2000,
            CCSDS_REFERENCE_FRAME.FIXED,
            CCSDS_REFERENCE_FRAME.ICRF,
            CCSDS_REFERENCE_FRAME.MEAN_EARTH,
            CCSDS_REFERENCE_FRAME.TOD,
        ]:
            exportToolv2.reference_frame = refFrame
            exportToolv2.export(outputFile)

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.ITRF,
            CCSDS_REFERENCE_FRAME.ITRF2000,
            CCSDS_REFERENCE_FRAME.ITRF2005,
            CCSDS_REFERENCE_FRAME.ITRF2008,
            CCSDS_REFERENCE_FRAME.ITRF2014,
            CCSDS_REFERENCE_FRAME.ITRF2020,
            CCSDS_REFERENCE_FRAME.TEME_OF_DATE,
            CCSDS_REFERENCE_FRAME.GCRF,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportToolv2.reference_frame = refFrame

        exportToolv2.central_body_name = "Mars"

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.EME2000,
            CCSDS_REFERENCE_FRAME.FIXED,
            CCSDS_REFERENCE_FRAME.ICRF,
            CCSDS_REFERENCE_FRAME.TOD,
        ]:
            exportToolv2.reference_frame = refFrame
            exportToolv2.export(outputFile)

        refFrame: "CCSDS_REFERENCE_FRAME"

        for refFrame in [
            CCSDS_REFERENCE_FRAME.MEAN_EARTH,
            CCSDS_REFERENCE_FRAME.ITRF,
            CCSDS_REFERENCE_FRAME.ITRF2000,
            CCSDS_REFERENCE_FRAME.ITRF2005,
            CCSDS_REFERENCE_FRAME.ITRF2008,
            CCSDS_REFERENCE_FRAME.ITRF2014,
            CCSDS_REFERENCE_FRAME.ITRF2020,
            CCSDS_REFERENCE_FRAME.TEME_OF_DATE,
            CCSDS_REFERENCE_FRAME.GCRF,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportToolv2.reference_frame = refFrame

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "FEA119646")

    def test_FEA119465_STKEphem_CB_and_RefFrames(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "FEA119465"), Satellite
        )
        sat.set_propagator_type(PROPAGATOR_TYPE.TWO_BODY)
        twoBody: "PropagatorTwoBody" = clr.CastAs(sat.propagator, PropagatorTwoBody)
        twoBody.propagate()

        outputFile: str = TestBase.GetScenarioFile("test.out")

        # STK Binary Ephemeris

        exportTool: "VehicleEphemerisExportTool" = sat.export_tools.get_ephemeris_stk_export_tool()
        exportTool.use_vehicle_central_body = False

        exportTool.central_body_name = "Earth"

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.INERTIAL,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.FIXED,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.J2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ICRF,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TRUE_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TEME_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2005,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2008,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2014,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2020,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [EPHEMERIS_COORDINATE_SYSTEM_TYPE.MEAN_EARTH]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        exportTool.central_body_name = "Moon"

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.FIXED,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.INERTIAL,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.J2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ICRF,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TRUE_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.MEAN_EARTH,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TEME_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2005,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2008,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2014,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2020,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        exportTool.central_body_name = "Mars"

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.FIXED,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.INERTIAL,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.J2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ICRF,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TRUE_OF_DATE,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.MEAN_EARTH,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TEME_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2005,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2008,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2014,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2020,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        #
        # Do the same with STK Binary Ephemeris
        #

        exportTool2: "VehicleEphemerisBinaryExportTool" = sat.export_tools.get_ephemeris_stk_binary_export_tool()
        exportTool2.use_vehicle_central_body = False

        exportTool2.central_body_name = "Earth"

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.INERTIAL,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.FIXED,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.J2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ICRF,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TRUE_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TEME_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2005,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2008,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2014,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2020,
        ]:
            exportTool2.coordinate_system = coordSys
            exportTool2.export(outputFile)

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [EPHEMERIS_COORDINATE_SYSTEM_TYPE.MEAN_EARTH]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool2.coordinate_system = coordSys

        exportTool.central_body_name = "Moon"

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.FIXED,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.INERTIAL,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.J2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ICRF,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TRUE_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.MEAN_EARTH,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TEME_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2005,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2008,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2014,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2020,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        exportTool.central_body_name = "Mars"

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.FIXED,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.INERTIAL,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.J2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ICRF,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TRUE_OF_DATE,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "EPHEMERIS_COORDINATE_SYSTEM_TYPE"

        for coordSys in [
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.MEAN_EARTH,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.TEME_OF_DATE,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2000,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2005,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2008,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2014,
            EPHEMERIS_COORDINATE_SYSTEM_TYPE.ITRF2020,
        ]:
            with pytest.raises(Exception, match=RegexSubstringMatch("must be in")):
                exportTool.coordinate_system = coordSys

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "FEA119465")
