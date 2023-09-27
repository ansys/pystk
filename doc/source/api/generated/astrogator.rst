Module contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    IUserVariableDefinitionCollection
    IUserVariableCollection
    IUserVariableUpdateCollection
    ICalculationGraphCollection
    IConstraintCollection
    IPluginProperties
    ISNOPTControlCollection
    ISNOPTResultCollection
    IIPOPTControlCollection
    IIPOPTResultCollection
    IManeuverOptimalFiniteSNOPTOptimizer
    IManeuverOptimalFiniteInitialBoundaryConditions
    IManeuverOptimalFiniteFinalBoundaryConditions
    IManeuverOptimalFinitePathBoundaryConditions
    IManeuverOptimalFiniteSteeringNodeCollection
    IManeuverOptimalFiniteBounds
    IGoldenSectionControlCollection
    IGoldenSectionControl
    IGoldenSectionResultCollection
    IGoldenSectionResult
    IGridSearchControlCollection
    IGridSearchControl
    IGridSearchResultCollection
    IGridSearchResult
    IBisectionControlCollection
    IBisectionResult
    IBisectionResultCollection
    IStoppingConditionElement
    IStoppingConditionCollection
    IMissionControlSequenceSegmentCollection
    IState
    IStoppingConditionComponent
    IAutomaticSequence
    IAutomaticSequenceCollection
    IBPlaneCollection
    ICalcObjectCollection
    IManeuverFinitePropagator
    IBurnoutVelocity
    IAttitudeControl
    IAttitudeControlFinite
    IAttitudeControlImpulsive
    IAttitudeControlOptimalFinite
    IManeuver
    IDisplaySystem
    IBurnout
    IScriptingSegment
    IScriptingSegmentCollection
    IScriptingParameterEnumerationChoice
    IScriptingParameterEnumerationChoiceCollection
    IScriptingParameter
    IScriptingParameterCollection
    IScriptingCalcObject
    IScriptingCalcObjectCollection
    IScriptingTool
    IElement
    ISpacecraftParameters
    IFuelTank
    IMissionControlSequenceSegmentProperties
    IMissionControlSequenceEnd
    IMissionControlSequenceInitialState
    IMissionControlSequenceSegment
    IMissionControlSequenceOptions
    IDriverMissionControlSequence
    IElementCartesian
    IElementKeplerian
    IElementDelaunay
    IElementEquinoctial
    IElementMixedSpherical
    IElementSpherical
    IElementTargetVectorIncomingAsymptote
    IElementTargetVectorOutgoingAsymptote
    IElementGeodetic
    IElementBPlane
    IStoppingCondition
    ILightingStoppingCondition
    IAccessStoppingCondition
    IMissionControlSequencePropagate
    IMissionControlSequenceSequence
    IMissionControlSequenceBackwardSequence
    IMissionControlSequenceLaunch
    IDisplaySystemGeodetic
    IDisplaySystemGeocentric
    IBurnoutCBFCartesian
    IBurnoutGeodetic
    IBurnoutGeocentric
    IBurnoutLaunchAzAltitude
    IBurnoutLaunchAzRadius
    IMissionControlSequenceFollow
    IMissionControlSequenceManeuver
    IManeuverFinite
    IManeuverImpulsive
    IAttitudeControlImpulsiveVelocityVector
    IAttitudeControlImpulsiveAntiVelocityVector
    IAttitudeControlImpulsiveAttitude
    IAttitudeControlImpulsiveFile
    IAttitudeControlImpulsiveThrustVector
    IAttitudeControlFiniteAntiVelocityVector
    IAttitudeControlFiniteAttitude
    IAttitudeControlFiniteFile
    IAttitudeControlFiniteThrustVector
    IAttitudeControlFiniteTimeVarying
    IAttitudeControlFiniteVelocityVector
    IAttitudeControlFinitePlugin
    IAttitudeControlOptimalFiniteLagrange
    IMissionControlSequenceHold
    IMissionControlSequenceUpdate
    IMissionControlSequenceReturn
    IMissionControlSequenceStop
    IProfile
    IProfileCollection
    IMissionControlSequenceTargetSequence
    IDifferentialCorrectorControl
    IDifferentialCorrectorResult
    ISearchPluginControl
    ISearchPluginResult
    ISearchPluginResultCollection
    ISearchPluginControlCollection
    IDifferentialCorrectorControlCollection
    IDifferentialCorrectorResultCollection
    ITargeterGraphActiveControl
    ITargeterGraphResult
    ITargeterGraphActiveControlCollection
    ITargeterGraphResultCollection
    ITargeterGraph
    ITargeterGraphCollection
    IProfileSearchPlugin
    IProfileDifferentialCorrector
    IProfileChangeManeuverType
    IProfileScriptingTool
    IProfileChangeReturnSegment
    IProfileChangePropagator
    IProfileChangeStopSegment
    IProfileChangeStoppingConditionState
    IProfileSeedFiniteManeuver
    IProfileRunOnce
    IUserVariableDefinition
    IUserVariable
    IUserVariableUpdate
    IProfileSNOPTOptimizer
    ISNOPTControl
    ISNOPTResult
    IProfileIPOPTOptimizer
    IIPOPTControl
    IIPOPTResult
    IManeuverOptimalFinite
    IManeuverOptimalFiniteSteeringNodeElement
    IProfileLambertProfile
    IProfileLambertSearchProfile
    IProfileGoldenSection
    IProfileGridSearch
    ICalcObjectLinkEmbedControlCollection
    IProfileBisection
    IBisectionControl
    IStateCalcHeightAboveTerrain
    IStateCalcEpoch
    IStateCalcOrbitDelaunayG
    IStateCalcOrbitDelaunayH
    IStateCalcOrbitDelaunayL
    IStateCalcOrbitSemiLatusRectum
    IStateCalcJacobiConstant
    IStateCalcCartesianElem
    IStateCalcCartSTMElem
    IStateCalcSTMEigenval
    IStateCalcSTMEigenvecElem
    IStateCalcEnvironment
    IStateCalcEquinoctialElem
    IStateCalcDamageFlux
    IStateCalcDamageMassFlux
    IStateCalcMagnitudeFieldDipoleL
    IStateCalcSEETMagnitudeFieldFieldLineSepAngle
    IStateCalcImpactFlux
    IStateCalcImpactMassFlux
    IStateCalcSEETSAAFlux
    IStateCalcSEETVehTemp
    IStateCalcCloseApproachBearing
    IStateCalcCloseApproachMagnitude
    IStateCalcCloseApproachTheta
    IStateCalcCloseApproachX
    IStateCalcCloseApproachY
    IStateCalcCloseApproachCosBearing
    IStateCalcRelGroundTrackError
    IStateCalcRelAtAOLMaster
    IStateCalcDeltaFromMaster
    IStateCalcLonDriftRate
    IStateCalcMeanEarthLon
    IStateCalcRectifiedLon
    IStateCalcTrueLongitude
    IStateCalcGeodeticTrueLongitude
    IStateCalcGeodeticTrueLongitudeAtTimeOfPerigee
    IStateCalcMeanRightAscension
    IStateCalcGeodeticMeanRightAscension
    IStateCalcTwoBodyDriftRate
    IStateCalcDriftRateFactor
    IStateCalcEccentricityX
    IStateCalcEccentricityY
    IStateCalcInclinationX
    IStateCalcInclinationY
    IStateCalcUnitAngularMomentumX
    IStateCalcUnitAngularMomentumY
    IStateCalcUnitAngularMomentumZ
    IStateCalcGeodeticElem
    IStateCalcRepeatingGroundTrackErr
    IStateCalcAltitudeOfApoapsis
    IStateCalcAltitudeOfPeriapsis
    IStateCalcArgOfLat
    IStateCalcArgOfPeriapsis
    IStateCalcEccentricityAnomaly
    IStateCalcEccentricity
    IStateCalcInclination
    IStateCalcLonOfAscNode
    IStateCalcMeanAnomaly
    IStateCalcMeanMotion
    IStateCalcOrbitPeriod
    IStateCalcNumRevs
    IStateCalcRAAN
    IStateCalcRadOfApoapsis
    IStateCalcRadOfPeriapsis
    IStateCalcSemiMajorAxis
    IStateCalcTimePastAscNode
    IStateCalcTimePastPeriapsis
    IStateCalcDeltaV
    IStateCalcDeltaVSquared
    IStateCalcMissionControlSequenceDeltaV
    IStateCalcMissionControlSequenceDeltaVSquared
    IStateCalcSequenceDeltaV
    IStateCalcSequenceDeltaVSquared
    IStateCalcFuelMass
    IStateCalcDensity
    IStateCalcInertialDeltaVMagnitude
    IStateCalcInertialDeltaVx
    IStateCalcInertialDeltaVy
    IStateCalcInertialDeltaVz
    IStateCalcManeuverSpecificImpulse
    IStateCalcPressure
    IStateCalcTemperature
    IStateCalcVectorX
    IStateCalcVectorY
    IStateCalcVectorZ
    IStateCalcMass
    IStateCalcManeuverTotalMassFlowRate
    IStateCalcAbsoluteValue
    IStateCalcDifference
    IStateCalcDifferenceOtherSegment
    IStateCalcPositionDifferenceOtherSegment
    IStateCalcVelDifferenceOtherSegment
    IStateCalcPositionVelDifferenceOtherSegment
    IStateCalcValueAtSegment
    IStateCalcMaxValue
    IStateCalcMinValue
    IStateCalcMeanValue
    IStateCalcMedianValue
    IStateCalcStandardDeviation
    IStateCalcNegative
    IStateCalcTrueAnomaly
    IBDotRCalc
    IBDotTCalc
    IBMagnitudeCalc
    IBThetaCalc
    IStateCalcDeltaDec
    IStateCalcDeltaRA
    IStateCalcBetaAngle
    IStateCalcLocalApparentSolarLon
    IStateCalcLonOfPeriapsis
    IStateCalcOrbitStateValue
    IStateCalcSignedEccentricity
    IStateCalcTrueLon
    IStateCalcPower
    IStateCalcRelMotion
    IStateCalcSolarBetaAngle
    IStateCalcSolarInPlaneAngle
    IStateCalcRelPositionDecAngle
    IStateCalcRelPositionInPlaneAngle
    IStateCalcRelativeInclination
    IStateCalcCurvilinearRelMotion
    IStateCalcCustomFunction
    IStateCalcScript
    IStateCalcCd
    IStateCalcCr
    IStateCalcDragArea
    IStateCalcRadiationPressureArea
    IStateCalcRadiationPressureCoefficient
    IStateCalcSRPArea
    IStateCalcCosOfVerticalFPA
    IStateCalcDec
    IStateCalcFPA
    IStateCalcRMagnitude
    IStateCalcRA
    IStateCalcVMagnitude
    IStateCalcVelAz
    IStateCalcC3Energy
    IStateCalcInAsympDec
    IStateCalcInAsympRA
    IStateCalcInVelAzAtPeriapsis
    IStateCalcOutAsympDec
    IStateCalcOutAsympRA
    IStateCalcOutVelAzAtPeriapsis
    IStateCalcDuration
    IStateCalcUserValue
    IStateCalcVectorGeometryToolAngle
    IStateCalcAngle
    IStateCalcDotProduct
    IStateCalcVectorDec
    IStateCalcVectorMagnitude
    IStateCalcVectorRA
    IStateCalcOnePointAccess
    IStateCalcDifferenceAcrossSegmentsOtherSat
    IStateCalcValueAtSegmentOtherSat
    IStateCalcRARate
    IStateCalcDecRate
    IStateCalcGravitationalParameter
    IStateCalcReferenceRadius
    IStateCalcGravCoeff
    IStateCalcSpeedOfLight
    IStateCalcPi
    IStateCalcScalar
    IStateCalcApparentSolarTime
    IStateCalcEarthMeanSolarTime
    IStateCalcEarthMeanLocTimeAN
    ICentralBodyCollection
    ICentralBodyEphemeris
    ICentralBodyGravityModel
    ICentralBodyShape
    ICentralBodyShapeSphere
    ICentralBodyShapeOblateSpheroid
    ICentralBodyShapeTriaxialEllipsoid
    ICentralBodyAttitude
    ICentralBodyAttitudeRotationCoefficientsFile
    ICentralBodyAttitudeIAU1994
    ICentralBodyEphemerisAnalyticOrbit
    ICentralBodyEphemerisJPLSpice
    ICentralBodyEphemerisFile
    ICentralBodyEphemerisJPLDesignExplorerOptimizer
    ICentralBodyEphemerisPlanetary
    IAstrogatorCentralBody
    IPowerInternal
    IPowerProcessed
    IPowerSolarArray
    IGeneralRelativityFunction
    IStateTransformationFunction
    ICR3BPFunc
    IRadiationPressureFunction
    IYarkovskyFunc
    IBlendedDensity
    IDragModelPlugin
    ICira72Function
    IExponential
    IHarrisPriester
    IDensityModelPlugin
    IJacchiaRoberts
    IJacchiaBowman2008
    IJacchia_1960
    IJacchia_1970
    IJacchia_1971
    IMSISE_1990
    IMSIS_1986
    INRLMSISE_2000
    IUS_Standard_Atmosphere
    IMarsGRAM37
    IMarsGRAM2005
    IVenusGRAM2005
    IMarsGRAM2010
    IMarsGRAM2001
    IMarsGRAM2000
    IDTM2012
    IDTM2020
    IGravityFieldFunction
    IPointMassFunction
    ITwoBodyFunction
    IHPOPPluginFunction
    IEOMFuncPluginFunction
    ISRPAeroT20
    ISRPAeroT30
    ISRPGSPM04aIIA
    ISRPGSPM04aIIR
    ISRPGSPM04aeIIA
    ISRPGSPM04aeIIR
    ISRPSpherical
    ISRPNPlate
    ISRPTabAreaVec
    ISRPVariableArea
    IThirdBodyFunction
    ISRPReflectionPlugin
    IEngineModelThrustCoefficients
    IEngineModelIspCoefficients
    IEngineConstAcc
    IEngineConstant
    IEngineDefinition
    IEngineThrottleTable
    IEngineIon
    IEngineCustom
    IEnginePlugin
    IEngineModelPoly
    IDesignCR3BPObjectCollection
    IDesignCR3BPSetup
    IDesignCR3BPObject
    IThruster
    IThrusterSetCollection
    IThrusterSet
    IAsTriggerCondition
    ICustomFunctionScriptEngine
    INumericalIntegrator
    IPropagatorFunctionCollection
    INumericalPropagatorWrapper
    INumericalPropagatorWrapperCR3BP
    IBulirschStoerIntegrator
    IGaussJacksonIntegrator
    IRungeKutta2nd3rd
    IRungeKutta4th
    IRungeKutta4th5th
    IRungeKutta4thAdapt
    IRungeKuttaF7th8th
    IRungeKuttaV8th9th


Enumerations
~~~~~~~~~~~~

.. autosummary::

    GRAPH_OPTION
    SMART_RUN_MODE
    FORMULATION
    LIGHTING_CONDITION
    PROFILE
    ACCESS_CRITERION
    ECLIPSING_BODIES_SOURCE
    CRITERION
    CALC_OBJECT_REFERENCE
    CALC_OBJECT_CENTRAL_BODY_REFERENCE
    CALC_OBJECT_ELEM
    PROFILE_MODE
    CONTROL_STOPPING_CONDITION
    STATE
    RETURN_CONTROL
    DRAW_PERTURBATION
    DERIVE_CALC_METHOD
    CONVERGENCE_CRITERIA
    DIFFERENTIAL_CORRECTOR_SCALING_METHOD
    CONTROL_UPDATE
    CONTROL_FOLLOW
    CONTROL_INIT_STATE
    CONTROL_MANEUVER
    CONTROL_LAUNCH
    CONTROL_ADVANCED
    TARGET_SEQ_ACTION
    PROFILES_FINISH
    UPDATE_PARAM
    UPDATE_ACTION
    PRESSURE_MODE
    THRUST_TYPE
    ATTITUDE_UPDATE
    PROPULSION_METHOD
    CUSTOM_FUNCTION
    BODY_AXIS
    CONSTRAINT_SIGN
    ATTITUDE_CONTROL
    FOLLOW_JOIN
    FOLLOW_SEPARATION
    FOLLOW_SPACECRAFT_AND_FUEL_TANK
    BURNOUT_OPTIONS
    BURNOUT_TYPE
    ASCENT_TYPE
    LAUNCH_DISPLAY_SYSTEM
    RUN_CODE
    SEQUENCE_STATE_TO_PASS
    MANEUVER_TYPE
    SEGMENT_TYPE
    ELEMENT_TYPE
    LANGUAGE
    STOPPING_CONDITION
    CLEAR_EPHEMERIS_DIRECTION
    PROFILE_INSERT_DIRECTION
    ROOT_FINDING_ALGORITHM
    SCRIPTING_PARAMETER_TYPE
    SNOPT_GOAL
    IPOPT_GOAL
    OPTIMAL_FINITE_SEED_METHOD
    OPTIMAL_FINITE_RUN_MODE
    OPTIMAL_FINITE_DISCRETIZATION_STRATEGY
    OPTIMAL_FINITE_WORKING_VARIABLES
    OPTIMAL_FINITE_SCALING_OPTIONS
    OPTIMAL_FINITE_SNOPT_OBJECTIVE
    OPTIMAL_FINITE_SNOPT_SCALING
    OPTIMAL_FINITE_EXPORT_NODES_FORMAT
    OPTIMAL_FINITE_GUESS_METHOD
    IMP_DELTA_V_REP
    LAMBERT_TARGET_COORD_TYPE
    LAMBERT_SOLUTION_OPTION_TYPE
    LAMBERT_ORBITAL_ENERGY_TYPE
    LAMBERT_DIRECTION_OF_MOTION_TYPE
    GOLDEN_SECTION_DESIRED_OPERATION
    GRID_SEARCH_DESIRED_OPERATION
    ELEMENT
    BASE_SELECTION
    CONTROL_ORBIT_STATE_VALUE
    SEGMENT_STATE
    DIFFERENCE_ORDER
    SEGMENT_DIFFERENCE_ORDER
    CONTROL_REPEATING_GROUND_TRACK_ERR
    CALC_OBJECT_DIRECTION
    CALC_OBJECT_ORBIT_PLANE_SOURCE
    CALC_OBJECT_SUN_POSITION
    CALC_OBJECT_ANGLE_SIGN
    CALC_OBJECT_REFERENCE_DIRECTION
    CALC_OBJECT_RELATIVE_POSITION
    CALC_OBJECT_REFERENCE_ELLIPSE
    CALC_OBJECT_LOCATION_SOURCE
    GRAVITATIONAL_PARAMETER_SOURCE
    REFERENCE_RADIUS_SOURCE
    GRAV_COEFF_NORMALIZATION_TYPE
    GRAV_COEFF_COEFFICIENT_TYPE
    STM_PERT_VARIABLES
    STM_EIGEN_NUMBER
    COMPLEX_NUMBER
    SQUARED_TYPE
    GEO_STATIONARY_DRIFT_RATE_MODEL
    GEO_STATIONARY_INCLINATION_MAGNITUDE
    CENTRAL_BODY_GRAVITY_MODEL
    CENTRAL_BODY_SHAPE
    CENTRAL_BODY_ATTITUDE
    CENTRAL_BODY_EPHEMERIS
    CONTROL_POWER_INTERNAL
    CONTROL_POWER_PROCESSED
    CONTROL_POWER_SOLAR_ARRAY
    THIRD_BODY_MODE
    GRAV_PARAM_SOURCE
    EPHEM_SOURCE
    SOLAR_FORCE_METHOD
    SHADOW_MODEL
    SUN_POSITION
    ATMOS_DATA_SOURCE
    GEO_MAGNETIC_FLUX_SOURCE
    GEO_MAGNETIC_FLUX_UPDATE_RATE
    DRAG_MODEL_TYPE
    MARS_GRAM_DENSITY_TYPE
    VENUS_GRAM_DENSITY_TYPE
    TAB_VEC_INTERP_METHOD
    CONTROL_ENGINE_CONST_ACC
    CONTROL_ENGINE_CONSTANT
    CONTROL_ENGINE_CUSTOM
    CONTROL_ENGINE_THROTTLE_TABLE
    CONTROL_ENGINE_ION
    CONTROL_ENGINE_MODEL_POLY
    ENGINE_MODEL_FUNCTION
    THROTTLE_TABLE_OPERATION_MODE
    IDEAL_ORBIT_RADIUS
    ROTATING_COORDINATE_SYSTEM
    CONTROL_THRUSTERS
    THRUSTER_DIRECTION
    CRITERIA
    ERROR_CONTROL
    PREDICTOR_CORRECTOR
    NUMERICAL_INTEGRATOR
    COEFF_RUNGE_KUTTA_V_8TH9_TH


Classes
~~~~~~~

.. autosummary::

    DriverMissionControlSequence
    MissionControlSequenceSegmentCollection
    MissionControlSequenceEnd
    MissionControlSequenceInitialState
    SpacecraftParameters
    FuelTank
    ElementCartesian
    ElementKeplerian
    ElementEquinoctial
    ElementDelaunay
    ElementMixedSpherical
    ElementSpherical
    ElementTargetVectorIncomingAsymptote
    ElementTargetVectorOutgoingAsymptote
    ElementGeodetic
    ElementBPlane
    MissionControlSequencePropagate
    State
    StoppingConditionCollection
    AccessStoppingCondition
    LightingStoppingCondition
    StoppingCondition
    StoppingConditionElement
    MissionControlSequenceSequence
    MissionControlSequenceBackwardSequence
    MissionControlSequenceLaunch
    DisplaySystemGeodetic
    DisplaySystemGeocentric
    BurnoutGeodetic
    BurnoutCBFCartesian
    BurnoutGeocentric
    BurnoutLaunchAzAltitude
    BurnoutLaunchAzRadius
    BurnoutVelocity
    MissionControlSequenceFollow
    MissionControlSequenceManeuver
    ManeuverFinite
    ManeuverImpulsive
    AttitudeControlImpulsiveVelocityVector
    AttitudeControlImpulsiveAntiVelocityVector
    AttitudeControlImpulsiveAttitude
    AttitudeControlImpulsiveFile
    AttitudeControlImpulsiveThrustVector
    AttitudeControlFiniteAntiVelocityVector
    AttitudeControlFiniteAttitude
    AttitudeControlFiniteFile
    AttitudeControlFiniteThrustVector
    AttitudeControlFiniteTimeVarying
    AttitudeControlFiniteVelocityVector
    AttitudeControlFinitePlugin
    AttitudeControlOptimalFiniteLagrange
    ManeuverFinitePropagator
    MissionControlSequenceHold
    MissionControlSequenceUpdate
    MissionControlSequenceReturn
    MissionControlSequenceStop
    MissionControlSequenceTargetSequence
    ProfileCollection
    MissionControlSequenceOptions
    CalcObjectCollection
    ConstraintCollection
    PluginProperties
    ProfileSearchPlugin
    TargeterGraph
    TargeterGraphCollection
    TargeterGraphResultCollection
    TargeterGraphActiveControlCollection
    TargeterGraphActiveControl
    TargeterGraphResult
    ProfileDifferentialCorrector
    ProfileScriptingTool
    DifferentialCorrectorControl
    DifferentialCorrectorResult
    DifferentialCorrectorControlCollection
    DifferentialCorrectorResultCollection
    SearchPluginControl
    SearchPluginControlCollection
    SearchPluginResult
    SearchPluginResultCollection
    ProfileChangeManeuverType
    ProfileChangeReturnSegment
    ProfileChangePropagator
    ProfileChangeStopSegment
    ProfileChangeStoppingConditionState
    ProfileSeedFiniteManeuver
    ProfileRunOnce
    BPlaneCollection
    StateCalcDamageFlux
    StateCalcDamageMassFlux
    StateCalcMagnitudeFieldDipoleL
    StateCalcSEETMagnitudeFieldFieldLineSepAngle
    StateCalcImpactFlux
    StateCalcImpactMassFlux
    StateCalcSEETSAAFlux
    StateCalcSEETVehTemp
    StateCalcEpoch
    StateCalcJacobiConstant
    StateCalcCartesianElem
    StateCalcCartSTMElem
    StateCalcSTMEigenval
    StateCalcSTMEigenvecElem
    StateCalcEnvironment
    StateCalcOrbitDelaunayG
    StateCalcOrbitDelaunayH
    StateCalcOrbitDelaunayL
    StateCalcOrbitSemiLatusRectum
    StateCalcEquinoctialElem
    StateCalcCloseApproachBearing
    StateCalcCloseApproachMagnitude
    StateCalcCloseApproachTheta
    StateCalcCloseApproachX
    StateCalcCloseApproachY
    StateCalcCloseApproachCosBearing
    StateCalcRelGroundTrackError
    StateCalcRelAtAOLMaster
    StateCalcDeltaFromMaster
    StateCalcLonDriftRate
    StateCalcMeanEarthLon
    StateCalcRectifiedLon
    StateCalcTrueLongitude
    StateCalcGeodeticTrueLongitude
    StateCalcGeodeticTrueLongitudeAtTimeOfPerigee
    StateCalcMeanRightAscension
    StateCalcGeodeticMeanRightAscension
    StateCalcTwoBodyDriftRate
    StateCalcDriftRateFactor
    StateCalcEccentricityX
    StateCalcEccentricityY
    StateCalcInclinationX
    StateCalcInclinationY
    StateCalcUnitAngularMomentumX
    StateCalcUnitAngularMomentumY
    StateCalcUnitAngularMomentumZ
    StateCalcHeightAboveTerrain
    StateCalcGeodeticElem
    StateCalcRepeatingGroundTrackErr
    StateCalcAltitudeOfApoapsis
    StateCalcAltitudeOfPeriapsis
    StateCalcArgOfLat
    StateCalcArgOfPeriapsis
    StateCalcEccentricityAnomaly
    StateCalcLonOfAscNode
    StateCalcMeanMotion
    StateCalcOrbitPeriod
    StateCalcNumRevs
    StateCalcRadOfApoapsis
    StateCalcRadOfPeriapsis
    StateCalcSemiMajorAxis
    StateCalcTimePastAscNode
    StateCalcTimePastPeriapsis
    StateCalcTrueAnomaly
    StateCalcDeltaV
    StateCalcDeltaVSquared
    StateCalcMissionControlSequenceDeltaV
    StateCalcMissionControlSequenceDeltaVSquared
    StateCalcSequenceDeltaV
    StateCalcSequenceDeltaVSquared
    StateCalcFuelMass
    StateCalcDensity
    StateCalcInertialDeltaVMagnitude
    StateCalcInertialDeltaVx
    StateCalcInertialDeltaVy
    StateCalcInertialDeltaVz
    StateCalcManeuverSpecificImpulse
    StateCalcPressure
    StateCalcTemperature
    StateCalcVectorY
    StateCalcVectorZ
    StateCalcMass
    StateCalcManeuverTotalMassFlowRate
    StateCalcAbsoluteValue
    StateCalcDifference
    StateCalcDifferenceOtherSegment
    StateCalcPositionDifferenceOtherSegment
    StateCalcVelDifferenceOtherSegment
    StateCalcPositionVelDifferenceOtherSegment
    StateCalcValueAtSegment
    StateCalcMaxValue
    StateCalcMinValue
    StateCalcMeanValue
    StateCalcMedianValue
    StateCalcStandardDeviation
    StateCalcNegative
    StateCalcEccentricity
    StateCalcMeanAnomaly
    StateCalcRAAN
    BDotRCalc
    BDotTCalc
    BMagnitudeCalc
    BThetaCalc
    StateCalcDeltaDec
    StateCalcDeltaRA
    StateCalcBetaAngle
    StateCalcLocalApparentSolarLon
    StateCalcLonOfPeriapsis
    StateCalcOrbitStateValue
    StateCalcSignedEccentricity
    StateCalcInclination
    StateCalcTrueLon
    StateCalcPower
    StateCalcRelMotion
    StateCalcSolarBetaAngle
    StateCalcSolarInPlaneAngle
    StateCalcRelPositionDecAngle
    StateCalcRelPositionInPlaneAngle
    StateCalcRelativeInclination
    StateCalcCurvilinearRelMotion
    StateCalcCustomFunction
    StateCalcScript
    StateCalcCd
    StateCalcCr
    StateCalcDragArea
    StateCalcRadiationPressureArea
    StateCalcRadiationPressureCoefficient
    StateCalcSRPArea
    StateCalcCosOfVerticalFPA
    StateCalcDec
    StateCalcFPA
    StateCalcRMagnitude
    StateCalcRA
    StateCalcVMagnitude
    StateCalcVelAz
    StateCalcC3Energy
    StateCalcInAsympDec
    StateCalcInAsympRA
    StateCalcInVelAzAtPeriapsis
    StateCalcOutAsympDec
    StateCalcOutAsympRA
    StateCalcOutVelAzAtPeriapsis
    StateCalcDuration
    StateCalcUserValue
    StateCalcVectorGeometryToolAngle
    StateCalcAngle
    StateCalcDotProduct
    StateCalcVectorDec
    StateCalcVectorMagnitude
    StateCalcVectorRA
    StateCalcVectorX
    StateCalcOnePointAccess
    StateCalcDifferenceAcrossSegmentsOtherSat
    StateCalcValueAtSegmentOtherSat
    StateCalcRARate
    StateCalcDecRate
    StateCalcGravitationalParameter
    StateCalcReferenceRadius
    StateCalcGravCoeff
    StateCalcSpeedOfLight
    StateCalcPi
    StateCalcScalar
    StateCalcApparentSolarTime
    StateCalcEarthMeanSolarTime
    StateCalcEarthMeanLocTimeAN
    AutomaticSequenceCollection
    AutomaticSequence
    CentralBodyCollection
    AstrogatorCentralBody
    CentralBodyGravityModel
    CentralBodyShapeSphere
    CentralBodyShapeOblateSpheroid
    CentralBodyShapeTriaxialEllipsoid
    CentralBodyAttitudeRotationCoefficientsFile
    CentralBodyAttitudeIAU1994
    CentralBodyEphemerisAnalyticOrbit
    CentralBodyEphemerisJPLSpice
    CentralBodyEphemerisFile
    CentralBodyEphemerisJPLDesignExplorerOptimizer
    CentralBodyEphemerisPlanetary
    MissionControlSequenceSegmentProperties
    PowerInternal
    PowerProcessed
    PowerSolarArray
    GeneralRelativityFunction
    StateTransformationFunction
    CR3BPFunc
    RadiationPressureFunction
    YarkovskyFunc
    BlendedDensity
    Cira72Function
    Exponential
    HarrisPriester
    DensityModelPlugin
    JacchiaRoberts
    JacchiaBowman2008
    Jacchia_1960
    Jacchia_1970
    Jacchia_1971
    MSISE_1990
    MSIS_1986
    NRLMSISE_2000
    US_Standard_Atmosphere
    MarsGRAM37
    MarsGRAM2000
    MarsGRAM2001
    MarsGRAM2005
    MarsGRAM2010
    VenusGRAM2005
    DTM2012
    DTM2020
    GravityFieldFunction
    PointMassFunction
    TwoBodyFunction
    HPOPPluginFunction
    EOMFuncPluginFunction
    SRPAeroT20
    SRPAeroT30
    SRPGSPM04aIIA
    SRPGSPM04aIIR
    SRPGSPM04aeIIA
    SRPGSPM04aeIIR
    SRPSpherical
    SRPNPlate
    SRPTabAreaVec
    SRPVariableArea
    ThirdBodyFunction
    DragModelPlugin
    SRPReflectionPlugin
    EngineConstAcc
    EngineConstant
    EngineIon
    EngineThrottleTable
    EngineCustom
    EnginePlugin
    EngineModelPoly
    EngineModelThrustCoefficients
    EngineModelIspCoefficients
    EngineDefinition
    DesignCR3BPSetup
    DesignCR3BPObject
    DesignCR3BPObjectCollection
    Thruster
    ThrusterSetCollection
    ThrusterSet
    AsTriggerCondition
    CustomFunctionScriptEngine
    NumericalPropagatorWrapper
    NumericalPropagatorWrapperCR3BP
    PropagatorFunctionCollection
    BulirschStoerIntegrator
    GaussJacksonIntegrator
    RungeKutta2nd3rd
    RungeKutta4th
    RungeKutta4th5th
    RungeKutta4thAdapt
    RungeKuttaF7th8th
    RungeKuttaV8th9th
    ScriptingTool
    ScriptingSegmentCollection
    ScriptingSegment
    ScriptingParameterCollection
    ScriptingParameter
    ScriptingCalcObject
    ScriptingCalcObjectCollection
    UserVariableDefinition
    UserVariable
    UserVariableUpdate
    UserVariableDefinitionCollection
    UserVariableCollection
    UserVariableUpdateCollection
    CalculationGraphCollection
    ScriptingParameterEnumerationChoice
    ScriptingParameterEnumerationChoiceCollection
    ProfileSNOPTOptimizer
    SNOPTControl
    SNOPTResult
    SNOPTControlCollection
    SNOPTResultCollection
    ProfileIPOPTOptimizer
    IPOPTControl
    IPOPTResult
    IPOPTControlCollection
    IPOPTResultCollection
    ManeuverOptimalFinite
    ManeuverOptimalFiniteSNOPTOptimizer
    ManeuverOptimalFiniteInitialBoundaryConditions
    ManeuverOptimalFiniteFinalBoundaryConditions
    ManeuverOptimalFinitePathBoundaryConditions
    ManeuverOptimalFiniteSteeringNodeElement
    ManeuverOptimalFiniteSteeringNodeCollection
    ManeuverOptimalFiniteBounds
    ProfileLambertProfile
    ProfileLambertSearchProfile
    ProfileGoldenSection
    GoldenSectionControlCollection
    GoldenSectionControl
    GoldenSectionResultCollection
    GoldenSectionResult
    ProfileGridSearch
    GridSearchControlCollection
    GridSearchControl
    GridSearchResultCollection
    GridSearchResult
    CalcObjectLinkEmbedControlCollection
    ProfileBisection
    BisectionControl
    BisectionControlCollection
    BisectionResult
    BisectionResultCollection


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: IUserVariableDefinitionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IUserVariableCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IUserVariableUpdateCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICalculationGraphCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IConstraintCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IPluginProperties
    :members:
    :exclude-members: __init__
.. autoclass:: ISNOPTControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ISNOPTResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IIPOPTControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IIPOPTResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverOptimalFiniteSNOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverOptimalFiniteInitialBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverOptimalFiniteFinalBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverOptimalFinitePathBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverOptimalFiniteSteeringNodeCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverOptimalFiniteBounds
    :members:
    :exclude-members: __init__
.. autoclass:: IGoldenSectionControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IGoldenSectionControl
    :members:
    :exclude-members: __init__
.. autoclass:: IGoldenSectionResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IGoldenSectionResult
    :members:
    :exclude-members: __init__
.. autoclass:: IGridSearchControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IGridSearchControl
    :members:
    :exclude-members: __init__
.. autoclass:: IGridSearchResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IGridSearchResult
    :members:
    :exclude-members: __init__
.. autoclass:: IBisectionControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IBisectionResult
    :members:
    :exclude-members: __init__
.. autoclass:: IBisectionResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IStoppingConditionElement
    :members:
    :exclude-members: __init__
.. autoclass:: IStoppingConditionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IState
    :members:
    :exclude-members: __init__
.. autoclass:: IStoppingConditionComponent
    :members:
    :exclude-members: __init__
.. autoclass:: IAutomaticSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IAutomaticSequenceCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IBPlaneCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverFinitePropagator
    :members:
    :exclude-members: __init__
.. autoclass:: IBurnoutVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlFinite
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlImpulsive
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlOptimalFinite
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: IDisplaySystem
    :members:
    :exclude-members: __init__
.. autoclass:: IBurnout
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingParameterEnumerationChoice
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingParameterEnumerationChoiceCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingParameter
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingParameterCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingCalcObject
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingCalcObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IScriptingTool
    :members:
    :exclude-members: __init__
.. autoclass:: IElement
    :members:
    :exclude-members: __init__
.. autoclass:: ISpacecraftParameters
    :members:
    :exclude-members: __init__
.. autoclass:: IFuelTank
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceSegmentProperties
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceEnd
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceInitialState
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IDriverMissionControlSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IElementCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: IElementKeplerian
    :members:
    :exclude-members: __init__
.. autoclass:: IElementDelaunay
    :members:
    :exclude-members: __init__
.. autoclass:: IElementEquinoctial
    :members:
    :exclude-members: __init__
.. autoclass:: IElementMixedSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: IElementSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: IElementTargetVectorIncomingAsymptote
    :members:
    :exclude-members: __init__
.. autoclass:: IElementTargetVectorOutgoingAsymptote
    :members:
    :exclude-members: __init__
.. autoclass:: IElementGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: IElementBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ILightingStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAccessStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequencePropagate
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceBackwardSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: IDisplaySystemGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: IDisplaySystemGeocentric
    :members:
    :exclude-members: __init__
.. autoclass:: IBurnoutCBFCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: IBurnoutGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: IBurnoutGeocentric
    :members:
    :exclude-members: __init__
.. autoclass:: IBurnoutLaunchAzAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: IBurnoutLaunchAzRadius
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverFinite
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverImpulsive
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlImpulsiveVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlImpulsiveAntiVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlImpulsiveAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlImpulsiveFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlImpulsiveThrustVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlFiniteAntiVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlFiniteAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlFiniteFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlFiniteThrustVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlFiniteTimeVarying
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlFiniteVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlFinitePlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeControlOptimalFiniteLagrange
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceHold
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceReturn
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceStop
    :members:
    :exclude-members: __init__
.. autoclass:: IProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IMissionControlSequenceTargetSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IDifferentialCorrectorControl
    :members:
    :exclude-members: __init__
.. autoclass:: IDifferentialCorrectorResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISearchPluginControl
    :members:
    :exclude-members: __init__
.. autoclass:: ISearchPluginResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISearchPluginResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ISearchPluginControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IDifferentialCorrectorControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IDifferentialCorrectorResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ITargeterGraphActiveControl
    :members:
    :exclude-members: __init__
.. autoclass:: ITargeterGraphResult
    :members:
    :exclude-members: __init__
.. autoclass:: ITargeterGraphActiveControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ITargeterGraphResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ITargeterGraph
    :members:
    :exclude-members: __init__
.. autoclass:: ITargeterGraphCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileSearchPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileDifferentialCorrector
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileChangeManeuverType
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileScriptingTool
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileChangeReturnSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileChangePropagator
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileChangeStopSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileChangeStoppingConditionState
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileSeedFiniteManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileRunOnce
    :members:
    :exclude-members: __init__
.. autoclass:: IUserVariableDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: IUserVariable
    :members:
    :exclude-members: __init__
.. autoclass:: IUserVariableUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileSNOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: ISNOPTControl
    :members:
    :exclude-members: __init__
.. autoclass:: ISNOPTResult
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileIPOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: IIPOPTControl
    :members:
    :exclude-members: __init__
.. autoclass:: IIPOPTResult
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverOptimalFinite
    :members:
    :exclude-members: __init__
.. autoclass:: IManeuverOptimalFiniteSteeringNodeElement
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileLambertProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileLambertSearchProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileGoldenSection
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileGridSearch
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcObjectLinkEmbedControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileBisection
    :members:
    :exclude-members: __init__
.. autoclass:: IBisectionControl
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcHeightAboveTerrain
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOrbitDelaunayG
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOrbitDelaunayH
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOrbitDelaunayL
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOrbitSemiLatusRectum
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcJacobiConstant
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCartesianElem
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCartSTMElem
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSTMEigenval
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSTMEigenvecElem
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEnvironment
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEquinoctialElem
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDamageFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDamageMassFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMagnitudeFieldDipoleL
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSEETMagnitudeFieldFieldLineSepAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcImpactFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcImpactMassFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSEETSAAFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSEETVehTemp
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCloseApproachBearing
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCloseApproachMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCloseApproachTheta
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCloseApproachX
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCloseApproachY
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCloseApproachCosBearing
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRelGroundTrackError
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRelAtAOLMaster
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDeltaFromMaster
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcLonDriftRate
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMeanEarthLon
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRectifiedLon
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcTrueLongitude
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcGeodeticTrueLongitude
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcGeodeticTrueLongitudeAtTimeOfPerigee
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMeanRightAscension
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcGeodeticMeanRightAscension
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcTwoBodyDriftRate
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDriftRateFactor
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEccentricityX
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEccentricityY
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInclinationX
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInclinationY
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcUnitAngularMomentumX
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcUnitAngularMomentumY
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcUnitAngularMomentumZ
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcGeodeticElem
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRepeatingGroundTrackErr
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcAltitudeOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcAltitudeOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcArgOfLat
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcArgOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEccentricityAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInclination
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcLonOfAscNode
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMeanAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMeanMotion
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOrbitPeriod
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcNumRevs
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRAAN
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRadOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRadOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSemiMajorAxis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcTimePastAscNode
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcTimePastPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMissionControlSequenceDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMissionControlSequenceDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSequenceDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSequenceDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcFuelMass
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDensity
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInertialDeltaVMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInertialDeltaVx
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInertialDeltaVy
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInertialDeltaVz
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcManeuverSpecificImpulse
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcPressure
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcTemperature
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVectorX
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVectorY
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVectorZ
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMass
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcManeuverTotalMassFlowRate
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcAbsoluteValue
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDifference
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcPositionDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcPositionVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcValueAtSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMaxValue
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMinValue
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMeanValue
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMedianValue
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcStandardDeviation
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcNegative
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcTrueAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: IBDotRCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IBDotTCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IBMagnitudeCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IBThetaCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDeltaDec
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDeltaRA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcBetaAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcLocalApparentSolarLon
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcLonOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOrbitStateValue
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSignedEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcTrueLon
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcPower
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRelMotion
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSolarBetaAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSolarInPlaneAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRelPositionDecAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRelPositionInPlaneAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRelativeInclination
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCurvilinearRelMotion
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCustomFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcScript
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCd
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCr
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDragArea
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRadiationPressureArea
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRadiationPressureCoefficient
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSRPArea
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcCosOfVerticalFPA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDec
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcFPA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVelAz
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcC3Energy
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInAsympDec
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInAsympRA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcInVelAzAtPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOutAsympDec
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOutAsympRA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOutVelAzAtPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDuration
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcUserValue
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVectorGeometryToolAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVectorDec
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVectorMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVectorRA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOnePointAccess
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDifferenceAcrossSegmentsOtherSat
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcValueAtSegmentOtherSat
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRARate
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcDecRate
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcGravitationalParameter
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcReferenceRadius
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcGravCoeff
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSpeedOfLight
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcPi
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcApparentSolarTime
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEarthMeanSolarTime
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEarthMeanLocTimeAN
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyEphemeris
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyGravityModel
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyShape
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyShapeSphere
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyShapeOblateSpheroid
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyShapeTriaxialEllipsoid
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyAttitudeRotationCoefficientsFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyAttitudeIAU1994
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyEphemerisAnalyticOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyEphemerisJPLSpice
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyEphemerisFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyEphemerisJPLDesignExplorerOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyEphemerisPlanetary
    :members:
    :exclude-members: __init__
.. autoclass:: IAstrogatorCentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: IPowerInternal
    :members:
    :exclude-members: __init__
.. autoclass:: IPowerProcessed
    :members:
    :exclude-members: __init__
.. autoclass:: IPowerSolarArray
    :members:
    :exclude-members: __init__
.. autoclass:: IGeneralRelativityFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IStateTransformationFunction
    :members:
    :exclude-members: __init__
.. autoclass:: ICR3BPFunc
    :members:
    :exclude-members: __init__
.. autoclass:: IRadiationPressureFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IYarkovskyFunc
    :members:
    :exclude-members: __init__
.. autoclass:: IBlendedDensity
    :members:
    :exclude-members: __init__
.. autoclass:: IDragModelPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: ICira72Function
    :members:
    :exclude-members: __init__
.. autoclass:: IExponential
    :members:
    :exclude-members: __init__
.. autoclass:: IHarrisPriester
    :members:
    :exclude-members: __init__
.. autoclass:: IDensityModelPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IJacchiaRoberts
    :members:
    :exclude-members: __init__
.. autoclass:: IJacchiaBowman2008
    :members:
    :exclude-members: __init__
.. autoclass:: IJacchia_1960
    :members:
    :exclude-members: __init__
.. autoclass:: IJacchia_1970
    :members:
    :exclude-members: __init__
.. autoclass:: IJacchia_1971
    :members:
    :exclude-members: __init__
.. autoclass:: IMSISE_1990
    :members:
    :exclude-members: __init__
.. autoclass:: IMSIS_1986
    :members:
    :exclude-members: __init__
.. autoclass:: INRLMSISE_2000
    :members:
    :exclude-members: __init__
.. autoclass:: IUS_Standard_Atmosphere
    :members:
    :exclude-members: __init__
.. autoclass:: IMarsGRAM37
    :members:
    :exclude-members: __init__
.. autoclass:: IMarsGRAM2005
    :members:
    :exclude-members: __init__
.. autoclass:: IVenusGRAM2005
    :members:
    :exclude-members: __init__
.. autoclass:: IMarsGRAM2010
    :members:
    :exclude-members: __init__
.. autoclass:: IMarsGRAM2001
    :members:
    :exclude-members: __init__
.. autoclass:: IMarsGRAM2000
    :members:
    :exclude-members: __init__
.. autoclass:: IDTM2012
    :members:
    :exclude-members: __init__
.. autoclass:: IDTM2020
    :members:
    :exclude-members: __init__
.. autoclass:: IGravityFieldFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IPointMassFunction
    :members:
    :exclude-members: __init__
.. autoclass:: ITwoBodyFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IHPOPPluginFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IEOMFuncPluginFunction
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPAeroT20
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPAeroT30
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPGSPM04aIIA
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPGSPM04aIIR
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPGSPM04aeIIA
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPGSPM04aeIIR
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPNPlate
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPTabAreaVec
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPVariableArea
    :members:
    :exclude-members: __init__
.. autoclass:: IThirdBodyFunction
    :members:
    :exclude-members: __init__
.. autoclass:: ISRPReflectionPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineModelThrustCoefficients
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineModelIspCoefficients
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineConstAcc
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineConstant
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineThrottleTable
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineIon
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineCustom
    :members:
    :exclude-members: __init__
.. autoclass:: IEnginePlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IEngineModelPoly
    :members:
    :exclude-members: __init__
.. autoclass:: IDesignCR3BPObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IDesignCR3BPSetup
    :members:
    :exclude-members: __init__
.. autoclass:: IDesignCR3BPObject
    :members:
    :exclude-members: __init__
.. autoclass:: IThruster
    :members:
    :exclude-members: __init__
.. autoclass:: IThrusterSetCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IThrusterSet
    :members:
    :exclude-members: __init__
.. autoclass:: IAsTriggerCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ICustomFunctionScriptEngine
    :members:
    :exclude-members: __init__
.. autoclass:: INumericalIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: IPropagatorFunctionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: INumericalPropagatorWrapper
    :members:
    :exclude-members: __init__
.. autoclass:: INumericalPropagatorWrapperCR3BP
    :members:
    :exclude-members: __init__
.. autoclass:: IBulirschStoerIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: IGaussJacksonIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: IRungeKutta2nd3rd
    :members:
    :exclude-members: __init__
.. autoclass:: IRungeKutta4th
    :members:
    :exclude-members: __init__
.. autoclass:: IRungeKutta4th5th
    :members:
    :exclude-members: __init__
.. autoclass:: IRungeKutta4thAdapt
    :members:
    :exclude-members: __init__
.. autoclass:: IRungeKuttaF7th8th
    :members:
    :exclude-members: __init__
.. autoclass:: IRungeKuttaV8th9th
    :members:
    :exclude-members: __init__


Enumerations
~~~~~~~~~~~~

.. autoenum:: GRAPH_OPTION
    :members:
.. autoenum:: SMART_RUN_MODE
    :members:
.. autoenum:: FORMULATION
    :members:
.. autoenum:: LIGHTING_CONDITION
    :members:
.. autoenum:: PROFILE
    :members:
.. autoenum:: ACCESS_CRITERION
    :members:
.. autoenum:: ECLIPSING_BODIES_SOURCE
    :members:
.. autoenum:: CRITERION
    :members:
.. autoenum:: CALC_OBJECT_REFERENCE
    :members:
.. autoenum:: CALC_OBJECT_CENTRAL_BODY_REFERENCE
    :members:
.. autoenum:: CALC_OBJECT_ELEM
    :members:
.. autoenum:: PROFILE_MODE
    :members:
.. autoenum:: CONTROL_STOPPING_CONDITION
    :members:
.. autoenum:: STATE
    :members:
.. autoenum:: RETURN_CONTROL
    :members:
.. autoenum:: DRAW_PERTURBATION
    :members:
.. autoenum:: DERIVE_CALC_METHOD
    :members:
.. autoenum:: CONVERGENCE_CRITERIA
    :members:
.. autoenum:: DIFFERENTIAL_CORRECTOR_SCALING_METHOD
    :members:
.. autoenum:: CONTROL_UPDATE
    :members:
.. autoenum:: CONTROL_FOLLOW
    :members:
.. autoenum:: CONTROL_INIT_STATE
    :members:
.. autoenum:: CONTROL_MANEUVER
    :members:
.. autoenum:: CONTROL_LAUNCH
    :members:
.. autoenum:: CONTROL_ADVANCED
    :members:
.. autoenum:: TARGET_SEQ_ACTION
    :members:
.. autoenum:: PROFILES_FINISH
    :members:
.. autoenum:: UPDATE_PARAM
    :members:
.. autoenum:: UPDATE_ACTION
    :members:
.. autoenum:: PRESSURE_MODE
    :members:
.. autoenum:: THRUST_TYPE
    :members:
.. autoenum:: ATTITUDE_UPDATE
    :members:
.. autoenum:: PROPULSION_METHOD
    :members:
.. autoenum:: CUSTOM_FUNCTION
    :members:
.. autoenum:: BODY_AXIS
    :members:
.. autoenum:: CONSTRAINT_SIGN
    :members:
.. autoenum:: ATTITUDE_CONTROL
    :members:
.. autoenum:: FOLLOW_JOIN
    :members:
.. autoenum:: FOLLOW_SEPARATION
    :members:
.. autoenum:: FOLLOW_SPACECRAFT_AND_FUEL_TANK
    :members:
.. autoenum:: BURNOUT_OPTIONS
    :members:
.. autoenum:: BURNOUT_TYPE
    :members:
.. autoenum:: ASCENT_TYPE
    :members:
.. autoenum:: LAUNCH_DISPLAY_SYSTEM
    :members:
.. autoenum:: RUN_CODE
    :members:
.. autoenum:: SEQUENCE_STATE_TO_PASS
    :members:
.. autoenum:: MANEUVER_TYPE
    :members:
.. autoenum:: SEGMENT_TYPE
    :members:
.. autoenum:: ELEMENT_TYPE
    :members:
.. autoenum:: LANGUAGE
    :members:
.. autoenum:: STOPPING_CONDITION
    :members:
.. autoenum:: CLEAR_EPHEMERIS_DIRECTION
    :members:
.. autoenum:: PROFILE_INSERT_DIRECTION
    :members:
.. autoenum:: ROOT_FINDING_ALGORITHM
    :members:
.. autoenum:: SCRIPTING_PARAMETER_TYPE
    :members:
.. autoenum:: SNOPT_GOAL
    :members:
.. autoenum:: IPOPT_GOAL
    :members:
.. autoenum:: OPTIMAL_FINITE_SEED_METHOD
    :members:
.. autoenum:: OPTIMAL_FINITE_RUN_MODE
    :members:
.. autoenum:: OPTIMAL_FINITE_DISCRETIZATION_STRATEGY
    :members:
.. autoenum:: OPTIMAL_FINITE_WORKING_VARIABLES
    :members:
.. autoenum:: OPTIMAL_FINITE_SCALING_OPTIONS
    :members:
.. autoenum:: OPTIMAL_FINITE_SNOPT_OBJECTIVE
    :members:
.. autoenum:: OPTIMAL_FINITE_SNOPT_SCALING
    :members:
.. autoenum:: OPTIMAL_FINITE_EXPORT_NODES_FORMAT
    :members:
.. autoenum:: OPTIMAL_FINITE_GUESS_METHOD
    :members:
.. autoenum:: IMP_DELTA_V_REP
    :members:
.. autoenum:: LAMBERT_TARGET_COORD_TYPE
    :members:
.. autoenum:: LAMBERT_SOLUTION_OPTION_TYPE
    :members:
.. autoenum:: LAMBERT_ORBITAL_ENERGY_TYPE
    :members:
.. autoenum:: LAMBERT_DIRECTION_OF_MOTION_TYPE
    :members:
.. autoenum:: GOLDEN_SECTION_DESIRED_OPERATION
    :members:
.. autoenum:: GRID_SEARCH_DESIRED_OPERATION
    :members:
.. autoenum:: ELEMENT
    :members:
.. autoenum:: BASE_SELECTION
    :members:
.. autoenum:: CONTROL_ORBIT_STATE_VALUE
    :members:
.. autoenum:: SEGMENT_STATE
    :members:
.. autoenum:: DIFFERENCE_ORDER
    :members:
.. autoenum:: SEGMENT_DIFFERENCE_ORDER
    :members:
.. autoenum:: CONTROL_REPEATING_GROUND_TRACK_ERR
    :members:
.. autoenum:: CALC_OBJECT_DIRECTION
    :members:
.. autoenum:: CALC_OBJECT_ORBIT_PLANE_SOURCE
    :members:
.. autoenum:: CALC_OBJECT_SUN_POSITION
    :members:
.. autoenum:: CALC_OBJECT_ANGLE_SIGN
    :members:
.. autoenum:: CALC_OBJECT_REFERENCE_DIRECTION
    :members:
.. autoenum:: CALC_OBJECT_RELATIVE_POSITION
    :members:
.. autoenum:: CALC_OBJECT_REFERENCE_ELLIPSE
    :members:
.. autoenum:: CALC_OBJECT_LOCATION_SOURCE
    :members:
.. autoenum:: GRAVITATIONAL_PARAMETER_SOURCE
    :members:
.. autoenum:: REFERENCE_RADIUS_SOURCE
    :members:
.. autoenum:: GRAV_COEFF_NORMALIZATION_TYPE
    :members:
.. autoenum:: GRAV_COEFF_COEFFICIENT_TYPE
    :members:
.. autoenum:: STM_PERT_VARIABLES
    :members:
.. autoenum:: STM_EIGEN_NUMBER
    :members:
.. autoenum:: COMPLEX_NUMBER
    :members:
.. autoenum:: SQUARED_TYPE
    :members:
.. autoenum:: GEO_STATIONARY_DRIFT_RATE_MODEL
    :members:
.. autoenum:: GEO_STATIONARY_INCLINATION_MAGNITUDE
    :members:
.. autoenum:: CENTRAL_BODY_GRAVITY_MODEL
    :members:
.. autoenum:: CENTRAL_BODY_SHAPE
    :members:
.. autoenum:: CENTRAL_BODY_ATTITUDE
    :members:
.. autoenum:: CENTRAL_BODY_EPHEMERIS
    :members:
.. autoenum:: CONTROL_POWER_INTERNAL
    :members:
.. autoenum:: CONTROL_POWER_PROCESSED
    :members:
.. autoenum:: CONTROL_POWER_SOLAR_ARRAY
    :members:
.. autoenum:: THIRD_BODY_MODE
    :members:
.. autoenum:: GRAV_PARAM_SOURCE
    :members:
.. autoenum:: EPHEM_SOURCE
    :members:
.. autoenum:: SOLAR_FORCE_METHOD
    :members:
.. autoenum:: SHADOW_MODEL
    :members:
.. autoenum:: SUN_POSITION
    :members:
.. autoenum:: ATMOS_DATA_SOURCE
    :members:
.. autoenum:: GEO_MAGNETIC_FLUX_SOURCE
    :members:
.. autoenum:: GEO_MAGNETIC_FLUX_UPDATE_RATE
    :members:
.. autoenum:: DRAG_MODEL_TYPE
    :members:
.. autoenum:: MARS_GRAM_DENSITY_TYPE
    :members:
.. autoenum:: VENUS_GRAM_DENSITY_TYPE
    :members:
.. autoenum:: TAB_VEC_INTERP_METHOD
    :members:
.. autoenum:: CONTROL_ENGINE_CONST_ACC
    :members:
.. autoenum:: CONTROL_ENGINE_CONSTANT
    :members:
.. autoenum:: CONTROL_ENGINE_CUSTOM
    :members:
.. autoenum:: CONTROL_ENGINE_THROTTLE_TABLE
    :members:
.. autoenum:: CONTROL_ENGINE_ION
    :members:
.. autoenum:: CONTROL_ENGINE_MODEL_POLY
    :members:
.. autoenum:: ENGINE_MODEL_FUNCTION
    :members:
.. autoenum:: THROTTLE_TABLE_OPERATION_MODE
    :members:
.. autoenum:: IDEAL_ORBIT_RADIUS
    :members:
.. autoenum:: ROTATING_COORDINATE_SYSTEM
    :members:
.. autoenum:: CONTROL_THRUSTERS
    :members:
.. autoenum:: THRUSTER_DIRECTION
    :members:
.. autoenum:: CRITERIA
    :members:
.. autoenum:: ERROR_CONTROL
    :members:
.. autoenum:: PREDICTOR_CORRECTOR
    :members:
.. autoenum:: NUMERICAL_INTEGRATOR
    :members:
.. autoenum:: COEFF_RUNGE_KUTTA_V_8TH9_TH
    :members:


Classes
~~~~~~~

.. autoclass:: DriverMissionControlSequence
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceEnd
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceInitialState
    :members:
    :exclude-members: __init__
.. autoclass:: SpacecraftParameters
    :members:
    :exclude-members: __init__
.. autoclass:: FuelTank
    :members:
    :exclude-members: __init__
.. autoclass:: ElementCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: ElementKeplerian
    :members:
    :exclude-members: __init__
.. autoclass:: ElementEquinoctial
    :members:
    :exclude-members: __init__
.. autoclass:: ElementDelaunay
    :members:
    :exclude-members: __init__
.. autoclass:: ElementMixedSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: ElementSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: ElementTargetVectorIncomingAsymptote
    :members:
    :exclude-members: __init__
.. autoclass:: ElementTargetVectorOutgoingAsymptote
    :members:
    :exclude-members: __init__
.. autoclass:: ElementGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: ElementBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequencePropagate
    :members:
    :exclude-members: __init__
.. autoclass:: State
    :members:
    :exclude-members: __init__
.. autoclass:: StoppingConditionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AccessStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: LightingStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: StoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: StoppingConditionElement
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceSequence
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceBackwardSequence
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: DisplaySystemGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: DisplaySystemGeocentric
    :members:
    :exclude-members: __init__
.. autoclass:: BurnoutGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: BurnoutCBFCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: BurnoutGeocentric
    :members:
    :exclude-members: __init__
.. autoclass:: BurnoutLaunchAzAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: BurnoutLaunchAzRadius
    :members:
    :exclude-members: __init__
.. autoclass:: BurnoutVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceFollow
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverFinite
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverImpulsive
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlImpulsiveVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlImpulsiveAntiVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlImpulsiveAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlImpulsiveFile
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlImpulsiveThrustVector
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlFiniteAntiVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlFiniteAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlFiniteFile
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlFiniteThrustVector
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlFiniteTimeVarying
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlFiniteVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlFinitePlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeControlOptimalFiniteLagrange
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverFinitePropagator
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceHold
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceReturn
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceStop
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceTargetSequence
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileCollection
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceOptions
    :members:
    :exclude-members: __init__
.. autoclass:: CalcObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ConstraintCollection
    :members:
    :exclude-members: __init__
.. autoclass:: PluginProperties
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileSearchPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: TargeterGraph
    :members:
    :exclude-members: __init__
.. autoclass:: TargeterGraphCollection
    :members:
    :exclude-members: __init__
.. autoclass:: TargeterGraphResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: TargeterGraphActiveControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: TargeterGraphActiveControl
    :members:
    :exclude-members: __init__
.. autoclass:: TargeterGraphResult
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileDifferentialCorrector
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileScriptingTool
    :members:
    :exclude-members: __init__
.. autoclass:: DifferentialCorrectorControl
    :members:
    :exclude-members: __init__
.. autoclass:: DifferentialCorrectorResult
    :members:
    :exclude-members: __init__
.. autoclass:: DifferentialCorrectorControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: DifferentialCorrectorResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: SearchPluginControl
    :members:
    :exclude-members: __init__
.. autoclass:: SearchPluginControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: SearchPluginResult
    :members:
    :exclude-members: __init__
.. autoclass:: SearchPluginResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileChangeManeuverType
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileChangeReturnSegment
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileChangePropagator
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileChangeStopSegment
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileChangeStoppingConditionState
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileSeedFiniteManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileRunOnce
    :members:
    :exclude-members: __init__
.. autoclass:: BPlaneCollection
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDamageFlux
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDamageMassFlux
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMagnitudeFieldDipoleL
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSEETMagnitudeFieldFieldLineSepAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcImpactFlux
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcImpactMassFlux
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSEETSAAFlux
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSEETVehTemp
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcJacobiConstant
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCartesianElem
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCartSTMElem
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSTMEigenval
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSTMEigenvecElem
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEnvironment
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOrbitDelaunayG
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOrbitDelaunayH
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOrbitDelaunayL
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOrbitSemiLatusRectum
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEquinoctialElem
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCloseApproachBearing
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCloseApproachMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCloseApproachTheta
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCloseApproachX
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCloseApproachY
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCloseApproachCosBearing
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRelGroundTrackError
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRelAtAOLMaster
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDeltaFromMaster
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcLonDriftRate
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMeanEarthLon
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRectifiedLon
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcTrueLongitude
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcGeodeticTrueLongitude
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcGeodeticTrueLongitudeAtTimeOfPerigee
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMeanRightAscension
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcGeodeticMeanRightAscension
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcTwoBodyDriftRate
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDriftRateFactor
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEccentricityX
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEccentricityY
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInclinationX
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInclinationY
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcUnitAngularMomentumX
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcUnitAngularMomentumY
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcUnitAngularMomentumZ
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcHeightAboveTerrain
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcGeodeticElem
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRepeatingGroundTrackErr
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcAltitudeOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcAltitudeOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcArgOfLat
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcArgOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEccentricityAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcLonOfAscNode
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMeanMotion
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOrbitPeriod
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcNumRevs
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRadOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRadOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSemiMajorAxis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcTimePastAscNode
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcTimePastPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcTrueAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMissionControlSequenceDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMissionControlSequenceDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSequenceDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSequenceDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcFuelMass
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDensity
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInertialDeltaVMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInertialDeltaVx
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInertialDeltaVy
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInertialDeltaVz
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcManeuverSpecificImpulse
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcPressure
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcTemperature
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorY
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorZ
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMass
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcManeuverTotalMassFlowRate
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcAbsoluteValue
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDifference
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcPositionDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcPositionVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcValueAtSegment
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMaxValue
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMinValue
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMeanValue
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMedianValue
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcStandardDeviation
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcNegative
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMeanAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRAAN
    :members:
    :exclude-members: __init__
.. autoclass:: BDotRCalc
    :members:
    :exclude-members: __init__
.. autoclass:: BDotTCalc
    :members:
    :exclude-members: __init__
.. autoclass:: BMagnitudeCalc
    :members:
    :exclude-members: __init__
.. autoclass:: BThetaCalc
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDeltaDec
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDeltaRA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcBetaAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcLocalApparentSolarLon
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcLonOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOrbitStateValue
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSignedEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInclination
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcTrueLon
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcPower
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRelMotion
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSolarBetaAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSolarInPlaneAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRelPositionDecAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRelPositionInPlaneAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRelativeInclination
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCurvilinearRelMotion
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCustomFunction
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcScript
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCd
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCr
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDragArea
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRadiationPressureArea
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRadiationPressureCoefficient
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSRPArea
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcCosOfVerticalFPA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDec
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcFPA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVelAz
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcC3Energy
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInAsympDec
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInAsympRA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcInVelAzAtPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOutAsympDec
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOutAsympRA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOutVelAzAtPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDuration
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcUserValue
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorGeometryToolAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorDec
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorRA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorX
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOnePointAccess
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDifferenceAcrossSegmentsOtherSat
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcValueAtSegmentOtherSat
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRARate
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcDecRate
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcGravitationalParameter
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcReferenceRadius
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcGravCoeff
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSpeedOfLight
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcPi
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcApparentSolarTime
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEarthMeanSolarTime
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEarthMeanLocTimeAN
    :members:
    :exclude-members: __init__
.. autoclass:: AutomaticSequenceCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AutomaticSequence
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AstrogatorCentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyGravityModel
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyShapeSphere
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyShapeOblateSpheroid
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyShapeTriaxialEllipsoid
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyAttitudeRotationCoefficientsFile
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyAttitudeIAU1994
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyEphemerisAnalyticOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyEphemerisJPLSpice
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyEphemerisFile
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyEphemerisJPLDesignExplorerOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyEphemerisPlanetary
    :members:
    :exclude-members: __init__
.. autoclass:: MissionControlSequenceSegmentProperties
    :members:
    :exclude-members: __init__
.. autoclass:: PowerInternal
    :members:
    :exclude-members: __init__
.. autoclass:: PowerProcessed
    :members:
    :exclude-members: __init__
.. autoclass:: PowerSolarArray
    :members:
    :exclude-members: __init__
.. autoclass:: GeneralRelativityFunction
    :members:
    :exclude-members: __init__
.. autoclass:: StateTransformationFunction
    :members:
    :exclude-members: __init__
.. autoclass:: CR3BPFunc
    :members:
    :exclude-members: __init__
.. autoclass:: RadiationPressureFunction
    :members:
    :exclude-members: __init__
.. autoclass:: YarkovskyFunc
    :members:
    :exclude-members: __init__
.. autoclass:: BlendedDensity
    :members:
    :exclude-members: __init__
.. autoclass:: Cira72Function
    :members:
    :exclude-members: __init__
.. autoclass:: Exponential
    :members:
    :exclude-members: __init__
.. autoclass:: HarrisPriester
    :members:
    :exclude-members: __init__
.. autoclass:: DensityModelPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: JacchiaRoberts
    :members:
    :exclude-members: __init__
.. autoclass:: JacchiaBowman2008
    :members:
    :exclude-members: __init__
.. autoclass:: Jacchia_1960
    :members:
    :exclude-members: __init__
.. autoclass:: Jacchia_1970
    :members:
    :exclude-members: __init__
.. autoclass:: Jacchia_1971
    :members:
    :exclude-members: __init__
.. autoclass:: MSISE_1990
    :members:
    :exclude-members: __init__
.. autoclass:: MSIS_1986
    :members:
    :exclude-members: __init__
.. autoclass:: NRLMSISE_2000
    :members:
    :exclude-members: __init__
.. autoclass:: US_Standard_Atmosphere
    :members:
    :exclude-members: __init__
.. autoclass:: MarsGRAM37
    :members:
    :exclude-members: __init__
.. autoclass:: MarsGRAM2000
    :members:
    :exclude-members: __init__
.. autoclass:: MarsGRAM2001
    :members:
    :exclude-members: __init__
.. autoclass:: MarsGRAM2005
    :members:
    :exclude-members: __init__
.. autoclass:: MarsGRAM2010
    :members:
    :exclude-members: __init__
.. autoclass:: VenusGRAM2005
    :members:
    :exclude-members: __init__
.. autoclass:: DTM2012
    :members:
    :exclude-members: __init__
.. autoclass:: DTM2020
    :members:
    :exclude-members: __init__
.. autoclass:: GravityFieldFunction
    :members:
    :exclude-members: __init__
.. autoclass:: PointMassFunction
    :members:
    :exclude-members: __init__
.. autoclass:: TwoBodyFunction
    :members:
    :exclude-members: __init__
.. autoclass:: HPOPPluginFunction
    :members:
    :exclude-members: __init__
.. autoclass:: EOMFuncPluginFunction
    :members:
    :exclude-members: __init__
.. autoclass:: SRPAeroT20
    :members:
    :exclude-members: __init__
.. autoclass:: SRPAeroT30
    :members:
    :exclude-members: __init__
.. autoclass:: SRPGSPM04aIIA
    :members:
    :exclude-members: __init__
.. autoclass:: SRPGSPM04aIIR
    :members:
    :exclude-members: __init__
.. autoclass:: SRPGSPM04aeIIA
    :members:
    :exclude-members: __init__
.. autoclass:: SRPGSPM04aeIIR
    :members:
    :exclude-members: __init__
.. autoclass:: SRPSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: SRPNPlate
    :members:
    :exclude-members: __init__
.. autoclass:: SRPTabAreaVec
    :members:
    :exclude-members: __init__
.. autoclass:: SRPVariableArea
    :members:
    :exclude-members: __init__
.. autoclass:: ThirdBodyFunction
    :members:
    :exclude-members: __init__
.. autoclass:: DragModelPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: SRPReflectionPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: EngineConstAcc
    :members:
    :exclude-members: __init__
.. autoclass:: EngineConstant
    :members:
    :exclude-members: __init__
.. autoclass:: EngineIon
    :members:
    :exclude-members: __init__
.. autoclass:: EngineThrottleTable
    :members:
    :exclude-members: __init__
.. autoclass:: EngineCustom
    :members:
    :exclude-members: __init__
.. autoclass:: EnginePlugin
    :members:
    :exclude-members: __init__
.. autoclass:: EngineModelPoly
    :members:
    :exclude-members: __init__
.. autoclass:: EngineModelThrustCoefficients
    :members:
    :exclude-members: __init__
.. autoclass:: EngineModelIspCoefficients
    :members:
    :exclude-members: __init__
.. autoclass:: EngineDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: DesignCR3BPSetup
    :members:
    :exclude-members: __init__
.. autoclass:: DesignCR3BPObject
    :members:
    :exclude-members: __init__
.. autoclass:: DesignCR3BPObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: Thruster
    :members:
    :exclude-members: __init__
.. autoclass:: ThrusterSetCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ThrusterSet
    :members:
    :exclude-members: __init__
.. autoclass:: AsTriggerCondition
    :members:
    :exclude-members: __init__
.. autoclass:: CustomFunctionScriptEngine
    :members:
    :exclude-members: __init__
.. autoclass:: NumericalPropagatorWrapper
    :members:
    :exclude-members: __init__
.. autoclass:: NumericalPropagatorWrapperCR3BP
    :members:
    :exclude-members: __init__
.. autoclass:: PropagatorFunctionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: BulirschStoerIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: GaussJacksonIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: RungeKutta2nd3rd
    :members:
    :exclude-members: __init__
.. autoclass:: RungeKutta4th
    :members:
    :exclude-members: __init__
.. autoclass:: RungeKutta4th5th
    :members:
    :exclude-members: __init__
.. autoclass:: RungeKutta4thAdapt
    :members:
    :exclude-members: __init__
.. autoclass:: RungeKuttaF7th8th
    :members:
    :exclude-members: __init__
.. autoclass:: RungeKuttaV8th9th
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingTool
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingSegment
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingParameterCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingParameter
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingCalcObject
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingCalcObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: UserVariableDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: UserVariable
    :members:
    :exclude-members: __init__
.. autoclass:: UserVariableUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: UserVariableDefinitionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: UserVariableCollection
    :members:
    :exclude-members: __init__
.. autoclass:: UserVariableUpdateCollection
    :members:
    :exclude-members: __init__
.. autoclass:: CalculationGraphCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingParameterEnumerationChoice
    :members:
    :exclude-members: __init__
.. autoclass:: ScriptingParameterEnumerationChoiceCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileSNOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: SNOPTControl
    :members:
    :exclude-members: __init__
.. autoclass:: SNOPTResult
    :members:
    :exclude-members: __init__
.. autoclass:: SNOPTControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: SNOPTResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileIPOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: IPOPTControl
    :members:
    :exclude-members: __init__
.. autoclass:: IPOPTResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPOPTControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IPOPTResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverOptimalFinite
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverOptimalFiniteSNOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverOptimalFiniteInitialBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverOptimalFiniteFinalBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverOptimalFinitePathBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverOptimalFiniteSteeringNodeElement
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverOptimalFiniteSteeringNodeCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ManeuverOptimalFiniteBounds
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileLambertProfile
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileLambertSearchProfile
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileGoldenSection
    :members:
    :exclude-members: __init__
.. autoclass:: GoldenSectionControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: GoldenSectionControl
    :members:
    :exclude-members: __init__
.. autoclass:: GoldenSectionResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: GoldenSectionResult
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileGridSearch
    :members:
    :exclude-members: __init__
.. autoclass:: GridSearchControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: GridSearchControl
    :members:
    :exclude-members: __init__
.. autoclass:: GridSearchResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: GridSearchResult
    :members:
    :exclude-members: __init__
.. autoclass:: CalcObjectLinkEmbedControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileBisection
    :members:
    :exclude-members: __init__
.. autoclass:: BisectionControl
    :members:
    :exclude-members: __init__
.. autoclass:: BisectionControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: BisectionResult
    :members:
    :exclude-members: __init__
.. autoclass:: BisectionResultCollection
    :members:
    :exclude-members: __init__

