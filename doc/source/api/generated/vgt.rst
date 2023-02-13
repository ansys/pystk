Module contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    ICrdnIntervalCollection
    ICrdnInterval
    ICrdnPoint
    ICrdnVector
    ICrdnSystem
    ICrdnAxes
    ICrdnAngle
    ICrdnPlane
    ICrdnContext
    ICrdn
    ICrdnEvaluateResult
    ICrdnEvaluateWithRateResult
    ICrdnEventIntervalResult
    ICrdnEventFindOccurrenceResult
    ICrdnFindTimesResult
    ICrdnIntervalsVectorResult
    ICrdnEventIntervalCollectionOccurredResult
    ICrdnIntervalListResult
    ICrdnIntervalVectorCollection
    ICrdnEventGroup
    ICrdnEventIntervalGroup
    ICrdnEventIntervalListGroup
    ICrdnEventArrayGroup
    ICrdnCalcScalarGroup
    ICrdnEventIntervalCollectionGroup
    ICrdnParameterSetGroup
    ICrdnConditionGroup
    ICrdnConditionSetGroup
    ICrdnConditionSetEvaluateResult
    ICrdnConditionSetEvaluateWithRateResult
    ICrdnVolumeGridGroup
    ICrdnVolumeGroup
    ICrdnVolumeCalcGroup
    ICrdnCalcScalar
    ICrdnCalcScalarAngle
    ICrdnCalcScalarConstant
    ICrdnCalcScalarCustom
    ICrdnCalcScalarDataElement
    ICrdnCalcScalarDerivative
    ICrdnCalcScalarDotProduct
    ICrdnCalcScalarElapsedTime
    ICrdnCalcScalarFactory
    ICrdnCalcScalarFile
    ICrdnCalcScalarFixedAtTimeInstant
    ICrdnCalcScalarFunction
    ICrdnCalcScalarFunction2Var
    ICrdnCalcScalarIntegral
    ICrdnCalcScalarPlugin
    ICrdnCalcScalarSurfaceDistanceBetweenPoints
    ICrdnCalcScalarVectorComponent
    ICrdnCalcScalarVectorMagnitude
    ICrdnCondition
    ICrdnConditionCombined
    ICrdnConditionFactory
    ICrdnConditionPointInVolume
    ICrdnConditionScalarBounds
    ICrdnConditionSet
    ICrdnConditionSetFactory
    ICrdnConditionSetScalarThresholds
    ICrdnConverge
    ICrdnConvergeBasic
    ICrdnDerivative
    ICrdnDerivativeBasic
    ICrdnEvent
    ICrdnEventArray
    ICrdnEventArrayConditionCrossings
    ICrdnEventArrayExtrema
    ICrdnEventArrayFactory
    ICrdnEventArrayFiltered
    ICrdnEventArrayFixedStep
    ICrdnEventArrayFixedTimes
    ICrdnEventArrayMerged
    ICrdnEventArraySignaled
    ICrdnEventArrayStartStopTimes
    ICrdnEventEpoch
    ICrdnEventExtremum
    ICrdnEventFactory
    ICrdnEventInterval
    ICrdnEventIntervalBetweenTimeInstants
    ICrdnEventIntervalCollection
    ICrdnEventIntervalCollectionCondition
    ICrdnEventIntervalCollectionFactory
    ICrdnEventIntervalCollectionLighting
    ICrdnEventIntervalCollectionSignaled
    ICrdnEventIntervalFactory
    ICrdnEventIntervalFixed
    ICrdnEventIntervalFixedDuration
    ICrdnEventIntervalFromIntervalList
    ICrdnEventIntervalList
    ICrdnEventIntervalListCondition
    ICrdnEventIntervalListFactory
    ICrdnEventIntervalListFile
    ICrdnEventIntervalListFiltered
    ICrdnEventIntervalListFixed
    ICrdnEventIntervalListMerged
    ICrdnEventIntervalListScaled
    ICrdnEventIntervalListSignaled
    ICrdnEventIntervalListTimeOffset
    ICrdnEventIntervalScaled
    ICrdnEventIntervalSignaled
    ICrdnEventIntervalSmartInterval
    ICrdnEventIntervalTimeOffset
    ICrdnEventSignaled
    ICrdnEventSmartEpoch
    ICrdnEventStartStopTime
    ICrdnEventTimeOffset
    ICrdnFirstIntervalsFilter
    ICrdnGapsFilter
    ICrdnIntegral
    ICrdnIntegralBasic
    ICrdnInterp
    ICrdnInterpBasic
    ICrdnIntervalsFilter
    ICrdnLastIntervalsFilter
    ICrdnParameterSet
    ICrdnParameterSetAttitude
    ICrdnParameterSetFactory
    ICrdnParameterSetGroundTrajectory
    ICrdnParameterSetOrbit
    ICrdnParameterSetTrajectory
    ICrdnParameterSetVector
    ICrdnPruneFilter
    ICrdnPruneFilterFactory
    ICrdnRelativeSatisfactionConditionFilter
    ICrdnSampling
    ICrdnSamplingBasic
    ICrdnSamplingCurvatureTolerance
    ICrdnSamplingFixedStep
    ICrdnSamplingMethod
    ICrdnSamplingMethodFactory
    ICrdnSamplingRelativeTolerance
    ICrdnSatisfactionConditionFilter
    ICrdnSignalDelay
    ICrdnSignalDelayBasic
    ICrdnVolumeCalcFactory
    ICrdnVolumeFactory
    ICrdnVolumeGridFactory
    ICrdnGridCoordinateDefinition
    ICrdnGridValuesCustom
    ICrdnGridValuesFixedNumberOfSteps
    ICrdnGridValuesFixedStep
    ICrdnGridValuesMethod
    ICrdnLightTimeDelay
    ICrdnVolume
    ICrdnVolumeCalc
    ICrdnVolumeCalcAltitude
    ICrdnVolumeCalcAngleOffVector
    ICrdnVolumeCalcConditionSatMetric
    ICrdnVolumeCalcDelayRange
    ICrdnVolumeCalcFile
    ICrdnVolumeCalcFromScalar
    ICrdnVolumeCalcRange
    ICrdnVolumeCalcSolarIntensity
    ICrdnVolumeCombined
    ICrdnVolumeFromCalc
    ICrdnVolumeFromCondition
    ICrdnVolumeFromGrid
    ICrdnVolumeFromTimeSatisfaction
    ICrdnVolumeGrid
    ICrdnVolumeGridBearingAlt
    ICrdnVolumeGridCartesian
    ICrdnVolumeGridConstrained
    ICrdnVolumeGridCylindrical
    ICrdnVolumeGridLatLonAlt
    ICrdnVolumeGridResult
    ICrdnVolumeGridSpherical
    ICrdnVolumeInview
    ICrdnVolumeLighting
    ICrdnVolumeOverTime
    ICrdnTimeProperties
    ICrdnTypeInfo
    ICrdnRefTo
    ICrdnTemplate
    ICrdnInstance
    ICrdnPointRefTo
    ICrdnVectorRefTo
    ICrdnAxesRefTo
    ICrdnAngleRefTo
    ICrdnSystemRefTo
    ICrdnPlaneRefTo
    ICrdnAxesLabels
    ICrdnPlaneLabels
    ICrdnAxesAlignedAndConstrained
    ICrdnAxesAngularOffset
    ICrdnAxesFixedAtEpoch
    ICrdnAxesBPlane
    ICrdnAxesCustomScript
    ICrdnAxesAttitudeFile
    ICrdnAxesFixed
    ICrdnAxesModelAttach
    ICrdnAxesSpinning
    ICrdnAxesOnSurface
    ICrdnAxesTrajectory
    ICrdnAxesLagrangeLibration
    ICrdnAxesCommonTasks
    ICrdnAxesAtTimeInstant
    ICrdnAxesPlugin
    ICrdnAngleBetweenVectors
    ICrdnAngleBetweenPlanes
    ICrdnAngleDihedral
    ICrdnAngleRotation
    ICrdnAngleToPlane
    ICrdnPlaneNormal
    ICrdnPlaneQuadrant
    ICrdnPlaneTrajectory
    ICrdnPlaneTriad
    ICrdnPlaneTwoVector
    ICrdnPointBPlane
    ICrdnPointFile
    ICrdnPointFixedInSystem
    ICrdnPointGrazing
    ICrdnPointGlint
    ICrdnPointCovarianceGrazing
    ICrdnPointPlaneIntersection
    ICrdnPointOnSurface
    ICrdnPointModelAttach
    ICrdnPointSatelliteCollectionEntry
    ICrdnPointPlaneProjection
    ICrdnPointLagrangeLibration
    ICrdnPointCommonTasks
    ICrdnPointCentBodyIntersect
    ICrdnPointAtTimeInstant
    ICrdnPointPlugin
    ICrdnPointCBFixedOffset
    ICrdnSystemAssembled
    ICrdnSystemOnSurface
    ICrdnLLAPosition
    ICrdnSystemCommonTasks
    ICrdnVectorAngleRate
    ICrdnVectorApoapsis
    ICrdnVectorFixedAtEpoch
    ICrdnVectorAngularVelocity
    ICrdnVectorConing
    ICrdnVectorCross
    ICrdnVectorCustomScript
    ICrdnVectorDerivative
    ICrdnVectorDisplacement
    ICrdnVectorTwoPlanesIntersection
    ICrdnVectorModelAttach
    ICrdnVectorProjection
    ICrdnVectorScaled
    ICrdnVectorEccentricity
    ICrdnVectorFixedInAxes
    ICrdnVectorLineOfNodes
    ICrdnVectorOrbitAngularMomentum
    ICrdnVectorOrbitNormal
    ICrdnVectorPeriapsis
    ICrdnVectorReflection
    ICrdnVectorRotationVector
    ICrdnVectorDirectionToStar
    ICrdnVectorFixedAtTimeInstant
    ICrdnVectorLinearCombination
    ICrdnVectorProjectAlongVector
    ICrdnVectorScalarLinearCombination
    ICrdnVectorScalarScaled
    ICrdnVectorVelocityAcceleration
    ICrdnVectorPlugin
    ICrdnVectorDispSurface
    ICrdnVectorFactory
    ICrdnAxesFactory
    ICrdnSystemFactory
    ICrdnPointFactory
    ICrdnPlaneFactory
    ICrdnAngleFactory
    ICrdnVectorGroup
    ICrdnPointGroup
    ICrdnAngleGroup
    ICrdnAxesGroup
    ICrdnPlaneGroup
    ICrdnSystemGroup
    ICrdnProvider
    ICrdnRoot
    ICrdnWellKnownEarthSystems
    ICrdnWellKnownEarthAxes
    ICrdnWellKnownSunSystems
    ICrdnWellKnownSunAxes
    ICrdnWellKnownSystems
    ICrdnWellKnownAxes
    ICrdnAngleFindAngleResult
    ICrdnAngleFindAngleWithRateResult
    ICrdnAngleFindWithRateResult
    ICrdnAngleFindResult
    ICrdnAxesTransformResult
    ICrdnAxesTransformWithRateResult
    ICrdnPlaneFindInAxesResult
    ICrdnPlaneFindInAxesWithRateResult
    ICrdnPlaneFindInSystemResult
    ICrdnPlaneFindInSystemWithRateResult
    ICrdnAxesFindInAxesResult
    ICrdnAxesFindInAxesWithRateResult
    ICrdnPointLocateInSystemResult
    ICrdnPointLocateInSystemWithRateResult
    ICrdnSystemTransformResult
    ICrdnSystemTransformWithRateResult
    ICrdnSystemFindInSystemResult
    ICrdnVectorFindInAxesResult
    ICrdnVectorFindInAxesWithRateResult
    ICrdnMethodCallResult
    ICrdnCentralBody
    ICrdnCentralBodyRefTo
    ICrdnCentralBodyCollection
    ICrdnCollection
    ICrdnPointSamplingResult
    ICrdnPointSamplingInterval
    ICrdnPointSamplingIntervalCollection
    ICrdnAxesSamplingResult
    ICrdnAxesSamplingInterval
    ICrdnAxesSamplingIntervalCollection


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

    CrdnEvaluateResult
    CrdnEvaluateWithRateResult
    CrdnEventIntervalResult
    CrdnEventFindOccurrenceResult
    CrdnFindTimesResult
    CrdnIntervalsVectorResult
    CrdnEventIntervalCollectionOccurredResult
    CrdnIntervalListResult
    CrdnIntervalVectorCollection
    CrdnEventGroup
    CrdnEventIntervalGroup
    CrdnEventIntervalListGroup
    CrdnEventArrayGroup
    CrdnCalcScalarGroup
    CrdnEventIntervalCollectionGroup
    CrdnParameterSetGroup
    CrdnConditionGroup
    CrdnConditionSetGroup
    CrdnConditionSetEvaluateResult
    CrdnConditionSetEvaluateWithRateResult
    CrdnVolumeGridGroup
    CrdnVolumeGroup
    CrdnVolumeCalcGroup
    CrdnCalcScalar
    CrdnCalcScalarAngle
    CrdnCalcScalarConstant
    CrdnCalcScalarCustom
    CrdnCalcScalarDataElement
    CrdnCalcScalarDerivative
    CrdnCalcScalarDotProduct
    CrdnCalcScalarElapsedTime
    CrdnCalcScalarFactory
    CrdnCalcScalarFile
    CrdnCalcScalarFixedAtTimeInstant
    CrdnCalcScalarFunction
    CrdnCalcScalarFunction2Var
    CrdnCalcScalarIntegral
    CrdnCalcScalarPlugin
    CrdnCalcScalarSurfaceDistanceBetweenPoints
    CrdnCalcScalarVectorComponent
    CrdnCalcScalarVectorMagnitude
    CrdnCondition
    CrdnConditionCombined
    CrdnConditionFactory
    CrdnConditionPointInVolume
    CrdnConditionScalarBounds
    CrdnConditionSet
    CrdnConditionSetFactory
    CrdnConditionSetScalarThresholds
    CrdnConverge
    CrdnConvergeBasic
    CrdnDerivative
    CrdnDerivativeBasic
    CrdnEvent
    CrdnEventArray
    CrdnEventArrayConditionCrossings
    CrdnEventArrayExtrema
    CrdnEventArrayFactory
    CrdnEventArrayFiltered
    CrdnEventArrayFixedStep
    CrdnEventArrayFixedTimes
    CrdnEventArrayMerged
    CrdnEventArraySignaled
    CrdnEventArrayStartStopTimes
    CrdnEventEpoch
    CrdnEventExtremum
    CrdnEventFactory
    CrdnEventInterval
    CrdnEventIntervalBetweenTimeInstants
    CrdnEventIntervalCollection
    CrdnEventIntervalCollectionCondition
    CrdnEventIntervalCollectionFactory
    CrdnEventIntervalCollectionLighting
    CrdnEventIntervalCollectionSignaled
    CrdnEventIntervalFactory
    CrdnEventIntervalFixed
    CrdnEventIntervalFixedDuration
    CrdnEventIntervalFromIntervalList
    CrdnEventIntervalList
    CrdnEventIntervalListCondition
    CrdnEventIntervalListFactory
    CrdnEventIntervalListFile
    CrdnEventIntervalListFiltered
    CrdnEventIntervalListFixed
    CrdnEventIntervalListMerged
    CrdnEventIntervalListScaled
    CrdnEventIntervalListSignaled
    CrdnEventIntervalListTimeOffset
    CrdnEventIntervalScaled
    CrdnEventIntervalSignaled
    CrdnEventIntervalSmartInterval
    CrdnEventIntervalTimeOffset
    CrdnEventSignaled
    CrdnEventSmartEpoch
    CrdnEventStartStopTime
    CrdnEventTimeOffset
    CrdnFirstIntervalsFilter
    CrdnGapsFilter
    CrdnIntegral
    CrdnIntegralBasic
    CrdnInterp
    CrdnInterpBasic
    CrdnIntervalsFilter
    CrdnLastIntervalsFilter
    CrdnParameterSet
    CrdnParameterSetAttitude
    CrdnParameterSetFactory
    CrdnParameterSetGroundTrajectory
    CrdnParameterSetOrbit
    CrdnParameterSetTrajectory
    CrdnParameterSetVector
    CrdnPruneFilter
    CrdnPruneFilterFactory
    CrdnRelativeSatisfactionConditionFilter
    CrdnSampling
    CrdnSamplingBasic
    CrdnSamplingCurvatureTolerance
    CrdnSamplingFixedStep
    CrdnSamplingMethod
    CrdnSamplingMethodFactory
    CrdnSamplingRelativeTolerance
    CrdnSatisfactionConditionFilter
    CrdnSignalDelay
    CrdnSignalDelayBasic
    CrdnVolumeCalcFactory
    CrdnVolumeFactory
    CrdnVolumeGridFactory
    CrdnGridCoordinateDefinition
    CrdnGridValuesCustom
    CrdnGridValuesFixedNumberOfSteps
    CrdnGridValuesFixedStep
    CrdnGridValuesMethod
    CrdnLightTimeDelay
    CrdnVolume
    CrdnVolumeCalc
    CrdnVolumeCalcAltitude
    CrdnVolumeCalcAngleOffVector
    CrdnVolumeCalcConditionSatMetric
    CrdnVolumeCalcDelayRange
    CrdnVolumeCalcFile
    CrdnVolumeCalcFromScalar
    CrdnVolumeCalcRange
    CrdnVolumeCalcSolarIntensity
    CrdnVolumeCombined
    CrdnVolumeFromCalc
    CrdnVolumeFromCondition
    CrdnVolumeFromGrid
    CrdnVolumeFromTimeSatisfaction
    CrdnVolumeGrid
    CrdnVolumeGridBearingAlt
    CrdnVolumeGridCartesian
    CrdnVolumeGridConstrained
    CrdnVolumeGridCylindrical
    CrdnVolumeGridLatLonAlt
    CrdnVolumeGridResult
    CrdnVolumeGridSpherical
    CrdnVolumeInview
    CrdnVolumeLighting
    CrdnVolumeOverTime
    CrdnGeneric
    CrdnTypeInfo
    CrdnInstance
    CrdnTemplate
    CrdnPointRefTo
    CrdnVectorRefTo
    CrdnAxesRefTo
    CrdnAngleRefTo
    CrdnSystemRefTo
    CrdnPlaneRefTo
    CrdnVector
    CrdnAxesLabels
    CrdnAxes
    CrdnPoint
    CrdnSystem
    CrdnAngle
    CrdnPlaneLabels
    CrdnPlane
    CrdnAxesAlignedAndConstrained
    CrdnAxesAngularOffset
    CrdnAxesFixedAtEpoch
    CrdnAxesBPlane
    CrdnAxesCustomScript
    CrdnAxesAttitudeFile
    CrdnAxesFixed
    CrdnAxesModelAttach
    CrdnAxesSpinning
    CrdnAxesOnSurface
    CrdnAxesTrajectory
    CrdnAxesLagrangeLibration
    CrdnAxesCommonTasks
    CrdnAxesAtTimeInstant
    CrdnAxesPlugin
    CrdnAngleBetweenVectors
    CrdnAngleBetweenPlanes
    CrdnAngleDihedral
    CrdnAngleRotation
    CrdnAngleToPlane
    CrdnPlaneNormal
    CrdnPlaneQuadrant
    CrdnPlaneTrajectory
    CrdnPlaneTriad
    CrdnPlaneTwoVector
    CrdnPointBPlane
    CrdnPointFile
    CrdnPointFixedInSystem
    CrdnPointGrazing
    CrdnPointGlint
    CrdnPointCovarianceGrazing
    CrdnPointPlaneIntersection
    CrdnPointOnSurface
    CrdnPointModelAttach
    CrdnPointSatelliteCollectionEntry
    CrdnPointPlaneProjection
    CrdnPointLagrangeLibration
    CrdnPointCommonTasks
    CrdnPointCentBodyIntersect
    CrdnPointAtTimeInstant
    CrdnPointPlugin
    CrdnPointCBFixedOffset
    CrdnSystemAssembled
    CrdnSystemOnSurface
    CrdnLLAPosition
    CrdnSystemCommonTasks
    CrdnVectorAngleRate
    CrdnVectorApoapsis
    CrdnVectorFixedAtEpoch
    CrdnVectorAngularVelocity
    CrdnVectorConing
    CrdnVectorCross
    CrdnVectorCustomScript
    CrdnVectorDerivative
    CrdnVectorDisplacement
    CrdnVectorTwoPlanesIntersection
    CrdnVectorModelAttach
    CrdnVectorProjection
    CrdnVectorScaled
    CrdnVectorEccentricity
    CrdnVectorFixedInAxes
    CrdnVectorLineOfNodes
    CrdnVectorOrbitAngularMomentum
    CrdnVectorOrbitNormal
    CrdnVectorPeriapsis
    CrdnVectorReflection
    CrdnVectorRotationVector
    CrdnVectorDirectionToStar
    CrdnVectorFixedAtTimeInstant
    CrdnVectorLinearCombination
    CrdnVectorProjectAlongVector
    CrdnVectorScalarLinearCombination
    CrdnVectorScalarScaled
    CrdnVectorVelocityAcceleration
    CrdnVectorPlugin
    CrdnVectorDispSurface
    CrdnVectorFactory
    CrdnAxesFactory
    CrdnSystemFactory
    CrdnPointFactory
    CrdnPlaneFactory
    CrdnAngleFactory
    CrdnVectorGroup
    CrdnPointGroup
    CrdnAngleGroup
    CrdnAxesGroup
    CrdnPlaneGroup
    CrdnSystemGroup
    CrdnProvider
    CrdnRoot
    CrdnWellKnownEarthSystems
    CrdnWellKnownEarthAxes
    CrdnWellKnownSunSystems
    CrdnWellKnownSunAxes
    CrdnWellKnownSystems
    CrdnWellKnownAxes
    CrdnMethodCallResult
    CrdnInterval
    CrdnIntervalCollection
    CrdnCentralBody
    CrdnCentralBodyRefTo
    CrdnCentralBodyCollection
    CrdnCollection
    CrdnPointSamplingResult
    CrdnPointSamplingInterval
    CrdnPointSamplingIntervalCollection
    CrdnAxesSamplingResult
    CrdnAxesSamplingInterval
    CrdnAxesSamplingIntervalCollection


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: ICrdnIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnInterval
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPoint
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVector
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystem
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngle
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlane
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnContext
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdn
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventFindOccurrenceResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnFindTimesResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnIntervalsVectorResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalCollectionOccurredResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnIntervalListResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnIntervalVectorCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalCollectionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnParameterSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionSetEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionSetEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarAngle
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarConstant
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarCustom
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarDataElement
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarElapsedTime
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarFunction
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarFunction2Var
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarSurfaceDistanceBetweenPoints
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarVectorComponent
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCalcScalarVectorMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionCombined
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionPointInVolume
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionScalarBounds
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionSet
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConditionSetScalarThresholds
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConverge
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnConvergeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnDerivativeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEvent
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArray
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayConditionCrossings
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayExtrema
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayFixedTimes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayMerged
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArraySignaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventArrayStartStopTimes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventExtremum
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventInterval
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalBetweenTimeInstants
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalCollectionCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalCollectionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalCollectionLighting
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalCollectionSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalFixed
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalFixedDuration
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalFromIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListFixed
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListMerged
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListScaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalListTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalScaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalSmartInterval
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventIntervalTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventSmartEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventStartStopTime
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnEventTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnFirstIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnGapsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnIntegralBasic
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnInterp
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnInterpBasic
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnLastIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnParameterSet
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnParameterSetAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnParameterSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnParameterSetGroundTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnParameterSetOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnParameterSetTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnParameterSetVector
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPruneFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPruneFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnRelativeSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSampling
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSamplingBasic
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSamplingCurvatureTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSamplingFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSamplingMethod
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSamplingMethodFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSamplingRelativeTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSignalDelay
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSignalDelayBasic
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnGridCoordinateDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnGridValuesCustom
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnGridValuesFixedNumberOfSteps
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnGridValuesFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnGridValuesMethod
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnLightTimeDelay
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolume
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalc
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcAngleOffVector
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcConditionSatMetric
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcDelayRange
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcFromScalar
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcRange
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCalcSolarIntensity
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeCombined
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeFromCalc
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeFromCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeFromGrid
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeFromTimeSatisfaction
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGrid
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridBearingAlt
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridCylindrical
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridLatLonAlt
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeGridSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeInview
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeLighting
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVolumeOverTime
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnTimeProperties
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnTypeInfo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnTemplate
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnInstance
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesLabels
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneLabels
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesAlignedAndConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesAngularOffset
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesAttitudeFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesFixed
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesSpinning
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleBetweenVectors
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleBetweenPlanes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleDihedral
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleRotation
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleToPlane
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneNormal
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneQuadrant
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneTriad
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneTwoVector
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointFixedInSystem
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointGlint
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointCovarianceGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointPlaneIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointSatelliteCollectionEntry
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointPlaneProjection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointCentBodyIntersect
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointCBFixedOffset
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemAssembled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnLLAPosition
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorAngleRate
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorAngularVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorConing
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorCross
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorDisplacement
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorTwoPlanesIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorProjection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorScaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorFixedInAxes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorLineOfNodes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorOrbitAngularMomentum
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorOrbitNormal
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorReflection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorRotationVector
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorDirectionToStar
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorProjectAlongVector
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorScalarLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorScalarScaled
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorVelocityAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorDispSurface
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnProvider
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnRoot
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnWellKnownEarthSystems
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnWellKnownEarthAxes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnWellKnownSunSystems
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnWellKnownSunAxes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnWellKnownSystems
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnWellKnownAxes
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleFindAngleResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleFindAngleWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleFindWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAngleFindResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesTransformResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesTransformWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneFindInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPlaneFindInSystemWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointLocateInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointLocateInSystemWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemTransformResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemTransformWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnSystemFindInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnVectorFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnMethodCallResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCentralBodyRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnPointSamplingIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: ICrdnAxesSamplingIntervalCollection
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

.. autoclass:: CrdnEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventFindOccurrenceResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnFindTimesResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnIntervalsVectorResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalCollectionOccurredResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnIntervalListResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnIntervalVectorCollection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalCollectionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnParameterSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionSetEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionSetEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarAngle
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarConstant
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarCustom
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarDataElement
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarElapsedTime
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarFile
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarFunction
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarFunction2Var
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarSurfaceDistanceBetweenPoints
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarVectorComponent
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCalcScalarVectorMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCondition
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionCombined
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionPointInVolume
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionScalarBounds
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionSet
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConditionSetScalarThresholds
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConverge
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnConvergeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnDerivativeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEvent
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArray
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayConditionCrossings
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayExtrema
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayFixedTimes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayMerged
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArraySignaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventArrayStartStopTimes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventExtremum
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventInterval
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalBetweenTimeInstants
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalCollectionCondition
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalCollectionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalCollectionLighting
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalCollectionSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalFixed
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalFixedDuration
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalFromIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListCondition
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListFile
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListFixed
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListMerged
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListScaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalListTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalScaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalSmartInterval
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventIntervalTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventSmartEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventStartStopTime
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnEventTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnFirstIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnGapsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnIntegralBasic
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnInterp
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnInterpBasic
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnLastIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnParameterSet
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnParameterSetAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnParameterSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnParameterSetGroundTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnParameterSetOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnParameterSetTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnParameterSetVector
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPruneFilter
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPruneFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnRelativeSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSampling
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSamplingBasic
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSamplingCurvatureTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSamplingFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSamplingMethod
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSamplingMethodFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSamplingRelativeTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSignalDelay
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSignalDelayBasic
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnGridCoordinateDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnGridValuesCustom
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnGridValuesFixedNumberOfSteps
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnGridValuesFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnGridValuesMethod
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnLightTimeDelay
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolume
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalc
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcAngleOffVector
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcConditionSatMetric
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcDelayRange
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcFile
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcFromScalar
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcRange
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCalcSolarIntensity
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeCombined
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeFromCalc
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeFromCondition
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeFromGrid
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeFromTimeSatisfaction
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGrid
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridBearingAlt
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridCylindrical
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridLatLonAlt
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeGridSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeInview
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeLighting
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVolumeOverTime
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnGeneric
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnTypeInfo
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnInstance
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnTemplate
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngleRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSystemRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVector
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesLabels
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPoint
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSystem
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngle
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneLabels
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlane
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesAlignedAndConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesAngularOffset
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesAttitudeFile
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesFixed
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesSpinning
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngleBetweenVectors
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngleBetweenPlanes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngleDihedral
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngleRotation
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngleToPlane
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneNormal
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneQuadrant
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneTriad
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneTwoVector
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointFile
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointFixedInSystem
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointGlint
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointCovarianceGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointPlaneIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointSatelliteCollectionEntry
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointPlaneProjection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointCentBodyIntersect
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointCBFixedOffset
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSystemAssembled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSystemOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnLLAPosition
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSystemCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorAngleRate
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorAngularVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorConing
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorCross
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorDisplacement
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorTwoPlanesIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorProjection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorScaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorFixedInAxes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorLineOfNodes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorOrbitAngularMomentum
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorOrbitNormal
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorReflection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorRotationVector
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorDirectionToStar
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorProjectAlongVector
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorScalarLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorScalarScaled
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorVelocityAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorDispSurface
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSystemFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngleFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnVectorGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAngleGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPlaneGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnSystemGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnProvider
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnRoot
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnWellKnownEarthSystems
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnWellKnownEarthAxes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnWellKnownSunSystems
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnWellKnownSunAxes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnWellKnownSystems
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnWellKnownAxes
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnMethodCallResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnInterval
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCentralBodyRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnCollection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnPointSamplingIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: CrdnAxesSamplingIntervalCollection
    :members:
    :exclude-members: __init__

