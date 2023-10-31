import pytest
from test_util import *
from app_provider import *
from assert_extension import *
from assertion_harness import *
from gator_helper import *
from logger import *
from math2 import *
from stk_util_helper import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        try:
            TestBase.Initialize()
            TestBase.LoadTestScenario(Path.Combine("AstrogatorTests", "AstrogatorTests.sc"))
            EarlyBoundTests.AG_SAT = clr.Convert(
                TestBase.Application.current_scenario.children["Satellite1"], Satellite
            )
            EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
            EarlyBoundTests.AG_VA = clr.Convert(EarlyBoundTests.AG_SAT.propagator, DriverMissionControlSequence)

        except Exception as e:
            Console.WriteLine(str(e))
            Console.WriteLine(e.StackTrace)
            Assert.fail(("Exception in Astrogator::EarlyBoundTests::Init: " + str(e)))

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.AG_SAT = None
        TestBase.Uninitialize()

    # endregion

    # region Static DataMembers
    AG_SAT: "Satellite" = None
    AG_VA: "DriverMissionControlSequence" = None
    # endregion

    def TestTargeterGraphsControlDisabled(self, tg: "TargeterGraphCollection", isDC: bool):
        Assert.assertEqual(tg[0].name, tg["Graph1"].name)
        graph2: "TargeterGraph" = tg.add_graph()
        Assert.assertEqual(2, tg.count)
        tempGraph: "TargeterGraph"
        for tempGraph in tg:
            Console.WriteLine(tempGraph.name)

        Assert.assertEqual("Graph2", graph2.name)

        graph2.name = "Graph2NameChanged"
        Assert.assertEqual("Graph2NameChanged", graph2.name)

        tg.remove_graph("Graph2NameChanged")
        Assert.assertEqual(1, tg.count)

        graph: "TargeterGraph" = tg[0]

        GatorHelper.TestRuntimeTypeInfo(graph)
        Assert.assertEqual("Graph1", graph.name)
        Assert.assertFalse(graph.generate_on_run)
        graph.generate_on_run = True
        Assert.assertTrue(graph.generate_on_run)
        Assert.assertEqual("Iteration", graph.independent_variable)

        try:
            graph.show_label_iterations = True
            Assert.fail("Read only.")

        except AssertionError as e:
            raise e

        except Exception as e:
            Console.WriteLine(str(e))

        try:
            graph.show_desired_value = True
            Assert.fail("Read only.")

        except AssertionError as e:
            raise e

        except Exception as e:
            Console.WriteLine(str(e))

        try:
            graph.show_tolerance_band = True
            Assert.fail("Read only.")

        except AssertionError as e:
            raise e

        except Exception as e:
            Console.WriteLine(str(e))

        graph.independent_variable = "prop1 : Epoch"
        Assert.assertEqual("prop1 : Epoch", graph.independent_variable)
        Assert.assertFalse(graph.show_desired_value)
        if isDC:
            graph.show_desired_value = True
            Assert.assertTrue(graph.show_desired_value)

        Assert.assertTrue(graph.show_label_iterations)
        graph.show_label_iterations = False
        Assert.assertFalse(graph.show_label_iterations)
        Assert.assertFalse(graph.show_tolerance_band)
        if isDC:
            graph.show_tolerance_band = True
            Assert.assertTrue(graph.show_tolerance_band)

        Assert.assertEqual("Targeter Graph", graph.user_comment)
        graph.user_comment = "Targeter Graph1 User Comment."
        Assert.assertEqual("Targeter Graph1 User Comment.", graph.user_comment)

        tgacc: "TargeterGraphActiveControlCollection" = tg[0].active_controls
        Assert.assertEqual(0, tgacc.count)
        GatorHelper.TestRuntimeTypeInfo(tgacc)

    def TestTargeterGraphsControlEnabled(self, tg: "TargeterGraphCollection", isDC: bool):
        tgacc: "TargeterGraphActiveControlCollection" = tg[0].active_controls
        Assert.assertEqual(1, tgacc.count)
        activeControl: "TargeterGraphActiveControl"
        for activeControl in tgacc:
            Console.WriteLine(activeControl.name)

        active: "TargeterGraphActiveControl" = tgacc[0]
        Assert.assertEqual("prop1 : MaxPropTime", active.name)
        Assert.assertEqual("prop1", active.parent_name)

        # all properties are readonly when show graph value = false;
        try:
            active.line_color = Color.Green
            Assert.fail("Read only.")

        except AssertionError as e:
            raise e

        except Exception as e:
            Console.WriteLine(str(e))

        try:
            active.point_style = "Plus"
            Assert.fail("Read only.")

        except AssertionError as e:
            raise e

        except Exception as e:
            Console.WriteLine(str(e))

        try:
            active.y_axis = "Y1"
            Assert.fail("Read only.")

        except AssertionError as e:
            raise e

        except Exception as e:
            Console.WriteLine(str(e))

        if TestBase.NoGraphicsMode:

            def action1():
                active.show_graph_value = True

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action1)

            def action2():
                active.line_color = Color.Blue

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action2)

            def action3():
                active.point_style = "Square"

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action3)

            def action4():
                active.y_axis = "Y2"

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action4)

        else:
            Assert.assertFalse(active.show_graph_value)
            active.show_graph_value = True
            Assert.assertTrue(active.show_graph_value)
            active.line_color = Color.Blue
            AssertEx.AreEqual(Color.Blue, active.line_color)
            active.point_style = "Square"
            Assert.assertEqual("Square", active.point_style)
            active.y_axis = "Y2"
            Assert.assertEqual("Y2", active.y_axis)

        tgrc: "TargeterGraphResultCollection" = tg[0].results
        GatorHelper.TestRuntimeTypeInfo(tgrc)

        Assert.assertEqual(1, tgrc.count)
        gresult: "TargeterGraphResult"
        for gresult in tgrc:
            Console.WriteLine(gresult.name)

        result: "TargeterGraphResult" = tgrc[0]
        Assert.assertEqual("prop1 : Epoch", result.name)
        Assert.assertEqual("prop1", result.parent_name)
        Assert.assertEqual(GRAPH_OPTION.NO_GRAPH, result.graph_option)

        def action5():
            result.show_desired_value = True

        # all options are read only.
        TryCatchAssertBlock.ExpectedException("read-only", action5)
        if not TestBase.NoGraphicsMode:

            def action6():
                result.line_color = Color.Green

            TryCatchAssertBlock.ExpectedException("read-only", action6)

        else:

            def action7():
                result.line_color = Color.Green

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action7)

        def action8():
            result.point_style = "Plus"

        TryCatchAssertBlock.ExpectedException("read-only", action8)

        def action9():
            result.y_axis = "Y2"

        TryCatchAssertBlock.ExpectedException("read-only", action9)

        def action10():
            result.show_tolerance_band = True

        TryCatchAssertBlock.ExpectedException("read-only", action10)

        result.graph_option = GRAPH_OPTION.GRAPH_VALUE
        Assert.assertEqual(GRAPH_OPTION.GRAPH_VALUE, result.graph_option)
        if isDC:
            result.graph_option = GRAPH_OPTION.GRAPH_DIFFERENCE
            Assert.assertEqual(GRAPH_OPTION.GRAPH_DIFFERENCE, result.graph_option)

        Assert.assertFalse(result.show_desired_value)
        # show desired is readonly
        try:
            result.show_desired_value = True
            Assert.fail("Read only.")

        except AssertionError as e:
            raise e

        except Exception as e:
            Console.WriteLine(str(e))

        if not TestBase.NoGraphicsMode:
            result.line_color = Color.Yellow
            AssertEx.AreEqual(Color.Yellow, result.line_color)

        else:

            def action11():
                result.line_color = Color.Yellow

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action11)

        result.point_style = "Diamond"
        Assert.assertEqual("Diamond", result.point_style)
        result.y_axis = "Y2"
        Assert.assertEqual("Y2", result.y_axis)
        Assert.assertFalse(result.show_tolerance_band)
        if isDC:
            result.show_tolerance_band = True
            Assert.assertTrue(result.show_tolerance_band)

        result.graph_option = GRAPH_OPTION.GRAPH_VALUE
        Assert.assertEqual(GRAPH_OPTION.GRAPH_VALUE, result.graph_option)
        Assert.assertFalse(result.show_desired_value)
        if isDC:
            result.show_desired_value = True
            Assert.assertTrue(result.show_desired_value)

    @category("ExcludeOnLinux")
    def test_TargeterGraphs(self):
        satellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "REQ57491"), Satellite
        )
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(satellite.propagator, DriverMissionControlSequence)
        ts: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence1", "-"),
            MissionControlSequenceTargetSequence,
        )
        prop1: "MissionControlSequencePropagate" = clr.CastAs(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "prop1", "-"), MissionControlSequencePropagate
        )
        prop1.enable_control_parameter(CONTROL_ADVANCED.PROPAGATE_MAX_PROP_TIME)
        (clr.CastAs(prop1, IMissionControlSequenceSegment)).results.add("Epoch")
        dc: "ProfileDifferentialCorrector" = clr.CastAs(ts.profiles[0], ProfileDifferentialCorrector)
        self.TestTargeterGraphsControlDisabled(dc.targeter_graphs, True)
        dc.control_parameters[0].enable = True
        self.TestTargeterGraphsControlEnabled(dc.targeter_graphs, True)

        # if (!OSHelper.Is64Bit() && !OSHelper.IsLinux())
        # {
        #    // DEOptimizer not available on x64/linux yet

        #    IAgVAProfileDEOptimizer deOptimizer = ts.Profiles.Add("Design Explorer Optimizer") as IAgVAProfileDEOptimizer;
        #    TestTargeterGraphsControlDisabled(deOptimizer.TargeterGraphs, false);
        #    deOptimizer.ControlParameters[0].Enable = true;
        #    TestTargeterGraphsControlEnabled(deOptimizer.TargeterGraphs, false);
        # }

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "REQ57491")

    def test_CloneObject(self):
        satellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ENG56187"), Satellite
        )
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(satellite.propagator, DriverMissionControlSequence)
        sequence: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence1", "-"),
            MissionControlSequenceTargetSequence,
        )
        directory: "ComponentDirectory" = (
            clr.CastAs(TestBase.Application.current_scenario, Scenario)
        ).component_directory
        infoCollection: "ComponentInfoCollection" = directory.get_components(COMPONENT.ASTROGATOR).get_folder(
            "MCS Segments"
        )
        info: "IComponentInfo" = clr.CastAs((clr.Convert(sequence, ICloneable)).clone_object(), IComponentInfo)
        browser: "IComponentInfo" = infoCollection[info.name]
        Assert.assertIsNotNone(browser)
        targetSequence: "MissionControlSequenceTargetSequence" = clr.CastAs(
            browser, MissionControlSequenceTargetSequence
        )
        Assert.assertIsNotNone(targetSequence)
        prop: "MissionControlSequencePropagate" = clr.CastAs(
            driver.main_sequence["Propagate"], MissionControlSequencePropagate
        )
        duration: "StoppingCondition" = clr.CastAs(prop.stopping_conditions["Duration"].properties, StoppingCondition)
        trigger: "AsTriggerCondition" = duration.constraints.add("UserDefined")
        trigger.value = 145
        trigger.tolerance = 0.5
        info2: "IComponentInfo" = clr.CastAs((clr.CastAs(trigger, ICloneable)).clone_object(), IComponentInfo)
        infoCollection = directory.get_components(COMPONENT.ASTROGATOR).get_folder("Constraints")
        browser = infoCollection[info2.name]
        Assert.assertIsNotNone(browser)
        browserTrigger: "AsTriggerCondition" = clr.CastAs(browser, AsTriggerCondition)
        Assert.assertIsNotNone(browserTrigger)
        Assert.assertEqual(browserTrigger.value, trigger.value)
        Assert.assertEqual(browserTrigger.tolerance, trigger.tolerance)
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "ENG56187")

    def test_ReferencePoint(self):
        satellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ReferencePoint"), Satellite
        )
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(satellite.propagator, DriverMissionControlSequence)
        prop: "MissionControlSequencePropagate" = clr.CastAs(
            driver.main_sequence["Propagate"], MissionControlSequencePropagate
        )
        stoppingCondition: "StoppingCondition" = clr.CastAs(
            prop.stopping_conditions.add("R Magnitude").properties, StoppingCondition
        )
        Console.WriteLine(stoppingCondition.reference_point)
        stoppingCondition.reference_point = "CentralBody/Earth L1"
        Assert.assertEqual("CentralBody/Earth L1", stoppingCondition.reference_point)

        duration: "StoppingCondition" = clr.CastAs(prop.stopping_conditions[0].properties, StoppingCondition)
        try:
            duration.reference_point = "CentralBody/Earth L1"
            Assert.fail("Attribute not available.")

        except AssertionError as e:
            raise e

        except Exception as e:
            Console.WriteLine(str(e))

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "ReferencePoint")

    def test_ScriptingToolObjectNames(self):
        satellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ENG55298"), Satellite
        )
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(satellite.propagator, DriverMissionControlSequence)
        sequence: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence1", "-"),
            MissionControlSequenceTargetSequence,
        )
        sequence.segments.insert(SEGMENT_TYPE.INITIAL_STATE, "InitState", "-")
        sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver1", "-")
        tool: "ProfileScriptingTool" = clr.CastAs(sequence.profiles.add("Scripting Tool"), ProfileScriptingTool)
        segment: "ScriptingSegment" = tool.segment_properties.add("Attribute")
        objectName: str
        for objectName in segment.available_object_names:
            Console.WriteLine(objectName)

        Assert.assertEqual(3, Array.Length(segment.available_object_names))
        Assert.assertEqual("Segments.InitState", segment.available_object_names[0])
        Assert.assertEqual("Segments.Maneuver1", segment.available_object_names[1])
        Assert.assertEqual("Profiles.Differential Corrector", segment.available_object_names[2])
        segment.object_name = "Profiles.Differential Corrector"
        Assert.assertEqual("Profiles.Differential Corrector", segment.object_name)
        segment.object_name = "Segments.Maneuver1"
        Assert.assertEqual("Segments.Maneuver1", segment.object_name)
        segment.object_name = "Segments.InitState"
        Assert.assertEqual("Segments.InitState", segment.object_name)
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "ENG55298")

    # region MCSOptions
    def test_MCSOptions(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - MCSOptions START")
        options: "MissionControlSequenceOptions" = EarlyBoundTests.AG_VA.options
        # MissionControlSequenceOptions does not support RuntimeTypeInfo
        # GatorHelper.TestRuntimeTypeInfo(options);

        options.clear_additional_b_plane_points = False
        Assert.assertFalse(options.clear_additional_b_plane_points)
        options.clear_additional_b_plane_points = True
        Assert.assertTrue(options.clear_additional_b_plane_points)

        options.clear_dwc_graphics_before_each_run = False
        Assert.assertFalse(options.clear_dwc_graphics_before_each_run)
        options.clear_dwc_graphics_before_each_run = True
        Assert.assertTrue(options.clear_dwc_graphics_before_each_run)

        options.draw_trajectory_in_2d = True
        Assert.assertTrue(options.draw_trajectory_in_2d)
        options.draw_trajectory_in_2d = False
        Assert.assertFalse(options.draw_trajectory_in_2d)

        options.draw_trajectory_in_3d = False
        Assert.assertFalse(options.draw_trajectory_in_3d)
        options.draw_trajectory_in_3d = True
        Assert.assertTrue(options.draw_trajectory_in_3d)

        options.enable_logging = True
        Assert.assertTrue(options.enable_logging)
        options.enable_logging = False
        Assert.assertFalse(options.enable_logging)

        options.enable_segment_controls = True
        Assert.assertTrue(options.enable_segment_controls)
        options.enable_segment_controls = False
        Assert.assertFalse(options.enable_segment_controls)

        options.enable_segment_results = True
        Assert.assertTrue(options.enable_segment_results)
        options.enable_segment_results = False
        Assert.assertFalse(options.enable_segment_results)
        if TestBase.NoGraphicsMode:

            def action12():
                options.enable_trajectory_segment_colors = True

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action12)

        else:
            options.enable_trajectory_segment_colors = False
            Assert.assertFalse(options.enable_trajectory_segment_colors)
            options.enable_trajectory_segment_colors = True
            Assert.assertTrue(options.enable_trajectory_segment_colors)

        options.graphics_update_rate = 1
        Assert.assertEqual(1, options.graphics_update_rate)
        options.graphics_update_rate = 0.15
        Assert.assertEqual(0.15, options.graphics_update_rate)

        options.min_ephem_step = 0.1
        Assert.assertEqual(0.1, options.min_ephem_step)
        options.min_ephem_step = 1.0
        Assert.assertEqual(1.0, options.min_ephem_step)

        options.promote_controls = False
        Assert.assertFalse(options.promote_controls)
        options.promote_controls = True
        Assert.assertTrue(options.promote_controls)

        options.propagate_on_apply = True
        Assert.assertTrue(options.propagate_on_apply)
        options.propagate_on_apply = False
        Assert.assertFalse(options.propagate_on_apply)

        options.save_numbers_in_raw_format = True
        Assert.assertTrue(options.save_numbers_in_raw_format)
        options.save_numbers_in_raw_format = False
        Assert.assertFalse(options.save_numbers_in_raw_format)

        options.stopping_condition_time_tolerance = 1
        Assert.assertEqual(1, options.stopping_condition_time_tolerance)
        options.stopping_condition_time_tolerance = 1e-05
        Assert.assertEqual(1e-05, options.stopping_condition_time_tolerance)

        options.update_animation_time_for_all_objects = True
        Assert.assertTrue(options.update_animation_time_for_all_objects)
        options.update_animation_time_for_all_objects = False
        Assert.assertFalse(options.update_animation_time_for_all_objects)

        options.use_nominal_settings = True
        Assert.assertTrue(options.use_nominal_settings)
        options.use_nominal_settings = False
        Assert.assertFalse(options.use_nominal_settings)

        options.generate_ephemeris = True
        Assert.assertTrue(options.generate_ephemeris)
        options.generate_ephemeris = False
        Assert.assertFalse(options.generate_ephemeris)

        options.smart_run_mode = SMART_RUN_MODE.ONLY_CHANGED
        Assert.assertEqual(SMART_RUN_MODE.ONLY_CHANGED, options.smart_run_mode)
        options.smart_run_mode = SMART_RUN_MODE.ENTIRE_MISSION_CONTROL_SEQUENCE
        Assert.assertEqual(SMART_RUN_MODE.ENTIRE_MISSION_CONTROL_SEQUENCE, options.smart_run_mode)

        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - MCSOptions END")

    # endregion

    # region TestUserVariableDefinitionCollection
    def TestUserVariableDefinitionCollection(self, userVarDefnColl: "UserVariableDefinitionCollection"):
        countOrig: int = userVarDefnColl.count
        userVarDefnColl.add("Param1")
        Assert.assertEqual((countOrig + 1), userVarDefnColl.count)

        def action13():
            userVarDefnColl.remove("BogusParam")

        TryCatchAssertBlock.DoAssert(action13)

        userVarDefn: "UserVariableDefinition" = userVarDefnColl[0]
        userVarDefn.variable_name = "VarName"
        Assert.assertEqual("VarName", userVarDefn.variable_name)

        Assert.assertEqual("DistanceUnit", userVarDefn.unit_dimension)
        userVarDefn.unit_dimension = "AngleUnit"
        Assert.assertEqual("AngleUnit", userVarDefn.unit_dimension)

        def action14():
            userVarDefn.unit_dimension = "BogusUnit"

        TryCatchAssertBlock.DoAssert(action14)

        userVarDefnColl.remove("VarName")
        Assert.assertEqual(countOrig, userVarDefnColl.count)

        countOrig = userVarDefnColl.count
        userVarDefnColl.add("Param2")
        Assert.assertEqual((countOrig + 1), userVarDefnColl.count)

        userVarDefnColl.remove("Param2")
        Assert.assertEqual(countOrig, userVarDefnColl.count)

        i: int = 0
        while i < userVarDefnColl.count:
            userVarDefn2: "UserVariableDefinition" = userVarDefnColl[i]
            userVarDefn2A: "UserVariableDefinition" = userVarDefnColl.get_item_by_index(i)
            Assert.assertEqual(
                userVarDefn2.variable_name,
                userVarDefn2A.variable_name,
                "propget and GetItemByIndex should return same UserVariableDefinition",
            )

            i += 1

        userVarDefn3: "UserVariableDefinition"
        for userVarDefn3 in userVarDefnColl:
            varName: str = userVarDefn3.variable_name
            userVarDefn3A: "UserVariableDefinition" = userVarDefnColl.get_item_by_name(varName)
            Assert.assertEqual(
                userVarDefn3.variable_name,
                userVarDefn3A.variable_name,
                "propget and GetItemByName should return same UserVariableDefinition",
            )

        def action15():
            userVarDefn4: "UserVariableDefinition" = userVarDefnColl[userVarDefnColl.count]

        TryCatchAssertBlock.DoAssert(action15)

        userVarDefnColl.add("ForRemoveByIndex")
        userVarDefnColl.remove((userVarDefnColl.count - 1))

        def action16():
            userVarDefnColl.remove(userVarDefnColl.count)

        TryCatchAssertBlock.DoAssert(action16)

        userVarDefnColl.remove_all()
        Assert.assertEqual(0, userVarDefnColl.count)

    # endregion

    # region TestUserVariableCollection
    def TestUserVariableCollection(self, userVarColl: "UserVariableCollection"):
        countOrig: int = userVarColl.count

        userVar: "UserVariable"

        for userVar in userVarColl:
            s: str = userVar.unit_dimension
            userVarA: "UserVariable" = userVarColl.get_item_by_name(userVar.variable_name)
            Assert.assertEqual(
                userVar.variable_name, userVarA.variable_name, "GetItemByName should return correct UserVariable"
            )

        i: int = 0
        while i < userVarColl.count:
            s: str = userVarColl[i].unit_dimension
            userVarA: "UserVariable" = userVarColl.get_item_by_index(i)
            Assert.assertEqual(
                userVarColl[i].variable_name,
                userVarA.variable_name,
                "GetItemByIndex should return correct UserVariable",
            )

            i += 1

        def action17():
            userVar2: "UserVariable" = userVarColl[userVarColl.count]

        TryCatchAssertBlock.DoAssert(action17)

    # endregion

    # region TestUserVariableUpdateCollection
    def TestUserVariableUpdateCollection(self, userVarUpdateColl: "UserVariableUpdateCollection"):
        countOrig: int = userVarUpdateColl.count

        userVarUpdate: "UserVariableUpdate"

        for userVarUpdate in userVarUpdateColl:
            s: str = userVarUpdate.unit_dimension
            userVarUpdateA: "UserVariableUpdate" = userVarUpdateColl.get_item_by_name(userVarUpdate.variable_name)
            Assert.assertEqual(
                userVarUpdate.variable_name,
                userVarUpdateA.variable_name,
                "GetItemByName should return correct UserVariableUpdate",
            )

        i: int = 0
        while i < userVarUpdateColl.count:
            s: str = userVarUpdateColl[i].unit_dimension
            userVarUpdateA: "UserVariableUpdate" = userVarUpdateColl.get_item_by_index(i)
            Assert.assertEqual(
                userVarUpdateColl[i].variable_name,
                userVarUpdateA.variable_name,
                "GetItemByIndex should return correct UserVariableUpdate",
            )

            i += 1

        def action18():
            userVarUpdate2: "UserVariableUpdate" = userVarUpdateColl[userVarUpdateColl.count]

        TryCatchAssertBlock.DoAssert(action18)

    # endregion

    # region UserVariables
    def test_UserVariables(self):
        userVarDefn: "UserVariableDefinition" = EarlyBoundTests.AG_VA.options.user_variables.add("test1")
        userVarDefn.unit_dimension = "DistanceUnit"
        Assert.assertEqual("DistanceUnit", userVarDefn.unit_dimension)

        initialState: "MissionControlSequenceInitialState" = clr.CastAs(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "test", "-"),
            MissionControlSequenceInitialState,
        )
        Assert.assertEqual("test1", initialState.user_variables[0].variable_name)
        Assert.assertEqual(0.001, initialState.user_variables[0].variable_value)
        initialState.user_variables[0].variable_value = 2
        Assert.assertEqual(2, initialState.user_variables[0].variable_value)
        Assert.assertFalse(initialState.user_variables[0].control_parameters_available)
        self.TestUserVariableCollection(initialState.user_variables)

        launch: "MissionControlSequenceLaunch" = clr.CastAs(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.LAUNCH, "launch1", "-"),
            MissionControlSequenceLaunch,
        )
        Assert.assertEqual("test1", launch.user_variables[0].variable_name)
        Assert.assertEqual(0.001, launch.user_variables[0].variable_value)
        launch.user_variables[0].variable_value = 3
        Assert.assertEqual(3, launch.user_variables[0].variable_value)
        Assert.assertFalse(launch.user_variables[0].control_parameters_available)
        self.TestUserVariableCollection(launch.user_variables)

        follow: "MissionControlSequenceFollow" = clr.CastAs(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.FOLLOW, "follow1", "-"),
            MissionControlSequenceFollow,
        )
        Assert.assertEqual("test1", follow.user_variables[0].variable_name)
        Assert.assertEqual(0.001, follow.user_variables[0].variable_value)
        follow.user_variables[0].variable_value = 4
        Assert.assertEqual(4, follow.user_variables[0].variable_value)
        Assert.assertFalse(follow.user_variables[0].control_parameters_available)
        self.TestUserVariableCollection(follow.user_variables)

        update: "MissionControlSequenceUpdate" = clr.CastAs(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.UPDATE, "update1", "-"),
            MissionControlSequenceUpdate,
        )
        Assert.assertEqual("test1", update.user_variables[0].variable_name)
        Assert.assertEqual("DistanceUnit", update.user_variables[0].unit_dimension)
        update.user_variables[0].variable_action = UPDATE_ACTION.ADD_VALUE
        Assert.assertEqual(UPDATE_ACTION.ADD_VALUE, update.user_variables[0].variable_action)
        self.TestUserVariableUpdateCollection(update.user_variables)

        update.user_variables[0].variable_action = UPDATE_ACTION.NO_CHANGE
        Assert.assertEqual(UPDATE_ACTION.NO_CHANGE, update.user_variables[0].variable_action)

        update.user_variables[0].variable_action = UPDATE_ACTION.SET_TO_NEW_VALUE
        Assert.assertEqual(UPDATE_ACTION.SET_TO_NEW_VALUE, update.user_variables[0].variable_action)

        update.user_variables[0].variable_action = UPDATE_ACTION.SUBTRACT_VALUE
        Assert.assertEqual(UPDATE_ACTION.SUBTRACT_VALUE, update.user_variables[0].variable_action)

        Assert.assertEqual("DistanceUnit", update.user_variables[0].unit_dimension)
        Assert.assertEqual(0, update.user_variables[0].variable_value)
        update.user_variables[0].variable_value = 10
        Assert.assertEqual(10, update.user_variables[0].variable_value)
        Assert.assertFalse(update.user_variables[0].control_parameters_available)

        ts: "MissionControlSequenceTargetSequence" = clr.CastAs(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "ts1", "-"),
            MissionControlSequenceTargetSequence,
        )
        initState2: "MissionControlSequenceInitialState" = clr.CastAs(
            ts.segments.insert_copy(clr.Convert(initialState, IMissionControlSequenceSegment), "-"),
            MissionControlSequenceInitialState,
        )
        launch2: "MissionControlSequenceLaunch" = clr.CastAs(
            ts.segments.insert_copy(clr.Convert(launch, IMissionControlSequenceSegment), "-"),
            MissionControlSequenceLaunch,
        )
        follow2: "MissionControlSequenceFollow" = clr.CastAs(
            ts.segments.insert_copy(clr.Convert(follow, IMissionControlSequenceSegment), "-"),
            MissionControlSequenceFollow,
        )
        update2: "MissionControlSequenceUpdate" = clr.CastAs(
            ts.segments.insert_copy(clr.Convert(update, IMissionControlSequenceSegment), "-"),
            MissionControlSequenceUpdate,
        )

        Assert.assertTrue(initState2.user_variables[0].control_parameters_available)
        initState2.user_variables[0].enable_control_parameter()
        Assert.assertTrue(initState2.user_variables[0].is_control_parameter_enabled())
        Assert.assertEqual(1, (clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)).control_parameters.count)
        initState2.user_variables[0].disable_control_parameter()
        Assert.assertFalse(initState2.user_variables[0].is_control_parameter_enabled())
        Assert.assertEqual(0, (clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)).control_parameters.count)

        Assert.assertTrue(launch2.user_variables[0].control_parameters_available)
        launch2.user_variables[0].enable_control_parameter()
        Assert.assertTrue(launch2.user_variables[0].is_control_parameter_enabled())
        Assert.assertEqual(1, (clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)).control_parameters.count)
        launch2.user_variables[0].disable_control_parameter()
        Assert.assertFalse(launch2.user_variables[0].is_control_parameter_enabled())
        Assert.assertEqual(0, (clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)).control_parameters.count)

        Assert.assertTrue(follow2.user_variables[0].control_parameters_available)
        follow2.user_variables[0].enable_control_parameter()
        Assert.assertTrue(follow2.user_variables[0].is_control_parameter_enabled())
        Assert.assertEqual(1, (clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)).control_parameters.count)
        follow2.user_variables[0].disable_control_parameter()
        Assert.assertFalse(follow2.user_variables[0].is_control_parameter_enabled())
        Assert.assertEqual(0, (clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)).control_parameters.count)

        Assert.assertTrue(update2.user_variables[0].control_parameters_available)
        update2.user_variables[0].enable_control_parameter()
        Assert.assertTrue(update2.user_variables[0].is_control_parameter_enabled())
        Assert.assertEqual(1, (clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)).control_parameters.count)
        update2.user_variables[0].disable_control_parameter()
        Assert.assertFalse(update2.user_variables[0].is_control_parameter_enabled())
        Assert.assertEqual(0, (clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)).control_parameters.count)
        EarlyBoundTests.AG_VA.main_sequence.remove_all()

        self.TestUserVariableDefinitionCollection(EarlyBoundTests.AG_VA.options.user_variables)

    # endregion

    # region SegCollections
    def test_SegCollections(self):
        #
        #  MissionControlSequenceSegmentCollection
        #

        mcsSegColl: "MissionControlSequenceSegmentCollection" = EarlyBoundTests.AG_VA.main_sequence

        GatorHelper.TestRuntimeTypeInfo(mcsSegColl)

        initialSegCount: int = mcsSegColl.count

        mcsSegment: "IMissionControlSequenceSegment"

        for mcsSegment in mcsSegColl:
            compInfo: "IComponentInfo" = clr.CastAs(mcsSegment, IComponentInfo)
            compInfoB: "IComponentInfo" = clr.CastAs(mcsSegColl.get_item_by_name(compInfo.name), IComponentInfo)
            TestBase.logger.WriteLine5("Segment name: {0}", compInfoB.name)
            Assert.assertIsNotNone(compInfo, "compInfo should not be null")
            Assert.assertIsNotNone(compInfoB, "compInfoB should not be null")
            Assert.assertEqual(
                compInfo.name,
                compInfoB.name,
                "Indexing collection using propget and GetItemByName should yield same ComponentInfo.",
            )
            TestBase.logger.WriteLine5("Segment name: {0}", compInfo.name)

        i: int = 0
        while i < mcsSegColl.count:
            compInfo: "IComponentInfo" = clr.Convert(mcsSegColl[i], IComponentInfo)
            compInfoB: "IComponentInfo" = clr.Convert(mcsSegColl.get_item_by_index(i), IComponentInfo)
            Assert.assertIsNotNone(compInfo, "compInfo should not be null")
            Assert.assertIsNotNone(compInfoB, "compInfoB should not be null")
            Assert.assertEqual(
                compInfo.name,
                compInfoB.name,
                "Indexing collection using propget and GetItemByIndex should yield same ComponentInfo.",
            )
            TestBase.logger.WriteLine5("Segment name: {0}", compInfo.name)

            i += 1

        def action19():
            compInfo: "IComponentInfo" = clr.Convert(mcsSegColl.get_item_by_index(mcsSegColl.count), IComponentInfo)

        TryCatchAssertBlock.ExpectedException("not found", action19)

        def action20():
            compInfo: "IComponentInfo" = clr.Convert(mcsSegColl.get_item_by_name("Bogus"), IComponentInfo)

        TryCatchAssertBlock.ExpectedException("value was not found", action20)

        mcsSegColl.insert(SEGMENT_TYPE.BACKWARD_SEQUENCE, "Seg1", "-")
        mcsSegColl.insert(SEGMENT_TYPE.BACKWARD_SEQUENCE, "Seg2", "Seg1")
        mcsSegColl.insert(SEGMENT_TYPE.BACKWARD_SEQUENCE, "Seg3", "Seg2")
        Assert.assertEqual((initialSegCount + 3), mcsSegColl.count, "count1 is wrong")

        mcsSegColl.insert_by_name("Launch", "Seg2")
        Assert.assertEqual((initialSegCount + 4), mcsSegColl.count, "count1a is wrong")
        mcsSegColl.remove("Launch")
        Assert.assertEqual((initialSegCount + 3), mcsSegColl.count, "count1b is wrong")

        def action21():
            mcsSegColl.insert_by_name("Launch", "BogusSeg")

        TryCatchAssertBlock.DoAssert(action21)

        def action22():
            mcsSegColl.insert_by_name("LaunchBogus", "Seg2")

        TryCatchAssertBlock.DoAssert(action22)

        mcsSegColl.remove("Seg2")
        Assert.assertEqual((initialSegCount + 2), mcsSegColl.count, "count2 is wrong")

        def action23():
            mcsSegColl.remove("BogusSeg")

        TryCatchAssertBlock.DoAssert(action23)

        def action24():
            mcsSegColl.remove("-")

        TryCatchAssertBlock.DoAssert(action24)

        mcsSegColl.remove_all()
        Assert.assertEqual(1, mcsSegColl.count, "count should be 1")  # End of Sequence segment should remain.

        #
        #  AutomaticSequenceCollection
        #

        autoSeqColl: "AutomaticSequenceCollection" = EarlyBoundTests.AG_VA.auto_sequence
        Assert.assertEqual(1, autoSeqColl.count, "AutoSeq count should be 1")

        autoSeqColl.add("AutoSeq1")
        autoSeqColl.add("AutoSeq2")
        Assert.assertEqual(3, autoSeqColl.count, "AutoSeq count should be 3")

        i: int = 0
        while i < autoSeqColl.count:
            as1: "AutomaticSequence" = autoSeqColl[i]
            as1b: "AutomaticSequence" = autoSeqColl.get_item_by_index(i)
            Assert.assertEqual(
                as1.name, as1b.name, "Indexing collection with propget and GetItemByIndex should return same AutoSeq"
            )

            i += 1

        as2: "AutomaticSequence" = autoSeqColl["Stop"]

        as3: "AutomaticSequence"

        for as3 in autoSeqColl:
            name: str = as3.name
            as3b: "AutomaticSequence" = autoSeqColl.get_item_by_name(name)
            Assert.assertEqual(
                as3.name, as3b.name, "Indexing collection with propget and GetItemByName should return same AutoSeq"
            )

        def action25():
            as4: "AutomaticSequence" = autoSeqColl[3]

        TryCatchAssertBlock.DoAssert(action25)

        def action26():
            as4a: "AutomaticSequence" = autoSeqColl.get_item_by_index(3)

        TryCatchAssertBlock.ExpectedException("Index Out of Range", action26)

        def action27():
            as5: "AutomaticSequence" = autoSeqColl["Bogus"]

        TryCatchAssertBlock.DoAssert(action27)

        def action28():
            as5a: "AutomaticSequence" = autoSeqColl.get_item_by_name("Bogus")

        TryCatchAssertBlock.ExpectedException("Item specified by ItemOrName could not be found", action28)

        bFirstTime: bool = True
        autoSeq: "AutomaticSequence"
        for autoSeq in autoSeqColl:
            if not bFirstTime:
                # The first sequence is read only
                autoSeq.name = "MyAutoSeqName"
                Assert.assertEqual("MyAutoSeqName", autoSeq.name, "unexpected autoSeq.Name")
                autoSeq.user_comment = "MyAutoSeqUserComment"
                Assert.assertEqual("MyAutoSeqUserComment", autoSeq.user_comment, "unexpected autoSeq.UserComment")

            bFirstTime = False

            autoSeqColl2: "MissionControlSequenceSegmentCollection" = autoSeq.sequence

        autoSeqColl.remove(1)
        Assert.assertEqual(2, autoSeqColl.count)

        def action29():
            autoSeqColl.remove(2)

        TryCatchAssertBlock.DoAssert(action29)

        def action30():
            autoSeqColl.remove("Bogus")

        TryCatchAssertBlock.DoAssert(action30)

        copyAutoSeq: "AutomaticSequence" = autoSeqColl[0].make_copy("MyCopyName")
        Assert.assertEqual("MyCopyName", copyAutoSeq.name, "unexpected MyCopyName")

        autoSeqColl.remove("MyAutoSeqName")
        Assert.assertEqual(2, autoSeqColl.count, "AutoSeq count should be 2")

        GatorHelper.TestRuntimeTypeInfo(mcsSegColl)

        TestBase.LoadTestScenario(Path.Combine("AstrogatorTests", "AstrogatorTests.sc"))
        EarlyBoundTests.AG_SAT = clr.Convert(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        EarlyBoundTests.AG_VA = clr.Convert(EarlyBoundTests.AG_SAT.propagator, DriverMissionControlSequence)

    # endregion

    # region NestedTargetSequence
    def test_NestedTargetSequence(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - NestedTargetSequence START")
        ts1: "MissionControlSequenceTargetSequence" = clr.CastAs(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Tg1", "-"),
            MissionControlSequenceTargetSequence,
        )
        ts2: "MissionControlSequenceTargetSequence" = clr.CastAs(
            ts1.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Tg2", "-"), MissionControlSequenceTargetSequence
        )
        launch: "MissionControlSequenceLaunch" = clr.CastAs(
            ts2.segments.insert(SEGMENT_TYPE.LAUNCH, "Launch", "-"), MissionControlSequenceLaunch
        )
        launch.enable_control_parameter(CONTROL_LAUNCH.EPOCH)
        EarlyBoundTests.AG_VA.options.promote_controls = True
        dc: "ProfileDifferentialCorrector" = clr.CastAs(
            ts1.profiles["Differential Corrector"], ProfileDifferentialCorrector
        )
        cp: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths("Tg2.Launch", "Launch.Epoch")
        Assert.assertEqual("Launch.Epoch", cp.name)
        EarlyBoundTests.AG_VA.options.promote_controls = False

        def action31():
            cp = dc.control_parameters.get_control_by_paths("Tg2.Launch", "Launch.Epoch")

        TryCatchAssertBlock.DoAssert(action31)

        try:
            seg: "IMissionControlSequenceSegment" = ts2.segments["SegBogus"]
            Assert.fail("SegBogus should not exist and should throw an exception.")

        except Exception as e:
            # Expected exception
            msg: str = str(e)
            Assert.assertEqual("Segment specified by Index value was not found.", msg)
            TestBase.logger.WriteLine(msg)

        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - NestedTargetSequence END")

    # endregion

    # region InitialState
    def test_InitialState(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - InitialState START")
        initState: "MissionControlSequenceInitialState" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitState", "Propagate"),
            MissionControlSequenceInitialState,
        )
        GatorHelper.TestInitialState(initState, False, TestBase.Application)
        GatorHelper.TestRuntimeTypeInfo(initState)
        self.TestSegment(clr.CastAs(initState, IMissionControlSequenceSegment))
        oInitState: "IMissionControlSequenceSegment" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence[0], IMissionControlSequenceSegment
        )

        GatorHelper.TestOrbitState(oInitState.initial_state)

        osEFFrame1: "State" = oInitState.initial_state.get_in_frame_name("CentralBody/Earth Fixed")
        Assert.assertIsNotNone(osEFFrame1)
        GatorHelper.TestOrbitState(osEFFrame1)

        GatorHelper.TestOrbitState(oInitState.run())
        osEFFrame2: "State" = oInitState.run().get_in_frame_name("CentralBody/Earth Fixed")
        Assert.assertIsNotNone(osEFFrame2)
        GatorHelper.TestOrbitState(osEFFrame2)

        GatorHelper.TestRuntimeTypeInfo(initState)

        EarlyBoundTests.AG_VA.main_sequence.remove("InitState")

        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - InitialState END")

    # endregion

    # region Propagate
    def test_Propagate(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Propagate START")
        propagate: "MissionControlSequencePropagate" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop1", "Propagate"),
            MissionControlSequencePropagate,
        )
        GatorHelper.TestPropagate(propagate, False)
        self.TestSegment(clr.CastAs(propagate, IMissionControlSequenceSegment))
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Propagate END")

    # endregion

    # region TestStopping
    def test_TestStopping(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - TestStopping START")
        propagate: "MissionControlSequencePropagate" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop1", "Propagate"),
            MissionControlSequencePropagate,
        )
        segment: "IMissionControlSequenceSegment" = clr.CastAs(propagate, IMissionControlSequenceSegment)
        self.TestSegment(segment)
        Assert.assertEqual(SEGMENT_TYPE.PROPAGATE, segment.type)
        propagate.propagator_name = "Earth Point Mass"
        Assert.assertEqual("Earth Point Mass", propagate.propagator_name)

        sc1: "AccessStoppingCondition" = clr.Convert(
            propagate.stopping_conditions.add("Access").properties, AccessStoppingCondition
        )

        temp1: "AccessStoppingCondition" = clr.Convert(
            propagate.stopping_conditions["Access"].properties, AccessStoppingCondition
        )
        Assert.assertEqual((clr.Convert(sc1, IComponentInfo)).name, (clr.Convert(temp1, IComponentInfo)).name)

        sc1.criterion = ACCESS_CRITERION.GAIN
        Assert.assertEqual(ACCESS_CRITERION.GAIN, sc1.criterion)
        sc1.criterion = ACCESS_CRITERION.LOSE
        Assert.assertEqual(ACCESS_CRITERION.LOSE, sc1.criterion)
        sc1.criterion = ACCESS_CRITERION.EITHER
        Assert.assertEqual(ACCESS_CRITERION.EITHER, sc1.criterion)

        sc1.set_base_selection(BASE_SELECTION.SPECIFY)
        Assert.assertEqual(BASE_SELECTION.SPECIFY, sc1.base_selection_type, "wrong BaseSelectionType")
        sc1.base_selection.bind_to("Satellite/Satellite1")
        Assert.assertEqual("Satellite/Satellite1", sc1.base_selection.name)

        sc1.target_object.bind_to("Facility/Facility1")
        Assert.assertEqual("Facility/Facility1", sc1.target_object.name)
        sc1.target_object.bind_to("Star/Star1")
        Assert.assertEqual("Star/Star1", sc1.target_object.name)

        def action32():
            sc1.base_selection.bind_to("Planet/Planet1")

        TryCatchAssertBlock.DoAssert(action32)

        sc1.target_object.bind_to("Facility/Facility1")
        sc1.base_selection.bind_to("Planet/Planet1")

        def action33():
            sc1.target_object.bind_to("Star/Star1")

        TryCatchAssertBlock.DoAssert(action33)

        sc1.base_selection.bind_to("Aircraft/Boing737")

        sc1.use_light_time_delay = False
        Assert.assertFalse(sc1.use_light_time_delay)
        sc1.use_light_time_delay = True
        Assert.assertTrue(sc1.use_light_time_delay)

        sc1.clock_host = IV_CLOCK_HOST.TARGET
        Assert.assertEqual(IV_CLOCK_HOST.TARGET, sc1.clock_host)
        sc1.clock_host = IV_CLOCK_HOST.BASE
        Assert.assertEqual(IV_CLOCK_HOST.BASE, sc1.clock_host)

        sc1.base_selection.bind_to("Satellite/Satellite1")

        def action34():
            sc1.clock_host = IV_CLOCK_HOST.BASE

        TryCatchAssertBlock.DoAssert(action34)

        sc1.base_selection.bind_to("Planet/Planet1")

        def action35():
            sc1.clock_host = IV_CLOCK_HOST.BASE

        TryCatchAssertBlock.DoAssert(action35)

        sc1.base_selection.bind_to("Aircraft/Boing737")
        sc1.target_object.bind_to("Satellite/Satellite1")

        def action36():
            sc1.clock_host = IV_CLOCK_HOST.BASE

        TryCatchAssertBlock.DoAssert(action36)

        sc1.target_object.bind_to("Planet/Planet1")

        def action37():
            sc1.clock_host = IV_CLOCK_HOST.BASE

        TryCatchAssertBlock.DoAssert(action37)

        sc1.target_object.bind_to("Facility/Facility1")

        sc1.signal_sense = IV_TIME_SENSE.RECEIVE
        Assert.assertEqual(IV_TIME_SENSE.RECEIVE, sc1.signal_sense)
        sc1.signal_sense = IV_TIME_SENSE.TRANSMIT
        Assert.assertEqual(IV_TIME_SENSE.TRANSMIT, sc1.signal_sense)

        sc1.time_convergence = 1.11e-05
        Assert.assertEqual(1.11e-05, sc1.time_convergence)

        sc1.aberration_type = ABERRATION_TYPE.NONE
        Assert.assertEqual(ABERRATION_TYPE.NONE, sc1.aberration_type)
        sc1.aberration_type = ABERRATION_TYPE.ANNUAL
        Assert.assertEqual(ABERRATION_TYPE.ANNUAL, sc1.aberration_type)
        sc1.aberration_type = ABERRATION_TYPE.TOTAL
        Assert.assertEqual(ABERRATION_TYPE.TOTAL, sc1.aberration_type)

        sc1.time_delay_convergence_tolerance = 1
        Assert.assertEqual(1, sc1.time_delay_convergence_tolerance)

        Assert.assertEqual(0, sc1.before_conditions.count, "incorrect BeforeConditions Count")

        constraintCollection: "ConstraintCollection" = sc1.constraints

        sc1.inherited = False
        Assert.assertFalse(sc1.inherited)
        sc1.inherited = True
        Assert.assertTrue(sc1.inherited)

        def action38():
            sc1.max_trip_times = 10001

        TryCatchAssertBlock.ExpectedException("read-only", action38)

        sc1.repeat_count = 2
        Assert.assertEqual(2, sc1.repeat_count)
        sc1.repeat_count = 1
        Assert.assertEqual(1, sc1.repeat_count)

        sc1.sequence = "Stop"
        Assert.assertEqual("Stop", sc1.sequence)

        sc1.base_selection.bind_to("Satellite/Satellite1")

        sc: "LightingStoppingCondition" = clr.Convert(
            propagate.stopping_conditions.add("Lighting").properties, LightingStoppingCondition
        )
        temp: "LightingStoppingCondition" = clr.Convert(
            propagate.stopping_conditions["Lighting"].properties, LightingStoppingCondition
        )

        scc: "StoppingConditionCollection" = sc.before_conditions
        constraintCollection2: "ConstraintCollection" = sc.constraints

        sc.eclipsing_bodies_list_source = ECLIPSING_BODIES_SOURCE.USER_DEFINED
        Assert.assertEqual(ECLIPSING_BODIES_SOURCE.USER_DEFINED, sc.eclipsing_bodies_list_source)
        sc.add_eclipsing_body("Sun")

        def action39():
            sc.add_eclipsing_body("Bogus")

        TryCatchAssertBlock.DoAssert(action39)

        assigned = sc.eclipsing_bodies

        i: int = 0
        while i < Array.Length(assigned):
            TestBase.logger.WriteLine2(assigned[i])

            i += 1

        sc.remove_eclipsing_body("Sun")

        def action40():
            sc.remove_eclipsing_body("Bogus")

        TryCatchAssertBlock.DoAssert(action40)

        available = sc.available_eclipsing_bodies

        i: int = 0
        while i < Array.Length(available):
            TestBase.logger.WriteLine2(available[i])

            i += 1

        sc.inherited = True
        Assert.assertTrue(sc.inherited)

        def action41():
            sc.max_trip_times = 10001.0

        TryCatchAssertBlock.ExpectedException("read-only", action41)

        sc.repeat_count = 1.0
        Assert.assertEqual(1.0, sc.repeat_count)

        sc.sequence = "Stop"
        Assert.assertEqual("Stop", sc.sequence)

        sct: "STOPPING_CONDITION" = sc.stopping_condition_type

        Assert.assertEqual((clr.Convert(sc, IComponentInfo)).name, (clr.Convert(temp, IComponentInfo)).name)
        sc.condition = LIGHTING_CONDITION.CRITERION_ENTER_DIRECT_SUN
        Assert.assertEqual(LIGHTING_CONDITION.CRITERION_ENTER_DIRECT_SUN, sc.condition)
        sc.condition = LIGHTING_CONDITION.CRITERION_EXIT_DIRECT_SUN
        Assert.assertEqual(LIGHTING_CONDITION.CRITERION_EXIT_DIRECT_SUN, sc.condition)
        sc.condition = LIGHTING_CONDITION.CRITERION_ENTER_UMBRA
        Assert.assertEqual(LIGHTING_CONDITION.CRITERION_ENTER_UMBRA, sc.condition)
        sc.condition = LIGHTING_CONDITION.CRITERION_EXIT_UMBRA
        Assert.assertEqual(LIGHTING_CONDITION.CRITERION_EXIT_UMBRA, sc.condition)

        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - TestStopping END")

    # endregion

    # region Sequence
    def test_Sequence(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Sequence START")
        ts: "IMissionControlSequenceSequence" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.SEQUENCE, "Sequence1", "Propagate"),
            IMissionControlSequenceSequence,
        )
        GatorHelper.TestSequence(ts, SEGMENT_TYPE.SEQUENCE, False)
        self.TestSegment(clr.CastAs(ts, IMissionControlSequenceSegment))
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Sequence END")

    # endregion

    # region BackwardSequence
    def test_BackwardSequence(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - BackwardSequence START")
        ts: "MissionControlSequenceBackwardSequence" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(
                SEGMENT_TYPE.BACKWARD_SEQUENCE, "BackwardsSequence", "Propagate"
            ),
            MissionControlSequenceBackwardSequence,
        )
        GatorHelper.TestSequence(ts, SEGMENT_TYPE.BACKWARD_SEQUENCE, False)
        GatorHelper.TestRuntimeTypeInfo(ts)
        self.TestSegment(clr.CastAs(ts, IMissionControlSequenceSegment))
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - BackwardSequence END")

    # endregion

    # region Launch
    def test_Launch(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Launch START")
        launch: "MissionControlSequenceLaunch" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.LAUNCH, "Launcher", "Propagate"),
            MissionControlSequenceLaunch,
        )
        GatorHelper.TestLaunch(launch, False)
        self.TestSegment(clr.CastAs(launch, IMissionControlSequenceSegment))
        EarlyBoundTests.AG_VA.main_sequence.remove("Launcher")
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Launch END")

    # endregion

    # region Follow
    def test_Follow(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Follow START")
        follow: "MissionControlSequenceFollow" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.FOLLOW, "Follow", "-"), MissionControlSequenceFollow
        )
        follow.leader.bind_to("Missile/Missile1")
        Assert.assertEqual("Missile/Missile1", follow.leader.name)
        Assert.assertIsNotNone(follow.leader.linked_object)
        self.TestSegment(clr.CastAs(follow, IMissionControlSequenceSegment))

        follow.x_offset = 1
        Assert.assertEqual(1, follow.x_offset)
        follow.y_offset = 2
        Assert.assertEqual(2, follow.y_offset)
        follow.z_offset = 3
        Assert.assertEqual(3, follow.z_offset)

        GatorHelper.TestSpaceCraftParameters(follow.spacecraft_parameters, False)
        GatorHelper.TestFuelTank(follow.fuel_tank, False, False)

        GatorHelper.TestStoppingConditionCollection(follow.separation_conditions)
        GatorHelper.TestStoppingConditionCollection(follow.joining_conditions)

        follow.joining_type = FOLLOW_JOIN.AT_BEGINNING
        Assert.assertEqual(FOLLOW_JOIN.AT_BEGINNING, follow.joining_type)
        follow.joining_type = FOLLOW_JOIN.AT_END
        Assert.assertEqual(follow.joining_type, FOLLOW_JOIN.AT_END)
        follow.joining_type = FOLLOW_JOIN.AT_FINAL_EPOCH_OF_PREVIOUS_SEG
        Assert.assertEqual(FOLLOW_JOIN.AT_FINAL_EPOCH_OF_PREVIOUS_SEG, follow.joining_type)
        follow.joining_type = FOLLOW_JOIN.SPECIFY
        Assert.assertEqual(FOLLOW_JOIN.SPECIFY, follow.joining_type)

        follow.separation_type = FOLLOW_SEPARATION.AT_END_OF_LEADERS_EPHEM
        Assert.assertEqual(FOLLOW_SEPARATION.AT_END_OF_LEADERS_EPHEM, follow.separation_type)
        follow.separation_type = FOLLOW_SEPARATION.SPECIFY
        Assert.assertEqual(FOLLOW_SEPARATION.SPECIFY, follow.separation_type)

        follow.spacecraft_and_fuel_tank_type = FOLLOW_SPACECRAFT_AND_FUEL_TANK.INHERIT
        Assert.assertEqual(FOLLOW_SPACECRAFT_AND_FUEL_TANK.INHERIT, follow.spacecraft_and_fuel_tank_type)
        follow.spacecraft_and_fuel_tank_type = FOLLOW_SPACECRAFT_AND_FUEL_TANK.SPECIFY
        Assert.assertEqual(FOLLOW_SPACECRAFT_AND_FUEL_TANK.SPECIFY, follow.spacecraft_and_fuel_tank_type)

        try:
            follow.spacecraft_and_fuel_tank_type = FOLLOW_SPACECRAFT_AND_FUEL_TANK.LEADER
            Assert.fail("Setting spacecraft config type to leader is invalid for non Astrogator satellites.")

        except Exception as ex:
            Assert.assertEqual(
                "Enumeration, must be in {Inherit Configuration From Previous Segment, Specify Configuration}", str(ex)
            )

        # in order to set to inherit from leader, need an astrogator satellite to be the leader
        leader: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "AstgLeader57325"), Satellite
        )
        leader.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        follow.leader.bind_to((clr.Convert(leader, IStkObject)).path)
        Assert.assertEqual(follow.leader.name, "Satellite/AstgLeader57325")

        follow.spacecraft_and_fuel_tank_type = FOLLOW_SPACECRAFT_AND_FUEL_TANK.LEADER
        Assert.assertEqual(FOLLOW_SPACECRAFT_AND_FUEL_TANK.LEADER, follow.spacecraft_and_fuel_tank_type)
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "AstgLeader57325")

        EarlyBoundTests.AG_VA.main_sequence.remove("Follow")

        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Follow END")

    # endregion

    # region Maneuver
    def test_Maneuver(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Maneuver START")
        maneuver: "MissionControlSequenceManeuver" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Man1", "-"),
            MissionControlSequenceManeuver,
        )
        self.TestSegment(clr.CastAs(maneuver, IMissionControlSequenceSegment))
        GatorHelper.TestManeuver(maneuver, False)
        GatorHelper.TestRuntimeTypeInfo(maneuver)
        EarlyBoundTests.AG_VA.main_sequence.remove("Man1")
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Maneuver END")

    # endregion

    # region Maneuver_OptimalFinite
    def test_Maneuver_OptimalFinite(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Maneuver_OptimalFinite START")
        if ((self.Target != TestTarget.eStkX)) and ((self.Target != TestTarget.eStkNoGfx)):
            maneuver: "MissionControlSequenceManeuver" = clr.Convert(
                EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Man2", "-"),
                MissionControlSequenceManeuver,
            )
            self.TestSegment(clr.CastAs(maneuver, IMissionControlSequenceSegment))
            GatorHelper.TestManeuver_OptimalFinite(maneuver, False, TestBase.Application)
            GatorHelper.TestRuntimeTypeInfo(maneuver)
            EarlyBoundTests.AG_VA.main_sequence.remove("Man2")

        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Maneuver_OptimalFinite END")

    # endregion

    # region Hold
    def test_Hold(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Hold START")
        hold: "MissionControlSequenceHold" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.HOLD, "Holder1", "-"), MissionControlSequenceHold
        )
        self.TestSegment(clr.CastAs(hold, IMissionControlSequenceSegment))
        GatorHelper.TestRuntimeTypeInfo(hold)

        hold.min_propagation_time = 0
        Assert.assertEqual(0, hold.min_propagation_time)
        hold.max_propagation_time = 2
        Assert.assertEqual(2, hold.max_propagation_time)
        hold.enable_warning_message = False
        Assert.assertFalse(hold.enable_warning_message)
        hold.override_max_propagation_time = True
        Assert.assertTrue(hold.override_max_propagation_time)
        hold.override_max_propagation_time = False
        Assert.assertFalse(hold.override_max_propagation_time)
        hold.enable_max_propagation_time = False
        Assert.assertFalse(hold.enable_max_propagation_time)

        hold.should_stop_for_initially_surpassed_epoch_stopping_conditions = True
        Assert.assertTrue(hold.should_stop_for_initially_surpassed_epoch_stopping_conditions)
        hold.should_stop_for_initially_surpassed_epoch_stopping_conditions = False
        Assert.assertFalse(hold.should_stop_for_initially_surpassed_epoch_stopping_conditions)

        hold.enable_hold_attitude = True
        Assert.assertTrue(hold.enable_hold_attitude)
        hold.enable_hold_attitude = False
        Assert.assertFalse(hold.enable_hold_attitude)
        hold.hold_frame_name = "CentralBody/Earth Mean of Date"
        Assert.assertEqual("CentralBody/Earth Mean_of_Date", hold.hold_frame_name)
        hold.step_size = 2
        Assert.assertEqual(2, hold.step_size)
        GatorHelper.TestStoppingConditionCollection(hold.stopping_conditions)

        Assert.assertFalse(hold.control_parameters_available)
        Assert.assertFalse(hold.is_control_parameter_enabled(CONTROL_ADVANCED.PROPAGATE_MAX_PROP_TIME))

        def action42():
            hold.enable_control_parameter(CONTROL_ADVANCED.PROPAGATE_MAX_PROP_TIME)

        TryCatchAssertBlock.DoAssert(action42)

        def action43():
            hold.disable_control_parameter(CONTROL_ADVANCED.PROPAGATE_MAX_PROP_TIME)

        TryCatchAssertBlock.DoAssert(action43)

        EarlyBoundTests.AG_VA.main_sequence.remove("Holder1")

        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Hold END")

    # endregion

    # region Update
    def test_Update(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Update START")
        update: "MissionControlSequenceUpdate" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.UPDATE, "Updater1", "-"),
            MissionControlSequenceUpdate,
        )
        GatorHelper.TestUpdate(update, False)
        self.TestSegment(clr.CastAs(update, IMissionControlSequenceSegment))
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Update END")

    # endregion

    # region ReturnSegment
    def test_ReturnSegment(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Return START")
        target: "MissionControlSequenceTargetSequence" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "target", "-"),
            MissionControlSequenceTargetSequence,
        )
        self.TestSegment(clr.CastAs(target, IMissionControlSequenceSegment))

        ret: "MissionControlSequenceReturn" = clr.Convert(
            target.segments.insert(SEGMENT_TYPE.RETURN, "returner1", "-"), MissionControlSequenceReturn
        )
        self.TestSegment(clr.CastAs(ret, IMissionControlSequenceSegment))
        GatorHelper.TestRuntimeTypeInfo(ret)

        ret.return_control_to_parent_sequence = RETURN_CONTROL.DISABLE
        Assert.assertEqual(RETURN_CONTROL.DISABLE, ret.return_control_to_parent_sequence)

        ret.return_control_to_parent_sequence = RETURN_CONTROL.ENABLE
        Assert.assertEqual(RETURN_CONTROL.ENABLE, ret.return_control_to_parent_sequence)

        ret.return_control_to_parent_sequence = RETURN_CONTROL.ENABLE_EXCEPT_PROFILES_BYPASS
        Assert.assertEqual(RETURN_CONTROL.ENABLE_EXCEPT_PROFILES_BYPASS, ret.return_control_to_parent_sequence)
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Return END")

    # endregion

    # region Stop
    def test_Stop(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Stop START")

        mcsSegColl: "MissionControlSequenceSegmentCollection" = EarlyBoundTests.AG_VA.main_sequence
        mcsSegment: "IMissionControlSequenceSegment"
        for mcsSegment in mcsSegColl:
            compInfo: "IComponentInfo" = clr.CastAs(mcsSegment, IComponentInfo)
            Assert.assertIsNotNone(compInfo, "compInfo should not be null")
            TestBase.logger.WriteLine5("Segment name: {0}", compInfo.name)
            TestBase.logger.WriteLine6("Segment type: {0}", mcsSegment.type)
            if compInfo.name == "-":
                end: "MissionControlSequenceEnd" = clr.CastAs(compInfo, MissionControlSequenceEnd)
                GatorHelper.TestRuntimeTypeInfo(end)
                Assert.assertIsNotNone(end)

                GatorHelper.TestRuntimeTypeInfo(end)
                STKUtilHelper.TestComponent(clr.CastAs(end, IComponentInfo), False)

                self.TestSegment(clr.CastAs(end, IMissionControlSequenceSegment))

                # IComponentInfo
                compCopy: "IComponentInfo" = compInfo
                oldName: str = compCopy.name
                oldUserComment: str = compCopy.user_comment
                compCopy.name = "TestName"
                Assert.assertEqual("TestName", compCopy.name)
                compCopy.user_comment = "UserComment"
                Assert.assertEqual("UserComment", compCopy.user_comment)
                desc: str = compCopy.description
                readOnly: bool = compCopy.is_read_only()
                compCopy.name = oldName
                compCopy.user_comment = oldUserComment

        stop: "MissionControlSequenceStop" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.STOP, "stop1", "-"), MissionControlSequenceStop
        )
        self.TestSegment(clr.CastAs(stop, IMissionControlSequenceSegment))
        GatorHelper.TestRuntimeTypeInfo(stop)

        mcsSegment: "IMissionControlSequenceSegment"

        for mcsSegment in mcsSegColl:
            compInfo: "IComponentInfo" = clr.CastAs(mcsSegment, IComponentInfo)
            Assert.assertIsNotNone(compInfo, "compInfo should not be null")
            TestBase.logger.WriteLine5("Segment name: {0}", compInfo.name)

        stop.enabled = True
        Assert.assertTrue(stop.enabled)
        stop.enabled = False
        Assert.assertFalse(stop.enabled)
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Stop END")

    # endregion

    # region TargetSequence
    def test_TargetSequence(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - TargetSequence START")
        ts: "MissionControlSequenceTargetSequence" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "ts1", "-"),
            MissionControlSequenceTargetSequence,
        )
        GatorHelper.bIsStkX = (self.Target == TestTarget.eStkX) or (self.Target == TestTarget.eStkNoGfx)
        GatorHelper.TestTargetSequence(ts, False, TestBase.Application)
        GatorHelper.TestRuntimeTypeInfo(ts)
        self.TestSegment(clr.CastAs(ts, IMissionControlSequenceSegment))
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - TargetSequence END")

    # endregion

    # region TargetSequence_SequenceDeltaV
    def test_TargetSequence_SequenceDeltaV(self):
        ts: "MissionControlSequenceTargetSequence" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "ts2", "-"),
            MissionControlSequenceTargetSequence,
        )
        seg: "IMissionControlSequenceSegment" = clr.CastAs(ts, IMissionControlSequenceSegment)

        sequenceDeltaV: "StateCalcSequenceDeltaV" = clr.CastAs(
            seg.results.add(r"Segments/Sequence DeltaV"), StateCalcSequenceDeltaV
        )

        def action44():
            sequenceDeltaV.sequence_name = "Bogus"

        TryCatchAssertBlock.ExpectedException("Invalid object specified", action44)
        sequenceDeltaV.sequence_name = "ts2"
        Assert.assertEqual("ts2", sequenceDeltaV.sequence_name)

        sequenceDeltaVSquared: "StateCalcSequenceDeltaVSquared" = clr.CastAs(
            seg.results.add(r"Segments/Sequence DeltaV Squared"), StateCalcSequenceDeltaVSquared
        )

        def action45():
            sequenceDeltaVSquared.sequence_name = "Bogus"

        TryCatchAssertBlock.ExpectedException("Invalid object specified", action45)
        sequenceDeltaVSquared.sequence_name = "ts2"
        Assert.assertEqual("ts2", sequenceDeltaVSquared.sequence_name)

        EarlyBoundTests.AG_VA.main_sequence.remove("ts2")

    # endregion

    # region MoonMission
    def test_MoonMission(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - MoonMission START")
        TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("Test")
        TestBase.Application.unit_preferences.set_current_unit("DistanceUnit", "km")
        #
        scene: "Scenario" = clr.Convert(TestBase.Application.current_scenario, Scenario)
        scene.start_time = "1 Jan 1993 00:00:00.00"
        scene.stop_time = "1 Jan 1994 00:00:00.00"
        if not TestBase.NoGraphicsMode:
            scene.animation.start_time = "1 Jan 1993 00:00:00.00"
            scene.animation.enable_anim_cycle_time = True
            scene.animation.anim_cycle_type = SCENARIO_END_LOOP_TYPE.END_TIME
            scene.animation.anim_cycle_time = "1 Jan 1994 00:00:00.00"
            (clr.Convert(TestBase.Application, StkObjectRoot)).rewind()

        else:

            def action46():
                scene.animation.start_time = "1 Jan 1993 00:00:00.00"

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action46)

        #
        sun: "Planet" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.PLANET, "Sun"), Planet
        )
        sun.position_source = PLANET_POSITION_SOURCE_TYPE.POSITION_CENTRAL_BODY
        pos: "PlanetPositionCentralBody" = clr.Convert(sun.position_source_data, PlanetPositionCentralBody)
        pos.auto_rename = True
        pos.central_body = "Sun"
        #
        moon: "Planet" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.PLANET, "Moon"), Planet
        )
        moon.position_source = PLANET_POSITION_SOURCE_TYPE.POSITION_CENTRAL_BODY
        pos = clr.Convert(moon.position_source_data, PlanetPositionCentralBody)
        pos.central_body = "Moon"
        #
        earth: "Planet" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.PLANET, "Earth"), Planet
        )
        earth.position_source = PLANET_POSITION_SOURCE_TYPE.POSITION_CENTRAL_BODY
        pos = clr.Convert(earth.position_source_data, PlanetPositionCentralBody)
        pos.central_body = "Earth"

        #
        sat: "Satellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "LunarProbe"), Satellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.Convert(sat.propagator, DriverMissionControlSequence)
        driver.options.draw_trajectory_in_2d = True
        driver.options.draw_trajectory_in_3d = True
        driver.options.update_animation_time_for_all_objects = True
        if not TestBase.NoGraphicsMode:
            sat.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)
            sat.graphics.pass_data.ground_track.set_lead_data_type(LEAD_TRAIL_DATA.DATA_NONE)
            sat.graphics.pass_data.orbit.set_lead_data_type(LEAD_TRAIL_DATA.DATA_ALL)
            sat.graphics_3d.pass_method.track_data.inherit_from_2d = True
            sat.graphics_3d.model.orbit_marker.marker_type = MARKER_TYPE.SHAPE
            markerData: "Graphics3DMarkerShape" = clr.Convert(
                sat.graphics_3d.model.orbit_marker.marker_data, Graphics3DMarkerShape
            )
            markerData.style = MARKER_SHAPE_3D.SHAPE_POINT
            sat.graphics_3d.model.orbit_marker.pixel_size = 7
            sat.graphics_3d.model.detail_threshold.marker_label = 1000000000000.0
            sat.graphics_3d.model.detail_threshold.marker = 1000000000000.0
            sat.graphics_3d.model.detail_threshold.point = 1000000000000.0

        else:

            def action47():
                sat.graphics.set_attributes_type(VEHICLE_GRAPHICS_2D_ATTRIBUTES.ATTRIBUTES_BASIC)

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action47)

            def action48():
                sat.graphics_3d.pass_method.track_data.inherit_from_2d = True

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action48)

        #
        driver.main_sequence.remove_all()
        ts: "MissionControlSequenceTargetSequence" = clr.Convert(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target Sequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        launch: "MissionControlSequenceLaunch" = clr.Convert(
            ts.segments.insert(SEGMENT_TYPE.LAUNCH, "Launch", "-"), MissionControlSequenceLaunch
        )
        launch.epoch = "1 Jan 1993 00:00:00.00"
        #
        coast: "MissionControlSequencePropagate" = clr.Convert(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "Coast", "-"), MissionControlSequencePropagate
        )
        (clr.Convert(coast.stopping_conditions[0].properties, StoppingCondition)).trip = 2700
        #
        transLunarInjection: "MissionControlSequenceManeuver" = clr.Convert(
            ts.segments.insert(SEGMENT_TYPE.MANEUVER, "TransLunarInjection", "-"), MissionControlSequenceManeuver
        )
        transLunarInjection.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
        impulsive: "ManeuverImpulsive" = clr.Convert(transLunarInjection.maneuver, ManeuverImpulsive)

        GatorHelper.TestRuntimeTypeInfo(impulsive)

        impulsive.set_attitude_control_type(ATTITUDE_CONTROL.THRUST_VECTOR)
        thrustVector: "AttitudeControlImpulsiveThrustVector" = clr.Convert(
            impulsive.attitude_control, AttitudeControlImpulsiveThrustVector
        )

        # ENG98248, BUG98514
        # We are deprecating the DeltaVVector property of AttitudeControlImpulsiveThrustVector, and
        # replacing it with individual properties X, Y, Z (for Cartesian) and Azimuth, Elevation and Magnitude (for spherical)
        # on the ImpulsiveThrustVector interface; we're also adding Assign/Query Cartesian and Spherical to the same interface.
        # The new properties will work in dimensions of 'SmallDistance'/'Time' as opposed to the 'Distance'/'Time' dimensions
        # of the former properties. The deprecation of DeltaVVector is in addition to its predecessor Position (which was
        # deprecated a long time ago, but never removed). Unfortunately the replacement for Position, DeltaVVector, only
        # corrected a poor naming convention. Other underlying issues associated with using a position vector for a
        # DeltaV vector remained. The changes for the referenced BUG and ENG are to address these lingering issues.

        thrustVector.x = 100.0  # new properties X, Y, Z, Magnitude set in small distance/time
        Assert.assertEqual(100.0, thrustVector.x)
        thrustVector.y = 200.0
        Assert.assertEqual(200.0, thrustVector.y)
        thrustVector.z = 300.0
        Assert.assertEqual(300.0, thrustVector.z)

        newVect = thrustVector.query_cartesian()

        Assert.assertEqual(100.0, newVect[0])  # compare against new QueryCartesian results in smalldistance/time
        Assert.assertEqual(200.0, newVect[1])
        Assert.assertEqual(300.0, newVect[2])

        thrustVector.assign_cartesian(-100.0, 100.0, 100.0)  # test AssignCartesian
        newVect = thrustVector.query_cartesian()

        Assert.assertEqual(-100.0, newVect[0])
        Assert.assertEqual(100.0, newVect[1])
        Assert.assertEqual(100.0, newVect[2])

        # The spherical assign call should be in the order of Az, El, Mag as it appears in the GUI and in common usage, but
        # because the underlying vector is a position vector we were trying to double-dip and the associated convention
        # for the position vector is Lat, Long, Rad where Long more closely relates to Az and Lat more closely relates
        # to Az so these are in an unnatural order. Position vectors also allow for other irrelevant Assign calls like
        # AssignCylindrical, AssignGeodetic, etc.

        # el, az, mag [small distance/time]
        thrustVector.assign_spherical(10.0, 20.0, 1000.0)

        # Assert.AreEqual(10.0, thrustVector.Azimuth);
        # Assert.AreEqual(20.0, thrustVector.Elevation);

        # AssignSpherical also introduces noise in the native storage data (in m/sec) making this comparison less accurate.
        # Assert.AreEqual(1000.0, thrustVector.Magnitude, 1e-12); // dimension: [small distance/time]

        thrustVector.azimuth = 10.0
        thrustVector.elevation = 20.0
        thrustVector.magnitude = 1000.0  # dimension: [small distance/time]

        Assert.assertEqual(10.0, thrustVector.azimuth)
        Assert.assertEqual(20.0, thrustVector.elevation)
        Assert.assertEqual(1000.0, thrustVector.magnitude)  # dimension: [small distance/time]

        # This will work because its bounds are handled appropriately in the local scope.
        thrustVector.allow_negative_spherical_magnitude = True
        thrustVector.magnitude = -1000.0
        thrustVector.magnitude = 1000.0

        # This shouldn't let us set the negative value when false.
        thrustVector.allow_negative_spherical_magnitude = False

        def action49():
            thrustVector.magnitude = -1000.0

        TryCatchAssertBlock.ExpectedException(
            "Value -1000.00000000 m*sec^-1 is invalid. Value minimum is 0 m*sec^-1", action49
        )

        # The radio buttons that control access to the Cartesian/spherical parameters are not enforced through the API, only in the GUI.
        # The attribute flags have been set such that the inactive parameter set is 'hidden' but not 'readonly' - readonly would
        # replicate the GUI behavior. It is possible that the flags were set the way they are to allow the AssignCartesian, AssignSpherical
        # and AllowNegativeSphericalMagnitude behaviors to function. Rather than break backward compatibility the attribute flags are
        # not being changed at this time - they should be changed for the next major release. The following simply tests the ability to
        # change from Cartesian to spherical and back even though doing so still has no consequences for the API.

        currentChoice: "IMP_DELTA_V_REP" = thrustVector.coord_type

        thrustVector.coord_type = IMP_DELTA_V_REP.CARTESIAN_IMP_DELTA_V
        Assert.assertEqual(IMP_DELTA_V_REP.CARTESIAN_IMP_DELTA_V, thrustVector.coord_type)
        thrustVector.coord_type = IMP_DELTA_V_REP.SPHERICAL_IMP_DELTA_V
        Assert.assertEqual(IMP_DELTA_V_REP.SPHERICAL_IMP_DELTA_V, thrustVector.coord_type)
        thrustVector.coord_type = currentChoice

        sphVect = thrustVector.query_spherical()
        thrustVector.assign_spherical(100.0, 80.0, 500.0)
        sphVect = thrustVector.query_spherical()

        Assert.assertEqual(100.0, sphVect[0])
        Assert.assertEqual(80.0, sphVect[1])
        Assert.assertEqual(500.0, sphVect[2])  # dimension: [small distance/time]

        Assert.assertEqual(100.0, thrustVector.azimuth)
        Assert.assertEqual(80.0, thrustVector.elevation)
        Assert.assertEqual(500.0, thrustVector.magnitude)  # dimension: [small distance/time]

        # This shouldn't let us set the negative value when false.
        thrustVector.allow_negative_spherical_magnitude = False

        def action50():
            thrustVector.assign_spherical(100.0, 80.0, -500.0)

        TryCatchAssertBlock.ExpectedException(
            "Value -500.00000000 m*sec^-1 is invalid. Value minimum is 0 m*sec^-1", action50
        )
        thrustVector.allow_negative_spherical_magnitude = True
        thrustVector.assign_spherical(100.0, 80.0, -500.0)

        def action51():
            thrustVector.assign_spherical(100.0, 100.0, -500.0)

        TryCatchAssertBlock.DoAssert(action51)

        # end ENG98248, BUG98514

        GatorHelper.TestRuntimeTypeInfo(thrustVector)

        #
        toSwingBy: "MissionControlSequencePropagate" = clr.Convert(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "ToSwingBy", "-"), MissionControlSequencePropagate
        )
        toSwingBy.propagator_name = "CisLunar"
        (clr.Convert(toSwingBy.stopping_conditions.add("R Magnitude").properties, StoppingCondition)).trip = 300000
        toSwingBy.stopping_conditions.remove("Duration")
        #
        toPersilene: "MissionControlSequencePropagate" = clr.Convert(
            ts.segments.insert(SEGMENT_TYPE.PROPAGATE, "ToPersilene", "-"), MissionControlSequencePropagate
        )
        toPersilene.propagator_name = "CisLunar"
        (clr.Convert(toPersilene.stopping_conditions[0].properties, StoppingCondition)).trip = 864000
        alt: "StoppingCondition" = clr.Convert(
            toPersilene.stopping_conditions.add("Altitude").properties, StoppingCondition
        )
        alt.trip = 0
        alt.central_body_name = "Moon"
        #
        periapsis: "StoppingCondition" = clr.Convert(
            toPersilene.stopping_conditions.add("Periapsis").properties, StoppingCondition
        )
        periapsis.central_body_name = "Moon"
        #
        #
        thrustVector.assign_cartesian(3150.0, 0.0, 0.0)

        thrustVector.body_constraint_vector.assign_xyz(1.0, 2.0, 3.0)
        driver.run_mission_control_sequence()
        #
        launch.enable_control_parameter(CONTROL_LAUNCH.EPOCH)
        coast.stopping_conditions[0].enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        #
        calcObject: "IComponentInfo" = (clr.Convert(toPersilene, IMissionControlSequenceSegment)).results.add(
            "MultiBody/Delta Right Asc"
        )
        (clr.Convert(toPersilene, IMissionControlSequenceSegment)).results.add("MultiBody/Delta Declination")
        self.TestCalcObjectCollection((clr.Convert(toPersilene, IMissionControlSequenceSegment)).results)
        #
        #
        diffCorrector: "ProfileDifferentialCorrector" = clr.Convert(ts.profiles[0], ProfileDifferentialCorrector)
        diffCorrector.name = "Delta RA and Dec"
        diffCorrector.control_parameters.get_control_by_paths("Launch", "Launch.Epoch").perturbation = 60
        diffCorrector.control_parameters.get_control_by_paths("Launch", "Launch.Epoch").max_step = 3600
        diffCorrector.control_parameters.get_control_by_paths("Launch", "Launch.Epoch").enable = True
        diffCorrector.control_parameters.get_control_by_paths(
            "Coast", "StoppingConditions.Duration.TripValue"
        ).perturbation = 60
        diffCorrector.control_parameters.get_control_by_paths(
            "Coast", "StoppingConditions.Duration.TripValue"
        ).max_step = 300
        diffCorrector.control_parameters.get_control_by_paths(
            "Coast", "StoppingConditions.Duration.TripValue"
        ).enable = True
        #
        diffCorrector.results[0].desired_value = 0
        diffCorrector.results[0].enable = True
        #
        diffCorrector.results[1].desired_value = 0
        diffCorrector.results[1].enable = True
        #
        ts.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES_ONCE
        driver.run_mission_control_sequence()
        ts.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        driver.run_mission_control_sequence()
        #
        ts.apply_profiles()
        ts.action = TARGET_SEQ_ACTION.RUN_NOMINAL_SEQ
        driver.run_mission_control_sequence()
        #
        dcCopy: "ProfileDifferentialCorrector" = clr.Convert(ts.profiles[0].copy(), ProfileDifferentialCorrector)
        dcCopy.name = "B_Plane_Targeting"
        ts.profiles[0].mode = PROFILE_MODE.NOT_ACTIVE
        #
        (clr.Convert(toPersilene, IMissionControlSequenceSegment)).results.add("Epoch")
        (clr.Convert(toPersilene, IMissionControlSequenceSegment)).results.add("MultiBody/BDotT")
        (clr.Convert(toPersilene, IMissionControlSequenceSegment)).results.add("MultiBody/BDotR")
        #

        transLunarInjection.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
        #

        # "ImpulsiveMnvr.Cartesian.X" attribute path deprecated, but backward compatibility translation code allows
        dcCopy.control_parameters.get_control_by_paths("TransLunarInjection", "ImpulsiveMnvr.Cartesian.X").enable = True
        Assert.assertEqual(
            True,
            dcCopy.control_parameters.get_control_by_paths("TransLunarInjection", "ImpulsiveMnvr.Cartesian.X").enable,
        )
        dcCopy.control_parameters.get_control_by_paths(
            "TransLunarInjection", "ImpulsiveMnvr.Cartesian.X"
        ).enable = False
        Assert.assertEqual(
            False,
            dcCopy.control_parameters.get_control_by_paths("TransLunarInjection", "ImpulsiveMnvr.Cartesian.X").enable,
        )

        # "ImpulsiveMnvr.Pointing.Cartesian.X" is the new attribute path
        dcCopy.control_parameters.get_control_by_paths(
            "TransLunarInjection", "ImpulsiveMnvr.Pointing.Cartesian.X"
        ).enable = True
        Assert.assertEqual(
            True,
            dcCopy.control_parameters.get_control_by_paths(
                "TransLunarInjection", "ImpulsiveMnvr.Pointing.Cartesian.X"
            ).enable,
        )

        #
        dcCopy.results.get_result_by_paths("ToPersilene", "Delta Declination").enable = False
        dcCopy.results.get_result_by_paths("ToPersilene", "Delta Right Asc").enable = False
        #
        dcCopy.results.get_result_by_paths("ToPersilene", "BDotR").enable = True
        dcCopy.results.get_result_by_paths("ToPersilene", "BDotT").enable = True
        dcCopy.results.get_result_by_paths("ToPersilene", "Epoch").enable = True
        dcCopy.results.get_result_by_paths("ToPersilene", "BDotR").desired_value = 5000
        dcCopy.results.get_result_by_paths("ToPersilene", "BDotT").desired_value = 0
        dcCopy.results.get_result_by_paths("ToPersilene", "Epoch").desired_value = "4 Jan 1993 00:00:00.00"
        if not TestBase.NoGraphicsMode:
            template: "VehicleGraphics3DBPlaneTemplate" = clr.Convert(
                sat.graphics_3d.b_planes.templates.add(), VehicleGraphics3DBPlaneTemplate
            )
            template.name = "Lunar_B-Plane"
            template.central_body = "Moon"
            template.reference_vector = "CentralBody/Moon Orbit_Normal Vector"
            bPlane: "VehicleGraphics3DBPlaneInstance" = clr.Convert(
                sat.graphics_3d.b_planes.instances.add("Lunar_B-Plane"), VehicleGraphics3DBPlaneInstance
            )
            bPlane.name = "LunarBPlane"
            (clr.Convert(toPersilene, IMissionControlSequenceSegment)).properties.b_planes.add("LunarBPlane")

        else:

            def action52():
                template: "VehicleGraphics3DBPlaneTemplate" = clr.Convert(
                    sat.graphics_3d.b_planes.templates.add(), VehicleGraphics3DBPlaneTemplate
                )

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action52)

        # Test BPlane collection iteration
        bplaneColl: "BPlaneCollection" = (clr.Convert(toPersilene, IMissionControlSequenceSegment)).properties.b_planes
        bplane: str
        for bplane in bplaneColl:
            TestBase.logger.WriteLine(bplane)

        i: int = 0
        while i < bplaneColl.count:
            bplane: str = bplaneColl[i]

            i += 1

        (clr.Convert(toPersilene, IMissionControlSequenceSegment)).properties.apply_final_state_to_b_planes()
        #
        ts.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES_ONCE
        driver.run_mission_control_sequence()
        #
        ts.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        driver.run_mission_control_sequence()
        # //
        ts.apply_profiles()
        ts.action = TARGET_SEQ_ACTION.RUN_NOMINAL_SEQ
        driver.run_mission_control_sequence()
        #
        #
        TestBase.Application.execute_command(
            'VectorTool * Moon Create Axes True_Moon_Equator "Aligned and Constrained" Cartesian 0 0 1 "CentralBody/Moon Angular_Velocity"  Cartesian 1 0 0 "CentralBody/Moon VernalEquinox"'
        )
        TestBase.Application.execute_command(
            'VectorTool * Moon Create System True_Lunar_Equatorial "Assembled" "CentralBody/Moon Center" "CentralBody/Moon True_Moon_Equator"'
        )
        #
        #
        altInc: "ProfileDifferentialCorrector" = clr.Convert(dcCopy.copy(), ProfileDifferentialCorrector)
        altInc.name = "Altitude and Inclination"
        #
        ts.profiles[0].mode = PROFILE_MODE.NOT_ACTIVE
        (clr.Convert(dcCopy, IProfile)).mode = PROFILE_MODE.NOT_ACTIVE
        #
        #
        calcAlt: "StateCalcGeodeticElem" = clr.Convert(
            (clr.Convert(toPersilene, IMissionControlSequenceSegment)).results.add("Geodetic/Altitude"),
            StateCalcGeodeticElem,
        )
        calcAlt.central_body_name = "Moon"
        calcInc: "StateCalcInclination" = clr.Convert(
            (clr.Convert(toPersilene, IMissionControlSequenceSegment)).results.add("Keplerian Elems/Inclination"),
            StateCalcInclination,
        )
        calcInc.coord_system_name = "CentralBody/Moon True_Lunar_Equatorial"

        count: int = 0
        while count < altInc.results.count:
            altInc.results[count].enable = False

            count += 1

        altInc.results.get_result_by_paths("ToPersilene", "Altitude").enable = True
        altInc.results.get_result_by_paths("ToPersilene", "Epoch").enable = True
        altInc.results.get_result_by_paths("ToPersilene", "Inclination").enable = True
        #
        altInc.results.get_result_by_paths("ToPersilene", "Altitude").desired_value = 100
        altInc.results.get_result_by_paths("ToPersilene", "Inclination").desired_value = 90
        altInc.results.get_result_by_paths("ToPersilene", "Epoch").desired_value = "4 Jan 1993 00:00:00.00"
        #
        ts.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        driver.run_mission_control_sequence()
        ts.apply_profiles()
        ts.action = TARGET_SEQ_ACTION.RUN_NOMINAL_SEQ
        driver.run_mission_control_sequence()
        #
        prop3Day: "MissionControlSequencePropagate" = clr.Convert(
            driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop3Days", "-"), MissionControlSequencePropagate
        )
        prop3Day.propagator_name = "CisLunar"
        (clr.Convert(prop3Day.stopping_conditions[0].properties, StoppingCondition)).trip = 259200
        #
        driver.run_mission_control_sequence()
        #
        ts2: "MissionControlSequenceTargetSequence" = clr.Convert(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target Sequence2", "Prop3Days"),
            MissionControlSequenceTargetSequence,
        )
        loi: "MissionControlSequenceManeuver" = clr.Convert(
            ts2.segments.insert(SEGMENT_TYPE.MANEUVER, "LOI", "-"), MissionControlSequenceManeuver
        )
        loi.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
        impulsive = clr.Convert(loi.maneuver, ManeuverImpulsive)
        impulsive.set_attitude_control_type(ATTITUDE_CONTROL.THRUST_VECTOR)
        thrust: "AttitudeControlImpulsiveThrustVector" = clr.Convert(
            impulsive.attitude_control, AttitudeControlImpulsiveThrustVector
        )
        thrust.thrust_axes_name = "Satellite VNC(Moon)"
        loi.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
        ecc: "StateCalcEccentricity" = clr.Convert(
            (clr.Convert(loi, IMissionControlSequenceSegment)).results.add("Keplerian Elems/Eccentricity"),
            StateCalcEccentricity,
        )
        ecc.central_body_name = "Moon"
        #
        diffCorrector = clr.Convert(ts2.profiles[0], ProfileDifferentialCorrector)
        diffCorrector.control_parameters[0].enable = True
        diffCorrector.results[0].enable = True
        #
        ts2.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        driver.run_mission_control_sequence()
        ts2.apply_profiles()
        ts2.action = TARGET_SEQ_ACTION.RUN_NOMINAL_SEQ
        driver.run_mission_control_sequence()
        if not TestBase.NoGraphicsMode:
            (clr.Convert(TestBase.Application, StkObjectRoot)).rewind()

        else:

            def action53():
                (clr.Convert(TestBase.Application, StkObjectRoot)).rewind()

            TryCatchAssertBlock.ExpectedException("NoGraphics property is set to true", action53)

        TestBase.LoadTestScenario(Path.Combine("AstrogatorTests", "AstrogatorTests.sc"))
        EarlyBoundTests.AG_SAT = clr.Convert(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        EarlyBoundTests.AG_VA = clr.Convert(EarlyBoundTests.AG_SAT.propagator, DriverMissionControlSequence)
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - MoonMission END")

    # endregion

    # region ScriptingToolSetControl
    def test_ScriptingToolSetControl(self):
        # Put the target sequence in a sequence
        s43701: "IMissionControlSequenceSequence" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.SEQUENCE, "s43701", "-"),
            IMissionControlSequenceSequence,
        )
        ts43701: "MissionControlSequenceTargetSequence" = clr.Convert(
            s43701.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "ts43701", "-"), MissionControlSequenceTargetSequence
        )

        # Put a propagate segment in a target sequence
        ps43701: "MissionControlSequencePropagate" = clr.Convert(
            ts43701.segments.insert(SEGMENT_TYPE.PROPAGATE, "ps43701", "-"), MissionControlSequencePropagate
        )

        # Make sure Trip Stopping Condition is enabled so can target in the DC
        Assert.assertEqual(1, ps43701.stopping_conditions.count)

        stopcond0: "StoppingConditionElement" = ps43701.stopping_conditions[0]
        stopcond0.active = False
        Assert.assertFalse(stopcond0.active)
        stopcond0.active = True
        Assert.assertTrue(stopcond0.active)

        scc: "IStoppingConditionComponent" = stopcond0.properties
        Assert.assertTrue(stopcond0.control_parameters_available)
        stopcond0.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        Assert.assertTrue(stopcond0.is_control_parameter_enabled(CONTROL_STOPPING_CONDITION.TRIP_VALUE))
        stopcond0.disable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        Assert.assertFalse(stopcond0.is_control_parameter_enabled(CONTROL_STOPPING_CONDITION.TRIP_VALUE))
        stopcond0.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        Assert.assertTrue(stopcond0.is_control_parameter_enabled(CONTROL_STOPPING_CONDITION.TRIP_VALUE))

        # target it's trip value in a DC
        dc: "ProfileDifferentialCorrector" = None
        dc = clr.CastAs(ts43701.profiles["Differential Corrector"], ProfileDifferentialCorrector)
        tripcontrol: "DifferentialCorrectorControl" = clr.CastAs(
            dc.control_parameters.get_control_by_paths("ps43701", "StoppingConditions.Duration.TripValue"),
            DifferentialCorrectorControl,
        )
        Assert.assertFalse(tripcontrol.enable)
        tripcontrol.enable = True
        Assert.assertTrue(tripcontrol.enable)

        # go to the sequence's scripting tool.
        scripttool: "ScriptingTool" = s43701.scripting_tool
        Assert.assertFalse(scripttool.enable)
        scripttool.enable = True
        Assert.assertTrue(scripttool.enable)

        GatorHelper.TestRuntimeTypeInfo(scripttool)

        # Create an attribute that is set to the targeter's
        # Profiles.DC.Controls.StoppingConditions.Duration.TripValue.MaxStep
        scriptseg: "ScriptingSegment" = scripttool.segment_properties.add("TargeterMaxStep")

        GatorHelper.TestRuntimeTypeInfo(scriptseg)

        objName: str = "Segments.ts43701"
        foundSegName: bool = False

        availObjs = scriptseg.available_object_names
        Assert.assertIsNotNone(availObjs)

        TestBase.logger.WriteLine("=================Available Segment Names ===========")
        TestBase.logger.WriteLine(("Count: " + str(Array.Length(availObjs))))

        i: int = 1
        choice: str
        for choice in availObjs:
            TestBase.logger.WriteLine(((str(i) + ". ") + choice))
            i += 1
            if objName == choice:
                foundSegName = True

        Assert.assertTrue(foundSegName)

        scriptseg.object_name = objName

        controlattr: str = (
            "Profiles.Differential_Corrector.Controls.ps43701_:_StoppingConditions_Duration_TripValue.MaxStep"
        )
        foundAttr: bool = False

        availattr = scriptseg.available_attribute_values
        Assert.assertIsNotNone(availattr)

        TestBase.logger.WriteLine("===============Available Attribute Values============")
        TestBase.logger.WriteLine(("Count: " + str(Array.Length(availattr))))

        j: int = 1
        choice: str
        for choice in availattr:
            TestBase.logger.WriteLine(((str(j) + ". ") + choice))
            j += 1
            if controlattr == choice:
                foundAttr = True

        Assert.assertTrue(foundAttr)

        scriptseg.attribute = controlattr
        EarlyBoundTests.AG_VA.run_mission_control_sequence()

        EarlyBoundTests.AG_VA.clear_dwc_graphics()

    # endregion

    # region GetChangeReturnSegment
    def test_GetChangeReturnSegment(self):
        EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None
        targSeq = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        ret: "MissionControlSequenceReturn" = None
        ret = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), MissionControlSequenceReturn)

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeq.profiles.add("Change Return Segment"), ProfileChangeReturnSegment)
        changeReturn.segment_name = "Return"
        changeReturn.name = "MyReturn"
        crs: "ProfileChangeReturnSegment" = clr.CastAs(targSeq.profiles["MyReturn"], ProfileChangeReturnSegment)
        Assert.assertIsNotNone(crs)

        # Need to remove something, can't just remove the "RemoveAll"
        # Thus remove the added stuff in this test, or else it
        # "corrupts" the Hold or whichever test is post/next this test
        # ( ie GetChangeReturnSegment ) in the NUNIT layout.  BUG47649.
        # This caused by  CL254087 that was trying to fix CL253323 from BUG46465.
        targSeq.profiles.remove("MyReturn")
        targSeq.segments.remove("Return")
        EarlyBoundTests.AG_VA.main_sequence.remove("TargetSequence")
        EarlyBoundTests.AG_VA.main_sequence.remove("InitialState")

    # endregion

    # region TestSegment
    def TestSegment(self, seg: "IMissionControlSequenceSegment"):
        # the follow segment needs the leader to be set with a long enough ephemeris
        EarlyBoundTests.AG_VA.begin_run()
        if clr.Is(seg, MissionControlSequenceFollow):

            def action54():
                orbitState: "State" = seg.run()

            TryCatchAssertBlock.DoAssert(action54)

        elif clr.Is(seg, MissionControlSequenceTargetSequence):
            pass

        else:
            orbitState: "State" = seg.run()

        EarlyBoundTests.AG_VA.end_run()

        type: "SEGMENT_TYPE" = seg.type
        segProperties: "MissionControlSequenceSegmentProperties" = seg.properties
        execSummary: "DataProviderResult" = seg.exec_summary
        finalState: "State" = seg.final_state
        initialState: "State" = seg.initial_state
        properties: "MissionControlSequenceSegmentProperties" = seg.properties
        calcObjectCollection: "CalcObjectCollection" = seg.results
        typeX: "SEGMENT_TYPE" = seg.type
        resultValue: typing.Any = seg.get_result_value("Epoch")

    # endregion

    # region TestCalcObjectCollection
    def TestCalcObjectCollection(self, calcObjColl: "CalcObjectCollection"):
        origCount: int = calcObjColl.count

        calcObjColl.add("MultiBody/BTheta")
        Assert.assertEqual((origCount + 1), calcObjColl.count)
        calcObjColl.add("MultiBody/Delta Declination")
        Assert.assertEqual((origCount + 2), calcObjColl.count)

        compInfo: "IComponentInfo"

        for compInfo in calcObjColl:
            name: str = compInfo.name
            compInfoA: "IComponentInfo" = calcObjColl.get_item_by_name(
                name.replace(" ", "_")
            )  # When fetching name, we replace underscores with spaces.
            Assert.assertEqual(
                compInfo.name, compInfoA.name, "propget and GetItemByName should return same IComponentInfo"
            )

        i: int = 0
        while i < calcObjColl.count:
            compInfo: "IComponentInfo" = calcObjColl[i]
            compInfoA: "IComponentInfo" = calcObjColl.get_item_by_index(i)
            Assert.assertEqual(
                compInfo.name, compInfoA.name, "propget and GetItemByIndex should return same IComponentInfo"
            )

            i += 1

        def action55():
            compInfo: "IComponentInfo" = calcObjColl[calcObjColl.count]

        TryCatchAssertBlock.DoAssert(action55)

        def action56():
            compInfoA: "IComponentInfo" = calcObjColl.get_item_by_index(calcObjColl.count)

        TryCatchAssertBlock.ExpectedException("Index Out of Range", action56)

        def action57():
            compInfoA: "IComponentInfo" = calcObjColl.get_item_by_name("bogus")

        TryCatchAssertBlock.ExpectedException("Item specified by ItemOrName could not be found", action57)

        compInfo2: "IComponentInfo" = calcObjColl["BTheta"]
        Assert.assertIsNotNone(compInfo2)

        def action58():
            compInfo3: "IComponentInfo" = calcObjColl["Item3"]

        TryCatchAssertBlock.DoAssert(action58)

        calcObjColl.remove((calcObjColl.count - 1))
        Assert.assertEqual((origCount + 1), calcObjColl.count)

        def action59():
            calcObjColl.remove(calcObjColl.count)

        TryCatchAssertBlock.DoAssert(action59)

        calcObjColl.remove("BTheta")
        Assert.assertEqual(origCount, calcObjColl.count)

        def action60():
            calcObjColl.remove("Item3")

        TryCatchAssertBlock.DoAssert(action60)

    # endregion

    # region TestDCProfileResetAndApply
    def test_TestDCProfileResetAndApply(self):
        ms: "MissionControlSequenceSegmentCollection" = EarlyBoundTests.AG_VA.main_sequence

        ms.remove_all()
        ms.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeg: "IMissionControlSequenceSegment" = None
        targSeg = ms.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(targSeg, MissionControlSequenceTargetSequence)
        targSeq.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES

        propSeg: "IMissionControlSequenceSegment" = None
        propSeg = targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        prop: "MissionControlSequencePropagate" = clr.CastAs(propSeg, MissionControlSequencePropagate)

        durStop: "StoppingConditionElement" = prop.stopping_conditions["Duration"]
        durStop.active = True
        durStop.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        stop: "StoppingCondition" = clr.CastAs(durStop.properties, StoppingCondition)
        stop.trip = 3600

        durationResult: "IComponentInfo" = propSeg.results.add("Time/Duration")

        prof: "IProfile" = targSeq.profiles["Differential Corrector"]
        dc: "ProfileDifferentialCorrector" = clr.CastAs(prof, ProfileDifferentialCorrector)

        dcc: "DifferentialCorrectorControl" = None
        dcc = dc.control_parameters.get_control_by_paths("Propagate", "StoppingConditions.Duration.TripValue")
        dcc.enable = True
        dcc.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.INITIAL_VALUE
        dcc.perturbation = 60
        dcc.max_step = 3600
        Assert.assertEqual(0, dcc.last_update)
        Assert.assertEqual(3600, dcc.initial_value)
        Assert.assertEqual(3600, dcc.final_value)
        Assert.assertEqual(0, dcc.correction)

        dcr: "DifferentialCorrectorResult" = None
        dcr = dc.results.get_result_by_paths("Propagate", "Duration")
        dcr.enable = True
        dcr.desired_value = 7200
        Assert.assertEqual("-Not Set-", dcr.current_value)
        Assert.assertEqual(7200, dcr.desired_value)

        EarlyBoundTests.AG_VA.run_mission_control_sequence()

        Assert.assertEqual(7200, dcc.final_value)
        Assert.assertEqual(3600, dcc.last_update)
        Assert.assertEqual(3600, dcc.initial_value)
        Assert.assertEqual(3600, dcc.correction)
        Assert.assertEqual(3600, dcc.max_step)

        Assert.assertEqual(7200, dcr.desired_value)
        Assert.assertEqual(7200, dcr.current_value)

        targSeq.reset_profile(prof)

        targSeq.reset_profile_by_name(prof.name)

        Assert.assertEqual(3600, dcc.final_value)
        Assert.assertEqual(0, dcc.last_update)
        Assert.assertEqual(3600, dcc.initial_value)
        Assert.assertEqual(0, dcc.correction)
        Assert.assertEqual(3600, dcc.max_step)

        Assert.assertEqual(7200, dcr.desired_value)
        Assert.assertEqual(7200, dcr.current_value)

        EarlyBoundTests.AG_VA.run_mission_control_sequence()

        Assert.assertEqual(7200, dcc.final_value)
        Assert.assertEqual(3600, dcc.last_update)
        Assert.assertEqual(3600, dcc.initial_value)
        Assert.assertEqual(3600, dcc.correction)
        Assert.assertEqual(3600, dcc.max_step)

        Assert.assertEqual(7200, dcr.desired_value)
        Assert.assertEqual(7200, dcr.current_value)

        targSeq.apply_profile(prof)

        targSeq.apply_profile_by_name(prof.name)

        # Have to get the dcr again? is this because after apply a new copy of
        # attrs is made and thus our old attrs in memeory are invalid? is this good/bad?
        dcc = dc.control_parameters.get_control_by_paths("Propagate", "StoppingConditions.Duration.TripValue")
        Assert.assertEqual(7200, dcc.final_value)
        Assert.assertEqual(0, dcc.last_update)
        Assert.assertEqual(7200, dcc.initial_value)
        Assert.assertEqual(0, dcc.correction)
        Assert.assertEqual(3600, dcc.max_step)

        # Have to get the dcr again? is this because after apply a new copy of
        # attrs is made and thus our old attrs in memeory are invalid? is this good/bad?
        dcr = dc.results.get_result_by_paths("Propagate", "Duration")
        Assert.assertEqual(7200, dcr.desired_value)
        Assert.assertEqual(7200, dcr.current_value)

        targSeq.profiles.add("Change Maneuver Type")
        targSeq.profiles.add("Change Propagator")
        targSeq.profiles.add("Change Return Segment")
        targSeq.profiles.add("Change Stop Segment")
        targSeq.profiles.add("Change Stopping Condition State")
        targSeq.profiles.add("Run Target Sequence Once")
        targSeq.profiles.add("Scripting Tool")
        targSeq.profiles.add("Seed Finite Maneuver")
        myProf: "IProfile"
        for myProf in targSeq.profiles:
            targSeq.reset_profile(myProf)
            targSeq.reset_profile_by_name(myProf.name)
            EarlyBoundTests.AG_VA.run_mission_control_sequence()
            targSeq.apply_profile(myProf)
            targSeq.apply_profile_by_name(myProf.name)
            EarlyBoundTests.AG_VA.run_mission_control_sequence()

        TestBase.LoadTestScenario(Path.Combine("AstrogatorTests", "AstrogatorTests.sc"))
        EarlyBoundTests.AG_SAT = clr.Convert(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        EarlyBoundTests.AG_VA = clr.Convert(EarlyBoundTests.AG_SAT.propagator, DriverMissionControlSequence)

    # endregion

    # region ApplyAndResetAllProfiles
    def test_ApplyAndResetAllProfiles(self):
        ms: "MissionControlSequenceSegmentCollection" = EarlyBoundTests.AG_VA.main_sequence

        ms.remove_all()
        ms.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        # region First Target Sequence

        targSeg: "IMissionControlSequenceSegment" = None
        targSeg = ms.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(targSeg, MissionControlSequenceTargetSequence)
        targSeq.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES

        propSeg: "IMissionControlSequenceSegment" = None
        propSeg = targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        prop: "MissionControlSequencePropagate" = clr.CastAs(propSeg, MissionControlSequencePropagate)

        durStop: "StoppingConditionElement" = prop.stopping_conditions["Duration"]
        durStop.active = True
        durStop.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        stop: "StoppingCondition" = clr.CastAs(durStop.properties, StoppingCondition)
        stop.trip = 3600

        durationResult: "IComponentInfo" = propSeg.results.add("Time/Duration")

        # endregion

        # region Second Target Sequence

        targSeg2: "IMissionControlSequenceSegment" = None
        targSeg2 = ms.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence1", "-")
        targSeq2: "MissionControlSequenceTargetSequence" = clr.CastAs(targSeg2, MissionControlSequenceTargetSequence)
        targSeq2.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES

        propSeg2: "IMissionControlSequenceSegment" = None
        propSeg2 = targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        prop2: "MissionControlSequencePropagate" = clr.CastAs(propSeg2, MissionControlSequencePropagate)

        durStop2: "StoppingConditionElement" = prop2.stopping_conditions["Duration"]
        durStop2.active = True
        durStop2.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        stop2: "StoppingCondition" = clr.CastAs(durStop2.properties, StoppingCondition)
        stop2.trip = 3600

        durationResult2: "IComponentInfo" = propSeg2.results.add("Time/Duration")

        # endregion

        # region First DC Profile

        prof: "IProfile" = targSeq.profiles["Differential Corrector"]
        dc: "ProfileDifferentialCorrector" = clr.CastAs(prof, ProfileDifferentialCorrector)

        dcc: "DifferentialCorrectorControl" = None
        dcc = dc.control_parameters.get_control_by_paths("Propagate", "StoppingConditions.Duration.TripValue")
        dcc.enable = True
        dcc.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.INITIAL_VALUE
        dcc.perturbation = 60
        dcc.max_step = 3600
        Assert.assertAlmostEqual(0, float(dcc.last_update), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.final_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc.correction), delta=1e-09)

        dcr: "DifferentialCorrectorResult" = None
        dcr = dc.results.get_result_by_paths("Propagate", "Duration")
        dcr.enable = True
        dcr.desired_value = 7200
        Assert.assertEqual("-Not Set-", dcr.current_value)
        Assert.assertAlmostEqual(7200, float(dcr.desired_value), delta=1e-09)

        # endregion

        # region Second DC Profile

        prof2: "IProfile" = targSeq2.profiles["Differential Corrector"]
        dc2: "ProfileDifferentialCorrector" = clr.CastAs(prof2, ProfileDifferentialCorrector)

        dcc2: "DifferentialCorrectorControl" = None
        dcc2 = dc2.control_parameters.get_control_by_paths("Propagate", "StoppingConditions.Duration.TripValue")
        dcc2.enable = True
        dcc2.scaling_method = DIFFERENTIAL_CORRECTOR_SCALING_METHOD.INITIAL_VALUE
        dcc2.perturbation = 60
        dcc2.max_step = 3600
        Assert.assertAlmostEqual(0, float(dcc2.last_update), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.final_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc2.correction), delta=1e-09)

        dcr2: "DifferentialCorrectorResult" = None
        dcr2 = dc2.results.get_result_by_paths("Propagate", "Duration")
        dcr2.enable = True
        dcr2.desired_value = 7200
        Assert.assertEqual("-Not Set-", dcr2.current_value)
        Assert.assertAlmostEqual(7200, float(dcr2.desired_value), delta=1e-09)

        # endregion

        EarlyBoundTests.AG_VA.run_mission_control_sequence()

        Assert.assertAlmostEqual(7200, float(dcc.final_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.last_update), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.correction), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.max_step), delta=1e-09)

        Assert.assertAlmostEqual(7200, float(dcr.desired_value), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcr.current_value), delta=1e-09)

        Assert.assertAlmostEqual(7200, float(dcc2.final_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.last_update), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.correction), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.max_step), delta=1e-09)

        Assert.assertAlmostEqual(7200, float(dcr2.desired_value), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcr2.current_value), delta=1e-09)

        EarlyBoundTests.AG_VA.reset_all_profiles()

        Assert.assertAlmostEqual(3600, float(dcc.final_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc.last_update), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc.correction), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.max_step), delta=1e-09)

        Assert.assertAlmostEqual(7200, float(dcr.desired_value), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcr.current_value), delta=1e-09)

        Assert.assertAlmostEqual(3600, float(dcc2.final_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc2.last_update), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc2.correction), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.max_step), delta=1e-09)

        Assert.assertAlmostEqual(7200, float(dcr2.desired_value), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcr2.current_value), delta=1e-09)

        EarlyBoundTests.AG_VA.run_mission_control_sequence()

        Assert.assertAlmostEqual(7200, float(dcc.final_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.last_update), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.correction), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.max_step), delta=1e-09)

        Assert.assertAlmostEqual(7200, float(dcr.desired_value), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcr.current_value), delta=1e-09)

        Assert.assertAlmostEqual(7200, float(dcc2.final_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.last_update), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.correction), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.max_step), delta=1e-09)

        Assert.assertAlmostEqual(7200, float(dcr2.desired_value), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcr2.current_value), delta=1e-09)

        EarlyBoundTests.AG_VA.apply_all_profile_changes()

        # Have to get the dcr again? is this because after apply a new copy of
        # attrs is made and thus our old attrs in memeory are invalid? is this good/bad?
        dcc = dc.control_parameters.get_control_by_paths("Propagate", "StoppingConditions.Duration.TripValue")
        Assert.assertAlmostEqual(7200, float(dcc.final_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc.last_update), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcc.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc.correction), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc.max_step), delta=1e-09)

        dcc2 = dc2.control_parameters.get_control_by_paths("Propagate", "StoppingConditions.Duration.TripValue")
        Assert.assertAlmostEqual(7200, float(dcc2.final_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc2.last_update), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcc2.initial_value), delta=1e-09)
        Assert.assertAlmostEqual(0, float(dcc2.correction), delta=1e-09)
        Assert.assertAlmostEqual(3600, float(dcc2.max_step), delta=1e-09)

        # Have to get the dcr again? is this because after apply a new copy of
        # attrs is made and thus our old attrs in memeory are invalid? is this good/bad?
        dcr = dc.results.get_result_by_paths("Propagate", "Duration")
        Assert.assertAlmostEqual(7200, float(dcr.desired_value), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcr.current_value), delta=1e-09)

        dcr2 = dc2.results.get_result_by_paths("Propagate", "Duration")
        Assert.assertAlmostEqual(7200, float(dcr2.desired_value), delta=1e-09)
        Assert.assertAlmostEqual(7200, float(dcr2.current_value), delta=1e-09)

        targSeq.profiles.add("Change Maneuver Type")
        targSeq.profiles.add("Change Propagator")
        targSeq.profiles.add("Change Return Segment")
        targSeq.profiles.add("Change Stop Segment")
        targSeq.profiles.add("Change Stopping Condition State")
        targSeq.profiles.add("Run Target Sequence Once")
        targSeq.profiles.add("Scripting Tool")
        targSeq.profiles.add("Seed Finite Maneuver")
        EarlyBoundTests.AG_VA.reset_all_profiles()
        EarlyBoundTests.AG_VA.run_mission_control_sequence()
        EarlyBoundTests.AG_VA.apply_all_profile_changes()
        EarlyBoundTests.AG_VA.run_mission_control_sequence()

        TestBase.LoadTestScenario(Path.Combine("AstrogatorTests", "AstrogatorTests.sc"))
        EarlyBoundTests.AG_SAT = clr.Convert(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        EarlyBoundTests.AG_VA = clr.Convert(EarlyBoundTests.AG_SAT.propagator, DriverMissionControlSequence)

    # endregion

    # region ScriptingToolFunctionality
    def test_ScriptingToolFunctionality(self):
        EarlyBoundTests.AG_VA.main_sequence.remove_all()
        EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "Initial State", "-")

        sequence: "IMissionControlSequenceSequence" = clr.CastAs(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"),
            IMissionControlSequenceSequence,
        )

        propagate: "MissionControlSequencePropagate" = clr.CastAs(
            sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )
        durationElem: "StoppingConditionElement" = propagate.stopping_conditions["Duration"]
        longitudeElem: "StoppingConditionElement" = propagate.stopping_conditions.add("Longitude")

        duration: "StoppingCondition" = clr.Convert(durationElem.properties, StoppingCondition)
        longitude: "StoppingCondition" = clr.Convert(longitudeElem.properties, StoppingCondition)

        duration.trip = 3600
        longitude.trip = 120

        # configure the scripting tool to change these values
        sequence.scripting_tool.enable = True
        durationAttr: "ScriptingSegment" = sequence.scripting_tool.segment_properties.add("duration")
        longitudeAttr: "ScriptingSegment" = sequence.scripting_tool.segment_properties.add("longitude")
        durationAttr.object_name = "Propagate"
        durationAttr.attribute = "StoppingConditions.Duration.TripValue"

        longitudeAttr.object_name = "Propagate"
        longitudeAttr.attribute = "StoppingConditions.Longitude.TripValue"

        sequence.scripting_tool.script_text(
            r"""duration=3601;
longitude = 121;"""
        )

        EarlyBoundTests.AG_VA.run_mission_control_sequence()
        Assert.assertEqual(3600, duration.trip)
        Assert.assertAlmostEqual(120, float(longitude.trip), delta=Math2.Epsilon12)

        propagate.stopping_conditions.remove("Duration")
        longitude.trip = 100

        EarlyBoundTests.AG_VA.run_mission_control_sequence()
        # make sure that the scripting tool doesn't try to reset this value to 120, the old
        # archived value
        Assert.assertEqual(100, longitude.trip)

        # REQ 57324 - Add Matlab as available script language

        sequence.scripting_tool.language_type = LANGUAGE.MATLAB
        Assert.assertEqual(sequence.scripting_tool.language_type, LANGUAGE.MATLAB)

        # set user comment on a parameter, REQ 59661
        param: "ScriptingParameter" = sequence.scripting_tool.parameters.add("Parameter")
        param.user_comment = "This is a custom user comment"
        Assert.assertEqual("This is a custom user comment", param.user_comment)

        # Set back to default configuration
        EarlyBoundTests.AG_VA.main_sequence.remove_all()
        EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "Initial State", "-")
        EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")

    # endregion

    # region DiffAcrossAndValueAtOtherSatellites

    def test_DiffAcrossAndValueAtOtherSatellites(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - DiffAcrossAndValueAtOtherSatellites START")
        newSat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "DiffAcross"), Satellite
        )
        anotherSat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "NonGator"), Satellite
        )
        newSat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        otherMCS: "DriverMissionControlSequence" = clr.CastAs(newSat.propagator, DriverMissionControlSequence)
        prop: "MissionControlSequencePropagate" = clr.CastAs(
            EarlyBoundTests.AG_VA.main_sequence["Propagate"], MissionControlSequencePropagate
        )
        result: "IComponentInfo" = (clr.Convert(prop, IMissionControlSequenceSegment)).results.add(
            "Segments/Difference Across Segments Across Satellites"
        )
        diffAcrossSegs: "StateCalcDifferenceAcrossSegmentsOtherSat" = clr.CastAs(
            result, StateCalcDifferenceAcrossSegmentsOtherSat
        )
        diffAcrossSegs.segment_state_to_use = SEGMENT_STATE.FINAL
        Assert.assertEqual(SEGMENT_STATE.FINAL, diffAcrossSegs.segment_state_to_use)
        STKUtilHelper.TestComponent(clr.CastAs(diffAcrossSegs, IComponentInfo), False)
        refSat: "LinkToObject" = diffAcrossSegs.reference_sat
        refSat.bind_to("Satellite/DiffAcross")
        Assert.assertEqual("Satellite/DiffAcross", refSat.name)

        def action61():
            refSat.bind_to("Satellite/NonGator")

        TryCatchAssertBlock.DoAssert(action61)
        diffAcrossSegs.calc_object_name = "Keplerian Elems/Eccentricity"
        Assert.assertEqual("Eccentricity", diffAcrossSegs.calc_object_name)
        diffAcrossSegs.other_segment_name = "Propagate"
        Assert.assertEqual("Propagate", diffAcrossSegs.other_segment_name)
        diffAcrossSegs.difference_order = SEGMENT_DIFFERENCE_ORDER.SEGMENT_MINUS_CURRENT
        Assert.assertEqual(SEGMENT_DIFFERENCE_ORDER.SEGMENT_MINUS_CURRENT, diffAcrossSegs.difference_order)

        result = (clr.Convert(prop, IMissionControlSequenceSegment)).results.add(
            "Segments/Value At Segment Other Satellite"
        )
        valueAtSegment: "StateCalcValueAtSegmentOtherSat" = clr.CastAs(result, StateCalcValueAtSegmentOtherSat)
        STKUtilHelper.TestComponent(clr.CastAs(valueAtSegment, IComponentInfo), False)
        refSat = valueAtSegment.reference_sat
        refSat.bind_to("Satellite/DiffAcross")
        Assert.assertEqual("Satellite/DiffAcross", refSat.name)

        def action62():
            refSat.bind_to("Satellite/NonGator")

        TryCatchAssertBlock.DoAssert(action62)
        valueAtSegment.calc_object_name = "Keplerian Elems/Eccentricity"
        Assert.assertEqual("Eccentricity", valueAtSegment.calc_object_name)
        valueAtSegment.other_segment_name = "Propagate"
        Assert.assertEqual("Propagate", valueAtSegment.other_segment_name)
        valueAtSegment.segment_state_to_use = SEGMENT_STATE.INITIAL
        Assert.assertEqual(SEGMENT_STATE.INITIAL, valueAtSegment.segment_state_to_use)

        otherMCS.run_mission_control_sequence()
        EarlyBoundTests.AG_VA.run_mission_control_sequence()

        value: float = float(
            (clr.Convert(prop, IMissionControlSequenceSegment)).get_result_value(
                "Difference_Across_Segments_Across_Satellites"
            )
        )
        Assert.assertAlmostEqual(0, Math.Round(value, 2), delta=1e-05)
        value = float(
            (clr.Convert(prop, IMissionControlSequenceSegment)).get_result_value("Value_At_Segment_Other_Satellite")
        )
        Assert.assertAlmostEqual(0, Math.Round(value, 2), delta=1e-05)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "DiffAcross")
        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "NonGator")
        (clr.Convert(prop, IMissionControlSequenceSegment)).results.remove(
            "Difference_Across_Segments_Across_Satellites"
        )
        (clr.Convert(prop, IMissionControlSequenceSegment)).results.remove("Value_At_Segment_Other_Satellite")
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - DiffAcrossAndValueAtOtherSatellites STOP")

    # endregion

    # region AppendRun
    @category("Causes crashes")
    def test_AppendRun(self):
        EarlyBoundTests.AG_VA.main_sequence.remove_all()
        initialState: "MissionControlSequenceInitialState" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-"),
            MissionControlSequenceInitialState,
        )
        propagate: "MissionControlSequencePropagate" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"),
            MissionControlSequencePropagate,
        )
        (clr.Convert(propagate.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        maneuver: "MissionControlSequenceManeuver" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"),
            MissionControlSequenceManeuver,
        )
        (
            clr.Convert(
                (clr.Convert(maneuver.maneuver, ManeuverImpulsive)).attitude_control,
                AttitudeControlImpulsiveVelocityVector,
            )
        ).delta_v_magnitude = 0.5
        propagate1: "MissionControlSequencePropagate" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Propagate1", "-"),
            MissionControlSequencePropagate,
        )
        propagate2: "MissionControlSequencePropagate" = clr.Convert(
            EarlyBoundTests.AG_VA.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Propagate2", "-"),
            MissionControlSequencePropagate,
        )

        # region Append
        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.append_run()
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()
        spatialInfo: "VehicleSpatialInfo" = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(
            False
        )
        spatialState: "SpatialState" = spatialInfo.get_state(
            (clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch
        )

        # the appended run will be 2 hours long
        convUtil: "ConversionUtility" = TestBase.Application.conversion_utility
        startTime: "Date" = convUtil.new_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime: "Date" = convUtil.new_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span: "Quantity" = stopTime.span(startTime)
        Assert.assertEqual(7200, span.value)

        # endregion

        # region AppendFromTimeClearForward

        # now append after the end of the first propagate and overwrite a maneuver and another propagate
        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 1.0
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate1, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        EarlyBoundTests.AG_VA.append_run_from_time(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).final_state.epoch, CLEAR_EPHEMERIS_DIRECTION.AFTER
        )
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        # the appended run will be two hours
        spatialInfo = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(False)
        spatialState = spatialInfo.get_state(
            (clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch
        )

        startTime = convUtil.new_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime = convUtil.new_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span = stopTime.span(startTime)
        Assert.assertEqual(7200, span.value)

        # set up getting the SMA from the ephemeris, not the states of the segments
        astgValues: "DataProviderGroup" = clr.CastAs(
            (clr.Convert(EarlyBoundTests.AG_SAT, IStkObject)).data_providers["Astrogator Values"], DataProviderGroup
        )
        dp: "DataProviderTimeVarying" = clr.CastAs(astgValues.group["Keplerian Elems"], DataProviderTimeVarying)
        elems = ["Time", "Semimajor_Axis"]

        # get the sma at the end of the propagate2 segment
        resInfo: "DataProviderResult" = dp.exec_single_elements(clr.Convert(spatialState.stop_time, str), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()

        Assert.assertLess(float((result[0])), 7000)  # show that the maneuver doesn't occur

        # endregion

        # region AppendFromTimeClearBackwards

        # now append after the end of the first propagate but clear the stuff before the appended run.
        # there's going to be a strange discontinuity when the hour propagation ends and the satellite jumps
        # to the long propagate1 ephemeris.
        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 1.0
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate1, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        EarlyBoundTests.AG_VA.append_run_from_time(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).final_state.epoch, CLEAR_EPHEMERIS_DIRECTION.BEFORE
        )
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        # the appended run will start at the end of the first propagate and end at the end of the long propagate from the previous run
        # bookkeeping should be that the starting epoch is 1 hour after the initial state and the total
        # span is 12 hours 1 second.  The orbit in the first hour will have an SMA around 6678 and after that will be the larger one
        # post-maneuver
        # need to get a new spatial state since the old one isn't in the ephemeris anymore
        spatialInfo = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(False)
        spatialState = spatialInfo.get_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).initial_state.epoch
        )
        startTime.set_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime.set_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span = stopTime.span(startTime)
        Assert.assertEqual(43201, span.value)  # total length of ephemeris

        initialStateEpoch: "Date" = convUtil.new_date(
            "UTCG", clr.Convert((clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch, str)
        )
        timeFromEpoch: "Quantity" = startTime.span(initialStateEpoch)
        Assert.assertEqual(3600, timeFromEpoch.value)

        # test that the two orbits are different for the different sections

        firstTestPoint: "Date" = startTime.add("sec", 1800)  # puts us in the middle of the one hour propagate

        resInfo = dp.exec_single_elements(firstTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        secondTestPoint: "Date" = startTime.add("sec", 21600)  # puts us in middle of long propagate
        resInfo = dp.exec_single_elements(secondTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertGreater(float((result[0])), 7000)

        # endregion

        # region AppendFromTimeDontClear

        # append to the end of the propagate but don't clear anything.  This will keep the previous hour propagation
        # and append on the new one and keep the old 12 hour one also...  the total span should be 13 hours 1 second
        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 1.0
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate1, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        EarlyBoundTests.AG_VA.append_run_from_time(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).final_state.epoch,
            CLEAR_EPHEMERIS_DIRECTION.NO_CLEAR,
        )
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        spatialInfo = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(False)
        spatialState = spatialInfo.get_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).initial_state.epoch
        )
        startTime.set_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime.set_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span = stopTime.span(startTime)
        # total length of ephemeris should be 13:00:01;
        Assert.assertEqual(46801, span.value)

        initialStateEpoch = convUtil.new_date(
            "UTCG", clr.Convert((clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch, str)
        )
        timeFromEpoch = startTime.span(initialStateEpoch)
        # test that ephemeris starts at initial state epoch
        Assert.assertEqual(0, timeFromEpoch.value)

        # test that the orbits are different for the different sections

        # puts us in the middle of the one hour propagate
        firstTestPoint = startTime.add("sec", 1800)

        resInfo = dp.exec_single_elements(firstTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        # test that the second propgate is based on the pre-maneuver state

        # puts us in middle of second hour propagate
        secondTestPoint = startTime.add("sec", 5400)
        resInfo = dp.exec_single_elements(secondTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        # test that the long propagate is still intact and based on the post maneuver state

        thirdTestPoint: "Date" = startTime.add("sec", 21600)
        resInfo = dp.exec_single_elements(thirdTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertGreater(float((result[0])), 7000)

        # endregion

        # region AppendFromTimeWithManeuver

        # append from time using a post maneuver state, orbit should be higher

        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate1, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        EarlyBoundTests.AG_VA.append_run_from_time(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).final_state.epoch, CLEAR_EPHEMERIS_DIRECTION.AFTER
        )
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        # append from time using the final time of propagate, coincident with maneuver, orbit should
        # be the postmaneuver one

        spatialInfo = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(False)
        spatialState = spatialInfo.get_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).initial_state.epoch
        )
        startTime.set_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime.set_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span = stopTime.span(startTime)
        # total length of ephemeris should be 2:00:00;
        Assert.assertEqual(7200, span.value)

        initialStateEpoch = convUtil.new_date(
            "UTCG", clr.Convert((clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch, str)
        )
        timeFromEpoch = startTime.span(initialStateEpoch)
        # test that ephemeris starts at initial state epoch
        Assert.assertEqual(0, timeFromEpoch.value)

        # test that the orbits are different for the different sections

        # puts us in the middle of the one hour propagate
        firstTestPoint = startTime.add("sec", 1800)

        resInfo = dp.exec_single_elements(firstTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        # test that the second propgate is based on the post-maneuver state since
        # we picked at time and the maneuver is included in the state at that time

        # puts us in middle of second hour propagate
        secondTestPoint = startTime.add("sec", 5400)
        resInfo = dp.exec_single_elements(secondTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertGreater(float((result[0])), 7000)

        # endregion

        # region AppendFromStateClearForward
        # append run from the final state of the propagate will not include the maneuver
        # and the orbit should be the low one

        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate1, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        EarlyBoundTests.AG_VA.append_run_from_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).final_state, CLEAR_EPHEMERIS_DIRECTION.AFTER
        )
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        # append from state using the final state of propagate, orbit should
        # be the pre maneuver one

        spatialInfo = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(False)
        spatialState = spatialInfo.get_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).initial_state.epoch
        )
        startTime.set_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime.set_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span = stopTime.span(startTime)
        # total length of ephemeris should be 2:00:00;
        Assert.assertEqual(7200, span.value)

        initialStateEpoch = convUtil.new_date(
            "UTCG", clr.Convert((clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch, str)
        )
        timeFromEpoch = startTime.span(initialStateEpoch)
        # test that ephemeris starts at initial state epoch
        Assert.assertEqual(0, timeFromEpoch.value)
        # test that the orbits are the same for the different sections

        # puts us in the middle of the one hour propagate
        firstTestPoint = startTime.add("sec", 1800)

        resInfo = dp.exec_single_elements(firstTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        # test that the second propgate is based on the pre-maneuver state since
        # we picked at state and the maneuver is not included in the state

        # puts us in middle of second hour propagate
        secondTestPoint = startTime.add("sec", 5400)
        resInfo = dp.exec_single_elements(secondTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)
        # endregion

        # region AppendFromStateClearBackwards
        # append run from the final state of the propagate will not include the maneuver
        # and the orbit should be the low one, clearing ephemeris backwards from state
        # should include only the 1 hour low propagated orbit and the rest of the 12 hour
        # high orbit.  Total span is 12 hours.

        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate1, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        EarlyBoundTests.AG_VA.append_run_from_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).final_state, CLEAR_EPHEMERIS_DIRECTION.BEFORE
        )
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        # the appended run will start at the end of the first propagate and end at the end of the long propagate from the previous run
        # bookkeeping should be that the starting epoch is 1 hour after the initial state and the total
        # span is 12 hours.  The orbit in the first hour will have an SMA around 6678 and after that will be the larger one
        # post-maneuver

        spatialInfo = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(False)
        spatialState = spatialInfo.get_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).initial_state.epoch
        )
        startTime.set_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime.set_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span = stopTime.span(startTime)
        Assert.assertEqual(43200, span.value)  # total length of ephemeris

        initialStateEpoch = convUtil.new_date(
            "UTCG", clr.Convert((clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch, str)
        )
        timeFromEpoch = startTime.span(initialStateEpoch)
        Assert.assertEqual(3600, timeFromEpoch.value)

        # test that the two orbits are different for the different sections

        firstTestPoint = startTime.add("sec", 1800)  # puts us in the middle of the one hour propagate

        resInfo = dp.exec_single_elements(firstTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        secondTestPoint = startTime.add("sec", 21600)  # puts us in middle of long propagate
        resInfo = dp.exec_single_elements(secondTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertGreater(float((result[0])), 7000)
        # endregion

        # region AppendFromStateDontClear
        # append run from the final state of the propagate will not include the maneuver
        # and the orbit should be the low one, keeping the hour of low orbit before and
        # also keeping the remnants of the 12 hour high orbit

        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate1, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        EarlyBoundTests.AG_VA.append_run_from_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).final_state, CLEAR_EPHEMERIS_DIRECTION.NO_CLEAR
        )
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        # append from state using the final state of propagate, orbit should
        # be the pre maneuver one

        spatialInfo = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(False)
        spatialState = spatialInfo.get_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).initial_state.epoch
        )
        startTime.set_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime.set_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span = stopTime.span(startTime)
        # total length of ephemeris should be 13:00:00;
        Assert.assertEqual(46800, span.value)

        initialStateEpoch = convUtil.new_date(
            "UTCG", clr.Convert((clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch, str)
        )
        timeFromEpoch = startTime.span(initialStateEpoch)
        # test that ephemeris starts at initial state epoch
        Assert.assertEqual(0, timeFromEpoch.value)

        # test that the orbits are different for the different sections

        # puts us in the middle of the one hour propagate
        firstTestPoint = startTime.add("sec", 1800)

        resInfo = dp.exec_single_elements(firstTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        # test that the second propgate is based on the pre-maneuver state

        # puts us in middle of second hour propagate
        secondTestPoint = startTime.add("sec", 5400)
        resInfo = dp.exec_single_elements(secondTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        # test that the long propagate is still intact and based on the post maneuver state

        thirdTestPoint = startTime.add("sec", 21600)
        resInfo = dp.exec_single_elements(thirdTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertGreater(float((result[0])), 7000)
        # endregion

        # region CheckInitialStateWorks

        # append run from the inital state of the maneuver will not include the maneuver
        # and the orbit should be the low one

        EarlyBoundTests.AG_VA.end_run()
        EarlyBoundTests.AG_VA.begin_run()
        (clr.Convert(initialState, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate, IMissionControlSequenceSegment)).run()
        (clr.Convert(maneuver, IMissionControlSequenceSegment)).run()
        (clr.Convert(propagate1, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        EarlyBoundTests.AG_VA.append_run_from_state(
            (clr.Convert(maneuver, IMissionControlSequenceSegment)).initial_state, CLEAR_EPHEMERIS_DIRECTION.AFTER
        )
        (clr.Convert(propagate2.stopping_conditions["Duration"].properties, StoppingCondition)).trip = 3600
        (clr.Convert(propagate2, IMissionControlSequenceSegment)).run()
        EarlyBoundTests.AG_VA.end_run()

        # append from state using the intial state of the maneuever, orbit should
        # be the pre maneuver one

        spatialInfo = (clr.Convert(EarlyBoundTests.AG_SAT, IProvideSpatialInfo)).get_spatial_info(False)
        spatialState = spatialInfo.get_state(
            (clr.Convert(propagate, IMissionControlSequenceSegment)).initial_state.epoch
        )
        startTime.set_date("UTCG", clr.Convert(spatialState.start_time, str))
        stopTime.set_date("UTCG", clr.Convert(spatialState.stop_time, str))
        span = stopTime.span(startTime)
        # total length of ephemeris should be 2:00:00;
        Assert.assertEqual(7200, span.value)

        initialStateEpoch = convUtil.new_date(
            "UTCG", clr.Convert((clr.Convert(initialState, IMissionControlSequenceSegment)).initial_state.epoch, str)
        )
        timeFromEpoch = startTime.span(initialStateEpoch)
        # test that ephemeris starts at initial state epoch
        Assert.assertEqual(0, timeFromEpoch.value)
        # test that the orbits are the same for the different sections

        # puts us in the middle of the one hour propagate
        firstTestPoint = startTime.add("sec", 1800)

        resInfo = dp.exec_single_elements(firstTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        # test that the second propgate is based on the pre-maneuver state since
        # we picked at state and the maneuver is not included in the state

        # puts us in middle of second hour propagate
        secondTestPoint = startTime.add("sec", 5400)
        resInfo = dp.exec_single_elements(secondTestPoint.format("UTCG"), elems)
        result = resInfo.data_sets.get_data_set_by_name("Semimajor_Axis").get_values()
        Assert.assertLess(float((result[0])), 7000)

        # endregion

        # region ResetToBefore

        TestBase.LoadTestScenario(Path.Combine("AstrogatorTests", "AstrogatorTests.sc"))
        EarlyBoundTests.AG_SAT = clr.Convert(TestBase.Application.current_scenario.children["Satellite1"], Satellite)
        EarlyBoundTests.AG_SAT.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        EarlyBoundTests.AG_VA = clr.Convert(EarlyBoundTests.AG_SAT.propagator, DriverMissionControlSequence)

    # endregion

    # region RunCodes
    def test_RunCodes(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - DiffAcrossAndValueAtOtherSatellites START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "RunCodes"), Satellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        targSeq.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        code: "RUN_CODE" = driver.run_mission_control_sequence2()
        code0: "RUN_CODE" = RUN_CODE.ERROR
        Assert.assertEqual(code0, code)
        driver.begin_run()
        try:
            (clr.Convert(targSeq, IMissionControlSequenceSegment)).run()
            Assert.fail("Expected an exception, none thrown.")

        except STKRuntimeError as e:
            Assert.assertEqual(
                "An error occurred while running the segment.  See the Message Viewer for details, or try running the segment from the user interface.",
                str(e),
            )

        except Exception as e:
            Assert.fail(("Expected a COM exception, but got a " + type(e).FullName))

        driver.end_run()
        Assert.assertEqual(
            RUN_CODE.ERROR, (clr.Convert(targSeq, IMissionControlSequenceSegment)).properties.last_run_code
        )

        prop: "MissionControlSequencePropagate" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Prop", "-"), MissionControlSequencePropagate
        )
        prop.stopping_conditions["Duration"].enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        (clr.Convert(prop, IMissionControlSequenceSegment)).results.add("Epoch")
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles["Differential_Corrector"], ProfileDifferentialCorrector
        )
        diffCorr.control_parameters[0].enable = True
        diffCorr.results[0].enable = True
        diffCorr.max_iterations = 1
        code = driver.run_mission_control_sequence2()
        code0 = RUN_CODE.PROFILE_FAILURE
        Assert.assertEqual(code0, code)
        driver.begin_run()
        (clr.Convert(targSeq, IMissionControlSequenceSegment)).run()
        driver.end_run()
        Assert.assertEqual(
            RUN_CODE.PROFILE_FAILURE, (clr.Convert(targSeq, IMissionControlSequenceSegment)).properties.last_run_code
        )

        driver.main_sequence.remove("TargetSequence")

        stop: "IMissionControlSequenceSegment" = driver.main_sequence.insert(SEGMENT_TYPE.STOP, "STOP", "Initial_State")
        code = driver.run_mission_control_sequence2()
        code0 = RUN_CODE.STOPPED
        Assert.assertEqual(code0, code)
        driver.begin_run()
        stop.run()
        driver.end_run()
        Assert.assertEqual(
            RUN_CODE.STOPPED, (clr.Convert(stop, IMissionControlSequenceSegment)).properties.last_run_code
        )

        driver.main_sequence.remove("STOP")

        code = driver.run_mission_control_sequence2()
        code0 = RUN_CODE.MARCHING
        Assert.assertEqual(code0, code)
        seg: "IMissionControlSequenceSegment" = driver.main_sequence["Propagate"]
        driver.begin_run()
        seg.run()
        driver.end_run()
        Assert.assertEqual(RUN_CODE.MARCHING, seg.properties.last_run_code)

        # TODO: fix NUNIT2JUNIT test conversion to handle OnPercentCompleteUpdate tests
        (clr.Convert(sat, IStkObject)).unload()

    def Application_OnPercentCompleteUpdate(self, args: "PctCmpltEventArgs"):
        args.cancel()

    # endregion

    # region NumIterations
    def test_NumIterations(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - NumIterations START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "NumIterations"), Satellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        targSeq.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES

        prop: "MissionControlSequencePropagate" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Prop", "-"), MissionControlSequencePropagate
        )
        prop.stopping_conditions["Duration"].enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        (clr.Convert(prop, IMissionControlSequenceSegment)).results.add("Time/Duration")

        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles["Differential_Corrector"], ProfileDifferentialCorrector
        )
        Assert.assertEqual(0, diffCorr.num_iterations)
        diffCorr.control_parameters[0].enable = True
        diffCorr.results[0].enable = True
        diffCorr.results[0].desired_value = 86400

        driver.run_mission_control_sequence()
        Assert.assertEqual(12, diffCorr.num_iterations)

        # test the "Values" attribute
        Assert.assertEqual(13, Array.Length(diffCorr.control_parameters[0].values))
        Assert.assertAlmostEqual(43200.0, float(diffCorr.control_parameters[0].values[0]), delta=1e-06)
        Assert.assertAlmostEqual(46800.0, float(diffCorr.control_parameters[0].values[1]), delta=1e-06)
        Assert.assertAlmostEqual(86400.0, float(diffCorr.control_parameters[0].values[12]), delta=1e-06)

        Assert.assertEqual(13, Array.Length(diffCorr.results[0].values))
        Assert.assertAlmostEqual(43200.0, float(diffCorr.results[0].values[0]), delta=1e-06)
        Assert.assertAlmostEqual(46800.0, float(diffCorr.results[0].values[1]), delta=1e-06)
        Assert.assertAlmostEqual(86400.0, float(diffCorr.results[0].values[12]), delta=1e-06)

        # make sure Values are being treated as a quantity
        TestBase.Application.current_scenario.root.unit_preferences.set_current_unit("TimeUnit", "day")
        Assert.assertAlmostEqual(1.0, float(diffCorr.control_parameters[0].values[12]), delta=1e-06)
        Assert.assertAlmostEqual(1.0, float(diffCorr.results[0].values[12]), delta=1e-06)
        TestBase.Application.current_scenario.root.unit_preferences.set_current_unit("TimeUnit", "sec")

        # test "Values" for dates
        diffCorr.control_parameters[0].enable = False
        diffCorr.results[0].enable = False
        initialStateSeg: "MissionControlSequenceInitialState" = clr.CastAs(
            driver.main_sequence["Initial_State"], MissionControlSequenceInitialState
        )
        initialStateSeg.orbit_epoch = "01 Jul 2000 12:00:00"

        prop.stopping_conditions["Duration"].active = False

        epochStop: "StoppingConditionElement" = prop.stopping_conditions.add("Epoch")
        epochStop.active = True
        epochStop.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        stop: "StoppingCondition" = clr.CastAs(epochStop.properties, StoppingCondition)
        stop.trip = "02 Jul 2000 12:00:00.000"

        (clr.Convert(prop, IMissionControlSequenceSegment)).results.add("Epoch")

        epochControl: "DifferentialCorrectorControl" = diffCorr.control_parameters.get_control_by_paths(
            "Prop", "StoppingConditions.Epoch.TripValue"
        )
        epochResult: "DifferentialCorrectorResult" = diffCorr.results.get_result_by_paths("Prop", "Epoch")

        epochControl.enable = True
        epochControl.max_step = 3600.0

        epochResult.enable = True
        epochResult.desired_value = "2 Jul 2000 14:00:00.000"

        driver.run_mission_control_sequence()

        Assert.assertEqual("2 Jul 2000 14:00:00.000", epochControl.values[2])
        Assert.assertEqual("2 Jul 2000 14:00:00.000", epochResult.values[2])

        (clr.Convert(sat, IStkObject)).unload()

    # endregion

    # region CustomUnits
    @category("ExcludeOnLinux")
    def test_CustomUnits(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - NumIterations START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "CustomUnits"), Satellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        targSeq.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES

        prop: "MissionControlSequencePropagate" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Prop", "-"), MissionControlSequencePropagate
        )
        prop.stopping_conditions["Duration"].enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        (clr.Convert(prop, IMissionControlSequenceSegment)).results.add("Time/Duration")
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles["Differential_Corrector"], ProfileDifferentialCorrector
        )

        control: "DifferentialCorrectorControl" = diffCorr.control_parameters[0]
        control.enable = True
        control.use_custom_display_unit = True
        Assert.assertTrue(control.use_custom_display_unit)
        control.use_custom_display_unit = False
        Assert.assertFalse(control.use_custom_display_unit)

        def action63():
            control.custom_display_unit = "hr"

        TryCatchAssertBlock.DoAssert(action63)
        control.use_custom_display_unit = True
        control.custom_display_unit = "hr"
        Assert.assertEqual("hr", control.custom_display_unit)

        result: "DifferentialCorrectorResult" = diffCorr.results[0]
        result.enable = True
        result.use_custom_display_unit = True
        Assert.assertTrue(result.use_custom_display_unit)
        result.use_custom_display_unit = False
        Assert.assertFalse(result.use_custom_display_unit)

        def action64():
            result.custom_display_unit = "hr"

        TryCatchAssertBlock.DoAssert(action64)
        result.use_custom_display_unit = True
        result.custom_display_unit = "hr"
        Assert.assertEqual("hr", result.custom_display_unit)

        (clr.Convert(sat, IStkObject)).unload()

    # endregion

    # region GeodeticInitState
    def test_GeodeticInitState(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - GeodeticInitState START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "GeodeticInitState"),
            Satellite,
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        initState: "MissionControlSequenceInitialState" = clr.CastAs(
            driver.main_sequence["Initial_State"], MissionControlSequenceInitialState
        )
        initState.coord_system_name = "CentralBody/Earth Inertial"

        def action65():
            initState.set_element_type(ELEMENT_TYPE.GEODETIC)

        TryCatchAssertBlock.DoAssert(action65)
        initState.coord_system_name = "CentralBody/Earth Fixed"
        initState.set_element_type(ELEMENT_TYPE.GEODETIC)
        Assert.assertEqual(ELEMENT_TYPE.GEODETIC, initState.element_type)
        geodetic: "ElementGeodetic" = clr.CastAs(initState.element, ElementGeodetic)
        Assert.assertIsNotNone(geodetic)

        geodetic.latitude = 45
        Assert.assertAlmostEqual(45, float(geodetic.latitude), delta=1e-09)

        def action66():
            geodetic.latitude = 100

        TryCatchAssertBlock.DoAssert(action66)

        geodetic.longitude = 135
        Assert.assertAlmostEqual(135, float(geodetic.longitude), delta=1e-09)

        geodetic.altitude = 150
        Assert.assertAlmostEqual(150, float(geodetic.altitude), delta=1e-09)

        def action67():
            geodetic.altitude = -1000

        TryCatchAssertBlock.DoAssert(action67)

        geodetic.radius_magnitude = 7000
        Assert.assertAlmostEqual(7000, float(geodetic.radius_magnitude), delta=1e-09)

        def action68():
            geodetic.radius_magnitude = 5000

        TryCatchAssertBlock.DoAssert(action68)

        geodetic.latitude_rate = 0.001
        Assert.assertAlmostEqual(0.001, float(geodetic.latitude_rate), delta=1e-09)

        geodetic.longitude_rate = 0.001
        Assert.assertAlmostEqual(0.001, float(geodetic.longitude_rate), delta=1e-09)

        geodetic.altitude_rate = 0.001
        Assert.assertAlmostEqual(0.001, float(geodetic.altitude_rate), delta=1e-09)

        geodetic.radius_rate = 0.001
        Assert.assertAlmostEqual(0.001, float(geodetic.radius_rate), delta=1e-09)

        components: "ComponentInfoCollection" = (
            clr.Convert(TestBase.Application.current_scenario, Scenario)
        ).component_directory.get_components(COMPONENT.ASTROGATOR)
        geodeticElems: "ComponentInfoCollection" = components.get_folder("Calculation Objects").get_folder("Geodetic")
        geodeticElem: "StateCalcGeodeticElem" = clr.CastAs(
            (clr.Convert(geodeticElems["LatitudeRate"], ICloneable)).clone_object(), StateCalcGeodeticElem
        )
        Assert.assertIsNotNone(geodeticElem)
        geodeticElem.central_body_name = "Jupiter"
        Assert.assertEqual("Jupiter", geodeticElem.central_body_name)

        (clr.Convert(sat, IStkObject)).unload()

    # endregion

    # region NormalizedVectors
    def test_NormalizedVectors(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - GeodeticInitState START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "NormalizedVectors"),
            Satellite,
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)

        initState: "MissionControlSequenceInitialState" = clr.CastAs(
            driver.main_sequence["Initial_State"], MissionControlSequenceInitialState
        )
        initState.set_element_type(ELEMENT_TYPE.CARTESIAN)
        cart: "ElementCartesian" = clr.CastAs(initState.element, ElementCartesian)
        cart.x = 5000
        cart.y = 5000
        cart.z = 5000
        vecX: "StateCalcVectorX" = clr.CastAs(
            (clr.Convert(initState, IMissionControlSequenceSegment)).results.add("Vector/Vector X"), StateCalcVectorX
        )
        vecX.vector_name = "Satellite/NormalizedVectors Position"
        vecX.unit_dimension = "DistanceUnit"

        vecY: "StateCalcVectorY" = clr.CastAs(
            (clr.Convert(initState, IMissionControlSequenceSegment)).results.add("Vector/Vector Y"), StateCalcVectorY
        )
        vecY.vector_name = "Satellite/NormalizedVectors Position"
        vecY.unit_dimension = "DistanceUnit"

        vecZ: "StateCalcVectorZ" = clr.CastAs(
            (clr.Convert(initState, IMissionControlSequenceSegment)).results.add("Vector/Vector Z"), StateCalcVectorZ
        )
        vecZ.vector_name = "Satellite/NormalizedVectors Position"
        vecZ.unit_dimension = "DistanceUnit"

        driver.run_mission_control_sequence()

        Assert.assertAlmostEqual(
            5000,
            float((clr.Convert(initState, IMissionControlSequenceSegment)).get_result_value("Vector_X")),
            delta=1e-09,
        )
        Assert.assertAlmostEqual(
            5000,
            float((clr.Convert(initState, IMissionControlSequenceSegment)).get_result_value("Vector_Y")),
            delta=1e-09,
        )
        Assert.assertAlmostEqual(
            5000,
            float((clr.Convert(initState, IMissionControlSequenceSegment)).get_result_value("Vector_Z")),
            delta=1e-09,
        )

        vecX.normalize = True
        vecY.normalize = True
        vecZ.normalize = True

        Assert.assertEqual("Unitless", vecX.unit_dimension)
        Assert.assertEqual("Unitless", vecY.unit_dimension)
        Assert.assertEqual("Unitless", vecZ.unit_dimension)

        Assert.assertAlmostEqual(
            0.5773502691896258,
            float((clr.Convert(initState, IMissionControlSequenceSegment)).get_result_value("Vector_X")),
            delta=1e-09,
        )
        Assert.assertAlmostEqual(
            0.5773502691896258,
            float((clr.Convert(initState, IMissionControlSequenceSegment)).get_result_value("Vector_Y")),
            delta=1e-09,
        )
        Assert.assertAlmostEqual(
            0.5773502691896258,
            float((clr.Convert(initState, IMissionControlSequenceSegment)).get_result_value("Vector_Z")),
            delta=1e-09,
        )
        (clr.Convert(sat, IStkObject)).unload()

    # endregion

    # region ManeuverSummary
    def test_ManeuverSummary(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - ManeuverSummary START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ManeuverSummary"), Satellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)

        # set up the epochs
        scene: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        scene.stop_time = "3 Jan 2010 12:00:00.000"
        scene.start_time = "1 Jan 2010 12:00:00.000"
        scene.epoch = "1 Jan 2010 12:00:00.000"

        initState: "MissionControlSequenceInitialState" = clr.CastAs(
            driver.main_sequence["Initial_State"], MissionControlSequenceInitialState
        )
        initState.orbit_epoch = "2 Jan 2010 12:00:00.000"

        # set up the MCS
        man1: "MissionControlSequenceManeuver" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Man1", "-"), MissionControlSequenceManeuver
        )
        man1.set_maneuver_type(MANEUVER_TYPE.FINITE)
        man1Fin: "ManeuverFinite" = clr.CastAs(man1.maneuver, ManeuverFinite)
        man1FinStop: "StoppingCondition" = clr.CastAs(
            man1Fin.propagator.stopping_conditions[0].properties, StoppingCondition
        )
        man1FinStop.trip = 300.0

        prop2: "MissionControlSequencePropagate" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop2", "-"), MissionControlSequencePropagate
        )
        prop2Stop: "StoppingCondition" = clr.CastAs(prop2.stopping_conditions[0].properties, StoppingCondition)
        prop2Stop.trip = 1000.0

        man2: "MissionControlSequenceManeuver" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Man2", "-"), MissionControlSequenceManeuver
        )
        man2.set_maneuver_type(MANEUVER_TYPE.FINITE)
        man2Fin: "ManeuverFinite" = clr.CastAs(man2.maneuver, ManeuverFinite)
        man2FinStop: "StoppingCondition" = clr.CastAs(
            man2Fin.propagator.stopping_conditions[0].properties, StoppingCondition
        )
        man2FinStop.trip = 300.0

        prop3: "MissionControlSequencePropagate" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop3", "-"), MissionControlSequencePropagate
        )
        prop3Stop: "StoppingCondition" = clr.CastAs(prop3.stopping_conditions[0].properties, StoppingCondition)
        prop3Stop.trip = 1000.0

        man3: "MissionControlSequenceManeuver" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Man3", "-"), MissionControlSequenceManeuver
        )
        man3.set_maneuver_type(MANEUVER_TYPE.FINITE)
        man3Fin: "ManeuverFinite" = clr.CastAs(man3.maneuver, ManeuverFinite)
        man3FinStop: "StoppingCondition" = clr.CastAs(
            man3Fin.propagator.stopping_conditions[0].properties, StoppingCondition
        )
        man3FinStop.trip = 300.0

        prop4: "MissionControlSequencePropagate" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop4", "-"), MissionControlSequencePropagate
        )
        prop4Stop: "StoppingCondition" = clr.CastAs(prop4.stopping_conditions[0].properties, StoppingCondition)
        prop4Stop.trip = 1000.0

        # run the MCS
        driver.run_mission_control_sequence()

        # Run the data provider
        satObj: "IStkObject" = clr.CastAs(sat, IStkObject)
        intvl: "DataProviderInterval" = clr.CastAs(satObj.data_providers["Maneuver Summary"], DataProviderInterval)
        result: "DataProviderResult" = intvl.exec(scene.start_time, scene.stop_time)
        intervals: "DataProviderResultIntervalCollection" = result.intervals

        Assert.assertEqual("3 Jan 2010 00:00:00.000", intervals[0].start_time)
        Assert.assertEqual("3 Jan 2010 00:48:20.000", intervals[0].stop_time)

        Assert.assertEqual(9, intervals[0].data_sets.count)
        Assert.assertEqual(3, intervals[0].data_sets[0].count)

        Assert.assertEqual("Maneuver Number", intervals[0].data_sets[0].element_name)
        dataSet = intervals[0].data_sets[0].get_values()
        Assert.assertEqual(1, dataSet[0])
        Assert.assertEqual(2, dataSet[1])
        Assert.assertEqual(3, dataSet[2])

        Assert.assertEqual("Segment", intervals[0].data_sets[1].element_name)
        dataSet = intervals[0].data_sets[1].get_values()
        Assert.assertEqual("Man1", dataSet[0])
        Assert.assertEqual("Man2", dataSet[1])
        Assert.assertEqual("Man3", dataSet[2])

        Assert.assertEqual("Start Time", intervals[0].data_sets[2].element_name)
        dataSet = intervals[0].data_sets[2].get_values()
        Assert.assertEqual("3 Jan 2010 00:00:00.000000000", dataSet[0])
        Assert.assertEqual("3 Jan 2010 00:21:40.000000000", dataSet[1])
        Assert.assertEqual("3 Jan 2010 00:43:20.000000000", dataSet[2])

        Assert.assertEqual("Stop Time", intervals[0].data_sets[3].element_name)
        dataSet = intervals[0].data_sets[3].get_values()
        Assert.assertEqual("3 Jan 2010 00:05:00.000000000", dataSet[0])
        Assert.assertEqual("3 Jan 2010 00:26:40.000000000", dataSet[1])
        Assert.assertEqual("3 Jan 2010 00:48:20.000000000", dataSet[2])

        Assert.assertEqual("Duration", intervals[0].data_sets[4].element_name)
        dataSet = intervals[0].data_sets[4].get_values()
        Assert.assertEqual(300.0, dataSet[0])
        Assert.assertEqual(300.0, dataSet[1])
        Assert.assertEqual(300.0, dataSet[2])

        Assert.assertEqual("Finite Burn Duration", intervals[0].data_sets[5].element_name)
        dataSet = intervals[0].data_sets[5].get_values()
        Assert.assertEqual(300.0, dataSet[0])
        Assert.assertEqual(300.0, dataSet[1])
        Assert.assertEqual(300.0, dataSet[2])

        Assert.assertEqual("Delta V", intervals[0].data_sets[6].element_name)
        dataSet = intervals[0].data_sets[6].get_values()
        Assert.assertAlmostEqual(153.96, float(dataSet[0]), delta=0.02)
        Assert.assertAlmostEqual(162.46, float(dataSet[1]), delta=0.02)
        Assert.assertAlmostEqual(171.96, float(dataSet[2]), delta=0.02)

        Assert.assertEqual("Fuel Used", intervals[0].data_sets[7].element_name)
        dataSet = intervals[0].data_sets[7].get_values()
        Assert.assertAlmostEqual(50.99, float(dataSet[0]), delta=0.02)
        Assert.assertAlmostEqual(50.99, float(dataSet[1]), delta=0.02)
        Assert.assertAlmostEqual(50.99, float(dataSet[2]), delta=0.02)

        Assert.assertEqual("Thruster/Engine", intervals[0].data_sets[8].element_name)
        dataSet = intervals[0].data_sets[8].get_values()
        Assert.assertEqual("Constant_Thrust_and_Isp", dataSet[0])
        Assert.assertEqual("Constant_Thrust_and_Isp", dataSet[1])
        Assert.assertEqual("Constant_Thrust_and_Isp", dataSet[2])

        # now try a b/w sequence
        bwSeq: "MissionControlSequenceBackwardSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.BACKWARD_SEQUENCE, "Backwards Sequence", "Propagate"),
            MissionControlSequenceBackwardSequence,
        )

        driver.main_sequence.cut("Propagate")
        bwSeq.segments.paste("-")
        driver.main_sequence.cut("Man1")
        bwSeq.segments.paste("-")
        driver.main_sequence.cut("Prop2")
        bwSeq.segments.paste("-")
        driver.main_sequence.cut("Man2")
        bwSeq.segments.paste("-")
        driver.main_sequence.cut("Prop3")
        bwSeq.segments.paste("-")
        driver.main_sequence.cut("Man3")
        bwSeq.segments.paste("-")
        driver.main_sequence.cut("Prop4")
        bwSeq.segments.paste("-")

        driver.run_mission_control_sequence()

        # Run the data provider again
        intvl = clr.CastAs(satObj.data_providers["Maneuver Summary"], DataProviderInterval)
        result = intvl.exec(scene.start_time, scene.stop_time)
        intervals = result.intervals

        Assert.assertEqual("1 Jan 2010 23:11:40.000", intervals[0].start_time)
        Assert.assertEqual("2 Jan 2010 00:00:00.000", intervals[0].stop_time)

        Assert.assertEqual(9, intervals[0].data_sets.count)
        Assert.assertEqual(3, intervals[0].data_sets[0].count)

        Assert.assertEqual("Maneuver Number", intervals[0].data_sets[0].element_name)
        dataSet = intervals[0].data_sets[0].get_values()
        Assert.assertEqual(1, dataSet[0])
        Assert.assertEqual(2, dataSet[1])
        Assert.assertEqual(3, dataSet[2])

        Assert.assertEqual("Segment", intervals[0].data_sets[1].element_name)
        dataSet = intervals[0].data_sets[1].get_values()
        Assert.assertEqual("Backwards_Sequence.Man1", dataSet[0])
        Assert.assertEqual("Backwards_Sequence.Man2", dataSet[1])
        Assert.assertEqual("Backwards_Sequence.Man3", dataSet[2])

        Assert.assertEqual("Start Time", intervals[0].data_sets[2].element_name)
        dataSet = intervals[0].data_sets[2].get_values()
        Assert.assertEqual("1 Jan 2010 23:55:00.000000000", dataSet[0])
        Assert.assertEqual("1 Jan 2010 23:33:20.000000000", dataSet[1])
        Assert.assertEqual("1 Jan 2010 23:11:40.000000000", dataSet[2])

        Assert.assertEqual("Stop Time", intervals[0].data_sets[3].element_name)
        dataSet = intervals[0].data_sets[3].get_values()
        Assert.assertEqual("2 Jan 2010 00:00:00.000000000", dataSet[0])
        Assert.assertEqual("1 Jan 2010 23:38:20.000000000", dataSet[1])
        Assert.assertEqual("1 Jan 2010 23:16:40.000000000", dataSet[2])

        Assert.assertEqual("Duration", intervals[0].data_sets[4].element_name)
        dataSet = intervals[0].data_sets[4].get_values()
        Assert.assertEqual(300.0, dataSet[0])
        Assert.assertEqual(300.0, dataSet[1])
        Assert.assertEqual(300.0, dataSet[2])

        Assert.assertEqual("Finite Burn Duration", intervals[0].data_sets[5].element_name)
        dataSet = intervals[0].data_sets[5].get_values()
        Assert.assertEqual(300.0, dataSet[0])
        Assert.assertEqual(300.0, dataSet[1])
        Assert.assertEqual(300.0, dataSet[2])

        Assert.assertEqual("Delta V", intervals[0].data_sets[6].element_name)
        dataSet = intervals[0].data_sets[6].get_values()
        Assert.assertAlmostEqual(146.3, float(dataSet[0]), delta=0.02)
        Assert.assertAlmostEqual(139.37, float(dataSet[1]), delta=0.02)
        Assert.assertAlmostEqual(133.06, float(dataSet[2]), delta=0.02)

        Assert.assertEqual("Fuel Used", intervals[0].data_sets[7].element_name)
        dataSet = intervals[0].data_sets[7].get_values()
        Assert.assertAlmostEqual(50.99, float(dataSet[0]), delta=0.02)
        Assert.assertAlmostEqual(50.99, float(dataSet[1]), delta=0.02)
        Assert.assertAlmostEqual(50.99, float(dataSet[2]), delta=0.02)

        Assert.assertEqual("Thruster/Engine", intervals[0].data_sets[8].element_name)
        dataSet = intervals[0].data_sets[8].get_values()
        Assert.assertEqual("Constant_Thrust_and_Isp", dataSet[0])
        Assert.assertEqual("Constant_Thrust_and_Isp", dataSet[1])
        Assert.assertEqual("Constant_Thrust_and_Isp", dataSet[2])

        (clr.Convert(sat, IStkObject)).unload()

    # endregion

    # region ScriptingToolParameters
    @category("ExcludeOnLinux")
    def test_ScriptingToolParameters(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - ScriptingToolParameters START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ScriptingToolParams"),
            Satellite,
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        driver.main_sequence.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-")
        driver.main_sequence.cut("Propagate")
        sequence: "IMissionControlSequenceSequence" = clr.Convert(
            driver.main_sequence["Sequence"], IMissionControlSequenceSequence
        )
        prop: "MissionControlSequencePropagate" = clr.CastAs(
            sequence.segments.paste("-"), MissionControlSequencePropagate
        )
        sequence.scripting_tool.enable = True
        parameter: "ScriptingParameter" = sequence.scripting_tool.parameters.add("Parameter")

        # region ENG57636 / ENG59714 / ENG 59760
        # Parameters have dimension and units and min and max.

        # region ChangingUnits
        parameter.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        parameter.dimension = "TimeUnit"
        Assert.assertEqual("TimeUnit", parameter.dimension)
        parameter.unit = "hr"
        Assert.assertEqual("hr", parameter.unit)

        def action69():
            parameter.unit = "km"

        TryCatchAssertBlock.DoAssert(action69)

        # this should be 60 seconds because of the object model unit prefs
        parameter.param_value = 60

        def action70():
            parameter.param_value = "bogus"

        TryCatchAssertBlock.DoAssert(action70)

        attribute: "ScriptingSegment" = sequence.scripting_tool.segment_properties.add("Attribute")
        attribute.object_name = "Propagate"
        attribute.attribute = "StoppingConditions.Duration.TripValue"
        attribute.unit = "hr"

        sequence.scripting_tool.script_text("Attribute = Parameter;")
        sequence.apply_script()
        Assert.assertAlmostEqual(
            60,
            float((clr.Convert(prop.stopping_conditions["Duration"].properties, StoppingCondition)).trip),
            delta=1e-09,
        )

        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "hr")
        parameter.use_max_value = True
        parameter.max_value = 70  # should be hours
        Assert.assertAlmostEqual(70, float(parameter.max_value), delta=1e-13)
        parameter.param_value = 60  # this should be 60 hours
        sequence.apply_script()
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")
        Assert.assertAlmostEqual(
            (60 * 3600),
            float((clr.Convert(prop.stopping_conditions["Duration"].properties, StoppingCondition)).trip),
            delta=1e-09,
        )
        Assert.assertAlmostEqual((70 * 3600), float(parameter.max_value), delta=1e-13)
        parameter.use_min_value = False
        parameter.use_max_value = False

        # endregion

        # test setting and using the new types
        # region Boolean
        parameter.type = SCRIPTING_PARAMETER_TYPE.BOOLEAN
        Assert.assertEqual(SCRIPTING_PARAMETER_TYPE.BOOLEAN, parameter.type)

        def action71():
            parameter.dimension = "TimeUnit"

        TryCatchAssertBlock.DoAssert(action71)

        def action72():
            parameter.unit = "hr"

        TryCatchAssertBlock.DoAssert(action72)
        parameter.param_value = True
        Assert.assertEqual(True, parameter.param_value)
        parameter.param_value = False
        Assert.assertEqual(False, parameter.param_value)

        def action73():
            parameter.use_min_value = True

        TryCatchAssertBlock.DoAssert(action73)

        def action74():
            parameter.use_max_value = True

        TryCatchAssertBlock.DoAssert(action74)

        def action75():
            parameter.min_value = -1

        TryCatchAssertBlock.DoAssert(action75)

        def action76():
            parameter.max_value = 1

        TryCatchAssertBlock.DoAssert(action76)
        # endregion

        # region Integer
        parameter.type = SCRIPTING_PARAMETER_TYPE.INTEGER

        def action77():
            parameter.dimension = "TimeUnit"

        TryCatchAssertBlock.DoAssert(action77)

        def action78():
            parameter.unit = "hr"

        TryCatchAssertBlock.DoAssert(action78)
        parameter.param_value = True
        Assert.assertEqual(-1, parameter.param_value)  # VARIANT_TRUE is -1
        parameter.param_value = 1
        Assert.assertEqual(1, parameter.param_value)
        parameter.param_value = 2.1
        Assert.assertEqual(2, parameter.param_value)  # converted to int

        def action79():
            parameter.param_value = "integer"

        TryCatchAssertBlock.DoAssert(action79)
        parameter.param_value = "5"
        Assert.assertEqual(5, parameter.param_value)
        parameter.use_max_value = True
        Assert.assertEqual(True, parameter.use_max_value)
        parameter.max_value = 100
        Assert.assertEqual(100, parameter.max_value)

        def action80():
            parameter.param_value = 101

        TryCatchAssertBlock.DoAssert(action80)
        parameter.use_min_value = True
        Assert.assertEqual(True, parameter.use_min_value)
        parameter.min_value = -100
        Assert.assertEqual(-100, parameter.min_value)

        def action81():
            parameter.param_value = -101

        TryCatchAssertBlock.DoAssert(action81)
        parameter.use_min_value = False
        parameter.use_max_value = False

        def action82():
            parameter.max_value = 100

        TryCatchAssertBlock.DoAssert(action82)

        def action83():
            parameter.min_value = 100

        TryCatchAssertBlock.DoAssert(action83)
        # endregion

        # region Double
        parameter.type = SCRIPTING_PARAMETER_TYPE.DOUBLE

        def action84():
            parameter.dimension = "TimeUnit"

        TryCatchAssertBlock.DoAssert(action84)

        def action85():
            parameter.unit = "hr"

        TryCatchAssertBlock.DoAssert(action85)
        parameter.param_value = True
        Assert.assertEqual(-1, parameter.param_value)  # VARIANT_TRUE is -1
        parameter.param_value = 1.1
        Assert.assertEqual(1.1, parameter.param_value)

        def action86():
            parameter.param_value = "integer"

        TryCatchAssertBlock.DoAssert(action86)
        parameter.param_value = "5.4"
        Assert.assertEqual(5.4, parameter.param_value)

        def action87():
            parameter.max_value = 100.4

        TryCatchAssertBlock.DoAssert(action87)

        def action88():
            parameter.min_value = 100.4

        TryCatchAssertBlock.DoAssert(action88)
        parameter.use_max_value = True
        Assert.assertEqual(True, parameter.use_max_value)
        parameter.max_value = 100.4
        Assert.assertAlmostEqual(100.4, float(parameter.max_value), delta=1e-13)

        def action89():
            parameter.param_value = 101.8

        TryCatchAssertBlock.DoAssert(action89)
        parameter.use_min_value = True
        Assert.assertEqual(True, parameter.use_min_value)
        parameter.min_value = -100.4
        Assert.assertAlmostEqual(-100.4, float(parameter.min_value), delta=1e-13)

        def action90():
            parameter.param_value = -101.8

        TryCatchAssertBlock.DoAssert(action90)
        parameter.use_min_value = False
        parameter.use_max_value = False

        def action91():
            parameter.max_value = 100

        TryCatchAssertBlock.DoAssert(action91)

        def action92():
            parameter.min_value = 100

        TryCatchAssertBlock.DoAssert(action92)
        # endregion

        # region Quantity
        parameter.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        parameter.dimension = "TimeUnit"
        Assert.assertEqual("TimeUnit", parameter.dimension)
        parameter.unit = "hr"
        Assert.assertEqual("hr", parameter.unit)

        def action93():
            parameter.dimension = "NoDimension"

        TryCatchAssertBlock.DoAssert(action93)

        def action94():
            parameter.unit = "km"

        TryCatchAssertBlock.DoAssert(action94)
        parameter.param_value = 1.1
        Assert.assertEqual(1.1, parameter.param_value)

        def action95():
            parameter.param_value = "quantity"

        TryCatchAssertBlock.DoAssert(action95)
        parameter.param_value = "5.4"
        Assert.assertEqual(5.4, parameter.param_value)

        def action96():
            parameter.max_value = 100.4

        TryCatchAssertBlock.DoAssert(action96)

        def action97():
            parameter.min_value = 100.4

        TryCatchAssertBlock.DoAssert(action97)
        parameter.use_max_value = True
        Assert.assertEqual(True, parameter.use_max_value)
        parameter.max_value = 100.4
        Assert.assertAlmostEqual(100.4, float(parameter.max_value), delta=1e-13)

        def action98():
            parameter.param_value = 101.8

        TryCatchAssertBlock.DoAssert(action98)
        parameter.use_min_value = True
        Assert.assertEqual(True, parameter.use_min_value)
        parameter.min_value = -100.4
        Assert.assertAlmostEqual(-100.4, float(parameter.min_value), delta=1e-13)

        def action99():
            parameter.param_value = -101.8

        TryCatchAssertBlock.DoAssert(action99)
        parameter.use_min_value = False
        parameter.use_max_value = False

        def action100():
            parameter.max_value = 100

        TryCatchAssertBlock.DoAssert(action100)

        def action101():
            parameter.min_value = 100

        TryCatchAssertBlock.DoAssert(action101)
        # endregion

        # region Date
        parameter.type = SCRIPTING_PARAMETER_TYPE.DATE

        def action102():
            parameter.dimension = "DateFormat"

        TryCatchAssertBlock.DoAssert(action102)
        parameter.unit = "EpSec"
        Assert.assertEqual("EpSec", parameter.unit)

        # switch object model to use epsec
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        parameter.param_value = 0.0

        def action103():
            parameter.max_value = 100.4

        TryCatchAssertBlock.DoAssert(action103)

        def action104():
            parameter.min_value = 100.4

        TryCatchAssertBlock.DoAssert(action104)
        parameter.use_max_value = True
        Assert.assertEqual(True, parameter.use_max_value)
        Console.WriteLine(("param date value is " + str(parameter.param_value)))
        parameter.max_value = 100.4
        Assert.assertAlmostEqual(100.4, float(parameter.max_value), delta=1e-13)

        def action105():
            parameter.param_value = 101.8

        TryCatchAssertBlock.DoAssert(action105)
        parameter.use_min_value = True
        Assert.assertEqual(True, parameter.use_min_value)
        parameter.min_value = -100.4
        Assert.assertAlmostEqual(-100.4, float(parameter.min_value), delta=1e-13)

        def action106():
            parameter.param_value = -101.8

        TryCatchAssertBlock.DoAssert(action106)
        parameter.use_min_value = False
        parameter.use_max_value = False

        def action107():
            parameter.max_value = 100

        TryCatchAssertBlock.DoAssert(action107)

        def action108():
            parameter.min_value = 100

        TryCatchAssertBlock.DoAssert(action108)

        parameter.unit = "UTCG"
        Assert.assertEqual("UTCG", parameter.unit)
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "UTCG")
        parameter.param_value = "21 Dec 2012 12:00:00"
        Assert.assertEqual("21 Dec 2012 12:00:00.000", parameter.param_value)

        def action109():
            parameter.max_value = "21 Dec 2012 13:00:00"

        TryCatchAssertBlock.DoAssert(action109)

        def action110():
            parameter.min_value = "21 Dec 2012 11:00:00"

        TryCatchAssertBlock.DoAssert(action110)
        parameter.use_max_value = True
        Assert.assertEqual(True, parameter.use_max_value)

        def action111():
            parameter.max_value = 100.4

        TryCatchAssertBlock.DoAssert(action111)

        parameter.max_value = "21 Dec 2012 13:00:00"
        Assert.assertEqual("21 Dec 2012 13:00:00.000", parameter.max_value)

        def action112():
            parameter.param_value = "21 Dec 2012 13:01:00"

        TryCatchAssertBlock.DoAssert(action112)
        parameter.use_min_value = True
        Assert.assertEqual(True, parameter.use_min_value)

        def action113():
            parameter.min_value = -100.4

        TryCatchAssertBlock.DoAssert(action113)
        parameter.min_value = "21 Dec 2012 11:00:00"
        Assert.assertEqual("21 Dec 2012 11:00:00.000", parameter.min_value)

        def action114():
            parameter.param_value = "21 Dec 2012 10:59:00.000"

        TryCatchAssertBlock.DoAssert(action114)
        parameter.use_min_value = False
        parameter.use_max_value = False

        def action115():
            parameter.max_value = "21 Dec 2012 10:59:00.000"

        TryCatchAssertBlock.DoAssert(action115)

        def action116():
            parameter.min_value = "21 Dec 2012 10:59:00.000"

        TryCatchAssertBlock.DoAssert(action116)
        # endregion

        # region String
        parameter.type = SCRIPTING_PARAMETER_TYPE.STRING
        parameter.param_value = "Awesome"

        def action117():
            parameter.dimension = "TimeUnit"

        TryCatchAssertBlock.DoAssert(action117)

        def action118():
            parameter.unit = "hr"

        TryCatchAssertBlock.DoAssert(action118)
        Assert.assertEqual("Awesome", parameter.param_value)

        def action119():
            parameter.use_min_value = True

        TryCatchAssertBlock.DoAssert(action119)

        def action120():
            parameter.use_max_value = True

        TryCatchAssertBlock.DoAssert(action120)

        def action121():
            parameter.min_value = "min"

        TryCatchAssertBlock.DoAssert(action121)

        def action122():
            parameter.max_value = "max"

        TryCatchAssertBlock.DoAssert(action122)
        # endregion

        # region Enumeration
        parameter.type = SCRIPTING_PARAMETER_TYPE.ENUMERATION
        enumChoices: "ScriptingParameterEnumerationChoiceCollection" = parameter.enumeration_choices
        choice1: "ScriptingParameterEnumerationChoice" = enumChoices[0]
        choice1A: "ScriptingParameterEnumerationChoice" = enumChoices.get_item_by_index(0)
        choice1B: "ScriptingParameterEnumerationChoice" = enumChoices.get_item_by_name(choice1.name)
        Assert.assertEqual(
            choice1.name,
            choice1A.name,
            "propget and GetItemByIndex should return same ScriptingParameterEnumerationChoice",
        )
        Assert.assertEqual(
            choice1.name,
            choice1B.name,
            "propget and GetItemByName should return same ScriptingParameterEnumerationChoice",
        )
        choice1.name = "Enum1"
        Assert.assertEqual("Enum1", choice1.name)
        choice1.value = 15
        Assert.assertEqual(15, choice1.value)
        choice2: "ScriptingParameterEnumerationChoice" = enumChoices.add("Enum2")
        Assert.assertEqual(2, parameter.enumeration_choices.count)
        parameter.enumeration_choices.remove("Enum2")
        Assert.assertEqual(1, parameter.enumeration_choices.count)
        choice2 = parameter.enumeration_choices.insert_copy(choice1)
        Assert.assertEqual(2, parameter.enumeration_choices.count)
        Assert.assertEqual("Enum2", choice2.name)
        Assert.assertEqual(0, choice2.value)  # value required to be unique.
        parameter.enumeration_choices.cut("Enum2")
        choice2 = parameter.enumeration_choices.paste()
        Assert.assertEqual(2, parameter.enumeration_choices.count)
        Assert.assertEqual("Enum2", choice2.name)
        enumChoices.add("Enum3")
        parameter.param_value = "Enum2"
        Assert.assertEqual("Enum2", parameter.param_value)

        def action123():
            parameter.dimension = "TimeUnit"

        TryCatchAssertBlock.DoAssert(action123)

        def action124():
            parameter.unit = "hr"

        TryCatchAssertBlock.DoAssert(action124)

        def action125():
            parameter.use_min_value = True

        TryCatchAssertBlock.DoAssert(action125)

        def action126():
            parameter.use_max_value = True

        TryCatchAssertBlock.DoAssert(action126)

        def action127():
            parameter.min_value = "min"

        TryCatchAssertBlock.DoAssert(action127)

        def action128():
            parameter.max_value = "max"

        TryCatchAssertBlock.DoAssert(action128)
        # endregion

        rttip: "IRuntimeTypeInfoProvider" = clr.CastAs(enumChoices, IRuntimeTypeInfoProvider)
        Assert.assertIsNotNone(rttip)
        rtti: "RuntimeTypeInfo" = rttip.provide_runtime_type_info
        if rtti.is_collection:
            i: int = 0
            while i < rtti.count:
                pi: "PropertyInfo" = rtti.get_item(i)
                rttip2: "IRuntimeTypeInfoProvider" = clr.CastAs(pi.get_value(), IRuntimeTypeInfoProvider)
                if rttip2 != None:
                    rtti2: "RuntimeTypeInfo" = rttip2.provide_runtime_type_info

                    name: "PropertyInfo" = rtti2.properties[0]
                    Assert.assertEqual(enumChoices[i].name, clr.Convert(name.get_value(), str))
                    value: "PropertyInfo" = rtti2.properties[1]
                    Assert.assertEqual(enumChoices[i].value, int(value.GetValue()))

                i += 1

        # endregion

        # region ENG57699
        # Parameters can be strings.
        attribute.attribute = "Propagator"
        parameter.type = SCRIPTING_PARAMETER_TYPE.STRING
        Assert.assertEqual(SCRIPTING_PARAMETER_TYPE.STRING, parameter.type)
        parameter.param_value = "Earth J2"
        sequence.apply_script()
        Assert.assertEqual("Earth J2", prop.propagator_name)

        # endregion

        # region ENG57878
        # Parameter values can be inherited from previous profiles.
        driver.main_sequence.remove("Sequence")

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        dc1: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles["Differential_Corrector"], ProfileDifferentialCorrector
        )
        dc1.scripting_tool.enable = True
        param: "ScriptingParameter" = dc1.scripting_tool.parameters.add("Parameter")
        # set up some initial parameter values
        param.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        param.dimension = "TimeUnit"
        param.unit = "hr"
        param.param_value = "21"

        def action129():
            param.inherit_value = True

        # places you shouldn't be able to inherit:  first profile, standalone profiles, sequence scripting tools
        TryCatchAssertBlock.DoAssert(action129)
        scriptTool: "ProfileScriptingTool" = clr.CastAs(targSeq.profiles.add("Scripting Tool"), ProfileScriptingTool)
        scriptTool.enable = True
        standAloneParam: "ScriptingParameter" = scriptTool.parameters.add("Parameter")

        def action130():
            standAloneParam.inherit_value = True

        TryCatchAssertBlock.DoAssert(action130)
        standAloneSeq: "IMissionControlSequenceSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"), IMissionControlSequenceSequence
        )
        standAloneSeq.scripting_tool.enable = True
        seqParam: "ScriptingParameter" = standAloneSeq.scripting_tool.parameters.add("Parameter")

        def action131():
            seqParam.inherit_value = True

        TryCatchAssertBlock.DoAssert(action131)
        targSeq.profiles.remove("Scripting Tool")
        driver.main_sequence.remove("Sequence")

        # add a second differential corrector
        dc2: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add("Differential_Corrector"), ProfileDifferentialCorrector
        )
        dc2.scripting_tool.enable = True
        param2: "ScriptingParameter" = dc2.scripting_tool.parameters.add("Parameter")

        # now with identically named parameters we can get somewhere
        # set up some initial values
        param2.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        param2.dimension = "DistanceUnit"
        param2.unit = "km"
        param2.param_value = 42

        param2.inherit_value = True
        Assert.assertEqual(True, param2.inherit_value)

        # all values should now be identical to the first parameters.
        Assert.assertEqual(param.type, param2.type)
        Assert.assertEqual(param.dimension, param2.dimension)
        Assert.assertEqual(param.unit, param2.unit)
        Assert.assertEqual(param.param_value, param2.param_value)

        # turn off inherit and everything should go back to before
        param2.inherit_value = False
        Assert.assertEqual("DistanceUnit", param2.dimension)
        Assert.assertEqual("km", param2.unit)
        Assert.assertEqual(42, float(param2.param_value))

        # change name and shouldn't be able to inherit
        param2.inherit_value = True
        param2.name = "NewName"
        Assert.assertEqual(False, param2.inherit_value)
        param2.name = "Parameter"

        # when inherit is on, the second parameter should inherit all properties from first and shouldn't be able to set them
        param.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        param.dimension = "TimeUnit"
        param.unit = "hr"
        param.param_value = "21"
        param2.inherit_value = True
        Assert.assertEqual(SCRIPTING_PARAMETER_TYPE.QUANTITY, param2.type)

        def action132():
            param2.type = SCRIPTING_PARAMETER_TYPE.INTEGER

        TryCatchAssertBlock.DoAssert(action132)
        Assert.assertEqual("TimeUnit", param2.dimension)

        def action133():
            param2.dimension = "TimeUnit"

        TryCatchAssertBlock.DoAssert(action133)
        Assert.assertEqual("hr", param2.unit)

        def action134():
            param2.unit = "hr"

        TryCatchAssertBlock.DoAssert(action134)
        Assert.assertEqual(21, param2.param_value)

        def action135():
            param2.param_value = 21

        TryCatchAssertBlock.DoAssert(action135)

        # rename the first guy and see that inherit is disabled
        param.name = "Rename"
        Assert.assertEqual(False, param2.inherit_value)
        param.name = "Parameter"

        # change the name of the inherited parameter to another one
        anotherParam: "ScriptingParameter" = dc1.scripting_tool.parameters.add("AnotherParam")
        anotherParam.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        anotherParam.dimension = "AngleUnit"
        anotherParam.unit = "rad"
        anotherParam.param_value = 2.6
        param2.name = anotherParam.name
        Assert.assertEqual(anotherParam.type, param2.type)
        Assert.assertEqual(anotherParam.dimension, param2.dimension)
        Assert.assertEqual(anotherParam.unit, param2.unit)
        Assert.assertEqual(anotherParam.param_value, param2.param_value)

        # turn off the first script
        dc1.scripting_tool.enable = False
        Assert.assertEqual(False, param2.inherit_value)
        dc1.scripting_tool.enable = True
        Assert.assertEqual(True, param2.inherit_value)

        # disable first profile
        (clr.Convert(dc1, IProfile)).mode = PROFILE_MODE.NOT_ACTIVE
        Assert.assertEqual(False, param2.inherit_value)
        (clr.Convert(dc1, IProfile)).mode = PROFILE_MODE.ITERATE
        Assert.assertEqual(True, param2.inherit_value)

        # functional test...
        driver.main_sequence.remove_all()

        initState: "MissionControlSequenceInitialState" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "Initial_State", "-"),
            MissionControlSequenceInitialState,
        )
        initState.set_element_type(ELEMENT_TYPE.KEPLERIAN)
        elems: "ElementKeplerian" = clr.CastAs(initState.element, ElementKeplerian)
        elems.periapsis_altitude_size = 300
        elems.eccentricity = 0.01
        elems.inclination = 28.5
        elems.raan = 0
        elems.arg_of_periapsis = 0
        elems.true_anomaly = 0

        targSeq = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        man1: "MissionControlSequenceManeuver" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver1", "-"), MissionControlSequenceManeuver
        )
        prop1: "MissionControlSequencePropagate" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate1", "-"), MissionControlSequencePropagate
        )
        man2: "MissionControlSequenceManeuver" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver2", "-"), MissionControlSequenceManeuver
        )
        prop2: "MissionControlSequencePropagate" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate2", "-"), MissionControlSequencePropagate
        )

        (clr.Convert(man1, IMissionControlSequenceSegment)).results.add("Maneuver/Inertial_DeltaV_Magnitude")

        prop1.stopping_conditions.add("Periapsis")
        prop1.stopping_conditions.remove("Duration")
        prop1.propagator_name = "Earth Point Mass"

        (clr.Convert(man2, IMissionControlSequenceSegment)).results.add("Maneuver/Inertial_DeltaV_Magnitude")

        prop2.stopping_conditions.add("Apoapsis")
        prop2.stopping_conditions.remove("Duration")
        (clr.Convert(prop2, IMissionControlSequenceSegment)).results.add("Spherical Elems/R_Mag")

        targSeq.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        targSeq.profiles.remove_all()

        chngProp: "ProfileChangePropagator" = clr.CastAs(
            targSeq.profiles.add("Change Propagator"), ProfileChangePropagator
        )
        chngProp.name = "Change Propagator1 to 2B"
        chngProp.propagator_name = "Earth Point Mass"

        chngProp = clr.CastAs(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        chngProp.name = "Change Propagator2 to 2B"
        chngProp.propagator_name = "Earth Point Mass"

        diffCorr2b: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add("Differential Corrector"), ProfileDifferentialCorrector
        )
        diffCorr2b.name = "target 2B"
        scriptingTool2b: "ScriptingTool" = diffCorr2b.scripting_tool
        scriptingTool2b.enable = True
        deltav12b: "ScriptingSegment" = scriptingTool2b.segment_properties.add("DeltaV1")
        deltav12b.object_name = "Maneuver1"
        deltav12b.attribute = "ImpulsiveMnvr.Spherical.Magnitude"
        deltav12b.unit = "km/sec"
        deltav22b: "ScriptingSegment" = scriptingTool2b.segment_properties.add("DeltaV2")
        deltav22b.object_name = "Maneuver2"
        deltav22b.attribute = "ImpulsiveMnvr.Spherical.Magnitude"
        deltav22b.unit = "km/sec"
        deltaV2b: "ScriptingParameter" = scriptingTool2b.parameters.add("DeltaV")
        deltaV2b.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        deltaV2b.dimension = "Rate"
        deltaV2b.unit = "km/sec"
        deltaV2b.param_value = 0
        scriptingTool2b.script_text((("DeltaV1 = DeltaV;" + Environment.NewLine) + "DeltaV2 = DeltaV;"))
        control2b: "DifferentialCorrectorControl" = diffCorr2b.control_parameters.get_control_by_paths(
            "Scripting_Tool", "DeltaV"
        )
        control2b.enable = True
        control2b.perturbation = 0.0001
        control2b.max_step = 0.1
        result2b: "DifferentialCorrectorResult" = diffCorr2b.results.get_result_by_paths("Propagate2", "R_Mag")
        result2b.enable = True
        result2b.desired_value = 15000
        result2b.tolerance = 0.1

        chngProp = clr.CastAs(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        chngProp.name = "Change Propagator1 to full"
        chngProp.propagator_name = "Earth HPOP Default v8-1-1"

        chngProp = clr.CastAs(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        chngProp.name = "Change Propagator2 to full"
        chngProp.propagator_name = "Earth HPOP Default v8-1-1"

        diffCorrff: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add("Differential Corrector"), ProfileDifferentialCorrector
        )
        diffCorrff.name = "target full"
        scriptingToolff: "ScriptingTool" = diffCorrff.scripting_tool
        scriptingToolff.enable = True
        deltav1ff: "ScriptingSegment" = scriptingToolff.segment_properties.add("DeltaV1")
        deltav1ff.object_name = "Maneuver1"
        deltav1ff.attribute = "ImpulsiveMnvr.Spherical.Magnitude"
        deltav1ff.unit = "km/sec"
        deltav2ff: "ScriptingSegment" = scriptingToolff.segment_properties.add("DeltaV2")
        deltav2ff.object_name = "Maneuver2"
        deltav2ff.attribute = "ImpulsiveMnvr.Spherical.Magnitude"
        deltav2ff.unit = "km/sec"
        deltaVff: "ScriptingParameter" = scriptingToolff.parameters.add("DeltaV")
        deltaVff.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        deltaVff.dimension = "Rate"
        deltaVff.unit = "km/sec"
        deltaVff.param_value = 0
        deltaVff.inherit_value = True
        scriptingToolff.script_text((("DeltaV1 = DeltaV;" + Environment.NewLine) + "DeltaV2 = DeltaV;"))
        controlff: "DifferentialCorrectorControl" = diffCorrff.control_parameters.get_control_by_paths(
            "Scripting_Tool", "DeltaV"
        )
        controlff.enable = True
        controlff.perturbation = 0.0001
        controlff.max_step = 0.1
        resultff: "DifferentialCorrectorResult" = diffCorrff.results.get_result_by_paths("Propagate2", "R_Mag")
        resultff.enable = True
        resultff.desired_value = 15000
        resultff.tolerance = 0.1
        # endregion

        (clr.Convert(sat, IStkObject)).unload()

    # endregion

    # region BUG86787
    @category("ExcludeOnLinux")
    def test_BUG86787(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ScriptingToolParamsBUG"),
            Satellite,
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        driver.main_sequence.remove_all()

        initState: "MissionControlSequenceInitialState" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "Initial_State", "-"),
            MissionControlSequenceInitialState,
        )
        initState.set_element_type(ELEMENT_TYPE.KEPLERIAN)
        elems: "ElementKeplerian" = clr.CastAs(initState.element, ElementKeplerian)
        elems.periapsis_altitude_size = 300
        elems.eccentricity = 0.01
        elems.inclination = 28.5
        elems.raan = 0
        elems.arg_of_periapsis = 0
        elems.true_anomaly = 0

        targSeq: "MissionControlSequenceTargetSequence" = None  # I added
        targSeq = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        targSeq.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        targSeq.profiles.remove_all()

        man1: "MissionControlSequenceManeuver" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver1", "-"), MissionControlSequenceManeuver
        )
        prop1: "MissionControlSequencePropagate" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate1", "-"), MissionControlSequencePropagate
        )
        man2: "MissionControlSequenceManeuver" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver2", "-"), MissionControlSequenceManeuver
        )
        prop2: "MissionControlSequencePropagate" = clr.CastAs(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate2", "-"), MissionControlSequencePropagate
        )

        (clr.Convert(man1, IMissionControlSequenceSegment)).results.add("Maneuver/Inertial_DeltaV_Magnitude")

        prop1.stopping_conditions.add("Periapsis")
        prop1.stopping_conditions.remove("Duration")
        prop1.propagator_name = "Earth Point Mass"

        (clr.Convert(man2, IMissionControlSequenceSegment)).results.add("Maneuver/Inertial_DeltaV_Magnitude")

        prop2.stopping_conditions.add("Apoapsis")
        prop2.stopping_conditions.remove("Duration")
        (clr.Convert(prop2, IMissionControlSequenceSegment)).results.add("Spherical Elems/R_Mag")

        diffCorr2b: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add("Differential Corrector"), ProfileDifferentialCorrector
        )
        diffCorr2b.name = "target 2B"
        scriptingTool2b: "ScriptingTool" = diffCorr2b.scripting_tool
        scriptingTool2b.enable = True
        deltav12b: "ScriptingSegment" = scriptingTool2b.segment_properties.add("DeltaV1")
        deltav12b.object_name = "Maneuver1"
        deltav12b.attribute = "ImpulsiveMnvr.Spherical.Magnitude"
        deltav12b.unit = "km/sec"
        deltav22b: "ScriptingSegment" = scriptingTool2b.segment_properties.add("DeltaV2")
        deltav22b.object_name = "Maneuver2"
        deltav22b.attribute = "ImpulsiveMnvr.Spherical.Magnitude"
        deltav22b.unit = "km/sec"
        deltaV2b: "ScriptingParameter" = scriptingTool2b.parameters.add("DeltaV")
        deltaV2b.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        deltaV2b.dimension = "Rate"
        deltaV2b.unit = "km/sec"
        deltaV2b.param_value = 0
        scriptingTool2b.script_text((("DeltaV1 = DeltaV;" + Environment.NewLine) + "DeltaV2 = DeltaV;"))
        control2b: "DifferentialCorrectorControl" = diffCorr2b.control_parameters.get_control_by_paths(
            "Scripting_Tool", "DeltaV"
        )
        control2b.enable = True
        control2b.perturbation = 0.0001
        control2b.max_step = 0.1
        result2b: "DifferentialCorrectorResult" = diffCorr2b.results.get_result_by_paths("Propagate2", "R_Mag")
        result2b.enable = True
        result2b.desired_value = 15000
        result2b.tolerance = 0.1

        diffCorrff: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add("Differential Corrector"), ProfileDifferentialCorrector
        )
        diffCorrff.name = "target full"
        scriptingToolff: "ScriptingTool" = diffCorrff.scripting_tool
        scriptingToolff.enable = True
        deltav1ff: "ScriptingSegment" = scriptingToolff.segment_properties.add("DeltaV1")
        deltav1ff.object_name = "Maneuver1"
        deltav1ff.attribute = "ImpulsiveMnvr.Spherical.Magnitude"
        deltav1ff.unit = "km/sec"
        deltav2ff: "ScriptingSegment" = scriptingToolff.segment_properties.add("DeltaV2")
        deltav2ff.object_name = "Maneuver2"
        deltav2ff.attribute = "ImpulsiveMnvr.Spherical.Magnitude"
        deltav2ff.unit = "km/sec"
        deltaVff: "ScriptingParameter" = scriptingToolff.parameters.add("DeltaV")
        deltaVff.type = SCRIPTING_PARAMETER_TYPE.QUANTITY
        deltaVff.dimension = "Rate"
        deltaVff.unit = "km/sec"
        deltaVff.param_value = 0
        deltaVff.inherit_value = True
        scriptingToolff.script_text((("DeltaV1 = DeltaV;" + Environment.NewLine) + "DeltaV2 = DeltaV;"))
        controlff: "DifferentialCorrectorControl" = diffCorrff.control_parameters.get_control_by_paths(
            "Scripting_Tool", "DeltaV"
        )
        controlff.enable = True
        controlff.perturbation = 0.0001
        controlff.max_step = 0.1
        resultff: "DifferentialCorrectorResult" = diffCorrff.results.get_result_by_paths("Propagate2", "R_Mag")
        resultff.enable = True
        resultff.desired_value = 15000
        resultff.tolerance = 0.1

        (clr.Convert(sat, IStkObject)).unload()

    # endregion

    # region BUG108892
    def test_BUG108892(self):
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "BUG108892"), Satellite
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        maneuver: "MissionControlSequenceManeuver" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Maneuver1", "-"), MissionControlSequenceManeuver
        )
        maneuver.set_maneuver_type(MANEUVER_TYPE.FINITE)
        driver.run_mission_control_sequence()
        # Save the satellite here, and notice the "Begin OverrideTrajectory" section in the file.

        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        twoBody: "VehiclePropagatorTwoBody" = clr.CastAs(sat.propagator, VehiclePropagatorTwoBody)
        twoBody.propagate()
        # Save the satellite here, and notice that the "Begin OverrideTrajectory" section is NOT in the file.

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "BUG108892")

    # endregion

    # region CalculationGraphs

    def test_CalculationGraphs(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Calculation Graphs START")
        sat: "Satellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "CalculationGraphs"),
            Satellite,
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.Convert(sat.propagator, DriverMissionControlSequence)

        graphs: "CalculationGraphCollection" = driver.calculation_graphs
        graphs.add("Classical Orbit Elements")
        graphs.add("Inertial Position Velocity")
        Assert.assertTrue((graphs.count == 2))
        graphs.remove("Classical Orbit Elements")
        Assert.assertTrue((graphs.count == 1))

        def action136():
            badindex: str = graphs[1]

        TryCatchAssertBlock.DoAssert(action136)

        def action137():
            graphs.remove("Invalid")

        TryCatchAssertBlock.DoAssert(action137)
        graphs.remove_all()
        Assert.assertTrue((graphs.count == 0))

        def action138():
            graphs.add("Invalid")

        TryCatchAssertBlock.DoAssert(action138)
        graphs.add("Classical Orbit Elements")
        graphs.add("Inertial Position Velocity")
        interesting: str = graphs[0]
        graphs.remove(interesting)
        graphs.add("Classical Orbit Elements")
        graphs.add("Classical Orbit Elements")  # add dup

        # make a copy of the graphs to avoid modifying while iterating
        graphsToRemove = []
        graph: str
        for graph in graphs:
            graphsToRemove.append(graph)
        graph: str
        for graph in graphsToRemove:
            graphs.remove(graph)

        Assert.assertTrue((graphs.count == 0))
        (clr.Convert(sat, IStkObject)).unload()

    # endregion

    # region DPExecElements

    def test_DPExecElements(self):
        satellite: "Satellite" = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "TestSat"), Satellite
        )
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.Convert(satellite.propagator, DriverMissionControlSequence)

        driver.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Man1", "-")
        driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop2", "-")
        driver.main_sequence.insert(SEGMENT_TYPE.MANEUVER, "Man2", "-")
        driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop3", "-")

        driver.run_mission_control_sequence()

        timevar: "DataProviderTimeVarying" = (
            clr.Convert(satellite, IStkObject)
        ).data_providers.get_data_provider_time_varying_from_path("Astrogator Targeter Data")
        Assert.assertIsNotNone(timevar)  # Verify 58379

        interval: "DataProviderInterval" = (
            clr.Convert(satellite, IStkObject)
        ).data_providers.get_data_provider_interval_from_path("Maneuver Summary")
        elements = ["Maneuver Number", "Start Time"]

        result: "DataProviderResult" = interval.exec_elements(
            (clr.Convert(TestBase.Application.current_scenario, Scenario)).start_time,
            (clr.Convert(TestBase.Application.current_scenario, Scenario)).stop_time,
            elements,
        )

        dataSetcount1: int = result.intervals[0].data_sets.count
        Assert.assertEqual(2, dataSetcount1)

        interval2: "DataProviderInterval" = (
            clr.Convert(satellite, IStkObject)
        ).data_providers.get_data_provider_interval_from_path("Astrogator MCS Ephemeris Segments")
        elements2 = ["Segment Name", "Segment Type", "Start Time"]

        result2: "DataProviderResult" = interval2.exec_elements(
            (clr.Convert(TestBase.Application.current_scenario, Scenario)).start_time,
            (clr.Convert(TestBase.Application.current_scenario, Scenario)).stop_time,
            elements2,
        )

        dataSetcount2: int = result2.intervals[0].data_sets.count
        Assert.assertEqual(3, dataSetcount2)

        interval3: "DataProviderInterval" = (
            clr.Convert(satellite, IStkObject)
        ).data_providers.get_data_provider_interval_from_path("Astrogator MCS Ephemeris Segments")

        elements3 = []

        result3: "DataProviderResult" = interval3.exec_elements(
            (clr.Convert(TestBase.Application.current_scenario, Scenario)).start_time,
            (clr.Convert(TestBase.Application.current_scenario, Scenario)).stop_time,
            elements3,
        )

        dataSetcount3: int = result3.intervals[0].data_sets.count
        Assert.assertEqual(6, dataSetcount3)

        interval4: "DataProviderInterval" = (
            clr.Convert(satellite, IStkObject)
        ).data_providers.get_data_provider_interval_from_path("Astrogator MCS Ephemeris Segments")
        elements4 = ["Bogus"]

        def action139():
            result4: "DataProviderResult" = interval4.exec_elements(
                (clr.Convert(TestBase.Application.current_scenario, Scenario)).start_time,
                (clr.Convert(TestBase.Application.current_scenario, Scenario)).stop_time,
                elements4,
            )

        TryCatchAssertBlock.DoAssert(action139)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "TestSat")

    # endregion

    # region CompBrowsCutCopyPaste
    @category("NUNITTestFails")
    def test_CompBrowsCutCopyPaste(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - Calculation Graphs START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "CompBrowsCutCopyPaste"),
            Satellite,
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        prop1: "MissionControlSequencePropagate" = clr.CastAs(
            driver.main_sequence["Propagate"], MissionControlSequencePropagate
        )

        # StoppingConditionElement stopCondElemXXX = prop1.StoppingConditions.Add("UserSelect");
        # StoppingCondition stopCondXXX = (StoppingCondition)stopCondElemXXX.Properties;
        # stopCondXXX.PasteUserCalcObjectFromClipboard();

        # AsTriggerCondition cond1;
        prop2: "MissionControlSequencePropagate" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        # StoppingConditionCollection test

        apoElem: "StoppingConditionElement" = prop1.stopping_conditions.add("Apoapsis")
        apo: "StoppingCondition" = clr.CastAs(apoElem.properties, StoppingCondition)
        apo.central_body_name = "Moon"

        def action140():
            prop1.stopping_conditions.get_item_by_index(prop1.stopping_conditions.count)

        TryCatchAssertBlock.ExpectedException("Index Out of Range", action140)

        def action141():
            prop1.stopping_conditions.get_item_by_name("bogus")

        TryCatchAssertBlock.ExpectedException("Item specified by IndexOrName could not be found", action141)

        conditionA: "StoppingConditionElement" = prop1.stopping_conditions.get_item_by_index(0)
        conditionB: "StoppingConditionElement" = prop1.stopping_conditions.get_item_by_name("Apoapsis")
        Assert.assertIsNotNone(conditionA)
        Assert.assertIsNotNone(conditionB)

        def action142():
            prop2.stopping_conditions.paste()

        TryCatchAssertBlock.DoAssert(action142)

        apoElem2: "StoppingConditionElement" = prop2.stopping_conditions.insert_copy(apoElem)
        apo2: "StoppingCondition" = clr.CastAs(apoElem2.properties, StoppingCondition)
        Assert.assertEqual(2, prop2.stopping_conditions.count)
        Assert.assertEqual(apo.central_body_name, apo2.central_body_name)
        apoElem2 = prop2.stopping_conditions.insert_copy(apoElem)

        def action143():
            apoElem2 = prop2.stopping_conditions.insert_copy(None)

        TryCatchAssertBlock.DoAssert(action143)

        prop1.stopping_conditions.cut(1)
        prop2.stopping_conditions.paste()
        Assert.assertEqual(1, prop1.stopping_conditions.count)
        Assert.assertEqual(4, prop2.stopping_conditions.count)

        prop2.stopping_conditions.cut("Apoapsis")
        prop1.stopping_conditions.paste()
        Assert.assertEqual(2, prop1.stopping_conditions.count)
        Assert.assertEqual(3, prop2.stopping_conditions.count)

        def action144():
            prop1.stopping_conditions.cut(4)

        TryCatchAssertBlock.DoAssert(action144)

        def action145():
            prop2.stopping_conditions.cut("bogus")

        TryCatchAssertBlock.DoAssert(action145)

        # ConstraintCollection test

        apoElem: "StoppingConditionElement" = prop1.stopping_conditions["Apoapsis"]
        apo: "StoppingCondition" = clr.CastAs(apoElem.properties, StoppingCondition)

        cond1: "AsTriggerCondition" = apo.constraints.add("UserDefined")
        cond1.calc_object_name = "Cartesian Elems/X"
        Assert.assertEqual(1, apo.constraints.count)

        def action146():
            apo.constraints.paste()

        TryCatchAssertBlock.DoAssert(action146)

        # test copy within stopping condition
        cond2: "AsTriggerCondition" = apo.constraints.insert_copy(cond1)
        Assert.assertEqual(2, apo.constraints.count)
        Assert.assertEqual("X", apo.constraints[1].calc_object.name)

        # test copy to another stopping condition
        apoElem2a: "StoppingConditionElement" = prop2.stopping_conditions["Apoapsis1"]
        comp: "IStoppingConditionComponent" = apoElem2a.properties
        apo2: "StoppingCondition" = clr.CastAs(comp, StoppingCondition)
        condAnotherStopCond: "AsTriggerCondition" = apo2.constraints.insert_copy(cond1)
        Assert.assertEqual(1, apo2.constraints.count)
        Assert.assertEqual("X", apo2.constraints[0].calc_object_name)

        apo.constraints.cut(1)
        apo2.constraints.paste()
        Assert.assertEqual(1, apo.constraints.count)
        Assert.assertEqual(2, apo2.constraints.count)

        apo2.constraints.cut("UserDefined1")
        apo.constraints.paste()
        Assert.assertEqual(2, apo.constraints.count)
        Assert.assertEqual(1, apo2.constraints.count)

        def action147():
            apo.constraints.cut(4)

        TryCatchAssertBlock.DoAssert(action147)

        def action148():
            apo2.constraints.cut("bogus")

        TryCatchAssertBlock.DoAssert(action148)

        # ProfileCollection test

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles["Differential_Corrector"], ProfileDifferentialCorrector
        )
        (clr.Convert(diffCorr, IProfile)).mode = PROFILE_MODE.NOT_ACTIVE

        def action149():
            targSeq.profiles.paste(0, PROFILE_INSERT_DIRECTION.AFTER)

        TryCatchAssertBlock.DoAssert(action149)

        def action150():
            targSeq.profiles.cut("bogus")

        TryCatchAssertBlock.DoAssert(action150)

        def action151():
            targSeq.profiles.cut(3)

        TryCatchAssertBlock.DoAssert(action151)

        targSeq.profiles.cut("Differential Corrector")
        Assert.assertEqual(0, targSeq.profiles.count)

        def action152():
            targSeq.profiles.paste("Differential Corrector", PROFILE_INSERT_DIRECTION.BEFORE)

        TryCatchAssertBlock.DoAssert(action152)

        def action153():
            targSeq.profiles.paste(5, PROFILE_INSERT_DIRECTION.BEFORE)

        TryCatchAssertBlock.DoAssert(action153)

        targSeq.profiles.add("Scripting Tool")
        targSeq.profiles.paste(0, PROFILE_INSERT_DIRECTION.AFTER)
        Assert.assertEqual(2, targSeq.profiles.count)
        Assert.assertEqual("Differential Corrector", targSeq.profiles[1].name)
        targSeq.profiles.paste(1, PROFILE_INSERT_DIRECTION.AFTER)
        targSeq.profiles.paste(2, PROFILE_INSERT_DIRECTION.AFTER)
        Assert.assertEqual(4, targSeq.profiles.count)
        targSeq.profiles.remove_all()

        def action154():
            targSeq.profiles.get_item_by_index(targSeq.profiles.count)

        TryCatchAssertBlock.ExpectedException("Index Out of Range", action154)

        def action155():
            targSeq.profiles.get_item_by_name("bogus")

        TryCatchAssertBlock.ExpectedException("Item specified by IndexOrName could not be found", action155)

        targSeq.profiles.add("Scripting Tool")
        profile: "IProfile" = targSeq.profiles.get_item_by_index(0)
        profileA: "IProfile" = targSeq.profiles.get_item_by_name("Scripting Tool")
        Assert.assertIsNotNone(profile)
        Assert.assertIsNotNone(profileA)
        Assert.assertEqual(
            profile.name, profileA.name, "GetItemByName and GetItemByIndex should return the same IProfile"
        )
        targSeq.profiles.remove("Scripting Tool")

        targSeq.profiles.add("Differential Corrector")
        targSeq.profiles.add("Scripting Tool")
        targSeq.profiles.cut(0)

        targSeq.profiles.paste("Scripting Tool", PROFILE_INSERT_DIRECTION.AFTER)
        Assert.assertEqual("Differential Corrector", targSeq.profiles[1].name)
        targSeq.profiles.remove(1)

        targSeq.profiles.paste("Scripting Tool", PROFILE_INSERT_DIRECTION.BEFORE)
        Assert.assertEqual("Differential Corrector", targSeq.profiles[0].name)
        targSeq.profiles.remove(0)

        targSeq.profiles.paste(0, PROFILE_INSERT_DIRECTION.AFTER)
        Assert.assertEqual("Differential Corrector", targSeq.profiles[1].name)
        targSeq.profiles.remove(1)

        targSeq.profiles.paste(0, PROFILE_INSERT_DIRECTION.BEFORE)
        Assert.assertEqual("Differential Corrector", targSeq.profiles[0].name)
        targSeq.profiles.remove(0)

        targSeq.profiles.remove("Scripting Tool")

        # Add2 before 0th guy
        dc: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE),
            ProfileDifferentialCorrector,
        )
        Assert.assertEqual(1, targSeq.profiles.count)
        targSeq.profiles.remove_all()

        # Add2 after 0th guy
        dc2: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.AFTER),
            ProfileDifferentialCorrector,
        )
        Assert.assertEqual(1, targSeq.profiles.count)

        # Add2 before 1st guy, should be new first profile
        dc3: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE),
            ProfileDifferentialCorrector,
        )
        dc3.name = "NewFirstProfile"
        Assert.assertEqual("NewFirstProfile", targSeq.profiles[0].name)

        # Add2 after 1st guy, should be second profile
        dc4: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.AFTER),
            ProfileDifferentialCorrector,
        )
        dc4.name = "NewSecondProfile"
        Assert.assertEqual("NewSecondProfile", targSeq.profiles[1].name)

        # Add2 after second guy, should be third profile
        dc5: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 1, PROFILE_INSERT_DIRECTION.AFTER),
            ProfileDifferentialCorrector,
        )
        dc5.name = "NewThirdProfile"
        Assert.assertEqual("NewThirdProfile", targSeq.profiles[2].name)
        Assert.assertEqual(4, targSeq.profiles.count)

        def action156():
            dc6: "IProfile" = targSeq.profiles.add2("Differential Corrector", 5, PROFILE_INSERT_DIRECTION.AFTER)

        # what happens if I Add2 after a nonexistent index
        TryCatchAssertBlock.DoAssert(action156)

        # what happens if I Add2 after the last index?
        dc7: "IProfile" = targSeq.profiles.add2("Differential Corrector", 3, PROFILE_INSERT_DIRECTION.AFTER)
        dc7.name = "LastProfile"
        Assert.assertEqual("LastProfile", targSeq.profiles[4].name)
        Assert.assertEqual(5, targSeq.profiles.count)

        # Add2 before last index?
        dc8: "IProfile" = targSeq.profiles.add2("Differential Corrector", 4, PROFILE_INSERT_DIRECTION.BEFORE)
        dc8.name = "SecondToLastProfile"
        Assert.assertEqual("SecondToLastProfile", targSeq.profiles[4].name)
        Assert.assertEqual(6, targSeq.profiles.count)

        targSeq.profiles.remove_all()
        targSeq.profiles.add("Scripting Tool")
        targSeq.profiles.add("Differential Corrector")
        profile0: "IProfile" = targSeq.profiles["Scripting Tool"]
        profile1: "IProfile" = targSeq.profiles["Differential Corrector"]

        targSeq.profiles.insert_copy(profile0, 0, PROFILE_INSERT_DIRECTION.BEFORE)
        Assert.assertEqual(3, targSeq.profiles.count)
        Assert.assertEqual(targSeq.profiles[0].name, "Scripting Tool1")

        targSeq.profiles.insert_copy(profile0, 0, PROFILE_INSERT_DIRECTION.AFTER)
        Assert.assertEqual(4, targSeq.profiles.count)
        Assert.assertEqual(targSeq.profiles[1].name, "Scripting Tool2")

        targSeq.profiles.insert_copy(profile1, 3, PROFILE_INSERT_DIRECTION.BEFORE)
        Assert.assertEqual(5, targSeq.profiles.count)
        Assert.assertEqual(targSeq.profiles[3].name, "Differential Corrector1")

        targSeq.profiles.insert_copy(profile1, 3, PROFILE_INSERT_DIRECTION.AFTER)
        Assert.assertEqual(6, targSeq.profiles.count)
        Assert.assertEqual(targSeq.profiles[4].name, "Differential Corrector2")

        targSeq.profiles.insert_copy(profile0, 6, PROFILE_INSERT_DIRECTION.AFTER)
        Assert.assertEqual(7, targSeq.profiles.count)
        Assert.assertEqual(targSeq.profiles[6].name, "Scripting Tool3")

        def action157():
            targSeq.profiles.insert_copy(profile0, "bogus", PROFILE_INSERT_DIRECTION.AFTER)

        TryCatchAssertBlock.DoAssert(action157)

        def action158():
            targSeq.profiles.insert_copy(profile0, 8, PROFILE_INSERT_DIRECTION.AFTER)

        TryCatchAssertBlock.DoAssert(action158)

        # ThrusterSetCollection test

        astComps: "ComponentInfoCollection" = (
            clr.Convert(TestBase.Application.current_scenario, Scenario)
        ).component_directory.get_components(COMPONENT.ASTROGATOR)
        thrusterSets: "ComponentInfoCollection" = astComps.get_folder("Thruster Sets")
        newThrusterSet: "ThrusterSet" = clr.CastAs(
            (clr.Convert(thrusterSets["Thruster Set"], ICloneable)).clone_object(), ThrusterSet
        )
        thrusterSetColl: "ThrusterSetCollection" = newThrusterSet.thrusters
        thrusterSetColl.remove_all()

        def action159():
            thrusterSetColl.paste()

        TryCatchAssertBlock.DoAssert(action159)

        thrusterSetColl.add("Thruster1")
        thrusterSetColl.add("Thruster2")
        thrusterSetColl.add("Thruster3")

        x: "Thruster" = thrusterSetColl["Thruster1"]
        y: "Thruster" = thrusterSetColl.get_item_by_index(0)
        z: "Thruster" = thrusterSetColl.get_item_by_name("Thruster1")
        Assert.assertEqual(x.name, y.name)
        Assert.assertEqual(x.name, z.name)

        thrusterSetColl.cut("Thruster2")
        Assert.assertEqual(2, thrusterSetColl.count)
        thrusterSetColl.cut(0)
        Assert.assertEqual(1, thrusterSetColl.count)

        def action160():
            thrusterSetColl.cut("NonExistent Thruster")

        # and now, try to remove guys that aren't there

        TryCatchAssertBlock.DoAssert(action160)

        def action161():
            thrusterSetColl.cut(1)

        TryCatchAssertBlock.DoAssert(action161)

        newThruster: "Thruster" = thrusterSetColl.paste()
        Assert.assertEqual(2, thrusterSetColl.count)
        Assert.assertEqual("Thruster1", newThruster.name)

        newThruster.thruster_efficiency = 0.5
        anotherNewThruster: "Thruster" = thrusterSetColl.insert_copy(newThruster)
        Assert.assertEqual(3, thrusterSetColl.count)
        Assert.assertEqual(0.5, anotherNewThruster.thruster_efficiency)

        def action162():
            thrusterSetColl.insert_copy(None)

        TryCatchAssertBlock.DoAssert(action162)

        # PropagatorFunctionCollection test

        astComps: "ComponentInfoCollection" = (
            clr.Convert(TestBase.Application.current_scenario, Scenario)
        ).component_directory.get_components(COMPONENT.ASTROGATOR)
        propagators: "ComponentInfoCollection" = astComps.get_folder("Propagators")
        newPropagator: "NumericalPropagatorWrapper" = clr.CastAs(
            (clr.Convert(propagators["Earth J2"], ICloneable)).clone_object(), NumericalPropagatorWrapper
        )

        propFuncColl: "PropagatorFunctionCollection" = newPropagator.propagator_functions

        def action163():
            propFuncColl.paste()

        TryCatchAssertBlock.DoAssert(action163)

        def action164():
            propFuncColl.cut("bogus")

        TryCatchAssertBlock.DoAssert(action164)

        def action165():
            propFuncColl.cut(3)

        TryCatchAssertBlock.DoAssert(action165)

        ci0: "IComponentInfo" = propFuncColl["WGS84"]
        ci1: "IComponentInfo" = propFuncColl.get_item_by_index(0)
        ci2: "IComponentInfo" = propFuncColl.get_item_by_name("WGS84")
        Assert.assertEqual(ci0.name, ci1.name)
        Assert.assertEqual(ci0.name, ci2.name)

        gravField: "GravityFieldFunction" = clr.CastAs(propFuncColl["WGS84"], GravityFieldFunction)
        gravField.degree = 16
        gravField.order = 16
        propFuncColl.cut("WGS84")
        sameGravField: "GravityFieldFunction" = clr.CastAs(propFuncColl.paste(), GravityFieldFunction)
        Assert.assertEqual(16, sameGravField.degree)
        Assert.assertEqual(1, propFuncColl.count)

        def action166():
            propFuncColl.cut("NonExistent Prop Func")

        TryCatchAssertBlock.DoAssert(action166)

        def action167():
            propFuncColl.cut(99)

        TryCatchAssertBlock.DoAssert(action167)

        anotherNewPropagator: "NumericalPropagatorWrapper" = clr.CastAs(
            (clr.Convert(propagators["Earth J2"], ICloneable)).clone_object(), NumericalPropagatorWrapper
        )
        propFuncColl2: "PropagatorFunctionCollection" = anotherNewPropagator.propagator_functions

        def action168():
            propFuncColl2.paste()

        TryCatchAssertBlock.DoAssert(action168)
        propFuncColl2.remove(0)
        Assert.assertEqual(0, propFuncColl2.count)

        def action169():
            propFuncColl.paste()

        TryCatchAssertBlock.DoAssert(action169)

        anotherFunc: "GravityFieldFunction" = clr.CastAs(propFuncColl2.paste(), GravityFieldFunction)
        Assert.assertEqual(16, anotherFunc.degree)
        Assert.assertEqual(1, propFuncColl2.count)
        propFuncColl2.remove_all()

        lastFunc: "GravityFieldFunction" = clr.CastAs(
            propFuncColl2.insert_copy(clr.Convert(anotherFunc, IComponentInfo)), GravityFieldFunction
        )
        Assert.assertEqual(16, lastFunc.degree)

        def action170():
            propFuncColl2.insert_copy(None)

        TryCatchAssertBlock.DoAssert(action170)

        # CalcObjectCollection test

        initState: "IMissionControlSequenceSegment" = driver.main_sequence["Initial State"]
        calcObjColl: "CalcObjectCollection" = initState.results

        def action171():
            calcObjColl.paste()

        TryCatchAssertBlock.DoAssert(action171)

        def action172():
            calcObjColl.cut("bogus")

        TryCatchAssertBlock.DoAssert(action172)

        def action173():
            calcObjColl.cut(3)

        TryCatchAssertBlock.DoAssert(action173)

        alt: "StateCalcGeodeticElem" = clr.CastAs(calcObjColl.add("Geodetic/Altitude"), StateCalcGeodeticElem)
        alt.central_body_name = "Mars"
        calcObjColl.cut("Altitude")
        pasted: "StateCalcGeodeticElem" = clr.CastAs(calcObjColl.paste(), StateCalcGeodeticElem)
        Assert.assertEqual("Mars", pasted.central_body_name)

        calcObjColl.cut(0)
        pasted2: "StateCalcGeodeticElem" = clr.CastAs(calcObjColl.paste(), StateCalcGeodeticElem)
        Assert.assertEqual("Mars", pasted2.central_body_name)

        prop: "IMissionControlSequenceSegment" = driver.main_sequence["Propagate"]
        pasted = clr.CastAs(prop.results.paste(), StateCalcGeodeticElem)
        Assert.assertEqual("Mars", pasted.central_body_name)

        prop.results.remove(0)
        Assert.assertEqual(0, prop.results.count)

        def action174():
            calcObjColl.insert_copy(None)

        TryCatchAssertBlock.DoAssert(action174)

        pasted = clr.CastAs(prop.results.insert_copy(clr.Convert(alt, IComponentInfo)), StateCalcGeodeticElem)
        Assert.assertEqual("Mars", pasted.central_body_name)

        # TargeterGraphCollection test

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence2", "-"),
            MissionControlSequenceTargetSequence,
        )
        dc8: "IProfile" = targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE)
        diffCorr: "ProfileDifferentialCorrector" = clr.Convert(dc8, ProfileDifferentialCorrector)
        targGraphColl: "TargeterGraphCollection" = diffCorr.targeter_graphs

        def action175():
            targGraphColl.paste()

        TryCatchAssertBlock.DoAssert(action175)

        def action176():
            targGraphColl.cut("bogus")

        TryCatchAssertBlock.DoAssert(action176)

        def action177():
            targGraphColl.cut(3)

        TryCatchAssertBlock.DoAssert(action177)

        def action178():
            targGraphColl.get_item_by_index(targGraphColl.count)

        TryCatchAssertBlock.ExpectedException("Index Out of Range", action178)

        def action179():
            targGraphColl.get_item_by_name("bogus")

        TryCatchAssertBlock.ExpectedException("Item specified by IndexOrName could not be found", action179)

        targGraphColl.remove_graph(0)
        graph: "TargeterGraph" = targGraphColl.add_graph()
        graph.name = "NewGraph"
        targGraphColl.cut("NewGraph")
        Assert.assertEqual(0, targGraphColl.count)

        pastedGraph: "TargeterGraph" = targGraphColl.paste()
        Assert.assertEqual(1, targGraphColl.count)
        Assert.assertEqual("NewGraph", pastedGraph.name)

        graphA: "TargeterGraph" = targGraphColl.get_item_by_index(0)
        graphB: "TargeterGraph" = targGraphColl.get_item_by_name("NewGraph")
        Assert.assertIsNotNone(graphA)
        Assert.assertIsNotNone(graphB)
        Assert.assertEqual(
            graphA.name, graphB.name, "GetItemByName and GetItemByIndex should return the same TargeterGraph"
        )

        targGraphColl.cut(0)
        Assert.assertEqual(0, targGraphColl.count)

        pastedGraph2: "TargeterGraph" = targGraphColl.paste()
        Assert.assertEqual(1, targGraphColl.count)
        Assert.assertEqual("NewGraph", pastedGraph2.name)

        def action180():
            targGraphColl.insert_copy(None)

        TryCatchAssertBlock.DoAssert(action180)

        newPastedGraph: "TargeterGraph" = targGraphColl.insert_copy(pastedGraph)
        Assert.assertEqual("NewGraph1", newPastedGraph.name)
        Assert.assertEqual(2, targGraphColl.count)

        # ScriptingSegmentCollection test

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence3", "-"),
            MissionControlSequenceTargetSequence,
        )
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE),
            ProfileDifferentialCorrector,
        )
        scriptTool: "ProfileScriptingTool" = clr.CastAs(targSeq.profiles.add("Scripting Tool"), ProfileScriptingTool)
        ssColl: "ScriptingSegmentCollection" = scriptTool.segment_properties

        def action181():
            ssColl.paste()

        TryCatchAssertBlock.DoAssert(action181)

        def action182():
            ssColl.cut("bogus")

        TryCatchAssertBlock.DoAssert(action182)

        def action183():
            ssColl.cut(3)

        TryCatchAssertBlock.DoAssert(action183)

        def action184():
            ssColl.get_item_by_index(ssColl.count)

        TryCatchAssertBlock.ExpectedException("Index Out of Range", action184)

        def action185():
            ssColl.get_item_by_name("bogus")

        TryCatchAssertBlock.ExpectedException("Item specified by IndexOrName could not be found", action185)

        ssColl.add("TestProperty")
        scriptingSegment: "ScriptingSegment" = ssColl.get_item_by_index(0)
        scriptingSegmentA: "ScriptingSegment" = ssColl.get_item_by_name("TestProperty")
        Assert.assertIsNotNone(scriptingSegment)
        Assert.assertIsNotNone(scriptingSegmentA)
        Assert.assertEqual(
            scriptingSegment.object_name,
            scriptingSegmentA.object_name,
            "GetItemByName and GetItemByIndex should return the same ScriptingSegment",
        )
        ssColl.remove("TestProperty")

        objProp: "ScriptingSegment" = ssColl.add("ObjectProperty")
        objProp2: "ScriptingSegment" = ssColl.insert_copy(objProp)
        Assert.assertEqual("ObjectProperty1", objProp2.component_name)
        Assert.assertEqual(2, ssColl.count)

        def action186():
            ssColl.insert_copy(None)

        TryCatchAssertBlock.DoAssert(action186)

        ssColl.cut(objProp2.component_name)
        Assert.assertEqual(1, ssColl.count)
        diffCorr = clr.CastAs(targSeq.profiles.add("Differential Corrector"), ProfileDifferentialCorrector)
        diffCorr.scripting_tool.enable = True
        newObjProp: "ScriptingSegment" = diffCorr.scripting_tool.segment_properties.paste()
        Assert.assertEqual("ObjectProperty2", newObjProp.component_name)

        ssColl.cut(0)
        Assert.assertEqual(0, ssColl.count)
        diffCorr = clr.CastAs(targSeq.profiles.add("Differential Corrector"), ProfileDifferentialCorrector)
        diffCorr.scripting_tool.enable = True
        newObjProp2: "ScriptingSegment" = diffCorr.scripting_tool.segment_properties.paste()
        Assert.assertEqual("ObjectProperty1", newObjProp2.component_name)

        # ScriptingCalcObjectCollection test

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence4", "-"),
            MissionControlSequenceTargetSequence,
        )
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE),
            ProfileDifferentialCorrector,
        )
        scriptTool: "ProfileScriptingTool" = clr.CastAs(targSeq.profiles.add("Scripting Tool"), ProfileScriptingTool)
        coColl: "ScriptingCalcObjectCollection" = scriptTool.calc_objects

        def action187():
            coColl.paste()

        TryCatchAssertBlock.DoAssert(action187)

        def action188():
            coColl.cut("bogus")

        TryCatchAssertBlock.DoAssert(action188)

        def action189():
            coColl.cut(3)

        TryCatchAssertBlock.DoAssert(action189)

        calcObj: "ScriptingCalcObject" = coColl.add("NewCalcObj")
        calcObj2: "ScriptingCalcObject" = coColl.insert_copy(calcObj)
        Assert.assertEqual("NewCalcObj1", calcObj2.component_name)

        def action190():
            coColl.insert_copy(None)

        TryCatchAssertBlock.DoAssert(action190)

        scriptTool.calc_objects.cut("NewCalcObj1")
        Assert.assertEqual(1, coColl.count)

        scriptTool.enable = False

        def action191():
            scriptTool.calc_objects.paste()

        TryCatchAssertBlock.DoAssert(action191)

        scriptTool.enable = True
        newCalcObj: "ScriptingCalcObject" = scriptTool.calc_objects.paste()
        Assert.assertEqual("NewCalcObj2", newCalcObj.component_name)
        Assert.assertEqual(2, scriptTool.calc_objects.count)

        scriptTool.calc_objects.cut(0)
        Assert.assertEqual(1, coColl.count)
        newCalcObj2: "ScriptingCalcObject" = scriptTool.calc_objects.paste()
        Assert.assertEqual("NewCalcObj1", newCalcObj2.component_name)
        Assert.assertEqual(2, scriptTool.calc_objects.count)

        # ScriptingParameterCollection test

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence5", "-"),
            MissionControlSequenceTargetSequence,
        )
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE),
            ProfileDifferentialCorrector,
        )
        scriptTool: "ProfileScriptingTool" = clr.CastAs(targSeq.profiles.add("Scripting Tool"), ProfileScriptingTool)
        paramColl: "ScriptingParameterCollection" = scriptTool.parameters

        def action192():
            paramColl.paste()

        TryCatchAssertBlock.DoAssert(action192)

        def action193():
            paramColl.cut("bogus")

        TryCatchAssertBlock.DoAssert(action193)

        def action194():
            paramColl.cut(3)

        TryCatchAssertBlock.DoAssert(action194)

        def action195():
            paramColl.get_item_by_index(paramColl.count)

        TryCatchAssertBlock.ExpectedException("Index Out of Range", action195)

        def action196():
            paramColl.get_item_by_name("bogus")

        TryCatchAssertBlock.ExpectedException("Item specified by IndexOrName could not be found", action196)

        paramColl.add("TestParam")
        paramA: "ScriptingParameter" = paramColl.get_item_by_index(0)
        paramB: "ScriptingParameter" = paramColl.get_item_by_name("TestParam")
        Assert.assertIsNotNone(paramA)
        Assert.assertIsNotNone(paramB)
        Assert.assertEqual(
            paramA.name, paramB.name, "GetItemByName and GetItemByIndex should return the same ScriptingParameter"
        )
        paramColl.remove("TestParam")

        param: "ScriptingParameter" = scriptTool.parameters.add("NewParam")
        param2: "ScriptingParameter" = scriptTool.parameters.insert_copy(param)
        Assert.assertEqual("NewParam1", param2.name)

        def action197():
            paramColl.insert_copy(None)

        TryCatchAssertBlock.DoAssert(action197)

        paramColl.cut("NewParam1")
        Assert.assertEqual(1, paramColl.count)

        scriptTool.enable = False

        def action198():
            scriptTool.parameters.paste()

        TryCatchAssertBlock.DoAssert(action198)

        scriptTool.enable = True
        newParam: "ScriptingParameter" = scriptTool.parameters.paste()
        Assert.assertEqual("NewParam2", newParam.name)
        Assert.assertEqual(2, scriptTool.parameters.count)

        paramColl.cut(0)
        Assert.assertEqual(1, paramColl.count)
        newParam2: "ScriptingParameter" = scriptTool.parameters.paste()
        Assert.assertEqual("NewParam1", newParam2.name)
        Assert.assertEqual(2, scriptTool.parameters.count)

        # ProfileScriptingTool - CopyToClipboard and PasteFromClipboard

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence6", "-"),
            MissionControlSequenceTargetSequence,
        )
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE),
            ProfileDifferentialCorrector,
        )
        psTool: "ProfileScriptingTool" = clr.CastAs(targSeq.profiles.add("Scripting Tool"), ProfileScriptingTool)

        # psTool.Parameters.RemoveAll();
        param: "ScriptingParameter" = psTool.parameters.add("TestParameterWoot")
        psTool.copy_to_clipboard()
        param.name = "ChangedName"
        psTool.paste_from_clipboard()
        Assert.assertEqual("TestParameterWoot", psTool.parameters[0].name)

        def action199():
            psTool.calc_objects.paste()

        TryCatchAssertBlock.DoAssert(action199)

        def action200():
            psTool.segment_properties.paste()

        TryCatchAssertBlock.DoAssert(action200)
        calcObj: "ScriptingCalcObject" = psTool.calc_objects.add("NewCalcObj")
        psTool.calc_objects.cut(0)

        def action201():
            psTool.parameters.paste()

        TryCatchAssertBlock.DoAssert(action201)

        def action202():
            psTool.paste_from_clipboard()

        TryCatchAssertBlock.DoAssert(action202)

        def action203():
            psTool.paste_from_clipboard()

        TryCatchAssertBlock.DoAssert(action203)

        # ScriptingTool - CopyToClipboard and PasteFromClipboard

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence7", "-"),
            MissionControlSequenceTargetSequence,
        )
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE),
            ProfileDifferentialCorrector,
        )

        scriptTool: "ScriptingTool" = diffCorr.scripting_tool
        scriptTool.parameters.remove_all()
        scriptTool.enable = True
        param: "ScriptingParameter" = scriptTool.parameters.add("TestParameterWoot")
        scriptTool.copy_to_clipboard()
        param.name = "ChangedName"
        scriptTool.paste_from_clipboard()
        Assert.assertEqual("TestParameterWoot", scriptTool.parameters[0].name)

        def action204():
            scriptTool.calc_objects.paste()

        TryCatchAssertBlock.DoAssert(action204)

        def action205():
            scriptTool.segment_properties.paste()

        TryCatchAssertBlock.DoAssert(action205)
        calcObj: "ScriptingCalcObject" = scriptTool.calc_objects.add("NewCalcObj")
        scriptTool.calc_objects.cut(0)

        def action206():
            scriptTool.parameters.paste()

        TryCatchAssertBlock.DoAssert(action206)

        def action207():
            scriptTool.paste_from_clipboard()

        TryCatchAssertBlock.DoAssert(action207)

        def action208():
            scriptTool.paste_from_clipboard()

        TryCatchAssertBlock.DoAssert(action208)

        # test copying calc objects in UserSelect stopping conditions, stopping condition constraints, calc object wrappers
        apoElem: "StoppingConditionElement" = prop1.stopping_conditions["Apoapsis"]
        apo: "StoppingCondition" = clr.CastAs(apoElem.properties, StoppingCondition)
        cond1: "AsTriggerCondition" = apo.constraints.add("UserDefined")

        targSeq: "MissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target_Sequence8", "-"),
            MissionControlSequenceTargetSequence,
        )
        diffCorr: "ProfileDifferentialCorrector" = clr.CastAs(
            targSeq.profiles.add2("Differential Corrector", 0, PROFILE_INSERT_DIRECTION.BEFORE),
            ProfileDifferentialCorrector,
        )
        scriptTool: "ScriptingTool" = diffCorr.scripting_tool
        scriptTool.enable = True
        newCalcObj: "ScriptingCalcObject" = scriptTool.calc_objects.add("NewCalcObj")

        stopCondElem: "StoppingConditionElement" = prop1.stopping_conditions.add("UserSelect")
        stopCond: "StoppingCondition" = clr.Convert(stopCondElem.properties, StoppingCondition)

        def action209():
            stopCond.paste_user_calc_object_from_clipboard()

        TryCatchAssertBlock.DoAssert(action209)

        def action210():
            cond1.paste_calc_object_from_clipboard()

        TryCatchAssertBlock.DoAssert(action210)

        def action211():
            newCalcObj.paste_calc_object_from_clipboard()

        TryCatchAssertBlock.DoAssert(action211)

        # user select stopping condition
        stopCond.user_calc_object_name = "Cartesian Elems/X"
        cartX: "IComponentInfo" = stopCond.user_calc_object
        stopCond.user_calc_object_name = "Cartesian Elems/Y"
        stopCond.user_calc_object = cartX
        Assert.assertEqual("X", stopCond.user_calc_object.name)

        newCalcObj.calc_object = cartX
        Assert.assertEqual("X", newCalcObj.calc_object.name)
        cond1.calc_object_name = "Cartesian Elems/Y"
        cond1.calc_object = cartX
        Assert.assertEqual("X", cond1.calc_object.name)

        cartX.name = "NewName"
        Assert.assertEqual("X", stopCond.user_calc_object.name)
        Assert.assertEqual("X", newCalcObj.calc_object.name)
        Assert.assertEqual("X", cond1.calc_object.name)

        # test that these things can be pasted on top of existing calc objects from the clipboard, including adding a copied
        # calc object to the results list.

        stopCond.user_calc_object.name = "ClipboardInstance"

        stopCond.copy_user_calc_object_to_clipboard()
        stopCond.paste_user_calc_object_from_clipboard()
        Assert.assertEqual("ClipboardInstance", stopCond.user_calc_object.name)
        newCalcObj.paste_calc_object_from_clipboard()
        Assert.assertEqual("ClipboardInstance", newCalcObj.calc_object.name)
        cond1.paste_calc_object_from_clipboard()
        Assert.assertEqual("ClipboardInstance", cond1.calc_object.name)

        newCalcObj.calc_object.name = "NewClipboardInstance"
        newCalcObj.copy_calc_object_to_clipboard()
        stopCond.paste_user_calc_object_from_clipboard()
        Assert.assertEqual("NewClipboardInstance", stopCond.user_calc_object.name)

        cond1.calc_object.name = "ThirdClipboardInstance"
        cond1.copy_calc_object_to_clipboard()
        stopCond.paste_user_calc_object_from_clipboard()
        Assert.assertEqual("ThirdClipboardInstance", stopCond.user_calc_object.name)

        # paste a clipboard calc object as a result
        fromClipboard: "IComponentInfo" = (clr.Convert(prop1, IMissionControlSequenceSegment)).results.paste()
        Assert.assertEqual("ThirdClipboardInstance", fromClipboard.name)

        # AstrogatorCentralBody - Cut, Copy, Paste

        # Gravity Model
        astComps: "ComponentInfoCollection" = (
            clr.Convert(TestBase.Application.current_scenario, Scenario)
        ).component_directory.get_components(COMPONENT.ASTROGATOR)
        cbs: "ComponentInfoCollection" = astComps.get_folder("Central Bodies")
        cb: "AstrogatorCentralBody" = clr.CastAs(
            (clr.Convert(cbs["Charon"], ICloneable)).clone_object(), AstrogatorCentralBody
        )
        model: "CentralBodyGravityModel" = cb.add_gravity_model(CENTRAL_BODY_GRAVITY_MODEL.EARTH_SIMPLE, "NewGrav")
        model.gravitational_param = 1337

        def action212():
            cb.paste_gravity_model()

        TryCatchAssertBlock.DoAssert(action212)

        def action213():
            cb.cut_gravity_model_by_name("bogus")

        TryCatchAssertBlock.DoAssert(action213)

        def action214():
            cb.add_copy_of_gravity_model(None)

        TryCatchAssertBlock.DoAssert(action214)

        # cut
        cb.cut_gravity_model_by_name("NewGrav")
        pastedGrav: "CentralBodyGravityModel" = cb.paste_gravity_model()
        Assert.assertEqual(1337, pastedGrav.gravitational_param)

        # copy
        cb.copy_gravity_model_by_name("NewGrav")
        clipGravity: "CentralBodyGravityModel" = cb.paste_gravity_model()
        Assert.assertEqual(1337, clipGravity.gravitational_param)

        # paste same name...
        pastedGrav = cb.paste_gravity_model()

        # insert copy
        copiedGrav: "CentralBodyGravityModel" = cb.add_copy_of_gravity_model(pastedGrav)
        Assert.assertEqual(1337, copiedGrav.gravitational_param)

        # make sure there's a new instance
        copiedGrav.gravitational_param = 1336
        Assert.assertEqual(1337, pastedGrav.gravitational_param)

        def action215():
            cb.paste_shape()

        # Shape
        TryCatchAssertBlock.DoAssert(action215)

        def action216():
            cb.cut_shape_by_name("bogus")

        TryCatchAssertBlock.DoAssert(action216)

        def action217():
            cb.add_copy_of_shape(None)

        TryCatchAssertBlock.DoAssert(action217)

        shape: "CentralBodyShapeOblateSpheroid" = clr.CastAs(
            cb.add_shape(CENTRAL_BODY_SHAPE.OBLATE_SPHEROID, "NewShape"), CentralBodyShapeOblateSpheroid
        )
        shape.min_radius = 1337
        cb.cut_shape_by_name("NewShape")
        pastedShape: "CentralBodyShapeOblateSpheroid" = clr.CastAs(cb.paste_shape(), CentralBodyShapeOblateSpheroid)
        Assert.assertEqual(1337, pastedShape.min_radius)

        # copy
        cb.copy_shape_by_name("NewShape")
        clipShape: "CentralBodyShapeOblateSpheroid" = clr.CastAs(cb.paste_shape(), CentralBodyShapeOblateSpheroid)
        Assert.assertEqual(1337, clipShape.min_radius)

        # paste same name...
        pastedShape = clr.CastAs(cb.paste_shape(), CentralBodyShapeOblateSpheroid)

        # insert copy
        copiedShape: "CentralBodyShapeOblateSpheroid" = clr.CastAs(
            cb.add_copy_of_shape(pastedShape), CentralBodyShapeOblateSpheroid
        )
        Assert.assertEqual(1337, copiedShape.min_radius)

        # new instance
        copiedShape.min_radius = 1336
        Assert.assertEqual(1337, pastedShape.min_radius)

        def action218():
            cb.paste_attitude()

        # Attitude Definition
        TryCatchAssertBlock.DoAssert(action218)

        def action219():
            cb.cut_attitude_by_name("bogus")

        TryCatchAssertBlock.DoAssert(action219)

        def action220():
            cb.add_copy_of_attitude(None)

        TryCatchAssertBlock.DoAssert(action220)

        newAtt: "CentralBodyAttitudeIAU1994" = clr.CastAs(
            cb.add_attitude(CENTRAL_BODY_ATTITUDE.IAU1994, "NewAttitude"), CentralBodyAttitudeIAU1994
        )
        newAtt.rotation_rate = 1
        cb.cut_attitude_by_name("NewAttitude")
        pastedAttitude: "CentralBodyAttitudeIAU1994" = clr.CastAs(cb.paste_attitude(), CentralBodyAttitudeIAU1994)
        Assert.assertEqual(1, pastedAttitude.rotation_rate)

        # copy
        cb.copy_attitude_by_name("NewAttitude")
        clipAtt: "CentralBodyAttitudeIAU1994" = clr.CastAs(cb.paste_attitude(), CentralBodyAttitudeIAU1994)
        Assert.assertEqual(1, clipAtt.rotation_rate)

        # paste same name...
        pastedAttitude = clr.CastAs(cb.paste_attitude(), CentralBodyAttitudeIAU1994)

        copiedAtt: "CentralBodyAttitudeIAU1994" = clr.CastAs(
            cb.add_copy_of_attitude(pastedAttitude), CentralBodyAttitudeIAU1994
        )
        Assert.assertEqual(1, copiedAtt.rotation_rate)

        # test that we have a new instance
        copiedAtt.rotation_rate = 1.1
        Assert.assertEqual(1, pastedAttitude.rotation_rate)

        def action221():
            cb.paste_ephemeris()

        # Ephemeris Definition
        TryCatchAssertBlock.DoAssert(action221)

        def action222():
            cb.cut_ephemeris_by_name("bogus")

        TryCatchAssertBlock.DoAssert(action222)

        def action223():
            cb.add_copy_of_ephemeris(None)

        TryCatchAssertBlock.DoAssert(action223)

        newEphem: "CentralBodyEphemerisAnalyticOrbit" = clr.CastAs(
            cb.add_ephemeris(CENTRAL_BODY_EPHEMERIS.ANALYTIC_ORBIT, "NewEphem"), CentralBodyEphemerisAnalyticOrbit
        )
        newEphem.inclination = 25
        cb.cut_ephemeris_by_name("NewEphem")
        pastedEphem: "CentralBodyEphemerisAnalyticOrbit" = clr.CastAs(
            cb.paste_ephemeris(), CentralBodyEphemerisAnalyticOrbit
        )
        Assert.assertEqual(25, pastedEphem.inclination)

        # copy
        cb.copy_ephemeris_by_name("NewEphem")
        clipEphem: "CentralBodyEphemerisAnalyticOrbit" = clr.CastAs(
            cb.paste_ephemeris(), CentralBodyEphemerisAnalyticOrbit
        )
        Assert.assertEqual(25, clipEphem.inclination)

        # paste same name...
        pastedEphem = clr.CastAs(cb.paste_ephemeris(), CentralBodyEphemerisAnalyticOrbit)

        copiedEphem: "CentralBodyEphemerisAnalyticOrbit" = clr.CastAs(
            cb.add_copy_of_ephemeris(pastedEphem), CentralBodyEphemerisAnalyticOrbit
        )
        Assert.assertEqual(25, copiedEphem.inclination)

        # test that we have a new instance
        copiedEphem.inclination = 26
        Assert.assertEqual(25, pastedEphem.inclination)

        del cb

    # endregion

    def test_TestComponentsInFolders(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - ComponentsInFolders START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "ComponentsInFolders"),
            Satellite,
        )
        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)

        astComps: "ComponentInfoCollection" = (
            clr.Convert(TestBase.Application.current_scenario, Scenario)
        ).component_directory.get_components(COMPONENT.ASTROGATOR)
        propagators: "ComponentInfoCollection" = astComps.get_folder("Propagators")
        newPropagator: "NumericalPropagatorWrapper" = clr.CastAs(
            (clr.Convert(propagators["Earth J2"], ICloneable)).clone_object(), NumericalPropagatorWrapper
        )
        propFuncColl: "PropagatorFunctionCollection" = newPropagator.propagator_functions

        # tests the Prop Function collection, components are in subfolders
        propFuncColl.add("Atmospheric Models/Cira72")
        Assert.assertIsNotNone(propFuncColl["Cira72"])
        propFuncColl.remove("Cira72")
        propFuncColl.add("Cira72")
        Assert.assertIsNotNone(propFuncColl["Cira72"])
        propFuncColl.remove("Cira72")
        # top level component
        propFuncColl.add("General Relativity")
        Assert.assertIsNotNone(propFuncColl["General Relativity"])
        propFuncColl.remove("General Relativity")

        def action224():
            propFuncColl.add("Nonexistent")

        TryCatchAssertBlock.DoAssert(action224)

        def action225():
            propFuncColl.add("Nonexistent/Cira72")

        TryCatchAssertBlock.DoAssert(action225)

        def action226():
            propFuncColl.add("Atmospheric Models/Nonexistent")

        TryCatchAssertBlock.DoAssert(action226)

        # tests Calc Object Collection
        propagate: "IMissionControlSequenceSegment" = driver.main_sequence["Propagate"]
        propagate.results.add("Keplerian Elems/Eccentricity")
        propagate.results.add("Inclination")
        propagate.results.add("Epoch")  # top level component
        Assert.assertEqual(3, propagate.results.count)

        def action227():
            propagate.results.add("Nonexistent")

        TryCatchAssertBlock.DoAssert(action227)

        def action228():
            propagate.results.add("Nonexistent/Inclination")

        TryCatchAssertBlock.DoAssert(action228)

        def action229():
            propagate.results.add("Keplerian Elems/Nonexistent")

        TryCatchAssertBlock.DoAssert(action229)

        # tests embeds
        userSel: "StoppingCondition" = clr.Convert(
            (clr.Convert(propagate, MissionControlSequencePropagate)).stopping_conditions.add("UserSelect").properties,
            StoppingCondition,
        )
        userSel.user_calc_object_name = "Keplerian Elems/Eccentricity"
        Assert.assertEqual("Eccentricity", userSel.user_calc_object_name)
        userSel.user_calc_object_name = "Inclination"
        Assert.assertEqual("Inclination", userSel.user_calc_object_name)

        # tests links (propagators)
        (
            clr.Convert(propagate, MissionControlSequencePropagate)
        ).propagator_name = "Previous Versions/Earth HPOP Default v8-1-1"
        Assert.assertEqual(
            "Earth HPOP Default v8-1-1", (clr.Convert(propagate, MissionControlSequencePropagate)).propagator_name
        )
        (clr.Convert(propagate, MissionControlSequencePropagate)).propagator_name = "Earth HPOP Default v8-1"
        Assert.assertEqual(
            "Earth HPOP Default v8-1", (clr.Convert(propagate, MissionControlSequencePropagate)).propagator_name
        )

        # backward comp.
        (clr.Convert(propagate, MissionControlSequencePropagate)).propagator_name = "Earth HPOP Default v8-1-1"
        Assert.assertEqual(
            "Earth HPOP Default v8-1-1", (clr.Convert(propagate, MissionControlSequencePropagate)).propagator_name
        )

        def action230():
            (clr.Convert(propagate, MissionControlSequencePropagate)).propagator_name = "Nonexistent"

        TryCatchAssertBlock.DoAssert(action230)

        def action231():
            (
                clr.Convert(propagate, MissionControlSequencePropagate)
            ).propagator_name = "Nonexistent/Earth HPOP Default v11"

        TryCatchAssertBlock.DoAssert(action231)

        def action232():
            (clr.Convert(propagate, MissionControlSequencePropagate)).propagator_name = "Previous Versions/Nonexistent"

        TryCatchAssertBlock.DoAssert(action232)

        # test segment collection
        driver.main_sequence.insert_by_name("Hohmann Transfer", "-")
        Assert.assertIsNotNone(driver.main_sequence["Hohmann Transfer"])

        def action233():
            driver.main_sequence.insert_by_name("Nonexistent", "-")

        TryCatchAssertBlock.DoAssert(action233)

        def action234():
            driver.main_sequence.insert_by_name("Nonexistent/Propagate", "-")

        TryCatchAssertBlock.DoAssert(action234)

        def action235():
            driver.main_sequence.insert_by_name("Examples/Propagate", "-")

        TryCatchAssertBlock.DoAssert(action235)

        driver.main_sequence.insert_by_name("Examples/Hohmann Transfer", "-")
        Assert.assertIsNotNone(driver.main_sequence["Hohmann Transfer1"])

        (clr.Convert(sat, IStkObject)).unload()

    def test_SpacesInVGTPath(self):
        TestBase.logger.WriteLine("*** Astrogator - EarlyBound - SpacesInVGTPath START")
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "VGT"), Satellite
        )
        satWithSpaces: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "VGT_Space"), Satellite
        )

        sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat.propagator, DriverMissionControlSequence)
        propSeg: "IMissionControlSequenceSegment" = driver.main_sequence["Propagate"]
        vecX: "StateCalcVectorX" = clr.Convert(propSeg.results.add("Vector/Vector X"), StateCalcVectorX)
        vecX.vector_name = "Satellite/VGT_Space Position"
        Assert.assertEqual("Satellite/VGT_Space Position", vecX.vector_name)
        vecX.vector_name = "Satellite/VGT Position"
        Assert.assertEqual("Satellite/VGT Position", vecX.vector_name)
        # make sure templates still work
        vecX.vector_name = "Satellite Position"
        Assert.assertEqual("Satellite Position", vecX.vector_name)

        # backwards compatible with not including underscores (also seen in prevous tests)
        vecX.vector_name = "CentralBody/Earth BBR Axes.X"
        Assert.assertEqual("CentralBody/Earth BBR_Axes.X", vecX.vector_name)
        vecX.vector_name = "CentralBody/Earth BBR_Axes.X"
        Assert.assertEqual("CentralBody/Earth BBR_Axes.X", vecX.vector_name)

        def action236():
            vecX.vector_name = "Satellite/Invalid Position"

        TryCatchAssertBlock.DoAssert(action236)

        def action237():
            vecX.vector_name = "Invalid/Invalid Position"

        TryCatchAssertBlock.DoAssert(action237)

        def action238():
            vecX.vector_name = "Invalid/VGT Position"

        TryCatchAssertBlock.DoAssert(action238)

        def action239():
            vecX.vector_name = "Satellite/VGT Invalid"

        TryCatchAssertBlock.DoAssert(action239)
        (clr.Convert(satWithSpaces, IStkObject)).unload()
        (clr.Convert(sat, IStkObject)).unload()

    @category("ExcludeOnLinux")
    def test_MarsGRAM(self):
        scenario: "Scenario" = clr.CastAs(TestBase.Application.current_scenario, Scenario)
        compCollection: "ComponentInfoCollection" = scenario.component_directory.get_components(COMPONENT.ASTROGATOR)
        propObjs: "ComponentInfoCollection" = compCollection.get_folder("Propagators")
        epmProp: "ICloneable" = clr.CastAs(propObjs["Earth Point Mass"], ICloneable)
        epmProp.clone_object()
        mpmProp: "IComponentInfo" = propObjs["Earth Point Mass1"]
        mpmProp.name = "Mars HPOP"
        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).central_body_name = "Mars"

        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.add("Atmospheric Models/Mars GRAM 2000")
        Assert.assertIsNotNone(
            (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions["Mars GRAM 2000"]
        )
        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.remove("Mars GRAM 2000")

        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.add("Atmospheric Models/Mars GRAM 2001")
        Assert.assertIsNotNone(
            (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions["Mars GRAM 2001"]
        )
        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.remove("Mars GRAM 2001")

        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.add("Atmospheric Models/Mars GRAM 2005")
        Assert.assertIsNotNone(
            (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions["Mars GRAM 2005"]
        )
        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.remove("Mars GRAM 2005")

        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.add("Atmospheric Models/Mars GRAM 2010")
        Assert.assertIsNotNone(
            (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions["Mars GRAM 2010"]
        )
        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.remove("Mars GRAM 2010")

        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.add("Atmospheric Models/Mars GRAM 3 7")
        Assert.assertIsNotNone((clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions["Mars GRAM 3 7"])
        (clr.Convert(mpmProp, NumericalPropagatorWrapper)).propagator_functions.remove("Mars GRAM 3 7")

        propObjs.remove("Mars HPOP")

    def test_BUG78776(self):
        sat78776: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Sat78776"), Satellite
        )
        sat78776.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        driver: "DriverMissionControlSequence" = clr.CastAs(sat78776.propagator, DriverMissionControlSequence)
        prop: "MissionControlSequencePropagate" = clr.CastAs(
            driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Prop", "-"), MissionControlSequencePropagate
        )

        scePeriapsis: "StoppingConditionElement" = prop.stopping_conditions.add("Periapsis")
        scePeriapsis.active = True
        sc: "StoppingCondition" = clr.CastAs(scePeriapsis.properties, StoppingCondition)
        sc.tolerance = 0.1
        Assert.assertEqual(0.1, sc.tolerance)
        sc.tolerance = 0.01
        Assert.assertEqual(0.01, sc.tolerance)

        sceApoapsis: "StoppingConditionElement" = prop.stopping_conditions.add("Apoapsis")
        sceApoapsis.active = True
        sc = clr.CastAs(sceApoapsis.properties, StoppingCondition)
        sc.tolerance = 0.1
        Assert.assertEqual(0.1, sc.tolerance)
        sc.tolerance = 0.01
        Assert.assertEqual(0.01, sc.tolerance)

        TestBase.Application.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "Sat78776")

    # endregion
