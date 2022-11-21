Module contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    IAgAvtrSite
    IAgAvtrWindModel
    IAgAvtrADDSMessage
    IAgAvtrFuelTankInternal
    IAgAvtrFuelTankExternal
    IAgAvtrPayloadStation
    IAgAvtrAircraft
    IAgAvtrAircraftSimpleAero
    IAgAvtrLevelTurns
    IAgAvtrAttitudeTransitions
    IAgAvtrClimbAndDescentTransitions
    IAgAvtrCatalogItem
    IAgAvtrAircraftBasicClimbModel
    IAgAvtrAircraftBasicAccelerationModel
    IAgAvtrAircraftCategory
    IAgAvtrRunwayCategory
    IAgAvtrBasicManeuverStrategy
    IAgAvtrAircraftVTOL
    IAgAvtrAircraftExternalAero
    IAgAvtrAircraftSimpleProp
    IAgAvtrAircraftExternalProp
    IAgAvtrAircraftBasicFixedWingProp
    IAgAvtrAircraftAdvClimbModel
    IAgAvtrAircraftBasicCruiseModel
    IAgAvtrAircraftAdvCruiseModel
    IAgAvtrAircraftBasicDescentModel
    IAgAvtrAircraftAdvDescentModel
    IAgAvtrAircraftBasicLandingModel
    IAgAvtrAircraftAdvLandingModel
    IAgAvtrAircraftBasicTakeoffModel
    IAgAvtrAircraftAdvTakeoffModel
    IAgAvtrAircraftVTOLModel
    IAgAvtrAircraftTerrainFollow
    IAgAvtrPerformanceModelOptions
    IAgAvtrAdvFixedWingTool
    IAgAvtrAdvFixedWingExternalAero
    IAgAvtrAdvFixedWingSubsonicAero
    IAgAvtrAdvFixedWingSubSuperHypersonicAero
    IAgAvtrAdvFixedWingSubSuperHypersonicProp
    IAgAvtrAdvFixedWingSupersonicAero
    IAgAvtrAdvFixedWingGeometryBasic
    IAgAvtrAdvFixedWingGeometryVariable
    IAgAvtrAdvFixedWingElectricPowerplant
    IAgAvtrAdvFixedWingExternalProp
    IAgAvtrAdvFixedWingPistonPowerplant
    IAgAvtrAdvFixedWingTurbopropPowerplant
    IAgAvtrAdvFixedWingEmpiricalJetEngine
    IAgAvtrAdvFixedWingTurbojetBasicABProp
    IAgAvtrAdvFixedWingTurbofanBasicABProp
    IAgAvtrVehicle
    IAgAvtrMissile
    IAgAvtrMissileAero
    IAgAvtrMissileProp
    IAgAvtrMissileSimpleAero
    IAgAvtrMissileSimpleProp
    IAgAvtrMissileExternalAero
    IAgAvtrMissileExternalProp
    IAgAvtrMissileAdvancedAero
    IAgAvtrMissileRamjetProp
    IAgAvtrMissileRocketProp
    IAgAvtrMissileTurbojetProp
    IAgAvtrRotorcraft
    IAgAvtrRotorcraftAero
    IAgAvtrRotorcraftProp
    IAgAvtrUserRunwaySource
    IAgAvtrUserRunway
    IAgAvtrARINC424Item
    IAgAvtrARINC424Source
    IAgAvtrDAFIFSource
    IAgAvtrUserVTOLPoint
    IAgAvtrUserVTOLPointSource
    IAgAvtrUserWaypoint
    IAgAvtrUserWaypointSource
    IAgAvtrPropulsionEfficiencies
    IAgAvtrFuelModelKeroseneAFPROP
    IAgAvtrFuelModelKeroseneCEA
    IAgAvtrAdvFixedWingRamjetBasic
    IAgAvtrAdvFixedWingScramjetBasic
    IAgAvtrRefuelDumpProperties
    IAgAvtrProcedureFastTimeOptions
    IAgAvtrAtmosphereModelBasic
    IAgAvtrAtmosphereModel
    IAgAvtrADDSMessageCollection
    IAgAvtrWindModelADDS
    IAgAvtrWindModelConstant
    IAgAvtrStation
    IAgAvtrStationCollection
    IAgAvtrConfiguration
    IAgAvtrCatalogSource
    IAgAvtrAircraftModels
    IAgAvtrMissileModels
    IAgAvtrRotorcraftModels
    IAgAvtrBasicFixedWingLiftHelper
    IAgAvtrAircraftBasicFixedWingAero
    IAgAvtrAircraftAero
    IAgAvtrAircraftProp
    IAgAvtrAircraftAccelerationMode
    IAgAvtrAircraftAdvAccelerationModel
    IAgAvtrAeroPropManeuverModeHelper
    IAgAvtrCatalogRunway
    IAgAvtrCatalogAirport
    IAgAvtrCatalogNavaid
    IAgAvtrCatalogVTOLPoint
    IAgAvtrCatalogWaypoint
    IAgAvtrARINC424Airport
    IAgAvtrDAFIFItem
    IAgAvtrARINC424Runway
    IAgAvtrAirportCategory
    IAgAvtrNavaidCategory
    IAgAvtrVTOLPointCategory
    IAgAvtrWaypointCategory
    IAgAvtrAircraftClimb
    IAgAvtrAircraftCruise
    IAgAvtrAircraftDescent
    IAgAvtrAircraftLanding
    IAgAvtrAircraftTakeoff
    IAgAvtrAircraftAcceleration
    IAgAvtrCatalog
    IAgAvtrProcedureTimeOptions
    IAgAvtrCalculationOptions
    IAgAvtrNavigationOptions
    IAgAvtrAltitudeMSLAndLevelOffOptions
    IAgAvtrAltitudeMSLOptions
    IAgAvtrAltitudeOptions
    IAgAvtrHoverAltitudeOptions
    IAgAvtrArcAltitudeOptions
    IAgAvtrArcAltitudeAndDelayOptions
    IAgAvtrArcOptions
    IAgAvtrVerticalPlaneOptions
    IAgAvtrVerticalPlaneAndFlightPathOptions
    IAgAvtrArcVerticalPlaneOptions
    IAgAvtrEnrouteOptions
    IAgAvtrEnrouteAndDelayOptions
    IAgAvtrEnrouteTurnDirectionOptions
    IAgAvtrCruiseAirspeedOptions
    IAgAvtrCruiseAirspeedProfile
    IAgAvtrCruiseAirspeedAndProfileOptions
    IAgAvtrAutomationStrategyFactory
    IAgAvtrConnect
    IAgAvtrRunwayHeadingOptions
    IAgAvtrProcedure
    IAgAvtrProcedureCollection
    IAgAvtrPhase
    IAgAvtrPhaseCollection
    IAgAvtrMission
    IAgAvtrPropagator
    IAgAvtrPerformanceModel
    IAgAvtrAdvFixedWingGeometry
    IAgAvtrAdvFixedWingTurbofanBasicABPowerplant
    IAgAvtrAdvFixedWingTurbojetBasicABPowerplant
    IAgAvtrAdvFixedWingPowerplant
    IAgAvtrSiteUnknown
    IAgAvtrAircraftTerrainFollowModel
    IAgAvtrPropulsionThrust
    IAgAvtrBasicManeuverAirspeedOptions
    IAgAvtrBasicManeuverStrategyAileronRoll
    IAgAvtrBasicManeuverStrategyAutopilotNav
    IAgAvtrBasicManeuverStrategyAutopilotProf
    IAgAvtrBasicManeuverStrategyBarrelRoll
    IAgAvtrBasicManeuverStrategyLoop
    IAgAvtrBasicManeuverStrategyLTAHover
    IAgAvtrBasicManeuverStrategyFlyAOA
    IAgAvtrBasicManeuverStrategyPull
    IAgAvtrBasicManeuverStrategyRollingPull
    IAgAvtrBasicManeuverStrategySmoothAccel
    IAgAvtrBasicManeuverStrategySmoothTurn
    IAgAvtrBasicManeuverStrategySimpleTurn
    IAgAvtrBasicManeuverStrategyIntercept
    IAgAvtrBasicManeuverStrategyRelativeBearing
    IAgAvtrBasicManeuverStrategyRelativeCourse
    IAgAvtrBasicManeuverStrategyRendezvous
    IAgAvtrBasicManeuverStrategyStationkeeping
    IAgAvtrBasicManeuverStrategyRelativeFPA
    IAgAvtrBasicManeuverStrategyRelSpeedAlt
    IAgAvtrBasicManeuverStrategyBezier
    IAgAvtrBasicManeuverStrategyPushPull
    IAgAvtrBasicManeuverStrategyGlideProfile
    IAgAvtrBasicManeuverStrategyCruiseProfile
    IAgAvtrBasicManeuverStrategyStraightAhead
    IAgAvtrBasicManeuverStrategyWeave
    IAgAvtrBasicManeuverStrategyBallistic3D
    IAgAvtrBasicManeuverStrategyPitch3D
    IAgAvtrTakeoffNormal
    IAgAvtrTakeoffDeparturePoint
    IAgAvtrTakeoffLowTransition
    IAgAvtrRefStateForwardFlightOptions
    IAgAvtrRefStateHoverOptions
    IAgAvtrRefStateWeightOnWheelsOptions
    IAgAvtrRefStateTakeoffLandingOptions
    IAgAvtrLandingEnterDownwindPattern
    IAgAvtrLandingInterceptGlideslope
    IAgAvtrLandingStandardInstrumentApproach
    IAgAvtrProcedureBasicManeuver
    IAgAvtrSiteWaypoint
    IAgAvtrSiteEndOfPrevProcedure
    IAgAvtrSiteVTOLPoint
    IAgAvtrSiteSTKVehicle
    IAgAvtrSiteReferenceState
    IAgAvtrSiteSuperProcedure
    IAgAvtrSiteRelToPrevProcedure
    IAgAvtrSiteSTKObjectWaypoint
    IAgAvtrSiteSTKStaticObject
    IAgAvtrSiteRelToSTKObject
    IAgAvtrSiteSTKAreaTarget
    IAgAvtrSiteRunway
    IAgAvtrProcedureLanding
    IAgAvtrProcedureEnroute
    IAgAvtrProcedureBasicPointToPoint
    IAgAvtrProcedureDelay
    IAgAvtrProcedureTakeoff
    IAgAvtrProcedureArcEnroute
    IAgAvtrProcedureArcPointToPoint
    IAgAvtrProcedureFlightLine
    IAgAvtrProcedureHoldingCircular
    IAgAvtrProcedureHoldingFigure8
    IAgAvtrProcedureHoldingRacetrack
    IAgAvtrProcedureTransitionToHover
    IAgAvtrProcedureTerrainFollow
    IAgAvtrProcedureHover
    IAgAvtrProcedureHoverTranslate
    IAgAvtrProcedureTransitionToForwardFlight
    IAgAvtrProcedureVerticalTakeoff
    IAgAvtrProcedureVerticalLanding
    IAgAvtrProcedureReferenceState
    IAgAvtrProcedureSuperProcedure
    IAgAvtrProcedureLaunch
    IAgAvtrProcedureAirway
    IAgAvtrProcedureAirwayRouter
    IAgAvtrProcedureAreaTargetSearch
    IAgAvtrProcedureFormationRecover
    IAgAvtrProcedureInFormation
    IAgAvtrProcedureParallelFlightLine
    IAgAvtrProcedureVGTPoint
    IAgAvtrSiteRunwayFromCatalog
    IAgAvtrSiteAirportFromCatalog
    IAgAvtrSiteNavaidFromCatalog
    IAgAvtrSiteVTOLPointFromCatalog
    IAgAvtrSiteWaypointFromCatalog
    IAgAvtrProcedureLaunchDynState
    IAgAvtrProcedureLaunchWaypoint
    IAgAvtrSiteDynState


Enumerations
~~~~~~~~~~~~

.. autosummary::

    AgEAvtrErrorCodes
    AgEAvtrClosureValue
    AgEAvtrProcedureType
    AgEAvtrSiteType
    AgEAvtrBasicManeuverStrategy
    AgEAvtrStraightAheadRefFrame
    AgEAvtrAirspeedType
    AgEAvtrAeroPropSimpleMode
    AgEAvtrAeroPropFlightMode
    AgEAvtrPhaseOfFlight
    AgEAvtrCruiseSpeed
    AgEAvtrTakeoffMode
    AgEAvtrApproachMode
    AgEAvtrNavigatorTurnDir
    AgEAvtrBasicManeuverFuelFlowType
    AgEAvtrBasicManeuverAltitudeLimit
    AgEAvtrRunwayHighLowEnd
    AgEAvtrBasicManeuverRefFrame
    AgEAvtrBasicManeuverStrategyNavControlLimit
    AgEAvtrAccelManeuverMode
    AgEAvtrAircraftAeroStrategy
    AgEAvtrAircraftPropStrategy
    AgEAvtrAGLMSL
    AgEAvtrLandingApproachFixRangeMode
    AgEAvtrAccelerationAdvAccelMode
    AgEAvtrAccelManeuverAeroPropMode
    AgEAvtrBasicManeuverStrategyAirspeedPerfLimits
    AgEAvtrTurnMode
    AgEAvtrPointToPointMode
    AgEAvtrAltitudeConstraintManeuverMode
    AgEAvtrWindModelType
    AgEAvtrWindAtmosModelSource
    AgEAvtrADDSMsgInterpType
    AgEAvtrADDSMissingMsgType
    AgEAvtrADDSMsgExtrapType
    AgEAvtrADDSForecastType
    AgEAvtrAtmosphereModel
    AgEAvtrSmoothTurnMode
    AgEAvtrPerfModelOverride
    AgEAvtrBasicManeuverAirspeedMode
    AgEAvtrAileronRollFlightPath
    AgEAvtrRollLeftRight
    AgEAvtrRollUprightInverted
    AgEAvtrAileronRollMode
    AgEAvtrFlyAOALeftRight
    AgEAvtrSmoothAccelLeftRight
    AgEAvtrPullMode
    AgEAvtrRollingPullMode
    AgEAvtrSmoothAccelStopConditions
    AgEAvtrAutopilotHorizPlaneMode
    AgEAvtrAngleMode
    AgEAvtrHoverAltitudeMode
    AgEAvtrHoverHeadingMode
    AgEAvtrAutopilotAltitudeMode
    AgEAvtrAutopilotAltitudeControlMode
    AgEAvtrClosureMode
    AgEAvtrInterceptMode
    AgEAvtrRendezvousStopCondition
    AgEAvtrAccelPerfModelOverride
    AgEAvtrStationkeepingStopCondition
    AgEAvtrTurnDirection
    AgEAvtrProfileControlLimit
    AgEAvtrRelSpeedAltStopCondition
    AgEAvtrRelativeAltitudeMode
    AgEAvtrFlyToFlightPathAngleMode
    AgEAvtrPushPull
    AgEAvtrAccelMode
    AgEAvtrDelayAltMode
    AgEAvtrJoinExitArcMethod
    AgEAvtrFlightLineProcType
    AgEAvtrTransitionToHoverMode
    AgEAvtrVTOLRateMode
    AgEAvtrHoldingProfileMode
    AgEAvtrHoldingDirection
    AgEAvtrHoldRefuelDumpMode
    AgEAvtrHoldingEntryManeuver
    AgEAvtrVTOLTransitionMode
    AgEAvtrVTOLFinalHeadingMode
    AgEAvtrVTOLTranslationMode
    AgEAvtrVTOLTranslationFinalCourseMode
    AgEAvtrHoverMode
    AgEAvtrVTOLHeadingMode
    AgEAvtrVertLandingMode
    AgEAvtrLaunchAttitudeMode
    AgEAvtrFuelFlowType
    AgEAvtrLineOrientation
    AgEAvtrRelAbsBearing
    AgEAvtrBasicFixedWingPropMode
    AgEAvtrClimbSpeedType
    AgEAvtrCruiseMaxPerfSpeedType
    AgEAvtrDescentSpeedType
    AgEAvtrTakeoffLandingSpeedMode
    AgEAvtrDepartureSpeedMode
    AgEAvtrAdvFixedWingAeroStrategy
    AgEAvtrAdvFixedWingGeometry
    AgEAvtrAdvFixedWingPowerplantStrategy
    AgEAvtrMissileAeroStrategy
    AgEAvtrMissilePropStrategy
    AgEAvtrRotorcraftPowerplantType
    AgEAvtrMinimizeSiteProcTimeDiff
    AgEAvtrSTKObjectWaypointOffsetMode
    AgEAvtrSearchPatternCourseMode
    AgEAvtrDelayTurnDir
    AgEAvtrTrajectoryBlendMode
    AgEAvtrRefStatePerfMode
    AgEAvtrRefStateLongitudinalAccelMode
    AgEAvtrRefStateLateralAccelMode
    AgEAvtrRefStateAttitudeMode
    AgEAvtrAndOr
    AgEAvtrJetEngineTechnologyLevel
    AgEAvtrJetEngineIntakeType
    AgEAvtrJetEngineTurbineType
    AgEAvtrJetEngineExhaustNozzleType
    AgEAvtrJetFuelType
    AgEAvtrAFPROPFuelType
    AgEAvtrCEAFuelType
    AgEAvtrTurbineMode
    AgEAvtrRamjetMode
    AgEAvtrScramjetMode
    AgEAvtrNumericalIntegrator
    AgEAvtrBallistic3DControlMode
    AgEAvtrLaunchDynStateCoordFrame
    AgEAvtrLaunchDynStateBearingRef
    AgEAvtrAltitudeRef
    AgEAvtrSmoothTurnFPAMode
    AgEAvtrPitch3DControlMode
    AgEAvtrRefuelDumpMode


Classes
~~~~~~~

.. autosummary::

    AgAvtrSiteWaypoint
    AgAvtrSiteEndOfPrevProcedure
    AgAvtrSiteVTOLPoint
    AgAvtrSiteReferenceState
    AgAvtrSiteSTKVehicle
    AgAvtrSiteSuperProcedure
    AgAvtrSiteRelToPrevProcedure
    AgAvtrSiteSTKObjectWaypoint
    AgAvtrSiteSTKStaticObject
    AgAvtrSiteRelToSTKObject
    AgAvtrSiteSTKAreaTarget
    AgAvtrSiteRunway
    AgAvtrSite
    AgAvtrProcedureLanding
    AgAvtrProcedureEnroute
    AgAvtrProcedureBasicPointToPoint
    AgAvtrProcedureArcEnroute
    AgAvtrProcedureArcPointToPoint
    AgAvtrProcedureFlightLine
    AgAvtrProcedureDelay
    AgAvtrProcedureTakeoff
    AgAvtrProcedureCollection
    AgAvtrPhase
    AgAvtrPhaseCollection
    AgAvtrMission
    AgAvtrPropagator
    AgAvtrProcedureBasicManeuver
    AgAvtrBasicManeuverStrategyWeave
    AgAvtrProcedureTimeOptions
    AgAvtrCalculationOptions
    AgAvtrAircraftCategory
    AgAvtrCatalog
    AgAvtrAircraft
    AgAvtrMissile
    AgAvtrRotorcraft
    AgAvtrRotorcraftAero
    AgAvtrRotorcraftProp
    AgAvtrAircraftAcceleration
    AgAvtrAircraftBasicAccelerationModel
    AgAvtrAircraftClimb
    AgAvtrAircraftCruise
    AgAvtrAircraftDescent
    AgAvtrAircraftLanding
    AgAvtrAircraftTakeoff
    AgAvtrAircraftBasicClimbModel
    AgAvtrAircraftAdvClimbModel
    AgAvtrAircraftBasicCruiseModel
    AgAvtrAircraftAdvCruiseModel
    AgAvtrAircraftBasicDescentModel
    AgAvtrAircraftAdvDescentModel
    AgAvtrAircraftBasicTakeoffModel
    AgAvtrAircraftAdvTakeoffModel
    AgAvtrAircraftBasicLandingModel
    AgAvtrAircraftAdvLandingModel
    AgAvtrAirportCategory
    AgAvtrARINC424Airport
    AgAvtrARINC424Runway
    AgAvtrDAFIFRunway
    AgAvtrDAFIFHelipad
    AgAvtrDAFIFWaypoint
    AgAvtrRunwayCategory
    AgAvtrUserRunwaySource
    AgAvtrUserRunway
    AgAvtrAltitudeMSLOptions
    AgAvtrAltitudeOptions
    AgAvtrArcAltitudeOptions
    AgAvtrArcAltitudeAndDelayOptions
    AgAvtrArcOptions
    AgAvtrAltitudeMSLAndLevelOffOptions
    AgAvtrCruiseAirspeedOptions
    AgAvtrCruiseAirspeedProfile
    AgAvtrCruiseAirspeedAndProfileOptions
    AgAvtrLandingCruiseAirspeedAndProfileOptions
    AgAvtrEnrouteOptions
    AgAvtrEnrouteAndDelayOptions
    AgAvtrLandingEnrouteOptions
    AgAvtrEnrouteTurnDirectionOptions
    AgAvtrNavigationOptions
    AgAvtrVerticalPlaneOptions
    AgAvtrArcVerticalPlaneOptions
    AgAvtrVerticalPlaneAndFlightPathOptions
    AgAvtrLandingVerticalPlaneOptions
    AgAvtrRunwayHeadingOptions
    AgAvtrLandingEnterDownwindPattern
    AgAvtrLandingInterceptGlideslope
    AgAvtrLandingStandardInstrumentApproach
    AgAvtrTakeoffDeparturePoint
    AgAvtrTakeoffLowTransition
    AgAvtrTakeoffNormal
    AgAvtrLevelTurns
    AgAvtrAttitudeTransitions
    AgAvtrClimbAndDescentTransitions
    AgAvtrAeroPropManeuverModeHelper
    AgAvtrAircraftAdvAccelerationModel
    AgAvtrAircraftAccelerationMode
    AgAvtrAircraftSimpleAero
    AgAvtrAircraftExternalAero
    AgAvtrAircraftAero
    AgAvtrAircraftBasicFixedWingAero
    AgAvtrAircraftProp
    AgAvtrAircraftSimpleProp
    AgAvtrAircraftExternalProp
    AgAvtrAircraftBasicFixedWingProp
    AgAvtrARINC424Source
    AgAvtrDAFIFSource
    AgAvtrBasicFixedWingFwdFlightLiftHelper
    AgAvtrBasicManeuverStrategyStraightAhead
    AgAvtrBasicManeuverStrategyCruiseProfile
    AgAvtrBasicManeuverStrategyGlideProfile
    AgAvtrAircraftModels
    AgAvtrMissileModels
    AgAvtrRotorcraftModels
    AgAvtrConfiguration
    AgAvtrFuelTankInternal
    AgAvtrFuelTankExternal
    AgAvtrPayloadStation
    AgAvtrStationCollection
    AgAvtrWindModel
    AgAvtrWindModelConstant
    AgAvtrWindModelADDS
    AgAvtrADDSMessage
    AgAvtrADDSMessageCollection
    AgAvtrProcedure
    AgAvtrAtmosphereModel
    AgAvtrAtmosphereModelBasic
    AgAvtrBasicManeuverStrategySimpleTurn
    AgAvtrBasicManeuverStrategyAileronRoll
    AgAvtrBasicManeuverStrategyFlyAOA
    AgAvtrBasicManeuverStrategyPull
    AgAvtrBasicManeuverStrategyRollingPull
    AgAvtrBasicManeuverStrategySmoothAccel
    AgAvtrBasicManeuverStrategySmoothTurn
    AgAvtrBasicManeuverAirspeedOptions
    AgAvtrPropulsionThrust
    AgAvtrBasicManeuverStrategyAutopilotNav
    AgAvtrBasicManeuverStrategyAutopilotProf
    AgAvtrBasicManeuverStrategyBarrelRoll
    AgAvtrBasicManeuverStrategyLoop
    AgAvtrBasicManeuverStrategyLTAHover
    AgAvtrBasicManeuverStrategyIntercept
    AgAvtrBasicManeuverStrategyRelativeBearing
    AgAvtrBasicManeuverStrategyRelativeCourse
    AgAvtrBasicManeuverStrategyRendezvous
    AgAvtrBasicManeuverStrategyStationkeeping
    AgAvtrBasicManeuverStrategyRelativeFPA
    AgAvtrBasicManeuverStrategyRelSpeedAlt
    AgAvtrBasicManeuverStrategyBezier
    AgAvtrBasicManeuverStrategyPushPull
    AgAvtrProcedureHoldingCircular
    AgAvtrProcedureHoldingFigure8
    AgAvtrProcedureHoldingRacetrack
    AgAvtrProcedureTransitionToHover
    AgAvtrProcedureTerrainFollow
    AgAvtrProcedureHover
    AgAvtrProcedureHoverTranslate
    AgAvtrProcedureTransitionToForwardFlight
    AgAvtrHoverAltitudeOptions
    AgAvtrProcedureVerticalTakeoff
    AgAvtrProcedureVerticalLanding
    AgAvtrProcedureReferenceState
    AgAvtrProcedureSuperProcedure
    AgAvtrProcedureLaunch
    AgAvtrProcedureAirway
    AgAvtrProcedureAirwayRouter
    AgAvtrProcedureAreaTargetSearch
    AgAvtrProcedureFormationRecover
    AgAvtrProcedureInFormation
    AgAvtrProcedureParallelFlightLine
    AgAvtrProcedureVGTPoint
    AgAvtrPerformanceModelOptions
    AgAvtrAdvFixedWingTool
    AgAvtrAdvFixedWingExternalAero
    AgAvtrAdvFixedWingSubsonicAero
    AgAvtrAdvFixedWingSubSuperHypersonicAero
    AgAvtrAdvFixedWingSupersonicAero
    AgAvtrPerformanceModel
    AgAvtrAdvFixedWingGeometryBasic
    AgAvtrAdvFixedWingGeometryVariable
    AgAvtrAdvFixedWingElectricPowerplant
    AgAvtrAdvFixedWingExternalProp
    AgAvtrAdvFixedWingSubSuperHypersonicProp
    AgAvtrAdvFixedWingPistonPowerplant
    AgAvtrAdvFixedWingEmpiricalJetEngine
    AgAvtrAdvFixedWingTurbofanBasicABPowerplant
    AgAvtrAdvFixedWingTurbojetBasicABPowerplant
    AgAvtrAdvFixedWingTurbofanBasicABProp
    AgAvtrAdvFixedWingTurbojetBasicABProp
    AgAvtrAdvFixedWingTurbopropPowerplant
    AgAvtrMissileSimpleAero
    AgAvtrMissileExternalAero
    AgAvtrMissileAdvancedAero
    AgAvtrMissileAero
    AgAvtrMissileProp
    AgAvtrMissileSimpleProp
    AgAvtrMissileExternalProp
    AgAvtrMissileRamjetProp
    AgAvtrMissileRocketProp
    AgAvtrMissileTurbojetProp
    AgAvtrRefStateForwardFlightOptions
    AgAvtrRefStateTakeoffLandingOptions
    AgAvtrRefStateHoverOptions
    AgAvtrRefStateWeightOnWheelsOptions
    AgAvtrSiteRunwayFromCatalog
    AgAvtrSiteAirportFromCatalog
    AgAvtrSiteNavaidFromCatalog
    AgAvtrSiteVTOLPointFromCatalog
    AgAvtrSiteWaypointFromCatalog
    AgAvtrNavaidCategory
    AgAvtrVTOLPointCategory
    AgAvtrWaypointCategory
    AgAvtrARINC424Navaid
    AgAvtrARINC424Helipad
    AgAvtrARINC424Waypoint
    AgAvtrUserVTOLPointSource
    AgAvtrUserVTOLPoint
    AgAvtrUserWaypointSource
    AgAvtrUserWaypoint
    AgAvtrPropulsionEfficiencies
    AgAvtrFuelModelKeroseneAFPROP
    AgAvtrFuelModelKeroseneCEA
    AgAvtrAdvFixedWingRamjetBasic
    AgAvtrAdvFixedWingScramjetBasic
    AgAvtrAircraftVTOLModel
    AgAvtrAircraftVTOL
    AgAvtrAircraftTerrainFollowModel
    AgAvtrAircraftTerrainFollow
    AgAvtrBasicManeuverStrategyBallistic3D
    AgAvtrProcedureLaunchDynState
    AgAvtrProcedureLaunchWaypoint
    AgAvtrSiteDynState
    AgAvtrBasicManeuverStrategyPitch3D
    AgAvtrRefuelDumpProperties
    AgAvtrProcedureFastTimeOptions


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: IAgAvtrSite
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrWindModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrADDSMessage
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrFuelTankInternal
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrFuelTankExternal
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrPayloadStation
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraft
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrLevelTurns
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAttitudeTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrClimbAndDescentTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCatalogItem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftBasicClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftBasicAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRunwayCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategy
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftVTOL
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftBasicFixedWingProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAdvClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftBasicCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAdvCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftBasicDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAdvDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftBasicLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAdvLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftBasicTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAdvTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftVTOLModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrPerformanceModelOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingTool
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingSubsonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingSubSuperHypersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingSubSuperHypersonicProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingSupersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingGeometryBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingGeometryVariable
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingElectricPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingPistonPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingTurbopropPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingEmpiricalJetEngine
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingTurbojetBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingTurbofanBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileAdvancedAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileRamjetProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileRocketProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileTurbojetProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRotorcraft
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRotorcraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRotorcraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrUserRunwaySource
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrUserRunway
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrARINC424Item
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrARINC424Source
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrDAFIFSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrUserVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrUserVTOLPointSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrUserWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrUserWaypointSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrPropulsionEfficiencies
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrFuelModelKeroseneAFPROP
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrFuelModelKeroseneCEA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingRamjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingScramjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRefuelDumpProperties
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureFastTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAtmosphereModelBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAtmosphereModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrADDSMessageCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrWindModelADDS
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrWindModelConstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrStation
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrStationCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrConfiguration
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCatalogSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMissileModels
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRotorcraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicFixedWingLiftHelper
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftBasicFixedWingAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAccelerationMode
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAdvAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAeroPropManeuverModeHelper
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCatalogRunway
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCatalogAirport
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCatalogNavaid
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCatalogVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCatalogWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrARINC424Airport
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrDAFIFItem
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrARINC424Runway
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAirportCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrNavaidCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrVTOLPointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrWaypointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftClimb
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftCruise
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftDescent
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCalculationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrNavigationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAltitudeMSLAndLevelOffOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAltitudeMSLOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrHoverAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrArcAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrArcAltitudeAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrArcOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrVerticalPlaneAndFlightPathOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrArcVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrEnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrEnrouteAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrEnrouteTurnDirectionOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCruiseAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCruiseAirspeedProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrCruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAutomationStrategyFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrConnect
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRunwayHeadingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrPhase
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrPhaseCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrMission
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrPropagator
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrPerformanceModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingGeometry
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingTurbofanBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingTurbojetBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAdvFixedWingPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteUnknown
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrAircraftTerrainFollowModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrPropulsionThrust
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyAileronRoll
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyAutopilotNav
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyAutopilotProf
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyBarrelRoll
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyLoop
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyLTAHover
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyFlyAOA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyPull
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyRollingPull
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategySmoothAccel
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategySmoothTurn
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategySimpleTurn
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyIntercept
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyRelativeBearing
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyRelativeCourse
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyRendezvous
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyStationkeeping
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyRelativeFPA
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyRelSpeedAlt
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyBezier
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyPushPull
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyGlideProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyCruiseProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyStraightAhead
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyWeave
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyBallistic3D
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrBasicManeuverStrategyPitch3D
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrTakeoffNormal
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrTakeoffDeparturePoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrTakeoffLowTransition
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRefStateForwardFlightOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRefStateHoverOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRefStateWeightOnWheelsOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrRefStateTakeoffLandingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrLandingEnterDownwindPattern
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrLandingInterceptGlideslope
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrLandingStandardInstrumentApproach
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureBasicManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteEndOfPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteSTKVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteRelToPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteSTKObjectWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteSTKStaticObject
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteRelToSTKObject
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteSTKAreaTarget
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteRunway
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureBasicPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureDelay
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureArcEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureArcPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureHoldingCircular
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureHoldingFigure8
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureHoldingRacetrack
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureTransitionToHover
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureHover
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureHoverTranslate
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureTransitionToForwardFlight
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureVerticalTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureVerticalLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureAirway
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureAirwayRouter
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureAreaTargetSearch
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureFormationRecover
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureInFormation
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureParallelFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureVGTPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteRunwayFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteAirportFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteNavaidFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteVTOLPointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteWaypointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureLaunchDynState
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrProcedureLaunchWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAgAvtrSiteDynState
    :members:
    :exclude-members: __init__


Enumerations
~~~~~~~~~~~~

.. autoenum:: AgEAvtrErrorCodes
    :members:
.. autoenum:: AgEAvtrClosureValue
    :members:
.. autoenum:: AgEAvtrProcedureType
    :members:
.. autoenum:: AgEAvtrSiteType
    :members:
.. autoenum:: AgEAvtrBasicManeuverStrategy
    :members:
.. autoenum:: AgEAvtrStraightAheadRefFrame
    :members:
.. autoenum:: AgEAvtrAirspeedType
    :members:
.. autoenum:: AgEAvtrAeroPropSimpleMode
    :members:
.. autoenum:: AgEAvtrAeroPropFlightMode
    :members:
.. autoenum:: AgEAvtrPhaseOfFlight
    :members:
.. autoenum:: AgEAvtrCruiseSpeed
    :members:
.. autoenum:: AgEAvtrTakeoffMode
    :members:
.. autoenum:: AgEAvtrApproachMode
    :members:
.. autoenum:: AgEAvtrNavigatorTurnDir
    :members:
.. autoenum:: AgEAvtrBasicManeuverFuelFlowType
    :members:
.. autoenum:: AgEAvtrBasicManeuverAltitudeLimit
    :members:
.. autoenum:: AgEAvtrRunwayHighLowEnd
    :members:
.. autoenum:: AgEAvtrBasicManeuverRefFrame
    :members:
.. autoenum:: AgEAvtrBasicManeuverStrategyNavControlLimit
    :members:
.. autoenum:: AgEAvtrAccelManeuverMode
    :members:
.. autoenum:: AgEAvtrAircraftAeroStrategy
    :members:
.. autoenum:: AgEAvtrAircraftPropStrategy
    :members:
.. autoenum:: AgEAvtrAGLMSL
    :members:
.. autoenum:: AgEAvtrLandingApproachFixRangeMode
    :members:
.. autoenum:: AgEAvtrAccelerationAdvAccelMode
    :members:
.. autoenum:: AgEAvtrAccelManeuverAeroPropMode
    :members:
.. autoenum:: AgEAvtrBasicManeuverStrategyAirspeedPerfLimits
    :members:
.. autoenum:: AgEAvtrTurnMode
    :members:
.. autoenum:: AgEAvtrPointToPointMode
    :members:
.. autoenum:: AgEAvtrAltitudeConstraintManeuverMode
    :members:
.. autoenum:: AgEAvtrWindModelType
    :members:
.. autoenum:: AgEAvtrWindAtmosModelSource
    :members:
.. autoenum:: AgEAvtrADDSMsgInterpType
    :members:
.. autoenum:: AgEAvtrADDSMissingMsgType
    :members:
.. autoenum:: AgEAvtrADDSMsgExtrapType
    :members:
.. autoenum:: AgEAvtrADDSForecastType
    :members:
.. autoenum:: AgEAvtrAtmosphereModel
    :members:
.. autoenum:: AgEAvtrSmoothTurnMode
    :members:
.. autoenum:: AgEAvtrPerfModelOverride
    :members:
.. autoenum:: AgEAvtrBasicManeuverAirspeedMode
    :members:
.. autoenum:: AgEAvtrAileronRollFlightPath
    :members:
.. autoenum:: AgEAvtrRollLeftRight
    :members:
.. autoenum:: AgEAvtrRollUprightInverted
    :members:
.. autoenum:: AgEAvtrAileronRollMode
    :members:
.. autoenum:: AgEAvtrFlyAOALeftRight
    :members:
.. autoenum:: AgEAvtrSmoothAccelLeftRight
    :members:
.. autoenum:: AgEAvtrPullMode
    :members:
.. autoenum:: AgEAvtrRollingPullMode
    :members:
.. autoenum:: AgEAvtrSmoothAccelStopConditions
    :members:
.. autoenum:: AgEAvtrAutopilotHorizPlaneMode
    :members:
.. autoenum:: AgEAvtrAngleMode
    :members:
.. autoenum:: AgEAvtrHoverAltitudeMode
    :members:
.. autoenum:: AgEAvtrHoverHeadingMode
    :members:
.. autoenum:: AgEAvtrAutopilotAltitudeMode
    :members:
.. autoenum:: AgEAvtrAutopilotAltitudeControlMode
    :members:
.. autoenum:: AgEAvtrClosureMode
    :members:
.. autoenum:: AgEAvtrInterceptMode
    :members:
.. autoenum:: AgEAvtrRendezvousStopCondition
    :members:
.. autoenum:: AgEAvtrAccelPerfModelOverride
    :members:
.. autoenum:: AgEAvtrStationkeepingStopCondition
    :members:
.. autoenum:: AgEAvtrTurnDirection
    :members:
.. autoenum:: AgEAvtrProfileControlLimit
    :members:
.. autoenum:: AgEAvtrRelSpeedAltStopCondition
    :members:
.. autoenum:: AgEAvtrRelativeAltitudeMode
    :members:
.. autoenum:: AgEAvtrFlyToFlightPathAngleMode
    :members:
.. autoenum:: AgEAvtrPushPull
    :members:
.. autoenum:: AgEAvtrAccelMode
    :members:
.. autoenum:: AgEAvtrDelayAltMode
    :members:
.. autoenum:: AgEAvtrJoinExitArcMethod
    :members:
.. autoenum:: AgEAvtrFlightLineProcType
    :members:
.. autoenum:: AgEAvtrTransitionToHoverMode
    :members:
.. autoenum:: AgEAvtrVTOLRateMode
    :members:
.. autoenum:: AgEAvtrHoldingProfileMode
    :members:
.. autoenum:: AgEAvtrHoldingDirection
    :members:
.. autoenum:: AgEAvtrHoldRefuelDumpMode
    :members:
.. autoenum:: AgEAvtrHoldingEntryManeuver
    :members:
.. autoenum:: AgEAvtrVTOLTransitionMode
    :members:
.. autoenum:: AgEAvtrVTOLFinalHeadingMode
    :members:
.. autoenum:: AgEAvtrVTOLTranslationMode
    :members:
.. autoenum:: AgEAvtrVTOLTranslationFinalCourseMode
    :members:
.. autoenum:: AgEAvtrHoverMode
    :members:
.. autoenum:: AgEAvtrVTOLHeadingMode
    :members:
.. autoenum:: AgEAvtrVertLandingMode
    :members:
.. autoenum:: AgEAvtrLaunchAttitudeMode
    :members:
.. autoenum:: AgEAvtrFuelFlowType
    :members:
.. autoenum:: AgEAvtrLineOrientation
    :members:
.. autoenum:: AgEAvtrRelAbsBearing
    :members:
.. autoenum:: AgEAvtrBasicFixedWingPropMode
    :members:
.. autoenum:: AgEAvtrClimbSpeedType
    :members:
.. autoenum:: AgEAvtrCruiseMaxPerfSpeedType
    :members:
.. autoenum:: AgEAvtrDescentSpeedType
    :members:
.. autoenum:: AgEAvtrTakeoffLandingSpeedMode
    :members:
.. autoenum:: AgEAvtrDepartureSpeedMode
    :members:
.. autoenum:: AgEAvtrAdvFixedWingAeroStrategy
    :members:
.. autoenum:: AgEAvtrAdvFixedWingGeometry
    :members:
.. autoenum:: AgEAvtrAdvFixedWingPowerplantStrategy
    :members:
.. autoenum:: AgEAvtrMissileAeroStrategy
    :members:
.. autoenum:: AgEAvtrMissilePropStrategy
    :members:
.. autoenum:: AgEAvtrRotorcraftPowerplantType
    :members:
.. autoenum:: AgEAvtrMinimizeSiteProcTimeDiff
    :members:
.. autoenum:: AgEAvtrSTKObjectWaypointOffsetMode
    :members:
.. autoenum:: AgEAvtrSearchPatternCourseMode
    :members:
.. autoenum:: AgEAvtrDelayTurnDir
    :members:
.. autoenum:: AgEAvtrTrajectoryBlendMode
    :members:
.. autoenum:: AgEAvtrRefStatePerfMode
    :members:
.. autoenum:: AgEAvtrRefStateLongitudinalAccelMode
    :members:
.. autoenum:: AgEAvtrRefStateLateralAccelMode
    :members:
.. autoenum:: AgEAvtrRefStateAttitudeMode
    :members:
.. autoenum:: AgEAvtrAndOr
    :members:
.. autoenum:: AgEAvtrJetEngineTechnologyLevel
    :members:
.. autoenum:: AgEAvtrJetEngineIntakeType
    :members:
.. autoenum:: AgEAvtrJetEngineTurbineType
    :members:
.. autoenum:: AgEAvtrJetEngineExhaustNozzleType
    :members:
.. autoenum:: AgEAvtrJetFuelType
    :members:
.. autoenum:: AgEAvtrAFPROPFuelType
    :members:
.. autoenum:: AgEAvtrCEAFuelType
    :members:
.. autoenum:: AgEAvtrTurbineMode
    :members:
.. autoenum:: AgEAvtrRamjetMode
    :members:
.. autoenum:: AgEAvtrScramjetMode
    :members:
.. autoenum:: AgEAvtrNumericalIntegrator
    :members:
.. autoenum:: AgEAvtrBallistic3DControlMode
    :members:
.. autoenum:: AgEAvtrLaunchDynStateCoordFrame
    :members:
.. autoenum:: AgEAvtrLaunchDynStateBearingRef
    :members:
.. autoenum:: AgEAvtrAltitudeRef
    :members:
.. autoenum:: AgEAvtrSmoothTurnFPAMode
    :members:
.. autoenum:: AgEAvtrPitch3DControlMode
    :members:
.. autoenum:: AgEAvtrRefuelDumpMode
    :members:


Classes
~~~~~~~

.. autoclass:: AgAvtrSiteWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteEndOfPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteSTKVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteRelToPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteSTKObjectWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteSTKStaticObject
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteRelToSTKObject
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteSTKAreaTarget
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteRunway
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSite
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureLanding
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureBasicPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureArcEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureArcPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureDelay
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrPhase
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrPhaseCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMission
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrPropagator
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureBasicManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyWeave
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrCalculationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraft
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissile
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRotorcraft
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRotorcraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRotorcraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftBasicAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftClimb
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftCruise
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftDescent
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftLanding
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftBasicClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAdvClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftBasicCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAdvCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftBasicDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAdvDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftBasicTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAdvTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftBasicLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAdvLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAirportCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrARINC424Airport
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrARINC424Runway
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrDAFIFRunway
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrDAFIFHelipad
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrDAFIFWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRunwayCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrUserRunwaySource
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrUserRunway
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAltitudeMSLOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrArcAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrArcAltitudeAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrArcOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAltitudeMSLAndLevelOffOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrCruiseAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrCruiseAirspeedProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrCruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrLandingCruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrEnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrEnrouteAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrLandingEnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrEnrouteTurnDirectionOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrNavigationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrArcVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrVerticalPlaneAndFlightPathOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrLandingVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRunwayHeadingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrLandingEnterDownwindPattern
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrLandingInterceptGlideslope
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrLandingStandardInstrumentApproach
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrTakeoffDeparturePoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrTakeoffLowTransition
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrTakeoffNormal
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrLevelTurns
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAttitudeTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrClimbAndDescentTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAeroPropManeuverModeHelper
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAdvAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAccelerationMode
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftBasicFixedWingAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftBasicFixedWingProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrARINC424Source
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrDAFIFSource
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicFixedWingFwdFlightLiftHelper
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyStraightAhead
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyCruiseProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyGlideProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileModels
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRotorcraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrConfiguration
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrFuelTankInternal
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrFuelTankExternal
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrPayloadStation
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrStationCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrWindModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrWindModelConstant
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrWindModelADDS
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrADDSMessage
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrADDSMessageCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAtmosphereModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAtmosphereModelBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategySimpleTurn
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyAileronRoll
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyFlyAOA
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyPull
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyRollingPull
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategySmoothAccel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategySmoothTurn
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrPropulsionThrust
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyAutopilotNav
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyAutopilotProf
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyBarrelRoll
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyLoop
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyLTAHover
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyIntercept
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyRelativeBearing
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyRelativeCourse
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyRendezvous
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyStationkeeping
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyRelativeFPA
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyRelSpeedAlt
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyBezier
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyPushPull
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureHoldingCircular
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureHoldingFigure8
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureHoldingRacetrack
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureTransitionToHover
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureHover
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureHoverTranslate
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureTransitionToForwardFlight
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrHoverAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureVerticalTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureVerticalLanding
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureAirway
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureAirwayRouter
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureAreaTargetSearch
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureFormationRecover
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureInFormation
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureParallelFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureVGTPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrPerformanceModelOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingTool
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingSubsonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingSubSuperHypersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingSupersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrPerformanceModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingGeometryBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingGeometryVariable
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingElectricPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingSubSuperHypersonicProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingPistonPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingEmpiricalJetEngine
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingTurbofanBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingTurbojetBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingTurbofanBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingTurbojetBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingTurbopropPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileAdvancedAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileAero
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileRamjetProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileRocketProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrMissileTurbojetProp
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRefStateForwardFlightOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRefStateTakeoffLandingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRefStateHoverOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRefStateWeightOnWheelsOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteRunwayFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteAirportFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteNavaidFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteVTOLPointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteWaypointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrNavaidCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrVTOLPointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrWaypointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrARINC424Navaid
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrARINC424Helipad
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrARINC424Waypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrUserVTOLPointSource
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrUserVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrUserWaypointSource
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrUserWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrPropulsionEfficiencies
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrFuelModelKeroseneAFPROP
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrFuelModelKeroseneCEA
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingRamjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAdvFixedWingScramjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftVTOLModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftVTOL
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftTerrainFollowModel
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrAircraftTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyBallistic3D
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureLaunchDynState
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureLaunchWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrSiteDynState
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrBasicManeuverStrategyPitch3D
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrRefuelDumpProperties
    :members:
    :exclude-members: __init__
.. autoclass:: AgAvtrProcedureFastTimeOptions
    :members:
    :exclude-members: __init__

