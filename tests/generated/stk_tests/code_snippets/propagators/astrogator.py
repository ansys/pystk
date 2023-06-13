from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *


class Astrogator(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Astrogator, self).__init__(*args, **kwargs)

    m_Satellite: "ISatellite" = None
    m_Object: "IDriverMissionControlSequence" = None
    m_DefaultName: str = "MyAstrogator"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        Astrogator.m_Satellite = clr.Convert(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eSatellite, Astrogator.m_DefaultName
            ),
            ISatellite,
        )
        Astrogator.m_Satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorAstrogator)
        Astrogator.m_Object = clr.CastAs(Astrogator.m_Satellite.Propagator, IDriverMissionControlSequence)
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        (clr.Convert(Astrogator.m_Satellite, IStkObject)).Unload()
        Astrogator.m_Object = None

    # endregion

    # region ConfigureAstrogratorPropagator
    def test_ConfigureAstrogratorPropagator(self):
        self.ConfigureAstrogratorPropagator(Astrogator.m_Satellite)

    def ConfigureAstrogratorPropagator(self, satellite: "ISatellite"):
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorAstrogator)

        driver = clr.CastAs(satellite.Propagator, IDriverMissionControlSequence)

        # Remove if necessary
        driver.MainSequence.RemoveAll()

        # Configure properties as necessarily
        driver.Options.DrawTrajectoryIn3D = True
        driver.Options.GraphicsUpdateRate = 0.9
        driver.Options.UpdateAnimationTimeForAllObjects = False
        driver.Options.StoppingConditionTimeTolerance = 5e-08
        driver.Options.EnableLogging = True

    # endregion

    # region ConfigureInitialStateSegment
    def test_ConfigureInitialStateSegment(self):
        self.ConfigureInitialStateSegment(Astrogator.m_Object)

    def ConfigureInitialStateSegment(self, driver: "IDriverMissionControlSequence"):
        # Add a new segment and cast the segment to the IAgVAMCSInitialState interface
        segment = driver.MainSequence.Insert(AgEVASegmentType.eVASegmentTypeInitialState, "Inner Orbit", "-")
        initState = clr.CastAs(segment, IMissionControlSequenceInitialState)

        initState.CoordSystemName = "CentralBody/Earth Fixed"
        initState.OrbitEpoch = "1 Jan 2012 12:00:00.000"

        # Set element type and cast the Element property to the appropriate interface
        # configure the element as necessary
        initState.SetElementType(AgEVAElementType.eVAElementTypeCartesian)
        cartesian = clr.CastAs(initState.Element, IElementCartesian)
        cartesian.Vx = 8051.21
        cartesian.Y = 55
        cartesian.Z = 0
        cartesian.Vx = 0.45
        cartesian.Vy = 8.10158
        cartesian.Vz = 3.51009

        # Configure fuel tank if necessary
        initState.FuelTank.FuelDensity = 1001
        initState.FuelTank.FuelMass = 501
        initState.FuelTank.TankPressure = 5001
        initState.FuelTank.TankTemperature = 292

        # Configure spacecraft parameters
        initState.SpacecraftParameters.Cd = 2.3
        initState.SpacecraftParameters.Ck = 1.1
        initState.SpacecraftParameters.Cr = 1.3
        initState.SpacecraftParameters.DragArea = 21
        initState.SpacecraftParameters.DryMass = 501
        initState.SpacecraftParameters.K1 = 2
        initState.SpacecraftParameters.K2 = 3
        initState.SpacecraftParameters.RadiationPressureArea = 23.0
        initState.SpacecraftParameters.SolarRadiationPressureArea = 22.0

    # endregion

    # region ConfigurePropagateSegment
    def test_ConfigurePropagateSegment(self):
        self.ConfigurePropagateSegment(Astrogator.m_Object)

    def ConfigurePropagateSegment(self, driver: "IDriverMissionControlSequence"):
        # Add a propagate segment to our sequence
        segment = driver.MainSequence.Insert(AgEVASegmentType.eVASegmentTypePropagate, "Propagate", "-")
        propagate = clr.CastAs(segment, IMissionControlSequencePropagate)
        propagate.PropagatorName = "Earth Point Mass"

        # Configure propagtor advanced properties
        propagate.MinPropagationTime = 0
        propagate.EnableMaxPropagationTime = True
        propagate.MaxPropagationTime = 72000000
        propagate.EnableWarningMessage = True

        # Configure stopping conditions
        duration = clr.CastAs(propagate.StoppingConditions["Duration"].Properties, IStoppingCondition)
        duration.Trip = 7200
        duration.Tolerance = 1e-05

        # Add any addition stopping conditions
        lightning = clr.CastAs(propagate.StoppingConditions.Add("Lighting"), IStoppingCondition)

    # endregion

    # region ConfigureTargetSequenceSegment
    def test_ConfigureTargetSequenceSegment(self):
        self.ConfigureTargetSequenceSegment(Astrogator.m_Object)

    def ConfigureTargetSequenceSegment(self, driver: "IDriverMissionControlSequence"):
        # First add a sequence target
        segment = driver.MainSequence.Insert(AgEVASegmentType.eVASegmentTypeTargetSequence, "Start Transfer", "-")
        targetSequence = clr.CastAs(segment, IMissionControlSequenceTargetSequence)

        targetSequence.Action = AgEVATargetSeqAction.eVATargetSeqActionRunActiveProfiles
        targetSequence.WhenProfilesFinish = AgEVAProfilesFinish.eVAProfilesFinishRunToReturnAndContinue
        targetSequence.ContinueOnFailure = False

        # Add as many child segments to target
        dv1 = clr.CastAs(
            targetSequence.Segments.Insert(AgEVASegmentType.eVASegmentTypeManeuver, "DV1", "-"),
            IMissionControlSequenceManeuver,
        )
        dv2 = clr.CastAs(
            targetSequence.Segments.Insert(AgEVASegmentType.eVASegmentTypeManeuver, "DV2", "-"),
            IMissionControlSequenceManeuver,
        )

        # Add more profiles if necessary
        profileName = "Change Maneuver Type"
        if Array.IndexOf(targetSequence.Profiles.AvailableProfiles, profileName) != -1:
            newProfile = targetSequence.Profiles.Add(profileName)

        # Enable controls
        dv1.EnableControlParameter(AgEVAControlManeuver.eVAControlManeuverImpulsiveCartesianX)
        dc = clr.CastAs(targetSequence.Profiles["Differential Corrector"], IProfileDifferentialCorrector)
        controlParam = dc.ControlParameters.GetControlByPaths("DV1", "ImpulsiveMnvr.Cartesian.X")
        controlParam.Enable = True
        controlParam.MaxStep = 0.3

        # Enable results
        (clr.Convert(dv1, IMissionControlSequenceSegment)).Results.Add("Epoch")
        roaResult = dc.Results.GetResultByPaths("DV1", "Epoch")
        roaResult.Enable = True

        # Confiure the differential corrector
        dc.MaxIterations = 50
        dc.EnableDisplayStatus = True
        dc.Mode = AgEVAProfileMode.eVAProfileModeIterate
        targetSequence.Action = AgEVATargetSeqAction.eVATargetSeqActionRunActiveProfiles

    # endregion

    # region ConfigureLaunchSegment
    def test_ConfigureLaunchSegment(self):
        self.ConfigureLaunchSegment(Astrogator.m_Object)

    def ConfigureLaunchSegment(self, driver: "IDriverMissionControlSequence"):
        # Add launch sequence and retrieve the
        segment = driver.MainSequence.Insert(AgEVASegmentType.eVASegmentTypeLaunch, "MyLaunch", "-")
        launch = clr.CastAs(segment, IMissionControlSequenceLaunch)

        # Configure launch properties
        launch.CentralBodyName = "Mars"
        launch.Epoch = "1 Jan 2012 12:00:00.000"
        launch.StepSize = 6
        launch.UsePreviousSegmentState = False
        launch.PreLaunchTime = 1
        launch.TimeOfFlight = 500
        launch.AscentType = AgEVAAscentType.eVAAscentTypeEllipseQuarticMotion
        launch.InitialAcceleration = 0.02

        # Configure display type
        launch.SetDisplaySystemType(AgEVALaunchDisplaySystem.eVADisplaySystemGeocentric)
        llr = clr.Convert(launch.DisplaySystem, IDisplaySystemGeocentric)
        llr.Latitude = 35.581
        llr.Longitude = -92.263
        llr.Radius = 1000

        # Configure launch type
        launch.AscentType = AgEVAAscentType.eVAAscentTypeEllipseQuarticMotion
        launch.InitialAcceleration = 0.02
        launch.AscentType = AgEVAAscentType.eVAAscentTypeEllipseCubicMotion

        # Configure burnout type
        velocity = launch.BurnoutVelocity
        velocity.BurnoutOption = AgEVABurnoutOptions.eVABurnoutOptionsInertialVelocity
        velocity.InertialVelocity = 20.0
        velocity.InertialHorizontalFPA = 22
        velocity.InertialVelocityAzimuth = 55
        velocity.BurnoutOption = AgEVABurnoutOptions.eVABurnoutOptionsFixedVelocity
        velocity.FixedVelocity = 20

    # endregion

    # region ConfigureUpdateSegment
    def test_ConfigureUpdateSegment(self):
        self.ConfigureUpdateSegment(Astrogator.m_Object)

    def ConfigureUpdateSegment(self, driver: "IDriverMissionControlSequence"):
        # Add launch sequence and retrieve the
        segment = driver.MainSequence.Insert(AgEVASegmentType.eVASegmentTypeUpdate, "MyUpdate", "-")
        update = clr.CastAs(segment, IMissionControlSequenceUpdate)

        # Specify the element to be changed, the action, and the value

        # Add values
        update.SetActionAndValue(AgEVAUpdateParam.eVAUpdateParamCd, AgEVAUpdateAction.eVAUpdateActionAddValue, 2)
        update.SetActionAndValue(
            AgEVAUpdateParam.eVAUpdateParamFuelDensity, AgEVAUpdateAction.eVAUpdateActionAddValue, 1
        )

        # Set to new value
        update.SetActionAndValue(
            AgEVAUpdateParam.eVAUpdateParamTankPressure, AgEVAUpdateAction.eVAUpdateActionSetToNewValue, 6000
        )
        update.SetActionAndValue(
            AgEVAUpdateParam.eVAUpdateParamTankTemp, AgEVAUpdateAction.eVAUpdateActionSetToNewValue, 5
        )

        # Subtract values
        update.SetActionAndValue(
            AgEVAUpdateParam.eVAUpdateParamSRPArea, AgEVAUpdateAction.eVAUpdateActionSubtractValue, 10
        )
        update.SetActionAndValue(
            AgEVAUpdateParam.eVAUpdateParamSRPArea, AgEVAUpdateAction.eVAUpdateActionSubtractValue, 1
        )

    # endregion

    # region ConfigureManeuverSegment
    def test_ConfigureManeuverSegment(self):
        self.ConfigureManeuverSegment(Astrogator.m_Object)

    def ConfigureManeuverSegment(self, driver: "IDriverMissionControlSequence"):
        # Add launch sequence and retrieve the IAgVAMCSManeuver interface
        segment = driver.MainSequence.Insert(AgEVASegmentType.eVASegmentTypeManeuver, "MyManeuver", "-")
        maneuver = clr.CastAs(segment, IMissionControlSequenceManeuver)

        # Set Maneuver to Impulsive
        maneuver.SetManeuverType(AgEVAManeuverType.eVAManeuverTypeImpulsive)
        impulse = clr.CastAs(maneuver.Maneuver, IManeuverImpulsive)

        # Set Impulsive attitude to VelocityVector
        impulse.SetAttitudeControlType(AgEVAAttitudeControl.eVAAttitudeControlVelocityVector)
        velVec = clr.CastAs(impulse.AttitudeControl, IAttitudeControlImpulsiveVelocityVector)
        velVec.DeltaVMagnitude = 1.0

        impulse.SetPropulsionMethod(AgEVAPropulsionMethod.eVAPropulsionMethodThrusterSet, "Thruster Set")
        impulse.UpdateMass = True

    # endregion

    # region ConfigureSequenceSegmentWithScriptingTool
    def test_ConfigureSequenceSegmentWithScriptingTool(self):
        self.ConfigureSequenceSegmentWithScriptingTool(Astrogator.m_Object)

    def ConfigureSequenceSegmentWithScriptingTool(self, driver: "IDriverMissionControlSequence"):
        # Add launch sequence and retrieve the
        segment = driver.MainSequence.Insert(AgEVASegmentType.eVASegmentTypeSequence, "MySequence", "-")
        sequence = clr.CastAs(segment, IMissionControlSequenceSequence)

        scriptTool = sequence.ScriptingTool
        scriptTool.Enable = True
        scriptTool.LanguageType = AgEVALanguage.eVALanguageVBScript
        scriptTool.ScriptText(
            r"""
            DeltaArg = dArg

            REM  Set the optimizers desired results
            DEOdArgUB = DeltaArg
            DEOdArgLB = DeltaArg


            REM  Initial guess tool:
            REM  Assume transfer orbit is something like a circular orbit linking apoapse of initial orbit to apoapse of final orbit
            REM  Constants: 
            mu = 398600
            pi = 3.14159265358979

            REM  Step 1:  propagate to apoapsis
            Prop1Dur = Period_0/2

            REM  Step 2:  conditions at end of initial orbit:
            SMA_0 = 0.5*(RadApo_0 + RadPeri_0)
            VelApo_0 = sqr( (RadPeri_0*mu) / (RadApo_0*SMA_0) )

            REM  Step 3:  evaluate properties of the circular transfer orbit
            Rcirc = RadApo_0
            Vcirc = sqr(mu/Rcirc)
            PeriodCirc = 2*pi*Sqr( Rcirc*Rcirc*Rcirc / mu)

            REM  Step 4:  set first maneuver to enter transfer orbit
            Burn1X = Vcirc - VelApo_0
            Burn1Z = 0

            REM  Step 5:  propagate along transfer orbit the desired change in argument of periapse
            If DeltaArg >= 0 Then
             TransferDur = PeriodCirc*(DeltaArg/360)
            Else 
             TransferDur = PeriodCirc*(360+DeltaArg)/360
            End If

            REM Step 6:  set second maneuver to enter desired final orbit
            Burn2X = -Burn1X
            Burn2Z = 0
            """
        )

        # Configure the script tool's segments

        burn1X = scriptTool.SegmentProperties.Add("Burn1X")
        if Array.IndexOf(burn1X.AvailableObjectNames, "Optimize_Delta_w.Burn1") != -1:
            burn1X.ObjectName = "Optimize_Delta_w.Burn1"
            burn1X.Attribute = "ImpulsiveMnvr.Cartesian.X"
            burn1X.Unit = "km/sec"

        period0 = scriptTool.CalcObjects.Add("Period_0")
        period0.CalcObjectName = "Segments/Value At Segment"
        valAtSeg = clr.CastAs(period0.CalcObject, IStateCalcValueAtSegment)
        valAtSeg.CalcObjectName = "Keplerian Elems/Orbit Period"

    # endregion

    # region ConfigureTargetSequenceWithDC
    def test_ConfigureTargetSequenceWithDC(self):
        Astrogator.m_Object.MainSequence.Insert(AgEVASegmentType.eVASegmentTypeTargetSequence, "Start Transfer", "-")
        self.ConfigureTargetSequenceWithDC(Astrogator.m_Object)

    def ConfigureTargetSequenceWithDC(self, driver: "IDriverMissionControlSequence"):
        startTransfer = clr.CastAs(driver.MainSequence["Start Transfer"], IMissionControlSequenceTargetSequence)

        dcString = "Differential Corrector"
        if Array.IndexOf(startTransfer.Profiles.AvailableProfiles, dcString) != -1:
            dc = clr.CastAs(startTransfer.Profiles.Add(dcString), IProfileDifferentialCorrector)

            # Configure differential corrector
            dc.ClearCorrectionsBeforeRun = True
            dc.ConvergenceCriteria = (
                AgEVAConvergenceCriteria.eVAConvervenceCriteriaEitherEqualityConstraintsOrControlParams
            )
            dc.EnableBPlaneNominal = False
            dc.EnableBPlanePerturbations = False
            dc.EnableDisplayStatus = True
            dc.EnableHomotopy = True
            dc.HomotopySteps = 2
            dc.EnableHomotopy = False
            dc.EnableLineSearch = True
            dc.LineSearchLowerBound = 0.001
            dc.LineSearchTolerance = 0.001
            dc.LineSearchUpperBound = 5.0
            dc.MaxLineSearchIterations = 5
            dc.MaxIterations = 20

            # Apply
            startTransfer.ApplyProfiles()

    # endregion

    # region SetUserDefinedMuValueOnThirdBody
    def test_SetUserDefinedMuValueOnThirdBody(self):
        self.SetUserDefinedMuValueOnThirdBody(clr.CastAs(TestBase.Application.CurrentScenario, IScenario))

    def SetUserDefinedMuValueOnThirdBody(self, scenario: "IScenario"):
        compInfoCol = scenario.ComponentDirectory.GetComponents(AgEComponent.eComponentAstrogator)
        thirdBodyFolder = compInfoCol.GetFolder("Propagator Functions").GetFolder("Third Bodies")
        newMoon = clr.CastAs(thirdBodyFolder.DuplicateComponent("Moon", "NewMoon"), IThirdBodyFunction)
        newMoon.SetModeType(AgEVAThirdBodyMode.eVAThirdBodyModePointMass)
        pointMass = clr.CastAs(newMoon.Mode, IPointMassFunction)
        pointMass.GravSource = AgEVAGravParamSource.eVAGravParamSourceUser
        pointMass.Mu = 390000.0

    # endregion

    # region SetUserDefinedMuValueOnThirdBodyFromPropagators
    def test_SetUserDefinedMuValueOnThirdBodyFromPropagators(self):
        self.SetUserDefinedMuValueOnThirdBodyFromPropagators(
            clr.CastAs(TestBase.Application.CurrentScenario, IScenario)
        )

    def SetUserDefinedMuValueOnThirdBodyFromPropagators(self, scenario: "IScenario"):
        compInfoCol = scenario.ComponentDirectory.GetComponents(AgEComponent.eComponentAstrogator)
        propagatorFolder = compInfoCol.GetFolder("Propagators")
        myEathHPOP = clr.CastAs(
            propagatorFolder.DuplicateComponent("Earth HPOP Default v10", "myEathHPOP"), INumericalPropagatorWrapper
        )
        moon = clr.CastAs(myEathHPOP.PropagatorFunctions["Moon"], IThirdBodyFunction)
        moon.SetModeType(AgEVAThirdBodyMode.eVAThirdBodyModePointMass)
        pointMass = clr.CastAs(moon.Mode, IPointMassFunction)
        pointMass.GravSource = AgEVAGravParamSource.eVAGravParamSourceUser
        pointMass.Mu = 390000.0

    # endregion
