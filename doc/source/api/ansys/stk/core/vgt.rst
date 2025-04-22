
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

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentContext`
              - The interface represents a context associated with a VGT component. All VGT components are associated with a valid context. A context can represent a VGT instance or a VGT template.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`
              - A base interface implemented by all VGT components. The methods and properties of the interface provide type information about the VGT component.

            * - :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :py:class:`~ansys.stk.core.vgt.ICalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :py:class:`~ansys.stk.core.vgt.ICalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchConvergence`
              - Represents a base class for convergence definitions.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolInstant`
              - Define an event (time instant).

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolTimeArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolTimeInterval`
              - A single time interval.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalCollection`
              - A collection of related interval lists.

            * - :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalList`
              - An ordered list of time intervals.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchInterpolator`
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

            * - :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolSpatialCalculation`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`
              - Define methods to compute time properties such as availability and special times.

            * - :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentReference`
              - A base interface for all VGT component references.

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

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalResult`
              - Contains the results returned with ITimeToolTimeIntervalList.FindIntervals method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantOccurrenceResult`
              - Contains the results returned with ITimeToolInstant.FindOccurrence method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayFindTimesResult`
              - Return a collection of intervals and an array of times.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalsVectorResult`
              - Contains the results returned with ITimeToolTimeIntervalCollection.FindIntervalCollection method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionOccurredResult`
              - Contains the results returned with ITimeToolTimeIntervalCollection.Occurred method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalListResult`
              - Contains the results returned with ITimeToolTimeIntervalList.FindIntervals method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalVectorCollection`
              - A collection of interval collections.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantGroup`
              - Access or create VGT events associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup`
              - Access or create VGT event intervals associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListGroup`
              - Access or create VGT event interval lists associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayGroup`
              - Access or create VGT event arrays associated with an object.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarGroup`
              - Access or create VGT calculation scalars associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionGroup`
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

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup`
              - Access or create spatial conditions associated with a volume grid.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationGroup`
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

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarCustomInlineScript`
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

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarFunctionOf2Variables`
              - Defined by performing a function(x,y) on two scalar arguments.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarIntegral`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarPlugin`
              - Use a scalar calculation plugin.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolScalarAlongTrajectory`
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

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionTrajectoryWithinVolume`
              - Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionScalarBounds`
              - Defined by determining if input scalar is within specified bounds; returns +1 if satisfied, -1 if not satisfied and 0 if on boundary.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSetFactory`
              - The factory creates condition set components.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConditionSetScalarThresholds`
              - Condition set based on single scalar calculation compared to set of threshold values.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchConvergence`
              - Represents a base class for convergence definitions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolConvergeBasic`
              - Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolDerivativeBasic`
              - Derivative definition determines how numerical differencing is used to compute derivatives.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstant`
              - Define an event (time instant).

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayConditionCrossings`
              - Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayExtrema`
              - Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayFactory`
              - The factory creates event arrays.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayFiltered`
              - Defined by filtering times from original time array according to specified filtering method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayFixedStep`
              - Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayFixedTimes`
              - Array defined by time ordered instants each explicitly specified.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayMerged`
              - Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArraySignaled`
              - Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeArrayStartStopTimes`
              - Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantEpoch`
              - Event set at specified date/time.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantExtremum`
              - Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantFactory`
              - The factory creates events.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeInterval`
              - A single time interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalBetweenTimeInstants`
              - Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollection`
              - A collection of related interval lists.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionFactory`
              - The factory creates collections of event interval lists.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionLighting`
              - Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalCollectionSignaled`
              - Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalFactory`
              - The factory creates event intervals.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalFixed`
              - Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalFixedDuration`
              - Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalFromIntervalList`
              - Interval created from specified interval list by using one of several selection methods.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalList`
              - An ordered list of time intervals.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFactory`
              - The factory creates event interval lists.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFile`
              - Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFiltered`
              - Defined by filtering intervals from original interval list using specified filtering method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListMerged`
              - Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListScaled`
              - Interval List defined by scaling every interval in original interval list using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval is removed from scaled list...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListSignaled`
              - Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalListTimeOffset`
              - Interval List defined by shifting the specified reference interval list by a fixed time offset.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalScaled`
              - Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalSignaled`
              - Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalSmartInterval`
              - A smart interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalTimeOffset`
              - Interval defined by shifting specified reference interval by fixed time offset.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantSignaled`
              - Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantSmartEpoch`
              - A smart epoch.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantStartStopTime`
              - Event is either start or stop time selected from a reference interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInstantTimeOffset`
              - Event at fixed offset from specified reference event.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalFirstIntervalsFilter`
              - The filter selects a portion of first intervals.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalGapsFilter`
              - The filter merges intervals unless they are separated by gaps of at least/most certain duration.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolIntegralBasic`
              - Integral definition determines how scalar calculation is numerically integrated.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchInterpolator`
              - Represents a base class for interpolation definitions.

            * - :py:class:`~ansys.stk.core.vgt.CalculationToolInterpolatorBasic`
              - Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalsFilter`
              - The filter selects intervals of at least/most certain duration.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalLastIntervalsFilter`
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

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalRelativeSatisfactionConditionFilter`
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

            * - :py:class:`~ansys.stk.core.vgt.TimeToolTimeIntervalSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain duration.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolSignalDelayBasic`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory`
              - The factory is used to create instances of volume calcs.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory`
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

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolSpatialCalculation`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationAltitude`
              - A volume calc altitude interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationAngleToLocation`
              - A volume calc angle off vector interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationConditionSatisfactionMetric`
              - A volume calc condition satisfaction interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation`
              - A volume calc propagation delay to location interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFile`
              - Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFromCalculationScalar`
              - A volume calc scalar to location interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationDistanceToLocation`
              - A volume calc distance to location interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationSolarIntensity`
              - A volume calc solar intensityn interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionCombined`
              - A combined volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionSpatialCalculationBounds`
              - An volume from calc volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionConditionAtLocation`
              - A volume from conditioninterface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGridBoundingVolume`
              - An over time volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionValidTimeAtLocation`
              - An volume from time satisfaction volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude`
              - A volume grid bearing alt (Surface Bearing) interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian`
              - A volume grid Cartesian interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridConstrained`
              - A volume grid constrained interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical`
              - A volume grid cylindrical interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude`
              - A volume grid lat lon alt (Cartogrographic) interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridResult`
              - An interface that generates Volume Grid results.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical`
              - A volume grid spherical interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionAccessToLocation`
              - An Inview volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionLighting`
              - A lighting volume interface.

            * - :py:class:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime`
              - An over time volume interface.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchComponent`
              - Generic VGT component.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentTypeInformation`
              - VGT component info.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentInstance`
              - Enable to obtain information about the parent object that owns the VGT component.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentTemplate`
              - Enable to obtain information about the STK class that owns the VGT component.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointReference`
              - Represents a reference to a VGT point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorReference`
              - Represents a vector reference.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesReference`
              - Represents a reference to a VGT axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAngleReference`
              - Represents a reference to a VGT angle.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemReference`
              - Represents a System reference.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPlaneReference`
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

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolAxesModelAttachment`
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

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointModelAttachment`
              - A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointSatelliteCollectionEntry`
              - A point placed at the center of mass of a specified satellite of the satellite collection.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointPlaneProjection`
              - The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration`
              - Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointCommonTasks`
              - Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect`
              - Point on central body surface along direction vector originating at source point.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant`
              - Point fixed relative to reference system based on another point evaluated at specified time instant.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointPlugin`
              - A VGT point plugin.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyFixedOffset`
              - Point specified by fixed components with respect to central body.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemAssembled`
              - A system assembled from an origin point and a set of reference axes.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface`
              - A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchPositionLLA`
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

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorModelAttachment`
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

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorProjectionAlongVector`
              - A projection of a source vector in the direction of another vector.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarLinearCombination`
              - Linear combination of two input vectors using scalars.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorScalarScaled`
              - Scaled version of the input vector using scalar.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorVelocityAcceleration`
              - Velocity vector of a point in a coordinate system.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorPlugin`
              - A VGT vector plugin.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorSurfaceDisplacement`
              - Displacement between origin and destination points using surface distance and altitude difference.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolVectorFile`
              - Vector interpolated from tabulated data from file.

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

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider`
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

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchAngleFindResult`
              - Represents result returned with IVectorGeometryToolAngle.FindCoordinates method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchAngleFindWithRateResult`
              - Contains the results returned with IVectorGeometryToolAngle.FindCoordinatesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformResult`
              - Contains the results returned with IVectorGeometryToolAxes.TransformFrom method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformWithRateResult`
              - Contains the results returned with IVectorGeometryToolAxes.TransformFromWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesResult`
              - Contains the results returned with IVectorGeometryToolAxes.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesWithRateResult`
              - Contains the results returned with IVectorGeometryToolAxes.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInAxesResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInAxesWithRateResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInSystem method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchPointLocateInSystemResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchPointLocateInSystemWithRateResult`
              - Contains the results returned with IVectorGeometryToolPoint.LocateInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformResult`
              - Contains the results returned with IVectorGeometryToolSystem.TransformFrom and IVectorGeometryToolSystem.TransformTo methods.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformWithRateResult`
              - Contains the results returned with IVectorGeometryToolSystem.TransformFromWithRate and IVectorGeometryToolSystem.TransformToWithRate methods.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult`
              - Contains the results returned with IVectorGeometryToolSystem.FindInSystem method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchVectorFindInAxesResult`
              - Contains the results returned with IVectorGeometryToolVector.FindInAxes method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchVectorFindInAxesWithRateResult`
              - Contains the results returned with IVectorGeometryToolVector.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchAngleFindAngleWithRateResult`
              - Contains the results returned with IVectorGeometryToolAngle.FindAngleWithRate method.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchAngleFindAngleResult`
              - Contains the results returned with IVectorGeometryToolAngle.FindAngle method.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolInterval`
              - Represents an interval.

            * - :py:class:`~ansys.stk.core.vgt.TimeToolIntervalCollection`
              - Represents a collection of intervals.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBody`
              - Represents an central body.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyReference`
              - Represents a central body reference.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchCentralBodyCollection`
              - A collection of central body names.

            * - :py:class:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection`
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
        

            * - :py:class:`~ansys.stk.core.vgt.CalculationScalarType`
              - Define available calculation scalar types.

            * - :py:class:`~ansys.stk.core.vgt.ConditionCombinedOperationType`
              - Define scalar condition combined operation types.

            * - :py:class:`~ansys.stk.core.vgt.ConditionSetType`
              - Define available condition set types.

            * - :py:class:`~ansys.stk.core.vgt.ConditionThresholdType`
              - Operations for Scalar Bounds Condition.

            * - :py:class:`~ansys.stk.core.vgt.ConditionType`
              - Define available condition types.

            * - :py:class:`~ansys.stk.core.vgt.InheritDimensionType`
              - Define how dimension is inherited.

            * - :py:class:`~ansys.stk.core.vgt.EventArrayFilterType`
              - Event array filter types.

            * - :py:class:`~ansys.stk.core.vgt.EventArrayType`
              - Define available time array types.

            * - :py:class:`~ansys.stk.core.vgt.EventIntervalCollectionType`
              - Define available interval collection types.

            * - :py:class:`~ansys.stk.core.vgt.EventIntervalListType`
              - Define available interval list types.

            * - :py:class:`~ansys.stk.core.vgt.EventIntervalType`
              - Define available interval types.

            * - :py:class:`~ansys.stk.core.vgt.EventListMergeOperation`
              - Define merge operations for interval lists.

            * - :py:class:`~ansys.stk.core.vgt.TimeEventType`
              - Define available time instant types.

            * - :py:class:`~ansys.stk.core.vgt.ExtremumType`
              - These constants are utilized when finding a local or global minimum or maximum, or the threshold crossing.

            * - :py:class:`~ansys.stk.core.vgt.FileInterpolatorType`
              - Interpolator types.

            * - :py:class:`~ansys.stk.core.vgt.QuadratureType`
              - Integral types.

            * - :py:class:`~ansys.stk.core.vgt.IntegrationWindowType`
              - Define the interval of times during which an integral is evaluated.

            * - :py:class:`~ansys.stk.core.vgt.InterpolationMethodType`
              - Interpolator types.

            * - :py:class:`~ansys.stk.core.vgt.IntervalDurationType`
              - Duration for filtering intervals or gaps from interval lists or time arrays.

            * - :py:class:`~ansys.stk.core.vgt.IntervalFromIntervalListSelectionType`
              - Select the method to choose an interval from an interval list.

            * - :py:class:`~ansys.stk.core.vgt.ParameterSetType`
              - Define parameter set types.

            * - :py:class:`~ansys.stk.core.vgt.IntervalPruneFilterType`
              - Specify the filter for filtering interval lists or time arrays.

            * - :py:class:`~ansys.stk.core.vgt.SampleReferenceTimeType`
              - Event array reference type.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolSamplingMethod`
              - Define the Sampling Method.

            * - :py:class:`~ansys.stk.core.vgt.SatisfactionCrossing`
              - Direction crossing flags.

            * - :py:class:`~ansys.stk.core.vgt.SaveDataType`
              - Method for saving computed data.

            * - :py:class:`~ansys.stk.core.vgt.SignalPathReferenceSystem`
              - Signal path reference system types.

            * - :py:class:`~ansys.stk.core.vgt.SmartEpochState`
              - Smart epoch states.

            * - :py:class:`~ansys.stk.core.vgt.SmartIntervalState`
              - Smart interval states.

            * - :py:class:`~ansys.stk.core.vgt.SpeedType`
              - Define various speed options.

            * - :py:class:`~ansys.stk.core.vgt.StartStopType`
              - Start/stop options.

            * - :py:class:`~ansys.stk.core.vgt.ThresholdConvergenceSenseType`
              - Specify the desired sense of the results from threshold crossing computations.

            * - :py:class:`~ansys.stk.core.vgt.VectorComponentType`
              - Define component directions for a vector.

            * - :py:class:`~ansys.stk.core.vgt.SpatialCalculationAltitudeReferenceType`
              - Define volume calc altitude reference types.

            * - :py:class:`~ansys.stk.core.vgt.AngleToLocationType`
              - Define volume calc angle off vector reference types.

            * - :py:class:`~ansys.stk.core.vgt.DistanceToLocationType`
              - Define volume calc range distance types.

            * - :py:class:`~ansys.stk.core.vgt.RangeSpeedType`
              - Define volume calc range distance types.

            * - :py:class:`~ansys.stk.core.vgt.SpatialCalculationType`
              - Define volume calc types.

            * - :py:class:`~ansys.stk.core.vgt.VolumeSatisfactionAccumulationType`
              - Define volume calc spatial condition accumulation types.

            * - :py:class:`~ansys.stk.core.vgt.VolumeSatisfactionDurationType`
              - Define volume calc spatial condition duration types.

            * - :py:class:`~ansys.stk.core.vgt.VolumeSatisfactionFilterType`
              - Define volume calc spatial condition filter types.

            * - :py:class:`~ansys.stk.core.vgt.VolumeSatisfactionMetricType`
              - Define volume calc spatial condition satisfaction metric types.

            * - :py:class:`~ansys.stk.core.vgt.VolumeGridType`
              - Define volume grid types.

            * - :py:class:`~ansys.stk.core.vgt.ResultVectorRequestType`
              - Define volume result vector request types.

            * - :py:class:`~ansys.stk.core.vgt.VolumeType`
              - Define volume grid types.

            * - :py:class:`~ansys.stk.core.vgt.AberrationModelType`
              - Define the model of aberration to use.

            * - :py:class:`~ansys.stk.core.vgt.ClockHostType`
              - Define whether base or target of an Access instance holds the clock for Access times.

            * - :py:class:`~ansys.stk.core.vgt.VolumeCombinedOperationType`
              - Define spatial condition combined operation types.

            * - :py:class:`~ansys.stk.core.vgt.VolumeFromGridEdgeType`
              - Define spatial condition from grid edge type.

            * - :py:class:`~ansys.stk.core.vgt.LightingConditionsType`
              - Define spatial condition lighting conditions types.

            * - :py:class:`~ansys.stk.core.vgt.SpatialConditionOverTypeDurationType`
              - Define spatial condition over time duration type.

            * - :py:class:`~ansys.stk.core.vgt.TimeSenseType`
              - Define whether object1 or object2 of an Access instance holds the clock for Access times.

            * - :py:class:`~ansys.stk.core.vgt.GridValuesMethodType`
              - Define volumetric grid values method types.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolComponentType`
              - Represents kinds of vectory geometry components.

            * - :py:class:`~ansys.stk.core.vgt.AngleType`
              - Represents angle types.

            * - :py:class:`~ansys.stk.core.vgt.AxesType`
              - Represents vector types.

            * - :py:class:`~ansys.stk.core.vgt.PlaneType`
              - Represents plane types.

            * - :py:class:`~ansys.stk.core.vgt.PointType`
              - Represents point types.

            * - :py:class:`~ansys.stk.core.vgt.SystemType`
              - Represents system types.

            * - :py:class:`~ansys.stk.core.vgt.VectorType`
              - Represents vector types.

            * - :py:class:`~ansys.stk.core.vgt.MeanElementTheory`
              - Mean element theory types for approximating motion.

            * - :py:class:`~ansys.stk.core.vgt.AsymptoteDirectionType`
              - Direction options.

            * - :py:class:`~ansys.stk.core.vgt.LagrangeLibrationPointType`
              - Types of the Lagrange points, also known as libration points. Lagrange points are points in space where gravitational forces and the orbital motion of a body balance each other.

            * - :py:class:`~ansys.stk.core.vgt.PlaneQuadrantType`
              - Quadrants from a reference system (e.g., XY, XZ, YZ, YX, ZX, ZY).

            * - :py:class:`~ansys.stk.core.vgt.TrajectoryAxesCoordinatesType`
              - Trajectory axes coordinate types.

            * - :py:class:`~ansys.stk.core.vgt.PrincipalAxisOfRotationType`
              - Rotation directions.

            * - :py:class:`~ansys.stk.core.vgt.SignedAngleType`
              - Define options for computing an angle.

            * - :py:class:`~ansys.stk.core.vgt.PointBPlaneType`
              - B-Plane point types.

            * - :py:class:`~ansys.stk.core.vgt.SurfaceReferenceShapeType`
              - Surface shape types.

            * - :py:class:`~ansys.stk.core.vgt.SurfaceShapeType`
              - Surface types.

            * - :py:class:`~ansys.stk.core.vgt.RotationSweepModeType`
              - The rotation sweeping modes.

            * - :py:class:`~ansys.stk.core.vgt.SignalDirectionType`
              - Signal sense transmission options.

            * - :py:class:`~ansys.stk.core.vgt.IntersectionSurfaceType`
              - Intersection surface flags.

            * - :py:class:`~ansys.stk.core.vgt.VectorGeometryToolScaledVectorDimensionInheritanceOptionType`
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
     IAnalysisWorkbenchComponentContext<vgt/IAnalysisWorkbenchComponentContext>
     IAnalysisWorkbenchComponent<vgt/IAnalysisWorkbenchComponent>
     ICalculationToolScalar<vgt/ICalculationToolScalar>
     ICalculationToolCondition<vgt/ICalculationToolCondition>
     ICalculationToolConditionSet<vgt/ICalculationToolConditionSet>
     IAnalysisWorkbenchConvergence<vgt/IAnalysisWorkbenchConvergence>
     IAnalysisWorkbenchDerivative<vgt/IAnalysisWorkbenchDerivative>
     ITimeToolInstant<vgt/ITimeToolInstant>
     ITimeToolTimeArray<vgt/ITimeToolTimeArray>
     ITimeToolTimeInterval<vgt/ITimeToolTimeInterval>
     ITimeToolTimeIntervalCollection<vgt/ITimeToolTimeIntervalCollection>
     ITimeToolTimeIntervalList<vgt/ITimeToolTimeIntervalList>
     IAnalysisWorkbenchIntegral<vgt/IAnalysisWorkbenchIntegral>
     IAnalysisWorkbenchInterpolator<vgt/IAnalysisWorkbenchInterpolator>
     ICalculationToolParameterSet<vgt/ICalculationToolParameterSet>
     ITimeToolPruneFilter<vgt/ITimeToolPruneFilter>
     IAnalysisWorkbenchSampling<vgt/IAnalysisWorkbenchSampling>
     ICalculationToolSamplingMethod<vgt/ICalculationToolSamplingMethod>
     IAnalysisWorkbenchSignalDelay<vgt/IAnalysisWorkbenchSignalDelay>
     ISpatialAnalysisToolGridValuesMethod<vgt/ISpatialAnalysisToolGridValuesMethod>
     ISpatialAnalysisToolVolume<vgt/ISpatialAnalysisToolVolume>
     ISpatialAnalysisToolSpatialCalculation<vgt/ISpatialAnalysisToolSpatialCalculation>
     ISpatialAnalysisToolVolumeGrid<vgt/ISpatialAnalysisToolVolumeGrid>
     IAnalysisWorkbenchComponentTimeProperties<vgt/IAnalysisWorkbenchComponentTimeProperties>
     IAnalysisWorkbenchComponentReference<vgt/IAnalysisWorkbenchComponentReference>
     IAnalysisWorkbenchMethodCallResult<vgt/IAnalysisWorkbenchMethodCallResult>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     CalculationToolEvaluateResult<vgt/CalculationToolEvaluateResult>
     CalculationToolEvaluateWithRateResult<vgt/CalculationToolEvaluateWithRateResult>
     TimeToolTimeIntervalResult<vgt/TimeToolTimeIntervalResult>
     TimeToolInstantOccurrenceResult<vgt/TimeToolInstantOccurrenceResult>
     TimeToolTimeArrayFindTimesResult<vgt/TimeToolTimeArrayFindTimesResult>
     TimeToolIntervalsVectorResult<vgt/TimeToolIntervalsVectorResult>
     TimeToolTimeIntervalCollectionOccurredResult<vgt/TimeToolTimeIntervalCollectionOccurredResult>
     TimeToolIntervalListResult<vgt/TimeToolIntervalListResult>
     TimeToolIntervalVectorCollection<vgt/TimeToolIntervalVectorCollection>
     TimeToolInstantGroup<vgt/TimeToolInstantGroup>
     TimeToolTimeIntervalGroup<vgt/TimeToolTimeIntervalGroup>
     TimeToolTimeIntervalListGroup<vgt/TimeToolTimeIntervalListGroup>
     TimeToolTimeArrayGroup<vgt/TimeToolTimeArrayGroup>
     CalculationToolScalarGroup<vgt/CalculationToolScalarGroup>
     TimeToolTimeIntervalCollectionGroup<vgt/TimeToolTimeIntervalCollectionGroup>
     CalculationToolParameterSetGroup<vgt/CalculationToolParameterSetGroup>
     CalculationToolConditionGroup<vgt/CalculationToolConditionGroup>
     CalculationToolConditionSetGroup<vgt/CalculationToolConditionSetGroup>
     CalculationToolConditionSetEvaluateResult<vgt/CalculationToolConditionSetEvaluateResult>
     CalculationToolConditionSetEvaluateWithRateResult<vgt/CalculationToolConditionSetEvaluateWithRateResult>
     SpatialAnalysisToolVolumeGridGroup<vgt/SpatialAnalysisToolVolumeGridGroup>
     SpatialAnalysisToolConditionGroup<vgt/SpatialAnalysisToolConditionGroup>
     SpatialAnalysisToolCalculationGroup<vgt/SpatialAnalysisToolCalculationGroup>
     CalculationToolScalar<vgt/CalculationToolScalar>
     CalculationToolScalarAngle<vgt/CalculationToolScalarAngle>
     CalculationToolScalarAverage<vgt/CalculationToolScalarAverage>
     CalculationToolScalarConstant<vgt/CalculationToolScalarConstant>
     CalculationToolScalarCustom<vgt/CalculationToolScalarCustom>
     CalculationToolScalarCustomInlineScript<vgt/CalculationToolScalarCustomInlineScript>
     CalculationToolScalarDataElement<vgt/CalculationToolScalarDataElement>
     CalculationToolScalarDerivative<vgt/CalculationToolScalarDerivative>
     CalculationToolScalarDotProduct<vgt/CalculationToolScalarDotProduct>
     CalculationToolScalarElapsedTime<vgt/CalculationToolScalarElapsedTime>
     CalculationToolScalarFactory<vgt/CalculationToolScalarFactory>
     CalculationToolScalarFile<vgt/CalculationToolScalarFile>
     CalculationToolScalarFixedAtTimeInstant<vgt/CalculationToolScalarFixedAtTimeInstant>
     CalculationToolScalarFunction<vgt/CalculationToolScalarFunction>
     CalculationToolScalarFunctionOf2Variables<vgt/CalculationToolScalarFunctionOf2Variables>
     CalculationToolScalarIntegral<vgt/CalculationToolScalarIntegral>
     CalculationToolScalarPlugin<vgt/CalculationToolScalarPlugin>
     CalculationToolScalarAlongTrajectory<vgt/CalculationToolScalarAlongTrajectory>
     CalculationToolScalarStandardDeviation<vgt/CalculationToolScalarStandardDeviation>
     CalculationToolScalarSurfaceDistanceBetweenPoints<vgt/CalculationToolScalarSurfaceDistanceBetweenPoints>
     CalculationToolScalarVectorComponent<vgt/CalculationToolScalarVectorComponent>
     CalculationToolScalarVectorMagnitude<vgt/CalculationToolScalarVectorMagnitude>
     CalculationToolCondition<vgt/CalculationToolCondition>
     CalculationToolConditionCombined<vgt/CalculationToolConditionCombined>
     CalculationToolConditionFactory<vgt/CalculationToolConditionFactory>
     CalculationToolConditionTrajectoryWithinVolume<vgt/CalculationToolConditionTrajectoryWithinVolume>
     CalculationToolConditionScalarBounds<vgt/CalculationToolConditionScalarBounds>
     CalculationToolConditionSet<vgt/CalculationToolConditionSet>
     CalculationToolConditionSetFactory<vgt/CalculationToolConditionSetFactory>
     CalculationToolConditionSetScalarThresholds<vgt/CalculationToolConditionSetScalarThresholds>
     AnalysisWorkbenchConvergence<vgt/AnalysisWorkbenchConvergence>
     CalculationToolConvergeBasic<vgt/CalculationToolConvergeBasic>
     AnalysisWorkbenchDerivative<vgt/AnalysisWorkbenchDerivative>
     CalculationToolDerivativeBasic<vgt/CalculationToolDerivativeBasic>
     TimeToolInstant<vgt/TimeToolInstant>
     TimeToolTimeArray<vgt/TimeToolTimeArray>
     TimeToolTimeArrayConditionCrossings<vgt/TimeToolTimeArrayConditionCrossings>
     TimeToolTimeArrayExtrema<vgt/TimeToolTimeArrayExtrema>
     TimeToolTimeArrayFactory<vgt/TimeToolTimeArrayFactory>
     TimeToolTimeArrayFiltered<vgt/TimeToolTimeArrayFiltered>
     TimeToolTimeArrayFixedStep<vgt/TimeToolTimeArrayFixedStep>
     TimeToolTimeArrayFixedTimes<vgt/TimeToolTimeArrayFixedTimes>
     TimeToolTimeArrayMerged<vgt/TimeToolTimeArrayMerged>
     TimeToolTimeArraySignaled<vgt/TimeToolTimeArraySignaled>
     TimeToolTimeArrayStartStopTimes<vgt/TimeToolTimeArrayStartStopTimes>
     TimeToolInstantEpoch<vgt/TimeToolInstantEpoch>
     TimeToolInstantExtremum<vgt/TimeToolInstantExtremum>
     TimeToolInstantFactory<vgt/TimeToolInstantFactory>
     TimeToolTimeInterval<vgt/TimeToolTimeInterval>
     TimeToolTimeIntervalBetweenTimeInstants<vgt/TimeToolTimeIntervalBetweenTimeInstants>
     TimeToolTimeIntervalCollection<vgt/TimeToolTimeIntervalCollection>
     TimeToolTimeIntervalCollectionCondition<vgt/TimeToolTimeIntervalCollectionCondition>
     TimeToolTimeIntervalCollectionFactory<vgt/TimeToolTimeIntervalCollectionFactory>
     TimeToolTimeIntervalCollectionLighting<vgt/TimeToolTimeIntervalCollectionLighting>
     TimeToolTimeIntervalCollectionSignaled<vgt/TimeToolTimeIntervalCollectionSignaled>
     TimeToolTimeIntervalFactory<vgt/TimeToolTimeIntervalFactory>
     TimeToolTimeIntervalFixed<vgt/TimeToolTimeIntervalFixed>
     TimeToolTimeIntervalFixedDuration<vgt/TimeToolTimeIntervalFixedDuration>
     TimeToolTimeIntervalFromIntervalList<vgt/TimeToolTimeIntervalFromIntervalList>
     TimeToolTimeIntervalList<vgt/TimeToolTimeIntervalList>
     TimeToolTimeIntervalListCondition<vgt/TimeToolTimeIntervalListCondition>
     TimeToolTimeIntervalListFactory<vgt/TimeToolTimeIntervalListFactory>
     TimeToolTimeIntervalListFile<vgt/TimeToolTimeIntervalListFile>
     TimeToolTimeIntervalListFiltered<vgt/TimeToolTimeIntervalListFiltered>
     TimeToolTimeIntervalListFixed<vgt/TimeToolTimeIntervalListFixed>
     TimeToolTimeIntervalListMerged<vgt/TimeToolTimeIntervalListMerged>
     TimeToolTimeIntervalListScaled<vgt/TimeToolTimeIntervalListScaled>
     TimeToolTimeIntervalListSignaled<vgt/TimeToolTimeIntervalListSignaled>
     TimeToolTimeIntervalListTimeOffset<vgt/TimeToolTimeIntervalListTimeOffset>
     TimeToolTimeIntervalScaled<vgt/TimeToolTimeIntervalScaled>
     TimeToolTimeIntervalSignaled<vgt/TimeToolTimeIntervalSignaled>
     TimeToolTimeIntervalSmartInterval<vgt/TimeToolTimeIntervalSmartInterval>
     TimeToolTimeIntervalTimeOffset<vgt/TimeToolTimeIntervalTimeOffset>
     TimeToolInstantSignaled<vgt/TimeToolInstantSignaled>
     TimeToolInstantSmartEpoch<vgt/TimeToolInstantSmartEpoch>
     TimeToolInstantStartStopTime<vgt/TimeToolInstantStartStopTime>
     TimeToolInstantTimeOffset<vgt/TimeToolInstantTimeOffset>
     TimeToolTimeIntervalFirstIntervalsFilter<vgt/TimeToolTimeIntervalFirstIntervalsFilter>
     TimeToolTimeIntervalGapsFilter<vgt/TimeToolTimeIntervalGapsFilter>
     AnalysisWorkbenchIntegral<vgt/AnalysisWorkbenchIntegral>
     CalculationToolIntegralBasic<vgt/CalculationToolIntegralBasic>
     AnalysisWorkbenchInterpolator<vgt/AnalysisWorkbenchInterpolator>
     CalculationToolInterpolatorBasic<vgt/CalculationToolInterpolatorBasic>
     TimeToolIntervalsFilter<vgt/TimeToolIntervalsFilter>
     TimeToolTimeIntervalLastIntervalsFilter<vgt/TimeToolTimeIntervalLastIntervalsFilter>
     CalculationToolParameterSet<vgt/CalculationToolParameterSet>
     CalculationToolParameterSetAttitude<vgt/CalculationToolParameterSetAttitude>
     CalculationToolParameterSetFactory<vgt/CalculationToolParameterSetFactory>
     CalculationToolParameterSetGroundTrajectory<vgt/CalculationToolParameterSetGroundTrajectory>
     CalculationToolParameterSetOrbit<vgt/CalculationToolParameterSetOrbit>
     CalculationToolParameterSetTrajectory<vgt/CalculationToolParameterSetTrajectory>
     CalculationToolParameterSetVector<vgt/CalculationToolParameterSetVector>
     TimeToolPruneFilter<vgt/TimeToolPruneFilter>
     TimeToolPruneFilterFactory<vgt/TimeToolPruneFilterFactory>
     TimeToolTimeIntervalRelativeSatisfactionConditionFilter<vgt/TimeToolTimeIntervalRelativeSatisfactionConditionFilter>
     AnalysisWorkbenchSampling<vgt/AnalysisWorkbenchSampling>
     CalculationToolSamplingBasic<vgt/CalculationToolSamplingBasic>
     CalculationToolSamplingCurvatureTolerance<vgt/CalculationToolSamplingCurvatureTolerance>
     CalculationToolSamplingFixedStep<vgt/CalculationToolSamplingFixedStep>
     CalculationToolSamplingMethod<vgt/CalculationToolSamplingMethod>
     CalculationToolSamplingMethodFactory<vgt/CalculationToolSamplingMethodFactory>
     CalculationToolSamplingRelativeTolerance<vgt/CalculationToolSamplingRelativeTolerance>
     TimeToolTimeIntervalSatisfactionConditionFilter<vgt/TimeToolTimeIntervalSatisfactionConditionFilter>
     AnalysisWorkbenchSignalDelay<vgt/AnalysisWorkbenchSignalDelay>
     TimeToolSignalDelayBasic<vgt/TimeToolSignalDelayBasic>
     SpatialAnalysisToolCalculationFactory<vgt/SpatialAnalysisToolCalculationFactory>
     SpatialAnalysisToolConditionFactory<vgt/SpatialAnalysisToolConditionFactory>
     SpatialAnalysisToolVolumeGridFactory<vgt/SpatialAnalysisToolVolumeGridFactory>
     SpatialAnalysisToolGridCoordinateDefinition<vgt/SpatialAnalysisToolGridCoordinateDefinition>
     SpatialAnalysisToolGridValuesCustom<vgt/SpatialAnalysisToolGridValuesCustom>
     SpatialAnalysisToolGridValuesFixedNumberOfSteps<vgt/SpatialAnalysisToolGridValuesFixedNumberOfSteps>
     SpatialAnalysisToolGridValuesFixedStep<vgt/SpatialAnalysisToolGridValuesFixedStep>
     SpatialAnalysisToolGridValuesMethod<vgt/SpatialAnalysisToolGridValuesMethod>
     TimeToolLightTimeDelay<vgt/TimeToolLightTimeDelay>
     SpatialAnalysisToolVolume<vgt/SpatialAnalysisToolVolume>
     SpatialAnalysisToolSpatialCalculation<vgt/SpatialAnalysisToolSpatialCalculation>
     SpatialAnalysisToolCalculationAltitude<vgt/SpatialAnalysisToolCalculationAltitude>
     SpatialAnalysisToolCalculationAngleToLocation<vgt/SpatialAnalysisToolCalculationAngleToLocation>
     SpatialAnalysisToolCalculationConditionSatisfactionMetric<vgt/SpatialAnalysisToolCalculationConditionSatisfactionMetric>
     SpatialAnalysisToolCalculationPropagationDelayToLocation<vgt/SpatialAnalysisToolCalculationPropagationDelayToLocation>
     SpatialAnalysisToolCalculationFile<vgt/SpatialAnalysisToolCalculationFile>
     SpatialAnalysisToolCalculationFromCalculationScalar<vgt/SpatialAnalysisToolCalculationFromCalculationScalar>
     SpatialAnalysisToolCalculationDistanceToLocation<vgt/SpatialAnalysisToolCalculationDistanceToLocation>
     SpatialAnalysisToolCalculationSolarIntensity<vgt/SpatialAnalysisToolCalculationSolarIntensity>
     SpatialAnalysisToolConditionCombined<vgt/SpatialAnalysisToolConditionCombined>
     SpatialAnalysisToolConditionSpatialCalculationBounds<vgt/SpatialAnalysisToolConditionSpatialCalculationBounds>
     SpatialAnalysisToolConditionConditionAtLocation<vgt/SpatialAnalysisToolConditionConditionAtLocation>
     SpatialAnalysisToolConditionGridBoundingVolume<vgt/SpatialAnalysisToolConditionGridBoundingVolume>
     SpatialAnalysisToolConditionValidTimeAtLocation<vgt/SpatialAnalysisToolConditionValidTimeAtLocation>
     SpatialAnalysisToolVolumeGrid<vgt/SpatialAnalysisToolVolumeGrid>
     SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude<vgt/SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude>
     SpatialAnalysisToolVolumeGridCartesian<vgt/SpatialAnalysisToolVolumeGridCartesian>
     SpatialAnalysisToolVolumeGridConstrained<vgt/SpatialAnalysisToolVolumeGridConstrained>
     SpatialAnalysisToolVolumeGridCylindrical<vgt/SpatialAnalysisToolVolumeGridCylindrical>
     SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude<vgt/SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude>
     SpatialAnalysisToolVolumeGridResult<vgt/SpatialAnalysisToolVolumeGridResult>
     SpatialAnalysisToolVolumeGridSpherical<vgt/SpatialAnalysisToolVolumeGridSpherical>
     SpatialAnalysisToolConditionAccessToLocation<vgt/SpatialAnalysisToolConditionAccessToLocation>
     SpatialAnalysisToolConditionLighting<vgt/SpatialAnalysisToolConditionLighting>
     SpatialAnalysisToolConditionOverTime<vgt/SpatialAnalysisToolConditionOverTime>
     AnalysisWorkbenchComponent<vgt/AnalysisWorkbenchComponent>
     AnalysisWorkbenchComponentTypeInformation<vgt/AnalysisWorkbenchComponentTypeInformation>
     AnalysisWorkbenchComponentInstance<vgt/AnalysisWorkbenchComponentInstance>
     AnalysisWorkbenchComponentTemplate<vgt/AnalysisWorkbenchComponentTemplate>
     VectorGeometryToolPointReference<vgt/VectorGeometryToolPointReference>
     VectorGeometryToolVectorReference<vgt/VectorGeometryToolVectorReference>
     VectorGeometryToolAxesReference<vgt/VectorGeometryToolAxesReference>
     VectorGeometryToolAngleReference<vgt/VectorGeometryToolAngleReference>
     VectorGeometryToolSystemReference<vgt/VectorGeometryToolSystemReference>
     VectorGeometryToolPlaneReference<vgt/VectorGeometryToolPlaneReference>
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
     VectorGeometryToolAxesModelAttachment<vgt/VectorGeometryToolAxesModelAttachment>
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
     VectorGeometryToolPointModelAttachment<vgt/VectorGeometryToolPointModelAttachment>
     VectorGeometryToolPointSatelliteCollectionEntry<vgt/VectorGeometryToolPointSatelliteCollectionEntry>
     VectorGeometryToolPointPlaneProjection<vgt/VectorGeometryToolPointPlaneProjection>
     VectorGeometryToolPointLagrangeLibration<vgt/VectorGeometryToolPointLagrangeLibration>
     VectorGeometryToolPointCommonTasks<vgt/VectorGeometryToolPointCommonTasks>
     VectorGeometryToolPointCentralBodyIntersect<vgt/VectorGeometryToolPointCentralBodyIntersect>
     VectorGeometryToolPointAtTimeInstant<vgt/VectorGeometryToolPointAtTimeInstant>
     VectorGeometryToolPointPlugin<vgt/VectorGeometryToolPointPlugin>
     VectorGeometryToolPointCentralBodyFixedOffset<vgt/VectorGeometryToolPointCentralBodyFixedOffset>
     VectorGeometryToolSystemAssembled<vgt/VectorGeometryToolSystemAssembled>
     VectorGeometryToolSystemOnSurface<vgt/VectorGeometryToolSystemOnSurface>
     AnalysisWorkbenchPositionLLA<vgt/AnalysisWorkbenchPositionLLA>
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
     VectorGeometryToolVectorModelAttachment<vgt/VectorGeometryToolVectorModelAttachment>
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
     VectorGeometryToolVectorProjectionAlongVector<vgt/VectorGeometryToolVectorProjectionAlongVector>
     VectorGeometryToolVectorScalarLinearCombination<vgt/VectorGeometryToolVectorScalarLinearCombination>
     VectorGeometryToolVectorScalarScaled<vgt/VectorGeometryToolVectorScalarScaled>
     VectorGeometryToolVectorVelocityAcceleration<vgt/VectorGeometryToolVectorVelocityAcceleration>
     VectorGeometryToolVectorPlugin<vgt/VectorGeometryToolVectorPlugin>
     VectorGeometryToolVectorSurfaceDisplacement<vgt/VectorGeometryToolVectorSurfaceDisplacement>
     VectorGeometryToolVectorFile<vgt/VectorGeometryToolVectorFile>
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
     AnalysisWorkbenchComponentProvider<vgt/AnalysisWorkbenchComponentProvider>
     AnalysisWorkbenchRoot<vgt/AnalysisWorkbenchRoot>
     VectorGeometryToolWellKnownEarthSystems<vgt/VectorGeometryToolWellKnownEarthSystems>
     VectorGeometryToolWellKnownEarthAxes<vgt/VectorGeometryToolWellKnownEarthAxes>
     VectorGeometryToolWellKnownSunSystems<vgt/VectorGeometryToolWellKnownSunSystems>
     VectorGeometryToolWellKnownSunAxes<vgt/VectorGeometryToolWellKnownSunAxes>
     VectorGeometryToolWellKnownSystems<vgt/VectorGeometryToolWellKnownSystems>
     VectorGeometryToolWellKnownAxes<vgt/VectorGeometryToolWellKnownAxes>
     AnalysisWorkbenchAngleFindResult<vgt/AnalysisWorkbenchAngleFindResult>
     AnalysisWorkbenchAngleFindWithRateResult<vgt/AnalysisWorkbenchAngleFindWithRateResult>
     AnalysisWorkbenchAxesTransformResult<vgt/AnalysisWorkbenchAxesTransformResult>
     AnalysisWorkbenchAxesTransformWithRateResult<vgt/AnalysisWorkbenchAxesTransformWithRateResult>
     AnalysisWorkbenchAxesFindInAxesResult<vgt/AnalysisWorkbenchAxesFindInAxesResult>
     AnalysisWorkbenchAxesFindInAxesWithRateResult<vgt/AnalysisWorkbenchAxesFindInAxesWithRateResult>
     AnalysisWorkbenchPlaneFindInAxesResult<vgt/AnalysisWorkbenchPlaneFindInAxesResult>
     AnalysisWorkbenchPlaneFindInAxesWithRateResult<vgt/AnalysisWorkbenchPlaneFindInAxesWithRateResult>
     AnalysisWorkbenchPlaneFindInSystemResult<vgt/AnalysisWorkbenchPlaneFindInSystemResult>
     AnalysisWorkbenchPlaneFindInSystemWithRateResult<vgt/AnalysisWorkbenchPlaneFindInSystemWithRateResult>
     AnalysisWorkbenchPointLocateInSystemResult<vgt/AnalysisWorkbenchPointLocateInSystemResult>
     AnalysisWorkbenchPointLocateInSystemWithRateResult<vgt/AnalysisWorkbenchPointLocateInSystemWithRateResult>
     AnalysisWorkbenchSystemTransformResult<vgt/AnalysisWorkbenchSystemTransformResult>
     AnalysisWorkbenchSystemTransformWithRateResult<vgt/AnalysisWorkbenchSystemTransformWithRateResult>
     AnalysisWorkbenchSystemFindInSystemResult<vgt/AnalysisWorkbenchSystemFindInSystemResult>
     AnalysisWorkbenchVectorFindInAxesResult<vgt/AnalysisWorkbenchVectorFindInAxesResult>
     AnalysisWorkbenchVectorFindInAxesWithRateResult<vgt/AnalysisWorkbenchVectorFindInAxesWithRateResult>
     AnalysisWorkbenchAngleFindAngleWithRateResult<vgt/AnalysisWorkbenchAngleFindAngleWithRateResult>
     AnalysisWorkbenchAngleFindAngleResult<vgt/AnalysisWorkbenchAngleFindAngleResult>
     TimeToolInterval<vgt/TimeToolInterval>
     TimeToolIntervalCollection<vgt/TimeToolIntervalCollection>
     AnalysisWorkbenchCentralBody<vgt/AnalysisWorkbenchCentralBody>
     AnalysisWorkbenchCentralBodyReference<vgt/AnalysisWorkbenchCentralBodyReference>
     AnalysisWorkbenchCentralBodyCollection<vgt/AnalysisWorkbenchCentralBodyCollection>
     AnalysisWorkbenchComponentCollection<vgt/AnalysisWorkbenchComponentCollection>
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

    ≔ CalculationScalarType<vgt/CalculationScalarType>
    ≔ ConditionCombinedOperationType<vgt/ConditionCombinedOperationType>
    ≔ ConditionSetType<vgt/ConditionSetType>
    ≔ ConditionThresholdType<vgt/ConditionThresholdType>
    ≔ ConditionType<vgt/ConditionType>
    ≔ InheritDimensionType<vgt/InheritDimensionType>
    ≔ EventArrayFilterType<vgt/EventArrayFilterType>
    ≔ EventArrayType<vgt/EventArrayType>
    ≔ EventIntervalCollectionType<vgt/EventIntervalCollectionType>
    ≔ EventIntervalListType<vgt/EventIntervalListType>
    ≔ EventIntervalType<vgt/EventIntervalType>
    ≔ EventListMergeOperation<vgt/EventListMergeOperation>
    ≔ TimeEventType<vgt/TimeEventType>
    ≔ ExtremumType<vgt/ExtremumType>
    ≔ FileInterpolatorType<vgt/FileInterpolatorType>
    ≔ QuadratureType<vgt/QuadratureType>
    ≔ IntegrationWindowType<vgt/IntegrationWindowType>
    ≔ InterpolationMethodType<vgt/InterpolationMethodType>
    ≔ IntervalDurationType<vgt/IntervalDurationType>
    ≔ IntervalFromIntervalListSelectionType<vgt/IntervalFromIntervalListSelectionType>
    ≔ ParameterSetType<vgt/ParameterSetType>
    ≔ IntervalPruneFilterType<vgt/IntervalPruneFilterType>
    ≔ SampleReferenceTimeType<vgt/SampleReferenceTimeType>
    ≔ VectorGeometryToolSamplingMethod<vgt/VectorGeometryToolSamplingMethod>
    ≔ SatisfactionCrossing<vgt/SatisfactionCrossing>
    ≔ SaveDataType<vgt/SaveDataType>
    ≔ SignalPathReferenceSystem<vgt/SignalPathReferenceSystem>
    ≔ SmartEpochState<vgt/SmartEpochState>
    ≔ SmartIntervalState<vgt/SmartIntervalState>
    ≔ SpeedType<vgt/SpeedType>
    ≔ StartStopType<vgt/StartStopType>
    ≔ ThresholdConvergenceSenseType<vgt/ThresholdConvergenceSenseType>
    ≔ VectorComponentType<vgt/VectorComponentType>
    ≔ SpatialCalculationAltitudeReferenceType<vgt/SpatialCalculationAltitudeReferenceType>
    ≔ AngleToLocationType<vgt/AngleToLocationType>
    ≔ DistanceToLocationType<vgt/DistanceToLocationType>
    ≔ RangeSpeedType<vgt/RangeSpeedType>
    ≔ SpatialCalculationType<vgt/SpatialCalculationType>
    ≔ VolumeSatisfactionAccumulationType<vgt/VolumeSatisfactionAccumulationType>
    ≔ VolumeSatisfactionDurationType<vgt/VolumeSatisfactionDurationType>
    ≔ VolumeSatisfactionFilterType<vgt/VolumeSatisfactionFilterType>
    ≔ VolumeSatisfactionMetricType<vgt/VolumeSatisfactionMetricType>
    ≔ VolumeGridType<vgt/VolumeGridType>
    ≔ ResultVectorRequestType<vgt/ResultVectorRequestType>
    ≔ VolumeType<vgt/VolumeType>
    ≔ AberrationModelType<vgt/AberrationModelType>
    ≔ ClockHostType<vgt/ClockHostType>
    ≔ VolumeCombinedOperationType<vgt/VolumeCombinedOperationType>
    ≔ VolumeFromGridEdgeType<vgt/VolumeFromGridEdgeType>
    ≔ LightingConditionsType<vgt/LightingConditionsType>
    ≔ SpatialConditionOverTypeDurationType<vgt/SpatialConditionOverTypeDurationType>
    ≔ TimeSenseType<vgt/TimeSenseType>
    ≔ GridValuesMethodType<vgt/GridValuesMethodType>
    ≔ VectorGeometryToolComponentType<vgt/VectorGeometryToolComponentType>
    ≔ AngleType<vgt/AngleType>
    ≔ AxesType<vgt/AxesType>
    ≔ PlaneType<vgt/PlaneType>
    ≔ PointType<vgt/PointType>
    ≔ SystemType<vgt/SystemType>
    ≔ VectorType<vgt/VectorType>
    ≔ MeanElementTheory<vgt/MeanElementTheory>
    ≔ AsymptoteDirectionType<vgt/AsymptoteDirectionType>
    ≔ LagrangeLibrationPointType<vgt/LagrangeLibrationPointType>
    ≔ PlaneQuadrantType<vgt/PlaneQuadrantType>
    ≔ TrajectoryAxesCoordinatesType<vgt/TrajectoryAxesCoordinatesType>
    ≔ PrincipalAxisOfRotationType<vgt/PrincipalAxisOfRotationType>
    ≔ SignedAngleType<vgt/SignedAngleType>
    ≔ PointBPlaneType<vgt/PointBPlaneType>
    ≔ SurfaceReferenceShapeType<vgt/SurfaceReferenceShapeType>
    ≔ SurfaceShapeType<vgt/SurfaceShapeType>
    ≔ RotationSweepModeType<vgt/RotationSweepModeType>
    ≔ SignalDirectionType<vgt/SignalDirectionType>
    ≔ IntersectionSurfaceType<vgt/IntersectionSurfaceType>
    ≔ VectorGeometryToolScaledVectorDimensionInheritanceOptionType<vgt/VectorGeometryToolScaledVectorDimensionInheritanceOptionType>

