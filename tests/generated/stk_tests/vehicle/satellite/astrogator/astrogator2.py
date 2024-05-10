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

        EarlyBoundTests.m_satellite = Satellite(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "CopyPasteTest")
        )
        EarlyBoundTests.m_satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        EarlyBoundTests.m_driver = DriverMissionControlSequence(EarlyBoundTests.m_satellite.propagator)

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
        targSeq: "MissionControlSequenceTargetSequence" = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )
        targSeq2: "MissionControlSequenceTargetSequence" = MissionControlSequenceTargetSequence(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )
        prop: "MissionControlSequencePropagate" = MissionControlSequencePropagate(
            targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        )
        prop.stopping_conditions["Duration"].enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        (IMissionControlSequenceSegment(prop)).results.add("Keplerian Elems/Inclination")
        diffCorr: "ProfileDifferentialCorrector" = ProfileDifferentialCorrector(
            targSeq.profiles["Differential Corrector"]
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
        targSeq: "MissionControlSequenceTargetSequence" = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )
        targSeq2: "MissionControlSequenceTargetSequence" = MissionControlSequenceTargetSequence(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )
        prop: "MissionControlSequencePropagate" = MissionControlSequencePropagate(
            targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        )
        result: "IComponentInfo" = (IMissionControlSequenceSegment(prop)).results.add("Keplerian Elems/Inclination")

        diffCorr: "ProfileDifferentialCorrector" = ProfileDifferentialCorrector(
            targSeq.profiles["Differential Corrector"]
        )
        dcEqConst: "DifferentialCorrectorResult" = diffCorr.results.get_result_by_paths(
            "TargetSequence.Propagate", "Inclination"
        )
        dcEqConst.enable = True
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReference
    def test_ChangeProfilesHoldReference(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None

        targSeq = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        man: "MissionControlSequenceManeuver" = None
        man = MissionControlSequenceManeuver(targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"))
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "MissionControlSequenceReturn" = None
        ret = MissionControlSequenceReturn(targSeq.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"))

        stop: "MissionControlSequenceStop" = None
        stop = MissionControlSequenceStop(targSeq.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"))

        sequence: "IMissionControlSequenceSequence" = None
        sequence = IMissionControlSequenceSequence(targSeq.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"))
        propInsideSequence: "MissionControlSequencePropagate" = None
        propInsideSequence = MissionControlSequencePropagate(
            sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        )

        sequence.scripting_tool.enable = True
        seqAttr: "ScriptingSegment" = sequence.scripting_tool.segment_properties.add("Attribute")
        seqAttr.object_name = "Propagate"

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = ProfileDifferentialCorrector(targSeq.profiles["Differential Corrector"])

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Propagate"

        changeMan: "ProfileChangeManeuverType" = None
        changeMan = ProfileChangeManeuverType(targSeq.profiles.add("Change Maneuver Type"))
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "ProfileChangePropagator" = None
        changeProp = ProfileChangePropagator(targSeq.profiles.add("Change Propagator"))
        changeProp.segment_name = "Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "ProfileChangePropagator" = None
        changePropMan = ProfileChangePropagator(targSeq.profiles.add("Change Propagator"))
        changePropMan.segment_name = "Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = ProfileChangeReturnSegment(targSeq.profiles.add("Change Return Segment"))
        changeReturn.segment_name = "Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "ProfileChangeStoppingConditionState" = None
        changeStopCondition = ProfileChangeStoppingConditionState(
            targSeq.profiles.add("Change Stopping Condition State")
        )
        changeStopCondition.segment_name = "Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "ProfileChangeStoppingConditionState" = None
        changeStopConditionMan = ProfileChangeStoppingConditionState(
            targSeq.profiles.add("Change Stopping Condition State")
        )
        changeStopConditionMan.segment_name = "Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "ProfileChangeStopSegment" = None
        changeStopSegment = ProfileChangeStopSegment(targSeq.profiles.add("Change Stop Segment"))
        changeStopSegment.segment_name = "Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "ProfileScriptingTool" = None
        scriptingTool = ProfileScriptingTool(targSeq.profiles.add("Scripting Tool"))

        attribute: "ScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReferenceNested
    def test_ChangeProfilesHoldReferenceNested(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None

        targSeq = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        sequence: "IMissionControlSequenceSequence" = None
        sequence = IMissionControlSequenceSequence(targSeq.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"))

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        man: "MissionControlSequenceManeuver" = None
        man = MissionControlSequenceManeuver(sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"))
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "MissionControlSequenceReturn" = None
        ret = MissionControlSequenceReturn(sequence.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"))

        stop: "MissionControlSequenceStop" = None
        stop = MissionControlSequenceStop(sequence.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"))

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = ProfileDifferentialCorrector(targSeq.profiles["Differential Corrector"])

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Sequence.Propagate"

        changeMan: "ProfileChangeManeuverType" = None
        changeMan = ProfileChangeManeuverType(targSeq.profiles.add("Change Maneuver Type"))
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "ProfileChangePropagator" = None
        changeProp = ProfileChangePropagator(targSeq.profiles.add("Change Propagator"))
        changeProp.segment_name = "Sequence.Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "ProfileChangePropagator" = None
        changePropMan = ProfileChangePropagator(targSeq.profiles.add("Change Propagator"))
        changePropMan.segment_name = "Sequence.Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = ProfileChangeReturnSegment(targSeq.profiles.add("Change Return Segment"))
        changeReturn.segment_name = "Sequence.Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "ProfileChangeStoppingConditionState" = None
        changeStopCondition = ProfileChangeStoppingConditionState(
            targSeq.profiles.add("Change Stopping Condition State")
        )
        changeStopCondition.segment_name = "Sequence.Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "ProfileChangeStoppingConditionState" = None
        changeStopConditionMan = ProfileChangeStoppingConditionState(
            targSeq.profiles.add("Change Stopping Condition State")
        )
        changeStopConditionMan.segment_name = "Sequence.Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "ProfileChangeStopSegment" = None
        changeStopSegment = ProfileChangeStopSegment(targSeq.profiles.add("Change Stop Segment"))
        changeStopSegment.segment_name = "Sequence.Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "ProfileScriptingTool" = None
        scriptingTool = ProfileScriptingTool(targSeq.profiles.add("Scripting Tool"))

        attribute: "ScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Sequence.Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReferenceCopyTargSeq
    def test_ChangeProfilesHoldReferenceCopyTargSeq(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None

        targSeq = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        man: "MissionControlSequenceManeuver" = None
        man = MissionControlSequenceManeuver(targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"))
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "MissionControlSequenceReturn" = None
        ret = MissionControlSequenceReturn(targSeq.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"))

        stop: "MissionControlSequenceStop" = None
        stop = MissionControlSequenceStop(targSeq.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"))

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = ProfileDifferentialCorrector(targSeq.profiles["Differential Corrector"])

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Propagate"

        changeMan: "ProfileChangeManeuverType" = None
        changeMan = ProfileChangeManeuverType(targSeq.profiles.add("Change Maneuver Type"))
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "ProfileChangePropagator" = None
        changeProp = ProfileChangePropagator(targSeq.profiles.add("Change Propagator"))
        changeProp.segment_name = "Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "ProfileChangePropagator" = None
        changePropMan = ProfileChangePropagator(targSeq.profiles.add("Change Propagator"))
        changePropMan.segment_name = "Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = ProfileChangeReturnSegment(targSeq.profiles.add("Change Return Segment"))
        changeReturn.segment_name = "Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "ProfileChangeStoppingConditionState" = None
        changeStopCondition = ProfileChangeStoppingConditionState(
            targSeq.profiles.add("Change Stopping Condition State")
        )
        changeStopCondition.segment_name = "Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "ProfileChangeStoppingConditionState" = None
        changeStopConditionMan = ProfileChangeStoppingConditionState(
            targSeq.profiles.add("Change Stopping Condition State")
        )
        changeStopConditionMan.segment_name = "Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "ProfileChangeStopSegment" = None
        changeStopSegment = ProfileChangeStopSegment(targSeq.profiles.add("Change Stop Segment"))
        changeStopSegment.segment_name = "Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "ProfileScriptingTool" = None
        scriptingTool = ProfileScriptingTool(targSeq.profiles.add("Scripting Tool"))

        attribute: "ScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region RenameActiveControl
    def test_RenameActiveControl(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None

        targSeq = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        targSeq2: "MissionControlSequenceTargetSequence" = None

        targSeq2 = MissionControlSequenceTargetSequence(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target Sequence", "-")
        )
        prop: "MissionControlSequencePropagate" = None

        prop = MissionControlSequencePropagate(targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = ProfileDifferentialCorrector(targSeq.profiles["Differential Corrector"])

    # endregion

    # region CutNestedSequences
    def test_CutNestedSequences(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeqOuter: "MissionControlSequenceTargetSequence" = None

        targSeqOuter = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        sequence: "IMissionControlSequenceSequence" = None
        sequence = IMissionControlSequenceSequence(targSeqOuter.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"))

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        man: "MissionControlSequenceManeuver" = None
        man = MissionControlSequenceManeuver(sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"))
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "MissionControlSequenceReturn" = None
        ret = MissionControlSequenceReturn(sequence.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"))

        stop: "MissionControlSequenceStop" = None
        stop = MissionControlSequenceStop(sequence.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"))

        targSeqInner: "MissionControlSequenceTargetSequence" = None
        targSeqInner = MissionControlSequenceTargetSequence(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target Sequence", "-")
        )

        prop2: "MissionControlSequencePropagate" = None
        prop2 = MissionControlSequencePropagate(targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        man2: "MissionControlSequenceManeuver" = None
        man2 = MissionControlSequenceManeuver(targSeqInner.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"))
        man2.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret2: "MissionControlSequenceReturn" = None
        ret2 = MissionControlSequenceReturn(targSeqInner.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"))

        stop2: "MissionControlSequenceStop" = None
        stop2 = MissionControlSequenceStop(targSeqInner.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"))

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = ProfileDifferentialCorrector(targSeqOuter.profiles["Differential Corrector"])

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Sequence.Propagate"

        changeMan: "ProfileChangeManeuverType" = None
        changeMan = ProfileChangeManeuverType(targSeqOuter.profiles.add("Change Maneuver Type"))
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "ProfileChangePropagator" = None
        changeProp = ProfileChangePropagator(targSeqOuter.profiles.add("Change Propagator"))
        changeProp.segment_name = "Sequence.Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "ProfileChangePropagator" = None
        changePropMan = ProfileChangePropagator(targSeqOuter.profiles.add("Change Propagator"))
        changePropMan.segment_name = "Sequence.Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "ProfileChangeReturnSegment" = None
        changeReturn = ProfileChangeReturnSegment(targSeqOuter.profiles.add("Change Return Segment"))
        changeReturn.segment_name = "Sequence.Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "ProfileChangeStoppingConditionState" = None
        changeStopCondition = ProfileChangeStoppingConditionState(
            targSeqOuter.profiles.add("Change Stopping Condition State")
        )
        changeStopCondition.segment_name = "Sequence.Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "ProfileChangeStoppingConditionState" = None
        changeStopConditionMan = ProfileChangeStoppingConditionState(
            targSeqOuter.profiles.add("Change Stopping Condition State")
        )
        changeStopConditionMan.segment_name = "Sequence.Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "ProfileChangeStopSegment" = None
        changeStopSegment = ProfileChangeStopSegment(targSeqOuter.profiles.add("Change Stop Segment"))
        changeStopSegment.segment_name = "Sequence.Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "ProfileScriptingTool" = None
        scriptingTool = ProfileScriptingTool(targSeqOuter.profiles.add("Scripting Tool"))

        attribute: "ScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Sequence.Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ParameterStaysEnabled
    def test_ParameterStaysEnabled(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "MissionControlSequenceTargetSequence" = None
        targSeq = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = ProfileDifferentialCorrector(targSeq.profiles["Differential Corrector"])
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
        targSeqOuter = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        targSeqInner: "MissionControlSequenceTargetSequence" = None
        targSeqInner = MissionControlSequenceTargetSequence(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        diffCorrOuter: "ProfileDifferentialCorrector" = None
        diffCorrOuter = ProfileDifferentialCorrector(targSeqOuter.profiles["Differential Corrector"])

        diffCorrInner: "ProfileDifferentialCorrector" = None
        diffCorrInner = ProfileDifferentialCorrector(targSeqInner.profiles["Differential Corrector"])

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
        targSeq = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        durationControl: "StoppingConditionElement" = prop.stopping_conditions["Duration"]

        duration2Control: "StoppingConditionElement" = prop.stopping_conditions.add("Duration")

        durationControl.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        duration2Control.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)

        durationResult: "IComponentInfo" = (IMissionControlSequenceSegment(prop)).results.add("Time/Duration")
        duration2Result: "IComponentInfo" = (IMissionControlSequenceSegment(prop)).results.add("Time/Duration")

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = ProfileDifferentialCorrector(targSeq.profiles["Differential Corrector"])
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region NestedParameterStaysEnabledCutPaste
    def test_NestedParameterStaysEnabledCutPaste(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeqOuter: "MissionControlSequenceTargetSequence" = None
        targSeqOuter = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        targSeqInner: "MissionControlSequenceTargetSequence" = None
        targSeqInner = MissionControlSequenceTargetSequence(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        diffCorrOuter: "ProfileDifferentialCorrector" = None
        diffCorrOuter = ProfileDifferentialCorrector(targSeqOuter.profiles["Differential Corrector"])

        diffCorrInner: "ProfileDifferentialCorrector" = None
        diffCorrInner = ProfileDifferentialCorrector(targSeqInner.profiles["Differential Corrector"])

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
        targSeq = MissionControlSequenceTargetSequence(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-")
        )

        prop: "MissionControlSequencePropagate" = None
        prop = MissionControlSequencePropagate(targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        prop2: "MissionControlSequencePropagate" = None
        prop2 = MissionControlSequencePropagate(targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"))

        result: "IComponentInfo" = (IMissionControlSequenceSegment(prop2)).results.add(
            "Segments/Difference Across Segments"
        )
        (StateCalcDifferenceOtherSegment(result)).other_segment_name = "TargetSequence.Propagate"

        diffAcrossSegs: "StoppingConditionElement" = prop2.stopping_conditions.add("UserSelect")

        (StoppingCondition(diffAcrossSegs.properties)).user_calc_object_name = "Segments/Difference Across Segments"
        stopCondCalcObj: "StateCalcDifferenceOtherSegment" = StateCalcDifferenceOtherSegment(
            (StoppingCondition(diffAcrossSegs.properties)).user_calc_object
        )
        stopCondCalcObj.other_segment_name = "TargetSequence.Propagate"

        beforeCond: "StoppingConditionElement" = (StoppingCondition(diffAcrossSegs.properties)).before_conditions.add(
            "UserSelect"
        )
        (StoppingCondition(beforeCond.properties)).user_calc_object_name = "Segments/Difference Across Segments"
        beforeCondCalcObj: "StateCalcDifferenceOtherSegment" = StateCalcDifferenceOtherSegment(
            (StoppingCondition(beforeCond.properties)).user_calc_object
        )
        beforeCondCalcObj.other_segment_name = "TargetSequence.Propagate"

        constraint: "AsTriggerCondition" = (StoppingCondition(diffAcrossSegs.properties)).constraints.add("UserDefined")

        constraint.calc_object_name = "Segments/Difference Across Segments"
        (StateCalcDifferenceOtherSegment(constraint.calc_object)).other_segment_name = "TargetSequence.Propagate"

        diffCorr: "ProfileDifferentialCorrector" = None
        diffCorr = ProfileDifferentialCorrector(targSeq.profiles["Differential Corrector"])

        dcScriptTool: "ScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttr: "ScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttr.object_name = "Propagate"
        dcCalcObjWrap: "ScriptingCalcObject" = dcScriptTool.calc_objects.add("CalcObject")
        dcCalcObjWrap.calc_object_name = "Segments/Difference Across Segments"
        dcDiffOtherSegment: "StateCalcDifferenceOtherSegment" = StateCalcDifferenceOtherSegment(
            dcCalcObjWrap.calc_object
        )
        dcDiffOtherSegment.other_segment_name = "TargetSequence.Propagate"

    # endregion
