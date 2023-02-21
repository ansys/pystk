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
    IStoppingConditionElement
    IStoppingConditionCollection
    IMCSSegmentCollection
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
    IMCSSegmentProperties
    IMCSEnd
    IMCSInitialState
    IMCSSegment
    IMCSOptions
    IDriverMCS
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
    IMCSPropagate
    IMCSSequence
    IMCSBackwardSequence
    IMCSLaunch
    IDisplaySystemGeodetic
    IDisplaySystemGeocentric
    IBurnoutCBFCartesian
    IBurnoutGeodetic
    IBurnoutGeocentric
    IBurnoutLaunchAzAlt
    IBurnoutLaunchAzRadius
    IMCSFollow
    IMCSManeuver
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
    IMCSHold
    IMCSUpdate
    IMCSReturn
    IMCSStop
    IProfile
    IProfileCollection
    IMCSTargetSequence
    IDCControl
    IDCResult
    ISearchPluginControl
    ISearchPluginResult
    ISearchPluginResultCollection
    ISearchPluginControlCollection
    IDCControlCollection
    IDCResultCollection
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
    IStateCalcMagFieldDipoleL
    IStateCalcSEETMagFieldFieldLineSepAngle
    IStateCalcImpactFlux
    IStateCalcImpactMassFlux
    IStateCalcSEETSAAFlux
    IStateCalcSEETVehTemp
    IStateCalcCloseApproachBearing
    IStateCalcCloseApproachMag
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
    IStateCalcGeodeticElem
    IStateCalcRepeatingGroundTrackErr
    IStateCalcAltOfApoapsis
    IStateCalcAltOfPeriapsis
    IStateCalcArgOfLat
    IStateCalcArgOfPeriapsis
    IStateCalcEccAnomaly
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
    IStateCalcMCSDeltaV
    IStateCalcMCSDeltaVSquared
    IStateCalcSequenceDeltaV
    IStateCalcSequenceDeltaVSquared
    IStateCalcFuelMass
    IStateCalcDensity
    IStateCalcInertialDeltaVMag
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
    IStateCalcPosDifferenceOtherSegment
    IStateCalcVelDifferenceOtherSegment
    IStateCalcPosVelDifferenceOtherSegment
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
    IBMagCalc
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
    IStateCalcRelPosDecAngle
    IStateCalcRelPosInPlaneAngle
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
    IStateCalcRMag
    IStateCalcRA
    IStateCalcVMag
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
    IStateCalcCrdnAngle
    IStateCalcAngle
    IStateCalcDotProduct
    IStateCalcVectorDec
    IStateCalcVectorMag
    IStateCalcVectorRA
    IStateCalcOnePtAccess
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
    ICbEphemeris
    ICbGravityModel
    ICbShape
    ICbShapeSphere
    ICbShapeOblateSpheroid
    ICbShapeTriaxialEllipsoid
    ICbAttitude
    ICbAttitudeRotationCoefficientsFile
    ICbAttitudeIAU1994
    ICbEphemerisAnalyticOrbit
    ICbEphemerisJPLSpice
    ICbEphemerisFile
    ICbEphemerisJPLDE
    ICbEphemerisPlanetary
    IAstrogatorCentralBody
    IPowerInternal
    IPowerProcessed
    IPowerSolarArray
    IGeneralRelativityFunction
    IStateTransFunction
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
    IRK2nd3rd
    IRK4th
    IRK4th5th
    IRK4thAdapt
    IRKF7th8th
    IRKV8th9th


Enumerations
~~~~~~~~~~~~

.. autosummary::

    AgEVAGraphOption
    AgEVASmartRunMode
    AgEVAFormulation
    AgEVALightingCondition
    AgEVAProfile
    AgEVAAccessCriterion
    AgEVAEclipsingBodiesSource
    AgEVACriterion
    AgEVACalcObjectReference
    AgEVACalcObjectCentralBodyReference
    AgEVACalcObjectElem
    AgEVAProfileMode
    AgEVAControlStoppingCondition
    AgEVAState
    AgEVAReturnControl
    AgEVADrawPerturbation
    AgEVADeriveCalcMethod
    AgEVAConvergenceCriteria
    AgEVADCScalingMethod
    AgEVAControlUpdate
    AgEVAControlFollow
    AgEVAControlInitState
    AgEVAControlManeuver
    AgEVAControlLaunch
    AgEVAControlAdvanced
    AgEVATargetSeqAction
    AgEVAProfilesFinish
    AgEVAUpdateParam
    AgEVAUpdateAction
    AgEVAPressureMode
    AgEVAThrustType
    AgEVAAttitudeUpdate
    AgEVAPropulsionMethod
    AgEVACustomFunction
    AgEVABodyAxis
    AgEVAConstraintSign
    AgEVAAttitudeControl
    AgEVAFollowJoin
    AgEVAFollowSeparation
    AgEVAFollowSpacecraftAndFuelTank
    AgEVABurnoutOptions
    AgEVABurnoutType
    AgEVAAscentType
    AgEVALaunchDisplaySystem
    AgEVARunCode
    AgEVASequenceStateToPass
    AgEVAManeuverType
    AgEVASegmentType
    AgEVAElementType
    AgEVALanguage
    AgEVAStoppingCondition
    AgEVAClearEphemerisDirection
    AgEVAProfileInsertDirection
    AgEVARootFindingAlgorithm
    AgEVAScriptingParameterType
    AgEVASNOPTGoal
    AgEVAIPOPTGoal
    AgEVAOptimalFiniteSeedMethod
    AgEVAOptimalFiniteRunMode
    AgEVAOptimalFiniteDiscretizationStrategy
    AgEVAOptimalFiniteWorkingVariables
    AgEVAOptimalFiniteScalingOptions
    AgEVAOptimalFiniteSNOPTObjective
    AgEVAOptimalFiniteSNOPTScaling
    AgEVAOptimalFiniteExportNodesFormat
    AgEVAOptimalFiniteGuessMethod
    AgEVAImpDeltaVRep
    AgEVALambertTargetCoordType
    AgEVALambertSolutionOptionType
    AgEVALambertOrbitalEnergyType
    AgEVALambertDirectionOfMotionType
    AgEVAGoldenSectionDesiredOperation
    AgEVAGridSearchDesiredOperation
    AgEVAElement
    AgEVABaseSelection
    AgEVAControlOrbitStateValue
    AgEVASegmentState
    AgEVADifferenceOrder
    AgEVASegmentDifferenceOrder
    AgEVAControlRepeatingGroundTrackErr
    AgEVACalcObjectDirection
    AgEVACalcObjectOrbitPlaneSource
    AgEVACalcObjectSunPosition
    AgEVACalcObjectAngleSign
    AgEVACalcObjectReferenceDirection
    AgEVACalcObjectRelativePosition
    AgEVACalcObjectReferenceEllipse
    AgEVACalcObjectLocationSource
    AgEVAGravitationalParameterSource
    AgEVAReferenceRadiusSource
    AgEVAGravCoeffNormalizationType
    AgEVAGravCoeffCoefficientType
    AgEVASTMPertVariables
    AgEVASTMEigenNumber
    AgEVAComplexNumber
    AgEVASquaredType
    AgEVACbGravityModel
    AgEVACbShape
    AgEVACbAttitude
    AgEVACbEphemeris
    AgEVAControlPowerInternal
    AgEVAControlPowerProcessed
    AgEVAControlPowerSolarArray
    AgEVAThirdBodyMode
    AgEVAGravParamSource
    AgEVAEphemSource
    AgEVASolarForceMethod
    AgEVAShadowModel
    AgEVASunPosition
    AgEVAAtmosDataSource
    AgEVAGeoMagneticFluxSource
    AgEVAGeoMagneticFluxUpdateRate
    AgEVADragModelType
    AgEVAMarsGRAMDensityType
    AgEVAVenusGRAMDensityType
    AgEVATabVecInterpMethod
    AgEVAControlEngineConstAcc
    AgEVAControlEngineConstant
    AgEVAControlEngineCustom
    AgEVAControlEngineThrottleTable
    AgEVAControlEngineIon
    AgEVAControlEngineModelPoly
    AgEVAEngineModelFunction
    AgEVAThrottleTableOperationMode
    AgEVAControlThrusters
    AgEVAThrusterDirection
    AgEVACriteria
    AgEVAErrorControl
    AgEVAPredictorCorrector
    AgEVANumericalIntegrator
    AgEVACoeffRKV8th9th


Classes
~~~~~~~

.. autosummary::

    DriverMCS
    MCSSegmentCollection
    MCSEnd
    MCSInitialState
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
    MCSPropagate
    State
    StoppingConditionCollection
    AccessStoppingCondition
    LightingStoppingCondition
    StoppingCondition
    StoppingConditionElement
    MCSSequence
    MCSBackwardSequence
    MCSLaunch
    DisplaySystemGeodetic
    DisplaySystemGeocentric
    BurnoutGeodetic
    BurnoutCBFCartesian
    BurnoutGeocentric
    BurnoutLaunchAzAlt
    BurnoutLaunchAzRadius
    BurnoutVelocity
    MCSFollow
    MCSManeuver
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
    MCSHold
    MCSUpdate
    MCSReturn
    MCSStop
    MCSTargetSequence
    ProfileCollection
    MCSOptions
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
    DCControl
    DCResult
    DCControlCollection
    DCResultCollection
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
    StateCalcMagFieldDipoleL
    StateCalcSEETMagFieldFieldLineSepAngle
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
    StateCalcCloseApproachMag
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
    StateCalcHeightAboveTerrain
    StateCalcGeodeticElem
    StateCalcRepeatingGroundTrackErr
    StateCalcAltOfApoapsis
    StateCalcAltOfPeriapsis
    StateCalcArgOfLat
    StateCalcArgOfPeriapsis
    StateCalcEccAnomaly
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
    StateCalcMCSDeltaV
    StateCalcMCSDeltaVSquared
    StateCalcSequenceDeltaV
    StateCalcSequenceDeltaVSquared
    StateCalcFuelMass
    StateCalcDensity
    StateCalcInertialDeltaVMag
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
    StateCalcPosDifferenceOtherSegment
    StateCalcVelDifferenceOtherSegment
    StateCalcPosVelDifferenceOtherSegment
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
    BMagCalc
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
    StateCalcRelPosDecAngle
    StateCalcRelPosInPlaneAngle
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
    StateCalcRMag
    StateCalcRA
    StateCalcVMag
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
    StateCalcCrdnAngle
    StateCalcAngle
    StateCalcDotProduct
    StateCalcVectorDec
    StateCalcVectorMag
    StateCalcVectorRA
    StateCalcVectorX
    StateCalcOnePtAccess
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
    CbGravityModel
    CbShapeSphere
    CbShapeOblateSpheroid
    CbShapeTriaxialEllipsoid
    CbAttitudeRotationCoefficientsFile
    CbAttitudeIAU1994
    CbEphemerisAnalyticOrbit
    CbEphemerisJPLSpice
    CbEphemerisFile
    CbEphemerisJPLDE
    CbEphemerisPlanetary
    MCSSegmentProperties
    PowerInternal
    PowerProcessed
    PowerSolarArray
    GeneralRelativityFunction
    StateTransFunction
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
    RK2nd3rd
    RK4th
    RK4th5th
    RK4thAdapt
    RKF7th8th
    RKV8th9th
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
.. autoclass:: IStoppingConditionElement
    :members:
    :exclude-members: __init__
.. autoclass:: IStoppingConditionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSSegmentCollection
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
.. autoclass:: IMCSSegmentProperties
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSEnd
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSInitialState
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IDriverMCS
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
.. autoclass:: IMCSPropagate
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSBackwardSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSLaunch
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
.. autoclass:: IBurnoutLaunchAzAlt
    :members:
    :exclude-members: __init__
.. autoclass:: IBurnoutLaunchAzRadius
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSManeuver
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
.. autoclass:: IMCSHold
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSReturn
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSStop
    :members:
    :exclude-members: __init__
.. autoclass:: IProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IProfileCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IMCSTargetSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IDCControl
    :members:
    :exclude-members: __init__
.. autoclass:: IDCResult
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
.. autoclass:: IDCControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IDCResultCollection
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
.. autoclass:: IStateCalcMagFieldDipoleL
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcSEETMagFieldFieldLineSepAngle
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
.. autoclass:: IStateCalcCloseApproachMag
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
.. autoclass:: IStateCalcGeodeticElem
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRepeatingGroundTrackErr
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcAltOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcAltOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcArgOfLat
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcArgOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcEccAnomaly
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
.. autoclass:: IStateCalcMCSDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcMCSDeltaVSquared
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
.. autoclass:: IStateCalcInertialDeltaVMag
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
.. autoclass:: IStateCalcPosDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcPosVelDifferenceOtherSegment
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
.. autoclass:: IBMagCalc
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
.. autoclass:: IStateCalcRelPosDecAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRelPosInPlaneAngle
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
.. autoclass:: IStateCalcRMag
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcRA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVMag
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
.. autoclass:: IStateCalcCrdnAngle
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
.. autoclass:: IStateCalcVectorMag
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcVectorRA
    :members:
    :exclude-members: __init__
.. autoclass:: IStateCalcOnePtAccess
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
.. autoclass:: ICbEphemeris
    :members:
    :exclude-members: __init__
.. autoclass:: ICbGravityModel
    :members:
    :exclude-members: __init__
.. autoclass:: ICbShape
    :members:
    :exclude-members: __init__
.. autoclass:: ICbShapeSphere
    :members:
    :exclude-members: __init__
.. autoclass:: ICbShapeOblateSpheroid
    :members:
    :exclude-members: __init__
.. autoclass:: ICbShapeTriaxialEllipsoid
    :members:
    :exclude-members: __init__
.. autoclass:: ICbAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: ICbAttitudeRotationCoefficientsFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICbAttitudeIAU1994
    :members:
    :exclude-members: __init__
.. autoclass:: ICbEphemerisAnalyticOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: ICbEphemerisJPLSpice
    :members:
    :exclude-members: __init__
.. autoclass:: ICbEphemerisFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICbEphemerisJPLDE
    :members:
    :exclude-members: __init__
.. autoclass:: ICbEphemerisPlanetary
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
.. autoclass:: IStateTransFunction
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
.. autoclass:: IRK2nd3rd
    :members:
    :exclude-members: __init__
.. autoclass:: IRK4th
    :members:
    :exclude-members: __init__
.. autoclass:: IRK4th5th
    :members:
    :exclude-members: __init__
.. autoclass:: IRK4thAdapt
    :members:
    :exclude-members: __init__
.. autoclass:: IRKF7th8th
    :members:
    :exclude-members: __init__
.. autoclass:: IRKV8th9th
    :members:
    :exclude-members: __init__


Enumerations
~~~~~~~~~~~~

.. autoenum:: AgEVAGraphOption
    :members:
.. autoenum:: AgEVASmartRunMode
    :members:
.. autoenum:: AgEVAFormulation
    :members:
.. autoenum:: AgEVALightingCondition
    :members:
.. autoenum:: AgEVAProfile
    :members:
.. autoenum:: AgEVAAccessCriterion
    :members:
.. autoenum:: AgEVAEclipsingBodiesSource
    :members:
.. autoenum:: AgEVACriterion
    :members:
.. autoenum:: AgEVACalcObjectReference
    :members:
.. autoenum:: AgEVACalcObjectCentralBodyReference
    :members:
.. autoenum:: AgEVACalcObjectElem
    :members:
.. autoenum:: AgEVAProfileMode
    :members:
.. autoenum:: AgEVAControlStoppingCondition
    :members:
.. autoenum:: AgEVAState
    :members:
.. autoenum:: AgEVAReturnControl
    :members:
.. autoenum:: AgEVADrawPerturbation
    :members:
.. autoenum:: AgEVADeriveCalcMethod
    :members:
.. autoenum:: AgEVAConvergenceCriteria
    :members:
.. autoenum:: AgEVADCScalingMethod
    :members:
.. autoenum:: AgEVAControlUpdate
    :members:
.. autoenum:: AgEVAControlFollow
    :members:
.. autoenum:: AgEVAControlInitState
    :members:
.. autoenum:: AgEVAControlManeuver
    :members:
.. autoenum:: AgEVAControlLaunch
    :members:
.. autoenum:: AgEVAControlAdvanced
    :members:
.. autoenum:: AgEVATargetSeqAction
    :members:
.. autoenum:: AgEVAProfilesFinish
    :members:
.. autoenum:: AgEVAUpdateParam
    :members:
.. autoenum:: AgEVAUpdateAction
    :members:
.. autoenum:: AgEVAPressureMode
    :members:
.. autoenum:: AgEVAThrustType
    :members:
.. autoenum:: AgEVAAttitudeUpdate
    :members:
.. autoenum:: AgEVAPropulsionMethod
    :members:
.. autoenum:: AgEVACustomFunction
    :members:
.. autoenum:: AgEVABodyAxis
    :members:
.. autoenum:: AgEVAConstraintSign
    :members:
.. autoenum:: AgEVAAttitudeControl
    :members:
.. autoenum:: AgEVAFollowJoin
    :members:
.. autoenum:: AgEVAFollowSeparation
    :members:
.. autoenum:: AgEVAFollowSpacecraftAndFuelTank
    :members:
.. autoenum:: AgEVABurnoutOptions
    :members:
.. autoenum:: AgEVABurnoutType
    :members:
.. autoenum:: AgEVAAscentType
    :members:
.. autoenum:: AgEVALaunchDisplaySystem
    :members:
.. autoenum:: AgEVARunCode
    :members:
.. autoenum:: AgEVASequenceStateToPass
    :members:
.. autoenum:: AgEVAManeuverType
    :members:
.. autoenum:: AgEVASegmentType
    :members:
.. autoenum:: AgEVAElementType
    :members:
.. autoenum:: AgEVALanguage
    :members:
.. autoenum:: AgEVAStoppingCondition
    :members:
.. autoenum:: AgEVAClearEphemerisDirection
    :members:
.. autoenum:: AgEVAProfileInsertDirection
    :members:
.. autoenum:: AgEVARootFindingAlgorithm
    :members:
.. autoenum:: AgEVAScriptingParameterType
    :members:
.. autoenum:: AgEVASNOPTGoal
    :members:
.. autoenum:: AgEVAIPOPTGoal
    :members:
.. autoenum:: AgEVAOptimalFiniteSeedMethod
    :members:
.. autoenum:: AgEVAOptimalFiniteRunMode
    :members:
.. autoenum:: AgEVAOptimalFiniteDiscretizationStrategy
    :members:
.. autoenum:: AgEVAOptimalFiniteWorkingVariables
    :members:
.. autoenum:: AgEVAOptimalFiniteScalingOptions
    :members:
.. autoenum:: AgEVAOptimalFiniteSNOPTObjective
    :members:
.. autoenum:: AgEVAOptimalFiniteSNOPTScaling
    :members:
.. autoenum:: AgEVAOptimalFiniteExportNodesFormat
    :members:
.. autoenum:: AgEVAOptimalFiniteGuessMethod
    :members:
.. autoenum:: AgEVAImpDeltaVRep
    :members:
.. autoenum:: AgEVALambertTargetCoordType
    :members:
.. autoenum:: AgEVALambertSolutionOptionType
    :members:
.. autoenum:: AgEVALambertOrbitalEnergyType
    :members:
.. autoenum:: AgEVALambertDirectionOfMotionType
    :members:
.. autoenum:: AgEVAGoldenSectionDesiredOperation
    :members:
.. autoenum:: AgEVAGridSearchDesiredOperation
    :members:
.. autoenum:: AgEVAElement
    :members:
.. autoenum:: AgEVABaseSelection
    :members:
.. autoenum:: AgEVAControlOrbitStateValue
    :members:
.. autoenum:: AgEVASegmentState
    :members:
.. autoenum:: AgEVADifferenceOrder
    :members:
.. autoenum:: AgEVASegmentDifferenceOrder
    :members:
.. autoenum:: AgEVAControlRepeatingGroundTrackErr
    :members:
.. autoenum:: AgEVACalcObjectDirection
    :members:
.. autoenum:: AgEVACalcObjectOrbitPlaneSource
    :members:
.. autoenum:: AgEVACalcObjectSunPosition
    :members:
.. autoenum:: AgEVACalcObjectAngleSign
    :members:
.. autoenum:: AgEVACalcObjectReferenceDirection
    :members:
.. autoenum:: AgEVACalcObjectRelativePosition
    :members:
.. autoenum:: AgEVACalcObjectReferenceEllipse
    :members:
.. autoenum:: AgEVACalcObjectLocationSource
    :members:
.. autoenum:: AgEVAGravitationalParameterSource
    :members:
.. autoenum:: AgEVAReferenceRadiusSource
    :members:
.. autoenum:: AgEVAGravCoeffNormalizationType
    :members:
.. autoenum:: AgEVAGravCoeffCoefficientType
    :members:
.. autoenum:: AgEVASTMPertVariables
    :members:
.. autoenum:: AgEVASTMEigenNumber
    :members:
.. autoenum:: AgEVAComplexNumber
    :members:
.. autoenum:: AgEVASquaredType
    :members:
.. autoenum:: AgEVACbGravityModel
    :members:
.. autoenum:: AgEVACbShape
    :members:
.. autoenum:: AgEVACbAttitude
    :members:
.. autoenum:: AgEVACbEphemeris
    :members:
.. autoenum:: AgEVAControlPowerInternal
    :members:
.. autoenum:: AgEVAControlPowerProcessed
    :members:
.. autoenum:: AgEVAControlPowerSolarArray
    :members:
.. autoenum:: AgEVAThirdBodyMode
    :members:
.. autoenum:: AgEVAGravParamSource
    :members:
.. autoenum:: AgEVAEphemSource
    :members:
.. autoenum:: AgEVASolarForceMethod
    :members:
.. autoenum:: AgEVAShadowModel
    :members:
.. autoenum:: AgEVASunPosition
    :members:
.. autoenum:: AgEVAAtmosDataSource
    :members:
.. autoenum:: AgEVAGeoMagneticFluxSource
    :members:
.. autoenum:: AgEVAGeoMagneticFluxUpdateRate
    :members:
.. autoenum:: AgEVADragModelType
    :members:
.. autoenum:: AgEVAMarsGRAMDensityType
    :members:
.. autoenum:: AgEVAVenusGRAMDensityType
    :members:
.. autoenum:: AgEVATabVecInterpMethod
    :members:
.. autoenum:: AgEVAControlEngineConstAcc
    :members:
.. autoenum:: AgEVAControlEngineConstant
    :members:
.. autoenum:: AgEVAControlEngineCustom
    :members:
.. autoenum:: AgEVAControlEngineThrottleTable
    :members:
.. autoenum:: AgEVAControlEngineIon
    :members:
.. autoenum:: AgEVAControlEngineModelPoly
    :members:
.. autoenum:: AgEVAEngineModelFunction
    :members:
.. autoenum:: AgEVAThrottleTableOperationMode
    :members:
.. autoenum:: AgEVAControlThrusters
    :members:
.. autoenum:: AgEVAThrusterDirection
    :members:
.. autoenum:: AgEVACriteria
    :members:
.. autoenum:: AgEVAErrorControl
    :members:
.. autoenum:: AgEVAPredictorCorrector
    :members:
.. autoenum:: AgEVANumericalIntegrator
    :members:
.. autoenum:: AgEVACoeffRKV8th9th
    :members:


Classes
~~~~~~~

.. autoclass:: DriverMCS
    :members:
    :exclude-members: __init__
.. autoclass:: MCSSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: MCSEnd
    :members:
    :exclude-members: __init__
.. autoclass:: MCSInitialState
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
.. autoclass:: MCSPropagate
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
.. autoclass:: MCSSequence
    :members:
    :exclude-members: __init__
.. autoclass:: MCSBackwardSequence
    :members:
    :exclude-members: __init__
.. autoclass:: MCSLaunch
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
.. autoclass:: BurnoutLaunchAzAlt
    :members:
    :exclude-members: __init__
.. autoclass:: BurnoutLaunchAzRadius
    :members:
    :exclude-members: __init__
.. autoclass:: BurnoutVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: MCSFollow
    :members:
    :exclude-members: __init__
.. autoclass:: MCSManeuver
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
.. autoclass:: MCSHold
    :members:
    :exclude-members: __init__
.. autoclass:: MCSUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: MCSReturn
    :members:
    :exclude-members: __init__
.. autoclass:: MCSStop
    :members:
    :exclude-members: __init__
.. autoclass:: MCSTargetSequence
    :members:
    :exclude-members: __init__
.. autoclass:: ProfileCollection
    :members:
    :exclude-members: __init__
.. autoclass:: MCSOptions
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
.. autoclass:: DCControl
    :members:
    :exclude-members: __init__
.. autoclass:: DCResult
    :members:
    :exclude-members: __init__
.. autoclass:: DCControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: DCResultCollection
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
.. autoclass:: StateCalcMagFieldDipoleL
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcSEETMagFieldFieldLineSepAngle
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
.. autoclass:: StateCalcCloseApproachMag
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
.. autoclass:: StateCalcHeightAboveTerrain
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcGeodeticElem
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRepeatingGroundTrackErr
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcAltOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcAltOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcArgOfLat
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcArgOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcEccAnomaly
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
.. autoclass:: StateCalcMCSDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcMCSDeltaVSquared
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
.. autoclass:: StateCalcInertialDeltaVMag
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
.. autoclass:: StateCalcPosDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcPosVelDifferenceOtherSegment
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
.. autoclass:: BMagCalc
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
.. autoclass:: StateCalcRelPosDecAngle
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRelPosInPlaneAngle
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
.. autoclass:: StateCalcRMag
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcRA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVMag
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
.. autoclass:: StateCalcCrdnAngle
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
.. autoclass:: StateCalcVectorMag
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorRA
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcVectorX
    :members:
    :exclude-members: __init__
.. autoclass:: StateCalcOnePtAccess
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
.. autoclass:: CbGravityModel
    :members:
    :exclude-members: __init__
.. autoclass:: CbShapeSphere
    :members:
    :exclude-members: __init__
.. autoclass:: CbShapeOblateSpheroid
    :members:
    :exclude-members: __init__
.. autoclass:: CbShapeTriaxialEllipsoid
    :members:
    :exclude-members: __init__
.. autoclass:: CbAttitudeRotationCoefficientsFile
    :members:
    :exclude-members: __init__
.. autoclass:: CbAttitudeIAU1994
    :members:
    :exclude-members: __init__
.. autoclass:: CbEphemerisAnalyticOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: CbEphemerisJPLSpice
    :members:
    :exclude-members: __init__
.. autoclass:: CbEphemerisFile
    :members:
    :exclude-members: __init__
.. autoclass:: CbEphemerisJPLDE
    :members:
    :exclude-members: __init__
.. autoclass:: CbEphemerisPlanetary
    :members:
    :exclude-members: __init__
.. autoclass:: MCSSegmentProperties
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
.. autoclass:: StateTransFunction
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
.. autoclass:: RK2nd3rd
    :members:
    :exclude-members: __init__
.. autoclass:: RK4th
    :members:
    :exclude-members: __init__
.. autoclass:: RK4th5th
    :members:
    :exclude-members: __init__
.. autoclass:: RK4thAdapt
    :members:
    :exclude-members: __init__
.. autoclass:: RKF7th8th
    :members:
    :exclude-members: __init__
.. autoclass:: RKV8th9th
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

