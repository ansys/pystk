Module contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    IAgVAUserVariableDefinitionCollection
    IAgVAUserVariableCollection
    IAgVAUserVariableUpdateCollection
    IAgVACalculationGraphCollection
    IAgVAConstraintCollection
    IAgVAPluginProperties
    IAgVASNOPTControlCollection
    IAgVASNOPTResultCollection
    IAgVAIPOPTControlCollection
    IAgVAIPOPTResultCollection
    IAgVAManeuverOptimalFiniteSNOPTOptimizer
    IAgVAManeuverOptimalFiniteInitialBoundaryConditions
    IAgVAManeuverOptimalFiniteFinalBoundaryConditions
    IAgVAManeuverOptimalFinitePathBoundaryConditions
    IAgVAManeuverOptimalFiniteSteeringNodeCollection
    IAgVAManeuverOptimalFiniteBounds
    IAgVAGoldenSectionControlCollection
    IAgVAGoldenSectionControl
    IAgVAGoldenSectionResultCollection
    IAgVAGoldenSectionResult
    IAgVAGridSearchControlCollection
    IAgVAGridSearchControl
    IAgVAGridSearchResultCollection
    IAgVAGridSearchResult
    IAgVAStoppingConditionElement
    IAgVAStoppingConditionCollection
    IAgVAMCSSegmentCollection
    IAgVAState
    IAgVAStoppingConditionComponent
    IAgVAAutomaticSequence
    IAgVAAutomaticSequenceCollection
    IAgVABPlaneCollection
    IAgVACalcObjectCollection
    IAgVAManeuverFinitePropagator
    IAgVABurnoutVelocity
    IAgVAAttitudeControl
    IAgVAAttitudeControlFinite
    IAgVAAttitudeControlImpulsive
    IAgVAAttitudeControlOptimalFinite
    IAgVAManeuver
    IAgVADisplaySystem
    IAgVABurnout
    IAgVAScriptingSegment
    IAgVAScriptingSegmentCollection
    IAgVAScriptingParameterEnumerationChoice
    IAgVAScriptingParameterEnumerationChoiceCollection
    IAgVAScriptingParameter
    IAgVAScriptingParameterCollection
    IAgVAScriptingCalcObject
    IAgVAScriptingCalcObjectCollection
    IAgVAScriptingTool
    IAgVAElement
    IAgVASpacecraftParameters
    IAgVAFuelTank
    IAgVAMCSSegmentProperties
    IAgVAMCSEnd
    IAgVAMCSInitialState
    IAgVAMCSSegment
    IAgVAMCSOptions
    IAgVADriverMCS
    IAgVAElementCartesian
    IAgVAElementKeplerian
    IAgVAElementDelaunay
    IAgVAElementEquinoctial
    IAgVAElementMixedSpherical
    IAgVAElementSpherical
    IAgVAElementTargetVectorIncomingAsymptote
    IAgVAElementTargetVectorOutgoingAsymptote
    IAgVAElementGeodetic
    IAgVAStoppingCondition
    IAgVALightingStoppingCondition
    IAgVAAccessStoppingCondition
    IAgVAMCSPropagate
    IAgVAMCSSequence
    IAgVAMCSBackwardSequence
    IAgVAMCSLaunch
    IAgVADisplaySystemGeodetic
    IAgVADisplaySystemGeocentric
    IAgVABurnoutCBFCartesian
    IAgVABurnoutGeodetic
    IAgVABurnoutGeocentric
    IAgVABurnoutLaunchAzAlt
    IAgVABurnoutLaunchAzRadius
    IAgVAMCSFollow
    IAgVAMCSManeuver
    IAgVAManeuverFinite
    IAgVAManeuverImpulsive
    IAgVAAttitudeControlImpulsiveVelocityVector
    IAgVAAttitudeControlImpulsiveAntiVelocityVector
    IAgVAAttitudeControlImpulsiveAttitude
    IAgVAAttitudeControlImpulsiveFile
    IAgVAAttitudeControlImpulsiveThrustVector
    IAgVAAttitudeControlFiniteAntiVelocityVector
    IAgVAAttitudeControlFiniteAttitude
    IAgVAAttitudeControlFiniteFile
    IAgVAAttitudeControlFiniteThrustVector
    IAgVAAttitudeControlFiniteTimeVarying
    IAgVAAttitudeControlFiniteVelocityVector
    IAgVAAttitudeControlFinitePlugin
    IAgVAAttitudeControlOptimalFiniteLagrange
    IAgVAMCSHold
    IAgVAMCSUpdate
    IAgVAMCSReturn
    IAgVAMCSStop
    IAgVAProfile
    IAgVAProfileCollection
    IAgVAMCSTargetSequence
    IAgVADCControl
    IAgVADCResult
    IAgVASearchPluginControl
    IAgVASearchPluginResult
    IAgVASearchPluginResultCollection
    IAgVASearchPluginControlCollection
    IAgVADCControlCollection
    IAgVADCResultCollection
    IAgVATargeterGraphActiveControl
    IAgVATargeterGraphResult
    IAgVATargeterGraphActiveControlCollection
    IAgVATargeterGraphResultCollection
    IAgVATargeterGraph
    IAgVATargeterGraphCollection
    IAgVAProfileSearchPlugin
    IAgVAProfileDifferentialCorrector
    IAgVAProfileChangeManeuverType
    IAgVAProfileScriptingTool
    IAgVAProfileChangeReturnSegment
    IAgVAProfileChangePropagator
    IAgVAProfileChangeStopSegment
    IAgVAProfileChangeStoppingConditionState
    IAgVAProfileSeedFiniteManeuver
    IAgVAProfileRunOnce
    IAgVAUserVariableDefinition
    IAgVAUserVariable
    IAgVAUserVariableUpdate
    IAgVAProfileSNOPTOptimizer
    IAgVASNOPTControl
    IAgVASNOPTResult
    IAgVAProfileIPOPTOptimizer
    IAgVAIPOPTControl
    IAgVAIPOPTResult
    IAgVAManeuverOptimalFinite
    IAgVAManeuverOptimalFiniteSteeringNodeElement
    IAgVAProfileLambertProfile
    IAgVAProfileLambertSearchProfile
    IAgVAProfileGoldenSection
    IAgVAProfileGridSearch
    IAgVAStateCalcHeightAboveTerrain
    IAgVAStateCalcEpoch
    IAgVAStateCalcOrbitDelaunayG
    IAgVAStateCalcOrbitDelaunayH
    IAgVAStateCalcOrbitDelaunayL
    IAgVAStateCalcOrbitSemiLatusRectum
    IAgVAStateCalcJacobiConstant
    IAgVAStateCalcCartesianElem
    IAgVAStateCalcCartSTMElem
    IAgVAStateCalcSTMEigenval
    IAgVAStateCalcSTMEigenvecElem
    IAgVAStateCalcEnvironment
    IAgVAStateCalcEquinoctialElem
    IAgVAStateCalcDamageFlux
    IAgVAStateCalcDamageMassFlux
    IAgVAStateCalcMagFieldDipoleL
    IAgVAStateCalcSEETMagFieldFieldLineSepAngle
    IAgVAStateCalcImpactFlux
    IAgVAStateCalcImpactMassFlux
    IAgVAStateCalcSEETSAAFlux
    IAgVAStateCalcSEETVehTemp
    IAgVAStateCalcCloseApproachBearing
    IAgVAStateCalcCloseApproachMag
    IAgVAStateCalcCloseApproachTheta
    IAgVAStateCalcCloseApproachX
    IAgVAStateCalcCloseApproachY
    IAgVAStateCalcCloseApproachCosBearing
    IAgVAStateCalcRelGroundTrackError
    IAgVAStateCalcRelAtAOLMaster
    IAgVAStateCalcDeltaFromMaster
    IAgVAStateCalcLonDriftRate
    IAgVAStateCalcMeanEarthLon
    IAgVAStateCalcRectifiedLon
    IAgVAStateCalcGeodeticElem
    IAgVAStateCalcRepeatingGroundTrackErr
    IAgVAStateCalcAltOfApoapsis
    IAgVAStateCalcAltOfPeriapsis
    IAgVAStateCalcArgOfLat
    IAgVAStateCalcArgOfPeriapsis
    IAgVAStateCalcEccAnomaly
    IAgVAStateCalcEccentricity
    IAgVAStateCalcInclination
    IAgVAStateCalcLonOfAscNode
    IAgVAStateCalcMeanAnomaly
    IAgVAStateCalcMeanMotion
    IAgVAStateCalcOrbitPeriod
    IAgVAStateCalcNumRevs
    IAgVAStateCalcRAAN
    IAgVAStateCalcRadOfApoapsis
    IAgVAStateCalcRadOfPeriapsis
    IAgVAStateCalcSemiMajorAxis
    IAgVAStateCalcTimePastAscNode
    IAgVAStateCalcTimePastPeriapsis
    IAgVAStateCalcDeltaV
    IAgVAStateCalcDeltaVSquared
    IAgVAStateCalcMCSDeltaV
    IAgVAStateCalcMCSDeltaVSquared
    IAgVAStateCalcSequenceDeltaV
    IAgVAStateCalcSequenceDeltaVSquared
    IAgVAStateCalcFuelMass
    IAgVAStateCalcDensity
    IAgVAStateCalcInertialDeltaVMag
    IAgVAStateCalcInertialDeltaVx
    IAgVAStateCalcInertialDeltaVy
    IAgVAStateCalcInertialDeltaVz
    IAgVAStateCalcManeuverSpecificImpulse
    IAgVAStateCalcPressure
    IAgVAStateCalcTemperature
    IAgVAStateCalcVectorX
    IAgVAStateCalcVectorY
    IAgVAStateCalcVectorZ
    IAgVAStateCalcMass
    IAgVAStateCalcManeuverTotalMassFlowRate
    IAgVAStateCalcAbsoluteValue
    IAgVAStateCalcDifference
    IAgVAStateCalcDifferenceOtherSegment
    IAgVAStateCalcPosDifferenceOtherSegment
    IAgVAStateCalcVelDifferenceOtherSegment
    IAgVAStateCalcPosVelDifferenceOtherSegment
    IAgVAStateCalcValueAtSegment
    IAgVAStateCalcMaxValue
    IAgVAStateCalcMinValue
    IAgVAStateCalcMeanValue
    IAgVAStateCalcMedianValue
    IAgVAStateCalcStandardDeviation
    IAgVAStateCalcNegative
    IAgVAStateCalcTrueAnomaly
    IAgVABDotRCalc
    IAgVABDotTCalc
    IAgVABMagCalc
    IAgVABThetaCalc
    IAgVAStateCalcDeltaDec
    IAgVAStateCalcDeltaRA
    IAgVAStateCalcBetaAngle
    IAgVAStateCalcLocalApparentSolarLon
    IAgVAStateCalcLonOfPeriapsis
    IAgVAStateCalcOrbitStateValue
    IAgVAStateCalcSignedEccentricity
    IAgVAStateCalcTrueLon
    IAgVAStateCalcPower
    IAgVAStateCalcRelMotion
    IAgVAStateCalcSolarBetaAngle
    IAgVAStateCalcSolarInPlaneAngle
    IAgVAStateCalcRelPosDecAngle
    IAgVAStateCalcRelPosInPlaneAngle
    IAgVAStateCalcRelativeInclination
    IAgVAStateCalcCurvilinearRelMotion
    IAgVAStateCalcCustomFunction
    IAgVAStateCalcScript
    IAgVAStateCalcCd
    IAgVAStateCalcCr
    IAgVAStateCalcDragArea
    IAgVAStateCalcRadiationPressureArea
    IAgVAStateCalcRadiationPressureCoefficient
    IAgVAStateCalcSRPArea
    IAgVAStateCalcCosOfVerticalFPA
    IAgVAStateCalcDec
    IAgVAStateCalcFPA
    IAgVAStateCalcRMag
    IAgVAStateCalcRA
    IAgVAStateCalcVMag
    IAgVAStateCalcVelAz
    IAgVAStateCalcC3Energy
    IAgVAStateCalcInAsympDec
    IAgVAStateCalcInAsympRA
    IAgVAStateCalcInVelAzAtPeriapsis
    IAgVAStateCalcOutAsympDec
    IAgVAStateCalcOutAsympRA
    IAgVAStateCalcOutVelAzAtPeriapsis
    IAgVAStateCalcDuration
    IAgVAStateCalcUserValue
    IAgVAStateCalcCrdnAngle
    IAgVAStateCalcAngle
    IAgVAStateCalcDotProduct
    IAgVAStateCalcVectorDec
    IAgVAStateCalcVectorMag
    IAgVAStateCalcVectorRA
    IAgVAStateCalcOnePtAccess
    IAgVAStateCalcDifferenceAcrossSegmentsOtherSat
    IAgVAStateCalcValueAtSegmentOtherSat
    IAgVAStateCalcRARate
    IAgVAStateCalcDecRate
    IAgVAStateCalcGravitationalParameter
    IAgVAStateCalcReferenceRadius
    IAgVAStateCalcGravCoeff
    IAgVAStateCalcSpeedOfLight
    IAgVAStateCalcPi
    IAgVAStateCalcScalar
    IAgVAStateCalcApparentSolarTime
    IAgVAStateCalcEarthMeanSolarTime
    IAgVAStateCalcEarthMeanLocTimeAN
    IAgVACentralBodyCollection
    IAgVACbEphemeris
    IAgVACbGravityModel
    IAgVACbShape
    IAgVACbShapeSphere
    IAgVACbShapeOblateSpheroid
    IAgVACbShapeTriaxialEllipsoid
    IAgVACbAttitude
    IAgVACbAttitudeRotationCoefficientsFile
    IAgVACbAttitudeIAU1994
    IAgVACbEphemerisAnalyticOrbit
    IAgVACbEphemerisJPLSpice
    IAgVACbEphemerisFile
    IAgVACbEphemerisJPLDE
    IAgVACbEphemerisPlanetary
    IAgVACentralBody
    IAgVAPowerInternal
    IAgVAPowerProcessed
    IAgVAPowerSolarArray
    IAgVAGeneralRelativityFunction
    IAgVAStateTransFunction
    IAgVACR3BPFunc
    IAgVARadiationPressureFunction
    IAgVAYarkovskyFunc
    IAgVABlendedDensity
    IAgVADragModelPlugin
    IAgVACira72Function
    IAgVAExponential
    IAgVAHarrisPriester
    IAgVADensityModelPlugin
    IAgVAJacchiaRoberts
    IAgVAJacchiaBowman2008
    IAgVAJacchia_1960
    IAgVAJacchia_1970
    IAgVAJacchia_1971
    IAgVAMSISE_1990
    IAgVAMSIS_1986
    IAgVANRLMSISE_2000
    IAgVAUS_Standard_Atmosphere
    IAgVAMarsGRAM37
    IAgVAMarsGRAM2005
    IAgVAVenusGRAM2005
    IAgVAMarsGRAM2010
    IAgVAMarsGRAM2001
    IAgVAMarsGRAM2000
    IAgVADTM2012
    IAgVADTM2020
    IAgVAGravityFieldFunction
    IAgVAPointMassFunction
    IAgVATwoBodyFunction
    IAgVAHPOPPluginFunction
    IAgVAEOMFuncPluginFunction
    IAgVASRPAeroT20
    IAgVASRPAeroT30
    IAgVASRPGSPM04aIIA
    IAgVASRPGSPM04aIIR
    IAgVASRPGSPM04aeIIA
    IAgVASRPGSPM04aeIIR
    IAgVASRPSpherical
    IAgVASRPNPlate
    IAgVASRPTabAreaVec
    IAgVASRPVariableArea
    IAgVAThirdBodyFunction
    IAgVASRPReflectionPlugin
    IAgVAEngineModelThrustCoefficients
    IAgVAEngineModelIspCoefficients
    IAgVAEngineConstAcc
    IAgVAEngineConstant
    IAgVAEngineDefinition
    IAgVAEngineThrottleTable
    IAgVAEngineIon
    IAgVAEngineCustom
    IAgVAEnginePlugin
    IAgVAEngineModelPoly
    IAgVAThruster
    IAgVAThrusterSetCollection
    IAgVAThrusterSet
    IAgVAAsTriggerCondition
    IAgVACustomFunctionScriptEngine
    IAgVANumericalIntegrator
    IAgVAPropagatorFunctionCollection
    IAgVANumericalPropagatorWrapper
    IAgVANumericalPropagatorWrapperCR3BP
    IAgVABulirschStoerIntegrator
    IAgVAGaussJacksonIntegrator
    IAgVARK2nd3rd
    IAgVARK4th
    IAgVARK4th5th
    IAgVARK4thAdapt
    IAgVARKF7th8th
    IAgVARKV8th9th


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

    AgVADriverMCS
    AgVAMCSSegmentCollection
    AgVAMCSEnd
    AgVAMCSInitialState
    AgVASpacecraftParameters
    AgVAFuelTank
    AgVAElementCartesian
    AgVAElementKeplerian
    AgVAElementEquinoctial
    AgVAElementDelaunay
    AgVAElementMixedSpherical
    AgVAElementSpherical
    AgVAElementTargetVectorIncomingAsymptote
    AgVAElementTargetVectorOutgoingAsymptote
    AgVAElementGeodetic
    AgVAMCSPropagate
    AgVAState
    AgVAStoppingConditionCollection
    AgVAAccessStoppingCondition
    AgVALightingStoppingCondition
    AgVAStoppingCondition
    AgVAStoppingConditionElement
    AgVAMCSSequence
    AgVAMCSBackwardSequence
    AgVAMCSLaunch
    AgVADisplaySystemGeodetic
    AgVADisplaySystemGeocentric
    AgVABurnoutGeodetic
    AgVABurnoutCBFCartesian
    AgVABurnoutGeocentric
    AgVABurnoutLaunchAzAlt
    AgVABurnoutLaunchAzRadius
    AgVABurnoutVelocity
    AgVAMCSFollow
    AgVAMCSManeuver
    AgVAManeuverFinite
    AgVAManeuverImpulsive
    AgVAAttitudeControlImpulsiveVelocityVector
    AgVAAttitudeControlImpulsiveAntiVelocityVector
    AgVAAttitudeControlImpulsiveAttitude
    AgVAAttitudeControlImpulsiveFile
    AgVAAttitudeControlImpulsiveThrustVector
    AgVAAttitudeControlFiniteAntiVelocityVector
    AgVAAttitudeControlFiniteAttitude
    AgVAAttitudeControlFiniteFile
    AgVAAttitudeControlFiniteThrustVector
    AgVAAttitudeControlFiniteTimeVarying
    AgVAAttitudeControlFiniteVelocityVector
    AgVAAttitudeControlFinitePlugin
    AgVAAttitudeControlOptimalFiniteLagrange
    AgVAManeuverFinitePropagator
    AgVAMCSHold
    AgVAMCSUpdate
    AgVAMCSReturn
    AgVAMCSStop
    AgVAMCSTargetSequence
    AgVAProfileCollection
    AgVAMCSOptions
    AgVACalcObjectCollection
    AgVAConstraintCollection
    AgVAPluginProperties
    AgVAProfileSearchPlugin
    AgVATargeterGraph
    AgVATargeterGraphCollection
    AgVATargeterGraphResultCollection
    AgVATargeterGraphActiveControlCollection
    AgVATargeterGraphActiveControl
    AgVATargeterGraphResult
    AgVAProfileDifferentialCorrector
    AgVAProfileScriptingTool
    AgVADCControl
    AgVADCResult
    AgVADCControlCollection
    AgVADCResultCollection
    AgVASearchPluginControl
    AgVASearchPluginControlCollection
    AgVASearchPluginResult
    AgVASearchPluginResultCollection
    AgVAProfileChangeManeuverType
    AgVAProfileChangeReturnSegment
    AgVAProfileChangePropagator
    AgVAProfileChangeStopSegment
    AgVAProfileChangeStoppingConditionState
    AgVAProfileSeedFiniteManeuver
    AgVAProfileRunOnce
    AgVABPlaneCollection
    AgVAStateCalcDamageFlux
    AgVAStateCalcDamageMassFlux
    AgVAStateCalcMagFieldDipoleL
    AgVAStateCalcSEETMagFieldFieldLineSepAngle
    AgVAStateCalcImpactFlux
    AgVAStateCalcImpactMassFlux
    AgVAStateCalcSEETSAAFlux
    AgVAStateCalcSEETVehTemp
    AgVAStateCalcEpoch
    AgVAStateCalcJacobiConstant
    AgVAStateCalcCartesianElem
    AgVAStateCalcCartSTMElem
    AgVAStateCalcSTMEigenval
    AgVAStateCalcSTMEigenvecElem
    AgVAStateCalcEnvironment
    AgVAStateCalcOrbitDelaunayG
    AgVAStateCalcOrbitDelaunayH
    AgVAStateCalcOrbitDelaunayL
    AgVAStateCalcOrbitSemiLatusRectum
    AgVAStateCalcEquinoctialElem
    AgVAStateCalcCloseApproachBearing
    AgVAStateCalcCloseApproachMag
    AgVAStateCalcCloseApproachTheta
    AgVAStateCalcCloseApproachX
    AgVAStateCalcCloseApproachY
    AgVAStateCalcCloseApproachCosBearing
    AgVAStateCalcRelGroundTrackError
    AgVAStateCalcRelAtAOLMaster
    AgVAStateCalcDeltaFromMaster
    AgVAStateCalcLonDriftRate
    AgVAStateCalcMeanEarthLon
    AgVAStateCalcRectifiedLon
    AgVAStateCalcHeightAboveTerrain
    AgVAStateCalcGeodeticElem
    AgVAStateCalcRepeatingGroundTrackErr
    AgVAStateCalcAltOfApoapsis
    AgVAStateCalcAltOfPeriapsis
    AgVAStateCalcArgOfLat
    AgVAStateCalcArgOfPeriapsis
    AgVAStateCalcEccAnomaly
    AgVAStateCalcLonOfAscNode
    AgVAStateCalcMeanMotion
    AgVAStateCalcOrbitPeriod
    AgVAStateCalcNumRevs
    AgVAStateCalcRadOfApoapsis
    AgVAStateCalcRadOfPeriapsis
    AgVAStateCalcSemiMajorAxis
    AgVAStateCalcTimePastAscNode
    AgVAStateCalcTimePastPeriapsis
    AgVAStateCalcTrueAnomaly
    AgVAStateCalcDeltaV
    AgVAStateCalcDeltaVSquared
    AgVAStateCalcMCSDeltaV
    AgVAStateCalcMCSDeltaVSquared
    AgVAStateCalcSequenceDeltaV
    AgVAStateCalcSequenceDeltaVSquared
    AgVAStateCalcFuelMass
    AgVAStateCalcDensity
    AgVAStateCalcInertialDeltaVMag
    AgVAStateCalcInertialDeltaVx
    AgVAStateCalcInertialDeltaVy
    AgVAStateCalcInertialDeltaVz
    AgVAStateCalcManeuverSpecificImpulse
    AgVAStateCalcPressure
    AgVAStateCalcTemperature
    AgVAStateCalcVectorY
    AgVAStateCalcVectorZ
    AgVAStateCalcMass
    AgVAStateCalcManeuverTotalMassFlowRate
    AgVAStateCalcAbsoluteValue
    AgVAStateCalcDifference
    AgVAStateCalcDifferenceOtherSegment
    AgVAStateCalcPosDifferenceOtherSegment
    AgVAStateCalcVelDifferenceOtherSegment
    AgVAStateCalcPosVelDifferenceOtherSegment
    AgVAStateCalcValueAtSegment
    AgVAStateCalcMaxValue
    AgVAStateCalcMinValue
    AgVAStateCalcMeanValue
    AgVAStateCalcMedianValue
    AgVAStateCalcStandardDeviation
    AgVAStateCalcNegative
    AgVAStateCalcEccentricity
    AgVAStateCalcMeanAnomaly
    AgVAStateCalcRAAN
    AgVABDotRCalc
    AgVABDotTCalc
    AgVABMagCalc
    AgVABThetaCalc
    AgVAStateCalcDeltaDec
    AgVAStateCalcDeltaRA
    AgVAStateCalcBetaAngle
    AgVAStateCalcLocalApparentSolarLon
    AgVAStateCalcLonOfPeriapsis
    AgVAStateCalcOrbitStateValue
    AgVAStateCalcSignedEccentricity
    AgVAStateCalcInclination
    AgVAStateCalcTrueLon
    AgVAStateCalcPower
    AgVAStateCalcRelMotion
    AgVAStateCalcSolarBetaAngle
    AgVAStateCalcSolarInPlaneAngle
    AgVAStateCalcRelPosDecAngle
    AgVAStateCalcRelPosInPlaneAngle
    AgVAStateCalcRelativeInclination
    AgVAStateCalcCurvilinearRelMotion
    AgVAStateCalcCustomFunction
    AgVAStateCalcScript
    AgVAStateCalcCd
    AgVAStateCalcCr
    AgVAStateCalcDragArea
    AgVAStateCalcRadiationPressureArea
    AgVAStateCalcRadiationPressureCoefficient
    AgVAStateCalcSRPArea
    AgVAStateCalcCosOfVerticalFPA
    AgVAStateCalcDec
    AgVAStateCalcFPA
    AgVAStateCalcRMag
    AgVAStateCalcRA
    AgVAStateCalcVMag
    AgVAStateCalcVelAz
    AgVAStateCalcC3Energy
    AgVAStateCalcInAsympDec
    AgVAStateCalcInAsympRA
    AgVAStateCalcInVelAzAtPeriapsis
    AgVAStateCalcOutAsympDec
    AgVAStateCalcOutAsympRA
    AgVAStateCalcOutVelAzAtPeriapsis
    AgVAStateCalcDuration
    AgVAStateCalcUserValue
    AgVAStateCalcCrdnAngle
    AgVAStateCalcAngle
    AgVAStateCalcDotProduct
    AgVAStateCalcVectorDec
    AgVAStateCalcVectorMag
    AgVAStateCalcVectorRA
    AgVAStateCalcVectorX
    AgVAStateCalcOnePtAccess
    AgVAStateCalcDifferenceAcrossSegmentsOtherSat
    AgVAStateCalcValueAtSegmentOtherSat
    AgVAStateCalcRARate
    AgVAStateCalcDecRate
    AgVAStateCalcGravitationalParameter
    AgVAStateCalcReferenceRadius
    AgVAStateCalcGravCoeff
    AgVAStateCalcSpeedOfLight
    AgVAStateCalcPi
    AgVAStateCalcScalar
    AgVAStateCalcApparentSolarTime
    AgVAStateCalcEarthMeanSolarTime
    AgVAStateCalcEarthMeanLocTimeAN
    AgVAAutomaticSequenceCollection
    AgVAAutomaticSequence
    AgVACentralBodyCollection
    AgVACentralBody
    AgVACbGravityModel
    AgVACbShapeSphere
    AgVACbShapeOblateSpheroid
    AgVACbShapeTriaxialEllipsoid
    AgVACbAttitudeRotationCoefficientsFile
    AgVACbAttitudeIAU1994
    AgVACbEphemerisAnalyticOrbit
    AgVACbEphemerisJPLSpice
    AgVACbEphemerisFile
    AgVACbEphemerisJPLDE
    AgVACbEphemerisPlanetary
    AgVAMCSSegmentProperties
    AgVAPowerInternal
    AgVAPowerProcessed
    AgVAPowerSolarArray
    AgVAGeneralRelativityFunction
    AgVAStateTransFunction
    AgVACR3BPFunc
    AgVARadiationPressureFunction
    AgVAYarkovskyFunc
    AgVABlendedDensity
    AgVACira72Function
    AgVAExponential
    AgVAHarrisPriester
    AgVADensityModelPlugin
    AgVAJacchiaRoberts
    AgVAJacchiaBowman2008
    AgVAJacchia_1960
    AgVAJacchia_1970
    AgVAJacchia_1971
    AgVAMSISE_1990
    AgVAMSIS_1986
    AgVANRLMSISE_2000
    AgVAUS_Standard_Atmosphere
    AgVAMarsGRAM37
    AgVAMarsGRAM2000
    AgVAMarsGRAM2001
    AgVAMarsGRAM2005
    AgVAMarsGRAM2010
    AgVAVenusGRAM2005
    AgVADTM2012
    AgVADTM2020
    AgVAGravityFieldFunction
    AgVAPointMassFunction
    AgVATwoBodyFunction
    AgVAHPOPPluginFunction
    AgVAEOMFuncPluginFunction
    AgVASRPAeroT20
    AgVASRPAeroT30
    AgVASRPGSPM04aIIA
    AgVASRPGSPM04aIIR
    AgVASRPGSPM04aeIIA
    AgVASRPGSPM04aeIIR
    AgVASRPSpherical
    AgVASRPNPlate
    AgVASRPTabAreaVec
    AgVASRPVariableArea
    AgVAThirdBodyFunction
    AgVADragModelPlugin
    AgVASRPReflectionPlugin
    AgVAEngineConstAcc
    AgVAEngineConstant
    AgVAEngineIon
    AgVAEngineThrottleTable
    AgVAEngineCustom
    AgVAEnginePlugin
    AgVAEngineModelPoly
    AgVAEngineModelThrustCoefficients
    AgVAEngineModelIspCoefficients
    AgVAEngineDefinition
    AgVAThruster
    AgVAThrusterSetCollection
    AgVAThrusterSet
    AgVAAsTriggerCondition
    AgVACustomFunctionScriptEngine
    AgVANumericalPropagatorWrapper
    AgVANumericalPropagatorWrapperCR3BP
    AgVAPropagatorFunctionCollection
    AgVABulirschStoerIntegrator
    AgVAGaussJacksonIntegrator
    AgVARK2nd3rd
    AgVARK4th
    AgVARK4th5th
    AgVARK4thAdapt
    AgVARKF7th8th
    AgVARKV8th9th
    AgVAScriptingTool
    AgVAScriptingSegmentCollection
    AgVAScriptingSegment
    AgVAScriptingParameterCollection
    AgVAScriptingParameter
    AgVAScriptingCalcObject
    AgVAScriptingCalcObjectCollection
    AgVAUserVariableDefinition
    AgVAUserVariable
    AgVAUserVariableUpdate
    AgVAUserVariableDefinitionCollection
    AgVAUserVariableCollection
    AgVAUserVariableUpdateCollection
    AgVACalculationGraphCollection
    AgVAScriptingParameterEnumerationChoice
    AgVAScriptingParameterEnumerationChoiceCollection
    AgVAProfileSNOPTOptimizer
    AgVASNOPTControl
    AgVASNOPTResult
    AgVASNOPTControlCollection
    AgVASNOPTResultCollection
    AgVAProfileIPOPTOptimizer
    AgVAIPOPTControl
    AgVAIPOPTResult
    AgVAIPOPTControlCollection
    AgVAIPOPTResultCollection
    AgVAManeuverOptimalFinite
    AgVAManeuverOptimalFiniteSNOPTOptimizer
    AgVAManeuverOptimalFiniteInitialBoundaryConditions
    AgVAManeuverOptimalFiniteFinalBoundaryConditions
    AgVAManeuverOptimalFinitePathBoundaryConditions
    AgVAManeuverOptimalFiniteSteeringNodeElement
    AgVAManeuverOptimalFiniteSteeringNodeCollection
    AgVAManeuverOptimalFiniteBounds
    AgVAProfileLambertProfile
    AgVAProfileLambertSearchProfile
    AgVAProfileGoldenSection
    AgVAGoldenSectionControlCollection
    AgVAGoldenSectionControl
    AgVAGoldenSectionResultCollection
    AgVAGoldenSectionResult
    AgVAProfileGridSearch
    AgVAGridSearchControlCollection
    AgVAGridSearchControl
    AgVAGridSearchResultCollection
    AgVAGridSearchResult


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: IAgVAUserVariableDefinitionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAUserVariableCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAUserVariableUpdateCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACalculationGraphCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAConstraintCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAPluginProperties
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASNOPTControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASNOPTResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAIPOPTControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAIPOPTResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverOptimalFiniteSNOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverOptimalFiniteInitialBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverOptimalFiniteFinalBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverOptimalFinitePathBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverOptimalFiniteSteeringNodeCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverOptimalFiniteBounds
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGoldenSectionControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGoldenSectionControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGoldenSectionResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGoldenSectionResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGridSearchControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGridSearchControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGridSearchResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGridSearchResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStoppingConditionElement
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStoppingConditionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAState
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStoppingConditionComponent
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAutomaticSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAutomaticSequenceCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABPlaneCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACalcObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverFinitePropagator
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABurnoutVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlFinite
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlImpulsive
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlOptimalFinite
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADisplaySystem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABurnout
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingParameterEnumerationChoice
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingParameterEnumerationChoiceCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingParameter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingParameterCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingCalcObject
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingCalcObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAScriptingTool
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElement
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASpacecraftParameters
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAFuelTank
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSSegmentProperties
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSEnd
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSInitialState
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADriverMCS
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementKeplerian
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementDelaunay
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementEquinoctial
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementMixedSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementTargetVectorIncomingAsymptote
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementTargetVectorOutgoingAsymptote
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAElementGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVALightingStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAccessStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSPropagate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSBackwardSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADisplaySystemGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADisplaySystemGeocentric
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABurnoutCBFCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABurnoutGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABurnoutGeocentric
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABurnoutLaunchAzAlt
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABurnoutLaunchAzRadius
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverFinite
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverImpulsive
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlImpulsiveVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlImpulsiveAntiVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlImpulsiveAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlImpulsiveFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlImpulsiveThrustVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlFiniteAntiVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlFiniteAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlFiniteFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlFiniteThrustVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlFiniteTimeVarying
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlFiniteVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlFinitePlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAttitudeControlOptimalFiniteLagrange
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSHold
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSReturn
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSStop
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMCSTargetSequence
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADCControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADCResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASearchPluginControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASearchPluginResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASearchPluginResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASearchPluginControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADCControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADCResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVATargeterGraphActiveControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVATargeterGraphResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVATargeterGraphActiveControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVATargeterGraphResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVATargeterGraph
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVATargeterGraphCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileSearchPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileDifferentialCorrector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileChangeManeuverType
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileScriptingTool
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileChangeReturnSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileChangePropagator
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileChangeStopSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileChangeStoppingConditionState
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileSeedFiniteManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileRunOnce
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAUserVariableDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAUserVariable
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAUserVariableUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileSNOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASNOPTControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASNOPTResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileIPOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAIPOPTControl
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAIPOPTResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverOptimalFinite
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAManeuverOptimalFiniteSteeringNodeElement
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileLambertProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileLambertSearchProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileGoldenSection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAProfileGridSearch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcHeightAboveTerrain
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOrbitDelaunayG
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOrbitDelaunayH
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOrbitDelaunayL
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOrbitSemiLatusRectum
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcJacobiConstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCartesianElem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCartSTMElem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSTMEigenval
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSTMEigenvecElem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcEnvironment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcEquinoctialElem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDamageFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDamageMassFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMagFieldDipoleL
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSEETMagFieldFieldLineSepAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcImpactFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcImpactMassFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSEETSAAFlux
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSEETVehTemp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCloseApproachBearing
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCloseApproachMag
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCloseApproachTheta
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCloseApproachX
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCloseApproachY
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCloseApproachCosBearing
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRelGroundTrackError
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRelAtAOLMaster
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDeltaFromMaster
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcLonDriftRate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMeanEarthLon
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRectifiedLon
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcGeodeticElem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRepeatingGroundTrackErr
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcAltOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcAltOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcArgOfLat
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcArgOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcEccAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcInclination
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcLonOfAscNode
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMeanAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMeanMotion
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOrbitPeriod
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcNumRevs
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRAAN
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRadOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRadOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSemiMajorAxis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcTimePastAscNode
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcTimePastPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMCSDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMCSDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSequenceDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSequenceDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcFuelMass
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDensity
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcInertialDeltaVMag
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcInertialDeltaVx
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcInertialDeltaVy
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcInertialDeltaVz
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcManeuverSpecificImpulse
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcPressure
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcTemperature
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVectorX
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVectorY
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVectorZ
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMass
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcManeuverTotalMassFlowRate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcAbsoluteValue
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDifference
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcPosDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcPosVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcValueAtSegment
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMaxValue
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMinValue
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMeanValue
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcMedianValue
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcStandardDeviation
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcNegative
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcTrueAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABDotRCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABDotTCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABMagCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABThetaCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDeltaDec
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDeltaRA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcBetaAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcLocalApparentSolarLon
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcLonOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOrbitStateValue
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSignedEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcTrueLon
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcPower
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRelMotion
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSolarBetaAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSolarInPlaneAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRelPosDecAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRelPosInPlaneAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRelativeInclination
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCurvilinearRelMotion
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCustomFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcScript
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCd
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCr
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDragArea
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRadiationPressureArea
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRadiationPressureCoefficient
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSRPArea
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCosOfVerticalFPA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDec
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcFPA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRMag
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVMag
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVelAz
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcC3Energy
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcInAsympDec
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcInAsympRA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcInVelAzAtPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOutAsympDec
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOutAsympRA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOutVelAzAtPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDuration
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcUserValue
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcCrdnAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVectorDec
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVectorMag
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcVectorRA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcOnePtAccess
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDifferenceAcrossSegmentsOtherSat
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcValueAtSegmentOtherSat
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcRARate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcDecRate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcGravitationalParameter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcReferenceRadius
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcGravCoeff
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcSpeedOfLight
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcPi
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcApparentSolarTime
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcEarthMeanSolarTime
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateCalcEarthMeanLocTimeAN
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbEphemeris
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbGravityModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbShape
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbShapeSphere
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbShapeOblateSpheroid
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbShapeTriaxialEllipsoid
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbAttitudeRotationCoefficientsFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbAttitudeIAU1994
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbEphemerisAnalyticOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbEphemerisJPLSpice
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbEphemerisFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbEphemerisJPLDE
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACbEphemerisPlanetary
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAPowerInternal
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAPowerProcessed
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAPowerSolarArray
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGeneralRelativityFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAStateTransFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACR3BPFunc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVARadiationPressureFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAYarkovskyFunc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABlendedDensity
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADragModelPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACira72Function
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAExponential
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAHarrisPriester
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADensityModelPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAJacchiaRoberts
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAJacchiaBowman2008
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAJacchia_1960
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAJacchia_1970
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAJacchia_1971
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMSISE_1990
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMSIS_1986
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVANRLMSISE_2000
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAUS_Standard_Atmosphere
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMarsGRAM37
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMarsGRAM2005
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAVenusGRAM2005
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMarsGRAM2010
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMarsGRAM2001
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAMarsGRAM2000
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADTM2012
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVADTM2020
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGravityFieldFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAPointMassFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVATwoBodyFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAHPOPPluginFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEOMFuncPluginFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPAeroT20
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPAeroT30
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPGSPM04aIIA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPGSPM04aIIR
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPGSPM04aeIIA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPGSPM04aeIIR
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPNPlate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPTabAreaVec
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPVariableArea
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAThirdBodyFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVASRPReflectionPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineModelThrustCoefficients
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineModelIspCoefficients
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineConstAcc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineConstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineThrottleTable
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineIon
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineCustom
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEnginePlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAEngineModelPoly
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAThruster
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAThrusterSetCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAThrusterSet
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAAsTriggerCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVACustomFunctionScriptEngine
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVANumericalIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAPropagatorFunctionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVANumericalPropagatorWrapper
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVANumericalPropagatorWrapperCR3BP
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVABulirschStoerIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVAGaussJacksonIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVARK2nd3rd
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVARK4th
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVARK4th5th
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVARK4thAdapt
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVARKF7th8th
    :members:
    :exclude-members: __init__
.. autoclass:: IAgVARKV8th9th
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

.. autoclass:: AgVADriverMCS
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSEnd
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSInitialState
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASpacecraftParameters
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAFuelTank
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementKeplerian
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementEquinoctial
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementDelaunay
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementMixedSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementTargetVectorIncomingAsymptote
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementTargetVectorOutgoingAsymptote
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAElementGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSPropagate
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAState
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStoppingConditionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAccessStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AgVALightingStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStoppingCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStoppingConditionElement
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSSequence
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSBackwardSequence
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADisplaySystemGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADisplaySystemGeocentric
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABurnoutGeodetic
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABurnoutCBFCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABurnoutGeocentric
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABurnoutLaunchAzAlt
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABurnoutLaunchAzRadius
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABurnoutVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSFollow
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverFinite
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverImpulsive
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlImpulsiveVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlImpulsiveAntiVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlImpulsiveAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlImpulsiveFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlImpulsiveThrustVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlFiniteAntiVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlFiniteAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlFiniteFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlFiniteThrustVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlFiniteTimeVarying
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlFiniteVelocityVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlFinitePlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAttitudeControlOptimalFiniteLagrange
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverFinitePropagator
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSHold
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSReturn
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSStop
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSTargetSequence
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACalcObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAConstraintCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAPluginProperties
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileSearchPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgVATargeterGraph
    :members:
    :exclude-members: __init__
.. autoclass:: AgVATargeterGraphCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVATargeterGraphResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVATargeterGraphActiveControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVATargeterGraphActiveControl
    :members:
    :exclude-members: __init__
.. autoclass:: AgVATargeterGraphResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileDifferentialCorrector
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileScriptingTool
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADCControl
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADCResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADCControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADCResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASearchPluginControl
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASearchPluginControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASearchPluginResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASearchPluginResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileChangeManeuverType
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileChangeReturnSegment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileChangePropagator
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileChangeStopSegment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileChangeStoppingConditionState
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileSeedFiniteManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileRunOnce
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABPlaneCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDamageFlux
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDamageMassFlux
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMagFieldDipoleL
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSEETMagFieldFieldLineSepAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcImpactFlux
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcImpactMassFlux
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSEETSAAFlux
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSEETVehTemp
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcJacobiConstant
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCartesianElem
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCartSTMElem
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSTMEigenval
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSTMEigenvecElem
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcEnvironment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOrbitDelaunayG
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOrbitDelaunayH
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOrbitDelaunayL
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOrbitSemiLatusRectum
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcEquinoctialElem
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCloseApproachBearing
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCloseApproachMag
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCloseApproachTheta
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCloseApproachX
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCloseApproachY
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCloseApproachCosBearing
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRelGroundTrackError
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRelAtAOLMaster
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDeltaFromMaster
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcLonDriftRate
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMeanEarthLon
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRectifiedLon
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcHeightAboveTerrain
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcGeodeticElem
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRepeatingGroundTrackErr
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcAltOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcAltOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcArgOfLat
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcArgOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcEccAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcLonOfAscNode
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMeanMotion
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOrbitPeriod
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcNumRevs
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRadOfApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRadOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSemiMajorAxis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcTimePastAscNode
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcTimePastPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcTrueAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMCSDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMCSDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSequenceDeltaV
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSequenceDeltaVSquared
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcFuelMass
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDensity
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcInertialDeltaVMag
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcInertialDeltaVx
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcInertialDeltaVy
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcInertialDeltaVz
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcManeuverSpecificImpulse
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcPressure
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcTemperature
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVectorY
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVectorZ
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMass
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcManeuverTotalMassFlowRate
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcAbsoluteValue
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDifference
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcPosDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcPosVelDifferenceOtherSegment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcValueAtSegment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMaxValue
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMinValue
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMeanValue
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMedianValue
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcStandardDeviation
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcNegative
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcMeanAnomaly
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRAAN
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABDotRCalc
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABDotTCalc
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABMagCalc
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABThetaCalc
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDeltaDec
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDeltaRA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcBetaAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcLocalApparentSolarLon
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcLonOfPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOrbitStateValue
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSignedEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcInclination
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcTrueLon
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcPower
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRelMotion
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSolarBetaAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSolarInPlaneAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRelPosDecAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRelPosInPlaneAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRelativeInclination
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCurvilinearRelMotion
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCustomFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcScript
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCd
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCr
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDragArea
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRadiationPressureArea
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRadiationPressureCoefficient
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSRPArea
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCosOfVerticalFPA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDec
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcFPA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRMag
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVMag
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVelAz
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcC3Energy
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcInAsympDec
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcInAsympRA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcInVelAzAtPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOutAsympDec
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOutAsympRA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOutVelAzAtPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDuration
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcUserValue
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcCrdnAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVectorDec
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVectorMag
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVectorRA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcVectorX
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcOnePtAccess
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDifferenceAcrossSegmentsOtherSat
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcValueAtSegmentOtherSat
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcRARate
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcDecRate
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcGravitationalParameter
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcReferenceRadius
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcGravCoeff
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcSpeedOfLight
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcPi
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcApparentSolarTime
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcEarthMeanSolarTime
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateCalcEarthMeanLocTimeAN
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAutomaticSequenceCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAutomaticSequence
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbGravityModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbShapeSphere
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbShapeOblateSpheroid
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbShapeTriaxialEllipsoid
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbAttitudeRotationCoefficientsFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbAttitudeIAU1994
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbEphemerisAnalyticOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbEphemerisJPLSpice
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbEphemerisFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbEphemerisJPLDE
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACbEphemerisPlanetary
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMCSSegmentProperties
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAPowerInternal
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAPowerProcessed
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAPowerSolarArray
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGeneralRelativityFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAStateTransFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACR3BPFunc
    :members:
    :exclude-members: __init__
.. autoclass:: AgVARadiationPressureFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAYarkovskyFunc
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABlendedDensity
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACira72Function
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAExponential
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAHarrisPriester
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADensityModelPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAJacchiaRoberts
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAJacchiaBowman2008
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAJacchia_1960
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAJacchia_1970
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAJacchia_1971
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMSISE_1990
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMSIS_1986
    :members:
    :exclude-members: __init__
.. autoclass:: AgVANRLMSISE_2000
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAUS_Standard_Atmosphere
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMarsGRAM37
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMarsGRAM2000
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMarsGRAM2001
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMarsGRAM2005
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAMarsGRAM2010
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAVenusGRAM2005
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADTM2012
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADTM2020
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGravityFieldFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAPointMassFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVATwoBodyFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAHPOPPluginFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEOMFuncPluginFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPAeroT20
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPAeroT30
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPGSPM04aIIA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPGSPM04aIIR
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPGSPM04aeIIA
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPGSPM04aeIIR
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPNPlate
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPTabAreaVec
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPVariableArea
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAThirdBodyFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgVADragModelPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASRPReflectionPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineConstAcc
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineConstant
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineIon
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineThrottleTable
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineCustom
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEnginePlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineModelPoly
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineModelThrustCoefficients
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineModelIspCoefficients
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAEngineDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAThruster
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAThrusterSetCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAThrusterSet
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAAsTriggerCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACustomFunctionScriptEngine
    :members:
    :exclude-members: __init__
.. autoclass:: AgVANumericalPropagatorWrapper
    :members:
    :exclude-members: __init__
.. autoclass:: AgVANumericalPropagatorWrapperCR3BP
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAPropagatorFunctionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVABulirschStoerIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGaussJacksonIntegrator
    :members:
    :exclude-members: __init__
.. autoclass:: AgVARK2nd3rd
    :members:
    :exclude-members: __init__
.. autoclass:: AgVARK4th
    :members:
    :exclude-members: __init__
.. autoclass:: AgVARK4th5th
    :members:
    :exclude-members: __init__
.. autoclass:: AgVARK4thAdapt
    :members:
    :exclude-members: __init__
.. autoclass:: AgVARKF7th8th
    :members:
    :exclude-members: __init__
.. autoclass:: AgVARKV8th9th
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingTool
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingSegmentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingSegment
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingParameterCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingParameter
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingCalcObject
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingCalcObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAUserVariableDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAUserVariable
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAUserVariableUpdate
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAUserVariableDefinitionCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAUserVariableCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAUserVariableUpdateCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVACalculationGraphCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingParameterEnumerationChoice
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAScriptingParameterEnumerationChoiceCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileSNOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASNOPTControl
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASNOPTResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASNOPTControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVASNOPTResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileIPOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAIPOPTControl
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAIPOPTResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAIPOPTControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAIPOPTResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverOptimalFinite
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverOptimalFiniteSNOPTOptimizer
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverOptimalFiniteInitialBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverOptimalFiniteFinalBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverOptimalFinitePathBoundaryConditions
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverOptimalFiniteSteeringNodeElement
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverOptimalFiniteSteeringNodeCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAManeuverOptimalFiniteBounds
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileLambertProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileLambertSearchProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileGoldenSection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGoldenSectionControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGoldenSectionControl
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGoldenSectionResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGoldenSectionResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAProfileGridSearch
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGridSearchControlCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGridSearchControl
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGridSearchResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgVAGridSearchResult
    :members:
    :exclude-members: __init__

