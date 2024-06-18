
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
        

            * - :py:class:`~ITimeToolIntervalCollection`
              - The interface represents a collection of intervals.

            * - :py:class:`~ITimeToolInterval`
              - The interface represents an interval.

            * - :py:class:`~IVectorGeometryToolPoint`
              - The interface defines methods and properties common to all points.

            * - :py:class:`~IVectorGeometryToolVector`
              - The interface defines methods and properties common to all vectors.

            * - :py:class:`~IVectorGeometryToolSystem`
              - The interface contains methods and properties shared by all VGT systems.

            * - :py:class:`~IVectorGeometryToolAxes`
              - The interface defines methods and properties common to all axes.

            * - :py:class:`~IVectorGeometryToolAngle`
              - The interface defines methods and properties common to all angles.

            * - :py:class:`~IVectorGeometryToolPlane`
              - The interface defines methods and properties common to all VGT planes.

            * - :py:class:`~IAnalysisWorkbenchContext`
              - The interface represents a context associated with a VGT component. All VGT components are associated with a valid context. A context can represent a VGT instance or a VGT template.

            * - :py:class:`~IAnalysisWorkbenchComponent`
              - A base interface implemented by all VGT components. The methods and properties of the interface provide type information about the VGT component.

            * - :py:class:`~ICalculationToolEvaluateResult`
              - Represents the results of evaluating a scalar component using IAgCrdnCalcScalar.Evaluate method.

            * - :py:class:`~ICalculationToolEvaluateWithRateResult`
              - Represents the results of evaluating a scalar component using IAgCrdnCalcScalar.Evaluate method.

            * - :py:class:`~ITimeToolEventIntervalResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :py:class:`~ITimeToolEventFindOccurrenceResult`
              - Contains the results returned with IAgCrdnEvent.FindOccurrence method.

            * - :py:class:`~ITimeToolFindTimesResult`
              - Return a collection of intervals and an array of times.

            * - :py:class:`~ITimeToolIntervalsVectorResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.FindIntervalCollection method.

            * - :py:class:`~ITimeToolEventIntervalCollectionOccurredResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.Occurred method.

            * - :py:class:`~ITimeToolIntervalListResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :py:class:`~ITimeToolIntervalVectorCollection`
              - A collection of interval collections.

            * - :py:class:`~ITimeToolEventGroup`
              - Access or create VGT events associated with an object.

            * - :py:class:`~ITimeToolEventIntervalGroup`
              - Access or create VGT event intervals associated with an object.

            * - :py:class:`~ITimeToolEventIntervalListGroup`
              - Access or create VGT event interval lists associated with an object.

            * - :py:class:`~ITimeToolEventArrayGroup`
              - Access or create VGT event arrays associated with an object.

            * - :py:class:`~ICalculationToolScalarGroup`
              - Access or create VGT calculation scalars associated with an object or a central body.

            * - :py:class:`~ITimeToolEventIntervalCollectionGroup`
              - Access or create VGT event interval collections associated with an object.

            * - :py:class:`~ICalculationToolParameterSetGroup`
              - Access or create VGT parameter sets associated with an object or a central body.

            * - :py:class:`~ICalculationToolConditionGroup`
              - Access or create VGT conditions associated with an object or a central body.

            * - :py:class:`~ICalculationToolConditionSetGroup`
              - Allow accessing and creating condition set components.

            * - :py:class:`~ICalculationToolConditionSetEvaluateResult`
              - Represents the results returned by ConditionSet.Evaluate.

            * - :py:class:`~ICalculationToolConditionSetEvaluateWithRateResult`
              - Represents the results returned by ConditionSet.EvaluateWithRate.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridGroup`
              - Access or create VGT volume grids associated with an object or a central body.

            * - :py:class:`~ISpatialAnalysisToolVolumeGroup`
              - Access or create spatial conditions associated with a volume grid.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcGroup`
              - Access or create VGT volume calcs associated with an object or a central body.

            * - :py:class:`~ICalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :py:class:`~ICalculationToolScalarAngle`
              - Scalar equal to angular displacement obtained from any angle in VGT.

            * - :py:class:`~ICalculationToolScalarAverage`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ICalculationToolScalarConstant`
              - Constant scalar value of specified dimension.

            * - :py:class:`~ICalculationToolScalarCustom`
              - A calc scalar based on a scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

            * - :py:class:`~ICalculationToolScalarCustomInline`
              - A calc scalar based on using an inline scripted algorithm in MATLAB, Perl, VBScript or JScript to define its value and rate.

            * - :py:class:`~ICalculationToolScalarDataElement`
              - Any time-dependent data element from STK data providers available for parent STK object.

            * - :py:class:`~ICalculationToolScalarDerivative`
              - Derivative of an input scalar calculation.

            * - :py:class:`~ICalculationToolScalarDotProduct`
              - Dot product between two vectors.

            * - :py:class:`~ICalculationToolScalarElapsedTime`
              - Time elapsed since the reference time instant. Negative if in the past.

            * - :py:class:`~ICalculationToolScalarFactory`
              - The factory creates scalar calculation components.

            * - :py:class:`~ICalculationToolScalarFile`
              - Tabulated scalar calculation data loaded from specified file - a file with .csc extension.

            * - :py:class:`~ICalculationToolScalarFixedAtTimeInstant`
              - Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

            * - :py:class:`~ICalculationToolScalarFunction`
              - Defined by performing the specified function on the input scalar or time instant.

            * - :py:class:`~ICalculationToolScalarFunction2Var`
              - Defined by performing a function(x,y) on two scalar arguments.

            * - :py:class:`~ICalculationToolScalarIntegral`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ICalculationToolScalarPlugin`
              - Use a scalar calculation plugin.

            * - :py:class:`~ICalculationToolScalarPointInVolumeCalc`
              - Scalar value of spatial calculation evaluated along trajectory of point.

            * - :py:class:`~ICalculationToolScalarStandardDeviation`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ICalculationToolScalarSurfaceDistanceBetweenPoints`
              - Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

            * - :py:class:`~ICalculationToolScalarVectorComponent`
              - The specified component of a vector when resolved in the specified axes.

            * - :py:class:`~ICalculationToolScalarVectorMagnitude`
              - Scalar equal to the magnitude of a specified vector.

            * - :py:class:`~ICalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :py:class:`~ICalculationToolConditionCombined`
              - Define a condition which combines multiple conditions.

            * - :py:class:`~ICalculationToolConditionFactory`
              - The factory creates condition components.

            * - :py:class:`~ICalculationToolConditionPointInVolume`
              - Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

            * - :py:class:`~ICalculationToolConditionScalarBounds`
              - Defined by determining if input scalar is within specified bounds; returns +1 if satisfied, -1 if not satisfied and 0 if on boundary.

            * - :py:class:`~ICalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :py:class:`~ICalculationToolConditionSetFactory`
              - The factory creates condition set components.

            * - :py:class:`~ICalculationToolConditionSetScalarThresholds`
              - Condition set based on single scalar calculation compared to set of threshold values.

            * - :py:class:`~IAnalysisWorkbenchConverge`
              - Represents a base class for convergence definitions.

            * - :py:class:`~ICalculationToolConvergeBasic`
              - Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

            * - :py:class:`~IAnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :py:class:`~ICalculationToolDerivativeBasic`
              - Derivative definition determines how numerical differencing is used to compute derivatives.

            * - :py:class:`~ITimeToolEvent`
              - Define an event (time instant).

            * - :py:class:`~ITimeToolEventArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :py:class:`~ITimeToolEventArrayConditionCrossings`
              - Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

            * - :py:class:`~ITimeToolEventArrayExtrema`
              - Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ITimeToolEventArrayFactory`
              - The factory creates event arrays.

            * - :py:class:`~ITimeToolEventArrayFiltered`
              - Defined by filtering times from original time array according to specified filtering method.

            * - :py:class:`~ITimeToolEventArrayFixedStep`
              - Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

            * - :py:class:`~ITimeToolEventArrayFixedTimes`
              - Array defined by time ordered instants each explicitly specified.

            * - :py:class:`~ITimeToolEventArrayMerged`
              - Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

            * - :py:class:`~ITimeToolEventArraySignaled`
              - Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations...

            * - :py:class:`~ITimeToolEventArrayStartStopTimes`
              - Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

            * - :py:class:`~ITimeToolEventEpoch`
              - Event set at specified date/time.

            * - :py:class:`~ITimeToolEventExtremum`
              - Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ITimeToolEventFactory`
              - The factory creates events.

            * - :py:class:`~ITimeToolEventInterval`
              - A single time interval.

            * - :py:class:`~ITimeToolEventIntervalBetweenTimeInstants`
              - Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

            * - :py:class:`~ITimeToolEventIntervalCollection`
              - A collection of related interval lists.

            * - :py:class:`~ITimeToolEventIntervalCollectionCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ITimeToolEventIntervalCollectionFactory`
              - The factory creates collections of event interval lists.

            * - :py:class:`~ITimeToolEventIntervalCollectionLighting`
              - Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

            * - :py:class:`~ITimeToolEventIntervalCollectionSignaled`
              - Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

            * - :py:class:`~ITimeToolEventIntervalFactory`
              - The factory creates event intervals.

            * - :py:class:`~ITimeToolEventIntervalFixed`
              - Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

            * - :py:class:`~ITimeToolEventIntervalFixedDuration`
              - Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

            * - :py:class:`~ITimeToolEventIntervalFromIntervalList`
              - Interval created from specified interval list by using one of several selection methods.

            * - :py:class:`~ITimeToolEventIntervalList`
              - An ordered list of time intervals.

            * - :py:class:`~ITimeToolEventIntervalListCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ITimeToolEventIntervalListFactory`
              - The factory creates event interval lists.

            * - :py:class:`~ITimeToolEventIntervalListFile`
              - Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

            * - :py:class:`~ITimeToolEventIntervalListFiltered`
              - Defined by filtering intervals from original interval list using specified filtering method.

            * - :py:class:`~ITimeToolEventIntervalListFixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

            * - :py:class:`~ITimeToolEventIntervalListMerged`
              - Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

            * - :py:class:`~ITimeToolEventIntervalListScaled`
              - Interval List defined by scaling every interval in original interval list using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval is removed from scaled list...

            * - :py:class:`~ITimeToolEventIntervalListSignaled`
              - Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

            * - :py:class:`~ITimeToolEventIntervalListTimeOffset`
              - Interval List defined by shifting the specified reference interval list by a fixed time offset.

            * - :py:class:`~ITimeToolEventIntervalScaled`
              - Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

            * - :py:class:`~ITimeToolEventIntervalSignaled`
              - Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

            * - :py:class:`~ITimeToolEventIntervalSmartInterval`
              - A smart interval.

            * - :py:class:`~ITimeToolEventIntervalTimeOffset`
              - Interval defined by shifting specified reference interval by fixed time offset.

            * - :py:class:`~ITimeToolEventSignaled`
              - Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

            * - :py:class:`~ITimeToolEventSmartEpoch`
              - A smart epoch.

            * - :py:class:`~ITimeToolEventStartStopTime`
              - Event is either start or stop time selected from a reference interval.

            * - :py:class:`~ITimeToolEventTimeOffset`
              - Event at fixed offset from specified reference event.

            * - :py:class:`~ITimeToolFirstIntervalsFilter`
              - The filter selects a portion of first intervals.

            * - :py:class:`~ITimeToolGapsFilter`
              - The filter merges intervals unless they are separated by gaps of at least/most certain duration.

            * - :py:class:`~IAnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :py:class:`~ICalculationToolIntegralBasic`
              - Integral definition determines how scalar calculation is numerically integrated.

            * - :py:class:`~IAnalysisWorkbenchInterp`
              - Represents a base class for interpolation definitions.

            * - :py:class:`~ICalculationToolInterpBasic`
              - Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

            * - :py:class:`~ITimeToolIntervalsFilter`
              - The filter selects intervals of at least/most certain duration.

            * - :py:class:`~ITimeToolLastIntervalsFilter`
              - The filter selects a portion of last intervals.

            * - :py:class:`~ICalculationToolParameterSet`
              - Parameter set contains various sets of scalar computations.

            * - :py:class:`~ICalculationToolParameterSetAttitude`
              - Attitude parameter set contains various representations of attitude of one set of axes relative to another.

            * - :py:class:`~ICalculationToolParameterSetFactory`
              - The factory is used to create instances of available parameter set types.

            * - :py:class:`~ICalculationToolParameterSetGroundTrajectory`
              - Ground trajectory parameter set contains various representations of trajectory of a point relative to central body reference shape.

            * - :py:class:`~ICalculationToolParameterSetOrbit`
              - Orbit parameter set contains various trajectory representations of an orbiting point.

            * - :py:class:`~ICalculationToolParameterSetTrajectory`
              - Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

            * - :py:class:`~ICalculationToolParameterSetVector`
              - Vector parameter set contains various representations of a vector in a reference set of axes.

            * - :py:class:`~ITimeToolPruneFilter`
              - A filter used with event interval list pruned class to prune interval lists...

            * - :py:class:`~ITimeToolPruneFilterFactory`
              - The factory creates pruning filters.

            * - :py:class:`~ITimeToolRelativeSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

            * - :py:class:`~IAnalysisWorkbenchSampling`
              - Base sampling interface.

            * - :py:class:`~ICalculationToolSamplingBasic`
              - Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

            * - :py:class:`~ICalculationToolSamplingCurvatureTolerance`
              - Curvature tolerance definition includes parameters that determine how scalar data should be sampled based on limits on slope changes between samples.

            * - :py:class:`~ICalculationToolSamplingFixedStep`
              - Fixed step definition includes parameters that determine how scalar data should be sampled based on fixed steps between samples.

            * - :py:class:`~ICalculationToolSamplingMethod`
              - A sampling method.

            * - :py:class:`~ICalculationToolSamplingMethodFactory`
              - The factory creates sampling method components.

            * - :py:class:`~ICalculationToolSamplingRelativeTolerance`
              - Relative tolerance definition includes parameters that determine how scalar data should be sampled based on limits on difference between actual changes between samples and changes predicted by dead reckoning.

            * - :py:class:`~ITimeToolSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain duration.

            * - :py:class:`~IAnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ITimeToolSignalDelayBasic`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcFactory`
              - The factory is used to create instances of volume calcs.

            * - :py:class:`~ISpatialAnalysisToolVolumeFactory`
              - The factory is used to create instances of volumes.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridFactory`
              - The factory is used to create instances of volume grids.

            * - :py:class:`~ISpatialAnalysisToolGridCoordinateDefinition`
              - Define a set of coordinate values.

            * - :py:class:`~ISpatialAnalysisToolGridValuesCustom`
              - Fixed step grid values.

            * - :py:class:`~ISpatialAnalysisToolGridValuesFixedNumberOfSteps`
              - Fixed step grid values.

            * - :py:class:`~ISpatialAnalysisToolGridValuesFixedStep`
              - Fixed step grid values.

            * - :py:class:`~ISpatialAnalysisToolGridValuesMethod`
              - A grid values method.

            * - :py:class:`~ITimeToolLightTimeDelay`
              - Manage Light Time Delay options..

            * - :py:class:`~ISpatialAnalysisToolVolume`
              - A volume interface. The methods and properties of the interface provide Volume functions.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalc`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcAltitude`
              - A volume calc altitude interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcAngleOffVector`
              - A volume calc angle off vector interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcConditionSatMetric`
              - A volume calc condition satisfaction interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcDelayRange`
              - A volume calc propagation delay to location interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcFile`
              - Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcFromScalar`
              - A volume calc scalar to location interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcRange`
              - A volume calc distance to location interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeCalcSolarIntensity`
              - A volume calc solar intensityn interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeCombined`
              - A combined volume interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeFromCalc`
              - An volume from calc volume interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeFromCondition`
              - A volume from conditioninterface.

            * - :py:class:`~ISpatialAnalysisToolVolumeFromGrid`
              - An over time volume interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeFromTimeSatisfaction`
              - An volume from time satisfaction volume interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridBearingAlt`
              - A volume grid bearing alt (Surface Bearing) interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridCartesian`
              - A volume grid Cartesian interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridConstrained`
              - A volume grid constrained interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridCylindrical`
              - A volume grid cylindrical interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridLatLonAlt`
              - A volume grid lat lon alt (Cartogrographic) interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridResult`
              - An interface that generates Volume Grid results.

            * - :py:class:`~ISpatialAnalysisToolVolumeGridSpherical`
              - A volume grid spherical interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeInview`
              - An Inview volume interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeLighting`
              - A lighting volume interface.

            * - :py:class:`~ISpatialAnalysisToolVolumeOverTime`
              - An over time volume interface.

            * - :py:class:`~ITimeToolTimeProperties`
              - Define methods to compute time properties such as availability and special times.

            * - :py:class:`~IAnalysisWorkbenchTypeInfo`
              - Provide information about the type of VGT components.

            * - :py:class:`~IAnalysisWorkbenchRefTo`
              - A base interface for all VGT component references.

            * - :py:class:`~IAnalysisWorkbenchTemplate`
              - The IAgCrdnTemplate interface enables to obtain information about the STK class that owns the VGT component.

            * - :py:class:`~IAnalysisWorkbenchInstance`
              - The IAgCrdnInstance interface enables to obtain information about the parent object that owns the VGT component.

            * - :py:class:`~IVectorGeometryToolPointRefTo`
              - Represents a reference to a VGT point.

            * - :py:class:`~IVectorGeometryToolVectorRefTo`
              - Represents a reference to a VGT vector.

            * - :py:class:`~IVectorGeometryToolAxesRefTo`
              - Represents a reference to a VGT axes.

            * - :py:class:`~IVectorGeometryToolAngleRefTo`
              - Represents a reference to a VGT angle.

            * - :py:class:`~IVectorGeometryToolSystemRefTo`
              - Represents a reference to a VGT system.

            * - :py:class:`~IVectorGeometryToolPlaneRefTo`
              - Represents a reference to a VGT plane.

            * - :py:class:`~IVectorGeometryToolAxesLabels`
              - Allow configuring the VGT axes labels.

            * - :py:class:`~IVectorGeometryToolPlaneLabels`
              - Allow configuring the X and Y axes labels.

            * - :py:class:`~IVectorGeometryToolAxesAlignedAndConstrained`
              - Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

            * - :py:class:`~IVectorGeometryToolAxesAngularOffset`
              - Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

            * - :py:class:`~IVectorGeometryToolAxesFixedAtEpoch`
              - Axes based on another set fixed at a specified epoch.

            * - :py:class:`~IVectorGeometryToolAxesBPlane`
              - B-Plane axes using the selected target body and reference vector.

            * - :py:class:`~IVectorGeometryToolAxesCustomScript`
              - Customized axes offset with respect to a set of reference Axes.

            * - :py:class:`~IVectorGeometryToolAxesAttitudeFile`
              - Axes specified by data from a file.

            * - :py:class:`~IVectorGeometryToolAxesFixed`
              - Axes fixed in reference axes.

            * - :py:class:`~IVectorGeometryToolAxesModelAttach`
              - Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

            * - :py:class:`~IVectorGeometryToolAxesSpinning`
              - Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

            * - :py:class:`~IVectorGeometryToolAxesOnSurface`
              - Topocentric axes located at the reference point's projection on the central body.

            * - :py:class:`~IVectorGeometryToolAxesTrajectory`
              - Axes based on trajectory of the point relative to the reference coordinate system.

            * - :py:class:`~IVectorGeometryToolAxesLagrangeLibration`
              - Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

            * - :py:class:`~IVectorGeometryToolAxesCommonTasks`
              - Provide methods to create non-persistent VGT axes components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~IVectorGeometryToolAxesAtTimeInstant`
              - Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

            * - :py:class:`~IVectorGeometryToolAxesPlugin`
              - A VGT axes plugin.

            * - :py:class:`~IVectorGeometryToolAngleBetweenVectors`
              - An angle between two vectors.

            * - :py:class:`~IVectorGeometryToolAngleBetweenPlanes`
              - An angle between two planes.

            * - :py:class:`~IVectorGeometryToolAngleDihedral`
              - An angle between two vectors about an axis.

            * - :py:class:`~IVectorGeometryToolAngleRotation`
              - Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

            * - :py:class:`~IVectorGeometryToolAngleToPlane`
              - An angle between a vector and a plane.

            * - :py:class:`~IVectorGeometryToolPlaneNormal`
              - A plane normal to a vector at a given point.

            * - :py:class:`~IVectorGeometryToolPlaneQuadrant`
              - A plane based on a selected Quadrant of a reference system.

            * - :py:class:`~IVectorGeometryToolPlaneTrajectory`
              - The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

            * - :py:class:`~IVectorGeometryToolPlaneTriad`
              - A Plane containing points A, B and ReferencePont with the first axis aligned with the direction from the ReferencePoint to point A and the second axis toward the direction from the ReferencePoint to point B.

            * - :py:class:`~IVectorGeometryToolPlaneTwoVector`
              - A plane passing through point and containing two given vectors.

            * - :py:class:`~IVectorGeometryToolPointBPlane`
              - B-Plane point using the selected target body.

            * - :py:class:`~IVectorGeometryToolPointFile`
              - Point specified by data from a file.

            * - :py:class:`~IVectorGeometryToolPointFixedInSystem`
              - Point fixed in a reference coordinate system using the selected coordinate type.

            * - :py:class:`~IVectorGeometryToolPointGrazing`
              - The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

            * - :py:class:`~IVectorGeometryToolPointGlint`
              - Point on central body surface that reflects from source to observer.

            * - :py:class:`~IVectorGeometryToolPointCovarianceGrazing`
              - The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

            * - :py:class:`~IVectorGeometryToolPointPlaneIntersection`
              - Point on a plane located along a given direction looking from a given origin.

            * - :py:class:`~IVectorGeometryToolPointOnSurface`
              - The detic subpoint of the reference point as projected onto the central body.

            * - :py:class:`~IVectorGeometryToolPointModelAttach`
              - A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

            * - :py:class:`~IVectorGeometryToolPointSatelliteCollectionEntry`
              - A point placed at the center of mass of a specified satellite of the satellite collection.

            * - :py:class:`~IVectorGeometryToolPointPlaneProjection`
              - The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

            * - :py:class:`~IVectorGeometryToolPointLagrangeLibration`
              - Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

            * - :py:class:`~IVectorGeometryToolPointCommonTasks`
              - Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~IVectorGeometryToolPointCentBodyIntersect`
              - Point on central body surface along direction vector originating at source point.

            * - :py:class:`~IVectorGeometryToolPointAtTimeInstant`
              - Point fixed relative to reference system based on another point evaluated at specified time instant.

            * - :py:class:`~IVectorGeometryToolPointPlugin`
              - A VGT point plugin.

            * - :py:class:`~IVectorGeometryToolPointCBFixedOffset`
              - Point specified by fixed components with respect to central body.

            * - :py:class:`~IVectorGeometryToolSystemAssembled`
              - A system assembled from an origin point and a set of reference axes.

            * - :py:class:`~IVectorGeometryToolSystemOnSurface`
              - A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

            * - :py:class:`~IAnalysisWorkbenchLLAPosition`
              - A position represented by the Latitude, longtitude and Latitude.

            * - :py:class:`~IVectorGeometryToolSystemCommonTasks`
              - Provide methods to create non-persistent VGT coordinate reference frames (systems). Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~IVectorGeometryToolVectorAngleRate`
              - Angle rate vector perpendicular to the plane in which the angle is defined.

            * - :py:class:`~IVectorGeometryToolVectorApoapsis`
              - Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~IVectorGeometryToolVectorFixedAtEpoch`
              - A vector based on another vector fixed at a specified epoch.

            * - :py:class:`~IVectorGeometryToolVectorAngularVelocity`
              - Angular velocity vector of one set of axes computed with respect to the reference set.

            * - :py:class:`~IVectorGeometryToolVectorConing`
              - Vector created by revolving the Reference vector around the About vector with the specified rate.

            * - :py:class:`~IVectorGeometryToolVectorCross`
              - The vector cross product of two vectors.

            * - :py:class:`~IVectorGeometryToolVectorCustomScript`
              - Customized vector components defined with respect to reference axes.

            * - :py:class:`~IVectorGeometryToolVectorDerivative`
              - A vector derivative of a vector computed with respect to specified axes.

            * - :py:class:`~IVectorGeometryToolVectorDisplacement`
              - Vector defined by its start and end points.

            * - :py:class:`~IVectorGeometryToolVectorTwoPlanesIntersection`
              - Defined along the intersection of two planes.

            * - :py:class:`~IVectorGeometryToolVectorModelAttach`
              - Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

            * - :py:class:`~IVectorGeometryToolVectorProjection`
              - A projection of a vector computed with respect to a reference plane.

            * - :py:class:`~IVectorGeometryToolVectorScaled`
              - Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

            * - :py:class:`~IVectorGeometryToolVectorEccentricity`
              - A vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~IVectorGeometryToolVectorFixedInAxes`
              - Vector fixed in the reference axes using the selected coordinate type.

            * - :py:class:`~IVectorGeometryToolVectorLineOfNodes`
              - Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

            * - :py:class:`~IVectorGeometryToolVectorOrbitAngularMomentum`
              - Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:class:`~IVectorGeometryToolVectorOrbitNormal`
              - Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:class:`~IVectorGeometryToolVectorPeriapsis`
              - Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~IVectorGeometryToolVectorReflection`
              - A vector (incident vector) reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

            * - :py:class:`~IVectorGeometryToolVectorRotationVector`
              - Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

            * - :py:class:`~IVectorGeometryToolVectorDirectionToStar`
              - Defined with respect to a star object. For a star object to be available, you must first create one.

            * - :py:class:`~IVectorGeometryToolVectorFixedAtTimeInstant`
              - Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

            * - :py:class:`~IVectorGeometryToolVectorLinearCombination`
              - Linear combination of two input vectors.

            * - :py:class:`~IVectorGeometryToolVectorProjectAlongVector`
              - A projection of a source vector in the direction of another vector.

            * - :py:class:`~IVectorGeometryToolVectorScalarLinearCombination`
              - Linear combination of two input vectors using scalars.

            * - :py:class:`~IVectorGeometryToolVectorScalarScaled`
              - Scaled version of the input vector using scalar.

            * - :py:class:`~IVectorGeometryToolVectorVelocityAcceleration`
              - Velocity vector of a point in a coordinate system.

            * - :py:class:`~IVectorGeometryToolVectorPlugin`
              - A VGT vector plugin.

            * - :py:class:`~IVectorGeometryToolVectorDispSurface`
              - Displacement between origin and destination points using surface distance and altitude difference.

            * - :py:class:`~IVectorGeometryToolVectorFactory`
              - A Factory object to create vectors.

            * - :py:class:`~IVectorGeometryToolAxesFactory`
              - A Factory object to create axes.

            * - :py:class:`~IVectorGeometryToolSystemFactory`
              - A Factory interface to create VGT systems.

            * - :py:class:`~IVectorGeometryToolPointFactory`
              - A Factory object to create points.

            * - :py:class:`~IVectorGeometryToolPlaneFactory`
              - A Factory object to create VGT planes.

            * - :py:class:`~IVectorGeometryToolAngleFactory`
              - A Factory object to create angles.

            * - :py:class:`~IVectorGeometryToolVectorGroup`
              - Access or create VGT vectors associated with an object or a central body.

            * - :py:class:`~IVectorGeometryToolPointGroup`
              - Access or create VGT points associated with an object or a central body.

            * - :py:class:`~IVectorGeometryToolAngleGroup`
              - Access or create VGT angles associated with an object or a central body.

            * - :py:class:`~IVectorGeometryToolAxesGroup`
              - Access or create VGT axes associated with an object or a central body.

            * - :py:class:`~IVectorGeometryToolPlaneGroup`
              - Represents a single entry point to manipulate VGT Planes associated with an object.

            * - :py:class:`~IVectorGeometryToolSystemGroup`
              - Access or create VGT systems associated with an object or a central body.

            * - :py:class:`~IAnalysisWorkbenchProvider`
              - Allow accessing existing Vector Geometry Tool components.

            * - :py:class:`~IAnalysisWorkbenchRoot`
              - Represents a VGT root object.

            * - :py:class:`~IVectorGeometryToolWellKnownEarthSystems`
              - Well-known Earth's coordinate systems.

            * - :py:class:`~IVectorGeometryToolWellKnownEarthAxes`
              - Well-known Earth's axes.

            * - :py:class:`~IVectorGeometryToolWellKnownSunSystems`
              - The Sun's well-known coordinate reference systems.

            * - :py:class:`~IVectorGeometryToolWellKnownSunAxes`
              - Well-known Sun's axes.

            * - :py:class:`~IVectorGeometryToolWellKnownSystems`
              - Well-known coordinate reference systems.

            * - :py:class:`~IVectorGeometryToolWellKnownAxes`
              - Well-known Axes.

            * - :py:class:`~IVectorGeometryToolAngleFindAngleResult`
              - Contains the results returned with IAgCrdnAngle.FindAngle method.

            * - :py:class:`~IVectorGeometryToolAngleFindAngleWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindAngleWithRate method.

            * - :py:class:`~IVectorGeometryToolAngleFindWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinatesWithRate method.

            * - :py:class:`~IVectorGeometryToolAngleFindResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinates method.

            * - :py:class:`~IVectorGeometryToolAxesTransformResult`
              - Contains the results returned with IAgCrdnAxes.TransformFrom method.

            * - :py:class:`~IVectorGeometryToolAxesTransformWithRateResult`
              - Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

            * - :py:class:`~IVectorGeometryToolPlaneFindInAxesResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxes method.

            * - :py:class:`~IVectorGeometryToolPlaneFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxesWithRate method.

            * - :py:class:`~IVectorGeometryToolPlaneFindInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystem method.

            * - :py:class:`~IVectorGeometryToolPlaneFindInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :py:class:`~IVectorGeometryToolAxesFindInAxesResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxes method.

            * - :py:class:`~IVectorGeometryToolAxesFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxesWithRate method.

            * - :py:class:`~IVectorGeometryToolPointLocateInSystemResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystem method.

            * - :py:class:`~IVectorGeometryToolPointLocateInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystemWithRate method.

            * - :py:class:`~IVectorGeometryToolSystemTransformResult`
              - Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

            * - :py:class:`~IVectorGeometryToolSystemTransformWithRateResult`
              - Contains the results returned with IAgCrdnSystem.TransformFromWithRate and IAgCrdnSystem.TransformToWithRate methods.

            * - :py:class:`~IVectorGeometryToolSystemFindInSystemResult`
              - Contains the results returned with IAgCrdnSystem.FindInSystem method.

            * - :py:class:`~IVectorGeometryToolVectorFindInAxesResult`
              - Contains the results returned with IAgCrdnVector.FindInAxes method.

            * - :py:class:`~IVectorGeometryToolVectorFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnVector.FindInAxesWithRate method.

            * - :py:class:`~IAnalysisWorkbenchMethodCallResult`
              - Instances of the interface are used to return the result of a computation.

            * - :py:class:`~IAnalysisWorkbenchCentralBody`
              - The interface represents a central body.

            * - :py:class:`~IAnalysisWorkbenchCentralBodyRefTo`
              - Represents a reference to a VGT CentralBody.

            * - :py:class:`~IAnalysisWorkbenchCentralBodyCollection`
              - A collection of central body names.

            * - :py:class:`~IAnalysisWorkbenchCollection`
              - A collection of VGT objects.

            * - :py:class:`~ITimeToolPointSamplingResult`
              - Contains tabulated positions and velocities of a point created by Sample method.

            * - :py:class:`~ITimeToolPointSamplingInterval`
              - The interface represents an interval with the time, position and velocity arrays.

            * - :py:class:`~ITimeToolPointSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, position and velocity arrays.

            * - :py:class:`~ITimeToolAxesSamplingResult`
              - Contains tabulated orientations and angular velocities of axes created by Sample method.

            * - :py:class:`~ITimeToolAxesSamplingInterval`
              - The interface represents an interval with the time, orientation and velocity arrays.

            * - :py:class:`~ITimeToolAxesSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, orientation and velocity arrays.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~CalculationToolEvaluateResult`
              - Represents the results of evaluating a scalar component.

            * - :py:class:`~CalculationToolEvaluateWithRateResult`
              - Represents the results of evaluating a scalar component.

            * - :py:class:`~TimeToolEventIntervalResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :py:class:`~TimeToolEventFindOccurrenceResult`
              - Contains the results returned with IAgCrdnEvent.FindOccurrence method.

            * - :py:class:`~TimeToolFindTimesResult`
              - Return a collection of intervals and an array of times.

            * - :py:class:`~TimeToolIntervalsVectorResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.FindIntervalCollection method.

            * - :py:class:`~TimeToolEventIntervalCollectionOccurredResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.Occurred method.

            * - :py:class:`~TimeToolIntervalListResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :py:class:`~TimeToolIntervalVectorCollection`
              - A collection of interval collections.

            * - :py:class:`~TimeToolEventGroup`
              - Access or create VGT events associated with an object.

            * - :py:class:`~TimeToolEventIntervalGroup`
              - Access or create VGT event intervals associated with an object.

            * - :py:class:`~TimeToolEventIntervalListGroup`
              - Access or create VGT event interval lists associated with an object.

            * - :py:class:`~TimeToolEventArrayGroup`
              - Access or create VGT event arrays associated with an object.

            * - :py:class:`~CalculationToolScalarGroup`
              - Access or create VGT calculation scalars associated with an object or a central body.

            * - :py:class:`~TimeToolEventIntervalCollectionGroup`
              - Access or create VGT event interval collections associated with an object.

            * - :py:class:`~CalculationToolParameterSetGroup`
              - Access or create VGT parameter sets associated with an object or a central body.

            * - :py:class:`~CalculationToolConditionGroup`
              - Access or create VGT conditions associated with an object or a central body.

            * - :py:class:`~CalculationToolConditionSetGroup`
              - Allow accessing and creating condition set components.

            * - :py:class:`~CalculationToolConditionSetEvaluateResult`
              - Represents the results returned by ConditionSet.Evaluate.

            * - :py:class:`~CalculationToolConditionSetEvaluateWithRateResult`
              - Represents the results returned by ConditionSet.EvaluateWithRate.

            * - :py:class:`~SpatialAnalysisToolVolumeGridGroup`
              - Access or create VGT volume grids associated with an object or a central body.

            * - :py:class:`~SpatialAnalysisToolVolumeGroup`
              - Access or create spatial conditions associated with a volume grid.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcGroup`
              - Access or create VGT volume calc associated with an object or a central body.

            * - :py:class:`~CalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :py:class:`~CalculationToolScalarAngle`
              - Scalar equal to angular displacement obtained from any angle in VGT.

            * - :py:class:`~CalculationToolScalarAverage`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~CalculationToolScalarConstant`
              - Constant scalar value of specified dimension.

            * - :py:class:`~CalculationToolScalarCustom`
              - A calc scalar based on a scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

            * - :py:class:`~CalculationToolScalarCustomInline`
              - A calc scalar based on using an inline scripted algorithm in MATLAB, Perl, VBScript or JScript to define its value and rate.

            * - :py:class:`~CalculationToolScalarDataElement`
              - Any time-dependent data element from STK data providers available for parent STK object.

            * - :py:class:`~CalculationToolScalarDerivative`
              - Derivative of an input scalar calculation.

            * - :py:class:`~CalculationToolScalarDotProduct`
              - Dot product between two vectors.

            * - :py:class:`~CalculationToolScalarElapsedTime`
              - Time elapsed since the reference time instant. Negative if in the past.

            * - :py:class:`~CalculationToolScalarFactory`
              - The factory creates scalar calculation components.

            * - :py:class:`~CalculationToolScalarFile`
              - Tabulated scalar calculation data loaded from specified file - a file with .csc extension.

            * - :py:class:`~CalculationToolScalarFixedAtTimeInstant`
              - Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

            * - :py:class:`~CalculationToolScalarFunction`
              - Defined by performing the specified function on the input scalar or time instant.

            * - :py:class:`~CalculationToolScalarFunction2Var`
              - Defined by performing a function(x,y) on two scalar arguments.

            * - :py:class:`~CalculationToolScalarIntegral`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~CalculationToolScalarPlugin`
              - Use a scalar calculation plugin.

            * - :py:class:`~CalculationToolScalarPointInVolumeCalc`
              - Scalar value of spatial calculation evaluated along trajectory of point.

            * - :py:class:`~CalculationToolScalarStandardDeviation`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~CalculationToolScalarSurfaceDistanceBetweenPoints`
              - Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

            * - :py:class:`~CalculationToolScalarVectorComponent`
              - The specified component of a vector when resolved in the specified axes.

            * - :py:class:`~CalculationToolScalarVectorMagnitude`
              - Scalar equal to the magnitude of a specified vector.

            * - :py:class:`~CalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :py:class:`~CalculationToolConditionCombined`
              - Define a condition which combines multiple conditions.

            * - :py:class:`~CalculationToolConditionFactory`
              - The factory creates condition components.

            * - :py:class:`~CalculationToolConditionPointInVolume`
              - Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

            * - :py:class:`~CalculationToolConditionScalarBounds`
              - Defined by determining if input scalar is within specified bounds; returns +1 if satisfied, -1 if not satisfied and 0 if on boundary.

            * - :py:class:`~CalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :py:class:`~CalculationToolConditionSetFactory`
              - The factory creates condition set components.

            * - :py:class:`~CalculationToolConditionSetScalarThresholds`
              - Condition set based on single scalar calculation compared to set of threshold values.

            * - :py:class:`~AnalysisWorkbenchConverge`
              - Represents a base class for convergence definitions.

            * - :py:class:`~CalculationToolConvergeBasic`
              - Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

            * - :py:class:`~AnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :py:class:`~CalculationToolDerivativeBasic`
              - Derivative definition determines how numerical differencing is used to compute derivatives.

            * - :py:class:`~TimeToolEvent`
              - Define an event (time instant).

            * - :py:class:`~TimeToolEventArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :py:class:`~TimeToolEventArrayConditionCrossings`
              - Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

            * - :py:class:`~TimeToolEventArrayExtrema`
              - Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~TimeToolEventArrayFactory`
              - The factory creates event arrays.

            * - :py:class:`~TimeToolEventArrayFiltered`
              - Defined by filtering times from original time array according to specified filtering method.

            * - :py:class:`~TimeToolEventArrayFixedStep`
              - Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

            * - :py:class:`~TimeToolEventArrayFixedTimes`
              - Array defined by time ordered instants each explicitly specified.

            * - :py:class:`~TimeToolEventArrayMerged`
              - Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

            * - :py:class:`~TimeToolEventArraySignaled`
              - Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations...

            * - :py:class:`~TimeToolEventArrayStartStopTimes`
              - Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

            * - :py:class:`~TimeToolEventEpoch`
              - Event set at specified date/time.

            * - :py:class:`~TimeToolEventExtremum`
              - Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~TimeToolEventFactory`
              - The factory creates events.

            * - :py:class:`~TimeToolEventInterval`
              - A single time interval.

            * - :py:class:`~TimeToolEventIntervalBetweenTimeInstants`
              - Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

            * - :py:class:`~TimeToolEventIntervalCollection`
              - A collection of related interval lists.

            * - :py:class:`~TimeToolEventIntervalCollectionCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~TimeToolEventIntervalCollectionFactory`
              - The factory creates collections of event interval lists.

            * - :py:class:`~TimeToolEventIntervalCollectionLighting`
              - Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

            * - :py:class:`~TimeToolEventIntervalCollectionSignaled`
              - Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

            * - :py:class:`~TimeToolEventIntervalFactory`
              - The factory creates event intervals.

            * - :py:class:`~TimeToolEventIntervalFixed`
              - Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

            * - :py:class:`~TimeToolEventIntervalFixedDuration`
              - Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

            * - :py:class:`~TimeToolEventIntervalFromIntervalList`
              - Interval created from specified interval list by using one of several selection methods.

            * - :py:class:`~TimeToolEventIntervalList`
              - An ordered list of time intervals.

            * - :py:class:`~TimeToolEventIntervalListCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~TimeToolEventIntervalListFactory`
              - The factory creates event interval lists.

            * - :py:class:`~TimeToolEventIntervalListFile`
              - Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

            * - :py:class:`~TimeToolEventIntervalListFiltered`
              - Defined by filtering intervals from original interval list using specified filtering method.

            * - :py:class:`~TimeToolEventIntervalListFixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

            * - :py:class:`~TimeToolEventIntervalListMerged`
              - Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

            * - :py:class:`~TimeToolEventIntervalListScaled`
              - Interval List defined by scaling every interval in original interval list using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval is removed from scaled list...

            * - :py:class:`~TimeToolEventIntervalListSignaled`
              - Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

            * - :py:class:`~TimeToolEventIntervalListTimeOffset`
              - Interval List defined by shifting the specified reference interval list by a fixed time offset.

            * - :py:class:`~TimeToolEventIntervalScaled`
              - Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

            * - :py:class:`~TimeToolEventIntervalSignaled`
              - Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

            * - :py:class:`~TimeToolEventIntervalSmartInterval`
              - A smart interval.

            * - :py:class:`~TimeToolEventIntervalTimeOffset`
              - Interval defined by shifting specified reference interval by fixed time offset.

            * - :py:class:`~TimeToolEventSignaled`
              - Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

            * - :py:class:`~TimeToolEventSmartEpoch`
              - A smart epoch.

            * - :py:class:`~TimeToolEventStartStopTime`
              - Event is either start or stop time selected from a reference interval.

            * - :py:class:`~TimeToolEventTimeOffset`
              - Event at fixed offset from specified reference event.

            * - :py:class:`~TimeToolFirstIntervalsFilter`
              - The filter selects a portion of first intervals.

            * - :py:class:`~TimeToolGapsFilter`
              - The filter merges intervals unless they are separated by gaps of at least/most certain duration.

            * - :py:class:`~AnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :py:class:`~CalculationToolIntegralBasic`
              - Integral definition determines how scalar calculation is numerically integrated.

            * - :py:class:`~AnalysisWorkbenchInterp`
              - Represents a base class for interpolation definitions.

            * - :py:class:`~CalculationToolInterpBasic`
              - Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

            * - :py:class:`~TimeToolIntervalsFilter`
              - The filter selects intervals of at least/most certain duration.

            * - :py:class:`~TimeToolLastIntervalsFilter`
              - The filter selects a portion of last intervals.

            * - :py:class:`~CalculationToolParameterSet`
              - Parameter set contains various sets of scalar computations.

            * - :py:class:`~CalculationToolParameterSetAttitude`
              - Attitude parameter set contains various representations of attitude of one set of axes relative to another.

            * - :py:class:`~CalculationToolParameterSetFactory`
              - The factory is used to create instances of available parameter set types.

            * - :py:class:`~CalculationToolParameterSetGroundTrajectory`
              - Ground trajectory parameter set contains various representations of trajectory of a point relative to central body reference shape.

            * - :py:class:`~CalculationToolParameterSetOrbit`
              - Orbit parameter set contains various trajectory representations of an orbiting point.

            * - :py:class:`~CalculationToolParameterSetTrajectory`
              - Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

            * - :py:class:`~CalculationToolParameterSetVector`
              - Vector parameter set contains various representations of a vector in a reference set of axes.

            * - :py:class:`~TimeToolPruneFilter`
              - A filter used with event interval list pruned class to prune interval lists...

            * - :py:class:`~TimeToolPruneFilterFactory`
              - The factory creates pruning filters.

            * - :py:class:`~TimeToolRelativeSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

            * - :py:class:`~AnalysisWorkbenchSampling`
              - Base sampling interface.

            * - :py:class:`~CalculationToolSamplingBasic`
              - Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

            * - :py:class:`~CalculationToolSamplingCurvatureTolerance`
              - Curvature tolerance definition includes parameters that determine how scalar data should be sampled based on limits on slope changes between samples.

            * - :py:class:`~CalculationToolSamplingFixedStep`
              - Fixed step definition includes parameters that determine how scalar data should be sampled based on fixed steps between samples.

            * - :py:class:`~CalculationToolSamplingMethod`
              - A sampling method.

            * - :py:class:`~CalculationToolSamplingMethodFactory`
              - The factory creates sampling method components.

            * - :py:class:`~CalculationToolSamplingRelativeTolerance`
              - Relative tolerance definition includes parameters that determine how scalar data should be sampled based on limits on difference between actual changes between samples and changes predicted by dead reckoning.

            * - :py:class:`~TimeToolSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain duration.

            * - :py:class:`~AnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~TimeToolSignalDelayBasic`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcFactory`
              - The factory is used to create instances of volume calcs.

            * - :py:class:`~SpatialAnalysisToolVolumeFactory`
              - The factory is used to create instances of volumes.

            * - :py:class:`~SpatialAnalysisToolVolumeGridFactory`
              - The factory is used to create instances of volume grids.

            * - :py:class:`~SpatialAnalysisToolGridCoordinateDefinition`
              - Define a set of coordinate values.

            * - :py:class:`~SpatialAnalysisToolGridValuesCustom`
              - Fixed step grid values.

            * - :py:class:`~SpatialAnalysisToolGridValuesFixedNumberOfSteps`
              - Fixed step grid values.

            * - :py:class:`~SpatialAnalysisToolGridValuesFixedStep`
              - Fixed step grid values.

            * - :py:class:`~SpatialAnalysisToolGridValuesMethod`
              - A grid values method.

            * - :py:class:`~TimeToolLightTimeDelay`
              - Manage Light Time Delay options..

            * - :py:class:`~SpatialAnalysisToolVolume`
              - A volume interface. The methods and properties of the interface provide Volume functions.

            * - :py:class:`~SpatialAnalysisToolVolumeCalc`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcAltitude`
              - A volume calc altitude interface.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcAngleOffVector`
              - A volume calc angle off vector interface.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcConditionSatMetric`
              - A volume calc condition satisfaction interface.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcDelayRange`
              - A volume calc propagation delay to location interface.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcFile`
              - Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcFromScalar`
              - A volume calc scalar to location interface.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcRange`
              - A volume calc distance to location interface.

            * - :py:class:`~SpatialAnalysisToolVolumeCalcSolarIntensity`
              - A volume calc solar intensityn interface.

            * - :py:class:`~SpatialAnalysisToolVolumeCombined`
              - A combined volume interface.

            * - :py:class:`~SpatialAnalysisToolVolumeFromCalc`
              - An volume from calc volume interface.

            * - :py:class:`~SpatialAnalysisToolVolumeFromCondition`
              - A volume from conditioninterface.

            * - :py:class:`~SpatialAnalysisToolVolumeFromGrid`
              - An over time volume interface.

            * - :py:class:`~SpatialAnalysisToolVolumeFromTimeSatisfaction`
              - An volume from time satisfaction volume interface.

            * - :py:class:`~SpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :py:class:`~SpatialAnalysisToolVolumeGridBearingAlt`
              - A volume grid bearing alt (Surface Bearing) interface.

            * - :py:class:`~SpatialAnalysisToolVolumeGridCartesian`
              - A volume grid Cartesian interface.

            * - :py:class:`~SpatialAnalysisToolVolumeGridConstrained`
              - A volume grid constrained interface.

            * - :py:class:`~SpatialAnalysisToolVolumeGridCylindrical`
              - A volume grid cylindrical interface.

            * - :py:class:`~SpatialAnalysisToolVolumeGridLatLonAlt`
              - A volume grid lat lon alt (Cartogrographic) interface.

            * - :py:class:`~SpatialAnalysisToolVolumeGridResult`
              - An interface that generates Volume Grid results.

            * - :py:class:`~SpatialAnalysisToolVolumeGridSpherical`
              - A volume grid spherical interface.

            * - :py:class:`~SpatialAnalysisToolVolumeInview`
              - An Inview volume interface.

            * - :py:class:`~SpatialAnalysisToolVolumeLighting`
              - A lighting volume interface.

            * - :py:class:`~SpatialAnalysisToolVolumeOverTime`
              - An over time volume interface.

            * - :py:class:`~AnalysisWorkbenchGeneric`
              - Generic VGT component.

            * - :py:class:`~AnalysisWorkbenchTypeInfo`
              - VGT component info.

            * - :py:class:`~AnalysisWorkbenchInstance`
              - Enable to obtain information about the parent object that owns the VGT component.

            * - :py:class:`~AnalysisWorkbenchTemplate`
              - Enable to obtain information about the STK class that owns the VGT component.

            * - :py:class:`~VectorGeometryToolPointRefTo`
              - Represents a reference to a VGT point.

            * - :py:class:`~VectorGeometryToolVectorRefTo`
              - Represents a vector reference.

            * - :py:class:`~VectorGeometryToolAxesRefTo`
              - Represents a reference to a VGT axes.

            * - :py:class:`~VectorGeometryToolAngleRefTo`
              - Represents a reference to a VGT angle.

            * - :py:class:`~VectorGeometryToolSystemRefTo`
              - Represents a System reference.

            * - :py:class:`~VectorGeometryToolPlaneRefTo`
              - Represents a Plane reference.

            * - :py:class:`~VectorGeometryToolVector`
              - A generic vector class.

            * - :py:class:`~VectorGeometryToolAxesLabels`
              - Allow configuring the VGT axes labels.

            * - :py:class:`~VectorGeometryToolAxes`
              - A generic axes class.

            * - :py:class:`~VectorGeometryToolPoint`
              - A generic VGT point class.

            * - :py:class:`~VectorGeometryToolSystem`
              - Base class for VGT axes.

            * - :py:class:`~VectorGeometryToolAngle`
              - Base class for VGT axes.

            * - :py:class:`~VectorGeometryToolPlaneLabels`
              - Allow configuring the X and Y axes labels.

            * - :py:class:`~VectorGeometryToolPlane`
              - Base class for VGT axes.

            * - :py:class:`~VectorGeometryToolAxesAlignedAndConstrained`
              - Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

            * - :py:class:`~VectorGeometryToolAxesAngularOffset`
              - Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

            * - :py:class:`~VectorGeometryToolAxesFixedAtEpoch`
              - Axes based on another set fixed at a specified epoch.

            * - :py:class:`~VectorGeometryToolAxesBPlane`
              - B-Plane axes using the selected target body and reference vector.

            * - :py:class:`~VectorGeometryToolAxesCustomScript`
              - Customized axes offset with respect to a set of reference Axes.

            * - :py:class:`~VectorGeometryToolAxesAttitudeFile`
              - Axes specified by data from a file.

            * - :py:class:`~VectorGeometryToolAxesFixed`
              - Axes fixed in reference axes.

            * - :py:class:`~VectorGeometryToolAxesModelAttach`
              - Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

            * - :py:class:`~VectorGeometryToolAxesSpinning`
              - Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

            * - :py:class:`~VectorGeometryToolAxesOnSurface`
              - Topocentric axes located at the reference point's projection on the central body.

            * - :py:class:`~VectorGeometryToolAxesTrajectory`
              - Axes based on trajectory of the point relative to the reference coordinate system.

            * - :py:class:`~VectorGeometryToolAxesLagrangeLibration`
              - Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

            * - :py:class:`~VectorGeometryToolAxesCommonTasks`
              - Provide methods to create non-persistent VGT axes components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~VectorGeometryToolAxesAtTimeInstant`
              - Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

            * - :py:class:`~VectorGeometryToolAxesPlugin`
              - A VGT axes plugin.

            * - :py:class:`~VectorGeometryToolAngleBetweenVectors`
              - An angle between two vectors.

            * - :py:class:`~VectorGeometryToolAngleBetweenPlanes`
              - An angle between two planes.

            * - :py:class:`~VectorGeometryToolAngleDihedral`
              - An angle between two vectors about an axis.

            * - :py:class:`~VectorGeometryToolAngleRotation`
              - Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

            * - :py:class:`~VectorGeometryToolAngleToPlane`
              - An angle between a vector and a plane.

            * - :py:class:`~VectorGeometryToolPlaneNormal`
              - A plane normal to a vector at a given point.

            * - :py:class:`~VectorGeometryToolPlaneQuadrant`
              - A plane based on a selected Quadrant of a reference system.

            * - :py:class:`~VectorGeometryToolPlaneTrajectory`
              - The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

            * - :py:class:`~VectorGeometryToolPlaneTriad`
              - A Plane containing points PointA, PointB and ReferencePont with the first axis aligned with the direction from the ReferencePoint to PointA and the second axis toward the direction from the ReferencePoint to PointB.

            * - :py:class:`~VectorGeometryToolPlaneTwoVector`
              - A plane normal to a vector at a given point.

            * - :py:class:`~VectorGeometryToolPointBPlane`
              - B-Plane point using the selected target body.

            * - :py:class:`~VectorGeometryToolPointFile`
              - Point specified by data from a file.

            * - :py:class:`~VectorGeometryToolPointFixedInSystem`
              - Point fixed in a reference coordinate system using the selected coordinate type.

            * - :py:class:`~VectorGeometryToolPointGrazing`
              - The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

            * - :py:class:`~VectorGeometryToolPointGlint`
              - Point on central body surface that reflects from source to observer.

            * - :py:class:`~VectorGeometryToolPointCovarianceGrazing`
              - The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

            * - :py:class:`~VectorGeometryToolPointPlaneIntersection`
              - Point on a plane located along a given direction looking from a given origin.

            * - :py:class:`~VectorGeometryToolPointOnSurface`
              - The detic subpoint of the reference point as projected onto the central body.

            * - :py:class:`~VectorGeometryToolPointModelAttach`
              - A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

            * - :py:class:`~VectorGeometryToolPointSatelliteCollectionEntry`
              - A point placed at the center of mass of a specified satellite of the satellite collection.

            * - :py:class:`~VectorGeometryToolPointPlaneProjection`
              - The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

            * - :py:class:`~VectorGeometryToolPointLagrangeLibration`
              - Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

            * - :py:class:`~VectorGeometryToolPointCommonTasks`
              - Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~VectorGeometryToolPointCentBodyIntersect`
              - Point on central body surface along direction vector originating at source point.

            * - :py:class:`~VectorGeometryToolPointAtTimeInstant`
              - Point fixed relative to reference system based on another point evaluated at specified time instant.

            * - :py:class:`~VectorGeometryToolPointPlugin`
              - A VGT point plugin.

            * - :py:class:`~VectorGeometryToolPointCBFixedOffset`
              - Point specified by fixed components with respect to central body.

            * - :py:class:`~VectorGeometryToolSystemAssembled`
              - A system assembled from an origin point and a set of reference axes.

            * - :py:class:`~VectorGeometryToolSystemOnSurface`
              - A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

            * - :py:class:`~AnalysisWorkbenchLLAPosition`
              - A position represented by the Latitude, longtitude and Latitude.

            * - :py:class:`~VectorGeometryToolSystemCommonTasks`
              - Provide methods to create non-persistent VGT coordinate reference frames (systems). Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~VectorGeometryToolVectorAngleRate`
              - Angle rate vector perpendicular to the plane in which the angle is defined.

            * - :py:class:`~VectorGeometryToolVectorApoapsis`
              - Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~VectorGeometryToolVectorFixedAtEpoch`
              - Based on another vector fixed at a specified epoch.

            * - :py:class:`~VectorGeometryToolVectorAngularVelocity`
              - Angular velocity vector of one set of axes computed with respect to the reference set.

            * - :py:class:`~VectorGeometryToolVectorConing`
              - Vector created by revolving the Reference vector around the About vector with the specified rate.

            * - :py:class:`~VectorGeometryToolVectorCross`
              - The vector cross product of two vectors.

            * - :py:class:`~VectorGeometryToolVectorCustomScript`
              - Customized vector components defined with respect to reference axes.

            * - :py:class:`~VectorGeometryToolVectorDerivative`
              - A vector derivative of a vector computed with respect to specified axes.

            * - :py:class:`~VectorGeometryToolVectorDisplacement`
              - Vector defined by its start and end points.

            * - :py:class:`~VectorGeometryToolVectorTwoPlanesIntersection`
              - Defined along the intersection of two planes.

            * - :py:class:`~VectorGeometryToolVectorModelAttach`
              - Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

            * - :py:class:`~VectorGeometryToolVectorProjection`
              - A projection of a vector computed with respect to a reference plane.

            * - :py:class:`~VectorGeometryToolVectorScaled`
              - Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

            * - :py:class:`~VectorGeometryToolVectorEccentricity`
              - A vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~VectorGeometryToolVectorFixedInAxes`
              - Vector fixed in reference axes.

            * - :py:class:`~VectorGeometryToolVectorLineOfNodes`
              - Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

            * - :py:class:`~VectorGeometryToolVectorOrbitAngularMomentum`
              - Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:class:`~VectorGeometryToolVectorOrbitNormal`
              - Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:class:`~VectorGeometryToolVectorPeriapsis`
              - Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~VectorGeometryToolVectorReflection`
              - Incident vector reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

            * - :py:class:`~VectorGeometryToolVectorRotationVector`
              - Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

            * - :py:class:`~VectorGeometryToolVectorDirectionToStar`
              - Defined with respect to a star object. For a star object to be available, you must first create one.

            * - :py:class:`~VectorGeometryToolVectorFixedAtTimeInstant`
              - Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

            * - :py:class:`~VectorGeometryToolVectorLinearCombination`
              - Linear combination of two input vectors.

            * - :py:class:`~VectorGeometryToolVectorProjectAlongVector`
              - A projection of a source vector in the direction of another vector.

            * - :py:class:`~VectorGeometryToolVectorScalarLinearCombination`
              - Linear combination of two input vectors using scalars.

            * - :py:class:`~VectorGeometryToolVectorScalarScaled`
              - Scaled version of the input vector using scalar.

            * - :py:class:`~VectorGeometryToolVectorVelocityAcceleration`
              - Velocity vector of a point in a coordinate system.

            * - :py:class:`~VectorGeometryToolVectorPlugin`
              - A VGT vector plugin.

            * - :py:class:`~VectorGeometryToolVectorDispSurface`
              - Displacement between origin and destination points using surface distance and altitude difference.

            * - :py:class:`~VectorGeometryToolVectorFactory`
              - A Factory object to create vectors.

            * - :py:class:`~VectorGeometryToolAxesFactory`
              - A Factory object to create axes.

            * - :py:class:`~VectorGeometryToolSystemFactory`
              - A Factory class to create VGT systems.

            * - :py:class:`~VectorGeometryToolPointFactory`
              - A Factory object to create points.

            * - :py:class:`~VectorGeometryToolPlaneFactory`
              - A Factory object to create VGT planes.

            * - :py:class:`~VectorGeometryToolAngleFactory`
              - A Factory object to create angles.

            * - :py:class:`~VectorGeometryToolVectorGroup`
              - Access or create VGT vectors associated with an object or a central body.

            * - :py:class:`~VectorGeometryToolPointGroup`
              - Access or create VGT points associated with an object or a central body.

            * - :py:class:`~VectorGeometryToolAngleGroup`
              - Access or create VGT angles associated with an object or a central body.

            * - :py:class:`~VectorGeometryToolAxesGroup`
              - Access or create VGT axes associated with an object or a central body.

            * - :py:class:`~VectorGeometryToolPlaneGroup`
              - Represents a VGT Plane component.

            * - :py:class:`~VectorGeometryToolSystemGroup`
              - Access or create VGT systems associated with an object or a central body.

            * - :py:class:`~AnalysisWorkbenchProvider`
              - Allow accessing existing Vector Geometry Tool components.

            * - :py:class:`~AnalysisWorkbenchRoot`
              - Represents a VGT root.

            * - :py:class:`~VectorGeometryToolWellKnownEarthSystems`
              - Well-known Earth's coordinate systems.

            * - :py:class:`~VectorGeometryToolWellKnownEarthAxes`
              - Well-known Earth's axes.

            * - :py:class:`~VectorGeometryToolWellKnownSunSystems`
              - The Sun's well-known coordinate reference systems.

            * - :py:class:`~VectorGeometryToolWellKnownSunAxes`
              - Well-known Sun's axes.

            * - :py:class:`~VectorGeometryToolWellKnownSystems`
              - Well-known coordinate reference systems.

            * - :py:class:`~VectorGeometryToolWellKnownAxes`
              - Represents well-known VGT Axes.

            * - :py:class:`~AnalysisWorkbenchMethodCallAngleFindResult`
              - Represents result returned with IAgCrdnAngle.FindCoordinates method.

            * - :py:class:`~AnalysisWorkbenchMethodCallAngleFindWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinatesWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallAxesTransformResult`
              - Contains the results returned with IAgCrdnAxes.TransformFrom method.

            * - :py:class:`~AnalysisWorkbenchMethodCallAxesTransformWithRateResult`
              - Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallAxesFindInAxesResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxes method.

            * - :py:class:`~AnalysisWorkbenchMethodCallAxesFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxesWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallPlaneFindInAxesResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxes method.

            * - :py:class:`~AnalysisWorkbenchMethodCallPlaneFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxesWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallPlaneFindInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystem method.

            * - :py:class:`~AnalysisWorkbenchMethodCallPlaneFindInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallPointLocateInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallPointLocateInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystemWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallSystemTransformResult`
              - Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

            * - :py:class:`~AnalysisWorkbenchMethodCallSystemTransformWithRateResult`
              - Contains the results returned with IAgCrdnSystem.TransformFromWithRate and IAgCrdnSystem.TransformToWithRate methods.

            * - :py:class:`~AnalysisWorkbenchMethodCallSystemFindInSystemResult`
              - Contains the results returned with IAgCrdnSystem.FindInSystem method.

            * - :py:class:`~AnalysisWorkbenchMethodCallVectorFindInAxesResult`
              - Contains the results returned with IAgCrdnVector.FindInAxes method.

            * - :py:class:`~AnalysisWorkbenchMethodCallVectorFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnVector.FindInAxesWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallAngleFindAngleWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindAngleWithRate method.

            * - :py:class:`~AnalysisWorkbenchMethodCallAngleFindAngleResult`
              - Contains the results returned with IAgCrdnAngle.FindAngle method.

            * - :py:class:`~TimeToolInterval`
              - Represents an interval.

            * - :py:class:`~TimeToolIntervalCollection`
              - Represents a collection of intervals.

            * - :py:class:`~AnalysisWorkbenchCentralBody`
              - Represents an central body.

            * - :py:class:`~AnalysisWorkbenchCentralBodyRefTo`
              - Represents a central body reference.

            * - :py:class:`~AnalysisWorkbenchCentralBodyCollection`
              - A collection of central body names.

            * - :py:class:`~AnalysisWorkbenchCollection`
              - A collection of VGT objects.

            * - :py:class:`~TimeToolPointSamplingResult`
              - Contains tabulated positions and velocities of a point created by Sample method.

            * - :py:class:`~TimeToolPointSamplingInterval`
              - The interface represents an interval with the time, position and velocity arrays.

            * - :py:class:`~TimeToolPointSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, position and velocity arrays.

            * - :py:class:`~TimeToolAxesSamplingResult`
              - Contains tabulated orientations and angular velocities of axes created by Sample method.

            * - :py:class:`~TimeToolAxesSamplingInterval`
              - The interface represents an interval with the time, orientation and velocity arrays.

            * - :py:class:`~TimeToolAxesSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, orientation and velocity arrays.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~CRDN_CALC_SCALAR_TYPE`
              - Define available calculation scalar types.

            * - :py:class:`~CRDN_CONDITION_COMBINED_OPERATION_TYPE`
              - Define scalar condition combined operation types.

            * - :py:class:`~CRDN_CONDITION_SET_TYPE`
              - Define available condition set types.

            * - :py:class:`~CRDN_CONDITION_THRESHOLD_OPTION`
              - Operations for Scalar Bounds Condition.

            * - :py:class:`~CRDN_CONDITION_TYPE`
              - Define available condition types.

            * - :py:class:`~CRDN_DIMENSION_INHERITANCE`
              - Define how dimension is inherited.

            * - :py:class:`~CRDN_EVENT_ARRAY_FILTER_TYPE`
              - Event array filter types.

            * - :py:class:`~CRDN_EVENT_ARRAY_TYPE`
              - Define available time array types.

            * - :py:class:`~CRDN_EVENT_INTERVAL_COLLECTION_TYPE`
              - Define available interval collection types.

            * - :py:class:`~CRDN_EVENT_INTERVAL_LIST_TYPE`
              - Define available interval list types.

            * - :py:class:`~CRDN_EVENT_INTERVAL_TYPE`
              - Define available interval types.

            * - :py:class:`~CRDN_EVENT_LIST_MERGE_OPERATION`
              - Define merge operations for interval lists.

            * - :py:class:`~CRDN_EVENT_TYPE`
              - Define available time instant types.

            * - :py:class:`~CRDN_EXTREMUM_CONSTANTS`
              - These constants are utilized when finding a local or global minimum or maximum, or the threshold crossing.

            * - :py:class:`~CRDN_FILE_INTERPOLATOR_TYPE`
              - Interpolator types.

            * - :py:class:`~CRDN_INTEGRAL_TYPE`
              - Integral types.

            * - :py:class:`~CRDN_INTEGRATION_WINDOW_TYPE`
              - Define the interval of times during which an integral is evaluated.

            * - :py:class:`~CRDN_INTERPOLATOR_TYPE`
              - Interpolator types.

            * - :py:class:`~CRDN_INTERVAL_DURATION_KIND`
              - Duration for filtering intervals or gaps from interval lists or time arrays.

            * - :py:class:`~CRDN_INTERVAL_SELECTION`
              - Select the method to choose an interval from an interval list.

            * - :py:class:`~CRDN_PARAMETER_SET_TYPE`
              - Define parameter set types.

            * - :py:class:`~CRDN_PRUNE_FILTER`
              - Specify the filter for filtering interval lists or time arrays.

            * - :py:class:`~CRDN_SAMPLED_REFERENCE_TIME`
              - Event array reference type.

            * - :py:class:`~CRDN_SAMPLING_METHOD`
              - Define the Sampling Method.

            * - :py:class:`~CRDN_SATISFACTION_CROSSING`
              - Direction crossing flags.

            * - :py:class:`~CRDN_SAVE_DATA_OPTION`
              - Method for saving computed data.

            * - :py:class:`~CRDN_SIGNAL_PATH_REFERENCE_SYSTEM`
              - Signal path reference system types.

            * - :py:class:`~CRDN_SMART_EPOCH_STATE`
              - Smart epoch states.

            * - :py:class:`~CRDN_SMART_INTERVAL_STATE`
              - Smart interval states.

            * - :py:class:`~CRDN_SPEED_OPTIONS`
              - Define various speed options.

            * - :py:class:`~CRDN_START_STOP_OPTION`
              - Start/stop options.

            * - :py:class:`~CRDN_THRESH_CONVERGE_SENSE`
              - Specify the desired sense of the results from threshold crossing computations.

            * - :py:class:`~VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE`
              - Define component directions for a vector.

            * - :py:class:`~CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE`
              - Define volume calc altitude reference types.

            * - :py:class:`~CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE`
              - Define volume calc angle off vector reference types.

            * - :py:class:`~CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE`
              - Define volume calc range distance types.

            * - :py:class:`~CRDN_VOLUME_CALC_RANGE_SPEED_TYPE`
              - Define volume calc range distance types.

            * - :py:class:`~CRDN_VOLUME_CALC_TYPE`
              - Define volume calc types.

            * - :py:class:`~CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE`
              - Define volume calc spatial condition accumulation types.

            * - :py:class:`~CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE`
              - Define volume calc spatial condition duration types.

            * - :py:class:`~CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE`
              - Define volume calc spatial condition filter types.

            * - :py:class:`~CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE`
              - Define volume calc spatial condition satisfaction metric types.

            * - :py:class:`~CRDN_VOLUME_GRID_TYPE`
              - Define volume grid types.

            * - :py:class:`~CRDN_VOLUME_RESULT_VECTOR_REQUEST`
              - Define volume result vector request types.

            * - :py:class:`~CRDN_VOLUME_TYPE`
              - Define volume grid types.

            * - :py:class:`~CRDN_VOLUME_ABERRATION_TYPE`
              - Define the model of aberration to use.

            * - :py:class:`~CRDN_VOLUME_CLOCK_HOST_TYPE`
              - Define whether base or target of an Access instance holds the clock for Access times.

            * - :py:class:`~CRDN_VOLUME_COMBINED_OPERATION_TYPE`
              - Define spatial condition combined operation types.

            * - :py:class:`~CRDN_VOLUME_FROM_GRID_EDGE_TYPE`
              - Define spatial condition from grid edge type.

            * - :py:class:`~CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE`
              - Define spatial condition lighting conditions types.

            * - :py:class:`~CRDN_VOLUME_OVER_TIME_DURATION_TYPE`
              - Define spatial condition over time duration type.

            * - :py:class:`~CRDN_VOLUME_TIME_SENSE_TYPE`
              - Define whether object1 or object2 of an Access instance holds the clock for Access times.

            * - :py:class:`~CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE`
              - Define volumetric grid values method types.

            * - :py:class:`~CRDN_KIND`
              - Represents kinds of vectory geometry components.

            * - :py:class:`~VECTOR_GEOMETRY_TOOL_ANGLE_TYPE`
              - Represents angle types.

            * - :py:class:`~VECTOR_GEOMETRY_TOOL_AXES_TYPE`
              - Represents vector types.

            * - :py:class:`~VECTOR_GEOMETRY_TOOL_PLANE_TYPE`
              - Represents plane types.

            * - :py:class:`~VECTOR_GEOMETRY_TOOL_POINT_TYPE`
              - Represents point types.

            * - :py:class:`~CRDN_SYSTEM_TYPE`
              - Represents system types.

            * - :py:class:`~VECTOR_GEOMETRY_TOOL_VECTOR_TYPE`
              - Represents vector types.

            * - :py:class:`~CRDN_MEAN_ELEMENT_THEORY`
              - Mean element theory types for approximating motion.

            * - :py:class:`~CRDN_DIRECTION_TYPE`
              - Direction options.

            * - :py:class:`~CRDN_LAGRANGE_LIBRATION_POINT_TYPE`
              - Types of the Lagrange points, also known as libration points. Lagrange points are points in space where gravitational forces and the orbital motion of a body balance each other.

            * - :py:class:`~CRDN_QUADRANT_TYPE`
              - Quadrants from a reference system (e.g., XY, XZ, YZ, YX, ZX, ZY).

            * - :py:class:`~CRDN_TRAJECTORY_AXES_TYPE`
              - Trajectory axes coordinate types.

            * - :py:class:`~CRDN_DISPLAY_AXIS_SELECTOR`
              - Rotation directions.

            * - :py:class:`~CRDN_SIGNED_ANGLE_TYPE`
              - Define options for computing an angle.

            * - :py:class:`~VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE`
              - B-Plane point types.

            * - :py:class:`~CRDN_REFERENCE_SHAPE_TYPE`
              - Surface shape types.

            * - :py:class:`~CRDN_SURFACE_TYPE`
              - Surface types.

            * - :py:class:`~CRDN_SWEEP_MODE`
              - The rotation sweeping modes.

            * - :py:class:`~CRDN_SIGNAL_SENSE`
              - Signal sense transmission options.

            * - :py:class:`~CRDN_INTERSECTION_SURFACE`
              - Intersection surface flags.

            * - :py:class:`~VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE`
              - Dimension inheritance constants used to configure the dimension inheritance of a vector scaled by a scalar.



Description
-----------

The Vector Geometry (VGT) API enables users define new or utilize existing geometric constructs such as coordinate systems, vectors, points, angles, axes and planes.

The geometric elements can be used to transform between coordinate
systems, compute first and second derivatives, or perform other types of
analysis.

Detail
------

.. py:currentmodule:: ansys.stk.core.vgt


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ITimeToolIntervalCollection<vgt\ITimeToolIntervalCollection>
     ITimeToolInterval<vgt\ITimeToolInterval>
     IVectorGeometryToolPoint<vgt\IVectorGeometryToolPoint>
     IVectorGeometryToolVector<vgt\IVectorGeometryToolVector>
     IVectorGeometryToolSystem<vgt\IVectorGeometryToolSystem>
     IVectorGeometryToolAxes<vgt\IVectorGeometryToolAxes>
     IVectorGeometryToolAngle<vgt\IVectorGeometryToolAngle>
     IVectorGeometryToolPlane<vgt\IVectorGeometryToolPlane>
     IAnalysisWorkbenchContext<vgt\IAnalysisWorkbenchContext>
     IAnalysisWorkbenchComponent<vgt\IAnalysisWorkbenchComponent>
     ICalculationToolEvaluateResult<vgt\ICalculationToolEvaluateResult>
     ICalculationToolEvaluateWithRateResult<vgt\ICalculationToolEvaluateWithRateResult>
     ITimeToolEventIntervalResult<vgt\ITimeToolEventIntervalResult>
     ITimeToolEventFindOccurrenceResult<vgt\ITimeToolEventFindOccurrenceResult>
     ITimeToolFindTimesResult<vgt\ITimeToolFindTimesResult>
     ITimeToolIntervalsVectorResult<vgt\ITimeToolIntervalsVectorResult>
     ITimeToolEventIntervalCollectionOccurredResult<vgt\ITimeToolEventIntervalCollectionOccurredResult>
     ITimeToolIntervalListResult<vgt\ITimeToolIntervalListResult>
     ITimeToolIntervalVectorCollection<vgt\ITimeToolIntervalVectorCollection>
     ITimeToolEventGroup<vgt\ITimeToolEventGroup>
     ITimeToolEventIntervalGroup<vgt\ITimeToolEventIntervalGroup>
     ITimeToolEventIntervalListGroup<vgt\ITimeToolEventIntervalListGroup>
     ITimeToolEventArrayGroup<vgt\ITimeToolEventArrayGroup>
     ICalculationToolScalarGroup<vgt\ICalculationToolScalarGroup>
     ITimeToolEventIntervalCollectionGroup<vgt\ITimeToolEventIntervalCollectionGroup>
     ICalculationToolParameterSetGroup<vgt\ICalculationToolParameterSetGroup>
     ICalculationToolConditionGroup<vgt\ICalculationToolConditionGroup>
     ICalculationToolConditionSetGroup<vgt\ICalculationToolConditionSetGroup>
     ICalculationToolConditionSetEvaluateResult<vgt\ICalculationToolConditionSetEvaluateResult>
     ICalculationToolConditionSetEvaluateWithRateResult<vgt\ICalculationToolConditionSetEvaluateWithRateResult>
     ISpatialAnalysisToolVolumeGridGroup<vgt\ISpatialAnalysisToolVolumeGridGroup>
     ISpatialAnalysisToolVolumeGroup<vgt\ISpatialAnalysisToolVolumeGroup>
     ISpatialAnalysisToolVolumeCalcGroup<vgt\ISpatialAnalysisToolVolumeCalcGroup>
     ICalculationToolScalar<vgt\ICalculationToolScalar>
     ICalculationToolScalarAngle<vgt\ICalculationToolScalarAngle>
     ICalculationToolScalarAverage<vgt\ICalculationToolScalarAverage>
     ICalculationToolScalarConstant<vgt\ICalculationToolScalarConstant>
     ICalculationToolScalarCustom<vgt\ICalculationToolScalarCustom>
     ICalculationToolScalarCustomInline<vgt\ICalculationToolScalarCustomInline>
     ICalculationToolScalarDataElement<vgt\ICalculationToolScalarDataElement>
     ICalculationToolScalarDerivative<vgt\ICalculationToolScalarDerivative>
     ICalculationToolScalarDotProduct<vgt\ICalculationToolScalarDotProduct>
     ICalculationToolScalarElapsedTime<vgt\ICalculationToolScalarElapsedTime>
     ICalculationToolScalarFactory<vgt\ICalculationToolScalarFactory>
     ICalculationToolScalarFile<vgt\ICalculationToolScalarFile>
     ICalculationToolScalarFixedAtTimeInstant<vgt\ICalculationToolScalarFixedAtTimeInstant>
     ICalculationToolScalarFunction<vgt\ICalculationToolScalarFunction>
     ICalculationToolScalarFunction2Var<vgt\ICalculationToolScalarFunction2Var>
     ICalculationToolScalarIntegral<vgt\ICalculationToolScalarIntegral>
     ICalculationToolScalarPlugin<vgt\ICalculationToolScalarPlugin>
     ICalculationToolScalarPointInVolumeCalc<vgt\ICalculationToolScalarPointInVolumeCalc>
     ICalculationToolScalarStandardDeviation<vgt\ICalculationToolScalarStandardDeviation>
     ICalculationToolScalarSurfaceDistanceBetweenPoints<vgt\ICalculationToolScalarSurfaceDistanceBetweenPoints>
     ICalculationToolScalarVectorComponent<vgt\ICalculationToolScalarVectorComponent>
     ICalculationToolScalarVectorMagnitude<vgt\ICalculationToolScalarVectorMagnitude>
     ICalculationToolCondition<vgt\ICalculationToolCondition>
     ICalculationToolConditionCombined<vgt\ICalculationToolConditionCombined>
     ICalculationToolConditionFactory<vgt\ICalculationToolConditionFactory>
     ICalculationToolConditionPointInVolume<vgt\ICalculationToolConditionPointInVolume>
     ICalculationToolConditionScalarBounds<vgt\ICalculationToolConditionScalarBounds>
     ICalculationToolConditionSet<vgt\ICalculationToolConditionSet>
     ICalculationToolConditionSetFactory<vgt\ICalculationToolConditionSetFactory>
     ICalculationToolConditionSetScalarThresholds<vgt\ICalculationToolConditionSetScalarThresholds>
     IAnalysisWorkbenchConverge<vgt\IAnalysisWorkbenchConverge>
     ICalculationToolConvergeBasic<vgt\ICalculationToolConvergeBasic>
     IAnalysisWorkbenchDerivative<vgt\IAnalysisWorkbenchDerivative>
     ICalculationToolDerivativeBasic<vgt\ICalculationToolDerivativeBasic>
     ITimeToolEvent<vgt\ITimeToolEvent>
     ITimeToolEventArray<vgt\ITimeToolEventArray>
     ITimeToolEventArrayConditionCrossings<vgt\ITimeToolEventArrayConditionCrossings>
     ITimeToolEventArrayExtrema<vgt\ITimeToolEventArrayExtrema>
     ITimeToolEventArrayFactory<vgt\ITimeToolEventArrayFactory>
     ITimeToolEventArrayFiltered<vgt\ITimeToolEventArrayFiltered>
     ITimeToolEventArrayFixedStep<vgt\ITimeToolEventArrayFixedStep>
     ITimeToolEventArrayFixedTimes<vgt\ITimeToolEventArrayFixedTimes>
     ITimeToolEventArrayMerged<vgt\ITimeToolEventArrayMerged>
     ITimeToolEventArraySignaled<vgt\ITimeToolEventArraySignaled>
     ITimeToolEventArrayStartStopTimes<vgt\ITimeToolEventArrayStartStopTimes>
     ITimeToolEventEpoch<vgt\ITimeToolEventEpoch>
     ITimeToolEventExtremum<vgt\ITimeToolEventExtremum>
     ITimeToolEventFactory<vgt\ITimeToolEventFactory>
     ITimeToolEventInterval<vgt\ITimeToolEventInterval>
     ITimeToolEventIntervalBetweenTimeInstants<vgt\ITimeToolEventIntervalBetweenTimeInstants>
     ITimeToolEventIntervalCollection<vgt\ITimeToolEventIntervalCollection>
     ITimeToolEventIntervalCollectionCondition<vgt\ITimeToolEventIntervalCollectionCondition>
     ITimeToolEventIntervalCollectionFactory<vgt\ITimeToolEventIntervalCollectionFactory>
     ITimeToolEventIntervalCollectionLighting<vgt\ITimeToolEventIntervalCollectionLighting>
     ITimeToolEventIntervalCollectionSignaled<vgt\ITimeToolEventIntervalCollectionSignaled>
     ITimeToolEventIntervalFactory<vgt\ITimeToolEventIntervalFactory>
     ITimeToolEventIntervalFixed<vgt\ITimeToolEventIntervalFixed>
     ITimeToolEventIntervalFixedDuration<vgt\ITimeToolEventIntervalFixedDuration>
     ITimeToolEventIntervalFromIntervalList<vgt\ITimeToolEventIntervalFromIntervalList>
     ITimeToolEventIntervalList<vgt\ITimeToolEventIntervalList>
     ITimeToolEventIntervalListCondition<vgt\ITimeToolEventIntervalListCondition>
     ITimeToolEventIntervalListFactory<vgt\ITimeToolEventIntervalListFactory>
     ITimeToolEventIntervalListFile<vgt\ITimeToolEventIntervalListFile>
     ITimeToolEventIntervalListFiltered<vgt\ITimeToolEventIntervalListFiltered>
     ITimeToolEventIntervalListFixed<vgt\ITimeToolEventIntervalListFixed>
     ITimeToolEventIntervalListMerged<vgt\ITimeToolEventIntervalListMerged>
     ITimeToolEventIntervalListScaled<vgt\ITimeToolEventIntervalListScaled>
     ITimeToolEventIntervalListSignaled<vgt\ITimeToolEventIntervalListSignaled>
     ITimeToolEventIntervalListTimeOffset<vgt\ITimeToolEventIntervalListTimeOffset>
     ITimeToolEventIntervalScaled<vgt\ITimeToolEventIntervalScaled>
     ITimeToolEventIntervalSignaled<vgt\ITimeToolEventIntervalSignaled>
     ITimeToolEventIntervalSmartInterval<vgt\ITimeToolEventIntervalSmartInterval>
     ITimeToolEventIntervalTimeOffset<vgt\ITimeToolEventIntervalTimeOffset>
     ITimeToolEventSignaled<vgt\ITimeToolEventSignaled>
     ITimeToolEventSmartEpoch<vgt\ITimeToolEventSmartEpoch>
     ITimeToolEventStartStopTime<vgt\ITimeToolEventStartStopTime>
     ITimeToolEventTimeOffset<vgt\ITimeToolEventTimeOffset>
     ITimeToolFirstIntervalsFilter<vgt\ITimeToolFirstIntervalsFilter>
     ITimeToolGapsFilter<vgt\ITimeToolGapsFilter>
     IAnalysisWorkbenchIntegral<vgt\IAnalysisWorkbenchIntegral>
     ICalculationToolIntegralBasic<vgt\ICalculationToolIntegralBasic>
     IAnalysisWorkbenchInterp<vgt\IAnalysisWorkbenchInterp>
     ICalculationToolInterpBasic<vgt\ICalculationToolInterpBasic>
     ITimeToolIntervalsFilter<vgt\ITimeToolIntervalsFilter>
     ITimeToolLastIntervalsFilter<vgt\ITimeToolLastIntervalsFilter>
     ICalculationToolParameterSet<vgt\ICalculationToolParameterSet>
     ICalculationToolParameterSetAttitude<vgt\ICalculationToolParameterSetAttitude>
     ICalculationToolParameterSetFactory<vgt\ICalculationToolParameterSetFactory>
     ICalculationToolParameterSetGroundTrajectory<vgt\ICalculationToolParameterSetGroundTrajectory>
     ICalculationToolParameterSetOrbit<vgt\ICalculationToolParameterSetOrbit>
     ICalculationToolParameterSetTrajectory<vgt\ICalculationToolParameterSetTrajectory>
     ICalculationToolParameterSetVector<vgt\ICalculationToolParameterSetVector>
     ITimeToolPruneFilter<vgt\ITimeToolPruneFilter>
     ITimeToolPruneFilterFactory<vgt\ITimeToolPruneFilterFactory>
     ITimeToolRelativeSatisfactionConditionFilter<vgt\ITimeToolRelativeSatisfactionConditionFilter>
     IAnalysisWorkbenchSampling<vgt\IAnalysisWorkbenchSampling>
     ICalculationToolSamplingBasic<vgt\ICalculationToolSamplingBasic>
     ICalculationToolSamplingCurvatureTolerance<vgt\ICalculationToolSamplingCurvatureTolerance>
     ICalculationToolSamplingFixedStep<vgt\ICalculationToolSamplingFixedStep>
     ICalculationToolSamplingMethod<vgt\ICalculationToolSamplingMethod>
     ICalculationToolSamplingMethodFactory<vgt\ICalculationToolSamplingMethodFactory>
     ICalculationToolSamplingRelativeTolerance<vgt\ICalculationToolSamplingRelativeTolerance>
     ITimeToolSatisfactionConditionFilter<vgt\ITimeToolSatisfactionConditionFilter>
     IAnalysisWorkbenchSignalDelay<vgt\IAnalysisWorkbenchSignalDelay>
     ITimeToolSignalDelayBasic<vgt\ITimeToolSignalDelayBasic>
     ISpatialAnalysisToolVolumeCalcFactory<vgt\ISpatialAnalysisToolVolumeCalcFactory>
     ISpatialAnalysisToolVolumeFactory<vgt\ISpatialAnalysisToolVolumeFactory>
     ISpatialAnalysisToolVolumeGridFactory<vgt\ISpatialAnalysisToolVolumeGridFactory>
     ISpatialAnalysisToolGridCoordinateDefinition<vgt\ISpatialAnalysisToolGridCoordinateDefinition>
     ISpatialAnalysisToolGridValuesCustom<vgt\ISpatialAnalysisToolGridValuesCustom>
     ISpatialAnalysisToolGridValuesFixedNumberOfSteps<vgt\ISpatialAnalysisToolGridValuesFixedNumberOfSteps>
     ISpatialAnalysisToolGridValuesFixedStep<vgt\ISpatialAnalysisToolGridValuesFixedStep>
     ISpatialAnalysisToolGridValuesMethod<vgt\ISpatialAnalysisToolGridValuesMethod>
     ITimeToolLightTimeDelay<vgt\ITimeToolLightTimeDelay>
     ISpatialAnalysisToolVolume<vgt\ISpatialAnalysisToolVolume>
     ISpatialAnalysisToolVolumeCalc<vgt\ISpatialAnalysisToolVolumeCalc>
     ISpatialAnalysisToolVolumeCalcAltitude<vgt\ISpatialAnalysisToolVolumeCalcAltitude>
     ISpatialAnalysisToolVolumeCalcAngleOffVector<vgt\ISpatialAnalysisToolVolumeCalcAngleOffVector>
     ISpatialAnalysisToolVolumeCalcConditionSatMetric<vgt\ISpatialAnalysisToolVolumeCalcConditionSatMetric>
     ISpatialAnalysisToolVolumeCalcDelayRange<vgt\ISpatialAnalysisToolVolumeCalcDelayRange>
     ISpatialAnalysisToolVolumeCalcFile<vgt\ISpatialAnalysisToolVolumeCalcFile>
     ISpatialAnalysisToolVolumeCalcFromScalar<vgt\ISpatialAnalysisToolVolumeCalcFromScalar>
     ISpatialAnalysisToolVolumeCalcRange<vgt\ISpatialAnalysisToolVolumeCalcRange>
     ISpatialAnalysisToolVolumeCalcSolarIntensity<vgt\ISpatialAnalysisToolVolumeCalcSolarIntensity>
     ISpatialAnalysisToolVolumeCombined<vgt\ISpatialAnalysisToolVolumeCombined>
     ISpatialAnalysisToolVolumeFromCalc<vgt\ISpatialAnalysisToolVolumeFromCalc>
     ISpatialAnalysisToolVolumeFromCondition<vgt\ISpatialAnalysisToolVolumeFromCondition>
     ISpatialAnalysisToolVolumeFromGrid<vgt\ISpatialAnalysisToolVolumeFromGrid>
     ISpatialAnalysisToolVolumeFromTimeSatisfaction<vgt\ISpatialAnalysisToolVolumeFromTimeSatisfaction>
     ISpatialAnalysisToolVolumeGrid<vgt\ISpatialAnalysisToolVolumeGrid>
     ISpatialAnalysisToolVolumeGridBearingAlt<vgt\ISpatialAnalysisToolVolumeGridBearingAlt>
     ISpatialAnalysisToolVolumeGridCartesian<vgt\ISpatialAnalysisToolVolumeGridCartesian>
     ISpatialAnalysisToolVolumeGridConstrained<vgt\ISpatialAnalysisToolVolumeGridConstrained>
     ISpatialAnalysisToolVolumeGridCylindrical<vgt\ISpatialAnalysisToolVolumeGridCylindrical>
     ISpatialAnalysisToolVolumeGridLatLonAlt<vgt\ISpatialAnalysisToolVolumeGridLatLonAlt>
     ISpatialAnalysisToolVolumeGridResult<vgt\ISpatialAnalysisToolVolumeGridResult>
     ISpatialAnalysisToolVolumeGridSpherical<vgt\ISpatialAnalysisToolVolumeGridSpherical>
     ISpatialAnalysisToolVolumeInview<vgt\ISpatialAnalysisToolVolumeInview>
     ISpatialAnalysisToolVolumeLighting<vgt\ISpatialAnalysisToolVolumeLighting>
     ISpatialAnalysisToolVolumeOverTime<vgt\ISpatialAnalysisToolVolumeOverTime>
     ITimeToolTimeProperties<vgt\ITimeToolTimeProperties>
     IAnalysisWorkbenchTypeInfo<vgt\IAnalysisWorkbenchTypeInfo>
     IAnalysisWorkbenchRefTo<vgt\IAnalysisWorkbenchRefTo>
     IAnalysisWorkbenchTemplate<vgt\IAnalysisWorkbenchTemplate>
     IAnalysisWorkbenchInstance<vgt\IAnalysisWorkbenchInstance>
     IVectorGeometryToolPointRefTo<vgt\IVectorGeometryToolPointRefTo>
     IVectorGeometryToolVectorRefTo<vgt\IVectorGeometryToolVectorRefTo>
     IVectorGeometryToolAxesRefTo<vgt\IVectorGeometryToolAxesRefTo>
     IVectorGeometryToolAngleRefTo<vgt\IVectorGeometryToolAngleRefTo>
     IVectorGeometryToolSystemRefTo<vgt\IVectorGeometryToolSystemRefTo>
     IVectorGeometryToolPlaneRefTo<vgt\IVectorGeometryToolPlaneRefTo>
     IVectorGeometryToolAxesLabels<vgt\IVectorGeometryToolAxesLabels>
     IVectorGeometryToolPlaneLabels<vgt\IVectorGeometryToolPlaneLabels>
     IVectorGeometryToolAxesAlignedAndConstrained<vgt\IVectorGeometryToolAxesAlignedAndConstrained>
     IVectorGeometryToolAxesAngularOffset<vgt\IVectorGeometryToolAxesAngularOffset>
     IVectorGeometryToolAxesFixedAtEpoch<vgt\IVectorGeometryToolAxesFixedAtEpoch>
     IVectorGeometryToolAxesBPlane<vgt\IVectorGeometryToolAxesBPlane>
     IVectorGeometryToolAxesCustomScript<vgt\IVectorGeometryToolAxesCustomScript>
     IVectorGeometryToolAxesAttitudeFile<vgt\IVectorGeometryToolAxesAttitudeFile>
     IVectorGeometryToolAxesFixed<vgt\IVectorGeometryToolAxesFixed>
     IVectorGeometryToolAxesModelAttach<vgt\IVectorGeometryToolAxesModelAttach>
     IVectorGeometryToolAxesSpinning<vgt\IVectorGeometryToolAxesSpinning>
     IVectorGeometryToolAxesOnSurface<vgt\IVectorGeometryToolAxesOnSurface>
     IVectorGeometryToolAxesTrajectory<vgt\IVectorGeometryToolAxesTrajectory>
     IVectorGeometryToolAxesLagrangeLibration<vgt\IVectorGeometryToolAxesLagrangeLibration>
     IVectorGeometryToolAxesCommonTasks<vgt\IVectorGeometryToolAxesCommonTasks>
     IVectorGeometryToolAxesAtTimeInstant<vgt\IVectorGeometryToolAxesAtTimeInstant>
     IVectorGeometryToolAxesPlugin<vgt\IVectorGeometryToolAxesPlugin>
     IVectorGeometryToolAngleBetweenVectors<vgt\IVectorGeometryToolAngleBetweenVectors>
     IVectorGeometryToolAngleBetweenPlanes<vgt\IVectorGeometryToolAngleBetweenPlanes>
     IVectorGeometryToolAngleDihedral<vgt\IVectorGeometryToolAngleDihedral>
     IVectorGeometryToolAngleRotation<vgt\IVectorGeometryToolAngleRotation>
     IVectorGeometryToolAngleToPlane<vgt\IVectorGeometryToolAngleToPlane>
     IVectorGeometryToolPlaneNormal<vgt\IVectorGeometryToolPlaneNormal>
     IVectorGeometryToolPlaneQuadrant<vgt\IVectorGeometryToolPlaneQuadrant>
     IVectorGeometryToolPlaneTrajectory<vgt\IVectorGeometryToolPlaneTrajectory>
     IVectorGeometryToolPlaneTriad<vgt\IVectorGeometryToolPlaneTriad>
     IVectorGeometryToolPlaneTwoVector<vgt\IVectorGeometryToolPlaneTwoVector>
     IVectorGeometryToolPointBPlane<vgt\IVectorGeometryToolPointBPlane>
     IVectorGeometryToolPointFile<vgt\IVectorGeometryToolPointFile>
     IVectorGeometryToolPointFixedInSystem<vgt\IVectorGeometryToolPointFixedInSystem>
     IVectorGeometryToolPointGrazing<vgt\IVectorGeometryToolPointGrazing>
     IVectorGeometryToolPointGlint<vgt\IVectorGeometryToolPointGlint>
     IVectorGeometryToolPointCovarianceGrazing<vgt\IVectorGeometryToolPointCovarianceGrazing>
     IVectorGeometryToolPointPlaneIntersection<vgt\IVectorGeometryToolPointPlaneIntersection>
     IVectorGeometryToolPointOnSurface<vgt\IVectorGeometryToolPointOnSurface>
     IVectorGeometryToolPointModelAttach<vgt\IVectorGeometryToolPointModelAttach>
     IVectorGeometryToolPointSatelliteCollectionEntry<vgt\IVectorGeometryToolPointSatelliteCollectionEntry>
     IVectorGeometryToolPointPlaneProjection<vgt\IVectorGeometryToolPointPlaneProjection>
     IVectorGeometryToolPointLagrangeLibration<vgt\IVectorGeometryToolPointLagrangeLibration>
     IVectorGeometryToolPointCommonTasks<vgt\IVectorGeometryToolPointCommonTasks>
     IVectorGeometryToolPointCentBodyIntersect<vgt\IVectorGeometryToolPointCentBodyIntersect>
     IVectorGeometryToolPointAtTimeInstant<vgt\IVectorGeometryToolPointAtTimeInstant>
     IVectorGeometryToolPointPlugin<vgt\IVectorGeometryToolPointPlugin>
     IVectorGeometryToolPointCBFixedOffset<vgt\IVectorGeometryToolPointCBFixedOffset>
     IVectorGeometryToolSystemAssembled<vgt\IVectorGeometryToolSystemAssembled>
     IVectorGeometryToolSystemOnSurface<vgt\IVectorGeometryToolSystemOnSurface>
     IAnalysisWorkbenchLLAPosition<vgt\IAnalysisWorkbenchLLAPosition>
     IVectorGeometryToolSystemCommonTasks<vgt\IVectorGeometryToolSystemCommonTasks>
     IVectorGeometryToolVectorAngleRate<vgt\IVectorGeometryToolVectorAngleRate>
     IVectorGeometryToolVectorApoapsis<vgt\IVectorGeometryToolVectorApoapsis>
     IVectorGeometryToolVectorFixedAtEpoch<vgt\IVectorGeometryToolVectorFixedAtEpoch>
     IVectorGeometryToolVectorAngularVelocity<vgt\IVectorGeometryToolVectorAngularVelocity>
     IVectorGeometryToolVectorConing<vgt\IVectorGeometryToolVectorConing>
     IVectorGeometryToolVectorCross<vgt\IVectorGeometryToolVectorCross>
     IVectorGeometryToolVectorCustomScript<vgt\IVectorGeometryToolVectorCustomScript>
     IVectorGeometryToolVectorDerivative<vgt\IVectorGeometryToolVectorDerivative>
     IVectorGeometryToolVectorDisplacement<vgt\IVectorGeometryToolVectorDisplacement>
     IVectorGeometryToolVectorTwoPlanesIntersection<vgt\IVectorGeometryToolVectorTwoPlanesIntersection>
     IVectorGeometryToolVectorModelAttach<vgt\IVectorGeometryToolVectorModelAttach>
     IVectorGeometryToolVectorProjection<vgt\IVectorGeometryToolVectorProjection>
     IVectorGeometryToolVectorScaled<vgt\IVectorGeometryToolVectorScaled>
     IVectorGeometryToolVectorEccentricity<vgt\IVectorGeometryToolVectorEccentricity>
     IVectorGeometryToolVectorFixedInAxes<vgt\IVectorGeometryToolVectorFixedInAxes>
     IVectorGeometryToolVectorLineOfNodes<vgt\IVectorGeometryToolVectorLineOfNodes>
     IVectorGeometryToolVectorOrbitAngularMomentum<vgt\IVectorGeometryToolVectorOrbitAngularMomentum>
     IVectorGeometryToolVectorOrbitNormal<vgt\IVectorGeometryToolVectorOrbitNormal>
     IVectorGeometryToolVectorPeriapsis<vgt\IVectorGeometryToolVectorPeriapsis>
     IVectorGeometryToolVectorReflection<vgt\IVectorGeometryToolVectorReflection>
     IVectorGeometryToolVectorRotationVector<vgt\IVectorGeometryToolVectorRotationVector>
     IVectorGeometryToolVectorDirectionToStar<vgt\IVectorGeometryToolVectorDirectionToStar>
     IVectorGeometryToolVectorFixedAtTimeInstant<vgt\IVectorGeometryToolVectorFixedAtTimeInstant>
     IVectorGeometryToolVectorLinearCombination<vgt\IVectorGeometryToolVectorLinearCombination>
     IVectorGeometryToolVectorProjectAlongVector<vgt\IVectorGeometryToolVectorProjectAlongVector>
     IVectorGeometryToolVectorScalarLinearCombination<vgt\IVectorGeometryToolVectorScalarLinearCombination>
     IVectorGeometryToolVectorScalarScaled<vgt\IVectorGeometryToolVectorScalarScaled>
     IVectorGeometryToolVectorVelocityAcceleration<vgt\IVectorGeometryToolVectorVelocityAcceleration>
     IVectorGeometryToolVectorPlugin<vgt\IVectorGeometryToolVectorPlugin>
     IVectorGeometryToolVectorDispSurface<vgt\IVectorGeometryToolVectorDispSurface>
     IVectorGeometryToolVectorFactory<vgt\IVectorGeometryToolVectorFactory>
     IVectorGeometryToolAxesFactory<vgt\IVectorGeometryToolAxesFactory>
     IVectorGeometryToolSystemFactory<vgt\IVectorGeometryToolSystemFactory>
     IVectorGeometryToolPointFactory<vgt\IVectorGeometryToolPointFactory>
     IVectorGeometryToolPlaneFactory<vgt\IVectorGeometryToolPlaneFactory>
     IVectorGeometryToolAngleFactory<vgt\IVectorGeometryToolAngleFactory>
     IVectorGeometryToolVectorGroup<vgt\IVectorGeometryToolVectorGroup>
     IVectorGeometryToolPointGroup<vgt\IVectorGeometryToolPointGroup>
     IVectorGeometryToolAngleGroup<vgt\IVectorGeometryToolAngleGroup>
     IVectorGeometryToolAxesGroup<vgt\IVectorGeometryToolAxesGroup>
     IVectorGeometryToolPlaneGroup<vgt\IVectorGeometryToolPlaneGroup>
     IVectorGeometryToolSystemGroup<vgt\IVectorGeometryToolSystemGroup>
     IAnalysisWorkbenchProvider<vgt\IAnalysisWorkbenchProvider>
     IAnalysisWorkbenchRoot<vgt\IAnalysisWorkbenchRoot>
     IVectorGeometryToolWellKnownEarthSystems<vgt\IVectorGeometryToolWellKnownEarthSystems>
     IVectorGeometryToolWellKnownEarthAxes<vgt\IVectorGeometryToolWellKnownEarthAxes>
     IVectorGeometryToolWellKnownSunSystems<vgt\IVectorGeometryToolWellKnownSunSystems>
     IVectorGeometryToolWellKnownSunAxes<vgt\IVectorGeometryToolWellKnownSunAxes>
     IVectorGeometryToolWellKnownSystems<vgt\IVectorGeometryToolWellKnownSystems>
     IVectorGeometryToolWellKnownAxes<vgt\IVectorGeometryToolWellKnownAxes>
     IVectorGeometryToolAngleFindAngleResult<vgt\IVectorGeometryToolAngleFindAngleResult>
     IVectorGeometryToolAngleFindAngleWithRateResult<vgt\IVectorGeometryToolAngleFindAngleWithRateResult>
     IVectorGeometryToolAngleFindWithRateResult<vgt\IVectorGeometryToolAngleFindWithRateResult>
     IVectorGeometryToolAngleFindResult<vgt\IVectorGeometryToolAngleFindResult>
     IVectorGeometryToolAxesTransformResult<vgt\IVectorGeometryToolAxesTransformResult>
     IVectorGeometryToolAxesTransformWithRateResult<vgt\IVectorGeometryToolAxesTransformWithRateResult>
     IVectorGeometryToolPlaneFindInAxesResult<vgt\IVectorGeometryToolPlaneFindInAxesResult>
     IVectorGeometryToolPlaneFindInAxesWithRateResult<vgt\IVectorGeometryToolPlaneFindInAxesWithRateResult>
     IVectorGeometryToolPlaneFindInSystemResult<vgt\IVectorGeometryToolPlaneFindInSystemResult>
     IVectorGeometryToolPlaneFindInSystemWithRateResult<vgt\IVectorGeometryToolPlaneFindInSystemWithRateResult>
     IVectorGeometryToolAxesFindInAxesResult<vgt\IVectorGeometryToolAxesFindInAxesResult>
     IVectorGeometryToolAxesFindInAxesWithRateResult<vgt\IVectorGeometryToolAxesFindInAxesWithRateResult>
     IVectorGeometryToolPointLocateInSystemResult<vgt\IVectorGeometryToolPointLocateInSystemResult>
     IVectorGeometryToolPointLocateInSystemWithRateResult<vgt\IVectorGeometryToolPointLocateInSystemWithRateResult>
     IVectorGeometryToolSystemTransformResult<vgt\IVectorGeometryToolSystemTransformResult>
     IVectorGeometryToolSystemTransformWithRateResult<vgt\IVectorGeometryToolSystemTransformWithRateResult>
     IVectorGeometryToolSystemFindInSystemResult<vgt\IVectorGeometryToolSystemFindInSystemResult>
     IVectorGeometryToolVectorFindInAxesResult<vgt\IVectorGeometryToolVectorFindInAxesResult>
     IVectorGeometryToolVectorFindInAxesWithRateResult<vgt\IVectorGeometryToolVectorFindInAxesWithRateResult>
     IAnalysisWorkbenchMethodCallResult<vgt\IAnalysisWorkbenchMethodCallResult>
     IAnalysisWorkbenchCentralBody<vgt\IAnalysisWorkbenchCentralBody>
     IAnalysisWorkbenchCentralBodyRefTo<vgt\IAnalysisWorkbenchCentralBodyRefTo>
     IAnalysisWorkbenchCentralBodyCollection<vgt\IAnalysisWorkbenchCentralBodyCollection>
     IAnalysisWorkbenchCollection<vgt\IAnalysisWorkbenchCollection>
     ITimeToolPointSamplingResult<vgt\ITimeToolPointSamplingResult>
     ITimeToolPointSamplingInterval<vgt\ITimeToolPointSamplingInterval>
     ITimeToolPointSamplingIntervalCollection<vgt\ITimeToolPointSamplingIntervalCollection>
     ITimeToolAxesSamplingResult<vgt\ITimeToolAxesSamplingResult>
     ITimeToolAxesSamplingInterval<vgt\ITimeToolAxesSamplingInterval>
     ITimeToolAxesSamplingIntervalCollection<vgt\ITimeToolAxesSamplingIntervalCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     CalculationToolEvaluateResult<vgt\CalculationToolEvaluateResult>
     CalculationToolEvaluateWithRateResult<vgt\CalculationToolEvaluateWithRateResult>
     TimeToolEventIntervalResult<vgt\TimeToolEventIntervalResult>
     TimeToolEventFindOccurrenceResult<vgt\TimeToolEventFindOccurrenceResult>
     TimeToolFindTimesResult<vgt\TimeToolFindTimesResult>
     TimeToolIntervalsVectorResult<vgt\TimeToolIntervalsVectorResult>
     TimeToolEventIntervalCollectionOccurredResult<vgt\TimeToolEventIntervalCollectionOccurredResult>
     TimeToolIntervalListResult<vgt\TimeToolIntervalListResult>
     TimeToolIntervalVectorCollection<vgt\TimeToolIntervalVectorCollection>
     TimeToolEventGroup<vgt\TimeToolEventGroup>
     TimeToolEventIntervalGroup<vgt\TimeToolEventIntervalGroup>
     TimeToolEventIntervalListGroup<vgt\TimeToolEventIntervalListGroup>
     TimeToolEventArrayGroup<vgt\TimeToolEventArrayGroup>
     CalculationToolScalarGroup<vgt\CalculationToolScalarGroup>
     TimeToolEventIntervalCollectionGroup<vgt\TimeToolEventIntervalCollectionGroup>
     CalculationToolParameterSetGroup<vgt\CalculationToolParameterSetGroup>
     CalculationToolConditionGroup<vgt\CalculationToolConditionGroup>
     CalculationToolConditionSetGroup<vgt\CalculationToolConditionSetGroup>
     CalculationToolConditionSetEvaluateResult<vgt\CalculationToolConditionSetEvaluateResult>
     CalculationToolConditionSetEvaluateWithRateResult<vgt\CalculationToolConditionSetEvaluateWithRateResult>
     SpatialAnalysisToolVolumeGridGroup<vgt\SpatialAnalysisToolVolumeGridGroup>
     SpatialAnalysisToolVolumeGroup<vgt\SpatialAnalysisToolVolumeGroup>
     SpatialAnalysisToolVolumeCalcGroup<vgt\SpatialAnalysisToolVolumeCalcGroup>
     CalculationToolScalar<vgt\CalculationToolScalar>
     CalculationToolScalarAngle<vgt\CalculationToolScalarAngle>
     CalculationToolScalarAverage<vgt\CalculationToolScalarAverage>
     CalculationToolScalarConstant<vgt\CalculationToolScalarConstant>
     CalculationToolScalarCustom<vgt\CalculationToolScalarCustom>
     CalculationToolScalarCustomInline<vgt\CalculationToolScalarCustomInline>
     CalculationToolScalarDataElement<vgt\CalculationToolScalarDataElement>
     CalculationToolScalarDerivative<vgt\CalculationToolScalarDerivative>
     CalculationToolScalarDotProduct<vgt\CalculationToolScalarDotProduct>
     CalculationToolScalarElapsedTime<vgt\CalculationToolScalarElapsedTime>
     CalculationToolScalarFactory<vgt\CalculationToolScalarFactory>
     CalculationToolScalarFile<vgt\CalculationToolScalarFile>
     CalculationToolScalarFixedAtTimeInstant<vgt\CalculationToolScalarFixedAtTimeInstant>
     CalculationToolScalarFunction<vgt\CalculationToolScalarFunction>
     CalculationToolScalarFunction2Var<vgt\CalculationToolScalarFunction2Var>
     CalculationToolScalarIntegral<vgt\CalculationToolScalarIntegral>
     CalculationToolScalarPlugin<vgt\CalculationToolScalarPlugin>
     CalculationToolScalarPointInVolumeCalc<vgt\CalculationToolScalarPointInVolumeCalc>
     CalculationToolScalarStandardDeviation<vgt\CalculationToolScalarStandardDeviation>
     CalculationToolScalarSurfaceDistanceBetweenPoints<vgt\CalculationToolScalarSurfaceDistanceBetweenPoints>
     CalculationToolScalarVectorComponent<vgt\CalculationToolScalarVectorComponent>
     CalculationToolScalarVectorMagnitude<vgt\CalculationToolScalarVectorMagnitude>
     CalculationToolCondition<vgt\CalculationToolCondition>
     CalculationToolConditionCombined<vgt\CalculationToolConditionCombined>
     CalculationToolConditionFactory<vgt\CalculationToolConditionFactory>
     CalculationToolConditionPointInVolume<vgt\CalculationToolConditionPointInVolume>
     CalculationToolConditionScalarBounds<vgt\CalculationToolConditionScalarBounds>
     CalculationToolConditionSet<vgt\CalculationToolConditionSet>
     CalculationToolConditionSetFactory<vgt\CalculationToolConditionSetFactory>
     CalculationToolConditionSetScalarThresholds<vgt\CalculationToolConditionSetScalarThresholds>
     AnalysisWorkbenchConverge<vgt\AnalysisWorkbenchConverge>
     CalculationToolConvergeBasic<vgt\CalculationToolConvergeBasic>
     AnalysisWorkbenchDerivative<vgt\AnalysisWorkbenchDerivative>
     CalculationToolDerivativeBasic<vgt\CalculationToolDerivativeBasic>
     TimeToolEvent<vgt\TimeToolEvent>
     TimeToolEventArray<vgt\TimeToolEventArray>
     TimeToolEventArrayConditionCrossings<vgt\TimeToolEventArrayConditionCrossings>
     TimeToolEventArrayExtrema<vgt\TimeToolEventArrayExtrema>
     TimeToolEventArrayFactory<vgt\TimeToolEventArrayFactory>
     TimeToolEventArrayFiltered<vgt\TimeToolEventArrayFiltered>
     TimeToolEventArrayFixedStep<vgt\TimeToolEventArrayFixedStep>
     TimeToolEventArrayFixedTimes<vgt\TimeToolEventArrayFixedTimes>
     TimeToolEventArrayMerged<vgt\TimeToolEventArrayMerged>
     TimeToolEventArraySignaled<vgt\TimeToolEventArraySignaled>
     TimeToolEventArrayStartStopTimes<vgt\TimeToolEventArrayStartStopTimes>
     TimeToolEventEpoch<vgt\TimeToolEventEpoch>
     TimeToolEventExtremum<vgt\TimeToolEventExtremum>
     TimeToolEventFactory<vgt\TimeToolEventFactory>
     TimeToolEventInterval<vgt\TimeToolEventInterval>
     TimeToolEventIntervalBetweenTimeInstants<vgt\TimeToolEventIntervalBetweenTimeInstants>
     TimeToolEventIntervalCollection<vgt\TimeToolEventIntervalCollection>
     TimeToolEventIntervalCollectionCondition<vgt\TimeToolEventIntervalCollectionCondition>
     TimeToolEventIntervalCollectionFactory<vgt\TimeToolEventIntervalCollectionFactory>
     TimeToolEventIntervalCollectionLighting<vgt\TimeToolEventIntervalCollectionLighting>
     TimeToolEventIntervalCollectionSignaled<vgt\TimeToolEventIntervalCollectionSignaled>
     TimeToolEventIntervalFactory<vgt\TimeToolEventIntervalFactory>
     TimeToolEventIntervalFixed<vgt\TimeToolEventIntervalFixed>
     TimeToolEventIntervalFixedDuration<vgt\TimeToolEventIntervalFixedDuration>
     TimeToolEventIntervalFromIntervalList<vgt\TimeToolEventIntervalFromIntervalList>
     TimeToolEventIntervalList<vgt\TimeToolEventIntervalList>
     TimeToolEventIntervalListCondition<vgt\TimeToolEventIntervalListCondition>
     TimeToolEventIntervalListFactory<vgt\TimeToolEventIntervalListFactory>
     TimeToolEventIntervalListFile<vgt\TimeToolEventIntervalListFile>
     TimeToolEventIntervalListFiltered<vgt\TimeToolEventIntervalListFiltered>
     TimeToolEventIntervalListFixed<vgt\TimeToolEventIntervalListFixed>
     TimeToolEventIntervalListMerged<vgt\TimeToolEventIntervalListMerged>
     TimeToolEventIntervalListScaled<vgt\TimeToolEventIntervalListScaled>
     TimeToolEventIntervalListSignaled<vgt\TimeToolEventIntervalListSignaled>
     TimeToolEventIntervalListTimeOffset<vgt\TimeToolEventIntervalListTimeOffset>
     TimeToolEventIntervalScaled<vgt\TimeToolEventIntervalScaled>
     TimeToolEventIntervalSignaled<vgt\TimeToolEventIntervalSignaled>
     TimeToolEventIntervalSmartInterval<vgt\TimeToolEventIntervalSmartInterval>
     TimeToolEventIntervalTimeOffset<vgt\TimeToolEventIntervalTimeOffset>
     TimeToolEventSignaled<vgt\TimeToolEventSignaled>
     TimeToolEventSmartEpoch<vgt\TimeToolEventSmartEpoch>
     TimeToolEventStartStopTime<vgt\TimeToolEventStartStopTime>
     TimeToolEventTimeOffset<vgt\TimeToolEventTimeOffset>
     TimeToolFirstIntervalsFilter<vgt\TimeToolFirstIntervalsFilter>
     TimeToolGapsFilter<vgt\TimeToolGapsFilter>
     AnalysisWorkbenchIntegral<vgt\AnalysisWorkbenchIntegral>
     CalculationToolIntegralBasic<vgt\CalculationToolIntegralBasic>
     AnalysisWorkbenchInterp<vgt\AnalysisWorkbenchInterp>
     CalculationToolInterpBasic<vgt\CalculationToolInterpBasic>
     TimeToolIntervalsFilter<vgt\TimeToolIntervalsFilter>
     TimeToolLastIntervalsFilter<vgt\TimeToolLastIntervalsFilter>
     CalculationToolParameterSet<vgt\CalculationToolParameterSet>
     CalculationToolParameterSetAttitude<vgt\CalculationToolParameterSetAttitude>
     CalculationToolParameterSetFactory<vgt\CalculationToolParameterSetFactory>
     CalculationToolParameterSetGroundTrajectory<vgt\CalculationToolParameterSetGroundTrajectory>
     CalculationToolParameterSetOrbit<vgt\CalculationToolParameterSetOrbit>
     CalculationToolParameterSetTrajectory<vgt\CalculationToolParameterSetTrajectory>
     CalculationToolParameterSetVector<vgt\CalculationToolParameterSetVector>
     TimeToolPruneFilter<vgt\TimeToolPruneFilter>
     TimeToolPruneFilterFactory<vgt\TimeToolPruneFilterFactory>
     TimeToolRelativeSatisfactionConditionFilter<vgt\TimeToolRelativeSatisfactionConditionFilter>
     AnalysisWorkbenchSampling<vgt\AnalysisWorkbenchSampling>
     CalculationToolSamplingBasic<vgt\CalculationToolSamplingBasic>
     CalculationToolSamplingCurvatureTolerance<vgt\CalculationToolSamplingCurvatureTolerance>
     CalculationToolSamplingFixedStep<vgt\CalculationToolSamplingFixedStep>
     CalculationToolSamplingMethod<vgt\CalculationToolSamplingMethod>
     CalculationToolSamplingMethodFactory<vgt\CalculationToolSamplingMethodFactory>
     CalculationToolSamplingRelativeTolerance<vgt\CalculationToolSamplingRelativeTolerance>
     TimeToolSatisfactionConditionFilter<vgt\TimeToolSatisfactionConditionFilter>
     AnalysisWorkbenchSignalDelay<vgt\AnalysisWorkbenchSignalDelay>
     TimeToolSignalDelayBasic<vgt\TimeToolSignalDelayBasic>
     SpatialAnalysisToolVolumeCalcFactory<vgt\SpatialAnalysisToolVolumeCalcFactory>
     SpatialAnalysisToolVolumeFactory<vgt\SpatialAnalysisToolVolumeFactory>
     SpatialAnalysisToolVolumeGridFactory<vgt\SpatialAnalysisToolVolumeGridFactory>
     SpatialAnalysisToolGridCoordinateDefinition<vgt\SpatialAnalysisToolGridCoordinateDefinition>
     SpatialAnalysisToolGridValuesCustom<vgt\SpatialAnalysisToolGridValuesCustom>
     SpatialAnalysisToolGridValuesFixedNumberOfSteps<vgt\SpatialAnalysisToolGridValuesFixedNumberOfSteps>
     SpatialAnalysisToolGridValuesFixedStep<vgt\SpatialAnalysisToolGridValuesFixedStep>
     SpatialAnalysisToolGridValuesMethod<vgt\SpatialAnalysisToolGridValuesMethod>
     TimeToolLightTimeDelay<vgt\TimeToolLightTimeDelay>
     SpatialAnalysisToolVolume<vgt\SpatialAnalysisToolVolume>
     SpatialAnalysisToolVolumeCalc<vgt\SpatialAnalysisToolVolumeCalc>
     SpatialAnalysisToolVolumeCalcAltitude<vgt\SpatialAnalysisToolVolumeCalcAltitude>
     SpatialAnalysisToolVolumeCalcAngleOffVector<vgt\SpatialAnalysisToolVolumeCalcAngleOffVector>
     SpatialAnalysisToolVolumeCalcConditionSatMetric<vgt\SpatialAnalysisToolVolumeCalcConditionSatMetric>
     SpatialAnalysisToolVolumeCalcDelayRange<vgt\SpatialAnalysisToolVolumeCalcDelayRange>
     SpatialAnalysisToolVolumeCalcFile<vgt\SpatialAnalysisToolVolumeCalcFile>
     SpatialAnalysisToolVolumeCalcFromScalar<vgt\SpatialAnalysisToolVolumeCalcFromScalar>
     SpatialAnalysisToolVolumeCalcRange<vgt\SpatialAnalysisToolVolumeCalcRange>
     SpatialAnalysisToolVolumeCalcSolarIntensity<vgt\SpatialAnalysisToolVolumeCalcSolarIntensity>
     SpatialAnalysisToolVolumeCombined<vgt\SpatialAnalysisToolVolumeCombined>
     SpatialAnalysisToolVolumeFromCalc<vgt\SpatialAnalysisToolVolumeFromCalc>
     SpatialAnalysisToolVolumeFromCondition<vgt\SpatialAnalysisToolVolumeFromCondition>
     SpatialAnalysisToolVolumeFromGrid<vgt\SpatialAnalysisToolVolumeFromGrid>
     SpatialAnalysisToolVolumeFromTimeSatisfaction<vgt\SpatialAnalysisToolVolumeFromTimeSatisfaction>
     SpatialAnalysisToolVolumeGrid<vgt\SpatialAnalysisToolVolumeGrid>
     SpatialAnalysisToolVolumeGridBearingAlt<vgt\SpatialAnalysisToolVolumeGridBearingAlt>
     SpatialAnalysisToolVolumeGridCartesian<vgt\SpatialAnalysisToolVolumeGridCartesian>
     SpatialAnalysisToolVolumeGridConstrained<vgt\SpatialAnalysisToolVolumeGridConstrained>
     SpatialAnalysisToolVolumeGridCylindrical<vgt\SpatialAnalysisToolVolumeGridCylindrical>
     SpatialAnalysisToolVolumeGridLatLonAlt<vgt\SpatialAnalysisToolVolumeGridLatLonAlt>
     SpatialAnalysisToolVolumeGridResult<vgt\SpatialAnalysisToolVolumeGridResult>
     SpatialAnalysisToolVolumeGridSpherical<vgt\SpatialAnalysisToolVolumeGridSpherical>
     SpatialAnalysisToolVolumeInview<vgt\SpatialAnalysisToolVolumeInview>
     SpatialAnalysisToolVolumeLighting<vgt\SpatialAnalysisToolVolumeLighting>
     SpatialAnalysisToolVolumeOverTime<vgt\SpatialAnalysisToolVolumeOverTime>
     AnalysisWorkbenchGeneric<vgt\AnalysisWorkbenchGeneric>
     AnalysisWorkbenchTypeInfo<vgt\AnalysisWorkbenchTypeInfo>
     AnalysisWorkbenchInstance<vgt\AnalysisWorkbenchInstance>
     AnalysisWorkbenchTemplate<vgt\AnalysisWorkbenchTemplate>
     VectorGeometryToolPointRefTo<vgt\VectorGeometryToolPointRefTo>
     VectorGeometryToolVectorRefTo<vgt\VectorGeometryToolVectorRefTo>
     VectorGeometryToolAxesRefTo<vgt\VectorGeometryToolAxesRefTo>
     VectorGeometryToolAngleRefTo<vgt\VectorGeometryToolAngleRefTo>
     VectorGeometryToolSystemRefTo<vgt\VectorGeometryToolSystemRefTo>
     VectorGeometryToolPlaneRefTo<vgt\VectorGeometryToolPlaneRefTo>
     VectorGeometryToolVector<vgt\VectorGeometryToolVector>
     VectorGeometryToolAxesLabels<vgt\VectorGeometryToolAxesLabels>
     VectorGeometryToolAxes<vgt\VectorGeometryToolAxes>
     VectorGeometryToolPoint<vgt\VectorGeometryToolPoint>
     VectorGeometryToolSystem<vgt\VectorGeometryToolSystem>
     VectorGeometryToolAngle<vgt\VectorGeometryToolAngle>
     VectorGeometryToolPlaneLabels<vgt\VectorGeometryToolPlaneLabels>
     VectorGeometryToolPlane<vgt\VectorGeometryToolPlane>
     VectorGeometryToolAxesAlignedAndConstrained<vgt\VectorGeometryToolAxesAlignedAndConstrained>
     VectorGeometryToolAxesAngularOffset<vgt\VectorGeometryToolAxesAngularOffset>
     VectorGeometryToolAxesFixedAtEpoch<vgt\VectorGeometryToolAxesFixedAtEpoch>
     VectorGeometryToolAxesBPlane<vgt\VectorGeometryToolAxesBPlane>
     VectorGeometryToolAxesCustomScript<vgt\VectorGeometryToolAxesCustomScript>
     VectorGeometryToolAxesAttitudeFile<vgt\VectorGeometryToolAxesAttitudeFile>
     VectorGeometryToolAxesFixed<vgt\VectorGeometryToolAxesFixed>
     VectorGeometryToolAxesModelAttach<vgt\VectorGeometryToolAxesModelAttach>
     VectorGeometryToolAxesSpinning<vgt\VectorGeometryToolAxesSpinning>
     VectorGeometryToolAxesOnSurface<vgt\VectorGeometryToolAxesOnSurface>
     VectorGeometryToolAxesTrajectory<vgt\VectorGeometryToolAxesTrajectory>
     VectorGeometryToolAxesLagrangeLibration<vgt\VectorGeometryToolAxesLagrangeLibration>
     VectorGeometryToolAxesCommonTasks<vgt\VectorGeometryToolAxesCommonTasks>
     VectorGeometryToolAxesAtTimeInstant<vgt\VectorGeometryToolAxesAtTimeInstant>
     VectorGeometryToolAxesPlugin<vgt\VectorGeometryToolAxesPlugin>
     VectorGeometryToolAngleBetweenVectors<vgt\VectorGeometryToolAngleBetweenVectors>
     VectorGeometryToolAngleBetweenPlanes<vgt\VectorGeometryToolAngleBetweenPlanes>
     VectorGeometryToolAngleDihedral<vgt\VectorGeometryToolAngleDihedral>
     VectorGeometryToolAngleRotation<vgt\VectorGeometryToolAngleRotation>
     VectorGeometryToolAngleToPlane<vgt\VectorGeometryToolAngleToPlane>
     VectorGeometryToolPlaneNormal<vgt\VectorGeometryToolPlaneNormal>
     VectorGeometryToolPlaneQuadrant<vgt\VectorGeometryToolPlaneQuadrant>
     VectorGeometryToolPlaneTrajectory<vgt\VectorGeometryToolPlaneTrajectory>
     VectorGeometryToolPlaneTriad<vgt\VectorGeometryToolPlaneTriad>
     VectorGeometryToolPlaneTwoVector<vgt\VectorGeometryToolPlaneTwoVector>
     VectorGeometryToolPointBPlane<vgt\VectorGeometryToolPointBPlane>
     VectorGeometryToolPointFile<vgt\VectorGeometryToolPointFile>
     VectorGeometryToolPointFixedInSystem<vgt\VectorGeometryToolPointFixedInSystem>
     VectorGeometryToolPointGrazing<vgt\VectorGeometryToolPointGrazing>
     VectorGeometryToolPointGlint<vgt\VectorGeometryToolPointGlint>
     VectorGeometryToolPointCovarianceGrazing<vgt\VectorGeometryToolPointCovarianceGrazing>
     VectorGeometryToolPointPlaneIntersection<vgt\VectorGeometryToolPointPlaneIntersection>
     VectorGeometryToolPointOnSurface<vgt\VectorGeometryToolPointOnSurface>
     VectorGeometryToolPointModelAttach<vgt\VectorGeometryToolPointModelAttach>
     VectorGeometryToolPointSatelliteCollectionEntry<vgt\VectorGeometryToolPointSatelliteCollectionEntry>
     VectorGeometryToolPointPlaneProjection<vgt\VectorGeometryToolPointPlaneProjection>
     VectorGeometryToolPointLagrangeLibration<vgt\VectorGeometryToolPointLagrangeLibration>
     VectorGeometryToolPointCommonTasks<vgt\VectorGeometryToolPointCommonTasks>
     VectorGeometryToolPointCentBodyIntersect<vgt\VectorGeometryToolPointCentBodyIntersect>
     VectorGeometryToolPointAtTimeInstant<vgt\VectorGeometryToolPointAtTimeInstant>
     VectorGeometryToolPointPlugin<vgt\VectorGeometryToolPointPlugin>
     VectorGeometryToolPointCBFixedOffset<vgt\VectorGeometryToolPointCBFixedOffset>
     VectorGeometryToolSystemAssembled<vgt\VectorGeometryToolSystemAssembled>
     VectorGeometryToolSystemOnSurface<vgt\VectorGeometryToolSystemOnSurface>
     AnalysisWorkbenchLLAPosition<vgt\AnalysisWorkbenchLLAPosition>
     VectorGeometryToolSystemCommonTasks<vgt\VectorGeometryToolSystemCommonTasks>
     VectorGeometryToolVectorAngleRate<vgt\VectorGeometryToolVectorAngleRate>
     VectorGeometryToolVectorApoapsis<vgt\VectorGeometryToolVectorApoapsis>
     VectorGeometryToolVectorFixedAtEpoch<vgt\VectorGeometryToolVectorFixedAtEpoch>
     VectorGeometryToolVectorAngularVelocity<vgt\VectorGeometryToolVectorAngularVelocity>
     VectorGeometryToolVectorConing<vgt\VectorGeometryToolVectorConing>
     VectorGeometryToolVectorCross<vgt\VectorGeometryToolVectorCross>
     VectorGeometryToolVectorCustomScript<vgt\VectorGeometryToolVectorCustomScript>
     VectorGeometryToolVectorDerivative<vgt\VectorGeometryToolVectorDerivative>
     VectorGeometryToolVectorDisplacement<vgt\VectorGeometryToolVectorDisplacement>
     VectorGeometryToolVectorTwoPlanesIntersection<vgt\VectorGeometryToolVectorTwoPlanesIntersection>
     VectorGeometryToolVectorModelAttach<vgt\VectorGeometryToolVectorModelAttach>
     VectorGeometryToolVectorProjection<vgt\VectorGeometryToolVectorProjection>
     VectorGeometryToolVectorScaled<vgt\VectorGeometryToolVectorScaled>
     VectorGeometryToolVectorEccentricity<vgt\VectorGeometryToolVectorEccentricity>
     VectorGeometryToolVectorFixedInAxes<vgt\VectorGeometryToolVectorFixedInAxes>
     VectorGeometryToolVectorLineOfNodes<vgt\VectorGeometryToolVectorLineOfNodes>
     VectorGeometryToolVectorOrbitAngularMomentum<vgt\VectorGeometryToolVectorOrbitAngularMomentum>
     VectorGeometryToolVectorOrbitNormal<vgt\VectorGeometryToolVectorOrbitNormal>
     VectorGeometryToolVectorPeriapsis<vgt\VectorGeometryToolVectorPeriapsis>
     VectorGeometryToolVectorReflection<vgt\VectorGeometryToolVectorReflection>
     VectorGeometryToolVectorRotationVector<vgt\VectorGeometryToolVectorRotationVector>
     VectorGeometryToolVectorDirectionToStar<vgt\VectorGeometryToolVectorDirectionToStar>
     VectorGeometryToolVectorFixedAtTimeInstant<vgt\VectorGeometryToolVectorFixedAtTimeInstant>
     VectorGeometryToolVectorLinearCombination<vgt\VectorGeometryToolVectorLinearCombination>
     VectorGeometryToolVectorProjectAlongVector<vgt\VectorGeometryToolVectorProjectAlongVector>
     VectorGeometryToolVectorScalarLinearCombination<vgt\VectorGeometryToolVectorScalarLinearCombination>
     VectorGeometryToolVectorScalarScaled<vgt\VectorGeometryToolVectorScalarScaled>
     VectorGeometryToolVectorVelocityAcceleration<vgt\VectorGeometryToolVectorVelocityAcceleration>
     VectorGeometryToolVectorPlugin<vgt\VectorGeometryToolVectorPlugin>
     VectorGeometryToolVectorDispSurface<vgt\VectorGeometryToolVectorDispSurface>
     VectorGeometryToolVectorFactory<vgt\VectorGeometryToolVectorFactory>
     VectorGeometryToolAxesFactory<vgt\VectorGeometryToolAxesFactory>
     VectorGeometryToolSystemFactory<vgt\VectorGeometryToolSystemFactory>
     VectorGeometryToolPointFactory<vgt\VectorGeometryToolPointFactory>
     VectorGeometryToolPlaneFactory<vgt\VectorGeometryToolPlaneFactory>
     VectorGeometryToolAngleFactory<vgt\VectorGeometryToolAngleFactory>
     VectorGeometryToolVectorGroup<vgt\VectorGeometryToolVectorGroup>
     VectorGeometryToolPointGroup<vgt\VectorGeometryToolPointGroup>
     VectorGeometryToolAngleGroup<vgt\VectorGeometryToolAngleGroup>
     VectorGeometryToolAxesGroup<vgt\VectorGeometryToolAxesGroup>
     VectorGeometryToolPlaneGroup<vgt\VectorGeometryToolPlaneGroup>
     VectorGeometryToolSystemGroup<vgt\VectorGeometryToolSystemGroup>
     AnalysisWorkbenchProvider<vgt\AnalysisWorkbenchProvider>
     AnalysisWorkbenchRoot<vgt\AnalysisWorkbenchRoot>
     VectorGeometryToolWellKnownEarthSystems<vgt\VectorGeometryToolWellKnownEarthSystems>
     VectorGeometryToolWellKnownEarthAxes<vgt\VectorGeometryToolWellKnownEarthAxes>
     VectorGeometryToolWellKnownSunSystems<vgt\VectorGeometryToolWellKnownSunSystems>
     VectorGeometryToolWellKnownSunAxes<vgt\VectorGeometryToolWellKnownSunAxes>
     VectorGeometryToolWellKnownSystems<vgt\VectorGeometryToolWellKnownSystems>
     VectorGeometryToolWellKnownAxes<vgt\VectorGeometryToolWellKnownAxes>
     AnalysisWorkbenchMethodCallAngleFindResult<vgt\AnalysisWorkbenchMethodCallAngleFindResult>
     AnalysisWorkbenchMethodCallAngleFindWithRateResult<vgt\AnalysisWorkbenchMethodCallAngleFindWithRateResult>
     AnalysisWorkbenchMethodCallAxesTransformResult<vgt\AnalysisWorkbenchMethodCallAxesTransformResult>
     AnalysisWorkbenchMethodCallAxesTransformWithRateResult<vgt\AnalysisWorkbenchMethodCallAxesTransformWithRateResult>
     AnalysisWorkbenchMethodCallAxesFindInAxesResult<vgt\AnalysisWorkbenchMethodCallAxesFindInAxesResult>
     AnalysisWorkbenchMethodCallAxesFindInAxesWithRateResult<vgt\AnalysisWorkbenchMethodCallAxesFindInAxesWithRateResult>
     AnalysisWorkbenchMethodCallPlaneFindInAxesResult<vgt\AnalysisWorkbenchMethodCallPlaneFindInAxesResult>
     AnalysisWorkbenchMethodCallPlaneFindInAxesWithRateResult<vgt\AnalysisWorkbenchMethodCallPlaneFindInAxesWithRateResult>
     AnalysisWorkbenchMethodCallPlaneFindInSystemResult<vgt\AnalysisWorkbenchMethodCallPlaneFindInSystemResult>
     AnalysisWorkbenchMethodCallPlaneFindInSystemWithRateResult<vgt\AnalysisWorkbenchMethodCallPlaneFindInSystemWithRateResult>
     AnalysisWorkbenchMethodCallPointLocateInSystemResult<vgt\AnalysisWorkbenchMethodCallPointLocateInSystemResult>
     AnalysisWorkbenchMethodCallPointLocateInSystemWithRateResult<vgt\AnalysisWorkbenchMethodCallPointLocateInSystemWithRateResult>
     AnalysisWorkbenchMethodCallSystemTransformResult<vgt\AnalysisWorkbenchMethodCallSystemTransformResult>
     AnalysisWorkbenchMethodCallSystemTransformWithRateResult<vgt\AnalysisWorkbenchMethodCallSystemTransformWithRateResult>
     AnalysisWorkbenchMethodCallSystemFindInSystemResult<vgt\AnalysisWorkbenchMethodCallSystemFindInSystemResult>
     AnalysisWorkbenchMethodCallVectorFindInAxesResult<vgt\AnalysisWorkbenchMethodCallVectorFindInAxesResult>
     AnalysisWorkbenchMethodCallVectorFindInAxesWithRateResult<vgt\AnalysisWorkbenchMethodCallVectorFindInAxesWithRateResult>
     AnalysisWorkbenchMethodCallAngleFindAngleWithRateResult<vgt\AnalysisWorkbenchMethodCallAngleFindAngleWithRateResult>
     AnalysisWorkbenchMethodCallAngleFindAngleResult<vgt\AnalysisWorkbenchMethodCallAngleFindAngleResult>
     TimeToolInterval<vgt\TimeToolInterval>
     TimeToolIntervalCollection<vgt\TimeToolIntervalCollection>
     AnalysisWorkbenchCentralBody<vgt\AnalysisWorkbenchCentralBody>
     AnalysisWorkbenchCentralBodyRefTo<vgt\AnalysisWorkbenchCentralBodyRefTo>
     AnalysisWorkbenchCentralBodyCollection<vgt\AnalysisWorkbenchCentralBodyCollection>
     AnalysisWorkbenchCollection<vgt\AnalysisWorkbenchCollection>
     TimeToolPointSamplingResult<vgt\TimeToolPointSamplingResult>
     TimeToolPointSamplingInterval<vgt\TimeToolPointSamplingInterval>
     TimeToolPointSamplingIntervalCollection<vgt\TimeToolPointSamplingIntervalCollection>
     TimeToolAxesSamplingResult<vgt\TimeToolAxesSamplingResult>
     TimeToolAxesSamplingInterval<vgt\TimeToolAxesSamplingInterval>
     TimeToolAxesSamplingIntervalCollection<vgt\TimeToolAxesSamplingIntervalCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ CRDN_CALC_SCALAR_TYPE<vgt\CRDN_CALC_SCALAR_TYPE>
    ≔ CRDN_CONDITION_COMBINED_OPERATION_TYPE<vgt\CRDN_CONDITION_COMBINED_OPERATION_TYPE>
    ≔ CRDN_CONDITION_SET_TYPE<vgt\CRDN_CONDITION_SET_TYPE>
    ≔ CRDN_CONDITION_THRESHOLD_OPTION<vgt\CRDN_CONDITION_THRESHOLD_OPTION>
    ≔ CRDN_CONDITION_TYPE<vgt\CRDN_CONDITION_TYPE>
    ≔ CRDN_DIMENSION_INHERITANCE<vgt\CRDN_DIMENSION_INHERITANCE>
    ≔ CRDN_EVENT_ARRAY_FILTER_TYPE<vgt\CRDN_EVENT_ARRAY_FILTER_TYPE>
    ≔ CRDN_EVENT_ARRAY_TYPE<vgt\CRDN_EVENT_ARRAY_TYPE>
    ≔ CRDN_EVENT_INTERVAL_COLLECTION_TYPE<vgt\CRDN_EVENT_INTERVAL_COLLECTION_TYPE>
    ≔ CRDN_EVENT_INTERVAL_LIST_TYPE<vgt\CRDN_EVENT_INTERVAL_LIST_TYPE>
    ≔ CRDN_EVENT_INTERVAL_TYPE<vgt\CRDN_EVENT_INTERVAL_TYPE>
    ≔ CRDN_EVENT_LIST_MERGE_OPERATION<vgt\CRDN_EVENT_LIST_MERGE_OPERATION>
    ≔ CRDN_EVENT_TYPE<vgt\CRDN_EVENT_TYPE>
    ≔ CRDN_EXTREMUM_CONSTANTS<vgt\CRDN_EXTREMUM_CONSTANTS>
    ≔ CRDN_FILE_INTERPOLATOR_TYPE<vgt\CRDN_FILE_INTERPOLATOR_TYPE>
    ≔ CRDN_INTEGRAL_TYPE<vgt\CRDN_INTEGRAL_TYPE>
    ≔ CRDN_INTEGRATION_WINDOW_TYPE<vgt\CRDN_INTEGRATION_WINDOW_TYPE>
    ≔ CRDN_INTERPOLATOR_TYPE<vgt\CRDN_INTERPOLATOR_TYPE>
    ≔ CRDN_INTERVAL_DURATION_KIND<vgt\CRDN_INTERVAL_DURATION_KIND>
    ≔ CRDN_INTERVAL_SELECTION<vgt\CRDN_INTERVAL_SELECTION>
    ≔ CRDN_PARAMETER_SET_TYPE<vgt\CRDN_PARAMETER_SET_TYPE>
    ≔ CRDN_PRUNE_FILTER<vgt\CRDN_PRUNE_FILTER>
    ≔ CRDN_SAMPLED_REFERENCE_TIME<vgt\CRDN_SAMPLED_REFERENCE_TIME>
    ≔ CRDN_SAMPLING_METHOD<vgt\CRDN_SAMPLING_METHOD>
    ≔ CRDN_SATISFACTION_CROSSING<vgt\CRDN_SATISFACTION_CROSSING>
    ≔ CRDN_SAVE_DATA_OPTION<vgt\CRDN_SAVE_DATA_OPTION>
    ≔ CRDN_SIGNAL_PATH_REFERENCE_SYSTEM<vgt\CRDN_SIGNAL_PATH_REFERENCE_SYSTEM>
    ≔ CRDN_SMART_EPOCH_STATE<vgt\CRDN_SMART_EPOCH_STATE>
    ≔ CRDN_SMART_INTERVAL_STATE<vgt\CRDN_SMART_INTERVAL_STATE>
    ≔ CRDN_SPEED_OPTIONS<vgt\CRDN_SPEED_OPTIONS>
    ≔ CRDN_START_STOP_OPTION<vgt\CRDN_START_STOP_OPTION>
    ≔ CRDN_THRESH_CONVERGE_SENSE<vgt\CRDN_THRESH_CONVERGE_SENSE>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE<vgt\VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE>
    ≔ CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE<vgt\CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE>
    ≔ CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE<vgt\CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE>
    ≔ CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE<vgt\CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE>
    ≔ CRDN_VOLUME_CALC_RANGE_SPEED_TYPE<vgt\CRDN_VOLUME_CALC_RANGE_SPEED_TYPE>
    ≔ CRDN_VOLUME_CALC_TYPE<vgt\CRDN_VOLUME_CALC_TYPE>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE<vgt\CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE<vgt\CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE<vgt\CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE<vgt\CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE>
    ≔ CRDN_VOLUME_GRID_TYPE<vgt\CRDN_VOLUME_GRID_TYPE>
    ≔ CRDN_VOLUME_RESULT_VECTOR_REQUEST<vgt\CRDN_VOLUME_RESULT_VECTOR_REQUEST>
    ≔ CRDN_VOLUME_TYPE<vgt\CRDN_VOLUME_TYPE>
    ≔ CRDN_VOLUME_ABERRATION_TYPE<vgt\CRDN_VOLUME_ABERRATION_TYPE>
    ≔ CRDN_VOLUME_CLOCK_HOST_TYPE<vgt\CRDN_VOLUME_CLOCK_HOST_TYPE>
    ≔ CRDN_VOLUME_COMBINED_OPERATION_TYPE<vgt\CRDN_VOLUME_COMBINED_OPERATION_TYPE>
    ≔ CRDN_VOLUME_FROM_GRID_EDGE_TYPE<vgt\CRDN_VOLUME_FROM_GRID_EDGE_TYPE>
    ≔ CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE<vgt\CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE>
    ≔ CRDN_VOLUME_OVER_TIME_DURATION_TYPE<vgt\CRDN_VOLUME_OVER_TIME_DURATION_TYPE>
    ≔ CRDN_VOLUME_TIME_SENSE_TYPE<vgt\CRDN_VOLUME_TIME_SENSE_TYPE>
    ≔ CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE<vgt\CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE>
    ≔ CRDN_KIND<vgt\CRDN_KIND>
    ≔ VECTOR_GEOMETRY_TOOL_ANGLE_TYPE<vgt\VECTOR_GEOMETRY_TOOL_ANGLE_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_AXES_TYPE<vgt\VECTOR_GEOMETRY_TOOL_AXES_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_PLANE_TYPE<vgt\VECTOR_GEOMETRY_TOOL_PLANE_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_POINT_TYPE<vgt\VECTOR_GEOMETRY_TOOL_POINT_TYPE>
    ≔ CRDN_SYSTEM_TYPE<vgt\CRDN_SYSTEM_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_TYPE<vgt\VECTOR_GEOMETRY_TOOL_VECTOR_TYPE>
    ≔ CRDN_MEAN_ELEMENT_THEORY<vgt\CRDN_MEAN_ELEMENT_THEORY>
    ≔ CRDN_DIRECTION_TYPE<vgt\CRDN_DIRECTION_TYPE>
    ≔ CRDN_LAGRANGE_LIBRATION_POINT_TYPE<vgt\CRDN_LAGRANGE_LIBRATION_POINT_TYPE>
    ≔ CRDN_QUADRANT_TYPE<vgt\CRDN_QUADRANT_TYPE>
    ≔ CRDN_TRAJECTORY_AXES_TYPE<vgt\CRDN_TRAJECTORY_AXES_TYPE>
    ≔ CRDN_DISPLAY_AXIS_SELECTOR<vgt\CRDN_DISPLAY_AXIS_SELECTOR>
    ≔ CRDN_SIGNED_ANGLE_TYPE<vgt\CRDN_SIGNED_ANGLE_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE<vgt\VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE>
    ≔ CRDN_REFERENCE_SHAPE_TYPE<vgt\CRDN_REFERENCE_SHAPE_TYPE>
    ≔ CRDN_SURFACE_TYPE<vgt\CRDN_SURFACE_TYPE>
    ≔ CRDN_SWEEP_MODE<vgt\CRDN_SWEEP_MODE>
    ≔ CRDN_SIGNAL_SENSE<vgt\CRDN_SIGNAL_SENSE>
    ≔ CRDN_INTERSECTION_SURFACE<vgt\CRDN_INTERSECTION_SURFACE>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE<vgt\VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE>

