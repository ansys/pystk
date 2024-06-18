
The ``aviator`` module
======================


.. py:module:: ansys.stk.core.stkobjects.aviator


Summary
-------

.. tab-set::
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ISite`
              - Interface to access Site options.

            * - :py:class:`~IWindModel`
              - Interface used to access the wind model for a mission, scenario, or procedure.

            * - :py:class:`~IADDSMessage`
              - Interface used to access a message from the NOAA ADDS forecast.

            * - :py:class:`~IFuelTankInternal`
              - Interface used to set an aircraft's internal fuel tank.

            * - :py:class:`~IFuelTankExternal`
              - Interface used to set an aircraft's external fuel tank.

            * - :py:class:`~IPayloadStation`
              - Interface used to set an aircraft's payload station.

            * - :py:class:`~IAircraftModel`
              - Interface used to access the aircraft options in the Aviator catalog.

            * - :py:class:`~IAircraftSimpleAero`
              - Interface used to access the Simple Aerodynamics options for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~ILevelTurns`
              - Interface used to access the Level Turns Transitions options found in the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAttitudeTransitions`
              - Interface used to access the Attitude Transitions options found in the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IClimbAndDescentTransitions`
              - Interface used to access the Climb and Descent Transitions options found in the Basic Acceleration Model of an aircraft.

            * - :py:class:`~ICatalogItem`
              - Interface used to access the options for a Catalog Item in the Aviator Catalog. Use this interface to Create, Remove, Duplicate, or Rename items in the catalog.

            * - :py:class:`~IAircraftBasicClimbModel`
              - Interface used to access the basic climb model options for a climb model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftBasicAccelerationModel`
              - Interface used to access the basic acceleration model options for an acceleration model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftCategory`
              - Interface used to access the Aircraft Category in the Aviator Catalog.

            * - :py:class:`~IRunwayCategory`
              - Interface used to access runways in the Aviator catalog.

            * - :py:class:`~IBasicManeuverStrategy`
              - Interface used to access options for a Basic Maneuver Strategy.

            * - :py:class:`~IAircraftVTOL`
              - Interface used to access the VTOL options for an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftExternalAero`
              - Interface used to access the External File Aerodynamics options for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftSimpleProp`
              - Interface used to access the Simple Propulsion options for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftExternalProp`
              - Interface used to access the External File Propulsion options for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftBasicFixedWingProp`
              - Interface used to access the Basic Fixed Wing Propulsion options for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftAdvancedClimbModel`
              - Interface used to access the advanced climb model options for a climb model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftBasicCruiseModel`
              - Interface used to access the basic cruise model options for a cruise model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftAdvancedCruiseModel`
              - Interface used to access the advanced cruise model options for a cruise model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftBasicDescentModel`
              - Interface used to access the basic descent model options for a descent model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftAdvancedDescentModel`
              - Interface used to access the advanced descent model options for a descent model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftBasicLandingModel`
              - Interface used to access the basic landing model options for a landing model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftAdvancedLandingModel`
              - Interface used to access the advanced landing model options for a landing model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftBasicTakeoffModel`
              - Interface used to access the basic takeoff model options for a takeoff model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftAdvancedTakeoffModel`
              - Interface used to access the advanced takeoff model options for a takeoff model of an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftVTOLModel`
              - Interface used to access the options for a VTOL performance model of an aircraft.

            * - :py:class:`~IAircraftTerrainFollow`
              - Interface used to access the TerrainFollow options for an aircraft in the Aviator catalog.

            * - :py:class:`~IPerformanceModelOptions`
              - Interface used to change the active performance model in a phase for a given model type.

            * - :py:class:`~IAdvancedFixedWingTool`
              - Interface used to access the options for the Advanced Fixed Wing Tool of an aircraft.

            * - :py:class:`~IAdvancedFixedWingExternalAero`
              - Interface used to access the options for an external file aerodynamic strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingSubsonicAero`
              - Interface used to access the options for the subsonic aerodynamic strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingSubSuperHypersonicAero`
              - Interface used to access the options for the Sub/Super/Hypersonic aerodynamic strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingSubSuperHypersonicProp`
              - Interface used to access the options for the Sub/Super/Hypersonic powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingSupersonicAero`
              - Interface used to access the options for the supersonic aerodynamic strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingGeometryBasic`
              - Interface used to access the options for a basic geometry wing in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingGeometryVariable`
              - Interface used to access the options for a variable geometry wing in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingElectricPowerplant`
              - Interface used to access the options for the Electric powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingExternalProp`
              - Interface used to access the options for the External Prop File powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingPistonPowerplant`
              - Interface used to access the options for the Piston powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingTurbopropPowerplant`
              - Interface used to access the options for the Turboprop powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingEmpiricalJetEngine`
              - Interface used to access the options for the Sub/Super/Hypersonic powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingTurbojetBasicABProp`
              - Interface used to access the options for the Turbojet - Basic w/AB (Thermodynamic) powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingTurbofanBasicABProp`
              - Interface used to access the options for the Turbofan - Basic w/AB (Thermodynamic) powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~IAviatorVehicle`
              - Interface for a vehicle in Aviator.

            * - :py:class:`~IMissileModel`
              - Interface used to access the missile options in the Aviator catalog.

            * - :py:class:`~IMissileAero`
              - Interface used to access the aerodynamics options for a missile.

            * - :py:class:`~IMissileProp`
              - Interface used to access the Propulsion options for a missile.

            * - :py:class:`~IMissileSimpleAero`
              - Interface used to access the Simple aerodynamics options for a missile.

            * - :py:class:`~IMissileSimpleProp`
              - Interface used to access the Simple propulsion options for a missile.

            * - :py:class:`~IMissileExternalAero`
              - Interface used to access the External aerodynamics options for a missile.

            * - :py:class:`~IMissileExternalProp`
              - Interface used to access the External Prop file options for a missile.

            * - :py:class:`~IMissileAdvancedAero`
              - Interface used to access the Advanced aerodynamics options for a missile.

            * - :py:class:`~IMissileRamjetProp`
              - Interface used to access the Ramjet propulsion options for a missile.

            * - :py:class:`~IMissileRocketProp`
              - Interface used to access the Rocket propulsion options for a missile.

            * - :py:class:`~IMissileTurbojetProp`
              - Interface used to access the Turbojet propulsion options for a missile.

            * - :py:class:`~IRotorcraftModel`
              - Interface used to access the rotorcraft options in the Aviator catalog.

            * - :py:class:`~IRotorcraftAero`
              - Interface used to access the aerodynamics options for a rotorcraft.

            * - :py:class:`~IRotorcraftProp`
              - Interface used to access the Propulsion options for a rotorcraft.

            * - :py:class:`~IUserRunwaySource`
              - Interface used to access the user runways in the Aviator catalog.

            * - :py:class:`~IUserRunway`
              - Interface used to access a user runway in the Aviator catalog.

            * - :py:class:`~IARINC424Item`
              - Interface used to access the options for an ARINC424 Item found in the Aviator catalog.

            * - :py:class:`~IARINC424Source`
              - Interface used to access the options for any ARINC424 source in the Aviator catalog.

            * - :py:class:`~IDAFIFSource`
              - Interface used to access the options for any DAFIF source in the Aviator catalog.

            * - :py:class:`~IUserVTOLPoint`
              - Interface used to access a user VTOL Point in the Aviator catalog.

            * - :py:class:`~IUserVTOLPointSource`
              - Interface used to access the user VTOL Points in the Aviator catalog.

            * - :py:class:`~IUserWaypoint`
              - Interface used to access a user waypoint in the Aviator catalog.

            * - :py:class:`~IUserWaypointSource`
              - Interface used to access the user waypoints in the Aviator catalog.

            * - :py:class:`~IPropulsionEfficiencies`
              - Interface used to access the options for the Efficiencies and Losses of a jet engine powerplant in the advanced fixed wing tool.

            * - :py:class:`~IFuelModelKeroseneAFPROP`
              - Interface used to access the options for Kerosense - CEA fuel for a thermodynamic a jet engine model.

            * - :py:class:`~IFuelModelKeroseneCEA`
              - Interface used to access the options for Kerosense - CEA fuel for a thermodynamic a jet engine model.

            * - :py:class:`~IAdvancedFixedWingRamjetBasic`
              - Interface used to access the options for a basic Ramjet mode.

            * - :py:class:`~IAdvancedFixedWingScramjetBasic`
              - Interface used to access the options for a basic Scramjet mode.

            * - :py:class:`~IRefuelDumpProperties`
              - Interface used to access the refuel/dump properties for the current procedure.

            * - :py:class:`~IProcedureFastTimeOptions`
              - Interface used to access the fast time options (without error or constraint checks) for the current procedure. Use this interface to set an Interrupt Time or Fixed Duration for a procedure.

            * - :py:class:`~IAtmosphereModelBasic`
              - Interface used to access the basic atmosphere model.

            * - :py:class:`~IAtmosphereModel`
              - Interface used to access the atmosphere model for a mission, scenario, or procedure.

            * - :py:class:`~IADDSMessageCollection`
              - Interface used to access the collection of messages from the NOAA ADDS forecast.

            * - :py:class:`~IWindModelADDS`
              - Interface used to access the options for a NOAA ADDS wind model.

            * - :py:class:`~IWindModelConstant`
              - Interface used to access the options for a Constant Bearing/Speed wind model.

            * - :py:class:`~IStation`
              - Interface used to access a station for an Aviator aircraft.

            * - :py:class:`~IStationCollection`
              - Interface used to access the list of stations for an Aviator aircraft.

            * - :py:class:`~IConfiguration`
              - Interface used to change an aircraft's configuration for an Aviator mission.

            * - :py:class:`~ICatalogSource`
              - Interface used to access options for a source in the Aviator Catalog. Examples of sources include User Aircraft Models, ARINC424runways, User Runways, etc.

            * - :py:class:`~IAircraftModels`
              - Interface for the User Aircraft Models in the Aviator Catalog.

            * - :py:class:`~IMissileModels`
              - Interface for the User Missile Models in the Aviator Catalog.

            * - :py:class:`~IRotorcraftModels`
              - Interface for the User Rotorcraft Models in the Aviator Catalog.

            * - :py:class:`~IBasicFixedWingLiftHelper`
              - Interface used to access Lift Coefficient Helper in the Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftBasicFixedWingAero`
              - Interface used to access Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftAero`
              - Interface used to access the Aerodynamics options for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftProp`
              - Interface used to access the propulsion options for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftAccelerationMode`
              - Interface used to set the Acceleration Mode for the Advanced Acceleration Model of an aircraft.

            * - :py:class:`~IAircraftAdvancedAccelerationModel`
              - Interface used to access the Advanced Acceleration Model options of an aircraft.

            * - :py:class:`~IAeroPropManeuverModeHelper`
              - Interface used to access the The calculation mode for the Aero/Prop maneuver mode helper. Helper found in the Basic Acceleration Model of an aircraft.

            * - :py:class:`~ICatalogRunway`
              - Interface used to access a runway in the Aviator catalog.

            * - :py:class:`~ICatalogAirport`
              - Interface used to access a airport in the Aviator catalog.

            * - :py:class:`~ICatalogNavaid`
              - Interface used to access a navaid in the Aviator catalog.

            * - :py:class:`~ICatalogVTOLPoint`
              - Interface used to access a VTOL Point in the Aviator catalog.

            * - :py:class:`~ICatalogWaypoint`
              - Interface used to access a waypoint in the Aviator catalog.

            * - :py:class:`~IARINC424Airport`
              - Do not use this interface, as it is deprecated. Use IAgAvtrARINC424Item instead.

            * - :py:class:`~IDAFIFItem`
              - Interface used to access the options for an DAFIF Item found in the Aviator catalog.

            * - :py:class:`~IARINC424Runway`
              - Do not use this interface, as it is deprecated. Use IAgAvtrARINC424Item instead.

            * - :py:class:`~IAirportCategory`
              - Interface used to access the airports in the Aviator catalog.

            * - :py:class:`~INavaidCategory`
              - Interface used to access the navaids in the Aviator catalog.

            * - :py:class:`~IVTOLPointCategory`
              - Interface used to access the VTOL Points in the Aviator catalog.

            * - :py:class:`~IWaypointCategory`
              - Interface used to access the waypoints in the Aviator catalog.

            * - :py:class:`~IAircraftClimb`
              - Interface used to access the climb options for an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftCruise`
              - Interface used to access the cruise options for an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftDescent`
              - Interface used to access the descent options for an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftLanding`
              - Interface used to access the landing options for an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftTakeoff`
              - Interface used to access the takeoff options for an aircraft in the Aviator catalog.

            * - :py:class:`~IAircraftAcceleration`
              - Interface used to access the acceleration options for an aircraft in the Aviator catalog.

            * - :py:class:`~ICatalog`
              - Interface used to access the Aviator catalog.

            * - :py:class:`~IProcedureTimeOptions`
              - Interface used to access the time options for the current procedure. Use this interface to set an Interrupt Time or Fixed Duration for a procedure.

            * - :py:class:`~ICalculationOptions`
              - Interface used to access the calculation options for a procedure or phase.

            * - :py:class:`~INavigationOptions`
              - Interface used to access the navigation options for an Aviator procedure.

            * - :py:class:`~IAltitudeMSLAndLevelOffOptions`
              - Interface used to access the altitude MSL and Level off options for an Aviator procedure.

            * - :py:class:`~IAltitudeMSLOptions`
              - Interface used to access the altitude MSL options for an Aviator procedure.

            * - :py:class:`~IAltitudeOptions`
              - Interface used to access the altitude options for an Aviator procedure.

            * - :py:class:`~IHoverAltitudeOptions`
              - Interface used to access the altitude options for VTOL procedure.

            * - :py:class:`~IArcAltitudeOptions`
              - Interface used to access the altitude options for an Arc procedure.

            * - :py:class:`~IArcAltitudeAndDelayOptions`
              - Interface used to access the altitude options for an Arc procedure.

            * - :py:class:`~IArcOptions`
              - Interface used to access the arc options for a procedure.

            * - :py:class:`~IVerticalPlaneOptions`
              - Interface used to access the Vertical Plane options for an Aviator procedure.

            * - :py:class:`~IVerticalPlaneAndFlightPathOptions`
              - Interface used to access the Vertical Plane and Final Flight Path Angle options for an Aviator procedure.

            * - :py:class:`~IArcVerticalPlaneOptions`
              - Interface used to access the Vertical Plane options for an arc procedure.

            * - :py:class:`~IEnrouteOptions`
              - Interface used to access the Enroute options for an Aviator procedure.

            * - :py:class:`~IEnrouteAndDelayOptions`
              - Interface used to access the Enroute options for an Aviator procedure.

            * - :py:class:`~IEnrouteTurnDirectionOptions`
              - Interface used to access the Enroute Turn Direction options for an Aviator procedure.

            * - :py:class:`~ICruiseAirspeedOptions`
              - Interface used to access the Cruise Airspeed options for an Aviator procedure.

            * - :py:class:`~ICruiseAirspeedProfile`
              - Interface used to access the Cruise Profile options for an Aviator procedure.

            * - :py:class:`~ICruiseAirspeedAndProfileOptions`
              - Interface used to access the cruise airspeed options that also include a profile field.

            * - :py:class:`~IAutomationStrategyFactory`
              - Interface used to send connect commands to Aviator objects.

            * - :py:class:`~IConnect`
              - Interface used to send connect commands to Aviator objects.

            * - :py:class:`~IRunwayHeadingOptions`
              - Interface for the Runway Heading Options found in a Takeoff or Landing procedure.

            * - :py:class:`~IProcedure`
              - Interface used to access the options for a procedure. Use this interface to get the Site and Get the time options for the current procedure.

            * - :py:class:`~IProcedureCollection`
              - Interface used to access the collection of procedures for a given phase in a mission. Use this interface to Get, Add, or Remove a procedure.

            * - :py:class:`~IPhase`
              - Interface used to access the phase options for a mission.

            * - :py:class:`~IPhaseCollection`
              - Interface used to access the collection of phases for a mission.

            * - :py:class:`~IMission`
              - Interface for the mission of an aircraft using the Aviator propagator.

            * - :py:class:`~IAviatorPropagator`
              - Interface used to access the Aviator interface for an aircraft. Use this interface to get the mission or Aviator catalog.

            * - :py:class:`~IPerformanceModel`
              - Interface for a performance model of an Aviator vehicle.

            * - :py:class:`~IAdvancedFixedWingGeometry`
              - Interface used to access the options for the wing geometry in the advanced fixed wing tool.

            * - :py:class:`~IAdvancedFixedWingTurbofanBasicABPowerplant`
              - Do not use this interface, as it is deprecated. Use IAgAvtrAdvFixedWingTurbofanBasicABProp instead.

            * - :py:class:`~IAdvancedFixedWingTurbojetBasicABPowerplant`
              - Do not use this interface, as it is deprecated. Use IAgAvtrAdvFixedWingTurbojetBasicABProp instead.

            * - :py:class:`~IAdvancedFixedWingPowerplant`
              - Interface for a powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~ISiteUnknown`
              - Interface of an unknown site.

            * - :py:class:`~IAircraftTerrainFollowModel`
              - Interface used to access the options for a TerrainFollow performance model of an aircraft.

            * - :py:class:`~IBasicManeuverTargetPositionVel`
              - Interface used to access target position and velocity strategies for basic maneuvers.

            * - :py:class:`~IPropulsionThrust`
              - Interface used to access propulsion thrust for basic maneuver strategies.

            * - :py:class:`~IBasicManeuverAirspeedOptions`
              - Interface used to access airspeed options for basic maneuver strategies.

            * - :py:class:`~IBasicManeuverStrategyAileronRoll`
              - Interface used to access options for a Aileron Roll Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyAutopilotNav`
              - Interface used to access options for the Autopilot - Horizontal Plane Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyAutopilotProf`
              - Interface used to access options for the Autopilot - Vertical Plane Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyBarrelRoll`
              - Interface used to access options for a Barrel Roll Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyLoop`
              - Interface used to access options for a Loop Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyLTAHover`
              - Interface used to access options for a Lighter than Air Hover Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyFlyAOA`
              - Interface used to access options for a Fly AOA Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyPull`
              - Interface used to access options for a Pull Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyRollingPull`
              - Interface used to access options for a Rolling Pull Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategySmoothAccel`
              - Interface used to access options for a Smooth Accel Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategySmoothTurn`
              - Interface used to access options for a Smooth Turn Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategySimpleTurn`
              - Interface used to access options for a Simple Turn Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyIntercept`
              - Interface used to access options for an Intercept Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyRelativeBearing`
              - Interface used to access options for a Relative Bearing Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyRelativeCourse`
              - Interface used to access options for a Relative Course Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyRendezvous`
              - Interface used to access options for a Rendezvous Formation Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyStationkeeping`
              - Interface used to access options for a Stationkeeping Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyRelativeFPA`
              - Interface used to access options for the Relative Flight Path Angle Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyRelSpeedAltitude`
              - Interface used to access options for a Relative Speed/Altitude Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyBezier`
              - Interface used to access options for a Bezier Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyPushPull`
              - Interface used to access options for a Push/Pull Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyGlideProfile`
              - Interface used to access options for a Glide Profile Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyCruiseProfile`
              - Interface used to access options for a Cruise Profile Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyStraightAhead`
              - Interface used to access options for a Straight Ahead Strategy of a Basic Maneuver Procedure.

            * - :py:class:`~IBasicManeuverStrategyWeave`
              - Interface used to access options for a weave strategy of a basic maneuver procedure.

            * - :py:class:`~IBasicManeuverStrategyBallistic3D`
              - Interface used to access options for a balistic 3D strategy of a basic maneuver procedure.

            * - :py:class:`~IBasicManeuverStrategyPitch3D`
              - Interface used to access options for a pitch 3D strategy of a basic maneuver procedure.

            * - :py:class:`~IBasicManeuverTargetPositionVelNoisyBrgRng`
              - Interface used to access target position and velocity strategy, NoisyBrnRng.

            * - :py:class:`~IBasicManeuverTargetPositionVelNoisySurfTgt`
              - Interface used to access target position and velocity strategy, Surf Tgt Pos Vel.

            * - :py:class:`~ITakeoffNormal`
              - The interface used to access the options for a Normal takeoff mode. The mode must be set to Normal to access this interface.

            * - :py:class:`~ITakeoffDeparturePoint`
              - The interface used to access the options for a Departure Point takeoff mode. The mode must be set to Departure Point to access this interface.

            * - :py:class:`~ITakeoffLowTransition`
              - The interface used to access the options for a Low Transition takeoff mode. The mode must be set to Low Transition to access this interface.

            * - :py:class:`~IReferenceStateForwardFlightOptions`
              - Interface used to access the forward flight options for a reference state procedure.

            * - :py:class:`~IReferenceStateHoverOptions`
              - Interface used to access the hover options for a reference state procedure.

            * - :py:class:`~IReferenceStateWeightOnWheelsOptions`
              - Interface used to access the weight on wheels options for a reference state procedure.

            * - :py:class:`~IReferenceStateTakeoffLandingOptions`
              - Interface used to access the takeoff or landing options for a reference state procedure.

            * - :py:class:`~ILandingEnterDownwindPattern`
              - The interface used to access the options for a Downwind Pattern approach mode for a landing procedure. The approach mode must be set to Downwind Pattern to access this interface.

            * - :py:class:`~ILandingInterceptGlideslope`
              - The interface used to access the options for an Intercept Glideslope approach mode for a landing procedure. The approach mode must be set to Intercept Glideslope to access this interface.

            * - :py:class:`~ILandingStandardInstrumentApproach`
              - The interface used to access the options for a Standard Instrument Approach mode for a landing procedure. The approach mode must be set to Standard Instrument Approach to access this interface.

            * - :py:class:`~IProcedureBasicManeuver`
              - Interface used to access the options for a Basic Maneuver procedure.

            * - :py:class:`~ISiteWaypoint`
              - Interface used to access the options for a waypoint site.

            * - :py:class:`~ISiteEndOfPrevProcedure`
              - Interface used to access the options for an End of Previous Procedure site type.

            * - :py:class:`~ISiteVTOLPoint`
              - Interface used to access the options for a VTOL Point site.

            * - :py:class:`~ISiteSTKVehicle`
              - Interface used to access the options for a STK Vehicle site.

            * - :py:class:`~ISiteReferenceState`
              - Interface used to access the options for a Reference State site.

            * - :py:class:`~ISiteSuperProcedure`
              - Interface used to access the options for a Super Procedure site.

            * - :py:class:`~ISiteRelToPrevProcedure`
              - Interface used to access the options for a Relative to Previous Procedure site.

            * - :py:class:`~ISiteSTKObjectWaypoint`
              - Interface used to access the options for a STK Object Waypoint site.

            * - :py:class:`~ISiteSTKStaticObject`
              - Interface used to access the options for a STK Static Object site.

            * - :py:class:`~ISiteRelToSTKObject`
              - Interface used to access the options for a Relative to Stationary STK Object site.

            * - :py:class:`~ISiteSTKAreaTarget`
              - Interface used to access the options for a STK Area Target site.

            * - :py:class:`~ISiteRunway`
              - Interface used to access the options for a Runway site type.

            * - :py:class:`~IProcedureLanding`
              - Interface used to access the options for a landing procedure.

            * - :py:class:`~IProcedureEnroute`
              - Interface used to access the options for an enroute procedure.

            * - :py:class:`~IProcedureExtEphem`
              - Interface used to access the options for an ExtEphem procedure.

            * - :py:class:`~IProcedureFormationFlyer`
              - Interface used to access the options for an enroute procedure.

            * - :py:class:`~IProcedureBasicPointToPoint`
              - Interface used to access the options for a basic point to point procedure.

            * - :py:class:`~IProcedureDelay`
              - Interface used to access the options for a delay procedure.

            * - :py:class:`~IProcedureTakeoff`
              - Interface used to access the options for a takeoff procedure.

            * - :py:class:`~IProcedureArcEnroute`
              - Interface used to access the options for an arc enroute procedure.

            * - :py:class:`~IProcedureArcPointToPoint`
              - Interface used to access the options for an arc point to point procedure.

            * - :py:class:`~IProcedureFlightLine`
              - Interface used to access the options for a flight line procedure.

            * - :py:class:`~IProcedureHoldingCircular`
              - Interface used to access the options for a holding circular procedure.

            * - :py:class:`~IProcedureHoldingFigure8`
              - Interface used to access the options for a holding figure 8 procedure.

            * - :py:class:`~IProcedureHoldingRacetrack`
              - Interface used to access the options for a holding racetrack procedure.

            * - :py:class:`~IProcedureTransitionToHover`
              - Interface used to access the options for a transition to hover procedure.

            * - :py:class:`~IProcedureTerrainFollow`
              - Interface used to access the options for a terrain following procedure.

            * - :py:class:`~IProcedureHover`
              - Interface used to access the options for a hover procedure.

            * - :py:class:`~IProcedureHoverTranslate`
              - Interface used to access the options for a hover translate procedure.

            * - :py:class:`~IProcedureTransitionToForwardFlight`
              - Interface used to access the options for a transition to forward flight procedure.

            * - :py:class:`~IProcedureVerticalTakeoff`
              - Interface used to access the options for a vertical takeoff procedure.

            * - :py:class:`~IProcedureVerticalLanding`
              - Interface used to access the options for a vertical landing procedure.

            * - :py:class:`~IProcedureReferenceState`
              - Interface used to access the options for a reference state procedure.

            * - :py:class:`~IProcedureSuperProcedure`
              - Interface used to access the options for a super procedure.

            * - :py:class:`~IProcedureLaunch`
              - Interface used to access the options for a launch procedure.

            * - :py:class:`~IProcedureAirway`
              - Interface used to access the options for an Airway procedure.

            * - :py:class:`~IProcedureAirwayRouter`
              - Interface used to access the options for an Airway Router procedure.

            * - :py:class:`~IProcedureAreaTargetSearch`
              - Interface used to access the options for an Area Target Search procedure.

            * - :py:class:`~IProcedureFormationRecover`
              - Interface used to access the options for a Formation Recover procedure.

            * - :py:class:`~IProcedureInFormation`
              - Interface used to access the options for an In Formation procedure.

            * - :py:class:`~IProcedureParallelFlightLine`
              - Interface used to access the options for a Parallel Flight Line procedure.

            * - :py:class:`~IProcedureVGTPoint`
              - Interface used to access the options for a VGT Point procedure.

            * - :py:class:`~ISiteRunwayFromCatalog`
              - Interface used to access the options for a Runway From Catalog site type.

            * - :py:class:`~ISiteAirportFromCatalog`
              - Interface used to access the options for a airport From Catalog site type.

            * - :py:class:`~ISiteNavaidFromCatalog`
              - Interface used to access the options for a navaid From Catalog site type.

            * - :py:class:`~ISiteVTOLPointFromCatalog`
              - Interface used to access the options for a VTOL Point From Catalog site type.

            * - :py:class:`~ISiteWaypointFromCatalog`
              - Interface used to access the options for a waypoint From Catalog site type.

            * - :py:class:`~IProcedureLaunchDynState`
              - Interface used to access the options for a dyn state launch procedure.

            * - :py:class:`~IProcedureLaunchWaypoint`
              - Interface used to access the options for a waypoint launch procedure.

            * - :py:class:`~ISiteDynState`
              - Interface used to access the options for a dyn state site type.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~SiteWaypoint`
              - Class defining a waypoint site.

            * - :py:class:`~SiteEndOfPrevProcedure`
              - Class defining an End of Previous Procedure site.

            * - :py:class:`~SiteVTOLPoint`
              - Class defining a VTOL Point site.

            * - :py:class:`~SiteReferenceState`
              - Class defining a Reference State site.

            * - :py:class:`~SiteSTKVehicle`
              - Class defining a STK Vehicle site.

            * - :py:class:`~SiteSuperProcedure`
              - Class defining a Super Procedure site.

            * - :py:class:`~SiteRelToPrevProcedure`
              - Class defining a Relative to Previous Procedure site.

            * - :py:class:`~SiteSTKObjectWaypoint`
              - Class defining a STK Object Waypoint site.

            * - :py:class:`~SiteSTKStaticObject`
              - Class defining a STK Static Object site.

            * - :py:class:`~SiteRelToSTKObject`
              - Class defining a Relative to Stationary STK Object site.

            * - :py:class:`~SiteSTKAreaTarget`
              - Class defining a STK Area Target site.

            * - :py:class:`~SiteRunway`
              - Class defining a runway site.

            * - :py:class:`~Site`
              - Class defining an unknown site type.

            * - :py:class:`~ProcedureLanding`
              - Class defining a landing procedure.

            * - :py:class:`~ProcedureEnroute`
              - Class defining an enroute procedure.

            * - :py:class:`~ProcedureExtEphem`
              - Class defining an ExtEphem procedure.

            * - :py:class:`~ProcedureFormationFlyer`
              - Class defining an formationflyer procedure.

            * - :py:class:`~ProcedureBasicPointToPoint`
              - Class defining a basic point to point procedure.

            * - :py:class:`~ProcedureArcEnroute`
              - Class defining a arc enroute procedure.

            * - :py:class:`~ProcedureArcPointToPoint`
              - Class defining a arc point to point procedure.

            * - :py:class:`~ProcedureFlightLine`
              - Class defining a flight line procedure.

            * - :py:class:`~ProcedureDelay`
              - Class defining a delay procedure.

            * - :py:class:`~ProcedureTakeoff`
              - Class defining a takeoff procedure.

            * - :py:class:`~ProcedureCollection`
              - Class defining the collection of procedures in the phase of an Aviator mission.

            * - :py:class:`~Phase`
              - Class defining a phase in an Aviator mission.

            * - :py:class:`~PhaseCollection`
              - Class defining the collection of phases.

            * - :py:class:`~Mission`
              - Class defining the Aviator mission.

            * - :py:class:`~AviatorPropagator`
              - Class defining the Aviator propagator.

            * - :py:class:`~ProcedureBasicManeuver`
              - Class defining a Basic Maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyWeave`
              - Class defining Weave strategy for a Basic Maneuver procedure.

            * - :py:class:`~ProcedureTimeOptions`
              - Class defining the time options for the current procedure.

            * - :py:class:`~CalculationOptions`
              - Class defining the calculation options for a procedure or phase.

            * - :py:class:`~AircraftCategory`
              - Class defining the aircraft category in the Aviator catalog.

            * - :py:class:`~Catalog`
              - Class defining the Aviator Catalog.

            * - :py:class:`~AircraftModel`
              - Class defining an aircraft in Aviator.

            * - :py:class:`~MissileModel`
              - Class defining a missile in Aviator.

            * - :py:class:`~RotorcraftModel`
              - Class defining a rotorcraft in Aviator.

            * - :py:class:`~RotorcraftAero`
              - Class defining the aerodynamic options for a rotorcraft.

            * - :py:class:`~RotorcraftProp`
              - Class defining the propulsion options for a rotorcraft.

            * - :py:class:`~AircraftAcceleration`
              - Class defining the aircraft acceleration category of an Aviator aircraft.

            * - :py:class:`~AircraftBasicAccelerationModel`
              - Class defining the basic acceleration performance model for an Aviator aircraft.

            * - :py:class:`~AircraftClimb`
              - Class defining the aircraft climb category of an Aviator aircraft.

            * - :py:class:`~AircraftCruise`
              - Class defining the aircraft cruise category of an Aviator aircraft.

            * - :py:class:`~AircraftDescent`
              - Class defining the aircraft descent category of an Aviator aircraft.

            * - :py:class:`~AircraftLanding`
              - Class defining the aircraft landing category of an Aviator aircraft.

            * - :py:class:`~AircraftTakeoff`
              - Class defining the aircraft takeoff category of an Aviator aircraft.

            * - :py:class:`~AircraftBasicClimbModel`
              - Class defining the basic climb performance model for an Aviator aircraft.

            * - :py:class:`~AircraftAdvancedClimbModel`
              - Class defining the advanced climb performance model for an Aviator aircraft.

            * - :py:class:`~AircraftBasicCruiseModel`
              - Class defining the basic cruise performance model for an Aviator aircraft.

            * - :py:class:`~AircraftAdvancedCruiseModel`
              - Class defining the advanced cruise performance model for an Aviator aircraft.

            * - :py:class:`~AircraftBasicDescentModel`
              - Class defining the basic descent performance model for an Aviator aircraft.

            * - :py:class:`~AircraftAdvancedDescentModel`
              - Class defining the advanced descent performance model for an Aviator aircraft.

            * - :py:class:`~AircraftBasicTakeoffModel`
              - Class defining the basic takeoff performance model for an Aviator aircraft.

            * - :py:class:`~AircraftAdvancedTakeoffModel`
              - Class defining the advanced takeoff performance model for an Aviator aircraft.

            * - :py:class:`~AircraftBasicLandingModel`
              - Class defining the basic landing performance model for an Aviator aircraft.

            * - :py:class:`~AircraftAdvancedLandingModel`
              - Class defining the advanced landing performance model for an Aviator aircraft.

            * - :py:class:`~AirportCategory`
              - Class defining the airport category in the Aviator catalog.

            * - :py:class:`~ARINC424Airport`
              - Class defining an ARINC424 Airport.

            * - :py:class:`~ARINC424Runway`
              - Class defining an ARINC424 Runway.

            * - :py:class:`~DAFIFRunway`
              - Class defining an DAFIF Runway.

            * - :py:class:`~DAFIFHelipad`
              - Class defining an DAFIF Helipad.

            * - :py:class:`~DAFIFWaypoint`
              - Class defining an DAFIF Waypoint.

            * - :py:class:`~RunwayCategory`
              - Class defining the runway category in the Aviator catalog.

            * - :py:class:`~UserRunwaySource`
              - Class defining the user runways in the Aviator catalog.

            * - :py:class:`~UserRunway`
              - Class defining the user runway in the Aviator catalog.

            * - :py:class:`~AltitudeMSLOptions`
              - Class defining the altitude MSL options in a procedure.

            * - :py:class:`~AltitudeOptions`
              - Class defining the altitude options in a procedure.

            * - :py:class:`~ArcAltitudeOptions`
              - Class defining the altitude options for an arc procedure.

            * - :py:class:`~ArcAltitudeAndDelayOptions`
              - Class defining the altitude and delay options for an arc procedure.

            * - :py:class:`~ArcOptions`
              - Class defining the arc options for a procedure.

            * - :py:class:`~AltitudeMSLAndLevelOffOptions`
              - Class defining the altitude MSL and Level off options in a procedure.

            * - :py:class:`~CruiseAirspeedOptions`
              - Class defining the cruise airspeed options in a procedure.

            * - :py:class:`~CruiseAirspeedProfile`
              - Class defining the cruise profile options in a procedure.

            * - :py:class:`~CruiseAirspeedAndProfileOptions`
              - Class defining the cruise airspeed and profile options in a procedure.

            * - :py:class:`~LandingCruiseAirspeedAndProfileOptions`
              - Class defining the cruise airspeed and profile options for a landing procedure.

            * - :py:class:`~EnrouteOptions`
              - Class defining the enroute options in a procedure.

            * - :py:class:`~EnrouteAndDelayOptions`
              - Class defining the enroute and delay options in a procedure.

            * - :py:class:`~LandingEnrouteOptions`
              - Class defining the enroute options in a landing procedure.

            * - :py:class:`~EnrouteTurnDirectionOptions`
              - Class defining the enroute turn direction options in a procedure.

            * - :py:class:`~NavigationOptions`
              - Class defining the navigation options in a procedure.

            * - :py:class:`~VerticalPlaneOptions`
              - Class defining the vertical plane options in a procedure.

            * - :py:class:`~ArcVerticalPlaneOptions`
              - Class defining the vertical plane options in a procedure.

            * - :py:class:`~VerticalPlaneAndFlightPathOptions`
              - Class defining the vertical plane options for an arc procedure.

            * - :py:class:`~LandingVerticalPlaneOptions`
              - Class defining the vertical plane options in a landing procedure.

            * - :py:class:`~RunwayHeadingOptions`
              - Class defining the runway heading options in a takeoff or landing procedure.

            * - :py:class:`~LandingEnterDownwindPattern`
              - Class defining the enter downwind pattern options for a landing procedure.

            * - :py:class:`~LandingInterceptGlideslope`
              - Class defining the intercept glideslope options for a landing procedure.

            * - :py:class:`~LandingStandardInstrumentApproach`
              - Class defining the standard instrument approach options for a landing procedure.

            * - :py:class:`~TakeoffDeparturePoint`
              - Class defining the departure point options for a takeoff procedure.

            * - :py:class:`~TakeoffLowTransition`
              - Class defining the low transition options for a takeoff procedure.

            * - :py:class:`~TakeoffNormal`
              - Class defining the normal options for a takeoff procedure.

            * - :py:class:`~LevelTurns`
              - Class defining the level turns options for an acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AttitudeTransitions`
              - Class defining the attitude transition options for an acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ClimbAndDescentTransitions`
              - Class defining the climb and descent transition options for an Acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AeroPropManeuverModeHelper`
              - Class defining the The calculation mode for the Aero/Prop maneuver mode helper. Helper for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftAdvancedAccelerationModel`
              - Class defining the advanced acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftAccelerationMode`
              - Class defining the acceleration mode options for an advanced acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftSimpleAero`
              - Class defining the simple aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftExternalAero`
              - Class defining the external file aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftAero`
              - Class defining the aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftBasicFixedWingAero`
              - Class defining the basic fixed wing aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftProp`
              - Class defining the propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftSimpleProp`
              - Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftExternalProp`
              - Class defining the external propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~AircraftBasicFixedWingProp`
              - Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ARINC424Source`
              - Class defining an ARINC424 source in the Aviator catalog.

            * - :py:class:`~DAFIFSource`
              - Class defining an DAFIF source in the Aviator catalog.

            * - :py:class:`~BasicFixedWingFwdFlightLiftHelper`
              - Class defining the Lift Coefficient Helper for Forward Flight in the Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~BasicManeuverStrategyStraightAhead`
              - Class defining the Straight Ahead strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyCruiseProfile`
              - Class defining the Cruise profile strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyGlideProfile`
              - Class defining the Glide profile strategy for a basic maneuver procedure.

            * - :py:class:`~AircraftModels`
              - Class defining the User Aircraft Models in the Aviator Catalog.

            * - :py:class:`~MissileModels`
              - Class defining the User Missile Models in the Aviator Catalog.

            * - :py:class:`~RotorcraftModels`
              - Class defining the User Rotorcraft Models in the Aviator Catalog.

            * - :py:class:`~Configuration`
              - Class defining the aircraft configuration for an Aviator mission.

            * - :py:class:`~FuelTankInternal`
              - Class defining an internal fuel tank for an Aviator aircraft.

            * - :py:class:`~FuelTankExternal`
              - Class defining an external fuel tank for an Aviator aircraft.

            * - :py:class:`~PayloadStation`
              - Class defining a payload station for an Aviator aircraft.

            * - :py:class:`~StationCollection`
              - Class defining a collection of payload stations for an Aviator aircraft.

            * - :py:class:`~WindModel`
              - Class defining the wind model for a mission, scenario, or procedure.

            * - :py:class:`~WindModelConstant`
              - Class defining a constant bearing/speed wind model for a mission.

            * - :py:class:`~WindModelADDS`
              - Class defining a wind model using the NOAA ADDS service for a mission.

            * - :py:class:`~ADDSMessage`
              - Class defining a message from the NOAA ADDS service.

            * - :py:class:`~ADDSMessageCollection`
              - Class defining a collection of messages from the NOAA ADDS service.

            * - :py:class:`~Procedure`
              - Class defining an unknown procedure type.

            * - :py:class:`~AtmosphereModel`
              - Class defining the atmosphere model for a mission, scenario, or procedure.

            * - :py:class:`~AtmosphereModelBasic`
              - Class defining the basic atmosphere model.

            * - :py:class:`~BasicManeuverStrategySimpleTurn`
              - Class defining the simple turn strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyAileronRoll`
              - Class defining the aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyFlyAOA`
              - Class defining the fly AOA strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyPull`
              - Class defining the pull strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyRollingPull`
              - Class defining the rolling pull strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategySmoothAccel`
              - Class defining the smooth accel strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategySmoothTurn`
              - Class defining the smooth turn strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverAirspeedOptions`
              - Class defining the airspeed options for basic maneuver strategies.

            * - :py:class:`~PropulsionThrust`
              - Class defining the the thrust propulsion used in basic maneuver procedures.

            * - :py:class:`~BasicManeuverStrategyAutopilotNav`
              - Class defining the autopilot - horizontal plane strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyAutopilotProf`
              - Class defining the autopiloc - vertical plane strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyBarrelRoll`
              - Class defining the barrel roll strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyLoop`
              - Class defining the loop strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyLTAHover`
              - Class defining the lighter than air hover strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyIntercept`
              - Class defining the Intercept strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyRelativeBearing`
              - Class defining the Relative Bearing strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyRelativeCourse`
              - Class defining the Relative Course strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyRendezvous`
              - Class defining the Rendezvous/Formation strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyStationkeeping`
              - Class defining the Stationkeeping strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyRelativeFPA`
              - Class defining the Relative Flight Path Angle strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyRelSpeedAltitude`
              - Class defining the Relative Speed/Altitude strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyBezier`
              - Class defining the Bezier strategy for a basic maneuver procedure.

            * - :py:class:`~BasicManeuverStrategyPushPull`
              - Class defining the Push/Pull strategy for a basic maneuver procedure.

            * - :py:class:`~ProcedureHoldingCircular`
              - Class defining a holding circular procedure.

            * - :py:class:`~ProcedureHoldingFigure8`
              - Class defining a holding figure 8 procedure.

            * - :py:class:`~ProcedureHoldingRacetrack`
              - Class defining a holding racetrack procedure.

            * - :py:class:`~ProcedureTransitionToHover`
              - Class defining a transition to hover procedure.

            * - :py:class:`~ProcedureTerrainFollow`
              - Class defining a terrain following procedure.

            * - :py:class:`~ProcedureHover`
              - Class defining a hover procedure.

            * - :py:class:`~ProcedureHoverTranslate`
              - Class defining a hover translate procedure.

            * - :py:class:`~ProcedureTransitionToForwardFlight`
              - Class defining a transition to forward flight procedure.

            * - :py:class:`~HoverAltitudeOptions`
              - Class defining the altitude options for a VTOL procedure.

            * - :py:class:`~ProcedureVerticalTakeoff`
              - Class defining a vertical takeoff procedure.

            * - :py:class:`~ProcedureVerticalLanding`
              - Class defining a vertical landing procedure.

            * - :py:class:`~ProcedureReferenceState`
              - Class defining a reference state procedure.

            * - :py:class:`~ProcedureSuperProcedure`
              - Class defining a super procedure.

            * - :py:class:`~ProcedureLaunch`
              - Class defining a launch procedure.

            * - :py:class:`~ProcedureAirway`
              - Class defining an Airway procedure.

            * - :py:class:`~ProcedureAirwayRouter`
              - Class defining an Airway Router procedure.

            * - :py:class:`~ProcedureAreaTargetSearch`
              - Class defining an Area Target Search procedure.

            * - :py:class:`~ProcedureFormationRecover`
              - Class defining a Formation/Recover procedure.

            * - :py:class:`~ProcedureInFormation`
              - Class defining an In Formation procedure.

            * - :py:class:`~ProcedureParallelFlightLine`
              - Class defining a Parallel Flight Line procedure.

            * - :py:class:`~ProcedureVGTPoint`
              - Class defining a VGT Point procedure.

            * - :py:class:`~PerformanceModelOptions`
              - Class defining the options for the active performance model in a phase.

            * - :py:class:`~AdvancedFixedWingTool`
              - Class defining the options for the Advanced Fixed Wing Tool of an aircraft.

            * - :py:class:`~AdvancedFixedWingExternalAero`
              - Class defining the External Aero File aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingSubsonicAero`
              - Class defining the subsonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingSubSuperHypersonicAero`
              - Class defining the Sub/Super/Hypersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingSupersonicAero`
              - Class defining the supersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~PerformanceModel`
              - Class defining an unknown performance model.

            * - :py:class:`~AdvancedFixedWingGeometryBasic`
              - Class defining a basic geometry wing in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingGeometryVariable`
              - Class defining a variable geometry wing in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingElectricPowerplant`
              - Class defining an Electric powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingExternalProp`
              - Class defining an External Prop File powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingSubSuperHypersonicProp`
              - Class defining a Sub/Super/Hypersonic powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingPistonPowerplant`
              - Class defining a Piston powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingEmpiricalJetEngine`
              - Class defining the Turbojet and Turbofan empirical models in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingTurbofanBasicABPowerplant`
              - Do not use this class, as it is deprecated. Use AgAvtrAdvFixedWingTurbofanBasicABProp instead.

            * - :py:class:`~AdvancedFixedWingTurbojetBasicABPowerplant`
              - Do not use this class, as it is deprecated. Use AgAvtrAdvFixedWingTurbojetBasicABProp instead.

            * - :py:class:`~AdvancedFixedWingTurbofanBasicABProp`
              - Class defining the Turbofan - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingTurbojetBasicABProp`
              - Class defining the Turbojet - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~AdvancedFixedWingTurbopropPowerplant`
              - Class defining the Turboprop powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~MissileSimpleAero`
              - Class defining the simple aerodynamic options for a missile.

            * - :py:class:`~MissileExternalAero`
              - Class defining the external aerodynamic options for a missile.

            * - :py:class:`~MissileAdvancedAero`
              - Class defining the advanced aerodynamic options for a missile.

            * - :py:class:`~MissileAero`
              - Class defining the aerodynamic options for a missile.

            * - :py:class:`~MissileProp`
              - Class defining the propulsion options for a missile.

            * - :py:class:`~MissileSimpleProp`
              - Class defining the Simple propulsion options for a missile.

            * - :py:class:`~MissileExternalProp`
              - Class defining the External propulsion options for a missile.

            * - :py:class:`~MissileRamjetProp`
              - Class defining the Ramjet propulsion options for a missile.

            * - :py:class:`~MissileRocketProp`
              - Class defining the Rocket propulsion options for a missile.

            * - :py:class:`~MissileTurbojetProp`
              - Class defining the Turbojet propulsion options for a missile.

            * - :py:class:`~ReferenceStateForwardFlightOptions`
              - Class defining the Forward Flight options for a Reference State procedure.

            * - :py:class:`~ReferenceStateTakeoffLandingOptions`
              - Class defining the Takeoff or Landing options for a Reference State procedure.

            * - :py:class:`~ReferenceStateHoverOptions`
              - Class defining the Hover options for a Reference State procedure.

            * - :py:class:`~ReferenceStateWeightOnWheelsOptions`
              - Class defining the Weight on Wheels options for a Reference State procedure.

            * - :py:class:`~SiteRunwayFromCatalog`
              - Class defining a runway from catalog site.

            * - :py:class:`~SiteAirportFromCatalog`
              - Class defining a airport from catalog site.

            * - :py:class:`~SiteNavaidFromCatalog`
              - Class defining a navaid from catalog site.

            * - :py:class:`~SiteVTOLPointFromCatalog`
              - Class defining a VTOL point from catalog site.

            * - :py:class:`~SiteWaypointFromCatalog`
              - Class defining a waypoint from catalog site.

            * - :py:class:`~NavaidCategory`
              - Class defining the navaid category in the Aviator catalog.

            * - :py:class:`~VTOLPointCategory`
              - Class defining the VTOL point category in the Aviator catalog.

            * - :py:class:`~WaypointCategory`
              - Class defining the waypoint category in the Aviator catalog.

            * - :py:class:`~ARINC424Navaid`
              - Class defining an ARINC424 Navaid.

            * - :py:class:`~ARINC424Helipad`
              - Class defining an ARINC424 Helipad.

            * - :py:class:`~ARINC424Waypoint`
              - Class defining an ARINC424 Waypoint.

            * - :py:class:`~UserVTOLPointSource`
              - Class defining the user VTOL Point source in the Aviator catalog.

            * - :py:class:`~UserVTOLPoint`
              - Class defining the user VTOL Point in the Aviator catalog.

            * - :py:class:`~UserWaypointSource`
              - Class defining the user waypoint source in the Aviator catalog.

            * - :py:class:`~UserWaypoint`
              - Class defining the user waypoint in the Aviator catalog.

            * - :py:class:`~PropulsionEfficiencies`
              - Class defining the Propulsion Efficiencies and Losses of a jet engine powerplant in the advanced fixed wing tool.

            * - :py:class:`~FuelModelKeroseneAFPROP`
              - Class defining the Kerosense - AFPROP fuel type for a thermodynamic jet engine model.

            * - :py:class:`~FuelModelKeroseneCEA`
              - Class defining the Kerosense - CEA fuel type for a thermodynamic jet engine model.

            * - :py:class:`~AdvancedFixedWingRamjetBasic`
              - Class defining the basic Ramjet model.

            * - :py:class:`~AdvancedFixedWingScramjetBasic`
              - Class defining the basic Scramjet model.

            * - :py:class:`~AircraftVTOLModel`
              - Class defining the VTOL performance model of an aircraft.

            * - :py:class:`~AircraftVTOL`
              - Class defining the VTOL category of an Aviator aircraft.

            * - :py:class:`~AircraftTerrainFollowModel`
              - Class defining the TerrainFollow performance model of an aircraft.

            * - :py:class:`~AircraftTerrainFollow`
              - Class defining the TerrainFollow category of an Aviator aircraft.

            * - :py:class:`~BasicManeuverStrategyBallistic3D`
              - Class defining Ballistic 3D strategy for a Basic Maneuver procedure.

            * - :py:class:`~ProcedureLaunchDynState`
              - Class defining a Launch Dyn State procedure.

            * - :py:class:`~ProcedureLaunchWaypoint`
              - Class defining a Launch Waypoint procedure.

            * - :py:class:`~SiteDynState`
              - Class defining a Dyn State site.

            * - :py:class:`~BasicManeuverStrategyPitch3D`
              - Class defining Pitch 3D strategy for a Basic Maneuver procedure.

            * - :py:class:`~RefuelDumpProperties`
              - Class defining the refuel/dump properties for the current procedure.

            * - :py:class:`~ProcedureFastTimeOptions`
              - Class defining fast operations (without error or constraint checks) for time options for the current procedure.

            * - :py:class:`~BasicManeuverTargetPositionVel`
              - Class defining the target position and velocity strategies for basic maneuvers.

            * - :py:class:`~BasicManeuverTargetPositionVelNoisyBrgRng`
              - Class defining the position and velocity strategy, Noisy Bearing Range.

            * - :py:class:`~BasicManeuverTargetPositionVelNoisySurfTgt`
              - Class defining the position and velocity strategy, Noisy Surface Target.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ERROR_CODES`
              - Error Codes.

            * - :py:class:`~CLOSURE_VALUE`
              - The closure value.

            * - :py:class:`~PROCEDURE_TYPE`
              - Aviator procedure types.

            * - :py:class:`~SITE_TYPE`
              - Aviator site types.

            * - :py:class:`~BASIC_MANEUVER_STRATEGY`
              - Basic maneuver strategy types.

            * - :py:class:`~STRAIGHT_AHEAD_REFERENCE_FRAME`
              - Straight Ahead basic maneuver Reference Frame.

            * - :py:class:`~AIRSPEED_TYPE`
              - Airspeed types.

            * - :py:class:`~AERO_PROP_SIMPLE_MODE`
              - Aircraft operating mode for basic acceleration models with aerodynamics set to Simple.

            * - :py:class:`~AERO_PROP_FLIGHT_MODE`
              - Flight mode for the Aero/Prop maneuver mode helper in aircraft acceleration models.

            * - :py:class:`~PHASE_OF_FLIGHT`
              - Flight mode for basic maneuver procedures.

            * - :py:class:`~CRUISE_SPEED`
              - Cruise airspeed type for the procedure.

            * - :py:class:`~TAKEOFF_MODE`
              - Takeoff procedure mode.

            * - :py:class:`~APPROACH_MODE`
              - Landing procedure approach mode.

            * - :py:class:`~NAVIGATOR_TURN_DIRECTION`
              - Turn mode for procedures with Enroute Turn Direction options.

            * - :py:class:`~BASIC_MANEUVER_FUEL_FLOW_TYPE`
              - Fuel flow type for basic maneuver procedures.

            * - :py:class:`~BASIC_MANEUVER_ALTITUDE_LIMIT`
              - The type of response Aviator will have if the maneuver attempts to exceed the altitude limit.

            * - :py:class:`~RUNWAY_HIGH_LOW_END`
              - Runway heading that the aircraft will use.

            * - :py:class:`~BASIC_MANEUVER_REFERENCE_FRAME`
              - Reference frame for the basic maneuver strategy.

            * - :py:class:`~BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT`
              - Define the control limits for the aircraft during the maneuver.

            * - :py:class:`~ACCEL_MANEUVER_MODE`
              - The mode that the aircraft will adhere to the specified acceleration parameters.

            * - :py:class:`~AIRCRAFT_AERO_STRATEGY`
              - The aerodynamic strategy used to compute lift, drag, angle of attack, sideslip and intermediate / derived values.

            * - :py:class:`~AIRCRAFT_PROP_STRATEGY`
              - The propulsion strategy used to compute thrust and throttle setting.

            * - :py:class:`~AGL_MSL`
              - The altitude mode.

            * - :py:class:`~LANDING_APPROACH_FIX_RANGE_MODE`
              - The reference point on the runway for the Approach Fix Range.

            * - :py:class:`~ACCELERATION_ADVANCED_ACCEL_MODE`
              - Acceleration mode for aircraft advanced acceleration models.

            * - :py:class:`~ACCEL_MANEUVER_AERO_PROP_MODE`
              - The mode used for the Aero/Prop maneuver mode helper for aircraft basic acceleration models.

            * - :py:class:`~BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS`
              - The type of response Aviator will have if the basic maneuver attempts to exceed the airspeed limit.

            * - :py:class:`~BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE`
              - Powered Cruise Options.

            * - :py:class:`~TURN_MODE`
              - The mode to specify an aircraft's level turn performance for acceleration performance models.

            * - :py:class:`~POINT_TO_POINT_MODE`
              - The heading or course of the aircraft at the beginning of the procedure.

            * - :py:class:`~ALTITUDE_CONSTRAINT_MANEUVER_MODE`
              - Turn mode for procedures that may require a level off maneuver.

            * - :py:class:`~WIND_MODEL_TYPE`
              - The wind model type.

            * - :py:class:`~WIND_ATMOS_MODEL_SOURCE`
              - The source for the wind or atmosphere model.

            * - :py:class:`~ADDS_MSG_INTERP_TYPE`
              - The interpolation method for the wind conditions.

            * - :py:class:`~ADDS_MISSING_MSG_TYPE`
              - The wind effect to apply if there is an interval gap between messages.

            * - :py:class:`~ADDS_MSG_EXTRAP_TYPE`
              - The wind effect to apply if the procedure(s) extend beyond the intervals of any available messages.

            * - :py:class:`~ADDS_FORECAST_TYPE`
              - The forecast type for the NOAA ADDS message.

            * - :py:class:`~ATMOSPHERE_MODEL`
              - The basic atmosphere model type.

            * - :py:class:`~SMOOTH_TURN_MODE`
              - The basic maneuver smooth turn mode.

            * - :py:class:`~PERF_MODEL_OVERRIDE`
              - The performance model override mode.

            * - :py:class:`~BASIC_MANEUVER_AIRSPEED_MODE`
              - The basic maneuver airspeed mode.

            * - :py:class:`~AILERON_ROLL_FLIGHT_PATH`
              - The flight path option for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ROLL_LEFT_RIGHT`
              - The roll direction for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ROLL_UPRIGHT_INVERTED`
              - The orientation for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~AILERON_ROLL_MODE`
              - The roll mode aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~FLY_AOA_LEFT_RIGHT`
              - The roll direction for a Fly AOA strategy for a basic maneuver procedure.

            * - :py:class:`~SMOOTH_ACCEL_LEFT_RIGHT`
              - The roll direction for a smooth acceleration strategy for a basic maneuver procedure.

            * - :py:class:`~PULL_MODE`
              - The pull mode for a pull strategy of a basic maneuver procedure.

            * - :py:class:`~ROLLING_PULL_MODE`
              - The rolling pull mode for a rolling pull strategy of a basic maneuver procedure.

            * - :py:class:`~SMOOTH_ACCEL_STOP_CONDITIONS`
              - The rolling pull mode for a rolling pull strategy of a basic maneuver procedure.

            * - :py:class:`~AUTOPILOT_HORIZ_PLANE_MODE`
              - The autopilot mode for an autopilot - horizontal plane strategy of a basic maneuver procedure.

            * - :py:class:`~ANGLE_MODE`
              - The angle mode for a barrel roll strategy of a basic maneuver procedure.

            * - :py:class:`~HOVER_ALTITUDE_MODE`
              - The altitude mode for the lighter than air hover strategy of a basic maneuver procedure.

            * - :py:class:`~HOVER_HEADING_MODE`
              - The heading mode for the lighter than air hover strategy of a basic maneuver procedure.

            * - :py:class:`~AUTOPILOT_ALTITUDE_MODE`
              - The altitude mode for the autopilot - vertical plane strategy of a basic maneuver procedure.

            * - :py:class:`~AUTOPILOT_ALTITUDE_CONTROL_MODE`
              - The altitude control mode for the autopilot - vertical plane strategy of a basic maneuver procedure.

            * - :py:class:`~CLOSURE_MODE`
              - The closure mode for guidance strategies of the basic maneuver procedure.

            * - :py:class:`~INTERCEPT_MODE`
              - The intercept mode for the intercept strategy of the basic maneuver procedure.

            * - :py:class:`~RENDEZVOUS_STOP_CONDITION`
              - The stop condition options for a rendezvous formation strategy of the basic maneuver procedure.

            * - :py:class:`~FORMATION_FLYER_STOP_CONDITION`
              - The stop condition options for a Formation Flyer procedure.

            * - :py:class:`~EXT_EPHEM_FLIGHT_MODE`
              - Flight mode enums for ExtEphem.

            * - :py:class:`~ACCEL_PERF_MODEL_OVERRIDE`
              - The acceleration performance model override mode.

            * - :py:class:`~STATIONKEEPING_STOP_CONDITION`
              - The stop condition options for a stationkeeping strategy.

            * - :py:class:`~TURN_DIRECTION`
              - The roll direction for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~PROFILE_CONTROL_LIMIT`
              - Define the control limits for a profile strategy of a basic maneuver procedure.

            * - :py:class:`~REL_SPEED_ALTITUDE_STOP_CONDITION`
              - The stop condition options for a relative speed/altitude strategy.

            * - :py:class:`~RELATIVE_ALTITUDE_MODE`
              - The relative altitude mode for a relative speed/altitude strategy.

            * - :py:class:`~FLY_TO_FLIGHT_PATH_ANGLE_MODE`
              - The flight path angle mode mode for a bezier profile strategy.

            * - :py:class:`~PUSH_PULL`
              - The option to pull up or push over for a push/pull profile strategy.

            * - :py:class:`~ACCEL_MODE`
              - The acceleration/decelation option for a push/pull profile strategy.

            * - :py:class:`~DELAY_ALTITUDE_MODE`
              - The altitude options for a delay procedure.

            * - :py:class:`~JOIN_EXIT_ARC_METHOD`
              - The options to join or exit an arc.

            * - :py:class:`~FLIGHT_LINE_PROC_TYPE`
              - The procedure methodology used to calculate the flight line.

            * - :py:class:`~TRANSITION_TO_HOVER_MODE`
              - The type of hover to transition to.

            * - :py:class:`~VTOL_RATE_MODE`
              - The rate mode for the VTOL procedure.

            * - :py:class:`~HOLDING_PROFILE_MODE`
              - How the aircraft will perform during the holding pattern with respect to airspeed and altitude.

            * - :py:class:`~HOLDING_DIRECTION`
              - The turn direction for the aircraft to enter the holding pattern.

            * - :py:class:`~HOLD_REFUEL_DUMP_MODE`
              - Define when the aircraft will leave the holding pattern after it has completed refueling or dumping fuel.

            * - :py:class:`~HOLDING_ENTRY_MANEUVER`
              - Define how the aircraft will enter the holding pattern.

            * - :py:class:`~VTOL_TRANSITION_MODE`
              - The mode to specify the course of the transition maneuver.

            * - :py:class:`~VTOL_FINAL_HEADING_MODE`
              - The mode to specify the heading at the end of the maneuver.

            * - :py:class:`~VTOL_TRANSLATION_MODE`
              - The mode to specify the translation of the VTOL maneuver.

            * - :py:class:`~VTOL_TRANSLATION_FINAL_COURSE_MODE`
              - The mode to specify the final course of the VTOL maneuver.

            * - :py:class:`~HOVER_MODE`
              - The hover mode.

            * - :py:class:`~VTOL_HEADING_MODE`
              - The heading mode for the hover maneuver.

            * - :py:class:`~VERT_LANDING_MODE`
              - The heading mode for a vertical landing maneuver.

            * - :py:class:`~LAUNCH_ATTITUDE_MODE`
              - The attitude mode for the launch procedure.

            * - :py:class:`~FUEL_FLOW_TYPE`
              - The fuel flow type to use for the procedure.

            * - :py:class:`~LINE_ORIENTATION`
              - The orientation for a parallel flight line procedure.

            * - :py:class:`~REL_ABS_BEARING`
              - The options for a bearing that can be relative or absolute.

            * - :py:class:`~BASIC_FIXED_WING_PROP_MODE`
              - The option to specify the thrust (jet engines) or power (propellers).

            * - :py:class:`~CLIMB_SPEED_TYPE`
              - The mode to calculate the aircraft's airspeed while climbing for an advanced climb performance model.

            * - :py:class:`~CRUISE_MAX_PERF_SPEED_TYPE`
              - The method for defining the maximum performance airspeed of the aircraft for an advanced cruise model.

            * - :py:class:`~DESCENT_SPEED_TYPE`
              - The method for calculating the aircraft's airspeed while descending.

            * - :py:class:`~TAKEOFF_LANDING_SPEED_MODE`
              - The method for calculating the aircraft's speed upon leaving the ground or at wheels down.

            * - :py:class:`~DEPARTURE_SPEED_MODE`
              - The method for calculating the aircraft's airspeed upon leaving the ground.

            * - :py:class:`~ADVANCED_FIXED_WING_AERO_STRATEGY`
              - The aerodynamic strategy for the Advanced Fixed Wing Tool.

            * - :py:class:`~ADVANCED_FIXED_WING_GEOMETRY`
              - The method to define the wing geometry of an aircraft in the Advanced Fixed Wing Tool.

            * - :py:class:`~ADVANCED_FIXED_WING_POWERPLANT_STRATEGY`
              - The powerplant strategy for the Advanced Fixed Wing Tool.

            * - :py:class:`~MISSILE_AERO_STRATEGY`
              - The aerodynamic strategy used to compute lift, drag, angle of attack, sideslip and intermediate / derived values.

            * - :py:class:`~MISSILE_PROP_STRATEGY`
              - The propulsion strategy used to compute thrust and throttle setting.

            * - :py:class:`~ROTORCRAFT_POWERPLANT_TYPE`
              - The powerplant type for a rotorcraft.

            * - :py:class:`~MINIMIZE_SITE_PROC_TIME_DIFF`
              - Options for minimizing the time difference between the procedure and site times.

            * - :py:class:`~STK_OBJECT_WAYPOINT_OFFSET_MODE`
              - The options to offset the site location relative to the STK Object.

            * - :py:class:`~SEARCH_PATTERN_COURSE_MODE`
              - The mode to determine the course of the search pattern.

            * - :py:class:`~DELAY_TURN_DIRECTION`
              - Turn mode for procedures with Delay options.

            * - :py:class:`~TRAJECTORY_BLEND_MODE`
              - The interpolation mode to determine the aircraft's position and velocity.

            * - :py:class:`~REFERENCE_STATE_PERF_MODE`
              - The type of motion the aircraft is engaged in at the reference state.

            * - :py:class:`~REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE`
              - The mode to specify the longitudinal acceleration of the aircraft.

            * - :py:class:`~REFERENCE_STATE_LATERAL_ACCEL_MODE`
              - The mode to specify the lateral acceleration of the aircraft.

            * - :py:class:`~REFERENCE_STATE_ATTITUDE_MODE`
              - The mode to specify the attitude rate of change.

            * - :py:class:`~AND_OR`
              - The option to specify AND or OR.

            * - :py:class:`~JET_ENGINE_TECHNOLOGY_LEVEL`
              - The technology level of the jet engine.

            * - :py:class:`~JET_ENGINE_INTAKE_TYPE`
              - The intake type of the jet engine.

            * - :py:class:`~JET_ENGINE_TURBINE_TYPE`
              - The turbine type of the jet engine.

            * - :py:class:`~JET_ENGINE_EXHAUST_NOZZLE_TYPE`
              - The exhaust nozzle type of the jet engine.

            * - :py:class:`~JET_FUEL_TYPE`
              - The jet fuel type.

            * - :py:class:`~AFPROP_FUEL_TYPE`
              - The AFPROP fuel type.

            * - :py:class:`~CEA_FUEL_TYPE`
              - The CEA fuel type.

            * - :py:class:`~TURBINE_MODE`
              - The turbine mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~RAMJET_MODE`
              - The ramjet mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~SCRAMJET_MODE`
              - The scramjet mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~NUMERICAL_INTEGRATOR`
              - The numerical integrator to be used for the procedure.

            * - :py:class:`~BALLISTIC_3D_CONTROL_MODE`
              - The control mode used to define the ballistic 3D strategy of the basic maneuver procedure.

            * - :py:class:`~LAUNCH_DYN_STATE_COORD_FRAME`
              - The coordinate frame used for a LaunchDynState procedure.

            * - :py:class:`~LAUNCH_DYN_STATE_BEARING_REFERENCE`
              - The vector used as a bearing reference for a LaunchDynState procedure.

            * - :py:class:`~ALTITUDE_REFERENCE`
              - The altitude reference.

            * - :py:class:`~SMOOTH_TURN_FPA_MODE`
              - The flight path angle mode for the Smooth Turn strategy of the Basic Maneuver procedure.

            * - :py:class:`~PITCH_3D_CONTROL_MODE`
              - The control mode used to define the pitch 3D strategy of the basic maneuver procedure.

            * - :py:class:`~REFUEL_DUMP_MODE`
              - The modes used to define procedure refuel/dump modes.

            * - :py:class:`~BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE`
              - The modes used to define basic maneuver glide speed control modes.

            * - :py:class:`~TARGET_POSITION_VEL_TYPE`
              - The target pos/vel type.

            * - :py:class:`~EPHEM_SHIFT_ROTATE_ALTITUDE_MODE`
              - Ephem alt mode.

            * - :py:class:`~EPHEM_SHIFT_ROTATE_COURSE_MODE`
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

     ISite<aviator\ISite>
     IWindModel<aviator\IWindModel>
     IADDSMessage<aviator\IADDSMessage>
     IFuelTankInternal<aviator\IFuelTankInternal>
     IFuelTankExternal<aviator\IFuelTankExternal>
     IPayloadStation<aviator\IPayloadStation>
     IAircraftModel<aviator\IAircraftModel>
     IAircraftSimpleAero<aviator\IAircraftSimpleAero>
     ILevelTurns<aviator\ILevelTurns>
     IAttitudeTransitions<aviator\IAttitudeTransitions>
     IClimbAndDescentTransitions<aviator\IClimbAndDescentTransitions>
     ICatalogItem<aviator\ICatalogItem>
     IAircraftBasicClimbModel<aviator\IAircraftBasicClimbModel>
     IAircraftBasicAccelerationModel<aviator\IAircraftBasicAccelerationModel>
     IAircraftCategory<aviator\IAircraftCategory>
     IRunwayCategory<aviator\IRunwayCategory>
     IBasicManeuverStrategy<aviator\IBasicManeuverStrategy>
     IAircraftVTOL<aviator\IAircraftVTOL>
     IAircraftExternalAero<aviator\IAircraftExternalAero>
     IAircraftSimpleProp<aviator\IAircraftSimpleProp>
     IAircraftExternalProp<aviator\IAircraftExternalProp>
     IAircraftBasicFixedWingProp<aviator\IAircraftBasicFixedWingProp>
     IAircraftAdvancedClimbModel<aviator\IAircraftAdvancedClimbModel>
     IAircraftBasicCruiseModel<aviator\IAircraftBasicCruiseModel>
     IAircraftAdvancedCruiseModel<aviator\IAircraftAdvancedCruiseModel>
     IAircraftBasicDescentModel<aviator\IAircraftBasicDescentModel>
     IAircraftAdvancedDescentModel<aviator\IAircraftAdvancedDescentModel>
     IAircraftBasicLandingModel<aviator\IAircraftBasicLandingModel>
     IAircraftAdvancedLandingModel<aviator\IAircraftAdvancedLandingModel>
     IAircraftBasicTakeoffModel<aviator\IAircraftBasicTakeoffModel>
     IAircraftAdvancedTakeoffModel<aviator\IAircraftAdvancedTakeoffModel>
     IAircraftVTOLModel<aviator\IAircraftVTOLModel>
     IAircraftTerrainFollow<aviator\IAircraftTerrainFollow>
     IPerformanceModelOptions<aviator\IPerformanceModelOptions>
     IAdvancedFixedWingTool<aviator\IAdvancedFixedWingTool>
     IAdvancedFixedWingExternalAero<aviator\IAdvancedFixedWingExternalAero>
     IAdvancedFixedWingSubsonicAero<aviator\IAdvancedFixedWingSubsonicAero>
     IAdvancedFixedWingSubSuperHypersonicAero<aviator\IAdvancedFixedWingSubSuperHypersonicAero>
     IAdvancedFixedWingSubSuperHypersonicProp<aviator\IAdvancedFixedWingSubSuperHypersonicProp>
     IAdvancedFixedWingSupersonicAero<aviator\IAdvancedFixedWingSupersonicAero>
     IAdvancedFixedWingGeometryBasic<aviator\IAdvancedFixedWingGeometryBasic>
     IAdvancedFixedWingGeometryVariable<aviator\IAdvancedFixedWingGeometryVariable>
     IAdvancedFixedWingElectricPowerplant<aviator\IAdvancedFixedWingElectricPowerplant>
     IAdvancedFixedWingExternalProp<aviator\IAdvancedFixedWingExternalProp>
     IAdvancedFixedWingPistonPowerplant<aviator\IAdvancedFixedWingPistonPowerplant>
     IAdvancedFixedWingTurbopropPowerplant<aviator\IAdvancedFixedWingTurbopropPowerplant>
     IAdvancedFixedWingEmpiricalJetEngine<aviator\IAdvancedFixedWingEmpiricalJetEngine>
     IAdvancedFixedWingTurbojetBasicABProp<aviator\IAdvancedFixedWingTurbojetBasicABProp>
     IAdvancedFixedWingTurbofanBasicABProp<aviator\IAdvancedFixedWingTurbofanBasicABProp>
     IAviatorVehicle<aviator\IAviatorVehicle>
     IMissileModel<aviator\IMissileModel>
     IMissileAero<aviator\IMissileAero>
     IMissileProp<aviator\IMissileProp>
     IMissileSimpleAero<aviator\IMissileSimpleAero>
     IMissileSimpleProp<aviator\IMissileSimpleProp>
     IMissileExternalAero<aviator\IMissileExternalAero>
     IMissileExternalProp<aviator\IMissileExternalProp>
     IMissileAdvancedAero<aviator\IMissileAdvancedAero>
     IMissileRamjetProp<aviator\IMissileRamjetProp>
     IMissileRocketProp<aviator\IMissileRocketProp>
     IMissileTurbojetProp<aviator\IMissileTurbojetProp>
     IRotorcraftModel<aviator\IRotorcraftModel>
     IRotorcraftAero<aviator\IRotorcraftAero>
     IRotorcraftProp<aviator\IRotorcraftProp>
     IUserRunwaySource<aviator\IUserRunwaySource>
     IUserRunway<aviator\IUserRunway>
     IARINC424Item<aviator\IARINC424Item>
     IARINC424Source<aviator\IARINC424Source>
     IDAFIFSource<aviator\IDAFIFSource>
     IUserVTOLPoint<aviator\IUserVTOLPoint>
     IUserVTOLPointSource<aviator\IUserVTOLPointSource>
     IUserWaypoint<aviator\IUserWaypoint>
     IUserWaypointSource<aviator\IUserWaypointSource>
     IPropulsionEfficiencies<aviator\IPropulsionEfficiencies>
     IFuelModelKeroseneAFPROP<aviator\IFuelModelKeroseneAFPROP>
     IFuelModelKeroseneCEA<aviator\IFuelModelKeroseneCEA>
     IAdvancedFixedWingRamjetBasic<aviator\IAdvancedFixedWingRamjetBasic>
     IAdvancedFixedWingScramjetBasic<aviator\IAdvancedFixedWingScramjetBasic>
     IRefuelDumpProperties<aviator\IRefuelDumpProperties>
     IProcedureFastTimeOptions<aviator\IProcedureFastTimeOptions>
     IAtmosphereModelBasic<aviator\IAtmosphereModelBasic>
     IAtmosphereModel<aviator\IAtmosphereModel>
     IADDSMessageCollection<aviator\IADDSMessageCollection>
     IWindModelADDS<aviator\IWindModelADDS>
     IWindModelConstant<aviator\IWindModelConstant>
     IStation<aviator\IStation>
     IStationCollection<aviator\IStationCollection>
     IConfiguration<aviator\IConfiguration>
     ICatalogSource<aviator\ICatalogSource>
     IAircraftModels<aviator\IAircraftModels>
     IMissileModels<aviator\IMissileModels>
     IRotorcraftModels<aviator\IRotorcraftModels>
     IBasicFixedWingLiftHelper<aviator\IBasicFixedWingLiftHelper>
     IAircraftBasicFixedWingAero<aviator\IAircraftBasicFixedWingAero>
     IAircraftAero<aviator\IAircraftAero>
     IAircraftProp<aviator\IAircraftProp>
     IAircraftAccelerationMode<aviator\IAircraftAccelerationMode>
     IAircraftAdvancedAccelerationModel<aviator\IAircraftAdvancedAccelerationModel>
     IAeroPropManeuverModeHelper<aviator\IAeroPropManeuverModeHelper>
     ICatalogRunway<aviator\ICatalogRunway>
     ICatalogAirport<aviator\ICatalogAirport>
     ICatalogNavaid<aviator\ICatalogNavaid>
     ICatalogVTOLPoint<aviator\ICatalogVTOLPoint>
     ICatalogWaypoint<aviator\ICatalogWaypoint>
     IARINC424Airport<aviator\IARINC424Airport>
     IDAFIFItem<aviator\IDAFIFItem>
     IARINC424Runway<aviator\IARINC424Runway>
     IAirportCategory<aviator\IAirportCategory>
     INavaidCategory<aviator\INavaidCategory>
     IVTOLPointCategory<aviator\IVTOLPointCategory>
     IWaypointCategory<aviator\IWaypointCategory>
     IAircraftClimb<aviator\IAircraftClimb>
     IAircraftCruise<aviator\IAircraftCruise>
     IAircraftDescent<aviator\IAircraftDescent>
     IAircraftLanding<aviator\IAircraftLanding>
     IAircraftTakeoff<aviator\IAircraftTakeoff>
     IAircraftAcceleration<aviator\IAircraftAcceleration>
     ICatalog<aviator\ICatalog>
     IProcedureTimeOptions<aviator\IProcedureTimeOptions>
     ICalculationOptions<aviator\ICalculationOptions>
     INavigationOptions<aviator\INavigationOptions>
     IAltitudeMSLAndLevelOffOptions<aviator\IAltitudeMSLAndLevelOffOptions>
     IAltitudeMSLOptions<aviator\IAltitudeMSLOptions>
     IAltitudeOptions<aviator\IAltitudeOptions>
     IHoverAltitudeOptions<aviator\IHoverAltitudeOptions>
     IArcAltitudeOptions<aviator\IArcAltitudeOptions>
     IArcAltitudeAndDelayOptions<aviator\IArcAltitudeAndDelayOptions>
     IArcOptions<aviator\IArcOptions>
     IVerticalPlaneOptions<aviator\IVerticalPlaneOptions>
     IVerticalPlaneAndFlightPathOptions<aviator\IVerticalPlaneAndFlightPathOptions>
     IArcVerticalPlaneOptions<aviator\IArcVerticalPlaneOptions>
     IEnrouteOptions<aviator\IEnrouteOptions>
     IEnrouteAndDelayOptions<aviator\IEnrouteAndDelayOptions>
     IEnrouteTurnDirectionOptions<aviator\IEnrouteTurnDirectionOptions>
     ICruiseAirspeedOptions<aviator\ICruiseAirspeedOptions>
     ICruiseAirspeedProfile<aviator\ICruiseAirspeedProfile>
     ICruiseAirspeedAndProfileOptions<aviator\ICruiseAirspeedAndProfileOptions>
     IAutomationStrategyFactory<aviator\IAutomationStrategyFactory>
     IConnect<aviator\IConnect>
     IRunwayHeadingOptions<aviator\IRunwayHeadingOptions>
     IProcedure<aviator\IProcedure>
     IProcedureCollection<aviator\IProcedureCollection>
     IPhase<aviator\IPhase>
     IPhaseCollection<aviator\IPhaseCollection>
     IMission<aviator\IMission>
     IAviatorPropagator<aviator\IAviatorPropagator>
     IPerformanceModel<aviator\IPerformanceModel>
     IAdvancedFixedWingGeometry<aviator\IAdvancedFixedWingGeometry>
     IAdvancedFixedWingTurbofanBasicABPowerplant<aviator\IAdvancedFixedWingTurbofanBasicABPowerplant>
     IAdvancedFixedWingTurbojetBasicABPowerplant<aviator\IAdvancedFixedWingTurbojetBasicABPowerplant>
     IAdvancedFixedWingPowerplant<aviator\IAdvancedFixedWingPowerplant>
     ISiteUnknown<aviator\ISiteUnknown>
     IAircraftTerrainFollowModel<aviator\IAircraftTerrainFollowModel>
     IBasicManeuverTargetPositionVel<aviator\IBasicManeuverTargetPositionVel>
     IPropulsionThrust<aviator\IPropulsionThrust>
     IBasicManeuverAirspeedOptions<aviator\IBasicManeuverAirspeedOptions>
     IBasicManeuverStrategyAileronRoll<aviator\IBasicManeuverStrategyAileronRoll>
     IBasicManeuverStrategyAutopilotNav<aviator\IBasicManeuverStrategyAutopilotNav>
     IBasicManeuverStrategyAutopilotProf<aviator\IBasicManeuverStrategyAutopilotProf>
     IBasicManeuverStrategyBarrelRoll<aviator\IBasicManeuverStrategyBarrelRoll>
     IBasicManeuverStrategyLoop<aviator\IBasicManeuverStrategyLoop>
     IBasicManeuverStrategyLTAHover<aviator\IBasicManeuverStrategyLTAHover>
     IBasicManeuverStrategyFlyAOA<aviator\IBasicManeuverStrategyFlyAOA>
     IBasicManeuverStrategyPull<aviator\IBasicManeuverStrategyPull>
     IBasicManeuverStrategyRollingPull<aviator\IBasicManeuverStrategyRollingPull>
     IBasicManeuverStrategySmoothAccel<aviator\IBasicManeuverStrategySmoothAccel>
     IBasicManeuverStrategySmoothTurn<aviator\IBasicManeuverStrategySmoothTurn>
     IBasicManeuverStrategySimpleTurn<aviator\IBasicManeuverStrategySimpleTurn>
     IBasicManeuverStrategyIntercept<aviator\IBasicManeuverStrategyIntercept>
     IBasicManeuverStrategyRelativeBearing<aviator\IBasicManeuverStrategyRelativeBearing>
     IBasicManeuverStrategyRelativeCourse<aviator\IBasicManeuverStrategyRelativeCourse>
     IBasicManeuverStrategyRendezvous<aviator\IBasicManeuverStrategyRendezvous>
     IBasicManeuverStrategyStationkeeping<aviator\IBasicManeuverStrategyStationkeeping>
     IBasicManeuverStrategyRelativeFPA<aviator\IBasicManeuverStrategyRelativeFPA>
     IBasicManeuverStrategyRelSpeedAltitude<aviator\IBasicManeuverStrategyRelSpeedAltitude>
     IBasicManeuverStrategyBezier<aviator\IBasicManeuverStrategyBezier>
     IBasicManeuverStrategyPushPull<aviator\IBasicManeuverStrategyPushPull>
     IBasicManeuverStrategyGlideProfile<aviator\IBasicManeuverStrategyGlideProfile>
     IBasicManeuverStrategyCruiseProfile<aviator\IBasicManeuverStrategyCruiseProfile>
     IBasicManeuverStrategyStraightAhead<aviator\IBasicManeuverStrategyStraightAhead>
     IBasicManeuverStrategyWeave<aviator\IBasicManeuverStrategyWeave>
     IBasicManeuverStrategyBallistic3D<aviator\IBasicManeuverStrategyBallistic3D>
     IBasicManeuverStrategyPitch3D<aviator\IBasicManeuverStrategyPitch3D>
     IBasicManeuverTargetPositionVelNoisyBrgRng<aviator\IBasicManeuverTargetPositionVelNoisyBrgRng>
     IBasicManeuverTargetPositionVelNoisySurfTgt<aviator\IBasicManeuverTargetPositionVelNoisySurfTgt>
     ITakeoffNormal<aviator\ITakeoffNormal>
     ITakeoffDeparturePoint<aviator\ITakeoffDeparturePoint>
     ITakeoffLowTransition<aviator\ITakeoffLowTransition>
     IReferenceStateForwardFlightOptions<aviator\IReferenceStateForwardFlightOptions>
     IReferenceStateHoverOptions<aviator\IReferenceStateHoverOptions>
     IReferenceStateWeightOnWheelsOptions<aviator\IReferenceStateWeightOnWheelsOptions>
     IReferenceStateTakeoffLandingOptions<aviator\IReferenceStateTakeoffLandingOptions>
     ILandingEnterDownwindPattern<aviator\ILandingEnterDownwindPattern>
     ILandingInterceptGlideslope<aviator\ILandingInterceptGlideslope>
     ILandingStandardInstrumentApproach<aviator\ILandingStandardInstrumentApproach>
     IProcedureBasicManeuver<aviator\IProcedureBasicManeuver>
     ISiteWaypoint<aviator\ISiteWaypoint>
     ISiteEndOfPrevProcedure<aviator\ISiteEndOfPrevProcedure>
     ISiteVTOLPoint<aviator\ISiteVTOLPoint>
     ISiteSTKVehicle<aviator\ISiteSTKVehicle>
     ISiteReferenceState<aviator\ISiteReferenceState>
     ISiteSuperProcedure<aviator\ISiteSuperProcedure>
     ISiteRelToPrevProcedure<aviator\ISiteRelToPrevProcedure>
     ISiteSTKObjectWaypoint<aviator\ISiteSTKObjectWaypoint>
     ISiteSTKStaticObject<aviator\ISiteSTKStaticObject>
     ISiteRelToSTKObject<aviator\ISiteRelToSTKObject>
     ISiteSTKAreaTarget<aviator\ISiteSTKAreaTarget>
     ISiteRunway<aviator\ISiteRunway>
     IProcedureLanding<aviator\IProcedureLanding>
     IProcedureEnroute<aviator\IProcedureEnroute>
     IProcedureExtEphem<aviator\IProcedureExtEphem>
     IProcedureFormationFlyer<aviator\IProcedureFormationFlyer>
     IProcedureBasicPointToPoint<aviator\IProcedureBasicPointToPoint>
     IProcedureDelay<aviator\IProcedureDelay>
     IProcedureTakeoff<aviator\IProcedureTakeoff>
     IProcedureArcEnroute<aviator\IProcedureArcEnroute>
     IProcedureArcPointToPoint<aviator\IProcedureArcPointToPoint>
     IProcedureFlightLine<aviator\IProcedureFlightLine>
     IProcedureHoldingCircular<aviator\IProcedureHoldingCircular>
     IProcedureHoldingFigure8<aviator\IProcedureHoldingFigure8>
     IProcedureHoldingRacetrack<aviator\IProcedureHoldingRacetrack>
     IProcedureTransitionToHover<aviator\IProcedureTransitionToHover>
     IProcedureTerrainFollow<aviator\IProcedureTerrainFollow>
     IProcedureHover<aviator\IProcedureHover>
     IProcedureHoverTranslate<aviator\IProcedureHoverTranslate>
     IProcedureTransitionToForwardFlight<aviator\IProcedureTransitionToForwardFlight>
     IProcedureVerticalTakeoff<aviator\IProcedureVerticalTakeoff>
     IProcedureVerticalLanding<aviator\IProcedureVerticalLanding>
     IProcedureReferenceState<aviator\IProcedureReferenceState>
     IProcedureSuperProcedure<aviator\IProcedureSuperProcedure>
     IProcedureLaunch<aviator\IProcedureLaunch>
     IProcedureAirway<aviator\IProcedureAirway>
     IProcedureAirwayRouter<aviator\IProcedureAirwayRouter>
     IProcedureAreaTargetSearch<aviator\IProcedureAreaTargetSearch>
     IProcedureFormationRecover<aviator\IProcedureFormationRecover>
     IProcedureInFormation<aviator\IProcedureInFormation>
     IProcedureParallelFlightLine<aviator\IProcedureParallelFlightLine>
     IProcedureVGTPoint<aviator\IProcedureVGTPoint>
     ISiteRunwayFromCatalog<aviator\ISiteRunwayFromCatalog>
     ISiteAirportFromCatalog<aviator\ISiteAirportFromCatalog>
     ISiteNavaidFromCatalog<aviator\ISiteNavaidFromCatalog>
     ISiteVTOLPointFromCatalog<aviator\ISiteVTOLPointFromCatalog>
     ISiteWaypointFromCatalog<aviator\ISiteWaypointFromCatalog>
     IProcedureLaunchDynState<aviator\IProcedureLaunchDynState>
     IProcedureLaunchWaypoint<aviator\IProcedureLaunchWaypoint>
     ISiteDynState<aviator\ISiteDynState>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     SiteWaypoint<aviator\SiteWaypoint>
     SiteEndOfPrevProcedure<aviator\SiteEndOfPrevProcedure>
     SiteVTOLPoint<aviator\SiteVTOLPoint>
     SiteReferenceState<aviator\SiteReferenceState>
     SiteSTKVehicle<aviator\SiteSTKVehicle>
     SiteSuperProcedure<aviator\SiteSuperProcedure>
     SiteRelToPrevProcedure<aviator\SiteRelToPrevProcedure>
     SiteSTKObjectWaypoint<aviator\SiteSTKObjectWaypoint>
     SiteSTKStaticObject<aviator\SiteSTKStaticObject>
     SiteRelToSTKObject<aviator\SiteRelToSTKObject>
     SiteSTKAreaTarget<aviator\SiteSTKAreaTarget>
     SiteRunway<aviator\SiteRunway>
     Site<aviator\Site>
     ProcedureLanding<aviator\ProcedureLanding>
     ProcedureEnroute<aviator\ProcedureEnroute>
     ProcedureExtEphem<aviator\ProcedureExtEphem>
     ProcedureFormationFlyer<aviator\ProcedureFormationFlyer>
     ProcedureBasicPointToPoint<aviator\ProcedureBasicPointToPoint>
     ProcedureArcEnroute<aviator\ProcedureArcEnroute>
     ProcedureArcPointToPoint<aviator\ProcedureArcPointToPoint>
     ProcedureFlightLine<aviator\ProcedureFlightLine>
     ProcedureDelay<aviator\ProcedureDelay>
     ProcedureTakeoff<aviator\ProcedureTakeoff>
     ProcedureCollection<aviator\ProcedureCollection>
     Phase<aviator\Phase>
     PhaseCollection<aviator\PhaseCollection>
     Mission<aviator\Mission>
     AviatorPropagator<aviator\AviatorPropagator>
     ProcedureBasicManeuver<aviator\ProcedureBasicManeuver>
     BasicManeuverStrategyWeave<aviator\BasicManeuverStrategyWeave>
     ProcedureTimeOptions<aviator\ProcedureTimeOptions>
     CalculationOptions<aviator\CalculationOptions>
     AircraftCategory<aviator\AircraftCategory>
     Catalog<aviator\Catalog>
     AircraftModel<aviator\AircraftModel>
     MissileModel<aviator\MissileModel>
     RotorcraftModel<aviator\RotorcraftModel>
     RotorcraftAero<aviator\RotorcraftAero>
     RotorcraftProp<aviator\RotorcraftProp>
     AircraftAcceleration<aviator\AircraftAcceleration>
     AircraftBasicAccelerationModel<aviator\AircraftBasicAccelerationModel>
     AircraftClimb<aviator\AircraftClimb>
     AircraftCruise<aviator\AircraftCruise>
     AircraftDescent<aviator\AircraftDescent>
     AircraftLanding<aviator\AircraftLanding>
     AircraftTakeoff<aviator\AircraftTakeoff>
     AircraftBasicClimbModel<aviator\AircraftBasicClimbModel>
     AircraftAdvancedClimbModel<aviator\AircraftAdvancedClimbModel>
     AircraftBasicCruiseModel<aviator\AircraftBasicCruiseModel>
     AircraftAdvancedCruiseModel<aviator\AircraftAdvancedCruiseModel>
     AircraftBasicDescentModel<aviator\AircraftBasicDescentModel>
     AircraftAdvancedDescentModel<aviator\AircraftAdvancedDescentModel>
     AircraftBasicTakeoffModel<aviator\AircraftBasicTakeoffModel>
     AircraftAdvancedTakeoffModel<aviator\AircraftAdvancedTakeoffModel>
     AircraftBasicLandingModel<aviator\AircraftBasicLandingModel>
     AircraftAdvancedLandingModel<aviator\AircraftAdvancedLandingModel>
     AirportCategory<aviator\AirportCategory>
     ARINC424Airport<aviator\ARINC424Airport>
     ARINC424Runway<aviator\ARINC424Runway>
     DAFIFRunway<aviator\DAFIFRunway>
     DAFIFHelipad<aviator\DAFIFHelipad>
     DAFIFWaypoint<aviator\DAFIFWaypoint>
     RunwayCategory<aviator\RunwayCategory>
     UserRunwaySource<aviator\UserRunwaySource>
     UserRunway<aviator\UserRunway>
     AltitudeMSLOptions<aviator\AltitudeMSLOptions>
     AltitudeOptions<aviator\AltitudeOptions>
     ArcAltitudeOptions<aviator\ArcAltitudeOptions>
     ArcAltitudeAndDelayOptions<aviator\ArcAltitudeAndDelayOptions>
     ArcOptions<aviator\ArcOptions>
     AltitudeMSLAndLevelOffOptions<aviator\AltitudeMSLAndLevelOffOptions>
     CruiseAirspeedOptions<aviator\CruiseAirspeedOptions>
     CruiseAirspeedProfile<aviator\CruiseAirspeedProfile>
     CruiseAirspeedAndProfileOptions<aviator\CruiseAirspeedAndProfileOptions>
     LandingCruiseAirspeedAndProfileOptions<aviator\LandingCruiseAirspeedAndProfileOptions>
     EnrouteOptions<aviator\EnrouteOptions>
     EnrouteAndDelayOptions<aviator\EnrouteAndDelayOptions>
     LandingEnrouteOptions<aviator\LandingEnrouteOptions>
     EnrouteTurnDirectionOptions<aviator\EnrouteTurnDirectionOptions>
     NavigationOptions<aviator\NavigationOptions>
     VerticalPlaneOptions<aviator\VerticalPlaneOptions>
     ArcVerticalPlaneOptions<aviator\ArcVerticalPlaneOptions>
     VerticalPlaneAndFlightPathOptions<aviator\VerticalPlaneAndFlightPathOptions>
     LandingVerticalPlaneOptions<aviator\LandingVerticalPlaneOptions>
     RunwayHeadingOptions<aviator\RunwayHeadingOptions>
     LandingEnterDownwindPattern<aviator\LandingEnterDownwindPattern>
     LandingInterceptGlideslope<aviator\LandingInterceptGlideslope>
     LandingStandardInstrumentApproach<aviator\LandingStandardInstrumentApproach>
     TakeoffDeparturePoint<aviator\TakeoffDeparturePoint>
     TakeoffLowTransition<aviator\TakeoffLowTransition>
     TakeoffNormal<aviator\TakeoffNormal>
     LevelTurns<aviator\LevelTurns>
     AttitudeTransitions<aviator\AttitudeTransitions>
     ClimbAndDescentTransitions<aviator\ClimbAndDescentTransitions>
     AeroPropManeuverModeHelper<aviator\AeroPropManeuverModeHelper>
     AircraftAdvancedAccelerationModel<aviator\AircraftAdvancedAccelerationModel>
     AircraftAccelerationMode<aviator\AircraftAccelerationMode>
     AircraftSimpleAero<aviator\AircraftSimpleAero>
     AircraftExternalAero<aviator\AircraftExternalAero>
     AircraftAero<aviator\AircraftAero>
     AircraftBasicFixedWingAero<aviator\AircraftBasicFixedWingAero>
     AircraftProp<aviator\AircraftProp>
     AircraftSimpleProp<aviator\AircraftSimpleProp>
     AircraftExternalProp<aviator\AircraftExternalProp>
     AircraftBasicFixedWingProp<aviator\AircraftBasicFixedWingProp>
     ARINC424Source<aviator\ARINC424Source>
     DAFIFSource<aviator\DAFIFSource>
     BasicFixedWingFwdFlightLiftHelper<aviator\BasicFixedWingFwdFlightLiftHelper>
     BasicManeuverStrategyStraightAhead<aviator\BasicManeuverStrategyStraightAhead>
     BasicManeuverStrategyCruiseProfile<aviator\BasicManeuverStrategyCruiseProfile>
     BasicManeuverStrategyGlideProfile<aviator\BasicManeuverStrategyGlideProfile>
     AircraftModels<aviator\AircraftModels>
     MissileModels<aviator\MissileModels>
     RotorcraftModels<aviator\RotorcraftModels>
     Configuration<aviator\Configuration>
     FuelTankInternal<aviator\FuelTankInternal>
     FuelTankExternal<aviator\FuelTankExternal>
     PayloadStation<aviator\PayloadStation>
     StationCollection<aviator\StationCollection>
     WindModel<aviator\WindModel>
     WindModelConstant<aviator\WindModelConstant>
     WindModelADDS<aviator\WindModelADDS>
     ADDSMessage<aviator\ADDSMessage>
     ADDSMessageCollection<aviator\ADDSMessageCollection>
     Procedure<aviator\Procedure>
     AtmosphereModel<aviator\AtmosphereModel>
     AtmosphereModelBasic<aviator\AtmosphereModelBasic>
     BasicManeuverStrategySimpleTurn<aviator\BasicManeuverStrategySimpleTurn>
     BasicManeuverStrategyAileronRoll<aviator\BasicManeuverStrategyAileronRoll>
     BasicManeuverStrategyFlyAOA<aviator\BasicManeuverStrategyFlyAOA>
     BasicManeuverStrategyPull<aviator\BasicManeuverStrategyPull>
     BasicManeuverStrategyRollingPull<aviator\BasicManeuverStrategyRollingPull>
     BasicManeuverStrategySmoothAccel<aviator\BasicManeuverStrategySmoothAccel>
     BasicManeuverStrategySmoothTurn<aviator\BasicManeuverStrategySmoothTurn>
     BasicManeuverAirspeedOptions<aviator\BasicManeuverAirspeedOptions>
     PropulsionThrust<aviator\PropulsionThrust>
     BasicManeuverStrategyAutopilotNav<aviator\BasicManeuverStrategyAutopilotNav>
     BasicManeuverStrategyAutopilotProf<aviator\BasicManeuverStrategyAutopilotProf>
     BasicManeuverStrategyBarrelRoll<aviator\BasicManeuverStrategyBarrelRoll>
     BasicManeuverStrategyLoop<aviator\BasicManeuverStrategyLoop>
     BasicManeuverStrategyLTAHover<aviator\BasicManeuverStrategyLTAHover>
     BasicManeuverStrategyIntercept<aviator\BasicManeuverStrategyIntercept>
     BasicManeuverStrategyRelativeBearing<aviator\BasicManeuverStrategyRelativeBearing>
     BasicManeuverStrategyRelativeCourse<aviator\BasicManeuverStrategyRelativeCourse>
     BasicManeuverStrategyRendezvous<aviator\BasicManeuverStrategyRendezvous>
     BasicManeuverStrategyStationkeeping<aviator\BasicManeuverStrategyStationkeeping>
     BasicManeuverStrategyRelativeFPA<aviator\BasicManeuverStrategyRelativeFPA>
     BasicManeuverStrategyRelSpeedAltitude<aviator\BasicManeuverStrategyRelSpeedAltitude>
     BasicManeuverStrategyBezier<aviator\BasicManeuverStrategyBezier>
     BasicManeuverStrategyPushPull<aviator\BasicManeuverStrategyPushPull>
     ProcedureHoldingCircular<aviator\ProcedureHoldingCircular>
     ProcedureHoldingFigure8<aviator\ProcedureHoldingFigure8>
     ProcedureHoldingRacetrack<aviator\ProcedureHoldingRacetrack>
     ProcedureTransitionToHover<aviator\ProcedureTransitionToHover>
     ProcedureTerrainFollow<aviator\ProcedureTerrainFollow>
     ProcedureHover<aviator\ProcedureHover>
     ProcedureHoverTranslate<aviator\ProcedureHoverTranslate>
     ProcedureTransitionToForwardFlight<aviator\ProcedureTransitionToForwardFlight>
     HoverAltitudeOptions<aviator\HoverAltitudeOptions>
     ProcedureVerticalTakeoff<aviator\ProcedureVerticalTakeoff>
     ProcedureVerticalLanding<aviator\ProcedureVerticalLanding>
     ProcedureReferenceState<aviator\ProcedureReferenceState>
     ProcedureSuperProcedure<aviator\ProcedureSuperProcedure>
     ProcedureLaunch<aviator\ProcedureLaunch>
     ProcedureAirway<aviator\ProcedureAirway>
     ProcedureAirwayRouter<aviator\ProcedureAirwayRouter>
     ProcedureAreaTargetSearch<aviator\ProcedureAreaTargetSearch>
     ProcedureFormationRecover<aviator\ProcedureFormationRecover>
     ProcedureInFormation<aviator\ProcedureInFormation>
     ProcedureParallelFlightLine<aviator\ProcedureParallelFlightLine>
     ProcedureVGTPoint<aviator\ProcedureVGTPoint>
     PerformanceModelOptions<aviator\PerformanceModelOptions>
     AdvancedFixedWingTool<aviator\AdvancedFixedWingTool>
     AdvancedFixedWingExternalAero<aviator\AdvancedFixedWingExternalAero>
     AdvancedFixedWingSubsonicAero<aviator\AdvancedFixedWingSubsonicAero>
     AdvancedFixedWingSubSuperHypersonicAero<aviator\AdvancedFixedWingSubSuperHypersonicAero>
     AdvancedFixedWingSupersonicAero<aviator\AdvancedFixedWingSupersonicAero>
     PerformanceModel<aviator\PerformanceModel>
     AdvancedFixedWingGeometryBasic<aviator\AdvancedFixedWingGeometryBasic>
     AdvancedFixedWingGeometryVariable<aviator\AdvancedFixedWingGeometryVariable>
     AdvancedFixedWingElectricPowerplant<aviator\AdvancedFixedWingElectricPowerplant>
     AdvancedFixedWingExternalProp<aviator\AdvancedFixedWingExternalProp>
     AdvancedFixedWingSubSuperHypersonicProp<aviator\AdvancedFixedWingSubSuperHypersonicProp>
     AdvancedFixedWingPistonPowerplant<aviator\AdvancedFixedWingPistonPowerplant>
     AdvancedFixedWingEmpiricalJetEngine<aviator\AdvancedFixedWingEmpiricalJetEngine>
     AdvancedFixedWingTurbofanBasicABPowerplant<aviator\AdvancedFixedWingTurbofanBasicABPowerplant>
     AdvancedFixedWingTurbojetBasicABPowerplant<aviator\AdvancedFixedWingTurbojetBasicABPowerplant>
     AdvancedFixedWingTurbofanBasicABProp<aviator\AdvancedFixedWingTurbofanBasicABProp>
     AdvancedFixedWingTurbojetBasicABProp<aviator\AdvancedFixedWingTurbojetBasicABProp>
     AdvancedFixedWingTurbopropPowerplant<aviator\AdvancedFixedWingTurbopropPowerplant>
     MissileSimpleAero<aviator\MissileSimpleAero>
     MissileExternalAero<aviator\MissileExternalAero>
     MissileAdvancedAero<aviator\MissileAdvancedAero>
     MissileAero<aviator\MissileAero>
     MissileProp<aviator\MissileProp>
     MissileSimpleProp<aviator\MissileSimpleProp>
     MissileExternalProp<aviator\MissileExternalProp>
     MissileRamjetProp<aviator\MissileRamjetProp>
     MissileRocketProp<aviator\MissileRocketProp>
     MissileTurbojetProp<aviator\MissileTurbojetProp>
     ReferenceStateForwardFlightOptions<aviator\ReferenceStateForwardFlightOptions>
     ReferenceStateTakeoffLandingOptions<aviator\ReferenceStateTakeoffLandingOptions>
     ReferenceStateHoverOptions<aviator\ReferenceStateHoverOptions>
     ReferenceStateWeightOnWheelsOptions<aviator\ReferenceStateWeightOnWheelsOptions>
     SiteRunwayFromCatalog<aviator\SiteRunwayFromCatalog>
     SiteAirportFromCatalog<aviator\SiteAirportFromCatalog>
     SiteNavaidFromCatalog<aviator\SiteNavaidFromCatalog>
     SiteVTOLPointFromCatalog<aviator\SiteVTOLPointFromCatalog>
     SiteWaypointFromCatalog<aviator\SiteWaypointFromCatalog>
     NavaidCategory<aviator\NavaidCategory>
     VTOLPointCategory<aviator\VTOLPointCategory>
     WaypointCategory<aviator\WaypointCategory>
     ARINC424Navaid<aviator\ARINC424Navaid>
     ARINC424Helipad<aviator\ARINC424Helipad>
     ARINC424Waypoint<aviator\ARINC424Waypoint>
     UserVTOLPointSource<aviator\UserVTOLPointSource>
     UserVTOLPoint<aviator\UserVTOLPoint>
     UserWaypointSource<aviator\UserWaypointSource>
     UserWaypoint<aviator\UserWaypoint>
     PropulsionEfficiencies<aviator\PropulsionEfficiencies>
     FuelModelKeroseneAFPROP<aviator\FuelModelKeroseneAFPROP>
     FuelModelKeroseneCEA<aviator\FuelModelKeroseneCEA>
     AdvancedFixedWingRamjetBasic<aviator\AdvancedFixedWingRamjetBasic>
     AdvancedFixedWingScramjetBasic<aviator\AdvancedFixedWingScramjetBasic>
     AircraftVTOLModel<aviator\AircraftVTOLModel>
     AircraftVTOL<aviator\AircraftVTOL>
     AircraftTerrainFollowModel<aviator\AircraftTerrainFollowModel>
     AircraftTerrainFollow<aviator\AircraftTerrainFollow>
     BasicManeuverStrategyBallistic3D<aviator\BasicManeuverStrategyBallistic3D>
     ProcedureLaunchDynState<aviator\ProcedureLaunchDynState>
     ProcedureLaunchWaypoint<aviator\ProcedureLaunchWaypoint>
     SiteDynState<aviator\SiteDynState>
     BasicManeuverStrategyPitch3D<aviator\BasicManeuverStrategyPitch3D>
     RefuelDumpProperties<aviator\RefuelDumpProperties>
     ProcedureFastTimeOptions<aviator\ProcedureFastTimeOptions>
     BasicManeuverTargetPositionVel<aviator\BasicManeuverTargetPositionVel>
     BasicManeuverTargetPositionVelNoisyBrgRng<aviator\BasicManeuverTargetPositionVelNoisyBrgRng>
     BasicManeuverTargetPositionVelNoisySurfTgt<aviator\BasicManeuverTargetPositionVelNoisySurfTgt>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ ERROR_CODES<aviator\ERROR_CODES>
    ≔ CLOSURE_VALUE<aviator\CLOSURE_VALUE>
    ≔ PROCEDURE_TYPE<aviator\PROCEDURE_TYPE>
    ≔ SITE_TYPE<aviator\SITE_TYPE>
    ≔ BASIC_MANEUVER_STRATEGY<aviator\BASIC_MANEUVER_STRATEGY>
    ≔ STRAIGHT_AHEAD_REFERENCE_FRAME<aviator\STRAIGHT_AHEAD_REFERENCE_FRAME>
    ≔ AIRSPEED_TYPE<aviator\AIRSPEED_TYPE>
    ≔ AERO_PROP_SIMPLE_MODE<aviator\AERO_PROP_SIMPLE_MODE>
    ≔ AERO_PROP_FLIGHT_MODE<aviator\AERO_PROP_FLIGHT_MODE>
    ≔ PHASE_OF_FLIGHT<aviator\PHASE_OF_FLIGHT>
    ≔ CRUISE_SPEED<aviator\CRUISE_SPEED>
    ≔ TAKEOFF_MODE<aviator\TAKEOFF_MODE>
    ≔ APPROACH_MODE<aviator\APPROACH_MODE>
    ≔ NAVIGATOR_TURN_DIRECTION<aviator\NAVIGATOR_TURN_DIRECTION>
    ≔ BASIC_MANEUVER_FUEL_FLOW_TYPE<aviator\BASIC_MANEUVER_FUEL_FLOW_TYPE>
    ≔ BASIC_MANEUVER_ALTITUDE_LIMIT<aviator\BASIC_MANEUVER_ALTITUDE_LIMIT>
    ≔ RUNWAY_HIGH_LOW_END<aviator\RUNWAY_HIGH_LOW_END>
    ≔ BASIC_MANEUVER_REFERENCE_FRAME<aviator\BASIC_MANEUVER_REFERENCE_FRAME>
    ≔ BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT<aviator\BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT>
    ≔ ACCEL_MANEUVER_MODE<aviator\ACCEL_MANEUVER_MODE>
    ≔ AIRCRAFT_AERO_STRATEGY<aviator\AIRCRAFT_AERO_STRATEGY>
    ≔ AIRCRAFT_PROP_STRATEGY<aviator\AIRCRAFT_PROP_STRATEGY>
    ≔ AGL_MSL<aviator\AGL_MSL>
    ≔ LANDING_APPROACH_FIX_RANGE_MODE<aviator\LANDING_APPROACH_FIX_RANGE_MODE>
    ≔ ACCELERATION_ADVANCED_ACCEL_MODE<aviator\ACCELERATION_ADVANCED_ACCEL_MODE>
    ≔ ACCEL_MANEUVER_AERO_PROP_MODE<aviator\ACCEL_MANEUVER_AERO_PROP_MODE>
    ≔ BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS<aviator\BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS>
    ≔ BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE<aviator\BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE>
    ≔ TURN_MODE<aviator\TURN_MODE>
    ≔ POINT_TO_POINT_MODE<aviator\POINT_TO_POINT_MODE>
    ≔ ALTITUDE_CONSTRAINT_MANEUVER_MODE<aviator\ALTITUDE_CONSTRAINT_MANEUVER_MODE>
    ≔ WIND_MODEL_TYPE<aviator\WIND_MODEL_TYPE>
    ≔ WIND_ATMOS_MODEL_SOURCE<aviator\WIND_ATMOS_MODEL_SOURCE>
    ≔ ADDS_MSG_INTERP_TYPE<aviator\ADDS_MSG_INTERP_TYPE>
    ≔ ADDS_MISSING_MSG_TYPE<aviator\ADDS_MISSING_MSG_TYPE>
    ≔ ADDS_MSG_EXTRAP_TYPE<aviator\ADDS_MSG_EXTRAP_TYPE>
    ≔ ADDS_FORECAST_TYPE<aviator\ADDS_FORECAST_TYPE>
    ≔ ATMOSPHERE_MODEL<aviator\ATMOSPHERE_MODEL>
    ≔ SMOOTH_TURN_MODE<aviator\SMOOTH_TURN_MODE>
    ≔ PERF_MODEL_OVERRIDE<aviator\PERF_MODEL_OVERRIDE>
    ≔ BASIC_MANEUVER_AIRSPEED_MODE<aviator\BASIC_MANEUVER_AIRSPEED_MODE>
    ≔ AILERON_ROLL_FLIGHT_PATH<aviator\AILERON_ROLL_FLIGHT_PATH>
    ≔ ROLL_LEFT_RIGHT<aviator\ROLL_LEFT_RIGHT>
    ≔ ROLL_UPRIGHT_INVERTED<aviator\ROLL_UPRIGHT_INVERTED>
    ≔ AILERON_ROLL_MODE<aviator\AILERON_ROLL_MODE>
    ≔ FLY_AOA_LEFT_RIGHT<aviator\FLY_AOA_LEFT_RIGHT>
    ≔ SMOOTH_ACCEL_LEFT_RIGHT<aviator\SMOOTH_ACCEL_LEFT_RIGHT>
    ≔ PULL_MODE<aviator\PULL_MODE>
    ≔ ROLLING_PULL_MODE<aviator\ROLLING_PULL_MODE>
    ≔ SMOOTH_ACCEL_STOP_CONDITIONS<aviator\SMOOTH_ACCEL_STOP_CONDITIONS>
    ≔ AUTOPILOT_HORIZ_PLANE_MODE<aviator\AUTOPILOT_HORIZ_PLANE_MODE>
    ≔ ANGLE_MODE<aviator\ANGLE_MODE>
    ≔ HOVER_ALTITUDE_MODE<aviator\HOVER_ALTITUDE_MODE>
    ≔ HOVER_HEADING_MODE<aviator\HOVER_HEADING_MODE>
    ≔ AUTOPILOT_ALTITUDE_MODE<aviator\AUTOPILOT_ALTITUDE_MODE>
    ≔ AUTOPILOT_ALTITUDE_CONTROL_MODE<aviator\AUTOPILOT_ALTITUDE_CONTROL_MODE>
    ≔ CLOSURE_MODE<aviator\CLOSURE_MODE>
    ≔ INTERCEPT_MODE<aviator\INTERCEPT_MODE>
    ≔ RENDEZVOUS_STOP_CONDITION<aviator\RENDEZVOUS_STOP_CONDITION>
    ≔ FORMATION_FLYER_STOP_CONDITION<aviator\FORMATION_FLYER_STOP_CONDITION>
    ≔ EXT_EPHEM_FLIGHT_MODE<aviator\EXT_EPHEM_FLIGHT_MODE>
    ≔ ACCEL_PERF_MODEL_OVERRIDE<aviator\ACCEL_PERF_MODEL_OVERRIDE>
    ≔ STATIONKEEPING_STOP_CONDITION<aviator\STATIONKEEPING_STOP_CONDITION>
    ≔ TURN_DIRECTION<aviator\TURN_DIRECTION>
    ≔ PROFILE_CONTROL_LIMIT<aviator\PROFILE_CONTROL_LIMIT>
    ≔ REL_SPEED_ALTITUDE_STOP_CONDITION<aviator\REL_SPEED_ALTITUDE_STOP_CONDITION>
    ≔ RELATIVE_ALTITUDE_MODE<aviator\RELATIVE_ALTITUDE_MODE>
    ≔ FLY_TO_FLIGHT_PATH_ANGLE_MODE<aviator\FLY_TO_FLIGHT_PATH_ANGLE_MODE>
    ≔ PUSH_PULL<aviator\PUSH_PULL>
    ≔ ACCEL_MODE<aviator\ACCEL_MODE>
    ≔ DELAY_ALTITUDE_MODE<aviator\DELAY_ALTITUDE_MODE>
    ≔ JOIN_EXIT_ARC_METHOD<aviator\JOIN_EXIT_ARC_METHOD>
    ≔ FLIGHT_LINE_PROC_TYPE<aviator\FLIGHT_LINE_PROC_TYPE>
    ≔ TRANSITION_TO_HOVER_MODE<aviator\TRANSITION_TO_HOVER_MODE>
    ≔ VTOL_RATE_MODE<aviator\VTOL_RATE_MODE>
    ≔ HOLDING_PROFILE_MODE<aviator\HOLDING_PROFILE_MODE>
    ≔ HOLDING_DIRECTION<aviator\HOLDING_DIRECTION>
    ≔ HOLD_REFUEL_DUMP_MODE<aviator\HOLD_REFUEL_DUMP_MODE>
    ≔ HOLDING_ENTRY_MANEUVER<aviator\HOLDING_ENTRY_MANEUVER>
    ≔ VTOL_TRANSITION_MODE<aviator\VTOL_TRANSITION_MODE>
    ≔ VTOL_FINAL_HEADING_MODE<aviator\VTOL_FINAL_HEADING_MODE>
    ≔ VTOL_TRANSLATION_MODE<aviator\VTOL_TRANSLATION_MODE>
    ≔ VTOL_TRANSLATION_FINAL_COURSE_MODE<aviator\VTOL_TRANSLATION_FINAL_COURSE_MODE>
    ≔ HOVER_MODE<aviator\HOVER_MODE>
    ≔ VTOL_HEADING_MODE<aviator\VTOL_HEADING_MODE>
    ≔ VERT_LANDING_MODE<aviator\VERT_LANDING_MODE>
    ≔ LAUNCH_ATTITUDE_MODE<aviator\LAUNCH_ATTITUDE_MODE>
    ≔ FUEL_FLOW_TYPE<aviator\FUEL_FLOW_TYPE>
    ≔ LINE_ORIENTATION<aviator\LINE_ORIENTATION>
    ≔ REL_ABS_BEARING<aviator\REL_ABS_BEARING>
    ≔ BASIC_FIXED_WING_PROP_MODE<aviator\BASIC_FIXED_WING_PROP_MODE>
    ≔ CLIMB_SPEED_TYPE<aviator\CLIMB_SPEED_TYPE>
    ≔ CRUISE_MAX_PERF_SPEED_TYPE<aviator\CRUISE_MAX_PERF_SPEED_TYPE>
    ≔ DESCENT_SPEED_TYPE<aviator\DESCENT_SPEED_TYPE>
    ≔ TAKEOFF_LANDING_SPEED_MODE<aviator\TAKEOFF_LANDING_SPEED_MODE>
    ≔ DEPARTURE_SPEED_MODE<aviator\DEPARTURE_SPEED_MODE>
    ≔ ADVANCED_FIXED_WING_AERO_STRATEGY<aviator\ADVANCED_FIXED_WING_AERO_STRATEGY>
    ≔ ADVANCED_FIXED_WING_GEOMETRY<aviator\ADVANCED_FIXED_WING_GEOMETRY>
    ≔ ADVANCED_FIXED_WING_POWERPLANT_STRATEGY<aviator\ADVANCED_FIXED_WING_POWERPLANT_STRATEGY>
    ≔ MISSILE_AERO_STRATEGY<aviator\MISSILE_AERO_STRATEGY>
    ≔ MISSILE_PROP_STRATEGY<aviator\MISSILE_PROP_STRATEGY>
    ≔ ROTORCRAFT_POWERPLANT_TYPE<aviator\ROTORCRAFT_POWERPLANT_TYPE>
    ≔ MINIMIZE_SITE_PROC_TIME_DIFF<aviator\MINIMIZE_SITE_PROC_TIME_DIFF>
    ≔ STK_OBJECT_WAYPOINT_OFFSET_MODE<aviator\STK_OBJECT_WAYPOINT_OFFSET_MODE>
    ≔ SEARCH_PATTERN_COURSE_MODE<aviator\SEARCH_PATTERN_COURSE_MODE>
    ≔ DELAY_TURN_DIRECTION<aviator\DELAY_TURN_DIRECTION>
    ≔ TRAJECTORY_BLEND_MODE<aviator\TRAJECTORY_BLEND_MODE>
    ≔ REFERENCE_STATE_PERF_MODE<aviator\REFERENCE_STATE_PERF_MODE>
    ≔ REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE<aviator\REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE>
    ≔ REFERENCE_STATE_LATERAL_ACCEL_MODE<aviator\REFERENCE_STATE_LATERAL_ACCEL_MODE>
    ≔ REFERENCE_STATE_ATTITUDE_MODE<aviator\REFERENCE_STATE_ATTITUDE_MODE>
    ≔ AND_OR<aviator\AND_OR>
    ≔ JET_ENGINE_TECHNOLOGY_LEVEL<aviator\JET_ENGINE_TECHNOLOGY_LEVEL>
    ≔ JET_ENGINE_INTAKE_TYPE<aviator\JET_ENGINE_INTAKE_TYPE>
    ≔ JET_ENGINE_TURBINE_TYPE<aviator\JET_ENGINE_TURBINE_TYPE>
    ≔ JET_ENGINE_EXHAUST_NOZZLE_TYPE<aviator\JET_ENGINE_EXHAUST_NOZZLE_TYPE>
    ≔ JET_FUEL_TYPE<aviator\JET_FUEL_TYPE>
    ≔ AFPROP_FUEL_TYPE<aviator\AFPROP_FUEL_TYPE>
    ≔ CEA_FUEL_TYPE<aviator\CEA_FUEL_TYPE>
    ≔ TURBINE_MODE<aviator\TURBINE_MODE>
    ≔ RAMJET_MODE<aviator\RAMJET_MODE>
    ≔ SCRAMJET_MODE<aviator\SCRAMJET_MODE>
    ≔ NUMERICAL_INTEGRATOR<aviator\NUMERICAL_INTEGRATOR>
    ≔ BALLISTIC_3D_CONTROL_MODE<aviator\BALLISTIC_3D_CONTROL_MODE>
    ≔ LAUNCH_DYN_STATE_COORD_FRAME<aviator\LAUNCH_DYN_STATE_COORD_FRAME>
    ≔ LAUNCH_DYN_STATE_BEARING_REFERENCE<aviator\LAUNCH_DYN_STATE_BEARING_REFERENCE>
    ≔ ALTITUDE_REFERENCE<aviator\ALTITUDE_REFERENCE>
    ≔ SMOOTH_TURN_FPA_MODE<aviator\SMOOTH_TURN_FPA_MODE>
    ≔ PITCH_3D_CONTROL_MODE<aviator\PITCH_3D_CONTROL_MODE>
    ≔ REFUEL_DUMP_MODE<aviator\REFUEL_DUMP_MODE>
    ≔ BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE<aviator\BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE>
    ≔ TARGET_POSITION_VEL_TYPE<aviator\TARGET_POSITION_VEL_TYPE>
    ≔ EPHEM_SHIFT_ROTATE_ALTITUDE_MODE<aviator\EPHEM_SHIFT_ROTATE_ALTITUDE_MODE>
    ≔ EPHEM_SHIFT_ROTATE_COURSE_MODE<aviator\EPHEM_SHIFT_ROTATE_COURSE_MODE>

