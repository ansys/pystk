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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eSatellite, Astrogator.m_DefaultName
            ),
            ISatellite,
        )
        Astrogator.m_Satellite.set_propagator_type(AgEVePropagatorType.ePropagatorAstrogator)
        Astrogator.m_Object = clr.CastAs(Astrogator.m_Satellite.propagator, IDriverMissionControlSequence)
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        (clr.Convert(Astrogator.m_Satellite, IStkObject)).unload()
        Astrogator.m_Object = None

    # endregion

    # region ConfigureAstrogratorPropagator
    def test_ConfigureAstrogratorPropagator(self):
        self.ConfigureAstrogratorPropagator(Astrogator.m_Satellite)

    def ConfigureAstrogratorPropagator(self, satellite: "ISatellite"):
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorAstrogator)

        driver: "IDriverMissionControlSequence" = clr.CastAs(satellite.propagator, IDriverMissionControlSequence)

        # Remove if necessary
        driver.main_sequence.remove_all()

        # Configure properties as necessarily
        driver.options.draw_trajectory_in3_d = True
        driver.options.graphics_update_rate = 0.9
        driver.options.update_animation_time_for_all_objects = False
        driver.options.stopping_condition_time_tolerance = 5e-08
        driver.options.enable_logging = True

    # endregion

    # region ConfigureInitialStateSegment
    def test_ConfigureInitialStateSegment(self):
        self.ConfigureInitialStateSegment(Astrogator.m_Object)

    def ConfigureInitialStateSegment(self, driver: "IDriverMissionControlSequence"):
        # Add a new segment and cast the segment to the IMissionControlSequenceInitialState interface
        segment: "IMissionControlSequenceSegment" = driver.main_sequence.insert(
            AgEVASegmentType.eVASegmentTypeInitialState, "Inner Orbit", "-"
        )
        initState: "IMissionControlSequenceInitialState" = clr.CastAs(segment, IMissionControlSequenceInitialState)

        initState.coord_system_name = "CentralBody/Earth Fixed"
        initState.orbit_epoch = "1 Jan 2012 12:00:00.000"

        # Set element type and cast the Element property to the appropriate interface
        # configure the element as necessary
        initState.set_element_type(AgEVAElementType.eVAElementTypeCartesian)
        cartesian: "IElementCartesian" = clr.CastAs(initState.element, IElementCartesian)
        cartesian.vx = 8051.21
        cartesian.y = 55
        cartesian.z = 0
        cartesian.vx = 0.45
        cartesian.vy = 8.10158
        cartesian.vz = 3.51009

        # Configure fuel tank if necessary
        initState.fuel_tank.fuel_density = 1001
        initState.fuel_tank.fuel_mass = 501
        initState.fuel_tank.tank_pressure = 5001
        initState.fuel_tank.tank_temperature = 292

        # Configure spacecraft parameters
        initState.spacecraft_parameters.cd = 2.3
        initState.spacecraft_parameters.ck = 1.1
        initState.spacecraft_parameters.cr = 1.3
        initState.spacecraft_parameters.drag_area = 21
        initState.spacecraft_parameters.dry_mass = 501
        initState.spacecraft_parameters.k1 = 2
        initState.spacecraft_parameters.k2 = 3
        initState.spacecraft_parameters.radiation_pressure_area = 23.0
        initState.spacecraft_parameters.solar_radiation_pressure_area = 22.0

    # endregion

    # region ConfigurePropagateSegment
    def test_ConfigurePropagateSegment(self):
        self.ConfigurePropagateSegment(Astrogator.m_Object)

    def ConfigurePropagateSegment(self, driver: "IDriverMissionControlSequence"):
        # Add a propagate segment to our sequence
        segment: "IMissionControlSequenceSegment" = driver.main_sequence.insert(
            AgEVASegmentType.eVASegmentTypePropagate, "Propagate", "-"
        )
        propagate: "IMissionControlSequencePropagate" = clr.CastAs(segment, IMissionControlSequencePropagate)
        propagate.propagator_name = "Earth Point Mass"

        # Configure propagtor advanced properties
        propagate.min_propagation_time = 0
        propagate.enable_max_propagation_time = True
        propagate.max_propagation_time = 72000000
        propagate.enable_warning_message = True

        # Configure stopping conditions
        duration: "IStoppingCondition" = clr.CastAs(
            propagate.stopping_conditions["Duration"].properties, IStoppingCondition
        )
        duration.trip = 7200
        duration.tolerance = 1e-05

        # Add any addition stopping conditions
        lightning: "IStoppingCondition" = clr.CastAs(propagate.stopping_conditions.add("Lighting"), IStoppingCondition)

    # endregion

    # region ConfigureTargetSequenceSegment
    def test_ConfigureTargetSequenceSegment(self):
        self.ConfigureTargetSequenceSegment(Astrogator.m_Object)

    def ConfigureTargetSequenceSegment(self, driver: "IDriverMissionControlSequence"):
        # First add a sequence target
        segment: "IMissionControlSequenceSegment" = driver.main_sequence.insert(
            AgEVASegmentType.eVASegmentTypeTargetSequence, "Start Transfer", "-"
        )
        targetSequence: "IMissionControlSequenceTargetSequence" = clr.CastAs(
            segment, IMissionControlSequenceTargetSequence
        )

        targetSequence.action = AgEVATargetSeqAction.eVATargetSeqActionRunActiveProfiles
        targetSequence.when_profiles_finish = AgEVAProfilesFinish.eVAProfilesFinishRunToReturnAndContinue
        targetSequence.continue_on_failure = False

        # Add as many child segments to target
        dv1: "IMissionControlSequenceManeuver" = clr.CastAs(
            targetSequence.segments.insert(AgEVASegmentType.eVASegmentTypeManeuver, "DV1", "-"),
            IMissionControlSequenceManeuver,
        )
        dv2: "IMissionControlSequenceManeuver" = clr.CastAs(
            targetSequence.segments.insert(AgEVASegmentType.eVASegmentTypeManeuver, "DV2", "-"),
            IMissionControlSequenceManeuver,
        )

        # Add more profiles if necessary
        profileName: str = "Change Maneuver Type"
        if Array.IndexOf(targetSequence.profiles.available_profiles, profileName) != -1:
            newProfile: "IProfile" = targetSequence.profiles.add(profileName)

        # Enable controls
        dv1.enable_control_parameter(AgEVAControlManeuver.eVAControlManeuverImpulsiveCartesianX)
        dc: "IProfileDifferentialCorrector" = clr.CastAs(
            targetSequence.profiles["Differential Corrector"], IProfileDifferentialCorrector
        )
        controlParam: "IDifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths(
            "DV1", "ImpulsiveMnvr.Cartesian.X"
        )
        controlParam.enable = True
        controlParam.max_step = 0.3

        # Enable results
        (clr.Convert(dv1, IMissionControlSequenceSegment)).results.add("Epoch")
        roaResult: "IDifferentialCorrectorResult" = dc.results.get_result_by_paths("DV1", "Epoch")
        roaResult.enable = True

        # Confiure the differential corrector
        dc.max_iterations = 50
        dc.enable_display_status = True
        dc.mode = AgEVAProfileMode.eVAProfileModeIterate
        targetSequence.action = AgEVATargetSeqAction.eVATargetSeqActionRunActiveProfiles

    # endregion

    # region ConfigureLaunchSegment
    def test_ConfigureLaunchSegment(self):
        self.ConfigureLaunchSegment(Astrogator.m_Object)

    def ConfigureLaunchSegment(self, driver: "IDriverMissionControlSequence"):
        # Add launch sequence and retrieve the
        segment: "IMissionControlSequenceSegment" = driver.main_sequence.insert(
            AgEVASegmentType.eVASegmentTypeLaunch, "MyLaunch", "-"
        )
        launch: "IMissionControlSequenceLaunch" = clr.CastAs(segment, IMissionControlSequenceLaunch)

        # Configure launch properties
        launch.central_body_name = "Mars"
        launch.epoch = "1 Jan 2012 12:00:00.000"
        launch.step_size = 6
        launch.use_previous_segment_state = False
        launch.pre_launch_time = 1
        launch.time_of_flight = 500
        launch.ascent_type = AgEVAAscentType.eVAAscentTypeEllipseQuarticMotion
        launch.initial_acceleration = 0.02

        # Configure display type
        launch.set_display_system_type(AgEVALaunchDisplaySystem.eVADisplaySystemGeocentric)
        llr: "IDisplaySystemGeocentric" = clr.Convert(launch.display_system, IDisplaySystemGeocentric)
        llr.latitude = 35.581
        llr.longitude = -92.263
        llr.radius = 1000

        # Configure launch type
        launch.ascent_type = AgEVAAscentType.eVAAscentTypeEllipseQuarticMotion
        launch.initial_acceleration = 0.02
        launch.ascent_type = AgEVAAscentType.eVAAscentTypeEllipseCubicMotion

        # Configure burnout type
        velocity: "IBurnoutVelocity" = launch.burnout_velocity
        velocity.burnout_option = AgEVABurnoutOptions.eVABurnoutOptionsInertialVelocity
        velocity.inertial_velocity = 20.0
        velocity.inertial_horizontal_fpa = 22
        velocity.inertial_velocity_azimuth = 55
        velocity.burnout_option = AgEVABurnoutOptions.eVABurnoutOptionsFixedVelocity
        velocity.fixed_velocity = 20

    # endregion

    # region ConfigureUpdateSegment
    def test_ConfigureUpdateSegment(self):
        self.ConfigureUpdateSegment(Astrogator.m_Object)

    def ConfigureUpdateSegment(self, driver: "IDriverMissionControlSequence"):
        # Add launch sequence and retrieve the
        segment: "IMissionControlSequenceSegment" = driver.main_sequence.insert(
            AgEVASegmentType.eVASegmentTypeUpdate, "MyUpdate", "-"
        )
        update: "IMissionControlSequenceUpdate" = clr.CastAs(segment, IMissionControlSequenceUpdate)

        # Specify the element to be changed, the action, and the value

        # Add values
        update.set_action_and_value(AgEVAUpdateParam.eVAUpdateParamCd, AgEVAUpdateAction.eVAUpdateActionAddValue, 2)
        update.set_action_and_value(
            AgEVAUpdateParam.eVAUpdateParamFuelDensity, AgEVAUpdateAction.eVAUpdateActionAddValue, 1
        )

        # Set to new value
        update.set_action_and_value(
            AgEVAUpdateParam.eVAUpdateParamTankPressure, AgEVAUpdateAction.eVAUpdateActionSetToNewValue, 6000
        )
        update.set_action_and_value(
            AgEVAUpdateParam.eVAUpdateParamTankTemp, AgEVAUpdateAction.eVAUpdateActionSetToNewValue, 5
        )

        # Subtract values
        update.set_action_and_value(
            AgEVAUpdateParam.eVAUpdateParamSRPArea, AgEVAUpdateAction.eVAUpdateActionSubtractValue, 10
        )
        update.set_action_and_value(
            AgEVAUpdateParam.eVAUpdateParamSRPArea, AgEVAUpdateAction.eVAUpdateActionSubtractValue, 1
        )

    # endregion

    # region ConfigureManeuverSegment
    def test_ConfigureManeuverSegment(self):
        self.ConfigureManeuverSegment(Astrogator.m_Object)

    def ConfigureManeuverSegment(self, driver: "IDriverMissionControlSequence"):
        # Add launch sequence and retrieve the IMissionControlSequenceManeuver interface
        segment: "IMissionControlSequenceSegment" = driver.main_sequence.insert(
            AgEVASegmentType.eVASegmentTypeManeuver, "MyManeuver", "-"
        )
        maneuver: "IMissionControlSequenceManeuver" = clr.CastAs(segment, IMissionControlSequenceManeuver)

        # Set Maneuver to Impulsive
        maneuver.set_maneuver_type(AgEVAManeuverType.eVAManeuverTypeImpulsive)
        impulse: "IManeuverImpulsive" = clr.CastAs(maneuver.maneuver, IManeuverImpulsive)

        # Set Impulsive attitude to VelocityVector
        impulse.set_attitude_control_type(AgEVAAttitudeControl.eVAAttitudeControlVelocityVector)
        velVec: "IAttitudeControlImpulsiveVelocityVector" = clr.CastAs(
            impulse.attitude_control, IAttitudeControlImpulsiveVelocityVector
        )
        velVec.delta_v_magnitude = 1.0

        impulse.set_propulsion_method(AgEVAPropulsionMethod.eVAPropulsionMethodThrusterSet, "Thruster Set")
        impulse.update_mass = True

    # endregion

    # region ConfigureSequenceSegmentWithScriptingTool
    def test_ConfigureSequenceSegmentWithScriptingTool(self):
        self.ConfigureSequenceSegmentWithScriptingTool(Astrogator.m_Object)

    def ConfigureSequenceSegmentWithScriptingTool(self, driver: "IDriverMissionControlSequence"):
        # Add launch sequence and retrieve the
        segment: "IMissionControlSequenceSegment" = driver.main_sequence.insert(
            AgEVASegmentType.eVASegmentTypeSequence, "MySequence", "-"
        )
        sequence: "IMissionControlSequenceSequence" = clr.CastAs(segment, IMissionControlSequenceSequence)

        scriptTool: "IScriptingTool" = sequence.scripting_tool
        scriptTool.enable = True
        scriptTool.language_type = AgEVALanguage.eVALanguageVBScript
        scriptTool.script_text(
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

        burn1X: "IScriptingSegment" = scriptTool.segment_properties.add("Burn1X")
        if Array.IndexOf(burn1X.available_object_names, "Optimize_Delta_w.Burn1") != -1:
            burn1X.object_name = "Optimize_Delta_w.Burn1"
            burn1X.attribute = "ImpulsiveMnvr.Cartesian.X"
            burn1X.unit = "km/sec"

        period0: "IScriptingCalcObject" = scriptTool.calc_objects.add("Period_0")
        period0.calc_object_name = "Segments/Value At Segment"
        valAtSeg: "IStateCalcValueAtSegment" = clr.CastAs(period0.calc_object, IStateCalcValueAtSegment)
        valAtSeg.calc_object_name = "Keplerian Elems/Orbit Period"

    # endregion

    # region ConfigureTargetSequenceWithDC
    def test_ConfigureTargetSequenceWithDC(self):
        Astrogator.m_Object.main_sequence.insert(AgEVASegmentType.eVASegmentTypeTargetSequence, "Start Transfer", "-")
        self.ConfigureTargetSequenceWithDC(Astrogator.m_Object)

    def ConfigureTargetSequenceWithDC(self, driver: "IDriverMissionControlSequence"):
        startTransfer: "IMissionControlSequenceTargetSequence" = clr.CastAs(
            driver.main_sequence["Start Transfer"], IMissionControlSequenceTargetSequence
        )

        dcString: str = "Differential Corrector"
        if Array.IndexOf(startTransfer.profiles.available_profiles, dcString) != -1:
            dc: "IProfileDifferentialCorrector" = clr.CastAs(
                startTransfer.profiles.add(dcString), IProfileDifferentialCorrector
            )

            # Configure differential corrector
            dc.clear_corrections_before_run = True
            dc.convergence_criteria = (
                AgEVAConvergenceCriteria.eVAConvervenceCriteriaEitherEqualityConstraintsOrControlParams
            )
            dc.enable_b_plane_nominal = False
            dc.enable_b_plane_perturbations = False
            dc.enable_display_status = True
            dc.enable_homotopy = True
            dc.homotopy_steps = 2
            dc.enable_homotopy = False
            dc.enable_line_search = True
            dc.line_search_lower_bound = 0.001
            dc.line_search_tolerance = 0.001
            dc.line_search_upper_bound = 5.0
            dc.max_line_search_iterations = 5
            dc.max_iterations = 20

            # Apply
            startTransfer.apply_profiles()

    # endregion

    # region SetUserDefinedMuValueOnThirdBody
    def test_SetUserDefinedMuValueOnThirdBody(self):
        self.SetUserDefinedMuValueOnThirdBody(clr.CastAs(TestBase.Application.current_scenario, IScenario))

    def SetUserDefinedMuValueOnThirdBody(self, scenario: "IScenario"):
        compInfoCol: "IComponentInfoCollection" = scenario.component_directory.get_components(
            AgEComponent.eComponentAstrogator
        )
        thirdBodyFolder: "IComponentInfoCollection" = compInfoCol.get_folder("Propagator Functions").get_folder(
            "Third Bodies"
        )
        newMoon: "IThirdBodyFunction" = clr.CastAs(
            thirdBodyFolder.duplicate_component("Moon", "NewMoon"), IThirdBodyFunction
        )
        newMoon.set_mode_type(AgEVAThirdBodyMode.eVAThirdBodyModePointMass)
        pointMass: "IPointMassFunction" = clr.CastAs(newMoon.mode, IPointMassFunction)
        pointMass.grav_source = AgEVAGravParamSource.eVAGravParamSourceUser
        pointMass.mu = 390000.0

    # endregion

    # region SetUserDefinedMuValueOnThirdBodyFromPropagators
    def test_SetUserDefinedMuValueOnThirdBodyFromPropagators(self):
        self.SetUserDefinedMuValueOnThirdBodyFromPropagators(
            clr.CastAs(TestBase.Application.current_scenario, IScenario)
        )

    def SetUserDefinedMuValueOnThirdBodyFromPropagators(self, scenario: "IScenario"):
        compInfoCol: "IComponentInfoCollection" = scenario.component_directory.get_components(
            AgEComponent.eComponentAstrogator
        )
        propagatorFolder: "IComponentInfoCollection" = compInfoCol.get_folder("Propagators")
        myEathHPOP: "INumericalPropagatorWrapper" = clr.CastAs(
            propagatorFolder.duplicate_component("Earth HPOP Default v10", "myEathHPOP"), INumericalPropagatorWrapper
        )
        moon: "IThirdBodyFunction" = clr.CastAs(myEathHPOP.propagator_functions["Moon"], IThirdBodyFunction)
        moon.set_mode_type(AgEVAThirdBodyMode.eVAThirdBodyModePointMass)
        pointMass: "IPointMassFunction" = clr.CastAs(moon.mode, IPointMassFunction)
        pointMass.grav_source = AgEVAGravParamSource.eVAGravParamSourceUser
        pointMass.mu = 390000.0

    # endregion
