from test_util import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.stkx import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    m_satellite: "Satellite" = None
    m_driver: "DriverMissionControlSequence" = None

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("AstrogatorTests", "AstrogatorTests.sc"))

        EarlyBoundTests.m_satellite = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "CopyPasteTest"), Satellite
        )
        EarlyBoundTests.m_satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        EarlyBoundTests.m_driver = clr.Convert(EarlyBoundTests.m_satellite.propagator, DriverMissionControlSequence)

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        EarlyBoundTests.m_satellite = None
        EarlyBoundTests.m_driver = None
        TestBase.Uninitialize()

    # endregion

    # region CutPropagateControlTest
    def test_CutPropagateControlTest(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")
        targSeq: "MissionControlSequenceTargetSequence" = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        targSeq2: "MissionControlSequenceTargetSequence" = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        prop: "MissionControlSequencePropagate" = clr.Convert(
            targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )
        prop.stopping_conditions["Duration"].enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        (clr.Convert(prop, IMissionControlSequenceSegment)).results.add("Keplerian Elems/Inclination")
        diffCorr: "ProfileDifferentialCorrector" = clr.Convert(
            targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector
        )
        control: "DifferentialCorrectorControl" = diffCorr.control_parameters.get_control_by_paths(
            "TargetSequence.Propagate", "StoppingConditions.Duration.TripValue"
        )
        constraint: "DifferentialCorrectorResult" = diffCorr.results.get_result_by_paths(
            "TargetSequence.Propagate", "Inclination"
        )
        control.enable = True
        control.max_step = 234
        constraint.enable = True
        constraint.desired_value = 45
        targSeq2.segments.cut("Propagate")
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "TargetSequence")
        targSeq2.segments.paste("-")
        control = diffCorr.control_parameters.get_control_by_paths(
            "TargetSequence.Propagate", "StoppingConditions.Duration.TripValue"
        )
        constraint = diffCorr.results.get_result_by_paths("TargetSequence.Propagate", "Inclination")
        Assert.assertEqual(234, float(control.max_step))
        Assert.assertTrue(control.enable)
        Assert.assertEqual(45, float(constraint.desired_value))
        Assert.assertTrue(constraint.enable)

        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeResultStayActive
    def test_ChangeResultStayActive(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")
        targSeq: "MissionControlSequenceTargetSequence" = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        targSeq2: "MissionControlSequenceTargetSequence" = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        prop: "MissionControlSequencePropagate" = clr.Convert(
            targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )
        result: "IComponentInfo" = (clr.Convert(prop, IMissionControlSequenceSegment)).results.add(
            "Keplerian Elems/Inclination"
        )

        diffCorr: "ProfileDifferentialCorrector" = clr.Convert(
            targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector
        )
        dcEqConst: "DifferentialCorrectorResult" = clr.Convert(
            diffCorr.results.get_result_by_paths("TargetSequence.Propagate", "Inclination"), DifferentialCorrectorResult
        )
        dcEqConst.enable = True
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReference
    def test_ChangeProfilesHoldReference(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None

        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        man: "MissionControlSequenceManeuver" = None
        man = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), MissionControlSequenceManeuver
        )
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "MissionControlSequenceReturn" = None
        ret = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), MissionControlSequenceReturn)

        stop: "MissionControlSequenceStop" = None
        stop = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), MissionControlSequenceStop)

        sequence: "IMissionControlSequenceSequence" = None
        sequence = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"), IMissionControlSequenceSequence
        )
        propInsideSequence: "MissionControlSequencePropagate" = None
        propInsideSequence = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        sequence.scripting_tool.enable = True
        seqAttr: "ScriptingSegment" = sequence.scripting_tool.segment_properties.add("Attribute")
        seqAttr.object_name = "Propagate"

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Propagate"

        changeMan: "ProfileChangeManeuverType" = None
        changeMan = clr.Convert(targSeq.profiles.add("Change Maneuver Type"), ProfileChangeManeuverType)
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "ProfileChangePropagator" = None
        changeProp = clr.Convert(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        changeProp.segment_name = "Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "ProfileChangePropagator" = None
        changePropMan = clr.Convert(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        changePropMan.segment_name = "Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeq.profiles.add("Change Return Segment"), ProfileChangeReturnSegment)
        changeReturn.segment_name = "Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "ProfileChangeStoppingConditionState" = None
        changeStopCondition = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), ProfileChangeStoppingConditionState
        )
        changeStopCondition.segment_name = "Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "ProfileChangeStoppingConditionState" = None
        changeStopConditionMan = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), ProfileChangeStoppingConditionState
        )
        changeStopConditionMan.segment_name = "Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "ProfileChangeStopSegment" = None
        changeStopSegment = clr.Convert(targSeq.profiles.add("Change Stop Segment"), ProfileChangeStopSegment)
        changeStopSegment.segment_name = "Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "ProfileScriptingTool" = None
        scriptingTool = clr.Convert(targSeq.profiles.add("Scripting Tool"), ProfileScriptingTool)

        attribute: "ScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReferenceNested
    def test_ChangeProfilesHoldReferenceNested(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None

        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        sequence: "IMissionControlSequenceSequence" = None
        sequence = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"), IMissionControlSequenceSequence
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        man: "MissionControlSequenceManeuver" = None
        man = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), MissionControlSequenceManeuver
        )
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "MissionControlSequenceReturn" = None
        ret = clr.Convert(sequence.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), MissionControlSequenceReturn)

        stop: "MissionControlSequenceStop" = None
        stop = clr.Convert(sequence.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), MissionControlSequenceStop)

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Sequence.Propagate"

        changeMan: "ProfileChangeManeuverType" = None
        changeMan = clr.Convert(targSeq.profiles.add("Change Maneuver Type"), ProfileChangeManeuverType)
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "ProfileChangePropagator" = None
        changeProp = clr.Convert(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        changeProp.segment_name = "Sequence.Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "ProfileChangePropagator" = None
        changePropMan = clr.Convert(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        changePropMan.segment_name = "Sequence.Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeq.profiles.add("Change Return Segment"), ProfileChangeReturnSegment)
        changeReturn.segment_name = "Sequence.Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "ProfileChangeStoppingConditionState" = None
        changeStopCondition = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), ProfileChangeStoppingConditionState
        )
        changeStopCondition.segment_name = "Sequence.Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "ProfileChangeStoppingConditionState" = None
        changeStopConditionMan = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), ProfileChangeStoppingConditionState
        )
        changeStopConditionMan.segment_name = "Sequence.Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "ProfileChangeStopSegment" = None
        changeStopSegment = clr.Convert(targSeq.profiles.add("Change Stop Segment"), ProfileChangeStopSegment)
        changeStopSegment.segment_name = "Sequence.Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "ProfileScriptingTool" = None
        scriptingTool = clr.Convert(targSeq.profiles.add("Scripting Tool"), ProfileScriptingTool)

        attribute: "ScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Sequence.Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReferenceCopyTargSeq
    def test_ChangeProfilesHoldReferenceCopyTargSeq(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None

        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        man: "MissionControlSequenceManeuver" = None
        man = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), MissionControlSequenceManeuver
        )
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "MissionControlSequenceReturn" = None
        ret = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), MissionControlSequenceReturn)

        stop: "MissionControlSequenceStop" = None
        stop = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), MissionControlSequenceStop)

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Propagate"

        changeMan: "ProfileChangeManeuverType" = None
        changeMan = clr.Convert(targSeq.profiles.add("Change Maneuver Type"), ProfileChangeManeuverType)
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "ProfileChangePropagator" = None
        changeProp = clr.Convert(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        changeProp.segment_name = "Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "ProfileChangePropagator" = None
        changePropMan = clr.Convert(targSeq.profiles.add("Change Propagator"), ProfileChangePropagator)
        changePropMan.segment_name = "Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeq.profiles.add("Change Return Segment"), ProfileChangeReturnSegment)
        changeReturn.segment_name = "Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "ProfileChangeStoppingConditionState" = None
        changeStopCondition = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), ProfileChangeStoppingConditionState
        )
        changeStopCondition.segment_name = "Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "ProfileChangeStoppingConditionState" = None
        changeStopConditionMan = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), ProfileChangeStoppingConditionState
        )
        changeStopConditionMan.segment_name = "Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "ProfileChangeStopSegment" = None
        changeStopSegment = clr.Convert(targSeq.profiles.add("Change Stop Segment"), ProfileChangeStopSegment)
        changeStopSegment.segment_name = "Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "ProfileScriptingTool" = None
        scriptingTool = clr.Convert(targSeq.profiles.add("Scripting Tool"), ProfileScriptingTool)

        attribute: "ScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region RenameActiveControl
    def test_RenameActiveControl(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None

        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        targSeq2: "MissionControlSequenceTargetSequence" = None

        targSeq2 = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target Sequence", "-"),
            MissionControlSequenceTargetSequence,
        )
        prop: "MissionControlSequencePropagate" = None

        prop = clr.Convert(
            targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector)

    # endregion

    # region CutNestedSequences
    def test_CutNestedSequences(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeqOuter: "MissionControlSequenceTargetSequence" = None

        targSeqOuter = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        sequence: "IMissionControlSequenceSequence" = None
        sequence = clr.Convert(
            targSeqOuter.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"), IMissionControlSequenceSequence
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        man: "MissionControlSequenceManeuver" = None
        man = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), MissionControlSequenceManeuver
        )
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "MissionControlSequenceReturn" = None
        ret = clr.Convert(sequence.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), MissionControlSequenceReturn)

        stop: "MissionControlSequenceStop" = None
        stop = clr.Convert(sequence.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), MissionControlSequenceStop)

        targSeqInner: "MissionControlSequenceTargetSequence" = None
        targSeqInner = clr.Convert(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target Sequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        prop2: "MissionControlSequencePropagate" = None
        prop2 = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        man2: "MissionControlSequenceManeuver" = None
        man2 = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), MissionControlSequenceManeuver
        )
        man2.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret2: "MissionControlSequenceReturn" = None
        ret2 = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), MissionControlSequenceReturn
        )

        stop2: "MissionControlSequenceStop" = None
        stop2 = clr.Convert(targSeqInner.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), MissionControlSequenceStop)

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeqOuter.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Sequence.Propagate"

        changeMan: "ProfileChangeManeuverType" = None
        changeMan = clr.Convert(targSeqOuter.profiles.add("Change Maneuver Type"), ProfileChangeManeuverType)
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "ProfileChangePropagator" = None
        changeProp = clr.Convert(targSeqOuter.profiles.add("Change Propagator"), ProfileChangePropagator)
        changeProp.segment_name = "Sequence.Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "ProfileChangePropagator" = None
        changePropMan = clr.Convert(targSeqOuter.profiles.add("Change Propagator"), ProfileChangePropagator)
        changePropMan.segment_name = "Sequence.Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeqOuter.profiles.add("Change Return Segment"), ProfileChangeReturnSegment)
        changeReturn.segment_name = "Sequence.Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "ProfileChangeStoppingConditionState" = None
        changeStopCondition = clr.Convert(
            targSeqOuter.profiles.add("Change Stopping Condition State"), ProfileChangeStoppingConditionState
        )
        changeStopCondition.segment_name = "Sequence.Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "ProfileChangeStoppingConditionState" = None
        changeStopConditionMan = clr.Convert(
            targSeqOuter.profiles.add("Change Stopping Condition State"), ProfileChangeStoppingConditionState
        )
        changeStopConditionMan.segment_name = "Sequence.Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "ProfileChangeStopSegment" = None
        changeStopSegment = clr.Convert(targSeqOuter.profiles.add("Change Stop Segment"), ProfileChangeStopSegment)
        changeStopSegment.segment_name = "Sequence.Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "ProfileScriptingTool" = None
        scriptingTool = clr.Convert(targSeqOuter.profiles.add("Scripting Tool"), ProfileScriptingTool)

        attribute: "ScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Sequence.Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ParameterStaysEnabled
    def test_ParameterStaysEnabled(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None
        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector)
        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True
        dcParam: "ScriptingParameter" = dcScriptTool.parameters.add("Parameter")
        dcParam2: "ScriptingParameter" = dcScriptTool.parameters.add("ParameterNowWithMoreChars")
        control: "DifferentialCorrectorControl" = diffCorr.control_parameters.get_control_by_paths(
            "Scripting_Tool", "Parameter"
        )
        control.enable = True

        dcParam.name = "RenamedAttr"

        Assert.assertTrue(control.enable)

    # endregion

    # region NestedParameterStaysEnabled
    def test_NestedParameterStaysEnabled(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeqOuter: "MissionControlSequenceTargetSequence" = None
        targSeqOuter = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        targSeqInner: "MissionControlSequenceTargetSequence" = None
        targSeqInner = clr.Convert(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        diffCorrOuter: "ProfileDifferentialCorrector" = None
        diffCorrOuter = clr.Convert(targSeqOuter.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        diffCorrInner: "ProfileDifferentialCorrector" = None
        diffCorrInner = clr.Convert(targSeqInner.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        dcScriptTool: "ScriptingTool" = diffCorrInner.scripting_tool
        dcScriptTool.enable = True

        dcParam: "ScriptingParameter" = dcScriptTool.parameters.add("Parameter")
        dcParam2: "ScriptingParameter" = dcScriptTool.parameters.add("ParameterNowWithMoreChars")

    # endregion

    # region SimilarNamesStayEnabled
    def test_SimilarNamesStayEnabled(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None
        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        durationControl: "StoppingConditionElement" = prop.stopping_conditions["Duration"]

        duration2Control: "StoppingConditionElement" = prop.stopping_conditions.add("Duration")

        durationControl.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        duration2Control.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)

        durationResult: "IComponentInfo" = (clr.Convert(prop, IMissionControlSequenceSegment)).results.add(
            "Time/Duration"
        )
        duration2Result: "IComponentInfo" = (clr.Convert(prop, IMissionControlSequenceSegment)).results.add(
            "Time/Duration"
        )

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector)
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region NestedParameterStaysEnabledCutPaste
    def test_NestedParameterStaysEnabledCutPaste(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeqOuter: "MissionControlSequenceTargetSequence" = None
        targSeqOuter = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        targSeqInner: "MissionControlSequenceTargetSequence" = None
        targSeqInner = clr.Convert(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        diffCorrOuter: "ProfileDifferentialCorrector" = None
        diffCorrOuter = clr.Convert(targSeqOuter.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        diffCorrInner: "ProfileDifferentialCorrector" = None
        diffCorrInner = clr.Convert(targSeqInner.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        dcScriptTool: "ScriptingTool" = diffCorrInner.scripting_tool
        dcScriptTool.enable = True

        dcParam: "ScriptingParameter" = dcScriptTool.parameters.add("Parameter")
        dcParam2: "ScriptingParameter" = dcScriptTool.parameters.add("ParameterNowWithMoreChars")
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region MaintainSegmentLinkThroughCutPaste
    # Perhaps test 42791 also?
    def test_MaintainSegmentLinkThroughCutPaste(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None
        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            MissionControlSequenceTargetSequence,
        )

        prop: "MissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        prop2: "MissionControlSequencePropagate" = None
        prop2 = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), MissionControlSequencePropagate
        )

        result: "IComponentInfo" = (clr.Convert(prop2, IMissionControlSequenceSegment)).results.add(
            "Segments/Difference Across Segments"
        )
        (clr.Convert(result, StateCalcDifferenceOtherSegment)).other_segment_name = "TargetSequence.Propagate"

        diffAcrossSegs: "StoppingConditionElement" = prop2.stopping_conditions.add("UserSelect")

        (
            clr.Convert(diffAcrossSegs.properties, StoppingCondition)
        ).user_calc_object_name = "Segments/Difference Across Segments"
        stopCondCalcObj: "StateCalcDifferenceOtherSegment" = clr.Convert(
            (clr.Convert(diffAcrossSegs.properties, StoppingCondition)).user_calc_object,
            StateCalcDifferenceOtherSegment,
        )
        stopCondCalcObj.other_segment_name = "TargetSequence.Propagate"

        beforeCond: "StoppingConditionElement" = (
            clr.Convert(diffAcrossSegs.properties, StoppingCondition)
        ).before_conditions.add("UserSelect")
        (
            clr.Convert(beforeCond.properties, StoppingCondition)
        ).user_calc_object_name = "Segments/Difference Across Segments"
        beforeCondCalcObj: "StateCalcDifferenceOtherSegment" = clr.Convert(
            (clr.Convert(beforeCond.properties, StoppingCondition)).user_calc_object, StateCalcDifferenceOtherSegment
        )
        beforeCondCalcObj.other_segment_name = "TargetSequence.Propagate"

        constraint: "AsTriggerCondition" = clr.Convert(
            (clr.Convert(diffAcrossSegs.properties, StoppingCondition)).constraints.add("UserDefined"),
            AsTriggerCondition,
        )

        constraint.calc_object_name = "Segments/Difference Across Segments"
        (
            clr.Convert(constraint.calc_object, StateCalcDifferenceOtherSegment)
        ).other_segment_name = "TargetSequence.Propagate"

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], ProfileDifferentialCorrector)

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttr: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttr.object_name = "Propagate"
        dcCalcObjWrap: "ScriptingCalcObject" = dcScriptTool.calc_objects.add("CalcObject")
        dcCalcObjWrap.calc_object_name = "Segments/Difference Across Segments"
        dcDiffOtherSegment: "StateCalcDifferenceOtherSegment" = clr.Convert(
            dcCalcObjWrap.calc_object, StateCalcDifferenceOtherSegment
        )
        dcDiffOtherSegment.other_segment_name = "TargetSequence.Propagate"

    # endregion
