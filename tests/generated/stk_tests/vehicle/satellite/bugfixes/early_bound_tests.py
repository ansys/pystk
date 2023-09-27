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

    AG_SAT: "ISatellite" = None

    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("SatelliteTests", "SatelliteTests.sc"))
        EarlyBoundTests.AG_SAT = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite2"), ISatellite
        )
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        (clr.Convert(EarlyBoundTests.AG_SAT.propagator, IVehiclePropagatorTwoBody)).propagate()

    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SAT = None
        TestBase.Uninitialize()

    def setUp(self):
        TestBase.Application.unit_preferences.set_current_unit("AngleUnit", "deg")
        TestBase.Application.unit_preferences.set_current_unit("LatitudeUnit", "deg")
        TestBase.Application.unit_preferences.set_current_unit("LongitudeUnit", "deg")
        if not TestBase.NoGraphicsMode:
            EarlyBoundTests.AG_SAT.graphics.time_events.remove_all()

        else:

            def action1():
                EarlyBoundTests.AG_SAT.graphics.time_events.remove_all()

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action1)

    def test_BUG63355_ExceptionOnBreakAngleTypeUnknown(self):
        def code1():
            EarlyBoundTests.AG_SAT.pass_break.definition.set_break_angle_type(
                VEHICLE_BREAK_ANGLE_TYPE.BREAK_ANGLE_TYPE_UNKNOWN
            )

        ex = ExceptionAssert.Throws(code1)
        StringAssert.Contains("Invalid", str(ex), "Exception message mismatch")

    def test_BUG62983_BUG67662_StkExternalOverride(self):
        # Improper default value of false for IVehiclePropagatorStkExternal.Override
        satellite: "ISatellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "StkExternalSatellite1"),
            ISatellite,
        )
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_STK_EXTERNAL)
        prop: "IVehiclePropagatorStkExternal" = clr.CastAs(satellite.propagator, IVehiclePropagatorStkExternal)
        prop.filename = TestBase.GetScenarioFile("External", "Satellite1.e")
        prop.propagate()
        Assert.assertEqual("9 Sep 2009 16:00:00.000", prop.start_time)
        Assert.assertEqual("10 Sep 2009 16:00:00.000", prop.stop_time)
        # Verify that the "Override" flag is set to false by default.
        Assert.assertFalse(prop.override)

    def test_BUG67722_SGP4SatelliteDuration(self):
        sat2: "ISatellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat2"), ISatellite
        )
        sat2.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
        prop2: "IVehiclePropagatorSGP4" = clr.CastAs(sat2.propagator, IVehiclePropagatorSGP4)
        prop2.propagate()
        scenario: "IScenario" = clr.CastAs(TestBase.Application.current_scenario, IScenario)
        Assert.assertEqual(scenario.start_time, prop2.ephemeris_interval.find_start_time())
        Assert.assertEqual(scenario.stop_time, prop2.ephemeris_interval.find_stop_time())
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat2")

    def test_BUG65831_VectorConstraints(self):
        sat: "ISatellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "BUG65831"), ISatellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
        sgp4: "IVehiclePropagatorSGP4" = clr.CastAs(sat.propagator, IVehiclePropagatorSGP4)
        sgp4.propagate()
        scenario: "IScenario" = clr.CastAs(TestBase.Application.current_scenario, IScenario)

        cnstrAngle: "IAccessConstraintCrdnConstellation" = clr.CastAs(
            sat.access_constraints.add_constraint(ACCESS_CONSTRAINTS.CSTR_VECTOR_GEOMETRY_TOOL_ANGLE),
            IAccessConstraintCrdnConstellation,
        )
        Assert.assertEqual("Satellite/BUG65831 VelocityAzimuth Angle", cnstrAngle.reference)

        cnstrCondition: "IAccessConstraintCrdnConstellation" = clr.CastAs(
            sat.access_constraints.add_constraint(ACCESS_CONSTRAINTS.CSTR_CRDN_CONDITION),
            IAccessConstraintCrdnConstellation,
        )
        Assert.assertEqual("Satellite/BUG65831 AfterStart Condition", cnstrCondition.reference)

        cnstrVectorMag: "IAccessConstraintCrdnConstellation" = clr.CastAs(
            sat.access_constraints.add_constraint(ACCESS_CONSTRAINTS.CSTR_VECTOR_GEOMETRY_TOOL_VECTOR_MAGNITUDE),
            IAccessConstraintCrdnConstellation,
        )
        Assert.assertEqual("Satellite/BUG65831 Velocity Vector", cnstrVectorMag.reference)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "BUG65831")

    # [Test]
    # public void BUG68243_CoordinateEpoch()
    # {
    #    ISatellite sat = Application.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "BUG68243") as ISatellite;
    #    sat.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation);
    #    IVehiclePropagatorJ2Perturbation j2prop = sat.Propagator as IVehiclePropagatorJ2Perturbation;

    #    IOrbitStateCartesian cart = (IOrbitStateCartesian)j2prop.InitialState.Representation.ConvertTo(
    #        AgEOrbitStateType.eOrbitStateCartesian);

    #    cart.CoordinateSystemType = AgECoordinateSystem.eCoordinateSystemMeanOfEpoch;
    #    IOrbitStateCoordinateSystem coordsys = (IOrbitStateCoordinateSystem)cart.CoordinateSystem;
    #    ITimeToolEvent referenceEvent = Application.CurrentScenario.Vgt.Events["AnalysisStartTime"];
    #    cart.CoordinateSystem.CoordinateSystemEpoch.SetImplicitTime(referenceEvent);

    #    j2prop.InitialState.Representation.Assign(cart);
    #    j2prop.Propagate();

    #    Application.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "BUG68243");
    # }

    @category("Graphics Tests")
    def test_BUG86580_AddSingleGfxTimeEvent(self):
        timeEvent: "IVehicleGraphics2DTimeEventsElement" = EarlyBoundTests.AG_SAT.graphics.time_events.add()

        Assert.assertEqual(timeEvent.time_event_type, VEHICLE_GRAPHICS2_D_TIME_EVENT_TYPE.TIME_EVENT_TYPE_MARKER)

        data: "IVehicleGraphics2DTimeEventTypeMarker" = clr.Convert(
            timeEvent.time_event_type_data, IVehicleGraphics2DTimeEventTypeMarker
        )
        Assert.assertEqual("TimeEvent1", data.unique_id)

    @category("Graphics Tests")
    def test_BUG86580_AddTwoGfxTimeEvents(self):
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        timeEvent: "IVehicleGraphics2DTimeEventsElement" = EarlyBoundTests.AG_SAT.graphics.time_events.add()

        Assert.assertEqual(2, EarlyBoundTests.AG_SAT.graphics.time_events.count)

        Assert.assertEqual(timeEvent.time_event_type, VEHICLE_GRAPHICS2_D_TIME_EVENT_TYPE.TIME_EVENT_TYPE_MARKER)

        data: "IVehicleGraphics2DTimeEventTypeMarker" = clr.Convert(
            timeEvent.time_event_type_data, IVehicleGraphics2DTimeEventTypeMarker
        )
        Assert.assertEqual("TimeEvent2", data.unique_id)

    @category("Graphics Tests")
    def test_BUG86580_AddThreeRemoveOneAddOneGfxTimeEvents(self):
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        EarlyBoundTests.AG_SAT.graphics.time_events.add()
        EarlyBoundTests.AG_SAT.graphics.time_events.remove_at(0)

        timeEvent: "IVehicleGraphics2DTimeEventsElement" = EarlyBoundTests.AG_SAT.graphics.time_events.add()

        Assert.assertEqual(3, EarlyBoundTests.AG_SAT.graphics.time_events.count)

        Assert.assertEqual(timeEvent.time_event_type, VEHICLE_GRAPHICS2_D_TIME_EVENT_TYPE.TIME_EVENT_TYPE_MARKER)

        data: "IVehicleGraphics2DTimeEventTypeMarker" = clr.Convert(
            timeEvent.time_event_type_data, IVehicleGraphics2DTimeEventTypeMarker
        )
        Assert.assertEqual("TimeEvent1", data.unique_id)

    @category("Graphics Tests")
    def test_BUG112927_IAgVORefCrdnAngle_ShowDihedralAngleSupportingArcs(self):
        TestBase.Application.vgt_root.get_provider("Satellite/Satellite1").angles.factory.create(
            "BUG112927_Dihedral", "", VECTOR_GEOMETRY_TOOL_ANGLE_TYPE.DIHEDRAL_ANGLE
        )
        dihedral: "IGraphics3DReferenceVectorGeometryToolAngle" = clr.CastAs(
            EarlyBoundTests.AG_SAT.graphics3_d.vector.reference_crdns.add(
                GEOMETRIC_ELEM_TYPE.ANGLE_ELEM, "Satellite/Satellite1 BUG112927_Dihedral Angle"
            ),
            IGraphics3DReferenceVectorGeometryToolAngle,
        )

        dihedral.visible = False
        Assert.assertFalse(dihedral.visible)
        dihedral.visible = True
        Assert.assertTrue(dihedral.visible)

        dihedral.label_visible = False
        Assert.assertFalse(dihedral.label_visible)
        dihedral.label_visible = True
        Assert.assertTrue(dihedral.label_visible)

        dihedral.angle_value_visible = False
        Assert.assertFalse(dihedral.angle_value_visible)
        dihedral.angle_value_visible = True
        Assert.assertTrue(dihedral.angle_value_visible)

        dihedral.show_dihedral_angle_supporting_arcs = False
        Assert.assertFalse(dihedral.show_dihedral_angle_supporting_arcs)
        dihedral.show_dihedral_angle_supporting_arcs = True
        Assert.assertTrue(dihedral.show_dihedral_angle_supporting_arcs)

    def test_BUG119916_StoppingConditions_MaxTripTimes(self):
        sat: "ISatellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "BUG119916"), ISatellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)

        mcs: "IDriverMissionControlSequence" = clr.CastAs(sat.propagator, IDriverMissionControlSequence)
        propagate: "IMissionControlSequencePropagate" = clr.CastAs(
            mcs.main_sequence.get_item_by_name("Propagate"), IMissionControlSequencePropagate
        )

        stopCond: "IStoppingCondition" = clr.CastAs(
            propagate.stopping_conditions["Duration"].properties, IStoppingCondition
        )

        def action2():
            stopCond.max_trip_times = 10001

        TryCatchAssertBlock.ExpectedException("read-only", action2)  # read-only without a Sequence set

        mcs.auto_sequence.add("AutoSeq1")
        stopCond.sequence = "AutoSeq1"
        stopCond.max_trip_times = 10001
        Assert.assertEqual(10001, stopCond.max_trip_times)  # settable when a Sequence is set

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "BUG119916")

    def test_FEA119646_CCSDS_CB_and_RefFrames(self):
        sat: "ISatellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "FEA119646"), ISatellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)
        twoBody.propagate()

        exportTool: "IVehicleEphemerisCCSDSExportTool" = sat.export_tools.get_ephemeris_ccsds_export_tool()
        exportTool.originator = "originator"
        exportTool.object_id = "objectid"
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

        def action3():
            exportTool.reference_frame = CCSDS_REFERENCE_FRAME.MEAN_EARTH

        TryCatchAssertBlock.ExpectedException("must be in", action3)

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

            def action4():
                exportTool.reference_frame = refFrame

            TryCatchAssertBlock.ExpectedException("must be in", action4)

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

            def action5():
                exportTool.reference_frame = refFrame

            TryCatchAssertBlock.ExpectedException("must be in", action5)

        #
        # Do the same as above with CCSDSv2
        #

        exportToolv2: "IVehicleEphemerisCCSDSv2ExportTool" = sat.export_tools.get_ephemeris_ccsd_sv2_export_tool()
        exportToolv2.originator = "originator"
        exportToolv2.object_id = "objectid"
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

        def action6():
            exportToolv2.reference_frame = CCSDS_REFERENCE_FRAME.MEAN_EARTH

        TryCatchAssertBlock.ExpectedException("must be in", action6)

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

            def action7():
                exportToolv2.reference_frame = refFrame

            TryCatchAssertBlock.ExpectedException("must be in", action7)

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

            def action8():
                exportToolv2.reference_frame = refFrame

            TryCatchAssertBlock.ExpectedException("must be in", action8)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "FEA119646")

    def test_FEA119465_STKEphem_CB_and_RefFrames(self):
        sat: "ISatellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "FEA119465"), ISatellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)
        twoBody.propagate()

        outputFile: str = TestBase.GetScenarioFile("test.out")

        # STK Binary Ephemeris

        exportTool: "IVehicleEphemerisStkExportTool" = sat.export_tools.get_ephemeris_stk_export_tool()
        exportTool.use_vehicle_central_body = False

        exportTool.central_body_name = "Earth"

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.INERTIAL,
            STK_EPHEM_COORDINATE_SYSTEM.FIXED,
            STK_EPHEM_COORDINATE_SYSTEM.J2000,
            STK_EPHEM_COORDINATE_SYSTEM.ICRF,
            STK_EPHEM_COORDINATE_SYSTEM.TRUE_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.TEME_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2000,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2005,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2008,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2014,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2020,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [STK_EPHEM_COORDINATE_SYSTEM.MEAN_EARTH]:

            def action9():
                exportTool.coordinate_system = coordSys

            TryCatchAssertBlock.ExpectedException("must be in", action9)

        exportTool.central_body_name = "Moon"

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.FIXED,
            STK_EPHEM_COORDINATE_SYSTEM.INERTIAL,
            STK_EPHEM_COORDINATE_SYSTEM.J2000,
            STK_EPHEM_COORDINATE_SYSTEM.ICRF,
            STK_EPHEM_COORDINATE_SYSTEM.TRUE_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.MEAN_EARTH,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.TEME_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2000,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2005,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2008,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2014,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2020,
        ]:

            def action10():
                exportTool.coordinate_system = coordSys

            TryCatchAssertBlock.ExpectedException("must be in", action10)

        exportTool.central_body_name = "Mars"

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.FIXED,
            STK_EPHEM_COORDINATE_SYSTEM.INERTIAL,
            STK_EPHEM_COORDINATE_SYSTEM.J2000,
            STK_EPHEM_COORDINATE_SYSTEM.ICRF,
            STK_EPHEM_COORDINATE_SYSTEM.TRUE_OF_DATE,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.MEAN_EARTH,
            STK_EPHEM_COORDINATE_SYSTEM.TEME_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2000,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2005,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2008,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2014,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2020,
        ]:

            def action11():
                exportTool.coordinate_system = coordSys

            TryCatchAssertBlock.ExpectedException("must be in", action11)

        #
        # Do the same with STK Binary Ephemeris
        #

        exportTool2: "IVehicleEphemerisStkBinaryExportTool" = sat.export_tools.get_ephemeris_stk_binary_export_tool()
        exportTool2.use_vehicle_central_body = False

        exportTool2.central_body_name = "Earth"

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.INERTIAL,
            STK_EPHEM_COORDINATE_SYSTEM.FIXED,
            STK_EPHEM_COORDINATE_SYSTEM.J2000,
            STK_EPHEM_COORDINATE_SYSTEM.ICRF,
            STK_EPHEM_COORDINATE_SYSTEM.TRUE_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.TEME_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2000,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2005,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2008,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2014,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2020,
        ]:
            exportTool2.coordinate_system = coordSys
            exportTool2.export(outputFile)

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [STK_EPHEM_COORDINATE_SYSTEM.MEAN_EARTH]:

            def action12():
                exportTool2.coordinate_system = coordSys

            TryCatchAssertBlock.ExpectedException("must be in", action12)

        exportTool.central_body_name = "Moon"

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.FIXED,
            STK_EPHEM_COORDINATE_SYSTEM.INERTIAL,
            STK_EPHEM_COORDINATE_SYSTEM.J2000,
            STK_EPHEM_COORDINATE_SYSTEM.ICRF,
            STK_EPHEM_COORDINATE_SYSTEM.TRUE_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.MEAN_EARTH,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.TEME_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2000,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2005,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2008,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2014,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2020,
        ]:

            def action13():
                exportTool.coordinate_system = coordSys

            TryCatchAssertBlock.ExpectedException("must be in", action13)

        exportTool.central_body_name = "Mars"

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.FIXED,
            STK_EPHEM_COORDINATE_SYSTEM.INERTIAL,
            STK_EPHEM_COORDINATE_SYSTEM.J2000,
            STK_EPHEM_COORDINATE_SYSTEM.ICRF,
            STK_EPHEM_COORDINATE_SYSTEM.TRUE_OF_DATE,
        ]:
            exportTool.coordinate_system = coordSys
            exportTool.export(outputFile)

        coordSys: "STK_EPHEM_COORDINATE_SYSTEM"

        for coordSys in [
            STK_EPHEM_COORDINATE_SYSTEM.MEAN_EARTH,
            STK_EPHEM_COORDINATE_SYSTEM.TEME_OF_DATE,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2000,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2005,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2008,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2014,
            STK_EPHEM_COORDINATE_SYSTEM.ITRF2020,
        ]:

            def action14():
                exportTool.coordinate_system = coordSys

            TryCatchAssertBlock.ExpectedException("must be in", action14)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "FEA119465")
