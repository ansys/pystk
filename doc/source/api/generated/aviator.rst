Module contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    ISite
    IWindModel
    IADDSMessage
    IFuelTankInternal
    IFuelTankExternal
    IPayloadStation
    IAircraftModel
    IAircraftSimpleAero
    ILevelTurns
    IAttitudeTransitions
    IClimbAndDescentTransitions
    ICatalogItem
    IAircraftBasicClimbModel
    IAircraftBasicAccelerationModel
    IAircraftCategory
    IRunwayCategory
    IBasicManeuverStrategy
    IAircraftVTOL
    IAircraftExternalAero
    IAircraftSimpleProp
    IAircraftExternalProp
    IAircraftBasicFixedWingProp
    IAircraftAdvClimbModel
    IAircraftBasicCruiseModel
    IAircraftAdvCruiseModel
    IAircraftBasicDescentModel
    IAircraftAdvDescentModel
    IAircraftBasicLandingModel
    IAircraftAdvLandingModel
    IAircraftBasicTakeoffModel
    IAircraftAdvTakeoffModel
    IAircraftVTOLModel
    IAircraftTerrainFollow
    IPerformanceModelOptions
    IAdvFixedWingTool
    IAdvFixedWingExternalAero
    IAdvFixedWingSubsonicAero
    IAdvFixedWingSubSuperHypersonicAero
    IAdvFixedWingSubSuperHypersonicProp
    IAdvFixedWingSupersonicAero
    IAdvFixedWingGeometryBasic
    IAdvFixedWingGeometryVariable
    IAdvFixedWingElectricPowerplant
    IAdvFixedWingExternalProp
    IAdvFixedWingPistonPowerplant
    IAdvFixedWingTurbopropPowerplant
    IAdvFixedWingEmpiricalJetEngine
    IAdvFixedWingTurbojetBasicABProp
    IAdvFixedWingTurbofanBasicABProp
    IAviatorVehicle
    IMissileModel
    IMissileAero
    IMissileProp
    IMissileSimpleAero
    IMissileSimpleProp
    IMissileExternalAero
    IMissileExternalProp
    IMissileAdvancedAero
    IMissileRamjetProp
    IMissileRocketProp
    IMissileTurbojetProp
    IRotorcraftModel
    IRotorcraftAero
    IRotorcraftProp
    IUserRunwaySource
    IUserRunway
    IARINC424Item
    IARINC424Source
    IDAFIFSource
    IUserVTOLPoint
    IUserVTOLPointSource
    IUserWaypoint
    IUserWaypointSource
    IPropulsionEfficiencies
    IFuelModelKeroseneAFPROP
    IFuelModelKeroseneCEA
    IAdvFixedWingRamjetBasic
    IAdvFixedWingScramjetBasic
    IRefuelDumpProperties
    IProcedureFastTimeOptions
    IAtmosphereModelBasic
    IAtmosphereModel
    IADDSMessageCollection
    IWindModelADDS
    IWindModelConstant
    IStation
    IStationCollection
    IConfiguration
    ICatalogSource
    IAircraftModels
    IMissileModels
    IRotorcraftModels
    IBasicFixedWingLiftHelper
    IAircraftBasicFixedWingAero
    IAircraftAero
    IAircraftProp
    IAircraftAccelerationMode
    IAircraftAdvAccelerationModel
    IAeroPropManeuverModeHelper
    ICatalogRunway
    ICatalogAirport
    ICatalogNavaid
    ICatalogVTOLPoint
    ICatalogWaypoint
    IARINC424Airport
    IDAFIFItem
    IARINC424Runway
    IAirportCategory
    INavaidCategory
    IVTOLPointCategory
    IWaypointCategory
    IAircraftClimb
    IAircraftCruise
    IAircraftDescent
    IAircraftLanding
    IAircraftTakeoff
    IAircraftAcceleration
    ICatalog
    IProcedureTimeOptions
    ICalculationOptions
    INavigationOptions
    IAltitudeMSLAndLevelOffOptions
    IAltitudeMSLOptions
    IAltitudeOptions
    IHoverAltitudeOptions
    IArcAltitudeOptions
    IArcAltitudeAndDelayOptions
    IArcOptions
    IVerticalPlaneOptions
    IVerticalPlaneAndFlightPathOptions
    IArcVerticalPlaneOptions
    IEnrouteOptions
    IEnrouteAndDelayOptions
    IEnrouteTurnDirectionOptions
    ICruiseAirspeedOptions
    ICruiseAirspeedProfile
    ICruiseAirspeedAndProfileOptions
    IAutomationStrategyFactory
    IConnect
    IRunwayHeadingOptions
    IProcedure
    IProcedureCollection
    IPhase
    IPhaseCollection
    IMission
    IAviatorPropagator
    IPerformanceModel
    IAdvFixedWingGeometry
    IAdvFixedWingTurbofanBasicABPowerplant
    IAdvFixedWingTurbojetBasicABPowerplant
    IAdvFixedWingPowerplant
    ISiteUnknown
    IAircraftTerrainFollowModel
    IBasicManeuverTargetPositionVel
    IPropulsionThrust
    IBasicManeuverAirspeedOptions
    IBasicManeuverStrategyAileronRoll
    IBasicManeuverStrategyAutopilotNav
    IBasicManeuverStrategyAutopilotProf
    IBasicManeuverStrategyBarrelRoll
    IBasicManeuverStrategyLoop
    IBasicManeuverStrategyLTAHover
    IBasicManeuverStrategyFlyAOA
    IBasicManeuverStrategyPull
    IBasicManeuverStrategyRollingPull
    IBasicManeuverStrategySmoothAccel
    IBasicManeuverStrategySmoothTurn
    IBasicManeuverStrategySimpleTurn
    IBasicManeuverStrategyIntercept
    IBasicManeuverStrategyRelativeBearing
    IBasicManeuverStrategyRelativeCourse
    IBasicManeuverStrategyRendezvous
    IBasicManeuverStrategyStationkeeping
    IBasicManeuverStrategyRelativeFPA
    IBasicManeuverStrategyRelSpeedAltitude
    IBasicManeuverStrategyBezier
    IBasicManeuverStrategyPushPull
    IBasicManeuverStrategyGlideProfile
    IBasicManeuverStrategyCruiseProfile
    IBasicManeuverStrategyStraightAhead
    IBasicManeuverStrategyWeave
    IBasicManeuverStrategyBallistic3D
    IBasicManeuverStrategyPitch3D
    IBasicManeuverTargetPositionVelNoisyBrnRng
    IBasicManeuverTargetPositionVelNoisySurfTgt
    ITakeoffNormal
    ITakeoffDeparturePoint
    ITakeoffLowTransition
    IReferenceStateForwardFlightOptions
    IReferenceStateHoverOptions
    IReferenceStateWeightOnWheelsOptions
    IReferenceStateTakeoffLandingOptions
    ILandingEnterDownwindPattern
    ILandingInterceptGlideslope
    ILandingStandardInstrumentApproach
    IProcedureBasicManeuver
    ISiteWaypoint
    ISiteEndOfPrevProcedure
    ISiteVTOLPoint
    ISiteSTKVehicle
    ISiteReferenceState
    ISiteSuperProcedure
    ISiteRelToPrevProcedure
    ISiteSTKObjectWaypoint
    ISiteSTKStaticObject
    ISiteRelToSTKObject
    ISiteSTKAreaTarget
    ISiteRunway
    IProcedureLanding
    IProcedureEnroute
    IProcedureExtEphem
    IProcedureFormationFlyer
    IProcedureBasicPointToPoint
    IProcedureDelay
    IProcedureTakeoff
    IProcedureArcEnroute
    IProcedureArcPointToPoint
    IProcedureFlightLine
    IProcedureHoldingCircular
    IProcedureHoldingFigure8
    IProcedureHoldingRacetrack
    IProcedureTransitionToHover
    IProcedureTerrainFollow
    IProcedureHover
    IProcedureHoverTranslate
    IProcedureTransitionToForwardFlight
    IProcedureVerticalTakeoff
    IProcedureVerticalLanding
    IProcedureReferenceState
    IProcedureSuperProcedure
    IProcedureLaunch
    IProcedureAirway
    IProcedureAirwayRouter
    IProcedureAreaTargetSearch
    IProcedureFormationRecover
    IProcedureInFormation
    IProcedureParallelFlightLine
    IProcedureVGTPoint
    ISiteRunwayFromCatalog
    ISiteAirportFromCatalog
    ISiteNavaidFromCatalog
    ISiteVTOLPointFromCatalog
    ISiteWaypointFromCatalog
    IProcedureLaunchDynState
    IProcedureLaunchWaypoint
    ISiteDynState


Enumerations
~~~~~~~~~~~~

.. autosummary::

    ERROR_CODES
    CLOSURE_VALUE
    PROCEDURE_TYPE
    SITE_TYPE
    BASIC_MANEUVER_STRATEGY
    STRAIGHT_AHEAD_REFERENCE_FRAME
    AIRSPEED_TYPE
    AERO_PROP_SIMPLE_MODE
    AERO_PROP_FLIGHT_MODE
    PHASE_OF_FLIGHT
    CRUISE_SPEED
    TAKEOFF_MODE
    APPROACH_MODE
    NAVIGATOR_TURN_DIRECTION
    BASIC_MANEUVER_FUEL_FLOW_TYPE
    BASIC_MANEUVER_ALTITUDE_LIMIT
    RUNWAY_HIGH_LOW_END
    BASIC_MANEUVER_REFERENCE_FRAME
    BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT
    ACCEL_MANEUVER_MODE
    AIRCRAFT_AERO_STRATEGY
    AIRCRAFT_PROP_STRATEGY
    AGL_MSL
    LANDING_APPROACH_FIX_RANGE_MODE
    ACCELERATION_ADV_ACCEL_MODE
    ACCEL_MANEUVER_AERO_PROP_MODE
    BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS
    BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE
    TURN_MODE
    POINT_TO_POINT_MODE
    ALTITUDE_CONSTRAINT_MANEUVER_MODE
    WIND_MODEL_TYPE
    WIND_ATMOS_MODEL_SOURCE
    ADDS_MSG_INTERP_TYPE
    ADDS_MISSING_MSG_TYPE
    ADDS_MSG_EXTRAP_TYPE
    ADDS_FORECAST_TYPE
    ATMOSPHERE_MODEL
    SMOOTH_TURN_MODE
    PERF_MODEL_OVERRIDE
    BASIC_MANEUVER_AIRSPEED_MODE
    AILERON_ROLL_FLIGHT_PATH
    ROLL_LEFT_RIGHT
    ROLL_UPRIGHT_INVERTED
    AILERON_ROLL_MODE
    FLY_AOA_LEFT_RIGHT
    SMOOTH_ACCEL_LEFT_RIGHT
    PULL_MODE
    ROLLING_PULL_MODE
    SMOOTH_ACCEL_STOP_CONDITIONS
    AUTOPILOT_HORIZ_PLANE_MODE
    ANGLE_MODE
    HOVER_ALTITUDE_MODE
    HOVER_HEADING_MODE
    AUTOPILOT_ALTITUDE_MODE
    AUTOPILOT_ALTITUDE_CONTROL_MODE
    CLOSURE_MODE
    INTERCEPT_MODE
    RENDEZVOUS_STOP_CONDITION
    FORMATION_FLYER_STOP_CONDITION
    EXT_EPHEM_FLIGHT_MODE
    ACCEL_PERF_MODEL_OVERRIDE
    STATIONKEEPING_STOP_CONDITION
    TURN_DIRECTION
    PROFILE_CONTROL_LIMIT
    REL_SPEED_ALTITUDE_STOP_CONDITION
    RELATIVE_ALTITUDE_MODE
    FLY_TO_FLIGHT_PATH_ANGLE_MODE
    PUSH_PULL
    ACCEL_MODE
    DELAY_ALTITUDE_MODE
    JOIN_EXIT_ARC_METHOD
    FLIGHT_LINE_PROC_TYPE
    TRANSITION_TO_HOVER_MODE
    VTOL_RATE_MODE
    HOLDING_PROFILE_MODE
    HOLDING_DIRECTION
    HOLD_REFUEL_DUMP_MODE
    HOLDING_ENTRY_MANEUVER
    VTOL_TRANSITION_MODE
    VTOL_FINAL_HEADING_MODE
    VTOL_TRANSLATION_MODE
    VTOL_TRANSLATION_FINAL_COURSE_MODE
    HOVER_MODE
    VTOL_HEADING_MODE
    VERT_LANDING_MODE
    LAUNCH_ATTITUDE_MODE
    FUEL_FLOW_TYPE
    LINE_ORIENTATION
    REL_ABS_BEARING
    BASIC_FIXED_WING_PROP_MODE
    CLIMB_SPEED_TYPE
    CRUISE_MAX_PERF_SPEED_TYPE
    DESCENT_SPEED_TYPE
    TAKEOFF_LANDING_SPEED_MODE
    DEPARTURE_SPEED_MODE
    ADV_FIXED_WING_AERO_STRATEGY
    ADV_FIXED_WING_GEOMETRY
    ADV_FIXED_WING_POWERPLANT_STRATEGY
    MISSILE_AERO_STRATEGY
    MISSILE_PROP_STRATEGY
    ROTORCRAFT_POWERPLANT_TYPE
    MINIMIZE_SITE_PROC_TIME_DIFF
    STK_OBJECT_WAYPOINT_OFFSET_MODE
    SEARCH_PATTERN_COURSE_MODE
    DELAY_TURN_DIRECTION
    TRAJECTORY_BLEND_MODE
    REFERENCE_STATE_PERF_MODE
    REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE
    REFERENCE_STATE_LATERAL_ACCEL_MODE
    REFERENCE_STATE_ATTITUDE_MODE
    AND_OR
    JET_ENGINE_TECHNOLOGY_LEVEL
    JET_ENGINE_INTAKE_TYPE
    JET_ENGINE_TURBINE_TYPE
    JET_ENGINE_EXHAUST_NOZZLE_TYPE
    JET_FUEL_TYPE
    AFPROP_FUEL_TYPE
    CEA_FUEL_TYPE
    TURBINE_MODE
    RAMJET_MODE
    SCRAMJET_MODE
    NUMERICAL_INTEGRATOR
    BALLISTIC_3D_CONTROL_MODE
    LAUNCH_DYN_STATE_COORD_FRAME
    LAUNCH_DYN_STATE_BEARING_REFERENCE
    ALTITUDE_REFERENCE
    SMOOTH_TURN_FPA_MODE
    PITCH_3D_CONTROL_MODE
    REFUEL_DUMP_MODE
    BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE
    TARGET_POSITION_VEL_TYPE


Classes
~~~~~~~

.. autosummary::

    SiteWaypoint
    SiteEndOfPrevProcedure
    SiteVTOLPoint
    SiteReferenceState
    SiteSTKVehicle
    SiteSuperProcedure
    SiteRelToPrevProcedure
    SiteSTKObjectWaypoint
    SiteSTKStaticObject
    SiteRelToSTKObject
    SiteSTKAreaTarget
    SiteRunway
    Site
    ProcedureLanding
    ProcedureEnroute
    ProcedureExtEphem
    ProcedureFormationFlyer
    ProcedureBasicPointToPoint
    ProcedureArcEnroute
    ProcedureArcPointToPoint
    ProcedureFlightLine
    ProcedureDelay
    ProcedureTakeoff
    ProcedureCollection
    Phase
    PhaseCollection
    Mission
    AviatorPropagator
    ProcedureBasicManeuver
    BasicManeuverStrategyWeave
    ProcedureTimeOptions
    CalculationOptions
    AircraftCategory
    Catalog
    AircraftModel
    MissileModel
    RotorcraftModel
    RotorcraftAero
    RotorcraftProp
    AircraftAcceleration
    AircraftBasicAccelerationModel
    AircraftClimb
    AircraftCruise
    AircraftDescent
    AircraftLanding
    AircraftTakeoff
    AircraftBasicClimbModel
    AircraftAdvClimbModel
    AircraftBasicCruiseModel
    AircraftAdvCruiseModel
    AircraftBasicDescentModel
    AircraftAdvDescentModel
    AircraftBasicTakeoffModel
    AircraftAdvTakeoffModel
    AircraftBasicLandingModel
    AircraftAdvLandingModel
    AirportCategory
    ARINC424Airport
    ARINC424Runway
    DAFIFRunway
    DAFIFHelipad
    DAFIFWaypoint
    RunwayCategory
    UserRunwaySource
    UserRunway
    AltitudeMSLOptions
    AltitudeOptions
    ArcAltitudeOptions
    ArcAltitudeAndDelayOptions
    ArcOptions
    AltitudeMSLAndLevelOffOptions
    CruiseAirspeedOptions
    CruiseAirspeedProfile
    CruiseAirspeedAndProfileOptions
    LandingCruiseAirspeedAndProfileOptions
    EnrouteOptions
    EnrouteAndDelayOptions
    LandingEnrouteOptions
    EnrouteTurnDirectionOptions
    NavigationOptions
    VerticalPlaneOptions
    ArcVerticalPlaneOptions
    VerticalPlaneAndFlightPathOptions
    LandingVerticalPlaneOptions
    RunwayHeadingOptions
    LandingEnterDownwindPattern
    LandingInterceptGlideslope
    LandingStandardInstrumentApproach
    TakeoffDeparturePoint
    TakeoffLowTransition
    TakeoffNormal
    LevelTurns
    AttitudeTransitions
    ClimbAndDescentTransitions
    AeroPropManeuverModeHelper
    AircraftAdvAccelerationModel
    AircraftAccelerationMode
    AircraftSimpleAero
    AircraftExternalAero
    AircraftAero
    AircraftBasicFixedWingAero
    AircraftProp
    AircraftSimpleProp
    AircraftExternalProp
    AircraftBasicFixedWingProp
    ARINC424Source
    DAFIFSource
    BasicFixedWingFwdFlightLiftHelper
    BasicManeuverStrategyStraightAhead
    BasicManeuverStrategyCruiseProfile
    BasicManeuverStrategyGlideProfile
    AircraftModels
    MissileModels
    RotorcraftModels
    Configuration
    FuelTankInternal
    FuelTankExternal
    PayloadStation
    StationCollection
    WindModel
    WindModelConstant
    WindModelADDS
    ADDSMessage
    ADDSMessageCollection
    Procedure
    AtmosphereModel
    AtmosphereModelBasic
    BasicManeuverStrategySimpleTurn
    BasicManeuverStrategyAileronRoll
    BasicManeuverStrategyFlyAOA
    BasicManeuverStrategyPull
    BasicManeuverStrategyRollingPull
    BasicManeuverStrategySmoothAccel
    BasicManeuverStrategySmoothTurn
    BasicManeuverAirspeedOptions
    PropulsionThrust
    BasicManeuverStrategyAutopilotNav
    BasicManeuverStrategyAutopilotProf
    BasicManeuverStrategyBarrelRoll
    BasicManeuverStrategyLoop
    BasicManeuverStrategyLTAHover
    BasicManeuverStrategyIntercept
    BasicManeuverStrategyRelativeBearing
    BasicManeuverStrategyRelativeCourse
    BasicManeuverStrategyRendezvous
    BasicManeuverStrategyStationkeeping
    BasicManeuverStrategyRelativeFPA
    BasicManeuverStrategyRelSpeedAltitude
    BasicManeuverStrategyBezier
    BasicManeuverStrategyPushPull
    ProcedureHoldingCircular
    ProcedureHoldingFigure8
    ProcedureHoldingRacetrack
    ProcedureTransitionToHover
    ProcedureTerrainFollow
    ProcedureHover
    ProcedureHoverTranslate
    ProcedureTransitionToForwardFlight
    HoverAltitudeOptions
    ProcedureVerticalTakeoff
    ProcedureVerticalLanding
    ProcedureReferenceState
    ProcedureSuperProcedure
    ProcedureLaunch
    ProcedureAirway
    ProcedureAirwayRouter
    ProcedureAreaTargetSearch
    ProcedureFormationRecover
    ProcedureInFormation
    ProcedureParallelFlightLine
    ProcedureVGTPoint
    PerformanceModelOptions
    AdvFixedWingTool
    AdvFixedWingExternalAero
    AdvFixedWingSubsonicAero
    AdvFixedWingSubSuperHypersonicAero
    AdvFixedWingSupersonicAero
    PerformanceModel
    AdvFixedWingGeometryBasic
    AdvFixedWingGeometryVariable
    AdvFixedWingElectricPowerplant
    AdvFixedWingExternalProp
    AdvFixedWingSubSuperHypersonicProp
    AdvFixedWingPistonPowerplant
    AdvFixedWingEmpiricalJetEngine
    AdvFixedWingTurbofanBasicABPowerplant
    AdvFixedWingTurbojetBasicABPowerplant
    AdvFixedWingTurbofanBasicABProp
    AdvFixedWingTurbojetBasicABProp
    AdvFixedWingTurbopropPowerplant
    MissileSimpleAero
    MissileExternalAero
    MissileAdvancedAero
    MissileAero
    MissileProp
    MissileSimpleProp
    MissileExternalProp
    MissileRamjetProp
    MissileRocketProp
    MissileTurbojetProp
    ReferenceStateForwardFlightOptions
    ReferenceStateTakeoffLandingOptions
    ReferenceStateHoverOptions
    ReferenceStateWeightOnWheelsOptions
    SiteRunwayFromCatalog
    SiteAirportFromCatalog
    SiteNavaidFromCatalog
    SiteVTOLPointFromCatalog
    SiteWaypointFromCatalog
    NavaidCategory
    VTOLPointCategory
    WaypointCategory
    ARINC424Navaid
    ARINC424Helipad
    ARINC424Waypoint
    UserVTOLPointSource
    UserVTOLPoint
    UserWaypointSource
    UserWaypoint
    PropulsionEfficiencies
    FuelModelKeroseneAFPROP
    FuelModelKeroseneCEA
    AdvFixedWingRamjetBasic
    AdvFixedWingScramjetBasic
    AircraftVTOLModel
    AircraftVTOL
    AircraftTerrainFollowModel
    AircraftTerrainFollow
    BasicManeuverStrategyBallistic3D
    ProcedureLaunchDynState
    ProcedureLaunchWaypoint
    SiteDynState
    BasicManeuverStrategyPitch3D
    RefuelDumpProperties
    ProcedureFastTimeOptions
    BasicManeuverTargetPositionVel
    BasicManeuverTargetPositionVelNoisyBrnRng
    BasicManeuverTargetPositionVelNoisySurfTgt


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: ISite
    :members:
    :exclude-members: __init__
.. autoclass:: IWindModel
    :members:
    :exclude-members: __init__
.. autoclass:: IADDSMessage
    :members:
    :exclude-members: __init__
.. autoclass:: IFuelTankInternal
    :members:
    :exclude-members: __init__
.. autoclass:: IFuelTankExternal
    :members:
    :exclude-members: __init__
.. autoclass:: IPayloadStation
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: ILevelTurns
    :members:
    :exclude-members: __init__
.. autoclass:: IAttitudeTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: IClimbAndDescentTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: ICatalogItem
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftBasicClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftBasicAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IRunwayCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategy
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftVTOL
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftBasicFixedWingProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAdvClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftBasicCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAdvCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftBasicDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAdvDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftBasicLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAdvLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftBasicTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAdvTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftVTOLModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IPerformanceModelOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingTool
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingSubsonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingSubSuperHypersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingSubSuperHypersonicProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingSupersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingGeometryBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingGeometryVariable
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingElectricPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingPistonPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingTurbopropPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingEmpiricalJetEngine
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingTurbojetBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingTurbofanBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAviatorVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileModel
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileAero
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileProp
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileAdvancedAero
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileRamjetProp
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileRocketProp
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileTurbojetProp
    :members:
    :exclude-members: __init__
.. autoclass:: IRotorcraftModel
    :members:
    :exclude-members: __init__
.. autoclass:: IRotorcraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: IRotorcraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: IUserRunwaySource
    :members:
    :exclude-members: __init__
.. autoclass:: IUserRunway
    :members:
    :exclude-members: __init__
.. autoclass:: IARINC424Item
    :members:
    :exclude-members: __init__
.. autoclass:: IARINC424Source
    :members:
    :exclude-members: __init__
.. autoclass:: IDAFIFSource
    :members:
    :exclude-members: __init__
.. autoclass:: IUserVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IUserVTOLPointSource
    :members:
    :exclude-members: __init__
.. autoclass:: IUserWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IUserWaypointSource
    :members:
    :exclude-members: __init__
.. autoclass:: IPropulsionEfficiencies
    :members:
    :exclude-members: __init__
.. autoclass:: IFuelModelKeroseneAFPROP
    :members:
    :exclude-members: __init__
.. autoclass:: IFuelModelKeroseneCEA
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingRamjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingScramjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IRefuelDumpProperties
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureFastTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAtmosphereModelBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAtmosphereModel
    :members:
    :exclude-members: __init__
.. autoclass:: IADDSMessageCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IWindModelADDS
    :members:
    :exclude-members: __init__
.. autoclass:: IWindModelConstant
    :members:
    :exclude-members: __init__
.. autoclass:: IStation
    :members:
    :exclude-members: __init__
.. autoclass:: IStationCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IConfiguration
    :members:
    :exclude-members: __init__
.. autoclass:: ICatalogSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: IMissileModels
    :members:
    :exclude-members: __init__
.. autoclass:: IRotorcraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicFixedWingLiftHelper
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftBasicFixedWingAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAccelerationMode
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAdvAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAeroPropManeuverModeHelper
    :members:
    :exclude-members: __init__
.. autoclass:: ICatalogRunway
    :members:
    :exclude-members: __init__
.. autoclass:: ICatalogAirport
    :members:
    :exclude-members: __init__
.. autoclass:: ICatalogNavaid
    :members:
    :exclude-members: __init__
.. autoclass:: ICatalogVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: ICatalogWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IARINC424Airport
    :members:
    :exclude-members: __init__
.. autoclass:: IDAFIFItem
    :members:
    :exclude-members: __init__
.. autoclass:: IARINC424Runway
    :members:
    :exclude-members: __init__
.. autoclass:: IAirportCategory
    :members:
    :exclude-members: __init__
.. autoclass:: INavaidCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IVTOLPointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IWaypointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftClimb
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftCruise
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftDescent
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: ICatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ICalculationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: INavigationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAltitudeMSLAndLevelOffOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAltitudeMSLOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IHoverAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IArcAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IArcAltitudeAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IArcOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IVerticalPlaneAndFlightPathOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IArcVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IEnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IEnrouteAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IEnrouteTurnDirectionOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ICruiseAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ICruiseAirspeedProfile
    :members:
    :exclude-members: __init__
.. autoclass:: ICruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAutomationStrategyFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IConnect
    :members:
    :exclude-members: __init__
.. autoclass:: IRunwayHeadingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IPhase
    :members:
    :exclude-members: __init__
.. autoclass:: IPhaseCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IMission
    :members:
    :exclude-members: __init__
.. autoclass:: IAviatorPropagator
    :members:
    :exclude-members: __init__
.. autoclass:: IPerformanceModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingGeometry
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingTurbofanBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingTurbojetBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAdvFixedWingPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteUnknown
    :members:
    :exclude-members: __init__
.. autoclass:: IAircraftTerrainFollowModel
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverTargetPositionVel
    :members:
    :exclude-members: __init__
.. autoclass:: IPropulsionThrust
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyAileronRoll
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyAutopilotNav
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyAutopilotProf
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyBarrelRoll
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyLoop
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyLTAHover
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyFlyAOA
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyPull
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyRollingPull
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategySmoothAccel
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategySmoothTurn
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategySimpleTurn
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyIntercept
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyRelativeBearing
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyRelativeCourse
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyRendezvous
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyStationkeeping
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyRelativeFPA
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyRelSpeedAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyBezier
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyPushPull
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyGlideProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyCruiseProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyStraightAhead
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyWeave
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyBallistic3D
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverStrategyPitch3D
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverTargetPositionVelNoisyBrnRng
    :members:
    :exclude-members: __init__
.. autoclass:: IBasicManeuverTargetPositionVelNoisySurfTgt
    :members:
    :exclude-members: __init__
.. autoclass:: ITakeoffNormal
    :members:
    :exclude-members: __init__
.. autoclass:: ITakeoffDeparturePoint
    :members:
    :exclude-members: __init__
.. autoclass:: ITakeoffLowTransition
    :members:
    :exclude-members: __init__
.. autoclass:: IReferenceStateForwardFlightOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IReferenceStateHoverOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IReferenceStateWeightOnWheelsOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IReferenceStateTakeoffLandingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ILandingEnterDownwindPattern
    :members:
    :exclude-members: __init__
.. autoclass:: ILandingInterceptGlideslope
    :members:
    :exclude-members: __init__
.. autoclass:: ILandingStandardInstrumentApproach
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureBasicManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteEndOfPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteSTKVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteRelToPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteSTKObjectWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteSTKStaticObject
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteRelToSTKObject
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteSTKAreaTarget
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteRunway
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureExtEphem
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureFormationFlyer
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureBasicPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureDelay
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureArcEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureArcPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureHoldingCircular
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureHoldingFigure8
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureHoldingRacetrack
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureTransitionToHover
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureHover
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureHoverTranslate
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureTransitionToForwardFlight
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureVerticalTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureVerticalLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureAirway
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureAirwayRouter
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureAreaTargetSearch
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureFormationRecover
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureInFormation
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureParallelFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureVGTPoint
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteRunwayFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteAirportFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteNavaidFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteVTOLPointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteWaypointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureLaunchDynState
    :members:
    :exclude-members: __init__
.. autoclass:: IProcedureLaunchWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: ISiteDynState
    :members:
    :exclude-members: __init__


Enumerations
~~~~~~~~~~~~

.. autoenum:: ERROR_CODES
    :members:
.. autoenum:: CLOSURE_VALUE
    :members:
.. autoenum:: PROCEDURE_TYPE
    :members:
.. autoenum:: SITE_TYPE
    :members:
.. autoenum:: BASIC_MANEUVER_STRATEGY
    :members:
.. autoenum:: STRAIGHT_AHEAD_REFERENCE_FRAME
    :members:
.. autoenum:: AIRSPEED_TYPE
    :members:
.. autoenum:: AERO_PROP_SIMPLE_MODE
    :members:
.. autoenum:: AERO_PROP_FLIGHT_MODE
    :members:
.. autoenum:: PHASE_OF_FLIGHT
    :members:
.. autoenum:: CRUISE_SPEED
    :members:
.. autoenum:: TAKEOFF_MODE
    :members:
.. autoenum:: APPROACH_MODE
    :members:
.. autoenum:: NAVIGATOR_TURN_DIRECTION
    :members:
.. autoenum:: BASIC_MANEUVER_FUEL_FLOW_TYPE
    :members:
.. autoenum:: BASIC_MANEUVER_ALTITUDE_LIMIT
    :members:
.. autoenum:: RUNWAY_HIGH_LOW_END
    :members:
.. autoenum:: BASIC_MANEUVER_REFERENCE_FRAME
    :members:
.. autoenum:: BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT
    :members:
.. autoenum:: ACCEL_MANEUVER_MODE
    :members:
.. autoenum:: AIRCRAFT_AERO_STRATEGY
    :members:
.. autoenum:: AIRCRAFT_PROP_STRATEGY
    :members:
.. autoenum:: AGL_MSL
    :members:
.. autoenum:: LANDING_APPROACH_FIX_RANGE_MODE
    :members:
.. autoenum:: ACCELERATION_ADV_ACCEL_MODE
    :members:
.. autoenum:: ACCEL_MANEUVER_AERO_PROP_MODE
    :members:
.. autoenum:: BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS
    :members:
.. autoenum:: BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE
    :members:
.. autoenum:: TURN_MODE
    :members:
.. autoenum:: POINT_TO_POINT_MODE
    :members:
.. autoenum:: ALTITUDE_CONSTRAINT_MANEUVER_MODE
    :members:
.. autoenum:: WIND_MODEL_TYPE
    :members:
.. autoenum:: WIND_ATMOS_MODEL_SOURCE
    :members:
.. autoenum:: ADDS_MSG_INTERP_TYPE
    :members:
.. autoenum:: ADDS_MISSING_MSG_TYPE
    :members:
.. autoenum:: ADDS_MSG_EXTRAP_TYPE
    :members:
.. autoenum:: ADDS_FORECAST_TYPE
    :members:
.. autoenum:: ATMOSPHERE_MODEL
    :members:
.. autoenum:: SMOOTH_TURN_MODE
    :members:
.. autoenum:: PERF_MODEL_OVERRIDE
    :members:
.. autoenum:: BASIC_MANEUVER_AIRSPEED_MODE
    :members:
.. autoenum:: AILERON_ROLL_FLIGHT_PATH
    :members:
.. autoenum:: ROLL_LEFT_RIGHT
    :members:
.. autoenum:: ROLL_UPRIGHT_INVERTED
    :members:
.. autoenum:: AILERON_ROLL_MODE
    :members:
.. autoenum:: FLY_AOA_LEFT_RIGHT
    :members:
.. autoenum:: SMOOTH_ACCEL_LEFT_RIGHT
    :members:
.. autoenum:: PULL_MODE
    :members:
.. autoenum:: ROLLING_PULL_MODE
    :members:
.. autoenum:: SMOOTH_ACCEL_STOP_CONDITIONS
    :members:
.. autoenum:: AUTOPILOT_HORIZ_PLANE_MODE
    :members:
.. autoenum:: ANGLE_MODE
    :members:
.. autoenum:: HOVER_ALTITUDE_MODE
    :members:
.. autoenum:: HOVER_HEADING_MODE
    :members:
.. autoenum:: AUTOPILOT_ALTITUDE_MODE
    :members:
.. autoenum:: AUTOPILOT_ALTITUDE_CONTROL_MODE
    :members:
.. autoenum:: CLOSURE_MODE
    :members:
.. autoenum:: INTERCEPT_MODE
    :members:
.. autoenum:: RENDEZVOUS_STOP_CONDITION
    :members:
.. autoenum:: FORMATION_FLYER_STOP_CONDITION
    :members:
.. autoenum:: EXT_EPHEM_FLIGHT_MODE
    :members:
.. autoenum:: ACCEL_PERF_MODEL_OVERRIDE
    :members:
.. autoenum:: STATIONKEEPING_STOP_CONDITION
    :members:
.. autoenum:: TURN_DIRECTION
    :members:
.. autoenum:: PROFILE_CONTROL_LIMIT
    :members:
.. autoenum:: REL_SPEED_ALTITUDE_STOP_CONDITION
    :members:
.. autoenum:: RELATIVE_ALTITUDE_MODE
    :members:
.. autoenum:: FLY_TO_FLIGHT_PATH_ANGLE_MODE
    :members:
.. autoenum:: PUSH_PULL
    :members:
.. autoenum:: ACCEL_MODE
    :members:
.. autoenum:: DELAY_ALTITUDE_MODE
    :members:
.. autoenum:: JOIN_EXIT_ARC_METHOD
    :members:
.. autoenum:: FLIGHT_LINE_PROC_TYPE
    :members:
.. autoenum:: TRANSITION_TO_HOVER_MODE
    :members:
.. autoenum:: VTOL_RATE_MODE
    :members:
.. autoenum:: HOLDING_PROFILE_MODE
    :members:
.. autoenum:: HOLDING_DIRECTION
    :members:
.. autoenum:: HOLD_REFUEL_DUMP_MODE
    :members:
.. autoenum:: HOLDING_ENTRY_MANEUVER
    :members:
.. autoenum:: VTOL_TRANSITION_MODE
    :members:
.. autoenum:: VTOL_FINAL_HEADING_MODE
    :members:
.. autoenum:: VTOL_TRANSLATION_MODE
    :members:
.. autoenum:: VTOL_TRANSLATION_FINAL_COURSE_MODE
    :members:
.. autoenum:: HOVER_MODE
    :members:
.. autoenum:: VTOL_HEADING_MODE
    :members:
.. autoenum:: VERT_LANDING_MODE
    :members:
.. autoenum:: LAUNCH_ATTITUDE_MODE
    :members:
.. autoenum:: FUEL_FLOW_TYPE
    :members:
.. autoenum:: LINE_ORIENTATION
    :members:
.. autoenum:: REL_ABS_BEARING
    :members:
.. autoenum:: BASIC_FIXED_WING_PROP_MODE
    :members:
.. autoenum:: CLIMB_SPEED_TYPE
    :members:
.. autoenum:: CRUISE_MAX_PERF_SPEED_TYPE
    :members:
.. autoenum:: DESCENT_SPEED_TYPE
    :members:
.. autoenum:: TAKEOFF_LANDING_SPEED_MODE
    :members:
.. autoenum:: DEPARTURE_SPEED_MODE
    :members:
.. autoenum:: ADV_FIXED_WING_AERO_STRATEGY
    :members:
.. autoenum:: ADV_FIXED_WING_GEOMETRY
    :members:
.. autoenum:: ADV_FIXED_WING_POWERPLANT_STRATEGY
    :members:
.. autoenum:: MISSILE_AERO_STRATEGY
    :members:
.. autoenum:: MISSILE_PROP_STRATEGY
    :members:
.. autoenum:: ROTORCRAFT_POWERPLANT_TYPE
    :members:
.. autoenum:: MINIMIZE_SITE_PROC_TIME_DIFF
    :members:
.. autoenum:: STK_OBJECT_WAYPOINT_OFFSET_MODE
    :members:
.. autoenum:: SEARCH_PATTERN_COURSE_MODE
    :members:
.. autoenum:: DELAY_TURN_DIRECTION
    :members:
.. autoenum:: TRAJECTORY_BLEND_MODE
    :members:
.. autoenum:: REFERENCE_STATE_PERF_MODE
    :members:
.. autoenum:: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE
    :members:
.. autoenum:: REFERENCE_STATE_LATERAL_ACCEL_MODE
    :members:
.. autoenum:: REFERENCE_STATE_ATTITUDE_MODE
    :members:
.. autoenum:: AND_OR
    :members:
.. autoenum:: JET_ENGINE_TECHNOLOGY_LEVEL
    :members:
.. autoenum:: JET_ENGINE_INTAKE_TYPE
    :members:
.. autoenum:: JET_ENGINE_TURBINE_TYPE
    :members:
.. autoenum:: JET_ENGINE_EXHAUST_NOZZLE_TYPE
    :members:
.. autoenum:: JET_FUEL_TYPE
    :members:
.. autoenum:: AFPROP_FUEL_TYPE
    :members:
.. autoenum:: CEA_FUEL_TYPE
    :members:
.. autoenum:: TURBINE_MODE
    :members:
.. autoenum:: RAMJET_MODE
    :members:
.. autoenum:: SCRAMJET_MODE
    :members:
.. autoenum:: NUMERICAL_INTEGRATOR
    :members:
.. autoenum:: BALLISTIC_3D_CONTROL_MODE
    :members:
.. autoenum:: LAUNCH_DYN_STATE_COORD_FRAME
    :members:
.. autoenum:: LAUNCH_DYN_STATE_BEARING_REFERENCE
    :members:
.. autoenum:: ALTITUDE_REFERENCE
    :members:
.. autoenum:: SMOOTH_TURN_FPA_MODE
    :members:
.. autoenum:: PITCH_3D_CONTROL_MODE
    :members:
.. autoenum:: REFUEL_DUMP_MODE
    :members:
.. autoenum:: BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE
    :members:
.. autoenum:: TARGET_POSITION_VEL_TYPE
    :members:


Classes
~~~~~~~

.. autoclass:: SiteWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: SiteEndOfPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: SiteVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: SiteReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: SiteSTKVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: SiteSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: SiteRelToPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: SiteSTKObjectWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: SiteSTKStaticObject
    :members:
    :exclude-members: __init__
.. autoclass:: SiteRelToSTKObject
    :members:
    :exclude-members: __init__
.. autoclass:: SiteSTKAreaTarget
    :members:
    :exclude-members: __init__
.. autoclass:: SiteRunway
    :members:
    :exclude-members: __init__
.. autoclass:: Site
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureLanding
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureExtEphem
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureFormationFlyer
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureBasicPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureArcEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureArcPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureDelay
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureCollection
    :members:
    :exclude-members: __init__
.. autoclass:: Phase
    :members:
    :exclude-members: __init__
.. autoclass:: PhaseCollection
    :members:
    :exclude-members: __init__
.. autoclass:: Mission
    :members:
    :exclude-members: __init__
.. autoclass:: AviatorPropagator
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureBasicManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyWeave
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: CalculationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftCategory
    :members:
    :exclude-members: __init__
.. autoclass:: Catalog
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftModel
    :members:
    :exclude-members: __init__
.. autoclass:: MissileModel
    :members:
    :exclude-members: __init__
.. autoclass:: RotorcraftModel
    :members:
    :exclude-members: __init__
.. autoclass:: RotorcraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: RotorcraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftBasicAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftClimb
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftCruise
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftDescent
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftLanding
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftBasicClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAdvClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftBasicCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAdvCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftBasicDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAdvDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftBasicTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAdvTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftBasicLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAdvLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: AirportCategory
    :members:
    :exclude-members: __init__
.. autoclass:: ARINC424Airport
    :members:
    :exclude-members: __init__
.. autoclass:: ARINC424Runway
    :members:
    :exclude-members: __init__
.. autoclass:: DAFIFRunway
    :members:
    :exclude-members: __init__
.. autoclass:: DAFIFHelipad
    :members:
    :exclude-members: __init__
.. autoclass:: DAFIFWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: RunwayCategory
    :members:
    :exclude-members: __init__
.. autoclass:: UserRunwaySource
    :members:
    :exclude-members: __init__
.. autoclass:: UserRunway
    :members:
    :exclude-members: __init__
.. autoclass:: AltitudeMSLOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ArcAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ArcAltitudeAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ArcOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AltitudeMSLAndLevelOffOptions
    :members:
    :exclude-members: __init__
.. autoclass:: CruiseAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: CruiseAirspeedProfile
    :members:
    :exclude-members: __init__
.. autoclass:: CruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: LandingCruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: EnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: EnrouteAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: LandingEnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: EnrouteTurnDirectionOptions
    :members:
    :exclude-members: __init__
.. autoclass:: NavigationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: VerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ArcVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: VerticalPlaneAndFlightPathOptions
    :members:
    :exclude-members: __init__
.. autoclass:: LandingVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: RunwayHeadingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: LandingEnterDownwindPattern
    :members:
    :exclude-members: __init__
.. autoclass:: LandingInterceptGlideslope
    :members:
    :exclude-members: __init__
.. autoclass:: LandingStandardInstrumentApproach
    :members:
    :exclude-members: __init__
.. autoclass:: TakeoffDeparturePoint
    :members:
    :exclude-members: __init__
.. autoclass:: TakeoffLowTransition
    :members:
    :exclude-members: __init__
.. autoclass:: TakeoffNormal
    :members:
    :exclude-members: __init__
.. autoclass:: LevelTurns
    :members:
    :exclude-members: __init__
.. autoclass:: AttitudeTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: ClimbAndDescentTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: AeroPropManeuverModeHelper
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAdvAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAccelerationMode
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftBasicFixedWingAero
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftBasicFixedWingProp
    :members:
    :exclude-members: __init__
.. autoclass:: ARINC424Source
    :members:
    :exclude-members: __init__
.. autoclass:: DAFIFSource
    :members:
    :exclude-members: __init__
.. autoclass:: BasicFixedWingFwdFlightLiftHelper
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyStraightAhead
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyCruiseProfile
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyGlideProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: MissileModels
    :members:
    :exclude-members: __init__
.. autoclass:: RotorcraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: Configuration
    :members:
    :exclude-members: __init__
.. autoclass:: FuelTankInternal
    :members:
    :exclude-members: __init__
.. autoclass:: FuelTankExternal
    :members:
    :exclude-members: __init__
.. autoclass:: PayloadStation
    :members:
    :exclude-members: __init__
.. autoclass:: StationCollection
    :members:
    :exclude-members: __init__
.. autoclass:: WindModel
    :members:
    :exclude-members: __init__
.. autoclass:: WindModelConstant
    :members:
    :exclude-members: __init__
.. autoclass:: WindModelADDS
    :members:
    :exclude-members: __init__
.. autoclass:: ADDSMessage
    :members:
    :exclude-members: __init__
.. autoclass:: ADDSMessageCollection
    :members:
    :exclude-members: __init__
.. autoclass:: Procedure
    :members:
    :exclude-members: __init__
.. autoclass:: AtmosphereModel
    :members:
    :exclude-members: __init__
.. autoclass:: AtmosphereModelBasic
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategySimpleTurn
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyAileronRoll
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyFlyAOA
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyPull
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyRollingPull
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategySmoothAccel
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategySmoothTurn
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: PropulsionThrust
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyAutopilotNav
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyAutopilotProf
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyBarrelRoll
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyLoop
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyLTAHover
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyIntercept
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyRelativeBearing
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyRelativeCourse
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyRendezvous
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyStationkeeping
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyRelativeFPA
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyRelSpeedAltitude
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyBezier
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyPushPull
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureHoldingCircular
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureHoldingFigure8
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureHoldingRacetrack
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureTransitionToHover
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureHover
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureHoverTranslate
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureTransitionToForwardFlight
    :members:
    :exclude-members: __init__
.. autoclass:: HoverAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureVerticalTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureVerticalLanding
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureAirway
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureAirwayRouter
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureAreaTargetSearch
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureFormationRecover
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureInFormation
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureParallelFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureVGTPoint
    :members:
    :exclude-members: __init__
.. autoclass:: PerformanceModelOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingTool
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingSubsonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingSubSuperHypersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingSupersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: PerformanceModel
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingGeometryBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingGeometryVariable
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingElectricPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingSubSuperHypersonicProp
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingPistonPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingEmpiricalJetEngine
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingTurbofanBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingTurbojetBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingTurbofanBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingTurbojetBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingTurbopropPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: MissileSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: MissileExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: MissileAdvancedAero
    :members:
    :exclude-members: __init__
.. autoclass:: MissileAero
    :members:
    :exclude-members: __init__
.. autoclass:: MissileProp
    :members:
    :exclude-members: __init__
.. autoclass:: MissileSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: MissileExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: MissileRamjetProp
    :members:
    :exclude-members: __init__
.. autoclass:: MissileRocketProp
    :members:
    :exclude-members: __init__
.. autoclass:: MissileTurbojetProp
    :members:
    :exclude-members: __init__
.. autoclass:: ReferenceStateForwardFlightOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ReferenceStateTakeoffLandingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ReferenceStateHoverOptions
    :members:
    :exclude-members: __init__
.. autoclass:: ReferenceStateWeightOnWheelsOptions
    :members:
    :exclude-members: __init__
.. autoclass:: SiteRunwayFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: SiteAirportFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: SiteNavaidFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: SiteVTOLPointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: SiteWaypointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: NavaidCategory
    :members:
    :exclude-members: __init__
.. autoclass:: VTOLPointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: WaypointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: ARINC424Navaid
    :members:
    :exclude-members: __init__
.. autoclass:: ARINC424Helipad
    :members:
    :exclude-members: __init__
.. autoclass:: ARINC424Waypoint
    :members:
    :exclude-members: __init__
.. autoclass:: UserVTOLPointSource
    :members:
    :exclude-members: __init__
.. autoclass:: UserVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: UserWaypointSource
    :members:
    :exclude-members: __init__
.. autoclass:: UserWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: PropulsionEfficiencies
    :members:
    :exclude-members: __init__
.. autoclass:: FuelModelKeroseneAFPROP
    :members:
    :exclude-members: __init__
.. autoclass:: FuelModelKeroseneCEA
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingRamjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AdvFixedWingScramjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftVTOLModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftVTOL
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftTerrainFollowModel
    :members:
    :exclude-members: __init__
.. autoclass:: AircraftTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyBallistic3D
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureLaunchDynState
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureLaunchWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: SiteDynState
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverStrategyPitch3D
    :members:
    :exclude-members: __init__
.. autoclass:: RefuelDumpProperties
    :members:
    :exclude-members: __init__
.. autoclass:: ProcedureFastTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverTargetPositionVel
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverTargetPositionVelNoisyBrnRng
    :members:
    :exclude-members: __init__
.. autoclass:: BasicManeuverTargetPositionVelNoisySurfTgt
    :members:
    :exclude-members: __init__

