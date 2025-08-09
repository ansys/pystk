
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


            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`
              - Properties for attitude options for a maneuver segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinite`
              - The attitude control of a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsive`
              - The attitude control of an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlOptimalFinite`
              - The attitude control of a optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IBurnout`
              - The burnout point reference frame.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyComponentAttitude`
              - The central body attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyComponentEphemeris`
              - The central body ephemeris source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyComponentEphemerisJPLDevelopmentalEphemerides`
              - Properties for the JPL DE ephemeris source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ICentralBodyComponentShape`
              - The central body shape.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IDisplaySystem`
              - The launch coordinate system.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IElement`
              - The elements of the selected coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuver`
              - Properties of an Impulsive Maneuver Segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment`
              - General properties for segments.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSequence`
              - Properties for a Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.INumericalIntegrator`
              - The type of numerical integrator to be used by the propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`
              - General properties for target sequence profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IStoppingConditionComponent`
              - Properties for a stopping condition.


    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AccessStoppingCondition`
              - The Access stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AsTriggerCondition`
              - Constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAntiVelocityVector`
              - The anti-velocity vector attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude`
              - The attitude attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile`
              - The file attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin`
              - The plugin attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector`
              - The thrust vector attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying`
              - The time varying attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector`
              - The velocity vector attitude control for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAntiVelocityVector`
              - The anti-velocity vector attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude`
              - The attitude attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile`
              - The file attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector`
              - The thrust vector attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveVelocityVector`
              - The velocity vector attitude control for an impulsive maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlOptimalFiniteLagrange`
              - The Lagrange Interpolation attitude control for a optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AutomaticSequence`
              - Automatic Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AutomaticSequenceCollection`
              - Automatic Sequence Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BDotRCalc`
              - BDotR Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BDotTCalc`
              - BDotT Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BisectionControl`
              - Control parameters for  Bisection Search Profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BisectionControlCollection`
              - Bisection control collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BisectionResult`
              - Result parameters for Bisection profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BisectionResultCollection`
              - Bisection result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity`
              - Blended atmospheric density propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BMagnitudeCalc`
              - BMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BPlaneCollection`
              - The collection of B-Planes.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BThetaCalc`
              - BTheta Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BulirschStoerIntegrator`
              - Bulirsch-Stoer Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutCBFCartesian`
              - The burnout state in CBF Cartesian coordinates.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutGeocentric`
              - The geocentric burnout point.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutGeodetic`
              - The geodetic burnout point.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzAltitude`
              - The launch azimuth and altitude burnout point.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutLaunchAzRadius`
              - The launch azimuth and radius burnout point.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutVelocity`
              - The burnout velocity.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection`
              - Calculation Graph Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCollection`
              - The Calculation Object component folder.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLinkEmbedControlCollection`
              - The Calculation Object link/embed component folder.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent`
              - Central Body.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentAttitudeIAU1994`
              - Central Body Attitude - IAU1994.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentAttitudeRotationCoefficientsFile`
              - Central Body Attitude - Rotation Coefficients File.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentCollection`
              - Central Body Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentEphemerisAnalyticOrbit`
              - Central Body Ephemeris - Analytic Orbit.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentEphemerisFile`
              - Central Body Ephemeris - File.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentEphemerisJPLDesignExplorerOptimizer`
              - Central Body Ephemeris - JPL DE.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentEphemerisJPLSpice`
              - Central Body Ephemeris - JPLSpice.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentEphemerisPlanetary`
              - Central Body Ephemeris - Planetary.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel`
              - Central Body Gravity Model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentShapeOblateSpheroid`
              - Central Body Shape - Spheroid.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentShapeSphere`
              - Central Body Shape - Sphere.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentShapeTriaxialEllipsoid`
              - Central Body Shape - Triaxial Ellipsoid.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Cira72Function`
              - Cira72 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ConstraintCollection`
              - The Constraint component folder.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CR3BPFunction`
              - CR3BP Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CustomFunctionScriptEngine`
              - Custom Function Script Engine.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DensityModelPlugin`
              - Plugin atmospheric density propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObject`
              - CR3BP associated object definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPObjectCollection`
              - CR3BP associated object Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignCR3BPSetup`
              - CR3BP Setup Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObject`
              - ER3BP associated object definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPObjectCollection`
              - ER3BP associated object Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DesignER3BPSetup`
              - ER3BP Setup Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControl`
              - Control Parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorControlCollection`
              - The collection of Control Parameters for a differential corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResult`
              - Differential Corrector equality constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorResultCollection`
              - The collection of results for a differential corrector.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DisplaySystemGeocentric`
              - The geocentric launch location.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DisplaySystemGeodetic`
              - The geodetic launch location.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DragModelPlugin`
              - Drag Model Plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DTM2012`
              - DTM 2012 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DTM2020`
              - DTM 2020 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane`
              - Bplane elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementCartesian`
              - Cartesian elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay`
              - Delaunay elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementEquinoctial`
              - Equinoctial elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic`
              - Geodetic elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementKeplerian`
              - Keplerian elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementMixedSpherical`
              - Mixed Spherical elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical`
              - Spherical elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementSphericalRangeRate`
              - Spherical Range Rate elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementTargetVectorIncomingAsymptote`
              - Target Vector Incoming Asymptote elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementTargetVectorOutgoingAsymptote`
              - Target Vector Outgoing Asymptote elements.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineConstant`
              - Constant Thrust engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineConstantAcceleration`
              - Constant Acceleration engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineCustom`
              - Custom engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineDefinition`
              - Engine definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineIon`
              - Ion Engine engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineModelIspCoefficients`
              - Engine Model Isp Coefficients.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineModelPolynomial`
              - Polynomial Thrust and Isp engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineModelThrustCoefficients`
              - Engine Model Thrust Coefficients.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EnginePlugin`
              - Plugin engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineThrottleTable`
              - Throttle Table engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EOMFuncPluginFunction`
              - EOM Function Plugin propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ER3BPFunc`
              - ER3BP Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Exponential`
              - Exponential atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FuelTank`
              - Fuel Tank parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GaussJacksonIntegrator`
              - Gauss-Jackson Numerical Integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GeneralRelativityFunction`
              - General Relativity Propagator Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl`
              - Control parameters for Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControlCollection`
              - Properties for the list of Golden Section control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult`
              - Result parameters for Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection`
              - Properties for the list of Golden Section result parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GravityFieldFunction`
              - Gravity Field gravity propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl`
              - Control parameters for Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchControlCollection`
              - Properties for the list of Grid Search control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchResult`
              - Result parameters for Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchResultCollection`
              - Properties for the list of Grid Search result parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.HarrisPriester`
              - Harris-Priester atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.HPOPPluginFunction`
              - HPOP Plugin propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl`
              - Control parameters for IPOPT optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTControlCollection`
              - Properties for the list of IPOPT control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTResult`
              - Properties for objecvtive and constraints of a IPOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection`
              - IPOPT result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Jacchia1960`
              - Jacchia_1960 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Jacchia1970`
              - Jacchia_1970 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Jacchia1971`
              - Jacchia_1971 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.JacchiaBowman2008`
              - Jacchia Bowman 2008 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.JacchiaRoberts`
              - Jacchia Roberts atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LightingStoppingCondition`
              - The Lighting stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinite`
              - The Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverFinitePropagator`
              - Propagation for a finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverImpulsive`
              - The Impulsive Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite`
              - The Optimal Finite Maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteBounds`
              - The elements of the steering node.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteFinalBoundaryConditions`
              - Properties of final boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteInitialBoundaryConditions`
              - Properties of initial boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinitePathBoundaryConditions`
              - Properties of path boundary conditions for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSNOPTOptimizer`
              - Properties of SNOPT Optimizer options for optimal finite maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSteeringNodeCollection`
              - Steering/nodes collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFiniteSteeringNodeElement`
              - The elements of the steering node.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2000`
              - Mars-GRAM 2000 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2001`
              - Mars-GRAM 2001 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2005`
              - Mars-GRAM 2005 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM2010`
              - Mars-GRAM 2010 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAM37`
              - Mars-GRAM 3.7 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSBackwardSequence`
              - The Backward Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSDriver`
              - Basic properties of an Astrogator satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSEnd`
              - The End segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSFollow`
              - The Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSHold`
              - The Hold segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSInitialState`
              - The Initial State segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch`
              - The Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSManeuver`
              - The Maneuver segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSOptions`
              - The MCS Options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSPropagate`
              - The Propagate segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSReturn`
              - The Return segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection`
              - The Mission Control Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentProperties`
              - Segment Properties.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSSequence`
              - The Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSStop`
              - The Stop segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence`
              - The Target Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MCSUpdate`
              - The Update segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MSIS1986`
              - MSIS 1986 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MSISE1990`
              - MSISE 1990 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.NRLMSISE2000`
              - NRLMSISE 2000 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapper`
              - Numerical Propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.NumericalPropagatorWrapperCR3BP`
              - Numerical CR3BP Propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PluginProperties`
              - The plugin attitude control type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PointMassFunction`
              - Point Mass function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PowerInternal`
              - Power - Internal.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PowerProcessed`
              - Power - Processed Power Unit.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray`
              - Power - Solar Array.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileBisection`
              - Single Parameter Bisection profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeManeuverType`
              - The Change Maneuver Type profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangePropagator`
              - The Change Propagator profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeReturnSegment`
              - The Change Return Segment profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStoppingConditionState`
              - The Change Stopping Condition State profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileChangeStopSegment`
              - The Change Stop Segment profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection`
              - The Profiles of a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector`
              - The Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileGoldenSection`
              - The Golden Section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch`
              - The Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileIPOPTOptimizer`
              - IPOPT optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile`
              - The Lambert profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile`
              - The Lambert profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileRunOnce`
              - The Run Once profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileScriptingTool`
              - The Scripting Tool profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileSearchPlugin`
              - The plugin search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileSeedFiniteManeuver`
              - The Seed Finite Maneuver profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer`
              - SNOPT optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection`
              - Propagator Function Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RadiationPressureFunction`
              - Radiation Pressure Propagator Function.

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

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObject`
              - Calc Object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection`
              - Calc Object Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter`
              - Scripting Parameter.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection`
              - Scripting Parameter Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoice`
              - Scripting Parameter Enumeration Choice.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection`
              - Scripting Parameter Enumeration Choice Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegment`
              - Scripting Segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection`
              - Scripting Segment Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingTool`
              - Scripting Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControl`
              - Control parameters for a plugin search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection`
              - The list of search plugin control parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult`
              - Equality constraints for a plugin search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection`
              - The list of search plugin equality constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl`
              - Control parameters for SNOPT optimizer profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTControlCollection`
              - SNOPT control collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTResult`
              - Properties for objecvtive and constraints of a SNOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection`
              - SNOPT result collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters`
              - Spacecraft parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPAerospaceT20`
              - AeroT20 SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPAerospaceT30`
              - AeroT30 SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPGSPM04aeIIA`
              - GSPM04aeIIA SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPGSPM04aeIIR`
              - GSPM04aeIIR SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPGSPM04aIIA`
              - GSPM04aIIA SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPGSPM04aIIR`
              - GSPM04aIIR SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate`
              - NPlate SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin`
              - SRP Reflection Plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical`
              - Spherical SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPTabulatedAreaVector`
              - Tabulated area vector SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SRPVariableArea`
              - Variable Area SRP propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.State`
              - The orbit state.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcAbsoluteValue`
              - AbsoluteValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcAltitudeOfApoapsis`
              - AltitudeOfApoapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcAltitudeOfPeriapsis`
              - AltitudeOfPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcAngle`
              - Angle Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcApparentSolarTime`
              - Apparent Solar Time Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcArgumentOfLatitude`
              - Argument of Latitude Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcArgumentOfPeriapsis`
              - Argument of Periapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcBetaAngle`
              - BetaAngle Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcC3Energy`
              - C3Energy Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartesianElem`
              - Cartesian Elements Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCartSTMElem`
              - Cartesian STM Elements Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCd`
              - Cd Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachBearing`
              - CloseApproachBearing Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachCosBearing`
              - CloseApproachCosBearing Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachMagnitude`
              - CloseApproachMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachTheta`
              - CloseApproachTheta Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachX`
              - CloseApproachX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCloseApproachY`
              - CloseApproachY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCosOfVerticalFlightPathAngle`
              - CosineOfVerticalFPA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCr`
              - Cr Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion`
              - Curvilinear Relative Motion objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcCustomFunction`
              - Custom Function Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDamageFlux`
              - CoClass StateCalcDamageFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDamageMassFlux`
              - CoClass StateCalcDamageMassFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDec`
              - Dec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDecRate`
              - DeclinationRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaDec`
              - DeltaDec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaFromMaster`
              - DeltaFromMaster Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaRA`
              - DeltaRA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaV`
              - DeltaV Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDeltaVSquared`
              - DeltaV Squared Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDensity`
              - Density  Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifference`
              - Difference Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite`
              - DifferenceAcrossSegmentsOtherSat Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment`
              - DifferenceOtherSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDotProduct`
              - DotProduct Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDragArea`
              - DragArea Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDriftRateFactor`
              - DriftRateFactor Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcDuration`
              - Duration Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEarthMeanLocalTimeOfAscendingNode`
              - EarthMeanLocTimeAN Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEarthMeanSolarTime`
              - EarthMeanSolarTime Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEccentricity`
              - Eccentricity Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEccentricityAnomaly`
              - EccAnomaly Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEccentricityX`
              - EccentricityX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEccentricityY`
              - EccentricityY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEnvironment`
              - Environment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEpoch`
              - Epoch Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcEquinoctialElem`
              - Equinoctial Elements Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcFlightPathAngle`
              - FPA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcFuelMass`
              - FuelMass Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGeodeticElem`
              - Geodetic Elements Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGeodeticMeanRightAscension`
              - GeodeticMeanRightAscension Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGeodeticTrueLongitude`
              - GeodeticTrueLongitude Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGeodeticTrueLongitudeAtTimeOfPerigee`
              - GeodeticTrueLongitudeAtTimeOfPerigee Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravCoeff`
              - Gravity Coefficient Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter`
              - GravitationalParameter Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcHeightAboveTerrain`
              - CoClass AsStateCalcHeightAboveTerrain.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcImpactFlux`
              - CoClass StateCalcImpactFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcImpactMassFlux`
              - CoClass StateCalcImpactMassFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInAsympDec`
              - InAsymptoteDec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInAsympRA`
              - InAsymptoteRA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInclination`
              - Inclination Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInclinationX`
              - InclinationX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInclinationY`
              - InclinationY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInertialDeltaVMagnitude`
              - InertialDeltaVMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInertialDeltaVx`
              - InertialDeltaVx Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInertialDeltaVy`
              - InertialDeltaVy Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInertialDeltaVz`
              - InertialDeltaVz Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcInVelocityAzAtPeriapsis`
              - InVelocityAzAtPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcJacobiConstant`
              - Jacobi Constant Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcJacobiOsculating`
              - Osculating Jacobi Integral Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcLocalApparentSolarLon`
              - LocalApparentSolarLon Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcLonDriftRate`
              - LongDriftRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcLonOfAscNode`
              - LongitudeOfAscendingNode Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcLonOfPeriapsis`
              - LonOfPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMagneticFieldDipoleL`
              - CoClass StateCalcMagFieldDipoleL.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcManeuverSpecificImpulse`
              - ManeuverSpecificImpulse Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcManeuverTotalMassFlowRate`
              - ManeuverTotalMassFlowRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMass`
              - Mass Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMaxValue`
              - MaximumValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMCSDeltaV`
              - MCS DeltaV Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMCSDeltaVSquared`
              - MCS DeltaV Squared Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanAnomaly`
              - MeanAnomaly Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanEarthLon`
              - MeanEarthLon Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanMotion`
              - MeanMotion Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanRightAscension`
              - MeanRightAscension Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMeanValue`
              - MeanValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMedianValue`
              - MedianValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcMinValue`
              - MinimumValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcNegative`
              - Negative Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcNumRevs`
              - NumRevs Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess`
              - Access Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitDelaunayG`
              - CoClass AsStateCalcOrbitDelaunayG.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitDelaunayH`
              - CoClass AsStateCalcOrbitDelaunayH.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitDelaunayL`
              - CoClass AsStateCalcOrbitDelaunayL.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitPeriod`
              - OrbitPeriod Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitSemilatusRectum`
              - CoClass AsStateCalcOrbitSemiLatusRectum.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOrbitStateValue`
              - OrbitStateValue Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOutAsympDec`
              - OutAsymptoteDec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOutAsympRA`
              - OutAsymptoteRA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcOutVelocityAzAtPeriapsis`
              - OutVelocityAzAtPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPi`
              - Pi Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPositionDifferenceOtherSegment`
              - PosDifferenceOtherSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPositionVelocityDifferenceOtherSegment`
              - PosVelDifferenceOtherSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPower`
              - Power Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcPressure`
              - Pressure Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRA`
              - RA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRAAN`
              - RAAN Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRadiationPressureArea`
              - RadPressureArea Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRadiationPressureCoefficient`
              - RadiationPressureCoefficient Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRadOfApoapsis`
              - RadiusOfApoapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRadOfPeriapsis`
              - RadiusOfPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRangeRate`
              - RangeRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRARate`
              - RightAscensionRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRectifiedLon`
              - RectifiedLongitude Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius`
              - Reference Radius Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster`
              - RelAOLMaster Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeGroundTrackError`
              - RelGroundTrackError Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination`
              - Relative Inclination Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion`
              - Relative Motion Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle`
              - Relative Position Declination Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle`
              - Relative Position Declination Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRepeatingGroundTrackErr`
              - RepeatingGrTrackErr Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcRMagnitude`
              - RMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcScalar`
              - Scalar Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcScript`
              - Script Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSEETMagneticFieldLineSeparationAngle`
              - SEETMagFieldFieldLineSepAngle Calc object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSEETSAAFlux`
              - CoClass StateCalcSEETSAAFlux.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSEETVehTemp`
              - CoClass StateCalcSEETVehTemp.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSemimajorAxis`
              - SemiMajorAxis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaV`
              - Sequence DeltaV Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSequenceDeltaVSquared`
              - Sequence DeltaV Squared Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSignedEccentricity`
              - SignedEccentricity Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarBetaAngle`
              - Solar Beta Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle`
              - Solar In Plane Angle objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSpeedOfLight`
              - Speed Of Light Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSRPArea`
              - SRPArea Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcStandardDeviation`
              - StandardDeviation Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenval`
              - Cartesian STM Eigenvalues Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcSTMEigenvecElem`
              - Cartesian STM Eigenvector Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTemperature`
              - Temperature Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTimePastAscNode`
              - TimePastAscNode Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTimePastPeriapsis`
              - TimePastPeriapsis Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTrueAnomaly`
              - TrueAnomaly Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTrueLon`
              - TrueLong Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTrueLongitude`
              - TrueLongitude Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcTwoBodyDriftRate`
              - TwoBodyDriftRate Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcUnitAngularMomentumX`
              - UnitAngularMomentumX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcUnitAngularMomentumY`
              - UnitAngularMomentumY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcUnitAngularMomentumZ`
              - UnitAngularMomentumZ Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcUserValue`
              - CoClass StateCalcUserValue.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegment`
              - ValueAtSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat`
              - ValueAtSegmentOtherSat Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorDec`
              - VectorDec Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorGeometryToolAngle`
              - Vector Geometry Tool Angle Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorMagnitude`
              - VectorMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorRA`
              - VectorRA Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorX`
              - VectorX Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorY`
              - VectorY Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVectorZ`
              - VectorZ Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVelocityAz`
              - Velocity Azimuth Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVelocityDifferenceOtherSegment`
              - VelDifferenceOtherSegment Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateCalcVMagnitude`
              - VMag Calc objects.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateTransformationFunction`
              - State Transition Propagator Function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StoppingCondition`
              - A stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionCollection`
              - The stopping conditions collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionElement`
              - A stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraph`
              - Targeter Graph.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControl`
              - Targeter Graph Active Control.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphActiveControlCollection`
              - Targeter Graph Active Control Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection`
              - Targeter Graphs.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResult`
              - Targeter Graph Result.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphResultCollection`
              - Targeter Graph Result Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyFunction`
              - ThirdBody propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Thruster`
              - Thruster definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThrusterSet`
              - Thruster Set.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThrusterSetCollection`
              - Thruster Set Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TwoBodyFunction`
              - Two Body gravity propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariable`
              - User Variable.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableCollection`
              - User Variable Initial Value Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinition`
              - User Variable Definition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection`
              - User Variable Definition Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdate`
              - User Variable Update.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UserVariableUpdateCollection`
              - User Variable Update Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.USStandardAtmosphere`
              - US_Standard_Atmosphere atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.VenusGRAM2005`
              - Venus-GRAM 2005 atmospheric propagator function.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.YarkovskyFunc`
              - Yarkovsky Effect Propagator Function.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AccessCriterion`
              - The criteria of an Access stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AscentType`
              - Ascent types for the Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AtmosphereDataSource`
              - The Atmospheric data source type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeControl`
              - Attitude Control options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.AttitudeUpdate`
              - Attitude Update.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BaseSelection`
              - Access base object selections types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BodyAxis`
              - Attitude body axis options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutOptions`
              - Burnout options for the Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.BurnoutType`
              - Burnout point definition types for the Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectAngleSign`
              - The sign of the angle when the relative position has a component along the orbit normal.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectCentralBodyReference`
              - The calculation object Central Body Reference Selection types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectDirection`
              - The direction to search for a desired value.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectElement`
              - The calculation object Element Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectLocationSource`
              - The calculation object location source Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectOrbitPlaneSource`
              - The calculation object orbit plane source Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectReference`
              - The calculation object Reference Selection types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectReferenceDirection`
              - Direction that establishes the zero value when projected into the orbit plane.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectReferenceEllipse`
              - The calculation object reference ellipse Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectRelativePosition`
              - The calculation object relative position Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CalculationObjectSunPosition`
              - The calculation object sun location Types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyAttitude`
              - The central body attitude types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyEphemeris`
              - The central body ephemeris types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel`
              - The gravity model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CentralBodyShape`
              - The central body shape types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ClearEphemerisDirection`
              - Direction in which to clear ephemeris.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CoeffRungeKuttaV8th9th`
              - Coefficient sets for RKV8th(9th) integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ComplexNumber`
              - Whether a value represents the real or imaginary portion of a number.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ConstraintSign`
              - Constraint vector sign options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlAdvanced`
              - Propagate segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlEngineConstant`
              - Constant Thrust and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlEngineConstantAcceleration`
              - Constant Acceleration and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlEngineCustom`
              - Custom engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlEngineIon`
              - Ion engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlEngineModelPolynomial`
              - Polynomial Thrust and Isp engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlEngineThrottleTable`
              - Throttle table engine model properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlFollow`
              - Follow segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlInitState`
              - Initial State segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlLaunch`
              - Launch segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlManeuver`
              - Maneuver segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlOrbitStateValue`
              - Orbit State Value properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlPowerInternal`
              - Internal Power properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlPowerProcessed`
              - Processed Power properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlPowerSolarArray`
              - Solar Array Power properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlRepeatingGroundTrackErr`
              - Repeating Ground Track Equator Error properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlStoppingCondition`
              - The stopping condition control types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlThrusters`
              - Thruster properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ControlUpdate`
              - Update segment properties that can be selected as control parameters for a Target Sequence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ConvergenceCriteria`
              - The Convergence Criteria types for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Criteria`
              - The criteria type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Criterion`
              - The stopping condition criterion types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.CustomFunction`
              - Attitude definition options for other STK functions.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DerivativeCalculationMethod`
              - The Derivative Calculation method types for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferenceOrder`
              - The Difference order types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DifferentialCorrectorScalingMethod`
              - The Scaling Method types for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DragModelType`
              - Type of Drag Model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.DrawPerturbation`
              - The Draw Perturbation types for a Differential Corrector profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EclipsingBodiesSource`
              - The source types of the eclipsing bodies list.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementSetType`
              - Types of orbit element sets.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ElementType`
              - Which type of elements (osculating or mean).

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EngineModelFunction`
              - The engine model function types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.EphemerisSource`
              - The ephemeris source type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ErrorControl`
              - Error Control for the numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FollowJoin`
              - Joining options for the Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FollowSeparation`
              - Separation options for the Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.FollowSpacecraftAndFuelTank`
              - Spacecraft parameter options for the Follow segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Formulation`
              - Equinoctial Formulation.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GeoMagneticFluxSource`
              - Whether to use Kp or Ap data from the flux file.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GeoMagneticFluxUpdateRate`
              - Method for using geomagnetic flux values from the flux file.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GeoStationaryDriftRateModel`
              - Gravity models used to compute geostationary drift rate.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GeoStationaryInclinationMagnitude`
              - Magnitude to use when computing the inclination vector.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionDesiredOperation`
              - The types for Desired Operation/Objective of golden section profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GraphOption`
              - Mode that the mcs will run in.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GravitationalParameterSource`
              - The source of the gravitational parameter for a CStateCalcGravitationalParameter calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GravityCoefficientNormalizationType`
              - The normalization type for the CStateCalcGravCoeff calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GravityCoefficientType`
              - The coefficient type for the CStateCalcGravCoeff calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GravParamSource`
              - The gravity parameter source.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.GridSearchDesiredOperation`
              - The types for Desired Operation/Objective of Grid Search profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IdealOrbitRadius`
              - Ideal Orbit Radius.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ImpulsiveDeltaVRepresentation`
              - Vector representations for impulsive DeltaV specification.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.IPOPTGoal`
              - The Goal types for a IPOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LambertDirectionOfMotionType`
              - Lambert Direction Of Motion Type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LambertOrbitalEnergyType`
              - Lambert Orbital Energy Type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LambertSolutionOptionType`
              - Lambert Solution Option Type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LambertTargetCoordinateType`
              - Lambert Target CoordType.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Language`
              - Scripting language types for the Scripting Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LaunchDisplaySystem`
              - Launch location coordinate types for the Launch segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.LightingCondition`
              - The criteria of a Lighting stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ManeuverType`
              - Maneuver types for the maneuver segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.MarsGRAMDensityType`
              - Density Type for MarsGRAM Density Models.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.NumericalIntegrator`
              - Numerical integrator type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteDiscretizationStrategy`
              - Discretization Strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteExportNodesFormat`
              - Steering nodes export format.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteGuessMethod`
              - Guess interpolation method.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteRunMode`
              - Run modes.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteScalingOptions`
              - Scaling Options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteSeedMethod`
              - Seed methods.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteSNOPTObjective`
              - Optimal Finite SNOPT objective.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteSNOPTScaling`
              - Optimal Finite SNOPT scaling option.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.OptimalFiniteWorkingVariables`
              - Working Variables.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PredictorCorrector`
              - Predictor corrector scheme for the numerical integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PressureMode`
              - Pressure Mode options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.Profile`
              - Type of profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileInsertDirection`
              - Direction to insert profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfileMode`
              - The Target Sequence profile modes.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ProfilesFinish`
              - Action options for Target Sequence profiles convergence.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.PropulsionMethod`
              - Propulsion method options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ReferenceRadiusSource`
              - The source of the reference radius for a CStateCalcReferenceRadius calculation object.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ReturnControl`
              - The Return segment control types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RootFindingAlgorithm`
              - Root-finding algorithms.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RotatingCoordinateSystem`
              - Barycenter centered rotating system.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.RunCode`
              - The run code returned after the MCS is run.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterType`
              - Scripting Tool parameter type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SegmentDifferenceOrder`
              - The Difference Across Segments order types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SegmentState`
              - Segment state to use types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SegmentType`
              - Segment types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SequenceStateToPass`
              - State To Pass options for the Sequence segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ShadowModel`
              - The shadow model type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SmartRunMode`
              - Mode that the mcs will run in.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SNOPTGoal`
              - The Goal types for a SNOPT profile.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SolarForceMethod`
              - The solar force method type for a spherical or N-plate SRP model.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SquaredType`
              - Whether to calculate the value as the square of the sum of each component or the sum of the squares.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StateType`
              - The Stop segment state types.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.STMEigenNumber`
              - The number that describes one of the 6 STM Eigenvalues or Eigenvectors.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.STMPerturbationVariables`
              - The initial and final Cartesian variational variables that describe an STM element.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.StoppingConditionType`
              - Type of stopping condition.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.SunPosition`
              - The sun position type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TabVecInterpolationMethod`
              - The interpolation method for tabulated area vector file.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.TargetSequenceAction`
              - Action options for Target Sequence profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThirdBodyMode`
              - The third body gravity mode.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThrottleTableOperationMode`
              - Engine operation mode.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThrusterDirection`
              - The thruster direction type.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.ThrustType`
              - Thrust options.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UpdateAction`
              - Actions for the Update segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.UpdateParam`
              - Spacecraft parameters that can be modified by an Update segment.

            * - :py:class:`~ansys.stk.core.stkobjects.astrogator.VenusGRAMDensityType`
              - Density Type for VenusGRAM Density Models.



Description
-----------

Object Model components specifically designed to support STK Astrogator.


.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IAttitudeControl<astrogator/IAttitudeControl>
     IAttitudeControlFinite<astrogator/IAttitudeControlFinite>
     IAttitudeControlImpulsive<astrogator/IAttitudeControlImpulsive>
     IAttitudeControlOptimalFinite<astrogator/IAttitudeControlOptimalFinite>
     IBurnout<astrogator/IBurnout>
     ICentralBodyComponentAttitude<astrogator/ICentralBodyComponentAttitude>
     ICentralBodyComponentEphemeris<astrogator/ICentralBodyComponentEphemeris>
     ICentralBodyComponentEphemerisJPLDevelopmentalEphemerides<astrogator/ICentralBodyComponentEphemerisJPLDevelopmentalEphemerides>
     ICentralBodyComponentShape<astrogator/ICentralBodyComponentShape>
     IDisplaySystem<astrogator/IDisplaySystem>
     IElement<astrogator/IElement>
     IManeuver<astrogator/IManeuver>
     IMCSSegment<astrogator/IMCSSegment>
     IMCSSequence<astrogator/IMCSSequence>
     INumericalIntegrator<astrogator/INumericalIntegrator>
     IProfile<astrogator/IProfile>
     IStoppingConditionComponent<astrogator/IStoppingConditionComponent>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     AccessStoppingCondition<astrogator/AccessStoppingCondition>
     AsTriggerCondition<astrogator/AsTriggerCondition>
     AttitudeControlFiniteAntiVelocityVector<astrogator/AttitudeControlFiniteAntiVelocityVector>
     AttitudeControlFiniteAttitude<astrogator/AttitudeControlFiniteAttitude>
     AttitudeControlFiniteFile<astrogator/AttitudeControlFiniteFile>
     AttitudeControlFinitePlugin<astrogator/AttitudeControlFinitePlugin>
     AttitudeControlFiniteThrustVector<astrogator/AttitudeControlFiniteThrustVector>
     AttitudeControlFiniteTimeVarying<astrogator/AttitudeControlFiniteTimeVarying>
     AttitudeControlFiniteVelocityVector<astrogator/AttitudeControlFiniteVelocityVector>
     AttitudeControlImpulsiveAntiVelocityVector<astrogator/AttitudeControlImpulsiveAntiVelocityVector>
     AttitudeControlImpulsiveAttitude<astrogator/AttitudeControlImpulsiveAttitude>
     AttitudeControlImpulsiveFile<astrogator/AttitudeControlImpulsiveFile>
     AttitudeControlImpulsiveThrustVector<astrogator/AttitudeControlImpulsiveThrustVector>
     AttitudeControlImpulsiveVelocityVector<astrogator/AttitudeControlImpulsiveVelocityVector>
     AttitudeControlOptimalFiniteLagrange<astrogator/AttitudeControlOptimalFiniteLagrange>
     AutomaticSequence<astrogator/AutomaticSequence>
     AutomaticSequenceCollection<astrogator/AutomaticSequenceCollection>
     BDotRCalc<astrogator/BDotRCalc>
     BDotTCalc<astrogator/BDotTCalc>
     BisectionControl<astrogator/BisectionControl>
     BisectionControlCollection<astrogator/BisectionControlCollection>
     BisectionResult<astrogator/BisectionResult>
     BisectionResultCollection<astrogator/BisectionResultCollection>
     BlendedDensity<astrogator/BlendedDensity>
     BMagnitudeCalc<astrogator/BMagnitudeCalc>
     BPlaneCollection<astrogator/BPlaneCollection>
     BThetaCalc<astrogator/BThetaCalc>
     BulirschStoerIntegrator<astrogator/BulirschStoerIntegrator>
     BurnoutCBFCartesian<astrogator/BurnoutCBFCartesian>
     BurnoutGeocentric<astrogator/BurnoutGeocentric>
     BurnoutGeodetic<astrogator/BurnoutGeodetic>
     BurnoutLaunchAzAltitude<astrogator/BurnoutLaunchAzAltitude>
     BurnoutLaunchAzRadius<astrogator/BurnoutLaunchAzRadius>
     BurnoutVelocity<astrogator/BurnoutVelocity>
     CalculationGraphCollection<astrogator/CalculationGraphCollection>
     CalculationObjectCollection<astrogator/CalculationObjectCollection>
     CalculationObjectLinkEmbedControlCollection<astrogator/CalculationObjectLinkEmbedControlCollection>
     CentralBodyComponent<astrogator/CentralBodyComponent>
     CentralBodyComponentAttitudeIAU1994<astrogator/CentralBodyComponentAttitudeIAU1994>
     CentralBodyComponentAttitudeRotationCoefficientsFile<astrogator/CentralBodyComponentAttitudeRotationCoefficientsFile>
     CentralBodyComponentCollection<astrogator/CentralBodyComponentCollection>
     CentralBodyComponentEphemerisAnalyticOrbit<astrogator/CentralBodyComponentEphemerisAnalyticOrbit>
     CentralBodyComponentEphemerisFile<astrogator/CentralBodyComponentEphemerisFile>
     CentralBodyComponentEphemerisJPLDesignExplorerOptimizer<astrogator/CentralBodyComponentEphemerisJPLDesignExplorerOptimizer>
     CentralBodyComponentEphemerisJPLSpice<astrogator/CentralBodyComponentEphemerisJPLSpice>
     CentralBodyComponentEphemerisPlanetary<astrogator/CentralBodyComponentEphemerisPlanetary>
     CentralBodyComponentGravityModel<astrogator/CentralBodyComponentGravityModel>
     CentralBodyComponentShapeOblateSpheroid<astrogator/CentralBodyComponentShapeOblateSpheroid>
     CentralBodyComponentShapeSphere<astrogator/CentralBodyComponentShapeSphere>
     CentralBodyComponentShapeTriaxialEllipsoid<astrogator/CentralBodyComponentShapeTriaxialEllipsoid>
     Cira72Function<astrogator/Cira72Function>
     ConstraintCollection<astrogator/ConstraintCollection>
     CR3BPFunction<astrogator/CR3BPFunction>
     CustomFunctionScriptEngine<astrogator/CustomFunctionScriptEngine>
     DensityModelPlugin<astrogator/DensityModelPlugin>
     DesignCR3BPObject<astrogator/DesignCR3BPObject>
     DesignCR3BPObjectCollection<astrogator/DesignCR3BPObjectCollection>
     DesignCR3BPSetup<astrogator/DesignCR3BPSetup>
     DesignER3BPObject<astrogator/DesignER3BPObject>
     DesignER3BPObjectCollection<astrogator/DesignER3BPObjectCollection>
     DesignER3BPSetup<astrogator/DesignER3BPSetup>
     DifferentialCorrectorControl<astrogator/DifferentialCorrectorControl>
     DifferentialCorrectorControlCollection<astrogator/DifferentialCorrectorControlCollection>
     DifferentialCorrectorResult<astrogator/DifferentialCorrectorResult>
     DifferentialCorrectorResultCollection<astrogator/DifferentialCorrectorResultCollection>
     DisplaySystemGeocentric<astrogator/DisplaySystemGeocentric>
     DisplaySystemGeodetic<astrogator/DisplaySystemGeodetic>
     DragModelPlugin<astrogator/DragModelPlugin>
     DTM2012<astrogator/DTM2012>
     DTM2020<astrogator/DTM2020>
     ElementBPlane<astrogator/ElementBPlane>
     ElementCartesian<astrogator/ElementCartesian>
     ElementDelaunay<astrogator/ElementDelaunay>
     ElementEquinoctial<astrogator/ElementEquinoctial>
     ElementGeodetic<astrogator/ElementGeodetic>
     ElementKeplerian<astrogator/ElementKeplerian>
     ElementMixedSpherical<astrogator/ElementMixedSpherical>
     ElementSpherical<astrogator/ElementSpherical>
     ElementSphericalRangeRate<astrogator/ElementSphericalRangeRate>
     ElementTargetVectorIncomingAsymptote<astrogator/ElementTargetVectorIncomingAsymptote>
     ElementTargetVectorOutgoingAsymptote<astrogator/ElementTargetVectorOutgoingAsymptote>
     EngineConstant<astrogator/EngineConstant>
     EngineConstantAcceleration<astrogator/EngineConstantAcceleration>
     EngineCustom<astrogator/EngineCustom>
     EngineDefinition<astrogator/EngineDefinition>
     EngineIon<astrogator/EngineIon>
     EngineModelIspCoefficients<astrogator/EngineModelIspCoefficients>
     EngineModelPolynomial<astrogator/EngineModelPolynomial>
     EngineModelThrustCoefficients<astrogator/EngineModelThrustCoefficients>
     EnginePlugin<astrogator/EnginePlugin>
     EngineThrottleTable<astrogator/EngineThrottleTable>
     EOMFuncPluginFunction<astrogator/EOMFuncPluginFunction>
     ER3BPFunc<astrogator/ER3BPFunc>
     Exponential<astrogator/Exponential>
     FuelTank<astrogator/FuelTank>
     GaussJacksonIntegrator<astrogator/GaussJacksonIntegrator>
     GeneralRelativityFunction<astrogator/GeneralRelativityFunction>
     GoldenSectionControl<astrogator/GoldenSectionControl>
     GoldenSectionControlCollection<astrogator/GoldenSectionControlCollection>
     GoldenSectionResult<astrogator/GoldenSectionResult>
     GoldenSectionResultCollection<astrogator/GoldenSectionResultCollection>
     GravityFieldFunction<astrogator/GravityFieldFunction>
     GridSearchControl<astrogator/GridSearchControl>
     GridSearchControlCollection<astrogator/GridSearchControlCollection>
     GridSearchResult<astrogator/GridSearchResult>
     GridSearchResultCollection<astrogator/GridSearchResultCollection>
     HarrisPriester<astrogator/HarrisPriester>
     HPOPPluginFunction<astrogator/HPOPPluginFunction>
     IPOPTControl<astrogator/IPOPTControl>
     IPOPTControlCollection<astrogator/IPOPTControlCollection>
     IPOPTResult<astrogator/IPOPTResult>
     IPOPTResultCollection<astrogator/IPOPTResultCollection>
     Jacchia1960<astrogator/Jacchia1960>
     Jacchia1970<astrogator/Jacchia1970>
     Jacchia1971<astrogator/Jacchia1971>
     JacchiaBowman2008<astrogator/JacchiaBowman2008>
     JacchiaRoberts<astrogator/JacchiaRoberts>
     LightingStoppingCondition<astrogator/LightingStoppingCondition>
     ManeuverFinite<astrogator/ManeuverFinite>
     ManeuverFinitePropagator<astrogator/ManeuverFinitePropagator>
     ManeuverImpulsive<astrogator/ManeuverImpulsive>
     ManeuverOptimalFinite<astrogator/ManeuverOptimalFinite>
     ManeuverOptimalFiniteBounds<astrogator/ManeuverOptimalFiniteBounds>
     ManeuverOptimalFiniteFinalBoundaryConditions<astrogator/ManeuverOptimalFiniteFinalBoundaryConditions>
     ManeuverOptimalFiniteInitialBoundaryConditions<astrogator/ManeuverOptimalFiniteInitialBoundaryConditions>
     ManeuverOptimalFinitePathBoundaryConditions<astrogator/ManeuverOptimalFinitePathBoundaryConditions>
     ManeuverOptimalFiniteSNOPTOptimizer<astrogator/ManeuverOptimalFiniteSNOPTOptimizer>
     ManeuverOptimalFiniteSteeringNodeCollection<astrogator/ManeuverOptimalFiniteSteeringNodeCollection>
     ManeuverOptimalFiniteSteeringNodeElement<astrogator/ManeuverOptimalFiniteSteeringNodeElement>
     MarsGRAM2000<astrogator/MarsGRAM2000>
     MarsGRAM2001<astrogator/MarsGRAM2001>
     MarsGRAM2005<astrogator/MarsGRAM2005>
     MarsGRAM2010<astrogator/MarsGRAM2010>
     MarsGRAM37<astrogator/MarsGRAM37>
     MCSBackwardSequence<astrogator/MCSBackwardSequence>
     MCSDriver<astrogator/MCSDriver>
     MCSEnd<astrogator/MCSEnd>
     MCSFollow<astrogator/MCSFollow>
     MCSHold<astrogator/MCSHold>
     MCSInitialState<astrogator/MCSInitialState>
     MCSLaunch<astrogator/MCSLaunch>
     MCSManeuver<astrogator/MCSManeuver>
     MCSOptions<astrogator/MCSOptions>
     MCSPropagate<astrogator/MCSPropagate>
     MCSReturn<astrogator/MCSReturn>
     MCSSegmentCollection<astrogator/MCSSegmentCollection>
     MCSSegmentProperties<astrogator/MCSSegmentProperties>
     MCSSequence<astrogator/MCSSequence>
     MCSStop<astrogator/MCSStop>
     MCSTargetSequence<astrogator/MCSTargetSequence>
     MCSUpdate<astrogator/MCSUpdate>
     MSIS1986<astrogator/MSIS1986>
     MSISE1990<astrogator/MSISE1990>
     NRLMSISE2000<astrogator/NRLMSISE2000>
     NumericalPropagatorWrapper<astrogator/NumericalPropagatorWrapper>
     NumericalPropagatorWrapperCR3BP<astrogator/NumericalPropagatorWrapperCR3BP>
     PluginProperties<astrogator/PluginProperties>
     PointMassFunction<astrogator/PointMassFunction>
     PowerInternal<astrogator/PowerInternal>
     PowerProcessed<astrogator/PowerProcessed>
     PowerSolarArray<astrogator/PowerSolarArray>
     ProfileBisection<astrogator/ProfileBisection>
     ProfileChangeManeuverType<astrogator/ProfileChangeManeuverType>
     ProfileChangePropagator<astrogator/ProfileChangePropagator>
     ProfileChangeReturnSegment<astrogator/ProfileChangeReturnSegment>
     ProfileChangeStoppingConditionState<astrogator/ProfileChangeStoppingConditionState>
     ProfileChangeStopSegment<astrogator/ProfileChangeStopSegment>
     ProfileCollection<astrogator/ProfileCollection>
     ProfileDifferentialCorrector<astrogator/ProfileDifferentialCorrector>
     ProfileGoldenSection<astrogator/ProfileGoldenSection>
     ProfileGridSearch<astrogator/ProfileGridSearch>
     ProfileIPOPTOptimizer<astrogator/ProfileIPOPTOptimizer>
     ProfileLambertProfile<astrogator/ProfileLambertProfile>
     ProfileLambertSearchProfile<astrogator/ProfileLambertSearchProfile>
     ProfileRunOnce<astrogator/ProfileRunOnce>
     ProfileScriptingTool<astrogator/ProfileScriptingTool>
     ProfileSearchPlugin<astrogator/ProfileSearchPlugin>
     ProfileSeedFiniteManeuver<astrogator/ProfileSeedFiniteManeuver>
     ProfileSNOPTOptimizer<astrogator/ProfileSNOPTOptimizer>
     PropagatorFunctionCollection<astrogator/PropagatorFunctionCollection>
     RadiationPressureFunction<astrogator/RadiationPressureFunction>
     RungeKutta2nd3rd<astrogator/RungeKutta2nd3rd>
     RungeKutta4th<astrogator/RungeKutta4th>
     RungeKutta4th5th<astrogator/RungeKutta4th5th>
     RungeKutta4thAdapt<astrogator/RungeKutta4thAdapt>
     RungeKuttaF7th8th<astrogator/RungeKuttaF7th8th>
     RungeKuttaV8th9th<astrogator/RungeKuttaV8th9th>
     ScriptingCalculationObject<astrogator/ScriptingCalculationObject>
     ScriptingCalculationObjectCollection<astrogator/ScriptingCalculationObjectCollection>
     ScriptingParameter<astrogator/ScriptingParameter>
     ScriptingParameterCollection<astrogator/ScriptingParameterCollection>
     ScriptingParameterEnumerationChoice<astrogator/ScriptingParameterEnumerationChoice>
     ScriptingParameterEnumerationChoiceCollection<astrogator/ScriptingParameterEnumerationChoiceCollection>
     ScriptingSegment<astrogator/ScriptingSegment>
     ScriptingSegmentCollection<astrogator/ScriptingSegmentCollection>
     ScriptingTool<astrogator/ScriptingTool>
     SearchPluginControl<astrogator/SearchPluginControl>
     SearchPluginControlCollection<astrogator/SearchPluginControlCollection>
     SearchPluginResult<astrogator/SearchPluginResult>
     SearchPluginResultCollection<astrogator/SearchPluginResultCollection>
     SNOPTControl<astrogator/SNOPTControl>
     SNOPTControlCollection<astrogator/SNOPTControlCollection>
     SNOPTResult<astrogator/SNOPTResult>
     SNOPTResultCollection<astrogator/SNOPTResultCollection>
     SpacecraftParameters<astrogator/SpacecraftParameters>
     SRPAerospaceT20<astrogator/SRPAerospaceT20>
     SRPAerospaceT30<astrogator/SRPAerospaceT30>
     SRPGSPM04aeIIA<astrogator/SRPGSPM04aeIIA>
     SRPGSPM04aeIIR<astrogator/SRPGSPM04aeIIR>
     SRPGSPM04aIIA<astrogator/SRPGSPM04aIIA>
     SRPGSPM04aIIR<astrogator/SRPGSPM04aIIR>
     SRPNPlate<astrogator/SRPNPlate>
     SRPReflectionPlugin<astrogator/SRPReflectionPlugin>
     SRPSpherical<astrogator/SRPSpherical>
     SRPTabulatedAreaVector<astrogator/SRPTabulatedAreaVector>
     SRPVariableArea<astrogator/SRPVariableArea>
     State<astrogator/State>
     StateCalcAbsoluteValue<astrogator/StateCalcAbsoluteValue>
     StateCalcAltitudeOfApoapsis<astrogator/StateCalcAltitudeOfApoapsis>
     StateCalcAltitudeOfPeriapsis<astrogator/StateCalcAltitudeOfPeriapsis>
     StateCalcAngle<astrogator/StateCalcAngle>
     StateCalcApparentSolarTime<astrogator/StateCalcApparentSolarTime>
     StateCalcArgumentOfLatitude<astrogator/StateCalcArgumentOfLatitude>
     StateCalcArgumentOfPeriapsis<astrogator/StateCalcArgumentOfPeriapsis>
     StateCalcBetaAngle<astrogator/StateCalcBetaAngle>
     StateCalcC3Energy<astrogator/StateCalcC3Energy>
     StateCalcCartesianElem<astrogator/StateCalcCartesianElem>
     StateCalcCartSTMElem<astrogator/StateCalcCartSTMElem>
     StateCalcCd<astrogator/StateCalcCd>
     StateCalcCloseApproachBearing<astrogator/StateCalcCloseApproachBearing>
     StateCalcCloseApproachCosBearing<astrogator/StateCalcCloseApproachCosBearing>
     StateCalcCloseApproachMagnitude<astrogator/StateCalcCloseApproachMagnitude>
     StateCalcCloseApproachTheta<astrogator/StateCalcCloseApproachTheta>
     StateCalcCloseApproachX<astrogator/StateCalcCloseApproachX>
     StateCalcCloseApproachY<astrogator/StateCalcCloseApproachY>
     StateCalcCosOfVerticalFlightPathAngle<astrogator/StateCalcCosOfVerticalFlightPathAngle>
     StateCalcCr<astrogator/StateCalcCr>
     StateCalcCurvilinearRelativeMotion<astrogator/StateCalcCurvilinearRelativeMotion>
     StateCalcCustomFunction<astrogator/StateCalcCustomFunction>
     StateCalcDamageFlux<astrogator/StateCalcDamageFlux>
     StateCalcDamageMassFlux<astrogator/StateCalcDamageMassFlux>
     StateCalcDec<astrogator/StateCalcDec>
     StateCalcDecRate<astrogator/StateCalcDecRate>
     StateCalcDeltaDec<astrogator/StateCalcDeltaDec>
     StateCalcDeltaFromMaster<astrogator/StateCalcDeltaFromMaster>
     StateCalcDeltaRA<astrogator/StateCalcDeltaRA>
     StateCalcDeltaV<astrogator/StateCalcDeltaV>
     StateCalcDeltaVSquared<astrogator/StateCalcDeltaVSquared>
     StateCalcDensity<astrogator/StateCalcDensity>
     StateCalcDifference<astrogator/StateCalcDifference>
     StateCalcDifferenceAcrossSegmentsOtherSatellite<astrogator/StateCalcDifferenceAcrossSegmentsOtherSatellite>
     StateCalcDifferenceOtherSegment<astrogator/StateCalcDifferenceOtherSegment>
     StateCalcDotProduct<astrogator/StateCalcDotProduct>
     StateCalcDragArea<astrogator/StateCalcDragArea>
     StateCalcDriftRateFactor<astrogator/StateCalcDriftRateFactor>
     StateCalcDuration<astrogator/StateCalcDuration>
     StateCalcEarthMeanLocalTimeOfAscendingNode<astrogator/StateCalcEarthMeanLocalTimeOfAscendingNode>
     StateCalcEarthMeanSolarTime<astrogator/StateCalcEarthMeanSolarTime>
     StateCalcEccentricity<astrogator/StateCalcEccentricity>
     StateCalcEccentricityAnomaly<astrogator/StateCalcEccentricityAnomaly>
     StateCalcEccentricityX<astrogator/StateCalcEccentricityX>
     StateCalcEccentricityY<astrogator/StateCalcEccentricityY>
     StateCalcEnvironment<astrogator/StateCalcEnvironment>
     StateCalcEpoch<astrogator/StateCalcEpoch>
     StateCalcEquinoctialElem<astrogator/StateCalcEquinoctialElem>
     StateCalcFlightPathAngle<astrogator/StateCalcFlightPathAngle>
     StateCalcFuelMass<astrogator/StateCalcFuelMass>
     StateCalcGeodeticElem<astrogator/StateCalcGeodeticElem>
     StateCalcGeodeticMeanRightAscension<astrogator/StateCalcGeodeticMeanRightAscension>
     StateCalcGeodeticTrueLongitude<astrogator/StateCalcGeodeticTrueLongitude>
     StateCalcGeodeticTrueLongitudeAtTimeOfPerigee<astrogator/StateCalcGeodeticTrueLongitudeAtTimeOfPerigee>
     StateCalcGravCoeff<astrogator/StateCalcGravCoeff>
     StateCalcGravitationalParameter<astrogator/StateCalcGravitationalParameter>
     StateCalcHeightAboveTerrain<astrogator/StateCalcHeightAboveTerrain>
     StateCalcImpactFlux<astrogator/StateCalcImpactFlux>
     StateCalcImpactMassFlux<astrogator/StateCalcImpactMassFlux>
     StateCalcInAsympDec<astrogator/StateCalcInAsympDec>
     StateCalcInAsympRA<astrogator/StateCalcInAsympRA>
     StateCalcInclination<astrogator/StateCalcInclination>
     StateCalcInclinationX<astrogator/StateCalcInclinationX>
     StateCalcInclinationY<astrogator/StateCalcInclinationY>
     StateCalcInertialDeltaVMagnitude<astrogator/StateCalcInertialDeltaVMagnitude>
     StateCalcInertialDeltaVx<astrogator/StateCalcInertialDeltaVx>
     StateCalcInertialDeltaVy<astrogator/StateCalcInertialDeltaVy>
     StateCalcInertialDeltaVz<astrogator/StateCalcInertialDeltaVz>
     StateCalcInVelocityAzAtPeriapsis<astrogator/StateCalcInVelocityAzAtPeriapsis>
     StateCalcJacobiConstant<astrogator/StateCalcJacobiConstant>
     StateCalcJacobiOsculating<astrogator/StateCalcJacobiOsculating>
     StateCalcLocalApparentSolarLon<astrogator/StateCalcLocalApparentSolarLon>
     StateCalcLonDriftRate<astrogator/StateCalcLonDriftRate>
     StateCalcLonOfAscNode<astrogator/StateCalcLonOfAscNode>
     StateCalcLonOfPeriapsis<astrogator/StateCalcLonOfPeriapsis>
     StateCalcMagneticFieldDipoleL<astrogator/StateCalcMagneticFieldDipoleL>
     StateCalcManeuverSpecificImpulse<astrogator/StateCalcManeuverSpecificImpulse>
     StateCalcManeuverTotalMassFlowRate<astrogator/StateCalcManeuverTotalMassFlowRate>
     StateCalcMass<astrogator/StateCalcMass>
     StateCalcMaxValue<astrogator/StateCalcMaxValue>
     StateCalcMCSDeltaV<astrogator/StateCalcMCSDeltaV>
     StateCalcMCSDeltaVSquared<astrogator/StateCalcMCSDeltaVSquared>
     StateCalcMeanAnomaly<astrogator/StateCalcMeanAnomaly>
     StateCalcMeanEarthLon<astrogator/StateCalcMeanEarthLon>
     StateCalcMeanMotion<astrogator/StateCalcMeanMotion>
     StateCalcMeanRightAscension<astrogator/StateCalcMeanRightAscension>
     StateCalcMeanValue<astrogator/StateCalcMeanValue>
     StateCalcMedianValue<astrogator/StateCalcMedianValue>
     StateCalcMinValue<astrogator/StateCalcMinValue>
     StateCalcNegative<astrogator/StateCalcNegative>
     StateCalcNumRevs<astrogator/StateCalcNumRevs>
     StateCalcOnePointAccess<astrogator/StateCalcOnePointAccess>
     StateCalcOrbitDelaunayG<astrogator/StateCalcOrbitDelaunayG>
     StateCalcOrbitDelaunayH<astrogator/StateCalcOrbitDelaunayH>
     StateCalcOrbitDelaunayL<astrogator/StateCalcOrbitDelaunayL>
     StateCalcOrbitPeriod<astrogator/StateCalcOrbitPeriod>
     StateCalcOrbitSemilatusRectum<astrogator/StateCalcOrbitSemilatusRectum>
     StateCalcOrbitStateValue<astrogator/StateCalcOrbitStateValue>
     StateCalcOutAsympDec<astrogator/StateCalcOutAsympDec>
     StateCalcOutAsympRA<astrogator/StateCalcOutAsympRA>
     StateCalcOutVelocityAzAtPeriapsis<astrogator/StateCalcOutVelocityAzAtPeriapsis>
     StateCalcPi<astrogator/StateCalcPi>
     StateCalcPositionDifferenceOtherSegment<astrogator/StateCalcPositionDifferenceOtherSegment>
     StateCalcPositionVelocityDifferenceOtherSegment<astrogator/StateCalcPositionVelocityDifferenceOtherSegment>
     StateCalcPower<astrogator/StateCalcPower>
     StateCalcPressure<astrogator/StateCalcPressure>
     StateCalcRA<astrogator/StateCalcRA>
     StateCalcRAAN<astrogator/StateCalcRAAN>
     StateCalcRadiationPressureArea<astrogator/StateCalcRadiationPressureArea>
     StateCalcRadiationPressureCoefficient<astrogator/StateCalcRadiationPressureCoefficient>
     StateCalcRadOfApoapsis<astrogator/StateCalcRadOfApoapsis>
     StateCalcRadOfPeriapsis<astrogator/StateCalcRadOfPeriapsis>
     StateCalcRangeRate<astrogator/StateCalcRangeRate>
     StateCalcRARate<astrogator/StateCalcRARate>
     StateCalcRectifiedLon<astrogator/StateCalcRectifiedLon>
     StateCalcReferenceRadius<astrogator/StateCalcReferenceRadius>
     StateCalcRelativeAtAOLMaster<astrogator/StateCalcRelativeAtAOLMaster>
     StateCalcRelativeGroundTrackError<astrogator/StateCalcRelativeGroundTrackError>
     StateCalcRelativeInclination<astrogator/StateCalcRelativeInclination>
     StateCalcRelativeMotion<astrogator/StateCalcRelativeMotion>
     StateCalcRelativePositionDecAngle<astrogator/StateCalcRelativePositionDecAngle>
     StateCalcRelativePositionInPlaneAngle<astrogator/StateCalcRelativePositionInPlaneAngle>
     StateCalcRepeatingGroundTrackErr<astrogator/StateCalcRepeatingGroundTrackErr>
     StateCalcRMagnitude<astrogator/StateCalcRMagnitude>
     StateCalcScalar<astrogator/StateCalcScalar>
     StateCalcScript<astrogator/StateCalcScript>
     StateCalcSEETMagneticFieldLineSeparationAngle<astrogator/StateCalcSEETMagneticFieldLineSeparationAngle>
     StateCalcSEETSAAFlux<astrogator/StateCalcSEETSAAFlux>
     StateCalcSEETVehTemp<astrogator/StateCalcSEETVehTemp>
     StateCalcSemimajorAxis<astrogator/StateCalcSemimajorAxis>
     StateCalcSequenceDeltaV<astrogator/StateCalcSequenceDeltaV>
     StateCalcSequenceDeltaVSquared<astrogator/StateCalcSequenceDeltaVSquared>
     StateCalcSignedEccentricity<astrogator/StateCalcSignedEccentricity>
     StateCalcSolarBetaAngle<astrogator/StateCalcSolarBetaAngle>
     StateCalcSolarInPlaneAngle<astrogator/StateCalcSolarInPlaneAngle>
     StateCalcSpeedOfLight<astrogator/StateCalcSpeedOfLight>
     StateCalcSRPArea<astrogator/StateCalcSRPArea>
     StateCalcStandardDeviation<astrogator/StateCalcStandardDeviation>
     StateCalcSTMEigenval<astrogator/StateCalcSTMEigenval>
     StateCalcSTMEigenvecElem<astrogator/StateCalcSTMEigenvecElem>
     StateCalcTemperature<astrogator/StateCalcTemperature>
     StateCalcTimePastAscNode<astrogator/StateCalcTimePastAscNode>
     StateCalcTimePastPeriapsis<astrogator/StateCalcTimePastPeriapsis>
     StateCalcTrueAnomaly<astrogator/StateCalcTrueAnomaly>
     StateCalcTrueLon<astrogator/StateCalcTrueLon>
     StateCalcTrueLongitude<astrogator/StateCalcTrueLongitude>
     StateCalcTwoBodyDriftRate<astrogator/StateCalcTwoBodyDriftRate>
     StateCalcUnitAngularMomentumX<astrogator/StateCalcUnitAngularMomentumX>
     StateCalcUnitAngularMomentumY<astrogator/StateCalcUnitAngularMomentumY>
     StateCalcUnitAngularMomentumZ<astrogator/StateCalcUnitAngularMomentumZ>
     StateCalcUserValue<astrogator/StateCalcUserValue>
     StateCalcValueAtSegment<astrogator/StateCalcValueAtSegment>
     StateCalcValueAtSegmentOtherSat<astrogator/StateCalcValueAtSegmentOtherSat>
     StateCalcVectorDec<astrogator/StateCalcVectorDec>
     StateCalcVectorGeometryToolAngle<astrogator/StateCalcVectorGeometryToolAngle>
     StateCalcVectorMagnitude<astrogator/StateCalcVectorMagnitude>
     StateCalcVectorRA<astrogator/StateCalcVectorRA>
     StateCalcVectorX<astrogator/StateCalcVectorX>
     StateCalcVectorY<astrogator/StateCalcVectorY>
     StateCalcVectorZ<astrogator/StateCalcVectorZ>
     StateCalcVelocityAz<astrogator/StateCalcVelocityAz>
     StateCalcVelocityDifferenceOtherSegment<astrogator/StateCalcVelocityDifferenceOtherSegment>
     StateCalcVMagnitude<astrogator/StateCalcVMagnitude>
     StateTransformationFunction<astrogator/StateTransformationFunction>
     StoppingCondition<astrogator/StoppingCondition>
     StoppingConditionCollection<astrogator/StoppingConditionCollection>
     StoppingConditionElement<astrogator/StoppingConditionElement>
     TargeterGraph<astrogator/TargeterGraph>
     TargeterGraphActiveControl<astrogator/TargeterGraphActiveControl>
     TargeterGraphActiveControlCollection<astrogator/TargeterGraphActiveControlCollection>
     TargeterGraphCollection<astrogator/TargeterGraphCollection>
     TargeterGraphResult<astrogator/TargeterGraphResult>
     TargeterGraphResultCollection<astrogator/TargeterGraphResultCollection>
     ThirdBodyFunction<astrogator/ThirdBodyFunction>
     Thruster<astrogator/Thruster>
     ThrusterSet<astrogator/ThrusterSet>
     ThrusterSetCollection<astrogator/ThrusterSetCollection>
     TwoBodyFunction<astrogator/TwoBodyFunction>
     UserVariable<astrogator/UserVariable>
     UserVariableCollection<astrogator/UserVariableCollection>
     UserVariableDefinition<astrogator/UserVariableDefinition>
     UserVariableDefinitionCollection<astrogator/UserVariableDefinitionCollection>
     UserVariableUpdate<astrogator/UserVariableUpdate>
     UserVariableUpdateCollection<astrogator/UserVariableUpdateCollection>
     USStandardAtmosphere<astrogator/USStandardAtmosphere>
     VenusGRAM2005<astrogator/VenusGRAM2005>
     YarkovskyFunc<astrogator/YarkovskyFunc>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ AccessCriterion<astrogator/AccessCriterion>
    ≔ AscentType<astrogator/AscentType>
    ≔ AtmosphereDataSource<astrogator/AtmosphereDataSource>
    ≔ AttitudeControl<astrogator/AttitudeControl>
    ≔ AttitudeUpdate<astrogator/AttitudeUpdate>
    ≔ BaseSelection<astrogator/BaseSelection>
    ≔ BodyAxis<astrogator/BodyAxis>
    ≔ BurnoutOptions<astrogator/BurnoutOptions>
    ≔ BurnoutType<astrogator/BurnoutType>
    ≔ CalculationObjectAngleSign<astrogator/CalculationObjectAngleSign>
    ≔ CalculationObjectCentralBodyReference<astrogator/CalculationObjectCentralBodyReference>
    ≔ CalculationObjectDirection<astrogator/CalculationObjectDirection>
    ≔ CalculationObjectElement<astrogator/CalculationObjectElement>
    ≔ CalculationObjectLocationSource<astrogator/CalculationObjectLocationSource>
    ≔ CalculationObjectOrbitPlaneSource<astrogator/CalculationObjectOrbitPlaneSource>
    ≔ CalculationObjectReference<astrogator/CalculationObjectReference>
    ≔ CalculationObjectReferenceDirection<astrogator/CalculationObjectReferenceDirection>
    ≔ CalculationObjectReferenceEllipse<astrogator/CalculationObjectReferenceEllipse>
    ≔ CalculationObjectRelativePosition<astrogator/CalculationObjectRelativePosition>
    ≔ CalculationObjectSunPosition<astrogator/CalculationObjectSunPosition>
    ≔ CentralBodyAttitude<astrogator/CentralBodyAttitude>
    ≔ CentralBodyEphemeris<astrogator/CentralBodyEphemeris>
    ≔ CentralBodyGravityModel<astrogator/CentralBodyGravityModel>
    ≔ CentralBodyShape<astrogator/CentralBodyShape>
    ≔ ClearEphemerisDirection<astrogator/ClearEphemerisDirection>
    ≔ CoeffRungeKuttaV8th9th<astrogator/CoeffRungeKuttaV8th9th>
    ≔ ComplexNumber<astrogator/ComplexNumber>
    ≔ ConstraintSign<astrogator/ConstraintSign>
    ≔ ControlAdvanced<astrogator/ControlAdvanced>
    ≔ ControlEngineConstant<astrogator/ControlEngineConstant>
    ≔ ControlEngineConstantAcceleration<astrogator/ControlEngineConstantAcceleration>
    ≔ ControlEngineCustom<astrogator/ControlEngineCustom>
    ≔ ControlEngineIon<astrogator/ControlEngineIon>
    ≔ ControlEngineModelPolynomial<astrogator/ControlEngineModelPolynomial>
    ≔ ControlEngineThrottleTable<astrogator/ControlEngineThrottleTable>
    ≔ ControlFollow<astrogator/ControlFollow>
    ≔ ControlInitState<astrogator/ControlInitState>
    ≔ ControlLaunch<astrogator/ControlLaunch>
    ≔ ControlManeuver<astrogator/ControlManeuver>
    ≔ ControlOrbitStateValue<astrogator/ControlOrbitStateValue>
    ≔ ControlPowerInternal<astrogator/ControlPowerInternal>
    ≔ ControlPowerProcessed<astrogator/ControlPowerProcessed>
    ≔ ControlPowerSolarArray<astrogator/ControlPowerSolarArray>
    ≔ ControlRepeatingGroundTrackErr<astrogator/ControlRepeatingGroundTrackErr>
    ≔ ControlStoppingCondition<astrogator/ControlStoppingCondition>
    ≔ ControlThrusters<astrogator/ControlThrusters>
    ≔ ControlUpdate<astrogator/ControlUpdate>
    ≔ ConvergenceCriteria<astrogator/ConvergenceCriteria>
    ≔ Criteria<astrogator/Criteria>
    ≔ Criterion<astrogator/Criterion>
    ≔ CustomFunction<astrogator/CustomFunction>
    ≔ DerivativeCalculationMethod<astrogator/DerivativeCalculationMethod>
    ≔ DifferenceOrder<astrogator/DifferenceOrder>
    ≔ DifferentialCorrectorScalingMethod<astrogator/DifferentialCorrectorScalingMethod>
    ≔ DragModelType<astrogator/DragModelType>
    ≔ DrawPerturbation<astrogator/DrawPerturbation>
    ≔ EclipsingBodiesSource<astrogator/EclipsingBodiesSource>
    ≔ ElementSetType<astrogator/ElementSetType>
    ≔ ElementType<astrogator/ElementType>
    ≔ EngineModelFunction<astrogator/EngineModelFunction>
    ≔ EphemerisSource<astrogator/EphemerisSource>
    ≔ ErrorControl<astrogator/ErrorControl>
    ≔ FollowJoin<astrogator/FollowJoin>
    ≔ FollowSeparation<astrogator/FollowSeparation>
    ≔ FollowSpacecraftAndFuelTank<astrogator/FollowSpacecraftAndFuelTank>
    ≔ Formulation<astrogator/Formulation>
    ≔ GeoMagneticFluxSource<astrogator/GeoMagneticFluxSource>
    ≔ GeoMagneticFluxUpdateRate<astrogator/GeoMagneticFluxUpdateRate>
    ≔ GeoStationaryDriftRateModel<astrogator/GeoStationaryDriftRateModel>
    ≔ GeoStationaryInclinationMagnitude<astrogator/GeoStationaryInclinationMagnitude>
    ≔ GoldenSectionDesiredOperation<astrogator/GoldenSectionDesiredOperation>
    ≔ GraphOption<astrogator/GraphOption>
    ≔ GravitationalParameterSource<astrogator/GravitationalParameterSource>
    ≔ GravityCoefficientNormalizationType<astrogator/GravityCoefficientNormalizationType>
    ≔ GravityCoefficientType<astrogator/GravityCoefficientType>
    ≔ GravParamSource<astrogator/GravParamSource>
    ≔ GridSearchDesiredOperation<astrogator/GridSearchDesiredOperation>
    ≔ IdealOrbitRadius<astrogator/IdealOrbitRadius>
    ≔ ImpulsiveDeltaVRepresentation<astrogator/ImpulsiveDeltaVRepresentation>
    ≔ IPOPTGoal<astrogator/IPOPTGoal>
    ≔ LambertDirectionOfMotionType<astrogator/LambertDirectionOfMotionType>
    ≔ LambertOrbitalEnergyType<astrogator/LambertOrbitalEnergyType>
    ≔ LambertSolutionOptionType<astrogator/LambertSolutionOptionType>
    ≔ LambertTargetCoordinateType<astrogator/LambertTargetCoordinateType>
    ≔ Language<astrogator/Language>
    ≔ LaunchDisplaySystem<astrogator/LaunchDisplaySystem>
    ≔ LightingCondition<astrogator/LightingCondition>
    ≔ ManeuverType<astrogator/ManeuverType>
    ≔ MarsGRAMDensityType<astrogator/MarsGRAMDensityType>
    ≔ NumericalIntegrator<astrogator/NumericalIntegrator>
    ≔ OptimalFiniteDiscretizationStrategy<astrogator/OptimalFiniteDiscretizationStrategy>
    ≔ OptimalFiniteExportNodesFormat<astrogator/OptimalFiniteExportNodesFormat>
    ≔ OptimalFiniteGuessMethod<astrogator/OptimalFiniteGuessMethod>
    ≔ OptimalFiniteRunMode<astrogator/OptimalFiniteRunMode>
    ≔ OptimalFiniteScalingOptions<astrogator/OptimalFiniteScalingOptions>
    ≔ OptimalFiniteSeedMethod<astrogator/OptimalFiniteSeedMethod>
    ≔ OptimalFiniteSNOPTObjective<astrogator/OptimalFiniteSNOPTObjective>
    ≔ OptimalFiniteSNOPTScaling<astrogator/OptimalFiniteSNOPTScaling>
    ≔ OptimalFiniteWorkingVariables<astrogator/OptimalFiniteWorkingVariables>
    ≔ PredictorCorrector<astrogator/PredictorCorrector>
    ≔ PressureMode<astrogator/PressureMode>
    ≔ Profile<astrogator/Profile>
    ≔ ProfileInsertDirection<astrogator/ProfileInsertDirection>
    ≔ ProfileMode<astrogator/ProfileMode>
    ≔ ProfilesFinish<astrogator/ProfilesFinish>
    ≔ PropulsionMethod<astrogator/PropulsionMethod>
    ≔ ReferenceRadiusSource<astrogator/ReferenceRadiusSource>
    ≔ ReturnControl<astrogator/ReturnControl>
    ≔ RootFindingAlgorithm<astrogator/RootFindingAlgorithm>
    ≔ RotatingCoordinateSystem<astrogator/RotatingCoordinateSystem>
    ≔ RunCode<astrogator/RunCode>
    ≔ ScriptingParameterType<astrogator/ScriptingParameterType>
    ≔ SegmentDifferenceOrder<astrogator/SegmentDifferenceOrder>
    ≔ SegmentState<astrogator/SegmentState>
    ≔ SegmentType<astrogator/SegmentType>
    ≔ SequenceStateToPass<astrogator/SequenceStateToPass>
    ≔ ShadowModel<astrogator/ShadowModel>
    ≔ SmartRunMode<astrogator/SmartRunMode>
    ≔ SNOPTGoal<astrogator/SNOPTGoal>
    ≔ SolarForceMethod<astrogator/SolarForceMethod>
    ≔ SquaredType<astrogator/SquaredType>
    ≔ StateType<astrogator/StateType>
    ≔ STMEigenNumber<astrogator/STMEigenNumber>
    ≔ STMPerturbationVariables<astrogator/STMPerturbationVariables>
    ≔ StoppingConditionType<astrogator/StoppingConditionType>
    ≔ SunPosition<astrogator/SunPosition>
    ≔ TabVecInterpolationMethod<astrogator/TabVecInterpolationMethod>
    ≔ TargetSequenceAction<astrogator/TargetSequenceAction>
    ≔ ThirdBodyMode<astrogator/ThirdBodyMode>
    ≔ ThrottleTableOperationMode<astrogator/ThrottleTableOperationMode>
    ≔ ThrusterDirection<astrogator/ThrusterDirection>
    ≔ ThrustType<astrogator/ThrustType>
    ≔ UpdateAction<astrogator/UpdateAction>
    ≔ UpdateParam<astrogator/UpdateParam>
    ≔ VenusGRAMDensityType<astrogator/VenusGRAMDensityType>

