
The ``vgt`` module
==================


.. py:module:: ansys.stk.core.vgt


Summary
-------

.. tab-set::

 
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`
              - The interface defines methods and properties common to all points.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`
              - The interface defines methods and properties common to all vectors.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolSystem`
              - The interface contains methods and properties shared by all VGT systems.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`
              - The interface defines methods and properties common to all axes.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngle`
              - The interface defines methods and properties common to all angles.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPlane`
              - The interface defines methods and properties common to all VGT planes.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchContext`
              - The interface represents a context associated with a VGT component. All VGT components are associated with a valid context. A context can represent a VGT instance or a VGT template.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`
              - A base interface implemented by all VGT components. The methods and properties of the interface provide type information about the VGT component.

            * - :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :py:class:`~ansys.stk.core.vgt.ICalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :py:class:`~ansys.stk.core.vgt.ICalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchConverge`
              - Represents a base class for convergence definitions.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolEvent`
              - Define an event (time instant).

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolEventArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolEventInterval`
              - A single time interval.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollection`
              - A collection of related interval lists.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolEventIntervalList`
              - An ordered list of time intervals.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchInterp`
              - Represents a base class for interpolation definitions.

            * - :py:class:`~ansys.stk.core.vgt.ICalculationToolParameterSet`
              - Parameter set contains various sets of scalar computations.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolPruneFilter`
              - A filter used with event interval list pruned class to prune interval lists...

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchSampling`
              - Base sampling interface.

            * - :py:class:`~ansys.stk.core.vgt.ICalculationToolSamplingMethod`
              - A sampling method.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolGridValuesMethod`
              - A grid values method.

            * - :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolume`
              - A volume interface. The methods and properties of the interface provide Volume functions.

            * - :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalc`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`
              - Define methods to compute time properties such as availability and special times.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchRefTo`
              - A base interface for all VGT component references.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleResult`
              - Contains the results returned with IAgCrdnAngle.FindAngle method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindAngleWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindAngleWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinatesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngleFindResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinates method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTransformResult`
              - Contains the results returned with IAgCrdnAxes.TransformFrom method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult`
              - Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystem method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystem method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolSystemTransformResult`
              - Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolSystemTransformWithRateResult`
              - Contains the results returned with IAgCrdnSystem.TransformFromWithRate and IAgCrdnSystem.TransformToWithRate methods.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult`
              - Contains the results returned with IAgCrdnSystem.FindInSystem method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesResult`
              - Contains the results returned with IAgCrdnVector.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnVector.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`
              - Instances of the interface are used to return the result of a computation.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolEvaluateResult`
              - Represents the results of evaluating a scalar component.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolEvaluateWithRateResult`
              - Represents the results of evaluating a scalar component.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventFindOccurrenceResult`
              - Contains the results returned with IAgCrdnEvent.FindOccurrence method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolFindTimesResult`
              - Return a collection of intervals and an array of times.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalsVectorResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.FindIntervalCollection method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionOccurredResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.Occurred method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalListResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalVectorCollection`
              - A collection of interval collections.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventGroup`
              - Access or create VGT events associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalGroup`
              - Access or create VGT event intervals associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListGroup`
              - Access or create VGT event interval lists associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayGroup`
              - Access or create VGT event arrays associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarGroup`
              - Access or create VGT calculation scalars associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionGroup`
              - Access or create VGT event interval collections associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup`
              - Access or create VGT parameter sets associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionGroup`
              - Access or create VGT conditions associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSetGroup`
              - Allow accessing and creating condition set components.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSetEvaluateResult`
              - Represents the results returned by ConditionSet.Evaluate.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSetEvaluateWithRateResult`
              - Represents the results returned by ConditionSet.EvaluateWithRate.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridGroup`
              - Access or create VGT volume grids associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGroup`
              - Access or create spatial conditions associated with a volume grid.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup`
              - Access or create VGT volume calc associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarAngle`
              - Scalar equal to angular displacement obtained from any angle in VGT.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarAverage`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarConstant`
              - Constant scalar value of specified dimension.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarCustom`
              - A calc scalar based on a scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarCustomInline`
              - A calc scalar based on using an inline scripted algorithm in MATLAB, Perl, VBScript or JScript to define its value and rate.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarDataElement`
              - Any time-dependent data element from STK data providers available for parent STK object.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarDerivative`
              - Derivative of an input scalar calculation.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarDotProduct`
              - Dot product between two vectors.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarElapsedTime`
              - Time elapsed since the reference time instant. Negative if in the past.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarFactory`
              - The factory creates scalar calculation components.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarFile`
              - Tabulated scalar calculation data loaded from specified file - a file with .csc extension.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarFixedAtTimeInstant`
              - Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarFunction`
              - Defined by performing the specified function on the input scalar or time instant.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarFunction2Var`
              - Defined by performing a function(x,y) on two scalar arguments.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarIntegral`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarPlugin`
              - Use a scalar calculation plugin.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarPointInVolumeCalc`
              - Scalar value of spatial calculation evaluated along trajectory of point.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarStandardDeviation`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarSurfaceDistanceBetweenPoints`
              - Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarVectorComponent`
              - The specified component of a vector when resolved in the specified axes.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarVectorMagnitude`
              - Scalar equal to the magnitude of a specified vector.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionCombined`
              - Define a condition which combines multiple conditions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionFactory`
              - The factory creates condition components.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionPointInVolume`
              - Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionScalarBounds`
              - Defined by determining if input scalar is within specified bounds; returns +1 if satisfied, -1 if not satisfied and 0 if on boundary.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSetFactory`
              - The factory creates condition set components.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSetScalarThresholds`
              - Condition set based on single scalar calculation compared to set of threshold values.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchConverge`
              - Represents a base class for convergence definitions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConvergeBasic`
              - Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolDerivativeBasic`
              - Derivative definition determines how numerical differencing is used to compute derivatives.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEvent`
              - Define an event (time instant).

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayConditionCrossings`
              - Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayExtrema`
              - Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayFactory`
              - The factory creates event arrays.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayFiltered`
              - Defined by filtering times from original time array according to specified filtering method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayFixedStep`
              - Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayFixedTimes`
              - Array defined by time ordered instants each explicitly specified.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayMerged`
              - Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArraySignaled`
              - Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventArrayStartStopTimes`
              - Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventEpoch`
              - Event set at specified date/time.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventExtremum`
              - Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventFactory`
              - The factory creates events.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventInterval`
              - A single time interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalBetweenTimeInstants`
              - Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalCollection`
              - A collection of related interval lists.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionFactory`
              - The factory creates collections of event interval lists.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionLighting`
              - Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalCollectionSignaled`
              - Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalFactory`
              - The factory creates event intervals.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalFixed`
              - Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalFixedDuration`
              - Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalFromIntervalList`
              - Interval created from specified interval list by using one of several selection methods.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalList`
              - An ordered list of time intervals.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListFactory`
              - The factory creates event interval lists.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListFile`
              - Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListFiltered`
              - Defined by filtering intervals from original interval list using specified filtering method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListFixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListMerged`
              - Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListScaled`
              - Interval List defined by scaling every interval in original interval list using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval is removed from scaled list...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListSignaled`
              - Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalListTimeOffset`
              - Interval List defined by shifting the specified reference interval list by a fixed time offset.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalScaled`
              - Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalSignaled`
              - Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalSmartInterval`
              - A smart interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventIntervalTimeOffset`
              - Interval defined by shifting specified reference interval by fixed time offset.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventSignaled`
              - Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventSmartEpoch`
              - A smart epoch.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventStartStopTime`
              - Event is either start or stop time selected from a reference interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolEventTimeOffset`
              - Event at fixed offset from specified reference event.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolFirstIntervalsFilter`
              - The filter selects a portion of first intervals.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolGapsFilter`
              - The filter merges intervals unless they are separated by gaps of at least/most certain duration.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolIntegralBasic`
              - Integral definition determines how scalar calculation is numerically integrated.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchInterp`
              - Represents a base class for interpolation definitions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolInterpBasic`
              - Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalsFilter`
              - The filter selects intervals of at least/most certain duration.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolLastIntervalsFilter`
              - The filter selects a portion of last intervals.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolParameterSet`
              - Parameter set contains various sets of scalar computations.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolParameterSetAttitude`
              - Attitude parameter set contains various representations of attitude of one set of axes relative to another.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolParameterSetFactory`
              - The factory is used to create instances of available parameter set types.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolParameterSetGroundTrajectory`
              - Ground trajectory parameter set contains various representations of trajectory of a point relative to central body reference shape.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolParameterSetOrbit`
              - Orbit parameter set contains various trajectory representations of an orbiting point.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolParameterSetTrajectory`
              - Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolParameterSetVector`
              - Vector parameter set contains various representations of a vector in a reference set of axes.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolPruneFilter`
              - A filter used with event interval list pruned class to prune interval lists...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolPruneFilterFactory`
              - The factory creates pruning filters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolRelativeSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchSampling`
              - Base sampling interface.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolSamplingBasic`
              - Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolSamplingCurvatureTolerance`
              - Curvature tolerance definition includes parameters that determine how scalar data should be sampled based on limits on slope changes between samples.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolSamplingFixedStep`
              - Fixed step definition includes parameters that determine how scalar data should be sampled based on fixed steps between samples.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolSamplingMethod`
              - A sampling method.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolSamplingMethodFactory`
              - The factory creates sampling method components.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolSamplingRelativeTolerance`
              - Relative tolerance definition includes parameters that determine how scalar data should be sampled based on limits on difference between actual changes between samples and changes predicted by dead reckoning.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain duration.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolSignalDelayBasic`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcFactory`
              - The factory is used to create instances of volume calcs.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory`
              - The factory is used to create instances of volumes.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridFactory`
              - The factory is used to create instances of volume grids.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolGridCoordinateDefinition`
              - Define a set of coordinate values.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesCustom`
              - Fixed step grid values.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedNumberOfSteps`
              - Fixed step grid values.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesFixedStep`
              - Fixed step grid values.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolGridValuesMethod`
              - A grid values method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolLightTimeDelay`
              - Manage Light Time Delay options..

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolume`
              - A volume interface. The methods and properties of the interface provide Volume functions.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalc`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude`
              - A volume calc altitude interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAngleOffVector`
              - A volume calc angle off vector interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcConditionSatMetric`
              - A volume calc condition satisfaction interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcDelayRange`
              - A volume calc propagation delay to location interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcFile`
              - Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcFromScalar`
              - A volume calc scalar to location interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange`
              - A volume calc distance to location interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcSolarIntensity`
              - A volume calc solar intensityn interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCombined`
              - A combined volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromCalc`
              - An volume from calc volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromCondition`
              - A volume from conditioninterface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromGrid`
              - An over time volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFromTimeSatisfaction`
              - An volume from time satisfaction volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt`
              - A volume grid bearing alt (Surface Bearing) interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian`
              - A volume grid Cartesian interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridConstrained`
              - A volume grid constrained interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical`
              - A volume grid cylindrical interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt`
              - A volume grid lat lon alt (Cartogrographic) interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridResult`
              - An interface that generates Volume Grid results.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical`
              - A volume grid spherical interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeInview`
              - An Inview volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeLighting`
              - A lighting volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeOverTime`
              - An over time volume interface.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchGeneric`
              - Generic VGT component.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchTypeInfo`
              - VGT component info.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchInstance`
              - Enable to obtain information about the parent object that owns the VGT component.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchTemplate`
              - Enable to obtain information about the STK class that owns the VGT component.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointRefTo`
              - Represents a reference to a VGT point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorRefTo`
              - Represents a vector reference.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesRefTo`
              - Represents a reference to a VGT axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleRefTo`
              - Represents a reference to a VGT angle.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemRefTo`
              - Represents a System reference.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneRefTo`
              - Represents a Plane reference.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVector`
              - A generic vector class.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesLabels`
              - Allow configuring the VGT axes labels.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxes`
              - A generic axes class.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPoint`
              - A generic VGT point class.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystem`
              - Base class for VGT axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngle`
              - Base class for VGT axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneLabels`
              - Allow configuring the X and Y axes labels.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlane`
              - Base class for VGT axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesAlignedAndConstrained`
              - Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesAngularOffset`
              - Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesFixedAtEpoch`
              - Axes based on another set fixed at a specified epoch.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesBPlane`
              - B-Plane axes using the selected target body and reference vector.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesCustomScript`
              - Customized axes offset with respect to a set of reference Axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesAttitudeFile`
              - Axes specified by data from a file.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesFixed`
              - Axes fixed in reference axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesModelAttach`
              - Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesSpinning`
              - Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesOnSurface`
              - Topocentric axes located at the reference point's projection on the central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesTrajectory`
              - Axes based on trajectory of the point relative to the reference coordinate system.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesLagrangeLibration`
              - Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesCommonTasks`
              - Provide methods to create non-persistent VGT axes components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesAtTimeInstant`
              - Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesPlugin`
              - A VGT axes plugin.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleBetweenVectors`
              - An angle between two vectors.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleBetweenPlanes`
              - An angle between two planes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleDihedral`
              - An angle between two vectors about an axis.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleRotation`
              - Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleToPlane`
              - An angle between a vector and a plane.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneNormal`
              - A plane normal to a vector at a given point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneQuadrant`
              - A plane based on a selected Quadrant of a reference system.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneTrajectory`
              - The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneTriad`
              - A Plane containing points PointA, PointB and ReferencePont with the first axis aligned with the direction from the ReferencePoint to PointA and the second axis toward the direction from the ReferencePoint to PointB.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneTwoVector`
              - A plane normal to a vector at a given point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointBPlane`
              - B-Plane point using the selected target body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointFile`
              - Point specified by data from a file.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointFixedInSystem`
              - Point fixed in a reference coordinate system using the selected coordinate type.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointGrazing`
              - The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointGlint`
              - Point on central body surface that reflects from source to observer.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing`
              - The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointPlaneIntersection`
              - Point on a plane located along a given direction looking from a given origin.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointOnSurface`
              - The detic subpoint of the reference point as projected onto the central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointModelAttach`
              - A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointSatelliteCollectionEntry`
              - A point placed at the center of mass of a specified satellite of the satellite collection.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointPlaneProjection`
              - The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration`
              - Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointCommonTasks`
              - Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointCentBodyIntersect`
              - Point on central body surface along direction vector originating at source point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant`
              - Point fixed relative to reference system based on another point evaluated at specified time instant.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointPlugin`
              - A VGT point plugin.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointCBFixedOffset`
              - Point specified by fixed components with respect to central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemAssembled`
              - A system assembled from an origin point and a set of reference axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface`
              - A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchLLAPosition`
              - A position represented by the Latitude, longtitude and Latitude.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemCommonTasks`
              - Provide methods to create non-persistent VGT coordinate reference frames (systems). Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorAngleRate`
              - Angle rate vector perpendicular to the plane in which the angle is defined.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorApoapsis`
              - Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtEpoch`
              - Based on another vector fixed at a specified epoch.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorAngularVelocity`
              - Angular velocity vector of one set of axes computed with respect to the reference set.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorConing`
              - Vector created by revolving the Reference vector around the About vector with the specified rate.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorCross`
              - The vector cross product of two vectors.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorCustomScript`
              - Customized vector components defined with respect to reference axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorDerivative`
              - A vector derivative of a vector computed with respect to specified axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement`
              - Vector defined by its start and end points.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorTwoPlanesIntersection`
              - Defined along the intersection of two planes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorModelAttach`
              - Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorProjection`
              - A projection of a vector computed with respect to a reference plane.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorScaled`
              - Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorEccentricity`
              - A vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorFixedInAxes`
              - Vector fixed in reference axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorLineOfNodes`
              - Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorOrbitAngularMomentum`
              - Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorOrbitNormal`
              - Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorPeriapsis`
              - Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorReflection`
              - Incident vector reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorRotationVector`
              - Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorDirectionToStar`
              - Defined with respect to a star object. For a star object to be available, you must first create one.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorFixedAtTimeInstant`
              - Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorLinearCombination`
              - Linear combination of two input vectors.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorProjectAlongVector`
              - A projection of a source vector in the direction of another vector.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarLinearCombination`
              - Linear combination of two input vectors using scalars.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled`
              - Scaled version of the input vector using scalar.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorVelocityAcceleration`
              - Velocity vector of a point in a coordinate system.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorPlugin`
              - A VGT vector plugin.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorDispSurface`
              - Displacement between origin and destination points using surface distance and altitude difference.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorFactory`
              - A Factory object to create vectors.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesFactory`
              - A Factory object to create axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemFactory`
              - A Factory class to create VGT systems.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointFactory`
              - A Factory object to create points.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneFactory`
              - A Factory object to create VGT planes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleFactory`
              - A Factory object to create angles.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup`
              - Access or create VGT vectors associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup`
              - Access or create VGT points associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup`
              - Access or create VGT angles associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup`
              - Access or create VGT axes associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup`
              - Represents a VGT Plane component.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup`
              - Access or create VGT systems associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider`
              - Allow accessing existing Vector Geometry Tool components.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchRoot`
              - Represents a VGT root.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolWellKnownEarthSystems`
              - Well-known Earth's coordinate systems.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolWellKnownEarthAxes`
              - Well-known Earth's axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolWellKnownSunSystems`
              - The Sun's well-known coordinate reference systems.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolWellKnownSunAxes`
              - Well-known Sun's axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolWellKnownSystems`
              - Well-known coordinate reference systems.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolWellKnownAxes`
              - Represents well-known VGT Axes.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallAngleFindResult`
              - Represents result returned with IAgCrdnAngle.FindCoordinates method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallAngleFindWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinatesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallAxesTransformResult`
              - Contains the results returned with IAgCrdnAxes.TransformFrom method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallAxesTransformWithRateResult`
              - Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallAxesFindInAxesResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallAxesFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallPlaneFindInAxesResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallPlaneFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallPlaneFindInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystem method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallPlaneFindInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallPointLocateInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallPointLocateInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallSystemTransformResult`
              - Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallSystemTransformWithRateResult`
              - Contains the results returned with IAgCrdnSystem.TransformFromWithRate and IAgCrdnSystem.TransformToWithRate methods.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallSystemFindInSystemResult`
              - Contains the results returned with IAgCrdnSystem.FindInSystem method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallVectorFindInAxesResult`
              - Contains the results returned with IAgCrdnVector.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallVectorFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnVector.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallAngleFindAngleWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindAngleWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchMethodCallAngleFindAngleResult`
              - Contains the results returned with IAgCrdnAngle.FindAngle method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInterval`
              - Represents an interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalCollection`
              - Represents a collection of intervals.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBody`
              - Represents an central body.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyRefTo`
              - Represents a central body reference.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection`
              - A collection of central body names.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchCollection`
              - A collection of VGT objects.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolPointSamplingResult`
              - Contains tabulated positions and velocities of a point created by Sample method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolPointSamplingInterval`
              - The interface represents an interval with the time, position and velocity arrays.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolPointSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, position and velocity arrays.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolAxesSamplingResult`
              - Contains tabulated orientations and angular velocities of axes created by Sample method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolAxesSamplingInterval`
              - The interface represents an interval with the time, orientation and velocity arrays.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolAxesSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, orientation and velocity arrays.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.vgt.CRDN_CALC_SCALAR_TYPE`
              - Define available calculation scalar types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_CONDITION_COMBINED_OPERATION_TYPE`
              - Define scalar condition combined operation types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_CONDITION_SET_TYPE`
              - Define available condition set types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_CONDITION_THRESHOLD_OPTION`
              - Operations for Scalar Bounds Condition.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_CONDITION_TYPE`
              - Define available condition types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_DIMENSION_INHERITANCE`
              - Define how dimension is inherited.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_EVENT_ARRAY_FILTER_TYPE`
              - Event array filter types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_EVENT_ARRAY_TYPE`
              - Define available time array types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_EVENT_INTERVAL_COLLECTION_TYPE`
              - Define available interval collection types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_EVENT_INTERVAL_LIST_TYPE`
              - Define available interval list types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_EVENT_INTERVAL_TYPE`
              - Define available interval types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_EVENT_LIST_MERGE_OPERATION`
              - Define merge operations for interval lists.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_EVENT_TYPE`
              - Define available time instant types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_EXTREMUM_CONSTANTS`
              - These constants are utilized when finding a local or global minimum or maximum, or the threshold crossing.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_FILE_INTERPOLATOR_TYPE`
              - Interpolator types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_INTEGRAL_TYPE`
              - Integral types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_INTEGRATION_WINDOW_TYPE`
              - Define the interval of times during which an integral is evaluated.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_INTERPOLATOR_TYPE`
              - Interpolator types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_INTERVAL_DURATION_KIND`
              - Duration for filtering intervals or gaps from interval lists or time arrays.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_INTERVAL_SELECTION`
              - Select the method to choose an interval from an interval list.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_PARAMETER_SET_TYPE`
              - Define parameter set types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_PRUNE_FILTER`
              - Specify the filter for filtering interval lists or time arrays.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SAMPLED_REFERENCE_TIME`
              - Event array reference type.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SAMPLING_METHOD`
              - Define the Sampling Method.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SATISFACTION_CROSSING`
              - Direction crossing flags.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SAVE_DATA_OPTION`
              - Method for saving computed data.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SIGNAL_PATH_REFERENCE_SYSTEM`
              - Signal path reference system types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SMART_EPOCH_STATE`
              - Smart epoch states.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SMART_INTERVAL_STATE`
              - Smart interval states.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SPEED_OPTIONS`
              - Define various speed options.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_START_STOP_OPTION`
              - Start/stop options.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_THRESH_CONVERGE_SENSE`
              - Specify the desired sense of the results from threshold crossing computations.

            * - :py:class:`~ansys.stk.core.vgt.VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE`
              - Define component directions for a vector.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE`
              - Define volume calc altitude reference types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE`
              - Define volume calc angle off vector reference types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE`
              - Define volume calc range distance types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_RANGE_SPEED_TYPE`
              - Define volume calc range distance types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_TYPE`
              - Define volume calc types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE`
              - Define volume calc spatial condition accumulation types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE`
              - Define volume calc spatial condition duration types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE`
              - Define volume calc spatial condition filter types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE`
              - Define volume calc spatial condition satisfaction metric types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_GRID_TYPE`
              - Define volume grid types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_RESULT_VECTOR_REQUEST`
              - Define volume result vector request types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_TYPE`
              - Define volume grid types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_ABERRATION_TYPE`
              - Define the model of aberration to use.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_CLOCK_HOST_TYPE`
              - Define whether base or target of an Access instance holds the clock for Access times.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_COMBINED_OPERATION_TYPE`
              - Define spatial condition combined operation types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_FROM_GRID_EDGE_TYPE`
              - Define spatial condition from grid edge type.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE`
              - Define spatial condition lighting conditions types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_OVER_TIME_DURATION_TYPE`
              - Define spatial condition over time duration type.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUME_TIME_SENSE_TYPE`
              - Define whether object1 or object2 of an Access instance holds the clock for Access times.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE`
              - Define volumetric grid values method types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_KIND`
              - Represents kinds of vectory geometry components.

            * - :py:class:`~ansys.stk.core.vgt.VECTOR_GEOMETRY_TOOL_ANGLE_TYPE`
              - Represents angle types.

            * - :py:class:`~ansys.stk.core.vgt.VECTOR_GEOMETRY_TOOL_AXES_TYPE`
              - Represents vector types.

            * - :py:class:`~ansys.stk.core.vgt.VECTOR_GEOMETRY_TOOL_PLANE_TYPE`
              - Represents plane types.

            * - :py:class:`~ansys.stk.core.vgt.VECTOR_GEOMETRY_TOOL_POINT_TYPE`
              - Represents point types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SYSTEM_TYPE`
              - Represents system types.

            * - :py:class:`~ansys.stk.core.vgt.VECTOR_GEOMETRY_TOOL_VECTOR_TYPE`
              - Represents vector types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_MEAN_ELEMENT_THEORY`
              - Mean element theory types for approximating motion.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_DIRECTION_TYPE`
              - Direction options.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_LAGRANGE_LIBRATION_POINT_TYPE`
              - Types of the Lagrange points, also known as libration points. Lagrange points are points in space where gravitational forces and the orbital motion of a body balance each other.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_QUADRANT_TYPE`
              - Quadrants from a reference system (e.g., XY, XZ, YZ, YX, ZX, ZY).

            * - :py:class:`~ansys.stk.core.vgt.CRDN_TRAJECTORY_AXES_TYPE`
              - Trajectory axes coordinate types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_DISPLAY_AXIS_SELECTOR`
              - Rotation directions.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SIGNED_ANGLE_TYPE`
              - Define options for computing an angle.

            * - :py:class:`~ansys.stk.core.vgt.VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE`
              - B-Plane point types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_REFERENCE_SHAPE_TYPE`
              - Surface shape types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SURFACE_TYPE`
              - Surface types.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SWEEP_MODE`
              - The rotation sweeping modes.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_SIGNAL_SENSE`
              - Signal sense transmission options.

            * - :py:class:`~ansys.stk.core.vgt.CRDN_INTERSECTION_SURFACE`
              - Intersection surface flags.

            * - :py:class:`~ansys.stk.core.vgt.VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE`
              - Dimension inheritance constants used to configure the dimension inheritance of a vector scaled by a scalar.



Description
-----------

The Vector Geometry (VGT) API enables users define new or utilize existing geometric constructs such as coordinate systems, vectors, points, angles, axes and planes.

The geometric elements can be used to transform between coordinate
systems, compute first and second derivatives, or perform other types of
analysis.


.. py:currentmodule:: ansys.stk.core.vgt


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IVectorGeometryToolPoint<vgt/IVectorGeometryToolPoint>
     IVectorGeometryToolVector<vgt/IVectorGeometryToolVector>
     IVectorGeometryToolSystem<vgt/IVectorGeometryToolSystem>
     IVectorGeometryToolAxes<vgt/IVectorGeometryToolAxes>
     IVectorGeometryToolAngle<vgt/IVectorGeometryToolAngle>
     IVectorGeometryToolPlane<vgt/IVectorGeometryToolPlane>
     IAnalysisWorkbenchContext<vgt/IAnalysisWorkbenchContext>
     IAnalysisWorkbenchComponent<vgt/IAnalysisWorkbenchComponent>
     ICalculationToolScalar<vgt/ICalculationToolScalar>
     ICalculationToolCondition<vgt/ICalculationToolCondition>
     ICalculationToolConditionSet<vgt/ICalculationToolConditionSet>
     IAnalysisWorkbenchConverge<vgt/IAnalysisWorkbenchConverge>
     IAnalysisWorkbenchDerivative<vgt/IAnalysisWorkbenchDerivative>
     ITimeToolEvent<vgt/ITimeToolEvent>
     ITimeToolEventArray<vgt/ITimeToolEventArray>
     ITimeToolEventInterval<vgt/ITimeToolEventInterval>
     ITimeToolEventIntervalCollection<vgt/ITimeToolEventIntervalCollection>
     ITimeToolEventIntervalList<vgt/ITimeToolEventIntervalList>
     IAnalysisWorkbenchIntegral<vgt/IAnalysisWorkbenchIntegral>
     IAnalysisWorkbenchInterp<vgt/IAnalysisWorkbenchInterp>
     ICalculationToolParameterSet<vgt/ICalculationToolParameterSet>
     ITimeToolPruneFilter<vgt/ITimeToolPruneFilter>
     IAnalysisWorkbenchSampling<vgt/IAnalysisWorkbenchSampling>
     ICalculationToolSamplingMethod<vgt/ICalculationToolSamplingMethod>
     IAnalysisWorkbenchSignalDelay<vgt/IAnalysisWorkbenchSignalDelay>
     ISpatialAnalysisToolGridValuesMethod<vgt/ISpatialAnalysisToolGridValuesMethod>
     ISpatialAnalysisToolVolume<vgt/ISpatialAnalysisToolVolume>
     ISpatialAnalysisToolVolumeCalc<vgt/ISpatialAnalysisToolVolumeCalc>
     ISpatialAnalysisToolVolumeGrid<vgt/ISpatialAnalysisToolVolumeGrid>
     ITimeToolTimeProperties<vgt/ITimeToolTimeProperties>
     IAnalysisWorkbenchRefTo<vgt/IAnalysisWorkbenchRefTo>
     IVectorGeometryToolAngleFindAngleResult<vgt/IVectorGeometryToolAngleFindAngleResult>
     IVectorGeometryToolAngleFindAngleWithRateResult<vgt/IVectorGeometryToolAngleFindAngleWithRateResult>
     IVectorGeometryToolAngleFindWithRateResult<vgt/IVectorGeometryToolAngleFindWithRateResult>
     IVectorGeometryToolAngleFindResult<vgt/IVectorGeometryToolAngleFindResult>
     IVectorGeometryToolAxesTransformResult<vgt/IVectorGeometryToolAxesTransformResult>
     IVectorGeometryToolAxesTransformWithRateResult<vgt/IVectorGeometryToolAxesTransformWithRateResult>
     IVectorGeometryToolPlaneFindInAxesResult<vgt/IVectorGeometryToolPlaneFindInAxesResult>
     IVectorGeometryToolPlaneFindInAxesWithRateResult<vgt/IVectorGeometryToolPlaneFindInAxesWithRateResult>
     IVectorGeometryToolPlaneFindInSystemResult<vgt/IVectorGeometryToolPlaneFindInSystemResult>
     IVectorGeometryToolPlaneFindInSystemWithRateResult<vgt/IVectorGeometryToolPlaneFindInSystemWithRateResult>
     IVectorGeometryToolAxesFindInAxesResult<vgt/IVectorGeometryToolAxesFindInAxesResult>
     IVectorGeometryToolAxesFindInAxesWithRateResult<vgt/IVectorGeometryToolAxesFindInAxesWithRateResult>
     IVectorGeometryToolPointLocateInSystemResult<vgt/IVectorGeometryToolPointLocateInSystemResult>
     IVectorGeometryToolPointLocateInSystemWithRateResult<vgt/IVectorGeometryToolPointLocateInSystemWithRateResult>
     IVectorGeometryToolSystemTransformResult<vgt/IVectorGeometryToolSystemTransformResult>
     IVectorGeometryToolSystemTransformWithRateResult<vgt/IVectorGeometryToolSystemTransformWithRateResult>
     IVectorGeometryToolSystemFindInSystemResult<vgt/IVectorGeometryToolSystemFindInSystemResult>
     IVectorGeometryToolVectorFindInAxesResult<vgt/IVectorGeometryToolVectorFindInAxesResult>
     IVectorGeometryToolVectorFindInAxesWithRateResult<vgt/IVectorGeometryToolVectorFindInAxesWithRateResult>
     IAnalysisWorkbenchMethodCallResult<vgt/IAnalysisWorkbenchMethodCallResult>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     CalculationToolEvaluateResult<vgt/CalculationToolEvaluateResult>
     CalculationToolEvaluateWithRateResult<vgt/CalculationToolEvaluateWithRateResult>
     TimeToolEventIntervalResult<vgt/TimeToolEventIntervalResult>
     TimeToolEventFindOccurrenceResult<vgt/TimeToolEventFindOccurrenceResult>
     TimeToolFindTimesResult<vgt/TimeToolFindTimesResult>
     TimeToolIntervalsVectorResult<vgt/TimeToolIntervalsVectorResult>
     TimeToolEventIntervalCollectionOccurredResult<vgt/TimeToolEventIntervalCollectionOccurredResult>
     TimeToolIntervalListResult<vgt/TimeToolIntervalListResult>
     TimeToolIntervalVectorCollection<vgt/TimeToolIntervalVectorCollection>
     TimeToolEventGroup<vgt/TimeToolEventGroup>
     TimeToolEventIntervalGroup<vgt/TimeToolEventIntervalGroup>
     TimeToolEventIntervalListGroup<vgt/TimeToolEventIntervalListGroup>
     TimeToolEventArrayGroup<vgt/TimeToolEventArrayGroup>
     CalculationToolScalarGroup<vgt/CalculationToolScalarGroup>
     TimeToolEventIntervalCollectionGroup<vgt/TimeToolEventIntervalCollectionGroup>
     CalculationToolParameterSetGroup<vgt/CalculationToolParameterSetGroup>
     CalculationToolConditionGroup<vgt/CalculationToolConditionGroup>
     CalculationToolConditionSetGroup<vgt/CalculationToolConditionSetGroup>
     CalculationToolConditionSetEvaluateResult<vgt/CalculationToolConditionSetEvaluateResult>
     CalculationToolConditionSetEvaluateWithRateResult<vgt/CalculationToolConditionSetEvaluateWithRateResult>
     SpatialAnalysisToolVolumeGridGroup<vgt/SpatialAnalysisToolVolumeGridGroup>
     SpatialAnalysisToolVolumeGroup<vgt/SpatialAnalysisToolVolumeGroup>
     SpatialAnalysisToolVolumeCalcGroup<vgt/SpatialAnalysisToolVolumeCalcGroup>
     CalculationToolScalar<vgt/CalculationToolScalar>
     CalculationToolScalarAngle<vgt/CalculationToolScalarAngle>
     CalculationToolScalarAverage<vgt/CalculationToolScalarAverage>
     CalculationToolScalarConstant<vgt/CalculationToolScalarConstant>
     CalculationToolScalarCustom<vgt/CalculationToolScalarCustom>
     CalculationToolScalarCustomInline<vgt/CalculationToolScalarCustomInline>
     CalculationToolScalarDataElement<vgt/CalculationToolScalarDataElement>
     CalculationToolScalarDerivative<vgt/CalculationToolScalarDerivative>
     CalculationToolScalarDotProduct<vgt/CalculationToolScalarDotProduct>
     CalculationToolScalarElapsedTime<vgt/CalculationToolScalarElapsedTime>
     CalculationToolScalarFactory<vgt/CalculationToolScalarFactory>
     CalculationToolScalarFile<vgt/CalculationToolScalarFile>
     CalculationToolScalarFixedAtTimeInstant<vgt/CalculationToolScalarFixedAtTimeInstant>
     CalculationToolScalarFunction<vgt/CalculationToolScalarFunction>
     CalculationToolScalarFunction2Var<vgt/CalculationToolScalarFunction2Var>
     CalculationToolScalarIntegral<vgt/CalculationToolScalarIntegral>
     CalculationToolScalarPlugin<vgt/CalculationToolScalarPlugin>
     CalculationToolScalarPointInVolumeCalc<vgt/CalculationToolScalarPointInVolumeCalc>
     CalculationToolScalarStandardDeviation<vgt/CalculationToolScalarStandardDeviation>
     CalculationToolScalarSurfaceDistanceBetweenPoints<vgt/CalculationToolScalarSurfaceDistanceBetweenPoints>
     CalculationToolScalarVectorComponent<vgt/CalculationToolScalarVectorComponent>
     CalculationToolScalarVectorMagnitude<vgt/CalculationToolScalarVectorMagnitude>
     CalculationToolCondition<vgt/CalculationToolCondition>
     CalculationToolConditionCombined<vgt/CalculationToolConditionCombined>
     CalculationToolConditionFactory<vgt/CalculationToolConditionFactory>
     CalculationToolConditionPointInVolume<vgt/CalculationToolConditionPointInVolume>
     CalculationToolConditionScalarBounds<vgt/CalculationToolConditionScalarBounds>
     CalculationToolConditionSet<vgt/CalculationToolConditionSet>
     CalculationToolConditionSetFactory<vgt/CalculationToolConditionSetFactory>
     CalculationToolConditionSetScalarThresholds<vgt/CalculationToolConditionSetScalarThresholds>
     AnalysisWorkbenchConverge<vgt/AnalysisWorkbenchConverge>
     CalculationToolConvergeBasic<vgt/CalculationToolConvergeBasic>
     AnalysisWorkbenchDerivative<vgt/AnalysisWorkbenchDerivative>
     CalculationToolDerivativeBasic<vgt/CalculationToolDerivativeBasic>
     TimeToolEvent<vgt/TimeToolEvent>
     TimeToolEventArray<vgt/TimeToolEventArray>
     TimeToolEventArrayConditionCrossings<vgt/TimeToolEventArrayConditionCrossings>
     TimeToolEventArrayExtrema<vgt/TimeToolEventArrayExtrema>
     TimeToolEventArrayFactory<vgt/TimeToolEventArrayFactory>
     TimeToolEventArrayFiltered<vgt/TimeToolEventArrayFiltered>
     TimeToolEventArrayFixedStep<vgt/TimeToolEventArrayFixedStep>
     TimeToolEventArrayFixedTimes<vgt/TimeToolEventArrayFixedTimes>
     TimeToolEventArrayMerged<vgt/TimeToolEventArrayMerged>
     TimeToolEventArraySignaled<vgt/TimeToolEventArraySignaled>
     TimeToolEventArrayStartStopTimes<vgt/TimeToolEventArrayStartStopTimes>
     TimeToolEventEpoch<vgt/TimeToolEventEpoch>
     TimeToolEventExtremum<vgt/TimeToolEventExtremum>
     TimeToolEventFactory<vgt/TimeToolEventFactory>
     TimeToolEventInterval<vgt/TimeToolEventInterval>
     TimeToolEventIntervalBetweenTimeInstants<vgt/TimeToolEventIntervalBetweenTimeInstants>
     TimeToolEventIntervalCollection<vgt/TimeToolEventIntervalCollection>
     TimeToolEventIntervalCollectionCondition<vgt/TimeToolEventIntervalCollectionCondition>
     TimeToolEventIntervalCollectionFactory<vgt/TimeToolEventIntervalCollectionFactory>
     TimeToolEventIntervalCollectionLighting<vgt/TimeToolEventIntervalCollectionLighting>
     TimeToolEventIntervalCollectionSignaled<vgt/TimeToolEventIntervalCollectionSignaled>
     TimeToolEventIntervalFactory<vgt/TimeToolEventIntervalFactory>
     TimeToolEventIntervalFixed<vgt/TimeToolEventIntervalFixed>
     TimeToolEventIntervalFixedDuration<vgt/TimeToolEventIntervalFixedDuration>
     TimeToolEventIntervalFromIntervalList<vgt/TimeToolEventIntervalFromIntervalList>
     TimeToolEventIntervalList<vgt/TimeToolEventIntervalList>
     TimeToolEventIntervalListCondition<vgt/TimeToolEventIntervalListCondition>
     TimeToolEventIntervalListFactory<vgt/TimeToolEventIntervalListFactory>
     TimeToolEventIntervalListFile<vgt/TimeToolEventIntervalListFile>
     TimeToolEventIntervalListFiltered<vgt/TimeToolEventIntervalListFiltered>
     TimeToolEventIntervalListFixed<vgt/TimeToolEventIntervalListFixed>
     TimeToolEventIntervalListMerged<vgt/TimeToolEventIntervalListMerged>
     TimeToolEventIntervalListScaled<vgt/TimeToolEventIntervalListScaled>
     TimeToolEventIntervalListSignaled<vgt/TimeToolEventIntervalListSignaled>
     TimeToolEventIntervalListTimeOffset<vgt/TimeToolEventIntervalListTimeOffset>
     TimeToolEventIntervalScaled<vgt/TimeToolEventIntervalScaled>
     TimeToolEventIntervalSignaled<vgt/TimeToolEventIntervalSignaled>
     TimeToolEventIntervalSmartInterval<vgt/TimeToolEventIntervalSmartInterval>
     TimeToolEventIntervalTimeOffset<vgt/TimeToolEventIntervalTimeOffset>
     TimeToolEventSignaled<vgt/TimeToolEventSignaled>
     TimeToolEventSmartEpoch<vgt/TimeToolEventSmartEpoch>
     TimeToolEventStartStopTime<vgt/TimeToolEventStartStopTime>
     TimeToolEventTimeOffset<vgt/TimeToolEventTimeOffset>
     TimeToolFirstIntervalsFilter<vgt/TimeToolFirstIntervalsFilter>
     TimeToolGapsFilter<vgt/TimeToolGapsFilter>
     AnalysisWorkbenchIntegral<vgt/AnalysisWorkbenchIntegral>
     CalculationToolIntegralBasic<vgt/CalculationToolIntegralBasic>
     AnalysisWorkbenchInterp<vgt/AnalysisWorkbenchInterp>
     CalculationToolInterpBasic<vgt/CalculationToolInterpBasic>
     TimeToolIntervalsFilter<vgt/TimeToolIntervalsFilter>
     TimeToolLastIntervalsFilter<vgt/TimeToolLastIntervalsFilter>
     CalculationToolParameterSet<vgt/CalculationToolParameterSet>
     CalculationToolParameterSetAttitude<vgt/CalculationToolParameterSetAttitude>
     CalculationToolParameterSetFactory<vgt/CalculationToolParameterSetFactory>
     CalculationToolParameterSetGroundTrajectory<vgt/CalculationToolParameterSetGroundTrajectory>
     CalculationToolParameterSetOrbit<vgt/CalculationToolParameterSetOrbit>
     CalculationToolParameterSetTrajectory<vgt/CalculationToolParameterSetTrajectory>
     CalculationToolParameterSetVector<vgt/CalculationToolParameterSetVector>
     TimeToolPruneFilter<vgt/TimeToolPruneFilter>
     TimeToolPruneFilterFactory<vgt/TimeToolPruneFilterFactory>
     TimeToolRelativeSatisfactionConditionFilter<vgt/TimeToolRelativeSatisfactionConditionFilter>
     AnalysisWorkbenchSampling<vgt/AnalysisWorkbenchSampling>
     CalculationToolSamplingBasic<vgt/CalculationToolSamplingBasic>
     CalculationToolSamplingCurvatureTolerance<vgt/CalculationToolSamplingCurvatureTolerance>
     CalculationToolSamplingFixedStep<vgt/CalculationToolSamplingFixedStep>
     CalculationToolSamplingMethod<vgt/CalculationToolSamplingMethod>
     CalculationToolSamplingMethodFactory<vgt/CalculationToolSamplingMethodFactory>
     CalculationToolSamplingRelativeTolerance<vgt/CalculationToolSamplingRelativeTolerance>
     TimeToolSatisfactionConditionFilter<vgt/TimeToolSatisfactionConditionFilter>
     AnalysisWorkbenchSignalDelay<vgt/AnalysisWorkbenchSignalDelay>
     TimeToolSignalDelayBasic<vgt/TimeToolSignalDelayBasic>
     SpatialAnalysisToolVolumeCalcFactory<vgt/SpatialAnalysisToolVolumeCalcFactory>
     SpatialAnalysisToolVolumeFactory<vgt/SpatialAnalysisToolVolumeFactory>
     SpatialAnalysisToolVolumeGridFactory<vgt/SpatialAnalysisToolVolumeGridFactory>
     SpatialAnalysisToolGridCoordinateDefinition<vgt/SpatialAnalysisToolGridCoordinateDefinition>
     SpatialAnalysisToolGridValuesCustom<vgt/SpatialAnalysisToolGridValuesCustom>
     SpatialAnalysisToolGridValuesFixedNumberOfSteps<vgt/SpatialAnalysisToolGridValuesFixedNumberOfSteps>
     SpatialAnalysisToolGridValuesFixedStep<vgt/SpatialAnalysisToolGridValuesFixedStep>
     SpatialAnalysisToolGridValuesMethod<vgt/SpatialAnalysisToolGridValuesMethod>
     TimeToolLightTimeDelay<vgt/TimeToolLightTimeDelay>
     SpatialAnalysisToolVolume<vgt/SpatialAnalysisToolVolume>
     SpatialAnalysisToolVolumeCalc<vgt/SpatialAnalysisToolVolumeCalc>
     SpatialAnalysisToolVolumeCalcAltitude<vgt/SpatialAnalysisToolVolumeCalcAltitude>
     SpatialAnalysisToolVolumeCalcAngleOffVector<vgt/SpatialAnalysisToolVolumeCalcAngleOffVector>
     SpatialAnalysisToolVolumeCalcConditionSatMetric<vgt/SpatialAnalysisToolVolumeCalcConditionSatMetric>
     SpatialAnalysisToolVolumeCalcDelayRange<vgt/SpatialAnalysisToolVolumeCalcDelayRange>
     SpatialAnalysisToolVolumeCalcFile<vgt/SpatialAnalysisToolVolumeCalcFile>
     SpatialAnalysisToolVolumeCalcFromScalar<vgt/SpatialAnalysisToolVolumeCalcFromScalar>
     SpatialAnalysisToolVolumeCalcRange<vgt/SpatialAnalysisToolVolumeCalcRange>
     SpatialAnalysisToolVolumeCalcSolarIntensity<vgt/SpatialAnalysisToolVolumeCalcSolarIntensity>
     SpatialAnalysisToolVolumeCombined<vgt/SpatialAnalysisToolVolumeCombined>
     SpatialAnalysisToolVolumeFromCalc<vgt/SpatialAnalysisToolVolumeFromCalc>
     SpatialAnalysisToolVolumeFromCondition<vgt/SpatialAnalysisToolVolumeFromCondition>
     SpatialAnalysisToolVolumeFromGrid<vgt/SpatialAnalysisToolVolumeFromGrid>
     SpatialAnalysisToolVolumeFromTimeSatisfaction<vgt/SpatialAnalysisToolVolumeFromTimeSatisfaction>
     SpatialAnalysisToolVolumeGrid<vgt/SpatialAnalysisToolVolumeGrid>
     SpatialAnalysisToolVolumeGridBearingAlt<vgt/SpatialAnalysisToolVolumeGridBearingAlt>
     SpatialAnalysisToolVolumeGridCartesian<vgt/SpatialAnalysisToolVolumeGridCartesian>
     SpatialAnalysisToolVolumeGridConstrained<vgt/SpatialAnalysisToolVolumeGridConstrained>
     SpatialAnalysisToolVolumeGridCylindrical<vgt/SpatialAnalysisToolVolumeGridCylindrical>
     SpatialAnalysisToolVolumeGridLatLonAlt<vgt/SpatialAnalysisToolVolumeGridLatLonAlt>
     SpatialAnalysisToolVolumeGridResult<vgt/SpatialAnalysisToolVolumeGridResult>
     SpatialAnalysisToolVolumeGridSpherical<vgt/SpatialAnalysisToolVolumeGridSpherical>
     SpatialAnalysisToolVolumeInview<vgt/SpatialAnalysisToolVolumeInview>
     SpatialAnalysisToolVolumeLighting<vgt/SpatialAnalysisToolVolumeLighting>
     SpatialAnalysisToolVolumeOverTime<vgt/SpatialAnalysisToolVolumeOverTime>
     AnalysisWorkbenchGeneric<vgt/AnalysisWorkbenchGeneric>
     AnalysisWorkbenchTypeInfo<vgt/AnalysisWorkbenchTypeInfo>
     AnalysisWorkbenchInstance<vgt/AnalysisWorkbenchInstance>
     AnalysisWorkbenchTemplate<vgt/AnalysisWorkbenchTemplate>
     VectorGeometryToolPointRefTo<vgt/VectorGeometryToolPointRefTo>
     VectorGeometryToolVectorRefTo<vgt/VectorGeometryToolVectorRefTo>
     VectorGeometryToolAxesRefTo<vgt/VectorGeometryToolAxesRefTo>
     VectorGeometryToolAngleRefTo<vgt/VectorGeometryToolAngleRefTo>
     VectorGeometryToolSystemRefTo<vgt/VectorGeometryToolSystemRefTo>
     VectorGeometryToolPlaneRefTo<vgt/VectorGeometryToolPlaneRefTo>
     VectorGeometryToolVector<vgt/VectorGeometryToolVector>
     VectorGeometryToolAxesLabels<vgt/VectorGeometryToolAxesLabels>
     VectorGeometryToolAxes<vgt/VectorGeometryToolAxes>
     VectorGeometryToolPoint<vgt/VectorGeometryToolPoint>
     VectorGeometryToolSystem<vgt/VectorGeometryToolSystem>
     VectorGeometryToolAngle<vgt/VectorGeometryToolAngle>
     VectorGeometryToolPlaneLabels<vgt/VectorGeometryToolPlaneLabels>
     VectorGeometryToolPlane<vgt/VectorGeometryToolPlane>
     VectorGeometryToolAxesAlignedAndConstrained<vgt/VectorGeometryToolAxesAlignedAndConstrained>
     VectorGeometryToolAxesAngularOffset<vgt/VectorGeometryToolAxesAngularOffset>
     VectorGeometryToolAxesFixedAtEpoch<vgt/VectorGeometryToolAxesFixedAtEpoch>
     VectorGeometryToolAxesBPlane<vgt/VectorGeometryToolAxesBPlane>
     VectorGeometryToolAxesCustomScript<vgt/VectorGeometryToolAxesCustomScript>
     VectorGeometryToolAxesAttitudeFile<vgt/VectorGeometryToolAxesAttitudeFile>
     VectorGeometryToolAxesFixed<vgt/VectorGeometryToolAxesFixed>
     VectorGeometryToolAxesModelAttach<vgt/VectorGeometryToolAxesModelAttach>
     VectorGeometryToolAxesSpinning<vgt/VectorGeometryToolAxesSpinning>
     VectorGeometryToolAxesOnSurface<vgt/VectorGeometryToolAxesOnSurface>
     VectorGeometryToolAxesTrajectory<vgt/VectorGeometryToolAxesTrajectory>
     VectorGeometryToolAxesLagrangeLibration<vgt/VectorGeometryToolAxesLagrangeLibration>
     VectorGeometryToolAxesCommonTasks<vgt/VectorGeometryToolAxesCommonTasks>
     VectorGeometryToolAxesAtTimeInstant<vgt/VectorGeometryToolAxesAtTimeInstant>
     VectorGeometryToolAxesPlugin<vgt/VectorGeometryToolAxesPlugin>
     VectorGeometryToolAngleBetweenVectors<vgt/VectorGeometryToolAngleBetweenVectors>
     VectorGeometryToolAngleBetweenPlanes<vgt/VectorGeometryToolAngleBetweenPlanes>
     VectorGeometryToolAngleDihedral<vgt/VectorGeometryToolAngleDihedral>
     VectorGeometryToolAngleRotation<vgt/VectorGeometryToolAngleRotation>
     VectorGeometryToolAngleToPlane<vgt/VectorGeometryToolAngleToPlane>
     VectorGeometryToolPlaneNormal<vgt/VectorGeometryToolPlaneNormal>
     VectorGeometryToolPlaneQuadrant<vgt/VectorGeometryToolPlaneQuadrant>
     VectorGeometryToolPlaneTrajectory<vgt/VectorGeometryToolPlaneTrajectory>
     VectorGeometryToolPlaneTriad<vgt/VectorGeometryToolPlaneTriad>
     VectorGeometryToolPlaneTwoVector<vgt/VectorGeometryToolPlaneTwoVector>
     VectorGeometryToolPointBPlane<vgt/VectorGeometryToolPointBPlane>
     VectorGeometryToolPointFile<vgt/VectorGeometryToolPointFile>
     VectorGeometryToolPointFixedInSystem<vgt/VectorGeometryToolPointFixedInSystem>
     VectorGeometryToolPointGrazing<vgt/VectorGeometryToolPointGrazing>
     VectorGeometryToolPointGlint<vgt/VectorGeometryToolPointGlint>
     VectorGeometryToolPointCovarianceGrazing<vgt/VectorGeometryToolPointCovarianceGrazing>
     VectorGeometryToolPointPlaneIntersection<vgt/VectorGeometryToolPointPlaneIntersection>
     VectorGeometryToolPointOnSurface<vgt/VectorGeometryToolPointOnSurface>
     VectorGeometryToolPointModelAttach<vgt/VectorGeometryToolPointModelAttach>
     VectorGeometryToolPointSatelliteCollectionEntry<vgt/VectorGeometryToolPointSatelliteCollectionEntry>
     VectorGeometryToolPointPlaneProjection<vgt/VectorGeometryToolPointPlaneProjection>
     VectorGeometryToolPointLagrangeLibration<vgt/VectorGeometryToolPointLagrangeLibration>
     VectorGeometryToolPointCommonTasks<vgt/VectorGeometryToolPointCommonTasks>
     VectorGeometryToolPointCentBodyIntersect<vgt/VectorGeometryToolPointCentBodyIntersect>
     VectorGeometryToolPointAtTimeInstant<vgt/VectorGeometryToolPointAtTimeInstant>
     VectorGeometryToolPointPlugin<vgt/VectorGeometryToolPointPlugin>
     VectorGeometryToolPointCBFixedOffset<vgt/VectorGeometryToolPointCBFixedOffset>
     VectorGeometryToolSystemAssembled<vgt/VectorGeometryToolSystemAssembled>
     VectorGeometryToolSystemOnSurface<vgt/VectorGeometryToolSystemOnSurface>
     AnalysisWorkbenchLLAPosition<vgt/AnalysisWorkbenchLLAPosition>
     VectorGeometryToolSystemCommonTasks<vgt/VectorGeometryToolSystemCommonTasks>
     VectorGeometryToolVectorAngleRate<vgt/VectorGeometryToolVectorAngleRate>
     VectorGeometryToolVectorApoapsis<vgt/VectorGeometryToolVectorApoapsis>
     VectorGeometryToolVectorFixedAtEpoch<vgt/VectorGeometryToolVectorFixedAtEpoch>
     VectorGeometryToolVectorAngularVelocity<vgt/VectorGeometryToolVectorAngularVelocity>
     VectorGeometryToolVectorConing<vgt/VectorGeometryToolVectorConing>
     VectorGeometryToolVectorCross<vgt/VectorGeometryToolVectorCross>
     VectorGeometryToolVectorCustomScript<vgt/VectorGeometryToolVectorCustomScript>
     VectorGeometryToolVectorDerivative<vgt/VectorGeometryToolVectorDerivative>
     VectorGeometryToolVectorDisplacement<vgt/VectorGeometryToolVectorDisplacement>
     VectorGeometryToolVectorTwoPlanesIntersection<vgt/VectorGeometryToolVectorTwoPlanesIntersection>
     VectorGeometryToolVectorModelAttach<vgt/VectorGeometryToolVectorModelAttach>
     VectorGeometryToolVectorProjection<vgt/VectorGeometryToolVectorProjection>
     VectorGeometryToolVectorScaled<vgt/VectorGeometryToolVectorScaled>
     VectorGeometryToolVectorEccentricity<vgt/VectorGeometryToolVectorEccentricity>
     VectorGeometryToolVectorFixedInAxes<vgt/VectorGeometryToolVectorFixedInAxes>
     VectorGeometryToolVectorLineOfNodes<vgt/VectorGeometryToolVectorLineOfNodes>
     VectorGeometryToolVectorOrbitAngularMomentum<vgt/VectorGeometryToolVectorOrbitAngularMomentum>
     VectorGeometryToolVectorOrbitNormal<vgt/VectorGeometryToolVectorOrbitNormal>
     VectorGeometryToolVectorPeriapsis<vgt/VectorGeometryToolVectorPeriapsis>
     VectorGeometryToolVectorReflection<vgt/VectorGeometryToolVectorReflection>
     VectorGeometryToolVectorRotationVector<vgt/VectorGeometryToolVectorRotationVector>
     VectorGeometryToolVectorDirectionToStar<vgt/VectorGeometryToolVectorDirectionToStar>
     VectorGeometryToolVectorFixedAtTimeInstant<vgt/VectorGeometryToolVectorFixedAtTimeInstant>
     VectorGeometryToolVectorLinearCombination<vgt/VectorGeometryToolVectorLinearCombination>
     VectorGeometryToolVectorProjectAlongVector<vgt/VectorGeometryToolVectorProjectAlongVector>
     VectorGeometryToolVectorScalarLinearCombination<vgt/VectorGeometryToolVectorScalarLinearCombination>
     VectorGeometryToolVectorScalarScaled<vgt/VectorGeometryToolVectorScalarScaled>
     VectorGeometryToolVectorVelocityAcceleration<vgt/VectorGeometryToolVectorVelocityAcceleration>
     VectorGeometryToolVectorPlugin<vgt/VectorGeometryToolVectorPlugin>
     VectorGeometryToolVectorDispSurface<vgt/VectorGeometryToolVectorDispSurface>
     VectorGeometryToolVectorFactory<vgt/VectorGeometryToolVectorFactory>
     VectorGeometryToolAxesFactory<vgt/VectorGeometryToolAxesFactory>
     VectorGeometryToolSystemFactory<vgt/VectorGeometryToolSystemFactory>
     VectorGeometryToolPointFactory<vgt/VectorGeometryToolPointFactory>
     VectorGeometryToolPlaneFactory<vgt/VectorGeometryToolPlaneFactory>
     VectorGeometryToolAngleFactory<vgt/VectorGeometryToolAngleFactory>
     VectorGeometryToolVectorGroup<vgt/VectorGeometryToolVectorGroup>
     VectorGeometryToolPointGroup<vgt/VectorGeometryToolPointGroup>
     VectorGeometryToolAngleGroup<vgt/VectorGeometryToolAngleGroup>
     VectorGeometryToolAxesGroup<vgt/VectorGeometryToolAxesGroup>
     VectorGeometryToolPlaneGroup<vgt/VectorGeometryToolPlaneGroup>
     VectorGeometryToolSystemGroup<vgt/VectorGeometryToolSystemGroup>
     AnalysisWorkbenchProvider<vgt/AnalysisWorkbenchProvider>
     AnalysisWorkbenchRoot<vgt/AnalysisWorkbenchRoot>
     VectorGeometryToolWellKnownEarthSystems<vgt/VectorGeometryToolWellKnownEarthSystems>
     VectorGeometryToolWellKnownEarthAxes<vgt/VectorGeometryToolWellKnownEarthAxes>
     VectorGeometryToolWellKnownSunSystems<vgt/VectorGeometryToolWellKnownSunSystems>
     VectorGeometryToolWellKnownSunAxes<vgt/VectorGeometryToolWellKnownSunAxes>
     VectorGeometryToolWellKnownSystems<vgt/VectorGeometryToolWellKnownSystems>
     VectorGeometryToolWellKnownAxes<vgt/VectorGeometryToolWellKnownAxes>
     AnalysisWorkbenchMethodCallAngleFindResult<vgt/AnalysisWorkbenchMethodCallAngleFindResult>
     AnalysisWorkbenchMethodCallAngleFindWithRateResult<vgt/AnalysisWorkbenchMethodCallAngleFindWithRateResult>
     AnalysisWorkbenchMethodCallAxesTransformResult<vgt/AnalysisWorkbenchMethodCallAxesTransformResult>
     AnalysisWorkbenchMethodCallAxesTransformWithRateResult<vgt/AnalysisWorkbenchMethodCallAxesTransformWithRateResult>
     AnalysisWorkbenchMethodCallAxesFindInAxesResult<vgt/AnalysisWorkbenchMethodCallAxesFindInAxesResult>
     AnalysisWorkbenchMethodCallAxesFindInAxesWithRateResult<vgt/AnalysisWorkbenchMethodCallAxesFindInAxesWithRateResult>
     AnalysisWorkbenchMethodCallPlaneFindInAxesResult<vgt/AnalysisWorkbenchMethodCallPlaneFindInAxesResult>
     AnalysisWorkbenchMethodCallPlaneFindInAxesWithRateResult<vgt/AnalysisWorkbenchMethodCallPlaneFindInAxesWithRateResult>
     AnalysisWorkbenchMethodCallPlaneFindInSystemResult<vgt/AnalysisWorkbenchMethodCallPlaneFindInSystemResult>
     AnalysisWorkbenchMethodCallPlaneFindInSystemWithRateResult<vgt/AnalysisWorkbenchMethodCallPlaneFindInSystemWithRateResult>
     AnalysisWorkbenchMethodCallPointLocateInSystemResult<vgt/AnalysisWorkbenchMethodCallPointLocateInSystemResult>
     AnalysisWorkbenchMethodCallPointLocateInSystemWithRateResult<vgt/AnalysisWorkbenchMethodCallPointLocateInSystemWithRateResult>
     AnalysisWorkbenchMethodCallSystemTransformResult<vgt/AnalysisWorkbenchMethodCallSystemTransformResult>
     AnalysisWorkbenchMethodCallSystemTransformWithRateResult<vgt/AnalysisWorkbenchMethodCallSystemTransformWithRateResult>
     AnalysisWorkbenchMethodCallSystemFindInSystemResult<vgt/AnalysisWorkbenchMethodCallSystemFindInSystemResult>
     AnalysisWorkbenchMethodCallVectorFindInAxesResult<vgt/AnalysisWorkbenchMethodCallVectorFindInAxesResult>
     AnalysisWorkbenchMethodCallVectorFindInAxesWithRateResult<vgt/AnalysisWorkbenchMethodCallVectorFindInAxesWithRateResult>
     AnalysisWorkbenchMethodCallAngleFindAngleWithRateResult<vgt/AnalysisWorkbenchMethodCallAngleFindAngleWithRateResult>
     AnalysisWorkbenchMethodCallAngleFindAngleResult<vgt/AnalysisWorkbenchMethodCallAngleFindAngleResult>
     TimeToolInterval<vgt/TimeToolInterval>
     TimeToolIntervalCollection<vgt/TimeToolIntervalCollection>
     AnalysisWorkbenchCentralBody<vgt/AnalysisWorkbenchCentralBody>
     AnalysisWorkbenchCentralBodyRefTo<vgt/AnalysisWorkbenchCentralBodyRefTo>
     AnalysisWorkbenchCentralBodyCollection<vgt/AnalysisWorkbenchCentralBodyCollection>
     AnalysisWorkbenchCollection<vgt/AnalysisWorkbenchCollection>
     TimeToolPointSamplingResult<vgt/TimeToolPointSamplingResult>
     TimeToolPointSamplingInterval<vgt/TimeToolPointSamplingInterval>
     TimeToolPointSamplingIntervalCollection<vgt/TimeToolPointSamplingIntervalCollection>
     TimeToolAxesSamplingResult<vgt/TimeToolAxesSamplingResult>
     TimeToolAxesSamplingInterval<vgt/TimeToolAxesSamplingInterval>
     TimeToolAxesSamplingIntervalCollection<vgt/TimeToolAxesSamplingIntervalCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ CRDN_CALC_SCALAR_TYPE<vgt/CRDN_CALC_SCALAR_TYPE_enum>
    ≔ CRDN_CONDITION_COMBINED_OPERATION_TYPE<vgt/CRDN_CONDITION_COMBINED_OPERATION_TYPE_enum>
    ≔ CRDN_CONDITION_SET_TYPE<vgt/CRDN_CONDITION_SET_TYPE_enum>
    ≔ CRDN_CONDITION_THRESHOLD_OPTION<vgt/CRDN_CONDITION_THRESHOLD_OPTION_enum>
    ≔ CRDN_CONDITION_TYPE<vgt/CRDN_CONDITION_TYPE_enum>
    ≔ CRDN_DIMENSION_INHERITANCE<vgt/CRDN_DIMENSION_INHERITANCE_enum>
    ≔ CRDN_EVENT_ARRAY_FILTER_TYPE<vgt/CRDN_EVENT_ARRAY_FILTER_TYPE_enum>
    ≔ CRDN_EVENT_ARRAY_TYPE<vgt/CRDN_EVENT_ARRAY_TYPE_enum>
    ≔ CRDN_EVENT_INTERVAL_COLLECTION_TYPE<vgt/CRDN_EVENT_INTERVAL_COLLECTION_TYPE_enum>
    ≔ CRDN_EVENT_INTERVAL_LIST_TYPE<vgt/CRDN_EVENT_INTERVAL_LIST_TYPE_enum>
    ≔ CRDN_EVENT_INTERVAL_TYPE<vgt/CRDN_EVENT_INTERVAL_TYPE_enum>
    ≔ CRDN_EVENT_LIST_MERGE_OPERATION<vgt/CRDN_EVENT_LIST_MERGE_OPERATION_enum>
    ≔ CRDN_EVENT_TYPE<vgt/CRDN_EVENT_TYPE_enum>
    ≔ CRDN_EXTREMUM_CONSTANTS<vgt/CRDN_EXTREMUM_CONSTANTS_enum>
    ≔ CRDN_FILE_INTERPOLATOR_TYPE<vgt/CRDN_FILE_INTERPOLATOR_TYPE_enum>
    ≔ CRDN_INTEGRAL_TYPE<vgt/CRDN_INTEGRAL_TYPE_enum>
    ≔ CRDN_INTEGRATION_WINDOW_TYPE<vgt/CRDN_INTEGRATION_WINDOW_TYPE_enum>
    ≔ CRDN_INTERPOLATOR_TYPE<vgt/CRDN_INTERPOLATOR_TYPE_enum>
    ≔ CRDN_INTERVAL_DURATION_KIND<vgt/CRDN_INTERVAL_DURATION_KIND_enum>
    ≔ CRDN_INTERVAL_SELECTION<vgt/CRDN_INTERVAL_SELECTION_enum>
    ≔ CRDN_PARAMETER_SET_TYPE<vgt/CRDN_PARAMETER_SET_TYPE_enum>
    ≔ CRDN_PRUNE_FILTER<vgt/CRDN_PRUNE_FILTER_enum>
    ≔ CRDN_SAMPLED_REFERENCE_TIME<vgt/CRDN_SAMPLED_REFERENCE_TIME_enum>
    ≔ CRDN_SAMPLING_METHOD<vgt/CRDN_SAMPLING_METHOD_enum>
    ≔ CRDN_SATISFACTION_CROSSING<vgt/CRDN_SATISFACTION_CROSSING_enum>
    ≔ CRDN_SAVE_DATA_OPTION<vgt/CRDN_SAVE_DATA_OPTION_enum>
    ≔ CRDN_SIGNAL_PATH_REFERENCE_SYSTEM<vgt/CRDN_SIGNAL_PATH_REFERENCE_SYSTEM_enum>
    ≔ CRDN_SMART_EPOCH_STATE<vgt/CRDN_SMART_EPOCH_STATE_enum>
    ≔ CRDN_SMART_INTERVAL_STATE<vgt/CRDN_SMART_INTERVAL_STATE_enum>
    ≔ CRDN_SPEED_OPTIONS<vgt/CRDN_SPEED_OPTIONS_enum>
    ≔ CRDN_START_STOP_OPTION<vgt/CRDN_START_STOP_OPTION_enum>
    ≔ CRDN_THRESH_CONVERGE_SENSE<vgt/CRDN_THRESH_CONVERGE_SENSE_enum>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE<vgt/VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE<vgt/CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE<vgt/CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE<vgt/CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_RANGE_SPEED_TYPE<vgt/CRDN_VOLUME_CALC_RANGE_SPEED_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_TYPE<vgt/CRDN_VOLUME_CALC_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE<vgt/CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE<vgt/CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE<vgt/CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE_enum>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE<vgt/CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE_enum>
    ≔ CRDN_VOLUME_GRID_TYPE<vgt/CRDN_VOLUME_GRID_TYPE_enum>
    ≔ CRDN_VOLUME_RESULT_VECTOR_REQUEST<vgt/CRDN_VOLUME_RESULT_VECTOR_REQUEST_enum>
    ≔ CRDN_VOLUME_TYPE<vgt/CRDN_VOLUME_TYPE_enum>
    ≔ CRDN_VOLUME_ABERRATION_TYPE<vgt/CRDN_VOLUME_ABERRATION_TYPE_enum>
    ≔ CRDN_VOLUME_CLOCK_HOST_TYPE<vgt/CRDN_VOLUME_CLOCK_HOST_TYPE_enum>
    ≔ CRDN_VOLUME_COMBINED_OPERATION_TYPE<vgt/CRDN_VOLUME_COMBINED_OPERATION_TYPE_enum>
    ≔ CRDN_VOLUME_FROM_GRID_EDGE_TYPE<vgt/CRDN_VOLUME_FROM_GRID_EDGE_TYPE_enum>
    ≔ CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE<vgt/CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE_enum>
    ≔ CRDN_VOLUME_OVER_TIME_DURATION_TYPE<vgt/CRDN_VOLUME_OVER_TIME_DURATION_TYPE_enum>
    ≔ CRDN_VOLUME_TIME_SENSE_TYPE<vgt/CRDN_VOLUME_TIME_SENSE_TYPE_enum>
    ≔ CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE<vgt/CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE_enum>
    ≔ CRDN_KIND<vgt/CRDN_KIND_enum>
    ≔ VECTOR_GEOMETRY_TOOL_ANGLE_TYPE<vgt/VECTOR_GEOMETRY_TOOL_ANGLE_TYPE_enum>
    ≔ VECTOR_GEOMETRY_TOOL_AXES_TYPE<vgt/VECTOR_GEOMETRY_TOOL_AXES_TYPE_enum>
    ≔ VECTOR_GEOMETRY_TOOL_PLANE_TYPE<vgt/VECTOR_GEOMETRY_TOOL_PLANE_TYPE_enum>
    ≔ VECTOR_GEOMETRY_TOOL_POINT_TYPE<vgt/VECTOR_GEOMETRY_TOOL_POINT_TYPE_enum>
    ≔ CRDN_SYSTEM_TYPE<vgt/CRDN_SYSTEM_TYPE_enum>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_TYPE<vgt/VECTOR_GEOMETRY_TOOL_VECTOR_TYPE_enum>
    ≔ CRDN_MEAN_ELEMENT_THEORY<vgt/CRDN_MEAN_ELEMENT_THEORY_enum>
    ≔ CRDN_DIRECTION_TYPE<vgt/CRDN_DIRECTION_TYPE_enum>
    ≔ CRDN_LAGRANGE_LIBRATION_POINT_TYPE<vgt/CRDN_LAGRANGE_LIBRATION_POINT_TYPE_enum>
    ≔ CRDN_QUADRANT_TYPE<vgt/CRDN_QUADRANT_TYPE_enum>
    ≔ CRDN_TRAJECTORY_AXES_TYPE<vgt/CRDN_TRAJECTORY_AXES_TYPE_enum>
    ≔ CRDN_DISPLAY_AXIS_SELECTOR<vgt/CRDN_DISPLAY_AXIS_SELECTOR_enum>
    ≔ CRDN_SIGNED_ANGLE_TYPE<vgt/CRDN_SIGNED_ANGLE_TYPE_enum>
    ≔ VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE<vgt/VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE_enum>
    ≔ CRDN_REFERENCE_SHAPE_TYPE<vgt/CRDN_REFERENCE_SHAPE_TYPE_enum>
    ≔ CRDN_SURFACE_TYPE<vgt/CRDN_SURFACE_TYPE_enum>
    ≔ CRDN_SWEEP_MODE<vgt/CRDN_SWEEP_MODE_enum>
    ≔ CRDN_SIGNAL_SENSE<vgt/CRDN_SIGNAL_SENSE_enum>
    ≔ CRDN_INTERSECTION_SURFACE<vgt/CRDN_INTERSECTION_SURFACE_enum>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE<vgt/VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE_enum>

