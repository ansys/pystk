
The ``aviator`` module
======================


.. py:module:: ansys.stk.core.stkobjects.aviator


Summary
-------

.. tab-set::

    .. tab-item:: Submodules

        .. list-table::
            :header-rows: 0
            :widths: auto
        
            * - :py:mod:`~ansys.stk.core.stkobjects.aviator.matlab`

             
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`
              - Interface to access Site options.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`
              - Interface used to access the options for a Catalog Item in the Aviator Catalog. Use this interface to Create, Remove, Duplicate, or Rename items in the catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`
              - Interface used to access options for a Basic Maneuver Strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IAviatorVehicle`
              - Interface for a vehicle in Aviator.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IARINC424Item`
              - Interface used to access the options for an ARINC424 Item found in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IStation`
              - Interface used to access a station for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogSource`
              - Interface used to access options for a source in the Aviator Catalog. Examples of sources include User Aircraft Models, ARINC424runways, User Runways, etc.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicFixedWingLiftHelper`
              - Interface used to access Lift Coefficient Helper in the Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogRunway`
              - Interface used to access a runway in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogAirport`
              - Interface used to access a airport in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogNavaid`
              - Interface used to access a navaid in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogVTOLPoint`
              - Interface used to access a VTOL Point in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogWaypoint`
              - Interface used to access a waypoint in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IARINC424Airport`
              - Do not use this interface, as it is deprecated. Use IAgAvtrARINC424Item instead.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IDAFIFItem`
              - Interface used to access the options for an DAFIF Item found in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IVerticalPlaneOptions`
              - Interface used to access the Vertical Plane options for an Aviator procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IEnrouteAndDelayOptions`
              - Interface used to access the Enroute options for an Aviator procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions`
              - Interface used to access the cruise airspeed options that also include a profile field.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IAutomationStrategyFactory`
              - Interface used to send connect commands to Aviator objects.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IConnect`
              - Interface used to send connect commands to Aviator objects.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`
              - Interface used to access the options for a procedure. Use this interface to get the Site and Get the time options for the current procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`
              - Interface for a performance model of an Aviator vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingGeometry`
              - Interface used to access the options for the wing geometry in the advanced fixed wing tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPowerplant`
              - Interface for a powerplant strategy in the advanced fixed wing tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ISiteUnknown`
              - Interface of an unknown site.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteWaypoint`
              - Class defining a waypoint site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteEndOfPrevProcedure`
              - Class defining an End of Previous Procedure site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint`
              - Class defining a VTOL Point site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteReferenceState`
              - Class defining a Reference State site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteSTKVehicle`
              - Class defining a STK Vehicle site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteSuperProcedure`
              - Class defining a Super Procedure site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure`
              - Class defining a Relative to Previous Procedure site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint`
              - Class defining a STK Object Waypoint site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteSTKStaticObject`
              - Class defining a STK Static Object site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteRelToSTKObject`
              - Class defining a Relative to Stationary STK Object site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteSTKAreaTarget`
              - Class defining a STK Area Target site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteRunway`
              - Class defining a runway site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.Site`
              - Class defining an unknown site type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureLanding`
              - Class defining a landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureEnroute`
              - Class defining an enroute procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem`
              - Class defining an ExtEphem procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationFlyer`
              - Class defining an formationflyer procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicPointToPoint`
              - Class defining a basic point to point procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureArcEnroute`
              - Class defining a arc enroute procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureArcPointToPoint`
              - Class defining a arc point to point procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureFlightLine`
              - Class defining a flight line procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureDelay`
              - Class defining a delay procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureTakeoff`
              - Class defining a takeoff procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureCollection`
              - Class defining the collection of procedures in the phase of an Aviator mission.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.Phase`
              - Class defining a phase in an Aviator mission.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PhaseCollection`
              - Class defining the collection of phases.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.Mission`
              - Class defining the Aviator mission.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator`
              - Class defining the Aviator propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureBasicManeuver`
              - Class defining a Basic Maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyWeave`
              - Class defining Weave strategy for a Basic Maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions`
              - Class defining the time options for the current procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CalculationOptions`
              - Class defining the calculation options for a procedure or phase.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftCategory`
              - Class defining the aircraft category in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.Catalog`
              - Class defining the Aviator Catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftModel`
              - Class defining an aircraft in Aviator.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileModel`
              - Class defining a missile in Aviator.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RotorcraftModel`
              - Class defining a rotorcraft in Aviator.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RotorcraftAero`
              - Class defining the aerodynamic options for a rotorcraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RotorcraftProp`
              - Class defining the propulsion options for a rotorcraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration`
              - Class defining the aircraft acceleration category of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel`
              - Class defining the basic acceleration performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftClimb`
              - Class defining the aircraft climb category of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftCruise`
              - Class defining the aircraft cruise category of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftDescent`
              - Class defining the aircraft descent category of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftLanding`
              - Class defining the aircraft landing category of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftTakeoff`
              - Class defining the aircraft takeoff category of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicClimbModel`
              - Class defining the basic climb performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedClimbModel`
              - Class defining the advanced climb performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel`
              - Class defining the basic cruise performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedCruiseModel`
              - Class defining the advanced cruise performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicDescentModel`
              - Class defining the basic descent performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedDescentModel`
              - Class defining the advanced descent performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel`
              - Class defining the basic takeoff performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel`
              - Class defining the advanced takeoff performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicLandingModel`
              - Class defining the basic landing performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel`
              - Class defining the advanced landing performance model for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AirportCategory`
              - Class defining the airport category in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ARINC424Airport`
              - Class defining an ARINC424 Airport.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ARINC424Runway`
              - Class defining an ARINC424 Runway.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DAFIFRunway`
              - Class defining an DAFIF Runway.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DAFIFHelipad`
              - Class defining an DAFIF Helipad.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DAFIFWaypoint`
              - Class defining an DAFIF Waypoint.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RunwayCategory`
              - Class defining the runway category in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.UserRunwaySource`
              - Class defining the user runways in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.UserRunway`
              - Class defining the user runway in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AltitudeMSLOptions`
              - Class defining the altitude MSL options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AltitudeOptions`
              - Class defining the altitude options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ArcAltitudeOptions`
              - Class defining the altitude options for an arc procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ArcAltitudeAndDelayOptions`
              - Class defining the altitude and delay options for an arc procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ArcOptions`
              - Class defining the arc options for a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AltitudeMSLAndLevelOffOptions`
              - Class defining the altitude MSL and Level off options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions`
              - Class defining the cruise airspeed options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedProfile`
              - Class defining the cruise profile options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedAndProfileOptions`
              - Class defining the cruise airspeed and profile options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LandingCruiseAirspeedAndProfileOptions`
              - Class defining the cruise airspeed and profile options for a landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.EnrouteOptions`
              - Class defining the enroute options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.EnrouteAndDelayOptions`
              - Class defining the enroute and delay options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LandingEnrouteOptions`
              - Class defining the enroute options in a landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.EnrouteTurnDirectionOptions`
              - Class defining the enroute turn direction options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.NavigationOptions`
              - Class defining the navigation options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VerticalPlaneOptions`
              - Class defining the vertical plane options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ArcVerticalPlaneOptions`
              - Class defining the vertical plane options in a procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VerticalPlaneAndFlightPathOptions`
              - Class defining the vertical plane options for an arc procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LandingVerticalPlaneOptions`
              - Class defining the vertical plane options in a landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RunwayHeadingOptions`
              - Class defining the runway heading options in a takeoff or landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LandingEnterDownwindPattern`
              - Class defining the enter downwind pattern options for a landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LandingInterceptGlideslope`
              - Class defining the intercept glideslope options for a landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LandingStandardInstrumentApproach`
              - Class defining the standard instrument approach options for a landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TakeoffDeparturePoint`
              - Class defining the departure point options for a takeoff procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TakeoffLowTransition`
              - Class defining the low transition options for a takeoff procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TakeoffNormal`
              - Class defining the normal options for a takeoff procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LevelTurns`
              - Class defining the level turns options for an acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AttitudeTransitions`
              - Class defining the attitude transition options for an acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ClimbAndDescentTransitions`
              - Class defining the climb and descent transition options for an Acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AeroPropManeuverModeHelper`
              - Class defining the The calculation mode for the Aero/Prop maneuver mode helper. Helper for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel`
              - Class defining the advanced acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAccelerationMode`
              - Class defining the acceleration mode options for an advanced acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAero`
              - Class defining the simple aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftExternalAero`
              - Class defining the external file aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAero`
              - Class defining the aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAero`
              - Class defining the basic fixed wing aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftProp`
              - Class defining the propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleProp`
              - Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftExternalProp`
              - Class defining the external propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp`
              - Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ARINC424Source`
              - Class defining an ARINC424 source in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DAFIFSource`
              - Class defining an DAFIF source in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicFixedWingFwdFlightLiftHelper`
              - Class defining the Lift Coefficient Helper for Forward Flight in the Basic Fixed Wing Aerodynamics interface for the Basic Acceleration Model of an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead`
              - Class defining the Straight Ahead strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile`
              - Class defining the Cruise profile strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyGlideProfile`
              - Class defining the Glide profile strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftModels`
              - Class defining the User Aircraft Models in the Aviator Catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileModels`
              - Class defining the User Missile Models in the Aviator Catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RotorcraftModels`
              - Class defining the User Rotorcraft Models in the Aviator Catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.Configuration`
              - Class defining the aircraft configuration for an Aviator mission.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal`
              - Class defining an internal fuel tank for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FuelTankExternal`
              - Class defining an external fuel tank for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PayloadStation`
              - Class defining a payload station for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.StationCollection`
              - Class defining a collection of payload stations for an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.WindModel`
              - Class defining the wind model for a mission, scenario, or procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.WindModelConstant`
              - Class defining a constant bearing/speed wind model for a mission.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.WindModelADDS`
              - Class defining a wind model using the NOAA ADDS service for a mission.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDSMessage`
              - Class defining a message from the NOAA ADDS service.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDSMessageCollection`
              - Class defining a collection of messages from the NOAA ADDS service.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.Procedure`
              - Class defining an unknown procedure type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel`
              - Class defining the atmosphere model for a mission, scenario, or procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic`
              - Class defining the basic atmosphere model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySimpleTurn`
              - Class defining the simple turn strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAileronRoll`
              - Class defining the aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyFlyAOA`
              - Class defining the fly AOA strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPull`
              - Class defining the pull strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRollingPull`
              - Class defining the rolling pull strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAccel`
              - Class defining the smooth accel strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn`
              - Class defining the smooth turn strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions`
              - Class defining the airspeed options for basic maneuver strategies.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust`
              - Class defining the the thrust propulsion used in basic maneuver procedures.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNav`
              - Class defining the autopilot - horizontal plane strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotProf`
              - Class defining the autopiloc - vertical plane strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll`
              - Class defining the barrel roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop`
              - Class defining the loop strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover`
              - Class defining the lighter than air hover strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyIntercept`
              - Class defining the Intercept strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeBearing`
              - Class defining the Relative Bearing strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeCourse`
              - Class defining the Relative Course strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRendezvous`
              - Class defining the Rendezvous/Formation strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStationkeeping`
              - Class defining the Stationkeeping strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFPA`
              - Class defining the Relative Flight Path Angle strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelSpeedAltitude`
              - Class defining the Relative Speed/Altitude strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier`
              - Class defining the Bezier strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull`
              - Class defining the Push/Pull strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingCircular`
              - Class defining a holding circular procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingFigure8`
              - Class defining a holding figure 8 procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureHoldingRacetrack`
              - Class defining a holding racetrack procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover`
              - Class defining a transition to hover procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow`
              - Class defining a terrain following procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureHover`
              - Class defining a hover procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate`
              - Class defining a hover translate procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToForwardFlight`
              - Class defining a transition to forward flight procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HoverAltitudeOptions`
              - Class defining the altitude options for a VTOL procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalTakeoff`
              - Class defining a vertical takeoff procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureVerticalLanding`
              - Class defining a vertical landing procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureReferenceState`
              - Class defining a reference state procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureSuperProcedure`
              - Class defining a super procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunch`
              - Class defining a launch procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureAirway`
              - Class defining an Airway procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureAirwayRouter`
              - Class defining an Airway Router procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureAreaTargetSearch`
              - Class defining an Area Target Search procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureFormationRecover`
              - Class defining a Formation/Recover procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureInFormation`
              - Class defining an In Formation procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureParallelFlightLine`
              - Class defining a Parallel Flight Line procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureVGTPoint`
              - Class defining a VGT Point procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions`
              - Class defining the options for the active performance model in a phase.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool`
              - Class defining the options for the Advanced Fixed Wing Tool of an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingExternalAero`
              - Class defining the External Aero File aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAero`
              - Class defining the subsonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAero`
              - Class defining the Sub/Super/Hypersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAero`
              - Class defining the supersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PerformanceModel`
              - Class defining an unknown performance model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryBasic`
              - Class defining a basic geometry wing in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable`
              - Class defining a variable geometry wing in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingElectricPowerplant`
              - Class defining an Electric powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingExternalProp`
              - Class defining an External Prop File powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp`
              - Class defining a Sub/Super/Hypersonic powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingPistonPowerplant`
              - Class defining a Piston powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingEmpiricalJetEngine`
              - Class defining the Turbojet and Turbofan empirical models in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPowerplant`
              - Do not use this class, as it is deprecated. Use AgAvtrAdvFixedWingTurbofanBasicABProp instead.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPowerplant`
              - Do not use this class, as it is deprecated. Use AgAvtrAdvFixedWingTurbojetBasicABProp instead.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABProp`
              - Class defining the Turbofan - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABProp`
              - Class defining the Turbojet - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbopropPowerplant`
              - Class defining the Turboprop powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAero`
              - Class defining the simple aerodynamic options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileExternalAero`
              - Class defining the external aerodynamic options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileAdvancedAero`
              - Class defining the advanced aerodynamic options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileAero`
              - Class defining the aerodynamic options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileProp`
              - Class defining the propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileSimpleProp`
              - Class defining the Simple propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileExternalProp`
              - Class defining the External propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileRamjetProp`
              - Class defining the Ramjet propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileRocketProp`
              - Class defining the Rocket propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetProp`
              - Class defining the Turbojet propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions`
              - Class defining the Forward Flight options for a Reference State procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ReferenceStateTakeoffLandingOptions`
              - Class defining the Takeoff or Landing options for a Reference State procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions`
              - Class defining the Hover options for a Reference State procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ReferenceStateWeightOnWheelsOptions`
              - Class defining the Weight on Wheels options for a Reference State procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteRunwayFromCatalog`
              - Class defining a runway from catalog site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteAirportFromCatalog`
              - Class defining a airport from catalog site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteNavaidFromCatalog`
              - Class defining a navaid from catalog site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPointFromCatalog`
              - Class defining a VTOL point from catalog site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteWaypointFromCatalog`
              - Class defining a waypoint from catalog site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.NavaidCategory`
              - Class defining the navaid category in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOLPointCategory`
              - Class defining the VTOL point category in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.WaypointCategory`
              - Class defining the waypoint category in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ARINC424Navaid`
              - Class defining an ARINC424 Navaid.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ARINC424Helipad`
              - Class defining an ARINC424 Helipad.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ARINC424Waypoint`
              - Class defining an ARINC424 Waypoint.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.UserVTOLPointSource`
              - Class defining the user VTOL Point source in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.UserVTOLPoint`
              - Class defining the user VTOL Point in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.UserWaypointSource`
              - Class defining the user waypoint source in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.UserWaypoint`
              - Class defining the user waypoint in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PropulsionEfficiencies`
              - Class defining the Propulsion Efficiencies and Losses of a jet engine powerplant in the advanced fixed wing tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FuelModelKeroseneAFPROP`
              - Class defining the Kerosense - AFPROP fuel type for a thermodynamic jet engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FuelModelKeroseneCEA`
              - Class defining the Kerosense - CEA fuel type for a thermodynamic jet engine model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic`
              - Class defining the basic Ramjet model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingScramjetBasic`
              - Class defining the basic Scramjet model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftVTOLModel`
              - Class defining the VTOL performance model of an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftVTOL`
              - Class defining the VTOL category of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel`
              - Class defining the TerrainFollow performance model of an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollow`
              - Class defining the TerrainFollow category of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBallistic3D`
              - Class defining Ballistic 3D strategy for a Basic Maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynState`
              - Class defining a Launch Dyn State procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint`
              - Class defining a Launch Waypoint procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteDynState`
              - Class defining a Dyn State site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D`
              - Class defining Pitch 3D strategy for a Basic Maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties`
              - Class defining the refuel/dump properties for the current procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions`
              - Class defining fast operations (without error or constraint checks) for time options for the current procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVel`
              - Class defining the target position and velocity strategies for basic maneuvers.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng`
              - Class defining the position and velocity strategy, Noisy Bearing Range.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTgt`
              - Class defining the position and velocity strategy, Noisy Surface Target.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ERROR_CODES`
              - Error Codes.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CLOSURE_VALUE`
              - The closure value.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PROCEDURE_TYPE`
              - Aviator procedure types.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SITE_TYPE`
              - Aviator site types.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_STRATEGY`
              - Basic maneuver strategy types.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.STRAIGHT_AHEAD_REFERENCE_FRAME`
              - Straight Ahead basic maneuver Reference Frame.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AIRSPEED_TYPE`
              - Airspeed types.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AERO_PROP_SIMPLE_MODE`
              - Aircraft operating mode for basic acceleration models with aerodynamics set to Simple.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AERO_PROP_FLIGHT_MODE`
              - Flight mode for the Aero/Prop maneuver mode helper in aircraft acceleration models.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PHASE_OF_FLIGHT`
              - Flight mode for basic maneuver procedures.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CRUISE_SPEED`
              - Cruise airspeed type for the procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TAKEOFF_MODE`
              - Takeoff procedure mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.APPROACH_MODE`
              - Landing procedure approach mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.NAVIGATOR_TURN_DIRECTION`
              - Turn mode for procedures with Enroute Turn Direction options.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_FUEL_FLOW_TYPE`
              - Fuel flow type for basic maneuver procedures.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_ALTITUDE_LIMIT`
              - The type of response Aviator will have if the maneuver attempts to exceed the altitude limit.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RUNWAY_HIGH_LOW_END`
              - Runway heading that the aircraft will use.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_REFERENCE_FRAME`
              - Reference frame for the basic maneuver strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT`
              - Define the control limits for the aircraft during the maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ACCEL_MANEUVER_MODE`
              - The mode that the aircraft will adhere to the specified acceleration parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AIRCRAFT_AERO_STRATEGY`
              - The aerodynamic strategy used to compute lift, drag, angle of attack, sideslip and intermediate / derived values.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AIRCRAFT_PROP_STRATEGY`
              - The propulsion strategy used to compute thrust and throttle setting.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AGL_MSL`
              - The altitude mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LANDING_APPROACH_FIX_RANGE_MODE`
              - The reference point on the runway for the Approach Fix Range.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ACCELERATION_ADVANCED_ACCEL_MODE`
              - Acceleration mode for aircraft advanced acceleration models.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ACCEL_MANEUVER_AERO_PROP_MODE`
              - The mode used for the Aero/Prop maneuver mode helper for aircraft basic acceleration models.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS`
              - The type of response Aviator will have if the basic maneuver attempts to exceed the airspeed limit.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE`
              - Powered Cruise Options.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TURN_MODE`
              - The mode to specify an aircraft's level turn performance for acceleration performance models.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.POINT_TO_POINT_MODE`
              - The heading or course of the aircraft at the beginning of the procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ALTITUDE_CONSTRAINT_MANEUVER_MODE`
              - Turn mode for procedures that may require a level off maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.WIND_MODEL_TYPE`
              - The wind model type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.WIND_ATMOS_MODEL_SOURCE`
              - The source for the wind or atmosphere model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDS_MSG_INTERP_TYPE`
              - The interpolation method for the wind conditions.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDS_MISSING_MSG_TYPE`
              - The wind effect to apply if there is an interval gap between messages.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDS_MSG_EXTRAP_TYPE`
              - The wind effect to apply if the procedure(s) extend beyond the intervals of any available messages.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDS_FORECAST_TYPE`
              - The forecast type for the NOAA ADDS message.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ATMOSPHERE_MODEL`
              - The basic atmosphere model type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SMOOTH_TURN_MODE`
              - The basic maneuver smooth turn mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PERF_MODEL_OVERRIDE`
              - The performance model override mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_AIRSPEED_MODE`
              - The basic maneuver airspeed mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AILERON_ROLL_FLIGHT_PATH`
              - The flight path option for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ROLL_LEFT_RIGHT`
              - The roll direction for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ROLL_UPRIGHT_INVERTED`
              - The orientation for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AILERON_ROLL_MODE`
              - The roll mode aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FLY_AOA_LEFT_RIGHT`
              - The roll direction for a Fly AOA strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SMOOTH_ACCEL_LEFT_RIGHT`
              - The roll direction for a smooth acceleration strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PULL_MODE`
              - The pull mode for a pull strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ROLLING_PULL_MODE`
              - The rolling pull mode for a rolling pull strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SMOOTH_ACCEL_STOP_CONDITIONS`
              - The rolling pull mode for a rolling pull strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AUTOPILOT_HORIZ_PLANE_MODE`
              - The autopilot mode for an autopilot - horizontal plane strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ANGLE_MODE`
              - The angle mode for a barrel roll strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HOVER_ALTITUDE_MODE`
              - The altitude mode for the lighter than air hover strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HOVER_HEADING_MODE`
              - The heading mode for the lighter than air hover strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AUTOPILOT_ALTITUDE_MODE`
              - The altitude mode for the autopilot - vertical plane strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AUTOPILOT_ALTITUDE_CONTROL_MODE`
              - The altitude control mode for the autopilot - vertical plane strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CLOSURE_MODE`
              - The closure mode for guidance strategies of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.INTERCEPT_MODE`
              - The intercept mode for the intercept strategy of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RENDEZVOUS_STOP_CONDITION`
              - The stop condition options for a rendezvous formation strategy of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FORMATION_FLYER_STOP_CONDITION`
              - The stop condition options for a Formation Flyer procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.EXT_EPHEM_FLIGHT_MODE`
              - Flight mode enums for ExtEphem.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ACCEL_PERF_MODEL_OVERRIDE`
              - The acceleration performance model override mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.STATIONKEEPING_STOP_CONDITION`
              - The stop condition options for a stationkeeping strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TURN_DIRECTION`
              - The roll direction for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PROFILE_CONTROL_LIMIT`
              - Define the control limits for a profile strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.REL_SPEED_ALTITUDE_STOP_CONDITION`
              - The stop condition options for a relative speed/altitude strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RELATIVE_ALTITUDE_MODE`
              - The relative altitude mode for a relative speed/altitude strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FLY_TO_FLIGHT_PATH_ANGLE_MODE`
              - The flight path angle mode mode for a bezier profile strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PUSH_PULL`
              - The option to pull up or push over for a push/pull profile strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ACCEL_MODE`
              - The acceleration/decelation option for a push/pull profile strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DELAY_ALTITUDE_MODE`
              - The altitude options for a delay procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JOIN_EXIT_ARC_METHOD`
              - The options to join or exit an arc.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FLIGHT_LINE_PROC_TYPE`
              - The procedure methodology used to calculate the flight line.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TRANSITION_TO_HOVER_MODE`
              - The type of hover to transition to.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOL_RATE_MODE`
              - The rate mode for the VTOL procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HOLDING_PROFILE_MODE`
              - How the aircraft will perform during the holding pattern with respect to airspeed and altitude.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HOLDING_DIRECTION`
              - The turn direction for the aircraft to enter the holding pattern.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HOLD_REFUEL_DUMP_MODE`
              - Define when the aircraft will leave the holding pattern after it has completed refueling or dumping fuel.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HOLDING_ENTRY_MANEUVER`
              - Define how the aircraft will enter the holding pattern.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOL_TRANSITION_MODE`
              - The mode to specify the course of the transition maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOL_FINAL_HEADING_MODE`
              - The mode to specify the heading at the end of the maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOL_TRANSLATION_MODE`
              - The mode to specify the translation of the VTOL maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOL_TRANSLATION_FINAL_COURSE_MODE`
              - The mode to specify the final course of the VTOL maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HOVER_MODE`
              - The hover mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOL_HEADING_MODE`
              - The heading mode for the hover maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VERT_LANDING_MODE`
              - The heading mode for a vertical landing maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LAUNCH_ATTITUDE_MODE`
              - The attitude mode for the launch procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FUEL_FLOW_TYPE`
              - The fuel flow type to use for the procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LINE_ORIENTATION`
              - The orientation for a parallel flight line procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.REL_ABS_BEARING`
              - The options for a bearing that can be relative or absolute.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_FIXED_WING_PROP_MODE`
              - The option to specify the thrust (jet engines) or power (propellers).

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CLIMB_SPEED_TYPE`
              - The mode to calculate the aircraft's airspeed while climbing for an advanced climb performance model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CRUISE_MAX_PERF_SPEED_TYPE`
              - The method for defining the maximum performance airspeed of the aircraft for an advanced cruise model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DESCENT_SPEED_TYPE`
              - The method for calculating the aircraft's airspeed while descending.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TAKEOFF_LANDING_SPEED_MODE`
              - The method for calculating the aircraft's speed upon leaving the ground or at wheels down.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DEPARTURE_SPEED_MODE`
              - The method for calculating the aircraft's airspeed upon leaving the ground.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADVANCED_FIXED_WING_AERO_STRATEGY`
              - The aerodynamic strategy for the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADVANCED_FIXED_WING_GEOMETRY`
              - The method to define the wing geometry of an aircraft in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADVANCED_FIXED_WING_POWERPLANT_STRATEGY`
              - The powerplant strategy for the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MISSILE_AERO_STRATEGY`
              - The aerodynamic strategy used to compute lift, drag, angle of attack, sideslip and intermediate / derived values.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MISSILE_PROP_STRATEGY`
              - The propulsion strategy used to compute thrust and throttle setting.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ROTORCRAFT_POWERPLANT_TYPE`
              - The powerplant type for a rotorcraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MINIMIZE_SITE_PROC_TIME_DIFF`
              - Options for minimizing the time difference between the procedure and site times.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.STK_OBJECT_WAYPOINT_OFFSET_MODE`
              - The options to offset the site location relative to the STK Object.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SEARCH_PATTERN_COURSE_MODE`
              - The mode to determine the course of the search pattern.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DELAY_TURN_DIRECTION`
              - Turn mode for procedures with Delay options.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TRAJECTORY_BLEND_MODE`
              - The interpolation mode to determine the aircraft's position and velocity.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.REFERENCE_STATE_PERF_MODE`
              - The type of motion the aircraft is engaged in at the reference state.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE`
              - The mode to specify the longitudinal acceleration of the aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.REFERENCE_STATE_LATERAL_ACCEL_MODE`
              - The mode to specify the lateral acceleration of the aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.REFERENCE_STATE_ATTITUDE_MODE`
              - The mode to specify the attitude rate of change.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AND_OR`
              - The option to specify AND or OR.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JET_ENGINE_TECHNOLOGY_LEVEL`
              - The technology level of the jet engine.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JET_ENGINE_INTAKE_TYPE`
              - The intake type of the jet engine.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JET_ENGINE_TURBINE_TYPE`
              - The turbine type of the jet engine.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JET_ENGINE_EXHAUST_NOZZLE_TYPE`
              - The exhaust nozzle type of the jet engine.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JET_FUEL_TYPE`
              - The jet fuel type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AFPROP_FUEL_TYPE`
              - The AFPROP fuel type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CEA_FUEL_TYPE`
              - The CEA fuel type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TURBINE_MODE`
              - The turbine mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RAMJET_MODE`
              - The ramjet mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SCRAMJET_MODE`
              - The scramjet mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.NUMERICAL_INTEGRATOR`
              - The numerical integrator to be used for the procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BALLISTIC_3D_CONTROL_MODE`
              - The control mode used to define the ballistic 3D strategy of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LAUNCH_DYN_STATE_COORD_FRAME`
              - The coordinate frame used for a LaunchDynState procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LAUNCH_DYN_STATE_BEARING_REFERENCE`
              - The vector used as a bearing reference for a LaunchDynState procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ALTITUDE_REFERENCE`
              - The altitude reference.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SMOOTH_TURN_FPA_MODE`
              - The flight path angle mode for the Smooth Turn strategy of the Basic Maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PITCH_3D_CONTROL_MODE`
              - The control mode used to define the pitch 3D strategy of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.REFUEL_DUMP_MODE`
              - The modes used to define procedure refuel/dump modes.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE`
              - The modes used to define basic maneuver glide speed control modes.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TARGET_POSITION_VEL_TYPE`
              - The target pos/vel type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.EPHEM_SHIFT_ROTATE_ALTITUDE_MODE`
              - Ephem alt mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.EPHEM_SHIFT_ROTATE_COURSE_MODE`
              - Ephem course mode.



Description
-----------

Object Model components specifically designed to support STK Aviator.


.. py:currentmodule:: ansys.stk.core.stkobjects.aviator


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    🗎 matlab<aviator/matlab>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ISite<aviator/ISite>
     ICatalogItem<aviator/ICatalogItem>
     IBasicManeuverStrategy<aviator/IBasicManeuverStrategy>
     IAviatorVehicle<aviator/IAviatorVehicle>
     IARINC424Item<aviator/IARINC424Item>
     IStation<aviator/IStation>
     ICatalogSource<aviator/ICatalogSource>
     IBasicFixedWingLiftHelper<aviator/IBasicFixedWingLiftHelper>
     ICatalogRunway<aviator/ICatalogRunway>
     ICatalogAirport<aviator/ICatalogAirport>
     ICatalogNavaid<aviator/ICatalogNavaid>
     ICatalogVTOLPoint<aviator/ICatalogVTOLPoint>
     ICatalogWaypoint<aviator/ICatalogWaypoint>
     IARINC424Airport<aviator/IARINC424Airport>
     IDAFIFItem<aviator/IDAFIFItem>
     IVerticalPlaneOptions<aviator/IVerticalPlaneOptions>
     IEnrouteAndDelayOptions<aviator/IEnrouteAndDelayOptions>
     ICruiseAirspeedAndProfileOptions<aviator/ICruiseAirspeedAndProfileOptions>
     IAutomationStrategyFactory<aviator/IAutomationStrategyFactory>
     IConnect<aviator/IConnect>
     IProcedure<aviator/IProcedure>
     IPerformanceModel<aviator/IPerformanceModel>
     IAdvancedFixedWingGeometry<aviator/IAdvancedFixedWingGeometry>
     IAdvancedFixedWingPowerplant<aviator/IAdvancedFixedWingPowerplant>
     ISiteUnknown<aviator/ISiteUnknown>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     SiteWaypoint<aviator/SiteWaypoint>
     SiteEndOfPrevProcedure<aviator/SiteEndOfPrevProcedure>
     SiteVTOLPoint<aviator/SiteVTOLPoint>
     SiteReferenceState<aviator/SiteReferenceState>
     SiteSTKVehicle<aviator/SiteSTKVehicle>
     SiteSuperProcedure<aviator/SiteSuperProcedure>
     SiteRelToPrevProcedure<aviator/SiteRelToPrevProcedure>
     SiteSTKObjectWaypoint<aviator/SiteSTKObjectWaypoint>
     SiteSTKStaticObject<aviator/SiteSTKStaticObject>
     SiteRelToSTKObject<aviator/SiteRelToSTKObject>
     SiteSTKAreaTarget<aviator/SiteSTKAreaTarget>
     SiteRunway<aviator/SiteRunway>
     Site<aviator/Site>
     ProcedureLanding<aviator/ProcedureLanding>
     ProcedureEnroute<aviator/ProcedureEnroute>
     ProcedureExtEphem<aviator/ProcedureExtEphem>
     ProcedureFormationFlyer<aviator/ProcedureFormationFlyer>
     ProcedureBasicPointToPoint<aviator/ProcedureBasicPointToPoint>
     ProcedureArcEnroute<aviator/ProcedureArcEnroute>
     ProcedureArcPointToPoint<aviator/ProcedureArcPointToPoint>
     ProcedureFlightLine<aviator/ProcedureFlightLine>
     ProcedureDelay<aviator/ProcedureDelay>
     ProcedureTakeoff<aviator/ProcedureTakeoff>
     ProcedureCollection<aviator/ProcedureCollection>
     Phase<aviator/Phase>
     PhaseCollection<aviator/PhaseCollection>
     Mission<aviator/Mission>
     AviatorPropagator<aviator/AviatorPropagator>
     ProcedureBasicManeuver<aviator/ProcedureBasicManeuver>
     BasicManeuverStrategyWeave<aviator/BasicManeuverStrategyWeave>
     ProcedureTimeOptions<aviator/ProcedureTimeOptions>
     CalculationOptions<aviator/CalculationOptions>
     AircraftCategory<aviator/AircraftCategory>
     Catalog<aviator/Catalog>
     AircraftModel<aviator/AircraftModel>
     MissileModel<aviator/MissileModel>
     RotorcraftModel<aviator/RotorcraftModel>
     RotorcraftAero<aviator/RotorcraftAero>
     RotorcraftProp<aviator/RotorcraftProp>
     AircraftAcceleration<aviator/AircraftAcceleration>
     AircraftBasicAccelerationModel<aviator/AircraftBasicAccelerationModel>
     AircraftClimb<aviator/AircraftClimb>
     AircraftCruise<aviator/AircraftCruise>
     AircraftDescent<aviator/AircraftDescent>
     AircraftLanding<aviator/AircraftLanding>
     AircraftTakeoff<aviator/AircraftTakeoff>
     AircraftBasicClimbModel<aviator/AircraftBasicClimbModel>
     AircraftAdvancedClimbModel<aviator/AircraftAdvancedClimbModel>
     AircraftBasicCruiseModel<aviator/AircraftBasicCruiseModel>
     AircraftAdvancedCruiseModel<aviator/AircraftAdvancedCruiseModel>
     AircraftBasicDescentModel<aviator/AircraftBasicDescentModel>
     AircraftAdvancedDescentModel<aviator/AircraftAdvancedDescentModel>
     AircraftBasicTakeoffModel<aviator/AircraftBasicTakeoffModel>
     AircraftAdvancedTakeoffModel<aviator/AircraftAdvancedTakeoffModel>
     AircraftBasicLandingModel<aviator/AircraftBasicLandingModel>
     AircraftAdvancedLandingModel<aviator/AircraftAdvancedLandingModel>
     AirportCategory<aviator/AirportCategory>
     ARINC424Airport<aviator/ARINC424Airport>
     ARINC424Runway<aviator/ARINC424Runway>
     DAFIFRunway<aviator/DAFIFRunway>
     DAFIFHelipad<aviator/DAFIFHelipad>
     DAFIFWaypoint<aviator/DAFIFWaypoint>
     RunwayCategory<aviator/RunwayCategory>
     UserRunwaySource<aviator/UserRunwaySource>
     UserRunway<aviator/UserRunway>
     AltitudeMSLOptions<aviator/AltitudeMSLOptions>
     AltitudeOptions<aviator/AltitudeOptions>
     ArcAltitudeOptions<aviator/ArcAltitudeOptions>
     ArcAltitudeAndDelayOptions<aviator/ArcAltitudeAndDelayOptions>
     ArcOptions<aviator/ArcOptions>
     AltitudeMSLAndLevelOffOptions<aviator/AltitudeMSLAndLevelOffOptions>
     CruiseAirspeedOptions<aviator/CruiseAirspeedOptions>
     CruiseAirspeedProfile<aviator/CruiseAirspeedProfile>
     CruiseAirspeedAndProfileOptions<aviator/CruiseAirspeedAndProfileOptions>
     LandingCruiseAirspeedAndProfileOptions<aviator/LandingCruiseAirspeedAndProfileOptions>
     EnrouteOptions<aviator/EnrouteOptions>
     EnrouteAndDelayOptions<aviator/EnrouteAndDelayOptions>
     LandingEnrouteOptions<aviator/LandingEnrouteOptions>
     EnrouteTurnDirectionOptions<aviator/EnrouteTurnDirectionOptions>
     NavigationOptions<aviator/NavigationOptions>
     VerticalPlaneOptions<aviator/VerticalPlaneOptions>
     ArcVerticalPlaneOptions<aviator/ArcVerticalPlaneOptions>
     VerticalPlaneAndFlightPathOptions<aviator/VerticalPlaneAndFlightPathOptions>
     LandingVerticalPlaneOptions<aviator/LandingVerticalPlaneOptions>
     RunwayHeadingOptions<aviator/RunwayHeadingOptions>
     LandingEnterDownwindPattern<aviator/LandingEnterDownwindPattern>
     LandingInterceptGlideslope<aviator/LandingInterceptGlideslope>
     LandingStandardInstrumentApproach<aviator/LandingStandardInstrumentApproach>
     TakeoffDeparturePoint<aviator/TakeoffDeparturePoint>
     TakeoffLowTransition<aviator/TakeoffLowTransition>
     TakeoffNormal<aviator/TakeoffNormal>
     LevelTurns<aviator/LevelTurns>
     AttitudeTransitions<aviator/AttitudeTransitions>
     ClimbAndDescentTransitions<aviator/ClimbAndDescentTransitions>
     AeroPropManeuverModeHelper<aviator/AeroPropManeuverModeHelper>
     AircraftAdvancedAccelerationModel<aviator/AircraftAdvancedAccelerationModel>
     AircraftAccelerationMode<aviator/AircraftAccelerationMode>
     AircraftSimpleAero<aviator/AircraftSimpleAero>
     AircraftExternalAero<aviator/AircraftExternalAero>
     AircraftAero<aviator/AircraftAero>
     AircraftBasicFixedWingAero<aviator/AircraftBasicFixedWingAero>
     AircraftProp<aviator/AircraftProp>
     AircraftSimpleProp<aviator/AircraftSimpleProp>
     AircraftExternalProp<aviator/AircraftExternalProp>
     AircraftBasicFixedWingProp<aviator/AircraftBasicFixedWingProp>
     ARINC424Source<aviator/ARINC424Source>
     DAFIFSource<aviator/DAFIFSource>
     BasicFixedWingFwdFlightLiftHelper<aviator/BasicFixedWingFwdFlightLiftHelper>
     BasicManeuverStrategyStraightAhead<aviator/BasicManeuverStrategyStraightAhead>
     BasicManeuverStrategyCruiseProfile<aviator/BasicManeuverStrategyCruiseProfile>
     BasicManeuverStrategyGlideProfile<aviator/BasicManeuverStrategyGlideProfile>
     AircraftModels<aviator/AircraftModels>
     MissileModels<aviator/MissileModels>
     RotorcraftModels<aviator/RotorcraftModels>
     Configuration<aviator/Configuration>
     FuelTankInternal<aviator/FuelTankInternal>
     FuelTankExternal<aviator/FuelTankExternal>
     PayloadStation<aviator/PayloadStation>
     StationCollection<aviator/StationCollection>
     WindModel<aviator/WindModel>
     WindModelConstant<aviator/WindModelConstant>
     WindModelADDS<aviator/WindModelADDS>
     ADDSMessage<aviator/ADDSMessage>
     ADDSMessageCollection<aviator/ADDSMessageCollection>
     Procedure<aviator/Procedure>
     AtmosphereModel<aviator/AtmosphereModel>
     AtmosphereModelBasic<aviator/AtmosphereModelBasic>
     BasicManeuverStrategySimpleTurn<aviator/BasicManeuverStrategySimpleTurn>
     BasicManeuverStrategyAileronRoll<aviator/BasicManeuverStrategyAileronRoll>
     BasicManeuverStrategyFlyAOA<aviator/BasicManeuverStrategyFlyAOA>
     BasicManeuverStrategyPull<aviator/BasicManeuverStrategyPull>
     BasicManeuverStrategyRollingPull<aviator/BasicManeuverStrategyRollingPull>
     BasicManeuverStrategySmoothAccel<aviator/BasicManeuverStrategySmoothAccel>
     BasicManeuverStrategySmoothTurn<aviator/BasicManeuverStrategySmoothTurn>
     BasicManeuverAirspeedOptions<aviator/BasicManeuverAirspeedOptions>
     PropulsionThrust<aviator/PropulsionThrust>
     BasicManeuverStrategyAutopilotNav<aviator/BasicManeuverStrategyAutopilotNav>
     BasicManeuverStrategyAutopilotProf<aviator/BasicManeuverStrategyAutopilotProf>
     BasicManeuverStrategyBarrelRoll<aviator/BasicManeuverStrategyBarrelRoll>
     BasicManeuverStrategyLoop<aviator/BasicManeuverStrategyLoop>
     BasicManeuverStrategyLTAHover<aviator/BasicManeuverStrategyLTAHover>
     BasicManeuverStrategyIntercept<aviator/BasicManeuverStrategyIntercept>
     BasicManeuverStrategyRelativeBearing<aviator/BasicManeuverStrategyRelativeBearing>
     BasicManeuverStrategyRelativeCourse<aviator/BasicManeuverStrategyRelativeCourse>
     BasicManeuverStrategyRendezvous<aviator/BasicManeuverStrategyRendezvous>
     BasicManeuverStrategyStationkeeping<aviator/BasicManeuverStrategyStationkeeping>
     BasicManeuverStrategyRelativeFPA<aviator/BasicManeuverStrategyRelativeFPA>
     BasicManeuverStrategyRelSpeedAltitude<aviator/BasicManeuverStrategyRelSpeedAltitude>
     BasicManeuverStrategyBezier<aviator/BasicManeuverStrategyBezier>
     BasicManeuverStrategyPushPull<aviator/BasicManeuverStrategyPushPull>
     ProcedureHoldingCircular<aviator/ProcedureHoldingCircular>
     ProcedureHoldingFigure8<aviator/ProcedureHoldingFigure8>
     ProcedureHoldingRacetrack<aviator/ProcedureHoldingRacetrack>
     ProcedureTransitionToHover<aviator/ProcedureTransitionToHover>
     ProcedureTerrainFollow<aviator/ProcedureTerrainFollow>
     ProcedureHover<aviator/ProcedureHover>
     ProcedureHoverTranslate<aviator/ProcedureHoverTranslate>
     ProcedureTransitionToForwardFlight<aviator/ProcedureTransitionToForwardFlight>
     HoverAltitudeOptions<aviator/HoverAltitudeOptions>
     ProcedureVerticalTakeoff<aviator/ProcedureVerticalTakeoff>
     ProcedureVerticalLanding<aviator/ProcedureVerticalLanding>
     ProcedureReferenceState<aviator/ProcedureReferenceState>
     ProcedureSuperProcedure<aviator/ProcedureSuperProcedure>
     ProcedureLaunch<aviator/ProcedureLaunch>
     ProcedureAirway<aviator/ProcedureAirway>
     ProcedureAirwayRouter<aviator/ProcedureAirwayRouter>
     ProcedureAreaTargetSearch<aviator/ProcedureAreaTargetSearch>
     ProcedureFormationRecover<aviator/ProcedureFormationRecover>
     ProcedureInFormation<aviator/ProcedureInFormation>
     ProcedureParallelFlightLine<aviator/ProcedureParallelFlightLine>
     ProcedureVGTPoint<aviator/ProcedureVGTPoint>
     PerformanceModelOptions<aviator/PerformanceModelOptions>
     AdvancedFixedWingTool<aviator/AdvancedFixedWingTool>
     AdvancedFixedWingExternalAero<aviator/AdvancedFixedWingExternalAero>
     AdvancedFixedWingSubsonicAero<aviator/AdvancedFixedWingSubsonicAero>
     AdvancedFixedWingSubSuperHypersonicAero<aviator/AdvancedFixedWingSubSuperHypersonicAero>
     AdvancedFixedWingSupersonicAero<aviator/AdvancedFixedWingSupersonicAero>
     PerformanceModel<aviator/PerformanceModel>
     AdvancedFixedWingGeometryBasic<aviator/AdvancedFixedWingGeometryBasic>
     AdvancedFixedWingGeometryVariable<aviator/AdvancedFixedWingGeometryVariable>
     AdvancedFixedWingElectricPowerplant<aviator/AdvancedFixedWingElectricPowerplant>
     AdvancedFixedWingExternalProp<aviator/AdvancedFixedWingExternalProp>
     AdvancedFixedWingSubSuperHypersonicProp<aviator/AdvancedFixedWingSubSuperHypersonicProp>
     AdvancedFixedWingPistonPowerplant<aviator/AdvancedFixedWingPistonPowerplant>
     AdvancedFixedWingEmpiricalJetEngine<aviator/AdvancedFixedWingEmpiricalJetEngine>
     AdvancedFixedWingTurbofanBasicABPowerplant<aviator/AdvancedFixedWingTurbofanBasicABPowerplant>
     AdvancedFixedWingTurbojetBasicABPowerplant<aviator/AdvancedFixedWingTurbojetBasicABPowerplant>
     AdvancedFixedWingTurbofanBasicABProp<aviator/AdvancedFixedWingTurbofanBasicABProp>
     AdvancedFixedWingTurbojetBasicABProp<aviator/AdvancedFixedWingTurbojetBasicABProp>
     AdvancedFixedWingTurbopropPowerplant<aviator/AdvancedFixedWingTurbopropPowerplant>
     MissileSimpleAero<aviator/MissileSimpleAero>
     MissileExternalAero<aviator/MissileExternalAero>
     MissileAdvancedAero<aviator/MissileAdvancedAero>
     MissileAero<aviator/MissileAero>
     MissileProp<aviator/MissileProp>
     MissileSimpleProp<aviator/MissileSimpleProp>
     MissileExternalProp<aviator/MissileExternalProp>
     MissileRamjetProp<aviator/MissileRamjetProp>
     MissileRocketProp<aviator/MissileRocketProp>
     MissileTurbojetProp<aviator/MissileTurbojetProp>
     ReferenceStateForwardFlightOptions<aviator/ReferenceStateForwardFlightOptions>
     ReferenceStateTakeoffLandingOptions<aviator/ReferenceStateTakeoffLandingOptions>
     ReferenceStateHoverOptions<aviator/ReferenceStateHoverOptions>
     ReferenceStateWeightOnWheelsOptions<aviator/ReferenceStateWeightOnWheelsOptions>
     SiteRunwayFromCatalog<aviator/SiteRunwayFromCatalog>
     SiteAirportFromCatalog<aviator/SiteAirportFromCatalog>
     SiteNavaidFromCatalog<aviator/SiteNavaidFromCatalog>
     SiteVTOLPointFromCatalog<aviator/SiteVTOLPointFromCatalog>
     SiteWaypointFromCatalog<aviator/SiteWaypointFromCatalog>
     NavaidCategory<aviator/NavaidCategory>
     VTOLPointCategory<aviator/VTOLPointCategory>
     WaypointCategory<aviator/WaypointCategory>
     ARINC424Navaid<aviator/ARINC424Navaid>
     ARINC424Helipad<aviator/ARINC424Helipad>
     ARINC424Waypoint<aviator/ARINC424Waypoint>
     UserVTOLPointSource<aviator/UserVTOLPointSource>
     UserVTOLPoint<aviator/UserVTOLPoint>
     UserWaypointSource<aviator/UserWaypointSource>
     UserWaypoint<aviator/UserWaypoint>
     PropulsionEfficiencies<aviator/PropulsionEfficiencies>
     FuelModelKeroseneAFPROP<aviator/FuelModelKeroseneAFPROP>
     FuelModelKeroseneCEA<aviator/FuelModelKeroseneCEA>
     AdvancedFixedWingRamjetBasic<aviator/AdvancedFixedWingRamjetBasic>
     AdvancedFixedWingScramjetBasic<aviator/AdvancedFixedWingScramjetBasic>
     AircraftVTOLModel<aviator/AircraftVTOLModel>
     AircraftVTOL<aviator/AircraftVTOL>
     AircraftTerrainFollowModel<aviator/AircraftTerrainFollowModel>
     AircraftTerrainFollow<aviator/AircraftTerrainFollow>
     BasicManeuverStrategyBallistic3D<aviator/BasicManeuverStrategyBallistic3D>
     ProcedureLaunchDynState<aviator/ProcedureLaunchDynState>
     ProcedureLaunchWaypoint<aviator/ProcedureLaunchWaypoint>
     SiteDynState<aviator/SiteDynState>
     BasicManeuverStrategyPitch3D<aviator/BasicManeuverStrategyPitch3D>
     RefuelDumpProperties<aviator/RefuelDumpProperties>
     ProcedureFastTimeOptions<aviator/ProcedureFastTimeOptions>
     BasicManeuverTargetPositionVel<aviator/BasicManeuverTargetPositionVel>
     BasicManeuverTargetPositionVelNoisyBrgRng<aviator/BasicManeuverTargetPositionVelNoisyBrgRng>
     BasicManeuverTargetPositionVelNoisySurfTgt<aviator/BasicManeuverTargetPositionVelNoisySurfTgt>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ ERROR_CODES<aviator/ERROR_CODES_enum>
    ≔ CLOSURE_VALUE<aviator/CLOSURE_VALUE_enum>
    ≔ PROCEDURE_TYPE<aviator/PROCEDURE_TYPE_enum>
    ≔ SITE_TYPE<aviator/SITE_TYPE_enum>
    ≔ BASIC_MANEUVER_STRATEGY<aviator/BASIC_MANEUVER_STRATEGY_enum>
    ≔ STRAIGHT_AHEAD_REFERENCE_FRAME<aviator/STRAIGHT_AHEAD_REFERENCE_FRAME_enum>
    ≔ AIRSPEED_TYPE<aviator/AIRSPEED_TYPE_enum>
    ≔ AERO_PROP_SIMPLE_MODE<aviator/AERO_PROP_SIMPLE_MODE_enum>
    ≔ AERO_PROP_FLIGHT_MODE<aviator/AERO_PROP_FLIGHT_MODE_enum>
    ≔ PHASE_OF_FLIGHT<aviator/PHASE_OF_FLIGHT_enum>
    ≔ CRUISE_SPEED<aviator/CRUISE_SPEED_enum>
    ≔ TAKEOFF_MODE<aviator/TAKEOFF_MODE_enum>
    ≔ APPROACH_MODE<aviator/APPROACH_MODE_enum>
    ≔ NAVIGATOR_TURN_DIRECTION<aviator/NAVIGATOR_TURN_DIRECTION_enum>
    ≔ BASIC_MANEUVER_FUEL_FLOW_TYPE<aviator/BASIC_MANEUVER_FUEL_FLOW_TYPE_enum>
    ≔ BASIC_MANEUVER_ALTITUDE_LIMIT<aviator/BASIC_MANEUVER_ALTITUDE_LIMIT_enum>
    ≔ RUNWAY_HIGH_LOW_END<aviator/RUNWAY_HIGH_LOW_END_enum>
    ≔ BASIC_MANEUVER_REFERENCE_FRAME<aviator/BASIC_MANEUVER_REFERENCE_FRAME_enum>
    ≔ BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT<aviator/BASIC_MANEUVER_STRATEGY_NAV_CONTROL_LIMIT_enum>
    ≔ ACCEL_MANEUVER_MODE<aviator/ACCEL_MANEUVER_MODE_enum>
    ≔ AIRCRAFT_AERO_STRATEGY<aviator/AIRCRAFT_AERO_STRATEGY_enum>
    ≔ AIRCRAFT_PROP_STRATEGY<aviator/AIRCRAFT_PROP_STRATEGY_enum>
    ≔ AGL_MSL<aviator/AGL_MSL_enum>
    ≔ LANDING_APPROACH_FIX_RANGE_MODE<aviator/LANDING_APPROACH_FIX_RANGE_MODE_enum>
    ≔ ACCELERATION_ADVANCED_ACCEL_MODE<aviator/ACCELERATION_ADVANCED_ACCEL_MODE_enum>
    ≔ ACCEL_MANEUVER_AERO_PROP_MODE<aviator/ACCEL_MANEUVER_AERO_PROP_MODE_enum>
    ≔ BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS<aviator/BASIC_MANEUVER_STRATEGY_AIRSPEED_PERF_LIMITS_enum>
    ≔ BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE<aviator/BASIC_MANEUVER_STRATEGY_POWERED_CRUISE_MODE_enum>
    ≔ TURN_MODE<aviator/TURN_MODE_enum>
    ≔ POINT_TO_POINT_MODE<aviator/POINT_TO_POINT_MODE_enum>
    ≔ ALTITUDE_CONSTRAINT_MANEUVER_MODE<aviator/ALTITUDE_CONSTRAINT_MANEUVER_MODE_enum>
    ≔ WIND_MODEL_TYPE<aviator/WIND_MODEL_TYPE_enum>
    ≔ WIND_ATMOS_MODEL_SOURCE<aviator/WIND_ATMOS_MODEL_SOURCE_enum>
    ≔ ADDS_MSG_INTERP_TYPE<aviator/ADDS_MSG_INTERP_TYPE_enum>
    ≔ ADDS_MISSING_MSG_TYPE<aviator/ADDS_MISSING_MSG_TYPE_enum>
    ≔ ADDS_MSG_EXTRAP_TYPE<aviator/ADDS_MSG_EXTRAP_TYPE_enum>
    ≔ ADDS_FORECAST_TYPE<aviator/ADDS_FORECAST_TYPE_enum>
    ≔ ATMOSPHERE_MODEL<aviator/ATMOSPHERE_MODEL_enum>
    ≔ SMOOTH_TURN_MODE<aviator/SMOOTH_TURN_MODE_enum>
    ≔ PERF_MODEL_OVERRIDE<aviator/PERF_MODEL_OVERRIDE_enum>
    ≔ BASIC_MANEUVER_AIRSPEED_MODE<aviator/BASIC_MANEUVER_AIRSPEED_MODE_enum>
    ≔ AILERON_ROLL_FLIGHT_PATH<aviator/AILERON_ROLL_FLIGHT_PATH_enum>
    ≔ ROLL_LEFT_RIGHT<aviator/ROLL_LEFT_RIGHT_enum>
    ≔ ROLL_UPRIGHT_INVERTED<aviator/ROLL_UPRIGHT_INVERTED_enum>
    ≔ AILERON_ROLL_MODE<aviator/AILERON_ROLL_MODE_enum>
    ≔ FLY_AOA_LEFT_RIGHT<aviator/FLY_AOA_LEFT_RIGHT_enum>
    ≔ SMOOTH_ACCEL_LEFT_RIGHT<aviator/SMOOTH_ACCEL_LEFT_RIGHT_enum>
    ≔ PULL_MODE<aviator/PULL_MODE_enum>
    ≔ ROLLING_PULL_MODE<aviator/ROLLING_PULL_MODE_enum>
    ≔ SMOOTH_ACCEL_STOP_CONDITIONS<aviator/SMOOTH_ACCEL_STOP_CONDITIONS_enum>
    ≔ AUTOPILOT_HORIZ_PLANE_MODE<aviator/AUTOPILOT_HORIZ_PLANE_MODE_enum>
    ≔ ANGLE_MODE<aviator/ANGLE_MODE_enum>
    ≔ HOVER_ALTITUDE_MODE<aviator/HOVER_ALTITUDE_MODE_enum>
    ≔ HOVER_HEADING_MODE<aviator/HOVER_HEADING_MODE_enum>
    ≔ AUTOPILOT_ALTITUDE_MODE<aviator/AUTOPILOT_ALTITUDE_MODE_enum>
    ≔ AUTOPILOT_ALTITUDE_CONTROL_MODE<aviator/AUTOPILOT_ALTITUDE_CONTROL_MODE_enum>
    ≔ CLOSURE_MODE<aviator/CLOSURE_MODE_enum>
    ≔ INTERCEPT_MODE<aviator/INTERCEPT_MODE_enum>
    ≔ RENDEZVOUS_STOP_CONDITION<aviator/RENDEZVOUS_STOP_CONDITION_enum>
    ≔ FORMATION_FLYER_STOP_CONDITION<aviator/FORMATION_FLYER_STOP_CONDITION_enum>
    ≔ EXT_EPHEM_FLIGHT_MODE<aviator/EXT_EPHEM_FLIGHT_MODE_enum>
    ≔ ACCEL_PERF_MODEL_OVERRIDE<aviator/ACCEL_PERF_MODEL_OVERRIDE_enum>
    ≔ STATIONKEEPING_STOP_CONDITION<aviator/STATIONKEEPING_STOP_CONDITION_enum>
    ≔ TURN_DIRECTION<aviator/TURN_DIRECTION_enum>
    ≔ PROFILE_CONTROL_LIMIT<aviator/PROFILE_CONTROL_LIMIT_enum>
    ≔ REL_SPEED_ALTITUDE_STOP_CONDITION<aviator/REL_SPEED_ALTITUDE_STOP_CONDITION_enum>
    ≔ RELATIVE_ALTITUDE_MODE<aviator/RELATIVE_ALTITUDE_MODE_enum>
    ≔ FLY_TO_FLIGHT_PATH_ANGLE_MODE<aviator/FLY_TO_FLIGHT_PATH_ANGLE_MODE_enum>
    ≔ PUSH_PULL<aviator/PUSH_PULL_enum>
    ≔ ACCEL_MODE<aviator/ACCEL_MODE_enum>
    ≔ DELAY_ALTITUDE_MODE<aviator/DELAY_ALTITUDE_MODE_enum>
    ≔ JOIN_EXIT_ARC_METHOD<aviator/JOIN_EXIT_ARC_METHOD_enum>
    ≔ FLIGHT_LINE_PROC_TYPE<aviator/FLIGHT_LINE_PROC_TYPE_enum>
    ≔ TRANSITION_TO_HOVER_MODE<aviator/TRANSITION_TO_HOVER_MODE_enum>
    ≔ VTOL_RATE_MODE<aviator/VTOL_RATE_MODE_enum>
    ≔ HOLDING_PROFILE_MODE<aviator/HOLDING_PROFILE_MODE_enum>
    ≔ HOLDING_DIRECTION<aviator/HOLDING_DIRECTION_enum>
    ≔ HOLD_REFUEL_DUMP_MODE<aviator/HOLD_REFUEL_DUMP_MODE_enum>
    ≔ HOLDING_ENTRY_MANEUVER<aviator/HOLDING_ENTRY_MANEUVER_enum>
    ≔ VTOL_TRANSITION_MODE<aviator/VTOL_TRANSITION_MODE_enum>
    ≔ VTOL_FINAL_HEADING_MODE<aviator/VTOL_FINAL_HEADING_MODE_enum>
    ≔ VTOL_TRANSLATION_MODE<aviator/VTOL_TRANSLATION_MODE_enum>
    ≔ VTOL_TRANSLATION_FINAL_COURSE_MODE<aviator/VTOL_TRANSLATION_FINAL_COURSE_MODE_enum>
    ≔ HOVER_MODE<aviator/HOVER_MODE_enum>
    ≔ VTOL_HEADING_MODE<aviator/VTOL_HEADING_MODE_enum>
    ≔ VERT_LANDING_MODE<aviator/VERT_LANDING_MODE_enum>
    ≔ LAUNCH_ATTITUDE_MODE<aviator/LAUNCH_ATTITUDE_MODE_enum>
    ≔ FUEL_FLOW_TYPE<aviator/FUEL_FLOW_TYPE_enum>
    ≔ LINE_ORIENTATION<aviator/LINE_ORIENTATION_enum>
    ≔ REL_ABS_BEARING<aviator/REL_ABS_BEARING_enum>
    ≔ BASIC_FIXED_WING_PROP_MODE<aviator/BASIC_FIXED_WING_PROP_MODE_enum>
    ≔ CLIMB_SPEED_TYPE<aviator/CLIMB_SPEED_TYPE_enum>
    ≔ CRUISE_MAX_PERF_SPEED_TYPE<aviator/CRUISE_MAX_PERF_SPEED_TYPE_enum>
    ≔ DESCENT_SPEED_TYPE<aviator/DESCENT_SPEED_TYPE_enum>
    ≔ TAKEOFF_LANDING_SPEED_MODE<aviator/TAKEOFF_LANDING_SPEED_MODE_enum>
    ≔ DEPARTURE_SPEED_MODE<aviator/DEPARTURE_SPEED_MODE_enum>
    ≔ ADVANCED_FIXED_WING_AERO_STRATEGY<aviator/ADVANCED_FIXED_WING_AERO_STRATEGY_enum>
    ≔ ADVANCED_FIXED_WING_GEOMETRY<aviator/ADVANCED_FIXED_WING_GEOMETRY_enum>
    ≔ ADVANCED_FIXED_WING_POWERPLANT_STRATEGY<aviator/ADVANCED_FIXED_WING_POWERPLANT_STRATEGY_enum>
    ≔ MISSILE_AERO_STRATEGY<aviator/MISSILE_AERO_STRATEGY_enum>
    ≔ MISSILE_PROP_STRATEGY<aviator/MISSILE_PROP_STRATEGY_enum>
    ≔ ROTORCRAFT_POWERPLANT_TYPE<aviator/ROTORCRAFT_POWERPLANT_TYPE_enum>
    ≔ MINIMIZE_SITE_PROC_TIME_DIFF<aviator/MINIMIZE_SITE_PROC_TIME_DIFF_enum>
    ≔ STK_OBJECT_WAYPOINT_OFFSET_MODE<aviator/STK_OBJECT_WAYPOINT_OFFSET_MODE_enum>
    ≔ SEARCH_PATTERN_COURSE_MODE<aviator/SEARCH_PATTERN_COURSE_MODE_enum>
    ≔ DELAY_TURN_DIRECTION<aviator/DELAY_TURN_DIRECTION_enum>
    ≔ TRAJECTORY_BLEND_MODE<aviator/TRAJECTORY_BLEND_MODE_enum>
    ≔ REFERENCE_STATE_PERF_MODE<aviator/REFERENCE_STATE_PERF_MODE_enum>
    ≔ REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE<aviator/REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE_enum>
    ≔ REFERENCE_STATE_LATERAL_ACCEL_MODE<aviator/REFERENCE_STATE_LATERAL_ACCEL_MODE_enum>
    ≔ REFERENCE_STATE_ATTITUDE_MODE<aviator/REFERENCE_STATE_ATTITUDE_MODE_enum>
    ≔ AND_OR<aviator/AND_OR_enum>
    ≔ JET_ENGINE_TECHNOLOGY_LEVEL<aviator/JET_ENGINE_TECHNOLOGY_LEVEL_enum>
    ≔ JET_ENGINE_INTAKE_TYPE<aviator/JET_ENGINE_INTAKE_TYPE_enum>
    ≔ JET_ENGINE_TURBINE_TYPE<aviator/JET_ENGINE_TURBINE_TYPE_enum>
    ≔ JET_ENGINE_EXHAUST_NOZZLE_TYPE<aviator/JET_ENGINE_EXHAUST_NOZZLE_TYPE_enum>
    ≔ JET_FUEL_TYPE<aviator/JET_FUEL_TYPE_enum>
    ≔ AFPROP_FUEL_TYPE<aviator/AFPROP_FUEL_TYPE_enum>
    ≔ CEA_FUEL_TYPE<aviator/CEA_FUEL_TYPE_enum>
    ≔ TURBINE_MODE<aviator/TURBINE_MODE_enum>
    ≔ RAMJET_MODE<aviator/RAMJET_MODE_enum>
    ≔ SCRAMJET_MODE<aviator/SCRAMJET_MODE_enum>
    ≔ NUMERICAL_INTEGRATOR<aviator/NUMERICAL_INTEGRATOR_enum>
    ≔ BALLISTIC_3D_CONTROL_MODE<aviator/BALLISTIC_3D_CONTROL_MODE_enum>
    ≔ LAUNCH_DYN_STATE_COORD_FRAME<aviator/LAUNCH_DYN_STATE_COORD_FRAME_enum>
    ≔ LAUNCH_DYN_STATE_BEARING_REFERENCE<aviator/LAUNCH_DYN_STATE_BEARING_REFERENCE_enum>
    ≔ ALTITUDE_REFERENCE<aviator/ALTITUDE_REFERENCE_enum>
    ≔ SMOOTH_TURN_FPA_MODE<aviator/SMOOTH_TURN_FPA_MODE_enum>
    ≔ PITCH_3D_CONTROL_MODE<aviator/PITCH_3D_CONTROL_MODE_enum>
    ≔ REFUEL_DUMP_MODE<aviator/REFUEL_DUMP_MODE_enum>
    ≔ BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE<aviator/BASIC_MANEUVER_GLIDE_SPEED_CONTROL_MODE_enum>
    ≔ TARGET_POSITION_VEL_TYPE<aviator/TARGET_POSITION_VEL_TYPE_enum>
    ≔ EPHEM_SHIFT_ROTATE_ALTITUDE_MODE<aviator/EPHEM_SHIFT_ROTATE_ALTITUDE_MODE_enum>
    ≔ EPHEM_SHIFT_ROTATE_COURSE_MODE<aviator/EPHEM_SHIFT_ROTATE_COURSE_MODE_enum>

