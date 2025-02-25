# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *


class AstrogatorSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(AstrogatorSnippets, self).__init__(*args, **kwargs)

    m_Satellite: "Satellite" = None
    m_Object: "MCSDriver" = None
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
        AstrogatorSnippets.m_Satellite = Satellite(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.SATELLITE, AstrogatorSnippets.m_DefaultName
            )
        )
        AstrogatorSnippets.m_Satellite.set_propagator_type(PropagatorType.ASTROGATOR)
        AstrogatorSnippets.m_Object = clr.CastAs(AstrogatorSnippets.m_Satellite.propagator, MCSDriver)
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        (IStkObject(AstrogatorSnippets.m_Satellite)).unload()
        AstrogatorSnippets.m_Object = None

    # endregion

    # region ConfigureAstrogratorPropagator
    def test_ConfigureAstrogratorPropagator(self):
        self.ConfigureAstrogratorPropagator(AstrogatorSnippets.m_Satellite)

    def ConfigureAstrogratorPropagator(self, satellite: "Satellite"):
        satellite.set_propagator_type(PropagatorType.ASTROGATOR)

        driver: "MCSDriver" = clr.CastAs(satellite.propagator, MCSDriver)

        # Remove if necessary
        driver.main_sequence.remove_all()

        # Configure properties as necessarily
        driver.options.draw_trajectory_in_3d = True
        driver.options.graphics_update_rate = 0.9
        driver.options.update_animation_time_for_all_objects = False
        driver.options.stopping_condition_time_tolerance = 5e-08
        driver.options.enable_logging = True

    # endregion

    # region ConfigureInitialStateSegment
    def test_ConfigureInitialStateSegment(self):
        self.ConfigureInitialStateSegment(AstrogatorSnippets.m_Object)

    def ConfigureInitialStateSegment(self, driver: "MCSDriver"):
        # Add a new segment and cast the segment to the MCSInitialState interface
        segment: "IMCSSegment" = driver.main_sequence.insert(SegmentType.INITIAL_STATE, "Inner Orbit", "-")
        initState: "MCSInitialState" = clr.CastAs(segment, MCSInitialState)

        initState.coord_system_name = "CentralBody/Earth Fixed"
        initState.orbit_epoch = "1 Jan 2012 12:00:00.000"

        # Set element type and cast the Element property to the appropriate interface
        # configure the element as necessary
        initState.set_element_type(ElementSetType.CARTESIAN)
        cartesian: "ElementCartesian" = clr.CastAs(initState.element, ElementCartesian)
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
        self.ConfigurePropagateSegment(AstrogatorSnippets.m_Object)

    def ConfigurePropagateSegment(self, driver: "MCSDriver"):
        # Add a propagate segment to our sequence
        segment: "IMCSSegment" = driver.main_sequence.insert(SegmentType.PROPAGATE, "Propagate", "-")
        propagate: "MCSPropagate" = clr.CastAs(segment, MCSPropagate)
        propagate.propagator_name = "Earth Point Mass"

        # Configure propagtor advanced properties
        propagate.min_propagation_time = 0
        propagate.enable_max_propagation_time = True
        propagate.max_propagation_time = 72000000
        propagate.enable_warning_message = True

        # Configure stopping conditions
        duration: "StoppingCondition" = clr.CastAs(
            propagate.stopping_conditions["Duration"].properties, StoppingCondition
        )
        duration.trip = 7200
        duration.tolerance = 1e-05

        # Add any addition stopping conditions
        lightning: "StoppingCondition" = clr.CastAs(propagate.stopping_conditions.add("Lighting"), StoppingCondition)

    # endregion

    # region ConfigureTargetSequenceSegment
    def test_ConfigureTargetSequenceSegment(self):
        self.ConfigureTargetSequenceSegment(AstrogatorSnippets.m_Object)

    def ConfigureTargetSequenceSegment(self, driver: "MCSDriver"):
        # First add a sequence target
        segment: "IMCSSegment" = driver.main_sequence.insert(SegmentType.TARGET_SEQUENCE, "Start Transfer", "-")
        targetSequence: "MCSTargetSequence" = clr.CastAs(segment, MCSTargetSequence)

        targetSequence.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
        targetSequence.when_profiles_finish = ProfilesFinish.RUN_TO_RETURN_AND_CONTINUE
        targetSequence.continue_on_failure = False

        # Add as many child segments to target
        dv1: "MCSManeuver" = clr.CastAs(targetSequence.segments.insert(SegmentType.MANEUVER, "DV1", "-"), MCSManeuver)
        dv2: "MCSManeuver" = clr.CastAs(targetSequence.segments.insert(SegmentType.MANEUVER, "DV2", "-"), MCSManeuver)

        # Add more profiles if necessary
        profileName: str = "Change Maneuver Type"
        if Array.IndexOf(targetSequence.profiles.available_profiles, profileName) != -1:
            newProfile: "IProfile" = targetSequence.profiles.add(profileName)

        # Enable controls
        dv1.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
        dc: "ProfileDifferentialCorrector" = clr.CastAs(
            targetSequence.profiles["Differential Corrector"], ProfileDifferentialCorrector
        )
        controlParam: "DifferentialCorrectorControl" = dc.control_parameters.get_control_by_paths(
            "DV1", "ImpulsiveMnvr.Cartesian.X"
        )
        controlParam.enable = True
        controlParam.max_step = 0.3

        # Enable results
        (IMCSSegment(dv1)).results.add("Epoch")
        roaResult: "DifferentialCorrectorResult" = dc.results.get_result_by_paths("DV1", "Epoch")
        roaResult.enable = True

        # Confiure the differential corrector
        dc.max_iterations = 50
        dc.enable_display_status = True
        dc.mode = ProfileMode.ITERATE
        targetSequence.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

    # endregion

    # region ConfigureLaunchSegment
    def test_ConfigureLaunchSegment(self):
        self.ConfigureLaunchSegment(AstrogatorSnippets.m_Object)

    def ConfigureLaunchSegment(self, driver: "MCSDriver"):
        # Add launch sequence and retrieve the
        segment: "IMCSSegment" = driver.main_sequence.insert(SegmentType.LAUNCH, "MyLaunch", "-")
        launch: "MCSLaunch" = clr.CastAs(segment, MCSLaunch)

        # Configure launch properties
        launch.central_body_name = "Mars"
        launch.epoch = "1 Jan 2012 12:00:00.000"
        launch.step_size = 6
        launch.use_previous_segment_state = False
        launch.pre_launch_time = 1
        launch.time_of_flight = 500
        launch.ascent_type = AscentType.ELLIPSE_QUARTIC_MOTION
        launch.initial_acceleration = 0.02

        # Configure display type
        launch.set_display_system_type(LaunchDisplaySystem.DISPLAY_SYSTEM_GEOCENTRIC)
        llr: "DisplaySystemGeocentric" = DisplaySystemGeocentric(launch.display_system)
        llr.latitude = 35.581
        llr.longitude = -92.263
        llr.radius = 1000

        # Configure launch type
        launch.ascent_type = AscentType.ELLIPSE_QUARTIC_MOTION
        launch.initial_acceleration = 0.02
        launch.ascent_type = AscentType.ELLIPSE_CUBIC_MOTION

        # Configure burnout type
        velocity: "BurnoutVelocity" = launch.burnout_velocity
        velocity.burnout_option = BurnoutOptions.INERTIAL_VELOCITY
        velocity.inertial_velocity = 20.0
        velocity.inertial_horizontal_flight_path_angle = 22
        velocity.inertial_velocity_azimuth = 55
        velocity.burnout_option = BurnoutOptions.FIXED_VELOCITY
        velocity.fixed_velocity = 20

    # endregion

    # region ConfigureUpdateSegment
    def test_ConfigureUpdateSegment(self):
        self.ConfigureUpdateSegment(AstrogatorSnippets.m_Object)

    def ConfigureUpdateSegment(self, driver: "MCSDriver"):
        # Add launch sequence and retrieve the
        segment: "IMCSSegment" = driver.main_sequence.insert(SegmentType.UPDATE, "MyUpdate", "-")
        update: "MCSUpdate" = clr.CastAs(segment, MCSUpdate)

        # Specify the element to be changed, the action, and the value

        # Add values
        update.set_action_and_value(UpdateParam.CD, UpdateAction.ADD_VALUE, 2)
        update.set_action_and_value(UpdateParam.FUEL_DENSITY, UpdateAction.ADD_VALUE, 1)

        # Set to new value
        update.set_action_and_value(UpdateParam.TANK_PRESSURE, UpdateAction.SET_TO_NEW_VALUE, 6000)
        update.set_action_and_value(UpdateParam.TANK_TEMPERATURE, UpdateAction.SET_TO_NEW_VALUE, 5)

        # Subtract values
        update.set_action_and_value(UpdateParam.SRP_AREA, UpdateAction.SUBTRACT_VALUE, 10)
        update.set_action_and_value(UpdateParam.SRP_AREA, UpdateAction.SUBTRACT_VALUE, 1)

    # endregion

    # region ConfigureManeuverSegment
    def test_ConfigureManeuverSegment(self):
        self.ConfigureManeuverSegment(AstrogatorSnippets.m_Object)

    def ConfigureManeuverSegment(self, driver: "MCSDriver"):
        # Add launch sequence and retrieve the MCSManeuver interface
        segment: "IMCSSegment" = driver.main_sequence.insert(SegmentType.MANEUVER, "MyManeuver", "-")
        maneuver: "MCSManeuver" = clr.CastAs(segment, MCSManeuver)

        # Set Maneuver to Impulsive
        maneuver.set_maneuver_type(ManeuverType.IMPULSIVE)
        impulse: "ManeuverImpulsive" = clr.CastAs(maneuver.maneuver, ManeuverImpulsive)

        # Set Impulsive attitude to VelocityVector
        impulse.set_attitude_control_type(AttitudeControl.VELOCITY_VECTOR)
        velVec: "AttitudeControlImpulsiveVelocityVector" = clr.CastAs(
            impulse.attitude_control, AttitudeControlImpulsiveVelocityVector
        )
        velVec.delta_v_magnitude = 1.0

        impulse.set_propulsion_method(PropulsionMethod.THRUSTER_SET, "Thruster Set")
        impulse.update_mass = True

    # endregion

    # region ConfigureSequenceSegmentWithScriptingTool
    def test_ConfigureSequenceSegmentWithScriptingTool(self):
        self.ConfigureSequenceSegmentWithScriptingTool(AstrogatorSnippets.m_Object)

    def ConfigureSequenceSegmentWithScriptingTool(self, driver: "MCSDriver"):
        # Add launch sequence and retrieve the
        segment: "IMCSSegment" = driver.main_sequence.insert(SegmentType.SEQUENCE, "MySequence", "-")
        sequence: "IMCSSequence" = clr.CastAs(segment, IMCSSequence)

        scriptTool: "ScriptingTool" = sequence.scripting_tool
        scriptTool.enable = True
        scriptTool.language_type = Language.VB_SCRIPT
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

        burn1X: "ScriptingSegment" = scriptTool.segment_properties.add("Burn1X")
        if Array.IndexOf(burn1X.available_object_names, "Optimize_Delta_w.Burn1") != -1:
            burn1X.object_name = "Optimize_Delta_w.Burn1"
            burn1X.attribute = "ImpulsiveMnvr.Cartesian.X"
            burn1X.unit = "km/sec"

        period0: "ScriptingCalculationObject" = scriptTool.calculation_objects.add("Period_0")
        period0.calculation_object_name = "Segments/Value At Segment"
        valAtSeg: "StateCalcValueAtSegment" = clr.CastAs(period0.calculation_object, StateCalcValueAtSegment)
        valAtSeg.calculation_object_name = "Keplerian Elems/Orbit Period"

    # endregion

    # region ConfigureTargetSequenceWithDC
    def test_ConfigureTargetSequenceWithDC(self):
        AstrogatorSnippets.m_Object.main_sequence.insert(SegmentType.TARGET_SEQUENCE, "Start Transfer", "-")
        self.ConfigureTargetSequenceWithDC(AstrogatorSnippets.m_Object)

    def ConfigureTargetSequenceWithDC(self, driver: "MCSDriver"):
        startTransfer: "MCSTargetSequence" = clr.CastAs(driver.main_sequence["Start Transfer"], MCSTargetSequence)

        dcString: str = "Differential Corrector"
        if Array.IndexOf(startTransfer.profiles.available_profiles, dcString) != -1:
            dc: "ProfileDifferentialCorrector" = clr.CastAs(
                startTransfer.profiles.add(dcString), ProfileDifferentialCorrector
            )

            # Configure differential corrector
            dc.clear_corrections_before_run = True
            dc.convergence_criteria = (
                ConvergenceCriteria.CONVERVENCE_CRITERIA_EITHER_EQUALITY_CONSTRAINTS_OR_CONTROL_PARAMS
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
        self.SetUserDefinedMuValueOnThirdBody(clr.CastAs(TestBase.Application.current_scenario, Scenario))

    def SetUserDefinedMuValueOnThirdBody(self, scenario: "Scenario"):
        compInfoCol: "ComponentInfoCollection" = scenario.component_directory.get_components(Component.ASTROGATOR)
        thirdBodyFolder: "ComponentInfoCollection" = compInfoCol.get_folder("Propagator Functions").get_folder(
            "Third Bodies"
        )
        newMoon: "ThirdBodyFunction" = clr.CastAs(
            thirdBodyFolder.duplicate_component("Moon", "NewMoon"), ThirdBodyFunction
        )
        newMoon.set_mode_type(ThirdBodyMode.POINT_MASS)
        pointMass: "PointMassFunction" = clr.CastAs(newMoon.mode, PointMassFunction)
        pointMass.gravitational_parameter_source = GravParamSource.USER
        pointMass.mu = 390000.0

    # endregion

    # region SetUserDefinedMuValueOnThirdBodyFromPropagators
    def test_SetUserDefinedMuValueOnThirdBodyFromPropagators(self):
        self.SetUserDefinedMuValueOnThirdBodyFromPropagators(
            clr.CastAs(TestBase.Application.current_scenario, Scenario)
        )

    def SetUserDefinedMuValueOnThirdBodyFromPropagators(self, scenario: "Scenario"):
        compInfoCol: "ComponentInfoCollection" = scenario.component_directory.get_components(Component.ASTROGATOR)
        propagatorFolder: "ComponentInfoCollection" = compInfoCol.get_folder("Propagators")
        myEathHPOP: "NumericalPropagatorWrapper" = clr.CastAs(
            propagatorFolder.duplicate_component("Earth HPOP Default v10", "myEathHPOP"), NumericalPropagatorWrapper
        )
        moon: "ThirdBodyFunction" = clr.CastAs(myEathHPOP.propagator_functions["Moon"], ThirdBodyFunction)
        moon.set_mode_type(ThirdBodyMode.POINT_MASS)
        pointMass: "PointMassFunction" = clr.CastAs(moon.mode, PointMassFunction)
        pointMass.gravitational_parameter_source = GravParamSource.USER
        pointMass.mu = 390000.0

    # endregion
