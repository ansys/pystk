
The ``AgStkGatorLib`` module
============================


.. py::module:: ansys.stk.core.stkobjects.astrogator


Summary
-------

.. tab-set::
    .. tab-items:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~IUserVariableDefinitionCollection`
              - The list of User Variables accessed through the Driver.

            * - :pyclass:`~IUserVariableCollection`
              - The list of User Variables accessed through a segment that sets initial conditions.

            * - :pyclass:`~IUserVariableUpdateCollection`
              - The list of User Variables accessed through an Update segment.

            * - :pyclass:`~ICalculationGraphCollection`
              - The list of Calculations Graphs to display.

            * - :pyclass:`~IConstraintCollection`
              - The list of constraints assigned to a stopping condition.

            * - :pyclass:`~IPluginProperties`
              - Properties of a plugin attitude control.

            * - :pyclass:`~ISNOPTControlCollection`
              - Properties for the list of SNOPT control parameters.

            * - :pyclass:`~ISNOPTResultCollection`
              - SNOPT result collection.

            * - :pyclass:`~IIPOPTControlCollection`
              - Properties for the list of IPOPT control parameters.

            * - :pyclass:`~IIPOPTResultCollection`
              - IPOPT result collection.

            * - :pyclass:`~IManeuverOptimalFiniteSNOPTOptimizer`
              - Properties of SNOPT Optimizer options for optimal finite maneuver.

            * - :pyclass:`~IManeuverOptimalFiniteInitialBoundaryConditions`
              - Properties of initial boundary conditions for optimal finite maneuver.

            * - :pyclass:`~IManeuverOptimalFiniteFinalBoundaryConditions`
              - Properties of final boundary conditions for optimal finite maneuver.

            * - :pyclass:`~IManeuverOptimalFinitePathBoundaryConditions`
              - Properties of path boundary conditions for optimal finite maneuver.

            * - :pyclass:`~IManeuverOptimalFiniteSteeringNodeCollection`
              - Steering/nodes collection.

            * - :pyclass:`~IManeuverOptimalFiniteBounds`
              - The bounds for boundary interfaces.

            * - :pyclass:`~IGoldenSectionControlCollection`
              - Properties for the list of Golden Section control parameters.

            * - :pyclass:`~IGoldenSectionControl`
              - Properties for control parameters of a Golden Section profile.

            * - :pyclass:`~IGoldenSectionResultCollection`
              - Properties for the list of Golden Section result parameters.

            * - :pyclass:`~IGoldenSectionResult`
              - Properties for result parameters of a Golden Section profile.

            * - :pyclass:`~IGridSearchControlCollection`
              - Properties for the list of Grid Search control parameters.

            * - :pyclass:`~IGridSearchControl`
              - Properties for control parameters of a Grid Search profile.

            * - :pyclass:`~IGridSearchResultCollection`
              - Properties for the list of Grid Search result parameters.

            * - :pyclass:`~IGridSearchResult`
              - Properties for result parameters of a Grid Search profile.

            * - :pyclass:`~IBisectionControlCollection`
              - Properties for the list of Bisection control parameters.

            * - :pyclass:`~IBisectionResult`
              - Properties for result parameters of a Bisection profile.

            * - :pyclass:`~IBisectionResultCollection`
              - Bisection result collection.

            * - :pyclass:`~IStoppingConditionElement`
              - The status of a stopping condition.

            * - :pyclass:`~IStoppingConditionCollection`
              - The list of Stopping Conditions.

            * - :pyclass:`~IMissionControlSequenceSegmentCollection`
              - Properties for a collection of segments.

            * - :pyclass:`~IState`
              - Spacecraft Parameters properties for the spacecraft configuration.

            * - :pyclass:`~IStoppingConditionComponent`
              - Properties for a stopping condition.

            * - :pyclass:`~IAutomaticSequence`
              - Properties for automatic sequences.

            * - :pyclass:`~IAutomaticSequenceCollection`
              - Properties for the Automatic Sequence Browser.

            * - :pyclass:`~IBPlaneCollection`
              - Properties for the collection of B-Planes.

            * - :pyclass:`~ICalcObjectCollection`
              - Collection of calculation objects.

            * - :pyclass:`~IManeuverFinitePropagator`
              - Properties for the propagation of a Finite Maneuver.

            * - :pyclass:`~IBurnoutVelocity`
              - Properties for the burnout velocity of a Launch segment.

            * - :pyclass:`~IAttitudeControl`
              - Properties for attitude options for a maneuver segment.

            * - :pyclass:`~IAttitudeControlFinite`
              - The attitude control of a finite maneuver.

            * - :pyclass:`~IAttitudeControlImpulsive`
              - The attitude control of an impulsive maneuver.

            * - :pyclass:`~IAttitudeControlOptimalFinite`
              - The attitude control of a optimal finite maneuver.

            * - :pyclass:`~IManeuver`
              - Properties of an Impulsive Maneuver Segment.

            * - :pyclass:`~IDisplaySystem`
              - The launch coordinate system.

            * - :pyclass:`~IBurnout`
              - The burnout point reference frame.

            * - :pyclass:`~IScriptingSegment`
              - Object properties for scripting options.

            * - :pyclass:`~IScriptingSegmentCollection`
              - The list of object properties that the script can interact with.

            * - :pyclass:`~IScriptingParameterEnumerationChoice`
              - Enumeration choice.

            * - :pyclass:`~IScriptingParameterEnumerationChoiceCollection`
              - The list of enumeration choices available when parameter type is Enumeration.

            * - :pyclass:`~IScriptingParameter`
              - Parameter properties for scripting options.

            * - :pyclass:`~IScriptingParameterCollection`
              - The list of parameters that the script can interact with.

            * - :pyclass:`~IScriptingCalcObject`
              - Calc Object properties for scripting options.

            * - :pyclass:`~IScriptingCalcObjectCollection`
              - The list of calc objects that the script can interact with.

            * - :pyclass:`~IScriptingTool`
              - Properties for the Scripting Tool.

            * - :pyclass:`~IElement`
              - The elements of the selected coordinate type.

            * - :pyclass:`~ISpacecraftParameters`
              - Properties for spacecraft configuration.

            * - :pyclass:`~IFuelTank`
              - Properties for fuel tank configuration.

            * - :pyclass:`~IMissionControlSequenceSegmentProperties`
              - The segment properties.

            * - :pyclass:`~IMissionControlSequenceEnd`
              - Properties for an End segment.

            * - :pyclass:`~IMissionControlSequenceInitialState`
              - Properties for an Initial State segment.

            * - :pyclass:`~IMissionControlSequenceSegment`
              - General properties for segments.

            * - :pyclass:`~IMissionControlSequenceOptions`
              - Properties for the MCS Options.

            * - :pyclass:`~IDriverMissionControlSequence`
              - Properties for the Mission Control Sequence.

            * - :pyclass:`~IElementCartesian`
              - Properties for Cartesian elements.

            * - :pyclass:`~IElementKeplerian`
              - Properties for Keplerian elements.

            * - :pyclass:`~IElementDelaunay`
              - Properties for Delaunay elements.

            * - :pyclass:`~IElementEquinoctial`
              - Properties for Equinoctial elements.

            * - :pyclass:`~IElementMixedSpherical`
              - Properties for Mixed Spherical elements.

            * - :pyclass:`~IElementSpherical`
              - Properties for Spherical elements.

            * - :pyclass:`~IElementTargetVectorIncomingAsymptote`
              - Properties for Target Vector Incoming Asymptote elements.

            * - :pyclass:`~IElementTargetVectorOutgoingAsymptote`
              - Properties for Target Vector Outgoing Asymptote elements.

            * - :pyclass:`~IElementGeodetic`
              - Properties for Geodetic elements.

            * - :pyclass:`~IElementBPlane`
              - Properties for BPlane elements.

            * - :pyclass:`~IElementSphericalRangeRate`
              - Properties for Spherical Range Rate elements.

            * - :pyclass:`~IStoppingCondition`
              - Basic properties for a stopping condition.

            * - :pyclass:`~ILightingStoppingCondition`
              - Properties for a lighting stopping condition.

            * - :pyclass:`~IAccessStoppingCondition`
              - Properties for an access stopping condition.

            * - :pyclass:`~IMissionControlSequencePropagate`
              - Properties for a Propagate segment.

            * - :pyclass:`~IMissionControlSequenceSequence`
              - Properties for a Sequence segment.

            * - :pyclass:`~IMissionControlSequenceBackwardSequence`
              - Properties for a Backward Sequence segment.

            * - :pyclass:`~IMissionControlSequenceLaunch`
              - Properties for a Launch segment.

            * - :pyclass:`~IDisplaySystemGeodetic`
              - Properties for a geodetic launch coordinate system.

            * - :pyclass:`~IDisplaySystemGeocentric`
              - Properties for a geocentric launch coordinate system.

            * - :pyclass:`~IBurnoutCBFCartesian`
              - Properties for a Cartesian CBF burnout state definition.

            * - :pyclass:`~IBurnoutGeodetic`
              - Properties for a geodetic burnout point definition.

            * - :pyclass:`~IBurnoutGeocentric`
              - {Properties for a geocentric burnout point definition.

            * - :pyclass:`~IBurnoutLaunchAzAltitude`
              - Properties for a launch azimuth / altitude burnout point definition.

            * - :pyclass:`~IBurnoutLaunchAzRadius`
              - Properties for a launch azimuth / radius burnout point definition.

            * - :pyclass:`~IMissionControlSequenceFollow`
              - Properties for a Follow segment.

            * - :pyclass:`~IMissionControlSequenceManeuver`
              - General properties for a Maneuver segment.

            * - :pyclass:`~IManeuverFinite`
              - Engine properties for a Finite Maneuver.

            * - :pyclass:`~IManeuverImpulsive`
              - Properties for an Impulsive Maneuver.

            * - :pyclass:`~IAttitudeControlImpulsiveVelocityVector`
              - Properties for the Velocity Vector attitude control for an Impulsive Maneuver.

            * - :pyclass:`~IAttitudeControlImpulsiveAntiVelocityVector`
              - Properties for the Anti-Velocity Vector attitude control for an Impulsive Maneuver.

            * - :pyclass:`~IAttitudeControlImpulsiveAttitude`
              - Properties for the Attitude attitude control for an Impulsive Maneuver.

            * - :pyclass:`~IAttitudeControlImpulsiveFile`
              - Properties for the File attitude control for an Impulsive Maneuver.

            * - :pyclass:`~IAttitudeControlImpulsiveThrustVector`
              - Properties for the Thrust Vector attitude control for an Impulsive Maneuver.

            * - :pyclass:`~IAttitudeControlFiniteAntiVelocityVector`
              - Properties for the Anti-Velocity Vector attitude control for a Finite Maneuver.

            * - :pyclass:`~IAttitudeControlFiniteAttitude`
              - Properties for the Attitude attitude control for a Finite Maneuver.

            * - :pyclass:`~IAttitudeControlFiniteFile`
              - Properties for the File attitude control for a Finite Maneuver.

            * - :pyclass:`~IAttitudeControlFiniteThrustVector`
              - Properties for the Thrust Vector attitude control for a Finite Maneuver.

            * - :pyclass:`~IAttitudeControlFiniteTimeVarying`
              - Properties for the Time Varying attitude control for a Finite Maneuver.

            * - :pyclass:`~IAttitudeControlFiniteVelocityVector`
              - Properties for the Velocity Vector attitude control for a Finite Maneuver.

            * - :pyclass:`~IAttitudeControlFinitePlugin`
              - Properties for the Plugin attitude control for a Finite Maneuver.

            * - :pyclass:`~IAttitudeControlOptimalFiniteLagrange`
              - Properties for the Lagrange Interpolation attitude control for a Optimal Finite Maneuver.

            * - :pyclass:`~IMissionControlSequenceHold`
              - Properties for a Hold segment.

            * - :pyclass:`~IMissionControlSequenceUpdate`
              - Properties for an Update segment.

            * - :pyclass:`~IMissionControlSequenceReturn`
              - Properties for a Return segment.

            * - :pyclass:`~IMissionControlSequenceStop`
              - Properties for a Stop segment.

            * - :pyclass:`~IProfile`
              - General properties for target sequence profiles.

            * - :pyclass:`~IProfileCollection`
              - Properties for a list of target sequence profiles.

            * - :pyclass:`~IMissionControlSequenceTargetSequence`
              - General properties of a TargetSequence segment.

            * - :pyclass:`~IDifferentialCorrectorControl`
              - Properties for control parameters of a differential corrector profile.

            * - :pyclass:`~IDifferentialCorrectorResult`
              - Properties for equality constraints of a differential corrector profile.

            * - :pyclass:`~ISearchPluginControl`
              - Properties of search plugin control parameters.

            * - :pyclass:`~ISearchPluginResult`
              - Properties of search plugin equality constraints.

            * - :pyclass:`~ISearchPluginResultCollection`
              - Properties for the list of search plugin equality constraints.

            * - :pyclass:`~ISearchPluginControlCollection`
              - Properties for the list of search plugin control parameters.

            * - :pyclass:`~IDifferentialCorrectorControlCollection`
              - Properties for the list of control parameters for a differential corrector profile.

            * - :pyclass:`~IDifferentialCorrectorResultCollection`
              - Differential Corrector result collection.

            * - :pyclass:`~ITargeterGraphActiveControl`
              - Properties for targeter graph active control.

            * - :pyclass:`~ITargeterGraphResult`
              - Properties for targeter graph result.

            * - :pyclass:`~ITargeterGraphActiveControlCollection`
              - Targeter graph active controls.

            * - :pyclass:`~ITargeterGraphResultCollection`
              - Targeter graph results.

            * - :pyclass:`~ITargeterGraph`
              - Properties for a Targeter Graph.

            * - :pyclass:`~ITargeterGraphCollection`
              - The list of User Variables accessed through the Driver.

            * - :pyclass:`~IProfileSearchPlugin`
              - Properties of a plugin search profile.

            * - :pyclass:`~IProfileDifferentialCorrector`
              - Properties for a Differential Corrector profile.

            * - :pyclass:`~IProfileChangeManeuverType`
              - Properties for a Change Maneuver Type profile.

            * - :pyclass:`~IProfileScriptingTool`
              - Properties for a Scripting Tool profile.

            * - :pyclass:`~IProfileChangeReturnSegment`
              - Properties for a Change Return Segment profile.

            * - :pyclass:`~IProfileChangePropagator`
              - Properties for a Change Propagator profile.

            * - :pyclass:`~IProfileChangeStopSegment`
              - Properties for a Change Stop Segment profile.

            * - :pyclass:`~IProfileChangeStoppingConditionState`
              - Properties for a Change Stopping Condition State profile.

            * - :pyclass:`~IProfileSeedFiniteManeuver`
              - Properties for a Seed Finite Maneuver segment.

            * - :pyclass:`~IProfileRunOnce`
              - Properties for a Run Once profile.

            * - :pyclass:`~IUserVariableDefinition`
              - Properties for a User Variable definition.

            * - :pyclass:`~IUserVariable`
              - The properties for a User Variable initial value.

            * - :pyclass:`~IUserVariableUpdate`
              - Properties for a User Variable update.

            * - :pyclass:`~IProfileSNOPTOptimizer`
              - Properties of SNOPT Optimizer profile.

            * - :pyclass:`~ISNOPTControl`
              - Properties for control parameters of a SNOPT profile.

            * - :pyclass:`~ISNOPTResult`
              - Properties for objecvtive and constraints of a SNOPT profile.

            * - :pyclass:`~IProfileIPOPTOptimizer`
              - Properties of IPOPT Optimizer profile.

            * - :pyclass:`~IIPOPTControl`
              - Properties for control parameters of a IPOPT profile.

            * - :pyclass:`~IIPOPTResult`
              - Properties for objecvtive and constraints of a IPOPT profile.

            * - :pyclass:`~IManeuverOptimalFinite`
              - Engine properties for a Optimal Finite Maneuver.

            * - :pyclass:`~IManeuverOptimalFiniteSteeringNodeElement`
              - The elements of the steering node.

            * - :pyclass:`~IProfileLambertProfile`
              - Properties for a Lambert profile.

            * - :pyclass:`~IProfileLambertSearchProfile`
              - Properties for a Lambert Search Profile.

            * - :pyclass:`~IProfileGoldenSection`
              - Properties for a Golden Section profile.

            * - :pyclass:`~IProfileGridSearch`
              - Properties for a Grid Search profile.

            * - :pyclass:`~ICalcObjectLinkEmbedControlCollection`
              - Collection of link/embed calculation objects.

            * - :pyclass:`~IProfileBisection`
              - Properties of Single Parameter Bisection profile.

            * - :pyclass:`~IBisectionControl`
              - Properties for control parameters of a Bisection Search profile.

            * - :pyclass:`~IStateCalcHeightAboveTerrain`
              - Interface for StateCalcHeightAboveTerrain.

            * - :pyclass:`~IStateCalcEpoch`
              - Properties for an Epoch calculation object.

            * - :pyclass:`~IStateCalcOrbitDelaunayG`
              - Interface for AsStateCalcOrbitDelaunayG.

            * - :pyclass:`~IStateCalcOrbitDelaunayH`
              - Interface for AsStateCalcOrbitDelaunayH.

            * - :pyclass:`~IStateCalcOrbitDelaunayL`
              - Interface for AsStateCalcOrbitDelaunayL.

            * - :pyclass:`~IStateCalcOrbitSemiLatusRectum`
              - Interface for AsStateCalcOrbitSemiLatusRectum.

            * - :pyclass:`~IStateCalcJacobiConstant`
              - Properties for a Jacobi Constant calculation object.

            * - :pyclass:`~IStateCalcJacobiOsculating`
              - Properties for an osculating Jacobi integral calculation object.

            * - :pyclass:`~IStateCalcCartesianElem`
              - Properties for a Cartesian Element calculation object.

            * - :pyclass:`~IStateCalcCartSTMElem`
              - Properties for a Cartesian STM Element calculation object.

            * - :pyclass:`~IStateCalcSTMEigenval`
              - Properties for an STM Eigenvalue calculation object.

            * - :pyclass:`~IStateCalcSTMEigenvecElem`
              - Properties for an STM Eigenvector element calculation object.

            * - :pyclass:`~IStateCalcEnvironment`
              - Properties for an Environment calculation object.

            * - :pyclass:`~IStateCalcEquinoctialElem`
              - Properties for an Equinoctial Element calculation object.

            * - :pyclass:`~IStateCalcDamageFlux`
              - Interface for AgAsStateCalcDamageFlux.

            * - :pyclass:`~IStateCalcDamageMassFlux`
              - Interface for AgAsStateCalcDamageMassFlux.

            * - :pyclass:`~IStateCalcMagnitudeFieldDipoleL`
              - Interface for AgAsStateCalcMagFieldDipoleL.

            * - :pyclass:`~IStateCalcSEETMagnitudeFieldFieldLineSepAngle`
              - Properties for a SEETMagFieldFieldLineSepAngle calculation object.

            * - :pyclass:`~IStateCalcImpactFlux`
              - Interface for AgAsStateCalcImpactFlux.

            * - :pyclass:`~IStateCalcImpactMassFlux`
              - Interface for AgAsStateCalcImpactMassFlux.

            * - :pyclass:`~IStateCalcSEETSAAFlux`
              - Interface for AgAsStateCalcSEETSAAFlux.

            * - :pyclass:`~IStateCalcSEETVehTemp`
              - Interface for AgAsStateCalcSEETVehTemp.

            * - :pyclass:`~IStateCalcCloseApproachBearing`
              - Properties for a CloseApproachBearing calculation object.

            * - :pyclass:`~IStateCalcCloseApproachMagnitude`
              - Properties for a CloseApproachMagnitude calculation object.

            * - :pyclass:`~IStateCalcCloseApproachTheta`
              - Properties for a CloseApproachTheta calculation object.

            * - :pyclass:`~IStateCalcCloseApproachX`
              - Properties for a CloseApproachX calculation object.

            * - :pyclass:`~IStateCalcCloseApproachY`
              - Properties for a CloseApproachY calculation object.

            * - :pyclass:`~IStateCalcCloseApproachCosBearing`
              - Properties for a CosineOfCloseApproachBearing calculation object.

            * - :pyclass:`~IStateCalcRelGroundTrackError`
              - Properties for a RelGroundTrackError calculation object.

            * - :pyclass:`~IStateCalcRelAtAOLMaster`
              - Properties for a RelativeAtAOL calculation object.

            * - :pyclass:`~IStateCalcDeltaFromMaster`
              - Properties for a Rel Mean Mean Anomaly calculation object.

            * - :pyclass:`~IStateCalcLonDriftRate`
              - Properties for a Longitude Drift Rate calculation object.

            * - :pyclass:`~IStateCalcMeanEarthLon`
              - Properties for a Mean Earth Longitude calculation object.

            * - :pyclass:`~IStateCalcRectifiedLon`
              - Properties for a RectifiedLon calculation object.

            * - :pyclass:`~IStateCalcTrueLongitude`
              - Properties for a TrueLongitude calculation object.

            * - :pyclass:`~IStateCalcGeodeticTrueLongitude`
              - Properties for a GeodeticTrueLongitude calculation object.

            * - :pyclass:`~IStateCalcGeodeticTrueLongitudeAtTimeOfPerigee`
              - Properties for a GeodeticTrueLongitudeAtTimeOfPerigee calculation object.

            * - :pyclass:`~IStateCalcMeanRightAscension`
              - Properties for a MeanRightAscension calculation object.

            * - :pyclass:`~IStateCalcGeodeticMeanRightAscension`
              - Properties for a GeodeticMeanRightAscension calculation object.

            * - :pyclass:`~IStateCalcTwoBodyDriftRate`
              - Properties for a TwoBodyDriftRate calculation object.

            * - :pyclass:`~IStateCalcDriftRateFactor`
              - Properties for a DriftRateFactor calculation object.

            * - :pyclass:`~IStateCalcEccentricityX`
              - Properties for a EccentricityX calculation object.

            * - :pyclass:`~IStateCalcEccentricityY`
              - Properties for a EccentricityY calculation object.

            * - :pyclass:`~IStateCalcInclinationX`
              - Properties for a InclinationX calculation object.

            * - :pyclass:`~IStateCalcInclinationY`
              - Properties for a InclinationY calculation object.

            * - :pyclass:`~IStateCalcUnitAngularMomentumX`
              - Properties for a UnitAngularMomentumX calculation object.

            * - :pyclass:`~IStateCalcUnitAngularMomentumY`
              - Properties for a UnitAngularMomentumY calculation object.

            * - :pyclass:`~IStateCalcUnitAngularMomentumZ`
              - Properties for a UnitAngularMomentumZ calculation object.

            * - :pyclass:`~IStateCalcGeodeticElem`
              - Properties for a Geodetic Element calculation object.

            * - :pyclass:`~IStateCalcRepeatingGroundTrackErr`
              - Properties for a RepeatingGroundTrackEquatorError calculation object.

            * - :pyclass:`~IStateCalcAltitudeOfApoapsis`
              - Properties for an Altitude of Apoapsis calculation object.

            * - :pyclass:`~IStateCalcAltitudeOfPeriapsis`
              - Properties for an Altitude Of Periapsis calculation object.

            * - :pyclass:`~IStateCalcArgOfLat`
              - Properties for an Argument of Latitude calculation object.

            * - :pyclass:`~IStateCalcArgOfPeriapsis`
              - Properties for an Argument of Periapsis calculation object.

            * - :pyclass:`~IStateCalcEccentricityAnomaly`
              - Properties for an Eccentric Anomaly calculation object.

            * - :pyclass:`~IStateCalcEccentricity`
              - Properties for an Eccentricity calculation object.

            * - :pyclass:`~IStateCalcInclination`
              - Properties for an Inclination calculation object.

            * - :pyclass:`~IStateCalcLonOfAscNode`
              - Properties for a Longitude of Ascending Node calculation object.

            * - :pyclass:`~IStateCalcMeanAnomaly`
              - Properties for a MeanAnomaly calculation object.

            * - :pyclass:`~IStateCalcMeanMotion`
              - Properties for a Mean Motion calculation object.

            * - :pyclass:`~IStateCalcOrbitPeriod`
              - Properties for an Orbit Period calculation object.

            * - :pyclass:`~IStateCalcNumRevs`
              - Properties for a Number of Revolutions calculation object.

            * - :pyclass:`~IStateCalcRAAN`
              - Properties for a RAAN calculation object.

            * - :pyclass:`~IStateCalcRadOfApoapsis`
              - Properties for a Radius Of Apoapsis calculation object.

            * - :pyclass:`~IStateCalcRadOfPeriapsis`
              - Properties for a Radius Of Periapsis calculation object.

            * - :pyclass:`~IStateCalcSemiMajorAxis`
              - Properties for a Semimajor Axis calculation object.

            * - :pyclass:`~IStateCalcTimePastAscNode`
              - Properties for a Time Past Ascending Node calculation object.

            * - :pyclass:`~IStateCalcTimePastPeriapsis`
              - Properties for a Time Past Periapsis calculation object.

            * - :pyclass:`~IStateCalcDeltaV`
              - Properties for a DeltaV calculation object.

            * - :pyclass:`~IStateCalcDeltaVSquared`
              - Properties for a DeltaV Squared calculation object.

            * - :pyclass:`~IStateCalcMissionControlSequenceDeltaV`
              - Properties for a MCS DeltaV calculation object.

            * - :pyclass:`~IStateCalcMissionControlSequenceDeltaVSquared`
              - Properties for a MCS DeltaV Squared calculation object.

            * - :pyclass:`~IStateCalcSequenceDeltaV`
              - Properties for a Sequence DeltaV calculation object.

            * - :pyclass:`~IStateCalcSequenceDeltaVSquared`
              - Properties for a Sequence DeltaV Squared calculation object.

            * - :pyclass:`~IStateCalcFuelMass`
              - Properties for a FuelMass calculation object.

            * - :pyclass:`~IStateCalcDensity`
              - Properties for a Fuel Density calculation object.

            * - :pyclass:`~IStateCalcInertialDeltaVMagnitude`
              - Properties for an Inertial DeltaV Magnitude calculation object.

            * - :pyclass:`~IStateCalcInertialDeltaVx`
              - Properties for an Inertial DeltaVx calculation object.

            * - :pyclass:`~IStateCalcInertialDeltaVy`
              - Properties for an Inertial DeltaVy calculation object.

            * - :pyclass:`~IStateCalcInertialDeltaVz`
              - Properties for an Inertial DeltaVz calculation object.

            * - :pyclass:`~IStateCalcManeuverSpecificImpulse`
              - Properties for a Specific Impulse calculation object.

            * - :pyclass:`~IStateCalcPressure`
              - Properties for a Tank Pressure calculation object.

            * - :pyclass:`~IStateCalcTemperature`
              - Properties for a Tank Temperature calculation object.

            * - :pyclass:`~IStateCalcVectorX`
              - Properties for a Vector X calculation object.

            * - :pyclass:`~IStateCalcVectorY`
              - Properties for a Vector Y calculation object.

            * - :pyclass:`~IStateCalcVectorZ`
              - Properties for a Vector Z calculation object.

            * - :pyclass:`~IStateCalcMass`
              - Properties for a Total Mass calculation object.

            * - :pyclass:`~IStateCalcManeuverTotalMassFlowRate`
              - Properties for a Total Mass Flow Rate calculation object.

            * - :pyclass:`~IStateCalcAbsoluteValue`
              - Properties for an Absolute Value calculation object.

            * - :pyclass:`~IStateCalcDifference`
              - Properties for a Difference calculation object.

            * - :pyclass:`~IStateCalcDifferenceOtherSegment`
              - Properties for a Difference Across Segments calculation object.

            * - :pyclass:`~IStateCalcPositionDifferenceOtherSegment`
              - Properties for a Position Difference Across Segments calculation object.

            * - :pyclass:`~IStateCalcVelDifferenceOtherSegment`
              - Properties for a Velocity Difference Across Segments calculation object.

            * - :pyclass:`~IStateCalcPositionVelDifferenceOtherSegment`
              - Properties for a Position and Velocity Difference Across Segments calculation object.

            * - :pyclass:`~IStateCalcValueAtSegment`
              - Properties for a Value At Segment calculation object.

            * - :pyclass:`~IStateCalcMaxValue`
              - Properties for a Maximum Value calculation object.

            * - :pyclass:`~IStateCalcMinValue`
              - Properties for a Minimum Value calculation object.

            * - :pyclass:`~IStateCalcMeanValue`
              - Properties for a Mean Value calculation object.

            * - :pyclass:`~IStateCalcMedianValue`
              - Properties for a Median Value calculation object.

            * - :pyclass:`~IStateCalcStandardDeviation`
              - Properties for a Standard Deviation calculation object.

            * - :pyclass:`~IStateCalcNegative`
              - Properties for a Negative calculation object.

            * - :pyclass:`~IStateCalcTrueAnomaly`
              - Properties for a Mean True Anomaly calculation object.

            * - :pyclass:`~IBDotRCalc`
              - Properties for a BDotR calculation object.

            * - :pyclass:`~IBDotTCalc`
              - Properties for a BDotT calculation object.

            * - :pyclass:`~IBMagnitudeCalc`
              - Properties for a BMagnitude calculation object.

            * - :pyclass:`~IBThetaCalc`
              - Properties for a BTheta calculation object.

            * - :pyclass:`~IStateCalcDeltaDec`
              - Properties for a Delta Declination calculation object.

            * - :pyclass:`~IStateCalcDeltaRA`
              - Properties for a Delta Right Asc calculation object.

            * - :pyclass:`~IStateCalcBetaAngle`
              - Properties for a Beta Angle calculation object.

            * - :pyclass:`~IStateCalcLocalApparentSolarLon`
              - Properties for a Local Apparent Solar Longitude calculation object.

            * - :pyclass:`~IStateCalcLonOfPeriapsis`
              - Properties for a Longitude of Periapsis calculation object.

            * - :pyclass:`~IStateCalcOrbitStateValue`
              - Properties for an Orbit State Value calculation object.

            * - :pyclass:`~IStateCalcSignedEccentricity`
              - Properties for a SignedEccentricity calculation object.

            * - :pyclass:`~IStateCalcTrueLon`
              - Properties for a True Longitude calculation object.

            * - :pyclass:`~IStateCalcPower`
              - Properties for a Power calculation object.

            * - :pyclass:`~IStateCalcRelMotion`
              - Properties for a Relative Motion calculation object.

            * - :pyclass:`~IStateCalcSolarBetaAngle`
              - Properties for a Solar Beta Angle calculation object.

            * - :pyclass:`~IStateCalcSolarInPlaneAngle`
              - Properties for a Solar In Plane Angle calculation object.

            * - :pyclass:`~IStateCalcRelPositionDecAngle`
              - Properties for a Relative Position Declination Angle calculation object.

            * - :pyclass:`~IStateCalcRelPositionInPlaneAngle`
              - Properties for a Relative Position In Plane Angle calculation object.

            * - :pyclass:`~IStateCalcRelativeInclination`
              - Properties for a Relative Inclination Angle calculation object.

            * - :pyclass:`~IStateCalcCurvilinearRelMotion`
              - Properties for Curvilinear Relative Motion  calculation object.

            * - :pyclass:`~IStateCalcCustomFunction`
              - Properties for a Custom Function calculation object.

            * - :pyclass:`~IStateCalcScript`
              - Properties for a Script calculation object.

            * - :pyclass:`~IStateCalcCd`
              - Properties for a Cd calculation object.

            * - :pyclass:`~IStateCalcCr`
              - Properties for a Cr calculation object.

            * - :pyclass:`~IStateCalcDragArea`
              - Properties for a DragArea calculation object. CAgAsStateCalcDragArea.

            * - :pyclass:`~IStateCalcRadiationPressureArea`
              - Properties for a RadPressureArea calculation object.

            * - :pyclass:`~IStateCalcRadiationPressureCoefficient`
              - Properties for a RadiationPressureCoefficient calculation object.

            * - :pyclass:`~IStateCalcSRPArea`
              - Properties for an SRPArea calculation object.

            * - :pyclass:`~IStateCalcCosOfVerticalFPA`
              - Properties for a Cosine of Vertical FPA calculation object.

            * - :pyclass:`~IStateCalcDec`
              - Properties for a Declination calculation object.

            * - :pyclass:`~IStateCalcFPA`
              - Properties for a Flight Path Angle calculation object.

            * - :pyclass:`~IStateCalcRMagnitude`
              - Properties for an R Mag calculation object. AsStateCalcRMag.

            * - :pyclass:`~IStateCalcRA`
              - Properties for a Right Asc calculation object.

            * - :pyclass:`~IStateCalcVMagnitude`
              - Properties for a V Mag calculation object.

            * - :pyclass:`~IStateCalcVelAz`
              - Properties for a Velocity Azimuth calculation object.

            * - :pyclass:`~IStateCalcC3Energy`
              - Properties for a C3 Energy calculation object.

            * - :pyclass:`~IStateCalcInAsympDec`
              - Properties for an Incoming Asymptote Dec calculation object.

            * - :pyclass:`~IStateCalcInAsympRA`
              - Properties for a Incoming Asymptote RA calculation object.

            * - :pyclass:`~IStateCalcInVelAzAtPeriapsis`
              - Properties for an Incoming Vel Az at Periapsis calculation object.

            * - :pyclass:`~IStateCalcOutAsympDec`
              - Properties for a Outgoing Asymptote Dec calculation object.

            * - :pyclass:`~IStateCalcOutAsympRA`
              - Properties for a Outgoing Asymptote RA calculation object.

            * - :pyclass:`~IStateCalcOutVelAzAtPeriapsis`
              - Properties for a Outgoing Vel Az at Periapsis calculation object.

            * - :pyclass:`~IStateCalcDuration`
              - Properties for a Duration calculation object.

            * - :pyclass:`~IStateCalcUserValue`
              - Interface for CAgAsStateCalcUserValue.

            * - :pyclass:`~IStateCalcVectorGeometryToolAngle`
              - Properties for an Vector Geometry Tool Angle calculation object.

            * - :pyclass:`~IStateCalcAngle`
              - Properties for an Angle Between Vectors calculation object.

            * - :pyclass:`~IStateCalcDotProduct`
              - Properties for a Dot Product calculation object.

            * - :pyclass:`~IStateCalcVectorDec`
              - Properties for a Vector Dec calculation object.

            * - :pyclass:`~IStateCalcVectorMagnitude`
              - Properties for a Vector Mag calculation object.

            * - :pyclass:`~IStateCalcVectorRA`
              - Properties for a Vector RA calculation object.

            * - :pyclass:`~IStateCalcOnePointAccess`
              - Properties for an Access calculation object.

            * - :pyclass:`~IStateCalcDifferenceAcrossSegmentsOtherSat`
              - Properties for a Difference Across Segments Across Satellites calculation object.

            * - :pyclass:`~IStateCalcValueAtSegmentOtherSat`
              - Properties for a Value At Segment Across Satellites calculation object.

            * - :pyclass:`~IStateCalcRARate`
              - Properties for a Right Ascension Rate calculation object.

            * - :pyclass:`~IStateCalcDecRate`
              - Properties for a Declination Rate calculation object.

            * - :pyclass:`~IStateCalcRangeRate`
              - Properties for a Range Rate calculation object.

            * - :pyclass:`~IStateCalcGravitationalParameter`
              - Properties for a Gravitational Parameter calculation object.

            * - :pyclass:`~IStateCalcReferenceRadius`
              - Properties for a Reference Radius calculation object.

            * - :pyclass:`~IStateCalcGravCoeff`
              - Properties for a gravity coefficient calculation object.

            * - :pyclass:`~IStateCalcSpeedOfLight`
              - Properties for a Speed of Light calculation object.

            * - :pyclass:`~IStateCalcPi`
              - Properties for a Pi calculation object.

            * - :pyclass:`~IStateCalcScalar`
              - Properties for a Scalar calculation object.

            * - :pyclass:`~IStateCalcApparentSolarTime`
              - Properties for an Apparent Solar Time calculation object.

            * - :pyclass:`~IStateCalcEarthMeanSolarTime`
              - Properties for an Earth Mean Solar Time calculation object.

            * - :pyclass:`~IStateCalcEarthMeanLocTimeAN`
              - Properties for an Earth Mean Local Time of Ascending Node calculation object.

            * - :pyclass:`~ICentralBodyCollection`
              - The list of central bodies.

            * - :pyclass:`~ICentralBodyEphemeris`
              - The central body ephemeris source.

            * - :pyclass:`~ICentralBodyGravityModel`
              - Properties for a central body gravity model.

            * - :pyclass:`~ICentralBodyShape`
              - The central body shape.

            * - :pyclass:`~ICentralBodyShapeSphere`
              - Properties for the central body sphere shape.

            * - :pyclass:`~ICentralBodyShapeOblateSpheroid`
              - Properties for the central body oblate spheroid shape.

            * - :pyclass:`~ICentralBodyShapeTriaxialEllipsoid`
              - Properties for the central body triaxial ellipsoid shape.

            * - :pyclass:`~ICentralBodyAttitude`
              - The central body attitude.

            * - :pyclass:`~ICentralBodyAttitudeRotationCoefficientsFile`
              - Properties for a rotation coefficients file attitude definition.

            * - :pyclass:`~ICentralBodyAttitudeIAU1994`
              - Properties for an IAU1994 attitude definition.

            * - :pyclass:`~ICentralBodyEphemerisAnalyticOrbit`
              - Properties for the Analytic Orbit ephemeris source.

            * - :pyclass:`~ICentralBodyEphemerisJPLSpice`
              - Properties for the JPL SPICE ephemeris source.

            * - :pyclass:`~ICentralBodyEphemerisFile`
              - Properties for the Ephemeris File ephemeris source.

            * - :pyclass:`~ICentralBodyEphemerisJPLDesignExplorerOptimizer`
              - Properties for the JPL DE ephemeris source.

            * - :pyclass:`~ICentralBodyEphemerisPlanetary`
              - Properties for the Planetary Ephemeris file ephemeris source.

            * - :pyclass:`~IAstrogatorCentralBody`
              - General properties for a central body.

            * - :pyclass:`~IPowerInternal`
              - Properties for the Internal Power power source component.

            * - :pyclass:`~IPowerProcessed`
              - Properties for the Processed Power power source component.

            * - :pyclass:`~IPowerSolarArray`
              - Properties for the Solar Array Power power source component.

            * - :pyclass:`~IGeneralRelativityFunction`
              - Properties for the General Relativity propagator function.

            * - :pyclass:`~IStateTransformationFunction`
              - Properties for the State Transition propagator function.

            * - :pyclass:`~ICR3BPFunc`
              - Properties for the CR3BP propagator function.

            * - :pyclass:`~IER3BPFunc`
              - Properties for the ER3BP propagator function.

            * - :pyclass:`~IRadiationPressureFunction`
              - Properties for the Radiation Pressure propagator function.

            * - :pyclass:`~IYarkovskyFunc`
              - Properties for the Yarkovsky Effect propagator function.

            * - :pyclass:`~IBlendedDensity`
              - Properties for the blended atmospheric density propagator function.

            * - :pyclass:`~IDragModelPlugin`
              - Properties for the Drag Model plugin.

            * - :pyclass:`~ICira72Function`
              - Properties for the CIRA 72 atmospheric model.

            * - :pyclass:`~IExponential`
              - Properties for the Exponential atmospheric model - a model that calculates atmospheric density using an equation involving a reference density, reference altitude, and scale altitude.

            * - :pyclass:`~IHarrisPriester`
              - Properties for the Harris-Priester atmospheric model - a model that takes into account a 10.7 cm solar flux level and diurnal bulge.

            * - :pyclass:`~IDensityModelPlugin`
              - Properties for the plugin atmospheric density model.

            * - :pyclass:`~IJacchiaRoberts`
              - Properties for the Jacchia-Roberts atmospheric model - a model that is similar to Jacchia 1971 but uses analytical methods to improve performance.

            * - :pyclass:`~IJacchiaBowman2008`
              - Properties for the Jacchia Bowman 2008 atmospheric density model.

            * - :pyclass:`~IJacchia_1960`
              - Properties for the Jacchia 1960 atmospheric model - an outdated atmospheric model provided for making comparisons with other software.

            * - :pyclass:`~IJacchia_1970`
              - Properties for the Jacchia 1970 atmospheric model - a model that computes atmospheric density based on the composition of the atmosphere, which depends on altitude as well as seasonal variation. Valid range is 100-2500 km.

            * - :pyclass:`~IJacchia_1971`
              - Properties for the Jacchia 1971 atmospheric model - a model that is similar to Jacchia 1970, with improved treatment of certain solar effects.

            * - :pyclass:`~IMSISE_1990`
              - Properties for the MSISE 1990 atmospheric model - an empirical density model developed by Hedin based on satellite data. Finds the total density by accounting for the contribution of N2, O, O2, He, Ar and H. 1990 version, valid range of 0-1000 km.

            * - :pyclass:`~IMSIS_1986`
              - Properties for the MSIS 1986 atmospheric model - an empirical density model developed by Hedin based on satellite data. Finds the total density by accounting for the contribution of N2, O, O2, He, Ar and H. 1986 version, valid range of 90-1000 km.

            * - :pyclass:`~INRLMSISE_2000`
              - Properties for the NRLMSISE 2000 atmospheric model.

            * - :pyclass:`~IUS_Standard_Atmosphere`
              - Properties for the US Standard Atmosphere atmospheric model.

            * - :pyclass:`~IMarsGRAM37`
              - Properties for the Mars-GRAM 3.7 atmospheric model.

            * - :pyclass:`~IMarsGRAM2005`
              - Properties for the Mars-GRAM 2005 atmospheric model.

            * - :pyclass:`~IVenusGRAM2005`
              - Properties for the Venus-GRAM 2005 atmospheric model.

            * - :pyclass:`~IMarsGRAM2010`
              - Properties for the Mars-GRAM 2010 atmospheric model.

            * - :pyclass:`~IMarsGRAM2001`
              - Properties for the Mars-GRAM 2001 atmospheric model.

            * - :pyclass:`~IMarsGRAM2000`
              - Properties for the Mars-GRAM 2000 atmospheric model.

            * - :pyclass:`~IDTM2012`
              - Properties for the DTM 2012 atmospheric model.

            * - :pyclass:`~IDTM2020`
              - Properties for the DTM 2020 atmospheric model.

            * - :pyclass:`~IGravityFieldFunction`
              - Properties for the Gravitational Force gravity model - a complex gravitational force calculation, optionally including solid and ocean tide effects.

            * - :pyclass:`~IPointMassFunction`
              - Properties for the Point Mass Function.

            * - :pyclass:`~ITwoBodyFunction`
              - Properties for the Two Body gravity model - a standard point mass model.

            * - :pyclass:`~IHPOPPluginFunction`
              - Properties for the HPOP Plugin propagator function.

            * - :pyclass:`~IEOMFuncPluginFunction`
              - Properties for the EOM Function Plugin propagator function.

            * - :pyclass:`~ISRPAeroT20`
              - Properties for the Aerospace T20 solar radiation pressure model for GPS block IIA.

            * - :pyclass:`~ISRPAeroT30`
              - Properties for the Aerospace T30 solar radiation pressure model for GPS block IIR.

            * - :pyclass:`~ISRPGSPM04aIIA`
              - Properties for the Bar-Sever GPS Solar Pressure Model 04a for block IIA.

            * - :pyclass:`~ISRPGSPM04aIIR`
              - Properties for the Bar-Sever GPS Solar Pressure Model 04a for block IIR.

            * - :pyclass:`~ISRPGSPM04aeIIA`
              - Properties for the Bar-Sever GPS Solar Pressure Model 04ae for block IIA.

            * - :pyclass:`~ISRPGSPM04aeIIR`
              - Properties for the Bar-Sever GPS Solar Pressure Model 04ae for block IIR.

            * - :pyclass:`~ISRPSpherical`
              - Properties for the Spherical SRP model; assumes a spherical spacecraft. The equation used by STK is described in the Solar Radiation technical note.

            * - :pyclass:`~ISRPNPlate`
              - Properties for the N-plate SRP model.

            * - :pyclass:`~ISRPTabAreaVec`
              - Properties for the tabulated area vector SRP model.

            * - :pyclass:`~ISRPVariableArea`
              - Properties for the Variable Area SRP model.

            * - :pyclass:`~IThirdBodyFunction`
              - Properties for a Third Body propagator function. The IAgComponentInfo object returned by the mode property can be cast to IAgVAGravityFieldFunction or IAgVAPointMassFunction depending on the selected ModeType.

            * - :pyclass:`~ISRPReflectionPlugin`
              - Properties for the plugin SRP Refelction.

            * - :pyclass:`~IEngineModelThrustCoefficients`
              - Thrust coefficient properties for engine definition.

            * - :pyclass:`~IEngineModelIspCoefficients`
              - Isp coefficient properties for engine definition.

            * - :pyclass:`~IEngineConstAcc`
              - Properties for a Constant Acceleration and Isp engine model.

            * - :pyclass:`~IEngineConstant`
              - Properties for a Constant Thrust and Isp engine model.

            * - :pyclass:`~IEngineDefinition`
              - Properties for engine definition for an Ion engine model.

            * - :pyclass:`~IEngineThrottleTable`
              - Properties for engine parameters for a Throttle Table engine model.

            * - :pyclass:`~IEngineIon`
              - Properties for engine parameters for an Ion engine model.

            * - :pyclass:`~IEngineCustom`
              - Properties for a Custom engine model.

            * - :pyclass:`~IEnginePlugin`
              - Properties for a Plugin engine model.

            * - :pyclass:`~IEngineModelPoly`
              - Properties for a Polynomial Thrust and Isp engine model.

            * - :pyclass:`~IDesignCR3BPObjectCollection`
              - The list of associated CR3BP objects.

            * - :pyclass:`~IDesignER3BPObjectCollection`
              - The list of associated ER3BP objects.

            * - :pyclass:`~IDesignCR3BPSetup`
              - Properties for the CR3BP Setup Tool.

            * - :pyclass:`~IDesignCR3BPObject`
              - Properties for individual associated CR3BP object.

            * - :pyclass:`~IDesignER3BPSetup`
              - Properties for the ER3BP Setup Tool.

            * - :pyclass:`~IDesignER3BPObject`
              - Properties for individual associated ER3BP object.

            * - :pyclass:`~IThruster`
              - Properties for individual thrusters.

            * - :pyclass:`~IThrusterSetCollection`
              - The list of thrusters in a thruster set.

            * - :pyclass:`~IThrusterSet`
              - The properties of a thruster set.

            * - :pyclass:`~IAsTriggerCondition`
              - Properties for a constraint - an additional condition to be met to satisfy a stopping condition.

            * - :pyclass:`~ICustomFunctionScriptEngine`
              - Properties for custom functions.

            * - :pyclass:`~INumericalIntegrator`
              - The type of numerical integrator to be used by the propagator.

            * - :pyclass:`~IPropagatorFunctionCollection`
              - The list of propagator functions - affecting forces that you want to model for orbit propagation.

            * - :pyclass:`~INumericalPropagatorWrapper`
              - General properties for propagators.

            * - :pyclass:`~INumericalPropagatorWrapperCR3BP`
              - General properties for three-body problem propagators.

            * - :pyclass:`~IBulirschStoerIntegrator`
              - Properties for the Bulirsch-Stoer numerical integrator.

            * - :pyclass:`~IGaussJacksonIntegrator`
              - Properties for the Gauss-Jackson numerical integrator.

            * - :pyclass:`~IRungeKutta2nd3rd`
              - Properties for the RK2nd3rd numerical integrator.

            * - :pyclass:`~IRungeKutta4th`
              - Properties for the RK4th numerical integrator.

            * - :pyclass:`~IRungeKutta4th5th`
              - Properties for the RK4th5th numerical integrator.

            * - :pyclass:`~IRungeKutta4thAdapt`
              - Properties for the RK4thAdapt numerical integrator.

            * - :pyclass:`~IRungeKuttaF7th8th`
              - Properties for the RK7th8th numerical integrator.

            * - :pyclass:`~IRungeKuttaV8th9th`
              - Properties for the RK8th9th numerical integrator.

    
    .. tab-items:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~DriverMissionControlSequence`
              - Basic properties of an Astrogator satellite.

            * - :pyclass:`~MissionControlSequenceSegmentCollection`
              - The Mission Control Sequence.

            * - :pyclass:`~MissionControlSequenceEnd`
              - The End segment.

            * - :pyclass:`~MissionControlSequenceInitialState`
              - The Initial State segment.

            * - :pyclass:`~SpacecraftParameters`
              - Spacecraft parameters.

            * - :pyclass:`~FuelTank`
              - Fuel Tank parameters.

            * - :pyclass:`~ElementCartesian`
              - Cartesian elements.

            * - :pyclass:`~ElementKeplerian`
              - Keplerian elements.

            * - :pyclass:`~ElementEquinoctial`
              - Equinoctial elements.

            * - :pyclass:`~ElementDelaunay`
              - Delaunay elements.

            * - :pyclass:`~ElementMixedSpherical`
              - Mixed Spherical elements.

            * - :pyclass:`~ElementSpherical`
              - Spherical elements.

            * - :pyclass:`~ElementTargetVectorIncomingAsymptote`
              - Target Vector Incoming Asymptote elements.

            * - :pyclass:`~ElementTargetVectorOutgoingAsymptote`
              - Target Vector Outgoing Asymptote elements.

            * - :pyclass:`~ElementGeodetic`
              - Geodetic elements.

            * - :pyclass:`~ElementBPlane`
              - Bplane elements.

            * - :pyclass:`~ElementSphericalRangeRate`
              - Spherical Range Rate elements.

            * - :pyclass:`~MissionControlSequencePropagate`
              - The Propagate segment.

            * - :pyclass:`~State`
              - The orbit state.

            * - :pyclass:`~StoppingConditionCollection`
              - The stopping conditions collection.

            * - :pyclass:`~AccessStoppingCondition`
              - The Access stopping condition.

            * - :pyclass:`~LightingStoppingCondition`
              - The Lighting stopping condition.

            * - :pyclass:`~StoppingCondition`
              - A stopping condition.

            * - :pyclass:`~StoppingConditionElement`
              - A stopping condition.

            * - :pyclass:`~MissionControlSequenceSequence`
              - The Sequence segment.

            * - :pyclass:`~MissionControlSequenceBackwardSequence`
              - The Backward Sequence segment.

            * - :pyclass:`~MissionControlSequenceLaunch`
              - The Launch segment.

            * - :pyclass:`~DisplaySystemGeodetic`
              - The geodetic launch location.

            * - :pyclass:`~DisplaySystemGeocentric`
              - The geocentric launch location.

            * - :pyclass:`~BurnoutGeodetic`
              - The geodetic burnout point.

            * - :pyclass:`~BurnoutCBFCartesian`
              - The burnout state in CBF Cartesian coordinates.

            * - :pyclass:`~BurnoutGeocentric`
              - The geocentric burnout point.

            * - :pyclass:`~BurnoutLaunchAzAltitude`
              - The launch azimuth and altitude burnout point.

            * - :pyclass:`~BurnoutLaunchAzRadius`
              - The launch azimuth and radius burnout point.

            * - :pyclass:`~BurnoutVelocity`
              - The burnout velocity.

            * - :pyclass:`~MissionControlSequenceFollow`
              - The Follow segment.

            * - :pyclass:`~MissionControlSequenceManeuver`
              - The Maneuver segment.

            * - :pyclass:`~ManeuverFinite`
              - The Finite Maneuver.

            * - :pyclass:`~ManeuverImpulsive`
              - The Impulsive Maneuver.

            * - :pyclass:`~AttitudeControlImpulsiveVelocityVector`
              - The velocity vector attitude control for an impulsive maneuver.

            * - :pyclass:`~AttitudeControlImpulsiveAntiVelocityVector`
              - The anti-velocity vector attitude control for an impulsive maneuver.

            * - :pyclass:`~AttitudeControlImpulsiveAttitude`
              - The attitude attitude control for an impulsive maneuver.

            * - :pyclass:`~AttitudeControlImpulsiveFile`
              - The file attitude control for an impulsive maneuver.

            * - :pyclass:`~AttitudeControlImpulsiveThrustVector`
              - The thrust vector attitude control for an impulsive maneuver.

            * - :pyclass:`~AttitudeControlFiniteAntiVelocityVector`
              - The anti-velocity vector attitude control for a finite maneuver.

            * - :pyclass:`~AttitudeControlFiniteAttitude`
              - The attitude attitude control for a finite maneuver.

            * - :pyclass:`~AttitudeControlFiniteFile`
              - The file attitude control for a finite maneuver.

            * - :pyclass:`~AttitudeControlFiniteThrustVector`
              - The thrust vector attitude control for a finite maneuver.

            * - :pyclass:`~AttitudeControlFiniteTimeVarying`
              - The time varying attitude control for a finite maneuver.

            * - :pyclass:`~AttitudeControlFiniteVelocityVector`
              - The velocity vector attitude control for a finite maneuver.

            * - :pyclass:`~AttitudeControlFinitePlugin`
              - The plugin attitude control for a finite maneuver.

            * - :pyclass:`~AttitudeControlOptimalFiniteLagrange`
              - The Lagrange Interpolation attitude control for a optimal finite maneuver.

            * - :pyclass:`~ManeuverFinitePropagator`
              - Propagation for a finite maneuver.

            * - :pyclass:`~MissionControlSequenceHold`
              - The Hold segment.

            * - :pyclass:`~MissionControlSequenceUpdate`
              - The Update segment.

            * - :pyclass:`~MissionControlSequenceReturn`
              - The Return segment.

            * - :pyclass:`~MissionControlSequenceStop`
              - The Stop segment.

            * - :pyclass:`~MissionControlSequenceTargetSequence`
              - The Target Sequence segment.

            * - :pyclass:`~ProfileCollection`
              - The Profiles of a Target Sequence.

            * - :pyclass:`~MissionControlSequenceOptions`
              - The MCS Options.

            * - :pyclass:`~CalcObjectCollection`
              - The Calculation Object component folder.

            * - :pyclass:`~ConstraintCollection`
              - The Constraint component folder.

            * - :pyclass:`~PluginProperties`
              - The plugin attitude control type.

            * - :pyclass:`~ProfileSearchPlugin`
              - The plugin search profile.

            * - :pyclass:`~TargeterGraph`
              - Targeter Graph.

            * - :pyclass:`~TargeterGraphCollection`
              - Targeter Graphs.

            * - :pyclass:`~TargeterGraphResultCollection`
              - Targeter Graph Result Collection.

            * - :pyclass:`~TargeterGraphActiveControlCollection`
              - Targeter Graph Active Control Collection.

            * - :pyclass:`~TargeterGraphActiveControl`
              - Targeter Graph Active Control.

            * - :pyclass:`~TargeterGraphResult`
              - Targeter Graph Result.

            * - :pyclass:`~ProfileDifferentialCorrector`
              - The Differential Corrector profile.

            * - :pyclass:`~ProfileScriptingTool`
              - The Scripting Tool profile.

            * - :pyclass:`~DifferentialCorrectorControl`
              - Control Parameters for a Target Sequence.

            * - :pyclass:`~DifferentialCorrectorResult`
              - Differential Corrector equality constraints.

            * - :pyclass:`~DifferentialCorrectorControlCollection`
              - The collection of Control Parameters for a differential corrector profile.

            * - :pyclass:`~DifferentialCorrectorResultCollection`
              - The collection of results for a differential corrector.

            * - :pyclass:`~SearchPluginControl`
              - Control parameters for a plugin search profile.

            * - :pyclass:`~SearchPluginControlCollection`
              - The list of search plugin control parameters.

            * - :pyclass:`~SearchPluginResult`
              - Equality constraints for a plugin search profile.

            * - :pyclass:`~SearchPluginResultCollection`
              - The list of search plugin equality constraints.

            * - :pyclass:`~ProfileChangeManeuverType`
              - The Change Maneuver Type profile.

            * - :pyclass:`~ProfileChangeReturnSegment`
              - The Change Return Segment profile.

            * - :pyclass:`~ProfileChangePropagator`
              - The Change Propagator profile.

            * - :pyclass:`~ProfileChangeStopSegment`
              - The Change Stop Segment profile.

            * - :pyclass:`~ProfileChangeStoppingConditionState`
              - The Change Stopping Condition State profile.

            * - :pyclass:`~ProfileSeedFiniteManeuver`
              - The Seed Finite Maneuver profile.

            * - :pyclass:`~ProfileRunOnce`
              - The Run Once profile.

            * - :pyclass:`~BPlaneCollection`
              - The collection of B-Planes.

            * - :pyclass:`~StateCalcDamageFlux`
              - CoClass StateCalcDamageFlux.

            * - :pyclass:`~StateCalcDamageMassFlux`
              - CoClass StateCalcDamageMassFlux.

            * - :pyclass:`~StateCalcMagnitudeFieldDipoleL`
              - CoClass StateCalcMagFieldDipoleL.

            * - :pyclass:`~StateCalcSEETMagnitudeFieldFieldLineSepAngle`
              - SEETMagFieldFieldLineSepAngle Calc object.

            * - :pyclass:`~StateCalcImpactFlux`
              - CoClass StateCalcImpactFlux.

            * - :pyclass:`~StateCalcImpactMassFlux`
              - CoClass StateCalcImpactMassFlux.

            * - :pyclass:`~StateCalcSEETSAAFlux`
              - CoClass StateCalcSEETSAAFlux.

            * - :pyclass:`~StateCalcSEETVehTemp`
              - CoClass StateCalcSEETVehTemp.

            * - :pyclass:`~StateCalcEpoch`
              - Epoch Calc objects.

            * - :pyclass:`~StateCalcJacobiConstant`
              - Jacobi Constant Calc objects.

            * - :pyclass:`~StateCalcJacobiOsculating`
              - Osculating Jacobi Integral Calc objects.

            * - :pyclass:`~StateCalcCartesianElem`
              - Cartesian Elements Calc objects.

            * - :pyclass:`~StateCalcCartSTMElem`
              - Cartesian STM Elements Calc objects.

            * - :pyclass:`~StateCalcSTMEigenval`
              - Cartesian STM Eigenvalues Calc objects.

            * - :pyclass:`~StateCalcSTMEigenvecElem`
              - Cartesian STM Eigenvector Calc objects.

            * - :pyclass:`~StateCalcEnvironment`
              - Environment Calc objects.

            * - :pyclass:`~StateCalcOrbitDelaunayG`
              - CoClass AsStateCalcOrbitDelaunayG.

            * - :pyclass:`~StateCalcOrbitDelaunayH`
              - CoClass AsStateCalcOrbitDelaunayH.

            * - :pyclass:`~StateCalcOrbitDelaunayL`
              - CoClass AsStateCalcOrbitDelaunayL.

            * - :pyclass:`~StateCalcOrbitSemiLatusRectum`
              - CoClass AsStateCalcOrbitSemiLatusRectum.

            * - :pyclass:`~StateCalcEquinoctialElem`
              - Equinoctial Elements Calc objects.

            * - :pyclass:`~StateCalcCloseApproachBearing`
              - CloseApproachBearing Calc objects.

            * - :pyclass:`~StateCalcCloseApproachMagnitude`
              - CloseApproachMag Calc objects.

            * - :pyclass:`~StateCalcCloseApproachTheta`
              - CloseApproachTheta Calc objects.

            * - :pyclass:`~StateCalcCloseApproachX`
              - CloseApproachX Calc objects.

            * - :pyclass:`~StateCalcCloseApproachY`
              - CloseApproachY Calc objects.

            * - :pyclass:`~StateCalcCloseApproachCosBearing`
              - CloseApproachCosBearing Calc objects.

            * - :pyclass:`~StateCalcRelGroundTrackError`
              - RelGroundTrackError Calc objects.

            * - :pyclass:`~StateCalcRelAtAOLMaster`
              - RelAOLMaster Calc objects.

            * - :pyclass:`~StateCalcDeltaFromMaster`
              - DeltaFromMaster Calc objects.

            * - :pyclass:`~StateCalcLonDriftRate`
              - LongDriftRate Calc objects.

            * - :pyclass:`~StateCalcMeanEarthLon`
              - MeanEarthLon Calc objects.

            * - :pyclass:`~StateCalcRectifiedLon`
              - RectifiedLongitude Calc objects.

            * - :pyclass:`~StateCalcTrueLongitude`
              - TrueLongitude Calc objects.

            * - :pyclass:`~StateCalcGeodeticTrueLongitude`
              - GeodeticTrueLongitude Calc objects.

            * - :pyclass:`~StateCalcGeodeticTrueLongitudeAtTimeOfPerigee`
              - GeodeticTrueLongitudeAtTimeOfPerigee Calc objects.

            * - :pyclass:`~StateCalcMeanRightAscension`
              - MeanRightAscension Calc objects.

            * - :pyclass:`~StateCalcGeodeticMeanRightAscension`
              - GeodeticMeanRightAscension Calc objects.

            * - :pyclass:`~StateCalcTwoBodyDriftRate`
              - TwoBodyDriftRate Calc objects.

            * - :pyclass:`~StateCalcDriftRateFactor`
              - DriftRateFactor Calc objects.

            * - :pyclass:`~StateCalcEccentricityX`
              - EccentricityX Calc objects.

            * - :pyclass:`~StateCalcEccentricityY`
              - EccentricityY Calc objects.

            * - :pyclass:`~StateCalcInclinationX`
              - InclinationX Calc objects.

            * - :pyclass:`~StateCalcInclinationY`
              - InclinationY Calc objects.

            * - :pyclass:`~StateCalcUnitAngularMomentumX`
              - UnitAngularMomentumX Calc objects.

            * - :pyclass:`~StateCalcUnitAngularMomentumY`
              - UnitAngularMomentumY Calc objects.

            * - :pyclass:`~StateCalcUnitAngularMomentumZ`
              - UnitAngularMomentumZ Calc objects.

            * - :pyclass:`~StateCalcHeightAboveTerrain`
              - CoClass AsStateCalcHeightAboveTerrain.

            * - :pyclass:`~StateCalcGeodeticElem`
              - Geodetic Elements Calc objects.

            * - :pyclass:`~StateCalcRepeatingGroundTrackErr`
              - RepeatingGrTrackErr Calc objects.

            * - :pyclass:`~StateCalcAltitudeOfApoapsis`
              - AltitudeOfApoapsis Calc objects.

            * - :pyclass:`~StateCalcAltitudeOfPeriapsis`
              - AltitudeOfPeriapsis Calc objects.

            * - :pyclass:`~StateCalcArgOfLat`
              - Argument of Latitude Calc objects.

            * - :pyclass:`~StateCalcArgOfPeriapsis`
              - Argument of Periapsis Calc objects.

            * - :pyclass:`~StateCalcEccentricityAnomaly`
              - EccAnomaly Calc objects.

            * - :pyclass:`~StateCalcLonOfAscNode`
              - LongitudeOfAscendingNode Calc objects.

            * - :pyclass:`~StateCalcMeanMotion`
              - MeanMotion Calc objects.

            * - :pyclass:`~StateCalcOrbitPeriod`
              - OrbitPeriod Calc objects.

            * - :pyclass:`~StateCalcNumRevs`
              - NumRevs Calc objects.

            * - :pyclass:`~StateCalcRadOfApoapsis`
              - RadiusOfApoapsis Calc objects.

            * - :pyclass:`~StateCalcRadOfPeriapsis`
              - RadiusOfPeriapsis Calc objects.

            * - :pyclass:`~StateCalcSemiMajorAxis`
              - SemiMajorAxis Calc objects.

            * - :pyclass:`~StateCalcTimePastAscNode`
              - TimePastAscNode Calc objects.

            * - :pyclass:`~StateCalcTimePastPeriapsis`
              - TimePastPeriapsis Calc objects.

            * - :pyclass:`~StateCalcTrueAnomaly`
              - TrueAnomaly Calc objects.

            * - :pyclass:`~StateCalcDeltaV`
              - DeltaV Calc objects.

            * - :pyclass:`~StateCalcDeltaVSquared`
              - DeltaV Squared Calc objects.

            * - :pyclass:`~StateCalcMissionControlSequenceDeltaV`
              - MCS DeltaV Calc objects.

            * - :pyclass:`~StateCalcMissionControlSequenceDeltaVSquared`
              - MCS DeltaV Squared Calc objects.

            * - :pyclass:`~StateCalcSequenceDeltaV`
              - Sequence DeltaV Calc objects.

            * - :pyclass:`~StateCalcSequenceDeltaVSquared`
              - Sequence DeltaV Squared Calc objects.

            * - :pyclass:`~StateCalcFuelMass`
              - FuelMass Calc objects.

            * - :pyclass:`~StateCalcDensity`
              - Density  Calc objects.

            * - :pyclass:`~StateCalcInertialDeltaVMagnitude`
              - InertialDeltaVMag Calc objects.

            * - :pyclass:`~StateCalcInertialDeltaVx`
              - InertialDeltaVx Calc objects.

            * - :pyclass:`~StateCalcInertialDeltaVy`
              - InertialDeltaVy Calc objects.

            * - :pyclass:`~StateCalcInertialDeltaVz`
              - InertialDeltaVz Calc objects.

            * - :pyclass:`~StateCalcManeuverSpecificImpulse`
              - ManeuverSpecificImpulse Calc objects.

            * - :pyclass:`~StateCalcPressure`
              - Pressure Calc objects.

            * - :pyclass:`~StateCalcTemperature`
              - Temperature Calc objects.

            * - :pyclass:`~StateCalcVectorY`
              - VectorY Calc objects.

            * - :pyclass:`~StateCalcVectorZ`
              - VectorZ Calc objects.

            * - :pyclass:`~StateCalcMass`
              - Mass Calc objects.

            * - :pyclass:`~StateCalcManeuverTotalMassFlowRate`
              - ManeuverTotalMassFlowRate Calc objects.

            * - :pyclass:`~StateCalcAbsoluteValue`
              - AbsoluteValue Calc objects.

            * - :pyclass:`~StateCalcDifference`
              - Difference Calc objects.

            * - :pyclass:`~StateCalcDifferenceOtherSegment`
              - DifferenceOtherSegment Calc objects.

            * - :pyclass:`~StateCalcPositionDifferenceOtherSegment`
              - PosDifferenceOtherSegment Calc objects.

            * - :pyclass:`~StateCalcVelDifferenceOtherSegment`
              - VelDifferenceOtherSegment Calc objects.

            * - :pyclass:`~StateCalcPositionVelDifferenceOtherSegment`
              - PosVelDifferenceOtherSegment Calc objects.

            * - :pyclass:`~StateCalcValueAtSegment`
              - ValueAtSegment Calc objects.

            * - :pyclass:`~StateCalcMaxValue`
              - MaximumValue Calc objects.

            * - :pyclass:`~StateCalcMinValue`
              - MinimumValue Calc objects.

            * - :pyclass:`~StateCalcMeanValue`
              - MeanValue Calc objects.

            * - :pyclass:`~StateCalcMedianValue`
              - MedianValue Calc objects.

            * - :pyclass:`~StateCalcStandardDeviation`
              - StandardDeviation Calc objects.

            * - :pyclass:`~StateCalcNegative`
              - Negative Calc objects.

            * - :pyclass:`~StateCalcEccentricity`
              - Eccentricity Calc objects.

            * - :pyclass:`~StateCalcMeanAnomaly`
              - MeanAnomaly Calc objects.

            * - :pyclass:`~StateCalcRAAN`
              - RAAN Calc objects.

            * - :pyclass:`~BDotRCalc`
              - BDotR Calc objects.

            * - :pyclass:`~BDotTCalc`
              - BDotT Calc objects.

            * - :pyclass:`~BMagnitudeCalc`
              - BMag Calc objects.

            * - :pyclass:`~BThetaCalc`
              - BTheta Calc objects.

            * - :pyclass:`~StateCalcDeltaDec`
              - DeltaDec Calc objects.

            * - :pyclass:`~StateCalcDeltaRA`
              - DeltaRA Calc objects.

            * - :pyclass:`~StateCalcBetaAngle`
              - BetaAngle Calc objects.

            * - :pyclass:`~StateCalcLocalApparentSolarLon`
              - LocalApparentSolarLon Calc objects.

            * - :pyclass:`~StateCalcLonOfPeriapsis`
              - LonOfPeriapsis Calc objects.

            * - :pyclass:`~StateCalcOrbitStateValue`
              - OrbitStateValue Calc objects.

            * - :pyclass:`~StateCalcSignedEccentricity`
              - SignedEccentricity Calc objects.

            * - :pyclass:`~StateCalcInclination`
              - Inclination Calc objects.

            * - :pyclass:`~StateCalcTrueLon`
              - TrueLong Calc objects.

            * - :pyclass:`~StateCalcPower`
              - Power Calc objects.

            * - :pyclass:`~StateCalcRelMotion`
              - Relative Motion Calc objects.

            * - :pyclass:`~StateCalcSolarBetaAngle`
              - Solar Beta Angle objects.

            * - :pyclass:`~StateCalcSolarInPlaneAngle`
              - Solar In Plane Angle objects.

            * - :pyclass:`~StateCalcRelPositionDecAngle`
              - Relative Position Declination Angle objects.

            * - :pyclass:`~StateCalcRelPositionInPlaneAngle`
              - Relative Position Declination Angle objects.

            * - :pyclass:`~StateCalcRelativeInclination`
              - Relative Inclination Angle objects.

            * - :pyclass:`~StateCalcCurvilinearRelMotion`
              - Curvilinear Relative Motion objects.

            * - :pyclass:`~StateCalcCustomFunction`
              - Custom Function Calc objects.

            * - :pyclass:`~StateCalcScript`
              - Script Calc objects.

            * - :pyclass:`~StateCalcCd`
              - Cd Calc objects.

            * - :pyclass:`~StateCalcCr`
              - Cr Calc objects.

            * - :pyclass:`~StateCalcDragArea`
              - DragArea Calc objects.

            * - :pyclass:`~StateCalcRadiationPressureArea`
              - RadPressureArea Calc objects.

            * - :pyclass:`~StateCalcRadiationPressureCoefficient`
              - RadiationPressureCoefficient Calc objects.

            * - :pyclass:`~StateCalcSRPArea`
              - SRPArea Calc objects.

            * - :pyclass:`~StateCalcCosOfVerticalFPA`
              - CosineOfVerticalFPA Calc objects.

            * - :pyclass:`~StateCalcDec`
              - Dec Calc objects.

            * - :pyclass:`~StateCalcFPA`
              - FPA Calc objects.

            * - :pyclass:`~StateCalcRMagnitude`
              - RMag Calc objects.

            * - :pyclass:`~StateCalcRA`
              - RA Calc objects.

            * - :pyclass:`~StateCalcVMagnitude`
              - VMag Calc objects.

            * - :pyclass:`~StateCalcVelAz`
              - Velocity Azimuth Calc objects.

            * - :pyclass:`~StateCalcC3Energy`
              - C3Energy Calc objects.

            * - :pyclass:`~StateCalcInAsympDec`
              - InAsymptoteDec Calc objects.

            * - :pyclass:`~StateCalcInAsympRA`
              - InAsymptoteRA Calc objects.

            * - :pyclass:`~StateCalcInVelAzAtPeriapsis`
              - InVelocityAzAtPeriapsis Calc objects.

            * - :pyclass:`~StateCalcOutAsympDec`
              - OutAsymptoteDec Calc objects.

            * - :pyclass:`~StateCalcOutAsympRA`
              - OutAsymptoteRA Calc objects.

            * - :pyclass:`~StateCalcOutVelAzAtPeriapsis`
              - OutVelocityAzAtPeriapsis Calc objects.

            * - :pyclass:`~StateCalcDuration`
              - Duration Calc objects.

            * - :pyclass:`~StateCalcUserValue`
              - CoClass StateCalcUserValue.

            * - :pyclass:`~StateCalcVectorGeometryToolAngle`
              - Vector Geometry Tool Angle Calc objects.

            * - :pyclass:`~StateCalcAngle`
              - Angle Calc objects.

            * - :pyclass:`~StateCalcDotProduct`
              - DotProduct Calc objects.

            * - :pyclass:`~StateCalcVectorDec`
              - VectorDec Calc objects.

            * - :pyclass:`~StateCalcVectorMagnitude`
              - VectorMag Calc objects.

            * - :pyclass:`~StateCalcVectorRA`
              - VectorRA Calc objects.

            * - :pyclass:`~StateCalcVectorX`
              - VectorX Calc objects.

            * - :pyclass:`~StateCalcOnePointAccess`
              - Access Calc objects.

            * - :pyclass:`~StateCalcDifferenceAcrossSegmentsOtherSat`
              - DifferenceAcrossSegmentsOtherSat Calc objects.

            * - :pyclass:`~StateCalcValueAtSegmentOtherSat`
              - ValueAtSegmentOtherSat Calc objects.

            * - :pyclass:`~StateCalcRARate`
              - RightAscensionRate Calc objects.

            * - :pyclass:`~StateCalcDecRate`
              - DeclinationRate Calc objects.

            * - :pyclass:`~StateCalcRangeRate`
              - RangeRate Calc objects.

            * - :pyclass:`~StateCalcGravitationalParameter`
              - GravitationalParameter Calc objects.

            * - :pyclass:`~StateCalcReferenceRadius`
              - Reference Radius Calc objects.

            * - :pyclass:`~StateCalcGravCoeff`
              - Gravity Coefficient Calc objects.

            * - :pyclass:`~StateCalcSpeedOfLight`
              - Speed Of Light Calc objects.

            * - :pyclass:`~StateCalcPi`
              - Pi Calc objects.

            * - :pyclass:`~StateCalcScalar`
              - Scalar Calc objects.

            * - :pyclass:`~StateCalcApparentSolarTime`
              - Apparent Solar Time Calc objects.

            * - :pyclass:`~StateCalcEarthMeanSolarTime`
              - EarthMeanSolarTime Calc objects.

            * - :pyclass:`~StateCalcEarthMeanLocTimeAN`
              - EarthMeanLocTimeAN Calc objects.

            * - :pyclass:`~AutomaticSequenceCollection`
              - Automatic Sequence Collection.

            * - :pyclass:`~AutomaticSequence`
              - Automatic Sequence.

            * - :pyclass:`~CentralBodyCollection`
              - Central Body Collection.

            * - :pyclass:`~AstrogatorCentralBody`
              - Central Body.

            * - :pyclass:`~CentralBodyGravityModel`
              - Central Body Gravity Model.

            * - :pyclass:`~CentralBodyShapeSphere`
              - Central Body Shape - Sphere.

            * - :pyclass:`~CentralBodyShapeOblateSpheroid`
              - Central Body Shape - Spheroid.

            * - :pyclass:`~CentralBodyShapeTriaxialEllipsoid`
              - Central Body Shape - Triaxial Ellipsoid.

            * - :pyclass:`~CentralBodyAttitudeRotationCoefficientsFile`
              - Central Body Attitude - Rotation Coefficients File.

            * - :pyclass:`~CentralBodyAttitudeIAU1994`
              - Central Body Attitude - IAU1994.

            * - :pyclass:`~CentralBodyEphemerisAnalyticOrbit`
              - Central Body Ephemeris - Analytic Orbit.

            * - :pyclass:`~CentralBodyEphemerisJPLSpice`
              - Central Body Ephemeris - JPLSpice.

            * - :pyclass:`~CentralBodyEphemerisFile`
              - Central Body Ephemeris - File.

            * - :pyclass:`~CentralBodyEphemerisJPLDesignExplorerOptimizer`
              - Central Body Ephemeris - JPL DE.

            * - :pyclass:`~CentralBodyEphemerisPlanetary`
              - Central Body Ephemeris - Planetary.

            * - :pyclass:`~MissionControlSequenceSegmentProperties`
              - Segment Properties.

            * - :pyclass:`~PowerInternal`
              - Power - Internal.

            * - :pyclass:`~PowerProcessed`
              - Power - Processed Power Unit.

            * - :pyclass:`~PowerSolarArray`
              - Power - Solar Array.

            * - :pyclass:`~GeneralRelativityFunction`
              - General Relativity Propagator Function.

            * - :pyclass:`~StateTransformationFunction`
              - State Transition Propagator Function.

            * - :pyclass:`~CR3BPFunc`
              - CR3BP Function.

            * - :pyclass:`~ER3BPFunc`
              - ER3BP Function.

            * - :pyclass:`~RadiationPressureFunction`
              - Radiation Pressure Propagator Function.

            * - :pyclass:`~YarkovskyFunc`
              - Yarkovsky Effect Propagator Function.

            * - :pyclass:`~BlendedDensity`
              - Blended atmospheric density propagator function.

            * - :pyclass:`~Cira72Function`
              - Cira72 atmospheric propagator function.

            * - :pyclass:`~Exponential`
              - Exponential atmospheric propagator function.

            * - :pyclass:`~HarrisPriester`
              - Harris-Priester atmospheric propagator function.

            * - :pyclass:`~DensityModelPlugin`
              - Plugin atmospheric density propagator function.

            * - :pyclass:`~JacchiaRoberts`
              - Jacchia Roberts atmospheric propagator function.

            * - :pyclass:`~JacchiaBowman2008`
              - Jacchia Bowman 2008 atmospheric propagator function.

            * - :pyclass:`~Jacchia_1960`
              - Jacchia_1960 atmospheric propagator function.

            * - :pyclass:`~Jacchia_1970`
              - Jacchia_1970 atmospheric propagator function.

            * - :pyclass:`~Jacchia_1971`
              - Jacchia_1971 atmospheric propagator function.

            * - :pyclass:`~MSISE_1990`
              - MSISE 1990 atmospheric propagator function.

            * - :pyclass:`~MSIS_1986`
              - MSIS 1986 atmospheric propagator function.

            * - :pyclass:`~NRLMSISE_2000`
              - NRLMSISE 2000 atmospheric propagator function.

            * - :pyclass:`~US_Standard_Atmosphere`
              - US_Standard_Atmosphere atmospheric propagator function.

            * - :pyclass:`~MarsGRAM37`
              - Mars-GRAM 3.7 atmospheric propagator function.

            * - :pyclass:`~MarsGRAM2000`
              - Mars-GRAM 2000 atmospheric propagator function.

            * - :pyclass:`~MarsGRAM2001`
              - Mars-GRAM 2001 atmospheric propagator function.

            * - :pyclass:`~MarsGRAM2005`
              - Mars-GRAM 2005 atmospheric propagator function.

            * - :pyclass:`~MarsGRAM2010`
              - Mars-GRAM 2010 atmospheric propagator function.

            * - :pyclass:`~VenusGRAM2005`
              - Venus-GRAM 2005 atmospheric propagator function.

            * - :pyclass:`~DTM2012`
              - DTM 2012 atmospheric propagator function.

            * - :pyclass:`~DTM2020`
              - DTM 2020 atmospheric propagator function.

            * - :pyclass:`~GravityFieldFunction`
              - Gravity Field gravity propagator function.

            * - :pyclass:`~PointMassFunction`
              - Point Mass function.

            * - :pyclass:`~TwoBodyFunction`
              - Two Body gravity propagator function.

            * - :pyclass:`~HPOPPluginFunction`
              - HPOP Plugin propagator function.

            * - :pyclass:`~EOMFuncPluginFunction`
              - EOM Function Plugin propagator function.

            * - :pyclass:`~SRPAeroT20`
              - AeroT20 SRP propagator function.

            * - :pyclass:`~SRPAeroT30`
              - AeroT30 SRP propagator function.

            * - :pyclass:`~SRPGSPM04aIIA`
              - GSPM04aIIA SRP propagator function.

            * - :pyclass:`~SRPGSPM04aIIR`
              - GSPM04aIIR SRP propagator function.

            * - :pyclass:`~SRPGSPM04aeIIA`
              - GSPM04aeIIA SRP propagator function.

            * - :pyclass:`~SRPGSPM04aeIIR`
              - GSPM04aeIIR SRP propagator function.

            * - :pyclass:`~SRPSpherical`
              - Spherical SRP propagator function.

            * - :pyclass:`~SRPNPlate`
              - NPlate SRP propagator function.

            * - :pyclass:`~SRPTabAreaVec`
              - Tabulated area vector SRP propagator function.

            * - :pyclass:`~SRPVariableArea`
              - Variable Area SRP propagator function.

            * - :pyclass:`~ThirdBodyFunction`
              - ThirdBody propagator function.

            * - :pyclass:`~DragModelPlugin`
              - Drag Model Plugin.

            * - :pyclass:`~SRPReflectionPlugin`
              - SRP Reflection Plugin.

            * - :pyclass:`~EngineConstAcc`
              - Constant Acceleration engine model.

            * - :pyclass:`~EngineConstant`
              - Constant Thrust engine model.

            * - :pyclass:`~EngineIon`
              - Ion Engine engine model.

            * - :pyclass:`~EngineThrottleTable`
              - Throttle Table engine model.

            * - :pyclass:`~EngineCustom`
              - Custom engine model.

            * - :pyclass:`~EnginePlugin`
              - Plugin engine model.

            * - :pyclass:`~EngineModelPoly`
              - Polynomial Thrust and Isp engine model.

            * - :pyclass:`~EngineModelThrustCoefficients`
              - Engine Model Thrust Coefficients.

            * - :pyclass:`~EngineModelIspCoefficients`
              - Engine Model Isp Coefficients.

            * - :pyclass:`~EngineDefinition`
              - Engine definition.

            * - :pyclass:`~DesignCR3BPSetup`
              - CR3BP Setup Tool.

            * - :pyclass:`~DesignCR3BPObject`
              - CR3BP associated object definition.

            * - :pyclass:`~DesignCR3BPObjectCollection`
              - CR3BP associated object Collection.

            * - :pyclass:`~DesignER3BPSetup`
              - ER3BP Setup Tool.

            * - :pyclass:`~DesignER3BPObject`
              - ER3BP associated object definition.

            * - :pyclass:`~DesignER3BPObjectCollection`
              - ER3BP associated object Collection.

            * - :pyclass:`~Thruster`
              - Thruster definition.

            * - :pyclass:`~ThrusterSetCollection`
              - Thruster Set Collection.

            * - :pyclass:`~ThrusterSet`
              - Thruster Set.

            * - :pyclass:`~AsTriggerCondition`
              - Constraint.

            * - :pyclass:`~CustomFunctionScriptEngine`
              - Custom Function Script Engine.

            * - :pyclass:`~NumericalPropagatorWrapper`
              - Numerical Propagator.

            * - :pyclass:`~NumericalPropagatorWrapperCR3BP`
              - Numerical CR3BP Propagator.

            * - :pyclass:`~PropagatorFunctionCollection`
              - Propagator Function Collection.

            * - :pyclass:`~BulirschStoerIntegrator`
              - Bulirsch-Stoer Numerical Integrator.

            * - :pyclass:`~GaussJacksonIntegrator`
              - Gauss-Jackson Numerical Integrator.

            * - :pyclass:`~RungeKutta2nd3rd`
              - RK2nd3rd Numerical Integrator.

            * - :pyclass:`~RungeKutta4th`
              - RK4th Numerical Integrator.

            * - :pyclass:`~RungeKutta4th5th`
              - RK4th5th Numerical Integrator.

            * - :pyclass:`~RungeKutta4thAdapt`
              - RK4thAdapt Numerical Integrator.

            * - :pyclass:`~RungeKuttaF7th8th`
              - RKF7th8th Numerical Integrator.

            * - :pyclass:`~RungeKuttaV8th9th`
              - RKV8th9th Numerical Integrator.

            * - :pyclass:`~ScriptingTool`
              - Scripting Tool.

            * - :pyclass:`~ScriptingSegmentCollection`
              - Scripting Segment Collection.

            * - :pyclass:`~ScriptingSegment`
              - Scripting Segment.

            * - :pyclass:`~ScriptingParameterCollection`
              - Scripting Parameter Collection.

            * - :pyclass:`~ScriptingParameter`
              - Scripting Parameter.

            * - :pyclass:`~ScriptingCalcObject`
              - Calc Object.

            * - :pyclass:`~ScriptingCalcObjectCollection`
              - Calc Object Collection.

            * - :pyclass:`~UserVariableDefinition`
              - User Variable Definition.

            * - :pyclass:`~UserVariable`
              - User Variable.

            * - :pyclass:`~UserVariableUpdate`
              - User Variable Update.

            * - :pyclass:`~UserVariableDefinitionCollection`
              - User Variable Definition Collection.

            * - :pyclass:`~UserVariableCollection`
              - User Variable Initial Value Collection.

            * - :pyclass:`~UserVariableUpdateCollection`
              - User Variable Update Collection.

            * - :pyclass:`~CalculationGraphCollection`
              - Calculation Graph Collection.

            * - :pyclass:`~ScriptingParameterEnumerationChoice`
              - Scripting Parameter Enumeration Choice.

            * - :pyclass:`~ScriptingParameterEnumerationChoiceCollection`
              - Scripting Parameter Enumeration Choice Collection.

            * - :pyclass:`~ProfileSNOPTOptimizer`
              - SNOPT optimizer profile.

            * - :pyclass:`~SNOPTControl`
              - Control parameters for SNOPT optimizer profile.

            * - :pyclass:`~SNOPTResult`
              - Properties for objecvtive and constraints of a SNOPT profile.

            * - :pyclass:`~SNOPTControlCollection`
              - SNOPT control collection.

            * - :pyclass:`~SNOPTResultCollection`
              - SNOPT result collection.

            * - :pyclass:`~ProfileIPOPTOptimizer`
              - IPOPT optimizer profile.

            * - :pyclass:`~IPOPTControl`
              - Control parameters for IPOPT optimizer profile.

            * - :pyclass:`~IPOPTResult`
              - Properties for objecvtive and constraints of a IPOPT profile.

            * - :pyclass:`~IPOPTControlCollection`
              - Properties for the list of IPOPT control parameters.

            * - :pyclass:`~IPOPTResultCollection`
              - IPOPT result collection.

            * - :pyclass:`~ManeuverOptimalFinite`
              - The Optimal Finite Maneuver.

            * - :pyclass:`~ManeuverOptimalFiniteSNOPTOptimizer`
              - Properties of SNOPT Optimizer options for optimal finite maneuver.

            * - :pyclass:`~ManeuverOptimalFiniteInitialBoundaryConditions`
              - Properties of initial boundary conditions for optimal finite maneuver.

            * - :pyclass:`~ManeuverOptimalFiniteFinalBoundaryConditions`
              - Properties of final boundary conditions for optimal finite maneuver.

            * - :pyclass:`~ManeuverOptimalFinitePathBoundaryConditions`
              - Properties of path boundary conditions for optimal finite maneuver.

            * - :pyclass:`~ManeuverOptimalFiniteSteeringNodeElement`
              - The elements of the steering node.

            * - :pyclass:`~ManeuverOptimalFiniteSteeringNodeCollection`
              - Steering/nodes collection.

            * - :pyclass:`~ManeuverOptimalFiniteBounds`
              - The elements of the steering node.

            * - :pyclass:`~ProfileLambertProfile`
              - The Lambert profile.

            * - :pyclass:`~ProfileLambertSearchProfile`
              - The Lambert profile.

            * - :pyclass:`~ProfileGoldenSection`
              - The Golden Section profile.

            * - :pyclass:`~GoldenSectionControlCollection`
              - Properties for the list of Golden Section control parameters.

            * - :pyclass:`~GoldenSectionControl`
              - Control parameters for Golden Section profile.

            * - :pyclass:`~GoldenSectionResultCollection`
              - Properties for the list of Golden Section result parameters.

            * - :pyclass:`~GoldenSectionResult`
              - Result parameters for Golden Section profile.

            * - :pyclass:`~ProfileGridSearch`
              - The Grid Search profile.

            * - :pyclass:`~GridSearchControlCollection`
              - Properties for the list of Grid Search control parameters.

            * - :pyclass:`~GridSearchControl`
              - Control parameters for Grid Search profile.

            * - :pyclass:`~GridSearchResultCollection`
              - Properties for the list of Grid Search result parameters.

            * - :pyclass:`~GridSearchResult`
              - Result parameters for Grid Search profile.

            * - :pyclass:`~CalcObjectLinkEmbedControlCollection`
              - The Calculation Object link/embed component folder.

            * - :pyclass:`~ProfileBisection`
              - Single Parameter Bisection profile.

            * - :pyclass:`~BisectionControl`
              - Control parameters for  Bisection Seacrh Profile.

            * - :pyclass:`~BisectionControlCollection`
              - Bisection control collection.

            * - :pyclass:`~BisectionResult`
              - Result parameters for Bisection profile.

            * - :pyclass:`~BisectionResultCollection`
              - Bisection result collection.


    .. tab-items:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~GRAPH_OPTION`
              - Mode that the mcs will run in.

            * - :pyclass:`~SMART_RUN_MODE`
              - Mode that the mcs will run in.

            * - :pyclass:`~FORMULATION`
              - Equinoctial Formulation.

            * - :pyclass:`~LIGHTING_CONDITION`
              - The criteria of a Lighting stopping condition.

            * - :pyclass:`~PROFILE`
              - Type of profile.

            * - :pyclass:`~ACCESS_CRITERION`
              - The criteria of an Access stopping condition.

            * - :pyclass:`~ECLIPSING_BODIES_SOURCE`
              - The source types of the eclipsing bodies list.

            * - :pyclass:`~CRITERION`
              - The stopping condition criterion types.

            * - :pyclass:`~CALC_OBJECT_REFERENCE`
              - The calculation object Reference Selection types.

            * - :pyclass:`~CALC_OBJECT_CENTRAL_BODY_REFERENCE`
              - The calculation object Central Body Reference Selection types.

            * - :pyclass:`~CALC_OBJECT_ELEM`
              - The calculation object Element Types.

            * - :pyclass:`~PROFILE_MODE`
              - The Target Sequence profile modes.

            * - :pyclass:`~CONTROL_STOPPING_CONDITION`
              - The stopping condition control types.

            * - :pyclass:`~STATE`
              - The Stop segment state types.

            * - :pyclass:`~RETURN_CONTROL`
              - The Return segment control types.

            * - :pyclass:`~DRAW_PERTURBATION`
              - The Draw Perturbation types for a Differential Corrector profile.

            * - :pyclass:`~DERIVE_CALC_METHOD`
              - The Derivative Calculation method types for a Differential Corrector profile.

            * - :pyclass:`~CONVERGENCE_CRITERIA`
              - The Convergence Criteria types for a Differential Corrector profile.

            * - :pyclass:`~DIFFERENTIAL_CORRECTOR_SCALING_METHOD`
              - The Scaling Method types for a Differential Corrector profile.

            * - :pyclass:`~CONTROL_UPDATE`
              - Update segment properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_FOLLOW`
              - Follow segment properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_INIT_STATE`
              - Initial State segment properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_MANEUVER`
              - Maneuver segment properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_LAUNCH`
              - Launch segment properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_ADVANCED`
              - Propagate segment properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~TARGET_SEQ_ACTION`
              - Action options for Target Sequence profiles.

            * - :pyclass:`~PROFILES_FINISH`
              - Action options for Target Sequence profiles convergence.

            * - :pyclass:`~UPDATE_PARAM`
              - Spacecraft parameters that can be modified by an Update segment.

            * - :pyclass:`~UPDATE_ACTION`
              - Actions for the Update segment.

            * - :pyclass:`~PRESSURE_MODE`
              - Pressure Mode options.

            * - :pyclass:`~THRUST_TYPE`
              - Thrust options.

            * - :pyclass:`~ATTITUDE_UPDATE`
              - Attitude Update.

            * - :pyclass:`~PROPULSION_METHOD`
              - Propulsion method options.

            * - :pyclass:`~CUSTOM_FUNCTION`
              - Attitude definition options for other STK functions.

            * - :pyclass:`~BODY_AXIS`
              - Attitude body axis options.

            * - :pyclass:`~CONSTRAINT_SIGN`
              - Constraint vector sign options.

            * - :pyclass:`~ATTITUDE_CONTROL`
              - Attitude Control options.

            * - :pyclass:`~FOLLOW_JOIN`
              - Joining options for the Follow segment.

            * - :pyclass:`~FOLLOW_SEPARATION`
              - Separation options for the Follow segment.

            * - :pyclass:`~FOLLOW_SPACECRAFT_AND_FUEL_TANK`
              - Spacecraft parameter options for the Follow segment.

            * - :pyclass:`~BURNOUT_OPTIONS`
              - Burnout options for the Launch segment.

            * - :pyclass:`~BURNOUT_TYPE`
              - Burnout point definition types for the Launch segment.

            * - :pyclass:`~ASCENT_TYPE`
              - Ascent types for the Launch segment.

            * - :pyclass:`~LAUNCH_DISPLAY_SYSTEM`
              - Launch location coordinate types for the Launch segment.

            * - :pyclass:`~RUN_CODE`
              - The run code returned after the MCS is run.

            * - :pyclass:`~SEQUENCE_STATE_TO_PASS`
              - State To Pass options for the Sequence segment.

            * - :pyclass:`~MANEUVER_TYPE`
              - Maneuver types for the maneuver segment.

            * - :pyclass:`~SEGMENT_TYPE`
              - Segment types.

            * - :pyclass:`~ELEMENT_TYPE`
              - Types of orbit element sets.

            * - :pyclass:`~LANGUAGE`
              - Scripting language types for the Scripting Tool.

            * - :pyclass:`~STOPPING_CONDITION`
              - Type of stopping condition.

            * - :pyclass:`~CLEAR_EPHEMERIS_DIRECTION`
              - Direction in which to clear ephemeris.

            * - :pyclass:`~PROFILE_INSERT_DIRECTION`
              - Direction to insert profile.

            * - :pyclass:`~ROOT_FINDING_ALGORITHM`
              - Root-finding algorithms.

            * - :pyclass:`~SCRIPTING_PARAMETER_TYPE`
              - Scripting Tool parameter type.

            * - :pyclass:`~SNOPT_GOAL`
              - The Goal types for a SNOPT profile.

            * - :pyclass:`~IPOPT_GOAL`
              - The Goal types for a IPOPT profile.

            * - :pyclass:`~OPTIMAL_FINITE_SEED_METHOD`
              - Seed methods.

            * - :pyclass:`~OPTIMAL_FINITE_RUN_MODE`
              - Run modes.

            * - :pyclass:`~OPTIMAL_FINITE_DISCRETIZATION_STRATEGY`
              - Discretization Strategy.

            * - :pyclass:`~OPTIMAL_FINITE_WORKING_VARIABLES`
              - Working Variables.

            * - :pyclass:`~OPTIMAL_FINITE_SCALING_OPTIONS`
              - Scaling Options.

            * - :pyclass:`~OPTIMAL_FINITE_SNOPT_OBJECTIVE`
              - Optimal Finite SNOPT objective.

            * - :pyclass:`~OPTIMAL_FINITE_SNOPT_SCALING`
              - Optimal Finite SNOPT scaling option.

            * - :pyclass:`~OPTIMAL_FINITE_EXPORT_NODES_FORMAT`
              - Steering nodes export format.

            * - :pyclass:`~OPTIMAL_FINITE_GUESS_METHOD`
              - Guess interpolation method.

            * - :pyclass:`~IMP_DELTA_V_REP`
              - Vector representations for impulsive DeltaV specification.

            * - :pyclass:`~LAMBERT_TARGET_COORD_TYPE`
              - Lambert Target CoordType.

            * - :pyclass:`~LAMBERT_SOLUTION_OPTION_TYPE`
              - Lambert Solution Option Type.

            * - :pyclass:`~LAMBERT_ORBITAL_ENERGY_TYPE`
              - Lambert Orbital Energy Type.

            * - :pyclass:`~LAMBERT_DIRECTION_OF_MOTION_TYPE`
              - Lambert Direction Of Motion Type.

            * - :pyclass:`~GOLDEN_SECTION_DESIRED_OPERATION`
              - The types for Desired Operation/Objective of golden section profile.

            * - :pyclass:`~GRID_SEARCH_DESIRED_OPERATION`
              - The types for Desired Operation/Objective of Grid Search profile.

            * - :pyclass:`~ELEMENT`
              - Which type of elements (osculating or mean).

            * - :pyclass:`~BASE_SELECTION`
              - Access base object selections types.

            * - :pyclass:`~CONTROL_ORBIT_STATE_VALUE`
              - Orbit State Value properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~SEGMENT_STATE`
              - Segment state to use types.

            * - :pyclass:`~DIFFERENCE_ORDER`
              - The Difference order types.

            * - :pyclass:`~SEGMENT_DIFFERENCE_ORDER`
              - The Difference Across Segments order types.

            * - :pyclass:`~CONTROL_REPEATING_GROUND_TRACK_ERR`
              - Repeating Ground Track Equator Error properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CALC_OBJECT_DIRECTION`
              - The direction to search for a desired value.

            * - :pyclass:`~CALC_OBJECT_ORBIT_PLANE_SOURCE`
              - The calculation object orbit plane source Types.

            * - :pyclass:`~CALC_OBJECT_SUN_POSITION`
              - The calculation object sun location Types.

            * - :pyclass:`~CALC_OBJECT_ANGLE_SIGN`
              - The sign of the angle when the relative position has a component along the orbit normal.

            * - :pyclass:`~CALC_OBJECT_REFERENCE_DIRECTION`
              - Direction that establishes the zero value when projected into the orbit plane.

            * - :pyclass:`~CALC_OBJECT_RELATIVE_POSITION`
              - The calculation object relative position Types.

            * - :pyclass:`~CALC_OBJECT_REFERENCE_ELLIPSE`
              - The calculation object reference ellipse Types.

            * - :pyclass:`~CALC_OBJECT_LOCATION_SOURCE`
              - The calculation object location source Types.

            * - :pyclass:`~GRAVITATIONAL_PARAMETER_SOURCE`
              - The source of the gravitational parameter for a CAgVAStateCalcGravitationalParameter calculation object.

            * - :pyclass:`~REFERENCE_RADIUS_SOURCE`
              - The source of the reference radius for a CAgVAStateCalcReferenceRadius calculation object.

            * - :pyclass:`~GRAV_COEFF_NORMALIZATION_TYPE`
              - The normalization type for the CAgVAStateCalcGravCoeff calculation object.

            * - :pyclass:`~GRAV_COEFF_COEFFICIENT_TYPE`
              - The coefficient type for the CAgVAStateCalcGravCoeff calculation object.

            * - :pyclass:`~STM_PERT_VARIABLES`
              - The initial and final Cartesian variational variables that describe an STM element.

            * - :pyclass:`~STM_EIGEN_NUMBER`
              - The number that describes one of the 6 STM Eigenvalues or Eigenvectors.

            * - :pyclass:`~COMPLEX_NUMBER`
              - Whether a value represents the real or imaginary portion of a number.

            * - :pyclass:`~SQUARED_TYPE`
              - Whether to calculate the value as the square of the sum of each component or the sum of the squares.

            * - :pyclass:`~GEO_STATIONARY_DRIFT_RATE_MODEL`
              - Gravity models used to compute geostationary drift rate.

            * - :pyclass:`~GEO_STATIONARY_INCLINATION_MAGNITUDE`
              - Magnitude to use when computing the inclination vector.

            * - :pyclass:`~CENTRAL_BODY_GRAVITY_MODEL`
              - The gravity model.

            * - :pyclass:`~CENTRAL_BODY_SHAPE`
              - The central body shape types.

            * - :pyclass:`~CENTRAL_BODY_ATTITUDE`
              - The central body attitude types.

            * - :pyclass:`~CENTRAL_BODY_EPHEMERIS`
              - The central body ephemeris types.

            * - :pyclass:`~CONTROL_POWER_INTERNAL`
              - Internal Power properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_POWER_PROCESSED`
              - Processed Power properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_POWER_SOLAR_ARRAY`
              - Solar Array Power properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~THIRD_BODY_MODE`
              - The third body gravity mode.

            * - :pyclass:`~GRAV_PARAM_SOURCE`
              - The gravity parameter source.

            * - :pyclass:`~EPHEM_SOURCE`
              - The ephemeris source type.

            * - :pyclass:`~SOLAR_FORCE_METHOD`
              - The solar force method type for a spherical or N-plate SRP model.

            * - :pyclass:`~SHADOW_MODEL`
              - The shadow model type.

            * - :pyclass:`~SUN_POSITION`
              - The sun position type.

            * - :pyclass:`~ATMOS_DATA_SOURCE`
              - The Atmospheric data source type.

            * - :pyclass:`~GEO_MAGNETIC_FLUX_SOURCE`
              - Whether to use Kp or Ap data from the flux file.

            * - :pyclass:`~GEO_MAGNETIC_FLUX_UPDATE_RATE`
              - Method for using geomagnetic flux values from the flux file.

            * - :pyclass:`~DRAG_MODEL_TYPE`
              - Type of Drag Model.

            * - :pyclass:`~MARS_GRAM_DENSITY_TYPE`
              - Density Type for MarsGRAM Density Models.

            * - :pyclass:`~VENUS_GRAM_DENSITY_TYPE`
              - Density Type for VenusGRAM Density Models.

            * - :pyclass:`~TAB_VEC_INTERP_METHOD`
              - The interpolation method for tabulated area vector file.

            * - :pyclass:`~CONTROL_ENGINE_CONST_ACC`
              - Constant Acceleration and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_ENGINE_CONSTANT`
              - Constant Thrust and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_ENGINE_CUSTOM`
              - Custom engine model properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_ENGINE_THROTTLE_TABLE`
              - Throttle table engine model properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_ENGINE_ION`
              - Ion engine model properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~CONTROL_ENGINE_MODEL_POLY`
              - Polynomial Thrust and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~ENGINE_MODEL_FUNCTION`
              - The engine model function types.

            * - :pyclass:`~THROTTLE_TABLE_OPERATION_MODE`
              - Engine operation mode.

            * - :pyclass:`~IDEAL_ORBIT_RADIUS`
              - Ideal Orbit Radius.

            * - :pyclass:`~ROTATING_COORDINATE_SYSTEM`
              - Barycenter centered rotating system.

            * - :pyclass:`~CONTROL_THRUSTERS`
              - Thruster properties that can be selected as control parameters for a Target Sequence.

            * - :pyclass:`~THRUSTER_DIRECTION`
              - The thruster direction type.

            * - :pyclass:`~CRITERIA`
              - The criteria type.

            * - :pyclass:`~ERROR_CONTROL`
              - Error Control for the numerical integrator.

            * - :pyclass:`~PREDICTOR_CORRECTOR`
              - Predictor corrector scheme for the numerical integrator.

            * - :pyclass:`~NUMERICAL_INTEGRATOR`
              - Numerical integrator type.

            * - :pyclass:`~COEFF_RUNGE_KUTTA_V_8TH_9TH`
              - Coefficient sets for RKV8th(9th) integrator.



Description
-----------

Object Model components specifically designed to support STK Astrogator.

Detail
------

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> IUserVariableDefinitionCollection<IUserVariableDefinitionCollection>
    --> IUserVariableCollection<IUserVariableCollection>
    --> IUserVariableUpdateCollection<IUserVariableUpdateCollection>
    --> ICalculationGraphCollection<ICalculationGraphCollection>
    --> IConstraintCollection<IConstraintCollection>
    --> IPluginProperties<IPluginProperties>
    --> ISNOPTControlCollection<ISNOPTControlCollection>
    --> ISNOPTResultCollection<ISNOPTResultCollection>
    --> IIPOPTControlCollection<IIPOPTControlCollection>
    --> IIPOPTResultCollection<IIPOPTResultCollection>
    --> IManeuverOptimalFiniteSNOPTOptimizer<IManeuverOptimalFiniteSNOPTOptimizer>
    --> IManeuverOptimalFiniteInitialBoundaryConditions<IManeuverOptimalFiniteInitialBoundaryConditions>
    --> IManeuverOptimalFiniteFinalBoundaryConditions<IManeuverOptimalFiniteFinalBoundaryConditions>
    --> IManeuverOptimalFinitePathBoundaryConditions<IManeuverOptimalFinitePathBoundaryConditions>
    --> IManeuverOptimalFiniteSteeringNodeCollection<IManeuverOptimalFiniteSteeringNodeCollection>
    --> IManeuverOptimalFiniteBounds<IManeuverOptimalFiniteBounds>
    --> IGoldenSectionControlCollection<IGoldenSectionControlCollection>
    --> IGoldenSectionControl<IGoldenSectionControl>
    --> IGoldenSectionResultCollection<IGoldenSectionResultCollection>
    --> IGoldenSectionResult<IGoldenSectionResult>
    --> IGridSearchControlCollection<IGridSearchControlCollection>
    --> IGridSearchControl<IGridSearchControl>
    --> IGridSearchResultCollection<IGridSearchResultCollection>
    --> IGridSearchResult<IGridSearchResult>
    --> IBisectionControlCollection<IBisectionControlCollection>
    --> IBisectionResult<IBisectionResult>
    --> IBisectionResultCollection<IBisectionResultCollection>
    --> IStoppingConditionElement<IStoppingConditionElement>
    --> IStoppingConditionCollection<IStoppingConditionCollection>
    --> IMissionControlSequenceSegmentCollection<IMissionControlSequenceSegmentCollection>
    --> IState<IState>
    --> IStoppingConditionComponent<IStoppingConditionComponent>
    --> IAutomaticSequence<IAutomaticSequence>
    --> IAutomaticSequenceCollection<IAutomaticSequenceCollection>
    --> IBPlaneCollection<IBPlaneCollection>
    --> ICalcObjectCollection<ICalcObjectCollection>
    --> IManeuverFinitePropagator<IManeuverFinitePropagator>
    --> IBurnoutVelocity<IBurnoutVelocity>
    --> IAttitudeControl<IAttitudeControl>
    --> IAttitudeControlFinite<IAttitudeControlFinite>
    --> IAttitudeControlImpulsive<IAttitudeControlImpulsive>
    --> IAttitudeControlOptimalFinite<IAttitudeControlOptimalFinite>
    --> IManeuver<IManeuver>
    --> IDisplaySystem<IDisplaySystem>
    --> IBurnout<IBurnout>
    --> IScriptingSegment<IScriptingSegment>
    --> IScriptingSegmentCollection<IScriptingSegmentCollection>
    --> IScriptingParameterEnumerationChoice<IScriptingParameterEnumerationChoice>
    --> IScriptingParameterEnumerationChoiceCollection<IScriptingParameterEnumerationChoiceCollection>
    --> IScriptingParameter<IScriptingParameter>
    --> IScriptingParameterCollection<IScriptingParameterCollection>
    --> IScriptingCalcObject<IScriptingCalcObject>
    --> IScriptingCalcObjectCollection<IScriptingCalcObjectCollection>
    --> IScriptingTool<IScriptingTool>
    --> IElement<IElement>
    --> ISpacecraftParameters<ISpacecraftParameters>
    --> IFuelTank<IFuelTank>
    --> IMissionControlSequenceSegmentProperties<IMissionControlSequenceSegmentProperties>
    --> IMissionControlSequenceEnd<IMissionControlSequenceEnd>
    --> IMissionControlSequenceInitialState<IMissionControlSequenceInitialState>
    --> IMissionControlSequenceSegment<IMissionControlSequenceSegment>
    --> IMissionControlSequenceOptions<IMissionControlSequenceOptions>
    --> IDriverMissionControlSequence<IDriverMissionControlSequence>
    --> IElementCartesian<IElementCartesian>
    --> IElementKeplerian<IElementKeplerian>
    --> IElementDelaunay<IElementDelaunay>
    --> IElementEquinoctial<IElementEquinoctial>
    --> IElementMixedSpherical<IElementMixedSpherical>
    --> IElementSpherical<IElementSpherical>
    --> IElementTargetVectorIncomingAsymptote<IElementTargetVectorIncomingAsymptote>
    --> IElementTargetVectorOutgoingAsymptote<IElementTargetVectorOutgoingAsymptote>
    --> IElementGeodetic<IElementGeodetic>
    --> IElementBPlane<IElementBPlane>
    --> IElementSphericalRangeRate<IElementSphericalRangeRate>
    --> IStoppingCondition<IStoppingCondition>
    --> ILightingStoppingCondition<ILightingStoppingCondition>
    --> IAccessStoppingCondition<IAccessStoppingCondition>
    --> IMissionControlSequencePropagate<IMissionControlSequencePropagate>
    --> IMissionControlSequenceSequence<IMissionControlSequenceSequence>
    --> IMissionControlSequenceBackwardSequence<IMissionControlSequenceBackwardSequence>
    --> IMissionControlSequenceLaunch<IMissionControlSequenceLaunch>
    --> IDisplaySystemGeodetic<IDisplaySystemGeodetic>
    --> IDisplaySystemGeocentric<IDisplaySystemGeocentric>
    --> IBurnoutCBFCartesian<IBurnoutCBFCartesian>
    --> IBurnoutGeodetic<IBurnoutGeodetic>
    --> IBurnoutGeocentric<IBurnoutGeocentric>
    --> IBurnoutLaunchAzAltitude<IBurnoutLaunchAzAltitude>
    --> IBurnoutLaunchAzRadius<IBurnoutLaunchAzRadius>
    --> IMissionControlSequenceFollow<IMissionControlSequenceFollow>
    --> IMissionControlSequenceManeuver<IMissionControlSequenceManeuver>
    --> IManeuverFinite<IManeuverFinite>
    --> IManeuverImpulsive<IManeuverImpulsive>
    --> IAttitudeControlImpulsiveVelocityVector<IAttitudeControlImpulsiveVelocityVector>
    --> IAttitudeControlImpulsiveAntiVelocityVector<IAttitudeControlImpulsiveAntiVelocityVector>
    --> IAttitudeControlImpulsiveAttitude<IAttitudeControlImpulsiveAttitude>
    --> IAttitudeControlImpulsiveFile<IAttitudeControlImpulsiveFile>
    --> IAttitudeControlImpulsiveThrustVector<IAttitudeControlImpulsiveThrustVector>
    --> IAttitudeControlFiniteAntiVelocityVector<IAttitudeControlFiniteAntiVelocityVector>
    --> IAttitudeControlFiniteAttitude<IAttitudeControlFiniteAttitude>
    --> IAttitudeControlFiniteFile<IAttitudeControlFiniteFile>
    --> IAttitudeControlFiniteThrustVector<IAttitudeControlFiniteThrustVector>
    --> IAttitudeControlFiniteTimeVarying<IAttitudeControlFiniteTimeVarying>
    --> IAttitudeControlFiniteVelocityVector<IAttitudeControlFiniteVelocityVector>
    --> IAttitudeControlFinitePlugin<IAttitudeControlFinitePlugin>
    --> IAttitudeControlOptimalFiniteLagrange<IAttitudeControlOptimalFiniteLagrange>
    --> IMissionControlSequenceHold<IMissionControlSequenceHold>
    --> IMissionControlSequenceUpdate<IMissionControlSequenceUpdate>
    --> IMissionControlSequenceReturn<IMissionControlSequenceReturn>
    --> IMissionControlSequenceStop<IMissionControlSequenceStop>
    --> IProfile<IProfile>
    --> IProfileCollection<IProfileCollection>
    --> IMissionControlSequenceTargetSequence<IMissionControlSequenceTargetSequence>
    --> IDifferentialCorrectorControl<IDifferentialCorrectorControl>
    --> IDifferentialCorrectorResult<IDifferentialCorrectorResult>
    --> ISearchPluginControl<ISearchPluginControl>
    --> ISearchPluginResult<ISearchPluginResult>
    --> ISearchPluginResultCollection<ISearchPluginResultCollection>
    --> ISearchPluginControlCollection<ISearchPluginControlCollection>
    --> IDifferentialCorrectorControlCollection<IDifferentialCorrectorControlCollection>
    --> IDifferentialCorrectorResultCollection<IDifferentialCorrectorResultCollection>
    --> ITargeterGraphActiveControl<ITargeterGraphActiveControl>
    --> ITargeterGraphResult<ITargeterGraphResult>
    --> ITargeterGraphActiveControlCollection<ITargeterGraphActiveControlCollection>
    --> ITargeterGraphResultCollection<ITargeterGraphResultCollection>
    --> ITargeterGraph<ITargeterGraph>
    --> ITargeterGraphCollection<ITargeterGraphCollection>
    --> IProfileSearchPlugin<IProfileSearchPlugin>
    --> IProfileDifferentialCorrector<IProfileDifferentialCorrector>
    --> IProfileChangeManeuverType<IProfileChangeManeuverType>
    --> IProfileScriptingTool<IProfileScriptingTool>
    --> IProfileChangeReturnSegment<IProfileChangeReturnSegment>
    --> IProfileChangePropagator<IProfileChangePropagator>
    --> IProfileChangeStopSegment<IProfileChangeStopSegment>
    --> IProfileChangeStoppingConditionState<IProfileChangeStoppingConditionState>
    --> IProfileSeedFiniteManeuver<IProfileSeedFiniteManeuver>
    --> IProfileRunOnce<IProfileRunOnce>
    --> IUserVariableDefinition<IUserVariableDefinition>
    --> IUserVariable<IUserVariable>
    --> IUserVariableUpdate<IUserVariableUpdate>
    --> IProfileSNOPTOptimizer<IProfileSNOPTOptimizer>
    --> ISNOPTControl<ISNOPTControl>
    --> ISNOPTResult<ISNOPTResult>
    --> IProfileIPOPTOptimizer<IProfileIPOPTOptimizer>
    --> IIPOPTControl<IIPOPTControl>
    --> IIPOPTResult<IIPOPTResult>
    --> IManeuverOptimalFinite<IManeuverOptimalFinite>
    --> IManeuverOptimalFiniteSteeringNodeElement<IManeuverOptimalFiniteSteeringNodeElement>
    --> IProfileLambertProfile<IProfileLambertProfile>
    --> IProfileLambertSearchProfile<IProfileLambertSearchProfile>
    --> IProfileGoldenSection<IProfileGoldenSection>
    --> IProfileGridSearch<IProfileGridSearch>
    --> ICalcObjectLinkEmbedControlCollection<ICalcObjectLinkEmbedControlCollection>
    --> IProfileBisection<IProfileBisection>
    --> IBisectionControl<IBisectionControl>
    --> IStateCalcHeightAboveTerrain<IStateCalcHeightAboveTerrain>
    --> IStateCalcEpoch<IStateCalcEpoch>
    --> IStateCalcOrbitDelaunayG<IStateCalcOrbitDelaunayG>
    --> IStateCalcOrbitDelaunayH<IStateCalcOrbitDelaunayH>
    --> IStateCalcOrbitDelaunayL<IStateCalcOrbitDelaunayL>
    --> IStateCalcOrbitSemiLatusRectum<IStateCalcOrbitSemiLatusRectum>
    --> IStateCalcJacobiConstant<IStateCalcJacobiConstant>
    --> IStateCalcJacobiOsculating<IStateCalcJacobiOsculating>
    --> IStateCalcCartesianElem<IStateCalcCartesianElem>
    --> IStateCalcCartSTMElem<IStateCalcCartSTMElem>
    --> IStateCalcSTMEigenval<IStateCalcSTMEigenval>
    --> IStateCalcSTMEigenvecElem<IStateCalcSTMEigenvecElem>
    --> IStateCalcEnvironment<IStateCalcEnvironment>
    --> IStateCalcEquinoctialElem<IStateCalcEquinoctialElem>
    --> IStateCalcDamageFlux<IStateCalcDamageFlux>
    --> IStateCalcDamageMassFlux<IStateCalcDamageMassFlux>
    --> IStateCalcMagnitudeFieldDipoleL<IStateCalcMagnitudeFieldDipoleL>
    --> IStateCalcSEETMagnitudeFieldFieldLineSepAngle<IStateCalcSEETMagnitudeFieldFieldLineSepAngle>
    --> IStateCalcImpactFlux<IStateCalcImpactFlux>
    --> IStateCalcImpactMassFlux<IStateCalcImpactMassFlux>
    --> IStateCalcSEETSAAFlux<IStateCalcSEETSAAFlux>
    --> IStateCalcSEETVehTemp<IStateCalcSEETVehTemp>
    --> IStateCalcCloseApproachBearing<IStateCalcCloseApproachBearing>
    --> IStateCalcCloseApproachMagnitude<IStateCalcCloseApproachMagnitude>
    --> IStateCalcCloseApproachTheta<IStateCalcCloseApproachTheta>
    --> IStateCalcCloseApproachX<IStateCalcCloseApproachX>
    --> IStateCalcCloseApproachY<IStateCalcCloseApproachY>
    --> IStateCalcCloseApproachCosBearing<IStateCalcCloseApproachCosBearing>
    --> IStateCalcRelGroundTrackError<IStateCalcRelGroundTrackError>
    --> IStateCalcRelAtAOLMaster<IStateCalcRelAtAOLMaster>
    --> IStateCalcDeltaFromMaster<IStateCalcDeltaFromMaster>
    --> IStateCalcLonDriftRate<IStateCalcLonDriftRate>
    --> IStateCalcMeanEarthLon<IStateCalcMeanEarthLon>
    --> IStateCalcRectifiedLon<IStateCalcRectifiedLon>
    --> IStateCalcTrueLongitude<IStateCalcTrueLongitude>
    --> IStateCalcGeodeticTrueLongitude<IStateCalcGeodeticTrueLongitude>
    --> IStateCalcGeodeticTrueLongitudeAtTimeOfPerigee<IStateCalcGeodeticTrueLongitudeAtTimeOfPerigee>
    --> IStateCalcMeanRightAscension<IStateCalcMeanRightAscension>
    --> IStateCalcGeodeticMeanRightAscension<IStateCalcGeodeticMeanRightAscension>
    --> IStateCalcTwoBodyDriftRate<IStateCalcTwoBodyDriftRate>
    --> IStateCalcDriftRateFactor<IStateCalcDriftRateFactor>
    --> IStateCalcEccentricityX<IStateCalcEccentricityX>
    --> IStateCalcEccentricityY<IStateCalcEccentricityY>
    --> IStateCalcInclinationX<IStateCalcInclinationX>
    --> IStateCalcInclinationY<IStateCalcInclinationY>
    --> IStateCalcUnitAngularMomentumX<IStateCalcUnitAngularMomentumX>
    --> IStateCalcUnitAngularMomentumY<IStateCalcUnitAngularMomentumY>
    --> IStateCalcUnitAngularMomentumZ<IStateCalcUnitAngularMomentumZ>
    --> IStateCalcGeodeticElem<IStateCalcGeodeticElem>
    --> IStateCalcRepeatingGroundTrackErr<IStateCalcRepeatingGroundTrackErr>
    --> IStateCalcAltitudeOfApoapsis<IStateCalcAltitudeOfApoapsis>
    --> IStateCalcAltitudeOfPeriapsis<IStateCalcAltitudeOfPeriapsis>
    --> IStateCalcArgOfLat<IStateCalcArgOfLat>
    --> IStateCalcArgOfPeriapsis<IStateCalcArgOfPeriapsis>
    --> IStateCalcEccentricityAnomaly<IStateCalcEccentricityAnomaly>
    --> IStateCalcEccentricity<IStateCalcEccentricity>
    --> IStateCalcInclination<IStateCalcInclination>
    --> IStateCalcLonOfAscNode<IStateCalcLonOfAscNode>
    --> IStateCalcMeanAnomaly<IStateCalcMeanAnomaly>
    --> IStateCalcMeanMotion<IStateCalcMeanMotion>
    --> IStateCalcOrbitPeriod<IStateCalcOrbitPeriod>
    --> IStateCalcNumRevs<IStateCalcNumRevs>
    --> IStateCalcRAAN<IStateCalcRAAN>
    --> IStateCalcRadOfApoapsis<IStateCalcRadOfApoapsis>
    --> IStateCalcRadOfPeriapsis<IStateCalcRadOfPeriapsis>
    --> IStateCalcSemiMajorAxis<IStateCalcSemiMajorAxis>
    --> IStateCalcTimePastAscNode<IStateCalcTimePastAscNode>
    --> IStateCalcTimePastPeriapsis<IStateCalcTimePastPeriapsis>
    --> IStateCalcDeltaV<IStateCalcDeltaV>
    --> IStateCalcDeltaVSquared<IStateCalcDeltaVSquared>
    --> IStateCalcMissionControlSequenceDeltaV<IStateCalcMissionControlSequenceDeltaV>
    --> IStateCalcMissionControlSequenceDeltaVSquared<IStateCalcMissionControlSequenceDeltaVSquared>
    --> IStateCalcSequenceDeltaV<IStateCalcSequenceDeltaV>
    --> IStateCalcSequenceDeltaVSquared<IStateCalcSequenceDeltaVSquared>
    --> IStateCalcFuelMass<IStateCalcFuelMass>
    --> IStateCalcDensity<IStateCalcDensity>
    --> IStateCalcInertialDeltaVMagnitude<IStateCalcInertialDeltaVMagnitude>
    --> IStateCalcInertialDeltaVx<IStateCalcInertialDeltaVx>
    --> IStateCalcInertialDeltaVy<IStateCalcInertialDeltaVy>
    --> IStateCalcInertialDeltaVz<IStateCalcInertialDeltaVz>
    --> IStateCalcManeuverSpecificImpulse<IStateCalcManeuverSpecificImpulse>
    --> IStateCalcPressure<IStateCalcPressure>
    --> IStateCalcTemperature<IStateCalcTemperature>
    --> IStateCalcVectorX<IStateCalcVectorX>
    --> IStateCalcVectorY<IStateCalcVectorY>
    --> IStateCalcVectorZ<IStateCalcVectorZ>
    --> IStateCalcMass<IStateCalcMass>
    --> IStateCalcManeuverTotalMassFlowRate<IStateCalcManeuverTotalMassFlowRate>
    --> IStateCalcAbsoluteValue<IStateCalcAbsoluteValue>
    --> IStateCalcDifference<IStateCalcDifference>
    --> IStateCalcDifferenceOtherSegment<IStateCalcDifferenceOtherSegment>
    --> IStateCalcPositionDifferenceOtherSegment<IStateCalcPositionDifferenceOtherSegment>
    --> IStateCalcVelDifferenceOtherSegment<IStateCalcVelDifferenceOtherSegment>
    --> IStateCalcPositionVelDifferenceOtherSegment<IStateCalcPositionVelDifferenceOtherSegment>
    --> IStateCalcValueAtSegment<IStateCalcValueAtSegment>
    --> IStateCalcMaxValue<IStateCalcMaxValue>
    --> IStateCalcMinValue<IStateCalcMinValue>
    --> IStateCalcMeanValue<IStateCalcMeanValue>
    --> IStateCalcMedianValue<IStateCalcMedianValue>
    --> IStateCalcStandardDeviation<IStateCalcStandardDeviation>
    --> IStateCalcNegative<IStateCalcNegative>
    --> IStateCalcTrueAnomaly<IStateCalcTrueAnomaly>
    --> IBDotRCalc<IBDotRCalc>
    --> IBDotTCalc<IBDotTCalc>
    --> IBMagnitudeCalc<IBMagnitudeCalc>
    --> IBThetaCalc<IBThetaCalc>
    --> IStateCalcDeltaDec<IStateCalcDeltaDec>
    --> IStateCalcDeltaRA<IStateCalcDeltaRA>
    --> IStateCalcBetaAngle<IStateCalcBetaAngle>
    --> IStateCalcLocalApparentSolarLon<IStateCalcLocalApparentSolarLon>
    --> IStateCalcLonOfPeriapsis<IStateCalcLonOfPeriapsis>
    --> IStateCalcOrbitStateValue<IStateCalcOrbitStateValue>
    --> IStateCalcSignedEccentricity<IStateCalcSignedEccentricity>
    --> IStateCalcTrueLon<IStateCalcTrueLon>
    --> IStateCalcPower<IStateCalcPower>
    --> IStateCalcRelMotion<IStateCalcRelMotion>
    --> IStateCalcSolarBetaAngle<IStateCalcSolarBetaAngle>
    --> IStateCalcSolarInPlaneAngle<IStateCalcSolarInPlaneAngle>
    --> IStateCalcRelPositionDecAngle<IStateCalcRelPositionDecAngle>
    --> IStateCalcRelPositionInPlaneAngle<IStateCalcRelPositionInPlaneAngle>
    --> IStateCalcRelativeInclination<IStateCalcRelativeInclination>
    --> IStateCalcCurvilinearRelMotion<IStateCalcCurvilinearRelMotion>
    --> IStateCalcCustomFunction<IStateCalcCustomFunction>
    --> IStateCalcScript<IStateCalcScript>
    --> IStateCalcCd<IStateCalcCd>
    --> IStateCalcCr<IStateCalcCr>
    --> IStateCalcDragArea<IStateCalcDragArea>
    --> IStateCalcRadiationPressureArea<IStateCalcRadiationPressureArea>
    --> IStateCalcRadiationPressureCoefficient<IStateCalcRadiationPressureCoefficient>
    --> IStateCalcSRPArea<IStateCalcSRPArea>
    --> IStateCalcCosOfVerticalFPA<IStateCalcCosOfVerticalFPA>
    --> IStateCalcDec<IStateCalcDec>
    --> IStateCalcFPA<IStateCalcFPA>
    --> IStateCalcRMagnitude<IStateCalcRMagnitude>
    --> IStateCalcRA<IStateCalcRA>
    --> IStateCalcVMagnitude<IStateCalcVMagnitude>
    --> IStateCalcVelAz<IStateCalcVelAz>
    --> IStateCalcC3Energy<IStateCalcC3Energy>
    --> IStateCalcInAsympDec<IStateCalcInAsympDec>
    --> IStateCalcInAsympRA<IStateCalcInAsympRA>
    --> IStateCalcInVelAzAtPeriapsis<IStateCalcInVelAzAtPeriapsis>
    --> IStateCalcOutAsympDec<IStateCalcOutAsympDec>
    --> IStateCalcOutAsympRA<IStateCalcOutAsympRA>
    --> IStateCalcOutVelAzAtPeriapsis<IStateCalcOutVelAzAtPeriapsis>
    --> IStateCalcDuration<IStateCalcDuration>
    --> IStateCalcUserValue<IStateCalcUserValue>
    --> IStateCalcVectorGeometryToolAngle<IStateCalcVectorGeometryToolAngle>
    --> IStateCalcAngle<IStateCalcAngle>
    --> IStateCalcDotProduct<IStateCalcDotProduct>
    --> IStateCalcVectorDec<IStateCalcVectorDec>
    --> IStateCalcVectorMagnitude<IStateCalcVectorMagnitude>
    --> IStateCalcVectorRA<IStateCalcVectorRA>
    --> IStateCalcOnePointAccess<IStateCalcOnePointAccess>
    --> IStateCalcDifferenceAcrossSegmentsOtherSat<IStateCalcDifferenceAcrossSegmentsOtherSat>
    --> IStateCalcValueAtSegmentOtherSat<IStateCalcValueAtSegmentOtherSat>
    --> IStateCalcRARate<IStateCalcRARate>
    --> IStateCalcDecRate<IStateCalcDecRate>
    --> IStateCalcRangeRate<IStateCalcRangeRate>
    --> IStateCalcGravitationalParameter<IStateCalcGravitationalParameter>
    --> IStateCalcReferenceRadius<IStateCalcReferenceRadius>
    --> IStateCalcGravCoeff<IStateCalcGravCoeff>
    --> IStateCalcSpeedOfLight<IStateCalcSpeedOfLight>
    --> IStateCalcPi<IStateCalcPi>
    --> IStateCalcScalar<IStateCalcScalar>
    --> IStateCalcApparentSolarTime<IStateCalcApparentSolarTime>
    --> IStateCalcEarthMeanSolarTime<IStateCalcEarthMeanSolarTime>
    --> IStateCalcEarthMeanLocTimeAN<IStateCalcEarthMeanLocTimeAN>
    --> ICentralBodyCollection<ICentralBodyCollection>
    --> ICentralBodyEphemeris<ICentralBodyEphemeris>
    --> ICentralBodyGravityModel<ICentralBodyGravityModel>
    --> ICentralBodyShape<ICentralBodyShape>
    --> ICentralBodyShapeSphere<ICentralBodyShapeSphere>
    --> ICentralBodyShapeOblateSpheroid<ICentralBodyShapeOblateSpheroid>
    --> ICentralBodyShapeTriaxialEllipsoid<ICentralBodyShapeTriaxialEllipsoid>
    --> ICentralBodyAttitude<ICentralBodyAttitude>
    --> ICentralBodyAttitudeRotationCoefficientsFile<ICentralBodyAttitudeRotationCoefficientsFile>
    --> ICentralBodyAttitudeIAU1994<ICentralBodyAttitudeIAU1994>
    --> ICentralBodyEphemerisAnalyticOrbit<ICentralBodyEphemerisAnalyticOrbit>
    --> ICentralBodyEphemerisJPLSpice<ICentralBodyEphemerisJPLSpice>
    --> ICentralBodyEphemerisFile<ICentralBodyEphemerisFile>
    --> ICentralBodyEphemerisJPLDesignExplorerOptimizer<ICentralBodyEphemerisJPLDesignExplorerOptimizer>
    --> ICentralBodyEphemerisPlanetary<ICentralBodyEphemerisPlanetary>
    --> IAstrogatorCentralBody<IAstrogatorCentralBody>
    --> IPowerInternal<IPowerInternal>
    --> IPowerProcessed<IPowerProcessed>
    --> IPowerSolarArray<IPowerSolarArray>
    --> IGeneralRelativityFunction<IGeneralRelativityFunction>
    --> IStateTransformationFunction<IStateTransformationFunction>
    --> ICR3BPFunc<ICR3BPFunc>
    --> IER3BPFunc<IER3BPFunc>
    --> IRadiationPressureFunction<IRadiationPressureFunction>
    --> IYarkovskyFunc<IYarkovskyFunc>
    --> IBlendedDensity<IBlendedDensity>
    --> IDragModelPlugin<IDragModelPlugin>
    --> ICira72Function<ICira72Function>
    --> IExponential<IExponential>
    --> IHarrisPriester<IHarrisPriester>
    --> IDensityModelPlugin<IDensityModelPlugin>
    --> IJacchiaRoberts<IJacchiaRoberts>
    --> IJacchiaBowman2008<IJacchiaBowman2008>
    --> IJacchia_1960<IJacchia_1960>
    --> IJacchia_1970<IJacchia_1970>
    --> IJacchia_1971<IJacchia_1971>
    --> IMSISE_1990<IMSISE_1990>
    --> IMSIS_1986<IMSIS_1986>
    --> INRLMSISE_2000<INRLMSISE_2000>
    --> IUS_Standard_Atmosphere<IUS_Standard_Atmosphere>
    --> IMarsGRAM37<IMarsGRAM37>
    --> IMarsGRAM2005<IMarsGRAM2005>
    --> IVenusGRAM2005<IVenusGRAM2005>
    --> IMarsGRAM2010<IMarsGRAM2010>
    --> IMarsGRAM2001<IMarsGRAM2001>
    --> IMarsGRAM2000<IMarsGRAM2000>
    --> IDTM2012<IDTM2012>
    --> IDTM2020<IDTM2020>
    --> IGravityFieldFunction<IGravityFieldFunction>
    --> IPointMassFunction<IPointMassFunction>
    --> ITwoBodyFunction<ITwoBodyFunction>
    --> IHPOPPluginFunction<IHPOPPluginFunction>
    --> IEOMFuncPluginFunction<IEOMFuncPluginFunction>
    --> ISRPAeroT20<ISRPAeroT20>
    --> ISRPAeroT30<ISRPAeroT30>
    --> ISRPGSPM04aIIA<ISRPGSPM04aIIA>
    --> ISRPGSPM04aIIR<ISRPGSPM04aIIR>
    --> ISRPGSPM04aeIIA<ISRPGSPM04aeIIA>
    --> ISRPGSPM04aeIIR<ISRPGSPM04aeIIR>
    --> ISRPSpherical<ISRPSpherical>
    --> ISRPNPlate<ISRPNPlate>
    --> ISRPTabAreaVec<ISRPTabAreaVec>
    --> ISRPVariableArea<ISRPVariableArea>
    --> IThirdBodyFunction<IThirdBodyFunction>
    --> ISRPReflectionPlugin<ISRPReflectionPlugin>
    --> IEngineModelThrustCoefficients<IEngineModelThrustCoefficients>
    --> IEngineModelIspCoefficients<IEngineModelIspCoefficients>
    --> IEngineConstAcc<IEngineConstAcc>
    --> IEngineConstant<IEngineConstant>
    --> IEngineDefinition<IEngineDefinition>
    --> IEngineThrottleTable<IEngineThrottleTable>
    --> IEngineIon<IEngineIon>
    --> IEngineCustom<IEngineCustom>
    --> IEnginePlugin<IEnginePlugin>
    --> IEngineModelPoly<IEngineModelPoly>
    --> IDesignCR3BPObjectCollection<IDesignCR3BPObjectCollection>
    --> IDesignER3BPObjectCollection<IDesignER3BPObjectCollection>
    --> IDesignCR3BPSetup<IDesignCR3BPSetup>
    --> IDesignCR3BPObject<IDesignCR3BPObject>
    --> IDesignER3BPSetup<IDesignER3BPSetup>
    --> IDesignER3BPObject<IDesignER3BPObject>
    --> IThruster<IThruster>
    --> IThrusterSetCollection<IThrusterSetCollection>
    --> IThrusterSet<IThrusterSet>
    --> IAsTriggerCondition<IAsTriggerCondition>
    --> ICustomFunctionScriptEngine<ICustomFunctionScriptEngine>
    --> INumericalIntegrator<INumericalIntegrator>
    --> IPropagatorFunctionCollection<IPropagatorFunctionCollection>
    --> INumericalPropagatorWrapper<INumericalPropagatorWrapper>
    --> INumericalPropagatorWrapperCR3BP<INumericalPropagatorWrapperCR3BP>
    --> IBulirschStoerIntegrator<IBulirschStoerIntegrator>
    --> IGaussJacksonIntegrator<IGaussJacksonIntegrator>
    --> IRungeKutta2nd3rd<IRungeKutta2nd3rd>
    --> IRungeKutta4th<IRungeKutta4th>
    --> IRungeKutta4th5th<IRungeKutta4th5th>
    --> IRungeKutta4thAdapt<IRungeKutta4thAdapt>
    --> IRungeKuttaF7th8th<IRungeKuttaF7th8th>
    --> IRungeKuttaV8th9th<IRungeKuttaV8th9th>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> DriverMissionControlSequence<>
    --> MissionControlSequenceSegmentCollection<>
    --> MissionControlSequenceEnd<>
    --> MissionControlSequenceInitialState<>
    --> SpacecraftParameters<>
    --> FuelTank<>
    --> ElementCartesian<>
    --> ElementKeplerian<>
    --> ElementEquinoctial<>
    --> ElementDelaunay<>
    --> ElementMixedSpherical<>
    --> ElementSpherical<>
    --> ElementTargetVectorIncomingAsymptote<>
    --> ElementTargetVectorOutgoingAsymptote<>
    --> ElementGeodetic<>
    --> ElementBPlane<>
    --> ElementSphericalRangeRate<>
    --> MissionControlSequencePropagate<>
    --> State<>
    --> StoppingConditionCollection<>
    --> AccessStoppingCondition<>
    --> LightingStoppingCondition<>
    --> StoppingCondition<>
    --> StoppingConditionElement<>
    --> MissionControlSequenceSequence<>
    --> MissionControlSequenceBackwardSequence<>
    --> MissionControlSequenceLaunch<>
    --> DisplaySystemGeodetic<>
    --> DisplaySystemGeocentric<>
    --> BurnoutGeodetic<>
    --> BurnoutCBFCartesian<>
    --> BurnoutGeocentric<>
    --> BurnoutLaunchAzAltitude<>
    --> BurnoutLaunchAzRadius<>
    --> BurnoutVelocity<>
    --> MissionControlSequenceFollow<>
    --> MissionControlSequenceManeuver<>
    --> ManeuverFinite<>
    --> ManeuverImpulsive<>
    --> AttitudeControlImpulsiveVelocityVector<>
    --> AttitudeControlImpulsiveAntiVelocityVector<>
    --> AttitudeControlImpulsiveAttitude<>
    --> AttitudeControlImpulsiveFile<>
    --> AttitudeControlImpulsiveThrustVector<>
    --> AttitudeControlFiniteAntiVelocityVector<>
    --> AttitudeControlFiniteAttitude<>
    --> AttitudeControlFiniteFile<>
    --> AttitudeControlFiniteThrustVector<>
    --> AttitudeControlFiniteTimeVarying<>
    --> AttitudeControlFiniteVelocityVector<>
    --> AttitudeControlFinitePlugin<>
    --> AttitudeControlOptimalFiniteLagrange<>
    --> ManeuverFinitePropagator<>
    --> MissionControlSequenceHold<>
    --> MissionControlSequenceUpdate<>
    --> MissionControlSequenceReturn<>
    --> MissionControlSequenceStop<>
    --> MissionControlSequenceTargetSequence<>
    --> ProfileCollection<>
    --> MissionControlSequenceOptions<>
    --> CalcObjectCollection<>
    --> ConstraintCollection<>
    --> PluginProperties<>
    --> ProfileSearchPlugin<>
    --> TargeterGraph<>
    --> TargeterGraphCollection<>
    --> TargeterGraphResultCollection<>
    --> TargeterGraphActiveControlCollection<>
    --> TargeterGraphActiveControl<>
    --> TargeterGraphResult<>
    --> ProfileDifferentialCorrector<>
    --> ProfileScriptingTool<>
    --> DifferentialCorrectorControl<>
    --> DifferentialCorrectorResult<>
    --> DifferentialCorrectorControlCollection<>
    --> DifferentialCorrectorResultCollection<>
    --> SearchPluginControl<>
    --> SearchPluginControlCollection<>
    --> SearchPluginResult<>
    --> SearchPluginResultCollection<>
    --> ProfileChangeManeuverType<>
    --> ProfileChangeReturnSegment<>
    --> ProfileChangePropagator<>
    --> ProfileChangeStopSegment<>
    --> ProfileChangeStoppingConditionState<>
    --> ProfileSeedFiniteManeuver<>
    --> ProfileRunOnce<>
    --> BPlaneCollection<>
    --> StateCalcDamageFlux<>
    --> StateCalcDamageMassFlux<>
    --> StateCalcMagnitudeFieldDipoleL<>
    --> StateCalcSEETMagnitudeFieldFieldLineSepAngle<>
    --> StateCalcImpactFlux<>
    --> StateCalcImpactMassFlux<>
    --> StateCalcSEETSAAFlux<>
    --> StateCalcSEETVehTemp<>
    --> StateCalcEpoch<>
    --> StateCalcJacobiConstant<>
    --> StateCalcJacobiOsculating<>
    --> StateCalcCartesianElem<>
    --> StateCalcCartSTMElem<>
    --> StateCalcSTMEigenval<>
    --> StateCalcSTMEigenvecElem<>
    --> StateCalcEnvironment<>
    --> StateCalcOrbitDelaunayG<>
    --> StateCalcOrbitDelaunayH<>
    --> StateCalcOrbitDelaunayL<>
    --> StateCalcOrbitSemiLatusRectum<>
    --> StateCalcEquinoctialElem<>
    --> StateCalcCloseApproachBearing<>
    --> StateCalcCloseApproachMagnitude<>
    --> StateCalcCloseApproachTheta<>
    --> StateCalcCloseApproachX<>
    --> StateCalcCloseApproachY<>
    --> StateCalcCloseApproachCosBearing<>
    --> StateCalcRelGroundTrackError<>
    --> StateCalcRelAtAOLMaster<>
    --> StateCalcDeltaFromMaster<>
    --> StateCalcLonDriftRate<>
    --> StateCalcMeanEarthLon<>
    --> StateCalcRectifiedLon<>
    --> StateCalcTrueLongitude<>
    --> StateCalcGeodeticTrueLongitude<>
    --> StateCalcGeodeticTrueLongitudeAtTimeOfPerigee<>
    --> StateCalcMeanRightAscension<>
    --> StateCalcGeodeticMeanRightAscension<>
    --> StateCalcTwoBodyDriftRate<>
    --> StateCalcDriftRateFactor<>
    --> StateCalcEccentricityX<>
    --> StateCalcEccentricityY<>
    --> StateCalcInclinationX<>
    --> StateCalcInclinationY<>
    --> StateCalcUnitAngularMomentumX<>
    --> StateCalcUnitAngularMomentumY<>
    --> StateCalcUnitAngularMomentumZ<>
    --> StateCalcHeightAboveTerrain<>
    --> StateCalcGeodeticElem<>
    --> StateCalcRepeatingGroundTrackErr<>
    --> StateCalcAltitudeOfApoapsis<>
    --> StateCalcAltitudeOfPeriapsis<>
    --> StateCalcArgOfLat<>
    --> StateCalcArgOfPeriapsis<>
    --> StateCalcEccentricityAnomaly<>
    --> StateCalcLonOfAscNode<>
    --> StateCalcMeanMotion<>
    --> StateCalcOrbitPeriod<>
    --> StateCalcNumRevs<>
    --> StateCalcRadOfApoapsis<>
    --> StateCalcRadOfPeriapsis<>
    --> StateCalcSemiMajorAxis<>
    --> StateCalcTimePastAscNode<>
    --> StateCalcTimePastPeriapsis<>
    --> StateCalcTrueAnomaly<>
    --> StateCalcDeltaV<>
    --> StateCalcDeltaVSquared<>
    --> StateCalcMissionControlSequenceDeltaV<>
    --> StateCalcMissionControlSequenceDeltaVSquared<>
    --> StateCalcSequenceDeltaV<>
    --> StateCalcSequenceDeltaVSquared<>
    --> StateCalcFuelMass<>
    --> StateCalcDensity<>
    --> StateCalcInertialDeltaVMagnitude<>
    --> StateCalcInertialDeltaVx<>
    --> StateCalcInertialDeltaVy<>
    --> StateCalcInertialDeltaVz<>
    --> StateCalcManeuverSpecificImpulse<>
    --> StateCalcPressure<>
    --> StateCalcTemperature<>
    --> StateCalcVectorY<>
    --> StateCalcVectorZ<>
    --> StateCalcMass<>
    --> StateCalcManeuverTotalMassFlowRate<>
    --> StateCalcAbsoluteValue<>
    --> StateCalcDifference<>
    --> StateCalcDifferenceOtherSegment<>
    --> StateCalcPositionDifferenceOtherSegment<>
    --> StateCalcVelDifferenceOtherSegment<>
    --> StateCalcPositionVelDifferenceOtherSegment<>
    --> StateCalcValueAtSegment<>
    --> StateCalcMaxValue<>
    --> StateCalcMinValue<>
    --> StateCalcMeanValue<>
    --> StateCalcMedianValue<>
    --> StateCalcStandardDeviation<>
    --> StateCalcNegative<>
    --> StateCalcEccentricity<>
    --> StateCalcMeanAnomaly<>
    --> StateCalcRAAN<>
    --> BDotRCalc<>
    --> BDotTCalc<>
    --> BMagnitudeCalc<>
    --> BThetaCalc<>
    --> StateCalcDeltaDec<>
    --> StateCalcDeltaRA<>
    --> StateCalcBetaAngle<>
    --> StateCalcLocalApparentSolarLon<>
    --> StateCalcLonOfPeriapsis<>
    --> StateCalcOrbitStateValue<>
    --> StateCalcSignedEccentricity<>
    --> StateCalcInclination<>
    --> StateCalcTrueLon<>
    --> StateCalcPower<>
    --> StateCalcRelMotion<>
    --> StateCalcSolarBetaAngle<>
    --> StateCalcSolarInPlaneAngle<>
    --> StateCalcRelPositionDecAngle<>
    --> StateCalcRelPositionInPlaneAngle<>
    --> StateCalcRelativeInclination<>
    --> StateCalcCurvilinearRelMotion<>
    --> StateCalcCustomFunction<>
    --> StateCalcScript<>
    --> StateCalcCd<>
    --> StateCalcCr<>
    --> StateCalcDragArea<>
    --> StateCalcRadiationPressureArea<>
    --> StateCalcRadiationPressureCoefficient<>
    --> StateCalcSRPArea<>
    --> StateCalcCosOfVerticalFPA<>
    --> StateCalcDec<>
    --> StateCalcFPA<>
    --> StateCalcRMagnitude<>
    --> StateCalcRA<>
    --> StateCalcVMagnitude<>
    --> StateCalcVelAz<>
    --> StateCalcC3Energy<>
    --> StateCalcInAsympDec<>
    --> StateCalcInAsympRA<>
    --> StateCalcInVelAzAtPeriapsis<>
    --> StateCalcOutAsympDec<>
    --> StateCalcOutAsympRA<>
    --> StateCalcOutVelAzAtPeriapsis<>
    --> StateCalcDuration<>
    --> StateCalcUserValue<>
    --> StateCalcVectorGeometryToolAngle<>
    --> StateCalcAngle<>
    --> StateCalcDotProduct<>
    --> StateCalcVectorDec<>
    --> StateCalcVectorMagnitude<>
    --> StateCalcVectorRA<>
    --> StateCalcVectorX<>
    --> StateCalcOnePointAccess<>
    --> StateCalcDifferenceAcrossSegmentsOtherSat<>
    --> StateCalcValueAtSegmentOtherSat<>
    --> StateCalcRARate<>
    --> StateCalcDecRate<>
    --> StateCalcRangeRate<>
    --> StateCalcGravitationalParameter<>
    --> StateCalcReferenceRadius<>
    --> StateCalcGravCoeff<>
    --> StateCalcSpeedOfLight<>
    --> StateCalcPi<>
    --> StateCalcScalar<>
    --> StateCalcApparentSolarTime<>
    --> StateCalcEarthMeanSolarTime<>
    --> StateCalcEarthMeanLocTimeAN<>
    --> AutomaticSequenceCollection<>
    --> AutomaticSequence<>
    --> CentralBodyCollection<>
    --> AstrogatorCentralBody<>
    --> CentralBodyGravityModel<>
    --> CentralBodyShapeSphere<>
    --> CentralBodyShapeOblateSpheroid<>
    --> CentralBodyShapeTriaxialEllipsoid<>
    --> CentralBodyAttitudeRotationCoefficientsFile<>
    --> CentralBodyAttitudeIAU1994<>
    --> CentralBodyEphemerisAnalyticOrbit<>
    --> CentralBodyEphemerisJPLSpice<>
    --> CentralBodyEphemerisFile<>
    --> CentralBodyEphemerisJPLDesignExplorerOptimizer<>
    --> CentralBodyEphemerisPlanetary<>
    --> MissionControlSequenceSegmentProperties<>
    --> PowerInternal<>
    --> PowerProcessed<>
    --> PowerSolarArray<>
    --> GeneralRelativityFunction<>
    --> StateTransformationFunction<>
    --> CR3BPFunc<>
    --> ER3BPFunc<>
    --> RadiationPressureFunction<>
    --> YarkovskyFunc<>
    --> BlendedDensity<>
    --> Cira72Function<>
    --> Exponential<>
    --> HarrisPriester<>
    --> DensityModelPlugin<>
    --> JacchiaRoberts<>
    --> JacchiaBowman2008<>
    --> Jacchia_1960<>
    --> Jacchia_1970<>
    --> Jacchia_1971<>
    --> MSISE_1990<>
    --> MSIS_1986<>
    --> NRLMSISE_2000<>
    --> US_Standard_Atmosphere<>
    --> MarsGRAM37<>
    --> MarsGRAM2000<>
    --> MarsGRAM2001<>
    --> MarsGRAM2005<>
    --> MarsGRAM2010<>
    --> VenusGRAM2005<>
    --> DTM2012<>
    --> DTM2020<>
    --> GravityFieldFunction<>
    --> PointMassFunction<>
    --> TwoBodyFunction<>
    --> HPOPPluginFunction<>
    --> EOMFuncPluginFunction<>
    --> SRPAeroT20<>
    --> SRPAeroT30<>
    --> SRPGSPM04aIIA<>
    --> SRPGSPM04aIIR<>
    --> SRPGSPM04aeIIA<>
    --> SRPGSPM04aeIIR<>
    --> SRPSpherical<>
    --> SRPNPlate<>
    --> SRPTabAreaVec<>
    --> SRPVariableArea<>
    --> ThirdBodyFunction<>
    --> DragModelPlugin<>
    --> SRPReflectionPlugin<>
    --> EngineConstAcc<>
    --> EngineConstant<>
    --> EngineIon<>
    --> EngineThrottleTable<>
    --> EngineCustom<>
    --> EnginePlugin<>
    --> EngineModelPoly<>
    --> EngineModelThrustCoefficients<>
    --> EngineModelIspCoefficients<>
    --> EngineDefinition<>
    --> DesignCR3BPSetup<>
    --> DesignCR3BPObject<>
    --> DesignCR3BPObjectCollection<>
    --> DesignER3BPSetup<>
    --> DesignER3BPObject<>
    --> DesignER3BPObjectCollection<>
    --> Thruster<>
    --> ThrusterSetCollection<>
    --> ThrusterSet<>
    --> AsTriggerCondition<>
    --> CustomFunctionScriptEngine<>
    --> NumericalPropagatorWrapper<>
    --> NumericalPropagatorWrapperCR3BP<>
    --> PropagatorFunctionCollection<>
    --> BulirschStoerIntegrator<>
    --> GaussJacksonIntegrator<>
    --> RungeKutta2nd3rd<>
    --> RungeKutta4th<>
    --> RungeKutta4th5th<>
    --> RungeKutta4thAdapt<>
    --> RungeKuttaF7th8th<>
    --> RungeKuttaV8th9th<>
    --> ScriptingTool<>
    --> ScriptingSegmentCollection<>
    --> ScriptingSegment<>
    --> ScriptingParameterCollection<>
    --> ScriptingParameter<>
    --> ScriptingCalcObject<>
    --> ScriptingCalcObjectCollection<>
    --> UserVariableDefinition<>
    --> UserVariable<>
    --> UserVariableUpdate<>
    --> UserVariableDefinitionCollection<>
    --> UserVariableCollection<>
    --> UserVariableUpdateCollection<>
    --> CalculationGraphCollection<>
    --> ScriptingParameterEnumerationChoice<>
    --> ScriptingParameterEnumerationChoiceCollection<>
    --> ProfileSNOPTOptimizer<>
    --> SNOPTControl<>
    --> SNOPTResult<>
    --> SNOPTControlCollection<>
    --> SNOPTResultCollection<>
    --> ProfileIPOPTOptimizer<>
    --> IPOPTControl<>
    --> IPOPTResult<>
    --> IPOPTControlCollection<>
    --> IPOPTResultCollection<>
    --> ManeuverOptimalFinite<>
    --> ManeuverOptimalFiniteSNOPTOptimizer<>
    --> ManeuverOptimalFiniteInitialBoundaryConditions<>
    --> ManeuverOptimalFiniteFinalBoundaryConditions<>
    --> ManeuverOptimalFinitePathBoundaryConditions<>
    --> ManeuverOptimalFiniteSteeringNodeElement<>
    --> ManeuverOptimalFiniteSteeringNodeCollection<>
    --> ManeuverOptimalFiniteBounds<>
    --> ProfileLambertProfile<>
    --> ProfileLambertSearchProfile<>
    --> ProfileGoldenSection<>
    --> GoldenSectionControlCollection<>
    --> GoldenSectionControl<>
    --> GoldenSectionResultCollection<>
    --> GoldenSectionResult<>
    --> ProfileGridSearch<>
    --> GridSearchControlCollection<>
    --> GridSearchControl<>
    --> GridSearchResultCollection<>
    --> GridSearchResult<>
    --> CalcObjectLinkEmbedControlCollection<>
    --> ProfileBisection<>
    --> BisectionControl<>
    --> BisectionControlCollection<>
    --> BisectionResult<>
    --> BisectionResultCollection<>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ GRAPH_OPTION<GRAPH_OPTION>
    ≔ SMART_RUN_MODE<SMART_RUN_MODE>
    ≔ FORMULATION<FORMULATION>
    ≔ LIGHTING_CONDITION<LIGHTING_CONDITION>
    ≔ PROFILE<PROFILE>
    ≔ ACCESS_CRITERION<ACCESS_CRITERION>
    ≔ ECLIPSING_BODIES_SOURCE<ECLIPSING_BODIES_SOURCE>
    ≔ CRITERION<CRITERION>
    ≔ CALC_OBJECT_REFERENCE<CALC_OBJECT_REFERENCE>
    ≔ CALC_OBJECT_CENTRAL_BODY_REFERENCE<CALC_OBJECT_CENTRAL_BODY_REFERENCE>
    ≔ CALC_OBJECT_ELEM<CALC_OBJECT_ELEM>
    ≔ PROFILE_MODE<PROFILE_MODE>
    ≔ CONTROL_STOPPING_CONDITION<CONTROL_STOPPING_CONDITION>
    ≔ STATE<STATE>
    ≔ RETURN_CONTROL<RETURN_CONTROL>
    ≔ DRAW_PERTURBATION<DRAW_PERTURBATION>
    ≔ DERIVE_CALC_METHOD<DERIVE_CALC_METHOD>
    ≔ CONVERGENCE_CRITERIA<CONVERGENCE_CRITERIA>
    ≔ DIFFERENTIAL_CORRECTOR_SCALING_METHOD<DIFFERENTIAL_CORRECTOR_SCALING_METHOD>
    ≔ CONTROL_UPDATE<CONTROL_UPDATE>
    ≔ CONTROL_FOLLOW<CONTROL_FOLLOW>
    ≔ CONTROL_INIT_STATE<CONTROL_INIT_STATE>
    ≔ CONTROL_MANEUVER<CONTROL_MANEUVER>
    ≔ CONTROL_LAUNCH<CONTROL_LAUNCH>
    ≔ CONTROL_ADVANCED<CONTROL_ADVANCED>
    ≔ TARGET_SEQ_ACTION<TARGET_SEQ_ACTION>
    ≔ PROFILES_FINISH<PROFILES_FINISH>
    ≔ UPDATE_PARAM<UPDATE_PARAM>
    ≔ UPDATE_ACTION<UPDATE_ACTION>
    ≔ PRESSURE_MODE<PRESSURE_MODE>
    ≔ THRUST_TYPE<THRUST_TYPE>
    ≔ ATTITUDE_UPDATE<ATTITUDE_UPDATE>
    ≔ PROPULSION_METHOD<PROPULSION_METHOD>
    ≔ CUSTOM_FUNCTION<CUSTOM_FUNCTION>
    ≔ BODY_AXIS<BODY_AXIS>
    ≔ CONSTRAINT_SIGN<CONSTRAINT_SIGN>
    ≔ ATTITUDE_CONTROL<ATTITUDE_CONTROL>
    ≔ FOLLOW_JOIN<FOLLOW_JOIN>
    ≔ FOLLOW_SEPARATION<FOLLOW_SEPARATION>
    ≔ FOLLOW_SPACECRAFT_AND_FUEL_TANK<FOLLOW_SPACECRAFT_AND_FUEL_TANK>
    ≔ BURNOUT_OPTIONS<BURNOUT_OPTIONS>
    ≔ BURNOUT_TYPE<BURNOUT_TYPE>
    ≔ ASCENT_TYPE<ASCENT_TYPE>
    ≔ LAUNCH_DISPLAY_SYSTEM<LAUNCH_DISPLAY_SYSTEM>
    ≔ RUN_CODE<RUN_CODE>
    ≔ SEQUENCE_STATE_TO_PASS<SEQUENCE_STATE_TO_PASS>
    ≔ MANEUVER_TYPE<MANEUVER_TYPE>
    ≔ SEGMENT_TYPE<SEGMENT_TYPE>
    ≔ ELEMENT_TYPE<ELEMENT_TYPE>
    ≔ LANGUAGE<LANGUAGE>
    ≔ STOPPING_CONDITION<STOPPING_CONDITION>
    ≔ CLEAR_EPHEMERIS_DIRECTION<CLEAR_EPHEMERIS_DIRECTION>
    ≔ PROFILE_INSERT_DIRECTION<PROFILE_INSERT_DIRECTION>
    ≔ ROOT_FINDING_ALGORITHM<ROOT_FINDING_ALGORITHM>
    ≔ SCRIPTING_PARAMETER_TYPE<SCRIPTING_PARAMETER_TYPE>
    ≔ SNOPT_GOAL<SNOPT_GOAL>
    ≔ IPOPT_GOAL<IPOPT_GOAL>
    ≔ OPTIMAL_FINITE_SEED_METHOD<OPTIMAL_FINITE_SEED_METHOD>
    ≔ OPTIMAL_FINITE_RUN_MODE<OPTIMAL_FINITE_RUN_MODE>
    ≔ OPTIMAL_FINITE_DISCRETIZATION_STRATEGY<OPTIMAL_FINITE_DISCRETIZATION_STRATEGY>
    ≔ OPTIMAL_FINITE_WORKING_VARIABLES<OPTIMAL_FINITE_WORKING_VARIABLES>
    ≔ OPTIMAL_FINITE_SCALING_OPTIONS<OPTIMAL_FINITE_SCALING_OPTIONS>
    ≔ OPTIMAL_FINITE_SNOPT_OBJECTIVE<OPTIMAL_FINITE_SNOPT_OBJECTIVE>
    ≔ OPTIMAL_FINITE_SNOPT_SCALING<OPTIMAL_FINITE_SNOPT_SCALING>
    ≔ OPTIMAL_FINITE_EXPORT_NODES_FORMAT<OPTIMAL_FINITE_EXPORT_NODES_FORMAT>
    ≔ OPTIMAL_FINITE_GUESS_METHOD<OPTIMAL_FINITE_GUESS_METHOD>
    ≔ IMP_DELTA_V_REP<IMP_DELTA_V_REP>
    ≔ LAMBERT_TARGET_COORD_TYPE<LAMBERT_TARGET_COORD_TYPE>
    ≔ LAMBERT_SOLUTION_OPTION_TYPE<LAMBERT_SOLUTION_OPTION_TYPE>
    ≔ LAMBERT_ORBITAL_ENERGY_TYPE<LAMBERT_ORBITAL_ENERGY_TYPE>
    ≔ LAMBERT_DIRECTION_OF_MOTION_TYPE<LAMBERT_DIRECTION_OF_MOTION_TYPE>
    ≔ GOLDEN_SECTION_DESIRED_OPERATION<GOLDEN_SECTION_DESIRED_OPERATION>
    ≔ GRID_SEARCH_DESIRED_OPERATION<GRID_SEARCH_DESIRED_OPERATION>
    ≔ ELEMENT<ELEMENT>
    ≔ BASE_SELECTION<BASE_SELECTION>
    ≔ CONTROL_ORBIT_STATE_VALUE<CONTROL_ORBIT_STATE_VALUE>
    ≔ SEGMENT_STATE<SEGMENT_STATE>
    ≔ DIFFERENCE_ORDER<DIFFERENCE_ORDER>
    ≔ SEGMENT_DIFFERENCE_ORDER<SEGMENT_DIFFERENCE_ORDER>
    ≔ CONTROL_REPEATING_GROUND_TRACK_ERR<CONTROL_REPEATING_GROUND_TRACK_ERR>
    ≔ CALC_OBJECT_DIRECTION<CALC_OBJECT_DIRECTION>
    ≔ CALC_OBJECT_ORBIT_PLANE_SOURCE<CALC_OBJECT_ORBIT_PLANE_SOURCE>
    ≔ CALC_OBJECT_SUN_POSITION<CALC_OBJECT_SUN_POSITION>
    ≔ CALC_OBJECT_ANGLE_SIGN<CALC_OBJECT_ANGLE_SIGN>
    ≔ CALC_OBJECT_REFERENCE_DIRECTION<CALC_OBJECT_REFERENCE_DIRECTION>
    ≔ CALC_OBJECT_RELATIVE_POSITION<CALC_OBJECT_RELATIVE_POSITION>
    ≔ CALC_OBJECT_REFERENCE_ELLIPSE<CALC_OBJECT_REFERENCE_ELLIPSE>
    ≔ CALC_OBJECT_LOCATION_SOURCE<CALC_OBJECT_LOCATION_SOURCE>
    ≔ GRAVITATIONAL_PARAMETER_SOURCE<GRAVITATIONAL_PARAMETER_SOURCE>
    ≔ REFERENCE_RADIUS_SOURCE<REFERENCE_RADIUS_SOURCE>
    ≔ GRAV_COEFF_NORMALIZATION_TYPE<GRAV_COEFF_NORMALIZATION_TYPE>
    ≔ GRAV_COEFF_COEFFICIENT_TYPE<GRAV_COEFF_COEFFICIENT_TYPE>
    ≔ STM_PERT_VARIABLES<STM_PERT_VARIABLES>
    ≔ STM_EIGEN_NUMBER<STM_EIGEN_NUMBER>
    ≔ COMPLEX_NUMBER<COMPLEX_NUMBER>
    ≔ SQUARED_TYPE<SQUARED_TYPE>
    ≔ GEO_STATIONARY_DRIFT_RATE_MODEL<GEO_STATIONARY_DRIFT_RATE_MODEL>
    ≔ GEO_STATIONARY_INCLINATION_MAGNITUDE<GEO_STATIONARY_INCLINATION_MAGNITUDE>
    ≔ CENTRAL_BODY_GRAVITY_MODEL<CENTRAL_BODY_GRAVITY_MODEL>
    ≔ CENTRAL_BODY_SHAPE<CENTRAL_BODY_SHAPE>
    ≔ CENTRAL_BODY_ATTITUDE<CENTRAL_BODY_ATTITUDE>
    ≔ CENTRAL_BODY_EPHEMERIS<CENTRAL_BODY_EPHEMERIS>
    ≔ CONTROL_POWER_INTERNAL<CONTROL_POWER_INTERNAL>
    ≔ CONTROL_POWER_PROCESSED<CONTROL_POWER_PROCESSED>
    ≔ CONTROL_POWER_SOLAR_ARRAY<CONTROL_POWER_SOLAR_ARRAY>
    ≔ THIRD_BODY_MODE<THIRD_BODY_MODE>
    ≔ GRAV_PARAM_SOURCE<GRAV_PARAM_SOURCE>
    ≔ EPHEM_SOURCE<EPHEM_SOURCE>
    ≔ SOLAR_FORCE_METHOD<SOLAR_FORCE_METHOD>
    ≔ SHADOW_MODEL<SHADOW_MODEL>
    ≔ SUN_POSITION<SUN_POSITION>
    ≔ ATMOS_DATA_SOURCE<ATMOS_DATA_SOURCE>
    ≔ GEO_MAGNETIC_FLUX_SOURCE<GEO_MAGNETIC_FLUX_SOURCE>
    ≔ GEO_MAGNETIC_FLUX_UPDATE_RATE<GEO_MAGNETIC_FLUX_UPDATE_RATE>
    ≔ DRAG_MODEL_TYPE<DRAG_MODEL_TYPE>
    ≔ MARS_GRAM_DENSITY_TYPE<MARS_GRAM_DENSITY_TYPE>
    ≔ VENUS_GRAM_DENSITY_TYPE<VENUS_GRAM_DENSITY_TYPE>
    ≔ TAB_VEC_INTERP_METHOD<TAB_VEC_INTERP_METHOD>
    ≔ CONTROL_ENGINE_CONST_ACC<CONTROL_ENGINE_CONST_ACC>
    ≔ CONTROL_ENGINE_CONSTANT<CONTROL_ENGINE_CONSTANT>
    ≔ CONTROL_ENGINE_CUSTOM<CONTROL_ENGINE_CUSTOM>
    ≔ CONTROL_ENGINE_THROTTLE_TABLE<CONTROL_ENGINE_THROTTLE_TABLE>
    ≔ CONTROL_ENGINE_ION<CONTROL_ENGINE_ION>
    ≔ CONTROL_ENGINE_MODEL_POLY<CONTROL_ENGINE_MODEL_POLY>
    ≔ ENGINE_MODEL_FUNCTION<ENGINE_MODEL_FUNCTION>
    ≔ THROTTLE_TABLE_OPERATION_MODE<THROTTLE_TABLE_OPERATION_MODE>
    ≔ IDEAL_ORBIT_RADIUS<IDEAL_ORBIT_RADIUS>
    ≔ ROTATING_COORDINATE_SYSTEM<ROTATING_COORDINATE_SYSTEM>
    ≔ CONTROL_THRUSTERS<CONTROL_THRUSTERS>
    ≔ THRUSTER_DIRECTION<THRUSTER_DIRECTION>
    ≔ CRITERIA<CRITERIA>
    ≔ ERROR_CONTROL<ERROR_CONTROL>
    ≔ PREDICTOR_CORRECTOR<PREDICTOR_CORRECTOR>
    ≔ NUMERICAL_INTEGRATOR<NUMERICAL_INTEGRATOR>
    ≔ COEFF_RUNGE_KUTTA_V_8TH_9TH<COEFF_RUNGE_KUTTA_V_8TH_9TH>

