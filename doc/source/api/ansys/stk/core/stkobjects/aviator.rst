
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
              - Do not use this interface, as it is deprecated. Use IARINC424Item instead.

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

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure`
              - Class defining a Relative to Previous Procedure site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteSTKObjectWaypoint`
              - Class defining a STK Object Waypoint site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteSTKStaticObject`
              - Class defining a STK Static Object site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject`
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

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic`
              - Class defining the aerodynamic options for a rotorcraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RotorcraftPropulsion`
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

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionManeuverModeHelper`
              - Class defining the The calculation mode for the Aero/Prop maneuver mode helper. Helper for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel`
              - Class defining the advanced acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAccelerationMode`
              - Class defining the acceleration mode options for an advanced acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftSimpleAerodynamic`
              - Class defining the simple aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftExternalAerodynamic`
              - Class defining the external file aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic`
              - Class defining the aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingAerodynamic`
              - Class defining the basic fixed wing aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion`
              - Class defining the propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftSimplePropulsion`
              - Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftExternalPropulsion`
              - Class defining the external propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingPropulsion`
              - Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ARINC424Source`
              - Class defining an ARINC424 source in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DAFIFSource`
              - Class defining an DAFIF source in the Aviator catalog.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicFixedWingForwardFlightLiftHelper`
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

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothAcceleration`
              - Class defining the smooth accel strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategySmoothTurn`
              - Class defining the smooth turn strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedOptions`
              - Class defining the airspeed options for basic maneuver strategies.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust`
              - Class defining the the thrust propulsion used in basic maneuver procedures.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAutopilotNavigation`
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

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle`
              - Class defining the Relative Flight Path Angle strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeSpeedAltitude`
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

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingExternalAerodynamic`
              - Class defining the External Aero File aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic`
              - Class defining the subsonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic`
              - Class defining the Sub/Super/Hypersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic`
              - Class defining the supersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PerformanceModel`
              - Class defining an unknown performance model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryBasic`
              - Class defining a basic geometry wing in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometryVariable`
              - Class defining a variable geometry wing in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingElectricPowerplant`
              - Class defining an Electric powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingExternalPropulsion`
              - Class defining an External Prop File powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicPropulsion`
              - Class defining a Sub/Super/Hypersonic powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingPistonPowerplant`
              - Class defining a Piston powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingEmpiricalJetEngine`
              - Class defining the Turbojet and Turbofan empirical models in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPowerplant`
              - Do not use this class, as it is deprecated. Use AdvancedFixedWingTurbofanBasicABPropulsion instead.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPowerplant`
              - Do not use this class, as it is deprecated. Use AdvancedFixedWingTurbojetBasicABPropulsion instead.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion`
              - Class defining the Turbofan - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion`
              - Class defining the Turbojet - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbopropPowerplant`
              - Class defining the Turboprop powerplant in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic`
              - Class defining the simple aerodynamic options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileExternalAerodynamic`
              - Class defining the external aerodynamic options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileAdvancedAerodynamic`
              - Class defining the advanced aerodynamic options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileAerodynamic`
              - Class defining the aerodynamic options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissilePropulsion`
              - Class defining the propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileSimplePropulsion`
              - Class defining the Simple propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileExternalPropulsion`
              - Class defining the External propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion`
              - Class defining the Ramjet propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileRocketPropulsion`
              - Class defining the Rocket propulsion options for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion`
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

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState`
              - Class defining a Launch Dyn State procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint`
              - Class defining a Launch Waypoint procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteDynamicState`
              - Class defining a Dyn State site.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPitch3D`
              - Class defining Pitch 3D strategy for a Basic Maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RefuelDumpProperties`
              - Class defining the refuel/dump properties for the current procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions`
              - Class defining fast operations (without error or constraint checks) for time options for the current procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity`
              - Class defining the target position and velocity strategies for basic maneuvers.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange`
              - Class defining the position and velocity strategy, Noisy Bearing Range.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget`
              - Class defining the position and velocity strategy, Noisy Surface Target.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic`
              - Class defining the FourPoint aerodynamic strategy in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic`
              - Class defining the FourPoint aerodynamic strategy in the Missile.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic`
              - Class defining the FourPoint aerodynamic strategy.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ErrorCodes`
              - Error Codes.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ClosureValue`
              - The closure value.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProcedureType`
              - Aviator procedure types.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SiteType`
              - Aviator site types.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategy`
              - Basic maneuver strategy types.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.StraightAheadReferenceFrame`
              - Straight Ahead basic maneuver Reference Frame.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AirspeedType`
              - Airspeed types.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionSimpleMode`
              - Aircraft operating mode for basic acceleration models with aerodynamics set to Simple.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AerodynamicPropulsionFlightMode`
              - Flight mode for the Aero/Prop maneuver mode helper in aircraft acceleration models.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PhaseOfFlight`
              - Flight mode for basic maneuver procedures.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CruiseSpeed`
              - Cruise airspeed type for the procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TakeoffMode`
              - Takeoff procedure mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ApproachMode`
              - Landing procedure approach mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.NavigatorTurnDirection`
              - Turn mode for procedures with Enroute Turn Direction options.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverFuelFlowType`
              - Fuel flow type for basic maneuver procedures.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAltitudeLimit`
              - The type of response Aviator will have if the maneuver attempts to exceed the altitude limit.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RunwayHighLowEnd`
              - Runway heading that the aircraft will use.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverReferenceFrame`
              - Reference frame for the basic maneuver strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyNavigationControlLimit`
              - Define the control limits for the aircraft during the maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AccelerationManeuverMode`
              - The mode that the aircraft will adhere to the specified acceleration parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamicStrategy`
              - The aerodynamic strategy used to compute lift, drag, angle of attack, sideslip and intermediate / derived values.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsionStrategy`
              - The propulsion strategy used to compute thrust and throttle setting.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AGLMSL`
              - The altitude mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LandingApproachFixRangeMode`
              - The reference point on the runway for the Approach Fix Range.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AccelerationAdvancedAccelerationMode`
              - Acceleration mode for aircraft advanced acceleration models.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AccelerationManeuverAerodynamicPropulsionMode`
              - The mode used for the Aero/Prop maneuver mode helper for aircraft basic acceleration models.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyAirspeedPerformanceLimits`
              - The type of response Aviator will have if the basic maneuver attempts to exceed the airspeed limit.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPoweredCruiseMode`
              - Powered Cruise Options.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TurnMode`
              - The mode to specify an aircraft's level turn performance for acceleration performance models.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PointToPointMode`
              - The heading or course of the aircraft at the beginning of the procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AltitudeConstraintManeuverMode`
              - Turn mode for procedures that may require a level off maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.WindModelType`
              - The wind model type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.WindAtmosphereModelSource`
              - The source for the wind or atmosphere model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDSMessageInterpolationType`
              - The interpolation method for the wind conditions.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDSMissingMessageType`
              - The wind effect to apply if there is an interval gap between messages.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDSMessageExtrapolationType`
              - The wind effect to apply if the procedure(s) extend beyond the intervals of any available messages.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ADDSForecastType`
              - The forecast type for the NOAA ADDS message.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelType`
              - The basic atmosphere model type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SmoothTurnMode`
              - The basic maneuver smooth turn mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOverride`
              - The performance model override mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverAirspeedMode`
              - The basic maneuver airspeed mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AileronRollFlightPath`
              - The flight path option for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RollLeftRight`
              - The roll direction for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RollUprightInverted`
              - The orientation for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AileronRollMode`
              - The roll mode aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FlyAOALeftRight`
              - The roll direction for a Fly AOA strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SmoothAccelerationLeftRight`
              - The roll direction for a smooth acceleration strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PullMode`
              - The pull mode for a pull strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RollingPullMode`
              - The rolling pull mode for a rolling pull strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SmoothAccelerationStopConditions`
              - The rolling pull mode for a rolling pull strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AutopilotHorizontalPlaneMode`
              - The autopilot mode for an autopilot - horizontal plane strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AngleMode`
              - The angle mode for a barrel roll strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HoverAltitudeMode`
              - The altitude mode for the lighter than air hover strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HoverHeadingMode`
              - The heading mode for the lighter than air hover strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AutopilotAltitudeMode`
              - The altitude mode for the autopilot - vertical plane strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AutopilotAltitudeControlMode`
              - The altitude control mode for the autopilot - vertical plane strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ClosureMode`
              - The closure mode for guidance strategies of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.InterceptMode`
              - The intercept mode for the intercept strategy of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RendezvousStopCondition`
              - The stop condition options for a rendezvous formation strategy of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FormationFlyerStopCondition`
              - The stop condition options for a Formation Flyer procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ExtEphemFlightMode`
              - Flight mode enums for ExtEphem.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AccelerationPerformanceModelOverride`
              - The acceleration performance model override mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.StationkeepingStopCondition`
              - The stop condition options for a stationkeeping strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TurnDirection`
              - The roll direction for an aileron roll strategy for a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ProfileControlLimit`
              - Define the control limits for a profile strategy of a basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RelativeSpeedAltitudeStopCondition`
              - The stop condition options for a relative speed/altitude strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RelativeAltitudeMode`
              - The relative altitude mode for a relative speed/altitude strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FlyToFlightPathAngleMode`
              - The flight path angle mode mode for a bezier profile strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.PushPull`
              - The option to pull up or push over for a push/pull profile strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AccelerationMode`
              - The acceleration/decelation option for a push/pull profile strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DelayAltitudeMode`
              - The altitude options for a delay procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JoinExitArcMethod`
              - The options to join or exit an arc.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FlightLineProcedureType`
              - The procedure methodology used to calculate the flight line.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TransitionToHoverMode`
              - The type of hover to transition to.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOLRateMode`
              - The rate mode for the VTOL procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HoldingProfileMode`
              - How the aircraft will perform during the holding pattern with respect to airspeed and altitude.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HoldingDirection`
              - The turn direction for the aircraft to enter the holding pattern.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HoldRefuelDumpMode`
              - Define when the aircraft will leave the holding pattern after it has completed refueling or dumping fuel.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HoldingEntryManeuver`
              - Define how the aircraft will enter the holding pattern.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOLTransitionMode`
              - The mode to specify the course of the transition maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOLFinalHeadingMode`
              - The mode to specify the heading at the end of the maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOLTranslationMode`
              - The mode to specify the translation of the VTOL maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOLTranslationFinalCourseMode`
              - The mode to specify the final course of the VTOL maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.HoverMode`
              - The hover mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VTOLHeadingMode`
              - The heading mode for the hover maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.VertLandingMode`
              - The heading mode for a vertical landing maneuver.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LaunchAttitudeMode`
              - The attitude mode for the launch procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.FuelFlowType`
              - The fuel flow type to use for the procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LineOrientation`
              - The orientation for a parallel flight line procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RelativeAbsoluteBearing`
              - The options for a bearing that can be relative or absolute.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicFixedWingPropulsionMode`
              - The option to specify the thrust (jet engines) or power (propellers).

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ClimbSpeedType`
              - The mode to calculate the aircraft's airspeed while climbing for an advanced climb performance model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CruiseMaxPerformanceSpeedType`
              - The method for defining the maximum performance airspeed of the aircraft for an advanced cruise model.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DescentSpeedType`
              - The method for calculating the aircraft's airspeed while descending.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TakeoffLandingSpeedMode`
              - The method for calculating the aircraft's speed upon leaving the ground or at wheels down.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DepartureSpeedMode`
              - The method for calculating the aircraft's airspeed upon leaving the ground.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingAerodynamicStrategy`
              - The aerodynamic strategy for the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingGeometry`
              - The method to define the wing geometry of an aircraft in the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingPowerplantStrategy`
              - The powerplant strategy for the Advanced Fixed Wing Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissileAerodynamicStrategy`
              - The aerodynamic strategy used to compute lift, drag, angle of attack, sideslip and intermediate / derived values.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MissilePropulsionStrategy`
              - The propulsion strategy used to compute thrust and throttle setting.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RotorcraftPowerplantType`
              - The powerplant type for a rotorcraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.MinimizeSiteProcedureTimeDiff`
              - Options for minimizing the time difference between the procedure and site times.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.STKObjectWaypointOffsetMode`
              - The options to offset the site location relative to the STK Object.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SearchPatternCourseMode`
              - The mode to determine the course of the search pattern.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.DelayTurnDirection`
              - Turn mode for procedures with Delay options.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TrajectoryBlendMode`
              - The interpolation mode to determine the aircraft's position and velocity.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ReferenceStatePerformanceMode`
              - The type of motion the aircraft is engaged in at the reference state.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ReferenceStateLongitudinalAccelerationMode`
              - The mode to specify the longitudinal acceleration of the aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ReferenceStateLateralAccelerationMode`
              - The mode to specify the lateral acceleration of the aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ReferenceStateAttitudeMode`
              - The mode to specify the attitude rate of change.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AndOr`
              - The option to specify AND or OR.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JetEngineTechnologyLevel`
              - The technology level of the jet engine.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JetEngineIntakeType`
              - The intake type of the jet engine.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JetEngineTurbineType`
              - The turbine type of the jet engine.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JetEngineExhaustNozzleType`
              - The exhaust nozzle type of the jet engine.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.JetFuelType`
              - The jet fuel type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AFPROPFuelType`
              - The AFPROP fuel type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.CEAFuelType`
              - The CEA fuel type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TurbineMode`
              - The turbine mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RamjetMode`
              - The ramjet mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.ScramjetMode`
              - The scramjet mode for a Sub/Super/Hypersonic powerplant.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AviatorNumericalIntegrator`
              - The numerical integrator to be used for the procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.Ballistic3DControlMode`
              - The control mode used to define the ballistic 3D strategy of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LaunchDynamicStateCoordFrame`
              - The coordinate frame used for a LaunchDynState procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.LaunchDynamicStateBearingReference`
              - The vector used as a bearing reference for a LaunchDynState procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.AltitudeReference`
              - The altitude reference.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.SmoothTurnFlightPathAngleMode`
              - The flight path angle mode for the Smooth Turn strategy of the Basic Maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.Pitch3DControlMode`
              - The control mode used to define the pitch 3D strategy of the basic maneuver procedure.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.RefuelDumpMode`
              - The modes used to define procedure refuel/dump modes.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.BasicManeuverGlideSpeedControlMode`
              - The modes used to define basic maneuver glide speed control modes.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.TargetPositionVelocityType`
              - The target pos/vel type.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.EphemShiftRotateAltitudeMode`
              - Ephem alt mode.

            * - :py:class:`~ansys.stk.core.stkobjects.aviator.EphemShiftRotateCourseMode`
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
     SiteRelativeToPrevProcedure<aviator/SiteRelativeToPrevProcedure>
     SiteSTKObjectWaypoint<aviator/SiteSTKObjectWaypoint>
     SiteSTKStaticObject<aviator/SiteSTKStaticObject>
     SiteRelativeToSTKObject<aviator/SiteRelativeToSTKObject>
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
     RotorcraftAerodynamic<aviator/RotorcraftAerodynamic>
     RotorcraftPropulsion<aviator/RotorcraftPropulsion>
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
     AerodynamicPropulsionManeuverModeHelper<aviator/AerodynamicPropulsionManeuverModeHelper>
     AircraftAdvancedAccelerationModel<aviator/AircraftAdvancedAccelerationModel>
     AircraftAccelerationMode<aviator/AircraftAccelerationMode>
     AircraftSimpleAerodynamic<aviator/AircraftSimpleAerodynamic>
     AircraftExternalAerodynamic<aviator/AircraftExternalAerodynamic>
     AircraftAerodynamic<aviator/AircraftAerodynamic>
     AircraftBasicFixedWingAerodynamic<aviator/AircraftBasicFixedWingAerodynamic>
     AircraftPropulsion<aviator/AircraftPropulsion>
     AircraftSimplePropulsion<aviator/AircraftSimplePropulsion>
     AircraftExternalPropulsion<aviator/AircraftExternalPropulsion>
     AircraftBasicFixedWingPropulsion<aviator/AircraftBasicFixedWingPropulsion>
     ARINC424Source<aviator/ARINC424Source>
     DAFIFSource<aviator/DAFIFSource>
     BasicFixedWingForwardFlightLiftHelper<aviator/BasicFixedWingForwardFlightLiftHelper>
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
     BasicManeuverStrategySmoothAcceleration<aviator/BasicManeuverStrategySmoothAcceleration>
     BasicManeuverStrategySmoothTurn<aviator/BasicManeuverStrategySmoothTurn>
     BasicManeuverAirspeedOptions<aviator/BasicManeuverAirspeedOptions>
     PropulsionThrust<aviator/PropulsionThrust>
     BasicManeuverStrategyAutopilotNavigation<aviator/BasicManeuverStrategyAutopilotNavigation>
     BasicManeuverStrategyAutopilotProf<aviator/BasicManeuverStrategyAutopilotProf>
     BasicManeuverStrategyBarrelRoll<aviator/BasicManeuverStrategyBarrelRoll>
     BasicManeuverStrategyLoop<aviator/BasicManeuverStrategyLoop>
     BasicManeuverStrategyLTAHover<aviator/BasicManeuverStrategyLTAHover>
     BasicManeuverStrategyIntercept<aviator/BasicManeuverStrategyIntercept>
     BasicManeuverStrategyRelativeBearing<aviator/BasicManeuverStrategyRelativeBearing>
     BasicManeuverStrategyRelativeCourse<aviator/BasicManeuverStrategyRelativeCourse>
     BasicManeuverStrategyRendezvous<aviator/BasicManeuverStrategyRendezvous>
     BasicManeuverStrategyStationkeeping<aviator/BasicManeuverStrategyStationkeeping>
     BasicManeuverStrategyRelativeFlightPathAngle<aviator/BasicManeuverStrategyRelativeFlightPathAngle>
     BasicManeuverStrategyRelativeSpeedAltitude<aviator/BasicManeuverStrategyRelativeSpeedAltitude>
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
     AdvancedFixedWingExternalAerodynamic<aviator/AdvancedFixedWingExternalAerodynamic>
     AdvancedFixedWingSubsonicAerodynamic<aviator/AdvancedFixedWingSubsonicAerodynamic>
     AdvancedFixedWingSubSuperHypersonicAerodynamic<aviator/AdvancedFixedWingSubSuperHypersonicAerodynamic>
     AdvancedFixedWingSupersonicAerodynamic<aviator/AdvancedFixedWingSupersonicAerodynamic>
     PerformanceModel<aviator/PerformanceModel>
     AdvancedFixedWingGeometryBasic<aviator/AdvancedFixedWingGeometryBasic>
     AdvancedFixedWingGeometryVariable<aviator/AdvancedFixedWingGeometryVariable>
     AdvancedFixedWingElectricPowerplant<aviator/AdvancedFixedWingElectricPowerplant>
     AdvancedFixedWingExternalPropulsion<aviator/AdvancedFixedWingExternalPropulsion>
     AdvancedFixedWingSubSuperHypersonicPropulsion<aviator/AdvancedFixedWingSubSuperHypersonicPropulsion>
     AdvancedFixedWingPistonPowerplant<aviator/AdvancedFixedWingPistonPowerplant>
     AdvancedFixedWingEmpiricalJetEngine<aviator/AdvancedFixedWingEmpiricalJetEngine>
     AdvancedFixedWingTurbofanBasicABPowerplant<aviator/AdvancedFixedWingTurbofanBasicABPowerplant>
     AdvancedFixedWingTurbojetBasicABPowerplant<aviator/AdvancedFixedWingTurbojetBasicABPowerplant>
     AdvancedFixedWingTurbofanBasicABPropulsion<aviator/AdvancedFixedWingTurbofanBasicABPropulsion>
     AdvancedFixedWingTurbojetBasicABPropulsion<aviator/AdvancedFixedWingTurbojetBasicABPropulsion>
     AdvancedFixedWingTurbopropPowerplant<aviator/AdvancedFixedWingTurbopropPowerplant>
     MissileSimpleAerodynamic<aviator/MissileSimpleAerodynamic>
     MissileExternalAerodynamic<aviator/MissileExternalAerodynamic>
     MissileAdvancedAerodynamic<aviator/MissileAdvancedAerodynamic>
     MissileAerodynamic<aviator/MissileAerodynamic>
     MissilePropulsion<aviator/MissilePropulsion>
     MissileSimplePropulsion<aviator/MissileSimplePropulsion>
     MissileExternalPropulsion<aviator/MissileExternalPropulsion>
     MissileRamjetPropulsion<aviator/MissileRamjetPropulsion>
     MissileRocketPropulsion<aviator/MissileRocketPropulsion>
     MissileTurbojetPropulsion<aviator/MissileTurbojetPropulsion>
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
     ProcedureLaunchDynamicState<aviator/ProcedureLaunchDynamicState>
     ProcedureLaunchWaypoint<aviator/ProcedureLaunchWaypoint>
     SiteDynamicState<aviator/SiteDynamicState>
     BasicManeuverStrategyPitch3D<aviator/BasicManeuverStrategyPitch3D>
     RefuelDumpProperties<aviator/RefuelDumpProperties>
     ProcedureFastTimeOptions<aviator/ProcedureFastTimeOptions>
     BasicManeuverTargetPositionVelocity<aviator/BasicManeuverTargetPositionVelocity>
     BasicManeuverTargetPositionVelocityNoisyBearingRange<aviator/BasicManeuverTargetPositionVelocityNoisyBearingRange>
     BasicManeuverTargetPositionVelocityNoisySurfTarget<aviator/BasicManeuverTargetPositionVelocityNoisySurfTarget>
     AdvancedFixedWingFourPointAerodynamic<aviator/AdvancedFixedWingFourPointAerodynamic>
     MissileFourPointAerodynamic<aviator/MissileFourPointAerodynamic>
     FourPointAerodynamic<aviator/FourPointAerodynamic>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ ErrorCodes<aviator/ErrorCodes>
    ≔ ClosureValue<aviator/ClosureValue>
    ≔ ProcedureType<aviator/ProcedureType>
    ≔ SiteType<aviator/SiteType>
    ≔ BasicManeuverStrategy<aviator/BasicManeuverStrategy>
    ≔ StraightAheadReferenceFrame<aviator/StraightAheadReferenceFrame>
    ≔ AirspeedType<aviator/AirspeedType>
    ≔ AerodynamicPropulsionSimpleMode<aviator/AerodynamicPropulsionSimpleMode>
    ≔ AerodynamicPropulsionFlightMode<aviator/AerodynamicPropulsionFlightMode>
    ≔ PhaseOfFlight<aviator/PhaseOfFlight>
    ≔ CruiseSpeed<aviator/CruiseSpeed>
    ≔ TakeoffMode<aviator/TakeoffMode>
    ≔ ApproachMode<aviator/ApproachMode>
    ≔ NavigatorTurnDirection<aviator/NavigatorTurnDirection>
    ≔ BasicManeuverFuelFlowType<aviator/BasicManeuverFuelFlowType>
    ≔ BasicManeuverAltitudeLimit<aviator/BasicManeuverAltitudeLimit>
    ≔ RunwayHighLowEnd<aviator/RunwayHighLowEnd>
    ≔ BasicManeuverReferenceFrame<aviator/BasicManeuverReferenceFrame>
    ≔ BasicManeuverStrategyNavigationControlLimit<aviator/BasicManeuverStrategyNavigationControlLimit>
    ≔ AccelerationManeuverMode<aviator/AccelerationManeuverMode>
    ≔ AircraftAerodynamicStrategy<aviator/AircraftAerodynamicStrategy>
    ≔ AircraftPropulsionStrategy<aviator/AircraftPropulsionStrategy>
    ≔ AGLMSL<aviator/AGLMSL>
    ≔ LandingApproachFixRangeMode<aviator/LandingApproachFixRangeMode>
    ≔ AccelerationAdvancedAccelerationMode<aviator/AccelerationAdvancedAccelerationMode>
    ≔ AccelerationManeuverAerodynamicPropulsionMode<aviator/AccelerationManeuverAerodynamicPropulsionMode>
    ≔ BasicManeuverStrategyAirspeedPerformanceLimits<aviator/BasicManeuverStrategyAirspeedPerformanceLimits>
    ≔ BasicManeuverStrategyPoweredCruiseMode<aviator/BasicManeuverStrategyPoweredCruiseMode>
    ≔ TurnMode<aviator/TurnMode>
    ≔ PointToPointMode<aviator/PointToPointMode>
    ≔ AltitudeConstraintManeuverMode<aviator/AltitudeConstraintManeuverMode>
    ≔ WindModelType<aviator/WindModelType>
    ≔ WindAtmosphereModelSource<aviator/WindAtmosphereModelSource>
    ≔ ADDSMessageInterpolationType<aviator/ADDSMessageInterpolationType>
    ≔ ADDSMissingMessageType<aviator/ADDSMissingMessageType>
    ≔ ADDSMessageExtrapolationType<aviator/ADDSMessageExtrapolationType>
    ≔ ADDSForecastType<aviator/ADDSForecastType>
    ≔ AtmosphereModelType<aviator/AtmosphereModelType>
    ≔ SmoothTurnMode<aviator/SmoothTurnMode>
    ≔ PerformanceModelOverride<aviator/PerformanceModelOverride>
    ≔ BasicManeuverAirspeedMode<aviator/BasicManeuverAirspeedMode>
    ≔ AileronRollFlightPath<aviator/AileronRollFlightPath>
    ≔ RollLeftRight<aviator/RollLeftRight>
    ≔ RollUprightInverted<aviator/RollUprightInverted>
    ≔ AileronRollMode<aviator/AileronRollMode>
    ≔ FlyAOALeftRight<aviator/FlyAOALeftRight>
    ≔ SmoothAccelerationLeftRight<aviator/SmoothAccelerationLeftRight>
    ≔ PullMode<aviator/PullMode>
    ≔ RollingPullMode<aviator/RollingPullMode>
    ≔ SmoothAccelerationStopConditions<aviator/SmoothAccelerationStopConditions>
    ≔ AutopilotHorizontalPlaneMode<aviator/AutopilotHorizontalPlaneMode>
    ≔ AngleMode<aviator/AngleMode>
    ≔ HoverAltitudeMode<aviator/HoverAltitudeMode>
    ≔ HoverHeadingMode<aviator/HoverHeadingMode>
    ≔ AutopilotAltitudeMode<aviator/AutopilotAltitudeMode>
    ≔ AutopilotAltitudeControlMode<aviator/AutopilotAltitudeControlMode>
    ≔ ClosureMode<aviator/ClosureMode>
    ≔ InterceptMode<aviator/InterceptMode>
    ≔ RendezvousStopCondition<aviator/RendezvousStopCondition>
    ≔ FormationFlyerStopCondition<aviator/FormationFlyerStopCondition>
    ≔ ExtEphemFlightMode<aviator/ExtEphemFlightMode>
    ≔ AccelerationPerformanceModelOverride<aviator/AccelerationPerformanceModelOverride>
    ≔ StationkeepingStopCondition<aviator/StationkeepingStopCondition>
    ≔ TurnDirection<aviator/TurnDirection>
    ≔ ProfileControlLimit<aviator/ProfileControlLimit>
    ≔ RelativeSpeedAltitudeStopCondition<aviator/RelativeSpeedAltitudeStopCondition>
    ≔ RelativeAltitudeMode<aviator/RelativeAltitudeMode>
    ≔ FlyToFlightPathAngleMode<aviator/FlyToFlightPathAngleMode>
    ≔ PushPull<aviator/PushPull>
    ≔ AccelerationMode<aviator/AccelerationMode>
    ≔ DelayAltitudeMode<aviator/DelayAltitudeMode>
    ≔ JoinExitArcMethod<aviator/JoinExitArcMethod>
    ≔ FlightLineProcedureType<aviator/FlightLineProcedureType>
    ≔ TransitionToHoverMode<aviator/TransitionToHoverMode>
    ≔ VTOLRateMode<aviator/VTOLRateMode>
    ≔ HoldingProfileMode<aviator/HoldingProfileMode>
    ≔ HoldingDirection<aviator/HoldingDirection>
    ≔ HoldRefuelDumpMode<aviator/HoldRefuelDumpMode>
    ≔ HoldingEntryManeuver<aviator/HoldingEntryManeuver>
    ≔ VTOLTransitionMode<aviator/VTOLTransitionMode>
    ≔ VTOLFinalHeadingMode<aviator/VTOLFinalHeadingMode>
    ≔ VTOLTranslationMode<aviator/VTOLTranslationMode>
    ≔ VTOLTranslationFinalCourseMode<aviator/VTOLTranslationFinalCourseMode>
    ≔ HoverMode<aviator/HoverMode>
    ≔ VTOLHeadingMode<aviator/VTOLHeadingMode>
    ≔ VertLandingMode<aviator/VertLandingMode>
    ≔ LaunchAttitudeMode<aviator/LaunchAttitudeMode>
    ≔ FuelFlowType<aviator/FuelFlowType>
    ≔ LineOrientation<aviator/LineOrientation>
    ≔ RelativeAbsoluteBearing<aviator/RelativeAbsoluteBearing>
    ≔ BasicFixedWingPropulsionMode<aviator/BasicFixedWingPropulsionMode>
    ≔ ClimbSpeedType<aviator/ClimbSpeedType>
    ≔ CruiseMaxPerformanceSpeedType<aviator/CruiseMaxPerformanceSpeedType>
    ≔ DescentSpeedType<aviator/DescentSpeedType>
    ≔ TakeoffLandingSpeedMode<aviator/TakeoffLandingSpeedMode>
    ≔ DepartureSpeedMode<aviator/DepartureSpeedMode>
    ≔ AdvancedFixedWingAerodynamicStrategy<aviator/AdvancedFixedWingAerodynamicStrategy>
    ≔ AdvancedFixedWingGeometry<aviator/AdvancedFixedWingGeometry>
    ≔ AdvancedFixedWingPowerplantStrategy<aviator/AdvancedFixedWingPowerplantStrategy>
    ≔ MissileAerodynamicStrategy<aviator/MissileAerodynamicStrategy>
    ≔ MissilePropulsionStrategy<aviator/MissilePropulsionStrategy>
    ≔ RotorcraftPowerplantType<aviator/RotorcraftPowerplantType>
    ≔ MinimizeSiteProcedureTimeDiff<aviator/MinimizeSiteProcedureTimeDiff>
    ≔ STKObjectWaypointOffsetMode<aviator/STKObjectWaypointOffsetMode>
    ≔ SearchPatternCourseMode<aviator/SearchPatternCourseMode>
    ≔ DelayTurnDirection<aviator/DelayTurnDirection>
    ≔ TrajectoryBlendMode<aviator/TrajectoryBlendMode>
    ≔ ReferenceStatePerformanceMode<aviator/ReferenceStatePerformanceMode>
    ≔ ReferenceStateLongitudinalAccelerationMode<aviator/ReferenceStateLongitudinalAccelerationMode>
    ≔ ReferenceStateLateralAccelerationMode<aviator/ReferenceStateLateralAccelerationMode>
    ≔ ReferenceStateAttitudeMode<aviator/ReferenceStateAttitudeMode>
    ≔ AndOr<aviator/AndOr>
    ≔ JetEngineTechnologyLevel<aviator/JetEngineTechnologyLevel>
    ≔ JetEngineIntakeType<aviator/JetEngineIntakeType>
    ≔ JetEngineTurbineType<aviator/JetEngineTurbineType>
    ≔ JetEngineExhaustNozzleType<aviator/JetEngineExhaustNozzleType>
    ≔ JetFuelType<aviator/JetFuelType>
    ≔ AFPROPFuelType<aviator/AFPROPFuelType>
    ≔ CEAFuelType<aviator/CEAFuelType>
    ≔ TurbineMode<aviator/TurbineMode>
    ≔ RamjetMode<aviator/RamjetMode>
    ≔ ScramjetMode<aviator/ScramjetMode>
    ≔ AviatorNumericalIntegrator<aviator/AviatorNumericalIntegrator>
    ≔ Ballistic3DControlMode<aviator/Ballistic3DControlMode>
    ≔ LaunchDynamicStateCoordFrame<aviator/LaunchDynamicStateCoordFrame>
    ≔ LaunchDynamicStateBearingReference<aviator/LaunchDynamicStateBearingReference>
    ≔ AltitudeReference<aviator/AltitudeReference>
    ≔ SmoothTurnFlightPathAngleMode<aviator/SmoothTurnFlightPathAngleMode>
    ≔ Pitch3DControlMode<aviator/Pitch3DControlMode>
    ≔ RefuelDumpMode<aviator/RefuelDumpMode>
    ≔ BasicManeuverGlideSpeedControlMode<aviator/BasicManeuverGlideSpeedControlMode>
    ≔ TargetPositionVelocityType<aviator/TargetPositionVelocityType>
    ≔ EphemShiftRotateAltitudeMode<aviator/EphemShiftRotateAltitudeMode>
    ≔ EphemShiftRotateCourseMode<aviator/EphemShiftRotateCourseMode>

