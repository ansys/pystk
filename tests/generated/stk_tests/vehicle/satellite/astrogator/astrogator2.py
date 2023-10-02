from test_util import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.stkx import *
from ansys.stk.core.stkutil import *


@category("EarlyBoundTests")
class EarlyBoundTests(TestBase):
    def __init__(self, *args, **kwargs):
        super(EarlyBoundTests, self).__init__(*args, **kwargs)

    m_satellite: "ISatellite" = None
    m_driver: "IDriverMissionControlSequence" = None

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        TestBase.Initialize()
        TestBase.LoadTestScenario(Path.Combine("AstrogatorTests", "AstrogatorTests.sc"))

        EarlyBoundTests.m_satellite = clr.Convert(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "CopyPasteTest"), ISatellite
        )
        EarlyBoundTests.m_satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        EarlyBoundTests.m_driver = clr.Convert(EarlyBoundTests.m_satellite.propagator, IDriverMissionControlSequence)

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
        targSeq: "IMissionControlSequenceTargetSequence" = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )
        targSeq2: "IMissionControlSequenceTargetSequence" = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )
        prop: "IMissionControlSequencePropagate" = clr.Convert(
            targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )
        prop.stopping_conditions["Duration"].enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        (clr.Convert(prop, IMissionControlSequenceSegment)).results.add("Keplerian Elems/Inclination")
        diffCorr: "IProfileDifferentialCorrector" = clr.Convert(
            targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector
        )
        control: "IDifferentialCorrectorControl" = diffCorr.control_parameters.get_control_by_paths(
            "TargetSequence.Propagate", "StoppingConditions.Duration.TripValue"
        )
        constraint: "IDifferentialCorrectorResult" = diffCorr.results.get_result_by_paths(
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
        targSeq: "IMissionControlSequenceTargetSequence" = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )
        targSeq2: "IMissionControlSequenceTargetSequence" = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )
        prop: "IMissionControlSequencePropagate" = clr.Convert(
            targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )
        result: "IComponentInfo" = (clr.Convert(prop, IMissionControlSequenceSegment)).results.add(
            "Keplerian Elems/Inclination"
        )

        diffCorr: "IProfileDifferentialCorrector" = clr.Convert(
            targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector
        )
        dcEqConst: "IDifferentialCorrectorResult" = clr.Convert(
            diffCorr.results.get_result_by_paths("TargetSequence.Propagate", "Inclination"),
            IDifferentialCorrectorResult,
        )
        dcEqConst.enable = True
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReference
    def test_ChangeProfilesHoldReference(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "IMissionControlSequenceTargetSequence" = None

        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        man: "IMissionControlSequenceManeuver" = None
        man = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), IMissionControlSequenceManeuver
        )
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "IMissionControlSequenceReturn" = None
        ret = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), IMissionControlSequenceReturn)

        stop: "IMissionControlSequenceStop" = None
        stop = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), IMissionControlSequenceStop)

        sequence: "IMissionControlSequenceSequence" = None
        sequence = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"), IMissionControlSequenceSequence
        )
        propInsideSequence: "IMissionControlSequencePropagate" = None
        propInsideSequence = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        sequence.scripting_tool.enable = True
        seqAttr: "IScriptingSegment" = sequence.scripting_tool.segment_properties.add("Attribute")
        seqAttr.object_name = "Propagate"

        diffCorr: "IProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        dcScriptTool: "IScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "IScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Propagate"

        changeMan: "IProfileChangeManeuverType" = None
        changeMan = clr.Convert(targSeq.profiles.add("Change Maneuver Type"), IProfileChangeManeuverType)
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "IProfileChangePropagator" = None
        changeProp = clr.Convert(targSeq.profiles.add("Change Propagator"), IProfileChangePropagator)
        changeProp.segment_name = "Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "IProfileChangePropagator" = None
        changePropMan = clr.Convert(targSeq.profiles.add("Change Propagator"), IProfileChangePropagator)
        changePropMan.segment_name = "Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "IProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeq.profiles.add("Change Return Segment"), IProfileChangeReturnSegment)
        changeReturn.segment_name = "Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "IProfileChangeStoppingConditionState" = None
        changeStopCondition = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), IProfileChangeStoppingConditionState
        )
        changeStopCondition.segment_name = "Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "IProfileChangeStoppingConditionState" = None
        changeStopConditionMan = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), IProfileChangeStoppingConditionState
        )
        changeStopConditionMan.segment_name = "Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "IProfileChangeStopSegment" = None
        changeStopSegment = clr.Convert(targSeq.profiles.add("Change Stop Segment"), IProfileChangeStopSegment)
        changeStopSegment.segment_name = "Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "IProfileScriptingTool" = None
        scriptingTool = clr.Convert(targSeq.profiles.add("Scripting Tool"), IProfileScriptingTool)

        attribute: "IScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReferenceNested
    def test_ChangeProfilesHoldReferenceNested(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "IMissionControlSequenceTargetSequence" = None

        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        sequence: "IMissionControlSequenceSequence" = None
        sequence = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"), IMissionControlSequenceSequence
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        man: "IMissionControlSequenceManeuver" = None
        man = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), IMissionControlSequenceManeuver
        )
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "IMissionControlSequenceReturn" = None
        ret = clr.Convert(sequence.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), IMissionControlSequenceReturn)

        stop: "IMissionControlSequenceStop" = None
        stop = clr.Convert(sequence.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), IMissionControlSequenceStop)

        diffCorr: "IProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        dcScriptTool: "IScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "IScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Sequence.Propagate"

        changeMan: "IProfileChangeManeuverType" = None
        changeMan = clr.Convert(targSeq.profiles.add("Change Maneuver Type"), IProfileChangeManeuverType)
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "IProfileChangePropagator" = None
        changeProp = clr.Convert(targSeq.profiles.add("Change Propagator"), IProfileChangePropagator)
        changeProp.segment_name = "Sequence.Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "IProfileChangePropagator" = None
        changePropMan = clr.Convert(targSeq.profiles.add("Change Propagator"), IProfileChangePropagator)
        changePropMan.segment_name = "Sequence.Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "IProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeq.profiles.add("Change Return Segment"), IProfileChangeReturnSegment)
        changeReturn.segment_name = "Sequence.Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "IProfileChangeStoppingConditionState" = None
        changeStopCondition = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), IProfileChangeStoppingConditionState
        )
        changeStopCondition.segment_name = "Sequence.Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "IProfileChangeStoppingConditionState" = None
        changeStopConditionMan = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), IProfileChangeStoppingConditionState
        )
        changeStopConditionMan.segment_name = "Sequence.Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "IProfileChangeStopSegment" = None
        changeStopSegment = clr.Convert(targSeq.profiles.add("Change Stop Segment"), IProfileChangeStopSegment)
        changeStopSegment.segment_name = "Sequence.Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "IProfileScriptingTool" = None
        scriptingTool = clr.Convert(targSeq.profiles.add("Scripting Tool"), IProfileScriptingTool)

        attribute: "IScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Sequence.Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ChangeProfilesHoldReferenceCopyTargSeq
    def test_ChangeProfilesHoldReferenceCopyTargSeq(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "IMissionControlSequenceTargetSequence" = None

        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        man: "IMissionControlSequenceManeuver" = None
        man = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), IMissionControlSequenceManeuver
        )
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "IMissionControlSequenceReturn" = None
        ret = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), IMissionControlSequenceReturn)

        stop: "IMissionControlSequenceStop" = None
        stop = clr.Convert(targSeq.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), IMissionControlSequenceStop)

        diffCorr: "IProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        dcScriptTool: "IScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "IScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Propagate"

        changeMan: "IProfileChangeManeuverType" = None
        changeMan = clr.Convert(targSeq.profiles.add("Change Maneuver Type"), IProfileChangeManeuverType)
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "IProfileChangePropagator" = None
        changeProp = clr.Convert(targSeq.profiles.add("Change Propagator"), IProfileChangePropagator)
        changeProp.segment_name = "Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "IProfileChangePropagator" = None
        changePropMan = clr.Convert(targSeq.profiles.add("Change Propagator"), IProfileChangePropagator)
        changePropMan.segment_name = "Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "IProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeq.profiles.add("Change Return Segment"), IProfileChangeReturnSegment)
        changeReturn.segment_name = "Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "IProfileChangeStoppingConditionState" = None
        changeStopCondition = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), IProfileChangeStoppingConditionState
        )
        changeStopCondition.segment_name = "Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "IProfileChangeStoppingConditionState" = None
        changeStopConditionMan = clr.Convert(
            targSeq.profiles.add("Change Stopping Condition State"), IProfileChangeStoppingConditionState
        )
        changeStopConditionMan.segment_name = "Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "IProfileChangeStopSegment" = None
        changeStopSegment = clr.Convert(targSeq.profiles.add("Change Stop Segment"), IProfileChangeStopSegment)
        changeStopSegment.segment_name = "Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "IProfileScriptingTool" = None
        scriptingTool = clr.Convert(targSeq.profiles.add("Scripting Tool"), IProfileScriptingTool)

        attribute: "IScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region RenameActiveControl
    def test_RenameActiveControl(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "IMissionControlSequenceTargetSequence" = None

        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        targSeq2: "IMissionControlSequenceTargetSequence" = None

        targSeq2 = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target Sequence", "-"),
            IMissionControlSequenceTargetSequence,
        )
        prop: "IMissionControlSequencePropagate" = None

        prop = clr.Convert(
            targSeq2.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        diffCorr: "IProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector)

    # endregion

    # region CutNestedSequences
    def test_CutNestedSequences(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeqOuter: "IMissionControlSequenceTargetSequence" = None

        targSeqOuter = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        sequence: "IMissionControlSequenceSequence" = None
        sequence = clr.Convert(
            targSeqOuter.segments.insert(SEGMENT_TYPE.SEQUENCE, "Sequence", "-"), IMissionControlSequenceSequence
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        man: "IMissionControlSequenceManeuver" = None
        man = clr.Convert(
            sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), IMissionControlSequenceManeuver
        )
        man.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret: "IMissionControlSequenceReturn" = None
        ret = clr.Convert(sequence.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), IMissionControlSequenceReturn)

        stop: "IMissionControlSequenceStop" = None
        stop = clr.Convert(sequence.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), IMissionControlSequenceStop)

        targSeqInner: "IMissionControlSequenceTargetSequence" = None
        targSeqInner = clr.Convert(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Target Sequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        prop2: "IMissionControlSequencePropagate" = None
        prop2 = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        man2: "IMissionControlSequenceManeuver" = None
        man2 = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.MANEUVER, "Maneuver", "-"), IMissionControlSequenceManeuver
        )
        man2.set_maneuver_type(MANEUVER_TYPE.FINITE)

        ret2: "IMissionControlSequenceReturn" = None
        ret2 = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.RETURN, "Return", "-"), IMissionControlSequenceReturn
        )

        stop2: "IMissionControlSequenceStop" = None
        stop2 = clr.Convert(targSeqInner.segments.insert(SEGMENT_TYPE.STOP, "Stop", "-"), IMissionControlSequenceStop)

        diffCorr: "IProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeqOuter.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        dcScriptTool: "IScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttribute: "IScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttribute.object_name = "Sequence.Propagate"

        changeMan: "IProfileChangeManeuverType" = None
        changeMan = clr.Convert(targSeqOuter.profiles.add("Change Maneuver Type"), IProfileChangeManeuverType)
        changeMan.segment = man
        changeMan.name = "MyChangeManeuver"

        changeProp: "IProfileChangePropagator" = None
        changeProp = clr.Convert(targSeqOuter.profiles.add("Change Propagator"), IProfileChangePropagator)
        changeProp.segment_name = "Sequence.Propagate"
        changeProp.name = "MyChangePropagator"

        changePropMan: "IProfileChangePropagator" = None
        changePropMan = clr.Convert(targSeqOuter.profiles.add("Change Propagator"), IProfileChangePropagator)
        changePropMan.segment_name = "Sequence.Maneuver"
        changePropMan.name = "MyChangePropagatorForManeuver"

        changeReturn: "IProfileChangeReturnSegment" = None
        changeReturn = clr.Convert(targSeqOuter.profiles.add("Change Return Segment"), IProfileChangeReturnSegment)
        changeReturn.segment_name = "Sequence.Return"
        changeReturn.name = "MyReturn"

        changeStopCondition: "IProfileChangeStoppingConditionState" = None
        changeStopCondition = clr.Convert(
            targSeqOuter.profiles.add("Change Stopping Condition State"), IProfileChangeStoppingConditionState
        )
        changeStopCondition.segment_name = "Sequence.Propagate"
        changeStopCondition.name = "MyChangeStopCondForPropagate"

        changeStopConditionMan: "IProfileChangeStoppingConditionState" = None
        changeStopConditionMan = clr.Convert(
            targSeqOuter.profiles.add("Change Stopping Condition State"), IProfileChangeStoppingConditionState
        )
        changeStopConditionMan.segment_name = "Sequence.Maneuver"
        changeStopConditionMan.name = "MyChangeStopCondForMan"

        changeStopSegment: "IProfileChangeStopSegment" = None
        changeStopSegment = clr.Convert(targSeqOuter.profiles.add("Change Stop Segment"), IProfileChangeStopSegment)
        changeStopSegment.segment_name = "Sequence.Stop"
        changeStopSegment.name = "MyChangeStopSegment"

        scriptingTool: "IProfileScriptingTool" = None
        scriptingTool = clr.Convert(targSeqOuter.profiles.add("Scripting Tool"), IProfileScriptingTool)

        attribute: "IScriptingSegment" = scriptingTool.segment_properties.add("Attribute")
        attribute.object_name = "Sequence.Propagate"
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region ParameterStaysEnabled
    def test_ParameterStaysEnabled(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "IMissionControlSequenceTargetSequence" = None
        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        diffCorr: "IProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector)
        dcScriptTool: "IScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True
        dcParam: "IScriptingParameter" = dcScriptTool.parameters.add("Parameter")
        dcParam2: "IScriptingParameter" = dcScriptTool.parameters.add("ParameterNowWithMoreChars")
        control: "IDifferentialCorrectorControl" = diffCorr.control_parameters.get_control_by_paths(
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

        targSeqOuter: "IMissionControlSequenceTargetSequence" = None
        targSeqOuter = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        targSeqInner: "IMissionControlSequenceTargetSequence" = None
        targSeqInner = clr.Convert(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        diffCorrOuter: "IProfileDifferentialCorrector" = None
        diffCorrOuter = clr.Convert(targSeqOuter.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        diffCorrInner: "IProfileDifferentialCorrector" = None
        diffCorrInner = clr.Convert(targSeqInner.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        dcScriptTool: "IScriptingTool" = diffCorrInner.scripting_tool
        dcScriptTool.enable = True

        dcParam: "IScriptingParameter" = dcScriptTool.parameters.add("Parameter")
        dcParam2: "IScriptingParameter" = dcScriptTool.parameters.add("ParameterNowWithMoreChars")

    # endregion

    # region SimilarNamesStayEnabled
    def test_SimilarNamesStayEnabled(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "IMissionControlSequenceTargetSequence" = None
        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        durationControl: "IStoppingConditionElement" = prop.stopping_conditions["Duration"]

        duration2Control: "IStoppingConditionElement" = prop.stopping_conditions.add("Duration")

        durationControl.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)
        duration2Control.enable_control_parameter(CONTROL_STOPPING_CONDITION.TRIP_VALUE)

        durationResult: "IComponentInfo" = (clr.Convert(prop, IMissionControlSequenceSegment)).results.add(
            "Time/Duration"
        )
        duration2Result: "IComponentInfo" = (clr.Convert(prop, IMissionControlSequenceSegment)).results.add(
            "Time/Duration"
        )

        diffCorr: "IProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector)
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region NestedParameterStaysEnabledCutPaste
    def test_NestedParameterStaysEnabledCutPaste(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeqOuter: "IMissionControlSequenceTargetSequence" = None
        targSeqOuter = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        targSeqInner: "IMissionControlSequenceTargetSequence" = None
        targSeqInner = clr.Convert(
            targSeqOuter.segments.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeqInner.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        diffCorrOuter: "IProfileDifferentialCorrector" = None
        diffCorrOuter = clr.Convert(targSeqOuter.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        diffCorrInner: "IProfileDifferentialCorrector" = None
        diffCorrInner = clr.Convert(targSeqInner.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        dcScriptTool: "IScriptingTool" = diffCorrInner.scripting_tool
        dcScriptTool.enable = True

        dcParam: "IScriptingParameter" = dcScriptTool.parameters.add("Parameter")
        dcParam2: "IScriptingParameter" = dcScriptTool.parameters.add("ParameterNowWithMoreChars")
        EarlyBoundTests.m_driver.main_sequence.remove_all()

    # endregion

    # region MaintainSegmentLinkThroughCutPaste
    # Perhaps test 42791 also?
    def test_MaintainSegmentLinkThroughCutPaste(self):
        EarlyBoundTests.m_driver.main_sequence.remove_all()
        EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "InitialState", "-")

        targSeq: "IMissionControlSequenceTargetSequence" = None
        targSeq = clr.Convert(
            EarlyBoundTests.m_driver.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "TargetSequence", "-"),
            IMissionControlSequenceTargetSequence,
        )

        prop: "IMissionControlSequencePropagate" = None
        prop = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        prop2: "IMissionControlSequencePropagate" = None
        prop2 = clr.Convert(
            targSeq.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-"), IMissionControlSequencePropagate
        )

        result: "IComponentInfo" = (clr.Convert(prop2, IMissionControlSequenceSegment)).results.add(
            "Segments/Difference Across Segments"
        )
        (clr.Convert(result, IStateCalcDifferenceOtherSegment)).other_segment_name = "TargetSequence.Propagate"

        diffAcrossSegs: "IStoppingConditionElement" = prop2.stopping_conditions.add("UserSelect")

        (
            clr.Convert(diffAcrossSegs.properties, IStoppingCondition)
        ).user_calc_object_name = "Segments/Difference Across Segments"
        stopCondCalcObj: "IStateCalcDifferenceOtherSegment" = clr.Convert(
            (clr.Convert(diffAcrossSegs.properties, IStoppingCondition)).user_calc_object,
            IStateCalcDifferenceOtherSegment,
        )
        stopCondCalcObj.other_segment_name = "TargetSequence.Propagate"

        beforeCond: "IStoppingConditionElement" = (
            clr.Convert(diffAcrossSegs.properties, IStoppingCondition)
        ).before_conditions.add("UserSelect")
        (
            clr.Convert(beforeCond.properties, IStoppingCondition)
        ).user_calc_object_name = "Segments/Difference Across Segments"
        beforeCondCalcObj: "IStateCalcDifferenceOtherSegment" = clr.Convert(
            (clr.Convert(beforeCond.properties, IStoppingCondition)).user_calc_object, IStateCalcDifferenceOtherSegment
        )
        beforeCondCalcObj.other_segment_name = "TargetSequence.Propagate"

        constraint: "IAsTriggerCondition" = clr.Convert(
            (clr.Convert(diffAcrossSegs.properties, IStoppingCondition)).constraints.add("UserDefined"),
            IAsTriggerCondition,
        )

        constraint.calc_object_name = "Segments/Difference Across Segments"
        (
            clr.Convert(constraint.calc_object, IStateCalcDifferenceOtherSegment)
        ).other_segment_name = "TargetSequence.Propagate"

        diffCorr: "IProfileDifferentialCorrector" = None
        diffCorr = clr.Convert(targSeq.profiles["Differential Corrector"], IProfileDifferentialCorrector)

        dcScriptTool: "IScriptingTool" = diffCorr.scripting_tool
        dcScriptTool.enable = True

        dcAttr: "IScriptingSegment" = dcScriptTool.segment_properties.add("Attribute")
        dcAttr.object_name = "Propagate"
        dcCalcObjWrap: "IScriptingCalcObject" = dcScriptTool.calc_objects.add("CalcObject")
        dcCalcObjWrap.calc_object_name = "Segments/Difference Across Segments"
        dcDiffOtherSegment: "IStateCalcDifferenceOtherSegment" = clr.Convert(
            dcCalcObjWrap.calc_object, IStateCalcDifferenceOtherSegment
        )
        dcDiffOtherSegment.other_segment_name = "TargetSequence.Propagate"

    # endregion
