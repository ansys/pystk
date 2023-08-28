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

    AVTR_ERROR_CODES
    AVTR_CLOSURE_VALUE
    AVTR_PROCEDURE_TYPE
    AVTR_SITE_TYPE
    AVTR_BASIC_MANEUVER_STRATEGY
    AVTR_STRAIGHT_AHEAD_REF_FRAME
    AVTR_AIRSPEED_TYPE
    AVTR_AERO_PROP_SIMPLE_MODE
    AVTR_AERO_PROP_FLIGHT_MODE
    AVTR_PHASE_OF_FLIGHT
    AVTR_CRUISE_SPEED
    AVTR_TAKEOFF_MODE
    AVTR_APPROACH_MODE
    AVTR_NAVIGATOR_TURN_DIR
    AVTR_BASIC_MANEUVER_FUEL_FLOW_TYPE
    AVTR_BASIC_MANEUVER_ALTITUDE_LIMIT
    AVTR_RUNWAY_HIGH_LOW_END
    AVTR_BASIC_MANEUVER_REF_FRAME
    AVTR_BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT
    AVTR_ACCEL_MANEUVER_MODE
    AVTR_AIRCRAFT_AERO_STRATEGY
    AVTR_AIRCRAFT_PROP_STRATEGY
    AVTR_AGLMSL
    AVTR_LANDING_APPROACH_FIX_RANGE_MODE
    AVTR_ACCELERATION_ADV_ACCEL_MODE
    AVTR_ACCEL_MANEUVER_AERO_PROP_MODE
    AVTR_BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS
    AVTR_BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE
    AVTR_TURN_MODE
    AVTR_POINT_TO_POINT_MODE
    AVTR_ALTITUDE_CONSTRAINT_MANEUVER_MODE
    AVTR_WIND_MODEL_TYPE
    AVTR_WIND_ATMOS_MODEL_SOURCE
    AVTR_ADDS_MSG_INTERP_TYPE
    AVTR_ADDS_MISSING_MSG_TYPE
    AVTR_ADDS_MSG_EXTRAP_TYPE
    AVTR_ADDS_FORECAST_TYPE
    AVTR_ATMOSPHERE_MODEL
    AVTR_SMOOTH_TURN_MODE
    AVTR_PERF_MODEL_OVERRIDE
    AVTR_BASIC_MANEUVER_AIRSPEED_MODE
    AVTR_AILERON_ROLL_FLIGHT_PATH
    AVTR_ROLL_LEFT_RIGHT
    AVTR_ROLL_UPRIGHT_INVERTED
    AVTR_AILERON_ROLL_MODE
    AVTR_FLY_AOA_LEFT_RIGHT
    AVTR_SMOOTH_ACCEL_LEFT_RIGHT
    AVTR_PULL_MODE
    AVTR_ROLLING_PULL_MODE
    AVTR_SMOOTH_ACCEL_STOP_CONDITIONS
    AVTR_AUTOPILOT_HORIZ_PLANE_MODE
    AVTR_ANGLE_MODE
    AVTR_HOVER_ALTITUDE_MODE
    AVTR_HOVER_HEADING_MODE
    AVTR_AUTOPILOT_ALTITUDE_MODE
    AVTR_AUTOPILOT_ALTITUDE_CONTROL_MODE
    AVTR_CLOSURE_MODE
    AVTR_INTERCEPT_MODE
    AVTR_RENDEZVOUS_STOP_CONDITION
    AVTR_FORMATION_FLYER_STOP_CONDITION
    AVTR_EXT_EPHEM_FLIGHT_MODE
    AVTR_ACCEL_PERF_MODEL_OVERRIDE
    AVTR_STATIONKEEPING_STOP_CONDITION
    AVTR_TURN_DIRECTION
    AVTR_PROFILE_CONTROL_LIMIT
    AVTR_REL_SPEED_ALT_STOP_CONDITION
    AVTR_RELATIVE_ALTITUDE_MODE
    AVTR_FLY_TO_FLIGHT_PATH_ANGLE_MODE
    AVTR_PUSH_PULL
    AVTR_ACCEL_MODE
    AVTR_DELAY_ALT_MODE
    AVTR_JOIN_EXIT_ARC_METHOD
    AVTR_FLIGHT_LINE_PROC_TYPE
    AVTR_TRANSITION_TO_HOVER_MODE
    AVTR_VTOL_RATE_MODE
    AVTR_HOLDING_PROFILE_MODE
    AVTR_HOLDING_DIRECTION
    AVTR_HOLD_REFUEL_DUMP_MODE
    AVTR_HOLDING_ENTRY_MANEUVER
    AVTR_VTOL_TRANSITION_MODE
    AVTR_VTOL_FINAL_HEADING_MODE
    AVTR_VTOL_TRANSLATION_MODE
    AVTR_VTOL_TRANSLATION_FINAL_COURSE_MODE
    AVTR_HOVER_MODE
    AVTR_VTOL_HEADING_MODE
    AVTR_VERT_LANDING_MODE
    AVTR_LAUNCH_ATTITUDE_MODE
    AVTR_FUEL_FLOW_TYPE
    AVTR_LINE_ORIENTATION
    AVTR_REL_ABS_BEARING
    AVTR_BASIC_FIXED_WING_PROP_MODE
    AVTR_CLIMB_SPEED_TYPE
    AVTR_CRUISE_MAX_PERF_SPEED_TYPE
    AVTR_DESCENT_SPEED_TYPE
    AVTR_TAKEOFF_LANDING_SPEED_MODE
    AVTR_DEPARTURE_SPEED_MODE
    AVTR_ADV_FIXED_WING_AERO_STRATEGY
    AVTR_ADV_FIXED_WING_GEOMETRY
    AVTR_ADV_FIXED_WING_POWERPLANT_STRATEGY
    AVTR_MISSILE_AERO_STRATEGY
    AVTR_MISSILE_PROP_STRATEGY
    AVTR_ROTORCRAFT_POWERPLANT_TYPE
    AVTR_MINIMIZE_SITE_PROC_TIME_DIFF
    AVTR_STK_OBJECT_WAYPOINT_OFFSET_MODE
    AVTR_SEARCH_PATTERN_COURSE_MODE
    AVTR_DELAY_TURN_DIR
    AVTR_TRAJECTORY_BLEND_MODE
    AVTR_REF_STATE_PERF_MODE
    AVTR_REF_STATE_LONGITUDINAL_ACCEL_MODE
    AVTR_REF_STATE_LATERAL_ACCEL_MODE
    AVTR_REF_STATE_ATTITUDE_MODE
    AVTR_AND_OR
    AVTR_JET_ENGINE_TECHNOLOGY_LEVEL
    AVTR_JET_ENGINE_INTAKE_TYPE
    AVTR_JET_ENGINE_TURBINE_TYPE
    AVTR_JET_ENGINE_EXHAUST_NOZZLE_TYPE
    AVTR_JET_FUEL_TYPE
    AVTR_AFPROP_FUEL_TYPE
    AVTR_CEA_FUEL_TYPE
    AVTR_TURBINE_MODE
    AVTR_RAMJET_MODE
    AVTR_SCRAMJET_MODE
    AVTR_NUMERICAL_INTEGRATOR
    AVTR_BALLISTIC3_D_CONTROL_MODE
    AVTR_LAUNCH_DYN_STATE_COORD_FRAME
    AVTR_LAUNCH_DYN_STATE_BEARING_REF
    AVTR_ALTITUDE_REF
    AVTR_SMOOTH_TURN_FPA_MODE
    AVTR_PITCH3_D_CONTROL_MODE
    AVTR_REFUEL_DUMP_MODE
    AVTR_BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE


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

.. autoenum:: AVTR_ERROR_CODES
    :members:
.. autoenum:: AVTR_CLOSURE_VALUE
    :members:
.. autoenum:: AVTR_PROCEDURE_TYPE
    :members:
.. autoenum:: AVTR_SITE_TYPE
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_STRATEGY
    :members:
.. autoenum:: AVTR_STRAIGHT_AHEAD_REF_FRAME
    :members:
.. autoenum:: AVTR_AIRSPEED_TYPE
    :members:
.. autoenum:: AVTR_AERO_PROP_SIMPLE_MODE
    :members:
.. autoenum:: AVTR_AERO_PROP_FLIGHT_MODE
    :members:
.. autoenum:: AVTR_PHASE_OF_FLIGHT
    :members:
.. autoenum:: AVTR_CRUISE_SPEED
    :members:
.. autoenum:: AVTR_TAKEOFF_MODE
    :members:
.. autoenum:: AVTR_APPROACH_MODE
    :members:
.. autoenum:: AVTR_NAVIGATOR_TURN_DIR
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_FUEL_FLOW_TYPE
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_ALTITUDE_LIMIT
    :members:
.. autoenum:: AVTR_RUNWAY_HIGH_LOW_END
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_REF_FRAME
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT
    :members:
.. autoenum:: AVTR_ACCEL_MANEUVER_MODE
    :members:
.. autoenum:: AVTR_AIRCRAFT_AERO_STRATEGY
    :members:
.. autoenum:: AVTR_AIRCRAFT_PROP_STRATEGY
    :members:
.. autoenum:: AVTR_AGLMSL
    :members:
.. autoenum:: AVTR_LANDING_APPROACH_FIX_RANGE_MODE
    :members:
.. autoenum:: AVTR_ACCELERATION_ADV_ACCEL_MODE
    :members:
.. autoenum:: AVTR_ACCEL_MANEUVER_AERO_PROP_MODE
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE
    :members:
.. autoenum:: AVTR_TURN_MODE
    :members:
.. autoenum:: AVTR_POINT_TO_POINT_MODE
    :members:
.. autoenum:: AVTR_ALTITUDE_CONSTRAINT_MANEUVER_MODE
    :members:
.. autoenum:: AVTR_WIND_MODEL_TYPE
    :members:
.. autoenum:: AVTR_WIND_ATMOS_MODEL_SOURCE
    :members:
.. autoenum:: AVTR_ADDS_MSG_INTERP_TYPE
    :members:
.. autoenum:: AVTR_ADDS_MISSING_MSG_TYPE
    :members:
.. autoenum:: AVTR_ADDS_MSG_EXTRAP_TYPE
    :members:
.. autoenum:: AVTR_ADDS_FORECAST_TYPE
    :members:
.. autoenum:: AVTR_ATMOSPHERE_MODEL
    :members:
.. autoenum:: AVTR_SMOOTH_TURN_MODE
    :members:
.. autoenum:: AVTR_PERF_MODEL_OVERRIDE
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_AIRSPEED_MODE
    :members:
.. autoenum:: AVTR_AILERON_ROLL_FLIGHT_PATH
    :members:
.. autoenum:: AVTR_ROLL_LEFT_RIGHT
    :members:
.. autoenum:: AVTR_ROLL_UPRIGHT_INVERTED
    :members:
.. autoenum:: AVTR_AILERON_ROLL_MODE
    :members:
.. autoenum:: AVTR_FLY_AOA_LEFT_RIGHT
    :members:
.. autoenum:: AVTR_SMOOTH_ACCEL_LEFT_RIGHT
    :members:
.. autoenum:: AVTR_PULL_MODE
    :members:
.. autoenum:: AVTR_ROLLING_PULL_MODE
    :members:
.. autoenum:: AVTR_SMOOTH_ACCEL_STOP_CONDITIONS
    :members:
.. autoenum:: AVTR_AUTOPILOT_HORIZ_PLANE_MODE
    :members:
.. autoenum:: AVTR_ANGLE_MODE
    :members:
.. autoenum:: AVTR_HOVER_ALTITUDE_MODE
    :members:
.. autoenum:: AVTR_HOVER_HEADING_MODE
    :members:
.. autoenum:: AVTR_AUTOPILOT_ALTITUDE_MODE
    :members:
.. autoenum:: AVTR_AUTOPILOT_ALTITUDE_CONTROL_MODE
    :members:
.. autoenum:: AVTR_CLOSURE_MODE
    :members:
.. autoenum:: AVTR_INTERCEPT_MODE
    :members:
.. autoenum:: AVTR_RENDEZVOUS_STOP_CONDITION
    :members:
.. autoenum:: AVTR_FORMATION_FLYER_STOP_CONDITION
    :members:
.. autoenum:: AVTR_EXT_EPHEM_FLIGHT_MODE
    :members:
.. autoenum:: AVTR_ACCEL_PERF_MODEL_OVERRIDE
    :members:
.. autoenum:: AVTR_STATIONKEEPING_STOP_CONDITION
    :members:
.. autoenum:: AVTR_TURN_DIRECTION
    :members:
.. autoenum:: AVTR_PROFILE_CONTROL_LIMIT
    :members:
.. autoenum:: AVTR_REL_SPEED_ALT_STOP_CONDITION
    :members:
.. autoenum:: AVTR_RELATIVE_ALTITUDE_MODE
    :members:
.. autoenum:: AVTR_FLY_TO_FLIGHT_PATH_ANGLE_MODE
    :members:
.. autoenum:: AVTR_PUSH_PULL
    :members:
.. autoenum:: AVTR_ACCEL_MODE
    :members:
.. autoenum:: AVTR_DELAY_ALT_MODE
    :members:
.. autoenum:: AVTR_JOIN_EXIT_ARC_METHOD
    :members:
.. autoenum:: AVTR_FLIGHT_LINE_PROC_TYPE
    :members:
.. autoenum:: AVTR_TRANSITION_TO_HOVER_MODE
    :members:
.. autoenum:: AVTR_VTOL_RATE_MODE
    :members:
.. autoenum:: AVTR_HOLDING_PROFILE_MODE
    :members:
.. autoenum:: AVTR_HOLDING_DIRECTION
    :members:
.. autoenum:: AVTR_HOLD_REFUEL_DUMP_MODE
    :members:
.. autoenum:: AVTR_HOLDING_ENTRY_MANEUVER
    :members:
.. autoenum:: AVTR_VTOL_TRANSITION_MODE
    :members:
.. autoenum:: AVTR_VTOL_FINAL_HEADING_MODE
    :members:
.. autoenum:: AVTR_VTOL_TRANSLATION_MODE
    :members:
.. autoenum:: AVTR_VTOL_TRANSLATION_FINAL_COURSE_MODE
    :members:
.. autoenum:: AVTR_HOVER_MODE
    :members:
.. autoenum:: AVTR_VTOL_HEADING_MODE
    :members:
.. autoenum:: AVTR_VERT_LANDING_MODE
    :members:
.. autoenum:: AVTR_LAUNCH_ATTITUDE_MODE
    :members:
.. autoenum:: AVTR_FUEL_FLOW_TYPE
    :members:
.. autoenum:: AVTR_LINE_ORIENTATION
    :members:
.. autoenum:: AVTR_REL_ABS_BEARING
    :members:
.. autoenum:: AVTR_BASIC_FIXED_WING_PROP_MODE
    :members:
.. autoenum:: AVTR_CLIMB_SPEED_TYPE
    :members:
.. autoenum:: AVTR_CRUISE_MAX_PERF_SPEED_TYPE
    :members:
.. autoenum:: AVTR_DESCENT_SPEED_TYPE
    :members:
.. autoenum:: AVTR_TAKEOFF_LANDING_SPEED_MODE
    :members:
.. autoenum:: AVTR_DEPARTURE_SPEED_MODE
    :members:
.. autoenum:: AVTR_ADV_FIXED_WING_AERO_STRATEGY
    :members:
.. autoenum:: AVTR_ADV_FIXED_WING_GEOMETRY
    :members:
.. autoenum:: AVTR_ADV_FIXED_WING_POWERPLANT_STRATEGY
    :members:
.. autoenum:: AVTR_MISSILE_AERO_STRATEGY
    :members:
.. autoenum:: AVTR_MISSILE_PROP_STRATEGY
    :members:
.. autoenum:: AVTR_ROTORCRAFT_POWERPLANT_TYPE
    :members:
.. autoenum:: AVTR_MINIMIZE_SITE_PROC_TIME_DIFF
    :members:
.. autoenum:: AVTR_STK_OBJECT_WAYPOINT_OFFSET_MODE
    :members:
.. autoenum:: AVTR_SEARCH_PATTERN_COURSE_MODE
    :members:
.. autoenum:: AVTR_DELAY_TURN_DIR
    :members:
.. autoenum:: AVTR_TRAJECTORY_BLEND_MODE
    :members:
.. autoenum:: AVTR_REF_STATE_PERF_MODE
    :members:
.. autoenum:: AVTR_REF_STATE_LONGITUDINAL_ACCEL_MODE
    :members:
.. autoenum:: AVTR_REF_STATE_LATERAL_ACCEL_MODE
    :members:
.. autoenum:: AVTR_REF_STATE_ATTITUDE_MODE
    :members:
.. autoenum:: AVTR_AND_OR
    :members:
.. autoenum:: AVTR_JET_ENGINE_TECHNOLOGY_LEVEL
    :members:
.. autoenum:: AVTR_JET_ENGINE_INTAKE_TYPE
    :members:
.. autoenum:: AVTR_JET_ENGINE_TURBINE_TYPE
    :members:
.. autoenum:: AVTR_JET_ENGINE_EXHAUST_NOZZLE_TYPE
    :members:
.. autoenum:: AVTR_JET_FUEL_TYPE
    :members:
.. autoenum:: AVTR_AFPROP_FUEL_TYPE
    :members:
.. autoenum:: AVTR_CEA_FUEL_TYPE
    :members:
.. autoenum:: AVTR_TURBINE_MODE
    :members:
.. autoenum:: AVTR_RAMJET_MODE
    :members:
.. autoenum:: AVTR_SCRAMJET_MODE
    :members:
.. autoenum:: AVTR_NUMERICAL_INTEGRATOR
    :members:
.. autoenum:: AVTR_BALLISTIC3_D_CONTROL_MODE
    :members:
.. autoenum:: AVTR_LAUNCH_DYN_STATE_COORD_FRAME
    :members:
.. autoenum:: AVTR_LAUNCH_DYN_STATE_BEARING_REF
    :members:
.. autoenum:: AVTR_ALTITUDE_REF
    :members:
.. autoenum:: AVTR_SMOOTH_TURN_FPA_MODE
    :members:
.. autoenum:: AVTR_PITCH3_D_CONTROL_MODE
    :members:
.. autoenum:: AVTR_REFUEL_DUMP_MODE
    :members:
.. autoenum:: AVTR_BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE
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

