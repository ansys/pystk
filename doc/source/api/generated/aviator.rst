Module contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    IAvtrSite
    IAvtrWindModel
    IAvtrADDSMessage
    IAvtrFuelTankInternal
    IAvtrFuelTankExternal
    IAvtrPayloadStation
    IAvtrAircraft
    IAvtrAircraftSimpleAero
    IAvtrLevelTurns
    IAvtrAttitudeTransitions
    IAvtrClimbAndDescentTransitions
    IAvtrCatalogItem
    IAvtrAircraftBasicClimbModel
    IAvtrAircraftBasicAccelerationModel
    IAvtrAircraftCategory
    IAvtrRunwayCategory
    IAvtrBasicManeuverStrategy
    IAvtrAircraftVTOL
    IAvtrAircraftExternalAero
    IAvtrAircraftSimpleProp
    IAvtrAircraftExternalProp
    IAvtrAircraftBasicFixedWingProp
    IAvtrAircraftAdvClimbModel
    IAvtrAircraftBasicCruiseModel
    IAvtrAircraftAdvCruiseModel
    IAvtrAircraftBasicDescentModel
    IAvtrAircraftAdvDescentModel
    IAvtrAircraftBasicLandingModel
    IAvtrAircraftAdvLandingModel
    IAvtrAircraftBasicTakeoffModel
    IAvtrAircraftAdvTakeoffModel
    IAvtrAircraftVTOLModel
    IAvtrAircraftTerrainFollow
    IAvtrPerformanceModelOptions
    IAvtrAdvFixedWingTool
    IAvtrAdvFixedWingExternalAero
    IAvtrAdvFixedWingSubsonicAero
    IAvtrAdvFixedWingSubSuperHypersonicAero
    IAvtrAdvFixedWingSubSuperHypersonicProp
    IAvtrAdvFixedWingSupersonicAero
    IAvtrAdvFixedWingGeometryBasic
    IAvtrAdvFixedWingGeometryVariable
    IAvtrAdvFixedWingElectricPowerplant
    IAvtrAdvFixedWingExternalProp
    IAvtrAdvFixedWingPistonPowerplant
    IAvtrAdvFixedWingTurbopropPowerplant
    IAvtrAdvFixedWingEmpiricalJetEngine
    IAvtrAdvFixedWingTurbojetBasicABProp
    IAvtrAdvFixedWingTurbofanBasicABProp
    IAvtrVehicle
    IAvtrMissile
    IAvtrMissileAero
    IAvtrMissileProp
    IAvtrMissileSimpleAero
    IAvtrMissileSimpleProp
    IAvtrMissileExternalAero
    IAvtrMissileExternalProp
    IAvtrMissileAdvancedAero
    IAvtrMissileRamjetProp
    IAvtrMissileRocketProp
    IAvtrMissileTurbojetProp
    IAvtrRotorcraft
    IAvtrRotorcraftAero
    IAvtrRotorcraftProp
    IAvtrUserRunwaySource
    IAvtrUserRunway
    IAvtrARINC424Item
    IAvtrARINC424Source
    IAvtrDAFIFSource
    IAvtrUserVTOLPoint
    IAvtrUserVTOLPointSource
    IAvtrUserWaypoint
    IAvtrUserWaypointSource
    IAvtrPropulsionEfficiencies
    IAvtrFuelModelKeroseneAFPROP
    IAvtrFuelModelKeroseneCEA
    IAvtrAdvFixedWingRamjetBasic
    IAvtrAdvFixedWingScramjetBasic
    IAvtrRefuelDumpProperties
    IAvtrProcedureFastTimeOptions
    IAvtrAtmosphereModelBasic
    IAvtrAtmosphereModel
    IAvtrADDSMessageCollection
    IAvtrWindModelADDS
    IAvtrWindModelConstant
    IAvtrStation
    IAvtrStationCollection
    IAvtrConfiguration
    IAvtrCatalogSource
    IAvtrAircraftModels
    IAvtrMissileModels
    IAvtrRotorcraftModels
    IAvtrBasicFixedWingLiftHelper
    IAvtrAircraftBasicFixedWingAero
    IAvtrAircraftAero
    IAvtrAircraftProp
    IAvtrAircraftAccelerationMode
    IAvtrAircraftAdvAccelerationModel
    IAvtrAeroPropManeuverModeHelper
    IAvtrCatalogRunway
    IAvtrCatalogAirport
    IAvtrCatalogNavaid
    IAvtrCatalogVTOLPoint
    IAvtrCatalogWaypoint
    IAvtrARINC424Airport
    IAvtrDAFIFItem
    IAvtrARINC424Runway
    IAvtrAirportCategory
    IAvtrNavaidCategory
    IAvtrVTOLPointCategory
    IAvtrWaypointCategory
    IAvtrAircraftClimb
    IAvtrAircraftCruise
    IAvtrAircraftDescent
    IAvtrAircraftLanding
    IAvtrAircraftTakeoff
    IAvtrAircraftAcceleration
    IAvtrCatalog
    IAvtrProcedureTimeOptions
    IAvtrCalculationOptions
    IAvtrNavigationOptions
    IAvtrAltitudeMSLAndLevelOffOptions
    IAvtrAltitudeMSLOptions
    IAvtrAltitudeOptions
    IAvtrHoverAltitudeOptions
    IAvtrArcAltitudeOptions
    IAvtrArcAltitudeAndDelayOptions
    IAvtrArcOptions
    IAvtrVerticalPlaneOptions
    IAvtrVerticalPlaneAndFlightPathOptions
    IAvtrArcVerticalPlaneOptions
    IAvtrEnrouteOptions
    IAvtrEnrouteAndDelayOptions
    IAvtrEnrouteTurnDirectionOptions
    IAvtrCruiseAirspeedOptions
    IAvtrCruiseAirspeedProfile
    IAvtrCruiseAirspeedAndProfileOptions
    IAvtrAutomationStrategyFactory
    IAvtrConnect
    IAvtrRunwayHeadingOptions
    IAvtrProcedure
    IAvtrProcedureCollection
    IAvtrPhase
    IAvtrPhaseCollection
    IAvtrMission
    IAvtrPropagator
    IAvtrPerformanceModel
    IAvtrAdvFixedWingGeometry
    IAvtrAdvFixedWingTurbofanBasicABPowerplant
    IAvtrAdvFixedWingTurbojetBasicABPowerplant
    IAvtrAdvFixedWingPowerplant
    IAvtrSiteUnknown
    IAvtrAircraftTerrainFollowModel
    IAvtrPropulsionThrust
    IAvtrBasicManeuverAirspeedOptions
    IAvtrBasicManeuverStrategyAileronRoll
    IAvtrBasicManeuverStrategyAutopilotNav
    IAvtrBasicManeuverStrategyAutopilotProf
    IAvtrBasicManeuverStrategyBarrelRoll
    IAvtrBasicManeuverStrategyLoop
    IAvtrBasicManeuverStrategyLTAHover
    IAvtrBasicManeuverStrategyFlyAOA
    IAvtrBasicManeuverStrategyPull
    IAvtrBasicManeuverStrategyRollingPull
    IAvtrBasicManeuverStrategySmoothAccel
    IAvtrBasicManeuverStrategySmoothTurn
    IAvtrBasicManeuverStrategySimpleTurn
    IAvtrBasicManeuverStrategyIntercept
    IAvtrBasicManeuverStrategyRelativeBearing
    IAvtrBasicManeuverStrategyRelativeCourse
    IAvtrBasicManeuverStrategyRendezvous
    IAvtrBasicManeuverStrategyStationkeeping
    IAvtrBasicManeuverStrategyRelativeFPA
    IAvtrBasicManeuverStrategyRelSpeedAlt
    IAvtrBasicManeuverStrategyBezier
    IAvtrBasicManeuverStrategyPushPull
    IAvtrBasicManeuverStrategyGlideProfile
    IAvtrBasicManeuverStrategyCruiseProfile
    IAvtrBasicManeuverStrategyStraightAhead
    IAvtrBasicManeuverStrategyWeave
    IAvtrBasicManeuverStrategyBallistic3D
    IAvtrBasicManeuverStrategyPitch3D
    IAvtrTakeoffNormal
    IAvtrTakeoffDeparturePoint
    IAvtrTakeoffLowTransition
    IAvtrRefStateForwardFlightOptions
    IAvtrRefStateHoverOptions
    IAvtrRefStateWeightOnWheelsOptions
    IAvtrRefStateTakeoffLandingOptions
    IAvtrLandingEnterDownwindPattern
    IAvtrLandingInterceptGlideslope
    IAvtrLandingStandardInstrumentApproach
    IAvtrProcedureBasicManeuver
    IAvtrSiteWaypoint
    IAvtrSiteEndOfPrevProcedure
    IAvtrSiteVTOLPoint
    IAvtrSiteSTKVehicle
    IAvtrSiteReferenceState
    IAvtrSiteSuperProcedure
    IAvtrSiteRelToPrevProcedure
    IAvtrSiteSTKObjectWaypoint
    IAvtrSiteSTKStaticObject
    IAvtrSiteRelToSTKObject
    IAvtrSiteSTKAreaTarget
    IAvtrSiteRunway
    IAvtrProcedureLanding
    IAvtrProcedureEnroute
    IAvtrProcedureBasicPointToPoint
    IAvtrProcedureDelay
    IAvtrProcedureTakeoff
    IAvtrProcedureArcEnroute
    IAvtrProcedureArcPointToPoint
    IAvtrProcedureFlightLine
    IAvtrProcedureHoldingCircular
    IAvtrProcedureHoldingFigure8
    IAvtrProcedureHoldingRacetrack
    IAvtrProcedureTransitionToHover
    IAvtrProcedureTerrainFollow
    IAvtrProcedureHover
    IAvtrProcedureHoverTranslate
    IAvtrProcedureTransitionToForwardFlight
    IAvtrProcedureVerticalTakeoff
    IAvtrProcedureVerticalLanding
    IAvtrProcedureReferenceState
    IAvtrProcedureSuperProcedure
    IAvtrProcedureLaunch
    IAvtrProcedureAirway
    IAvtrProcedureAirwayRouter
    IAvtrProcedureAreaTargetSearch
    IAvtrProcedureFormationRecover
    IAvtrProcedureInFormation
    IAvtrProcedureParallelFlightLine
    IAvtrProcedureVGTPoint
    IAvtrSiteRunwayFromCatalog
    IAvtrSiteAirportFromCatalog
    IAvtrSiteNavaidFromCatalog
    IAvtrSiteVTOLPointFromCatalog
    IAvtrSiteWaypointFromCatalog
    IAvtrProcedureLaunchDynState
    IAvtrProcedureLaunchWaypoint
    IAvtrSiteDynState


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

    AvtrSiteWaypoint
    AvtrSiteEndOfPrevProcedure
    AvtrSiteVTOLPoint
    AvtrSiteReferenceState
    AvtrSiteSTKVehicle
    AvtrSiteSuperProcedure
    AvtrSiteRelToPrevProcedure
    AvtrSiteSTKObjectWaypoint
    AvtrSiteSTKStaticObject
    AvtrSiteRelToSTKObject
    AvtrSiteSTKAreaTarget
    AvtrSiteRunway
    AvtrSite
    AvtrProcedureLanding
    AvtrProcedureEnroute
    AvtrProcedureBasicPointToPoint
    AvtrProcedureArcEnroute
    AvtrProcedureArcPointToPoint
    AvtrProcedureFlightLine
    AvtrProcedureDelay
    AvtrProcedureTakeoff
    AvtrProcedureCollection
    AvtrPhase
    AvtrPhaseCollection
    AvtrMission
    AvtrPropagator
    AvtrProcedureBasicManeuver
    AvtrBasicManeuverStrategyWeave
    AvtrProcedureTimeOptions
    AvtrCalculationOptions
    AvtrAircraftCategory
    AvtrCatalog
    AvtrAircraft
    AvtrMissile
    AvtrRotorcraft
    AvtrRotorcraftAero
    AvtrRotorcraftProp
    AvtrAircraftAcceleration
    AvtrAircraftBasicAccelerationModel
    AvtrAircraftClimb
    AvtrAircraftCruise
    AvtrAircraftDescent
    AvtrAircraftLanding
    AvtrAircraftTakeoff
    AvtrAircraftBasicClimbModel
    AvtrAircraftAdvClimbModel
    AvtrAircraftBasicCruiseModel
    AvtrAircraftAdvCruiseModel
    AvtrAircraftBasicDescentModel
    AvtrAircraftAdvDescentModel
    AvtrAircraftBasicTakeoffModel
    AvtrAircraftAdvTakeoffModel
    AvtrAircraftBasicLandingModel
    AvtrAircraftAdvLandingModel
    AvtrAirportCategory
    AvtrARINC424Airport
    AvtrARINC424Runway
    AvtrDAFIFRunway
    AvtrDAFIFHelipad
    AvtrDAFIFWaypoint
    AvtrRunwayCategory
    AvtrUserRunwaySource
    AvtrUserRunway
    AvtrAltitudeMSLOptions
    AvtrAltitudeOptions
    AvtrArcAltitudeOptions
    AvtrArcAltitudeAndDelayOptions
    AvtrArcOptions
    AvtrAltitudeMSLAndLevelOffOptions
    AvtrCruiseAirspeedOptions
    AvtrCruiseAirspeedProfile
    AvtrCruiseAirspeedAndProfileOptions
    AvtrLandingCruiseAirspeedAndProfileOptions
    AvtrEnrouteOptions
    AvtrEnrouteAndDelayOptions
    AvtrLandingEnrouteOptions
    AvtrEnrouteTurnDirectionOptions
    AvtrNavigationOptions
    AvtrVerticalPlaneOptions
    AvtrArcVerticalPlaneOptions
    AvtrVerticalPlaneAndFlightPathOptions
    AvtrLandingVerticalPlaneOptions
    AvtrRunwayHeadingOptions
    AvtrLandingEnterDownwindPattern
    AvtrLandingInterceptGlideslope
    AvtrLandingStandardInstrumentApproach
    AvtrTakeoffDeparturePoint
    AvtrTakeoffLowTransition
    AvtrTakeoffNormal
    AvtrLevelTurns
    AvtrAttitudeTransitions
    AvtrClimbAndDescentTransitions
    AvtrAeroPropManeuverModeHelper
    AvtrAircraftAdvAccelerationModel
    AvtrAircraftAccelerationMode
    AvtrAircraftSimpleAero
    AvtrAircraftExternalAero
    AvtrAircraftAero
    AvtrAircraftBasicFixedWingAero
    AvtrAircraftProp
    AvtrAircraftSimpleProp
    AvtrAircraftExternalProp
    AvtrAircraftBasicFixedWingProp
    AvtrARINC424Source
    AvtrDAFIFSource
    AvtrBasicFixedWingFwdFlightLiftHelper
    AvtrBasicManeuverStrategyStraightAhead
    AvtrBasicManeuverStrategyCruiseProfile
    AvtrBasicManeuverStrategyGlideProfile
    AvtrAircraftModels
    AvtrMissileModels
    AvtrRotorcraftModels
    AvtrConfiguration
    AvtrFuelTankInternal
    AvtrFuelTankExternal
    AvtrPayloadStation
    AvtrStationCollection
    AvtrWindModel
    AvtrWindModelConstant
    AvtrWindModelADDS
    AvtrADDSMessage
    AvtrADDSMessageCollection
    AvtrProcedure
    AvtrAtmosphereModel
    AvtrAtmosphereModelBasic
    AvtrBasicManeuverStrategySimpleTurn
    AvtrBasicManeuverStrategyAileronRoll
    AvtrBasicManeuverStrategyFlyAOA
    AvtrBasicManeuverStrategyPull
    AvtrBasicManeuverStrategyRollingPull
    AvtrBasicManeuverStrategySmoothAccel
    AvtrBasicManeuverStrategySmoothTurn
    AvtrBasicManeuverAirspeedOptions
    AvtrPropulsionThrust
    AvtrBasicManeuverStrategyAutopilotNav
    AvtrBasicManeuverStrategyAutopilotProf
    AvtrBasicManeuverStrategyBarrelRoll
    AvtrBasicManeuverStrategyLoop
    AvtrBasicManeuverStrategyLTAHover
    AvtrBasicManeuverStrategyIntercept
    AvtrBasicManeuverStrategyRelativeBearing
    AvtrBasicManeuverStrategyRelativeCourse
    AvtrBasicManeuverStrategyRendezvous
    AvtrBasicManeuverStrategyStationkeeping
    AvtrBasicManeuverStrategyRelativeFPA
    AvtrBasicManeuverStrategyRelSpeedAlt
    AvtrBasicManeuverStrategyBezier
    AvtrBasicManeuverStrategyPushPull
    AvtrProcedureHoldingCircular
    AvtrProcedureHoldingFigure8
    AvtrProcedureHoldingRacetrack
    AvtrProcedureTransitionToHover
    AvtrProcedureTerrainFollow
    AvtrProcedureHover
    AvtrProcedureHoverTranslate
    AvtrProcedureTransitionToForwardFlight
    AvtrHoverAltitudeOptions
    AvtrProcedureVerticalTakeoff
    AvtrProcedureVerticalLanding
    AvtrProcedureReferenceState
    AvtrProcedureSuperProcedure
    AvtrProcedureLaunch
    AvtrProcedureAirway
    AvtrProcedureAirwayRouter
    AvtrProcedureAreaTargetSearch
    AvtrProcedureFormationRecover
    AvtrProcedureInFormation
    AvtrProcedureParallelFlightLine
    AvtrProcedureVGTPoint
    AvtrPerformanceModelOptions
    AvtrAdvFixedWingTool
    AvtrAdvFixedWingExternalAero
    AvtrAdvFixedWingSubsonicAero
    AvtrAdvFixedWingSubSuperHypersonicAero
    AvtrAdvFixedWingSupersonicAero
    AvtrPerformanceModel
    AvtrAdvFixedWingGeometryBasic
    AvtrAdvFixedWingGeometryVariable
    AvtrAdvFixedWingElectricPowerplant
    AvtrAdvFixedWingExternalProp
    AvtrAdvFixedWingSubSuperHypersonicProp
    AvtrAdvFixedWingPistonPowerplant
    AvtrAdvFixedWingEmpiricalJetEngine
    AvtrAdvFixedWingTurbofanBasicABPowerplant
    AvtrAdvFixedWingTurbojetBasicABPowerplant
    AvtrAdvFixedWingTurbofanBasicABProp
    AvtrAdvFixedWingTurbojetBasicABProp
    AvtrAdvFixedWingTurbopropPowerplant
    AvtrMissileSimpleAero
    AvtrMissileExternalAero
    AvtrMissileAdvancedAero
    AvtrMissileAero
    AvtrMissileProp
    AvtrMissileSimpleProp
    AvtrMissileExternalProp
    AvtrMissileRamjetProp
    AvtrMissileRocketProp
    AvtrMissileTurbojetProp
    AvtrRefStateForwardFlightOptions
    AvtrRefStateTakeoffLandingOptions
    AvtrRefStateHoverOptions
    AvtrRefStateWeightOnWheelsOptions
    AvtrSiteRunwayFromCatalog
    AvtrSiteAirportFromCatalog
    AvtrSiteNavaidFromCatalog
    AvtrSiteVTOLPointFromCatalog
    AvtrSiteWaypointFromCatalog
    AvtrNavaidCategory
    AvtrVTOLPointCategory
    AvtrWaypointCategory
    AvtrARINC424Navaid
    AvtrARINC424Helipad
    AvtrARINC424Waypoint
    AvtrUserVTOLPointSource
    AvtrUserVTOLPoint
    AvtrUserWaypointSource
    AvtrUserWaypoint
    AvtrPropulsionEfficiencies
    AvtrFuelModelKeroseneAFPROP
    AvtrFuelModelKeroseneCEA
    AvtrAdvFixedWingRamjetBasic
    AvtrAdvFixedWingScramjetBasic
    AvtrAircraftVTOLModel
    AvtrAircraftVTOL
    AvtrAircraftTerrainFollowModel
    AvtrAircraftTerrainFollow
    AvtrBasicManeuverStrategyBallistic3D
    AvtrProcedureLaunchDynState
    AvtrProcedureLaunchWaypoint
    AvtrSiteDynState
    AvtrBasicManeuverStrategyPitch3D
    AvtrRefuelDumpProperties
    AvtrProcedureFastTimeOptions


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: IAvtrSite
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrWindModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrADDSMessage
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrFuelTankInternal
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrFuelTankExternal
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrPayloadStation
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraft
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrLevelTurns
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAttitudeTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrClimbAndDescentTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCatalogItem
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftBasicClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftBasicAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRunwayCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategy
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftVTOL
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftBasicFixedWingProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAdvClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftBasicCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAdvCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftBasicDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAdvDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftBasicLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAdvLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftBasicTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAdvTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftVTOLModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrPerformanceModelOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingTool
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingSubsonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingSubSuperHypersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingSubSuperHypersonicProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingSupersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingGeometryBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingGeometryVariable
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingElectricPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingPistonPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingTurbopropPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingEmpiricalJetEngine
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingTurbojetBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingTurbofanBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissile
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileAdvancedAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileRamjetProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileRocketProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileTurbojetProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRotorcraft
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRotorcraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRotorcraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrUserRunwaySource
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrUserRunway
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrARINC424Item
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrARINC424Source
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrDAFIFSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrUserVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrUserVTOLPointSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrUserWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrUserWaypointSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrPropulsionEfficiencies
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrFuelModelKeroseneAFPROP
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrFuelModelKeroseneCEA
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingRamjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingScramjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRefuelDumpProperties
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureFastTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAtmosphereModelBasic
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAtmosphereModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrADDSMessageCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrWindModelADDS
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrWindModelConstant
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrStation
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrStationCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrConfiguration
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCatalogSource
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMissileModels
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRotorcraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicFixedWingLiftHelper
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftBasicFixedWingAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAccelerationMode
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAdvAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAeroPropManeuverModeHelper
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCatalogRunway
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCatalogAirport
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCatalogNavaid
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCatalogVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCatalogWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrARINC424Airport
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrDAFIFItem
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrARINC424Runway
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAirportCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrNavaidCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrVTOLPointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrWaypointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftClimb
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftCruise
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftDescent
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCalculationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrNavigationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAltitudeMSLAndLevelOffOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAltitudeMSLOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrHoverAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrArcAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrArcAltitudeAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrArcOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrVerticalPlaneAndFlightPathOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrArcVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrEnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrEnrouteAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrEnrouteTurnDirectionOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCruiseAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCruiseAirspeedProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrCruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAutomationStrategyFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrConnect
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRunwayHeadingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrPhase
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrPhaseCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrMission
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrPropagator
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrPerformanceModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingGeometry
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingTurbofanBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingTurbojetBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAdvFixedWingPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteUnknown
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrAircraftTerrainFollowModel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrPropulsionThrust
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyAileronRoll
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyAutopilotNav
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyAutopilotProf
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyBarrelRoll
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyLoop
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyLTAHover
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyFlyAOA
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyPull
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyRollingPull
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategySmoothAccel
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategySmoothTurn
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategySimpleTurn
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyIntercept
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyRelativeBearing
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyRelativeCourse
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyRendezvous
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyStationkeeping
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyRelativeFPA
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyRelSpeedAlt
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyBezier
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyPushPull
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyGlideProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyCruiseProfile
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyStraightAhead
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyWeave
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyBallistic3D
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrBasicManeuverStrategyPitch3D
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrTakeoffNormal
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrTakeoffDeparturePoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrTakeoffLowTransition
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRefStateForwardFlightOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRefStateHoverOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRefStateWeightOnWheelsOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrRefStateTakeoffLandingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrLandingEnterDownwindPattern
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrLandingInterceptGlideslope
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrLandingStandardInstrumentApproach
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureBasicManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteEndOfPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteSTKVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteRelToPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteSTKObjectWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteSTKStaticObject
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteRelToSTKObject
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteSTKAreaTarget
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteRunway
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureBasicPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureDelay
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureArcEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureArcPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureHoldingCircular
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureHoldingFigure8
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureHoldingRacetrack
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureTransitionToHover
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureHover
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureHoverTranslate
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureTransitionToForwardFlight
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureVerticalTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureVerticalLanding
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureAirway
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureAirwayRouter
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureAreaTargetSearch
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureFormationRecover
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureInFormation
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureParallelFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureVGTPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteRunwayFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteAirportFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteNavaidFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteVTOLPointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteWaypointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureLaunchDynState
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrProcedureLaunchWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: IAvtrSiteDynState
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

.. autoclass:: AvtrSiteWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteEndOfPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteSTKVehicle
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteRelToPrevProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteSTKObjectWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteSTKStaticObject
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteRelToSTKObject
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteSTKAreaTarget
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteRunway
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSite
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureLanding
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureBasicPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureArcEnroute
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureArcPointToPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureDelay
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrPhase
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrPhaseCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMission
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrPropagator
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureBasicManeuver
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyWeave
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureTimeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrCalculationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraft
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissile
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRotorcraft
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRotorcraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRotorcraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAcceleration
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftBasicAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftClimb
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftCruise
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftDescent
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftLanding
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftBasicClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAdvClimbModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftBasicCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAdvCruiseModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftBasicDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAdvDescentModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftBasicTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAdvTakeoffModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftBasicLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAdvLandingModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAirportCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrARINC424Airport
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrARINC424Runway
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrDAFIFRunway
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrDAFIFHelipad
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrDAFIFWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRunwayCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrUserRunwaySource
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrUserRunway
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAltitudeMSLOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrArcAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrArcAltitudeAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrArcOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAltitudeMSLAndLevelOffOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrCruiseAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrCruiseAirspeedProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrCruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrLandingCruiseAirspeedAndProfileOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrEnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrEnrouteAndDelayOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrLandingEnrouteOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrEnrouteTurnDirectionOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrNavigationOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrArcVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrVerticalPlaneAndFlightPathOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrLandingVerticalPlaneOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRunwayHeadingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrLandingEnterDownwindPattern
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrLandingInterceptGlideslope
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrLandingStandardInstrumentApproach
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrTakeoffDeparturePoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrTakeoffLowTransition
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrTakeoffNormal
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrLevelTurns
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAttitudeTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrClimbAndDescentTransitions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAeroPropManeuverModeHelper
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAdvAccelerationModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAccelerationMode
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftBasicFixedWingAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftBasicFixedWingProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrARINC424Source
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrDAFIFSource
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicFixedWingFwdFlightLiftHelper
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyStraightAhead
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyCruiseProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyGlideProfile
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileModels
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRotorcraftModels
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrConfiguration
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrFuelTankInternal
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrFuelTankExternal
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrPayloadStation
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrStationCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrWindModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrWindModelConstant
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrWindModelADDS
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrADDSMessage
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrADDSMessageCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAtmosphereModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAtmosphereModelBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategySimpleTurn
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyAileronRoll
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyFlyAOA
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyPull
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyRollingPull
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategySmoothAccel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategySmoothTurn
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverAirspeedOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrPropulsionThrust
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyAutopilotNav
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyAutopilotProf
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyBarrelRoll
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyLoop
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyLTAHover
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyIntercept
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyRelativeBearing
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyRelativeCourse
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyRendezvous
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyStationkeeping
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyRelativeFPA
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyRelSpeedAlt
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyBezier
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyPushPull
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureHoldingCircular
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureHoldingFigure8
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureHoldingRacetrack
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureTransitionToHover
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureHover
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureHoverTranslate
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureTransitionToForwardFlight
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrHoverAltitudeOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureVerticalTakeoff
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureVerticalLanding
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureReferenceState
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureSuperProcedure
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureLaunch
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureAirway
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureAirwayRouter
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureAreaTargetSearch
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureFormationRecover
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureInFormation
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureParallelFlightLine
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureVGTPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrPerformanceModelOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingTool
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingSubsonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingSubSuperHypersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingSupersonicAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrPerformanceModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingGeometryBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingGeometryVariable
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingElectricPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingSubSuperHypersonicProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingPistonPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingEmpiricalJetEngine
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingTurbofanBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingTurbojetBasicABPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingTurbofanBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingTurbojetBasicABProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingTurbopropPowerplant
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileSimpleAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileExternalAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileAdvancedAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileAero
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileSimpleProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileExternalProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileRamjetProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileRocketProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrMissileTurbojetProp
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRefStateForwardFlightOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRefStateTakeoffLandingOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRefStateHoverOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRefStateWeightOnWheelsOptions
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteRunwayFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteAirportFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteNavaidFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteVTOLPointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteWaypointFromCatalog
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrNavaidCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrVTOLPointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrWaypointCategory
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrARINC424Navaid
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrARINC424Helipad
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrARINC424Waypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrUserVTOLPointSource
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrUserVTOLPoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrUserWaypointSource
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrUserWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrPropulsionEfficiencies
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrFuelModelKeroseneAFPROP
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrFuelModelKeroseneCEA
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingRamjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAdvFixedWingScramjetBasic
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftVTOLModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftVTOL
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftTerrainFollowModel
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrAircraftTerrainFollow
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyBallistic3D
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureLaunchDynState
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureLaunchWaypoint
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrSiteDynState
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrBasicManeuverStrategyPitch3D
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrRefuelDumpProperties
    :members:
    :exclude-members: __init__
.. autoclass:: AvtrProcedureFastTimeOptions
    :members:
    :exclude-members: __init__

