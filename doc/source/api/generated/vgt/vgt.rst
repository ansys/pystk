
The ``AgSTKVgtLib`` module
==========================


.. py::module:: ansys.stk.core.vgt


Summary
-------

.. tab-set::
    .. tab-items:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~ITimeToolIntervalCollection`
              - The interface represents a collection of intervals.

            * - :pyclass:`~ITimeToolInterval`
              - The interface represents an interval.

            * - :pyclass:`~IVectorGeometryToolPoint`
              - The interface defines methods and properties common to all points.

            * - :pyclass:`~IVectorGeometryToolVector`
              - The interface defines methods and properties common to all vectors.

            * - :pyclass:`~IVectorGeometryToolSystem`
              - The interface contains methods and properties shared by all VGT systems.

            * - :pyclass:`~IVectorGeometryToolAxes`
              - The interface defines methods and properties common to all axes.

            * - :pyclass:`~IVectorGeometryToolAngle`
              - The interface defines methods and properties common to all angles.

            * - :pyclass:`~IVectorGeometryToolPlane`
              - The interface defines methods and properties common to all VGT planes.

            * - :pyclass:`~IAnalysisWorkbenchContext`
              - The interface represents a context associated with a VGT component. All VGT components are associated with a valid context. A context can represent a VGT instance or a VGT template.

            * - :pyclass:`~IAnalysisWorkbenchComponent`
              - A base interface implemented by all VGT components. The methods and properties of the interface provide type information about the VGT component.

            * - :pyclass:`~ICalculationToolEvaluateResult`
              - Represents the results of evaluating a scalar component using IAgCrdnCalcScalar.Evaluate method.

            * - :pyclass:`~ICalculationToolEvaluateWithRateResult`
              - Represents the results of evaluating a scalar component using IAgCrdnCalcScalar.Evaluate method.

            * - :pyclass:`~ITimeToolEventIntervalResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :pyclass:`~ITimeToolEventFindOccurrenceResult`
              - Contains the results returned with IAgCrdnEvent.FindOccurrence method.

            * - :pyclass:`~ITimeToolFindTimesResult`
              - Return a collection of intervals and an array of times.

            * - :pyclass:`~ITimeToolIntervalsVectorResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.FindIntervalCollection method.

            * - :pyclass:`~ITimeToolEventIntervalCollectionOccurredResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.Occurred method.

            * - :pyclass:`~ITimeToolIntervalListResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :pyclass:`~ITimeToolIntervalVectorCollection`
              - A collection of interval collections.

            * - :pyclass:`~ITimeToolEventGroup`
              - Access or create VGT events associated with an object.

            * - :pyclass:`~ITimeToolEventIntervalGroup`
              - Access or create VGT event intervals associated with an object.

            * - :pyclass:`~ITimeToolEventIntervalListGroup`
              - Access or create VGT event interval lists associated with an object.

            * - :pyclass:`~ITimeToolEventArrayGroup`
              - Access or create VGT event arrays associated with an object.

            * - :pyclass:`~ICalculationToolScalarGroup`
              - Access or create VGT calculation scalars associated with an object or a central body.

            * - :pyclass:`~ITimeToolEventIntervalCollectionGroup`
              - Access or create VGT event interval collections associated with an object.

            * - :pyclass:`~ICalculationToolParameterSetGroup`
              - Access or create VGT parameter sets associated with an object or a central body.

            * - :pyclass:`~ICalculationToolConditionGroup`
              - Access or create VGT conditions associated with an object or a central body.

            * - :pyclass:`~ICalculationToolConditionSetGroup`
              - Allow accessing and creating condition set components.

            * - :pyclass:`~ICalculationToolConditionSetEvaluateResult`
              - Represents the results returned by ConditionSet.Evaluate.

            * - :pyclass:`~ICalculationToolConditionSetEvaluateWithRateResult`
              - Represents the results returned by ConditionSet.EvaluateWithRate.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridGroup`
              - Access or create VGT volume grids associated with an object or a central body.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGroup`
              - Access or create spatial conditions associated with a volume grid.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcGroup`
              - Access or create VGT volume calcs associated with an object or a central body.

            * - :pyclass:`~ICalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :pyclass:`~ICalculationToolScalarAngle`
              - Scalar equal to angular displacement obtained from any angle in VGT.

            * - :pyclass:`~ICalculationToolScalarAverage`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :pyclass:`~ICalculationToolScalarConstant`
              - Constant scalar value of specified dimension.

            * - :pyclass:`~ICalculationToolScalarCustom`
              - A calc scalar based on a scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

            * - :pyclass:`~ICalculationToolScalarCustomInline`
              - A calc scalar based on using an inline scripted algorithm in MATLAB, Perl, VBScript or JScript to define its value and rate.

            * - :pyclass:`~ICalculationToolScalarDataElement`
              - Any time-dependent data element from STK data providers available for parent STK object.

            * - :pyclass:`~ICalculationToolScalarDerivative`
              - Derivative of an input scalar calculation.

            * - :pyclass:`~ICalculationToolScalarDotProduct`
              - Dot product between two vectors.

            * - :pyclass:`~ICalculationToolScalarElapsedTime`
              - Time elapsed since the reference time instant. Negative if in the past.

            * - :pyclass:`~ICalculationToolScalarFactory`
              - The factory creates scalar calculation components.

            * - :pyclass:`~ICalculationToolScalarFile`
              - Tabulated scalar calculation data loaded from specified file - a file with .csc extension.

            * - :pyclass:`~ICalculationToolScalarFixedAtTimeInstant`
              - Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

            * - :pyclass:`~ICalculationToolScalarFunction`
              - Defined by performing the specified function on the input scalar or time instant.

            * - :pyclass:`~ICalculationToolScalarFunction2Var`
              - Defined by performing a function(x,y) on two scalar arguments.

            * - :pyclass:`~ICalculationToolScalarIntegral`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :pyclass:`~ICalculationToolScalarPlugin`
              - Use a scalar calculation plugin.

            * - :pyclass:`~ICalculationToolScalarPointInVolumeCalc`
              - Scalar value of spatial calculation evaluated along trajectory of point.

            * - :pyclass:`~ICalculationToolScalarStandardDeviation`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :pyclass:`~ICalculationToolScalarSurfaceDistanceBetweenPoints`
              - Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

            * - :pyclass:`~ICalculationToolScalarVectorComponent`
              - The specified component of a vector when resolved in the specified axes.

            * - :pyclass:`~ICalculationToolScalarVectorMagnitude`
              - Scalar equal to the magnitude of a specified vector.

            * - :pyclass:`~ICalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :pyclass:`~ICalculationToolConditionCombined`
              - Define a condition which combines multiple conditions.

            * - :pyclass:`~ICalculationToolConditionFactory`
              - The factory creates condition components.

            * - :pyclass:`~ICalculationToolConditionPointInVolume`
              - Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

            * - :pyclass:`~ICalculationToolConditionScalarBounds`
              - Defined by determining if input scalar is within specified bounds; returns +1 if satisfied, -1 if not satisfied and 0 if on boundary.

            * - :pyclass:`~ICalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :pyclass:`~ICalculationToolConditionSetFactory`
              - The factory creates condition set components.

            * - :pyclass:`~ICalculationToolConditionSetScalarThresholds`
              - Condition set based on single scalar calculation compared to set of threshold values.

            * - :pyclass:`~IAnalysisWorkbenchConverge`
              - Represents a base class for convergence definitions.

            * - :pyclass:`~ICalculationToolConvergeBasic`
              - Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

            * - :pyclass:`~IAnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :pyclass:`~ICalculationToolDerivativeBasic`
              - Derivative definition determines how numerical differencing is used to compute derivatives.

            * - :pyclass:`~ITimeToolEvent`
              - Define an event (time instant).

            * - :pyclass:`~ITimeToolEventArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :pyclass:`~ITimeToolEventArrayConditionCrossings`
              - Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

            * - :pyclass:`~ITimeToolEventArrayExtrema`
              - Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :pyclass:`~ITimeToolEventArrayFactory`
              - The factory creates event arrays.

            * - :pyclass:`~ITimeToolEventArrayFiltered`
              - Defined by filtering times from original time array according to specified filtering method.

            * - :pyclass:`~ITimeToolEventArrayFixedStep`
              - Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

            * - :pyclass:`~ITimeToolEventArrayFixedTimes`
              - Array defined by time ordered instants each explicitly specified.

            * - :pyclass:`~ITimeToolEventArrayMerged`
              - Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

            * - :pyclass:`~ITimeToolEventArraySignaled`
              - Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations...

            * - :pyclass:`~ITimeToolEventArrayStartStopTimes`
              - Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

            * - :pyclass:`~ITimeToolEventEpoch`
              - Event set at specified date/time.

            * - :pyclass:`~ITimeToolEventExtremum`
              - Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :pyclass:`~ITimeToolEventFactory`
              - The factory creates events.

            * - :pyclass:`~ITimeToolEventInterval`
              - A single time interval.

            * - :pyclass:`~ITimeToolEventIntervalBetweenTimeInstants`
              - Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

            * - :pyclass:`~ITimeToolEventIntervalCollection`
              - A collection of related interval lists.

            * - :pyclass:`~ITimeToolEventIntervalCollectionCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :pyclass:`~ITimeToolEventIntervalCollectionFactory`
              - The factory creates collections of event interval lists.

            * - :pyclass:`~ITimeToolEventIntervalCollectionLighting`
              - Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

            * - :pyclass:`~ITimeToolEventIntervalCollectionSignaled`
              - Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

            * - :pyclass:`~ITimeToolEventIntervalFactory`
              - The factory creates event intervals.

            * - :pyclass:`~ITimeToolEventIntervalFixed`
              - Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

            * - :pyclass:`~ITimeToolEventIntervalFixedDuration`
              - Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

            * - :pyclass:`~ITimeToolEventIntervalFromIntervalList`
              - Interval created from specified interval list by using one of several selection methods.

            * - :pyclass:`~ITimeToolEventIntervalList`
              - An ordered list of time intervals.

            * - :pyclass:`~ITimeToolEventIntervalListCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :pyclass:`~ITimeToolEventIntervalListFactory`
              - The factory creates event interval lists.

            * - :pyclass:`~ITimeToolEventIntervalListFile`
              - Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

            * - :pyclass:`~ITimeToolEventIntervalListFiltered`
              - Defined by filtering intervals from original interval list using specified filtering method.

            * - :pyclass:`~ITimeToolEventIntervalListFixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

            * - :pyclass:`~ITimeToolEventIntervalListMerged`
              - Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

            * - :pyclass:`~ITimeToolEventIntervalListScaled`
              - Interval List defined by scaling every interval in original interval list using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval is removed from scaled list...

            * - :pyclass:`~ITimeToolEventIntervalListSignaled`
              - Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

            * - :pyclass:`~ITimeToolEventIntervalListTimeOffset`
              - Interval List defined by shifting the specified reference interval list by a fixed time offset.

            * - :pyclass:`~ITimeToolEventIntervalScaled`
              - Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

            * - :pyclass:`~ITimeToolEventIntervalSignaled`
              - Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

            * - :pyclass:`~ITimeToolEventIntervalSmartInterval`
              - A smart interval.

            * - :pyclass:`~ITimeToolEventIntervalTimeOffset`
              - Interval defined by shifting specified reference interval by fixed time offset.

            * - :pyclass:`~ITimeToolEventSignaled`
              - Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

            * - :pyclass:`~ITimeToolEventSmartEpoch`
              - A smart epoch.

            * - :pyclass:`~ITimeToolEventStartStopTime`
              - Event is either start or stop time selected from a reference interval.

            * - :pyclass:`~ITimeToolEventTimeOffset`
              - Event at fixed offset from specified reference event.

            * - :pyclass:`~ITimeToolFirstIntervalsFilter`
              - The filter selects a portion of first intervals.

            * - :pyclass:`~ITimeToolGapsFilter`
              - The filter merges intervals unless they are separated by gaps of at least/most certain duration.

            * - :pyclass:`~IAnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :pyclass:`~ICalculationToolIntegralBasic`
              - Integral definition determines how scalar calculation is numerically integrated.

            * - :pyclass:`~IAnalysisWorkbenchInterp`
              - Represents a base class for interpolation definitions.

            * - :pyclass:`~ICalculationToolInterpBasic`
              - Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

            * - :pyclass:`~ITimeToolIntervalsFilter`
              - The filter selects intervals of at least/most certain duration.

            * - :pyclass:`~ITimeToolLastIntervalsFilter`
              - The filter selects a portion of last intervals.

            * - :pyclass:`~ICalculationToolParameterSet`
              - Parameter set contains various sets of scalar computations.

            * - :pyclass:`~ICalculationToolParameterSetAttitude`
              - Attitude parameter set contains various representations of attitude of one set of axes relative to another.

            * - :pyclass:`~ICalculationToolParameterSetFactory`
              - The factory is used to create instances of available parameter set types.

            * - :pyclass:`~ICalculationToolParameterSetGroundTrajectory`
              - Ground trajectory parameter set contains various representations of trajectory of a point relative to central body reference shape.

            * - :pyclass:`~ICalculationToolParameterSetOrbit`
              - Orbit parameter set contains various trajectory representations of an orbiting point.

            * - :pyclass:`~ICalculationToolParameterSetTrajectory`
              - Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

            * - :pyclass:`~ICalculationToolParameterSetVector`
              - Vector parameter set contains various representations of a vector in a reference set of axes.

            * - :pyclass:`~ITimeToolPruneFilter`
              - A filter used with event interval list pruned class to prune interval lists...

            * - :pyclass:`~ITimeToolPruneFilterFactory`
              - The factory creates pruning filters.

            * - :pyclass:`~ITimeToolRelativeSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

            * - :pyclass:`~IAnalysisWorkbenchSampling`
              - Base sampling interface.

            * - :pyclass:`~ICalculationToolSamplingBasic`
              - Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

            * - :pyclass:`~ICalculationToolSamplingCurvatureTolerance`
              - Curvature tolerance definition includes parameters that determine how scalar data should be sampled based on limits on slope changes between samples.

            * - :pyclass:`~ICalculationToolSamplingFixedStep`
              - Fixed step definition includes parameters that determine how scalar data should be sampled based on fixed steps between samples.

            * - :pyclass:`~ICalculationToolSamplingMethod`
              - A sampling method.

            * - :pyclass:`~ICalculationToolSamplingMethodFactory`
              - The factory creates sampling method components.

            * - :pyclass:`~ICalculationToolSamplingRelativeTolerance`
              - Relative tolerance definition includes parameters that determine how scalar data should be sampled based on limits on difference between actual changes between samples and changes predicted by dead reckoning.

            * - :pyclass:`~ITimeToolSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain duration.

            * - :pyclass:`~IAnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :pyclass:`~ITimeToolSignalDelayBasic`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcFactory`
              - The factory is used to create instances of volume calcs.

            * - :pyclass:`~ISpatialAnalysisToolVolumeFactory`
              - The factory is used to create instances of volumes.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridFactory`
              - The factory is used to create instances of volume grids.

            * - :pyclass:`~ISpatialAnalysisToolGridCoordinateDefinition`
              - Define a set of coordinate values.

            * - :pyclass:`~ISpatialAnalysisToolGridValuesCustom`
              - Fixed step grid values.

            * - :pyclass:`~ISpatialAnalysisToolGridValuesFixedNumberOfSteps`
              - Fixed step grid values.

            * - :pyclass:`~ISpatialAnalysisToolGridValuesFixedStep`
              - Fixed step grid values.

            * - :pyclass:`~ISpatialAnalysisToolGridValuesMethod`
              - A grid values method.

            * - :pyclass:`~ITimeToolLightTimeDelay`
              - Manage Light Time Delay options..

            * - :pyclass:`~ISpatialAnalysisToolVolume`
              - A volume interface. The methods and properties of the interface provide Volume functions.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalc`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcAltitude`
              - A volume calc altitude interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcAngleOffVector`
              - A volume calc angle off vector interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcConditionSatMetric`
              - A volume calc condition satisfaction interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcDelayRange`
              - A volume calc propagation delay to location interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcFile`
              - Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcFromScalar`
              - A volume calc scalar to location interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcRange`
              - A volume calc distance to location interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCalcSolarIntensity`
              - A volume calc solar intensityn interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeCombined`
              - A combined volume interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeFromCalc`
              - An volume from calc volume interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeFromCondition`
              - A volume from conditioninterface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeFromGrid`
              - An over time volume interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeFromTimeSatisfaction`
              - An volume from time satisfaction volume interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridBearingAlt`
              - A volume grid bearing alt (Surface Bearing) interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridCartesian`
              - A volume grid Cartesian interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridConstrained`
              - A volume grid constrained interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridCylindrical`
              - A volume grid cylindrical interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridLatLonAlt`
              - A volume grid lat lon alt (Cartogrographic) interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridResult`
              - An interface that generates Volume Grid results.

            * - :pyclass:`~ISpatialAnalysisToolVolumeGridSpherical`
              - A volume grid spherical interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeInview`
              - An Inview volume interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeLighting`
              - A lighting volume interface.

            * - :pyclass:`~ISpatialAnalysisToolVolumeOverTime`
              - An over time volume interface.

            * - :pyclass:`~ITimeToolTimeProperties`
              - Define methods to compute time properties such as availability and special times.

            * - :pyclass:`~IAnalysisWorkbenchTypeInfo`
              - Provide information about the type of VGT components.

            * - :pyclass:`~IAnalysisWorkbenchRefTo`
              - A base interface for all VGT component references.

            * - :pyclass:`~IAnalysisWorkbenchTemplate`
              - The IAgCrdnTemplate interface enables to obtain information about the STK class that owns the VGT component.

            * - :pyclass:`~IAnalysisWorkbenchInstance`
              - The IAgCrdnInstance interface enables to obtain information about the parent object that owns the VGT component.

            * - :pyclass:`~IVectorGeometryToolPointRefTo`
              - Represents a reference to a VGT point.

            * - :pyclass:`~IVectorGeometryToolVectorRefTo`
              - Represents a reference to a VGT vector.

            * - :pyclass:`~IVectorGeometryToolAxesRefTo`
              - Represents a reference to a VGT axes.

            * - :pyclass:`~IVectorGeometryToolAngleRefTo`
              - Represents a reference to a VGT angle.

            * - :pyclass:`~IVectorGeometryToolSystemRefTo`
              - Represents a reference to a VGT system.

            * - :pyclass:`~IVectorGeometryToolPlaneRefTo`
              - Represents a reference to a VGT plane.

            * - :pyclass:`~IVectorGeometryToolAxesLabels`
              - Allow configuring the VGT axes labels.

            * - :pyclass:`~IVectorGeometryToolPlaneLabels`
              - Allow configuring the X and Y axes labels.

            * - :pyclass:`~IVectorGeometryToolAxesAlignedAndConstrained`
              - Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

            * - :pyclass:`~IVectorGeometryToolAxesAngularOffset`
              - Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

            * - :pyclass:`~IVectorGeometryToolAxesFixedAtEpoch`
              - Axes based on another set fixed at a specified epoch.

            * - :pyclass:`~IVectorGeometryToolAxesBPlane`
              - B-Plane axes using the selected target body and reference vector.

            * - :pyclass:`~IVectorGeometryToolAxesCustomScript`
              - Customized axes offset with respect to a set of reference Axes.

            * - :pyclass:`~IVectorGeometryToolAxesAttitudeFile`
              - Axes specified by data from a file.

            * - :pyclass:`~IVectorGeometryToolAxesFixed`
              - Axes fixed in reference axes.

            * - :pyclass:`~IVectorGeometryToolAxesModelAttach`
              - Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

            * - :pyclass:`~IVectorGeometryToolAxesSpinning`
              - Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

            * - :pyclass:`~IVectorGeometryToolAxesOnSurface`
              - Topocentric axes located at the reference point's projection on the central body.

            * - :pyclass:`~IVectorGeometryToolAxesTrajectory`
              - Axes based on trajectory of the point relative to the reference coordinate system.

            * - :pyclass:`~IVectorGeometryToolAxesLagrangeLibration`
              - Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

            * - :pyclass:`~IVectorGeometryToolAxesCommonTasks`
              - Provide methods to create non-persistent VGT axes components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :pyclass:`~IVectorGeometryToolAxesAtTimeInstant`
              - Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

            * - :pyclass:`~IVectorGeometryToolAxesPlugin`
              - A VGT axes plugin.

            * - :pyclass:`~IVectorGeometryToolAngleBetweenVectors`
              - An angle between two vectors.

            * - :pyclass:`~IVectorGeometryToolAngleBetweenPlanes`
              - An angle between two planes.

            * - :pyclass:`~IVectorGeometryToolAngleDihedral`
              - An angle between two vectors about an axis.

            * - :pyclass:`~IVectorGeometryToolAngleRotation`
              - Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

            * - :pyclass:`~IVectorGeometryToolAngleToPlane`
              - An angle between a vector and a plane.

            * - :pyclass:`~IVectorGeometryToolPlaneNormal`
              - A plane normal to a vector at a given point.

            * - :pyclass:`~IVectorGeometryToolPlaneQuadrant`
              - A plane based on a selected Quadrant of a reference system.

            * - :pyclass:`~IVectorGeometryToolPlaneTrajectory`
              - The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

            * - :pyclass:`~IVectorGeometryToolPlaneTriad`
              - A Plane containing points A, B and ReferencePont with the first axis aligned with the direction from the ReferencePoint to point A and the second axis toward the direction from the ReferencePoint to point B.

            * - :pyclass:`~IVectorGeometryToolPlaneTwoVector`
              - A plane passing through point and containing two given vectors.

            * - :pyclass:`~IVectorGeometryToolPointBPlane`
              - B-Plane point using the selected target body.

            * - :pyclass:`~IVectorGeometryToolPointFile`
              - Point specified by data from a file.

            * - :pyclass:`~IVectorGeometryToolPointFixedInSystem`
              - Point fixed in a reference coordinate system using the selected coordinate type.

            * - :pyclass:`~IVectorGeometryToolPointGrazing`
              - The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

            * - :pyclass:`~IVectorGeometryToolPointGlint`
              - Point on central body surface that reflects from source to observer.

            * - :pyclass:`~IVectorGeometryToolPointCovarianceGrazing`
              - The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

            * - :pyclass:`~IVectorGeometryToolPointPlaneIntersection`
              - Point on a plane located along a given direction looking from a given origin.

            * - :pyclass:`~IVectorGeometryToolPointOnSurface`
              - The detic subpoint of the reference point as projected onto the central body.

            * - :pyclass:`~IVectorGeometryToolPointModelAttach`
              - A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

            * - :pyclass:`~IVectorGeometryToolPointSatelliteCollectionEntry`
              - A point placed at the center of mass of a specified satellite of the satellite collection.

            * - :pyclass:`~IVectorGeometryToolPointPlaneProjection`
              - The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

            * - :pyclass:`~IVectorGeometryToolPointLagrangeLibration`
              - Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

            * - :pyclass:`~IVectorGeometryToolPointCommonTasks`
              - Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :pyclass:`~IVectorGeometryToolPointCentBodyIntersect`
              - Point on central body surface along direction vector originating at source point.

            * - :pyclass:`~IVectorGeometryToolPointAtTimeInstant`
              - Point fixed relative to reference system based on another point evaluated at specified time instant.

            * - :pyclass:`~IVectorGeometryToolPointPlugin`
              - A VGT point plugin.

            * - :pyclass:`~IVectorGeometryToolPointCBFixedOffset`
              - Point specified by fixed components with respect to central body.

            * - :pyclass:`~IVectorGeometryToolSystemAssembled`
              - A system assembled from an origin point and a set of reference axes.

            * - :pyclass:`~IVectorGeometryToolSystemOnSurface`
              - A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

            * - :pyclass:`~IAnalysisWorkbenchLLAPosition`
              - A position represented by the Latitude, longtitude and Latitude.

            * - :pyclass:`~IVectorGeometryToolSystemCommonTasks`
              - Provide methods to create non-persistent VGT coordinate reference frames (systems). Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :pyclass:`~IVectorGeometryToolVectorAngleRate`
              - Angle rate vector perpendicular to the plane in which the angle is defined.

            * - :pyclass:`~IVectorGeometryToolVectorApoapsis`
              - Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

            * - :pyclass:`~IVectorGeometryToolVectorFixedAtEpoch`
              - A vector based on another vector fixed at a specified epoch.

            * - :pyclass:`~IVectorGeometryToolVectorAngularVelocity`
              - Angular velocity vector of one set of axes computed with respect to the reference set.

            * - :pyclass:`~IVectorGeometryToolVectorConing`
              - Vector created by revolving the Reference vector around the About vector with the specified rate.

            * - :pyclass:`~IVectorGeometryToolVectorCross`
              - The vector cross product of two vectors.

            * - :pyclass:`~IVectorGeometryToolVectorCustomScript`
              - Customized vector components defined with respect to reference axes.

            * - :pyclass:`~IVectorGeometryToolVectorDerivative`
              - A vector derivative of a vector computed with respect to specified axes.

            * - :pyclass:`~IVectorGeometryToolVectorDisplacement`
              - Vector defined by its start and end points.

            * - :pyclass:`~IVectorGeometryToolVectorTwoPlanesIntersection`
              - Defined along the intersection of two planes.

            * - :pyclass:`~IVectorGeometryToolVectorModelAttach`
              - Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

            * - :pyclass:`~IVectorGeometryToolVectorProjection`
              - A projection of a vector computed with respect to a reference plane.

            * - :pyclass:`~IVectorGeometryToolVectorScaled`
              - Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

            * - :pyclass:`~IVectorGeometryToolVectorEccentricity`
              - A vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :pyclass:`~IVectorGeometryToolVectorFixedInAxes`
              - Vector fixed in the reference axes using the selected coordinate type.

            * - :pyclass:`~IVectorGeometryToolVectorLineOfNodes`
              - Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

            * - :pyclass:`~IVectorGeometryToolVectorOrbitAngularMomentum`
              - Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :pyclass:`~IVectorGeometryToolVectorOrbitNormal`
              - Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :pyclass:`~IVectorGeometryToolVectorPeriapsis`
              - Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :pyclass:`~IVectorGeometryToolVectorReflection`
              - A vector (incident vector) reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

            * - :pyclass:`~IVectorGeometryToolVectorRotationVector`
              - Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

            * - :pyclass:`~IVectorGeometryToolVectorDirectionToStar`
              - Defined with respect to a star object. For a star object to be available, you must first create one.

            * - :pyclass:`~IVectorGeometryToolVectorFixedAtTimeInstant`
              - Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

            * - :pyclass:`~IVectorGeometryToolVectorLinearCombination`
              - Linear combination of two input vectors.

            * - :pyclass:`~IVectorGeometryToolVectorProjectAlongVector`
              - A projection of a source vector in the direction of another vector.

            * - :pyclass:`~IVectorGeometryToolVectorScalarLinearCombination`
              - Linear combination of two input vectors using scalars.

            * - :pyclass:`~IVectorGeometryToolVectorScalarScaled`
              - Scaled version of the input vector using scalar.

            * - :pyclass:`~IVectorGeometryToolVectorVelocityAcceleration`
              - Velocity vector of a point in a coordinate system.

            * - :pyclass:`~IVectorGeometryToolVectorPlugin`
              - A VGT vector plugin.

            * - :pyclass:`~IVectorGeometryToolVectorDispSurface`
              - Displacement between origin and destination points using surface distance and altitude difference.

            * - :pyclass:`~IVectorGeometryToolVectorFactory`
              - A Factory object to create vectors.

            * - :pyclass:`~IVectorGeometryToolAxesFactory`
              - A Factory object to create axes.

            * - :pyclass:`~IVectorGeometryToolSystemFactory`
              - A Factory interface to create VGT systems.

            * - :pyclass:`~IVectorGeometryToolPointFactory`
              - A Factory object to create points.

            * - :pyclass:`~IVectorGeometryToolPlaneFactory`
              - A Factory object to create VGT planes.

            * - :pyclass:`~IVectorGeometryToolAngleFactory`
              - A Factory object to create angles.

            * - :pyclass:`~IVectorGeometryToolVectorGroup`
              - Access or create VGT vectors associated with an object or a central body.

            * - :pyclass:`~IVectorGeometryToolPointGroup`
              - Access or create VGT points associated with an object or a central body.

            * - :pyclass:`~IVectorGeometryToolAngleGroup`
              - Access or create VGT angles associated with an object or a central body.

            * - :pyclass:`~IVectorGeometryToolAxesGroup`
              - Access or create VGT axes associated with an object or a central body.

            * - :pyclass:`~IVectorGeometryToolPlaneGroup`
              - Represents a single entry point to manipulate VGT Planes associated with an object.

            * - :pyclass:`~IVectorGeometryToolSystemGroup`
              - Access or create VGT systems associated with an object or a central body.

            * - :pyclass:`~IAnalysisWorkbenchProvider`
              - Allow accessing existing Vector Geometry Tool components.

            * - :pyclass:`~IAnalysisWorkbenchRoot`
              - Represents a VGT root object.

            * - :pyclass:`~IVectorGeometryToolWellKnownEarthSystems`
              - Well-known Earth's coordinate systems.

            * - :pyclass:`~IVectorGeometryToolWellKnownEarthAxes`
              - Well-known Earth's axes.

            * - :pyclass:`~IVectorGeometryToolWellKnownSunSystems`
              - The Sun's well-known coordinate reference systems.

            * - :pyclass:`~IVectorGeometryToolWellKnownSunAxes`
              - Well-known Sun's axes.

            * - :pyclass:`~IVectorGeometryToolWellKnownSystems`
              - Well-known coordinate reference systems.

            * - :pyclass:`~IVectorGeometryToolWellKnownAxes`
              - Well-known Axes.

            * - :pyclass:`~IVectorGeometryToolAngleFindAngleResult`
              - Contains the results returned with IAgCrdnAngle.FindAngle method.

            * - :pyclass:`~IVectorGeometryToolAngleFindAngleWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindAngleWithRate method.

            * - :pyclass:`~IVectorGeometryToolAngleFindWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinatesWithRate method.

            * - :pyclass:`~IVectorGeometryToolAngleFindResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinates method.

            * - :pyclass:`~IVectorGeometryToolAxesTransformResult`
              - Contains the results returned with IAgCrdnAxes.TransformFrom method.

            * - :pyclass:`~IVectorGeometryToolAxesTransformWithRateResult`
              - Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

            * - :pyclass:`~IVectorGeometryToolPlaneFindInAxesResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxes method.

            * - :pyclass:`~IVectorGeometryToolPlaneFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxesWithRate method.

            * - :pyclass:`~IVectorGeometryToolPlaneFindInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystem method.

            * - :pyclass:`~IVectorGeometryToolPlaneFindInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :pyclass:`~IVectorGeometryToolAxesFindInAxesResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxes method.

            * - :pyclass:`~IVectorGeometryToolAxesFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxesWithRate method.

            * - :pyclass:`~IVectorGeometryToolPointLocateInSystemResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystem method.

            * - :pyclass:`~IVectorGeometryToolPointLocateInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystemWithRate method.

            * - :pyclass:`~IVectorGeometryToolSystemTransformResult`
              - Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

            * - :pyclass:`~IVectorGeometryToolSystemTransformWithRateResult`
              - Contains the results returned with IAgCrdnSystem.TransformFromWithRate and IAgCrdnSystem.TransformToWithRate methods.

            * - :pyclass:`~IVectorGeometryToolSystemFindInSystemResult`
              - Contains the results returned with IAgCrdnSystem.FindInSystem method.

            * - :pyclass:`~IVectorGeometryToolVectorFindInAxesResult`
              - Contains the results returned with IAgCrdnVector.FindInAxes method.

            * - :pyclass:`~IVectorGeometryToolVectorFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnVector.FindInAxesWithRate method.

            * - :pyclass:`~IAnalysisWorkbenchMethodCallResult`
              - Instances of the interface are used to return the result of a computation.

            * - :pyclass:`~IAnalysisWorkbenchCentralBody`
              - The interface represents a central body.

            * - :pyclass:`~IAnalysisWorkbenchCentralBodyRefTo`
              - Represents a reference to a VGT CentralBody.

            * - :pyclass:`~IAnalysisWorkbenchCentralBodyCollection`
              - A collection of central body names.

            * - :pyclass:`~IAnalysisWorkbenchCollection`
              - A collection of VGT objects.

            * - :pyclass:`~ITimeToolPointSamplingResult`
              - Contains tabulated positions and velocities of a point created by Sample method.

            * - :pyclass:`~ITimeToolPointSamplingInterval`
              - The interface represents an interval with the time, position and velocity arrays.

            * - :pyclass:`~ITimeToolPointSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, position and velocity arrays.

            * - :pyclass:`~ITimeToolAxesSamplingResult`
              - Contains tabulated orientations and angular velocities of axes created by Sample method.

            * - :pyclass:`~ITimeToolAxesSamplingInterval`
              - The interface represents an interval with the time, orientation and velocity arrays.

            * - :pyclass:`~ITimeToolAxesSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, orientation and velocity arrays.

    
    .. tab-items:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~CalculationToolEvaluateResult`
              - Represents the results of evaluating a scalar component.

            * - :pyclass:`~CalculationToolEvaluateWithRateResult`
              - Represents the results of evaluating a scalar component.

            * - :pyclass:`~TimeToolEventIntervalResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :pyclass:`~TimeToolEventFindOccurrenceResult`
              - Contains the results returned with IAgCrdnEvent.FindOccurrence method.

            * - :pyclass:`~TimeToolFindTimesResult`
              - Return a collection of intervals and an array of times.

            * - :pyclass:`~TimeToolIntervalsVectorResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.FindIntervalCollection method.

            * - :pyclass:`~TimeToolEventIntervalCollectionOccurredResult`
              - Contains the results returned with IAgCrdnEventIntervalCollection.Occurred method.

            * - :pyclass:`~TimeToolIntervalListResult`
              - Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

            * - :pyclass:`~TimeToolIntervalVectorCollection`
              - A collection of interval collections.

            * - :pyclass:`~TimeToolEventGroup`
              - Access or create VGT events associated with an object.

            * - :pyclass:`~TimeToolEventIntervalGroup`
              - Access or create VGT event intervals associated with an object.

            * - :pyclass:`~TimeToolEventIntervalListGroup`
              - Access or create VGT event interval lists associated with an object.

            * - :pyclass:`~TimeToolEventArrayGroup`
              - Access or create VGT event arrays associated with an object.

            * - :pyclass:`~CalculationToolScalarGroup`
              - Access or create VGT calculation scalars associated with an object or a central body.

            * - :pyclass:`~TimeToolEventIntervalCollectionGroup`
              - Access or create VGT event interval collections associated with an object.

            * - :pyclass:`~CalculationToolParameterSetGroup`
              - Access or create VGT parameter sets associated with an object or a central body.

            * - :pyclass:`~CalculationToolConditionGroup`
              - Access or create VGT conditions associated with an object or a central body.

            * - :pyclass:`~CalculationToolConditionSetGroup`
              - Allow accessing and creating condition set components.

            * - :pyclass:`~CalculationToolConditionSetEvaluateResult`
              - Represents the results returned by ConditionSet.Evaluate.

            * - :pyclass:`~CalculationToolConditionSetEvaluateWithRateResult`
              - Represents the results returned by ConditionSet.EvaluateWithRate.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridGroup`
              - Access or create VGT volume grids associated with an object or a central body.

            * - :pyclass:`~SpatialAnalysisToolVolumeGroup`
              - Access or create spatial conditions associated with a volume grid.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcGroup`
              - Access or create VGT volume calc associated with an object or a central body.

            * - :pyclass:`~CalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :pyclass:`~CalculationToolScalarAngle`
              - Scalar equal to angular displacement obtained from any angle in VGT.

            * - :pyclass:`~CalculationToolScalarAverage`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :pyclass:`~CalculationToolScalarConstant`
              - Constant scalar value of specified dimension.

            * - :pyclass:`~CalculationToolScalarCustom`
              - A calc scalar based on a scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

            * - :pyclass:`~CalculationToolScalarCustomInline`
              - A calc scalar based on using an inline scripted algorithm in MATLAB, Perl, VBScript or JScript to define its value and rate.

            * - :pyclass:`~CalculationToolScalarDataElement`
              - Any time-dependent data element from STK data providers available for parent STK object.

            * - :pyclass:`~CalculationToolScalarDerivative`
              - Derivative of an input scalar calculation.

            * - :pyclass:`~CalculationToolScalarDotProduct`
              - Dot product between two vectors.

            * - :pyclass:`~CalculationToolScalarElapsedTime`
              - Time elapsed since the reference time instant. Negative if in the past.

            * - :pyclass:`~CalculationToolScalarFactory`
              - The factory creates scalar calculation components.

            * - :pyclass:`~CalculationToolScalarFile`
              - Tabulated scalar calculation data loaded from specified file - a file with .csc extension.

            * - :pyclass:`~CalculationToolScalarFixedAtTimeInstant`
              - Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

            * - :pyclass:`~CalculationToolScalarFunction`
              - Defined by performing the specified function on the input scalar or time instant.

            * - :pyclass:`~CalculationToolScalarFunction2Var`
              - Defined by performing a function(x,y) on two scalar arguments.

            * - :pyclass:`~CalculationToolScalarIntegral`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :pyclass:`~CalculationToolScalarPlugin`
              - Use a scalar calculation plugin.

            * - :pyclass:`~CalculationToolScalarPointInVolumeCalc`
              - Scalar value of spatial calculation evaluated along trajectory of point.

            * - :pyclass:`~CalculationToolScalarStandardDeviation`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :pyclass:`~CalculationToolScalarSurfaceDistanceBetweenPoints`
              - Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

            * - :pyclass:`~CalculationToolScalarVectorComponent`
              - The specified component of a vector when resolved in the specified axes.

            * - :pyclass:`~CalculationToolScalarVectorMagnitude`
              - Scalar equal to the magnitude of a specified vector.

            * - :pyclass:`~CalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :pyclass:`~CalculationToolConditionCombined`
              - Define a condition which combines multiple conditions.

            * - :pyclass:`~CalculationToolConditionFactory`
              - The factory creates condition components.

            * - :pyclass:`~CalculationToolConditionPointInVolume`
              - Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

            * - :pyclass:`~CalculationToolConditionScalarBounds`
              - Defined by determining if input scalar is within specified bounds; returns +1 if satisfied, -1 if not satisfied and 0 if on boundary.

            * - :pyclass:`~CalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :pyclass:`~CalculationToolConditionSetFactory`
              - The factory creates condition set components.

            * - :pyclass:`~CalculationToolConditionSetScalarThresholds`
              - Condition set based on single scalar calculation compared to set of threshold values.

            * - :pyclass:`~AnalysisWorkbenchConverge`
              - Represents a base class for convergence definitions.

            * - :pyclass:`~CalculationToolConvergeBasic`
              - Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

            * - :pyclass:`~AnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :pyclass:`~CalculationToolDerivativeBasic`
              - Derivative definition determines how numerical differencing is used to compute derivatives.

            * - :pyclass:`~TimeToolEvent`
              - Define an event (time instant).

            * - :pyclass:`~TimeToolEventArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :pyclass:`~TimeToolEventArrayConditionCrossings`
              - Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

            * - :pyclass:`~TimeToolEventArrayExtrema`
              - Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :pyclass:`~TimeToolEventArrayFactory`
              - The factory creates event arrays.

            * - :pyclass:`~TimeToolEventArrayFiltered`
              - Defined by filtering times from original time array according to specified filtering method.

            * - :pyclass:`~TimeToolEventArrayFixedStep`
              - Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

            * - :pyclass:`~TimeToolEventArrayFixedTimes`
              - Array defined by time ordered instants each explicitly specified.

            * - :pyclass:`~TimeToolEventArrayMerged`
              - Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

            * - :pyclass:`~TimeToolEventArraySignaled`
              - Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations...

            * - :pyclass:`~TimeToolEventArrayStartStopTimes`
              - Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

            * - :pyclass:`~TimeToolEventEpoch`
              - Event set at specified date/time.

            * - :pyclass:`~TimeToolEventExtremum`
              - Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :pyclass:`~TimeToolEventFactory`
              - The factory creates events.

            * - :pyclass:`~TimeToolEventInterval`
              - A single time interval.

            * - :pyclass:`~TimeToolEventIntervalBetweenTimeInstants`
              - Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

            * - :pyclass:`~TimeToolEventIntervalCollection`
              - A collection of related interval lists.

            * - :pyclass:`~TimeToolEventIntervalCollectionCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :pyclass:`~TimeToolEventIntervalCollectionFactory`
              - The factory creates collections of event interval lists.

            * - :pyclass:`~TimeToolEventIntervalCollectionLighting`
              - Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

            * - :pyclass:`~TimeToolEventIntervalCollectionSignaled`
              - Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

            * - :pyclass:`~TimeToolEventIntervalFactory`
              - The factory creates event intervals.

            * - :pyclass:`~TimeToolEventIntervalFixed`
              - Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

            * - :pyclass:`~TimeToolEventIntervalFixedDuration`
              - Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

            * - :pyclass:`~TimeToolEventIntervalFromIntervalList`
              - Interval created from specified interval list by using one of several selection methods.

            * - :pyclass:`~TimeToolEventIntervalList`
              - An ordered list of time intervals.

            * - :pyclass:`~TimeToolEventIntervalListCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :pyclass:`~TimeToolEventIntervalListFactory`
              - The factory creates event interval lists.

            * - :pyclass:`~TimeToolEventIntervalListFile`
              - Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

            * - :pyclass:`~TimeToolEventIntervalListFiltered`
              - Defined by filtering intervals from original interval list using specified filtering method.

            * - :pyclass:`~TimeToolEventIntervalListFixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

            * - :pyclass:`~TimeToolEventIntervalListMerged`
              - Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

            * - :pyclass:`~TimeToolEventIntervalListScaled`
              - Interval List defined by scaling every interval in original interval list using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval is removed from scaled list...

            * - :pyclass:`~TimeToolEventIntervalListSignaled`
              - Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

            * - :pyclass:`~TimeToolEventIntervalListTimeOffset`
              - Interval List defined by shifting the specified reference interval list by a fixed time offset.

            * - :pyclass:`~TimeToolEventIntervalScaled`
              - Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

            * - :pyclass:`~TimeToolEventIntervalSignaled`
              - Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

            * - :pyclass:`~TimeToolEventIntervalSmartInterval`
              - A smart interval.

            * - :pyclass:`~TimeToolEventIntervalTimeOffset`
              - Interval defined by shifting specified reference interval by fixed time offset.

            * - :pyclass:`~TimeToolEventSignaled`
              - Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

            * - :pyclass:`~TimeToolEventSmartEpoch`
              - A smart epoch.

            * - :pyclass:`~TimeToolEventStartStopTime`
              - Event is either start or stop time selected from a reference interval.

            * - :pyclass:`~TimeToolEventTimeOffset`
              - Event at fixed offset from specified reference event.

            * - :pyclass:`~TimeToolFirstIntervalsFilter`
              - The filter selects a portion of first intervals.

            * - :pyclass:`~TimeToolGapsFilter`
              - The filter merges intervals unless they are separated by gaps of at least/most certain duration.

            * - :pyclass:`~AnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :pyclass:`~CalculationToolIntegralBasic`
              - Integral definition determines how scalar calculation is numerically integrated.

            * - :pyclass:`~AnalysisWorkbenchInterp`
              - Represents a base class for interpolation definitions.

            * - :pyclass:`~CalculationToolInterpBasic`
              - Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

            * - :pyclass:`~TimeToolIntervalsFilter`
              - The filter selects intervals of at least/most certain duration.

            * - :pyclass:`~TimeToolLastIntervalsFilter`
              - The filter selects a portion of last intervals.

            * - :pyclass:`~CalculationToolParameterSet`
              - Parameter set contains various sets of scalar computations.

            * - :pyclass:`~CalculationToolParameterSetAttitude`
              - Attitude parameter set contains various representations of attitude of one set of axes relative to another.

            * - :pyclass:`~CalculationToolParameterSetFactory`
              - The factory is used to create instances of available parameter set types.

            * - :pyclass:`~CalculationToolParameterSetGroundTrajectory`
              - Ground trajectory parameter set contains various representations of trajectory of a point relative to central body reference shape.

            * - :pyclass:`~CalculationToolParameterSetOrbit`
              - Orbit parameter set contains various trajectory representations of an orbiting point.

            * - :pyclass:`~CalculationToolParameterSetTrajectory`
              - Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

            * - :pyclass:`~CalculationToolParameterSetVector`
              - Vector parameter set contains various representations of a vector in a reference set of axes.

            * - :pyclass:`~TimeToolPruneFilter`
              - A filter used with event interval list pruned class to prune interval lists...

            * - :pyclass:`~TimeToolPruneFilterFactory`
              - The factory creates pruning filters.

            * - :pyclass:`~TimeToolRelativeSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

            * - :pyclass:`~AnalysisWorkbenchSampling`
              - Base sampling interface.

            * - :pyclass:`~CalculationToolSamplingBasic`
              - Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

            * - :pyclass:`~CalculationToolSamplingCurvatureTolerance`
              - Curvature tolerance definition includes parameters that determine how scalar data should be sampled based on limits on slope changes between samples.

            * - :pyclass:`~CalculationToolSamplingFixedStep`
              - Fixed step definition includes parameters that determine how scalar data should be sampled based on fixed steps between samples.

            * - :pyclass:`~CalculationToolSamplingMethod`
              - A sampling method.

            * - :pyclass:`~CalculationToolSamplingMethodFactory`
              - The factory creates sampling method components.

            * - :pyclass:`~CalculationToolSamplingRelativeTolerance`
              - Relative tolerance definition includes parameters that determine how scalar data should be sampled based on limits on difference between actual changes between samples and changes predicted by dead reckoning.

            * - :pyclass:`~TimeToolSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain duration.

            * - :pyclass:`~AnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :pyclass:`~TimeToolSignalDelayBasic`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcFactory`
              - The factory is used to create instances of volume calcs.

            * - :pyclass:`~SpatialAnalysisToolVolumeFactory`
              - The factory is used to create instances of volumes.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridFactory`
              - The factory is used to create instances of volume grids.

            * - :pyclass:`~SpatialAnalysisToolGridCoordinateDefinition`
              - Define a set of coordinate values.

            * - :pyclass:`~SpatialAnalysisToolGridValuesCustom`
              - Fixed step grid values.

            * - :pyclass:`~SpatialAnalysisToolGridValuesFixedNumberOfSteps`
              - Fixed step grid values.

            * - :pyclass:`~SpatialAnalysisToolGridValuesFixedStep`
              - Fixed step grid values.

            * - :pyclass:`~SpatialAnalysisToolGridValuesMethod`
              - A grid values method.

            * - :pyclass:`~TimeToolLightTimeDelay`
              - Manage Light Time Delay options..

            * - :pyclass:`~SpatialAnalysisToolVolume`
              - A volume interface. The methods and properties of the interface provide Volume functions.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalc`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcAltitude`
              - A volume calc altitude interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcAngleOffVector`
              - A volume calc angle off vector interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcConditionSatMetric`
              - A volume calc condition satisfaction interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcDelayRange`
              - A volume calc propagation delay to location interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcFile`
              - Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcFromScalar`
              - A volume calc scalar to location interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcRange`
              - A volume calc distance to location interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeCalcSolarIntensity`
              - A volume calc solar intensityn interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeCombined`
              - A combined volume interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeFromCalc`
              - An volume from calc volume interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeFromCondition`
              - A volume from conditioninterface.

            * - :pyclass:`~SpatialAnalysisToolVolumeFromGrid`
              - An over time volume interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeFromTimeSatisfaction`
              - An volume from time satisfaction volume interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridBearingAlt`
              - A volume grid bearing alt (Surface Bearing) interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridCartesian`
              - A volume grid Cartesian interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridConstrained`
              - A volume grid constrained interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridCylindrical`
              - A volume grid cylindrical interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridLatLonAlt`
              - A volume grid lat lon alt (Cartogrographic) interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridResult`
              - An interface that generates Volume Grid results.

            * - :pyclass:`~SpatialAnalysisToolVolumeGridSpherical`
              - A volume grid spherical interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeInview`
              - An Inview volume interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeLighting`
              - A lighting volume interface.

            * - :pyclass:`~SpatialAnalysisToolVolumeOverTime`
              - An over time volume interface.

            * - :pyclass:`~AnalysisWorkbenchGeneric`
              - Generic VGT component.

            * - :pyclass:`~AnalysisWorkbenchTypeInfo`
              - VGT component info.

            * - :pyclass:`~AnalysisWorkbenchInstance`
              - Enable to obtain information about the parent object that owns the VGT component.

            * - :pyclass:`~AnalysisWorkbenchTemplate`
              - Enable to obtain information about the STK class that owns the VGT component.

            * - :pyclass:`~VectorGeometryToolPointRefTo`
              - Represents a reference to a VGT point.

            * - :pyclass:`~VectorGeometryToolVectorRefTo`
              - Represents a vector reference.

            * - :pyclass:`~VectorGeometryToolAxesRefTo`
              - Represents a reference to a VGT axes.

            * - :pyclass:`~VectorGeometryToolAngleRefTo`
              - Represents a reference to a VGT angle.

            * - :pyclass:`~VectorGeometryToolSystemRefTo`
              - Represents a System reference.

            * - :pyclass:`~VectorGeometryToolPlaneRefTo`
              - Represents a Plane reference.

            * - :pyclass:`~VectorGeometryToolVector`
              - A generic vector class.

            * - :pyclass:`~VectorGeometryToolAxesLabels`
              - Allow configuring the VGT axes labels.

            * - :pyclass:`~VectorGeometryToolAxes`
              - A generic axes class.

            * - :pyclass:`~VectorGeometryToolPoint`
              - A generic VGT point class.

            * - :pyclass:`~VectorGeometryToolSystem`
              - Base class for VGT axes.

            * - :pyclass:`~VectorGeometryToolAngle`
              - Base class for VGT axes.

            * - :pyclass:`~VectorGeometryToolPlaneLabels`
              - Allow configuring the X and Y axes labels.

            * - :pyclass:`~VectorGeometryToolPlane`
              - Base class for VGT axes.

            * - :pyclass:`~VectorGeometryToolAxesAlignedAndConstrained`
              - Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

            * - :pyclass:`~VectorGeometryToolAxesAngularOffset`
              - Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

            * - :pyclass:`~VectorGeometryToolAxesFixedAtEpoch`
              - Axes based on another set fixed at a specified epoch.

            * - :pyclass:`~VectorGeometryToolAxesBPlane`
              - B-Plane axes using the selected target body and reference vector.

            * - :pyclass:`~VectorGeometryToolAxesCustomScript`
              - Customized axes offset with respect to a set of reference Axes.

            * - :pyclass:`~VectorGeometryToolAxesAttitudeFile`
              - Axes specified by data from a file.

            * - :pyclass:`~VectorGeometryToolAxesFixed`
              - Axes fixed in reference axes.

            * - :pyclass:`~VectorGeometryToolAxesModelAttach`
              - Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

            * - :pyclass:`~VectorGeometryToolAxesSpinning`
              - Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

            * - :pyclass:`~VectorGeometryToolAxesOnSurface`
              - Topocentric axes located at the reference point's projection on the central body.

            * - :pyclass:`~VectorGeometryToolAxesTrajectory`
              - Axes based on trajectory of the point relative to the reference coordinate system.

            * - :pyclass:`~VectorGeometryToolAxesLagrangeLibration`
              - Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

            * - :pyclass:`~VectorGeometryToolAxesCommonTasks`
              - Provide methods to create non-persistent VGT axes components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :pyclass:`~VectorGeometryToolAxesAtTimeInstant`
              - Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

            * - :pyclass:`~VectorGeometryToolAxesPlugin`
              - A VGT axes plugin.

            * - :pyclass:`~VectorGeometryToolAngleBetweenVectors`
              - An angle between two vectors.

            * - :pyclass:`~VectorGeometryToolAngleBetweenPlanes`
              - An angle between two planes.

            * - :pyclass:`~VectorGeometryToolAngleDihedral`
              - An angle between two vectors about an axis.

            * - :pyclass:`~VectorGeometryToolAngleRotation`
              - Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

            * - :pyclass:`~VectorGeometryToolAngleToPlane`
              - An angle between a vector and a plane.

            * - :pyclass:`~VectorGeometryToolPlaneNormal`
              - A plane normal to a vector at a given point.

            * - :pyclass:`~VectorGeometryToolPlaneQuadrant`
              - A plane based on a selected Quadrant of a reference system.

            * - :pyclass:`~VectorGeometryToolPlaneTrajectory`
              - The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

            * - :pyclass:`~VectorGeometryToolPlaneTriad`
              - A Plane containing points PointA, PointB and ReferencePont with the first axis aligned with the direction from the ReferencePoint to PointA and the second axis toward the direction from the ReferencePoint to PointB.

            * - :pyclass:`~VectorGeometryToolPlaneTwoVector`
              - A plane normal to a vector at a given point.

            * - :pyclass:`~VectorGeometryToolPointBPlane`
              - B-Plane point using the selected target body.

            * - :pyclass:`~VectorGeometryToolPointFile`
              - Point specified by data from a file.

            * - :pyclass:`~VectorGeometryToolPointFixedInSystem`
              - Point fixed in a reference coordinate system using the selected coordinate type.

            * - :pyclass:`~VectorGeometryToolPointGrazing`
              - The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

            * - :pyclass:`~VectorGeometryToolPointGlint`
              - Point on central body surface that reflects from source to observer.

            * - :pyclass:`~VectorGeometryToolPointCovarianceGrazing`
              - The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

            * - :pyclass:`~VectorGeometryToolPointPlaneIntersection`
              - Point on a plane located along a given direction looking from a given origin.

            * - :pyclass:`~VectorGeometryToolPointOnSurface`
              - The detic subpoint of the reference point as projected onto the central body.

            * - :pyclass:`~VectorGeometryToolPointModelAttach`
              - A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

            * - :pyclass:`~VectorGeometryToolPointSatelliteCollectionEntry`
              - A point placed at the center of mass of a specified satellite of the satellite collection.

            * - :pyclass:`~VectorGeometryToolPointPlaneProjection`
              - The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

            * - :pyclass:`~VectorGeometryToolPointLagrangeLibration`
              - Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

            * - :pyclass:`~VectorGeometryToolPointCommonTasks`
              - Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :pyclass:`~VectorGeometryToolPointCentBodyIntersect`
              - Point on central body surface along direction vector originating at source point.

            * - :pyclass:`~VectorGeometryToolPointAtTimeInstant`
              - Point fixed relative to reference system based on another point evaluated at specified time instant.

            * - :pyclass:`~VectorGeometryToolPointPlugin`
              - A VGT point plugin.

            * - :pyclass:`~VectorGeometryToolPointCBFixedOffset`
              - Point specified by fixed components with respect to central body.

            * - :pyclass:`~VectorGeometryToolSystemAssembled`
              - A system assembled from an origin point and a set of reference axes.

            * - :pyclass:`~VectorGeometryToolSystemOnSurface`
              - A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

            * - :pyclass:`~AnalysisWorkbenchLLAPosition`
              - A position represented by the Latitude, longtitude and Latitude.

            * - :pyclass:`~VectorGeometryToolSystemCommonTasks`
              - Provide methods to create non-persistent VGT coordinate reference frames (systems). Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :pyclass:`~VectorGeometryToolVectorAngleRate`
              - Angle rate vector perpendicular to the plane in which the angle is defined.

            * - :pyclass:`~VectorGeometryToolVectorApoapsis`
              - Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

            * - :pyclass:`~VectorGeometryToolVectorFixedAtEpoch`
              - Based on another vector fixed at a specified epoch.

            * - :pyclass:`~VectorGeometryToolVectorAngularVelocity`
              - Angular velocity vector of one set of axes computed with respect to the reference set.

            * - :pyclass:`~VectorGeometryToolVectorConing`
              - Vector created by revolving the Reference vector around the About vector with the specified rate.

            * - :pyclass:`~VectorGeometryToolVectorCross`
              - The vector cross product of two vectors.

            * - :pyclass:`~VectorGeometryToolVectorCustomScript`
              - Customized vector components defined with respect to reference axes.

            * - :pyclass:`~VectorGeometryToolVectorDerivative`
              - A vector derivative of a vector computed with respect to specified axes.

            * - :pyclass:`~VectorGeometryToolVectorDisplacement`
              - Vector defined by its start and end points.

            * - :pyclass:`~VectorGeometryToolVectorTwoPlanesIntersection`
              - Defined along the intersection of two planes.

            * - :pyclass:`~VectorGeometryToolVectorModelAttach`
              - Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

            * - :pyclass:`~VectorGeometryToolVectorProjection`
              - A projection of a vector computed with respect to a reference plane.

            * - :pyclass:`~VectorGeometryToolVectorScaled`
              - Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

            * - :pyclass:`~VectorGeometryToolVectorEccentricity`
              - A vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :pyclass:`~VectorGeometryToolVectorFixedInAxes`
              - Vector fixed in reference axes.

            * - :pyclass:`~VectorGeometryToolVectorLineOfNodes`
              - Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

            * - :pyclass:`~VectorGeometryToolVectorOrbitAngularMomentum`
              - Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :pyclass:`~VectorGeometryToolVectorOrbitNormal`
              - Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :pyclass:`~VectorGeometryToolVectorPeriapsis`
              - Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :pyclass:`~VectorGeometryToolVectorReflection`
              - Incident vector reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

            * - :pyclass:`~VectorGeometryToolVectorRotationVector`
              - Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

            * - :pyclass:`~VectorGeometryToolVectorDirectionToStar`
              - Defined with respect to a star object. For a star object to be available, you must first create one.

            * - :pyclass:`~VectorGeometryToolVectorFixedAtTimeInstant`
              - Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

            * - :pyclass:`~VectorGeometryToolVectorLinearCombination`
              - Linear combination of two input vectors.

            * - :pyclass:`~VectorGeometryToolVectorProjectAlongVector`
              - A projection of a source vector in the direction of another vector.

            * - :pyclass:`~VectorGeometryToolVectorScalarLinearCombination`
              - Linear combination of two input vectors using scalars.

            * - :pyclass:`~VectorGeometryToolVectorScalarScaled`
              - Scaled version of the input vector using scalar.

            * - :pyclass:`~VectorGeometryToolVectorVelocityAcceleration`
              - Velocity vector of a point in a coordinate system.

            * - :pyclass:`~VectorGeometryToolVectorPlugin`
              - A VGT vector plugin.

            * - :pyclass:`~VectorGeometryToolVectorDispSurface`
              - Displacement between origin and destination points using surface distance and altitude difference.

            * - :pyclass:`~VectorGeometryToolVectorFactory`
              - A Factory object to create vectors.

            * - :pyclass:`~VectorGeometryToolAxesFactory`
              - A Factory object to create axes.

            * - :pyclass:`~VectorGeometryToolSystemFactory`
              - A Factory class to create VGT systems.

            * - :pyclass:`~VectorGeometryToolPointFactory`
              - A Factory object to create points.

            * - :pyclass:`~VectorGeometryToolPlaneFactory`
              - A Factory object to create VGT planes.

            * - :pyclass:`~VectorGeometryToolAngleFactory`
              - A Factory object to create angles.

            * - :pyclass:`~VectorGeometryToolVectorGroup`
              - Access or create VGT vectors associated with an object or a central body.

            * - :pyclass:`~VectorGeometryToolPointGroup`
              - Access or create VGT points associated with an object or a central body.

            * - :pyclass:`~VectorGeometryToolAngleGroup`
              - Access or create VGT angles associated with an object or a central body.

            * - :pyclass:`~VectorGeometryToolAxesGroup`
              - Access or create VGT axes associated with an object or a central body.

            * - :pyclass:`~VectorGeometryToolPlaneGroup`
              - Represents a VGT Plane component.

            * - :pyclass:`~VectorGeometryToolSystemGroup`
              - Access or create VGT systems associated with an object or a central body.

            * - :pyclass:`~AnalysisWorkbenchProvider`
              - Allow accessing existing Vector Geometry Tool components.

            * - :pyclass:`~AnalysisWorkbenchRoot`
              - Represents a VGT root.

            * - :pyclass:`~VectorGeometryToolWellKnownEarthSystems`
              - Well-known Earth's coordinate systems.

            * - :pyclass:`~VectorGeometryToolWellKnownEarthAxes`
              - Well-known Earth's axes.

            * - :pyclass:`~VectorGeometryToolWellKnownSunSystems`
              - The Sun's well-known coordinate reference systems.

            * - :pyclass:`~VectorGeometryToolWellKnownSunAxes`
              - Well-known Sun's axes.

            * - :pyclass:`~VectorGeometryToolWellKnownSystems`
              - Well-known coordinate reference systems.

            * - :pyclass:`~VectorGeometryToolWellKnownAxes`
              - Represents well-known VGT Axes.

            * - :pyclass:`~AnalysisWorkbenchMethodCallAngleFindResult`
              - Represents result returned with IAgCrdnAngle.FindCoordinates method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallAngleFindWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindCoordinatesWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallAxesTransformResult`
              - Contains the results returned with IAgCrdnAxes.TransformFrom method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallAxesTransformWithRateResult`
              - Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallAxesFindInAxesResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxes method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallAxesFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnAxes.FindInAxesWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallPlaneFindInAxesResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxes method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallPlaneFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInAxesWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallPlaneFindInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystem method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallPlaneFindInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallPointLocateInSystemResult`
              - Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallPointLocateInSystemWithRateResult`
              - Contains the results returned with IAgCrdnPoint.LocateInSystemWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallSystemTransformResult`
              - Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

            * - :pyclass:`~AnalysisWorkbenchMethodCallSystemTransformWithRateResult`
              - Contains the results returned with IAgCrdnSystem.TransformFromWithRate and IAgCrdnSystem.TransformToWithRate methods.

            * - :pyclass:`~AnalysisWorkbenchMethodCallSystemFindInSystemResult`
              - Contains the results returned with IAgCrdnSystem.FindInSystem method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallVectorFindInAxesResult`
              - Contains the results returned with IAgCrdnVector.FindInAxes method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallVectorFindInAxesWithRateResult`
              - Contains the results returned with IAgCrdnVector.FindInAxesWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallAngleFindAngleWithRateResult`
              - Contains the results returned with IAgCrdnAngle.FindAngleWithRate method.

            * - :pyclass:`~AnalysisWorkbenchMethodCallAngleFindAngleResult`
              - Contains the results returned with IAgCrdnAngle.FindAngle method.

            * - :pyclass:`~TimeToolInterval`
              - Represents an interval.

            * - :pyclass:`~TimeToolIntervalCollection`
              - Represents a collection of intervals.

            * - :pyclass:`~AnalysisWorkbenchCentralBody`
              - Represents an central body.

            * - :pyclass:`~AnalysisWorkbenchCentralBodyRefTo`
              - Represents a central body reference.

            * - :pyclass:`~AnalysisWorkbenchCentralBodyCollection`
              - A collection of central body names.

            * - :pyclass:`~AnalysisWorkbenchCollection`
              - A collection of VGT objects.

            * - :pyclass:`~TimeToolPointSamplingResult`
              - Contains tabulated positions and velocities of a point created by Sample method.

            * - :pyclass:`~TimeToolPointSamplingInterval`
              - The interface represents an interval with the time, position and velocity arrays.

            * - :pyclass:`~TimeToolPointSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, position and velocity arrays.

            * - :pyclass:`~TimeToolAxesSamplingResult`
              - Contains tabulated orientations and angular velocities of axes created by Sample method.

            * - :pyclass:`~TimeToolAxesSamplingInterval`
              - The interface represents an interval with the time, orientation and velocity arrays.

            * - :pyclass:`~TimeToolAxesSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, orientation and velocity arrays.


    .. tab-items:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~CRDN_CALC_SCALAR_TYPE`
              - Define available calculation scalar types.

            * - :pyclass:`~CRDN_CONDITION_COMBINED_OPERATION_TYPE`
              - Define scalar condition combined operation types.

            * - :pyclass:`~CRDN_CONDITION_SET_TYPE`
              - Define available condition set types.

            * - :pyclass:`~CRDN_CONDITION_THRESHOLD_OPTION`
              - Operations for Scalar Bounds Condition.

            * - :pyclass:`~CRDN_CONDITION_TYPE`
              - Define available condition types.

            * - :pyclass:`~CRDN_DIMENSION_INHERITANCE`
              - Define how dimension is inherited.

            * - :pyclass:`~CRDN_EVENT_ARRAY_FILTER_TYPE`
              - Event array filter types.

            * - :pyclass:`~CRDN_EVENT_ARRAY_TYPE`
              - Define available time array types.

            * - :pyclass:`~CRDN_EVENT_INTERVAL_COLLECTION_TYPE`
              - Define available interval collection types.

            * - :pyclass:`~CRDN_EVENT_INTERVAL_LIST_TYPE`
              - Define available interval list types.

            * - :pyclass:`~CRDN_EVENT_INTERVAL_TYPE`
              - Define available interval types.

            * - :pyclass:`~CRDN_EVENT_LIST_MERGE_OPERATION`
              - Define merge operations for interval lists.

            * - :pyclass:`~CRDN_EVENT_TYPE`
              - Define available time instant types.

            * - :pyclass:`~CRDN_EXTREMUM_CONSTANTS`
              - These constants are utilized when finding a local or global minimum or maximum, or the threshold crossing.

            * - :pyclass:`~CRDN_FILE_INTERPOLATOR_TYPE`
              - Interpolator types.

            * - :pyclass:`~CRDN_INTEGRAL_TYPE`
              - Integral types.

            * - :pyclass:`~CRDN_INTEGRATION_WINDOW_TYPE`
              - Define the interval of times during which an integral is evaluated.

            * - :pyclass:`~CRDN_INTERPOLATOR_TYPE`
              - Interpolator types.

            * - :pyclass:`~CRDN_INTERVAL_DURATION_KIND`
              - Duration for filtering intervals or gaps from interval lists or time arrays.

            * - :pyclass:`~CRDN_INTERVAL_SELECTION`
              - Select the method to choose an interval from an interval list.

            * - :pyclass:`~CRDN_PARAMETER_SET_TYPE`
              - Define parameter set types.

            * - :pyclass:`~CRDN_PRUNE_FILTER`
              - Specify the filter for filtering interval lists or time arrays.

            * - :pyclass:`~CRDN_SAMPLED_REFERENCE_TIME`
              - Event array reference type.

            * - :pyclass:`~CRDN_SAMPLING_METHOD`
              - Define the Sampling Method.

            * - :pyclass:`~CRDN_SATISFACTION_CROSSING`
              - Direction crossing flags.

            * - :pyclass:`~CRDN_SAVE_DATA_OPTION`
              - Method for saving computed data.

            * - :pyclass:`~CRDN_SIGNAL_PATH_REFERENCE_SYSTEM`
              - Signal path reference system types.

            * - :pyclass:`~CRDN_SMART_EPOCH_STATE`
              - Smart epoch states.

            * - :pyclass:`~CRDN_SMART_INTERVAL_STATE`
              - Smart interval states.

            * - :pyclass:`~CRDN_SPEED_OPTIONS`
              - Define various speed options.

            * - :pyclass:`~CRDN_START_STOP_OPTION`
              - Start/stop options.

            * - :pyclass:`~CRDN_THRESH_CONVERGE_SENSE`
              - Specify the desired sense of the results from threshold crossing computations.

            * - :pyclass:`~VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE`
              - Define component directions for a vector.

            * - :pyclass:`~CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE`
              - Define volume calc altitude reference types.

            * - :pyclass:`~CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE`
              - Define volume calc angle off vector reference types.

            * - :pyclass:`~CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE`
              - Define volume calc range distance types.

            * - :pyclass:`~CRDN_VOLUME_CALC_RANGE_SPEED_TYPE`
              - Define volume calc range distance types.

            * - :pyclass:`~CRDN_VOLUME_CALC_TYPE`
              - Define volume calc types.

            * - :pyclass:`~CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE`
              - Define volume calc spatial condition accumulation types.

            * - :pyclass:`~CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE`
              - Define volume calc spatial condition duration types.

            * - :pyclass:`~CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE`
              - Define volume calc spatial condition filter types.

            * - :pyclass:`~CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE`
              - Define volume calc spatial condition satisfaction metric types.

            * - :pyclass:`~CRDN_VOLUME_GRID_TYPE`
              - Define volume grid types.

            * - :pyclass:`~CRDN_VOLUME_RESULT_VECTOR_REQUEST`
              - Define volume result vector request types.

            * - :pyclass:`~CRDN_VOLUME_TYPE`
              - Define volume grid types.

            * - :pyclass:`~CRDN_VOLUME_ABERRATION_TYPE`
              - Define the model of aberration to use.

            * - :pyclass:`~CRDN_VOLUME_CLOCK_HOST_TYPE`
              - Define whether base or target of an Access instance holds the clock for Access times.

            * - :pyclass:`~CRDN_VOLUME_COMBINED_OPERATION_TYPE`
              - Define spatial condition combined operation types.

            * - :pyclass:`~CRDN_VOLUME_FROM_GRID_EDGE_TYPE`
              - Define spatial condition from grid edge type.

            * - :pyclass:`~CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE`
              - Define spatial condition lighting conditions types.

            * - :pyclass:`~CRDN_VOLUME_OVER_TIME_DURATION_TYPE`
              - Define spatial condition over time duration type.

            * - :pyclass:`~CRDN_VOLUME_TIME_SENSE_TYPE`
              - Define whether object1 or object2 of an Access instance holds the clock for Access times.

            * - :pyclass:`~CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE`
              - Define volumetric grid values method types.

            * - :pyclass:`~CRDN_KIND`
              - Represents kinds of vectory geometry components.

            * - :pyclass:`~VECTOR_GEOMETRY_TOOL_ANGLE_TYPE`
              - Represents angle types.

            * - :pyclass:`~VECTOR_GEOMETRY_TOOL_AXES_TYPE`
              - Represents vector types.

            * - :pyclass:`~VECTOR_GEOMETRY_TOOL_PLANE_TYPE`
              - Represents plane types.

            * - :pyclass:`~VECTOR_GEOMETRY_TOOL_POINT_TYPE`
              - Represents point types.

            * - :pyclass:`~CRDN_SYSTEM_TYPE`
              - Represents system types.

            * - :pyclass:`~VECTOR_GEOMETRY_TOOL_VECTOR_TYPE`
              - Represents vector types.

            * - :pyclass:`~CRDN_MEAN_ELEMENT_THEORY`
              - Mean element theory types for approximating motion.

            * - :pyclass:`~CRDN_DIRECTION_TYPE`
              - Direction options.

            * - :pyclass:`~CRDN_LAGRANGE_LIBRATION_POINT_TYPE`
              - Types of the Lagrange points, also known as libration points. Lagrange points are points in space where gravitational forces and the orbital motion of a body balance each other.

            * - :pyclass:`~CRDN_QUADRANT_TYPE`
              - Quadrants from a reference system (e.g., XY, XZ, YZ, YX, ZX, ZY).

            * - :pyclass:`~CRDN_TRAJECTORY_AXES_TYPE`
              - Trajectory axes coordinate types.

            * - :pyclass:`~CRDN_DISPLAY_AXIS_SELECTOR`
              - Rotation directions.

            * - :pyclass:`~CRDN_SIGNED_ANGLE_TYPE`
              - Define options for computing an angle.

            * - :pyclass:`~VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE`
              - B-Plane point types.

            * - :pyclass:`~CRDN_REFERENCE_SHAPE_TYPE`
              - Surface shape types.

            * - :pyclass:`~CRDN_SURFACE_TYPE`
              - Surface types.

            * - :pyclass:`~CRDN_SWEEP_MODE`
              - The rotation sweeping modes.

            * - :pyclass:`~CRDN_SIGNAL_SENSE`
              - Signal sense transmission options.

            * - :pyclass:`~CRDN_INTERSECTION_SURFACE`
              - Intersection surface flags.

            * - :pyclass:`~VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE`
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

    --> ITimeToolIntervalCollection<ITimeToolIntervalCollection>
    --> ITimeToolInterval<ITimeToolInterval>
    --> IVectorGeometryToolPoint<IVectorGeometryToolPoint>
    --> IVectorGeometryToolVector<IVectorGeometryToolVector>
    --> IVectorGeometryToolSystem<IVectorGeometryToolSystem>
    --> IVectorGeometryToolAxes<IVectorGeometryToolAxes>
    --> IVectorGeometryToolAngle<IVectorGeometryToolAngle>
    --> IVectorGeometryToolPlane<IVectorGeometryToolPlane>
    --> IAnalysisWorkbenchContext<IAnalysisWorkbenchContext>
    --> IAnalysisWorkbenchComponent<IAnalysisWorkbenchComponent>
    --> ICalculationToolEvaluateResult<ICalculationToolEvaluateResult>
    --> ICalculationToolEvaluateWithRateResult<ICalculationToolEvaluateWithRateResult>
    --> ITimeToolEventIntervalResult<ITimeToolEventIntervalResult>
    --> ITimeToolEventFindOccurrenceResult<ITimeToolEventFindOccurrenceResult>
    --> ITimeToolFindTimesResult<ITimeToolFindTimesResult>
    --> ITimeToolIntervalsVectorResult<ITimeToolIntervalsVectorResult>
    --> ITimeToolEventIntervalCollectionOccurredResult<ITimeToolEventIntervalCollectionOccurredResult>
    --> ITimeToolIntervalListResult<ITimeToolIntervalListResult>
    --> ITimeToolIntervalVectorCollection<ITimeToolIntervalVectorCollection>
    --> ITimeToolEventGroup<ITimeToolEventGroup>
    --> ITimeToolEventIntervalGroup<ITimeToolEventIntervalGroup>
    --> ITimeToolEventIntervalListGroup<ITimeToolEventIntervalListGroup>
    --> ITimeToolEventArrayGroup<ITimeToolEventArrayGroup>
    --> ICalculationToolScalarGroup<ICalculationToolScalarGroup>
    --> ITimeToolEventIntervalCollectionGroup<ITimeToolEventIntervalCollectionGroup>
    --> ICalculationToolParameterSetGroup<ICalculationToolParameterSetGroup>
    --> ICalculationToolConditionGroup<ICalculationToolConditionGroup>
    --> ICalculationToolConditionSetGroup<ICalculationToolConditionSetGroup>
    --> ICalculationToolConditionSetEvaluateResult<ICalculationToolConditionSetEvaluateResult>
    --> ICalculationToolConditionSetEvaluateWithRateResult<ICalculationToolConditionSetEvaluateWithRateResult>
    --> ISpatialAnalysisToolVolumeGridGroup<ISpatialAnalysisToolVolumeGridGroup>
    --> ISpatialAnalysisToolVolumeGroup<ISpatialAnalysisToolVolumeGroup>
    --> ISpatialAnalysisToolVolumeCalcGroup<ISpatialAnalysisToolVolumeCalcGroup>
    --> ICalculationToolScalar<ICalculationToolScalar>
    --> ICalculationToolScalarAngle<ICalculationToolScalarAngle>
    --> ICalculationToolScalarAverage<ICalculationToolScalarAverage>
    --> ICalculationToolScalarConstant<ICalculationToolScalarConstant>
    --> ICalculationToolScalarCustom<ICalculationToolScalarCustom>
    --> ICalculationToolScalarCustomInline<ICalculationToolScalarCustomInline>
    --> ICalculationToolScalarDataElement<ICalculationToolScalarDataElement>
    --> ICalculationToolScalarDerivative<ICalculationToolScalarDerivative>
    --> ICalculationToolScalarDotProduct<ICalculationToolScalarDotProduct>
    --> ICalculationToolScalarElapsedTime<ICalculationToolScalarElapsedTime>
    --> ICalculationToolScalarFactory<ICalculationToolScalarFactory>
    --> ICalculationToolScalarFile<ICalculationToolScalarFile>
    --> ICalculationToolScalarFixedAtTimeInstant<ICalculationToolScalarFixedAtTimeInstant>
    --> ICalculationToolScalarFunction<ICalculationToolScalarFunction>
    --> ICalculationToolScalarFunction2Var<ICalculationToolScalarFunction2Var>
    --> ICalculationToolScalarIntegral<ICalculationToolScalarIntegral>
    --> ICalculationToolScalarPlugin<ICalculationToolScalarPlugin>
    --> ICalculationToolScalarPointInVolumeCalc<ICalculationToolScalarPointInVolumeCalc>
    --> ICalculationToolScalarStandardDeviation<ICalculationToolScalarStandardDeviation>
    --> ICalculationToolScalarSurfaceDistanceBetweenPoints<ICalculationToolScalarSurfaceDistanceBetweenPoints>
    --> ICalculationToolScalarVectorComponent<ICalculationToolScalarVectorComponent>
    --> ICalculationToolScalarVectorMagnitude<ICalculationToolScalarVectorMagnitude>
    --> ICalculationToolCondition<ICalculationToolCondition>
    --> ICalculationToolConditionCombined<ICalculationToolConditionCombined>
    --> ICalculationToolConditionFactory<ICalculationToolConditionFactory>
    --> ICalculationToolConditionPointInVolume<ICalculationToolConditionPointInVolume>
    --> ICalculationToolConditionScalarBounds<ICalculationToolConditionScalarBounds>
    --> ICalculationToolConditionSet<ICalculationToolConditionSet>
    --> ICalculationToolConditionSetFactory<ICalculationToolConditionSetFactory>
    --> ICalculationToolConditionSetScalarThresholds<ICalculationToolConditionSetScalarThresholds>
    --> IAnalysisWorkbenchConverge<IAnalysisWorkbenchConverge>
    --> ICalculationToolConvergeBasic<ICalculationToolConvergeBasic>
    --> IAnalysisWorkbenchDerivative<IAnalysisWorkbenchDerivative>
    --> ICalculationToolDerivativeBasic<ICalculationToolDerivativeBasic>
    --> ITimeToolEvent<ITimeToolEvent>
    --> ITimeToolEventArray<ITimeToolEventArray>
    --> ITimeToolEventArrayConditionCrossings<ITimeToolEventArrayConditionCrossings>
    --> ITimeToolEventArrayExtrema<ITimeToolEventArrayExtrema>
    --> ITimeToolEventArrayFactory<ITimeToolEventArrayFactory>
    --> ITimeToolEventArrayFiltered<ITimeToolEventArrayFiltered>
    --> ITimeToolEventArrayFixedStep<ITimeToolEventArrayFixedStep>
    --> ITimeToolEventArrayFixedTimes<ITimeToolEventArrayFixedTimes>
    --> ITimeToolEventArrayMerged<ITimeToolEventArrayMerged>
    --> ITimeToolEventArraySignaled<ITimeToolEventArraySignaled>
    --> ITimeToolEventArrayStartStopTimes<ITimeToolEventArrayStartStopTimes>
    --> ITimeToolEventEpoch<ITimeToolEventEpoch>
    --> ITimeToolEventExtremum<ITimeToolEventExtremum>
    --> ITimeToolEventFactory<ITimeToolEventFactory>
    --> ITimeToolEventInterval<ITimeToolEventInterval>
    --> ITimeToolEventIntervalBetweenTimeInstants<ITimeToolEventIntervalBetweenTimeInstants>
    --> ITimeToolEventIntervalCollection<ITimeToolEventIntervalCollection>
    --> ITimeToolEventIntervalCollectionCondition<ITimeToolEventIntervalCollectionCondition>
    --> ITimeToolEventIntervalCollectionFactory<ITimeToolEventIntervalCollectionFactory>
    --> ITimeToolEventIntervalCollectionLighting<ITimeToolEventIntervalCollectionLighting>
    --> ITimeToolEventIntervalCollectionSignaled<ITimeToolEventIntervalCollectionSignaled>
    --> ITimeToolEventIntervalFactory<ITimeToolEventIntervalFactory>
    --> ITimeToolEventIntervalFixed<ITimeToolEventIntervalFixed>
    --> ITimeToolEventIntervalFixedDuration<ITimeToolEventIntervalFixedDuration>
    --> ITimeToolEventIntervalFromIntervalList<ITimeToolEventIntervalFromIntervalList>
    --> ITimeToolEventIntervalList<ITimeToolEventIntervalList>
    --> ITimeToolEventIntervalListCondition<ITimeToolEventIntervalListCondition>
    --> ITimeToolEventIntervalListFactory<ITimeToolEventIntervalListFactory>
    --> ITimeToolEventIntervalListFile<ITimeToolEventIntervalListFile>
    --> ITimeToolEventIntervalListFiltered<ITimeToolEventIntervalListFiltered>
    --> ITimeToolEventIntervalListFixed<ITimeToolEventIntervalListFixed>
    --> ITimeToolEventIntervalListMerged<ITimeToolEventIntervalListMerged>
    --> ITimeToolEventIntervalListScaled<ITimeToolEventIntervalListScaled>
    --> ITimeToolEventIntervalListSignaled<ITimeToolEventIntervalListSignaled>
    --> ITimeToolEventIntervalListTimeOffset<ITimeToolEventIntervalListTimeOffset>
    --> ITimeToolEventIntervalScaled<ITimeToolEventIntervalScaled>
    --> ITimeToolEventIntervalSignaled<ITimeToolEventIntervalSignaled>
    --> ITimeToolEventIntervalSmartInterval<ITimeToolEventIntervalSmartInterval>
    --> ITimeToolEventIntervalTimeOffset<ITimeToolEventIntervalTimeOffset>
    --> ITimeToolEventSignaled<ITimeToolEventSignaled>
    --> ITimeToolEventSmartEpoch<ITimeToolEventSmartEpoch>
    --> ITimeToolEventStartStopTime<ITimeToolEventStartStopTime>
    --> ITimeToolEventTimeOffset<ITimeToolEventTimeOffset>
    --> ITimeToolFirstIntervalsFilter<ITimeToolFirstIntervalsFilter>
    --> ITimeToolGapsFilter<ITimeToolGapsFilter>
    --> IAnalysisWorkbenchIntegral<IAnalysisWorkbenchIntegral>
    --> ICalculationToolIntegralBasic<ICalculationToolIntegralBasic>
    --> IAnalysisWorkbenchInterp<IAnalysisWorkbenchInterp>
    --> ICalculationToolInterpBasic<ICalculationToolInterpBasic>
    --> ITimeToolIntervalsFilter<ITimeToolIntervalsFilter>
    --> ITimeToolLastIntervalsFilter<ITimeToolLastIntervalsFilter>
    --> ICalculationToolParameterSet<ICalculationToolParameterSet>
    --> ICalculationToolParameterSetAttitude<ICalculationToolParameterSetAttitude>
    --> ICalculationToolParameterSetFactory<ICalculationToolParameterSetFactory>
    --> ICalculationToolParameterSetGroundTrajectory<ICalculationToolParameterSetGroundTrajectory>
    --> ICalculationToolParameterSetOrbit<ICalculationToolParameterSetOrbit>
    --> ICalculationToolParameterSetTrajectory<ICalculationToolParameterSetTrajectory>
    --> ICalculationToolParameterSetVector<ICalculationToolParameterSetVector>
    --> ITimeToolPruneFilter<ITimeToolPruneFilter>
    --> ITimeToolPruneFilterFactory<ITimeToolPruneFilterFactory>
    --> ITimeToolRelativeSatisfactionConditionFilter<ITimeToolRelativeSatisfactionConditionFilter>
    --> IAnalysisWorkbenchSampling<IAnalysisWorkbenchSampling>
    --> ICalculationToolSamplingBasic<ICalculationToolSamplingBasic>
    --> ICalculationToolSamplingCurvatureTolerance<ICalculationToolSamplingCurvatureTolerance>
    --> ICalculationToolSamplingFixedStep<ICalculationToolSamplingFixedStep>
    --> ICalculationToolSamplingMethod<ICalculationToolSamplingMethod>
    --> ICalculationToolSamplingMethodFactory<ICalculationToolSamplingMethodFactory>
    --> ICalculationToolSamplingRelativeTolerance<ICalculationToolSamplingRelativeTolerance>
    --> ITimeToolSatisfactionConditionFilter<ITimeToolSatisfactionConditionFilter>
    --> IAnalysisWorkbenchSignalDelay<IAnalysisWorkbenchSignalDelay>
    --> ITimeToolSignalDelayBasic<ITimeToolSignalDelayBasic>
    --> ISpatialAnalysisToolVolumeCalcFactory<ISpatialAnalysisToolVolumeCalcFactory>
    --> ISpatialAnalysisToolVolumeFactory<ISpatialAnalysisToolVolumeFactory>
    --> ISpatialAnalysisToolVolumeGridFactory<ISpatialAnalysisToolVolumeGridFactory>
    --> ISpatialAnalysisToolGridCoordinateDefinition<ISpatialAnalysisToolGridCoordinateDefinition>
    --> ISpatialAnalysisToolGridValuesCustom<ISpatialAnalysisToolGridValuesCustom>
    --> ISpatialAnalysisToolGridValuesFixedNumberOfSteps<ISpatialAnalysisToolGridValuesFixedNumberOfSteps>
    --> ISpatialAnalysisToolGridValuesFixedStep<ISpatialAnalysisToolGridValuesFixedStep>
    --> ISpatialAnalysisToolGridValuesMethod<ISpatialAnalysisToolGridValuesMethod>
    --> ITimeToolLightTimeDelay<ITimeToolLightTimeDelay>
    --> ISpatialAnalysisToolVolume<ISpatialAnalysisToolVolume>
    --> ISpatialAnalysisToolVolumeCalc<ISpatialAnalysisToolVolumeCalc>
    --> ISpatialAnalysisToolVolumeCalcAltitude<ISpatialAnalysisToolVolumeCalcAltitude>
    --> ISpatialAnalysisToolVolumeCalcAngleOffVector<ISpatialAnalysisToolVolumeCalcAngleOffVector>
    --> ISpatialAnalysisToolVolumeCalcConditionSatMetric<ISpatialAnalysisToolVolumeCalcConditionSatMetric>
    --> ISpatialAnalysisToolVolumeCalcDelayRange<ISpatialAnalysisToolVolumeCalcDelayRange>
    --> ISpatialAnalysisToolVolumeCalcFile<ISpatialAnalysisToolVolumeCalcFile>
    --> ISpatialAnalysisToolVolumeCalcFromScalar<ISpatialAnalysisToolVolumeCalcFromScalar>
    --> ISpatialAnalysisToolVolumeCalcRange<ISpatialAnalysisToolVolumeCalcRange>
    --> ISpatialAnalysisToolVolumeCalcSolarIntensity<ISpatialAnalysisToolVolumeCalcSolarIntensity>
    --> ISpatialAnalysisToolVolumeCombined<ISpatialAnalysisToolVolumeCombined>
    --> ISpatialAnalysisToolVolumeFromCalc<ISpatialAnalysisToolVolumeFromCalc>
    --> ISpatialAnalysisToolVolumeFromCondition<ISpatialAnalysisToolVolumeFromCondition>
    --> ISpatialAnalysisToolVolumeFromGrid<ISpatialAnalysisToolVolumeFromGrid>
    --> ISpatialAnalysisToolVolumeFromTimeSatisfaction<ISpatialAnalysisToolVolumeFromTimeSatisfaction>
    --> ISpatialAnalysisToolVolumeGrid<ISpatialAnalysisToolVolumeGrid>
    --> ISpatialAnalysisToolVolumeGridBearingAlt<ISpatialAnalysisToolVolumeGridBearingAlt>
    --> ISpatialAnalysisToolVolumeGridCartesian<ISpatialAnalysisToolVolumeGridCartesian>
    --> ISpatialAnalysisToolVolumeGridConstrained<ISpatialAnalysisToolVolumeGridConstrained>
    --> ISpatialAnalysisToolVolumeGridCylindrical<ISpatialAnalysisToolVolumeGridCylindrical>
    --> ISpatialAnalysisToolVolumeGridLatLonAlt<ISpatialAnalysisToolVolumeGridLatLonAlt>
    --> ISpatialAnalysisToolVolumeGridResult<ISpatialAnalysisToolVolumeGridResult>
    --> ISpatialAnalysisToolVolumeGridSpherical<ISpatialAnalysisToolVolumeGridSpherical>
    --> ISpatialAnalysisToolVolumeInview<ISpatialAnalysisToolVolumeInview>
    --> ISpatialAnalysisToolVolumeLighting<ISpatialAnalysisToolVolumeLighting>
    --> ISpatialAnalysisToolVolumeOverTime<ISpatialAnalysisToolVolumeOverTime>
    --> ITimeToolTimeProperties<ITimeToolTimeProperties>
    --> IAnalysisWorkbenchTypeInfo<IAnalysisWorkbenchTypeInfo>
    --> IAnalysisWorkbenchRefTo<IAnalysisWorkbenchRefTo>
    --> IAnalysisWorkbenchTemplate<IAnalysisWorkbenchTemplate>
    --> IAnalysisWorkbenchInstance<IAnalysisWorkbenchInstance>
    --> IVectorGeometryToolPointRefTo<IVectorGeometryToolPointRefTo>
    --> IVectorGeometryToolVectorRefTo<IVectorGeometryToolVectorRefTo>
    --> IVectorGeometryToolAxesRefTo<IVectorGeometryToolAxesRefTo>
    --> IVectorGeometryToolAngleRefTo<IVectorGeometryToolAngleRefTo>
    --> IVectorGeometryToolSystemRefTo<IVectorGeometryToolSystemRefTo>
    --> IVectorGeometryToolPlaneRefTo<IVectorGeometryToolPlaneRefTo>
    --> IVectorGeometryToolAxesLabels<IVectorGeometryToolAxesLabels>
    --> IVectorGeometryToolPlaneLabels<IVectorGeometryToolPlaneLabels>
    --> IVectorGeometryToolAxesAlignedAndConstrained<IVectorGeometryToolAxesAlignedAndConstrained>
    --> IVectorGeometryToolAxesAngularOffset<IVectorGeometryToolAxesAngularOffset>
    --> IVectorGeometryToolAxesFixedAtEpoch<IVectorGeometryToolAxesFixedAtEpoch>
    --> IVectorGeometryToolAxesBPlane<IVectorGeometryToolAxesBPlane>
    --> IVectorGeometryToolAxesCustomScript<IVectorGeometryToolAxesCustomScript>
    --> IVectorGeometryToolAxesAttitudeFile<IVectorGeometryToolAxesAttitudeFile>
    --> IVectorGeometryToolAxesFixed<IVectorGeometryToolAxesFixed>
    --> IVectorGeometryToolAxesModelAttach<IVectorGeometryToolAxesModelAttach>
    --> IVectorGeometryToolAxesSpinning<IVectorGeometryToolAxesSpinning>
    --> IVectorGeometryToolAxesOnSurface<IVectorGeometryToolAxesOnSurface>
    --> IVectorGeometryToolAxesTrajectory<IVectorGeometryToolAxesTrajectory>
    --> IVectorGeometryToolAxesLagrangeLibration<IVectorGeometryToolAxesLagrangeLibration>
    --> IVectorGeometryToolAxesCommonTasks<IVectorGeometryToolAxesCommonTasks>
    --> IVectorGeometryToolAxesAtTimeInstant<IVectorGeometryToolAxesAtTimeInstant>
    --> IVectorGeometryToolAxesPlugin<IVectorGeometryToolAxesPlugin>
    --> IVectorGeometryToolAngleBetweenVectors<IVectorGeometryToolAngleBetweenVectors>
    --> IVectorGeometryToolAngleBetweenPlanes<IVectorGeometryToolAngleBetweenPlanes>
    --> IVectorGeometryToolAngleDihedral<IVectorGeometryToolAngleDihedral>
    --> IVectorGeometryToolAngleRotation<IVectorGeometryToolAngleRotation>
    --> IVectorGeometryToolAngleToPlane<IVectorGeometryToolAngleToPlane>
    --> IVectorGeometryToolPlaneNormal<IVectorGeometryToolPlaneNormal>
    --> IVectorGeometryToolPlaneQuadrant<IVectorGeometryToolPlaneQuadrant>
    --> IVectorGeometryToolPlaneTrajectory<IVectorGeometryToolPlaneTrajectory>
    --> IVectorGeometryToolPlaneTriad<IVectorGeometryToolPlaneTriad>
    --> IVectorGeometryToolPlaneTwoVector<IVectorGeometryToolPlaneTwoVector>
    --> IVectorGeometryToolPointBPlane<IVectorGeometryToolPointBPlane>
    --> IVectorGeometryToolPointFile<IVectorGeometryToolPointFile>
    --> IVectorGeometryToolPointFixedInSystem<IVectorGeometryToolPointFixedInSystem>
    --> IVectorGeometryToolPointGrazing<IVectorGeometryToolPointGrazing>
    --> IVectorGeometryToolPointGlint<IVectorGeometryToolPointGlint>
    --> IVectorGeometryToolPointCovarianceGrazing<IVectorGeometryToolPointCovarianceGrazing>
    --> IVectorGeometryToolPointPlaneIntersection<IVectorGeometryToolPointPlaneIntersection>
    --> IVectorGeometryToolPointOnSurface<IVectorGeometryToolPointOnSurface>
    --> IVectorGeometryToolPointModelAttach<IVectorGeometryToolPointModelAttach>
    --> IVectorGeometryToolPointSatelliteCollectionEntry<IVectorGeometryToolPointSatelliteCollectionEntry>
    --> IVectorGeometryToolPointPlaneProjection<IVectorGeometryToolPointPlaneProjection>
    --> IVectorGeometryToolPointLagrangeLibration<IVectorGeometryToolPointLagrangeLibration>
    --> IVectorGeometryToolPointCommonTasks<IVectorGeometryToolPointCommonTasks>
    --> IVectorGeometryToolPointCentBodyIntersect<IVectorGeometryToolPointCentBodyIntersect>
    --> IVectorGeometryToolPointAtTimeInstant<IVectorGeometryToolPointAtTimeInstant>
    --> IVectorGeometryToolPointPlugin<IVectorGeometryToolPointPlugin>
    --> IVectorGeometryToolPointCBFixedOffset<IVectorGeometryToolPointCBFixedOffset>
    --> IVectorGeometryToolSystemAssembled<IVectorGeometryToolSystemAssembled>
    --> IVectorGeometryToolSystemOnSurface<IVectorGeometryToolSystemOnSurface>
    --> IAnalysisWorkbenchLLAPosition<IAnalysisWorkbenchLLAPosition>
    --> IVectorGeometryToolSystemCommonTasks<IVectorGeometryToolSystemCommonTasks>
    --> IVectorGeometryToolVectorAngleRate<IVectorGeometryToolVectorAngleRate>
    --> IVectorGeometryToolVectorApoapsis<IVectorGeometryToolVectorApoapsis>
    --> IVectorGeometryToolVectorFixedAtEpoch<IVectorGeometryToolVectorFixedAtEpoch>
    --> IVectorGeometryToolVectorAngularVelocity<IVectorGeometryToolVectorAngularVelocity>
    --> IVectorGeometryToolVectorConing<IVectorGeometryToolVectorConing>
    --> IVectorGeometryToolVectorCross<IVectorGeometryToolVectorCross>
    --> IVectorGeometryToolVectorCustomScript<IVectorGeometryToolVectorCustomScript>
    --> IVectorGeometryToolVectorDerivative<IVectorGeometryToolVectorDerivative>
    --> IVectorGeometryToolVectorDisplacement<IVectorGeometryToolVectorDisplacement>
    --> IVectorGeometryToolVectorTwoPlanesIntersection<IVectorGeometryToolVectorTwoPlanesIntersection>
    --> IVectorGeometryToolVectorModelAttach<IVectorGeometryToolVectorModelAttach>
    --> IVectorGeometryToolVectorProjection<IVectorGeometryToolVectorProjection>
    --> IVectorGeometryToolVectorScaled<IVectorGeometryToolVectorScaled>
    --> IVectorGeometryToolVectorEccentricity<IVectorGeometryToolVectorEccentricity>
    --> IVectorGeometryToolVectorFixedInAxes<IVectorGeometryToolVectorFixedInAxes>
    --> IVectorGeometryToolVectorLineOfNodes<IVectorGeometryToolVectorLineOfNodes>
    --> IVectorGeometryToolVectorOrbitAngularMomentum<IVectorGeometryToolVectorOrbitAngularMomentum>
    --> IVectorGeometryToolVectorOrbitNormal<IVectorGeometryToolVectorOrbitNormal>
    --> IVectorGeometryToolVectorPeriapsis<IVectorGeometryToolVectorPeriapsis>
    --> IVectorGeometryToolVectorReflection<IVectorGeometryToolVectorReflection>
    --> IVectorGeometryToolVectorRotationVector<IVectorGeometryToolVectorRotationVector>
    --> IVectorGeometryToolVectorDirectionToStar<IVectorGeometryToolVectorDirectionToStar>
    --> IVectorGeometryToolVectorFixedAtTimeInstant<IVectorGeometryToolVectorFixedAtTimeInstant>
    --> IVectorGeometryToolVectorLinearCombination<IVectorGeometryToolVectorLinearCombination>
    --> IVectorGeometryToolVectorProjectAlongVector<IVectorGeometryToolVectorProjectAlongVector>
    --> IVectorGeometryToolVectorScalarLinearCombination<IVectorGeometryToolVectorScalarLinearCombination>
    --> IVectorGeometryToolVectorScalarScaled<IVectorGeometryToolVectorScalarScaled>
    --> IVectorGeometryToolVectorVelocityAcceleration<IVectorGeometryToolVectorVelocityAcceleration>
    --> IVectorGeometryToolVectorPlugin<IVectorGeometryToolVectorPlugin>
    --> IVectorGeometryToolVectorDispSurface<IVectorGeometryToolVectorDispSurface>
    --> IVectorGeometryToolVectorFactory<IVectorGeometryToolVectorFactory>
    --> IVectorGeometryToolAxesFactory<IVectorGeometryToolAxesFactory>
    --> IVectorGeometryToolSystemFactory<IVectorGeometryToolSystemFactory>
    --> IVectorGeometryToolPointFactory<IVectorGeometryToolPointFactory>
    --> IVectorGeometryToolPlaneFactory<IVectorGeometryToolPlaneFactory>
    --> IVectorGeometryToolAngleFactory<IVectorGeometryToolAngleFactory>
    --> IVectorGeometryToolVectorGroup<IVectorGeometryToolVectorGroup>
    --> IVectorGeometryToolPointGroup<IVectorGeometryToolPointGroup>
    --> IVectorGeometryToolAngleGroup<IVectorGeometryToolAngleGroup>
    --> IVectorGeometryToolAxesGroup<IVectorGeometryToolAxesGroup>
    --> IVectorGeometryToolPlaneGroup<IVectorGeometryToolPlaneGroup>
    --> IVectorGeometryToolSystemGroup<IVectorGeometryToolSystemGroup>
    --> IAnalysisWorkbenchProvider<IAnalysisWorkbenchProvider>
    --> IAnalysisWorkbenchRoot<IAnalysisWorkbenchRoot>
    --> IVectorGeometryToolWellKnownEarthSystems<IVectorGeometryToolWellKnownEarthSystems>
    --> IVectorGeometryToolWellKnownEarthAxes<IVectorGeometryToolWellKnownEarthAxes>
    --> IVectorGeometryToolWellKnownSunSystems<IVectorGeometryToolWellKnownSunSystems>
    --> IVectorGeometryToolWellKnownSunAxes<IVectorGeometryToolWellKnownSunAxes>
    --> IVectorGeometryToolWellKnownSystems<IVectorGeometryToolWellKnownSystems>
    --> IVectorGeometryToolWellKnownAxes<IVectorGeometryToolWellKnownAxes>
    --> IVectorGeometryToolAngleFindAngleResult<IVectorGeometryToolAngleFindAngleResult>
    --> IVectorGeometryToolAngleFindAngleWithRateResult<IVectorGeometryToolAngleFindAngleWithRateResult>
    --> IVectorGeometryToolAngleFindWithRateResult<IVectorGeometryToolAngleFindWithRateResult>
    --> IVectorGeometryToolAngleFindResult<IVectorGeometryToolAngleFindResult>
    --> IVectorGeometryToolAxesTransformResult<IVectorGeometryToolAxesTransformResult>
    --> IVectorGeometryToolAxesTransformWithRateResult<IVectorGeometryToolAxesTransformWithRateResult>
    --> IVectorGeometryToolPlaneFindInAxesResult<IVectorGeometryToolPlaneFindInAxesResult>
    --> IVectorGeometryToolPlaneFindInAxesWithRateResult<IVectorGeometryToolPlaneFindInAxesWithRateResult>
    --> IVectorGeometryToolPlaneFindInSystemResult<IVectorGeometryToolPlaneFindInSystemResult>
    --> IVectorGeometryToolPlaneFindInSystemWithRateResult<IVectorGeometryToolPlaneFindInSystemWithRateResult>
    --> IVectorGeometryToolAxesFindInAxesResult<IVectorGeometryToolAxesFindInAxesResult>
    --> IVectorGeometryToolAxesFindInAxesWithRateResult<IVectorGeometryToolAxesFindInAxesWithRateResult>
    --> IVectorGeometryToolPointLocateInSystemResult<IVectorGeometryToolPointLocateInSystemResult>
    --> IVectorGeometryToolPointLocateInSystemWithRateResult<IVectorGeometryToolPointLocateInSystemWithRateResult>
    --> IVectorGeometryToolSystemTransformResult<IVectorGeometryToolSystemTransformResult>
    --> IVectorGeometryToolSystemTransformWithRateResult<IVectorGeometryToolSystemTransformWithRateResult>
    --> IVectorGeometryToolSystemFindInSystemResult<IVectorGeometryToolSystemFindInSystemResult>
    --> IVectorGeometryToolVectorFindInAxesResult<IVectorGeometryToolVectorFindInAxesResult>
    --> IVectorGeometryToolVectorFindInAxesWithRateResult<IVectorGeometryToolVectorFindInAxesWithRateResult>
    --> IAnalysisWorkbenchMethodCallResult<IAnalysisWorkbenchMethodCallResult>
    --> IAnalysisWorkbenchCentralBody<IAnalysisWorkbenchCentralBody>
    --> IAnalysisWorkbenchCentralBodyRefTo<IAnalysisWorkbenchCentralBodyRefTo>
    --> IAnalysisWorkbenchCentralBodyCollection<IAnalysisWorkbenchCentralBodyCollection>
    --> IAnalysisWorkbenchCollection<IAnalysisWorkbenchCollection>
    --> ITimeToolPointSamplingResult<ITimeToolPointSamplingResult>
    --> ITimeToolPointSamplingInterval<ITimeToolPointSamplingInterval>
    --> ITimeToolPointSamplingIntervalCollection<ITimeToolPointSamplingIntervalCollection>
    --> ITimeToolAxesSamplingResult<ITimeToolAxesSamplingResult>
    --> ITimeToolAxesSamplingInterval<ITimeToolAxesSamplingInterval>
    --> ITimeToolAxesSamplingIntervalCollection<ITimeToolAxesSamplingIntervalCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> CalculationToolEvaluateResult<>
    --> CalculationToolEvaluateWithRateResult<>
    --> TimeToolEventIntervalResult<>
    --> TimeToolEventFindOccurrenceResult<>
    --> TimeToolFindTimesResult<>
    --> TimeToolIntervalsVectorResult<>
    --> TimeToolEventIntervalCollectionOccurredResult<>
    --> TimeToolIntervalListResult<>
    --> TimeToolIntervalVectorCollection<>
    --> TimeToolEventGroup<>
    --> TimeToolEventIntervalGroup<>
    --> TimeToolEventIntervalListGroup<>
    --> TimeToolEventArrayGroup<>
    --> CalculationToolScalarGroup<>
    --> TimeToolEventIntervalCollectionGroup<>
    --> CalculationToolParameterSetGroup<>
    --> CalculationToolConditionGroup<>
    --> CalculationToolConditionSetGroup<>
    --> CalculationToolConditionSetEvaluateResult<>
    --> CalculationToolConditionSetEvaluateWithRateResult<>
    --> SpatialAnalysisToolVolumeGridGroup<>
    --> SpatialAnalysisToolVolumeGroup<>
    --> SpatialAnalysisToolVolumeCalcGroup<>
    --> CalculationToolScalar<>
    --> CalculationToolScalarAngle<>
    --> CalculationToolScalarAverage<>
    --> CalculationToolScalarConstant<>
    --> CalculationToolScalarCustom<>
    --> CalculationToolScalarCustomInline<>
    --> CalculationToolScalarDataElement<>
    --> CalculationToolScalarDerivative<>
    --> CalculationToolScalarDotProduct<>
    --> CalculationToolScalarElapsedTime<>
    --> CalculationToolScalarFactory<>
    --> CalculationToolScalarFile<>
    --> CalculationToolScalarFixedAtTimeInstant<>
    --> CalculationToolScalarFunction<>
    --> CalculationToolScalarFunction2Var<>
    --> CalculationToolScalarIntegral<>
    --> CalculationToolScalarPlugin<>
    --> CalculationToolScalarPointInVolumeCalc<>
    --> CalculationToolScalarStandardDeviation<>
    --> CalculationToolScalarSurfaceDistanceBetweenPoints<>
    --> CalculationToolScalarVectorComponent<>
    --> CalculationToolScalarVectorMagnitude<>
    --> CalculationToolCondition<>
    --> CalculationToolConditionCombined<>
    --> CalculationToolConditionFactory<>
    --> CalculationToolConditionPointInVolume<>
    --> CalculationToolConditionScalarBounds<>
    --> CalculationToolConditionSet<>
    --> CalculationToolConditionSetFactory<>
    --> CalculationToolConditionSetScalarThresholds<>
    --> AnalysisWorkbenchConverge<>
    --> CalculationToolConvergeBasic<>
    --> AnalysisWorkbenchDerivative<>
    --> CalculationToolDerivativeBasic<>
    --> TimeToolEvent<>
    --> TimeToolEventArray<>
    --> TimeToolEventArrayConditionCrossings<>
    --> TimeToolEventArrayExtrema<>
    --> TimeToolEventArrayFactory<>
    --> TimeToolEventArrayFiltered<>
    --> TimeToolEventArrayFixedStep<>
    --> TimeToolEventArrayFixedTimes<>
    --> TimeToolEventArrayMerged<>
    --> TimeToolEventArraySignaled<>
    --> TimeToolEventArrayStartStopTimes<>
    --> TimeToolEventEpoch<>
    --> TimeToolEventExtremum<>
    --> TimeToolEventFactory<>
    --> TimeToolEventInterval<>
    --> TimeToolEventIntervalBetweenTimeInstants<>
    --> TimeToolEventIntervalCollection<>
    --> TimeToolEventIntervalCollectionCondition<>
    --> TimeToolEventIntervalCollectionFactory<>
    --> TimeToolEventIntervalCollectionLighting<>
    --> TimeToolEventIntervalCollectionSignaled<>
    --> TimeToolEventIntervalFactory<>
    --> TimeToolEventIntervalFixed<>
    --> TimeToolEventIntervalFixedDuration<>
    --> TimeToolEventIntervalFromIntervalList<>
    --> TimeToolEventIntervalList<>
    --> TimeToolEventIntervalListCondition<>
    --> TimeToolEventIntervalListFactory<>
    --> TimeToolEventIntervalListFile<>
    --> TimeToolEventIntervalListFiltered<>
    --> TimeToolEventIntervalListFixed<>
    --> TimeToolEventIntervalListMerged<>
    --> TimeToolEventIntervalListScaled<>
    --> TimeToolEventIntervalListSignaled<>
    --> TimeToolEventIntervalListTimeOffset<>
    --> TimeToolEventIntervalScaled<>
    --> TimeToolEventIntervalSignaled<>
    --> TimeToolEventIntervalSmartInterval<>
    --> TimeToolEventIntervalTimeOffset<>
    --> TimeToolEventSignaled<>
    --> TimeToolEventSmartEpoch<>
    --> TimeToolEventStartStopTime<>
    --> TimeToolEventTimeOffset<>
    --> TimeToolFirstIntervalsFilter<>
    --> TimeToolGapsFilter<>
    --> AnalysisWorkbenchIntegral<>
    --> CalculationToolIntegralBasic<>
    --> AnalysisWorkbenchInterp<>
    --> CalculationToolInterpBasic<>
    --> TimeToolIntervalsFilter<>
    --> TimeToolLastIntervalsFilter<>
    --> CalculationToolParameterSet<>
    --> CalculationToolParameterSetAttitude<>
    --> CalculationToolParameterSetFactory<>
    --> CalculationToolParameterSetGroundTrajectory<>
    --> CalculationToolParameterSetOrbit<>
    --> CalculationToolParameterSetTrajectory<>
    --> CalculationToolParameterSetVector<>
    --> TimeToolPruneFilter<>
    --> TimeToolPruneFilterFactory<>
    --> TimeToolRelativeSatisfactionConditionFilter<>
    --> AnalysisWorkbenchSampling<>
    --> CalculationToolSamplingBasic<>
    --> CalculationToolSamplingCurvatureTolerance<>
    --> CalculationToolSamplingFixedStep<>
    --> CalculationToolSamplingMethod<>
    --> CalculationToolSamplingMethodFactory<>
    --> CalculationToolSamplingRelativeTolerance<>
    --> TimeToolSatisfactionConditionFilter<>
    --> AnalysisWorkbenchSignalDelay<>
    --> TimeToolSignalDelayBasic<>
    --> SpatialAnalysisToolVolumeCalcFactory<>
    --> SpatialAnalysisToolVolumeFactory<>
    --> SpatialAnalysisToolVolumeGridFactory<>
    --> SpatialAnalysisToolGridCoordinateDefinition<>
    --> SpatialAnalysisToolGridValuesCustom<>
    --> SpatialAnalysisToolGridValuesFixedNumberOfSteps<>
    --> SpatialAnalysisToolGridValuesFixedStep<>
    --> SpatialAnalysisToolGridValuesMethod<>
    --> TimeToolLightTimeDelay<>
    --> SpatialAnalysisToolVolume<>
    --> SpatialAnalysisToolVolumeCalc<>
    --> SpatialAnalysisToolVolumeCalcAltitude<>
    --> SpatialAnalysisToolVolumeCalcAngleOffVector<>
    --> SpatialAnalysisToolVolumeCalcConditionSatMetric<>
    --> SpatialAnalysisToolVolumeCalcDelayRange<>
    --> SpatialAnalysisToolVolumeCalcFile<>
    --> SpatialAnalysisToolVolumeCalcFromScalar<>
    --> SpatialAnalysisToolVolumeCalcRange<>
    --> SpatialAnalysisToolVolumeCalcSolarIntensity<>
    --> SpatialAnalysisToolVolumeCombined<>
    --> SpatialAnalysisToolVolumeFromCalc<>
    --> SpatialAnalysisToolVolumeFromCondition<>
    --> SpatialAnalysisToolVolumeFromGrid<>
    --> SpatialAnalysisToolVolumeFromTimeSatisfaction<>
    --> SpatialAnalysisToolVolumeGrid<>
    --> SpatialAnalysisToolVolumeGridBearingAlt<>
    --> SpatialAnalysisToolVolumeGridCartesian<>
    --> SpatialAnalysisToolVolumeGridConstrained<>
    --> SpatialAnalysisToolVolumeGridCylindrical<>
    --> SpatialAnalysisToolVolumeGridLatLonAlt<>
    --> SpatialAnalysisToolVolumeGridResult<>
    --> SpatialAnalysisToolVolumeGridSpherical<>
    --> SpatialAnalysisToolVolumeInview<>
    --> SpatialAnalysisToolVolumeLighting<>
    --> SpatialAnalysisToolVolumeOverTime<>
    --> AnalysisWorkbenchGeneric<>
    --> AnalysisWorkbenchTypeInfo<>
    --> AnalysisWorkbenchInstance<>
    --> AnalysisWorkbenchTemplate<>
    --> VectorGeometryToolPointRefTo<>
    --> VectorGeometryToolVectorRefTo<>
    --> VectorGeometryToolAxesRefTo<>
    --> VectorGeometryToolAngleRefTo<>
    --> VectorGeometryToolSystemRefTo<>
    --> VectorGeometryToolPlaneRefTo<>
    --> VectorGeometryToolVector<>
    --> VectorGeometryToolAxesLabels<>
    --> VectorGeometryToolAxes<>
    --> VectorGeometryToolPoint<>
    --> VectorGeometryToolSystem<>
    --> VectorGeometryToolAngle<>
    --> VectorGeometryToolPlaneLabels<>
    --> VectorGeometryToolPlane<>
    --> VectorGeometryToolAxesAlignedAndConstrained<>
    --> VectorGeometryToolAxesAngularOffset<>
    --> VectorGeometryToolAxesFixedAtEpoch<>
    --> VectorGeometryToolAxesBPlane<>
    --> VectorGeometryToolAxesCustomScript<>
    --> VectorGeometryToolAxesAttitudeFile<>
    --> VectorGeometryToolAxesFixed<>
    --> VectorGeometryToolAxesModelAttach<>
    --> VectorGeometryToolAxesSpinning<>
    --> VectorGeometryToolAxesOnSurface<>
    --> VectorGeometryToolAxesTrajectory<>
    --> VectorGeometryToolAxesLagrangeLibration<>
    --> VectorGeometryToolAxesCommonTasks<>
    --> VectorGeometryToolAxesAtTimeInstant<>
    --> VectorGeometryToolAxesPlugin<>
    --> VectorGeometryToolAngleBetweenVectors<>
    --> VectorGeometryToolAngleBetweenPlanes<>
    --> VectorGeometryToolAngleDihedral<>
    --> VectorGeometryToolAngleRotation<>
    --> VectorGeometryToolAngleToPlane<>
    --> VectorGeometryToolPlaneNormal<>
    --> VectorGeometryToolPlaneQuadrant<>
    --> VectorGeometryToolPlaneTrajectory<>
    --> VectorGeometryToolPlaneTriad<>
    --> VectorGeometryToolPlaneTwoVector<>
    --> VectorGeometryToolPointBPlane<>
    --> VectorGeometryToolPointFile<>
    --> VectorGeometryToolPointFixedInSystem<>
    --> VectorGeometryToolPointGrazing<>
    --> VectorGeometryToolPointGlint<>
    --> VectorGeometryToolPointCovarianceGrazing<>
    --> VectorGeometryToolPointPlaneIntersection<>
    --> VectorGeometryToolPointOnSurface<>
    --> VectorGeometryToolPointModelAttach<>
    --> VectorGeometryToolPointSatelliteCollectionEntry<>
    --> VectorGeometryToolPointPlaneProjection<>
    --> VectorGeometryToolPointLagrangeLibration<>
    --> VectorGeometryToolPointCommonTasks<>
    --> VectorGeometryToolPointCentBodyIntersect<>
    --> VectorGeometryToolPointAtTimeInstant<>
    --> VectorGeometryToolPointPlugin<>
    --> VectorGeometryToolPointCBFixedOffset<>
    --> VectorGeometryToolSystemAssembled<>
    --> VectorGeometryToolSystemOnSurface<>
    --> AnalysisWorkbenchLLAPosition<>
    --> VectorGeometryToolSystemCommonTasks<>
    --> VectorGeometryToolVectorAngleRate<>
    --> VectorGeometryToolVectorApoapsis<>
    --> VectorGeometryToolVectorFixedAtEpoch<>
    --> VectorGeometryToolVectorAngularVelocity<>
    --> VectorGeometryToolVectorConing<>
    --> VectorGeometryToolVectorCross<>
    --> VectorGeometryToolVectorCustomScript<>
    --> VectorGeometryToolVectorDerivative<>
    --> VectorGeometryToolVectorDisplacement<>
    --> VectorGeometryToolVectorTwoPlanesIntersection<>
    --> VectorGeometryToolVectorModelAttach<>
    --> VectorGeometryToolVectorProjection<>
    --> VectorGeometryToolVectorScaled<>
    --> VectorGeometryToolVectorEccentricity<>
    --> VectorGeometryToolVectorFixedInAxes<>
    --> VectorGeometryToolVectorLineOfNodes<>
    --> VectorGeometryToolVectorOrbitAngularMomentum<>
    --> VectorGeometryToolVectorOrbitNormal<>
    --> VectorGeometryToolVectorPeriapsis<>
    --> VectorGeometryToolVectorReflection<>
    --> VectorGeometryToolVectorRotationVector<>
    --> VectorGeometryToolVectorDirectionToStar<>
    --> VectorGeometryToolVectorFixedAtTimeInstant<>
    --> VectorGeometryToolVectorLinearCombination<>
    --> VectorGeometryToolVectorProjectAlongVector<>
    --> VectorGeometryToolVectorScalarLinearCombination<>
    --> VectorGeometryToolVectorScalarScaled<>
    --> VectorGeometryToolVectorVelocityAcceleration<>
    --> VectorGeometryToolVectorPlugin<>
    --> VectorGeometryToolVectorDispSurface<>
    --> VectorGeometryToolVectorFactory<>
    --> VectorGeometryToolAxesFactory<>
    --> VectorGeometryToolSystemFactory<>
    --> VectorGeometryToolPointFactory<>
    --> VectorGeometryToolPlaneFactory<>
    --> VectorGeometryToolAngleFactory<>
    --> VectorGeometryToolVectorGroup<>
    --> VectorGeometryToolPointGroup<>
    --> VectorGeometryToolAngleGroup<>
    --> VectorGeometryToolAxesGroup<>
    --> VectorGeometryToolPlaneGroup<>
    --> VectorGeometryToolSystemGroup<>
    --> AnalysisWorkbenchProvider<>
    --> AnalysisWorkbenchRoot<>
    --> VectorGeometryToolWellKnownEarthSystems<>
    --> VectorGeometryToolWellKnownEarthAxes<>
    --> VectorGeometryToolWellKnownSunSystems<>
    --> VectorGeometryToolWellKnownSunAxes<>
    --> VectorGeometryToolWellKnownSystems<>
    --> VectorGeometryToolWellKnownAxes<>
    --> AnalysisWorkbenchMethodCallAngleFindResult<>
    --> AnalysisWorkbenchMethodCallAngleFindWithRateResult<>
    --> AnalysisWorkbenchMethodCallAxesTransformResult<>
    --> AnalysisWorkbenchMethodCallAxesTransformWithRateResult<>
    --> AnalysisWorkbenchMethodCallAxesFindInAxesResult<>
    --> AnalysisWorkbenchMethodCallAxesFindInAxesWithRateResult<>
    --> AnalysisWorkbenchMethodCallPlaneFindInAxesResult<>
    --> AnalysisWorkbenchMethodCallPlaneFindInAxesWithRateResult<>
    --> AnalysisWorkbenchMethodCallPlaneFindInSystemResult<>
    --> AnalysisWorkbenchMethodCallPlaneFindInSystemWithRateResult<>
    --> AnalysisWorkbenchMethodCallPointLocateInSystemResult<>
    --> AnalysisWorkbenchMethodCallPointLocateInSystemWithRateResult<>
    --> AnalysisWorkbenchMethodCallSystemTransformResult<>
    --> AnalysisWorkbenchMethodCallSystemTransformWithRateResult<>
    --> AnalysisWorkbenchMethodCallSystemFindInSystemResult<>
    --> AnalysisWorkbenchMethodCallVectorFindInAxesResult<>
    --> AnalysisWorkbenchMethodCallVectorFindInAxesWithRateResult<>
    --> AnalysisWorkbenchMethodCallAngleFindAngleWithRateResult<>
    --> AnalysisWorkbenchMethodCallAngleFindAngleResult<>
    --> TimeToolInterval<>
    --> TimeToolIntervalCollection<>
    --> AnalysisWorkbenchCentralBody<>
    --> AnalysisWorkbenchCentralBodyRefTo<>
    --> AnalysisWorkbenchCentralBodyCollection<>
    --> AnalysisWorkbenchCollection<>
    --> TimeToolPointSamplingResult<>
    --> TimeToolPointSamplingInterval<>
    --> TimeToolPointSamplingIntervalCollection<>
    --> TimeToolAxesSamplingResult<>
    --> TimeToolAxesSamplingInterval<>
    --> TimeToolAxesSamplingIntervalCollection<>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ CRDN_CALC_SCALAR_TYPE<CRDN_CALC_SCALAR_TYPE>
    ≔ CRDN_CONDITION_COMBINED_OPERATION_TYPE<CRDN_CONDITION_COMBINED_OPERATION_TYPE>
    ≔ CRDN_CONDITION_SET_TYPE<CRDN_CONDITION_SET_TYPE>
    ≔ CRDN_CONDITION_THRESHOLD_OPTION<CRDN_CONDITION_THRESHOLD_OPTION>
    ≔ CRDN_CONDITION_TYPE<CRDN_CONDITION_TYPE>
    ≔ CRDN_DIMENSION_INHERITANCE<CRDN_DIMENSION_INHERITANCE>
    ≔ CRDN_EVENT_ARRAY_FILTER_TYPE<CRDN_EVENT_ARRAY_FILTER_TYPE>
    ≔ CRDN_EVENT_ARRAY_TYPE<CRDN_EVENT_ARRAY_TYPE>
    ≔ CRDN_EVENT_INTERVAL_COLLECTION_TYPE<CRDN_EVENT_INTERVAL_COLLECTION_TYPE>
    ≔ CRDN_EVENT_INTERVAL_LIST_TYPE<CRDN_EVENT_INTERVAL_LIST_TYPE>
    ≔ CRDN_EVENT_INTERVAL_TYPE<CRDN_EVENT_INTERVAL_TYPE>
    ≔ CRDN_EVENT_LIST_MERGE_OPERATION<CRDN_EVENT_LIST_MERGE_OPERATION>
    ≔ CRDN_EVENT_TYPE<CRDN_EVENT_TYPE>
    ≔ CRDN_EXTREMUM_CONSTANTS<CRDN_EXTREMUM_CONSTANTS>
    ≔ CRDN_FILE_INTERPOLATOR_TYPE<CRDN_FILE_INTERPOLATOR_TYPE>
    ≔ CRDN_INTEGRAL_TYPE<CRDN_INTEGRAL_TYPE>
    ≔ CRDN_INTEGRATION_WINDOW_TYPE<CRDN_INTEGRATION_WINDOW_TYPE>
    ≔ CRDN_INTERPOLATOR_TYPE<CRDN_INTERPOLATOR_TYPE>
    ≔ CRDN_INTERVAL_DURATION_KIND<CRDN_INTERVAL_DURATION_KIND>
    ≔ CRDN_INTERVAL_SELECTION<CRDN_INTERVAL_SELECTION>
    ≔ CRDN_PARAMETER_SET_TYPE<CRDN_PARAMETER_SET_TYPE>
    ≔ CRDN_PRUNE_FILTER<CRDN_PRUNE_FILTER>
    ≔ CRDN_SAMPLED_REFERENCE_TIME<CRDN_SAMPLED_REFERENCE_TIME>
    ≔ CRDN_SAMPLING_METHOD<CRDN_SAMPLING_METHOD>
    ≔ CRDN_SATISFACTION_CROSSING<CRDN_SATISFACTION_CROSSING>
    ≔ CRDN_SAVE_DATA_OPTION<CRDN_SAVE_DATA_OPTION>
    ≔ CRDN_SIGNAL_PATH_REFERENCE_SYSTEM<CRDN_SIGNAL_PATH_REFERENCE_SYSTEM>
    ≔ CRDN_SMART_EPOCH_STATE<CRDN_SMART_EPOCH_STATE>
    ≔ CRDN_SMART_INTERVAL_STATE<CRDN_SMART_INTERVAL_STATE>
    ≔ CRDN_SPEED_OPTIONS<CRDN_SPEED_OPTIONS>
    ≔ CRDN_START_STOP_OPTION<CRDN_START_STOP_OPTION>
    ≔ CRDN_THRESH_CONVERGE_SENSE<CRDN_THRESH_CONVERGE_SENSE>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE<VECTOR_GEOMETRY_TOOL_VECTOR_COMPONENT_TYPE>
    ≔ CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE<CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE>
    ≔ CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE<CRDN_VOLUME_CALC_ANGLE_OFF_VECTOR_TYPE>
    ≔ CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE<CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE>
    ≔ CRDN_VOLUME_CALC_RANGE_SPEED_TYPE<CRDN_VOLUME_CALC_RANGE_SPEED_TYPE>
    ≔ CRDN_VOLUME_CALC_TYPE<CRDN_VOLUME_CALC_TYPE>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE<CRDN_VOLUME_CALC_VOLUME_SATISFACTION_ACCUMULATION_TYPE>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE<CRDN_VOLUME_CALC_VOLUME_SATISFACTION_DURATION_TYPE>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE<CRDN_VOLUME_CALC_VOLUME_SATISFACTION_FILTER_TYPE>
    ≔ CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE<CRDN_VOLUME_CALC_VOLUME_SATISFACTION_METRIC_TYPE>
    ≔ CRDN_VOLUME_GRID_TYPE<CRDN_VOLUME_GRID_TYPE>
    ≔ CRDN_VOLUME_RESULT_VECTOR_REQUEST<CRDN_VOLUME_RESULT_VECTOR_REQUEST>
    ≔ CRDN_VOLUME_TYPE<CRDN_VOLUME_TYPE>
    ≔ CRDN_VOLUME_ABERRATION_TYPE<CRDN_VOLUME_ABERRATION_TYPE>
    ≔ CRDN_VOLUME_CLOCK_HOST_TYPE<CRDN_VOLUME_CLOCK_HOST_TYPE>
    ≔ CRDN_VOLUME_COMBINED_OPERATION_TYPE<CRDN_VOLUME_COMBINED_OPERATION_TYPE>
    ≔ CRDN_VOLUME_FROM_GRID_EDGE_TYPE<CRDN_VOLUME_FROM_GRID_EDGE_TYPE>
    ≔ CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE<CRDN_VOLUME_LIGHTING_CONDITIONS_TYPE>
    ≔ CRDN_VOLUME_OVER_TIME_DURATION_TYPE<CRDN_VOLUME_OVER_TIME_DURATION_TYPE>
    ≔ CRDN_VOLUME_TIME_SENSE_TYPE<CRDN_VOLUME_TIME_SENSE_TYPE>
    ≔ CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE<CRDN_VOLUMETRIC_GRID_VALUES_METHOD_TYPE>
    ≔ CRDN_KIND<CRDN_KIND>
    ≔ VECTOR_GEOMETRY_TOOL_ANGLE_TYPE<VECTOR_GEOMETRY_TOOL_ANGLE_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_AXES_TYPE<VECTOR_GEOMETRY_TOOL_AXES_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_PLANE_TYPE<VECTOR_GEOMETRY_TOOL_PLANE_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_POINT_TYPE<VECTOR_GEOMETRY_TOOL_POINT_TYPE>
    ≔ CRDN_SYSTEM_TYPE<CRDN_SYSTEM_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_TYPE<VECTOR_GEOMETRY_TOOL_VECTOR_TYPE>
    ≔ CRDN_MEAN_ELEMENT_THEORY<CRDN_MEAN_ELEMENT_THEORY>
    ≔ CRDN_DIRECTION_TYPE<CRDN_DIRECTION_TYPE>
    ≔ CRDN_LAGRANGE_LIBRATION_POINT_TYPE<CRDN_LAGRANGE_LIBRATION_POINT_TYPE>
    ≔ CRDN_QUADRANT_TYPE<CRDN_QUADRANT_TYPE>
    ≔ CRDN_TRAJECTORY_AXES_TYPE<CRDN_TRAJECTORY_AXES_TYPE>
    ≔ CRDN_DISPLAY_AXIS_SELECTOR<CRDN_DISPLAY_AXIS_SELECTOR>
    ≔ CRDN_SIGNED_ANGLE_TYPE<CRDN_SIGNED_ANGLE_TYPE>
    ≔ VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE<VECTOR_GEOMETRY_TOOL_POINT_B_PLANE_TYPE>
    ≔ CRDN_REFERENCE_SHAPE_TYPE<CRDN_REFERENCE_SHAPE_TYPE>
    ≔ CRDN_SURFACE_TYPE<CRDN_SURFACE_TYPE>
    ≔ CRDN_SWEEP_MODE<CRDN_SWEEP_MODE>
    ≔ CRDN_SIGNAL_SENSE<CRDN_SIGNAL_SENSE>
    ≔ CRDN_INTERSECTION_SURFACE<CRDN_INTERSECTION_SURFACE>
    ≔ VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE<VECTOR_GEOMETRY_TOOL_VECTOR_SCALED_DIMENSION_INHERITANCE>

