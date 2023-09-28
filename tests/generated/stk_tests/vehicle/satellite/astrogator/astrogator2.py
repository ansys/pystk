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

        # The commented section should be converted to test SNOPT/IPOPT once OM is hooked up for them (ENG96768)
        # At present they are both supported for 64 bit, but not on Linux.
        # if (!OSHelper.Is64Bit() && !OSHelper.IsLinux())
        # {
        #    // DEOptimizer not available on x64/linux yet

        #    IAgVAProfileDEOptimizer optimizer =
        #        (IAgVAProfileDEOptimizer)targSeq.Profiles.Add("Design Explorer Optimizer");
        #    IAgVADEResult optEqConst =
        #        (IAgVADEResult)optimizer.Results.
        #        GetResultByPaths("TargetSequence.Propagate", "Inclination");
        #    optEqConst.Enable = true;

        #    targSeq2.Segments.Cut("Propagate");
        #    m_driver.MainSequence.Insert(SEGMENT_TYPE.eVASegmentTypePropagate,
        #        "Propagate", "-");
        #    targSeq2.Segments.Paste("-");

        #    result = (IComponentInfo)targSeq2.Segments["Propagate"].Results["Inclination"];
        #    result.Name = "NewName";

        #    dcEqConst = (IDifferentialCorrectorResult)diffCorr.Results.
        #        GetResultByPaths("TargetSequence.Propagate", "NewName");

        #    optEqConst = (IAgVADEResult)optimizer.Results.
        #        GetResultByPaths("TargetSequence.Propagate", "NewName");
        #    Assert.IsTrue(dcEqConst.Enable);
        #    Assert.IsTrue(optEqConst.Enable);
        # }

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

        # The commented section should be converted to test SNOPT/IPOPT once OM is hooked up for them (ENG96768)
        # At present they are both supported for 64 bit, but not on Linux.
        # if (!OSHelper.Is64Bit() && !OSHelper.IsLinux())
        # {
        #    // DEOptimizer not available on x64/linux yet

        #    IAgVAProfileDEOptimizer optimizer = null;
        #    optimizer = (IAgVAProfileDEOptimizer)targSeq.Profiles.Add("Design Explorer Optimizer");

        #    IScriptingSegment optAttr = null;
        #    optimizer.ScriptingTool.Enable = true;
        #    optAttr = optimizer.ScriptingTool.SegmentProperties.Add("Attribute");
        #    optAttr.ObjectName = "Propagate";

        #    targSeq.Segments.Cut("Propagate");

        #    m_driver.MainSequence.Insert(SEGMENT_TYPE.eVASegmentTypePropagate, "Propagate", "-");

        #    targSeq.Segments.Paste("-");
        #    prop = (IMissionControlSequencePropagate)targSeq.Segments["Propagate"];
        #    ((IComponentInfo)prop).Name = "RenamedPropagate";

        #    Assert.AreEqual("RenamedPropagate", optAttr.SegmentName);
        #    Assert.AreEqual("RenamedPropagate", attribute.SegmentName);
        #    Assert.AreEqual("RenamedPropagate", changeStopCondition.SegmentName);
        #    Assert.AreEqual("RenamedPropagate", changeProp.SegmentName);
        #    Assert.AreEqual("RenamedPropagate", dcAttribute.SegmentName);

        #    targSeq.Segments.Cut("Maneuver");

        #    m_driver.MainSequence.Insert(SEGMENT_TYPE.eVASegmentTypeManeuver, "Maneuver", "-");

        #    targSeq.Segments.Paste("-");
        #    man = (IMissionControlSequenceManeuver)targSeq.Segments["Maneuver"];
        #    ((IComponentInfo)man).Name = "RenamedManeuver";

        #    Assert.AreEqual("RenamedManeuver", changeStopConditionMan.SegmentName);
        #    Assert.AreEqual("RenamedManeuver", changePropMan.SegmentName);

        #    sequence.Segments.Cut("Propagate");
        #    m_driver.MainSequence.Insert(SEGMENT_TYPE.eVASegmentTypePropagate, "Propagate", "-");
        #    propInsideSequence = (IMissionControlSequencePropagate)sequence.Segments.Paste("-");
        #    ((IComponentInfo)propInsideSequence).Name = "RenamedPropagate";

        #    Assert.AreEqual("RenamedPropagate", seqAttr.SegmentName);

        #    targSeq.Segments.Cut("Return");
        #    m_driver.MainSequence.Insert(SEGMENT_TYPE.eVASegmentTypeReturn, "Return", "-");
        #    ret = (IMissionControlSequenceReturn)targSeq.Segments.Paste("-");
        #    ((IComponentInfo)ret).Name = "RenamedReturn";

        #    Assert.AreEqual("RenamedReturn", changeReturn.SegmentName);

        #    targSeq.Segments.Cut("Stop");
        #    m_driver.MainSequence.Insert(SEGMENT_TYPE.eVASegmentTypeStop, "Stop", "-");
        #    stop = (IMissionControlSequenceStop)targSeq.Segments.Paste("-");
        #    ((IComponentInfo)stop).Name = "RenamedStop";

        #    Assert.AreEqual("RenamedStop", changeStopSegment.SegmentName);
        # }

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

        # The commented section should be converted to test SNOPT/IPOPT once OM is hooked up for them (ENG96768)
        # At present they are both supported for 64 bit, but not on Linux.
        # if (!OSHelper.Is64Bit() && !OSHelper.IsLinux())
        # {
        #    // DEOptimizer not available on x64/linux yet

        #    IAgVAProfileDEOptimizer optimizer = null;
        #    optimizer = (IAgVAProfileDEOptimizer)targSeq.Profiles.Add("Design Explorer Optimizer");

        #    IScriptingSegment optAttr = null;
        #    optimizer.ScriptingTool.Enable = true;
        #    optAttr = optimizer.ScriptingTool.SegmentProperties.Add("Attribute");
        #    optAttr.ObjectName = "Sequence.Propagate";

        #    //moving inside and out of a nested sequence

        #    sequence.Segments.Cut("Propagate");

        #    targSeq.Segments.Paste("-");

        #    Assert.AreEqual("Propagate", optAttr.SegmentName);
        #    Assert.AreEqual("Propagate", attribute.SegmentName);
        #    Assert.AreEqual("Propagate", changeStopCondition.SegmentName);
        #    Assert.AreEqual("Propagate", changeProp.SegmentName);
        #    Assert.AreEqual("Propagate", dcAttribute.SegmentName);

        #    targSeq.Segments.Cut("Propagate");

        #    sequence.Segments.Paste("-");

        #    Assert.AreEqual("Sequence.Propagate", optAttr.SegmentName);
        #    Assert.AreEqual("Sequence.Propagate", attribute.SegmentName);
        #    Assert.AreEqual("Sequence.Propagate", changeStopCondition.SegmentName);
        #    Assert.AreEqual("Sequence.Propagate", changeProp.SegmentName);
        #    Assert.AreEqual("Sequence.Propagate", dcAttribute.SegmentName);

        #    sequence.Segments.Cut("Maneuver");

        #    targSeq.Segments.Paste("-");

        #    Assert.AreEqual("Maneuver", changeStopConditionMan.SegmentName);
        #    Assert.AreEqual("Maneuver", changePropMan.SegmentName);

        #    targSeq.Segments.Cut("Maneuver");

        #    sequence.Segments.Paste("-");

        #    Assert.AreEqual("Sequence.Maneuver", changeStopConditionMan.SegmentName);
        #    Assert.AreEqual("Sequence.Maneuver", changePropMan.SegmentName);

        #    sequence.Segments.Cut("Return");
        #    targSeq.Segments.Paste("-");

        #    Assert.AreEqual("Return", changeReturn.SegmentName);

        #    targSeq.Segments.Cut("Return");
        #    sequence.Segments.Paste("-");

        #    Assert.AreEqual("Sequence.Return", changeReturn.SegmentName);

        #    sequence.Segments.Cut("Stop");
        #    targSeq.Segments.Paste("-");

        #    Assert.AreEqual("Stop", changeStopSegment.SegmentName);

        #    targSeq.Segments.Cut("Stop");
        #    sequence.Segments.Paste("-");

        #    Assert.AreEqual("Sequence.Stop", changeStopSegment.SegmentName);

        #    //testing to make sure that the link follows through a paste causing a rename
        #    // i.e. segment ->segment1

        #    sequence.Segments.Cut("Propagate");
        #    targSeq.Segments.Insert(SEGMENT_TYPE.eVASegmentTypePropagate, "Propagate", "-");
        #    targSeq.Segments.Paste("-");

        #    Assert.AreEqual("Propagate1", optAttr.SegmentName);
        #    Assert.AreEqual("Propagate1", attribute.SegmentName);
        #    Assert.AreEqual("Propagate1", changeStopCondition.SegmentName);
        #    Assert.AreEqual("Propagate1", changeProp.SegmentName);
        #    Assert.AreEqual("Propagate1", dcAttribute.SegmentName);

        #    sequence.Segments.Cut("Maneuver");
        #    targSeq.Segments.Insert(SEGMENT_TYPE.eVASegmentTypeManeuver, "Maneuver", "-");
        #    targSeq.Segments.Paste("-");

        #    Assert.AreEqual("Maneuver1", changeStopConditionMan.SegmentName);
        #    Assert.AreEqual("Maneuver1", changePropMan.SegmentName);

        #    sequence.Segments.Cut("Return");
        #    targSeq.Segments.Insert(SEGMENT_TYPE.eVASegmentTypeReturn, "Return", "-");
        #    targSeq.Segments.Paste("-");

        #    Assert.AreEqual("Return1", changeReturn.SegmentName);

        #    sequence.Segments.Cut("Stop");
        #    targSeq.Segments.Insert(SEGMENT_TYPE.eVASegmentTypeStop, "Stop", "-");
        #    targSeq.Segments.Paste("-");

        #    Assert.AreEqual("Stop1", changeStopSegment.SegmentName);
        # }

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

        # The commented section should be converted to test SNOPT/IPOPT once OM is hooked up for them (ENG96768)
        # At present they are both supported for 64 bit, but not on Linux.
        # if (!OSHelper.Is64Bit() && !OSHelper.IsLinux())
        # {
        #    // DEOptimizer not available on x64/linux yet

        #    IAgVAProfileDEOptimizer optimizer = null;
        #    optimizer = (IAgVAProfileDEOptimizer)targSeq.Profiles.Add("Design Explorer Optimizer");

        #    IScriptingSegment optAttr = null;
        #    optimizer.ScriptingTool.Enable = true;
        #    optAttr = optimizer.ScriptingTool.SegmentProperties.Add("Attribute");
        #    optAttr.ObjectName = "Propagate";

        #    ((IComponentInfo)prop).Name = "RenamedProp";
        #    ((IComponentInfo)man).Name = "RenamedMan";
        #    ((IComponentInfo)ret).Name = "RenamedReturn";
        #    ((IComponentInfo)stop).Name = "RenamedStop";

        #    targSeq.Segments.Cut("RenamedProp");
        #    targSeq.Segments.Paste("-");
        #    targSeq.Segments.Cut("RenamedMan");
        #    targSeq.Segments.Paste("-");
        #    targSeq.Segments.Cut("RenamedReturn");
        #    targSeq.Segments.Paste("-");
        #    targSeq.Segments.Cut("RenamedStop");
        #    targSeq.Segments.Paste("-");

        #    IMissionControlSequenceTargetSequence targSeq2 = (IMissionControlSequenceTargetSequence)m_driver.MainSequence.InsertCopy((IMissionControlSequenceSegment)targSeq, "-");
        #    IMissionControlSequencePropagate prop2 = (IMissionControlSequencePropagate)targSeq2.Segments["RenamedProp"];
        #    IMissionControlSequenceManeuver man2 = (IMissionControlSequenceManeuver)targSeq2.Segments["RenamedMan"];
        #    IMissionControlSequenceReturn return2 = (IMissionControlSequenceReturn)targSeq2.Segments["RenamedReturn"];
        #    IMissionControlSequenceStop stop2 = (IMissionControlSequenceStop)targSeq2.Segments["RenamedStop"];

        #    ((IComponentInfo)prop2).Name = "Propagate";
        #    ((IComponentInfo)man2).Name = "Maneuver";
        #    ((IComponentInfo)return2).Name = "Return";
        #    ((IComponentInfo)stop2).Name = "Stop";

        #    targSeq2.Segments.Cut("Propagate");
        #    prop2 = (IMissionControlSequencePropagate)targSeq2.Segments.Paste("-");
        #    targSeq2.Segments.Cut("Maneuver");
        #    man2 = (IMissionControlSequenceManeuver)targSeq2.Segments.Paste("-");
        #    targSeq2.Segments.Cut("Return");
        #    return2 = (IMissionControlSequenceReturn)targSeq2.Segments.Paste("-");
        #    targSeq2.Segments.Cut("Stop");
        #    stop2 = (IMissionControlSequenceStop)targSeq2.Segments.Paste("-");

        #    ((IComponentInfo)prop2).Name = "Propagate2";
        #    ((IComponentInfo)man2).Name = "Maneuver2";
        #    ((IComponentInfo)return2).Name = "Return2";
        #    ((IComponentInfo)stop2).Name = "Stop2";

        #    IProfileDifferentialCorrector diffCorr2 = null;
        #    diffCorr2 = (IProfileDifferentialCorrector)targSeq2.Profiles["Differential Corrector"];

        #    IScriptingTool dcScriptTool2 = diffCorr2.ScriptingTool;
        #    IScriptingSegment dcAttribute2 = dcScriptTool2.SegmentProperties["Attribute"];

        #    IProfileChangeManeuverType changeMan2 = null;
        #    changeMan2 = (IProfileChangeManeuverType)targSeq2.Profiles["MyChangeManeuver"];

        #    IProfileChangePropagator changeProp2 = null;
        #    changeProp2 = (IProfileChangePropagator)targSeq2.Profiles["MyChangePropagator"];

        #    IProfileChangePropagator changePropMan2 = null;
        #    changePropMan2 = (IProfileChangePropagator)targSeq2.Profiles["MyChangePropagatorForManeuver"];

        #    IProfileChangeReturnSegment changeReturn2 = null;
        #    changeReturn2 = (IProfileChangeReturnSegment)targSeq2.Profiles["MyReturn"];

        #    IProfileChangeStoppingConditionState changeStopCondition2 = null;
        #    changeStopCondition2 = (IProfileChangeStoppingConditionState)targSeq2.Profiles["MyChangeStopCondForPropagate"];

        #    IProfileChangeStoppingConditionState changeStopConditionMan2 = null;
        #    changeStopConditionMan2 = (IProfileChangeStoppingConditionState)targSeq2.Profiles["MyChangeStopCondForMan"];

        #    IProfileChangeStopSegment changeStopSegment2 = null;
        #    changeStopSegment2 = (IProfileChangeStopSegment)targSeq2.Profiles["MyChangeStopSegment"];

        #    IProfileScriptingTool scriptingTool2 = null;
        #    scriptingTool2 = (IProfileScriptingTool)targSeq2.Profiles["Scripting Tool"];

        #    IScriptingSegment attribute2 = scriptingTool2.SegmentProperties["Attribute"];

        #    IAgVAProfileDEOptimizer optimizer2 = null;
        #    optimizer2 = (IAgVAProfileDEOptimizer)targSeq2.Profiles["Design Explorer Optimizer"];

        #    IScriptingSegment optAttr2 = null;
        #    optAttr2 = optimizer2.ScriptingTool.SegmentProperties["Attribute"];

        #    Assert.AreEqual("Propagate2", optAttr2.SegmentName);
        #    Assert.AreEqual("Propagate2", attribute2.SegmentName);
        #    Assert.AreEqual("Propagate2", changeStopCondition2.SegmentName);
        #    Assert.AreEqual("Propagate2", changeProp2.SegmentName);
        #    Assert.AreEqual("Propagate2", dcAttribute2.SegmentName);

        #    Assert.AreEqual("Maneuver2", changeStopConditionMan2.SegmentName);
        #    Assert.AreEqual("Maneuver2", changePropMan2.SegmentName);

        #    Assert.AreEqual("Return2", changeReturn2.SegmentName);

        #    Assert.AreEqual("Stop2", changeStopSegment2.SegmentName);
        # }

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

        # The commented section should be converted to test SNOPT/IPOPT once OM is hooked up for them (ENG96768)
        # At present they are both supported for 64 bit, but not on Linux.
        # if (!OSHelper.Is64Bit() && !OSHelper.IsLinux())
        # {
        #    // DEOptimizer not available on x64/linux yet

        #    IAgVAProfileDEOptimizer optimizer = null;
        #    optimizer = (IAgVAProfileDEOptimizer)targSeqOuter.Profiles.Add("Design Explorer Optimizer");

        #    IScriptingSegment optAttr = null;
        #    optimizer.ScriptingTool.Enable = true;
        #    optAttr = optimizer.ScriptingTool.SegmentProperties.Add("Attribute");
        #    optAttr.ObjectName = "Sequence.Propagate";

        #    targSeqOuter.Segments.Cut("Sequence");
        #    sequence = (IMissionControlSequenceSequence)targSeqOuter.Segments.Paste("-");
        #    ((IComponentInfo)sequence).Name = "RenamedSequence";

        #    Assert.AreEqual("RenamedSequence.Propagate", optAttr.SegmentName);
        #    Assert.AreEqual("RenamedSequence.Propagate", attribute.SegmentName);
        #    Assert.AreEqual("RenamedSequence.Propagate", changeStopCondition.SegmentName);
        #    Assert.AreEqual("RenamedSequence.Propagate", changeProp.SegmentName);
        #    Assert.AreEqual("RenamedSequence.Propagate", dcAttribute.SegmentName);

        #    Assert.AreEqual("RenamedSequence.Maneuver", changeStopConditionMan.SegmentName);
        #    Assert.AreEqual("RenamedSequence.Maneuver", changePropMan.SegmentName);

        #    Assert.AreEqual("RenamedSequence.Return", changeReturn.SegmentName);

        #    Assert.AreEqual("RenamedSequence.Stop", changeStopSegment.SegmentName);

        #    dcAttribute.ObjectName = "Target_Sequence.Propagate";
        #    changeMan.Segment = man2;
        #    changeProp.SegmentName = "Target_Sequence.Propagate";
        #    changePropMan.SegmentName = "Target_Sequence.Maneuver";
        #    changeReturn.SegmentName = "Target_Sequence.Return";
        #    changeStopCondition.SegmentName = "Target_Sequence.Propagate";
        #    changeStopConditionMan.SegmentName = "Target_Sequence.Maneuver";
        #    changeStopSegment.SegmentName = "Target_Sequence.Stop";
        #    attribute.ObjectName = "Target_Sequence.Propagate";
        #    optAttr.ObjectName = "Target_Sequence.Propagate";

        #    targSeqOuter.Segments.Cut("Target_Sequence");
        #    targSeqInner = (IMissionControlSequenceTargetSequence)targSeqOuter.Segments.Paste("-");
        #    ((IComponentInfo)targSeqInner).Name = "RenamedTargetSequence";

        #    Assert.AreEqual("RenamedTargetSequence.Propagate", optAttr.SegmentName);
        #    Assert.AreEqual("RenamedTargetSequence.Propagate", attribute.SegmentName);
        #    Assert.AreEqual("RenamedTargetSequence.Propagate", changeStopCondition.SegmentName);
        #    Assert.AreEqual("RenamedTargetSequence.Propagate", changeProp.SegmentName);
        #    Assert.AreEqual("RenamedTargetSequence.Propagate", dcAttribute.SegmentName);

        #    Assert.AreEqual("RenamedTargetSequence.Maneuver", changeStopConditionMan.SegmentName);
        #    Assert.AreEqual("RenamedTargetSequence.Maneuver", changePropMan.SegmentName);

        #    Assert.AreEqual("RenamedTargetSequence.Return", changeReturn.SegmentName);

        #    Assert.AreEqual("RenamedTargetSequence.Stop", changeStopSegment.SegmentName);
        # }

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

        # The commented section should be converted to test SNOPT/IPOPT once OM is hooked up for them (ENG96768)
        # At present they are both supported for 64 bit, but not on Linux.
        # if (!OSHelper.Is64Bit() && !OSHelper.IsLinux())
        # {
        #    // DEOptimizer not available on x64/linux yet

        #    IAgVAProfileDEOptimizer optimizer = null;
        #    optimizer = (IAgVAProfileDEOptimizer)targSeq.Profiles.Add("Design Explorer Optimizer");

        #    IDifferentialCorrectorControl dcControl1 = null;
        #    IDifferentialCorrectorControl dcControl2 = null;
        #    IDifferentialCorrectorResult dcResult1 = null;
        #    IDifferentialCorrectorResult dcResult2 = null;

        #    dcControl1 = diffCorr.ControlParameters.GetControlByPaths("Propagate", "StoppingConditions.Duration.TripValue");
        #    dcControl1.Enable = true;
        #    dcControl2 = diffCorr.ControlParameters.GetControlByPaths("Propagate", "StoppingConditions.Duration1.TripValue");
        #    dcControl2.Enable = true;
        #    dcResult1 = diffCorr.Results.GetResultByPaths("Propagate", "Duration");
        #    dcResult1.Enable = true;
        #    dcResult2 = diffCorr.Results.GetResultByPaths("Propagate", "Duration1");
        #    dcResult2.Enable = true;

        #    IAgVADEControl optControl1 = null;
        #    IAgVADEControl optControl2 = null;
        #    IAgVADEResult optResult1 = null;
        #    IAgVADEResult optResult2 = null;

        #    optControl1 = optimizer.ControlParameters.GetControlByPaths("Propagate", "StoppingConditions.Duration.TripValue");
        #    optControl1.Enable = true;
        #    optControl2 = optimizer.ControlParameters.GetControlByPaths("Propagate", "StoppingConditions.Duration1.TripValue");
        #    optControl2.Enable = true;
        #    optResult1 = optimizer.Results.GetResultByPaths("Propagate", "Duration");
        #    optResult1.Enable = true;
        #    optResult2 = optimizer.Results.GetResultByPaths("Propagate", "Duration1");
        #    optResult2.Enable = true;

        #    ((IComponentInfo)durationControl).Name = "DurationRename";
        #    durationResult.Name = "DurationRename";

        #    Assert.IsTrue(dcControl1.Enable);
        #    Assert.IsTrue(dcControl2.Enable);
        #    Assert.IsTrue(dcResult1.Enable);
        #    Assert.IsTrue(dcResult2.Enable);
        #    Assert.IsTrue(optControl1.Enable);
        #    Assert.IsTrue(optControl2.Enable);
        #    Assert.IsTrue(optResult1.Enable);
        #    Assert.IsTrue(optResult2.Enable);

        #    Assert.AreEqual("StoppingConditions.DurationRename.TripValue", dcControl1.Name);
        #    Assert.AreEqual("StoppingConditions.Duration1.TripValue", dcControl2.Name);
        #    Assert.AreEqual("DurationRename", dcResult1.Name);
        #    Assert.AreEqual("Duration1", dcResult2.Name);
        #    Assert.AreEqual("StoppingConditions.DurationRename.TripValue", optControl1.Name);
        #    Assert.AreEqual("StoppingConditions.Duration1.TripValue", optControl2.Name);
        #    Assert.AreEqual("DurationRename", optResult1.Name);
        #    Assert.AreEqual("Duration1", optResult2.Name);
        # }

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

        # The commented section should be converted to test SNOPT/IPOPT once OM is hooked up for them (ENG96768)
        # At present they are both supported for 64 bit, but not on Linux.
        # if (!OSHelper.Is64Bit() && !OSHelper.IsLinux())
        # {
        #    // DEOptimizer not available on x64/linux yet

        #    IAgVAProfileDEOptimizer optimizer = null;
        #    optimizer = (IAgVAProfileDEOptimizer)targSeqInner.Profiles.Add("Design Explorer Optimizer");
        #    IScriptingTool optScriptTool = optimizer.ScriptingTool;
        #    optScriptTool.Enable = true;

        #    IScriptingParameter optParam = optScriptTool.Parameters.Add("Parameter");
        #    IScriptingParameter optParam2 = optScriptTool.Parameters.Add("ParameterNowWithMoreChars");

        #    IProfileScriptingTool scriptTool = (IProfileScriptingTool)targSeqInner.Profiles.Add("Scripting Tool");
        #    IScriptingParameter scriptToolParam = scriptTool.Parameters.Add("Parameter");
        #    IScriptingParameter scriptToolParam2 = scriptTool.Parameters.Add("ParameterNowWithMoreChars");

        #    IDifferentialCorrectorControl outerControl1 = diffCorrOuter.ControlParameters.GetControlByPaths(
        #        "TargetSequence.Differential_Corrector.Scripting_Tool",
        #        "Parameter");
        #    outerControl1.Enable = true;

        #    IDifferentialCorrectorControl outerControl2 = diffCorrOuter.ControlParameters.GetControlByPaths(
        #        "TargetSequence.Scripting_Tool",
        #        "Parameter");
        #    outerControl2.Enable = true;

        #    IDifferentialCorrectorControl outerControl3 = diffCorrOuter.ControlParameters.GetControlByPaths(
        #        "TargetSequence.Design_Explorer_Optimizer.Scripting_Tool",
        #        "Parameter");
        #    outerControl3.Enable = true;

        #    dcParam.Name = "RenamedParam";
        #    optParam.Name = "RenamedParam";
        #    scriptToolParam.Name = "RenamedParam";

        #    targSeqOuter.Segments.Cut("TargetSequence");
        #    targSeqOuter.Segments.Paste("-");

        #    Assert.IsTrue(outerControl1.Enable);
        #    Assert.IsTrue(outerControl2.Enable);
        #    Assert.IsTrue(outerControl3.Enable);

        #    IMissionControlSequenceTargetSequence newTargSeq = (IMissionControlSequenceTargetSequence)
        #        m_driver.MainSequence.InsertCopy((IMissionControlSequenceSegment)targSeqOuter, "-");
        #    IProfileDifferentialCorrector newDiffCorrOuter = (IProfileDifferentialCorrector)
        #        newTargSeq.Profiles["Differential Corrector"];

        #    IDifferentialCorrectorControl newOuterControl1 = newDiffCorrOuter.ControlParameters.GetControlByPaths(
        #        "TargetSequence.Differential_Corrector.Scripting_Tool",
        #        "RenamedParam");
        #    IDifferentialCorrectorControl newOuterControl2 = newDiffCorrOuter.ControlParameters.GetControlByPaths(
        #        "TargetSequence.Scripting_Tool",
        #        "RenamedParam");
        #    IDifferentialCorrectorControl newOuterControl3 = newDiffCorrOuter.ControlParameters.GetControlByPaths(
        #        "TargetSequence.Design_Explorer_Optimizer.Scripting_Tool",
        #        "RenamedParam");

        #    Assert.IsTrue(newOuterControl1.Enable);
        #    Assert.IsTrue(newOuterControl2.Enable);
        #    Assert.IsTrue(newOuterControl3.Enable);
        # }

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
