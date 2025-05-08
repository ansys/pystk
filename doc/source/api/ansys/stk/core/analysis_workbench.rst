
The ``analysis_workbench`` module
=================================


.. py:module:: ansys.stk.core.analysis_workbench


Summary
-------

.. tab-set::

 
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`
              - A base interface implemented by all VGT components. The methods and properties of the interface provide type information about the VGT component.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentContext`
              - The interface represents a context associated with a VGT component. All VGT components are associated with a valid context. A context can represent a VGT instance or a VGT template.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentReference`
              - A base interface for all VGT component references.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`
              - Define methods to compute time properties such as availability and special times.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchConvergence`
              - Represents a base class for convergence definitions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchInterpolator`
              - Represents a base class for interpolation definitions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`
              - Instances of the interface are used to return the result of a computation.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchSampling`
              - Base sampling interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolParameterSet`
              - Parameter set contains various sets of scalar computations.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolSamplingMethod`
              - A sampling method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolGridValuesMethod`
              - A grid values method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolSpatialCalculation`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolume`
              - A volume interface. The methods and properties of the interface provide Volume functions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolInstant`
              - Define an event (time instant).

            * - :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolPruneFilter`
              - A filter used with event interval list pruned class to prune interval lists...

            * - :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeInterval`
              - A single time interval.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection`
              - A collection of related interval lists.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList`
              - An ordered list of time intervals.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle`
              - The interface defines methods and properties common to all angles.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`
              - The interface defines methods and properties common to all axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane`
              - The interface defines methods and properties common to all VGT planes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`
              - The interface defines methods and properties common to all points.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolSystem`
              - The interface contains methods and properties shared by all VGT systems.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`
              - The interface defines methods and properties common to all vectors.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleResult`
              - Contains the results returned with IVectorGeometryToolAngle.FindAngle method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindAngleWithRateResult`
              - Contains the results returned with IVectorGeometryToolAngle.FindAngleWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult`
              - Represents result returned with IVectorGeometryToolAngle.FindCoordinates method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindWithRateResult`
              - Contains the results returned with IVectorGeometryToolAngle.FindCoordinatesWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesResult`
              - Contains the results returned with IVectorGeometryToolAxes.FindInAxes method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesWithRateResult`
              - Contains the results returned with IVectorGeometryToolAxes.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesTransformResult`
              - Contains the results returned with IVectorGeometryToolAxes.TransformFrom method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesTransformWithRateResult`
              - Contains the results returned with IVectorGeometryToolAxes.TransformFromWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBody`
              - Represents an central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyCollection`
              - A collection of central body names.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchCentralBodyReference`
              - Represents a central body reference.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponent`
              - Generic VGT component.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection`
              - A collection of VGT objects.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentInstance`
              - Enable to obtain information about the parent object that owns the VGT component.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentProvider`
              - Allow accessing existing Vector Geometry Tool components.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentTemplate`
              - Enable to obtain information about the STK class that owns the VGT component.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentTypeInformation`
              - VGT component info.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchConvergence`
              - Represents a base class for convergence definitions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchDerivative`
              - Represents a base class for derivative definitions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchIntegral`
              - Represents a base class for integral definitions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchInterpolator`
              - Represents a base class for interpolation definitions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInAxes method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesWithRateResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInSystem method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemWithRateResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemResult`
              - Contains the results returned with IVectorGeometryToolPlane.FindInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemWithRateResult`
              - Contains the results returned with IVectorGeometryToolPoint.LocateInSystemWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPositionLLA`
              - A position represented by the Latitude, longtitude and Latitude.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot`
              - Represents a VGT root.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSampling`
              - Base sampling interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSignalDelay`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult`
              - Contains the results returned with IVectorGeometryToolSystem.FindInSystem method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformResult`
              - Contains the results returned with IVectorGeometryToolSystem.TransformFrom and IVectorGeometryToolSystem.TransformTo methods.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult`
              - Contains the results returned with IVectorGeometryToolSystem.TransformFromWithRate and IVectorGeometryToolSystem.TransformToWithRate methods.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesResult`
              - Contains the results returned with IVectorGeometryToolVector.FindInAxes method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesWithRateResult`
              - Contains the results returned with IVectorGeometryToolVector.FindInAxesWithRate method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolCondition`
              - Condition returns a non-dimensional metric that is positive if satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for accurate detection of condition crossings.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionCombined`
              - Define a condition which combines multiple conditions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionFactory`
              - The factory creates condition components.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionGroup`
              - Access or create VGT conditions associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionScalarBounds`
              - Defined by determining if input scalar is within specified bounds; returns +1 if satisfied, -1 if not satisfied and 0 if on boundary.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSet`
              - Condition set returns an array of non-dimensional metrics, one for each condition in the set; each metric is positive if corresponding condition is satisfied, negative if not satisfied and 0 if on boundary; this provides computational methods needed for...

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetEvaluateResult`
              - Represents the results returned by ConditionSet.Evaluate.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetEvaluateWithRateResult`
              - Represents the results returned by ConditionSet.EvaluateWithRate.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetFactory`
              - The factory creates condition set components.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetGroup`
              - Allow accessing and creating condition set components.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetScalarThresholds`
              - Condition set based on single scalar calculation compared to set of threshold values.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume`
              - Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic`
              - Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolDerivativeBasic`
              - Derivative definition determines how numerical differencing is used to compute derivatives.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolEvaluateResult`
              - Represents the results of evaluating a scalar component.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolEvaluateWithRateResult`
              - Represents the results of evaluating a scalar component.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolIntegralBasic`
              - Integral definition determines how scalar calculation is numerically integrated.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolInterpolatorBasic`
              - Interpolation definition determines how to obtain values in between tabulated samples. See STK help on interpolation for further details.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSet`
              - Parameter set contains various sets of scalar computations.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetAttitude`
              - Attitude parameter set contains various representations of attitude of one set of axes relative to another.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetFactory`
              - The factory is used to create instances of available parameter set types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetGroundTrajectory`
              - Ground trajectory parameter set contains various representations of trajectory of a point relative to central body reference shape.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetGroup`
              - Access or create VGT parameter sets associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetOrbit`
              - Orbit parameter set contains various trajectory representations of an orbiting point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetTrajectory`
              - Trajectory parameter set contains various representations of trajectory of a point relative to a reference coordinate system.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolParameterSetVector`
              - Vector parameter set contains various representations of a vector in a reference set of axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingBasic`
              - Sampling definition determines how scalar data should be sampled in order to adequately capture trends in that data.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance`
              - Curvature tolerance definition includes parameters that determine how scalar data should be sampled based on limits on slope changes between samples.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingFixedStep`
              - Fixed step definition includes parameters that determine how scalar data should be sampled based on fixed steps between samples.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingMethod`
              - A sampling method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingMethodFactory`
              - The factory creates sampling method components.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance`
              - Relative tolerance definition includes parameters that determine how scalar data should be sampled based on limits on difference between actual changes between samples and changes predicted by dead reckoning.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalar`
              - Any scalar calculation that is not constant by construction.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarAlongTrajectory`
              - Scalar value of spatial calculation evaluated along trajectory of point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarAngle`
              - Scalar equal to angular displacement obtained from any angle in VGT.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarAverage`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarConstant`
              - Constant scalar value of specified dimension.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCustom`
              - A calc scalar based on a scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarCustomInlineScript`
              - A calc scalar based on using an inline scripted algorithm in MATLAB, Perl, VBScript or JScript to define its value and rate.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDataElement`
              - Any time-dependent data element from STK data providers available for parent STK object.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDerivative`
              - Derivative of an input scalar calculation.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarDotProduct`
              - Dot product between two vectors.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarElapsedTime`
              - Time elapsed since the reference time instant. Negative if in the past.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFactory`
              - The factory creates scalar calculation components.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFile`
              - Tabulated scalar calculation data loaded from specified file - a file with .csc extension.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFixedAtTimeInstant`
              - Constant scalar created by evaluating the input scalar calculation at the specified reference time instant. Undefined if original scalar is not available at specified time or if reference time instant is undefined.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunction`
              - Defined by performing the specified function on the input scalar or time instant.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarFunctionOf2Variables`
              - Defined by performing a function(x,y) on two scalar arguments.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup`
              - Access or create VGT calculation scalars associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarIntegral`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarPlugin`
              - Use a scalar calculation plugin.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarStandardDeviation`
              - Integral of input scalar computed with respect to time using one of the specified numerical methods and using one of the specified accumulation types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints`
              - Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarVectorComponent`
              - The specified component of a vector when resolved in the specified axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationToolScalarVectorMagnitude`
              - Scalar equal to the magnitude of a specified vector.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude`
              - A volume grid bearing alt (Surface Bearing) interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude`
              - A volume calc altitude interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation`
              - A volume calc angle off vector interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationConditionSatisfactionMetric`
              - A volume calc condition satisfaction interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation`
              - A volume calc distance to location interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory`
              - The factory is used to create instances of volume calcs.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFile`
              - Volumetric data loaded from a specified file - A file with .h5 extension. See STK help.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFromCalculationScalar`
              - A volume calc scalar to location interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationGroup`
              - Access or create VGT volume calc associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationPropagationDelayToLocation`
              - A volume calc propagation delay to location interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationSolarIntensity`
              - A volume calc solar intensityn interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionAccessToLocation`
              - An Inview volume interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined`
              - A combined volume interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionConditionAtLocation`
              - A volume from conditioninterface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionFactory`
              - The factory is used to create instances of volumes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionGridBoundingVolume`
              - An over time volume interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionGroup`
              - Access or create spatial conditions associated with a volume grid.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionLighting`
              - A lighting volume interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime`
              - An over time volume interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionSpatialCalculationBounds`
              - An volume from calc volume interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionValidTimeAtLocation`
              - An volume from time satisfaction volume interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridCoordinateDefinition`
              - Define a set of coordinate values.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesCustom`
              - Fixed step grid values.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedNumberOfSteps`
              - Fixed step grid values.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesFixedStep`
              - Fixed step grid values.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolGridValuesMethod`
              - A grid values method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolSpatialCalculation`
              - A volume calc interface. The methods and properties of the interface provide Volumetric calc functions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolume`
              - A volume interface. The methods and properties of the interface provide Volume functions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGrid`
              - A volume grid interface. The methods and properties of the interface provide Volumetric Grid functions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian`
              - A volume grid Cartesian interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridConstrained`
              - A volume grid constrained interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical`
              - A volume grid cylindrical interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory`
              - The factory is used to create instances of volume grids.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridGroup`
              - Access or create VGT volume grids associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude`
              - A volume grid lat lon alt (Cartogrographic) interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridResult`
              - An interface that generates Volume Grid results.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical`
              - A volume grid spherical interface.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolAxesSamplingInterval`
              - The interface represents an interval with the time, orientation and velocity arrays.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolAxesSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, orientation and velocity arrays.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolAxesSamplingResult`
              - Contains tabulated orientations and angular velocities of axes created by Sample method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstant`
              - Define an event (time instant).

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantEpoch`
              - Event set at specified date/time.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantExtremum`
              - Determine time of global minimum or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory`
              - The factory creates events.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup`
              - Access or create VGT events associated with an object.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantOccurrenceResult`
              - Contains the results returned with ITimeToolInstant.FindOccurrence method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantSignaled`
              - Event recorded on specified clock via signal transmission from original time instant recorded on different clock.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch`
              - A smart epoch.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantStartStopTime`
              - Event is either start or stop time selected from a reference interval.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInstantTimeOffset`
              - Event at fixed offset from specified reference event.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolInterval`
              - Represents an interval.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolIntervalCollection`
              - Represents a collection of intervals.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolIntervalListResult`
              - Contains the results returned with ITimeToolTimeIntervalList.FindIntervals method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolIntervalsFilter`
              - The filter selects intervals of at least/most certain duration.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolIntervalsVectorResult`
              - Contains the results returned with ITimeToolTimeIntervalCollection.FindIntervalCollection method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolIntervalVectorCollection`
              - A collection of interval collections.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolLightTimeDelay`
              - Manage Light Time Delay options..

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingInterval`
              - The interface represents an interval with the time, position and velocity arrays.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingIntervalCollection`
              - A collection of intervals where each interval contains the time, position and velocity arrays.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolPointSamplingResult`
              - Contains tabulated positions and velocities of a point created by Sample method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolPruneFilter`
              - A filter used with event interval list pruned class to prune interval lists...

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolPruneFilterFactory`
              - The factory creates pruning filters.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolSignalDelayBasic`
              - Signal delay definition determines how long it takes for a signal to propagate from one location to another.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArray`
              - An ordered array of times, which may or may not be evenly spaced.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayConditionCrossings`
              - Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayExtrema`
              - Determine times of local minimum and/or maximum of specified scalar calculation. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFactory`
              - The factory creates event arrays.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered`
              - Defined by filtering times from original time array according to specified filtering method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFindTimesResult`
              - Return a collection of intervals and an array of times.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep`
              - Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedTimes`
              - Array defined by time ordered instants each explicitly specified.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayGroup`
              - Access or create VGT event arrays associated with an object.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayMerged`
              - Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArraySignaled`
              - Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations...

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayStartStopTimes`
              - Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeInterval`
              - A single time interval.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalBetweenTimeInstants`
              - Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollection`
              - A collection of related interval lists.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionFactory`
              - The factory creates collections of event interval lists.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionGroup`
              - Access or create VGT event interval collections associated with an object.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionLighting`
              - Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionOccurredResult`
              - Contains the results returned with ITimeToolTimeIntervalCollection.Occurred method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalCollectionSignaled`
              - Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations...

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFactory`
              - The factory creates event intervals.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFirstIntervalsFilter`
              - The filter selects a portion of first intervals.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixed`
              - Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixedDuration`
              - Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFromIntervalList`
              - Interval created from specified interval list by using one of several selection methods.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGapsFilter`
              - The filter merges intervals unless they are separated by gaps of at least/most certain duration.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup`
              - Access or create VGT event intervals associated with an object.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalLastIntervalsFilter`
              - The filter selects a portion of last intervals.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalList`
              - An ordered list of time intervals.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListCondition`
              - Interval list containing intervals during which specified condition is satisfied. Determination is performed within interval list using Sampling and Convergence parameters.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFactory`
              - The factory creates event interval lists.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFile`
              - Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFiltered`
              - Defined by filtering intervals from original interval list using specified filtering method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFixed`
              - Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup`
              - Access or create VGT event interval lists associated with an object.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged`
              - Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListScaled`
              - Interval List defined by scaling every interval in original interval list using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval is removed from scaled list...

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListSignaled`
              - Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations...

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListTimeOffset`
              - Interval List defined by shifting the specified reference interval list by a fixed time offset.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalRelativeSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain percentage of time.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalResult`
              - Contains the results returned with ITimeToolTimeIntervalList.FindIntervals method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSatisfactionConditionFilter`
              - The filter selects intervals if certain side condition is satisfied at least/most certain duration.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalScaled`
              - Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSignaled`
              - Determine what interval is recorded at target clock location by performing signal transmission of original interval between base and target clock locations.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval`
              - A smart interval.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalTimeOffset`
              - Interval defined by shifting specified reference interval by fixed time offset.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngle`
              - Base class for VGT axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleBetweenPlanes`
              - An angle between two planes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleBetweenVectors`
              - An angle between two vectors.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleDihedral`
              - An angle between two vectors about an axis.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleFactory`
              - A Factory object to create angles.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup`
              - Access or create VGT angles associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleReference`
              - Represents a reference to a VGT angle.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleRotation`
              - Angle of the shortest rotation between the specified FromAxes and ToAxes axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleToPlane`
              - An angle between a vector and a plane.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxes`
              - A generic axes class.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAlignedAndConstrained`
              - Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset`
              - Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAtTimeInstant`
              - Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAttitudeFile`
              - Axes specified by data from a file.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane`
              - B-Plane axes using the selected target body and reference vector.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks`
              - Provide methods to create non-persistent VGT axes components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCustomScript`
              - Customized axes offset with respect to a set of reference Axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFactory`
              - A Factory object to create axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixed`
              - Axes fixed in reference axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixedAtEpoch`
              - Axes based on another set fixed at a specified epoch.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup`
              - Access or create VGT axes associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesLabels`
              - Allow configuring the VGT axes labels.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesLagrangeLibration`
              - Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesModelAttachment`
              - Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesOnSurface`
              - Topocentric axes located at the reference point's projection on the central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesPlugin`
              - A VGT axes plugin.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesReference`
              - Represents a reference to a VGT axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesSpinning`
              - Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesTrajectory`
              - Axes based on trajectory of the point relative to the reference coordinate system.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlane`
              - Base class for VGT axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneFactory`
              - A Factory object to create VGT planes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneGroup`
              - Represents a VGT Plane component.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneLabels`
              - Allow configuring the X and Y axes labels.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneNormal`
              - A plane normal to a vector at a given point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneQuadrant`
              - A plane based on a selected Quadrant of a reference system.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneReference`
              - Represents a Plane reference.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTrajectory`
              - The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTriad`
              - A Plane containing points PointA, PointB and ReferencePont with the first axis aligned with the direction from the ReferencePoint to PointA and the second axis toward the direction from the ReferencePoint to PointB.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTwoVector`
              - A plane normal to a vector at a given point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPoint`
              - A generic VGT point class.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointAtTimeInstant`
              - Point fixed relative to reference system based on another point evaluated at specified time instant.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointBPlane`
              - B-Plane point using the selected target body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyFixedOffset`
              - Point specified by fixed components with respect to central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCentralBodyIntersect`
              - Point on central body surface along direction vector originating at source point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCommonTasks`
              - Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCovarianceGrazing`
              - The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFactory`
              - A Factory object to create points.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFile`
              - Point specified by data from a file.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFixedInSystem`
              - Point fixed in a reference coordinate system using the selected coordinate type.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGlint`
              - Point on central body surface that reflects from source to observer.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGrazing`
              - The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup`
              - Access or create VGT points associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointLagrangeLibration`
              - Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointModelAttachment`
              - A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointOnSurface`
              - The detic subpoint of the reference point as projected onto the central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneIntersection`
              - Point on a plane located along a given direction looking from a given origin.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlaneProjection`
              - The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointPlugin`
              - A VGT point plugin.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointReference`
              - Represents a reference to a VGT point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointSatelliteCollectionEntry`
              - A point placed at the center of mass of a specified satellite of the satellite collection.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystem`
              - Base class for VGT axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemAssembled`
              - A system assembled from an origin point and a set of reference axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemCommonTasks`
              - Provide methods to create non-persistent VGT coordinate reference frames (systems). Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemFactory`
              - A Factory class to create VGT systems.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemGroup`
              - Access or create VGT systems associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemOnSurface`
              - A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemReference`
              - Represents a System reference.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVector`
              - A generic vector class.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngleRate`
              - Angle rate vector perpendicular to the plane in which the angle is defined.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngularVelocity`
              - Angular velocity vector of one set of axes computed with respect to the reference set.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorApoapsis`
              - Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorConing`
              - Vector created by revolving the Reference vector around the About vector with the specified rate.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCross`
              - The vector cross product of two vectors.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCustomScript`
              - Customized vector components defined with respect to reference axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDerivative`
              - A vector derivative of a vector computed with respect to specified axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDirectionToStar`
              - Defined with respect to a star object. For a star object to be available, you must first create one.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement`
              - Vector defined by its start and end points.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorEccentricity`
              - A vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFactory`
              - A Factory object to create vectors.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFile`
              - Vector interpolated from tabulated data from file.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtEpoch`
              - Based on another vector fixed at a specified epoch.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtTimeInstant`
              - Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedInAxes`
              - Vector fixed in reference axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorGroup`
              - Access or create VGT vectors associated with an object or a central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLinearCombination`
              - Linear combination of two input vectors.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorLineOfNodes`
              - Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorModelAttachment`
              - Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitAngularMomentum`
              - Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorOrbitNormal`
              - Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorPeriapsis`
              - Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorPlugin`
              - A VGT vector plugin.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjection`
              - A projection of a vector computed with respect to a reference plane.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjectionAlongVector`
              - A projection of a source vector in the direction of another vector.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReference`
              - Represents a vector reference.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorReflection`
              - Incident vector reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorRotationVector`
              - Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarLinearCombination`
              - Linear combination of two input vectors using scalars.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScalarScaled`
              - Scaled version of the input vector using scalar.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorScaled`
              - Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorSurfaceDisplacement`
              - Displacement between origin and destination points using surface distance and altitude difference.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorTwoPlanesIntersection`
              - Defined along the intersection of two planes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorVelocityAcceleration`
              - Velocity vector of a point in a coordinate system.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolWellKnownAxes`
              - Represents well-known VGT Axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolWellKnownEarthAxes`
              - Well-known Earth's axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolWellKnownEarthSystems`
              - Well-known Earth's coordinate systems.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolWellKnownSunAxes`
              - Well-known Sun's axes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolWellKnownSunSystems`
              - The Sun's well-known coordinate reference systems.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolWellKnownSystems`
              - Well-known coordinate reference systems.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.analysis_workbench.AberrationModelType`
              - Define the model of aberration to use.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AngleToLocationType`
              - Define volume calc angle off vector reference types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AngleType`
              - Represents angle types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AsymptoteDirectionType`
              - Direction options.

            * - :py:class:`~ansys.stk.core.analysis_workbench.AxesType`
              - Represents vector types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.CalculationScalarType`
              - Define available calculation scalar types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ClockHostType`
              - Define whether base or target of an Access instance holds the clock for Access times.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ConditionCombinedOperationType`
              - Define scalar condition combined operation types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ConditionSetType`
              - Define available condition set types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ConditionThresholdType`
              - Operations for Scalar Bounds Condition.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ConditionType`
              - Define available condition types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.DistanceToLocationType`
              - Define volume calc range distance types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.EventArrayFilterType`
              - Event array filter types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.EventArrayType`
              - Define available time array types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.EventIntervalCollectionType`
              - Define available interval collection types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.EventIntervalListType`
              - Define available interval list types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.EventIntervalType`
              - Define available interval types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.EventListMergeOperation`
              - Define merge operations for interval lists.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ExtremumType`
              - These constants are utilized when finding a local or global minimum or maximum, or the threshold crossing.

            * - :py:class:`~ansys.stk.core.analysis_workbench.FileInterpolatorType`
              - Interpolator types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.GridValuesMethodType`
              - Define volumetric grid values method types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.InheritDimensionType`
              - Define how dimension is inherited.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IntegrationWindowType`
              - Define the interval of times during which an integral is evaluated.

            * - :py:class:`~ansys.stk.core.analysis_workbench.InterpolationMethodType`
              - Interpolator types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IntersectionSurfaceType`
              - Intersection surface flags.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IntervalDurationType`
              - Duration for filtering intervals or gaps from interval lists or time arrays.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IntervalFromIntervalListSelectionType`
              - Select the method to choose an interval from an interval list.

            * - :py:class:`~ansys.stk.core.analysis_workbench.IntervalPruneFilterType`
              - Specify the filter for filtering interval lists or time arrays.

            * - :py:class:`~ansys.stk.core.analysis_workbench.LagrangeLibrationPointType`
              - Types of the Lagrange points, also known as libration points. Lagrange points are points in space where gravitational forces and the orbital motion of a body balance each other.

            * - :py:class:`~ansys.stk.core.analysis_workbench.LightingConditionsType`
              - Define spatial condition lighting conditions types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.MeanElementTheory`
              - Mean element theory types for approximating motion.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ParameterSetType`
              - Define parameter set types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.PlaneQuadrantType`
              - Quadrants from a reference system (e.g., XY, XZ, YZ, YX, ZX, ZY).

            * - :py:class:`~ansys.stk.core.analysis_workbench.PlaneType`
              - Represents plane types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.PointBPlaneType`
              - B-Plane point types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.PointType`
              - Represents point types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.PrincipalAxisOfRotationType`
              - Rotation directions.

            * - :py:class:`~ansys.stk.core.analysis_workbench.QuadratureType`
              - Integral types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.RangeSpeedType`
              - Define volume calc range distance types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ResultVectorRequestType`
              - Define volume result vector request types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.RotationSweepModeType`
              - The rotation sweeping modes.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SampleReferenceTimeType`
              - Event array reference type.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SatisfactionCrossing`
              - Direction crossing flags.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SaveDataType`
              - Method for saving computed data.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SignalDirectionType`
              - Signal sense transmission options.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SignalPathReferenceSystem`
              - Signal path reference system types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SignedAngleType`
              - Define options for computing an angle.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SmartEpochState`
              - Smart epoch states.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SmartIntervalState`
              - Smart interval states.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialCalculationAltitudeReferenceType`
              - Define volume calc altitude reference types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialCalculationType`
              - Define volume calc types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpatialConditionOverTypeDurationType`
              - Define spatial condition over time duration type.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SpeedType`
              - Define various speed options.

            * - :py:class:`~ansys.stk.core.analysis_workbench.StartStopType`
              - Start/stop options.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SurfaceReferenceShapeType`
              - Surface shape types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SurfaceShapeType`
              - Surface types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.SystemType`
              - Represents system types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.ThresholdConvergenceSenseType`
              - Specify the desired sense of the results from threshold crossing computations.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeEventType`
              - Define available time instant types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TimeSenseType`
              - Define whether object1 or object2 of an Access instance holds the clock for Access times.

            * - :py:class:`~ansys.stk.core.analysis_workbench.TrajectoryAxesCoordinatesType`
              - Trajectory axes coordinate types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorComponentType`
              - Define component directions for a vector.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolComponentType`
              - Represents kinds of vectory geometry components.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSamplingMethod`
              - Define the Sampling Method.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorGeometryToolScaledVectorDimensionInheritanceOptionType`
              - Dimension inheritance constants used to configure the dimension inheritance of a vector scaled by a scalar.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VectorType`
              - Represents vector types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VolumeCombinedOperationType`
              - Define spatial condition combined operation types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VolumeFromGridEdgeType`
              - Define spatial condition from grid edge type.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VolumeGridType`
              - Define volume grid types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VolumeSatisfactionAccumulationType`
              - Define volume calc spatial condition accumulation types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VolumeSatisfactionDurationType`
              - Define volume calc spatial condition duration types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VolumeSatisfactionFilterType`
              - Define volume calc spatial condition filter types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VolumeSatisfactionMetricType`
              - Define volume calc spatial condition satisfaction metric types.

            * - :py:class:`~ansys.stk.core.analysis_workbench.VolumeType`
              - Define volume grid types.



Description
-----------

The Vector Geometry (VGT) API enables users define new or utilize existing geometric constructs such as coordinate systems, vectors, points, angles, axes and planes.

The geometric elements can be used to transform between coordinate
systems, compute first and second derivatives, or perform other types of
analysis.


.. py:currentmodule:: ansys.stk.core.analysis_workbench


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IAnalysisWorkbenchComponent<analysis_workbench/IAnalysisWorkbenchComponent>
     IAnalysisWorkbenchComponentContext<analysis_workbench/IAnalysisWorkbenchComponentContext>
     IAnalysisWorkbenchComponentReference<analysis_workbench/IAnalysisWorkbenchComponentReference>
     IAnalysisWorkbenchComponentTimeProperties<analysis_workbench/IAnalysisWorkbenchComponentTimeProperties>
     IAnalysisWorkbenchConvergence<analysis_workbench/IAnalysisWorkbenchConvergence>
     IAnalysisWorkbenchDerivative<analysis_workbench/IAnalysisWorkbenchDerivative>
     IAnalysisWorkbenchIntegral<analysis_workbench/IAnalysisWorkbenchIntegral>
     IAnalysisWorkbenchInterpolator<analysis_workbench/IAnalysisWorkbenchInterpolator>
     IAnalysisWorkbenchMethodCallResult<analysis_workbench/IAnalysisWorkbenchMethodCallResult>
     IAnalysisWorkbenchSampling<analysis_workbench/IAnalysisWorkbenchSampling>
     IAnalysisWorkbenchSignalDelay<analysis_workbench/IAnalysisWorkbenchSignalDelay>
     ICalculationToolCondition<analysis_workbench/ICalculationToolCondition>
     ICalculationToolConditionSet<analysis_workbench/ICalculationToolConditionSet>
     ICalculationToolParameterSet<analysis_workbench/ICalculationToolParameterSet>
     ICalculationToolSamplingMethod<analysis_workbench/ICalculationToolSamplingMethod>
     ICalculationToolScalar<analysis_workbench/ICalculationToolScalar>
     ISpatialAnalysisToolGridValuesMethod<analysis_workbench/ISpatialAnalysisToolGridValuesMethod>
     ISpatialAnalysisToolSpatialCalculation<analysis_workbench/ISpatialAnalysisToolSpatialCalculation>
     ISpatialAnalysisToolVolume<analysis_workbench/ISpatialAnalysisToolVolume>
     ISpatialAnalysisToolVolumeGrid<analysis_workbench/ISpatialAnalysisToolVolumeGrid>
     ITimeToolInstant<analysis_workbench/ITimeToolInstant>
     ITimeToolPruneFilter<analysis_workbench/ITimeToolPruneFilter>
     ITimeToolTimeArray<analysis_workbench/ITimeToolTimeArray>
     ITimeToolTimeInterval<analysis_workbench/ITimeToolTimeInterval>
     ITimeToolTimeIntervalCollection<analysis_workbench/ITimeToolTimeIntervalCollection>
     ITimeToolTimeIntervalList<analysis_workbench/ITimeToolTimeIntervalList>
     IVectorGeometryToolAngle<analysis_workbench/IVectorGeometryToolAngle>
     IVectorGeometryToolAxes<analysis_workbench/IVectorGeometryToolAxes>
     IVectorGeometryToolPlane<analysis_workbench/IVectorGeometryToolPlane>
     IVectorGeometryToolPoint<analysis_workbench/IVectorGeometryToolPoint>
     IVectorGeometryToolSystem<analysis_workbench/IVectorGeometryToolSystem>
     IVectorGeometryToolVector<analysis_workbench/IVectorGeometryToolVector>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     AnalysisWorkbenchAngleFindAngleResult<analysis_workbench/AnalysisWorkbenchAngleFindAngleResult>
     AnalysisWorkbenchAngleFindAngleWithRateResult<analysis_workbench/AnalysisWorkbenchAngleFindAngleWithRateResult>
     AnalysisWorkbenchAngleFindResult<analysis_workbench/AnalysisWorkbenchAngleFindResult>
     AnalysisWorkbenchAngleFindWithRateResult<analysis_workbench/AnalysisWorkbenchAngleFindWithRateResult>
     AnalysisWorkbenchAxesFindInAxesResult<analysis_workbench/AnalysisWorkbenchAxesFindInAxesResult>
     AnalysisWorkbenchAxesFindInAxesWithRateResult<analysis_workbench/AnalysisWorkbenchAxesFindInAxesWithRateResult>
     AnalysisWorkbenchAxesTransformResult<analysis_workbench/AnalysisWorkbenchAxesTransformResult>
     AnalysisWorkbenchAxesTransformWithRateResult<analysis_workbench/AnalysisWorkbenchAxesTransformWithRateResult>
     AnalysisWorkbenchCentralBody<analysis_workbench/AnalysisWorkbenchCentralBody>
     AnalysisWorkbenchCentralBodyCollection<analysis_workbench/AnalysisWorkbenchCentralBodyCollection>
     AnalysisWorkbenchCentralBodyReference<analysis_workbench/AnalysisWorkbenchCentralBodyReference>
     AnalysisWorkbenchComponent<analysis_workbench/AnalysisWorkbenchComponent>
     AnalysisWorkbenchComponentCollection<analysis_workbench/AnalysisWorkbenchComponentCollection>
     AnalysisWorkbenchComponentInstance<analysis_workbench/AnalysisWorkbenchComponentInstance>
     AnalysisWorkbenchComponentProvider<analysis_workbench/AnalysisWorkbenchComponentProvider>
     AnalysisWorkbenchComponentTemplate<analysis_workbench/AnalysisWorkbenchComponentTemplate>
     AnalysisWorkbenchComponentTypeInformation<analysis_workbench/AnalysisWorkbenchComponentTypeInformation>
     AnalysisWorkbenchConvergence<analysis_workbench/AnalysisWorkbenchConvergence>
     AnalysisWorkbenchDerivative<analysis_workbench/AnalysisWorkbenchDerivative>
     AnalysisWorkbenchIntegral<analysis_workbench/AnalysisWorkbenchIntegral>
     AnalysisWorkbenchInterpolator<analysis_workbench/AnalysisWorkbenchInterpolator>
     AnalysisWorkbenchPlaneFindInAxesResult<analysis_workbench/AnalysisWorkbenchPlaneFindInAxesResult>
     AnalysisWorkbenchPlaneFindInAxesWithRateResult<analysis_workbench/AnalysisWorkbenchPlaneFindInAxesWithRateResult>
     AnalysisWorkbenchPlaneFindInSystemResult<analysis_workbench/AnalysisWorkbenchPlaneFindInSystemResult>
     AnalysisWorkbenchPlaneFindInSystemWithRateResult<analysis_workbench/AnalysisWorkbenchPlaneFindInSystemWithRateResult>
     AnalysisWorkbenchPointLocateInSystemResult<analysis_workbench/AnalysisWorkbenchPointLocateInSystemResult>
     AnalysisWorkbenchPointLocateInSystemWithRateResult<analysis_workbench/AnalysisWorkbenchPointLocateInSystemWithRateResult>
     AnalysisWorkbenchPositionLLA<analysis_workbench/AnalysisWorkbenchPositionLLA>
     AnalysisWorkbenchRoot<analysis_workbench/AnalysisWorkbenchRoot>
     AnalysisWorkbenchSampling<analysis_workbench/AnalysisWorkbenchSampling>
     AnalysisWorkbenchSignalDelay<analysis_workbench/AnalysisWorkbenchSignalDelay>
     AnalysisWorkbenchSystemFindInSystemResult<analysis_workbench/AnalysisWorkbenchSystemFindInSystemResult>
     AnalysisWorkbenchSystemTransformResult<analysis_workbench/AnalysisWorkbenchSystemTransformResult>
     AnalysisWorkbenchSystemTransformWithRateResult<analysis_workbench/AnalysisWorkbenchSystemTransformWithRateResult>
     AnalysisWorkbenchVectorFindInAxesResult<analysis_workbench/AnalysisWorkbenchVectorFindInAxesResult>
     AnalysisWorkbenchVectorFindInAxesWithRateResult<analysis_workbench/AnalysisWorkbenchVectorFindInAxesWithRateResult>
     CalculationToolCondition<analysis_workbench/CalculationToolCondition>
     CalculationToolConditionCombined<analysis_workbench/CalculationToolConditionCombined>
     CalculationToolConditionFactory<analysis_workbench/CalculationToolConditionFactory>
     CalculationToolConditionGroup<analysis_workbench/CalculationToolConditionGroup>
     CalculationToolConditionScalarBounds<analysis_workbench/CalculationToolConditionScalarBounds>
     CalculationToolConditionSet<analysis_workbench/CalculationToolConditionSet>
     CalculationToolConditionSetEvaluateResult<analysis_workbench/CalculationToolConditionSetEvaluateResult>
     CalculationToolConditionSetEvaluateWithRateResult<analysis_workbench/CalculationToolConditionSetEvaluateWithRateResult>
     CalculationToolConditionSetFactory<analysis_workbench/CalculationToolConditionSetFactory>
     CalculationToolConditionSetGroup<analysis_workbench/CalculationToolConditionSetGroup>
     CalculationToolConditionSetScalarThresholds<analysis_workbench/CalculationToolConditionSetScalarThresholds>
     CalculationToolConditionTrajectoryWithinVolume<analysis_workbench/CalculationToolConditionTrajectoryWithinVolume>
     CalculationToolConvergeBasic<analysis_workbench/CalculationToolConvergeBasic>
     CalculationToolDerivativeBasic<analysis_workbench/CalculationToolDerivativeBasic>
     CalculationToolEvaluateResult<analysis_workbench/CalculationToolEvaluateResult>
     CalculationToolEvaluateWithRateResult<analysis_workbench/CalculationToolEvaluateWithRateResult>
     CalculationToolIntegralBasic<analysis_workbench/CalculationToolIntegralBasic>
     CalculationToolInterpolatorBasic<analysis_workbench/CalculationToolInterpolatorBasic>
     CalculationToolParameterSet<analysis_workbench/CalculationToolParameterSet>
     CalculationToolParameterSetAttitude<analysis_workbench/CalculationToolParameterSetAttitude>
     CalculationToolParameterSetFactory<analysis_workbench/CalculationToolParameterSetFactory>
     CalculationToolParameterSetGroundTrajectory<analysis_workbench/CalculationToolParameterSetGroundTrajectory>
     CalculationToolParameterSetGroup<analysis_workbench/CalculationToolParameterSetGroup>
     CalculationToolParameterSetOrbit<analysis_workbench/CalculationToolParameterSetOrbit>
     CalculationToolParameterSetTrajectory<analysis_workbench/CalculationToolParameterSetTrajectory>
     CalculationToolParameterSetVector<analysis_workbench/CalculationToolParameterSetVector>
     CalculationToolSamplingBasic<analysis_workbench/CalculationToolSamplingBasic>
     CalculationToolSamplingCurvatureTolerance<analysis_workbench/CalculationToolSamplingCurvatureTolerance>
     CalculationToolSamplingFixedStep<analysis_workbench/CalculationToolSamplingFixedStep>
     CalculationToolSamplingMethod<analysis_workbench/CalculationToolSamplingMethod>
     CalculationToolSamplingMethodFactory<analysis_workbench/CalculationToolSamplingMethodFactory>
     CalculationToolSamplingRelativeTolerance<analysis_workbench/CalculationToolSamplingRelativeTolerance>
     CalculationToolScalar<analysis_workbench/CalculationToolScalar>
     CalculationToolScalarAlongTrajectory<analysis_workbench/CalculationToolScalarAlongTrajectory>
     CalculationToolScalarAngle<analysis_workbench/CalculationToolScalarAngle>
     CalculationToolScalarAverage<analysis_workbench/CalculationToolScalarAverage>
     CalculationToolScalarConstant<analysis_workbench/CalculationToolScalarConstant>
     CalculationToolScalarCustom<analysis_workbench/CalculationToolScalarCustom>
     CalculationToolScalarCustomInlineScript<analysis_workbench/CalculationToolScalarCustomInlineScript>
     CalculationToolScalarDataElement<analysis_workbench/CalculationToolScalarDataElement>
     CalculationToolScalarDerivative<analysis_workbench/CalculationToolScalarDerivative>
     CalculationToolScalarDotProduct<analysis_workbench/CalculationToolScalarDotProduct>
     CalculationToolScalarElapsedTime<analysis_workbench/CalculationToolScalarElapsedTime>
     CalculationToolScalarFactory<analysis_workbench/CalculationToolScalarFactory>
     CalculationToolScalarFile<analysis_workbench/CalculationToolScalarFile>
     CalculationToolScalarFixedAtTimeInstant<analysis_workbench/CalculationToolScalarFixedAtTimeInstant>
     CalculationToolScalarFunction<analysis_workbench/CalculationToolScalarFunction>
     CalculationToolScalarFunctionOf2Variables<analysis_workbench/CalculationToolScalarFunctionOf2Variables>
     CalculationToolScalarGroup<analysis_workbench/CalculationToolScalarGroup>
     CalculationToolScalarIntegral<analysis_workbench/CalculationToolScalarIntegral>
     CalculationToolScalarPlugin<analysis_workbench/CalculationToolScalarPlugin>
     CalculationToolScalarStandardDeviation<analysis_workbench/CalculationToolScalarStandardDeviation>
     CalculationToolScalarSurfaceDistanceBetweenPoints<analysis_workbench/CalculationToolScalarSurfaceDistanceBetweenPoints>
     CalculationToolScalarVectorComponent<analysis_workbench/CalculationToolScalarVectorComponent>
     CalculationToolScalarVectorMagnitude<analysis_workbench/CalculationToolScalarVectorMagnitude>
     SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude<analysis_workbench/SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude>
     SpatialAnalysisToolCalculationAltitude<analysis_workbench/SpatialAnalysisToolCalculationAltitude>
     SpatialAnalysisToolCalculationAngleToLocation<analysis_workbench/SpatialAnalysisToolCalculationAngleToLocation>
     SpatialAnalysisToolCalculationConditionSatisfactionMetric<analysis_workbench/SpatialAnalysisToolCalculationConditionSatisfactionMetric>
     SpatialAnalysisToolCalculationDistanceToLocation<analysis_workbench/SpatialAnalysisToolCalculationDistanceToLocation>
     SpatialAnalysisToolCalculationFactory<analysis_workbench/SpatialAnalysisToolCalculationFactory>
     SpatialAnalysisToolCalculationFile<analysis_workbench/SpatialAnalysisToolCalculationFile>
     SpatialAnalysisToolCalculationFromCalculationScalar<analysis_workbench/SpatialAnalysisToolCalculationFromCalculationScalar>
     SpatialAnalysisToolCalculationGroup<analysis_workbench/SpatialAnalysisToolCalculationGroup>
     SpatialAnalysisToolCalculationPropagationDelayToLocation<analysis_workbench/SpatialAnalysisToolCalculationPropagationDelayToLocation>
     SpatialAnalysisToolCalculationSolarIntensity<analysis_workbench/SpatialAnalysisToolCalculationSolarIntensity>
     SpatialAnalysisToolConditionAccessToLocation<analysis_workbench/SpatialAnalysisToolConditionAccessToLocation>
     SpatialAnalysisToolConditionCombined<analysis_workbench/SpatialAnalysisToolConditionCombined>
     SpatialAnalysisToolConditionConditionAtLocation<analysis_workbench/SpatialAnalysisToolConditionConditionAtLocation>
     SpatialAnalysisToolConditionFactory<analysis_workbench/SpatialAnalysisToolConditionFactory>
     SpatialAnalysisToolConditionGridBoundingVolume<analysis_workbench/SpatialAnalysisToolConditionGridBoundingVolume>
     SpatialAnalysisToolConditionGroup<analysis_workbench/SpatialAnalysisToolConditionGroup>
     SpatialAnalysisToolConditionLighting<analysis_workbench/SpatialAnalysisToolConditionLighting>
     SpatialAnalysisToolConditionOverTime<analysis_workbench/SpatialAnalysisToolConditionOverTime>
     SpatialAnalysisToolConditionSpatialCalculationBounds<analysis_workbench/SpatialAnalysisToolConditionSpatialCalculationBounds>
     SpatialAnalysisToolConditionValidTimeAtLocation<analysis_workbench/SpatialAnalysisToolConditionValidTimeAtLocation>
     SpatialAnalysisToolGridCoordinateDefinition<analysis_workbench/SpatialAnalysisToolGridCoordinateDefinition>
     SpatialAnalysisToolGridValuesCustom<analysis_workbench/SpatialAnalysisToolGridValuesCustom>
     SpatialAnalysisToolGridValuesFixedNumberOfSteps<analysis_workbench/SpatialAnalysisToolGridValuesFixedNumberOfSteps>
     SpatialAnalysisToolGridValuesFixedStep<analysis_workbench/SpatialAnalysisToolGridValuesFixedStep>
     SpatialAnalysisToolGridValuesMethod<analysis_workbench/SpatialAnalysisToolGridValuesMethod>
     SpatialAnalysisToolSpatialCalculation<analysis_workbench/SpatialAnalysisToolSpatialCalculation>
     SpatialAnalysisToolVolume<analysis_workbench/SpatialAnalysisToolVolume>
     SpatialAnalysisToolVolumeGrid<analysis_workbench/SpatialAnalysisToolVolumeGrid>
     SpatialAnalysisToolVolumeGridCartesian<analysis_workbench/SpatialAnalysisToolVolumeGridCartesian>
     SpatialAnalysisToolVolumeGridConstrained<analysis_workbench/SpatialAnalysisToolVolumeGridConstrained>
     SpatialAnalysisToolVolumeGridCylindrical<analysis_workbench/SpatialAnalysisToolVolumeGridCylindrical>
     SpatialAnalysisToolVolumeGridFactory<analysis_workbench/SpatialAnalysisToolVolumeGridFactory>
     SpatialAnalysisToolVolumeGridGroup<analysis_workbench/SpatialAnalysisToolVolumeGridGroup>
     SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude<analysis_workbench/SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude>
     SpatialAnalysisToolVolumeGridResult<analysis_workbench/SpatialAnalysisToolVolumeGridResult>
     SpatialAnalysisToolVolumeGridSpherical<analysis_workbench/SpatialAnalysisToolVolumeGridSpherical>
     TimeToolAxesSamplingInterval<analysis_workbench/TimeToolAxesSamplingInterval>
     TimeToolAxesSamplingIntervalCollection<analysis_workbench/TimeToolAxesSamplingIntervalCollection>
     TimeToolAxesSamplingResult<analysis_workbench/TimeToolAxesSamplingResult>
     TimeToolInstant<analysis_workbench/TimeToolInstant>
     TimeToolInstantEpoch<analysis_workbench/TimeToolInstantEpoch>
     TimeToolInstantExtremum<analysis_workbench/TimeToolInstantExtremum>
     TimeToolInstantFactory<analysis_workbench/TimeToolInstantFactory>
     TimeToolInstantGroup<analysis_workbench/TimeToolInstantGroup>
     TimeToolInstantOccurrenceResult<analysis_workbench/TimeToolInstantOccurrenceResult>
     TimeToolInstantSignaled<analysis_workbench/TimeToolInstantSignaled>
     TimeToolInstantSmartEpoch<analysis_workbench/TimeToolInstantSmartEpoch>
     TimeToolInstantStartStopTime<analysis_workbench/TimeToolInstantStartStopTime>
     TimeToolInstantTimeOffset<analysis_workbench/TimeToolInstantTimeOffset>
     TimeToolInterval<analysis_workbench/TimeToolInterval>
     TimeToolIntervalCollection<analysis_workbench/TimeToolIntervalCollection>
     TimeToolIntervalListResult<analysis_workbench/TimeToolIntervalListResult>
     TimeToolIntervalsFilter<analysis_workbench/TimeToolIntervalsFilter>
     TimeToolIntervalsVectorResult<analysis_workbench/TimeToolIntervalsVectorResult>
     TimeToolIntervalVectorCollection<analysis_workbench/TimeToolIntervalVectorCollection>
     TimeToolLightTimeDelay<analysis_workbench/TimeToolLightTimeDelay>
     TimeToolPointSamplingInterval<analysis_workbench/TimeToolPointSamplingInterval>
     TimeToolPointSamplingIntervalCollection<analysis_workbench/TimeToolPointSamplingIntervalCollection>
     TimeToolPointSamplingResult<analysis_workbench/TimeToolPointSamplingResult>
     TimeToolPruneFilter<analysis_workbench/TimeToolPruneFilter>
     TimeToolPruneFilterFactory<analysis_workbench/TimeToolPruneFilterFactory>
     TimeToolSignalDelayBasic<analysis_workbench/TimeToolSignalDelayBasic>
     TimeToolTimeArray<analysis_workbench/TimeToolTimeArray>
     TimeToolTimeArrayConditionCrossings<analysis_workbench/TimeToolTimeArrayConditionCrossings>
     TimeToolTimeArrayExtrema<analysis_workbench/TimeToolTimeArrayExtrema>
     TimeToolTimeArrayFactory<analysis_workbench/TimeToolTimeArrayFactory>
     TimeToolTimeArrayFiltered<analysis_workbench/TimeToolTimeArrayFiltered>
     TimeToolTimeArrayFindTimesResult<analysis_workbench/TimeToolTimeArrayFindTimesResult>
     TimeToolTimeArrayFixedStep<analysis_workbench/TimeToolTimeArrayFixedStep>
     TimeToolTimeArrayFixedTimes<analysis_workbench/TimeToolTimeArrayFixedTimes>
     TimeToolTimeArrayGroup<analysis_workbench/TimeToolTimeArrayGroup>
     TimeToolTimeArrayMerged<analysis_workbench/TimeToolTimeArrayMerged>
     TimeToolTimeArraySignaled<analysis_workbench/TimeToolTimeArraySignaled>
     TimeToolTimeArrayStartStopTimes<analysis_workbench/TimeToolTimeArrayStartStopTimes>
     TimeToolTimeInterval<analysis_workbench/TimeToolTimeInterval>
     TimeToolTimeIntervalBetweenTimeInstants<analysis_workbench/TimeToolTimeIntervalBetweenTimeInstants>
     TimeToolTimeIntervalCollection<analysis_workbench/TimeToolTimeIntervalCollection>
     TimeToolTimeIntervalCollectionCondition<analysis_workbench/TimeToolTimeIntervalCollectionCondition>
     TimeToolTimeIntervalCollectionFactory<analysis_workbench/TimeToolTimeIntervalCollectionFactory>
     TimeToolTimeIntervalCollectionGroup<analysis_workbench/TimeToolTimeIntervalCollectionGroup>
     TimeToolTimeIntervalCollectionLighting<analysis_workbench/TimeToolTimeIntervalCollectionLighting>
     TimeToolTimeIntervalCollectionOccurredResult<analysis_workbench/TimeToolTimeIntervalCollectionOccurredResult>
     TimeToolTimeIntervalCollectionSignaled<analysis_workbench/TimeToolTimeIntervalCollectionSignaled>
     TimeToolTimeIntervalFactory<analysis_workbench/TimeToolTimeIntervalFactory>
     TimeToolTimeIntervalFirstIntervalsFilter<analysis_workbench/TimeToolTimeIntervalFirstIntervalsFilter>
     TimeToolTimeIntervalFixed<analysis_workbench/TimeToolTimeIntervalFixed>
     TimeToolTimeIntervalFixedDuration<analysis_workbench/TimeToolTimeIntervalFixedDuration>
     TimeToolTimeIntervalFromIntervalList<analysis_workbench/TimeToolTimeIntervalFromIntervalList>
     TimeToolTimeIntervalGapsFilter<analysis_workbench/TimeToolTimeIntervalGapsFilter>
     TimeToolTimeIntervalGroup<analysis_workbench/TimeToolTimeIntervalGroup>
     TimeToolTimeIntervalLastIntervalsFilter<analysis_workbench/TimeToolTimeIntervalLastIntervalsFilter>
     TimeToolTimeIntervalList<analysis_workbench/TimeToolTimeIntervalList>
     TimeToolTimeIntervalListCondition<analysis_workbench/TimeToolTimeIntervalListCondition>
     TimeToolTimeIntervalListFactory<analysis_workbench/TimeToolTimeIntervalListFactory>
     TimeToolTimeIntervalListFile<analysis_workbench/TimeToolTimeIntervalListFile>
     TimeToolTimeIntervalListFiltered<analysis_workbench/TimeToolTimeIntervalListFiltered>
     TimeToolTimeIntervalListFixed<analysis_workbench/TimeToolTimeIntervalListFixed>
     TimeToolTimeIntervalListGroup<analysis_workbench/TimeToolTimeIntervalListGroup>
     TimeToolTimeIntervalListMerged<analysis_workbench/TimeToolTimeIntervalListMerged>
     TimeToolTimeIntervalListScaled<analysis_workbench/TimeToolTimeIntervalListScaled>
     TimeToolTimeIntervalListSignaled<analysis_workbench/TimeToolTimeIntervalListSignaled>
     TimeToolTimeIntervalListTimeOffset<analysis_workbench/TimeToolTimeIntervalListTimeOffset>
     TimeToolTimeIntervalRelativeSatisfactionConditionFilter<analysis_workbench/TimeToolTimeIntervalRelativeSatisfactionConditionFilter>
     TimeToolTimeIntervalResult<analysis_workbench/TimeToolTimeIntervalResult>
     TimeToolTimeIntervalSatisfactionConditionFilter<analysis_workbench/TimeToolTimeIntervalSatisfactionConditionFilter>
     TimeToolTimeIntervalScaled<analysis_workbench/TimeToolTimeIntervalScaled>
     TimeToolTimeIntervalSignaled<analysis_workbench/TimeToolTimeIntervalSignaled>
     TimeToolTimeIntervalSmartInterval<analysis_workbench/TimeToolTimeIntervalSmartInterval>
     TimeToolTimeIntervalTimeOffset<analysis_workbench/TimeToolTimeIntervalTimeOffset>
     VectorGeometryToolAngle<analysis_workbench/VectorGeometryToolAngle>
     VectorGeometryToolAngleBetweenPlanes<analysis_workbench/VectorGeometryToolAngleBetweenPlanes>
     VectorGeometryToolAngleBetweenVectors<analysis_workbench/VectorGeometryToolAngleBetweenVectors>
     VectorGeometryToolAngleDihedral<analysis_workbench/VectorGeometryToolAngleDihedral>
     VectorGeometryToolAngleFactory<analysis_workbench/VectorGeometryToolAngleFactory>
     VectorGeometryToolAngleGroup<analysis_workbench/VectorGeometryToolAngleGroup>
     VectorGeometryToolAngleReference<analysis_workbench/VectorGeometryToolAngleReference>
     VectorGeometryToolAngleRotation<analysis_workbench/VectorGeometryToolAngleRotation>
     VectorGeometryToolAngleToPlane<analysis_workbench/VectorGeometryToolAngleToPlane>
     VectorGeometryToolAxes<analysis_workbench/VectorGeometryToolAxes>
     VectorGeometryToolAxesAlignedAndConstrained<analysis_workbench/VectorGeometryToolAxesAlignedAndConstrained>
     VectorGeometryToolAxesAngularOffset<analysis_workbench/VectorGeometryToolAxesAngularOffset>
     VectorGeometryToolAxesAtTimeInstant<analysis_workbench/VectorGeometryToolAxesAtTimeInstant>
     VectorGeometryToolAxesAttitudeFile<analysis_workbench/VectorGeometryToolAxesAttitudeFile>
     VectorGeometryToolAxesBPlane<analysis_workbench/VectorGeometryToolAxesBPlane>
     VectorGeometryToolAxesCommonTasks<analysis_workbench/VectorGeometryToolAxesCommonTasks>
     VectorGeometryToolAxesCustomScript<analysis_workbench/VectorGeometryToolAxesCustomScript>
     VectorGeometryToolAxesFactory<analysis_workbench/VectorGeometryToolAxesFactory>
     VectorGeometryToolAxesFixed<analysis_workbench/VectorGeometryToolAxesFixed>
     VectorGeometryToolAxesFixedAtEpoch<analysis_workbench/VectorGeometryToolAxesFixedAtEpoch>
     VectorGeometryToolAxesGroup<analysis_workbench/VectorGeometryToolAxesGroup>
     VectorGeometryToolAxesLabels<analysis_workbench/VectorGeometryToolAxesLabels>
     VectorGeometryToolAxesLagrangeLibration<analysis_workbench/VectorGeometryToolAxesLagrangeLibration>
     VectorGeometryToolAxesModelAttachment<analysis_workbench/VectorGeometryToolAxesModelAttachment>
     VectorGeometryToolAxesOnSurface<analysis_workbench/VectorGeometryToolAxesOnSurface>
     VectorGeometryToolAxesPlugin<analysis_workbench/VectorGeometryToolAxesPlugin>
     VectorGeometryToolAxesReference<analysis_workbench/VectorGeometryToolAxesReference>
     VectorGeometryToolAxesSpinning<analysis_workbench/VectorGeometryToolAxesSpinning>
     VectorGeometryToolAxesTrajectory<analysis_workbench/VectorGeometryToolAxesTrajectory>
     VectorGeometryToolPlane<analysis_workbench/VectorGeometryToolPlane>
     VectorGeometryToolPlaneFactory<analysis_workbench/VectorGeometryToolPlaneFactory>
     VectorGeometryToolPlaneGroup<analysis_workbench/VectorGeometryToolPlaneGroup>
     VectorGeometryToolPlaneLabels<analysis_workbench/VectorGeometryToolPlaneLabels>
     VectorGeometryToolPlaneNormal<analysis_workbench/VectorGeometryToolPlaneNormal>
     VectorGeometryToolPlaneQuadrant<analysis_workbench/VectorGeometryToolPlaneQuadrant>
     VectorGeometryToolPlaneReference<analysis_workbench/VectorGeometryToolPlaneReference>
     VectorGeometryToolPlaneTrajectory<analysis_workbench/VectorGeometryToolPlaneTrajectory>
     VectorGeometryToolPlaneTriad<analysis_workbench/VectorGeometryToolPlaneTriad>
     VectorGeometryToolPlaneTwoVector<analysis_workbench/VectorGeometryToolPlaneTwoVector>
     VectorGeometryToolPoint<analysis_workbench/VectorGeometryToolPoint>
     VectorGeometryToolPointAtTimeInstant<analysis_workbench/VectorGeometryToolPointAtTimeInstant>
     VectorGeometryToolPointBPlane<analysis_workbench/VectorGeometryToolPointBPlane>
     VectorGeometryToolPointCentralBodyFixedOffset<analysis_workbench/VectorGeometryToolPointCentralBodyFixedOffset>
     VectorGeometryToolPointCentralBodyIntersect<analysis_workbench/VectorGeometryToolPointCentralBodyIntersect>
     VectorGeometryToolPointCommonTasks<analysis_workbench/VectorGeometryToolPointCommonTasks>
     VectorGeometryToolPointCovarianceGrazing<analysis_workbench/VectorGeometryToolPointCovarianceGrazing>
     VectorGeometryToolPointFactory<analysis_workbench/VectorGeometryToolPointFactory>
     VectorGeometryToolPointFile<analysis_workbench/VectorGeometryToolPointFile>
     VectorGeometryToolPointFixedInSystem<analysis_workbench/VectorGeometryToolPointFixedInSystem>
     VectorGeometryToolPointGlint<analysis_workbench/VectorGeometryToolPointGlint>
     VectorGeometryToolPointGrazing<analysis_workbench/VectorGeometryToolPointGrazing>
     VectorGeometryToolPointGroup<analysis_workbench/VectorGeometryToolPointGroup>
     VectorGeometryToolPointLagrangeLibration<analysis_workbench/VectorGeometryToolPointLagrangeLibration>
     VectorGeometryToolPointModelAttachment<analysis_workbench/VectorGeometryToolPointModelAttachment>
     VectorGeometryToolPointOnSurface<analysis_workbench/VectorGeometryToolPointOnSurface>
     VectorGeometryToolPointPlaneIntersection<analysis_workbench/VectorGeometryToolPointPlaneIntersection>
     VectorGeometryToolPointPlaneProjection<analysis_workbench/VectorGeometryToolPointPlaneProjection>
     VectorGeometryToolPointPlugin<analysis_workbench/VectorGeometryToolPointPlugin>
     VectorGeometryToolPointReference<analysis_workbench/VectorGeometryToolPointReference>
     VectorGeometryToolPointSatelliteCollectionEntry<analysis_workbench/VectorGeometryToolPointSatelliteCollectionEntry>
     VectorGeometryToolSystem<analysis_workbench/VectorGeometryToolSystem>
     VectorGeometryToolSystemAssembled<analysis_workbench/VectorGeometryToolSystemAssembled>
     VectorGeometryToolSystemCommonTasks<analysis_workbench/VectorGeometryToolSystemCommonTasks>
     VectorGeometryToolSystemFactory<analysis_workbench/VectorGeometryToolSystemFactory>
     VectorGeometryToolSystemGroup<analysis_workbench/VectorGeometryToolSystemGroup>
     VectorGeometryToolSystemOnSurface<analysis_workbench/VectorGeometryToolSystemOnSurface>
     VectorGeometryToolSystemReference<analysis_workbench/VectorGeometryToolSystemReference>
     VectorGeometryToolVector<analysis_workbench/VectorGeometryToolVector>
     VectorGeometryToolVectorAngleRate<analysis_workbench/VectorGeometryToolVectorAngleRate>
     VectorGeometryToolVectorAngularVelocity<analysis_workbench/VectorGeometryToolVectorAngularVelocity>
     VectorGeometryToolVectorApoapsis<analysis_workbench/VectorGeometryToolVectorApoapsis>
     VectorGeometryToolVectorConing<analysis_workbench/VectorGeometryToolVectorConing>
     VectorGeometryToolVectorCross<analysis_workbench/VectorGeometryToolVectorCross>
     VectorGeometryToolVectorCustomScript<analysis_workbench/VectorGeometryToolVectorCustomScript>
     VectorGeometryToolVectorDerivative<analysis_workbench/VectorGeometryToolVectorDerivative>
     VectorGeometryToolVectorDirectionToStar<analysis_workbench/VectorGeometryToolVectorDirectionToStar>
     VectorGeometryToolVectorDisplacement<analysis_workbench/VectorGeometryToolVectorDisplacement>
     VectorGeometryToolVectorEccentricity<analysis_workbench/VectorGeometryToolVectorEccentricity>
     VectorGeometryToolVectorFactory<analysis_workbench/VectorGeometryToolVectorFactory>
     VectorGeometryToolVectorFile<analysis_workbench/VectorGeometryToolVectorFile>
     VectorGeometryToolVectorFixedAtEpoch<analysis_workbench/VectorGeometryToolVectorFixedAtEpoch>
     VectorGeometryToolVectorFixedAtTimeInstant<analysis_workbench/VectorGeometryToolVectorFixedAtTimeInstant>
     VectorGeometryToolVectorFixedInAxes<analysis_workbench/VectorGeometryToolVectorFixedInAxes>
     VectorGeometryToolVectorGroup<analysis_workbench/VectorGeometryToolVectorGroup>
     VectorGeometryToolVectorLinearCombination<analysis_workbench/VectorGeometryToolVectorLinearCombination>
     VectorGeometryToolVectorLineOfNodes<analysis_workbench/VectorGeometryToolVectorLineOfNodes>
     VectorGeometryToolVectorModelAttachment<analysis_workbench/VectorGeometryToolVectorModelAttachment>
     VectorGeometryToolVectorOrbitAngularMomentum<analysis_workbench/VectorGeometryToolVectorOrbitAngularMomentum>
     VectorGeometryToolVectorOrbitNormal<analysis_workbench/VectorGeometryToolVectorOrbitNormal>
     VectorGeometryToolVectorPeriapsis<analysis_workbench/VectorGeometryToolVectorPeriapsis>
     VectorGeometryToolVectorPlugin<analysis_workbench/VectorGeometryToolVectorPlugin>
     VectorGeometryToolVectorProjection<analysis_workbench/VectorGeometryToolVectorProjection>
     VectorGeometryToolVectorProjectionAlongVector<analysis_workbench/VectorGeometryToolVectorProjectionAlongVector>
     VectorGeometryToolVectorReference<analysis_workbench/VectorGeometryToolVectorReference>
     VectorGeometryToolVectorReflection<analysis_workbench/VectorGeometryToolVectorReflection>
     VectorGeometryToolVectorRotationVector<analysis_workbench/VectorGeometryToolVectorRotationVector>
     VectorGeometryToolVectorScalarLinearCombination<analysis_workbench/VectorGeometryToolVectorScalarLinearCombination>
     VectorGeometryToolVectorScalarScaled<analysis_workbench/VectorGeometryToolVectorScalarScaled>
     VectorGeometryToolVectorScaled<analysis_workbench/VectorGeometryToolVectorScaled>
     VectorGeometryToolVectorSurfaceDisplacement<analysis_workbench/VectorGeometryToolVectorSurfaceDisplacement>
     VectorGeometryToolVectorTwoPlanesIntersection<analysis_workbench/VectorGeometryToolVectorTwoPlanesIntersection>
     VectorGeometryToolVectorVelocityAcceleration<analysis_workbench/VectorGeometryToolVectorVelocityAcceleration>
     VectorGeometryToolWellKnownAxes<analysis_workbench/VectorGeometryToolWellKnownAxes>
     VectorGeometryToolWellKnownEarthAxes<analysis_workbench/VectorGeometryToolWellKnownEarthAxes>
     VectorGeometryToolWellKnownEarthSystems<analysis_workbench/VectorGeometryToolWellKnownEarthSystems>
     VectorGeometryToolWellKnownSunAxes<analysis_workbench/VectorGeometryToolWellKnownSunAxes>
     VectorGeometryToolWellKnownSunSystems<analysis_workbench/VectorGeometryToolWellKnownSunSystems>
     VectorGeometryToolWellKnownSystems<analysis_workbench/VectorGeometryToolWellKnownSystems>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ AberrationModelType<analysis_workbench/AberrationModelType>
    ≔ AngleToLocationType<analysis_workbench/AngleToLocationType>
    ≔ AngleType<analysis_workbench/AngleType>
    ≔ AsymptoteDirectionType<analysis_workbench/AsymptoteDirectionType>
    ≔ AxesType<analysis_workbench/AxesType>
    ≔ CalculationScalarType<analysis_workbench/CalculationScalarType>
    ≔ ClockHostType<analysis_workbench/ClockHostType>
    ≔ ConditionCombinedOperationType<analysis_workbench/ConditionCombinedOperationType>
    ≔ ConditionSetType<analysis_workbench/ConditionSetType>
    ≔ ConditionThresholdType<analysis_workbench/ConditionThresholdType>
    ≔ ConditionType<analysis_workbench/ConditionType>
    ≔ DistanceToLocationType<analysis_workbench/DistanceToLocationType>
    ≔ EventArrayFilterType<analysis_workbench/EventArrayFilterType>
    ≔ EventArrayType<analysis_workbench/EventArrayType>
    ≔ EventIntervalCollectionType<analysis_workbench/EventIntervalCollectionType>
    ≔ EventIntervalListType<analysis_workbench/EventIntervalListType>
    ≔ EventIntervalType<analysis_workbench/EventIntervalType>
    ≔ EventListMergeOperation<analysis_workbench/EventListMergeOperation>
    ≔ ExtremumType<analysis_workbench/ExtremumType>
    ≔ FileInterpolatorType<analysis_workbench/FileInterpolatorType>
    ≔ GridValuesMethodType<analysis_workbench/GridValuesMethodType>
    ≔ InheritDimensionType<analysis_workbench/InheritDimensionType>
    ≔ IntegrationWindowType<analysis_workbench/IntegrationWindowType>
    ≔ InterpolationMethodType<analysis_workbench/InterpolationMethodType>
    ≔ IntersectionSurfaceType<analysis_workbench/IntersectionSurfaceType>
    ≔ IntervalDurationType<analysis_workbench/IntervalDurationType>
    ≔ IntervalFromIntervalListSelectionType<analysis_workbench/IntervalFromIntervalListSelectionType>
    ≔ IntervalPruneFilterType<analysis_workbench/IntervalPruneFilterType>
    ≔ LagrangeLibrationPointType<analysis_workbench/LagrangeLibrationPointType>
    ≔ LightingConditionsType<analysis_workbench/LightingConditionsType>
    ≔ MeanElementTheory<analysis_workbench/MeanElementTheory>
    ≔ ParameterSetType<analysis_workbench/ParameterSetType>
    ≔ PlaneQuadrantType<analysis_workbench/PlaneQuadrantType>
    ≔ PlaneType<analysis_workbench/PlaneType>
    ≔ PointBPlaneType<analysis_workbench/PointBPlaneType>
    ≔ PointType<analysis_workbench/PointType>
    ≔ PrincipalAxisOfRotationType<analysis_workbench/PrincipalAxisOfRotationType>
    ≔ QuadratureType<analysis_workbench/QuadratureType>
    ≔ RangeSpeedType<analysis_workbench/RangeSpeedType>
    ≔ ResultVectorRequestType<analysis_workbench/ResultVectorRequestType>
    ≔ RotationSweepModeType<analysis_workbench/RotationSweepModeType>
    ≔ SampleReferenceTimeType<analysis_workbench/SampleReferenceTimeType>
    ≔ SatisfactionCrossing<analysis_workbench/SatisfactionCrossing>
    ≔ SaveDataType<analysis_workbench/SaveDataType>
    ≔ SignalDirectionType<analysis_workbench/SignalDirectionType>
    ≔ SignalPathReferenceSystem<analysis_workbench/SignalPathReferenceSystem>
    ≔ SignedAngleType<analysis_workbench/SignedAngleType>
    ≔ SmartEpochState<analysis_workbench/SmartEpochState>
    ≔ SmartIntervalState<analysis_workbench/SmartIntervalState>
    ≔ SpatialCalculationAltitudeReferenceType<analysis_workbench/SpatialCalculationAltitudeReferenceType>
    ≔ SpatialCalculationType<analysis_workbench/SpatialCalculationType>
    ≔ SpatialConditionOverTypeDurationType<analysis_workbench/SpatialConditionOverTypeDurationType>
    ≔ SpeedType<analysis_workbench/SpeedType>
    ≔ StartStopType<analysis_workbench/StartStopType>
    ≔ SurfaceReferenceShapeType<analysis_workbench/SurfaceReferenceShapeType>
    ≔ SurfaceShapeType<analysis_workbench/SurfaceShapeType>
    ≔ SystemType<analysis_workbench/SystemType>
    ≔ ThresholdConvergenceSenseType<analysis_workbench/ThresholdConvergenceSenseType>
    ≔ TimeEventType<analysis_workbench/TimeEventType>
    ≔ TimeSenseType<analysis_workbench/TimeSenseType>
    ≔ TrajectoryAxesCoordinatesType<analysis_workbench/TrajectoryAxesCoordinatesType>
    ≔ VectorComponentType<analysis_workbench/VectorComponentType>
    ≔ VectorGeometryToolComponentType<analysis_workbench/VectorGeometryToolComponentType>
    ≔ VectorGeometryToolSamplingMethod<analysis_workbench/VectorGeometryToolSamplingMethod>
    ≔ VectorGeometryToolScaledVectorDimensionInheritanceOptionType<analysis_workbench/VectorGeometryToolScaledVectorDimensionInheritanceOptionType>
    ≔ VectorType<analysis_workbench/VectorType>
    ≔ VolumeCombinedOperationType<analysis_workbench/VolumeCombinedOperationType>
    ≔ VolumeFromGridEdgeType<analysis_workbench/VolumeFromGridEdgeType>
    ≔ VolumeGridType<analysis_workbench/VolumeGridType>
    ≔ VolumeSatisfactionAccumulationType<analysis_workbench/VolumeSatisfactionAccumulationType>
    ≔ VolumeSatisfactionDurationType<analysis_workbench/VolumeSatisfactionDurationType>
    ≔ VolumeSatisfactionFilterType<analysis_workbench/VolumeSatisfactionFilterType>
    ≔ VolumeSatisfactionMetricType<analysis_workbench/VolumeSatisfactionMetricType>
    ≔ VolumeType<analysis_workbench/VolumeType>

