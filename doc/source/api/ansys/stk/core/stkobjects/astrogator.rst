
The ``astrogator`` module
=========================


.. py:module:: ansys.stk.core.stkobjects.astrogator


Summary
-------

.. tab-set::

 
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection`
              - The list of User Variables accessed through the Driver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IUserVariableCollection`
              - The list of User Variables accessed through a segment that sets initial conditions.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection`
              - The list of User Variables accessed through an Update segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICalculationGraphCollection`
              - The list of Calculations Graphs to display.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IConstraintCollection`
              - The list of constraints assigned to a stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPluginProperties`
              - Properties of a plugin attitude control.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISNOPTControlCollection`
              - Properties for the list of SNOPT control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResultCollection`
              - SNOPT result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControlCollection`
              - Properties for the list of IPOPT control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IIPOPTResultCollection`
              - IPOPT result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSNOPTOptimizer`
              - Properties of SNOPT Optimizer options for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteInitialBoundaryConditions`
              - Properties of initial boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteFinalBoundaryConditions`
              - Properties of final boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinitePathBoundaryConditions`
              - Properties of path boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeCollection`
              - Steering/nodes collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteBounds`
              - The bounds for boundary interfaces.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControlCollection`
              - Properties for the list of Golden Section control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl`
              - Properties for control parameters of a Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionResultCollection`
              - Properties for the list of Golden Section result parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionResult`
              - Properties for result parameters of a Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection`
              - Properties for the list of Grid Search control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl`
              - Properties for control parameters of a Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection`
              - Properties for the list of Grid Search result parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGridSearchResult`
              - Properties for result parameters of a Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBisectionControlCollection`
              - Properties for the list of Bisection control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult`
              - Properties for result parameters of a Bisection profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBisectionResultCollection`
              - Bisection result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStoppingConditionElement`
              - The status of a stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStoppingConditionCollection`
              - The list of Stopping Conditions.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection`
              - Properties for a collection of segments.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IState`
              - Spacecraft Parameters properties for the spacecraft configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStoppingConditionComponent`
              - Properties for a stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequence`
              - Properties for automatic sequences.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAutomaticSequenceCollection`
              - Properties for the Automatic Sequence Browser.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBPlaneCollection`
              - Properties for the collection of B-Planes.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectCollection`
              - Collection of calculation objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverFinitePropagator`
              - Properties for the propagation of a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity`
              - Properties for the burnout velocity of a Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`
              - Properties for attitude options for a maneuver segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinite`
              - The attitude control of a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsive`
              - The attitude control of an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlOptimalFinite`
              - The attitude control of a optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuver`
              - Properties of an Impulsive Maneuver Segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDisplaySystem`
              - The launch coordinate system.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnout`
              - The burnout point reference frame.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegment`
              - Object properties for scripting options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection`
              - The list of object properties that the script can interact with.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoice`
              - Enumeration choice.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection`
              - The list of enumeration choices available when parameter type is Enumeration.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameter`
              - Parameter properties for scripting options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection`
              - The list of parameters that the script can interact with.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObject`
              - Calc Object properties for scripting options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection`
              - The list of calc objects that the script can interact with.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IScriptingTool`
              - Properties for the Scripting Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElement`
              - The elements of the selected coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters`
              - Properties for spacecraft configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IFuelTank`
              - Properties for fuel tank configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentProperties`
              - The segment properties.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceEnd`
              - Properties for an End segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceInitialState`
              - Properties for an Initial State segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment`
              - General properties for segments.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceOptions`
              - Properties for the MCS Options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDriverMissionControlSequence`
              - Properties for the Mission Control Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementCartesian`
              - Properties for Cartesian elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian`
              - Properties for Keplerian elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay`
              - Properties for Delaunay elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementEquinoctial`
              - Properties for Equinoctial elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical`
              - Properties for Mixed Spherical elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementSpherical`
              - Properties for Spherical elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementTargetVectorIncomingAsymptote`
              - Properties for Target Vector Incoming Asymptote elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementTargetVectorOutgoingAsymptote`
              - Properties for Target Vector Outgoing Asymptote elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic`
              - Properties for Geodetic elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementBPlane`
              - Properties for BPlane elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElementSphericalRangeRate`
              - Properties for Spherical Range Rate elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStoppingCondition`
              - Basic properties for a stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ILightingStoppingCondition`
              - Properties for a lighting stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAccessStoppingCondition`
              - Properties for an access stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequencePropagate`
              - Properties for a Propagate segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSequence`
              - Properties for a Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceBackwardSequence`
              - Properties for a Backward Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch`
              - Properties for a Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDisplaySystemGeodetic`
              - Properties for a geodetic launch coordinate system.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDisplaySystemGeocentric`
              - Properties for a geocentric launch coordinate system.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnoutCBFCartesian`
              - Properties for a Cartesian CBF burnout state definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnoutGeodetic`
              - Properties for a geodetic burnout point definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnoutGeocentric`
              - {Properties for a geocentric burnout point definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnoutLaunchAzAltitude`
              - Properties for a launch azimuth / altitude burnout point definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnoutLaunchAzRadius`
              - Properties for a launch azimuth / radius burnout point definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceFollow`
              - Properties for a Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceManeuver`
              - General properties for a Maneuver segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverFinite`
              - Engine properties for a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverImpulsive`
              - Properties for an Impulsive Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveVelocityVector`
              - Properties for the Velocity Vector attitude control for an Impulsive Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveAntiVelocityVector`
              - Properties for the Anti-Velocity Vector attitude control for an Impulsive Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveAttitude`
              - Properties for the Attitude attitude control for an Impulsive Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile`
              - Properties for the File attitude control for an Impulsive Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector`
              - Properties for the Thrust Vector attitude control for an Impulsive Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAntiVelocityVector`
              - Properties for the Anti-Velocity Vector attitude control for a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAttitude`
              - Properties for the Attitude attitude control for a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteFile`
              - Properties for the File attitude control for a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector`
              - Properties for the Thrust Vector attitude control for a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying`
              - Properties for the Time Varying attitude control for a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteVelocityVector`
              - Properties for the Velocity Vector attitude control for a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinitePlugin`
              - Properties for the Plugin attitude control for a Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlOptimalFiniteLagrange`
              - Properties for the Lagrange Interpolation attitude control for a Optimal Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceHold`
              - Properties for a Hold segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceUpdate`
              - Properties for an Update segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceReturn`
              - Properties for a Return segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceStop`
              - Properties for a Stop segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`
              - General properties for target sequence profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection`
              - Properties for a list of target sequence profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceTargetSequence`
              - General properties of a TargetSequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorControl`
              - Properties for control parameters of a differential corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResult`
              - Properties for equality constraints of a differential corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl`
              - Properties of search plugin control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult`
              - Properties of search plugin equality constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection`
              - Properties for the list of search plugin equality constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControlCollection`
              - Properties for the list of search plugin control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorControlCollection`
              - Properties for the list of control parameters for a differential corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDifferentialCorrectorResultCollection`
              - Differential Corrector result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControl`
              - Properties for targeter graph active control.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphResult`
              - Properties for targeter graph result.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphActiveControlCollection`
              - Targeter graph active controls.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphResultCollection`
              - Targeter graph results.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraph`
              - Properties for a Targeter Graph.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection`
              - The list of User Variables accessed through the Driver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin`
              - Properties of a plugin search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector`
              - Properties for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeManeuverType`
              - Properties for a Change Maneuver Type profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileScriptingTool`
              - Properties for a Scripting Tool profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeReturnSegment`
              - Properties for a Change Return Segment profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileChangePropagator`
              - Properties for a Change Propagator profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStopSegment`
              - Properties for a Change Stop Segment profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileChangeStoppingConditionState`
              - Properties for a Change Stopping Condition State profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileSeedFiniteManeuver`
              - Properties for a Seed Finite Maneuver segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileRunOnce`
              - Properties for a Run Once profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinition`
              - Properties for a User Variable definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IUserVariable`
              - The properties for a User Variable initial value.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IUserVariableUpdate`
              - Properties for a User Variable update.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer`
              - Properties of SNOPT Optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISNOPTControl`
              - Properties for control parameters of a SNOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISNOPTResult`
              - Properties for objecvtive and constraints of a SNOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer`
              - Properties of IPOPT Optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl`
              - Properties for control parameters of a IPOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IIPOPTResult`
              - Properties for objecvtive and constraints of a IPOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite`
              - Engine properties for a Optimal Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFiniteSteeringNodeElement`
              - The elements of the steering node.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile`
              - Properties for a Lambert profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile`
              - Properties for a Lambert Search Profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection`
              - Properties for a Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileGridSearch`
              - Properties for a Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICalcObjectLinkEmbedControlCollection`
              - Collection of link/embed calculation objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfileBisection`
              - Properties of Single Parameter Bisection profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBisectionControl`
              - Properties for control parameters of a Bisection Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcHeightAboveTerrain`
              - Interface for StateCalcHeightAboveTerrain.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEpoch`
              - Properties for an Epoch calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitDelaunayG`
              - Interface for AsStateCalcOrbitDelaunayG.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitDelaunayH`
              - Interface for AsStateCalcOrbitDelaunayH.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitDelaunayL`
              - Interface for AsStateCalcOrbitDelaunayL.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitSemiLatusRectum`
              - Interface for AsStateCalcOrbitSemiLatusRectum.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcJacobiConstant`
              - Properties for a Jacobi Constant calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcJacobiOsculating`
              - Properties for an osculating Jacobi integral calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCartesianElem`
              - Properties for a Cartesian Element calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCartSTMElem`
              - Properties for a Cartesian STM Element calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenval`
              - Properties for an STM Eigenvalue calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSTMEigenvecElem`
              - Properties for an STM Eigenvector element calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEnvironment`
              - Properties for an Environment calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEquinoctialElem`
              - Properties for an Equinoctial Element calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDamageFlux`
              - Interface for AgAsStateCalcDamageFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDamageMassFlux`
              - Interface for AgAsStateCalcDamageMassFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMagnitudeFieldDipoleL`
              - Interface for AgAsStateCalcMagFieldDipoleL.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSEETMagnitudeFieldFieldLineSepAngle`
              - Properties for a SEETMagFieldFieldLineSepAngle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcImpactFlux`
              - Interface for AgAsStateCalcImpactFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcImpactMassFlux`
              - Interface for AgAsStateCalcImpactMassFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSEETSAAFlux`
              - Interface for AgAsStateCalcSEETSAAFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSEETVehTemp`
              - Interface for AgAsStateCalcSEETVehTemp.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCloseApproachBearing`
              - Properties for a CloseApproachBearing calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCloseApproachMagnitude`
              - Properties for a CloseApproachMagnitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCloseApproachTheta`
              - Properties for a CloseApproachTheta calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCloseApproachX`
              - Properties for a CloseApproachX calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCloseApproachY`
              - Properties for a CloseApproachY calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCloseApproachCosBearing`
              - Properties for a CosineOfCloseApproachBearing calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError`
              - Properties for a RelGroundTrackError calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster`
              - Properties for a RelativeAtAOL calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaFromMaster`
              - Properties for a Rel Mean Mean Anomaly calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcLonDriftRate`
              - Properties for a Longitude Drift Rate calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMeanEarthLon`
              - Properties for a Mean Earth Longitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRectifiedLon`
              - Properties for a RectifiedLon calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcTrueLongitude`
              - Properties for a TrueLongitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcGeodeticTrueLongitude`
              - Properties for a GeodeticTrueLongitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcGeodeticTrueLongitudeAtTimeOfPerigee`
              - Properties for a GeodeticTrueLongitudeAtTimeOfPerigee calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMeanRightAscension`
              - Properties for a MeanRightAscension calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcGeodeticMeanRightAscension`
              - Properties for a GeodeticMeanRightAscension calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcTwoBodyDriftRate`
              - Properties for a TwoBodyDriftRate calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDriftRateFactor`
              - Properties for a DriftRateFactor calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEccentricityX`
              - Properties for a EccentricityX calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEccentricityY`
              - Properties for a EccentricityY calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInclinationX`
              - Properties for a InclinationX calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInclinationY`
              - Properties for a InclinationY calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcUnitAngularMomentumX`
              - Properties for a UnitAngularMomentumX calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcUnitAngularMomentumY`
              - Properties for a UnitAngularMomentumY calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcUnitAngularMomentumZ`
              - Properties for a UnitAngularMomentumZ calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcGeodeticElem`
              - Properties for a Geodetic Element calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRepeatingGroundTrackErr`
              - Properties for a RepeatingGroundTrackEquatorError calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcAltitudeOfApoapsis`
              - Properties for an Altitude of Apoapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcAltitudeOfPeriapsis`
              - Properties for an Altitude Of Periapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcArgOfLat`
              - Properties for an Argument of Latitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcArgOfPeriapsis`
              - Properties for an Argument of Periapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEccentricityAnomaly`
              - Properties for an Eccentric Anomaly calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEccentricity`
              - Properties for an Eccentricity calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInclination`
              - Properties for an Inclination calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcLonOfAscNode`
              - Properties for a Longitude of Ascending Node calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMeanAnomaly`
              - Properties for a MeanAnomaly calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMeanMotion`
              - Properties for a Mean Motion calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitPeriod`
              - Properties for an Orbit Period calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcNumRevs`
              - Properties for a Number of Revolutions calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRAAN`
              - Properties for a RAAN calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRadOfApoapsis`
              - Properties for a Radius Of Apoapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRadOfPeriapsis`
              - Properties for a Radius Of Periapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSemiMajorAxis`
              - Properties for a Semimajor Axis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcTimePastAscNode`
              - Properties for a Time Past Ascending Node calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcTimePastPeriapsis`
              - Properties for a Time Past Periapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaV`
              - Properties for a DeltaV calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaVSquared`
              - Properties for a DeltaV Squared calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMissionControlSequenceDeltaV`
              - Properties for a MCS DeltaV calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMissionControlSequenceDeltaVSquared`
              - Properties for a MCS DeltaV Squared calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSequenceDeltaV`
              - Properties for a Sequence DeltaV calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSequenceDeltaVSquared`
              - Properties for a Sequence DeltaV Squared calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcFuelMass`
              - Properties for a FuelMass calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDensity`
              - Properties for a Fuel Density calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInertialDeltaVMagnitude`
              - Properties for an Inertial DeltaV Magnitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInertialDeltaVx`
              - Properties for an Inertial DeltaVx calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInertialDeltaVy`
              - Properties for an Inertial DeltaVy calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInertialDeltaVz`
              - Properties for an Inertial DeltaVz calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcManeuverSpecificImpulse`
              - Properties for a Specific Impulse calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcPressure`
              - Properties for a Tank Pressure calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcTemperature`
              - Properties for a Tank Temperature calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVectorX`
              - Properties for a Vector X calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVectorY`
              - Properties for a Vector Y calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVectorZ`
              - Properties for a Vector Z calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMass`
              - Properties for a Total Mass calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcManeuverTotalMassFlowRate`
              - Properties for a Total Mass Flow Rate calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcAbsoluteValue`
              - Properties for an Absolute Value calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDifference`
              - Properties for a Difference calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceOtherSegment`
              - Properties for a Difference Across Segments calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcPositionDifferenceOtherSegment`
              - Properties for a Position Difference Across Segments calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVelDifferenceOtherSegment`
              - Properties for a Velocity Difference Across Segments calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcPositionVelDifferenceOtherSegment`
              - Properties for a Position and Velocity Difference Across Segments calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegment`
              - Properties for a Value At Segment calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMaxValue`
              - Properties for a Maximum Value calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMinValue`
              - Properties for a Minimum Value calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMeanValue`
              - Properties for a Mean Value calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcMedianValue`
              - Properties for a Median Value calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcStandardDeviation`
              - Properties for a Standard Deviation calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcNegative`
              - Properties for a Negative calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcTrueAnomaly`
              - Properties for a Mean True Anomaly calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBDotRCalc`
              - Properties for a BDotR calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBDotTCalc`
              - Properties for a BDotT calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBMagnitudeCalc`
              - Properties for a BMagnitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBThetaCalc`
              - Properties for a BTheta calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaDec`
              - Properties for a Delta Declination calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaRA`
              - Properties for a Delta Right Asc calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcBetaAngle`
              - Properties for a Beta Angle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcLocalApparentSolarLon`
              - Properties for a Local Apparent Solar Longitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcLonOfPeriapsis`
              - Properties for a Longitude of Periapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOrbitStateValue`
              - Properties for an Orbit State Value calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSignedEccentricity`
              - Properties for a SignedEccentricity calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcTrueLon`
              - Properties for a True Longitude calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcPower`
              - Properties for a Power calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelMotion`
              - Properties for a Relative Motion calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle`
              - Properties for a Solar Beta Angle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle`
              - Properties for a Solar In Plane Angle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionDecAngle`
              - Properties for a Relative Position Declination Angle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle`
              - Properties for a Relative Position In Plane Angle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination`
              - Properties for a Relative Inclination Angle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion`
              - Properties for Curvilinear Relative Motion  calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCustomFunction`
              - Properties for a Custom Function calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcScript`
              - Properties for a Script calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCd`
              - Properties for a Cd calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCr`
              - Properties for a Cr calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDragArea`
              - Properties for a DragArea calculation object. CAgAsStateCalcDragArea.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRadiationPressureArea`
              - Properties for a RadPressureArea calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRadiationPressureCoefficient`
              - Properties for a RadiationPressureCoefficient calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSRPArea`
              - Properties for an SRPArea calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCosOfVerticalFPA`
              - Properties for a Cosine of Vertical FPA calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDec`
              - Properties for a Declination calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcFPA`
              - Properties for a Flight Path Angle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRMagnitude`
              - Properties for an R Mag calculation object. AsStateCalcRMag.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRA`
              - Properties for a Right Asc calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVMagnitude`
              - Properties for a V Mag calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVelAz`
              - Properties for a Velocity Azimuth calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcC3Energy`
              - Properties for a C3 Energy calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInAsympDec`
              - Properties for an Incoming Asymptote Dec calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInAsympRA`
              - Properties for a Incoming Asymptote RA calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcInVelAzAtPeriapsis`
              - Properties for an Incoming Vel Az at Periapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOutAsympDec`
              - Properties for a Outgoing Asymptote Dec calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOutAsympRA`
              - Properties for a Outgoing Asymptote RA calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOutVelAzAtPeriapsis`
              - Properties for a Outgoing Vel Az at Periapsis calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDuration`
              - Properties for a Duration calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcUserValue`
              - Interface for CAgAsStateCalcUserValue.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVectorGeometryToolAngle`
              - Properties for an Vector Geometry Tool Angle calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcAngle`
              - Properties for an Angle Between Vectors calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDotProduct`
              - Properties for a Dot Product calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVectorDec`
              - Properties for a Vector Dec calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVectorMagnitude`
              - Properties for a Vector Mag calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcVectorRA`
              - Properties for a Vector RA calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess`
              - Properties for an Access calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat`
              - Properties for a Difference Across Segments Across Satellites calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat`
              - Properties for a Value At Segment Across Satellites calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRARate`
              - Properties for a Right Ascension Rate calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDecRate`
              - Properties for a Declination Rate calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRangeRate`
              - Properties for a Range Rate calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcGravitationalParameter`
              - Properties for a Gravitational Parameter calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcReferenceRadius`
              - Properties for a Reference Radius calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcGravCoeff`
              - Properties for a gravity coefficient calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSpeedOfLight`
              - Properties for a Speed of Light calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcPi`
              - Properties for a Pi calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcScalar`
              - Properties for a Scalar calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcApparentSolarTime`
              - Properties for an Apparent Solar Time calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEarthMeanSolarTime`
              - Properties for an Earth Mean Solar Time calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateCalcEarthMeanLocTimeAN`
              - Properties for an Earth Mean Local Time of Ascending Node calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection`
              - The list of central bodies.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemeris`
              - The central body ephemeris source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyGravityModel`
              - Properties for a central body gravity model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyShape`
              - The central body shape.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyShapeSphere`
              - Properties for the central body sphere shape.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyShapeOblateSpheroid`
              - Properties for the central body oblate spheroid shape.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyShapeTriaxialEllipsoid`
              - Properties for the central body triaxial ellipsoid shape.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitude`
              - The central body attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeRotationCoefficientsFile`
              - Properties for a rotation coefficients file attitude definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyAttitudeIAU1994`
              - Properties for an IAU1994 attitude definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit`
              - Properties for the Analytic Orbit ephemeris source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisJPLSpice`
              - Properties for the JPL SPICE ephemeris source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisFile`
              - Properties for the Ephemeris File ephemeris source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisJPLDesignExplorerOptimizer`
              - Properties for the JPL DE ephemeris source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisPlanetary`
              - Properties for the Planetary Ephemeris file ephemeris source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody`
              - General properties for a central body.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPowerInternal`
              - Properties for the Internal Power power source component.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPowerProcessed`
              - Properties for the Processed Power power source component.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray`
              - Properties for the Solar Array Power power source component.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGeneralRelativityFunction`
              - Properties for the General Relativity propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStateTransformationFunction`
              - Properties for the State Transition propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICR3BPFunc`
              - Properties for the CR3BP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IER3BPFunc`
              - Properties for the ER3BP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IRadiationPressureFunction`
              - Properties for the Radiation Pressure propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc`
              - Properties for the Yarkovsky Effect propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBlendedDensity`
              - Properties for the blended atmospheric density propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDragModelPlugin`
              - Properties for the Drag Model plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICira72Function`
              - Properties for the CIRA 72 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IExponential`
              - Properties for the Exponential atmospheric model - a model that calculates atmospheric density using an equation involving a reference density, reference altitude, and scale altitude.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IHarrisPriester`
              - Properties for the Harris-Priester atmospheric model - a model that takes into account a 10.7 cm solar flux level and diurnal bulge.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDensityModelPlugin`
              - Properties for the plugin atmospheric density model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IJacchiaRoberts`
              - Properties for the Jacchia-Roberts atmospheric model - a model that is similar to Jacchia 1971 but uses analytical methods to improve performance.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IJacchiaBowman2008`
              - Properties for the Jacchia Bowman 2008 atmospheric density model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IJacchia_1960`
              - Properties for the Jacchia 1960 atmospheric model - an outdated atmospheric model provided for making comparisons with other software.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IJacchia_1970`
              - Properties for the Jacchia 1970 atmospheric model - a model that computes atmospheric density based on the composition of the atmosphere, which depends on altitude as well as seasonal variation. Valid range is 100-2500 km.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IJacchia_1971`
              - Properties for the Jacchia 1971 atmospheric model - a model that is similar to Jacchia 1970, with improved treatment of certain solar effects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMSISE_1990`
              - Properties for the MSISE 1990 atmospheric model - an empirical density model developed by Hedin based on satellite data. Finds the total density by accounting for the contribution of N2, O, O2, He, Ar and H. 1990 version, valid range of 0-1000 km.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMSIS_1986`
              - Properties for the MSIS 1986 atmospheric model - an empirical density model developed by Hedin based on satellite data. Finds the total density by accounting for the contribution of N2, O, O2, He, Ar and H. 1986 version, valid range of 90-1000 km.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.INRLMSISE_2000`
              - Properties for the NRLMSISE 2000 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IUS_Standard_Atmosphere`
              - Properties for the US Standard Atmosphere atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMarsGRAM37`
              - Properties for the Mars-GRAM 3.7 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMarsGRAM2005`
              - Properties for the Mars-GRAM 2005 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IVenusGRAM2005`
              - Properties for the Venus-GRAM 2005 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMarsGRAM2010`
              - Properties for the Mars-GRAM 2010 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMarsGRAM2001`
              - Properties for the Mars-GRAM 2001 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMarsGRAM2000`
              - Properties for the Mars-GRAM 2000 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDTM2012`
              - Properties for the DTM 2012 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDTM2020`
              - Properties for the DTM 2020 atmospheric model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction`
              - Properties for the Gravitational Force gravity model - a complex gravitational force calculation, optionally including solid and ocean tide effects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPointMassFunction`
              - Properties for the Point Mass Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ITwoBodyFunction`
              - Properties for the Two Body gravity model - a standard point mass model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IHPOPPluginFunction`
              - Properties for the HPOP Plugin propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEOMFuncPluginFunction`
              - Properties for the EOM Function Plugin propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPAeroT20`
              - Properties for the Aerospace T20 solar radiation pressure model for GPS block IIA.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPAeroT30`
              - Properties for the Aerospace T30 solar radiation pressure model for GPS block IIR.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aIIA`
              - Properties for the Bar-Sever GPS Solar Pressure Model 04a for block IIA.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aIIR`
              - Properties for the Bar-Sever GPS Solar Pressure Model 04a for block IIR.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIA`
              - Properties for the Bar-Sever GPS Solar Pressure Model 04ae for block IIA.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPGSPM04aeIIR`
              - Properties for the Bar-Sever GPS Solar Pressure Model 04ae for block IIR.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPSpherical`
              - Properties for the Spherical SRP model; assumes a spherical spacecraft. The equation used by STK is described in the Solar Radiation technical note.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPNPlate`
              - Properties for the N-plate SRP model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPTabAreaVec`
              - Properties for the tabulated area vector SRP model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPVariableArea`
              - Properties for the Variable Area SRP model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IThirdBodyFunction`
              - Properties for a Third Body propagator function. The IAgComponentInfo object returned by the mode property can be cast to IAgVAGravityFieldFunction or IAgVAPointMassFunction depending on the selected ModeType.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin`
              - Properties for the plugin SRP Refelction.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineModelThrustCoefficients`
              - Thrust coefficient properties for engine definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineModelIspCoefficients`
              - Isp coefficient properties for engine definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineConstAcc`
              - Properties for a Constant Acceleration and Isp engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineConstant`
              - Properties for a Constant Thrust and Isp engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineDefinition`
              - Properties for engine definition for an Ion engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable`
              - Properties for engine parameters for a Throttle Table engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineIon`
              - Properties for engine parameters for an Ion engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom`
              - Properties for a Custom engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEnginePlugin`
              - Properties for a Plugin engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IEngineModelPoly`
              - Properties for a Polynomial Thrust and Isp engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDesignCR3BPObjectCollection`
              - The list of associated CR3BP objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDesignER3BPObjectCollection`
              - The list of associated ER3BP objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDesignCR3BPSetup`
              - Properties for the CR3BP Setup Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDesignCR3BPObject`
              - Properties for individual associated CR3BP object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDesignER3BPSetup`
              - Properties for the ER3BP Setup Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDesignER3BPObject`
              - Properties for individual associated ER3BP object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IThruster`
              - Properties for individual thrusters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IThrusterSetCollection`
              - The list of thrusters in a thruster set.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IThrusterSet`
              - The properties of a thruster set.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAsTriggerCondition`
              - Properties for a constraint - an additional condition to be met to satisfy a stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICustomFunctionScriptEngine`
              - Properties for custom functions.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalIntegrator`
              - The type of numerical integrator to be used by the propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection`
              - The list of propagator functions - affecting forces that you want to model for orbit propagation.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapper`
              - General properties for propagators.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalPropagatorWrapperCR3BP`
              - General properties for three-body problem propagators.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBulirschStoerIntegrator`
              - Properties for the Bulirsch-Stoer numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IGaussJacksonIntegrator`
              - Properties for the Gauss-Jackson numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IRungeKutta2nd3rd`
              - Properties for the RK2nd3rd numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IRungeKutta4th`
              - Properties for the RK4th numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IRungeKutta4th5th`
              - Properties for the RK4th5th numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IRungeKutta4thAdapt`
              - Properties for the RK4thAdapt numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IRungeKuttaF7th8th`
              - Properties for the RK7th8th numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IRungeKuttaV8th9th`
              - Properties for the RK8th9th numerical integrator.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DriverMissionControlSequence`
              - Basic properties of an Astrogator satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceSegmentCollection`
              - The Mission Control Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceEnd`
              - The End segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceInitialState`
              - The Initial State segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters`
              - Spacecraft parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FuelTank`
              - Fuel Tank parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementCartesian`
              - Cartesian elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementKeplerian`
              - Keplerian elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial`
              - Equinoctial elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay`
              - Delaunay elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementMixedSpherical`
              - Mixed Spherical elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical`
              - Spherical elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementTargetVectorIncomingAsymptote`
              - Target Vector Incoming Asymptote elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementTargetVectorOutgoingAsymptote`
              - Target Vector Outgoing Asymptote elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic`
              - Geodetic elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane`
              - Bplane elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate`
              - Spherical Range Rate elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequencePropagate`
              - The Propagate segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.State`
              - The orbit state.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection`
              - The stopping conditions collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition`
              - The Access stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition`
              - The Lighting stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StoppingCondition`
              - A stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionElement`
              - A stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceSequence`
              - The Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceBackwardSequence`
              - The Backward Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceLaunch`
              - The Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DisplaySystemGeodetic`
              - The geodetic launch location.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DisplaySystemGeocentric`
              - The geocentric launch location.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutGeodetic`
              - The geodetic burnout point.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutCBFCartesian`
              - The burnout state in CBF Cartesian coordinates.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutGeocentric`
              - The geocentric burnout point.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzAltitude`
              - The launch azimuth and altitude burnout point.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius`
              - The launch azimuth and radius burnout point.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutVelocity`
              - The burnout velocity.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceFollow`
              - The Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceManeuver`
              - The Maneuver segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinite`
              - The Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverImpulsive`
              - The Impulsive Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveVelocityVector`
              - The velocity vector attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAntiVelocityVector`
              - The anti-velocity vector attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude`
              - The attitude attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile`
              - The file attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector`
              - The thrust vector attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAntiVelocityVector`
              - The anti-velocity vector attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude`
              - The attitude attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile`
              - The file attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector`
              - The thrust vector attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying`
              - The time varying attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector`
              - The velocity vector attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin`
              - The plugin attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlOptimalFiniteLagrange`
              - The Lagrange Interpolation attitude control for a optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator`
              - Propagation for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceHold`
              - The Hold segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceUpdate`
              - The Update segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceReturn`
              - The Return segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceStop`
              - The Stop segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceTargetSequence`
              - The Target Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection`
              - The Profiles of a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions`
              - The MCS Options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalcObjectCollection`
              - The Calculation Object component folder.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection`
              - The Constraint component folder.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PluginProperties`
              - The plugin attitude control type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileSearchPlugin`
              - The plugin search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph`
              - Targeter Graph.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection`
              - Targeter Graphs.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResultCollection`
              - Targeter Graph Result Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection`
              - Targeter Graph Active Control Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControl`
              - Targeter Graph Active Control.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult`
              - Targeter Graph Result.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector`
              - The Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool`
              - The Scripting Tool profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl`
              - Control Parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult`
              - Differential Corrector equality constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection`
              - The collection of Control Parameters for a differential corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection`
              - The collection of results for a differential corrector.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControl`
              - Control parameters for a plugin search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection`
              - The list of search plugin control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult`
              - Equality constraints for a plugin search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection`
              - The list of search plugin equality constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeManeuverType`
              - The Change Maneuver Type profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment`
              - The Change Return Segment profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangePropagator`
              - The Change Propagator profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStopSegment`
              - The Change Stop Segment profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState`
              - The Change Stopping Condition State profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver`
              - The Seed Finite Maneuver profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileRunOnce`
              - The Run Once profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BPlaneCollection`
              - The collection of B-Planes.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDamageFlux`
              - CoClass StateCalcDamageFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDamageMassFlux`
              - CoClass StateCalcDamageMassFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMagnitudeFieldDipoleL`
              - CoClass StateCalcMagFieldDipoleL.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSEETMagnitudeFieldFieldLineSepAngle`
              - SEETMagFieldFieldLineSepAngle Calc object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcImpactFlux`
              - CoClass StateCalcImpactFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcImpactMassFlux`
              - CoClass StateCalcImpactMassFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSEETSAAFlux`
              - CoClass StateCalcSEETSAAFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSEETVehTemp`
              - CoClass StateCalcSEETVehTemp.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEpoch`
              - Epoch Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcJacobiConstant`
              - Jacobi Constant Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcJacobiOsculating`
              - Osculating Jacobi Integral Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartesianElem`
              - Cartesian Elements Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem`
              - Cartesian STM Elements Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval`
              - Cartesian STM Eigenvalues Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenvecElem`
              - Cartesian STM Eigenvector Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEnvironment`
              - Environment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitDelaunayG`
              - CoClass AsStateCalcOrbitDelaunayG.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitDelaunayH`
              - CoClass AsStateCalcOrbitDelaunayH.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitDelaunayL`
              - CoClass AsStateCalcOrbitDelaunayL.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitSemiLatusRectum`
              - CoClass AsStateCalcOrbitSemiLatusRectum.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEquinoctialElem`
              - Equinoctial Elements Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachBearing`
              - CloseApproachBearing Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachMagnitude`
              - CloseApproachMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachTheta`
              - CloseApproachTheta Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachX`
              - CloseApproachX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachY`
              - CloseApproachY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachCosBearing`
              - CloseApproachCosBearing Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelGroundTrackError`
              - RelGroundTrackError Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelAtAOLMaster`
              - RelAOLMaster Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaFromMaster`
              - DeltaFromMaster Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcLonDriftRate`
              - LongDriftRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanEarthLon`
              - MeanEarthLon Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRectifiedLon`
              - RectifiedLongitude Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTrueLongitude`
              - TrueLongitude Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGeodeticTrueLongitude`
              - GeodeticTrueLongitude Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGeodeticTrueLongitudeAtTimeOfPerigee`
              - GeodeticTrueLongitudeAtTimeOfPerigee Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanRightAscension`
              - MeanRightAscension Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGeodeticMeanRightAscension`
              - GeodeticMeanRightAscension Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTwoBodyDriftRate`
              - TwoBodyDriftRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDriftRateFactor`
              - DriftRateFactor Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEccentricityX`
              - EccentricityX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEccentricityY`
              - EccentricityY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInclinationX`
              - InclinationX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInclinationY`
              - InclinationY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcUnitAngularMomentumX`
              - UnitAngularMomentumX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcUnitAngularMomentumY`
              - UnitAngularMomentumY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcUnitAngularMomentumZ`
              - UnitAngularMomentumZ Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcHeightAboveTerrain`
              - CoClass AsStateCalcHeightAboveTerrain.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGeodeticElem`
              - Geodetic Elements Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr`
              - RepeatingGrTrackErr Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcAltitudeOfApoapsis`
              - AltitudeOfApoapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcAltitudeOfPeriapsis`
              - AltitudeOfPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcArgOfLat`
              - Argument of Latitude Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcArgOfPeriapsis`
              - Argument of Periapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEccentricityAnomaly`
              - EccAnomaly Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcLonOfAscNode`
              - LongitudeOfAscendingNode Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanMotion`
              - MeanMotion Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitPeriod`
              - OrbitPeriod Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcNumRevs`
              - NumRevs Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRadOfApoapsis`
              - RadiusOfApoapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRadOfPeriapsis`
              - RadiusOfPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSemiMajorAxis`
              - SemiMajorAxis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTimePastAscNode`
              - TimePastAscNode Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTimePastPeriapsis`
              - TimePastPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTrueAnomaly`
              - TrueAnomaly Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaV`
              - DeltaV Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaVSquared`
              - DeltaV Squared Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMissionControlSequenceDeltaV`
              - MCS DeltaV Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMissionControlSequenceDeltaVSquared`
              - MCS DeltaV Squared Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaV`
              - Sequence DeltaV Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared`
              - Sequence DeltaV Squared Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcFuelMass`
              - FuelMass Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDensity`
              - Density  Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInertialDeltaVMagnitude`
              - InertialDeltaVMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInertialDeltaVx`
              - InertialDeltaVx Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInertialDeltaVy`
              - InertialDeltaVy Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInertialDeltaVz`
              - InertialDeltaVz Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcManeuverSpecificImpulse`
              - ManeuverSpecificImpulse Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPressure`
              - Pressure Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTemperature`
              - Temperature Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorY`
              - VectorY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorZ`
              - VectorZ Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMass`
              - Mass Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcManeuverTotalMassFlowRate`
              - ManeuverTotalMassFlowRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcAbsoluteValue`
              - AbsoluteValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifference`
              - Difference Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment`
              - DifferenceOtherSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPositionDifferenceOtherSegment`
              - PosDifferenceOtherSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVelDifferenceOtherSegment`
              - VelDifferenceOtherSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPositionVelDifferenceOtherSegment`
              - PosVelDifferenceOtherSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegment`
              - ValueAtSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMaxValue`
              - MaximumValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMinValue`
              - MinimumValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanValue`
              - MeanValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMedianValue`
              - MedianValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcStandardDeviation`
              - StandardDeviation Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcNegative`
              - Negative Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEccentricity`
              - Eccentricity Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanAnomaly`
              - MeanAnomaly Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRAAN`
              - RAAN Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BDotRCalc`
              - BDotR Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BDotTCalc`
              - BDotT Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BMagnitudeCalc`
              - BMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BThetaCalc`
              - BTheta Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaDec`
              - DeltaDec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaRA`
              - DeltaRA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcBetaAngle`
              - BetaAngle Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcLocalApparentSolarLon`
              - LocalApparentSolarLon Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcLonOfPeriapsis`
              - LonOfPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue`
              - OrbitStateValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSignedEccentricity`
              - SignedEccentricity Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInclination`
              - Inclination Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTrueLon`
              - TrueLong Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPower`
              - Power Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion`
              - Relative Motion Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarBetaAngle`
              - Solar Beta Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle`
              - Solar In Plane Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelPositionDecAngle`
              - Relative Position Declination Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelPositionInPlaneAngle`
              - Relative Position Declination Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination`
              - Relative Inclination Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelMotion`
              - Curvilinear Relative Motion objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction`
              - Custom Function Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript`
              - Script Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCd`
              - Cd Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCr`
              - Cr Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDragArea`
              - DragArea Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRadiationPressureArea`
              - RadPressureArea Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRadiationPressureCoefficient`
              - RadiationPressureCoefficient Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSRPArea`
              - SRPArea Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCosOfVerticalFPA`
              - CosineOfVerticalFPA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDec`
              - Dec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcFPA`
              - FPA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRMagnitude`
              - RMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRA`
              - RA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVMagnitude`
              - VMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVelAz`
              - Velocity Azimuth Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcC3Energy`
              - C3Energy Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInAsympDec`
              - InAsymptoteDec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInAsympRA`
              - InAsymptoteRA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInVelAzAtPeriapsis`
              - InVelocityAzAtPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOutAsympDec`
              - OutAsymptoteDec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOutAsympRA`
              - OutAsymptoteRA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOutVelAzAtPeriapsis`
              - OutVelocityAzAtPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDuration`
              - Duration Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcUserValue`
              - CoClass StateCalcUserValue.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorGeometryToolAngle`
              - Vector Geometry Tool Angle Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcAngle`
              - Angle Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDotProduct`
              - DotProduct Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorDec`
              - VectorDec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorMagnitude`
              - VectorMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorRA`
              - VectorRA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorX`
              - VectorX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess`
              - Access Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSat`
              - DifferenceAcrossSegmentsOtherSat Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat`
              - ValueAtSegmentOtherSat Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRARate`
              - RightAscensionRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDecRate`
              - DeclinationRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRangeRate`
              - RangeRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter`
              - GravitationalParameter Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius`
              - Reference Radius Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff`
              - Gravity Coefficient Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSpeedOfLight`
              - Speed Of Light Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPi`
              - Pi Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcScalar`
              - Scalar Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcApparentSolarTime`
              - Apparent Solar Time Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEarthMeanSolarTime`
              - EarthMeanSolarTime Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEarthMeanLocTimeAN`
              - EarthMeanLocTimeAN Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AutomaticSequenceCollection`
              - Automatic Sequence Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AutomaticSequence`
              - Automatic Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyCollection`
              - Central Body Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AstrogatorCentralBody`
              - Central Body.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel`
              - Central Body Gravity Model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyShapeSphere`
              - Central Body Shape - Sphere.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyShapeOblateSpheroid`
              - Central Body Shape - Spheroid.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyShapeTriaxialEllipsoid`
              - Central Body Shape - Triaxial Ellipsoid.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyAttitudeRotationCoefficientsFile`
              - Central Body Attitude - Rotation Coefficients File.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyAttitudeIAU1994`
              - Central Body Attitude - IAU1994.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyEphemerisAnalyticOrbit`
              - Central Body Ephemeris - Analytic Orbit.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyEphemerisJPLSpice`
              - Central Body Ephemeris - JPLSpice.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyEphemerisFile`
              - Central Body Ephemeris - File.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyEphemerisJPLDesignExplorerOptimizer`
              - Central Body Ephemeris - JPL DE.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyEphemerisPlanetary`
              - Central Body Ephemeris - Planetary.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceSegmentProperties`
              - Segment Properties.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PowerInternal`
              - Power - Internal.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed`
              - Power - Processed Power Unit.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray`
              - Power - Solar Array.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GeneralRelativityFunction`
              - General Relativity Propagator Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateTransformationFunction`
              - State Transition Propagator Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunc`
              - CR3BP Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc`
              - ER3BP Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction`
              - Radiation Pressure Propagator Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.YarkovskyFunc`
              - Yarkovsky Effect Propagator Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity`
              - Blended atmospheric density propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Cira72Function`
              - Cira72 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Exponential`
              - Exponential atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester`
              - Harris-Priester atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin`
              - Plugin atmospheric density propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.JacchiaRoberts`
              - Jacchia Roberts atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.JacchiaBowman2008`
              - Jacchia Bowman 2008 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Jacchia_1960`
              - Jacchia_1960 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Jacchia_1970`
              - Jacchia_1970 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Jacchia_1971`
              - Jacchia_1971 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MSISE_1990`
              - MSISE 1990 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MSIS_1986`
              - MSIS 1986 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.NRLMSISE_2000`
              - NRLMSISE 2000 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.US_Standard_Atmosphere`
              - US_Standard_Atmosphere atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM37`
              - Mars-GRAM 3.7 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2000`
              - Mars-GRAM 2000 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001`
              - Mars-GRAM 2001 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2005`
              - Mars-GRAM 2005 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010`
              - Mars-GRAM 2010 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.VenusGRAM2005`
              - Venus-GRAM 2005 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DTM2012`
              - DTM 2012 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DTM2020`
              - DTM 2020 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GravityFieldFunction`
              - Gravity Field gravity propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PointMassFunction`
              - Point Mass function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TwoBodyFunction`
              - Two Body gravity propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.HPOPPluginFunction`
              - HPOP Plugin propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EOMFuncPluginFunction`
              - EOM Function Plugin propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPAeroT20`
              - AeroT20 SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPAeroT30`
              - AeroT30 SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPGSPM04aIIA`
              - GSPM04aIIA SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPGSPM04aIIR`
              - GSPM04aIIR SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPGSPM04aeIIA`
              - GSPM04aeIIA SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPGSPM04aeIIR`
              - GSPM04aeIIR SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical`
              - Spherical SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate`
              - NPlate SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPTabAreaVec`
              - Tabulated area vector SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPVariableArea`
              - Variable Area SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction`
              - ThirdBody propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DragModelPlugin`
              - Drag Model Plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin`
              - SRP Reflection Plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineConstAcc`
              - Constant Acceleration engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineConstant`
              - Constant Thrust engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineIon`
              - Ion Engine engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineThrottleTable`
              - Throttle Table engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineCustom`
              - Custom engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EnginePlugin`
              - Plugin engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineModelPoly`
              - Polynomial Thrust and Isp engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineModelThrustCoefficients`
              - Engine Model Thrust Coefficients.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineModelIspCoefficients`
              - Engine Model Isp Coefficients.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition`
              - Engine definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPSetup`
              - CR3BP Setup Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObject`
              - CR3BP associated object definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection`
              - CR3BP associated object Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPSetup`
              - ER3BP Setup Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObject`
              - ER3BP associated object definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection`
              - ER3BP associated object Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Thruster`
              - Thruster definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection`
              - Thruster Set Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThrusterSet`
              - Thruster Set.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition`
              - Constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CustomFunctionScriptEngine`
              - Custom Function Script Engine.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapper`
              - Numerical Propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP`
              - Numerical CR3BP Propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection`
              - Propagator Function Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator`
              - Bulirsch-Stoer Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator`
              - Gauss-Jackson Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RungeKutta2nd3rd`
              - RK2nd3rd Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4th`
              - RK4th Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4th5th`
              - RK4th5th Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RungeKutta4thAdapt`
              - RK4thAdapt Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaF7th8th`
              - RKF7th8th Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RungeKuttaV8th9th`
              - RKV8th9th Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool`
              - Scripting Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection`
              - Scripting Segment Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegment`
              - Scripting Segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection`
              - Scripting Parameter Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter`
              - Scripting Parameter.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObject`
              - Calc Object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection`
              - Calc Object Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinition`
              - User Variable Definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariable`
              - User Variable.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate`
              - User Variable Update.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection`
              - User Variable Definition Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableCollection`
              - User Variable Initial Value Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection`
              - User Variable Update Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection`
              - Calculation Graph Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoice`
              - Scripting Parameter Enumeration Choice.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection`
              - Scripting Parameter Enumeration Choice Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer`
              - SNOPT optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl`
              - Control parameters for SNOPT optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult`
              - Properties for objecvtive and constraints of a SNOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection`
              - SNOPT control collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection`
              - SNOPT result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileIPOPTOptimizer`
              - IPOPT optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl`
              - Control parameters for IPOPT optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult`
              - Properties for objecvtive and constraints of a IPOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection`
              - Properties for the list of IPOPT control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection`
              - IPOPT result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite`
              - The Optimal Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer`
              - Properties of SNOPT Optimizer options for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteInitialBoundaryConditions`
              - Properties of initial boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteFinalBoundaryConditions`
              - Properties of final boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions`
              - Properties of path boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSteeringNodeElement`
              - The elements of the steering node.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSteeringNodeCollection`
              - Steering/nodes collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteBounds`
              - The elements of the steering node.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile`
              - The Lambert profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile`
              - The Lambert profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileGoldenSection`
              - The Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection`
              - Properties for the list of Golden Section control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl`
              - Control parameters for Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection`
              - Properties for the list of Golden Section result parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult`
              - Result parameters for Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch`
              - The Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection`
              - Properties for the list of Grid Search control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl`
              - Control parameters for Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchResultCollection`
              - Properties for the list of Grid Search result parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchResult`
              - Result parameters for Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalcObjectLinkEmbedControlCollection`
              - The Calculation Object link/embed component folder.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileBisection`
              - Single Parameter Bisection profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BisectionControl`
              - Control parameters for  Bisection Seacrh Profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BisectionControlCollection`
              - Bisection control collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BisectionResult`
              - Result parameters for Bisection profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BisectionResultCollection`
              - Bisection result collection.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GRAPH_OPTION`
              - Mode that the mcs will run in.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SMART_RUN_MODE`
              - Mode that the mcs will run in.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FORMULATION`
              - Equinoctial Formulation.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LIGHTING_CONDITION`
              - The criteria of a Lighting stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PROFILE`
              - Type of profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ACCESS_CRITERION`
              - The criteria of an Access stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ECLIPSING_BODIES_SOURCE`
              - The source types of the eclipsing bodies list.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CRITERION`
              - The stopping condition criterion types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_REFERENCE`
              - The calculation object Reference Selection types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_CENTRAL_BODY_REFERENCE`
              - The calculation object Central Body Reference Selection types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_ELEM`
              - The calculation object Element Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PROFILE_MODE`
              - The Target Sequence profile modes.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_STOPPING_CONDITION`
              - The stopping condition control types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.STATE`
              - The Stop segment state types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RETURN_CONTROL`
              - The Return segment control types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DRAW_PERTURBATION`
              - The Draw Perturbation types for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DERIVE_CALC_METHOD`
              - The Derivative Calculation method types for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONVERGENCE_CRITERIA`
              - The Convergence Criteria types for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DIFFERENTIAL_CORRECTOR_SCALING_METHOD`
              - The Scaling Method types for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_UPDATE`
              - Update segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_FOLLOW`
              - Follow segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_INIT_STATE`
              - Initial State segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_MANEUVER`
              - Maneuver segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_LAUNCH`
              - Launch segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_ADVANCED`
              - Propagate segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TARGET_SEQ_ACTION`
              - Action options for Target Sequence profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PROFILES_FINISH`
              - Action options for Target Sequence profiles convergence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UPDATE_PARAM`
              - Spacecraft parameters that can be modified by an Update segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UPDATE_ACTION`
              - Actions for the Update segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PRESSURE_MODE`
              - Pressure Mode options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.THRUST_TYPE`
              - Thrust options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ATTITUDE_UPDATE`
              - Attitude Update.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PROPULSION_METHOD`
              - Propulsion method options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CUSTOM_FUNCTION`
              - Attitude definition options for other STK functions.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BODY_AXIS`
              - Attitude body axis options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONSTRAINT_SIGN`
              - Constraint vector sign options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ATTITUDE_CONTROL`
              - Attitude Control options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FOLLOW_JOIN`
              - Joining options for the Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FOLLOW_SEPARATION`
              - Separation options for the Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FOLLOW_SPACECRAFT_AND_FUEL_TANK`
              - Spacecraft parameter options for the Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BURNOUT_OPTIONS`
              - Burnout options for the Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BURNOUT_TYPE`
              - Burnout point definition types for the Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ASCENT_TYPE`
              - Ascent types for the Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LAUNCH_DISPLAY_SYSTEM`
              - Launch location coordinate types for the Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RUN_CODE`
              - The run code returned after the MCS is run.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SEQUENCE_STATE_TO_PASS`
              - State To Pass options for the Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MANEUVER_TYPE`
              - Maneuver types for the maneuver segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SEGMENT_TYPE`
              - Segment types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ELEMENT_TYPE`
              - Types of orbit element sets.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LANGUAGE`
              - Scripting language types for the Scripting Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.STOPPING_CONDITION`
              - Type of stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CLEAR_EPHEMERIS_DIRECTION`
              - Direction in which to clear ephemeris.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PROFILE_INSERT_DIRECTION`
              - Direction to insert profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ROOT_FINDING_ALGORITHM`
              - Root-finding algorithms.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SCRIPTING_PARAMETER_TYPE`
              - Scripting Tool parameter type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPT_GOAL`
              - The Goal types for a SNOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPT_GOAL`
              - The Goal types for a IPOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_SEED_METHOD`
              - Seed methods.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_RUN_MODE`
              - Run modes.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_DISCRETIZATION_STRATEGY`
              - Discretization Strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_WORKING_VARIABLES`
              - Working Variables.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_SCALING_OPTIONS`
              - Scaling Options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_SNOPT_OBJECTIVE`
              - Optimal Finite SNOPT objective.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_SNOPT_SCALING`
              - Optimal Finite SNOPT scaling option.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_EXPORT_NODES_FORMAT`
              - Steering nodes export format.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OPTIMAL_FINITE_GUESS_METHOD`
              - Guess interpolation method.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMP_DELTA_V_REP`
              - Vector representations for impulsive DeltaV specification.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LAMBERT_TARGET_COORD_TYPE`
              - Lambert Target CoordType.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LAMBERT_SOLUTION_OPTION_TYPE`
              - Lambert Solution Option Type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LAMBERT_ORBITAL_ENERGY_TYPE`
              - Lambert Orbital Energy Type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LAMBERT_DIRECTION_OF_MOTION_TYPE`
              - Lambert Direction Of Motion Type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GOLDEN_SECTION_DESIRED_OPERATION`
              - The types for Desired Operation/Objective of golden section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GRID_SEARCH_DESIRED_OPERATION`
              - The types for Desired Operation/Objective of Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ELEMENT`
              - Which type of elements (osculating or mean).

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BASE_SELECTION`
              - Access base object selections types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_ORBIT_STATE_VALUE`
              - Orbit State Value properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SEGMENT_STATE`
              - Segment state to use types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DIFFERENCE_ORDER`
              - The Difference order types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SEGMENT_DIFFERENCE_ORDER`
              - The Difference Across Segments order types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_REPEATING_GROUND_TRACK_ERR`
              - Repeating Ground Track Equator Error properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_DIRECTION`
              - The direction to search for a desired value.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_ORBIT_PLANE_SOURCE`
              - The calculation object orbit plane source Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_SUN_POSITION`
              - The calculation object sun location Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_ANGLE_SIGN`
              - The sign of the angle when the relative position has a component along the orbit normal.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_REFERENCE_DIRECTION`
              - Direction that establishes the zero value when projected into the orbit plane.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_RELATIVE_POSITION`
              - The calculation object relative position Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_REFERENCE_ELLIPSE`
              - The calculation object reference ellipse Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CALC_OBJECT_LOCATION_SOURCE`
              - The calculation object location source Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GRAVITATIONAL_PARAMETER_SOURCE`
              - The source of the gravitational parameter for a CAgVAStateCalcGravitationalParameter calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.REFERENCE_RADIUS_SOURCE`
              - The source of the reference radius for a CAgVAStateCalcReferenceRadius calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GRAV_COEFF_NORMALIZATION_TYPE`
              - The normalization type for the CAgVAStateCalcGravCoeff calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GRAV_COEFF_COEFFICIENT_TYPE`
              - The coefficient type for the CAgVAStateCalcGravCoeff calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.STM_PERT_VARIABLES`
              - The initial and final Cartesian variational variables that describe an STM element.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.STM_EIGEN_NUMBER`
              - The number that describes one of the 6 STM Eigenvalues or Eigenvectors.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.COMPLEX_NUMBER`
              - Whether a value represents the real or imaginary portion of a number.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SQUARED_TYPE`
              - Whether to calculate the value as the square of the sum of each component or the sum of the squares.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GEO_STATIONARY_DRIFT_RATE_MODEL`
              - Gravity models used to compute geostationary drift rate.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GEO_STATIONARY_INCLINATION_MAGNITUDE`
              - Magnitude to use when computing the inclination vector.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CENTRAL_BODY_GRAVITY_MODEL`
              - The gravity model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CENTRAL_BODY_SHAPE`
              - The central body shape types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CENTRAL_BODY_ATTITUDE`
              - The central body attitude types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CENTRAL_BODY_EPHEMERIS`
              - The central body ephemeris types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_POWER_INTERNAL`
              - Internal Power properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_POWER_PROCESSED`
              - Processed Power properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_POWER_SOLAR_ARRAY`
              - Solar Array Power properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.THIRD_BODY_MODE`
              - The third body gravity mode.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GRAV_PARAM_SOURCE`
              - The gravity parameter source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EPHEM_SOURCE`
              - The ephemeris source type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SOLAR_FORCE_METHOD`
              - The solar force method type for a spherical or N-plate SRP model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SHADOW_MODEL`
              - The shadow model type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SUN_POSITION`
              - The sun position type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ATMOS_DATA_SOURCE`
              - The Atmospheric data source type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GEO_MAGNETIC_FLUX_SOURCE`
              - Whether to use Kp or Ap data from the flux file.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GEO_MAGNETIC_FLUX_UPDATE_RATE`
              - Method for using geomagnetic flux values from the flux file.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DRAG_MODEL_TYPE`
              - Type of Drag Model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MARS_GRAM_DENSITY_TYPE`
              - Density Type for MarsGRAM Density Models.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.VENUS_GRAM_DENSITY_TYPE`
              - Density Type for VenusGRAM Density Models.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TAB_VEC_INTERP_METHOD`
              - The interpolation method for tabulated area vector file.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_ENGINE_CONST_ACC`
              - Constant Acceleration and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_ENGINE_CONSTANT`
              - Constant Thrust and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_ENGINE_CUSTOM`
              - Custom engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_ENGINE_THROTTLE_TABLE`
              - Throttle table engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_ENGINE_ION`
              - Ion engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_ENGINE_MODEL_POLY`
              - Polynomial Thrust and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ENGINE_MODEL_FUNCTION`
              - The engine model function types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.THROTTLE_TABLE_OPERATION_MODE`
              - Engine operation mode.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDEAL_ORBIT_RADIUS`
              - Ideal Orbit Radius.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ROTATING_COORDINATE_SYSTEM`
              - Barycenter centered rotating system.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CONTROL_THRUSTERS`
              - Thruster properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.THRUSTER_DIRECTION`
              - The thruster direction type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CRITERIA`
              - The criteria type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ERROR_CONTROL`
              - Error Control for the numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PREDICTOR_CORRECTOR`
              - Predictor corrector scheme for the numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.NUMERICAL_INTEGRATOR`
              - Numerical integrator type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.COEFF_RUNGE_KUTTA_V_8TH_9TH`
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

     IUserVariableDefinitionCollection<astrogator/IUserVariableDefinitionCollection>
     IUserVariableCollection<astrogator/IUserVariableCollection>
     IUserVariableUpdateCollection<astrogator/IUserVariableUpdateCollection>
     ICalculationGraphCollection<astrogator/ICalculationGraphCollection>
     IConstraintCollection<astrogator/IConstraintCollection>
     IPluginProperties<astrogator/IPluginProperties>
     ISNOPTControlCollection<astrogator/ISNOPTControlCollection>
     ISNOPTResultCollection<astrogator/ISNOPTResultCollection>
     IIPOPTControlCollection<astrogator/IIPOPTControlCollection>
     IIPOPTResultCollection<astrogator/IIPOPTResultCollection>
     IManeuverOptimalFiniteSNOPTOptimizer<astrogator/IManeuverOptimalFiniteSNOPTOptimizer>
     IManeuverOptimalFiniteInitialBoundaryConditions<astrogator/IManeuverOptimalFiniteInitialBoundaryConditions>
     IManeuverOptimalFiniteFinalBoundaryConditions<astrogator/IManeuverOptimalFiniteFinalBoundaryConditions>
     IManeuverOptimalFinitePathBoundaryConditions<astrogator/IManeuverOptimalFinitePathBoundaryConditions>
     IManeuverOptimalFiniteSteeringNodeCollection<astrogator/IManeuverOptimalFiniteSteeringNodeCollection>
     IManeuverOptimalFiniteBounds<astrogator/IManeuverOptimalFiniteBounds>
     IGoldenSectionControlCollection<astrogator/IGoldenSectionControlCollection>
     IGoldenSectionControl<astrogator/IGoldenSectionControl>
     IGoldenSectionResultCollection<astrogator/IGoldenSectionResultCollection>
     IGoldenSectionResult<astrogator/IGoldenSectionResult>
     IGridSearchControlCollection<astrogator/IGridSearchControlCollection>
     IGridSearchControl<astrogator/IGridSearchControl>
     IGridSearchResultCollection<astrogator/IGridSearchResultCollection>
     IGridSearchResult<astrogator/IGridSearchResult>
     IBisectionControlCollection<astrogator/IBisectionControlCollection>
     IBisectionResult<astrogator/IBisectionResult>
     IBisectionResultCollection<astrogator/IBisectionResultCollection>
     IStoppingConditionElement<astrogator/IStoppingConditionElement>
     IStoppingConditionCollection<astrogator/IStoppingConditionCollection>
     IMissionControlSequenceSegmentCollection<astrogator/IMissionControlSequenceSegmentCollection>
     IState<astrogator/IState>
     IStoppingConditionComponent<astrogator/IStoppingConditionComponent>
     IAutomaticSequence<astrogator/IAutomaticSequence>
     IAutomaticSequenceCollection<astrogator/IAutomaticSequenceCollection>
     IBPlaneCollection<astrogator/IBPlaneCollection>
     ICalcObjectCollection<astrogator/ICalcObjectCollection>
     IManeuverFinitePropagator<astrogator/IManeuverFinitePropagator>
     IBurnoutVelocity<astrogator/IBurnoutVelocity>
     IAttitudeControl<astrogator/IAttitudeControl>
     IAttitudeControlFinite<astrogator/IAttitudeControlFinite>
     IAttitudeControlImpulsive<astrogator/IAttitudeControlImpulsive>
     IAttitudeControlOptimalFinite<astrogator/IAttitudeControlOptimalFinite>
     IManeuver<astrogator/IManeuver>
     IDisplaySystem<astrogator/IDisplaySystem>
     IBurnout<astrogator/IBurnout>
     IScriptingSegment<astrogator/IScriptingSegment>
     IScriptingSegmentCollection<astrogator/IScriptingSegmentCollection>
     IScriptingParameterEnumerationChoice<astrogator/IScriptingParameterEnumerationChoice>
     IScriptingParameterEnumerationChoiceCollection<astrogator/IScriptingParameterEnumerationChoiceCollection>
     IScriptingParameter<astrogator/IScriptingParameter>
     IScriptingParameterCollection<astrogator/IScriptingParameterCollection>
     IScriptingCalcObject<astrogator/IScriptingCalcObject>
     IScriptingCalcObjectCollection<astrogator/IScriptingCalcObjectCollection>
     IScriptingTool<astrogator/IScriptingTool>
     IElement<astrogator/IElement>
     ISpacecraftParameters<astrogator/ISpacecraftParameters>
     IFuelTank<astrogator/IFuelTank>
     IMissionControlSequenceSegmentProperties<astrogator/IMissionControlSequenceSegmentProperties>
     IMissionControlSequenceEnd<astrogator/IMissionControlSequenceEnd>
     IMissionControlSequenceInitialState<astrogator/IMissionControlSequenceInitialState>
     IMissionControlSequenceSegment<astrogator/IMissionControlSequenceSegment>
     IMissionControlSequenceOptions<astrogator/IMissionControlSequenceOptions>
     IDriverMissionControlSequence<astrogator/IDriverMissionControlSequence>
     IElementCartesian<astrogator/IElementCartesian>
     IElementKeplerian<astrogator/IElementKeplerian>
     IElementDelaunay<astrogator/IElementDelaunay>
     IElementEquinoctial<astrogator/IElementEquinoctial>
     IElementMixedSpherical<astrogator/IElementMixedSpherical>
     IElementSpherical<astrogator/IElementSpherical>
     IElementTargetVectorIncomingAsymptote<astrogator/IElementTargetVectorIncomingAsymptote>
     IElementTargetVectorOutgoingAsymptote<astrogator/IElementTargetVectorOutgoingAsymptote>
     IElementGeodetic<astrogator/IElementGeodetic>
     IElementBPlane<astrogator/IElementBPlane>
     IElementSphericalRangeRate<astrogator/IElementSphericalRangeRate>
     IStoppingCondition<astrogator/IStoppingCondition>
     ILightingStoppingCondition<astrogator/ILightingStoppingCondition>
     IAccessStoppingCondition<astrogator/IAccessStoppingCondition>
     IMissionControlSequencePropagate<astrogator/IMissionControlSequencePropagate>
     IMissionControlSequenceSequence<astrogator/IMissionControlSequenceSequence>
     IMissionControlSequenceBackwardSequence<astrogator/IMissionControlSequenceBackwardSequence>
     IMissionControlSequenceLaunch<astrogator/IMissionControlSequenceLaunch>
     IDisplaySystemGeodetic<astrogator/IDisplaySystemGeodetic>
     IDisplaySystemGeocentric<astrogator/IDisplaySystemGeocentric>
     IBurnoutCBFCartesian<astrogator/IBurnoutCBFCartesian>
     IBurnoutGeodetic<astrogator/IBurnoutGeodetic>
     IBurnoutGeocentric<astrogator/IBurnoutGeocentric>
     IBurnoutLaunchAzAltitude<astrogator/IBurnoutLaunchAzAltitude>
     IBurnoutLaunchAzRadius<astrogator/IBurnoutLaunchAzRadius>
     IMissionControlSequenceFollow<astrogator/IMissionControlSequenceFollow>
     IMissionControlSequenceManeuver<astrogator/IMissionControlSequenceManeuver>
     IManeuverFinite<astrogator/IManeuverFinite>
     IManeuverImpulsive<astrogator/IManeuverImpulsive>
     IAttitudeControlImpulsiveVelocityVector<astrogator/IAttitudeControlImpulsiveVelocityVector>
     IAttitudeControlImpulsiveAntiVelocityVector<astrogator/IAttitudeControlImpulsiveAntiVelocityVector>
     IAttitudeControlImpulsiveAttitude<astrogator/IAttitudeControlImpulsiveAttitude>
     IAttitudeControlImpulsiveFile<astrogator/IAttitudeControlImpulsiveFile>
     IAttitudeControlImpulsiveThrustVector<astrogator/IAttitudeControlImpulsiveThrustVector>
     IAttitudeControlFiniteAntiVelocityVector<astrogator/IAttitudeControlFiniteAntiVelocityVector>
     IAttitudeControlFiniteAttitude<astrogator/IAttitudeControlFiniteAttitude>
     IAttitudeControlFiniteFile<astrogator/IAttitudeControlFiniteFile>
     IAttitudeControlFiniteThrustVector<astrogator/IAttitudeControlFiniteThrustVector>
     IAttitudeControlFiniteTimeVarying<astrogator/IAttitudeControlFiniteTimeVarying>
     IAttitudeControlFiniteVelocityVector<astrogator/IAttitudeControlFiniteVelocityVector>
     IAttitudeControlFinitePlugin<astrogator/IAttitudeControlFinitePlugin>
     IAttitudeControlOptimalFiniteLagrange<astrogator/IAttitudeControlOptimalFiniteLagrange>
     IMissionControlSequenceHold<astrogator/IMissionControlSequenceHold>
     IMissionControlSequenceUpdate<astrogator/IMissionControlSequenceUpdate>
     IMissionControlSequenceReturn<astrogator/IMissionControlSequenceReturn>
     IMissionControlSequenceStop<astrogator/IMissionControlSequenceStop>
     IProfile<astrogator/IProfile>
     IProfileCollection<astrogator/IProfileCollection>
     IMissionControlSequenceTargetSequence<astrogator/IMissionControlSequenceTargetSequence>
     IDifferentialCorrectorControl<astrogator/IDifferentialCorrectorControl>
     IDifferentialCorrectorResult<astrogator/IDifferentialCorrectorResult>
     ISearchPluginControl<astrogator/ISearchPluginControl>
     ISearchPluginResult<astrogator/ISearchPluginResult>
     ISearchPluginResultCollection<astrogator/ISearchPluginResultCollection>
     ISearchPluginControlCollection<astrogator/ISearchPluginControlCollection>
     IDifferentialCorrectorControlCollection<astrogator/IDifferentialCorrectorControlCollection>
     IDifferentialCorrectorResultCollection<astrogator/IDifferentialCorrectorResultCollection>
     ITargeterGraphActiveControl<astrogator/ITargeterGraphActiveControl>
     ITargeterGraphResult<astrogator/ITargeterGraphResult>
     ITargeterGraphActiveControlCollection<astrogator/ITargeterGraphActiveControlCollection>
     ITargeterGraphResultCollection<astrogator/ITargeterGraphResultCollection>
     ITargeterGraph<astrogator/ITargeterGraph>
     ITargeterGraphCollection<astrogator/ITargeterGraphCollection>
     IProfileSearchPlugin<astrogator/IProfileSearchPlugin>
     IProfileDifferentialCorrector<astrogator/IProfileDifferentialCorrector>
     IProfileChangeManeuverType<astrogator/IProfileChangeManeuverType>
     IProfileScriptingTool<astrogator/IProfileScriptingTool>
     IProfileChangeReturnSegment<astrogator/IProfileChangeReturnSegment>
     IProfileChangePropagator<astrogator/IProfileChangePropagator>
     IProfileChangeStopSegment<astrogator/IProfileChangeStopSegment>
     IProfileChangeStoppingConditionState<astrogator/IProfileChangeStoppingConditionState>
     IProfileSeedFiniteManeuver<astrogator/IProfileSeedFiniteManeuver>
     IProfileRunOnce<astrogator/IProfileRunOnce>
     IUserVariableDefinition<astrogator/IUserVariableDefinition>
     IUserVariable<astrogator/IUserVariable>
     IUserVariableUpdate<astrogator/IUserVariableUpdate>
     IProfileSNOPTOptimizer<astrogator/IProfileSNOPTOptimizer>
     ISNOPTControl<astrogator/ISNOPTControl>
     ISNOPTResult<astrogator/ISNOPTResult>
     IProfileIPOPTOptimizer<astrogator/IProfileIPOPTOptimizer>
     IIPOPTControl<astrogator/IIPOPTControl>
     IIPOPTResult<astrogator/IIPOPTResult>
     IManeuverOptimalFinite<astrogator/IManeuverOptimalFinite>
     IManeuverOptimalFiniteSteeringNodeElement<astrogator/IManeuverOptimalFiniteSteeringNodeElement>
     IProfileLambertProfile<astrogator/IProfileLambertProfile>
     IProfileLambertSearchProfile<astrogator/IProfileLambertSearchProfile>
     IProfileGoldenSection<astrogator/IProfileGoldenSection>
     IProfileGridSearch<astrogator/IProfileGridSearch>
     ICalcObjectLinkEmbedControlCollection<astrogator/ICalcObjectLinkEmbedControlCollection>
     IProfileBisection<astrogator/IProfileBisection>
     IBisectionControl<astrogator/IBisectionControl>
     IStateCalcHeightAboveTerrain<astrogator/IStateCalcHeightAboveTerrain>
     IStateCalcEpoch<astrogator/IStateCalcEpoch>
     IStateCalcOrbitDelaunayG<astrogator/IStateCalcOrbitDelaunayG>
     IStateCalcOrbitDelaunayH<astrogator/IStateCalcOrbitDelaunayH>
     IStateCalcOrbitDelaunayL<astrogator/IStateCalcOrbitDelaunayL>
     IStateCalcOrbitSemiLatusRectum<astrogator/IStateCalcOrbitSemiLatusRectum>
     IStateCalcJacobiConstant<astrogator/IStateCalcJacobiConstant>
     IStateCalcJacobiOsculating<astrogator/IStateCalcJacobiOsculating>
     IStateCalcCartesianElem<astrogator/IStateCalcCartesianElem>
     IStateCalcCartSTMElem<astrogator/IStateCalcCartSTMElem>
     IStateCalcSTMEigenval<astrogator/IStateCalcSTMEigenval>
     IStateCalcSTMEigenvecElem<astrogator/IStateCalcSTMEigenvecElem>
     IStateCalcEnvironment<astrogator/IStateCalcEnvironment>
     IStateCalcEquinoctialElem<astrogator/IStateCalcEquinoctialElem>
     IStateCalcDamageFlux<astrogator/IStateCalcDamageFlux>
     IStateCalcDamageMassFlux<astrogator/IStateCalcDamageMassFlux>
     IStateCalcMagnitudeFieldDipoleL<astrogator/IStateCalcMagnitudeFieldDipoleL>
     IStateCalcSEETMagnitudeFieldFieldLineSepAngle<astrogator/IStateCalcSEETMagnitudeFieldFieldLineSepAngle>
     IStateCalcImpactFlux<astrogator/IStateCalcImpactFlux>
     IStateCalcImpactMassFlux<astrogator/IStateCalcImpactMassFlux>
     IStateCalcSEETSAAFlux<astrogator/IStateCalcSEETSAAFlux>
     IStateCalcSEETVehTemp<astrogator/IStateCalcSEETVehTemp>
     IStateCalcCloseApproachBearing<astrogator/IStateCalcCloseApproachBearing>
     IStateCalcCloseApproachMagnitude<astrogator/IStateCalcCloseApproachMagnitude>
     IStateCalcCloseApproachTheta<astrogator/IStateCalcCloseApproachTheta>
     IStateCalcCloseApproachX<astrogator/IStateCalcCloseApproachX>
     IStateCalcCloseApproachY<astrogator/IStateCalcCloseApproachY>
     IStateCalcCloseApproachCosBearing<astrogator/IStateCalcCloseApproachCosBearing>
     IStateCalcRelGroundTrackError<astrogator/IStateCalcRelGroundTrackError>
     IStateCalcRelAtAOLMaster<astrogator/IStateCalcRelAtAOLMaster>
     IStateCalcDeltaFromMaster<astrogator/IStateCalcDeltaFromMaster>
     IStateCalcLonDriftRate<astrogator/IStateCalcLonDriftRate>
     IStateCalcMeanEarthLon<astrogator/IStateCalcMeanEarthLon>
     IStateCalcRectifiedLon<astrogator/IStateCalcRectifiedLon>
     IStateCalcTrueLongitude<astrogator/IStateCalcTrueLongitude>
     IStateCalcGeodeticTrueLongitude<astrogator/IStateCalcGeodeticTrueLongitude>
     IStateCalcGeodeticTrueLongitudeAtTimeOfPerigee<astrogator/IStateCalcGeodeticTrueLongitudeAtTimeOfPerigee>
     IStateCalcMeanRightAscension<astrogator/IStateCalcMeanRightAscension>
     IStateCalcGeodeticMeanRightAscension<astrogator/IStateCalcGeodeticMeanRightAscension>
     IStateCalcTwoBodyDriftRate<astrogator/IStateCalcTwoBodyDriftRate>
     IStateCalcDriftRateFactor<astrogator/IStateCalcDriftRateFactor>
     IStateCalcEccentricityX<astrogator/IStateCalcEccentricityX>
     IStateCalcEccentricityY<astrogator/IStateCalcEccentricityY>
     IStateCalcInclinationX<astrogator/IStateCalcInclinationX>
     IStateCalcInclinationY<astrogator/IStateCalcInclinationY>
     IStateCalcUnitAngularMomentumX<astrogator/IStateCalcUnitAngularMomentumX>
     IStateCalcUnitAngularMomentumY<astrogator/IStateCalcUnitAngularMomentumY>
     IStateCalcUnitAngularMomentumZ<astrogator/IStateCalcUnitAngularMomentumZ>
     IStateCalcGeodeticElem<astrogator/IStateCalcGeodeticElem>
     IStateCalcRepeatingGroundTrackErr<astrogator/IStateCalcRepeatingGroundTrackErr>
     IStateCalcAltitudeOfApoapsis<astrogator/IStateCalcAltitudeOfApoapsis>
     IStateCalcAltitudeOfPeriapsis<astrogator/IStateCalcAltitudeOfPeriapsis>
     IStateCalcArgOfLat<astrogator/IStateCalcArgOfLat>
     IStateCalcArgOfPeriapsis<astrogator/IStateCalcArgOfPeriapsis>
     IStateCalcEccentricityAnomaly<astrogator/IStateCalcEccentricityAnomaly>
     IStateCalcEccentricity<astrogator/IStateCalcEccentricity>
     IStateCalcInclination<astrogator/IStateCalcInclination>
     IStateCalcLonOfAscNode<astrogator/IStateCalcLonOfAscNode>
     IStateCalcMeanAnomaly<astrogator/IStateCalcMeanAnomaly>
     IStateCalcMeanMotion<astrogator/IStateCalcMeanMotion>
     IStateCalcOrbitPeriod<astrogator/IStateCalcOrbitPeriod>
     IStateCalcNumRevs<astrogator/IStateCalcNumRevs>
     IStateCalcRAAN<astrogator/IStateCalcRAAN>
     IStateCalcRadOfApoapsis<astrogator/IStateCalcRadOfApoapsis>
     IStateCalcRadOfPeriapsis<astrogator/IStateCalcRadOfPeriapsis>
     IStateCalcSemiMajorAxis<astrogator/IStateCalcSemiMajorAxis>
     IStateCalcTimePastAscNode<astrogator/IStateCalcTimePastAscNode>
     IStateCalcTimePastPeriapsis<astrogator/IStateCalcTimePastPeriapsis>
     IStateCalcDeltaV<astrogator/IStateCalcDeltaV>
     IStateCalcDeltaVSquared<astrogator/IStateCalcDeltaVSquared>
     IStateCalcMissionControlSequenceDeltaV<astrogator/IStateCalcMissionControlSequenceDeltaV>
     IStateCalcMissionControlSequenceDeltaVSquared<astrogator/IStateCalcMissionControlSequenceDeltaVSquared>
     IStateCalcSequenceDeltaV<astrogator/IStateCalcSequenceDeltaV>
     IStateCalcSequenceDeltaVSquared<astrogator/IStateCalcSequenceDeltaVSquared>
     IStateCalcFuelMass<astrogator/IStateCalcFuelMass>
     IStateCalcDensity<astrogator/IStateCalcDensity>
     IStateCalcInertialDeltaVMagnitude<astrogator/IStateCalcInertialDeltaVMagnitude>
     IStateCalcInertialDeltaVx<astrogator/IStateCalcInertialDeltaVx>
     IStateCalcInertialDeltaVy<astrogator/IStateCalcInertialDeltaVy>
     IStateCalcInertialDeltaVz<astrogator/IStateCalcInertialDeltaVz>
     IStateCalcManeuverSpecificImpulse<astrogator/IStateCalcManeuverSpecificImpulse>
     IStateCalcPressure<astrogator/IStateCalcPressure>
     IStateCalcTemperature<astrogator/IStateCalcTemperature>
     IStateCalcVectorX<astrogator/IStateCalcVectorX>
     IStateCalcVectorY<astrogator/IStateCalcVectorY>
     IStateCalcVectorZ<astrogator/IStateCalcVectorZ>
     IStateCalcMass<astrogator/IStateCalcMass>
     IStateCalcManeuverTotalMassFlowRate<astrogator/IStateCalcManeuverTotalMassFlowRate>
     IStateCalcAbsoluteValue<astrogator/IStateCalcAbsoluteValue>
     IStateCalcDifference<astrogator/IStateCalcDifference>
     IStateCalcDifferenceOtherSegment<astrogator/IStateCalcDifferenceOtherSegment>
     IStateCalcPositionDifferenceOtherSegment<astrogator/IStateCalcPositionDifferenceOtherSegment>
     IStateCalcVelDifferenceOtherSegment<astrogator/IStateCalcVelDifferenceOtherSegment>
     IStateCalcPositionVelDifferenceOtherSegment<astrogator/IStateCalcPositionVelDifferenceOtherSegment>
     IStateCalcValueAtSegment<astrogator/IStateCalcValueAtSegment>
     IStateCalcMaxValue<astrogator/IStateCalcMaxValue>
     IStateCalcMinValue<astrogator/IStateCalcMinValue>
     IStateCalcMeanValue<astrogator/IStateCalcMeanValue>
     IStateCalcMedianValue<astrogator/IStateCalcMedianValue>
     IStateCalcStandardDeviation<astrogator/IStateCalcStandardDeviation>
     IStateCalcNegative<astrogator/IStateCalcNegative>
     IStateCalcTrueAnomaly<astrogator/IStateCalcTrueAnomaly>
     IBDotRCalc<astrogator/IBDotRCalc>
     IBDotTCalc<astrogator/IBDotTCalc>
     IBMagnitudeCalc<astrogator/IBMagnitudeCalc>
     IBThetaCalc<astrogator/IBThetaCalc>
     IStateCalcDeltaDec<astrogator/IStateCalcDeltaDec>
     IStateCalcDeltaRA<astrogator/IStateCalcDeltaRA>
     IStateCalcBetaAngle<astrogator/IStateCalcBetaAngle>
     IStateCalcLocalApparentSolarLon<astrogator/IStateCalcLocalApparentSolarLon>
     IStateCalcLonOfPeriapsis<astrogator/IStateCalcLonOfPeriapsis>
     IStateCalcOrbitStateValue<astrogator/IStateCalcOrbitStateValue>
     IStateCalcSignedEccentricity<astrogator/IStateCalcSignedEccentricity>
     IStateCalcTrueLon<astrogator/IStateCalcTrueLon>
     IStateCalcPower<astrogator/IStateCalcPower>
     IStateCalcRelMotion<astrogator/IStateCalcRelMotion>
     IStateCalcSolarBetaAngle<astrogator/IStateCalcSolarBetaAngle>
     IStateCalcSolarInPlaneAngle<astrogator/IStateCalcSolarInPlaneAngle>
     IStateCalcRelPositionDecAngle<astrogator/IStateCalcRelPositionDecAngle>
     IStateCalcRelPositionInPlaneAngle<astrogator/IStateCalcRelPositionInPlaneAngle>
     IStateCalcRelativeInclination<astrogator/IStateCalcRelativeInclination>
     IStateCalcCurvilinearRelMotion<astrogator/IStateCalcCurvilinearRelMotion>
     IStateCalcCustomFunction<astrogator/IStateCalcCustomFunction>
     IStateCalcScript<astrogator/IStateCalcScript>
     IStateCalcCd<astrogator/IStateCalcCd>
     IStateCalcCr<astrogator/IStateCalcCr>
     IStateCalcDragArea<astrogator/IStateCalcDragArea>
     IStateCalcRadiationPressureArea<astrogator/IStateCalcRadiationPressureArea>
     IStateCalcRadiationPressureCoefficient<astrogator/IStateCalcRadiationPressureCoefficient>
     IStateCalcSRPArea<astrogator/IStateCalcSRPArea>
     IStateCalcCosOfVerticalFPA<astrogator/IStateCalcCosOfVerticalFPA>
     IStateCalcDec<astrogator/IStateCalcDec>
     IStateCalcFPA<astrogator/IStateCalcFPA>
     IStateCalcRMagnitude<astrogator/IStateCalcRMagnitude>
     IStateCalcRA<astrogator/IStateCalcRA>
     IStateCalcVMagnitude<astrogator/IStateCalcVMagnitude>
     IStateCalcVelAz<astrogator/IStateCalcVelAz>
     IStateCalcC3Energy<astrogator/IStateCalcC3Energy>
     IStateCalcInAsympDec<astrogator/IStateCalcInAsympDec>
     IStateCalcInAsympRA<astrogator/IStateCalcInAsympRA>
     IStateCalcInVelAzAtPeriapsis<astrogator/IStateCalcInVelAzAtPeriapsis>
     IStateCalcOutAsympDec<astrogator/IStateCalcOutAsympDec>
     IStateCalcOutAsympRA<astrogator/IStateCalcOutAsympRA>
     IStateCalcOutVelAzAtPeriapsis<astrogator/IStateCalcOutVelAzAtPeriapsis>
     IStateCalcDuration<astrogator/IStateCalcDuration>
     IStateCalcUserValue<astrogator/IStateCalcUserValue>
     IStateCalcVectorGeometryToolAngle<astrogator/IStateCalcVectorGeometryToolAngle>
     IStateCalcAngle<astrogator/IStateCalcAngle>
     IStateCalcDotProduct<astrogator/IStateCalcDotProduct>
     IStateCalcVectorDec<astrogator/IStateCalcVectorDec>
     IStateCalcVectorMagnitude<astrogator/IStateCalcVectorMagnitude>
     IStateCalcVectorRA<astrogator/IStateCalcVectorRA>
     IStateCalcOnePointAccess<astrogator/IStateCalcOnePointAccess>
     IStateCalcDifferenceAcrossSegmentsOtherSat<astrogator/IStateCalcDifferenceAcrossSegmentsOtherSat>
     IStateCalcValueAtSegmentOtherSat<astrogator/IStateCalcValueAtSegmentOtherSat>
     IStateCalcRARate<astrogator/IStateCalcRARate>
     IStateCalcDecRate<astrogator/IStateCalcDecRate>
     IStateCalcRangeRate<astrogator/IStateCalcRangeRate>
     IStateCalcGravitationalParameter<astrogator/IStateCalcGravitationalParameter>
     IStateCalcReferenceRadius<astrogator/IStateCalcReferenceRadius>
     IStateCalcGravCoeff<astrogator/IStateCalcGravCoeff>
     IStateCalcSpeedOfLight<astrogator/IStateCalcSpeedOfLight>
     IStateCalcPi<astrogator/IStateCalcPi>
     IStateCalcScalar<astrogator/IStateCalcScalar>
     IStateCalcApparentSolarTime<astrogator/IStateCalcApparentSolarTime>
     IStateCalcEarthMeanSolarTime<astrogator/IStateCalcEarthMeanSolarTime>
     IStateCalcEarthMeanLocTimeAN<astrogator/IStateCalcEarthMeanLocTimeAN>
     ICentralBodyCollection<astrogator/ICentralBodyCollection>
     ICentralBodyEphemeris<astrogator/ICentralBodyEphemeris>
     ICentralBodyGravityModel<astrogator/ICentralBodyGravityModel>
     ICentralBodyShape<astrogator/ICentralBodyShape>
     ICentralBodyShapeSphere<astrogator/ICentralBodyShapeSphere>
     ICentralBodyShapeOblateSpheroid<astrogator/ICentralBodyShapeOblateSpheroid>
     ICentralBodyShapeTriaxialEllipsoid<astrogator/ICentralBodyShapeTriaxialEllipsoid>
     ICentralBodyAttitude<astrogator/ICentralBodyAttitude>
     ICentralBodyAttitudeRotationCoefficientsFile<astrogator/ICentralBodyAttitudeRotationCoefficientsFile>
     ICentralBodyAttitudeIAU1994<astrogator/ICentralBodyAttitudeIAU1994>
     ICentralBodyEphemerisAnalyticOrbit<astrogator/ICentralBodyEphemerisAnalyticOrbit>
     ICentralBodyEphemerisJPLSpice<astrogator/ICentralBodyEphemerisJPLSpice>
     ICentralBodyEphemerisFile<astrogator/ICentralBodyEphemerisFile>
     ICentralBodyEphemerisJPLDesignExplorerOptimizer<astrogator/ICentralBodyEphemerisJPLDesignExplorerOptimizer>
     ICentralBodyEphemerisPlanetary<astrogator/ICentralBodyEphemerisPlanetary>
     IAstrogatorCentralBody<astrogator/IAstrogatorCentralBody>
     IPowerInternal<astrogator/IPowerInternal>
     IPowerProcessed<astrogator/IPowerProcessed>
     IPowerSolarArray<astrogator/IPowerSolarArray>
     IGeneralRelativityFunction<astrogator/IGeneralRelativityFunction>
     IStateTransformationFunction<astrogator/IStateTransformationFunction>
     ICR3BPFunc<astrogator/ICR3BPFunc>
     IER3BPFunc<astrogator/IER3BPFunc>
     IRadiationPressureFunction<astrogator/IRadiationPressureFunction>
     IYarkovskyFunc<astrogator/IYarkovskyFunc>
     IBlendedDensity<astrogator/IBlendedDensity>
     IDragModelPlugin<astrogator/IDragModelPlugin>
     ICira72Function<astrogator/ICira72Function>
     IExponential<astrogator/IExponential>
     IHarrisPriester<astrogator/IHarrisPriester>
     IDensityModelPlugin<astrogator/IDensityModelPlugin>
     IJacchiaRoberts<astrogator/IJacchiaRoberts>
     IJacchiaBowman2008<astrogator/IJacchiaBowman2008>
     IJacchia_1960<astrogator/IJacchia_1960>
     IJacchia_1970<astrogator/IJacchia_1970>
     IJacchia_1971<astrogator/IJacchia_1971>
     IMSISE_1990<astrogator/IMSISE_1990>
     IMSIS_1986<astrogator/IMSIS_1986>
     INRLMSISE_2000<astrogator/INRLMSISE_2000>
     IUS_Standard_Atmosphere<astrogator/IUS_Standard_Atmosphere>
     IMarsGRAM37<astrogator/IMarsGRAM37>
     IMarsGRAM2005<astrogator/IMarsGRAM2005>
     IVenusGRAM2005<astrogator/IVenusGRAM2005>
     IMarsGRAM2010<astrogator/IMarsGRAM2010>
     IMarsGRAM2001<astrogator/IMarsGRAM2001>
     IMarsGRAM2000<astrogator/IMarsGRAM2000>
     IDTM2012<astrogator/IDTM2012>
     IDTM2020<astrogator/IDTM2020>
     IGravityFieldFunction<astrogator/IGravityFieldFunction>
     IPointMassFunction<astrogator/IPointMassFunction>
     ITwoBodyFunction<astrogator/ITwoBodyFunction>
     IHPOPPluginFunction<astrogator/IHPOPPluginFunction>
     IEOMFuncPluginFunction<astrogator/IEOMFuncPluginFunction>
     ISRPAeroT20<astrogator/ISRPAeroT20>
     ISRPAeroT30<astrogator/ISRPAeroT30>
     ISRPGSPM04aIIA<astrogator/ISRPGSPM04aIIA>
     ISRPGSPM04aIIR<astrogator/ISRPGSPM04aIIR>
     ISRPGSPM04aeIIA<astrogator/ISRPGSPM04aeIIA>
     ISRPGSPM04aeIIR<astrogator/ISRPGSPM04aeIIR>
     ISRPSpherical<astrogator/ISRPSpherical>
     ISRPNPlate<astrogator/ISRPNPlate>
     ISRPTabAreaVec<astrogator/ISRPTabAreaVec>
     ISRPVariableArea<astrogator/ISRPVariableArea>
     IThirdBodyFunction<astrogator/IThirdBodyFunction>
     ISRPReflectionPlugin<astrogator/ISRPReflectionPlugin>
     IEngineModelThrustCoefficients<astrogator/IEngineModelThrustCoefficients>
     IEngineModelIspCoefficients<astrogator/IEngineModelIspCoefficients>
     IEngineConstAcc<astrogator/IEngineConstAcc>
     IEngineConstant<astrogator/IEngineConstant>
     IEngineDefinition<astrogator/IEngineDefinition>
     IEngineThrottleTable<astrogator/IEngineThrottleTable>
     IEngineIon<astrogator/IEngineIon>
     IEngineCustom<astrogator/IEngineCustom>
     IEnginePlugin<astrogator/IEnginePlugin>
     IEngineModelPoly<astrogator/IEngineModelPoly>
     IDesignCR3BPObjectCollection<astrogator/IDesignCR3BPObjectCollection>
     IDesignER3BPObjectCollection<astrogator/IDesignER3BPObjectCollection>
     IDesignCR3BPSetup<astrogator/IDesignCR3BPSetup>
     IDesignCR3BPObject<astrogator/IDesignCR3BPObject>
     IDesignER3BPSetup<astrogator/IDesignER3BPSetup>
     IDesignER3BPObject<astrogator/IDesignER3BPObject>
     IThruster<astrogator/IThruster>
     IThrusterSetCollection<astrogator/IThrusterSetCollection>
     IThrusterSet<astrogator/IThrusterSet>
     IAsTriggerCondition<astrogator/IAsTriggerCondition>
     ICustomFunctionScriptEngine<astrogator/ICustomFunctionScriptEngine>
     INumericalIntegrator<astrogator/INumericalIntegrator>
     IPropagatorFunctionCollection<astrogator/IPropagatorFunctionCollection>
     INumericalPropagatorWrapper<astrogator/INumericalPropagatorWrapper>
     INumericalPropagatorWrapperCR3BP<astrogator/INumericalPropagatorWrapperCR3BP>
     IBulirschStoerIntegrator<astrogator/IBulirschStoerIntegrator>
     IGaussJacksonIntegrator<astrogator/IGaussJacksonIntegrator>
     IRungeKutta2nd3rd<astrogator/IRungeKutta2nd3rd>
     IRungeKutta4th<astrogator/IRungeKutta4th>
     IRungeKutta4th5th<astrogator/IRungeKutta4th5th>
     IRungeKutta4thAdapt<astrogator/IRungeKutta4thAdapt>
     IRungeKuttaF7th8th<astrogator/IRungeKuttaF7th8th>
     IRungeKuttaV8th9th<astrogator/IRungeKuttaV8th9th>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     DriverMissionControlSequence<astrogator/DriverMissionControlSequence>
     MissionControlSequenceSegmentCollection<astrogator/MissionControlSequenceSegmentCollection>
     MissionControlSequenceEnd<astrogator/MissionControlSequenceEnd>
     MissionControlSequenceInitialState<astrogator/MissionControlSequenceInitialState>
     SpacecraftParameters<astrogator/SpacecraftParameters>
     FuelTank<astrogator/FuelTank>
     ElementCartesian<astrogator/ElementCartesian>
     ElementKeplerian<astrogator/ElementKeplerian>
     ElementEquinoctial<astrogator/ElementEquinoctial>
     ElementDelaunay<astrogator/ElementDelaunay>
     ElementMixedSpherical<astrogator/ElementMixedSpherical>
     ElementSpherical<astrogator/ElementSpherical>
     ElementTargetVectorIncomingAsymptote<astrogator/ElementTargetVectorIncomingAsymptote>
     ElementTargetVectorOutgoingAsymptote<astrogator/ElementTargetVectorOutgoingAsymptote>
     ElementGeodetic<astrogator/ElementGeodetic>
     ElementBPlane<astrogator/ElementBPlane>
     ElementSphericalRangeRate<astrogator/ElementSphericalRangeRate>
     MissionControlSequencePropagate<astrogator/MissionControlSequencePropagate>
     State<astrogator/State>
     StoppingConditionCollection<astrogator/StoppingConditionCollection>
     AccessStoppingCondition<astrogator/AccessStoppingCondition>
     LightingStoppingCondition<astrogator/LightingStoppingCondition>
     StoppingCondition<astrogator/StoppingCondition>
     StoppingConditionElement<astrogator/StoppingConditionElement>
     MissionControlSequenceSequence<astrogator/MissionControlSequenceSequence>
     MissionControlSequenceBackwardSequence<astrogator/MissionControlSequenceBackwardSequence>
     MissionControlSequenceLaunch<astrogator/MissionControlSequenceLaunch>
     DisplaySystemGeodetic<astrogator/DisplaySystemGeodetic>
     DisplaySystemGeocentric<astrogator/DisplaySystemGeocentric>
     BurnoutGeodetic<astrogator/BurnoutGeodetic>
     BurnoutCBFCartesian<astrogator/BurnoutCBFCartesian>
     BurnoutGeocentric<astrogator/BurnoutGeocentric>
     BurnoutLaunchAzAltitude<astrogator/BurnoutLaunchAzAltitude>
     BurnoutLaunchAzRadius<astrogator/BurnoutLaunchAzRadius>
     BurnoutVelocity<astrogator/BurnoutVelocity>
     MissionControlSequenceFollow<astrogator/MissionControlSequenceFollow>
     MissionControlSequenceManeuver<astrogator/MissionControlSequenceManeuver>
     ManeuverFinite<astrogator/ManeuverFinite>
     ManeuverImpulsive<astrogator/ManeuverImpulsive>
     AttitudeControlImpulsiveVelocityVector<astrogator/AttitudeControlImpulsiveVelocityVector>
     AttitudeControlImpulsiveAntiVelocityVector<astrogator/AttitudeControlImpulsiveAntiVelocityVector>
     AttitudeControlImpulsiveAttitude<astrogator/AttitudeControlImpulsiveAttitude>
     AttitudeControlImpulsiveFile<astrogator/AttitudeControlImpulsiveFile>
     AttitudeControlImpulsiveThrustVector<astrogator/AttitudeControlImpulsiveThrustVector>
     AttitudeControlFiniteAntiVelocityVector<astrogator/AttitudeControlFiniteAntiVelocityVector>
     AttitudeControlFiniteAttitude<astrogator/AttitudeControlFiniteAttitude>
     AttitudeControlFiniteFile<astrogator/AttitudeControlFiniteFile>
     AttitudeControlFiniteThrustVector<astrogator/AttitudeControlFiniteThrustVector>
     AttitudeControlFiniteTimeVarying<astrogator/AttitudeControlFiniteTimeVarying>
     AttitudeControlFiniteVelocityVector<astrogator/AttitudeControlFiniteVelocityVector>
     AttitudeControlFinitePlugin<astrogator/AttitudeControlFinitePlugin>
     AttitudeControlOptimalFiniteLagrange<astrogator/AttitudeControlOptimalFiniteLagrange>
     ManeuverFinitePropagator<astrogator/ManeuverFinitePropagator>
     MissionControlSequenceHold<astrogator/MissionControlSequenceHold>
     MissionControlSequenceUpdate<astrogator/MissionControlSequenceUpdate>
     MissionControlSequenceReturn<astrogator/MissionControlSequenceReturn>
     MissionControlSequenceStop<astrogator/MissionControlSequenceStop>
     MissionControlSequenceTargetSequence<astrogator/MissionControlSequenceTargetSequence>
     ProfileCollection<astrogator/ProfileCollection>
     MissionControlSequenceOptions<astrogator/MissionControlSequenceOptions>
     CalcObjectCollection<astrogator/CalcObjectCollection>
     ConstraintCollection<astrogator/ConstraintCollection>
     PluginProperties<astrogator/PluginProperties>
     ProfileSearchPlugin<astrogator/ProfileSearchPlugin>
     TargeterGraph<astrogator/TargeterGraph>
     TargeterGraphCollection<astrogator/TargeterGraphCollection>
     TargeterGraphResultCollection<astrogator/TargeterGraphResultCollection>
     TargeterGraphActiveControlCollection<astrogator/TargeterGraphActiveControlCollection>
     TargeterGraphActiveControl<astrogator/TargeterGraphActiveControl>
     TargeterGraphResult<astrogator/TargeterGraphResult>
     ProfileDifferentialCorrector<astrogator/ProfileDifferentialCorrector>
     ProfileScriptingTool<astrogator/ProfileScriptingTool>
     DifferentialCorrectorControl<astrogator/DifferentialCorrectorControl>
     DifferentialCorrectorResult<astrogator/DifferentialCorrectorResult>
     DifferentialCorrectorControlCollection<astrogator/DifferentialCorrectorControlCollection>
     DifferentialCorrectorResultCollection<astrogator/DifferentialCorrectorResultCollection>
     SearchPluginControl<astrogator/SearchPluginControl>
     SearchPluginControlCollection<astrogator/SearchPluginControlCollection>
     SearchPluginResult<astrogator/SearchPluginResult>
     SearchPluginResultCollection<astrogator/SearchPluginResultCollection>
     ProfileChangeManeuverType<astrogator/ProfileChangeManeuverType>
     ProfileChangeReturnSegment<astrogator/ProfileChangeReturnSegment>
     ProfileChangePropagator<astrogator/ProfileChangePropagator>
     ProfileChangeStopSegment<astrogator/ProfileChangeStopSegment>
     ProfileChangeStoppingConditionState<astrogator/ProfileChangeStoppingConditionState>
     ProfileSeedFiniteManeuver<astrogator/ProfileSeedFiniteManeuver>
     ProfileRunOnce<astrogator/ProfileRunOnce>
     BPlaneCollection<astrogator/BPlaneCollection>
     StateCalcDamageFlux<astrogator/StateCalcDamageFlux>
     StateCalcDamageMassFlux<astrogator/StateCalcDamageMassFlux>
     StateCalcMagnitudeFieldDipoleL<astrogator/StateCalcMagnitudeFieldDipoleL>
     StateCalcSEETMagnitudeFieldFieldLineSepAngle<astrogator/StateCalcSEETMagnitudeFieldFieldLineSepAngle>
     StateCalcImpactFlux<astrogator/StateCalcImpactFlux>
     StateCalcImpactMassFlux<astrogator/StateCalcImpactMassFlux>
     StateCalcSEETSAAFlux<astrogator/StateCalcSEETSAAFlux>
     StateCalcSEETVehTemp<astrogator/StateCalcSEETVehTemp>
     StateCalcEpoch<astrogator/StateCalcEpoch>
     StateCalcJacobiConstant<astrogator/StateCalcJacobiConstant>
     StateCalcJacobiOsculating<astrogator/StateCalcJacobiOsculating>
     StateCalcCartesianElem<astrogator/StateCalcCartesianElem>
     StateCalcCartSTMElem<astrogator/StateCalcCartSTMElem>
     StateCalcSTMEigenval<astrogator/StateCalcSTMEigenval>
     StateCalcSTMEigenvecElem<astrogator/StateCalcSTMEigenvecElem>
     StateCalcEnvironment<astrogator/StateCalcEnvironment>
     StateCalcOrbitDelaunayG<astrogator/StateCalcOrbitDelaunayG>
     StateCalcOrbitDelaunayH<astrogator/StateCalcOrbitDelaunayH>
     StateCalcOrbitDelaunayL<astrogator/StateCalcOrbitDelaunayL>
     StateCalcOrbitSemiLatusRectum<astrogator/StateCalcOrbitSemiLatusRectum>
     StateCalcEquinoctialElem<astrogator/StateCalcEquinoctialElem>
     StateCalcCloseApproachBearing<astrogator/StateCalcCloseApproachBearing>
     StateCalcCloseApproachMagnitude<astrogator/StateCalcCloseApproachMagnitude>
     StateCalcCloseApproachTheta<astrogator/StateCalcCloseApproachTheta>
     StateCalcCloseApproachX<astrogator/StateCalcCloseApproachX>
     StateCalcCloseApproachY<astrogator/StateCalcCloseApproachY>
     StateCalcCloseApproachCosBearing<astrogator/StateCalcCloseApproachCosBearing>
     StateCalcRelGroundTrackError<astrogator/StateCalcRelGroundTrackError>
     StateCalcRelAtAOLMaster<astrogator/StateCalcRelAtAOLMaster>
     StateCalcDeltaFromMaster<astrogator/StateCalcDeltaFromMaster>
     StateCalcLonDriftRate<astrogator/StateCalcLonDriftRate>
     StateCalcMeanEarthLon<astrogator/StateCalcMeanEarthLon>
     StateCalcRectifiedLon<astrogator/StateCalcRectifiedLon>
     StateCalcTrueLongitude<astrogator/StateCalcTrueLongitude>
     StateCalcGeodeticTrueLongitude<astrogator/StateCalcGeodeticTrueLongitude>
     StateCalcGeodeticTrueLongitudeAtTimeOfPerigee<astrogator/StateCalcGeodeticTrueLongitudeAtTimeOfPerigee>
     StateCalcMeanRightAscension<astrogator/StateCalcMeanRightAscension>
     StateCalcGeodeticMeanRightAscension<astrogator/StateCalcGeodeticMeanRightAscension>
     StateCalcTwoBodyDriftRate<astrogator/StateCalcTwoBodyDriftRate>
     StateCalcDriftRateFactor<astrogator/StateCalcDriftRateFactor>
     StateCalcEccentricityX<astrogator/StateCalcEccentricityX>
     StateCalcEccentricityY<astrogator/StateCalcEccentricityY>
     StateCalcInclinationX<astrogator/StateCalcInclinationX>
     StateCalcInclinationY<astrogator/StateCalcInclinationY>
     StateCalcUnitAngularMomentumX<astrogator/StateCalcUnitAngularMomentumX>
     StateCalcUnitAngularMomentumY<astrogator/StateCalcUnitAngularMomentumY>
     StateCalcUnitAngularMomentumZ<astrogator/StateCalcUnitAngularMomentumZ>
     StateCalcHeightAboveTerrain<astrogator/StateCalcHeightAboveTerrain>
     StateCalcGeodeticElem<astrogator/StateCalcGeodeticElem>
     StateCalcRepeatingGroundTrackErr<astrogator/StateCalcRepeatingGroundTrackErr>
     StateCalcAltitudeOfApoapsis<astrogator/StateCalcAltitudeOfApoapsis>
     StateCalcAltitudeOfPeriapsis<astrogator/StateCalcAltitudeOfPeriapsis>
     StateCalcArgOfLat<astrogator/StateCalcArgOfLat>
     StateCalcArgOfPeriapsis<astrogator/StateCalcArgOfPeriapsis>
     StateCalcEccentricityAnomaly<astrogator/StateCalcEccentricityAnomaly>
     StateCalcLonOfAscNode<astrogator/StateCalcLonOfAscNode>
     StateCalcMeanMotion<astrogator/StateCalcMeanMotion>
     StateCalcOrbitPeriod<astrogator/StateCalcOrbitPeriod>
     StateCalcNumRevs<astrogator/StateCalcNumRevs>
     StateCalcRadOfApoapsis<astrogator/StateCalcRadOfApoapsis>
     StateCalcRadOfPeriapsis<astrogator/StateCalcRadOfPeriapsis>
     StateCalcSemiMajorAxis<astrogator/StateCalcSemiMajorAxis>
     StateCalcTimePastAscNode<astrogator/StateCalcTimePastAscNode>
     StateCalcTimePastPeriapsis<astrogator/StateCalcTimePastPeriapsis>
     StateCalcTrueAnomaly<astrogator/StateCalcTrueAnomaly>
     StateCalcDeltaV<astrogator/StateCalcDeltaV>
     StateCalcDeltaVSquared<astrogator/StateCalcDeltaVSquared>
     StateCalcMissionControlSequenceDeltaV<astrogator/StateCalcMissionControlSequenceDeltaV>
     StateCalcMissionControlSequenceDeltaVSquared<astrogator/StateCalcMissionControlSequenceDeltaVSquared>
     StateCalcSequenceDeltaV<astrogator/StateCalcSequenceDeltaV>
     StateCalcSequenceDeltaVSquared<astrogator/StateCalcSequenceDeltaVSquared>
     StateCalcFuelMass<astrogator/StateCalcFuelMass>
     StateCalcDensity<astrogator/StateCalcDensity>
     StateCalcInertialDeltaVMagnitude<astrogator/StateCalcInertialDeltaVMagnitude>
     StateCalcInertialDeltaVx<astrogator/StateCalcInertialDeltaVx>
     StateCalcInertialDeltaVy<astrogator/StateCalcInertialDeltaVy>
     StateCalcInertialDeltaVz<astrogator/StateCalcInertialDeltaVz>
     StateCalcManeuverSpecificImpulse<astrogator/StateCalcManeuverSpecificImpulse>
     StateCalcPressure<astrogator/StateCalcPressure>
     StateCalcTemperature<astrogator/StateCalcTemperature>
     StateCalcVectorY<astrogator/StateCalcVectorY>
     StateCalcVectorZ<astrogator/StateCalcVectorZ>
     StateCalcMass<astrogator/StateCalcMass>
     StateCalcManeuverTotalMassFlowRate<astrogator/StateCalcManeuverTotalMassFlowRate>
     StateCalcAbsoluteValue<astrogator/StateCalcAbsoluteValue>
     StateCalcDifference<astrogator/StateCalcDifference>
     StateCalcDifferenceOtherSegment<astrogator/StateCalcDifferenceOtherSegment>
     StateCalcPositionDifferenceOtherSegment<astrogator/StateCalcPositionDifferenceOtherSegment>
     StateCalcVelDifferenceOtherSegment<astrogator/StateCalcVelDifferenceOtherSegment>
     StateCalcPositionVelDifferenceOtherSegment<astrogator/StateCalcPositionVelDifferenceOtherSegment>
     StateCalcValueAtSegment<astrogator/StateCalcValueAtSegment>
     StateCalcMaxValue<astrogator/StateCalcMaxValue>
     StateCalcMinValue<astrogator/StateCalcMinValue>
     StateCalcMeanValue<astrogator/StateCalcMeanValue>
     StateCalcMedianValue<astrogator/StateCalcMedianValue>
     StateCalcStandardDeviation<astrogator/StateCalcStandardDeviation>
     StateCalcNegative<astrogator/StateCalcNegative>
     StateCalcEccentricity<astrogator/StateCalcEccentricity>
     StateCalcMeanAnomaly<astrogator/StateCalcMeanAnomaly>
     StateCalcRAAN<astrogator/StateCalcRAAN>
     BDotRCalc<astrogator/BDotRCalc>
     BDotTCalc<astrogator/BDotTCalc>
     BMagnitudeCalc<astrogator/BMagnitudeCalc>
     BThetaCalc<astrogator/BThetaCalc>
     StateCalcDeltaDec<astrogator/StateCalcDeltaDec>
     StateCalcDeltaRA<astrogator/StateCalcDeltaRA>
     StateCalcBetaAngle<astrogator/StateCalcBetaAngle>
     StateCalcLocalApparentSolarLon<astrogator/StateCalcLocalApparentSolarLon>
     StateCalcLonOfPeriapsis<astrogator/StateCalcLonOfPeriapsis>
     StateCalcOrbitStateValue<astrogator/StateCalcOrbitStateValue>
     StateCalcSignedEccentricity<astrogator/StateCalcSignedEccentricity>
     StateCalcInclination<astrogator/StateCalcInclination>
     StateCalcTrueLon<astrogator/StateCalcTrueLon>
     StateCalcPower<astrogator/StateCalcPower>
     StateCalcRelMotion<astrogator/StateCalcRelMotion>
     StateCalcSolarBetaAngle<astrogator/StateCalcSolarBetaAngle>
     StateCalcSolarInPlaneAngle<astrogator/StateCalcSolarInPlaneAngle>
     StateCalcRelPositionDecAngle<astrogator/StateCalcRelPositionDecAngle>
     StateCalcRelPositionInPlaneAngle<astrogator/StateCalcRelPositionInPlaneAngle>
     StateCalcRelativeInclination<astrogator/StateCalcRelativeInclination>
     StateCalcCurvilinearRelMotion<astrogator/StateCalcCurvilinearRelMotion>
     StateCalcCustomFunction<astrogator/StateCalcCustomFunction>
     StateCalcScript<astrogator/StateCalcScript>
     StateCalcCd<astrogator/StateCalcCd>
     StateCalcCr<astrogator/StateCalcCr>
     StateCalcDragArea<astrogator/StateCalcDragArea>
     StateCalcRadiationPressureArea<astrogator/StateCalcRadiationPressureArea>
     StateCalcRadiationPressureCoefficient<astrogator/StateCalcRadiationPressureCoefficient>
     StateCalcSRPArea<astrogator/StateCalcSRPArea>
     StateCalcCosOfVerticalFPA<astrogator/StateCalcCosOfVerticalFPA>
     StateCalcDec<astrogator/StateCalcDec>
     StateCalcFPA<astrogator/StateCalcFPA>
     StateCalcRMagnitude<astrogator/StateCalcRMagnitude>
     StateCalcRA<astrogator/StateCalcRA>
     StateCalcVMagnitude<astrogator/StateCalcVMagnitude>
     StateCalcVelAz<astrogator/StateCalcVelAz>
     StateCalcC3Energy<astrogator/StateCalcC3Energy>
     StateCalcInAsympDec<astrogator/StateCalcInAsympDec>
     StateCalcInAsympRA<astrogator/StateCalcInAsympRA>
     StateCalcInVelAzAtPeriapsis<astrogator/StateCalcInVelAzAtPeriapsis>
     StateCalcOutAsympDec<astrogator/StateCalcOutAsympDec>
     StateCalcOutAsympRA<astrogator/StateCalcOutAsympRA>
     StateCalcOutVelAzAtPeriapsis<astrogator/StateCalcOutVelAzAtPeriapsis>
     StateCalcDuration<astrogator/StateCalcDuration>
     StateCalcUserValue<astrogator/StateCalcUserValue>
     StateCalcVectorGeometryToolAngle<astrogator/StateCalcVectorGeometryToolAngle>
     StateCalcAngle<astrogator/StateCalcAngle>
     StateCalcDotProduct<astrogator/StateCalcDotProduct>
     StateCalcVectorDec<astrogator/StateCalcVectorDec>
     StateCalcVectorMagnitude<astrogator/StateCalcVectorMagnitude>
     StateCalcVectorRA<astrogator/StateCalcVectorRA>
     StateCalcVectorX<astrogator/StateCalcVectorX>
     StateCalcOnePointAccess<astrogator/StateCalcOnePointAccess>
     StateCalcDifferenceAcrossSegmentsOtherSat<astrogator/StateCalcDifferenceAcrossSegmentsOtherSat>
     StateCalcValueAtSegmentOtherSat<astrogator/StateCalcValueAtSegmentOtherSat>
     StateCalcRARate<astrogator/StateCalcRARate>
     StateCalcDecRate<astrogator/StateCalcDecRate>
     StateCalcRangeRate<astrogator/StateCalcRangeRate>
     StateCalcGravitationalParameter<astrogator/StateCalcGravitationalParameter>
     StateCalcReferenceRadius<astrogator/StateCalcReferenceRadius>
     StateCalcGravCoeff<astrogator/StateCalcGravCoeff>
     StateCalcSpeedOfLight<astrogator/StateCalcSpeedOfLight>
     StateCalcPi<astrogator/StateCalcPi>
     StateCalcScalar<astrogator/StateCalcScalar>
     StateCalcApparentSolarTime<astrogator/StateCalcApparentSolarTime>
     StateCalcEarthMeanSolarTime<astrogator/StateCalcEarthMeanSolarTime>
     StateCalcEarthMeanLocTimeAN<astrogator/StateCalcEarthMeanLocTimeAN>
     AutomaticSequenceCollection<astrogator/AutomaticSequenceCollection>
     AutomaticSequence<astrogator/AutomaticSequence>
     CentralBodyCollection<astrogator/CentralBodyCollection>
     AstrogatorCentralBody<astrogator/AstrogatorCentralBody>
     CentralBodyGravityModel<astrogator/CentralBodyGravityModel>
     CentralBodyShapeSphere<astrogator/CentralBodyShapeSphere>
     CentralBodyShapeOblateSpheroid<astrogator/CentralBodyShapeOblateSpheroid>
     CentralBodyShapeTriaxialEllipsoid<astrogator/CentralBodyShapeTriaxialEllipsoid>
     CentralBodyAttitudeRotationCoefficientsFile<astrogator/CentralBodyAttitudeRotationCoefficientsFile>
     CentralBodyAttitudeIAU1994<astrogator/CentralBodyAttitudeIAU1994>
     CentralBodyEphemerisAnalyticOrbit<astrogator/CentralBodyEphemerisAnalyticOrbit>
     CentralBodyEphemerisJPLSpice<astrogator/CentralBodyEphemerisJPLSpice>
     CentralBodyEphemerisFile<astrogator/CentralBodyEphemerisFile>
     CentralBodyEphemerisJPLDesignExplorerOptimizer<astrogator/CentralBodyEphemerisJPLDesignExplorerOptimizer>
     CentralBodyEphemerisPlanetary<astrogator/CentralBodyEphemerisPlanetary>
     MissionControlSequenceSegmentProperties<astrogator/MissionControlSequenceSegmentProperties>
     PowerInternal<astrogator/PowerInternal>
     PowerProcessed<astrogator/PowerProcessed>
     PowerSolarArray<astrogator/PowerSolarArray>
     GeneralRelativityFunction<astrogator/GeneralRelativityFunction>
     StateTransformationFunction<astrogator/StateTransformationFunction>
     CR3BPFunc<astrogator/CR3BPFunc>
     ER3BPFunc<astrogator/ER3BPFunc>
     RadiationPressureFunction<astrogator/RadiationPressureFunction>
     YarkovskyFunc<astrogator/YarkovskyFunc>
     BlendedDensity<astrogator/BlendedDensity>
     Cira72Function<astrogator/Cira72Function>
     Exponential<astrogator/Exponential>
     HarrisPriester<astrogator/HarrisPriester>
     DensityModelPlugin<astrogator/DensityModelPlugin>
     JacchiaRoberts<astrogator/JacchiaRoberts>
     JacchiaBowman2008<astrogator/JacchiaBowman2008>
     Jacchia_1960<astrogator/Jacchia_1960>
     Jacchia_1970<astrogator/Jacchia_1970>
     Jacchia_1971<astrogator/Jacchia_1971>
     MSISE_1990<astrogator/MSISE_1990>
     MSIS_1986<astrogator/MSIS_1986>
     NRLMSISE_2000<astrogator/NRLMSISE_2000>
     US_Standard_Atmosphere<astrogator/US_Standard_Atmosphere>
     MarsGRAM37<astrogator/MarsGRAM37>
     MarsGRAM2000<astrogator/MarsGRAM2000>
     MarsGRAM2001<astrogator/MarsGRAM2001>
     MarsGRAM2005<astrogator/MarsGRAM2005>
     MarsGRAM2010<astrogator/MarsGRAM2010>
     VenusGRAM2005<astrogator/VenusGRAM2005>
     DTM2012<astrogator/DTM2012>
     DTM2020<astrogator/DTM2020>
     GravityFieldFunction<astrogator/GravityFieldFunction>
     PointMassFunction<astrogator/PointMassFunction>
     TwoBodyFunction<astrogator/TwoBodyFunction>
     HPOPPluginFunction<astrogator/HPOPPluginFunction>
     EOMFuncPluginFunction<astrogator/EOMFuncPluginFunction>
     SRPAeroT20<astrogator/SRPAeroT20>
     SRPAeroT30<astrogator/SRPAeroT30>
     SRPGSPM04aIIA<astrogator/SRPGSPM04aIIA>
     SRPGSPM04aIIR<astrogator/SRPGSPM04aIIR>
     SRPGSPM04aeIIA<astrogator/SRPGSPM04aeIIA>
     SRPGSPM04aeIIR<astrogator/SRPGSPM04aeIIR>
     SRPSpherical<astrogator/SRPSpherical>
     SRPNPlate<astrogator/SRPNPlate>
     SRPTabAreaVec<astrogator/SRPTabAreaVec>
     SRPVariableArea<astrogator/SRPVariableArea>
     ThirdBodyFunction<astrogator/ThirdBodyFunction>
     DragModelPlugin<astrogator/DragModelPlugin>
     SRPReflectionPlugin<astrogator/SRPReflectionPlugin>
     EngineConstAcc<astrogator/EngineConstAcc>
     EngineConstant<astrogator/EngineConstant>
     EngineIon<astrogator/EngineIon>
     EngineThrottleTable<astrogator/EngineThrottleTable>
     EngineCustom<astrogator/EngineCustom>
     EnginePlugin<astrogator/EnginePlugin>
     EngineModelPoly<astrogator/EngineModelPoly>
     EngineModelThrustCoefficients<astrogator/EngineModelThrustCoefficients>
     EngineModelIspCoefficients<astrogator/EngineModelIspCoefficients>
     EngineDefinition<astrogator/EngineDefinition>
     DesignCR3BPSetup<astrogator/DesignCR3BPSetup>
     DesignCR3BPObject<astrogator/DesignCR3BPObject>
     DesignCR3BPObjectCollection<astrogator/DesignCR3BPObjectCollection>
     DesignER3BPSetup<astrogator/DesignER3BPSetup>
     DesignER3BPObject<astrogator/DesignER3BPObject>
     DesignER3BPObjectCollection<astrogator/DesignER3BPObjectCollection>
     Thruster<astrogator/Thruster>
     ThrusterSetCollection<astrogator/ThrusterSetCollection>
     ThrusterSet<astrogator/ThrusterSet>
     AsTriggerCondition<astrogator/AsTriggerCondition>
     CustomFunctionScriptEngine<astrogator/CustomFunctionScriptEngine>
     NumericalPropagatorWrapper<astrogator/NumericalPropagatorWrapper>
     NumericalPropagatorWrapperCR3BP<astrogator/NumericalPropagatorWrapperCR3BP>
     PropagatorFunctionCollection<astrogator/PropagatorFunctionCollection>
     BulirschStoerIntegrator<astrogator/BulirschStoerIntegrator>
     GaussJacksonIntegrator<astrogator/GaussJacksonIntegrator>
     RungeKutta2nd3rd<astrogator/RungeKutta2nd3rd>
     RungeKutta4th<astrogator/RungeKutta4th>
     RungeKutta4th5th<astrogator/RungeKutta4th5th>
     RungeKutta4thAdapt<astrogator/RungeKutta4thAdapt>
     RungeKuttaF7th8th<astrogator/RungeKuttaF7th8th>
     RungeKuttaV8th9th<astrogator/RungeKuttaV8th9th>
     ScriptingTool<astrogator/ScriptingTool>
     ScriptingSegmentCollection<astrogator/ScriptingSegmentCollection>
     ScriptingSegment<astrogator/ScriptingSegment>
     ScriptingParameterCollection<astrogator/ScriptingParameterCollection>
     ScriptingParameter<astrogator/ScriptingParameter>
     ScriptingCalcObject<astrogator/ScriptingCalcObject>
     ScriptingCalcObjectCollection<astrogator/ScriptingCalcObjectCollection>
     UserVariableDefinition<astrogator/UserVariableDefinition>
     UserVariable<astrogator/UserVariable>
     UserVariableUpdate<astrogator/UserVariableUpdate>
     UserVariableDefinitionCollection<astrogator/UserVariableDefinitionCollection>
     UserVariableCollection<astrogator/UserVariableCollection>
     UserVariableUpdateCollection<astrogator/UserVariableUpdateCollection>
     CalculationGraphCollection<astrogator/CalculationGraphCollection>
     ScriptingParameterEnumerationChoice<astrogator/ScriptingParameterEnumerationChoice>
     ScriptingParameterEnumerationChoiceCollection<astrogator/ScriptingParameterEnumerationChoiceCollection>
     ProfileSNOPTOptimizer<astrogator/ProfileSNOPTOptimizer>
     SNOPTControl<astrogator/SNOPTControl>
     SNOPTResult<astrogator/SNOPTResult>
     SNOPTControlCollection<astrogator/SNOPTControlCollection>
     SNOPTResultCollection<astrogator/SNOPTResultCollection>
     ProfileIPOPTOptimizer<astrogator/ProfileIPOPTOptimizer>
     IPOPTControl<astrogator/IPOPTControl>
     IPOPTResult<astrogator/IPOPTResult>
     IPOPTControlCollection<astrogator/IPOPTControlCollection>
     IPOPTResultCollection<astrogator/IPOPTResultCollection>
     ManeuverOptimalFinite<astrogator/ManeuverOptimalFinite>
     ManeuverOptimalFiniteSNOPTOptimizer<astrogator/ManeuverOptimalFiniteSNOPTOptimizer>
     ManeuverOptimalFiniteInitialBoundaryConditions<astrogator/ManeuverOptimalFiniteInitialBoundaryConditions>
     ManeuverOptimalFiniteFinalBoundaryConditions<astrogator/ManeuverOptimalFiniteFinalBoundaryConditions>
     ManeuverOptimalFinitePathBoundaryConditions<astrogator/ManeuverOptimalFinitePathBoundaryConditions>
     ManeuverOptimalFiniteSteeringNodeElement<astrogator/ManeuverOptimalFiniteSteeringNodeElement>
     ManeuverOptimalFiniteSteeringNodeCollection<astrogator/ManeuverOptimalFiniteSteeringNodeCollection>
     ManeuverOptimalFiniteBounds<astrogator/ManeuverOptimalFiniteBounds>
     ProfileLambertProfile<astrogator/ProfileLambertProfile>
     ProfileLambertSearchProfile<astrogator/ProfileLambertSearchProfile>
     ProfileGoldenSection<astrogator/ProfileGoldenSection>
     GoldenSectionControlCollection<astrogator/GoldenSectionControlCollection>
     GoldenSectionControl<astrogator/GoldenSectionControl>
     GoldenSectionResultCollection<astrogator/GoldenSectionResultCollection>
     GoldenSectionResult<astrogator/GoldenSectionResult>
     ProfileGridSearch<astrogator/ProfileGridSearch>
     GridSearchControlCollection<astrogator/GridSearchControlCollection>
     GridSearchControl<astrogator/GridSearchControl>
     GridSearchResultCollection<astrogator/GridSearchResultCollection>
     GridSearchResult<astrogator/GridSearchResult>
     CalcObjectLinkEmbedControlCollection<astrogator/CalcObjectLinkEmbedControlCollection>
     ProfileBisection<astrogator/ProfileBisection>
     BisectionControl<astrogator/BisectionControl>
     BisectionControlCollection<astrogator/BisectionControlCollection>
     BisectionResult<astrogator/BisectionResult>
     BisectionResultCollection<astrogator/BisectionResultCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ GRAPH_OPTION<astrogator/GRAPH_OPTION_enum>
    ≔ SMART_RUN_MODE<astrogator/SMART_RUN_MODE_enum>
    ≔ FORMULATION<astrogator/FORMULATION_enum>
    ≔ LIGHTING_CONDITION<astrogator/LIGHTING_CONDITION_enum>
    ≔ PROFILE<astrogator/PROFILE_enum>
    ≔ ACCESS_CRITERION<astrogator/ACCESS_CRITERION_enum>
    ≔ ECLIPSING_BODIES_SOURCE<astrogator/ECLIPSING_BODIES_SOURCE_enum>
    ≔ CRITERION<astrogator/CRITERION_enum>
    ≔ CALC_OBJECT_REFERENCE<astrogator/CALC_OBJECT_REFERENCE_enum>
    ≔ CALC_OBJECT_CENTRAL_BODY_REFERENCE<astrogator/CALC_OBJECT_CENTRAL_BODY_REFERENCE_enum>
    ≔ CALC_OBJECT_ELEM<astrogator/CALC_OBJECT_ELEM_enum>
    ≔ PROFILE_MODE<astrogator/PROFILE_MODE_enum>
    ≔ CONTROL_STOPPING_CONDITION<astrogator/CONTROL_STOPPING_CONDITION_enum>
    ≔ STATE<astrogator/STATE_enum>
    ≔ RETURN_CONTROL<astrogator/RETURN_CONTROL_enum>
    ≔ DRAW_PERTURBATION<astrogator/DRAW_PERTURBATION_enum>
    ≔ DERIVE_CALC_METHOD<astrogator/DERIVE_CALC_METHOD_enum>
    ≔ CONVERGENCE_CRITERIA<astrogator/CONVERGENCE_CRITERIA_enum>
    ≔ DIFFERENTIAL_CORRECTOR_SCALING_METHOD<astrogator/DIFFERENTIAL_CORRECTOR_SCALING_METHOD_enum>
    ≔ CONTROL_UPDATE<astrogator/CONTROL_UPDATE_enum>
    ≔ CONTROL_FOLLOW<astrogator/CONTROL_FOLLOW_enum>
    ≔ CONTROL_INIT_STATE<astrogator/CONTROL_INIT_STATE_enum>
    ≔ CONTROL_MANEUVER<astrogator/CONTROL_MANEUVER_enum>
    ≔ CONTROL_LAUNCH<astrogator/CONTROL_LAUNCH_enum>
    ≔ CONTROL_ADVANCED<astrogator/CONTROL_ADVANCED_enum>
    ≔ TARGET_SEQ_ACTION<astrogator/TARGET_SEQ_ACTION_enum>
    ≔ PROFILES_FINISH<astrogator/PROFILES_FINISH_enum>
    ≔ UPDATE_PARAM<astrogator/UPDATE_PARAM_enum>
    ≔ UPDATE_ACTION<astrogator/UPDATE_ACTION_enum>
    ≔ PRESSURE_MODE<astrogator/PRESSURE_MODE_enum>
    ≔ THRUST_TYPE<astrogator/THRUST_TYPE_enum>
    ≔ ATTITUDE_UPDATE<astrogator/ATTITUDE_UPDATE_enum>
    ≔ PROPULSION_METHOD<astrogator/PROPULSION_METHOD_enum>
    ≔ CUSTOM_FUNCTION<astrogator/CUSTOM_FUNCTION_enum>
    ≔ BODY_AXIS<astrogator/BODY_AXIS_enum>
    ≔ CONSTRAINT_SIGN<astrogator/CONSTRAINT_SIGN_enum>
    ≔ ATTITUDE_CONTROL<astrogator/ATTITUDE_CONTROL_enum>
    ≔ FOLLOW_JOIN<astrogator/FOLLOW_JOIN_enum>
    ≔ FOLLOW_SEPARATION<astrogator/FOLLOW_SEPARATION_enum>
    ≔ FOLLOW_SPACECRAFT_AND_FUEL_TANK<astrogator/FOLLOW_SPACECRAFT_AND_FUEL_TANK_enum>
    ≔ BURNOUT_OPTIONS<astrogator/BURNOUT_OPTIONS_enum>
    ≔ BURNOUT_TYPE<astrogator/BURNOUT_TYPE_enum>
    ≔ ASCENT_TYPE<astrogator/ASCENT_TYPE_enum>
    ≔ LAUNCH_DISPLAY_SYSTEM<astrogator/LAUNCH_DISPLAY_SYSTEM_enum>
    ≔ RUN_CODE<astrogator/RUN_CODE_enum>
    ≔ SEQUENCE_STATE_TO_PASS<astrogator/SEQUENCE_STATE_TO_PASS_enum>
    ≔ MANEUVER_TYPE<astrogator/MANEUVER_TYPE_enum>
    ≔ SEGMENT_TYPE<astrogator/SEGMENT_TYPE_enum>
    ≔ ELEMENT_TYPE<astrogator/ELEMENT_TYPE_enum>
    ≔ LANGUAGE<astrogator/LANGUAGE_enum>
    ≔ STOPPING_CONDITION<astrogator/STOPPING_CONDITION_enum>
    ≔ CLEAR_EPHEMERIS_DIRECTION<astrogator/CLEAR_EPHEMERIS_DIRECTION_enum>
    ≔ PROFILE_INSERT_DIRECTION<astrogator/PROFILE_INSERT_DIRECTION_enum>
    ≔ ROOT_FINDING_ALGORITHM<astrogator/ROOT_FINDING_ALGORITHM_enum>
    ≔ SCRIPTING_PARAMETER_TYPE<astrogator/SCRIPTING_PARAMETER_TYPE_enum>
    ≔ SNOPT_GOAL<astrogator/SNOPT_GOAL_enum>
    ≔ IPOPT_GOAL<astrogator/IPOPT_GOAL_enum>
    ≔ OPTIMAL_FINITE_SEED_METHOD<astrogator/OPTIMAL_FINITE_SEED_METHOD_enum>
    ≔ OPTIMAL_FINITE_RUN_MODE<astrogator/OPTIMAL_FINITE_RUN_MODE_enum>
    ≔ OPTIMAL_FINITE_DISCRETIZATION_STRATEGY<astrogator/OPTIMAL_FINITE_DISCRETIZATION_STRATEGY_enum>
    ≔ OPTIMAL_FINITE_WORKING_VARIABLES<astrogator/OPTIMAL_FINITE_WORKING_VARIABLES_enum>
    ≔ OPTIMAL_FINITE_SCALING_OPTIONS<astrogator/OPTIMAL_FINITE_SCALING_OPTIONS_enum>
    ≔ OPTIMAL_FINITE_SNOPT_OBJECTIVE<astrogator/OPTIMAL_FINITE_SNOPT_OBJECTIVE_enum>
    ≔ OPTIMAL_FINITE_SNOPT_SCALING<astrogator/OPTIMAL_FINITE_SNOPT_SCALING_enum>
    ≔ OPTIMAL_FINITE_EXPORT_NODES_FORMAT<astrogator/OPTIMAL_FINITE_EXPORT_NODES_FORMAT_enum>
    ≔ OPTIMAL_FINITE_GUESS_METHOD<astrogator/OPTIMAL_FINITE_GUESS_METHOD_enum>
    ≔ IMP_DELTA_V_REP<astrogator/IMP_DELTA_V_REP_enum>
    ≔ LAMBERT_TARGET_COORD_TYPE<astrogator/LAMBERT_TARGET_COORD_TYPE_enum>
    ≔ LAMBERT_SOLUTION_OPTION_TYPE<astrogator/LAMBERT_SOLUTION_OPTION_TYPE_enum>
    ≔ LAMBERT_ORBITAL_ENERGY_TYPE<astrogator/LAMBERT_ORBITAL_ENERGY_TYPE_enum>
    ≔ LAMBERT_DIRECTION_OF_MOTION_TYPE<astrogator/LAMBERT_DIRECTION_OF_MOTION_TYPE_enum>
    ≔ GOLDEN_SECTION_DESIRED_OPERATION<astrogator/GOLDEN_SECTION_DESIRED_OPERATION_enum>
    ≔ GRID_SEARCH_DESIRED_OPERATION<astrogator/GRID_SEARCH_DESIRED_OPERATION_enum>
    ≔ ELEMENT<astrogator/ELEMENT_enum>
    ≔ BASE_SELECTION<astrogator/BASE_SELECTION_enum>
    ≔ CONTROL_ORBIT_STATE_VALUE<astrogator/CONTROL_ORBIT_STATE_VALUE_enum>
    ≔ SEGMENT_STATE<astrogator/SEGMENT_STATE_enum>
    ≔ DIFFERENCE_ORDER<astrogator/DIFFERENCE_ORDER_enum>
    ≔ SEGMENT_DIFFERENCE_ORDER<astrogator/SEGMENT_DIFFERENCE_ORDER_enum>
    ≔ CONTROL_REPEATING_GROUND_TRACK_ERR<astrogator/CONTROL_REPEATING_GROUND_TRACK_ERR_enum>
    ≔ CALC_OBJECT_DIRECTION<astrogator/CALC_OBJECT_DIRECTION_enum>
    ≔ CALC_OBJECT_ORBIT_PLANE_SOURCE<astrogator/CALC_OBJECT_ORBIT_PLANE_SOURCE_enum>
    ≔ CALC_OBJECT_SUN_POSITION<astrogator/CALC_OBJECT_SUN_POSITION_enum>
    ≔ CALC_OBJECT_ANGLE_SIGN<astrogator/CALC_OBJECT_ANGLE_SIGN_enum>
    ≔ CALC_OBJECT_REFERENCE_DIRECTION<astrogator/CALC_OBJECT_REFERENCE_DIRECTION_enum>
    ≔ CALC_OBJECT_RELATIVE_POSITION<astrogator/CALC_OBJECT_RELATIVE_POSITION_enum>
    ≔ CALC_OBJECT_REFERENCE_ELLIPSE<astrogator/CALC_OBJECT_REFERENCE_ELLIPSE_enum>
    ≔ CALC_OBJECT_LOCATION_SOURCE<astrogator/CALC_OBJECT_LOCATION_SOURCE_enum>
    ≔ GRAVITATIONAL_PARAMETER_SOURCE<astrogator/GRAVITATIONAL_PARAMETER_SOURCE_enum>
    ≔ REFERENCE_RADIUS_SOURCE<astrogator/REFERENCE_RADIUS_SOURCE_enum>
    ≔ GRAV_COEFF_NORMALIZATION_TYPE<astrogator/GRAV_COEFF_NORMALIZATION_TYPE_enum>
    ≔ GRAV_COEFF_COEFFICIENT_TYPE<astrogator/GRAV_COEFF_COEFFICIENT_TYPE_enum>
    ≔ STM_PERT_VARIABLES<astrogator/STM_PERT_VARIABLES_enum>
    ≔ STM_EIGEN_NUMBER<astrogator/STM_EIGEN_NUMBER_enum>
    ≔ COMPLEX_NUMBER<astrogator/COMPLEX_NUMBER_enum>
    ≔ SQUARED_TYPE<astrogator/SQUARED_TYPE_enum>
    ≔ GEO_STATIONARY_DRIFT_RATE_MODEL<astrogator/GEO_STATIONARY_DRIFT_RATE_MODEL_enum>
    ≔ GEO_STATIONARY_INCLINATION_MAGNITUDE<astrogator/GEO_STATIONARY_INCLINATION_MAGNITUDE_enum>
    ≔ CENTRAL_BODY_GRAVITY_MODEL<astrogator/CENTRAL_BODY_GRAVITY_MODEL_enum>
    ≔ CENTRAL_BODY_SHAPE<astrogator/CENTRAL_BODY_SHAPE_enum>
    ≔ CENTRAL_BODY_ATTITUDE<astrogator/CENTRAL_BODY_ATTITUDE_enum>
    ≔ CENTRAL_BODY_EPHEMERIS<astrogator/CENTRAL_BODY_EPHEMERIS_enum>
    ≔ CONTROL_POWER_INTERNAL<astrogator/CONTROL_POWER_INTERNAL_enum>
    ≔ CONTROL_POWER_PROCESSED<astrogator/CONTROL_POWER_PROCESSED_enum>
    ≔ CONTROL_POWER_SOLAR_ARRAY<astrogator/CONTROL_POWER_SOLAR_ARRAY_enum>
    ≔ THIRD_BODY_MODE<astrogator/THIRD_BODY_MODE_enum>
    ≔ GRAV_PARAM_SOURCE<astrogator/GRAV_PARAM_SOURCE_enum>
    ≔ EPHEM_SOURCE<astrogator/EPHEM_SOURCE_enum>
    ≔ SOLAR_FORCE_METHOD<astrogator/SOLAR_FORCE_METHOD_enum>
    ≔ SHADOW_MODEL<astrogator/SHADOW_MODEL_enum>
    ≔ SUN_POSITION<astrogator/SUN_POSITION_enum>
    ≔ ATMOS_DATA_SOURCE<astrogator/ATMOS_DATA_SOURCE_enum>
    ≔ GEO_MAGNETIC_FLUX_SOURCE<astrogator/GEO_MAGNETIC_FLUX_SOURCE_enum>
    ≔ GEO_MAGNETIC_FLUX_UPDATE_RATE<astrogator/GEO_MAGNETIC_FLUX_UPDATE_RATE_enum>
    ≔ DRAG_MODEL_TYPE<astrogator/DRAG_MODEL_TYPE_enum>
    ≔ MARS_GRAM_DENSITY_TYPE<astrogator/MARS_GRAM_DENSITY_TYPE_enum>
    ≔ VENUS_GRAM_DENSITY_TYPE<astrogator/VENUS_GRAM_DENSITY_TYPE_enum>
    ≔ TAB_VEC_INTERP_METHOD<astrogator/TAB_VEC_INTERP_METHOD_enum>
    ≔ CONTROL_ENGINE_CONST_ACC<astrogator/CONTROL_ENGINE_CONST_ACC_enum>
    ≔ CONTROL_ENGINE_CONSTANT<astrogator/CONTROL_ENGINE_CONSTANT_enum>
    ≔ CONTROL_ENGINE_CUSTOM<astrogator/CONTROL_ENGINE_CUSTOM_enum>
    ≔ CONTROL_ENGINE_THROTTLE_TABLE<astrogator/CONTROL_ENGINE_THROTTLE_TABLE_enum>
    ≔ CONTROL_ENGINE_ION<astrogator/CONTROL_ENGINE_ION_enum>
    ≔ CONTROL_ENGINE_MODEL_POLY<astrogator/CONTROL_ENGINE_MODEL_POLY_enum>
    ≔ ENGINE_MODEL_FUNCTION<astrogator/ENGINE_MODEL_FUNCTION_enum>
    ≔ THROTTLE_TABLE_OPERATION_MODE<astrogator/THROTTLE_TABLE_OPERATION_MODE_enum>
    ≔ IDEAL_ORBIT_RADIUS<astrogator/IDEAL_ORBIT_RADIUS_enum>
    ≔ ROTATING_COORDINATE_SYSTEM<astrogator/ROTATING_COORDINATE_SYSTEM_enum>
    ≔ CONTROL_THRUSTERS<astrogator/CONTROL_THRUSTERS_enum>
    ≔ THRUSTER_DIRECTION<astrogator/THRUSTER_DIRECTION_enum>
    ≔ CRITERIA<astrogator/CRITERIA_enum>
    ≔ ERROR_CONTROL<astrogator/ERROR_CONTROL_enum>
    ≔ PREDICTOR_CORRECTOR<astrogator/PREDICTOR_CORRECTOR_enum>
    ≔ NUMERICAL_INTEGRATOR<astrogator/NUMERICAL_INTEGRATOR_enum>
    ≔ COEFF_RUNGE_KUTTA_V_8TH_9TH<astrogator/COEFF_RUNGE_KUTTA_V_8TH_9TH_enum>

