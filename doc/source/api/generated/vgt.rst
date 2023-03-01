Module contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    IIntervalCollection
    IInterval
    IPoint
    IVector
    ISystem
    IAxes
    IAngle
    IPlane
    IContext
    ICoordinate
    IEvaluateResult
    IEvaluateWithRateResult
    IEventIntervalResult
    IEventFindOccurrenceResult
    IFindTimesResult
    IIntervalsVectorResult
    IEventIntervalCollectionOccurredResult
    IIntervalListResult
    IIntervalVectorCollection
    IEventGroup
    IEventIntervalGroup
    IEventIntervalListGroup
    IEventArrayGroup
    ICalcScalarGroup
    IEventIntervalCollectionGroup
    IParameterSetGroup
    IConditionGroup
    IConditionSetGroup
    IConditionSetEvaluateResult
    IConditionSetEvaluateWithRateResult
    IVolumeGridGroup
    IVolumeGroup
    IVolumeCalcGroup
    ICalcScalar
    ICalcScalarAngle
    ICalcScalarConstant
    ICalcScalarCustom
    ICalcScalarDataElement
    ICalcScalarDerivative
    ICalcScalarDotProduct
    ICalcScalarElapsedTime
    ICalcScalarFactory
    ICalcScalarFile
    ICalcScalarFixedAtTimeInstant
    ICalcScalarFunction
    ICalcScalarFunction2Var
    ICalcScalarIntegral
    ICalcScalarPlugin
    ICalcScalarSurfaceDistanceBetweenPoints
    ICalcScalarVectorComponent
    ICalcScalarVectorMagnitude
    ICondition
    IConditionCombined
    IConditionFactory
    IConditionPointInVolume
    IConditionScalarBounds
    IConditionSet
    IConditionSetFactory
    IConditionSetScalarThresholds
    IConverge
    IConvergeBasic
    IDerivative
    IDerivativeBasic
    IEvent
    IEventArray
    IEventArrayConditionCrossings
    IEventArrayExtrema
    IEventArrayFactory
    IEventArrayFiltered
    IEventArrayFixedStep
    IEventArrayFixedTimes
    IEventArrayMerged
    IEventArraySignaled
    IEventArrayStartStopTimes
    IEventEpoch
    IEventExtremum
    IEventFactory
    IEventInterval
    IEventIntervalBetweenTimeInstants
    IEventIntervalCollection
    IEventIntervalCollectionCondition
    IEventIntervalCollectionFactory
    IEventIntervalCollectionLighting
    IEventIntervalCollectionSignaled
    IEventIntervalFactory
    IEventIntervalFixed
    IEventIntervalFixedDuration
    IEventIntervalFromIntervalList
    IEventIntervalList
    IEventIntervalListCondition
    IEventIntervalListFactory
    IEventIntervalListFile
    IEventIntervalListFiltered
    IEventIntervalListFixed
    IEventIntervalListMerged
    IEventIntervalListScaled
    IEventIntervalListSignaled
    IEventIntervalListTimeOffset
    IEventIntervalScaled
    IEventIntervalSignaled
    IEventIntervalSmartInterval
    IEventIntervalTimeOffset
    IEventSignaled
    IEventSmartEpoch
    IEventStartStopTime
    IEventTimeOffset
    IFirstIntervalsFilter
    IGapsFilter
    IIntegral
    IIntegralBasic
    IInterp
    IInterpBasic
    IIntervalsFilter
    ILastIntervalsFilter
    IParameterSet
    IParameterSetAttitude
    IParameterSetFactory
    IParameterSetGroundTrajectory
    IParameterSetOrbit
    IParameterSetTrajectory
    IParameterSetVector
    IPruneFilter
    IPruneFilterFactory
    IRelativeSatisfactionConditionFilter
    ISampling
    ISamplingBasic
    ISamplingCurvatureTolerance
    ISamplingFixedStep
    ISamplingMethod
    ISamplingMethodFactory
    ISamplingRelativeTolerance
    ISatisfactionConditionFilter
    ISignalDelay
    ISignalDelayBasic
    IVolumeCalcFactory
    IVolumeFactory
    IVolumeGridFactory
    IGridCoordinateDefinition
    IGridValuesCustom
    IGridValuesFixedNumberOfSteps
    IGridValuesFixedStep
    IGridValuesMethod
    ILightTimeDelay
    IVolume
    IVolumeCalc
    IVolumeCalcAltitude
    IVolumeCalcAngleOffVector
    IVolumeCalcConditionSatMetric
    IVolumeCalcDelayRange
    IVolumeCalcFile
    IVolumeCalcFromScalar
    IVolumeCalcRange
    IVolumeCalcSolarIntensity
    IVolumeCombined
    IVolumeFromCalc
    IVolumeFromCondition
    IVolumeFromGrid
    IVolumeFromTimeSatisfaction
    IVolumeGrid
    IVolumeGridBearingAlt
    IVolumeGridCartesian
    IVolumeGridConstrained
    IVolumeGridCylindrical
    IVolumeGridLatLonAlt
    IVolumeGridResult
    IVolumeGridSpherical
    IVolumeInview
    IVolumeLighting
    IVolumeOverTime
    ITimeProperties
    ITypeInfo
    IRefTo
    ITemplate
    IInstance
    IPointRefTo
    IVectorRefTo
    IAxesRefTo
    IAngleRefTo
    ISystemRefTo
    IPlaneRefTo
    IAxesLabels
    IPlaneLabels
    IAxesAlignedAndConstrained
    IAxesAngularOffset
    IAxesFixedAtEpoch
    IAxesBPlane
    IAxesCustomScript
    IAxesAttitudeFile
    IAxesFixed
    IAxesModelAttach
    IAxesSpinning
    IAxesOnSurface
    IAxesTrajectory
    IAxesLagrangeLibration
    IAxesCommonTasks
    IAxesAtTimeInstant
    IAxesPlugin
    IAngleBetweenVectors
    IAngleBetweenPlanes
    IAngleDihedral
    IAngleRotation
    IAngleToPlane
    IPlaneNormal
    IPlaneQuadrant
    IPlaneTrajectory
    IPlaneTriad
    IPlaneTwoVector
    IPointBPlane
    IPointFile
    IPointFixedInSystem
    IPointGrazing
    IPointGlint
    IPointCovarianceGrazing
    IPointPlaneIntersection
    IPointOnSurface
    IPointModelAttach
    IPointSatelliteCollectionEntry
    IPointPlaneProjection
    IPointLagrangeLibration
    IPointCommonTasks
    IPointCentBodyIntersect
    IPointAtTimeInstant
    IPointPlugin
    IPointCBFixedOffset
    ISystemAssembled
    ISystemOnSurface
    ILLAPosition
    ISystemCommonTasks
    IVectorAngleRate
    IVectorApoapsis
    IVectorFixedAtEpoch
    IVectorAngularVelocity
    IVectorConing
    IVectorCross
    IVectorCustomScript
    IVectorDerivative
    IVectorDisplacement
    IVectorTwoPlanesIntersection
    IVectorModelAttach
    IVectorProjection
    IVectorScaled
    IVectorEccentricity
    IVectorFixedInAxes
    IVectorLineOfNodes
    IVectorOrbitAngularMomentum
    IVectorOrbitNormal
    IVectorPeriapsis
    IVectorReflection
    IVectorRotationVector
    IVectorDirectionToStar
    IVectorFixedAtTimeInstant
    IVectorLinearCombination
    IVectorProjectAlongVector
    IVectorScalarLinearCombination
    IVectorScalarScaled
    IVectorVelocityAcceleration
    IVectorPlugin
    IVectorDispSurface
    IVectorFactory
    IAxesFactory
    ISystemFactory
    IPointFactory
    IPlaneFactory
    IAngleFactory
    IVectorGroup
    IPointGroup
    IAngleGroup
    IAxesGroup
    IPlaneGroup
    ISystemGroup
    IProvider
    IRoot
    IWellKnownEarthSystems
    IWellKnownEarthAxes
    IWellKnownSunSystems
    IWellKnownSunAxes
    IWellKnownSystems
    IWellKnownAxes
    IAngleFindAngleResult
    IAngleFindAngleWithRateResult
    IAngleFindWithRateResult
    IAngleFindResult
    IAxesTransformResult
    IAxesTransformWithRateResult
    IPlaneFindInAxesResult
    IPlaneFindInAxesWithRateResult
    IPlaneFindInSystemResult
    IPlaneFindInSystemWithRateResult
    IAxesFindInAxesResult
    IAxesFindInAxesWithRateResult
    IPointLocateInSystemResult
    IPointLocateInSystemWithRateResult
    ISystemTransformResult
    ISystemTransformWithRateResult
    ISystemFindInSystemResult
    IVectorFindInAxesResult
    IVectorFindInAxesWithRateResult
    IMethodCallResult
    ICentralBody
    ICentralBodyRefTo
    ICentralBodyCollection
    ICollection
    IPointSamplingResult
    IPointSamplingInterval
    IPointSamplingIntervalCollection
    IAxesSamplingResult
    IAxesSamplingInterval
    IAxesSamplingIntervalCollection


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

    EvaluateResult
    EvaluateWithRateResult
    EventIntervalResult
    EventFindOccurrenceResult
    FindTimesResult
    IntervalsVectorResult
    EventIntervalCollectionOccurredResult
    IntervalListResult
    IntervalVectorCollection
    EventGroup
    EventIntervalGroup
    EventIntervalListGroup
    EventArrayGroup
    CalcScalarGroup
    EventIntervalCollectionGroup
    ParameterSetGroup
    ConditionGroup
    ConditionSetGroup
    ConditionSetEvaluateResult
    ConditionSetEvaluateWithRateResult
    VolumeGridGroup
    VolumeGroup
    VolumeCalcGroup
    CalcScalar
    CalcScalarAngle
    CalcScalarConstant
    CalcScalarCustom
    CalcScalarDataElement
    CalcScalarDerivative
    CalcScalarDotProduct
    CalcScalarElapsedTime
    CalcScalarFactory
    CalcScalarFile
    CalcScalarFixedAtTimeInstant
    CalcScalarFunction
    CalcScalarFunction2Var
    CalcScalarIntegral
    CalcScalarPlugin
    CalcScalarSurfaceDistanceBetweenPoints
    CalcScalarVectorComponent
    CalcScalarVectorMagnitude
    Condition
    ConditionCombined
    ConditionFactory
    ConditionPointInVolume
    ConditionScalarBounds
    ConditionSet
    ConditionSetFactory
    ConditionSetScalarThresholds
    Converge
    ConvergeBasic
    Derivative
    DerivativeBasic
    Event
    EventArray
    EventArrayConditionCrossings
    EventArrayExtrema
    EventArrayFactory
    EventArrayFiltered
    EventArrayFixedStep
    EventArrayFixedTimes
    EventArrayMerged
    EventArraySignaled
    EventArrayStartStopTimes
    EventEpoch
    EventExtremum
    EventFactory
    EventInterval
    EventIntervalBetweenTimeInstants
    EventIntervalCollection
    EventIntervalCollectionCondition
    EventIntervalCollectionFactory
    EventIntervalCollectionLighting
    EventIntervalCollectionSignaled
    EventIntervalFactory
    EventIntervalFixed
    EventIntervalFixedDuration
    EventIntervalFromIntervalList
    EventIntervalList
    EventIntervalListCondition
    EventIntervalListFactory
    EventIntervalListFile
    EventIntervalListFiltered
    EventIntervalListFixed
    EventIntervalListMerged
    EventIntervalListScaled
    EventIntervalListSignaled
    EventIntervalListTimeOffset
    EventIntervalScaled
    EventIntervalSignaled
    EventIntervalSmartInterval
    EventIntervalTimeOffset
    EventSignaled
    EventSmartEpoch
    EventStartStopTime
    EventTimeOffset
    FirstIntervalsFilter
    GapsFilter
    Integral
    IntegralBasic
    Interp
    InterpBasic
    IntervalsFilter
    LastIntervalsFilter
    ParameterSet
    ParameterSetAttitude
    ParameterSetFactory
    ParameterSetGroundTrajectory
    ParameterSetOrbit
    ParameterSetTrajectory
    ParameterSetVector
    PruneFilter
    PruneFilterFactory
    RelativeSatisfactionConditionFilter
    Sampling
    SamplingBasic
    SamplingCurvatureTolerance
    SamplingFixedStep
    SamplingMethod
    SamplingMethodFactory
    SamplingRelativeTolerance
    SatisfactionConditionFilter
    SignalDelay
    SignalDelayBasic
    VolumeCalcFactory
    VolumeFactory
    VolumeGridFactory
    GridCoordinateDefinition
    GridValuesCustom
    GridValuesFixedNumberOfSteps
    GridValuesFixedStep
    GridValuesMethod
    LightTimeDelay
    Volume
    VolumeCalc
    VolumeCalcAltitude
    VolumeCalcAngleOffVector
    VolumeCalcConditionSatMetric
    VolumeCalcDelayRange
    VolumeCalcFile
    VolumeCalcFromScalar
    VolumeCalcRange
    VolumeCalcSolarIntensity
    VolumeCombined
    VolumeFromCalc
    VolumeFromCondition
    VolumeFromGrid
    VolumeFromTimeSatisfaction
    VolumeGrid
    VolumeGridBearingAlt
    VolumeGridCartesian
    VolumeGridConstrained
    VolumeGridCylindrical
    VolumeGridLatLonAlt
    VolumeGridResult
    VolumeGridSpherical
    VolumeInview
    VolumeLighting
    VolumeOverTime
    Generic
    TypeInfo
    Instance
    Template
    PointRefTo
    VectorRefTo
    AxesRefTo
    AngleRefTo
    SystemRefTo
    PlaneRefTo
    Vector
    AxesLabels
    Axes
    Point
    System
    Angle
    PlaneLabels
    Plane
    AxesAlignedAndConstrained
    AxesAngularOffset
    AxesFixedAtEpoch
    AxesBPlane
    AxesCustomScript
    AxesAttitudeFile
    AxesFixed
    AxesModelAttach
    AxesSpinning
    AxesOnSurface
    AxesTrajectory
    AxesLagrangeLibration
    AxesCommonTasks
    AxesAtTimeInstant
    AxesPlugin
    AngleBetweenVectors
    AngleBetweenPlanes
    AngleDihedral
    AngleRotation
    AngleToPlane
    PlaneNormal
    PlaneQuadrant
    PlaneTrajectory
    PlaneTriad
    PlaneTwoVector
    PointBPlane
    PointFile
    PointFixedInSystem
    PointGrazing
    PointGlint
    PointCovarianceGrazing
    PointPlaneIntersection
    PointOnSurface
    PointModelAttach
    PointSatelliteCollectionEntry
    PointPlaneProjection
    PointLagrangeLibration
    PointCommonTasks
    PointCentBodyIntersect
    PointAtTimeInstant
    PointPlugin
    PointCBFixedOffset
    SystemAssembled
    SystemOnSurface
    LLAPosition
    SystemCommonTasks
    VectorAngleRate
    VectorApoapsis
    VectorFixedAtEpoch
    VectorAngularVelocity
    VectorConing
    VectorCross
    VectorCustomScript
    VectorDerivative
    VectorDisplacement
    VectorTwoPlanesIntersection
    VectorModelAttach
    VectorProjection
    VectorScaled
    VectorEccentricity
    VectorFixedInAxes
    VectorLineOfNodes
    VectorOrbitAngularMomentum
    VectorOrbitNormal
    VectorPeriapsis
    VectorReflection
    VectorRotationVector
    VectorDirectionToStar
    VectorFixedAtTimeInstant
    VectorLinearCombination
    VectorProjectAlongVector
    VectorScalarLinearCombination
    VectorScalarScaled
    VectorVelocityAcceleration
    VectorPlugin
    VectorDispSurface
    VectorFactory
    AxesFactory
    SystemFactory
    PointFactory
    PlaneFactory
    AngleFactory
    VectorGroup
    PointGroup
    AngleGroup
    AxesGroup
    PlaneGroup
    SystemGroup
    Provider
    Root
    WellKnownEarthSystems
    WellKnownEarthAxes
    WellKnownSunSystems
    WellKnownSunAxes
    WellKnownSystems
    WellKnownAxes
    MethodCallResult
    Interval
    IntervalCollection
    CentralBody
    CentralBodyRefTo
    CentralBodyCollection
    Collection
    PointSamplingResult
    PointSamplingInterval
    PointSamplingIntervalCollection
    AxesSamplingResult
    AxesSamplingInterval
    AxesSamplingIntervalCollection


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: IIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IVector
    :members:
    :exclude-members: __init__
.. autoclass:: ISystem
    :members:
    :exclude-members: __init__
.. autoclass:: IAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IAngle
    :members:
    :exclude-members: __init__
.. autoclass:: IPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IContext
    :members:
    :exclude-members: __init__
.. autoclass:: ICoordinate
    :members:
    :exclude-members: __init__
.. autoclass:: IEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalResult
    :members:
    :exclude-members: __init__
.. autoclass:: IEventFindOccurrenceResult
    :members:
    :exclude-members: __init__
.. autoclass:: IFindTimesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IIntervalsVectorResult
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalCollectionOccurredResult
    :members:
    :exclude-members: __init__
.. autoclass:: IIntervalListResult
    :members:
    :exclude-members: __init__
.. autoclass:: IIntervalVectorCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IEventGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalCollectionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IParameterSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionSetEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionSetEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarAngle
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarConstant
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarCustom
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarDataElement
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarElapsedTime
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarFile
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarFunction
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarFunction2Var
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarSurfaceDistanceBetweenPoints
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarVectorComponent
    :members:
    :exclude-members: __init__
.. autoclass:: ICalcScalarVectorMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: ICondition
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionCombined
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionPointInVolume
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionScalarBounds
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionSet
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IConditionSetScalarThresholds
    :members:
    :exclude-members: __init__
.. autoclass:: IConverge
    :members:
    :exclude-members: __init__
.. autoclass:: IConvergeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: IDerivativeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IEvent
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArray
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayConditionCrossings
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayExtrema
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayFixedTimes
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayMerged
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArraySignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IEventArrayStartStopTimes
    :members:
    :exclude-members: __init__
.. autoclass:: IEventEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IEventExtremum
    :members:
    :exclude-members: __init__
.. autoclass:: IEventFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IEventInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalBetweenTimeInstants
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalCollectionCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalCollectionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalCollectionLighting
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalCollectionSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalFixed
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalFixedDuration
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalFromIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListFile
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListFixed
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListMerged
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListScaled
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalListTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalScaled
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalSmartInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IEventIntervalTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IEventSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: IEventSmartEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IEventStartStopTime
    :members:
    :exclude-members: __init__
.. autoclass:: IEventTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IFirstIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IGapsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: IIntegralBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IInterp
    :members:
    :exclude-members: __init__
.. autoclass:: IInterpBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ILastIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IParameterSet
    :members:
    :exclude-members: __init__
.. autoclass:: IParameterSetAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: IParameterSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IParameterSetGroundTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: IParameterSetOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: IParameterSetTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: IParameterSetVector
    :members:
    :exclude-members: __init__
.. autoclass:: IPruneFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IPruneFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IRelativeSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ISampling
    :members:
    :exclude-members: __init__
.. autoclass:: ISamplingBasic
    :members:
    :exclude-members: __init__
.. autoclass:: ISamplingCurvatureTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: ISamplingFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: ISamplingMethod
    :members:
    :exclude-members: __init__
.. autoclass:: ISamplingMethodFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ISamplingRelativeTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: ISatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ISignalDelay
    :members:
    :exclude-members: __init__
.. autoclass:: ISignalDelayBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IGridCoordinateDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: IGridValuesCustom
    :members:
    :exclude-members: __init__
.. autoclass:: IGridValuesFixedNumberOfSteps
    :members:
    :exclude-members: __init__
.. autoclass:: IGridValuesFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: IGridValuesMethod
    :members:
    :exclude-members: __init__
.. autoclass:: ILightTimeDelay
    :members:
    :exclude-members: __init__
.. autoclass:: IVolume
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcAngleOffVector
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcConditionSatMetric
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcDelayRange
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcFile
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcFromScalar
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcRange
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCalcSolarIntensity
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeCombined
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeFromCalc
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeFromCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeFromGrid
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeFromTimeSatisfaction
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGrid
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridBearingAlt
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridCylindrical
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridLatLonAlt
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridResult
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeGridSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeInview
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeLighting
    :members:
    :exclude-members: __init__
.. autoclass:: IVolumeOverTime
    :members:
    :exclude-members: __init__
.. autoclass:: ITimeProperties
    :members:
    :exclude-members: __init__
.. autoclass:: ITypeInfo
    :members:
    :exclude-members: __init__
.. autoclass:: IRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ITemplate
    :members:
    :exclude-members: __init__
.. autoclass:: IInstance
    :members:
    :exclude-members: __init__
.. autoclass:: IPointRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesLabels
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneLabels
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesAlignedAndConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesAngularOffset
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesAttitudeFile
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesFixed
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesSpinning
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleBetweenVectors
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleBetweenPlanes
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleDihedral
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleRotation
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleToPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneNormal
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneQuadrant
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneTriad
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneTwoVector
    :members:
    :exclude-members: __init__
.. autoclass:: IPointBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: IPointFile
    :members:
    :exclude-members: __init__
.. autoclass:: IPointFixedInSystem
    :members:
    :exclude-members: __init__
.. autoclass:: IPointGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: IPointGlint
    :members:
    :exclude-members: __init__
.. autoclass:: IPointCovarianceGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: IPointPlaneIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: IPointOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: IPointModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: IPointSatelliteCollectionEntry
    :members:
    :exclude-members: __init__
.. autoclass:: IPointPlaneProjection
    :members:
    :exclude-members: __init__
.. autoclass:: IPointLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: IPointCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: IPointCentBodyIntersect
    :members:
    :exclude-members: __init__
.. autoclass:: IPointAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: IPointPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IPointCBFixedOffset
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemAssembled
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: ILLAPosition
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorAngleRate
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorAngularVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorConing
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorCross
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorDisplacement
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorTwoPlanesIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorProjection
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorScaled
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorFixedInAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorLineOfNodes
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorOrbitAngularMomentum
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorOrbitNormal
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorReflection
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorRotationVector
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorDirectionToStar
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorProjectAlongVector
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorScalarLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorScalarScaled
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorVelocityAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorDispSurface
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IPointFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IPointGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemGroup
    :members:
    :exclude-members: __init__
.. autoclass:: IProvider
    :members:
    :exclude-members: __init__
.. autoclass:: IRoot
    :members:
    :exclude-members: __init__
.. autoclass:: IWellKnownEarthSystems
    :members:
    :exclude-members: __init__
.. autoclass:: IWellKnownEarthAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IWellKnownSunSystems
    :members:
    :exclude-members: __init__
.. autoclass:: IWellKnownSunAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IWellKnownSystems
    :members:
    :exclude-members: __init__
.. autoclass:: IWellKnownAxes
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleFindAngleResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleFindAngleWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleFindWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAngleFindResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesTransformResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesTransformWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneFindInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPlaneFindInSystemWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPointLocateInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPointLocateInSystemWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemTransformResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemTransformWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISystemFindInSystemResult
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorFindInAxesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorFindInAxesWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: IMethodCallResult
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ICollection
    :members:
    :exclude-members: __init__
.. autoclass:: IPointSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPointSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IPointSamplingIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesSamplingIntervalCollection
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

.. autoclass:: EvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: EvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalResult
    :members:
    :exclude-members: __init__
.. autoclass:: EventFindOccurrenceResult
    :members:
    :exclude-members: __init__
.. autoclass:: FindTimesResult
    :members:
    :exclude-members: __init__
.. autoclass:: IntervalsVectorResult
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalCollectionOccurredResult
    :members:
    :exclude-members: __init__
.. autoclass:: IntervalListResult
    :members:
    :exclude-members: __init__
.. autoclass:: IntervalVectorCollection
    :members:
    :exclude-members: __init__
.. autoclass:: EventGroup
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalGroup
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListGroup
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarGroup
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalCollectionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ParameterSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionSetGroup
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionSetEvaluateResult
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionSetEvaluateWithRateResult
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridGroup
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGroup
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcGroup
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalar
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarAngle
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarConstant
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarCustom
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarDataElement
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarDotProduct
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarElapsedTime
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarFile
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarFunction
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarFunction2Var
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarIntegral
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarSurfaceDistanceBetweenPoints
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarVectorComponent
    :members:
    :exclude-members: __init__
.. autoclass:: CalcScalarVectorMagnitude
    :members:
    :exclude-members: __init__
.. autoclass:: Condition
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionCombined
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionPointInVolume
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionScalarBounds
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionSet
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ConditionSetScalarThresholds
    :members:
    :exclude-members: __init__
.. autoclass:: Converge
    :members:
    :exclude-members: __init__
.. autoclass:: ConvergeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: Derivative
    :members:
    :exclude-members: __init__
.. autoclass:: DerivativeBasic
    :members:
    :exclude-members: __init__
.. autoclass:: Event
    :members:
    :exclude-members: __init__
.. autoclass:: EventArray
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayConditionCrossings
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayExtrema
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayFixedTimes
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayMerged
    :members:
    :exclude-members: __init__
.. autoclass:: EventArraySignaled
    :members:
    :exclude-members: __init__
.. autoclass:: EventArrayStartStopTimes
    :members:
    :exclude-members: __init__
.. autoclass:: EventEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: EventExtremum
    :members:
    :exclude-members: __init__
.. autoclass:: EventFactory
    :members:
    :exclude-members: __init__
.. autoclass:: EventInterval
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalBetweenTimeInstants
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalCollectionCondition
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalCollectionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalCollectionLighting
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalCollectionSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalFactory
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalFixed
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalFixedDuration
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalFromIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalList
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListCondition
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListFactory
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListFile
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListFiltered
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListFixed
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListMerged
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListScaled
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalListTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalScaled
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalSmartInterval
    :members:
    :exclude-members: __init__
.. autoclass:: EventIntervalTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: EventSignaled
    :members:
    :exclude-members: __init__
.. autoclass:: EventSmartEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: EventStartStopTime
    :members:
    :exclude-members: __init__
.. autoclass:: EventTimeOffset
    :members:
    :exclude-members: __init__
.. autoclass:: FirstIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: GapsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: Integral
    :members:
    :exclude-members: __init__
.. autoclass:: IntegralBasic
    :members:
    :exclude-members: __init__
.. autoclass:: Interp
    :members:
    :exclude-members: __init__
.. autoclass:: InterpBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: LastIntervalsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ParameterSet
    :members:
    :exclude-members: __init__
.. autoclass:: ParameterSetAttitude
    :members:
    :exclude-members: __init__
.. autoclass:: ParameterSetFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ParameterSetGroundTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: ParameterSetOrbit
    :members:
    :exclude-members: __init__
.. autoclass:: ParameterSetTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: ParameterSetVector
    :members:
    :exclude-members: __init__
.. autoclass:: PruneFilter
    :members:
    :exclude-members: __init__
.. autoclass:: PruneFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: RelativeSatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: Sampling
    :members:
    :exclude-members: __init__
.. autoclass:: SamplingBasic
    :members:
    :exclude-members: __init__
.. autoclass:: SamplingCurvatureTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: SamplingFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: SamplingMethod
    :members:
    :exclude-members: __init__
.. autoclass:: SamplingMethodFactory
    :members:
    :exclude-members: __init__
.. autoclass:: SamplingRelativeTolerance
    :members:
    :exclude-members: __init__
.. autoclass:: SatisfactionConditionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: SignalDelay
    :members:
    :exclude-members: __init__
.. autoclass:: SignalDelayBasic
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcFactory
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeFactory
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridFactory
    :members:
    :exclude-members: __init__
.. autoclass:: GridCoordinateDefinition
    :members:
    :exclude-members: __init__
.. autoclass:: GridValuesCustom
    :members:
    :exclude-members: __init__
.. autoclass:: GridValuesFixedNumberOfSteps
    :members:
    :exclude-members: __init__
.. autoclass:: GridValuesFixedStep
    :members:
    :exclude-members: __init__
.. autoclass:: GridValuesMethod
    :members:
    :exclude-members: __init__
.. autoclass:: LightTimeDelay
    :members:
    :exclude-members: __init__
.. autoclass:: Volume
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalc
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcAngleOffVector
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcConditionSatMetric
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcDelayRange
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcFile
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcFromScalar
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcRange
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCalcSolarIntensity
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeCombined
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeFromCalc
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeFromCondition
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeFromGrid
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeFromTimeSatisfaction
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGrid
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridBearingAlt
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridCartesian
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridCylindrical
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridLatLonAlt
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridResult
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeGridSpherical
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeInview
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeLighting
    :members:
    :exclude-members: __init__
.. autoclass:: VolumeOverTime
    :members:
    :exclude-members: __init__
.. autoclass:: Generic
    :members:
    :exclude-members: __init__
.. autoclass:: TypeInfo
    :members:
    :exclude-members: __init__
.. autoclass:: Instance
    :members:
    :exclude-members: __init__
.. autoclass:: Template
    :members:
    :exclude-members: __init__
.. autoclass:: PointRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: VectorRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AxesRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: AngleRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: SystemRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: Vector
    :members:
    :exclude-members: __init__
.. autoclass:: AxesLabels
    :members:
    :exclude-members: __init__
.. autoclass:: Axes
    :members:
    :exclude-members: __init__
.. autoclass:: Point
    :members:
    :exclude-members: __init__
.. autoclass:: System
    :members:
    :exclude-members: __init__
.. autoclass:: Angle
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneLabels
    :members:
    :exclude-members: __init__
.. autoclass:: Plane
    :members:
    :exclude-members: __init__
.. autoclass:: AxesAlignedAndConstrained
    :members:
    :exclude-members: __init__
.. autoclass:: AxesAngularOffset
    :members:
    :exclude-members: __init__
.. autoclass:: AxesFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: AxesBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: AxesCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: AxesAttitudeFile
    :members:
    :exclude-members: __init__
.. autoclass:: AxesFixed
    :members:
    :exclude-members: __init__
.. autoclass:: AxesModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: AxesSpinning
    :members:
    :exclude-members: __init__
.. autoclass:: AxesOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: AxesTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: AxesLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: AxesCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: AxesAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: AxesPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: AngleBetweenVectors
    :members:
    :exclude-members: __init__
.. autoclass:: AngleBetweenPlanes
    :members:
    :exclude-members: __init__
.. autoclass:: AngleDihedral
    :members:
    :exclude-members: __init__
.. autoclass:: AngleRotation
    :members:
    :exclude-members: __init__
.. autoclass:: AngleToPlane
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneNormal
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneQuadrant
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneTrajectory
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneTriad
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneTwoVector
    :members:
    :exclude-members: __init__
.. autoclass:: PointBPlane
    :members:
    :exclude-members: __init__
.. autoclass:: PointFile
    :members:
    :exclude-members: __init__
.. autoclass:: PointFixedInSystem
    :members:
    :exclude-members: __init__
.. autoclass:: PointGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: PointGlint
    :members:
    :exclude-members: __init__
.. autoclass:: PointCovarianceGrazing
    :members:
    :exclude-members: __init__
.. autoclass:: PointPlaneIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: PointOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: PointModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: PointSatelliteCollectionEntry
    :members:
    :exclude-members: __init__
.. autoclass:: PointPlaneProjection
    :members:
    :exclude-members: __init__
.. autoclass:: PointLagrangeLibration
    :members:
    :exclude-members: __init__
.. autoclass:: PointCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: PointCentBodyIntersect
    :members:
    :exclude-members: __init__
.. autoclass:: PointAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: PointPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: PointCBFixedOffset
    :members:
    :exclude-members: __init__
.. autoclass:: SystemAssembled
    :members:
    :exclude-members: __init__
.. autoclass:: SystemOnSurface
    :members:
    :exclude-members: __init__
.. autoclass:: LLAPosition
    :members:
    :exclude-members: __init__
.. autoclass:: SystemCommonTasks
    :members:
    :exclude-members: __init__
.. autoclass:: VectorAngleRate
    :members:
    :exclude-members: __init__
.. autoclass:: VectorApoapsis
    :members:
    :exclude-members: __init__
.. autoclass:: VectorFixedAtEpoch
    :members:
    :exclude-members: __init__
.. autoclass:: VectorAngularVelocity
    :members:
    :exclude-members: __init__
.. autoclass:: VectorConing
    :members:
    :exclude-members: __init__
.. autoclass:: VectorCross
    :members:
    :exclude-members: __init__
.. autoclass:: VectorCustomScript
    :members:
    :exclude-members: __init__
.. autoclass:: VectorDerivative
    :members:
    :exclude-members: __init__
.. autoclass:: VectorDisplacement
    :members:
    :exclude-members: __init__
.. autoclass:: VectorTwoPlanesIntersection
    :members:
    :exclude-members: __init__
.. autoclass:: VectorModelAttach
    :members:
    :exclude-members: __init__
.. autoclass:: VectorProjection
    :members:
    :exclude-members: __init__
.. autoclass:: VectorScaled
    :members:
    :exclude-members: __init__
.. autoclass:: VectorEccentricity
    :members:
    :exclude-members: __init__
.. autoclass:: VectorFixedInAxes
    :members:
    :exclude-members: __init__
.. autoclass:: VectorLineOfNodes
    :members:
    :exclude-members: __init__
.. autoclass:: VectorOrbitAngularMomentum
    :members:
    :exclude-members: __init__
.. autoclass:: VectorOrbitNormal
    :members:
    :exclude-members: __init__
.. autoclass:: VectorPeriapsis
    :members:
    :exclude-members: __init__
.. autoclass:: VectorReflection
    :members:
    :exclude-members: __init__
.. autoclass:: VectorRotationVector
    :members:
    :exclude-members: __init__
.. autoclass:: VectorDirectionToStar
    :members:
    :exclude-members: __init__
.. autoclass:: VectorFixedAtTimeInstant
    :members:
    :exclude-members: __init__
.. autoclass:: VectorLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: VectorProjectAlongVector
    :members:
    :exclude-members: __init__
.. autoclass:: VectorScalarLinearCombination
    :members:
    :exclude-members: __init__
.. autoclass:: VectorScalarScaled
    :members:
    :exclude-members: __init__
.. autoclass:: VectorVelocityAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: VectorPlugin
    :members:
    :exclude-members: __init__
.. autoclass:: VectorDispSurface
    :members:
    :exclude-members: __init__
.. autoclass:: VectorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AxesFactory
    :members:
    :exclude-members: __init__
.. autoclass:: SystemFactory
    :members:
    :exclude-members: __init__
.. autoclass:: PointFactory
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AngleFactory
    :members:
    :exclude-members: __init__
.. autoclass:: VectorGroup
    :members:
    :exclude-members: __init__
.. autoclass:: PointGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AngleGroup
    :members:
    :exclude-members: __init__
.. autoclass:: AxesGroup
    :members:
    :exclude-members: __init__
.. autoclass:: PlaneGroup
    :members:
    :exclude-members: __init__
.. autoclass:: SystemGroup
    :members:
    :exclude-members: __init__
.. autoclass:: Provider
    :members:
    :exclude-members: __init__
.. autoclass:: Root
    :members:
    :exclude-members: __init__
.. autoclass:: WellKnownEarthSystems
    :members:
    :exclude-members: __init__
.. autoclass:: WellKnownEarthAxes
    :members:
    :exclude-members: __init__
.. autoclass:: WellKnownSunSystems
    :members:
    :exclude-members: __init__
.. autoclass:: WellKnownSunAxes
    :members:
    :exclude-members: __init__
.. autoclass:: WellKnownSystems
    :members:
    :exclude-members: __init__
.. autoclass:: WellKnownAxes
    :members:
    :exclude-members: __init__
.. autoclass:: MethodCallResult
    :members:
    :exclude-members: __init__
.. autoclass:: Interval
    :members:
    :exclude-members: __init__
.. autoclass:: IntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBody
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyRefTo
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyCollection
    :members:
    :exclude-members: __init__
.. autoclass:: Collection
    :members:
    :exclude-members: __init__
.. autoclass:: PointSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: PointSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: PointSamplingIntervalCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AxesSamplingResult
    :members:
    :exclude-members: __init__
.. autoclass:: AxesSamplingInterval
    :members:
    :exclude-members: __init__
.. autoclass:: AxesSamplingIntervalCollection
    :members:
    :exclude-members: __init__

