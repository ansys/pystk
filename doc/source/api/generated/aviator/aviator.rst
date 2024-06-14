
The ``AgStkAvtrLib`` module
===========================


.. py::module:: ansys.stk.core.stkobjects.aviator


Summary
-------

.. tab-set::
    .. tab-items:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~ISite`
              - Interface to access Site options.

            * - :pyclass:`~IWindModel`
              - Interface used to access the wind model for a mission, scenario, or procedure.

            * - :pyclass:`~IADDSMessage`
              - Interface used to access a message from the NOAA ADDS forecast.

            * - :pyclass:`~IFuelTankInternal`
              - Interface used to set an aircraft's internal fuel tank.

            * - :pyclass:`~IFuelTankExternal`
              - Interface used to set an aircraft's external fuel tank.

            * - :pyclass:`~IPayloadStation`
              - Interface used to set an aircraft's payload station.

            * - :pyclass:`~IAircraftModel`
              - Interface used to access the aircraft options in the Aviator catalog.

            * - :pyclass:`~IAircraftSimpleAero`
              - Interface used to access the Simple Aerodynamics options for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~ILevelTurns`
              - Interface used to access the Level Turns Transitions options found in the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAttitudeTransitions`
              - Interface used to access the Attitude Transitions options found in the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IClimbAndDescentTransitions`
              - Interface used to access the Climb and Descent Transitions options found in the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~ICatalogItem`
              - Interface used to access the options for a Catalog Item in the Aviator Catalog. Use this interface to Create, Remove, Duplicate, or Rename items in the catalog.

            * - :pyclass:`~IAircraftBasicClimbModel`
              - Interface used to access the basic climb model options for a climb model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftBasicAccelerationModel`
              - Interface used to access the basic acceleration model options for an acceleration model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftCategory`
              - Interface used to access the Aircraft Category in the Aviator Catalog.

            * - :pyclass:`~IRunwayCategory`
              - Interface used to access runways in the Aviator catalog.

            * - :pyclass:`~IBasicManeuverStrategy`
              - Interface used to access options for a Basic Maneuver Strategy.

            * - :pyclass:`~IAircraftVTOL`
              - Interface used to access the VTOL options for an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftExternalAero`
              - Interface used to access the External File Aerodynamics options for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftSimpleProp`
              - Interface used to access the Simple Propulsion options for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftExternalProp`
              - Interface used to access the External File Propulsion options for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftBasicFixedWingProp`
              - Interface used to access the Basic Fixed Wing Propulsion options for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftAdvancedClimbModel`
              - Interface used to access the advanced climb model options for a climb model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftBasicCruiseModel`
              - Interface used to access the basic cruise model options for a cruise model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftAdvancedCruiseModel`
              - Interface used to access the advanced cruise model options for a cruise model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftBasicDescentModel`
              - Interface used to access the basic descent model options for a descent model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftAdvancedDescentModel`
              - Interface used to access the advanced descent model options for a descent model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftBasicLandingModel`
              - Interface used to access the basic landing model options for a landing model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftAdvancedLandingModel`
              - Interface used to access the advanced landing model options for a landing model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftBasicTakeoffModel`
              - Interface used to access the basic takeoff model options for a takeoff model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftAdvancedTakeoffModel`
              - Interface used to access the advanced takeoff model options for a takeoff model of an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftVTOLModel`
              - Interface used to access the options for a VTOL performance model of an aircraft.

            * - :pyclass:`~IAircraftTerrainFollow`
              - Interface used to access the TerrainFollow options for an aircraft in the Aviator catalog.

            * - :pyclass:`~IPerformanceModelOptions`
              - Interface used to change the active performance model in a phase for a given model type.

            * - :pyclass:`~IAdvancedFixedWingTool`
              - Interface used to access the options for the Advanced Fixed Wing Tool of an aircraft.

            * - :pyclass:`~IAdvancedFixedWingExternalAero`
              - Interface used to access the options for an external file aerodynamic strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingSubsonicAero`
              - Interface used to access the options for the subsonic aerodynamic strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingSubSuperHypersonicAero`
              - Interface used to access the options for the Sub/Super/Hypersonic aerodynamic strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingSubSuperHypersonicProp`
              - Interface used to access the options for the Sub/Super/Hypersonic powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingSupersonicAero`
              - Interface used to access the options for the supersonic aerodynamic strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingGeometryBasic`
              - Interface used to access the options for a basic geometry wing in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingGeometryVariable`
              - Interface used to access the options for a variable geometry wing in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingElectricPowerplant`
              - Interface used to access the options for the Electric powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingExternalProp`
              - Interface used to access the options for the External Prop File powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingPistonPowerplant`
              - Interface used to access the options for the Piston powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingTurbopropPowerplant`
              - Interface used to access the options for the Turboprop powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingEmpiricalJetEngine`
              - Interface used to access the options for the Sub/Super/Hypersonic powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingTurbojetBasicABProp`
              - Interface used to access the options for the Turbojet - Basic w/AB (Thermodynamic) powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingTurbofanBasicABProp`
              - Interface used to access the options for the Turbofan - Basic w/AB (Thermodynamic) powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~IAviatorVehicle`
              - Interface for a vehicle in Aviator.

            * - :pyclass:`~IMissileModel`
              - Interface used to access the missile options in the Aviator catalog.

            * - :pyclass:`~IMissileAero`
              - Interface used to access the aerodynamics options for a missile.

            * - :pyclass:`~IMissileProp`
              - Interface used to access the Propulsion options for a missile.

            * - :pyclass:`~IMissileSimpleAero`
              - Interface used to access the Simple aerodynamics options for a missile.

            * - :pyclass:`~IMissileSimpleProp`
              - Interface used to access the Simple propulsion options for a missile.

            * - :pyclass:`~IMissileExternalAero`
              - Interface used to access the External aerodynamics options for a missile.

            * - :pyclass:`~IMissileExternalProp`
              - Interface used to access the External Prop file options for a missile.

            * - :pyclass:`~IMissileAdvancedAero`
              - Interface used to access the Advanced aerodynamics options for a missile.

            * - :pyclass:`~IMissileRamjetProp`
              - Interface used to access the Ramjet propulsion options for a missile.

            * - :pyclass:`~IMissileRocketProp`
              - Interface used to access the Rocket propulsion options for a missile.

            * - :pyclass:`~IMissileTurbojetProp`
              - Interface used to access the Turbojet propulsion options for a missile.

            * - :pyclass:`~IRotorcraftModel`
              - Interface used to access the rotorcraft options in the Aviator catalog.

            * - :pyclass:`~IRotorcraftAero`
              - Interface used to access the aerodynamics options for a rotorcraft.

            * - :pyclass:`~IRotorcraftProp`
              - Interface used to access the Propulsion options for a rotorcraft.

            * - :pyclass:`~IUserRunwaySource`
              - Interface used to access the user runways in the Aviator catalog.

            * - :pyclass:`~IUserRunway`
              - Interface used to access a user runway in the Aviator catalog.

            * - :pyclass:`~IARINC424Item`
              - Interface used to access the options for an ARINC424 Item found in the Aviator catalog.

            * - :pyclass:`~IARINC424Source`
              - Interface used to access the options for any ARINC424 source in the Aviator catalog.

            * - :pyclass:`~IDAFIFSource`
              - Interface used to access the options for any DAFIF source in the Aviator catalog.

            * - :pyclass:`~IUserVTOLPoint`
              - Interface used to access a user VTOL Point in the Aviator catalog.

            * - :pyclass:`~IUserVTOLPointSource`
              - Interface used to access the user VTOL Points in the Aviator catalog.

            * - :pyclass:`~IUserWaypoint`
              - Interface used to access a user waypoint in the Aviator catalog.

            * - :pyclass:`~IUserWaypointSource`
              - Interface used to access the user waypoints in the Aviator catalog.

            * - :pyclass:`~IPropulsionEfficiencies`
              - Interface used to access the options for the Efficiencies and Losses of a jet engine powerplant in the advanced fixed wing tool.

            * - :pyclass:`~IFuelModelKeroseneAFPROP`
              - Interface used to access the options for Kerosense - CEA fuel for a thermodynamic a jet engine model.

            * - :pyclass:`~IFuelModelKeroseneCEA`
              - Interface used to access the options for Kerosense - CEA fuel for a thermodynamic a jet engine model.

            * - :pyclass:`~IAdvancedFixedWingRamjetBasic`
              - Interface used to access the options for a basic Ramjet mode.

            * - :pyclass:`~IAdvancedFixedWingScramjetBasic`
              - Interface used to access the options for a basic Scramjet mode.

            * - :pyclass:`~IRefuelDumpProperties`
              - Interface used to access the refuel/dump properties for the current procedure.

            * - :pyclass:`~IProcedureFastTimeOptions`
              - Interface used to access the fast time options (without error or constraint checks) for the current procedure. Use this interface to set an Interrupt Time or Fixed Duration for a procedure.

            * - :pyclass:`~IAtmosphereModelBasic`
              - Interface used to access the basic atmosphere model.

            * - :pyclass:`~IAtmosphereModel`
              - Interface used to access the atmosphere model for a mission, scenario, or procedure.

            * - :pyclass:`~IADDSMessageCollection`
              - Interface used to access the collection of messages from the NOAA ADDS forecast.

            * - :pyclass:`~IWindModelADDS`
              - Interface used to access the options for a NOAA ADDS wind model.

            * - :pyclass:`~IWindModelConstant`
              - Interface used to access the options for a Constant Bearing/Speed wind model.

            * - :pyclass:`~IStation`
              - Interface used to access a station for an Aviator aircraft.

            * - :pyclass:`~IStationCollection`
              - Interface used to access the list of stations for an Aviator aircraft.

            * - :pyclass:`~IConfiguration`
              - Interface used to change an aircraft's configuration for an Aviator mission.

            * - :pyclass:`~ICatalogSource`
              - Interface used to access options for a source in the Aviator Catalog. Examples of sources include User Aircraft Models, ARINC424runways, User Runways, etc.

            * - :pyclass:`~IAircraftModels`
              - Interface for the User Aircraft Models in the Aviator Catalog.

            * - :pyclass:`~IMissileModels`
              - Interface for the User Missile Models in the Aviator Catalog.

            * - :pyclass:`~IRotorcraftModels`
              - Interface for the User Rotorcraft Models in the Aviator Catalog.

            * - :pyclass:`~IBasicFixedWingLiftHelper`
              - Interface used to access Lift Coefficient Helper in the Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftBasicFixedWingAero`
              - Interface used to access Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftAero`
              - Interface used to access the Aerodynamics options for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftProp`
              - Interface used to access the propulsion options for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftAccelerationMode`
              - Interface used to set the Acceleration Mode for the Advanced Acceleration Model of an aircraft.

            * - :pyclass:`~IAircraftAdvancedAccelerationModel`
              - Interface used to access the Advanced Acceleration Model options of an aircraft.

            * - :pyclass:`~IAeroPropManeuverModeHelper`
              - Interface used to access the The calculation mode for the Aero/Prop maneuver mode helper. Helper found in the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~ICatalogRunway`
              - Interface used to access a runway in the Aviator catalog.

            * - :pyclass:`~ICatalogAirport`
              - Interface used to access a airport in the Aviator catalog.

            * - :pyclass:`~ICatalogNavaid`
              - Interface used to access a navaid in the Aviator catalog.

            * - :pyclass:`~ICatalogVTOLPoint`
              - Interface used to access a VTOL Point in the Aviator catalog.

            * - :pyclass:`~ICatalogWaypoint`
              - Interface used to access a waypoint in the Aviator catalog.

            * - :pyclass:`~IARINC424Airport`
              - Do not use this interface, as it is deprecated. Use IAgAvtrARINC424Item instead.

            * - :pyclass:`~IDAFIFItem`
              - Interface used to access the options for an DAFIF Item found in the Aviator catalog.

            * - :pyclass:`~IARINC424Runway`
              - Do not use this interface, as it is deprecated. Use IAgAvtrARINC424Item instead.

            * - :pyclass:`~IAirportCategory`
              - Interface used to access the airports in the Aviator catalog.

            * - :pyclass:`~INavaidCategory`
              - Interface used to access the navaids in the Aviator catalog.

            * - :pyclass:`~IVTOLPointCategory`
              - Interface used to access the VTOL Points in the Aviator catalog.

            * - :pyclass:`~IWaypointCategory`
              - Interface used to access the waypoints in the Aviator catalog.

            * - :pyclass:`~IAircraftClimb`
              - Interface used to access the climb options for an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftCruise`
              - Interface used to access the cruise options for an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftDescent`
              - Interface used to access the descent options for an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftLanding`
              - Interface used to access the landing options for an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftTakeoff`
              - Interface used to access the takeoff options for an aircraft in the Aviator catalog.

            * - :pyclass:`~IAircraftAcceleration`
              - Interface used to access the acceleration options for an aircraft in the Aviator catalog.

            * - :pyclass:`~ICatalog`
              - Interface used to access the Aviator catalog.

            * - :pyclass:`~IProcedureTimeOptions`
              - Interface used to access the time options for the current procedure. Use this interface to set an Interrupt Time or Fixed Duration for a procedure.

            * - :pyclass:`~ICalculationOptions`
              - Interface used to access the calculation options for a procedure or phase.

            * - :pyclass:`~INavigationOptions`
              - Interface used to access the navigation options for an Aviator procedure.

            * - :pyclass:`~IAltitudeMSLAndLevelOffOptions`
              - Interface used to access the altitude MSL and Level off options for an Aviator procedure.

            * - :pyclass:`~IAltitudeMSLOptions`
              - Interface used to access the altitude MSL options for an Aviator procedure.

            * - :pyclass:`~IAltitudeOptions`
              - Interface used to access the altitude options for an Aviator procedure.

            * - :pyclass:`~IHoverAltitudeOptions`
              - Interface used to access the altitude options for VTOL procedure.

            * - :pyclass:`~IArcAltitudeOptions`
              - Interface used to access the altitude options for an Arc procedure.

            * - :pyclass:`~IArcAltitudeAndDelayOptions`
              - Interface used to access the altitude options for an Arc procedure.

            * - :pyclass:`~IArcOptions`
              - Interface used to access the arc options for a procedure.

            * - :pyclass:`~IVerticalPlaneOptions`
              - Interface used to access the Vertical Plane options for an Aviator procedure.

            * - :pyclass:`~IVerticalPlaneAndFlightPathOptions`
              - Interface used to access the Vertical Plane and Final Flight Path Angle options for an Aviator procedure.

            * - :pyclass:`~IArcVerticalPlaneOptions`
              - Interface used to access the Vertical Plane options for an arc procedure.

            * - :pyclass:`~IEnrouteOptions`
              - Interface used to access the Enroute options for an Aviator procedure.

            * - :pyclass:`~IEnrouteAndDelayOptions`
              - Interface used to access the Enroute options for an Aviator procedure.

            * - :pyclass:`~IEnrouteTurnDirectionOptions`
              - Interface used to access the Enroute Turn Direction options for an Aviator procedure.

            * - :pyclass:`~ICruiseAirspeedOptions`
              - Interface used to access the Cruise Airspeed options for an Aviator procedure.

            * - :pyclass:`~ICruiseAirspeedProfile`
              - Interface used to access the Cruise Profile options for an Aviator procedure.

            * - :pyclass:`~ICruiseAirspeedAndProfileOptions`
              - Interface used to access the cruise airspeed options that also include a profile field.

            * - :pyclass:`~IAutomationStrategyFactory`
              - Interface used to send connect commands to Aviator objects.

            * - :pyclass:`~IConnect`
              - Interface used to send connect commands to Aviator objects.

            * - :pyclass:`~IRunwayHeadingOptions`
              - Interface for the Runway Heading Options found in a Takeoff or Landing procedure.

            * - :pyclass:`~IProcedure`
              - Interface used to access the options for a procedure. Use this interface to get the Site and Get the time options for the current procedure.

            * - :pyclass:`~IProcedureCollection`
              - Interface used to access the collection of procedures for a given phase in a mission. Use this interface to Get, Add, or Remove a procedure.

            * - :pyclass:`~IPhase`
              - Interface used to access the phase options for a mission.

            * - :pyclass:`~IPhaseCollection`
              - Interface used to access the collection of phases for a mission.

            * - :pyclass:`~IMission`
              - Interface for the mission of an aircraft using the Aviator propagator.

            * - :pyclass:`~IAviatorPropagator`
              - Interface used to access the Aviator interface for an aircraft. Use this interface to get the mission or Aviator catalog.

            * - :pyclass:`~IPerformanceModel`
              - Interface for a performance model of an Aviator vehicle.

            * - :pyclass:`~IAdvancedFixedWingGeometry`
              - Interface used to access the options for the wing geometry in the advanced fixed wing tool.

            * - :pyclass:`~IAdvancedFixedWingTurbofanBasicABPowerplant`
              - Do not use this interface, as it is deprecated. Use IAgAvtrAdvFixedWingTurbofanBasicABProp instead.

            * - :pyclass:`~IAdvancedFixedWingTurbojetBasicABPowerplant`
              - Do not use this interface, as it is deprecated. Use IAgAvtrAdvFixedWingTurbojetBasicABProp instead.

            * - :pyclass:`~IAdvancedFixedWingPowerplant`
              - Interface for a powerplant strategy in the advanced fixed wing tool.

            * - :pyclass:`~ISiteUnknown`
              - Interface of an unknown site.

            * - :pyclass:`~IAircraftTerrainFollowModel`
              - Interface used to access the options for a TerrainFollow performance model of an aircraft.

            * - :pyclass:`~IBasicManeuverTargetPositionVel`
              - Interface used to access target position and velocity strategies for basic maneuvers.

            * - :pyclass:`~IPropulsionThrust`
              - Interface used to access propulsion thrust for basic maneuver strategies.

            * - :pyclass:`~IBasicManeuverAirspeedOptions`
              - Interface used to access airspeed options for basic maneuver strategies.

            * - :pyclass:`~IBasicManeuverStrategyAileronRoll`
              - Interface used to access options for a Aileron Roll Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyAutopilotNav`
              - Interface used to access options for the Autopilot - Horizontal Plane Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyAutopilotProf`
              - Interface used to access options for the Autopilot - Vertical Plane Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyBarrelRoll`
              - Interface used to access options for a Barrel Roll Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyLoop`
              - Interface used to access options for a Loop Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyLTAHover`
              - Interface used to access options for a Lighter than Air Hover Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyFlyAOA`
              - Interface used to access options for a Fly AOA Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyPull`
              - Interface used to access options for a Pull Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyRollingPull`
              - Interface used to access options for a Rolling Pull Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategySmoothAccel`
              - Interface used to access options for a Smooth Accel Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategySmoothTurn`
              - Interface used to access options for a Smooth Turn Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategySimpleTurn`
              - Interface used to access options for a Simple Turn Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyIntercept`
              - Interface used to access options for an Intercept Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyRelativeBearing`
              - Interface used to access options for a Relative Bearing Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyRelativeCourse`
              - Interface used to access options for a Relative Course Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyRendezvous`
              - Interface used to access options for a Rendezvous Formation Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyStationkeeping`
              - Interface used to access options for a Stationkeeping Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyRelativeFPA`
              - Interface used to access options for the Relative Flight Path Angle Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyRelSpeedAltitude`
              - Interface used to access options for a Relative Speed/Altitude Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyBezier`
              - Interface used to access options for a Bezier Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyPushPull`
              - Interface used to access options for a Push/Pull Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyGlideProfile`
              - Interface used to access options for a Glide Profile Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyCruiseProfile`
              - Interface used to access options for a Cruise Profile Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyStraightAhead`
              - Interface used to access options for a Straight Ahead Strategy of a Basic Maneuver Procedure.

            * - :pyclass:`~IBasicManeuverStrategyWeave`
              - Interface used to access options for a weave strategy of a basic maneuver procedure.

            * - :pyclass:`~IBasicManeuverStrategyBallistic3D`
              - Interface used to access options for a balistic 3D strategy of a basic maneuver procedure.

            * - :pyclass:`~IBasicManeuverStrategyPitch3D`
              - Interface used to access options for a pitch 3D strategy of a basic maneuver procedure.

            * - :pyclass:`~IBasicManeuverTargetPositionVelNoisyBrgRng`
              - Interface used to access target position and velocity strategy, NoisyBrnRng.

            * - :pyclass:`~IBasicManeuverTargetPositionVelNoisySurfTgt`
              - Interface used to access target position and velocity strategy, Surf Tgt Pos Vel.

            * - :pyclass:`~ITakeoffNormal`
              - The interface used to access the options for a Normal takeoff mode. The mode must be set to Normal to access this interface.

            * - :pyclass:`~ITakeoffDeparturePoint`
              - The interface used to access the options for a Departure Point takeoff mode. The mode must be set to Departure Point to access this interface.

            * - :pyclass:`~ITakeoffLowTransition`
              - The interface used to access the options for a Low Transition takeoff mode. The mode must be set to Low Transition to access this interface.

            * - :pyclass:`~IReferenceStateForwardFlightOptions`
              - Interface used to access the forward flight options for a reference state procedure.

            * - :pyclass:`~IReferenceStateHoverOptions`
              - Interface used to access the hover options for a reference state procedure.

            * - :pyclass:`~IReferenceStateWeightOnWheelsOptions`
              - Interface used to access the weight on wheels options for a reference state procedure.

            * - :pyclass:`~IReferenceStateTakeoffLandingOptions`
              - Interface used to access the takeoff or landing options for a reference state procedure.

            * - :pyclass:`~ILandingEnterDownwindPattern`
              - The interface used to access the options for a Downwind Pattern approach mode for a landing procedure. The approach mode must be set to Downwind Pattern to access this interface.

            * - :pyclass:`~ILandingInterceptGlideslope`
              - The interface used to access the options for an Intercept Glideslope approach mode for a landing procedure. The approach mode must be set to Intercept Glideslope to access this interface.

            * - :pyclass:`~ILandingStandardInstrumentApproach`
              - The interface used to access the options for a Standard Instrument Approach mode for a landing procedure. The approach mode must be set to Standard Instrument Approach to access this interface.

            * - :pyclass:`~IProcedureBasicManeuver`
              - Interface used to access the options for a Basic Maneuver procedure.

            * - :pyclass:`~ISiteWaypoint`
              - Interface used to access the options for a waypoint site.

            * - :pyclass:`~ISiteEndOfPrevProcedure`
              - Interface used to access the options for an End of Previous Procedure site type.

            * - :pyclass:`~ISiteVTOLPoint`
              - Interface used to access the options for a VTOL Point site.

            * - :pyclass:`~ISiteSTKVehicle`
              - Interface used to access the options for a STK Vehicle site.

            * - :pyclass:`~ISiteReferenceState`
              - Interface used to access the options for a Reference State site.

            * - :pyclass:`~ISiteSuperProcedure`
              - Interface used to access the options for a Super Procedure site.

            * - :pyclass:`~ISiteRelToPrevProcedure`
              - Interface used to access the options for a Relative to Previous Procedure site.

            * - :pyclass:`~ISiteSTKObjectWaypoint`
              - Interface used to access the options for a STK Object Waypoint site.

            * - :pyclass:`~ISiteSTKStaticObject`
              - Interface used to access the options for a STK Static Object site.

            * - :pyclass:`~ISiteRelToSTKObject`
              - Interface used to access the options for a Relative to Stationary STK Object site.

            * - :pyclass:`~ISiteSTKAreaTarget`
              - Interface used to access the options for a STK Area Target site.

            * - :pyclass:`~ISiteRunway`
              - Interface used to access the options for a Runway site type.

            * - :pyclass:`~IProcedureLanding`
              - Interface used to access the options for a landing procedure.

            * - :pyclass:`~IProcedureEnroute`
              - Interface used to access the options for an enroute procedure.

            * - :pyclass:`~IProcedureExtEphem`
              - Interface used to access the options for an ExtEphem procedure.

            * - :pyclass:`~IProcedureFormationFlyer`
              - Interface used to access the options for an enroute procedure.

            * - :pyclass:`~IProcedureBasicPointToPoint`
              - Interface used to access the options for a basic point to point procedure.

            * - :pyclass:`~IProcedureDelay`
              - Interface used to access the options for a delay procedure.

            * - :pyclass:`~IProcedureTakeoff`
              - Interface used to access the options for a takeoff procedure.

            * - :pyclass:`~IProcedureArcEnroute`
              - Interface used to access the options for an arc enroute procedure.

            * - :pyclass:`~IProcedureArcPointToPoint`
              - Interface used to access the options for an arc point to point procedure.

            * - :pyclass:`~IProcedureFlightLine`
              - Interface used to access the options for a flight line procedure.

            * - :pyclass:`~IProcedureHoldingCircular`
              - Interface used to access the options for a holding circular procedure.

            * - :pyclass:`~IProcedureHoldingFigure8`
              - Interface used to access the options for a holding figure 8 procedure.

            * - :pyclass:`~IProcedureHoldingRacetrack`
              - Interface used to access the options for a holding racetrack procedure.

            * - :pyclass:`~IProcedureTransitionToHover`
              - Interface used to access the options for a transition to hover procedure.

            * - :pyclass:`~IProcedureTerrainFollow`
              - Interface used to access the options for a terrain following procedure.

            * - :pyclass:`~IProcedureHover`
              - Interface used to access the options for a hover procedure.

            * - :pyclass:`~IProcedureHoverTranslate`
              - Interface used to access the options for a hover translate procedure.

            * - :pyclass:`~IProcedureTransitionToForwardFlight`
              - Interface used to access the options for a transition to forward flight procedure.

            * - :pyclass:`~IProcedureVerticalTakeoff`
              - Interface used to access the options for a vertical takeoff procedure.

            * - :pyclass:`~IProcedureVerticalLanding`
              - Interface used to access the options for a vertical landing procedure.

            * - :pyclass:`~IProcedureReferenceState`
              - Interface used to access the options for a reference state procedure.

            * - :pyclass:`~IProcedureSuperProcedure`
              - Interface used to access the options for a super procedure.

            * - :pyclass:`~IProcedureLaunch`
              - Interface used to access the options for a launch procedure.

            * - :pyclass:`~IProcedureAirway`
              - Interface used to access the options for an Airway procedure.

            * - :pyclass:`~IProcedureAirwayRouter`
              - Interface used to access the options for an Airway Router procedure.

            * - :pyclass:`~IProcedureAreaTargetSearch`
              - Interface used to access the options for an Area Target Search procedure.

            * - :pyclass:`~IProcedureFormationRecover`
              - Interface used to access the options for a Formation Recover procedure.

            * - :pyclass:`~IProcedureInFormation`
              - Interface used to access the options for an In Formation procedure.

            * - :pyclass:`~IProcedureParallelFlightLine`
              - Interface used to access the options for a Parallel Flight Line procedure.

            * - :pyclass:`~IProcedureVGTPoint`
              - Interface used to access the options for a VGT Point procedure.

            * - :pyclass:`~ISiteRunwayFromCatalog`
              - Interface used to access the options for a Runway From Catalog site type.

            * - :pyclass:`~ISiteAirportFromCatalog`
              - Interface used to access the options for a airport From Catalog site type.

            * - :pyclass:`~ISiteNavaidFromCatalog`
              - Interface used to access the options for a navaid From Catalog site type.

            * - :pyclass:`~ISiteVTOLPointFromCatalog`
              - Interface used to access the options for a VTOL Point From Catalog site type.

            * - :pyclass:`~ISiteWaypointFromCatalog`
              - Interface used to access the options for a waypoint From Catalog site type.

            * - :pyclass:`~IProcedureLaunchDynState`
              - Interface used to access the options for a dyn state launch procedure.

            * - :pyclass:`~IProcedureLaunchWaypoint`
              - Interface used to access the options for a waypoint launch procedure.

            * - :pyclass:`~ISiteDynState`
              - Interface used to access the options for a dyn state site type.

    
    .. tab-items:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~SiteWaypoint`
              - Class defining a waypoint site.

            * - :pyclass:`~SiteEndOfPrevProcedure`
              - Class defining an End of Previous Procedure site.

            * - :pyclass:`~SiteVTOLPoint`
              - Class defining a VTOL Point site.

            * - :pyclass:`~SiteReferenceState`
              - Class defining a Reference State site.

            * - :pyclass:`~SiteSTKVehicle`
              - Class defining a STK Vehicle site.

            * - :pyclass:`~SiteSuperProcedure`
              - Class defining a Super Procedure site.

            * - :pyclass:`~SiteRelToPrevProcedure`
              - Class defining a Relative to Previous Procedure site.

            * - :pyclass:`~SiteSTKObjectWaypoint`
              - Class defining a STK Object Waypoint site.

            * - :pyclass:`~SiteSTKStaticObject`
              - Class defining a STK Static Object site.

            * - :pyclass:`~SiteRelToSTKObject`
              - Class defining a Relative to Stationary STK Object site.

            * - :pyclass:`~SiteSTKAreaTarget`
              - Class defining a STK Area Target site.

            * - :pyclass:`~SiteRunway`
              - Class defining a runway site.

            * - :pyclass:`~Site`
              - Class defining an unknown site type.

            * - :pyclass:`~ProcedureLanding`
              - Class defining a landing procedure.

            * - :pyclass:`~ProcedureEnroute`
              - Class defining an enroute procedure.

            * - :pyclass:`~ProcedureExtEphem`
              - Class defining an ExtEphem procedure.

            * - :pyclass:`~ProcedureFormationFlyer`
              - Class defining an formationflyer procedure.

            * - :pyclass:`~ProcedureBasicPointToPoint`
              - Class defining a basic point to point procedure.

            * - :pyclass:`~ProcedureArcEnroute`
              - Class defining a arc enroute procedure.

            * - :pyclass:`~ProcedureArcPointToPoint`
              - Class defining a arc point to point procedure.

            * - :pyclass:`~ProcedureFlightLine`
              - Class defining a flight line procedure.

            * - :pyclass:`~ProcedureDelay`
              - Class defining a delay procedure.

            * - :pyclass:`~ProcedureTakeoff`
              - Class defining a takeoff procedure.

            * - :pyclass:`~ProcedureCollection`
              - Class defining the collection of procedures in the phase of an Aviator mission.

            * - :pyclass:`~Phase`
              - Class defining a phase in an Aviator mission.

            * - :pyclass:`~PhaseCollection`
              - Class defining the collection of phases.

            * - :pyclass:`~Mission`
              - Class defining the Aviator mission.

            * - :pyclass:`~AviatorPropagator`
              - Class defining the Aviator propagator.

            * - :pyclass:`~ProcedureBasicManeuver`
              - Class defining a Basic Maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyWeave`
              - Class defining Weave strategy for a Basic Maneuver procedure.

            * - :pyclass:`~ProcedureTimeOptions`
              - Class defining the time options for the current procedure.

            * - :pyclass:`~CalculationOptions`
              - Class defining the calculation options for a procedure or phase.

            * - :pyclass:`~AircraftCategory`
              - Class defining the aircraft category in the Aviator catalog.

            * - :pyclass:`~Catalog`
              - Class defining the Aviator Catalog.

            * - :pyclass:`~AircraftModel`
              - Class defining an aircraft in Aviator.

            * - :pyclass:`~MissileModel`
              - Class defining a missile in Aviator.

            * - :pyclass:`~RotorcraftModel`
              - Class defining a rotorcraft in Aviator.

            * - :pyclass:`~RotorcraftAero`
              - Class defining the aerodynamic options for a rotorcraft.

            * - :pyclass:`~RotorcraftProp`
              - Class defining the propulsion options for a rotorcraft.

            * - :pyclass:`~AircraftAcceleration`
              - Class defining the aircraft acceleration category of an Aviator aircraft.

            * - :pyclass:`~AircraftBasicAccelerationModel`
              - Class defining the basic acceleration performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftClimb`
              - Class defining the aircraft climb category of an Aviator aircraft.

            * - :pyclass:`~AircraftCruise`
              - Class defining the aircraft cruise category of an Aviator aircraft.

            * - :pyclass:`~AircraftDescent`
              - Class defining the aircraft descent category of an Aviator aircraft.

            * - :pyclass:`~AircraftLanding`
              - Class defining the aircraft landing category of an Aviator aircraft.

            * - :pyclass:`~AircraftTakeoff`
              - Class defining the aircraft takeoff category of an Aviator aircraft.

            * - :pyclass:`~AircraftBasicClimbModel`
              - Class defining the basic climb performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftAdvancedClimbModel`
              - Class defining the advanced climb performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftBasicCruiseModel`
              - Class defining the basic cruise performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftAdvancedCruiseModel`
              - Class defining the advanced cruise performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftBasicDescentModel`
              - Class defining the basic descent performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftAdvancedDescentModel`
              - Class defining the advanced descent performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftBasicTakeoffModel`
              - Class defining the basic takeoff performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftAdvancedTakeoffModel`
              - Class defining the advanced takeoff performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftBasicLandingModel`
              - Class defining the basic landing performance model for an Aviator aircraft.

            * - :pyclass:`~AircraftAdvancedLandingModel`
              - Class defining the advanced landing performance model for an Aviator aircraft.

            * - :pyclass:`~AirportCategory`
              - Class defining the airport category in the Aviator catalog.

            * - :pyclass:`~ARINC424Airport`
              - Class defining an ARINC424 Airport.

            * - :pyclass:`~ARINC424Runway`
              - Class defining an ARINC424 Runway.

            * - :pyclass:`~DAFIFRunway`
              - Class defining an DAFIF Runway.

            * - :pyclass:`~DAFIFHelipad`
              - Class defining an DAFIF Helipad.

            * - :pyclass:`~DAFIFWaypoint`
              - Class defining an DAFIF Waypoint.

            * - :pyclass:`~RunwayCategory`
              - Class defining the runway category in the Aviator catalog.

            * - :pyclass:`~UserRunwaySource`
              - Class defining the user runways in the Aviator catalog.

            * - :pyclass:`~UserRunway`
              - Class defining the user runway in the Aviator catalog.

            * - :pyclass:`~AltitudeMSLOptions`
              - Class defining the altitude MSL options in a procedure.

            * - :pyclass:`~AltitudeOptions`
              - Class defining the altitude options in a procedure.

            * - :pyclass:`~ArcAltitudeOptions`
              - Class defining the altitude options for an arc procedure.

            * - :pyclass:`~ArcAltitudeAndDelayOptions`
              - Class defining the altitude and delay options for an arc procedure.

            * - :pyclass:`~ArcOptions`
              - Class defining the arc options for a procedure.

            * - :pyclass:`~AltitudeMSLAndLevelOffOptions`
              - Class defining the altitude MSL and Level off options in a procedure.

            * - :pyclass:`~CruiseAirspeedOptions`
              - Class defining the cruise airspeed options in a procedure.

            * - :pyclass:`~CruiseAirspeedProfile`
              - Class defining the cruise profile options in a procedure.

            * - :pyclass:`~CruiseAirspeedAndProfileOptions`
              - Class defining the cruise airspeed and profile options in a procedure.

            * - :pyclass:`~LandingCruiseAirspeedAndProfileOptions`
              - Class defining the cruise airspeed and profile options for a landing procedure.

            * - :pyclass:`~EnrouteOptions`
              - Class defining the enroute options in a procedure.

            * - :pyclass:`~EnrouteAndDelayOptions`
              - Class defining the enroute and delay options in a procedure.

            * - :pyclass:`~LandingEnrouteOptions`
              - Class defining the enroute options in a landing procedure.

            * - :pyclass:`~EnrouteTurnDirectionOptions`
              - Class defining the enroute turn direction options in a procedure.

            * - :pyclass:`~NavigationOptions`
              - Class defining the navigation options in a procedure.

            * - :pyclass:`~VerticalPlaneOptions`
              - Class defining the vertical plane options in a procedure.

            * - :pyclass:`~ArcVerticalPlaneOptions`
              - Class defining the vertical plane options in a procedure.

            * - :pyclass:`~VerticalPlaneAndFlightPathOptions`
              - Class defining the vertical plane options for an arc procedure.

            * - :pyclass:`~LandingVerticalPlaneOptions`
              - Class defining the vertical plane options in a landing procedure.

            * - :pyclass:`~RunwayHeadingOptions`
              - Class defining the runway heading options in a takeoff or landing procedure.

            * - :pyclass:`~LandingEnterDownwindPattern`
              - Class defining the enter downwind pattern options for a landing procedure.

            * - :pyclass:`~LandingInterceptGlideslope`
              - Class defining the intercept glideslope options for a landing procedure.

            * - :pyclass:`~LandingStandardInstrumentApproach`
              - Class defining the standard instrument approach options for a landing procedure.

            * - :pyclass:`~TakeoffDeparturePoint`
              - Class defining the departure point options for a takeoff procedure.

            * - :pyclass:`~TakeoffLowTransition`
              - Class defining the low transition options for a takeoff procedure.

            * - :pyclass:`~TakeoffNormal`
              - Class defining the normal options for a takeoff procedure.

            * - :pyclass:`~LevelTurns`
              - Class defining the level turns options for an acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AttitudeTransitions`
              - Class defining the attitude transition options for an acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~ClimbAndDescentTransitions`
              - Class defining the climb and descent transition options for an Acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AeroPropManeuverModeHelper`
              - Class defining the The calculation mode for the Aero/Prop maneuver mode helper. Helper for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftAdvancedAccelerationModel`
              - Class defining the advanced acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftAccelerationMode`
              - Class defining the acceleration mode options for an advanced acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftSimpleAero`
              - Class defining the simple aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftExternalAero`
              - Class defining the external file aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftAero`
              - Class defining the aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftBasicFixedWingAero`
              - Class defining the basic fixed wing aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftProp`
              - Class defining the propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftSimpleProp`
              - Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftExternalProp`
              - Class defining the external propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~AircraftBasicFixedWingProp`
              - Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :pyclass:`~ARINC424Source`
              - Class defining an ARINC424 source in the Aviator catalog.

            * - :pyclass:`~DAFIFSource`
              - Class defining an DAFIF source in the Aviator catalog.

            * - :pyclass:`~BasicFixedWingFwdFlightLiftHelper`
              - Class defining the Lift Coefficient Helper for Forward Flight in the Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

            * - :pyclass:`~BasicManeuverStrategyStraightAhead`
              - Class defining the Straight Ahead strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyCruiseProfile`
              - Class defining the Cruise profile strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyGlideProfile`
              - Class defining the Glide profile strategy for a basic maneuver procedure.

            * - :pyclass:`~AircraftModels`
              - Class defining the User Aircraft Models in the Aviator Catalog.

            * - :pyclass:`~MissileModels`
              - Class defining the User Missile Models in the Aviator Catalog.

            * - :pyclass:`~RotorcraftModels`
              - Class defining the User Rotorcraft Models in the Aviator Catalog.

            * - :pyclass:`~Configuration`
              - Class defining the aircraft configuration for an Aviator mission.

            * - :pyclass:`~FuelTankInternal`
              - Class defining an internal fuel tank for an Aviator aircraft.

            * - :pyclass:`~FuelTankExternal`
              - Class defining an external fuel tank for an Aviator aircraft.

            * - :pyclass:`~PayloadStation`
              - Class defining a payload station for an Aviator aircraft.

            * - :pyclass:`~StationCollection`
              - Class defining a collection of payload stations for an Aviator aircraft.

            * - :pyclass:`~WindModel`
              - Class defining the wind model for a mission, scenario, or procedure.

            * - :pyclass:`~WindModelConstant`
              - Class defining a constant bearing/speed wind model for a mission.

            * - :pyclass:`~WindModelADDS`
              - Class defining a wind model using the NOAA ADDS service for a mission.

            * - :pyclass:`~ADDSMessage`
              - Class defining a message from the NOAA ADDS service.

            * - :pyclass:`~ADDSMessageCollection`
              - Class defining a collection of messages from the NOAA ADDS service.

            * - :pyclass:`~Procedure`
              - Class defining an unknown procedure type.

            * - :pyclass:`~AtmosphereModel`
              - Class defining the atmosphere model for a mission, scenario, or procedure.

            * - :pyclass:`~AtmosphereModelBasic`
              - Class defining the basic atmosphere model.

            * - :pyclass:`~BasicManeuverStrategySimpleTurn`
              - Class defining the simple turn strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyAileronRoll`
              - Class defining the aileron roll strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyFlyAOA`
              - Class defining the fly AOA strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyPull`
              - Class defining the pull strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyRollingPull`
              - Class defining the rolling pull strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategySmoothAccel`
              - Class defining the smooth accel strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategySmoothTurn`
              - Class defining the smooth turn strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverAirspeedOptions`
              - Class defining the airspeed options for basic maneuver strategies.

            * - :pyclass:`~PropulsionThrust`
              - Class defining the the thrust propulsion used in basic maneuver procedures.

            * - :pyclass:`~BasicManeuverStrategyAutopilotNav`
              - Class defining the autopilot - horizontal plane strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyAutopilotProf`
              - Class defining the autopiloc - vertical plane strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyBarrelRoll`
              - Class defining the barrel roll strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyLoop`
              - Class defining the loop strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyLTAHover`
              - Class defining the lighter than air hover strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyIntercept`
              - Class defining the Intercept strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyRelativeBearing`
              - Class defining the Relative Bearing strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyRelativeCourse`
              - Class defining the Relative Course strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyRendezvous`
              - Class defining the Rendezvous/Formation strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyStationkeeping`
              - Class defining the Stationkeeping strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyRelativeFPA`
              - Class defining the Relative Flight Path Angle strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyRelSpeedAltitude`
              - Class defining the Relative Speed/Altitude strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyBezier`
              - Class defining the Bezier strategy for a basic maneuver procedure.

            * - :pyclass:`~BasicManeuverStrategyPushPull`
              - Class defining the Push/Pull strategy for a basic maneuver procedure.

            * - :pyclass:`~ProcedureHoldingCircular`
              - Class defining a holding circular procedure.

            * - :pyclass:`~ProcedureHoldingFigure8`
              - Class defining a holding figure 8 procedure.

            * - :pyclass:`~ProcedureHoldingRacetrack`
              - Class defining a holding racetrack procedure.

            * - :pyclass:`~ProcedureTransitionToHover`
              - Class defining a transition to hover procedure.

            * - :pyclass:`~ProcedureTerrainFollow`
              - Class defining a terrain following procedure.

            * - :pyclass:`~ProcedureHover`
              - Class defining a hover procedure.

            * - :pyclass:`~ProcedureHoverTranslate`
              - Class defining a hover translate procedure.

            * - :pyclass:`~ProcedureTransitionToForwardFlight`
              - Class defining a transition to forward flight procedure.

            * - :pyclass:`~HoverAltitudeOptions`
              - Class defining the altitude options for a VTOL procedure.

            * - :pyclass:`~ProcedureVerticalTakeoff`
              - Class defining a vertical takeoff procedure.

            * - :pyclass:`~ProcedureVerticalLanding`
              - Class defining a vertical landing procedure.

            * - :pyclass:`~ProcedureReferenceState`
              - Class defining a reference state procedure.

            * - :pyclass:`~ProcedureSuperProcedure`
              - Class defining a super procedure.

            * - :pyclass:`~ProcedureLaunch`
              - Class defining a launch procedure.

            * - :pyclass:`~ProcedureAirway`
              - Class defining an Airway procedure.

            * - :pyclass:`~ProcedureAirwayRouter`
              - Class defining an Airway Router procedure.

            * - :pyclass:`~ProcedureAreaTargetSearch`
              - Class defining an Area Target Search procedure.

            * - :pyclass:`~ProcedureFormationRecover`
              - Class defining a Formation/Recover procedure.

            * - :pyclass:`~ProcedureInFormation`
              - Class defining an In Formation procedure.

            * - :pyclass:`~ProcedureParallelFlightLine`
              - Class defining a Parallel Flight Line procedure.

            * - :pyclass:`~ProcedureVGTPoint`
              - Class defining a VGT Point procedure.

            * - :pyclass:`~PerformanceModelOptions`
              - Class defining the options for the active performance model in a phase.

            * - :pyclass:`~AdvancedFixedWingTool`
              - Class defining the options for the Advanced Fixed Wing Tool of an aircraft.

            * - :pyclass:`~AdvancedFixedWingExternalAero`
              - Class defining the External Aero File aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingSubsonicAero`
              - Class defining the subsonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingSubSuperHypersonicAero`
              - Class defining the Sub/Super/Hypersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingSupersonicAero`
              - Class defining the supersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :pyclass:`~PerformanceModel`
              - Class defining an unknown performance model.

            * - :pyclass:`~AdvancedFixedWingGeometryBasic`
              - Class defining a basic geometry wing in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingGeometryVariable`
              - Class defining a variable geometry wing in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingElectricPowerplant`
              - Class defining an Electric powerplant in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingExternalProp`
              - Class defining an External Prop File powerplant in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingSubSuperHypersonicProp`
              - Class defining a Sub/Super/Hypersonic powerplant in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingPistonPowerplant`
              - Class defining a Piston powerplant in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingEmpiricalJetEngine`
              - Class defining the Turbojet and Turbofan empirical models in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingTurbofanBasicABPowerplant`
              - Do not use this class, as it is deprecated. Use AgAvtrAdvFixedWingTurbofanBasicABProp instead.

            * - :pyclass:`~AdvancedFixedWingTurbojetBasicABPowerplant`
              - Do not use this class, as it is deprecated. Use AgAvtrAdvFixedWingTurbojetBasicABProp instead.

            * - :pyclass:`~AdvancedFixedWingTurbofanBasicABProp`
              - Class defining the Turbofan - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingTurbojetBasicABProp`
              - Class defining the Turbojet - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

            * - :pyclass:`~AdvancedFixedWingTurbopropPowerplant`
              - Class defining the Turboprop powerplant in the Advanced Fixed Wing Tool.

            * - :pyclass:`~MissileSimpleAero`
              - Class defining the simple aerodynamic options for a missile.

            * - :pyclass:`~MissileExternalAero`
              - Class defining the external aerodynamic options for a missile.

            * - :pyclass:`~MissileAdvancedAero`
              - Class defining the advanced aerodynamic options for a missile.

            * - :pyclass:`~MissileAero`
              - Class defining the aerodynamic options for a missile.

            * - :pyclass:`~MissileProp`
              - Class defining the propulsion options for a missile.

            * - :pyclass:`~MissileSimpleProp`
              - Class defining the Simple propulsion options for a missile.

            * - :pyclass:`~MissileExternalProp`
              - Class defining the External propulsion options for a missile.

            * - :pyclass:`~MissileRamjetProp`
              - Class defining the Ramjet propulsion options for a missile.

            * - :pyclass:`~MissileRocketProp`
              - Class defining the Rocket propulsion options for a missile.

            * - :pyclass:`~MissileTurbojetProp`
              - Class defining the Turbojet propulsion options for a missile.

            * - :pyclass:`~ReferenceStateForwardFlightOptions`
              - Class defining the Forward Flight options for a Reference State procedure.

            * - :pyclass:`~ReferenceStateTakeoffLandingOptions`
              - Class defining the Takeoff or Landing options for a Reference State procedure.

            * - :pyclass:`~ReferenceStateHoverOptions`
              - Class defining the Hover options for a Reference State procedure.

            * - :pyclass:`~ReferenceStateWeightOnWheelsOptions`
              - Class defining the Weight on Wheels options for a Reference State procedure.

            * - :pyclass:`~SiteRunwayFromCatalog`
              - Class defining a runway from catalog site.

            * - :pyclass:`~SiteAirportFromCatalog`
              - Class defining a airport from catalog site.

            * - :pyclass:`~SiteNavaidFromCatalog`
              - Class defining a navaid from catalog site.

            * - :pyclass:`~SiteVTOLPointFromCatalog`
              - Class defining a VTOL point from catalog site.

            * - :pyclass:`~SiteWaypointFromCatalog`
              - Class defining a waypoint from catalog site.

            * - :pyclass:`~NavaidCategory`
              - Class defining the navaid category in the Aviator catalog.

            * - :pyclass:`~VTOLPointCategory`
              - Class defining the VTOL point category in the Aviator catalog.

            * - :pyclass:`~WaypointCategory`
              - Class defining the waypoint category in the Aviator catalog.

            * - :pyclass:`~ARINC424Navaid`
              - Class defining an ARINC424 Navaid.

            * - :pyclass:`~ARINC424Helipad`
              - Class defining an ARINC424 Helipad.

            * - :pyclass:`~ARINC424Waypoint`
              - Class defining an ARINC424 Waypoint.

            * - :pyclass:`~UserVTOLPointSource`
              - Class defining the user VTOL Point source in the Aviator catalog.

            * - :pyclass:`~UserVTOLPoint`
              - Class defining the user VTOL Point in the Aviator catalog.

            * - :pyclass:`~UserWaypointSource`
              - Class defining the user waypoint source in the Aviator catalog.

            * - :pyclass:`~UserWaypoint`
              - Class defining the user waypoint in the Aviator catalog.

            * - :pyclass:`~PropulsionEfficiencies`
              - Class defining the Propulsion Efficiencies and Losses of a jet engine powerplant in the advanced fixed wing tool.

            * - :pyclass:`~FuelModelKeroseneAFPROP`
              - Class defining the Kerosense - AFPROP fuel type for a thermodynamic jet engine model.

            * - :pyclass:`~FuelModelKeroseneCEA`
              - Class defining the Kerosense - CEA fuel type for a thermodynamic jet engine model.

            * - :pyclass:`~AdvancedFixedWingRamjetBasic`
              - Class defining the basic Ramjet model.

            * - :pyclass:`~AdvancedFixedWingScramjetBasic`
              - Class defining the basic Scramjet model.

            * - :pyclass:`~AircraftVTOLModel`
              - Class defining the VTOL performance model of an aircraft.

            * - :pyclass:`~AircraftVTOL`
              - Class defining the VTOL category of an Aviator aircraft.

            * - :pyclass:`~AircraftTerrainFollowModel`
              - Class defining the TerrainFollow performance model of an aircraft.

            * - :pyclass:`~AircraftTerrainFollow`
              - Class defining the TerrainFollow category of an Aviator aircraft.

            * - :pyclass:`~BasicManeuverStrategyBallistic3D`
              - Class defining Ballistic 3D strategy for a Basic Maneuver procedure.

            * - :pyclass:`~ProcedureLaunchDynState`
              - Class defining a Launch Dyn State procedure.

            * - :pyclass:`~ProcedureLaunchWaypoint`
              - Class defining a Launch Waypoint procedure.

            * - :pyclass:`~SiteDynState`
              - Class defining a Dyn State site.

            * - :pyclass:`~BasicManeuverStrategyPitch3D`
              - Class defining Pitch 3D strategy for a Basic Maneuver procedure.

            * - :pyclass:`~RefuelDumpProperties`
              - Class defining the refuel/dump properties for the current procedure.

            * - :pyclass:`~ProcedureFastTimeOptions`
              - Class defining fast operations (without error or constraint checks) for time options for the current procedure.

            * - :pyclass:`~BasicManeuverTargetPositionVel`
              - Class defining the target position and velocity strategies for basic maneuvers.

            * - :pyclass:`~BasicManeuverTargetPositionVelNoisyBrgRng`
              - Class defining the position and velocity strategy, Noisy Bearing Range.

            * - :pyclass:`~BasicManeuverTargetPositionVelNoisySurfTgt`
              - Class defining the position and velocity strategy, Noisy Surface Target.


    .. tab-items:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~ERROR_CODES`
              - Error Codes.

            * - :pyclass:`~CLOSURE_VALUE`
              - The closure value.

            * - :pyclass:`~PROCEDURE_TYPE`
              - Aviator procedure types.

            * - :pyclass:`~SITE_TYPE`
              - Aviator site types.

            * - :pyclass:`~BASIC_MANEUVER_STRATEGY`
              - Basic maneuver strategy types.

            * - :pyclass:`~STRAIGHT_AHEAD_REFERENCE_FRAME`
              - Straight Ahead basic maneuver Reference Frame.

            * - :pyclass:`~AIRSPEED_TYPE`
              - Airspeed types.

            * - :pyclass:`~AERO_PROP_SIMPLE_MODE`
              - Aircraft operating mode for basic acceleration models with aerodynamics set to Simple.

            * - :pyclass:`~AERO_PROP_FLIGHT_MODE`
              - Flight mode for the Aero/Prop maneuver mode helper in aircraft acceleration models.

            * - :pyclass:`~PHASE_OF_FLIGHT`
              - Flight mode for basic maneuver procedures.

            * - :pyclass:`~CRUISE_SPEED`
              - Cruise airspeed type for the procedure.

            * - :pyclass:`~TAKEOFF_MODE`
              - Takeoff procedure mode.

            * - :pyclass:`~APPROACH_MODE`
              - Landing procedure approach mode.

            * - :pyclass:`~NAVIGATOR_TURN_DIRECTION`
              - Turn mode for procedures with Enroute Turn Direction options.

            * - :pyclass:`~BASIC_MANEUVER_FUEL_FLOW_TYPE`
              - Fuel flow type for basic maneuver procedures.

            * - :pyclass:`~BASIC_MANEUVER_ALTITUDE_LIMIT`
              - The type of response Aviator will have if the maneuver attempts to exceed the altitude limit.

            * - :pyclass:`~RUNWAY_HIGH_LOW_END`
              - Runway heading that the aircraft will use.

            * - :pyclass:`~BASIC_MANEUVER_REFERENCE_FRAME`
              - Reference frame for the basic maneuver strategy.

            * - :pyclass:`~BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT`
              - Define the control limits for the aircraft during the maneuver.

            * - :pyclass:`~ACCEL_MANEUVER_MODE`
              - The mode that the aircraft will adhere to the specified acceleration parameters.

            * - :pyclass:`~AIRCRAFT_AERO_STRATEGY`
              - The aerodynamic strategy used to compute lift, drag, angle of attack, sideslip and intermediate / derived values.

            * - :pyclass:`~AIRCRAFT_PROP_STRATEGY`
              - The propulsion strategy used to compute thrust and throttle setting.

            * - :pyclass:`~AGL_MSL`
              - The altitude mode.

            * - :pyclass:`~LANDING_APPROACH_FIX_RANGE_MODE`
              - The reference point on the runway for the Approach Fix Range.

            * - :pyclass:`~ACCELERATION_ADVANCED_ACCEL_MODE`
              - Acceleration mode for aircraft advanced acceleration models.

            * - :pyclass:`~ACCEL_MANEUVER_AERO_PROP_MODE`
              - The mode used for the Aero/Prop maneuver mode helper for aircraft basic acceleration models.

            * - :pyclass:`~BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS`
              - The type of response Aviator will have if the basic maneuver attempts to exceed the airspeed limit.

            * - :pyclass:`~BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE`
              - Powered Cruise Options.

            * - :pyclass:`~TURN_MODE`
              - The mode to specify an aircraft's level turn performance for acceleration performance models.

            * - :pyclass:`~POINT_TO_POINT_MODE`
              - The heading or course of the aircraft at the beginning of the procedure.

            * - :pyclass:`~ALTITUDE_CONSTRAINT_MANEUVER_MODE`
              - Turn mode for procedures that may require a level off maneuver.

            * - :pyclass:`~WIND_MODEL_TYPE`
              - The wind model type.

            * - :pyclass:`~WIND_ATMOS_MODEL_SOURCE`
              - The source for the wind or atmosphere model.

            * - :pyclass:`~ADDS_MSG_INTERP_TYPE`
              - The interpolation method for the wind conditions.

            * - :pyclass:`~ADDS_MISSING_MSG_TYPE`
              - The wind effect to apply if there is an interval gap between messages.

            * - :pyclass:`~ADDS_MSG_EXTRAP_TYPE`
              - The wind effect to apply if the procedure(s) extend beyond the intervals of any available messages.

            * - :pyclass:`~ADDS_FORECAST_TYPE`
              - The forecast type for the NOAA ADDS message.

            * - :pyclass:`~ATMOSPHERE_MODEL`
              - The basic atmosphere model type.

            * - :pyclass:`~SMOOTH_TURN_MODE`
              - The basic maneuver smooth turn mode.

            * - :pyclass:`~PERF_MODEL_OVERRIDE`
              - The performance model override mode.

            * - :pyclass:`~BASIC_MANEUVER_AIRSPEED_MODE`
              - The basic maneuver airspeed mode.

            * - :pyclass:`~AILERON_ROLL_FLIGHT_PATH`
              - The flight path option for an aileron roll strategy for a basic maneuver procedure.

            * - :pyclass:`~ROLL_LEFT_RIGHT`
              - The roll direction for an aileron roll strategy for a basic maneuver procedure.

            * - :pyclass:`~ROLL_UPRIGHT_INVERTED`
              - The orientation for an aileron roll strategy for a basic maneuver procedure.

            * - :pyclass:`~AILERON_ROLL_MODE`
              - The roll mode aileron roll strategy for a basic maneuver procedure.

            * - :pyclass:`~FLY_AOA_LEFT_RIGHT`
              - The roll direction for a Fly AOA strategy for a basic maneuver procedure.

            * - :pyclass:`~SMOOTH_ACCEL_LEFT_RIGHT`
              - The roll direction for a smooth acceleration strategy for a basic maneuver procedure.

            * - :pyclass:`~PULL_MODE`
              - The pull mode for a pull strategy of a basic maneuver procedure.

            * - :pyclass:`~ROLLING_PULL_MODE`
              - The rolling pull mode for a rolling pull strategy of a basic maneuver procedure.

            * - :pyclass:`~SMOOTH_ACCEL_STOP_CONDITIONS`
              - The rolling pull mode for a rolling pull strategy of a basic maneuver procedure.

            * - :pyclass:`~AUTOPILOT_HORIZ_PLANE_MODE`
              - The autopilot mode for an autopilot - horizontal plane strategy of a basic maneuver procedure.

            * - :pyclass:`~ANGLE_MODE`
              - The angle mode for a barrel roll strategy of a basic maneuver procedure.

            * - :pyclass:`~HOVER_ALTITUDE_MODE`
              - The altitude mode for the lighter than air hover strategy of a basic maneuver procedure.

            * - :pyclass:`~HOVER_HEADING_MODE`
              - The heading mode for the lighter than air hover strategy of a basic maneuver procedure.

            * - :pyclass:`~AUTOPILOT_ALTITUDE_MODE`
              - The altitude mode for the autopilot - vertical plane strategy of a basic maneuver procedure.

            * - :pyclass:`~AUTOPILOT_ALTITUDE_CONTROL_MODE`
              - The altitude control mode for the autopilot - vertical plane strategy of a basic maneuver procedure.

            * - :pyclass:`~CLOSURE_MODE`
              - The closure mode for guidance strategies of the basic maneuver procedure.

            * - :pyclass:`~INTERCEPT_MODE`
              - The intercept mode for the intercept strategy of the basic maneuver procedure.

            * - :pyclass:`~RENDEZVOUS_STOP_CONDITION`
              - The stop condition options for a rendezvous formation strategy of the basic maneuver procedure.

            * - :pyclass:`~FORMATION_FLYER_STOP_CONDITION`
              - The stop condition options for a Formation Flyer procedure.

            * - :pyclass:`~EXT_EPHEM_FLIGHT_MODE`
              - Flight mode enums for ExtEphem.

            * - :pyclass:`~ACCEL_PERF_MODEL_OVERRIDE`
              - The acceleration performance model override mode.

            * - :pyclass:`~STATIONKEEPING_STOP_CONDITION`
              - The stop condition options for a stationkeeping strategy.

            * - :pyclass:`~TURN_DIRECTION`
              - The roll direction for an aileron roll strategy for a basic maneuver procedure.

            * - :pyclass:`~PROFILE_CONTROL_LIMIT`
              - Define the control limits for a profile strategy of a basic maneuver procedure.

            * - :pyclass:`~REL_SPEED_ALTITUDE_STOP_CONDITION`
              - The stop condition options for a relative speed/altitude strategy.

            * - :pyclass:`~RELATIVE_ALTITUDE_MODE`
              - The relative altitude mode for a relative speed/altitude strategy.

            * - :pyclass:`~FLY_TO_FLIGHT_PATH_ANGLE_MODE`
              - The flight path angle mode mode for a bezier profile strategy.

            * - :pyclass:`~PUSH_PULL`
              - The option to pull up or push over for a push/pull profile strategy.

            * - :pyclass:`~ACCEL_MODE`
              - The acceleration/decelation option for a push/pull profile strategy.

            * - :pyclass:`~DELAY_ALTITUDE_MODE`
              - The altitude options for a delay procedure.

            * - :pyclass:`~JOIN_EXIT_ARC_METHOD`
              - The options to join or exit an arc.

            * - :pyclass:`~FLIGHT_LINE_PROC_TYPE`
              - The procedure methodology used to calculate the flight line.

            * - :pyclass:`~TRANSITION_TO_HOVER_MODE`
              - The type of hover to transition to.

            * - :pyclass:`~VTOL_RATE_MODE`
              - The rate mode for the VTOL procedure.

            * - :pyclass:`~HOLDING_PROFILE_MODE`
              - How the aircraft will perform during the holding pattern with respect to airspeed and altitude.

            * - :pyclass:`~HOLDING_DIRECTION`
              - The turn direction for the aircraft to enter the holding pattern.

            * - :pyclass:`~HOLD_REFUEL_DUMP_MODE`
              - Define when the aircraft will leave the holding pattern after it has completed refueling or dumping fuel.

            * - :pyclass:`~HOLDING_ENTRY_MANEUVER`
              - Define how the aircraft will enter the holding pattern.

            * - :pyclass:`~VTOL_TRANSITION_MODE`
              - The mode to specify the course of the transition maneuver.

            * - :pyclass:`~VTOL_FINAL_HEADING_MODE`
              - The mode to specify the heading at the end of the maneuver.

            * - :pyclass:`~VTOL_TRANSLATION_MODE`
              - The mode to specify the translation of the VTOL maneuver.

            * - :pyclass:`~VTOL_TRANSLATION_FINAL_COURSE_MODE`
              - The mode to specify the final course of the VTOL maneuver.

            * - :pyclass:`~HOVER_MODE`
              - The hover mode.

            * - :pyclass:`~VTOL_HEADING_MODE`
              - The heading mode for the hover maneuver.

            * - :pyclass:`~VERT_LANDING_MODE`
              - The heading mode for a vertical landing maneuver.

            * - :pyclass:`~LAUNCH_ATTITUDE_MODE`
              - The attitude mode for the launch procedure.

            * - :pyclass:`~FUEL_FLOW_TYPE`
              - The fuel flow type to use for the procedure.

            * - :pyclass:`~LINE_ORIENTATION`
              - The orientation for a parallel flight line procedure.

            * - :pyclass:`~REL_ABS_BEARING`
              - The options for a bearing that can be relative or absolute.

            * - :pyclass:`~BASIC_FIXED_WING_PROP_MODE`
              - The option to specify the thrust (jet engines) or power (propellers).

            * - :pyclass:`~CLIMB_SPEED_TYPE`
              - The mode to calculate the aircraft's airspeed while climbing for an advanced climb performance model.

            * - :pyclass:`~CRUISE_MAX_PERF_SPEED_TYPE`
              - The method for defining the maximum performance airspeed of the aircraft for an advanced cruise model.

            * - :pyclass:`~DESCENT_SPEED_TYPE`
              - The method for calculating the aircraft's airspeed while descending.

            * - :pyclass:`~TAKEOFF_LANDING_SPEED_MODE`
              - The method for calculating the aircraft's speed upon leaving the ground or at wheels down.

            * - :pyclass:`~DEPARTURE_SPEED_MODE`
              - The method for calculating the aircraft's airspeed upon leaving the ground.

            * - :pyclass:`~ADVANCED_FIXED_WING_AERO_STRATEGY`
              - The aerodynamic strategy for the Advanced Fixed Wing Tool.

            * - :pyclass:`~ADVANCED_FIXED_WING_GEOMETRY`
              - The method to define the wing geometry of an aircraft in the Advanced Fixed Wing Tool.

            * - :pyclass:`~ADVANCED_FIXED_WING_POWERPLANT_STRATEGY`
              - The powerplant strategy for the Advanced Fixed Wing Tool.

            * - :pyclass:`~MISSILE_AERO_STRATEGY`
              - The aerodynamic strategy used to compute lift, drag, angle of attack, sideslip and intermediate / derived values.

            * - :pyclass:`~MISSILE_PROP_STRATEGY`
              - The propulsion strategy used to compute thrust and throttle setting.

            * - :pyclass:`~ROTORCRAFT_POWERPLANT_TYPE`
              - The powerplant type for a rotorcraft.

            * - :pyclass:`~MINIMIZE_SITE_PROC_TIME_DIFF`
              - Options for minimizing the time difference between the procedure and site times.

            * - :pyclass:`~STK_OBJECT_WAYPOINT_OFFSET_MODE`
              - The options to offset the site location relative to the STK Object.

            * - :pyclass:`~SEARCH_PATTERN_COURSE_MODE`
              - The mode to determine the course of the search pattern.

            * - :pyclass:`~DELAY_TURN_DIRECTION`
              - Turn mode for procedures with Delay options.

            * - :pyclass:`~TRAJECTORY_BLEND_MODE`
              - The interpolation mode to determine the aircraft's position and velocity.

            * - :pyclass:`~REFERENCE_STATE_PERF_MODE`
              - The type of motion the aircraft is engaged in at the reference state.

            * - :pyclass:`~REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE`
              - The mode to specify the longitudinal acceleration of the aircraft.

            * - :pyclass:`~REFERENCE_STATE_LATERAL_ACCEL_MODE`
              - The mode to specify the lateral acceleration of the aircraft.

            * - :pyclass:`~REFERENCE_STATE_ATTITUDE_MODE`
              - The mode to specify the attitude rate of change.

            * - :pyclass:`~AND_OR`
              - The option to specify AND or OR.

            * - :pyclass:`~JET_ENGINE_TECHNOLOGY_LEVEL`
              - The technology level of the jet engine.

            * - :pyclass:`~JET_ENGINE_INTAKE_TYPE`
              - The intake type of the jet engine.

            * - :pyclass:`~JET_ENGINE_TURBINE_TYPE`
              - The turbine type of the jet engine.

            * - :pyclass:`~JET_ENGINE_EXHAUST_NOZZLE_TYPE`
              - The exhaust nozzle type of the jet engine.

            * - :pyclass:`~JET_FUEL_TYPE`
              - The jet fuel type.

            * - :pyclass:`~AFPROP_FUEL_TYPE`
              - The AFPROP fuel type.

            * - :pyclass:`~CEA_FUEL_TYPE`
              - The CEA fuel type.

            * - :pyclass:`~TURBINE_MODE`
              - The turbine mode for a Sub/Super/Hypersonic powerplant.

            * - :pyclass:`~RAMJET_MODE`
              - The ramjet mode for a Sub/Super/Hypersonic powerplant.

            * - :pyclass:`~SCRAMJET_MODE`
              - The scramjet mode for a Sub/Super/Hypersonic powerplant.

            * - :pyclass:`~NUMERICAL_INTEGRATOR`
              - The numerical integrator to be used for the procedure.

            * - :pyclass:`~BALLISTIC_3D_CONTROL_MODE`
              - The control mode used to define the ballistic 3D strategy of the basic maneuver procedure.

            * - :pyclass:`~LAUNCH_DYN_STATE_COORD_FRAME`
              - The coordinate frame used for a LaunchDynState procedure.

            * - :pyclass:`~LAUNCH_DYN_STATE_BEARING_REFERENCE`
              - The vector used as a bearing reference for a LaunchDynState procedure.

            * - :pyclass:`~ALTITUDE_REFERENCE`
              - The altitude reference.

            * - :pyclass:`~SMOOTH_TURN_FPA_MODE`
              - The flight path angle mode for the Smooth Turn strategy of the Basic Maneuver procedure.

            * - :pyclass:`~PITCH_3D_CONTROL_MODE`
              - The control mode used to define the pitch 3D strategy of the basic maneuver procedure.

            * - :pyclass:`~REFUEL_DUMP_MODE`
              - The modes used to define procedure refuel/dump modes.

            * - :pyclass:`~BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE`
              - The modes used to define basic maneuver glide speed control modes.

            * - :pyclass:`~TARGET_POSITION_VEL_TYPE`
              - The target pos/vel type.

            * - :pyclass:`~EPHEM_SHIFT_ROTATE_ALTITUDE_MODE`
              - Ephem alt mode.

            * - :pyclass:`~EPHEM_SHIFT_ROTATE_COURSE_MODE`
              - Ephem course mode.



Description
-----------

Object Model components specifically designed to support STK Aviator.

Detail
------

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    🗎 matlab<matlab>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> ISite<ISite>
    --> IWindModel<IWindModel>
    --> IADDSMessage<IADDSMessage>
    --> IFuelTankInternal<IFuelTankInternal>
    --> IFuelTankExternal<IFuelTankExternal>
    --> IPayloadStation<IPayloadStation>
    --> IAircraftModel<IAircraftModel>
    --> IAircraftSimpleAero<IAircraftSimpleAero>
    --> ILevelTurns<ILevelTurns>
    --> IAttitudeTransitions<IAttitudeTransitions>
    --> IClimbAndDescentTransitions<IClimbAndDescentTransitions>
    --> ICatalogItem<ICatalogItem>
    --> IAircraftBasicClimbModel<IAircraftBasicClimbModel>
    --> IAircraftBasicAccelerationModel<IAircraftBasicAccelerationModel>
    --> IAircraftCategory<IAircraftCategory>
    --> IRunwayCategory<IRunwayCategory>
    --> IBasicManeuverStrategy<IBasicManeuverStrategy>
    --> IAircraftVTOL<IAircraftVTOL>
    --> IAircraftExternalAero<IAircraftExternalAero>
    --> IAircraftSimpleProp<IAircraftSimpleProp>
    --> IAircraftExternalProp<IAircraftExternalProp>
    --> IAircraftBasicFixedWingProp<IAircraftBasicFixedWingProp>
    --> IAircraftAdvancedClimbModel<IAircraftAdvancedClimbModel>
    --> IAircraftBasicCruiseModel<IAircraftBasicCruiseModel>
    --> IAircraftAdvancedCruiseModel<IAircraftAdvancedCruiseModel>
    --> IAircraftBasicDescentModel<IAircraftBasicDescentModel>
    --> IAircraftAdvancedDescentModel<IAircraftAdvancedDescentModel>
    --> IAircraftBasicLandingModel<IAircraftBasicLandingModel>
    --> IAircraftAdvancedLandingModel<IAircraftAdvancedLandingModel>
    --> IAircraftBasicTakeoffModel<IAircraftBasicTakeoffModel>
    --> IAircraftAdvancedTakeoffModel<IAircraftAdvancedTakeoffModel>
    --> IAircraftVTOLModel<IAircraftVTOLModel>
    --> IAircraftTerrainFollow<IAircraftTerrainFollow>
    --> IPerformanceModelOptions<IPerformanceModelOptions>
    --> IAdvancedFixedWingTool<IAdvancedFixedWingTool>
    --> IAdvancedFixedWingExternalAero<IAdvancedFixedWingExternalAero>
    --> IAdvancedFixedWingSubsonicAero<IAdvancedFixedWingSubsonicAero>
    --> IAdvancedFixedWingSubSuperHypersonicAero<IAdvancedFixedWingSubSuperHypersonicAero>
    --> IAdvancedFixedWingSubSuperHypersonicProp<IAdvancedFixedWingSubSuperHypersonicProp>
    --> IAdvancedFixedWingSupersonicAero<IAdvancedFixedWingSupersonicAero>
    --> IAdvancedFixedWingGeometryBasic<IAdvancedFixedWingGeometryBasic>
    --> IAdvancedFixedWingGeometryVariable<IAdvancedFixedWingGeometryVariable>
    --> IAdvancedFixedWingElectricPowerplant<IAdvancedFixedWingElectricPowerplant>
    --> IAdvancedFixedWingExternalProp<IAdvancedFixedWingExternalProp>
    --> IAdvancedFixedWingPistonPowerplant<IAdvancedFixedWingPistonPowerplant>
    --> IAdvancedFixedWingTurbopropPowerplant<IAdvancedFixedWingTurbopropPowerplant>
    --> IAdvancedFixedWingEmpiricalJetEngine<IAdvancedFixedWingEmpiricalJetEngine>
    --> IAdvancedFixedWingTurbojetBasicABProp<IAdvancedFixedWingTurbojetBasicABProp>
    --> IAdvancedFixedWingTurbofanBasicABProp<IAdvancedFixedWingTurbofanBasicABProp>
    --> IAviatorVehicle<IAviatorVehicle>
    --> IMissileModel<IMissileModel>
    --> IMissileAero<IMissileAero>
    --> IMissileProp<IMissileProp>
    --> IMissileSimpleAero<IMissileSimpleAero>
    --> IMissileSimpleProp<IMissileSimpleProp>
    --> IMissileExternalAero<IMissileExternalAero>
    --> IMissileExternalProp<IMissileExternalProp>
    --> IMissileAdvancedAero<IMissileAdvancedAero>
    --> IMissileRamjetProp<IMissileRamjetProp>
    --> IMissileRocketProp<IMissileRocketProp>
    --> IMissileTurbojetProp<IMissileTurbojetProp>
    --> IRotorcraftModel<IRotorcraftModel>
    --> IRotorcraftAero<IRotorcraftAero>
    --> IRotorcraftProp<IRotorcraftProp>
    --> IUserRunwaySource<IUserRunwaySource>
    --> IUserRunway<IUserRunway>
    --> IARINC424Item<IARINC424Item>
    --> IARINC424Source<IARINC424Source>
    --> IDAFIFSource<IDAFIFSource>
    --> IUserVTOLPoint<IUserVTOLPoint>
    --> IUserVTOLPointSource<IUserVTOLPointSource>
    --> IUserWaypoint<IUserWaypoint>
    --> IUserWaypointSource<IUserWaypointSource>
    --> IPropulsionEfficiencies<IPropulsionEfficiencies>
    --> IFuelModelKeroseneAFPROP<IFuelModelKeroseneAFPROP>
    --> IFuelModelKeroseneCEA<IFuelModelKeroseneCEA>
    --> IAdvancedFixedWingRamjetBasic<IAdvancedFixedWingRamjetBasic>
    --> IAdvancedFixedWingScramjetBasic<IAdvancedFixedWingScramjetBasic>
    --> IRefuelDumpProperties<IRefuelDumpProperties>
    --> IProcedureFastTimeOptions<IProcedureFastTimeOptions>
    --> IAtmosphereModelBasic<IAtmosphereModelBasic>
    --> IAtmosphereModel<IAtmosphereModel>
    --> IADDSMessageCollection<IADDSMessageCollection>
    --> IWindModelADDS<IWindModelADDS>
    --> IWindModelConstant<IWindModelConstant>
    --> IStation<IStation>
    --> IStationCollection<IStationCollection>
    --> IConfiguration<IConfiguration>
    --> ICatalogSource<ICatalogSource>
    --> IAircraftModels<IAircraftModels>
    --> IMissileModels<IMissileModels>
    --> IRotorcraftModels<IRotorcraftModels>
    --> IBasicFixedWingLiftHelper<IBasicFixedWingLiftHelper>
    --> IAircraftBasicFixedWingAero<IAircraftBasicFixedWingAero>
    --> IAircraftAero<IAircraftAero>
    --> IAircraftProp<IAircraftProp>
    --> IAircraftAccelerationMode<IAircraftAccelerationMode>
    --> IAircraftAdvancedAccelerationModel<IAircraftAdvancedAccelerationModel>
    --> IAeroPropManeuverModeHelper<IAeroPropManeuverModeHelper>
    --> ICatalogRunway<ICatalogRunway>
    --> ICatalogAirport<ICatalogAirport>
    --> ICatalogNavaid<ICatalogNavaid>
    --> ICatalogVTOLPoint<ICatalogVTOLPoint>
    --> ICatalogWaypoint<ICatalogWaypoint>
    --> IARINC424Airport<IARINC424Airport>
    --> IDAFIFItem<IDAFIFItem>
    --> IARINC424Runway<IARINC424Runway>
    --> IAirportCategory<IAirportCategory>
    --> INavaidCategory<INavaidCategory>
    --> IVTOLPointCategory<IVTOLPointCategory>
    --> IWaypointCategory<IWaypointCategory>
    --> IAircraftClimb<IAircraftClimb>
    --> IAircraftCruise<IAircraftCruise>
    --> IAircraftDescent<IAircraftDescent>
    --> IAircraftLanding<IAircraftLanding>
    --> IAircraftTakeoff<IAircraftTakeoff>
    --> IAircraftAcceleration<IAircraftAcceleration>
    --> ICatalog<ICatalog>
    --> IProcedureTimeOptions<IProcedureTimeOptions>
    --> ICalculationOptions<ICalculationOptions>
    --> INavigationOptions<INavigationOptions>
    --> IAltitudeMSLAndLevelOffOptions<IAltitudeMSLAndLevelOffOptions>
    --> IAltitudeMSLOptions<IAltitudeMSLOptions>
    --> IAltitudeOptions<IAltitudeOptions>
    --> IHoverAltitudeOptions<IHoverAltitudeOptions>
    --> IArcAltitudeOptions<IArcAltitudeOptions>
    --> IArcAltitudeAndDelayOptions<IArcAltitudeAndDelayOptions>
    --> IArcOptions<IArcOptions>
    --> IVerticalPlaneOptions<IVerticalPlaneOptions>
    --> IVerticalPlaneAndFlightPathOptions<IVerticalPlaneAndFlightPathOptions>
    --> IArcVerticalPlaneOptions<IArcVerticalPlaneOptions>
    --> IEnrouteOptions<IEnrouteOptions>
    --> IEnrouteAndDelayOptions<IEnrouteAndDelayOptions>
    --> IEnrouteTurnDirectionOptions<IEnrouteTurnDirectionOptions>
    --> ICruiseAirspeedOptions<ICruiseAirspeedOptions>
    --> ICruiseAirspeedProfile<ICruiseAirspeedProfile>
    --> ICruiseAirspeedAndProfileOptions<ICruiseAirspeedAndProfileOptions>
    --> IAutomationStrategyFactory<IAutomationStrategyFactory>
    --> IConnect<IConnect>
    --> IRunwayHeadingOptions<IRunwayHeadingOptions>
    --> IProcedure<IProcedure>
    --> IProcedureCollection<IProcedureCollection>
    --> IPhase<IPhase>
    --> IPhaseCollection<IPhaseCollection>
    --> IMission<IMission>
    --> IAviatorPropagator<IAviatorPropagator>
    --> IPerformanceModel<IPerformanceModel>
    --> IAdvancedFixedWingGeometry<IAdvancedFixedWingGeometry>
    --> IAdvancedFixedWingTurbofanBasicABPowerplant<IAdvancedFixedWingTurbofanBasicABPowerplant>
    --> IAdvancedFixedWingTurbojetBasicABPowerplant<IAdvancedFixedWingTurbojetBasicABPowerplant>
    --> IAdvancedFixedWingPowerplant<IAdvancedFixedWingPowerplant>
    --> ISiteUnknown<ISiteUnknown>
    --> IAircraftTerrainFollowModel<IAircraftTerrainFollowModel>
    --> IBasicManeuverTargetPositionVel<IBasicManeuverTargetPositionVel>
    --> IPropulsionThrust<IPropulsionThrust>
    --> IBasicManeuverAirspeedOptions<IBasicManeuverAirspeedOptions>
    --> IBasicManeuverStrategyAileronRoll<IBasicManeuverStrategyAileronRoll>
    --> IBasicManeuverStrategyAutopilotNav<IBasicManeuverStrategyAutopilotNav>
    --> IBasicManeuverStrategyAutopilotProf<IBasicManeuverStrategyAutopilotProf>
    --> IBasicManeuverStrategyBarrelRoll<IBasicManeuverStrategyBarrelRoll>
    --> IBasicManeuverStrategyLoop<IBasicManeuverStrategyLoop>
    --> IBasicManeuverStrategyLTAHover<IBasicManeuverStrategyLTAHover>
    --> IBasicManeuverStrategyFlyAOA<IBasicManeuverStrategyFlyAOA>
    --> IBasicManeuverStrategyPull<IBasicManeuverStrategyPull>
    --> IBasicManeuverStrategyRollingPull<IBasicManeuverStrategyRollingPull>
    --> IBasicManeuverStrategySmoothAccel<IBasicManeuverStrategySmoothAccel>
    --> IBasicManeuverStrategySmoothTurn<IBasicManeuverStrategySmoothTurn>
    --> IBasicManeuverStrategySimpleTurn<IBasicManeuverStrategySimpleTurn>
    --> IBasicManeuverStrategyIntercept<IBasicManeuverStrategyIntercept>
    --> IBasicManeuverStrategyRelativeBearing<IBasicManeuverStrategyRelativeBearing>
    --> IBasicManeuverStrategyRelativeCourse<IBasicManeuverStrategyRelativeCourse>
    --> IBasicManeuverStrategyRendezvous<IBasicManeuverStrategyRendezvous>
    --> IBasicManeuverStrategyStationkeeping<IBasicManeuverStrategyStationkeeping>
    --> IBasicManeuverStrategyRelativeFPA<IBasicManeuverStrategyRelativeFPA>
    --> IBasicManeuverStrategyRelSpeedAltitude<IBasicManeuverStrategyRelSpeedAltitude>
    --> IBasicManeuverStrategyBezier<IBasicManeuverStrategyBezier>
    --> IBasicManeuverStrategyPushPull<IBasicManeuverStrategyPushPull>
    --> IBasicManeuverStrategyGlideProfile<IBasicManeuverStrategyGlideProfile>
    --> IBasicManeuverStrategyCruiseProfile<IBasicManeuverStrategyCruiseProfile>
    --> IBasicManeuverStrategyStraightAhead<IBasicManeuverStrategyStraightAhead>
    --> IBasicManeuverStrategyWeave<IBasicManeuverStrategyWeave>
    --> IBasicManeuverStrategyBallistic3D<IBasicManeuverStrategyBallistic3D>
    --> IBasicManeuverStrategyPitch3D<IBasicManeuverStrategyPitch3D>
    --> IBasicManeuverTargetPositionVelNoisyBrgRng<IBasicManeuverTargetPositionVelNoisyBrgRng>
    --> IBasicManeuverTargetPositionVelNoisySurfTgt<IBasicManeuverTargetPositionVelNoisySurfTgt>
    --> ITakeoffNormal<ITakeoffNormal>
    --> ITakeoffDeparturePoint<ITakeoffDeparturePoint>
    --> ITakeoffLowTransition<ITakeoffLowTransition>
    --> IReferenceStateForwardFlightOptions<IReferenceStateForwardFlightOptions>
    --> IReferenceStateHoverOptions<IReferenceStateHoverOptions>
    --> IReferenceStateWeightOnWheelsOptions<IReferenceStateWeightOnWheelsOptions>
    --> IReferenceStateTakeoffLandingOptions<IReferenceStateTakeoffLandingOptions>
    --> ILandingEnterDownwindPattern<ILandingEnterDownwindPattern>
    --> ILandingInterceptGlideslope<ILandingInterceptGlideslope>
    --> ILandingStandardInstrumentApproach<ILandingStandardInstrumentApproach>
    --> IProcedureBasicManeuver<IProcedureBasicManeuver>
    --> ISiteWaypoint<ISiteWaypoint>
    --> ISiteEndOfPrevProcedure<ISiteEndOfPrevProcedure>
    --> ISiteVTOLPoint<ISiteVTOLPoint>
    --> ISiteSTKVehicle<ISiteSTKVehicle>
    --> ISiteReferenceState<ISiteReferenceState>
    --> ISiteSuperProcedure<ISiteSuperProcedure>
    --> ISiteRelToPrevProcedure<ISiteRelToPrevProcedure>
    --> ISiteSTKObjectWaypoint<ISiteSTKObjectWaypoint>
    --> ISiteSTKStaticObject<ISiteSTKStaticObject>
    --> ISiteRelToSTKObject<ISiteRelToSTKObject>
    --> ISiteSTKAreaTarget<ISiteSTKAreaTarget>
    --> ISiteRunway<ISiteRunway>
    --> IProcedureLanding<IProcedureLanding>
    --> IProcedureEnroute<IProcedureEnroute>
    --> IProcedureExtEphem<IProcedureExtEphem>
    --> IProcedureFormationFlyer<IProcedureFormationFlyer>
    --> IProcedureBasicPointToPoint<IProcedureBasicPointToPoint>
    --> IProcedureDelay<IProcedureDelay>
    --> IProcedureTakeoff<IProcedureTakeoff>
    --> IProcedureArcEnroute<IProcedureArcEnroute>
    --> IProcedureArcPointToPoint<IProcedureArcPointToPoint>
    --> IProcedureFlightLine<IProcedureFlightLine>
    --> IProcedureHoldingCircular<IProcedureHoldingCircular>
    --> IProcedureHoldingFigure8<IProcedureHoldingFigure8>
    --> IProcedureHoldingRacetrack<IProcedureHoldingRacetrack>
    --> IProcedureTransitionToHover<IProcedureTransitionToHover>
    --> IProcedureTerrainFollow<IProcedureTerrainFollow>
    --> IProcedureHover<IProcedureHover>
    --> IProcedureHoverTranslate<IProcedureHoverTranslate>
    --> IProcedureTransitionToForwardFlight<IProcedureTransitionToForwardFlight>
    --> IProcedureVerticalTakeoff<IProcedureVerticalTakeoff>
    --> IProcedureVerticalLanding<IProcedureVerticalLanding>
    --> IProcedureReferenceState<IProcedureReferenceState>
    --> IProcedureSuperProcedure<IProcedureSuperProcedure>
    --> IProcedureLaunch<IProcedureLaunch>
    --> IProcedureAirway<IProcedureAirway>
    --> IProcedureAirwayRouter<IProcedureAirwayRouter>
    --> IProcedureAreaTargetSearch<IProcedureAreaTargetSearch>
    --> IProcedureFormationRecover<IProcedureFormationRecover>
    --> IProcedureInFormation<IProcedureInFormation>
    --> IProcedureParallelFlightLine<IProcedureParallelFlightLine>
    --> IProcedureVGTPoint<IProcedureVGTPoint>
    --> ISiteRunwayFromCatalog<ISiteRunwayFromCatalog>
    --> ISiteAirportFromCatalog<ISiteAirportFromCatalog>
    --> ISiteNavaidFromCatalog<ISiteNavaidFromCatalog>
    --> ISiteVTOLPointFromCatalog<ISiteVTOLPointFromCatalog>
    --> ISiteWaypointFromCatalog<ISiteWaypointFromCatalog>
    --> IProcedureLaunchDynState<IProcedureLaunchDynState>
    --> IProcedureLaunchWaypoint<IProcedureLaunchWaypoint>
    --> ISiteDynState<ISiteDynState>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> SiteWaypoint<>
    --> SiteEndOfPrevProcedure<>
    --> SiteVTOLPoint<>
    --> SiteReferenceState<>
    --> SiteSTKVehicle<>
    --> SiteSuperProcedure<>
    --> SiteRelToPrevProcedure<>
    --> SiteSTKObjectWaypoint<>
    --> SiteSTKStaticObject<>
    --> SiteRelToSTKObject<>
    --> SiteSTKAreaTarget<>
    --> SiteRunway<>
    --> Site<>
    --> ProcedureLanding<>
    --> ProcedureEnroute<>
    --> ProcedureExtEphem<>
    --> ProcedureFormationFlyer<>
    --> ProcedureBasicPointToPoint<>
    --> ProcedureArcEnroute<>
    --> ProcedureArcPointToPoint<>
    --> ProcedureFlightLine<>
    --> ProcedureDelay<>
    --> ProcedureTakeoff<>
    --> ProcedureCollection<>
    --> Phase<>
    --> PhaseCollection<>
    --> Mission<>
    --> AviatorPropagator<>
    --> ProcedureBasicManeuver<>
    --> BasicManeuverStrategyWeave<>
    --> ProcedureTimeOptions<>
    --> CalculationOptions<>
    --> AircraftCategory<>
    --> Catalog<>
    --> AircraftModel<>
    --> MissileModel<>
    --> RotorcraftModel<>
    --> RotorcraftAero<>
    --> RotorcraftProp<>
    --> AircraftAcceleration<>
    --> AircraftBasicAccelerationModel<>
    --> AircraftClimb<>
    --> AircraftCruise<>
    --> AircraftDescent<>
    --> AircraftLanding<>
    --> AircraftTakeoff<>
    --> AircraftBasicClimbModel<>
    --> AircraftAdvancedClimbModel<>
    --> AircraftBasicCruiseModel<>
    --> AircraftAdvancedCruiseModel<>
    --> AircraftBasicDescentModel<>
    --> AircraftAdvancedDescentModel<>
    --> AircraftBasicTakeoffModel<>
    --> AircraftAdvancedTakeoffModel<>
    --> AircraftBasicLandingModel<>
    --> AircraftAdvancedLandingModel<>
    --> AirportCategory<>
    --> ARINC424Airport<>
    --> ARINC424Runway<>
    --> DAFIFRunway<>
    --> DAFIFHelipad<>
    --> DAFIFWaypoint<>
    --> RunwayCategory<>
    --> UserRunwaySource<>
    --> UserRunway<>
    --> AltitudeMSLOptions<>
    --> AltitudeOptions<>
    --> ArcAltitudeOptions<>
    --> ArcAltitudeAndDelayOptions<>
    --> ArcOptions<>
    --> AltitudeMSLAndLevelOffOptions<>
    --> CruiseAirspeedOptions<>
    --> CruiseAirspeedProfile<>
    --> CruiseAirspeedAndProfileOptions<>
    --> LandingCruiseAirspeedAndProfileOptions<>
    --> EnrouteOptions<>
    --> EnrouteAndDelayOptions<>
    --> LandingEnrouteOptions<>
    --> EnrouteTurnDirectionOptions<>
    --> NavigationOptions<>
    --> VerticalPlaneOptions<>
    --> ArcVerticalPlaneOptions<>
    --> VerticalPlaneAndFlightPathOptions<>
    --> LandingVerticalPlaneOptions<>
    --> RunwayHeadingOptions<>
    --> LandingEnterDownwindPattern<>
    --> LandingInterceptGlideslope<>
    --> LandingStandardInstrumentApproach<>
    --> TakeoffDeparturePoint<>
    --> TakeoffLowTransition<>
    --> TakeoffNormal<>
    --> LevelTurns<>
    --> AttitudeTransitions<>
    --> ClimbAndDescentTransitions<>
    --> AeroPropManeuverModeHelper<>
    --> AircraftAdvancedAccelerationModel<>
    --> AircraftAccelerationMode<>
    --> AircraftSimpleAero<>
    --> AircraftExternalAero<>
    --> AircraftAero<>
    --> AircraftBasicFixedWingAero<>
    --> AircraftProp<>
    --> AircraftSimpleProp<>
    --> AircraftExternalProp<>
    --> AircraftBasicFixedWingProp<>
    --> ARINC424Source<>
    --> DAFIFSource<>
    --> BasicFixedWingFwdFlightLiftHelper<>
    --> BasicManeuverStrategyStraightAhead<>
    --> BasicManeuverStrategyCruiseProfile<>
    --> BasicManeuverStrategyGlideProfile<>
    --> AircraftModels<>
    --> MissileModels<>
    --> RotorcraftModels<>
    --> Configuration<>
    --> FuelTankInternal<>
    --> FuelTankExternal<>
    --> PayloadStation<>
    --> StationCollection<>
    --> WindModel<>
    --> WindModelConstant<>
    --> WindModelADDS<>
    --> ADDSMessage<>
    --> ADDSMessageCollection<>
    --> Procedure<>
    --> AtmosphereModel<>
    --> AtmosphereModelBasic<>
    --> BasicManeuverStrategySimpleTurn<>
    --> BasicManeuverStrategyAileronRoll<>
    --> BasicManeuverStrategyFlyAOA<>
    --> BasicManeuverStrategyPull<>
    --> BasicManeuverStrategyRollingPull<>
    --> BasicManeuverStrategySmoothAccel<>
    --> BasicManeuverStrategySmoothTurn<>
    --> BasicManeuverAirspeedOptions<>
    --> PropulsionThrust<>
    --> BasicManeuverStrategyAutopilotNav<>
    --> BasicManeuverStrategyAutopilotProf<>
    --> BasicManeuverStrategyBarrelRoll<>
    --> BasicManeuverStrategyLoop<>
    --> BasicManeuverStrategyLTAHover<>
    --> BasicManeuverStrategyIntercept<>
    --> BasicManeuverStrategyRelativeBearing<>
    --> BasicManeuverStrategyRelativeCourse<>
    --> BasicManeuverStrategyRendezvous<>
    --> BasicManeuverStrategyStationkeeping<>
    --> BasicManeuverStrategyRelativeFPA<>
    --> BasicManeuverStrategyRelSpeedAltitude<>
    --> BasicManeuverStrategyBezier<>
    --> BasicManeuverStrategyPushPull<>
    --> ProcedureHoldingCircular<>
    --> ProcedureHoldingFigure8<>
    --> ProcedureHoldingRacetrack<>
    --> ProcedureTransitionToHover<>
    --> ProcedureTerrainFollow<>
    --> ProcedureHover<>
    --> ProcedureHoverTranslate<>
    --> ProcedureTransitionToForwardFlight<>
    --> HoverAltitudeOptions<>
    --> ProcedureVerticalTakeoff<>
    --> ProcedureVerticalLanding<>
    --> ProcedureReferenceState<>
    --> ProcedureSuperProcedure<>
    --> ProcedureLaunch<>
    --> ProcedureAirway<>
    --> ProcedureAirwayRouter<>
    --> ProcedureAreaTargetSearch<>
    --> ProcedureFormationRecover<>
    --> ProcedureInFormation<>
    --> ProcedureParallelFlightLine<>
    --> ProcedureVGTPoint<>
    --> PerformanceModelOptions<>
    --> AdvancedFixedWingTool<>
    --> AdvancedFixedWingExternalAero<>
    --> AdvancedFixedWingSubsonicAero<>
    --> AdvancedFixedWingSubSuperHypersonicAero<>
    --> AdvancedFixedWingSupersonicAero<>
    --> PerformanceModel<>
    --> AdvancedFixedWingGeometryBasic<>
    --> AdvancedFixedWingGeometryVariable<>
    --> AdvancedFixedWingElectricPowerplant<>
    --> AdvancedFixedWingExternalProp<>
    --> AdvancedFixedWingSubSuperHypersonicProp<>
    --> AdvancedFixedWingPistonPowerplant<>
    --> AdvancedFixedWingEmpiricalJetEngine<>
    --> AdvancedFixedWingTurbofanBasicABPowerplant<>
    --> AdvancedFixedWingTurbojetBasicABPowerplant<>
    --> AdvancedFixedWingTurbofanBasicABProp<>
    --> AdvancedFixedWingTurbojetBasicABProp<>
    --> AdvancedFixedWingTurbopropPowerplant<>
    --> MissileSimpleAero<>
    --> MissileExternalAero<>
    --> MissileAdvancedAero<>
    --> MissileAero<>
    --> MissileProp<>
    --> MissileSimpleProp<>
    --> MissileExternalProp<>
    --> MissileRamjetProp<>
    --> MissileRocketProp<>
    --> MissileTurbojetProp<>
    --> ReferenceStateForwardFlightOptions<>
    --> ReferenceStateTakeoffLandingOptions<>
    --> ReferenceStateHoverOptions<>
    --> ReferenceStateWeightOnWheelsOptions<>
    --> SiteRunwayFromCatalog<>
    --> SiteAirportFromCatalog<>
    --> SiteNavaidFromCatalog<>
    --> SiteVTOLPointFromCatalog<>
    --> SiteWaypointFromCatalog<>
    --> NavaidCategory<>
    --> VTOLPointCategory<>
    --> WaypointCategory<>
    --> ARINC424Navaid<>
    --> ARINC424Helipad<>
    --> ARINC424Waypoint<>
    --> UserVTOLPointSource<>
    --> UserVTOLPoint<>
    --> UserWaypointSource<>
    --> UserWaypoint<>
    --> PropulsionEfficiencies<>
    --> FuelModelKeroseneAFPROP<>
    --> FuelModelKeroseneCEA<>
    --> AdvancedFixedWingRamjetBasic<>
    --> AdvancedFixedWingScramjetBasic<>
    --> AircraftVTOLModel<>
    --> AircraftVTOL<>
    --> AircraftTerrainFollowModel<>
    --> AircraftTerrainFollow<>
    --> BasicManeuverStrategyBallistic3D<>
    --> ProcedureLaunchDynState<>
    --> ProcedureLaunchWaypoint<>
    --> SiteDynState<>
    --> BasicManeuverStrategyPitch3D<>
    --> RefuelDumpProperties<>
    --> ProcedureFastTimeOptions<>
    --> BasicManeuverTargetPositionVel<>
    --> BasicManeuverTargetPositionVelNoisyBrgRng<>
    --> BasicManeuverTargetPositionVelNoisySurfTgt<>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ ERROR_CODES<ERROR_CODES>
    ≔ CLOSURE_VALUE<CLOSURE_VALUE>
    ≔ PROCEDURE_TYPE<PROCEDURE_TYPE>
    ≔ SITE_TYPE<SITE_TYPE>
    ≔ BASIC_MANEUVER_STRATEGY<BASIC_MANEUVER_STRATEGY>
    ≔ STRAIGHT_AHEAD_REFERENCE_FRAME<STRAIGHT_AHEAD_REFERENCE_FRAME>
    ≔ AIRSPEED_TYPE<AIRSPEED_TYPE>
    ≔ AERO_PROP_SIMPLE_MODE<AERO_PROP_SIMPLE_MODE>
    ≔ AERO_PROP_FLIGHT_MODE<AERO_PROP_FLIGHT_MODE>
    ≔ PHASE_OF_FLIGHT<PHASE_OF_FLIGHT>
    ≔ CRUISE_SPEED<CRUISE_SPEED>
    ≔ TAKEOFF_MODE<TAKEOFF_MODE>
    ≔ APPROACH_MODE<APPROACH_MODE>
    ≔ NAVIGATOR_TURN_DIRECTION<NAVIGATOR_TURN_DIRECTION>
    ≔ BASIC_MANEUVER_FUEL_FLOW_TYPE<BASIC_MANEUVER_FUEL_FLOW_TYPE>
    ≔ BASIC_MANEUVER_ALTITUDE_LIMIT<BASIC_MANEUVER_ALTITUDE_LIMIT>
    ≔ RUNWAY_HIGH_LOW_END<RUNWAY_HIGH_LOW_END>
    ≔ BASIC_MANEUVER_REFERENCE_FRAME<BASIC_MANEUVER_REFERENCE_FRAME>
    ≔ BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT<BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT>
    ≔ ACCEL_MANEUVER_MODE<ACCEL_MANEUVER_MODE>
    ≔ AIRCRAFT_AERO_STRATEGY<AIRCRAFT_AERO_STRATEGY>
    ≔ AIRCRAFT_PROP_STRATEGY<AIRCRAFT_PROP_STRATEGY>
    ≔ AGL_MSL<AGL_MSL>
    ≔ LANDING_APPROACH_FIX_RANGE_MODE<LANDING_APPROACH_FIX_RANGE_MODE>
    ≔ ACCELERATION_ADVANCED_ACCEL_MODE<ACCELERATION_ADVANCED_ACCEL_MODE>
    ≔ ACCEL_MANEUVER_AERO_PROP_MODE<ACCEL_MANEUVER_AERO_PROP_MODE>
    ≔ BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS<BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS>
    ≔ BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE<BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE>
    ≔ TURN_MODE<TURN_MODE>
    ≔ POINT_TO_POINT_MODE<POINT_TO_POINT_MODE>
    ≔ ALTITUDE_CONSTRAINT_MANEUVER_MODE<ALTITUDE_CONSTRAINT_MANEUVER_MODE>
    ≔ WIND_MODEL_TYPE<WIND_MODEL_TYPE>
    ≔ WIND_ATMOS_MODEL_SOURCE<WIND_ATMOS_MODEL_SOURCE>
    ≔ ADDS_MSG_INTERP_TYPE<ADDS_MSG_INTERP_TYPE>
    ≔ ADDS_MISSING_MSG_TYPE<ADDS_MISSING_MSG_TYPE>
    ≔ ADDS_MSG_EXTRAP_TYPE<ADDS_MSG_EXTRAP_TYPE>
    ≔ ADDS_FORECAST_TYPE<ADDS_FORECAST_TYPE>
    ≔ ATMOSPHERE_MODEL<ATMOSPHERE_MODEL>
    ≔ SMOOTH_TURN_MODE<SMOOTH_TURN_MODE>
    ≔ PERF_MODEL_OVERRIDE<PERF_MODEL_OVERRIDE>
    ≔ BASIC_MANEUVER_AIRSPEED_MODE<BASIC_MANEUVER_AIRSPEED_MODE>
    ≔ AILERON_ROLL_FLIGHT_PATH<AILERON_ROLL_FLIGHT_PATH>
    ≔ ROLL_LEFT_RIGHT<ROLL_LEFT_RIGHT>
    ≔ ROLL_UPRIGHT_INVERTED<ROLL_UPRIGHT_INVERTED>
    ≔ AILERON_ROLL_MODE<AILERON_ROLL_MODE>
    ≔ FLY_AOA_LEFT_RIGHT<FLY_AOA_LEFT_RIGHT>
    ≔ SMOOTH_ACCEL_LEFT_RIGHT<SMOOTH_ACCEL_LEFT_RIGHT>
    ≔ PULL_MODE<PULL_MODE>
    ≔ ROLLING_PULL_MODE<ROLLING_PULL_MODE>
    ≔ SMOOTH_ACCEL_STOP_CONDITIONS<SMOOTH_ACCEL_STOP_CONDITIONS>
    ≔ AUTOPILOT_HORIZ_PLANE_MODE<AUTOPILOT_HORIZ_PLANE_MODE>
    ≔ ANGLE_MODE<ANGLE_MODE>
    ≔ HOVER_ALTITUDE_MODE<HOVER_ALTITUDE_MODE>
    ≔ HOVER_HEADING_MODE<HOVER_HEADING_MODE>
    ≔ AUTOPILOT_ALTITUDE_MODE<AUTOPILOT_ALTITUDE_MODE>
    ≔ AUTOPILOT_ALTITUDE_CONTROL_MODE<AUTOPILOT_ALTITUDE_CONTROL_MODE>
    ≔ CLOSURE_MODE<CLOSURE_MODE>
    ≔ INTERCEPT_MODE<INTERCEPT_MODE>
    ≔ RENDEZVOUS_STOP_CONDITION<RENDEZVOUS_STOP_CONDITION>
    ≔ FORMATION_FLYER_STOP_CONDITION<FORMATION_FLYER_STOP_CONDITION>
    ≔ EXT_EPHEM_FLIGHT_MODE<EXT_EPHEM_FLIGHT_MODE>
    ≔ ACCEL_PERF_MODEL_OVERRIDE<ACCEL_PERF_MODEL_OVERRIDE>
    ≔ STATIONKEEPING_STOP_CONDITION<STATIONKEEPING_STOP_CONDITION>
    ≔ TURN_DIRECTION<TURN_DIRECTION>
    ≔ PROFILE_CONTROL_LIMIT<PROFILE_CONTROL_LIMIT>
    ≔ REL_SPEED_ALTITUDE_STOP_CONDITION<REL_SPEED_ALTITUDE_STOP_CONDITION>
    ≔ RELATIVE_ALTITUDE_MODE<RELATIVE_ALTITUDE_MODE>
    ≔ FLY_TO_FLIGHT_PATH_ANGLE_MODE<FLY_TO_FLIGHT_PATH_ANGLE_MODE>
    ≔ PUSH_PULL<PUSH_PULL>
    ≔ ACCEL_MODE<ACCEL_MODE>
    ≔ DELAY_ALTITUDE_MODE<DELAY_ALTITUDE_MODE>
    ≔ JOIN_EXIT_ARC_METHOD<JOIN_EXIT_ARC_METHOD>
    ≔ FLIGHT_LINE_PROC_TYPE<FLIGHT_LINE_PROC_TYPE>
    ≔ TRANSITION_TO_HOVER_MODE<TRANSITION_TO_HOVER_MODE>
    ≔ VTOL_RATE_MODE<VTOL_RATE_MODE>
    ≔ HOLDING_PROFILE_MODE<HOLDING_PROFILE_MODE>
    ≔ HOLDING_DIRECTION<HOLDING_DIRECTION>
    ≔ HOLD_REFUEL_DUMP_MODE<HOLD_REFUEL_DUMP_MODE>
    ≔ HOLDING_ENTRY_MANEUVER<HOLDING_ENTRY_MANEUVER>
    ≔ VTOL_TRANSITION_MODE<VTOL_TRANSITION_MODE>
    ≔ VTOL_FINAL_HEADING_MODE<VTOL_FINAL_HEADING_MODE>
    ≔ VTOL_TRANSLATION_MODE<VTOL_TRANSLATION_MODE>
    ≔ VTOL_TRANSLATION_FINAL_COURSE_MODE<VTOL_TRANSLATION_FINAL_COURSE_MODE>
    ≔ HOVER_MODE<HOVER_MODE>
    ≔ VTOL_HEADING_MODE<VTOL_HEADING_MODE>
    ≔ VERT_LANDING_MODE<VERT_LANDING_MODE>
    ≔ LAUNCH_ATTITUDE_MODE<LAUNCH_ATTITUDE_MODE>
    ≔ FUEL_FLOW_TYPE<FUEL_FLOW_TYPE>
    ≔ LINE_ORIENTATION<LINE_ORIENTATION>
    ≔ REL_ABS_BEARING<REL_ABS_BEARING>
    ≔ BASIC_FIXED_WING_PROP_MODE<BASIC_FIXED_WING_PROP_MODE>
    ≔ CLIMB_SPEED_TYPE<CLIMB_SPEED_TYPE>
    ≔ CRUISE_MAX_PERF_SPEED_TYPE<CRUISE_MAX_PERF_SPEED_TYPE>
    ≔ DESCENT_SPEED_TYPE<DESCENT_SPEED_TYPE>
    ≔ TAKEOFF_LANDING_SPEED_MODE<TAKEOFF_LANDING_SPEED_MODE>
    ≔ DEPARTURE_SPEED_MODE<DEPARTURE_SPEED_MODE>
    ≔ ADVANCED_FIXED_WING_AERO_STRATEGY<ADVANCED_FIXED_WING_AERO_STRATEGY>
    ≔ ADVANCED_FIXED_WING_GEOMETRY<ADVANCED_FIXED_WING_GEOMETRY>
    ≔ ADVANCED_FIXED_WING_POWERPLANT_STRATEGY<ADVANCED_FIXED_WING_POWERPLANT_STRATEGY>
    ≔ MISSILE_AERO_STRATEGY<MISSILE_AERO_STRATEGY>
    ≔ MISSILE_PROP_STRATEGY<MISSILE_PROP_STRATEGY>
    ≔ ROTORCRAFT_POWERPLANT_TYPE<ROTORCRAFT_POWERPLANT_TYPE>
    ≔ MINIMIZE_SITE_PROC_TIME_DIFF<MINIMIZE_SITE_PROC_TIME_DIFF>
    ≔ STK_OBJECT_WAYPOINT_OFFSET_MODE<STK_OBJECT_WAYPOINT_OFFSET_MODE>
    ≔ SEARCH_PATTERN_COURSE_MODE<SEARCH_PATTERN_COURSE_MODE>
    ≔ DELAY_TURN_DIRECTION<DELAY_TURN_DIRECTION>
    ≔ TRAJECTORY_BLEND_MODE<TRAJECTORY_BLEND_MODE>
    ≔ REFERENCE_STATE_PERF_MODE<REFERENCE_STATE_PERF_MODE>
    ≔ REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE<REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE>
    ≔ REFERENCE_STATE_LATERAL_ACCEL_MODE<REFERENCE_STATE_LATERAL_ACCEL_MODE>
    ≔ REFERENCE_STATE_ATTITUDE_MODE<REFERENCE_STATE_ATTITUDE_MODE>
    ≔ AND_OR<AND_OR>
    ≔ JET_ENGINE_TECHNOLOGY_LEVEL<JET_ENGINE_TECHNOLOGY_LEVEL>
    ≔ JET_ENGINE_INTAKE_TYPE<JET_ENGINE_INTAKE_TYPE>
    ≔ JET_ENGINE_TURBINE_TYPE<JET_ENGINE_TURBINE_TYPE>
    ≔ JET_ENGINE_EXHAUST_NOZZLE_TYPE<JET_ENGINE_EXHAUST_NOZZLE_TYPE>
    ≔ JET_FUEL_TYPE<JET_FUEL_TYPE>
    ≔ AFPROP_FUEL_TYPE<AFPROP_FUEL_TYPE>
    ≔ CEA_FUEL_TYPE<CEA_FUEL_TYPE>
    ≔ TURBINE_MODE<TURBINE_MODE>
    ≔ RAMJET_MODE<RAMJET_MODE>
    ≔ SCRAMJET_MODE<SCRAMJET_MODE>
    ≔ NUMERICAL_INTEGRATOR<NUMERICAL_INTEGRATOR>
    ≔ BALLISTIC_3D_CONTROL_MODE<BALLISTIC_3D_CONTROL_MODE>
    ≔ LAUNCH_DYN_STATE_COORD_FRAME<LAUNCH_DYN_STATE_COORD_FRAME>
    ≔ LAUNCH_DYN_STATE_BEARING_REFERENCE<LAUNCH_DYN_STATE_BEARING_REFERENCE>
    ≔ ALTITUDE_REFERENCE<ALTITUDE_REFERENCE>
    ≔ SMOOTH_TURN_FPA_MODE<SMOOTH_TURN_FPA_MODE>
    ≔ PITCH_3D_CONTROL_MODE<PITCH_3D_CONTROL_MODE>
    ≔ REFUEL_DUMP_MODE<REFUEL_DUMP_MODE>
    ≔ BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE<BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE>
    ≔ TARGET_POSITION_VEL_TYPE<TARGET_POSITION_VEL_TYPE>
    ≔ EPHEM_SHIFT_ROTATE_ALTITUDE_MODE<EPHEM_SHIFT_ROTATE_ALTITUDE_MODE>
    ≔ EPHEM_SHIFT_ROTATE_COURSE_MODE<EPHEM_SHIFT_ROTATE_COURSE_MODE>

