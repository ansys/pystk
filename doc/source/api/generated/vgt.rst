Module Contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    IAgCrdnIntervalCollection
    IAgCrdnInterval
    IAgCrdnPoint
    IAgCrdnVector
    IAgCrdnSystem
    IAgCrdnAxes
    IAgCrdnAngle
    IAgCrdnPlane
    IAgCrdnContext
    IAgCrdn
    IAgCrdnEvaluateResult
    IAgCrdnEvaluateWithRateResult
    IAgCrdnEventIntervalResult
    IAgCrdnEventFindOccurrenceResult
    IAgCrdnFindTimesResult
    IAgCrdnIntervalsVectorResult
    IAgCrdnEventIntervalCollectionOccurredResult
    IAgCrdnIntervalListResult
    IAgCrdnIntervalVectorCollection
    IAgCrdnEventGroup
    IAgCrdnEventIntervalGroup
    IAgCrdnEventIntervalListGroup
    IAgCrdnEventArrayGroup
    IAgCrdnCalcScalarGroup
    IAgCrdnEventIntervalCollectionGroup
    IAgCrdnParameterSetGroup
    IAgCrdnConditionGroup
    IAgCrdnConditionSetGroup
    IAgCrdnConditionSetEvaluateResult
    IAgCrdnConditionSetEvaluateWithRateResult
    IAgCrdnVolumeGridGroup
    IAgCrdnVolumeGroup
    IAgCrdnVolumeCalcGroup
    IAgCrdnCalcScalar
    IAgCrdnCalcScalarAngle
    IAgCrdnCalcScalarConstant
    IAgCrdnCalcScalarCustom
    IAgCrdnCalcScalarDataElement
    IAgCrdnCalcScalarDerivative
    IAgCrdnCalcScalarDotProduct
    IAgCrdnCalcScalarElapsedTime
    IAgCrdnCalcScalarFactory
    IAgCrdnCalcScalarFile
    IAgCrdnCalcScalarFixedAtTimeInstant
    IAgCrdnCalcScalarFunction
    IAgCrdnCalcScalarFunction2Var
    IAgCrdnCalcScalarIntegral
    IAgCrdnCalcScalarPlugin
    IAgCrdnCalcScalarSurfaceDistanceBetweenPoints
    IAgCrdnCalcScalarVectorComponent
    IAgCrdnCalcScalarVectorMagnitude
    IAgCrdnCondition
    IAgCrdnConditionCombined
    IAgCrdnConditionFactory
    IAgCrdnConditionPointInVolume
    IAgCrdnConditionScalarBounds
    IAgCrdnConditionSet
    IAgCrdnConditionSetFactory
    IAgCrdnConditionSetScalarThresholds
    IAgCrdnConverge
    IAgCrdnConvergeBasic
    IAgCrdnDerivative
    IAgCrdnDerivativeBasic
    IAgCrdnEvent
    IAgCrdnEventArray
    IAgCrdnEventArrayConditionCrossings
    IAgCrdnEventArrayExtrema
    IAgCrdnEventArrayFactory
    IAgCrdnEventArrayFiltered
    IAgCrdnEventArrayFixedStep
    IAgCrdnEventArrayFixedTimes
    IAgCrdnEventArrayMerged
    IAgCrdnEventArraySignaled
    IAgCrdnEventArrayStartStopTimes
    IAgCrdnEventEpoch
    IAgCrdnEventExtremum
    IAgCrdnEventFactory
    IAgCrdnEventInterval
    IAgCrdnEventIntervalBetweenTimeInstants
    IAgCrdnEventIntervalCollection
    IAgCrdnEventIntervalCollectionCondition
    IAgCrdnEventIntervalCollectionFactory
    IAgCrdnEventIntervalCollectionLighting
    IAgCrdnEventIntervalCollectionSignaled
    IAgCrdnEventIntervalFactory
    IAgCrdnEventIntervalFixed
    IAgCrdnEventIntervalFixedDuration
    IAgCrdnEventIntervalFromIntervalList
    IAgCrdnEventIntervalList
    IAgCrdnEventIntervalListCondition
    IAgCrdnEventIntervalListFactory
    IAgCrdnEventIntervalListFile
    IAgCrdnEventIntervalListFiltered
    IAgCrdnEventIntervalListFixed
    IAgCrdnEventIntervalListMerged
    IAgCrdnEventIntervalListScaled
    IAgCrdnEventIntervalListSignaled
    IAgCrdnEventIntervalListTimeOffset
    IAgCrdnEventIntervalScaled
    IAgCrdnEventIntervalSignaled
    IAgCrdnEventIntervalSmartInterval
    IAgCrdnEventIntervalTimeOffset
    IAgCrdnEventSignaled
    IAgCrdnEventSmartEpoch
    IAgCrdnEventStartStopTime
    IAgCrdnEventTimeOffset
    IAgCrdnFirstIntervalsFilter
    IAgCrdnGapsFilter
    IAgCrdnIntegral
    IAgCrdnIntegralBasic
    IAgCrdnInterp
    IAgCrdnInterpBasic
    IAgCrdnIntervalsFilter
    IAgCrdnLastIntervalsFilter
    IAgCrdnParameterSet
    IAgCrdnParameterSetAttitude
    IAgCrdnParameterSetFactory
    IAgCrdnParameterSetGroundTrajectory
    IAgCrdnParameterSetOrbit
    IAgCrdnParameterSetTrajectory
    IAgCrdnParameterSetVector
    IAgCrdnPruneFilter
    IAgCrdnPruneFilterFactory
    IAgCrdnRelativeSatisfactionConditionFilter
    IAgCrdnSampling
    IAgCrdnSamplingBasic
    IAgCrdnSamplingCurvatureTolerance
    IAgCrdnSamplingFixedStep
    IAgCrdnSamplingMethod
    IAgCrdnSamplingMethodFactory
    IAgCrdnSamplingRelativeTolerance
    IAgCrdnSatisfactionConditionFilter
    IAgCrdnSignalDelay
    IAgCrdnSignalDelayBasic
    IAgCrdnVolumeCalcFactory
    IAgCrdnVolumeFactory
    IAgCrdnVolumeGridFactory
    IAgCrdnGridCoordinateDefinition
    IAgCrdnGridValuesCustom
    IAgCrdnGridValuesFixedNumberOfSteps
    IAgCrdnGridValuesFixedStep
    IAgCrdnGridValuesMethod
    IAgCrdnLightTimeDelay
    IAgCrdnVolume
    IAgCrdnVolumeCalc
    IAgCrdnVolumeCalcAltitude
    IAgCrdnVolumeCalcAngleOffVector
    IAgCrdnVolumeCalcConditionSatMetric
    IAgCrdnVolumeCalcDelayRange
    IAgCrdnVolumeCalcFile
    IAgCrdnVolumeCalcFromScalar
    IAgCrdnVolumeCalcRange
    IAgCrdnVolumeCalcSolarIntensity
    IAgCrdnVolumeCombined
    IAgCrdnVolumeFromCalc
    IAgCrdnVolumeFromCondition
    IAgCrdnVolumeFromGrid
    IAgCrdnVolumeFromTimeSatisfaction
    IAgCrdnVolumeGrid
    IAgCrdnVolumeGridBearingAlt
    IAgCrdnVolumeGridCartesian
    IAgCrdnVolumeGridConstrained
    IAgCrdnVolumeGridCylindrical
    IAgCrdnVolumeGridLatLonAlt
    IAgCrdnVolumeGridResult
    IAgCrdnVolumeGridSpherical
    IAgCrdnVolumeInview
    IAgCrdnVolumeLighting
    IAgCrdnVolumeOverTime
    IAgCrdnTimeProperties
    IAgCrdnTypeInfo
    IAgCrdnRefTo
    IAgCrdnTemplate
    IAgCrdnInstance
    IAgCrdnPointRefTo
    IAgCrdnVectorRefTo
    IAgCrdnAxesRefTo
    IAgCrdnAngleRefTo
    IAgCrdnSystemRefTo
    IAgCrdnPlaneRefTo
    IAgCrdnAxesLabels
    IAgCrdnPlaneLabels
    IAgCrdnAxesAlignedAndConstrained
    IAgCrdnAxesAngularOffset
    IAgCrdnAxesFixedAtEpoch
    IAgCrdnAxesBPlane
    IAgCrdnAxesCustomScript
    IAgCrdnAxesAttitudeFile
    IAgCrdnAxesFixed
    IAgCrdnAxesModelAttach
    IAgCrdnAxesSpinning
    IAgCrdnAxesOnSurface
    IAgCrdnAxesTrajectory
    IAgCrdnAxesLagrangeLibration
    IAgCrdnAxesCommonTasks
    IAgCrdnAxesAtTimeInstant
    IAgCrdnAxesPlugin
    IAgCrdnAngleBetweenVectors
    IAgCrdnAngleBetweenPlanes
    IAgCrdnAngleDihedral
    IAgCrdnAngleRotation
    IAgCrdnAngleToPlane
    IAgCrdnPlaneNormal
    IAgCrdnPlaneQuadrant
    IAgCrdnPlaneTrajectory
    IAgCrdnPlaneTriad
    IAgCrdnPlaneTwoVector
    IAgCrdnPointBPlane
    IAgCrdnPointFile
    IAgCrdnPointFixedInSystem
    IAgCrdnPointGrazing
    IAgCrdnPointGlint
    IAgCrdnPointCovarianceGrazing
    IAgCrdnPointPlaneIntersection
    IAgCrdnPointOnSurface
    IAgCrdnPointModelAttach
    IAgCrdnPointSatelliteCollectionEntry
    IAgCrdnPointPlaneProjection
    IAgCrdnPointLagrangeLibration
    IAgCrdnPointCommonTasks
    IAgCrdnPointCentBodyIntersect
    IAgCrdnPointAtTimeInstant
    IAgCrdnPointPlugin
    IAgCrdnPointCBFixedOffset
    IAgCrdnSystemAssembled
    IAgCrdnSystemOnSurface
    IAgCrdnLLAPosition
    IAgCrdnSystemCommonTasks
    IAgCrdnVectorAngleRate
    IAgCrdnVectorApoapsis
    IAgCrdnVectorFixedAtEpoch
    IAgCrdnVectorAngularVelocity
    IAgCrdnVectorConing
    IAgCrdnVectorCross
    IAgCrdnVectorCustomScript
    IAgCrdnVectorDerivative
    IAgCrdnVectorDisplacement
    IAgCrdnVectorTwoPlanesIntersection
    IAgCrdnVectorModelAttach
    IAgCrdnVectorProjection
    IAgCrdnVectorScaled
    IAgCrdnVectorEccentricity
    IAgCrdnVectorFixedInAxes
    IAgCrdnVectorLineOfNodes
    IAgCrdnVectorOrbitAngularMomentum
    IAgCrdnVectorOrbitNormal
    IAgCrdnVectorPeriapsis
    IAgCrdnVectorReflection
    IAgCrdnVectorRotationVector
    IAgCrdnVectorDirectionToStar
    IAgCrdnVectorFixedAtTimeInstant
    IAgCrdnVectorLinearCombination
    IAgCrdnVectorProjectAlongVector
    IAgCrdnVectorScalarLinearCombination
    IAgCrdnVectorScalarScaled
    IAgCrdnVectorVelocityAcceleration
    IAgCrdnVectorPlugin
    IAgCrdnVectorDispSurface
    IAgCrdnVectorFactory
    IAgCrdnAxesFactory
    IAgCrdnSystemFactory
    IAgCrdnPointFactory
    IAgCrdnPlaneFactory
    IAgCrdnAngleFactory
    IAgCrdnVectorGroup
    IAgCrdnPointGroup
    IAgCrdnAngleGroup
    IAgCrdnAxesGroup
    IAgCrdnPlaneGroup
    IAgCrdnSystemGroup
    IAgCrdnProvider
    IAgCrdnRoot
    IAgCrdnWellKnownEarthSystems
    IAgCrdnWellKnownEarthAxes
    IAgCrdnWellKnownSunSystems
    IAgCrdnWellKnownSunAxes
    IAgCrdnWellKnownSystems
    IAgCrdnWellKnownAxes
    IAgCrdnAngleFindAngleResult
    IAgCrdnAngleFindAngleWithRateResult
    IAgCrdnAngleFindWithRateResult
    IAgCrdnAngleFindResult
    IAgCrdnAxesTransformResult
    IAgCrdnAxesTransformWithRateResult
    IAgCrdnPlaneFindInAxesResult
    IAgCrdnPlaneFindInAxesWithRateResult
    IAgCrdnPlaneFindInSystemResult
    IAgCrdnPlaneFindInSystemWithRateResult
    IAgCrdnAxesFindInAxesResult
    IAgCrdnAxesFindInAxesWithRateResult
    IAgCrdnPointLocateInSystemResult
    IAgCrdnPointLocateInSystemWithRateResult
    IAgCrdnSystemTransformResult
    IAgCrdnSystemTransformWithRateResult
    IAgCrdnSystemFindInSystemResult
    IAgCrdnVectorFindInAxesResult
    IAgCrdnVectorFindInAxesWithRateResult
    IAgCrdnMethodCallResult
    IAgCrdnCentralBody
    IAgCrdnCentralBodyRefTo
    IAgCrdnCentralBodyCollection
    IAgCrdnCollection
    IAgCrdnPointSamplingResult
    IAgCrdnPointSamplingInterval
    IAgCrdnPointSamplingIntervalCollection
    IAgCrdnAxesSamplingResult
    IAgCrdnAxesSamplingInterval
    IAgCrdnAxesSamplingIntervalCollection


Enumerations
~~~~~~~~~~~~

.. autosummary::

    AgECrdnCalcScalarType
    AgECrdnConditionCombinedOperationType
    AgECrdnConditionSetType
    AgECrdnConditionThresholdOption
    AgECrdnConditionType
    AgECrdnDimensionInheritance
    AgECrdnEventArrayFilterType
    AgECrdnEventArrayType
    AgECrdnEventIntervalCollectionType
    AgECrdnEventIntervalListType
    AgECrdnEventIntervalType
    AgECrdnEventListMergeOperation
    AgECrdnEventType
    AgECrdnExtremumConstants
    AgECrdnFileInterpolatorType
    AgECrdnIntegralType
    AgECrdnIntegrationWindowType
    AgECrdnInterpolatorType
    AgECrdnIntervalDurationKind
    AgECrdnIntervalSelection
    AgECrdnParameterSetType
    AgECrdnPruneFilter
    AgECrdnSampledReferenceTime
    AgECrdnSamplingMethod
    AgECrdnSatisfactionCrossing
    AgECrdnSaveDataOption
    AgECrdnSignalPathReferenceSystem
    AgECrdnSmartEpochState
    AgECrdnSmartIntervalState
    AgECrdnSpeedOptions
    AgECrdnStartStopOption
    AgECrdnThreshConvergeSense
    AgECrdnVectorComponentType
    AgECrdnVolumeCalcAltitudeReferenceType
    AgECrdnVolumeCalcAngleOffVectorType
    AgECrdnVolumeCalcRangeDistanceType
    AgECrdnVolumeCalcRangeSpeedType
    AgECrdnVolumeCalcType
    AgECrdnVolumeCalcVolumeSatisfactionAccumulationType
    AgECrdnVolumeCalcVolumeSatisfactionDurationType
    AgECrdnVolumeCalcVolumeSatisfactionFilterType
    AgECrdnVolumeCalcVolumeSatisfactionMetricType
    AgECrdnVolumeGridType
    AgECrdnVolumeResultVectorRequest
    AgECrdnVolumeType
    AgECrdnVolumeAberrationType
    AgECrdnVolumeClockHostType
    AgECrdnVolumeCombinedOperationType
    AgECrdnVolumeFromGridEdgeType
    AgECrdnVolumeLightingConditionsType
    AgECrdnVolumeOverTimeDurationType
    AgECrdnVolumeTimeSenseType
    AgECrdnVolumetricGridValuesMethodType
    AgECrdnKind
    AgECrdnAngleType
    AgECrdnAxesType
    AgECrdnPlaneType
    AgECrdnPointType
    AgECrdnSystemType
    AgECrdnVectorType
    AgECrdnMeanElementTheory
    AgECrdnDirectionType
    AgECrdnLagrangeLibrationPointType
    AgECrdnQuadrantType
    AgECrdnTrajectoryAxesType
    AgECrdnDisplayAxisSelector
    AgECrdnSignedAngleType
    AgECrdnPointBPlaneType
    AgECrdnReferenceShapeType
    AgECrdnSurfaceType
    AgECrdnSweepMode
    AgECrdnSignalSense
    AgECrdnIntersectionSurface
    AgECrdnVectorScaledDimensionInheritance


Classes
~~~~~~~

.. autosummary::

    AgCrdnEvaluateResult
    AgCrdnEvaluateWithRateResult
    AgCrdnEventIntervalResult
    AgCrdnEventFindOccurrenceResult
    AgCrdnFindTimesResult
    AgCrdnIntervalsVectorResult
    AgCrdnEventIntervalCollectionOccurredResult
    AgCrdnIntervalListResult
    AgCrdnIntervalVectorCollection
    AgCrdnEventGroup
    AgCrdnEventIntervalGroup
    AgCrdnEventIntervalListGroup
    AgCrdnEventArrayGroup
    AgCrdnCalcScalarGroup
    AgCrdnEventIntervalCollectionGroup
    AgCrdnParameterSetGroup
    AgCrdnConditionGroup
    AgCrdnConditionSetGroup
    AgCrdnConditionSetEvaluateResult
    AgCrdnConditionSetEvaluateWithRateResult
    AgCrdnVolumeGridGroup
    AgCrdnVolumeGroup
    AgCrdnVolumeCalcGroup
    AgCrdnCalcScalar
    AgCrdnCalcScalarAngle
    AgCrdnCalcScalarConstant
    AgCrdnCalcScalarCustom
    AgCrdnCalcScalarDataElement
    AgCrdnCalcScalarDerivative
    AgCrdnCalcScalarDotProduct
    AgCrdnCalcScalarElapsedTime
    AgCrdnCalcScalarFactory
    AgCrdnCalcScalarFile
    AgCrdnCalcScalarFixedAtTimeInstant
    AgCrdnCalcScalarFunction
    AgCrdnCalcScalarFunction2Var
    AgCrdnCalcScalarIntegral
    AgCrdnCalcScalarPlugin
    AgCrdnCalcScalarSurfaceDistanceBetweenPoints
    AgCrdnCalcScalarVectorComponent
    AgCrdnCalcScalarVectorMagnitude
    AgCrdnCondition
    AgCrdnConditionCombined
    AgCrdnConditionFactory
    AgCrdnConditionPointInVolume
    AgCrdnConditionScalarBounds
    AgCrdnConditionSet
    AgCrdnConditionSetFactory
    AgCrdnConditionSetScalarThresholds
    AgCrdnConverge
    AgCrdnConvergeBasic
    AgCrdnDerivative
    AgCrdnDerivativeBasic
    AgCrdnEvent
    AgCrdnEventArray
    AgCrdnEventArrayConditionCrossings
    AgCrdnEventArrayExtrema
    AgCrdnEventArrayFactory
    AgCrdnEventArrayFiltered
    AgCrdnEventArrayFixedStep
    AgCrdnEventArrayFixedTimes
    AgCrdnEventArrayMerged
    AgCrdnEventArraySignaled
    AgCrdnEventArrayStartStopTimes
    AgCrdnEventEpoch
    AgCrdnEventExtremum
    AgCrdnEventFactory
    AgCrdnEventInterval
    AgCrdnEventIntervalBetweenTimeInstants
    AgCrdnEventIntervalCollection
    AgCrdnEventIntervalCollectionCondition
    AgCrdnEventIntervalCollectionFactory
    AgCrdnEventIntervalCollectionLighting
    AgCrdnEventIntervalCollectionSignaled
    AgCrdnEventIntervalFactory
    AgCrdnEventIntervalFixed
    AgCrdnEventIntervalFixedDuration
    AgCrdnEventIntervalFromIntervalList
    AgCrdnEventIntervalList
    AgCrdnEventIntervalListCondition
    AgCrdnEventIntervalListFactory
    AgCrdnEventIntervalListFile
    AgCrdnEventIntervalListFiltered
    AgCrdnEventIntervalListFixed
    AgCrdnEventIntervalListMerged
    AgCrdnEventIntervalListScaled
    AgCrdnEventIntervalListSignaled
    AgCrdnEventIntervalListTimeOffset
    AgCrdnEventIntervalScaled
    AgCrdnEventIntervalSignaled
    AgCrdnEventIntervalSmartInterval
    AgCrdnEventIntervalTimeOffset
    AgCrdnEventSignaled
    AgCrdnEventSmartEpoch
    AgCrdnEventStartStopTime
    AgCrdnEventTimeOffset
    AgCrdnFirstIntervalsFilter
    AgCrdnGapsFilter
    AgCrdnIntegral
    AgCrdnIntegralBasic
    AgCrdnInterp
    AgCrdnInterpBasic
    AgCrdnIntervalsFilter
    AgCrdnLastIntervalsFilter
    AgCrdnParameterSet
    AgCrdnParameterSetAttitude
    AgCrdnParameterSetFactory
    AgCrdnParameterSetGroundTrajectory
    AgCrdnParameterSetOrbit
    AgCrdnParameterSetTrajectory
    AgCrdnParameterSetVector
    AgCrdnPruneFilter
    AgCrdnPruneFilterFactory
    AgCrdnRelativeSatisfactionConditionFilter
    AgCrdnSampling
    AgCrdnSamplingBasic
    AgCrdnSamplingCurvatureTolerance
    AgCrdnSamplingFixedStep
    AgCrdnSamplingMethod
    AgCrdnSamplingMethodFactory
    AgCrdnSamplingRelativeTolerance
    AgCrdnSatisfactionConditionFilter
    AgCrdnSignalDelay
    AgCrdnSignalDelayBasic
    AgCrdnVolumeCalcFactory
    AgCrdnVolumeFactory
    AgCrdnVolumeGridFactory
    AgCrdnGridCoordinateDefinition
    AgCrdnGridValuesCustom
    AgCrdnGridValuesFixedNumberOfSteps
    AgCrdnGridValuesFixedStep
    AgCrdnGridValuesMethod
    AgCrdnLightTimeDelay
    AgCrdnVolume
    AgCrdnVolumeCalc
    AgCrdnVolumeCalcAltitude
    AgCrdnVolumeCalcAngleOffVector
    AgCrdnVolumeCalcConditionSatMetric
    AgCrdnVolumeCalcDelayRange
    AgCrdnVolumeCalcFile
    AgCrdnVolumeCalcFromScalar
    AgCrdnVolumeCalcRange
    AgCrdnVolumeCalcSolarIntensity
    AgCrdnVolumeCombined
    AgCrdnVolumeFromCalc
    AgCrdnVolumeFromCondition
    AgCrdnVolumeFromGrid
    AgCrdnVolumeFromTimeSatisfaction
    AgCrdnVolumeGrid
    AgCrdnVolumeGridBearingAlt
    AgCrdnVolumeGridCartesian
    AgCrdnVolumeGridConstrained
    AgCrdnVolumeGridCylindrical
    AgCrdnVolumeGridLatLonAlt
    AgCrdnVolumeGridResult
    AgCrdnVolumeGridSpherical
    AgCrdnVolumeInview
    AgCrdnVolumeLighting
    AgCrdnVolumeOverTime
    AgCrdnGeneric
    AgCrdnTypeInfo
    AgCrdnInstance
    AgCrdnTemplate
    AgCrdnPointRefTo
    AgCrdnVectorRefTo
    AgCrdnAxesRefTo
    AgCrdnAngleRefTo
    AgCrdnSystemRefTo
    AgCrdnPlaneRefTo
    AgCrdnVector
    AgCrdnAxesLabels
    AgCrdnAxes
    AgCrdnPoint
    AgCrdnSystem
    AgCrdnAngle
    AgCrdnPlaneLabels
    AgCrdnPlane
    AgCrdnAxesAlignedAndConstrained
    AgCrdnAxesAngularOffset
    AgCrdnAxesFixedAtEpoch
    AgCrdnAxesBPlane
    AgCrdnAxesCustomScript
    AgCrdnAxesAttitudeFile
    AgCrdnAxesFixed
    AgCrdnAxesModelAttach
    AgCrdnAxesSpinning
    AgCrdnAxesOnSurface
    AgCrdnAxesTrajectory
    AgCrdnAxesLagrangeLibration
    AgCrdnAxesCommonTasks
    AgCrdnAxesAtTimeInstant
    AgCrdnAxesPlugin
    AgCrdnAngleBetweenVectors
    AgCrdnAngleBetweenPlanes
    AgCrdnAngleDihedral
    AgCrdnAngleRotation
    AgCrdnAngleToPlane
    AgCrdnPlaneNormal
    AgCrdnPlaneQuadrant
    AgCrdnPlaneTrajectory
    AgCrdnPlaneTriad
    AgCrdnPlaneTwoVector
    AgCrdnPointBPlane
    AgCrdnPointFile
    AgCrdnPointFixedInSystem
    AgCrdnPointGrazing
    AgCrdnPointGlint
    AgCrdnPointCovarianceGrazing
    AgCrdnPointPlaneIntersection
    AgCrdnPointOnSurface
    AgCrdnPointModelAttach
    AgCrdnPointSatelliteCollectionEntry
    AgCrdnPointPlaneProjection
    AgCrdnPointLagrangeLibration
    AgCrdnPointCommonTasks
    AgCrdnPointCentBodyIntersect
    AgCrdnPointAtTimeInstant
    AgCrdnPointPlugin
    AgCrdnPointCBFixedOffset
    AgCrdnSystemAssembled
    AgCrdnSystemOnSurface
    AgCrdnLLAPosition
    AgCrdnSystemCommonTasks
    AgCrdnVectorAngleRate
    AgCrdnVectorApoapsis
    AgCrdnVectorFixedAtEpoch
    AgCrdnVectorAngularVelocity
    AgCrdnVectorConing
    AgCrdnVectorCross
    AgCrdnVectorCustomScript
    AgCrdnVectorDerivative
    AgCrdnVectorDisplacement
    AgCrdnVectorTwoPlanesIntersection
    AgCrdnVectorModelAttach
    AgCrdnVectorProjection
    AgCrdnVectorScaled
    AgCrdnVectorEccentricity
    AgCrdnVectorFixedInAxes
    AgCrdnVectorLineOfNodes
    AgCrdnVectorOrbitAngularMomentum
    AgCrdnVectorOrbitNormal
    AgCrdnVectorPeriapsis
    AgCrdnVectorReflection
    AgCrdnVectorRotationVector
    AgCrdnVectorDirectionToStar
    AgCrdnVectorFixedAtTimeInstant
    AgCrdnVectorLinearCombination
    AgCrdnVectorProjectAlongVector
    AgCrdnVectorScalarLinearCombination
    AgCrdnVectorScalarScaled
    AgCrdnVectorVelocityAcceleration
    AgCrdnVectorPlugin
    AgCrdnVectorDispSurface
    AgCrdnVectorFactory
    AgCrdnAxesFactory
    AgCrdnSystemFactory
    AgCrdnPointFactory
    AgCrdnPlaneFactory
    AgCrdnAngleFactory
    AgCrdnVectorGroup
    AgCrdnPointGroup
    AgCrdnAngleGroup
    AgCrdnAxesGroup
    AgCrdnPlaneGroup
    AgCrdnSystemGroup
    AgCrdnProvider
    AgCrdnRoot
    AgCrdnWellKnownEarthSystems
    AgCrdnWellKnownEarthAxes
    AgCrdnWellKnownSunSystems
    AgCrdnWellKnownSunAxes
    AgCrdnWellKnownSystems
    AgCrdnWellKnownAxes
    AgCrdnMethodCallResult
    AgCrdnInterval
    AgCrdnIntervalCollection
    AgCrdnCentralBody
    AgCrdnCentralBodyRefTo
    AgCrdnCentralBodyCollection
    AgCrdnCollection
    AgCrdnPointSamplingResult
    AgCrdnPointSamplingInterval
    AgCrdnPointSamplingIntervalCollection
    AgCrdnAxesSamplingResult
    AgCrdnAxesSamplingInterval
    AgCrdnAxesSamplingIntervalCollection


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: IAgCrdnIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnContext
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdn
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventFindOccurrenceResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnFindTimesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnIntervalsVectorResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalCollectionOccurredResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnIntervalListResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnIntervalVectorCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalCollectionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnParameterSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionSetEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionSetEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarConstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarCustom
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarDataElement
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarElapsedTime
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarFunction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarFunction2Var
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarSurfaceDistanceBetweenPoints
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarVectorComponent
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCalcScalarVectorMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionCombined
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionPointInVolume
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionScalarBounds
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionSet
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConditionSetScalarThresholds
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConverge
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnConvergeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnDerivativeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEvent
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArray
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayConditionCrossings
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayExtrema
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayFixedTimes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayMerged
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArraySignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventArrayStartStopTimes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventExtremum
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalBetweenTimeInstants
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalCollectionCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalCollectionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalCollectionLighting
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalCollectionSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalFixed
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalFixedDuration
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalFromIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListFixed
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListMerged
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListScaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalListTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalScaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalSmartInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventIntervalTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventSmartEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventStartStopTime
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnEventTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnFirstIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnGapsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnIntegralBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnInterp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnInterpBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnLastIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnParameterSet
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnParameterSetAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnParameterSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnParameterSetGroundTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnParameterSetOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnParameterSetTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnParameterSetVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPruneFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPruneFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnRelativeSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSampling
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSamplingBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSamplingCurvatureTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSamplingFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSamplingMethod
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSamplingMethodFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSamplingRelativeTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSignalDelay
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSignalDelayBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnGridCoordinateDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnGridValuesCustom
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnGridValuesFixedNumberOfSteps
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnGridValuesFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnGridValuesMethod
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnLightTimeDelay
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolume
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcAngleOffVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcConditionSatMetric
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcDelayRange
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcFromScalar
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcRange
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCalcSolarIntensity
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeCombined
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeFromCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeFromCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeFromGrid
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeFromTimeSatisfaction
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGrid
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridBearingAlt
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridCylindrical
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridLatLonAlt
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeGridSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeInview
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeLighting
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVolumeOverTime
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnTimeProperties
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnTypeInfo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnTemplate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnInstance
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesLabels
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneLabels
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesAlignedAndConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesAngularOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesAttitudeFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesFixed
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesSpinning
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleBetweenVectors
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleBetweenPlanes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleDihedral
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleRotation
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleToPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneNormal
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneQuadrant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneTriad
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneTwoVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointFixedInSystem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointGlint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointCovarianceGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointPlaneIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointSatelliteCollectionEntry
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointPlaneProjection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointCentBodyIntersect
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointCBFixedOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemAssembled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnLLAPosition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorAngleRate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorAngularVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorConing
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorCross
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorDisplacement
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorTwoPlanesIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorProjection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorScaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorFixedInAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorLineOfNodes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorOrbitAngularMomentum
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorOrbitNormal
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorReflection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorRotationVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorDirectionToStar
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorProjectAlongVector
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorScalarLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorScalarScaled
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorVelocityAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorDispSurface
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnProvider
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnRoot
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnWellKnownEarthSystems
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnWellKnownEarthAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnWellKnownSunSystems
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnWellKnownSunAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnWellKnownSystems
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnWellKnownAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleFindAngleResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleFindAngleWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleFindWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAngleFindResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesTransformResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesTransformWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneFindInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPlaneFindInSystemWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointLocateInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointLocateInSystemWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemTransformResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemTransformWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnSystemFindInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnVectorFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnMethodCallResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCentralBodyRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnPointSamplingIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IAgCrdnAxesSamplingIntervalCollection
    :members:
    :exclude-members: __init__


Enumerations
~~~~~~~~~~~~

.. autoenum:: AgECrdnCalcScalarType
    :members:
.. autoenum:: AgECrdnConditionCombinedOperationType
    :members:
.. autoenum:: AgECrdnConditionSetType
    :members:
.. autoenum:: AgECrdnConditionThresholdOption
    :members:
.. autoenum:: AgECrdnConditionType
    :members:
.. autoenum:: AgECrdnDimensionInheritance
    :members:
.. autoenum:: AgECrdnEventArrayFilterType
    :members:
.. autoenum:: AgECrdnEventArrayType
    :members:
.. autoenum:: AgECrdnEventIntervalCollectionType
    :members:
.. autoenum:: AgECrdnEventIntervalListType
    :members:
.. autoenum:: AgECrdnEventIntervalType
    :members:
.. autoenum:: AgECrdnEventListMergeOperation
    :members:
.. autoenum:: AgECrdnEventType
    :members:
.. autoenum:: AgECrdnExtremumConstants
    :members:
.. autoenum:: AgECrdnFileInterpolatorType
    :members:
.. autoenum:: AgECrdnIntegralType
    :members:
.. autoenum:: AgECrdnIntegrationWindowType
    :members:
.. autoenum:: AgECrdnInterpolatorType
    :members:
.. autoenum:: AgECrdnIntervalDurationKind
    :members:
.. autoenum:: AgECrdnIntervalSelection
    :members:
.. autoenum:: AgECrdnParameterSetType
    :members:
.. autoenum:: AgECrdnPruneFilter
    :members:
.. autoenum:: AgECrdnSampledReferenceTime
    :members:
.. autoenum:: AgECrdnSamplingMethod
    :members:
.. autoenum:: AgECrdnSatisfactionCrossing
    :members:
.. autoenum:: AgECrdnSaveDataOption
    :members:
.. autoenum:: AgECrdnSignalPathReferenceSystem
    :members:
.. autoenum:: AgECrdnSmartEpochState
    :members:
.. autoenum:: AgECrdnSmartIntervalState
    :members:
.. autoenum:: AgECrdnSpeedOptions
    :members:
.. autoenum:: AgECrdnStartStopOption
    :members:
.. autoenum:: AgECrdnThreshConvergeSense
    :members:
.. autoenum:: AgECrdnVectorComponentType
    :members:
.. autoenum:: AgECrdnVolumeCalcAltitudeReferenceType
    :members:
.. autoenum:: AgECrdnVolumeCalcAngleOffVectorType
    :members:
.. autoenum:: AgECrdnVolumeCalcRangeDistanceType
    :members:
.. autoenum:: AgECrdnVolumeCalcRangeSpeedType
    :members:
.. autoenum:: AgECrdnVolumeCalcType
    :members:
.. autoenum:: AgECrdnVolumeCalcVolumeSatisfactionAccumulationType
    :members:
.. autoenum:: AgECrdnVolumeCalcVolumeSatisfactionDurationType
    :members:
.. autoenum:: AgECrdnVolumeCalcVolumeSatisfactionFilterType
    :members:
.. autoenum:: AgECrdnVolumeCalcVolumeSatisfactionMetricType
    :members:
.. autoenum:: AgECrdnVolumeGridType
    :members:
.. autoenum:: AgECrdnVolumeResultVectorRequest
    :members:
.. autoenum:: AgECrdnVolumeType
    :members:
.. autoenum:: AgECrdnVolumeAberrationType
    :members:
.. autoenum:: AgECrdnVolumeClockHostType
    :members:
.. autoenum:: AgECrdnVolumeCombinedOperationType
    :members:
.. autoenum:: AgECrdnVolumeFromGridEdgeType
    :members:
.. autoenum:: AgECrdnVolumeLightingConditionsType
    :members:
.. autoenum:: AgECrdnVolumeOverTimeDurationType
    :members:
.. autoenum:: AgECrdnVolumeTimeSenseType
    :members:
.. autoenum:: AgECrdnVolumetricGridValuesMethodType
    :members:
.. autoenum:: AgECrdnKind
    :members:
.. autoenum:: AgECrdnAngleType
    :members:
.. autoenum:: AgECrdnAxesType
    :members:
.. autoenum:: AgECrdnPlaneType
    :members:
.. autoenum:: AgECrdnPointType
    :members:
.. autoenum:: AgECrdnSystemType
    :members:
.. autoenum:: AgECrdnVectorType
    :members:
.. autoenum:: AgECrdnMeanElementTheory
    :members:
.. autoenum:: AgECrdnDirectionType
    :members:
.. autoenum:: AgECrdnLagrangeLibrationPointType
    :members:
.. autoenum:: AgECrdnQuadrantType
    :members:
.. autoenum:: AgECrdnTrajectoryAxesType
    :members:
.. autoenum:: AgECrdnDisplayAxisSelector
    :members:
.. autoenum:: AgECrdnSignedAngleType
    :members:
.. autoenum:: AgECrdnPointBPlaneType
    :members:
.. autoenum:: AgECrdnReferenceShapeType
    :members:
.. autoenum:: AgECrdnSurfaceType
    :members:
.. autoenum:: AgECrdnSweepMode
    :members:
.. autoenum:: AgECrdnSignalSense
    :members:
.. autoenum:: AgECrdnIntersectionSurface
    :members:
.. autoenum:: AgECrdnVectorScaledDimensionInheritance
    :members:


Classes
~~~~~~~

.. autoclass:: AgCrdnEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventFindOccurrenceResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnFindTimesResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnIntervalsVectorResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalCollectionOccurredResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnIntervalListResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnIntervalVectorCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalCollectionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnParameterSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionSetEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionSetEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarConstant
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarCustom
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarDataElement
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarElapsedTime
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarFunction
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarFunction2Var
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarSurfaceDistanceBetweenPoints
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarVectorComponent
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCalcScalarVectorMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionCombined
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionPointInVolume
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionScalarBounds
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionSet
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConditionSetScalarThresholds
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConverge
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnConvergeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnDerivativeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEvent
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArray
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayConditionCrossings
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayExtrema
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayFixedTimes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayMerged
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArraySignaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventArrayStartStopTimes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventExtremum
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventInterval
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalBetweenTimeInstants
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalCollectionCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalCollectionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalCollectionLighting
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalCollectionSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalFixed
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalFixedDuration
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalFromIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListFixed
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListMerged
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListScaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalListTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalScaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalSmartInterval
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventIntervalTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventSmartEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventStartStopTime
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnEventTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnFirstIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnGapsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnIntegralBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnInterp
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnInterpBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnLastIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnParameterSet
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnParameterSetAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnParameterSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnParameterSetGroundTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnParameterSetOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnParameterSetTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnParameterSetVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPruneFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPruneFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnRelativeSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSampling
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSamplingBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSamplingCurvatureTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSamplingFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSamplingMethod
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSamplingMethodFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSamplingRelativeTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSignalDelay
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSignalDelayBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnGridCoordinateDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnGridValuesCustom
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnGridValuesFixedNumberOfSteps
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnGridValuesFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnGridValuesMethod
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnLightTimeDelay
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolume
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalc
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcAngleOffVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcConditionSatMetric
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcDelayRange
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcFromScalar
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcRange
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCalcSolarIntensity
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeCombined
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeFromCalc
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeFromCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeFromGrid
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeFromTimeSatisfaction
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGrid
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridBearingAlt
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridCylindrical
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridLatLonAlt
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeGridSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeInview
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeLighting
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVolumeOverTime
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnGeneric
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnTypeInfo
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnInstance
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnTemplate
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngleRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSystemRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesLabels
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSystem
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngle
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneLabels
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlane
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesAlignedAndConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesAngularOffset
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesAttitudeFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesFixed
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesSpinning
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngleBetweenVectors
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngleBetweenPlanes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngleDihedral
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngleRotation
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngleToPlane
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneNormal
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneQuadrant
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneTriad
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneTwoVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointFile
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointFixedInSystem
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointGlint
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointCovarianceGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointPlaneIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointSatelliteCollectionEntry
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointPlaneProjection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointCentBodyIntersect
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointCBFixedOffset
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSystemAssembled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSystemOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnLLAPosition
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSystemCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorAngleRate
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorAngularVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorConing
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorCross
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorDisplacement
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorTwoPlanesIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorProjection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorScaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorFixedInAxes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorLineOfNodes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorOrbitAngularMomentum
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorOrbitNormal
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorReflection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorRotationVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorDirectionToStar
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorProjectAlongVector
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorScalarLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorScalarScaled
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorVelocityAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorDispSurface
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSystemFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngleFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnVectorGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAngleGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPlaneGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnSystemGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnProvider
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnRoot
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnWellKnownEarthSystems
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnWellKnownEarthAxes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnWellKnownSunSystems
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnWellKnownSunAxes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnWellKnownSystems
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnWellKnownAxes
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnMethodCallResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnInterval
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCentralBodyRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnPointSamplingIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: AgCrdnAxesSamplingIntervalCollection
    :members:
    :exclude-members: __init__

